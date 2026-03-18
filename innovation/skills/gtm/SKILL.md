---
name: gtm
description: >
  Activate for: go to market, GTM, GTM strategy, go-to-market, ICP, ideal
  customer profile, target customer, who to sell to, channel strategy, sales
  channel, how to acquire customers, customer acquisition, outreach strategy,
  LinkedIn outreach, cold email, sales process, sales funnel, pricing strategy,
  price point, pricing tiers, positioning statement, positioning, how to position,
  first customers, early adopters, 90-day plan, launch plan, customer success,
  onboarding, retention.
  NOT for: customer discovery (use discovery), competitive analysis (use market),
  unit economics (use financials), pitch deck (use pitch).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/gtm"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, target_customer
- customer_profiles: personas, pains, gains, WTP, buying_process
- competitive_landscape: differentiation, moat_building
- financial_model: unit_economics (CAC, LTV, pricing)

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: Warning -- "GTM strategy at the IDEA stage is premature. You don't have an ICP grounded in customer evidence yet. Consider running /discovery first."
- DISCOVERY: Warning -- "You don't have a validated ICP yet. GTM strategy requires knowing who your customer is, what triggers their buying, and how they evaluate solutions. Complete discovery first."
- VALIDATION: GTM planning is appropriate -- you should be defining your ICP from validated customer data.
- MVP: This is your focus stage. GTM should be specific, measured, and iterated weekly.
- GROWTH: This is your focus stage for scaling what works.

## DLA PROGRESSION CHECK

If no customer_profiles with validated data exist in innov.local.md:
"You are building a GTM strategy without validated customer profiles.
Your ICP will be based on guesses rather than evidence. Consider
running /discovery to ground your ICP in real customer data."

## GO-TO-MARKET WORKFLOW

### Task Types

TYPE 1: ICP DEFINITION
Input: Problem area; discovery data; current customer data
Output: Primary ICP (role, company, trigger, signals, NOT a fit) + secondary ICP

TYPE 2: POSITIONING STATEMENT
Input: ICP; value proposition; competitive landscape
Output: Positioning statement (For/Who/Our product/That/Unlike/We format)

TYPE 3: CHANNEL STRATEGY
Input: ICP; team constraints; budget; existing assets
Output: Channels ranked by CAC efficiency; Week 1 activation for each

TYPE 4: SALES PROCESS
Input: ICP; product type; sales cycle data
Output: Step-by-step process from lead identification to signed contract

TYPE 5: 90-DAY GTM CALENDAR
Input: Target (N customers by Day 90); channel strategy; team
Output: Week-by-week activity plan with decision gates at Day 30 and Day 60

TYPE 6: PRICING STRATEGY
Input: WTP data from discovery; competitive pricing; unit economics
Output: Pricing tiers; anchoring strategy; discounting policy; trial policy

TYPE 7: CUSTOMER SUCCESS PROGRAMME
Input: Target segment; onboarding complexity; churn risk factors
Output: Day 1-90 success programme with adoption metrics and intervention triggers

### ICP Output Structure

```
IDEAL CUSTOMER PROFILE (ICP)
Venture: [Name] | Version: [N] | Based on: [N discovery interviews + N customers]
================================================================
PRIMARY ICP:
  Company:
    Sector:       [Specific -- not "all industries"]
    Size:         [Revenue band OR headcount band]
    Geography:    [Region / country / city tier]
    Technology:   [What systems they use; what they do NOT use]
    Structure:    [Number of relevant staff; team maturity]

  Person:
    Role:         [Job title -- be specific; CFO != VP Finance != Controller]
    Seniority:    [Level; direct reports; budget authority]
    Cares about:  [Their top 3 professional priorities right now]
    How they buy: [Solo / committee; budget cycle; evaluation process]

  Buying Trigger:
    [The specific event that makes them ready to buy RIGHT NOW]
    Why trigger matters: Customers without a trigger browse but don't buy.

  Signals (how to identify ICP prospects):
    [What they post; what groups they join; what events they attend]

  NOT a fit (explicitly exclude):
    [Who wastes your time -- be specific; saves sales team hours]

SECONDARY ICP (if applicable):
  [Same structure]

ICP CONFIDENCE: [LOW / MEDIUM / HIGH] -- based on [N] paying customers
Next validation: [What ICP assumption still needs more customer data]
================================================================
```

### Positioning Statement Format

For: [Primary ICP -- the specific person]
Who: [The problem they have -- from discovery language]
Our product: [Category name -- what kind of thing it is]
That: [The primary value delivered -- outcome, not feature]
Unlike: [The primary alternative they currently use]
We: [The specific differentiating claim -- why you win]

### Channel Strategy Framework

CHANNEL ARCHETYPES:

FOUNDER-LED OUTREACH (early stage; months 1-6):
CAC: Low (founder time) | Scale: Low | Speed: Fast
Best for: ICP refinement; first 10 customers

CONTENT / THOUGHT LEADERSHIP (months 3-12):
CAC: Medium-low | Scale: Medium | Speed: Slow to start; compounds
Best for: Building inbound pipeline over 6-12 months

COMMUNITY AND ASSOCIATIONS (months 3-9):
CAC: Medium | Scale: Medium | Speed: Medium
Best for: Warm introductions in trust-based markets

REFERRAL PROGRAMME (months 6+):
CAC: Low | Scale: Medium | Speed: Depends on customer base
Best for: Once you have 10+ happy customers

INSIDE SALES (months 9-18; requires funding):
CAC: Medium-high | Scale: High | Speed: Fast once ramped
Best for: Scaling what founder-led sales has proven

PARTNERSHIPS / CHANNELS (months 12+):
CAC: Variable | Scale: High | Speed: Slow to develop
Best for: Distribution leverage through partners

### Pricing Strategy Rules

ANCHOR HIGH, JUSTIFY, THEN TIER:
Start with the highest price you can credibly defend.
Never start low -- it is very hard to raise prices.

VALUE-BASED PRICING PRINCIPLE:
Price should be <10% of the value delivered (the "10% rule").

DISCOUNTING POLICY:
Annual prepay only: 1-2 months free for annual commitment.
No arbitrary discounts: customers who price-negotiate before signing churn faster.

TRIAL POLICY:
Paid trial preferred over free trial.
Trial with LOI preferred: require a letter of intent before granting trial access.

## ASSUMPTION TRACKING

After any GTM output:

- Surface the most critical untested GTM assumption (ICP, channel, pricing)
- Propose innov.local.md updates for customer profiles or competitive landscape
- Always distinguish between ASSUMED, ANECDOTAL, and VALIDATED evidence

## NEVER DO THESE

- NEVER define ICP as a demographic without a buying trigger --
  "CFOs at $10M companies" is a description; add the trigger
- NEVER launch multiple channels simultaneously without measuring each
- NEVER set pricing based on competitor pricing alone -- price based on
  value delivered and unit economics
- NEVER skip the "NOT a fit" section of the ICP
- NEVER design a customer success programme that assumes high-touch
  is sustainable at scale

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
