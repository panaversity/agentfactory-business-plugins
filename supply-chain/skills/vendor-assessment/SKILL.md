---
name: vendor-assessment
description: >
  Activate for: vendor assessment, vendor review, supplier assessment,
  vendor onboarding, new vendor approval, vendor audit, annual vendor review,
  vendor scorecard, supplier evaluation, vendor qualification, approve vendor,
  vendor due diligence, vendor health check, vendor performance review,
  vendor classification, strategic supplier, bottleneck supplier, vendor exit,
  Kraljic matrix, vendor tier.
  NOT for: invoice reconciliation (use invoice-reconciliation), carrier
  performance review (use logistics-brief), spend category analysis
  (use spend-analysis).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/vendor-assess"
  mcp-integrations: "ERP, Web Search, Companies House, Creditsafe, QMS"
---

## UNIVERSAL RULES (apply to every vendor task)

- NEVER classify a sole-source supplier as low risk based on spend alone --
  always assess operational dependency separately from spend volume
- NEVER accept a vendor risk assessment that contains fabricated financial
  data -- label all estimates and flag where primary data is unavailable
- NEVER recommend a vendor exit without a qualified alternative identified
  or an explicit "no alternative -- managed risk" decision documented
- ALWAYS include specific recommended actions with deadlines in every output --
  observations without actions are not acceptable

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          [e.g. Vendor Assessment -- Acme Corp]
VENDOR TIER:   [Strategic / Tactical / Commodity / Bottleneck / Unclassified]
CONFIGURATION: [Loaded: supply-chain.local.md / Not configured]
DATA SOURCES:  [ERP / Web / Manual input]
```

## ASSESSMENT WORKFLOW

### Phase 1: Vendor Classification (Kraljic Matrix)

Before any assessment, classify the vendor:

| Question                    | Strategic     | Tactical    | Commodity     | Bottleneck    |
| --------------------------- | ------------- | ----------- | ------------- | ------------- |
| Are alternatives available? | No / very few | Yes -- 2-3  | Many          | No / very few |
| Annual spend?               | High          | Medium      | Any           | Low-Medium    |
| Impact if vendor fails?     | Critical      | Significant | Manageable    | Critical      |
| Relationship depth?         | Deep / long   | Established | Transactional | Variable      |

STRATEGIC (Tier 1): High spend AND high dependency. Single-source or near-sole-source. Review: quarterly + event-triggered.
TACTICAL (Tier 2): Significant spend. Multiple alternatives available. Review: bi-annual + event-triggered.
COMMODITY (Tier 3): Standard goods/services. Easy to switch. Review: annual.
BOTTLENECK (Tier 4): LOW spend but HIGH dependency. MOST DANGEROUS -- most often neglected. Review: quarterly despite low spend.

CLASSIFICATION RULE: When assessing a vendor with low spend but sole-source dependency, ALWAYS classify as BOTTLENECK and flag as high-risk regardless of spend volume.

CLASSIFICATION DETERMINES:

- Assessment depth (number of dimensions assessed)
- Review frequency
- Risk threshold stringency
- Escalation level

### Phase 2: Six-Dimension Assessment

DIMENSION 1: COMMERCIAL
Contract status:

- Active contract: Yes/No; expiry date; auto-renewal clause?
- Notice period for non-renewal: documented?
- Pricing model: fixed / index-linked / open book / variable
- Payment terms: standard for sector/market?
- Volume commitments: minimum order quantities; penalty clauses?
- IP ownership: critical for manufactured-to-spec components

Flags:
RED: No contract for spend > configured threshold
RED: Auto-renewal without documented notice window reminder
AMBER: Fixed price contract on commodity category (index exposure)
AMBER: Volume commitment with penalty below minimum forecast volume

DIMENSION 2: OPERATIONAL
Metrics from ERP (last 12 months):

- On-time delivery rate (OTD): calculate from GR dates vs. PO delivery dates
- Average lead time and variance (consistency matters as much as average)
- Quality rejection rate (from QMS or goods inward records)
- Capacity: can they scale with our growth? (ask directly)
- Business continuity: single site or multiple?

Flags:
RED: OTD < configured threshold for tier (e.g. <90% for Strategic)
RED: Quality rejection > configured threshold (e.g. >2% for direct materials)
AMBER: OTD declining trend (even if above threshold -- trajectory matters)
AMBER: Single production site with no documented BCP

DIMENSION 3: FINANCIAL
For publicly listed vendors:

- Revenue trend (last 3 years): growing / stable / declining
- Profitability trend: EBIT margin trajectory
- Debt to equity ratio: deteriorating?
- Days Sales Outstanding (DSO): lengthening = cash pressure
- Analyst commentary (if listed): any concerns raised?

For private vendors:

- Companies House / SECP / equivalent filings (annual accounts)
- Credit rating from Creditsafe / D&B / Experian
- Request audited accounts for Strategic and Bottleneck vendors annually
- Trade references from other customers (for new vendors)

Flags:
RED: Restructuring, administration, or insolvency proceedings
RED: Zero financial visibility on Strategic or Bottleneck vendor
AMBER: Revenue decline >15% year-on-year
AMBER: Credit rating downgrade
AMBER: EBIT margin below 3% (marginal viability risk)

DIMENSION 4: COMPLIANCE
Certifications required (configure by category in local settings):

- Quality: ISO 9001 / sector-specific (IATF 16949 for automotive, etc.)
- Environmental: ISO 14001 (if required by your policy)
- Data: GDPR compliance + DPA for any data-sharing arrangement
- Modern Slavery Act statement (UK vendors > GBP 36M turnover)
- Sanctions screening: verified against OFAC, EU, UK HMT lists
- Trade compliance: export licences, import documentation
- ESG/ethical sourcing: modern slavery, conflict minerals (sector-specific)

Flags:
RED: Active sanctions match -- immediate escalation; stop all activity
RED: Required certification expired with no renewal in progress
AMBER: Certification expiring within 90 days -- request renewal evidence
AMBER: No modern slavery statement (UK statutory requirement above threshold)

DIMENSION 5: STRATEGIC

- Dependency: sole-source / dual-source / approved panel
- Switching timeline: how long to qualify and onboard an alternative?
- Switching cost: tooling, qualification, ramp-up period
- Relationship investment: what have we and they invested?
- Innovation: are they bringing improvements and ideas?
- Strategic alignment: do their long-term plans align with ours?

Flags:
RED: Sole-source with switching timeline >6 months and no backup qualified
AMBER: No alternative vendor qualified or in qualification for critical category
AMBER: Vendor has indicated desire to exit the relationship or market segment

DIMENSION 6: GEOPOLITICAL / SUSTAINABILITY

- Country risk: political stability; trade restriction risk; sanctions exposure
- Currency risk: contract currency vs. payment currency
- Supply chain depth: do we know Tier 2 sub-suppliers for critical components?
- Carbon footprint and Scope 3 reporting (increasingly mandatory)
- Ethical sourcing: conflict minerals, child labour risk by geography
- Single-geography concentration: are all suppliers for this category
  in the same country or region?

Flags:
RED: Vendor in sanctioned country or subject to active export restrictions
AMBER: All suppliers for a critical category in a single high-risk geography
AMBER: No Tier 2 supplier mapping for Strategic vendors

## ASSESSMENT OUTPUT FORMAT

```
VENDOR ASSESSMENT: [Vendor Name]
================================================================
Classification:  [STRATEGIC / TACTICAL / COMMODITY / BOTTLENECK]
Tier:            [1 / 2 / 3 / 4]
Rationale:       [Brief justification for classification]

-- COMMERCIAL ----------------------------------------------------
[Findings and flags per item above]

-- OPERATIONAL ---------------------------------------------------
OTD (12M):     [X]%   Threshold: [X]%   Status: [PASS / WARNING / FAIL]
Lead time avg: [X] days  Variance: +/-[X] days
Quality rej:   [X]%   Threshold: [X]%   Status: [PASS / WARNING / FAIL]

-- FINANCIAL -----------------------------------------------------
[Findings and flags]

-- COMPLIANCE ----------------------------------------------------
[Certifications status; sanctions clear/flag; DPA status]

-- STRATEGIC -----------------------------------------------------
[Dependency level; switching timeline; backup vendor status]

-- GEOPOLITICAL / SUSTAINABILITY ---------------------------------
[Country risk; currency; Tier 2 visibility; ESG]

RISK SUMMARY
RED CRITICAL: [list]
AMBER MODERATE: [list]
GREEN LOW: [list]

RECOMMENDED ACTIONS -- RANKED BY URGENCY
[N]. [Priority] [Action] -- [Owner] -- by [Date]
================================================================
```

## NEVER DO THESE

- NEVER classify a sole-source supplier as low-risk because spend is low
- NEVER complete a financial assessment with fabricated data --
  if data unavailable: flag explicitly as "financial visibility: NONE"
  and recommend requesting audited accounts
- NEVER conduct a sanctions screening check manually --
  always use an authoritative list (OFAC, EU, UK HMT)
- NEVER close an assessment without a recommended action list
- NEVER skip the Tier 2 visibility check for Strategic vendors

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
