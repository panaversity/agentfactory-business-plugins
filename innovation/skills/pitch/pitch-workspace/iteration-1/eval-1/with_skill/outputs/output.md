

I'm working without your venture context file (`innov.local.md`). After we finish this deck, consider running Exercise 8 from Chapter 40 to build it — it will make every subsequent output specific to your venture rather than generic.

---

# PITCH DECK NARRATIVE — AP Invoice Matching for Mid-Market Manufacturers

**Round:** $500K Pre-Seed | SAFE | $5M Cap

---

## SLIDE 1: THE HOOK

**Headline:** Mid-market manufacturers lose $47K/year per AP manager to manual invoice matching — and they don't even know it.

**Content:** AP managers at manufacturers with $50M–$500M revenue spend 3 full working days every month — 36 days/year — manually matching invoices to POs and receiving reports. At a fully loaded cost of ~$85K/year, that's $47K in labor per AP manager burned on a task that should be automatic. Multiply by 2–4 AP staff per company, and the cost is $100K–$200K/year per manufacturer — hidden in headcount, not in a line item anyone questions.

**Says:** "Every manufacturer you know has an AP team. And every AP team has people spending a quarter of their time opening PDFs, cross-referencing PO numbers, and chasing down discrepancies by email. This isn't a new problem — it's a problem everyone has accepted as normal. We're changing that."

**Emotional job:** Curiosity + urgency — the investor should think "I've never thought about this, but the math is obvious."

---

## SLIDE 2: THE PROBLEM

**Headline:** Three-way matching is the most hated task in every AP department — and ERP vendors have ignored it for 20 years.

**Content:**
- **Discovery finding:** In 23 interviews with AP managers at mid-market manufacturers, every single one described invoice-to-PO matching as their #1 time sink. Quote: *"I have two people whose entire job is opening invoices, finding the PO, checking the receiving report, and flagging the exceptions. They hate it. I hate it. But if we get it wrong, we pay twice or we short a vendor and lose terms."* — AP Manager, $120M industrial parts manufacturer.
- The process: Invoice arrives (PDF, email, sometimes fax) → AP clerk finds PO number → cross-references line items, quantities, prices → checks receiving report → flags discrepancies → emails procurement or warehouse → waits → resolves → posts to ERP.
- Average time per invoice: 8–12 minutes for a clean match. 25–40 minutes for an exception.
- Mid-market ERPs (Epicor, Infor, SYSPRO) have basic matching modules, but they require structured data input — which means someone still has to key in the invoice data manually.

**Says:** "Let me walk you through what actually happens. An invoice arrives as a PDF attachment. Your AP clerk opens it, finds the PO number, goes into the ERP, pulls up the PO, and starts comparing line by line. Quantities, unit prices, part numbers. Then they check if the warehouse actually received what was ordered. If anything doesn't match — and something doesn't match about 30% of the time — they start a chain of emails that can take days to resolve. This is 2026, and it's still happening manually because ERPs expect clean data in, and invoices are messy documents."

**Emotional job:** Recognition and empathy — the investor should feel the tedium and understand why this hasn't been solved at this market tier.

---

## SLIDE 3: THE SOLUTION

**Headline:** We turn unstructured invoices into auto-matched, exception-flagged transactions inside your existing ERP — no data entry, no workflow change.

**Content:**
- **How it works:** Invoice arrives by email → our system extracts all line-item data (OCR + LLM parsing) → matches against open POs and receiving reports via ERP API → auto-approves clean matches → routes exceptions with specific discrepancy details to the right person.
- **Three capabilities that matter:**
  1. **Unstructured → Structured:** Handles any invoice format — PDF, image, email body — without templates or training per vendor.
  2. **Fuzzy matching logic:** Matches part numbers, descriptions, and quantities even when vendor naming conventions differ from PO data (e.g., "SS 304 Hex Bolt 3/8-16" vs. "HEX BLT 304SS .375-16").
  3. **ERP-native:** Integrates directly with Epicor, Infor, and SYSPRO via existing APIs — posts matched transactions, so AP never leaves their system.
- **Key differentiator:** We don't replace the ERP or require a new workflow. AP managers see matched invoices in the same screen they already use. The 70% of invoices that match cleanly just appear — already done. The 30% that don't match arrive with the specific discrepancy highlighted, cutting exception resolution from 30+ minutes to under 5.

**Says:** "We didn't build a new AP platform. Nobody wants another login. We built an automation layer that sits behind the ERP your customer already uses. Invoices come in, we parse them — any format, any vendor — match them against POs and receiving reports, and push clean matches straight into the ERP as completed transactions. For exceptions, we don't just flag them — we tell you exactly what's wrong: 'Line 3, PO says 500 units at $4.20, invoice says 480 units at $4.35.' That cuts exception handling time by 80%."

**Emotional job:** Relief — "this makes sense, and it doesn't require ripping out existing systems."

---

## SLIDE 4: THE MARKET

**Headline:** 12,400 mid-market manufacturers in the US spend $1.5B/year on AP staff doing work our product automates.

**Content:**
- **Bottom-up TAM:** ~38,000 US manufacturers with $50M–$500M revenue (Census Bureau, NAICS 31-33). Average 3 AP staff per company. ~$47K/year in matching labor per AP staff = **$5.4B** in addressable labor cost.
- **SAM (our ERP ecosystem):** ~12,400 manufacturers running Epicor, Infor, or SYSPRO (our current integrations) = **$1.5B** in addressable labor cost.
- **SOM (18-month target):** 80 customers × $30K ACV = **$2.4M ARR**. That's 0.6% of our SAM — a penetration rate we can achieve through ERP partner channels and direct outreach.
- **Why now:** LLM capabilities for unstructured document parsing crossed the accuracy threshold (~97% field-level accuracy) in 2024–2025. Before this, OCR-only solutions required per-vendor templates and still had 15–20% error rates — unacceptable for financial documents. The technology unlock is real and recent.

**Says:** "Let me give you the math. There are about 38,000 mid-market manufacturers in the US. We're focused on the 12,400 running the three ERPs we currently integrate with — Epicor, Infor, and SYSPRO. Each of those companies has 2–4 AP staff spending roughly a quarter of their time on manual matching. That's $1.5 billion in labor cost doing work our product automates. Our 18-month target is 80 customers at $30K ACV — $2.4 million ARR. That's less than 1% of our serviceable market. The reason this is possible now and wasn't three years ago: LLM-based document parsing hit the accuracy threshold for financial documents in the last 18 months. Before that, you needed per-vendor templates and still got 15–20% error rates. Now we're at 97%+ accuracy on first pass."

**Emotional job:** Scale calibration — the market is specific, credible, and large enough to be interesting.

---

## SLIDE 5: TRACTION

**Headline:** 8 paying customers. $16K MRR. 15% month-over-month growth. Built in [X] months with no institutional capital.

**Content:**
- **8 paying manufacturers** on annual contracts — $16K MRR / $192K ARR run-rate
- **15% MoM revenue growth** over the past [X] months
- **3% monthly churn** (1 customer lost in [time period] — [reason if known])
- **Customer profile:** Manufacturers with $60M–$250M revenue, 2–5 AP staff, running Epicor or Infor
- **Usage metrics:** Average customer processes [X] invoices/month through the platform; [X]% auto-match rate
- **Customer quote:** *"We went from 3 days of matching per month to half a day. My AP team is now spending time on vendor negotiations and early-pay discounts instead."* — Controller, $90M precision machining company
- **How we got here:** Direct outreach to AP managers via LinkedIn + referrals from first 3 customers

**Says:** "We have 8 paying manufacturers. $16K MRR, growing 15% month over month. We built this with no institutional capital — just revenue. Our churn is 3% monthly, which I'll address — it's higher than we want, and I'll tell you what we're doing about it. But the signal that matters: customers who stay are expanding usage, and 3 of our 8 customers came from referrals. AP managers talk to each other. When you save someone 3 days a month, they tell their counterpart at the company down the road."

**Emotional job:** De-risking — this team has built a product people pay for and use, without outside capital.

---

## SLIDE 6: BUSINESS MODEL

**Headline:** $2K/month ACV. 80%+ gross margin. LTV:CAC of 4.2x today — improving as churn decreases.

**Content:**
- **Pricing:** $1,500–$3,000/month based on invoice volume (tiered). Average ACV: ~$24K.
- **Gross margin:** ~82% (primary COGS: LLM API costs for document parsing + cloud infrastructure).
- **Unit economics:**
  - **CAC:** ~$5,700 (founder-led sales; blended cost of time + LinkedIn outreach tools)
  - **Monthly churn:** 3% → implied average lifetime: ~33 months
  - **LTV:** ~$24K (33 months × $2K/mo × 82% gross margin ÷ simplified)
  - **LTV:CAC:** ~4.2x
- **Path to improving unit economics:** Churn reduction (see below) extends LTV; ERP partner channel reduces CAC. Target: LTV:CAC of 8x+ by end of 2027.
- **Churn note (honest):** 3% monthly = ~31% annual. This is above target. Root cause from exit interviews: implementation friction with less common ERP configurations. We are investing the pre-seed capital partly in implementation engineering to bring this below 2% monthly within 6 months.
- **18-month ARR target:** $2.4M (80 customers at $30K blended ACV as we move upmarket slightly)

**Says:** "Our average customer pays $2,000 a month. Gross margin is north of 80% — our primary cost is LLM API calls for document parsing, which are dropping in cost every quarter. Our LTV:CAC is 4.2x today, which is solid for pre-seed but not where we want it. The main lever is churn. 3% monthly is too high. When we dig into it, the churn is concentrated in customers with non-standard ERP configurations where our integration requires more setup. Part of this raise goes directly to implementation engineering to fix that. If we get churn to 2%, LTV:CAC goes to 6x+. If we get it to 1.5% — which is our target — it's north of 8x."

**Emotional job:** Financial conviction — the math works, and the founder knows the weaknesses.

---

## SLIDE 7: THE TEAM

**Headline:** [Founder name(s)] — [X] years in manufacturing operations/AP automation/ERP integrations.

**Content:**
- [Founder 1]: [Specific relevant background — e.g., "Built the AP automation module at [company]; managed AP teams at two mid-market manufacturers; knows the ERP integration landscape from the inside"]
- [Founder 2, if applicable]: [Specific relevant background]
- **Why us for this problem:** [The specific insight or experience that gave you the unfair advantage — e.g., "I was the AP manager who spent 3 days a month matching invoices. I built the first version for my own team."]
- **Key hires planned:** Implementation engineer (reduce churn); second sales rep (ERP partner channel)

**Says:** "[Personalize this — the team slide must be authentic. Explain: why you personally care about this problem, what specific experience gives you an edge, and why you started this company rather than staying in your previous role. Investors are buying the team as much as the product at pre-seed.]"

**Emotional job:** Trust — this team understands the problem from the inside.

---

## SLIDE 8: THE ASK

**Headline:** $500K to go from $192K ARR to $2.4M ARR in 18 months.

**Content:**
- **Instrument:** SAFE, $5M cap
- **Use of funds:**
  - **40% — Sales + go-to-market ($200K):** Second sales hire; ERP partner channel development; first industry trade show presence
  - **30% — Product + engineering ($150K):** ERP integration depth (reduce implementation friction → reduce churn); add SYSPRO integration; improve auto-match rate from [X]% to [target]%
  - **20% — Implementation engineering ($100K):** Dedicated implementation support to reduce churn from 3% to <2% monthly
  - **10% — Operations + buffer ($50K):** Legal, accounting, insurance, runway buffer
- **18-month milestones:**
  - 80 customers / $2.4M ARR
  - Monthly churn < 1.5%
  - 3 ERP integrations live (Epicor, Infor, SYSPRO)
  - Position for $3M–$5M seed round at $20M–$25M cap

**Says:** "We're raising $500K on a SAFE with a $5M cap. This gets us from $192K ARR to $2.4M ARR in 18 months. 40% goes to sales — we're adding a second rep and building the ERP partner channel. 30% goes to product — deeper integrations and a higher auto-match rate. 20% goes to implementation engineering, which is our churn fix. And 10% is buffer. At $2.4M ARR with churn under 1.5%, we'll be in a strong position for a $3–5M seed round."

**Emotional job:** Clarity — the investor knows exactly what their money buys and when you raise again.

---

## SLIDE 9: THE VISION

**Headline:** Invoice matching is the wedge. The real opportunity is autonomous AP for mid-market manufacturing.

**Content:**
- **Phase 1 (now):** Automated three-way invoice matching — the most painful, highest-frequency AP task
- **Phase 2 (post-seed):** Expand to full AP workflow — vendor onboarding, payment scheduling, early-pay discount optimization, compliance documentation
- **Phase 3 (Series A+):** The autonomous AP department — from invoice receipt to payment execution, with human oversight only on exceptions and approvals above threshold
- **Comparable trajectory:** Bill.com started with SMB bill pay, expanded to full AP/AR workflow, and reached $1B+ revenue. We're taking the same playbook to mid-market manufacturing, where the complexity is higher (three-way matching vs. simple bill pay) and willingness to pay is stronger.
- **Why manufacturing stays our focus:** Highest invoice complexity (part numbers, quantities, receiving reports); highest switching costs once integrated with ERP; procurement teams value reliability over novelty — once you're in, you stay in.

**Says:** "We're starting with invoice matching because it's the sharpest pain point and the fastest sale. But matching is just the entry point. Once we're integrated with a customer's ERP and processing their invoices, we're in position to automate the entire AP workflow — vendor management, payment timing, discount capture, compliance. The long-term vision is the autonomous AP department for mid-market manufacturing. Bill.com proved this model in SMB. We're bringing it to a market that's more complex, more willing to pay, and stickier once you're embedded."

**Emotional job:** Ambition — this could be a very large company, and the wedge strategy is credible.

---

# ASSUMPTION AUDIT

| Claim in Deck | Evidence Level | Risk |
|---|---|---|
| 8 paying customers, $16K MRR | **VALIDATED** — real revenue | Low |
| 15% MoM growth | **VALIDATED** — if sustained over 3+ months | Low-Medium |
| 3% monthly churn | **VALIDATED** — but needs root cause fix | **Medium-High** |
| 3 days/month on manual matching | **VALIDATED** — 23 discovery interviews | Low |
| 12,400 manufacturers in SAM | **ASSUMED** — needs Census + ERP vendor verification | Medium |
| 80 customers in 18 months | **PROJECTED** — 10x growth from current base | Medium |
| LTV:CAC of 4.2x | **CALCULATED** — but churn assumption is load-bearing | Medium |
| 97% field-level accuracy | **ASSUMED** — needs published benchmark | Medium |
| ERP partner channel will reduce CAC | **ASSUMED** — no partner deals signed yet | **High** |

## Strongest Slides
- **Slide 5 (Traction):** Real revenue, real growth, real customers. This is your best asset at pre-seed.
- **Slide 2 (Problem):** 23 discovery interviews with specific quotes — investors will trust this.

## Weakest Slides
- **Slide 7 (Team):** Needs personalization — I've left placeholders. This slide cannot be generic.
- **Slide 6 (Business Model):** The 3% monthly churn is the elephant in the room. You addressed it honestly, which is correct — but investors will push hard on this. Have your churn cohort data ready (is churn concentrated in early cohorts? Is it improving?).

## Top 3 Things to Strengthen Before Pitching

1. **Churn cohort analysis:** Show that recent cohorts churn less than early cohorts. If they don't, that's a harder conversation.
2. **ERP partner validation:** Even one LOI or verbal from an Epicor/Infor partner rep transforms Slide 8 from "we plan to" into "we're already in motion."
3. **Fill in the Team slide** with your specific, authentic story. At pre-seed on a $5M cap, investors are underwriting the founders more than the metrics.

---

Want me to run **Hard Questions Prep** (the 15 toughest questions an investor will ask about this deck) or build the **100-word Executive Summary** for email intros?
