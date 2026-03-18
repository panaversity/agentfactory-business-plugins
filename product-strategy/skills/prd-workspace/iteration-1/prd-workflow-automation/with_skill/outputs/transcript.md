# PRD Generation Transcript — Workflow Automation

**Date**: 2026-03-19
**Skill used**: `/prd` (product-strategy plugin, v1.0)
**Input**: "Write a PRD for our Workflow Automation feature. This is a major new product area that will require work from the platform team, the integrations team, and the frontend team. Target delivery is Q3. The feature lets users create automated workflows triggered by data events."

---

## Steps Taken

### 1. Read the skill file
- Read `/product-strategy/skills/prd/SKILL.md` to understand the 10-section PRD template, status gates, and "never do" rules.
- Noted the skill requires `product.local.md` for context loading (personas, engineering team, stakeholders, terminology).

### 2. Checked for product.local.md
- Searched for `product.local.md` in the product-strategy directory. **Not found** — only the `.template` file exists.
- Per skill instructions: "If not configured, ask the user for product name, personas, and engineering context." However, the task required autonomous execution, so I proceeded with reasonable assumptions and clearly labelled them.

### 3. Read supporting context
- Read `product.local.md.template` to understand what fields would normally be populated.
- Read `CLAUDE.md` (plugin instructions) for Layer 1/Layer 2 architecture, context loading rules, spec quality rules, and universal rules.
- Read `README.md` for plugin overview and workflow patterns.

### 4. Wrote the PRD
- Followed the 10-section template exactly as defined in the skill:
  1. Executive Summary (What/Why/When/Win)
  2. Business Context (problem statement, commercial evidence, strategic fit, success metrics with failure threshold)
  3. User Requirements (two personas, user stories, journey map)
  4. Functional Requirements (8 features with MoSCoW — 4 MUST, 2 SHOULD, 2 COULD = 50% MUST, within the 60% ceiling)
  5. Non-Functional Requirements (performance, reliability, security, compliance, accessibility, scalability)
  6. Technical Architecture Notes (with note that engineering lead must review before REVIEW status)
  7. Go-to-Market Requirements (docs, CS enablement, sales enablement, pricing, beta programme, comms)
  8. Launch Plan (phased rollout, rollback plan, feature flags, monitoring)
  9. Dependencies and Risks (6 dependencies, 6 risks with mitigations)
  10. Open Questions (7 questions with owners and due dates)
- Included appendices: competitive landscape, user research excerpts (illustrative), technical discovery (TBD), prior art.

### 5. Compliance with skill rules
- **Named personas**: Used "Ops Olivia" and "Dev Darius" (labelled as assumptions since no product.local.md exists).
- **No "a user"**: All requirements reference named personas.
- **Failure threshold defined**: <10% adoption at 6 months or <98% reliability triggers re-evaluation.
- **MUST items are genuinely must-ship**: All 4 MUST features are essential for a viable product.
- **Status set to DRAFT**: Sections present but several contain assumptions that need validation.
- **Engineering sign-off note**: Section 6 explicitly flagged as requiring engineering lead review.
- **Mandatory output header**: Included at top of document per CLAUDE.md instructions.

### 6. Key assumptions flagged
- All commercial evidence (deal counts, ticket volumes, ARR estimates) is illustrative — labelled for replacement with real data.
- Persona names are illustrative — should be replaced with named personas from product.local.md when configured.
- User research quotes are illustrative — should be replaced with actual research.

## Output
- **PRD**: `outputs/prd.md` (DRAFT status, 10 sections + appendices, ~350 lines)
- **Transcript**: `outputs/transcript.md` (this file)

## What's Needed to Move to REVIEW Status
1. Replace illustrative commercial evidence with real data
2. Configure `product.local.md` and replace assumed persona names
3. Engineering lead reviews and confirms Section 6 (Architecture Notes)
4. Resolve all 7 Open Questions (owners and due dates assigned)
5. Replace illustrative user research quotes with actual research excerpts
