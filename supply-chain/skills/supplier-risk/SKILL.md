---
name: supplier-risk
description: >
  Activate for: supplier risk, vendor risk, supply risk, risk brief,
  supplier financial risk, supplier operational risk, supplier compliance risk,
  geopolitical risk, Tier 2 risk, sub-supplier, supply disruption, risk monitor,
  risk assessment, risk rating, risk alert, distress signal, supplier news,
  country risk, single source risk, supply chain resilience.
  NOT for: vendor onboarding or classification (use vendor-assessment),
  invoice processing (use invoice-reconciliation), carrier performance
  (use logistics-brief).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/supplier-risk"
  mcp-integrations: "Web Search, Companies House, Creditsafe, ERP, QMS, News APIs"
---

## UNIVERSAL RULES (apply to every risk task)

- NEVER classify a sole-source supplier as low risk based on spend alone --
  always assess operational dependency separately from spend volume
- NEVER accept a vendor risk assessment that contains fabricated financial
  data -- label all estimates and flag where primary data is unavailable
- ALWAYS flag when a vendor's Tier 2 sub-supplier shows distress signals
  that could affect Tier 1 supply continuity
- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Supplier Risk Brief -- Vendor X]
VENDOR TIER:   [Strategic / Tactical / Commodity / Bottleneck / Unclassified]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [Web Search / Creditsafe / ERP / Manual input]
```

## RISK MONITORING WORKFLOW

### Five Risk Dimensions

DIMENSION 1: FINANCIAL RISK
Monitor for:

- Revenue and profitability trend (from annual filings or reported results)
- Credit rating: any downgrade from Creditsafe / D&B / Experian
- Restructuring announcements, CVA, administration proceedings
- DSO trend: lengthening = cash pressure on the vendor
- Ownership changes: acquisition, MBO, private equity involvement
- Key customer losses announced
- Late filing of statutory accounts (itself a distress signal)

Sources: Companies House / SECP / equivalent registry;
Creditsafe / D&B; trade press; web search MCP

Risk levels:
RED HIGH: Restructuring / CVA / credit rating CCC or below / accounts overdue
AMBER MEDIUM: Revenue decline >15% YoY; margin below 3%; rating downgrade 1 notch
GREEN LOW: Stable financials; positive trend; adequate credit rating

DIMENSION 2: OPERATIONAL RISK
Monitor from ERP data (updated continuously):

- OTD rate: 13-week rolling average + trend direction
- Quality rejection rate: 13-week rolling average + trend direction
- Lead time variance: increasing variance = capacity or process strain
- Missed delivery pattern: same day of week? Same product? (capacity signals)
- Partial deliveries increasing? (material shortage signal)

Risk levels:
RED HIGH: OTD < configured critical threshold; quality > critical threshold
AMBER MEDIUM: Declining trend even if above threshold; partial deliveries increasing
GREEN LOW: Stable; above threshold; no adverse trend

DIMENSION 3: REGULATORY & COMPLIANCE RISK
Monitor for:

- Certification expiry (ISO, sector-specific, data protection)
- Regulatory enforcement action (sector regulators, HSE, ICO)
- Environmental incidents (prosecution, fine, site closure risk)
- Trade compliance issues (export licence violations, customs irregularities)
- Sanctions list changes affecting the vendor or their key sub-suppliers

Risk levels:
RED HIGH: Active sanctions match; enforcement action; certification lapsed
AMBER MEDIUM: Certification expiring within 90 days; regulatory warning issued
GREEN LOW: All certifications current; no adverse regulatory signals

DIMENSION 4: GEOPOLITICAL RISK
Monitor for:

- Political instability in vendor's operating country
- Trade restrictions, tariffs, or export controls affecting category
- Currency volatility affecting contract economics
- Infrastructure disruption (port strikes, border closures, natural disaster)
- Conflict affecting supply routes

Sources: web search MCP; UK FCO travel advisories; trade association bulletins

Risk levels:
RED HIGH: Active disruption to supply route or vendor operations
AMBER MEDIUM: Elevated country risk; currency movement >5% since contract
GREEN LOW: Stable environment; no material currency exposure

DIMENSION 5: TIER 2 / SUB-SUPPLIER RISK
Monitor for:

- Financial distress at critical Tier 2 suppliers
- Tier 2 supplier capacity constraints affecting Tier 1 output
- Single-geography concentration at Tier 2 level
- Tier 2 supplier relationship with Tier 1 deteriorating

Requirement: Tier 2 mapping must exist for all Tier 1 Strategic vendors.
If mapping does not exist: flag as UNASSESSED RISK; request Tier 2 data
from Tier 1 supplier as priority action.

### Risk Rating Change Rules

ESCALATE overall rating if ANY dimension reaches RED
ELEVATE to MEDIUM-HIGH if TWO dimensions reach AMBER simultaneously
REDUCE rating only after confirmed remediation (not just vendor assurance)

## RISK BRIEF OUTPUT FORMAT

```
SUPPLIER RISK BRIEF: [Vendor Name]
Assessment date: [Date] | Next scheduled review: [Date]
================================================================
OVERALL RISK RATING: [GREEN LOW / AMBER MEDIUM / AMBER MEDIUM-HIGH / RED HIGH / RED CRITICAL]
Change since last review: [No change / Elevated / Reduced]

FINANCIAL RISK:   [GREEN / AMBER / RED] [Rating]
[Findings and signals with sources and dates]

OPERATIONAL RISK: [GREEN / AMBER / RED] [Rating]
[OTD trend, quality trend, lead time data from ERP]

COMPLIANCE RISK:  [GREEN / AMBER / RED] [Rating]
[Certification status, regulatory findings]

GEOPOLITICAL RISK:[GREEN / AMBER / RED] [Rating]
[Country, currency, route findings]

TIER 2 RISK:      [GREEN / AMBER / RED / NOT MAPPED]
[Sub-supplier findings or mapping gap flag]

RECOMMENDED ACTIONS -- RANKED BY URGENCY
RED [IMMEDIATE -- this week]: [Action] -- [Owner]
AMBER [SHORT-TERM -- 30 days]: [Action] -- [Owner]
GREEN [PLANNED -- 90 days]:    [Action] -- [Owner]
================================================================
```

### Executive Brief Format (for CPO weekly summary)

```
VENDOR RISK SUMMARY -- Week of [Date]
---------------------------------------------------------
[Vendor]    [Overall]  [Change]  [Key signal]   [Action required]
[Vendor]    [Overall]  [Change]  [Key signal]   [Action required]
---------------------------------------------------------
New alerts this week:   [N]
Escalations to CPO:     [N]
Contingency plans live: [N]
```

## NEVER DO THESE

- NEVER rate a vendor as LOW risk in any dimension without verified data --
  absence of negative data does not equal low risk; label as UNASSESSED if no data
- NEVER rely on vendor self-assessment alone for financial risk --
  always cross-reference with independent sources
- NEVER downgrade a risk rating based on vendor assurance alone --
  require evidence (updated accounts, certification renewal, remediation proof)
- NEVER omit the Tier 2 risk section -- mark as NOT MAPPED if absent,
  not LOW RISK
- NEVER wait for the scheduled review to act on a HOT signal --
  HOT signals override the review schedule

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
