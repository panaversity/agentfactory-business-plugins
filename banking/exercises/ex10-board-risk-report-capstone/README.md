# Exercise 10: Capstone -- Board Risk Report

## Scenario Profile

| Field               | Value                                   |
| ------------------- | --------------------------------------- |
| **Domain**          | Integrated Risk Reporting (all domains) |
| **Jurisdiction**    | United Kingdom (PRA)                    |
| **Time Estimate**   | 75 minutes                              |
| **Skills Required** | All banking skills + `uk-pra`           |

---

## Bank Data

You are the Chief Risk Officer preparing the quarterly Board Risk Report. Compile a comprehensive risk dashboard from the following data.

### Credit Risk

| Metric              | Current Quarter | Prior Quarter | Change |
| ------------------- | --------------- | ------------- | ------ |
| Total Loan Book     | GBP 4,200M      | GBP 4,050M    | +3.7%  |
| Total ECL Provision | GBP 124M        | GBP 118M      | +5.1%  |
| ECL Coverage Ratio  | 2.95%           | 2.91%         | +4bp   |
| Stage 1 Balance     | GBP 3,400M      | GBP 3,350M    | --     |
| Stage 2 Balance     | GBP 620M        | GBP 550M      | +12.7% |
| Stage 3 Balance     | GBP 180M        | GBP 150M      | +20.0% |

### Capital

| Metric                       | Current | Prior | Regulatory Min      |
| ---------------------------- | ------- | ----- | ------------------- |
| CET1 Ratio                   | 11.2%   | 11.8% | 9.0% (incl buffers) |
| Tier 1 Ratio                 | 13.5%   | 14.0% | 10.5%               |
| Total Capital Ratio          | 15.8%   | 16.2% | 13.0%               |
| Leverage Ratio               | 4.8%    | 5.0%  | 3.25%               |
| CET1 Ratio (Stressed Trough) | 10.8%   | 11.2% | 4.5%                |

### Liquidity

| Metric                   | Current | Prior    | Regulatory Min |
| ------------------------ | ------- | -------- | -------------- |
| LCR                      | 142%    | 148%     | 100%           |
| NSFR                     | 108%    | 110%     | 100%           |
| Survival Days (stressed) | 95 days | 105 days | 30 days        |

### AML / Financial Crime

| Metric                      | Current Quarter | Prior Quarter |
| --------------------------- | --------------- | ------------- |
| TM Alerts Generated         | 847             | 792           |
| Alerts Closed (Level 1)     | 612             | 598           |
| Alerts Escalated (Level 2+) | 235             | 194           |
| SARs Filed                  | 28              | 22            |
| Sanctions Hits (true)       | 2               | 1             |
| Sanctions False Positives   | 1,247           | 1,189         |
| Overdue KYC Reviews         | 34              | 18            |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The credit risk, capital, liquidity, and AML/financial crime data tables above
- Skills active: all banking skills + `uk-pra`
- Estimated time: 75 minutes

---

## Step-by-Step Instructions

### Step 1: Credit Risk Section (15 min)

1. Draft the credit risk narrative for the Board
2. Highlight the Stage 2 and Stage 3 increases -- what is driving them?
3. Build the ECL provision movement table (opening to closing)
4. Identify the top 3 portfolio concentrations requiring attention

### Step 2: Capital Section (15 min)

1. Explain the 60bp CET1 decline (11.8% to 11.2%)
2. Calculate MDA headroom: CET1 - combined buffer = 11.2% - 9.0% = 220bp
3. Present the stress test trough and distance to hard minimum
4. Flag any capital actions needed (AT1 issuance, RWA reduction, dividend review)

### Step 3: Liquidity Section (10 min)

1. Report LCR and NSFR with trends
2. Explain the LCR decline (148% to 142%)
3. Assess whether management targets (110-130% LCR) are still met
4. Identify any funding concentration risks

### Step 4: Financial Crime Section (10 min)

1. Report AML alert volumes and escalation trends
2. Highlight the increase in SARs filed (+27%) -- is this better detection or more suspicious activity?
3. Flag the overdue KYC reviews (34 overdue, nearly doubled)
4. Report sanctions screening effectiveness (true hit rate vs false positive volume)

### Step 5: Integrated Risk Dashboard (15 min)

1. Compile a single-page RAG (Red/Amber/Green) dashboard with all metrics
2. Identify the top 3 risks for Board attention
3. Recommend specific actions for each risk
4. Draft the CRO summary paragraph for the Board pack cover page

### Step 6: Discussion (10 min)

1. If the PRA were to increase the UK CCyB by 50bp, what would the impact be?
2. If Stage 2 continues to grow at this rate, project the ECL impact for next quarter
3. What early warning indicators would you monitor between now and next quarter?

---

## Deliverable

Produce: 10-slide Board Risk Report structure (PowerPoint format) with credit risk narrative, capital adequacy section, liquidity dashboard, financial crime summary, single-page RAG dashboard, top 3 risks with recommended actions, and CRO summary paragraph.

---

## Key Learning

- Board risk reports must integrate credit, capital, liquidity, and financial crime into a coherent narrative
- Trends matter more than point-in-time values -- the Board needs to understand direction of travel
- MDA headroom is the most operationally relevant capital metric (not just the CET1 ratio)
- AML metrics require qualitative interpretation -- more SARs may be good (better detection) or bad (more suspicious activity)
- The CRO must translate technical risk metrics into decision-relevant language for non-executive directors
