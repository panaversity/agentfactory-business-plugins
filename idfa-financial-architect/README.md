# IDFA Financial Architect

A Claude Code plugin that applies **Intent-Driven Financial Architecture (IDFA)** to every financial modelling interaction — automatically.

IDFA is a methodology for building financial models that are human-readable, AI-operable, and mathematically audit-proof. Developed by the [Panaversity](https://panaversity.org) team.

## Installation

### Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add panaversity/agentfactory-business-plugins
/plugin install idfa-financial-architect@agentfactory-business
```

The plugin ships two skills: **financial-architect** (IDFA methodology — auto-activates on financial model conversations) and **idfa-ops** (programmatic model interaction — Named Range CRUD, compliance auditing, recalculation).

### Cowork (Claude.ai)

1. In the Cowork sidebar, click **Customize** → **Browse plugins** → **Personal**
2. Click **+**, then select **Add marketplace from GitHub**
3. Enter: `https://github.com/panaversity/agentfactory-business-plugins`
4. Find **IDFA Financial Architect** → click **Install**

### Local Testing

Clone the repo and load it directly:

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/idfa-financial-architect
```

### Other Agents (GitHub Copilot, VS Code, Codex, Cursor)

Download `skills/financial-architect/SKILL.md` from this repo and place it in your agent's custom instructions path:

| Agent          | Path                                         |
| -------------- | -------------------------------------------- |
| GitHub Copilot | `.github/copilot-instructions.md`            |
| VS Code        | `.vscode/copilot-instructions.md`            |
| Codex (OpenAI) | Project instructions or system prompt        |
| Cursor         | `.cursorrules` or project-level instructions |

The SKILL.md content is identical across all platforms — only the file path changes.

## What It Does

When the plugin is active, the agent automatically applies four deterministic guardrails to every financial model interaction:

1. **Named Range Priority** — every formula uses Named Ranges, zero coordinate references
2. **LaTeX Verification** — complex formulas (WACC, NPV, DCF, IRR) are verified in LaTeX before writing
3. **Audit-Ready Intent Notes** — every AI-generated formula includes an Intent Note documenting its purpose
4. **Delegated Calculation** — the agent writes inputs and reads results via the spreadsheet engine, never calculating internally

## The Three Layers

Every IDFA-compliant model separates:

- **Layer 1 — Assumptions**: inputs only, all prefixed with `Inp_`
- **Layer 2 — Calculations**: Named Ranges only, readable as business rules
- **Layer 3 — Output**: presentation and formatting only

## Prerequisites

| Dependency                       | Required         | Purpose                              |
| -------------------------------- | ---------------- | ------------------------------------ |
| Python 3.10+                     | Yes              | Script runtime for `idfa-ops`        |
| [uv](https://docs.astral.sh/uv/) | Yes              | PEP 723 inline dependency resolution |
| LibreOffice                      | Yes (for recalc) | Deterministic formula evaluation     |

This plugin works best alongside Anthropic's `xlsx` skill for deterministic formula recalculation.

## Plugin Structure

```
idfa-financial-architect/
├── .claude-plugin/
│   └── plugin.json                         ← Plugin metadata (v2.0.0)
├── skills/
│   ├── financial-architect/                ← IDFA methodology
│   │   ├── SKILL.md                        ← Four Guardrails, Three Layers, Naming
│   │   └── references/
│   │       └── IDFA-reference.md           ← Enterprise governance, complex formulas
│   └── idfa-ops/                           ← Execution engine
│       ├── SKILL.md                        ← Operations guide + script reference
│       └── scripts/
│           ├── idfa_ops.py                 ← Named Range CRUD (openpyxl, PEP 723)
│           ├── idfa_audit.py               ← Compliance auditor (openpyxl, PEP 723)
│           └── recalc_bridge.py            ← LibreOffice recalc bridge (PEP 723)
├── examples/
│   └── gp_waterfall.xlsx                   ← Reference model
├── README.md
└── LICENSE
```

## Learn More

This plugin is taught in **Chapter 18: Intent-Driven Financial Architecture** of [The AI Agent Factory](https://panaversity.org) book, which covers the full methodology from the Coordinate Trap through enterprise governance.

## License

Proprietary — see [LICENSE](./LICENSE). For commercial licensing, contact licensing@panaversity.org.

## Attribution

The Intent-Driven Financial Architecture (IDFA) is original research developed by the **Panaversity team** (https://panaversity.org). IDFA is a new financial modeling language that replaces Excel's coordinate-based cell references (A1, B2, etc.) with Named Ranges that read like business rules — making financial models human-readable, AI-operable, and mathematically audit-proof.
