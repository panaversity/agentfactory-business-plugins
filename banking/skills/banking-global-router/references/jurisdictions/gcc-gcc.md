---
name: gcc-gcc
version: 1.0
description: >
  Jurisdiction overlay for the Gulf Cooperation Council (GCC) — covering SAMA
  (Saudi Arabia), CBUAE (UAE), CBB (Bahrain), CBK (Kuwait), QCB (Qatar), and
  CBO (Oman). Applies to capital adequacy, IFRS 9 ECL, liquidity, and AML/KYC
  for banks operating across the GCC region.
jurisdiction: GCC (Saudi Arabia, UAE, Bahrain, Kuwait, Qatar, Oman)
regulators:
  saudi_arabia: Saudi Central Bank (SAMA)
  uae: Central Bank of the UAE (CBUAE)
  bahrain: Central Bank of Bahrain (CBB)
  kuwait: Central Bank of Kuwait (CBK)
  qatar: Qatar Central Bank (QCB)
  oman: Central Bank of Oman (CBO)
accounting_standard: IFRS 9 (adopted across all GCC states)
capital_framework: Basel III (all GCC central banks are BCBS members or observers)
aml_framework: FATF recommendations via MENAFATF (Middle East and North Africa FATF)
author: Panaversity — The AI Agent Factory
---

## IFRS 9 ECL — GCC-SPECIFIC

All six GCC states have adopted IFRS 9 as their accounting standard for financial instruments.

Key regional considerations:

- SAMA: Full IFRS 9 adoption effective 1 January 2018. SAMA issued Circular No. 381000064902 requiring banks to apply IFRS 9 ECL with forward-looking macroeconomic scenarios
- CBUAE: IFRS 9 mandatory from 2018. CBUAE issued Guidance on IFRS 9 ECL (2018) requiring banks to incorporate UAE-specific macro variables (non-oil GDP, real estate index, oil price)
- CBB: IFRS 9 adopted 2018. Islamic banks must reconcile AAOIFI FAS 30 impairment with IFRS 9 staging
- CBK: IFRS 9 adopted 2018. CBK mandates a minimum general provision of 1% on cash facilities and 0.5% on non-cash facilities — applied as a floor even when IFRS 9 ECL is lower
- QCB: IFRS 9 adopted 2018. QCB requires banks to maintain a minimum risk reserve of 2.5% of gross loans

GCC-specific ECL drivers:

- Oil price sensitivity: GCC economies are heavily oil-dependent; ECL scenarios must include oil price paths
- Real estate cycles: Dubai/Abu Dhabi property cycles create significant Stage 2 migration risk for CRE portfolios
- Government-related entities (GREs): GCC banks hold large exposures to sovereign-linked entities; staging these requires sovereign risk assessment
- Expatriate workforce concentration: Retail portfolios in UAE/Qatar/Bahrain have high expatriate share, creating abscondment risk unique to the region

## BASEL / CAPITAL — GCC-SPECIFIC

SAMA (Saudi Arabia):

- Minimum CET1: 4.5% + CCB 2.5% = 7.0%
- SAMA applies a D-SIB surcharge of 0.5%-1.5% for systemically important Saudi banks
- Saudi banks must also meet SAMA's capital adequacy ratio (CAR) of minimum 8% (Total Capital / RWA)
- Leverage ratio: 3% minimum (Basel standard)

CBUAE (UAE):

- Minimum CET1: 7.0% (higher than Basel minimum)
- Total CAR minimum: 10.5% (including CCB)
- CBUAE ECL floor: if IFRS 9 ECL < 1.5% of credit RWA, additional provision required
- D-SIB buffer: up to 1.5% for UAE systemically important banks

CBB (Bahrain):

- Minimum CET1: 6.5% (CBB Volume 1 CA-2)
- Total CAR: 12.5% minimum (one of the highest in GCC)
- CCB: 2.5%. CBB does not apply a countercyclical buffer

CBK (Kuwait):

- CET1 minimum: 4.5% + CCB 2.5%
- Total CAR: minimum 13% (Kuwait maintains the highest capital floor in the GCC)
- CBK also applies a profit-sharing ratio floor for Islamic banks

QCB (Qatar):

- CET1: 6.0% minimum
- Total CAR: 10.0% minimum
- QCB has designated 4 D-SIBs with additional capital surcharges

## LIQUIDITY — GCC-SPECIFIC

- All GCC central banks have implemented the LCR (100% minimum) and NSFR (100% minimum)
- SAMA: LCR reporting is monthly; NSFR is quarterly. SAMA has implemented a Net Stable Funding Amount (NSFA) metric in addition to the ratio
- CBUAE: Eligible Liquid Assets Ratio (ELAR) of 10% applies alongside the LCR for UAE banks not yet on full LCR reporting
- CBB: LCR 100% minimum. CBB additionally requires a liquidity ratio of 25% of customer deposits for retail banks
- GCC-specific liquidity risk: high deposit concentration from government entities and GREs creates volatility in the stable funding base

## AML / KYC — GCC-SPECIFIC

FATF / MENAFATF status:

- UAE: Removed from FATF grey list (February 2024) after strengthening AML/CFT framework. UAE now under regular follow-up
- Saudi Arabia: FATF member since June 2019. Saudi Anti-Money Laundering Law (Royal Decree M/20, 2003, amended 2017)
- Bahrain: FATF mutual evaluation (2018); largely compliant. CBB AML/CFT module (FC module)
- Kuwait: FATF mutual evaluation (2019); enhanced follow-up for strategic deficiencies in beneficial ownership transparency
- Qatar: FATF mutual evaluation (2019); largely compliant

Key GCC AML features:

- All GCC states have FIU (Financial Intelligence Unit) structures, but reporting formats and thresholds differ by jurisdiction
- UAE: goAML platform for SAR/STR filing. AML Federal Law No. 20 of 2018 (amended by Decree-Law No. 26 of 2021)
- SAMA: SAR filing via SAMA AML/CFT portal. Mandatory reporting threshold for cash transactions >= SAR 60,000 (~USD 16,000)
- PEP definitions: GCC states broadly align with FATF definition; domestic PEPs included in CDD requirements since 2020 reforms
- Hawala and informal value transfer: GCC regulators require registration and monitoring of hawala/hawalat operators under AML frameworks

## RECENT REGULATORY DEVELOPMENTS

- SAMA Vision 2030 alignment: SAMA is strengthening open banking and fintech regulation, impacting KYC digital onboarding
- CBUAE Basel III Final Reforms: CBUAE issued implementation timeline for Basel IV output floor (phased 2025-2028)
- UAE CBUAE Targeted Financial Sanctions (TFS): enhanced sanctions screening requirements post-FATF grey list exit
- GCC harmonization: GCC central bank governors announced roadmap for regional regulatory convergence on Basel III and AML standards (2024)
- Islamic banking growth: Islamic banking assets exceed 25% of total banking assets across the GCC, requiring parallel AAOIFI and IFRS compliance
