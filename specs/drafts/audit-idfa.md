## IDFA Financial Architect Compliance Report

### Summary
- Total skills audited: 2
- Total agents audited: 0
- Total violations found: 1
- Critical (invalid fields): 1
- Warning (best practice): 0

---

### Violations

#### `idfa-financial-architect/skills/financial-architect/SKILL.md`
- [ ] VIOLATION S6: `name: idfa-financial-architect` does not match the parent directory name `financial-architect`
  - FIX: Change `name` to `financial-architect` to match the parent directory

---

### Proposed Fixed Frontmatter

#### `idfa-financial-architect/skills/financial-architect/SKILL.md`
```yaml
---
name: financial-architect
description: >-
  Use this skill for hands-on Excel financial model work: building models
  from scratch (SaaS, three-statement, revenue/COGS/EBITDA), auditing a
  spreadsheet for formula errors, explaining or mapping out model logic,
  converting cell references to named ranges, running what-if or scenario
  analysis, goal-seeking (what input value produces a target output?), or
  running Monte Carlo simulations. Also use when someone has inherited an
  unfamiliar model, calls it a "black box", or needs a specific formula
  (like WACC) checked. The trigger is a user who has a spreadsheet and
  needs to do something with it. Do NOT use for accounting theory, tax
  questions, investment advice, or finance questions with no model attached.
license: Proprietary
metadata:
  author: Panaversity
  research-lead: Zia Khan
  version: "1.0"
  published: "2026"
  homepage: https://panaversity.org
  standard: https://agentskills.io
  description: >-
    IDFA is original research by the Panaversity team — pioneers in AI-native
    education and developers of the Agent Factory methodology. IDFA translates
    the principles of spec-driven, logic-first design into a deployable
    architecture for the Office of the CFO.
---
```

---

### Clean Files (No Violations)

- `idfa-financial-architect/skills/idfa-ops/SKILL.md` — fully compliant
- `idfa-financial-architect/.claude-plugin/plugin.json` — fully compliant
