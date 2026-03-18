TASK:          Knowledge Capture Plan -- David Park
DOCUMENT TYPE: Knowledge Capture Plan
JURISDICTION:  Not specified (best practices applied)
CONFIGURATION: best practices (no hr.local.md loaded)
SENSITIVITY:   CONFIDENTIAL

KNOWLEDGE CAPTURE PLAN: David Park
================================================================
Role: Lead Infrastructure Engineer | Tenure: 8 years | Risk: HIGH

RISK SCORING:
  Tenure:             3 (5+ years — 8 years)
  Role criticality:   3 (Sole expert — only person who understands these systems)
  Documentation level: 3 (Assumed undocumented — no successor, no shared access)
  Successor readiness: 3 (None identified)
  Client/revenue impact: 3 (Direct and significant — deployment pipeline,
                            AWS architecture, hosting vendor relationship
                            all directly impact uptime and operations)
  TOTAL SCORE: 15 / 15 — MAXIMUM HIGH RISK

CAPTURE TYPE: REACTIVE (departure confirmed, 4-week notice, last day March 28)

URGENCY ASSESSMENT:
  Working days remaining: ~7 (March 19 to March 28, excluding weekends)
  Competing demands: David must still perform his day role
  Realistic capture time: 12-16 hours across sessions
  This is a CRITICAL timeline — every day without capture is permanent
  knowledge loss risk.

================================================================
KEY KNOWLEDGE AREAS (ranked by risk):
================================================================

  1. DEPLOYMENT PIPELINE (CRITICAL)
     What makes it unique: David is the sole person who understands how
     code moves from commit to production. If this breaks after March 28,
     no one can diagnose or repair it. This is the highest-risk area
     because it blocks ALL engineering work if it fails.
     Includes: CI/CD configuration, build steps, environment promotion
     logic, rollback procedures, secret management, deployment triggers,
     known failure modes and their fixes.

  2. AWS ARCHITECTURE (CRITICAL)
     What makes it unique: David is the only person with deep understanding
     of how AWS services are configured, why architectural decisions were
     made, cost structure, scaling behaviour, and disaster recovery
     posture. No one else has equivalent access or understanding.
     Includes: VPC topology, IAM roles and policies, service
     interdependencies, auto-scaling rules, monitoring and alerting
     configuration, backup and DR procedures, cost optimisation decisions,
     security group logic, account structure.

  3. HOSTING VENDOR RELATIONSHIP (HIGH)
     What makes it unique: David manages the relationship with the hosting
     provider. Contract terms, escalation paths, SLA enforcement,
     commercial leverage, and the history of what has gone wrong are all
     in his head. Losing this means the next person starts from zero in
     a commercial relationship the vendor knows far better than we do.
     Includes: Contract terms and renewal dates, vendor contacts and
     escalation matrix, SLA thresholds and enforcement history, pricing
     structure and negotiation history, known vendor limitations and
     workarounds, support ticket processes.

  4. SYSTEM ACCESS AND CREDENTIALS (CRITICAL — IMMEDIATE ACTION)
     What makes it unique: David holds access to systems no one else can
     reach. Before ANY knowledge capture, we need to ensure access
     continuity. This is not a knowledge capture session — this is a
     day-one emergency action.
     Includes: AWS root/admin account access, CI/CD platform admin access,
     hosting provider portal credentials, monitoring/alerting platform
     access, DNS management access, SSL certificate management, any
     personal SSH keys or API tokens used in production.

  5. INSTITUTIONAL CONTEXT AND "WHAT NOT TO DO" (HIGH)
     What makes it unique: 8 years of accumulated organisational wisdom —
     why things are built the way they are, what was tried and failed,
     which decisions were forced by constraints that may no longer exist,
     and what David would change if starting fresh. This is the knowledge
     most likely to be permanently lost and most likely to cause the
     organisation to repeat expensive mistakes.

================================================================
IMMEDIATE ACTIONS (March 19-20 — before any capture sessions):
================================================================

  ACTION 1: ACCESS AUDIT AND TRANSFER (March 19 — TODAY)
  Owner: IT Security / David's manager
  - Inventory every system David has admin/sole access to
  - Create secondary admin accounts for at least TWO other people
  - Document all credentials in a secure vault (not email, not Slack)
  - Verify the secondary accounts work by having the new holders log in
  - Do NOT wait — if David is hit by a bus tomorrow, these systems
    are inaccessible

  ACTION 2: IDENTIFY CAPTURE SESSION PARTICIPANTS (March 19)
  Owner: David's manager
  - Who will absorb each knowledge area? Assign specific people:
    * Deployment pipeline → [Name TBD — most senior backend engineer]
    * AWS architecture → [Name TBD — engineer with some AWS experience]
    * Vendor relationship → [Name TBD — engineering manager or VP Eng]
  - These people MUST attend the relevant capture sessions
  - They are not just scribes — they will be the new knowledge holders

  ACTION 3: BLOCK DAVID'S CALENDAR (March 19)
  Owner: David's manager
  - Remove David from all non-essential meetings for remaining tenure
  - Block 2-hour capture sessions on the schedule below
  - David's ONLY priorities for the next 7 working days:
    1. Knowledge capture sessions
    2. Keeping systems running
    3. Nothing else

================================================================
CAPTURE SESSIONS:
================================================================

  SESSION 1: Deployment Pipeline Deep Dive
  Date:     March 20 (Thursday)
  Duration: 2.5 hours
  Method:   Pair working + Interview (David walks through the pipeline
            live with the designated successor, explaining each step)
  Attendees: David + pipeline successor + scribe
  Outputs:
    - Knowledge Article: "Deployment Pipeline — How It Actually Works"
    - Knowledge Article: "Deployment Pipeline — Failure Modes and Recovery"
    - Screen recording of David performing a deployment end-to-end
    - Architecture diagram (drawn or validated by David during session)

  SESSION 2: AWS Architecture and Operations
  Date:     March 21 (Friday)
  Duration: 3 hours
  Method:   Pair working + Interview (David walks through the AWS console,
            explaining the architecture, then answers interview questions)
  Attendees: David + AWS successor + scribe
  Outputs:
    - Knowledge Article: "AWS Architecture — Service Map and Rationale"
    - Knowledge Article: "AWS Operations — Monitoring, Scaling, and DR"
    - Knowledge Article: "AWS Cost Structure — What We Pay and Why"
    - Annotated architecture diagram (David draws/validates)
    - Screen recording of David navigating key AWS configurations

  SESSION 3: Vendor Relationship and Commercial Context
  Date:     March 24 (Monday)
  Duration: 1.5 hours
  Method:   Interview-based (structured around vendor knowledge questions)
  Attendees: David + vendor relationship successor + scribe
  Outputs:
    - Knowledge Article: "Hosting Vendor — Relationship Map and History"
    - Knowledge Article: "Hosting Vendor — Contract Terms and Escalation"
    - Contact list with notes on each vendor contact's role and temperament
    - Introduction email/call between David and vendor, with successor CC'd

  SESSION 4: Institutional Context and Organisational Wisdom
  Date:     March 25 (Tuesday)
  Duration: 2 hours
  Method:   Interview-based (structured around organisational knowledge
            questions — this is where the "what not to do" knowledge lives)
  Attendees: David + engineering manager + scribe
  Outputs:
    - Knowledge Article: "Infrastructure Decisions — Why Things Are Built
      This Way"
    - Knowledge Article: "Lessons Learned — What We Tried That Failed"
    - Knowledge Article: "If I Were Starting Fresh — David's Recommendations"

  SESSION 5: Validation and Gap-Filling
  Date:     March 27 (Thursday)
  Duration: 2 hours
  Method:   Review + Interview (successors review DRAFT articles, ask
            follow-up questions, David validates or corrects)
  Attendees: David + all successors + scribe
  Outputs:
    - Corrected and validated knowledge articles (move from DRAFT to
      REVIEWED status)
    - Gap list: anything still unclear after 4 sessions
    - David's contact information for post-departure questions (if willing)

  TOTAL: 5 sessions × ~2 hours avg = ~11 hours of David's time

================================================================
KNOWLEDGE INTERVIEW GUIDE:
================================================================

OPENING (use at the start of every session):
"David, the goal of this session is to make sure the knowledge and
insights you've built up over 8 years here don't disappear when you
leave. There are no wrong answers — we want what's in your head,
not what's in the documents."

--- DEPLOYMENT PIPELINE QUESTIONS (Session 1) ---

PROCESS / METHODOLOGY:
- "Walk me through what actually happens when code gets deployed.
  Start from the commit and end at production."
- "Our documentation says [X]. Where does reality differ?"
- "What are the early warning signs that a deployment is going wrong?
  The signals you've learned to watch for?"
- "What's the rollback procedure? Not the documented one — the one
  that actually works under pressure."
- "What breaks most often? What's the fix each time?"
- "If I followed our documented deployment process exactly, what
  would I get wrong?"
- "Are there any manual steps that should be automated but aren't?
  Why haven't they been automated?"
- "What secrets, tokens, or credentials does the pipeline depend on?
  Where are they stored? When do they expire?"

--- AWS ARCHITECTURE QUESTIONS (Session 2) ---

PROCESS / METHODOLOGY:
- "Draw me the architecture. Start with the request path from the
  user to the database and back."
- "Why is it built this way? What constraints forced these decisions?"
- "What would you change if you were redesigning it today?"
- "What are the scaling limits? At what traffic level does something
  break first?"
- "Walk me through disaster recovery. If us-east-1 goes down at 2am
  on a Saturday, what happens? What do you do?"
- "What are the cost drivers? What's expensive and why?"
- "What monitoring exists? What's NOT monitored that should be?"
- "Are there any resources running that we don't need anymore but
  nobody has turned off?"

ORGANISATIONAL CONTEXT:
- "Who else in the org has any AWS knowledge? Even partial?"
- "What AWS support tier are we on? Have you ever used it?"
- "Are there any compliance or security configurations that must not
  be changed? Why?"

--- VENDOR RELATIONSHIP QUESTIONS (Session 3) ---

CLIENT / STAKEHOLDER:
- "Tell me about our hosting vendor. Who are the real decision-makers
  — not just the named contacts but the people whose opinion counts?"
- "What has gone wrong in this relationship and how was it recovered?
  What would you do differently?"
- "What are the unwritten rules? Things not in any contract but that
  the next person needs to know?"
- "What does the vendor actually care about most? Not what the
  contract says — what makes them feel the relationship is working?"
- "When is the contract up for renewal? What leverage do we have?
  What leverage do they have?"
- "What's their escalation path when something is broken at 2am?"
- "Are there any ongoing disputes, credits, or unresolved issues?"

--- INSTITUTIONAL CONTEXT QUESTIONS (Session 4) ---

ORGANISATIONAL:
- "What would you tell someone starting your role tomorrow that is
  not in any document?"
- "What has this organisation tried that didn't work, and why?
  What should we not try again?"
- "Who are the internal stakeholders you manage carefully? What do
  I need to know about each of them?"
- "What are you most worried we'll get wrong after you leave?"
- "If you were staying, what would you do in the next 12 months
  that we haven't done yet?"
- "What technical debt keeps you up at night?"
- "Are there any ticking time bombs — things that will break or
  expire in the next 6-12 months that only you know about?"
- "Is there anyone outside the company (consultants, former
  employees, vendor contacts) who holds knowledge we might need?"

CLOSING (use at the end of every session):
"Is there anything we haven't talked about that you think is
important for the next person to know?"

================================================================
KNOWLEDGE ARTICLE OUTPUTS:
================================================================

All articles use this structure and are marked DRAFT until a
successor validates them in Session 5:

  KNOWLEDGE ARTICLE: [Title]
  ================================================================
  Author:    David Park | Captured by: [Session scribe]
  Date:      [Session date] | Reviewed by: [Successor] | Status: DRAFT
  Category:  [Process / Technical / Client / Organisational]
  Audience:  [Successor / Engineering team / Leadership]

  THE KNOWLEDGE
  [What to know — the substance, in plain language]

  WHEN IT APPLIES
  [Context: when does this knowledge become relevant?]

  EXCEPTIONS AND EDGE CASES
  [When does the standard approach NOT apply?]

  RELATED CONTACTS
  [Who else holds related knowledge?]

  RELATED DOCUMENTS
  [What documentation exists that this supplements?]

  CONFIDENCE LEVEL
  [HIGH / MEDIUM / LOW with verification instructions]
  ================================================================

PLANNED ARTICLES (10 total):
  1. "Deployment Pipeline — How It Actually Works"         — Due: March 21
  2. "Deployment Pipeline — Failure Modes and Recovery"     — Due: March 21
  3. "AWS Architecture — Service Map and Rationale"         — Due: March 24
  4. "AWS Operations — Monitoring, Scaling, and DR"         — Due: March 24
  5. "AWS Cost Structure — What We Pay and Why"             — Due: March 24
  6. "Hosting Vendor — Relationship Map and History"        — Due: March 25
  7. "Hosting Vendor — Contract Terms and Escalation"       — Due: March 25
  8. "Infrastructure Decisions — Why Things Are Built       — Due: March 26
     This Way"
  9. "Lessons Learned — What We Tried That Failed"          — Due: March 26
  10. "If I Were Starting Fresh — David's Recommendations"  — Due: March 26

================================================================
ESCALATION RECOMMENDATIONS:
================================================================

  1. ESCALATE TO LEADERSHIP IMMEDIATELY (March 19):
     David is a 15/15 risk score — the maximum possible. Leadership
     must be aware that:
     - There is NO successor for any of his three critical areas
     - If knowledge capture fails or is incomplete, the organisation
       faces significant operational risk
     - Hiring a replacement or contractor with AWS/pipeline expertise
       should begin NOW, not after March 28

  2. CONSIDER RETENTION OR EXTENSION:
     - Can David's notice period be extended to 6-8 weeks?
     - Can David be retained as a part-time consultant for 3 months
       post-departure? Even 4 hours/week would dramatically reduce risk
     - Can David be offered a retention bonus to stay longer?
     - These options should be explored TODAY — every day reduces leverage

  3. CONSIDER EXTERNAL SUPPORT:
     - Engage an AWS-certified consultant to review the architecture
       BEFORE David leaves (while David can validate their findings)
     - Engage a DevOps contractor to shadow David on the pipeline
     - This is insurance, not replacement — the consultant can fill
       gaps that capture sessions miss

  4. POST-DEPARTURE SUPPORT AGREEMENT:
     - Ask David if he's willing to be available for questions after
       March 28 (paid, time-limited — e.g., 2 hours/week for 4 weeks)
     - Document this agreement in writing
     - This is your safety net for knowledge gaps discovered after departure

================================================================
TIMELINE SUMMARY:
================================================================

  March 19 (TODAY):
    □ ACCESS AUDIT AND TRANSFER — emergency action
    □ Identify capture session participants
    □ Block David's calendar for all sessions
    □ Escalate to leadership (15/15 risk score)
    □ Begin retention/extension conversation

  March 20 (Thu):
    □ Session 1: Deployment Pipeline (2.5 hours)

  March 21 (Fri):
    □ Articles 1-2 drafted from Session 1 notes
    □ Session 2: AWS Architecture (3 hours)

  March 24 (Mon):
    □ Articles 3-5 drafted from Session 2 notes
    □ Session 3: Vendor Relationship (1.5 hours)

  March 25 (Tue):
    □ Articles 6-7 drafted from Session 3 notes
    □ Session 4: Institutional Context (2 hours)
    □ Vendor introduction call (David + successor + vendor)

  March 26 (Wed):
    □ Articles 8-10 drafted from Session 4 notes
    □ All DRAFT articles sent to David for pre-review

  March 27 (Thu):
    □ Session 5: Validation and Gap-Filling (2 hours)
    □ Articles updated to REVIEWED status
    □ Gap list documented

  March 28 (Fri — LAST DAY):
    □ Final Q&A window (keep 1 hour open)
    □ Confirm post-departure contact agreement
    □ Secure handover of any remaining credentials/access
    □ David's accounts transitioned (not deleted — preserved
      for audit trail per retention policy)

================================================================
CROSS-REFERENCE NOTE:
================================================================

This plan is based on David's account of his knowledge areas as
provided by his manager. Per knowledge capture best practice:
- Do NOT treat David's account as the complete truth
- Cross-reference with: existing documentation, other engineers
  who may hold partial knowledge, system access logs (who else
  has logged into these systems?), vendor records
- The "nobody else knows this" assessment should be verified —
  "I thought someone else knew" is the most common and expensive
  mistake in knowledge capture

================================================================

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE
IN BUSINESS DECISIONS.
