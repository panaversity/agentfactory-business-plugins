# Exercise 3: GCC Sukuk Issuance — Multi-Jurisdiction Accounting

## Scenario Profile

| Field                 | Value                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Issuer**            | Abu Dhabi National Energy Company (ADNEC)                                                                    |
| **Product**           | $500M 5-year ijarah sukuk                                                                                    |
| **Underlying Assets** | UAE power generation infrastructure leased to ADNEC                                                          |
| **Distribution Rate** | 5.25% p.a., semi-annual                                                                                      |
| **Listing**           | Nasdaq Dubai and London Stock Exchange                                                                       |
| **Jurisdictions**     | UAE (issuer), Bahrain (investor), Malaysia (investor), UK (investor)                                         |
| **Target Time**       | 60 minutes                                                                                                   |
| **Skills Required**   | `sukuk-issuer.md`, `sukuk-investor.md`, `bahrain-aaoifi.md`, `malaysia-mfrs.md`, `uae-ifrs.md`, `uk-ifrs.md` |

---

## Sukuk Structure Data

### Issuance Details

| Parameter                     | Value                                                           |
| ----------------------------- | --------------------------------------------------------------- |
| Total issuance                | $500,000,000                                                    |
| Tenor                         | 5 years                                                         |
| Distribution rate             | 5.25% p.a.                                                      |
| Distribution frequency        | Semi-annual (June 30 and December 31)                           |
| Semi-annual distribution      | $13,125,000                                                     |
| Total distributions over life | $131,250,000                                                    |
| Structure                     | Ijarah — assets leased from SPV to ADNEC                        |
| SPV                           | ADNEC Sukuk Limited (Cayman Islands)                            |
| Purchase undertaking          | ADNEC undertakes to repurchase assets at face value at maturity |
| Governing law                 | English law                                                     |

### Tranche Structure

| Tranche                  | Amount       | Distribution Rate | SPPI Test Consideration                                    |
| ------------------------ | ------------ | ----------------- | ---------------------------------------------------------- |
| Tranche A (Senior)       | $300,000,000 | 5.00% p.a. fixed  | Fixed rental — straightforward SPPI pass                   |
| Tranche B (Mezzanine)    | $150,000,000 | 5.50% p.a. fixed  | Fixed rental — SPPI pass                                   |
| Tranche C (Subordinated) | $50,000,000  | 6.25% p.a. fixed  | Higher return for subordination — SPPI assessment required |

### SPPI Test Data

| Factor                    | Assessment                                               |
| ------------------------- | -------------------------------------------------------- |
| Cash flows                | Fixed periodic rental + return of face value at maturity |
| Underlying assets         | Power generation infrastructure — tangible, identifiable |
| Purchase undertaking      | At face value — no equity-like upside/downside           |
| Subordination (Tranche C) | Absorbs first losses — potential SPPI complication       |
| Credit risk               | ADNEC is majority government-owned (Abu Dhabi)           |

---

## Investor Profiles

### Bahrain Investor — Gulf Finance House (AAOIFI)

| Item               | Value                                                               |
| ------------------ | ------------------------------------------------------------------- |
| Entity             | Gulf Finance House BSC                                              |
| Holding            | $50,000,000 (Tranche A)                                             |
| Framework          | AAOIFI FAS 25 (Investment in Sukuk, Shares and Similar Instruments) |
| Business model     | Hold to collect                                                     |
| Semi-annual income | $1,250,000                                                          |

### Malaysia Investor — Employees Provident Fund (MFRS)

| Item               | Value                                                      |
| ------------------ | ---------------------------------------------------------- |
| Entity             | EPF Shariah Savings Portfolio                              |
| Holding            | $75,000,000 (Tranche A: $50M, Tranche B: $25M)             |
| Framework          | MFRS 9                                                     |
| Business model     | Hold to collect                                            |
| Semi-annual income | $1,250,000 (Tranche A) + $687,500 (Tranche B) = $1,937,500 |

### UK Investor — Legal & General Islamic Fund (IFRS)

| Item               | Value                            |
| ------------------ | -------------------------------- |
| Entity             | L&G Shariah-compliant fund       |
| Holding            | $25,000,000 (Tranche B)          |
| Framework          | IFRS 9 / FRS 101                 |
| Business model     | Hold to collect and sell (FVOCI) |
| Semi-annual income | $687,500                         |

---

## Your Task

1. **UAE issuer accounting (IFRS)**: Determine whether ADNEC derecognises the power assets. Analyse the purchase undertaking's impact on derecognition. Classify the sukuk (financial liability vs. equity under IAS 32). Generate initial recognition journal entry.
2. **Bahrain investor (AAOIFI FAS 25)**: Classify the $50M holding. Generate entries for: initial recognition, semi-annual income, year-end measurement.
3. **Malaysia investor (MFRS 9)**: Apply business model and SPPI tests to both tranches. Classify at amortised cost. Generate entries for initial recognition and semi-annual income for both tranches.
4. **UK investor (IFRS 9)**: Apply FVOCI classification. Generate entries including OCI mark-to-market if market yields move +50bps after issuance.
5. **Cross-jurisdiction comparison**: Build a table showing how the same sukuk certificate is accounted for differently by each investor depending on their jurisdiction and framework.

---

## Expected Output

- Issuer journal entries (initial recognition of $500M proceeds, semi-annual distribution, maturity repurchase)
- 3 sets of investor journal entries (Bahrain AAOIFI, Malaysia MFRS, UK IFRS)
- SPPI test analysis for each tranche (noting Tranche C subordination risk)
- Comparison table: classification, measurement basis, income label, and balance sheet presentation per jurisdiction
- Discussion of why the purchase undertaking at face value means the issuer likely does NOT derecognise the assets (substance over form)
