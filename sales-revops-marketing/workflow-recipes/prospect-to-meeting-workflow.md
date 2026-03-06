# Workflow Recipe: Prospect to Meeting -- End-to-End

## Task Overview

| Field         | Value                                                                          |
| ------------- | ------------------------------------------------------------------------------ |
| **Task Name** | Prospect to Meeting: From Signal Detection through Booked Discovery Call       |
| **Frequency** | Continuous (triggered by each new HOT lead or qualifying signal)               |
| **Purpose**   | Convert an identified prospect into a booked meeting via research and outreach |
| **Owner**     | Account Executive / SDR (assigned rep in CRM)                                  |

---

## Trigger Conditions

| Trigger             | Condition                                           | Action                                               |
| ------------------- | --------------------------------------------------- | ---------------------------------------------------- |
| **HOT lead scored** | Lead crosses 60-point threshold via /score-lead     | Start prospect-to-meeting sequence                   |
| **Signal alert**    | Lead Intelligence Agent fires HOT signal alert      | Start prospect-to-meeting sequence                   |
| **Manual trigger**  | Rep requests /research-prospect for a named account | Start at Step 2 (skip scoring)                       |
| **Inbound request** | Prospect fills in demo/contact form                 | Flag INBOUND; start at Step 2; prioritise 4-hour SLA |

---

## Step-by-Step Execution

### Step 1: Score and Qualify

```
Input: Lead record from CRM or signal alert
Actions:
  - Run /score-lead on the prospect
  - Evaluate three dimensions: Fit (0-40), Timing (0-40), Engagement (0-20)
  - If total >= 60 (HOT): proceed to Step 2
  - If total 35-59 (WARM): route to nurture sequence, exit this workflow
  - If total < 35 (COLD): log in CRM, no action, exit this workflow

Output: Score card with routing recommendation
```

### Step 2: Deep Research

```
Input: HOT lead record + any signal context
Actions:
  - Run /research-prospect with company name and contact name
  - Generate prospect brief: company overview, ICP match analysis,
    recent signals, tech stack, competitive landscape, key contacts
  - Identify 3 personalisation hooks from verifiable public sources
  - Check jurisdiction -> load outreach compliance overlay

Output: Prospect research brief with personalisation hooks
```

### Step 3: Build Outreach Sequence

```
Input: Research brief + personalisation hooks + jurisdiction overlay
Actions:
  - Run /build-sequence (HOT 6-touch or WARM 5-touch)
  - Generate personalised multi-touch sequence across channels
  - Apply Five Laws of Outreach to every touch
  - Apply jurisdiction compliance rules (opt-out, consent, timing)
  - Schedule Touch 1 within 24 hours of HOT classification

Output: Complete sequence with channel, timing, and content per touch
```

### Step 4: Execute Touch 1

```
Input: Touch 1 draft from sequence
Actions:
  - Present draft to assigned rep for review
  - Rep approves, edits, or rejects
  - On approval: send via configured channel (email/LinkedIn)
  - Log in CRM: sequence started, Touch 1 sent, timestamp, channel

CRITICAL: ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
```

### Step 5: Monitor and Advance

```
Outreach Sequencing Agent takes over:
  - Track delivery, opens, clicks for each touch
  - Before each subsequent touch: check for reply, bounce, unsubscribe
  - If REPLY: pause sequence, alert rep within 15 minutes
  - If BOUNCE: pause sequence, trigger CRM enrichment for updated email
  - If no response: send next touch per schedule

Timing (HOT default): Day 1, 3, 7, 10, 17, 21
```

### Step 6: Reply Handling and Meeting Booking

```
On prospect reply:
  - Immediately pause automated sequence
  - Alert rep with: reply content, recommended response, meeting link
  - Rep takes over conversation (human-led from this point)
  - If meeting booked: update CRM opportunity stage
  - If objection: rep handles; agent can draft response if requested

On sequence completion (no reply):
  - Move to CULTIVATE nurture cadence (monthly marketing email)
  - Schedule re-evaluation in 90 days
  - Do NOT archive -- leave on watch list
```

---

## Required Skill Files

| Skill File                      | Purpose                                   |
| ------------------------------- | ----------------------------------------- |
| `lead-scoring`                  | Three-dimension scoring and qualification |
| `prospect-research`             | Deep account and contact research         |
| `sequence`                      | Multi-touch sequence design               |
| `outreach`                      | Individual message drafting               |
| `outreach-sequencing-agent`     | Automated sequence lifecycle management   |
| `lead-intelligence-agent`       | Signal detection triggering this workflow |
| `sales-marketing-global-router` | Routing and jurisdiction identification   |

---

## Escalation / Review Checkpoints

| Checkpoint            | Condition                                     | Reviewer      |
| --------------------- | --------------------------------------------- | ------------- |
| **Score review**      | Lead scored >= 60; ready for outreach         | SDR / AE      |
| **Research complete** | Brief generated with 3+ personalisation hooks | AE            |
| **Touch 1 approval**  | First outreach drafted and awaiting send      | Assigned rep  |
| **Reply received**    | Prospect responded to any touch               | Assigned rep  |
| **Sequence complete** | All touches sent with no response             | Sales Manager |
| **Meeting booked**    | Discovery call confirmed in calendar          | AE            |

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
