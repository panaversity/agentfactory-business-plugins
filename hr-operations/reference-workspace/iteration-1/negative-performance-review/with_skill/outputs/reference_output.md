# /reference — Task Routing Response

## This task is outside the scope of the /reference skill.

The `/reference` skill handles **reference letters**, **employment references**, and **employment verification**. It does not handle performance reviews.

Your request — writing a year-end performance review with structured feedback and objectives — should be handled by the **`/performance-review`** skill instead.

---

### Why /reference cannot help here

| What you asked for | What /reference does |
|---|---|
| Year-end performance review | Reference letters for external parties |
| Structured feedback for a direct report | Factual or professional references for prospective employers, landlords, or mortgage providers |
| Setting objectives for next year | Employment verification letters |

These are fundamentally different HR documents:

- A **performance review** is an internal document between a manager and employee, focused on evaluating past performance and setting future goals.
- A **reference letter** is an external document provided to a third party, confirming employment facts or providing a professional recommendation.

---

### Recommended next step

Use **`/performance-review`** which is designed for:

- Structuring year-end feedback (achievements, areas for development, overall rating)
- Writing balanced performance narratives
- Setting SMART objectives for the next review period
- Handling sensitive performance conversations (including underperformance)
- Ensuring compliance with your organisation's review cycle and rating framework

---

**SKILL BOUNDARY:** The /reference skill explicitly excludes performance reviews from its scope. Generating a performance review under /reference would bypass the specialised guardrails, templates, and compliance checks built into /performance-review. Routing to the correct skill ensures you get the right structure, legal considerations, and best-practice guidance for this task.
