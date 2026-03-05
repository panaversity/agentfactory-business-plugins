# Workflow Recipe: Quarterly ECL Full Run

## Task Overview

| Field         | Value                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------- |
| **Task Name** | Quarterly IFRS 9 ECL Full Model Run and Governance Cycle                                          |
| **Frequency** | Quarterly (last month of each quarter, T-15 days before reporting date)                           |
| **Purpose**   | Run full ECL model, apply scenarios, calculate PMAs, four-way reconciliation, governance approval |
| **Owner**     | IFRS 9 Model Team / Finance / Credit Risk                                                         |

---

## Trigger Conditions

| Trigger          | Condition                                   | Action                                 |
| ---------------- | ------------------------------------------- | -------------------------------------- |
| **Scheduled**    | T-15 business days before quarter-end       | Initiate full ECL run cycle            |
| **Event-driven** | Material credit event mid-quarter           | Ad-hoc ECL reassessment                |
| **Event-driven** | Macro scenario update from Economics team   | Scenario refresh before full run       |
| **Manual**       | IFRS 9 Governance Committee requests re-run | Full recalculation with updated inputs |

---

## Step-by-Step Execution

### Step 1: Data Extract and Validation (T-15)

- Extract full portfolio from core banking system (all facilities, balances, DPD, ratings)
- Validate data completeness: no missing ratings, no missing DPD, no duplicate facilities
- Reconcile facility count and total balance to prior quarter

### Step 2: Staging Assessment (T-14 to T-12)

- Run full staging assessment for all facilities
- Apply quantitative SICR criteria (DPD, rating downgrades, PD thresholds)
- Apply qualitative SICR criteria (watchlist, covenant breach, sector stress)
- Generate stage migration table vs. prior quarter

### Step 3: Macroeconomic Scenarios (T-12 to T-10)

- Receive scenarios from Economics team (base, upside, adverse, severe)
- Validate scenario weights sum to 1.0
- Calculate CCA for each scenario
- Convert TTC PD to PIT PD for each borrower under each scenario

### Step 4: ECL Calculation (T-10 to T-8)

- Stage 1: ECL_12 = PD_PIT x LGD x EAD for each scenario
- Stage 2/3: Lifetime ECL = sum of marginal PD x LGD x EAD x DF for each scenario
- Probability-weight across scenarios
- Aggregate by portfolio segment

### Step 5: Post-Model Adjustments (T-8 to T-6)

- Review existing PMAs: retain, adjust, or release
- Assess need for new PMAs (sector stress, model limitations, emerging risks)
- Document each PMA: rationale, amount, time limit, review date
- PMAs must be approved by IFRS 9 Governance Committee

### Step 6: Four-Way Reconciliation (T-6 to T-4)

- Tier 1: ECL model output
- Tier 2: Risk system facility sum
- Tier 3: GL provision account balance
- Tier 4: Disclosure draft
- Investigate and resolve all breaks before sign-off

### Step 7: Governance Approval (T-4 to T-2)

- Present to IFRS 9 Governance Committee:
  - ECL by stage, portfolio, and scenario
  - Stage migration analysis
  - PMA rationale and amounts
  - Four-way reconciliation certificate
  - IFRS 7 disclosure draft
- Obtain formal approval (documented minutes)

### Step 8: GL Posting and Disclosure (T-2 to T)

- Post approved ECL journals to GL
- Finalise IFRS 7 disclosure notes
- Confirm four-way reconciliation still holds post-journal-posting
- Sign reconciliation certificate

---

## Quality Gates

- Data extract completeness > 99.9% (no missing critical fields)
- Four-way reconciliation zero unexplained breaks
- All PMAs documented and committee-approved
- IFRS 7 disclosures reconciled to GL and model output
- Governance Committee minutes signed before GL posting
