---
name: meeting-intelligence
description: >
  Activate for: meeting prep, meeting synthesis, before the meeting,
  after the meeting, D/A/F/Q/R, meeting brief, stakeholder prep,
  meeting notes synthesis, meeting follow-up, meeting actions,
  meeting decisions, post-meeting notes, synthesise the meeting,
  what was decided in the meeting, meeting record.
  NOT for: situation briefs (use executive-brief),
  daily digest (use digest).
---

## MEETING INTELLIGENCE WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

### STEP 2 — IDENTIFY PHASE

### The Three-Phase Model

BEFORE (30 minutes pre-meeting):
Purpose: Ensure every attendee (especially you) is prepared to contribute
Input: Meeting name, agenda, attendees
Output: Context brief per agenda item; stakeholder notes; decisions needed;
meeting rules from work.local.md culture

DURING (real-time support):
Purpose: Structured note-taking format that produces synthesis-ready output
Output: Note-taking template with D/A/F/Q/R coding

AFTER (within 2 hours post-meeting):
Purpose: Convert raw notes into structured, distributable meeting record
Input: Raw notes (any format)
Output: Decisions (with owners), actions (with owners and deadlines),
deferred items (with triggers), next meeting proposal,
work.local.md update proposals

### STEP 3 — EXECUTE

#### Meeting Prep Output Structure

```
MEETING BRIEF — [Meeting Name]
Date: [Date] | Time: [Time + Timezone] | Duration: [Duration]
Attendees: [List — with roles from work.local.md if available]
================================================================
AGENDA ITEM 1: [Item name]
  Context:         [Background the attendees need to contribute well]
  Decision needed: [What must be decided vs. what is for discussion only]
  Your position:   [What you think; what you want from this item]
  Key risk:        [What could go wrong in this discussion]
  Stakeholder note: [Relevant communication guidance for key attendees]

[Repeat for each agenda item]

STAKEHOLDER NOTES:
[Person] ([Role]): [Communication style; what they need to engage;
                    what they are likely to push on; how to handle]

MEETING RULES (from work.local.md):
[Apply culture.decision_making; culture.unwritten_rules relevant to this group]

LAST TIME THIS GROUP MET:
[Date; key decisions made; open actions from that meeting]
[Surface from decision log in work.local.md]

WHAT YOU NEED FROM THIS MEETING:
[Restate the user's goal — decision / alignment / update / commitment]
================================================================
```

#### During-Meeting Note-Taking Template

```
MEETING NOTES — [Name] — [Date]
---------------------------------------------------------
Use these codes while taking notes:
D: [Decision made]
A: [Action — who; what; by when]
F: [Fact / context to keep on record]
Q: [Question raised but not resolved — needs follow-up]
R: [Risk or concern raised]

[Take notes in any order during the meeting — synthesis will organise them]
---------------------------------------------------------
```

#### Meeting Synthesis Output Structure

```
MEETING NOTES — [Meeting Name]
Date: [Date] | Duration: [N min] | Synthesised: [Time]
Attendees: [List]
================================================================
DECISIONS MADE:
D-[NNN]: [Decision — specific; who made it; any conditions]

ACTION ITEMS:
A-[NNN]: [What must be done]
         Owner: [Named person — not "the team"]
         Due:   [Specific date — not "ASAP"]

ITEMS DEFERRED:
[Item]: Deferred — reason: [why]; trigger for revisit: [specific condition]

QUESTIONS OPEN:
[Question]: [Who owns finding the answer]; [by when]

NEXT MEETING:
Proposed: [Date] | [Time] | Proposed agenda: [Items from today's deferrals
+ open actions to review + any standing agenda items]

WORK.LOCAL.MD UPDATES PROPOSED:
[Specific updates — project status changes; new decisions; new actions]
================================================================
```

### Decision Numbering Convention

Decisions are numbered D-[YYYY]-[NNN] for persistence across meetings.
Actions are numbered A-[YYYY]-[NNN].

Both are stored in work.local.md decision log and action log respectively.
This creates a searchable history of what was decided and why.

### Synthesis Quality Rules

DECISIONS:
Good: "approved GBP 50K analytics budget in principle, subject to ROI brief"
Bad: "discussed the analytics budget"

ACTIONS:
Good: Owned by one named person; has a specific date; describes the output
Bad: "Omar to look into the analytics thing"

DEFERRED ITEMS:
Good: Has a trigger — "revisit when Nighthawk facility resolved"
Bad: "discussed but not resolved; will revisit later"

## NEVER DO THESE

- NEVER produce a meeting prep brief without stakeholder notes
- NEVER produce a meeting synthesis where actions say "the team will..."
  — one person owns each action; shared ownership is no ownership
- NEVER use "ASAP" as an action deadline — set a specific date
- NEVER omit deferred items from the synthesis — items that are
  not decided need a trigger for revisit; "later" means never
- NEVER skip the "last time this group met" section in meeting prep
  if prior meeting records exist in work.local.md
