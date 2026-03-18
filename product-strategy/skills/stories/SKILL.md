---
name: stories
description: >
  Activate for: user stories, write user stories, story, as a user I want,
  user story map, story mapping, epic, story breakdown, story splitting,
  acceptance criteria for stories, BDD, given when then, story refinement,
  sprint stories, story writing, feature to stories, spec to stories,
  decompose requirements, break down PRD.
  NOT for: feature specifications (use official /write-spec), sprint planning
  (use official /sprint-planning), roadmap planning (use official /roadmap-update).
license: Apache-2.0
argument-hint: "<feature or spec name>"
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/stories"
---

## CONTEXT LOADING

Before generating stories, load `product.local.md` for product context,
personas, and engineering team details. If not configured, ask the user
for product name, personas, and sprint cadence.

## USER STORY WORKFLOW

### Story Anatomy

Every user story must have three parts:

As a [SPECIFIC PERSONA -- not "user"],
I want to [CAPABILITY -- behaviour, not UI element],
So that [USER OUTCOME -- the value they receive].

Quality test for each part:
PERSONA: Is it a named persona from product.local.md?
"A user" is not a persona. "An enterprise IT admin" is.
WANT: Is it a capability (what they can do) not a UI element
(what they click)? "filter by date range" is capability.
"click the date picker" is UI -- not a story.
OUTCOME: Is it a user outcome (benefit to them) not a system action?
"so that I can find relevant data faster" is an outcome.
"so that the filter is applied" is a system action.

### Story Acceptance Criteria

Each story must have acceptance criteria -- testable statements that
define when the story is complete.

Acceptance Criteria format:

- [Condition: Given / When / Then format optional but encouraged]
- Each AC independently testable
- No "and" in a single AC -- split compound statements
- Include: happy path + key error states
- Include: edge cases if they affect the story's primary flow

### Story Sizing Guidance

Ideal story size: completable in 1-3 days by one engineer
Too large (epic): requires splitting into sub-stories
Too small (task): should be a sub-task, not a story

When to split a story:

- Story cannot be completed in one sprint
- Story has more than 7 acceptance criteria
- Story covers multiple distinct user flows
- Story has multiple personas (split by persona)

### Epic / Story / Sub-task Hierarchy

EPIC: A complete user capability too large for one sprint
(e.g. "Enterprise SSO")
STORY: A slice of the epic deliverable in one sprint
(e.g. "SAML 2.0 provider configuration")
SUB-TASK: A technical task within a story (engineering-owned)
(e.g. "Write SAML metadata parser")

Rule: PMs own epics and stories. Engineers own sub-tasks.
PMs should not write sub-tasks -- that is engineering territory.

### Story Output Format

```
USER STORIES: [Feature / Epic name]
================================================================
Epic: [Epic name and one-line description]
Stories: [N] | Sprints: [Estimated N] | Persona(s): [Names]

-- [PERSONA] STORIES -----------------------------------------------

Story [N]: [Short name]
  As a [Persona],
  I want to [capability],
  So that [user outcome].

  Acceptance Criteria:
  AC1: [Testable statement]
  AC2: [Testable statement]
  AC3: [Error state or edge case]

  Size:         [S / M / L -- relative]
  Dependencies: [Other stories this depends on, if any]
  Notes:        [Anything engineering needs to know]

[Repeat for each story]
================================================================
```

### Story Generation from Spec

When generating stories from an existing spec or PRD:

1. Identify each distinct user flow from the spec
2. Identify each distinct persona who has a flow
3. Create one story per persona-flow combination
4. Derive ACs from the spec's acceptance criteria
5. Flag any spec AC that cannot be expressed as a story AC
   (usually implementation details -- these belong in sub-tasks)
6. Flag any user flow in the spec that has no corresponding story
   (coverage gap)

## COMPLEMENTARY WORKFLOWS

This skill decomposes specs/PRDs into stories. For related PM workflows:

- Writing the spec that stories are derived from: use official `/write-spec`
- Writing the PRD that stories are derived from: use `/prd` from this plugin
- Prioritising the story backlog: use `/prioritise` from this plugin
- Sprint planning with stories: use official `/sprint-planning`

## NEVER DO THESE

- NEVER use "a user" as the persona -- always use a named persona
  from product.local.md
- NEVER write a "want" that describes a UI element rather than
  a user capability
- NEVER write a "so that" that describes a system action rather
  than a user outcome
- NEVER write a story that cannot be completed in one sprint
  without flagging it as an epic that needs splitting
- NEVER write an AC with "and" -- split it
- NEVER write a story without at least one error-state AC
  (what happens when the happy path fails?)

ALL OUTPUTS REQUIRE REVIEW BY THE PM AND ENGINEERING LEAD BEFORE SPRINT PLANNING.
