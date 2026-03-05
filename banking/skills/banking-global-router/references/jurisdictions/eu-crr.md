---
name: eu-crr
version: 1.0
description: >
  Jurisdiction overlay for European Union — ECB (Single Supervisory Mechanism for
  significant institutions), national regulators (for less significant institutions).
  Covers EU CRR3 (implementing Basel IV), IFRS 9 ECL under EU-adopted IFRS,
  EU 6AMLD, and FRTB implementation.
regulator_capital: ECB (SSM significant institutions); national NCAs for less significant
regulator_conduct: EBA (European Banking Authority) — sets binding technical standards
aml_regulator: National FIUs; EBA (AML/CFT coordination)
accounting_standard: EU-adopted IFRS 9 (carve-outs for macro hedging)
capital_framework: CRR3 (Capital Requirements Regulation 3, implementing Basel IV)
aml_legislation: 6th Anti-Money Laundering Directive (6AMLD); EU AML Regulation (forthcoming)
author: Panaversity — The AI Agent Factory
---

## IFRS 9 ECL — EU-SPECIFIC
Standard: EU-adopted IFRS 9 — largely identical to IASB IFRS 9 with minor carve-outs
ECB guidance: ECB guidance on ECL models (2017, updated guidance ongoing)
EBA guidelines: EBA/GL/2017/06 — Credit institutions' credit risk management practices and ECL

EU-specific ECL features:
- EBA NPL (non-performing loan) guidelines: more prescriptive NPL definition criteria
- EBA backstop regulation (Pillar 1 backstop): for NPLs, progressive provision coverage
  requirements irrespective of IFRS 9 outcomes (creates binding floor on provisions for NPLs)
  NPL vintage 0–2 years: 35% unsecured / 25% secured coverage minimum
  NPL vintage 2–7 years: 100% unsecured / variable secured coverage
  This backstop is IN ADDITION TO IFRS 9 ECL — apply whichever gives higher provision

## CAPITAL — EU CRR3
CRR3 implements Basel IV reforms in EU, phased from January 2025.
CET1 minimum: 4.5% | T1: 6.0% | TC: 8.0% | Leverage: 3.0%
Combined buffer: CCB 2.5% + CCyB (jurisdiction and institution-specific)
O-SII (Other Systemically Important Institution) buffer: 0–3% (national discretion)
G-SII buffer: 1–3.5% (FSB-designated global systemic banks)

Output floor: CRR3 implements 72.5% output floor with 2025–2030 phase-in:
  2025: 50%; 2026: 55%; 2027: 60%; 2028: 65%; 2029: 70%; 2030: 72.5% (full)

FRTB: CRR3 mandates FRTB SA from January 2025; IMA subject to regulator approval.

SME supporting factor: REMOVED from CRR3 for most SME exposures (divergence from UK).

EBA stress test: EBA conducts EU-wide stress test biannually.
  Participating banks submit capital depletion path under EBA adverse scenario.
  Results published — markets track CET1 ratios at end of stress horizon.

## AML — EU 6AMLD / EU AML PACKAGE
6AMLD (implemented by member states): harmonised list of 22 predicate offences
EU AML Authority (AMLA): new EU supervisory body for cross-border AML (from 2025)
EU AML Regulation (AMLR): directly applicable regulation (no national implementation needed)
SAR filing: to national FIU (FIU.net interconnects EU FIUs for cross-border information sharing)
PEP: 4AMLD/5AMLD PEP definition — domestic PEPs included
Beneficial ownership: EU 4AMLD/5AMLD — BO registers in each member state
  Central BO registers must be publicly accessible (CJEU ruling complicated this)

## LIQUIDITY — EU
LCR: Delegated Regulation 2015/61. Level 2B assets included (national discretion mostly aligned).
NSFR: CRR2 mandated NSFR from June 2021. 100% minimum.
ECB LCR monitoring: SSM banks report LCR daily to ECB.
