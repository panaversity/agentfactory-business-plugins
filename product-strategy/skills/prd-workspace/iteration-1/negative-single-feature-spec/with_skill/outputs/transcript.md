# Transcript: negative-single-feature-spec (with_skill)

## Task Given

"Write a spec for adding a dark mode toggle to our settings page. It's one feature for the frontend team, should take about a sprint."

## What I Did

1. **Read the skill file** (`/prd/SKILL.md`) — 227 lines covering PRD workflow, template sections, status gates, and routing logic.

2. **Evaluated the routing logic** — The skill contains explicit triage criteria (lines 30-34):
   - SPEC when: one feature, one team, 1-3 sprints
   - PRD when: multiple features, multiple teams, major platform change, new product area, or executive alignment
   - The skill metadata (line 9) also lists `single-feature specifications` under "NOT for."

3. **Matched the task against criteria** — The request is: one feature (dark mode toggle), one team (frontend), one sprint. This matches the SPEC path exactly and is explicitly excluded from the PRD path.

4. **Declined the task** — Following the skill's own instructions, I did NOT generate a PRD. Instead, I documented why the skill declined and recommended `/write-spec` as the correct tool.

5. **Wrote response.md** — Explains the decline decision, quotes the routing logic, and analyzes what would happen if the PRD template were forced onto this single-feature task (most sections would be empty or over-engineered).

## Key Observation

The skill is well-designed for this negative case. It has clear routing logic that prevents scope mismatch — using a 10-section cross-functional PRD for a one-team, one-sprint toggle would create unnecessary overhead. The skill correctly redirects to `/write-spec` for this type of work.

## Time Spent

~2 minutes. Read skill → evaluated routing → wrote decline response.
