## Banking Plugin Compliance Report

### Summary
- Total skills audited: 17
- Total agents audited: 0
- Total violations found: 48
- Critical (invalid fields): 48
- Warning (best practice): 0
- plugin.json violations: 0

---

### Violations

#### banking/skills/banking-global-router/SKILL.md
No violations. Frontmatter is fully compliant.

---

#### banking/skills/aml-cdd-edd/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: FATF Recommendation 10 (CDD), 12 (PEPs), 13 (Correspondent Banking)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "FATF Recommendation 10 (CDD), 12 (PEPs), 13 (Correspondent Banking)"`

---

#### banking/skills/aml-sar-drafting/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Jurisdiction-specific — load jurisdiction overlay for format requirements` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Jurisdiction-specific — load jurisdiction overlay for format requirements"`

---

#### banking/skills/aml-typologies/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: FATF 40 Recommendations — jurisdiction AML legislation (load overlay)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "FATF 40 Recommendations — jurisdiction AML legislation (load overlay)"`

---

#### banking/skills/bank-reconciliation/SKILL.md
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`

---

#### banking/skills/basel-capital/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Basel III (BCBS) — jurisdiction implementations vary (load overlay)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Basel III (BCBS) — jurisdiction implementations vary (load overlay)"`

---

#### banking/skills/basel-rwa-credit/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Basel III Standardised Approach for Credit Risk (BCBS)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Basel III Standardised Approach for Credit Risk (BCBS)"`

---

#### banking/skills/basel-rwa-market/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity -- The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Basel III FRTB (BCBS d352/d457) -- jurisdiction implementations vary (load overlay)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Basel III FRTB (BCBS d352/d457) — jurisdiction implementations vary (load overlay)"`

---

#### banking/skills/ifrs9-disclosure/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: IFRS 7 Financial Instruments Disclosures` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "IFRS 7 Financial Instruments Disclosures"`

---

#### banking/skills/ifrs9-ecl/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: IFRS 9 Financial Instruments (IASB)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "IFRS 9 Financial Instruments (IASB)"`
- [ ] VIOLATION S27: `disclosure: IFRS 7 Financial Instruments Disclosures` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  disclosure: "IFRS 7 Financial Instruments Disclosures"`
- [ ] VIOLATION S27: `not_applicable_in: USA (use CECL / FASB ASC 326 instead)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  not_applicable_in: "USA (use CECL / FASB ASC 326 instead)"`

---

#### banking/skills/ifrs9-scenarios/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: IFRS 9.5.5.17 (Forward-looking information)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "IFRS 9.5.5.17 (Forward-looking information)"`

---

#### banking/skills/ifrs9-staging/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: IFRS 9.5.5 Impairment` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "IFRS 9.5.5 Impairment"`

---

#### banking/skills/kyc-risk-rating/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: FATF Recommendation 1 (Risk-Based Approach), Recommendation 10 (CDD)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "FATF Recommendation 1 (Risk-Based Approach), Recommendation 10 (CDD)"`

---

#### banking/skills/liquidity-lcr/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Basel III Liquidity Coverage Ratio (BCBS 2013, updated 2014)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Basel III Liquidity Coverage Ratio (BCBS 2013, updated 2014)"`

---

#### banking/skills/liquidity-nsfr/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: Basel III Net Stable Funding Ratio (BCBS 2014)` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "Basel III Net Stable Funding Ratio (BCBS 2014)"`

---

#### banking/skills/sanctions-screening/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: OFAC (USA), OFSI/HMT (UK), EU CFSP, UN Security Council Resolutions` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "OFAC (USA), OFSI/HMT (UK), EU CFSP, UN Security Council Resolutions"`

---

#### banking/skills/stress-testing/SKILL.md
- [ ] VIOLATION S20: `version: 1.0` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  version: "1.0"`
- [ ] VIOLATION S21: `author: Panaversity — The AI Agent Factory` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  author: "Panaversity — The AI Agent Factory"`
- [ ] VIOLATION S22: `standard: BCBS Pillar 2 / SREP framework — jurisdiction implementations vary` is not a valid SKILL.md frontmatter field
  - FIX: Move to `metadata:` block → `metadata:\n  standard: "BCBS Pillar 2 / SREP framework — jurisdiction implementations vary"`

---

#### banking/.claude-plugin/plugin.json
No violations. All fields (`name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`) are valid per P1–P15. No skills/agents/commands declared so P18 is not applicable.

---

### Proposed Fixed Frontmatter

#### banking/skills/banking-global-router/SKILL.md
No changes required.

---

#### banking/skills/aml-cdd-edd/SKILL.md
```yaml
---
name: aml-cdd-edd
description: >
  Activate for: CDD, EDD, customer due diligence, enhanced due diligence,
  simplified due diligence, KYC, know your customer, customer onboarding,
  source of wealth, source of funds, PEP, politically exposed person,
  beneficial ownership, UBO, corporate structure, ongoing monitoring.
  NOT for: personal finance advice or retail banking product recommendations,
  tax compliance or tax residency determinations, credit underwriting decisions.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "FATF Recommendation 10 (CDD), 12 (PEPs), 13 (Correspondent Banking)"
---
```

---

#### banking/skills/aml-sar-drafting/SKILL.md
```yaml
---
name: aml-sar-drafting
description: >
  Activate for: SAR, STR, suspicious activity report, suspicious transaction report,
  NCA, FinCEN, AUSTRAC, SAR narrative, SAR drafting, SAR format, MLRO,
  money laundering reporting officer, tipping-off, consent SAR, defence SAR.
  NOT for: transaction monitoring alert triage (use aml-typologies), customer
  due diligence or KYC onboarding (use aml-cdd-edd), sanctions screening (use
  sanctions-screening).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Jurisdiction-specific — load jurisdiction overlay for format requirements"
---
```

---

#### banking/skills/aml-typologies/SKILL.md
```yaml
---
name: aml-typologies
description: >
  Activate for: AML alert, transaction monitoring, suspicious activity,
  money laundering, structuring, smurfing, round-tripping, layering,
  placement, integration, typology, red flag, velocity alert, geographic
  anomaly, TBML, trade-based money laundering, network analysis, PEP alert.
  NOT for: SAR/STR drafting or filing (use aml-sar-drafting), customer onboarding
  or KYC documentation (use aml-cdd-edd), sanctions list screening (use
  sanctions-screening).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "FATF 40 Recommendations — jurisdiction AML legislation (load overlay)"
---
```

---

#### banking/skills/bank-reconciliation/SKILL.md
```yaml
---
name: bank-reconciliation
description: >
  Activate for: bank reconciliation, nostro reconciliation, suspense account,
  GL reconciliation, provision reconciliation, inter-company reconciliation,
  nostro break, unmatched item, reconciling item, MT940, MT950, MT942,
  aged items, reconciliation certificate, suspense clearing, four-way
  reconciliation, IFRS 9 provision reconciliation, settlement break,
  trade reconciliation, position break, GL-to-risk reconciliation.
  NOT for: IFRS 9 ECL model calculation (use ifrs9-ecl), capital adequacy
  reporting (use basel-capital), AML transaction monitoring (use aml-typologies).
metadata:
  author: "Panaversity — The AI Agent Factory"
---
```

---

#### banking/skills/basel-capital/SKILL.md
```yaml
---
name: basel-capital
description: >
  Activate for: CET1, Tier 1, Total Capital, capital ratio, RWA, risk-weighted
  assets, Basel III, Basel IV, capital adequacy, capital buffers, MDA, maximum
  distributable amount, leverage ratio, ICAAP, output floor, Pillar 2, CCB,
  CCyB, G-SIB, D-SIB, capital conservation buffer.
  NOT for: credit risk RWA calculation detail (use basel-rwa-credit), market risk
  FRTB capital (use basel-rwa-market), liquidity ratios LCR/NSFR (use liquidity-lcr
  / liquidity-nsfr).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III (BCBS) — jurisdiction implementations vary (load overlay)"
---
```

---

#### banking/skills/basel-rwa-credit/SKILL.md
```yaml
---
name: basel-rwa-credit
description: >
  Activate for: credit risk RWA, risk-weighted assets, standardised approach,
  SA risk weight, risk weight table, CCF, credit conversion factor, EAD,
  exposure at default, IRB approach, mortgage risk weight, LTV band,
  corporate risk weight, SME risk weight, CRE risk weight.
  NOT for: market risk RWA or FRTB calculations (use basel-rwa-market),
  overall capital adequacy ratios or buffer stacking (use basel-capital),
  IFRS 9 ECL provisioning or impairment (use ifrs9-ecl).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III Standardised Approach for Credit Risk (BCBS)"
---
```

---

#### banking/skills/basel-rwa-market/SKILL.md
```yaml
---
name: basel-rwa-market
description: >
  Activate for: FRTB, Fundamental Review of the Trading Book, market risk RWA,
  trading book capital, SA-TB, standardised approach trading book, sensitivities-
  based method, SBM, delta, vega, curvature, default risk charge, DRC, residual
  risk add-on, RRAO, internal models approach, IMA, expected shortfall, ES,
  P&L attribution, PLA, backtesting, GIRR, CSR, equity risk, commodity risk,
  FX risk, market risk capital, trading desk.
  NOT for: credit risk RWA under standardised or IRB approach (use basel-rwa-credit),
  capital adequacy ratios and buffer calculations (use basel-capital), IFRS 9 ECL
  provisioning (use ifrs9-ecl).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III FRTB (BCBS d352/d457) — jurisdiction implementations vary (load overlay)"
---
```

---

#### banking/skills/ifrs9-disclosure/SKILL.md
```yaml
---
name: ifrs9-disclosure
description: >
  Activate for: IFRS 7 disclosure, ECL disclosure note, credit risk
  disclosure, IFRS 9 annual report note, sensitivity analysis IFRS 9,
  stage distribution table, credit quality table, IFRS 7 note drafting.
  NOT for: ECL calculation methodology (use ifrs9-ecl), staging assessment
  (use ifrs9-staging), US GAAP disclosure requirements under ASC 326 / CECL.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 7 Financial Instruments Disclosures"
---
```

---

#### banking/skills/ifrs9-ecl/SKILL.md
```yaml
---
name: ifrs9-ecl
description: >
  Activate for: IFRS 9, ECL, expected credit loss, PD, LGD, EAD,
  loan loss provision, impairment, 12-month ECL, lifetime ECL,
  post-model adjustment, PMA, IFRS 7, provision movement, forward-looking.
  NOT for: US GAAP CECL calculation (ASC 326), hedge accounting under
  IFRS 9, classification and measurement of financial instruments.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 9 Financial Instruments (IASB)"
  disclosure: "IFRS 7 Financial Instruments Disclosures"
  not_applicable_in: "USA (use CECL / FASB ASC 326 instead)"
---
```

---

#### banking/skills/ifrs9-scenarios/SKILL.md
```yaml
---
name: ifrs9-scenarios
description: >
  Activate for: macro overlay, macroeconomic scenarios, PIT PD,
  point-in-time PD, credit cycle adjustment, scenario weighting,
  forward-looking information, satellite model, GDP, unemployment,
  house price index, IFRS 9 scenarios, scenario probability.
  NOT for: ECL calculation mechanics (use ifrs9-ecl), staging assessment
  (use ifrs9-staging), stress testing for capital adequacy (use stress-testing).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 9.5.5.17 (Forward-looking information)"
---
```

---

#### banking/skills/ifrs9-staging/SKILL.md
```yaml
---
name: ifrs9-staging
description: >
  Activate for: SICR, significant increase in credit risk, staging assessment,
  stage migration, Stage 1 to Stage 2, rebuttable presumption, 30 days past due,
  90 days past due, watchlist, covenant breach, stage cure, qualitative SICR.
  NOT for: initial recognition and measurement of financial instruments, hedge
  accounting, IFRS 9 classification questions, US GAAP CECL staging.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "IFRS 9.5.5 Impairment"
---
```

---

#### banking/skills/kyc-risk-rating/SKILL.md
```yaml
---
name: kyc-risk-rating
description: >
  Activate for: KYC risk rating, customer risk classification, AML risk score,
  customer risk assessment, high-risk customer, risk-based approach, risk rating,
  customer due diligence risk score, PEP risk, geographic risk, product risk,
  customer risk categories.
  NOT for: transaction monitoring alerts (use aml-typologies), SAR/STR drafting
  (use aml-sar-drafting), sanctions screening (use sanctions-screening).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "FATF Recommendation 1 (Risk-Based Approach), Recommendation 10 (CDD)"
---
```

---

#### banking/skills/liquidity-lcr/SKILL.md
```yaml
---
name: liquidity-lcr
description: >
  Activate for: LCR, liquidity coverage ratio, HQLA, high quality liquid assets,
  net cash outflow, run-off rate, Level 1 assets, Level 2A, Level 2B, 30-day
  stress scenario, liquidity buffer, liquidity coverage, cash outflow, inflow cap.
  NOT for: structural funding / NSFR calculations (use liquidity-nsfr), capital
  adequacy ratios (use basel-capital), interest rate risk in the banking book (IRRBB).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III Liquidity Coverage Ratio (BCBS 2013, updated 2014)"
---
```

---

#### banking/skills/liquidity-nsfr/SKILL.md
```yaml
---
name: liquidity-nsfr
description: >
  Activate for: NSFR, net stable funding ratio, available stable funding,
  required stable funding, ASF, RSF, structural liquidity, funding mismatch,
  term funding, long-term funding, stable funding, 1-year funding.
  NOT for: short-term liquidity stress (use liquidity-lcr), intraday liquidity
  monitoring, interest rate risk in the banking book (IRRBB), market risk capital.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III Net Stable Funding Ratio (BCBS 2014)"
---
```

---

#### banking/skills/sanctions-screening/SKILL.md
```yaml
---
name: sanctions-screening
description: >
  Activate for: sanctions, OFAC, HMT, SDN list, EU sanctions, UN sanctions,
  sanctioned entity, sanctions screening, false positive, name match,
  OFSI, consolidated list, sanctions breach, SWIFT screening, payments screening,
  sanctions compliance, derisking.
  NOT for: AML transaction monitoring or typology assessment (use aml-typologies),
  KYC customer onboarding CDD/EDD (use aml-cdd-edd), SAR drafting (use aml-sar-drafting).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "OFAC (USA), OFSI/HMT (UK), EU CFSP, UN Security Council Resolutions"
---
```

---

#### banking/skills/stress-testing/SKILL.md
```yaml
---
name: stress-testing
description: >
  Activate for: ICAAP, ILAAP, stress test, capital depletion, reverse stress test,
  ACS (Annual Cyclical Scenario), DFAST, CCAR, BoE stress test, EBA stress test,
  stressed capital ratio, Pillar 2, capital planning, going concern, stressed ECL,
  stressed RWA, stressed NII.
  NOT for: IFRS 9 macroeconomic scenario weighting (use ifrs9-scenarios),
  market risk capital under FRTB (use basel-rwa-market), liquidity stress
  testing for LCR/NSFR purposes (use liquidity-lcr / liquidity-nsfr).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "BCBS Pillar 2 / SREP framework — jurisdiction implementations vary"
---
```
