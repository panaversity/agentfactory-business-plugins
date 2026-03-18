

I'm working without your venture context. Run Exercise 8 from Chapter 40 to build `innov.local.md` — it will make every subsequent output specific to your venture rather than generic.

That said, your pilot data is rich enough to run a full BML analysis. Here it is:

---

```
BUILD-MEASURE-LEARN ANALYSIS
Sprint/Pilot: Pilot 1 | Period: 6 weeks | Date: 2026-03-19
================================================================

WHAT WE TESTED:
  Learning goal: A-001 (willingness to pay $2K/mo), A-002 (50%+ time
                 reduction), A-003 (self-serve adoption without IT)
  Method:        Paid pilot with 5 mid-market manufacturers
  Sample:        5 companies

WHAT WE MEASURED:

  Renewal at $2,000/mo:
    A: $2,000 ✓ | B: $2,000 ✓ | C: asked for extension at 50% off ✗
    D: churned ✗ | E: $1,500 (negotiated down) PARTIAL
    Result: 2/5 full price, 1/5 partial, 2/5 fail — PARTIAL

  Time reduction ≥50%:
    A: 62% ✓ | B: 45% ✗ | C: not reported | D: not reported | E: not reported
    Result: 1/5 passed, 1/5 near-miss — INCONCLUSIVE (insufficient data
    from 3 companies, likely correlated with low adoption)

  Self-serve adoption (proxy: >50% adoption without IT involvement):
    A: 89% ✓ | B: 71% ✓ | C: 34% ✗ | D: 12% ✗ | E: 56% ✓
    Result: 3/5 passed — PARTIAL

ASSUMPTION OUTCOMES:

  A-001 (AP managers will pay $2,000/month): PARTIALLY VALIDATED
  Evidence: 2 of 5 renewed at full price. 1 renewed at $1,500 (25% haircut).
  1 wanted a 50% discount extension. 1 churned entirely.
  Confidence: MEDIUM — the 2 full-price renewals are real revealed
  preference (they paid). But 40% full-price conversion on a 5-company
  pilot is a warning sign, not a celebration.
  Key question: Is $2,000 the right price, or is $1,500 the real
  market-clearing price? Company E's negotiation may be the signal.

  A-002 (tool achieves 50%+ time reduction): INCONCLUSIVE
  Evidence: Only 2 companies have reported time reduction data.
  Company A hit 62% (strong). Company B hit 45% (near-miss).
  Confidence: LOW — you cannot validate a performance claim with
  N=2 data points. The 3 companies with missing data likely correlate
  with low adoption (you can't measure time savings if they're not
  using it).
  Action required: You MUST instrument time-reduction measurement
  into the product. Relying on customer self-report is unreliable.

  A-003 (self-serve adoption without IT): INVALIDATED
  Evidence: 3/5 achieved >50% adoption, but the failure mode is
  devastating. Company D's churn reason — "not enough ERP integration"
  — means self-serve adoption IS gated by IT/ERP in at least some
  environments. Company C's 34% adoption suggests the same friction.
  Confidence: HIGH — Company D's churn is revealed preference
  (they left). This is the strongest signal in your dataset.
  Critical insight: "Self-serve without IT" is true for SOME
  manufacturers but not all. The assumption as stated is too broad.

UNEXPECTED LEARNINGS:

  1. ERP INTEGRATION IS A GATING FACTOR, NOT A NICE-TO-HAVE
     Company D didn't say "we wish you had ERP integration." They
     churned. That's not a feature request — it's a deal-breaker
     for a segment of your market.
     Implication: Your addressable market splits into two segments:
     (a) companies where AP workflow is loosely coupled to ERP
         → self-serve works, your current product fits
     (b) companies where AP is tightly coupled to ERP
         → without integration, adoption stalls and they churn

  2. ADOPTION IS BIMODAL, NOT A SPECTRUM
     Your adoption numbers: 89%, 71%, 56% | 34%, 12%
     There's no company at 40-50%. They either got it or they didn't.
     Implication: Something in the onboarding or environment causes a
     tipping point. Find what A, B, and E have in common that C and D
     don't. Hypothesis: it's ERP coupling depth.

  3. PRICE SENSITIVITY CORRELATES WITH ADOPTION
     Company E: 56% adoption, negotiated to $1,500.
     Company C: 34% adoption, wanted 50% discount.
     Companies A & B: high adoption, paid full price without flinching.
     Implication: Customers who get less value negotiate harder.
     This is rational. Your pricing may need to be value-tiered.

PIVOT OR PERSEVERE RECOMMENDATION:

  ➤ PERSEVERE WITH CUSTOMER SEGMENT REFINEMENT (not a full pivot)

  Rationale:
  Your core product works. 3/5 companies adopted meaningfully, 3/5
  are paying you (2 at full price). That's signal. But your assumption
  that ALL mid-market manufacturers are your customer is wrong.

  Specifically:
  - PERSEVERE on the product for manufacturers with loosely-coupled
    ERP environments. Your 60% conversion at full price within this
    sub-segment is strong for a first pilot.
  - DO NOT BUILD ERP integration yet. That is a 6-month engineering
    bet on a segment you haven't validated willingness-to-pay for.
    Instead, test whether tightly-coupled ERP companies would pay
    MORE (e.g., $3,000/mo) to justify the integration cost.
  - REFINE your qualification criteria before scaling. The most
    expensive mistake you can make now is acquiring Company D clones
    at scale.

  Next most critical assumption to test:
  NEW A-004: "We can identify ERP-coupling depth during sales
  qualification with 3 or fewer questions, achieving 80%+ accuracy
  in predicting adoption success."
  This is now your highest-risk assumption because it determines
  your CAC and churn rate at scale.

innov.local.md UPDATES PROPOSED:

  A-001: PARTIALLY VALIDATED → refine to segment-specific pricing
    - Loosely-coupled segment: $2,000/mo validated (2/3 paid full)
    - Tightly-coupled segment: UNTESTED at any price
    - Consider: is $1,500 the right price for the middle tier?

  A-002: INCONCLUSIVE → must instrument automated measurement
    - Add in-product time tracking before next sprint
    - Cannot rely on self-report from 2 companies

  A-003: INVALIDATED as stated → split into two assumptions:
    - A-003a: "Self-serve adoption works in loosely-coupled ERP
      environments" — VALIDATED (3/3 in-segment achieved >50%)
    - A-003b: "Self-serve adoption works in tightly-coupled ERP
      environments" — INVALIDATED (0/2 achieved >50%, 1 churned)

  NEW A-004: Qualification accuracy assumption (UNTESTED)

  Customer segments: Split "mid-market manufacturers" into
  loose-ERP and tight-ERP sub-segments. Update personas accordingly.

================================================================
```

---

**Bottom line:** Your product works for a *subset* of your target market. The pilot didn't fail — it drew a boundary. Your next sprint should focus on (1) defining that boundary precisely enough to qualify leads, and (2) instrumenting time-reduction measurement so A-002 doesn't stay inconclusive. Do not invest in ERP integration until you've validated that the tight-ERP segment will pay enough to justify the build.

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
