# Exercise 4: LCR and NSFR Calculation

## Scenario Profile

| Field               | Value                                                 |
| ------------------- | ----------------------------------------------------- |
| **Domain**          | Basel III Liquidity                                   |
| **Jurisdiction**    | EU / UK                                               |
| **Time Estimate**   | 40 minutes                                            |
| **Skills Required** | `liquidity-lcr`, `liquidity-nsfr`, `uk-pra`, `eu-crr` |

---

## HQLA Data

| Asset                                      | Amount GBP M | HQLA Level | Haircut |
| ------------------------------------------ | ------------ | ---------- | ------- |
| Central bank reserves                      | 420          | Level 1    | 0%      |
| UK Government bonds (Gilts)                | 380          | Level 1    | 0%      |
| Covered bonds (rated AA)                   | 95           | Level 2A   | 15%     |
| Investment-grade corporate bonds (rated A) | 60           | Level 2B   | 50%     |

## Cash Outflows (30-day stress)

| Category                                        | Balance GBP M | Run-off Rate |
| ----------------------------------------------- | ------------- | ------------ |
| Retail stable deposits (insured)                | 2,800         | 3%           |
| Retail less stable deposits                     | 1,200         | 10%          |
| Non-financial corporate (operational)           | 600           | 25%          |
| Non-financial corporate (non-operational)       | 400           | 40%          |
| Financial institution (non-operational)         | 250           | 100%         |
| Undrawn committed credit facilities (corporate) | 500           | 10%          |
| Undrawn committed credit facilities (financial) | 200           | 40%          |

## Cash Inflows (30-day)

| Category                                   | Amount GBP M | Inflow Rate |
| ------------------------------------------ | ------------ | ----------- |
| Retail loan repayments due                 | 180          | 50%         |
| Non-financial corporate repayments due     | 120          | 100%        |
| Financial institution repayments due       | 80           | 100%        |
| Maturing secured lending (HQLA collateral) | 150          | 0%          |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The HQLA data, cash outflow, and cash inflow tables above
- Skills active: `liquidity-lcr`, `liquidity-nsfr`, `uk-pra`, `eu-crr`
- Estimated time: 40 minutes

---

## Step-by-Step Instructions

### Step 1: HQLA Stock Calculation (10 min)

1. Apply haircuts to each HQLA category
2. Check Level 2A cap (40% of total HQLA after haircuts)
3. Check Level 2B cap (15% of total HQLA after haircuts)
4. Check combined Level 2 cap (40% of total HQLA)
5. Calculate adjusted HQLA stock

### Step 2: Net Cash Outflow Calculation (10 min)

1. Calculate total outflows: Balance x Run-off Rate for each category
2. Calculate total inflows: Amount x Inflow Rate for each category
3. Apply the 75% inflow cap: Net Outflows = Total Outflows - MIN(Total Inflows, 75% x Total Outflows)

### Step 3: LCR Ratio (5 min)

LCR = HQLA Stock / Net Cash Outflows
Assess against 100% minimum and 110-130% management target range.

### Step 4: NSFR Calculation (10 min)

Using the same balance sheet data, calculate:

1. Available Stable Funding (ASF) using ASF factor table
2. Required Stable Funding (RSF) using RSF factor table
3. NSFR = ASF / RSF
   Assess against 100% minimum.

### Step 5: Discussion Questions (5 min)

1. Why is the 75% inflow cap critical? What happens if a bank assumes 100% inflow?
2. What actions could the bank take to improve LCR if it were below 100%?
3. How does the LCR interact with the NSFR? Can a bank pass one and fail the other?

---

## Deliverable

Produce: LCR/NSFR calculation workbook with HQLA stock (after haircuts and caps), net cash outflow schedule, LCR and NSFR ratios, and a stress scenario comparison against management targets.

---

## Key Learning

- HQLA haircuts and caps significantly reduce the buffer value of lower-quality assets
- The 75% inflow cap is a major constraint -- banks cannot assume all counterparties pay on time in stress
- LCR (30-day) and NSFR (1-year) address different risk horizons; both are required simultaneously
- Retail stable deposits are the cheapest liquidity source (3% run-off vs 100% for financial wholesale)
