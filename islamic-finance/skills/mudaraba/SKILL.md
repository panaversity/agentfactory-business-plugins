---
name: mudaraba
description: >
  Activate for: mudaraba, investment account, IAH, investment account holder,
  profit-sharing investment, mudarib, rabb ul mal, PER, IRR,
  profit equalization reserve, investment risk reserve, restricted investment account,
  unrestricted investment account, FAS 3, profit pool, profit distribution,
  weightage table, Islamic deposit.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 3 (Mudaraba Financing)"
---

## THE STRUCTURE

**Mudaraba:** A partnership where:

- Rabb ul mal (capital provider): provides all the capital, bears all financial loss
- Mudarib (entrepreneur/manager): provides all the labour and management skill

In Islamic banking, the bank acts as MUDARIB for its Investment Account Holders (IAH),
who are the rabb ul mal (capital providers).

Profits are shared in a pre-agreed ratio (e.g., bank 30%, IAH 70%).
Losses are borne entirely by the IAH (unless caused by bank negligence or breach).

---

## THE PROFIT POOL CALCULATION

The profit pool for IAH distribution is calculated as follows:

**Step 1 — Determine total income earned by the bank from all deployments.**

**Step 2 — Allocate income between bank's own funds and IAH funds:**
Income attributable to bank's own equity = Total Income x (Bank Equity / Total Funds)
Income attributable to IAH = Total Income x (IAH Funds / Total Funds)

**Step 3 — Apply mudarib share:**
Mudarib fee (bank's share) = IAH Income x Mudarib Percentage (e.g., 30%)
Remaining distributable to IAH = IAH Income x IAH Percentage (e.g., 70%)

**Step 4 — Apply weightages:**
Different account types receive different weightages based on tenure and conditions.
Higher weightage = greater share of the distributable pool.

| Account Type     | Balance | Weightage | Weighted Balance |
| ---------------- | ------- | --------- | ---------------- |
| Savings (30-day) | X       | 0.90      | X x 0.90         |
| 90-day term      | X       | 1.00      | X x 1.00         |
| 180-day term     | X       | 1.15      | X x 1.15         |
| 365-day term     | X       | 1.25      | X x 1.25         |
| Total            |         |           | Sum              |

Distribution rate per unit of weighted balance = Distributable Income / Total Weighted Balance

**Step 5 — Apply PER and IRR transfers (see below).**

**Step 6 — Final distribution to each account type.**

---

## PROFIT EQUALIZATION RESERVE (PER) AND INVESTMENT RISK RESERVE (IRR)

**PER (Profit Equalization Reserve):**
Purpose: Smooth returns to IAH across periods of high and low profit.
In high-profit periods: transfer a portion to PER (building the reserve).
In low-profit periods: draw from PER to supplement IAH returns.

Entry when building PER:
Dr: Distributable Income (before final allocation to IAH)
Cr: Profit Equalization Reserve (liability / separate fund)

Entry when drawing from PER:
Dr: Profit Equalization Reserve
Cr: Distributable Income to IAH

**IRR (Investment Risk Reserve):**
Purpose: Buffer against capital loss to IAH.
Funded from IAH's share of profits (taken before distribution to IAH).

Entry when building IRR:
Dr: IAH Income Distributable
Cr: Investment Risk Reserve

Entry when drawing from IRR to cover loss:
Dr: Investment Risk Reserve
Cr: IAH Capital / Loss on IAH Investment

IMPORTANT: PER and IRR must be approved by SSB. Their levels must be disclosed.
Excessive PER/IRR that permanently suppresses IAH returns may raise Shariah concerns.

---

## JOURNAL ENTRIES — PROFIT DISTRIBUTION

**Recognition of gross income into profit pool:**
Dr: Income Receivable / Cash
Cr: Profit Pool (internal allocation account)

**Allocation to bank's own equity income:**
Dr: Profit Pool
Cr: Bank's Own Income (P&L)

**Mudarib fee recognition:**
Dr: Profit Pool
Cr: Mudarib Fee Income (bank's P&L)

**PER transfer:**
Dr: Profit Pool (IAH portion)
Cr: Profit Equalization Reserve

**IRR transfer:**
Dr: Profit Pool (IAH portion)
Cr: Investment Risk Reserve

**Final distribution to IAH:**
Dr: Profit Pool (remaining IAH distributable)
Cr: Payable to Investment Account Holders

**Distribution paid:**
Dr: Payable to Investment Account Holders
Cr: Cash / Credited to IAH accounts

---

## IAH BALANCE SHEET CLASSIFICATION

AAOIFI regime: IAH funds = "Equity of Investment Account Holders"
— Separate balance sheet section, distinct from the bank's own equity and liabilities.
— Reflects Shariah reality: IAH bear investment risk, not creditors.

IFRS regime: IAH funds = Financial Liabilities (IAS 32)
— Because the bank has a practical obligation to return capital (due to regulatory
requirements and market expectations), IAH deposits meet the definition of
a financial liability under IAS 32.
— Measured at amortised cost under IFRS 9.

THIS IS THE MOST SIGNIFICANT BALANCE SHEET DIFFERENCE between AAOIFI and IFRS
for Islamic banks. It directly affects Return on Equity and capital ratios.

---

## RESTRICTED vs. UNRESTRICTED INVESTMENT ACCOUNTS

**Unrestricted Investment Accounts (URIA):**
IAH gives bank full discretion to invest in any Shariah-compliant assets.
Bank commingles URIA funds with its own funds.
Most common type in retail Islamic banking.

**Restricted Investment Accounts (RIA):**
IAH specifies investment mandate (e.g., only real estate, only sukuk).
Bank manages as a separate pool; does not commingle with general funds.
BNM in Malaysia has specific guidance on RIA accounting (on vs. off balance sheet).

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 3 / AAOIFI Governance Standard:**

1. Accounting policy for investment accounts (mudaraba basis)
2. Movement in IAH funds (opening, new deposits, withdrawals, profit credited, closing)
3. Profit distribution methodology (profit pool, weightage table)
4. Mudarib percentage share
5. PER: opening balance, transfers in/out, closing balance, policy
6. IRR: opening balance, transfers in/out, closing balance, policy
7. Return on deposits by account type (annualised rate for the period)
8. SSB approval of profit distribution methodology

**IFRS regime (supplementary):**

1. Above IAH disclosures (as supplementary Shariah disclosures)
2. IFRS 7: maturity analysis of IAH deposits (as financial liabilities)
3. Fair value of IAH deposits (if different from carrying amount)
