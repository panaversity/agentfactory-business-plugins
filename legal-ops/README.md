# Legal Operations and Compliance

Plugin for **Chapter 22: Legal Operations and Compliance** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Legal Operations and Compliance agent with 8 product skills, 6 jurisdiction overlays, and 4 domain commands covering contract review, NDA triage, IP protection, regulatory monitoring, DSAR management, legal spend analysis, compliance calendar tracking, and contract intake routing across UK, EU, US, Pakistan, UAE, and GCC jurisdictions.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install legal-ops@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "legal-ops"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `legal-ops-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/legal-ops
```

### Verify Installation

Start a new Claude session and say: "I need to review a vendor agreement under English law." The agent should automatically reference UCTA and the three-tier classification system -- if it does, the plugin is active.

---

## What's in This Plugin

```
legal-ops/
├── .claude-plugin/plugin.json         # Plugin manifest
├── skills/                            # 9 skills (auto-loaded by agent)
│   ├── legal-global-router/           # Routes to correct product + jurisdiction
│   │   └── references/jurisdictions/  # 6 jurisdiction overlays (on-demand)
│   ├── contract-review/               # Full clause-by-clause contract review
│   ├── nda-triage/                    # NDA pre-screening and routing
│   ├── ip-protection/                 # Patent, trademark, copyright, OSS
│   ├── regulatory-monitoring/         # Regulatory change tracking
│   ├── dsar-privacy/                  # DSAR/privacy request management
│   ├── legal-spend/                   # External legal spend analysis
│   ├── compliance-calendar/           # Obligation and deadline tracking
│   └── contract-intake-agent/         # End-to-end contract intake
├── commands/                          # 4 slash commands
│   ├── review-contract.md             # /review-contract
│   ├── triage-nda.md                  # /triage-nda
│   ├── vendor-check.md               # /vendor-check
│   └── legal-brief.md                # /legal-brief
├── hooks/hooks.json                   # SessionStart + PostToolUse validation
├── scripts/validate-routing.py        # Routing validation test harness
├── evals/                             # Golden-file tests
├── exercises/                         # 8 exercise files (download as zip)
├── workflow-recipes/                  # 4 operational playbooks (download as zip)
└── legal.local.md.template            # Negotiation playbook -- fill in + rename
```

---

## Commands

| Command            | What It Does                                  | Example                                                             |
| ------------------ | --------------------------------------------- | ------------------------------------------------------------------- |
| `/review-contract` | Full clause-by-clause review against playbook | `/review-contract "SaaS MSA" "English law" "customer, GBP 48K"`     |
| `/triage-nda`      | NDA pre-screening with tier routing           | `/triage-nda "mutual NDA" "tech partner, response by Friday"`       |
| `/vendor-check`    | Obligation tracking and compliance calendar   | `/vendor-check scope:"all contracts" filter:"due in 60 days"`       |
| `/legal-brief`     | Research, regulatory, IP, spend analysis      | `/legal-brief topic:"regulatory monitoring" jurisdictions:"UK, EU"` |

---

## How Each Folder Maps to Chapter 22 Lessons

| Folder                                 | Lessons       | What You Do                                              |
| -------------------------------------- | ------------- | -------------------------------------------------------- |
| `skills/jurisdiction-contract-review/` | Part One      | Jurisdiction-aware contract review against your playbook |
| `skills/jurisdiction-nda-triage/`      | Part Two      | Jurisdiction-aware NDA triage with three-tier routing    |
| `skills/ip-protection/`                | Part Three    | Patent landscape, trademark monitoring, FTO research     |
| `skills/contract-intake-agent/`        | Part Five     | Build the Contract Intake Agent                          |
| `skills/regulatory-monitoring/`        | Part Five     | Build the Regulatory Monitoring Agent                    |
| `skills/compliance-calendar/`          | Part Five     | Build the Compliance Calendar Agent                      |
| `skills/legal-spend/`                  | Part Five     | Build the Legal Spend Analytics Agent                    |
| `skills/dsar-privacy/`                 | Part Five     | Build the DSAR Response Agent                            |
| `skills/legal-global-router/`          | All           | Routing + 6 jurisdiction overlays                        |
| `exercises/`                           | Exercises 1-8 | Hands-on exercise files                                  |
| `workflow-recipes/`                    | Operational   | Production workflow playbooks                            |
| `evals/`                               | Validation    | Golden-file routing and product tests                    |

---

## Customizing for Your Jurisdiction

| Variable             | Default                                             | Your Value              |
| -------------------- | --------------------------------------------------- | ----------------------- |
| Primary Jurisdiction | Multi-jurisdiction (UK, EU, US, Pakistan, UAE, GCC) | _your jurisdiction_     |
| Negotiation Playbook | General commercial standards                        | _your legal.local.md_   |
| NDA Standard Form    | General commercial NDA                              | _your standard form_    |
| IP Marks             | Not configured                                      | _your registered marks_ |
| Escalation Contacts  | Generic roles                                       | _your named contacts_   |

To customize: copy `legal.local.md.template`, rename to `legal.local.md`, and fill in your organisation's positions. To add a jurisdiction: create a new overlay file in `skills/legal-global-router/references/jurisdictions/` following the same format.

---

## Prerequisites

- Chapters 1-21 of The AI Agent Factory
- Claude Code or Cowork access
- Basic understanding of commercial contract concepts

## The Governing Principle

> **The agent reviews, triages, drafts, and flags.**
> **The licensed attorney advises, decides, and signs.**

Every file in this plugin enforces this distinction. Every output ends with: **ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY.**

## License

Apache-2.0 -- see [LICENSE](./LICENSE).
