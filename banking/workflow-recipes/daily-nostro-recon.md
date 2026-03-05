# Workflow Recipe: Daily Nostro Reconciliation

## Task Overview

| Field         | Value                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Task Name** | Daily Nostro Account Reconciliation                                                                                    |
| **Frequency** | Daily (every business day by 10:00 local time)                                                                         |
| **Purpose**   | Match internal mirror entries against correspondent bank statements, identify and classify breaks, escalate aged items |
| **Owner**     | Operations / Payments team                                                                                             |

---

## Trigger Conditions

| Trigger          | Condition                            | Action                                      |
| ---------------- | ------------------------------------ | ------------------------------------------- |
| **Scheduled**    | Every business day at 08:00          | Ingest MT940/MT950 statements, run matching |
| **Event-driven** | SWIFT gpi status update received     | Update break status for pending items       |
| **Event-driven** | Large payment instruction (> USD 1M) | Priority matching within 2 hours            |
| **Manual**       | Counterparty query response received | Re-run matching for affected items          |

---

## Step-by-Step Execution

### Step 1: Ingest External Statements

- Source: MT940 (end-of-day) or MT942 (intraday) from each correspondent bank
- Parse statement entries into standardised format (date, amount, reference, counterparty)

### Step 2: Run Matching Hierarchy

Apply the 5-step matching hierarchy from `bank-reconciliation`:

1. Exact match (amount + date + reference)
2. Fuzzy match (amount + date, reference partially matches)
3. Date tolerance match (amount + reference, date within +/- 2 business days)
4. Partial sum pool (multiple items aggregate to single entry)
5. Unmatched residual

### Step 3: Classify Breaks

For each unmatched item, auto-classify:

- Mirror-only: timing difference or payment failure
- Statement-only: unbooked receipt or unexpected debit
- Amount mismatch: correspondent fee or FX rounding

### Step 4: Generate Daily Break Report

Output: Daily Nostro Break Report with columns:

- Nostro account, currency, correspondent
- Break type, amount, age in business days
- Investigation hypothesis, assigned owner
- Escalation status per ageing SLA

### Step 5: Escalation Enforcement

- Items 3-5 days: auto-notify account owner
- Items 6-15 days: auto-alert Head of Operations
- Items > 15 days: auto-alert Finance Controller
- Items > 30 days: flag for write-off assessment

---

## Quality Gates

- All MT940 statements ingested before matching starts
- Match rate target: > 95% auto-match
- Zero unidentified credits left in mirror at end of day (moved to suspense)
- All large breaks (> USD 500K) notified to Treasurer regardless of age
