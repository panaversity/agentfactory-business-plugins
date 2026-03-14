# Legal Operations and Compliance

Plugin for **Chapter 22: Legal Operations and Compliance** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

**1 agent, 1 skill (with 5 product reference files), 6 jurisdiction overlays, 1 playbook template.** Extends Anthropic's built-in Legal Plugin with multi-jurisdiction awareness and domain-specific legal operations workflows across UK, EU, US, Pakistan, UAE, and GCC jurisdictions.

---

## How It Works: Layer 1 + Layer 2

**Layer 1 (Anthropic's Legal Plugin):** 9 built-in commands for contract review, NDA triage, vendor assessment, compliance checks, legal research, risk assessment, meeting prep, legal responses, and e-signatures.

**Layer 2 (This Plugin):** Adds jurisdiction-aware routing, domain-specific product knowledge (loaded on demand), and an orchestration agent that enriches Layer 1 commands with jurisdiction overlays, negotiation playbook context, and pre-check logic.

The router skill sits between user queries and all legal operations -- it identifies the task type, loads the correct jurisdiction overlay, checks for a negotiation playbook, and routes to the appropriate Layer 1 command or loads the relevant product reference file with enriched context.

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
├── .claude-plugin/plugin.json                # v3.1.0 manifest
├── agents/                                   # Orchestrator agent
│   └── contract-intake.md                    # End-to-end contract intake orchestration
├── skills/                                   # Domain knowledge
│   └── legal-global-router/                  # Router + all domain knowledge
│       ├── SKILL.md                          # Routing table, NDA pre-checks, playbook logic
│       ├── products/                         # On-demand product reference files
│       │   ├── ip-protection.md              # Patent/trademark/copyright/OSS
│       │   ├── regulatory-monitoring.md      # Weekly regulatory briefing
│       │   ├── dsar-privacy.md               # DSAR 30-day workflow
│       │   ├── legal-spend.md                # Spend analytics + anomaly detection
│       │   └── compliance-calendar.md        # Obligation tracking + escalation
│       └── references/jurisdictions/         # 6 jurisdiction overlays
│           ├── uk-law.md                     # England & Wales
│           ├── eu-law.md                     # EU + member state notes
│           ├── us-law.md                     # US federal + state
│           ├── pakistan-law.md               # Pakistan
│           ├── uae-law.md                    # UAE mainland/DIFC/ADGM
│           └── gcc-law.md                    # KSA, Bahrain, Kuwait, Oman, Qatar
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

## Skill (1) -- Router + Domain Knowledge

| Skill                 | Purpose                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `legal-global-router` | Routing table, jurisdiction overlays, NDA pre-checks, playbook loading. Loads product reference files on demand for domain-specific analysis. |

### Product Reference Files (5)

Loaded on demand by the router when a query matches their domain:

| File                       | Domain                                               |
| -------------------------- | ---------------------------------------------------- |
| `ip-protection.md`         | Patent landscape, trademark watch, FTO scaffolding   |
| `regulatory-monitoring.md` | Weekly regulatory brief with impact assessment       |
| `dsar-privacy.md`          | 30-day DSAR workflow with multi-jurisdiction support |
| `legal-spend.md`           | Spend tracking, anomaly detection, benchmarking      |
| `compliance-calendar.md`   | Filing deadlines, renewals, escalation sequences     |

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
