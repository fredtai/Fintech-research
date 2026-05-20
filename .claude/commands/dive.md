---
description: "Single-company deep analysis — business model, forensics, earnings, management (HK-enhanced with AH spread)"
argument-hint: "[ticker] [optional: skill name or what to analyze]"
---

The user invoked `/dive`. This is the single-company deep-work category.

**Step 1 — Routing.**
- If `$ARGUMENTS` clearly names a skill, go straight to Step 3.
- Otherwise, ask the user which lens. Present menu verbatim.

**Step 2 — Menu:**

| # | Skill | Use when |
|---|---|---|
| 1 | `business-model` | how the company makes money, 8-dimension scoring |
| 2 | `financial-forensics` | FCF vs net-income gap, IFRS non-GAAP adjustments |
| 3 | `earnings-scorecard` | 8-dimension tone + 6 content-integrity checks |
| 4 | `reporting-quality` | IFRS metric drift, ESG disclosure quality |
| 5 | `management` | capital allocation, WVR governance, HK code compliance |
| 6 | `initiating-coverage` | full initiation note (Anthropic) |
| 7 | `earnings-preview` | pre-print (Anthropic) |
| 8 | `earnings-analysis` | post-print (Anthropic) |
| 9 | `model-update` | financial model update (Anthropic) |

**Step 3 — Load and follow:**
- 1 → `community-skills/dive/business-model.md`
- 2 → `community-skills/dive/financial-forensics.md`
- 3 → `community-skills/dive/earnings-scorecard.md`
- 4 → `community-skills/dive/reporting-quality.md`
- 5 → `community-skills/dive/management.md`
- 6-9 → respective Anthropic skills

If no ticker provided, ask for one first.
