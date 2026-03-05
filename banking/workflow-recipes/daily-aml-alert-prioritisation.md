# Workflow Recipe: Daily AML Alert Prioritisation

## Task Overview

| Field         | Value                                                                          |
| ------------- | ------------------------------------------------------------------------------ |
| **Task Name** | Daily AML Transaction Monitoring Alert Prioritisation                          |
| **Frequency** | Daily (every business day by 09:00)                                            |
| **Purpose**   | Triage TM alerts, prioritise by risk, assign to analysts, track SLA compliance |
| **Owner**     | Financial Crime / AML Operations                                               |

---

## Trigger Conditions

| Trigger          | Condition                                            | Action                     |
| ---------------- | ---------------------------------------------------- | -------------------------- |
| **Scheduled**    | Every business day at 07:00                          | Ingest overnight TM alerts |
| **Event-driven** | High-priority alert (sanctions hit, PEP, large cash) | Immediate escalation       |
| **Event-driven** | Law enforcement request received                     | Priority case creation     |
| **Manual**       | MLRO requests re-prioritisation                      | Re-run prioritisation      |

---

## Step-by-Step Execution

### Step 1: Ingest Alerts

- Source: Transaction monitoring system overnight batch
- Parse alert data: customer, account, alert type, trigger rule, transaction details

### Step 2: Risk-Based Prioritisation

Apply priority scoring:

- P1 (Critical): Sanctions hit, law enforcement request, PEP with large unusual transaction
- P2 (High): Structuring pattern, rapid fund movement, high-risk jurisdiction
- P3 (Medium): Velocity alert, geographic anomaly, peer group outlier
- P4 (Low): Minor threshold breach, known business pattern variation

### Step 3: Assignment

- P1: Assign to senior analyst immediately, MLRO notification
- P2: Assign to Level 2 analyst, 24-hour SLA
- P3: Assign to Level 1 analyst, 48-hour SLA
- P4: Assign to Level 1 analyst, 5-day SLA

### Step 4: Dashboard Generation

Output: Daily AML Operations Dashboard with:

- New alerts by priority
- Open alerts by age band and priority
- SLA compliance rate (% within SLA)
- SAR pipeline (cases in preparation)
- Analyst workload distribution

### Step 5: SLA Monitoring

- P1 overdue (> 4 hours): Auto-escalate to Head of Financial Crime
- P2 overdue (> 24 hours): Auto-escalate to AML team lead
- P3/P4 overdue (> SLA): Weekly escalation report to compliance

---

## Quality Gates

- All overnight alerts ingested before prioritisation
- No P1 alert left unassigned for > 1 hour
- SAR filing backlog < 5 working days
- Monthly false positive rate tracked and reported
