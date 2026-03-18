# Skill Boundary — Request Declined

**Requested task:** Market rate / salary benchmarking data for a Product Manager in San Francisco to set compensation bands.

**Skill invoked:** `/jd` (Job Description writing and improvement)

**Decision:** This request falls outside the scope of the `/jd` skill.

## Why This Was Declined

The `/jd` skill description explicitly defines its boundary:

> NOT for: ... compensation benchmarking (use comp-analysis).

The `/jd` skill writes and improves job descriptions with inclusive language. It does not:

- Perform market rate analysis or salary surveys
- Provide compensation benchmarking data
- Set or recommend compensation bands
- Analyse pay equity or salary positioning

## What the JD Skill Does With Compensation

The JD skill *requires* a salary range as an input — it enforces that every job description includes a specific salary range (never "competitive"). But it does not *generate* that range. The salary range must come from the user or from a compensation analysis tool.

## Recommended Route

Use the **comp-analysis** skill (referenced in the JD skill's own scope statement) for:

- Market rate data by role, level, and geography
- Compensation band design
- Salary benchmarking against market percentiles

Once you have the salary range from comp-analysis, bring it back to `/jd` to write the job description with that range included.

---

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
