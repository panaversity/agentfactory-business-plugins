---
name: banking-global-router
description: >
  Routes banking regulatory queries to the correct product skill and jurisdiction
  overlay. Activate for any query involving IFRS 9, ECL, expected credit loss,
  Stage 1, Stage 2, Stage 3, SICR, PD, LGD, EAD, Basel III, Basel IV, CET1,
  RWA, capital ratio, LCR, NSFR, HQLA, ICAAP, stress test, AML, KYC, CDD, EDD,
  SAR, STR, sanctions, OFAC, HMT, PEP, FATF, reconciliation, nostro, suspense,
  FRTB, market risk RWA. Covers 7 jurisdictions across multiple regulatory
  regimes (PRA, ECB/EBA, Fed/OCC, APRA, MAS, CBUAE, SBP).
---

## PURPOSE

Top-level routing controller. Determines which domain SKILL.md and
jurisdiction overlay to load before generating any banking regulatory output.
Does NOT contain regulatory rules -- it routes to the files that do.

## STEP 1 -- IDENTIFY JURISDICTION

Read query for: country, regulator name, or regulatory standard reference.
If no jurisdiction identifiable: ASK before proceeding.
NEVER default to any jurisdiction.

## STEP 2 -- LOAD DOMAIN FILE

| Query Terms                                             | Load                         |
| ------------------------------------------------------- | ---------------------------- |
| IFRS 9, ECL, PD, LGD, EAD, impairment, provision        | ifrs9-ecl                    |
| Stage 1/2/3, SICR, staging, DPD, covenant breach        | ifrs9-staging                |
| Macro overlay, PIT PD, scenarios, credit cycle          | ifrs9-scenarios              |
| IFRS 7 disclosure, ECL note, sensitivity analysis       | ifrs9-disclosure             |
| CET1, RWA, capital ratio, MDA, output floor, ICAAP      | basel-capital                |
| SA risk weight, credit RWA, CCF, standardised approach  | basel-rwa-credit             |
| FRTB, market risk RWA, trading book, SBM, DRC, IMA      | basel-rwa-market             |
| LCR, HQLA, liquidity coverage, run-off rate             | liquidity-lcr                |
| NSFR, stable funding, ASF, RSF                          | liquidity-nsfr               |
| Stress test, capital depletion, ACS, DFAST, ICAAP       | stress-testing               |
| AML alert, typology, money laundering, structuring      | aml-typologies               |
| SAR, STR, suspicious activity report, NCA, FinCEN       | aml-sar-drafting             |
| CDD, EDD, KYC, source of wealth, PEP onboarding         | aml-cdd-edd                  |
| Sanctions, OFAC, HMT, SDN, sanctioned entity            | sanctions-screening          |
| KYC risk rating, customer risk, risk classification     | kyc-risk-rating              |
| Nostro, suspense, GL recon, provision recon, settlement | bank-reconciliation          |
| CECL, ASC 326, US ECL, current expected credit losses   | us-cecl (comparison overlay) |
| Islamic banking, AAOIFI, FAS 30, riba, murabaha, ijara  | islamic-banking-interaction  |

## STEP 3 -- LOAD JURISDICTION OVERLAY

When a jurisdiction is identified, load the appropriate overlay:

- [UK / PRA / FCA](references/jurisdictions/uk-pra.md)
- [EU / ECB / EBA / CRR](references/jurisdictions/eu-crr.md)
- [USA / Fed / OCC / FinCEN](references/jurisdictions/us-federal.md)
- [Australia / APRA / AUSTRAC](references/jurisdictions/australia-apra.md)
- [Singapore / MAS](references/jurisdictions/singapore-mas.md)
- [UAE / CBUAE](references/jurisdictions/uae-cbuae.md)
- [Pakistan / SBP](references/jurisdictions/pakistan-sbp.md)
- [GCC / SAMA / CBUAE / CBB / CBK / QCB](references/jurisdictions/gcc-gcc.md)
- [CECL / ASC 326 / US ECL comparison](references/jurisdictions/us-cecl.md)
- [Islamic banking / AAOIFI / riba / murabaha](references/jurisdictions/islamic-banking-interaction.md)

## STEP 4 -- MANDATORY OUTPUT HEADER

Every banking regulatory output must begin with:
GOVERNING STANDARD: [e.g. IFRS 9 / Basel III SA -- UK PRA]
DOMAIN: [e.g. IFRS 9 ECL -- Stage Assessment]
JURISDICTION: [e.g. United Kingdom -- PRA Rulebook / UK CRR]

## UNIVERSAL RULES

- NEVER use incurred-loss thinking for IFRS 9 -- it is forward-looking
- NEVER recognise Stage 3 interest on the gross carrying amount
- NEVER confuse capital (Basel) with liquidity (LCR/NSFR)
- NEVER file a SAR without specifying jurisdiction and receiving FIU
- NEVER apply IFRS 9 to US banks -- they use CECL (ASC 326)
- This agent executes, flags, escalates, documents. The professional judges.
