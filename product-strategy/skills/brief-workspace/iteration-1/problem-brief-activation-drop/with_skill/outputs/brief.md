TASK:          Problem Brief -- Onboarding Activation Drop
FEATURE/AREA:  Onboarding / First Project Creation
CONFIGURATION: Not configured (product.local.md not found)
AUDIENCE:      PM / Engineering / Design
VERSION:       Draft

---

Product Brief: Onboarding Activation Drop -- First Project Creation
Type:          Problem Brief
Date:          2026-03-19
Author:        [PM -- to be assigned]
Team:          Product, Engineering (Onboarding Squad), Design, Data/Analytics

## THE PROBLEM

New users complete registration successfully but 40% fewer are creating their first project compared to the prior baseline. The activation funnel is breaking between account creation and the moment of first value -- users sign up, land in the product, and then leave without taking the core action that defines an activated user. This means the product is acquiring users it cannot retain.

## WHO IS AFFECTED

- **New Signups** -- all users who complete registration and enter the product for the first time. This spans all acquisition channels (organic, paid, referral) and all plan tiers.
- **Volume**: the 40% drop applies to the full new-signup cohort. If baseline activation was, for example, 60%, it has fallen to ~36%, meaning roughly 1 in 3 new signups who would previously have activated are now churning before first value.
- **Segment note**: it is not yet confirmed whether the drop is uniform across segments or concentrated in specific channels, plan types, or geographies. This is a critical gap (see below).

## EVIDENCE

- **Activation metric decline**: 40% relative drop in "first project created" rate among new signups. *(Source: product analytics -- exact dashboard and date range to be cited by data team.)*
- **Funnel data** (estimated): registration completion rate remains stable, indicating the drop is post-registration, not a sign-up form issue.
- **Assumption**: no major changes to the registration flow itself during the affected period. If there were changes (new fields, verification steps, onboarding redesign), these must be surfaced immediately as candidate causes.
- **Support signal**: [DATA GAP -- support ticket volume related to onboarding should be pulled and trended for the same period.]
- **Session data**: [DATA GAP -- average time-on-page and drop-off screen for new users in their first session should be analyzed.]

## IMPACT OF NOT SOLVING

- **Revenue**: every unactivated user is a lost conversion opportunity. At current signup volumes, a 40% activation drop translates directly into reduced trial-to-paid conversion downstream, compressing revenue growth.
- **CAC efficiency**: customer acquisition cost remains constant while the yield per acquired user drops -- effective CAC per activated user has increased by ~67% (1/0.6 vs 1/1.0 relative).
- **Retention cliff**: users who never create a first project have near-zero day-7 and day-30 retention. The longer this persists, the more the active user base stagnates despite continued top-of-funnel growth.
- **Competitive risk**: if users sign up and fail to activate, they are likely evaluating alternatives. Each unactivated user is a warm lead handed to competitors.
- **Team morale and trust**: sustained activation decline erodes confidence in growth investments and can trigger reactive feature churn rather than disciplined discovery.

## WHAT WE DO NOT KNOW YET

1. **When did the drop begin?** We need the exact cohort date range to correlate with product changes, marketing mix shifts, or external events.
2. **Is the drop uniform across segments?** Channel (organic vs. paid vs. referral), plan tier, geography, device type -- are all segments affected equally, or is this driven by a specific cohort?
3. **Where exactly do users drop off?** After registration, do they reach the dashboard? Do they start a project and abandon? Do they never click "create project"? The specific screen-level drop-off point is unknown.
4. **Were there product or infrastructure changes?** New onboarding flow, UI changes, broken flows, performance regressions, or third-party integration failures during the affected period.
5. **What do users experience qualitatively?** We have no qualitative data (session recordings, user interviews, support verbatim) explaining why users are not creating their first project.
6. **Has the user mix changed?** If marketing shifted spend toward a channel that brings lower-intent users, the drop may reflect audience quality, not product friction.

## HYPOTHESIS

We believe that a friction point introduced between registration completion and first project creation -- whether a UX change, a missing prompt, a confusing empty state, or a performance issue -- is preventing new users from reaching their first moment of value. We will know this is true when we identify the specific drop-off point in the post-registration funnel and can correlate it with a product or environment change that occurred at the onset of the decline.

## DISCOVERY QUESTIONS

1. **At which exact step in the post-registration flow do new users drop off?** (Requires: funnel analysis from registration → dashboard → create project → project created, broken by cohort week.)
2. **Does the activation drop correlate with a specific product change, deploy, or A/B test?** (Requires: cross-referencing the decline start date with the engineering changelog and experiment log.)
3. **Is the drop concentrated in a specific user segment, channel, or device type?** (Requires: segmented activation analysis across acquisition source, plan tier, geography, and device.)
4. **What do new users see and do in their first session?** (Requires: session replay review of 20+ recent new-user sessions and qualitative analysis of behavior patterns.)
5. **What do unactivated users say when asked why they didn't continue?** (Requires: intercept survey or outbound interview with 5-10 users who registered in the last 14 days but never created a project.)

## NEXT STEP

**Decision needed**: Approve a 1-week discovery sprint to answer the five questions above. The data team should begin segmented funnel analysis immediately (questions 1-3) while design recruits for qualitative research (questions 4-5). A discovery readout is targeted for end of sprint, with a go/no-go on solution scoping.

---

*This brief contains no solution proposals by design. Solutions should follow discovery, not precede it.*

*ALL OUTPUTS REQUIRE REVIEW BY THE PM BEFORE DISTRIBUTION TO STAKEHOLDERS.*
