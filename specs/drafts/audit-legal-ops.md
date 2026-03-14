## Legal Ops Compliance Report

### Summary
- Total skills audited: 6
- Total agents audited: 1
- Total violations found: 3
- Critical (invalid fields): 3
- Warning (best practice): 0

---

### Violations

#### legal-ops/skills/legal-global-router/SKILL.md
- [ ] VIOLATION S20: `version: 3.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "3.0"`
- [ ] VIOLATION S21: `author: Panaversity -- The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity -- The AI Agent Factory"`
- [ ] VIOLATION S27: `chapter: 22 -- Legal Operations and Compliance` is not a recognised SKILL.md field (not listed in S1–S19)
  - FIX: Move to `metadata:` block → `metadata:\n  chapter: "22 -- Legal Operations and Compliance"` OR remove if not needed

#### legal-ops/skills/compliance-calendar/SKILL.md
- No violations found.

#### legal-ops/skills/dsar-privacy/SKILL.md
- No violations found.

#### legal-ops/skills/ip-protection/SKILL.md
- No violations found.

#### legal-ops/skills/legal-spend/SKILL.md
- No violations found.

#### legal-ops/skills/regulatory-monitoring/SKILL.md
- No violations found.

#### legal-ops/agents/contract-intake.md
- No violations found.

#### legal-ops/.claude-plugin/plugin.json
- No violations found.

---

### Proposed Fixed Frontmatter

#### legal-ops/skills/legal-global-router/SKILL.md

```yaml
---
name: legal-global-router
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
metadata:
  version: "3.0"
  author: "Panaversity -- The AI Agent Factory"
  chapter: "22 -- Legal Operations and Compliance"
---
```
