---
name: zakat-global
description: >
  Activate for: zakat, zakatable assets, nisab, zakat calculation,
  institutional zakat, ZATCA zakat, zakat and ushr, sadaqah,
  non-Shariah income purification, charity payable Islamic,
  zakat on bank accounts, zakat disclosure, zakat journal entry.
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
  standard: "AAOIFI FAS 9 (Zakah), ZATCA Regulations (KSA)"
---

## THE GLOBAL ZAKAT LANDSCAPE

Zakat is the obligatory Islamic alms payment — 2.5% of qualifying wealth above the nisab threshold,
calculated on a lunar year basis (354 days). Its treatment for Islamic financial institutions
varies significantly by jurisdiction.

---

## JURISDICTION SUMMARY TABLE

| Jurisdiction | Mandatory? | Formula | Rate | Payer | Filing |
|---|---|---|---|---|---|
| Saudi Arabia | Mandatory (ZATCA) | ZATCA equity-based formula | 2.5% p.a. | IFI pays to ZATCA | Annual ZATCA return |
| Pakistan | Mandatory (deduction at source) | Deduction on savings accounts | 2.5% on qualifying accounts | Bank deducts as agent | 1st Ramadan each year |
| Bahrain | Voluntary (institutional) | AAOIFI GS9 / Hanafi | 2.5% p.a. | IFI may pay on behalf of shareholders | Annual disclosure |
| Malaysia | Voluntary | AAOIFI GS9 / Hanafi or Shafi'i | 2.5% p.a. | IFI voluntary; disclose | Annual disclosure |
| UAE | Voluntary | AAOIFI GS9 | 2.5% p.a. | IFI voluntary; disclose | Annual disclosure |
| UK | Not applicable | N/A | N/A | Individual obligation only | N/A |
| Nigeria | Voluntary | AAOIFI GS9 | 2.5% p.a. | Voluntary | Annual disclosure |

---

## THE NISAB THRESHOLD

The nisab is the minimum wealth threshold above which zakat becomes obligatory.
Two measures, take the lower (traditionally silver nisab is used for financial assets):

**Gold nisab:** Equivalent of 87.48 grams of gold (at current gold price)
**Silver nisab:** Equivalent of 612.36 grams of silver (at current silver price)

Check the current gold/silver price to calculate the nisab in local currency.
For Islamic banks with large balance sheets: the nisab is almost always exceeded.
Still check and document the check annually.

**Lunar year minimum balance rule:**
Zakat is payable on the MINIMUM BALANCE of zakatable wealth
maintained continuously throughout the lunar year — not the year-end balance.
If wealth fell below nisab at any point during the year, recalculate from that point.

---

## FORMULA 1: HANAFI / AAOIFI GS9 (MOST JURISDICTIONS)

**Step 1 — Identify zakatable assets:**
ZAKATABLE (trade wealth and liquid assets):
+ Cash and near-cash
+ Trade receivables (murabaha receivables, DM receivables net of provisions)
+ Inventory / commodities held for trade
+ Short-term investments and sukuk classified as trading / short-term
+ Mudaraba and musharaka investments intended for profit
+ Salam receivables

NOT ZAKATABLE (productive fixed assets / long-term investments):
- Fixed assets (property, plant, equipment used in operations)
- Ijarah assets on IFI's books (productive, not trade goods)
- Long-term strategic investments
- Goodwill and intangibles

**Step 2 — Identify current liabilities due within the lunar year:**
- Payables to suppliers
- Short-term borrowings
- Dividends payable
- Tax payable

**Step 3 — Calculate Zakat Base:**
Zakat Base = Zakatable Assets - Current Liabilities

**Step 4 — Apply nisab check and calculate zakat:**
If Zakat Base > Nisab: Zakat = Zakat Base x 2.5%
If Zakat Base <= Nisab: No zakat payable (unlikely for a bank)

---

## FORMULA 2: ZATCA (SAUDI ARABIA)

Saudi Arabia's Zakat, Tax and Customs Authority uses a different formula:

**Zakat Base = Share Capital + Retained Earnings + Statutory Reserves + Other Reserves
            - Fixed Assets - Long-term Investments - Unamortised Expenses**

This is an EQUITY-BASED formula — it starts from equity, not from liquid assets.

Apply the Saudi jurisdiction overlay for ZATCA-specific line-item mapping.

Note: For Saudi IFIs, ZATCA zakat REPLACES income tax for Saudi-owned companies.
Foreign-owned portions of the bank pay income tax; Saudi-owned portions pay zakat.
Ensure correct proportional calculation if the bank has mixed Saudi/foreign ownership.

---

## FORMULA 3: PAKISTAN — ZAKAT AND USHR ORDINANCE 1980

Pakistan's Zakat and Ushr Ordinance requires banks to DEDUCT ZAKAT AT SOURCE:

**From which accounts:** Savings accounts, Profit and Loss Sharing (PLS) accounts,
and other qualifying deposit accounts.

**When:** On the first day of Ramadan each lunar year.

**Rate:** 2.5% of the account balance on that date (if balance >= nisab threshold).

**Exemptions:** Account holders may claim exemption by submitting a declaration form.

**The bank's role:** The bank is an AGENT (wakeel) for the Central Zakat Administration.
The bank deducts zakat from each qualifying account and remits it to the Zakat Fund.

**Journal entry in bank's books:**
On deduction date:
Dr: Depositor's Account [Zakat amount]
Cr: Zakat Payable — Central Zakat Administration [Zakat amount]

On remittance to Zakat Fund:
Dr: Zakat Payable — Central Zakat Administration [Zakat amount]
Cr: Cash / Remittance Account [Zakat amount]

Note: This is NOT the IFI's own zakat — it is a DEDUCTION ON BEHALF OF depositors.
Do not recognise as the IFI's expense. Merely a pass-through.

---

## NON-SHARIAH INCOME PURIFICATION (ALL JURISDICTIONS)

When an IFI receives income from non-Shariah-compliant sources:
Examples: penalty charges that cannot be retained, inadvertent interest income,
conventional bank income during conversion, dividend from a company with >5% non-halal income.

**This income CANNOT be retained by the IFI.**
It must be donated to charity (sadaqah) — it is not a deductible expense for zakat purposes.

**Journal entry:**
Dr: Non-Shariah Income Received [Amount]
Cr: Charity Payable — Purification [Amount]

On payment to charity:
Dr: Charity Payable — Purification [Amount]
Cr: Cash [Amount]

**In the income statement:** Show as a separate line "Purification / Charity Donation"
NOT as operating income of the IFI.

**In AAOIFI disclosures:** Mandatory disclosure of non-Shariah income amount and
the charity to which it was donated, confirmed by SSB review.

---

## MANDATORY DISCLOSURES

1. Whether zakat is paid by the institution or is the individual obligation of shareholders
2. The calculation basis adopted (ZATCA / Hanafi / Shafi'i / other) — per SSB fatwa
3. Zakat base amount
4. Zakat paid (or accrued if not yet paid)
5. Non-Shariah income received and purification amount donated
6. Charity / sadaqah paid — recipient and amount

For ZATCA (Saudi Arabia): zakat return filing reference number.
For Pakistan: aggregate zakat deducted from depositors and remitted.
