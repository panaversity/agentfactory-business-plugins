---
name: match
description: >
  Assess internal candidates for roles and succession planning. Activate for:
  talent match, internal mobility, internal candidate, succession planning,
  succession, who should be promoted, internal promotion, internal hire,
  talent pipeline, high potential, HIPO, development plan for promotion,
  readiness assessment, role fit, candidate assessment internal, compare
  candidates, talent review, career pathway, promotion readiness, who is
  ready for next level.
  NOT for: external recruiting pipeline (use recruiting-pipeline),
  compensation benchmarking (use comp-analysis), org restructuring
  (use org-planning).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/match"
---

## UNIVERSAL RULES (apply to every talent matching task)

- NEVER base a readiness assessment on tenure alone --
  years in role does not equal readiness for next role
- NEVER omit the motivation / career intent dimension --
  developing someone toward a role they do not want is wasteful
  and can backfire if the development leads to them leaving
- NEVER classify a gap as "NOT A FIT" without evidence --
  distinguish between "not ready" and "not suited"
- NEVER produce a talent assessment without the CONFIDENTIAL label
- NEVER share a talent assessment with the employee being assessed
  without explicit HR and manager review and decision
- NEVER make a specific promotion commitment in a talent assessment
  output -- these assessments inform decisions; they are not decisions
- ALWAYS include specific recommended actions for each candidate

## BEFORE IMPLEMENTATION

| Source            | Check                                                                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Conversation**  | Role requirements (critical, important, nice-to-have), candidate names and current roles, assessment context (vacancy, succession, or development mapping) |
| **hr.local.md**   | Performance review cycle dates, promotion cycle timing, internal mobility policy, competency framework in use                                              |
| **Prior outputs** | /jd output for the target role requirements (if a JD has been written for this role)                                                                       |

## CLARIFICATION QUESTIONS

**Required** (ask if not provided):

- What role or level are candidates being assessed for?
- Who are the candidates? (at least 2 names with current roles and tenure)
- Is this a current vacancy, succession planning, or development mapping?

**Optional** (ask if context suggests value):

- Is there a timeline urgency (e.g., current holder departing)?
- Are there specific competencies to weight more heavily than others?
- Has the organisation defined readiness criteria for this level?

**If information is missing**: Assess all six dimensions with equal weighting. Use standard readiness classifications. Note any dimensions where evidence is insufficient for a confident rating.

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          Internal Talent Assessment -- [Role Title]
DOCUMENT TYPE: Talent Assessment
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   CONFIDENTIAL -- HR AND HIRING MANAGER USE ONLY
```

## TALENT MATCHING WORKFLOW

### The Internal Mobility Imperative

External hiring costs 3-6x more than internal promotion. External hires
take 6-12 months to reach full productivity. Internal candidates who are
overlooked for growth either stagnate or leave -- taking institutional
knowledge with them.

Before any external job posting: assess internal candidates first.
Before any development conversation: map the internal mobility pathway.
The /match command supports both.

### Phase 1: Gather Requirements

Collect from user:

- Target role requirements (critical, important, nice-to-have)
- Candidates to assess (name, current role, years in role, known strengths/gaps)
- Context: is this a current vacancy, succession planning, or development mapping?

### Phase 2: Six-Dimension Assessment

For each candidate, assess against role requirements across:

DIMENSION 1: CRITICAL SKILLS (must-haves for the role)
Rating: DEMONSTRATED | DEVELOPING | ABSENT
Evidence required for DEMONSTRATED rating -- not just assertion

DIMENSION 2: EXPERIENCE (relevant background)
Rating: RELEVANT | PARTIAL | LIMITED
Note: experience gap can often be bridged with a structured plan

DIMENSION 3: PERFORMANCE TRAJECTORY
Rating: ASCENDING | CONSISTENT | VARIABLE
Note: trajectory matters as much as current level

DIMENSION 4: READINESS INDICATORS (signals of next-level capability)
Look for: instances of operating above current role level;
self-initiated work; peer/stakeholder recognition; problem-solving
in ambiguous situations

DIMENSION 5: DEVELOPMENT AREAS (gaps relative to target role)
Classify gap type:

- EXPERIENCE GAP: has the aptitude; needs the opportunity
- SKILL GAP: needs to build a specific capability
- MINDSET GAP: operates with assumptions that need to shift
  (Each gap type has different development interventions)

DIMENSION 6: MOTIVATION AND CAREER INTENT
Has this person expressed interest in this direction?
What is their stated career ambition?
Retention risk if they are not developed: HIGH / MEDIUM / LOW

### Phase 3: Readiness Classification

READY NOW: Can take the role immediately; development continues in role
READY IN 6 MONTHS: Specific gaps bridgeable with structured plan
READY IN 12 MONTHS:Meaningful development required; strong potential
DEVELOPING: Strong pipeline; not ready; invest for 18-24 months
NOT A FIT: Skills or motivation not aligned with this direction

### Phase 4: Recommendations

For each candidate:

- Specific action recommendation (have conversation, create plan, post externally)
- If READY IN N MONTHS: detailed development plan with timeline
- Retention risk assessment
- Succession conversation guidance if appropriate

## OUTPUT FORMAT

```
TASK:          Internal Talent Assessment -- [Role Title]
DOCUMENT TYPE: Talent Assessment
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL -- HR AND HIRING MANAGER USE ONLY

INTERNAL TALENT ASSESSMENT: [Role Title]
================================================================
[CONFIDENTIAL -- HR AND HIRING MANAGER USE ONLY]

ROLE REQUIREMENTS:
  Critical: [must-haves]
  Important: [significant but bridgeable]
  Nice-to-have: [list]

--- CANDIDATE: [Name] ------------------------------------------
  Current role: [Role, years]
  Fit assessment: [STRONG / DEVELOPING / NOT A FIT]
  Readiness: [classification]

  Critical requirements:
    [DEMONSTRATED/DEVELOPING/ABSENT] [Requirement]: [Evidence or gap]

  Important requirements:
    [DEMONSTRATED/DEVELOPING/ABSENT] [Requirement]: [Evidence or gap]

  Development gap: [Specific -- with gap type: experience/skill/mindset]
  Career intent: [What they expressed; motivation level]
  Retention risk: [HIGH / MEDIUM / LOW if not developed]

  RECOMMENDATION: [Specific action]

  Suggested development plan (if READY IN N MONTHS):
  [Specific actions with timeline]
-----------------------------------------------------------------
[Repeat for each candidate]

OVERALL RECOMMENDATION:
  [Priority order with rationale; action to take first]
================================================================
```

### Succession Conversation Guide

For HR/managers having career development conversations with
high-potential employees without making specific promises:

OPENING: Acknowledge their contribution and trajectory
MIDDLE: "We see you as someone with significant potential here
and we want to invest in your development"
Describe the pathway (not a promise)
Invite their input: "What does your career ambition look like?"
CLOSE: Agree one concrete next step
Set a follow-up date

NEVER SAY: "You will definitely be promoted in [date]"
ALWAYS SAY: "If [conditions] continue, [pathway] becomes realistic"

## NEVER DO THESE

- NEVER base a readiness assessment on tenure alone --
  years in role does not equal readiness for next role
- NEVER omit the motivation / career intent dimension --
  developing someone toward a role they do not want is wasteful
- NEVER classify a gap as "NOT A FIT" without evidence --
  distinguish between "not ready" and "not suited"
- NEVER produce a talent assessment without the CONFIDENTIAL label
- NEVER share a talent assessment with the employee being assessed
  without explicit HR and manager review and decision
- NEVER make a specific promotion commitment in a talent assessment
  output -- these assessments inform decisions; they are not decisions

## AUTHORITATIVE SOURCES

- CIPD (cipd.org) — Talent management and succession planning resources
- DDI (ddiworld.com) — Succession planning methodology, leadership readiness assessment
- Korn Ferry (kornferry.com) — Competency-based assessment framework, leadership potential model
- SHL (shl.com) — Occupational personality and ability assessment frameworks

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
