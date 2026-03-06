# Exercise 11: Skill Library Build

## Scenario Profile

| Field               | Value                                      |
| ------------------- | ------------------------------------------ |
| **Domain**          | Claude Code Plugin Development             |
| **Jurisdiction**    | Global                                     |
| **Time Estimate**   | 90 minutes                                 |
| **Skills Required** | All banking skills (as reference patterns) |

---

## Objective

Build and deploy a custom banking SKILL.md library with automated scheduling. This capstone exercise bridges domain expertise with AI agent architecture.

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- All banking skills available as reference patterns (read-only access to `banking/skills/`)
- A text editor or Claude Code for SKILL.md authoring
- Estimated time: 90 minutes

---

## Step-by-Step Instructions

### Step 1: Analyse the Banking Plugin Structure (15 min)

1. Review the banking plugin directory structure
2. Identify the router pattern: how does the banking-global-router route to product skills?
3. Map the relationship between skills, jurisdictions, and commands
4. Document the YAML frontmatter format used across all skills

### Step 2: Create a Custom Skill (25 min)

Design and build a new SKILL.md for a domain NOT covered by the existing 16 product skills. Choose one:

- **Option A**: Operational Risk (Basel III BIA/SMA) -- operational risk capital calculation
- **Option B**: Interest Rate Risk in the Banking Book (IRRBB) -- EVE and NII sensitivity
- **Option C**: Credit Valuation Adjustment (CVA) -- CVA risk capital charge

Your SKILL.md must include:

1. YAML frontmatter with name, description, standard, and author
2. Core principle section
3. Key formulas and calculation steps
4. Jurisdiction-specific considerations
5. "NEVER DO THESE" guardrails section

### Step 3: Update the Router (10 min)

1. Add your new skill to the banking-global-router routing table
2. Define the activation terms that should trigger your skill
3. Test the routing logic by writing 5 sample queries that should route to your skill

### Step 4: Create a Command (10 min)

Create a slash command (.md file) for your new skill following the pattern of existing commands:

- Usage syntax
- 3 example invocations
- Workflow steps

### Step 5: Create an Exercise (15 min)

Write an exercise for your new skill:

- Scenario profile with realistic data
- Step-by-step instructions
- Key learning section

### Step 6: Scheduling and Automation (15 min)

Design a workflow recipe that uses your skill on a recurring schedule:

- Define the trigger conditions (scheduled + event-driven)
- List the step-by-step execution flow
- Define the output format and distribution list
- Add quality control gates

---

## Deliverable

Produce: Complete banking SKILL.md library extension containing a new custom skill file, updated router entry, a slash command, an exercise for the new skill, and 11 test query results demonstrating correct routing and skill activation.

---

## Key Learning

- Banking domain skills follow a consistent pattern: YAML frontmatter, core principle, formulas, guardrails
- The router pattern enables automatic activation without the user needing to know which skill to load
- Commands provide structured entry points for common workflows
- Exercises with realistic data are essential for skill validation and user training
- Workflow recipes bridge the gap between skills (knowledge) and operations (automation)
