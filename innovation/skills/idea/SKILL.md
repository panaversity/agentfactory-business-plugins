---
name: idea
description: >
  Activate for: idea, brainstorm, ideate, 100 ideas, idea generation,
  idea sprint, new product idea, innovation sprint, what should I build,
  what problem should I solve, idea evaluation, idea scoring, idea shortlist,
  pressure test idea, devil's advocate, adjacent possible, contrarian ideas,
  analogy ideas, crazy ideas, how might we, HMW, pivot idea, new venture concept.
  NOT for: customer discovery or interview synthesis (use discovery),
  assumption mapping (use hypothesis), pitch deck (use pitch).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/idea"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, problem_statement, target_customer
- key_assumptions: all entries with IDs, risk levels, evidence, test status
- customer_profiles: personas, pains, gains

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: This is your focus stage. Full idea generation is appropriate.
- DISCOVERY: Idea generation is fine -- you may be refining direction after interviews.
- VALIDATION: Warning -- "You are past ideation. Your assumptions are being tested. Are you pivoting, or exploring adjacent ideas? If pivoting, use /validate first to synthesise what was invalidated."
- MVP: Warning -- "You are building. Generating new ideas mid-build risks distraction. Are you considering a pivot? If so, use /validate to assess your pilot results first."
- GROWTH: Warning -- "You are scaling what works. New ideas here should be adjacent optimisations, not new ventures. If you are genuinely exploring a new direction, that is a separate venture."

## DLA PROGRESSION CHECK

If venture.stage is IDEA and no discovery data exists in innov.local.md:
"You are generating ideas before talking to customers. Ideas without
customer evidence are guesses. Consider running /discovery first to
ground your ideation in real pain points."

## IDEA GENERATION WORKFLOW

### Idea Types

TYPE 1: 100-IDEA SPRINT
Purpose: Generate maximum idea volume on a problem statement.
Input: HMW problem statement + any constraints
Output: 100 ideas across 10 categories (10 per category)
Rule: No self-censorship -- generate all ideas including obvious and impossible

TYPE 2: SHORTLISTING
Purpose: Filter 100 ideas to actionable shortlist using DVF framework.
Input: Full idea list
Filter: Desirability (would customers pay?), Viability (path to $10M+ revenue?),
Feasibility (small team can build MVP in <3 months?)
Output: Top 10 with one-sentence rationale per idea

TYPE 3: SINGLE-IDEA PRESSURE TEST
Purpose: Stress-test one selected idea before committing to it.
Input: One idea description
Output: 5 strongest arguments against; what must be proven to overcome each

TYPE 4: PIVOT IDEATION
Purpose: Generate alternative directions after a failed assumption.
Input: What was invalidated; what we still know to be true
Output: 5-10 pivot directions with rationale; which to explore first

TYPE 5: ANALOGICAL IDEATION
Purpose: Apply successful models from other domains to your problem.
Input: Problem statement + industry context
Output: "What would [Company/Model] do with this problem?" x 10 analogies

### 100-Idea Sprint Output Structure

```
IDEA SPRINT -- [Problem Statement]
================================================================
PRODUCT IDEAS (how the product could work):
1. [One sentence -- specific enough to imagine building it]
2-10. [Continue]

BUSINESS MODEL IDEAS (how it could make money differently):
11-20. [One sentence each]

DISTRIBUTION IDEAS (how customers find and buy it):
21-30. [One sentence each]

ANALOGY IDEAS (what worked for similar problems elsewhere):
31-40. [One sentence -- reference the model it draws from]

TECHNOLOGY IDEAS (how new tech could change the solution):
41-50. [One sentence -- name the specific technology]

CRAZY / 10X IDEAS (what would 10x better look like?):
51-60. [Permission to be unrealistic -- suspend disbelief]

BORING IDEAS (the most obvious thing):
61-70. [What the incumbent would build; what anyone would think of first]

CONTRARIAN IDEAS (the exact opposite of obvious):
71-80. [What happens if we invert the conventional assumption?]

PARTNERSHIP IDEAS (who could solve this together?):
81-90. [Name the partner type + what they bring]

INCUMBENT IDEAS (what the market leader would do if they noticed):
91-100. [How the biggest player in the space would respond]
================================================================
```

### DVF Scoring Framework

For each idea in the shortlist:

DESIRABILITY: Would customers pay for this today?
HIGH: Clear willingness to pay; customer already spending on adjacent solution
MEDIUM: Pain is real but payment behaviour not established
LOW: Nice to have; customers tolerate the problem without urgency

VIABILITY: Could this become a $10M+ revenue business?
HIGH: Clear path to scale; large addressable market; strong unit economics
MEDIUM: Uncertain scale; niche market or unclear monetisation at volume
LOW: Too small a market; unit economics problematic at scale

FEASIBILITY: Can a small team build an MVP in <3 months?
HIGH: Core technology is available; team has or can access required skills
MEDIUM: 3-6 month MVP; one significant technical risk
LOW: Requires proprietary technology or hardware; > 6 months to test

### Idea Quality Rules

STRONG idea has:

- A specific customer (not "everyone" or "businesses")
- A specific pain (not "inefficiency" or "they want something better")
- A specific mechanism (not "AI-powered" -- what does the AI actually do?)
- A reason why now (what changed that makes this possible/necessary today?)
- A reason why you (what do you know, have, or can do that others cannot?)

WEAK idea has:

- Generic customer ("SMEs", "people", "anyone who...")
- Generic pain ("they want it to be easier/faster/cheaper")
- Technology-first ("AI chatbot for X" without a specific job-to-be-done)
- No timing reason (why hasn't someone done this already?)

### The "Why Now?" Test

Before shortlisting any idea, apply the "Why Now?" test:
What changed in the last 2-3 years that makes this possible or urgent today?

Valid "Why Now?" reasons:

- New technology (LLM capabilities; mobile penetration; API availability)
- Regulatory change (new requirement creates demand)
- Behaviour change (remote work; new platform adoption)
- Cost inflection (cloud; AI inference costs)
- Demographic shift (new generation in workforce)
- Market gap (incumbent exited; price increase)

If you cannot answer "Why Now?": the idea may be fine but timing is unclear.

## ASSUMPTION TRACKING

After any idea output that references or creates new assumptions:

- Surface the most critical untested assumption relevant to the selected idea
- Propose innov.local.md updates if new assumptions were identified
- Always distinguish between ASSUMED, ANECDOTAL, and VALIDATED evidence

## NEVER DO THESE

- NEVER stop at fewer than 100 ideas in a generation sprint --
  the best ideas are usually in the second half; early ideas are obvious
- NEVER score an idea HIGH on Desirability without evidence of
  customer willingness to pay (not just interest -- actual payment intent)
- NEVER proceed to building from idea selection without running
  /hypothesis to make assumptions explicit first
- NEVER generate a contrarian or crazy idea and immediately dismiss it --
  the point is to expand the solution space; evaluation comes later

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
