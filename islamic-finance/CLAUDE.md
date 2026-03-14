# Islamic Finance Plugin — Development Guide

## Identity

v3.0.0 — Islamic Finance Domain Agent plugin for Cowork.

## Architecture

1 router skill + 12 product skills + 13 jurisdiction overlays + 4 commands.

The router (`skills/islamic-finance-router/SKILL.md`) identifies jurisdiction and product from queries, then loads the correct product skill and jurisdiction overlay. Products are standalone skills that auto-activate through the router.

## Key Files

- `skills/islamic-finance-router/SKILL.md` — routing logic
- `skills/islamic-finance-router/references/jurisdictions/*.md` — 13 overlays
- `skills/islamic-finance-router/references/aaoifi-fas-reference.md` — AAOIFI FAS lookup
- `skills/islamic-finance-router/references/global-standards-map.md` — 20-jurisdiction map
- `commands/*.md` — 4 domain commands
- `hooks/hooks.json` — SessionStart + PostToolUse hooks
- `evals/` — golden file tests
- `scripts/validate-routing.py` — routing validation

## Universal Rules

- NEVER use "interest income" — use jurisdiction-appropriate label
- NEVER use "loans and advances" in AAOIFI jurisdictions
- NEVER make Shariah compliance judgments — escalate to SSB
- Every output must have GOVERNING FRAMEWORK / PRODUCT / JURISDICTION header
