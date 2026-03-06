# Workflow Recipe: NDA Triage

## Task Overview

| Field         | Value                                                                  |
| ------------- | ---------------------------------------------------------------------- |
| **Task Name** | NDA Triage: Three-Tier Routing for Incoming NDAs                       |
| **Frequency** | Per NDA received (typical: 10-50 per month)                            |
| **Purpose**   | Route NDAs to the correct review level, reducing attorney time by 70%+ |
| **Owner**     | Legal Operations Manager / Designated Reviewing Attorney               |

---

## Step-by-Step Execution

### Step 1: Receive NDA

```
Input: Incoming NDA (PDF, DOCX, or via MCP connector)
Actions:
  - Log receipt: counterparty, date, requesting business unit, stated urgency
  - Confirm: mutual or unilateral?
  - Confirm: purpose (vendor eval / partnership / M&A / employment / other)
```

### Step 2: Load Standard Form

```
CHECK for NDA configuration in legal.local.md

IF FOUND:
  - Load standard form reference
  - Load Tier 1/2/3 criteria
  - Compare incoming NDA against standard form directly

IF NOT FOUND:
  - Apply general commercial NDA standards
  - Label: "Reviewed against general commercial NDA standards"
```

### Step 3: Classify Tier

```
TIER 1 -- STANDARD APPROVAL
  Criteria: Substantially identical to standard form, or deviations
  within pre-approved ranges.
  Target: 60-70% of incoming NDAs.
  Attorney time: 0 minutes.
  Action: Route to authorised signatory.

TIER 2 -- COUNSEL REVIEW
  Criteria: Deviations within acceptable range but needing confirmation.
  Target: 20-30%.
  Attorney time: ~15 minutes.
  Action: Route to reviewing attorney with triage summary.

TIER 3 -- FULL REVIEW
  Criteria: RED deviations, unusual structure, high-risk provisions.
  Target: 10-15%.
  Attorney time: ~45 minutes.
  Action: Route to senior counsel / GC with full risk summary.
```

### Step 4: Check Automatic RED Flags

```
These ALWAYS trigger Tier 3 regardless of playbook:
  - Residuals clause ("retained in unaided memory")
  - No carve-out for publicly available information
  - Non-compete provisions of any scope
  - Perpetual confidentiality obligations
  - Governing law: jurisdiction with no commercial law framework
  - No definition of Confidential Information
  - Unilateral when mutual expected (without justification)
  - Asymmetric injunctive relief
  - Disclosure to affiliates without need-to-know
```

### Step 5: Produce Triage Report

```
Output format:
  NDA TRIAGE REPORT
  Counterparty:   [Name]
  Date:           [Date]
  Playbook:       [Loaded / Not configured]
  TRIAGE TIER:    [1 / 2 / 3] -- [Label]
  Attorney time:  [0 / ~15 min / ~45 min]
  SUMMARY:        [N] GREEN | [N] YELLOW | [N] RED
  RECOMMENDATION: [Route to / Approve]
  DEVIATIONS:     [Listed with classification]
```

### Step 6: Route

```
Tier 1: Send acknowledgement to business unit; route to signatory
Tier 2: Send to reviewing attorney with triage summary; SLA: 2 days
Tier 3: Send to GC with full summary; SLA: 5 days
```

---

## SLA Targets

| Tier   | Attorney Time | Response SLA    | Escalation If Breached    |
| ------ | ------------- | --------------- | ------------------------- |
| Tier 1 | 0 min         | 1 business day  | Notify business unit      |
| Tier 2 | ~15 min       | 2 business days | Notify GC                 |
| Tier 3 | ~45 min       | 5 business days | Notify GC + business unit |

---

## Required Skill Files

| Skill File            | Purpose                                 |
| --------------------- | --------------------------------------- |
| `nda-triage`          | Three-tier classification and RED flags |
| `legal-global-router` | Jurisdiction identification             |
| Jurisdiction overlays | Governing law considerations            |

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
