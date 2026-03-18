# Q3/Q4 Product Roadmap Planning

## Current Product Landscape

### What We Have Today

**AgentFactory Business Plugins** — a marketplace of domain-specific Claude Code plugins for regulated business domains.

| Plugin                        | Status | Skills | Agents | Book Chapter | Maturity                 |
| ----------------------------- | ------ | ------ | ------ | ------------ | ------------------------ |
| Islamic Finance               | v3.0.0 | 13     | 0      | Ch 31        | Shipped, stable          |
| IDFA Financial Architect      | v2.0.0 | 2      | 0      | Ch 29        | Shipped, stable          |
| Banking                       | v2.0.0 | 17     | 0      | Ch 32        | Shipped, stable          |
| Legal Ops                     | v3.0.0 | 6      | 1      | Ch 33        | Shipped, stable          |
| Sales, RevOps & Marketing     | v1.0   | 15     | 5      | Ch 34        | Shipped, stable          |
| Supply Chain & Procurement    | v1.0.0 | 8      | 5      | Ch 35        | New, content in progress |
| Product Strategy              | —      | 6      | 3      | Ch 36        | New, content in progress |
| HR Operations                 | v1.0.0 | 5      | 4      | Ch 37        | New, content in progress |
| Operations Intelligence       | —      | 4      | 4+     | Ch 38        | New, content in progress |
| Agentic Office                | —      | 10     | 4+     | Ch 39        | New, content in progress |
| Innovation & Intrapreneurship | v1.0.0 | 10     | 4      | Ch 40        | New, content in progress |

**Book (The AI Agent Factory)** — educational platform at learn.panaversity.org:

- Part 0 (Thinking is the Curriculum): Complete — 160+ files, 44 lessons, 10 quizzes
- Part 1 (General Agents Foundations): Ch 12-18
- Part 2 (Agent Workflow Primitives): Ch 19-24
- Part 3 (Business Domain Agent Workflows): Ch 25-40, content in active production for Ch 35-40
- Part 4 (Programming in the AI Era): Planned

**Platform**: learn-app (Docusaurus), SSO, content-api, progress-api, study-mode-api

---

## Strategic Context

The product sits at an intersection of three value streams:

1. **Education** — The AI Agent Factory book teaches domain experts to build sellable AI agents
2. **Plugins** — Reusable agent skills that readers build with and learn from
3. **Platform** — The infrastructure (learn-app, APIs, practice environment) that delivers the experience

The Layer 1/Layer 2 architecture (our plugins extend Anthropic's first-party plugins) means we are dependent on Anthropic's plugin ecosystem velocity. This is both an advantage (distribution) and a constraint (API surface changes).

---

## Initiative Candidates

Based on current state, open issues, and momentum, here are the candidate initiatives for Q3/Q4:

### A. Complete Part 3 Content (Ch 35-40)

**What**: Finish the 6 remaining chapters covering supply chain, product management, HR, operations, productivity/agentic office, and innovation.

**Current state**: Plugin code exists for all 6. Book content is in active production (branch `feat/part3-chapters-35-40`). Chapters 25-34 are shipped.

**Effort**: Medium-high (6 chapters × ~15 lessons each = ~90 lessons). Active team prompt / parallel agent workflows exist.

**Impact**: Completes the business domain coverage. Unlocks Part 4.

**Risk**: Content quality — each chapter requires plugin verification, exercise design, flashcards, quizzes, and summaries. The content-implementer pipeline is mature but each chapter still requires ~2-3 sessions.

**Dependencies**: Plugin repos for each chapter must be stable first.

### B. Part 4: Programming in the AI Era

**What**: Start the final part of the book — teaching programming through an AI-first lens.

**Current state**: Directory exists but no content. This is the culmination of the book — readers have domain knowledge from Parts 0-3, now they learn to code.

**Effort**: High (unknown chapter count, likely 6-10 chapters, new pedagogical approach since students have zero programming background per Part 3 assumptions).

**Impact**: Completes the book. Transforms the product from "business domain agents" to "full-stack agent factory."

**Risk**: Pedagogical — the transition from no-code (Parts 0-3) to code (Part 4) is the hardest design challenge in the book.

**Dependencies**: Part 3 should be substantially complete first.

### C. AICheck Component / Exercise Submission (Phase 2)

**What**: Redesign the exercise submission UX from the broken 7-step ExercisePrompt + SubmissionDialog into a unified inline `<AICheck>` component.

**Current state**: Phase 1 shipped (text-primary evidence, auto score extraction, 50 XP). Phase 2 vision documented. Current UX has 0.01% adoption due to friction.

**Effort**: Medium (frontend component redesign + context wiring fix).

**Impact**: High — this is the primary engagement mechanism. If students don't submit exercises, the entire learning loop breaks.

**Risk**: Low technical risk, but requires getting the UX right on first iteration.

**Dependencies**: None — can be parallelized with content work.

### D. Sidebar Toggle (Issue #830)

**What**: Add a toggle button to open/close the learn-app sidebar.

**Effort**: Low.

**Impact**: Low-medium — quality of life improvement.

**Risk**: None.

**Dependencies**: None.

### E. CI Sync Check (Issues #787, #788)

**What**: Add CI pipeline to validate TypeScript and Python field definitions stay in sync. Add Python field_definitions.py with ?enrich=true query param.

**Effort**: Low-medium.

**Impact**: Medium — prevents silent API drift between TS frontend and Python backend.

**Risk**: Low.

**Dependencies**: None.

### F. Contextual Micro-Prompts for Profile Completion (Issue #786)

**What**: Progressive profile completion through contextual micro-prompts instead of a single onboarding form.

**Effort**: Medium.

**Impact**: Medium — better user data enables better personalization in the learn skill.

**Risk**: Low.

**Dependencies**: None, but more valuable after AICheck adoption improves.

### G. Content API / Learn Skill Improvements

**What**: JWKS gap fix (add `scope: "openid"` to auth.py), auto-auth design improvements, Blended Discovery v2.0.0 refinements.

**Current state**: 73 tests passing, device flow auth working but with opaque token round-trips.

**Effort**: Low-medium per improvement.

**Impact**: Medium — performance and reliability of the AI tutoring experience.

**Risk**: Low.

**Dependencies**: SSO changes for JWKS fix.

### H. Plugin Marketplace Distribution

**What**: Improve plugin discoverability — better marketplace.json, automated release pipeline, cross-platform install guides (Copilot, Cursor, Codex).

**Effort**: Low-medium.

**Impact**: Medium-high — the plugins only have value if people find and install them.

**Risk**: Low.

**Dependencies**: Plugins must be stable (they are).

---

## Recommended Sequencing

### Q3 (July–September)

**Theme: Complete the core product.**

| Priority | Initiative                        | Rationale                                                                                                                                                               |
| -------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | **A. Complete Part 3 (Ch 35-40)** | This is in-flight. Momentum is high. Stopping mid-part would waste the pipeline investment. Target: all 6 chapters shipped by end of Q3.                                |
| P0       | **C. AICheck Component**          | Parallel track. Current 0.01% adoption means the exercise system is effectively dead. Fix this before Part 4 launches or Part 4 exercises will also be dead on arrival. |
| P1       | **D. Sidebar Toggle**             | Quick win. Ship in a single session.                                                                                                                                    |
| P1       | **E. CI Sync Check**              | Infrastructure hygiene. Prevents future breakage. Ship early Q3.                                                                                                        |
| P2       | **G. Content API improvements**   | JWKS fix is low-effort, high-reliability. Do it when touching auth code for anything else.                                                                              |

**Q3 exit criteria:**

- Part 3 complete (Ch 25-40, all content shipped)
- AICheck component live with >5% exercise completion rate
- CI sync pipeline active
- Sidebar toggle shipped

### Q4 (October–December)

**Theme: Launch Part 4 and grow distribution.**

| Priority | Initiative                               | Rationale                                                                                                                                                       |
| -------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P0       | **B. Part 4: Programming in the AI Era** | The book's climax. With Part 3 done, this is the critical path. Begin with pedagogical design (how to transition no-code → code), then implement.               |
| P1       | **H. Plugin Marketplace Distribution**   | With all domain plugins stable and book complete through Part 3, invest in discoverability. Cross-platform guides, better install UX, marketplace improvements. |
| P1       | **F. Contextual Micro-Prompts**          | With AICheck working (from Q3), profile data becomes more valuable — you can personalize exercise feedback.                                                     |
| P2       | **G. Content API continued**             | Blended Discovery refinements informed by Q3 usage data.                                                                                                        |

**Q4 exit criteria:**

- Part 4 chapters 1-4 (of estimated 6-10) shipped
- Plugin installs growing week-over-week
- Profile completion rate >30% via micro-prompts
- Learn skill using JWT (not opaque tokens) for all auth

---

## What We're NOT Doing (Explicit Cuts)

| Initiative                                  | Why Not                                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| New business domain plugins beyond Ch 35-40 | The current 11 plugins cover the book scope. New domains only after the book is complete.                     |
| Mobile app                                  | The learn-app is web-first. Mobile adds complexity without proportional reach at current scale.               |
| Video content                               | Text + AI tutoring is the pedagogical model. Video is a different product.                                    |
| Multi-language book translation             | The `/md-translator` skill exists but translation is maintenance-heavy. English-first until book is complete. |
| Practice environment expansion              | Phase 1 shipped (142 tests). Expand only if Part 4 requires it for coding exercises.                          |
| Plugin monetization / paid tiers            | Too early. Build the audience first through the free book + plugins, then monetize.                           |

---

## Key Risks and Mitigations

| Risk                                              | Likelihood | Impact                              | Mitigation                                                                                                                         |
| ------------------------------------------------- | ---------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Part 3 Ch 35-40 takes longer than Q3              | Medium     | High — blocks Part 4                | Parallel agent teams are already working. Monitor weekly. Cut scope per-chapter if needed (fewer exercises, not fewer lessons).    |
| AICheck redesign doesn't improve adoption         | Low        | High — exercise loop stays broken   | Ship MVP fast, measure within 2 weeks, iterate. The 7-step problem is well-understood.                                             |
| Part 4 pedagogical design is harder than expected | High       | High — bad transition loses readers | Invest in design conversation before implementation. Read research on code-first vs concepts-first for adult learners. Don't rush. |
| Anthropic plugin API changes                      | Low        | Medium — breaks install flows       | Pin to known-working versions. Monitor Anthropic changelog.                                                                        |
| Content quality regression at scale               | Medium     | Medium — 90 new lessons is a lot    | Use content-implementer subagent consistently. Run editorial-reviewer on each chapter before merge.                                |

---

## Decision Points Needed

1. **Part 4 chapter count and scope** — How many chapters? What languages/frameworks? This needs a design conversation before Q4 begins.
2. **AICheck component ownership** — Who builds this? It's frontend-heavy (React + Framer Motion). Can it be parallelized with content work?
3. **Plugin distribution strategy** — Organic (book readers install) vs. outbound (marketplace promotion, blog posts, community)? This affects Q4 effort.
4. **Measurement** — What metrics define success for Q3/Q4? Suggestion: lessons published, exercise completion rate, plugin installs, learn-app DAU.

---

## Summary

**Q3 = Complete + Fix** (finish Part 3, fix exercise UX, ship quick wins)
**Q4 = Launch + Grow** (start Part 4, improve distribution, personalize)

The single most important thing is completing Part 3 and fixing AICheck. Everything else is secondary. If Q3 goes well, Q4 is about the exciting transition to Part 4 and growing the user base.
