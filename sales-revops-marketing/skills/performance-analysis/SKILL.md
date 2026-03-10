---
name: performance-analysis
description: >
  Activate for: performance analysis, campaign performance, marketing analytics,
  channel performance, what's working, what's not working, optimise campaign,
  improve results, weekly report, marketing report, ROI, cost per lead, CPL,
  ROAS, return on ad spend, email performance, LinkedIn performance, A/B results,
  conversion rate, click rate, open rate, lead quality analysis.
  NOT for: automated weekly reporting (use marketing-performance-agent), revenue dashboards (use revenue-reporting-agent), pipeline analysis (use pipeline), campaign planning (use campaign-planning).
context: fork
---

## ANALYSIS WORKFLOW

### Phase 1: Data Collection

Accept via MCP connection or pasted data:

- Channel-level performance (impressions, clicks, CTR, conversions, spend)
- Lead data by source (volume, score distribution, conversion to opp)
- Email performance (open rate, click rate, unsubscribes by email)
- Content performance (downloads, time-on-page, shares)
- CRM data (lead to MQL to SAL to opp conversion rates by source)
- Budget pacing (spend to date vs. plan)

### Phase 2: Analysis Framework

LAYER 1 -- ARE WE ON TRACK?
Compare actuals vs. targets for primary KPI and secondary KPIs.
Classify each metric: On track / At risk / Off track

LAYER 2 -- WHY? (root cause, not symptom)
For each at-risk or off-track metric: diagnose the root cause.
Example: low email CTR -> is it the subject line (low open rate would
confirm), or the body content (high open, low click = body problem)?
Do not recommend actions until root cause is confirmed.

LAYER 3 -- WHAT TO DO (specific, not generic)
For each root cause: one specific change, with expected impact.
"Rewrite Email 3" is not specific enough.
"Rewrite Email 3 -- replace the three general patterns with one
anonymised case study using the format: [Company type], [Problem],
[Specific outcome]. Expected CTR improvement: +1-1.5%." is specific.

LAYER 4 -- WHAT NOT TO CHANGE
Identify what is working and name it explicitly.
Optimisation teams have a bias to change things that are working.
Naming what to protect is as important as naming what to fix.

### Performance Report Output Format

CAMPAIGN PERFORMANCE ANALYSIS -- Week [N] of [Total]
Generated: [Date] | Campaign: [Name]
================================================================

HEADLINE NUMBERS -- THIS PERIOD
[Metric]: [Actual] ([target]) -- [status] [% vs. target]

TOP [N] OPTIMISATION OPPORTUNITIES

[N]. [ISSUE NAME IN CAPS]
Analysis: [What the data shows -- describe the pattern precisely]
Diagnosis: [Root cause -- why this is happening]
Change: [Exact change to make -- specific enough to action immediately]
Owner: [Who does this]
Deadline: [By when]
Expected: [Quantified impact of making this change]

WHAT IS WORKING -- DO NOT CHANGE
[Observation]: [Why it's working and what not to disrupt]

WEEK [N+1] ACTION PLAN
[ ] [Action] -- [Owner] -- by [Date]
================================================================

## BENCHMARKS REFERENCE

| Metric                    | Poor   | Average    | Good | Best-in-class |
| ------------------------- | ------ | ---------- | ---- | ------------- |
| LinkedIn Sponsored CTR    | <0.25% | 0.35-0.45% | 0.6% | >1%           |
| LinkedIn Thought Leader   | <0.6%  | 0.8-1.2%   | 1.5% | >2%           |
| B2B email open rate       | <20%   | 28-35%     | 40%  | >50%          |
| B2B email CTR             | <2%    | 3.5-5%     | 6%   | >8%           |
| Landing page conversion   | <5%    | 10-20%     | 25%  | >35%          |
| Webinar to opp conversion | <10%   | 15-20%     | 25%  | >30%          |
| MQL to SAL                | <20%   | 35-50%     | 60%  | >70%          |
| SAL to opp                | <40%   | 55-70%     | 75%  | >85%          |

## NEVER DO THESE

- NEVER report on metrics without benchmarks -- a number without context
  is meaningless; always compare to target, benchmark, or prior period
- NEVER make recommendations without identifying root cause first
  -- treating symptoms produces temporary improvement at best
- NEVER recommend pausing a channel that is underperforming without first
  testing whether the creative/copy/audience is the problem, not the channel
- NEVER produce observations without actions -- the report exists to
  drive decisions, not to describe what happened
- NEVER report on vanity metrics (impressions, followers, likes) as
  primary success indicators -- measure outcomes that predict revenue
