# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl>=3.1", "pytest>=7.0"]
# ///
"""Tests for idfa_ops.py and idfa_audit.py using fixture workbooks."""

import json
import shutil
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import openpyxl
import pytest

# Paths
FIXTURES_DIR = Path(__file__).parent / "fixtures"
SCRIPTS_DIR = Path(__file__).parent.parent / "skills" / "idfa-ops" / "scripts"
COMPLIANT = FIXTURES_DIR / "gp_waterfall_compliant.xlsx"
VIOLATIONS = FIXTURES_DIR / "gp_waterfall_violations.xlsx"

# Import scripts as modules
sys.path.insert(0, str(SCRIPTS_DIR))
import idfa_audit
import idfa_ops


@pytest.fixture
def compliant_copy(tmp_path):
    dest = tmp_path / "compliant.xlsx"
    shutil.copy2(COMPLIANT, dest)
    return str(dest)


@pytest.fixture
def violations_copy(tmp_path):
    dest = tmp_path / "violations.xlsx"
    shutil.copy2(VIOLATIONS, dest)
    return str(dest)


def _run_ops(args: list[str]) -> dict:
    """Run idfa_ops.py as a subprocess and parse JSON output."""
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "idfa_ops.py")] + args,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout), result.returncode


class TestWriteAssumption:
    def test_write_assumption(self, compliant_copy):
        """Write a Named Range value, reload file, confirm value persists."""
        idfa_ops.cmd_write(compliant_copy, "Inp_Rev_Y1", "15000000")
        wb = openpyxl.load_workbook(compliant_copy)
        dest = idfa_ops._resolve_named_range(wb, "Inp_Rev_Y1")
        assert dest is not None
        sheet, cell = dest
        assert wb[sheet][cell].value == 15_000_000


class TestReadOutput:
    def test_read_output(self, compliant_copy, capsys):
        """Read a known Named Range value from the compliant model."""
        idfa_ops.cmd_read(compliant_copy, ["Inp_Rev_Y1"])
        output = json.loads(capsys.readouterr().out)
        assert output["status"] == "ok"
        assert output["values"]["Inp_Rev_Y1"] == 10_000_000


class TestInspectModel:
    def test_inspect_model(self, compliant_copy, capsys):
        """Inspect model — confirm all Named Ranges are listed."""
        idfa_ops.cmd_inspect(compliant_copy)
        output = json.loads(capsys.readouterr().out)
        assert output["status"] == "ok"
        names = {r["name"] for r in output["named_ranges"]}
        expected = {
            "Inp_Rev_Y1",
            "Inp_Rev_Growth",
            "Inp_COGS_Pct_Y1",
            "Inp_COGS_Efficiency",
            "Revenue_Y1",
            "Revenue_Y2",
            "Revenue_Y3",
            "COGS_Pct_Y1",
            "COGS_Pct_Y2",
            "COGS_Pct_Y3",
            "COGS_Y1",
            "COGS_Y2",
            "COGS_Y3",
            "Gross_Profit_Y1",
            "Gross_Profit_Y2",
            "Gross_Profit_Y3",
        }
        assert expected.issubset(names)


class TestReadFormula:
    def test_read_formula(self, compliant_copy, capsys):
        """Read formula text for a Named Range — confirm formula string matches."""
        idfa_ops.cmd_formula(compliant_copy, "Revenue_Y2")
        output = json.loads(capsys.readouterr().out)
        assert output["status"] == "ok"
        assert output["formula"] == "=Revenue_Y1*(1+Inp_Rev_Growth)"


class TestCreateNamedRange:
    def test_create_named_range(self, compliant_copy):
        """Create a new Named Range, confirm it exists in workbook."""
        idfa_ops.cmd_create_range(compliant_copy, "Test_Range", "Assumptions", "A1")
        wb = openpyxl.load_workbook(compliant_copy)
        dest = idfa_ops._resolve_named_range(wb, "Test_Range")
        assert dest is not None
        assert dest[0] == "Assumptions"


class TestWriteReadRoundtrip:
    def test_write_read_roundtrip(self, compliant_copy, capsys):
        """Write value then read back — confirm match."""
        idfa_ops.cmd_write(compliant_copy, "Inp_Rev_Y1", "20000000")
        idfa_ops.cmd_read(compliant_copy, ["Inp_Rev_Y1"])
        output = json.loads(capsys.readouterr().out.strip().split("\n")[-1])
        assert output["values"]["Inp_Rev_Y1"] == 20_000_000


class TestAuditPassingModel:
    def test_audit_passing_model(self, compliant_copy):
        """Audit a compliant model — all guardrails PASS."""
        result = idfa_audit.audit(compliant_copy)
        assert result["guardrail_1_named_ranges"]["status"] == "PASS"
        assert result["guardrail_3_intent_notes"]["status"] == "PASS"
        assert result["guardrail_4_layer_isolation"]["status"] == "PASS"
        assert result["overall"] == "PASS"


class TestAuditFailingModel:
    def test_audit_failing_model(self, violations_copy):
        """Audit violations model — correct violations detected."""
        result = idfa_audit.audit(violations_copy)
        # Guardrail 1: coordinate refs (=B2*1.10)
        assert result["guardrail_1_named_ranges"]["status"] == "FAIL"
        assert result["guardrail_1_named_ranges"]["violations"] >= 1
        # Guardrail 3: missing Intent Note on Gross_Profit_Y2
        assert result["guardrail_3_intent_notes"]["status"] == "FAIL"
        # Guardrail 4: hardcoded 0.60 in COGS_Y1
        assert result["guardrail_4_layer_isolation"]["status"] == "FAIL"
        assert result["guardrail_4_layer_isolation"]["violations"] >= 1
        assert result["overall"] == "FAIL"


class TestAuditCoordinateDetection:
    def test_audit_coordinate_detection(self, violations_copy):
        """Formulas with =B2*1.10 flagged; formulas with Named Ranges pass."""
        result = idfa_audit.audit(violations_copy)
        coord_details = result["guardrail_1_named_ranges"]["details"]
        # Find the B2*1.10 violation
        flagged_formulas = [d["formula"] for d in coord_details]
        assert any("B2" in f for f in flagged_formulas)
        # Compliant formulas should NOT be in violations
        assert not any("Revenue_Y1*(1+Inp_Rev_Growth)" in f for f in flagged_formulas)


class TestNamedRangeNotFound:
    def test_named_range_not_found(self, compliant_copy):
        """Write/read non-existent Named Range — exit code 1, clear error."""
        output, code = _run_ops(["read", compliant_copy, "Nonexistent_Range"])
        assert code == 1
        assert "error" in output
        assert "not found" in output["error"].lower()


class TestRecalcNoLibreOffice:
    def test_recalc_no_libreoffice(self, compliant_copy):
        """When LibreOffice not installed — graceful error, not crash."""
        import recalc_bridge

        with (
            patch.object(recalc_bridge, "_find_xlsx_recalc", return_value=None),
            patch.object(recalc_bridge, "_find_libreoffice", return_value=None),
        ):
            result = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "recalc_bridge.py"), compliant_copy],
                capture_output=True,
                text=True,
                env={
                    **__import__("os").environ,
                    "PYTHONPATH": "",
                },  # Don't let cached modules interfere
            )
            assert result.returncode == 1
            output = json.loads(result.stdout)
            assert output["status"] == "error"
            assert "recalculation engine" in output["message"].lower()
