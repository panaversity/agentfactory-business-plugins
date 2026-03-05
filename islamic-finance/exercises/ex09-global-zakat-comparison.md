# Exercise 9: Global Zakat — Institutional Calculation Across Jurisdictions

## Scenario Profile

| Field               | Value                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Domain**          | Zakat Accounting — Global comparison                                                                          |
| **Jurisdictions**   | Saudi Arabia (ZATCA), Malaysia (voluntary AAOIFI/Hanafi), Pakistan (Zakat and Ushr Ordinance), UK (voluntary) |
| **Target Time**     | 40 minutes                                                                                                    |
| **Skills Required** | `zakat-global.md`, `saudi-ifrs.md`, `malaysia-mfrs.md`, `pakistan-ifrs.md`, `uk-ifrs.md`                      |

---

## Zakat Framework Comparison

| Dimension            | Saudi Arabia                   | Malaysia                     | Pakistan                               | UK                           |
| -------------------- | ------------------------------ | ---------------------------- | -------------------------------------- | ---------------------------- |
| Legal basis          | ZATCA mandatory                | Voluntary (fatwa-based)      | Zakat & Ushr Ordinance 1980            | Entirely voluntary           |
| Calculation method   | ZATCA balance sheet formula    | Hanafi net zakatable assets  | Deduction at source + self-assessment  | AAOIFI GS 9 or Hanafi        |
| Rate                 | 2.5%                           | 2.5%                         | 2.5% (deduction at source on deposits) | 2.5%                         |
| Filing deadline      | 120 days after fiscal year-end | Per Shariah board resolution | 1st Ramadan (lunar calendar)           | Per Shariah board resolution |
| Regulator            | ZATCA                          | None (voluntary)             | Central Zakat Fund / SBP               | None                         |
| Accounting treatment | P&L expense                    | \_\_\_                       | \_\_\_                                 | \_\_\_                       |

---

## IFI 1: Al Rajhi Bank (Saudi Arabia)

### Balance Sheet Extract (SAR millions)

| Item                       | Amount     | Zakat Base Treatment |
| -------------------------- | ---------- | -------------------- |
| Share capital              | 40,000     | Include              |
| Retained earnings          | 28,000     | Include              |
| Statutory reserves         | 18,000     | Include              |
| General provisions         | 3,500      | Include              |
| **Gross zakat base**       | **89,500** |                      |
| Fixed assets (net)         | (6,000)    | Deduct               |
| Long-term investments      | (45,000)   | Deduct               |
| **Net ZATCA zakat base**   | **38,500** |                      |
| Zakat rate                 | 2.5%       |                      |
| **ZATCA zakat obligation** | **962.5**  |                      |

**ZATCA formula**: (Share capital + Reserves + Retained earnings + Provisions) - (Fixed assets + Long-term investments) x 2.5%

**Note**: ZATCA zakat generally replaces income tax for Saudi-owned entities.

---

## IFI 2: Maybank Islamic Berhad (Malaysia)

### Balance Sheet Extract (MYR millions)

| Item                                 | Amount                       | Zakatable? |
| ------------------------------------ | ---------------------------- | ---------- |
| Cash and equivalents                 | 12,000                       | Yes        |
| Murabaha receivables (net)           | 85,000                       | Yes        |
| Sukuk investments                    | 32,000                       | Yes        |
| **Total zakatable assets**           | **129,000**                  |            |
| Fixed assets (net)                   | 4,000                        | No         |
| Long-term equity investments         | 8,000                        | No         |
| **Total non-zakatable assets**       | **12,000**                   |            |
| Current liabilities                  | 45,000                       | Deduct     |
| **Net zakatable wealth**             | **84,000**                   |            |
| Nisab check                          | MYR 25,000 (gold equivalent) | Exceeded   |
| Zakat rate                           | 2.5%                         |            |
| **Zakat obligation (Hanafi method)** | **2,100**                    |            |

**Hanafi formula**: (Zakatable assets - Current liabilities) x 2.5%

**Note**: Voluntary — paid under fatwa approved by Maybank Islamic's Shariah Supervisory Board. Treated as appropriation of profit, not P&L expense.

---

## IFI 3: Meezan Bank (Pakistan)

### Balance Sheet Extract (PKR millions)

| Item                              | Amount                         | Notes                                |
| --------------------------------- | ------------------------------ | ------------------------------------ |
| Savings deposits (Islamic)        | 485,000                        | Subject to zakat deduction at source |
| Investment accounts               | 320,000                        | Subject to zakat deduction at source |
| Current accounts                  | 215,000                        | Exempt (no return)                   |
| **Deposits subject to deduction** | **805,000**                    |                                      |
| Deduction rate                    | 2.5% of balance on 1st Ramadan |                                      |
| **Zakat collected as agent**      | **20,125**                     |                                      |
| Bank's own institutional zakat    | Separate self-assessment       |                                      |

### Pakistan Zakat Collection Mechanics

| Step                   | Action                                           | Amount               |
| ---------------------- | ------------------------------------------------ | -------------------- |
| 1st Ramadan            | Deduct 2.5% from eligible accounts               | PKR 20,125M          |
| Within 30 days         | Remit to Central Zakat Fund                      | PKR 20,125M          |
| Exemption applications | CZF exemption certificates (Shia, other schools) | Varies               |
| Bank's own zakat       | Self-assessed per Shariah board                  | Separate calculation |

---

## IFI 4: Gatehouse Bank (UK)

### Balance Sheet Extract (GBP millions)

| Item                          | Amount     | Notes         |
| ----------------------------- | ---------- | ------------- |
| Cash and equivalents          | 85         | Zakatable     |
| Islamic financing receivables | 420        | Zakatable     |
| Sukuk investments             | 150        | Zakatable     |
| **Total zakatable assets**    | **655**    |               |
| Fixed assets                  | 12         | Non-zakatable |
| Current liabilities           | 180        | Deduct        |
| **Net zakatable wealth**      | **475**    |               |
| Zakat rate                    | 2.5%       |               |
| **Zakat obligation**          | **11.875** |               |

**Note**: Entirely voluntary. No UK regulatory requirement. Disclosed in notes to financial statements only. Per Shariah board resolution, treated as footnote disclosure — not P&L expense, not equity appropriation.

---

## Your Task

1. **Build a global zakat comparison framework**: Complete the comparison table (fill in accounting treatment column for Malaysia, Pakistan, UK). Build a single workbook with one tab per jurisdiction
2. **Saudi ZATCA zakat**: Verify the Al Rajhi calculation. Generate journal entry (Dr Zakat Expense, Cr Zakat Payable). Note ZATCA-vs-income-tax interaction
3. **Malaysia voluntary zakat**: Verify the Maybank calculation. Draft the zakat disclosure note for the annual report. Note this is appropriation, not expense
4. **Pakistan Zakat and Ushr**: Generate the bank-as-agent journal entries for: collection, remittance to Central Zakat Fund. Note exemption certificate mechanics
5. **Build global zakat SKILL.md**: Draft the skill file covering all four jurisdictions with: mandatory vs. voluntary, formula, P&L vs. equity vs. footnote, journal entry sequence, disclosure content, trigger conditions

---

## Expected Output

- Completed comparison table across all four jurisdictions
- 4 sets of journal entries (one per jurisdiction)
- Disclosure note draft for Malaysia (voluntary zakat)
- Pakistan agent collection entries (distinct from institutional zakat)
- Draft zakat SKILL.md with jurisdiction routing logic
- Key insight: ZATCA equity-based formula vs. Hanafi liquid-assets formula produce materially different obligations for the same bank profile
