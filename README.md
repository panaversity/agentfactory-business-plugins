# Agent Factory — Business Domain Plugins

Marketplace for business domain agent plugins from **[The AI Agent Factory](https://learn.panaversity.org)** by Panaversity — Part 3: Business Domain Agent Workflows.

---

## Available Plugins

| Plugin | Description | Version | Install |
|--------|-------------|---------|---------|
| **[islamic-finance](./islamic-finance/)** | 12 product skills, 13 jurisdiction overlays, 4 domain commands for Islamic finance accounting across AAOIFI, IFRS, and local standards | v2.0.0 | `claude plugin install islamic-finance@agentfactory-business` |

---

## Quick Start

### Option A: Install via Claude Code CLI (Recommended)

```bash
# Install a plugin
claude plugin install islamic-finance@agentfactory-business

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
└── [future plugins...]       # Ch18, Ch19 plugins planned
```

---

## For Learners

Each plugin is a companion to a specific chapter in The AI Agent Factory:

| Plugin | Chapter | What You Learn |
|--------|---------|---------------|
| islamic-finance | Ch 20: Islamic Finance Domain Agents | Build jurisdiction-aware Islamic finance agents using 3 accounting regimes |

### Downloading Exercise Data

After installing a plugin, download the exercise data:

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download the zip you need:

| Download | What's Inside | Use With |
|----------|--------------|----------|
| `islamic-finance-full.zip` | Everything | Complete setup / capstone |
| `islamic-finance-exercise-data.zip` | 14 exercises + reference tables | Chapter exercises |
| `islamic-finance-workflow-recipes.zip` | 4 operational playbooks | Production workflows |

3. Unzip into your project:

```bash
unzip islamic-finance-exercise-data.zip -d my-project/
```

---

## For Other AI Agents

Only Claude Code / Cowork get full plugin functionality (auto-routing, commands, hooks). For other platforms, copy the skill content as custom instructions:

| Agent | Instructions Path | What to Copy |
|-------|------------------|-------------|
| GitHub Copilot | `.github/copilot-instructions.md` | Router SKILL.md + relevant product skills |
| VS Code Copilot | `.vscode/copilot-instructions.md` | Same |
| Cursor | `.cursorrules` | Same |
| Codex | `AGENTS.md` or system prompt | Same |

---

## Contributing

This marketplace is maintained by [Panaversity](https://github.com/panaversity). Contributions welcome via pull request.

## License

Apache-2.0 — see [LICENSE](./LICENSE).
