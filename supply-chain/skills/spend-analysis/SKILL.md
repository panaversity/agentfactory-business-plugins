---
name: spend-analysis
description: >
  Activate for: spend analysis, spend analytics, procurement spend, category
  spend, vendor consolidation, supplier consolidation, price consistency,
  price benchmark, market benchmark, RFQ strategy, spend report, category
  management, tail spend, maverick spend, buying compliance, savings pipeline,
  identified savings, cost reduction, procurement ROI, spend by category,
  spend by vendor, spend by site.
  NOT for: invoice reconciliation (use invoice-reconciliation), vendor risk
  assessment (use supplier-risk), carrier performance (use logistics-brief).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/spend-analysis"
  mcp-integrations: "ERP, finance system, procurement system, web search"
---

## UNIVERSAL RULES (apply to every spend task)

- NEVER accept a vendor risk assessment that contains fabricated financial
  data -- label all estimates and flag where primary data is unavailable
- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Category Spend Overview -- Packaging -- FY2024]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [ERP / Finance system / Web search]
```

## SPEND ANALYSIS WORKFLOW

### Three Strategic Questions Spend Analytics Answers

Question 1: WHO are we actually buying from?
  -> Vendor concentration analysis; consolidation opportunity identification

Question 2: WHAT are we paying?
  -> Price consistency across sites/BUs; contract compliance monitoring

Question 3: WHAT SHOULD we be paying?
  -> Market benchmarking; renegotiation trigger identification

### Analysis Types

#### Type 1: Category Spend Overview

DATA FROM ERP (define period: typically last 12 months):
- Total spend by category (top level and sub-category)
- Spend by vendor within each category
- Spend by business unit / site / cost centre
- PO compliance: what % of spend had a PO before the invoice?

OUTPUT:

```
CATEGORY SPEND OVERVIEW -- [Period]
================================================================
TOTAL SPEND ANALYSED: [X]

TOP CATEGORIES BY SPEND:
[Category]: [X] | [N] vendors | [N] BUs buying | PO compliance: [X]%

TAIL SPEND ALERT:
[X]% of spend is with vendors who each represent <0.5% of total spend.
[N] vendors account for [X]% of total spend.
Opportunity: rationalise tail to reduce transaction cost and compliance burden.

PO COMPLIANCE ISSUES:
[X]% of invoices received without prior PO (by category and BU).
Non-compliant spend: [X] -- escalate to Finance and Procurement leadership.
================================================================
```

#### Type 2: Vendor Consolidation Analysis

TARGET: categories with >3 vendors where commodity characteristics suggest
consolidation would deliver price advantage without unacceptable supply risk.

CONSOLIDATION CANDIDATE CRITERIA:
  - Multiple vendors supplying same specification / same category
  - No strategic reason for multiple sources (i.e. not deliberate dual-sourcing)
  - Combined volume would be meaningful to a single preferred vendor
  - Competitive market with multiple qualified alternatives

CONSOLIDATION OUTPUT (per candidate category):

```
CONSOLIDATION ANALYSIS: [Category]
---------------------------------------------------------
Current state:
  Vendors:       [N] active vendors
  Total spend:   [X]
  Price range:   [low] -- [high] per [unit] -- [X]% variance
  Price winner:  [Vendor at lowest price] at [X] per unit

Consolidated state:
  Target vendor(s): [1 or 2 preferred suppliers recommended]
  Combined volume:  [X]
  Target saving:    [X]% discount estimated at consolidated volume
  Annual saving:    [X] -- [X] (range based on discount range)

Risk assessment:
  Supply continuity: [Single source risk? Mitigation?]
  Switching effort:  [Qualification, trials, tooling -- estimate]

Recommendation: [PROCEED / PROCEED WITH DUAL-SOURCE / MONITOR]
---------------------------------------------------------
```

#### Type 3: Price Consistency Check

IDENTIFY: same item or specification being purchased at different prices
by different business units or sites.

DETECT WHEN:
  - Same vendor code, same item code, different unit price
  - Same item description, different vendor, significantly different price
  - Same contract but different sites paying different prices

PRICE CONSISTENCY OUTPUT:

```
PRICE INCONSISTENCY REPORT -- [Category] -- [Period]
---------------------------------------------------------
Item:            [Description and specification]
Vendor:          [Vendor name]

Site/BU         Price paid    Volume    Annual spend
[Site A]        [X]           [N units] [X]
[Site B]        [Y]           [N units] [X]
[Site C]        [Z]           [N units] [X]

Price variance:  [X]% between highest and lowest
Best rate:       [X] (Site [X])
Saving if all aligned to best rate: [X]/year

Action: Issue group pricing directive; notify all sites of best rate;
require contract compliance from [date]
---------------------------------------------------------
```

#### Type 4: Market Benchmark

USE WEB SEARCH MCP to identify:
- Published market price indices (commodity categories)
- Trade association price surveys (sector-specific)
- Publicly available tender results (public sector categories)
- Analyst market reports (technology, energy, logistics)

BENCHMARK OUTPUT:

```
MARKET BENCHMARK: [Category/Item]
---------------------------------------------------------
Your current price:   [X] per [unit]
Market range:         [low] -- [high] per [unit]
Your position:        [X]% above / below market midpoint
Data source:          [Specify source and date -- never fabricate]
Data quality:         [HIGH -- published index / MEDIUM -- survey /
                       LOW -- estimate only]

IF ABOVE MARKET: Renegotiation recommended
  Estimated saving:   [X]% -- [X]/year at current volume
  Timing:             [Contract renewal date or next review]
  Leverage:           [Market evidence + volume commitment]
---------------------------------------------------------
```

### Savings Pipeline Format

```
PROCUREMENT SAVINGS PIPELINE -- [Date]
================================================================
IDENTIFIED OPPORTUNITIES:
[Category]  [Type]          [Est. Saving]  [Status]  [Owner]  [Timeline]
[Category]  Consolidation   [X]            Draft     [Name]   Q[N] 20[XX]
[Category]  Price alignment [X]            Active    [Name]   [Month]

TOTAL PIPELINE: [X]
CAPTURED YTD:   [X]
REMAINING:      [X]
================================================================
```

## NEVER DO THESE

- NEVER fabricate market benchmark prices -- always cite source and date;
  if no reliable benchmark available, label as "no reliable benchmark found"
- NEVER recommend single-sourcing a critical category without
  documenting the supply continuity risk and mitigation plan
- NEVER report "savings" without defining the baseline clearly:
  savings vs. prior contract / vs. market / vs. budget -- specify
- NEVER include tail spend vendors in consolidation analysis without
  checking whether they supply something unique or critical

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
