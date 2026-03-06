---
name: liquidity-lcr
version: 1.0
description: >
  Activate for: LCR, liquidity coverage ratio, HQLA, high quality liquid assets,
  net cash outflow, run-off rate, Level 1 assets, Level 2A, Level 2B, 30-day
  stress scenario, liquidity buffer, liquidity coverage, cash outflow, inflow cap.
  NOT for: structural funding / NSFR calculations (use liquidity-nsfr), capital
  adequacy ratios (use basel-capital), interest rate risk in the banking book (IRRBB).
standard: Basel III Liquidity Coverage Ratio (BCBS 2013, updated 2014)
author: Panaversity — The AI Agent Factory
---

## LCR FORMULA
LCR = HQLA Stock / Total Net Cash Outflows (30-day stress) >= 100%

Minimum regulatory: 100%
Management buffer best practice: 110-130% (gives operating room above minimum)

## HQLA CATEGORISATION AND HAIRCUTS

### Level 1 Assets — No Haircut
- Coins and banknotes
- Central bank reserves (eligible for withdrawal in stress)
- Central government / central bank bonds in domestic currency
- Central government / central bank bonds in foreign currency (up to 15% cap per currency)
- Qualifying 0% risk weight sovereign bonds in Basel SA
Level 1 assets: NO haircut, NO cap as proportion of HQLA.

### Level 2A Assets — 15% Haircut
- Sovereign / central bank / MDB bonds rated AA- or above (not qualifying for Level 1)
- Non-0% RW sovereign bonds from countries with low risk
- Qualifying corporate bonds rated AA- or above
- Qualifying covered bonds rated AA or above
Level 2A assets after haircut: capped at 40% of total HQLA after haircuts.

### Level 2B Assets — 25-50% Haircuts (national discretion to include)
- Qualifying RMBS (residential mortgage-backed securities): 25% haircut
- Qualifying corporate bonds rated A+ to BBB-: 50% haircut
- Qualifying equities in main stock index: 50% haircut
Level 2B assets after haircut: capped at 15% of total HQLA after haircuts.
Combined Level 2A + 2B cap: 40% of total HQLA after haircuts.

## HQLA CALCULATION EXAMPLE — WITH LEVEL 2 CAP CHECK
Level 1: 800M x 100% = 800M
Level 2A: 100M x 85% = 85M
Level 2B: 60M x 75% = 45M (after 25% RMBS haircut)
Subtotal before cap: 930M
Level 2 cap check: Level 2 = 130M. 40% of 930M = 372M. Cap not binding.
HQLA Stock = 930M

### Example Where Level 2 Cap IS Binding
Level 1: 200M x 100% = 200M
Level 2A: 200M x 85% = 170M
Level 2B: 100M x 50% = 50M (after 50% equity haircut)
Subtotal before cap: 420M
Level 2 cap check: Level 2 = 220M. 40% of 420M = 168M. CAP IS BINDING.
Adjusted Level 2 = 168M. Excess 52M excluded.
HQLA Stock = 200M + 168M = 368M (not 420M)

The Level 2 cap commonly binds for banks with limited sovereign bond portfolios
that rely heavily on corporate bonds or RMBS for their liquidity buffer.

## CASH OUTFLOWS — KEY RUN-OFF RATES

### Retail Deposits
| Category | Run-off Rate |
|---|---|
| Stable retail deposits (insured, established relationship) | 3% |
| Less stable retail deposits (uninsured, online, new customers) | 10% |
| Very high rate / promotional deposits | 20% |

### Wholesale Deposits
| Category | Run-off Rate |
|---|---|
| Non-financial corporate (operational) | 25% |
| Non-financial corporate (non-operational) | 40% |
| Financial institution (non-operational) | 100% |
| Central bank / sovereign (operational) | 25% |
| Secured funding (government collateral) | 0% |
| Secured funding (non-HQLA collateral) | 25% |
| Unsecured wholesale < 30 days (financial) | 100% |

### Off-Balance-Sheet
| Facility Type | Drawdown Rate |
|---|---|
| Credit facilities to retail customers | 5% |
| Credit facilities to non-financial corporates | 10% |
| Credit facilities to financial institutions | 40% |
| Liquidity facilities to SPVs / conduits | 100% |
| Committed undrawn facilities (unconditional cancellable) | 0% |

## CASH INFLOWS — KEY RATES AND 75% CAP
Maturing secured lending collateralised by HQLA: 0% (assumed rolled)
Maturing secured lending collateralised by non-HQLA: 100%
Retail customer loan repayments: 50%
Non-financial corporate loan repayments: 100%
Financial institution loan repayments: 100%

CRITICAL: Total inflows are CAPPED at 75% of total outflows.
Net Cash Outflows = Total Outflows - MIN(Total Inflows, 75% x Total Outflows)

## OPERATIONAL DEPOSITS
Operational deposits (funds held for clearing, custody, cash management):
  May receive lower run-off treatment (25%) if the bank is the core relationship
  provider and the customer has no practical alternative for these services.
  Operational determination requires documented evidence of operational relationship.

## INTRADAY LIQUIDITY
LCR measures 30-day liquidity. Banks also need intraday liquidity for payment
system settlement. BCBS monitoring tools (April 2013) address intraday liquidity
separately — check jurisdiction overlay for monitoring requirements.

## OUTPUT FORMAT — LCR REPORT

```
LCR CALCULATION REPORT
As at:              [YYYY-MM-DD]
Entity:             [Bank / Group name]
Currency:           [Reporting currency]

HIGH QUALITY LIQUID ASSETS (HQLA):
  Level 1 assets:                   [Amount] x 100% = [After haircut]
  Level 2A assets:                  [Amount] x 85%  = [After haircut]
  Level 2B assets:                  [Amount] x [%]  = [After haircut]
  Subtotal before cap:              [Amount]
  Level 2 cap (40%):                [Binding? Y/N — adjusted amount]
  TOTAL HQLA:                       [Amount]

CASH OUTFLOWS (30-day stress):
  Retail deposits:                  [Amount] x [rate] = [Outflow]
  Wholesale non-operational:        [Amount] x [rate] = [Outflow]
  Wholesale operational:            [Amount] x [rate] = [Outflow]
  Secured funding:                  [Amount] x [rate] = [Outflow]
  Off-balance-sheet:                [Amount] x [rate] = [Outflow]
  TOTAL OUTFLOWS:                   [Amount]

CASH INFLOWS:
  Maturing secured (non-HQLA):      [Amount] x 100% = [Inflow]
  Loan repayments:                  [Amount] x [rate] = [Inflow]
  TOTAL INFLOWS (before cap):       [Amount]
  75% CAP:                          [75% x Total Outflows]
  INFLOWS RECOGNISED:               MIN([Inflows], [Cap])

NET CASH OUTFLOWS:                  [Outflows - Inflows Recognised]
LCR:                                [HQLA / Net Cash Outflows] = [Ratio]%
Regulatory Minimum:                 100%
Management Target:                  [Target]%
```

## NEVER DO THESE
- NEVER include Level 2B assets without checking if jurisdiction permits them (national discretion)
- NEVER forget the combined 40% Level 2 cap
- NEVER forget the 75% inflow cap (can't assume all counterparties pay)
- NEVER include encumbered assets in HQLA (must be unencumbered)
- NEVER double-count assets that are both HQLA and maturing loan collateral
- NEVER classify deposits as "operational" without documented evidence of the operational relationship — regulators audit operational deposit determinations closely

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
