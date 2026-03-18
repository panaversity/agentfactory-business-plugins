TASK:          Discovery Brief — Enterprise Bulk Export Requests
FEATURE/AREA:  Data Management / Export Infrastructure
CONFIGURATION: Not configured (product.local.md not found — assumptions noted below)
AUDIENCE:      PM / Engineering / Design Research
VERSION:       Draft

---

# Discovery Brief: Enterprise Bulk Export Functionality

| Field     | Value                                           |
|-----------|-------------------------------------------------|
| Duration  | 2 weeks (10 business days)                      |
| Methods   | Customer interviews, support ticket analysis, CRM deal analysis, competitive audit, internal data audit |
| Sample    | Enterprise customers (n≥8 interviews); churned/at-risk accounts with export mentions (n≥3); internal stakeholders (Sales, CS, Engineering — n≥4) |

---

## Assumed Product Context

> **Note**: `product.local.md` was not found. The following assumptions are
> used as placeholders. Replace with actual product context before distributing.

- **Product**: A B2B SaaS platform with a self-serve tier and enterprise contracts.
- **Key Personas**:
  - **Enterprise Admin ("Alex")** — IT/data team lead at a 500+ seat customer who manages integrations, compliance, and data governance.
  - **Power User PM ("Jordan")** — Product or operations manager who uses the platform daily and needs data for downstream reporting.
  - **Procurement / Compliance Lead ("Sam")** — Ensures vendor contracts meet data portability and regulatory requirements.
- **Stage**: Growth — expanding enterprise segment; enterprise ACV growing but churn signals emerging.

---

## QUESTIONS TO ANSWER (ranked)

1. **What specific jobs are enterprise customers trying to do when they request "bulk export"?**
   Are they migrating data to a warehouse, fulfilling compliance/audit obligations, feeding downstream BI tools, creating backups, or preparing to churn? The answer determines whether this is a retention feature, a compliance feature, or an integration feature — each leads to a very different solution shape.

2. **What is the commercial impact of not having bulk export today?**
   How many enterprise deals have stalled, downsized, or churned where export capability was cited? What is the revenue at risk in the current pipeline? (Pull from CRM closed-lost reasons and CS escalation tags.)

3. **What data do enterprise customers actually need to export, and in what format/frequency?**
   Is this a one-time migration need or a recurring sync? Do they need raw transactional data, aggregated reports, or full account snapshots? What file formats and volumes are involved?

4. **What regulatory or contractual obligations are driving the request?**
   Are customers citing GDPR Article 20 (data portability), SOC 2 audit requirements, internal data governance policies, or procurement checklists? If compliance is the driver, the bar for "done" is externally defined.

5. **How are enterprise customers currently working around the lack of bulk export?**
   Are they screen-scraping, using the API with custom scripts, asking CS to pull manual dumps, or accepting incomplete data? The severity and cost of the workaround reveals urgency and willingness to pay.

---

## OUT OF SCOPE FOR THIS DISCOVERY

- **Solution design or technical architecture** — This sprint produces a problem definition, not a spec. Solution exploration happens after synthesis.
- **Self-serve / SMB export needs** — This discovery focuses exclusively on enterprise segment requests. SMB needs may be explored in a follow-up.
- **Pricing and packaging decisions** — Whether bulk export is a paid add-on, included in enterprise tier, or usage-based is a commercial decision that follows discovery, not part of it.
- **API-based integration patterns** — If the need turns out to be primarily API/webhook-driven rather than file export, that will be flagged as a finding but not explored in depth during this sprint.

---

## RESEARCH PLAN (Week-by-Week)

### Week 1: Data Collection & Interviews

| Day | Activity | Owner | Output |
|-----|----------|-------|--------|
| 1   | Pull and tag all support tickets mentioning "export", "download", "data out", "migration" from last 12 months. Quantify volume and segment. | PM + CS | Tagged ticket dataset with frequency counts |
| 1   | Pull CRM closed-lost and churn records where export/data portability was flagged. | PM + Sales Ops | Revenue-impact summary |
| 2-3 | Conduct 4 interviews with enterprise customers who have requested export (recruit from ticket/request list). Focus: job-to-be-done, current workaround, compliance context. | PM + Design Researcher | Interview notes (structured) |
| 3-4 | Conduct 2 interviews with churned or at-risk enterprise accounts where export was a factor. Focus: what they switched to and why. | PM | Interview notes |
| 4-5 | Internal stakeholder interviews: Sales (deal friction), CS (escalation patterns), Engineering (current API usage patterns for export-like behavior). | PM | Stakeholder input notes |
| 5   | Competitive audit: How do 3-4 direct competitors handle enterprise data export? | PM or Analyst | Competitive comparison table |

### Week 2: Synthesis & Framing

| Day | Activity | Owner | Output |
|-----|----------|-------|--------|
| 6-7 | Affinity mapping of interview findings. Cluster by job-to-be-done, not by feature request. | PM + Design Researcher | Clustered insight map |
| 7-8 | Quantitative overlay: match interview themes to ticket volumes, revenue at risk, and competitive gaps. | PM | Evidence-backed insight summary |
| 8-9 | Draft Problem Brief (using `/brief` Problem Brief format) with evidence from discovery. | PM | Problem Brief v1 |
| 9   | Internal review with Engineering lead and Design — pressure-test assumptions and feasibility signals. | PM + Eng Lead + Design | Annotated Problem Brief |
| 10  | Present findings and recommendation to product leadership. | PM | Go / no-go / redirect recommendation |

---

## RECRUITMENT CRITERIA

### Enterprise Customer Interviews (n≥8)

- **Must have**: Active enterprise contract (or churned within last 6 months)
- **Must have**: Has submitted a support ticket, feature request, or sales inquiry mentioning export, data download, data portability, or migration
- **Segment mix**: At least 2 accounts from regulated industries (financial services, healthcare, government) and at least 2 from non-regulated (tech, retail)
- **Role mix**: At least 3 interviews with Enterprise Admins ("Alex" persona), at least 2 with Power Users ("Jordan" persona), at least 1 with Procurement/Compliance ("Sam" persona)

### Recruitment Method

- CS team nominates from escalation and request logs
- Sales team nominates from pipeline and closed-lost deals
- Incentive: early access to export improvements or account credit

---

## SUCCESS CRITERIA

This discovery is successful when:

1. We can answer Question 1 (job-to-be-done) with evidence from at least 5 distinct enterprise customers, with clear clustering into no more than 3 primary use cases.
2. We can quantify the commercial impact (Question 2) with actual revenue figures — deals lost, accounts at risk, pipeline blocked — not estimates.
3. We have a clear answer to whether the primary driver is compliance/regulatory vs. operational/workflow — because the solution shape and urgency differ fundamentally.
4. We can articulate a crisp Problem Brief that the team agrees on before any solution discussion begins.
5. Product leadership can make a go / no-go / redirect decision based on the findings.

---

## OUTPUTS EXPECTED

| Output | Format | Audience | Due |
|--------|--------|----------|-----|
| Research synthesis report | Structured doc with evidence tables | PM, Design, Engineering | End of Day 8 |
| Problem Brief | `/brief` Problem Brief format | Product leadership, Engineering | End of Day 9 |
| Go / no-go / redirect recommendation | 1-page memo with supporting data | Product leadership | End of Day 10 |
| Raw interview notes (anonymized) | Shared folder | Research repository | End of Day 10 |

---

## WHAT WE DO NOT KNOW YET

- Whether "bulk export" means the same thing to different enterprise customers — it could be file download, API sync, warehouse replication, or compliance dump. We are assuming heterogeneity until proven otherwise.
- Whether this is driven by a small number of vocal accounts or represents broad enterprise demand. Ticket analysis in Week 1 will clarify.
- Whether our current API already satisfies the need and the gap is documentation/discoverability rather than capability.
- Whether competitors who offer export are winning deals specifically because of it, or whether export is table-stakes that simply removes an objection.

---

## DECISION NEEDED

**At the end of this 2-week sprint, product leadership must decide:**

1. **Go** — Commission a full PRD (use `/prd`) for enterprise bulk export, prioritized for the next quarter.
2. **No-go** — The demand is insufficient or the problem is better solved by existing capabilities (e.g., API documentation, CS-assisted exports).
3. **Redirect** — The real need is different from what was requested (e.g., the actual job is real-time integration, not batch export), and a different initiative should be scoped.

---

## NEXT STEPS

- [ ] PM to confirm or replace assumed personas with actual `product.local.md` personas
- [ ] PM to request CS ticket pull (export-related, last 12 months) — **by Day 1**
- [ ] PM to request Sales Ops CRM query (closed-lost with export mentions) — **by Day 1**
- [ ] PM + CS to recruit first 4 interview participants — **by Day 2**
- [ ] PM to schedule internal stakeholder interviews (Sales, CS, Eng) — **by Day 3**
- [ ] Design Researcher to prepare interview guide (use `/interview` skill) — **by Day 2**

---

*ALL OUTPUTS REQUIRE REVIEW BY THE PM BEFORE DISTRIBUTION TO STAKEHOLDERS.*
