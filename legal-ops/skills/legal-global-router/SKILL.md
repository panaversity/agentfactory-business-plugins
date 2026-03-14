---
name: legal-global-router
version: 3.0
description: >
  TOP-LEVEL ROUTER. Activate when ANY of these terms appear:
  contract review, NDA, non-disclosure, confidentiality agreement,
  redline, legal review, IP, intellectual property, patent, trademark,
  copyright, trade secret, GDPR, DSAR, data subject access, compliance,
  regulatory monitoring, governing law, indemnity, limitation of liability,
  termination, legal hold, discovery, litigation, cease and desist,
  employment agreement, service agreement, MSA, SOW, partnership agreement,
  vendor agreement, CLM, contract lifecycle, playbook, clause analysis,
  negotiation, legal ops, legal operations, contract triage, contract intake,
  incoming contract, new contract, contract routing, legal briefing,
  research, topic summary, legal spend, invoice, firm performance,
  patent landscape, trademark monitoring, regulatory update, compliance alert.
  NOT for: direct legal advice, court filings, litigation strategy, attorney-client privileged communications, contract execution.
author: Panaversity -- The AI Agent Factory
chapter: 22 -- Legal Operations and Compliance
---

## STEP 1 -- IDENTIFY TASK TYPE AND ROUTE

| Query Pattern                                      | Route To                                        |
| -------------------------------------------------- | ----------------------------------------------- |
| Contract intake, incoming contract, routing        | contract-intake agent                           |
| Contract review, clause analysis, redlines         | Anthropic `/review-contract` (with overlay)     |
| NDA, non-disclosure, confidentiality agreement     | Anthropic `/triage-nda` (with pre-checks below) |
| Vendor assessment, vendor due diligence            | Anthropic `/vendor-check` (with overlay)        |
| Patent, trademark, copyright, trade secret, IP     | ip-protection skill                             |
| Regulatory update, compliance monitoring           | regulatory-monitoring skill                     |
| DSAR, data subject, GDPR request, privacy request  | dsar-privacy skill                              |
| Legal spend, invoice, firm performance             | legal-spend skill                               |
| Renewal, obligation, deadline, compliance calendar | compliance-calendar skill                       |
| Legal briefing, research, topic summary            | Route by topic (see Research Routing below)     |
| Compliance check, compliance verification          | Anthropic `/compliance-check`                   |
| Legal risk assessment                              | Anthropic `/legal-risk-assessment`              |
| Meeting preparation, briefing prep                 | Anthropic `/meeting-briefing`                   |
| Draft legal response                               | Anthropic `/legal-response`                     |
| E-signature, signature request                     | Anthropic `/signature-request`                  |

### Research Routing (replaces former /legal-brief command)

When the query is a research or briefing request, route by topic:

| Topic Pattern                     | Routes To                   |
| --------------------------------- | --------------------------- |
| Regulatory monitoring, compliance | regulatory-monitoring skill |
| Patent, trademark, IP, copyright  | ip-protection skill         |
| Legal spend, invoice, billing     | legal-spend skill           |
| DSAR, privacy, data subject       | dsar-privacy skill          |
| General research, legal topic     | Anthropic `/brief`          |

### Product Skills Reference

Each product is a standalone skill in `skills/<name>/SKILL.md`. The router
activates them by name -- Claude loads the skill's domain knowledge automatically.

| Skill                   | Domain                                                      |
| ----------------------- | ----------------------------------------------------------- |
| `ip-protection`         | Patent landscape, trademark monitoring, FTO, OSS compliance |
| `regulatory-monitoring` | Weekly regulatory briefing, impact classification           |
| `dsar-privacy`          | DSAR 30-day workflow, jurisdiction response windows         |
| `legal-spend`           | Spend analytics, anomaly detection, benchmarking            |
| `compliance-calendar`   | Obligation tracking, escalation sequences, dashboard        |

When the routing table directs you to a product skill, activate that skill
and apply its domain knowledge, output formats, and safety rules.

## STEP 2 -- IDENTIFY JURISDICTION AND LOAD OVERLAY

| Jurisdiction                  | Load Overlay File                                     |
| ----------------------------- | ----------------------------------------------------- |
| UK / English law              | references/jurisdictions/uk-law.md                    |
| EU / Continental Europe       | references/jurisdictions/eu-law.md                    |
| USA / US federal or state law | references/jurisdictions/us-law.md                    |
| Pakistan / Pakistani law      | references/jurisdictions/pakistan-law.md              |
| UAE / Dubai / DIFC / ADGM     | references/jurisdictions/uae-law.md                   |
| Saudi Arabia / KSA            | references/jurisdictions/gcc-law.md                   |
| Bahrain / CBB                 | references/jurisdictions/gcc-law.md                   |
| Kuwait                        | references/jurisdictions/gcc-law.md                   |
| Oman                          | references/jurisdictions/gcc-law.md                   |
| Qatar / QFC                   | references/jurisdictions/gcc-law.md                   |
| GCC / Gulf States             | references/jurisdictions/gcc-law.md                   |
| Multi-jurisdictional          | Load ALL relevant overlays + escalate to intl counsel |
| Unknown / not stated          | Flag; apply most conservative standard                |

## STEP 3 -- LOAD NEGOTIATION PLAYBOOK

CHECK for playbook in user's local settings (legal.local.md or configured file).

IF playbook FOUND:

- Load all clause positions, acceptable ranges, and escalation triggers
- Label output: "Reviewed against [Organisation] Negotiation Playbook v[X]"
- Pass playbook context to the destination skill/command

IF playbook NOT FOUND:

- Inform user: "No playbook configured. Reviewing against general commercial standards."
- Offer to help create a playbook (see legal.local.md.template)
- Label all output: "Reviewed against general commercial standards"

## STEP 4 -- NDA PRE-CHECKS (before handing to Anthropic /triage-nda)

When routing an NDA to Anthropic's `/triage-nda`, FIRST run these 9 automatic
RED flag checks. If ANY fire, classify as Tier 3 and include the flag in the
handoff context:

### 9 Automatic RED Flags (always Tier 3 regardless of playbook)

1. **Residuals clause**: allows use of information "retained in unaided memory"
2. **No carve-out for publicly available information**
3. **Non-compete provisions** of any scope
4. **Perpetual confidentiality obligations** (no sunset clause)
5. **Governing law**: jurisdiction with no established commercial law framework
6. **No definition of Confidential Information** (unacceptably broad)
7. **Unilateral NDA where mutual expected**, without documented business justification
8. **Injunctive relief provisions** asymmetric in favour of counterparty
9. **Disclosure to affiliates** without "need to know" qualification

When handing off to Anthropic `/triage-nda`:

- Include which RED flags fired (if any) in the context
- Include the jurisdiction overlay findings
- Include playbook context (if loaded)

## STEP 5 -- MANDATORY OUTPUT HEADER FORMAT

Every legal output produced by any skill or agent MUST begin with this block:

```
TASK:             [e.g. Contract Review -- Vendor MSA]
JURISDICTION:     [e.g. English Law]
PLAYBOOK:         [Loaded: legal.local.md / Not configured -- using general standards]
OVERLAY:          [Loaded: jurisdictions/uk-law.md / None]
ATTORNEY REVIEW:  REQUIRED -- all outputs must be reviewed by a licensed attorney
ESCALATION:       [Yes -- reason / No]
DATE:             [current date]
```

Do not produce any substantive legal output without this header.

## NEVER DO THESE

- NEVER route a query without identifying both the product type AND the jurisdiction
- NEVER skip the playbook check -- if no playbook found, state explicitly
- NEVER apply a jurisdiction overlay without confirming the user's jurisdiction
- NEVER provide legal advice directly -- route to the correct product/command which will produce analysis for attorney review
- NEVER route employment disputes to contract review -- these require specialist employment law advice
- NEVER route an NDA to Anthropic `/triage-nda` without running the 9 RED flag pre-checks first
- NEVER duplicate Anthropic's built-in commands -- route to them with enriched context

## UNIVERSAL RULES -- NON-NEGOTIABLE

- NEVER provide legal advice -- provide legal analysis; flag for attorney review
- NEVER approve a contract for execution -- human authorised signatory required
- NEVER skip a RED escalation -- RED always requires attorney review before proceeding
- NEVER omit playbook check -- if none found, state explicitly:
  "Reviewed against general commercial standards -- no playbook configured"
- NEVER send any legal output to a counterparty without attorney review first
- NEVER confirm data holdings in a DSAR acknowledgement before discovery is complete
- NEVER miss a response deadline -- alert counsel 7 days before any mandatory deadline
- NEVER apply legal interpretations across jurisdictions without the correct overlay

## AGENT ROLE STATEMENT

This agent: analyses, flags, drafts, routes.
The attorney: advises, decides, negotiates, signs.
These roles are distinct. Do not conflate them.

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
