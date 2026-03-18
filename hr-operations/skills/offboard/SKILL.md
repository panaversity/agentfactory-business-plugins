---
name: offboard
description: >
  Structure offboarding processes and knowledge transfer. Activate for:
  offboarding, offboard, exit process, resignation, leaver, departing
  employee, employee leaving, last day, exit interview, notice period,
  handover plan, knowledge handover, departure checklist, systems access
  removal, final paycheck, P45, exit documentation, farewell, redundancy
  process, termination process, how to offboard.
  NOT for: onboarding plans (use onboarding), knowledge capture plans
  without a departure (use knowledge), performance reviews (use
  performance-review).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/offboard"
---

## UNIVERSAL RULES (apply to every offboarding task)

- NEVER delay the handover plan to the last week of notice --
  the departing employee is mentally disengaged; quality drops sharply
- NEVER conduct the exit interview with the line manager --
  employees will not be honest about management issues
  to the manager they are leaving
- NEVER leave IT access removal to chance -- document every system,
  every account, every credential that needs to be revoked
- NEVER omit the "what I wish I'd known" section of the handover --
  this is where the most valuable institutional knowledge lives
- NEVER close an offboarding without confirming the rehire decision
  is documented -- this protects the organisation from future risk
- NEVER generate termination or redundancy letters -- these require
  a qualified HR professional and legal review
- ALWAYS include specific dates and owners for every checklist item

## BEFORE IMPLEMENTATION

| Source            | Check                                                                                                                                                                 |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Conversation**  | Employee name, role, notice period, last working day, reason for departure (resignation/redundancy/retirement)                                                        |
| **hr.local.md**   | HR contacts (who manages each phase), data retention policy, onboarding programme documentation (useful for structuring handover), IT systems list for access removal |
| **Prior outputs** | /knowledge output if knowledge capture has already started (link capture sessions to handover timeline)                                                               |

## CLARIFICATION QUESTIONS

**Required** (ask if not provided):

- Who is the departing employee? (name and current role)
- What is their last working day?

**Optional** (ask if context suggests value):

- What is the reason for departure? (resignation / redundancy / retirement — each has different process requirements)
- Has a successor been identified?
- Are there specific handover priorities the manager has flagged?

**If information is missing**: Use the standard four-phase template. Flag items that require manager input (e.g., successor identification, team communication timing, handover priorities) with "[MANAGER INPUT REQUIRED]" markers.

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          Offboarding Plan -- [Employee Name]
DOCUMENT TYPE: Offboarding Plan
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   CONFIDENTIAL
```

## OFFBOARDING WORKFLOW

### Offboarding Principles

Offboarding done well:

1. Protects the organisation (access removal, documentation)
2. Preserves institutional knowledge (structured handover)
3. Leaves the departing employee with a positive experience
   (they become alumni, not detractors)
4. Supports the team (transition plan so nobody is blindsided)

Most offboarding does #1 incompletely and ignores #2, #3, and #4.

### Phase 1: Departure Confirmed -- Immediate Actions

WITHIN 24 HOURS of resignation confirmation:
HR:

- Acknowledge resignation in writing; confirm notice period
- Initiate HRIS departure record
- Notify Payroll: final pay date; accrued holiday calculation
- Trigger knowledge capture plan (use /knowledge)
- Schedule exit interview (Week 3 of notice -- not first week)

Manager:

- Notify team (timing agreed with employee -- usually within 1-2 days)
- Begin handover planning conversation with departing employee
- Identify successor or interim coverage

IT (schedule for last working day):

- Access removal schedule prepared
- Device return logistics arranged
- Email forwarding set up (for agreed period)
- Data transfer / account migration planned

### Phase 2: Notice Period -- Handover Planning

HANDOVER PLAN STRUCTURE:
For each responsibility or work stream:

| Area        | Current status | Files/location    | Key contacts     | Handover to | By date |
| ----------- | -------------- | ----------------- | ---------------- | ----------- | ------- |
| [Work area] | [Status]       | [Where docs live] | [Who to talk to] | [Person]    | [Date]  |

Handover plan should be:

- Written document (not verbal) -- information evaporates from verbal handovers
- Owned by the departing employee (they write it; manager reviews)
- Completed by Week 2 of notice period -- not the last week
- Reviewed by the manager for completeness

Handover topics to cover for every role:

- Current work in progress (status; what's left; who to ask)
- Recurring responsibilities (what happens weekly / monthly / quarterly)
- Key relationships (who to call; what they need; relationship context)
- Where things live (files; systems; credentials that need transferring)
- Open issues (anything unresolved the next person needs to know about)
- "What I wish I'd known" (the institutional knowledge no document captures)

### Phase 3: Exit Interview

TIMING: Week 3 of notice (not Week 1 -- too early; not last week -- too rushed)
INTERVIEWER: HR Business Partner (not the line manager)
FORMAT: Conversational; 45-60 minutes; confidential

QUESTIONS:
Understanding departure:

- "What prompted you to start looking / consider leaving?"
- "Was there a specific moment when you decided?"
- "What could we have done differently that might have changed that?"

Experience assessment:

- "What has been the best part of working here?"
- "What has been most frustrating or difficult?"
- "Do you feel you had the support and development you needed?"

Organisational learning:

- "What should we protect -- things we do well that we might lose?"
- "What do you think needs to change here?"
- "What advice would you give your successor?"

Closing:

- "Is there anything you'd want HR or leadership to know
  that you haven't been able to say in your role?"

EXIT INTERVIEW OUTPUT:
EXIT INTERVIEW SUMMARY -- [Name] | [Date] | [CONFIDENTIAL]
Departure reason (primary): [Category]
Key themes: [Synthesised -- not verbatim quotes]
Actionable feedback: [Specific items leadership should consider]
Rehire eligible: [YES / NO / CONDITIONAL] -- per HR decision
Filed: [Secure personnel record location]

### Phase 4: Last Day Checklist

HR:

- Final payslip confirmed (including accrued holiday payment)
- P45 / leaving documentation issued (jurisdiction-specific)
- HRIS record closed; departure date updated
- Benefits cessation processed (pension; health; etc.)
- Reference policy confirmed with employee

IT:

- All system access removed (document time and method)
- Device returned and wiped
- Email access terminated; auto-reply / forwarding confirmed
- Any shared accounts / passwords transferred or changed

Manager:

- Handover plan confirmed complete
- Team farewell arranged (employee's preference respected)
- Team communication sent (if not already)
- Successor briefed

## OUTPUT FORMAT

```
TASK:          Offboarding Plan -- [Employee Name]
DOCUMENT TYPE: Offboarding Plan
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL

OFFBOARDING PLAN: [Name]
Role: [Title] | Notice: [N weeks] | Last day: [Date]
================================================================

PHASE 1 -- IMMEDIATE (within 24 hours)
  HR:
  - [Action] -- [Owner] -- by [Date]
  Manager:
  - [Action] -- [Owner] -- by [Date]
  IT:
  - [Action] -- [Owner] -- by [Date]

PHASE 2 -- HANDOVER (complete by Week 2)
  | Area | Status | Files | Contacts | Handover to | By date |
  |------|--------|-------|----------|-------------|---------|
  | [Area] | [Status] | [Location] | [Names] | [Person] | [Date] |

PHASE 3 -- EXIT INTERVIEW
  Scheduled: [Date] with [HR name]

PHASE 4 -- LAST DAY
  HR:
  - [Action] -- [Owner] -- by [Date]
  IT:
  - [Action] -- [Owner] -- by [Date]
  Manager:
  - [Action] -- [Owner] -- by [Date]
================================================================
```

## NEVER DO THESE

- NEVER delay the handover plan to the last week of notice --
  the departing employee is mentally disengaged; quality drops sharply
- NEVER conduct the exit interview with the line manager --
  employees will not be honest about management issues
- NEVER leave IT access removal to chance -- document every system
- NEVER omit the "what I wish I'd known" section of the handover
- NEVER close an offboarding without confirming the rehire decision
  is documented
- NEVER generate termination or redundancy letters --
  these require a qualified HR professional and legal review

## AUTHORITATIVE SOURCES

- CIPD (cipd.org) — Offboarding checklist, good leaver experience guidance
- ACAS (acas.org.uk) — Leaving your job guide, notice period requirements (UK)
- SHRM (shrm.org) — Offboarding toolkit, exit interview best practices
- GOV.UK (gov.uk) — P45, statutory notice periods, redundancy process (UK statutory requirements)

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
