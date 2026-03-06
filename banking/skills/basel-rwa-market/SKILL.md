---
name: basel-rwa-market
version: 1.0
description: >
  Activate for: FRTB, Fundamental Review of the Trading Book, market risk RWA,
  trading book capital, SA-TB, standardised approach trading book, sensitivities-
  based method, SBM, delta, vega, curvature, default risk charge, DRC, residual
  risk add-on, RRAO, internal models approach, IMA, expected shortfall, ES,
  P&L attribution, PLA, backtesting, GIRR, CSR, equity risk, commodity risk,
  FX risk, market risk capital, trading desk.
  NOT for: credit risk RWA under standardised or IRB approach (use basel-rwa-credit),
  capital adequacy ratios and buffer calculations (use basel-capital), IFRS 9 ECL
  provisioning (use ifrs9-ecl).
standard: Basel III FRTB (BCBS d352/d457) -- jurisdiction implementations vary (load overlay)
author: Panaversity -- The AI Agent Factory
---

## CORE PRINCIPLE

Market risk capital under FRTB replaces the pre-2016 VaR-based framework with
a risk-sensitive approach that distinguishes between the Standardised Approach (SA)
and the Internal Models Approach (IMA). The SA is the default and fallback; IMA
requires desk-level regulatory approval including P&L attribution and backtesting.

FRTB applies to all instruments in the regulatory trading book. The trading book
boundary is defined by strict criteria (intent to trade, ability to hedge, daily
fair-value accounting) -- not by the bank's internal designation alone.

---

## STANDARDISED APPROACH (SA-TB) -- THREE COMPONENTS

Market Risk Capital (SA) = SBM + DRC + RRAO

### Component 1: Sensitivities-Based Method (SBM)

The SBM captures delta, vega, and curvature risks across seven risk classes.

#### Seven Risk Classes

| #   | Risk Class                        | Key Risk Factors                                                                            |
| --- | --------------------------------- | ------------------------------------------------------------------------------------------- |
| 1   | GIRR (General Interest Rate Risk) | Risk-free rates by tenor (3M, 6M, 1Y, 2Y, 3Y, 5Y, 10Y, 15Y, 20Y, 30Y), cross-currency basis |
| 2   | CSR non-securitisation            | Credit spreads by issuer, sector, tenor                                                     |
| 3   | CSR securitisation (CTP)          | Correlation trading portfolio credit spreads                                                |
| 4   | CSR securitisation (non-CTP)      | Non-correlation trading securitisation spreads                                              |
| 5   | Equity                            | Equity spot prices, repo rates                                                              |
| 6   | Commodity                         | Commodity prices by type (energy, metals, agricultural, other) and tenor                    |
| 7   | FX                                | Exchange rates against reporting currency                                                   |

#### SBM Calculation Steps

Step 1 -- Net Sensitivities: Calculate net delta, vega, and curvature sensitivities
per risk factor within each risk class.

Step 2 -- Weighted Sensitivities: Multiply each net sensitivity by the prescribed
risk weight for that risk factor.
Delta risk weights vary by risk class and tenor (e.g., GIRR: 1.5%-2.4% by tenor;
Equity: 15%-70% by market cap and economy; FX: 15%).
Vega risk weights: uniform within risk class, calibrated to stressed implied volatility.

Step 3 -- Aggregation Within Bucket: Aggregate weighted sensitivities within each
bucket using prescribed intra-bucket correlations (rho).
K*b = sqrt( sum_i sum_j rho_ij * WS*i * WS_j )
where WS = weighted sensitivity, rho = intra-bucket correlation

Step 4 -- Aggregation Across Buckets: Aggregate across buckets using prescribed
inter-bucket correlations (gamma).
Capital = sqrt( sum*b sum_c gamma_bc * S*b * S_c )
where S_b = net bucket-level capital, gamma = inter-bucket correlation

Step 5 -- Three Correlation Scenarios: Calculate SBM under three correlation scenarios:
(a) Medium correlations (prescribed rho and gamma)
(b) High correlations (rho _ 1.25, gamma _ 1.25, capped at 1)
(c) Low correlations (rho _ 0.75, gamma _ 0.75)
SBM = MAX(SBM_medium, SBM_high, SBM_low)

#### Curvature Risk

Curvature risk captures the non-linear risk that delta sensitivities miss.
Calculate by shocking each risk factor up and down by a prescribed amount,
revaluing the portfolio, and computing the curvature charge:
CVR*k = -min( V(x_k^up) - V(x_k) - s_k * delta*k,
V(x_k^down) - V(x_k) + s_k * delta_k, 0 )
where s_k = prescribed shock size for risk factor k.

### Component 2: Default Risk Charge (DRC)

DRC captures jump-to-default risk for credit and equity instruments in the
trading book -- the risk of an issuer defaulting between now and the next
rebalancing period.

DRC Calculation:
DRC = sum*i ( LGD_i * Notional*i * RW_i ) after hedging benefit
Risk weights by credit quality: AAA 0.5%, AA 2%, A 3%, BBB 6%, BB 15%, B 30%, CCC 50%, Default 100%
Hedging benefit: long-short offset within same issuer and seniority; partial
offset across issuers in the same sector using prescribed hedge benefit ratios.

DRC is additive to SBM -- no diversification benefit between DRC and SBM.

### Component 3: Residual Risk Add-On (RRAO)

RRAO is a simple gross notional charge for instruments with exotic risks not
captured by SBM or DRC:

- Instruments bearing exotic underlying risks (e.g., longevity, weather, natural disaster): 1.0% of gross notional
- Other instruments with residual risks (e.g., gap risk, correlation risk, behavioural risk): 0.1% of gross notional

Instruments subject to RRAO include: barrier options, digital options, Asian
options, basket options with non-standard payoffs, variance/volatility swaps,
correlation products, weather derivatives.

RRAO is additive -- no diversification with SBM or DRC.

---

## INTERNAL MODELS APPROACH (IMA)

IMA is approved on a desk-by-desk basis by the regulator. Any desk failing
IMA eligibility reverts to SA for that desk.

### IMA Capital Charge

IMA Capital = max( ES_t-1, m \* ES_avg ) + DRC_IMA + SES
where:
ES = Expected Shortfall at 97.5% confidence
m = multiplier (minimum 1.5, increased by regulator based on backtesting failures)
ES_avg = 60-day weighted average ES
DRC_IMA = internal default risk charge
SES = stressed expected shortfall (calibrated to stressed period)

### Expected Shortfall (ES) -- Calculation

ES replaces VaR as the primary risk measure under FRTB.
ES is calculated at the 97.5th percentile (vs. VaR at 99th percentile).
ES is coherent (satisfies sub-additivity); VaR is not.

Liquidity-Adjusted ES:
ES = sqrt( sum_j ( ES_j(P_j) \* sqrt(LH_j / 10) )^2 )
where LH_j = regulatory liquidity horizon for risk factor j:
10 days: Large-cap equity, FX (major currencies), GIRR (G7 currencies)
20 days: Small-cap equity, FX (other), credit investment grade
40 days: Credit high yield, emerging market sovereign
60 days: Securitised products, commodity (other)
120 days: Correlation trading, illiquid exotic

### IMA Eligibility Tests (Desk-Level)

#### Test 1: P&L Attribution (PLA)

Compare the hypothetical P&L (from risk model) to the actual P&L (from front office).
Two statistics:
Spearman correlation: must be > 0.7
Kolmogorov-Smirnov (KS) test: KS statistic must be < 0.09
If either fails for 4+ quarters: desk reverts to SA.

Traffic light assessment:
Green: Both metrics pass
Amber: One metric in warning zone
Red: Either metric fails -- desk loses IMA eligibility

#### Test 2: Backtesting

Compare daily VaR (at 99%) to actual P&L over the prior 250 trading days.
Count exceptions (days where actual loss > VaR estimate):
Green zone: 0-4 exceptions (multiplier = 1.5)
Amber zone: 5-9 exceptions (multiplier = 1.5 + 0.1 per additional exception)
Red zone: 10+ exceptions (multiplier >= 2.0; regulator may revoke IMA for desk)

Backtesting is performed at desk level AND at bank-wide level.

---

## TRADING BOOK BOUNDARY

### Assignment to Trading Book

Instruments must be assigned to the trading book if:

- Held with intent to trade or to hedge trading book positions
- Subject to daily fair value accounting under the relevant accounting framework
- The bank has the ability to trade or hedge the risk

### Instruments Presumed in Trading Book

- Correlation trading
- Instruments resulting from market-making activities
- Listed equity holdings
- Instruments arising from underwriting commitments
- Positions in a CIU (collective investment undertaking) look through to underlying

### Internal Risk Transfers (IRT)

Transfers of risk between banking book and trading book must be strictly documented.
Capital relief is only granted if the IRT is properly hedged in the trading book
and meets regulatory IRT documentation standards.

---

## KEY RISK WEIGHT TABLES (SA -- SELECTED)

### GIRR Delta Risk Weights by Tenor

| Tenor | Risk Weight |
| ----- | ----------- |
| 0.25Y | 2.4%        |
| 0.5Y  | 2.4%        |
| 1Y    | 2.25%       |
| 2Y    | 1.88%       |
| 3Y    | 1.73%       |
| 5Y    | 1.5%        |
| 10Y   | 1.5%        |
| 15Y   | 1.5%        |
| 20Y   | 1.5%        |
| 30Y   | 1.5%        |

### Equity Delta Risk Weights

| Bucket | Description                   | Risk Weight |
| ------ | ----------------------------- | ----------- |
| 1      | Large cap, emerging markets   | 55%         |
| 2      | Large cap, advanced economies | 30%         |
| 3      | Small cap, emerging markets   | 70%         |
| 4      | Small cap, advanced economies | 50%         |
| 5-8    | Sector-specific               | 15%-70%     |
| Other  | Indices, ETFs                 | 15%         |

### FX Delta Risk Weight

All currency pairs: 15%
Specified liquid currency pairs (EUR/USD, USD/JPY, etc.): eligible for sqrt(2) reduction

### DRC Risk Weights by Credit Quality

| Rating    | Risk Weight |
| --------- | ----------- |
| AAA       | 0.5%        |
| AA        | 2%          |
| A         | 3%          |
| BBB       | 6%          |
| BB        | 15%         |
| B         | 30%         |
| CCC       | 50%         |
| Unrated   | 15%         |
| Defaulted | 100%        |

---

## FRTB IMPLEMENTATION STATUS

| Jurisdiction           | SA Mandatory | IMA Available       | Implementation Date     |
| ---------------------- | ------------ | ------------------- | ----------------------- |
| EU (CRR3)              | Yes          | Yes (desk approval) | January 2025            |
| UK (PRA)               | Yes          | Yes (desk approval) | Consultation ongoing    |
| US (Basel III Endgame) | Proposed     | Proposed            | TBD (check Fed website) |
| Australia (APRA)       | Consulting   | TBD                 | TBD (check APRA)        |
| Singapore (MAS)        | Consulting   | TBD                 | TBD (check MAS)         |

Always load jurisdiction overlay to confirm current FRTB implementation status.

---

## NEVER DO THESE

- NEVER use pre-FRTB VaR-based market risk capital for new calculations -- FRTB replaces VaR with ES
- NEVER aggregate DRC with SBM using diversification -- DRC is additive
- NEVER skip the three correlation scenarios in SBM -- capital = MAX of all three
- NEVER assume IMA approval is bank-wide -- it is granted desk-by-desk
- NEVER ignore P&L attribution test results -- 4 quarterly failures = mandatory reversion to SA
- NEVER apply banking book risk weights to trading book positions -- FRTB has its own risk weight framework
- NEVER forget the RRAO for exotic instruments -- it is a separate additive charge

## OUTPUT FORMAT -- MARKET RISK CAPITAL SUMMARY

```
MARKET RISK CAPITAL SUMMARY (FRTB)
Entity:             [Bank / Group name]
Reporting Date:     [YYYY-MM-DD]
Approach:           [SA / IMA / Mixed (desk-level)]
Jurisdiction:       [Overlay applied: EU CRR3 / UK PRA / US Fed / etc.]

STANDARDISED APPROACH (SA):
  SBM (Sensitivities-Based Method):
    GIRR:                        [Amount]
    CSR non-sec:                 [Amount]
    CSR sec (CTP):               [Amount]
    CSR sec (non-CTP):           [Amount]
    Equity:                      [Amount]
    Commodity:                   [Amount]
    FX:                          [Amount]
    Total SBM:                   [Amount]
    Binding scenario:            [Medium / High / Low correlations]

  DRC (Default Risk Charge):    [Amount]
  RRAO (Residual Risk Add-On):  [Amount]

  SA TOTAL:                      [Amount]

IMA (if applicable):
  Desks on IMA:                  [List]
  ES (Expected Shortfall):      [Amount]
  DRC (IMA):                    [Amount]
  SES (Stressed ES):            [Amount]
  IMA multiplier:               [X.X]
  IMA TOTAL:                    [Amount]
  Desks reverted to SA:         [List + reason]

TOTAL MARKET RISK CAPITAL:      [Amount]
```

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
