# Exercise 1: Build Your Negotiation Playbook

## Scenario Profile

| Field               | Value                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| **Type**            | SKILL.md Configuration                                                 |
| **Time**            | 60-90 minutes                                                          |
| **Skills Required** | `contract-review`, `legal-global-router`, `legal.local.md.template`    |
| **Prerequisite**    | Legal Ops plugin installed; access to 3 recently negotiated agreements |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance                          |

---

## Overview

The negotiation playbook is the single most important configuration decision in your
Legal Ops plugin deployment. Without it, every review is generic. With it, every review
reflects your organisation's actual risk tolerance and negotiation history.

---

## Steps

### Step 1 -- Conduct the Expert Interview (30 minutes)

Before opening the plugin, conduct a structured interview with your General Counsel
or most senior commercial attorney. Use these questions exactly:

1. In a typical vendor agreement where you are the customer, what is your standard
   position on limitation of liability? What is the absolute minimum you would accept?
2. Which IP clauses are truly non-negotiable -- where you would decline the deal?
3. In the last 12 months, which clause caused the most negotiation difficulty?
4. Which contract types do you personally review? Which delegate to juniors?
5. What looks acceptable on paper but your instinct always flags in practice?

Record the answers verbatim.

### Step 2 -- Document Extraction

For each of your three most recently negotiated vendor agreements:

- What was the starting position on the three most-negotiated clauses?
- What was the final agreed position?
- Was the compromise one your organisation was comfortable with?

### Step 3 -- Draft Your Playbook

Using the `legal.local.md.template`, draft your playbook covering at minimum:
limitation of liability, IP ownership, indemnification, data protection,
termination, and governing law.

### Step 4 -- Test and Calibrate

```
/review-contract
[Upload: one of the three executed contracts from Step 2]

Context: provide your position, urgency level, and any known issues
```

Compare the agent's output against your knowledge of the actual negotiation:

- Did the agent flag the clauses that actually required negotiation?
- Were any significant issues missed?
- Were the GREEN/YELLOW/RED classifications consistent with your risk tolerance?

### Step 5 -- Refine and Re-test

Update your playbook based on the gaps. Re-run the review. Document changes.

---

## Expected Output

- A validated `legal.local.md` negotiation playbook
- Documentation of calibration changes (what was adjusted and why)
- Comparison showing agent output vs. actual negotiation history

---

## Deliverable

A validated negotiation playbook ready to deploy as your organisation's
Legal Ops plugin configuration.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
