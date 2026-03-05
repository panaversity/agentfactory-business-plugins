# Workflow Recipe: Monthly Murabaha Income Recognition

## Task Overview

| Field         | Value                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Task Name** | Monthly Murabaha Income Recognition and Disclosure Update                                                                                    |
| **Frequency** | Monthly (last business day of each month)                                                                                                    |
| **Purpose**   | Recognise murabaha profit income for the period, update deferred income balances, generate journal entries, and refresh disclosure schedules |
| **Owner**     | Islamic finance accounting unit / financial controller                                                                                       |

---

## Trigger Conditions

| Trigger          | Condition                                          | Action                                                 |
| ---------------- | -------------------------------------------------- | ------------------------------------------------------ |
| **Scheduled**    | Last business day of each month at 17:00           | Run full monthly income recognition cycle              |
| **Event-driven** | New murabaha facility booked during month          | Include in current month recognition from booking date |
| **Event-driven** | Early settlement received                          | Accelerate remaining deferred income, close facility   |
| **Event-driven** | Facility classified as non-performing (Stage 3)    | Suspend income recognition, reverse accrued income     |
| **Manual**       | Month-end close adjustment requested by controller | Run with specific override parameters                  |

---

## Step-by-Step Execution

### Step 1: Extract Active Murabaha Portfolio

```
Source: Core banking system / /inputs/murabaha-portfolio-[YYYY-MM].csv
Fields required per facility:
  - Facility ID
  - Customer name
  - Booking date
  - Cost price
  - Selling price
  - Total deferred profit (selling price minus cost)
  - Tenure (months)
  - Outstanding receivable (gross)
  - Deferred murabaha income balance
  - ECL stage (1, 2, or 3)
  - Instalment amount
  - Instalments received this month
  - Jurisdiction
  - Applicable framework (AAOIFI FAS 2, MFRS 9, IFRS 9)
Validate: All active facilities included, no duplicate entries, ECL staging current
```

### Step 2: Calculate Monthly Income Per Facility

**For AAOIFI FAS 2 (Bahrain, Qatar):**

```
Method: Proportional allocation
Monthly income = (Total deferred profit / Total number of instalments) x Instalments due this month
OR
Monthly income = Deferred profit x (Monthly instalment / Total selling price)

Label: "Murabaha Income" — NEVER "interest income"
```

**For MFRS 9 / IFRS 9 (Malaysia, UAE, Saudi, UK, etc.):**

```
Method: Effective profit rate (EPR) / effective interest rate
Monthly income = Opening amortised cost balance x Monthly EPR

Label per jurisdiction:
  - Malaysia: "Profit from Islamic Financing"
  - UAE/Saudi/UK: "Income from Islamic Financing"
  - NEVER "interest income" in any jurisdiction
```

### Step 3: Handle Non-Performing Facilities

```
IF facility ECL Stage = 3 (non-performing):
  → Suspend income recognition
  → Reverse any accrued income not yet received in cash
  → Journal: Dr Murabaha Income (reversal), Cr Accrued Income Receivable
  → Note: Income recognised on cash basis only for Stage 3

IF facility ECL Stage transitions from 1→2:
  → Continue income recognition on accrual basis
  → Increase ECL provision per IFRS 9 / AAOIFI requirements
```

### Step 4: Generate Journal Entries

**Standard monthly entry (performing facilities):**

```
Dr  Accrued Murabaha Income Receivable    [amount]
  Cr  Deferred Murabaha Income              [amount]     (AAOIFI)
  OR
Dr  [no separate deferred income entry under IFRS 9 amortised cost]
  Cr  Income from Islamic Financing          [amount]     (IFRS 9)
```

**Instalment receipt entry:**

```
Dr  Cash / Bank                              [instalment amount]
  Cr  Murabaha Receivable (gross)             [instalment amount]
```

**Early settlement entry:**

```
Dr  Cash / Bank                              [settlement amount]
Dr  Deferred Murabaha Income                 [remaining deferred balance]
  Cr  Murabaha Receivable (gross)             [outstanding receivable]
  Cr  Murabaha Income — Early Settlement      [accelerated income, if applicable]
```

### Step 5: Update Disclosure Schedules

```
Output: /outputs/murabaha-income-schedule-[YYYY-MM].xlsx

Tab 1: Monthly Income Summary
  - Total murabaha income recognised this month
  - Breakdown by tenor bucket (< 1 year, 1-3 years, > 3 years)
  - Breakdown by jurisdiction
  - Comparison to prior month and budget

Tab 2: Deferred Income Movement
  - Opening deferred murabaha income
  - New facilities booked (additions)
  - Income recognised this month (releases)
  - Early settlements (accelerations)
  - Closing deferred murabaha income

Tab 3: Non-Performing Facilities
  - Facilities in Stage 3
  - Income suspended this month
  - Cumulative suspended income
  - Cash basis income received (if any)

Tab 4: Portfolio Aging
  - 0-30 days past due
  - 31-60 days past due
  - 61-90 days past due
  - 90+ days past due
  - Portfolio quality ratios (NPF ratio, coverage ratio)
```

### Step 6: Validate and Post

```
Validation checks:
  □ Total income recognised = sum of individual facility calculations
  □ Closing deferred income = Opening - Released + New facilities
  □ No income recognised on Stage 3 facilities (unless cash basis)
  □ Labels are jurisdiction-compliant (no "interest" anywhere)
  □ Reconciliation to general ledger trial balance
```

---

## Required Skill Files

| Skill File                                     | Purpose                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------ |
| `murabaha.md`                                  | Income recognition rules (AAOIFI proportional vs. IFRS 9 effective rate) |
| `bahrain-aaoifi.md`                            | AAOIFI FAS 2 specific labels and presentation                            |
| `malaysia-mfrs.md`                             | MFRS 9 labels ("Profit from Islamic Financing")                          |
| `uae-ifrs.md` / `saudi-ifrs.md` / `uk-ifrs.md` | Jurisdiction-specific labels and disclosure                              |
| `zakat-global.md`                              | Murabaha receivables in zakat base (if applicable)                       |

---

## Output Deliverables

| Deliverable                    | Format                                  | Recipient                          |
| ------------------------------ | --------------------------------------- | ---------------------------------- |
| Monthly journal entries        | Journal entry file (.csv or ERP import) | General ledger / accounting system |
| Murabaha income schedule       | Spreadsheet (.xlsx)                     | Financial controller, CFO          |
| Non-performing facility report | Markdown (.md)                          | Credit risk, Shariah compliance    |
| Disclosure note update         | Word (.docx) draft                      | External reporting team            |

---

## Escalation / Review Checkpoints

| Checkpoint             | Condition                                                    | Reviewer                         |
| ---------------------- | ------------------------------------------------------------ | -------------------------------- |
| **Pre-posting review** | All journal entries reviewed before GL posting               | Senior accountant                |
| **NPF threshold**      | If NPF ratio exceeds 3%, escalate to risk committee          | Head of credit risk              |
| **Income variance**    | If monthly income varies > 10% from prior month, investigate | Financial controller             |
| **Methodology change** | If switching between proportional and effective rate methods | CFO + external auditor           |
| **Quarter-end**        | Additional disclosure review for interim reporting           | External auditor                 |
| **Year-end**           | Full reconciliation and auditor walkthrough                  | External auditor + Shariah audit |
