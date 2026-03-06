# Workflow Recipe: Regulatory Weekly Brief

## Task Overview

| Field         | Value                                                                 |
| ------------- | --------------------------------------------------------------------- |
| **Task Name** | Weekly Regulatory Monitoring Brief and Monthly Board Summary          |
| **Frequency** | Weekly (brief) + Monthly (board summary)                              |
| **Purpose**   | Track regulatory changes, assess impact, produce actionable briefings |
| **Owner**     | Compliance Officer / General Counsel                                  |

---

## Trigger Conditions

| Trigger       | Condition                          | Action                        |
| ------------- | ---------------------------------- | ----------------------------- |
| **Scheduled** | Every Monday 08:00                 | Run weekly monitoring cycle   |
| **Ad-hoc**    | Significant regulatory development | Run immediate alert cycle     |
| **Monthly**   | Last business day of each month    | Compile monthly board summary |

---

## Step-by-Step Execution

### Step 1: Configure Monitoring Scope

```
Required parameters (load from settings or confirm with user):
  - Organisation type: [industry, size, structure]
  - Primary regulatory areas:
    - Data Protection: UK GDPR, EU GDPR, CCPA, ICO guidance
    - AI Regulation: EU AI Act phases, UK AI framework
    - Employment: Working time, IR35, TUPE, redundancy
    - Company Law: Annual return, director duties, PSC register, UKBA
    - Sector-specific: [configure for industry]
  - Key jurisdictions: [all relevant jurisdictions]
  - Escalation contacts: [Compliance Officer, GC, relevant leads]
```

### Step 2: Search Regulatory Sources

```
Sources (via web search MCP):
  - ICO (UK data protection)
  - EC / national DPAs (EU data protection)
  - FCA / PRA (if financial services)
  - SEC / FTC (US)
  - Companies House / SECP / equivalent
  - Official government legislative databases
  - Regulatory body announcement pages

Search for: new regulations, guidance, enforcement actions, consultations,
effective date changes, court decisions with regulatory impact
```

### Step 3: Classify Impact

```
HIGH PRIORITY (RED):
  Effective within 30 days; OR requires immediate policy change;
  OR potential enforcement risk.

MONITOR (YELLOW):
  Effective within 6 months; OR affects contracts on renewal;
  OR requires internal process change.

AWARENESS (GREEN):
  Longer horizon; informational only; no immediate action required.
```

### Step 4: Produce Weekly Brief

```
Output format:
  WEEKLY REGULATORY BRIEFING -- [Date]
  ========================================================

  RED -- HIGH PRIORITY -- Action required within 30 days
  --------------------------------------------------------
  [Regulation] -- [Jurisdiction]
  Effective:       [Date]
  Summary:         [2 sentences]
  Internal impact: [Policy/process needing update]
  Contract impact: [N contracts with relevant clauses]
  Action:          [Specific action] by [date] -- Owner: [name]

  YELLOW -- MONITOR
  --------------------------------------------------------
  [...]

  GREEN -- AWARENESS
  --------------------------------------------------------
  [...]

  ========================================================
  NOTE: Confirm all interpretations with qualified counsel.
```

### Step 5: Monthly Board Summary (last business day)

```
Structure:
  - Executive Summary: 3-5 bullets (most important changes)
  - RAG Status: traffic-light per regulatory area
  - Actions Required: owner / action / deadline (table)
  - Horizon Items: significant changes in next 3-6 months
  - Appendix: link to weekly brief archive

Compile from 4 weekly briefs + any ad-hoc alerts.
```

---

## Escalation Rules

| Trigger                            | Action                                    |
| ---------------------------------- | ----------------------------------------- |
| HIGH PRIORITY item identified      | Notify GC and Compliance Officer same day |
| Effective date < 7 days            | Emergency escalation to GC                |
| Enforcement action in our sector   | GC + relevant business unit immediately   |
| New obligation affecting contracts | Flag for contract review team             |

---

## Required Skill Files

| Skill File              | Purpose                                         |
| ----------------------- | ----------------------------------------------- |
| `regulatory-monitoring` | Monitoring parameters and impact classification |
| `legal-global-router`   | Jurisdiction identification and overlay loading |
| Jurisdiction overlays   | Jurisdiction-specific regulatory frameworks     |

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
