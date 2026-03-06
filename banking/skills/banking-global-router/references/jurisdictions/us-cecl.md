---
name: us-cecl
version: 1.0
description: >
  Comparison overlay for US CECL (ASC 326 — Current Expected Credit Losses)
  versus IFRS 9 ECL. NOT a full US jurisdiction overlay for Basel/AML — this
  file specifically covers the ECL measurement differences that affect cross-border
  banks and analysts comparing US GAAP and IFRS approaches to credit impairment.
standard_us: ASC 326 (FASB Accounting Standards Update 2016-13)
standard_ifrs: IFRS 9 Financial Instruments (IASB, 2014)
us_regulators: Federal Reserve, OCC, FDIC
effective_dates:
  large_sec_filers: 2020-01-01
  smaller_reporting: 2023-01-01
author: Panaversity — The AI Agent Factory
---

## CORE DIFFERENCE — STAGING vs NO STAGING

IFRS 9 uses a three-stage model:

- Stage 1: 12-month ECL (no SICR since origination)
- Stage 2: Lifetime ECL (SICR identified, not credit-impaired)
- Stage 3: Lifetime ECL (credit-impaired)
- Transition from Stage 1 to Stage 2 requires a "significant increase in credit risk" (SICR) assessment

CECL (ASC 326) has NO staging model:

- ALL financial assets measured at amortized cost carry a lifetime ECL allowance from Day 1
- No SICR trigger — no cliff effect between 12-month and lifetime measurement
- No distinction between performing and underperforming (until formal non-accrual)
- Result: higher Day 1 allowances, but no sudden Stage 2 migration spikes

## MEASUREMENT APPROACH

IFRS 9 ECL:

- Uses probability-weighted scenarios (minimum 3: base, upside, downside)
- Forward-looking macro variables with explicit scenario weights
- PD x LGD x EAD formula applied per scenario, then weighted
- Discount rate: original effective interest rate
- Reasonable and supportable forecast period + reversion to historical loss

CECL (ASC 326):

- Uses "reasonable and supportable forecasts" of expected credit losses
- Methodologies: vintage analysis, loss rate, probability of default, discounted cash flow
- Forecast period: entity-specific — must be reasonable and supportable
- Beyond the forecast period: revert immediately to historical loss experience
- Discount rate: not required for non-DCF methods (many US banks use undiscounted loss rates)
- Single best estimate permitted (no explicit probability-weighting requirement, though permitted)

## DAY 1 IMPACT COMPARISON

CECL Day 1 impact was significantly larger than IFRS 9 Day 1:

- CECL: Large US banks reported 20-50% increases in allowances on adoption (January 1, 2020)
- IFRS 9: Typical Day 1 increase was 10-30% (Stage 1 = 12-month ECL only)
- Root cause: CECL requires lifetime ECL on ALL assets, including healthy Stage 1 equivalents

Ongoing measurement:

- IFRS 9 shows more volatility because Stage 2 migration creates sharp ECL increases when credit deteriorates
- CECL shows more stability because lifetime ECL is already recognized — deterioration increases the estimate but without a cliff
- IFRS 9 has lower allowances in benign environments (Stage 1 = 12-month only)
- CECL has higher allowances in benign environments (lifetime ECL on all assets)

## PD / LGD / EAD FRAMEWORK

IFRS 9: Explicit PD x LGD x EAD framework is standard practice

- 12-month PD for Stage 1, lifetime PD for Stage 2/3
- PIT PD conversion required (TTC PD adjusted for point-in-time macro conditions)
- LGD includes forward-looking collateral values and recovery estimates
- EAD includes undrawn commitments via credit conversion factors (CCF)

CECL: PD x LGD x EAD is one permitted methodology, but not required

- Many US banks use loss rate methods (historical loss rates adjusted for current conditions)
- Vintage analysis: track losses by origination cohort and project remaining lifetime losses
- DCF method: project expected cash flows and discount at original effective rate; smaller banks often use WARM method

## CAPITAL INTERACTION

IFRS 9 capital impact:

- IFRS 9 provisions interact with Basel IRB expected loss (EL)
- If IFRS 9 ECL > IRB EL: excess added to Tier 2 (capped at 0.6% credit RWA)
- If IRB EL > IFRS 9 ECL: shortfall deducted from CET1
- IFRS 9 transitional arrangements phased in 2018-2022 (now fully loaded)

CECL capital impact:

- US banking agencies provided a 3-year phase-in for CECL Day 1 impact on regulatory capital
- Phase-in: 25% of CECL Day 1 impact recognized per year (2020-2022 for large banks; extended for COVID)
- COVID modification: 5-year phase-in option available for banks adopting CECL 2020-2021
- Standardised Approach banks: CECL allowances reduce RWA exposure measure (credit risk mitigation)
- Advanced Approach (IRB) banks: same shortfall/excess framework as IFRS 9

## KEY DIFFERENCES SUMMARY

| Dimension                | IFRS 9                         | CECL (ASC 326)                    |
| ------------------------ | ------------------------------ | --------------------------------- |
| Staging                  | 3-stage model (1/2/3)          | No staging — lifetime for all     |
| SICR trigger             | Required (30 DPD rebuttable)   | Not applicable                    |
| Day 1 performing assets  | 12-month ECL only              | Lifetime ECL                      |
| Scenario weighting       | Mandatory multiple scenarios   | Single estimate permitted         |
| Forecast reversion       | Gradual reversion permitted    | Immediate reversion to historical |
| Discounting              | Required at original EIR       | Not required for all methods      |
| Volatility profile       | Higher (Stage 2 cliff)         | Lower (already lifetime)          |
| Allowance level (benign) | Lower (12-month on performing) | Higher (lifetime on all)          |
| Effective date           | 2018                           | 2020 (large) / 2023 (smaller)     |

## CROSS-BORDER IMPLICATIONS

Banks operating under both regimes (e.g., UK/EU bank with US subsidiary, or US bank with UK branch):

- Must maintain dual impairment calculations: IFRS 9 for group reporting, CECL for US entity
- Consolidation adjustments required at group level
- Scenario frameworks and regulatory capital may differ between home and host supervisors due to methodology and provisioning differences
