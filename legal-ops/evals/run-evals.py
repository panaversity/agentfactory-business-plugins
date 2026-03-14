# /// script
# dependencies = []
# ///
"""
Legal Ops Plugin -- Eval Runner
Run: uv run evals/run-evals.py

Validates that golden files exist and have expected structure.
Does NOT run actual LLM inference -- that requires the plugin installed.

Two eval buckets:
  1. Panaversity-local: tests routing/behavior for skills THIS plugin owns
  2. Integration: tests handoff to Anthropic Layer 1 + overlay application
"""

import json
import sys
from pathlib import Path


# Skills owned by this plugin (Panaversity Layer 2)
PANAVERSITY_SKILLS = {
    "ip-protection",
    "regulatory-monitoring",
    "dsar-privacy",
    "legal-spend",
    "compliance-calendar",
    "contract-intake-agent",
}

EXPECTED_JURISDICTIONS = {"UK", "EU", "US", "Pakistan", "UAE"}


def validate_routing_golden(path: Path) -> list[str]:
    """Validate Panaversity-local routing cases."""
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 6:
        errors.append(f"routing-golden.json: expected 6+ cases (one per Panaversity skill), got {len(cases)}")
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
        # Every case in this file must route to a Panaversity-owned skill
        skill = c.get("expected_product_skill", "")
        if skill and skill not in PANAVERSITY_SKILLS:
            errors.append(
                f"routing-golden.json case {i}: skill '{skill}' is not Panaversity-owned. "
                f"Move to routing-integration-golden.json."
            )
    # Verify all 6 Panaversity skills are covered
    skills = {c["expected_product_skill"] for c in cases}
    missing_skills = PANAVERSITY_SKILLS - skills
    if missing_skills:
        errors.append(f"routing-golden.json: missing Panaversity skills: {missing_skills}")
    return errors


def validate_routing_integration(path: Path) -> list[str]:
    """Validate cross-plugin routing cases (handoff to Anthropic Layer 1)."""
    errors = []
    cases = json.loads(path.read_text())
    required_fields = [
        "query",
        "expected_handoff",
        "expected_jurisdiction",
        "expected_overlay",
        "expected_contains",
        "must_not_contain",
    ]
    for i, c in enumerate(cases):
        for f in required_fields:
            if f not in c:
                errors.append(f"routing-integration-golden.json case {i}: missing field '{f}'")
        # Every case must have owner: anthropic
        if c.get("owner") != "anthropic":
            errors.append(f"routing-integration-golden.json case {i}: missing or wrong 'owner' (expected 'anthropic')")
    return errors


def validate_product_golden(path: Path) -> list[str]:
    """Validate Panaversity-local product behavior cases."""
    errors = []
    cases = json.loads(path.read_text())
    if len(cases) < 2:
        errors.append(f"product-golden.json: expected 2+ Panaversity product cases, got {len(cases)}")
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
        # Every case must test a Panaversity-owned skill
        product = c.get("product", "")
        if product and product not in PANAVERSITY_SKILLS:
            errors.append(
                f"product-golden.json case {i}: product '{product}' is not Panaversity-owned. "
                f"Move to product-integration-golden.json."
            )
    return errors


def validate_product_integration(path: Path) -> list[str]:
    """Validate cross-plugin product behavior cases (Anthropic Layer 1 output)."""
    errors = []
    cases = json.loads(path.read_text())
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
                errors.append(f"product-integration-golden.json case {i}: missing field '{f}'")
        if c.get("owner") != "anthropic":
            errors.append(f"product-integration-golden.json case {i}: missing or wrong 'owner' (expected 'anthropic')")
    return errors


def main():
    eval_dir = Path(__file__).parent
    all_errors = []

    print("=" * 60)
    print("PANAVERSITY-LOCAL EVALS (skills owned by this plugin)")
    print("=" * 60)

    routing = eval_dir / "routing-golden.json"
    if routing.exists():
        all_errors.extend(validate_routing_golden(routing))
        cases = json.loads(routing.read_text())
        skills = {c["expected_product_skill"] for c in cases}
        print(f"  routing-golden.json: {len(cases)} cases covering {len(skills)} Panaversity skills")
    else:
        all_errors.append("routing-golden.json not found")

    product = eval_dir / "product-golden.json"
    if product.exists():
        all_errors.extend(validate_product_golden(product))
        print(f"  product-golden.json: {len(json.loads(product.read_text()))} cases")
    else:
        all_errors.append("product-golden.json not found")

    print()
    print("=" * 60)
    print("INTEGRATION EVALS (handoff to Anthropic Layer 1)")
    print("=" * 60)

    routing_int = eval_dir / "routing-integration-golden.json"
    if routing_int.exists():
        all_errors.extend(validate_routing_integration(routing_int))
        print(f"  routing-integration-golden.json: {len(json.loads(routing_int.read_text()))} cases")
    else:
        print("  routing-integration-golden.json: not found (optional)")

    product_int = eval_dir / "product-integration-golden.json"
    if product_int.exists():
        all_errors.extend(validate_product_integration(product_int))
        print(f"  product-integration-golden.json: {len(json.loads(product_int.read_text()))} cases")
    else:
        print("  product-integration-golden.json: not found (optional)")

    print()
    if all_errors:
        print(f"FAILED: {len(all_errors)} errors:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("PASSED: All golden files valid.")


if __name__ == "__main__":
    main()
