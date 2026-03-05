# /banking-aml

Analyse an AML alert, identify typologies, apply the disposition decision tree, and draft a SAR if warranted.

## Usage

/banking-aml <jurisdiction> <alert-details>

## Examples

/banking-aml uk "Cash structuring alert: 5 deposits of GBP 8-9K in 10 days, customer declared income 40K"
/banking-aml usa "PEP alert: incoming wire USD 1.2M from Cayman entity, customer is former minister"
/banking-aml uae "Rapid fund movement: AED 2M received and transferred out within 24 hours, shell company"

## Workflow

1. Route to the correct product skill via banking-global-router (aml-typologies, aml-sar-drafting, aml-cdd-edd)
2. Load the jurisdiction overlay for local SAR requirements and thresholds
3. Identify the applicable typology(ies) from the top 20 list
4. Apply the 4-level alert disposition decision tree
5. If SAR warranted: draft the SAR narrative following jurisdiction format
6. Apply the SAR quality checklist
7. Flag tipping-off requirements
8. Generate the mandatory output header and present analysis
