---
name: brief
description: >
  Activate for: product brief, discovery brief, problem brief, opportunity
  brief, problem statement, opportunity framing, how might we, design brief,
  research brief, discovery scope, kickoff brief, initiative framing,
  problem definition, hypothesis brief, PM brief, product hypothesis,
  frame the problem, scope a discovery sprint, initiative alignment.
  NOT for: feature specifications (use official /write-spec), competitive
  analysis (use official /competitive-brief), user research synthesis
  (use official /synthesize-research).
license: Apache-2.0
argument-hint: "<brief type> for <topic>"
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/brief"
---

## CONTEXT LOADING

Before generating any brief, load `product.local.md` for product context,
personas, and terminology. If not configured, ask the user for product name,
stage, and primary persona before proceeding.

## BRIEF WORKFLOW

### Brief Types

Ask the user which type of brief they need, or infer from context:

TYPE 1: PROBLEM BRIEF (use at start of discovery)
  Purpose: Align the team on the problem before discussing solutions.
  Rule: A problem brief contains NO solution proposals.
  If you are already thinking about solutions, that is fine --
  but keep them out of the brief. Solutions too early anchor thinking.

  PROBLEM BRIEF FORMAT:
  ```
  Product Brief: [Area / Opportunity name]
  Type:          Problem Brief
  Date:          [Date]
  Author:        [PM]
  Team:          [Who should read and respond to this]

  THE PROBLEM
  [2-3 sentences: What is happening that should not be happening,
   or what is not happening that should be?]

  WHO IS AFFECTED
  [Persona(s) from product.local.md; how many users; what segment]

  EVIDENCE
  [Quantified: support tickets, research quotes, behavioral data,
   lost deals, NPS verbatim -- cite sources]

  IMPACT OF NOT SOLVING
  [What continues to happen if we do nothing? Commercial impact?
   User impact? Competitive impact?]

  WHAT WE DO NOT KNOW YET
  [Explicit gaps: what questions need research before we can
   define a solution? What assumptions are we making?]

  HYPOTHESIS (optional -- only if confident)
  [If you have a directional hypothesis about the solution,
   state it clearly as a hypothesis, not a requirement:
   "We believe that [X] will solve [problem] for [persona].
   We will know this is true when [measurable outcome]."]

  DISCOVERY QUESTIONS
  [The 3-5 questions that discovery research needs to answer
   before we can write a spec]
  ```

TYPE 2: DISCOVERY BRIEF (use to scope a research sprint)
  Purpose: Define exactly what a discovery sprint will explore,
  with whom, using what methods, to answer which questions.

  DISCOVERY BRIEF FORMAT:
  ```
  Discovery Brief: [Area]
  Duration:        [1 week / 2 weeks / sprint]
  Methods:         [Interviews / data analysis / usability testing / mixed]
  Sample:          [Who to talk to; n=X minimum; how to recruit]

  QUESTIONS TO ANSWER (ranked):
  1. [Primary question -- most important to answer]
  2. [Secondary question]
  3. [Tertiary question]

  OUT OF SCOPE FOR THIS DISCOVERY:
  [What we are explicitly NOT exploring in this sprint]

  SUCCESS CRITERIA:
  [How will we know the discovery was successful?
   Not "we talked to users" -- but "we can answer question 1 with
   evidence from at least 5 participants"]

  OUTPUTS EXPECTED:
  [Research synthesis report / insight deck / problem statement /
   updated spec / go / no-go recommendation]
  ```

TYPE 3: INITIATIVE BRIEF (use before writing a full PRD)
  Purpose: One-page framing of a major initiative to get alignment
  before investing in a full PRD.

  INITIATIVE BRIEF FORMAT:
  ```
  Initiative Brief: [Name]
  Status:           [Concept / Approved for discovery / Approved for build]
  Champion:         [PM name]
  Stakeholders:     [Who needs to sign off]

  THE BET
  [One sentence: what we believe, who it benefits, and why now]

  PROBLEM
  [With evidence -- 3-5 sentences]

  PROPOSED DIRECTION
  [High-level: what kind of solution are we exploring?
   No detailed spec here -- just direction]

  SIZE OF PRIZE
  [Commercial or user impact if successful]

  ROUGH EFFORT
  [Order of magnitude: days / weeks / months / quarters]

  RISKS
  [Top 2-3 risks if we pursue this]

  DECISION NEEDED
  [What approval or decision does this brief request?
   "Approve discovery sprint" / "Approve as Q3 initiative" / etc.]
  ```

## COMPLEMENTARY WORKFLOWS

This skill handles problem/discovery/initiative framing. For related PM workflows:
- Feature specifications: use official `/write-spec`
- Competitive analysis: use official `/competitive-brief`
- Research synthesis after discovery: use official `/synthesize-research`
- Full requirements documents: use `/prd` from this plugin

## NEVER DO THESE

- NEVER include solution proposals in a Problem Brief
- NEVER write a Discovery Brief without explicit discovery questions
  that have clear answers (not "explore user needs" -- too vague)
- NEVER produce a brief without a "decision needed" or "next step"
- NEVER omit the "what we do not know" section --
  acknowledging uncertainty is strength, not weakness
- NEVER use "a user" as the persona -- always reference named personas
  from product.local.md

ALL OUTPUTS REQUIRE REVIEW BY THE PM BEFORE DISTRIBUTION TO STAKEHOLDERS.
