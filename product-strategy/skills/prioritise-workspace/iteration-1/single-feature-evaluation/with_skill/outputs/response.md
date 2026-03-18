# Feature Evaluation: Slack Integration

This is a single feature evaluation — not a full backlog ranking. Using the single feature evaluation framework.

```
FEATURE EVALUATION: Slack Integration
---------------------------------------------------------
Request source:      Customer (single key customer, churn threat)
Frequency of request: Single customer request with churn ultimatum.
                      No data on whether other customers have
                      requested this. This is important — one
                      customer threatening churn is different from
                      a pattern across the customer base.
User problem:        Customer wants to receive product notifications/
                      updates in Slack rather than switching context
                      to the product dashboard. The underlying
                      problem is context-switching friction.
Alternative solutions:
                      - Email notifications (already exist?)
                      - Webhook integration (customer builds their
                        own Slack bot using our API)
                      - Zapier/Make integration (no-code bridge)
                      - RSS feed of updates
                      The question is whether any of these solve the
                      customer's actual problem without 3 sprints.
Effort:              3 sprints (~6 person-weeks). This is significant
                      — that's 6 weeks of engineering capacity that
                      won't be spent on other roadmap items.
Opportunity cost:    What does NOT get built if we build this?
                      3 sprints is substantial. This displaces
                      roughly one medium-priority roadmap item.
                      The PM needs to name the specific item that
                      gets pushed to answer this honestly.
Confidence in value: LOW — with basis:
                      - Single customer request (no pattern)
                      - Churn threat ≠ churn certainty (customers
                        threaten churn for leverage; many don't follow
                        through)
                      - We don't know if the customer would actually
                        use it daily or if it's a checkbox requirement
                      - No data on whether Slack integration correlates
                        with retention in comparable products

RECOMMENDATION: DISCOVERY SPIKE
Rationale: A 3-sprint investment based on one customer's churn
threat and no broader demand signal is too risky to commit to
directly. The confidence in value is too low for the effort
required. Instead:

1. Survey other customers about Slack integration interest
   (1-2 days)
2. Offer the threatening customer a webhook-based workaround
   (1-2 days to set up) to buy time
3. If survey shows 10%+ interest, escalate to BUILD
4. If only this one customer wants it, have a commercial
   conversation about whether retaining this account at
   3 sprints of engineering cost makes business sense
---------------------------------------------------------
```

**Key insight**: The churn threat creates urgency, but urgency ≠ importance. A 2-day discovery spike (customer survey + workaround offer) costs almost nothing and dramatically increases confidence in the decision.
