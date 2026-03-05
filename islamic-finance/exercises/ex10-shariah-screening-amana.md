# Exercise 10: Shariah Portfolio Screening — Amana Income Fund

## Scenario Profile

| Field                    | Value                                                              |
| ------------------------ | ------------------------------------------------------------------ |
| **Entity**               | Saturna Capital — Amana Income Fund (US-based Islamic fund)        |
| **Domain**               | Shariah Compliance — Portfolio Screening                           |
| **Screening Frameworks** | SC Malaysia, Saudi Tadawul, AAOIFI Standard 21, MSCI Islamic Index |
| **Target Time**          | 45 minutes                                                         |
| **Skills Required**      | `shariah-screening-global.md`                                      |

---

## Global Screening Thresholds

| Criterion                                         | SC Malaysia                                                                          | Tadawul (Saudi) | AAOIFI Std 21 | MSCI Islamic                              |
| ------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------- | ------------- | ----------------------------------------- |
| Debt / total assets                               | < 33%                                                                                | < 33%           | < 30%         | < 33.33%                                  |
| Cash + interest-bearing securities / total assets | < 33%                                                                                | < 33%           | < 30%         | < 33.33%                                  |
| Non-permissible income / total revenue            | < 5%                                                                                 | < 5%            | < 5%          | < 5%                                      |
| Accounts receivable / total assets                | N/A                                                                                  | < 49%           | < 45%         | < 49%                                     |
| **Sector exclusions**                             | Alcohol, tobacco, gambling, weapons, pork, conventional finance, adult entertainment | Same            | Same          | Same + nuclear weapons, civilian firearms |

---

## Amana Income Fund — 10 Equity Positions

### Position 1: Microsoft Corp (MSFT)

| Metric                    | Value      | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | ---------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 18.2%      | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 22.5%      | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 0.3%       | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 12.8%      | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Technology | OK          | OK       | OK        | OK       |
| **Overall**               |            | **PASS**    | **PASS** | **PASS**  | **PASS** |

### Position 2: Johnson & Johnson (JNJ)

| Metric                    | Value      | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | ---------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 28.5%      | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 15.3%      | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 1.2%       | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 8.9%       | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Healthcare | OK          | OK       | OK        | OK       |
| **Overall**               |            | **PASS**    | **PASS** | **PASS**  | **PASS** |

### Position 3: Sime Darby Plantation (Malaysia)

| Metric                    | Value                 | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI           |
| ------------------------- | --------------------- | ----------- | -------- | --------- | -------------- |
| Debt / Total Assets       | 22.1%                 | PASS        | PASS     | PASS      | PASS           |
| Cash + IBS / Total Assets | 8.4%                  | PASS        | PASS     | PASS      | PASS           |
| Non-permissible income %  | 0.8%                  | PASS        | PASS     | PASS      | PASS           |
| A/R / Total Assets        | 11.2%                 | N/A         | PASS     | PASS      | PASS           |
| Sector                    | Palm oil / Plantation | OK          | OK       | OK        | **FAIL** (ESG) |
| **Overall**               |                       | **PASS**    | **PASS** | **PASS**  | **FAIL**       |

### Position 4: Saudi Telecom (STC)

| Metric                    | Value   | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | ------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 35.2%   | **FAIL**    | **FAIL** | **FAIL**  | **FAIL** |
| Cash + IBS / Total Assets | 12.1%   | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 0.4%    | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 18.5%   | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Telecom | OK          | OK       | OK        | OK       |
| **Overall**               |         | **FAIL**    | **FAIL** | **FAIL**  | **FAIL** |

### Position 5: HSBC Holdings

| Metric      | Value                | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ----------- | -------------------- | ----------- | -------- | --------- | -------- |
| Sector      | Conventional banking | **FAIL**    | **FAIL** | **FAIL**  | **FAIL** |
| **Overall** |                      | **FAIL**    | **FAIL** | **FAIL**  | **FAIL** |

_Note: Conventional financial services is an absolute sector exclusion under all four screens._

### Position 6: Nestlé SA

| Metric                    | Value           | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | --------------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 31.8%           | PASS        | PASS     | **FAIL**  | PASS     |
| Cash + IBS / Total Assets | 14.2%           | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 0.1%            | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 9.5%            | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Food & Beverage | OK          | OK       | OK        | OK       |
| **Overall**               |                 | **PASS**    | **PASS** | **FAIL**  | **PASS** |

### Position 7: Aramco (Saudi Arabia)

| Metric                    | Value     | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | --------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 12.5%     | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 18.9%     | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 0.6%      | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 14.2%     | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Oil & Gas | OK          | OK       | OK        | OK       |
| **Overall**               |           | **PASS**    | **PASS** | **PASS**  | **PASS** |

### Position 8: Unilever PLC (UK)

| Metric                    | Value          | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | -------------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 29.4%          | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 11.8%          | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 6.2%           | **FAIL**    | **FAIL** | **FAIL**  | PASS     |
| A/R / Total Assets        | 7.3%           | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Consumer Goods | OK          | OK       | OK        | OK       |
| **Overall**               |                | **FAIL**    | **FAIL** | **FAIL**  | **PASS** |

_Note: MSCI uses a different definition of non-permissible income that excludes certain revenue streams included by the other three frameworks._

### Position 9: Petronas Chemicals (Malaysia)

| Metric                    | Value     | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | --------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 8.3%      | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 25.1%     | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 0.2%      | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 15.8%     | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Chemicals | OK          | OK       | OK        | OK       |
| **Overall**               |           | **PASS**    | **PASS** | **PASS**  | **PASS** |

### Position 10: Etisalat (UAE)

| Metric                    | Value   | SC Malaysia | Tadawul  | AAOIFI 21 | MSCI     |
| ------------------------- | ------- | ----------- | -------- | --------- | -------- |
| Debt / Total Assets       | 24.6%   | PASS        | PASS     | PASS      | PASS     |
| Cash + IBS / Total Assets | 28.7%   | PASS        | PASS     | PASS      | PASS     |
| Non-permissible income %  | 3.8%    | PASS        | PASS     | PASS      | PASS     |
| A/R / Total Assets        | 42.1%   | N/A         | PASS     | PASS      | PASS     |
| Sector                    | Telecom | OK          | OK       | OK        | OK       |
| **Overall**               |         | **PASS**    | **PASS** | **PASS**  | **PASS** |

---

## Dividend and Purification Data

| Parameter                                             | Value                                                |
| ----------------------------------------------------- | ---------------------------------------------------- |
| Total quarterly dividends received                    | USD 4,200,000                                        |
| Weighted average non-Shariah income ratio (portfolio) | 1.8%                                                 |
| Purification amount                                   | USD 4,200,000 x 1.8% = USD 75,600                    |
| Eligible charity recipients                           | Any registered charity (not the fund's own expenses) |

---

## Your Task

1. **Build the global screening workbook**: Complete the pass/fail matrix for all 10 positions across all 4 screening frameworks. Identify which positions pass ALL four and which have divergences
2. **Purification calculation**: Calculate the quarterly purification obligation. Generate journal entry (Dr Purification Expense, Cr Purification Payable). Draft unitholder disclosure
3. **Screening divergence analysis**: For positions 3 (Sime Darby), 6 (Nestlé), and 8 (Unilever) — explain WHY the screens disagree. Which screen should the fund adopt as governing? Document the resolution policy
4. **Quarterly SSB report**: Draft the Shariah Supervisory Board quarterly report with: compliance status, changes from prior quarter, purification, stocks under review, recommended actions
5. **Scheduled screening task**: Write the quarterly automated screening workflow specification

---

## Expected Output

- Completed 10x4 screening matrix with PASS/FAIL for each cell
- Purification journal entry and unitholder disclosure
- Divergence analysis for 3 stocks with documented resolution policy
- SSB quarterly report formatted for a 3-member global board (USA, Malaysia, Saudi)
- Quarterly screening task specification with trigger, data sources, output format, escalation rules
- Key insight: different screening methodologies produce different results for the same company — the fund must have a documented governing methodology
