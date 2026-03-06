# Exercise 6: Regulatory Monitoring -- The Weekly Brief

## Scenario Profile

| Field               | Value                                          |
| ------------------- | ---------------------------------------------- |
| **Type**            | Workflow Configuration                         |
| **Time**            | 45 minutes                                     |
| **Skills Required** | `regulatory-monitoring`, `legal-global-router` |
| **Plugin Command**  | `/legal-brief`                                 |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance  |

---

## Overview

You are Compliance Officer at a 150-person technology company with UK and EU
operations. Your board has asked for a monthly regulatory briefing covering:
data protection, AI regulation, employment law, and company law. This currently
takes 4-6 hours per month.

---

## Steps

### Step 1 -- Configure Monitoring Parameters

```
/legal-brief type:"regulatory-monitoring-setup"
      organisation:"technology company, 150 employees,
                    UK and EU operations, SaaS product"
      primary-areas:
        - "Data Protection: UK GDPR, EU GDPR, ICO guidance"
        - "AI Regulation: EU AI Act implementation, UK AI framework"
        - "Employment: UK employment law, EU Working Time,
           remote working developments"
        - "Company Law: Companies House requirements, director duties"
      jurisdictions:"UK, EU (Germany, France, Netherlands primary)"
      output:"weekly monitoring brief + monthly board summary"
```

### Step 2 -- Run a Live Test Brief

Use the current week. Evaluate:

- Did it identify genuine regulatory developments?
- Are the impact assessments (HIGH/MONITOR/AWARENESS) correctly calibrated?
- Is anything missing that you know should be covered?

Update configuration based on gaps. Re-run.

### Step 3 -- Build the Monthly Board Summary Template

The board summary needs:

- 3-5 bullet executive summary (most important changes this month)
- RAG traffic-light status for each regulatory area
- Actions required (owner, action, deadline)
- Horizon items (significant changes in next 3-6 months)

Draft this template. Test by producing a sample monthly summary from
four weeks of monitoring briefs.

---

## Deliverable

Working regulatory monitoring configuration producing weekly briefs and
a monthly board summary -- reducing preparation time from 4-6 hours to
45-60 minutes of review and sign-off.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
