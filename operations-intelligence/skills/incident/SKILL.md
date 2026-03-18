---
name: incident
description: >
  Activate for: incident, outage, system failure, post-mortem, incident
  post-mortem, root cause analysis, RCA, five whys, corrective action,
  lessons learned, incident log, incident report, P1, P2, major incident,
  incident review, incident timeline, what went wrong, service outage,
  payment failure, data breach incident, incident response, MTTD, MTTR,
  incident management, on-call, escalation, incident retrospective,
  corrective action tracker, lessons learned brief.
  NOT for: change impact assessment (use official /change-request),
  risk register building (use official risk-assessment auto-skill),
  compliance obligation mapping (use official compliance-tracking auto-skill).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/incident"
  mcp-integrations: "ITSM / incident log, calendar, email / Slack"
---

## UNIVERSAL RULES (apply to every incident task)

- NEVER skip the post-mortem for a P1 incident -- the post-mortem is
  how the organisation learns; skipping it guarantees recurrence
- NEVER conduct a post-mortem as a blame session -- frame every question
  as "what in our systems, processes, or controls allowed this?" not
  "who made the mistake?"
- NEVER accept a corrective action that targets only the proximate cause --
  fixing "the thing that broke" without fixing "why it was able to break"
  is incomplete
- ALWAYS include specific recommended actions with deadlines in every
  output -- observations without actions are not acceptable
- ALWAYS load ops.local.md for incident severity definitions, escalation
  paths, and post-mortem requirements

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          [e.g. Post-Mortem -- Payment System Outage]
INCIDENT TYPE: [Post-Mortem / Five Whys / Log Entry / CA Tracker / Brief]
CONFIGURATION: [Loaded: ops.local.md / Not configured]
DATE:          [Date of output]
OWNER:         [Named post-mortem lead]
```

## INCIDENT SEVERITY CLASSIFICATION

Configure in ops.local.md -- defaults:

```
P1 -- CRITICAL:
  Service unavailable; >50% of users/transactions affected;
  revenue impact >threshold; regulatory notification likely
  Response: immediate; senior management within 15 min
  Post-mortem: mandatory; within 5 business days

P2 -- MAJOR:
  Significant degradation; >20% affected; revenue impact;
  customer-visible; no regulatory notification
  Response: within 30 min; team lead engaged; hourly updates
  Post-mortem: mandatory; within 10 business days

P3 -- MINOR:
  Limited impact; <20% affected; no revenue impact; workaround available
  Response: within 2 hours; standard team response; daily updates
  Post-mortem: optional; log entry required
```

## INCIDENT QUALITY STANDARDS

Every post-mortem output must include:

- Timeline (specific times -- not "eventually" or "shortly after")
- Root cause (systemic -- not the proximate event)
- Contributing factors (what made it worse)
- What went well (protect what works)
- Corrective actions (specific, owned, time-bound)
- Lessons learned (for organisation-wide sharing)

## INCIDENT WORKFLOW

### Task Type 1: POST-MORTEM

```
INCIDENT POST-MORTEM REPORT
================================================================
Incident ID:   [INC-YYYY-NNN]
Severity:      [P1 / P2 / P3]
Date:          [Date] | Duration: [Start-End, total hours]
Status:        CLOSED
Lead:          [Named person]
Distribution:  [Who receives this report]

INCIDENT SUMMARY
[2-3 sentences: what happened, how long, what the impact was.
 Written for a leadership audience -- no technical jargon.]

TIMELINE
[HH:MM]: [Event -- specific; factual; not interpretive]
[HH:MM]: [Event]
[Note gap between START and DETECTION -- this is MTTD]
[Note gap between DETECTION and first ACTION -- response lag]

IMPACT
Users/customers affected: [N]
Transactions affected:    [N / value]
Duration of impact:       [Time]
Regulatory notification:  [Required / Not required -- reason]
Reputational impact:      [Social media / press / complaints]
Estimated financial impact: [Range]

ROOT CAUSE ANALYSIS
Immediate cause:  [The proximate event]
Root cause(s):    [The systemic reason -- use Five Whys]

CONTRIBUTING FACTORS
[What amplified impact or slowed resolution]

WHAT WENT WELL
[Specific items -- every incident has things that worked]

CORRECTIVE ACTIONS
[CA-NNN]: [Action title]
  Action:    [Specific -- what changes]
  Owner:     [Named person -- not "the team"]
  Due:       [Date -- not "ASAP"]
  Priority:  [P1 = 1 week / P2 = 1 month / P3 = quarter]
  Done when: [Verifiable outcome]

LESSONS LEARNED
[L-N]: [Principle for organisation-wide sharing]

FOLLOW-UP
CA review meeting: [Date -- typically 4 weeks after]
Distributed to:    [List]
================================================================
```

### Task Type 2: FIVE WHYS ROOT CAUSE DRILL

Principle: Ask "why?" five times. Each answer becomes the next question.
Goal: Move from proximate cause to systemic root cause.

```
FIVE WHYS ANALYSIS: [Incident description]
----------------------------------------------------------------
WHY 1: Why did [the incident] happen?
-> [Answer]

WHY 2: Why did [answer to WHY 1] happen?
-> [Answer]

WHY 3: Why did [answer to WHY 2] happen?
-> [Answer]

WHY 4: Why did [answer to WHY 3] happen?
-> [Answer]

WHY 5: Why did [answer to WHY 4] happen?
-> [Answer]

SYSTEMIC ROOT CAUSE:
[Summary -- the organisational, process, or control gap]

CORRECTIVE ACTION targets ROOT CAUSE -- not WHY 1:
WRONG: [Action addressing proximate cause only]
RIGHT: [Action addressing systemic cause at WHY 4/5]
----------------------------------------------------------------
```

### Task Type 3: INCIDENT LOG ENTRY

```
INCIDENT LOG ENTRY
----------------------------------------------------------------
ID:          [INC-YYYY-NNN]
Date:        [Date] | Time: [HH:MM] | Duration: [N hours]
Severity:    [P1 / P2 / P3]
Summary:     [One sentence]
Impact:      [Users affected; transactions affected; financial]
Root cause:  [Brief -- systemic]
Status:      [Open / Resolved / CA pending]
Owner:       [Named person]
Post-mortem: [Completed / Scheduled [date] / Not required (P3)]
----------------------------------------------------------------
```

### Task Type 4: CORRECTIVE ACTION TRACKER

```
CORRECTIVE ACTION TRACKER -- [Date]
================================================================
| CA ID | Incident | Action | Owner | Due | Status | Overdue? |
|---|---|---|---|---|---|---|
| [CA-NNN] | [INC-ID] | [Action] | [Name] | [Date] | [Open/Done] | [Y/N] |

OVERDUE ACTIONS: [N]
ACTIONS DUE THIS WEEK: [N]
ESCALATION REQUIRED: [List any >2 weeks overdue]
================================================================
```

### Task Type 5: LESSONS LEARNED BRIEF

```
LESSONS LEARNED BRIEF
----------------------------------------------------------------
Incident: [INC-ID] -- [Title]
Date:     [Date]
For:      [All-staff / Leadership / Ops team]

WHAT HAPPENED (plain language):
[2-3 sentences -- accessible to non-technical audience]

KEY LESSON:
[One principle that would prevent this or reduce its impact]

WHAT WE CHANGED:
[Specific corrective actions taken or in progress]

WHAT THIS MEANS FOR YOU:
[How this affects day-to-day operations; any new procedures]
----------------------------------------------------------------
```

## CORRECTIVE ACTION QUALITY TEST

Before accepting any corrective action:

```
SPECIFIC:   Can you describe exactly what will be different when done?
  FAIL: "Improve the runbook process"
  PASS: "All runbooks validated; sign-off logged; validation in checklist"

OWNED:      Is there one named person accountable?
  FAIL: "IT will handle it"
  PASS: "[Named: Head of Infrastructure]"

TIME-BOUND: Is there a specific date?
  FAIL: "As soon as possible"
  PASS: "By [specific date]"

ROOT CAUSE: Does this close the systemic gap?
  FAIL: Action targets WHY 1 only
  PASS: Action targets WHY 4 or WHY 5

VERIFIABLE: How will we confirm it is done?
  FAIL: "The team will be more careful"
  PASS: "[Specific deliverable or evidence]"
```

## NEVER DO THESE

- NEVER assign a corrective action to "the team" -- one named person;
  shared ownership is no ownership
- NEVER write "ASAP" as a corrective action due date -- set a specific date
- NEVER close a post-mortem without scheduling the CA review meeting --
  corrective actions not followed up are good intentions, not actions
- NEVER omit "What went well" from a post-mortem -- every incident has
  things that worked; protecting those is as important as fixing gaps
- NEVER produce a timeline with vague time references -- "shortly after"
  and "eventually" are not acceptable; use specific timestamps

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
