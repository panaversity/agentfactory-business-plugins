# Product Strategy Plugin -- Instructions

## Layer 1 / Layer 2 Architecture

This plugin is **Layer 2** -- it complements the official Anthropic
`product-management` plugin (Layer 1). The two plugins work together
to cover the full PM workflow cycle.

**Layer 1 (official product-management)** provides:

- `/write-spec` -- Feature specifications
- `/roadmap-update` -- Roadmap planning and communication
- `/synthesize-research` -- User research synthesis
- `/stakeholder-update` -- Stakeholder communications
- `/competitive-brief` -- Competitive intelligence
- `/metrics-review` -- Metrics and OKR tracking
- `/sprint-planning` -- Sprint planning and capacity

**Layer 2 (this plugin, product-strategy)** fills the gaps:

- `/brief` -- Problem, discovery, and initiative briefs
- `/interview` -- User interview guide generation
- `/prd` -- Multi-team initiative PRDs
- `/stories` -- Spec-to-user-story translation
- `/prioritise` -- RICE/ICE/MoSCoW backlog scoring
- `/retro` -- Post-launch product retrospectives

**Rule**: Do NOT duplicate Layer 1 commands. If a query matches a Layer 1
skill, direct the user to the official plugin command instead.

## Context Loading

Always load `product.local.md` before generating any output. This file
contains the product identity, personas, engineering team details,
stakeholder map, terminology, and quality standards that make every
output context-aware.

If `product.local.md` is not found, ask the user for essential context
before proceeding: product name, stage, primary persona, and engineering
team size.

## Mandatory Output Header

Every skill output must begin with a header identifying the task:

```
TASK:          [e.g. Problem Brief -- Workflow Automation]
FEATURE/AREA:  [Product area or initiative name]
CONFIGURATION: [Loaded: product.local.md / Not configured]
AUDIENCE:      [PM / Engineering / Executive / Customer]
VERSION:       [Draft / Review / Final]
```

## Spec Quality Rules

When generating or reviewing specifications, PRDs, or stories:

- Problem section must have at least one quantified data point
- Solution section must have an explicit OUT OF SCOPE list (minimum 2 items)
- All ACs must be independently testable
- No AC may contain "and" -- split compound ACs
- No AC may describe UI elements rather than user behaviour
- Edge cases table must have minimum 4 rows
- All open questions must have owners and due dates

## Research Quality Rules

When generating interview guides or research briefs:

- Ask about behaviour, not opinions
- Ask about the past, not hypothetical futures
- Do not mention solutions in the first half of any interview
- Minimum 5 interviews before drawing directional conclusions
- One interview is an anecdote; five are a signal

## Communication Calibration

When generating stakeholder updates or communications:

- Executive: headline metric + 1-page summary + risk flags
- Engineering: technical detail + dependency status + blockers
- Customer: user-impact language + timeline + what's next

Never send the same version to different audiences.

## Universal Rules (Non-Negotiable)

- Always use named personas from product.local.md -- never "a user"
- Always include specific recommended actions with deadlines
- Never fabricate data -- label estimates and flag data gaps
- Never produce output without a clear next step or decision needed
- All outputs require human review before use in business decisions
