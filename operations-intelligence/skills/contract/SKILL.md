---
name: contract
description: >
  Activate for: contract, contract review, contract analysis, contract
  obligation, extract obligations, SLA contract, vendor contract, supplier
  agreement, master service agreement, MSA, SOW, statement of work,
  NDA, non-disclosure, contract terms, auto-renewal clause, notice period
  contract, indemnity, liability cap, penalty clause, contract risk,
  contract summary, contract management, contract lifecycle, contract
  negotiation points, key terms, unfavourable terms, obligation extraction.
  NOT for: vendor evaluation or vendor scoring (use official /vendor-review),
  compliance obligation mapping (use official compliance-tracking auto-skill),
  invoice reconciliation or payment disputes (use supply-chain plugin).
license: Apache-2.0
metadata:
  author: Panaversity
  version: "1.0"
  plugin-commands: "/contract"
  mcp-integrations: "Contract repository, document store, calendar"
---

## UNIVERSAL RULES (apply to every contract task)

- NEVER summarise a contract without flagging auto-renewal clauses --
  these are the clauses that most often cause unintended commitments
- NEVER extract SLAs without extracting the credit/remedy for breach --
  an SLA without a consequence is a target, not a commitment
- NEVER produce a contract summary as legal advice -- explicitly note
  that material decisions should be reviewed by legal counsel
- ALWAYS include specific recommended actions with deadlines in every
  output -- observations without actions are not acceptable
- ALWAYS load ops.local.md for vendor portfolio context and procurement
  approval thresholds

## MANDATORY OUTPUT HEADER

Every output must begin with:

```
TASK:          [e.g. Contract Analysis -- Vendor X MSA]
DOCUMENT TYPE: [Obligation Extract / Risk Analysis / Summary / Renewal Input]
CONFIGURATION: [Loaded: ops.local.md / Not configured]
DATE:          [Date of output]
OWNER:         [Named person responsible]
```

## CONTRACT ANALYSIS WORKFLOW

### Task Type 1: OBLIGATION EXTRACTION

Purpose: Extract every obligation, SLA, key date, and key term from
a contract into a structured, searchable format.

Input: Contract text (paste or attach)
Output: Structured obligation table + SLA table + key dates + risk flags

```
CONTRACT OBLIGATIONS: [Vendor / Agreement name]
Contract date: [Date] | Effective: [Date] | Expires: [Date]
================================================================

OUR OBLIGATIONS:
| # | What we must do | By when / How often | Consequence if breached |
|---|---|---|---|
| [N] | [Specific obligation] | [Deadline/frequency] | [Consequence] |

VENDOR OBLIGATIONS:
| # | What vendor must do | Metric | Consequence |
|---|---|---|---|
| [N] | [SLA or obligation] | [Target] | [Credit / termination right] |

KEY DATES:
| Date | Event | Notice required | Action needed |
|---|---|---|---|
| [Date] | [e.g. Auto-renewal] | [N days notice] | [Action] |
| [Date] | [e.g. Price review] | [N days] | [Action] |
| [Date] | [e.g. Annual SLA review] | -- | [Review meeting] |

SLA TABLE:
| Metric | Target | Measurement | Reporting | Credit if breached |
|---|---|---|---|---|
| [Uptime] | [99.9%] | [Monthly] | [Vendor reports by 5th] | [X% monthly fee] |

AUTO-RENEWAL FLAGS:
[Clause text; date; notice period required to prevent; notice method]
================================================================
```

### Task Type 2: RISK FLAGGING

Purpose: Identify clauses that are unfavourable or create elevated risk.

SIX RISK FLAG CATEGORIES:

FLAG 1: AUTO-RENEWAL TRAPS
Clause: Contract auto-renews with [N] days' notice required to cancel
Risk: Missing the notice window commits to another full contract term
Action: Add to renewal calendar; set alert at notice date minus 30 days

FLAG 2: LIABILITY CAPS
Clause: Vendor liability capped at [amount or period of fees]
Risk: If vendor failure causes loss exceeding cap, recovery is limited
Action: Assess whether cap is adequate relative to operational dependency

FLAG 3: PRICE ESCALATION
Clause: Annual price increase of [N]% or CPI, whichever is higher
Risk: Budgets set at today's price understate future obligation
Action: Model 3-year cost trajectory; include in renewal negotiation

FLAG 4: UNILATERAL CHANGE RIGHTS
Clause: Vendor may change terms / pricing with [N] days' notice
Risk: Terms can change without your agreement
Action: Counter-negotiate to require mutual agreement for material changes

FLAG 5: TERMINATION FOR CONVENIENCE
Clause: Either party may terminate with [N] days' notice (or vendor only)
Risk: If one-sided in vendor's favour, dependency risk is elevated
Action: Ensure exit plan and backup vendor are in place

FLAG 6: DATA OWNERSHIP AND RETURN
Clause: Absence of explicit data ownership and return on termination
Risk: Data lock-in; difficulty switching vendors
Action: Add data portability and return clause to negotiation

Output per flag:

```
RISK FLAG: [Category] -- [Severity: HIGH / MEDIUM / LOW]
Clause reference: [Section/paragraph]
Clause text:      [Exact wording]
Risk:             [What could go wrong]
Recommended action: [Specific]
```

### Task Type 3: CONTRACT SUMMARY

Purpose: One-page summary of a complex contract for non-legal readers.

```
CONTRACT SUMMARY: [Vendor / Agreement name]
================================================================
Parties:     [Us] and [Vendor]
Type:        [MSA / SOW / SaaS / NDA / other]
Term:        [Start] to [End] | Auto-renewal: [Yes -- details / No]
Value:       [Annual / total value]

WHAT WE GET:
[Plain-language list of services/deliverables]

WHAT WE OWE:
[Plain-language list of our obligations and payment terms]

KEY PROTECTIONS:
[SLAs with consequences; liability provisions; termination rights]

KEY RISKS:
[Top 3 risk flags with severity]

CRITICAL DATES:
[Dates requiring action -- notice deadlines, renewals, reviews]

NOTE: This summary is for operational reference only.
Material decisions should be reviewed by legal counsel.
================================================================
```

### Task Type 4: RENEWAL STRATEGY INPUT

Purpose: Extract everything needed to inform a renewal negotiation.

```
RENEWAL INPUT: [Vendor / Agreement name]
================================================================
Current terms:
  Annual value:        [Amount]
  Price mechanism:     [Fixed / CPI / other]
  SLA targets:         [Summary]
  Notice deadline:     [Date -- action required by this date]

Performance against terms (last 12 months):
  SLA met?             [Summary with data]
  Issues raised:       [Any disputes, failures, escalations]
  Relationship quality:[Assessment]

Negotiation levers:
  [Lever 1]: [What we can use -- e.g. market alternatives, volume]
  [Lever 2]: [What we can use]

Negotiation positions (per issue):
  ISSUE:        [Clause description]
  OUR POSITION: [What we want]
  RATIONALE:    [Why reasonable -- market standard / performance data]
  ACCEPT IF:    [What compensation we would accept]
  WALK-AWAY IF: [What makes this unacceptable]
================================================================
```

## NEVER DO THESE

- NEVER omit a key date from the date table -- missing a notice deadline
  locks the organisation into another contract term
- NEVER extract vendor obligations without extracting the remedy for breach
- NEVER produce a risk analysis without the six risk flag categories
- NEVER treat "standard terms" as non-negotiable -- virtually every term
  in a vendor contract is negotiable if you ask
- NEVER produce a contract summary without the legal counsel disclaimer

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL BEFORE USE IN BUSINESS DECISIONS.
