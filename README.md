# Agent Factory — Business Domain Plugins

Marketplace for business domain agent plugins from **[The AI Agent Factory](https://learn.panaversity.org)** by Panaversity — Part 3: Business Domain Agent Workflows.

---

## Available Plugins

| Plugin                                                      | Description                                                                                                                                                            | Version | Install                                                                |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| **[islamic-finance](./islamic-finance/)**                   | 12 product skills, 13 jurisdiction overlays, 4 domain commands for Islamic finance accounting across AAOIFI, IFRS, and local standards                                 | v2.0.0  | `claude plugin install islamic-finance@agentfactory-business`          |
| **[idfa-financial-architect](./idfa-financial-architect/)** | Intent-Driven Financial Architecture (IDFA) — four guardrails, three layers, two skills for human-readable, AI-operable, audit-proof financial models                  | v2.0.0  | `claude plugin install idfa-financial-architect@agentfactory-business` |
| **[banking](./banking/)**                                   | 16 product skills, 7 jurisdiction overlays, 4 domain commands for banking regulatory compliance across IFRS 9, Basel III/IV, AML/KYC/sanctions                         | v1.0.0  | `claude plugin install banking@agentfactory-business`                  |
| **[legal-ops](./legal-ops/)**                               | 8 product skills, 5 jurisdiction overlays, 4 domain commands for legal operations — contract review, NDA triage, IP protection, regulatory monitoring, DSAR management | v1.0.0  | `claude plugin install legal-ops@agentfactory-business`                |

> Individual plugins may have their own license terms. See each plugin's LICENSE file for details.

---

## Quick Start

### Option A: Install via Claude Code CLI (Recommended)

```bash
# Install a plugin
claude plugin install islamic-finance@agentfactory-business
claude plugin install idfa-financial-architect@agentfactory-business
claude plugin install banking@agentfactory-business
claude plugin install legal-ops@agentfactory-business

# Verify installation
claude --list-plugins
```

### Option B: Install via Cowork (Claude.ai)

1. Sidebar → Customize → Browse plugins → +
2. Add marketplace from GitHub → `panaversity/agentfactory-business-plugins`
3. Select and install the plugin you need

### Option C: Clone for Local Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/islamic-finance
claude --plugin-dir ./agentfactory-business-plugins/idfa-financial-architect
claude --plugin-dir ./agentfactory-business-plugins/banking
claude --plugin-dir ./agentfactory-business-plugins/legal-ops
```

---

## Marketplace Structure

```
agentfactory-business-plugins/
├── marketplace.json          # Plugin catalog
├── islamic-finance/          # Islamic Finance Domain Agents plugin
│   ├── .claude-plugin/       # Plugin manifest
│   ├── skills/               # 13 domain skills (auto-loaded)
│   ├── commands/             # 4 slash commands (auto-loaded)
│   ├── hooks/                # Session + validation hooks (auto-loaded)
│   ├── scripts/              # Test harness
│   ├── evals/                # Golden-file tests
│   ├── exercises/            # Exercise data (download as zip)
│   ├── workflow-recipes/     # Operational playbooks (download as zip)
│   └── references/           # Lookup tables
├── idfa-financial-architect/ # IDFA Financial Architect plugin
│   ├── .claude-plugin/       # Plugin manifest
│   ├── skills/               # 2 domain skills (auto-loaded)
│   ├── evals/                # Two-tier eval harness
│   ├── tests/                # Unit tests
│   └── examples/             # Reference models
├── banking/                  # Banking Regulatory Compliance plugin
│   ├── .claude-plugin/       # Plugin manifest
│   ├── skills/               # 16 product skills (auto-loaded)
│   ├── commands/             # 4 slash commands (auto-loaded)
│   ├── hooks/                # Session + validation hooks (auto-loaded)
│   ├── evals/                # Golden-file tests
│   └── exercises/            # Exercise data (download as zip)
├── legal-ops/                # Legal Operations and Compliance plugin
│   ├── .claude-plugin/       # Plugin manifest
│   ├── skills/               # 9 skills (auto-loaded)
│   ├── commands/             # 4 slash commands (auto-loaded)
│   ├── hooks/                # Session + validation hooks (auto-loaded)
│   ├── scripts/              # Test harness
│   ├── evals/                # Golden-file tests
│   ├── exercises/            # 8 exercises (download as zip)
│   └── workflow-recipes/     # 4 operational playbooks (download as zip)
└── [future plugins...]       # More business domain plugins planned
```

---

## For Learners

Each plugin is a companion to a specific chapter in The AI Agent Factory:

| Plugin                   | Chapter                                     | What You Learn                                                                       |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------ |
| islamic-finance          | Ch 20: Islamic Finance Domain Agents        | Build jurisdiction-aware Islamic finance agents using 3 accounting regimes           |
| idfa-financial-architect | Ch 18: Intent-Driven Financial Architecture | Build audit-proof financial models using Named Ranges, four guardrails, three layers |
| banking                  | Ch 21: Banking Regulatory Compliance        | Build jurisdiction-aware banking regulatory agents for IFRS 9, Basel III/IV, AML/KYC |
| legal-ops                | Ch 22: Legal Operations and Compliance      | Build legal operations agents for contract review, NDA triage, IP protection, DSAR   |

### Downloading Exercise Data

After installing a plugin, download the exercise data:

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download the zip you need:

| Download                                | What's Inside                   | Use With                  |
| --------------------------------------- | ------------------------------- | ------------------------- |
| `islamic-finance-full.zip`              | Everything                      | Complete setup / capstone |
| `islamic-finance-exercise-data.zip`     | 14 exercises + reference tables | Chapter exercises         |
| `islamic-finance-workflow-recipes.zip`  | 4 operational playbooks         | Production workflows      |
| `idfa-financial-architect-full.zip`     | Plugin + examples + evals       | Complete setup            |
| `idfa-financial-architect-examples.zip` | Example models (GP Waterfall)   | Quick start               |
| `banking-full.zip`                      | Everything                      | Complete setup / capstone |
| `legal-ops-full.zip`                    | Everything                      | Complete setup / capstone |
| `legal-ops-exercise-data.zip`           | 8 exercises                     | Chapter exercises         |
| `legal-ops-workflow-recipes.zip`        | 4 operational playbooks         | Production workflows      |

3. Unzip into your project:

```bash
unzip islamic-finance-exercise-data.zip -d my-project/
```

---

## For Other AI Agents

Only Claude Code / Cowork get full plugin functionality (auto-routing, commands, hooks). For other platforms, copy the skill content as custom instructions:

| Agent           | Instructions Path                 | What to Copy                              |
| --------------- | --------------------------------- | ----------------------------------------- |
| GitHub Copilot  | `.github/copilot-instructions.md` | Router SKILL.md + relevant product skills |
| VS Code Copilot | `.vscode/copilot-instructions.md` | Same                                      |
| Cursor          | `.cursorrules`                    | Same                                      |
| Codex           | `AGENTS.md` or system prompt      | Same                                      |

---

## Contributing

This marketplace is maintained by [Panaversity](https://github.com/panaversity). Contributions welcome via pull request.

## License

Repository-level: Apache-2.0 — see [LICENSE](./LICENSE). Individual plugins may have their own license terms (see each plugin's LICENSE file).
