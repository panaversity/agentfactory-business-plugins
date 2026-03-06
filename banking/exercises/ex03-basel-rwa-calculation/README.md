# Exercise 3: Basel III Capital Ratio -- Standardised Approach

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Domain**          | Basel III Capital Adequacy -- SA              |
| **Jurisdiction**    | United Kingdom (PRA)                          |
| **Time Estimate**   | 45 minutes                                    |
| **Skills Required** | `basel-capital`, `basel-rwa-credit`, `uk-pra` |

---

## Asset Data

You are a capital management analyst at a mid-size UK bank. Calculate the CET1, Tier 1, and Total Capital ratios under the Standardised Approach.

### On-Balance-Sheet Assets

| Asset                                     | Balance GBP M | Risk Weight | Notes                               |
| ----------------------------------------- | ------------- | ----------- | ----------------------------------- |
| UK Gilts                                  | 850           | 0%          | Domestic sovereign, GBP-denominated |
| BoE Reserves                              | 420           | 0%          | Central bank reserves               |
| Claims on Barclays                        | 180           | 20%         | UK bank, AA- rated, short-term      |
| UK Residential Mortgages (LTV <= 50%)     | 1,200         | 20%         | Basel IV LTV-based                  |
| UK Residential Mortgages (LTV 50-80%)     | 2,400         | 30%         | Basel IV LTV-based                  |
| UK Residential Mortgages (LTV 80-90%)     | 600           | 40%         | Basel IV LTV-based                  |
| Corporate Loans (rated BBB+ to BB-)       | 900           | 75%         | Basel IV revised corporate RW       |
| Corporate Loans (unrated)                 | 450           | 100%        | Unrated corporate                   |
| SME Loans (qualifying)                    | 350           | 75%         | SME supporting factor applies       |
| Commercial Real Estate (income-producing) | 280           | 75%         | CRE under Basel IV                  |
| Consumer Loans                            | 500           | 75%         | Qualifying retail                   |
| Past Due (>90 days, provision < 20%)      | 85            | 150%        | Net of specific provisions          |
| Past Due (>90 days, provision >= 20%)     | 45            | 100%        | Net of specific provisions          |
| Fixed Assets                              | 120           | 100%        | PP&E                                |
| Other Assets                              | 200           | 100%        | Miscellaneous                       |

### Off-Balance-Sheet Items

| Item                                   | Notional GBP M | CCF  | Notes                |
| -------------------------------------- | -------------- | ---- | -------------------- |
| Undrawn committed facilities (>1 year) | 600            | 40%  | Corporate revolvers  |
| Undrawn unconditionally cancellable    | 400            | 10%  | Retail credit cards  |
| Direct credit substitutes (guarantees) | 150            | 100% | Financial guarantees |

### Capital Components

| Component               | Amount GBP M |
| ----------------------- | ------------ |
| CET1 Capital            | 285          |
| Additional Tier 1 (AT1) | 45           |
| Tier 2                  | 60           |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The on-balance-sheet asset table, off-balance-sheet items, and capital components above
- Skills active: `basel-capital`, `basel-rwa-credit`, `uk-pra`
- Estimated time: 45 minutes

---

## Step-by-Step Instructions

### Step 1: Credit RWA Calculation (15 min)

For each on-balance-sheet asset line:

- RWA = Balance x Risk Weight
  Calculate total on-balance-sheet credit RWA.

### Step 2: Off-Balance-Sheet RWA (10 min)

For each off-balance-sheet item:

- EAD = Notional x CCF
- RWA = EAD x Risk Weight (use the risk weight of the underlying exposure type)
  Assume: committed facilities are to corporates (75% RW), cancellable to retail (75% RW), guarantees to corporates (100% RW).

### Step 3: Total RWA and Capital Ratios (10 min)

- Total RWA = On-BS Credit RWA + Off-BS Credit RWA
  (Assume Market RWA and Operational RWA are zero for this exercise)
- CET1 Ratio = CET1 / Total RWA
- Tier 1 Ratio = (CET1 + AT1) / Total RWA
- Total Capital Ratio = (CET1 + AT1 + T2) / Total RWA
- Leverage Ratio = Tier 1 / Total Exposure Measure (use total assets for simplification)

### Step 4: Buffer Assessment (5 min)

Calculate the effective CET1 requirement for this UK bank:

- 4.5% minimum + 2.5% CCB + 2.0% UK CCyB (current) = 9.0%
- Compare to calculated CET1 ratio
- Determine MDA headroom: CET1 ratio - 9.0%

### Step 5: Discussion Questions (5 min)

1. How would the RWA change if the bank used IRB for the mortgage portfolio?
2. What is the impact of the Basel IV output floor on an IRB bank with this portfolio?
3. If the UK CCyB were released to 0%, how much CET1 headroom would be freed?

---

## Deliverable

Produce: RWA calculation table (on-BS and off-BS line items), capital ratio dashboard (CET1, Tier 1, Total Capital, Leverage), and MDA headroom assessment.

---

## Key Learning

- Risk weights vary dramatically by asset class (0% for sovereign to 150% for past-due)
- Off-balance-sheet items can contribute materially to RWA through CCF conversion
- The UK CCyB adds significant CET1 requirement above Basel minimums
- MDA restrictions create a practical constraint well above the hard 4.5% minimum
