---
name: audit
description: >
  Activate for: audit, audit preparation, audit pack, internal audit,
  external audit, regulatory audit, supervisory visit, audit evidence,
  audit trail, audit readiness, mock audit, audit findings, audit response,
  audit remediation, audit committee, board audit, annual audit, ISO audit,
  surveillance audit, certification audit, regulator visit, FCA visit,
  BSI audit, PCI audit, SOC 2 audit, audit questionnaire, evidence inventory.
  NOT for: compliance obligation mapping (use official compliance-tracking
  auto-skill), vendor evaluation (use official /vendor-review), risk
  register building (use official risk-assessment auto-skill).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/audit"
  mcp-integrations: "Compliance obligation map, document store, calendar"
---

## UNIVERSAL RULES (apply to every audit task)

- NEVER walk into an audit without an evidence inventory -- the audit
  that reveals you cannot locate your own evidence is harder to recover
  from than the audit that reveals a control gap
- NEVER respond to a finding by arguing with it -- acknowledge; explain
  root cause; state corrective action; provide timeline
- ALWAYS include specific recommended actions with deadlines in every
  output -- observations without actions are not acceptable
- ALWAYS load ops.local.md for organisation-specific regulatory frameworks,
  compliance evidence locations, and escalation contacts

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          [e.g. Audit Preparation -- ISO 27001 Surveillance]
AUDIT TYPE:    [Internal / External / Regulatory / Customer / Certification]
CONFIGURATION: [Loaded: ops.local.md / Not configured]
DATE:          [Date of output]
OWNER:         [Named person responsible]
REVIEW DATE:   [When to review/update]
```

## COMPLIANCE STATUS STANDARD

Apply to every obligation assessed during audit preparation:

```
🟢 CURRENT:        Control effective; evidence current; no gaps
🟡 REVIEW NEEDED:  Evidence aging; control not recently tested
🟡 PARTIAL:        Control exists but incomplete; evidence gaps
🔴 GAP:            No effective control; evidence absent; obligation unmet
🔴 URGENT:         Active breach risk; immediate action required
```

RULE: Never mark an obligation as CURRENT without evidence.
An obligation without evidence is, at best, PARTIAL.

## AUDIT WORKFLOW

### Task Type 1: PRE-AUDIT PREPARATION PLAN

For any audit with >4 weeks' notice, generate a preparation plan:

```
AUDIT PREPARATION PLAN: [Audit name / body]
================================================================
Audit type:      [Internal / External / Regulatory / Certification]
Auditor:         [Body name]
Date:            [Audit date or window]
Focus areas:     [What the auditor has indicated they will review]
Time to prepare: [Weeks]

WEEK-BY-WEEK PREPARATION TIMELINE:
[Week N]: [Actions -- evidence gathering; gap remediation]
[Week N]: [Actions -- document review; mock interviews]
[Final week]: [Actions -- final checks; logistics; briefings]

EVIDENCE INVENTORY (for each focus area):
| Obligation / Control | Evidence Required | Location | Age | Status |
|---|---|---|---|---|
| [Name] | [Document/record] | [Where stored] | [Date] | [Ready/Gap] |

GAPS TO CLOSE BEFORE AUDIT:
Priority 1 (close by [date -- 2 weeks before]):
  [Gap; action; owner]
Priority 2 (close by [date -- 1 week before]):
  [Gap; action; owner]

BRIEFING REQUIRED FOR:
[Who needs to be briefed; on what; by when]
================================================================
```

### Task Type 2: MOCK AUDIT / REVIEW

Simulate the auditor's approach before the real audit:

```
MOCK AUDIT: [Focus area]
----------------------------------------------------------------
Simulated auditor questions (by area):

Q: [Question as auditor would phrase it]
A: [Ideal answer]
Evidence: [What you would present]
Gap: [If the answer is weak or evidence incomplete]

[Repeat for each focus area question]
----------------------------------------------------------------
```

Generate 5-10 questions per focus area. Weight towards areas where
evidence is weakest (identified in the preparation plan).

### Task Type 3: AUDIT RESPONSE FRAMEWORK

When audit findings are received, generate structured responses:

FINDING CLASSIFICATION:

```
CRITICAL: Immediate regulatory action possible; fix within 30 days
MAJOR:    Significant control failure; fix within 60-90 days
MINOR:    Process improvement opportunity; fix within 6 months
OBSERVATION: No immediate action required; monitor
```

RESPONSE STRUCTURE (per finding):

```
AUDIT FINDING RESPONSE: [Finding reference]
----------------------------------------------------------------
Finding:             [Exact wording from auditor]
Classification:      [CRITICAL / MAJOR / MINOR / OBSERVATION]
Our response:        [Factual; acknowledge the finding]
Root cause:          [Why this gap existed]
Action taken/planned:[Specific; with dates]
Owner:               [Named person]
Target completion:   [Date]
Evidence of completion: [What we will provide when done]
----------------------------------------------------------------
```

RULE: Audit responses are read by regulators and auditors as evidence
of governance maturity. Defensive responses damage the relationship.
Specific, accountable, evidenced responses demonstrate maturity.

## AUDIT TYPES REFERENCE

INTERNAL AUDIT: Organisation's own audit function reviewing controls
EXTERNAL AUDIT: Third-party auditor (financial; certification body)
REGULATORY AUDIT: Regulator reviewing compliance (FCA; ICO; HMRC; HSE)
CUSTOMER AUDIT: Customer reviewing supplier controls
CERTIFICATION AUDIT: Certification body assessing against standard (ISO; PCI)

## NEVER DO THESE

- NEVER produce an evidence inventory with "TBD" or "unknown" locations --
  if the evidence location is unknown, that is a GAP; flag it as such
- NEVER brief only the team lead for an audit -- anyone who may be
  interviewed should understand the scope and their role
- NEVER leave a mock audit finding unresolved before the real audit --
  a mock finding that is not closed before the real audit is a real finding
- NEVER treat a MINOR finding as unimportant -- minor findings that
  repeat across multiple audits signal a systemic governance weakness
- NEVER produce an audit response without a named owner and specific date
- NEVER treat "standard terms" as automatically compliant -- verify each
  obligation against actual evidence

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
