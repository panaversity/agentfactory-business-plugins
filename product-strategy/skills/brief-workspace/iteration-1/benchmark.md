# Benchmark: brief skill

## Summary

| Configuration | Pass Rate |
|---|---|
| with_skill | **100%** (25/25) |
| without_skill | **73%** (18/25) |
| **Delta** | **+27%** |

## Per-Eval Breakdown

| Eval | with_skill | without_skill | Delta |
|---|---|---|---|
| 1. problem-brief-activation-drop | 100% (7/7) | 57% (4/7) | +43% |
| 2. discovery-brief-enterprise-export | 100% (6/6) | 100% (6/6) | 0% |
| 3. initiative-brief-marketplace | 100% (6/6) | 83% (5/6) | +17% |
| 4. negative-solution-in-problem-brief | 100% (4/4) | 25% (1/4) | +75% |
| 5. negative-off-domain-code-request | 100% (2/2) | 100% (2/2) | 0% |

## Key Observations

- **with_skill achieves 100% pass rate** across all 5 evals (25/25 assertions passed)
- **without_skill achieves 73% average pass rate** (18/25 assertions passed), with high variance (0.25 to 1.0)
- **Eval 4** (solution-in-problem-brief) shows the **largest gap**: +75%. The skill's "no solutions in problem brief" rule is highly effective
- **Eval 2** (discovery-brief) is **non-discriminating**: both configurations pass 100%
- **Eval 5** (off-domain) is **non-discriminating**: both configurations handle correctly
- **Eval 1** (problem-brief) shows **moderate gap** (+43%): without the skill, Claude includes solutions and uses generic personas
- **Eval 3** (initiative-brief) shows **small gap** (+17%): only THE BET format was missed

## Discriminating Assertions

1. **"Contains no solution proposals"** — Most impactful. Without skill, Claude includes solutions when user provides them.
2. **"WHO IS AFFECTED references a named persona"** — Without skill, Claude uses generic "users".
3. **"DISCOVERY QUESTIONS contains 3-5 concrete questions"** — Without skill, different framing used.
4. **"THE BET section is one sentence"** — Format-specific convention unknown without skill.

## Non-Discriminating Assertions

- "Output is a [brief type]" — Claude identifies types from context
- "EVIDENCE includes quantified data" — Claude consistently quantifies
- "OUT OF SCOPE lists exclusions" — Claude includes naturally
- "Output includes a next step" — Claude consistently adds next steps
