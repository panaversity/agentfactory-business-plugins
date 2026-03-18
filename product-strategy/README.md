# Product Strategy Plugin

Product strategy skills for B2B SaaS Product Managers. Covers the PM workflow gaps that the official Anthropic `product-management` plugin does not: discovery briefs, interview guides, PRDs, user stories, backlog prioritisation, and retrospectives.

## Two-Plugin Architecture

This plugin is **Layer 2** -- it complements the official `product-management` plugin (Layer 1). Install both for full PM workflow coverage.

| Layer | Plugin | Commands | Purpose |
|---|---|---|---|
| Layer 1 (Official) | `product-management` | `/write-spec`, `/roadmap-update`, `/synthesize-research`, `/stakeholder-update`, `/competitive-brief`, `/metrics-review`, `/sprint-planning` | Foundational PM workflows |
| Layer 2 (This) | `product-strategy` | `/brief`, `/interview`, `/prd`, `/stories`, `/prioritise`, `/retro` | Discovery, requirements, prioritisation, reflection |

## Installation

Install both plugins for the complete PM workflow:

```bash
# Layer 1: Official plugin
claude plugin install product-management@anthropic

# Layer 2: This plugin
claude plugin install product-strategy@agentfactory-business
```

## Setup

1. Copy `product.local.md.template` to `product.local.md`
2. Fill in your product details (identity, personas, engineering team, stakeholders)
3. Test with `/brief` -- does the output sound like your product?

## Skills

| Command | Skill | Purpose |
|---|---|---|
| `/brief` | Discovery briefs | Frame problems, scope discovery sprints, align on initiatives |
| `/interview` | Interview guides | Generate structured interview guides with note-taking templates |
| `/prd` | PRDs | Multi-team initiative requirements with 10-section template |
| `/stories` | User stories | Decompose specs/PRDs into properly structured user stories |
| `/prioritise` | Backlog prioritisation | RICE/ICE/MoSCoW scoring with three mandatory challenges |
| `/retro` | Retrospectives | Four-question retro framework with process improvement format |

## Agents

| Agent | Purpose | Trigger |
|---|---|---|
| `research-intelligence` | Weekly user signal monitoring across support, NPS, and feature requests | Scheduled (weekly) + threshold escalation |
| `stakeholder-update` | Three-version stakeholder updates with PM review gate | Scheduled (weekly) + status change triggers |
| `roadmap-coherence` | Backlog orphan detection, spec coverage, sprint alignment | Scheduled (weekly) + threshold escalation |

## Example Workflows

### Discovery to Spec

```
/brief          -- Frame the problem (Problem Brief)
/interview      -- Generate interview guide for discovery
                -- [Conduct interviews, take notes]
/synthesize-research  -- Synthesise findings (official plugin)
/write-spec     -- Write feature spec (official plugin)
```

### PRD to Sprint

```
/prd            -- Write multi-team requirements
/stories        -- Decompose PRD into user stories
/prioritise     -- Score and rank the story backlog
/sprint-planning -- Plan the sprint (official plugin)
```

### Ship to Learn

```
/stakeholder-update -- Communicate launch (official plugin)
/metrics-review     -- Review outcomes (official plugin)
/retro              -- Run product retrospective
```

## Configuration

All skills read from `product.local.md` for context-aware output. Key sections:

- **Product Identity**: name, stage, business model, value proposition
- **Personas**: named personas with goals, frustrations, behavioural signals
- **Engineering Team**: size, sprint cadence, velocity, backlog tool
- **Stakeholder Map**: who cares about what, communication preferences
- **Quality Standards**: spec review checklist, performance bars
- **Research Configuration**: data sources, signal thresholds

## License

Apache-2.0
