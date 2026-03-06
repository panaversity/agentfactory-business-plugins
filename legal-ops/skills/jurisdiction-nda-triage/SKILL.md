---
name: jurisdiction-nda-triage
version: 1.0
description: >
  Activate for: NDA, non-disclosure agreement, confidentiality agreement,
  mutual NDA, unilateral NDA, mutual CA, MCA, CDA, triage NDA, review NDA,
  incoming NDA, NDA received, sign NDA, NDA approval, quick NDA check.
  NOT for: full contract review (use jurisdiction-contract-review), IP matters, regulatory monitoring, DSAR processing, employment agreements.
plugin-commands: /triage-nda
chapter: 22 -- Legal Operations and Compliance
---

## TRIAGE WORKFLOW

### Phase 1: Context

Ask before reviewing:

1. Mutual (both parties disclose) or unilateral (one party discloses)?
   If unilateral: which party is the discloser?
2. Purpose: vendor evaluation / partnership / M&A / employment / other?
3. Counterparty type: new vendor / strategic partner / large enterprise / individual?
4. Urgency / deadline?
5. Any known concerns?

### Phase 2: Standard Form Loading

CHECK for NDA configuration in legal.local.md.

IF NDA configuration FOUND:

- Load standard form reference; Tier 1/2/3 criteria
- Compare incoming NDA against standard form directly

IF NOT FOUND:

- Apply general commercial NDA standards
- Label: "Reviewed against general commercial NDA standards"

### Phase 3: Three-Tier Routing Classification

TIER 1 -- STANDARD APPROVAL (no attorney review required)
Criteria: NDA substantially identical to standard form, OR deviations
fall within pre-approved acceptable ranges (defined in playbook).
Action: Notify business unit -- proceed to authorised signatory.
Target: 60-70% of incoming NDAs.

TIER 2 -- COUNSEL REVIEW (attorney review; no negotiation expected)
Criteria: Deviations within acceptable range requiring attorney confirmation.
Action: Route to reviewing attorney with triage summary attached.
Target: 20-30%.

TIER 3 -- FULL REVIEW (attorney review + likely negotiation)
Criteria: RED deviations present. Unusual structure. High-risk provisions.
Action: Route to senior counsel / GC with full risk summary.
Target: 10-15%.

### Phase 4: Triage Report Format

NDA TRIAGE REPORT

---

Counterparty: [Name]
Date: [Date]
Playbook: [Loaded / Not configured]

TRIAGE TIER: [1 / 2 / 3] -- [Label]
Attorney time: [0 / ~15 min / ~45 min]

SUMMARY: [N] GREEN | [N] YELLOW | [N] RED
RECOMMENDATION: [Route to / Approve for execution]

DEVIATIONS FROM STANDARD:
GREEN [Clause]: [deviation] -- [classification and reason]
YELLOW [Clause]: [deviation] -- [flag and proposed position]
RED [Clause]: [deviation] -- [RED reason and escalation note]

---

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY

## AUTOMATIC RED FLAGS (always Tier 3 regardless of playbook)

- Residuals clause: allows use of information "retained in unaided memory"
- No carve-out for publicly available information
- Non-compete provisions of any scope
- Perpetual confidentiality obligations (no sunset clause)
- Governing law: jurisdiction with no established commercial law framework
- No definition of Confidential Information (unacceptably broad)
- Unilateral NDA where mutual expected, without documented business justification
- Injunctive relief provisions asymmetric in favour of counterparty
- Disclosure to affiliates without "need to know" qualification

## NEVER DO THESE

- NEVER route a Tier 3 NDA to Tier 1 regardless of business urgency
- NEVER approve execution without an authorised signatory
- NEVER omit the residuals clause check -- most commonly missed high-risk provision
- NEVER classify an NDA as Tier 1 if governing law differs from standard
  without attorney confirmation

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
