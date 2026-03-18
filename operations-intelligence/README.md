# Operations Intelligence Plugin

Complements the official Operations plugin with audit preparation, contract analysis,
incident management, operational metrics, and four persistent operations agents.

## Installation

```bash
claude plugins add agentfactory-business-plugins/operations-intelligence
```

For the complete operations intelligence layer taught in Chapter 38,
also install the official Operations plugin:

```bash
claude plugins add knowledge-work-plugins/operations
```

## Commands

| Command     | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| `/audit`    | Prepare for audits -- evidence inventory, mock reviews, response framework |
| `/contract` | Analyse contracts -- extract obligations, flag risks, inform negotiations  |
| `/incident` | Run post-mortems -- timeline, Five Whys RCA, corrective actions            |
| `/metrics`  | Design metrics frameworks -- leading/lagging indicators, dashboards        |

## Agents

| Agent              | Purpose                                                                        | Schedule         |
| ------------------ | ------------------------------------------------------------------------------ | ---------------- |
| vendor-watchdog    | Monitor vendor portfolio (renewals, SLAs, spend, unapproved payments)          | Weekly Mon 07:00 |
| process-health     | Monitor SOP library (currency, orphans, triggered reviews)                     | Monthly 1st Mon  |
| compliance-monitor | Track compliance obligations (reviews due, evidence aging, regulatory changes) | Weekly Mon 08:00 |
| change-tracker     | Monitor change pipeline (impact assessments, rollback plans, PIRs)             | Weekly Fri 16:00 |

## Two-Plugin Architecture

This plugin is designed to work alongside the official **Operations** plugin
(`knowledge-work-plugins/operations`). The two plugins have **zero overlap**:

| This Plugin (Custom)  | Official Plugin                          |
| --------------------- | ---------------------------------------- |
| `/audit`              | `/vendor-review`                         |
| `/contract`           | `/process-doc`                           |
| `/incident`           | `/change-request`                        |
| `/metrics`            | `/runbook`                               |
|                       | `/status-report`                         |
|                       | `/capacity-plan`                         |
|                       | `compliance-tracking` (auto-skill)       |
|                       | `risk-assessment` (auto-skill)           |
|                       | `process-optimization` (auto-skill)      |

## Configuration

Copy `local.md.template` to `ops.local.md` and populate with your organisation's
vendors, regulatory frameworks, risk appetite, change authority matrix, and
operational metrics. See Chapter 38, Lesson 2 for guided setup.

### Configuration Sections

1. **Organisation Context** -- company details, jurisdiction, contacts
2. **Vendor Portfolio** -- categories, spend bands, critical vendors, approval thresholds
3. **Regulatory Frameworks** -- obligations, evidence repository, review cycles
4. **Risk Configuration** -- appetite statement, 5x5 scoring matrix, escalation contacts
5. **Change Management** -- authority matrix, CAB schedule, freeze periods, PIR requirements
6. **Process Library** -- SOP numbering, repository, critical process inventory, review cycles
7. **Operational Metrics** -- KPI framework, reporting cadence, dashboard configuration
8. **Incident Management** -- severity definitions, escalation path, incident log

## Evals

Run the evaluation harness to verify plugin behaviour:

```bash
# List all test cases
uv run evals/run.py --list

# Run all tests
uv run evals/run.py

# Run a single case
uv run evals/run.py --case route_audit_iso

# Run a category
uv run evals/run.py --category routing
```

## License

Apache-2.0
