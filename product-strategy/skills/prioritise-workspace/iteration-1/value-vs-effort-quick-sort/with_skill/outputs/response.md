# Value vs. Effort Matrix

You asked for a quick 2x2 — no complex scoring. Here it is.

## Framework Selection

> "We need a quick 2x2 without complex scoring"

Using **Value vs. Effort matrix**.

## Assumptions

Before placing items, here are the assumptions behind value and effort estimates:

| Item | Value Rationale | Effort Rationale |
|---|---|---|
| Notification preferences | **Medium value** — quality-of-life improvement, reduces noise complaints. Not a deal-maker. | **Low effort** — UI settings page + backend filtering. Well-understood pattern. |
| Bulk user import | **High value** — enterprise onboarding blocker. Manual imports waste CSM time and delay time-to-value. | **Medium effort** — CSV parsing, validation, error handling, edge cases (duplicates, encoding). |
| SSO | **High value** — enterprise requirement, often a procurement checkbox. Blocks deals. | **High effort** — Identity provider integration, SAML/OIDC, multi-IdP testing, security review. |
| Dark mode | **Low value** — cosmetic preference. Rarely a purchase/retention driver. | **Low effort** — CSS variables, theme toggle. Mostly styling work. |
| API webhooks | **High value** — enables integrations, automation, and ecosystem growth. Developers expect it. | **Medium effort** — event system, retry logic, webhook management UI, security (signing). |
| Custom dashboard layouts | **Medium value** — power users want it, most users don't care. | **High effort** — drag-and-drop, layout persistence, responsive grid, widget system. |

## The 2x2 Matrix

```
                        HIGH VALUE
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        │   STRATEGIC BETS  │    QUICK WINS     │
        │                   │                   │
        │   • SSO           │  • Bulk user      │
        │                   │    import         │
        │                   │  • API webhooks   │
        │                   │                   │
HIGH ───┼───────────────────┼───────────────────┤─── LOW
EFFORT  │                   │                   │   EFFORT
        │     AVOID         │    FILL-INS       │
        │                   │                   │
        │   • Custom        │  • Dark mode      │
        │     dashboard     │  • Notification   │
        │     layouts       │    preferences    │
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                        LOW VALUE
```

**Quick Wins** (high value, low effort): Bulk user import, API webhooks — do these first.
**Strategic Bets** (high value, high effort): SSO — commit only if strategically justified.
**Fill-ins** (low value, low effort): Dark mode, Notification preferences — do when capacity allows.
**Avoid** (low value, high effort): Custom dashboard layouts — don't build this quarter.

---

## The Three Mandatory Challenges

### CHALLENGE 1: STRATEGIC OVERRIDE TEST

Is there any item that scored low that you would build anyway?

**Custom dashboard layouts** — if a major enterprise deal or strategic partnership requires it, this could become an override. But right now, no evidence justifies it. No override documented.

**SSO** — placed in Strategic Bets (high effort), but if there are active enterprise deals contingent on SSO, it should be treated as a Quick Win regardless of effort. Check with sales.

### CHALLENGE 2: DATA GAP TEST

Items with uncertain value:
- **Notification preferences**: How many support tickets are about notification noise? If it's a top-5 complaint, the value is higher than estimated.
- **Dark mode**: Do we have feature request data? If 30%+ of users have asked, it's worth reconsidering.

No discovery spikes needed — these are all low-effort items where the cost of being wrong is small.

### CHALLENGE 3: "WHAT WOULD WE REGRET?" TEST

Ignoring the matrix: which item, if we shipped nothing else this quarter, would our best customers be most grateful for?

**Bulk user import.** Enterprise customers manually uploading users one-by-one during onboarding is painful and visible. It's the kind of thing that makes your product feel amateur.

Does it match the matrix? **Yes** — it's in Quick Wins. Good alignment.

---

## Summary Priority

1. **Bulk user import** (Quick Win + regret test winner)
2. **API webhooks** (Quick Win, enables ecosystem)
3. **SSO** (Strategic Bet — validate with sales first)
4. **Notification preferences** (Fill-in, low effort)
5. **Dark mode** (Fill-in, cosmetic)
6. **Custom dashboard layouts** (Avoid this quarter)
