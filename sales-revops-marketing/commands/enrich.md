# /enrich

Single-record CRM enrichment: verify and update contact or company data.

## Usage

/enrich [company-or-contact] [context]

## Examples

/enrich "Meridian Logistics" "Key account, last updated 6 months ago"
/enrich "Jane Smith, VP Operations, Meridian Logistics" "Pre-sequence data check"
/enrich "Al Baraka Holdings" "New inbound lead, verify firmographics before scoring"

## Workflow

1. Route to crm-enrichment skill via sales-marketing-global-router
2. Identify record type (contact or company) and locate in CRM data
3. Gather fresh data from available sources (web, LinkedIn, Companies House, press)
4. Compare fresh data against existing CRM record field by field
5. Flag stale, missing, or conflicting fields with confidence scores
6. Generate enrichment report with recommended updates and data sources

## Output

- Mandatory header block (task, record type, configuration, verify data)
- Current vs. updated data comparison (field-by-field)
- Confidence score per field (HIGH / MEDIUM / LOW)
- Recommended CRM updates with change rationale
- Data sources used for each enrichment
- Fields that could not be verified

REVIEW ENRICHMENT RECOMMENDATIONS BEFORE UPDATING CRM RECORDS
