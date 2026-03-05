# Exercise 13: Islamic Fintech and Digital Banking — Accounting for New Structures

## Scenario Profile

| Field               | Value                                                                             |
| ------------------- | --------------------------------------------------------------------------------- |
| **Domain**          | Islamic Finance Innovation — 4 fintech scenarios                                  |
| **Jurisdictions**   | Malaysia, UAE, UK                                                                 |
| **Target Time**     | 40 minutes                                                                        |
| **Skills Required** | `murabaha.md`, `sukuk-issuer.md`, `malaysia-mfrs.md`, `uae-ifrs.md`, `uk-ifrs.md` |

---

## Scenario 1: Digital Murabaha Platform — HelloGold (Malaysia)

### Entity Profile

| Parameter         | Value                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| Entity            | HelloGold Sdn Bhd (Malaysia)                                                                       |
| Product           | Digital gold murabaha via mobile app                                                               |
| Structure         | Platform (wakeel/agent) purchases gold at spot, sells to customer at mark-up with deferred payment |
| Physical delivery | None — gold held in vault, customer holds digital certificate                                      |
| Regulatory status | Licensed by SC Malaysia                                                                            |
| Framework         | MFRS 9 (platform), MFRS 15 (wakala fee)                                                            |

### Transaction Data

| Parameter                       | Value                          |
| ------------------------------- | ------------------------------ |
| Gold spot price (cost)          | MYR 350 per gram               |
| Selling price to customer       | MYR 385 per gram (10% mark-up) |
| Deferred payment period         | 6 months                       |
| Average transaction size        | MYR 3,850 (10 grams)           |
| Monthly transactions            | 12,000                         |
| Monthly gross transaction value | MYR 46,200,000                 |
| Platform wakala fee             | 2.5% of transaction value      |
| Monthly wakala fee income       | MYR 1,155,000                  |
| Bank murabaha income (mark-up)  | MYR 4,200,000 / month          |

### Accounting Questions

| Question                           | Considerations                                                           |
| ---------------------------------- | ------------------------------------------------------------------------ |
| Valid murabaha or tawarruq?        | No physical delivery to customer — commodity murabaha characteristics    |
| Platform receivable classification | MFRS 9 amortised cost if SPPI passes                                     |
| Revenue recognition split          | Platform earns wakala fee (MFRS 15); Bank earns murabaha income (MFRS 9) |
| BNM/SC licensing                   | E-money, digital investment, or Islamic banking?                         |

---

## Scenario 2: Robo-Adviser — Wahed Invest (UK/US)

### Entity Profile

| Parameter              | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| Entity                 | Wahed Invest Ltd (UK-registered, US operations)            |
| Product                | Shariah-compliant robo-advisory investment platform        |
| Structure              | Discretionary portfolio management using Islamic screening |
| AUM                    | USD 280,000,000                                            |
| Number of clients      | 45,000                                                     |
| Average portfolio size | USD 6,222                                                  |
| Regulatory status      | FCA authorised (UK), SEC registered (US)                   |

### Fee Structure

| Fee Type           | Rate                             | Annual Revenue (USD) |
| ------------------ | -------------------------------- | -------------------- |
| Management fee     | 0.79% of AUM                     | 2,212,000            |
| Performance fee    | None                             | 0                    |
| Minimum investment | USD 100                          |                      |
| Fee frequency      | Monthly deduction from portfolio |                      |

### Portfolio Composition

| Asset Class                    | Allocation | Screening Standard         |
| ------------------------------ | ---------- | -------------------------- |
| US equities (Shariah-screened) | 40%        | AAOIFI Std 21 + MSCI       |
| International equities         | 25%        | AAOIFI Std 21 + MSCI       |
| Sukuk (global)                 | 20%        | N/A (inherently compliant) |
| Gold (physical-backed ETF)     | 10%        | N/A                        |
| Cash equivalents               | 5%         | Shariah-compliant deposits |

### Purification Data

| Parameter                         | Value                                                                    |
| --------------------------------- | ------------------------------------------------------------------------ |
| Quarterly portfolio dividends     | USD 1,400,000                                                            |
| Weighted non-Shariah income ratio | 2.1%                                                                     |
| Purification obligation           | USD 29,400                                                               |
| Purification responsibility       | Platform calculates and deducts; donates to charity on behalf of clients |

### IFRS 15 Performance Obligations

| Obligation           | Nature        | Satisfaction                       |
| -------------------- | ------------- | ---------------------------------- |
| Portfolio management | Over time     | Monthly as services rendered       |
| Shariah screening    | Over time     | Integrated with management         |
| Purification service | Point in time | Quarterly calculation and donation |
| Reporting            | Over time     | Monthly statements                 |

---

## Scenario 3: P2P Islamic Lending — Qardus (UK)

### Entity Profile

| Parameter         | Value                                                         |
| ----------------- | ------------------------------------------------------------- |
| Entity            | Qardus Ltd (UK P2P platform)                                  |
| Product           | Shariah-compliant P2P financing for Muslim SMEs               |
| Structure         | Murabaha — platform matches savers with SME borrowers         |
| Regulatory status | FCA authorised as P2P lending platform                        |
| Framework         | IFRS 9 (for each saver's receivable), IFRS 15 (platform fees) |

### Portfolio Data

| Parameter                         | Value            |
| --------------------------------- | ---------------- |
| Total facilities outstanding      | GBP 18,000,000   |
| Number of active facilities       | 240              |
| Average facility size             | GBP 75,000       |
| Number of active savers/investors | 3,200            |
| Average saver commitment          | GBP 5,625        |
| Platform fee (from borrower)      | 3.0% of facility |
| Saver return (murabaha profit)    | 8.5% p.a.        |
| Default rate (12-month)           | 4.2%             |

### Structural Questions

| Question                   | Considerations                                                         |
| -------------------------- | ---------------------------------------------------------------------- |
| Who is the IFI?            | Platform? Each individual saver? The SPV?                              |
| FCA authorisation category | P2P lending platform (not bank) — but murabaha requires asset purchase |
| Saver's IFRS 9 treatment   | Amortised cost for each saver's murabaha receivable?                   |
| Shariah governance         | Full SSB? Single scholar? Fatwa from established institution?          |

---

## Scenario 4: Climate Sukuk — Solar Rooftop (UAE)

### Entity Profile

| Parameter         | Value                                                              |
| ----------------- | ------------------------------------------------------------------ |
| Entity            | SolarSukuk ADGM Ltd (Abu Dhabi Global Market)                      |
| Product           | Retail impact sukuk funding solar rooftop installations            |
| Structure         | Ijarah — investors own solar panels, lease to homeowners           |
| Regulatory status | ADGM Financial Services Permission                                 |
| Framework         | IFRS 9 (investor), IFRS 16 (lease), IFRS 15 (installation revenue) |

### Sukuk Structure Data

| Parameter                        | Value                                 |
| -------------------------------- | ------------------------------------- |
| Total issuance                   | AED 50,000,000                        |
| Number of retail investors       | 2,500                                 |
| Minimum investment               | AED 1,000                             |
| Average investment               | AED 20,000                            |
| Underlying assets                | 500 residential solar rooftop systems |
| Cost per system                  | AED 100,000                           |
| Monthly lease rental per system  | AED 1,200                             |
| Total monthly rental income      | AED 600,000                           |
| Annual distribution to investors | ~14.4% of AED 50M = AED 7,200,000     |
| Distribution frequency           | Quarterly                             |
| Quarterly distribution           | AED 1,800,000                         |
| Sukuk tenor                      | 10 years                              |
| Estimated system useful life     | 25 years                              |

### SPV Accounting

| Item                                  | Amount (AED)                               |
| ------------------------------------- | ------------------------------------------ |
| Solar assets (cost)                   | 50,000,000                                 |
| Annual depreciation (25-year life)    | 2,000,000                                  |
| Annual rental income                  | 7,200,000                                  |
| Annual operating expenses             | 800,000                                    |
| Annual net income before distribution | 4,400,000                                  |
| Annual investor distribution          | 7,200,000                                  |
| Shortfall funded from                 | Asset value appreciation / sponsor support |

### Classification Question

| Option                | Ijarah Sukuk                        | Musharaka Sukuk              |
| --------------------- | ----------------------------------- | ---------------------------- |
| Investor owns         | Solar panels (specific assets)      | Share in the project         |
| Return from           | Lease rental (fixed)                | Profit share (variable)      |
| Risk profile          | Asset risk + lessee credit risk     | Full business risk           |
| IFRS 9 classification | Likely amortised cost (fixed flows) | Likely FVPL (variable flows) |

---

## Your Task

1. **Digital murabaha (HelloGold)**: Determine if valid murabaha or tawarruq. Classify the fintech receivable under MFRS 9. Show revenue split between platform (wakala fee) and bank (murabaha income). Identify BNM/SC licensing requirements
2. **Robo-adviser (Wahed)**: Analyse management fees under IFRS 15. Determine purification responsibility (platform vs. client). Classify under UK FCA (collective investment scheme, adviser, or portfolio manager?)
3. **P2P Islamic lending (Qardus)**: Determine who is the IFI. Assess FCA authorisation requirements. Show each saver's IFRS 9 accounting. Recommend Shariah governance structure
4. **Climate sukuk (SolarSukuk)**: Classify as ijarah or musharaka. Show retail investor IFRS 9 accounting. Identify ADGM regulatory framework. Draft SPV accounting policy

---

## Expected Output

- HelloGold: murabaha validity assessment, MFRS 9 classification, revenue recognition split, licensing note
- Wahed: IFRS 15 performance obligation analysis, purification journal entries, FCA classification
- Qardus: "Who is the IFI?" analysis, FCA authorisation assessment, saver IFRS 9 entries, governance recommendation
- SolarSukuk: ijarah vs. musharaka classification, investor entries, ADGM framework note, SPV accounting policy
- Key insight: Islamic fintech compresses centuries of jurisprudence into app UX — and raises accounting questions that standard-setters have not yet resolved
