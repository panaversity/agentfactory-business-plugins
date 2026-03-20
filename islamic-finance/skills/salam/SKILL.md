---
name: salam
description: >
  Activate for: salam, forward purchase Islamic, advance payment commodity,
  FAS 7, agricultural finance Islamic, salam receivable, parallel salam,
  commodity forward Islamic, advance purchase contract.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 7 (Salam and Parallel Salam)"
---

## THE STRUCTURE

Salam: The bank pays in FULL and IN ADVANCE for a commodity to be delivered
at a specified future date, location, and of specified quality and quantity.

Shariah requirements (all must be met — if any fails, contract is void):

1. Full payment at contract date (not deferred)
2. Commodity is fungible and standardised (gold, wheat, oil — not unique items)
3. Delivery date, location, and quantity all specified precisely
4. Commodity need not exist at contract date (unlike conventional spot contracts)

## AAOIFI FAS 7 — SALAM RECEIVABLE

**At contract execution (payment of advance):**
Dr: Salam Receivable [Full payment amount]
Cr: Cash [Full payment amount]

The salam receivable represents the bank's right to receive the commodity.
Carry at cost (the advance price paid), not at fair value of the commodity.

**At delivery:**
Dr: Salam Commodity / Inventory [Cost = original salam payment]
Cr: Salam Receivable [Cost — derecognise the receivable]

**On sale of commodity (bank sells to market):**
Dr: Cash / Receivable from buyer [Sale price]
Cr: Salam Commodity / Inventory [Cost]
Cr/Dr: Gain / Loss on Salam [Difference]

Commodity price risk: The bank bears price risk between advance payment and delivery.
If market price falls below advance price → loss. If it rises → gain.
This risk is inherent in salam. It is NOT a Shariah compliance issue.

## PARALLEL SALAM

To hedge or resell: Bank enters a SECOND salam (parallel salam) selling the
same commodity to another party at a higher price for delivery on the same date.

IMPORTANT: The two salam contracts must be INDEPENDENT.
The bank bears delivery risk in both. Cannot use customer's delivery to satisfy
the parallel salam (linking the two contracts may violate Shariah).

Parallel salam accounting: recognise as a separate salam liability.
Do not net the two contracts.

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 7:**

1. Accounting policy for salam transactions
2. Salam receivables movement table (opening, new contracts, deliveries, closing)
3. Commodity price risk exposure
4. Parallel salam liabilities outstanding
5. Shariah compliance: confirmation of full advance payment at contract date
