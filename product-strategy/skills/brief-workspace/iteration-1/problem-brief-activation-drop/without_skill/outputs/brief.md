# Problem Brief: Onboarding Activation Drop — First Project Creation

## Problem Statement

User activation has dropped 40% in the onboarding flow. New signups are completing registration successfully but are not progressing to create their first project — the key activation milestone. This represents a critical breakdown in the registration-to-value pipeline.

## Impact

- **Activation rate decline**: 40% fewer users reaching first-project creation compared to the prior baseline period
- **Revenue risk**: Users who never activate have near-zero retention at Day 7 and Day 30, directly impacting conversion to paid plans and lifetime value
- **Acquisition waste**: Marketing spend to acquire these signups is lost if they never reach the product's core value proposition
- **Estimated impact**: If monthly signups are ~10,000, approximately 4,000 additional users per month are failing to activate, representing significant lost revenue potential

## Context

### What We Know
- Registration completion rates remain stable — the drop is isolated to the post-registration, pre-activation segment
- The 40% decline suggests either a sudden change (deployment, UI change, external factor) or a gradual trend that crossed a detection threshold
- "First project creation" is the defined activation event — it is the first moment users experience the product's core value

### What We Don't Know
- **When exactly the drop began** — need to correlate with deployment timelines, A/B tests, or product changes
- **Which user segments are most affected** — is this uniform across all cohorts (geo, acquisition channel, plan type) or concentrated?
- **Where in the post-registration flow users are dropping off** — are they reaching the project creation screen and abandoning, or never navigating there?
- **Whether the registration flow itself changed** — a change that attracts different user intent could explain lower activation without a product bug
- **Qualitative reasons** — we have no user feedback or session data explaining *why* users stop

## Hypotheses

### H1: Post-Registration UX Friction
A recent change to the onboarding flow (new steps, changed navigation, broken CTA) is preventing or discouraging users from reaching project creation.

**Evidence needed**: Compare onboarding funnel step-by-step conversion rates before and after the drop. Check deployment logs for UI changes in the relevant timeframe.

### H2: Empty State / Value Gap
Users land in an empty dashboard after registration and don't understand what to do next or why they should create a project. The path to value is unclear.

**Evidence needed**: Session recordings of new users post-registration. Heatmaps on the dashboard/home screen. Time-on-page data for the first screen after registration.

### H3: Technical Blocker
A bug, performance regression, or error in the project creation flow is silently failing or frustrating users.

**Evidence needed**: Error logs and 4xx/5xx rates on project creation endpoints. Client-side error tracking. Load time metrics for the project creation page.

### H4: Audience Shift
A change in acquisition channels or campaigns is bringing in users with different intent who were never likely to activate (e.g., content marketing attracting researchers, not doers).

**Evidence needed**: Activation rates segmented by acquisition channel. Compare channel mix before and after the drop. Survey or intent data from recent signups.

### H5: Onboarding Email / Nudge Failure
Automated onboarding emails or in-app nudges that previously guided users to first project creation are broken, suppressed, or landing in spam.

**Evidence needed**: Email delivery and open rates for onboarding sequences. In-app tooltip/guide impression and click-through data.

## Out of Scope

- Retention beyond activation (Day 7, Day 30 loops) — separate initiative
- Registration flow conversion optimization — registration rates are stable
- Pricing or plan structure changes
- Long-term onboarding redesign — this brief is about diagnosing and fixing the current drop

## Proposed Investigation Plan

| Step | Action | Owner | Due |
|------|--------|-------|-----|
| 1 | Pull activation funnel data segmented by week, channel, and cohort for the last 90 days | Analytics | [TBD — assign owner, target 2 business days] |
| 2 | Audit deployment log for all changes to onboarding and project creation flows in the timeframe of the drop | Engineering | [TBD — assign owner, target 2 business days] |
| 3 | Check project creation endpoint error rates, latency, and client-side errors | Engineering | [TBD — assign owner, target 1 business day] |
| 4 | Review onboarding email delivery, open, and click-through rates | Growth / Marketing | [TBD — assign owner, target 2 business days] |
| 5 | Pull 20 session recordings of users who registered but did not create a project in the last 2 weeks | Product / UX Research | [TBD — assign owner, target 3 business days] |
| 6 | Reconvene with findings to validate or eliminate hypotheses | Product Lead | [TBD — target 1 week from kickoff] |

## Success Criteria

- Root cause identified and validated with data
- Activation rate returns to within 10% of the pre-drop baseline within 30 days of fix deployment
- Monitoring alert configured to detect future activation drops of >15% within a 7-day window

## Open Questions

| Question | Owner | Due |
|----------|-------|-----|
| When exactly did the 40% drop begin — was it a step change or gradual decline? | Analytics | [TBD] |
| Were any A/B tests running on the onboarding flow during the affected period? | Product | [TBD] |
| Has the definition or instrumentation of "first project created" event changed recently? | Engineering | [TBD] |
| Are there segments (e.g., mobile vs desktop, geo, plan type) where activation is stable? | Analytics | [TBD] |
| Do we have qualitative data (support tickets, NPS comments) mentioning onboarding friction? | Support / CX | [TBD] |

## Recommended Next Step

**Immediate**: Schedule a 30-minute triage meeting with Product, Engineering, Analytics, and Growth to assign owners to the investigation steps above and set firm due dates. The 40% magnitude warrants treating this as a P1 investigation — every week of delay compounds the activation loss.

---

*This brief requires human review before use in business decisions. All figures are based on the reported 40% drop; underlying data should be independently verified. Estimates are labeled as such.*
