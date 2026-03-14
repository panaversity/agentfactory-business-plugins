# Plugin Compliance Audit — Master Architecture

## Part 1: Master Audit Checklist

Every rule from the three specs (agentskills.io SKILL.md, Claude Code Subagents, plugin.json)
is numbered below. Auditors reference these IDs in their violation reports.

---

### SKILL.md Frontmatter Rules (agentskills.io + Claude Code extensions)

#### Name field
- **S1.** `name` field is REQUIRED
- **S2.** `name` must be 1–64 characters
- **S3.** `name` must contain only lowercase letters, numbers, and hyphens
- **S4.** `name` must not start or end with a hyphen
- **S5.** `name` must not contain consecutive hyphens (`--`)
- **S6.** `name` must match the parent directory name exactly

#### Description field
- **S7.** `description` field is REQUIRED
- **S8.** `description` must be 1–1024 characters

#### Valid optional fields (agentskills.io base spec)
- **S9.** `license` is a valid optional field
- **S10.** `compatibility` is a valid optional field (1–500 chars)
- **S11.** `metadata` is a valid optional field — must be a string key-value map
- **S12.** `allowed-tools` is a valid optional field — must be a space-delimited string (NOT a YAML list)

#### Valid optional fields (Claude Code extensions)
- **S13.** `argument-hint` is a valid optional field (autocomplete hint)
- **S14.** `disable-model-invocation` is a valid optional field (boolean)
- **S15.** `user-invocable` is a valid optional field (boolean, default true)
- **S16.** `model` is a valid optional field
- **S17.** `context` is a valid optional field (value: `"fork"`)
- **S18.** `agent` is a valid optional field (subagent type name)
- **S19.** `hooks` is a valid optional field (hook config object)

#### Invalid fields — MUST NOT appear in SKILL.md frontmatter
- **S20.** `version` is NOT a valid SKILL.md field — must be moved under `metadata:`
- **S21.** `author` is NOT a valid SKILL.md field — must be moved under `metadata:`
- **S22.** `standard` is NOT a valid SKILL.md field — must be moved under `metadata:`
- **S23.** `background` is a SUBAGENT field — must be removed from skills
- **S24.** `memory` is a SUBAGENT field — must be removed from skills
- **S25.** `tools` is a SUBAGENT field — skills must use `allowed-tools` (space-delimited string)
- **S26.** `skills` is a SUBAGENT field — must be removed from skills
- **S27.** Any field not listed in S1–S19 that is not covered by S20–S26 is also invalid

#### Allowed-tools format
- **S28.** If `allowed-tools` is present, it must be a space-delimited string, not a YAML list

---

### Agent .md Frontmatter Rules (Claude Code Subagents spec)

#### Required fields
- **A1.** `name` field is REQUIRED
- **A2.** `name` must contain only lowercase letters and hyphens
- **A3.** `description` field is REQUIRED — describes when Claude should delegate to this agent

#### Valid optional fields
- **A4.** `tools` is a valid optional field — comma-separated or YAML list of tool names
- **A5.** `disallowedTools` is a valid optional field — tool names to exclude
- **A6.** `model` is a valid optional field — valid values: `sonnet`, `opus`, `haiku`, full model ID, or `inherit`
- **A7.** `permissionMode` is a valid optional field — valid values: `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`
- **A8.** `maxTurns` is a valid optional field — integer
- **A9.** `skills` is a valid optional field — list of skill names to preload
- **A10.** `mcpServers` is a valid optional field
- **A11.** `hooks` is a valid optional field
- **A12.** `memory` is a valid optional field — valid values: `user`, `project`, `local`
- **A13.** `background` is a valid optional field — boolean
- **A14.** `isolation` is a valid optional field — value: `worktree`

#### Invalid fields
- **A15.** Any field not listed in A1–A14 is invalid and must be removed or restructured
- **A16.** `version` is NOT a valid agent field
- **A17.** `author` is NOT a valid agent field
- **A18.** `standard` is NOT a valid agent field
- **A19.** `allowed-tools` is NOT a valid agent field — agents use `tools` (not `allowed-tools`)

---

### plugin.json Rules (Claude Code Plugins Reference)

#### Required fields
- **P1.** `name` is the ONLY required field

#### Valid optional fields
- **P2.** `version` — valid optional field
- **P3.** `description` — valid optional field
- **P4.** `author` — valid optional field (string or object with name/url)
- **P5.** `homepage` — valid optional field
- **P6.** `repository` — valid optional field
- **P7.** `license` — valid optional field
- **P8.** `keywords` — valid optional field (array of strings)
- **P9.** `commands` — valid optional field
- **P10.** `agents` — valid optional field
- **P11.** `skills` — valid optional field
- **P12.** `hooks` — valid optional field
- **P13.** `mcpServers` — valid optional field
- **P14.** `outputStyles` — valid optional field
- **P15.** `lspServers` — valid optional field

#### Invalid fields
- **P16.** Any field not listed in P1–P15 is invalid

#### Structural validation
- **P17.** `name` must be present and non-empty
- **P18.** All declared skills/agents/commands should have corresponding files on disk

---

## Part 2: Per-Plugin Audit Briefs

---

### Banking Plugin Audit Brief

#### Files to Read

**SKILL.md files (17):**
1. `banking/skills/banking-global-router/SKILL.md`
2. `banking/skills/aml-cdd-edd/SKILL.md`
3. `banking/skills/aml-sar-drafting/SKILL.md`
4. `banking/skills/aml-typologies/SKILL.md`
5. `banking/skills/bank-reconciliation/SKILL.md`
6. `banking/skills/basel-capital/SKILL.md`
7. `banking/skills/basel-rwa-credit/SKILL.md`
8. `banking/skills/basel-rwa-market/SKILL.md`
9. `banking/skills/ifrs9-disclosure/SKILL.md`
10. `banking/skills/ifrs9-ecl/SKILL.md`
11. `banking/skills/ifrs9-scenarios/SKILL.md`
12. `banking/skills/ifrs9-staging/SKILL.md`
13. `banking/skills/kyc-risk-rating/SKILL.md`
14. `banking/skills/liquidity-lcr/SKILL.md`
15. `banking/skills/liquidity-nsfr/SKILL.md`
16. `banking/skills/sanctions-screening/SKILL.md`
17. `banking/skills/stress-testing/SKILL.md`

**Other files:**
- `banking/.claude-plugin/plugin.json`
- `banking/CLAUDE.md`

**Agent files:** None

#### Applicable Checklist Items
- S1–S28 (all SKILL.md rules) for each of the 17 SKILL.md files
- P1–P18 (all plugin.json rules) for plugin.json

#### Exit Criteria
- Every SKILL.md frontmatter checked against S1–S28
- plugin.json checked against P1–P18
- Every violation has a proposed fix with corrected frontmatter YAML block
- Report written to `specs/drafts/audit-banking.md`

---

### Islamic Finance Plugin Audit Brief

#### Files to Read

**SKILL.md files (13):**
1. `islamic-finance/skills/islamic-finance-router/SKILL.md`
2. `islamic-finance/skills/ijarah-imb/SKILL.md`
3. `islamic-finance/skills/istisna-a/SKILL.md`
4. `islamic-finance/skills/mudaraba/SKILL.md`
5. `islamic-finance/skills/murabaha/SKILL.md`
6. `islamic-finance/skills/musharaka-dm/SKILL.md`
7. `islamic-finance/skills/musharaka-full/SKILL.md`
8. `islamic-finance/skills/salam/SKILL.md`
9. `islamic-finance/skills/shariah-screening-global/SKILL.md`
10. `islamic-finance/skills/sukuk-investor/SKILL.md`
11. `islamic-finance/skills/sukuk-issuer/SKILL.md`
12. `islamic-finance/skills/takaful-ifrs17/SKILL.md`
13. `islamic-finance/skills/zakat-global/SKILL.md`

**Other files:**
- `islamic-finance/.claude-plugin/plugin.json`
- `islamic-finance/CLAUDE.md`

**Agent files:** None

#### Applicable Checklist Items
- S1–S28 (all SKILL.md rules) for each of the 13 SKILL.md files
- P1–P18 (all plugin.json rules) for plugin.json

#### Exit Criteria
- Every SKILL.md frontmatter checked against S1–S28
- plugin.json checked against P1–P18
- Every violation has a proposed fix with corrected frontmatter YAML block
- Report written to `specs/drafts/audit-islamic-finance.md`

---

### IDFA Financial Architect Plugin Audit Brief

#### Files to Read

**SKILL.md files (2):**
1. `idfa-financial-architect/skills/financial-architect/SKILL.md`
2. `idfa-financial-architect/skills/idfa-ops/SKILL.md`

**Other files:**
- `idfa-financial-architect/.claude-plugin/plugin.json`
- `idfa-financial-architect/CLAUDE.md`

**Agent files:** None

#### Applicable Checklist Items
- S1–S28 (all SKILL.md rules) for each of the 2 SKILL.md files
- P1–P18 (all plugin.json rules) for plugin.json

#### Exit Criteria
- Every SKILL.md frontmatter checked against S1–S28
- plugin.json checked against P1–P18
- Every violation has a proposed fix with corrected frontmatter YAML block
- Report written to `specs/drafts/audit-idfa-financial-architect.md`

---

### Legal Ops Plugin Audit Brief

#### Files to Read

**SKILL.md files (6):**
1. `legal-ops/skills/legal-global-router/SKILL.md`
2. `legal-ops/skills/compliance-calendar/SKILL.md`
3. `legal-ops/skills/dsar-privacy/SKILL.md`
4. `legal-ops/skills/ip-protection/SKILL.md`
5. `legal-ops/skills/legal-spend/SKILL.md`
6. `legal-ops/skills/regulatory-monitoring/SKILL.md`

**Agent files (1):**
1. `legal-ops/agents/contract-intake.md`

**Other files:**
- `legal-ops/.claude-plugin/plugin.json`
- `legal-ops/CLAUDE.md`

#### Applicable Checklist Items
- S1–S28 (all SKILL.md rules) for each of the 6 SKILL.md files
- A1–A19 (all Agent rules) for `contract-intake.md`
- P1–P18 (all plugin.json rules) for plugin.json

#### Exit Criteria
- Every SKILL.md frontmatter checked against S1–S28
- Agent .md frontmatter checked against A1–A19
- plugin.json checked against P1–P18
- Every violation has a proposed fix with corrected frontmatter YAML block
- Report written to `specs/drafts/audit-legal-ops.md`

---

### Sales, RevOps & Marketing Plugin Audit Brief

#### Files to Read

**SKILL.md files (15):**
1. `sales-revops-marketing/skills/sales-marketing-global-router/SKILL.md`
2. `sales-revops-marketing/skills/campaign-planning/SKILL.md`
3. `sales-revops-marketing/skills/content-calendar/SKILL.md`
4. `sales-revops-marketing/skills/content-creation/SKILL.md`
5. `sales-revops-marketing/skills/copywriting/SKILL.md`
6. `sales-revops-marketing/skills/crm-enrichment/SKILL.md`
7. `sales-revops-marketing/skills/follow-up/SKILL.md`
8. `sales-revops-marketing/skills/lead-scoring/SKILL.md`
9. `sales-revops-marketing/skills/outreach/SKILL.md`
10. `sales-revops-marketing/skills/performance-analysis/SKILL.md`
11. `sales-revops-marketing/skills/persona-icp/SKILL.md`
12. `sales-revops-marketing/skills/pipeline/SKILL.md`
13. `sales-revops-marketing/skills/pre-call-brief/SKILL.md`
14. `sales-revops-marketing/skills/prospect-research/SKILL.md`
15. `sales-revops-marketing/skills/sequence/SKILL.md`

**Agent files (5):**
1. `sales-revops-marketing/agents/crm-hygiene-agent.md`
2. `sales-revops-marketing/agents/lead-intelligence-agent.md`
3. `sales-revops-marketing/agents/marketing-performance-agent.md`
4. `sales-revops-marketing/agents/outreach-sequencing-agent.md`
5. `sales-revops-marketing/agents/revenue-reporting-agent.md`

**Other files:**
- `sales-revops-marketing/.claude-plugin/plugin.json`
- `sales-revops-marketing/CLAUDE.md`

#### Applicable Checklist Items
- S1–S28 (all SKILL.md rules) for each of the 15 SKILL.md files
- A1–A19 (all Agent rules) for each of the 5 agent .md files
- P1–P18 (all plugin.json rules) for plugin.json

#### Exit Criteria
- Every SKILL.md frontmatter checked against S1–S28
- Every agent .md frontmatter checked against A1–A19
- plugin.json checked against P1–P18
- Every violation has a proposed fix with corrected frontmatter YAML block
- Report written to `specs/drafts/audit-sales-revops-marketing.md`

---

## Part 3: Known Violation Patterns (Pre-Audit Intelligence)

Based on the team prompt's pre-audit intelligence, auditors should expect these
common violations across most plugins:

| Invalid Field | Violation Rule | Expected Fix |
|---------------|----------------|--------------|
| `version` at top level | S20 | Move to `metadata:\n  version: "X.Y.Z"` |
| `author` at top level | S21 | Move to `metadata:\n  author: "Panaversity"` |
| `standard` at top level | S22 | Move to `metadata:\n  standard: "..."` |
| `background` in skill | S23 | Remove entirely (subagent-only field) |
| `memory` in skill | S24 | Remove entirely (subagent-only field) |
| `tools` in skill | S25 | Replace with `allowed-tools` (space-delimited string) |
| `skills` in skill | S26 | Remove entirely (subagent-only field) |
| `allowed-tools` as YAML list | S28 | Convert to space-delimited string |

Auditors: check EVERY SKILL.md for ALL of these, not just the ones flagged here.
There may be additional violations not covered by this pre-audit intelligence.

---

## Part 4: Audit Report Format

Each auditor must produce a report at `specs/drafts/audit-<plugin-name>.md` using
this exact structure:

```markdown
## <Plugin Name> Compliance Report

### Summary
- Total skills audited: N
- Total agents audited: N
- Total violations found: N
- Critical (invalid fields): N
- Warning (best practice): N

### Violations

#### <file-path>
- [ ] VIOLATION S20: `version: 1.0` is not a valid frontmatter field
  - FIX: Move to `metadata:` block -> `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity` is not a valid frontmatter field
  - FIX: Move to `metadata:` block -> `metadata:\n  author: "Panaversity"`
...

### Proposed Fixed Frontmatter

#### <file-path>
\```yaml
---
name: skill-name
description: >-
  Skill description here.
metadata:
  version: "1.0"
  author: "Panaversity"
  standard: "Relevant Standard"
allowed-tools: "tool1 tool2 tool3"
---
\```
```

---

## Part 5: File Inventory Summary

| Plugin | Skills | Agents | plugin.json | Total Files to Audit |
|--------|--------|--------|-------------|---------------------|
| Banking | 17 | 0 | 1 | 18 |
| Islamic Finance | 13 | 0 | 1 | 14 |
| IDFA Financial Architect | 2 | 0 | 1 | 3 |
| Legal Ops | 6 | 1 | 1 | 8 |
| Sales, RevOps & Marketing | 15 | 5 | 1 | 21 |
| **TOTAL** | **53** | **6** | **5** | **64** |
