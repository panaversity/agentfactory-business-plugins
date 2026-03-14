# /contract-intake

Orchestrated contract intake workflow: receives incoming contracts, classifies document type, routes through Anthropic's `/review-contract` or `/triage-nda` with jurisdiction overlay, and tracks through tier-based SLA.

## Usage

/contract-intake [contract-description] [jurisdiction] [context]

## Examples

/contract-intake "SaaS vendor agreement received from UK company" "English law" "We are the customer, GBP 48K annual"
/contract-intake "incoming NDA from German technology partner" "German law" "Mutual NDA, need response by Friday"
/contract-intake "new consulting agreement for Dubai advisory project" "DIFC" "6-month term, AED 180K"

## Workflow

1. Receive contract and assign reference ID [YYYY-MM-DD-XXXX]
2. Run legal-global-router to identify jurisdiction and load overlay
3. Classify document type (NDA → Anthropic's `/triage-nda`; vendor/MSA/SaaS → Anthropic's `/review-contract`; employment → HR Legal queue; M&A → GC immediately)
4. Extract metadata: counterparty, contract type, business unit, urgency, value, governing law
5. Execute the appropriate Anthropic command with jurisdiction overlay applied
6. Assign triage tier based on output (Tier 1: standard approval / Tier 2: counsel review / Tier 3: full review + GC)
7. Route using communication templates (Template A/B/C per tier)
8. Set SLA reminders and track progress
9. On execution: log to repository, set renewal/obligation reminders

## Layer Architecture

This command is a **Layer 2 orchestration wrapper**. It does NOT duplicate Anthropic's contract review or NDA triage logic. Instead, it:

- Adds jurisdiction-aware routing via the legal-global-router
- Applies jurisdiction overlays before handing off to Anthropic's Layer 1 commands
- Adds tier-based SLA tracking and escalation
- Provides communication templates for each tier
- Manages post-execution obligation tracking

## Output

- Intake receipt with reference ID and metadata
- Document classification and routing decision
- Triage tier assignment with SLA timeline
- Communication template for the assigned tier
- Post-execution: obligation tracking entries and calendar reminders

ALL OUTPUTS REQUIRE REVIEW BY LICENSED ATTORNEY
