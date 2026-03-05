# Exercise 1: Murabaha Income Schedule — Bahrain (AAOIFI) vs. Malaysia (MFRS/IFRS 9)

## Scenario Profile

| Field               | Value                                                            |
| ------------------- | ---------------------------------------------------------------- |
| **Entity**          | Islamic banking group with subsidiaries in Bahrain and Malaysia  |
| **Product**         | Murabaha financing — cost-plus sale with deferred payment        |
| **Jurisdictions**   | Bahrain (AAOIFI FAS 2) and Malaysia (MFRS 9 / IFRS 9 equivalent) |
| **Target Time**     | 35 minutes                                                       |
| **Skills Required** | `murabaha.md`, `bahrain-aaoifi.md`, `malaysia-mfrs.md`           |

---

## Transaction Data

Both subsidiaries enter identical murabaha transactions:

| Parameter               | Bahrain Entity            | Malaysia Entity           |
| ----------------------- | ------------------------- | ------------------------- |
| Cost to bank            | BHD 500,000               | MYR 500,000               |
| Mark-up rate            | 18% per annum             | 18% per annum             |
| Tenure                  | 18 months                 | 18 months                 |
| Instalment frequency    | Monthly equal instalments | Monthly equal instalments |
| Total mark-up           | BHD 135,000               | MYR 135,000               |
| Total amount receivable | BHD 635,000               | MYR 635,000               |
| Monthly instalment      | BHD 35,277.78             | MYR 35,277.78             |

### Derived Amounts

| Item                               | Calculation                                                      | Amount                                |
| ---------------------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| Total selling price                | 500,000 + (500,000 x 18% x 1.5 years)                            | 635,000                               |
| Deferred murabaha income (Day 1)   | 135,000                                                          | 135,000                               |
| Monthly instalment                 | 635,000 / 18                                                     | 35,277.78                             |
| Effective profit rate (for MFRS 9) | IRR solving for 18 payments of 35,277.78 on principal of 500,000 | ~1.38% per month (~16.56% annualised) |

---

## Amortisation Schedule Template — Bahrain (AAOIFI FAS 2)

**Income label**: "Murabaha Income" (NEVER "interest income")

| Month     | Opening Murabaha Receivable | Monthly Instalment | Principal Portion | Murabaha Income (Profit Portion) | Deferred Murabaha Income Released | Closing Murabaha Receivable |
| --------- | --------------------------- | ------------------ | ----------------- | -------------------------------- | --------------------------------- | --------------------------- |
| 1         | 635,000.00                  | 35,277.78          | \_\_\_            | \_\_\_                           | \_\_\_                            | \_\_\_                      |
| 2         | \_\_\_                      | 35,277.78          | \_\_\_            | \_\_\_                           | \_\_\_                            | \_\_\_                      |
| 3         | \_\_\_                      | 35,277.78          | \_\_\_            | \_\_\_                           | \_\_\_                            | \_\_\_                      |
| ...       | ...                         | ...                | ...               | ...                              | ...                               | ...                         |
| 18        | \_\_\_                      | 35,277.78          | \_\_\_            | \_\_\_                           | \_\_\_                            | \_\_\_                      |
| **Total** |                             | **635,000.00**     | **500,000.00**    | **135,000.00**                   | **135,000.00**                    | **0.00**                    |

**AAOIFI FAS 2 note**: Profit allocation may use proportional method (straight-line over selling price) or effective rate. Confirm which method the Bahrain entity's accounting policy specifies.

---

## Amortisation Schedule Template — Malaysia (MFRS 9)

**Income label**: "Profit from Islamic Financing" (NEVER "interest income", NEVER "Murabaha Income")

| Month     | Opening Amortised Cost | Monthly Instalment | Principal Repayment | Profit from Islamic Financing (EIR method) | Closing Amortised Cost |
| --------- | ---------------------- | ------------------ | ------------------- | ------------------------------------------ | ---------------------- |
| 1         | 500,000.00             | 35,277.78          | \_\_\_              | \_\_\_                                     | \_\_\_                 |
| 2         | \_\_\_                 | 35,277.78          | \_\_\_              | \_\_\_                                     | \_\_\_                 |
| 3         | \_\_\_                 | 35,277.78          | \_\_\_              | \_\_\_                                     | \_\_\_                 |
| ...       | ...                    | ...                | ...                 | ...                                        | ...                    |
| 18        | \_\_\_                 | 35,277.78          | \_\_\_              | \_\_\_                                     | \_\_\_                 |
| **Total** |                        | **635,000.00**     | **500,000.00**      | **135,000.00**                             | **0.00**               |

**MFRS 9 note**: Uses effective profit rate (EPR) method — the constant rate applied to the amortised cost balance each period. The opening balance is the cost (500,000), not the selling price (635,000).

---

## Your Task

1. **Build the Bahrain AAOIFI schedule** — complete all cells using proportional allocation method under AAOIFI FAS 2
2. **Build the Malaysia MFRS schedule** — complete all cells using effective profit rate method under MFRS 9
3. **Compare the two schedules numerically** — are the total income amounts identical? Are the period-by-period allocations identical or different?
4. **Generate Month 1 journal entries** for both jurisdictions — all four entries per entity (initial recognition, instalment receipt, income recognition, deferred income release)
5. **Document every labelling difference** between the two sets of entries

---

## Expected Output

- Two completed amortisation schedules (18 rows each)
- Numerical comparison showing whether total income is identical (it should be) and whether period allocation differs (it may, depending on method)
- 8 journal entries total (4 per jurisdiction)
- A summary paragraph explaining: same economics, different labels, different presentation, different disclosure requirements
- Identification that AAOIFI FAS 2 proportional method and MFRS 9 effective rate method may produce slightly different period allocations but identical total income
