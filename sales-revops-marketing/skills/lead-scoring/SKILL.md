---
name: lead-scoring
description: >
  Activate for: lead score, score this lead, qualify, qualification,
  lead quality, ICP match, fit score, should we pursue, is this a good
  lead, lead tier, hot lead, warm lead, MQL, SQL, prioritise leads,
  lead ranking, lead rating, account score.
  NOT for: prospect research (use prospect-research), CRM enrichment (use crm-enrichment), outreach drafting (use outreach), pipeline forecasting (use pipeline).
---

## THREE-DIMENSION SCORING MODEL

Every lead is scored across three independent dimensions.
Total score: 0-100.

### Dimension 1: Fit Score (0-40 points)

How closely does the prospect match the configured ICP?
Load scoring weights from sales-marketing.local.md.

Default weight allocation (customise in local config):
Company size match: 0-8 points
Revenue range match: 0-8 points
Industry / vertical: 0-8 points
Technology maturity: 0-8 points
Geography / territory: 0-4 points
Persona seniority: 0-4 points

Scoring:
Exact match to ICP: Full points
Within acceptable range: Half points
Outside range: Zero points

### Dimension 2: Timing Score (0-40 points)

What external signals suggest buying readiness RIGHT NOW?
This dimension requires web research via search MCP.

Signal weights (customise in local config):
Funding announcement (last 30 days): 15 points
Major new contract win: 15 points
New leadership in target role (<6 months): 12 points
Rapid hiring in target department: 10 points
Prospect posted about your problem area: 8 points
Office / facility expansion: 8 points
Regulatory change affecting their sector: 6 points
Website visit (pricing/solution page): 6 points
Job posting in target department: 4 points
General growth signals: 3 points

MAXIMUM timing score: 40 (cap at 40 even if multiple signals stack)

### Dimension 3: Engagement Score (0-20 points)

What has the prospect done that signals active interest?
Load from CRM / email platform / web analytics via MCP.

Pricing page visit (unprompted): 8 points
Content download (gated asset): 8 points
Email open + click: 6 points
Webinar or event attendance: 6 points
Social engagement with your content: 4 points
Email open only (no click): 2 points
Form submission (contact us / demo request): 20 points (auto HOT)

## SCORE CLASSIFICATION AND ROUTING

| Score  | Tier | Label            | Action                            | SLA      |
| ------ | ---- | ---------------- | --------------------------------- | -------- |
| 80-100 | HOT  | HOT -- Immediate | Personal outreach; priority queue | 24 hours |
| 60-79  | WARM | WARM -- MQL      | Personalised sequence; follow-up  | 5 days   |
| 40-59  | CULT | CULTIVATE        | Marketing nurture; quarterly      | No SLA   |
| 0-39   | NYT  | NOT YET          | Monitor; do not invest sales time | Monitor  |

## SCORE OUTPUT FORMAT

# LEAD SCORE: [Company] / [Contact Name]

TOTAL SCORE: [X] / 100 -- [Tier label]

FIT SCORE: [X] / 40
[Criterion]: [+points] ([explanation])

TIMING SCORE: [X] / 40
[Signal]: [+points] ([source and date])

ENGAGEMENT SCORE: [X] / 20
[Action]: [+points] ([date])

SCORE RATIONALE:
[2-3 sentences explaining why this score reflects this lead's
actual buying readiness -- not just a summary of the numbers]

RECOMMENDED ACTION:
Route to: [Rep name / tier / territory]
Outreach: [Channel and timing]
Frame: [Positioning recommendation]
Goal: [First touch goal]

# NEXT REVIEW: [Date -- set based on timing signal urgency]

## SCORE RECALIBRATION

Run /score recalibration if:

- Conversion rates from HOT leads are below 15% (threshold too low)
- HOT leads are too few (<3/week) despite healthy pipeline (threshold too high)
- Closed-won deals were not HOT-scored at time of first touch (model missing signals)

Recalibration method:

1. Take last 20 closed-won deals; score retroactively
2. All should score 60+. If <80% do: identify missing dimensions
3. Take last 10 significant losses; score retroactively
4. These should score 50-70. If higher: investigate why they lost
5. Adjust weights; re-test; document changes in sales-marketing.local.md

## NEVER DO THESE

- NEVER route a lead as HOT based on Fit Score alone -- timing must be present
- NEVER ignore a Dimension 2 (Timing) signal because Dimension 1 (Fit) is weak
  -- flag as "wrong-fit but hot timing; monitor for right-fit contact at company"
- NEVER mark a demo request or contact-us form as anything below HOT
- NEVER set and forget the scoring model -- recalibrate quarterly
- NEVER score leads without checking Dimension 2 via web search -- stale
  CRM data without external signal check is a Fit-only score, not a full score
