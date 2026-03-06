# Exercise 8: Sanctions Screening

## Scenario Profile

| Field               | Value                                     |
| ------------------- | ----------------------------------------- |
| **Domain**          | Sanctions Compliance                      |
| **Jurisdiction**    | UK / EU / OFAC                            |
| **Time Estimate**   | 40 minutes                                |
| **Skills Required** | `sanctions-screening`, `uk-pra`, `eu-crr` |

---

## Payment Data

You are a sanctions analyst reviewing 3 payments flagged by the automated screening system. For each payment, determine whether it is a true hit, false positive, or requires escalation.

### Payment 1: Ali Hassan Al-Farsi -- UAE Steel

| Field                | Value                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Originator**       | Ali Hassan Al-Farsi                                                                                                                                 |
| **Originator Bank**  | Emirates NBD, Dubai                                                                                                                                 |
| **Beneficiary**      | Sheffield Steel Supplies Ltd                                                                                                                        |
| **Beneficiary Bank** | Your bank (UK)                                                                                                                                      |
| **Amount**           | USD 425,000                                                                                                                                         |
| **Purpose**          | "Payment for steel rebar order #ST-2024-0847"                                                                                                       |
| **Screening Hit**    | Name match: "Ali Hassan" -- partial match to SDN entry "Ali Hassan al-Farsi" (Iranian national, designated for support of IRGC procurement network) |

SDN Entry Details:

- Full name: Ali Hassan al-Farsi
- Nationality: Iranian
- DOB: 12 March 1968
- Passport: Iranian passport W45892301
- Designation reason: Support for IRGC procurement of dual-use technology

Customer Information Available:

- Ali Hassan Al-Farsi (customer's counterparty): UAE national, DOB 5 September 1982, UAE passport A7823456
- Resident in Dubai since 2010, director of Al-Farsi Trading LLC (UAE registered)

### Payment 2: Zermatt Engineering AG -- Aerospace Parts

| Field                | Value                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Originator**       | Zermatt Engineering AG (Switzerland)                                                                                     |
| **Originator Bank**  | Credit Suisse, Zurich                                                                                                    |
| **Beneficiary**      | Rostec Aerospace Components Ltd                                                                                          |
| **Beneficiary Bank** | Intermediary request through your bank (UK)                                                                              |
| **Amount**           | EUR 1,850,000                                                                                                            |
| **Purpose**          | "Aerospace precision components -- contract ZE-2024-112"                                                                 |
| **Screening Hit**    | "Rostec" -- exact match to EU/UK sanctioned entity Rostec (Russian state corporation, designated under Russia sanctions) |

### Payment 3: Bosphorus Trading -- Correspondent Banking

| Field                 | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| **Originator**        | Bosphorus Trading Co. (Turkey)                               |
| **Originator Bank**   | Turkiye Is Bankasi, Istanbul                                 |
| **Intermediary Bank** | Your bank (UK) acting as correspondent                       |
| **Beneficiary**       | Parsian Trading House                                        |
| **Beneficiary Bank**  | Bank Saderat Iran, Tehran                                    |
| **Amount**            | EUR 380,000                                                  |
| **Purpose**           | "Food and medical supplies"                                  |
| **Screening Hit**     | "Bank Saderat Iran" -- OFAC SDN list; OFSI consolidated list |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The 3 payment data profiles (Ali Hassan Al-Farsi, Zermatt Engineering, Bosphorus Trading) above
- Skills active: `sanctions-screening`, `uk-pra`, `eu-crr`
- Estimated time: 40 minutes

---

## Step-by-Step Instructions

### Step 1: Payment 1 -- False Positive Analysis (10 min)

1. Compare the screening hit details (SDN entry) against available customer information
2. Identify differentiating factors: nationality, DOB, passport number
3. Document the false positive resolution with specific evidence
4. Determine: can this payment be released?

### Step 2: Payment 2 -- True Hit Assessment (10 min)

1. Confirm Rostec's designation status on EU and UK sanctions lists
2. Assess whether the payment can proceed under any licence or exemption
3. Determine required actions: block, freeze, report
4. Identify the regulatory reporting obligations (OFSI, EU NCA)
5. Apply the 50% rule: is Rostec Aerospace Components Ltd a subsidiary of designated Rostec?

### Step 3: Payment 3 -- Complex Correspondent Banking (10 min)

1. Identify all sanctions issues: Bank Saderat Iran (OFAC SDN, OFSI), Iran country sanctions
2. Assess the "food and medical" humanitarian exemption claim
3. Determine your bank's obligations as a UK correspondent bank processing this payment
4. Can the payment proceed under any humanitarian licence?
5. What are the OFAC secondary sanctions implications for your UK bank?

### Step 4: Documentation and Reporting (10 min)

For each payment:

1. Document the screening outcome (true hit, false positive, escalation)
2. Draft the regulatory notification where required
3. Complete the sanctions screening log entry

---

## Deliverable

Produce: Sanctions escalation memo to the MLRO covering all 3 payments with screening outcome (true hit, false positive, or escalation), specific differentiating evidence for false positives, regulatory notifications for true hits, and completed sanctions screening log entries.

---

## Key Learning

- False positive resolution requires specific differentiating evidence (DOB, nationality, passport), not just a judgment call
- Exact name matches to sanctioned entities must be blocked immediately pending investigation
- Bank Saderat Iran is designated under both OFAC and OFSI -- dual-regime exposure
- Humanitarian exemptions for Iran are narrow and require specific licensing (OFAC General License, OFSI licence)
- OFAC's extraterritorial reach means UK banks face secondary sanctions risk for Iran-connected payments even in non-USD currencies
- Every false positive resolution must be documented -- undocumented resolutions are treated as missed hits by auditors
