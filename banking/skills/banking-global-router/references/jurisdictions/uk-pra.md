---
name: uk-pra
version: 1.0
description: >
  Jurisdiction overlay for United Kingdom — PRA (Prudential Regulation Authority)
  and FCA (Financial Conduct Authority). Applies to all UK-authorised banks and
  building societies for capital adequacy, IFRS 9 ECL, liquidity, and AML/KYC.
regulator_capital: Prudential Regulation Authority (PRA)
regulator_conduct: Financial Conduct Authority (FCA)
aml_regulator: FCA (financial sector) / NCA (suspicious activity reports)
accounting_standard: UK-adopted IFRS 9 (same as IASB IFRS 9)
capital_framework: UK CRR (retained EU CRR post-Brexit with UK modifications)
aml_legislation: Proceeds of Crime Act 2002 (POCA), Terrorism Act 2000, Money Laundering Regulations 2017 (as amended)
author: Panaversity — The AI Agent Factory
---

## IFRS 9 ECL — UK-SPECIFIC
Standard: UK-adopted IFRS 9 (identical to IASB IFRS 9 for impairment purposes)
Regulator: PRA supervises ECL models as part of SREP / model risk programme
PRA SS11/13 (Model Risk Management): applies to all IFRS 9 ECL models
PRA supervisory statement SS3/17: IFRS 9 and capital — interactions
Key disclosure requirement: IFRS 7 disclosures reviewed by PRA as part of Pillar 3 review

UK-specific ECL judgments:
- COVID-19 PMA: PRA issued guidance (Dear CEO letter 2020) on expected approach to PMAs
- Climate risk: PRA expects banks to incorporate climate risk in IFRS 9 scenarios (SS3/19)
- BoE climate scenarios: align IFRS 9 climate overlay with BoE CBES scenarios where applicable

## BASEL / CAPITAL — UK-SPECIFIC (UK CRR)
Minimum CET1: 4.5%
Capital Conservation Buffer: 2.5%
UK Countercyclical Buffer (UK CCyB): Check current rate at bankofengland.co.uk/financial-stability
  (was 0% during Covid, restored to 2.0% — always verify current rate)
UK Systemic Risk Buffer (UK SyRB): 0.0%–3.0% (set by PRA for individual D-SIBs)
PRA buffer (Pillar 2 guidance P2G): confidential; set per institution based on SREP

Effective minimum CET1 for large UK bank (illustrative):
  4.5% (minimum) + 2.5% (CCB) + 2.0% (UK CCyB) + 1.5% (UK SyRB) + P2R = ~11%+

Leverage ratio: UK Enhanced Leverage framework
  Minimum: 3.25% Tier 1 / Total Exposure
  Additional leverage ratio buffer: 0.35% (for major UK banks with >£50bn retail deposits)

UK CRR vs EU CRR3 differences post-Brexit:
  UK has NOT yet fully implemented Basel IV output floor (72.5% — consultation ongoing)
  UK SME supporting factor: retained in UK CRR (removed from EU CRR3)
  UK infrastructure supporting factor: retained in UK CRR

Annual Cyclical Scenario (ACS): BoE stress test scenario used in ICAAP
  Published annually by the Bank of England. Banks use BoE ACS as severe scenario.

## LIQUIDITY — UK-SPECIFIC
LCR: 100% minimum (same as Basel). UK CCyB may be released (LCR buffer released) in stress.
UK PRA Regulatory Liquidity Return: Daily (for major banks) / Monthly LCR reporting
NSFR: 100% minimum. UK PRA monitors NSFR through supervisory reporting.
ILAAP: Required annually. PRA uses ILAAP to set Pillar 2 liquidity guidance.

## AML / KYC — UK-SPECIFIC
Primary legislation: Proceeds of Crime Act 2002 (POCA); Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (MLRs 2017)
SAR filing: To National Crime Agency (NCA) via SARs Online platform
SAR standard: "Knows or suspects, or has reasonable grounds for knowing or suspecting"
Consent SAR (DAML): File with NCA; 7-day moratorium; NCA can extend to 31 days
Tipping-off prohibition: POCA 2002 s333A (criminal offence)
CDD requirements: MLRs 2017 regs 28–37 (broadly aligned with 4AMLD / 5AMLD)
PEP definition: MLRs 2017 Regulation 35 — domestic PEPs included (post-5AMLD implementation)
Reporting threshold for cash: no specific SAR threshold; all suspicious activity must be reported
Large cash: No general requirement to report all large cash; structured cash is suspicious
FCA Supervision: FCA oversees AML systems and controls for regulated firms; enforcement includes fines, restriction, withdrawal of authorisation

## CAPITAL-ECL INTERACTION — UK-SPECIFIC
IFRS 9 transitional arrangements: UK banks may apply transitional provisions (UK CRR Art 473a equivalent)
  Phase-in: 2018–2022 (completed). UK banks should now be fully loaded.
IRB shortfall/excess: UK CRR rules apply — excess provisions over IRB EL counted in T2 up to 0.6% of credit RWA
