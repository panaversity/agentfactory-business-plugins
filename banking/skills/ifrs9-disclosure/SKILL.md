---
name: ifrs9-disclosure
version: 1.0
description: >
  Activate for: IFRS 7 disclosure, ECL disclosure note, credit risk
  disclosure, IFRS 9 annual report note, sensitivity analysis IFRS 9,
  stage distribution table, credit quality table, IFRS 7 note drafting.
  NOT for: ECL calculation methodology (use ifrs9-ecl), staging assessment
  (use ifrs9-staging), US GAAP disclosure requirements under ASC 326 / CECL.
standard: IFRS 7 Financial Instruments Disclosures
author: Panaversity — The AI Agent Factory
---

## IFRS 7 ECL DISCLOSURE REQUIREMENTS — COMPLETE LIST

### Qualitative Disclosures (always required)

1. SICR assessment methodology — quantitative and qualitative criteria used
2. Definition of default — the bank's specific definition and why it was chosen
3. Write-off policy — when exposures are derecognised (written off)
4. Macroeconomic scenario descriptions — narrative for each scenario
5. ECL model methodology — overview for each major portfolio segment
6. PMA rationale — types and reasons for post-model adjustments

### Quantitative Disclosures (always required)

7. Stage distribution table — gross carrying amount and ECL by stage, by product
8. Stage migration table — movements during the period with ECL impact
9. Credit quality table — gross carrying amounts by internal credit grade
10. Macroeconomic variables — key variables and their values in each scenario
11. Scenario weights — probability assigned to each scenario
12. Sensitivity analysis — ECL under each scenario individually (IFRS 7.35G)
13. PMA amounts — aggregate PMA by direction (add/release) with rationale
14. Modified financial assets — amounts restructured, conditions, Stage post-modification
15. Collateral — types held, LTV distributions for mortgage portfolios
16. Concentration risk — geographic and industry concentrations

### For Stage 3 Specifically

17. Gross carrying amount vs. ECL provision by product (coverage ratio)
18. Write-offs during the period
19. Recoveries on previously written-off amounts

## TEMPLATE: STAGE DISTRIBUTION TABLE

|                           | Stage 1 | Stage 2 | Stage 3 | Total |
| ------------------------- | ------- | ------- | ------- | ----- |
| Gross carrying amount (M) |         |         |         |       |
| ECL provision (M)         |         |         |         |       |
| Net carrying amount (M)   |         |         |         |       |
| ECL coverage ratio %      |         |         |         |       |
| Number of facilities      |         |         |         |       |

Repeat for each major product category (mortgages, SME, corporate, consumer, etc.)

## TEMPLATE: STAGE MIGRATION TABLE

| Movement                                      | Gross Amount (M) | ECL Impact (M)             |
| --------------------------------------------- | ---------------- | -------------------------- |
| Opening balance — Stage 1                     |                  |                            |
| Opening balance — Stage 2                     |                  |                            |
| Opening balance — Stage 3                     |                  |                            |
| New financial assets originated (all Stage 1) | +                | +                          |
| Transfers: Stage 1 to Stage 2                 | reclassify       | + (lifetime vs. 12-mo ECL) |
| Transfers: Stage 1 to Stage 3                 | reclassify       | +                          |
| Transfers: Stage 2 to Stage 3                 | reclassify       | +                          |
| Transfers: Stage 3 to Stage 2 (cures)         | reclassify       | -                          |
| Transfers: Stage 2 to Stage 1 (cures)         | reclassify       | -                          |
| Repayments / maturities                       | -                | - (ECL released)           |
| Write-offs                                    | -                | - (matched derecognition)  |
| Changes in model parameters                   | --               | +/-                        |
| Changes in macroeconomic scenarios            | --               | +/-                        |
| PMA movements                                 | --               | +/-                        |
| Closing balance — Stage 1                     |                  |                            |
| Closing balance — Stage 2                     |                  |                            |
| Closing balance — Stage 3                     |                  |                            |

## TEMPLATE: CREDIT QUALITY TABLE

| Internal Grade     | Description                     | Gross Amount (M) | ECL (M) | Coverage % |
| ------------------ | ------------------------------- | ---------------- | ------- | ---------- |
| 1 -- Minimal risk  | AAA-AA equivalent               |                  |         |            |
| 2 -- Low risk      | A equivalent                    |                  |         |            |
| 3 -- Standard      | BBB equivalent                  |                  |         |            |
| 4 -- Watch         | BB equivalent, SICR approaching |                  |         |            |
| Stage 2 -- SICR    | Various                         |                  |         |            |
| Stage 3 -- Default | Various                         |                  |         |            |

## TEMPLATE: COLLATERAL AND LTV DISTRIBUTION TABLE (IFRS 7.35K)

| LTV Band                 | Gross Amount (M) | ECL (M) | Coverage % | % of Mortgage Book |
| ------------------------ | ---------------- | ------- | ---------- | ------------------ |
| <= 50%                   |                  |         |            |                    |
| 50-60%                   |                  |         |            |                    |
| 60-70%                   |                  |         |            |                    |
| 70-80%                   |                  |         |            |                    |
| 80-90%                   |                  |         |            |                    |
| 90-100%                  |                  |         |            |                    |
| > 100% (negative equity) |                  |         |            |                    |
| Total                    |                  |         |            |                    |

Collateral types to disclose: residential property, commercial property,
cash collateral, financial guarantees, credit insurance, receivables.
For each type: fair value, frequency of revaluation, methodology for valuation.

## TEMPLATE: CONCENTRATION RISK TABLE (IFRS 7.35M)

| Dimension | Segment            | Gross Amount (M) | % of Total | ECL (M) | Coverage % |
| --------- | ------------------ | ---------------- | ---------- | ------- | ---------- |
| Geography | UK                 |                  |            |         |            |
| Geography | Europe (ex-UK)     |                  |            |         |            |
| Geography | North America      |                  |            |         |            |
| Geography | Asia Pacific       |                  |            |         |            |
| Geography | Middle East        |                  |            |         |            |
| Industry  | Financial services |                  |            |         |            |
| Industry  | Real estate        |                  |            |         |            |
| Industry  | Manufacturing      |                  |            |         |            |
| Industry  | Retail/Consumer    |                  |            |         |            |

## SENSITIVITY ANALYSIS FORMAT (IFRS 7.35G REQUIREMENT)

"If the [upside / adverse / severe] macroeconomic scenario were applied with a
100% weighting, the Group's ECL provision would be [X higher / X lower],
representing a [Y%] [increase / decrease] from the reported provision of [Z]."

Calculate and disclose for each named scenario.
This is one of the most scrutinised disclosures in bank annual reports.

### Extended Sensitivity Disclosure (Best Practice)

In addition to single-scenario sensitivity, disclose:

- ECL impact of a 10% shift in scenario weights (e.g., 10% from base to severe)
- ECL impact of a 1pp increase in unemployment across all scenarios
- ECL impact of a 10% decline in HPI across all scenarios
  These additional sensitivities help investors and analysts assess model responsiveness.

## DRAFTING STANDARDS FOR ECL NOTES

- Use plain English alongside technical terms
- Quantify every disclosure where possible (avoid "significant" without a number)
- Cross-reference to the accounting policy note for IFRS 9 classification and measurement
- Distinguish clearly between performing (Stage 1/2) and non-performing (Stage 3)
- Auditors will check every number in the disclosure ties to the ECL model output
- Ensure year-on-year comparatives are presented for all quantitative tables
- Changes from prior period must be explained narratively, not just shown numerically

## OUTPUT FORMAT — DISCLOSURE NOTE DRAFT

```
IFRS 7 ECL DISCLOSURE NOTE
Entity:             [Bank / Group name]
Reporting Period:   [YYYY-MM-DD to YYYY-MM-DD]

SECTION 1: QUALITATIVE
  SICR methodology:      [Summary of quantitative and qualitative criteria]
  Definition of default: [Bank's definition with rationale]
  Write-off policy:      [When exposures are derecognised]
  ECL model overview:    [Summary by portfolio segment]
  PMA rationale:         [Types applied and reasons]

SECTION 2: QUANTITATIVE
  [Stage distribution table — by product]
  [Stage migration table — with ECL impact]
  [Credit quality table — by rating grade]
  [Sensitivity analysis — per IFRS 7.35G]
  [Scenario weights and key variables]
  [PMA aggregate amounts]
  [Collateral / LTV distribution]
  [Concentration risk — geographic and industry]

SECTION 3: STAGE 3 DETAIL
  Stage 3 coverage ratios by product
  Write-offs during period
  Recoveries on prior write-offs
```

## NEVER DO THESE

- NEVER draft disclosure tables from a stale risk system extract — all numbers must tie to the approved ECL model output for the reporting date; stale extracts are the most common source of disclosure restatements
- NEVER omit the IFRS 7.35G sensitivity analysis — regulators and auditors treat this as a mandatory disclosure; omission will result in a qualified audit opinion or regulatory finding
- NEVER present ECL disclosure without year-on-year comparatives — IFRS 7 requires comparative information, and omission raises immediate auditor concern
- NEVER use vague language ("significant increase", "material amount") without quantification — every qualitative descriptor must be supported by a number
- NEVER disclose scenario weights that do not sum to 100% — this is an immediate credibility issue and will be flagged by both auditors and analysts

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
