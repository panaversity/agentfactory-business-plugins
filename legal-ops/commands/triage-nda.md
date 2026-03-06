# /triage-nda

Rapid NDA pre-screening and three-tier routing recommendation.

## Usage

/triage-nda [nda-type] [counterparty-context]

## Examples

/triage-nda "mutual NDA" "prospective technology partner, need response by Friday"
/triage-nda "unilateral NDA" "large enterprise vendor, M&A due diligence"
/triage-nda "incoming NDA" "new SaaS vendor, routine evaluation"

## Workflow

1. Route to nda-triage skill via legal-global-router
2. Load NDA configuration from playbook (legal.local.md) if available
3. Gather context: mutual/unilateral, purpose, counterparty type, urgency
4. Compare incoming NDA against standard form or general commercial standards
5. Classify deviations and assign tier:
   - Tier 1: Standard Approval (no attorney review) -- target 60-70%
   - Tier 2: Counsel Review (attorney review, no negotiation expected) -- target 20-30%
   - Tier 3: Full Review (attorney review + likely negotiation) -- target 10-15%
6. Check for automatic RED flags (residuals clause, no public info carve-out, etc.)
7. Produce triage report with routing recommendation

## Output

- NDA Triage Report with tier classification
- Estimated attorney time: 0 / ~15 min / ~45 min
- Deviation summary: GREEN/YELLOW/RED counts
- Routing recommendation with specific deviations listed

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
