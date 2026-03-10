---
name: crm-enrichment
description: >
  Activate for: enrich, CRM enrichment, update CRM, data enrichment,
  stale data, missing data, contact data, company data, verify email,
  verify contact, update record, data hygiene, CRM cleanup, enrich leads,
  refresh accounts, outdated records, data quality.
  NOT for: prospect research briefs (use prospect-research), lead scoring (use lead-scoring), bulk automated enrichment scheduling (use crm-hygiene-agent), pipeline analysis (use pipeline).
---

## ENRICHMENT WORKFLOW

### Scope Definition

Before enriching, confirm scope:

- Single contact or account (on-demand)
- Segment (e.g. all Tier 1 accounts with no activity >60 days)
- Full pipeline (monthly refresh)
- All HOT/WARM leads (weekly refresh)
- Trigger-based (new website visit, new content download)

### Contact-Level Enrichment Fields

For each contact record, verify and update:

MANDATORY FIELDS:
Full name: Verify spelling against LinkedIn
Current title: Update if changed; flag role change for re-routing
Current company: Update if changed; trigger re-scoring if new company
Work email: Verify deliverability; update if bouncing
Direct phone: Verify if present; add if findable
LinkedIn URL: Add if missing

INTELLIGENCE FIELDS:
Time in current role: Calculate from LinkedIn start date
Recent public activity: Posts, articles, quotes (last 30 days)
New pain signals: Any new posts or interviews about your problem area
Career change flag: Has this person changed jobs since last enrichment?

### Account-Level Enrichment Fields

For each company record:

MANDATORY FIELDS:
Legal company name: Verify against Companies House / equivalent
Revenue estimate: Update from latest public sources (label: estimated)
Headcount: Current LinkedIn company page; flag >20% change
Headquarters: Verify current registered address
Website: Verify current; update if changed

INTELLIGENCE FIELDS:
News events (last 30 days): Funding, contracts, M&A, leadership changes
Hiring signal: New job postings in target departments (last 30 days)
Tech stack changes: New tools or dropped tools visible in job postings
Financial signals: Revenue growth/decline indicators
Timing signal refresh: Re-classify HOT / WARM / WATCH

### Enrichment Schedule (configure in local settings)

HOT leads: Weekly enrichment + immediate alert if new signal
Tier 1 accounts: Monthly full enrichment
Tier 2 accounts: Quarterly enrichment
All active pipeline: Monthly enrichment
Trigger-based: Within 24 hours of website visit or content download

### Enrichment Output Format

# CRM ENRICHMENT REPORT -- [Date]

Scope: [Description of records enriched]
Total: [N] records processed

CHANGES MADE:
[Company / Contact] -- [Field updated: old value -> new value]

ROLE CHANGES DETECTED (require re-routing):
[Contact name] -- changed from [old role] at [company] to
[new role] at [new company] -- CRM record flagged for rep review

NEW HOT SIGNALS IDENTIFIED:
[Company]: [Signal description] -- [source] -- Score updated [X -> Y]
Action: [Rep name] to be alerted; /research brief recommended

RECORDS WITH MISSING MANDATORY FIELDS:
[N] records still missing: [field list] -- manual review required

# DATA QUALITY SCORE: [X]% of enriched records now complete

## NEVER DO THESE

- NEVER overwrite a manually entered field without flagging the change
  to the record owner (human-entered data may be more current than web data)
- NEVER mark an email as "verified" without actually checking deliverability
- NEVER assume a contact is still at a company if LinkedIn shows no
  updates in >12 months -- flag for manual verification
- NEVER enrich and update a record that is in an active deal stage
  without notifying the assigned rep -- timing of data changes matters
- NEVER remove a contact from a sequence because their email changed --
  pause the sequence and alert the rep to verify new contact details first
