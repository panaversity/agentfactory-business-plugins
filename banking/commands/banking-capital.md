# /banking-capital

Calculate Basel III/IV capital ratios, assess buffer compliance, and determine MDA headroom for a given jurisdiction.

## Usage

/banking-capital <jurisdiction> <capital-and-rwa-details>

## Examples

/banking-capital uk "CET1 GBP 285M, AT1 45M, T2 60M, Total RWA GBP 4,500M"
/banking-capital eu "IRB bank, credit RWA EUR 12B, check output floor binding"
/banking-capital singapore "D-SIB assessment, CET1 SGD 8.5B, RWA SGD 65B"

## Workflow

1. Route to the correct product skill via banking-global-router (basel-capital, basel-rwa-credit, basel-rwa-market)
2. Load the jurisdiction overlay for local minimum requirements and buffer rates
3. Calculate CET1, Tier 1, and Total Capital ratios
4. Calculate leverage ratio
5. Determine combined buffer requirement (CCB + CCyB + D-SIB/G-SIB + SyRB)
6. Calculate MDA headroom and assess distribution restrictions
7. If IRB bank: check Basel IV output floor (72.5% of SA RWA)
8. Generate the mandatory output header and present results
