# Stories Skill Benchmark — Iteration 1

## Summary

| Configuration | Pass Rate | Assertions Passed |
|---------------|-----------|-------------------|
| **with_skill** | **100%** | 22/22 |
| without_skill | 61% | 12/22 |
| **Delta** | **+39%** | **+10** |

## Per-Eval Breakdown

| Eval | with_skill | without_skill | Delta | Key Difference |
|------|-----------|---------------|-------|----------------|
| 1. stories-from-spec-date-filter | 7/7 (100%) | 2/7 (29%) | +71% | Without skill: no sizing, no dependencies, no coverage analysis, no error-state ACs, generic persona |
| 2. stories-from-prd-auth | 5/5 (100%) | 5/5 (100%) | 0% | Both produce high-quality auth stories. Without skill adds 2 unrequested stories (scope creep). |
| 3. negative-vague-persona | 4/4 (100%) | 0/4 (0%) | +100% | Without skill accepts "a user" as-is. With skill flags it as a blocker and explains why. |
| 4. negative-compound-ac | 4/4 (100%) | 3/4 (75%) | +25% | Without skill splits AC organically but doesn't explain why. With skill explicitly documents the split rationale. |
| 5. negative-sprint-planning | 2/2 (100%) | 2/2 (100%) | 0% | Both correctly redirect to /sprint-planning. Non-discriminating. |

## Analysis

### Where the skill adds the most value

1. **Quality enforcement** (eval 3): The skill's NEVER rules prevent "a user" as a persona. Without the skill, Claude accepts vague personas without question. This is the single biggest differentiator.

2. **Structural completeness** (eval 1): The skill enforces sizing (S/M/L), dependency mapping, and coverage analysis against the source spec. Without the skill, none of these appear.

3. **Error-state coverage** (eval 1): The skill requires at least one error-state AC per story. Without the skill, stories focus only on happy paths.

4. **Explicit rationale** (eval 4): When splitting compound ACs, the skill documents why the split was necessary. Without the skill, splits happen but silently.

### Where the skill adds no value

- **Auth stories** (eval 2): Claude's base model already produces excellent auth stories with proper personas, error states, and Given/When/Then format. The prompt itself specifies personas, which helps.
- **Scope boundaries** (eval 5): Both configurations correctly identify sprint planning as out-of-scope. The redirect behavior is already in Claude's base capabilities.

### Non-discriminating assertion

Eval 5 (sprint planning redirect) passes 100% in both configurations. This eval validates that the skill doesn't break boundary enforcement, but it doesn't demonstrate skill value. Consider removing from future benchmarks or replacing with a subtler scope-boundary test.
