---
name: financials
description: >
  Activate for: unit economics, CAC, LTV, customer acquisition cost, lifetime
  value, payback period, churn, gross margin, breakeven, runway, burn rate,
  MRR, ARR, monthly recurring revenue, annual recurring revenue, financial model,
  revenue model, revenue projections, fundraising model, scenario analysis,
  sensitivity analysis, how much money do I need, how long will the money last,
  how many customers to break even, what are my unit economics, Series A readiness.
  NOT for: business model canvas (use canvas), pitch deck (use pitch),
  competitive analysis (use market).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/financials"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type
- financial_model: unit_economics, current_state, milestones
- business_model_canvas: revenue_streams, cost_structure
- key_assumptions: business model assumptions (pricing, churn, CAC)

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: Warning -- "You don't have enough data for a financial model yet. At the IDEA stage, unit economics are pure guesses. Consider running /discovery and /hypothesis first to get evidence-based inputs for your financial model."
- DISCOVERY: Warning -- "Financial modelling at the DISCOVERY stage is early. Your pricing and CAC assumptions are untested. Proceed, but mark everything as ASSUMED and flag high uncertainty."
- VALIDATION: Financial modelling is appropriate -- you should have some evidence from assumption tests.
- MVP: This is your focus stage. Financial models should be grounded in pilot data.
- GROWTH: This is your focus stage. Financial models should use measured data.

## DLA PROGRESSION CHECK

If venture.stage is IDEA or DISCOVERY and no validated pricing or customer data exists:
"You are building a financial model on assumed inputs. The outputs will
look precise but are unreliable. Focus on validating your pricing
assumption and CAC before investing time in detailed financial models."

## FINANCIAL MODELLING WORKFLOW

### Task Types

TYPE 1: UNIT ECONOMICS
  Input: Pricing; CAC inputs; churn assumption; gross margin
  Output: CAC, LTV, LTV:CAC, payback period, contribution margin, breakeven count

TYPE 2: REVENUE AND RUNWAY MODEL
  Input: Starting conditions + growth assumptions
  Output: Month-by-month model (3 scenarios); breakeven date; fundraising trigger

TYPE 3: FUNDRAISING MODEL
  Input: Raise amount; current state; milestones
  Output: What the capital buys; Series A readiness criteria; valuation framework

TYPE 4: SENSITIVITY ANALYSIS
  Input: Base model + key variable ranges
  Output: How breakeven and runway shift under pessimistic assumptions

TYPE 5: SERIES A READINESS ASSESSMENT
  Input: Current metrics
  Output: What metrics Series A investors expect; gap analysis; timeline to readiness

### Unit Economics Output Structure

```
UNIT ECONOMICS MODEL
Venture: [Name] | Currency: [USD / local] | Date: [Date]
================================================================
CUSTOMER ACQUISITION COST (CAC):
  [Method: list all cost inputs and calculation]
  Founder-led CAC:        [Amount] (artificially low -- founder not at market rate)
  Sustainable CAC:        [Amount] (use market-rate founder + any marketing spend)
  [Note: use Sustainable CAC for all planning; Founder-led CAC understates true cost]

LIFETIME VALUE (LTV):
  MRR per customer:       [Amount]
  Annual churn:           [%] (ASSUMED / MEASURED -- specify)
  Average lifetime:       [1 / churn rate = years]
  LTV (gross revenue):    [MRR x 12 x lifetime]
  Gross margin:           [%]
  LTV (gross profit):     [LTV x gross margin]
  [WARNING: If churn is assumed, LTV is unreliable. Validate churn at Month 12.]

KEY RATIOS:
  LTV:CAC ratio:          [LTV / CAC] -- [assessment: <3 poor; 3-5 acceptable; >5 strong; >10 exceptional]
  CAC payback:            [CAC / monthly contribution = months]
  Contribution margin:    [Revenue - variable cost = $ and %]

CASH FLOW BREAKEVEN:
  Monthly fixed costs:    [List major items + total]
  Contribution/customer:  [Monthly revenue x gross margin]
  Breakeven customer N:   [Fixed costs / contribution per customer]
  Timeline to breakeven:  [At current acquisition pace]

KEY WARNINGS:
  [Flag any assumption that is not yet measured]
  [Flag any assumption where a 2x error would change the business viability]
================================================================
```

### Three-Scenario Model Structure

SCENARIO LABELS:
  BASE:         Your realistic expectation
  CONSERVATIVE: Half the growth; 1.5x the churn; 20% higher CAC
  OPTIMISTIC:   1.5x the growth; half the churn; 20% lower CAC

FOR EACH SCENARIO, SHOW MONTH BY MONTH:
  New customers this month | Churned customers | Total customers
  MRR | Monthly burn | Net cash flow | Cumulative cash balance
  Runway remaining (months at current burn)

MARK ON THE MODEL:
  Breakeven date (MRR contribution >= burn)
  Fundraising trigger point (runway < 6 months)
  Series A readiness (target ARR milestone)

### Churn Warning Standard

Churn is the most dangerous assumption in SaaS financial models.
  At 10% annual churn: average lifetime = 10 years; LTV = 10x ARPU x margin
  At 40% annual churn: average lifetime = 2.5 years; LTV = 2.5x ARPU x margin

A 4x difference in churn produces a 4x difference in LTV.
If churn is assumed (not measured), flag the model as:
HIGH UNCERTAINTY -- churn assumption is [X]%, not yet measured.
Model validity depends heavily on this assumption. Validate at Month 12.

### Series A Readiness Framework

General benchmarks (B2B SaaS -- adjust for sector and geography):
  MINIMUM VIABLE METRICS for Series A conversation:
  -- ARR: $1M-$3M (or local equivalent at similar purchasing power)
  -- Growth rate: >100% year-over-year (or >15% month-over-month)
  -- Churn: <10% annual (net revenue retention ideally >100%)
  -- LTV:CAC: >3x (ideally >5x)
  -- At least 3-5 reference customers who will take investor calls

## FINANCIAL REASONING STANDARD

For all financial outputs:
- UNIT ECONOMICS FIRST: Before any revenue projections, establish
  whether the unit economics work. If LTV:CAC < 3, flag as a serious concern.
- CHURN IS THE MOST DANGEROUS ASSUMPTION: Always test the churn
  assumption explicitly. If churn is not yet measured, flag as HIGH RISK.
- RUNWAY IS NON-NEGOTIABLE: Always show runway remaining.
  If runway < 6 months: flag as critical. If < 3 months: flag as existential.
- NEVER PRODUCE PROJECTIONS WITHOUT ASSUMPTIONS STATED:
  Every revenue projection must list the growth rate, churn rate, and
  pricing assumptions that produced it.

## ASSUMPTION TRACKING

After any financial output:
- Surface the most critical untested financial assumption
- Propose innov.local.md financial_model updates with new data
- Always distinguish between ASSUMED and MEASURED inputs
- Flag any input where a 2x error would change the conclusion

## NEVER DO THESE

- NEVER use founder-time CAC as the basis for fundraising models --
  it understates the true cost of customer acquisition at scale
- NEVER present revenue projections without stating all key assumptions
  (growth rate, churn rate, pricing) in the same output
- NEVER show a runway model without a fundraising trigger point --
  the most common startup failure is running out of money because
  the fundraising process started too late
- NEVER call churn "low" without measured data -- assumed churn of 10%
  is not low churn; it is an unvalidated assumption
- NEVER model only the base case -- always include conservative scenario;
  investors will ask "what if growth is half of your base case?"

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
