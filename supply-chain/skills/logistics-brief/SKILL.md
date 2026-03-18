---
name: logistics-brief
description: >
  Activate for: logistics, carrier, freight, shipping, route, delivery,
  on-time delivery, OTD carrier, logistics performance, carrier review,
  freight cost, cost per kg, lane analysis, route optimisation, logistics brief,
  carrier scorecard, logistics KPI, shipping performance, freight audit,
  expedited freight, premium freight, mode of transport, logistics network,
  carbon emissions, Scope 3 logistics.
  NOT for: supply network facility placement (use network-design), vendor
  assessment (use vendor-assessment), spend category analysis (use spend-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/logistics-brief"
  mcp-integrations: "TMS, ERP, carrier APIs, freight rate databases"
---

## UNIVERSAL RULES (apply to every logistics task)

- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Carrier Performance Review -- Q1 2024]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [TMS / ERP / Carrier APIs / Manual input]
```

## LOGISTICS BRIEF TYPES

### Type 1: Carrier Performance Review

Use for: periodic carrier performance assessment, contract negotiation prep,
carrier selection, carrier exit decision.

DATA REQUIRED (from TMS or ERP, for defined period):

- Shipment volume by carrier (number of shipments + weight/units shipped)
- On-time delivery rate by carrier (shipments delivered on or before promised date)
- Damage rate and claim value by carrier
- Cost per kg (or per shipment) by carrier
- Track-and-trace reliability (% shipments with real-time tracking events)
- Carrier compliance: invoicing accuracy vs. contracted rates

CARRIER SCORECARD FORMAT:

```
CARRIER PERFORMANCE SCORECARD -- [Period]
================================================================
                 Shipments  OTD%   Damage%  Cost/kg  Track%  Score
[Carrier A]      [N]        [X]%   [X]%     [X]      [X]%    [X]/5
[Carrier B]      [N]        [X]%   [X]%     [X]      [X]%    [X]/5

SCORING KEY:
OTD >= 95%: 5/5  |  93-95%: 4/5  |  90-93%: 3/5  |  <90%: FLAG
Damage < 0.2%: 5/5  |  0.2-0.5%: 3/5  |  >0.5%: FLAG
Cost: benchmark against market rate (see local config)
Track >= 98%: 5/5  |  95-98%: 3/5  |  <95%: FLAG

FINDINGS:
RED [Carrier underperforming]: [specific metric] -- recommended action
AMBER [Carrier at risk]:       [trend concern] -- monitor; review at [date]
PASS [Carrier outperforming]:  [strength] -- protect relationship

LANE ROUTING RECOMMENDATIONS:
[Lane]: current routing -> optimal routing | saving: [X]/month
================================================================
```

### Type 2: Lane Optimisation Analysis

Use for: specific origin-destination analysis; carrier selection for a new lane;
mode of transport optimisation.

INPUT REQUIRED:

- Origin and destination (city/postcode/country)
- Shipment profile: volume (units/kg), frequency, typical parcel dimensions
- Service requirement: transit time; temperature controlled; track-and-trace
- Current arrangement: carrier, mode, cost, SLA
- Available alternatives (if known -- agent will also identify via MCP)

ANALYSIS OUTPUT:

```
LANE ANALYSIS: [Origin] -> [Destination]
---------------------------------------------------------
Shipment profile:  [Volume, frequency, specification]
Service req:       [Transit time; special requirements]

OPTION COMPARISON:
            Mode      Transit  Cost/kg  OTD%   Carbon   Score
Current:    [Mode]    [X days] [X]      [X]%   [X]g     [X]/5
Option A:   [Mode]    [X days] [X]      [X]%   [X]g     [X]/5
Option B:   [Mode]    [X days] [X]      [X]%   [X]g     [X]/5

RECOMMENDATION: [Option] because [specific rationale]
Annual saving vs. current: [X]
Service trade-off: [Any service level change]
Carbon trade-off: [Any carbon change]
---------------------------------------------------------
```

### Type 3: Expedited Freight Analysis

Use for: investigating high premium freight spend; root cause analysis;
upstream problem identification.

OUTPUT:

- Total expedited spend (% of total freight budget)
- Expedited volume by business unit / site / category
- Root cause classification:
  a) Late supplier delivery (procurement/vendor issue)
  b) Demand forecast error (planning issue)
  c) Inventory positioning error (supply chain design issue)
  d) Customer emergency (valid commercial reason)
  e) Production planning error (internal operations)
- Recommended intervention by root cause category
- Quantified saving if root cause is addressed

RULE: Expedited freight > 10% of total freight spend indicates an upstream
supply chain design or process problem, not a logistics problem.
Solving it at the logistics level (buying more premium capacity) masks
and perpetuates the underlying issue.

### Type 4: Carbon Assessment

Use for: Scope 3 emissions reporting; sustainability target setting;
mode-shift analysis; decarbonisation planning.

OUTPUT:

- Total logistics Scope 3 emissions (tCO2e) by carrier and lane
- Emissions intensity (gCO2e per km-tonne shipped)
- Breakdown by transport mode
- Highest-emission routes
- Mode-shift options with cost and service trade-offs
- Estimated reduction from implementing each option

EMISSIONS REFERENCE (approximate; verify with actual carrier data):
Air freight: 500-600 gCO2e per tonne-km
Road (HGV): 60-80 gCO2e per tonne-km
Rail (electric): 20-30 gCO2e per tonne-km
Sea (container): 10-15 gCO2e per tonne-km

## NEVER DO THESE

- NEVER recommend exiting an underperforming carrier without confirming
  alternative capacity is available for the affected lanes
- NEVER use cost per shipment as the sole metric -- cost per kg
  normalises for shipment size differences
- NEVER accept carrier invoice rate creep without audit:
  compare actual invoiced rate to contracted rate line by line
- NEVER diagnose an expedited freight problem as a logistics problem
  without first checking whether the root cause is upstream
- NEVER report carbon figures without the source and methodology --
  Scope 3 emissions data quality varies significantly by carrier

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
