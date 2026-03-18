---
name: network-design
description: >
  Designs and compares supply chain network scenarios. Activate for: network
  design, supply chain network, warehouse location, distribution centre,
  DC placement, new DC, nearshoring, reshoring, offshoring, facility
  consolidation, network optimisation, make vs buy, sourcing location,
  scenario analysis, network scenario, scenario comparison, logistics network,
  node optimisation, where to warehouse, where to manufacture, cross-docking,
  open a new warehouse, open a new distribution centre.
  USE THIS when the task involves comparing network configurations, evaluating
  new facility locations, or running scenario comparisons. Respond directly
  with scenario analysis -- do not ask clarifying questions when sufficient
  context is provided.
  NOT for: carrier performance (use logistics-brief), vendor assessment
  (use vendor-assessment), spend category analysis (use spend-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/supply-network-design"
  mcp-integrations: "Network optimisation MCP, ERP, TMS, customs databases, web search"
---

## UNIVERSAL RULES (apply to every network design task)

- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable
- ALWAYS respond directly with scenario analysis when the user provides a
  network scenario or comparison request -- do NOT ask clarifying questions
  when sufficient context exists to begin analysis. Use reasonable assumptions
  and state them explicitly rather than blocking on missing details.

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Network Design -- EMEA Distribution Review]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [ERP / TMS / Network optimisation MCP / Manual input]
```

## NETWORK DESIGN WORKFLOW

### When to Trigger a Network Design Review

TRIGGER EVENTS (any of these warrant a review):

- Demand volume has shifted >20% in a key region since last design
- New significant customer acquisition in a new geography
- Supplier base has materially changed (new sourcing region)
- Carrier or transport cost has increased >15% since last optimisation
- New DC or manufacturing facility planned or available
- Regulatory change affecting trade routes (tariffs, customs)
- Sustainability target requiring carbon reduction in Scope 3 logistics
- Company acquisition creating overlapping distribution networks

### Scenario Definition Framework

Before running any optimisation, define clearly:

OBJECTIVE FUNCTION (rank order -- what are you optimising for?):
Primary: [Cost / Service level / Carbon / Resilience -- choose one]
Secondary: [Cost / Service level / Carbon / Resilience]
Constraint: [Any hard constraints that cannot be traded off]

NETWORK PARAMETERS:
Supply nodes: Manufacturing sites and key suppliers (with capacities)
Demand nodes: Customer locations with demand volumes
Intermediate: Existing and candidate warehouse/DC locations
Time horizon: [1 year / 3 years / 5 years]
Demand forecast: [Current + growth assumptions per region]

SCENARIO STRUCTURE:
Scenario A: Status quo (baseline -- always include)
Scenario B: [First alternative -- name the key change]
Scenario C: [Second alternative]
Scenario D: [Optional: stress test scenario -- e.g. loss of one node]

### Network Design Output Format

```
NETWORK DESIGN ANALYSIS: [Project Name]
================================================================
Objective:       [Primary / Secondary optimisation goal]
Scenarios:       [N] scenarios analysed
Horizon:         [Time period]

SCENARIO COMPARISON:

            [Scenario A]    [Scenario B]    [Scenario C]
Total cost: [X]/yr          [X]/yr          [X]/yr
Avg transit: [X] days       [X] days        [X] days
Service %:  [X]%            [X]%            [X]%
Carbon:     [X] tCO2e       [X] tCO2e       [X] tCO2e
Capex req:  [X]             [X]             [X]
Payback:    N/A              [X] months      [X] months

RECOMMENDATION: Scenario [X]
Rationale:      [2-3 sentences: why this scenario best meets the
                stated objectives and constraints]

KEY TRADE-OFFS:
[Trade-off 1]: [e.g. "Scenario C saves Xk/yr more than B but
                requires Xk additional capex and adds 0.5 days
                to average transit time"]

RISKS AND SENSITIVITIES:
[What assumptions, if wrong, would change the recommendation?]
[Sensitivity: how does the recommendation change if demand in
Region X is 20% higher/lower than forecast?]

NEXT STEPS:
1. [Specific: site survey / regulatory check / carrier RFQ]
2. [Specific: approval required from whom]
3. [Implementation timeline and key milestones]
================================================================
```

### Conversational Scenario Iteration

Network design is most valuable when decision-makers can challenge
assumptions in real time. Support these question patterns:

"What if we increase [region] capacity by [X]%?"
-> Re-run affected scenario with modified parameter; show delta vs. prior result

"What if fuel costs rise another 15%?"
-> Re-run all scenarios with updated transport cost assumption; identify
which scenario is most robust to this change

"What's the break-even volume for opening the [location] DC?"
-> Calculate the demand volume at which the new DC scenario equals
the cost of the status quo; present as break-even analysis

"What happens if the [country] supply route is disrupted for 3 months?"
-> Model the contingency cost: what would re-routing through an
alternative network node cost, and does the current network design
have enough redundancy?

## NEVER DO THESE

- NEVER present a single scenario as a recommendation --
  always compare against the status quo baseline at minimum
- NEVER optimise for cost alone without showing the service level
  and carbon implications -- all three dimensions must be visible
- NEVER recommend closing an existing node without modelling
  the transition cost and the risk of the transition period
- NEVER base a network design on demand data >18 months old --
  always confirm demand assumptions before running optimisation
- NEVER present a payback calculation without stating the
  assumptions (discount rate, demand growth, cost escalation)

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
