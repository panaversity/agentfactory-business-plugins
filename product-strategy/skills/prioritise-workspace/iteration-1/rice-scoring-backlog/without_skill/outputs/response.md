# RICE Prioritisation

Here's a RICE analysis of your 5 backlog items:

## RICE Scores

RICE = (Reach × Impact × Confidence) / Effort

| Item | Reach | Impact | Confidence | Effort | RICE Score |
|---|---|---|---|---|---|
| Dashboard performance | 100% | 2 | 80% | 2 | 80.0 |
| SSO integration | 5% | 3 | 90% | 3 | 4.5 |
| Bulk export | 5% | 2 | 70% | 2 | 3.5 |
| Mobile app notifications | 30% | 1 | 50% | 1 | 15.0 |
| API rate limiting | 20% | 2 | 50% | 2 | 10.0 |

## Recommended Priority Order

1. **Dashboard performance** (RICE: 80.0) — High reach, clear impact on all users
2. **Mobile app notifications** (RICE: 15.0) — Quick win with low effort
3. **API rate limiting** (RICE: 10.0) — Important technical foundation
4. **SSO integration** (RICE: 4.5) — High impact but narrow reach
5. **Bulk export** (RICE: 3.5) — Limited to a few enterprise customers

## Key Considerations

- **SSO** might be worth prioritising higher if those enterprise deals are time-sensitive
- **Dashboard performance** is the clear winner — affects everyone
- **API rate limiting** is tech debt that could bite you later if ignored
- Consider the $120K ARR impact of SSO when making final decisions

I'd recommend shipping Dashboard performance first, then SSO (given the revenue impact), and Mobile notifications as a quick win between larger projects.
