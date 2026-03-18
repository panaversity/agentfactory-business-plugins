# Prioritise Skill Benchmark Results

## Summary

| Configuration | Pass Rate | Assertions Passed |
|---|---|---|
| **with_skill** | **100%** (20/20) | 20/20 |
| **without_skill** | **20%** (4/20) | 4/20 |
| **Delta** | **+80%** | +16 |

## Per-Eval Breakdown

### Eval 1: RICE Scoring Backlog (7 assertions)

| Assertion | With Skill | Without Skill |
|---|---|---|
| RICE table with all columns | PASS | PASS |
| Scoring assumptions visible | PASS | FAIL |
| Strategic Override Test | PASS | FAIL |
| Data Gap Test | PASS | FAIL |
| What Would We Regret test | PASS | FAIL |
| EXPLICITLY NOT BUILDING list | PASS | FAIL |
| Discovery spike recommended | PASS | FAIL |

**With skill: 7/7 (100%) | Without skill: 1/7 (14%)**

### Eval 2: Single Feature Evaluation (5 assertions)

| Assertion | With Skill | Without Skill |
|---|---|---|
| Uses single feature format | PASS | FAIL |
| Includes opportunity cost | PASS | FAIL |
| Frequency of request assessed | PASS | PASS |
| Confidence rated with basis | PASS | FAIL |
| Structured recommendation | PASS | FAIL |

**With skill: 5/5 (100%) | Without skill: 1/5 (20%)**

### Eval 3: Value vs Effort Quick Sort (4 assertions)

| Assertion | With Skill | Without Skill |
|---|---|---|
| Uses Value vs Effort matrix | PASS | PASS |
| Items in four quadrants | PASS | PASS |
| Assumptions visible | PASS | FAIL |
| Three mandatory challenges | PASS | FAIL |

**With skill: 4/4 (100%) | Without skill: 2/4 (50%)**

### Eval 4: Negative -- Sprint Planning (2 assertions)

| Assertion | With Skill | Without Skill |
|---|---|---|
| Does NOT perform sprint planning | PASS | FAIL |
| Redirects to /sprint-planning | PASS | FAIL |

**With skill: 2/2 (100%) | Without skill: 0/2 (0%)**

### Eval 5: Negative -- Metrics Review (2 assertions)

| Assertion | With Skill | Without Skill |
|---|---|---|
| Does NOT review metrics | PASS | FAIL |
| Redirects to /metrics-review | PASS | FAIL |

**With skill: 2/2 (100%) | Without skill: 0/2 (0%)**

## Analyst Observations

1. **Three mandatory challenges are the strongest differentiators** -- Strategic Override, Data Gap, and What Would We Regret tests NEVER appear without the skill and ALWAYS appear with it.
2. **Negative evals show perfect boundary enforcement** -- With skill, the agent correctly redirects to complementary workflows. Without skill, it answers directly (wrong behavior).
3. **Claude has baseline PM knowledge** -- Without the skill, Claude can produce a RICE table and Value vs. Effort quadrants. The skill's value is in the structured challenge framework that catches scoring errors.
4. **One non-discriminating assertion**: "Frequency of request assessed" (eval 2) passes in both configurations. Claude naturally flags single-customer churn threats.
5. **Assumptions visibility consistently differentiates**: With skill, detailed rationale is always shown. Without skill, raw numbers only.
