# /brief

Pre-call and pre-meeting brief with ICP-scored context and deal health analysis.

## Usage

/brief [prospect-name] [meeting-type] [context]

## Examples

/brief "Jane Smith, Meridian Logistics" "discovery call" "First meeting, inbound from whitepaper"
/brief "Ahmed Khan, TechServe Pakistan" "demo" "Second call, requested pricing last week"
/brief "Sarah Mueller, Nordic Supply GmbH" "renewal review" "Contract expires in 60 days, usage declining"

## Workflow

1. Route to pre-call-brief skill via sales-marketing-global-router
2. Pull upstream research, scoring, and outreach history for this prospect
3. Assess deal health across three dimensions: fit, timing, engagement
4. Identify talking points, risks, and questions based on prospect context
5. Generate conversation starters tailored to meeting type and stage
6. Flag any data gaps or hallucination risks carried forward from earlier research

## Output

- Mandatory header block (task, prospect, meeting type, configuration, verify data)
- Deal health summary: fit score, timing score, engagement score
- Prospect context: role, company, recent activity, relationship history
- Meeting objective and desired outcome
- Talking points (3-5) with supporting evidence
- Questions to ask (3-5) tailored to meeting type
- Topics to avoid and reasons
- Conversation starters
- Cautions: data gaps and confidence warnings

VERIFY ALL PROSPECT DATA BEFORE THE MEETING
