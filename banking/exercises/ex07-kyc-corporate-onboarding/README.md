# Exercise 7: KYC Corporate Onboarding

## Scenario Profile

| Field               | Value                                      |
| ------------------- | ------------------------------------------ |
| **Domain**          | KYC / Customer Due Diligence               |
| **Jurisdiction**    | United Kingdom (5MLD / MLRs 2017)          |
| **Time Estimate**   | 35 minutes                                 |
| **Skills Required** | `aml-cdd-edd`, `kyc-risk-rating`, `uk-pra` |

---

## Customer Data

You are a KYC analyst onboarding a new corporate customer for a UK-regulated bank.

### Entity: Azura Power Holdings Ltd

| Field                        | Value                                                             |
| ---------------------------- | ----------------------------------------------------------------- |
| **Registered Name**          | Azura Power Holdings Ltd                                          |
| **Jurisdiction**             | United Kingdom (Companies House)                                  |
| **Incorporation Date**       | 2019                                                              |
| **Registered Address**       | 45 Cheapside, London EC2V 6AX                                     |
| **Business Description**     | Holding company for power generation assets in sub-Saharan Africa |
| **Declared Annual Turnover** | GBP 85M                                                           |
| **Requested Product**        | GBP 50M revolving credit facility                                 |

### Corporate Structure

| Entity                          | Jurisdiction      | Ownership                      | Role                        |
| ------------------------------- | ----------------- | ------------------------------ | --------------------------- |
| Azura Power Holdings Ltd        | UK                | --                             | Customer entity             |
| Azura-Edo Power Ltd             | Nigeria           | 100% subsidiary                | 450MW gas-fired power plant |
| Azura Kenya Energy Ltd          | Kenya             | 80% subsidiary                 | 200MW solar project         |
| Azura Zambia Ltd                | Zambia            | 70% subsidiary                 | 150MW wind project          |
| Savannah Infrastructure PE Fund | Cayman Islands    | 35% shareholder of Azura Power | Private equity fund         |
| Blackstone Africa Fund II       | Delaware, USA     | 25% shareholder                | PE co-investor              |
| Ibrahim Okonkwo                 | Nigerian national | 22% shareholder (direct)       | Founder and CEO             |
| Fatima Okonkwo                  | Nigerian national | 18% shareholder (direct)       | Non-executive director      |

### PEP Flag

Ibrahim Okonkwo's father, Chief Emmanuel Okonkwo, served as Minister of Power and Steel, Federal Republic of Nigeria (2011-2015). Ibrahim is therefore a PEP family member (Tier 1 -- close associate of a foreign PEP).

---

## What You Need

- Banking plugin installed (`claude plugin install banking@agentfactory-business`)
- The Azura Power Holdings customer data and corporate structure tables above
- Skills active: `aml-cdd-edd`, `kyc-risk-rating`, `uk-pra`
- Estimated time: 35 minutes

---

## Step-by-Step Instructions

### Step 1: Identify Beneficial Owners (10 min)

1. Apply the 25% beneficial ownership threshold
2. Identify all UBOs who meet the threshold (direct + indirect)
3. For Savannah Infrastructure PE Fund (Cayman): what additional information is needed?
4. For Blackstone Africa Fund II: can SDD apply given it is a regulated entity?

### Step 2: Risk Rating (10 min)

Apply the four-dimension risk rating framework:

1. Customer type risk: holding company with offshore PE shareholders
2. Geographic risk: Nigeria, Kenya, Zambia, Cayman Islands
3. Product/service risk: GBP 50M revolving credit facility
4. Relationship/behavioural risk: new customer, PEP family member
   Calculate composite score and determine CDD level (Standard or Enhanced).

### Step 3: PEP EDD Requirements (10 min)

Given the PEP family member status:

1. Who must approve the relationship? (Senior management level)
2. What source of wealth documentation is required for Ibrahim Okonkwo?
3. How long does PEP status persist after Chief Okonkwo left office in 2015?
4. What enhanced ongoing monitoring must be applied?

### Step 4: Onboarding Decision (5 min)

1. Summarize the risk rating and EDD findings
2. Identify any blockers to onboarding
3. Draft the CDD file summary note for the compliance record

---

## Deliverable

Produce: KYC client profile document with beneficial ownership analysis, four-dimension risk rating scorecard, PEP EDD requirements checklist, and risk rating justification memo for the compliance record.

---

## Key Learning

- Beneficial ownership analysis requires looking through complex structures to natural persons
- Cayman-incorporated PE funds require additional BO disclosure since the register may be private
- PEP family member status triggers mandatory EDD regardless of the composite risk score
- Source of wealth for a PEP means understanding total net worth accumulation, not just the transaction
- The 25% threshold is the FATF standard but some jurisdictions (e.g., USA) use lower thresholds for certain entities
