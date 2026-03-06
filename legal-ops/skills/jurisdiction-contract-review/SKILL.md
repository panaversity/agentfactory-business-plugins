---
name: jurisdiction-contract-review
version: 1.0
description: >
  Activate for: contract review, clause analysis, redline, vendor agreement,
  MSA, master services agreement, SOW, statement of work, SaaS agreement,
  software licence, professional services agreement, partnership agreement,
  supply agreement, distribution agreement, review contract, full NDA review
  (use jurisdiction-nda-triage for quick triage only).
  NOT for: NDA-only triage (use jurisdiction-nda-triage), IP research, regulatory monitoring, DSAR processing, general legal advice, litigation strategy.
plugin-commands: /review-contract
chapter: 22 -- Legal Operations and Compliance
---

## REVIEW WORKFLOW -- EXECUTE IN ORDER

### Phase 1: Context Gathering (before reading the contract)

Ask the user:

1. Which party are you? (Customer / Vendor / Licensor / Licensee / Partner / Other)
2. What is the contract type? (SaaS / Professional Services / Licence / Partnership / Other)
3. When does this need to be finalised?
4. Approximate contract value?
5. Any specific clauses of concern?
6. Relevant business context (new vs. strategic vs. commodity vendor)?

### Phase 2: Playbook Loading

CHECK for playbook in user's local settings (legal.local.md or configured file).

IF playbook FOUND:

- Load all clause positions, acceptable ranges, and escalation triggers
- Label output: "Reviewed against [Organisation] Negotiation Playbook v[X]"

IF playbook NOT FOUND:

- Inform user: "No playbook configured. Reviewing against general commercial standards."
- Offer to help create a playbook (see legal.local.md.template)
- Label all output: "Reviewed against general commercial standards"

### Phase 3: Full Contract Read

READ THE ENTIRE CONTRACT before flagging any issues.
Reason: Clauses interact. An uncapped indemnity may be partially offset by a broad
limitation of liability. Review holistically, not clause-by-clause in isolation.

Identify:

- Contract type (confirm or update from context phase)
- User's side (confirm from context)
- Governing law and jurisdiction
- Material clauses present / absent
- Unusual structure or atypical provisions

### Phase 4: Clause-by-Clause Analysis

ANALYSE each material clause against playbook (or general standards).

PRIORITY CLAUSES (always analyse):

1.  Limitation of liability -- cap amount, mutual/asymmetric, carve-outs
2.  Intellectual property -- ownership, work product, licence-back
3.  Indemnification -- scope, triggers, caps, mutual/one-sided
4.  Data protection -- DPA requirement, transfer mechanisms, breach notification
5.  Termination -- for convenience, for cause, notice periods, consequences
6.  Governing law and jurisdiction -- choice of law, dispute resolution
7.  Confidentiality -- scope, duration, carve-outs
8.  Payment and pricing -- fixed/variable, invoicing, late payment
9.  Warranties and representations -- scope, disclaimers
10. Force majeure -- scope, notification, relief

SECONDARY CLAUSES (analyse if present):

- Non-compete / non-solicitation
- Audit rights
- Assignment and change of control
- Insurance requirements
- SLA and service credits
- Auto-renewal provisions

### Phase 5: Three-Tier Flag Classification

Classify every deviation from playbook (or general standard):

GREEN -- ACCEPTABLE
Within standard position or acceptable range.
No action required. Note for completeness.

YELLOW -- NEGOTIATE
Outside standard position but within acceptable range.
Action: Provide primary redline + fallback position.

RED -- ESCALATE
Outside acceptable range. Potential material risk.
Action: Flag for attorney review. Do not proceed without legal sign-off.

### Phase 6: Redline Generation Format

For each YELLOW and RED item:

CLAUSE: [Clause name and section number]
STATUS: [YELLOW / RED]
CURRENT: "[Exact current contract text]"
ISSUE: [Specific problem and why it matters]
REDLINE: "[Exact proposed replacement text -- ready to insert]"
FALLBACK: [If YELLOW: fallback position if primary ask is rejected]
RATIONALE: "[Professional rationale suitable for sharing with counterparty's counsel]"
PRIORITY: [Must-have / Nice-to-have]

### Phase 7: Holistic Risk Summary

Conclude with:

- Total: [N] GREEN | [N] YELLOW | [N] RED
- Single most material risk in this contract
- Overall recommendation: Approve / Negotiate / Escalate to counsel / Decline
- Suggested negotiation priority order (most important first)

## OUTPUT FORMAT

### Redline Output (per YELLOW / RED clause)

```
CLAUSE: [Clause name and section number]
STATUS: [YELLOW / RED]
CURRENT: "[Exact current contract text]"
ISSUE: [Specific problem and why it matters]
REDLINE: "[Exact proposed replacement text -- ready to insert]"
FALLBACK: [If YELLOW: fallback position if primary ask is rejected]
RATIONALE: "[Professional rationale suitable for sharing with counterparty's counsel]"
PRIORITY: [Must-have / Nice-to-have]
```

### Holistic Risk Summary Output

```
CONTRACT REVIEW SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract: [Type -- Counterparty]
Governing Law: [jurisdiction]
Playbook: [Loaded / General standards]
Reviewed by: Legal Ops Agent

CLAUSE ANALYSIS: [N] GREEN | [N] YELLOW | [N] RED

MOST MATERIAL RISK:
[description of the single most significant risk]

RECOMMENDATION: [Approve / Negotiate / Escalate to counsel / Decline]

NEGOTIATION PRIORITY ORDER:
1. [highest priority item]
2. [next priority]
3. [...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
```

## NEVER DO THESE

- NEVER approve a contract for execution -- route for authorised signatory
- NEVER skip Phase 1 context gathering -- user's position changes the entire analysis
- NEVER flag an issue without a specific proposed remedy
- NEVER read clauses in isolation without considering the full contract
- NEVER send redlines to counterparty -- attorney review required first
- NEVER classify a liability carve-out for death/personal injury from negligence
  as GREEN -- void under English law (UCTA s.2(1)); RED regardless of playbook

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
