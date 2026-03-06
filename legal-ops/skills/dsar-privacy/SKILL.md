---
name: dsar-privacy
version: 1.0
description: >
  Activate for: DSAR, data subject access request, subject access request,
  SAR, right of access, Article 15, GDPR request, CCPA request, privacy
  request, right to be forgotten, erasure request, Article 17, data
  portability, Article 20, data rectification, Article 16, restriction of
  processing, Article 18, objection to processing, Article 21, data subject
  rights, privacy inquiry, ICO complaint, privacy response.
  NOT for: contract review, NDA triage, IP matters, regulatory monitoring, legal advice on data protection interpretation, erasure execution.
plugin-commands: /legal-brief
chapter: 22 -- Legal Operations and Compliance
---

## JURISDICTION RESPONSE WINDOWS

| Jurisdiction      | Window       | Regulator    | Extension                       |
| ----------------- | ------------ | ------------ | ------------------------------- |
| UK GDPR           | 30 cal. days | ICO          | +60 days if complex (w/ notice) |
| EU GDPR           | 30 cal. days | National DPA | +60 days if complex (w/ notice) |
| CCPA (California) | 45 days      | CA AG        | +45 days with notice            |
| PIPEDA (Canada)   | 30 days      | OPC          | Escalate to Privacy Officer     |
| Other             | Escalate now | --           | Confirm with Privacy Counsel    |

## REQUEST TYPE ROUTING

| Request Type                         | Action                                  |
| ------------------------------------ | --------------------------------------- |
| Subject Access (Art. 15 / CCPA)      | Full data discovery workflow (below)    |
| Erasure / Right to be Forgotten (17) | IMMEDIATE escalation to Privacy Counsel |
| Data Portability (Art. 20)           | IT lead + Privacy Counsel               |
| Rectification (Art. 16)              | Relevant system owner + confirmation    |
| Restriction of Processing (Art. 18)  | Privacy Counsel immediately             |
| Objection to Processing (Art. 21)    | Privacy Counsel immediately             |
| Related ICO/DPA complaint            | GC immediately                          |

## SUBJECT ACCESS REQUEST -- FULL WORKFLOW

### Stage 1: Receipt and Acknowledgement (Day 1)

ACKNOWLEDGE THE SAME DAY. Acknowledgement MUST include:

- Confirmation of receipt
- The statutory response deadline (Day 30)
- Identity verification requirements (if identity is in doubt)
- Contact details for queries

Acknowledgement MUST NOT include:

- Confirmation or denial of what data is held
- Any substantive response to the request
- Legal advice of any kind

### Stage 2: Identity Verification (Days 1-3)

If requester identity is in doubt:

- Request reasonable proof of identity
- Do NOT request excessive documentation
- The 30-day clock pauses while awaiting verification
- If identity cannot be verified -> consult Privacy Counsel before refusing

### Stage 3: Data Discovery (Days 1-10)

Send discovery requests to ALL relevant system owners:

- CRM / customer database
- Email and communications systems
- Billing and financial systems
- Marketing and analytics platforms
- HR system (if individual was ever an employee)
- Customer support / ticketing systems
- Legal case management (handle with care -- privilege issues)
- Any legacy or archive systems

Discovery deadline: Day 10
Alert: if discovery not complete by Day 15 -> escalate to Privacy Counsel.

### Stage 4: Data Compilation and Redaction Assessment (Days 10-20)

REDACT (do not disclose):

- Third-party personal data (other individuals mentioned in records)
- Internal staff personal data (beyond names in standard business capacity)
- Legally privileged material (obtain counsel advice before withholding)
- Commercially sensitive information genuinely unrelated to the requester

DO NOT REDACT:

- Opinions ABOUT the requester -- these ARE personal data (Art. 4(1))
- Internal notes about the requester's behaviour or interactions
- Automated decision-making logic applied to the requester

COMMON ERROR: CRM/sales notes containing opinions about the requester
(e.g. "difficult customer", "pushes for discounts") ARE personal data
and MUST be disclosed unless a specific exemption applies.
Consult Privacy Counsel if in doubt about any redaction decision.

### Stage 5: Response Drafting (Days 20-27)

Response letter MUST include:

- Confirmation of personal data held (by category)
- Purposes of processing
- Legal basis for each processing activity
- Recipients or categories of recipients
- Retention periods (or criteria used to determine them)
- Rights: rectification, erasure, restriction, objection, portability,
  lodge a complaint with the supervisory authority
- Source of data (if not collected directly from the requester)
- Existence of any automated decision-making / profiling

ROUTE for attorney review on Day 27 at the latest.
DO NOT send to requester without attorney sign-off.

### Stage 6: Response and Logging (Day 30)

Send approved response. Log:

- Date received / Date acknowledged / Date responded
- Data categories disclosed
- Any data withheld and legal basis for withholding
- Attorney sign-off confirmation
- Store in compliance archive

## OUTPUT FORMATS

### Stage 1: Acknowledgement Letter Format

```
DSAR ACKNOWLEDGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference: [DSAR-YYYY-MM-DD-XXXX]
Date received: [date]
Requester: [name]
Request type: [Access / Erasure / Portability / Rectification / Other]

Dear [Requester],

We acknowledge receipt of your data subject access request dated [date].

Statutory response deadline: [calculated date -- 30 days UK/EU, 45 days CCPA]
Identity verification: [Required -- please provide X / Confirmed]
Contact for queries: [privacy team email]

We will respond within the statutory timeframe. If we require an extension,
we will notify you with reasons before the deadline.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Stage 3: Data Discovery Request Format

```
INTERNAL DATA DISCOVERY REQUEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DSAR Reference: [DSAR-YYYY-MM-DD-XXXX]
Requester: [name / identifier]
Discovery deadline: Day 10 ([date])
Escalation date: Day 15 ([date]) -- if incomplete, escalate to Privacy Counsel

SYSTEMS TO SEARCH:
[ ] CRM / customer database
[ ] Email and communications systems
[ ] Billing and financial systems
[ ] Marketing and analytics platforms
[ ] HR system (if applicable)
[ ] Customer support / ticketing
[ ] Legal case management (privilege review required)
[ ] Legacy / archive systems

Please return all personal data relating to [requester identifier] by [deadline].
Flag any records that may be subject to legal privilege or third-party data.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Stage 5: Response Letter Format

```
DSAR RESPONSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference: [DSAR-YYYY-MM-DD-XXXX]
Date received: [date]
Response date: [date]
Jurisdiction: [UK GDPR / EU GDPR / CCPA / Other]

Dear [Requester],

In response to your data subject access request, we confirm the following:

PERSONAL DATA HELD (by category):
- [Category]: [description of data held]

PURPOSES OF PROCESSING:
- [Purpose]: [legal basis]

RECIPIENTS / CATEGORIES OF RECIPIENTS:
- [Recipient category]

RETENTION PERIODS:
- [Category]: [period or criteria]

YOUR RIGHTS:
- Rectification, erasure, restriction, objection, portability
- Right to lodge a complaint with [supervisory authority]

SOURCE OF DATA: [collected directly / obtained from third party]

AUTOMATED DECISION-MAKING: [Yes -- details / None identified]

DATA WITHHELD: [None / Details of data withheld with legal basis]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
```

## ESCALATION RULES

- 7 days before deadline: Alert Privacy Counsel if response not substantially complete
- 1 day before deadline: Emergency alert -- GC involved if not resolved
- Any erasure/restriction/objection: Privacy Counsel immediately
- Legally privileged material involved: Privacy Counsel immediately
- Identity fraud suspected: Privacy Counsel immediately
- Related regulatory inquiry: GC immediately

## NEVER DO THESE

- NEVER confirm data holdings before discovery is complete
- NEVER send data to requester without attorney review of full response
- NEVER miss the response window -- UK GDPR fines up to 17.5M GBP or 4% of global turnover
- NEVER reject a request without attorney sign-off on rejection grounds
- NEVER apply a fee without attorney confirmation it is lawful
- NEVER confuse an SAR with a Freedom of Information request
  (FOI is for public bodies only)

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
