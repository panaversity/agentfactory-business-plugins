---
name: ifrs9-staging
version: 1.0
description: >
  Activate for: SICR, significant increase in credit risk, staging assessment,
  stage migration, Stage 1 to Stage 2, rebuttable presumption, 30 days past due,
  90 days past due, watchlist, covenant breach, stage cure, qualitative SICR.
standard: IFRS 9.5.5 Impairment
author: Panaversity — The AI Agent Factory
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
  [ ] PD at reporting date ≥ 2× PD at origination (many banks use this)
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
Stage 3 → Stage 2: All default triggers resolved + satisfactory probation period
  (typically 3–6 months) + updated financials reviewed + credit officer sign-off
Stage 2 → Stage 1: All SICR triggers resolved + probation period current
  (typically 3–12 months) + borrower risk profile back to origination level

## QUALITATIVE SICR — PROFESSIONAL JUDGMENT FRAMEWORK
When qualitative factors are present, apply this framework:
  1. What specific information suggests deterioration?
  2. How significant is this relative to risk at origination?
  3. Would a prudent lender consider credit risk materially higher than at origination?
  4. Is there documented evidence that risk has NOT materially increased?
If answer to (3) is YES and (4) cannot be answered convincingly: Stage 2.
DOCUMENT all qualitative staging decisions — auditors will challenge undocumented
assessments where observable risk signals were present.

## STAGE MIGRATION TABLE FORMAT
| Migration | # Facilities | Balance £M | ECL Before | ECL After | P&L Impact |
|---|---|---|---|---|---|
| Stage 1 → 2 | X | X | 12-mo ECL | Lifetime ECL | Increase |
| Stage 1 → 3 | X | X | 12-mo ECL | Lifetime ECL | Increase |
| Stage 2 → 3 | X | X | Lifetime ECL | Higher lifetime ECL | Increase |
| Stage 3 → 2 (cure) | X | X | Lifetime ECL | Lower lifetime ECL | Decrease |
| Stage 2 → 1 (cure) | X | X | Lifetime ECL | 12-mo ECL | Decrease |
Every migration must trace to a specific trigger event in audit documentation.
