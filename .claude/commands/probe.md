---
description: "Idea discovery — themes, supply chain, alt-plays, sector overviews (HK-enhanced)"
argument-hint: "[optional: ticker, theme, sector, or skill name]"
---

The user invoked `/probe`. This is the idea-discovery category.

**Step 1 — Routing.**

- If `$ARGUMENTS` clearly matches one of the skills below (e.g., "themes", "supply-chain on 0700.HK", "screen for value"), go straight to Step 3.
- Otherwise, ask the user which lens they want. Present the menu below verbatim and end with: *"or just describe what you want — I'll route."*

**Step 2 — Menu:**

| # | Skill | Use when |
|---|---|---|
| 1 | `themes` | reading what the market is rewarding — HK + US + A-share cross-market |
| 2 | `supply-chain` | mapping upstream / downstream from a ticker or theme |
| 3 | `alt-plays` | finding better-priced expressions of a thesis — AH spread aware |
| 4 | `sector-overview` | sector-level state of play |
| 5 | `idea-generation` | systematic screens — value / growth / quality / short |

End with: *"Or just describe what you want — I'll pick the right lens."*

**Step 3 — Load and follow:**

- 1 / themes → `community-skills/probe/themes.md`
- 2 / supply-chain → `community-skills/probe/supply-chain.md`
- 3 / alt-plays → `community-skills/probe/alt-plays.md`
- 4 / sector-overview → `anthropic-equity-research-skills/sector-overview/SKILL.md`
- 5 / idea-generation → `anthropic-equity-research-skills/idea-generation/SKILL.md`
- Free-text → match to closest skill; ask one clarifying question only if ambiguous.

Read the chosen file and execute its workflow.
