---
name: pitch
description: >
  Activate for: pitch, investor deck, fundraising, pitch deck, pitch narrative,
  investor presentation, raise money, seed round, Series A, SAFE, convertible note,
  valuation, investor story, narrative architecture, pitch slides, executive summary,
  investor email, one pager, funding, angel investor, venture capital, VC pitch,
  pitch practice, hard questions, investor Q&A, term sheet, data room, investor brief.
  NOT for: unit economics or financial modelling (use financials),
  business model canvas (use canvas), market sizing (use market).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/pitch"
---

## CONTEXT LOADING

Before executing, check for `innov.local.md` in the working directory.
If found, extract:

- venture: name, stage, type, problem_statement, solution_hypothesis, unfair_advantage
- financial_model: unit_economics, current_state, milestones
- business_model_canvas: all blocks with evidence quality
- competitive_landscape: direct_competitors, differentiation, moat_building
- fundraising: current_round, investor_pipeline, data_room_status
- customer_profiles: personas, WTP, buying_process

If `innov.local.md` is not found:
Continue with conversation context. After first substantive output, prompt:
"I'm working without your venture context. Run Exercise 8 from Chapter 40
to build innov.local.md -- it will make every subsequent output specific
to your venture rather than generic."

## STAGE-AWARE CALIBRATION

Check venture.stage and calibrate:

- IDEA: Warning -- "You have no traction to pitch. Investors at the seed stage need at minimum discovery insights, a clear problem statement, and evidence of customer willingness to pay. Consider running /discovery and /hypothesis first."
- DISCOVERY: Warning -- "Pitching at the DISCOVERY stage is early. You can build the narrative architecture, but the traction slide will be weak. Focus on completing discovery and getting LOIs before pitching."
- VALIDATION: Pitching is appropriate if you have pilot results or LOIs.
- MVP: This is a strong pitching stage -- you should have real metrics.
- GROWTH: This is your focus stage for fundraising -- strong traction story.

## DLA PROGRESSION CHECK

If no financial_model or business_model_canvas data exists in innov.local.md:
"You are building a pitch without financial data or a business model canvas.
Your Slide 6 (Business Model) and Slide 4 (Market) will be weak.
Consider running /canvas and /financials first."

## PITCH AND FUNDRAISING WORKFLOW

### Task Types

TYPE 1: PITCH DECK NARRATIVE
Purpose: Build the narrative architecture for a full investor pitch deck.
Input: Venture context + traction + raise details + investor type
Output: 9-slide structure with headline, content, verbal script, emotional job

TYPE 2: HARD QUESTIONS PREP
Purpose: Prepare for the 15 hardest questions investors will ask.
Input: Venture context + investor type + known weaknesses
Output: Question + honest answer + what to do before the pitch if no good answer

TYPE 3: EXECUTIVE SUMMARY
Purpose: One-paragraph (100-word) venture summary for investor email intro.
Input: Venture context
Output: Problem, solution, traction, ask, why worth their time -- specific, no cliches

TYPE 4: INVESTOR RESEARCH BRIEF
Purpose: Pre-meeting brief on a specific investor.
Input: Investor name / firm
Output: Portfolio, known thesis, past questions from public sources, 5 likely hard questions

TYPE 5: TERM SHEET ANALYSIS
Purpose: Identify non-standard terms in a term sheet.
Input: Term sheet (or key terms)
Output: Standard vs. non-standard; what to push back on; what is acceptable

### Pitch Deck Narrative Structure

9 SLIDES -- NARRATIVE ARC:

SLIDE 1: THE HOOK -- Why does this matter, and why now?
Headline: [The most memorable one-sentence claim]
Content: [The number that makes the problem real; or the striking contrast]
Says: [30-second verbal; make the investor feel why this matters]
Emotional job: Curiosity + urgency

SLIDE 2: THE PROBLEM -- Make the investor feel the pain
Headline: [The specific, surprising, or counterintuitive problem framing]
Content: [Journey map or pain stats from discovery; customer quote]
Says: [Walk through how it actually works today -- the messy reality]
Emotional job: Recognition; empathy with the customer

SLIDE 3: THE SOLUTION -- Your specific answer
Headline: [What makes this different from the obvious solution]
Content: [Screenshot or demo; 3 capabilities; key differentiator]
Says: [What you built differently; why it works with existing behaviour]
Emotional job: Relief; "this makes sense"

SLIDE 4: THE MARKET -- The size of the opportunity
Headline: [Bottom-up market size -- specific and credible]
Content: [TAM / SAM / SOM from bottom-up model; market timing reason]
Says: [The math; why now; why this market]
Emotional job: Scale calibration; serious but achievable

SLIDE 5: TRACTION -- Why should investors believe you?
Headline: [Your strongest traction claim -- specific numbers]
Content: [Paying customers; revenue; retention; usage; LOIs; growth rate]
Says: [What you have built and proved without institutional capital]
Emotional job: De-risking; this team can execute

SLIDE 6: BUSINESS MODEL -- How it makes money
Headline: [Unit economics headline -- LTV:CAC or payback or margin]
Content: [Pricing; unit economics; breakeven; 18-month ARR target]
Says: [The math that shows this is a real business, not just a product]
Emotional job: Financial conviction

SLIDE 7: THE TEAM -- Why this team
Headline: [The founding team's specific unfair advantage for this problem]
Content: [Relevant experience -- not generic CVs; why this problem, why now]
Says: [Authentic; personal; why you are the right people]
Emotional job: Trust

SLIDE 8: THE ASK -- What you need and exactly how you'll use it
Headline: [$X to go from [current state] to [18-month milestone]]
Content: [Use of funds in %; 18-month milestone; instrument + cap/rate]
Says: [This is exactly what the capital buys; when we raise again]
Emotional job: Clarity; the investor knows what they are buying

SLIDE 9: THE VISION -- Where this goes
Headline: [The big picture -- what this becomes in 5-10 years]
Content: [Product path; market expansion; comparable exit / category]
Says: [The wedge is X; the real opportunity is Y]
Emotional job: Ambition; this could be very large

## PITCH QUALITY STANDARD

EVERY CLAIM must have a source:

- Customer data: "9 of 10 CFOs in our discovery interviews..."
- Pilot results: "In our 3 pilots, adoption was 71-89%..."
- Market data: "According to [source], there are X companies..."
- Your own metrics: "$X MRR; N customers; X% month-over-month growth"

NEVER USE THESE PHRASES (red flags for experienced investors):

- "Massive market opportunity" -- give the number
- "Disruptive technology" -- explain the specific disruption mechanism
- "First mover advantage" -- explain what makes the advantage durable
- "Proprietary AI" -- what specifically is proprietary about it?
- "Conservative projections" -- all projections are optimistic; say "base case"
- "We just need 1% of the market" -- this is not a strategy; it's math
- "No direct competition" -- if there's no competition, there's no market

TRACTION HIERARCHY (most to least convincing):

1. Revenue + growth rate (paying customers; MRR; month-over-month)
2. Pilot results with specific metrics (adoption rate; retention; NPS)
3. Letters of intent with specific terms (amount; timeline)
4. Waitlist with conversion rate
5. Discovery interviews with specific insights and quotes

### Investor Research Brief Format

```
INVESTOR BRIEF -- [Name / Firm] -- Pre-Meeting
================================================================
INVESTOR PROFILE:
  Known focus: [Stage, sector, geography preferences]
  Portfolio: [Relevant portfolio companies -- especially in your sector]
  Investment thesis: [Any public statements about what they look for]

WHAT THEY CARE ABOUT (based on portfolio and public statements):
  [2-3 specific themes this investor has shown pattern interest in]

LIKELY HARD QUESTIONS:
  1. [Question they will almost certainly ask -- with recommended answer]
  2. [Question based on known portfolio pattern]
  3. [Question based on your known weaknesses]
  4. [Question based on market conditions]
  5. [The question that tests whether you know your numbers]

HOW TO APPROACH THIS MEETING:
  Opening: [What to emphasise given their known focus]
  Watch for: [Any sensitivity; portfolio conflicts; known preferences]
================================================================
```

## FINANCIAL REASONING STANDARD

For Slide 6 (Business Model) and any financial claims in the pitch:

- Unit economics first: LTV:CAC must be stated with evidence level
- Churn must be flagged if ASSUMED -- investors will ask
- Market size must use bottom-up methodology, not top-down analyst TAM
- Runway and use of funds must be specific and add up

## ASSUMPTION TRACKING

After any pitch output:

- Surface any claim in the pitch that is ASSUMED rather than validated
- Propose strengthening weak claims before the pitch meeting
- Identify the strongest and weakest slides based on evidence quality

## NEVER DO THESE

- NEVER send a pitch deck without practicing the verbal narrative out loud
  at least once -- the slide is the prompt; the verbal is the pitch
- NEVER claim traction you cannot defend with specifics in a follow-up
- NEVER show only the base-case financial scenario -- always have the
  conservative scenario ready; investors will ask
- NEVER leave the team slide generic -- it must explain WHY this team
  has an advantage for this specific problem
- NEVER use a top-down TAM ("the market is $X trillion") without a
  bottom-up sanity check; investors know the top-down number is misleading

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
