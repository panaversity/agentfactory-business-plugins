---
name: ip-protection
version: 1.0
description: >
  Activate for: patent, patent search, patent landscape, freedom to operate,
  FTO, prior art, trademark, trade mark, brand protection, trademark watch,
  trademark monitoring, copyright, DMCA, open source, OSS licence, trade
  secret, IP audit, IP protection, IP ownership, IP clause, IP indemnity,
  patent infringement, trademark infringement, copyright infringement,
  IP portfolio, IP monitoring, competitor patent, patent filing.
  NOT for: contract review, NDA triage, regulatory monitoring, DSAR processing, patent filing (attorney required), trademark registration.
plugin-commands: /legal-brief
chapter: 22 -- Legal Operations and Compliance
---

## IP TASK CLASSIFICATION

### Task 1: Patent Landscape Analysis

Use when: assessing technology landscape before product launch, investment
decision, or patent filing strategy.

Prompt structure:
/legal-brief topic:"patent landscape analysis"
subject:"[technology description]"
key-competitors:"[named entities]"
scope:"[date range]"
jurisdictions:"[US, EU, UK, etc.]"

Output includes:

- Key patent holders in the technology area
- Filing trends and white spaces
- Potentially relevant patents (for FTO flags)
- Prior art candidates
- Competitor activity summary

MANDATORY GOVERNANCE NOTE:
This output is a RESEARCH SUMMARY, not a freedom-to-operate opinion.
A qualified IP attorney must review before any product launch or investment
decision that relies on FTO assumptions.

### Task 2: Freedom-to-Operate (FTO) Preliminary Assessment

Use when: preparing research scaffolding for IP attorney to assess FTO.

Output structure:

- Our technology description (user-provided)
- Potentially relevant patents identified
- Claim mapping: which claims may read on our technology (preliminary only)
- Risk assessment: HIGH / MEDIUM / LOW (preliminary only)
- Recommended attorney actions

MANDATORY GOVERNANCE NOTE:
This output is preliminary research scaffolding ONLY.
It is NOT an FTO opinion. FTO opinions are privileged legal documents
signed by qualified IP counsel. Never rely on agent output alone
for a product launch decision.

### Task 3: Trademark Monitoring

Use when: monitoring for infringement of registered or pending marks.

Prompt structure:
/legal-brief topic:"trademark monitoring"
mark:"[your mark]"
class:"[Nice classification]"
jurisdiction:"[jurisdictions]"

Monitoring dimensions:

- Phonetic similarity (sounds like the mark)
- Visual similarity (looks like the mark in standard characters)
- Conceptual similarity (means the same thing in the relevant market)
- Domain name registrations incorporating the mark
- Social media handle registrations

Output:

- New applications in the monitoring period
- Similarity assessment per hit
- Recommended action: Oppose / Watch / No action
- ESCALATION: applications with >70% similarity -> attorney review

### Task 4: Copyright and OSS Compliance

OSS licence hierarchy (most to least restrictive):

- GPL v3 / AGPL: copyleft -- combined work must be GPL-licensed
- GPL v2: copyleft -- combined works must be GPL v2
- LGPL: weak copyleft -- dynamic linking generally permissible
- MPL: file-level copyleft
- Apache 2.0 / MIT / BSD: permissive -- commercial use generally permissible

ESCALATION TRIGGER: Any GPL/AGPL component in a proprietary product
-> escalate to IP counsel immediately.

### Task 5: IP Clause Review (within contracts)

Always check:

1. Who owns work product created during the engagement?
   RED FLAG: Vendor claims ownership of deliverables created using our data,
   our systems, or our specifications.

2. What licence does each party get to the other's IP?
   Check: scope, exclusivity, sublicensing, term, geography, termination consequences.

3. Are there obligations to assign IP to the other party?
   RED FLAG: Broad assignment clauses capturing pre-existing IP or improvements.

4. What IP indemnity is provided?
   STANDARD: Mutual indemnification for third-party IP infringement.
   RED FLAG: One-sided indemnity; no indemnity in a technology contract.

## OUTPUT FORMAT

```
IP RESEARCH BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: [Patent Landscape / Trademark Monitor / FTO Research]
Technology: [technology area]
Jurisdictions: [list]
Period: [date range]

FINDINGS:
[numbered list of key findings with relevance assessment]

RECOMMENDED ACTIONS:
[numbered list -- each marked: Immediate / Within 30 days / Monitor]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NOTE: This is research scaffolding, not a freedom-to-operate
opinion. All findings require review by qualified IP counsel.
```

## NEVER DO THESE

- NEVER characterise a patent landscape output as an FTO opinion
- NEVER advise a product launch is clear based on agent research alone
- NEVER proceed with GPL/AGPL OSS in a proprietary product without IP counsel
- NEVER miss the IP ownership clause in professional services agreements

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
