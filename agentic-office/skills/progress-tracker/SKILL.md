---
name: progress-tracker
description: >
  Activate for: weekly status, project status, milestone, blocker,
  RAG status, executive dashboard, portfolio view, progress report,
  what's blocking, how are we doing on, what's the status of,
  where are we with, is this on track, milestone check,
  what have we completed, what's in progress.
  NOT for: daily digest (use digest),
  brain dump prioritisation (use task-intelligence).
---

## PROGRESS TRACKING AND DASHBOARD WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

Load dashboard configuration from work.local.md `dashboard:` section.

### STEP 2 — IDENTIFY REQUEST TYPE

TYPE 1: WEEKLY STATUS (across all projects)
Output: RAG status per project; current milestone; this week's action;
critical path; open delegations

TYPE 2: PROJECT MILESTONE PLAN
Output: Full milestone breakdown for a project with owners and dates

TYPE 3: BLOCKER IDENTIFICATION
Output: All blockers across all projects; who owns resolving each;
escalation recommendation if stalled

TYPE 4: COMPLETION SUMMARY
Output: What was completed this week/period; what the impact was;
what carries forward

TYPE 5: EXECUTIVE DASHBOARD
Output: Full cross-domain dashboard view

### STEP 3 — PRODUCE OUTPUT

#### Weekly Status Output

```
WEEKLY PROJECT STATUS — Week of [Date]
================================================================
-- [PROJECT NAME] ([Priority]) ----------------------------------
Status:           [GREEN/AMBER/RED] [ONE-LINE STATUS]
This week:        [Current milestone or activity]
Next:             [Next milestone; due date]
Risk:             [What could derail — be specific; not "general risk"]
This week's action: [The one thing that moves this forward most]
Open delegations: [Any delegated items affecting this project]

-- CRITICAL PATH (this week) ------------------------------------
[The 3-5 items that, if done, make the week a success]
1. [Item] — [Owner] — [Due]
2. [Item] — [Owner] — [Due]

-- BLOCKERS ------------------------------------------------------
RED [Project]: [What is blocked] — [Who owns unblocking] — [Days blocked]
[Escalation recommended if blocked >7 days]
================================================================
```

#### Milestone Plan Format

```
MILESTONE PLAN: [Project Name]
Owner: [Name] | Priority: [P1/P2/P3] | Target: [End date]
------------------------------------------------------------
MILESTONE 1: [Name]
Due:    [Date]
Owner:  [Person]
Done when: [Specific deliverable or outcome]
Dependencies: [What must be true before this can complete]
Status: [NOT STARTED / IN PROGRESS / AT RISK / COMPLETE]

[Repeat for each milestone]
------------------------------------------------------------
```

#### Executive Dashboard Output

```
EXECUTIVE DASHBOARD — [Date] — [Name from work.local.md]
================================================================
HEADLINE: [GREEN ALL CLEAR / AMBER WATCH ITEMS / RED ACTION REQUIRED]

-- P1 PROJECTS ---------------------------------------------------
[Project name]    [GREEN/AMBER/RED] [One-line status]
This week:        [Current milestone]
Risk:             [If AMBER/RED — what specifically]
Action:           [What needs doing this week]

-- P2 PROJECTS ---------------------------------------------------
[Same format — briefer]

-- KEY METRICS (from domain agents) ------------------------------
[Domain]: [Metric name] — [Value] — [GREEN/AMBER/RED]
[Only metrics configured in work.local.md dashboard.metrics_sources]

-- OPEN ACTIONS (this week) --------------------------------------
[ ] [Item] — [Owner] — [Due date]
[Only actions due this week or overdue]

-- OPEN DELEGATIONS ----------------------------------------------
[Person]: [What] — due [date] — [PENDING / CONFIRMED / OVERDUE]

-- UPCOMING DECISIONS --------------------------------------------
[Date]: [Decision needed] — [Owner]

-- CALENDAR HIGHLIGHTS -------------------------------------------
[Day]: [Meeting or deadline that matters most this week]
================================================================
```

### RAG Status Rules

GREEN — ON TRACK:
All milestones on schedule; no blockers; no decisions overdue

AMBER — WATCH:
One milestone at risk; minor blocker present; decision needed this week

RED — ACTION REQUIRED:
Milestone missed or at imminent risk; hard blocker; decision overdue;
escalation needed

RULE: Never show GREEN for a project where a milestone has slipped
without explicit acknowledgement that the slip was accepted.

### Blocker Classification

SOFT BLOCKER: Slowing progress but workaround exists
Action: Note; monitor; apply workaround

HARD BLOCKER: Progress cannot continue without resolution
Action: Escalate immediately; name who must resolve; set deadline

STALE BLOCKER: Has been open >7 days without movement
Action: Escalate to next level; flag in digest

## NEVER DO THESE

- NEVER report a project as GREEN if a milestone has slipped —
  acknowledge the slip; reforecast; then assess if still on track
- NEVER leave a hard blocker without naming who owns resolving it
- NEVER omit completion notes when a milestone closes — what was
  delivered, what was not, and what it enables next
- NEVER make the dashboard longer than one page
- NEVER omit the headline status — the first thing a busy executive
  needs is whether anything needs immediate attention
