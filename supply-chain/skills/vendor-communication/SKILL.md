---
name: vendor-communication
description: >
  Activate for: vendor communication, supplier communication, dispute letter,
  invoice dispute, corrective action request, CAR, price dispute, quantity
  dispute, performance notice, vendor notice, vendor warning, exit notice,
  contract notice, non-renewal notice, vendor rejection, vendor escalation,
  write to vendor, email supplier, communicate with vendor, supply assurance.
  NOT for: invoice processing (use invoice-reconciliation), vendor assessment
  (use vendor-assessment), spend analytics (use spend-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/vendor-communicate"
  mcp-integrations: "Email MCP, contract register"
---

## UNIVERSAL RULES (apply to every communication task)

- NEVER recommend a vendor exit without a qualified alternative identified
  or an explicit "no alternative -- managed risk" decision documented
- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Vendor Communication -- Invoice Dispute INV-2024-0847]
VENDOR TIER:   [Strategic / Tactical / Commodity / Bottleneck / Unclassified]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
COMMUNICATION TYPE: [Invoice Dispute / CAR / Non-Renewal / Supply Assurance / Exit]
```

## COMMUNICATION TYPES AND STRUCTURES

### Type 1: Invoice Dispute Notice

Use when: invoice exception identified in reconciliation; vendor must provide
credit note, revised invoice, or supporting evidence.

```
Subject: Invoice Dispute -- Invoice [Number] dated [Date]
         Reference: PO [Number]

Dear [Contact name at vendor],

We have reviewed Invoice [Number] dated [Date] for [Amount] and have
identified the following discrepancy/discrepancies requiring your
attention before payment can be processed.

DISCREPANCY [N]:
Item:         [Description]
Invoiced:     [Qty or price as invoiced]
Our records:  [Qty or price per PO/GR]
Variance:     [Amount or units]
Basis:        [PO reference or Goods Receipt reference]

REQUIRED ACTION:
Please [issue a credit note for X / provide a revised invoice /
provide documentary evidence supporting the invoiced amount]
by [date -- typically 5 business days].

Payment of the undisputed amount ([X]) will be processed on our
standard payment terms from receipt of resolution.

[Sign-off: your name, title, contact details]
```

### Type 2: Corrective Action Request (CAR)

Use when: vendor performance has breached a threshold (OTD, quality,
or other contractual KPI) requiring formal documented response.

```
Subject: Corrective Action Request -- [Vendor Name] -- [KPI] Performance
         Reference: CAR-[Year]-[Number]

Dear [Contact name],

We are writing to formally notify you that [Vendor Name]'s performance
against [KPI] has fallen below the contractual threshold during
[period], and to request a formal corrective action plan.

PERFORMANCE DATA:
KPI:              [On-time delivery / Quality rejection rate / Other]
Contractual SLA:  [X]%
Actual (period):  [X]%
Shortfall:        [X percentage points]
Period:           [Start date -- End date]
Supporting data:  [Reference to ERP report or attached data]

REQUIRED CORRECTIVE ACTION PLAN:
Please provide a written corrective action plan within [10 / 14] calendar
days of this notice, addressing:
1. Root cause analysis of the performance shortfall
2. Immediate containment actions already taken
3. Corrective actions to be implemented, with target dates
4. How compliance with the SLA will be monitored going forward

We will schedule a review meeting for [proposed date] to discuss
the plan and agree monitoring arrangements.

This notice is issued under Clause [X] of our Supply Agreement dated [date].

[Sign-off: your name, title]
```

### Type 3: Contract Non-Renewal Notice

Use when: exercising the right not to renew a contract within the
contractual notice period. Must be sent before the notice deadline.

```
Subject: Notice of Non-Renewal -- [Contract Reference/Description]
         Agreement dated [Date]

Dear [Contact name],

In accordance with Clause [X] of our [Agreement name] dated [date],
we are providing [X days'] written notice that we will not be renewing
the Agreement upon its expiry on [date].

The Agreement will therefore terminate on [expiry date].

We will honour all purchase orders issued prior to this notice and
will expect fulfilment of all confirmed orders through to [date].

Please confirm receipt of this notice and advise us of any transition
support you are able to provide during the wind-down period.

We thank you for your service over the period of the Agreement.

[Sign-off: authorised signatory, title]
```

### Type 4: Emergency Supply Assurance Request

Use when: a risk signal (financial distress, Tier 2 disruption, news event)
requires immediate assurance from a critical vendor.

```
Subject: Supply Assurance Request -- [Category/Product] -- Urgent

Dear [Contact name],

We have become aware of [brief, factual description of the concern --
e.g. reports of supply disruption at one of your key raw material
suppliers / your company's published restructuring announcement].

As [Vendor Name] is a critical supplier to our operations, we are
writing to request written assurance on the following points:

1. Is your production capacity for [category/product] unaffected?
2. Do you have sufficient raw material / component inventory to
   fulfil orders over the next [60/90] days?
3. Are there any circumstances that could affect your ability to
   meet our confirmed purchase orders?

Please respond by [date -- 3-5 business days] with a formal
written statement. We may follow this with a request for a
call with your [CEO/Operations Director] to discuss further.

We appreciate your prompt attention to this matter.

[Sign-off: CPO or category manager]
```

### Type 5: Vendor Exit Notice (Planned Transition)

Use when: ending a vendor relationship by mutual agreement or for
convenience, with a planned transition period.

```
Subject: Transition Notice -- Supply Relationship Wind-Down

Dear [Contact name],

We are writing to notify you that [Your Company] has taken the
decision to transition [category/product] supply to [alternative
arrangement / consolidation with existing supplier].

We anticipate a transition period of [X weeks/months], during which
we will continue to issue purchase orders in accordance with our
current arrangement.

We would appreciate your cooperation with the following transition
requirements:
- Continued fulfilment of confirmed orders through [date]
- Return of any customer-owned tooling, moulds, or intellectual
  property by [date]
- Transfer of technical documentation and specifications by [date]
- [Other transition-specific items]

We value the relationship we have had with [Vendor Name] and will
provide a reference for future customers upon request.

[Sign-off: CPO or authorised signatory]
```

## COMMUNICATION STANDARDS

Tone: Professional, factual, constructive.

- State facts; do not attribute blame or motive
- Be specific: reference PO numbers, dates, quantities, thresholds
- State the required action and deadline clearly
- Avoid emotional language regardless of the severity of the issue

Authority: All communications above configured value threshold
require sign-off from the appropriate authority level before sending.
Dispute notices: Category Manager sign-off
CARs: CPO sign-off
Contract notices: CPO + Legal review recommended
Exit notices: CPO + Finance Director

## NEVER DO THESE

- NEVER send a dispute notice without specific reference to the
  PO number and the contractual basis for the dispute
- NEVER send a CAR without the supporting performance data attached
- NEVER send a contract notice after the notice deadline has passed
  without legal advice (you may have lost the right to non-renew)
- NEVER send a vendor exit notice without confirming transition
  requirements for tooling, IP, and documentation first
- NEVER respond to a phishing or social engineering attempt
  (bank detail change requests) by email -- always call the vendor
  on a known number to verify

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
