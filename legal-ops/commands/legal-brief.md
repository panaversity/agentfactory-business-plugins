# /legal-brief

Legal research, regulatory monitoring, IP analysis, legal spend analysis, and DSAR management.

## Usage

/legal-brief topic:[topic] [parameters]

## Examples

/legal-brief topic:"regulatory monitoring" jurisdictions:"UK, EU" since:"2026-03-01"
/legal-brief topic:"patent landscape analysis" subject:"AI document analysis" jurisdictions:"US, EU, UK"
/legal-brief topic:"trademark monitoring" mark:"AgentFactory" class:"9,42" jurisdiction:"UK, EU, US"
/legal-brief topic:"legal-spend-analysis" period:"Q1 2026" flag-anomalies:true
/legal-brief topic:"DSAR acknowledgement" requester:"Sarah Johnson" jurisdiction:"UK GDPR"

## Routing

The /legal-brief command routes to the appropriate product skill based on topic:

| Topic Pattern                     | Routes To              |
| --------------------------------- | ---------------------- |
| regulatory monitoring, compliance | regulatory-monitoring  |
| patent, trademark, IP, copyright  | ip-protection          |
| legal spend, invoice, billing     | legal-spend            |
| DSAR, privacy, data subject       | dsar-privacy           |
| general research, legal topic     | direct research output |

## Workflow

1. Identify topic and route to correct product skill via legal-global-router
2. Load jurisdiction overlay if applicable
3. Execute the product-specific workflow (see individual skill files)
4. Apply mandatory output header
5. Include attorney review disclaimer

## Output

- Structured briefing or analysis per the relevant product skill format
- Mandatory header block (task, jurisdiction, playbook, attorney review)
- Topic-specific output format (weekly brief, landscape analysis, spend report, etc.)

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
