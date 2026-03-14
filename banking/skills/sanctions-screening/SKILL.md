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

## MAJOR SANCTIONS REGIMES

| Authority                  | Scope                                              | Key Lists                                                     |
| -------------------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| OFAC (USA)                 | Extraterritorial (USD transactions globally)       | SDN List; Consolidated Sanctions List; OFAC Country Sanctions |
| OFSI / HMT (UK)            | UK persons, UK-incorporated entities, UK territory | UK Consolidated Sanctions List                                |
| EU Council                 | EU persons, EU-incorporated entities, EU territory | EU Sanctions Map (CFSP)                                       |
| UN Security Council        | All UN member states                               | UN Consolidated List                                          |
| AUSTRAC / DFAT (Australia) | Australian persons, Australian territory           | DFAT Consolidated List                                        |

## OFAC SDN LIST — CRITICAL RULES

The OFAC Specially Designated Nationals (SDN) list is the most consequential
sanctions list globally due to OFAC's extraterritorial enforcement of USD transactions.

Rule: Any transaction involving an SDN — directly OR through a non-US financial
institution — is subject to US sanctions regardless of whether the transaction
touches US persons, US territory, or US infrastructure.

"50% Rule": An entity owned 50% or more (directly or indirectly) by an SDN is
itself treated as an SDN, even if the entity is not explicitly listed.
This rule requires looking through corporate structures to identify SDN ownership.

Penalties for OFAC violations: Civil penalties up to $1M per violation (or twice
the transaction amount, whichever is greater); criminal penalties for wilful
violations; debarment from US financial system (the "death penalty" for banks).

## UK SANCTIONS — OFSI / HMT

Office of Financial Sanctions Implementation (OFSI) administers UK sanctions.
UK Consolidated Sanctions List: includes all UN lists + UK-specific designations.
Post-Brexit: UK may designate individuals/entities not designated by EU (and vice versa).
Always screen against BOTH UK and EU lists for UK-connected counterparties.

OFSI monetary penalty: Up to £1M or 50% of estimated value of sanctioned activity,
whichever is greater. Strict liability (no intent required for civil penalty).
Reporting: Banks must report known/suspected sanctions violations to OFSI promptly.

## SCREENING PROCESS

### What Must Be Screened

Customers (at onboarding and periodically)
Beneficial owners and directors of corporate customers
All payment counterparties (sender and receiver in wire transfers)
Correspondent banks and their underlying customers (nested accounts)
Securities issuers (bond and equity investments)
Trade finance counterparties (importers, exporters, shipping companies)

### Screening Methodology

1. Name screening against all applicable lists
2. Fuzzy matching (typos, transliterations, partial names — common Arabic, Russian, Chinese names)
3. Date of birth, nationality, known aliases, passport numbers if available
4. Entity: registration number, jurisdiction, SWIFT BIC, IBAN

### False Positive Resolution

A false positive is a name match that is NOT actually a sanctioned individual/entity.
Resolution process:
a) Gather full identifying information from the match: DOB, nationality, address, ID
b) Compare against listed person's identifying information in full
c) Determine if match is the same person or a different person with similar name
d) If DIFFERENT person: document resolution clearly with differentiating evidence
e) If SAME or UNABLE TO DETERMINE: escalate to Sanctions Officer — do not release
the transaction

Documentation: Every false positive resolution must be documented.
Auditors will sample false positive resolutions — undocumented resolutions are
a finding equivalent to a missed sanction.

## SANCTIONS HIT — ESCALATION PROCEDURE

1. STOP the transaction / freeze the funds immediately
2. Notify the Sanctions Officer or MLRO immediately
3. Do NOT inform the customer that a sanctions match has been detected
   (may constitute a warning offence under UK/US law)
4. Gather all available information on the counterparty
5. Consult legal counsel (sanctions analysis is a legal determination)
6. If confirmed hit: freeze funds, report to OFAC/OFSI as required
7. Regulatory reporting deadline: promptly (varies by jurisdiction — check overlay)

## THE 50% RULE — OWNERSHIP SCREENING

Before clearing a counterparty that is NOT on a list:
Check: Is this entity ≥ 50% owned directly or indirectly by an SDN or listed entity?
If yes: treat as if the entity itself is listed.
Corporate registries, beneficial ownership databases (Refinitiv/LSEG, Dow Jones,
Moody's/Bureau van Dijk) support this analysis.

## CORRESPONDENT BANKING — NESTED ACCOUNT RISK

Risk: The respondent bank (foreign correspondent) holds accounts for its own
customers within the correspondent relationship. The host bank does not know
who the underlying customers are — "nested accounts."
Mitigation: FATF Recommendation 13 EDD for correspondent banking:
a) Understand respondent's AML programme quality
b) Assess respondent's sanctions compliance programme
c) Obtain written agreement that respondent will not allow nested accounts
without host bank's knowledge
d) Satisfy that respondent is not a shell bank

## DERISKING

Some banks have "derisk" certain respondent relationships (exit the relationship)
rather than manage the risk of unknown underlying customers.
FATF and the BCBS have issued guidance cautioning against blanket derisking
on a country or regional basis — this undermines financial inclusion.
Derisking should be: risk-based; documented; with individual assessment of
specific relationships rather than blanket country exits.

## NEVER DO THESE

- NEVER release a transaction without clearing a sanctions hit — even a probable false positive
- NEVER inform the customer about a sanctions screening (could be tip-off)
- NEVER rely solely on name matching without fuzzy-matching for transliterations
- NEVER omit the 50% ownership rule analysis for corporate counterparties
- NEVER assume a non-listed entity is clear without checking its ownership chain

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
