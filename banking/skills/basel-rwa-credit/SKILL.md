---
name: basel-rwa-credit
version: 1.0
description: >
  Activate for: credit risk RWA, risk-weighted assets, standardised approach,
  SA risk weight, risk weight table, CCF, credit conversion factor, EAD,
  exposure at default, IRB approach, mortgage risk weight, LTV band,
  corporate risk weight, SME risk weight, CRE risk weight.
standard: Basel III Standardised Approach for Credit Risk (BCBS)
author: Panaversity — The AI Agent Factory
---

## STANDARDISED APPROACH — RISK WEIGHT TABLE

### Sovereign and Central Bank Exposures
| Credit Assessment | Risk Weight |
|---|---|
| AAA to AA− | 0% |
| A+ to A− | 20% |
| BBB+ to BBB− | 50% |
| BB+ to B− | 100% |
| Below B− | 150% |
| Unrated | 100% |
Domestic currency sovereign claims (where funded in same currency): 0% (national discretion).

### Banks and Securities Firms
| Credit Assessment | Short-term (≤3M) | Long-term |
|---|---|---|
| AAA to AA− | 20% | 20% |
| A+ to A− | 20% | 50% |
| BBB+ to BBB− | 20% | 50% |
| BB+ to B− | 50% | 100% |
| Below B− | 150% | 150% |
| Unrated | 20% | 50% |

### Corporate Exposures
| Credit Assessment | Risk Weight |
|---|---|
| AAA to AA− | 20% |
| A+ to A− | 50% |
| BBB+ to BB− | 75% (Basel IV; 100% pre-Basel IV) |
| Below BB− | 150% |
| Unrated | 100% |
Investment-grade corporates (BCBS Basel IV): 65% if criteria met.
SME corporate (qualifying): 75% (SME supporting factor may apply — check jurisdiction overlay).

### Retail Exposures
Qualifying revolving retail: 45%
Other retail (consumer loans, personal loans): 75%
Qualifying SME retail: 75%

### Residential Mortgage Exposures (Basel IV LTV-based)
| LTV | Risk Weight (General) |
|---|---|
| ≤ 50% | 20% |
| 50–60% | 25% |
| 60–80% | 30% |
| 80–90% | 40% |
| 90–100% | 50% |
| > 100% | 70% |
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
| Facility Type | CCF |
|---|---|
| Unconditionally cancellable commitments | 10% |
| Commitments with original maturity ≤ 1 year | 20% |
| Commitments with original maturity > 1 year | 40% |
| Note issuance facilities / revolving underwriting | 50% |
| Direct credit substitutes (guarantees) | 100% |
| Forward asset purchases | 100% |

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
