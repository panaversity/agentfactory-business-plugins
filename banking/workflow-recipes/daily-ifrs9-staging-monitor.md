# Workflow Recipe: Daily IFRS 9 Staging Monitor

## Task Overview

| Field         | Value                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Task Name** | Daily IFRS 9 Stage Migration and Early Warning Monitor                                   |
| **Frequency** | Daily (every business day by 10:00)                                                      |
| **Purpose**   | Monitor stage migrations, identify SICR triggers, flag material movements for governance |
| **Owner**     | Credit Risk / IFRS 9 Model team                                                          |

---

## Trigger Conditions

| Trigger          | Condition                     | Action                      |
| ---------------- | ----------------------------- | --------------------------- |
| **Scheduled**    | Every business day at 08:00   | Run staging checks          |
| **Event-driven** | Facility reaches 30 DPD       | Immediate SICR assessment   |
| **Event-driven** | Rating downgrade (2+ notches) | Immediate staging review    |
| **Event-driven** | Watchlist addition            | Flag for Stage 2 assessment |
| **Event-driven** | Covenant breach notification  | Immediate staging review    |

---

## Step-by-Step Execution

### Step 1: DPD Extraction

- Extract current DPD for all facilities from core banking system
- Identify facilities crossing 30-day and 90-day thresholds since prior day

### Step 2: Stage Assessment

For each facility crossing a threshold:

1. Apply Stage 3 test (90+ DPD, formal default)
2. Apply Stage 2 test (30-89 DPD, rating downgrade, watchlist, covenant breach)
3. Check for Stage 2 to Stage 1 cures (probation period completed)
4. Check for Stage 3 to Stage 2 cures (all default triggers resolved)

### Step 3: ECL Impact Estimation

For each migration:

- Calculate ECL before and after stage change
- Estimate P&L impact of migration
- Aggregate material impacts for governance reporting

### Step 4: Early Warning Dashboard

Output: Daily Staging Dashboard with:

- New Stage 2 migrations (count, balance, ECL impact)
- New Stage 3 migrations (count, balance, ECL impact)
- Cures (Stage 3 to 2, Stage 2 to 1)
- Top 10 facilities approaching SICR thresholds
- Sector concentration in Stage 2/3

### Step 5: Governance Escalation

- Any single facility migration with ECL impact > GBP 1M: alert IFRS 9 Governance Committee
- Aggregate Stage 2 increase > 5% month-over-month: alert CRO
- Any macro-driven mass migration (sector stress): alert Board Risk Committee

---

## Quality Gates

- DPD data reconciled to core banking system
- All rating changes from credit team reflected in staging
- Stage migrations documented with specific trigger reason
- Probation periods tracked for all cure candidates
