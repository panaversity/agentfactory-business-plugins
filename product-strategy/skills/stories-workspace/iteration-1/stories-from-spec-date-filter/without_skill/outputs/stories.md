# User Stories: Dashboard Date Range Filter

## Epic: Dashboard Date Range Filtering

**Problem**: Users cannot filter dashboard data by custom date ranges. They currently export to Excel and filter manually.

**Solution**: Add a date range picker to the dashboard header that filters all widgets.

---

## Story 1: Preset Date Range Selection

**As a** dashboard user,
**I want to** select from preset date ranges (7 days, 30 days, 90 days, Year-to-Date),
**So that** I can quickly view common reporting periods without manual date entry.

### Acceptance Criteria

- [ ] A date range picker is visible in the dashboard header
- [ ] The picker displays four preset options: 7d, 30d, 90d, YTD
- [ ] Selecting a preset immediately calculates the correct start and end dates relative to today
- [ ] YTD calculates from January 1 of the current year to today
- [ ] The currently selected preset is visually highlighted
- [ ] A default preset is selected on first load (e.g., 30d)

---

## Story 2: Custom Date Range Selection

**As a** dashboard user,
**I want to** select a custom start date and end date,
**So that** I can analyze data for specific periods that don't match the presets.

### Acceptance Criteria

- [ ] The date range picker includes a "Custom" option that reveals start and end date inputs
- [ ] Both start and end dates can be selected via a calendar date picker
- [ ] The selected custom range is applied when the user confirms the selection
- [ ] Selecting a custom range deselects any active preset
- [ ] The chosen start and end dates are displayed in the picker after selection

---

## Story 3: Dashboard Widgets Update on Range Change

**As a** dashboard user,
**I want** all dashboard widgets to update when I change the date range,
**So that** every chart, table, and metric reflects the same time period.

### Acceptance Criteria

- [ ] Changing the date range (preset or custom) triggers a data refresh for all widgets
- [ ] All widgets display data scoped to the selected start and end dates
- [ ] A loading state is shown on widgets while data is being fetched
- [ ] If a widget has no data for the selected range, it displays an empty state (not an error)
- [ ] Widgets do not flicker or reset scroll position unnecessarily during refresh

---

## Story 4: Date Range Persists Across Navigation

**As a** dashboard user,
**I want** my selected date range to persist when I navigate away and return to the dashboard,
**So that** I don't have to reselect my date range every time I switch pages.

### Acceptance Criteria

- [ ] The selected date range is stored (e.g., in URL params, session storage, or user preferences)
- [ ] Navigating away from the dashboard and returning restores the previously selected range
- [ ] If a preset was selected, the preset is restored (not a stale absolute date)
- [ ] If a custom range was selected, the exact start and end dates are restored
- [ ] Opening the dashboard in a new tab uses the default range, not another tab's selection

---

## Story 5: Invalid Date Range Validation

**As a** dashboard user,
**I want to** see a clear error message when I select an invalid date range,
**So that** I understand what went wrong and can correct it.

### Acceptance Criteria

- [ ] An error is shown if the start date is after the end date
- [ ] An error is shown if a future end date beyond today is selected (if applicable to the data source)
- [ ] An error is shown if either date field is left empty when submitting a custom range
- [ ] Error messages are displayed inline near the date picker, not as a page-level alert
- [ ] The previous valid range remains active until a new valid range is submitted
- [ ] The submit/apply button is disabled while the range is invalid
