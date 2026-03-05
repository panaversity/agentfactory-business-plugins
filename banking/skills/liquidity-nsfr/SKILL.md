---
name: liquidity-nsfr
version: 1.0
description: >
  Activate for: NSFR, net stable funding ratio, available stable funding,
  required stable funding, ASF, RSF, structural liquidity, funding mismatch,
  term funding, long-term funding, stable funding, 1-year funding.
standard: Basel III Net Stable Funding Ratio (BCBS 2014)
author: Panaversity — The AI Agent Factory
---

## NSFR FORMULA
NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF) ≥ 100%

Purpose: Ensure banks maintain a stable funding profile over a 1-year time horizon,
reducing dependence on short-term wholesale funding that evaporated in 2008.

## AVAILABLE STABLE FUNDING (ASF) — FACTOR TABLE

| Funding Category | ASF Factor |
|---|---|
| Tier 1 and Tier 2 capital instruments | 100% |
| Other capital instruments with residual maturity ≥ 1 year | 100% |
| Stable retail deposits (insured) with maturity < 1 year | 95% |
| Less stable retail deposits with maturity < 1 year | 90% |
| Wholesale funding from non-financial corporates ≥ 1 year | 50% |
| Wholesale funding from non-financial corporates < 1 year | 50% |
| Operational deposits (wholesale) | 50% |
| Debt securities with residual maturity ≥ 1 year issued to retail | 100% |
| Debt securities with residual maturity ≥ 1 year (non-retail) | 100% |
| Other wholesale funding with residual maturity ≥ 6 months but < 1 year | 30% |
| Other wholesale funding with residual maturity < 6 months (financial institutions) | 0% |
| Other wholesale funding with residual maturity < 6 months (non-financial) | 50% |
| All other liabilities (derivatives, deferred tax, etc.) | 0% |

ASF = Σ (Funding amount × ASF factor)

## REQUIRED STABLE FUNDING (RSF) — FACTOR TABLE

| Asset Category | RSF Factor |
|---|---|
| Cash and unencumbered Level 1 HQLA | 0% |
| Unencumbered Level 2A HQLA | 15% |
| Unencumbered Level 2B HQLA (RMBS) | 25% |
| Unencumbered Level 2B HQLA (other) | 50% |
| Unencumbered loans to financial institutions < 6 months | 10% |
| Unencumbered loans to financial institutions ≥ 6 months, < 1 year | 15% |
| Unencumbered performing loans to non-financial corporates < 1 year | 50% |
| Unencumbered performing loans to retail/SME < 1 year | 50% |
| Unencumbered performing residential mortgages ≥ 1 year, RW ≤ 35% | 65% |
| Unencumbered performing loans to non-financial corporates ≥ 1 year | 65% |
| Unencumbered performing loans to retail/SME ≥ 1 year, not RW ≤ 35% | 85% |
| Non-HQLA securities | 50% |
| Non-performing loans (any maturity) | 100% (net of provisions) |
| Fixed assets (PP&E, goodwill, intangibles) | 100% |
| Off-balance-sheet: undrawn committed facilities | 5% |
| Derivatives: net positive fair value | 100% |
| All other assets | 100% |

RSF = Σ (Asset / off-balance-sheet amount × RSF factor)

## NSFR INTERPRETATION
NSFR > 100%: Stable funding surplus. Bank can absorb funding stress for > 1 year.
NSFR 100–105%: Meeting minimum but limited buffer. Review funding strategy.
NSFR < 100%: Regulatory breach. Immediate remediation required.

Management targets: Most major banks target 105–115% NSFR.

## NSFR vs. LCR — KEY DISTINCTION
LCR: Measures ability to survive a 30-day acute stress (short-term liquidity)
NSFR: Measures structural funding stability over 1 year (medium-term liquidity)
A bank can pass LCR but fail NSFR if it has short-term HQLA but mismatched
  long-term funding (long assets, short liabilities structurally).
Both metrics are required simultaneously — they address different risk horizons.

## ENCUMBERED ASSETS
Encumbered assets (pledged as collateral, subject to repo, in securitisation pool)
receive a RSF factor based on the remaining term of the encumbrance:
  Encumbered for ≥ 1 year: 100% RSF
  Encumbered for 6 months–1 year: the RSF factor of unencumbered equivalent
  Encumbered for < 6 months: the RSF factor of unencumbered equivalent
