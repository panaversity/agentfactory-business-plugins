USER STORIES: Dashboard Date Range Filter
================================================================
Epic: Date Range Filtering — Enable users to filter all dashboard
widgets by preset or custom date ranges, persisting their selection
across navigation.
Stories: 5 | Sprints: 1 | Persona(s): Marketing Analyst, Sales Manager, Executive Stakeholder

> **Note — Personas**: No `product.local.md` was found. Personas below
> are inferred from the analytics dashboard context. Replace with your
> actual product personas before sprint planning.

-- MARKETING ANALYST STORIES ----------------------------------------

Story 1: Filter dashboard by preset date range
  As a Marketing Analyst,
  I want to select a preset date range (7d, 30d, 90d, YTD) from
  the dashboard header,
  So that I can quickly scope campaign metrics to standard
  reporting periods without manual data exports.

  Acceptance Criteria:
  AC1: Given the dashboard is loaded, when I click the date range
       selector, then I see preset options: 7d, 30d, 90d, YTD.
  AC2: Given I select "30d", when the selection is applied, then
       all dashboard widgets display data for the last 30 days only.
  AC3: Given I select "YTD", when the current date is January 1,
       then the range covers January 1 to January 1 (single day)
       and widgets render without error.
  AC4: Given the data source returns an error for the selected range,
       when the request fails, then each affected widget shows an
       inline error state (not a blank widget).

  Size:         M
  Dependencies: None
  Notes:        "7d" means rolling 7 calendar days ending today.
                YTD starts January 1 of the current year.

Story 2: Filter dashboard by custom date range
  As a Marketing Analyst,
  I want to select a custom start and end date for the dashboard,
  So that I can analyse campaign performance for specific
  promotional windows that don't match preset ranges.

  Acceptance Criteria:
  AC1: Given I open the date range selector, when I choose "Custom",
       then I see start-date and end-date inputs.
  AC2: Given I enter a valid start date before the end date, when I
       apply the range, then all dashboard widgets update to show
       data within that range (inclusive of both dates).
  AC3: Given I enter a start date after the end date, when I attempt
       to apply, then I see an error message stating the start date
       must be before the end date.
  AC4: Given I enter a start date in the future (beyond today), when
       I apply the range, then I see an error message stating the
       range must not extend beyond today.
  AC5: Given I clear one of the two date fields and attempt to apply,
       then I see an error message stating both dates are required.

  Size:         M
  Dependencies: Story 1 (shared date range selector UI)
  Notes:        Clarify with engineering whether partial-day
                boundaries use start-of-day / end-of-day or
                the user's timezone.

-- SALES MANAGER STORIES -------------------------------------------

Story 3: Dashboard widgets react to date range changes
  As a Sales Manager,
  I want all dashboard widgets to update simultaneously when I
  change the date range,
  So that I can compare pipeline metrics across a consistent
  time window without checking each widget individually.

  Acceptance Criteria:
  AC1: Given I change the date range, when the new range is applied,
       then every widget on the dashboard re-fetches and displays
       data for the new range.
  AC2: Given a widget is still loading data from the previous range
       change, when I select a new range, then the in-flight request
       is cancelled and the widget fetches the latest range.
  AC3: Given one widget fails to load data for the new range, when
       other widgets succeed, then only the failed widget shows an
       error — successful widgets render normally.
  AC4: Given the dashboard has 10+ widgets, when I change the range,
       then a loading indicator appears on each widget until its data
       arrives (no stale data shown during loading).

  Size:         M
  Dependencies: Story 1 (date range selector exists)
  Notes:        Coordinate with backend on whether widgets make
                individual API calls or a single batch request.
                Consider debouncing rapid range changes.

-- EXECUTIVE STAKEHOLDER STORIES ------------------------------------

Story 4: Date range persists across page navigation
  As an Executive Stakeholder,
  I want my selected date range to persist when I navigate between
  dashboard pages,
  So that I do not have to re-select my reporting period every time
  I switch views during a board review.

  Acceptance Criteria:
  AC1: Given I select "90d" on the Overview page, when I navigate to
       the Revenue page, then the "90d" range is still active and
       widgets show 90-day data.
  AC2: Given I select a custom range, when I navigate away and return,
       then the custom start and end dates are preserved.
  AC3: Given I have a persisted range and I open the dashboard in a
       new browser tab, then the new tab uses the default range (not
       the other tab's selection).
  AC4: Given my persisted range becomes invalid (e.g., "YTD" crosses
       a year boundary overnight), when I return to the dashboard,
       then the range recalculates to the current YTD rather than
       showing stale boundaries.

  Size:         S
  Dependencies: Story 1 (date range selector exists)
  Notes:        Persistence mechanism TBD — URL query params
                recommended over localStorage for shareability.
                Clarify whether persistence survives logout.

Story 5: Invalid date range error handling
  As an Executive Stakeholder,
  I want to see a clear error message when I enter an invalid date
  range,
  So that I understand what to correct instead of seeing a broken
  or empty dashboard.

  Acceptance Criteria:
  AC1: Given I enter a start date after the end date, when I attempt
       to apply, then I see an inline error message below the date
       inputs: "Start date must be before end date."
  AC2: Given I enter a date in an unsupported format (e.g., text),
       when I attempt to apply, then the input rejects the entry
       with a format hint (e.g., "Use MM/DD/YYYY").
  AC3: Given I select a range spanning more than 365 days, when I
       apply, then either the range is accepted or a clear limit
       message is shown (decide with PM — flag for backlog).
  AC4: Given I dismiss the error and correct the dates, when I
       re-apply, then the error clears and widgets update normally.

  Size:         S
  Dependencies: Story 2 (custom date input exists)
  Notes:        Error messages should be user-friendly, not
                technical. Consider accessibility — errors must
                be announced to screen readers.

================================================================

COVERAGE ANALYSIS
================================================================

Spec ACs → Story mapping:
  AC1 (Preset ranges)              → Story 1
  AC2 (Custom start/end date)      → Story 2
  AC3 (All widgets update)         → Story 3
  AC4 (Persists across navigation) → Story 4
  AC5 (Invalid range error)        → Story 5, Story 2 (AC3-AC5)

Gaps identified:
  GAP 1: The spec does not define a default date range (what does a
         new user see on first load?). Recommend adding a story or
         AC for default range behaviour (suggest 30d).
  GAP 2: The spec does not mention URL shareability. If an executive
         shares a dashboard link, should the date range be encoded
         in the URL? Recommend yes — add to Story 4 or new story.
  GAP 3: The spec does not address timezone handling. Users in
         different timezones may see different "today" boundaries.
         Recommend a sub-task under Story 1 to define timezone
         policy.
  GAP 4: The spec does not mention keyboard accessibility or screen
         reader support for the date picker. Recommend as AC on
         Story 2 or a separate accessibility story.

Implementation details moved to sub-tasks (not stories):
  - Date picker component selection (engineering)
  - API query parameter design for date filtering (engineering)
  - Widget loading state skeleton design (engineering/design)
  - State management approach for range persistence (engineering)

================================================================
ALL OUTPUTS REQUIRE REVIEW BY THE PM AND ENGINEERING LEAD
BEFORE SPRINT PLANNING.
================================================================
