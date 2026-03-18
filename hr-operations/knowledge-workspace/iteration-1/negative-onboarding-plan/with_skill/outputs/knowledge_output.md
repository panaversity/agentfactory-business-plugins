# Knowledge Skill Response: Onboarding Plan Request

## SKILL MISMATCH DETECTED

**Requested task:** Create a 30-60-90 day onboarding plan for a new starter joining the data team next Monday.

**Activated skill:** `/knowledge` (Knowledge Capture & Transfer)

**Assessment:** This task does NOT fall within the scope of the `/knowledge` skill.

The `/knowledge` skill is designed for:
- Capturing and structuring institutional knowledge before it is lost
- Knowledge transfer from departing employees
- Knowledge risk assessment and interview-based extraction
- Creating knowledge articles from tacit/undocumented knowledge

The `/knowledge` skill explicitly excludes:
> "NOT for: policy lookup or FAQ queries (use policy-lookup), **onboarding plans (use onboarding)**, offboarding checklists (use offboard)."

## RECOMMENDED ROUTING

This request should be routed to the **`/onboarding`** skill, which is purpose-built for:
- Structuring new starter onboarding programmes
- 30-60-90 day plan generation
- Role-specific induction milestones
- First-week logistics and team integration

## WHAT THE KNOWLEDGE SKILL COULD CONTRIBUTE (Adjacent Value)

While `/knowledge` should not generate the onboarding plan itself, it could play a supporting role in onboarding preparation:

1. **Pre-onboarding knowledge capture** — If the new starter is replacing a departing team member, `/knowledge` should be invoked first to capture what the predecessor knew before they leave.

2. **Knowledge article inventory** — `/knowledge` can audit existing knowledge articles relevant to the data team role, identifying gaps that should be filled before the new starter arrives.

3. **Knowledge map for the role** — `/knowledge` can produce a knowledge map showing what tacit knowledge exists within the data team, helping identify who the new starter should shadow or pair with during onboarding.

These are supplementary actions. The primary onboarding plan should come from `/onboarding`.

## NO OUTPUT GENERATED

Because this task falls outside the skill's defined scope, no Knowledge Capture Plan has been generated. Generating an onboarding plan using the knowledge capture template would produce a poorly structured output that:

- Frames the new starter as a "knowledge holder" (they hold no institutional knowledge yet)
- Applies risk scoring designed for knowledge loss, not knowledge acquisition
- Uses interview guides designed for extracting existing knowledge, not building new knowledge
- Misses critical onboarding elements: IT setup, compliance training, team introductions, role expectations, probation milestones

## RECOMMENDATION

Route this request to `/onboarding` with the following context:
- **Role:** Data team member (specific title TBC)
- **Start date:** Next Monday (2026-03-23)
- **Plan scope:** 30-60-90 days
- **Team:** Data team
- **Additional context needed:** reporting line, tech stack, team size, any predecessor knowledge articles available

---

*This response demonstrates correct skill boundary enforcement. The `/knowledge` skill declined a task outside its scope and recommended the appropriate skill.*
