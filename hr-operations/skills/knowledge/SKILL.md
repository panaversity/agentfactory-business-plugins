---
name: knowledge
description: >
  Capture and structure institutional knowledge before it is lost. Activate for:
  institutional knowledge, knowledge capture, knowledge transfer, knowledge
  base article, knowledge management, preserve knowledge, what do they know,
  departing employee knowledge, exit knowledge, succession knowledge, tacit
  knowledge, undocumented knowledge, before they leave, knowledge interview,
  knowledge extraction, document what we know, knowledge at risk, knowledge map.
  NOT for: policy lookup or FAQ queries (use policy-lookup),
  onboarding plans (use onboarding), offboarding checklists (use offboard).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/knowledge"
---

## UNIVERSAL RULES (apply to every knowledge capture task)

- NEVER treat the departing employee's account as the complete truth --
  cross-reference with documentation and other stakeholders where possible
- NEVER let knowledge capture become a blame session --
  frame all capture as organisational learning, not performance review
- NEVER classify knowledge as LOW RISK without checking whether
  anyone else actually holds it -- "I thought [person] knew this too"
  is a common and expensive mistake
- NEVER publish a knowledge article without a reviewer confirming
  accuracy -- mark as DRAFT until reviewed
- NEVER skip the "what we should NOT try again" question --
  this is often the most valuable institutional knowledge captured
- ALWAYS include specific recommended actions and timeline

## BEFORE IMPLEMENTATION

| Source            | Check                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Conversation**  | Departing employee name, role, tenure, last working day, known critical knowledge areas                                                                |
| **hr.local.md**   | HR contact directory (who conducts capture sessions), data retention policy (how long knowledge articles are kept), knowledge article storage location |
| **Prior outputs** | None — /knowledge is typically the first skill invoked in a departure workflow                                                                         |

## CLARIFICATION QUESTIONS

**Required** (ask if not provided):

- Who is the departing employee? (name and role)
- When is their departure date?

**Optional** (ask if context suggests value):

- What are the known critical knowledge areas this person holds?
- Has a successor been identified?
- Is this reactive (departure confirmed) or proactive (no departure planned)?

**If information is missing**: Run the full five-factor risk assessment to identify knowledge areas. Use hr.local.md defaults for session logistics and article storage. State assumptions about risk classification explicitly.

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          Knowledge Capture Plan -- [Employee Name]
DOCUMENT TYPE: Knowledge Capture Plan
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   CONFIDENTIAL
```

## KNOWLEDGE CAPTURE WORKFLOW

### Phase 1: Knowledge Risk Assessment

Before designing a capture plan, assess the risk:

HIGH RISK:

- Sole holder of critical knowledge (no one else knows this)
- Knowledge is client-facing or revenue-critical
- Departure is confirmed or imminent
- Knowledge is undocumented
- No successor identified or ready

MEDIUM RISK:

- Significant knowledge holder (others have partial knowledge)
- Some documentation exists but incomplete
- Departure possible in 6-12 months
- Successor exists but not yet fully prepared

LOW RISK:

- Knowledge broadly distributed in team
- Well-documented
- Multiple holders
- Successor fully prepared

RISK SCORING (score each factor 1-3):
Tenure: <2 years (1) | 2-5 years (2) | 5+ years (3)
Role criticality: Support (1) | Specialist (2) | Leadership/sole expert (3)
Documentation level: Well documented (1) | Partial (2) | Undocumented (3)
Successor readiness: Ready (1) | Developing (2) | None identified (3)
Client/revenue impact: None (1) | Some (2) | Direct and significant (3)

TOTAL SCORE:
5-7: LOW RISK -- standard handover document
8-10: MEDIUM RISK -- 2 knowledge capture sessions; 3-4 knowledge articles
11-15: HIGH RISK -- full capture programme; 3+ sessions; immediate escalation

### Phase 2: Proactive vs. Reactive Capture

REACTIVE (triggered by departure): Urgent; comprehensive; time-limited
Generate a knowledge capture plan immediately on resignation.
Prioritise: what is ONLY in this person's head?

PROACTIVE (no departure planned): Systematic; can be thorough
Annual knowledge review for HIGH-risk knowledge holders.
Focus on the knowledge most likely to be lost if departure occurs.
Build knowledge articles over time, not all at once.

### Phase 3: Generate Capture Plan

For each knowledge holder, capture plan includes:

EMPLOYEE: [Name] | ROLE: [Role] | TENURE: [Years] | RISK: [H/M/L]
KEY KNOWLEDGE AREAS (ranked by risk):

1. [Area -- describe what makes this knowledge unique or hard to replace]
2. [Area]
3. [Area]

CAPTURE METHOD:

- Interview-based (recommended for complex tacit knowledge)
- Document review (for knowledge that IS documented but needs curation)
- Shadowing / observation (for procedural or behavioural knowledge)
- Pair working (for technical or skills transfer)

SESSIONS RECOMMENDED:
[N] sessions x [duration] = [total hours]
Session 1: [Knowledge area] -- [Method] -- [Date]
Session 2: [Knowledge area] -- [Method] -- [Date]

OUTPUTS:
[Document type] -- [Title] -- [Target completion]

### Phase 4: Knowledge Interview Guide

OPENING (5 minutes):
"The goal of this session is to make sure the knowledge and
insights you've built up over [N] years here don't disappear
when you leave. There are no wrong answers -- we want what's
in your head, not what's in the documents."

CORE QUESTIONS (by knowledge area):

FOR CLIENT / STAKEHOLDER KNOWLEDGE:

- "Tell me about [client/stakeholder]. Who are the real decision-makers
  -- not just the named contacts but the people whose opinion actually counts?"
- "What has gone wrong in this relationship and how was it recovered?
  What would you do differently?"
- "What are the unwritten rules? Things that aren't in any document
  but that the next person needs to know?"
- "What does [client/stakeholder] actually care about most?
  Not what the contract says -- what makes them feel it's working?"

FOR PROCESS / METHODOLOGY KNOWLEDGE:

- "Our process says [X]. Where does reality differ from the documentation?"
- "What are the early warning signs that something is going wrong?
  The signals you've learned to watch for?"
- "What decisions do you make yourself vs. escalate?
  Walk me through a recent example."
- "If I followed our documented process exactly, what would I get wrong?"

FOR ORGANISATIONAL / CONTEXT KNOWLEDGE:

- "What would you tell someone starting your role tomorrow
  that is not in any document?"
- "What has this organisation tried that didn't work,
  and why? What should we not try again?"
- "Who are the internal stakeholders I need to manage carefully?
  What do I need to know about each of them?"
- "What are you most worried we'll get wrong after you leave?"
- "If you were staying, what would you do in the next 12 months
  that we haven't done yet?"

CLOSING:
"Is there anything we haven't talked about that you think
is important for the next person to know?"

### Phase 5: Knowledge Article Structure (output from sessions)

```
KNOWLEDGE ARTICLE: [Title]
================================================================
Author:    [Departing employee] | Captured by: [HR/manager]
Date:      [Date of capture] | Reviewed by: [HR] | Status: DRAFT
Category:  [Client / Process / Organisational / Technical]
Audience:  [Successor / Team / Whole organisation]

THE KNOWLEDGE
[What to know -- the substance, in plain language]

WHEN IT APPLIES
[Context: when does this knowledge become relevant?]

EXCEPTIONS AND EDGE CASES
[When does the standard approach NOT apply?]

RELATED CONTACTS
[Who else holds related knowledge?]

RELATED DOCUMENTS
[What documentation exists that this supplements?]

CONFIDENCE LEVEL
[HIGH: this is definitely how it works
 MEDIUM: this is the expert's interpretation; verify with [name]
 LOW: this may be out of date; confirm with [name] before relying]
================================================================
```

## OUTPUT FORMAT

```
TASK:          Knowledge Capture Plan -- [Employee Name]
DOCUMENT TYPE: Knowledge Capture Plan
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL

KNOWLEDGE CAPTURE PLAN: [Name]
================================================================
Role: [Title] | Tenure: [Years] | Risk: [HIGH/MEDIUM/LOW]

KEY KNOWLEDGE AREAS:
  1. [Area -- what makes it unique]
  2. [Area]

CAPTURE METHOD: [Interview / Document review / Shadowing / Pair working]

SESSIONS:
  Session 1: [Knowledge area] -- [Duration] -- [Date]
  Session 2: [Knowledge area] -- [Duration] -- [Date]

OUTPUTS:
  [Document type] -- [Title] -- [Target date]

INTERVIEW GUIDE:
  [Questions by knowledge area -- client/process/organisational]
================================================================
```

## NEVER DO THESE

- NEVER treat the departing employee's account as the complete truth --
  cross-reference with documentation and other stakeholders where possible
- NEVER let knowledge capture become a blame session --
  frame all capture as organisational learning, not performance review
- NEVER classify knowledge as LOW RISK without checking whether
  anyone else actually holds it
- NEVER publish a knowledge article without a reviewer confirming
  accuracy -- mark as DRAFT until reviewed
- NEVER skip the "what we should NOT try again" question --
  this is often the most valuable institutional knowledge captured

## AUTHORITATIVE SOURCES

- APQC (apqc.org) — Knowledge management best practices, maturity model, benchmarking data
- Nonaka & Takeuchi, _The Knowledge-Creating Company_ (1995) — SECI model for tacit-to-explicit knowledge conversion
- NASA Lessons Learned database (llis.nasa.gov) — Example of institutional knowledge capture at scale
- KM World (kmworld.com) — Knowledge management industry research and case studies

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
