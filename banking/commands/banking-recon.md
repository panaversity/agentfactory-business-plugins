# /banking-recon

Perform bank reconciliation (nostro, suspense, IFRS 9 provision, GL-to-risk), apply matching hierarchy, classify breaks, and prescribe resolution actions.

## Usage

/banking-recon <recon-type> <data-details>

## Examples

/banking-recon nostro "USD nostro with JPMorgan, 7 mirror entries, 8 statement entries, see data"
/banking-recon provision "Quarterly four-way recon: model ECL 94.4M, risk system 94.0M, GL 94.4M"
/banking-recon suspense "12 items across 3 suspense accounts, ages 1-35 days, month-end clearance"

## Workflow

1. Route to the bank-reconciliation skill via banking-global-router
2. Identify reconciliation type (nostro, provision, suspense, inter-company, trade)
3. Apply the 5-step matching hierarchy (exact, fuzzy, date tolerance, partial sum, unmatched)
4. Classify each break (timing, data, manual, FX, amount mismatch)
5. Apply ageing SLA enforcement and identify required escalations
6. Prescribe resolution action for each break
7. Generate the reconciliation report with break summary, age analysis, and action items
