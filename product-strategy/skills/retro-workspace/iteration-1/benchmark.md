# Skill Benchmark: retro

**Model**: claude-opus-4-6
**Date**: 2026-03-19
**Evals**: 4 (1 run each per configuration)

## Summary

| Metric | with_skill | without_skill | Delta |
|--------|------------|---------------|-------|
| Pass Rate | 100% | 18.75% | **+81.25%** |
| Assertions Passed | 16/16 | 3/16 | +13 |

## Per-Eval Breakdown

| Eval | with_skill | without_skill | Delta |
|------|-----------|---------------|-------|
| retro-quick-reports | 7/7 (100%) | 1/7 (14%) | +86% |
| retro-successful-launch | 4/4 (100%) | 2/4 (50%) | +50% |
| negative-no-outcome-data | 3/3 (100%) | 0/3 (0%) | +100% |
| negative-stakeholder-update | 2/2 (100%) | 0/2 (0%) | +100% |

## Analyst Observations

1. **Perfect skill performance**: The retro skill achieves 100% pass rate across all 16 assertions. The four-question framework (Q1-Q4) reliably structures output with data-driven verdicts, metrics quality evaluation, specific process improvements, and actionable follow-ups.

2. **Strongest differentiation on structure and guardrails**: Without the skill, the model produces generic "What Went Well / What Didn't Go Well" retros that miss critical elements:
   - No metrics quality evaluation (Q3) — the most valuable retro section
   - No specific, enforceable process changes — only vague intentions
   - No PRODUCT.LOCAL.MD configuration updates
   - No owners or due dates on action items

3. **Negative evals show the biggest gap**: Without the skill, the model is a people-pleaser — it complies with requests it should push back on (running a retro with no data) and produces content outside its domain (stakeholder updates). The skill's NEVER rules and COMPLEMENTARY WORKFLOWS section provide critical guardrails.

4. **One non-discriminating assertion**: "Uses actual data" passes in both configurations (eval 1). This tests baseline LLM capability, not skill value. Consider removing or replacing with a more discriminating assertion.

5. **Successful-launch eval is the weakest differentiator**: The without-skill output still passes 50% of assertions here, suggesting the skill adds less value when the scenario is straightforward. The skill's unique value on success retros is extracting *replicable process patterns* — something generic retros consistently miss.
