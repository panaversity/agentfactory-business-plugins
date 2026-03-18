# Transcript: Negative Roadmap Planning (With Skill)

## Task

User asked for help planning a Q3/Q4 product roadmap — deciding which initiatives to pursue and in what order.

## Steps Taken

1. **Read the PRD skill** (`/prd` SKILL.md) to understand its scope and instructions.
2. **Identified scope mismatch**: The skill's description field explicitly excludes roadmap planning: `"NOT for: roadmap planning (use official /roadmap-update)"`. The complementary workflows section reinforces this: `"Roadmap placement: use official /roadmap-update"`.
3. **Checked for product.local.md**: Not found — but irrelevant since the skill shouldn't activate for this task.
4. **Checked for /roadmap-update skill**: Not present in the product-strategy plugin directory.
5. **Wrote response**: Explained the mismatch, quoted the skill's own exclusion language, and redirected to `/roadmap-update` as the skill instructs.

## Key Decision

The PRD skill was followed precisely. Its instructions say roadmap planning is out of scope and should use `/roadmap-update`. Rather than ignoring this boundary and generating an ill-fitting PRD, the correct behavior is to decline the task and redirect to the appropriate tool.

## Outcome

- **Skill activated**: Yes (read and followed)
- **PRD generated**: No (task is outside skill scope)
- **Redirect provided**: Yes (to `/roadmap-update`)
- **Skill boundary respected**: Yes
