# /calendar

Content calendar and publishing schedule generation.

## Usage

/calendar [period] [context]

## Examples

/calendar "Q3 2026" "Thought leadership campaign for VP Ops audience, 3 posts per week"
/calendar "next 4 weeks" "Product launch support, webinar on July 15th"
/calendar "monthly" "Ongoing LinkedIn + blog cadence for fintech persona"

## Workflow

1. Route to content-calendar skill via sales-marketing-global-router
2. Load campaign strategy, ICP, and brand voice from sales-marketing.local.md if configured
3. Identify content themes and topics aligned to campaign goals
4. Map topics to channels and formats (blog, LinkedIn, email, webinar, video)
5. Schedule with appropriate frequency and spacing
6. Align content milestones with campaign events and product dates

## Output

- Mandatory header block (task, period, audience, configuration, verify data)
- Calendar view: weekly or monthly grid with content items
- Per item: topic, format, channel, publish date, owner (if applicable)
- Theme alignment: how each item supports campaign objectives
- Resource requirements: estimated effort per item
- Distribution plan: promotion channels and amplification strategy

ADJUST DATES AND TOPICS TO MATCH YOUR TEAM CAPACITY AND MARKET EVENTS
