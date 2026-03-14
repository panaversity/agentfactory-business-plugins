# /// script
# dependencies = []
# ///
"""
Banking Plugin -- Routing Validation
Run: uv run scripts/validate-routing.py

Validates that all expected skills exist and the router references them.
"""

import sys
from pathlib import Path

EXPECTED_SKILLS = [
    "banking-global-router",
    "ifrs9-ecl",
    "ifrs9-staging",
    "ifrs9-scenarios",
    "ifrs9-disclosure",
    "basel-capital",
    "basel-rwa-credit",
    "basel-rwa-market",
    "liquidity-lcr",
    "liquidity-nsfr",
    "stress-testing",
    "aml-typologies",
    "aml-sar-drafting",
    "aml-cdd-edd",
    "sanctions-screening",
    "kyc-risk-rating",
    "bank-reconciliation",
]

EXPECTED_JURISDICTIONS = [
    "uk-pra",
    "eu-crr",
    "us-federal",
    "australia-apra",
    "singapore-mas",
    "uae-cbuae",
    "pakistan-sbp",
]


def main():
    root = Path(__file__).parent.parent
    skills_dir = root / "skills"
    router_dir = skills_dir / "banking-global-router"
    jurisdictions_dir = router_dir / "references" / "jurisdictions"
    errors = []

    # Check all skills exist
    for skill in EXPECTED_SKILLS:
        skill_file = skills_dir / skill / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"Missing skill: {skill}/SKILL.md")

    # Check jurisdictions exist
    for jur in EXPECTED_JURISDICTIONS:
        jur_file = jurisdictions_dir / f"{jur}.md"
        if not jur_file.exists():
            errors.append(f"Missing jurisdiction: {jur}.md")

    # Check router references skills
    router_file = router_dir / "SKILL.md"
    if router_file.exists():
        router_content = router_file.read_text()
        for skill in EXPECTED_SKILLS:
            if skill == "banking-global-router":
                continue
            if skill not in router_content:
                errors.append(f"Router does not reference skill: {skill}")

    if errors:
        print(f"FAILED: {len(errors)} errors")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"PASSED: {len(EXPECTED_SKILLS)} skills, {len(EXPECTED_JURISDICTIONS)} jurisdictions validated")
        sys.exit(0)


if __name__ == "__main__":
    main()
