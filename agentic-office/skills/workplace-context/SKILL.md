---
name: workplace-context
description: >
  Activate for: workplace memory, person brief, team profile,
  organisation profile, add person, add project, add terminology,
  four-layer memory, communication style, stakeholder brief,
  post-meeting memory revision, who works on, team directory,
  revise workplace memory, organisation context.
  NOT for: basic memory CRUD (use official productivity plugin memory-management),
  cross-context search (use workplace-search).
---

## WORKPLACE MEMORY WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

### STEP 2 — IDENTIFY REQUEST TYPE

TYPE 1: ADD PERSON
Input: Name, role, reporting line, communication style, current focus,
any sensitivities
Output: Formatted person entry for work.local.md Layer 2 + confirmation

PERSON ENTRY FORMAT:

```
- name: "[Full name]"
  role: "[Job title]"
  reports_to: "[Manager name]"
  communication: >
    [How they prefer to receive information; what works; what annoys them]
  current_focus: "[What they are working on right now]"
  priorities: "[Their current top 1-3 priorities]"
  note: "[Anything important about working with this person]"
  sensitivity: "[Optional — anything that must not be shared broadly]"
```

TYPE 2: ADD PROJECT
Input: Project name, codename, status, priority, owner, description,
current milestone, risks, decisions already made
Output: Formatted project entry for work.local.md Layer 3 + confirmation

PROJECT ENTRY FORMAT:

```
- name: "[Project full name]"
  codename: "[Internal codename if different]"
  status: "[PLANNING / IN PROGRESS / AT RISK / BLOCKED / COMPLETE]"
  priority: "[P1 / P2 / P3]"
  owner: "[Named person]"
  description: >
    [What this project is; why it matters; key context]
  current_milestone: "[What is happening now]"
  next_milestone: "[What comes next; by when]"
  at_risk: "[What could go wrong; what is currently stalled]"
  decisions: ["[Decision made; date]"]
  key_contacts: ["[Person; role in project]"]
```

TYPE 3: ADD TERM
Input: Term, definition, when to use, when NOT to use, related terms
Output: Formatted terminology entry in Layer 4 + confirmation

TERMINOLOGY ENTRY FORMAT:

```
"[Term]": >
  [Definition in plain language — what it means in this organisation]
  Use: [When this term is appropriate]
  Not: [When NOT to use it — external comms? formal docs? pre-announcement?]
  Related: [Synonyms or near-synonyms]
```

TYPE 4: PERSON BRIEF
Input: Person name (or "everyone I'm meeting today" with list)
Output: Structured brief per person

PERSON BRIEF FORMAT:

```
--- [NAME] — [Role] -----------------------------------------------
Reports to:     [Name]
Current focus:  [What they are working on]
Communication:  [How to approach them today]
Today's context: [Anything live that affects this interaction]
How to approach: [Specific guidance for today]
Watch for:       [Anything to be aware of]
Do not:          [Any specific sensitivities]
-------------------------------------------------------------------
```

TYPE 5: POST-MEETING UPDATE
Input: Meeting name, decisions made, new actions, status changes,
new information about people
Output: Proposed updates to work.local.md across all relevant layers

PROPOSED UPDATES FORMAT:

```
MEMORY UPDATE PROPOSAL — [Meeting Name] — [Date]
================================================================
1. UPDATE: [Section]: [What changes]
   Current: "[Old text]"
   Proposed: "[New text]"
[Continue for each update]
Confirm to apply all? Or specify which updates to apply.
================================================================
```

TYPE 6: TERMINOLOGY QUERY
Input: "What does X mean?" or "What do we call Y?"
Output: Load from terminology dictionary in work.local.md;
apply in the response; if not found, offer to add

### STEP 3 — EXECUTE AND CONFIRM

For ADD operations (Types 1-3): Draft the entry, present for confirmation,
then write to work.local.md only after user confirms.

For QUERY operations (Types 4, 6): Load from work.local.md and present.

For UPDATE operations (Type 5): Propose all changes, let user select
which to apply.

### Sensitivity Handling

Some entries contain sensitive information:

- Succession planning (who is being considered for a role)
- Personal information about employees
- Commercial sensitivities (unannounced projects; pricing)
- Interpersonal dynamics (conflict; performance concerns)

RULES for sensitive entries:

- Add to work.local.md with a `sensitivity: RESTRICTED` flag
- Never surface in outputs where the subject might see them
- Never include in shared briefings or group outputs
- Apply only when directly relevant to the specific interaction

### Memory Maintenance Rules

STALE MEMORY DETECTION:
Flag any entry in work.local.md that has not been updated in >90 days
and prompt user to confirm or update.

Common staleness patterns:

- Person's role has changed but work.local.md has old title
- Project status is "IN PROGRESS" but it was completed months ago
- Terminology entry references a product or team that no longer exists

## NEVER DO THESE

- NEVER add a person entry without confirming the communication style
  observation is accurate (not assumed)
- NEVER apply a person entry's sensitivity notes in a group output
  where the subject might see it
- NEVER mark a project as COMPLETE without noting what was delivered
  and what (if anything) was not delivered
- NEVER add a terminology entry without defining BOTH when to use
  and when NOT to use the term
- NEVER propose memory updates without the user's explicit confirmation
