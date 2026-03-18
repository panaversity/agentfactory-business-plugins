---
name: invoice-reconciliation
description: >
  Activate for: invoice, reconcile, reconciliation, three-way match, two-way
  match, invoice processing, AP, accounts payable, purchase order match,
  goods receipt match, invoice exception, price variance, quantity variance,
  duplicate invoice, invoice approval, invoice hold, invoice dispute, PO
  mismatch, over-invoiced, under-delivered, missing PO.
  NOT for: bank reconciliation (use banking plugin), vendor assessment
  (use vendor-assessment), spend category analysis (use spend-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/invoice-reconcile"
  mcp-integrations: "ERP, AP system, email-inbox MCP"
---

## UNIVERSAL RULES (apply to every reconciliation task)

- NEVER approve an invoice that has not been matched against a PO
  (above the configured materiality threshold)
- NEVER process a duplicate invoice -- always check against prior submissions
  before authorising payment
- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## THREE-WAY MATCH ENFORCEMENT

Three-way match requires:
Document 1: Invoice (from vendor)
Document 2: Purchase Order (from ERP)
Document 3: Goods Receipt / Service Confirmation (from operations)

TWO-WAY MATCH (acceptable only for):

- Services (no goods receipt exists)
- Utilities (no PO in advance)
- Invoices below configured materiality threshold

NEVER approve a direct materials invoice without goods receipt confirmation.

## MANDATORY OUTPUT HEADER

```
TASK:          [e.g. Invoice Reconciliation -- INV-2024-0847]
VENDOR TIER:   [Strategic / Tactical / Commodity / Bottleneck / Unclassified]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [ERP / AP system / Manual input]
```

## RECONCILIATION WORKFLOW -- FOUR-STAGE PROCESS

### Stage 1: Document Intelligence

Extract structured data from invoice (PDF, email, EDI, manual entry):

MANDATORY FIELDS TO EXTRACT:
Vendor name: [Exact legal name -- match against vendor master]
Vendor ID: [Cross-reference ERP vendor master]
Invoice number: [For duplicate detection]
Invoice date: [Check against late submission rules]
PO reference: [Required for matching -- flag if absent]
Line items: [Description / quantity / unit / unit price / line total]
Total amount: [Verify arithmetic: sum of lines + tax = total]
Payment terms: [Match against contracted terms]
Bank details: [Flag if different from vendor master -- fraud risk]

VALIDATION CHECKS AT EXTRACTION:
Arithmetic check: do line items sum to invoice total?
Vendor name match: does invoice name match ERP vendor master?
Duplicate check: has this invoice number been submitted before?
Late submission: is invoice date within the configured day limit?
Bank detail change: are bank details the same as vendor master?

FLAG IMMEDIATELY IF:
RED Bank details differ from vendor master -> FRAUD ALERT -- do not process;
contact vendor by phone (not email) to verify; escalate to Finance Director
RED Duplicate invoice number -> REJECT; notify vendor
RED Invoice > configured days old -> REJECT; notify vendor of late submission policy
RED Vendor not in approved vendor list -> HOLD; escalate to Procurement

### Stage 2: Three-Way Match

MATCH EACH LINE ITEM AGAINST:
Document A: Invoice line (what vendor claims to be owed)
Document B: Purchase Order line (what was authorised to buy)
Document C: Goods Receipt / Service Confirmation (what was actually received)

QUERY ERP via MCP:

1. Find PO by reference number
2. Retrieve all PO line items with authorised quantities and prices
3. Find Goods Receipt(s) matched to this PO
4. Retrieve confirmed received quantities from GR

MATCH CLASSIFICATION PER LINE ITEM:

MATCHED -- all within tolerance
Invoice qty = GR qty (within tolerance)
Invoice price = PO price (within tolerance)
-> Auto-approve this line

PRICE VARIANCE -- OUTSIDE TOLERANCE
Invoice price != PO price, outside tolerance
-> Route to Procurement; require vendor price justification

PRICE VARIANCE -- WITHIN TOLERANCE
Invoice price != PO price, but within configured tolerance
-> Auto-approve with flag to Finance (audit trail)

QUANTITY VARIANCE -- OVER-INVOICED
Invoice quantity > GR confirmed quantity
-> Hold over-invoiced portion; investigate with warehouse/vendor

QUANTITY VARIANCE -- GOODS RECEIPT PENDING
Invoice quantity matches PO but GR not yet received/confirmed
-> Hold invoice; alert warehouse for GR confirmation;
set 5-day follow-up reminder

PO NOT FOUND
Invoice references a PO that does not exist in ERP
-> Hold entire invoice; route to Procurement for retrospective PO
or rejection decision

DUPLICATE DETECTED
Same vendor, same amount, within configured days of prior invoice
-> Reject; notify vendor; log as potential fraud attempt if persistent

UNAUTHORISED CHARGE
Line item has no corresponding PO line
-> Reject this line; notify vendor; request credit note

### Stage 3: Exception Routing

FOR EACH EXCEPTION TYPE, APPLY ROUTING RULES:

Price variance -- within tolerance:
Action: Auto-approve with Finance notification
Log: Exception register (for pattern monitoring)
Owner: Finance (automated)

Price variance -- outside tolerance (< escalation threshold):
Action: Route to category manager for approval
Deadline: 3 business days
Owner: Category manager + Procurement

Price variance -- outside tolerance (> escalation threshold):
Action: Route to CPO for approval
Deadline: 5 business days
Owner: CPO

Quantity variance -- over-invoiced:
Action: Hold excess; investigate with warehouse team
Deadline: 5 business days to confirm GR or reject
Owner: Warehouse + Finance

GR pending:
Action: Hold invoice; alert warehouse; 5-day auto-reminder
If unresolved at 10 days: escalate to Operations Manager
Owner: Warehouse -> Finance on resolution

PO not found (> materiality threshold):
Action: Route to Procurement for retrospective PO or rejection
Deadline: 3 business days
Owner: Procurement

Duplicate invoice:
Action: Reject immediately; notify vendor; log incident
Owner: Finance (automated)

Fraud alert (bank details changed):
Action: STOP all processing; escalate to Finance Director immediately
Owner: Finance Director

### Stage 4: Audit and Pattern Monitoring

LOG FOR EVERY INVOICE:

- Invoice number, vendor, date, amount
- Match outcome: APPROVED / EXCEPTION TYPE / REJECTED
- Exception resolution: action taken, approver, date resolved
- Payment amount approved vs. original invoice amount

PATTERN DETECTION (run weekly):
Same exception from same vendor > 3x in 30 days:
-> Flag as systematic issue; recommend vendor data alignment meeting

Price variance on same line item > 2 consecutive invoices:
-> Flag as contract non-compliance; initiate commercial review

GR pending rate > 15% of invoices from one vendor:
-> Flag as goods receipt process issue (warehouse or vendor despatch?)

## RECONCILIATION OUTPUT FORMAT

```
INVOICE RECONCILIATION: [Invoice Number] | [Vendor]
================================================================
Invoice date:  [Date]   PO matched:    [PO number or NOT FOUND]
Processing:    [Date]   GR matched:    [GR number or PENDING/NONE]

LINE ITEM ANALYSIS:
Item [N]: [Description] -- [Qty] @ [Price]
  PO price:      [X]    Invoice price: [X]
  Price variance: [+/-X] ([+/-X]%)
  GR qty:        [N] confirmed
  Invoice qty:   [N]
  Qty variance:  [+/-N units]
  TOLERANCE:     [+/-X% configured for this category]
  STATUS:        [MATCHED / WITHIN TOLERANCE / EXCEPTION TYPE]
  Action:        [Specific action required]

RECONCILIATION SUMMARY:
Approved for payment:    [X]
On hold (pending GR):    [X]
Disputed (variance):     [X]
Rejected (unauthorised): [X]
Original invoice total:  [X]
RECOMMENDED PAYMENT:     [X]

VENDOR COMMUNICATION: [Drafted -- see /vendor-communicate]
AUDIT LOG:             [Saved to exception register]
================================================================
```

## NEVER DO THESE

- NEVER approve a direct materials invoice without a goods receipt confirmation
- NEVER process an invoice where bank details differ from vendor master
  without phone verification -- this is the primary invoice fraud vector
- NEVER approve a duplicate invoice -- always reject and notify vendor
- NEVER approve a PO-not-found invoice above materiality threshold
  without a retrospective PO or documented exception approval
- NEVER process an invoice from a vendor not on the approved vendor list
  without Procurement escalation
- NEVER mark a GR as confirmed without system evidence --
  verbal confirmation from warehouse is not sufficient for audit purposes

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
