# HR Operations Domain Agents

Plugin for **Chapter 37: People & HR** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

HR operations domain agent (v1.0.0) with 5 skills covering job descriptions, talent matching, institutional knowledge capture, reference letters, and offboarding. 4 persistent agents for knowledge base Q&A, onboarding orchestration, policy maintenance, and departure knowledge capture. No jurisdiction overlays -- policy-configurable via `hr.local.md`.

Complements the official `human-resources` plugin (9 skills). Zero naming collisions. Install both for the complete Chapter 37 experience.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install hr-operations@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "hr-operations"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `hr-operations-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/hr-operations
```

### Verify Installation

Start a new Claude session and say: "Write a job description for a Senior Data Analyst." The agent should automatically produce a structured JD with inclusive language check, candidate-first perspective, and calibrated requirements -- if it does, the plugin is active.

---

## What's in This Plugin

```
hr-operations/
├── .claude-plugin/plugin.json        # Plugin manifest (v1.0.0)
├── skills/                           # 5 skills (auto-loaded by agent)
│   ├── jd/                           # Job descriptions with inclusive language
│   ├── match/                        # Internal talent matching and succession
│   ├── knowledge/                    # Institutional knowledge capture
│   ├── reference/                    # Reference letters and employment verification
│   └── offboard/                     # Offboarding processes and knowledge transfer
├── agents/                           # 4 persistent agents
│   ├── knowledge-base-agent.md       # 24/7 employee HR Q&A with escalation
│   ├── onboarding-orchestrator.md    # New hire workflow (T-14 to Day 90)
│   ├── policy-maintenance-agent.md   # Monthly policy currency + statutory rates
│   └── offboarding-knowledge-agent.md # Departure knowledge capture automation
├── evals/                            # Eval harness (routing + content checks)
│   ├── cases.yaml                    # 14 test cases
│   └── run.py                        # Deterministic eval runner
├── hr.local.md.template              # Organisation configuration template
├── README.md
└── LICENSE
```

---

## Commands

| Command      | What It Does                                | Example                                                              |
| ------------ | ------------------------------------------- | -------------------------------------------------------------------- |
| `/jd`        | Job description with inclusive language     | `/jd "Senior Data Analyst, Analytics team, GBP 55-65K"`              |
| `/match`     | Internal talent assessment and succession   | `/match "Assess Zara and Ahmed for Team Lead vacancy"`               |
| `/knowledge` | Institutional knowledge capture plan        | `/knowledge "Senior PM leaving in 6 weeks, 8 years tenure"`          |
| `/reference` | Reference letter or employment verification | `/reference "Factual reference for Bilal Ahmed, 3 years as Analyst"` |
| `/offboard`  | Offboarding plan with handover structure    | `/offboard "Sarah resigned, 4 weeks notice, Marketing Manager"`      |

---

## Relationship to Official Plugin

This plugin **complements** the official `human-resources` plugin. Zero naming collisions -- install both for full coverage.

| Function                    | Official Plugin        | This Plugin (hr-operations) |
| --------------------------- | ---------------------- | --------------------------- |
| Policy lookup               | `/policy-lookup`       | --                          |
| Onboarding plans            | `/onboarding`          | --                          |
| Offer letters               | `/draft-offer`         | --                          |
| Interview questions         | `/interview-prep`      | --                          |
| Performance reviews         | `/performance-review`  | --                          |
| Compensation analysis       | `/comp-analysis`       | --                          |
| Org planning                | `/org-planning`        | --                          |
| People analytics            | `/people-report`       | --                          |
| Recruiting pipeline         | `/recruiting-pipeline` | --                          |
| Job descriptions            | --                     | `/jd`                       |
| Internal talent matching    | --                     | `/match`                    |
| Knowledge capture           | --                     | `/knowledge`                |
| Reference letters           | --                     | `/reference`                |
| Offboarding                 | --                     | `/offboard`                 |
| HR Q&A agent                | --                     | knowledge-base-agent        |
| Onboarding automation       | --                     | onboarding-orchestrator     |
| Policy maintenance          | --                     | policy-maintenance-agent    |
| Departure knowledge capture | --                     | offboarding-knowledge-agent |

---

## Skills by Domain

| Domain                   | Skills    | Key Capabilities                                                  |
| ------------------------ | --------- | ----------------------------------------------------------------- |
| **Talent Acquisition**   | jd        | Candidate-first JDs, inclusive language, requirements calibration |
| **Talent Management**    | match     | 6-dimension assessment, readiness classification, succession      |
| **Knowledge Management** | knowledge | Risk scoring, 3-session methodology, knowledge articles           |
| **Employment Records**   | reference | 3 reference types, policy compliance, legal risk awareness        |
| **Employee Lifecycle**   | offboard  | 4-phase offboarding, handover plans, exit interviews              |

---

## Agents

| Agent                       | Schedule                               | What It Monitors                                       |
| --------------------------- | -------------------------------------- | ------------------------------------------------------ |
| knowledge-base-agent        | Always-on                              | Employee policy queries, escalation routing, gaps      |
| onboarding-orchestrator     | Event-triggered (HRIS new hire)        | Pre-boarding, compliance training, 30/60/90 milestones |
| policy-maintenance-agent    | Monthly (1st Monday) + event-triggered | Policy currency, statutory rates, consistency, links   |
| offboarding-knowledge-agent | Event-triggered (HRIS resignation)     | Knowledge risk, capture sessions, completion reports   |

---

## Configuration

All configuration is policy-based via `hr.local.md` (no jurisdiction overlays). Copy the template and customise:

```bash
cp hr.local.md.template hr.local.md
```

Key configuration sections:

| Section                  | What to Configure                                      |
| ------------------------ | ------------------------------------------------------ |
| Organisation Profile     | Company name, size, jurisdiction, legal counsel        |
| Statutory Rates          | UK NLW/SSP/SMP, Pakistan minimum wages, UAE gratuity   |
| Policy Library           | All HR policies with locations, owners, review dates   |
| Leave Entitlements       | Annual, sick, parental, compassionate, study leave     |
| Benefits Summary         | Pension, health, EAP, L&D budget                       |
| HR Contact Directory     | Named contacts for escalation routing                  |
| Onboarding Programme     | IT profiles, access matrix, training, buddy programme  |
| Performance Review Cycle | Frequency, rating scale, promotion cycle               |
| Equal Opportunities      | Standard statement for JDs and offer letters           |
| Reference Policy         | Factual only vs. opinion, who provides, rehire process |
| Data Retention           | Retention periods by document type                     |

---

## Evals

Run the eval harness to verify skill routing and content accuracy:

```bash
# List all cases
uv run evals/run.py --list

# Run all cases
uv run evals/run.py

# Run a single case
uv run evals/run.py --case route_jd_basic -v

# Run by category
uv run evals/run.py --category routing
```

14 test cases: 12 routing + 2 negative (out-of-scope rejection).

---

## Prerequisites

- Chapters 1-36 of The AI Agent Factory (especially Ch 28-36: Business Domain Agents)
- Claude Code or Cowork access
- Official `human-resources` plugin installed (for full Chapter 37 experience)

## License

Apache-2.0 -- see [LICENSE](./LICENSE).
