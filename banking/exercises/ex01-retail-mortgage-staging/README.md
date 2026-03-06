# Exercise 1: IFRS 9 Stage Assessment -- Retail Mortgage Portfolio

## Scenario Profile

| Field               | Value                                     |
| ------------------- | ----------------------------------------- |
| **Domain**          | IFRS 9 ECL -- Staging and ECL Calculation |
| **Jurisdiction**    | United Kingdom (PRA)                      |
| **Time Estimate**   | 35 minutes                                |
| **Skills Required** | `ifrs9-ecl`, `ifrs9-staging`, `uk-pra`    |

---

## Portfolio Data

You are the IFRS 9 model analyst at a UK retail bank. Below is a sample of 8 mortgage facilities from the retail mortgage book. Assess each facility's IFRS 9 stage and calculate the ECL.

| Facility | Balance GBP | DPD | Rating Now | Rating at Origin | LTV % | Notes                                    |
| -------- | ----------- | --- | ---------- | ---------------- | ----- | ---------------------------------------- |
| A001     | 180,000     | 0   | BB+        | BB+              | 65    | Performing, no issues                    |
| A002     | 245,000     | 15  | BB         | BB+              | 78    | 1-notch downgrade                        |
| A003     | 310,000     | 35  | B+         | BB               | 82    | 2-notch downgrade, 30+ DPD               |
| A004     | 195,000     | 0   | BB+        | BB+              | 55    | Performing, low LTV                      |
| A005     | 420,000     | 95  | CCC        | BB-              | 92    | 90+ DPD, high LTV                        |
| A006     | 275,000     | 45  | B          | BB+              | 88    | On watchlist, 3-notch downgrade          |
| A007     | 160,000     | 0   | BB-        | BB               | 60    | 1-notch downgrade, covenant breach noted |
| A008     | 350,000     | 0   | BB+        | A-               | 71    | 4-notch downgrade but performing         |

## ECL Parameters

| Parameter             | Value |
| --------------------- | ----- |
| Stage 1 PD (12-month) | 0.8%  |
| Stage 2 Lifetime PD   | 12.0% |
| Stage 3 Lifetime PD   | 55.0% |
| LGD (LTV <= 80%)      | 25%   |
| LGD (LTV > 80%)       | 40%   |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The 8-facility mortgage portfolio data table above
- Skills active: `ifrs9-ecl`, `ifrs9-staging`, `uk-pra`
- Estimated time: 35 minutes

---

## Step-by-Step Instructions

### Step 1: Stage Assessment (15 min)

For each of the 8 facilities, apply the staging decision tree from `ifrs9-staging`:

1. Test for Stage 3 first (90+ DPD, formal default, significant financial difficulty)
2. Test for Stage 2 (30-89 DPD rebuttable presumption, 2+ notch downgrade, watchlist, covenant breach)
3. Default to Stage 1 if no triggers

Document the trigger reason for each staging decision.

### Step 2: ECL Calculation (10 min)

For each facility, calculate ECL using the appropriate formula:

- Stage 1: ECL = PD_12 x LGD x EAD
- Stage 2: ECL = Lifetime_PD x LGD x EAD
- Stage 3: ECL = Lifetime_PD x LGD x EAD

Select LGD based on the LTV threshold (25% for LTV <= 80%, 40% for LTV > 80%).

### Step 3: Portfolio Summary Table (5 min)

Build a summary table showing:

- Stage distribution by count and balance
- Total ECL by stage
- ECL coverage ratio by stage

### Step 4: Discussion Questions (5 min)

1. Facility A003 is 35 DPD. Can the 30-day rebuttable presumption be rebutted? Under what conditions?
2. Facility A008 has a 4-notch downgrade but is current on payments. Why is this still Stage 2?
3. What would change if the bank used PIT PD instead of TTC PD for the ECL calculation?

---

## Deliverable

Produce: Stage migration table showing each facility's stage assignment with trigger reason, ECL by facility, and a portfolio summary with ECL coverage ratios by stage.

---

## Key Learning

- The staging decision tree must be applied in the correct order: Stage 3 first, then Stage 2, then default to Stage 1
- DPD alone does not determine stage -- qualitative factors (watchlist, covenant breach, rating downgrade) also trigger SICR
- LGD varies materially with LTV, making collateral monitoring critical for mortgage portfolios
- Stage 2 dramatically increases ECL (from 12-month to lifetime PD) even before a facility is in default
