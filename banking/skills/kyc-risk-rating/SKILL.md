---
name: kyc-risk-rating
version: 1.0
description: >
  Activate for: KYC risk rating, customer risk classification, AML risk score,
  customer risk assessment, high-risk customer, risk-based approach, risk rating,
  customer due diligence risk score, PEP risk, geographic risk, product risk,
  customer risk categories.
  NOT for: transaction monitoring alerts (use aml-typologies), SAR/STR drafting
  (use aml-sar-drafting), sanctions screening (use sanctions-screening).
standard: FATF Recommendation 1 (Risk-Based Approach), Recommendation 10 (CDD)
author: Panaversity — The AI Agent Factory
---

## RISK-BASED APPROACH PRINCIPLE

The FATF Risk-Based Approach requires that AML/CFT measures be proportionate
to the risks identified. Higher-risk customers receive Enhanced Due Diligence (EDD);
lower-risk customers may receive Simplified Due Diligence (SDD) in some cases.
Every customer must be assigned a risk rating and the rating must be reviewed periodically.

## RISK SCORING FRAMEWORK — FOUR DIMENSIONS

### Dimension 1: Customer Type Risk

| Customer Category                                             | Risk Score               |
| ------------------------------------------------------------- | ------------------------ |
| Listed company (major exchange)                               | 1 — Low                  |
| Regulated financial institution (home jurisdiction)           | 2 — Low                  |
| Domestic corporate (private, no PEP links)                    | 3 — Medium               |
| High net worth individual                                     | 3 — Medium               |
| Non-profit organisation / charity                             | 4 — Medium-High          |
| Foreign private company                                       | 4 — Medium-High          |
| Offshore structure (Cayman, BVI, Panama)                      | 5 — High                 |
| Trust or foundation (complex beneficiary structure)           | 5 — High                 |
| PEP individual (Tier 1 — foreign)                             | 5 — High (mandatory EDD) |
| Cash-intensive business (jeweller, currency exchange, casino) | 5 — High                 |

### Dimension 2: Geographic Risk

| Geography                                    | Risk Score     |
| -------------------------------------------- | -------------- |
| FATF member, low TI-CPI risk                 | 1 — Low        |
| FATF member, moderate TI-CPI risk            | 2 — Low-Medium |
| FATF under enhanced follow-up (grey list)    | 4 — High       |
| FATF blacklisted jurisdiction                | 5 — Very High  |
| Non-FATF jurisdiction with strong AML regime | 3 — Medium     |
| Non-FATF jurisdiction with weak AML regime   | 4 — High       |

Check current FATF grey/black list at fatf-gafi.org — updated three times per year.
TI Corruption Perceptions Index (CPI): scores below 40/100 indicate high corruption risk.

### Dimension 3: Product / Service Risk

| Product / Service                         | Risk Score      |
| ----------------------------------------- | --------------- |
| Basic current account (domestic customer) | 1 — Low         |
| Fixed-term savings/deposit                | 1 — Low         |
| Retail mortgage                           | 2 — Low-Medium  |
| Business current account                  | 3 — Medium      |
| International wire transfers              | 4 — Medium-High |
| Private banking / wealth management       | 4 — Medium-High |
| Correspondent banking                     | 5 — High        |
| Trade finance                             | 5 — High        |
| Cryptocurrency-related services           | 5 — High        |
| Cash-heavy transactions                   | 5 — High        |

### Dimension 4: Relationship / Behavioural Risk

| Indicator                                                 | Risk Score      |
| --------------------------------------------------------- | --------------- |
| Long-standing customer, consistent behaviour              | 1 — Low         |
| New customer, no prior relationship                       | 3 — Medium      |
| Complex or inconsistent business explanation              | 4 — Medium-High |
| Reluctance to provide CDD documentation                   | 5 — High        |
| Third-party introduction with no independent verification | 4 — Medium-High |
| Adverse media (unverified)                                | 4 — Medium-High |
| Adverse media (verified / criminal conviction)            | 5 — High        |
| Prior SAR on this customer (bank or other FI)             | 5 — High        |

## OVERALL RISK RATING CALCULATION

Composite score = Weighted average of four dimension scores:
Customer type: 35%
Geographic: 30%
Product/service: 20%
Relationship/behavioural: 15%

| Composite Score | Overall Risk Rating | CDD Level                                 | Monitoring Frequency |
| --------------- | ------------------- | ----------------------------------------- | -------------------- |
| 1.0 - 2.0       | Low                 | Standard CDD                              | Every 5 years        |
| 2.1 - 3.0       | Medium              | Standard CDD                              | Every 3 years        |
| 3.1 - 4.0       | High                | Enhanced CDD                              | Annually             |
| 4.1 - 5.0       | Very High           | Enhanced CDD + Senior Management Approval | 6-monthly or more    |

### Scoring Methodology Detail

The weighted average approach is the most common, but banks must consider:

- Whether to use the highest single dimension score as a floor
- Whether to apply non-linear scaling (e.g., any dimension at 5 forces overall High)
- Some regulators require that certain triggers override the composite score entirely

Example calculation:
Customer type: Foreign private company = 4
Geographic: FATF grey list jurisdiction = 4
Product: Correspondent banking = 5
Behavioural: New customer = 3
Composite = (4 x 0.35) + (4 x 0.30) + (5 x 0.20) + (3 x 0.15) = 4.05 = Very High

In this case the composite score of 4.05 falls in the Very High band. Additionally,
the mandatory override for correspondent banking (score 5) would independently
trigger a High rating regardless of the composite calculation.

## MANDATORY OVERRIDES (automatic High/Very High regardless of score)

The following automatically classify a customer as High or Very High risk:

- PEP status (any tier) -> Very High (mandatory EDD, senior management approval)
- FATF black-listed jurisdiction customer -> Very High
- Cash-intensive business above defined threshold -> High
- Customer subject to law enforcement request or known investigation -> Very High
- Beneficial owner structure includes jurisdiction with no beneficial ownership register -> High

## KYC REFRESH TRIGGERS (outside periodic schedule)

Trigger an unscheduled KYC refresh when:

- Adverse media alert on customer or associated party
- Change in ownership or beneficial ownership
- Significant change in transaction behaviour
- Law enforcement contact or request for information
- Customer notifies of major change (new business, new address, change of director)
- Internal SAR filed on this customer
- Customer added to watchlist by transaction monitoring system

## OUTPUT FORMAT — RISK RATING ASSESSMENT

```
KYC RISK RATING ASSESSMENT
Customer ID:        [ID]
Customer Name:      [Name]
Assessment Date:    [YYYY-MM-DD]
Assessor:           [Name / Role]

DIMENSION SCORES:
  Customer Type:     [Score] — [Category]
  Geographic:        [Score] — [Category]
  Product/Service:   [Score] — [Category]
  Behavioural:       [Score] — [Category]

COMPOSITE SCORE:     [X.XX]
OVERALL RATING:      [Low / Medium / High / Very High]

MANDATORY OVERRIDES APPLIED:
  [List any override triggers, or "None"]

CDD LEVEL:           [Standard / Enhanced / Enhanced + Senior Mgmt]
MONITORING FREQUENCY: [5yr / 3yr / Annual / 6-monthly]
NEXT REVIEW DATE:    [YYYY-MM-DD]

RATIONALE:
  [Brief narrative justifying the rating]
```

## NEVER DO THESE

- NEVER assign a risk rating without checking all four dimensions — omitting a dimension (especially geographic or behavioural) systematically underestimates risk and will fail regulatory examination
- NEVER override a mandatory High/Very High classification downward without documented senior management approval and a clear regulatory basis — PEP status and FATF blacklist triggers are not discretionary
- NEVER rely solely on the composite score when a mandatory override trigger is present — the override takes precedence regardless of the weighted average
- NEVER defer a KYC refresh when a trigger event occurs — trigger-based refresh is regulatory expectation, and delay creates a compliance gap that regulators treat as a finding

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
