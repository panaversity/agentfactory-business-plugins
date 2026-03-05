# Workflow Recipe: Daily Sanctions Batch Screening

## Task Overview

| Field         | Value                                                                           |
| ------------- | ------------------------------------------------------------------------------- |
| **Task Name** | Daily Sanctions List Update and Batch Screening                                 |
| **Frequency** | Daily (every business day by 08:00)                                             |
| **Purpose**   | Update sanctions lists, screen customer base and pending payments, resolve hits |
| **Owner**     | Sanctions Compliance                                                            |

---

## Trigger Conditions

| Trigger          | Condition                       | Action                                        |
| ---------------- | ------------------------------- | --------------------------------------------- |
| **Scheduled**    | Every business day at 06:00     | Download updated lists, run batch screen      |
| **Event-driven** | OFAC/OFSI list update published | Immediate re-screen within 4 hours            |
| **Event-driven** | New customer onboarded          | Real-time screening before account activation |
| **Event-driven** | Large payment (> USD 100K)      | Real-time screening before release            |

---

## Step-by-Step Execution

### Step 1: List Updates

- Download latest OFAC SDN list, OFSI Consolidated List, EU Sanctions Map, UN Consolidated List
- Compare to prior day: identify new additions, removals, amendments
- Alert sanctions team to new designations affecting bank's customer base or geographic footprint

### Step 2: Batch Customer Screening

- Screen entire customer base (names, beneficial owners, directors) against updated lists
- Apply fuzzy matching (transliterations, name variations, partial matches)
- Apply 50% ownership rule for corporate customers

### Step 3: Payment Screening

- Screen all pending outbound payments (SWIFT MT103, MT202) against all lists
- Screen all pending inbound payments
- Block any payment with unresolved hit

### Step 4: Hit Resolution

- Auto-classify obvious false positives (matching DOB, nationality confirms different person)
- Route probable true hits to sanctions analyst for manual review
- Escalate confirmed true hits to Sanctions Officer immediately

### Step 5: Reporting

Output: Daily Sanctions Screening Report with:

- List update summary (new designations)
- Screening volume (customers, payments)
- Hits by category (true, false positive, pending)
- Blocked payments pending resolution
- Regulatory reports filed

---

## Quality Gates

- All sanctions lists updated before batch screening starts
- Zero payments released with unresolved sanctions hits
- All hits resolved or escalated within 4 hours
- Monthly screening coverage = 100% of active customers
