# Workflow Recipe: DSAR 30-Day Response

## Task Overview

| Field         | Value                                                                           |
| ------------- | ------------------------------------------------------------------------------- |
| **Task Name** | DSAR Response: Receipt through Completion within 30-Day Statutory Window        |
| **Frequency** | Per request (triggered by each incoming DSAR)                                   |
| **Purpose**   | Manage data subject access requests end-to-end within mandatory response window |
| **Owner**     | Privacy Officer / Data Protection Officer                                       |

---

## Response Windows by Jurisdiction

| Jurisdiction | Window       | Extension                       | Regulator    |
| ------------ | ------------ | ------------------------------- | ------------ |
| UK GDPR      | 30 cal. days | +60 days if complex (w/ notice) | ICO          |
| EU GDPR      | 30 cal. days | +60 days if complex (w/ notice) | National DPA |
| CCPA         | 45 days      | +45 days with notice            | CA AG        |
| PIPEDA       | 30 days      | Escalate to Privacy Officer     | OPC          |

---

## Step-by-Step Execution

### Day 1: Receipt and Acknowledgement

```
Input: DSAR received (email, portal, letter)
Actions:
  - Log request: requester name, contact, date, request type, jurisdiction
  - Start response clock
  - Set internal alerts: Day 7, Day 15, Day 21, Day 27
  - Draft and send acknowledgement letter

Acknowledgement MUST include:
  - Confirmation of receipt
  - Statutory response deadline
  - Identity verification requirements (if needed)
  - Contact details for queries

Acknowledgement MUST NOT include:
  - Confirmation or denial of what data is held
  - Any substantive response
  - Legal advice
```

### Days 1-3: Identity Verification

```
IF requester identity is in doubt:
  - Request reasonable proof of identity
  - Do NOT request excessive documentation
  - 30-day clock pauses while awaiting verification
  - If unverifiable -> consult Privacy Counsel before refusing

IF identity verified:
  - Log verification and proceed
```

### Days 1-10: Data Discovery

```
Send discovery requests to ALL relevant system owners:
  - CRM / customer database
  - Email and communications systems
  - Billing and financial systems
  - Marketing and analytics platforms
  - HR system (if individual was ever employee)
  - Customer support / ticketing systems
  - Legal case management (handle with care -- privilege)
  - Legacy or archive systems

Discovery deadline: Day 10
IF NOT complete by Day 15: escalate to Privacy Counsel
```

### Days 10-20: Compilation and Redaction Assessment

```
REDACT (do not disclose):
  - Third-party personal data
  - Internal staff personal data (beyond standard business capacity)
  - Legally privileged material (counsel advice required)
  - Commercially sensitive info genuinely unrelated to requester

DO NOT REDACT:
  - Opinions ABOUT the requester (these ARE personal data)
  - Internal notes about requester's behaviour
  - Automated decision-making logic applied to requester

COMMON ERROR: CRM notes like "difficult customer" ARE personal data
and MUST be disclosed unless a specific exemption applies.
```

### Days 20-27: Response Drafting

```
Response letter MUST include:
  - Confirmation of personal data held (by category)
  - Purposes of processing
  - Legal basis for each processing activity
  - Recipients or categories of recipients
  - Retention periods
  - Rights: rectification, erasure, restriction, objection, portability,
    lodge complaint with supervisory authority
  - Source of data (if not collected from requester)
  - Automated decision-making / profiling information

Route for attorney review by Day 27 at latest.
DO NOT send without attorney sign-off.
```

### Day 30: Response and Logging

```
Send approved response. Log:
  - Date received / Date acknowledged / Date responded
  - Data categories disclosed
  - Data withheld and legal basis
  - Attorney sign-off confirmation
  - Store in compliance archive
```

---

## Escalation Rules

| Trigger                       | Action                                | Deadline  |
| ----------------------------- | ------------------------------------- | --------- |
| 7 days before deadline        | Alert Privacy Counsel if not complete | Day 23    |
| 1 day before deadline         | Emergency alert -- GC involved        | Day 29    |
| Erasure/restriction/objection | Privacy Counsel immediately           | Day 1     |
| Privileged material involved  | Privacy Counsel immediately           | Day 10-20 |
| Identity fraud suspected      | Privacy Counsel immediately           | Day 1-3   |
| Related regulatory inquiry    | GC immediately                        | Any day   |

---

## Required Skill Files

| Skill File            | Purpose                                         |
| --------------------- | ----------------------------------------------- |
| `dsar-privacy`        | Full DSAR workflow and request type routing     |
| `legal-global-router` | Jurisdiction identification and overlay loading |
| UK/EU/US overlays     | Jurisdiction-specific response requirements     |

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
