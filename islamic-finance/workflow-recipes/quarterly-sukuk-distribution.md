# Workflow Recipe: Quarterly Sukuk Distribution Processing

## Task Overview

| Field         | Value                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Task Name** | Quarterly Sukuk Distribution Processing                                                                                            |
| **Frequency** | Quarterly (within 10 business days of quarter-end)                                                                                 |
| **Purpose**   | Calculate sukuk distributions, allocate to investors, generate journal entries, prepare regulatory reporting, and process payments |
| **Owner**     | Treasury / sukuk operations unit                                                                                                   |

---

## Trigger Conditions

| Trigger          | Condition                                                       | Action                                            |
| ---------------- | --------------------------------------------------------------- | ------------------------------------------------- |
| **Scheduled**    | 5th business day after quarter-end                              | Begin distribution calculation cycle              |
| **Event-driven** | New sukuk issuance during quarter                               | Add to distribution register from settlement date |
| **Event-driven** | Sukuk maturity during quarter                                   | Process final distribution + principal repayment  |
| **Event-driven** | Rating downgrade of sukuk holding                               | Reassess ECL staging before distribution          |
| **Event-driven** | Issuer announces distribution rate change (variable rate sukuk) | Update calculation with new rate                  |
| **Manual**       | Board or SSB requests early distribution reporting              | Run on-demand                                     |

---

## Step-by-Step Execution

### Step 1: Load Sukuk Portfolio Register

```
Source: /inputs/sukuk-portfolio-register-[YYYY-QN].csv
Fields required per holding:
  - Sukuk ISIN / identifier
  - Issuer name
  - Structure (ijarah, musharakah, wakala, hybrid)
  - Face value held
  - Distribution rate (fixed or variable)
  - Distribution frequency (semi-annual, quarterly, annual)
  - Next distribution date
  - Day count convention (Actual/360, Actual/365, 30/360)
  - IFRS 9 classification (amortised cost, FVOCI, FVPL)
  - ECL stage (1, 2, 3)
  - Jurisdiction of issuer
  - Jurisdiction of investor (our entity)
  - Currency
Validate: All holdings reconcile to custody statements, no stale pricing data
```

### Step 2: Calculate Distribution Amounts

**For each sukuk holding:**

```
Distribution = Face value x Distribution rate x (Days in period / Day count basis)

Example (ijarah sukuk, quarterly):
  Face value: $50,000,000
  Distribution rate: 5.25% p.a.
  Days in quarter: 91
  Day count: Actual/360
  Distribution = $50,000,000 x 5.25% x (91/360) = $663,541.67
```

**For variable rate sukuk:**

```
Distribution rate = Reference rate (e.g., SOFR) + Spread
Fetch current reference rate from /inputs/market-rates.csv
Calculate distribution using current rate
```

### Step 3: Income Recognition by Framework

**Amortised Cost (IFRS 9 / MFRS 9):**

```
Income recognised = Carrying value x Effective profit rate x (Days / 360)
Note: EPR income may differ from cash distribution if purchased at premium/discount
Amortisation adjustment = EPR income - Cash distribution received
```

**FVOCI (IFRS 9):**

```
Income recognised = Same as amortised cost (EPR method through P&L)
Fair value change = (Quarter-end fair value - Prior quarter fair value) through OCI
Fetch quarter-end market values from /inputs/sukuk-market-values.csv
```

**FVPL (IFRS 9):**

```
Income = Cash distribution + Fair value change (both through P&L)
```

**AAOIFI FAS 25 (Bahrain/Qatar investors):**

```
Classification per AAOIFI FAS 25 measurement categories
Income label: "Income from Sukuk Investments" — NEVER "interest income"
```

### Step 4: Generate Journal Entries

**Distribution received (amortised cost):**

```
Dr  Cash / Bank                                    [distribution amount]
Dr  Amortisation adjustment (if premium)            [adjustment]
  Cr  Income from Sukuk Investments                  [EPR income amount]
  Cr  Amortisation adjustment (if discount)          [adjustment]
```

**Distribution received (FVOCI):**

```
Dr  Cash / Bank                                    [distribution amount]
  Cr  Income from Sukuk Investments                  [EPR income amount]
  Cr/Dr  Amortisation adjustment                     [premium/discount]

Dr/Cr  Sukuk Investments — FVOCI                   [fair value change]
  Cr/Dr  Other Comprehensive Income — Sukuk          [fair value change]
```

**ECL provision update:**

```
Dr  ECL Expense — Sukuk Investments                [provision change]
  Cr  ECL Allowance — Sukuk Investments              [provision change]
```

### Step 5: Investor Allocation (if issuer)

**For entities that are sukuk ISSUERS:**

```
Calculate total distribution payable to all investors:
  Total = Face value outstanding x Distribution rate x (Days / Day count)

Allocate to investor register:
  Each investor's share = (Investor holding / Total outstanding) x Total distribution

Generate payment instruction file:
  /outputs/sukuk-distribution-payment-[YYYY-QN].csv
  Fields: Investor name, Account, IBAN, Currency, Amount, Value date
```

### Step 6: Regulatory Reporting

**Prepare jurisdiction-specific regulatory returns:**

| Jurisdiction | Regulator | Return                      | Content                                           |
| ------------ | --------- | --------------------------- | ------------------------------------------------- |
| Bahrain      | CBB       | Quarterly prudential return | Sukuk portfolio by type, maturity, rating, income |
| Malaysia     | BNM       | Statistical return          | Islamic securities by classification, income      |
| UAE          | CBUAE     | Quarterly return            | Investment securities schedule                    |
| Saudi        | SAMA      | Quarterly return            | Sukuk portfolio analysis                          |
| UK           | PRA       | Regulatory return           | Investment holdings, RWA calculation              |
| Nigeria      | CBN       | Non-interest banking return | Sukuk by structure, maturity, credit quality      |

```
Output: /outputs/regulatory-sukuk-return-[jurisdiction]-[YYYY-QN].xlsx
```

### Step 7: Validate and Reconcile

```
Validation checks:
  □ Total distributions received = sum of individual calculations
  □ Income recognised reconciles to GL trial balance
  □ FVOCI OCI movement reconciles to fair value changes
  □ ECL provisions updated for any staging changes
  □ Investor payment file reconciles to total distribution payable
  □ Custody statement reconciles to internal register
  □ All labels jurisdiction-compliant (no "interest" terminology)
```

---

## Required Skill Files

| Skill File                                                         | Purpose                                                      |
| ------------------------------------------------------------------ | ------------------------------------------------------------ |
| `sukuk-investor.md`                                                | IFRS 9 classification, SPPI test, income recognition methods |
| `sukuk-issuer.md`                                                  | Distribution calculation, investor allocation, derecognition |
| `bahrain-aaoifi.md`                                                | AAOIFI FAS 25 classification and measurement                 |
| `malaysia-mfrs.md`                                                 | MFRS 9 labels and BNM reporting                              |
| `uae-ifrs.md` / `saudi-ifrs.md` / `uk-ifrs.md` / `nigeria-ifrs.md` | Jurisdiction-specific regulatory returns                     |

---

## Output Deliverables

| Deliverable                           | Format                                  | Recipient             |
| ------------------------------------- | --------------------------------------- | --------------------- |
| Distribution calculation workbook     | Spreadsheet (.xlsx)                     | Treasury, accounting  |
| Journal entries                       | Journal entry file (.csv or ERP import) | General ledger        |
| FVOCI OCI movement schedule           | Spreadsheet (.xlsx)                     | Financial reporting   |
| Investor payment file (if issuer)     | Payment instruction (.csv)              | Operations / payments |
| Regulatory returns (per jurisdiction) | Jurisdiction-specific format            | Regulator             |
| Quarter-end sukuk portfolio summary   | Markdown (.md)                          | CFO, board            |

---

## Escalation / Review Checkpoints

| Checkpoint                          | Condition                                                         | Reviewer                   |
| ----------------------------------- | ----------------------------------------------------------------- | -------------------------- |
| **Distribution calculation review** | Before payment processing                                         | Treasury manager           |
| **ECL staging change**              | Any sukuk moves between stages                                    | Credit risk committee      |
| **Fair value loss > 5%**            | Any FVOCI holding loses > 5% in quarter                           | CIO / investment committee |
| **Issuer credit event**             | Missed distribution, restructuring, default                       | Risk committee + SSB       |
| **Regulatory deadline**             | Returns submitted within regulatory timeline                      | Compliance officer         |
| **Year-end**                        | Full sukuk portfolio audit, fair value verification               | External auditor           |
| **Shariah compliance**              | Quarterly confirmation that all holdings remain Shariah-compliant | SSB                        |
