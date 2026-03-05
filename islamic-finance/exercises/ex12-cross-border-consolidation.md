# Exercise 12: Cross-Border Islamic Banking Group — Consolidated Reporting Challenge

## Scenario Profile

| Field               | Value                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| **Group**           | Al Baraka Banking Group (simplified to 4 entities)                                               |
| **Parent**          | Bahrain (AAOIFI)                                                                                 |
| **Subsidiaries**    | UAE (IFRS), Malaysia (MFRS), Pakistan (IFRS + SBP overlay)                                       |
| **Target Time**     | 75 minutes                                                                                       |
| **Skills Required** | `gcc-crossborder.md`, `bahrain-aaoifi.md`, `uae-ifrs.md`, `malaysia-mfrs.md`, `pakistan-ifrs.md` |

---

## Group Structure

```
Al Baraka Islamic Bank BSC (Bahrain) — PARENT
├── Al Baraka Islamic Bank UAE LLC — 100% owned (IFRS / CBUAE)
├── Al Baraka Islamic Bank Malaysia Bhd — 100% owned (MFRS / BNM)
└── Al Baraka Islamic Bank Pakistan Ltd — 85% owned (IFRS / SBP)
```

---

## Entity 1: Bahrain Parent (AAOIFI)

### Balance Sheet (USD millions)

| Item                             | AAOIFI Label                             | Amount    |
| -------------------------------- | ---------------------------------------- | --------- |
| Cash                             | Cash and balances with banks             | 320       |
| Murabaha receivables (net)       | Murabaha receivables                     | 2,800     |
| Ijarah assets (net)              | Ijarah assets                            | 1,500     |
| Investment in subsidiaries       | Investment in subsidiaries               | 1,200     |
| Sukuk investments                | Sukuk investments                        | 480       |
| Other assets                     | Other assets                             | 200       |
| **Total Assets**                 |                                          | **6,500** |
| Current accounts                 | Current accounts                         | 650       |
| **Equity of IAH**                | **Equity of investment account holders** | **3,900** |
| Other liabilities                | Other liabilities                        | 150       |
| Intra-group payable (to UAE sub) | Murabaha payable                         | 0         |
| **Total Liabilities + IAH**      |                                          | **4,700** |
| Share capital                    | Share capital                            | 1,000     |
| Reserves                         | Reserves                                 | 500       |
| Retained earnings                | Retained earnings                        | 300       |
| **Total Equity**                 |                                          | **1,800** |

---

## Entity 2: UAE Subsidiary (IFRS)

### Balance Sheet (USD millions)

| Item                                 | IFRS Label                     | Amount    |
| ------------------------------------ | ------------------------------ | --------- |
| Cash                                 | Cash and cash equivalents      | 180       |
| Islamic financing receivables        | Loans and advances (Islamic)   | 1,850     |
| Sukuk investments                    | Investment securities          | 320       |
| Other assets                         | Other assets                   | 150       |
| **Total Assets**                     |                                | **2,500** |
| Customer deposits — demand           | Current accounts               | 280       |
| Customer deposits — investment       | Investment deposits (mudaraba) | 1,600     |
| Intra-group receivable (from parent) | Inter-company receivable       | 200       |
| Other liabilities                    | Other liabilities              | 80        |
| **Total Liabilities**                |                                | **2,160** |
| Share capital                        | Share capital                  | 200       |
| Reserves                             | Reserves                       | 80        |
| Retained earnings                    | Retained earnings              | 60        |
| **Total Equity**                     |                                | **340**   |

---

## Entity 3: Malaysia Subsidiary (MFRS)

### Balance Sheet (MYR millions — translated at USD 1 = MYR 4.5)

| Item                           | MFRS Label                           | MYR       | USD equivalent |
| ------------------------------ | ------------------------------------ | --------- | -------------- |
| Cash                           | Cash and cash equivalents            | 405       | 90             |
| Islamic financing (net)        | Financing and advances               | 5,400     | 1,200          |
| Sukuk investments              | Financial investments                | 900       | 200            |
| Other assets                   | Other assets                         | 225       | 50             |
| **Total Assets**               |                                      | **6,930** | **1,540**      |
| Customer deposits — demand     | Deposits from customers (demand)     | 675       | 150            |
| Customer deposits — investment | Deposits from customers (investment) | 4,500     | 1,000          |
| Other liabilities              | Other liabilities                    | 225       | 50             |
| **Total Liabilities**          |                                      | **5,400** | **1,200**      |
| Share capital                  | Share capital                        | 900       | 200            |
| Reserves                       | Reserves                             | 360       | 80             |
| Retained earnings              | Retained earnings                    | 270       | 60             |
| **Total Equity**               |                                      | **1,530** | **340**        |

---

## Entity 4: Pakistan Subsidiary (IFRS + SBP)

### Balance Sheet (PKR millions — translated at USD 1 = PKR 280)

| Item                           | Label                         | PKR         | USD equivalent |
| ------------------------------ | ----------------------------- | ----------- | -------------- |
| Cash                           | Cash and balances             | 22,400      | 80             |
| Islamic financing (net)        | Advances — Islamic financing  | 168,000     | 600            |
| Sukuk investments              | Investments                   | 42,000      | 150            |
| Other assets                   | Other assets                  | 16,800      | 60             |
| **Total Assets**               |                               | **249,200** | **890**        |
| Customer deposits — demand     | Deposits — current            | 33,600      | 120            |
| Customer deposits — investment | Deposits — investment/savings | 154,000     | 550            |
| Other liabilities              | Other liabilities             | 14,000      | 50             |
| **Total Liabilities**          |                               | **201,600** | **720**        |
| Share capital                  | Share capital                 | 28,000      | 100            |
| Reserves                       | Reserves                      | 11,200      | 40             |
| Retained earnings              | Retained earnings             | 8,400       | 30             |
| **Total Equity**               |                               | **47,600**  | **170**        |
| **NCI (15%)**                  |                               |             | **25.5**       |

---

## Intra-Group Murabaha Data

| Parameter                   | Value                                                    |
| --------------------------- | -------------------------------------------------------- |
| Facility                    | Bahrain parent provides $200M murabaha to UAE subsidiary |
| Purpose                     | Fund subsidiary's Islamic financing operations           |
| Structure                   | Commodity murabaha via London Metal Exchange             |
| Mark-up rate                | 5.8% p.a.                                                |
| Tenor                       | 1 year, renewable                                        |
| Parent's books (AAOIFI)     | Murabaha receivable $200M                                |
| Subsidiary's books (IFRS)   | Inter-company payable $200M                              |
| Annual income (parent)      | $11.6M                                                   |
| Annual expense (subsidiary) | $11.6M                                                   |

### Transfer Pricing: Mudarib Fee

| Parameter                                  | Value                                               |
| ------------------------------------------ | --------------------------------------------------- |
| Pakistan subsidiary pays to Bahrain parent | $3.2M annual mudarib management fee                 |
| Fee basis                                  | 1.5% of assets under management                     |
| Pakistan FBR transfer pricing concern      | Must be arm's length                                |
| Shariah concern                            | Can one group entity charge mudarib fee to another? |

---

## Your Task

1. **Identify consolidation adjustments**: List the top 5 accounting policy differences when consolidating AAOIFI parent with IFRS subsidiaries. For each: parent treatment, subsidiary treatment, required adjustment, and whether group should consolidate under AAOIFI or IFRS
2. **IAH funds in consolidation**: The parent presents IAH as separate category; subsidiaries present investment deposits as liabilities. Which treatment for the group? Generate the reclassification adjustment entry
3. **Intra-group murabaha elimination**: Is the $200M facility a genuine murabaha or intra-group funding? Should it be eliminated on consolidation? Generate elimination entries. Address the Shariah question of intra-group murabaha
4. **Transfer pricing and Shariah**: Analyse the mudarib fee — arm's length for Pakistan FBR? Shariah-compliant between group entities? Documentation requirements
5. **Group consolidated financial statements**: Produce consolidated statement of financial position and income statement under IFRS (primary framework), with supplementary AAOIFI disclosures for Bahrain regulatory compliance. Draft the accounting policy note explaining the dual-framework approach

---

## Expected Output

- 5-item consolidation adjustment register
- IAH reclassification journal (move $3,900M parent IAH + $1,600M UAE + $1,000M Malaysia + $550M Pakistan investment deposits to single "Customer deposits — investment" line under IFRS)
- Intra-group elimination entries ($200M murabaha receivable/payable + $11.6M income/expense)
- NCI calculation for Pakistan (15% of $170M equity = $25.5M)
- Consolidated balance sheet and income statement (IFRS primary)
- Supplementary AAOIFI disclosure note
- Transfer pricing documentation guidance for Pakistan mudarib fee
