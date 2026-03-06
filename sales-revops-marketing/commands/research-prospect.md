# /research-prospect

Deep prospect and account intelligence brief for sales preparation.

## Usage

/research-prospect [prospect-name] [title] [company] [context]

## Examples

/research-prospect "Jane Smith" "VP Operations" "Meridian Logistics" "Selling warehouse automation, discovery call next week"
/research-prospect "Ahmed Khan" "CTO" "TechServe Pakistan" "Enterprise SaaS, inbound lead from webinar"
/research-prospect "Sarah Mueller" "Head of Procurement" "Nordic Supply GmbH" "Partner referral, expansion into DACH market"

## Workflow

1. Route to prospect-research skill via sales-marketing-global-router
2. Load ICP and persona configuration from sales-marketing.local.md if configured
3. Gather context: prospect name, title, company, purpose of research
4. Execute contact-level research (LinkedIn, company website, press)
5. Execute account-level research (news, funding, hiring, tech stack)
6. Classify timing signals: HOT / WARM / WATCH
7. Assess pain and product fit against configured ICP
8. Identify the specific hook for personalised outreach
9. Produce research brief with recommended first touch

## Output

- Mandatory header block (task, ICP match, configuration, verify data)
- Contact profile (role, tenure, activity, signal interpretation)
- Account profile (model, revenue, headcount, tech stack, market position)
- Timing signals classified (HOT / WARM / WATCH)
- Pain assessment and product fit
- Recommended hook for outreach
- Recommended first touch channel, tone, and goal

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
