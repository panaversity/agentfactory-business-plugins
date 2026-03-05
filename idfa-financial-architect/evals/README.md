# IDFA Eval Harness

Two-tier evaluation system for the IDFA Financial Architect skill.

## Architecture

**Tier 1 — Deterministic checks** (code-based, ungameable):

- `g1_named_ranges` — Zero coordinate references in formulas
- `g3_intent_notes` — Every formula has an intent note comment
- `g4_layer_isolation` — No hardcoded constants in calculation formulas
- `artifact_delta` — Named range values changed correctly after whatif/goalseeking
- `target_reached` — Goal-seeking output within tolerance of target
- `layer_separation` — Inp\_\* ranges on Assumptions sheet, calc ranges on Calculations
- `row_insertion` — Named range outputs unchanged after row insertion

**Tier 2 — LLM judges** (subjective quality via `claude -p` headless):

- `decision_ready` — Could a CFO take this to the board?
- `risk_awareness` — Does the output surface assumptions and limitations?
- `handover_safe` — Could someone else pick this up tomorrow?
- `scope_control` — Does the agent refuse out-of-scope requests?

## Usage

```bash
# Full eval (all 11 cases)
uv run evals/run.py

# Single case (fast iteration)
uv run evals/run.py --case build_gp_waterfall --verbose

# Judge calibration (verify judges agree with golden labels)
uv run evals/run.py --calibrate

# Stability check (3 runs, flag flipping judges)
uv run evals/run.py --runs 3
```

## Reading Results

Console output shows pass/fail per case, aggregated by operation and check type.
JSON results are written to `evals/results/` (gitignored) with a `latest.json` symlink.

```bash
cat evals/results/latest.json | python -m json.tool
```

## Test Cases

| ID                     | Operation    | What It Tests                          |
| ---------------------- | ------------ | -------------------------------------- |
| `build_gp_waterfall`   | build        | Create compliant model from scratch    |
| `audit_compliant`      | audit        | Correctly identify a clean model       |
| `audit_violations`     | audit        | Correctly identify specific violations |
| `retrofit_legacy`      | retrofit     | Fix violations (FAIL -> PASS)          |
| `whatif_revenue`       | whatif       | Change input, verify delta             |
| `goalseeking_gp`       | goalseeking  | Iterate to target output               |
| `explain_formula`      | explain      | Plain-language formula explanation     |
| `negative_tax`         | negative     | Refuse tax question                    |
| `negative_invest`      | negative     | Refuse investment advice               |
| `negative_accounting`  | negative     | Refuse accounting guidance             |
| `row_insertion_robust` | programmatic | Named ranges survive row insertion     |

## Adding Cases

Add entries to `cases.yaml`. Each case needs:

- `id`, `operation`, `prompt`
- `fixture` (optional path relative to repo root)
- `tier1_checks` (list of check names)
- `tier2_judges` (list of judge names)
- Operation-specific fields: `expected_delta`, `target`, `expected_audit_result`, etc.

## Adding Judges

Create a `.txt` file in `evals/graders/` following the 4-component structure:

1. Task + Criterion
2. Pass/Fail definitions (operation-aware)
3. Few-shot examples (2 PASS + 2 FAIL)
4. Output format (JSON schema enforced)

Then add golden calibration examples in `evals/golden/` with format `{grader}_{pass|fail}_{n}.txt`.
