# Workflow Recipe: Daily GL-to-Risk System Reconciliation

## Task Overview

| Field         | Value                                                                             |
| ------------- | --------------------------------------------------------------------------------- |
| **Task Name** | Daily GL-to-Risk System Balance Reconciliation                                    |
| **Frequency** | Daily (every business day by 11:00)                                               |
| **Purpose**   | Ensure GL balances reconcile to risk system, identify breaks before they compound |
| **Owner**     | Finance / Risk Operations                                                         |

---

## Trigger Conditions

| Trigger          | Condition                                      | Action                                 |
| ---------------- | ---------------------------------------------- | -------------------------------------- |
| **Scheduled**    | Every business day at 09:00                    | Run daily reconciliation               |
| **Event-driven** | Manual GL journal posted to provision accounts | Immediate recon check                  |
| **Event-driven** | Write-off processed                            | Verify GL and risk system both updated |
| **Event-driven** | New product or portfolio onboarded             | Verify risk system capture             |

---

## Step-by-Step Execution

### Step 1: Extract Balances

- GL: Extract provision account balances by stage and portfolio segment
- Risk system: Extract facility-level ECL aggregated to same segments
- Compare at portfolio segment level and at total level

### Step 2: Identify Breaks

- Threshold: any difference > GBP 10K (or bank-defined materiality)
- Classify breaks:
  - Timing: GL journal pending for known risk system change
  - Data: facility missing from risk system but present in GL (or vice versa)
  - Manual: GL contains manual journal not reflected in risk system
  - FX: translation difference between systems

### Step 3: Resolution

- Timing breaks: monitor for auto-resolution within 2 business days
- Data breaks: investigate root cause; reconcile facility count
- Manual breaks: require documented justification and approval
- FX breaks: apply consistent FX rate source; post adjustment if needed

### Step 4: Daily Report

Output: Daily GL-Risk Recon Report with:

- Breaks by category and amount
- Aged breaks (carried forward from prior days)
- Breaks resolved today
- Cumulative break trend (should be declining toward quarter-end)

### Step 5: Quarter-End Preparation

- Target: zero breaks at quarter-end (required for four-way recon sign-off)
- Any break > 5 days: escalate to Finance Controller
- Any break > 10 days: escalate to CFO

---

## Quality Gates

- Both GL and risk system extracts from same cut-off time
- Facility count reconciled (not just amounts)
- All manual GL journals documented with approval
- Zero tolerance for unexplained breaks at quarter-end
