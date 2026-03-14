# /compliance-calendar

Obligation tracking, renewal calendar, deadline management, and compliance dashboard with jurisdiction-aware escalation.

## Usage

/compliance-calendar [scope] [filter] [output-format]

## Examples

/compliance-calendar "all active contracts" "obligations due within 60 days"
/compliance-calendar scope:"vendor agreements" filter:"renewal dates in 90 days" output:"dashboard"
/compliance-calendar "Acme Corp" "all obligations" "summary"

## Workflow

1. Route to compliance-calendar skill via legal-global-router
2. Load jurisdiction overlay for regulatory deadline context
3. Query connected contract repository (Google Drive / SharePoint MCP)
4. Extract obligation data: deliverables, payments, notices, renewals, regulatory filings
5. Apply escalation timeline:
   - 60 days: add to dashboard
   - 30 days: notify obligation owner
   - 14 days: notify owner + manager
   - 7 days: notify General Counsel; add to weekly brief
   - 1 day: emergency alert (CFO for financial, GC for legal/regulatory)
   - Missed: log compliance incident; initiate remediation
6. Produce compliance calendar dashboard with RED/YELLOW/GREEN categorisation

## Coverage

- **Contract obligations**: deliverables, payments, notice periods, audit windows, SLA reviews
- **Regulatory filings**: annual returns, licence renewals, data protection registrations
- **Internal reviews**: DPIA, privacy policy, HR policy, infosec policy, vendor risk
- **Auto-renewal alerts**: flag contracts approaching auto-renewal that should be renegotiated

## Output

- Compliance Calendar with RED (overdue) / YELLOW (due 14 days) / GREEN (due 15-60 days)
- Obligations summary by owner and deadline
- Renewal calendar with notice period deadlines (last date to give non-renewal notice)
- Overdue items requiring immediate action
- Total open obligations count

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
