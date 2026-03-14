# Islamic Finance Domain Agents

Plugin for **Chapter 20: Islamic Finance Domain Agents** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Jurisdiction-aware Islamic finance accounting agent with 12 product skills, 13 jurisdiction overlays, and 4 domain commands covering AAOIFI, IFRS with Islamic guidance, and local standards across 20 jurisdictions.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install islamic-finance@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar → Customize → Browse plugins → + → Add marketplace from GitHub → `panaversity/agentfactory-business-plugins` → Install "islamic-finance"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `islamic-finance-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/islamic-finance
```

### Verify Installation

Start a new Claude session and say: "I have a Bahrain murabaha query." The agent should automatically reference AAOIFI FAS 2 — if it does, the plugin is active.

---

## What's in This Plugin

```
islamic-finance/
├── .claude-plugin/plugin.json        # Plugin manifest
├── skills/                           # 13 skills (auto-loaded by agent)
│   ├── islamic-finance-router/       # Routes to correct product + jurisdiction
│   │   └── references/
│   │       ├── jurisdictions/        # 13 jurisdiction overlays (on-demand)
│   │       ├── aaoifi-fas-reference.md
│   │       └── global-standards-map.md
│   ├── murabaha/                     # Cost-plus financing
│   ├── ijarah-imb/                   # Lease-to-own
│   ├── musharaka-dm/                 # Diminishing partnership
│   ├── mudaraba/                     # Profit-sharing investment
│   ├── musharaka-full/               # Full partnership
│   ├── salam/                        # Forward sale
│   ├── istisna-a/                    # Construction finance
│   ├── sukuk-issuer/                 # Islamic bond (issuer side)
│   ├── sukuk-investor/               # Islamic bond (investor side)
│   ├── takaful-ifrs17/               # Islamic insurance
│   ├── zakat-global/                 # Zakat computation
│   └── shariah-screening-global/     # Equity screening
├── commands/                         # 4 slash commands
│   ├── if-journal.md                 # /if-journal — journal entries + schedules
│   ├── if-compare.md                 # /if-compare — cross-jurisdiction comparison
│   ├── if-screen.md                  # /if-screen — Shariah screening
│   └── if-zakat.md                   # /if-zakat — zakat computation
├── hooks/hooks.json                  # SessionStart + PostToolUse validation
├── scripts/validate-routing.py       # 13-jurisdiction routing test harness
└── evals/                            # Golden-file tests
```

---

## Commands

| Command       | What It Does                         | Example                                              |
| ------------- | ------------------------------------ | ---------------------------------------------------- |
| `/if-journal` | Generate journal entries + schedules | `/if-journal murabaha bahrain "BHD 500K, 18mo, 18%"` |
| `/if-compare` | Compare across jurisdictions         | `/if-compare murabaha bahrain malaysia`              |
| `/if-screen`  | Shariah compliance screening         | `/if-screen sc-malaysia "company data..."`           |
| `/if-zakat`   | Compute zakat                        | `/if-zakat saudi "equity SAR 40B, ..."`              |

---

## How Each Folder Maps to Chapter 20 Lessons

| Folder                             | Lessons | What You Do                                           |
| ---------------------------------- | ------- | ----------------------------------------------------- |
| `skills/murabaha/`                 | L04     | Process murabaha transactions, compare AAOIFI vs MFRS |
| `skills/ijarah-imb/`               | L05     | Ijarah-IMB across 4 jurisdictions                     |
| `skills/sukuk-*/`                  | L06     | Sukuk from issuer and investor perspectives           |
| `skills/takaful-ifrs17/`           | L07     | Takaful with IFRS 17 overlay                          |
| `skills/islamic-finance-router/`   | L08-L11 | Jurisdiction-specific deep dives                      |
| `skills/zakat-global/`             | L12     | Zakat computation across jurisdictions                |
| `skills/shariah-screening-global/` | L13     | Shariah screening methodologies                       |
| `evals/`                           | L17-L18 | Capstone validation                                   |

---

## Customizing for Your Jurisdiction

| Variable              | Default                           | Your Value                   |
| --------------------- | --------------------------------- | ---------------------------- |
| Currency              | Multi-currency (per jurisdiction) | _your currency_              |
| Primary Framework     | AAOIFI / IFRS (auto-detected)     | _your framework_             |
| Regulatory Body       | Per jurisdiction                  | _your regulator_             |
| Zakat Method          | Jurisdiction-specific             | _your method_                |
| Screening Methodology | SC Malaysia                       | _your preferred methodology_ |

To customize: edit the relevant jurisdiction overlay in `skills/islamic-finance-router/references/jurisdictions/` or create a new one following the same format.

---

## Prerequisites

- Chapters 1-19 of The AI Agent Factory (especially Ch18: IDFA Financial Architect)
- Claude Code or Cowork access
- Basic understanding of financial accounting concepts

## License

Apache-2.0 — see [LICENSE](../LICENSE).
