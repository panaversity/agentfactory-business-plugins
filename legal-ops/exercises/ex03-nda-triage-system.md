# Exercise 3: NDA Triage System -- Build, Test, Deploy

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Type**            | Workflow Configuration                        |
| **Time**            | 45 minutes                                    |
| **Skills Required** | `nda-triage`, `legal-global-router`           |
| **Plugin Command**  | `/triage-nda`                                 |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance |

---

## Overview

Your organisation receives approximately 25 NDA requests per month. Currently all
go to the same junior attorney, taking 30-45 minutes each -- approximately 12+ hours
of attorney time per month. Your task: design and test a triage system that reduces
attorney NDA time to 3-4 hours per month.

---

## Steps

### Step 1 -- Configure Your NDA Triage Playbook

Add the NDA-specific section to `legal.local.md`. Define your Tier 1/2/3 criteria.

### Step 2 -- Build a Four-NDA Test Set

- **NDA A**: Your own standard form, unmodified
- **NDA B**: Your standard form with the counterparty's jurisdiction as governing law
- **NDA C**: Your standard form + residuals clause + 5-year term (vs. standard 3)
- **NDA D**: Unilateral NDA (disclosing only, counterparty is discloser) when mutual
  expected; broad confidential information definition; no public-info carve-out;
  perpetual survival

For each: run `/triage-nda`, provide context, record the classification.

### Step 3 -- Expected Results

| NDA   | Expected Tier | Reason                                                  |
| ----- | ------------- | ------------------------------------------------------- |
| NDA A | Tier 1        | Standard form, no deviations                            |
| NDA B | Tier 2        | Governing law deviation -- counsel confirmation         |
| NDA C | Tier 2 or 3   | Residuals clause = automatic RED flag                   |
| NDA D | Tier 3        | Multiple RED items: unilateral, no carve-out, perpetual |

### Step 4 -- Calibrate

If results diverge from expected, update the playbook and re-run. Document why
the initial configuration missed the expected result.

### Step 5 -- Draft Routing Templates

- Tier 1 to business unit: approved, here is the execution process
- Tier 2 to reviewing attorney: here are the flagged deviations and deadline
- Tier 3 to General Counsel: here are the RED items, urgency, recommendation

---

## Expected Output

- Tested NDA triage configuration
- Three routing email templates
- Calculation showing reduction from 12+ to ~3-4 attorney hours/month

---

## Deliverable

Validated NDA triage configuration + routing templates + documented time savings.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
