---
name: ifrs9-scenarios
version: 1.0
description: >
  Activate for: macro overlay, macroeconomic scenarios, PIT PD,
  point-in-time PD, credit cycle adjustment, scenario weighting,
  forward-looking information, satellite model, GDP, unemployment,
  house price index, IFRS 9 scenarios, scenario probability.
  NOT for: ECL calculation mechanics (use ifrs9-ecl), staging assessment
  (use ifrs9-staging), stress testing for capital adequacy (use stress-testing).
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

| Scenario | Typical Weight | Key Feature                                  |
| -------- | -------------- | -------------------------------------------- |
| Upside   | 10–20%         | Above-trend growth, falling unemployment     |
| Base     | 35–50%         | Central forecast, moderate conditions        |
| Adverse  | 25–35%         | Mild recession, rising unemployment          |
| Severe   | 10–20%         | Deep recession, sharply falling asset prices |

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

PIT PD = TTC PD x CCA
CCA is estimated from a satellite model. Typical satellite model form:
ln(CCA) = a + b1(GDP_growth) + b2(Unemployment) + b3(HPI_growth) + e

Example CCA values:
Severe recession: CCA = 1.8–2.5 (PDs 80–150% above long-run average)
Adverse: CCA = 1.2–1.5
Base: CCA ~ 1.0 (by definition — TTC PD already reflects long-run average)
Upside: CCA = 0.7–0.9 (PDs below long-run average)

## SATELLITE MODEL DETAIL

### Model Structure

The satellite model links macroeconomic variables to credit risk parameters.
Typical specification for a UK mortgage portfolio:

ln(Default Rate*t) = a + b1 * Unemployment_t + b2 * HPI_growth_t + b3 * Base_Rate_t + b4 * ln(Default Rate*{t-1}) + e_t

Key requirements for the satellite model:

- Estimated on a sufficiently long time series (minimum 1 full cycle, ideally 2+)
- Must include at least one recession period in calibration data
- Coefficients must have economically intuitive signs (e.g., higher unemployment
  increases default rates)
- Out-of-sample validation required (typically holdout the most recent 2–3 years)
- R-squared typically 0.6–0.85 for well-specified models

### Model Validation Requirements

- Annual independent validation by Model Risk Management
- Backtesting: compare predicted vs actual default rates over rolling windows
- Sensitivity testing: how much does ECL change for a 1pp change in each variable?
- Benchmarking: compare against external provider models (Moody's, Oxford Economics)

## WEIGHTED ECL CALCULATION

Step 1: Calculate PIT PD for each scenario using scenario-specific CCA
Step 2: Calculate ECL for each scenario: ECL_s = PD_PIT_s x LGD x EAD (Stage 1)
or ECL_s = Sum_t [PD_marginal_t_s x LGD_t x EAD_t x DF_t] (Stage 2/3)
Step 3: Weighted ECL = Sum_s (Weight_s x ECL_s)

## NON-LINEAR EFFECTS

Weighted ECL != ECL at weighted-average PD (due to non-linearity in ECL formula).
Always calculate ECL for each scenario separately, then probability-weight the results.
The difference between these approaches (non-linear adjustment) is material for
portfolios with high LGD or long remaining maturities.

### Non-Linearity Worked Example

Portfolio: 1,000M gross carrying amount, LGD = 40%

| Scenario | Weight | PIT PD | ECL (PD x LGD x EAD) |
| -------- | ------ | ------ | -------------------- |
| Upside   | 15%    | 0.8%   | 3.2M                 |
| Base     | 40%    | 1.5%   | 6.0M                 |
| Adverse  | 30%    | 3.0%   | 12.0M                |
| Severe   | 15%    | 6.0%   | 24.0M                |

Correct: Weighted ECL = 0.15 x 3.2 + 0.40 x 6.0 + 0.30 x 12.0 + 0.15 x 24.0 = 10.08M
Wrong: Weighted PD = 0.15 x 0.8 + 0.40 x 1.5 + 0.30 x 3.0 + 0.15 x 6.0 = 2.52%
ECL at weighted PD = 2.52% x 40% x 1,000 = 10.08M (linear case — same)

For lifetime ECL with compounding and discounting, the non-linear effect becomes
material (typically 5–15% higher ECL when correctly scenario-weighted).

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

### Governance Calendar — Typical Quarterly Cycle

| Week    | Activity                                             | Owner                 |
| ------- | ---------------------------------------------------- | --------------------- |
| Week 1  | Economics team produces draft scenarios              | Chief Economist       |
| Week 2  | Model Risk reviews satellite model outputs           | Model Risk Management |
| Week 3  | IFRS 9 Governance Committee reviews and approves     | CRO / CFO             |
| Week 4  | ECL calculation run with approved scenarios          | Finance / Credit Risk |
| Week 4+ | Results reviewed, PMAs assessed, disclosures drafted | Finance               |

## OUTPUT FORMAT — SCENARIO SUMMARY

```
IFRS 9 SCENARIO SUMMARY
Reporting Date:     [YYYY-MM-DD]
Entity:             [Bank / Group name]
Approved By:        [IFRS 9 Governance Committee, date]

SCENARIO DEFINITIONS:
| Scenario | Weight | GDP (Y1/Y2/Y3) | Unemployment (Y1/Y2/Y3) | HPI (Y1/Y2/Y3) |
|----------|--------|-----------------|--------------------------|-----------------|
| Upside   | [%]    | [%/%/%]         | [%/%/%]                  | [%/%/%]         |
| Base     | [%]    | [%/%/%]         | [%/%/%]                  | [%/%/%]         |
| Adverse  | [%]    | [%/%/%]         | [%/%/%]                  | [%/%/%]         |
| Severe   | [%]    | [%/%/%]         | [%/%/%]                  | [%/%/%]         |

ECL BY SCENARIO:
| Scenario | ECL (M) | vs Prior Quarter |
|----------|---------|------------------|
| Upside   | [X]     | [+/- Y]          |
| Base     | [X]     | [+/- Y]          |
| Adverse  | [X]     | [+/- Y]          |
| Severe   | [X]     | [+/- Y]          |
| Weighted | [X]     | [+/- Y]          |

SENSITIVITY (IFRS 7.35G):
  100% Severe scenario ECL:   [Amount] ([+X%] vs reported)
  100% Upside scenario ECL:   [Amount] ([-X%] vs reported)
```

## NEVER DO THESE

- NEVER use a single macroeconomic scenario for IFRS 9 ECL — this is non-compliant with IFRS 9.5.5.17 and will result in a qualified audit opinion
- NEVER apply equal scenario weights (25% each) without documented justification — auditors treat equal weighting as a rebuttable presumption of inadequate governance
- NEVER calculate ECL at the weighted-average PD instead of weighting scenario-level ECLs — the non-linear effect is material for lifetime ECL portfolios
- NEVER use a satellite model calibrated on data that excludes a recession period — the model will systematically underestimate adverse and severe scenario PDs
- NEVER change scenario weights between quarters without documented rationale approved by the Governance Committee — unexplained weight changes are a common audit finding

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
