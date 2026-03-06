# Workflow Recipe: Weekly RevOps Review -- End-to-End

## Task Overview

| Field         | Value                                                                        |
| ------------- | ---------------------------------------------------------------------------- |
| **Task Name** | Weekly RevOps Review: Automated Dashboard Generation and Leadership Briefing |
| **Frequency** | Weekly (Monday morning; Friday for marketing performance)                    |
| **Purpose**   | Generate revenue and marketing dashboards, surface risks, brief leadership   |
| **Owner**     | RevOps Lead / VP Sales                                                       |

---

## Trigger Conditions

| Trigger             | Condition                                       | Action                                              |
| ------------------- | ----------------------------------------------- | --------------------------------------------------- |
| **Monday schedule** | Weekly cadence (configurable day)               | Start revenue dashboard generation                  |
| **Friday schedule** | Weekly cadence (configurable day)               | Start marketing performance report                  |
| **Ad hoc request**  | Leadership requests pipeline or revenue update  | Start at Step 2 for revenue or Step 3 for marketing |
| **Alert threshold** | Leading indicator breaches configured threshold | Immediate alert (bypass weekly cadence)             |

---

## Step-by-Step Execution

### Step 1: Data Freshness Check

```
Input: Configured data sources (CRM, marketing platform, finance system)
Actions:
  - Verify CRM data freshness: last sync must be < 48 hours
  - Verify marketing platform data: last sync must be < 7 days
  - If any source is stale: flag explicitly in dashboard header
  - If CRM sync failed: alert RevOps lead, do NOT generate dashboard
    with stale data silently

Output: Data freshness validation report
```

### Step 2: Revenue Dashboard (Monday)

```
Input: CRM pipeline data + forecast data + prior period benchmarks
Actions:
  - Revenue Reporting Agent generates weekly dashboard:
    -> Pipeline metrics: total, weighted, coverage ratio, at-risk deals
    -> Lead velocity: HOT leads, MQL->SAL conversion, cycle length
    -> Forecast: committed, likely, upside vs. quarterly target
    -> Leading indicator alerts with downstream revenue impact
  - Cross-reference forecast with activity signals (not just rep probability)
  - Identify top WIN, top RISK, and top ASK for leadership

Output: Revenue dashboard with highlights and at-risk deal list
```

### Step 3: Marketing Performance Report (Friday)

```
Input: Channel data from all connected platforms + campaign KPIs
Actions:
  - Marketing Performance Agent pulls weekly data:
    -> LinkedIn: impressions, clicks, CTR, CPC, CPL
    -> Google Analytics: sessions by source, conversion rates
    -> Email: open rate, click rate, unsubscribe rate
    -> CRM: leads by source, score distribution, pipeline from marketing
  - Compare actuals to targets AND to prior week (trend)
  - Run performance analysis: top 3 optimisation recommendations
  - Flag anomalies for immediate alert if threshold breached

Output: Marketing performance report (full + summary versions)
```

### Step 4: CRM Health Check

```
Input: CRM database quality metrics
Actions:
  - CRM Hygiene Agent runs weekly scan:
    -> HOT/WARM leads with enrichment > 7 days old
    -> Contact verification (email deliverability)
    -> Role changes detected
    -> Score changes crossing 60-point threshold
  - Generate data quality snapshot for RevOps

Output: CRM health summary appended to weekly review
```

### Step 5: Distribute Reports

```
Distribution rules:
  - Revenue dashboard (Monday):
    -> Full report: VP Sales, RevOps Lead, Sales Managers
    -> Summary only: CEO, VP Marketing
  - Marketing performance (Friday):
    -> Full report: Marketing team
    -> Summary only: VP Marketing, VP Sales, CEO
  - Anomaly alerts (immediate):
    -> RevOps Lead + relevant VP (based on alert type)

All distribution lists configurable in sales-marketing.local.md
```

### Step 6: Track Actions and Follow-Up

```
After distribution:
  - Log dashboard generation in CRM activity log
  - Track which at-risk deals were actioned by reps
  - If at-risk deal still inactive after 7 days: re-escalate
  - Carry forward unresolved RISKs and ASKs to next week's dashboard
  - At month-end: generate trend summary (4-week rolling)

Output: Action tracking log updated weekly
```

---

## Required Skill Files

| Skill File                      | Purpose                                |
| ------------------------------- | -------------------------------------- |
| `revenue-reporting-agent`       | Monday revenue dashboard generation    |
| `marketing-performance-agent`   | Friday marketing performance reporting |
| `crm-hygiene-agent`             | Weekly CRM health check                |
| `pipeline`                      | Pipeline analysis for deep dives       |
| `performance-analysis`          | On-demand marketing analysis           |
| `lead-intelligence-agent`       | Signal alerts that feed into dashboard |
| `sales-marketing-global-router` | Routing and configuration              |

---

## Escalation / Review Checkpoints

| Checkpoint              | Condition                                      | Reviewer        |
| ----------------------- | ---------------------------------------------- | --------------- |
| **Data freshness**      | Any source > freshness threshold               | RevOps Lead     |
| **Pipeline coverage**   | Coverage ratio < configured threshold          | VP Sales + CEO  |
| **MQL->SAL conversion** | Below threshold for 2+ consecutive weeks       | VP Marketing    |
| **At-risk pipeline**    | > 15% of total pipeline at risk                | VP Sales        |
| **Anomaly alert**       | Any immediate alert threshold breached         | RevOps Lead     |
| **Month-end trend**     | Rolling 4-week trends require strategic review | Leadership team |

ALL DASHBOARD DATA SHOULD BE VERIFIED AGAINST SOURCE SYSTEMS
