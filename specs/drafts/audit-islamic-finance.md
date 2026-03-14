## Islamic Finance Compliance Report

### Summary
- Total skills audited: 13
- Total agents audited: 0
- Total violations found: 2
- Critical (invalid fields): 0
- Warning (best practice / content bug): 2

---

### Violations

#### `islamic-finance/skills/shariah-screening-global/SKILL.md`
- [ ] WARNING (content, not frontmatter): Line 11 contains an unexpanded shell substitution:
  `$(cat "/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag2/specs/chapter 20 islamic finance/islamic-finance-skills/products/shariah-screening-global.md" | tail -n +11)`
  This appears to be a stale authoring artifact — a shell command that was never executed or templated. The skill body is empty except for this line.
  - FIX: Replace with the actual skill content that was meant to be included.

#### `islamic-finance/skills/takaful-ifrs17/SKILL.md`
- [ ] WARNING (content, not frontmatter): Line 10 contains an unexpanded shell substitution:
  `$(cat "/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag2/specs/chapter 20 islamic finance/islamic-finance-skills/products/takaful-ifrs17.md" | tail -n +12)`
  Same issue as above — the skill body is empty except for this line.
  - FIX: Replace with the actual skill content that was meant to be included.

---

### Frontmatter Compliance — All 13 Skills

All 13 SKILL.md files passed S1–S28 checks. Specifically:

| File | S1 name | S2 len | S3 chars | S4 no edge hyphen | S5 no -- | S6 dir match | S7 desc | S8 desc len | S20–S27 invalid fields | S28 allowed-tools format |
|------|---------|--------|----------|-------------------|----------|--------------|---------|-------------|------------------------|--------------------------|
| islamic-finance-router | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| ijarah-imb | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| istisna-a | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| mudaraba | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| murabaha | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| musharaka-dm | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| musharaka-full | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| salam | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| shariah-screening-global | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| sukuk-investor | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| sukuk-issuer | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| takaful-ifrs17 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |
| zakat-global | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (none present) | PASS (not used) |

No invalid fields (`version`, `author`, `standard`, `background`, `memory`, `tools`, `skills`) found in any SKILL.md frontmatter. No `allowed-tools` fields present, so S28 is not applicable.

---

### plugin.json Compliance

`islamic-finance/.claude-plugin/plugin.json` — **PASS** (all P1–P18 rules)

| Rule | Field | Result |
|------|-------|--------|
| P1 / P17 | `name: "islamic-finance"` | PASS — present and non-empty |
| P2 | `version: "3.0.0"` | PASS |
| P3 | `description` | PASS |
| P4 | `author` (object with name/url) | PASS |
| P5 | `homepage` | PASS |
| P6 | `repository` | PASS |
| P7 | `license` | PASS |
| P8 | `keywords` (array of strings) | PASS |
| P9–P15 | `commands`, `agents`, `skills`, `hooks`, `mcpServers`, `outputStyles`, `lspServers` | Not present — no violation |
| P16 | No unknown fields | PASS |
| P18 | No skills/agents/commands declared, so no missing files | PASS |

Note: The plugin.json does not declare a `skills` array. The 13 skill directories exist on disk and are functional, but are not enumerated in plugin.json. This is not a P18 violation (P18 only checks declared entries against disk), but it may be intentional or an omission worth noting.

---

### Proposed Fixed Frontmatter

No frontmatter violations were found. No corrected YAML blocks are required.

The two warnings (content bugs in `shariah-screening-global` and `takaful-ifrs17`) require content replacement, not frontmatter changes.
