# Exercise 11: AAOIFI vs. IFRS Full Comparative Financial Statements — Bahrain IFI (Capstone)

## Scenario Profile

| Field               | Value                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Entity**          | ABC Islamic Bank (Bahrain) — hypothetical mid-size IFI                                                     |
| **Domain**          | Islamic Accounting — Full Standards Reconciliation                                                         |
| **Jurisdiction**    | Bahrain (AAOIFI FAS mandatory), with IFRS comparison                                                       |
| **Total Assets**    | USD 8,000,000,000                                                                                          |
| **Target Time**     | 90 minutes (capstone accounting exercise)                                                                  |
| **Skills Required** | `bahrain-aaoifi.md`, `murabaha.md`, `ijarah-imb.md`, `musharaka-dm.md`, `mudaraba.md`, `sukuk-investor.md` |

---

## Product Portfolio Breakdown

| Product                     | % of Financing | Amount (USD millions) | AAOIFI Standard | IFRS Standard    |
| --------------------------- | -------------- | --------------------- | --------------- | ---------------- |
| Murabaha                    | 45%            | 3,600                 | FAS 2           | IFRS 9           |
| Ijarah / IMB                | 30%            | 2,400                 | FAS 32          | IFRS 16 / IFRS 9 |
| Musharaka / Mudaraba        | 20%            | 1,600                 | FAS 3, FAS 4    | IFRS 9           |
| Other (salam, istisna'a)    | 5%             | 400                   | FAS 7, FAS 10   | IFRS 9, IFRS 15  |
| **Total Islamic Financing** | **100%**       | **8,000**             |                 |                  |

---

## Trial Balance Data (USD millions)

### Assets

| Account                        | AAOIFI Label                 | Amount    | IFRS Equivalent Label                    |
| ------------------------------ | ---------------------------- | --------- | ---------------------------------------- |
| Cash and balances with banks   | Cash and balances with banks | 450       | Cash and cash equivalents                |
| Murabaha receivables (gross)   | Murabaha receivables         | 3,780     | Islamic financing receivables            |
| Less: Deferred murabaha income | Deferred murabaha income     | (180)     | N/A (netted in amortised cost)           |
| Less: ECL provision — murabaha | Provision for impairment     | (72)      | ECL allowance                            |
| **Net murabaha receivables**   |                              | **3,528** |                                          |
| Ijarah assets (cost)           | Ijarah assets                | 2,800     | N/A (derecognised if finance lease)      |
| Less: Accumulated depreciation | Accumulated depreciation     | (400)     | N/A                                      |
| **Net ijarah assets**          |                              | **2,400** | **Net investment in lease: 2,400**       |
| Musharaka investments          | Musharaka investments        | 1,200     | Financial assets at FVOCI/amortised cost |
| Mudaraba investments           | Mudaraba investments         | 400       | Financial assets at FVPL/FVOCI           |
| Sukuk investments              | Sukuk investments            | 650       | Investment securities                    |
| Other assets                   | Other assets                 | 372       | Other assets                             |
| **Total Assets**               |                              | **8,000** |                                          |

### Liabilities and Equity

| Account                              | AAOIFI Label                             | Amount    | IFRS Equivalent Label              |
| ------------------------------------ | ---------------------------------------- | --------- | ---------------------------------- |
| Current accounts                     | Current accounts                         | 1,200     | Customer deposits — demand         |
| **Equity of IAH**                    | **Equity of investment account holders** | **5,200** | **Customer deposits — investment** |
| Other liabilities                    | Other liabilities                        | 200       | Other liabilities                  |
| **Total Liabilities + IAH**          |                                          | **6,600** |                                    |
| Share capital                        | Share capital                            | 800       | Share capital                      |
| Reserves                             | Reserves                                 | 350       | Reserves                           |
| Retained earnings                    | Retained earnings                        | 250       | Retained earnings                  |
| **Total Equity**                     |                                          | **1,400** |                                    |
| **Total Liabilities + IAH + Equity** |                                          | **8,000** |                                    |

---

## Income Statement Data (USD millions, annual)

| Line Item                               | AAOIFI Label                         | Amount  | IFRS Label                            |
| --------------------------------------- | ------------------------------------ | ------- | ------------------------------------- |
| Murabaha income                         | Income from murabaha                 | 285     | Income from Islamic financing         |
| Ijarah income                           | Income from ijarah                   | 192     | Income from Islamic financing         |
| Musharaka/Mudaraba income               | Income from musharaka/mudaraba       | 128     | Income from Islamic financing         |
| Other Islamic income                    | Other Islamic income                 | 35      | Other Islamic income                  |
| **Total income from Islamic financing** |                                      | **640** | **Net income from Islamic financing** |
| Less: Return to IAH                     | Return to investment account holders | (312)   | Finance cost on customer deposits     |
| **Net income after IAH distribution**   |                                      | **328** | **Net financing margin**              |
| Fee and commission income               | Fee and commission income            | 45      | Fee and commission income             |
| Operating expenses                      | Operating expenses                   | (185)   | Operating expenses                    |
| ECL provision charge                    | Provision for impairment             | (38)    | ECL expense                           |
| **Net income before zakat**             |                                      | **150** | **Profit before tax**                 |
| Zakat                                   | Zakat expense                        | (8)     | N/A (footnote only or tax)            |
| **Net income**                          |                                      | **142** | **150** (no zakat in IFRS P&L)        |

---

## IAH Fund Data

| Item                                 | Amount (USD millions)   |
| ------------------------------------ | ----------------------- |
| Opening IAH balance                  | 4,900                   |
| New investment accounts              | 1,800                   |
| Withdrawals                          | (1,500)                 |
| Closing IAH balance (before returns) | 5,200                   |
| Return distributed to IAH            | 312                     |
| Mudarib share (bank's fee)           | 78 (20% of gross pool)  |
| Profit pool (total)                  | 390                     |
| Profit distribution ratio            | 80% to IAH, 20% to bank |

---

## AAOIFI Financial Statement Templates

### Statement of Financial Position (AAOIFI)

```
ASSETS
  Cash and balances with banks          ___
  Murabaha receivables (net)            ___
  Ijarah assets (net)                   ___
  Musharaka investments                 ___
  Mudaraba investments                  ___
  Sukuk investments                     ___
  Other assets                          ___
TOTAL ASSETS                            ___

LIABILITIES
  Current accounts                      ___
  Other liabilities                     ___
TOTAL LIABILITIES                       ___

EQUITY OF INVESTMENT ACCOUNT HOLDERS    ___

OWNERS' EQUITY
  Share capital                         ___
  Reserves                              ___
  Retained earnings                     ___
TOTAL OWNERS' EQUITY                    ___

TOTAL LIABILITIES + IAH + EQUITY        ___
```

### Statement of Changes in Equity of IAH (AAOIFI-specific)

| Item                | Amount    |
| ------------------- | --------- |
| Opening balance     | 4,900     |
| New investments     | 1,800     |
| Withdrawals         | (1,500)   |
| Share of profit     | 312       |
| **Closing balance** | **5,512** |

_Note: This statement does NOT exist under IFRS — it is AAOIFI-specific._

---

## Your Task

1. **AAOIFI financial statements**: Complete all four AAOIFI statements (financial position, income, changes in IAH equity, cash flows). Use AAOIFI labels throughout — no "loans," no "interest," no "net interest income"
2. **IFRS reconciliation**: Identify the 5 most material AAOIFI-to-IFRS differences. For each: AAOIFI treatment, IFRS treatment, USD impact on assets/liabilities/equity/net income. Produce a reconciliation table
3. **IFRS financial statements**: Apply reconciling adjustments. Produce IFRS-compliant statements (IAS 1, IFRS 7). The critical change: IAH funds move from separate category to financial liabilities
4. **Key ratio comparison**: Calculate under both frameworks: Net Financing Margin, ROA, ROE, NPF ratio, IAH-to-Total-Assets. Identify which ratios differ by >5% and explain why
5. **External auditor workpaper**: Draft assessment of 5 most significant audit risks arising from the AAOIFI/IFRS framework tension
6. **Master Bahrain-AAOIFI SKILL.md**: Draft the comprehensive jurisdiction overlay covering: mandatory FAS list, balance sheet presentation, income statement labels, IAH treatment, SSB disclosure, CBB Rulebook references, zakat disclosure

---

## Expected Output

- Complete AAOIFI financial statements (4 statements)
- 5-item reconciliation table with USD impacts
- Complete IFRS financial statements (reclassifying IAH as liabilities)
- Ratio comparison table showing ROE divergence (AAOIFI ROE lower due to larger equity base including IAH vs. IFRS ROE higher with IAH as liabilities)
- 5 audit risk assessments with source, rating, procedure, and conclusion
- Deployable Bahrain-AAOIFI SKILL.md
- Key insight: the IAH reclassification alone can swing ROE by several percentage points — an entirely accounting-driven difference, not a performance difference
