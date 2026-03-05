# IDFA Reference Guide

Deep reference material for agents performing advanced IDFA tasks.
Load this file when the main SKILL.md is insufficient for the task at hand.

---

## Enterprise Governance Standards

### The Four Governance Artefacts

**1. IDFA Standards Document**
A written specification of your organisation's naming conventions, layer
structure, LaTeX verification protocol, and Intent Note format. Version-
controlled. Reviewed annually. Without it, different teams implement IDFA
differently and standardisation benefits are lost.

**2. Model Registry**
A centralised record of every IDFA-compliant model in the organisation.
Fields: model name, owner, last validation date, Intent Note coverage %
(number of AI-generated formulas with Intent Notes / total AI-generated
formulas), and link to model file. Reviewed quarterly by the Controller.

**3. Validation Protocol**
Before any model is used in board-level or regulator-facing context, it
must pass formal IDFA validation:

- All Calculation layer formulas use Named Ranges (zero coordinate references)
- All complex formulas have LaTeX verification documented
- All AI-generated formulas have Intent Notes
- Model produces correct outputs on a standard set of test inputs
  Validation is documented and attached to the model in the registry.

**4. Finance Domain Agent Standards Policy**
Governs how AI agents interact with IDFA-compliant models:

- MCP Dependency guardrail is mandatory for all agent interactions
- Agents may not modify Named Range definitions without Controller sign-off
- All agent-generated formulas require LaTeX verification and Intent Notes
  before being committed to a production model
- Agent session logs are retained for 90 days minimum

---

## The Five Finance Domain Agent Capability Tests

Use these tests to validate that an IDFA deployment is working correctly.
All five must pass before a model is considered production-ready for
agent-assisted workflows.

### Capability 1 — Intent Synthesis

**What it tests:** Can the agent convert a plain-English Intent Statement
into a fully structured, three-layer IDFA model specification?

**Test procedure:** Provide a new Intent Statement the agent has not seen.
Ask it to produce the full model specification — every Named Range, every
formula, in correct IDFA notation — _before_ writing anything to Excel.
Verify that the specification is complete and correctly layered.

**Pass criteria:** Zero coordinate references in proposed formulas; all
inputs prefixed with `Inp_`; all calculations readable as plain-English
business rules.

### Capability 2 — Deterministic What-If

**What it tests:** Does the agent use MCP for all calculation, or does it
perform arithmetic internally?

**Test procedure:** Ask a what-if question. After the agent responds, ask it
to verify by reading back each affected Named Range from the model. The
reported answer and the verified answer must match exactly — not approximately.

**Pass criteria:** Agent uses the write → recalculate → read sequence for
every result; no instance of the agent reporting a number before reading it
from the model.

### Capability 3 — Logic De-compilation

**What it tests:** Can the agent reconstruct the business logic of an
unfamiliar coordinate-based model?

**Test procedure:** Provide a coordinate-based model the agent has not seen.
Ask it to produce a full IDFA Logic Map by inspecting the model. Ask a human
analyst who knows the model to verify every business rule. Document
discrepancies.

**Pass criteria:** Fewer than 5% of identified business rules are incorrect
or missing. All discrepancies are explained (ambiguity in original vs. agent
inference error).

### Capability 4 — Strategic Goal-Seeking

**What it tests:** Can the agent find a required input value by iterating
through the model?

**Test procedure:** Ask the agent to find the input value needed to achieve
a specific output target (e.g. "Find the Year 1 Revenue needed for Year 3
EBITDA to equal exactly $3M"). The agent must iterate the write → recalculate
→ read sequence until the target is reached. It must not estimate or calculate
the answer internally.

**Pass criteria:** Agent reaches target through model iteration; the final
read confirms the output equals the target; agent reports the required input
value from the model, not from calculation.

### Capability 5 — Stochastic Simulation

**What it tests:** Can the agent orchestrate Monte Carlo simulation across
an IDFA model?

**Test procedure:** Ask the agent to run 500 scenarios with specified
probability distributions for two or more assumptions. The agent must
iterate via the write → recalculate → read sequence, collect results, and
return a distribution summary (mean, median, 10th percentile, 90th percentile).

**Pass criteria:** 500 iterations completed; results collected from the model
after each iteration; distribution statistics calculated from the collected
results, not estimated; no internal simulation performed.

---

## Retrofitting — Extended Guidance

### Phase-by-Phase Detail

**Phase 1 — Full Inspection**

Inspect the model to produce: full list of Named Ranges (if any exist), all
formulas, all hardcoded values, dependency map showing which cells feed which
others.

**Phase 2 — Input Identification**
Distinguish inputs from calculations:

- Inputs: cells containing a raw number (no formula)
- Calculations: cells containing a formula

For each input:

1. Determine what it represents (from context, headers, or proximity)
2. Propose an IDFA-compliant Named Range following the `Inp_` convention
3. Confirm with the analyst before assigning

**Phase 3 — Dependency Ordering**
Before rewriting formulas, establish the dependency order:

- Identify which calculations depend on which inputs
- Rewrite in order: inputs first, then calculations that depend only on
  inputs, then calculations that depend on other calculations
- Never rewrite a dependent formula before its dependencies are rewritten

**Phase 4 — Formula Rewriting**
For each formula, in dependency order:

1. Read the original formula for the Named Range
2. State the business rule it encodes in plain English
3. Write the IDFA equivalent using Named Ranges
4. LaTeX-verify if the formula involves WACC, IRR, NPV, DCF, or any
   multi-step mathematical relationship
5. Confirm the rewritten formula produces the same output as the original
6. Write the IDFA formula to the model
7. Attach Intent Note

**Phase 5 — Validation**
Run the model on its original inputs. Confirm every output matches the
pre-retrofit values exactly. Any discrepancy indicates either:

- A formula error in the original model (surfaced by the retrofit) — document
  and discuss with analyst before proceeding
- An inference error in the retrofitted formula — correct and re-validate

**The critical principle:** Do not change business logic during a retrofit.
The objective is transparency, not improvement. Improvements happen after
the logic is readable.

---

## Complex Formula Reference

### WACC

$$WACC = \frac{E}{E+D} \times K_e + \frac{D}{E+D} \times K_d \times (1-T)$$

IDFA formula:

```
WACC = (Equity_Value / (Equity_Value + Debt_Value)) * Cost_of_Equity
     + (Debt_Value  / (Equity_Value + Debt_Value)) * Cost_of_Debt * (1 - Tax_Rate)
```

Common errors: missing `(1 - Tax_Rate)` on debt; weights not summing to 1.0;
mixing percentage and decimal inputs.

### NPV (Net Present Value)

$$NPV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - Initial\_Investment$$

IDFA formula (using Excel NPV function):

```
NPV_Result = NPV(Inp_Discount_Rate, CF_Y1, CF_Y2, CF_Y3, CF_Y4, CF_Y5)
           - Inp_Initial_Investment
```

Note: Excel's `NPV()` function assumes cash flows start at period 1, not
period 0. Initial investment at period 0 must be subtracted separately.

### Terminal Value (Gordon Growth Model)

$$TV = \frac{FCF_n \times (1+g)}{WACC - g}$$

IDFA formula:

```
Terminal_Value = (FCF_Final * (1 + Inp_Terminal_Growth))
               / (WACC - Inp_Terminal_Growth)
```

Common error: using the final projection year FCF directly without growing
it by `(1 + g)` to get the first terminal period FCF.

### IRR (Internal Rate of Return)

Excel's `IRR()` function is iterative — it cannot be expressed in closed-form
LaTeX. Verify by confirming `NPV = 0` at the computed IRR:

```
IRR_Result     = IRR(CF_Y0, CF_Y1, CF_Y2, CF_Y3, CF_Y4, CF_Y5)
IRR_Validation = NPV(IRR_Result, CF_Y1, CF_Y2, CF_Y3, CF_Y4, CF_Y5) + CF_Y0
```

`IRR_Validation` should equal 0 (or within floating point tolerance of 0).

---

## Sector-Specific Naming Extensions

For teams working within specific financial domains, extend the naming
convention with a domain prefix:

| Domain             | Prefix | Example                           |
| ------------------ | ------ | --------------------------------- |
| Investment Banking | `IB_`  | `IB_EV_Entry`, `IB_LBO_IRR`       |
| Private Equity     | `PE_`  | `PE_Entry_Multiple`, `PE_MOIC`    |
| FP&A / Corporate   | `FP_`  | `FP_Budget_Rev_Y1`, `FP_Variance` |
| Treasury           | `TR_`  | `TR_FX_Hedge_Ratio`, `TR_DSO`     |
| Credit / Risk      | `CR_`  | `CR_PD_Rating`, `CR_DSCR`         |

This is optional but recommended for multi-domain models where variables
from different contexts may otherwise collide.

---

_IDFA Reference Guide v1.0 — Panaversity (https://panaversity.org)_
_Proprietary — Panaversity. See LICENSE._
