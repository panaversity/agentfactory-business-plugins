# Exercise 14: Suspense Account Clearance

## Scenario Profile

| Field               | Value                                   |
| ------------------- | --------------------------------------- |
| **Domain**          | Bank Reconciliation -- Suspense Control |
| **Jurisdiction**    | Global                                  |
| **Time Estimate**   | 30 minutes                              |
| **Skills Required** | `bank-reconciliation`                   |

---

## Data

You are the Operations Manager responsible for suspense account clearance at month-end. The following 12 items are sitting across 3 suspense accounts.

### Payment Suspense (Account: SUSP-PAY-001)

| Item   | Date Posted | Amount GBP | Description                                                  | Age (days) |
| ------ | ----------- | ---------- | ------------------------------------------------------------ | ---------- |
| PS-001 | 28 Feb      | 45,000     | Unidentified wire from Emirates NBD                          | 5          |
| PS-002 | 25 Feb      | 120,000    | Credit from "Oceanic Trades" -- no matching expected receipt | 8          |
| PS-003 | 15 Feb      | 88,500     | Partial payment -- customer ref truncated in SWIFT           | 18         |
| PS-004 | 1 Feb       | 33,000     | Unidentified domestic BACS credit                            | 32         |

### FX Suspense (Account: SUSP-FX-002)

| Item   | Date Posted | Amount GBP | Description                                          | Age (days) |
| ------ | ----------- | ---------- | ---------------------------------------------------- | ---------- |
| FX-001 | 3 Mar       | 2,400      | EUR/GBP rounding difference on FX settlement         | 2          |
| FX-002 | 27 Feb      | 8,750      | USD/GBP rate discrepancy on treasury deal            | 6          |
| FX-003 | 20 Feb      | 45,200     | Unmatched FX forward settlement leg                  | 13         |
| FX-004 | 5 Feb       | 1,200,000  | Failed FX settlement -- counterparty did not deliver | 28         |

### Operations Suspense (Account: SUSP-OPS-003)

| Item   | Date Posted | Amount GBP | Description                                               | Age (days) |
| ------ | ----------- | ---------- | --------------------------------------------------------- | ---------- |
| OP-001 | 4 Mar       | 15,000     | Duplicate wire instruction posted twice                   | 1          |
| OP-002 | 26 Feb      | 67,000     | Trade settlement break -- securities not received         | 7          |
| OP-003 | 10 Feb      | 250,000    | Inter-company transfer misrouted to wrong entity          | 23         |
| OP-004 | 28 Jan      | 180,000    | Correspondent bank charge disputed -- awaiting resolution | 35         |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The 12-item suspense account data across 3 accounts (SUSP-PAY-001, SUSP-FX-002, SUSP-OPS-003) above
- Skills active: `bank-reconciliation`
- Estimated time: 30 minutes

---

## Step-by-Step Instructions

### Step 1: Age Classification and Escalation (10 min)

Apply the ageing SLA to all 12 items:

- 0-2 days: Monitor only
- 3-5 days: Notify account owner, initiate investigation
- 6-15 days: Formal counterparty query, Head of Operations alert
- 16+ days: Finance Controller alert, P&L provision assessment
- 30+ days: Write-off assessment, operational risk event log

Classify each item and identify required escalations.

### Step 2: Clearance Actions (10 min)

For each item, prescribe the specific clearance action:

**Payment Suspense:**

- PS-001 (5 days): Contact Emirates NBD for remitter details
- PS-002 (8 days): Search corporate client expected receipts, send formal query
- PS-003 (18 days): Match to original payment using partial reference, post to correct account
- PS-004 (32 days): Regulatory obligation to return funds to sender if unresolved; assess write-off

**FX Suspense:**

- FX-001 (2 days): Post to FX rounding account (below materiality threshold)
- FX-002 (6 days): Investigate rate discrepancy with treasury desk, post adjustment
- FX-003 (13 days): Contact counterparty for settlement confirmation
- FX-004 (28 days): Escalate failed settlement to Finance Controller; calculate cost of fail

**Operations Suspense:**

- OP-001 (1 day): Reverse duplicate posting, log as operational risk event
- OP-002 (7 days): Check with custodian (CREST/Euroclear) for settlement status
- OP-003 (23 days): Coordinate with inter-company reconciliation team for correction
- OP-004 (35 days): Write-off assessment required; log as operational risk loss event

### Step 3: Month-End Report (5 min)

Compile the month-end suspense account report:

- Total items by account
- Total value by account
- Items by age band (0-5, 6-15, 16-30, 30+)
- Items requiring write-off assessment
- Items requiring regulatory notification

### Step 4: Control Findings (5 min)

Identify control weaknesses:

1. Which suspense accounts have items > 30 days? (control finding)
2. Are all suspense accounts owned? (check named owner requirement)
3. What is the month-end zero balance achievement? (audit metric)
4. Recommend process improvements to prevent recurrence

---

## Deliverable

Produce: Month-end suspense certification for CFO with age classification matrix, clearance action plan per item, month-end report (totals by account, value by age band), control findings with recommended process improvements, and zero-balance achievement assessment.

---

## Key Learning

- Suspense accounts are a critical control point -- aged items indicate operational control failures
- Every suspense item must have a named owner and documented investigation status
- Items > 30 days require CFO-level write-off assessment and operational risk logging
- The month-end zero balance target is an audit metric -- material balances are an audit finding
- Duplicate postings must be reversed AND logged as operational risk events
- Failed FX settlements can be material and require immediate escalation
