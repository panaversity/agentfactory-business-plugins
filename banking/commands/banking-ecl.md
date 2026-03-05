# /banking-ecl

Calculate IFRS 9 Expected Credit Loss for a facility or portfolio, applying jurisdiction-specific rules and scenario weighting.

## Usage

/banking-ecl <jurisdiction> <portfolio-or-facility-details>

## Examples

/banking-ecl uk "Retail mortgage, GBP 250K, LTV 75%, rating BB+, current on payments"
/banking-ecl uae "Corporate portfolio: 6 borrowers, see attached data table"
/banking-ecl eu "Stage 2 migration assessment for SME book, 30+ DPD facilities"

## Workflow

1. Route to the correct product skill via banking-global-router (ifrs9-ecl, ifrs9-staging, ifrs9-scenarios)
2. Load the jurisdiction overlay for local requirements
3. Assess IFRS 9 stage using the staging decision tree
4. Calculate ECL using scenario-weighted PIT PD x LGD x EAD
5. Apply jurisdiction-specific minimum provisions if applicable (e.g., CBUAE, SBP floors)
6. Generate the mandatory output header (GOVERNING STANDARD, DOMAIN, JURISDICTION)
7. Present results with stage justification, ECL breakdown, and disclosure-ready format
