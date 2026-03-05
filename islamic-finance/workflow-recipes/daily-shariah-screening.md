# Workflow Recipe: Daily Shariah Equity Screening

## Task Overview

| Field         | Value                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Task Name** | Daily Shariah Equity Screening                                                                                                        |
| **Frequency** | Daily (end of business day, after market close)                                                                                       |
| **Purpose**   | Screen all portfolio holdings against applicable Shariah screening methodologies and flag compliance breaches for immediate attention |
| **Owner**     | Portfolio compliance officer / Shariah compliance unit                                                                                |

---

## Trigger Conditions

| Trigger          | Condition                                                       | Action                                                            |
| ---------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Scheduled**    | Every business day at 18:00 local time (after market close)     | Run full screening cycle                                          |
| **Event-driven** | New position added to portfolio                                 | Screen new position immediately against all applicable frameworks |
| **Event-driven** | Company publishes quarterly financials                          | Re-screen that company with updated financial ratios              |
| **Event-driven** | Screening methodology update (SC Malaysia list, MSCI rebalance) | Re-screen entire portfolio against updated methodology            |
| **Manual**       | Shariah Supervisory Board requests ad-hoc screening             | Run full or targeted screening per SSB instruction                |

---

## Step-by-Step Execution

### Step 1: Load Current Portfolio Holdings

```
Source: /inputs/portfolio-holdings.csv
Fields required: Ticker, Company Name, Sector, Market Cap, Shares Held, Market Value, Jurisdiction
Validate: All required fields populated, no stale data (last update < 24 hours)
```

### Step 2: Fetch Updated Financial Data

```
Source: Financial data provider API or /inputs/financial-ratios.csv
For each holding, retrieve:
  - Total debt
  - Total assets
  - Cash + interest-bearing securities
  - Accounts receivable
  - Total revenue
  - Non-permissible revenue (breakdown by category)
  - Sector classification (GICS or equivalent)
Validate: Data date within 90 days of current date (quarterly refresh cycle)
```

### Step 3: Apply Screening Criteria

Run each holding against ALL applicable screening frameworks:

| Framework          | Debt/TA Limit | Cash+IBS/TA Limit | NPI/Revenue Limit | AR/TA Limit |
| ------------------ | ------------- | ----------------- | ----------------- | ----------- |
| SC Malaysia        | < 33%         | < 33%             | < 5%              | N/A         |
| Tadawul (Saudi)    | < 33%         | < 33%             | < 5%              | < 49%       |
| AAOIFI Standard 21 | < 30%         | < 30%             | < 5%              | < 45%       |
| MSCI Islamic Index | < 33.33%      | < 33.33%          | < 5%              | < 49%       |

Also check sector exclusions: conventional financial services, alcohol, tobacco, gambling, weapons, pork, adult entertainment (MSCI adds nuclear weapons, civilian firearms).

### Step 4: Classify Results

For each holding, assign status:

| Status            | Definition                                                            | Action Required                            |
| ----------------- | --------------------------------------------------------------------- | ------------------------------------------ |
| **COMPLIANT**     | Passes all applicable screens                                         | None                                       |
| **BORDERLINE**    | Any ratio within 2% of threshold (e.g., debt/TA at 31% vs. 33% limit) | Add to watchlist, alert compliance officer |
| **NON-COMPLIANT** | Fails one or more screens                                             | Trigger divestment alert                   |
| **DIVERGENT**     | Passes some screens, fails others                                     | Flag for SSB adjudication                  |
| **DATA STALE**    | Financial data older than 90 days                                     | Flag for data refresh                      |

### Step 5: Generate Compliance Report

```
Output: /outputs/daily-screening-report-[YYYY-MM-DD].md
Sections:
  1. Portfolio Summary: X holdings screened, Y compliant, Z non-compliant, W borderline
  2. Non-Compliant Holdings: Company, which screen(s) failed, specific ratio(s), recommended action
  3. Borderline Holdings: Company, which ratio(s) within 2% of threshold
  4. Divergent Holdings: Company, which screens pass/fail, SSB decision needed
  5. Changes from Prior Day: Newly non-compliant, newly compliant, status changes
  6. Data Quality: Holdings with stale data
```

### Step 6: Escalation (if applicable)

```
IF any holding is NEWLY NON-COMPLIANT:
  → Send priority alert to: Shariah compliance officer, portfolio manager, SSB chair
  → Alert content: Company name, failed screen(s), current ratio(s), divestment deadline
  → Divestment deadline: Per fund policy (typically 30-90 days for newly non-compliant)

IF any holding is DIVERGENT:
  → Send SSB referral with: Company name, which screens pass/fail, all ratio data
  → Request: SSB ruling on which methodology governs for this holding
```

---

## Required Skill Files

| Skill File                            | Purpose                                                         |
| ------------------------------------- | --------------------------------------------------------------- |
| `shariah-screening-global.md`         | All four screening methodologies, thresholds, sector exclusions |
| Jurisdiction overlays (as applicable) | SC Malaysia, Tadawul, AAOIFI specifics                          |

---

## Output Deliverables

| Deliverable            | Format                             | Recipient                             |
| ---------------------- | ---------------------------------- | ------------------------------------- |
| Daily screening report | Markdown (.md)                     | Compliance officer, portfolio manager |
| Non-compliance alert   | Priority notification              | Shariah compliance officer, SSB chair |
| Screening matrix       | Spreadsheet (.xlsx)                | Compliance file (audit trail)         |
| Watchlist update       | Appended to /outputs/watchlist.csv | Ongoing monitoring                    |

---

## Escalation / Review Checkpoints

| Checkpoint                | Condition                                           | Reviewer                        |
| ------------------------- | --------------------------------------------------- | ------------------------------- |
| **Daily sign-off**        | Screening report reviewed and acknowledged          | Compliance officer              |
| **Weekly SSB update**     | Cumulative changes reported to SSB                  | SSB secretary                   |
| **Quarterly full review** | Complete re-screening with refreshed financial data | SSB + external auditor          |
| **Divestment tracking**   | Non-compliant holdings tracked until fully divested | Portfolio manager + compliance  |
| **Methodology update**    | When any screening body updates its criteria        | SSB for policy alignment review |
