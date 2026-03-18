# RICE Prioritisation: 5 Backlog Items

## Context Loading

No `product.local.md` found. Working with the information provided in the backlog.

## Framework Selection

> "We have too many features and need to rank them"

Using **RICE** (Reach, Impact, Confidence, Effort).

---

## RICE Scoring

### Scoring Assumptions

Before the table, here are the assumptions behind each score:

1. **Bulk export** — Reach is limited to the 3 requesting enterprise customers (say ~5% of user base). Impact is moderate (2) — it unblocks a workflow but isn't transformational. Confidence is medium (60%) — we know they want it but haven't validated exact scope. Effort: 2 sprints (standard data pipeline work).

2. **SSO integration** — Reach is narrow (the 2 enterprise deals = ~3% of users), but Impact is significant (3) — it's a blocker, not an enhancement. Confidence is high (90%) — we have signed deal contingencies. Effort: 3 sprints (identity provider integration, testing across IdPs).

3. **Dashboard performance** — Reach is 100% (all users hit the dashboard). Impact is moderate (2) — 5s load is painful but not broken. Confidence is high (85%) — we have APM data showing the bottleneck. Effort: 2 sprints (query optimisation, caching).

4. **Mobile app notifications** — Reach ~40% (mobile users subset). Impact is minimal (1) — nice-to-have, not solving a burning problem. Confidence is medium (50%) — no usage data on mobile notification preferences. Effort: 1 sprint (low effort as stated).

5. **API rate limiting** — Reach ~15% (API-heavy customers). Impact is moderate (2) — prevents abuse and improves reliability. Confidence is low (40%) — no customer requests, internal assessment only. Effort: 2 sprints (rate limiter, monitoring, documentation).

### RICE Table

| Item | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|---|---|---|---|---|---|
| Dashboard performance | 100% | 2 | 85% | 2 sprints | **85.0** | 1 |
| Mobile app notifications | 40% | 1 | 50% | 1 sprint | **20.0** | 2 |
| SSO integration | 3% | 3 | 90% | 3 sprints | **2.7** | 3 |
| Bulk export | 5% | 2 | 60% | 2 sprints | **3.0** | 3 |
| API rate limiting | 15% | 2 | 40% | 2 sprints | **6.0** | 4 |

*RICE = (Reach × Impact × Confidence) / Effort*

**Note:** These scores are only as good as the estimates behind them. A score from bad data is worse than no score — it creates false precision.

Recalculated and re-ranked:

| Item | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|---|---|---|---|---|---|
| Dashboard performance | 100% | 2 | 85% | 2 sprints | **85.0** | 1 |
| Mobile app notifications | 40% | 1 | 50% | 1 sprint | **20.0** | 2 |
| API rate limiting | 15% | 2 | 40% | 2 sprints | **6.0** | 3 |
| Bulk export | 5% | 2 | 60% | 2 sprints | **3.0** | 4 |
| SSO integration | 3% | 3 | 90% | 3 sprints | **2.7** | 5 |

---

## The Three Mandatory Challenges

### CHALLENGE 1: STRATEGIC OVERRIDE TEST

Is there any item that scored low that you would build anyway?

**Yes — SSO integration.** It scored #5 by RICE (2.7) because its Reach is tiny (3% of users). But it's blocking **$120K ARR** in enterprise deals. This is a textbook strategic override:

- **Override reason**: Enterprise deal dependency — two signed deals contingent on SSO.
- **Why this is valid**: RICE penalises low-reach items, but $120K ARR from 2 customers can justify a 3-sprint investment regardless of reach percentage.
- **Documentation**: This override must be recorded explicitly. If we don't document it, next quarter someone will look at the RICE scores and ask why we built the #5 item.

### CHALLENGE 2: DATA GAP TEST

Items with confidence below 50%:

**API rate limiting (Confidence: 40%)**
- What would raise confidence above 70%? Usage data on current API abuse patterns. Are customers actually hitting issues? How many requests/second do heavy users make?
- Can we get this in a 2-week discovery spike? Yes — instrument the API gateway, run for 2 weeks, analyse patterns.
- **Should we spike before committing?** Yes. This is a low-confidence, high-effort (2 sprints) item. Rule: low-confidence, high-effort items should almost always have a discovery spike before they enter a sprint.

**Mobile app notifications (Confidence: 50%)**
- What would raise confidence? Survey of mobile users on notification preferences, push notification opt-in rate data.
- Can we get this in a 2-week spike? Partially — we could run an in-app survey and check existing analytics.
- **Should we spike?** It's borderline. Effort is low (1 sprint) so the cost of being wrong is small. A lightweight survey would help but isn't strictly necessary.

### CHALLENGE 3: "WHAT WOULD WE REGRET?" TEST

Ignoring all scores: which item, if we shipped nothing else this quarter, would our best customers be most grateful for?

**Dashboard performance.** A 5-second page load affects every single user, every single session. It's the kind of thing that erodes trust silently — users don't file tickets about slow dashboards, they just stop logging in.

Does it match the top scorer? **Yes** — Dashboard performance is #1 in both the RICE ranking and the regret test. This is a strong signal that the scoring is aligned with reality.

---

## Quarterly Priority Decision

```
QUARTERLY PRIORITY DECISION
================================================================
PRIORITY 1 (must ship):
  Dashboard performance -- Affects 100% of users, high confidence,
  and matches the regret test. No-brainer.

PRIORITY 2 (ships if P1 goes well):
  SSO integration -- Strategic override: $120K ARR in enterprise
  deals contingent on this. Low RICE score but high business value.

STRETCH GOAL (ships if capacity allows):
  Mobile app notifications -- Low effort (1 sprint), quick win
  for mobile users if bandwidth opens up.

EXPLICITLY NOT BUILDING THIS QUARTER:
  Bulk export -- Low reach (3 customers), moderate effort.
  Revisit when enterprise customer count grows or if it becomes
  a pattern across more accounts.

  API rate limiting -- Low confidence (40%). Discovery spike
  recommended before committing engineering time.

STRATEGIC OVERRIDES DOCUMENTED:
  SSO integration -- Override reason: enterprise deal dependency
  ($120K ARR from 2 deals). RICE score of 2.7 overridden due to
  direct revenue impact.

DISCOVERY SPIKES RECOMMENDED:
  API rate limiting -- Spike question: What are actual API abuse
  patterns? Instrument gateway for 2 weeks to get usage data
  before committing 2 sprints of engineering.
================================================================
```
