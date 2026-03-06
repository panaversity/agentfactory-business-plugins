# Exercise 5: ICAAP Stress Test

## Scenario Profile

| Field               | Value                                                    |
| ------------------- | -------------------------------------------------------- |
| **Domain**          | Stress Testing / Capital Planning                        |
| **Jurisdiction**    | United Kingdom (BoE ACS)                                 |
| **Time Estimate**   | 50 minutes                                               |
| **Skills Required** | `stress-testing`, `basel-capital`, `ifrs9-ecl`, `uk-pra` |

---

## Starting Position

| Metric                             | Value       |
| ---------------------------------- | ----------- |
| CET1 Capital                       | GBP 3,200M  |
| Total RWA                          | GBP 25,000M |
| Starting CET1 Ratio                | 12.8%       |
| Loan Book                          | GBP 18,500M |
| Net Interest Income (annual, base) | GBP 1,800M  |
| Operating Costs (annual)           | GBP 1,100M  |
| Dividends (annual)                 | GBP 350M    |
| Corporate Tax Rate                 | 25%         |

## BoE Severe Scenario

| Variable         | Year 1 | Year 2 | Year 3 |
| ---------------- | ------ | ------ | ------ |
| UK GDP Growth    | -4.0%  | -1.5%  | +1.0%  |
| UK Unemployment  | 7.5%   | 9.0%   | 8.0%   |
| UK HPI Change    | -25%   | -10%   | +2%    |
| Base Rate        | 0.5%   | 0.25%  | 0.25%  |
| CRE Value Change | -35%   | -15%   | +5%    |

## Stress Assumptions

| Parameter                        | Year 1    | Year 2    | Year 3      |
| -------------------------------- | --------- | --------- | ----------- |
| NII Reduction (vs. base)         | -10%      | -15%      | -8%         |
| Credit Losses (% of loan book)   | 1.8%      | 2.5%      | 1.2%        |
| RWA Inflation (credit migration) | +8%       | +12%      | +5%         |
| Market RWA Increase              | +30%      | +20%      | +10%        |
| Dividends                        | Suspended | Suspended | Reduced 50% |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The starting position, BoE severe scenario, and stress assumptions tables above
- Skills active: `stress-testing`, `basel-capital`, `ifrs9-ecl`, `uk-pra`
- Estimated time: 50 minutes

---

## Step-by-Step Instructions

### Step 1: Capital Depletion Path (20 min)

For each of the 3 stress years, calculate:

1. Opening CET1 capital
2. - Pre-tax profit: (NII - Operating Costs - Credit Losses)
3. - Tax (if profitable; tax credit if loss, subject to deferred tax asset limits)
4. - Dividends (suspended Y1-Y2, halved Y3)
5. = Closing CET1 capital

### Step 2: Stressed RWA (10 min)

For each year:

1. Opening RWA
2. - Credit RWA inflation (from migration to higher risk weight buckets)
3. - Market RWA increase
4. = Closing stressed RWA

### Step 3: Stressed Capital Ratios (5 min)

Calculate for each year-end:

- Stressed CET1 Ratio = Closing CET1 / Closing RWA
- Distance to 4.5% hard minimum
- Distance to combined buffer requirement (9.0% for UK)
- Identify the year of maximum capital depletion (trough)

### Step 4: MDA and Buffer Breach Assessment (5 min)

At the trough CET1 ratio:

- Is the bank above the combined buffer requirement?
- If not, what MDA restrictions apply?
- What management actions could restore the ratio?

### Step 5: Reverse Stress Test (10 min)

Work backwards: What credit loss rate would cause CET1 to breach 4.5%?

- Start from Year 2 (worst point)
- Solve for the credit loss percentage that drives CET1 ratio to exactly 4.5%
- Assess the plausibility of that scenario

---

## Deliverable

Produce: ICAAP capital depletion path over a 3-year horizon showing opening/closing CET1 by year, stressed RWA trajectory, stressed capital ratios with distance to minimum, and reverse stress test breakpoint analysis.

---

## Key Learning

- Credit losses dominate capital depletion in severe stress scenarios
- RWA inflation compounds the problem: even without additional losses, migration increases the denominator
- Dividend suspension is the first management action and preserves meaningful capital
- The reverse stress test identifies the bank's breaking point and guides management monitoring
- The UK BoE ACS scenario is the benchmark severe scenario for ICAAP submissions
