PRODUCT RETROSPECTIVE: Quick Reports
Shipped: 2026-02-05 | Retro date: 2026-03-19 | PM: [Unspecified]
================================================================

Q1: DID IT SOLVE THE PROBLEM?

Original problem:   Reporting workflow was too slow and generated excessive support tickets.
Target outcome:     50% adoption among target users, reduced support burden, improved NPS.

Evidence:
[WARN] Adoption: 34% actual vs. 50% target — below goal by 16pp
[PASS] Support tickets: reports-related tickets dropped 60% — strong improvement
[PASS] NPS: reporting NPS improved from 6.2 to 7.1 (+0.9) — meaningful positive shift

Verdict: PARTIALLY SOLVED
Summary: Quick Reports significantly improved the user experience for those who adopted
it — support tickets dropped 60% and NPS rose meaningfully. However, adoption at 34%
is well below the 50% target, meaning the majority of target users haven't switched.
The feature works well for those who find it, but discoverability or onboarding to the
feature itself needs investigation. The support and NPS improvements suggest the
underlying solution is sound; the gap is in getting users to it.

Q2: DID WE BUILD IT AS INTENDED?

[WARN] Delivered on time: 1 week late — scope change (PDF export added mid-sprint)
[WARN] Spec quality:     PDF export was not in the original spec; added during development
[FAIL] Scope maintained: Scope change mid-sprint — PDF export added without formal change control
[    ] Quality (bugs):   No bug data provided — needs follow-up
[    ] ACs met:          No AC verification data provided — needs follow-up

The 1-week delay traces directly to the PDF export scope change. Adding features
mid-sprint without adjusting timelines is a process failure, not an engineering failure.
The team absorbed the scope increase and still delivered only 1 week late, which
suggests strong execution — but the process that allowed uncontrolled scope expansion
needs a corrective action.

Q3: WERE THE METRICS RIGHT?

Adoption (34% vs 50% target):
- Measurable? YES — can be tracked via feature usage analytics
- Sensitive? YES — it moved (34%), though below target
- Right thing to measure? PARTIALLY — adoption tells us who tried it, but not
  why 66% didn't. Need to add a "feature awareness" metric (do users even know
  Quick Reports exists?) to distinguish discovery failure from rejection.
- Failure threshold? NOT DEFINED — at what adoption % would we have killed the feature?

Support tickets (down 60%):
- Measurable? YES — support system tracks this
- Sensitive? YES — clear movement
- Right thing to measure? YES — directly measures the problem we set out to solve
- Failure threshold? NOT DEFINED

NPS (6.2 → 7.1):
- Measurable? YES — survey-based
- Sensitive? MODERATE — 0.9 point increase is meaningful but NPS is a lagging indicator
- Right thing to measure? PARTIALLY — NPS reflects overall sentiment but may not
  isolate Quick Reports' contribution from other changes in the same period
- Failure threshold? NOT DEFINED

Metric quality rating: MEDIUM
Learning: We measured outcomes but not causes. The adoption miss would have been
more actionable if we'd also tracked feature awareness (did users see the feature?)
and activation (did users who saw it try it?). Also, none of our metrics had a
defined failure threshold — we should define "at what point do we stop investing"
before launch, not after.

Q4: WHAT WOULD WE DO DIFFERENTLY?

Process improvement 1:
  What happened:  PDF export was added mid-sprint without formal scope change approval.
                  This caused a 1-week delay and compressed testing time.
  What to change: Scope changes after sprint start require written sign-off from both
                  PM and engineering lead, with an explicit timeline impact assessment.
  How to apply:   On the next feature: any scope addition after sprint kickoff triggers
                  a "Scope Change Request" document (what, why, impact on timeline).
                  No code starts on new scope items without PM + eng lead signature.

Process improvement 2:
  What happened:  Adoption was 34% vs 50% target but we had no mechanism to understand
                  why users weren't adopting — was it awareness, UX friction, or rejection?
  What to change: Every feature launch must include a discovery/activation funnel alongside
                  outcome metrics. Track: saw feature → tried feature → retained feature.
  How to apply:   On the next feature: add funnel metrics to the spec alongside outcome
                  metrics. First sprint post-launch includes a funnel analysis checkpoint.

Process improvement 3:
  What happened:  No failure thresholds were defined for any metric.
  What to change: Every success metric in a spec must have a corresponding failure threshold.
                  "What number means we stop investing?"
  How to apply:   On the next feature: spec template requires a "Failure threshold" field
                  for each success metric. No spec enters sprint planning without it.

FOLLOW-ON ACTIONS (from retro findings)
1. Investigate adoption gap: run user research on why 66% of target users haven't adopted — [PM] — Due: 2026-04-02
2. Add feature awareness tracking to Quick Reports analytics — [Engineering] — Due: 2026-04-09
3. Define failure thresholds retroactively for Quick Reports metrics — [PM] — Due: 2026-03-26
4. Update spec template to require failure thresholds — [PM] — Due: 2026-03-26
5. Create Scope Change Request template and add to sprint process docs — [PM + Eng Lead] — Due: 2026-04-02

PRODUCT.LOCAL.MD UPDATES RECOMMENDED
- Add quality rule: "Every spec must define a failure threshold for each success metric before entering sprint planning."
- Add quality rule: "Scope changes after sprint start require PM + eng lead written sign-off with timeline impact assessment."
- Add quality rule: "Feature launches must include discovery/activation funnel metrics alongside outcome metrics."
================================================================
