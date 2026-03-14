---
name: liquidity-nsfr
description: >
  Activate for: NSFR, net stable funding ratio, available stable funding,
  required stable funding, ASF, RSF, structural liquidity, funding mismatch,
  term funding, long-term funding, stable funding, 1-year funding.
  NOT for: short-term liquidity stress (use liquidity-lcr), intraday liquidity
  monitoring, interest rate risk in the banking book (IRRBB), market risk capital.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III Net Stable Funding Ratio (BCBS 2014)"
---

## NSFR FORMULA

NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF) >= 100%

Purpose: Ensure banks maintain a stable funding profile over a 1-year time horizon,
reducing dependence on short-term wholesale funding that evaporated in 2008.

## AVAILABLE STABLE FUNDING (ASF) — FACTOR TABLE

| Funding Category                                                                   | ASF Factor |
| ---------------------------------------------------------------------------------- | ---------- |
| Tier 1 and Tier 2 capital instruments                                              | 100%       |
| Other capital instruments with residual maturity >= 1 year                         | 100%       |
| Stable retail deposits (insured) with maturity < 1 year                            | 95%        |
| Less stable retail deposits with maturity < 1 year                                 | 90%        |
| Wholesale funding from non-financial corporates >= 1 year                          | 50%        |
| Wholesale funding from non-financial corporates < 1 year                           | 50%        |
| Operational deposits (wholesale)                                                   | 50%        |
| Debt securities with residual maturity >= 1 year issued to retail                  | 100%       |
| Debt securities with residual maturity >= 1 year (non-retail)                      | 100%       |
| Other wholesale funding with residual maturity >= 6 months but < 1 year            | 30%        |
| Other wholesale funding with residual maturity < 6 months (financial institutions) | 0%         |
| Other wholesale funding with residual maturity < 6 months (non-financial)          | 50%        |
| All other liabilities (derivatives, deferred tax, etc.)                            | 0%         |

ASF = Sum (Funding amount x ASF factor)

## REQUIRED STABLE FUNDING (RSF) — FACTOR TABLE

| Asset Category                                                       | RSF Factor               |
| -------------------------------------------------------------------- | ------------------------ |
| Cash and unencumbered Level 1 HQLA                                   | 0%                       |
| Unencumbered Level 2A HQLA                                           | 15%                      |
| Unencumbered Level 2B HQLA (RMBS)                                    | 25%                      |
| Unencumbered Level 2B HQLA (other)                                   | 50%                      |
| Unencumbered loans to financial institutions < 6 months              | 10%                      |
| Unencumbered loans to financial institutions >= 6 months, < 1 year   | 15%                      |
| Unencumbered performing loans to non-financial corporates < 1 year   | 50%                      |
| Unencumbered performing loans to retail/SME < 1 year                 | 50%                      |
| Unencumbered performing residential mortgages >= 1 year, RW <= 35%   | 65%                      |
| Unencumbered performing loans to non-financial corporates >= 1 year  | 65%                      |
| Unencumbered performing loans to retail/SME >= 1 year, not RW <= 35% | 85%                      |
| Non-HQLA securities                                                  | 50%                      |
| Non-performing loans (any maturity)                                  | 100% (net of provisions) |
| Fixed assets (PP&E, goodwill, intangibles)                           | 100%                     |
| Off-balance-sheet: undrawn committed facilities                      | 5%                       |
| Derivatives: net positive fair value                                 | 100%                     |
| All other assets                                                     | 100%                     |

RSF = Sum (Asset / off-balance-sheet amount x RSF factor)

## NSFR WORKED EXAMPLE

| Item                                     | Amount (M) | Factor | Weighted (M) |
| ---------------------------------------- | ---------- | ------ | ------------ |
| **ASF Side**                             |            |        |              |
| CET1 + AT1 + T2 capital                  | 5,000      | 100%   | 5,000        |
| Stable retail deposits                   | 20,000     | 95%    | 19,000       |
| Less stable retail deposits              | 8,000      | 90%    | 7,200        |
| Wholesale NFC < 1 year                   | 6,000      | 50%    | 3,000        |
| Wholesale FI < 6 months                  | 4,000      | 0%     | 0            |
| Senior debt >= 1 year                    | 3,000      | 100%   | 3,000        |
| **Total ASF**                            |            |        | **37,200**   |
| **RSF Side**                             |            |        |              |
| Cash + central bank reserves             | 6,000      | 0%     | 0            |
| Level 2A sovereign bonds                 | 2,000      | 15%    | 300          |
| Performing mortgages >= 1 yr (RW <= 35%) | 15,000     | 65%    | 9,750        |
| Performing corporate loans >= 1 yr       | 10,000     | 65%    | 6,500        |
| Performing retail/SME >= 1 yr            | 5,000      | 85%    | 4,250        |
| Non-performing loans (net)               | 1,000      | 100%   | 1,000        |
| Fixed assets                             | 500        | 100%   | 500          |
| Off-BS undrawn commitments               | 8,000      | 5%     | 400          |
| Other assets                             | 2,000      | 100%   | 2,000        |
| **Total RSF**                            |            |        | **24,700**   |
| **NSFR**                                 |            |        | **150.6%**   |

In this example NSFR = 37,200 / 24,700 = 150.6% — well above the 100% minimum.

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
Encumbered for >= 1 year: 100% RSF
Encumbered for 6 months–1 year: the RSF factor of unencumbered equivalent
Encumbered for < 6 months: the RSF factor of unencumbered equivalent

## COMMON NSFR MANAGEMENT ACTIONS

When NSFR is under pressure, banks typically consider:

- Issue longer-term debt (converts 0% ASF short-term into 100% ASF long-term)
- Grow retail deposit base (95% ASF factor vs 0% for short-term wholesale)
- Reduce long-dated illiquid assets (lowers RSF requirement)
- Securitise mortgage or loan portfolios (removes assets from balance sheet)
- Increase central bank reserve holdings (0% RSF, funded by term liabilities)

## OUTPUT FORMAT — NSFR REPORT

```
NSFR CALCULATION REPORT
As at:              [YYYY-MM-DD]
Entity:             [Bank / Group name]
Currency:           [Reporting currency]

AVAILABLE STABLE FUNDING (ASF)
  Capital instruments:              [Amount] x 100% = [Weighted]
  Stable retail deposits:           [Amount] x 95%  = [Weighted]
  Less stable retail deposits:      [Amount] x 90%  = [Weighted]
  Wholesale NFC >= 1 year:          [Amount] x 50%  = [Weighted]
  Other wholesale >= 6M < 1 year:   [Amount] x 30%  = [Weighted]
  Short-term wholesale (FI):        [Amount] x 0%   = [Weighted]
  TOTAL ASF:                        [Total]

REQUIRED STABLE FUNDING (RSF)
  Cash and Level 1 HQLA:            [Amount] x 0%   = [Weighted]
  Level 2 HQLA:                     [Amount] x 15%  = [Weighted]
  Performing mortgages:              [Amount] x 65%  = [Weighted]
  Performing corporate loans:        [Amount] x 65%  = [Weighted]
  Non-performing loans:              [Amount] x 100% = [Weighted]
  Off-balance-sheet commitments:     [Amount] x 5%   = [Weighted]
  TOTAL RSF:                        [Total]

NSFR:                               [ASF / RSF] = [Ratio]%
Regulatory Minimum:                 100%
Management Target:                  [Target]%
Buffer over Minimum:                [Ratio - 100]%
```

## NEVER DO THESE

- NEVER confuse NSFR with LCR — NSFR addresses 1-year structural funding, LCR addresses 30-day acute stress; using LCR factors for NSFR calculation produces materially wrong results
- NEVER assign a non-zero ASF factor to short-term wholesale funding from financial institutions (< 6 months) — the factor is 0% because this funding is assumed to disappear entirely in stress
- NEVER ignore the RSF charge on off-balance-sheet committed facilities — the 5% RSF factor applies to the full undrawn amount and is material for banks with large commitment books
- NEVER treat encumbered assets the same as unencumbered — encumbered assets receive 100% RSF if the encumbrance exceeds 1 year, regardless of the underlying asset quality

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
