# /vendor-check

Obligation tracking, vendor status check, renewal calendar, and compliance dashboard.

## Usage

/vendor-check [scope] [filter] [output-format]

## Examples

/vendor-check "Acme Corp" "all obligations" "summary"
/vendor-check scope:"all active contracts" filter:"obligations due within 60 days"
/vendor-check scope:"vendor agreements" filter:"renewal dates in 90 days" output:"compliance calendar"

## Workflow

1. Route to compliance-calendar skill via legal-global-router
2. Query connected contract repository (Google Drive / SharePoint MCP)
3. Extract obligation data: deliverables, payments, notices, renewals
4. Apply escalation timeline:
   - 60 days: add to dashboard
   - 30 days: notify obligation owner
   - 14 days: notify owner + manager
   - 7 days: notify General Counsel
   - 1 day: emergency alert (CFO for financial, GC for legal/regulatory)
   - Missed: log compliance incident; initiate remediation
5. Produce compliance calendar dashboard

## Output

- Compliance Calendar with RED/YELLOW/GREEN categorisation
- Obligations summary by owner and deadline
- Renewal calendar with notice period deadlines
- Overdue items requiring immediate action

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
