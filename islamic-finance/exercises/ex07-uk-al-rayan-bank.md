# Exercise 7: UK Islamic Bank — Al Rayan Bank

## Scenario Profile

| Field               | Value                                                                           |
| ------------------- | ------------------------------------------------------------------------------- |
| **Entity**          | Al Rayan Bank plc (UK) — largest UK Islamic bank                                |
| **Products**        | DM home finance, mudaraba savings, murabaha business finance, ijarah buy-to-let |
| **Jurisdiction**    | UK (IFRS / FRS 101, PRA/FCA, HMRC)                                              |
| **Target Time**     | 50 minutes                                                                      |
| **Skills Required** | `musharaka-dm.md`, `murabaha.md`, `uk-ifrs.md`                                  |

---

## DM Home Finance Portfolio

### Portfolio Summary (GBP)

| Parameter                            | Value                              |
| ------------------------------------ | ---------------------------------- |
| Total portfolio                      | GBP 200,000,000                    |
| Number of facilities                 | 850                                |
| Average facility size                | GBP 235,294                        |
| Average bank share (Day 1)           | 80% of property value              |
| Average monthly rental on bank share | Approximately 4.2% p.a. equivalent |
| Average monthly equity purchase      | GBP 1,000 per facility             |

### Sample Transaction

| Parameter                             | Value             |
| ------------------------------------- | ----------------- |
| Property value                        | GBP 625,000       |
| Bank's initial share                  | GBP 500,000 (80%) |
| Customer's initial share              | GBP 125,000 (20%) |
| Monthly rental on bank's share        | GBP 1,750         |
| Monthly equity purchase by customer   | GBP 1,000         |
| Implied annual rate on bank's capital | ~4.2% p.a.        |
| Expected buy-out period               | ~25 years         |

### DM Portfolio Aging

| Origination Year | Outstanding Bank Share (GBP millions) | Rental Yield      | Remaining Units |
| ---------------- | ------------------------------------- | ----------------- | --------------- |
| 2019             | 35                                    | 3.8%              | 140             |
| 2020             | 28                                    | 3.5%              | 115             |
| 2021             | 42                                    | 4.0%              | 175             |
| 2022             | 38                                    | 4.5%              | 160             |
| 2023             | 32                                    | 4.8%              | 135             |
| 2024             | 25                                    | 5.2%              | 125             |
| **Total**        | **200**                               | **4.2% weighted** | **850**         |

---

## HMRC Tax Data

### Finance Act 2005 — Alternative Finance Arrangements

| Conventional Equivalent       | Islamic Structure    | HMRC Treatment                                                 |
| ----------------------------- | -------------------- | -------------------------------------------------------------- |
| Mortgage interest (bank)      | DM rental income     | Treated as interest equivalent for tax                         |
| Mortgage interest (customer)  | DM rental payments   | Tax-deductible as mortgage interest equivalent                 |
| Mortgage principal (customer) | DM equity purchase   | Capital repayment — not tax-deductible                         |
| SDLT on property purchase     | SDLT on DM structure | Single SDLT charge (not double — Finance Act 2003 s71A relief) |

### Customer Tax Position

| Item                     | Annual Amount (GBP)     | Tax Treatment                       |
| ------------------------ | ----------------------- | ----------------------------------- |
| Rental payments to bank  | 21,000                  | Deductible as finance cost (if BTL) |
| Equity purchase payments | 12,000                  | Capital — not deductible            |
| Total payments           | 33,000                  |                                     |
| SDLT on initial purchase | 21,250 (on GBP 625,000) | Single charge, not double           |

---

## Construction Finance Scenario

### Client: UK Property Developer

| Parameter                          | Value                                         |
| ---------------------------------- | --------------------------------------------- |
| Client                             | Meridian Developments Ltd                     |
| Project                            | 45-unit residential development, South London |
| Total development cost             | GBP 8,000,000                                 |
| Al Rayan facility                  | DM construction facility                      |
| Bank contribution                  | GBP 6,000,000 (75%)                           |
| Developer contribution             | GBP 2,000,000 (25%)                           |
| Construction period                | 24 months                                     |
| Post-completion buy-out            | 5 years                                       |
| Developer role during construction | Agent (wakeel) for the bank                   |

### Construction Draw-Down Schedule

| Phase            | Month | Draw-Down (GBP) | Cumulative | Bank Share |
| ---------------- | ----- | --------------- | ---------- | ---------- |
| Land acquisition | 0     | 2,500,000       | 2,500,000  | 1,875,000  |
| Foundation       | 1-4   | 1,200,000       | 3,700,000  | 2,775,000  |
| Structure        | 5-12  | 2,800,000       | 6,500,000  | 4,875,000  |
| Fit-out          | 13-20 | 1,200,000       | 7,700,000  | 5,775,000  |
| Completion       | 21-24 | 300,000         | 8,000,000  | 6,000,000  |

---

## PRA Capital Ratios

### Al Rayan Bank Regulatory Capital

| Item                        | Amount (GBP millions) | Ratio |
| --------------------------- | --------------------- | ----- |
| CET1 Capital                | 180                   | 14.4% |
| Tier 1 Capital              | 180                   | 14.4% |
| Total Capital               | 195                   | 15.6% |
| Risk-Weighted Assets (RWA)  | 1,250                 |       |
| Minimum CET1 requirement    | 4.5%                  | 56.25 |
| Capital conservation buffer | 2.5%                  | 31.25 |
| Total CET1 requirement      | 7.0%                  | 87.50 |
| CET1 surplus                |                       | 92.50 |

### RWA for DM Home Finance

| Category                         | Risk Weight | Application                          |
| -------------------------------- | ----------- | ------------------------------------ |
| Residential mortgage (LTV < 80%) | 35%         | Standard PRA residential mortgage RW |
| Residential mortgage (LTV > 80%) | 75%         | Higher RW for higher LTV             |
| Construction phase exposure      | 150%        | Speculative development              |
| Post-completion (occupied)       | 35%         | Once completed and occupied          |

---

## Your Task

1. **DM home finance IFRS 9 treatment**: Apply business model and SPPI tests. Is this a financial instrument (loan in substance) or a property co-ownership? Generate Month 1 journal entries under IFRS 9
2. **HMRC tax treatment**: Explain how HMRC characterises rental income and equity payments for: (a) the bank's tax computation; (b) the customer's tax position. Address SDLT relief for Islamic mortgages
3. **Construction finance**: Classify the DM construction facility — istisna'a, construction DM, or wakala? Account for the construction-period investment under IFRS 9. When does income recognition begin — draw-down or completion?
4. **PRA regulatory capital**: Calculate RWA for the DM home finance portfolio. Does the Shariah structure change the RWA classification vs. conventional mortgage? Identify PRA returns required
5. **Client advisory report**: Draft comparison of conventional vs. Islamic construction finance covering: cost comparison, HMRC treatment, IFRS 16 lessee accounting, Shariah compliance certification

---

## Expected Output

- IFRS 9 classification analysis for DM (financial instrument at amortised cost in most cases)
- Month 1 journal entries: rental income recognition, equity purchase accounting
- HMRC advisory note for the property developer
- RWA calculation for the GBP 200M DM portfolio
- Construction finance accounting timeline (no income during construction, income from completion)
- Client-facing advisory comparing Islamic vs. conventional construction finance
- Confirmation that PRA treats Islamic and conventional banking identically for regulatory capital
