# Exercise 2: Ijarah Accounting Across Four Jurisdictions

## Scenario Profile

| Field               | Value                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------- |
| **Entity**          | Islamic bank providing equipment financing via IMB (Ijarah Muntahia Bittamleek)       |
| **Product**         | Ijarah / IMB — operating lease with ownership transfer at end                         |
| **Jurisdictions**   | Bahrain (AAOIFI FAS 32), Malaysia (MFRS 16), UAE (IFRS 16), UK (IFRS 16)              |
| **Target Time**     | 50 minutes                                                                            |
| **Skills Required** | `ijarah-imb.md`, `bahrain-aaoifi.md`, `malaysia-mfrs.md`, `uae-ifrs.md`, `uk-ifrs.md` |

---

## Transaction Data

Identical transaction in all four jurisdictions:

| Parameter                 | Value                                 |
| ------------------------- | ------------------------------------- |
| Asset cost                | $2,000,000                            |
| Monthly rental            | $40,000                               |
| Implied annual rate       | ~18% p.a.                             |
| Lease tenure              | 5 years (60 months)                   |
| Asset useful life         | 10 years                              |
| Ownership transfer        | At end of lease, by nominal sale ($1) |
| Total rentals over tenure | $2,400,000                            |

### Key Financial Derivations

| Item                                               | Value       |
| -------------------------------------------------- | ----------- |
| Total rental income (5 years)                      | $2,400,000  |
| Annual rental income                               | $480,000    |
| Annual depreciation (10-year life)                 | $200,000    |
| Annual profit (AAOIFI: rental minus depreciation)  | $280,000    |
| Implicit rate in lease                             | ~18.0% p.a. |
| Present value of lease payments (at implicit rate) | $2,000,000  |

---

## Jurisdiction-Specific Parameters

### Bahrain — AAOIFI FAS 32 (Lessor)

| Item                | Treatment                                                              |
| ------------------- | ---------------------------------------------------------------------- |
| Governing standard  | AAOIFI FAS 32 (Ijarah and Ijarah Muntahia Bittamleek)                  |
| Asset recognition   | Bank recognises ijarah asset at cost ($2,000,000) on its balance sheet |
| Depreciation        | Over asset useful life (10 years), NOT the lease term (5 years)        |
| Annual depreciation | $200,000                                                               |
| Income recognition  | Rental income recognised monthly: $40,000/month                        |
| Annual profit       | $480,000 rental - $200,000 depreciation = $280,000                     |
| Balance sheet label | "Ijarah Assets" (NEVER "Property, Plant and Equipment")                |
| Income label        | "Income from Ijarah" (NEVER "Lease income" or "Rental income")         |

### Malaysia — MFRS 16 (Lessor)

| Item                            | Treatment                                                                |
| ------------------------------- | ------------------------------------------------------------------------ |
| Governing standard              | MFRS 16 (equivalent to IFRS 16)                                          |
| Classification test             | Does this qualify as a finance lease? Transfer of ownership at end = YES |
| If finance lease                | Derecognise asset, recognise net investment in lease                     |
| Net investment in lease (Day 1) | $2,000,000 (PV of lease payments + residual)                             |
| Income recognition              | Effective profit rate method on net investment balance                   |
| Income label                    | "Profit from Islamic Financing"                                          |

### UAE — IFRS 16 (Lessor)

| Item                | Treatment                                                                |
| ------------------- | ------------------------------------------------------------------------ |
| Governing standard  | IFRS 16                                                                  |
| Classification test | Same as Malaysia — finance lease                                         |
| Treatment           | Same as MFRS 16                                                          |
| Income label        | "Financing Income" or "Income from Ijarah Financing" (per entity policy) |
| Regulator           | CBUAE                                                                    |

### UK — IFRS 16 (Lessor)

| Item                | Treatment                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Governing standard  | IFRS 16 / FRS 101                                                                           |
| Classification test | Same — finance lease                                                                        |
| Treatment           | Same as IFRS 16                                                                             |
| Income label        | "Financing Income"                                                                          |
| Tax treatment       | HMRC Alternative Finance Arrangements — treated as equivalent to conventional lease for tax |
| Regulator           | PRA/FCA                                                                                     |

---

## Your Task

1. **Bahrain (AAOIFI FAS 32)**: Build the 5-year lessor schedule — annual rows showing: ijarah asset carrying value, depreciation, rental income, net profit
2. **Malaysia (MFRS 16)**: Build the 5-year finance lease schedule — monthly/annual rows showing: net investment in lease, rental received, profit recognised (effective rate), principal reduction
3. **UAE (IFRS 16)**: Build the same finance lease schedule as Malaysia (numbers identical, labels may differ)
4. **UK (IFRS 16)**: Build the same finance lease schedule, plus draft the HMRC tax note explaining Alternative Finance Arrangements treatment
5. **Comparison table**: Side-by-side annual P&L impact for all four jurisdictions showing income recognised per year

---

## Expected Output

- 4 completed schedules (one per jurisdiction)
- Bahrain schedule will show DIFFERENT annual profit pattern than the other three (because AAOIFI keeps the asset on balance sheet with straight-line depreciation)
- Malaysia/UAE/UK schedules will show SAME numbers (all apply IFRS 16 finance lease) but different labels
- Comparison table showing Year 1-5 income per jurisdiction
- Explanation of why Bahrain produces a flat annual profit while IFRS jurisdictions produce declining profit (front-loaded under effective rate method)
- UK HMRC note on tax equivalence
