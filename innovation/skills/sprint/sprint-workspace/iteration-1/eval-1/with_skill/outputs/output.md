No `innov.local.md` found — I'll work from the context you've provided.

---

```
INNOVATION SPRINT PLAN -- Sprint 1
Dates: 2026-03-23 - 2026-04-03 | Team: 3 people | Velocity: 15 points
================================================================

SPRINT GOAL:
  Learning goal: Validate A-003 -- "AP Managers will adopt the tool
                 without IT department involvement (self-serve onboarding)"
                 Success signal: ≥3 out of 5 recruited AP Managers complete
                 onboarding independently (no IT assist) within 30 minutes.
  Delivery goal: Build and deploy a self-serve onboarding flow that an
                 AP Manager can use end-to-end without technical support.

SPRINT BACKLOG:

  US-001: Self-serve account creation [3 points] [Person A]
  As an AP Manager, I want to create an account using only my work email
  so that I can start using the tool without submitting an IT ticket.
  Acceptance criteria:
    - Account creation completes with only: name, work email, password
    - Email verification link arrives within 60 seconds
    - No SSO, admin provisioning, or IT approval step required
    - Error states (duplicate email, weak password) show actionable messages
  Tests assumption: A-003

  US-002: Guided workspace setup [3 points] [Person B]
  As an AP Manager, I want a step-by-step setup wizard that configures
  my workspace so that I can reach a usable state without reading docs
  or calling support.
  Acceptance criteria:
    - Wizard has ≤5 steps (company name, approval workflow, currency, done)
    - Each step has inline help text — no external links required
    - "Skip" is available on optional steps; mandatory steps are marked
    - Wizard completion lands on a populated dashboard (not a blank state)
  Tests assumption: A-003

  US-003: Sample data seeding [2 points] [Person B]
  As an AP Manager, I want the tool pre-loaded with sample invoices and
  approval workflows so that I can understand the product's value before
  entering my own data.
  Acceptance criteria:
    - 3 sample invoices appear on dashboard after wizard completion
    - 1 sample approval workflow is pre-configured and visible
    - Sample data is clearly labelled "[Sample]" and deletable in one click
  Tests assumption: A-003

  US-004: Onboarding progress tracker & help beacon [2 points] [Person A]
  As an AP Manager, I want to see what setup steps remain and access
  contextual help so that I can self-resolve blockers without contacting IT.
  Acceptance criteria:
    - Checklist widget shows completed/remaining onboarding steps
    - Help beacon offers searchable FAQ (≥10 entries covering common blockers)
    - "Contact support" option exists but is tracked — every use is a
      signal that self-serve failed at that step
  Tests assumption: A-003

  US-005: Onboarding analytics & drop-off instrumentation [2 points] [Person C]
  As the product team, I want to see where pilot users drop off or
  request help so that I can measure whether self-serve onboarding
  actually works.
  Acceptance criteria:
    - Funnel tracks: landing → signup → email verified → wizard started
      → wizard completed → first real action
    - Each "Contact support" click logs the step the user was on
    - Dashboard shows per-user time-to-complete and drop-off step
  Tests assumption: A-003

  US-006: Recruit & run 5 AP Manager pilot onboardings [3 points] [Person C]
  As the product team, I want 5 real AP Managers to attempt self-serve
  onboarding in week 2 so that we get direct evidence on A-003.
  Acceptance criteria:
    - 5 AP Managers recruited (not from existing customers; no prior exposure)
    - Each attempts onboarding with zero assistance — observer watches silently
    - Post-session: 3-question debrief (difficulty rating 1-5, where stuck,
      would they have called IT?)
    - Raw data captured: completion Y/N, time, drop-off step, debrief answers
  Tests assumption: A-003

DEFINITION OF DONE:
  Code:     Deployed to staging by end of Day 5; deployed to pilot
            environment by Day 7
  Learning: 5 pilot onboardings completed and data collected by Day 10
  Docs:     Sprint learning, assumption status update, and funnel data
            documented (ready for innov.local.md update)

MID-SPRINT CHECK (Day 5):
  Review:   Are US-001 through US-005 code-complete and on staging?
            US-006 recruitment — are 5 AP Managers confirmed and scheduled?
  Measure:  Internal team dogfood: can each team member complete onboarding
            in <15 min without help? If not, the pilot will fail.
  Risk:     If recruitment is behind, cut to 3 participants (minimum viable
            signal). If wizard (US-002) is behind, descope US-003 sample
            data — it's the lowest priority-score item.

SPRINT REVIEW FORMAT:
  Demo:     Live walkthrough of the full onboarding flow — show to
            team + any stakeholders
  Measure:  Pilot results:
            - X/5 completed independently
            - Median time-to-complete
            - Drop-off points (funnel data)
            - Debrief: average difficulty rating, common blockers
  Learning: Did ≥3/5 complete without IT involvement?
            YES → A-003 moves to VALIDATED (with caveats noted)
            NO  → A-003 moves to INVALIDATED — identify the specific
                  barriers (technical? trust? permissions?)
  Input:    What did pilot AP Managers say they expected but didn't find?

SPRINT RETROSPECTIVE FORMAT:
  What worked? (1 item per person — specific)
  What did not work? (1 item per person — specific)
  Assumption updates:
    A-003: [VALIDATED / INVALIDATED / PARTIALLY VALIDATED]
           Evidence: [X/5 completed; median time Ymin; blockers: ...]
           If partially validated: what conditions must hold for
           self-serve to work? (e.g., "works for managers with
           cloud tool experience, fails for those in paper-first orgs")
  One experiment for next sprint based on learning:
    If validated:   Test A-003 at scale — can 20 managers onboard in a week?
    If invalidated: Test a "light-touch IT" variant — minimal IT step
                    (e.g., domain allowlisting) instead of full self-serve
  Next sprint priority: [Determined by which assumption is now highest-risk]
================================================================
```

**Backlog prioritisation rationale:**

| Story  | Assumption Risk | Delivery Value | Score | Rationale |
|--------|:-:|:-:|:-:|---|
| US-001 | 3 | 3 | **9** | No signup = no test of A-003 at all |
| US-002 | 3 | 3 | **9** | Wizard is the core self-serve experience |
| US-006 | 3 | 3 | **9** | Without the pilot sessions, nothing is validated |
| US-004 | 3 | 2 | **6** | Self-resolution is key to "no IT involvement" |
| US-005 | 2 | 3 | **6** | Without instrumentation we can't measure drop-off |
| US-003 | 2 | 2 | **4** | Helps comprehension but not critical to the test |

If velocity is at risk, **US-003 is the first to cut** (lowest score). US-006 is non-negotiable — the sprint fails without real AP Manager data.

---

I'm working without your venture context. Run Exercise 8 from Chapter 40 to build `innov.local.md` — it will make every subsequent sprint plan specific to your venture rather than generic.
