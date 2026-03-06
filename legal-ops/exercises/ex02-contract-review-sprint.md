# Exercise 2: Contract Review Sprint -- Three Contracts in One Hour

## Scenario Profile

| Field               | Value                                         |
| ------------------- | --------------------------------------------- |
| **Type**            | Applied Practice                              |
| **Time**            | 60 minutes (20 minutes per contract)          |
| **Skills Required** | `contract-review`, `legal-global-router`      |
| **Plugin Command**  | `/review-contract`                            |
| **Chapter**         | Chapter 22 -- Legal Operations and Compliance |

---

## Overview

You are the Legal Operations Manager at a 150-person technology company.
Three contracts arrived this morning, all requesting review by end of business.

---

## Contract A -- SaaS Vendor Agreement (you are the customer)

If you do not have a real SaaS agreement, generate a training document:

```
/legal-brief topic:"generate a realistic vendor-favourable SaaS MSA for training"
      clauses:"limitation of liability (3 months' fees cap),
               IP ownership (vendor retains all IP including customisations),
               data processing, termination for convenience (60 days vendor;
               immediate for cause only for customer),
               governing law: vendor's state"
```

Then run `/review-contract` against it.

Context: We are the customer. Cloud-based project management software.
Annual value: GBP 48,000. Vendor evaluation in progress for 3 months.
Business unit wants to sign by Friday.

**Answer:**

1. What is the overall risk rating?
2. How many RED items? Are they genuine deal issues?
3. What is the single most important redline given the Friday deadline?
4. Recommend: approve / negotiate / escalate / decline

---

## Contract B -- Consulting Services Agreement (you are the customer)

Context: Engaging an external consultant for a 6-month product strategy project.
Fixed fee: GBP 95,000. Consultant will access product roadmap and customer data.

**Answer:**

1. What IP ownership issues does the agent flag?
2. The agent flags a RED on data protection -- what is the specific issue?
3. The liability cap is GBP 10,000 (~10% of fee). Classification and recommendation?
4. Draft a negotiation strategy email using the top 3 redline suggestions.

---

## Contract C -- Co-Marketing Partnership Agreement

Context: Co-marketing and referral agreement with a complementary software company.
We refer customers to them; they refer to us. No cash. Term: 2 years.

**Answer:**

1. Which clauses are most important for this partnership structure?
2. The contract has a residuals clause. Is this RED? Why?
3. No limitation of liability clause at all. Draft the clause to propose.
4. Write a one-paragraph risk summary for your CFO in plain English.

---

## Sprint Debrief

Which of the three reviews was most valuable? Which produced the most useful
redlines? Which would have benefited most from additional playbook configuration?

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
