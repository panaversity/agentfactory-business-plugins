---
name: us-federal
version: 1.0
description: >
  Jurisdiction overlay for United States — Federal Reserve, OCC, FDIC for
  capital; FinCEN for AML; FASB ASC 326 (CECL) for credit losses.
  CRITICAL: The USA uses CECL, not IFRS 9 ECL. Do NOT apply IFRS 9 rules
  to US banks — the models, timing, and calculation methodology differ materially.
regulator_capital: Federal Reserve (bank holding companies and FBOs); OCC (national banks); FDIC (state non-member banks)
regulator_conduct: Consumer Financial Protection Bureau (CFPB)
aml_regulator: FinCEN (Financial Crimes Enforcement Network); OFAC (sanctions)
accounting_standard: US GAAP — FASB ASC 326 (CECL — Current Expected Credit Loss)
capital_framework: US Basel III Final Rule (2013) + Basel III Endgame proposed rules
aml_legislation: Bank Secrecy Act (BSA) 1970, USA PATRIOT Act 2001, AML Act 2020
author: Panaversity — The AI Agent Factory
---

## CRITICAL: CECL vs IFRS 9 — KEY DIFFERENCES

| Feature | IFRS 9 ECL | US CECL (ASC 326) |
|---|---|---|
| Standard | IASB | FASB |
| Scope | All financial assets | Loans held for investment, held-to-maturity debt securities, lease receivables |
| Loss horizon | Stage 1: 12-month; Stage 2/3: lifetime | ALWAYS lifetime — no 12-month stage |
| Staging | 3-stage model (SICR required for lifetime ECL) | No staging — lifetime ECL from day 1 for all loans |
| Effective date | January 2018 | Large public companies: January 2020; others phased |
| Interest income | Stage 3: net basis | Troubled debt restructurings: gross basis retained |

CECL KEY POINT: Under CECL, banks must estimate lifetime expected credit losses
for ALL loans from the moment of origination — there is no 12-month ECL stage.
This front-loads credit loss recognition compared to IFRS 9.

## US CAPITAL FRAMEWORK — BASEL III FINAL RULE
Minimum ratios (US implementation): CET1 4.5%; T1 6.0%; TC 8.0%; Leverage 4.0%
  Note: US leverage ratio = 4.0% (higher than Basel 3.0% minimum)
Capital Conservation Buffer: 2.5%
Countercyclical Capital Buffer (CCyB): 0%–2.5% (set by Fed; currently under review)
Enhanced Supplementary Leverage Ratio (eSLR): G-SIBs must maintain T1 / total leverage
  exposure ≥ 5% (bank holding company); ≥ 6% (subsidiary banks)

G-SIB Surcharge: 1.0%–3.5% based on G-SIB score (methodology differs from BCBS)
  US G-SIBs include: JPMorgan Chase, Bank of America, Wells Fargo, Citigroup,
  Goldman Sachs, Morgan Stanley, BNY Mellon, State Street

Basel III Endgame / Basel IV US Implementation:
  US is still finalising the US implementation of Basel IV (output floor etc.)
  Final rule expected — check Federal Reserve website for current status.

## US STRESS TESTING — DFAST / CCAR
Dodd-Frank Act Stress Test (DFAST): Annual supervisory stress test for large banks
Comprehensive Capital Analysis and Review (CCAR): Annual capital planning supervisory process
  DFAST/CCAR scenarios: Supervisory baseline, adverse, severely adverse
  Results: Published for large banks — market benchmark for capital adequacy
  Severely adverse scenario: typically GDP −4–5%, unemployment 10%+

## US AML — BSA / PATRIOT ACT
Bank Secrecy Act (BSA): primary US AML statute
FinCEN SAR: Required when bank knows, suspects, or has reason to suspect a transaction involves
  funds from illegal activity AND involves $5,000+ (or $2,000+ for certain drug offences)
  SAR format: FinCEN Form 114/111 (BSA E-Filing System)
  Filing deadline: 30 calendar days after detection (60 days if no suspect identified)

Currency Transaction Report (CTR): Required for all cash transactions > $10,000
  (or structured transactions that bank knows are intended to evade the $10,000 threshold)

Tipping-off: Prohibited under 31 USC 5318(g)(2). Civil and criminal penalties.
Beneficial ownership rule: FinCEN 2016 rule — collect and verify BO for legal entities
  at 25% ownership threshold (with 1 individual control person at any ownership level)

OFAC screening: All banks must screen against OFAC SDN list. Strict liability.
  OFAC reporting: Within 10 business days of blocking funds; annually for blocked property.

## US SPECIFIC — COMMUNITY REINVESTMENT ACT (CRA)
Applies to FDIC-insured depository institutions.
Not a capital or AML rule — but affects bank lending strategy and community investment.
CRA rating influences merger approvals and can constrain bank activities.
