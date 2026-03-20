---
name: bank-reconciliation
description: >
  Activate for: bank reconciliation, nostro reconciliation, suspense account,
  GL reconciliation, provision reconciliation, inter-company reconciliation,
  nostro break, unmatched item, reconciling item, MT940, MT950, MT942,
  aged items, reconciliation certificate, suspense clearing, four-way
  reconciliation, IFRS 9 provision reconciliation, settlement break,
  trade reconciliation, position break, GL-to-risk reconciliation.
  NOT for: IFRS 9 ECL model calculation (use ifrs9-ecl), capital adequacy
  reporting (use basel-capital), AML transaction monitoring (use aml-typologies).
metadata:
  version: "1.0"
  author: "Panaversity — The AI Agent Factory"
---

## RECONCILIATION TYPES — LOAD THE RIGHT CONTEXT

| Task Description               | Use This Context                                 |
| ------------------------------ | ------------------------------------------------ |
| Nostro / correspondent account | sections: NOSTRO, AGEING SLA, MATCHING HIERARCHY |
| IFRS 9 provision GL tie-out    | sections: FOUR-WAY RECON, P&L TIE-OUT            |
| Suspense account clearance     | sections: SUSPENSE, AGEING SLA, WRITE-OFF        |
| Inter-company / inter-branch   | sections: INTERCO, AGEING SLA                    |
| Trade / securities settlement  | sections: TRADE SETTLEMENT, AGEING SLA           |
| Full financial close           | ALL sections                                     |

---

## MATCHING HIERARCHY — APPLY IN THIS EXACT ORDER

Step 1 — EXACT MATCH
Criteria: amount = amount AND value date = value date AND reference = reference
Action: Auto-clear. No human review required. Log as matched.

Step 2 — FUZZY MATCH
Criteria: amount = amount AND value date = value date AND reference partially matches
(truncated, reformatted, leading zeros stripped, SWIFT truncation applied)
Action: Auto-clear with exception note. Flag for daily exception report review.

Step 3 — DATE TOLERANCE MATCH
Criteria: amount = amount AND reference matches AND value date within ±2 business days
Action: Auto-clear with timing difference notation. Post value date correction if needed.

Step 4 — PARTIAL SUM POOL
Criteria: Multiple items on one side aggregate to a single item on the other side
(common in retail settlement aggregation, netting arrangements)
Action: Group items into pool. Present to human analyst for confirmation before clearing.

Step 5 — UNMATCHED RESIDUAL
Criteria: No rule above is satisfied
Action: Generate investigation hypothesis (see BREAK INVESTIGATION below).
Queue for analyst with hypothesis, probability estimate, and recommended action.

---

## BREAK CLASSIFICATION

Mirror item only (no external statement item):
→ TIMING DIFFERENCE: Payment sent / instructed but not yet appearing on statement
Probability: High for items ≤ 2 business days
Action: Monitor for settlement; query counterparty if aged > 3 days
→ PAYMENT FAILURE / REJECTION: Payment rejected by correspondent, no credit applied
Probability: Rises sharply after 2 days with no statement match
Action: Check SWIFT gpi tracker; request SWIFT MT199 status query

Statement item only (no internal mirror item):
→ UNBOOKED RECEIPT: Inbound credit not yet identified and posted in internal systems
Action: Move to Payment Suspense immediately; search expected inbound payment pipeline
→ UNEXPECTED DEBIT: Correspondent fee, charge, or debit not anticipated in mirror
Action: Verify legitimacy of charge; post to bank charges or dispute

Amount mismatch (reference and date match, amounts differ):
→ CORRESPONDENT FEE: Correspondent deducted charges from payment amount (SHA/OUR confusion)
Action: Post difference to bank charges; close break
→ FX ROUNDING: Currency conversion rounding difference (typically < USD 5)
Action: Post to FX rounding account; close break
→ PARTIAL PAYMENT: Counterparty paid less than full amount
Action: Post partial receipt; raise query for remainder; assess credit risk impact

Duplicate:
→ SYSTEMS PROCESSING ERROR: Same instruction processed twice
Action: Reverse the duplicate posting; investigate root cause; log as operational risk event

---

## AGEING SLA ENFORCEMENT

Apply to ALL reconciliation types. Escalation is automatic — do not wait to be asked.

| Age       | Action                                                                                 | Escalation Recipient     |
| --------- | -------------------------------------------------------------------------------------- | ------------------------ |
| 0–2 days  | Auto-match window. Monitor only.                                                       | None                     |
| 3–5 days  | Notify account owner. Initiate investigation.                                          | Account owner            |
| 6–15 days | Formal counterparty query. Head of Operations alert.                                   | Head of Operations       |
| > 15 days | Finance Controller alert. P&L provision assessment.                                    | Finance Controller / CFO |
| > 30 days | Write-off assessment. Operational risk event log. Regulatory notification if material. | CFO + Head of Compliance |

---

## NOSTRO-SPECIFIC RULES

1. Every open nostro break must appear on the daily nostro break report with:
   - Break type classification
   - Age in business days
   - Investigation status and next action
   - Owner name and date assigned

2. Unidentified credits must be moved to a named suspense account within 24 hours.
   Never leave an unidentified credit sitting unallocated in the nostro mirror.

3. SWIFT gpi (global payments innovation) tracker should be checked for all mirror-only
   items before raising a formal query. The gpi tracker shows real-time payment status
   and eliminates the majority of correspondent queries for recent payments.

4. Large nostro breaks (above materialiy threshold, typically > USD 500,000 equivalent):
   notify the Treasurer and Head of Correspondent Banking regardless of age.

---

## IFRS 9 PROVISION — FOUR-WAY RECONCILIATION

Required at every reporting date (quarterly minimum). BLOCK CLOSE if any tier disagrees.

TIER 1 — ECL Model Output
Source: IFRS 9 ECL model run approved by the IFRS 9 Governance Committee
This is the source of truth. All other tiers must reconcile to Tier 1.

TIER 2 — Risk System Facility Sum
Source: Sum of all individual facility-level ECL amounts in the credit risk system
Must equal Tier 1 after model output is uploaded to the risk system.
Common break causes: Upload error; timing cut-off; new facilities booked after model run

TIER 3 — GL Provision Account Balance
Source: Balance on the IFRS 9 provision / allowance account in the general ledger
Must equal Tier 2. All journal entries affecting the provision must be posted.
Common break causes:
Write-off processed in source system before GL journal is posted
PMA approved by committee but GL journal contains data entry error
Manual override posted to GL without corresponding update in risk system
FX translation posted to GL but not reflected in risk system

TIER 4 — Financial Statement Disclosure
Source: IFRS 7 stage distribution table and net loan balance note
Must equal Tier 3. Disclosure note must be extracted from GL, not from earlier risk export.
Common break causes: Disclosure drafted from stale risk system extract; manual edit error

CHECK: Any difference between adjacent tiers must be traced to a specific root cause,
resolved with a documented journal entry or system correction, and re-confirmed
before the four-way reconciliation certificate is signed.

---

## PROVISION MOVEMENT TIE-OUT (P&L RECONCILIATION)

Must be performed at every reporting date alongside the four-way balance reconciliation:

Opening ECL provision (GL — prior period closing balance) £M

- Impairment charge for the period (income statement — credit line) £M

* Write-offs during the period (gross balance AND provision removed) (£M)

- Recoveries on previously written-off amounts £M
  +/- FX translation on foreign currency provisions £M
  +/- Other movements (interest unwind on Stage 3, etc.) £M
  = Closing ECL provision (GL — current period) £M

This MUST equal Tier 3 of the four-way reconciliation.
Any unexplained difference: escalate to Finance Controller. BLOCK CLOSE until resolved.

NOTE ON WRITE-OFFS: A write-off removes both the gross loan balance AND the provision
from the balance sheet simultaneously — it is a balance sheet derecognition, not a P&L
charge (the P&L charge was taken when the provision was first created). The provision
movement table shows write-offs as a release of provision (negative) to match the
balance sheet reduction. Correctly distinguishing write-offs from P&L charges is the
most common error in provision movement reconciliations.

---

## SUSPENSE ACCOUNT CONTROL

Rules that apply to ALL suspense accounts:

1. Every suspense account has a named owner. Unowned suspense = immediate control finding.
2. Items must be cleared within the SLA (see AGEING SLA above).
3. Month-end zero balance target. Material balances at reporting dates = audit finding.
4. Items > 30 days that cannot be cleared must be:
   a) Documented with full investigation history
   b) Approved by CFO for write-off to P&L
   c) Logged as an operational risk loss event
   d) Reported in the bank's operational risk loss database

SUSPENSE ACCOUNT CLEARANCE ACTIONS:

Inbound payment / beneficiary unknown:
Post to Payment Suspense within 24 hours
Search for matching expected inbound in payments pipeline
Contact correspondent for remitter details if no match in 24 hours
If no resolution in 5 days: contact any potential corporate customers about expected receipts
If no resolution in 30 days: regulatory obligation may require return of funds to sender

Duplicate payment:
Reverse the duplicate posting
Send recall instruction to correspondent via SWIFT MT192
Log as operational risk event (erroneous outward payment)
Monitor for return of funds

FX rounding / small difference:
Post to FX rounding account or bank charges account
No investigation required if < materiality threshold (define in bank policy)

Trade settlement break:
Confirm with custodian whether settlement has occurred in CSD (CREST, Euroclear, etc.)
If unsettled: investigate with counterparty; assess whether trade will fail
Settlement failure: notify front office; calculate cost of fail (penalty or opportunity cost)

---

## NEVER DO THESE

- NEVER leave nostro breaks > 5 days without a formal counterparty query on file
- NEVER leave unidentified credits in the nostro mirror — move to Payment Suspense within 24 hours
- NEVER allow the GL provision account to differ from the risk system total at reporting date
- NEVER post manual journals to IFRS 9 provision accounts without IFRS 9 Governance Committee approval
- NEVER clear a break by forcing a match without a documented rationale for the match
- NEVER allow suspense items > 30 days without a documented escalation and write-off assessment on file
- NEVER produce a reconciliation certificate with unexplained differences
- NEVER confuse a write-off (balance sheet derecognition) with an impairment charge (P&L event)

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN REGULATORY FILINGS OR BUSINESS DECISIONS.
