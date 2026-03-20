---
name: musharaka-dm
description: >
  Activate for: diminishing musharaka, DM, musharaka mutanaqisah,
  co-ownership finance, Islamic home finance, declining musharaka,
  bank equity share, FAS 4, diminishing musharaka schedule,
  rental on bank share, equity buy-out, Islamic mortgage.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 4 (Musharaka Financing)"
---

## THE STRUCTURE

In Diminishing Musharaka:
1. Bank and customer jointly purchase an asset (typically property or equipment).
2. Bank owns a large share (e.g., 80%); customer owns the rest (e.g., 20%).
3. Customer pays RENT on the bank's share.
4. Customer simultaneously PURCHASES units of the bank's share (equity buy-out).
5. As bank's share diminishes, the rental income payable on it DECLINES.
6. When customer has purchased all of the bank's share, the asset belongs to the customer.

TWO CONTRACTS RUN SIMULTANEOUSLY:
- A musharaka (partnership): for the joint ownership
- An ijarah (lease): for the customer's use of the bank's share

SHARIAH CRITICAL: These must be TWO SEPARATE contracts. If the rental
and buy-out are combined into a single contract guaranteeing the bank's return,
the structure may resemble a loan and fail the Shariah form test.

---

## ACCOUNTING — AAOIFI FAS 4 (BAHRAIN, QATAR)

**Initial Recognition:**
Dr: Musharaka Investment — [Property Name] [Bank's share of purchase price]
Cr: Cash [Bank's share of purchase price]

**Monthly Rental Income (on current bank ownership share):**
Dr: Accrued Rental Receivable [Rental rate x Bank's current ownership % x Asset value / 12]
Cr: Musharaka Rental Income [Same]

The rental amount DECREASES each time the customer buys a unit of the bank's share.
Re-calculate the rental EVERY time a buy-out payment is received.

**Monthly Equity Buy-Out (customer purchases bank's units):**
Dr: Cash [Buy-out payment]
Cr: Musharaka Investment [Same — derecognise this portion of the asset]

The buy-out price per unit = agreed price per unit (typically at original purchase value,
or at periodic revaluation per the musharaka agreement).

**Gain or Loss on unit derecognition:**
If buy-out price > carrying value of unit: recognise gain
If buy-out price < carrying value of unit: recognise loss
(Common if property has been impaired)

**The Equity Schedule (build for each DM facility):**

| Month | Opening Bank % | Rental Income | Buy-Out Received | Closing Bank % |
|-------|--------------|---------------|-----------------|---------------|
| 1     | 80.00%       | X             | Y               | 79.XX%        |
| 2     | 79.XX%       | X-delta       | Y               | 78.XX%        |

The key output: declining rental income over the life of the facility.
Total return = Sum of all rental payments + any gain on unit derecognition.

---

## ACCOUNTING — IFRS 9 SUBSTANCE ANALYSIS (ALL IFRS REGIMES)

**The SPPI Test:**
Does the DM arrangement produce cash flows that represent solely payments of
principal and a return consistent with a basic lending arrangement?

Analysis:
- The bank pays an initial amount (its share of property purchase price) = principal
- The customer pays monthly rent + monthly equity buy-out = interest + principal repayment
- Over the full term, the bank receives total payments in excess of its initial outlay = return

IFRS 9 CONCLUSION (typical in UAE, Malaysia, UK, Saudi Arabia, Pakistan listed entities):
DM home finance is typically classified as a financial asset at AMORTISED COST
because it passes both the business model test (held-to-collect) and SPPI test.

The effective interest rate (EIR) is calculated as the rate that equates:
Initial bank outlay = PV of all future cash flows (rental + equity buy-out payments)

Monthly income recognition = Opening carrying value x EIR / 12

**Important: Under IFRS 9 amortised cost, the income is front-loaded (higher in early
months, lower in later months) unlike AAOIFI FAS 4 where the income declines linearly
with the ownership share. This produces a systematic difference in income profile
between AAOIFI and IFRS regimes for the same DM facility.**

---

## INCOME LABELS

AAOIFI regime: "Musharaka Rental Income" or "Income from Diminishing Musharaka"
IFRS regime: "Profit from Islamic Home Finance" or "Islamic Financing Income — DM"
NEVER use: "Interest Income" or "Mortgage Interest"

---

## IMPAIRMENT

AAOIFI regime: AAOIFI FAS 30 — stage classification on the DM investment.
IFRS regime: IFRS 9 ECL — stage classification on the DM financial asset.

SHARIAH CONSTRAINT: Cannot charge penalty interest on overdue amounts.
If customer misses a buy-out payment or rental, no additional return can be earned.
Bank remedies: security enforcement, guarantor call, renegotiation only.

---

## VARIABLE RENTAL RATE NOTES

DM rental rates in many jurisdictions are variable (repriced periodically).
If tied to a benchmark rate (KIBOR, SOFR-equivalent, or bank's published rate):
- Shariah compliance check: the benchmark must itself be Shariah-permissible.
- In Pakistan: SBP has issued guidance on permissible benchmarks for variable-rate DM.
- In Malaysia: BNM has issued guidance on benchmark rates for Islamic products.
- NEVER tie to LIBOR or a conventional interest benchmark without Shariah approval.

When repricing occurs: recalculate the rental on the bank's current ownership share
at the new rate. The buy-out schedule is typically unchanged.

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 4:**
1. Accounting policy: joint ownership structure, not a loan
2. DM investment movement table (opening, new facilities, buy-outs received, impairments, closing)
3. Musharaka rental income recognised in the period
4. Declining ownership profile description
5. Non-performing DM facilities: amount, stage, provision

**IFRS 9:**
1. DM financial assets — classification basis (amortised cost) and SPPI justification
2. Movement in gross carrying amount
3. ECL provision movement (Stage 1, 2, 3)
4. Income from DM financing
5. Collateral held against DM exposures (property value, LTV ratios)
