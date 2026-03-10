---
name: pipeline
description: >
  Activate for: pipeline, pipeline review, pipeline analysis, pipeline report,
  forecast, sales forecast, deal review, deal health, at risk deals, stalled
  deals, pipeline hygiene, win rate, close rate, pipeline by stage, weighted
  pipeline, coverage ratio, pipeline gap, revenue forecast, quarterly forecast.
  NOT for: lead scoring (use lead-scoring), prospect research (use prospect-research), weekly revenue dashboard (use revenue-reporting-agent), campaign performance (use performance-analysis).
context: fork
---

## PIPELINE ANALYSIS WORKFLOW

### Input Required

Pull from CRM via MCP or accept pasted export containing:

- Deal name / company
- Deal value
- Stage (defined in your pipeline stages)
- Last activity date
- Expected close date
- Assigned rep
- Lead source
- Any notes or context

### Analysis Dimensions

DIMENSION 1: Pipeline Health

- Total pipeline value by stage
- Weighted pipeline (value x stage probability)
- Pipeline coverage ratio (total pipeline / quota remaining)
- Average deal size vs. target
- Pipeline velocity (average days per stage)

DIMENSION 2: Risk Identification
Flag as AT RISK if any of:

- No activity logged in >14 days
- Expected close date passed with no stage change
- Deal has been in same stage >2x average stage duration
- Champion contact has changed roles (detected via /enrich)
- Competitor mentioned but not logged in CRM
- Budget not confirmed after qualification stage

Flag as STALLED if:

- No activity >30 days
- No next step agreed
- Close date pushed >2x without explanation

DIMENSION 3: Forecast Accuracy

- Compare rep-submitted forecast vs. weighted pipeline model
- Identify deals where rep confidence differs materially from signals
- Flag sandbagged deals (high confidence; low activity)
- Flag optimistic deals (high value; low engagement signals)

DIMENSION 4: Source Analysis

- Pipeline created by channel / campaign (last 90 days)
- Win rate by lead source
- Average deal size by source
- CAC by source (if cost data available)

### Pipeline Report Format

# PIPELINE REPORT -- [Date] | [Period: weekly / monthly / QBR]

SUMMARY
Total pipeline: [X]
Weighted pipeline: [X]
Coverage ratio: [X]x quota
Deals in pipeline: [N] across [N] stages

STAGE BREAKDOWN
[Stage name]: [N] deals | [X] total | avg [X] | avg [N] days in stage

FORECAST THIS QUARTER
Committed (>80% probability): [X] -- [N] deals
Likely (50-80%): [X] -- [N] deals
Upside (<50%): [X] -- [N] deals
Realistic forecast: [X]

AT-RISK DEALS -- IMMEDIATE ACTION REQUIRED
[Deal name] | [X] | [Stage] | Last activity: [N] days ago
Risk: [Specific reason] | Action: [Specific recommended next step]

STALLED DEALS -- REVIEW OR REMOVE
[Deal name] | [X] | Stalled [N] days | Recommend: [action / close lost]

TOP 5 DEALS TO CLOSE THIS QUARTER
[Rank] [Deal] | [X] | [Stage] | [Close date] | [Confidence signal]
Next action: [Specific]

PIPELINE GAPS
[If coverage ratio is below 3x]: Pipeline gap: [X]
Source recommendations to fill gap:
[Which channels/campaigns are generating the best pipeline per invested]

WINS THIS PERIOD
[N] deals closed | [X] total | Win rate: [X]% | Avg cycle: [N] days

KEY METRICS vs. TARGETS
[Metric] | [Actual] | [Target] | [vs. Target]
================================================================

## NEVER DO THESE

- NEVER forecast based on rep optimism alone -- always cross-reference
  with activity signals and stage duration vs. average
- NEVER leave an AT RISK deal in the pipeline without a specific
  recommended action and deadline for that action
- NEVER remove a deal from pipeline without logging the loss reason --
  loss reasons are the most valuable sales intelligence you have
- NEVER accept "expected to close this quarter" without confirming:
  has the prospect confirmed the timeline directly?
