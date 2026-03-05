---
name: pakistan-sbp
version: 1.0
description: >
  Jurisdiction overlay for Pakistan — SBP (State Bank of Pakistan) for banking
  regulation, capital, and liquidity; FMU (Financial Monitoring Unit) for AML.
  Note: Pakistan is implementing full conversion to Islamic banking by 2028
  per Federal Shariat Court ruling — see Islamic finance overlay for Shariah compliance.
regulator: State Bank of Pakistan (SBP)
aml_regulator: Financial Monitoring Unit (FMU Pakistan)
accounting_standard: IFRS 9 (applicable to listed companies / banking companies)
capital_framework: SBP BPRD Circular — Basel III implementation
aml_legislation: Anti-Money Laundering Act 2010 (AMLA); Proceeds of Crime Act 2010
author: Panaversity — The AI Agent Factory
---

## IFRS 9 ECL — PAKISTAN
IFRS 9 adopted for banking companies per SBP directive (phased implementation).
IFRS 9 mandatory for all scheduled banks from accounting year beginning January 2024.
SBP PRs (Prudential Regulations) for consumer finance and corporate banking set
  minimum provisioning requirements — apply the HIGHER of IFRS 9 ECL and SBP PRs.

SBP Prudential Regulations minimum provisions:
  Substandard (90–180 DPD): 25% specific provision
  Doubtful (180–365 DPD): 50% specific provision
  Loss (>365 DPD): 100% specific provision
Where SBP PRs require higher provision than IFRS 9 ECL: apply SBP PRs.
This creates a "floor" on Stage 3 provisions for Pakistan-regulated banks.

## CAPITAL — SBP BASEL III
Minimum CET1: 6.0% (SBP maintains higher than Basel 4.5%)
Minimum T1: 7.5%
Minimum TC: 10.0%
Capital Conservation Buffer: 2.5%
Countercyclical Buffer: 0% (SBP has not activated this buffer to date)
D-SIB surcharge: Not yet formally implemented (SBP consulting)

Leverage ratio: 3.0% (Basel minimum; SBP implementing)

SBP Basel IV: Pakistan adopting Basel IV framework through updated prudential regulations.
  Check SBP website (sbp.org.pk) for current circular references.

## LIQUIDITY — SBP
LCR: SBP implemented LCR for larger banks. 100% minimum.
  Pakistan Government Securities (T-Bills, PIBs) qualify as Level 1 HQLA.
  SBP reverse repos with government securities: Level 1 HQLA treatment.
NSFR: SBP implementing — check current status.
SLR (Statutory Liquidity Requirement): Pakistan maintains SLR in addition to LCR.
  Banks must hold minimum % of demand liabilities in liquid assets (T-Bills, T-Bonds, SBP instruments).
  Current SLR: check SBP website (changes periodically).

## AML — PAKISTAN FMU / AMLA 2010
Anti-Money Laundering Act 2010: primary legislation
Financial Monitoring Unit (FMU): national FIU for Pakistan
  STR/SAR filing: goAML portal (same as UAE and Singapore)
  Filing standard: suspicious or reasonable grounds to suspect
  Threshold reporting: cash transactions above PKR 500,000 equivalent (check current threshold)

FATF status: Pakistan was on FATF grey list 2018–2022; removed in October 2022.
  Post-grey list, Pakistan must demonstrate continued AML/CFT effectiveness.
  SBP AML/CFT regulations: updated following FATF action plan requirements.

SBP AML/CFT regulations for banks: SBP BPRD Circular (updated) — covers CDD/EDD,
  ongoing monitoring, correspondent banking, wire transfer rules.
Customer risk rating: risk-based approach required per SBP regulations.

## ISLAMIC BANKING — RIBA CONVERSION MANDATE
Federal Shariat Court April 2022 ruling: riba (interest) unconstitutional.
Full conversion of banking system to Islamic finance: mandated by January 2028.
Impact: conventional banks must establish Islamic subsidiaries or convert fully.
SBP Shariah Governance Framework (SGF, revised 2024): governs Islamic banking operations.
For Islamic banking entities in Pakistan: ALSO load islamic-finance-global-router.md
  and jurisdictions/pakistan-sbp.md from the Islamic Finance skills library.
