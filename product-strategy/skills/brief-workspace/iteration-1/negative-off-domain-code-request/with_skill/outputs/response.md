TASK:          Off-Domain Request — Code Generation
FEATURE/AREA:  N/A
CONFIGURATION: Not applicable
AUDIENCE:      Requestor
VERSION:       Final

---

## Request Declined — Outside Skill Scope

The `/brief` skill handles **product briefs, discovery briefs, problem briefs,
and initiative framing** for PM workflows. It does not generate code, scripts,
or technical implementations.

**Your request** — "Write a Python script that loads a CSV and generates a bar
chart of monthly revenue" — is a code-generation task, not a product strategy
task.

### Recommended Next Steps

1. **For the Python script**: Ask Claude directly (without invoking `/brief`)
   — it can write the script immediately.
2. **If this is part of a product initiative**: Frame it as a brief first —
   e.g., `/brief problem brief for revenue visibility dashboard` — and the
   script becomes a discovery artifact, not a brief output.

### Why This Matters

Skills have defined boundaries so they produce high-quality, domain-appropriate
output. Forcing a code task through a brief template would produce neither a
good brief nor a good script.
