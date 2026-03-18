---
name: delegation
description: >
  Activate for: delegate, delegation record, handoff, delegation brief,
  follow-up, delegation quality, assign to, hand off to,
  delegation tracking, who should handle this, delegate this to,
  open delegations, what have I delegated, delegation audit.
  NOT for: basic task CRUD (use official productivity plugin task-management),
  brain dump prioritisation (use task-intelligence).
---

## DELEGATION WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

Load the delegatee's person entry from work.local.md Layer 2 (Team).

### STEP 2 — PRODUCE DELEGATION RECORD

OUTPUT STRUCTURE:

```
DELEGATION RECORD — [Description]
================================================================
Delegated to:  [Person name — from work.local.md if available]
Delegated by:  [Your name from work.local.md personal layer]
Date:          [Today]
Due:           [Specific date and time — not ASAP]

DELIVERABLE:
What:    [Precise description of what must be produced]
Format:  [Slides / doc / data / email / verbal — specific]
Length:  [If relevant — 2-page; 10 slides; 500 words]

CONTEXT:
Purpose:   [Why this is needed; what decision it supports]
Audience:  [Who will see/use this output]
Key question the output should answer: [The most important question]

CONSTRAINTS:
What not to do: [Any specific exclusions or out-of-scope items]
Prior work:     [Any existing documents or decisions to build from]

HANDOFF COMMUNICATION (ready to send):
[Draft message in the delegatee's preferred channel and style,
 loaded from work.local.md person entry]

FOLLOW-UP PLAN:
Confirmation due:  [Time — typically EOD today for same-week items]
Check-in:          [If no confirmation: follow up at this time]
Escalation:        [If no delivery by [date - N days]: flag in digest]
================================================================
```

### STEP 3 — LOG THE DELEGATION

Add an entry to the delegation log in work.local.md:

```
- task: "[Description]"
  delegated_to: "[Person]"
  delegated_by: "[You]"
  date_delegated: "[Date]"
  due_date: "[Date]"
  confirmed: false
  status: "PENDING CONFIRMATION"
  deliverable: "[What was requested]"
```

### Handoff Communication Calibration

Apply the delegatee's communication style from work.local.md:

PERSON prefers async / written:
Draft a Slack message or email; not a meeting request

PERSON needs lead time / dislikes last-minute:
Acknowledge the ask is time-sensitive; offer to adjust scope if needed
Note in the message: "I know this is a short timeline — let me know
if the scope needs adjusting"

PERSON is detail-oriented:
Provide more context than you think necessary

PERSON pushes back on scope creep:
Be hyper-specific about exactly what you need; avoid open-ended asks

### Delegation Quality Checklist

Before sending any delegation:

1. Specific deliverable (not activity)
2. Named person (one; not "the team")
3. Specific deadline (not ASAP)
4. Context (purpose + audience)
5. Format specified
6. Written in the delegatee's preferred style
7. Follow-up mechanism defined

### Delegation Follow-up Standards

CONFIRMATION WINDOW: 24 hours for same-week items; 48 hours for longer ones
If no confirmation within window: send a gentle follow-up
If still no confirmation after second contact: flag in next digest

STATUS CADENCE:
Items <5 days: one check-in at midpoint
Items 5-14 days: weekly check-in
Items >14 days: bi-weekly check-in

OVERDUE HANDLING:
1 day late: polite inquiry — "any blockers I can help with?"
3 days late: explicit conversation — "this is affecting [downstream item]"
1 week late: flag in digest; consider re-routing or taking back

## NEVER DO THESE

- NEVER delegate without a specific deadline — "when you can" produces
  the lowest-priority work on the delegatee's list
- NEVER delegate to a group — one person owns the delivery
- NEVER use jargon or internal codenames in a delegation brief unless
  you are certain the delegatee knows them
- NEVER forget to load the delegatee's communication style from
  work.local.md before drafting the handoff message
- NEVER close a delegation in the log without confirming the deliverable
  was actually received and meets the standard
