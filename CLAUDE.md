# AgentFactory Business Plugins — Development Guide

## What This Repo Is

A collection of Claude Code plugins for regulated business domains. Each plugin
is a self-contained directory following the Claude Code plugin spec.

| Plugin | Path | Skills | Agents | Version |
|--------|------|--------|--------|---------|
| Banking | `banking/` | 17 | 0 | 2.0.0 |
| Islamic Finance | `islamic-finance/` | 13 | 0 | 3.0.0 |
| IDFA Financial Architect | `idfa-financial-architect/` | 2 | 0 | 1.0 |
| Legal Operations | `legal-ops/` | 6 | 1 | 3.0.0 |
| Sales, RevOps & Marketing | `sales-revops-marketing/` | 15 | 5 | 1.0 |

## Before Building a New Plugin — Check Anthropic's First-Party Plugins

**HARD RULE**: Before creating any new plugin or skill, audit what already exists in
Anthropic's official knowledge-work-plugins repo:
https://github.com/anthropics/knowledge-work-plugins/tree/main

Our plugins are **Layer 2** — they extend, specialize, or add jurisdiction-aware
depth to Anthropic's **Layer 1** plugins. We do NOT duplicate what Anthropic already
provides. We wrap it, override it with domain-specific logic, or fill gaps they don't cover.

### Anthropic's First-Party Plugins (Layer 1)

| Plugin | Skills | Our Overlap |
|--------|--------|-------------|
| **sales** | account-research, call-prep, call-summary, competitive-intelligence, create-an-asset, daily-briefing, draft-outreach, forecast, pipeline-review | Our `sales-revops-marketing` wraps/overrides 7 of these — see collision table in its CLAUDE.md |
| **marketing** | brand-review, campaign-plan, competitive-brief, content-creation, draft-content, email-sequence, performance-report, seo-audit | Our `sales-revops-marketing` wraps/overrides 3 of these |
| **legal** | brief, compliance-check, legal-response, legal-risk-assessment, meeting-briefing, review-contract, signature-request, triage-nda, vendor-check | Our `legal-ops` routes through these 9 commands as Layer 1, adds jurisdiction overlays |
| **finance** | audit-support, close-management, financial-statements, journal-entry-prep, journal-entry, reconciliation, sox-testing, variance-analysis | Our `banking` is adjacent (regulatory, not corporate finance) — minimal overlap |
| **productivity** | Task/calendar/workflow management | No overlap |
| **customer-support** | Ticket triage, responses, escalation | No overlap |
| **product-management** | Specs, roadmaps, user research | No overlap |
| **data** | SQL, analytics, dashboards | No overlap |
| **enterprise-search** | Cross-tool search | No overlap |
| **bio-research** | Life sciences R&D | No overlap |

Also check `partner-built/` for: apollo, brand-voice, common-room, slack.

### Collision Resolution Patterns

When our plugin overlaps with an Anthropic plugin, use one of these patterns
(documented in the overlapping plugin's CLAUDE.md):

| Pattern | When to Use | How It Works |
|---------|-------------|--------------|
| **Wrapper** | We add value on top of their skill | Call their skill first, then enhance output (e.g., add ICP scoring, jurisdiction compliance) |
| **Override** | Our version fully replaces theirs | Our skill includes all their functionality plus domain-specific logic |
| **Delegation** | Context determines which to use | Router selects their skill or ours based on query |

### What This Means in Practice

1. **New sales/marketing skill?** Check if `anthropics/knowledge-work-plugins/sales/` or `/marketing/` already has it. If yes → wrap or override, don't duplicate.
2. **New legal skill?** Check if it's one of the 9 Layer 1 commands. If yes → our router enriches it with jurisdiction overlays, don't rebuild.
3. **New finance skill?** Check `/finance/` for corporate finance overlap. Our banking plugin covers regulatory (Basel, IFRS 9, AML) — different domain.
4. **Entirely new domain?** (e.g., healthcare, insurance) → Check the full repo first, then build fresh.

## Specifications We Follow

All plugins, skills, and agents MUST comply with:

1. **Agent Skills spec** — https://agentskills.io/specification
2. **Claude Code Skills spec** — https://code.claude.com/docs/en/skills
3. **Claude Code Subagents spec** — https://code.claude.com/docs/en/sub-agents
4. **Claude Code Plugins reference** — https://code.claude.com/docs/en/plugins-reference

## SKILL.md Frontmatter Rules

### Valid fields (and ONLY these)

From agentskills.io:
- `name` (required) — 1-64 chars, lowercase + numbers + hyphens, must match directory name
- `description` (required) — 1-1024 chars, describes what the skill does and when to use it
- `license` (optional)
- `compatibility` (optional) — 1-500 chars
- `metadata` (optional) — string key-value map for author, version, standard, etc.
- `allowed-tools` (optional) — space-delimited string (NOT a YAML list)

Claude Code extensions:
- `argument-hint` (optional)
- `disable-model-invocation` (optional, boolean)
- `user-invocable` (optional, boolean, default true)
- `model` (optional)
- `context` (optional, value: `"fork"`)
- `agent` (optional, subagent type name)
- `hooks` (optional, hook config object)

### Fields that MUST NOT appear in SKILL.md

| Field | Why | Where It Belongs |
|-------|-----|------------------|
| `version` | Not in spec | `metadata:\n  version: "1.0"` |
| `author` | Not in spec | `metadata:\n  author: "Panaversity"` |
| `standard` | Not in spec | `metadata:\n  standard: "..."` |
| `background` | Subagent field | Only in `agents/*.md` |
| `memory` | Subagent field | Only in `agents/*.md` |
| `tools` | Subagent field | Use `allowed-tools` (space-delimited string) |
| `skills` | Subagent field | Only in `agents/*.md` |

### Name rules

- Lowercase letters, numbers, hyphens only
- No leading/trailing hyphens
- No consecutive hyphens (`--`)
- Must match the parent directory name exactly

### Correct example

```yaml
---
name: aml-cdd-edd
description: >
  Activate for: CDD, EDD, customer due diligence...
  NOT for: personal finance advice...
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "FATF Recommendation 10 (CDD), 12 (PEPs)"
---
```

## Agent .md Frontmatter Rules

### Valid fields (and ONLY these)

- `name` (required) — lowercase + hyphens
- `description` (required) — when Claude should delegate to this agent
- `tools` (optional) — YAML list of tool names
- `disallowedTools` (optional)
- `model` (optional) — `sonnet`, `opus`, `haiku`, full model ID, or `inherit`
- `permissionMode` (optional) — `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`
- `maxTurns` (optional) — integer
- `skills` (optional) — list of skill names to preload
- `mcpServers` (optional)
- `hooks` (optional)
- `memory` (optional) — `user`, `project`, or `local`
- `background` (optional) — boolean
- `isolation` (optional) — `worktree`

### Fields that MUST NOT appear in agents

`version`, `author`, `standard`, `allowed-tools` (agents use `tools`, not `allowed-tools`)

## plugin.json Rules

Located at `<plugin>/.claude-plugin/plugin.json`.

- `name` is the only required field
- Valid optional fields: `version`, `description`, `author`, `homepage`, `repository`,
  `license`, `keywords`, `commands`, `agents`, `skills`, `hooks`, `mcpServers`,
  `outputStyles`, `lspServers`

## Plugin Directory Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json        # Manifest (only file in this dir)
├── skills/                # Skills with SKILL.md
│   └── skill-name/
│       ├── SKILL.md       # Required
│       ├── references/    # Optional reference docs
│       └── scripts/       # Optional executable code
├── agents/                # Subagent definitions
│   └── agent-name.md
├── commands/              # Legacy commands (prefer skills/)
├── hooks/
│   └── hooks.json
├── scripts/               # Utility scripts
├── evals/                 # Eval harness
├── CLAUDE.md              # Plugin-level instructions
└── README.md
```

## Architecture Patterns

### Router pattern

Each multi-skill plugin has a global router skill that:
1. Identifies the task type from the user query
2. Maps to the appropriate product skill
3. Loads jurisdiction overlays if applicable
4. Applies a mandatory output header

### Mandatory output header

Every plugin defines a mandatory output header in its CLAUDE.md. All responses
from the plugin must begin with this header (governing standard, jurisdiction, etc.).

### Jurisdiction overlays

Stored in `skills/<router>/references/jurisdictions/*.md`. Loaded by the router
based on the user's query context.

## Quality Checklist (Before Committing)

Run these checks before committing any skill or agent changes:

```bash
# 1. No invalid top-level fields in SKILL.md
for f in $(find . -name "SKILL.md" -path "*/skills/*"); do
  head -20 "$f" | grep -E "^(version|author|standard|background|memory|tools:|skills:)" && echo "FAIL: $f"
done

# 2. All names match directories
for f in $(find . -name "SKILL.md" -path "*/skills/*"); do
  dir=$(basename $(dirname "$f"))
  name=$(grep "^name:" "$f" | head -1 | sed 's/name: *//')
  [ "$dir" != "$name" ] && echo "MISMATCH: $f (dir=$dir, name=$name)"
done

# 3. No stale shell substitutions
grep -r '$(cat ' */skills/*/SKILL.md && echo "STALE SHELL SUBS FOUND"
```

## Compliance Audit Team Prompt

For full repo-wide compliance audits, use the team prompt at:
`specs/drafts/plugin-compliance-audit-team-prompt.md`

This spawns a 7-teammate agent team (1 architect + 5 parallel auditors + lead consolidation)
that checks every SKILL.md and agent .md against all three specs. Produces per-plugin
audit reports with paste-ready corrected frontmatter blocks.

The March 2026 audit found 52 violations (48 in banking, 3 in legal-ops, 1 in IDFA) —
all fixed. Sales-marketing and islamic-finance were already clean.
