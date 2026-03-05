# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Recalculation bridge — triggers LibreOffice headless recalculation.

Usage:
    uv run recalc_bridge.py <file>

Delegates to the xlsx skill's recalc.py if found, otherwise runs its own
LibreOffice Basic macro. Zero Python dependencies.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

XLSX_SKILL_RECALC_PATHS = [
    Path.home() / ".claude" / "skills" / "xlsx" / "scripts" / "recalc.py",
    Path.home() / ".claude" / "plugins" / "xlsx" / "scripts" / "recalc.py",
]

MACRO_TEMPLATE = """\
Sub RecalculateAndSave
    Dim oDoc As Object
    Dim sURL As String
    sURL = ConvertToURL("{file_path}")
    oDoc = StarDesktop.loadComponentFromURL(sURL, "_blank", 0, Array())
    oDoc.calculateAll()
    oDoc.store()
    oDoc.close(True)
End Sub
"""


def _find_xlsx_recalc() -> Path | None:
    for p in XLSX_SKILL_RECALC_PATHS:
        if p.exists():
            return p
    return None


def _find_libreoffice() -> str | None:
    soffice = shutil.which("soffice")
    if soffice:
        return soffice
    # macOS common paths
    mac_paths = [
        "/Applications/LibreOffice.app/Contents/MacOS/soffice",
        os.path.expanduser("~/Applications/LibreOffice.app/Contents/MacOS/soffice"),
    ]
    for p in mac_paths:
        if os.path.isfile(p):
            return p
    return None


def recalc_via_xlsx_skill(recalc_py: Path, file: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(recalc_py), file],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode == 0:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return {
                "status": "ok",
                "recalculated": True,
                "delegate": "xlsx-skill",
                "raw": result.stdout.strip(),
            }
    return {"status": "error", "message": result.stderr.strip(), "delegate": "xlsx-skill"}


def recalc_via_libreoffice(soffice: str, file: str) -> dict:
    abs_path = str(Path(file).resolve())

    with tempfile.NamedTemporaryFile(mode="w", suffix=".bas", delete=False) as f:
        f.write(MACRO_TEMPLATE.replace("{file_path}", abs_path))
        macro_path = f.name

    try:
        result = subprocess.run(
            [soffice, "--headless", "--invisible", "--calc", f"macro:///{macro_path}"],
            capture_output=True,
            text=True,
            timeout=120,
        )

        # Fallback: if macro execution is tricky, just open and save
        if result.returncode != 0:
            result = subprocess.run(
                [
                    soffice,
                    "--headless",
                    "--calc",
                    "--convert-to",
                    "xlsx",
                    "--outdir",
                    str(Path(abs_path).parent),
                    abs_path,
                ],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode == 0:
                return {"status": "ok", "recalculated": True, "method": "libreoffice-convert"}
            return {"status": "error", "message": result.stderr.strip(), "method": "libreoffice"}

        return {"status": "ok", "recalculated": True, "method": "libreoffice-macro"}
    finally:
        os.unlink(macro_path)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: recalc_bridge.py <file>", file=sys.stderr)
        sys.exit(2)

    file = sys.argv[1]
    if not Path(file).exists():
        print(json.dumps({"error": f"File not found: {file}"}))
        sys.exit(2)

    # Strategy 1: Delegate to xlsx skill's recalc.py
    xlsx_recalc = _find_xlsx_recalc()
    if xlsx_recalc:
        result = recalc_via_xlsx_skill(xlsx_recalc, file)
        print(json.dumps(result))
        sys.exit(0 if result.get("status") == "ok" else 1)

    # Strategy 2: Own LibreOffice execution
    soffice = _find_libreoffice()
    if soffice:
        result = recalc_via_libreoffice(soffice, file)
        print(json.dumps(result))
        sys.exit(0 if result.get("status") == "ok" else 1)

    # No recalc engine available
    print(
        json.dumps(
            {
                "status": "error",
                "message": (
                    "No recalculation engine found. Install one of:\n"
                    "  1. Anthropic's xlsx skill (recommended): provides recalc.py\n"
                    "  2. LibreOffice (brew install --cask libreoffice)\n"
                    "Without a recalc engine, the Write-Recalculate-Read pattern cannot\n"
                    "complete. You can still write assumptions and read cached values."
                ),
            }
        )
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
