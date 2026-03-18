# PRD Skill Benchmark Results

**Skill**: prd
**Date**: 2026-03-19
**Model**: claude-opus-4-6
**Evals**: 4 (2 positive + 2 negative)

## Summary

| Configuration | Pass Rate | Assertions Passed |
|---------------|-----------|-------------------|
| **with_skill** | **100%** | 17/17 |
| without_skill | 29.4% | 7/17 (mean across evals) |
| **Delta** | **+70.6%** | |

## Per-Eval Results

| Eval | Type | With Skill | Without Skill | Delta |
|------|------|-----------|---------------|-------|
| prd-workflow-automation | Positive | 8/8 (100%) | 3/8 (37.5%) | +62.5% |
| prd-ai-search-platform | Positive | 5/5 (100%) | 4/5 (80%) | +20% |
| negative-single-feature-spec | Negative | 2/2 (100%) | 0/2 (0%) | +100% |
| negative-roadmap-planning | Negative | 2/2 (100%) | 0/2 (0%) | +100% |

## Key Findings

1. **Perfect scope discrimination**: The skill correctly declined both negative evals (single-feature spec redirected to /write-spec, roadmap planning redirected to /roadmap-update). Without the skill, Claude has no concept of when NOT to write a PRD — it just answers whatever is asked.

2. **Structural completeness**: The skill enforces the 10-section PRD template consistently. Without it, Claude produces good-quality but structurally inconsistent PRDs (custom section structures, missing GTM, missing failure thresholds).

3. **MoSCoW enforcement**: The skill always uses MoSCoW prioritization with explicit percentage tracking. Without it, Claude defaults to P0/P1/P2 — a different scheme that doesn't enforce the 60% MUST ceiling.

4. **Named personas**: The skill creates named personas (Ops Olivia, Dev Darius, Dana) even when product.local.md is absent. Without it, Claude uses generic role descriptions.

5. **Baseline is decent for complex topics**: On eval 2 (AI search platform), without-skill scored 80% — Claude naturally includes scope boundaries, dependencies, and domain-specific risks for complex technical topics. The skill's added value is in consistency and completeness, not in raw quality for straightforward cases.

## Assertion Discrimination Analysis

- **Non-discriminating assertions**: "Tech architecture notes present" and "DRAFT status" pass in both configurations — these don't differentiate skill value.
- **Highly discriminating**: Scope discrimination (negative evals), MoSCoW enforcement, named personas, failure thresholds, GTM section — these only pass with the skill.

## Viewer

Static HTML report at: `/tmp/prd-eval-review.html`
