---
description: "Position tracking — watchlist, thesis check, event radar (HK-enhanced with Connect flow)"
argument-hint: "[optional: ticker, watchlist, or skill name]"
---

The user invoked `/track`. This is position-tracking category.

**Step 1 — Routing.**
- If `$ARGUMENTS` matches a skill, go straight to Step 3.
- Otherwise, present menu.

**Step 2 — Menu:**

| # | Skill | Use when |
|---|---|---|
| 1 | `watchlist` | view, add, or remove tracked tickers |
| 2 | `thesis-check` | quarterly thesis review: Intact/Improved/Weakening/Broken |
| 3 | `event-radar` | HKEX announcements, Connect adjustments, short ratio alerts |
| 4 | `thesis-tracker` | create/update thesis (Anthropic) |
| 5 | `catalyst-calendar` | forward catalysts (Anthropic) |
| 6 | `morning-note` | desk-style morning note (Anthropic) |

**Step 3 — Load and follow:**
- 1 → `community-skills/track/watchlist.md`
- 2 → `community-skills/track/thesis-check.md`
- 3 → `community-skills/track/event-radar.md`
- 4-6 → respective Anthropic skills
