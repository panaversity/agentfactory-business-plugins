# Workflow Recipe: Contract Intake -- End-to-End

## Task Overview

| Field         | Value                                                                              |
| ------------- | ---------------------------------------------------------------------------------- |
| **Task Name** | Contract Intake: Receipt through Execution and Obligation Monitoring               |
| **Frequency** | Continuous (triggered by each incoming contract)                                   |
| **Purpose**   | Route incoming contracts through triage, review, approval, execution, and tracking |
| **Owner**     | Legal Operations Manager / Legal Intake Coordinator                                |

---

## Trigger Conditions

| Trigger      | Condition                                               | Action                                          |
| ------------ | ------------------------------------------------------- | ----------------------------------------------- |
| **Email**    | Contract received at legal-intake@yourcompany.com       | Start intake sequence                           |
| **Upload**   | Document uploaded to designated SharePoint/Drive folder | Start intake sequence                           |
| **Web form** | Contract submitted via internal portal                  | Start intake sequence                           |
| **URGENT**   | Business deadline stated < 48 hours                     | Flag URGENT; notify GC; halve all SLA timelines |

---

## Step-by-Step Execution

### Step 1: Receive and Log

```
Input: Contract document (PDF, DOCX, or via MCP connector)
Actions:
  - Assign reference ID: [YYYY-MM-DD-XXXX]
  - Record receipt timestamp
  - Log in contract tracking system
  - Extract: counterparty name, contract type, requesting business unit,
    stated urgency, deal value (if stated), governing law (if stated)
```

### Step 2: Classify Document Type

```
NDA / Mutual CA / CDA         -> Run /triage-nda protocol
Vendor Agreement / MSA / SOW  -> Run /review-contract protocol
SaaS / Software Licence        -> Run /review-contract protocol
Employment / Contractor        -> Route to HR Legal queue (no agent triage)
Partnership / JV               -> Run /review-contract + notify GC
M&A / Investment               -> Route to GC immediately (no agent triage)
Unknown                        -> Extract key terms; route to GC queue
```

### Step 3: Run Triage Protocol

```
Execute the appropriate product skill:
  - nda-triage: produces Tier 1/2/3 classification
  - contract-review: produces GREEN/YELLOW/RED analysis

Output: Triage tier + deviation summary + routing recommendation
```

### Step 4: Route Based on Tier

```
Tier 1 (Standard Approval):
  -> Send Template A to business unit
  -> Route to authorised signatory queue
  -> Set follow-up reminder: 3 business days

Tier 2 (Counsel Review):
  -> Send Template B to reviewing attorney
  -> Attach triage summary
  -> Set SLA reminder: 2 business days

Tier 3 (Full Review / RED items):
  -> Send Template C to General Counsel
  -> Attach full review output
  -> Schedule review call if value > threshold
  -> Set SLA reminder: 5 business days
```

### Step 5: Track Progress

```
Daily status check. Escalate if SLA breached:
  - Tier 1 > 1 business day: notify business unit + attorney
  - Tier 2 > 2 business days: notify GC
  - Tier 3 > 5 business days: notify GC + CFO (if above threshold)
```

### Step 6: Post-Execution

```
On confirmed signing:
  - Save executed contract to repository
  - Update tracking log: status = EXECUTED
  - Extract: execution date, effective date, term, renewal date, notice period
  - Set calendar reminders:
    -> Notice period deadline (last date for non-renewal notice)
    -> Contract expiry date
    -> Key obligation due dates
  - Notify business unit: confirmation + renewal date
```

---

## Required Skill Files

| Skill File              | Purpose                                 |
| ----------------------- | --------------------------------------- |
| `contract-intake-agent` | Intake sequence, routing, and templates |
| `contract-review`       | Full contract review (Tier 2/3)         |
| `nda-triage`            | NDA triage (Tier 1/2/3)                 |
| `compliance-calendar`   | Post-execution obligation tracking      |
| `legal-global-router`   | Routing and jurisdiction identification |

---

## Escalation / Review Checkpoints

| Checkpoint          | Condition                                        | Reviewer           |
| ------------------- | ------------------------------------------------ | ------------------ |
| **Triage complete** | All metadata extracted, tier assigned            | Legal Ops Manager  |
| **SLA breach**      | Tier 1 > 1 day, Tier 2 > 2 days, Tier 3 > 5 days | GC                 |
| **RED escalation**  | Any RED deviation identified                     | GC immediately     |
| **Execution**       | Signed contract confirmed                        | Legal Ops Manager  |
| **Post-execution**  | Calendar reminders and obligations logged        | Compliance Officer |

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
