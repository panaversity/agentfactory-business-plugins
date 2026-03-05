# /// script
# dependencies = []
# ///
"""
Islamic Finance Plugin — Eval Runner
Run: uv run evals/run-evals.py

Validates that golden files exist and have expected structure.
Does NOT run actual LLM inference — that requires the plugin installed.
"""

import json
import sys
from pathlib import Path


def validate_routing_golden(path: Path) -> list[str]:
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 13:
        errors.append(f"routing-golden.json: expected 13+ cases, got {len(cases)}")
    required_fields = [
        "jurisdiction",
        "query",
        "expected_framework",
        "expected_income_label",
        "expected_key_disclosure",
    ]
    for i, c in enumerate(cases):
        for f in required_fields:
            if f not in c:
                errors.append(f"routing-golden.json case {i}: missing field '{f}'")
    jurisdictions = {c["jurisdiction"] for c in cases}
    expected = {
        "Bahrain",
        "Qatar",
        "Malaysia",
        "Saudi Arabia",
        "UAE",
        "UK",
        "Kuwait",
        "Oman",
        "Pakistan",
        "Indonesia",
        "Nigeria",
        "Turkey",
        "GCC Cross-Border",
    }
    missing = expected - jurisdictions
    if missing:
        errors.append(f"routing-golden.json: missing jurisdictions: {missing}")
    return errors


def validate_product_golden(path: Path) -> list[str]:
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 3:
        errors.append(f"product-golden.json: expected 3+ cases, got {len(cases)}")
    required_fields = [
        "product",
        "jurisdiction",
        "scenario",
        "expected_contains",
        "must_not_contain",
    ]
    for i, c in enumerate(cases):
        for f in required_fields:
            if f not in c:
                errors.append(f"product-golden.json case {i}: missing field '{f}'")
    return errors


def main():
    eval_dir = Path(__file__).parent
    all_errors = []

    routing = eval_dir / "routing-golden.json"
    if routing.exists():
        all_errors.extend(validate_routing_golden(routing))
        print(f"routing-golden.json: {len(json.loads(routing.read_text()))} cases")
    else:
        all_errors.append("routing-golden.json not found")

    product = eval_dir / "product-golden.json"
    if product.exists():
        all_errors.extend(validate_product_golden(product))
        print(f"product-golden.json: {len(json.loads(product.read_text()))} cases")
    else:
        all_errors.append("product-golden.json not found")

    if all_errors:
        print(f"\nFAILED: {len(all_errors)} errors:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("\nPASSED: All golden files valid.")


if __name__ == "__main__":
    main()
