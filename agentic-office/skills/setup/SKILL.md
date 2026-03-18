---
name: setup
description: >
  Activate for: configure agentic office, install agentic office,
  agentic office orientation, two-plugin architecture, create work.local,
  initialise workplace memory, agentic office getting started,
  configure agents, workplace configuration.
  NOT for: official productivity plugin setup (use /productivity:start).
---

## AGENTIC OFFICE SETUP

This skill creates your `work.local.md` workplace memory file from the
bundled template and orients you to the two-plugin architecture.

### STEP 1 — LOAD CONTEXT

Read `work.local.md` in the current working directory.
If it already exists, skip to STEP 4 (orientation only).

### STEP 2 — CREATE WORK.LOCAL.MD

Copy the template from `${CLAUDE_PLUGIN_ROOT}/work.local.md.template`
to `work.local.md` in the current working directory.

Tell the user:

```
I have created work.local.md from the Agentic Office template.
This file is your four-layer workplace memory — the foundation
for all professional intelligence features.
```

### STEP 3 — GUIDED CONFIGURATION

Walk the user through filling in each layer interactively:

**Layer 1 — Personal:**
Ask for: name, role, working style, decision-making approach,
current focus (top 1-3 priorities), working hours, communication preference.

**Layer 2 — Team (People):**
Ask: "Who are the 5-8 people you interact with most? For each, I need:
name, role, how they prefer to receive information, and what they are
working on right now."

**Layer 3 — Projects:**
Ask: "What are your active projects? For each: name, any internal codename,
current status, priority (P1/P2/P3), and what is happening right now."

**Layer 4 — Organisational:**
Ask: "What internal terms, acronyms, or codenames would confuse an outsider?
What are your recurring meetings? Any unwritten rules that every colleague
knows but nobody writes down?"

After each layer, write the entries to work.local.md and confirm.

### STEP 4 — ORIENTATION MESSAGE

Deliver this orientation:

```
Your Agentic Office uses two plugins working together:

OFFICIAL PRODUCTIVITY PLUGIN (Anthropic)
  /productivity:start  — Initialise TASKS.md + CLAUDE.md + dashboard
  /productivity:update — Sync from external tools, triage stale items
  Provides: Basic task CRUD, two-tier memory, visual dashboard

AGENTIC OFFICE PLUGIN (Panaversity)
  9 professional intelligence skills:
    workplace-context  — Four-layer workplace memory (work.local.md)
    workplace-search   — Cross-context search across all memory layers
    task-intelligence   — Brain dump capture, P1/P2/P3 prioritisation
    delegation          — Delegation quality standard + handoff comms
    digest              — Daily morning briefing assembly
    meeting-intelligence — Three-phase meeting model (before/during/after)
    progress-tracker    — RAG status, milestones, blocker classification
    context-loader      — Cross-domain context injection
    executive-brief     — Situation briefs (pre-meeting, decision, person)

  4 persistent agents:
    chief-of-staff          — Orchestration: digest delivery, threshold alerts
    memory-keeper           — work.local.md maintenance, trigger-based updates
    meeting-intelligence-agent — Calendar-triggered prep and post-meeting synthesis
    work-tracker            — Delegation lifecycle, overdue protocol

The official plugin handles task and memory CRUD.
The agentic office adds professional intelligence on top.

Try: "Give me my daily digest" or "Brain dump my priorities"
```

### STEP 5 — CONFIGURE AGENT INTEGRATIONS

Ask: "Do you have any domain agents deployed from other chapters
(finance, sales, HR, operations, supply chain)? I can configure
the agent integration section so your digest and dashboard pull
from those domain agents too."

If yes: update the `agent_integrations` section of work.local.md
with the appropriate feeds.

### STEP 6 — VERIFY

Run a quick test: generate a brief digest using the data just entered.
If the output feels generic, prompt the user to add more specificity
to terminology and unwritten_rules sections.

## NEVER DO THESE

- NEVER skip the orientation message — users must understand the
  two-plugin architecture before using any skills
- NEVER overwrite an existing work.local.md without asking first
- NEVER leave the agent_integrations section empty without asking
  whether domain agents are deployed
