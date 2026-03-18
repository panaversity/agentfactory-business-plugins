# Roadmap Planning — Skill Mismatch Detected

## What You Asked

You asked for help planning the Q3/Q4 product roadmap — deciding which initiatives to pursue and in what order.

## Why the PRD Skill Cannot Help Here

The `/prd` skill is designed for writing **Product Requirements Documents** for individual multi-team initiatives. Its scope description explicitly states:

> **NOT for:** roadmap planning (use official `/roadmap-update`)

And in its complementary workflows section:

> Roadmap placement: use official `/roadmap-update`

Roadmap planning (prioritizing across initiatives, sequencing work, allocating capacity across quarters) is a fundamentally different activity from documenting the requirements of a single initiative. The PRD skill handles depth on one initiative; roadmap planning handles breadth across many.

## What You Should Use Instead

**`/roadmap-update`** — the official roadmap planning skill referenced by the PRD skill. This is the correct tool for:

- Evaluating which initiatives to pursue
- Prioritizing and sequencing across Q3 and Q4
- Allocating engineering capacity across initiatives
- Making trade-off decisions between competing priorities

## How PRD and Roadmap Planning Work Together

The correct workflow sequence is:

1. **`/roadmap-update`** — Decide *which* initiatives make the roadmap and *when*
2. **`/prd`** — For each approved initiative, write the full requirements document
3. **`/sprint-planning`** — Break approved PRDs into sprint-level work

The PRD skill is the right tool for step 2, after you've already decided what belongs on the roadmap.

## Recommendation

Use `/roadmap-update` to plan your Q3/Q4 roadmap. Once you've selected and sequenced initiatives, return to `/prd` to write detailed requirements for each one.
