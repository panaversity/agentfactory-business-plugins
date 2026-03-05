# Exercise 6: Saudi Arabia — Alinma Bank IFI Review

## Scenario Profile

| Field               | Value                                                                |
| ------------------- | -------------------------------------------------------------------- |
| **Entity**          | Alinma Bank (Saudi Arabia) — benchmarked against Al Rajhi Bank       |
| **Domain**          | Islamic Accounting — Saudi Arabia (IFRS + ZATCA zakat + Vision 2030) |
| **Jurisdiction**    | Saudi Arabia (IFRS as adopted in KSA, ZATCA, SAMA)                   |
| **Target Time**     | 55 minutes                                                           |
| **Skills Required** | `murabaha.md`, `saudi-ifrs.md`, `zakat-global.md`                    |

---

## Alinma Bank Financial Data

### Balance Sheet Extract (SAR millions)

| Item                          | Amount  |
| ----------------------------- | ------- |
| Share capital                 | 20,000  |
| Statutory reserves            | 4,500   |
| Retained earnings             | 3,200   |
| Total equity                  | 27,700  |
| Fixed assets (net)            | 1,800   |
| Long-term sukuk investments   | 5,000   |
| Murabaha receivables (net)    | 48,000  |
| Home finance (DM) receivables | 32,000  |
| Other Islamic financing       | 8,500   |
| Total Islamic financing       | 88,500  |
| Customer deposits             | 72,000  |
| Total assets                  | 125,000 |

### Murabaha Portfolio Breakdown

| Tenor Bucket     | Outstanding (SAR millions) | Weighted Average Rate | NPF Ratio |
| ---------------- | -------------------------- | --------------------- | --------- |
| Less than 1 year | 18,000                     | 6.8%                  | 1.2%      |
| 1-3 years        | 20,000                     | 7.2%                  | 2.1%      |
| Over 3 years     | 10,000                     | 7.8%                  | 3.5%      |
| **Total**        | **48,000**                 | **7.2%**              | **2.0%**  |

### DM Home Finance Portfolio

| Year of Origination | Outstanding (SAR millions) | Monthly Rental Yield  | Remaining Tenor |
| ------------------- | -------------------------- | --------------------- | --------------- |
| 2020                | 8,000                      | 5.2%                  | 22 years        |
| 2021                | 7,500                      | 4.8%                  | 23 years        |
| 2022                | 6,500                      | 5.5%                  | 24 years        |
| 2023                | 5,500                      | 6.1%                  | 25 years        |
| 2024                | 4,500                      | 6.5%                  | 26 years        |
| **Total**           | **32,000**                 | **5.6% weighted avg** |                 |

---

## ZATCA Zakat Computation Data

### Zakat Base Items

| Item                        | Amount (SAR millions) | Include/Deduct |
| --------------------------- | --------------------- | -------------- |
| Share capital               | 20,000                | Include        |
| Statutory reserves          | 4,500                 | Include        |
| Retained earnings           | 3,200                 | Include        |
| Provisions (general)        | 1,200                 | Include        |
| **Gross zakat base**        | **28,900**            |                |
| Fixed assets (net)          | (1,800)               | Deduct         |
| Long-term sukuk investments | (5,000)               | Deduct         |
| **Net ZATCA zakat base**    | **22,100**            |                |
| Zakat rate                  | 2.5%                  |                |
| **ZATCA zakat obligation**  | **552.5**             |                |

---

## PIF Sukuk Investment Data

| Parameter             | Value                                      |
| --------------------- | ------------------------------------------ |
| Holding               | SAR 2,000,000,000 face value               |
| Structure             | PIF sukuk (wakala structure)               |
| Distribution rate     | 4.25% p.a.                                 |
| Tenor                 | 7 years (3 remaining)                      |
| IFRS 9 classification | FVOCI (hold to collect and sell)           |
| Current fair value    | SAR 1,920,000,000 (yield +100bps scenario) |

### PIF Sukuk Mark-to-Market Scenario

| Scenario   | Market Yield Change | Fair Value Impact | OCI Impact (SAR millions) |
| ---------- | ------------------- | ----------------- | ------------------------- |
| Base case  | 0 bps               | 2,000             | 0                         |
| Yield rise | +100 bps            | \_\_\_            | \_\_\_                    |
| Yield fall | -50 bps             | \_\_\_            | \_\_\_                    |

**Duration**: ~2.8 years (modified duration for remaining 3-year tenor)

**Impact calculation**: Face value x modified duration x yield change = approximate FV change

---

## Saudi Electricity Green Sukuk Data

| Parameter                   | Value                                                   |
| --------------------------- | ------------------------------------------------------- |
| Alinma holding              | SAR 500,000,000                                         |
| Structure                   | Green sukuk — funding renewable energy projects         |
| Distribution rate           | 4.50% p.a.                                              |
| Green framework             | Saudi Electricity Company Sustainable Finance Framework |
| ESG disclosure requirements | SAMA encouraged (not yet mandatory)                     |

---

## Your Task

1. **IFRS murabaha benchmarking**: How does Al Rajhi classify and present murabaha receivables? Apply those benchmark practices to Alinma's accounting policy review
2. **ZATCA zakat computation**: Calculate the full ZATCA zakat base using the formula above. Generate the journal entry. Note the difference between ZATCA zakat and AAOIFI Governance Standard 9 zakat
3. **PIF sukuk accounting**: Classify under IFRS 9 (business model + SPPI). Generate entries for initial recognition and quarterly income. Calculate mark-to-market OCI impact under the +100bps yield rise scenario
4. **Saudi Electricity green sukuk**: Draft the accounting policy note and IFRS 7 disclosures for the green sukuk holding. Note SAMA ESG disclosure guidance
5. **Management accounts**: Produce monthly management accounts with: murabaha income by tenor, DM income trend, sukuk portfolio income and mark-to-market, zakat accrual, key ratios (Net Financing Margin, NPF ratio, Coverage ratio)

---

## Expected Output

- ZATCA zakat calculation worksheet with journal entry (Dr Zakat Expense SAR 552.5M, Cr Zakat Payable SAR 552.5M)
- PIF sukuk OCI impact calculation (~SAR 56M loss for +100bps on 2.8 duration)
- Comparison note: ZATCA formula vs. AAOIFI Hanafi methodology
- Monthly management accounts template formatted for Saudi board
- Green sukuk accounting policy note
- All figures in SAR, all labels Saudi IFRS-compliant
