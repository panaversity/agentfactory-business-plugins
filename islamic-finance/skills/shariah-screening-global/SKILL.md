---
name: shariah-screening-global
description: >
  Activate for: Shariah screening, halal stocks, Shariah-compliant portfolio,
  prohibited sectors Islamic, financial ratio screen Islamic, purification,
  PSX Shariah list, SC Malaysia Shariah list, Tadawul Shariah,
  MSCI Islamic index, DJIM, Dow Jones Islamic, AAOIFI Shariah Standard 21,
  non-permissible income, debt ratio screen, interest-bearing securities screen.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI Shariah Standard 21, SC Malaysia Guidelines, S&P Dow Jones Islamic Index"
---

## THE FOUR SCREENING METHODOLOGIES — GLOBAL COMPARISON

| Methodology | Maintained By | Sector Screen | Debt Screen | NPI Screen | Cash Screen |
|---|---|---|---|---|---|
| SC Malaysia SRI | Securities Commission Malaysia | Comprehensive positive/negative list | 33% total debt/total assets | 5% non-permissible income | 33% |
| Saudi Tadawul | Tadawul (Saudi Exchange) | Exclusion-based | 30% debt | 5% non-permissible income | 33% |
| MSCI Islamic | MSCI / independent scholars | Exclusion-based | 33% total debt/market cap | 5% non-permissible income | 33% |
| DJIM | S&P Dow Jones / Shariah scholars | Exclusion-based | 33% trailing 24-month average market cap | 5% non-permissible income | 33% |
| AAOIFI SS 21 | AAOIFI | Exclusion-based | 30% total debt/market cap | 5% non-permissible revenue | 30% |

---

## STEP 1: SECTOR SCREENS (ALL METHODOLOGIES — EXCLUSIONS)

Automatically exclude any company with MATERIAL INVOLVEMENT in:

**Hard exclusions (zero tolerance — any involvement disqualifies):**
- Conventional banking (interest-based)
- Conventional insurance
- Alcohol production or distribution
- Tobacco production or distribution
- Pork products (including gelatin, pork-based food processing)
- Gambling (casinos, bookmakers, lottery, online gambling)
- Adult entertainment / pornography
- Weapons of mass destruction

**Soft exclusions (use NPI income screen — see Step 3):**
- Defence / military equipment (below WMD level)
- Conventional media (mixed — needs NPI test)
- Hotels and hospitality (may have alcohol revenue — needs NPI test)
- Entertainment (needs NPI test)
- Non-halal food with permissible majority products (needs NPI test)

---

## STEP 2: FINANCIAL RATIO SCREENS

**Debt Screen (interest-bearing debt / total assets or market cap):**
- If interest-bearing debt > 33% of total assets (AAOIFI/MSCI) or market cap → EXCLUDE
- "Interest-bearing debt" = conventional loans, bonds, overdrafts, interest-bearing leases
- Does NOT include trade payables, deferred tax, operating liabilities

**Cash + Interest-Bearing Securities Screen:**
- If (cash + short-term investments + interest-bearing securities) > 33% of total assets → EXCLUDE
- Rationale: Company holds excessive amount of conventional financial assets

**Accounts Receivable Screen (some methodologies):**
- If accounts receivable > 49% or 70% (methodology dependent) of total assets → flag
  (Indicates a company that is effectively lending rather than trading)

**Data sources:**
- Latest annual financial statements (12-month trailing or most recent)
- Some methodologies use 24-month trailing averages for market-cap ratios
- SC Malaysia uses total assets; MSCI and DJIM use market capitalisation denominator

---

## STEP 3: NON-PERMISSIBLE INCOME (NPI) SCREEN

**NPI Definition:** Revenue from activities that are prohibited under Shariah.
Examples: interest income, revenue from conventional insurance, alcohol sales,
tobacco sales, pork sales, gambling revenue, adult content revenue.

**NPI Threshold:** 5% of total revenue (all four methodologies)

Calculation:
NPI % = Total Non-Permissible Revenue / Total Revenue × 100

If NPI % > 5% → EXCLUDE
If NPI % ≤ 5% → PASS (but requires PURIFICATION — see Step 4)
If NPI % = 0% → FULLY CLEAN

**Data source:** Annual report revenue breakdown, segment reporting.
If not disclosed: use analyst estimates or conservative assumption.

---

## STEP 4: PURIFICATION CALCULATION

For holdings that PASS the 5% NPI screen but have some non-permissible income:

**Purification Obligation:**
For each dividend received from such a company:
Purification Amount = Dividend Received × NPI % of that company

Total Portfolio Purification = Σ (Dividend from company i × NPI % of company i)

**Action:** Donate the purification amount to charity (sadaqah).
Do not retain. Cannot offset against income.

**Journal entry in investor's / fund's books:**
Dr: Purification Expense [Amount]
Cr: Charity Payable — Purification [Amount]

On payment:
Dr: Charity Payable — Purification [Amount]
Cr: Cash [Amount]

---

## STEP 5: SCREENING CONFLICT RESOLUTION

When different methodologies produce different results for the same company:

**Priority hierarchy (conservative approach):**
1. Apply the methodology specified in the fund's SSB-approved investment policy.
2. If the fund applies "most conservative of all methodologies" → exclude if any methodology excludes.
3. For borderline cases → refer to SSB for ruling. Do not trade without SSB determination.

**Common conflict scenarios:**
- SC Malaysia includes a company that MSCI excludes (e.g., different debt ratio denominators)
- DJIM includes a company with 4.9% NPI that a stricter SSB considers too close to limit
- Plantation companies: SC Malaysia includes palm oil; MSCI may screen for environmental reasons

---

## QUARTERLY REBALANCING WORKFLOW

1. Obtain updated Shariah-compliant securities list from each applicable methodology provider.
2. Compare against current portfolio holdings.
3. Identify newly NON-COMPLIANT holdings → immediate divestment required.
4. Identify newly COMPLIANT holdings → eligible for purchase.
5. For holdings that remain compliant: update NPI % from latest annual reports.
6. Recalculate portfolio-level purification obligation.
7. Produce SSB quarterly compliance report.

**Divestment timeline after compliance breach:**
Most SSBs allow 30 days to divest non-compliant holdings without triggering additional
Shariah liability. Confirm with the fund's specific SSB fatwa on divestment timing.

---

## MANDATORY QUARTERLY SSB REPORT — STRUCTURE

1. Portfolio composition: # and % of holdings by Shariah status (Compliant / Borderline / Non-Compliant)
2. Changes from prior quarter: additions to non-compliant list requiring divestment
3. Purification obligation: calculation, amount, recommended charities
4. Borderline holdings under SSB review
5. Recommended actions before next quarter
6. SSB attestation signature

---

## MANDATORY ANNUAL FUND DISCLOSURES

1. Shariah screening methodology adopted (and which authority approved it)
2. SSB composition and qualifications
3. Number of portfolio reviews conducted in the year
4. Non-compliant holdings identified and divested (number, % of portfolio affected)
5. Purification amounts paid and recipients
6. Any unresolved borderline cases and SSB rulings sought
