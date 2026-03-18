# Skill Boundary — Request Declined

**Requested task:** Screen external CVs and rank the top 5 candidates for a Head of Data Science hire.

**Skill invoked:** `/match` (Internal Talent Assessment)

**Decision:** This request falls outside the scope of the `/match` skill.

## Why This Was Declined

The `/match` skill description explicitly defines its boundary:

> NOT for: external recruiting pipeline (use recruiting-pipeline).

The `/match` skill assesses **internal candidates** against roles using the organisation's direct evidence of their performance, trajectory, readiness indicators, and career intent. It does not:

- Screen CVs or resumes from external applicants
- Rank external candidates based on submitted application materials
- Evaluate candidates where the organisation has no direct performance evidence
- Manage an external recruiting pipeline or applicant tracking workflow

## Why Internal and External Assessment Are Different

Internal talent assessment (what `/match` does) relies on six dimensions that require **organisational evidence**: demonstrated critical skills observed in role, performance trajectory over time, readiness indicators visible to managers and peers, and known career intent from ongoing development conversations. None of this evidence exists for external candidates.

External candidate screening requires a fundamentally different methodology — resume parsing, credential verification, structured interview design, and reference-based assessment — which is what the recruiting pipeline skill is built for.

## Recommended Route

Use the **recruiting-pipeline** skill (referenced in the match skill's own scope statement) for:

- External CV screening and shortlisting
- Candidate ranking against role requirements
- Applicant pipeline management
- Interview scheduling and candidate progression tracking

If, after hiring externally, you want to assess **internal candidates** for the Head of Data Science role as part of succession planning or internal mobility, bring that request to `/match` with the candidates' names, current roles, and known strengths and gaps.

---

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
