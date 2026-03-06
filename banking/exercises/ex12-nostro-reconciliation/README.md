# Exercise 12: Nostro Reconciliation

## Scenario Profile

| Field               | Value                         |
| ------------------- | ----------------------------- |
| **Domain**          | Bank Reconciliation -- Nostro |
| **Jurisdiction**    | Global (multi-currency)       |
| **Time Estimate**   | 35 minutes                    |
| **Skills Required** | `bank-reconciliation`         |

---

## Data

You are an Operations analyst performing the daily nostro reconciliation for a USD nostro account held with JPMorgan Chase, New York.

### Internal Mirror (Your Bank's Records)

| Ref  | Date  | Description                                | Debit USD | Credit USD |
| ---- | ----- | ------------------------------------------ | --------- | ---------- |
| M001 | 3 Mar | Wire to ABC Corp (client instruction)      | 250,000   |            |
| M002 | 3 Mar | Wire to Delta Trading (client instruction) | 180,000   |            |
| M003 | 3 Mar | Expected receipt from Gulf Oil Ltd         |           | 425,000    |
| M004 | 4 Mar | Wire to Meridian Holdings                  | 95,000    |            |
| M005 | 4 Mar | Expected receipt from Osaka Industries     |           | 310,000    |
| M006 | 5 Mar | Wire to Santos Energy SA                   | 520,000   |            |
| M007 | 5 Mar | FX settlement USD buy (treasury)           |           | 1,200,000  |

### External Statement (JPMorgan Chase Statement -- MT940)

| Ref  | Date  | Description                   | Debit USD | Credit USD |
| ---- | ----- | ----------------------------- | --------- | ---------- |
| S001 | 3 Mar | Wire ABC Corp                 | 250,000   |            |
| S002 | 3 Mar | Wire Delta Trading            | 179,964   |            |
| S003 | 3 Mar | Credit Gulf Oil Ltd           |           | 425,000    |
| S004 | 4 Mar | Correspondent fee (quarterly) | 1,850     |            |
| S005 | 4 Mar | Wire Meridian Holdings        | 95,000    |            |
| S006 | 5 Mar | FX settlement USD buy         |           | 1,200,000  |
| S007 | 5 Mar | Credit Parsec Technologies    |           | 88,500     |
| S008 | 5 Mar | Wire Santos Energy SA         | 520,000   |            |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The internal mirror and external statement (MT940) data tables above
- Skills active: `bank-reconciliation`
- Estimated time: 35 minutes

---

## Step-by-Step Instructions

### Step 1: Apply Matching Hierarchy (15 min)

Apply the 5-step matching hierarchy from `bank-reconciliation`:

1. **Exact Match**: Match items where amount, date, and reference all agree
2. **Fuzzy Match**: Match items where amount and date agree but reference differs slightly
3. **Date Tolerance**: Match items where amount and reference agree but date differs by up to 2 business days
4. **Partial Sum Pool**: Check for multiple items on one side matching a single item on the other
5. **Unmatched Residual**: Identify all remaining unmatched items

Build the reconciliation table showing matched pairs and unmatched items.

### Step 2: Classify Breaks (10 min)

For each unmatched item, classify the break:

- M002 vs S002: Amount mismatch (USD 180,000 vs USD 179,964) -- what caused the difference?
- S004: Statement-only item (correspondent fee) -- no mirror entry
- M005: Mirror-only item (expected receipt from Osaka Industries) -- no statement entry
- S007: Statement-only item (unexpected credit from Parsec Technologies) -- no mirror entry

### Step 3: Resolution Actions (5 min)

For each break, prescribe the action per the ageing SLA:

1. Amount difference on M002/S002: likely correspondent fee deduction (SHA/OUR confusion)
2. S004 correspondent fee: post to bank charges account
3. M005 missing receipt: check SWIFT gpi tracker, initiate counterparty query if > 2 days
4. S007 unidentified credit: move to Payment Suspense within 24 hours, search expected inbound pipeline

### Step 4: Daily Break Report (5 min)

Compile the daily nostro break report with:

- Break type classification
- Age in business days
- Investigation status and next action
- Assigned owner

---

## Deliverable

Produce: Nostro reconciliation certificate with matched pairs table, break classification schedule, resolution actions with ageing SLA status, and daily break report for Operations sign-off.

---

## Key Learning

- The matching hierarchy must be applied in order: exact match first, then progressively looser matching
- Amount differences between mirror and statement are often caused by correspondent fees or FX rounding
- Unidentified credits must be moved to suspense within 24 hours -- never leave them in the nostro mirror
- SWIFT gpi tracker should be checked before raising formal counterparty queries for recent payments
- Every break must have an assigned owner and documented investigation status
