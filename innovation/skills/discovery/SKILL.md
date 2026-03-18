---
name: discovery
description: >
  Activate for: customer discovery, user research, interview, empathy,
  jobs to be done, JTBD, persona, pain point, customer insight, discovery,
  interview guide, synthesis, insight map, interview notes, customer quotes,
  what do customers want, what problems do customers have, user needs,
  customer feedback, research synthesis, discovery sprint, problem validation,
  HMW problem statement, how might we, empathy map, journey map.
  NOT for: idea generation (use idea), assumption mapping (use hypothesis),
  pilot results analysis (use validate).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/discovery"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, problem_statement, target_customer
- customer_profiles: all persona entries with JTBD, pains, gains, WTP
- key_assumptions: customer and problem assumptions

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: This is your focus stage. Customer discovery is exactly right.
- DISCOVERY: This is your focus stage. Deep customer research is the priority.
- VALIDATION: Discovery is still valuable -- you may be validating problem assumptions or discovering new segments.
- MVP: Discovery remains useful -- understanding adoption behaviour from early customers.
- GROWTH: Discovery is ongoing -- understanding churn reasons, new segments, expansion needs.

## DLA PROGRESSION CHECK

No skip warning needed -- discovery is foundational to all stages.
If venture.stage is beyond DISCOVERY and no customer_profiles exist in innov.local.md:
"You have progressed past discovery without documented customer profiles.
Consider running customer discovery now to validate the assumptions
your current work is built on."

## CUSTOMER DISCOVERY WORKFLOW

### Discovery Task Types

TYPE 1: INTERVIEW GUIDE GENERATION
  Purpose: Generate a structured interview guide for customer discovery.
  Input: Product/problem area; target customer; stage (problem vs. solution discovery)
  Output: Full interview guide with protocol notes, question banks, and probing guides

TYPE 2: OUTREACH AND SCREENING
  Purpose: Generate outreach messages and screening surveys to recruit interviews.
  Input: Target customer profile; channel (LinkedIn / email / in-person)
  Output: Outreach message (< 100 words); screening survey (5 questions); booking message

TYPE 3: INTERVIEW SYNTHESIS
  Purpose: Synthesise raw interview notes into structured insight output.
  Input: Raw notes from N interviews (any format)
  Output: JTBD map, pain ranking matrix, insight statements, quotes, learning gaps

TYPE 4: PROBLEM STATEMENT GENERATION
  Purpose: Convert synthesis insights into testable HMW problem statements.
  Input: Synthesis output + any constraints
  Output: 5 HMW variants + recommended primary + rationale

TYPE 5: PERSONA DEVELOPMENT
  Purpose: Build structured customer personas from discovery data.
  Input: Synthesis output; number of distinct segments identified
  Output: Persona cards for each segment with JTBD, pains, gains, WTP, buying process

### Interview Guide Output Structure

```
CUSTOMER DISCOVERY INTERVIEW GUIDE
Product area: [Area] | Target: [Customer] | Duration: [N] min
================================================================
INTERVIEW PROTOCOL NOTES:
  [Ground rules for the interviewer -- tone, what to listen for, what to avoid]

OPENING ([N] min)
  [Rapport-building questions -- role, context, day-to-day]

CURRENT PROCESS -- THE JOB ([N] min)
  [Walk-through questions -- how do they do X today? Step by step.]
  [Focus: observe the process, not opinions about the process]

PAIN POINTS -- THE FRUSTRATION ([N] min)
  [Frustration probe questions]
  [Workaround questions -- what do they do when it fails?]
  [Quantification questions -- how much time/money/stress?]

WORKAROUNDS AND CURRENT SPEND ([N] min)
  [What have they tried? What do they pay for adjacent solutions?]
  [Magic wand question: if you could fix one thing...]

PRIORITISATION ([N] min)
  [Which pain costs the most? What would a solution be worth?]

CLOSING
  [Referral request; open question; thank and close]
================================================================

INTERVIEW STYLE RULES:
  Listen 80%; talk 20%
  Never mention your product or solution concept during problem discovery
  When they say something interesting: "tell me more about that"
  When they describe a pain: "what do you do when that happens?"
  When they name a solution: "why that one? what does it not do?"
  Never ask: "Would you use a product that...?"
  Never ask: "Do you think X is a problem?" (leading)
  Never validate your hypothesis in the question
```

### Synthesis Output Structure

```
CUSTOMER DISCOVERY SYNTHESIS
Interviews: [N] | Segment: [Description] | Date: [Date]
================================================================
JOBS-TO-BE-DONE MAP:

  FUNCTIONAL JOBS (what they are literally trying to accomplish):
  - [Job 1] -- mentioned by [N/N] interviewees
  - [Job 2]

  RELATED JOBS (adjacent tasks they get pulled into):
  - [Related job] -- [N/N interviewees]

  EMOTIONAL JOBS (how they want to feel; what they want to avoid):
  - [Emotional job] -- [N/N interviewees]

  SOCIAL JOBS (how they want to be perceived):
  - [Social job] -- [N/N interviewees]

PAIN RANKING (frequency x severity):

  RANK 1: [Pain name] ([N/N] interviews; severity: HIGH [N/N])
  Current state: [What is actually happening today -- specific]
  Cost: [Time / money / stress quantified where possible]

  RANK 2-3: [Continue]
  RANK 4-5: [Continue]

INSIGHT STATEMENTS (3 minimum):
  "We discovered that [non-obvious finding about this customer]."
  [Each insight should be non-obvious -- not "customers want it to be faster"]

VIVID QUOTES:
  "[Direct customer quote that makes the pain real]" -- [Role], [Company type]

WHAT WE STILL NEED TO LEARN:
  1. [Specific unknown that could affect direction]
  2. [Specific unknown]
================================================================
```

### "How Might We" Generation Rules

Each HMW variant should approach the problem through a different lens:
  -- Solution lens (what the product does)
  -- Outcome lens (what the customer achieves)
  -- Emotional lens (how the customer feels)
  -- Constraint lens (the workaround they already use -- work with it)
  -- Systemic lens (the root cause, not the symptom)

A strong HMW:
  - Specific enough to focus ideation
  - Open enough not to prescribe the solution
  - Grounded in discovery data (references a real insight)

### Insight Statement Quality Test

A strong insight statement is:
  - NON-OBVIOUS -- something you would not have known without discovery
  - SPECIFIC -- names the customer segment and context
  - ACTIONABLE -- implies a direction for ideation or design
  - EVIDENCE-BASED -- references the number of interviews that support it

  WEAK: "Customers want the process to be faster."
  STRONG: "We discovered that the bottleneck is not processing speed but
  approval authority -- invoices sit for 3-7 days waiting for a manager
  who is unreachable, not for a system that is slow."

## ASSUMPTION TRACKING

After any discovery output that surfaces new information:
- Identify which assumptions in innov.local.md are affected by new evidence
- Propose assumption status updates (UNTESTED -> ANECDOTAL if interview-based)
- Surface the most critical untested assumption remaining
- Always distinguish between ASSUMED, ANECDOTAL, and VALIDATED evidence

## NEVER DO THESE

- NEVER include your solution concept in an interview guide --
  problem discovery and solution validation are separate phases
- NEVER use closed yes/no questions in a discovery interview --
  they produce agreement bias, not insight
- NEVER present fewer than 3 insight statements -- one insight is a
  data point; three is a pattern; below three is insufficient synthesis
- NEVER produce a synthesis from fewer than 5 interviews without
  flagging that the sample is insufficient for reliable pattern detection
  (5 is minimum; 8-12 is recommended for initial discovery)
- NEVER call a pain "validated" because multiple people mentioned it --
  validation requires willingness to pay, not just acknowledgement of pain

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
