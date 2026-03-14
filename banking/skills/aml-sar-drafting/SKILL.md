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

## SAR/STR OVERVIEW

A Suspicious Activity Report (SAR) or Suspicious Transaction Report (STR) is a
legally required filing made by a bank when it has the requisite suspicion of
money laundering, terrorist financing, or related predicate offences.

## JURISDICTION SAR STANDARDS

| Jurisdiction | Standard                                        | FIU                             | Filing System             |
| ------------ | ----------------------------------------------- | ------------------------------- | ------------------------- |
| UK           | Reasonable grounds to suspect                   | National Crime Agency (NCA)     | SARs Online               |
| USA          | Reason to suspect + USD 5,000 + legal violation | FinCEN                          | BSA E-Filing (FinCEN 111) |
| Australia    | Suspicion on reasonable grounds                 | AUSTRAC                         | AUSTRAC Online (SMR)      |
| EU           | Suspicion                                       | National FIU (per 6AMLD)        | National system           |
| UAE          | Reasonable grounds to suspect                   | UAE FIU                         | goAML                     |
| Pakistan     | Suspicion                                       | Financial Monitoring Unit (FMU) | goAML                     |

## UK SAR — DETAILED FORMAT REQUIREMENTS

### Section 1: Subject of Disclosure

- Full name (individual) or full registered name (corporate)
- Date of birth / incorporation date
- Current address / registered address
- National Insurance number / Companies House registration number
- Any aliases, trading names, related parties

### Section 2: Grounds for Suspicion

This is the most critical section. Must contain:
a) Description of the suspicious activity (who, what, when, amounts, frequency)
b) The specific typology or typologies identified
c) What is known about the customer's legitimate business
d) Why the activity is inconsistent with the legitimate business
e) What innocent explanation was considered and why it was found inadequate
f) Any steps taken to obtain further information

### Section 3: The Suspicious Activity

Timeline of suspicious transactions:

- Date, type, amount, counterparty, jurisdiction for each suspicious transaction
- Total suspicious amount over the suspicious period
- Supporting evidence available (wire confirmations, account statements)

### Section 4: Account and Relationship Details

- Account number(s) and product type
- Date account was opened
- How the business relationship was established (branch, online, introducer)
- KYC documentation on file

### Section 5: Prior Disclosures

- Has a prior SAR been filed on this customer?
- If yes: SAR reference number and date

### Section 6: Consent Requirement (UK only)

A "consent SAR" (Defence Against Money Laundering — DAML) is filed when
the bank wants to continue processing a specific transaction that it suspects
is money laundering, seeking consent from the NCA before proceeding.
If a DAML SAR is filed: the bank has a 7-day moratorium to await consent.
If no response in 7 days: deemed consent granted.
If the NCA grants consent or the moratorium expires: bank may proceed.

## SAR QUALITY STANDARDS — MANDATORY REQUIREMENTS

### Must Include

- Specific amounts (not "large amounts" — give the exact figures)
- Specific dates (not "recently" — give exact dates)
- Specific counterparties (full names, countries, account details if known)
- The specific reason for suspicion (which typology, why suspicious)
- The customer's explanation (if sought) and why it was insufficient
- What innocent explanation was considered and why eliminated

### Must NOT Include

- Conclusory statements ("we believe this is money laundering")
  The SAR reports facts and suspicion — the FIU makes the legal determination
- Speculation without factual basis
- Privileged legal advice
- Information from other customers' accounts not directly connected to the case
- The analyst's personal opinion about the customer's character

### The "Reasonable Grounds" Test (UK)

The test is OBJECTIVE: would a reasonable person, knowing the same facts,
have reasonable grounds to suspect money laundering?
It is NOT required to be CERTAIN it is money laundering.
It IS required that there are REASONABLE GROUNDS for the suspicion.
Mere unease or vague concern without factual basis does not meet the standard.

## TIPPING-OFF PROHIBITION

After a SAR/STR is filed, the bank MUST NOT disclose to the customer or any
connected party that a disclosure has been made.

UK: POCA 2002 s333A — criminal offence to tip off, maximum 5 years imprisonment
USA: Bank Secrecy Act — criminal offence, civil penalties
Australia: AML/CTF Act 2006 — criminal offence

### PERMISSIBLE after SAR filing:

- Continue normal business relationship (unless prohibited by consent SAR or other order)
- Respond to general compliance enquiries not related to the SAR
- Process unrelated transactions
- Request routine commercial information

### NOT PERMISSIBLE after SAR filing:

- Telling the customer a SAR has been filed
- Asking questions that could only relate to the SAR
- Closing the account immediately in a manner that signals the SAR to the customer
- Discussing the SAR with colleagues outside the need-to-know group

## SAR QUALITY CHECKLIST — BEFORE SUBMITTING FOR MLRO REVIEW

[ ] Customer identification complete and accurate
[ ] Suspicious period clearly defined (from date — to date)
[ ] Total amount of suspicious activity stated
[ ] Typology identified and explained in plain English
[ ] Customer's explanation included (if sought) and assessed
[ ] Innocent explanation considered and why eliminated
[ ] Prior SARs on this customer referenced
[ ] All transaction details (date, amount, type, counterparty) included
[ ] Consent SAR requirement considered (UK)
[ ] All factual statements supported by available evidence

## NEVER DO THESE

- NEVER include conclusory legal determinations in a SAR narrative — the SAR reports facts and suspicion; the FIU determines whether a criminal offence occurred
- NEVER disclose to the customer or any connected party that a SAR has been filed — tipping-off is a criminal offence (POCA 2002 s333A UK; BSA USA; AML/CTF Act 2006 Australia)
- NEVER use vague language in SAR narratives ("large amounts", "recently", "suspicious transactions") — every amount, date, and counterparty must be specific
- NEVER file a SAR without considering and documenting what innocent explanation was evaluated and why it was insufficient
- NEVER process a transaction subject to a UK consent SAR (DAML) during the 7-day moratorium period before NCA consent is received or deemed granted

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
