# Story Generation: Data Export

## INPUT RECEIVED

> As a user, I want to export my data so that I can use it in other tools.

## QUALITY CHECK: FAILED

The input story fails the skill's quality test on all three parts:

| Part | Input | Problem | Severity |
|------|-------|---------|----------|
| **PERSONA** | "a user" | Not a named persona. "A user" is generic and tells engineering nothing about who needs this, what permissions they have, or what "my data" means to them. | **Blocker** |
| **WANT** | "export my data" | Ambiguous capability. What data? What format? What volume? "Export" could mean CSV download, API bulk fetch, streaming pipeline, or clipboard copy. | **Needs refinement** |
| **OUTCOME** | "so that I can use it in other tools" | Vague outcome. Which tools? What workflow does this enable? Without knowing the destination, engineering cannot make format or integration decisions. | **Needs refinement** |

## WHY THIS CANNOT BE WRITTEN AS-IS

The skill prohibits writing stories with "a user" as the persona (see NEVER rules). Without a `product.local.md` or equivalent context, there is no persona list to draw from.

Additionally, "export my data" is almost certainly an **epic**, not a single story -- different personas export different data for different reasons, and each combination is a distinct user flow.

## WHAT THE PM NEEDS TO PROVIDE

Before stories can be generated, the PM must supply:

1. **Product name and context** (or configure `product.local.md`)
2. **Named personas** who need data export -- examples:
   - "Enterprise IT admin" (bulk export for compliance/audit)
   - "Individual contributor" (personal data portability)
   - "Integration engineer" (programmatic access for pipeline)
   - "Account owner" (GDPR/data subject access request)
3. **What data each persona needs to export** -- e.g., reports, raw records, configurations, activity history
4. **What "other tools" means** -- Excel? BI dashboards? CRM? Data warehouse? Another SaaS product?
5. **Volume and frequency** -- one-time download vs. recurring sync vs. real-time stream

## EXAMPLE: WHAT GOOD LOOKS LIKE

If the PM came back and said: "We have an Analytics Manager persona who needs to export dashboard report data as CSV so they can build custom visualizations in Tableau," the story would be:

```
USER STORIES: Data Export
================================================================
Epic: Data Export -- Enable personas to extract their data in
      portable formats for use in external tools and workflows.
Stories: 3 (example set) | Sprints: 1-2 | Persona(s): Analytics Manager

-- ANALYTICS MANAGER STORIES ------------------------------------

Story 1: Export dashboard report as CSV
  As an Analytics Manager,
  I want to export any dashboard report as a CSV file,
  So that I can build custom visualizations in Tableau
  without manually re-entering data.

  Acceptance Criteria:
  AC1: Given a dashboard report is displayed, when I select
       "Export as CSV", then a CSV file downloads containing
       all visible data columns with headers.
  AC2: Given a report has more than 10,000 rows, when I
       export, then all rows are included in the CSV (not
       just the visible page).
  AC3: Given a report contains date columns, when exported,
       then dates are formatted as ISO 8601 (YYYY-MM-DD).
  AC4: Given I have no data in the selected report, when I
       attempt to export, then I see a message "No data
       available to export" and no empty file is downloaded.
  AC5: Given the export process fails due to a server error,
       when the failure occurs, then I see an error message
       with a retry option and no partial file is downloaded.

  Size:         M
  Dependencies: None
  Notes:        CSV chosen over Excel because Tableau imports
                CSV natively. Excel export is a separate story
                if needed.

Story 2: Schedule recurring CSV export
  As an Analytics Manager,
  I want to schedule a recurring export of a dashboard report,
  So that my Tableau data source refreshes automatically
  without manual intervention each week.

  Acceptance Criteria:
  AC1: Given I am viewing a report, when I select "Schedule
       Export", then I can choose daily, weekly, or monthly
       frequency.
  AC2: Given a schedule is active, when the scheduled time
       arrives, then the CSV is generated and delivered to
       my configured destination (email or cloud storage).
  AC3: Given a scheduled export fails, when the failure
       occurs, then I receive an email notification with
       the error reason.
  AC4: Given I have an active schedule, when I delete the
       report, then the schedule is cancelled and I receive
       a notification.

  Size:         L
  Dependencies: Story 1 (CSV export must work first)
  Notes:        Cloud storage destinations (S3, GCS) may
                require a separate integration story.

Story 3: Preview export before download
  As an Analytics Manager,
  I want to preview the first 10 rows of an export before
  downloading the full file,
  So that I can verify the data and format are correct
  before importing into Tableau.

  Acceptance Criteria:
  AC1: Given I select "Export as CSV", when the export is
       ready, then I see a preview of the first 10 rows
       before confirming the download.
  AC2: Given the preview shows unexpected data, when I
       cancel, then no file is downloaded.
  AC3: Given the report has fewer than 10 rows, when I
       preview, then all rows are shown with a note
       indicating the full dataset is displayed.

  Size:         S
  Dependencies: Story 1
  Notes:        Preview renders in-app, not as a separate
                file download.
================================================================
```

## NEXT STEP

Provide the named personas and data context, and I will generate the full story set with proper acceptance criteria, sizing, and dependency mapping.

---

ALL OUTPUTS REQUIRE REVIEW BY THE PM AND ENGINEERING LEAD BEFORE SPRINT PLANNING.
