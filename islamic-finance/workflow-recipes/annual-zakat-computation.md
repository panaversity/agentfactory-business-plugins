# Workflow Recipe: Annual Zakat Computation

## Task Overview

| Field         | Value                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Task Name** | Annual Institutional Zakat Computation                                                                                                                    |
| **Frequency** | Annual (aligned with fiscal year-end or Hijri year, per jurisdiction)                                                                                     |
| **Purpose**   | Calculate the institutional zakat obligation by jurisdiction, generate payment instructions, prepare disclosure notes, and file with relevant authorities |
| **Owner**     | Financial controller / Shariah compliance officer                                                                                                         |

---

## Trigger Conditions

| Trigger                  | Condition                                                                  | Action                                                    |
| ------------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Scheduled (Saudi)**    | Fiscal year-end + 30 days (ZATCA filing deadline: 120 days after year-end) | Begin ZATCA zakat computation                             |
| **Scheduled (Pakistan)** | 1st day of Ramadan (Hijri calendar)                                        | Execute zakat deduction at source from eligible accounts  |
| **Scheduled (Malaysia)** | Per Shariah board resolution (typically fiscal year-end)                   | Calculate voluntary institutional zakat                   |
| **Scheduled (UK)**       | Fiscal year-end (voluntary, per Shariah board)                             | Calculate voluntary zakat, prepare footnote disclosure    |
| **Event-driven**         | Shariah board resolution on zakat method or rate                           | Re-calculate using approved methodology                   |
| **Event-driven**         | ZATCA audit notification (Saudi)                                           | Prepare supporting documentation                          |
| **Monthly**              | Zakat accrual monitoring                                                   | Update monthly zakat provision (1/12 of estimated annual) |

---

## Step-by-Step Execution

### Step 1: Determine Applicable Methodology by Jurisdiction

| Jurisdiction | Methodology                             | Legal Status                    | Formula Basis                                                                                       | Filing Authority              |
| ------------ | --------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| Saudi Arabia | ZATCA balance sheet formula             | Mandatory                       | Equity-based: (Share capital + Reserves + RE + Provisions) - (Fixed assets + Long-term investments) | ZATCA                         |
| Pakistan     | Zakat & Ushr Ordinance 1980             | Mandatory (deduction at source) | 2.5% of eligible deposit balances on 1st Ramadan                                                    | Central Zakat Fund via SBP    |
| Malaysia     | Hanafi net zakatable assets (voluntary) | Voluntary (fatwa-based)         | Asset-based: (Zakatable assets - Current liabilities)                                               | None (internal Shariah board) |
| UK           | AAOIFI GS 9 or Hanafi (voluntary)       | Voluntary                       | Per Shariah board adopted method                                                                    | None (internal Shariah board) |
| Bahrain      | Per AAOIFI Governance Standard 9        | Varies by entity                | Per Shariah board adopted method                                                                    | None (CBB does not collect)   |
| UAE          | Voluntary (no federal requirement)      | Voluntary                       | Per Shariah board adopted method                                                                    | None                          |

### Step 2: Extract Financial Data

**For ZATCA (Saudi Arabia):**

```
Source: Audited financial statements / trial balance
Extract:
  Share capital                     SAR ___
  Statutory reserves                SAR ___
  Retained earnings                 SAR ___
  General provisions                SAR ___
  Other equity items per ZATCA      SAR ___
  GROSS ZAKAT BASE                  SAR ___
  Less: Fixed assets (net)          SAR (__)
  Less: Long-term investments       SAR (__)
  Less: Other ZATCA deductions      SAR (__)
  NET ZATCA ZAKAT BASE              SAR ___
  x 2.5%
  ZATCA ZAKAT OBLIGATION            SAR ___
```

**For Pakistan (Zakat & Ushr):**

```
Source: Core banking system — deposit balances as of 1st Ramadan
Extract:
  Savings deposits (Islamic)        PKR ___
  Investment accounts               PKR ___
  Fixed deposits maturing < 1 year  PKR ___
  TOTAL ELIGIBLE DEPOSITS           PKR ___
  Less: Exemption certificates      PKR (__)
  NET DEPOSITS SUBJECT TO ZAKAT     PKR ___
  x 2.5%
  ZAKAT DEDUCTION AMOUNT            PKR ___

Separately:
  Bank's own institutional zakat = self-assessed per Shariah board method
```

**For Malaysia (Hanafi voluntary):**

```
Source: Audited financial statements
Extract:
  Cash and equivalents              MYR ___
  Islamic financing receivables     MYR ___
  Sukuk investments                 MYR ___
  Other liquid trade assets         MYR ___
  TOTAL ZAKATABLE ASSETS            MYR ___
  Less: Current liabilities         MYR (__)
  NET ZAKATABLE WEALTH              MYR ___
  Nisab check: > gold nisab equivalent? [YES/NO]
  x 2.5%
  ZAKAT OBLIGATION                  MYR ___
```

**For UK (voluntary):**

```
Source: Audited financial statements
Method: Per Shariah board resolution (typically Hanafi or AAOIFI GS 9)
[Same calculation structure as Malaysia]
Accounting treatment: Footnote disclosure only (per most UK Islamic banks)
```

### Step 3: Generate Journal Entries by Jurisdiction

**Saudi Arabia (ZATCA — P&L expense):**

```
Dr  Zakat Expense (P&L)                           SAR [amount]
  Cr  Zakat Payable — ZATCA                        SAR [amount]

On payment:
Dr  Zakat Payable — ZATCA                          SAR [amount]
  Cr  Cash / Bank                                   SAR [amount]
```

**Pakistan (deduction at source — agent):**

```
On 1st Ramadan (collection):
Dr  Customer Deposits — Savings                     PKR [amount]
Dr  Customer Deposits — Investment                  PKR [amount]
  Cr  Zakat Collected — Payable to CZF              PKR [total]

On remittance (within 30 days):
Dr  Zakat Collected — Payable to CZF                PKR [total]
  Cr  Cash / Bank                                    PKR [total]

Bank's own institutional zakat (if paid voluntarily):
Dr  Zakat Expense / Retained Earnings Appropriation  PKR [amount]
  Cr  Zakat Payable                                   PKR [amount]
```

**Malaysia (voluntary — equity appropriation):**

```
Dr  Retained Earnings (appropriation)              MYR [amount]
  Cr  Zakat Payable                                 MYR [amount]

On payment:
Dr  Zakat Payable                                   MYR [amount]
  Cr  Cash / Bank                                    MYR [amount]

Note: NOT a P&L expense — treated as appropriation of profit per Shariah board resolution
```

**UK (voluntary — footnote only):**

```
Option A (if treated as expense per Shariah board):
Dr  Zakat Expense                                   GBP [amount]
  Cr  Zakat Payable                                  GBP [amount]

Option B (footnote only — most common for UK IFIs):
No journal entry — disclosure in notes to financial statements only
```

### Step 4: Prepare Disclosure Notes

**For each jurisdiction, draft the appropriate disclosure:**

**Saudi Arabia:**

```
Zakat is calculated in accordance with ZATCA regulations. The zakat base
is determined using the balance sheet method prescribed by ZATCA. The zakat
charge for the year amounted to SAR [X] million (prior year: SAR [Y] million).
Zakat is classified as an expense in the income statement.
```

**Malaysia:**

```
The Bank fulfils its obligation on zakat based on a method approved by the
Shariah Supervisory Board. The zakat for the financial year amounted to
MYR [X] million (prior year: MYR [Y] million). Zakat is treated as an
appropriation of profits and charged directly to retained earnings.
```

**Pakistan:**

```
The Bank deducts zakat at source from eligible deposit accounts in accordance
with the Zakat and Ushr Ordinance 1980. Total zakat collected and remitted
to the Central Zakat Fund during the year amounted to PKR [X] million.
The Bank's own institutional zakat obligation of PKR [Y] million was
calculated in accordance with the method approved by the Shariah Board.
```

**UK:**

```
The Bank calculates its institutional zakat obligation on a voluntary basis
in accordance with the method approved by its Shariah Supervisory Board.
The zakat obligation for the year, based on the Hanafi methodology applied
to the Bank's net zakatable assets, amounted to GBP [X] million.
[If footnote only: This amount is disclosed for the information of
stakeholders and is not recognised as an expense in the income statement.]
```

### Step 5: File with Authorities (where applicable)

| Jurisdiction | Filing                         | Deadline                       | Method                    |
| ------------ | ------------------------------ | ------------------------------ | ------------------------- |
| Saudi Arabia | ZATCA zakat return             | 120 days after fiscal year-end | ZATCA electronic portal   |
| Pakistan     | Zakat deduction confirmation   | Within 30 days of 1st Ramadan  | SBP reporting system      |
| Malaysia     | No filing required (voluntary) | N/A                            | Internal board resolution |
| UK           | No filing required (voluntary) | N/A                            | Internal board resolution |

### Step 6: Payment Processing

```
Generate payment instructions:
  /outputs/zakat-payment-[jurisdiction]-[YYYY].csv

Fields: Recipient (ZATCA / CZF / designated charity), Amount, Currency,
        Bank account, Value date, Reference number

For voluntary payments (Malaysia, UK):
  Recipient per Shariah board designation (may be specific charities or
  zakat collection bodies)
```

---

## Required Skill Files

| Skill File          | Purpose                                                           |
| ------------------- | ----------------------------------------------------------------- |
| `zakat-global.md`   | All jurisdictional zakat methodologies, formulas, journal entries |
| `saudi-ifrs.md`     | ZATCA-specific formula, filing requirements, tax interaction      |
| `pakistan-ifrs.md`  | Zakat & Ushr Ordinance, deduction at source mechanics             |
| `malaysia-mfrs.md`  | Voluntary zakat, Hanafi methodology, appropriation treatment      |
| `uk-ifrs.md`        | Voluntary zakat, footnote disclosure practice                     |
| `bahrain-aaoifi.md` | AAOIFI Governance Standard 9 zakat requirements                   |

---

## Output Deliverables

| Deliverable                                   | Format                                  | Recipient                           |
| --------------------------------------------- | --------------------------------------- | ----------------------------------- |
| Zakat computation workbook (per jurisdiction) | Spreadsheet (.xlsx)                     | Financial controller, Shariah board |
| Journal entries                               | Journal entry file (.csv or ERP import) | General ledger                      |
| Disclosure note drafts (per jurisdiction)     | Word (.docx)                            | External reporting team             |
| ZATCA filing (Saudi)                          | Electronic submission                   | ZATCA                               |
| Pakistan deduction confirmation               | Regulatory return                       | SBP                                 |
| Payment instructions                          | Payment file (.csv)                     | Treasury / payments                 |
| Shariah board resolution (Malaysia/UK)        | Board minutes template                  | Shariah board secretary             |

---

## Escalation / Review Checkpoints

| Checkpoint                      | Condition                                                      | Reviewer                              |
| ------------------------------- | -------------------------------------------------------------- | ------------------------------------- |
| **Methodology approval**        | Shariah board must approve zakat calculation method annually   | SSB                                   |
| **ZATCA pre-filing review**     | Saudi zakat return reviewed before submission                  | Tax manager + external adviser        |
| **Pakistan deduction accuracy** | Deduction amounts verified against deposit balances            | Internal audit                        |
| **Zakat base dispute**          | If ZATCA queries the zakat base calculation                    | Tax manager + ZATCA liaison           |
| **Voluntary zakat amount**      | Malaysia/UK — amount reviewed and approved by Shariah board    | SSB chair                             |
| **Year-end audit**              | External auditor reviews zakat computation and disclosure      | External auditor                      |
| **Comparative analysis**        | Compare ZATCA formula result vs. Hanafi result for same entity | CFO (awareness of methodology impact) |
| **Payment confirmation**        | Zakat payments confirmed received by recipients                | Treasury + compliance                 |
