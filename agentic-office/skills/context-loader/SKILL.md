---
name: context-loader
description: >
  Activate for: load context, inject context, cross-domain context,
  context for this endeavour, relevant background, multi-domain context,
  what context do I need, before I work on this, context from HR,
  context from finance, context from ops, combine context,
  cross-domain brief, what should I know before starting.
  NOT for: situation briefs (use executive-brief),
  search queries (use workplace-search).
---

## CONTEXT INJECTION WORKFLOW

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it does not exist, tell the user to run `/agentic-office:setup` first.

Check agent_integrations in work.local.md for configured domain agents.

### STEP 2 — IDENTIFY CONTEXT TYPE

TYPE 1: SINGLE-DOMAIN CONTEXT
Load context from one domain for a specific endeavour.
Example: "Load finance context before I review the analytics budget proposal"

TYPE 2: CROSS-DOMAIN CONTEXT
Load context from multiple domains simultaneously.
Example: "Load HR + Finance + Ops context for onboarding Dr. Sana Mirza"

TYPE 3: PERSON CONTEXT
Load everything known about a specific person before an interaction.
Example: "Load full context on Omar before our budget conversation"

TYPE 4: PROJECT CONTEXT
Load full project context including cross-domain implications.
Example: "Load full context on Project Nighthawk"

TYPE 5: DECISION CONTEXT
Load context needed to make a specific decision well.
Example: "Load context for the Islamabad expansion decision"

### STEP 3 — PRODUCE OUTPUT

OUTPUT STRUCTURE:

```
CONTEXT BRIEF — [Subject]
Loaded from: [Domain(s) + work.local.md layers used]
================================================================
CORE CONTEXT:
[The most important things to know for this endeavour]

[DOMAIN 1] CONTEXT:
[What is known from this domain that is relevant]
[Current status; recent changes; open items]

[DOMAIN 2] CONTEXT:
[Same structure]

PEOPLE CONTEXT:
[Anyone involved — communication style; current focus; approach tips]

WHAT TO WATCH FOR:
[Specific things to pay attention to given the full context]

GAPS IN CONTEXT:
[What is NOT known that would be useful — and how to get it]
================================================================
```

### Integration Protocol

When loading cross-domain context, check each configured domain:

HR domain:
Check: Is anyone involved in a new hire / onboarding / performance situation?
Check: Any HR obligations or approvals affecting this endeavour?

Finance domain:
Check: Any budget approvals pending that affect this endeavour?
Check: Any financial constraints or targets relevant?

Operations domain:
Check: Any vendor, compliance, or change management items relevant?
Check: Any SOPs that govern this activity?

Sales domain:
Check: Any client or pipeline considerations?

Supply chain domain:
Check: Any procurement or vendor dependencies?

## NEVER DO THESE

- NEVER load context from a domain that is not relevant to the endeavour —
  more context is not always better; irrelevant context creates noise
- NEVER omit the "gaps in context" section — knowing what you do not
  know is as important as knowing what you do know
- NEVER surface sensitive person entries (marked sensitivity: RESTRICTED)
  in cross-domain context outputs where the subject might see them
