---
name: reference
description: >
  Draft reference letters and verify employment. Activate for: reference
  letter, reference, employment reference, character reference, professional
  reference, write a reference, employment verification, confirm employment,
  verify employment, salary verification, dates of employment, job title
  verification, reference request, provide a reference, reference template,
  letter of recommendation, HR reference, factual reference.
  NOT for: performance reviews (use performance-review), offer letters
  (use draft-offer), job descriptions (use jd).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/reference"
---

## UNIVERSAL RULES (apply to every reference task)

- NEVER provide a reference that is inconsistent with the employee's
  documented performance record -- this creates legal and ethical risk
- NEVER include salary information without the employee's explicit consent
- NEVER provide a reference that you personally do not believe to be true
  -- if you cannot provide a positive reference, provide factual only
- NEVER send a reference without HR review, especially for former employees
  who left on difficult terms
- NEVER include information about disciplinary matters, health conditions,
  or protected characteristics in any reference
- ALWAYS include the "REVIEW BEFORE SENDING" warning in every output

## BEFORE IMPLEMENTATION

| Source            | Check                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Conversation**  | Employee name, reference type requested (factual/professional/verification), recipient and purpose if known                                |
| **hr.local.md**   | Reference policy (factual only vs professional permitted), company letterhead information, HR signatory details, rehire eligibility policy |
| **Prior outputs** | None — /reference is typically invoked independently                                                                                       |

## CLARIFICATION QUESTIONS

**Required** (ask if not provided):

- Who is the reference for? (employee name)
- What type of reference is needed? (factual / professional / employment verification)

**Optional** (ask if context suggests value):

- Who is the recipient and what is the purpose? (job application / mortgage / visa / rental)
- Has the employee given written consent for this reference?
- Is there specific information the recipient has requested?

**If information is missing**: Default to factual reference (safest option). State "defaulting to factual reference — confirm if a professional reference is required and authorised" in the output.

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          Reference Letter -- [Employee Name]
DOCUMENT TYPE: [Factual Reference / Professional Reference / Employment Verification]
JURISDICTION:  [From hr.local.md or user input]
CONFIGURATION: [hr.local.md loaded / best practices]
SENSITIVITY:   CONFIDENTIAL
```

## REFERENCE LETTER WORKFLOW

### Phase 1: Check Reference Policy

ALWAYS check before generating:

- Does this organisation's policy permit opinion references,
  or factual only? (Load from hr.local.md)
- Has the employee given written consent for this reference?
- Is the content consistent with the employee's documented performance?
- Has the reference been reviewed by HR before sending?

### Phase 2: Determine Reference Type

TYPE 1: FACTUAL REFERENCE (most common corporate policy)
Contents: job title, dates of employment, whether eligible for rehire
Policy in many organisations: HR provides factual only;
managers do not provide opinion references
ALWAYS CHECK: what is this organisation's reference policy
(from hr.local.md) before generating any content

TYPE 2: FULL PROFESSIONAL REFERENCE
Contents: factual + performance assessment + specific achievements

- professional recommendation
  Requirements: written authorisation from the employee;
  confirmation this is within the signer's authority

TYPE 3: EMPLOYMENT VERIFICATION LETTER
Contents: confirms current employment status, role, and salary
(for mortgage, visa, or rental applications)
Contents: role title; employment type; start date; current salary;
confirmation employment is ongoing as of letter date
NEVER include: future salary projections; pending bonuses unless confirmed

### Phase 3: Verify Facts

Verify all facts against HRIS before including:

- Exact dates of employment (start date and end date or "present")
- Exact job title (as it appears in the employment record)
- Salary: only include if employee has explicitly requested and consented
- Rehire eligibility: follow the organisation's policy and process

### Phase 4: Generate Reference

TONE:
Professional and neutral.
If providing a positive reference: specific and evidenced.
If unable to provide a positive reference: stick to factual only.
NEVER: be dishonest or misleading about performance.
NEVER: provide a reference you cannot stand behind.

LEGAL RISK:
Two types of legal risk with references:

1. Defamation: providing false negative information about an employee
2. Misrepresentation: providing falsely positive information that
   influences hiring decisions; if the new employer relies on this
   and is harmed, liability may exist
   In both cases: stick to what you know to be factually true.
   When in doubt: factual reference only.

## OUTPUT FORMAT

TYPE 1 -- FACTUAL REFERENCE:

```
TASK:          Reference Letter -- [Employee Name]
DOCUMENT TYPE: Factual Reference
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL

[Date]

To Whom It May Concern / [Named recipient if known]

Re: [Employee Full Name]

This letter confirms that [Full Name] was employed by [Company Name]
as [Job Title] from [Start Date] to [End Date / "the present"].

[Their employment is ongoing as of the date of this letter. /
 They left the organisation on [date].]

[OPTIONAL -- only if organisation policy permits and it is true:
 [Name] is eligible for re-employment at [Company Name].]

This reference is provided in a factual capacity only. For further
information, please contact [HR contact name, email].

Yours sincerely,
[Name, Title -- HR only for factual references]

WARNING: REVIEW BEFORE SENDING -- This reference must be reviewed by HR
before sending. Verify all facts against HRIS. Remove this note
before issuing.
```

TYPE 2 -- FULL PROFESSIONAL REFERENCE:

```
TASK:          Reference Letter -- [Employee Name]
DOCUMENT TYPE: Professional Reference
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL

[Date]

[Recipient name and address]

Dear [Name / To Whom It May Concern],

Re: Reference for [Employee Full Name]

[Paragraph 1: Relationship -- how long; in what capacity]
[Paragraph 2: Performance -- 2-3 specific achievements with evidence]
[Paragraph 3: Character and ways of working -- specific and honest]
[Paragraph 4: Recommendation -- genuine and proportionate]

I am happy to discuss this reference further if helpful.

Yours sincerely,
[Name, Title, Contact details]

WARNING: REVIEW BEFORE SENDING -- This reference must be reviewed by HR
before sending. Verify all facts against HRIS. Remove this note
before issuing.
```

TYPE 3 -- EMPLOYMENT VERIFICATION:

```
TASK:          Employment Verification -- [Employee Name]
DOCUMENT TYPE: Employment Verification
JURISDICTION:  [Jurisdiction]
CONFIGURATION: [hr.local.md status]
SENSITIVITY:   CONFIDENTIAL

[Date]

To Whom It May Concern,

Re: Employment Verification -- [Employee Full Name]

This letter confirms that [Full Name] is currently employed by
[Company Name] as [Job Title] on a [full-time/part-time] basis.

Start date: [Date]
Current annual salary: [Amount -- only if employee has consented]

This employment is ongoing as of the date of this letter.

For further information, please contact [HR contact name, email].

Yours sincerely,
[Name, Title]

WARNING: REVIEW BEFORE SENDING -- This reference must be reviewed by HR
before sending. Verify all facts against HRIS. Remove this note
before issuing.
```

## NEVER DO THESE

- NEVER provide a reference that is inconsistent with the employee's
  documented performance record -- this creates legal and ethical risk
- NEVER include salary information without the employee's explicit consent
- NEVER provide a reference that you personally do not believe to be true
  -- if you cannot provide a positive reference, provide factual only
- NEVER send a reference without HR review, especially for former employees
  who left on difficult terms
- NEVER include information about disciplinary matters, health conditions,
  or protected characteristics in any reference

## AUTHORITATIVE SOURCES

- ACAS (acas.org.uk) — Guidance on providing references (UK employment law perspective)
- SHRM (shrm.org) — Reference checking toolkit, best practices for providing employment references
- Spring v Guardian Assurance [1995] 2 AC 296 — UK case law establishing duty of care in employment references
- CIPD (cipd.org) — Employment references guidance for HR practitioners

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
