# Exercise 6: AML Alert Review + SAR Drafting

## Scenario Profile

| Field               | Value                                          |
| ------------------- | ---------------------------------------------- |
| **Domain**          | AML / Financial Crime                          |
| **Jurisdiction**    | United Kingdom (NCA / POCA 2002)               |
| **Time Estimate**   | 45 minutes                                     |
| **Skills Required** | `aml-typologies`, `aml-sar-drafting`, `uk-pra` |

---

## Alert Data

You are a Level 2 AML analyst at a UK bank. Review the following 3 alerts from the transaction monitoring system and determine the appropriate disposition for each.

### Alert 1: Mohammed Al-Rashid -- Cash Structuring

| Field                      | Value                                            |
| -------------------------- | ------------------------------------------------ |
| **Customer**               | Mohammed Al-Rashid                               |
| **Account Type**           | Personal current account                         |
| **Customer Since**         | 2023                                             |
| **Declared Occupation**    | Restaurant owner                                 |
| **Declared Annual Income** | GBP 45,000                                       |
| **Alert Trigger**          | Multiple cash deposits below reporting threshold |

**Transaction History (past 30 days):**

| Date   | Type         | Amount GBP | Branch              |
| ------ | ------------ | ---------- | ------------------- |
| 1 Mar  | Cash deposit | 8,500      | Edgware Road        |
| 3 Mar  | Cash deposit | 7,800      | Marble Arch         |
| 7 Mar  | Cash deposit | 9,200      | Edgware Road        |
| 10 Mar | Cash deposit | 8,100      | Paddington          |
| 14 Mar | Wire out     | 28,000     | Online (to Lebanon) |
| 17 Mar | Cash deposit | 7,500      | Edgware Road        |
| 21 Mar | Cash deposit | 9,400      | Marble Arch         |
| 24 Mar | Wire out     | 22,000     | Online (to Lebanon) |

### Alert 2: Meridian Trading Ltd -- International Wires

| Field                        | Value                                                              |
| ---------------------------- | ------------------------------------------------------------------ |
| **Customer**                 | Meridian Trading Ltd                                               |
| **Account Type**             | Business current account                                           |
| **Customer Since**           | 2024                                                               |
| **Declared Business**        | Import/export of textiles                                          |
| **Declared Annual Turnover** | GBP 2.5M                                                           |
| **Directors**                | Two nominees (BVI-incorporated management company)                 |
| **Alert Trigger**            | High-value international wires inconsistent with declared business |

**Transaction History (past 60 days):**

| Date   | Type     | Amount GBP | Counterparty       | Country   |
| ------ | -------- | ---------- | ------------------ | --------- |
| 15 Jan | Wire in  | 450,000    | Zara Holdings      | Cyprus    |
| 18 Jan | Wire out | 425,000    | Eastern Star LLC   | Dubai     |
| 2 Feb  | Wire in  | 380,000    | Zara Holdings      | Cyprus    |
| 5 Feb  | Wire out | 370,000    | Caspian Imports    | Turkey    |
| 20 Feb | Wire in  | 520,000    | Pacific Ventures   | Hong Kong |
| 23 Feb | Wire out | 505,000    | Eastern Star LLC   | Dubai     |
| 10 Mar | Wire in  | 290,000    | Zara Holdings      | Cyprus    |
| 12 Mar | Wire out | 280,000    | Silk Route Trading | Pakistan  |

### Alert 3: Amara Diallo -- PEP

| Field                         | Value                                                            |
| ----------------------------- | ---------------------------------------------------------------- |
| **Customer**                  | Amara Diallo                                                     |
| **Account Type**              | Private banking                                                  |
| **Customer Since**            | 2021                                                             |
| **PEP Status**                | Tier 1 -- Former Minister of Finance, Senegal (left office 2020) |
| **Declared Source of Wealth** | Government salary, family business (agriculture)                 |
| **Alert Trigger**             | Large incoming transfer inconsistent with profile                |

**Transaction History (past 90 days):**

| Date   | Type     | Amount GBP | Source                              |
| ------ | -------- | ---------- | ----------------------------------- |
| 5 Jan  | Wire in  | 850,000    | Dakar Mining Corp (Senegal)         |
| 15 Jan | Wire out | 200,000    | Property solicitor (London)         |
| 1 Feb  | Wire in  | 425,000    | Unnamed account (Mauritius)         |
| 20 Feb | Wire out | 180,000    | Luxury car dealer (London)          |
| 5 Mar  | Wire in  | 1,200,000  | "Consultancy fees" (Cayman Islands) |

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The 3 alert data profiles (Mohammed Al-Rashid, Meridian Trading, Amara Diallo) above
- Skills active: `aml-typologies`, `aml-sar-drafting`, `uk-pra`
- Estimated time: 45 minutes

---

## Step-by-Step Instructions

### Step 1: Alert 1 Triage (10 min)

1. Identify the typology (structuring / smurfing)
2. Apply the alert disposition decision tree from Level 1 through Level 4
3. Calculate total suspicious cash deposits and outbound transfers
4. Assess whether the activity is consistent with the declared restaurant income

### Step 2: Alert 2 Investigation (10 min)

1. Identify the typologies (rapid fund movement / layering / TBML)
2. Note the red flags: nominee directors, BVI structure, consistent rapid in-out pattern
3. Assess whether declared textile business explains the transaction pattern
4. Determine disposition: close, escalate, or SAR

### Step 3: Alert 3 Assessment (10 min)

1. Note PEP status and apply EDD framework
2. Identify red flags: mining company payments inconsistent with declared agricultural wealth, Mauritius unnamed account, Cayman "consultancy fees"
3. Assess source of wealth vs. source of funds discrepancy
4. Determine disposition

### Step 4: SAR Drafting (15 min)

For the alert(s) that warrant a SAR, draft the SAR narrative following the UK format:

- Section 1: Subject of Disclosure
- Section 2: Grounds for Suspicion (most critical section)
- Section 3: The Suspicious Activity (timeline with amounts)
- Section 4: Account and Relationship Details
- Section 5: Prior Disclosures
  Apply the SAR quality checklist before submission.

---

## Deliverable

Produce: SAR narrative draft for NCA submission (UK format: Sections 1-5) for the alert(s) warranting a SAR, with typology classification and disposition decision for all 3 alerts.

---

## Key Learning

- Structuring is identified by multiple cash transactions just below the reporting threshold in a short period
- Layering through shell companies (BVI/Cyprus) with rapid fund movements is a classic ML typology
- PEP EDD requires understanding source of wealth (total net worth) not just source of funds (individual transactions)
- SAR quality depends on specific facts, dates, and amounts -- never use vague language like "large amounts" or "recently"
- The UK SAR standard is "reasonable grounds to suspect" (POCA 2002) -- it does not require certainty
