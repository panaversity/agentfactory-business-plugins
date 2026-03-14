# Plugin Compliance Audit — Consolidated Report

**Date**: 2026-03-15
**Audited against**: agentskills.io spec, Claude Code Skills spec, Claude Code Subagents spec, Claude Code Plugins Reference

---

## Executive Summary

| Plugin | Skills | Agents | Violations | Content Warnings |
|--------|--------|--------|------------|------------------|
| Banking | 17 | 0 | **48** | 0 |
| Islamic Finance | 13 | 0 | **0** | 2 |
| IDFA Financial Architect | 2 | 0 | **1** | 0 |
| Legal Ops | 6 | 1 | **3** | 0 |
| Sales, RevOps & Marketing | 15 | 5 | **0** | 0 |
| **TOTAL** | **53** | **6** | **52** | **2** |

**All 5 plugin.json files: PASS** (0 violations)
**All 6 agent .md files: PASS** (0 violations)
**All violations are in SKILL.md frontmatter** (52 total)

---

## Violation Frequency Table

| Violation Rule | Description | Occurrences | Plugins Affected |
|----------------|-------------|-------------|------------------|
| **S21** | `author` at top level (not a valid field) | **17** | Banking (16), Legal Ops (1) |
| **S20** | `version` at top level (not a valid field) | **16** | Banking (15), Legal Ops (1) |
| **S22** | `standard` at top level (not a valid field) | **16** | Banking (15), Legal Ops (1) |
| **S27** | Other unrecognised fields (`disclosure`, `not_applicable_in`, `chapter`) | **3** | Banking (2: ifrs9-ecl), Legal Ops (1: legal-global-router) |
| **S6** | `name` doesn't match parent directory | **1** | IDFA (financial-architect) |
| | | **52 total** | |

### Content Warnings (not frontmatter violations)

| Warning | Occurrences | Plugin |
|---------|-------------|--------|
| Unexpanded shell substitution (`$(cat ...)`) in skill body | 2 | Islamic Finance (shariah-screening-global, takaful-ifrs17) |

---

## Analysis

### Pattern: Banking is the outlier

Banking accounts for **48 of 52 violations** (92%). The pattern is uniform — 16 of 17 skills have the same 3 invalid top-level fields (`version`, `author`, `standard`), and `ifrs9-ecl` has 2 additional unrecognised fields (`disclosure`, `not_applicable_in`). The router (`banking-global-router`) is clean.

This suggests banking was written before the team adopted the clean frontmatter pattern used in islamic-finance and sales-revops-marketing.

### Pattern: Newer plugins are clean

- **Islamic Finance** (v3.0.0): 0 frontmatter violations — all metadata properly omitted
- **Sales, RevOps & Marketing** (v1.0): 0 violations — skills AND agents fully compliant
- **Legal Ops** (v3.0.0): Only 1 of 6 skills has violations (the router, which was likely written first)

### The single structural violation

IDFA's `financial-architect/SKILL.md` has `name: idfa-financial-architect` but the directory is `financial-architect/`. Per S6, the name must match the directory. Fix: change `name` to `financial-architect`.

---

## Cross-Plugin Consistency Check

| Aspect | Banking | Islamic Finance | IDFA | Legal Ops | Sales & Marketing |
|--------|---------|-----------------|------|-----------|-------------------|
| Uses `metadata:` block | No (needs fix) | No (fields omitted) | Yes | No (needs fix for router) | No (fields omitted) |
| Has `version` in frontmatter | Yes (invalid) | No | No | Yes in router (invalid) | No |
| Has `author` in frontmatter | Yes (invalid) | No | No | Yes in router (invalid) | No |
| Has `standard` in frontmatter | Yes (invalid) | No | No | No | No |
| Agent files compliant | N/A | N/A | N/A | Yes | Yes |
| plugin.json compliant | Yes | Yes | Yes | Yes | Yes |

**Recommendation**: After fixing banking and legal-ops router, all plugins should use the same pattern — either include `metadata:` with version/author/standard, or omit them entirely (as islamic-finance and sales-marketing do). For consistency, recommend the `metadata:` approach since the information is valuable.

---

## Recommended Batch Fix Strategy

### Fix 1: Banking skills (48 violations) — Automated

All 16 affected banking skills need the same transformation:

```
BEFORE:
---
name: skill-name
version: 1.0
description: >
  ...
standard: ...
author: Panaversity — The AI Agent Factory
---

AFTER:
---
name: skill-name
description: >
  ...
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "..."
---
```

**Approach**: A single agent task with `context: fork` can read each file, extract the invalid fields, restructure them under `metadata:`, and write back. Or a Python/sed script.

Special cases:
- `ifrs9-ecl` has 2 extra fields (`disclosure`, `not_applicable_in`) — also move to `metadata:`
- `bank-reconciliation` has `author` but no `version` or `standard`

### Fix 2: Legal-ops router (3 violations) — Manual

One file: `legal-ops/skills/legal-global-router/SKILL.md`
Move `version`, `author`, `chapter` under `metadata:`. Corrected frontmatter is in `audit-legal-ops.md`.

### Fix 3: IDFA name mismatch (1 violation) — Manual

One file: `idfa-financial-architect/skills/financial-architect/SKILL.md`
Change `name: idfa-financial-architect` → `name: financial-architect`. Corrected frontmatter is in `audit-idfa.md`.

### Fix 4: Islamic Finance content stubs (2 warnings) — Manual

Two files need their skill bodies replaced with actual content:
- `islamic-finance/skills/shariah-screening-global/SKILL.md`
- `islamic-finance/skills/takaful-ifrs17/SKILL.md`

Both contain unexpanded `$(cat ...)` shell commands pointing to paths that no longer exist.

---

## Verification After Fixes

After applying all fixes, run this verification:

```bash
# Check no invalid top-level fields remain in any SKILL.md
for f in $(find . -name "SKILL.md" -path "*/skills/*"); do
  head -20 "$f" | grep -E "^(version|author|standard|background|memory|tools:|skills:)" && echo "FAIL: $f"
done

# Check all names match directories
for f in $(find . -name "SKILL.md" -path "*/skills/*"); do
  dir=$(basename $(dirname "$f"))
  name=$(grep "^name:" "$f" | head -1 | sed 's/name: *//')
  [ "$dir" != "$name" ] && echo "MISMATCH: $f (dir=$dir, name=$name)"
done

# Check no unexpanded shell substitutions
grep -r '$(cat ' */skills/*/SKILL.md && echo "STALE SHELL SUBS FOUND"
```

---

## Individual Audit Reports

- [audit-banking.md](audit-banking.md) — 48 violations, 17 corrected frontmatter blocks
- [audit-islamic-finance.md](audit-islamic-finance.md) — 0 violations, 2 content warnings
- [audit-idfa.md](audit-idfa.md) — 1 violation (name mismatch), corrected frontmatter
- [audit-legal-ops.md](audit-legal-ops.md) — 3 violations, corrected frontmatter
- [audit-sales-marketing.md](audit-sales-marketing.md) — 0 violations, fully clean
