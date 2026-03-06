# /review-contract

Full clause-by-clause contract review against your organisation's negotiation playbook.

## Usage

/review-contract [contract-type] [jurisdiction] [context]

## Examples

/review-contract "SaaS vendor agreement" "English law" "We are the customer, annual value GBP 48,000"
/review-contract "MSA" "New York law" "Consulting engagement, 6-month term, USD 95,000"
/review-contract "partnership agreement" "UAE/DIFC" "Co-marketing referral arrangement, no cash exchange"

## Workflow

1. Route to contract-review skill via legal-global-router
2. Load the jurisdiction overlay from router references
3. Load the negotiation playbook (legal.local.md) if configured
4. Gather context: party role, contract type, deadline, value, concerns
5. Read the entire contract before flagging any issues
6. Analyse clause-by-clause against playbook or general standards
7. Classify deviations: GREEN (acceptable) / YELLOW (negotiate) / RED (escalate)
8. Generate specific redline text for each YELLOW and RED item
9. Produce holistic risk summary with negotiation priority order

## Output

- Mandatory header block (task, jurisdiction, playbook, attorney review, escalation)
- Clause-by-clause analysis with three-tier classification
- Specific redline language ready to insert for each flagged item
- Holistic risk summary: GREEN/YELLOW/RED counts, material risk, recommendation

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
