# Exercise 8: The Legal Ops Dashboard

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Type**            | Integration and Measurement                   |
| **Time**            | 60 minutes                                    |
| **Skills Required** | All product skills                            |
| **Plugin Commands** | `/vendor-check`, `/legal-brief`               |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance |

---

## Overview

You have now built a negotiation playbook, contract review workflow, NDA triage
system, IP monitoring brief, regulatory monitoring workflow, and DSAR agent.
This exercise ties them together into the Legal Operations Dashboard your
General Counsel needs to run the function strategically.

---

## Steps

### Step 1 -- Define the KPIs

| Metric                                  | Data Source           | Target                                    |
| --------------------------------------- | --------------------- | ----------------------------------------- |
| Contract review cycle time (by tier)    | Contract tracking log | Tier 1: <=1 day; Tier 2: <=2; Tier 3: <=5 |
| NDA Tier 1 auto-approval rate           | NDA triage log        | >60%                                      |
| Open RED items pending attorney review  | Contract queue        | Zero items >5 days old                    |
| Contracts with renewal dates in 60 days | Contract repository   | 100% visibility                           |
| Overdue compliance obligations          | Compliance calendar   | Zero overdue                              |
| Open DSARs vs. 30-day window            | DSAR log              | Zero overdue                              |
| Regulatory alerts actioned              | Monitoring log        | 100% within 30 days                       |
| External legal spend vs. budget         | AP system             | Within 10% of budget                      |

### Step 2 -- Build the Dashboard

```
/legal-brief topic:"legal-ops-dashboard"
      data-sources:
        - "contract tracking log [link]"
        - "NDA triage log [link]"
        - "compliance calendar [link]"
        - "DSAR log [link]"
      output:"weekly dashboard for General Counsel"
      include:"RAG status per category; trend vs. prior week;
               items requiring GC personal attention"
```

### Step 3 -- Write the Weekly GC Briefing

Using the dashboard, draft a 1-page briefing for your General Counsel:

- Takes 5 minutes to read
- Immediate picture of the legal pipeline state
- Items requiring GC personal attention clearly identified
- Emerging risks identified before they become urgent

### Step 4 -- Measure the Transformation

| Function                       | Hours/month before | Hours/month after | Saving |
| ------------------------------ | ------------------ | ----------------- | ------ |
| Contract review                |                    |                   |        |
| NDA triage (attorney time)     |                    |                   |        |
| Regulatory monitoring          |                    |                   |        |
| DSAR processing (per request)  |                    |                   |        |
| Compliance calendar management |                    |                   |        |
| **Total**                      |                    |                   |        |

---

## Deliverable

A Legal Ops Dashboard specification, a sample weekly GC briefing, and a
documented ROI analysis showing the capacity transformation in your legal
department.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
