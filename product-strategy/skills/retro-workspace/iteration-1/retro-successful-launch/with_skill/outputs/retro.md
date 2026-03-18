PRODUCT RETROSPECTIVE: New Onboarding Flow
Shipped: On time | Retro date: 2026-03-19 | PM: [Unspecified]
================================================================

Q1: DID IT SOLVE THE PROBLEM?

Original problem:   Onboarding experience was causing friction, leading to drop-offs
                    and generating support tickets.
Target outcome:     60% adoption among target users, reduced onboarding support burden.

Evidence:
[PASS] Adoption: 72% actual vs. 60% target — exceeded goal by 12pp
[PASS] Support tickets: onboarding-related tickets dropped 45% — strong improvement

Verdict: SOLVED
Summary: The new onboarding flow exceeded its adoption target by 12 percentage points
and meaningfully reduced support burden. Both primary success metrics show clear positive
movement. This is a genuine success — the team correctly identified the problem, designed
an effective solution, and executed well. The question now is whether there are learnings
to extract that make the next feature this successful too.

Q2: DID WE BUILD IT AS INTENDED?

[PASS] Delivered on time: On time — no delays
[PASS] Spec quality:     No spec ambiguity issues reported by engineering
[PASS] Scope maintained: No scope changes during development
[PASS] Quality (bugs):   No bug data provided, but no quality concerns flagged
[PASS] ACs met:          All acceptance criteria met

This is a clean delivery. On time, no scope changes, ACs met. Worth documenting
WHY this went well so the process can be replicated:
- Spec was clear enough that engineering had no ambiguity questions
- Scope was locked — no mid-sprint additions
- The team "felt really good about this one" — team confidence is a leading
  indicator worth paying attention to

Q3: WERE THE METRICS RIGHT?

Adoption (72% vs 60% target):
- Measurable? YES — tracked via analytics
- Sensitive? YES — clearly moved above target
- Right thing to measure? YES — directly measures whether users are using the
  new flow
- Failure threshold? NOT SPECIFIED — but at 72% this is clearly above any
  reasonable threshold

Support tickets (down 45%):
- Measurable? YES — support system tracking
- Sensitive? YES — clear 45% reduction
- Right thing to measure? YES — directly measures whether the friction that
  generated support load has been reduced
- Failure threshold? NOT SPECIFIED

Metric quality rating: HIGH
Learning: Good metric selection — both metrics directly measure the problem and
the solution. For future features, consider adding a "time to value" metric (how
quickly new users complete onboarding) as a leading indicator alongside the
lagging adoption number. Also define failure thresholds upfront even for features
where success seems likely.

Q4: WHAT WOULD WE DO DIFFERENTLY?

Process improvement 1:
  What happened:  The spec was clean and engineering had no ambiguity issues.
                  This contributed directly to on-time delivery.
  What to change: Formalize what made this spec work. Was it the level of detail?
                  The engineering review before development started? The AC format?
  How to apply:   On the next feature: PM documents which spec practices were used
                  for this feature and adds them to the spec template as best practices.

Process improvement 2:
  What happened:  Scope was maintained throughout development — no mid-sprint additions.
  What to change: Understand why scope held here when it doesn't always. Was it because
                  the problem was well-understood? Because stakeholders were aligned? Because
                  the PM actively defended scope?
  How to apply:   On the next feature: PM documents scope defense strategy used and whether
                  any scope requests were received and deflected. This creates a playbook
                  for scope management.

Process improvement 3:
  What happened:  Team confidence was high ("felt really good about this one"). High team
                  confidence correlated with on-time delivery and quality output.
  What to change: Start tracking team confidence as a leading indicator. A pre-sprint
                  confidence check could surface risk early.
  How to apply:   On the next feature: add a "team confidence" question to sprint kickoff —
                  "On a scale of 1-5, how confident are you we'll deliver this on time and
                  at quality?" Track over time to see if it predicts outcomes.

FOLLOW-ON ACTIONS (from retro findings)
1. Document spec practices that worked — add to spec template — [PM] — Due: 2026-04-02
2. Document scope defense strategy used — add to process playbook — [PM] — Due: 2026-04-02
3. Add "time to value" metric tracking for onboarding flow — [Engineering] — Due: 2026-04-09
4. Pilot team confidence tracking at next sprint kickoff — [PM] — Due: next sprint

PRODUCT.LOCAL.MD UPDATES RECOMMENDED
- Add quality rule: "Successful delivery patterns should be documented in retros with the same rigor as failures — protecting what works is as important as fixing what doesn't."
- Add quality rule: "Every feature spec should define failure thresholds even when the team is confident — it's cheaper to define them before launch than to debate them after."
================================================================
