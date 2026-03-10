---
name: sales-marketing-global-router
description: >
  TOP-LEVEL ROUTER. Activate when ANY of these terms appear:
  prospect, lead, outreach, email, LinkedIn message, cold email, sales,
  CRM, Salesforce, HubSpot, Pipedrive, pipeline, deal, opportunity,
  discovery call, demo, follow-up, sequence, nurture, ICP, ideal customer,
  lead score, lead scoring, enrich, enrichment, account research, research
  prospect, campaign, content, marketing, SEO, social media, LinkedIn ad,
  blog post, whitepaper, case study, newsletter, persona, buyer persona,
  audience segment, performance analysis, analytics, RevOps, revenue
  operations, marketing qualified lead, MQL, sales qualified lead, SQL,
  sales accepted lead, SAL, ghostwrite, personalised outreach, account
  intelligence, signal, timing signal, brand voice, content calendar,
  campaign brief, ad copy, landing page, subject line, A/B test.
  NOT for: legal advice, contract review, regulatory compliance, financial advisory, tax advice, HR decisions, litigation strategy.
---

## STEP 1 -- IDENTIFY TASK AND LOAD PRODUCT SKILL

| Query Pattern                             | Load Product Skill                   |
| ----------------------------------------- | ------------------------------------ |
| Prospect/account research, account intel  | skills/prospect-research/SKILL.md    |
| Lead scoring, qualification, ICP match    | skills/lead-scoring/SKILL.md         |
| CRM enrichment, data update, data hygiene | skills/crm-enrichment/SKILL.md       |
| Outreach email, LinkedIn DM, cold message | skills/outreach/SKILL.md             |
| Multi-touch sequence, cadence             | skills/sequence/SKILL.md             |
| Pre-call brief, pre-meeting, deal health  | skills/pre-call-brief/SKILL.md       |
| Follow-up after call/demo/meeting         | skills/follow-up/SKILL.md            |
| Pipeline analysis, forecast, deal review  | skills/pipeline/SKILL.md             |
| Content creation (any format)             | skills/content-creation/SKILL.md     |
| Campaign planning, campaign brief         | skills/campaign-planning/SKILL.md    |
| Ad copy, landing page, subject line, CTA  | skills/copywriting/SKILL.md          |
| Campaign performance, analytics, optimise | skills/performance-analysis/SKILL.md |
| Content calendar, publishing schedule     | skills/content-calendar/SKILL.md     |
| Persona, ICP, buyer profile, audience     | skills/persona-icp/SKILL.md          |

## STEP 2 -- IDENTIFY TASK AND LOAD AGENT

| Query Pattern                                     | Load Agent                            |
| ------------------------------------------------- | ------------------------------------- |
| HOT signal monitoring, prospect alerts, signals   | agents/lead-intelligence-agent.md     |
| CRM hygiene, data quality, bulk enrichment        | agents/crm-hygiene-agent.md           |
| Sequence management, outreach tracking, touches   | agents/outreach-sequencing-agent.md   |
| Weekly marketing report, automated analytics      | agents/marketing-performance-agent.md |
| Revenue dashboard, pipeline report, Monday report | agents/revenue-reporting-agent.md     |

## STEP 3 -- FOR OUTREACH TASKS: IDENTIFY JURISDICTION AND LOAD OVERLAY

| Jurisdiction / Region        | Load Overlay File                                 |
| ---------------------------- | ------------------------------------------------- |
| USA / US / American          | references/jurisdictions/us-outreach-law.md       |
| EU / Europe / GDPR / Germany | references/jurisdictions/eu-outreach-law.md       |
| Pakistan / Pakistani         | references/jurisdictions/pakistan-outreach-law.md |
| GCC / UAE / Saudi / Bahrain  | references/jurisdictions/gcc-outreach-law.md      |
| Multi-jurisdictional         | Load ALL relevant overlays + flag for review      |
| Unknown / not stated         | Flag; apply most conservative standard            |

## STEP 3B -- SKILL COLLISION RESOLUTION (dual-plugin environment)

When the Anthropic base `knowledge-work-plugins/sales` and `/marketing` plugins are also
installed, the following overlapping skills are resolved automatically:

| Skill                | Base Plugin | Extension | Resolution   |
| -------------------- | ----------- | --------- | ------------ |
| campaign-planning    | Yes         | Yes       | **Wrapper**  |
| content-creation     | Yes         | Yes       | **Wrapper**  |
| prospect-research    | Yes         | Yes       | **Override** |
| outreach             | Yes         | Yes       | **Override** |
| pre-call-brief       | Yes         | Yes       | **Override** |
| performance-analysis | Yes         | Yes       | **Wrapper**  |
| pipeline             | Yes         | Yes       | **Override** |

- **Wrapper**: Route to extension skill. Extension calls base skill internally, then enhances
  output with ICP calibration, jurisdiction compliance, and local configuration.
- **Override**: Route to extension skill exclusively. Extension includes all base functionality
  plus domain-specific logic (three-dimension scoring, Five Laws, jurisdiction overlays).

If only the extension is installed (no base plugins), all skills route to extension directly.

## STEP 4 -- ALWAYS LOAD CONFIGURATION

Always load: sales-marketing.local.md
Check for:

- ICP definition (firmographic + technographic + timing signals)
- Brand voice configuration
- Competitor intelligence
- Persona profiles
- Messaging framework and positioning

IF sales-marketing.local.md NOT FOUND:
Inform user: "No ICP/brand configuration found. Outputs will use general
best practices. For better results, fill in sales-marketing.local.md.
Use the template provided in this skills library."

## STEP 5 -- MANDATORY OUTPUT HEADER (all sales outputs)

TASK: [e.g. Prospect Research -- Meridian Logistics]
ICP MATCH: [STRONG / MODERATE / WEAK / UNVERIFIED]
CONFIGURATION: [Loaded: sales-marketing.local.md / Not configured]
VERIFY DATA: All prospect data should be verified before outreach

## UNIVERSAL RULES -- NON-NEGOTIABLE

- NEVER fabricate prospect data -- only report what is verifiable from sources
- NEVER invent statistics, revenue figures, or company information;
  label estimates explicitly as "estimated" or "unverified"
- NEVER write an outreach message that is not personalised to at least one
  specific, verifiable fact about the prospect or their company
- NEVER lead an outreach message with your product or company name
- NEVER write marketing copy that makes claims the product cannot support
- NEVER skip ICP validation before building research or outreach materials --
  if a lead does not meet minimum ICP criteria, flag it first
- ALWAYS apply the Five Laws of Outreach before finalising any message
- ALWAYS provide specific, actionable recommendations in any analysis --
  observations without recommended actions are not acceptable outputs
- NEVER send a sequence touch after a prospect has replied -- reply = exit sequence
- ALWAYS check jurisdiction overlay for outreach to regulated markets

## THE FIVE LAWS OF OUTREACH (enforce on every message)

Law 1: Reference something specific and real
The message must contain at least one specific, verifiable reference that
proves you researched this person. Not generic -- specific.

Law 2: Lead with their problem, not your product
First sentence is about them. Product appears later as a potential solution
to the problem already established. Never lead with "We help companies..."

Law 3: One ask. One clear next step.
Every message ends with exactly one question or request. Not multiple options.

Law 4: Short.
Email: maximum 150 words. LinkedIn: maximum 100 words.
Every word must earn its place.

Law 5: Sound like a person, not a company.
No: "leverage," "synergy," "best-in-class," "seamless," "robust," "solution."
Yes: direct, specific, human language.

## FIVE LAWS COMPLIANCE CHECK (run before finalising any outreach)

Before outputting any outreach message, confirm:
Law 1: Is there a specific, verifiable reference to this prospect?
Law 2: Does the message lead with their problem, not our product?
Law 3: Is there exactly one ask or one clear next step?
Law 4: Is the message within word count limits?
Law 5: Does the message use direct, human language with no jargon?

If any law is violated: revise before outputting.

## NEVER DO THESE

- NEVER route a query without identifying both the task type AND (for outreach) the jurisdiction
- NEVER skip the configuration check -- if no config found, state explicitly
- NEVER apply a jurisdiction overlay without confirming the prospect's location
- NEVER route legal, financial, HR, or compliance queries -- these are out of scope
- NEVER produce outreach without checking the Five Laws of Outreach

## AGENT ROLE STATEMENT

This agent: researches, drafts, scores, analyses, recommends.
The sales professional: decides, sends, negotiates, closes.
These roles are distinct. Do not conflate them.

## ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
