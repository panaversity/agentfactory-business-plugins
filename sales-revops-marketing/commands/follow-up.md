# /follow-up

Post-meeting and post-call follow-up message generation with next steps.

## Usage

/follow-up [prospect-name] [meeting-type] [context]

## Examples

/follow-up "Jane Smith, Meridian Logistics" "discovery call" "Discussed warehouse pain points, interested in pilot"
/follow-up "Ahmed Khan, TechServe Pakistan" "demo" "Positive reaction, asked about SSO integration"
/follow-up "Sarah Mueller, Nordic Supply GmbH" "renewal review" "Agreed to 2-year extension, pending legal review"

## Workflow

1. Route to follow-up skill via sales-marketing-global-router
2. Load meeting context, notes, and any prior outreach history
3. Identify agreed next steps with owners and deadlines
4. Apply Five Laws compliance to follow-up messaging
5. Draft follow-up message with appropriate tone for meeting outcome
6. Determine recommended channel (email, LinkedIn, or both)

## Output

- Mandatory header block (task, prospect, meeting type, configuration, verify data)
- Meeting recap: key topics discussed, decisions made, objections raised
- Next steps with specific owners, actions, and dates
- Follow-up message draft (ready to personalise and send)
- Recommended channel and send timing
- Five Laws compliance check on the drafted message

REVIEW AND PERSONALISE BEFORE SENDING
