---
name: sukuk-issuer
description: >
  Activate for: sukuk issuance, sukuk structuring, sukuk SPV, trust deed,
  sukuk al-ijarah, sukuk al-musharakah, sukuk al-mudarabah, sukuk al-wakala,
  sukuk originator, sukuk proceeds, purchase undertaking, sukuk liability,
  sukuk equity, FAS 33, IAS 32 sukuk, sukuk derecognition,
  green sukuk, sustainable sukuk, sale and leaseback sukuk.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 33 (Investment in Sukuk — Issuer), IAS 32"
---

## SUKUK TYPES AND UNDERLYING STRUCTURES

| Sukuk Type | Underlying Structure | Key Accounting Question |
|---|---|---|
| Ijarah sukuk | Sale and leaseback of assets | Does originator derecognise assets? |
| Musharakah sukuk | Joint venture / partnership | Financial liability or equity? |
| Mudarabah sukuk | Profit-sharing investment | Financial liability or equity? |
| Wakala sukuk | Agency investment management | What is the agent's balance sheet position? |
| Murabaha sukuk | Portfolio of murabaha receivables | Tradability — Shariah restriction on debt sale |
| Hybrid sukuk | Mixed pool (murabaha/ijarah/wakala) | Dominant contract determines treatment |

---

## IJARAH SUKUK — THE MOST COMMON STRUCTURE

**Structure:**
1. Originator sells assets to SPV (sukuk trustee) for proceeds = sukuk face value.
2. SPV issues sukuk certificates to investors; investors pay face value to SPV.
3. SPV leases assets back to originator. Rental = sukuk distribution payments.
4. At maturity, originator repurchases assets (purchase undertaking).

**The Two Critical Accounting Questions:**

**Question 1 — Derecognition of assets by originator:**
Has the originator transferred substantially all the risks and rewards of the assets?

IFRS 9 derecognition test:
If YES (risks and rewards transferred): Derecognise assets, recognise proceeds as cash.
If NO (risks and rewards retained): Keep assets on balance sheet (failed derecognition).

CRITICAL: If the originator has a PURCHASE UNDERTAKING to repurchase at FACE VALUE
at maturity regardless of the asset's current market value, this is strong evidence
that risks and rewards have NOT been transferred. The originator still bears the
value risk of the underlying assets. → Failed derecognition.
→ Keep assets on balance sheet + recognise sukuk proceeds as a financial liability.

Most ijarah sukuk globally are accounted for as failed derecognition:
Assets stay on originator's balance sheet; sukuk = financial liability.

**Question 2 — Sukuk classification: financial liability or equity (IAS 32)?**

If originator has a contractual obligation to:
(a) Pay periodic cash distributions (rental) → creates financial liability component
(b) Repay face value at maturity (purchase undertaking) → creates financial liability

IAS 32 conclusion (for most ijarah sukuk): FINANCIAL LIABILITY, not equity.
Because there is a contractual obligation to deliver cash.

If the sukuk structure gives investors no contractual right to cash
(returns are purely profit-contingent) → may be equity. Rare in practice.

---

## ISSUER JOURNAL ENTRIES — IJARAH SUKUK (TYPICAL — FAILED DERECOGNITION)

**At issuance:**
Dr: Cash [Sukuk proceeds]
Cr: Sukuk Payable / Islamic Financing Liabilities [Face value]

(Assets remain on balance sheet — no derecognition entry required)

**Periodic rental payment (= sukuk distribution):**
Dr: Finance Cost / Profit on Sukuk [Distribution amount]
Cr: Cash [Distribution amount]

Note: In AAOIFI regime, label as "Profit on Sukuk" not "Interest on Sukuk."
In IFRS regime: "Finance Cost" is acceptable; some preparers use "Sukuk Distribution."

**At maturity (purchase undertaking execution):**
Dr: Sukuk Payable [Face value]
Cr: Cash [Repurchase price per purchase undertaking]

---

## MUSHARAKAH / MUDARABAH SUKUK — EQUITY-LIKE TREATMENT

If the sukuk is genuinely equity-based (no redemption obligation, returns are profit-contingent):
→ IAS 32 equity classification
→ Distributions are equity distributions, not finance costs
→ NOT deducted in calculating profit before tax

AAOIFI Shariah Standard: Purchase undertakings at face value are NOT permissible
for musharakah and mudarabah sukuk (they guarantee capital, eliminating investment risk).
Therefore: genuine musharakah/mudarabah sukuk should have no guaranteed redemption.
In practice, many structures use exercise price at market value (not face value) for musharakah.

---

## AAOIFI DRAFT STANDARD 62 — ASSET-BACKED SUKUK

Proposed shift: from "asset-based" (sukuk = unsecured claim on originator)
to "asset-backed" (sukuk = secured claim on specific assets, no recourse to originator).

If adopted:
- Originator must genuinely transfer assets (true sale)
- Investors have recourse ONLY to the transferred assets
- Most current sukuk structures would need restructuring

Status: Extended deadlines as of 2025; under active debate.
RISK FLAG for issuance advice: Always note the Standard 62 risk in advisory memos.

---

## MANDATORY DISCLOSURES

**AAOIFI FAS 33:**
1. Nature of sukuk structure and underlying assets
2. SSB approval and fatwa reference for the sukuk structure
3. Classification on balance sheet (liability or equity)
4. Movement in sukuk payable
5. Profit/distribution recognised in the period
6. Purchase undertaking terms
7. Compliance with AAOIFI Shariah Standard 17 (Investment Sukuk)

**IAS 32 / IFRS 7 (IFRS regime):**
1. Classification basis (liability or equity) with IAS 32 analysis
2. Maturity profile of sukuk liability
3. Finance costs recognised in the period
4. Fair value of sukuk (if different from carrying value)
5. Collateral / underlying assets description
6. Derecognition analysis — why assets remain on balance sheet

**Green / Sustainable Sukuk (additional):**
1. Use of proceeds — allocation to eligible green/social projects
2. Impact report: metrics achieved
3. Alignment with relevant framework (SC Malaysia SRI, ICMA Green Bond Principles)
