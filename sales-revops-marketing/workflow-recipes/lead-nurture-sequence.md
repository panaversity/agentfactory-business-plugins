# Workflow Recipe: Lead Nurture Sequence -- End-to-End

## Task Overview

| Field         | Value                                                                         |
| ------------- | ----------------------------------------------------------------------------- |
| **Task Name** | Lead Nurture: From Cold/Warm Classification through Re-Engagement or Archival |
| **Frequency** | Continuous (triggered by lead classification or sequence completion)          |
| **Purpose**   | Keep non-HOT leads engaged until timing signals warrant re-activation         |
| **Owner**     | Marketing Team (nurture cadence) / SDR (re-activation outreach)               |

---

## Trigger Conditions

| Trigger                    | Condition                                               | Action                        |
| -------------------------- | ------------------------------------------------------- | ----------------------------- |
| **WARM scoring**           | Lead scores 35-59 via /score-lead                       | Enter WARM nurture track      |
| **Sequence completed**     | HOT sequence finished with no reply                     | Enter CULTIVATE nurture track |
| **Re-engagement timer**    | 90-day re-evaluation timer fires                        | Run re-scoring workflow       |
| **New signal on nurtured** | Lead Intelligence Agent detects signal on nurtured lead | Evaluate for re-activation    |

---

## Step-by-Step Execution

### Step 1: Classify Nurture Track

```
Input: Lead record with score and history
Actions:
  - Determine nurture track based on entry condition:
    -> WARM (scored 35-59): Monthly value-add content
    -> CULTIVATE (HOT sequence completed, no reply): Monthly marketing email
    -> RE-ENGAGE (dormant > 90 days, score dropped): Quarterly light touch
  - Log nurture track in CRM: NURTURE_TRACK = [WARM/CULTIVATE/RE-ENGAGE]
  - Set re-evaluation timer based on track

Timing:
  - WARM: re-evaluate every 60 days
  - CULTIVATE: re-evaluate every 90 days
  - RE-ENGAGE: re-evaluate every 90 days
```

### Step 2: Build Nurture Content

```
Input: Nurture track + prospect industry + known interests
Actions:
  - Select content based on prospect profile:
    -> Industry-relevant blog posts, whitepapers, case studies
    -> Thought leadership content from content calendar
    -> Event invitations (webinars, conferences)
  - Generate personalised email using content-creation skill
  - Apply jurisdiction compliance overlay for email marketing
  - Do NOT include hard sales CTAs -- value-first approach

Content rules:
  - WARM track: 1 email per month, personalised to industry
  - CULTIVATE track: 1 email per month, marketing newsletter style
  - RE-ENGAGE track: 1 email per quarter, "checking in" with new value
```

### Step 3: Execute Nurture Touches

```
Input: Scheduled nurture content
Actions:
  - Outreach Sequencing Agent manages touch scheduling
  - Before each touch: verify email deliverability
  - Before each touch: check for reply, bounce, or unsubscribe
  - Send via marketing email platform (not personal email)
  - Track: delivery, open, click for each touch

Branch conditions (same as outreach-sequencing-agent):
  - Reply -> STOP nurture, alert SDR, human takes over
  - Bounce -> PAUSE, trigger CRM enrichment for updated email
  - Unsubscribe -> STOP all channels, update CRM DO NOT CONTACT
  - Multiple opens without click -> try different content angle next month
```

### Step 4: Monitor Engagement Signals

```
Ongoing monitoring:
  - Lead Intelligence Agent watches for new signals
  - CRM Hygiene Agent verifies contact data monthly
  - Track engagement metrics across nurture touches:
    -> Open rate trend (improving / stable / declining)
    -> Click rate trend
    -> Content topics that generate engagement

If engagement declining for 3+ consecutive months:
  - Move to RE-ENGAGE track (reduce frequency)
  - Do NOT continue sending to disengaged contacts
```

### Step 5: Re-Evaluation and Re-Scoring

```
When re-evaluation timer fires:
  - Run CRM enrichment for latest company data
  - Run lead scoring with refreshed data
  - Check for any new timing signals since last evaluation

Re-scoring outcomes:
  - Score >= 60 (HOT): RE-ACTIVATE -> exit nurture, enter prospect-to-meeting workflow
  - Score 35-59 (WARM): CONTINUE nurture on current track
  - Score < 35 with engagement: CONTINUE on RE-ENGAGE track
  - Score < 35 with no engagement for 6+ months: route to Step 6
```

### Step 6: Archive or Continue Decision

```
For leads with no engagement and low score:
  - If no activity for 12+ months AND score < 20: archive in CRM
  - If some activity but score < 35: continue RE-ENGAGE quarterly
  - If recently enriched with new data: continue WARM monthly

Archive process:
  - Log archive reason in CRM
  - Do NOT delete record -- mark as ARCHIVED
  - Remove from all active nurture sequences
  - Retain for future bulk re-evaluation (annual)
```

---

## Required Skill Files

| Skill File                      | Purpose                                      |
| ------------------------------- | -------------------------------------------- |
| `lead-scoring`                  | Periodic re-scoring of nurtured leads        |
| `crm-enrichment`                | Data refresh before re-evaluation            |
| `content-creation`              | Nurture email content generation             |
| `outreach-sequencing-agent`     | Nurture touch scheduling and tracking        |
| `lead-intelligence-agent`       | Signal monitoring for re-activation triggers |
| `crm-hygiene-agent`             | Monthly contact data verification            |
| `marketing-performance-agent`   | Nurture campaign performance tracking        |
| `sales-marketing-global-router` | Routing and jurisdiction identification      |

---

## Escalation / Review Checkpoints

| Checkpoint             | Condition                                           | Reviewer          |
| ---------------------- | --------------------------------------------------- | ----------------- |
| **Re-activation**      | Nurtured lead re-scores to HOT (>= 60)              | SDR / AE          |
| **Unsubscribe spike**  | > 0.5% unsubscribe rate on any nurture send         | Marketing Manager |
| **Engagement decline** | 3+ months declining engagement on a track           | Marketing Manager |
| **Archive decision**   | Lead meets archive criteria (12 months, score < 20) | RevOps Lead       |
| **Quarterly review**   | Nurture funnel health: conversion rates, volume     | VP Marketing      |

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
