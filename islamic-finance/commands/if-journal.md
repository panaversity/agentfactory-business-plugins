# /if-journal

Generate jurisdiction-aware journal entries or amortisation/distribution schedules
for an Islamic finance transaction.

## Usage

/if-journal <product> <jurisdiction> <transaction-details>

## Examples

/if-journal murabaha bahrain "BHD 500,000, 18 months, 18% markup, asset: vehicle"
/if-journal sukuk-issuer malaysia "MYR 1B, 5-year, wakala structure"
/if-journal ijarah-imb uk "GBP 350,000 home finance, 25 years, diminishing musharaka"

## Workflow

1. Route to the correct product skill via islamic-finance-router
2. Load the jurisdiction overlay from router references
3. Generate journal entries for all recognition events (initial, periodic, derecognition)
4. If the transaction spans multiple periods, produce the full amortisation/distribution schedule
5. Apply jurisdiction-specific labels and disclosure requirements
6. Flag any items requiring SSB review
