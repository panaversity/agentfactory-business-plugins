---
name: task-intelligence
description: >
  Activate for: brain dump, prioritise, P1 P2 P3, critical path,
  daily priorities, weekly planning, backlog review, cross-domain plan,
  what should I work on, capture everything in my head, sort my priorities,
  what is most important right now, weekly critical path.
  NOT for: basic task CRUD (use official productivity plugin task-management),
  delegation (use delegation skill).
---

## TASK INTELLIGENCE WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

### STEP 2 — IDENTIFY REQUEST TYPE

TYPE 1: CAPTURE (from brain dump / meeting notes / messages)
Purpose: Rapidly capture and structure unorganised input.
Input: Raw notes, brain dump, meeting output, messages — any format
Output: Structured, prioritised list with owners and deadlines

TYPE 2: DAILY PRIORITISATION
Purpose: Determine what to work on today from a larger set.
Input: Full list (from work.local.md or provided)
Output: Today's critical path (3-5 items) + schedule suggestion

TYPE 3: WEEKLY PLANNING
Purpose: Set the week's priorities before it begins.
Input: Project statuses; open delegations; upcoming deadlines
Output: Week-ahead critical path; delegation candidates; decision items

TYPE 4: BACKLOG REVIEW
Purpose: Audit the backlog — drop dead items; re-prioritise the rest.
Input: Current backlog
Output: Kept / dropped / re-prioritised list with rationale

TYPE 5: CROSS-DOMAIN PLAN
Purpose: Generate an integrated action plan for a scenario that
spans multiple functions (HR + Finance + Ops, etc.)
Output: Items by function; dependencies; delegations; timeline

### STEP 3 — EXECUTE WITH PRIORITY SORTING

OUTPUT STRUCTURE:

```
CAPTURE — [Date]
================================================================
[N] items captured | [N] overdue | [N] delegation candidates

-- P1 — URGENT / HIGH IMPACT ---------------------------------
[ ] [ITEM-NNN] [Title]
  Context:  [Why this matters; what it connects to]
  Due:      [Specific date or "today"]
  Project:  [Project name from work.local.md]
  Action:   [Specific first action — not vague]
  Delegate: [If applicable — to whom]
  Note:     [Any sensitivity or communication guidance]

-- P2 — IMPORTANT / THIS WEEK --------------------------------
[Same structure]

-- P3 — STANDARD / BACKLOG -----------------------------------
[Same structure — briefer]

-- DELEGATION CANDIDATES --------------------------------------
[Item] → [Person from work.local.md] (with brief note on approach)

-- BLOCKED / AT RISK ------------------------------------------
[Any item that cannot proceed without something else; name the blocker]
================================================================
```

### Priority Sorting Logic

When determining priority, apply in order:

1. Is there a hard deadline? (Date-certain = prioritise)
2. Is it blocking someone else? (Blocking = elevate)
3. Does it affect a P1 project? (P1 project item = at least P2)
4. What is the consequence if it slips one week? (Assess impact honestly)
5. Is the urgency feeling real or just habitual? (Email = rarely P1)

### The Brain Dump Pattern

When user provides unorganised input:

1. Extract every distinct item (even if vague or incomplete)
2. Enrich each with project context from work.local.md
3. Identify dependencies between items
4. Flag anything that should be delegated
5. Flag anything that should be dropped or questioned

### Item vs. Project Distinction

ITEM: Can be completed in one session; has a single clear output
PROJECT: Multiple items; spans days or weeks; has milestones

If an "item" has >3 steps and spans >1 day: it is a project.
Create a project entry in work.local.md instead.
Breaking projects down into single-session items is the user's job —
or use `/agentic-office:progress-tracker` to create a milestone plan.

## NEVER DO THESE

- NEVER classify more than 5 items as P1 — force re-prioritisation
  if the user tries to make everything critical
- NEVER leave a captured item without a project reference if
  it connects to a known project in work.local.md
- NEVER produce a list without a critical path — a list of
  everything is not a plan; a critical path is
- NEVER mark an item as P1 based purely on urgency without
  assessing actual importance
- NEVER produce a weekly plan without surfacing open delegations
