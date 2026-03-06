# Exercise 2: Corporate ECL Model -- GCC

## Scenario Profile

| Field               | Value                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| **Domain**          | IFRS 9 ECL -- Corporate Portfolio                                      |
| **Jurisdiction**    | GCC (UAE CBUAE / UK PRA cross-border)                                  |
| **Time Estimate**   | 55 minutes                                                             |
| **Skills Required** | `ifrs9-ecl`, `ifrs9-scenarios`, `ifrs9-staging`, `uae-cbuae`, `uk-pra` |

---

## Portfolio Data

You are the credit risk analyst for a GCC-focused international bank with head office in London (PRA-regulated) and a major subsidiary in Abu Dhabi (CBUAE-regulated). Assess ECL for the following 6 corporate borrowers.

| Borrower           | Country | Sector        | Rating | Facility GBP M | Maturity | Collateral      |
| ------------------ | ------- | ------------- | ------ | -------------- | -------- | --------------- |
| Al-Jazira Steel    | KSA     | Manufacturing | BB+    | 45.0           | 3 years  | Unsecured       |
| Dubai Towers       | UAE     | Real Estate   | BBB    | 120.0          | 5 years  | CRE (LTV 70%)   |
| Gulf Energy        | Bahrain | Energy        | A-     | 85.0           | 4 years  | Secured (plant) |
| Riyadh Retail      | KSA     | Consumer      | BB     | 30.0           | 2 years  | Unsecured       |
| Emirates Logistics | UAE     | Transport     | BBB-   | 55.0           | 3 years  | Fleet (LTV 60%) |
| Manama Finance     | Bahrain | Financial     | BB-    | 25.0           | 1 year   | Unsecured       |

## Macroeconomic Scenarios

| Scenario | Weight | GCC GDP Growth | Oil Price USD/bbl | UK GDP Growth | Unemployment |
| -------- | ------ | -------------- | ----------------- | ------------- | ------------ |
| Upside   | 15%    | 4.5%           | 95                | 2.0%          | 3.5%         |
| Base     | 40%    | 2.8%           | 78                | 1.2%          | 4.2%         |
| Adverse  | 30%    | 0.5%           | 55                | -0.5%         | 5.8%         |
| Severe   | 15%    | -2.0%          | 38                | -2.5%         | 7.5%         |

## PD and LGD Parameters

| Rating | TTC PD (Annual) | CCA Base | CCA Adverse | CCA Severe | CCA Upside |
| ------ | --------------- | -------- | ----------- | ---------- | ---------- |
| A-     | 0.15%           | 1.0      | 1.4         | 2.2        | 0.8        |
| BBB    | 0.35%           | 1.0      | 1.5         | 2.5        | 0.8        |
| BBB-   | 0.50%           | 1.0      | 1.5         | 2.5        | 0.8        |
| BB+    | 0.80%           | 1.0      | 1.6         | 2.8        | 0.7        |
| BB     | 1.20%           | 1.0      | 1.7         | 3.0        | 0.7        |
| BB-    | 1.80%           | 1.0      | 1.8         | 3.2        | 0.7        |

| Collateral Type                   | LGD |
| --------------------------------- | --- |
| Unsecured corporate               | 45% |
| CRE (LTV <= 70%)                  | 30% |
| Secured (plant/fleet, LTV <= 60%) | 25% |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The 6-borrower GCC corporate portfolio and macroeconomic scenario tables above
- Skills active: `ifrs9-ecl`, `ifrs9-scenarios`, `ifrs9-staging`, `uae-cbuae`, `uk-pra`
- Estimated time: 55 minutes

---

## Step-by-Step Instructions

### Step 1: Stage Assessment (10 min)

Assess the stage for each borrower. All are currently performing (no DPD). Consider qualitative factors: sector stress, GCC oil dependency, real estate cycle.

### Step 2: PIT PD Conversion (10 min)

Convert TTC PD to PIT PD for each scenario using the CCA factors provided.

### Step 3: 12-Month ECL (Stage 1) per Scenario (10 min)

Calculate ECL_12 = PIT_PD x LGD x EAD for each borrower under each scenario.

### Step 4: Scenario-Weighted ECL (10 min)

Compute the probability-weighted ECL across all 4 scenarios.
Verify that Weighted ECL != ECL at weighted-average PD (demonstrate non-linearity).

### Step 5: CBUAE vs PRA Reporting (10 min)

Identify any differences in reporting for the Abu Dhabi subsidiary vs the London head office:

- CBUAE minimum CET1 of 7.0% vs PRA minimum
- Any CBUAE-specific provisioning requirements above IFRS 9

### Step 6: Governance Documentation (5 min)

Draft the scenario justification note for the IFRS 9 Governance Committee, including scenario weights rationale.

---

## Deliverable

Produce: GCC corporate ECL summary table with scenario-weighted ECL per borrower, CBUAE vs PRA reporting comparison, and a Risk Committee briefing note with scenario justification.

---

## Key Learning

- PIT PD conversion is mandatory for IFRS 9 -- TTC PDs systematically understate risk in downturns
- Scenario weighting must reflect genuine management view; equal weights are rarely defensible
- GCC exposures are highly correlated with oil price -- this must be reflected in scenario design
- Cross-border banks must satisfy BOTH home and host regulator provisioning requirements
