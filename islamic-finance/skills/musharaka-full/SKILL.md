---
name: musharaka-full
description: >
  Activate for: musharaka, joint venture Islamic, partnership finance,
  musharaka capital, profit and loss sharing, musharaka investment,
  FAS 4 musharaka, running musharaka, working capital musharaka,
  project musharaka, permanent musharaka.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 4 (Musharaka Financing)"
---

## THE STRUCTURE

In full Musharaka, ALL parties contribute BOTH capital AND (typically) management.
Profits are shared in a pre-agreed ratio (not necessarily proportional to capital).
Losses are shared STRICTLY in proportion to capital contributions.

This distinguishes musharaka from mudaraba (where one party provides only labour).

Types of musharaka:

- **Permanent Musharaka**: indefinite joint venture (equity finance)
- **Diminishing Musharaka**: see musharaka-dm skill — buy-out structure
- **Running Musharaka**: short-term revolving working capital facility

---

## AAOIFI FAS 4 TREATMENT

**Initial Recognition — Bank's Capital Contribution:**
Dr: Musharaka Investment [Bank's capital contribution]
Cr: Cash [Same]

The investment is recognised at COST (not fair value at inception).

**Profit Recognition — When Distributable Profit is Earned:**
Dr: Accrued Musharaka Profit Receivable [Bank's share of profit]
Cr: Income from Musharaka [Same]

IMPORTANT: Recognise profit only when EARNED AND DISTRIBUTABLE.
Do not accrue profit merely because the business is profitable on paper.
Profit is recognised when the musharaka venture has computed and declared
its distributable profit for the period.

**Loss Recognition — When a Loss is Incurred:**
Dr: Loss on Musharaka Investment [Bank's proportional share of loss]
Cr: Musharaka Investment [Same — reduces carrying value]

Losses are shared IN PROPORTION TO CAPITAL, regardless of the profit-sharing ratio.
If the bank contributed 60% of capital, it absorbs 60% of any loss.

**Capital Repayment / Exit:**
Dr: Cash [Capital returned]
Dr: Loss on Exit / Cr: Gain on Exit [Difference from carrying value]
Cr: Musharaka Investment [Original carrying value]

---

## IFRS ASSESSMENT FOR MUSHARAKA

Under IFRS, a musharaka arrangement requires analysis under IFRS 11 (Joint Arrangements):

**Step 1 — Does the bank have JOINT CONTROL?**
Joint control = contractually agreed sharing of control over an arrangement,
which exists only when decisions about relevant activities require unanimous consent.

If yes → IFRS 11 applies. Classify as:

- Joint Operation: bank recognises its share of assets, liabilities, revenue, expenses
- Joint Venture: bank recognises its investment using equity method (IAS 28)

**Step 2 — If NO joint control → IFRS 9 Financial Asset**
If the bank merely contributes capital and receives a return (no control),
IFRS 9 governs. Classify the musharaka investment as:

- FVTPL (most likely — the return depends on venture profit, failing SPPI test)
- Equity instrument → designated at FVOCI (irrevocable, no recycling)

**The SPPI Test for Musharaka:**
Musharaka returns depend on actual profit of the venture — they are NOT solely
payments of principal and a fixed return. Therefore musharaka FAILS the SPPI test.
Do NOT classify musharaka investments at amortised cost under IFRS 9.

---

## RUNNING MUSHARAKA (WORKING CAPITAL FACILITY)

Running Musharaka is used for short-term revolving working capital:
Bank deposits funds into the customer's business account as its musharaka capital.
Customer uses and replenishes the funds within agreed limits.
At period end, profits are calculated and distributed.

This structure is common in Pakistan (SBP guidelines for running musharaka),
Malaysia (BNM guidance), and UAE.

Accounting treatment: each drawing-down and repayment tracked as capital movement.
Monthly profit accrual on average capital balance.

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 4:**

1. Accounting policy for musharaka investments (cost basis, profit recognition trigger)
2. Movement in musharaka investments (opening, new, returned, losses, closing)
3. Income from musharaka recognised in the period
4. Impaired musharaka investments and provisions
5. Nature and duration of principal musharaka ventures
6. Capital contribution ratios and profit-sharing ratios for significant ventures

**IFRS 11 (if joint arrangement):**

1. Nature, purpose, place, proportion of ownership
2. Summarised financial information of material joint ventures (IAS 28)
3. Unrecognised losses if equity method investment is at nil

**IFRS 9 (if financial asset):**

1. Classification basis and SPPI assessment explanation
2. Movement in carrying amount
3. Fair value (if FVTPL) or OCI movements (if FVOCI)
