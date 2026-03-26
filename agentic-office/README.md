# Agentic Office

Professional intelligence layer for the Agentic Office. Extends the official [Productivity plugin](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) with senior-professional workflows: workplace memory, task prioritisation, delegation quality, daily digests, meeting intelligence, executive dashboards, cross-domain context injection, and four persistent agents.

## Prerequisites

The official **Productivity** plugin must be installed first:

```bash
claude plugins add knowledge-work-plugins/productivity
```

The Agentic Office plugin builds on top of the official plugin's task and memory CRUD. It does not replace it.

## Installation

### Claude Code CLI

```bash
claude plugins add panaversity/agentfactory-business-plugins/agentic-office
```

### Cowork

Cowork sidebar > Customize > Browse plugins > Personal > + > Add marketplace from GitHub > `https://github.com/panaversity/agentfactory-business-plugins` > find **Agentic Office** > Install

## Quick Start

After installation, run the setup skill:

```
/agentic-office:setup
```

This creates your `work.local.md` workplace memory file and walks you through configuring your four-layer memory (personal, team, projects, organisational).

## Two-Plugin Architecture

| Concern             | Official `productivity`                | Custom `agentic-office`                              |
| ------------------- | -------------------------------------- | ---------------------------------------------------- |
| Task list CRUD      | `/productivity:start`, task-management | --                                                   |
| Memory architecture | CLAUDE.md hot cache, memory/ files     | work.local.md 4-layer professional memory            |
| Task intelligence   | Basic add/complete/query               | Brain dump, P1/P2/P3 sort, cross-domain plans        |
| Delegation          | --                                     | Quality standard, handoff comms, follow-up protocols |
| Morning briefing    | --                                     | Daily digest assembly                                |
| Meeting support     | --                                     | Three-phase model (before/during/after)              |
| Dashboard           | dashboard.html (visual board)          | RAG executive dashboard (text-based, cross-domain)   |
| Search              | --                                     | Cross-context search across all memory layers        |
| Context injection   | --                                     | Cross-domain context loading                         |
| Agents              | --                                     | 4 persistent agents                                  |

## Skills

| Skill                  | Trigger Phrases                                                          | Description                                                      |
| ---------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `setup`                | configure agentic office, create work.local                              | Initial setup and orientation                                    |
| `workplace-context`    | workplace memory, person brief, add person, add project, add terminology | Four-layer workplace memory CRUD and person briefs               |
| `task-intelligence`    | brain dump, prioritise, P1 P2 P3, critical path, weekly planning         | Brain dump capture and priority sorting                          |
| `delegation`           | delegate, handoff, delegation brief, delegation quality                  | Delegation quality standard and handoff communications           |
| `digest`               | daily digest, morning briefing, what's happening today, Monday brief     | Daily morning briefing assembly                                  |
| `meeting-intelligence` | meeting prep, meeting synthesis, D/A/F/Q/R, after the meeting            | Three-phase meeting model (before/during/after)                  |
| `progress-tracker`     | weekly status, project status, RAG status, executive dashboard, blocker  | RAG status, milestones, blocker classification                   |
| `workplace-search`     | search everything, cross-context search, what do we know about           | Cross-context search across all memory layers                    |
| `context-loader`       | load context, inject context, cross-domain context                       | Cross-domain context injection                                   |
| `executive-brief`      | situation brief, bring me up to speed, prep me for, decision brief       | Situation briefs (pre-meeting, decision, person, project, topic) |

## Agents

| Agent                        | Purpose                                                                   | Skills Used                                                                 |
| ---------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `chief-of-staff`             | Orchestration: daily digest delivery, threshold alerts, weekly briefs     | digest, progress-tracker, executive-brief, workplace-search, context-loader |
| `memory-keeper`              | work.local.md maintenance, trigger-based updates, weekly staleness checks | workplace-context, workplace-search                                         |
| `meeting-intelligence-agent` | Calendar-triggered prep, post-meeting synthesis, weekly meeting audit     | meeting-intelligence, executive-brief, workplace-context                    |
| `work-tracker`               | Delegation lifecycle, overdue protocol, weekly delegation audit           | delegation, task-intelligence, progress-tracker                             |

## Cowork Mode: Activating the Agents with Scheduled Tasks

The four agents listed above have `background: true` in their frontmatter. In **Claude Code CLI**, this enables automatic background invocation when trigger conditions are met (new person mentioned, meeting approaching, etc.).

In **Cowork mode**, background agents do not auto-invoke on their own. To get the same persistent agent behavior, you need to create **Scheduled Tasks** that invoke each agent at the right time. This gives you the same daily digest, meeting prep, delegation tracking, and memory maintenance - just powered by Cowork's scheduler instead of CLI background mode.

### Recommended Schedule

| Time (local) | Agent | Frequency | What it does |
| ------------ | ----- | --------- | ------------ |
| 06:30 AM Mon | `memory-keeper` | Weekly | Staleness checks on projects, people, terminology, orphaned actions |
| 08:30 AM | `meeting-intelligence-agent` | Daily | Meeting prep briefs for today's calendar + Friday meeting audit |
| 08:50 AM | `work-tracker` | Daily | Delegation status, overdue flags, confirmation checks + Friday audit |
| 09:00 AM | `chief-of-staff` | Daily | Morning digest (Mon: week-ahead brief, Fri: week-close summary) |

### Quick Setup

You can set up all four scheduled tasks at once by giving Claude this prompt in Cowork:

```
Please read the file at agentic-office/COWORK-SCHEDULED-TASKS.md
and create all four agent scheduled tasks using the schedule and
prompts defined there.
```

Or create them manually from the Cowork sidebar under Scheduled Tasks.

### What Changes in Cowork vs CLI

| Behavior | Claude Code CLI | Cowork |
| -------- | --------------- | ------ |
| Agent auto-invocation | `background: true` handles it | Scheduled Tasks handle it |
| Calendar-triggered meeting prep | Automatic (if calendar MCP connected) | Scheduled task checks calendar daily |
| Trigger-based memory updates | Detected in conversation | Detected in conversation (same) |
| Threshold breach alerts | Real-time | Included in next scheduled digest |
| Weekly audits (Fri/Mon) | Automatic | Scheduled tasks run on those days |

The skills (digest, delegation, meeting-intelligence, etc.) work identically in both modes. Only the agent invocation mechanism differs.

## Trigger Word Separation

The official Productivity plugin and the Agentic Office plugin use completely separate trigger vocabularies to avoid routing conflicts:

**Official plugin owns:** task, to-do, todo, remember, memory, who is, start, update, sync, triage

**Agentic Office uses:** brain dump, prioritise, delegate, daily digest, meeting prep, executive dashboard, workplace memory, person brief, cross-domain context

## Evals

Run the eval suite:

```bash
# List all cases
python evals/run.py --list

# Run all cases
python evals/run.py

# Run a single case
python evals/run.py --case routing-workplace-context

# Verbose output
python evals/run.py -v
```

Requires `pyyaml`: `pip install pyyaml`

## Configuration

All configuration lives in `work.local.md` (created from `work.local.md.template` during setup). Key sections:

- **Layer 1 -- Personal:** Working style, priorities, communication preferences
- **Layer 2 -- Team:** Stakeholder profiles with communication guidance
- **Layer 3 -- Projects:** Active projects with status, milestones, risks
- **Layer 4 -- Organisational:** Terminology dictionary, meeting rhythm, culture
- **Digest Configuration:** Schedule, sections, critical flag thresholds
- **Dashboard Configuration:** Sections, metrics sources, format
- **Agent Integrations:** How the four agents connect with domain agents

## License

Apache-2.0. See [LICENSE](LICENSE).
