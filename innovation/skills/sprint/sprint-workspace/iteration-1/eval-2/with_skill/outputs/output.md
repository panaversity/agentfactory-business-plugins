No `innov.local.md` found, so I'll work from your conversation context. I need to make assumptions about the risk tiers of your assumptions since I don't have their definitions. I'll assign tiers based on what the assumption names imply, then score each item.

---

## BACKLOG PRIORITISATION — Assumption Risk × Delivery Value

### Assumption Tier Assignments (inferred)

| ID | Assumption | Inferred Tier | Rationale |
|---|---|---|---|
| A-003 | Self-serve adoption | TIER 1 (existential) | If customers can't onboard without hand-holding, the business model breaks at scale |
| A-004 | Volume handling | TIER 1 (existential) | If the product can't handle real invoice volumes, core value prop fails |
| A-005 | ERP compatibility | TIER 2 (serious) | Limits addressable market but doesn't kill the product outright |
| A-006 | Customization need | TIER 2 (serious) | Determines stickiness and competitive differentiation |
| A-007 | Team collaboration | TIER 3 (important) | Enhances workflow but not existential |
| A-008 | Mobile workflow | TIER 3 (important) | Convenience feature; unlikely to be a dealbreaker |
| A-009 | Channel viability | TIER 2 (serious) | Tests an entire go-to-market path |

**If these tier assignments are wrong, the priority order changes — tell me and I'll rescore.**

---

### Scoring

| # | Item | Assumption Risk (1-3) | Delivery Value (1-3) | Priority Score | Notes |
|---|---|---|---|---|---|
| 1 | Self-serve onboarding wizard | **3** (Tier 1: A-003) | **3** (unblocks scalable acquisition) | **9** | Highest priority. Tests whether customers can adopt without sales touch. |
| 6 | Bulk invoice upload via CSV | **3** (Tier 1: A-004) | **3** (blocks proof that core product works at real volume) | **9** | Tied for top. Without volume handling, pilots fail. |
| 4 | Multi-ERP support for NetSuite | **2** (Tier 2: A-005) | **3** (blocks expansion to NetSuite segment — critical path to TAM) | **6** | High. Opens a major market segment. |
| 7 | Custom matching rule editor | **2** (Tier 2: A-006) | **2** (enables learning on customization, not on critical path) | **4** | Medium. Worth doing but not before existential assumptions are tested. |
| 10 | White-label for resellers | **2** (Tier 2: A-009) | **2** (tests a GTM channel but not blocking current path) | **4** | Medium. High learning value but heavy build — consider a lighter test first. |
| 2 | Slack integration for exception routing | **1** (Tier 3: A-007) | **2** (enables faster pilot workflows) | **2** | Low. Backlog unless quick win (<3 points). |
| 9 | Mobile approval interface | **1** (Tier 3: A-008) | **1** (nice to have, no dependency) | **1** | Low. Park it. |
| 3 | Dashboard with matching accuracy metrics | **0** (no assumption) | **2** (useful for demos and trust-building) | **0** | No assumption tested. Only pull in if it supports a sprint's learning goal. |
| 5 | Email notification system | **0** (no assumption) | **1** (commodity feature, no learning) | **0** | No assumption tested, no critical dependency. Bottom of backlog. |
| 8 | API documentation for IT teams | **—** | **—** | **DROP** | **Red flag.** This *contradicts* A-003 (self-serve adoption). If your thesis is that customers onboard themselves, building IT-team documentation signals you're hedging toward an enterprise sales motion. Either A-003 is wrong (and you should test that first), or this item undermines your strategy. Do not build it until A-003 is resolved. |

---

### Recommended Priority Order

```
PRIORITY   ITEM                              SCORE   ACTION
────────────────────────────────────────────────────────────
  1        Self-serve onboarding wizard         9     Sprint 1 — existential test
  2        Bulk invoice upload via CSV          9     Sprint 1 — existential test
  3        Multi-ERP support (NetSuite)         6     Sprint 2 — market expansion
  4        Custom matching rule editor          4     Sprint 2/3 — stickiness test
  5        White-label for resellers            4     Sprint 3 — consider lighter MVP test first
  6        Slack integration                    2     Backlog — pull in as quick win only
  7        Mobile approval interface            1     Backlog — park
  8        Dashboard (accuracy metrics)         0     Backlog — attach to a learning goal or skip
  9        Email notifications                  0     Backlog — commodity, defer
  ✕        API docs for IT teams               DROP   Contradicts A-003 — resolve assumption first
────────────────────────────────────────────────────────────
```

### Key Calls

1. **Sprint 1 should target items 1 + 6 together.** The onboarding wizard gets users in; bulk upload proves the product works at real volume. Together they test: "Can a customer self-serve onboard AND process real invoice volumes?" — that's your existential gate.

2. **Item 8 (API docs) is a strategic contradiction**, not just a low-priority item. If you find yourself wanting to build it, that's a signal A-003 may be wrong. Test A-003 first, then decide.

3. **Item 10 (white-label) scores 4 but is likely heavy.** Before committing a full sprint, consider whether there's a lighter way to test A-009 (e.g., a partner conversation or a fake-door test with a reseller).

---

I'm working without your venture context. Run Exercise 8 from Chapter 40 to build `innov.local.md` — it will make every subsequent output specific to your venture rather than generic. In particular, I had to **guess your assumption tier levels** — with `innov.local.md` those would be explicit and the scoring would be precise.

Want me to plan Sprint 1 around items 1 and 6?
