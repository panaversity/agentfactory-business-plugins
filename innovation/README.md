# Innovation & Intrapreneurship Domain Agents

Plugin for **Chapter 40: Intrapreneurship & Innovation Agents** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Innovation and intrapreneurship domain agent (v1.0.0) with 10 skills covering the full DLA Stack -- Design Thinking, Lean Startup, and Agile -- and 4 persistent agents for continuous innovation intelligence. Policy-configurable via `innov.local.md`.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install innovation@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "innovation"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `innovation-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/innovation
```

### Verify Installation

Start a new Claude session and say: "I am starting a new venture for AP automation. Help me generate 100 ideas." The agent should automatically use the /idea skill with the 10-category framework -- if it does, the plugin is active.

---

## What's in This Plugin

```
innovation/
├── .claude-plugin/plugin.json        # Plugin manifest (v1.0.0)
├── skills/                           # 10 skills (auto-loaded by agent)
│   ├── idea/                         # 100-idea sprint, DVF scoring, pressure testing
│   ├── discovery/                    # Interview guides, synthesis, JTBD mapping, HMW
│   ├── hypothesis/                   # Assumption mapping, MVP design, validation plans
│   ├── canvas/                       # Business Model Canvas build, stress test, alternatives
│   ├── financials/                   # Unit economics, 3-scenario models, Series A readiness
│   ├── pitch/                        # 9-slide narrative, hard Q&A prep, investor briefs
│   ├── sprint/                       # Innovation sprint planning, backlog prioritisation
│   ├── market/                       # Competitive landscape, bottom-up sizing, moat assessment
│   ├── gtm/                          # ICP definition, channel strategy, 90-day calendar
│   └── validate/                     # Build-Measure-Learn analysis, pivot framework
├── agents/                           # 4 persistent agents
│   ├── idea-generator.md             # Weekly Innovation Briefs + on-demand ideation
│   ├── customer-intelligence.md      # Customer Signal Digests + churn/NPS analysis
│   ├── business-model-architect.md   # Monthly Financial Health Reviews + canvas updates
│   └── fundraising-readiness.md      # Investor pipeline tracking + meeting prep
├── local.md.template                 # innov.local.md configuration template
├── evals/                            # Eval harness (routing + content checks)
│   ├── cases.yaml                    # 26 test cases
│   └── run.py                        # Deterministic eval runner
├── README.md
└── LICENSE
```

---

## Commands

| Command       | What It Does                             | Example                                                                |
| ------------- | ---------------------------------------- | ---------------------------------------------------------------------- |
| `/idea`       | Idea generation + DVF scoring            | `/idea "100 ideas for AP automation for mid-market CFOs"`              |
| `/discovery`  | Customer discovery + synthesis           | `/discovery "Generate interview guide for CFOs at $5M-$50M companies"` |
| `/hypothesis` | Assumption mapping + MVP design          | `/hypothesis "Build assumption map for AP automation SaaS"`            |
| `/canvas`     | Business Model Canvas                    | `/canvas "Build BMC for AP automation venture"`                        |
| `/financials` | Unit economics + financial modelling     | `/financials "Calculate unit economics: $500 MRR, 10% churn"`          |
| `/pitch`      | Investor pitch narrative                 | `/pitch "Build 9-slide pitch for $500K seed raise"`                    |
| `/sprint`     | Innovation sprint planning               | `/sprint "Plan 2-week sprint to validate WhatsApp adoption"`           |
| `/market`     | Competitive intelligence + market sizing | `/market "Competitive landscape scan for AP automation"`               |
| `/gtm`        | Go-to-market strategy                    | `/gtm "Define ICP and 90-day plan for first 10 customers"`             |
| `/validate`   | Build-Measure-Learn analysis             | `/validate "Analyse 6-week pilot results -- should we pivot?"`         |

---

## The DLA Stack

The plugin follows the **DLA Stack** progression -- Design Thinking, Lean Startup, Agile -- applied in order:

```
DESIGN THINKING (Problem Level)     LEAN STARTUP (Solution Level)     AGILE (Delivery Level)
─────────────────────────────       ──────────────────────────────    ────────────────────────
/discovery → /idea                  /hypothesis → /validate           /sprint
                                    /canvas → /financials
                                    /market → /gtm → /pitch
```

Each skill includes **stage-aware calibration** that warns if you are skipping ahead in the DLA progression. For example, `/financials` at the IDEA stage warns that you lack data for reliable modelling.

---

## Agents

| Agent                    | Schedule                    | What It Does                                                    |
| ------------------------ | --------------------------- | --------------------------------------------------------------- |
| idea-generator           | Weekly (Monday) + on-demand | Innovation Briefs with 3 ideas, market signals, provocations    |
| customer-intelligence    | Weekly (Monday) + on-demand | Customer Signal Digests, churn analysis, persona maintenance    |
| business-model-architect | Monthly + trigger-based     | Financial Health Reviews, canvas version updates, runway alerts |
| fundraising-readiness    | Weekly (during fundraising) | Investor pipeline tracking, meeting prep, pitch practice        |

---

## Configuration

All configuration is policy-based via `innov.local.md`. Copy the template and customise:

```bash
cp local.md.template innov.local.md
```

Key configuration sections:

| Section               | What to Configure                                           |
| --------------------- | ----------------------------------------------------------- |
| venture               | Name, stage, type, problem statement, target customer       |
| key_assumptions       | Full assumption stack with IDs, risk, evidence, test status |
| customer_profiles     | Personas with JTBD, pains, gains, WTP, buying process       |
| business_model_canvas | 9 blocks with evidence quality                              |
| financial_model       | Unit economics, current state, milestones                   |
| competitive_landscape | Competitors, alternatives, differentiation, moat            |
| fundraising           | Current round, investor pipeline, data room status          |
| intrapreneurship      | Parent org, sponsor, approval pathway, internal constraints |

---

## Evals

Run the eval harness to verify skill routing and content accuracy:

```bash
# List all cases
uv run evals/run.py --list

# Run all cases
uv run evals/run.py

# Run a single case
uv run evals/run.py --case route_idea_generation -v

# Run by category
uv run evals/run.py --category routing
```

26 test cases: 20 routing (2 per skill) + 5 accuracy + 6 negative (DLA progression + scope control).

---

## Works With

| Tool / Platform          | How                                                      |
| ------------------------ | -------------------------------------------------------- |
| Claude Code CLI          | `claude plugin install innovation@agentfactory-business` |
| Cowork (Claude.ai)       | Install from marketplace; use commands in chat           |
| innov.local.md           | Venture context file -- personalises all skill outputs   |
| Other innovation plugins | Compatible with supply-chain, banking, legal-ops plugins |

---

## Prerequisites

- Chapters 1-39 of The AI Agent Factory (especially Ch 25-39: Business Domain Agents)
- Claude Code or Cowork access
- Understanding of innovation and startup methodology concepts

## License

Apache-2.0 -- see [LICENSE](../LICENSE).
