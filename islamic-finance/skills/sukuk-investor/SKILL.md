---
name: sukuk-investor
description: >
  Activate for: sukuk investment, sukuk holding, sukuk portfolio,
  sukuk classification IFRS 9, SPPI sukuk, sukuk amortised cost,
  sukuk FVOCI, sukuk FVTPL, FAS 25, sukuk income accrual,
  sukuk mark-to-market, Government Investment Issue, GII,
  Government of Pakistan Ijarah Sukuk, GIS, sukuk ECL.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 25 (Investment in Sukuk), IFRS 9 Classification"
---

## INVESTOR CLASSIFICATION — IFRS 9

For sukuk held by investors, apply the IFRS 9 two-step classification:

### Step 1 — Business Model Test

**Held-to-collect (HTC):** Investor holds sukuk to collect contractual cash flows.
→ If SPPI test also passed: Amortised Cost

**Held-to-collect-and-sell (HTCS):** Investor collects cash flows but also sells.
→ If SPPI test also passed: Fair Value through OCI (FVOCI, debt instrument)

**Other:** Trading, short-term, managed on fair value basis.
→ FVTPL regardless of SPPI test

### Step 2 — SPPI Test (Solely Payments of Principal and Interest)

The sukuk cash flows must represent SOLELY:
- Repayment of principal (the face value / initial investment)
- A return consistent with a basic lending arrangement (compensation for time value of
  money, credit risk, and basic lending costs)

**SPPI PASS (typically leads to Amortised Cost or FVOCI):**
- Ijarah sukuk with fixed periodic distributions + fixed maturity redemption
  → Cash flows represent principal + fixed return → SPPI PASS
- Ijarah sukuk with floating rate tied to a benchmark (SOFR, KIBOR, etc.)
  → SPPI may pass if benchmark + spread is pure time-value-of-money compensation
- Government ijarah sukuk (GIS Pakistan, GII Malaysia)
  → Typically classified at amortised cost by Islamic banks in respective countries

**SPPI FAIL (requires FVTPL):**
- Musharakah sukuk: return depends on venture profit → not solely principal + return
  → SPPI FAILS → FVTPL classification
- Mudarabah sukuk: same as musharakah → SPPI FAILS → FVTPL
- Equity-linked sukuk: return depends on equity performance → SPPI FAILS
- Convertible sukuk: conversion feature creates equity kicker → SPPI FAILS

**PURCHASE UNDERTAKING EFFECT ON SPPI:**
If the sukuk has a purchase undertaking at face value (common in ijarah sukuk):
The maturity payment = face value regardless of asset value.
This is economically similar to principal repayment on a loan.
Most practitioners conclude: this does NOT cause SPPI failure.
The undertaking ensures the investor receives what was contracted → consistent with lending.

---

## INITIAL RECOGNITION

**Amortised Cost (ijarah sukuk, HTC, SPPI pass):**
Dr: Investment in Sukuk — Amortised Cost [Fair value at acquisition = usually face value +/- premium/discount]
Cr: Cash [Purchase price]

If acquired at premium or discount: carry the difference as unamortised premium/discount,
amortise using effective profit rate over remaining life to bring to face value at maturity.

**FVOCI (ijarah sukuk, HTCS, SPPI pass):**
Dr: Investment in Sukuk — FVOCI [Fair value at acquisition]
Cr: Cash [Purchase price]

**FVTPL (musharakah / mudarabah sukuk, or other):**
Dr: Investment in Sukuk — FVTPL [Fair value at acquisition]
Cr: Cash [Purchase price]

---

## PERIODIC INCOME RECOGNITION

**Amortised Cost:**
Dr: Accrued Sukuk Income Receivable [Carrying value x effective profit rate / periods]
Cr: Income from Sukuk — Amortised Cost [Same]

**FVOCI:**
Same income accrual as amortised cost (effective profit rate on amortised cost).
Plus period-end fair value remeasurement:
Dr/Cr: Investment in Sukuk — FVOCI [Fair value change]
Cr/Dr: OCI — Sukuk Fair Value Reserve [Same]

**FVTPL:**
Dr/Cr: Investment in Sukuk — FVTPL [Fair value change]
Cr/Dr: Gain/Loss on Sukuk — FVTPL (P&L) [Same]
Plus any distributions received → income.

---

## AAOIFI FAS 25 (BAHRAIN, QATAR)

AAOIFI FAS 25 classifies sukuk investments into:
- **Held-to-maturity** (similar to amortised cost)
- **Trading** (similar to FVTPL)
- **Available-for-sale** (similar to FVOCI)

Measurement: held-to-maturity at amortised cost; trading at fair value (P&L);
AFS at fair value with changes in OCI.

Income labels under AAOIFI FAS 25:
"Income from Sukuk Investments" or "Return on Sukuk" — NEVER "Interest Income."

---

## IMPAIRMENT

**Amortised Cost and FVOCI:** Apply IFRS 9 ECL model.
Sukuk ECL staging:
- Government sukuk (AAA/AA sovereign): Stage 1 only (12-month ECL, typically minimal)
- Investment grade corporate sukuk: Stage 1 or 2 depending on credit migration
- Sub-investment grade or distressed sukuk: Stage 3 (lifetime ECL)

ECL for sukuk is typically modelled using:
PD (probability of default) x LGD (loss given default) x EAD (exposure at default)

Note: For GIS (Pakistan) and GII (Malaysia) — sovereign sukuk rated at sovereign level.
Use sovereign rating as PD input.

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 25:**
1. Classification of sukuk investments by type
2. Movement in each classification category
3. Income recognised by category
4. Fair value of held-to-maturity sukuk (for disclosure purposes only)
5. Impairment provisions on sukuk

**IFRS 7 / IFRS 9:**
1. Classification basis and SPPI analysis for each category
2. Movement table: amortised cost / FVOCI / FVTPL by category
3. ECL movement table (Stage 1, 2, 3)
4. Fair value hierarchy (Level 1 / 2 / 3)
5. OCI reserve movement (for FVOCI sukuk)
6. Sensitivity analysis: impact of 100bp yield movement on FVOCI/FVTPL portfolio
7. Concentration risk: top 10 sukuk holdings by issuer
