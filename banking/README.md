# Banking Domain Agents

Plugin for **Chapter 21: Banking Domain Agents** from [The AI Agent Factory](https://learn.panaversity.org) by Panaversity.

Jurisdiction-aware banking regulatory agent (v2.0.0) with 17 skills (1 router + 16 products), 7 jurisdiction overlays, 4 commands, hooks, and eval harness covering IFRS 9 ECL, Basel III/IV capital and liquidity, AML/KYC/sanctions compliance, and bank reconciliation across UK, EU, US, Australia, Singapore, UAE, and Pakistan.

---

## Quick Start

### Option A: Claude Code CLI (Recommended)

```bash
claude plugin install banking@agentfactory-business
```

### Option B: Cowork (Claude.ai)

Sidebar -> Customize -> Browse plugins -> + -> Add marketplace from GitHub -> `panaversity/agentfactory-business-plugins` -> Install "banking"

### Option C: Download ZIP

1. Go to the [Releases page](https://github.com/panaversity/agentfactory-business-plugins/releases/latest)
2. Download `banking-full.zip`
3. Unzip and follow setup instructions

### Option D: Clone for Development

```bash
git clone https://github.com/panaversity/agentfactory-business-plugins.git
claude --plugin-dir ./agentfactory-business-plugins/banking
```

### Verify Installation

Start a new Claude session and say: "I have a UK IFRS 9 ECL query for a mortgage portfolio." The agent should automatically reference IFRS 9 staging rules and UK PRA requirements -- if it does, the plugin is active.

---

## What's in This Plugin

```
banking/
├── .claude-plugin/plugin.json        # Plugin manifest (v2.0.0)
├── skills/                           # 17 skills (auto-loaded by agent)
│   ├── banking-global-router/        # Routes to correct product + jurisdiction
│   │   └── references/              # Regulatory map, SA risk weights, jurisdictions
│   │       ├── regulatory-map.md
│   │       ├── sa-risk-weight-table.md
│   │       └── jurisdictions/        # 7 jurisdiction overlays (on-demand)
│   ├── ifrs9-ecl/                    # Expected credit loss calculation
│   ├── ifrs9-staging/                # Stage 1/2/3 assessment
│   ├── ifrs9-scenarios/              # Macroeconomic scenario framework
│   ├── ifrs9-disclosure/             # IFRS 7 disclosure drafting
│   ├── basel-capital/                # Capital ratios and buffers
│   ├── basel-rwa-credit/             # Credit risk RWA (SA + IRB)
│   ├── basel-rwa-market/             # Market risk RWA (FRTB)
│   ├── liquidity-lcr/                # Liquidity Coverage Ratio
│   ├── liquidity-nsfr/               # Net Stable Funding Ratio
│   ├── stress-testing/               # ICAAP and stress test framework
│   ├── aml-typologies/               # 20 AML typologies with detection logic
│   ├── aml-sar-drafting/             # SAR/STR drafting by jurisdiction
│   ├── aml-cdd-edd/                  # CDD, EDD, PEP, beneficial ownership
│   ├── sanctions-screening/          # OFAC, OFSI, EU sanctions, 50% rule
│   ├── kyc-risk-rating/              # 4-dimension KYC risk scoring
│   └── bank-reconciliation/          # Nostro, suspense, provision recon
├── commands/                         # 4 slash commands
│   ├── banking-ecl.md                # /banking-ecl -- ECL calculation
│   ├── banking-capital.md            # /banking-capital -- capital ratio check
│   ├── banking-aml.md                # /banking-aml -- AML alert analysis
│   └── banking-recon.md              # /banking-recon -- reconciliation
├── hooks/hooks.json                  # SessionStart + PostToolUse hooks
├── scripts/validate-routing.py       # CI routing validation
├── evals/                            # Eval harness (routing + content checks)
├── CLAUDE.md                         # Agent instructions
└── README.md
```

---

## Commands

| Command            | What It Does             | Example                                                       |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `/banking-ecl`     | Calculate IFRS 9 ECL     | `/banking-ecl uk "Retail mortgage, GBP 250K, LTV 75%, BB+"`   |
| `/banking-capital` | Capital ratio assessment | `/banking-capital uk "CET1 285M, AT1 45M, T2 60M, RWA 4.5B"`  |
| `/banking-aml`     | AML alert analysis + SAR | `/banking-aml uk "Structuring alert: 5 deposits GBP 8K each"` |
| `/banking-recon`   | Bank reconciliation      | `/banking-recon nostro "USD nostro with JPMorgan, 7 entries"` |

---

## Skills by Domain

| Domain             | Skills                                                                              | Key Capabilities                                                         |
| ------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **IFRS 9 ECL**     | ifrs9-ecl, ifrs9-staging, ifrs9-scenarios, ifrs9-disclosure                         | Stage assessment, ECL calculation, scenario weighting, IFRS 7 disclosure |
| **Basel Capital**  | basel-capital, basel-rwa-credit, basel-rwa-market                                   | CET1/T1/TC ratios, SA risk weights, FRTB, output floor, MDA              |
| **Liquidity**      | liquidity-lcr, liquidity-nsfr                                                       | HQLA, run-off rates, LCR/NSFR calculation                                |
| **Stress Testing** | stress-testing                                                                      | ICAAP, capital depletion, reverse stress test                            |
| **AML/KYC**        | aml-typologies, aml-sar-drafting, aml-cdd-edd, sanctions-screening, kyc-risk-rating | 20 typologies, SAR drafting, CDD/EDD, sanctions, risk rating             |
| **Reconciliation** | bank-reconciliation                                                                 | Nostro, suspense, IFRS 9 four-way, GL-to-risk                            |

---

## Jurisdictions

| Jurisdiction | Overlay        | Key Regulators               |
| ------------ | -------------- | ---------------------------- |
| UK           | uk-pra         | PRA, FCA, NCA                |
| EU           | eu-crr         | ECB, EBA, national FIUs      |
| USA          | us-federal     | Fed, OCC, FDIC, FinCEN, OFAC |
| Australia    | australia-apra | APRA, AUSTRAC                |
| Singapore    | singapore-mas  | MAS                          |
| UAE          | uae-cbuae      | CBUAE, DFSA, FSRA            |
| Pakistan     | pakistan-sbp   | SBP, FMU                     |

---

## Customizing for Your Jurisdiction

| Variable          | Default                            | Your Value       |
| ----------------- | ---------------------------------- | ---------------- |
| Primary Framework | IFRS 9 / Basel III (auto-detected) | _your framework_ |
| Regulatory Body   | Per jurisdiction                   | _your regulator_ |
| Capital Buffers   | Per jurisdiction                   | _your CCyB rate_ |
| AML Filing System | Per jurisdiction                   | _your FIU_       |

To customize: edit the relevant jurisdiction overlay in `skills/banking-global-router/references/jurisdictions/` or create a new one following the same format.

---

## Prerequisites

- Chapters 1-20 of The AI Agent Factory (especially Ch18: IDFA Financial Architect and Ch20: Islamic Finance)
- Claude Code or Cowork access
- Understanding of banking regulatory concepts (IFRS 9, Basel III, AML)

## License

Apache-2.0 -- see [LICENSE](../LICENSE).
