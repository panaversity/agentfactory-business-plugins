I'm working without your venture context. There's no `innov.local.md` file in the working directory.

Here's what I'd recommend:

**You're in the right mindset but using the wrong tool.** You haven't tested anything yet, which means:

1. **Validation requires something to validate.** The `/validate` workflow analyzes results from tests you've already run. You don't have results yet.

2. **What you actually need is `/hypothesis`** — that's the skill for building an assumption map with risk tiers, designing cheap tests, and defining success/failure criteria for each assumption.

The workflow should be:

```
/hypothesis  →  design tests  →  run tests  →  /validate
    ↑                                              |
    └──────────── pivot if needed ─────────────────┘
```

**Before either skill can give you specific (not generic) output**, you should build your `innov.local.md` file. Run **Exercise 8 from Chapter 40** to create it — it captures your venture name, stage, problem statement, customer profiles, and financial model. Every subsequent output will be tailored to your specific venture rather than generic templates.

**Want to proceed?** Tell me:

1. **Your venture** — what's the problem you're solving, for whom, and your proposed solution? I can help you build the assumption map right here in conversation.
2. Or run `/hypothesis` once you're ready, and it will produce the three-tier map (leap-of-faith → critical → nice-to-know) with cheap test designs for each.

What's your venture?
