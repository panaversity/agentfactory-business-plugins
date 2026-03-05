---
name: ifrs9-scenarios
version: 1.0
description: >
  Activate for: macro overlay, macroeconomic scenarios, PIT PD,
  point-in-time PD, credit cycle adjustment, scenario weighting,
  forward-looking information, satellite model, GDP, unemployment,
  house price index, IFRS 9 scenarios, scenario probability.
standard: IFRS 9.5.5.17 (Forward-looking information)
author: Panaversity — The AI Agent Factory
---

## IFRS 9 SCENARIO FRAMEWORK REQUIREMENTS
IFRS 9.5.5.17 requires: reasonable and supportable information about
future economic conditions, including forward-looking information.
This is not optional. Single-scenario ECL is non-compliant with IFRS 9.

## SCENARIO STRUCTURE — MINIMUM AND BEST PRACTICE
Minimum (IFRS 9): base + 1 upside + 1 adverse
Best practice: 4–5 scenarios with explicit probability weights

| Scenario | Typical Weight | Key Feature |
|---|---|---|
| Upside | 10–20% | Above-trend growth, falling unemployment |
| Base | 35–50% | Central forecast, moderate conditions |
| Adverse | 25–35% | Mild recession, rising unemployment |
| Severe | 10–20% | Deep recession, sharply falling asset prices |

Weights must: sum to 1.0; reflect management's genuine probability assessment;
be documented and approved by the IFRS 9 Governance Committee.
Equal weighting (25% each) is RARELY defensible and will be challenged by auditors.

## KEY MACROECONOMIC VARIABLES BY ASSET CLASS
Retail mortgages: House Price Index (HPI), unemployment rate, base rate
Consumer loans: Unemployment rate, disposable income index, base rate
SME loans: GDP growth, SME default index, unemployment rate
Corporate loans: GDP growth, corporate default rates, sector-specific indices
Commercial Real Estate: CRE capital value index, vacancy rates, GDP growth

## CREDIT CYCLE ADJUSTMENT (CCA) — CONVERTING TTC TO PIT PD
PIT PD = TTC PD × CCA
CCA is estimated from a satellite model. Typical satellite model form:
  ln(CCA) = α + β₁(GDP_growth) + β₂(Unemployment) + β₃(HPI_growth) + ε

Example CCA values:
  Severe recession: CCA = 1.8–2.5 (PDs 80–150% above long-run average)
  Adverse: CCA = 1.2–1.5
  Base: CCA ≈ 1.0 (by definition — TTC PD already reflects long-run average)
  Upside: CCA = 0.7–0.9 (PDs below long-run average)

## WEIGHTED ECL CALCULATION
Step 1: Calculate PIT PD for each scenario using scenario-specific CCA
Step 2: Calculate ECL for each scenario: ECL_s = PD_PIT_s × LGD × EAD (Stage 1)
        or ECL_s = Σt [PD_marginal_t_s × LGD_t × EAD_t × DF_t] (Stage 2/3)
Step 3: Weighted ECL = Σs (Weight_s × ECL_s)

## NON-LINEAR EFFECTS
Weighted ECL ≠ ECL at weighted-average PD (due to non-linearity in ECL formula).
Always calculate ECL for each scenario separately, then probability-weight the results.
The difference between these approaches (non-linear adjustment) is material for
portfolios with high LGD or long remaining maturities.

## SCENARIO EXPLAINABILITY FOR GOVERNANCE COMMITTEE
For each quarterly scenario update, prepare:
  1. Scenario name and narrative description
  2. Key macroeconomic variables for each scenario (3-year forward path)
  3. Scenario weights and rationale for any weight changes from prior quarter
  4. ECL under each scenario individually
  5. Probability-weighted ECL (reported figure)
  6. Sensitivity: ECL if severe scenario were weighted 100% (IFRS 7 required)
  7. Changes from prior quarter: which scenarios/weights/variables changed and why

## FORWARD-LOOKING HORIZON
Explicit forecast horizon: typically 2–5 years (period with supportable forecasts)
Mean reversion: beyond explicit horizon, variables revert to long-run average
  over a reversion period (typically 2–5 additional years)
Perpetuity: beyond reversion period, variables held at long-run average

## GOVERNANCE OF SCENARIOS
Scenarios must be:
  - Approved by the IFRS 9 Governance Committee before each calculation
  - Sourced from a credible economic forecaster (internal Economics team or
    external provider: Oxford Economics, Moody's Analytics, Bloomberg)
  - Documented in detail in the IFRS 9 Governance Pack
  - Disclosed (key variables and weights) in the IFRS 7 notes
