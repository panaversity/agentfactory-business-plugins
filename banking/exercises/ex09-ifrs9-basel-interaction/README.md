# Exercise 9: IFRS 9 x Basel Interaction

## Scenario Profile

| Field               | Value                                                      |
| ------------------- | ---------------------------------------------------------- |
| **Domain**          | IFRS 9 ECL / Basel Capital Interaction                     |
| **Jurisdiction**    | United Kingdom (PRA)                                       |
| **Time Estimate**   | 50 minutes                                                 |
| **Skills Required** | `ifrs9-ecl`, `basel-capital`, `ifrs9-disclosure`, `uk-pra` |

---

## Starting Data

You are the Head of Capital Management at a UK IRB bank. The following data shows the interaction between IFRS 9 provisions and Basel capital.

### ECL by Stage

| Stage     | Gross Exposure GBP M | ECL Provision GBP M | Coverage % |
| --------- | -------------------- | ------------------- | ---------- |
| Stage 1   | 8,500                | 12.5                | 0.15%      |
| Stage 2   | 2,200                | 38.2                | 1.74%      |
| Stage 3   | 450                  | 24.8                | 5.51%      |
| **Total** | **11,150**           | **75.5**            | **0.68%**  |

### IRB Expected Loss

| Component                         | Amount GBP M |
| --------------------------------- | ------------ |
| IRB Regulatory Expected Loss (EL) | 42.0         |

### Capital Position (Pre-Adjustment)

| Component                               | Amount GBP M |
| --------------------------------------- | ------------ |
| CET1 Capital (before ECL/EL adjustment) | 1,850        |
| AT1                                     | 280          |
| Tier 2                                  | 190          |
| Credit RWA (IRB)                        | 12,500       |
| Total RWA                               | 15,800       |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The ECL by stage, IRB expected loss, and capital position tables above
- Skills active: `ifrs9-ecl`, `basel-capital`, `ifrs9-disclosure`, `uk-pra`
- Estimated time: 50 minutes

---

## Step-by-Step Instructions

### Step 1: IRB Shortfall / Excess Calculation (10 min)

1. Compare IFRS 9 ECL provision (GBP 75.5M) to IRB Regulatory EL (GBP 42.0M)
2. Determine if there is a shortfall or excess:
   - If ECL > EL: Excess provisions (positive for capital)
   - If ECL < EL: Shortfall (deducted from CET1)
3. Calculate the IRB excess/shortfall amount

### Step 2: Capital Impact (10 min)

1. If excess: Add to Tier 2 capital, capped at 0.6% of credit RWA
   - Calculate 0.6% cap: 0.6% x GBP 12,500M = GBP 75M
   - Determine how much of the excess can be added to T2
2. If shortfall: Deduct from CET1 capital
3. Calculate adjusted CET1, T1, and Total Capital

### Step 3: Adjusted Capital Ratios (10 min)

Calculate:

- Adjusted CET1 Ratio
- Adjusted Tier 1 Ratio
- Adjusted Total Capital Ratio
- Compare to pre-adjustment ratios
- Quantify the capital impact in basis points

### Step 4: Output Floor Check (10 min)

If this bank's IRB credit RWA is GBP 12,500M, calculate:

1. SA credit RWA for the same portfolio (use simplified SA risk weights)
2. 72.5% output floor: 72.5% x SA RWA
3. Is the output floor binding? (Is 72.5% x SA RWA > IRB RWA?)
4. If binding, what is the adjusted Total RWA?
5. Recalculate capital ratios with output floor applied

### Step 5: Disclosure Draft (10 min)

Draft the IFRS 7 sensitivity analysis paragraph:

- "If the severe macroeconomic scenario were applied with 100% weighting..."
- Calculate ECL impact under 100% severe weighting (assume severe ECL = 2.5x base ECL)
- Express as GBP impact and basis point impact on CET1 ratio

---

## Deliverable

Produce: Integrated capital management report showing IRB shortfall/excess calculation, adjusted capital ratios (pre- and post-adjustment), output floor impact analysis, and IFRS 7 sensitivity disclosure paragraph.

---

## Key Learning

- IFRS 9 provisions and Basel IRB expected loss are different measures calculated differently
- When IFRS 9 ECL exceeds IRB EL, the excess can boost Tier 2 (capped at 0.6% of credit RWA)
- When IRB EL exceeds IFRS 9 ECL, the shortfall is deducted from CET1 -- this is a direct capital hit
- The Basel IV output floor (72.5%) may override IRB RWA benefits for low-risk portfolios
- Banks must disclose the sensitivity of ECL to scenario changes -- this is one of the most scrutinised IFRS 7 disclosures
