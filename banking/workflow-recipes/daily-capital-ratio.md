# Workflow Recipe: Daily Capital Ratio Monitor

## Task Overview

| Field         | Value                                                                         |
| ------------- | ----------------------------------------------------------------------------- |
| **Task Name** | Daily Capital Ratio Calculation and Monitor                                   |
| **Frequency** | Daily (every business day by 09:00)                                           |
| **Purpose**   | Calculate intraday capital ratios, monitor MDA headroom, flag buffer breaches |
| **Owner**     | Capital Management / Treasury                                                 |

---

## Trigger Conditions

| Trigger          | Condition                             | Action                              |
| ---------------- | ------------------------------------- | ----------------------------------- |
| **Scheduled**    | Every business day at 07:00           | Run daily capital ratio calculation |
| **Event-driven** | Large loss event (> 10bp CET1 impact) | Immediate recalculation             |
| **Event-driven** | RWA change > 2% intraday              | Alert and recalculate               |
| **Event-driven** | Regulator announces CCyB change       | Update buffer requirement           |

---

## Step-by-Step Execution

### Step 1: Extract Daily Capital Data

- CET1 capital: prior day closing + any intraday adjustments
- AT1 and Tier 2: prior day closing
- Total RWA: credit RWA (daily feed from risk system) + market RWA (daily VaR/ES) + operational RWA

### Step 2: Calculate Ratios

- CET1 Ratio = CET1 / Total RWA
- Tier 1 Ratio = (CET1 + AT1) / Total RWA
- Total Capital Ratio = (CET1 + AT1 + T2) / Total RWA
- Leverage Ratio = Tier 1 / Total Exposure Measure

### Step 3: Buffer Assessment

- Combined buffer requirement = 4.5% + CCB + CCyB + D-SIB/G-SIB surcharge
- MDA headroom = CET1 Ratio - combined buffer requirement
- Flag if MDA headroom < 100bp (amber) or < 50bp (red)

### Step 4: Generate Dashboard

Output: Daily Capital Dashboard with:

- Current ratios vs. regulatory minimums
- MDA headroom in bps
- Day-over-day change and 30-day trend
- Distance to stress trough (from latest ICAAP)

### Step 5: Alert Distribution

- Green: Dashboard to Capital Management team
- Amber (MDA < 100bp): Alert to CFO and Treasurer
- Red (MDA < 50bp): Alert to CEO, CFO, and Board Risk Committee Chair

---

## Quality Gates

- RWA feed reconciled to risk system before ratio calculation
- Capital data reconciled to GL before use
- Any manual adjustment to capital data requires CFO sign-off
