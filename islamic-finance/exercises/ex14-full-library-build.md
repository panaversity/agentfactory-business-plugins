# Exercise 14: Full Islamic Finance Domain Agent — Global SKILL.md Library Build (Capstone)

## Scenario Profile

| Field                                                  | Value                                                                                           |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **Domain**                                             | Islamic Finance Agent Architecture — full library deployment                                    |
| **Scope**                                              | 25 SKILL.md files (12 product + 13 jurisdiction) + routing logic + scheduled tasks + test suite |
| **Target Time**                                        | 90 minutes across multiple sessions                                                             |
| **This is the agent-building capstone for Chapter 20** |

---

## Skills Library Inventory — 25 Files Required

### Product Skills (12 files)

| #   | File                          | Path                | Key Standards                    | Core Content                                                          |
| --- | ----------------------------- | ------------------- | -------------------------------- | --------------------------------------------------------------------- |
| 1   | `murabaha.md`                 | `/skills/products/` | AAOIFI FAS 2, IFRS 9             | Cost-plus sale, deferred payment, income recognition, journal entries |
| 2   | `ijarah-imb.md`               | `/skills/products/` | AAOIFI FAS 32, IFRS 16           | Operating lease, IMB with transfer, lessor vs. lessee accounting      |
| 3   | `musharaka-dm.md`             | `/skills/products/` | AAOIFI FAS 3, IFRS 9             | Diminishing musharaka, home finance, equity purchase mechanics        |
| 4   | `mudaraba.md`                 | `/skills/products/` | AAOIFI FAS 4, IFRS 9             | Profit-sharing, IAH fund accounting, mudarib fee                      |
| 5   | `musharaka-full.md`           | `/skills/products/` | AAOIFI FAS 3, IFRS 9             | Full partnership, joint venture, profit/loss sharing                  |
| 6   | `sukuk-issuer.md`             | `/skills/products/` | AAOIFI FAS 25/33, IFRS 9, IAS 32 | SPV structure, derecognition analysis, liability vs. equity           |
| 7   | `sukuk-investor.md`           | `/skills/products/` | AAOIFI FAS 25, IFRS 9            | Classification, SPPI test, income recognition                         |
| 8   | `salam.md`                    | `/skills/products/` | AAOIFI FAS 7, IFRS 9             | Forward sale, agricultural/commodity, parallel salam                  |
| 9   | `istisna-a.md`                | `/skills/products/` | AAOIFI FAS 10, IFRS 15           | Construction contracts, milestone billing, parallel istisna'a         |
| 10  | `takaful-ifrs17.md`           | `/skills/products/` | IFRS 17, AAOIFI                  | Wakala model, Participants' Fund, qard hasan                          |
| 11  | `zakat-global.md`             | `/skills/products/` | AAOIFI GS 9, ZATCA               | ZATCA formula, Hanafi method, by-jurisdiction rules                   |
| 12  | `shariah-screening-global.md` | `/skills/products/` | AAOIFI Std 21, MSCI              | Financial ratio screens, sector exclusions, purification              |

### Jurisdiction Overlay Skills (13 files)

| #   | File                 | Path                     | Framework                         | Key Regulator    |
| --- | -------------------- | ------------------------ | --------------------------------- | ---------------- |
| 1   | `bahrain-aaoifi.md`  | `/skills/jurisdictions/` | AAOIFI FAS mandatory              | CBB              |
| 2   | `qatar-aaoifi.md`    | `/skills/jurisdictions/` | AAOIFI FAS mandatory              | QCB              |
| 3   | `malaysia-mfrs.md`   | `/skills/jurisdictions/` | MFRS + BNM overlay                | BNM, SC Malaysia |
| 4   | `indonesia-psak.md`  | `/skills/jurisdictions/` | PSAK Islamic standards            | OJK, DSN-MUI     |
| 5   | `saudi-ifrs.md`      | `/skills/jurisdictions/` | IFRS + ZATCA zakat                | SAMA, ZATCA      |
| 6   | `uae-ifrs.md`        | `/skills/jurisdictions/` | IFRS + CBUAE                      | CBUAE            |
| 7   | `kuwait-ifrs.md`     | `/skills/jurisdictions/` | IFRS + CBK                        | CBK              |
| 8   | `oman-ifrs.md`       | `/skills/jurisdictions/` | IFRS + AAOIFI Shariah mandatory   | CBO              |
| 9   | `pakistan-ifrs.md`   | `/skills/jurisdictions/` | IFRS + SBP SGF                    | SBP              |
| 10  | `uk-ifrs.md`         | `/skills/jurisdictions/` | IFRS + HMRC + PRA/FCA             | PRA, FCA, HMRC   |
| 11  | `nigeria-ifrs.md`    | `/skills/jurisdictions/` | IFRS + CBN Non-Interest Banking   | CBN, FRCN        |
| 12  | `turkey-tfrs.md`     | `/skills/jurisdictions/` | TFRS + BDDK participation banking | BDDK, CMB        |
| 13  | `gcc-crossborder.md` | `/skills/jurisdictions/` | Multi-jurisdiction GCC rules      | Multiple         |

---

## Global Routing Master SKILL.md Specification

```yaml
---
name: islamic-finance-global-router
description: >
  Activate whenever any Islamic finance term appears in a query:
  murabaha, ijarah, musharaka, mudaraba, sukuk, takaful, zakat,
  AAOIFI, FAS, Shariah-compliant, Islamic banking, non-interest banking,
  halal finance, riba, gharar.
  Before any output: identify jurisdiction and product, then load
  appropriate product SKILL.md and jurisdiction overlay SKILL.md.
---
```

### Routing Rules

| Step | Action                    | Rule                                                                                                                                              |
| ---- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Identify jurisdiction     | If none specified: ASK before proceeding. NEVER assume IFRS                                                                                       |
| 2    | Map to framework          | AAOIFI mandatory: Bahrain, Qatar, Sudan. MFRS: Malaysia. IFRS: UAE, Saudi, Kuwait, Oman, UK, Nigeria, Kenya, Turkey                               |
| 3    | Identify product          | Load corresponding product SKILL.md                                                                                                               |
| 4    | Load jurisdiction overlay | Apply jurisdiction-specific modifications                                                                                                         |
| 5    | Pre-output checks         | Confirm governing standard in header. Label income per jurisdiction. NEVER use "interest income." NEVER use "loans and advances" in AAOIFI regime |

---

## Test Suite — 13 Queries (One Per Jurisdiction)

| #   | Test Query                                                 | Expected Jurisdiction        | Expected Product Skill | Key Verification                              |
| --- | ---------------------------------------------------------- | ---------------------------- | ---------------------- | --------------------------------------------- |
| 1   | "Account for a murabaha receivable for our Bahrain entity" | Bahrain (AAOIFI)             | murabaha.md            | Labels: "Murabaha Income," AAOIFI FAS 2 cited |
| 2   | "Book the ijarah income for our Qatar subsidiary"          | Qatar (AAOIFI)               | ijarah-imb.md          | AAOIFI FAS 32, "Income from Ijarah"           |
| 3   | "Generate the sukuk journal for our Malaysian portfolio"   | Malaysia (MFRS)              | sukuk-investor.md      | "Profit from Islamic Financing," MFRS 9       |
| 4   | "Calculate zakat for our Saudi bank"                       | Saudi (IFRS + ZATCA)         | zakat-global.md        | ZATCA formula, NOT Hanafi method              |
| 5   | "How should we classify the home finance under UAE IFRS?"  | UAE (IFRS)                   | musharaka-dm.md        | IFRS 9 classification, CBUAE reference        |
| 6   | "Record the mudaraba profit distribution in Kuwait"        | Kuwait (IFRS)                | mudaraba.md            | IFRS, CBK reference                           |
| 7   | "Account for our Oman branch's musharaka investment"       | Oman (IFRS + AAOIFI Shariah) | musharaka-full.md      | IFRS accounting, AAOIFI Shariah governance    |
| 8   | "Prepare the SBP return for our Pakistan Islamic bank"     | Pakistan (IFRS + SBP)        | Multiple               | SBP Shariah Governance Framework              |
| 9   | "Generate the HMRC tax note for Al Rayan's DM portfolio"   | UK (IFRS + HMRC)             | musharaka-dm.md        | HMRC Alternative Finance Arrangements, PRA    |
| 10  | "Book the FGN sukuk income for Jaiz Bank"                  | Nigeria (IFRS + CBN)         | sukuk-investor.md      | CBN Non-Interest Banking Framework            |
| 11  | "Account for our participation banking income in Turkey"   | Turkey (TFRS)                | murabaha.md            | TFRS, BDDK participation banking              |
| 12  | "Prepare the takaful IFRS 17 statements for Indonesia"     | Indonesia (PSAK)             | takaful-ifrs17.md      | PSAK Islamic, OJK reference                   |
| 13  | "Consolidate our GCC banking group across 4 countries"     | GCC cross-border             | gcc-crossborder.md     | AAOIFI parent + IFRS subs, IAH treatment      |

---

## Scheduled Task Specifications

### Daily Tasks

| Task                        | Trigger             | Skill File        | Output                       |
| --------------------------- | ------------------- | ----------------- | ---------------------------- |
| Murabaha profit recognition | End of business day | murabaha.md       | Daily income accrual entries |
| Ijarah rental recognition   | End of business day | ijarah-imb.md     | Daily rental income entries  |
| Sukuk income accrual        | End of business day | sukuk-investor.md | Daily distribution accrual   |

### Monthly Tasks

| Task                     | Trigger   | Skill File                  | Output                                        |
| ------------------------ | --------- | --------------------------- | --------------------------------------------- |
| Profit pool distribution | Month-end | mudaraba.md                 | IAH profit distribution calculation + entries |
| Zakat monitoring         | Month-end | zakat-global.md             | Minimum balance tracking, accrual update      |
| Shariah income check     | Month-end | shariah-screening-global.md | Non-Shariah income % check, charity payable   |

### Quarterly Tasks

| Task                     | Trigger               | Skill File                  | Output                                          |
| ------------------------ | --------------------- | --------------------------- | ----------------------------------------------- |
| Shariah portfolio screen | Quarter-end + 5 days  | shariah-screening-global.md | Full portfolio screening with divergence report |
| SSB quarterly report     | Quarter-end + 10 days | shariah-screening-global.md | Compliance status, purification, actions        |

### Annual Tasks

| Task                       | Trigger  | Skill File                             | Output                                        |
| -------------------------- | -------- | -------------------------------------- | --------------------------------------------- |
| AAOIFI-IFRS reconciliation | Year-end | bahrain-aaoifi.md + gcc-crossborder.md | Full reconciliation for dual-framework groups |

---

## Your Task

1. **Audit the skills inventory**: Confirm all 25 files are listed. Identify any gaps in product or jurisdiction coverage
2. **Build the global routing master SKILL.md**: Implement the routing rules with jurisdiction detection, product matching, and pre-output validation
3. **Method A knowledge extraction for murabaha (AAOIFI)**: Interview yourself on the 3 most common FAS 2 errors, Shariah compliance conditions, and murabaha receivable aging review checks. Convert to SKILL.md instructions
4. **Method B document analysis for jurisdiction overlays**: For each of the 13 jurisdiction files, extract key accounting and disclosure rules from regulatory sources into SKILL.md format
5. **Deploy scheduled tasks**: Configure all daily, monthly, quarterly, and annual tasks
6. **Run 13-query test suite**: Execute all test queries, verify correct routing and labelling per jurisdiction
7. **Document the capability statement**: Produce a one-page agent capability statement for client engagements

---

## Expected Output

- Complete inventory checklist (25 files, all accounted for)
- Global routing SKILL.md (deployable)
- murabaha.md product skill (complete, with AAOIFI and IFRS sections)
- 13 jurisdiction overlay skills (at minimum: key standards, labels, regulator, disclosure requirements)
- Scheduled task configuration (10 tasks across 4 frequencies)
- Test results (13/13 pass with correct routing)
- One-page capability statement ending with the SSB judgment paragraph
