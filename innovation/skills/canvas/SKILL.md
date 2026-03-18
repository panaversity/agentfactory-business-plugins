---
name: canvas
description: >
  Activate for: business model canvas, BMC, business model, value proposition,
  customer segments, channels, customer relationships, revenue streams, key
  resources, key activities, key partnerships, cost structure, canvas build,
  canvas stress test, alternative business model, monetisation, pricing model,
  revenue model, how does the business make money, business design, Osterwalder.
  NOT for: unit economics or financial modelling (use financials),
  competitive analysis (use market), pitch deck (use pitch).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/canvas"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, problem_statement, target_customer
- business_model_canvas: current version with all blocks and evidence quality
- customer_profiles: personas, pains, gains, WTP
- key_assumptions: business model assumptions

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: Warning -- "Building a canvas at the IDEA stage is premature. Most blocks will be ASSUMED with no evidence. Consider running /discovery first to get real customer data before designing a business model."
- DISCOVERY: A canvas is useful here -- you can start mapping hypotheses as you learn from customers.
- VALIDATION: This is your focus stage. The canvas should reflect what you are testing and learning.
- MVP: This is your focus stage. The canvas should be updated with pilot data and evidence.
- GROWTH: The canvas should be largely validated. Focus on optimising blocks, not hypothesising.

## DLA PROGRESSION CHECK

If no customer_profiles or discovery data exist in innov.local.md:
"You are building a business model canvas without customer discovery data.
Every block will be hypothetical. Consider running /discovery first --
a canvas grounded in customer evidence is vastly more useful than one
built from assumptions alone."

## BUSINESS MODEL CANVAS WORKFLOW

### Task Types

TYPE 1: CANVAS BUILD (first draft)
Input: Venture context from innov.local.md + any additional context
Output: All 9 blocks with hypotheses, evidence quality, biggest risk, open question

TYPE 2: CANVAS STRESS TEST
Input: Existing canvas
Output: One adversarial question per block + strongest counter-argument

TYPE 3: ALTERNATIVE MODELS
Input: Current canvas
Output: 3 alternative business model configurations with trade-off analysis

TYPE 4: CANVAS UPDATE (post-learning)
Input: Previous canvas version + new validation data
Output: Updated canvas with specific changes highlighted + version increment

TYPE 5: CANVAS HEALTH SUMMARY
Input: Current canvas
Output: Which blocks are validated vs. hypothetical; critical gaps; priority actions

### Canvas Output Structure

```
BUSINESS MODEL CANVAS -- [Venture Name]
Version: [N.N] (post-[stage]) | Date: [Date]
================================================================

1. CUSTOMER SEGMENTS
   Primary:   [Who specifically -- not "SMEs"; name the role and context]
   Secondary: [If applicable; note if different product/price needed]
   Evidence:  [ASSUMED / ANECDOTAL / VALIDATED]
   Risk:      [Biggest risk in this block]
   Open Q:    [The one thing we still need to learn about this segment]

2. VALUE PROPOSITIONS
   Primary:   [The core promise -- specific, differentiated, outcome-focused]
   Secondary: [Supporting value]
   Evidence:  [ASSUMED / ANECDOTAL / VALIDATED]
   Risk:      [What could undermine this value proposition]
   Open Q:    [What the customer might not believe without proof]

3. CHANNELS
   Awareness:  [How customers discover you]
   Evaluation: [How customers decide to buy]
   Purchase:   [How they buy]
   Delivery:   [How they receive value]
   After-sale: [How you retain and grow them]
   Evidence:  [ASSUMED / ANECDOTAL / VALIDATED]
   Risk:      [Scalability; CAC at volume]
   Open Q:    [Which channel needs validation first]

4. CUSTOMER RELATIONSHIPS
   Current:   [How you manage the relationship today]
   Target:    [How it scales]
   Evidence:  [ASSUMED / ANECDOTAL / VALIDATED]
   Risk:      [What breaks when you can no longer do high-touch]
   Open Q:    [Minimum viable onboarding that produces adoption]

5. REVENUE STREAMS
   Primary:   [Pricing model + price point]
   Secondary: [If applicable]
   Evidence:  [ASSUMED / ANECDOTAL / VALIDATED]
   Risk:      [The pricing assumption that has been least tested]
   Open Q:    [What pricing behaviour validates willingness to pay?]

6. KEY RESOURCES
   Critical:  [The resource without which value cannot be delivered]
   Important: [Resources that matter but can be substituted]
   Risk:      [Most fragile resource; what if it disappears?]
   Open Q:    [Which resource must be built/owned vs. rented/accessed?]

7. KEY ACTIVITIES
   Core:      [The activity most central to value creation]
   Growth:    [The activity most central to customer acquisition]
   Risk:      [What the team cannot currently do; capability gap]
   Open Q:    [What activity, if outsourced, would be dangerous?]

8. KEY PARTNERSHIPS
   Critical:  [Partner without whom value cannot be delivered]
   Strategic: [Partner who provides competitive advantage]
   Risk:      [Single-point-of-failure partnerships]
   Open Q:    [Which partnership must be formalised before scaling?]

9. COST STRUCTURE
   Fixed:     [Monthly fixed costs -- list with amounts]
   Variable:  [Per-customer or per-transaction costs]
   Unit cost: [Total cost to serve one customer per month]
   Margin:    [Revenue - unit cost = contribution margin]
   Evidence:  [ESTIMATED / MEASURED]
   Open Q:    [Which cost assumption changes most at 10x scale?]

CANVAS HEALTH SUMMARY:
  Validated blocks:           [List]
  Partially validated:        [List]
  Hypothetical (build risk):  [List]
  Critical gaps:              [Blocks where evidence is weakest vs. risk is highest]
================================================================
```

### Value Proposition Quality Standard

A strong Value Proposition has:

- A specific outcome for a specific customer (not a feature list)
- A differentiated claim (why this, not the alternative)
- Evidence it is valued (customer said it or paid for it)
- A reason the customer cannot easily get this elsewhere

### Alternative Business Model Patterns

When generating alternatives, explore these structural variations:

- Subscription vs. usage-based vs. transaction fee
- Selling to enterprise vs. selling to individual professionals
- Direct vs. marketplace vs. platform
- Free + premium vs. paid only vs. free forever
- Product-led growth vs. sales-led growth
- Build vs. partner vs. white-label

## FINANCIAL REASONING STANDARD

For Revenue Streams and Cost Structure blocks:

- Unit economics first: ensure the unit economics work before projecting revenue
- If LTV:CAC < 3, flag as a serious concern in the canvas
- Churn is the most dangerous assumption: if churn is ASSUMED, flag it
- Always show contribution margin calculation in Cost Structure

## ASSUMPTION TRACKING

After any canvas output:

- Surface which blocks have changed and what evidence supports the change
- Identify the most critical untested assumption across all 9 blocks
- Propose innov.local.md updates for any changed blocks
- Always distinguish between ASSUMED, ANECDOTAL, and VALIDATED evidence

## NEVER DO THESE

- NEVER leave a canvas block empty -- if you don't know: write your assumption
  and mark it ASSUMED; an empty block is a hidden risk
- NEVER mark a block VALIDATED without customer payment or sustained usage data
- NEVER produce a canvas without a health summary showing which blocks
  are validated vs. hypothetical -- this is what tells you where to focus
- NEVER accept "We'll figure out monetisation later" -- Revenue Streams and
  Cost Structure must be at least hypothesised from Day 1

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
