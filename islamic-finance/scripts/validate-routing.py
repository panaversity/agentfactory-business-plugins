# /// script
# dependencies = []
# ///
"""
Islamic Finance Plugin — Routing Validation Test Harness
Run: uv run scripts/validate-routing.py

Prints 13 jurisdiction test queries with expected outputs.
Student runs each query through the installed plugin and
compares agent output against expected values.
"""

import json
import sys
from pathlib import Path


def main():
    golden = Path(__file__).parent.parent / "evals" / "routing-golden.json"
    if not golden.exists():
        print(f"Error: {golden} not found", file=sys.stderr)
        sys.exit(1)
    cases = json.loads(golden.read_text())
    print("Islamic Finance Plugin — Routing Validation")
    print("=" * 60)
    print(f"Total test cases: {len(cases)}\n")
    for i, c in enumerate(cases, 1):
        print(f"Test {i:02d}: {c['jurisdiction']}")
        print(f"  Query:    {c['query']}")
        print(
            f"  Expected: framework={c['expected_framework']}, "
            f"income_label={c['expected_income_label']}, "
            f"disclosure={c['expected_key_disclosure']}\n"
        )
    print("Run each query through your installed plugin.")
    print("Compare output against expected values. PASS = all 3 match.")


if __name__ == "__main__":
    main()
