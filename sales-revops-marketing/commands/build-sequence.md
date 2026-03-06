# /build-sequence

Multi-touch outreach sequence with channel mix, branching rules, and compliance checks.

## Usage

/build-sequence [prospect-name] tier:[HOT/WARM/RE-ENGAGE] goal:[goal]

## Examples

/build-sequence "Jane Smith" tier:"HOT" goal:"discovery call" channels:"LinkedIn + Email"
/build-sequence "Ahmed Khan" tier:"WARM" goal:"webinar registration"
/build-sequence "Sarah Mueller" tier:"RE-ENGAGE" goal:"reconnect after 3 months silent"

## Workflow

1. Route to sequence skill via sales-marketing-global-router
2. Load research brief for this prospect (or prompt to run /research-prospect first)
3. Load ICP, brand voice, and Five Laws from configuration
4. For outreach to regulated jurisdictions: load jurisdiction overlay for compliance
5. Select sequence structure based on tier: HOT-6 / WARM-5 / RE-ENGAGE-3
6. Generate each touch with personalised content, channel, and timing
7. Apply Five Laws compliance check to every outreach touch
8. Define branching rules (reply, bounce, unsubscribe, open-without-click)
9. Define sequence completion actions

## Output

- Sequence overview: tier, touch count, duration, channels, goal
- Each touch: full message text, channel, timing, word count
- Five Laws compliance check for each outreach touch
- Branching rules: reply, bounce, unsubscribe, engagement signals
- Sequence completion actions: CRM logging, nurture cadence, re-evaluation

ALL OUTREACH OUTPUTS REQUIRE HUMAN REVIEW BEFORE SENDING
