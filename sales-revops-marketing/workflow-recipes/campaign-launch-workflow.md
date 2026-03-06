# Workflow Recipe: Campaign Launch -- End-to-End

## Task Overview

| Field         | Value                                                                     |
| ------------- | ------------------------------------------------------------------------- |
| **Task Name** | Campaign Launch: From Brief through Execution and Performance Measurement |
| **Frequency** | Per campaign (typically monthly or quarterly launch cadence)              |
| **Purpose**   | Plan, build, launch, and measure a multi-channel marketing campaign       |
| **Owner**     | Marketing Manager / Campaign Lead                                         |

---

## Trigger Conditions

| Trigger                | Condition                                          | Action                                       |
| ---------------------- | -------------------------------------------------- | -------------------------------------------- |
| **Quarterly planning** | New quarter begins; campaign calendar slot open    | Start at Step 1                              |
| **Product launch**     | New product/feature requires go-to-market campaign | Start at Step 1; flag cross-functional       |
| **Performance gap**    | Performance analysis shows pipeline shortfall      | Start at Step 1; focus on pipeline gap       |
| **Opportunistic**      | Market event or competitor signal creates window   | Start at Step 1; compress timeline to 1 week |

---

## Step-by-Step Execution

### Step 1: Campaign Brief

```
Input: Campaign objective, target audience, budget, timeline
Actions:
  - Run /plan-campaign with objective and constraints
  - Generate campaign brief: objective, ICP segments, channel mix,
    budget allocation, content requirements, KPIs, timeline
  - Load persona-icp skill for audience definition
  - Validate ICP alignment with configured ideal customer profiles

Output: Complete campaign brief with measurable KPIs
```

### Step 2: Audience and Messaging

```
Input: Campaign brief + ICP definitions
Actions:
  - Define audience segments from persona-icp profiles
  - Generate messaging matrix: segment x channel x message variant
  - Run copywriting skill for ad copy variants (3 per channel minimum)
  - Run content-creation skill for long-form assets (if needed)
  - Apply Five Laws of Outreach to any direct messaging components

Output: Messaging matrix + all creative assets drafted
```

### Step 3: Content Production

```
Input: Messaging matrix + creative briefs
Actions:
  - Run content-creation for each required asset:
    -> Blog posts, whitepapers, case studies
    -> Landing page copy
    -> Email nurture sequences
  - Run copywriting for each ad variant:
    -> LinkedIn ad copy (headline + body + CTA)
    -> Google Ads copy (headlines + descriptions)
    -> Email subject lines (3 variants per send)
  - Run content-calendar to schedule all content

Output: All assets drafted and scheduled on content calendar
```

### Step 4: Launch Readiness Check

```
Pre-launch verification:
  - All creative assets reviewed and approved by marketing lead
  - Landing pages live and conversion tracking verified
  - UTM parameters configured for all links
  - Email lists segmented and verified (no stale addresses)
  - Ad accounts funded and campaigns in draft
  - CRM lead routing rules configured for inbound leads
  - Jurisdiction compliance checked for all outreach channels

CRITICAL: Campaign lead must approve before any paid spend begins
```

### Step 5: Launch and Monitor

```
On launch day:
  - Activate all scheduled campaigns per content calendar
  - Monitor first 24 hours closely for anomalies:
    -> Ad disapprovals or policy flags
    -> Email bounce rates > 2%
    -> Landing page errors or slow load times
    -> CRM integration errors (leads not flowing)
  - Marketing Performance Agent begins automated tracking

Week 1 check: compare actuals vs. targets for leading indicators
```

### Step 6: Optimise and Report

```
Ongoing (weekly cadence):
  - Marketing Performance Agent pulls weekly channel data
  - Run performance-analysis for on-demand deep dives
  - Identify top 3 optimisation opportunities each week:
    -> Pause underperforming ads (only after 2+ weeks decline)
    -> Increase budget on high-performing channels
    -> A/B test new creative variants
  - Generate weekly performance report for stakeholders
  - At campaign end: final ROI report with learnings

Output: Weekly performance reports + final campaign retrospective
```

---

## Required Skill Files

| Skill File                      | Purpose                                 |
| ------------------------------- | --------------------------------------- |
| `campaign-planning`             | Campaign brief and strategy             |
| `persona-icp`                   | Audience definition and ICP segments    |
| `copywriting`                   | Ad copy and short-form content          |
| `content-creation`              | Long-form content assets                |
| `content-calendar`              | Scheduling and editorial calendar       |
| `performance-analysis`          | On-demand performance deep dives        |
| `marketing-performance-agent`   | Automated weekly reporting              |
| `sales-marketing-global-router` | Routing and jurisdiction identification |

---

## Escalation / Review Checkpoints

| Checkpoint            | Condition                                    | Reviewer          |
| --------------------- | -------------------------------------------- | ----------------- |
| **Brief approved**    | Campaign brief complete with KPIs and budget | VP Marketing      |
| **Creative approved** | All assets reviewed for brand and accuracy   | Marketing Manager |
| **Launch readiness**  | All systems verified and tracking configured | Campaign Lead     |
| **Week 1 review**     | Leading indicators compared to targets       | Marketing Manager |
| **Anomaly alert**     | Any metric breaches alert threshold          | RevOps Lead       |
| **Campaign close**    | Final ROI report and learnings documented    | VP Marketing      |

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
