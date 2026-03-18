---
name: prioritise
description: >
  Activate for: prioritise, prioritization, backlog prioritisation, backlog
  order, what to build first, RICE, ICE, MoSCoW, Kano, value vs effort,
  impact vs effort, backlog ranking, roadmap prioritisation, compare features,
  what is most important, which feature, product decision, build order,
  quarterly priorities, should we build this, feature value, rank backlog.
  NOT for: roadmap planning (use official /roadmap-update), sprint planning
  (use official /sprint-planning), metrics review (use official /metrics-review).
license: Apache-2.0
argument-hint: "<backlog items or feature list>"
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/prioritise"
---

## CONTEXT LOADING

Before prioritising, load `product.local.md` for product context,
current themes, and engineering capacity. If not configured, ask the user
for product context and current strategic priorities.

## PRIORITISATION WORKFLOW

### Framework Selection

Ask: what is the primary prioritisation challenge?

"We have too many features and need to rank them"
-> Use RICE (reach, impact, confidence, effort)

"We need a quick 2x2 without complex scoring"
-> Use Value vs. Effort matrix

"We need to sort a large backlog by customer demand vs. complexity"
-> Use Kano model (basic needs / performance needs / delighters)

"We need to communicate to stakeholders what is MUST vs. SHOULD vs. COULD"
-> Use MoSCoW

"We need to evaluate a single feature request -- yes or no"
-> Use the single-feature evaluation framework

### RICE Framework

RICE Score = (Reach x Impact x Confidence) / Effort

Reach: % of active users/accounts that will use this
in the first 3 months after launch
[0-100%]

Impact: How much will this improve the experience for
those who use it?
1 = minimal | 2 = moderate | 3 = significant
(be conservative -- overestimating is common)

Confidence: How confident are you in the Reach and Impact estimates?
High = 80-100% | Medium = 50-80% | Low = 25-50%
[use the lower number if you have less data]

Effort: How much engineering time does this require?
Express in person-sprints (1 sprint = ~2 weeks x 1 engineer)

RICE OUTPUT FORMAT:
| Item | Reach | Impact | Confidence | Effort | RICE | Rank |
|---|---|---|---|---|---|---|
| [Item] | [X]% | [1/2/3] | [X]% | [N sprints] | [Score] | [N] |

IMPORTANT: Show all assumptions. RICE scores are only as good as
the estimates behind them. A score from bad data is worse than
no score -- it creates false precision.

### The Three Mandatory Challenges (run after any framework)

CHALLENGE 1: STRATEGIC OVERRIDE TEST
Is there any item that scored low that you would build anyway?
If yes: write the override reason explicitly.
Hidden strategic overrides are where backlogs go wrong.
Common override reasons: CEO commitment / competitive necessity /
technical prerequisite / enterprise deal dependency.
None of these are wrong -- but they must be documented as overrides,
not buried in a score.

CHALLENGE 2: DATA GAP TEST
For each item with confidence below 50%:

- What would you need to know to raise confidence above 70%?
- Can you get that in a 2-week discovery spike?
- Should you do the spike before committing to the build?
  Rule: Low-confidence, high-effort items should almost always have
  a discovery spike before they enter a sprint.

CHALLENGE 3: "WHAT WOULD WE REGRET?" TEST
Ignore all scores. Ask: which item, if we shipped nothing else
this quarter, would our best customers be most grateful for?
Does it match the top scorer? If not: why the gap?
(The gap is usually a data quality issue in the scoring --
fix the data, not just override the score)

### Defining the Quarter Output

After running the framework and three challenges, produce:

```
QUARTERLY PRIORITY DECISION
================================================================
PRIORITY 1 (must ship):
  [Item] -- [One-sentence rationale]

PRIORITY 2 (ships if P1 goes well):
  [Item] -- [One-sentence rationale]

STRETCH GOAL (ships if capacity allows):
  [Item] -- [One-sentence rationale]

EXPLICITLY NOT BUILDING THIS QUARTER:
  [Item] -- [One-sentence rationale -- this is the most important entry]

STRATEGIC OVERRIDES DOCUMENTED:
  [Item] -- [Override reason -- why scoring was overridden]

DISCOVERY SPIKES RECOMMENDED:
  [Item] -- [What question the spike needs to answer]
================================================================
```

### Single Feature Evaluation

For a yes/no decision on one feature request:

```
FEATURE EVALUATION: [Feature name]
---------------------------------------------------------
Request source:      [Customer / internal / competitor pressure]
Frequency of request:[How often; from how many sources]
User problem:        [What problem does it solve?]
Alternative solutions:[Can this be solved another way?]
Effort:              [Rough estimate]
Opportunity cost:    [What does NOT get built if we build this?]
Confidence in value: [Low / Medium / High -- with basis]

RECOMMENDATION: [BUILD / DEFER / DECLINE / DISCOVERY SPIKE]
Rationale:       [2-3 sentences]
---------------------------------------------------------
```

## COMPLEMENTARY WORKFLOWS

This skill handles backlog prioritisation and framework scoring.
For related PM workflows:

- Roadmap planning with prioritised items: use official `/roadmap-update`
- Sprint planning from prioritised backlog: use official `/sprint-planning`
- Decomposing features into stories before prioritising: use `/stories` from this plugin
- Reviewing metrics to inform priorities: use official `/metrics-review`

## NEVER DO THESE

- NEVER produce a RICE output without showing the scoring assumptions --
  a score without assumptions is meaningless
- NEVER present a prioritisation as objective -- all frameworks involve
  judgment; make the judgment visible
- NEVER omit the "explicitly NOT building" list --
  it is as important as the build list
- NEVER skip the three challenges -- they catch the errors that
  framework scores reliably miss
- NEVER allow a low-confidence, high-effort item to enter a sprint
  without a discovery spike first

ALL OUTPUTS REQUIRE REVIEW BY THE PM AND STAKEHOLDERS BEFORE COMMITMENT.
