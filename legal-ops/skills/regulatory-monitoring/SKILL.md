---
name: regulatory-monitoring
version: 1.0
description: >
  Activate for: regulatory update, regulation change, new law, compliance
  monitoring, regulatory briefing, regulatory calendar, law change, legal
  development, regulatory risk, ICO guidance, FCA update, GDPR update,
  EU AI Act, employment law change, company law update, sector regulation,
  regulatory horizon, compliance alert, policy review, board briefing.
  NOT for: contract review, NDA triage, IP research, DSAR processing, legal advice on regulatory interpretation.
plugin-commands: /legal-brief
chapter: 22 -- Legal Operations and Compliance
---

## CONFIGURATION PARAMETERS (load from settings or ask user)

Required:

- Organisation type: [industry, size, structure]
- Primary regulatory areas: [list all that apply]
- Key jurisdictions: [all jurisdictions where the org operates]
- Escalation contacts: [Compliance Officer, GC, relevant leads]
- Output format: [weekly brief / monthly board summary / ad-hoc alert]

Standard regulatory areas to monitor (configure for relevance):

- Data Protection: UK GDPR, EU GDPR, CCPA, PIPEDA, ICO guidance
- AI Regulation: EU AI Act (implementation phases), UK AI framework,
  OECD AI Principles, sector AI guidance (FCA, ICO)
- Employment: Working time, remote working, IR35/contractor status,
  whistleblowing, TUPE, redundancy
- Company Law: Annual return, director duties, PSC register,
  anti-bribery (UKBA), corporate criminal offences
- Financial Services (if applicable): FCA rules, PRA requirements
- Sector-specific: [configure for organisation's industry]

## IMPACT CLASSIFICATION

HIGH PRIORITY (RED): Effective within 30 days; OR requires immediate policy change;
OR potential enforcement risk.

MONITOR (YELLOW): Effective within 6 months; OR affects current contracts on renewal;
OR requires internal process change.

AWARENESS (GREEN): Longer horizon; informational only; no immediate action required.

## OUTPUT: WEEKLY MONITORING BRIEF

WEEKLY REGULATORY BRIEFING -- [Date]
Generated: Legal Ops Monitoring Agent
========================================================

RED -- HIGH PRIORITY -- Action required within 30 days

---

[Regulation name] -- [Jurisdiction]
Effective: [Date]
Summary: [2 sentences]
Internal impact: [Which policy/process needs updating]
Contract impact: [N contracts with relevant clauses -- see list]
Action: [Specific action] by [date] -- Owner: [name]

YELLOW -- MONITOR -- No immediate action; review within 6 months

---

[...]

GREEN -- AWARENESS -- For information only

---

[...]

========================================================
NOTE: All regulatory interpretations must be confirmed with
qualified legal counsel before reliance.

## OUTPUT: MONTHLY BOARD SUMMARY

```
MONTHLY REGULATORY BOARD SUMMARY -- [Month Year]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prepared: [date]
Period: [month]

EXECUTIVE SUMMARY:
1. [Most important regulatory change this month]
2. [Second most important]
3. [Third]

RAG STATUS BY REGULATORY AREA:
| Area              | Status  | Key Development          | Action Required |
| ----------------- | ------- | ------------------------ | --------------- |
| Data Protection   | [R/A/G] | [summary]                | [Y/N -- detail] |
| AI Regulation     | [R/A/G] | [summary]                | [Y/N -- detail] |
| Employment        | [R/A/G] | [summary]                | [Y/N -- detail] |
| Company Law       | [R/A/G] | [summary]                | [Y/N -- detail] |
| Sector-specific   | [R/A/G] | [summary]                | [Y/N -- detail] |

ACTIONS REQUIRED:
| Owner       | Action                    | Deadline   | Priority |
| ----------- | ------------------------- | ---------- | -------- |
| [name/role] | [specific action]         | [date]     | [R/Y/G]  |

HORIZON ITEMS (next 3-6 months):
- [Upcoming regulation]: effective [date] -- preparation required by [date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
```

## SOURCE CONFIGURATION

Configure regulatory sources per jurisdiction:

| Jurisdiction | Primary Sources                                       |
| ------------ | ----------------------------------------------------- |
| UK           | legislation.gov.uk, ICO, FCA, Companies House, GOV.UK |
| EU           | EUR-Lex, EDPB, ESMA, EC official journal              |
| US           | Federal Register, state legislature sites, FTC, SEC   |
| UAE          | WAM, DIFC, ADGM, UAE Official Gazette                 |
| Pakistan     | SECP, FBR, National Assembly, Pakistan Gazette        |
| GCC          | GCC official gazette, national regulatory authorities |

Source update frequency:

- RED items: check daily during implementation period
- YELLOW items: check weekly
- GREEN items: check monthly
- New jurisdiction added: verify source list with local counsel before relying

## NEVER DO THESE

- NEVER characterise monitoring output as legal advice
- NEVER state "you are compliant" -- flag for counsel to confirm
- NEVER miss an effective date -- build in 30-day advance warning
  for all HIGH PRIORITY items
- NEVER monitor a jurisdiction without loading the correct overlay file

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
