---
name: digest
description: >
  Activate for: daily digest, morning briefing, what's happening today,
  start of day brief, week ahead, Monday brief, weekly digest,
  start of week, what do I need to know today, morning rundown,
  daily overview, what's due today, Friday close, end of week summary.
  NOT for: executive dashboard (use progress-tracker),
  meeting prep (use meeting-intelligence).
---

## DAILY DIGEST WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

Load the digest configuration from work.local.md `digest:` section.

### STEP 2 — ASSEMBLE SOURCES

Pull from (in order of priority):

1. work.local.md — projects, priorities, open delegations, people context
2. Google Calendar (via MCP if available) — today's meetings; upcoming deadlines
3. Notion / project tracker (via MCP if available) — open items; overdue
4. Gmail (via MCP if available) — flagged / unread requiring response
5. Slack (via MCP if available) — @mentions; flagged items
6. Domain agent feeds — if configured in work.local.md agent_integrations

If MCP sources are not available, assemble from work.local.md alone
and note which sources could not be reached.

### STEP 3 — PRODUCE DIGEST

OUTPUT STRUCTURE:

```
DAILY DIGEST — [Day, Date] — [Name from work.local.md personal layer]
Prepared: [Time] [Timezone]
================================================================
HEADLINE STATUS: [GREEN CLEAR RUNWAY / AMBER WATCH ITEMS / RED CRITICAL ITEM(S)]

-- TODAY'S CRITICAL PATH -----------------------------------
[3-5 items maximum — ordered by importance, not urgency]
1. [RED if blocking/overdue] [Item] — [specific action]
2. [Item] — [specific action]
[No more than 5; if more exist, the user needs to re-prioritise]

-- TODAY'S CALENDAR ----------------------------------------
[Time]: [Meeting name] ([duration]; [brief context if non-obvious])
[Only show meetings that require preparation or attention]
Deep work blocks: [Note any unscheduled time for focused work]

-- OPEN DELEGATIONS STATUS ---------------------------------
[Person] — [What] — due [date] — [AWAITING / IN PROGRESS / OVERDUE]
[Flag overdue or unconfirmed delegations prominently]

-- FLAGGED FROM YESTERDAY ----------------------------------
[Items from yesterday that were not completed and remain live]
[Items that arose yesterday that need action today]

-- THIS WEEK AT A GLANCE -----------------------------------
[Day]: [Key item or meeting]
[Show the shape of the week — not every item; just the anchors]

-- UPCOMING DEADLINES --------------------------------------
[Date]: [Item] — [days away]
[Show next 7-14 days only; not the full calendar horizon]

-- WEEKLY PRIORITIES REMINDER ------------------------------
This week's [Boulders / Priorities / OKRs — use org terminology]:
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
================================================================
```

### Digest Length Rules

MAXIMUM: 1 page / ~5 minutes to read
If the digest exceeds one page, items are being included that
should not be there. Apply:

- Critical path: max 5 items
- Calendar: only meetings that require prep or attention
- Delegations: only those needing action today (overdue / no confirmation)
- Upcoming deadlines: next 7-14 days only

### Digest Tone

NOT: A comprehensive status report (that is the dashboard)
NOT: A list of everything happening (that is the full backlog)
IS: A briefing — the 5 things you most need to know today
written by a knowledgeable colleague, not a system

Tone: Warm and direct. First person where appropriate.
Example: "Nighthawk has been quiet for 10 days — escalation today, not tomorrow."
Not: "Project Nighthawk: status — no update for 10 days. Action: escalate."

### Digest Variants

MONDAY DIGEST (start of week):
Add section: "This Week's Critical Path" — the 3-5 things that,
if done this week, make the week a success.
Add section: "Open from Last Week" — anything that carried over.

FRIDAY DIGEST (end of week):
Replace "This Week at a Glance" with "Week Close":

- What was completed (celebrate progress)
- What carries over (and why — not as judgment; as information)
- What to set up for Monday (things that will be easier if done today)

## NEVER DO THESE

- NEVER produce a digest longer than one page — it will not be read
- NEVER put everything in the critical path — max 5 items;
  if everything is critical, nothing is; help the user re-prioritise
- NEVER omit open delegations — what you are waiting for is as
  important as what you are doing
- NEVER produce a digest without a weekly priorities reminder —
  daily urgency hijacks weekly importance; the reminder anchors the day
- NEVER use system-style language ("Status: pending; Action: review") —
  write as a knowledgeable colleague would brief a senior professional
