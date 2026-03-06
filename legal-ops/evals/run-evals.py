# /// script
# dependencies = []
# ///
"""
Legal Ops Plugin -- Eval Runner
Run: uv run evals/run-evals.py

Validates that golden files exist and have expected structure.
Does NOT run actual LLM inference -- that requires the plugin installed.
"""

import json
import sys
from pathlib import Path


def validate_routing_golden(path: Path) -> list[str]:
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 10:
        errors.append(f"routing-golden.json: expected 10+ cases, got {len(cases)}")
    required_fields = [
        "query",
        "expected_product_skill",
        "expected_jurisdiction",
        "expected_overlay",
        "expected_contains",
        "must_not_contain",
    ]
    for i, c in enumerate(cases):
        for f in required_fields:
            if f not in c:
                errors.append(f"routing-golden.json case {i}: missing field '{f}'")
    # Verify all 8 product skills are covered
    skills = {c["expected_product_skill"] for c in cases}
    expected_skills = {
        "contract-review",
        "nda-triage",
        "ip-protection",
        "regulatory-monitoring",
        "dsar-privacy",
        "legal-spend",
        "compliance-calendar",
        "contract-intake-agent",
    }
    missing_skills = expected_skills - skills
    if missing_skills:
        errors.append(f"routing-golden.json: missing product skills: {missing_skills}")
    # Verify all 5 jurisdictions are covered
    jurisdictions = {c["expected_jurisdiction"] for c in cases}
    expected_jurisdictions = {"UK", "EU", "US", "Pakistan", "UAE"}
    missing_jurisdictions = expected_jurisdictions - jurisdictions
    if missing_jurisdictions:
        errors.append(f"routing-golden.json: missing jurisdictions: {missing_jurisdictions}")
    return errors


def validate_product_golden(path: Path) -> list[str]:
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 5:
        errors.append(f"product-golden.json: expected 5+ cases, got {len(cases)}")
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
