# Legal Operations and Compliance

Plugin for **Chapter 22: Legal Operations and Compliance** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

**1 agent, 6 skills (1 router + 5 products), 6 jurisdiction overlays, 1 playbook template.** Extends Anthropic's built-in Legal Plugin with multi-jurisdiction awareness and domain-specific legal operations workflows across UK, EU, US, Pakistan, UAE, and GCC jurisdictions.

---

## How It Works: Layer 1 + Layer 2

**Layer 1 (Anthropic's Legal Plugin):** 9 built-in commands for contract review, NDA triage, vendor assessment, compliance checks, legal research, risk assessment, meeting prep, legal responses, and e-signatures.

**Layer 2 (This Plugin):** Adds jurisdiction-aware routing, domain-specific product skills, and an orchestration agent that enriches Layer 1 commands with jurisdiction overlays, negotiation playbook context, and pre-check logic.

The router skill sits between user queries and all legal operations -- it identifies the task type, loads the correct jurisdiction overlay, checks for a negotiation playbook, and routes to the appropriate Layer 1 command or activates the relevant product skill with enriched context.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
# Layer 1: Anthropic's base Legal Plugin
claude plugin install legal@knowledge-work-plugins

# Layer 2: Agent Factory jurisdiction extension
/plugin marketplace add panaversity/agentfactory-business-plugins
/plugin install legal-ops@agentfactory-business
```

### Option B: Cowork (Claude.ai)

**Layer 1:** Sidebar -> Customize -> Browse plugins -> Search "Legal" -> Install `knowledge-work-plugins/legal`

**Layer 2:** Sidebar -> Customize -> Browse plugins -> Personal -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "legal-ops"

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
├── .claude-plugin/plugin.json                # v3.0.0 manifest
├── agents/                                   # Orchestrator agent
│   └── contract-intake.md                    # End-to-end contract intake orchestration
├── skills/                                   # Router + product skills
│   ├── legal-global-router/                  # Router skill
│   │   ├── SKILL.md                          # Routing table, NDA pre-checks, playbook logic
│   │   └── references/jurisdictions/         # 6 jurisdiction overlays
│   │       ├── uk-law.md                     # England & Wales
│   │       ├── eu-law.md                     # EU + member state notes
│   │       ├── us-law.md                     # US federal + state
│   │       ├── pakistan-law.md               # Pakistan
│   │       ├── uae-law.md                    # UAE mainland/DIFC/ADGM
│   │       └── gcc-law.md                    # KSA, Bahrain, Kuwait, Oman, Qatar
│   ├── compliance-calendar/                  # Product skill
│   │   └── SKILL.md                          # Obligation tracking + escalation
│   ├── dsar-privacy/                         # Product skill
│   │   └── SKILL.md                          # DSAR 30-day workflow
│   ├── ip-protection/                        # Product skill
│   │   └── SKILL.md                          # Patent/trademark/copyright/OSS
│   ├── legal-spend/                          # Product skill
│   │   └── SKILL.md                          # Spend analytics + anomaly detection
│   └── regulatory-monitoring/                # Product skill
│       └── SKILL.md                          # Weekly regulatory briefing
├── evals/                                    # Golden-file tests
│   ├── routing-golden.json                   # 12 routing test cases
│   ├── product-golden.json                   # 5 product accuracy cases
│   └── run-evals.py                          # Structural validator
├── hooks/hooks.json                          # SessionStart + PostToolUse validation
├── scripts/validate-routing.py               # Routing validation test harness
├── legal.local.md.template                   # Negotiation playbook -- fill in + rename
├── CLAUDE.md                                 # Agent instructions
├── LICENSE                                   # Apache-2.0
└── README.md                                 # This file
```

---

## Agent (1) -- Orchestrator

| Agent             | Purpose                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contract-intake` | Manages end-to-end contract intake: receive, classify, extract metadata, triage via Anthropic commands, route by tier, track SLA, handle post-execution. |

## Skills (6) -- 1 Router + 5 Products

| Skill                   | Purpose                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| `legal-global-router`   | Routing table, jurisdiction overlays, NDA pre-checks, playbook loading. Activates product skills.     |
| `compliance-calendar`   | Obligation tracking, filing deadlines, renewal reminders, escalation sequences, compliance dashboard. |
| `dsar-privacy`          | 30-day DSAR workflow with multi-jurisdiction support (UK GDPR, EU GDPR, CCPA, PIPEDA).                |
| `ip-protection`         | Patent landscape analysis, trademark monitoring, FTO scaffolding, copyright and OSS compliance.       |
| `legal-spend`           | Spend analytics, billing anomaly detection, rate benchmarking, quarterly reporting.                   |
| `regulatory-monitoring` | Weekly regulatory brief with impact classification, monthly board summaries.                          |

## Jurisdiction Overlays (6)

| Overlay           | Covers                                                  |
| ----------------- | ------------------------------------------------------- |
| `uk-law.md`       | UCTA, CRA 2015, UK GDPR, DPA 2018, Bribery Act 2010     |
| `eu-law.md`       | GDPR, EU AI Act, Late Payment Directive, member states  |
| `us-law.md`       | CCPA/CPRA, BIPA, UCC, DTSA, state non-compete rules     |
| `pakistan-law.md` | Contract Act 1872, PDPA 2023, Islamic finance (riba)    |
| `uae-law.md`      | Mainland/DIFC/ADGM dual system, PDPL, Commercial Agency |
| `gcc-law.md`      | KSA PDPL, Bahrain PDPL, Sharia-compliant clauses        |

---

## Customizing for Your Organisation

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
- Anthropic's Legal Plugin installed (Layer 1)
- Basic understanding of commercial contract concepts

## The Governing Principle

> **The agent reviews, triages, drafts, and flags.**
> **The licensed attorney advises, decides, and signs.**

Every file in this plugin enforces this distinction. Every output ends with: **ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY.**

## License

Apache-2.0 -- see [LICENSE](./LICENSE).
