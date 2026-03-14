---
name: basel-rwa-credit
description: >
  Activate for: credit risk RWA, risk-weighted assets, standardised approach,
  SA risk weight, risk weight table, CCF, credit conversion factor, EAD,
  exposure at default, IRB approach, mortgage risk weight, LTV band,
  corporate risk weight, SME risk weight, CRE risk weight.
  NOT for: market risk RWA or FRTB calculations (use basel-rwa-market),
  overall capital adequacy ratios or buffer stacking (use basel-capital),
  IFRS 9 ECL provisioning or impairment (use ifrs9-ecl).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "Basel III Standardised Approach for Credit Risk (BCBS)"
---

## STANDARDISED APPROACH — RISK WEIGHT TABLE

### Sovereign and Central Bank Exposures

| Credit Assessment | Risk Weight |
| ----------------- | ----------- |
| AAA to AA−        | 0%          |
| A+ to A−          | 20%         |
| BBB+ to BBB−      | 50%         |
| BB+ to B−         | 100%        |
| Below B−          | 150%        |
| Unrated           | 100%        |

Domestic currency sovereign claims (where funded in same currency): 0% (national discretion).

### Banks and Securities Firms

| Credit Assessment | Short-term (≤3M) | Long-term |
| ----------------- | ---------------- | --------- |
| AAA to AA−        | 20%              | 20%       |
| A+ to A−          | 20%              | 50%       |
| BBB+ to BBB−      | 20%              | 50%       |
| BB+ to B−         | 50%              | 100%      |
| Below B−          | 150%             | 150%      |
| Unrated           | 20%              | 50%       |

### Corporate Exposures

| Credit Assessment | Risk Weight                       |
| ----------------- | --------------------------------- |
| AAA to AA−        | 20%                               |
| A+ to A−          | 50%                               |
| BBB+ to BB−       | 75% (Basel IV; 100% pre-Basel IV) |
| Below BB−         | 150%                              |
| Unrated           | 100%                              |

Investment-grade corporates (BCBS Basel IV): 65% if criteria met.
SME corporate (qualifying): 75% (SME supporting factor may apply — check jurisdiction overlay).

### Retail Exposures

Qualifying revolving retail: 45%
Other retail (consumer loans, personal loans): 75%
Qualifying SME retail: 75%

### Residential Mortgage Exposures (Basel IV LTV-based)

| LTV     | Risk Weight (General) |
| ------- | --------------------- |
| ≤ 50%   | 20%                   |
| 50–60%  | 25%                   |
| 60–80%  | 30%                   |
| 80–90%  | 40%                   |
| 90–100% | 50%                   |
| > 100%  | 70%                   |

Note: Pre-Basel IV (current in many jurisdictions): flat 35–50%. Load jurisdiction
overlay to confirm whether Basel IV LTV table has been implemented.

### Commercial Real Estate (Basel IV)

Income-producing CRE: 75% (LTV-based table in Basel IV, higher than residential)
Land acquisition, development, construction (ADC): 150%
CRE securing a residential or SME loan (ancillary): follows the underlying loan RW.
Check jurisdiction overlay — CRE risk weights vary significantly.

### Past Due and Stage 3 Exposures

Unsecured past-due (>90 days, net of specific provisions):
Provision < 20% of outstanding: 150%
Provision ≥ 20% of outstanding: 100%
Provision ≥ 50% of outstanding: 50%

### Off-Balance-Sheet Credit Conversion Factors (CCF)

| Facility Type                                     | CCF  |
| ------------------------------------------------- | ---- |
| Unconditionally cancellable commitments           | 10%  |
| Commitments with original maturity ≤ 1 year       | 20%  |
| Commitments with original maturity > 1 year       | 40%  |
| Note issuance facilities / revolving underwriting | 50%  |
| Direct credit substitutes (guarantees)            | 100% |
| Forward asset purchases                           | 100% |

EAD for off-balance-sheet = Notional amount × CCF
Then apply the risk weight for the underlying exposure type.

## CREDIT RWA CALCULATION

Credit RWA = Σ (EAD × Risk Weight)
For off-balance-sheet: EAD = Drawn + (Undrawn × CCF), then × Risk Weight.

## IRB APPROACH (for reference)

IRB RWA = K × 12.5 × EAD
Where K = WCDR × LGD − PD × LGD (simplified form of Basel IRB formula)
WCDR = Conditional PD under the worst-case systematic risk scenario
Advanced IRB: bank supplies PD, LGD, EAD
Foundation IRB: bank supplies PD; regulator supplies LGD and EAD
Basel IV restrictions: AIRB no longer permitted for banks and large corporates.

## CREDIT RISK MITIGATION (CRM)

Eligible financial collateral: cash, sovereign bonds, bank bonds, equities in main index
CRM reduces EAD (collateralised portion gets lower or 0% risk weight).
Guarantees: substitute risk weight of guarantor for the guaranteed portion.
Netting: bilateral netting agreements reduce gross derivative exposure to net.

## WORKED EXAMPLE — CREDIT RWA CALCULATION

Portfolio: Mixed lending book (simplified)

| Exposure Class                            | Gross Exposure (M) | CCF (if OBS) | EAD (M)   | Risk Weight | RWA (M) |
| ----------------------------------------- | ------------------ | ------------ | --------- | ----------- | ------- |
| Domestic sovereign (AAA, domestic ccy)    | 500                | —            | 500       | 0%          | 0       |
| Bank (A+ rated, long-term)                | 200                | —            | 200       | 50%         | 100     |
| Corporate (BBB+ rated)                    | 300                | —            | 300       | 75%         | 225     |
| Corporate (unrated)                       | 150                | —            | 150       | 100%        | 150     |
| Residential mortgage (LTV 70%)            | 400                | —            | 400       | 30%         | 120     |
| Retail revolving                          | 100                | —            | 100       | 45%         | 45      |
| Undrawn commitment > 1yr (corporate, BBB) | 200                | 40%          | 80        | 75%         | 60      |
| Guarantee (on BB- rated entity)           | 50                 | 100%         | 50        | 150%        | 75      |
| **Total**                                 | **1,900**          |              | **1,780** |             | **775** |

Credit RWA = 775M
At 8% total capital requirement: minimum capital = 775 x 8% = 62M

## OUTPUT FORMAT — CREDIT RWA SUMMARY

```
CREDIT RWA SUMMARY
Entity:             [Bank / Group name]
Reporting Date:     [YYYY-MM-DD]
Approach:           [SA / F-IRB / A-IRB]
Jurisdiction:       [Overlay applied: UK PRA / EU CRR / US Fed / etc.]

EXPOSURE BREAKDOWN (M):
  Sovereigns:                    EAD [X]    RW [X%]    RWA [X]
  Banks:                         EAD [X]    RW [X%]    RWA [X]
  Corporates:                   EAD [X]    RW [X%]    RWA [X]
  Retail:                       EAD [X]    RW [X%]    RWA [X]
  Residential Mortgage:         EAD [X]    RW [X%]    RWA [X]
  Commercial Real Estate:       EAD [X]    RW [X%]    RWA [X]
  Past Due:                     EAD [X]    RW [X%]    RWA [X]
  Off-Balance-Sheet:            Notional [X]  CCF [X%]  EAD [X]  RWA [X]

TOTAL CREDIT RWA:               [Amount]
  of which Output Floor (if IRB): [Amount if binding]

CRM APPLIED:
  Eligible collateral:          [Amount]
  Guarantees (substitution):    [Amount]
  RWA reduction from CRM:       [Amount]
```

## NEVER DO THESE

- NEVER apply the 0% domestic currency sovereign risk weight to foreign currency sovereign exposures — the 0% treatment is only for domestic currency claims funded in the same currency
- NEVER use Basel IV LTV-based residential mortgage risk weights without confirming that the jurisdiction has implemented them — many jurisdictions still use the flat 35% pre-Basel IV weight
- NEVER omit the CCF step for off-balance-sheet exposures — EAD must be calculated as Notional x CCF before applying the risk weight
- NEVER apply the SME supporting factor without verifying the exposure qualifies under the jurisdiction's SME definition (turnover threshold, exposure cap)
- NEVER ignore the Basel IV output floor for IRB banks — IRB credit RWA must be >= 72.5% of SA RWA for the same portfolio

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
