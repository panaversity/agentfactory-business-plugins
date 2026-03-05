---
name: idfa-ops
description: >-
  Named Range operations for IDFA-compliant Excel models. Provides scripts
  to write assumptions, read results, inspect model structure, audit compliance,
  and trigger deterministic recalculation. Use alongside the idfa-financial-architect
  methodology skill. Activate when the agent needs to programmatically interact
  with an Excel financial model — reading, writing, auditing, or recalculating.
license: Proprietary
metadata:
  author: Panaversity
  version: "2.0"
  homepage: https://panaversity.org
  requires: python>=3.10
---

# IDFA Operations

Scripts for programmatic interaction with IDFA-compliant Excel financial models.

---

## When to Use This Skill

Activate when the `idfa-financial-architect` methodology skill calls for model
interaction:

- **Writing assumptions** — setting Named Range input values
- **Reading results** — retrieving calculated outputs after recalculation
- **Inspecting structure** — listing all Named Ranges, formulas, and dependencies
- **Auditing compliance** — checking all four IDFA guardrails
- **Recalculating** — triggering deterministic formula evaluation via LibreOffice

This skill provides the HOW. The methodology skill provides the WHAT.

---

## Prerequisites

| Dependency           | Required         | Purpose                              |
| -------------------- | ---------------- | ------------------------------------ |
| Python 3.10+         | Yes              | Script runtime                       |
| uv                   | Yes              | PEP 723 inline dependency resolution |
| LibreOffice          | Yes (for recalc) | Deterministic formula evaluation     |
| Anthropic xlsx skill | Recommended      | Provides battle-tested recalc.py     |

Scripts use PEP 723 inline metadata — `uv run` handles dependency installation
automatically. Zero manual `pip install` needed.

---

## Operations Reference

| Operation          | Command                                                                | What It Does                                       |
| ------------------ | ---------------------------------------------------------------------- | -------------------------------------------------- |
| Write assumption   | `uv run scripts/idfa_ops.py write <file> <name> <value>`               | Set a Named Range input value                      |
| Read result        | `uv run scripts/idfa_ops.py read <file> <name> [name2...]`             | Read Named Range value(s)                          |
| Inspect model      | `uv run scripts/idfa_ops.py inspect <file>`                            | List all Named Ranges, values, formulas            |
| Read formula       | `uv run scripts/idfa_ops.py formula <file> <name>`                     | Return the formula text for a Named Range          |
| Create Named Range | `uv run scripts/idfa_ops.py create-range <file> <name> <sheet> <cell>` | Create a new Named Range definition                |
| Recalculate        | `uv run scripts/recalc_bridge.py <file>`                               | Trigger LibreOffice deterministic recalculation    |
| Audit compliance   | `uv run scripts/idfa_audit.py <file>`                                  | Check all four IDFA guardrails, return JSON report |

All script paths are relative to this skill's directory (`skills/idfa-ops/`).

---

## The Write-Recalculate-Read Pattern

The fundamental interaction pattern for IDFA model operations. The agent
reasons about what values to set, but the spreadsheet engine performs all
arithmetic.

```bash
# Step 1: Write assumption
uv run scripts/idfa_ops.py write model.xlsx Inp_Rev_Y1 12000000

# Step 2: Recalculate (LibreOffice evaluates all formulas)
uv run scripts/recalc_bridge.py model.xlsx

# Step 3: Read results
uv run scripts/idfa_ops.py read model.xlsx Gross_Profit_Y1 Gross_Profit_Y2 Gross_Profit_Y3
```

**Step 1** writes the assumption to the Named Range. The value is stored but
dependent formulas are not yet recalculated.

**Step 2** triggers LibreOffice to evaluate every formula in the workbook
deterministically. This is essential — openpyxl cannot evaluate formulas.

**Step 3** reads the recalculated results. The values returned are the
model's deterministic output, not the agent's estimate.

---

## Composing with the xlsx Skill

When Anthropic's `xlsx` skill is also installed, `recalc_bridge.py` automatically
delegates to the xlsx skill's `recalc.py` for LibreOffice-based formula evaluation.
When only `idfa-ops` is installed, `recalc_bridge.py` runs its own LibreOffice macro.

The interface is identical either way — the agent calls the same command regardless
of which recalculation backend is available.

---

## Output Formats

All scripts output JSON to stdout for agent consumption.

**Success example (read):**

```json
{
  "status": "ok",
  "values": { "Gross_Profit_Y1": 4000000, "Gross_Profit_Y2": 4510000 }
}
```

**Success example (inspect):**

```json
{"status": "ok", "named_ranges": [...], "count": 16}
```

**Error example:**

```json
{ "error": "Named Range not found: Bad_Name" }
```

Exit codes: `0` = success, `1` = Named Range not found, `2` = file/usage error.

---

## Error Handling

| Error                     | Exit Code | Agent Action                                            |
| ------------------------- | --------- | ------------------------------------------------------- |
| Named Range not found     | 1         | Inspect model to find correct name                      |
| File not found            | 2         | Verify path and retry                                   |
| LibreOffice not installed | 1         | Warn user; read/write still work but recalc unavailable |
| Permission denied         | 2         | Check if file is open in Excel                          |

When LibreOffice is unavailable, the agent can still write assumptions and read
cached values — but the Write-Recalculate-Read pattern cannot complete. The agent
should inform the user that results may not reflect the latest assumptions.

---

## Attribution

IDFA Operations is part of the IDFA Financial Architect plugin, developed by
the **Panaversity team** (https://panaversity.org). Proprietary — see LICENSE.
