# Sales, RevOps & Marketing

Plugin for **Chapter 23: Sales, RevOps & Marketing** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Sales, RevOps & Marketing agent with 14 product skills, 5 autonomous agents, and 4 jurisdiction overlays covering prospect research, lead scoring, CRM enrichment, outreach, sequences, pipeline analysis, content creation, campaign planning, copywriting, performance analysis, and revenue reporting across US, EU, Pakistan, and GCC jurisdictions.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install sales-revops-marketing@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "sales-revops-marketing"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `sales-revops-marketing-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/sales-revops-marketing
```

### Verify Installation

Start a new Claude session and say: "I need to research a prospect at Meridian Logistics before my discovery call." The agent should automatically reference prospect research, ICP matching, and the Five Laws of Outreach -- if it does, the plugin is active.

---

## What's in This Plugin

```
sales-revops-marketing/
├── .claude-plugin/plugin.json          # Plugin manifest
├── skills/                             # 15 skills (14 product + 1 router)
│   ├── sales-marketing-global-router/  # Routes to correct skill + jurisdiction
│   │   └── references/jurisdictions/   # 4 jurisdiction overlays (on-demand)
│   ├── prospect-research/              # Deep prospect and account intelligence
│   ├── lead-scoring/                   # Three-dimension lead scoring
│   ├── crm-enrichment/                 # CRM record enrichment
│   ├── outreach/                       # Personalised outreach drafting
│   ├── sequence/                       # Multi-touch sequence generation
│   ├── pre-call-brief/                 # Pre-call and deal health briefs
│   ├── follow-up/                      # Post-meeting follow-up emails
│   ├── pipeline/                       # Pipeline analysis and forecasting
│   ├── content-creation/               # Content in all formats
│   ├── campaign-planning/              # Campaign brief and strategy
│   ├── copywriting/                    # Ad copy, subject lines, CTAs
│   ├── performance-analysis/           # Channel and campaign analytics
│   ├── content-calendar/               # Publishing schedule and calendar
│   └── persona-icp/                    # ICP and buyer persona development
├── agents/                             # 5 autonomous agents
│   ├── lead-intelligence-agent.md      # HOT signal monitoring
│   ├── crm-hygiene-agent.md            # Automated CRM enrichment
│   ├── outreach-sequencing-agent.md    # Sequence management
│   ├── marketing-performance-agent.md  # Weekly analytics
│   └── revenue-reporting-agent.md      # Pipeline and forecast dashboard
└── sales-marketing.local.md.template   # ICP + brand config -- fill in + rename
```

---

## How Each Folder Maps to Chapter 23 Lessons

| Folder                                  | Lessons    | What You Do                              |
| --------------------------------------- | ---------- | ---------------------------------------- |
| `skills/prospect-research/`             | Part One   | Research prospects, build account briefs |
| `skills/lead-scoring/`                  | Part One   | Score and qualify leads                  |
| `skills/outreach/`                      | Part Two   | Draft personalised outreach messages     |
| `skills/sequence/`                      | Part Two   | Build multi-touch sequences              |
| `skills/pipeline/`                      | Part Three | Analyse pipeline, forecast revenue       |
| `skills/content-creation/`              | Part Four  | Create marketing content in all formats  |
| `skills/campaign-planning/`             | Part Four  | Plan and budget campaigns                |
| `agents/lead-intelligence-agent`        | Part Five  | Build the Lead Intelligence Agent        |
| `agents/crm-hygiene-agent`              | Part Five  | Build the CRM Hygiene Agent              |
| `agents/outreach-sequencing-agent`      | Part Five  | Build the Outreach Sequencing Agent      |
| `agents/marketing-performance-agent`    | Part Five  | Build the Marketing Performance Agent    |
| `agents/revenue-reporting-agent`        | Part Five  | Build the Revenue Reporting Agent        |
| `skills/sales-marketing-global-router/` | All        | Routing + 4 jurisdiction overlays        |

---

## Customizing for Your Organisation

| Variable         | Default                      | Your Value            |
| ---------------- | ---------------------------- | --------------------- |
| ICP Definition   | General B2B                  | _your ICP_            |
| Brand Voice      | Direct, practical, no jargon | _your brand voice_    |
| Persona Profiles | Not configured               | _your buyer personas_ |
| Competitor Intel | Not configured               | _your competitors_    |
| CRM System       | Not configured               | _your CRM_            |
| Pipeline Stages  | Not configured               | _your stages_         |

To customize: copy `sales-marketing.local.md.template`, rename to `sales-marketing.local.md`, and fill in your organisation's ICP, personas, brand voice, and competitors.

---

## Prerequisites

- Chapters 1-22 of The AI Agent Factory
- Claude Code or Cowork access
- Basic understanding of sales and marketing operations

## The Governing Principle

> **The agent researches, drafts, and recommends.**
> **The sales professional decides and sends.**

Every file in this plugin enforces this distinction. Every outreach output ends with: **ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING.**

## License

Apache-2.0 -- see [LICENSE](./LICENSE).
