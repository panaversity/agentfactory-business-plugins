---
name: ijarah-imb
description: >
  Activate for: ijarah, IMB, ijarah muntahia bittamleek, Islamic lease,
  FAS 8, FAS 32, rental income, lease ending in ownership, operating lease Islamic,
  finance lease Islamic, right-of-use asset Islamic, IFRS 16 Islamic,
  ijarah assets, ijarah rental schedule, ijarah depreciation.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 8 (Ijarah), FAS 32 (Ijarah)"
---

## THE FUNDAMENTAL SHARIAH DISTINCTION

In ijarah, the lessor retains OWNERSHIP of the asset throughout the lease term.
The lessee pays for USUFRUCT (the right to use) — not for the asset itself.
The lessor bears the risks and rewards of ownership at all times.

This Shariah requirement is the source of the AAOIFI/IFRS divergence:

- AAOIFI: lessor keeps asset on balance sheet because Shariah says lessor owns it.
- IFRS 16: may require lessor to derecognise (finance lease) because substance
  may indicate risks/rewards have transferred to lessee.

---

## IJARAH TYPES

**Ijarah (classical operating lease):**
Pure rental. No promise of ownership transfer at end. Lessor retains asset.
AAOIFI: FAS 32 — asset on lessor's books, depreciated over useful life.
IFRS 16: Operating lease — asset on lessor's books, depreciated over useful life.
(For pure operating lease, AAOIFI and IFRS 16 lessor treatment are similar.)

**Ijarah Muntahia Bittamleek (IMB) — lease ending in ownership:**
Rental contract PLUS a separate promise (wa'd) to transfer ownership at end.
CRITICAL SHARIAH POINT: The promise of ownership transfer must be a SEPARATE
document from the lease contract. Combining them in one document may invalidate
the Shariah structure.
Transfer mechanism: gift (hibah) or nominal sale (bay').

---

## LESSOR ACCOUNTING — AAOIFI FAS 32

**Initial Recognition:**
Dr: Ijarah Assets (non-current asset) [Cost of asset]
Cr: Cash / Payable to Supplier [Cost of asset]

**Periodic Depreciation:**
Dr: Depreciation — Ijarah Assets [Cost / Useful Life of Asset]
Cr: Accumulated Depreciation — Ijarah Assets

CRITICAL: Depreciate over USEFUL LIFE of the asset, NOT over the lease term.
The lease term is irrelevant to depreciation because the lessor retains ownership.
For an IMB with a 7-year lease on an asset with a 20-year useful life:
Depreciate over 20 years, not 7 years.

**Rental Income Recognition (FAS 32):**
Dr: Accrued Rental Receivable [Monthly rental]
Cr: Ijarah Rental Income [Monthly rental]
(Recognise on straight-line basis or pattern matching usage)

**At end of IMB — Ownership Transfer (gift):**
Dr: Accumulated Depreciation [Carrying amount of accumulated depreciation]
Dr: Loss on Transfer (if any) [Remaining net book value if not fully depreciated]
Cr: Ijarah Asset [Original cost]
(Asset derecognised when ownership transfers)

**At end of IMB — Ownership Transfer (nominal sale):**
Dr: Cash [Nominal sale price, e.g., USD 1]
Dr: Accumulated Depreciation [Cumulative depreciation to date]
Dr: Loss on Transfer [Remaining net book value minus sale proceeds]
Cr: Ijarah Asset [Original cost]

---

## LESSOR ACCOUNTING — IFRS 16 (IFRS REGIMES)

**Classification test (lessor must assess):**
Is this a finance lease or operating lease?
Finance lease indicators (IFRS 16.63):

- Ownership transfers at end of lease term
- Purchase option the lessee is reasonably certain to exercise
- Lease term covers major part of economic life
- PV of payments substantially equals fair value of asset
- Asset is specialised — lessee only can use

**If OPERATING LEASE (IFRS 16):**
Same as AAOIFI treatment: asset stays on lessor's balance sheet, depreciate,
recognise rental income on straight-line basis.

**If FINANCE LEASE (IFRS 16):**
Dr: Net Investment in Lease [PV of future lease payments + unguaranteed residual]
Cr: Ijarah Asset [Carrying amount derecognised]
Cr/Dr: Gain/Loss on finance lease commencement

Monthly interest income recognition:
Dr: Accrued Receivable [Net Investment x effective interest rate / 12]
Cr: Finance Lease Income [Same amount]

IMPORTANT: For IMB assessed as IFRS 16 finance lease, the lessor DERECOGNISES
the asset. This directly contradicts AAOIFI FAS 32 which keeps asset on lessor's books.
This is the major balance sheet divergence between AAOIFI and IFRS 16 regimes.

---

## LESSEE ACCOUNTING — IFRS 16 (ALL IFRS REGIMES)

When a corporate lessee takes an ijarah or IMB from an Islamic bank,
the lessee accounts for the arrangement under IFRS 16 in their own books,
regardless of how the Islamic bank (lessor) accounts for it.

**Identify if IFRS 16 applies:**
Does the contract convey the right to control use of an identified asset? → Yes → IFRS 16.
Islamic structure does not exempt from IFRS 16. Assess on economic substance.
Exemptions: short-term leases (<=12 months), low-value asset leases.

**Initial Recognition:**
Right-of-Use (ROU) Asset = Present Value of future lease payments
(discounted at rate implicit in lease, or lessee's incremental borrowing rate)

Dr: Right-of-Use Asset [PV of lease payments]
Cr: Lease Liability [PV of lease payments]

**Monthly:**
Dr: Depreciation — ROU Asset [ROU Asset / shorter of lease term or useful life]
Cr: Accumulated Depreciation — ROU Asset

Dr: Lease Liability [Payment — Finance Charge]
Dr: Finance Charge [Opening Liability x discount rate / 12]
Cr: Cash [Monthly rental payment]

---

## INCOME LABELS

AAOIFI regime: "Ijarah Income" or "Rental Income from Ijarah"
IFRS regime (if operating lease): "Income from Islamic Financing — Ijarah"
IFRS regime (if finance lease): "Finance Income — Ijarah"
Lessee (all IFRS): "Depreciation" + "Finance Charge" (two separate P&L lines)

---

## MANDATORY DISCLOSURES

**Lessor — AAOIFI FAS 32:**

1. Ijarah assets movement table (cost, accumulated depreciation, net book value)
2. Useful life assumptions by asset class
3. Rental income recognised in the period
4. Future minimum rentals receivable (< 1 year, 1-5 years, > 5 years)
5. Shariah compliance note: ownership retained by IFI throughout lease term

**Lessor — IFRS 16 (if finance lease):**

1. Net investment in lease maturity analysis
2. Unearned finance income
3. Finance income recognised in the period
4. Reconciliation: gross investment vs. net investment

**Lessee — IFRS 16:**

1. ROU asset roll-forward by class
2. Lease liability maturity analysis
3. Total cash outflow for leases
4. Depreciation charge and finance charge for the period
5. Short-term and low-value lease expense (if exemption applied)
