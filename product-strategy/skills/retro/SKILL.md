---
name: retro
description: >
  Activate for: retrospective, retro, post-mortem, post launch review,
  feature review, what went well, what didn't go well, lessons learned,
  sprint retrospective, product review, launch review, did it work,
  measure impact, feature retrospective, post-ship review, outcome review,
  product retro, evaluate feature success.
  NOT for: metrics dashboards (use official /metrics-review), stakeholder
  updates (use official /stakeholder-update), sprint planning
  (use official /sprint-planning).
license: Apache-2.0
argument-hint: "<feature name> retrospective"
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/retro"
---

## CONTEXT LOADING

Before running a retro, load `product.local.md` for product context,
quality standards, and PM process standards. If not configured, ask the
user for product context and the feature being reviewed.

## RETROSPECTIVE WORKFLOW

### The Four Retro Questions

A useful product retro answers exactly four questions:

  Q1: DID IT SOLVE THE PROBLEM?
    Was the PM right about the user need?
    Did the feature change what it was supposed to change?

  Q2: DID WE BUILD IT AS INTENDED?
    Was the spec good enough? Did engineering deliver what was specified?
    Were there scope changes, quality issues, or delivery delays?

  Q3: WERE THE METRICS RIGHT?
    Were the success metrics we defined measuring the right things?
    Did we have a failure threshold, and were we honest about it?

  Q4: WHAT WOULD WE DO DIFFERENTLY?
    Not "what went wrong" -- but "what specific process change would
    we make if we started this feature again today?"

### Data Required Before Running a Retro

OUTCOME DATA (4-12 weeks post-launch):
  - Adoption: % of target users who have used the feature at least once
  - Engagement: how often? for how long? (if applicable)
  - Support impact: did support tickets about this area increase or decrease?
  - NPS impact: has there been movement in relevant NPS questions?
  - Business metric: did the primary success metric move?

DELIVERY DATA:
  - On time or late? If late: by how long?
  - Were there scope changes during development? What was added or cut?
  - Were there significant spec ambiguity issues flagged by engineering?

TEAM DATA (optional but valuable):
  - Did engineering flag any spec quality issues?
  - Did design flag any requirement gaps during design review?
  - Did CS/Support flag anything unexpected post-launch?

### Retro Output Format

```
PRODUCT RETROSPECTIVE: [Feature name]
Shipped: [Date] | Retro date: [Date] | PM: [Name]
================================================================

Q1: DID IT SOLVE THE PROBLEM?

Original problem:   [From the spec -- what were we trying to solve?]
Target outcome:     [From the spec -- what did we say success looked like?]

Evidence:
[PASS/WARN/FAIL] [Metric]: [actual result] vs. [target]
[PASS/WARN/FAIL] [Metric]: [actual result] vs. [target]

Verdict: [SOLVED / PARTIALLY SOLVED / NOT SOLVED / TOO EARLY TO TELL]
Summary: [2-3 sentences: what the data shows about whether the
          feature delivered on its intent]

Q2: DID WE BUILD IT AS INTENDED?

[PASS/WARN/FAIL] Delivered on time: [On time / [N] weeks late -- reason]
[PASS/WARN/FAIL] Spec quality:     [No major ambiguity / [Issue reported]]
[PASS/WARN/FAIL] Scope maintained: [No changes / Changes: describe]
[PASS/WARN/FAIL] Quality (bugs):   [Bug rate in first 30 days]
[PASS/WARN/FAIL] ACs met:          [All ACs verified / Outstanding: list]

Q3: WERE THE METRICS RIGHT?

For each success metric defined in the spec/PRD:
- Was it measurable? (Could we actually get the data?)
- Was it sensitive? (Did it move in response to the feature?)
- Was it the right thing to measure? (Did it reflect user value?)
- Did we have a failure threshold? Did we use it?

Metric quality rating: [HIGH / MEDIUM / LOW]
Learning: [What we should measure differently next time]

Q4: WHAT WOULD WE DO DIFFERENTLY?

Process improvement [N]:
  What happened:  [Specific -- not "better communication"]
  What to change: [Specific rule or step to add/change]
  How to apply:   [On the next feature: [specific action]]

FOLLOW-ON ACTIONS (from retro findings)
[N]. [Action] -- [Owner] -- [Due date]

PRODUCT.LOCAL.MD UPDATES RECOMMENDED
[Any quality rules to add to the configuration based on this retro]
================================================================
```

### Process Improvement Format

Rule: Every "what went wrong" must be converted into a specific,
testable process change -- not a vague intention.

  WEAK:  "Write better specs"
  STRONG: "Every AC must be independently testable.
           If an AC contains 'and', split it before REVIEW status."

  WEAK:  "Communicate better with engineering"
  STRONG: "Engineering lead must confirm architecture notes in PRD
           before the PRD moves to REVIEW status."

  WEAK:  "Define success metrics earlier"
  STRONG: "Primary metric and failure threshold must be in the spec
           before it enters sprint planning. No spec without metrics."

## COMPLEMENTARY WORKFLOWS

This skill handles product retrospectives. For related PM workflows:
- Reviewing metrics that inform the retro: use official `/metrics-review`
- Communicating retro findings to stakeholders: use official `/stakeholder-update`
- Updating the roadmap based on retro learnings: use official `/roadmap-update`

## NEVER DO THESE

- NEVER run a retro without outcome data -- opinions without data
  produce blame, not learning
- NEVER produce a retro that only documents what went wrong --
  what went well is equally important (protect what works)
- NEVER produce a vague process improvement ("communicate better")
  -- convert every improvement into a specific, enforceable rule
- NEVER skip the metrics quality section -- bad metrics are as
  dangerous as no metrics; they create false confidence
- NEVER close a retro without at least one product.local.md
  update -- if nothing changes, the retro was a waste of time

ALL OUTPUTS REQUIRE REVIEW BY THE PM AND ENGINEERING LEAD.
