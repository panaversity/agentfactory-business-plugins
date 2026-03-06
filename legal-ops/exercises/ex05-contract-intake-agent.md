# Exercise 5: Build the Legal Ops Agent -- Contract Intake

## Scenario Profile

| Field               | Value                                              |
| ------------------- | -------------------------------------------------- |
| **Type**            | Agent Configuration and Testing                    |
| **Time**            | 90 minutes                                         |
| **Skills Required** | All product skills + `contract-intake-agent`       |
| **Plugin Commands** | `/review-contract`, `/triage-nda`, `/vendor-check` |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance      |

---

## Overview

You are building a complete Contract Intake Agent that manages all incoming
contracts from receipt through routing, tracking, and obligation monitoring.

---

## Steps

### Step 1 -- Map Your Current Process

Before configuring anything, document precisely:

- How do contracts currently arrive?
- Who handles first review? How long does it take?
- Where are executed contracts stored? Are they searchable?
- How are renewal dates tracked?
- What falls through the cracks most often?

This is the process you are replacing. Document it to measure improvement.

### Step 2 -- Configure the SKILL.md

Using the contract-intake-agent SKILL.md, customise for your organisation:

- Add your specific contract types
- Define SLA thresholds with named owners (actual names, not generic roles)
- Write your three communication templates
- Add your escalation triggers

### Step 3 -- Connect via MCP

Work with IT to connect:

- Google Drive or SharePoint (contract storage)
- Gmail or Outlook (legal intake email)
- Google Sheets or Notion (contract tracking log)

### Step 4 -- Test with Five Historical Contracts

- One NDA (standard / should be Tier 1)
- One NDA (non-standard / should be Tier 2 or 3)
- One vendor agreement (straightforward)
- One vendor agreement (complex IP, data processing, unusual terms)
- One employment or contractor agreement

For each: record intake classification, routing decision, communication output.

### Step 5 -- Calibrate

For incorrect routing, identify whether the error was in:

- Playbook threshold
- SKILL.md routing logic
- Document type classification

Fix and re-test.

### Step 6 -- Build the Tracking Dashboard

Using Google Sheets MCP, create a contract tracking dashboard showing:

- All active contracts by status
- Obligations due in 30/60/90 days
- Average cycle time by tier (baseline vs. agent-assisted)

---

## Deliverable

A functioning Contract Intake Agent connected to your document management system,
with tested SKILL.md, live tracking dashboard, and documented time savings.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
