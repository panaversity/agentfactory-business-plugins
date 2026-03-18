# PRD Skill — Task Declined

## Request

"Write a spec for adding a dark mode toggle to our settings page. It's one feature for the frontend team, should take about a sprint."

## Skill Decision: DECLINED — Wrong Tool

The `/prd` skill explicitly excludes this type of request. The task describes:

- **One feature** (dark mode toggle)
- **One team** (frontend)
- **One sprint** (~2 weeks)

The skill's routing logic (lines 30-34) is unambiguous:

> **Write a SPEC when:** One feature, one team, one-to-three sprints
> **Write a PRD when:** Multiple features, multiple teams, major platform change, new product area, or executive alignment required

The skill's description metadata (line 9) also explicitly excludes this:

> NOT for: single-feature specifications (use official `/write-spec`)

## Recommended Action

Use the **`/write-spec`** skill instead, which is designed for single-feature specifications scoped to one team and one-to-three sprints.

A PRD is a cross-functional alignment document for multi-team initiatives. Using it for a single feature toggle would produce unnecessary overhead — sections like Go-to-Market Requirements (Section 7), Launch Plan with phased rollout (Section 8), and multi-team dependency tables (Section 9) are not meaningful for a settings page toggle owned by one frontend team in one sprint.

## What Would Happen If We Forced It

If the PRD template were applied anyway, the result would be:

- **Sections 1-4**: Useful but over-structured for the scope
- **Sections 5-6**: Partially useful (accessibility, feature flags)
- **Section 7 (GTM)**: Mostly N/A — no sales enablement or pricing changes for a dark mode toggle
- **Section 8 (Launch Plan)**: Over-engineered — a settings toggle doesn't need a phased beta programme
- **Section 9 (Dependencies)**: Empty or trivial — one team, no external dependencies
- **Section 10 (Open Questions)**: Could be useful but doesn't require PRD ceremony

The skill is correctly designed to prevent this kind of scope mismatch.
