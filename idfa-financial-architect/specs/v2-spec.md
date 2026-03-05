# IDFA Financial Architect Plugin — v2.0 Spec

## Context

The IDFA plugin (v1.0) encodes the methodology correctly but references fictional tooling:

- `write_cell()`, `read_cell()`, `inspect_model()`, `read_formula()` — functions presented as "Excel MCP Server" tools that don't exist
- These function signatures cause **agent hallucination** — Claude will literally try to call `write_cell()` if instructed to

The methodology is sound. The execution layer is fiction. v2.0 makes it real.

## Decision: Two-Skill Architecture

The plugin ships two complementary skills:

| Skill                 | Purpose                                                                                  | Changes in v2.0                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `financial-architect` | IDFA methodology — Three Layers, Four Guardrails, Naming Conventions                     | **Surgical edits only**: replace fictional function signatures with references to `idfa-ops` companion skill |
| `idfa-ops` (NEW)      | Execution engine — real scripts for Named Range CRUD, compliance auditing, recalculation | **Brand new skill** with PEP 723 scripts run via `uv run`                                                    |

**Why two skills, not one?**

- The methodology skill is tested and proven — don't break what works
- Separation of concerns: WHAT to do (methodology) vs HOW to do it (operations)
- Other agents (Copilot, Cursor, Codex) can use the methodology skill standalone
- The ops skill can evolve independently (new scripts, better tooling) without touching methodology

**Composition with Anthropic's xlsx skill:**
The `idfa-ops` skill composes with — but does not require — Anthropic's `xlsx` skill. When both are installed, the xlsx skill provides `recalc.py` for LibreOffice-based formula evaluation. When only `idfa-ops` is installed, `recalc_bridge.py` handles recalculation standalone.

---

## What Changes in v2.0

### 1. Surgical Edits to `skills/financial-architect/SKILL.md`

**Scope:** Replace fictional function signatures that cause agent hallucination. All methodology content stays unchanged.

**Lines requiring edit (v1.0 line numbers):**

#### a. Guardrail 4 section (lines 155-184)

**Current (causes hallucination):**

```
### Guardrail 4 — MCP Dependency
...
| `write_cell(name, value)` | Set a Named Range assumption |
| `read_cell(name)` | Read a Named Range result |
| `inspect_model()` | List all Named Ranges, values, and dependencies |
| `read_formula(name)` | Return the formula assigned to a Named Range |
```

**Replace with:**

```
### Guardrail 4 — Delegated Calculation

**Rule:** An AI agent operating on an IDFA-compliant model is prohibited from
performing calculations internally. It must delegate all arithmetic to the
spreadsheet engine — writing assumptions, triggering recalculation, and reading
back results.

**The workflow:**
```

Agent reasons: "The correct value for Inp_COGS_Pct_Y2 is 59%"
↓
Agent writes assumption to the model (Named Range Inp_COGS_Pct_Y2 = 0.59)
↓
Spreadsheet engine recalculates deterministically
↓
Agent reads result from model (Named Range Gross_Profit_Y2 → $4,510,000)
↓
Agent reports: "Year 2 Gross Profit is $4,510,000"

```

**Why:** This separation ensures the agent provides the reasoning while the
spreadsheet engine provides the mathematics. The result is not the agent's
estimate — it is the model's deterministic output.

**Implementation:** The companion `idfa-ops` skill provides scripts for all
model interactions — writing assumptions, reading results, inspecting model
structure, and auditing compliance. See `idfa-ops` skill documentation.
```

**What stays:** The "Why" paragraph explaining deterministic separation. The workflow concept (write → calculate → read). The principle that agents must not calculate internally.

#### b. Worked Example "What-If via MCP" (lines 260-271)

**Current:**

```python
write_cell("Inp_Rev_Y1", 12000000)
read_cell("Gross_Profit_Y1")  # → $4,800,000
```

**Replace with:**

```
### What-If Analysis

User asks: "What if Year 1 Revenue is $12M?"

The agent updates Inp_Rev_Y1 to 12,000,000 in the model, triggers
recalculation, and reads back:

| Output | Value |
|--------|-------|
| Gross_Profit_Y1 | $4,800,000 |
| Gross_Profit_Y2 | $5,412,000 |
| Gross_Profit_Y3 | $6,098,400 |

The agent does not calculate these numbers. The spreadsheet engine does.
The `idfa-ops` companion skill handles the write → recalculate → read sequence.
```

#### c. Agent Decision Table (lines 275-287)

Replace all function call syntax with semantic operations:

| Task         | Current (hallucination risk)           | Replacement                                                               |
| ------------ | -------------------------------------- | ------------------------------------------------------------------------- |
| Auditing     | `inspect_model()` → check...           | Inspect the model (via `idfa-ops`) → check...                             |
| Retrofitting | `inspect_model()` → identify...        | Inspect the model (via `idfa-ops`) → identify...                          |
| What-if      | `write_cell()` → `read_cell()`         | Write assumption → recalculate → read result (via `idfa-ops`)             |
| Goal-seeking | `write_cell()` → `read_cell()` iterate | Write → recalculate → read, iterate until target reached (via `idfa-ops`) |
| Explaining   | `read_formula(name)`                   | Read the formula for the Named Range (via `idfa-ops`)                     |
| Compliance   | `inspect_model()` → verify...          | Inspect the model (via `idfa-ops`) → verify...                            |

#### d. Common Mistakes line 300

**Current:** "Use `read_cell()`."
**Replace with:** "Read the result from the model via the `idfa-ops` skill."

#### e. Trigger Phrases table (lines 317-328)

Replace all function call syntax with semantic operations (same pattern as Agent Decision Table).

**What does NOT change in financial-architect/SKILL.md:**

- YAML frontmatter (name, description, triggers, metadata)
- Core Principle section
- The Problem This Solves section
- Three Layers section
- Guardrails 1-3 (Named Range Priority, LaTeX Verification, Intent Notes)
- Naming Conventions
- Worked Example Steps 1-4 (the formulas and business logic)
- Common Mistakes (except line 300)
- Attribution

### 2. Surgical Edits to `references/IDFA-reference.md`

Same pattern — replace fictional function signatures, keep all methodology content.

**Sections requiring edit:**

#### a. Five Capability Tests (lines 49-113)

- Capability 2 (Deterministic What-If): Replace `read_cell()` / `write_cell()` with "write assumption to model" / "read result from model"
- Capability 3 (Logic De-compilation): Replace `inspect_model()` with "inspect the model"
- Capability 4 (Strategic Goal-Seeking): Replace `write_cell()` / `read_cell()` iteration with "write → recalculate → read" iteration
- Capability 5 (Stochastic Simulation): Replace `read_cell()` with "read result from model"

#### b. Retrofitting Phase 1 (lines 120-125)

Replace `inspect_model()` code block with plain description: "Inspect the model to produce: full list of Named Ranges, all formulas, all hardcoded values, dependency map."

#### c. Retrofitting Phase 4 steps (lines 145-153)

Replace `read_formula()` with "Read the original formula for the Named Range"

### 3. New `skills/idfa-ops/` Skill

Brand new skill providing the real execution layer.

#### Directory Structure

```
skills/idfa-ops/
├── SKILL.md                    ← Methodology-aware operations guide
└── scripts/
    ├── idfa_ops.py            ← Core Named Range CRUD (PEP 723, openpyxl)
    ├── idfa_audit.py          ← IDFA compliance auditor (PEP 723, openpyxl)
    └── recalc_bridge.py       ← LibreOffice recalc (PEP 723, standalone or xlsx skill bridge)
```

#### `skills/idfa-ops/SKILL.md`

YAML frontmatter:

```yaml
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
```

Content sections:

1. **When to Use This Skill** — Activate when the `financial-architect` methodology skill calls for model interaction (writing assumptions, reading results, inspecting structure, auditing compliance)

2. **Prerequisites** — Python 3.10+, uv (for PEP 723 inline deps), LibreOffice (for recalculation)

3. **Operations Reference** — Semantic operations mapped to script commands:

| Operation          | Script Command                                                         | What It Does                                          |
| ------------------ | ---------------------------------------------------------------------- | ----------------------------------------------------- |
| Write assumption   | `uv run scripts/idfa_ops.py write <file> <name> <value>`               | Set a Named Range input value                         |
| Read result        | `uv run scripts/idfa_ops.py read <file> <name> [name2...]`             | Read Named Range value(s) after recalc                |
| Inspect model      | `uv run scripts/idfa_ops.py inspect <file>`                            | List all Named Ranges, values, formulas, dependencies |
| Read formula       | `uv run scripts/idfa_ops.py formula <file> <name>`                     | Return the formula text for a Named Range             |
| Create Named Range | `uv run scripts/idfa_ops.py create-range <file> <name> <sheet> <cell>` | Create a new Named Range definition                   |
| Recalculate        | `uv run scripts/recalc_bridge.py <file>`                               | Trigger LibreOffice deterministic recalculation       |
| Audit compliance   | `uv run scripts/idfa_audit.py <file>`                                  | Check all four IDFA guardrails, return JSON report    |

4. **The Write-Recalculate-Read Pattern** — The fundamental interaction pattern:

```
# Step 1: Write assumption
uv run scripts/idfa_ops.py write model.xlsx Inp_Rev_Y1 12000000

# Step 2: Recalculate (LibreOffice evaluates all formulas)
uv run scripts/recalc_bridge.py model.xlsx

# Step 3: Read results
uv run scripts/idfa_ops.py read model.xlsx Gross_Profit_Y1 Gross_Profit_Y2 Gross_Profit_Y3
```

5. **Composing with the xlsx Skill** — When Anthropic's xlsx skill is also installed, `recalc_bridge.py` delegates to the xlsx skill's `recalc.py`. When standalone, it runs its own LibreOffice macro. The interface is identical either way.

6. **Output Formats** — All scripts output JSON to stdout for agent consumption. Human-readable summaries on stderr.

7. **Error Handling** — Named Range not found, LibreOffice not installed (graceful degradation with warning), file not found, permission errors.

#### `scripts/idfa_ops.py`

PEP 723 inline metadata:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl>=3.1"]
# ///
```

CLI interface:

```
idfa_ops.py write <file> <name> <value>
idfa_ops.py read <file> <name> [name2 ...]
idfa_ops.py inspect <file>
idfa_ops.py formula <file> <name>
idfa_ops.py create-range <file> <name> <sheet> <cell>
```

Implementation details:

- All operations work through Named Ranges (Excel Defined Names), never cell coordinates
- `write`: Find Named Range → resolve to sheet/cell → write value → save
- `read`: Load workbook with `data_only=True` → find Named Range → return value
- `inspect`: Iterate `wb.defined_names.definedNameList` → for each, resolve destination, read value and formula → return JSON summary
- `formula`: Load workbook WITHOUT `data_only` → find Named Range → return cell formula string
- `create-range`: Create new `DefinedName` → add to workbook → save
- All output as JSON to stdout
- Exit codes: 0 = success, 1 = Named Range not found, 2 = file error

#### `scripts/idfa_audit.py`

PEP 723 inline metadata:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl>=3.1"]
# ///
```

CLI: `idfa_audit.py <file>`

Checks all four IDFA guardrails:

1. **Named Range Priority** — Scan all formulas for coordinate references (regex: `[A-Z]+\d+`, `\$[A-Z]+\$\d+`). Flag any formula in Calculation layer using cell addresses instead of Named Ranges.

2. **LaTeX Verification** — Check for Intent Notes on complex formulas (WACC, NPV, DCF, IRR). Warn if complex formulas lack LaTeX verification documentation.

3. **Intent Notes** — Check all formulas for attached Excel comments/notes. Report coverage percentage.

4. **Layer Isolation** — Check Calculation layer formulas for hardcoded constants (numbers that should be in Assumptions layer).

Output JSON:

```json
{
  "guardrail_1_named_ranges": {
    "status": "PASS|FAIL",
    "violations": 0,
    "details": []
  },
  "guardrail_2_latex": {
    "status": "PASS|WARN|FAIL",
    "complex_formulas_without_verification": 0
  },
  "guardrail_3_intent_notes": { "status": "PASS|FAIL", "coverage": "100%" },
  "guardrail_4_layer_isolation": {
    "status": "PASS|FAIL",
    "violations": 0,
    "details": []
  },
  "overall": "PASS|FAIL",
  "compliance_score": "100%"
}
```

#### `scripts/recalc_bridge.py`

PEP 723 inline metadata:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
```

No Python dependencies — calls LibreOffice headless via subprocess.

Logic:

1. Check if xlsx skill's `recalc.py` exists at known paths → delegate if found
2. Otherwise, run own LibreOffice macro (same approach as xlsx skill):
   - Write a Basic macro to `RecalculateAndSave`
   - Run `soffice --headless --invisible` with the macro
   - Scan for formula errors in the result
3. Output JSON: `{ "status": "ok|error", "recalculated": true, "errors": [] }`
4. If LibreOffice not installed: exit with clear error message explaining the dependency

### 4. Fix README.md

**Remove:**

- Generic "Browse plugins" for Cowork (needs Personal → GitHub route)

**Update:**

- Claude Code install: keep `/plugin marketplace add` + `/plugin install` syntax
- Local Testing: keep `claude --plugin-dir` (confirmed valid)
- Cowork install: Replace with Personal → Add marketplace from GitHub route:
  ```
  1. In the Cowork sidebar, click Customize → Browse plugins → Personal
  2. Click +, then select Add marketplace from GitHub
  3. Enter: https://github.com/panaversity/idfa-financial-architect
  4. Find IDFA Financial Architect → click Install
  ```

**Add:**

- Dependency note: "This plugin works best alongside Anthropic's `xlsx` skill for deterministic formula recalculation"
- Note about the two skills: methodology (auto-activates on financial model conversations) + operations (provides programmatic model interaction)
- Prerequisites: Python 3.10+, uv, LibreOffice (for recalculation)

### 5. Plugin Manifest Updates

#### `.claude-plugin/plugin.json`

Version bump to `2.0.0`.

#### `.claude-plugin/marketplace.json`

Version bump to `2.0.0`. The marketplace entry covers the whole plugin; both skills are auto-discovered from `skills/` directory.

### 6. Plugin Structure (v2.0)

```
idfa-financial-architect/
├── .claude-plugin/
│   ├── plugin.json                         ← v2.0.0
│   └── marketplace.json                    ← v2.0.0
├── skills/
│   ├── financial-architect/                ← Methodology (surgical edits only)
│   │   ├── SKILL.md                        ← Four Guardrails, Three Layers, Naming
│   │   └── references/
│   │       └── IDFA-reference.md           ← Enterprise governance, complex formulas
│   └── idfa-ops/                           ← Execution engine (NEW)
│       ├── SKILL.md                        ← Operations guide + script reference
│       └── scripts/
│           ├── idfa_ops.py                 ← Named Range CRUD (openpyxl, PEP 723)
│           ├── idfa_audit.py               ← Compliance auditor (openpyxl, PEP 723)
│           └── recalc_bridge.py            ← LibreOffice recalc bridge (PEP 723)
├── examples/
│   └── gp_waterfall.xlsx                   ← Pre-built reference model (NEW)
├── README.md                               ← Fixed install commands
├── LICENSE                                 ← Proprietary (unchanged)
└── specs/
    └── v2-spec.md                          ← This file
```

---

## Dependencies

| Dependency           | Required?                  | Purpose                                                     |
| -------------------- | -------------------------- | ----------------------------------------------------------- |
| Python 3.10+         | Yes                        | Script runtime                                              |
| uv                   | Yes                        | PEP 723 inline dependency resolution                        |
| openpyxl >= 3.1      | Yes (auto-installed by uv) | Excel read/write with Named Ranges                          |
| LibreOffice          | Yes (for recalc)           | Deterministic formula evaluation                            |
| Anthropic xlsx skill | Recommended                | Provides battle-tested recalc.py + professional conventions |

Scripts use PEP 723 inline metadata — `uv run` handles dependency installation automatically. Zero manual `pip install` needed.

---

## Test Plan

### Script Tests (pytest, run via `uv run`)

| #   | Test                              | What It Verifies                                                              |
| --- | --------------------------------- | ----------------------------------------------------------------------------- |
| 1   | `test_write_assumption`           | Write a Named Range value, reload file, confirm value persists                |
| 2   | `test_read_output`                | Read a Named Range value from a known model, confirm correct value            |
| 3   | `test_inspect_model`              | Inspect a model, confirm all Named Ranges listed with correct metadata        |
| 4   | `test_read_formula`               | Read formula text for a Named Range, confirm formula string matches           |
| 5   | `test_create_named_range`         | Create a new Named Range, confirm it exists in workbook                       |
| 6   | `test_write_read_roundtrip`       | Write value → read back → confirm match (no recalc needed)                    |
| 7   | `test_audit_passing_model`        | Audit a compliant model, confirm all guardrails PASS                          |
| 8   | `test_audit_failing_model`        | Audit a non-compliant model, confirm correct violations detected              |
| 9   | `test_audit_coordinate_detection` | Formulas with `=B4*1.10` flagged; formulas with `=Revenue_Y1*Inp_Growth` pass |
| 10  | `test_named_range_not_found`      | Write/read non-existent Named Range → exit code 1, clear error                |
| 11  | `test_recalc_no_libreoffice`      | When LibreOffice not installed → graceful error message, not crash            |

### Integration Tests (require LibreOffice)

| #   | Test                     | What It Verifies                                                                         |
| --- | ------------------------ | ---------------------------------------------------------------------------------------- |
| 12  | `test_write_recalc_read` | Full cycle: write assumption → recalc → read dependent output → confirm calculated value |
| 13  | `test_what_if_scenario`  | GP Waterfall: change Inp_Rev_Y1 to $12M → recalc → confirm GP_Y3 = $6,098,400            |

### Test Fixtures

- `tests/fixtures/gp_waterfall_compliant.xlsx` — IDFA-compliant GP Waterfall model with all Named Ranges, formulas, and Intent Notes
- `tests/fixtures/gp_waterfall_violations.xlsx` — Same model with intentional violations (coordinate refs, hardcoded constants, missing Intent Notes)

---

## Success Criteria

1. `uv run scripts/idfa_ops.py write model.xlsx Inp_Rev_Y1 12000000` changes the Named Range value
2. `uv run scripts/idfa_ops.py read model.xlsx Gross_Profit_Y3` reads back a value
3. `uv run scripts/idfa_audit.py model.xlsx` produces a real JSON compliance report
4. `uv run scripts/recalc_bridge.py model.xlsx` triggers LibreOffice recalculation
5. All 11 unit tests pass; integration tests pass when LibreOffice is available
6. The `financial-architect` SKILL.md contains zero fictional function signatures (`write_cell`, `read_cell`, `inspect_model`, `read_formula` as callable functions)
7. An agent reading the updated SKILL.md knows to use `idfa-ops` scripts for model interaction
8. The plugin installs correctly in Claude Code via `/plugin` commands
9. README.md install instructions are verified working

## Constraints

- No new runtime dependencies beyond openpyxl + LibreOffice
- Proprietary license maintained
- Each SKILL.md remains a single file readable by any agent (not just Claude)
- Scripts must work standalone (no xlsx skill required) but compose well with it
- The methodology content (Three Layers, Four Guardrails, Naming Conventions) does NOT change — only fictional function signatures are replaced
- All scripts use PEP 723 inline metadata — zero setup required beyond `uv`
