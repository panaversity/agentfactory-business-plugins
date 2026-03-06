---
name: basel-capital
version: 1.0
description: >
  Activate for: CET1, Tier 1, Total Capital, capital ratio, RWA, risk-weighted
  assets, Basel III, Basel IV, capital adequacy, capital buffers, MDA, maximum
  distributable amount, leverage ratio, ICAAP, output floor, Pillar 2, CCB,
  CCyB, G-SIB, D-SIB, capital conservation buffer.
  NOT for: credit risk RWA calculation detail (use basel-rwa-credit), market risk
  FRTB capital (use basel-rwa-market), liquidity ratios LCR/NSFR (use liquidity-lcr
  / liquidity-nsfr).
standard: Basel III (BCBS) — jurisdiction implementations vary (load overlay)
author: Panaversity — The AI Agent Factory
---

## CAPITAL COMPONENTS

### CET1 (Common Equity Tier 1)
CET1 = Ordinary share capital
      + Share premium account
      + Retained earnings
      + Accumulated other comprehensive income (AOCI)
      - Goodwill and other intangible assets (net of deferred tax)
      - Deferred tax assets dependent on future profitability
      - Significant investments in financial institutions (>10% threshold)
      - Excess of regulatory expected loss over IFRS provisions (IRB banks)
      - Other regulatory deductions (jurisdiction-specific — load overlay)

### Additional Tier 1 (AT1)
Perpetual instruments with mandatory loss absorption.
Must be: perpetual; fully discretionary distributions; absorb losses on going concern.
Contingent convertibles (CoCos) / write-down instruments qualifying as AT1.
AT1 coupons subject to MDA restrictions if CET1 in combined buffer requirement zone.

#### AT1 Trigger Mechanics
CoCo bonds have contractual triggers for conversion or write-down:
  - Low trigger: 5.125% CET1 ratio — instrument converts to equity or writes down
  - High trigger: 7.0% CET1 ratio — required by some regulators (PRA for UK G-SIBs)
When triggered: AT1 converts to ordinary shares (diluting existing shareholders)
  or writes down to zero (permanent or temporary, per instrument terms).
The conversion ratio determines how many shares the AT1 holder receives.
Post-conversion: CET1 increases by the amount of AT1 converted; AT1 decreases.
This mechanism is critical in stress testing — approaching trigger levels
  can itself accelerate market panic and deposit outflows.

### Tier 2
Subordinated debt: minimum 5-year original maturity, amortised in final 5 years.
Eligible IFRS provisions: excess of IFRS provisions over IRB expected loss,
  capped at 0.6% of credit RWA.
General loan-loss reserves (SA banks): up to 1.25% of credit RWA.

## CAPITAL RATIO CALCULATIONS

CET1 Ratio = CET1 Capital / Total RWA
Tier 1 Ratio = (CET1 + AT1) / Total RWA
Total Capital Ratio = (CET1 + AT1 + T2) / Total RWA
Leverage Ratio = Tier 1 Capital / Total Exposure Measure

## RISK-WEIGHTED ASSETS COMPONENTS
Total RWA = Credit RWA + Market RWA + Operational RWA + CVA RWA
See products/basel-rwa-credit.md for credit RWA calculation.

## MINIMUM REQUIREMENTS (BASEL III GLOBAL STANDARDS)
CET1: 4.5% | Tier 1: 6.0% | Total Capital: 8.0% | Leverage: 3.0%
Load jurisdiction overlay for local minimums (UK, EU, US, APRA, MAS all differ).

## CAPITAL BUFFERS (add to minimums above)
Capital Conservation Buffer (CCB): 2.5% (all banks, all jurisdictions)
Countercyclical Capital Buffer (CCyB): 0.0%-2.5% (set by national authority)
  CCyB is RELEASED in a downturn — always check current rate for the jurisdiction
G-SIB surcharge: 1.0%-3.5% (global systemically important banks, FSOC/FSB list)
D-SIB / O-SII surcharge: 0.0%-3.0% (domestic systemically important banks)
Systemic Risk Buffer (SyRB): varies by jurisdiction (EU/UK only)

### Buffer Stacking — Effective CET1 Requirement
Buffers stack on top of the CET1 minimum. Example for a UK G-SIB:

| Component | Rate | Cumulative |
|---|---|---|
| CET1 hard minimum | 4.5% | 4.5% |
| + CCB | 2.5% | 7.0% |
| + CCyB (UK current rate — check BoE) | 2.0% | 9.0% |
| + G-SIB surcharge | 1.5% | 10.5% |
| + Systemic Risk Buffer (if applicable) | 1.0% | 11.5% |
| + Pillar 2A (bank-specific, confidential) | ~1.5% | ~13.0% |
| + Management buffer (internal) | ~1.5% | ~14.5% |

The effective CET1 a large UK bank targets is therefore ~14-15%, well above
the 4.5% Basel III minimum. Breaching ANY buffer layer triggers restrictions.

## MAXIMUM DISTRIBUTABLE AMOUNT (MDA)
MDA restrictions apply when CET1 falls INTO the combined buffer requirement
(i.e., below [4.5% + CCB + CCyB + surcharge] but above the 4.5% hard minimum).

| % of Combined Buffer Remaining | Max % of Profits Distributable |
|---|---|
| 0-25% | 0% |
| 25-50% | 20% |
| 50-75% | 40% |
| 75-100% | 60% |
| Above 100% (fully met) | No restriction |

MDA restrictions apply to: ordinary dividends, AT1 coupon payments,
discretionary staff variable remuneration above regulatory threshold.

## BASEL IV OUTPUT FLOOR
IRB-calculated credit RWA must be >= 72.5% of SA RWA for the same portfolio.
If IRB RWA < 72.5% x SA RWA -> use SA RWA x 72.5% as the binding RWA.
Phase-in: gradual from 2025 to full implementation 2030 (varies by jurisdiction).
This is the most consequential Basel IV change for large IRB banks.

## LEVERAGE RATIO DETAIL
Total Exposure Measure =
  On-balance-sheet assets (net of eligible credit risk mitigation)
  + Derivative exposures (at replacement cost + potential future exposure)
  + Securities financing transaction exposures
  + Off-balance-sheet items (x 100% CCF, or 10% for unconditionally cancellable)
Note: Leverage ratio can be the BINDING capital constraint for banks holding large
  pools of low-risk assets (government bonds, central bank reserves at 0% RW but
  full leverage exposure). This often drives the treasury/balance sheet strategy.

## OUTPUT FORMAT — CAPITAL ADEQUACY REPORT

```
CAPITAL ADEQUACY REPORT
Entity:             [Bank / Group name]
Reporting Date:     [YYYY-MM-DD]
Jurisdiction:       [UK PRA / EU CRR / US Fed / etc.]

CAPITAL COMPONENTS (M):
  CET1 Capital:                    [Amount]
  AT1 Capital:                     [Amount]
  Tier 1 Capital:                  [Amount]
  Tier 2 Capital:                  [Amount]
  Total Capital:                   [Amount]

RISK-WEIGHTED ASSETS (M):
  Credit RWA:                      [Amount]
  Market RWA:                      [Amount]
  Operational RWA:                 [Amount]
  CVA RWA:                         [Amount]
  Total RWA:                       [Amount]
  Output Floor RWA (if binding):   [Amount]

CAPITAL RATIOS:
  CET1 Ratio:                      [X.X%]
  Tier 1 Ratio:                    [X.X%]
  Total Capital Ratio:             [X.X%]
  Leverage Ratio:                  [X.X%]

BUFFER POSITION:
  Combined buffer requirement:     [X.X%]
  Distance to MDA trigger:         [+/- X.X pp]
  Buffer utilisation:              [X%] of combined buffer
```

## NEVER DO THESE
- NEVER deduct IFRS provisions directly from CET1 without checking IRB shortfall calculation
- NEVER omit goodwill and intangibles from CET1 deductions
- NEVER apply 0% risk weight to non-domestic-currency sovereign bonds under SA
- NEVER forget output floor check for IRB banks (Basel IV)
- NEVER conflate capital adequacy and liquidity — they are separate regulatory frameworks
- NEVER ignore AT1 trigger mechanics when CET1 approaches 5.125% or 7% — conversion changes the capital structure materially

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
