#!/usr/bin/env python3
"""
Agentic Office Plugin — Eval Runner

Usage:
    python evals/run.py             # Run all cases
    python evals/run.py --list      # List all case names
    python evals/run.py --case NAME # Run a single case
    python evals/run.py -v          # Verbose output
"""

import argparse
import json
import sys
from pathlib import Path

import yaml


CASES_DIR = Path(__file__).parent / "cases"


def load_cases() -> list[dict]:
    """Load all YAML eval cases from the cases/ directory."""
    cases = []
    for path in sorted(CASES_DIR.glob("*.yaml")):
        with open(path) as f:
            case = yaml.safe_load(f)
            case["_file"] = path.name
            cases.append(case)
    return cases


def check_routing(case: dict, verbose: bool = False) -> tuple[bool, str]:
    """
    Check that the query text contains trigger phrases that would
    activate the expected skill and NOT the negative-check skill.

    This is a deterministic check against SKILL.md description fields.
    """
    query = case["query"].lower()
    expected = case["expected_skill"]
    negative = case.get("negative_check_skill")

    # Load expected skill's trigger phrases from its SKILL.md
    skill_dir = Path(__file__).parent.parent / "skills" / expected / "SKILL.md"
    if not skill_dir.exists():
        return False, f"SKILL.md not found: {skill_dir}"

    content = skill_dir.read_text()
    # Extract description field from YAML frontmatter
    in_frontmatter = False
    description_lines = []
    for line in content.split("\n"):
        if line.strip() == "---":
            if in_frontmatter:
                break
            in_frontmatter = True
            continue
        if in_frontmatter and (line.startswith("description:") or description_lines):
            if line.startswith("description:"):
                description_lines.append(line.split("description:", 1)[1].strip())
            elif line.startswith("  ") or line.startswith("\t"):
                description_lines.append(line.strip())
            else:
                break

    description = " ".join(description_lines).lower()

    # Check that at least one trigger phrase from the expected skill matches
    # Extract trigger phrases (words after "Activate for:")
    trigger_section = ""
    if "activate for:" in description:
        trigger_section = description.split("activate for:", 1)[1]
        # Stop at "NOT for:" if present
        if "not for:" in trigger_section:
            trigger_section = trigger_section.split("not for:", 1)[0]

    triggers = [t.strip().rstrip(".") for t in trigger_section.split(",") if t.strip()]

    # Check for at least one trigger match in the query
    matched_triggers = [t for t in triggers if t in query]

    if not matched_triggers:
        return False, f"No trigger phrases from '{expected}' matched in query"

    if verbose:
        print(f"  Matched triggers: {matched_triggers}")

    # Negative check: ensure the query does NOT match official plugin triggers
    if negative:
        official_reserved = {
            "memory-management": [
                "task", "to-do", "todo", "add task", "complete task",
                "what's on my plate", "my tasks", "remind me to",
                "remember", "memory", "remember this", "who is",
                "what does x mean", "glossary", "acronym",
            ],
            "task-management": [
                "task", "to-do", "todo", "add task", "complete task",
                "what's on my plate", "my tasks", "remind me to",
                "done with", "finished", "waiting on",
            ],
            "update": [
                "update", "sync", "triage", "comprehensive scan", "refresh",
            ],
        }
        reserved = official_reserved.get(negative, [])
        collisions = [r for r in reserved if r in query]
        if collisions:
            return False, (
                f"Query collides with official '{negative}' triggers: {collisions}"
            )

    return True, f"Routed to '{expected}' via triggers: {matched_triggers}"


def check_accuracy(case: dict, verbose: bool = False) -> tuple[bool, str]:
    """
    Check that the expected skill's SKILL.md contains the output format
    elements required by this accuracy test case.
    """
    expected = case["expected_skill"]
    quality_checks = case.get("quality_checks", [])

    skill_path = Path(__file__).parent.parent / "skills" / expected / "SKILL.md"
    if not skill_path.exists():
        return False, f"SKILL.md not found: {skill_path}"

    content = skill_path.read_text().lower()

    missing = []
    for check in quality_checks:
        # Check that key terms from each quality check are present in the skill
        key_terms = [t.strip().lower() for t in check.split(",")]
        for term in key_terms:
            if len(term) > 3 and term not in content:
                missing.append(term)

    if missing:
        return False, f"Skill missing quality elements: {missing[:5]}"

    return True, "All quality check elements present in skill definition"


def check_negative(case: dict, verbose: bool = False) -> tuple[bool, str]:
    """
    Check that the skill handles 'not found' scenarios correctly.
    """
    expected = case["expected_skill"]
    skill_path = Path(__file__).parent.parent / "skills" / expected / "SKILL.md"
    if not skill_path.exists():
        return False, f"SKILL.md not found: {skill_path}"

    content = skill_path.read_text().lower()

    # Check the skill has explicit "not found" handling
    not_found_phrases = [
        "not in workplace memory",
        "not found",
        "do not fabricate",
        "not fabricate",
    ]

    found_phrases = [p for p in not_found_phrases if p in content]
    if not found_phrases:
        return False, "Skill does not contain 'not found' handling"

    return True, f"Skill has not-found handling: {found_phrases}"


def run_case(case: dict, verbose: bool = False) -> tuple[bool, str]:
    """Run a single eval case and return (passed, message)."""
    case_type = case.get("type", "routing")

    if case_type == "routing":
        return check_routing(case, verbose)
    elif case_type == "accuracy":
        return check_accuracy(case, verbose)
    elif case_type == "negative":
        return check_negative(case, verbose)
    else:
        return False, f"Unknown case type: {case_type}"


def main():
    parser = argparse.ArgumentParser(description="Agentic Office eval runner")
    parser.add_argument("--list", action="store_true", help="List all case names")
    parser.add_argument("--case", type=str, help="Run a single case by name")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    cases = load_cases()

    if args.list:
        for case in cases:
            print(f"  {case['name']}: {case.get('rationale', '')}")
        return

    if args.case:
        cases = [c for c in cases if c["name"] == args.case]
        if not cases:
            print(f"Case not found: {args.case}")
            sys.exit(1)

    passed = 0
    failed = 0
    results = []

    for case in cases:
        success, message = run_case(case, args.verbose)
        status = "PASS" if success else "FAIL"
        results.append((case["name"], status, message))

        if success:
            passed += 1
        else:
            failed += 1

        if args.verbose or not success:
            print(f"[{status}] {case['name']}: {message}")
        else:
            print(f"[{status}] {case['name']}")

    print(f"\n{passed} passed, {failed} failed, {len(results)} total")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
