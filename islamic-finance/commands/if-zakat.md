# /if-zakat

Compute zakat for an entity under a specific jurisdiction's rules.

## Usage

/if-zakat <jurisdiction> <financial-data>

## Examples

/if-zakat saudi "Equity SAR 40B, reserves 28B, retained earnings 18B, provisions 6B, LT debt 45B"
/if-zakat malaysia "Zakatable assets MYR 129B, current liabilities 45B"
/if-zakat pakistan "Bank deposits PKR 5B, inventory 2B, receivables 1.5B"

## Workflow

1. Load zakat-global skill
2. Identify jurisdiction zakat regime (ZATCA equity / Hanafi liquid-assets / voluntary)
3. Load jurisdiction overlay for local regulatory requirements
4. Apply correct formula with jurisdiction-specific adjustments
5. Compute zakat base and zakat amount (2.5% Hijri / 2.577% Gregorian adjustment)
6. Generate disclosure notes per jurisdiction requirements
