# /score-lead

Three-dimension lead scoring with fit, timing, and engagement analysis.

## Usage

/score-lead [company] [contact-name] [context]

## Examples

/score-lead "Meridian Logistics" "Jane Smith, VP Operations" "Inbound from whitepaper download"
/score-lead "Al Baraka Holdings" "Fatima Al-Rashid, CFO" "Referral from existing customer"
/score-lead "Nordic Supply GmbH" "Thomas Berg, Head of IT" "LinkedIn ad click, visited pricing page"

## Workflow

1. Route to lead-scoring skill via sales-marketing-global-router
2. Load scoring weights from sales-marketing.local.md if configured
3. Score Dimension 1: Fit (0-40 points) -- ICP match on firmographics
4. Score Dimension 2: Timing (0-40 points) -- external buying signals via web research
5. Score Dimension 3: Engagement (0-20 points) -- prospect actions and interactions
6. Calculate total score (0-100) and classify tier
7. Route to correct tier: HOT (80+) / WARM (60-79) / CULTIVATE (40-59) / NOT YET (<40)
8. Provide specific recommended action and next review date

## Output

- Mandatory header block (task, ICP match, configuration, verify data)
- Total score with tier classification
- Dimension-by-dimension breakdown with scoring rationale
- Score rationale (why this score reflects actual buying readiness)
- Recommended action: routing, outreach channel, timing, positioning
- Next review date based on signal urgency

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
