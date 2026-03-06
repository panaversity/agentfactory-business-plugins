# Exercise 4: IP Monitoring -- Competitor Patent Watch

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Type**            | Applied Research                              |
| **Time**            | 45 minutes                                    |
| **Skills Required** | `ip-protection`, `legal-global-router`        |
| **Plugin Command**  | `/legal-brief`                                |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance |

---

## Overview

You are in-house counsel for a company that has developed a proprietary AI-based
document analysis system. Your legal team has asked you to establish a patent
monitoring programme for two key competitors and to assess freedom-to-operate
risk before launching your next product feature.

---

## Steps

### Step 1 -- Landscape Analysis

```
/legal-brief topic:"patent landscape analysis"
      technology:"AI document analysis, natural language processing,
                  contract review automation, clause extraction"
      key-competitors:"[Competitor 1], [Competitor 2]"
      scope:"patents filed or granted 2021-2026"
      jurisdictions:"US (USPTO), EU (EPO), UK (UKIPO)"
      output:"landscape summary with freedom-to-operate flags"
```

Analyse: Who are the most active filers? Are there patents with broad claim
language that may cover your planned feature? What white spaces exist?

### Step 2 -- Set Up Weekly Competitor Monitoring

```
/legal-brief topic:"patent monitoring brief"
      monitor-assignees:"[Competitor 1], [Competitor 2]"
      technology-keywords:"[list 5-8 relevant technical terms]"
      jurisdictions:"US, EU, UK"
      output:"weekly summary for IP attorney"
```

Draft the monitoring brief template for weekly delivery to your IP attorney.

### Step 3 -- FTO Preliminary Assessment Brief

```
/legal-brief topic:"freedom-to-operate preliminary research"
      our-technology:"[describe planned feature in 2-3 sentences]"
      potentially-relevant:"[list patents from Step 1]"
      jurisdiction:"US"
      note:"This is preliminary research for attorney review,
            not a freedom-to-operate opinion."
```

Write the cover memo to your IP attorney that accurately characterises
what the agent produced and what you need them to confirm or act on.

---

## Governance Reminder

The output of Step 3 is research scaffolding for your IP attorney -- not an
FTO opinion. The cover memo must make this crystal clear. An FTO opinion is
a privileged legal opinion signed by a qualified IP attorney.

---

## Deliverable

IP monitoring workflow + weekly competitor brief template + FTO research memo
correctly scoped for attorney review.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
