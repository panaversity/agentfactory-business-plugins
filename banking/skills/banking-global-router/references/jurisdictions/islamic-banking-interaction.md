---
name: islamic-banking-interaction
version: 1.0
description: >
  Interaction overlay for Islamic banking products with conventional banking
  regulation. Covers how Islamic finance products (murabaha, ijara, musharaka,
  mudaraba, istisna, salam) interact with IFRS 9 staging, Basel capital
  requirements, and AML/KYC frameworks. References AAOIFI FAS 30, IFSB standards,
  and jurisdiction-specific dual frameworks (Pakistan SBP, Malaysia BNM, UAE CBUAE).
standards:
  - AAOIFI FAS 30 (Impairment, Credit Losses, and Onerous Commitments)
  - AAOIFI FAS 28 (Murabaha and Other Deferred Payment Sales)
  - IFSB-15 (Revised Capital Adequacy Standard)
  - IFSB-12 (Guiding Principles on Liquidity Risk Management)
key_jurisdictions: Pakistan (SBP), Malaysia (BNM), UAE (CBUAE), Bahrain (CBB), Saudi Arabia (SAMA)
author: Panaversity — The AI Agent Factory
---

## IFRS 9 ECL AND ISLAMIC FINANCE PRODUCTS

Islamic finance products must be assessed for IFRS 9 staging despite their Sharia-compliant structure.

Murabaha (cost-plus sale):

- IFRS 9 classification: typically amortized cost (contractual cash flows are solely payments of principal and profit)
- Staging applies normally: assess SICR based on the counterparty's credit risk, not the product structure
- ECL calculation: PD x LGD x EAD framework applies. The profit element is part of the gross carrying amount
- Key difference: no interest rate — profit margin is fixed at inception. Discount rate for ECL uses the implicit rate in the murabaha contract

Ijara (lease):

- IFRS 9 applies to the receivable portion; IFRS 16 applies to the lease asset
- Staging: assess SICR on the lessee's credit risk
- Residual value risk is borne by the lessor (bank) in operating ijara — not covered by IFRS 9 ECL
- Ijara muntahia bittamleek (lease ending in ownership): ECL on the lease receivable, asset risk on the leased property

Musharaka / Mudaraba (partnership / profit-sharing):

- These are equity-like instruments under IFRS 9 — classification depends on contractual terms
- Diminishing musharaka: often classified at amortized cost if cash flows represent principal + profit
- Mudaraba: typically FVTPL (fair value through profit or loss) — no ECL calculation applies
- Key judgment: does the contract pass the SPPI (Solely Payments of Principal and Interest) test?

Istisna (manufacturing contract) and Salam (forward sale):

- Istisna: IFRS 9 ECL applies to progress billing receivables; staging based on contractor creditworthiness and project completion risk
- Salam: prepayment by bank for future delivery of goods; ECL applies to the bank's right to receive goods or cash equivalent
- Both assessed like trade finance receivables for counterparty default risk

## AAOIFI FAS 30 vs IFRS 9

AAOIFI FAS 30 (effective 2020) introduced an expected credit loss model for Islamic financial institutions:

| Dimension          | IFRS 9                                 | AAOIFI FAS 30                           |
| ------------------ | -------------------------------------- | --------------------------------------- |
| Staging            | 3-stage model                          | 3-stage model (aligned with IFRS 9)     |
| SICR assessment    | Required                               | Required (same principles)              |
| Measurement        | PD x LGD x EAD                         | PD x LGD x EAD (same formula)           |
| Scope              | All financial assets at amortized cost | Islamic financing assets + off-BS items |
| Profit recognition | EIR on gross (Stage 1/2)               | Profit on gross (Stage 1/2)             |
| Stage 3 income     | EIR on net carrying amount             | No profit on impaired assets (stricter) |
| Forward-looking    | Required (scenarios)                   | Required (scenarios)                    |
| PMA permitted      | Yes                                    | Yes (management overlay)                |

Key divergence: AAOIFI FAS 30 prohibits recognizing any profit on Stage 3 (credit-impaired) assets. IFRS 9 recognizes interest on the net carrying amount. This creates a P&L difference for Islamic banking windows applying both standards.

## DUAL FRAMEWORK JURISDICTIONS

Pakistan (State Bank of Pakistan — SBP):

- SBP requires Islamic banking institutions (IBIs) to apply BOTH AAOIFI standards AND IFRS 9
- SBP BPRD Circular No. 02 of 2021: IBIs must prepare IFRS 9-compliant financial statements AND AAOIFI-compliant Sharia disclosures
- Pakistan riba elimination deadline: Federal Shariat Court ruling requires elimination of riba from the banking system by 2028. SBP issued a framework for interest-free banking transition
- Impact on skills: ECL calculations must produce dual outputs — IFRS 9 for statutory reporting and AAOIFI FAS 30 for Sharia supervisory board

Malaysia (Bank Negara Malaysia — BNM):

- BNM operates a dual regulatory framework: Islamic Financial Services Act 2013 (IFSA) for Islamic banks, Financial Services Act 2013 (FSA) for conventional
- Malaysian Financial Reporting Standards (MFRS 9) = IFRS 9 applies to all banks, including Islamic
- AAOIFI standards are NOT mandatory in Malaysia — BNM uses its own Sharia Advisory Council rulings
- BNM Policy Document on Capital Adequacy Framework for Islamic Banks (CAFIB): adapts Basel III for Islamic products
- BNM liquidity: Islamic banks may use Sharia-compliant HQLA (sukuk, Islamic money market instruments) for LCR

UAE (CBUAE):

- CBUAE allows both IFRS 9 and AAOIFI for Islamic banks and Islamic banking windows
- In practice, most UAE Islamic banks apply IFRS 9 for financial reporting and AAOIFI for Sharia governance
- CBUAE Islamic banking regulation: Standard RE-6/2020 (Islamic banking business)
- UAE Federal Law No. 14 of 2018: permits Islamic banking windows within conventional banks

Bahrain (CBB):

- CBB mandates AAOIFI for all Islamic banks licensed in Bahrain (CBB Rulebook Volume 2)
- IFRS 9 does NOT directly apply to Bahrain Islamic banks — AAOIFI FAS 30 is the primary standard
- Conventional banks in Bahrain follow IFRS 9 (CBB Rulebook Volume 1)
- Dual-licensed institutions must reconcile between the two frameworks

## BASEL CAPITAL FOR ISLAMIC BANKS

IFSB-15 (Revised Capital Adequacy Standard for Islamic banks):

- Adapts Basel III for Islamic banking: defines eligible capital instruments (sukuk-based AT1 and T2)
- Risk-weighted assets: same risk weight categories as Basel III SA, applied to Islamic finance exposures
- Profit-sharing investment accounts (PSIA): alpha factor determines how much of PSIA risk is borne by the bank vs depositors
- Displaced commercial risk (DCR): banks may absorb losses that should be borne by PSIA holders to remain competitive — this creates an additional capital charge

Key capital differences:

- Murabaha receivables: risk-weighted as corporate/retail exposures (same as conventional loans)
- Ijara assets: risk-weighted based on the underlying asset and counterparty risk
- Musharaka / equity investments: 100-400% risk weight depending on listing and nature
- Sukuk held as investments: risk-weighted based on issuer credit rating (same as conventional bonds)

## AML / KYC FOR ISLAMIC BANKING

Islamic banking products do not change AML/KYC obligations:

- All CDD, EDD, PEP, and SAR/STR obligations apply identically regardless of product structure
- Hawala/hawalat: regulated as money services businesses in all GCC jurisdictions
- Zakat, waqf, and Islamic charity accounts: must comply with source of funds verification and enhanced CFT scrutiny (FATF Recommendation 8)
