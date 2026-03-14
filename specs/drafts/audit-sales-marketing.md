## Sales, RevOps & Marketing Plugin Compliance Report

### Summary

- Total skills audited: 15
- Total agents audited: 5
- Total violations found: 0
- Critical (invalid fields): 0
- Warning (best practice): 0

---

### Violations

No violations found. All 15 SKILL.md files and all 5 agent .md files pass every rule in S1–S28 and A1–A19 respectively. The plugin.json passes all P1–P18 rules.

---

### Per-File Results

#### Skills

| File | Valid Fields Present | Violations |
|------|----------------------|------------|
| `sales-revops-marketing/skills/sales-marketing-global-router/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/campaign-planning/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/content-calendar/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/content-creation/SKILL.md` | `name`, `description`, `context: fork` | None |
| `sales-revops-marketing/skills/copywriting/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/crm-enrichment/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/follow-up/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/lead-scoring/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/outreach/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/performance-analysis/SKILL.md` | `name`, `description`, `context: fork` | None |
| `sales-revops-marketing/skills/persona-icp/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/pipeline/SKILL.md` | `name`, `description`, `context: fork` | None |
| `sales-revops-marketing/skills/pre-call-brief/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/prospect-research/SKILL.md` | `name`, `description` | None |
| `sales-revops-marketing/skills/sequence/SKILL.md` | `name`, `description` | None |

Notes:
- Three skills use `context: fork` (content-creation, performance-analysis, pipeline) — this is a valid optional field per S17.
- No skill uses `version`, `author`, `standard`, `background`, `memory`, `tools`, or `skills` at top level.
- No skill uses `allowed-tools` as a YAML list.

#### Agents

| File | Valid Fields Present | Violations |
|------|----------------------|------------|
| `sales-revops-marketing/agents/crm-hygiene-agent.md` | `name`, `description`, `memory`, `skills`, `tools`, `maxTurns` | None |
| `sales-revops-marketing/agents/lead-intelligence-agent.md` | `name`, `description`, `background`, `memory`, `skills`, `tools` | None |
| `sales-revops-marketing/agents/marketing-performance-agent.md` | `name`, `description`, `background`, `memory`, `skills`, `tools` | None |
| `sales-revops-marketing/agents/outreach-sequencing-agent.md` | `name`, `description`, `skills`, `tools` | None |
| `sales-revops-marketing/agents/revenue-reporting-agent.md` | `name`, `description`, `background`, `memory`, `skills`, `tools` | None |

Notes:
- All agent `tools` fields are YAML lists — correct for agents (A4).
- `memory: project` is a valid value per A12.
- `background: true` is a valid boolean per A13.
- `maxTurns: 50` in crm-hygiene-agent is a valid integer per A8.
- No agent uses `version`, `author`, `standard`, or `allowed-tools`.

#### plugin.json

| Field | Value | Valid? |
|-------|-------|--------|
| `name` | `"sales-revops-marketing"` | Yes (P1, P17) |
| `version` | `"1.0.0"` | Yes (P2) |
| `description` | present | Yes (P3) |
| `author` | object with `name` and `url` | Yes (P4) |
| `homepage` | present | Yes (P5) |
| `repository` | present | Yes (P6) |
| `license` | `"Apache-2.0"` | Yes (P7) |
| `keywords` | array of strings | Yes (P8) |

No invalid fields. No missing required fields. Result: PASS.

---

### Proposed Fixed Frontmatter

No fixes required. All files are compliant as-is.
