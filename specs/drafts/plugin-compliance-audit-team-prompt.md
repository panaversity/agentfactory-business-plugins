# Plugin Compliance Audit — Agent Team Prompt

Create an agent team to audit all 5 plugins for compliance with three specifications:

1. **Agent Skills spec** — https://agentskills.io/specification
2. **Claude Code Skills spec** — https://code.claude.com/docs/en/skills
3. **Claude Code Subagents spec** — https://code.claude.com/docs/en/sub-agents
4. **Claude Code Plugins reference** — https://code.claude.com/docs/en/plugins-reference

IMPORTANT: This MUST be an agent team (https://code.claude.com/docs/en/agent-teams),
NOT subagents. Use TeamCreate to create the team. Spawn teammates — do NOT use the
Agent tool or spawn subagents. Every worker below is a TEAMMATE in the team,
coordinated through the shared task list and inter-teammate messaging.

---

## Context: What We're Auditing

This repository contains 5 Claude Code plugins at:
`/Users/mjs/Documents/code/panaversity-official/agentfactory-business-plugins/`

| Plugin | Path | Skills | Agents |
|--------|------|--------|--------|
| Banking | `banking/` | 17 (1 router + 16 products) | 0 |
| Islamic Finance | `islamic-finance/` | 13 (1 router + 12 products) | 0 |
| IDFA Financial Architect | `idfa-financial-architect/` | 2 | 0 |
| Legal Operations | `legal-ops/` | 6 (1 router + 5 products) | 1 agent |
| Sales, RevOps & Marketing | `sales-revops-marketing/` | 15 (1 router + 14 products) | 5 agents |

**Total: 53 skills + 6 agents across 5 plugins.**

---

## Known Compliance Issues (Pre-Audit Intelligence)

Based on spec analysis, these violations are ALREADY KNOWN to exist. Auditors must
find ALL instances and propose fixes:

### SKILL.md Frontmatter Violations

The agentskills.io spec defines these as the ONLY valid frontmatter fields:
- `name` (required) — max 64 chars, lowercase + hyphens, must match directory name
- `description` (required) — max 1024 chars
- `license` (optional)
- `compatibility` (optional)
- `metadata` (optional) — arbitrary key-value map
- `allowed-tools` (optional) — space-delimited tool list

Claude Code extends with:
- `argument-hint`, `disable-model-invocation`, `user-invocable`, `model`,
  `context`, `agent`, `hooks`

**Fields that DO NOT EXIST in either spec (but are used in our plugins):**

| Invalid Field | Found In | What To Do |
|---------------|----------|------------|
| `version` | Most skills | Move under `metadata:` as `metadata.version` |
| `author` | Most skills | Move under `metadata:` as `metadata.author` |
| `standard` | Most skills | Move under `metadata:` as `metadata.standard` |
| `background` | Some skills | This is a SUBAGENT field, not a skill field. Remove from skills. |
| `memory` | Some skills | This is a SUBAGENT field, not a skill field. Remove from skills. |
| `tools` | Some skills | This is a SUBAGENT field, not a skill field. For skills, use `allowed-tools` (space-delimited string, not YAML list). |
| `skills` | Some skills | This is a SUBAGENT field, not a skill field. Remove from skills. |

### Agent .md Frontmatter Violations

The Claude Code subagent spec defines these valid frontmatter fields:
- `name` (required) — lowercase letters and hyphens
- `description` (required) — when Claude should delegate
- `tools` (optional) — comma-separated or YAML list of tool names
- `disallowedTools` (optional)
- `model` (optional) — `sonnet`, `opus`, `haiku`, full model ID, or `inherit`
- `permissionMode` (optional) — `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`
- `maxTurns` (optional)
- `skills` (optional) — list of skills to preload
- `mcpServers` (optional)
- `hooks` (optional)
- `memory` (optional) — `user`, `project`, or `local`
- `background` (optional) — boolean
- `isolation` (optional) — `worktree`

**Agents may have their own invalid fields — auditors must check.**

### plugin.json Compliance

Each plugin has `.claude-plugin/plugin.json`. Verify:
- `name` is the only required field
- All metadata fields match the schema
- No extraneous fields

### SKILL.md Name vs Directory Name

The `name` field MUST match the parent directory name. Example:
- Directory: `skills/aml-cdd-edd/` → `name: aml-cdd-edd` ✓
- Directory: `skills/AML-CDD-EDD/` → `name: aml-cdd-edd` ✗ (directory must also be lowercase)

### Name Format Validation

Names must be:
- 1-64 characters
- Lowercase letters, numbers, hyphens only
- No leading/trailing hyphens
- No consecutive hyphens (`--`)

---

## Team Structure

### Phase 1: Architect (1 teammate, Opus)

**Teammate: `architect`**

Reads all specs (already summarized above) and all 5 plugin directories. Produces:

1. **Master Audit Checklist** — every rule from all 3 specs, numbered
2. **Per-Plugin Audit Briefs** — for each of the 5 auditor teammates:
   - Exact file paths to read
   - Which checklist items apply
   - Exit criteria (what "done" means)

Write output to: `specs/drafts/audit-architecture.md`

When finished, message the team lead: "ARCHITECT DONE — audit-architecture.md written"

### Phase 2: Auditor Teammates (5 teammates, parallel, Sonnet)

One teammate per plugin. Each reads ONLY:
1. The architect's audit brief for their plugin
2. Every SKILL.md in their plugin's `skills/` directory
3. Every agent .md in their plugin's `agents/` directory (if any)
4. Their plugin's `.claude-plugin/plugin.json`
5. Their plugin's `CLAUDE.md`

Each produces a **compliance report** at `specs/drafts/audit-<plugin-name>.md` with:

```
## <Plugin Name> Compliance Report

### Summary
- Total skills audited: N
- Total agents audited: N
- Total violations found: N
- Critical (invalid fields): N
- Warning (best practice): N

### Violations

#### <file-path>
- [ ] VIOLATION: `version: 1.0` is not a valid frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION: `author: Panaversity` is not a valid frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION: `standard: FATF...` is not a valid frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "FATF Recommendation 10..."`
...

### Proposed Fixed Frontmatter

For each file with violations, provide the corrected YAML frontmatter block
(the full `---` to `---` section) ready to paste.
```

#### Teammate Assignments

**`auditor-banking`** — `banking/` plugin
- 17 skills in `banking/skills/`
- 0 agents
- `banking/.claude-plugin/plugin.json`

**`auditor-islamic-finance`** — `islamic-finance/` plugin
- 13 skills in `islamic-finance/skills/`
- 0 agents
- `islamic-finance/.claude-plugin/plugin.json`

**`auditor-idfa`** — `idfa-financial-architect/` plugin
- 2 skills in `idfa-financial-architect/skills/`
- 0 agents
- `idfa-financial-architect/.claude-plugin/plugin.json`

**`auditor-legal-ops`** — `legal-ops/` plugin
- 6 skills in `legal-ops/skills/`
- 1 agent in `legal-ops/agents/`
- `legal-ops/.claude-plugin/plugin.json`

**`auditor-sales-marketing`** — `sales-revops-marketing/` plugin
- 15 skills in `sales-revops-marketing/skills/`
- 5 agents in `sales-revops-marketing/agents/`
- `sales-revops-marketing/.claude-plugin/plugin.json`

Each auditor teammate MUST message the lead when done:
"AUDITOR [PLUGIN] DONE — audit-<plugin-name>.md written, N violations found"

### Phase 3: Consolidation (Lead does this, not a teammate)

After all 5 auditors complete, the lead:

1. Reads all 5 audit reports
2. Produces a consolidated summary at `specs/drafts/audit-consolidated.md`:
   - Total violations across all plugins
   - Violation frequency table (which invalid fields appear most)
   - Recommended batch fix strategy (e.g., sed script or agent task)
   - Cross-plugin consistency check (are all plugins using the same metadata structure?)
3. Reports the consolidated summary to the user

---

## Lead Coordination Rules

1. Create the team with TeamCreate
2. Create all tasks upfront with dependencies:
   - Task: "Architect audit framework" (Phase 1, no dependencies)
   - Task: "Audit banking plugin" (Phase 2, depends on Phase 1)
   - Task: "Audit islamic-finance plugin" (Phase 2, depends on Phase 1)
   - Task: "Audit idfa plugin" (Phase 2, depends on Phase 1)
   - Task: "Audit legal-ops plugin" (Phase 2, depends on Phase 1)
   - Task: "Audit sales-marketing plugin" (Phase 2, depends on Phase 1)
   - Task: "Consolidate audit reports" (Phase 3, depends on all Phase 2)
3. Do NOT write audit content yourself — delegate everything to teammates
4. Wait for Phase 1 to complete before spawning Phase 2 teammates
5. Phase 2 teammates run in PARALLEL
6. After all Phase 2 teammates finish, do Phase 3 consolidation yourself
7. Shut down teammates, clean up team

---

## Anti-Patterns to Avoid

- Do NOT use the Agent tool or spawn subagents — this is a TEAM with TEAMMATES
- Do NOT write audit content yourself (except Phase 3 consolidation) — delegate to teammates
- Do NOT spawn Phase 2 auditor teammates before the architect completes
- Do NOT let auditor teammates read the full specs (the architect's brief has everything they need)
- Do NOT approve the architect's output without reviewing the checklist completeness
- Do NOT skip Phase 3 consolidation — the user needs a single summary

---

## Spec Summary (for architect reference)

### agentskills.io SKILL.md Valid Fields

```yaml
---
name: required, 1-64 chars, lowercase+hyphens, matches directory name
description: required, 1-1024 chars
license: optional
compatibility: optional, 1-500 chars
metadata: optional, string key-value map
allowed-tools: optional, space-delimited string
---
```

### Claude Code SKILL.md Additional Valid Fields

```yaml
argument-hint: optional, autocomplete hint
disable-model-invocation: optional, boolean
user-invocable: optional, boolean (default true)
allowed-tools: optional (same as agentskills.io)
model: optional
context: optional, "fork"
agent: optional, subagent type name
hooks: optional, hook config object
```

### Claude Code Agent .md Valid Fields

```yaml
---
name: required, lowercase+hyphens
description: required
tools: optional, tool list
disallowedTools: optional, tool list
model: optional (sonnet/opus/haiku/full-id/inherit)
permissionMode: optional (default/acceptEdits/dontAsk/bypassPermissions/plan)
maxTurns: optional, integer
skills: optional, skill name list
mcpServers: optional
hooks: optional
memory: optional (user/project/local)
background: optional, boolean
isolation: optional, "worktree"
---
```

### plugin.json Required Fields

Only `name` is required. All other fields (`version`, `description`, `author`,
`homepage`, `repository`, `license`, `keywords`, `commands`, `agents`, `skills`,
`hooks`, `mcpServers`, `outputStyles`, `lspServers`) are optional.

---

## Model Preferences

- Architect: **Opus** (needs to synthesize multiple specs into a coherent framework)
- Auditors: **Sonnet** (pattern-matching against a checklist — speed over depth)
- Lead: inherits session model

---

## Success Criteria

The audit is DONE when:

1. `specs/drafts/audit-architecture.md` exists with complete checklist
2. All 5 `specs/drafts/audit-<plugin>.md` files exist with violation reports
3. `specs/drafts/audit-consolidated.md` exists with:
   - Total violation count
   - Frequency table
   - Recommended fix strategy
4. Every SKILL.md and agent .md file in the repo has been read and checked
5. Every violation includes a concrete, paste-ready fix
