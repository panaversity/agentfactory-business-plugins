# /pipeline

Pipeline review and analysis with three-dimension scoring and forecast.

## Usage

/pipeline [filter] [context]

## Examples

/pipeline "Q3 2026" "Quarterly business review prep"
/pipeline "enterprise tier" "Board deck — need weighted forecast"
/pipeline "at-risk deals" "Identify deals that need intervention this week"

## Workflow

1. Route to pipeline skill via sales-marketing-global-router
2. Pull CRM pipeline data and apply filter criteria
3. Analyse deals by stage, value, and age
4. Apply three-dimension scoring (fit, timing, engagement) to each deal
5. Calculate pipeline coverage ratio against target
6. Flag at-risk deals with specific risk reasons
7. Generate weighted forecast with confidence bands

## Output

- Mandatory header block (task, filter applied, configuration, verify data)
- Pipeline summary: total value, weighted value, deal count by stage
- Deal-level analysis: top deals with score, stage, value, and next action
- At-risk deals with risk reasons and recommended interventions
- Coverage ratio against quota or target
- Weighted forecast with confidence range
- Recommended actions: deals to advance, rescue, or disqualify

PIPELINE ANALYSIS BASED ON AVAILABLE CRM DATA — VERIFY DEAL STATUSES ARE CURRENT
