---
name: stress-testing
description: >
  Activate for: ICAAP, ILAAP, stress test, capital depletion, reverse stress test,
  ACS (Annual Cyclical Scenario), DFAST, CCAR, BoE stress test, EBA stress test,
  stressed capital ratio, Pillar 2, capital planning, going concern, stressed ECL,
  stressed RWA, stressed NII.
  NOT for: IFRS 9 macroeconomic scenario weighting (use ifrs9-scenarios),
  market risk capital under FRTB (use basel-rwa-market), liquidity stress
  testing for LCR/NSFR purposes (use liquidity-lcr / liquidity-nsfr).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "BCBS Pillar 2 / SREP framework — jurisdiction implementations vary"
---

## ICAAP PURPOSE AND STRUCTURE

The ICAAP (Internal Capital Adequacy Assessment Process) is the bank's own
assessment of how much capital it needs given its specific risk profile, strategic plan,
and stress scenarios. The regulator uses the ICAAP output to set Pillar 2 requirements.

Required sections:

1. Business model and strategic overview
2. Risk identification — material risks and their capital impact
3. Capital quantification — Pillar 1 and Pillar 2 needs by risk type
4. Stress testing — capital depletion under severe macroeconomic scenarios
5. Capital planning — sources of capital and management actions under stress
6. Capital adequacy conclusion — does the bank hold sufficient capital?

## STRESS TEST FRAMEWORK

### Scenario Design

Base case: 3-year capital projection under central business plan assumptions.
Adverse scenario: Moderate downturn (unemployment +2pp, GDP -1%, HPI -10%).
Severe scenario: Deep recession (unemployment +4pp, GDP -4%, HPI -30%).
Bank-specific idiosyncratic scenario: scenario tailored to bank's specific vulnerabilities
(e.g., CRE concentration stress, single large counterparty default).
Reverse stress test: Work backwards — what scenario causes the bank to fail?
(Required in UK by PRA; useful management discipline globally)

### Capital Depletion Path — Year-by-Year Model

For each scenario year (typically 3 years):
Opening CET1 capital (M)

- Pre-tax profit (NII + fee income - operating costs)

* Tax charge (at applicable corporate tax rate)
* Stressed credit losses (IFRS 9 ECL under scenario conditions)
* Dividend / AT1 coupon payments (suspended in Year 1-2 of severe stress)
  +/- Other comprehensive income (AFS securities fair value movements)
  = Closing CET1 capital (M)
  / Stressed RWA (M) — see RWA inflation below
  = Stressed CET1 Ratio (%)

### RWA Inflation Under Stress

Credit RWA: Increases as Stage 3 NPLs grow (150% risk weight) and
downgrades shift exposures to higher risk weight buckets.
Typical severe scenario: credit RWA +10-15%
Market RWA: Increases as ES/VaR models expand with higher volatility.
Typical severe scenario: market RWA +30-50%
Operational RWA: Increases as conduct/AML losses feed into Business Indicator.
Typical severe scenario: operational RWA +5-10%

### Stressed NII

Asset-sensitive banks (more assets than liabilities repricing in 12 months):
Benefit from initial rate rise; hurt by subsequent rate fall
Liability-sensitive banks (more liabilities than assets repricing):
Hurt by initial rate rise; benefit from subsequent rate fall
IRRBB (Interest Rate Risk in the Banking Book) stress: typically +/- 200bp parallel
shift, +300bp steepening, -200bp flattening. Load jurisdiction overlay for
specific IRRBB scenarios required by the relevant regulator.

## CAPITAL DEPLETION PATH — TEMPLATE

| Line Item                     | Base Y1 | Base Y2 | Base Y3 | Severe Y1 | Severe Y2 | Severe Y3 |
| ----------------------------- | ------- | ------- | ------- | --------- | --------- | --------- |
| Opening CET1 capital (M)      |         |         |         |           |           |           |
| + Net interest income         |         |         |         |           |           |           |
| + Non-interest income         |         |         |         |           |           |           |
| - Operating expenses          |         |         |         |           |           |           |
| = Pre-provision profit        |         |         |         |           |           |           |
| - Credit losses (ECL charge)  |         |         |         |           |           |           |
| - Tax                         |         |         |         |           |           |           |
| - Dividends and AT1 coupons   |         |         |         |           |           |           |
| +/- OCI movements             |         |         |         |           |           |           |
| = Closing CET1 capital (M)    |         |         |         |           |           |           |
| RWA (M)                       |         |         |         |           |           |           |
| **CET1 Ratio (%)**            |         |         |         |           |           |           |
| Distance to 4.5% minimum (pp) |         |         |         |           |           |           |
| Distance to MDA trigger (pp)  |         |         |         |           |           |           |

## DISTANCE TO REGULATORY TRIGGER

At each stress year-end, calculate:
Distance to hard CET1 minimum (4.5%): Stressed CET1 - 4.5%
Distance to combined buffer requirement: Stressed CET1 - [4.5% + CCB + CCyB + surcharge]
Distance to MDA trigger: Same as combined buffer requirement
Going concern test: Is CET1 above 4.5% at all times? If not: plan capital actions.

## MANAGEMENT ACTIONS IN STRESS

Permitted in base case, restricted in severe scenario (per regulator instructions):

- Dividend suspension (Year 1-2): Preserves ~1% CET1 annually for typical bank
- Asset disposals: Non-core asset sales raise CET1 but may crystallise losses
- RWA reduction: Pull back on new lending, reducing RWA growth
- Capital issuance: Rights issue, AT1 issuance — available in moderate but not severe stress
- AT1 conversion: CoCos convert to equity at trigger (typically 5.125% or 7% CET1)

### Management Action Credibility Assessment

Regulators assess management actions for credibility under stress:
| Action | Credible in Adverse? | Credible in Severe? | Notes |
|---|---|---|---|
| Dividend cut/suspension | Yes | Yes (mandatory if MDA breached) | Expected action |
| AT1 coupon suspension | Yes | Yes (mandatory if MDA breached) | Legal discretion |
| Asset disposal | Yes | Unlikely (fire sale prices) | Haircut assumed proceeds |
| Rights issue | Possible | No (market access lost) | Investors unavailable |
| RWA reduction | Yes | Limited (pipeline committed) | 6-12 month lag |

## ICAAP SUBMISSION STANDARDS

The ICAAP is submitted to the regulator (PRA, ECB, APRA, etc.) annually.
It must be: approved by the Board; prepared with independent review (CRO, Finance, Audit);
consistent with financial plan and IFRS 9 ECL assumptions; stress scenarios materially
more severe than the base case.

## REVERSE STRESS TEST

Required by PRA (UK) and increasingly by other regulators.
Process: Start from a point of failure (e.g., CET1 breaches 4.5%).
Work backwards to identify which scenario(s) could cause this outcome.
Assess plausibility of those scenarios.
Identify mitigants and recovery actions.
Purpose: Not prediction — identification of the bank's most acute vulnerabilities
and the triggers that management should monitor most closely.

## REGULATORY STRESS TEST PROGRAMMES

| Programme                             | Jurisdiction | Frequency | Key Feature                                       |
| ------------------------------------- | ------------ | --------- | ------------------------------------------------- |
| ACS (Annual Cyclical Scenario)        | UK (BoE/PRA) | Annual    | Hurdle rates published; public disclosure         |
| EBA Stress Test                       | EU (EBA/ECB) | Biennial  | Static balance sheet; no capital threshold        |
| DFAST (Dodd-Frank Act Stress Test)    | US (Fed)     | Annual    | Severely adverse scenario; public disclosure      |
| CCAR (Comprehensive Capital Analysis) | US (Fed)     | Annual    | Qualitative + quantitative; capital plan approval |

## OUTPUT FORMAT — STRESS TEST SUMMARY

```
STRESS TEST SUMMARY
Entity:             [Bank / Group name]
Assessment Date:    [YYYY-MM-DD]
Scenarios:          [Base / Adverse / Severe / Reverse]

CAPITAL DEPLETION — SEVERE SCENARIO:
  Opening CET1 Ratio:          [X.X%]
  Year 1 CET1 Ratio:           [X.X%]  (distance to 4.5%: [+/-X.X pp])
  Year 2 CET1 Ratio:           [X.X%]  (distance to 4.5%: [+/-X.X pp])
  Year 3 CET1 Ratio:           [X.X%]  (distance to 4.5%: [+/-X.X pp])
  Trough CET1 Ratio:           [X.X%] in Year [N]
  MDA breach:                   [Yes/No — in Year N]

KEY DRIVERS:
  Cumulative credit losses:     [Amount M]
  RWA inflation:                [Amount M] ([+X%])
  NII impact:                   [Amount M]

MANAGEMENT ACTIONS ASSUMED:
  [List with credibility assessment]

REVERSE STRESS TEST:
  Failure scenario:             [Description]
  Plausibility assessment:      [Low / Medium / High]

CONCLUSION:
  Capital adequacy:             [Adequate / Requires action]
  Recommended buffer:           [X.X% above minimum]
```

## NEVER DO THESE

- NEVER assume management actions are fully available in a severe stress scenario — regulators require credibility assessment and will reject actions that are unrealistic under severe market conditions (e.g., equity issuance during a banking crisis)
- NEVER ignore RWA inflation under stress — credit RWA typically increases 10–15% in severe scenarios due to rating downgrades and increased Stage 3 exposures at 150% risk weight
- NEVER use IFRS 9 base-case ECL assumptions in a stress scenario — stressed ECL must reflect the stressed macroeconomic variables, not the probability-weighted base case
- NEVER present a reverse stress test without a plausibility assessment — the purpose is to identify realistic vulnerabilities, not theoretical impossibilities
- NEVER omit AT1 conversion mechanics from severe stress projections — if CET1 approaches the CoCo trigger (typically 5.125% or 7%), AT1 instruments convert to equity and materially change the capital position

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
