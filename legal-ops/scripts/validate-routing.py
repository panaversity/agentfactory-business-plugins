# /// script
# dependencies = []
# ///
"""
Legal Ops Plugin -- Routing Validation Test Harness
Run: uv run scripts/validate-routing.py

Prints 12 routing test queries with expected outputs.
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
    print("Legal Ops Plugin -- Routing Validation")
    print("=" * 60)
    print(f"Total test cases: {len(cases)}\n")
    for i, c in enumerate(cases, 1):
        print(f"Test {i:02d}: {c['expected_product_skill']} | {c['expected_jurisdiction']}")
        print(f"  Query:    {c['query']}")
        print(
            f"  Expected: skill={c['expected_product_skill']}, "
            f"jurisdiction={c['expected_jurisdiction']}, "
            f"overlay={c['expected_overlay']}"
        )
        print(f"  Must contain:     {c['expected_contains']}")
        print(f"  Must NOT contain: {c['must_not_contain']}\n")
    print("Run each query through your installed plugin.")
    print("Compare output against expected values.")
    print("PASS = correct skill routed, correct jurisdiction loaded,")
    print("       expected terms present, forbidden terms absent.")


if __name__ == "__main__":
    main()
