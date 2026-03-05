# /if-screen

Run Shariah compliance screening on a company or portfolio.

## Usage

/if-screen <methodology> <company-or-portfolio-data>

## Methodologies

- sc-malaysia (Securities Commission Malaysia)
- tadawul (Saudi Exchange)
- aaoifi-ss21 (AAOIFI Shariah Standard 21)
- msci (MSCI Islamic Index)

## Examples

/if-screen sc-malaysia "Tenaga Nasional: debt/TA 0.35, cash+receivables/TA 0.28, ..."
/if-screen aaoifi-ss21 "Portfolio of 10 companies with balance sheet data..."

## Workflow

1. Load shariah-screening-global skill
2. Apply selected screening methodology thresholds
3. Test each financial ratio
4. Report: PASS/FAIL with specific ratio breakdowns
5. Calculate purification amount if applicable
6. Note divergence against other methodologies for the same company
