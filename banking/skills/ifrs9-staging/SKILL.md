---
name: ifrs9-staging
description: >
  Activate for: SICR, significant increase in credit risk, staging assessment,
  stage migration, Stage 1 to Stage 2, rebuttable presumption, 30 days past due,
  90 days past due, watchlist, covenant breach, stage cure, qualitative SICR.
  NOT for: initial recognition and measurement of financial instruments, hedge
  accounting, IFRS 9 classification questions, US GAAP CECL staging.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 9.5.5 Impairment"
---

## STAGING DECISION TREE — APPLY IN THIS EXACT ORDER

### STEP 1 — Test for Stage 3 (Credit Impairment)
Any one of the following triggers Stage 3:
  [ ] 90+ days past due
  [ ] Formal default event (insolvency filing, legal default notice)
  [ ] Significant financial difficulty, no credible recovery path
  [ ] Forbearance / restructuring at terms bank would not otherwise offer
  [ ] Partial or full write-off recognised
  → If ANY trigger: STAGE 3 — Lifetime ECL — Interest on NET amount

### STEP 2 — Test for Stage 2 (SICR)
Any one of the following triggers Stage 2:
  Quantitative:
  [ ] 30–89 days past due (rebuttable presumption — see below)
  [ ] Internal rating downgraded 2+ notches since origination
  [ ] PD at reporting date ≥ 2x PD at origination (many banks use this)
  [ ] Lifetime PD exceeds bank-defined absolute SICR threshold
  Qualitative:
  [ ] On watchlist / credit monitoring list
  [ ] Financial covenant breach (leverage, DSCR, LTV, interest cover)
  [ ] Loss of major customer / key contract
  [ ] Adverse regulatory action on borrower
  [ ] Industry under systemic stress (macro-driven transfer)
  [ ] Parent / key affiliate significant SICR
  → If ANY trigger: STAGE 2 — Lifetime ECL — Interest on GROSS amount

### STEP 3 — Default: Stage 1
No triggers from Step 1 or Step 2 → STAGE 1 — 12-month ECL

## THE 30-DAY REBUTTABLE PRESUMPTION
IFRS 9.5.5.11: 30+ DPD creates a rebuttable presumption of SICR.
Can be rebutted ONLY with documented evidence of:
  - Administrative processing delay (not customer fault)
  - Payment in bona fide dispute with clear resolution pathway
  - Payment received shortly after reporting date (documented)
CANNOT be rebutted on grounds of: past payment history, prior accommodations.
DOCUMENT every rebuttal. Auditors review all instances where 30+ DPD was not staged.

## STAGE CURE CONDITIONS

### Stage 3 to Stage 2 Cure Requirements
All of the following must be satisfied before cure to Stage 2:
  a) All default triggers resolved (no longer 90+ DPD, no active forbearance)
  b) Satisfactory probation period completed (typically 3–6 months depending on
     portfolio — retail tends to 3 months, corporate 6 months)
  c) Updated financial information reviewed and credit assessment performed
  d) Credit officer sign-off on cure determination (documented)
  e) No new adverse information during probation period (no new covenant breaches,
     no adverse media, no further deterioration in financial metrics)
  f) If forbearance was the trigger: the borrower must have made at least 3
     consecutive scheduled payments under the revised terms

### Stage 2 to Stage 1 Cure Requirements
All of the following must be satisfied before cure to Stage 1:
  a) All SICR triggers resolved (rating restored, no longer past due, covenant
     compliance restored)
  b) Probation period current (typically 3–12 months; banks with large corporate
     portfolios often require 6–12 months to confirm sustained improvement)
  c) Borrower risk profile demonstrably back to the level at origination
  d) No residual concerns that would indicate risk remains elevated
  e) Quantitative PD at reporting date no longer meets the SICR threshold
     relative to origination PD

### Cure Probation — Common Pitfalls
- Setting probation too short (< 3 months) will draw auditor challenge
- Not documenting the cure rationale is equivalent to having no cure process
- Curing a borrower from Stage 3 directly to Stage 1 without a Stage 2
  probation period is NOT permitted under IFRS 9 (must pass through Stage 2)

## QUALITATIVE SICR — PROFESSIONAL JUDGMENT FRAMEWORK
When qualitative factors are present, apply this framework:
  1. What specific information suggests deterioration?
  2. How significant is this relative to risk at origination?
  3. Would a prudent lender consider credit risk materially higher than at origination?
  4. Is there documented evidence that risk has NOT materially increased?
If answer to (3) is YES and (4) cannot be answered convincingly: Stage 2.
DOCUMENT all qualitative staging decisions — auditors will challenge undocumented
assessments where observable risk signals were present.

### Qualitative SICR Examples by Portfolio

| Portfolio | Qualitative SICR Trigger | Evidence Required |
|---|---|---|
| Corporate | Loss of largest customer (>30% revenue) | Customer filing, revenue data |
| Corporate | Covenant breach — DSCR below 1.2x | Financial statements |
| Corporate | Sector downgrade by regulator or rating agency | Published report |
| Mortgage | Borrower made redundant (known to bank) | Employment status change |
| Mortgage | Property value decline >20% (negative equity) | Valuation data |
| SME | Owner/director personal insolvency | Public register search |
| SME | Key supplier ceased trading | Credit bureau data |
| Consumer | Material increase in credit bureau arrears on other products | Bureau data |

## STAGE MIGRATION TABLE FORMAT
| Migration | # Facilities | Balance (M) | ECL Before | ECL After | P&L Impact |
|---|---|---|---|---|---|
| Stage 1 to 2 | X | X | 12-mo ECL | Lifetime ECL | Increase |
| Stage 1 to 3 | X | X | 12-mo ECL | Lifetime ECL | Increase |
| Stage 2 to 3 | X | X | Lifetime ECL | Higher lifetime ECL | Increase |
| Stage 3 to 2 (cure) | X | X | Lifetime ECL | Lower lifetime ECL | Decrease |
| Stage 2 to 1 (cure) | X | X | Lifetime ECL | 12-mo ECL | Decrease |
Every migration must trace to a specific trigger event in audit documentation.

## OUTPUT FORMAT — STAGING ASSESSMENT

```
STAGING ASSESSMENT
Facility ID:       [ID]
Borrower:          [Name]
Portfolio:         [Retail Mortgage / Corporate / SME / Consumer]
Assessment Date:   [YYYY-MM-DD]

CURRENT STAGE:     [1 / 2 / 3]
PROPOSED STAGE:    [1 / 2 / 3]

TRIGGERS IDENTIFIED:
  Quantitative:    [List each trigger with data point]
  Qualitative:     [List each trigger with evidence]

CURE ASSESSMENT (if applicable):
  Probation start: [YYYY-MM-DD]
  Probation end:   [YYYY-MM-DD]
  Conditions met:  [Yes/No with details]

ECL IMPACT:
  ECL before:      [Amount]
  ECL after:       [Amount]
  P&L impact:      [Amount increase/decrease]

RECOMMENDATION:    [Stage X — with rationale]
APPROVED BY:       [Credit officer name and date]
```

## NEVER DO THESE
- NEVER cure a borrower directly from Stage 3 to Stage 1 — IFRS 9 requires passage through Stage 2 with a documented probation period
- NEVER rebut the 30-day past due presumption without written, auditable evidence — past payment history alone is not sufficient grounds for rebuttal
- NEVER apply staging criteria without comparing to the credit risk at origination — SICR is measured relative to initial recognition, not relative to the prior reporting date
- NEVER omit qualitative SICR assessment when observable signals exist — quantitative triggers alone are insufficient if the bank has knowledge of qualitative deterioration
- NEVER set a cure probation period of less than 3 months for any portfolio — shorter periods will not withstand auditor or regulatory challenge

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
