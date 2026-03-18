No `innov.local.md` found — I'll run the retrospective from the results you've shared.

---

# INNOVATION SPRINT RETROSPECTIVE — Sprint 3

**Sprint Goal Recap:**
- **Learning goal:** Validate that AP managers can self-serve onboard without IT involvement (assumption: self-serve onboarding removes the IT-dependency barrier to adoption)
- **Delivery goal:** Build and ship the self-serve onboarding flow; run with 5 pilot AP managers

---

## RESULTS ASSESSMENT

| Metric | Target | Actual | Verdict |
|---|---|---|---|
| Onboarding without IT help | 5/5 (100%) | 4/5 (80%) | **PARTIAL** — 1 failure due to domain whitelisting |
| Onboarding time | ≤ 15 min | 22 min avg | **MISSED** — 47% over target |
| Stated intent to use | 5/5 | 5/5 | **MET** |
| Actual Week 2 logins | 5/5 | 3/5 (60%) | **MISSED** — 40% drop-off |

---

## WHAT WORKED (be specific)

1. **The core onboarding flow works.** 4 of 5 completed it unassisted — this is a real signal that self-serve is viable, not just theoretical.
2. **Pilot recruitment and execution.** Getting 5 real AP managers through the flow in a single sprint is strong execution. We got usable data.
3. **We surfaced a hidden blocker we didn't know about.** The domain whitelisting issue would have been invisible in a demo environment — only a real pilot exposed it.

## WHAT DID NOT WORK (be specific)

1. **22 minutes is too long.** The 15-minute target wasn't arbitrary — AP managers are interruptible. Every extra minute increases abandonment risk. We need to identify which steps consumed the excess 7 minutes.
2. **Stated intent ≠ actual usage.** 5/5 said they'd use the tool; only 3/5 actually logged in during Week 2. This is the most important signal from the sprint — it suggests either (a) the tool didn't deliver enough value on first use to pull them back, (b) they forgot / had no trigger to return, or (c) their workflow didn't naturally create a reason to return within that week.
3. **IT dependency not fully eliminated.** Domain whitelisting is an enterprise IT policy issue outside our onboarding flow. "Self-serve" means nothing if IT has to act first in some environments.

---

## ASSUMPTION UPDATES

These should be written back to `innov.local.md` when you create it:

| Assumption ID | Assumption | Previous Status | New Status | Evidence |
|---|---|---|---|---|
| A-??? | AP managers can self-onboard without IT involvement | UNTESTED | **ANECDOTAL — PARTIALLY VALIDATED** | 4/5 succeeded unassisted. 1 blocked by enterprise domain whitelisting (IT policy, not product UX). n=5; not yet generalizable. |
| A-??? *(NEW)* | AP managers who onboard will return and use the tool regularly | UNTESTED | **ANECDOTAL — AT RISK** | Only 3/5 logged in during Week 2 despite 5/5 stating intent. 40% drop-off after first use. This is now the highest-risk assumption. |
| A-??? *(NEW)* | Enterprise IT policies (domain whitelisting, firewall rules) won't block self-serve onboarding | UNTESTED | **ANECDOTAL — PARTIALLY INVALIDATED** | 1/5 was blocked. If 20% of enterprises require IT action before onboarding, "self-serve" is misleading for that segment. Small n — could be higher or lower at scale. |

---

## CARRY-OVER ASSESSMENT

**Should we keep optimising the onboarding flow (getting from 22 → 15 min)?**

Not yet. The onboarding time miss matters, but the **Week 2 drop-off is a bigger risk.** If users onboard in 15 minutes but still don't come back, we've optimised the wrong thing. Onboarding speed becomes a Sprint 5+ priority once we've validated that people who onboard actually retain.

---

## ONE EXPERIMENT FOR NEXT SPRINT

**Experiment:** Instrument the first-use experience and add a "return trigger" mechanism (e.g., email/Slack notification when an invoice enters their approval queue). Then re-run with the same 5 users (or expand to 8-10) and measure Week 2 return rate.

**Why this experiment:** The 5/5 → 3/5 drop-off is the sharpest signal from Sprint 3. We need to distinguish between three hypotheses:
1. The tool didn't deliver enough value on first use → need to improve first-session experience
2. Users had no reason to return that week → need a trigger/hook
3. Users tried it, decided it wasn't worth switching workflows → deeper problem

Without this data, we're guessing which problem to solve.

---

## NEXT SPRINT PRIORITY

**Sprint 4 Learning Goal:** Validate that AP managers who complete onboarding will return and actively use the tool when given a contextual trigger (testing the retention/activation assumption — now the highest-risk item).

**Sprint 4 Delivery Goal:** Build return-trigger mechanism + first-use instrumentation; run activation experiment with ≥5 pilot users over 2 weeks.

---

> **Critical note:** The gap between stated intent (5/5) and actual behavior (3/5) is a classic innovation trap. People are polite in pilots — they say they'll use it. The only evidence that matters is what they *do*. Sprint 4 must be designed around observed behavior, not reported intent.

---

I'm working without your venture context. Run Exercise 8 from Chapter 40 to build `innov.local.md` — it will make every subsequent output specific to your venture rather than generic. In particular, I had to assign placeholder assumption IDs (A-???) because there's no assumption map to reference. Running `/hypothesis` first would give these proper IDs and risk tiers.
