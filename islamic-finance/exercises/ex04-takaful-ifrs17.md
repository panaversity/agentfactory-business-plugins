# Exercise 4: Global Takaful Operator — IFRS 17 and Wakala Model

## Scenario Profile

| Field               | Value                                                                |
| ------------------- | -------------------------------------------------------------------- |
| **Entity**          | Etiqa Takaful Berhad (Malaysia) — with UAE and UK comparators        |
| **Product**         | Family takaful (life) and general takaful under wakala model         |
| **Jurisdictions**   | Malaysia (MFRS 17), UAE (IFRS 17), UK (IFRS 17)                      |
| **Target Time**     | 50 minutes                                                           |
| **Skills Required** | `takaful-ifrs17.md`, `malaysia-mfrs.md`, `uae-ifrs.md`, `uk-ifrs.md` |

---

## Operator Financial Data — Malaysia (Etiqa Takaful Berhad)

### General Takaful Book

| Line Item                               | Amount (MYR millions) |
| --------------------------------------- | --------------------- |
| Gross written contributions             | 850                   |
| Wakala fee (30% of contributions)       | 255                   |
| Claims incurred                         | 410                   |
| Retakaful (reinsurance) ceded           | 125                   |
| Investment income on Participants' Fund | 68                    |
| Management expenses (operator)          | 180                   |
| Participants' Fund opening balance      | 1,200                 |

### Family Takaful Book

| Line Item                               | Amount (MYR millions) |
| --------------------------------------- | --------------------- |
| Gross written contributions             | 1,450                 |
| Wakala fee (25% of contributions)       | 362.5                 |
| Claims and benefits paid                | 780                   |
| Retakaful ceded                         | 210                   |
| Investment income on Participants' Fund | 195                   |
| Participants' Fund opening balance      | 4,800                 |

### Wakala Model Key Parameters

| Parameter                 | Value                                        |
| ------------------------- | -------------------------------------------- |
| Wakala fee rate (general) | 30% of gross contributions                   |
| Wakala fee rate (family)  | 25% of gross contributions                   |
| Surplus sharing (general) | 50% to participants, 50% retained in fund    |
| Qard hasan facility       | MYR 200M available from shareholder fund     |
| Qard hasan trigger        | Participants' Fund deficit exceeding MYR 50M |

---

## Qard Hasan Scenario

| Event                                       | Data                                                |
| ------------------------------------------- | --------------------------------------------------- |
| Catastrophe claims (Q3)                     | MYR 320M additional claims in general takaful       |
| Participants' Fund balance post-catastrophe | Deficit of MYR 85M                                  |
| Qard hasan drawn                            | MYR 85M from shareholder fund                       |
| Repayment terms                             | From future surpluses, no fixed timeline, no profit |

---

## UAE Comparator — Emirates Islamic Takaful

| Line Item                          | Amount (AED millions)        |
| ---------------------------------- | ---------------------------- |
| Gross written contributions        | 620                          |
| Wakala fee (28%)                   | 173.6                        |
| Claims incurred                    | 295                          |
| Participants' Fund opening balance | 480                          |
| Regulatory framework               | IFRS 17 as required by CBUAE |

## UK Comparator — Salaam Halal Insurance (hypothetical)

| Line Item                          | Amount (GBP millions)     |
| ---------------------------------- | ------------------------- |
| Gross written contributions        | 45                        |
| Wakala fee (32%)                   | 14.4                      |
| Claims incurred                    | 22                        |
| Participants' Fund opening balance | 38                        |
| Regulatory framework               | IFRS 17 / PRA Solvency II |

---

## Your Task

1. **IFRS 17 fundamental question**: Does the takaful operator have insurance contracts on its own books? Is the Participants' Fund subject to IFRS 17? What is BNM Malaysia's ruling?
2. **Malaysia (MFRS 17)**: Build Etiqa's income statement showing: (a) Operator's own income statement (wakala fee only); (b) Participants' Fund statement (contributions, claims, retakaful, investment income)
3. **Qard hasan accounting**: When the operator provides MYR 85M qard hasan to cover the fund deficit: journal entries in operator's books AND in Participants' Fund; classification of the receivable (is it an asset or is recovery uncertain?); disclosure requirements
4. **UAE comparison**: How does the UAE takaful operator present its IFRS 17 statements WITHOUT BNM-level guidance? What judgments must the UAE entity make that Malaysia has pre-determined?
5. **UK comparison**: How does PRA Solvency II interact with IFRS 17 for a UK takaful operator? Is the Participants' Fund risk-bearing capital from a PRA perspective?

---

## Expected Output

- Two-panel income statement for Etiqa (Operator panel + Participants' Fund panel)
- Qard hasan journal entries (4 entries: draw-down in operator books, receipt in fund books, partial repayment from surplus, year-end assessment)
- Comparison table: Malaysia vs. UAE vs. UK treatment of the SAME wakala model
- Discussion of the core IFRS 17 tension: conventional insurance assumes the insurer bears risk; takaful assumes participants collectively bear risk — and how each jurisdiction resolves this
- Note on why the Participants' Fund balance is NOT operator equity
