---
name: validate
description: >
  Activate for: validate, build measure learn, BML, pivot, persevere, pilot
  results, what did we learn, experiment results, assumption test results,
  was I right, did it work, should I pivot, what should I change, learning
  synthesis, validated learning, invalidated assumption, pilot analysis,
  what our pilot taught us, early customer data, what customers told us,
  post-pilot analysis, pivot or continue, kill or continue.
  NOT for: assumption mapping (use hypothesis), idea generation (use idea),
  sprint planning (use sprint).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/validate"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, problem_statement
- key_assumptions: all entries with IDs, risk levels, evidence, test status
- sprint_log: previous sprint results and learnings
- customer_profiles: personas, pains
- financial_model: current_state (for impact assessment)

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: N/A -- validation requires something to validate. Consider running /discovery or /hypothesis first.
- DISCOVERY: Validation is appropriate for discovery-stage assumptions -- did the problem exist as hypothesised?
- VALIDATION: This is your focus stage. Full BML analysis and pivot decisions are the priority.
- MVP: This is your focus stage. Pilot results analysis and assumption updates are critical.
- GROWTH: Validation remains important for new features and expansion hypotheses.

## DLA PROGRESSION CHECK

If no key_assumptions exist in innov.local.md or all are UNTESTED:
"You are trying to validate without an assumption map. Validation
requires knowing what you were testing and what success/failure looks like.
Consider running /hypothesis first to build your assumption map."

## BUILD-MEASURE-LEARN WORKFLOW

### Task Types

TYPE 1: BUILD-MEASURE-LEARN ANALYSIS
Input: What was tested; pilot results (metrics, adoption, customer feedback)
Output: Validated/invalidated assumptions; unexpected learnings;
pivot/persevere recommendation; V1 priorities

TYPE 2: PIVOT DECISION FRAMEWORK
Input: Invalidated assumption(s); what is still true
Output: 5 pivot directions; pivot recommendation with rationale

TYPE 3: LEARNING SYNTHESIS
Input: Raw pilot data; customer interviews; usage metrics; NPS/feedback
Output: Pattern map; assumption updates; open questions; next sprint priority

TYPE 4: ASSUMPTION STATUS UPDATE
Input: New data from any source (pilot; interview; market research)
Output: Specific assumption updates for innov.local.md

### BML Analysis Output Structure

```
BUILD-MEASURE-LEARN ANALYSIS
Sprint/Pilot: [N] | Period: [Start]-[End] | Date: [Date]
================================================================
WHAT WE TESTED:
  Learning goal: [Assumption(s) targeted]
  Method:        [How we tested -- pilot / survey / interview / experiment]
  Sample:        [N customers / N users / N transactions]

WHAT WE MEASURED:
  [Metric 1]: [Result] vs. [Success criterion] -- [PASS / FAIL / PARTIAL]
  [Metric 2]: [Result] vs. [Success criterion] -- [PASS / FAIL / PARTIAL]
  [Metric 3]: [Result] vs. [Success criterion] -- [PASS / FAIL / PARTIAL]

ASSUMPTION OUTCOMES:
  A-00X ([Assumption]): VALIDATED / INVALIDATED / INCONCLUSIVE
  Evidence: [Specific -- "3 of 3 pilots signed at $X" not "customers liked it"]
  Confidence: [HIGH / MEDIUM / LOW -- based on sample size and data quality]

  [Repeat for each assumption that was tested or affected]

UNEXPECTED LEARNINGS:
  [Things you discovered that you were not looking for]
  [New assumptions revealed by the pilot]
  [Customer behaviour that surprised you]
  Implication: [What each unexpected learning means for direction]

PIVOT OR PERSEVERE RECOMMENDATION:
  [PERSEVERE / PIVOT ON SPECIFIC ELEMENT / FULL PIVOT]
  Rationale: [Why -- based on the evidence, not on attachment to the idea]
  If PERSEVERE: [What is the next most critical assumption to test?]
  If PIVOT: [On what specifically -- see pivot framework below]

innov.local.md UPDATES PROPOSED:
  [Specific changes to assumption status, canvas blocks, personas, financials]
================================================================
```

### Pivot Types (from Lean Startup methodology)

ZOOM-IN PIVOT: One feature becomes the whole product.
ZOOM-OUT PIVOT: The whole product becomes one feature of a larger product.
CUSTOMER SEGMENT PIVOT: Same product; different customer.
CUSTOMER NEED PIVOT: Same customer; different problem.
PLATFORM PIVOT: Application becomes a platform (or vice versa).
BUSINESS ARCHITECTURE PIVOT: High-margin/low-volume to low-margin/high-volume.
TECHNOLOGY PIVOT: Same positioning; different technology.
CHANNEL PIVOT: Same product; different distribution channel.

### Evidence Quality Standard

VALIDATED means: customers paid for it OR used it N times per week for N weeks.
Not: "They said they would use it" (interest != behaviour)
Not: "They signed up for the waitlist" (intent != payment)
Not: "They said it was great" (enthusiasm != value)

Evidence hierarchy (most to least reliable):

1. Customer paid AND renewed (revealed preference over time)
2. Customer paid once (revealed preference at a moment)
3. Customer signed a letter of intent with specific terms
4. Customer used the product N times without prompting
5. Customer said they would pay [specific amount] in an interview
6. Customer said the problem is real and painful
7. Multiple people described the same problem

### Pivot Decision Checklist

Before recommending a pivot:

- Have you run at least 2 iterations of the current approach?
- Is the invalidation based on behaviour (what customers did) or
  opinions (what they said)?
- Is the team emotionally ready for a pivot?
- What is still true -- what learning is preserved into the pivot?

## ASSUMPTION TRACKING

After any validation output:

- Update all affected assumption statuses with specific evidence
- Propose innov.local.md updates for assumptions, canvas, financials, personas
- Surface the next most critical untested assumption
- Always distinguish between ASSUMED, ANECDOTAL, and VALIDATED evidence

## NEVER DO THESE

- NEVER call a "no results" inconclusive -- if you ran the test correctly
  and customers did not engage, that IS a result: treat it as INVALIDATED
- NEVER pivot based on one customer's feedback -- one customer is a
  data point; a pattern across 3+ customers is signal
- NEVER persevere past 3 iterations of the same invalidated assumption
- NEVER update innov.local.md assumption status to VALIDATED without
  specific evidence (N customers, $X paid, N% retention)

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
