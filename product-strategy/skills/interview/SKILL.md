---
name: interview
description: >
  Activate for: user interview, interview guide, interview questions,
  discovery interview, research interview, customer interview, user research
  guide, interview script, how to interview users, what to ask users,
  interview protocol, research protocol, interview template, qualitative
  research, jobs to be done, JTBD, contextual inquiry, interview planning.
  NOT for: research synthesis from completed interviews (use official
  /synthesize-research), competitive analysis (use official /competitive-brief),
  survey design or quantitative research.
license: Apache-2.0
argument-hint: "<research topic> for <persona>"
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/interview"
---

## CONTEXT LOADING

Before generating an interview guide, load `product.local.md` for product
context, personas, and research configuration. If not configured, ask the
user for the research topic, target persona, and product context.

## INTERVIEW GUIDE WORKFLOW

### Interview Design Principles

PRINCIPLE 1: BEHAVIOR OVER OPINION
Ask what users DO, not what they THINK or WANT.
"Walk me through the last time you did X" > "How important is X to you?"
Behavior is evidence. Opinion is noise.

PRINCIPLE 2: PAST OVER HYPOTHETICAL
Ask about the past, not the future.
"Tell me about the last time you exported a report" >
"Would you use a bulk export feature?"
Users are terrible at predicting their future behavior.
They are excellent reporters of their past behavior.

PRINCIPLE 3: PROBLEM BEFORE SOLUTION
Do not mention your product, feature idea, or proposed solution
in the first half of the interview. Explore the problem space fully
before introducing any solution context.

PRINCIPLE 4: SILENCE IS DATA
When a user pauses or struggles to answer, do not fill the silence.
The pause is often the most revealing moment in the interview.

PRINCIPLE 5: "WHY" FIVE TIMES
When a user says something interesting: ask why. Then why again.
The surface answer is rarely the real answer.

### Interview Guide Structure (45-minute default)

SEGMENT 1: OPENING (5 minutes)
Purpose: build rapport; set expectations; get consent

Script:
"Thanks for taking the time to speak with me today. I'm [name],
a product manager at [company]. I'm here to learn from you --
there are no right or wrong answers. I'm interested in how
you work, not in testing you on our product. Is it okay if
I take notes / record this conversation? [Get consent]
Before we start -- any questions for me?"

SEGMENT 2: WARM-UP (5-10 minutes)
Purpose: understand who this person is and how they work

Questions (use 2-3):

- "Can you tell me a bit about your role and what a typical
  day looks like for you?"
- "How does [relevant area] fit into your day-to-day work?"
- "How long have you been in this role? Has the way you
  approach [area] changed over that time?"

SEGMENT 3: CORE DISCOVERY (20-25 minutes)
Purpose: understand the specific problem area in depth

Structure: one recent specific experience then depth questions

Opening:
"I'd like to understand how you currently [do the thing we're
researching]. Can you walk me through the last time you did this
-- as concretely as possible?"

Depth questions (follow the story):

- "What prompted you to do that?"
- "What happened next?"
- "What was difficult about that step?"
- "How do you handle [obstacle they mention]?"
- "How long does that typically take?"
- "What do you do when [edge case they describe] happens?"
- "If that step didn't exist, what would change for you?"

Workaround probe (always ask):
"Before we had [product feature / before you used our product],
how did you handle this? [Wait] And do you still use any part
of that workaround today?"

Frequency and importance probe:
"How often do you go through this process?
On a scale of [frustrating-fine], where does this sit for you?"

SEGMENT 4: WRAP-UP (5 minutes)
Purpose: catch anything missed; leave door open

- "Is there anything about [area] that we haven't talked about
  that you think would be important for me to understand?"
- "If you could change one thing about [area / current product
  experience], what would it be?"
- "Is there anyone else you think I should talk to who has a
  different perspective on this?"

Close:
"This has been really valuable. I may have some follow-up
questions as I synthesise everything -- would it be okay to
reach back out? Thank you so much for your time."

### Interview Guide Output Format

```
INTERVIEW GUIDE: [Study topic]
================================================================
Purpose:     [What question this research is trying to answer]
Participants:[Persona; company size; role; n= target]
Duration:    [30 / 45 / 60 minutes]
Interviewer: [Name]
Note-taker:  [Name or "interviewer only"]

[Full guide by segment -- see structure above]

NOTE-TAKING TEMPLATE (for each interview):
Participant: [ID -- not name in notes]
Date:        [Date]
Key observations:
- [Behavior observed]
Notable quotes:
- "[Quote]"
Surprises / unexpected:
- [Anything that challenged assumptions]
Follow-up questions:
- [Things to probe in subsequent interviews]
================================================================
```

## COMPLEMENTARY WORKFLOWS

This skill generates interview guides and note-taking templates.
For related PM workflows:

- Synthesising completed interview notes: use official `/synthesize-research`
- Framing the problem before interviews: use `/brief` from this plugin
- Competitive context for interviews: use official `/competitive-brief`

## NEVER DO THESE

- NEVER ask leading questions ("Would you find it useful if...")
- NEVER mention your feature idea or hypothesis before the
  problem space has been fully explored
- NEVER ask hypothetical future questions ("Would you use...")
  as the primary evidence -- use them only to probe, not to decide
- NEVER fill silence -- wait at least 5 seconds after a pause
  before asking a follow-up
- NEVER conduct fewer than 5 interviews before drawing conclusions
  from qualitative research -- patterns require repetition
- NEVER quote a single interview as "users want X" --
  one interview is an anecdote; five are a signal

ALL OUTPUTS REQUIRE REVIEW BY THE PM BEFORE USE IN RESEARCH SESSIONS.
