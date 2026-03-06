---
name: aml-typologies
version: 1.0
description: >
  Activate for: AML alert, transaction monitoring, suspicious activity,
  money laundering, structuring, smurfing, round-tripping, layering,
  placement, integration, typology, red flag, velocity alert, geographic
  anomaly, TBML, trade-based money laundering, network analysis, PEP alert.
  NOT for: SAR/STR drafting or filing (use aml-sar-drafting), customer onboarding
  or KYC documentation (use aml-cdd-edd), sanctions list screening (use
  sanctions-screening).
standard: FATF 40 Recommendations — jurisdiction AML legislation (load overlay)
author: Panaversity — The AI Agent Factory
---

## THE THREE STAGES OF MONEY LAUNDERING

Placement — Introducing illicit funds into the financial system
Red flags: Large cash deposits; multiple deposits just below reporting threshold
(structuring); money service business transactions; casino chip purchases/redemptions.

Layering — Obscuring the audit trail through multiple transactions
Red flags: Rapid movement through multiple accounts; complex wire sequences across
multiple jurisdictions; shell company or nominee director use; conversion between
asset classes (cash → wire → crypto → real estate).

Integration — Re-introducing laundered funds as apparently legitimate income
Red flags: Luxury asset purchases (real estate, vehicles, art); unexplained business
investments; loan repayments from obscure sources; complex "business transactions"
with no apparent commercial purpose.

## TOP 20 AML TYPOLOGIES WITH DETECTION LOGIC

1. STRUCTURING (SMURFING)
   Indicator: Multiple cash deposits/withdrawals in a single account, each just below
   the reporting threshold, within a defined period.
   Detection rule: ≥3 transactions within 7 days each ≥ 80% of the reporting threshold.
   ML enhancement: Aggregate transactions per customer per rolling 30-day window.
   Note: The reporting threshold is jurisdiction-specific (USD 10,000 in USA, varies elsewhere).

2. ROUND-TRIPPING
   Indicator: Funds sent from Account A to Jurisdiction X, then returned from Jurisdiction X
   to Account A or a closely connected account within a short period.
   Detection: Wire-out to jurisdiction X followed by wire-in from same jurisdiction
   within 30 days, same approximate amount (±10%).

3. RAPID FUND MOVEMENT / VELOCITY
   Indicator: Account receives large funds then transfers them out within 24–72 hours
   with minimal balance remaining.
   Detection rule: Opening balance < 10% of daily inflow; >80% of incoming funds
   transferred out within 48 hours.

4. GEOGRAPHIC ANOMALY
   Indicator: Transactions to/from high-risk jurisdictions inconsistent with customer profile.
   Detection: Any transaction above de minimis to FATF grey-listed or black-listed countries.
   Enhanced scrutiny for: Iran, North Korea, Myanmar (FATF black list);
   current grey list — check FATF.org for current listing as it changes quarterly.

5. TRADE-BASED MONEY LAUNDERING (TBML)
   Indicator: Over/under-invoicing; multiple invoicing; falsely described goods.
   Red flags: Invoice amounts inconsistent with commodity market price;
   import/export volumes inconsistent with declared business size;
   inconsistency between shipping documents and invoices.

6. PROFESSIONAL MONEY LAUNDERING NETWORKS
   Indicator: Account connected through transactions to other accounts with known
   AML suspicion or law enforcement interest.
   Detection: Graph network analysis — identify high-centrality nodes, clusters of
   accounts with high internal velocity and cash-out at network periphery.

7. PEP UNUSUAL TRANSACTION
   Indicator: Politically Exposed Person receives unexplained large incoming transfer
   disproportionate to known income/wealth profile.
   Detection rule: Any PEP account single transaction > 3× average monthly balance.
   Any PEP incoming transfer from jurisdiction with high corruption index.

8. SHELL COMPANY LAYERING
   Indicator: Corporate account with no apparent operational activity — no payroll,
   no supplier payments, only wire receipts and outflows.
   Red flags: Beneficial owner structure through Cayman / BVI / Panama / Cyprus;
   multiple directors with no apparent operational role; no website or publicly
   verifiable business presence.

9. LOAN-BACK
   Indicator: Customer places cash/funds in account, then takes a "loan" collateralised
   by those funds. Repays loan with laundered funds; withdraws original "collateral" clean.
   Detection: Secured lending against own deposits; loan repayments from sources
   inconsistent with declared income.

10. REAL ESTATE MONEY LAUNDERING
    Indicator: All-cash property purchase; multiple rapid buy/sell transactions in same
    property; purchase at significantly above or below market value.
    Red flags: Payment from a third party with no apparent connection to the buyer;
    offshore corporate as buyer with opaque beneficial ownership.

11. CRYPTO-TO-FIAT CONVERSION
    Indicator: Incoming wires from cryptocurrency exchanges to bank accounts.
    Red flags: High-frequency conversion from multiple exchanges; exchanges operating
    in high-risk jurisdictions with weak AML controls; transaction amounts not rounded
    (characteristic of crypto exchange deposits).

12. MONEY MULE ACTIVITY
    Indicator: Account receives funds from multiple unknown sources and immediately
    transfers to third parties; account holder's profile inconsistent with transaction volumes.
    Detection: Multiple incoming wires from unknown parties; average transaction ≫
    declared income; account holder has changed personal details (address, employment) recently.

13. INSURANCE PREMIUM FINANCING LAUNDERING
    Indicator: Purchase large-value life insurance policy with lump sum; cancel early
    and accept surrender penalty to receive "clean" refund cheque from insurer.
    Red flags: Large single premium life insurance; early policy surrender; cash source
    inconsistent with declared income.

14. INVOICE FRAUD / ADVANCE FEE FRAUD
    Indicator: Account receives multiple large payments described as "invoices" or
    "commissions" from offshore entities with no apparent business relationship.

15. LAYERING VIA SECURITIES
    Indicator: Purchase securities (equities, bonds) with cash/wire, then rapidly sell
    and withdraw cash from proceeds.
    Detection: Same-day or next-day securities purchase and sale with no apparent
    investment rationale; securities transactions from accounts with no investment history.

16. CROSS-BORDER CASH SMUGGLING FRONT
    Indicator: Business with declared import/export activities used to justify cross-border
    fund movements that are disproportionate to the declared business scale.

17. HAWALA / INFORMAL VALUE TRANSFER
    Indicator: Payments to known hawala operators; international transfers with
    "settlement" description; amounts consistent with remittance fees charged on
    informal value transfer.

18. GAMBLING / CASINO LAYERING
    Indicator: Purchase casino chips with cash; minimal gambling; cash out.
    Remote gambling: Fund online gambling account; withdraw without significant play.

19. CORRESPONDENT BANKING NESTED ACCOUNTS
    Indicator: Respondent bank (foreign) maintains accounts for its own customers
    within the correspondent relationship — "nested" accounts not directly visible
    to the correspondent bank.
    Detection: Wire patterns suggesting multiple underlying account holders using
    a single correspondent relationship.

20. TERRORIST FINANCING (SMALL AMOUNTS, UNUSUAL DESTINATIONS)
    Indicator: Multiple small international transfers to individuals in conflict zones
    or areas with known terrorist activity.
    Distinguishing feature: Unlike money laundering (large amounts laundered to appear
    clean), terrorist financing often involves small amounts from legitimate sources.

## ALERT DISPOSITION DECISION TREE

Level 1 — Quick Close (< 5 min): Fully explained by known business profile?
YES with documentation → Close with documented rationale

Level 2 — Customer/RM Contact (< 1 hr): Plausible explanation but insufficient info?
Request clarification → If satisfactory + documented → Close
If unsatisfactory → Escalate to Level 3

Level 3 — Enhanced Investigation (< 24 hr): Suspicious despite explanation?
Obtain: company filings, adverse media search, transaction history, BO verification
If suspicion eliminated + documented → Close
If suspicion remains → Escalate to Level 4

Level 4 — MLRO SAR Decision: Apply jurisdiction's SAR standard (see overlay)
UK: "reasonable grounds to suspect" (POCA 2002)
USA: "reason to suspect" involving $5,000+ and a legal violation (BSA)
File SAR/STR if standard met → Account continuation decision

## MACHINE LEARNING ENHANCEMENTS

Peer group analysis: Flag customers whose transaction patterns deviate >2 standard
deviations from statistically similar peers (same product, geography, business type).
Network/graph analysis: Flag customers who are highly connected through transactions
to other flagged/suspicious customers — even if their own transactions appear benign.
Autoencoder anomaly detection: Train on "normal" transactions; flag those with high
reconstruction error as novel — effective for detecting new typologies.
Reported outcomes: Featurespace/Visa and NICE Actimize report 50–70% false positive
reduction in production deployments while maintaining or improving detection rates.

## OUTPUT FORMAT — TYPOLOGY ASSESSMENT

```
TYPOLOGY ASSESSMENT
Alert ID:          [System-generated alert ID]
Customer:          [Name / ID]
Assessment Date:   [YYYY-MM-DD]

ALERT TRIGGER:
  Rule/Model:      [Rule name or ML model that generated the alert]
  Transaction(s):  [Date, amount, type, counterparty for each flagged transaction]

TYPOLOGY IDENTIFIED:
  Primary:         [Typology name from list above — e.g., STRUCTURING, ROUND-TRIPPING]
  Secondary:       [Additional typology if applicable]
  ML Stage:        [Placement / Layering / Integration]

ASSESSMENT:
  Customer Profile:    [Summary of expected activity vs. observed activity]
  Innocent Explanation:[Considered and why insufficient, OR why activity is legitimate]
  Risk Indicators:     [List specific red flags observed]

DISPOSITION:
  Level:           [1 — Quick Close / 2 — RM Contact / 3 — Enhanced Investigation / 4 — MLRO SAR Decision]
  Decision:        [Close with rationale / Escalate / File SAR]
  Rationale:       [Documented reasoning for disposition]
```

## NEVER DO THESE

- NEVER close an alert without documenting the rationale — undocumented closures are treated as control failures by regulators and auditors
- NEVER apply a single typology's detection rule in isolation without considering whether multiple typologies may be operating simultaneously (e.g., structuring + round-tripping)
- NEVER dismiss geographic anomaly alerts solely because the customer has a stated business reason for transacting with high-risk jurisdictions — the business explanation must be independently verified against trade documents and commercial reality
- NEVER use ML model output alone as the sole basis for closing or escalating — model scores inform human judgment but do not replace the analyst's documented assessment
- NEVER treat terrorist financing alerts using the same thresholds as money laundering alerts — TF often involves small amounts from legitimate sources directed to conflict zones

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
