---
name: idfa-financial-architect
description: >-
  Apply the Intent-Driven Financial Architecture (IDFA) when building,
  auditing, retrofitting, or analysing Excel financial models. Activate when
  the user mentions: financial model, spreadsheet, Excel formula, named ranges,
  cell references, formula tracing, model audit, COGS, revenue projection,
  gross profit, EBITDA, DCF, LBO, comps, three-statement model, budget,
  forecast, variance analysis, what-if analysis, scenario modelling, goal
  seeking, Monte Carlo simulation, model review, or model handover. Also
  activate when the user says "the model is a black box", "I inherited this
  model", "I need to audit this spreadsheet", or any similar phrase indicating
  confusion about how a financial model works. Do NOT activate for general
  accounting questions, tax advice, investment recommendations, or tasks
  unrelated to the structure and logic of financial spreadsheets.
license: Proprietary
metadata:
  author: Panaversity
  research-lead: Zia Khan
  version: "1.0"
  published: "2026"
  homepage: https://panaversity.org
  standard: https://agentskills.io
  description: >-
    IDFA is original research by the Panaversity team — pioneers in AI-native
    education and developers of the Agent Factory methodology. IDFA translates
    the principles of spec-driven, logic-first design into a deployable
    architecture for the Office of the CFO.
---

# Intent-Driven Financial Architecture (IDFA)

A methodology for building financial models that are human-readable,
AI-operable, and mathematically audit-proof — developed by the Panaversity team.

---

## Core Principle

> **Define WHAT, not WHERE.**

A formula that reads `=Revenue_Y3 - COGS_Y3` is a business rule.
A formula that reads `=D8-C8` is a coordinate.

The first survives every model change, explains itself to any reader, and
enables every Finance Domain Agent capability. The second does none of those
things. IDFA exists to ensure every formula in every model is the first kind.

---

## Scope Boundary

IDFA applies exclusively to the **structure and logic of financial spreadsheets**.

**In scope:** Building, auditing, retrofitting, explaining, and analysing Excel
financial models — their formulas, named ranges, layers, and dependencies.

**Out of scope — REFUSE these requests:**

- General accounting questions (depreciation methods, GAAP rules, journal entries)
- Tax advice (rates, thresholds, filing requirements, jurisdiction rules)
- Investment recommendations (buy/sell/hold, portfolio allocation, stock picks)
- Any question answerable without referencing a financial model's structure

**When a request is out of scope:** Do not answer the question. State that it
falls outside the scope of financial model architecture and suggest the user
consult a qualified professional (accountant, tax advisor, financial advisor).
Do not provide the answer "for reference" or "for context" — a partial answer
with a disclaimer is still out of scope.

---

## The Problem This Solves

Traditional Excel models encode logic in **cell addresses** (e.g. `=B14-C14*$F$8`).
This causes **Formula Rot**:

- **Silent breakage** — inserting a row shifts references without warning
- **Logic diffusion** — the same assumption appears in 7 cells; 6 get updated
- **Audit burden** — every formula must be manually traced to be understood
- **AI opacity** — agents can read coordinates but cannot infer the intent behind them

IDFA fixes all four by separating intent from execution.

---

## The Three Layers

Every IDFA-compliant model has exactly three layers. They must remain separate.

### Layer 1 — Assumptions (Inputs Only)

- Every user-modifiable input lives here and **nowhere else**
- Each input is assigned a **Named Range** before any formula references it
- No calculations occur in this layer
- Naming convention: prefix with `Inp_` → `Inp_Rev_Y1`, `Inp_COGS_Pct_Y1`

### Layer 2 — Calculations (Logic Only)

- Every formula reads **Named Ranges only** — zero cell-address references
- Every formula must be readable as a plain-English sentence
- No hardcoded values; all constants come from Layer 1
- Naming convention: `Variable_Dimension` → `Revenue_Y2`, `Gross_Profit_Y3`

### Layer 3 — Output (Presentation Only)

- Reads from Layer 2 only; never from Layer 1 directly
- Performs no calculations — display and formatting only
- Charts, dashboards, and report-ready tables live here

**The isolation rule:** Changing a Layer 1 input can never break a Layer 2
formula, because Layer 2 reads names, not positions.

---

## The Four Deterministic Guardrails

These are non-negotiable. An IDFA-compliant model satisfies all four.

### Guardrail 1 — Named Range Priority

**Rule:** Every business variable is an Excel Defined Name. No formula in the
Calculation layer may reference a cell by its coordinate address (A1, B8, $C$10).

**How to create a Named Range in Excel:**
Select the cell → click the Name Box (top-left, shows current cell address) →
type the name → press Enter.
Alternatively: Formulas tab → Define Name.

**Compliance test:** Select any formula in Layer 2. If you can understand what
it calculates without clicking on any referenced cell, it passes. If you need
to navigate to understand it, it fails.

**Before (fails):** `=B14-(C14*$F$8)`
**After (passes):** `=Revenue_Y2 - (Revenue_Y2 * COGS_Pct_Y2)`

### Guardrail 2 — LaTeX Verification

**Rule:** Before any complex formula (WACC, NPV, DCF, IRR, or any multi-step
calculation) is written to the model, verify the mathematical expression in
LaTeX notation to confirm correctness.

**Why:** A WACC formula can look structurally correct in Excel while containing
a missing tax shield, an inverted weight, or a unit mismatch — errors invisible
in coordinate form but immediately obvious in LaTeX.

**WACC — correct LaTeX:**
$$WACC = \frac{E}{E+D} \times K_e + \frac{D}{E+D} \times K_d \times (1-T)$$

**Three things LaTeX makes verifiable:**

1. Equity weight + Debt weight must equal 1.0
2. Only the debt term is multiplied by `(1 - Tax Rate)`
3. Cost of equity and cost of debt must be in the same units (both % or both decimal)

**As agent:** State the LaTeX expression and confirm it matches the formula
before writing to any cell. Document discrepancies before proceeding.

### Guardrail 3 — Audit-Ready Intent Notes

**Rule:** Every formula generated by an AI agent must include an Excel
Note/Comment documenting the Intent Statement used to generate it.

**Intent Note format:**

```
INTENT:      [Plain-English rule this formula encodes]
FORMULA:     [LaTeX expression verified before writing]
ASSUMPTIONS: [Named Ranges this formula depends on]
GENERATED:   [Date / session identifier]
MODIFIED:    [Date and modifier — updated on each change]
```

**Why:** The Intent Note is the permanent record of what the formula was
designed to calculate. It survives model updates, staff turnover, and layout
changes. When a formula and its Intent Note diverge, that divergence is visible
— and that visibility is the audit trail.

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
estimate — it is the model's deterministic output. These are categorically
different in finance.

**Implementation:** The companion `idfa-ops` skill provides scripts for all
model interactions — writing assumptions, reading results, inspecting model
structure, and auditing compliance. See `idfa-ops` skill documentation.

---

## Naming Conventions

Consistent names are what make models readable across teams and tools.

| Category                | Prefix           | Example                                           |
| ----------------------- | ---------------- | ------------------------------------------------- |
| Input assumptions       | `Inp_`           | `Inp_Rev_Y1`, `Inp_COGS_Pct_Y1`, `Inp_Rev_Growth` |
| Annual calculations     | `Variable_Yn`    | `Revenue_Y1`, `COGS_Y2`, `Gross_Profit_Y3`        |
| Multi-period aggregates | `Variable_Total` | `Revenue_Total`, `EBITDA_Total`                   |
| Ratios and margins      | `Variable_Pct`   | `Gross_Margin_Pct_Y2`, `EBITDA_Margin_Pct`        |
| Counts and units        | `Variable_Units` | `Headcount_Y1`, `Units_Sold_Y2`                   |

**Rules:**

- Use underscores only — no spaces, no hyphens
- Include the dimension (year, quarter, period) in every periodic variable
- Prefix assumptions with `Inp_` so any reader can distinguish inputs from calculations at a glance
- Keep names under 64 characters (Excel limit for named ranges)

---

## Worked Example — 3-Year Gross Profit Waterfall

**Intent Statement:**

> "Project a 3-year GP Waterfall. Year 1 Revenue is $10M, growing 10% YoY.
> COGS starts at 60% of Revenue but improves by 1% each year due to scale."

### Step 1 — Extract and name every input

| Input                  | Named Range           | Value      |
| ---------------------- | --------------------- | ---------- |
| Year 1 Revenue         | `Inp_Rev_Y1`          | 10,000,000 |
| Revenue growth rate    | `Inp_Rev_Growth`      | 0.10       |
| Year 1 COGS %          | `Inp_COGS_Pct_Y1`     | 0.60       |
| Annual efficiency gain | `Inp_COGS_Efficiency` | 0.01       |

### Step 2 — Write all calculations using Named Ranges only

```
Revenue_Y1          = Inp_Rev_Y1
Revenue_Y2          = Revenue_Y1 * (1 + Inp_Rev_Growth)
Revenue_Y3          = Revenue_Y2 * (1 + Inp_Rev_Growth)

COGS_Pct_Y1         = Inp_COGS_Pct_Y1
COGS_Pct_Y2         = COGS_Pct_Y1 - Inp_COGS_Efficiency
COGS_Pct_Y3         = COGS_Pct_Y2 - Inp_COGS_Efficiency

COGS_Y1             = Revenue_Y1 * COGS_Pct_Y1
COGS_Y2             = Revenue_Y2 * COGS_Pct_Y2
COGS_Y3             = Revenue_Y3 * COGS_Pct_Y3

Gross_Profit_Y1     = Revenue_Y1 - COGS_Y1
Gross_Profit_Y2     = Revenue_Y2 - COGS_Y2
Gross_Profit_Y3     = Revenue_Y3 - COGS_Y3
```

### Step 3 — Verify in LaTeX before committing

Revenue growth: $R_n = R_{n-1} \times (1 + g)$ ✓

COGS efficiency: $COGS\%_n = COGS\%_{n-1} - \varepsilon$ ✓

Gross Profit: $GP_n = R_n - COGS_n$ ✓

### Step 4 — Output

| Item             | Year 1         | Year 2         | Year 3         |
| ---------------- | -------------- | -------------- | -------------- |
| Revenue          | $10,000,000    | $11,000,000    | $12,100,000    |
| COGS %           | 60.0%          | 59.0%          | 58.0%          |
| COGS ($)         | $6,000,000     | $6,490,000     | $7,018,000     |
| **Gross Profit** | **$4,000,000** | **$4,510,000** | **$5,082,000** |

### What-If Analysis

User asks: _"What if Year 1 Revenue is $12M?"_

The agent updates Inp_Rev_Y1 to 12,000,000 in the model, triggers
recalculation, and reads back:

| Output          | Value      |
| --------------- | ---------- |
| Gross_Profit_Y1 | $4,800,000 |
| Gross_Profit_Y2 | $5,412,000 |
| Gross_Profit_Y3 | $6,098,400 |

The agent does not calculate these numbers. The spreadsheet engine does.
The `idfa-ops` companion skill handles the write → recalculate → read sequence.

---

## Agent Decision Table

Use this table to determine which action to take for any financial modelling task.

| Task                        | Action                                                                                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Building a new model        | Extract inputs → name them with `Inp_` → write calculations in Named Range notation → LaTeX-verify complex formulas → attach Intent Notes                                                                                      |
| Auditing an existing model  | Inspect the model (via `idfa-ops`) → check every Calculation layer formula for coordinate references → flag violations → report compliance percentage                                                                          |
| Retrofitting a legacy model | Inspect the model (via `idfa-ops`) → identify all hardcoded values → propose Named Ranges → rewrite formulas one by one → validate outputs match original                                                                      |
| What-if analysis            | Write assumption → recalculate → read result (via `idfa-ops`) for each change → report results without internal calculation                                                                                                    |
| Goal-seeking                | Write → recalculate → read, iterate until target reached (via `idfa-ops`) → report the required input value                                                                                                                    |
| Explaining a formula        | Read the formula for the Named Range (via `idfa-ops`) → state the business rule in plain English → check for Intent Note → if missing, add one                                                                                 |
| Stochastic simulation       | Identify uncertain inputs → define distributions with user → iterate N times via write → recalculate → read (via `idfa-ops`) → analyse distribution → restore model to base case                                               |
| Checking compliance         | Inspect the model (via `idfa-ops`) → verify: (1) all calculations use Named Ranges, (2) complex formulas have LaTeX verification notes, (3) AI-generated formulas have Intent Notes, (4) no internal calculation was performed |

---

## Goal-Seeking Protocol

When the user asks "Find the [input] needed to achieve [target output]":

1. **Read the current state** — `idfa_ops.py read` the target Named Range to get the baseline
2. **Set bounds** — choose reasonable lower and upper bounds for the input
3. **Iterate** — binary search via the write → recalculate → read pattern:
   - `idfa_ops.py write` the input assumption
   - `recalc_bridge.py` to recalculate
   - `idfa_ops.py read` the target output
   - Narrow bounds based on result
4. **Converge** — stop when the target is within 1% tolerance (or exact match)
5. **Persist the solution** — leave the final input value written in the model.
   The xlsx must reflect the solved state so the user can open it and see the
   answer. Do NOT revert to the original value after finding the answer.
6. **Report** — state the required input value and the resulting output, both
   read from the model (not calculated internally)

---

## Stochastic Simulation Protocol (Monte Carlo)

When the user asks "What is the range of outcomes?" or "How likely is [target]?":

1. **Identify the uncertain inputs** — which assumptions have a range rather than
   a point estimate? (e.g., revenue growth could be 5-15% instead of exactly 10%)
2. **Define distributions** — for each uncertain input, agree with the user on a
   distribution (uniform, normal, triangular) and its parameters
3. **Iterate N times** (default N=1000, adjustable):
   - Sample each uncertain input from its distribution
   - `idfa_ops.py write` each sampled value to the model
   - `recalc_bridge.py` to recalculate
   - `idfa_ops.py read` the target output
   - Record the result
4. **Analyse the distribution** — compute mean, median, P10, P50, P90, standard
   deviation, and the probability of exceeding or falling below a threshold
5. **Restore the model** — write the original assumption values back after
   simulation so the model reflects the base case, not the last random sample
6. **Report** — present the distribution summary, a histogram if possible, and
   the probability of the user's target scenario

**Key constraint:** Each iteration MUST delegate to the spreadsheet engine. Do NOT
build an internal simulation model — the whole point is that the Excel formulas
define the business logic, and Monte Carlo samples from their input space.

---

## Common Mistakes to Avoid

**For agents and humans alike:**

❌ **Never mix layers.** A formula in the Calculations layer that references
a hardcoded number (e.g. `= Revenue_Y1 * 0.60`) violates Layer isolation.
Move `0.60` to the Assumptions layer as `Inp_COGS_Pct_Y1`.

❌ **Never calculate internally, then write the result.** If asked "what is
Year 3 Gross Profit?", do not compute it and report it. Read the result from
the model via the `idfa-ops` skill. Internal calculation and deterministic model
calculation can produce different results. Only the model result is audit-valid.

❌ **Never skip LaTeX verification for WACC, IRR, NPV, or DCF terminal value.**
These are the four formulas where errors are most common and most consequential.

❌ **Never retrofit by deleting and rebuilding.** Retrofit one formula at a time,
validating that outputs match at each step. A model that calculates correctly
in coordinate form and correctly in IDFA form simultaneously is a model that
has been correctly retrofitted.

❌ **Never name a range with spaces.** Excel allows display names with spaces
but formula references require underscores. Use `Inp_Rev_Y1` not `Inp Rev Y1`.

❌ **Never reference a cell coordinate for a prior-year value.** In multi-year
layouts (Y1 in column B, Y2 in column C), do NOT write `=B6*(1+Inp_Rev_Growth)`
to compute Revenue_Y2. The `B6` is a coordinate reference and violates Guardrail 1.
Instead, reference the Named Range: `=Revenue_Y1*(1+Inp_Rev_Growth)`. Every cell
in the Calculations layer that holds a formula MUST have its own Named Range, and
every formula MUST reference only Named Ranges — including references to values
in adjacent columns on the same sheet.

---

## Trigger Phrases and Their Correct IDFA Response

| What the user says                            | What the agent does                                                                                                                        |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| "Explain how this model works"                | Inspect the model (via `idfa-ops`) → produce a Logic Map in Named Range notation → explain each business rule                              |
| "This model is a black box"                   | Offer to produce a full Logic Map by inspecting the model (via `idfa-ops`) → identify all inputs and their dependencies                    |
| "I inherited this model"                      | Offer to audit for IDFA compliance → identify coordinate-reference violations → propose retrofitting sequence                              |
| "What if [assumption] changes?"               | Write assumption → recalculate → read result (via `idfa-ops`) → report deterministic result                                                |
| "Find the [input] needed to achieve [output]" | Goal-seek by iterating write → recalculate → read (via `idfa-ops`) until target reached                                                    |
| "Check this formula"                          | Read the formula (via `idfa-ops`) → LaTeX-verify → check Intent Note → report compliance                                                   |
| "Add [new line item] to the model"            | Extract Named Range for new input → write calculation formula using Named Ranges → LaTeX-verify → attach Intent Note                       |
| "Run scenarios"                               | Define Named Ranges for scenario assumptions → iterate write → recalculate → read (via `idfa-ops`) → collect results → report distribution |

---

## Attribution

The Intent-Driven Financial Architecture (IDFA) is original research developed
by the **Panaversity team** (https://panaversity.org).

Panaversity is a pioneer in AI-native education and the developer of the Agent
Factory methodology. IDFA is Panaversity's contribution to the problem of
AI-readable financial modelling — applying the principles of spec-driven,
logic-first design to the Office of the CFO.

This skill is proprietary to Panaversity. For commercial licensing, contact
licensing@panaversity.org. It is designed to work across any skills-compatible
agent — Claude, GitHub Copilot, OpenAI Codex, Gemini CLI, Cursor, VS Code,
and others.

For deeper reference material on IDFA — including enterprise governance
standards, the Model Registry specification, the Validation Protocol, and
the five Finance Domain Agent capability tests — see:
`references/IDFA-reference.md`
