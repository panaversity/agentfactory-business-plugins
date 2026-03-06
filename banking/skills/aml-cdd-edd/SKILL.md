---
name: aml-cdd-edd
version: 1.0
description: >
  Activate for: CDD, EDD, customer due diligence, enhanced due diligence,
  simplified due diligence, KYC, know your customer, customer onboarding,
  source of wealth, source of funds, PEP, politically exposed person,
  beneficial ownership, UBO, corporate structure, ongoing monitoring.
  NOT for: personal finance advice or retail banking product recommendations,
  tax compliance or tax residency determinations, credit underwriting decisions.
standard: FATF Recommendation 10 (CDD), 12 (PEPs), 13 (Correspondent Banking)
author: Panaversity — The AI Agent Factory
---

## CUSTOMER DUE DILIGENCE (CDD) — STANDARD MEASURES

Required for all customers at account opening:

1. Identify the customer — obtain identifying information
2. Verify the customer's identity — using reliable, independent source documents
3. Identify the beneficial owner (BO) — persons owning or controlling ≥ 25% (or lower)
4. Verify the beneficial owner's identity
5. Understand the nature and purpose of the business relationship
6. Conduct ongoing monitoring of the relationship

### Individual Customer Identity Verification

Documents (in order of reliability):
Tier 1 (highest): Passport; national ID card; government-issued photo ID
Tier 2: Driving licence; residence permit
Address verification: Utility bill, bank statement, government correspondence
(must be dated within 3 months)
For non-face-to-face onboarding: certified copies; electronic verification;
video identification (where jurisdiction permits).

### Corporate Customer Identity Verification

Company: Certificate of incorporation; memorandum and articles of association;
latest audited accounts; register of directors; register of shareholders
Beneficial owner: Identify all individuals owning or controlling ≥ 25%
(FATF threshold — some jurisdictions use lower: 10% in USA for certain entities)
Director verification: Verify identity of all directors with day-to-day control
Authorised signatories: Verify identity of all authorised signatories

### Understanding Business Purpose

Document: Nature of business; anticipated transaction types, volumes, and values;
source of funds for specific transactions; geographic profile of activity.
Risk-proportionate: More detail required for higher-risk customers and products.

## POLITICALLY EXPOSED PERSONS (PEPs) — ENHANCED DUE DILIGENCE

### PEP Definition (FATF Recommendation 12)

Individuals entrusted with prominent public functions:

- Heads of state, heads of government, senior politicians
- Senior government officials, judicial or military officials
- Senior executives of state-owned enterprises
- Senior officials of political parties

### PEP Classifications

Tier 1 — Foreign PEP: Individual holding prominent function in foreign country.
Mandatory EDD under FATF. Highest risk.
Tier 2 — Domestic PEP: Individual holding prominent function in the bank's home country.
EDD required under 5AMLD (EU) and most jurisdictions. Moderate-high risk.
Tier 3 — International Organisation PEP: Senior officials of international organisations.
EDD required under 5AMLD. Moderate risk.
Family members and close associates: Treated as PEPs for EDD purposes.

### Duration of PEP Status

PEP status does not automatically end when the individual leaves office.
FATF guidance: risk-based approach — senior positions warrant longer post-tenure treatment.
Minimum: 12-month post-tenure review period.
Best practice for senior officials (heads of state, senior ministers): 2–5 years.
Bank must document why the individual's risk has reduced to non-PEP level before
downgrading their status.

### PEP EDD Requirements

a) Senior management approval (minimum: Head of Business, often CRO level)
b) Source of wealth — understand how the individual accumulated their wealth
(not just source of funds for this transaction)
c) Source of funds — specific source of funds for this relationship/transactions
d) Enhanced ongoing monitoring — more frequent and more detailed transaction review
e) Annual or more frequent risk review of the relationship

### Source of Wealth vs. Source of Funds

Source of wealth: How did this person accumulate their total net worth?
Evidence: Business ownership documents; pay slips; investment records;
inheritance documentation; property sales; prior wealth disclosures.
Source of funds: Where do the specific funds entering this account come from?
Evidence: Bank transfer confirmations; investment sale proceeds; salary receipts.
Both are required for PEPs and high-risk customers. Vague assertions ("business
income") without documentary evidence are NOT sufficient for EDD.

## ENHANCED DUE DILIGENCE (EDD) — HIGH RISK CUSTOMERS

### Triggers for EDD

- PEP status (mandatory)
- High-risk jurisdiction (FATF grey/black list, high TI Corruption Perceptions Index)
- Complex corporate structure (offshore holding company, nominee directors)
- High-value or complex transactions inconsistent with declared profile
- Adverse media or negative information during screening
- Non-face-to-face onboarding for high-value relationships
- Correspondent banking (FATF Rec 13 — specific requirements)

### EDD Process

1. Gather more detailed information (source of wealth, source of funds, BO structure)
2. Verify information using independent sources (not just what customer provides)
3. Senior management sign-off (written approval, documented)
4. Enhanced ongoing monitoring (more frequent transaction reviews, lower alert thresholds)
5. Annual EDD refresh (minimum) — re-verify key information

## SIMPLIFIED DUE DILIGENCE (SDD)

Permitted in limited circumstances where risk is demonstrably low:

- Listed companies on regulated markets (public ownership = transparency)
- Government entities (inherently low money laundering risk)
- Supervised financial institutions (subject to AML regulation themselves)
  Do NOT apply SDD automatically — must assess risk and document justification.
  SDD does NOT eliminate the need for ongoing monitoring.

## ONGOING MONITORING

All customer relationships require ongoing monitoring:

- Transaction monitoring (automated TM system — see aml-typologies.md)
- Periodic KYC refresh (frequency based on risk rating):
  High risk: annual or more frequent
  Medium risk: every 2–3 years
  Low risk: every 3–5 years
- Trigger-based refresh: adverse media, change in ownership, change in business,
  large unusual transaction, law enforcement contact

## BENEFICIAL OWNERSHIP — COMPLEX STRUCTURES

### The Look-Through Principle

For complex corporate structures (holding companies, trusts, foundations):
Look through the corporate layers until you identify the natural person(s) who
ultimately own or control the customer entity.

- Ownership: direct + indirect shareholdings aggregated ≥ 25%
- Control: right to appoint/remove majority of directors; shareholder agreement
  giving effective control below 25% formal threshold

### Offshore / Secrecy Jurisdictions

Cayman Islands, BVI, Panama, Isle of Man, Jersey, Guernsey: register of members
may be private. The bank must still obtain BO information.
Options: Obtain certified copy of private register from registered agent;
obtain written declaration from customer with supporting documentation;
where documentation cannot be obtained: CANNOT onboard or must apply
enhanced risk mitigation with documented rationale.

### Trust Structures

Identify: Settlor; trustee(s); protector(s); beneficiaries (or class of beneficiaries).
Verify: Identity of all controlling parties and beneficial owners of > 25%.

## NEVER DO THESE

- NEVER approve SDD without a documented risk assessment — SDD is not the default, it requires demonstrable low risk
- NEVER accept "business income" as sufficient source of wealth evidence for PEPs — documentary evidence of how wealth was accumulated is mandatory
- NEVER onboard a customer when beneficial ownership cannot be established through the full corporate chain — if BO is opaque, the relationship must be declined or escalated to senior management with documented enhanced risk mitigation
- NEVER downgrade a PEP's risk status immediately upon leaving office — a minimum 12-month post-tenure review period is required, and senior officials require 2-5 years
- NEVER treat CDD as a one-time onboarding event — ongoing monitoring and periodic refresh (frequency per risk rating) are mandatory for the life of the relationship

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
