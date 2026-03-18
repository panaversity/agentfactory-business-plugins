---
name: metrics
description: >
  Activate for: metrics, KPI, operational metrics, performance metrics,
  operational dashboard, performance measurement, operations reporting,
  monthly report operations, operations scorecard, leading indicator,
  lagging indicator, red amber green, RAG status, operational performance,
  KRI, key risk indicator, SLA metrics, efficiency metrics, throughput,
  cycle time, error rate, cost per transaction, operational excellence,
  metrics framework, dashboard design, metric definition.
  NOT for: generating status reports (use official /status-report),
  vendor performance scoring (use official /vendor-review), risk
  register building (use official risk-assessment auto-skill).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/metrics"
  mcp-integrations: "ERP, ITSM, compliance system, document store"
---

## UNIVERSAL RULES (apply to every metrics task)

- NEVER produce a metrics framework without defined red thresholds --
  a metric without an alarm level is just reporting; it does not drive action
- NEVER produce more than 10 metrics for an operational dashboard --
  if everything is measured, nothing is managed
- NEVER accept "the team will monitor" as a metric owner -- one named person
- ALWAYS include at least one leading indicator for every major risk area
- ALWAYS load ops.local.md for existing KPI targets, reporting cadence,
  and dashboard configuration

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          [e.g. Operational Metrics Framework Design]
DOCUMENT TYPE: [Framework / Dashboard / Monthly Report / Metric Definition]
CONFIGURATION: [Loaded: ops.local.md / Not configured]
DATE:          [Date of output]
OWNER:         [Named person responsible]
REVIEW DATE:   [When to review/update]
```

## METRICS FRAMEWORK DESIGN PRINCIPLES

PRINCIPLE 1: MEASURE WHAT MATTERS, NOT WHAT IS EASY
The easiest metrics to collect are often the least useful.
Start from: "What do we need to know to run operations well?"
Then determine how to measure it -- not the other way round.

PRINCIPLE 2: LEADING INDICATORS OVER LAGGING
Lagging: tells you what happened (incidents last month)
Leading: tells you what is about to happen (open SLA warnings)
Every major risk area should have at least one leading indicator.

PRINCIPLE 3: EVERY METRIC HAS AN OWNER
A metric nobody is responsible for improving is decoration.
Every metric must have a named owner accountable for both the
measurement and the performance it reflects.

PRINCIPLE 4: RED THRESHOLDS TRIGGER ACTIONS
Metrics without defined red thresholds are thermometers, not alarms.
Define: what level triggers an escalation? To whom? By when?

PRINCIPLE 5: FEWER, BETTER
5-10 well-chosen metrics that tell the operational story clearly
are worth more than 30 metrics nobody reads.

## METRICS WORKFLOW

### Task Type 1: METRIC DEFINITION

For each metric:

```
METRIC: [Name -- short, descriptive]
----------------------------------------------------------------
What it measures: [Plain language -- one sentence]
Why it matters:   [What decision or action this metric informs]
Type:             [LEADING / LAGGING]
Formula:          [Exactly how calculated -- no ambiguity]
Data source:      [Where the data comes from]
Measurement freq: [Daily / Weekly / Monthly]
Owner:            [Named role -- who produces AND is responsible]

Thresholds:
  GREEN:  [Target range -- what good looks like]
  AMBER:  [Watch zone -- investigate; action may be needed]
  RED:    [Action zone -- escalate to [role] within [timeframe]]

Trend direction:  [Higher is better / Lower is better / Target is stable]
----------------------------------------------------------------
```

### Task Type 2: METRICS FRAMEWORK (FULL DASHBOARD)

Design a complete operational metrics framework:

```
OPERATIONAL METRICS FRAMEWORK: [Organisation / Function]
================================================================

VENDOR MANAGEMENT:
  [Metric] | [Type] | [Owner] | [Green] | [Amber] | [Red]
  - Vendor SLA compliance rate (Lagging)
  - Renewal pipeline value (Leading)
  - Open SLA warnings (Leading)
  - Vendor spend vs. budget (Lagging)

PROCESS OPERATIONS:
  - Process error rate (Lagging)
  - SOP currency rate (Leading)
  - Key-person dependency count (Leading)
  - Cycle time (Lagging)

CHANGE MANAGEMENT:
  - Change failure rate (Lagging)
  - Changes without impact assessment (Leading)
  - PIR completion rate (Lagging)
  - Emergency change rate (Leading/Lagging)

COMPLIANCE:
  - Obligation currency rate (Leading)
  - Evidence age (Leading)
  - Audit findings open (Lagging)
  - Regulatory change response time (Lagging)

RISK:
  - Risk register review completion (Leading)
  - Risks above appetite (Leading)
  - Mitigation action completion rate (Lagging)

INCIDENT:
  - MTTR by severity (Lagging)
  - MTTD (Lagging/Leading)
  - Corrective action completion rate (Lagging)
  - Repeat incident rate (Lagging -- key signal)

RECOMMENDED TOP 5-10 FOR DASHBOARD:
[Select the most impactful from above for the executive dashboard]
================================================================
```

### Task Type 3: MONTHLY OPERATIONAL REPORT

```
MONTHLY OPERATIONS REPORT: [Month Year]
Prepared by: [Name] | For: [COO / Board / Ops team]
================================================================
HEADLINE STATUS: [STABLE / WATCH ITEMS / ACTION REQUIRED]

| Metric | Status | This Month | Last Month | Trend | Action |
|---|---|---|---|---|---|
| [Name] | [G/A/R] | [Value] | [Value] | [Up/Down/Stable] | [If needed] |

KEY ISSUES:
[RED metrics only -- specific; what is being done]

WATCH ITEMS:
[AMBER metrics -- what we are monitoring and why]

COMPLETED ACTIONS (from last month):
[What was agreed and is now done]

UPCOMING:
[What needs attention in the next 30 days]
================================================================
```

## STANDARD OPERATIONS METRICS LIBRARY

Reference library of common operational metrics by domain:

VENDOR: SLA compliance %, renewal pipeline value, open SLA warnings,
spend vs. budget
PROCESS: error rate per 1000 transactions, SOP currency %, key-person
dependency count, cycle time
CHANGE: failure rate %, changes without impact assessment, PIR completion
rate, emergency change rate
COMPLIANCE: obligation currency %, evidence age, open audit findings,
regulatory change response time
RISK: register review completion %, risks above appetite, mitigation
completion rate, risk materialisation rate
INCIDENT: MTTR, MTTD, CA completion rate, repeat incident rate

## NEVER DO THESE

- NEVER report only lagging indicators -- by the time they are red,
  the problem has already occurred; leading indicators prevent it
- NEVER define a metric by its data source rather than what it measures
  ("Zendesk tickets" is a data source; "unresolved customer issues rate"
  is a metric)
- NEVER produce a monthly report without the KEY ISSUES section --
  the report's value is in driving decisions, not documenting data
- NEVER design a framework with more than 10 executive dashboard metrics
- NEVER omit the formula field -- ambiguous calculation leads to
  inconsistent measurement and disputed results

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
