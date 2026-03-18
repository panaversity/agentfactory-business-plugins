---
name: executive-brief
description: >
  Activate for: situation brief, bring me up to speed, prep me for,
  pre-meeting brief, decision brief, context brief, catch me up,
  quick brief, what do I need to know before, background on,
  what's the situation with, before I call, what's the history on.
  NOT for: daily digest (use digest), meeting prep (use meeting-intelligence),
  cross-domain context injection (use context-loader).
---

## SITUATION BRIEF WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

### STEP 2 — IDENTIFY BRIEF TYPE

TYPE 1: PRE-MEETING BRIEF
Purpose: Everything you need to know before a specific meeting.
Input: Meeting name / attendees / agenda
Output: Context per agenda item; stakeholder notes; decisions needed;
prior meeting summary

TYPE 2: PRE-DECISION BRIEF
Purpose: All relevant context before making a specific decision.
Input: Decision to be made; who is affected; constraints
Output: Decision context; options; relevant precedents; stakeholder positions

TYPE 3: PERSON BRIEF
Purpose: Quick profile of someone you are about to interact with.
Input: Person name
Output: Role; current focus; communication style; today's context; approach tips

TYPE 4: PROJECT BRIEF
Purpose: Current status of a project you need to speak about.
Input: Project name
Output: Status; current milestone; risks; decisions made; key contacts

TYPE 5: TOPIC BRIEF
Purpose: Everything in workplace memory relevant to a topic.
Input: Topic name
Output: What is known across all memory layers; relevant decisions; open questions

### STEP 3 — PRODUCE BRIEF

OUTPUT STRUCTURE:

```
SITUATION BRIEF — [Subject]
Prepared: [Date/Time] | For: [Name from work.local.md]
================================================================
THE SITUATION IN ONE SENTENCE:
[Most important thing to know — written as a colleague would say it]

CONTEXT:
[Background — what led to this; relevant history; decisions already made]

WHAT YOU NEED TO KNOW NOW:
[Current status; what is live; what has changed recently]

THE KEY QUESTION:
[The one thing that needs resolving — decision / answer / commitment]

STAKEHOLDER POSITIONS (if relevant):
[Person]: [Their likely position; what they need; how to approach]

RISKS:
[What could go wrong in this conversation / decision]

YOUR RECOMMENDED APPROACH:
[Specific guidance — not generic; based on work.local.md context]
================================================================
```

### Brief Length Rules

QUICK BRIEF (< 5 minutes to read):
Use for: routine meetings; familiar topics; regular stakeholders
Length: 3-4 short sections; bullet points acceptable

FULL BRIEF (5-15 minutes to read):
Use for: high-stakes meetings; new stakeholders; complex decisions
Length: All sections; narrative where context is nuanced

## NEVER DO THESE

- NEVER produce a brief that is longer than the meeting it prepares for
- NEVER omit the "one sentence" summary — the most senior people
  read the summary first; if it is good, they read on
- NEVER ignore work.local.md person entries when writing stakeholder
  positions — generic stakeholder advice ignores what you actually know
