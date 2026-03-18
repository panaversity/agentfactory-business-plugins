---
name: jd
description: >
  Write and improve job descriptions with inclusive language. Activate for:
  job description, JD, job posting, role description, job advert, vacancy
  description, job specification, person specification, write a job description,
  improve job description, inclusive job description, job requirements, role
  requirements, hiring, recruiting, talent acquisition, position description,
  role profile, what to put in job description.
  NOT for: interview questions or scorecards (use interview-prep),
  offer letters (use draft-offer), compensation benchmarking (use comp-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/jd"
---

## UNIVERSAL RULES (apply to every job description task)

- NEVER produce a JD with salary listed as "competitive" --
  always include a range; omitting the range deters good candidates
- NEVER list more than 5 essential requirements without questioning
  whether all are genuinely essential
- NEVER use "rockstar", "ninja", "guru" or similar --
  these are exclusionary and have no descriptive value
- NEVER omit the equal opportunities statement
- NEVER omit the reasonable adjustments offer --
  this is both good practice and a legal requirement in many jurisdictions
- NEVER write requirements in terms of years of experience with a
  specific tool when you mean proficiency at a skill level
- ALWAYS apply the inclusive language check automatically to every JD

## BEFORE IMPLEMENTATION

| Source            | Check                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| **Conversation**  | Role details (title, department, seniority level), team context, salary range, location and working pattern |
| **hr.local.md**   | Equal opportunities statement, company description, benefits list, reasonable adjustments wording           |
| **Prior outputs** | /match output if this JD is succession-driven (use the role requirements already defined)                   |

## CLARIFICATION QUESTIONS

**Required** (ask if not provided):

- What is the role title and seniority level?
- Which team or department is this role in?
- What does this person actually do (the work, not the requirements)?

**Optional** (ask if context suggests value):

- What is the salary range for this role?
- Is this role remote, hybrid, or office-based?
- Are there specific technical skills or tools required?

**If information is missing**: Use hr.local.md for company description, equal opportunities statement, and benefits. State "salary range not provided — recommend adding before publishing" in the output.

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          Job Description -- [Role Title]
DOCUMENT TYPE: Job Description
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   ROUTINE
```

## JOB DESCRIPTION WORKFLOW

### The Four JD Principles

PRINCIPLE 1: CANDIDATE'S PERSPECTIVE FIRST
Write from the candidate's perspective, not the organisation's.
"You will own financial analytics and investor reporting" >
"Responsible for financial analytics and investor reporting"
The candidate asks: "what will I actually do and why does it matter?"
Answer that question first.

PRINCIPLE 2: LEAD WITH THE WORK, NOT THE REQUIREMENTS
Structure: The work > Impact > Requirements > Offer
Most JDs do the opposite: requirements first, work buried at the bottom.
Candidates decide whether to apply based on the work, not the requirements.
Put the work first.

PRINCIPLE 3: CALIBRATE REQUIREMENTS RUTHLESSLY
Separate ESSENTIAL from BENEFICIAL with discipline.
Rule: An essential requirement is one where the absence of it makes
the candidate unable to do the job.
Everything else is BENEFICIAL.
Most JDs list 15 "essential" requirements. Most have 3-5 genuine ones.
Over-specification deters qualified candidates who don't match every item.

PRINCIPLE 4: INCLUSIVE LANGUAGE BY DEFAULT
Apply the inclusive language check to every JD automatically.
Do not wait to be asked.

### Phase 1: Gather Information

Collect from user or hr.local.md:

- Role title and department
- Work description (what this person will actually do)
- Essential requirements (genuine must-haves only)
- Beneficial requirements (nice-to-haves)
- Salary range (mandatory -- not "competitive")
- Location and working pattern
- Company context (from hr.local.md or user input)

### Phase 2: Structure the JD

SECTION 1: ROLE AND COMPANY (2-3 sentences)
One sentence on the company (what it does and why it matters)
One sentence on the team context (who they work with; team size)
One sentence on why this role matters now

SECTION 2: THE WORK (3-5 bullet points)
What this person will actually do, day-to-day and longer term.
Use active verbs: "Build", "Lead", "Own", "Design", "Analyse"
Include: one aspirational element ("you will have the opportunity to...")
Avoid: task lists that sound like a job manual

SECTION 3: WHAT WE'RE LOOKING FOR
Essential (3-5 items maximum -- enforce this):

- [Skill or quality] -- explain why it is essential if not obvious
  Beneficial (not required):
- [Items that would help but are not blockers]
  Character / ways of working:
- [1-2 items about how they work, not what they know]

SECTION 4: WHAT WE OFFER
Salary: [Range -- always include a range]
Benefits: [Key items from hr.local.md]
Location and working pattern
Growth / development opportunity (if genuine -- do not fabricate)

SECTION 5: HOW TO APPLY + EQUAL OPPORTUNITIES
Application instructions
Equal opportunities statement (load standard from hr.local.md)
Reasonable adjustments offer (always include)

### Phase 3: Inclusive Language Check

Apply to every JD without being asked:

REMOVE these words/phrases:
Gender-coded masculine: "rockstar", "ninja", "guru", "dominate",
"aggressive growth", "crushing it", "killing it", "hunt"
Gender-coded feminine: "nurturing", "collaborative" as the only descriptor
Age-coded: "young and dynamic", "recent graduate" (unless required),
"digital native", "energetic young team"
Unnecessary specificity: "5 years in [specific tool]" (replace with
"proficiency in [tool category]"); "degree in [specific subject]"
unless genuinely required
Requirements that mask experience bias: "culture fit" (too vague;
replace with specific behaviours); "startup experience required"
unless genuinely relevant

FLAG for review:
Any requirement listed as essential with a years-of-experience
threshold that could be replaced with a skills/competency description.
Years of experience predicts tenure, not ability.

ALWAYS INCLUDE:
Salary range (or "competitive" is not acceptable -- be specific)
Reasonable adjustments offer
Equal opportunities statement
Hybrid/remote flexibility if it exists

### Phase 4: Requirements Calibration Test

Before finalising the essential requirements list:
For each "essential" item, ask:
"Could a highly capable candidate do this job well without this?"
If YES -> move to BENEFICIAL
If NO -> keep as ESSENTIAL

Rule: If your essential list has more than 5 items, at least 2 of them
are almost certainly BENEFICIAL masquerading as ESSENTIAL.

## OUTPUT FORMAT

```
TASK:          Job Description -- [Role Title]
DOCUMENT TYPE: Job Description
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   ROUTINE

[ROLE TITLE] -- [DEPARTMENT]
[Company] | [Location] | [Salary Range]

THE WORK
[3-5 bullet points, active verbs, candidate perspective]

WHAT WE'RE LOOKING FOR
Essential:
  - [Requirement -- why it is essential if not obvious]
Beneficial (not required):
  - [Item]
Character / ways of working:
  - [1-2 items]

WHAT WE OFFER
  [Salary, benefits, location, growth]

HOW TO APPLY
  [Instructions]
  [Equal opportunities statement from hr.local.md]
  [Reasonable adjustments offer]

INCLUSIVE LANGUAGE CHECK:
  [Pass/Fail with specific findings]
  [Requirements calibration status]
```

## NEVER DO THESE

- NEVER produce a JD with a salary listed as "competitive" --
  this is the single most effective way to deter good candidates
- NEVER list more than 5 essential requirements without questioning
  whether all 5 are genuinely essential
- NEVER use "rockstar", "ninja", "guru" or similar -- these are
  exclusionary and have no descriptive value
- NEVER omit the equal opportunities statement
- NEVER omit the reasonable adjustments offer -- this is both good
  practice and a legal requirement in many jurisdictions
- NEVER write requirements in terms of years of experience with a
  specific tool when you mean proficiency at a skill level

## AUTHORITATIVE SOURCES

- CIPD (cipd.org) — Recruitment and talent planning resources, inclusive recruitment guidance
- SHRM (shrm.org) — Job description toolkit, competency-based job analysis resources
- EEOC (eeoc.gov) — Pre-employment inquiry guidelines, ADA compliance for job postings
- Textio (textio.com) — Research on inclusive language impact in job descriptions

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
