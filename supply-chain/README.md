# Supply Chain & Procurement Domain Agents

Plugin for **Chapter 35: Supply Chain & Procurement** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Supply chain and procurement domain agent (v1.0.0) with 8 skills covering vendor assessment, invoice reconciliation, supplier risk monitoring, logistics analysis, spend analytics, network design, vendor communications, and executive briefing. 5 persistent agents for continuous supply chain intelligence. No jurisdiction overlays -- policy-configurable via `supply-chain.local.md`.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install supply-chain@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "supply-chain"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `supply-chain-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/supply-chain
```

### Verify Installation

Start a new Claude session and say: "Assess our strategic vendor Acme Corp -- they are our sole source for packaging materials." The agent should automatically classify the vendor using the Kraljic matrix and run a six-dimension assessment -- if it does, the plugin is active.

---

## What's in This Plugin

```
supply-chain/
├── .claude-plugin/plugin.json        # Plugin manifest (v1.0.0)
├── skills/                           # 8 skills (auto-loaded by agent)
│   ├── vendor-assessment/            # Kraljic classification + 6-dimension assessment
│   ├── supplier-risk/                # 5-dimension risk monitoring
│   ├── invoice-reconciliation/       # 4-stage three-way match workflow
│   ├── vendor-communication/         # 5 communication types (dispute, CAR, exit, etc.)
│   ├── logistics-brief/              # Carrier scorecard, lane analysis, carbon
│   ├── spend-analysis/               # Category spend, consolidation, benchmarking
│   ├── network-design/               # Multi-scenario supply network optimisation
│   └── supply-chain-brief/           # Weekly executive brief + escalation alerts
├── agents/                           # 5 persistent agents
│   ├── vendor-health-monitor.md      # Daily vendor financial/operational scanning
│   ├── invoice-reconciliation-agent.md  # Automated AP inbox processing
│   ├── spend-intelligence-agent.md   # Monthly spend analytics + commodity alerts
│   ├── procurement-calendar-agent.md # Contract renewal + certification tracking
│   └── logistics-intelligence-agent.md  # Carrier SLA monitoring + disruption alerts
├── evals/                            # Eval harness (routing + content checks)
│   ├── cases.yaml                    # 18 test cases
│   └── run.py                        # Deterministic eval runner
└── README.md
```

---

## Commands

| Command                | What It Does                        | Example                                                                          |
| ---------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| `/vendor-assess`       | Vendor classification + assessment  | `/vendor-assess "Acme Corp -- sole-source packaging, GBP 2.1M annual spend"`     |
| `/supplier-risk`       | Supplier risk brief                 | `/supplier-risk "Steel supplier credit downgrade from BB to B-"`                 |
| `/invoice-reconcile`   | Invoice three-way match             | `/invoice-reconcile "INV-2024-0847 vs PO-4521 and GR-9012"`                      |
| `/vendor-communicate`  | Draft vendor communication          | `/vendor-communicate "Invoice dispute -- price variance on INV-2024-0847"`       |
| `/logistics-brief`     | Carrier performance + lane analysis | `/logistics-brief "Q1 carrier scorecard for top 5 carriers"`                     |
| `/spend-analysis`      | Spend analytics + consolidation     | `/spend-analysis "Packaging category -- consolidation opportunities"`            |
| `/supply-network-design` | Network design scenario comparison | `/supply-network-design "Compare UK-only vs UK+Poland DC network"`               |
| `/supply-chain-brief`  | Weekly executive brief              | `/supply-chain-brief "Weekly brief for CPO -- week of 2024-03-18"`               |

---

## Skills by Domain

| Domain                 | Skills                                        | Key Capabilities                                                     |
| ---------------------- | --------------------------------------------- | -------------------------------------------------------------------- |
| **Vendor Management**  | vendor-assessment, vendor-communication       | Kraljic classification, 6-dimension assessment, 5 communication types |
| **Risk Monitoring**    | supplier-risk                                 | 5-dimension risk rating, Tier 2 cascade, escalation rules            |
| **Invoice Processing** | invoice-reconciliation                        | 4-stage workflow, three-way match, exception routing, audit trail    |
| **Logistics**          | logistics-brief, network-design               | Carrier scorecard, lane optimisation, carbon assessment, scenario comparison |
| **Spend Analytics**    | spend-analysis                                | Category overview, consolidation, price consistency, market benchmark |
| **Executive Reporting**| supply-chain-brief                            | Weekly brief, traffic light summary, escalation alerts               |

---

## Agents

| Agent                        | Schedule       | What It Monitors                                           |
| ---------------------------- | -------------- | ---------------------------------------------------------- |
| vendor-health-monitor        | Daily + weekly | Financial news, OTD trends, Tier 2 signals, certifications |
| invoice-reconciliation-agent | On arrival     | AP inbox, three-way match, exception routing               |
| spend-intelligence-agent     | Monthly + weekly triggers | Category spend, price consistency, commodity indices |
| procurement-calendar-agent   | Continuous     | Contract renewals, notice deadlines, certification expiry  |
| logistics-intelligence-agent | Weekly + daily triggers | Carrier SLA, fuel index, disruption news, expedited freight |

---

## MCP Integrations

| MCP Connection                | Used By                                         | Purpose                                           |
| ----------------------------- | ----------------------------------------------- | ------------------------------------------------- |
| ERP                           | All skills and agents                           | PO, GR, vendor master, spend data, OTD metrics   |
| AP system / email inbox       | invoice-reconciliation, invoice-recon agent      | Invoice intake, payment queue                     |
| TMS (Transport Management)    | logistics-brief, logistics-intelligence agent    | Shipment data, carrier performance, lane costs    |
| Web Search                    | supplier-risk, vendor-health-monitor, spend-intelligence | Financial news, commodity indices, disruptions |
| Companies House / Creditsafe  | vendor-assessment, supplier-risk                | Financial filings, credit ratings                 |
| QMS (Quality Management)      | vendor-assessment, vendor-health-monitor        | Quality rejection data                            |
| Contract register             | procurement-calendar agent, supply-chain-brief  | Contract dates, notice periods, certifications    |
| Network optimisation MCP      | network-design                                  | Scenario modelling (FastAPI microservice)         |

---

## Configuration

All configuration is policy-based via `supply-chain.local.md` (no jurisdiction overlays). Copy the template and customise:

```bash
cp supply-chain.local.md.template supply-chain.local.md
```

Key configuration sections:

| Section                    | What to Configure                                           |
| -------------------------- | ----------------------------------------------------------- |
| Vendor classification register | Strategic/Tactical/Commodity/Bottleneck vendors          |
| Tolerance rules            | Price and quantity thresholds by category                    |
| Risk thresholds            | OTD and quality thresholds per vendor tier                   |
| Carrier SLAs               | Approved carriers with contracted OTD and rate              |
| Escalation contacts        | CPO, Finance Director, category managers                    |
| Commodity indices           | Indices to monitor for renegotiation triggers               |
| Contract register          | Vendor contracts with dates and notice periods              |

---

## Evals

Run the eval harness to verify skill routing and content accuracy:

```bash
# List all cases
uv run evals/run.py --list

# Run all cases
uv run evals/run.py

# Run a single case
uv run evals/run.py --case route_vendor_assess_strategic -v

# Run by category
uv run evals/run.py --category routing
```

18 test cases: 8 routing + 8 accuracy + 2 negative (out-of-scope rejection).

---

## Prerequisites

- Chapters 1-34 of The AI Agent Factory (especially Ch 28-34: Business Domain Agents)
- Claude Code or Cowork access
- Understanding of supply chain and procurement concepts

## License

Apache-2.0 -- see [LICENSE](../LICENSE).
