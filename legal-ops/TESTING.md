# Pre-Merge Smoke Test Protocol

## Context

This plugin (v2.0.0) deleted duplicate skills (`jurisdiction-contract-review`, `jurisdiction-nda-triage`) and colliding commands (`/review-contract`, `/triage-nda`, `/vendor-check`). Contract review and NDA triage are now handled by Anthropic's Layer 1 plugin. Panaversity provides jurisdiction overlays and orchestration wrappers.

**These tests MUST pass before merging.**

---

## Test 1: Anthropic Layer 1 — Jurisdiction Overlay Fires

Install both plugins in Cowork (Anthropic legal + Panaversity legal-ops).

```
Use /review-contract to review this SaaS vendor agreement under English law.
The vendor limits liability to 3 months' fees. We are the customer.
```

**Pass criteria:**

- Output references UCTA (Unfair Contract Terms Act 1977)
- Output references `uk-law.md` overlay or UK-specific statutory framework
- Output includes mandatory header block (TASK, JURISDICTION, ATTORNEY REVIEW)

```
Use /triage-nda for this mutual NDA with a German company under German law.
Standard mutual form, 3-year term, no residuals clause.
```

**Pass criteria:**

- Output references `eu-law.md` overlay or EU-specific framework
- Output produces Tier classification
- Output includes attorney review disclaimer

**If overlays do NOT fire:** Do not merge. The router needs adjustment to ensure overlays load even when Anthropic handles the core review/triage.

---

## Test 2: `/contract-intake` Wrapper Handoff

```
/contract-intake "SaaS vendor agreement from UK company" "English law" "We are the customer, GBP 48K annual"
```

**Pass criteria:**

- Assigns reference ID
- Classifies as vendor agreement → routes to Anthropic's `/review-contract`
- Jurisdiction overlay (uk-law.md) is loaded before handoff
- Triage tier is assigned after review
- Communication template is suggested

```
/contract-intake "incoming NDA from German technology partner" "German law" "Mutual NDA, need response by Friday"
```

**Pass criteria:**

- Classifies as NDA → routes to Anthropic's `/triage-nda`
- EU overlay loads
- Tier classification produced

---

## Test 3: `/compliance-calendar` Standalone

```
/compliance-calendar scope:"all active contracts" filter:"obligations due within 60 days"
```

**Pass criteria:**

- Produces RED/YELLOW/GREEN dashboard format
- Escalation timeline referenced
- Attorney review disclaimer present

---

## Test 4: `/legal-brief` Domain Routing

```
/legal-brief topic:"patent landscape analysis" subject:"AI document analysis" jurisdictions:"US, EU, UK"
```

**Pass criteria:**

- Routes to `ip-protection` skill
- Jurisdiction overlays load
- Output is IP research brief format (not general briefing)

---

## Structural Verification (automated)

```bash
# No Panaversity command files for Anthropic-owned names
ls commands/  # Should list: compliance-calendar.md, contract-intake.md, legal-brief.md

# No plugin-commands declarations in any SKILL.md
grep -r 'plugin-commands' skills/  # Should return 0 results

# No stale skill directories
ls skills/  # Should NOT contain jurisdiction-contract-review or jurisdiction-nda-triage

# Evals pass
uv run evals/run-evals.py  # Should print PASSED
```
