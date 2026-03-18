No `innov.local.md` found — I'll work from your conversation context.

---

# MOAT ASSESSMENT — AP Automation Startup

**Date:** 2026-03-19 | **Stage:** MVP/Early Growth (8 months, 15 paying customers)

---

## MOAT TYPE 1 — DATA

**Status: BUILDING — This is your strongest emerging moat.**

- Your AI learns each customer's unique matching rules from historical invoice data. Every invoice processed makes the model better *for that specific customer*.
- After 8 months with 15 customers, you have 15 distinct trained models that a competitor would need months of customer data to replicate.
- **Durability: HIGH** — but only if you architect it correctly. The moat is not "we have data." The moat is "our models improve with each customer's tenure, and a new entrant starts at zero for that customer."

**Critical question:** Is the learning customer-specific only, or does cross-customer learning also occur (e.g., vendor normalization patterns, common GL coding logic)? If cross-customer, the moat compounds — each new customer makes the system smarter for all customers. If customer-specific only, the moat is real but narrower.

**Evidence level: ANECDOTAL** — You know the AI learns. You need to quantify: what is the accuracy at month 1 vs. month 8 for your earliest customers? That curve *is* the moat, expressed as a number.

---

## MOAT TYPE 2 — SWITCHING COSTS

**Status: BUILDING — Moderate and growing.**

- Every customer has trained matching rules embedded in your system. Switching means:
  - Losing months of learned rules
  - Retraining a new system (cost + time + error period)
  - Re-integrating with their ERP/accounting system
  - Staff re-learning workflows
- At 8 months, your earliest customers likely have meaningful switching costs already. By 18 months, switching will feel painful.

**Durability: MEDIUM-HIGH** — increases with tenure. The key metric: what percentage of a customer's invoices are auto-matched without human review? As that number climbs, the cost of "starting over" with a competitor becomes visceral.

**Evidence level: ASSUMED** — You need to measure churn intent and the stated reasons customers stay. "It just works now" = switching cost moat confirmed.

---

## MOAT TYPE 3 — NETWORK EFFECTS

**Status: NOT PRESENT (and that's okay).**

- AP automation is not inherently a network-effects business. Your product does not become more valuable to Customer A because Customer B uses it — unless you build supplier-side features (e.g., a supplier portal where vendors submit standardized invoices).
- If you eventually build a supplier network, this changes. But don't claim it today.

**Durability: N/A currently.**

---

## MOAT TYPE 4 — BRAND

**Status: NOT YET — Too early.**

- At 15 customers and 8 months, you do not have a brand moat. This is normal.
- Brand in AP automation = "the thing the CFO trusts." That takes 3-5 years and case studies.

**Durability: N/A currently.** Invest in collecting testimonials and case studies now; the brand moat is planted by stories, not logos.

---

## MOAT TYPE 5 — REGULATORY / COMPLIANCE

**Status: POTENTIAL — Depends on your market.**

- If you serve regulated industries (healthcare, government, financial services), SOC 2, HIPAA, or FedRAMP certification creates a real barrier. Competitors without certification cannot compete for those customers.
- If you're serving SMBs with no compliance requirements, this moat is irrelevant.

**Evidence level: ASSUMED** — Do your 15 customers require compliance certifications? If even 3-4 do, invest here.

---

## MOAT TYPE 6 — DISTRIBUTION

**Status: NOT YET — But an opportunity.**

- You have no distribution moat at 15 customers. But the path is clear:
  - **ERP integrations** — deep integration with NetSuite, QuickBooks, Sage, or Xero creates a distribution channel (marketplace listing) and adds switching cost simultaneously.
  - **Accounting firm partnerships** — if a firm recommends you to all their clients, that's a distribution moat competitors can't easily replicate.

**Durability: MEDIUM** — Partnerships can change, but deep ERP integrations are sticky.

---

## STRATEGIC RECOMMENDATION

### What you HAVE (defend these):
| Moat | Strength | Action |
|------|----------|--------|
| Data (customer-specific AI) | Emerging | **Quantify the accuracy curve.** Measure month-1 vs. month-8 auto-match rates. This number is your moat, your sales pitch, and your retention story. |
| Switching costs | Growing | **Track it.** Measure auto-match percentage per customer over time. Report it to them — making the moat visible to the customer reinforces it. |

### What you're BUILDING (invest here):
| Moat | Investment | Priority |
|------|------------|----------|
| Cross-customer learning | Architect your AI so patterns learned from one customer (vendor name normalization, common GL mappings) improve predictions for new customers. This turns a linear moat into a compounding one. | **#1 — Highest priority** |
| ERP integration depth | Go deep on 1-2 ERPs rather than shallow on 5. Deep = bi-directional sync, approval workflows, payment triggering. Shallow = CSV import. Deep integrations are moats; shallow ones are features. | **#2** |
| Compliance certification | If any of your 15 customers are in regulated industries, start SOC 2 now. It takes 6-12 months and blocks competitors from your best segments. | **#3 (conditional)** |

### What NOT to invest in yet:
- **Brand** — too early; let case studies accumulate naturally.
- **Network effects** — don't build a supplier portal until you have 200+ customers creating real supplier density.
- **Distribution partnerships** — premature until your product-market fit is locked and you can predictably onboard.

---

## MOST CRITICAL UNTESTED ASSUMPTION

**"Our AI learning creates meaningful switching costs."**

You believe it does. Your customers probably agree anecdotally. But you haven't measured it. The test:

> For your 5 longest-tenured customers, what is the auto-match rate today vs. month 1? If the answer is "65% → 94%," your moat is real and provable. If the answer is "we don't track that," you're flying blind on your core thesis.

Measure this. It's the single most important number in your business.

---

## ASSUMPTIONS MADE IN THIS ANALYSIS

| Assumption | Type | Impact if Wrong |
|------------|------|-----------------|
| AI accuracy improves meaningfully over time per customer | ASSUMED | Core moat thesis collapses — must validate |
| Customers value auto-matching enough to resist switching | ASSUMED | Switching costs lower than believed |
| Cross-customer learning is architecturally feasible | ASSUMED | Moat remains linear, not compounding |
| 15 customers represent a repeatable ICP | ANECDOTAL | Market sizing and moat strategy may need recalibration |

---

*I'm working without your venture context. Run Exercise 8 from Chapter 40 to build `innov.local.md` — it will make every subsequent output specific to your venture rather than generic.*

*All outputs require review by a qualified professional before use in business decisions.*
