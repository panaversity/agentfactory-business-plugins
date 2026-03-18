# Knowledge Skill — Policy Lookup Request (Negative Case)

## Query

> What's our company's maternity leave policy? I need to know how many weeks are covered and whether it's full pay or statutory.

## Skill Response

**This query falls outside the scope of the /knowledge skill.**

The `/knowledge` skill is designed for **institutional knowledge capture** — preserving tacit, undocumented knowledge held by individuals (typically departing employees) before it is lost. It covers knowledge risk assessment, capture session planning, knowledge interviews, and knowledge article creation.

Your question is a **policy lookup** — a request for a specific, documented company policy (maternity leave entitlement and pay structure). The skill's own description explicitly states:

> *NOT for: policy lookup or FAQ queries (use policy-lookup)*

### Why /knowledge cannot answer this

1. **No policy data source**: The /knowledge skill does not contain or reference company policy documents, employee handbooks, or benefits schedules.
2. **Wrong task type**: Policy lookups require retrieving documented facts. Knowledge capture is about extracting undocumented expertise from people's heads.
3. **No hr.local.md found**: No `hr.local.md` configuration file exists in this plugin, so there is no local HR policy reference to consult.

### What you should do instead

- **Use the `/policy-lookup` skill** (if available) — this is the skill the /knowledge description explicitly recommends for policy and FAQ queries.
- **Consult your company's employee handbook or HR portal** — maternity leave policies are typically documented in benefits/leave policy sections.
- **Contact your HR team directly** — for specific entitlements (weeks covered, full pay vs. statutory), HR can provide the authoritative answer for your jurisdiction and contract type.

### Summary

| Aspect | Detail |
|--------|--------|
| **Query type** | Policy lookup (leave entitlement) |
| **Skill designed for** | Institutional knowledge capture |
| **Can skill answer this?** | No |
| **Correct routing** | /policy-lookup or HR department |
| **Reason for refusal** | Out of scope — skill explicitly excludes policy lookups |
