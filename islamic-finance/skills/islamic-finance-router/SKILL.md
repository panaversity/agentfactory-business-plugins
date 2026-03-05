---
name: islamic-finance-router
description: >
  Routes Islamic finance queries to the correct product skill and jurisdiction
  overlay. Activate for any query involving Islamic banking, AAOIFI, Shariah-
  compliant finance, sukuk, takaful, murabaha, ijarah, musharaka, mudaraba,
  salam, istisna'a, zakat, or Shariah screening. Covers 20 jurisdictions
  across 3 accounting regimes (AAOIFI-primary, IFRS with Islamic guidance,
  local standards).
---

$(cat "/Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag2/specs/chapter 20 islamic finance/islamic-finance-skills/islamic-finance-global-router.md" | tail -n +16)

## Jurisdiction Overlays

When a jurisdiction is identified, load the appropriate overlay:

- [Bahrain (AAOIFI)](references/jurisdictions/bahrain-aaoifi.md)
- [Qatar (AAOIFI)](references/jurisdictions/qatar-aaoifi.md)
- [Malaysia (MFRS)](references/jurisdictions/malaysia-mfrs.md)
- [Saudi Arabia (IFRS)](references/jurisdictions/saudi-ifrs.md)
- [UAE (IFRS)](references/jurisdictions/uae-ifrs.md)
- [UK (IFRS)](references/jurisdictions/uk-ifrs.md)
- [Kuwait (IFRS)](references/jurisdictions/kuwait-ifrs.md)
- [Oman (IFRS)](references/jurisdictions/oman-ifrs.md)
- [Pakistan (IFRS)](references/jurisdictions/pakistan-ifrs.md)
- [Indonesia (PSAK)](references/jurisdictions/indonesia-psak.md)
- [Nigeria (IFRS)](references/jurisdictions/nigeria-ifrs.md)
- [Turkey (TFRS)](references/jurisdictions/turkey-tfrs.md)
- [GCC Cross-Border](references/jurisdictions/gcc-crossborder.md)
