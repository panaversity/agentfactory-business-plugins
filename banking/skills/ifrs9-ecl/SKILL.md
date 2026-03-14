---
name: ifrs9-ecl
description: >
  Activate for: IFRS 9, ECL, expected credit loss, PD, LGD, EAD,
  loan loss provision, impairment, 12-month ECL, lifetime ECL,
  post-model adjustment, PMA, IFRS 7, provision movement, forward-looking.
  NOT for: US GAAP CECL calculation (ASC 326), hedge accounting under
  IFRS 9, classification and measurement of financial instruments.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 9 Financial Instruments (IASB)"
  disclosure: "IFRS 7 Financial Instruments Disclosures"
  not_applicable_in: "USA (use CECL / FASB ASC 326 instead)"
---

## CORE PRINCIPLE

ECL is FORWARD-LOOKING and PROBABILITY-WEIGHTED.
It is NOT the incurred loss. It is the probability-weighted expectation of credit
losses given ALL reasonable and supportable information, including future economic
conditions. Never wait for objective evidence of impairment to recognise a loss.

## STAGE SUMMARY

| Stage   | Trigger                                       | ECL Horizon  | Interest Income                      |
| ------- | --------------------------------------------- | ------------ | ------------------------------------ |
| Stage 1 | No SICR since origination                     | 12-month ECL | On GROSS carrying amount             |
| Stage 2 | SICR since origination — see ifrs9-staging.md | Lifetime ECL | On GROSS carrying amount             |
| Stage 3 | Credit impairment occurred                    | Lifetime ECL | On NET carrying amount (gross - ECL) |

CRITICAL: Stage 3 interest is on the NET amount. Recognising Stage 3 interest on
the gross amount is a material accounting error.

## ECL FORMULAS

12-Month ECL (Stage 1):
ECL_12 = PD_12 x LGD x EAD

Lifetime ECL (Stage 2 and 3):
ECL_life = Sum_t [ PD_marginal_t x LGD_t x EAD_t x DF_t ]
where t = each future period until maturity
DF_t = discount factor at the asset's effective interest rate

Scenario-Weighted ECL (REQUIRED):
ECL = Sum_s ( Weight_s x ECL_scenario_s )
Weights must sum to 1.0 and reflect management's genuine scenario probability assessment

## DISCOUNT FACTOR TREATMENT

The discount factor (DF_t) is calculated using the asset's effective interest rate (EIR).
For floating-rate instruments: use current EIR at the reporting date.
For fixed-rate instruments: use the EIR at initial recognition.

DF_t = 1 / (1 + EIR)^t

Discounting matters because:

- Lifetime ECL for long-dated assets (e.g., 25-year mortgages) extends decades
- Without discounting, future losses are materially overstated in present-value terms
- The discount effect is largest for Stage 2 facilities with long remaining maturity

Example: A 1% marginal PD at year 20 with LGD 30% and EAD 100k:
Undiscounted: 1% x 30% x 100k = 300
Discounted at 4% EIR: 300 / (1.04)^20 = 137
The discount effect reduces the contribution by more than half.

## PD ESTIMATION

TTC PD: Long-run average over a full economic cycle — starting point only.
PIT PD: REQUIRED for IFRS 9. PIT PD = TTC PD x Credit Cycle Adjustment (CCA).
CCA > 1.0 in recession (PDs higher than long-run average)
CCA < 1.0 in expansion (PDs lower than long-run average)
CCA derived from macroeconomic satellite model — see ifrs9-scenarios.md

## LGD ESTIMATION

MUST use downturn/stressed collateral values. NOT current market values.
Mortgage LGD: LGD = MAX(0, EAD - Forced Sale Value) / EAD
Forced Sale Value = Market Value x (1 - forced sale haircut 15-25%)
Rule of thumb: LGD ~ 25-30% for LTV <= 80%; LGD ~ 35-50% for LTV > 80%
Unsecured consumer: LGD ~ 65-80%
Corporate unsecured senior: LGD ~ 40-60%

## PORTFOLIO SEGMENTATION

ECL models must be segmented by portfolios with homogeneous risk characteristics:

| Segment                | Typical PD Model                  | LGD Approach                      | Key Drivers               |
| ---------------------- | --------------------------------- | --------------------------------- | ------------------------- |
| Retail mortgages       | Behavioural scorecard             | Property collateral + forced sale | LTV, income, employment   |
| Consumer unsecured     | Behavioural scorecard             | Statistical cure rate model       | Utilisation, bureau score |
| SME                    | Application/behavioural scorecard | Collateral-dependent              | Revenue, leverage, age    |
| Corporate              | Rating model (PD master scale)    | Workout LGD                       | Financial ratios, sector  |
| Commercial real estate | Rating model                      | Property collateral               | LTV, DSCR, vacancy        |

## EAD AND CREDIT CONVERSION FACTORS (CCF)

Term loans: EAD = scheduled outstanding balance at default
Revolving facilities: EAD = Drawn balance + (CCF x Undrawn committed amount)
CCF: unconditionally cancellable ~ 0-10%; committed revolving corporate ~ 50-75%

## MACROECONOMIC SCENARIOS

Minimum: base + 1 upside + 1 adverse. Best practice: 4 scenarios.
Weights must reflect genuine management view — equal weights rarely defensible.
Common structure: Upside 15%, Base 40%, Adverse 30%, Severe 15%.
See ifrs9-scenarios.md for full satellite model framework.

## POST-MODEL ADJUSTMENTS (PMAs)

Required when known model limitation would cause material under/overstatement.
Common types: pandemic PMA, sector concentration PMA, new product PMA, climate PMA.
Each PMA must be: documented, committee-approved, time-limited, reviewed quarterly.
Aggregate PMA amount must be disclosed in IFRS 7 notes.
NEVER use PMAs to substitute management conservatism for model output.

## PROVISION MOVEMENT TABLE

Build every quarter. Every line must trace to a documented source:
Opening provision -> New business -> Stage 1->2 migration -> Stage 2->3 migration
-> Cures -> Repayments -> Write-offs -> Model parameter changes
-> Macro scenario changes -> PMA movements -> FX -> Closing provision

## IFRS 7 MANDATORY DISCLOSURES (minimum)

1. SICR criteria (quantitative and qualitative)
2. Definition of default used
3. Write-off policy
4. Macroeconomic scenarios: names, weights, key variables
5. Sensitivity analysis: single-scenario stress
6. Stage distribution table: count and amount by stage, by product
7. Stage migration table: movements with ECL impact
8. Credit quality distribution: by rating grade or score band
9. Post-model adjustments: aggregate amount and rationale
10. Modified financial assets: amounts and conditions

## OUTPUT FORMAT — ECL CALCULATION SUMMARY

```
ECL CALCULATION SUMMARY
Entity:             [Bank / Group name]
Reporting Date:     [YYYY-MM-DD]
Portfolio:          [Segment name]

INPUTS:
  Gross Carrying Amount:     [Amount]
  Stage Distribution:        Stage 1: [X%] | Stage 2: [Y%] | Stage 3: [Z%]
  PD (12-month, base):       [X.XX%]
  LGD:                       [X%]
  EAD:                       [Amount]
  Discount Rate (EIR):       [X.XX%]

SCENARIO ECL:
  Upside  ([W1]%):           [Amount]
  Base    ([W2]%):           [Amount]
  Adverse ([W3]%):           [Amount]
  Severe  ([W4]%):           [Amount]

WEIGHTED ECL:                [Amount]
  of which PMA:              [Amount] ([description])

PROVISION MOVEMENT:
  Opening:                   [Amount]
  Change this period:        [+/- Amount]
  Closing:                   [Amount]
```

## NEVER DO THESE

- NEVER calculate ECL using the incurred loss methodology
- NEVER apply a single macroeconomic scenario (must be probability-weighted)
- NEVER use TTC PD without PIT conversion
- NEVER use current market value of collateral (use downturn LGD)
- NEVER recognise Stage 3 interest on the gross amount
- NEVER omit the discount factor for lifetime ECL — undiscounted lifetime ECL materially overstates the provision for long-dated assets
- NEVER use PMAs as a substitute for fixing a known model deficiency — PMAs are temporary overlays, not permanent model corrections

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
