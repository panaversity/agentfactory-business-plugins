---
name: legal-spend
description: >
  Legal spend analytics, anomaly detection, and benchmarking. Analyses
  outside counsel invoices by matter type, law firm, and business unit.
  Flags billing anomalies and produces quarterly spend reports with
  rate benchmarking against market data.
user-invocable: false
---

# Legal Spend -- Analytics, Anomaly Detection, and Benchmarking

## DATA SOURCES (connect via MCP)

- Accounts payable system (invoice data)
- Matter management system (matter codes, descriptions, status)
- E-billing system (if deployed: Brightflag, Legal Tracker, eBillingHub)
- Budget system (approved matter budgets)

## ANALYSIS DIMENSIONS

By Matter Type:

- Transactional (M&A, financing, commercial contracts)
- Litigation and disputes
- Regulatory and compliance
- Employment
- IP prosecution and licensing
- General corporate / governance

By Law Firm / Provider:

- Total spend per firm
- Effective blended rate (total spend / total hours)
- Budget vs. actual variance per matter
- Write-off rate (billed vs. collected)
- Billing realisation rate

By Business Unit:

- Which business units generate the most legal spend?
- Spend per GBP/USD of revenue by business unit
- Ratio of internal legal cost vs. external legal cost

## ANOMALY DETECTION RULES -- FLAG FOR REVIEW IF:

- Invoice total exceeds matter budget by >20% without documented explanation
- Effective hourly rate >15% above agreed rates without written authorisation
- Invoice includes time entries for >12 hours in a single day
- Invoice submitted >90 days after work performed
- Same task described in multiple time entries across consecutive days
  (potential duplication)
- Significant increase in billings in a matter's final month
  (common pattern before matter close -- always review)
- Paralegal or trainee time billed at associate rates
- Multiple partners billing to the same low-complexity matter
- Research time exceeds 30% of total matter hours on a well-established
  area of law (possible training at client's expense)
- Block billing (single time entry covering multiple tasks without breakdown)
  -- request itemisation before payment approval

## BENCHMARKING COMPARISON METHOD

To compare firm rates against market:

1. Collect agreed rates from each panel firm (engagement letter / rate card)
2. Calculate effective blended rate per firm: total fees / total hours
3. Compare effective rate against benchmark reference points (below)
4. Flag any firm where effective rate exceeds benchmark by >20%
5. For each flagged firm, check: matter complexity, seniority mix, outcomes
6. Present comparison to GC with context -- do not draw conclusions
   without understanding matter complexity and outcomes

Rate comparison output:

| Firm | Agreed Rate | Effective Rate | Benchmark | Variance | Flag  |
| ---- | ----------- | -------------- | --------- | -------- | ----- |
| [X]  | GBP [X]/hr  | GBP [X]/hr     | GBP [X]   | [+/-X%]  | [Y/N] |

## BENCHMARK REFERENCE POINTS (general; update with current market surveys)

UK (London) Senior Associate -- Magic Circle: GBP 450-650/hr
UK (London) Senior Associate -- Silver Circle/Top50: GBP 300-450/hr
UK (Regional) Senior Associate: GBP 200-350/hr
US (NY/CA) Senior Associate -- AmLaw 100: USD 700-1,100/hr
In-house equivalent (all-in, UK mid-level): GBP 120,000-180,000/yr

## OUTPUT FORMAT

# LEGAL SPEND ANALYSIS -- [Period]

SUMMARY
Total spend: GBP [X]
vs. prior period: [+/-X%]
vs. budget: [+/-X%]

BY FIRM (top 5)
[Firm] GBP [X] Eff. rate: GBP [X]/hr vs. budget: [+/-X%]

ANOMALIES FLAGGED: [N]
[Item] -- [Anomaly description] -- [Recommended action]

============================================
NOTE: Billing anomalies require discussion with the relevant
partner before any payment dispute is raised.

## OUTPUT FORMAT: QUARTERLY SPEND REPORT

```
QUARTERLY LEGAL SPEND REPORT -- Q[N] [Year]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Prepared: [date]
Period: [start date] -- [end date]

EXECUTIVE SUMMARY:
Total external spend: GBP [X] (vs Q[N-1]: [+/-X%])
Total matters active: [N]
Budget utilisation: [X%] of annual budget consumed YTD
Top spending area: [matter type]

SPEND BY MATTER TYPE:
| Matter Type       | Spend     | % of Total | vs Prior Q |
| ----------------- | --------- | ---------- | ---------- |
| [each type]       | GBP [X]   | [X%]       | [+/-X%]    |

PANEL FIRM PERFORMANCE:
| Firm  | Spend     | Eff. Rate | Budget Var | Anomalies |
| ----- | --------- | --------- | ---------- | --------- |
| [X]   | GBP [X]   | GBP [X]   | [+/-X%]    | [N]       |

ANOMALIES REQUIRING REVIEW: [N]
[list with recommended actions]

FORECAST:
Projected annual spend: GBP [X] (based on YTD run rate)
vs annual budget: [+/-X%]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY BEFORE ACTION
```

## NEVER DO THESE

- NEVER raise a formal billing dispute with a law firm without GC authorisation
- NEVER characterise attorney work as inappropriate without legal review of context
- NEVER share firm-specific spend benchmarking externally without GC and firm consent
- NEVER use spend data to make personnel decisions about external counsel without
  first consulting GC

## ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY BEFORE ACTION
