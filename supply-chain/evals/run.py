# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Supply Chain Eval Harness -- deterministic routing and content checks.

Tier 1: Deterministic checks (routing accuracy, content presence, formula verification)
Tier 2: LLM judges via `claude -p` headless (optional, for domain accuracy)

Usage:
    uv run evals/run.py                          # full eval, all cases
    uv run evals/run.py --case route_vendor_assess_strategic  # single case
    uv run evals/run.py --category routing        # all routing tests
    uv run evals/run.py --list                    # list all cases
    uv run evals/run.py --verbose                 # real-time output
"""

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent  # supply-chain/ root
EVALS_DIR = Path(__file__).resolve().parent
RESULTS_DIR = EVALS_DIR / "results"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def log(msg: str, verbose: bool = True) -> None:
    if verbose:
        print(f"  {msg}", file=sys.stderr)


def load_cases(path: Path) -> list[dict]:
    with open(path) as f:
        data = yaml.safe_load(f)
    return data["cases"]


def run_claude(prompt: str, timeout: int = 180) -> str:
    """Run a prompt through claude CLI and capture output."""
    cmd = [
        "claude",
        "-p",
        prompt,
        "--plugin-dir",
        str(ROOT),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "[TIMEOUT]"
    except FileNotFoundError:
        return "[CLAUDE_NOT_FOUND]"


# ---------------------------------------------------------------------------
# Tier 1 -- Deterministic checks
# ---------------------------------------------------------------------------


def check_content(output: str, checks: list[str]) -> dict:
    """Check that expected content strings appear in output.

    Supports pipe-separated alternatives: "outside|beyond|not within"
    means ANY of those substrings matching counts as a pass.
    """
    results = {}
    output_lower = output.lower()
    for check in checks:
        alternatives = [alt.strip().lower() for alt in check.split("|")]
        results[check] = any(alt in output_lower for alt in alternatives)
    return results


def check_routing(
    output: str, expected_skill: str | None, alternatives: list[str] | None = None
) -> bool:
    """Check that the correct skill was referenced in the output.

    Checks for the skill name (with hyphens as spaces) in the output.
    Also checks any routing_alternatives provided in the case.
    """
    if expected_skill is None:
        return True
    output_normalised = output.lower().replace("-", " ")
    if expected_skill.lower().replace("-", " ") in output_normalised:
        return True
    if alternatives:
        return any(alt.lower() in output_normalised for alt in alternatives)
    return False


def check_formula(output: str, expected_answer: str | None, tolerance: float = 0) -> bool:
    """Check that a numeric answer appears in the output."""
    if expected_answer is None:
        return True
    try:
        expected = float(expected_answer)
        # Search for the number in the output
        import re

        numbers = re.findall(r"[\d,]+\.?\d*", output)
        for num_str in numbers:
            try:
                found = float(num_str.replace(",", ""))
                if abs(found - expected) <= tolerance:
                    return True
            except ValueError:
                continue
        return False
    except ValueError:
        # Non-numeric expected answer -- check string presence
        return expected_answer.lower() in output.lower()


# ---------------------------------------------------------------------------
# Run a single case
# ---------------------------------------------------------------------------


def run_case(case: dict, verbose: bool = False) -> dict:
    """Run a single eval case and return results."""
    case_id = case["id"]
    category = case.get("category", "unknown")
    prompt = case.get("prompt", "")

    log(f"Running: {case_id} ({category})", verbose)

    # Skip cases without prompts (programmatic tests)
    if not prompt:
        return {"id": case_id, "status": "skipped", "reason": "no prompt"}

    # Run through claude (retry once on empty output or timeout)
    output = run_claude(prompt)

    if output in ("[TIMEOUT]", "[CLAUDE_NOT_FOUND]", ""):
        log(f"  Retrying {case_id} (got: {output or 'empty'})", verbose)
        output = run_claude(prompt)

    if output in ("[TIMEOUT]", "[CLAUDE_NOT_FOUND]"):
        return {"id": case_id, "status": "error", "reason": output}

    if not output:
        return {"id": case_id, "status": "error", "reason": "[EMPTY_OUTPUT]"}

    # Tier 1 checks
    results = {"id": case_id, "category": category, "checks": {}}

    # Content checks
    content_checks = case.get("content_checks", [])
    if content_checks:
        content_results = check_content(output, content_checks)
        results["checks"]["content"] = content_results
        results["content_pass"] = all(content_results.values())

    # Routing check
    expected_skill = case.get("expected_skill")
    if expected_skill:
        routing_alts = case.get("routing_alternatives")
        results["checks"]["routing"] = check_routing(output, expected_skill, routing_alts)

    # Formula check
    expected_answer = case.get("expected_answer")
    if expected_answer:
        tolerance = case.get("tolerance", 0)
        results["checks"]["formula"] = check_formula(output, expected_answer, tolerance)

    # Overall pass/fail
    all_checks = []
    for key, val in results["checks"].items():
        if isinstance(val, dict):
            all_checks.extend(val.values())
        elif isinstance(val, bool):
            all_checks.append(val)

    results["status"] = "pass" if all(all_checks) else "fail"
    results["output_preview"] = output[:500] if verbose else output[:200]

    log(f"  Result: {results['status']}", verbose)
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Supply Chain Eval Harness")
    parser.add_argument("--case", help="Run a single case by ID")
    parser.add_argument("--category", help="Run all cases in a category")
    parser.add_argument("--list", action="store_true", help="List all cases")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--dry-run", action="store_true", help="Show cases without running")
    args = parser.parse_args()

    cases = load_cases(EVALS_DIR / "cases.yaml")

    # List mode
    if args.list:
        for case in cases:
            print(f"  {case['id']} ({case.get('category', 'unknown')})")
        print(f"\nTotal: {len(cases)} cases")
        return

    # Filter cases
    if args.case:
        cases = [c for c in cases if c["id"] == args.case]
        if not cases:
            print(f"Case '{args.case}' not found.", file=sys.stderr)
            sys.exit(1)
    elif args.category:
        cases = [c for c in cases if c.get("category") == args.category]
        if not cases:
            print(f"No cases in category '{args.category}'.", file=sys.stderr)
            sys.exit(1)

    if args.dry_run:
        for case in cases:
            print(f"  {case['id']} ({case.get('category', 'unknown')})")
        print(f"\nTotal: {len(cases)} cases")
        return

    # Run cases
    print(f"\nSupply Chain Eval Harness -- {len(cases)} cases", file=sys.stderr)
    print(f"{'=' * 60}", file=sys.stderr)

    results = []
    for case in cases:
        result = run_case(case, verbose=args.verbose)
        results.append(result)

    # Summary
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = sum(1 for r in results if r["status"] == "fail")
    errors = sum(1 for r in results if r["status"] == "error")
    skipped = sum(1 for r in results if r["status"] == "skipped")

    print(f"\n{'=' * 60}", file=sys.stderr)
    print(
        f"Results: {passed} passed, {failed} failed, {errors} errors, {skipped} skipped",
        file=sys.stderr,
    )

    # Save results
    RESULTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    results_path = RESULTS_DIR / f"eval_{timestamp}.json"
    with open(results_path, "w") as f:
        json.dump({"timestamp": timestamp, "results": results}, f, indent=2)
    print(f"Results saved: {results_path}", file=sys.stderr)

    # Exit code
    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
