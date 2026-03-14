---
name: compliance-calendar
description: >
  Obligation tracking, deadline management, and compliance calendar dashboards.
  Covers contract obligations, regulatory filings, internal compliance reviews,
  and litigation deadline escalation. Produces RAG-status dashboards with
  escalation timelines.
user-invocable: false
---

# Compliance Calendar -- Obligation Tracking

## CALENDAR CATEGORIES

### Category 1: Contract Obligations

- Deliverables due under executed contracts
- Payment obligations and invoice deadlines
- Notice periods for renewal / non-renewal
- Audit rights windows (must be exercised within defined periods)
- SLA review and reporting obligations
- Certification / accreditation obligations required by contract

### Category 2: Regulatory Filings

- Annual returns (Companies House / equivalent)
- Licence renewals (sector-specific)
- Data protection registration renewals (where required)
- Annual accounts filing deadlines
- PAYE / payroll compliance filings (coordinate with Finance)

### Category 3: Internal Compliance Reviews

- Data Protection Impact Assessments (DPIA) -- annual review
- Privacy Policy and Cookie Policy review (annual minimum)
- Employee Handbook / HR Policy review (annual minimum)
- Information Security Policy review (annual minimum)
- Third-party vendor risk reviews (annual for high-risk vendors)
- Anti-bribery and anti-corruption training refresh

### Category 4: Litigation and Dispute Deadlines

IMMEDIATE ESCALATION TO COUNSEL -- do not track without legal oversight:

- Limitation periods
- Court filing deadlines
- Disclosure / discovery deadlines
- Hearing dates
- Settlement offer expiry dates

## ESCALATION TIMELINE

| Time Before Deadline | Action                                                     |
| -------------------- | ---------------------------------------------------------- |
| 60 days              | Add to upcoming obligations dashboard                      |
| 30 days              | Notify obligation owner by email                           |
| 14 days              | Notify obligation owner + direct manager                   |
| 7 days               | Notify General Counsel; add to weekly brief                |
| 1 day                | Emergency alert: CFO (financial) / GC (legal/regulatory)   |
| Day of (missed)      | Log compliance incident; initiate remediation workflow     |
| Day after (missed)   | Incident report to GC; assess regulatory notification req. |

## DASHBOARD OUTPUT FORMAT

# COMPLIANCE CALENDAR -- [Date Range]

RED -- OVERDUE -- immediate action required

---

[Item] | [Contract/Obligation] | [Due date] | [Owner] | [Action]

YELLOW -- DUE IN 14 DAYS

---

[Item] | [Contract/Obligation] | [Due date] | [Owner] | [Action]

GREEN -- DUE IN 15-60 DAYS

---

[Item] | [Contract/Obligation] | [Due date] | [Owner] | [Action]

========================================================
Total open obligations: [N]
Overdue: [N] | Due 14 days: [N] | Due 60 days: [N]

## NEVER DO THESE

- NEVER track litigation deadlines without attorney oversight -- errors
  can result in time-barred claims or procedural sanctions
- NEVER mark an obligation as "complete" without documented evidence
  (confirmation email, delivery receipt, filing acknowledgement)
- NEVER remove an item from the calendar without GC approval if it
  was previously escalated
- NEVER set renewal reminders at the renewal date itself -- always set
  to the last date on which notice can be given to avoid auto-renewal
- NEVER manage limitation periods without qualified legal counsel

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
