# Workflow Recipe: Daily LCR Monitor

## Task Overview

| Field         | Value                                                              |
| ------------- | ------------------------------------------------------------------ |
| **Task Name** | Daily Liquidity Coverage Ratio Monitor                             |
| **Frequency** | Daily (every business day by 09:30)                                |
| **Purpose**   | Calculate LCR, monitor HQLA adequacy, flag breaches, report to PRA |
| **Owner**     | Treasury / Liquidity Management                                    |

---

## Trigger Conditions

| Trigger          | Condition                                        | Action                  |
| ---------------- | ------------------------------------------------ | ----------------------- |
| **Scheduled**    | Every business day at 08:00                      | Run LCR calculation     |
| **Event-driven** | Large deposit outflow (> 5% of total deposits)   | Immediate recalculation |
| **Event-driven** | HQLA encumbrance event (repo, collateral pledge) | Update HQLA stock       |
| **Event-driven** | Central bank reserve drawdown                    | Update Level 1 HQLA     |

---

## Step-by-Step Execution

### Step 1: Update HQLA Stock

- Level 1: Central bank reserves + unencumbered sovereign bonds
- Level 2A: Qualifying corporate bonds (AA-) + covered bonds (AA) after 15% haircut
- Level 2B: Qualifying RMBS (25% haircut) + corporate bonds A-BBB- (50% haircut)
- Apply Level 2 caps (40% combined, 15% Level 2B)

### Step 2: Calculate Net Cash Outflows

- Retail outflows: stable deposits x 3% + less stable x 10%
- Wholesale outflows: operational x 25% + non-operational x 40% + financial x 100%
- Off-balance-sheet: committed facilities x drawdown rate
- Inflows: capped at 75% of total outflows

### Step 3: Calculate LCR

LCR = HQLA Stock / Net Cash Outflows
Compare to: 100% regulatory minimum, 110-130% management target

### Step 4: Generate Report

Output: Daily Liquidity Dashboard with:

- LCR ratio and HQLA composition
- Top 10 deposit concentration risks
- Projected LCR for next 7 days (given known maturities)
- Survival days under stress scenario

### Step 5: Regulatory Reporting

- UK PRA: Daily LCR return for major banks
- Alert if LCR approaches 110% (management action trigger)
- Alert if LCR approaches 100% (regulatory minimum)

---

## Quality Gates

- HQLA encumbrance status verified before calculation
- Deposit balance feeds reconciled to core banking system
- All off-balance-sheet commitments included
