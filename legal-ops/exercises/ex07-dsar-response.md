# Exercise 7: DSAR Response -- The 30-Day Clock

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Type**            | Process Simulation                            |
| **Time**            | 45 minutes                                    |
| **Skills Required** | `dsar-privacy`, `legal-global-router`         |
| **Plugin Command**  | `/legal-brief`                                |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance |

---

## Overview

At 09:17 this morning, the following email arrived at privacy@yourcompany.com:

> "Dear Sir/Madam, I am writing to request all personal data that your company
> holds about me under Article 15 of the GDPR. My name is Sarah Johnson. I was
> a customer from March 2021 to June 2023. My email address at that time was
> sarah.johnson.42@gmail.com. Please confirm receipt and advise when I can expect
> a response. Regards, Sarah Johnson."

You are the Privacy Officer. The 30-day GDPR clock started at 09:17.

---

## Steps

### Day 1 -- Acknowledge Immediately

```
/legal-brief topic:"DSAR-acknowledgement"
         requester-name:"Sarah Johnson"
         requester-email:"sarah.johnson.42@gmail.com"
         request-date:"[today]"
         request-type:"Subject Access Request (Article 15 UK GDPR)"
         jurisdiction:"UK GDPR"
```

Review: does it confirm receipt, state deadline, set out identity verification,
and avoid confirming or denying data held? This letter goes out today.

### Days 1-10 -- Data Discovery

```
/legal-brief topic:"DSAR-data-discovery"
         requester:"Sarah Johnson, sarah.johnson.42@gmail.com"
         customer-period:"March 2021 to June 2023"
         systems:"CRM, billing, email, customer support,
                  marketing database, HR system"
```

The agent drafts internal discovery requests to each system owner (Day 10 deadline).

### Day 12 -- Data Received (Simulate)

The following has been identified:

- CRM: Full customer record, purchase history, support tickets, sales rep notes
  (including: "difficult customer -- always pushes for discounts")
- Billing: Invoice history, last 4 digits of payment card, billing address
- Email: 47 support emails
- Marketing: Campaign history, open/click tracking, preference settings
- HR system: No data found
- Legal case management: No data found

```
/legal-brief topic:"DSAR-response-preparation"
         data-found:[provide summary above]
         redaction-required:"third-party personal data in support tickets;
           internal staff personal data; commercially sensitive info"
         jurisdiction:"UK GDPR"
```

### Day 15 -- Response Draft

Draft the final response letter: categories of data held, how it is processed,
legal basis, retention periods, and information about Sarah's rights.

Route for attorney review before sending.

---

## Reflection Questions

1. The sales rep's CRM note calls Sarah a "difficult customer." Is this personal
   data she is entitled to see under Article 15? (Answer: YES)

2. If Sarah had also requested erasure under Article 17, how would the workflow
   change? Which step requires immediate escalation?

3. Your response is ready on Day 28. Then IT discovers a legacy database with
   Sarah's data not included in discovery. What do you do?

---

## Deliverable

Completed DSAR simulation demonstrating the full 30-day workflow, with a validated
DSAR Agent SKILL.md and documented process map.

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
