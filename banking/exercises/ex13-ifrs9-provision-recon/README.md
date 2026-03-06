# Exercise 13: IFRS 9 Provision Reconciliation

## Scenario Profile

| Field               | Value                                                            |
| ------------------- | ---------------------------------------------------------------- |
| **Domain**          | Bank Reconciliation -- IFRS 9 Four-Way Recon                     |
| **Jurisdiction**    | United Kingdom (PRA)                                             |
| **Time Estimate**   | 40 minutes                                                       |
| **Skills Required** | `bank-reconciliation`, `ifrs9-ecl`, `ifrs9-disclosure`, `uk-pra` |

---

## Data

You are the Finance Controller performing the quarterly IFRS 9 four-way reconciliation before signing the reconciliation certificate.

### Tier 1: ECL Model Output (approved by IFRS 9 Governance Committee)

| Stage                      | ECL GBP M |
| -------------------------- | --------- |
| Stage 1                    | 18.4      |
| Stage 2                    | 42.7      |
| Stage 3                    | 28.1      |
| PMA (management overlay)   | 5.2       |
| **Total ECL Model Output** | **94.4**  |

### Tier 2: Risk System Facility Sum

| Stage                 | ECL GBP M |
| --------------------- | --------- |
| Stage 1               | 18.4      |
| Stage 2               | 42.3      |
| Stage 3               | 28.1      |
| PMA                   | 5.2       |
| **Total Risk System** | **94.0**  |

### Tier 3: GL Provision Account Balance

| Account                     | Balance GBP M |
| --------------------------- | ------------- |
| IFRS 9 Provision -- Stage 1 | 18.4          |
| IFRS 9 Provision -- Stage 2 | 42.7          |
| IFRS 9 Provision -- Stage 3 | 27.5          |
| IFRS 9 PMA Account          | 5.8           |
| **Total GL Provision**      | **94.4**      |

### Tier 4: Financial Statement Disclosure (draft IFRS 7 note)

| Stage                | ECL GBP M (per disclosure) |
| -------------------- | -------------------------- |
| Stage 1              | 18.4                       |
| Stage 2              | 42.7                       |
| Stage 3              | 28.1                       |
| PMA                  | 5.2                        |
| **Total Disclosure** | **94.4**                   |

---

## Known Breaks

Three breaks have been identified. Your task is to investigate, explain, and resolve each.

### Break 1: Tier 1 vs Tier 2 (Stage 2 difference: GBP 0.4M)

Model output shows Stage 2 ECL of GBP 42.7M but risk system shows GBP 42.3M.

### Break 2: Tier 2 vs Tier 3 (Stage 3 difference: GBP 0.6M)

Risk system shows Stage 3 ECL of GBP 28.1M but GL shows GBP 27.5M.

### Break 3: Tier 3 vs Tier 3 (PMA difference: GBP 0.6M)

GL PMA account shows GBP 5.8M but model output and risk system show GBP 5.2M.

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The four-tier data tables (ECL model output, risk system, GL, financial statement disclosure) above
- Skills active: `bank-reconciliation`, `ifrs9-ecl`, `ifrs9-disclosure`, `uk-pra`
- Estimated time: 40 minutes

---

## Step-by-Step Instructions

### Step 1: Map the Four Tiers (5 min)

Build the four-way reconciliation matrix showing all tiers side by side with differences highlighted.

### Step 2: Investigate Break 1 (10 min)

Tier 1 (Model) vs Tier 2 (Risk System): GBP 0.4M Stage 2 difference.
Possible causes:

- New facilities booked after the model run cut-off
- Upload error from model output to risk system
- Timing difference in stage migration

Determine the most likely cause and prescribe the resolution action.

### Step 3: Investigate Break 2 (10 min)

Tier 2 (Risk System) vs Tier 3 (GL): GBP 0.6M Stage 3 difference.
Possible causes:

- Write-off processed in risk system but GL journal not yet posted
- Manual override in GL without corresponding risk system update
- FX translation difference

Determine the most likely cause and prescribe the resolution action.

### Step 4: Investigate Break 3 (10 min)

Tier 3 (GL) PMA account shows GBP 5.8M but model shows GBP 5.2M.
Possible causes:

- Prior quarter PMA not fully released
- New PMA approved but model not updated
- GL journal contains a data entry error (GBP 0.6M over-posted)

Determine the most likely cause and prescribe the resolution action.

### Step 5: Reconciliation Certificate (5 min)

After resolving all breaks:

1. Restate each tier with corrected amounts
2. Confirm all four tiers agree
3. Sign off the reconciliation certificate
4. Document the root causes and corrective actions for the audit file

---

## Deliverable

Produce: Four-way provision reconciliation sign-off memo with reconciliation matrix, root cause analysis for each break, corrective action log, restated tier amounts, and signed reconciliation certificate.

---

## Key Learning

- The four-way reconciliation is mandatory at every reporting date and must agree before close
- Model-to-risk-system breaks are typically caused by timing (new facilities, upload errors)
- Risk-system-to-GL breaks are typically caused by write-offs or manual GL journals
- PMA breaks often arise from prior quarter PMAs not being properly released or updated
- Every break must be traced to a specific root cause with documented corrective action
- The reconciliation certificate cannot be signed with unexplained differences
