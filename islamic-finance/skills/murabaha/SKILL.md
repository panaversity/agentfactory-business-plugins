---
name: murabaha
description: >
  Activate for: murabaha, cost-plus financing, deferred sale,
  commodity murabaha, tawarruq, FAS 2, murabaha receivable,
  deferred murabaha income, murabaha portfolio, murabaha schedule,
  murabaha profit recognition, mark-up financing.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 2 (Murabaha and Murabaha to the Purchase Orderer)"
---

## CORE PRINCIPLE

Murabaha is a SALE transaction, not a LOAN transaction.
The bank is a merchant purchasing and reselling — not a lender charging interest.

This principle governs all accounting treatment and terminology.
The jurisdiction overlay determines which label system applies in output.

---

## SHARIAH STRUCTURE VERIFICATION

Before any accounting entry, confirm the four Shariah conditions:

1. The bank (IFI) must have actually purchased the asset from the supplier before
   selling it to the customer. If the bank never held title, the contract is void.
2. The selling price (cost + mark-up) must be disclosed to the customer.
3. There must be a binding offer and acceptance (ijab and qabul).
4. The deferred payment terms must be specified and agreed in the contract.

If any condition cannot be confirmed: FLAG for SSB review before posting entries.

---

## RECOGNITION RULES — FOUR-STEP SEQUENCE

**Step 1 — Bank purchases asset from supplier:**
Dr: Murabaha Asset (inventory) [Cost Price]
Cr: Cash / Payable to Supplier [Cost Price]

**Step 2 — Bank sells asset to customer at mark-up (contract execution date):**
Dr: Murabaha Receivable [Total Selling Price = Cost + Total Mark-up]
Cr: Murabaha Asset [Cost Price]
Cr: Deferred Murabaha Income [Total Mark-up]

**Step 3 — Periodic profit recognition (each period-end):**
Dr: Deferred Murabaha Income [Period allocation per effective profit rate]
Cr: [Income account — label per jurisdiction overlay]

**Step 4 — Customer instalment payment received:**
Dr: Cash [Instalment amount]
Cr: Murabaha Receivable [Instalment amount]

---

## EFFECTIVE PROFIT RATE CALCULATION

Method: Identical mathematics to IFRS 9 effective interest rate (EIR).
The rate that discounts all future cash flows to equal the initial murabaha receivable.
Label this rate "effective profit rate" — NEVER "effective interest rate."

Period allocation formula:
Opening Receivable x (Effective Profit Rate / Periods per Year) = Period Profit

Closing Receivable = Opening Receivable + Period Profit — Cash Instalment Received

---

## INCOME LABELS BY REGIME

AAOIFI regime (Bahrain, Qatar): "Murabaha Income"
MFRS regime (Malaysia): "Profit from Islamic Financing" or "Islamic Financing Income"
IFRS regime (UAE, Saudi Arabia, UK, Pakistan listed): "Profit from Murabaha Financing"
NEVER use: "Interest Income" or "Finance Income" (generic)
Use jurisdiction overlay to confirm the correct label.

---

## BALANCE SHEET CLASSIFICATION

AAOIFI regime: "Murabaha Receivables" — separate line, NOT under "Loans and Advances"
IFRS regime: May appear under "Islamic Financing Receivables" or "Loans and Advances"
with Islamic sub-classification. Jurisdiction overlay specifies exact presentation.

Deferred Murabaha Income: ALWAYS a credit balance, shown as a contra or separate liability.
In AAOIFI regime: shown as a deduction from gross Murabaha Receivables, or separately.
In IFRS regime: typically netted such that the carrying value = amortised cost.

---

## IMPAIRMENT

AAOIFI regime: Apply AAOIFI FAS 30 (Impairment, Credit Losses and Onerous Commitments).
Stage 1: 12-month expected credit loss
Stage 2: Lifetime ECL (significant increase in credit risk)
Stage 3: Lifetime ECL + non-accrual of murabaha income

IFRS regime: Apply IFRS 9 ECL model.
SPPI test: Murabaha receivables generally pass (fixed contractual cash flows).
Business model: held-to-collect → amortised cost.

IMPORTANT — SHARIAH CONSTRAINT ON DEFAULT:
When a customer defaults, the bank CANNOT charge additional profit/mark-up on
the overdue amount. Additional charges on overdue amounts constitute riba.
Bank remedies: collateral enforcement, guarantor call, legal action only.
Overdue profit that has not yet been earned is NOT accelerated on default.
Only already-earned profit (released from deferred income) is a receivable.

---

## COMMODITY MURABAHA / TAWARRUQ NOTES

In commodity murabaha (tawarruq), the bank purchases a commodity from a broker,
sells it to the customer at a mark-up, and the customer sells to a third broker for cash.

Accounting treatment is identical to asset murabaha.
Additional Shariah compliance check: confirm the two commodity sale transactions
are genuinely separate (not a sham back-to-back). Some scholars object to tawarruq.
If the jurisdiction's Shariah board has specific rulings on tawarruq, flag for SSB review.

---

## MANDATORY DISCLOSURES

Include all of the following in notes to financial statements:

1. Accounting policy for murabaha financing (which standard governs)
2. Movement table for Murabaha Receivables:
   Opening balance / New facilities / Instalments received / Written off / Closing balance
3. Movement table for Deferred Murabaha Income:
   Opening balance / Unearned income on new facilities / Released to income / Closing balance
4. Murabaha income recognised in the period
5. Non-performing murabaha receivables:
   Amount / Ageing / Stage classification / Provision held
6. Accounting policy for income non-accrual on Stage 3 facilities

AAOIFI regime: also include Shariah compliance statement confirming
all murabaha contracts were executed in accordance with AAOIFI Shariah Standard No. 8.
