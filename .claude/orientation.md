# Orientation

An open-source project for fundamental fintech research in Claude Code.

Anthropic shipped an excellent [equity-research skills bundle](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/equity-research/skills) — Apache-licensed, nine institutional workflow templates, written abstractly so they don't hardcode any data provider. The catch: to actually run them, you need a data connector. Anthropic's reference [`.mcp.json`](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/.mcp.json) wires through **eleven separate institutional MCPs** — FactSet, LSEG, S&P Global, Morningstar, and others. No single provider covers fundamentals + filings + transcripts + news in one place, so the full bundle stacks multiple subscriptions, each typically five figures a year per seat. Out of reach for independent analysts, academic economists, and anyone who wants institutional-grade workflows without an institutional budget.

This project closes that gap. **Both Anthropic's Apache-licensed equity-research skill bundle and a community-maintained library of fundamental analysis skills**, running on a **self-hosted free MCP server** that consolidates what would otherwise require multiple institutional subscriptions. Our MCP server sources data directly from primary public sources — yfinance, HKEX News Portal, FRED, NewsAPI, RSS feeds, and SEC EDGAR — all free, no subscription required. Free tier for all data sources; no FactSet, LSEG, S&P Global, or Morningstar subscription required.

---

## What the MCP Server provides

Free access to multi-market financial data:

- **Multi-market equity data** — Hong Kong (.HK), US stocks, and A-shares (via AH cross-listing arbitrage)
  - Real-time and historical price data via yfinance
  - HKEX News Portal disclosures (announcements, circulars, price-sensitive news)
  - A-share data through dual-listed company comparison
- **Structured fundamentals** — financial statements, ratios, multi-year history via yfinance
- **SEC filing search** — 10-K, 10-Q, 8-K, proxy, S-1 via SEC EDGAR API
- **News & events** — breaking news via NewsAPI (free tier), RSS feeds for HKEX and global financial sources
- **Macro data** — FRED economic indicators (yield curve, employment, inflation, trade flows) — free API key registration at fred.stlouisfed.org
- **Alternative signals** — government contracts, regulatory filings, disclosure pattern tracking

**Supported markets:**

| Market | Coverage | Data Source | Example Tickers |
|--------|----------|-------------|-----------------|
| US Equities | Full | yfinance + SEC EDGAR + FRED | AAPL, TSLA, NVDA, MSFT, GOOGL |
| Hong Kong | Full | HKEX News Portal + yfinance | 0700.HK, 9988.HK, 3690.HK, 1810.HK |
| A-shares | Via AH cross-listing | yfinance dual-listing | 600519 (茅台), 000858 (五粮液) |

---

## Two skill libraries, one data layer

### Anthropic equity-research skill bundle (Apache-licensed)

Nine institutional workflow templates from `anthropics/financial-services`. Abstract methodology files, no hardcoded data provider — our local MCP server slots in as the data layer.

- **`initiating-coverage`** — Full initiation note: thesis, model, valuation, risks.
- **`catalyst-calendar`** — Forward-looking catalyst tracker for a name or sector.
- **`earnings-analysis`** — Post-print review and writeup.
- **`morning-note`** — Desk-style morning note for the day's flow.
- **`thesis-tracker`** — Track an active thesis as confirms and breaks accumulate.
- *Plus `earnings-preview`, `idea-generation`, `model-update`, `sector-overview`.*

### Community-maintained fundamental analysis skills

Analyst-contributed lenses — opinionated methodologies, not buttons. How to read what the market is rewarding from the numbers up, how to walk a supply chain to find hidden champions, how to score an earnings call when management is dodging questions, how to detect channel stuffing or metric definition drift.

- **`probe/themes`** — Read what the market is actually rewarding, from the numbers up. The sharpest entry point: it tells you which lenses to pull next.
- **`probe/supply-chain`** — Walk upstream and downstream from a theme to find the picks-and-shovels names everyone else missed.
- **`dive/earnings-scorecard`** — Quantitative + qualitative scoring of calls. Tone, hedging, what got dropped from the prepared remarks.
- **`dive/financial-forensics`** — FCF gap, SBC dilution, non-GAAP creep, channel stuffing. Catches what the press release won't tell you.
- **`dive/reporting-quality`** — Metric definition drift across quarters, selective omission, language patterns that signal management is hiding something.
- **`probe/alt-plays`** — When you like a thesis but hate the valuation, find a better-priced expression of the same idea.
- **`probe/gov-contracts`** — Federal contract awards as a leading revenue indicator. See the contract before it shows up in the income statement.

In our experience, this repo also works well for academic economists doing exploratory company-level analysis.

---

## How to invoke a skill

Two ways, same skills underneath — pick whichever feels natural.

**Plain language.** Just say what you want — *"run forensics on 0700.HK"*, *"what's coming up for 9988.HK"*, *"build a theme around AI capex"*. I'll match your request to the right skill.

**Four slash commands.** Prefer a menu? Four category dispatchers cover everything:

- **`/probe`** — idea generation (themes, supply chain, alt-plays, federal contracts, screens, sector overviews)
- **`/dive`** — single-company deep work (business model, earnings tone, forensics, reporting drift, management, initiation, model updates)
- **`/track`** — position tracking (watchlist, thesis check, event radar, thesis tracker, catalyst calendar, morning note)
- **`/landscape`** — economic research (yield curve, trade flows, labor market)

Each command opens a short menu of the available lenses; pick one, or just describe what you want and I'll route from there. The slash-command surface stays at four commands no matter how big the skill library grows — new skills are added inside the dispatchers, not as new commands.

---

## Contribute a skill — please

Contributions go to the **community library**. If you have a lens you use — a sector framework, a forensic check, a screen, a macro signal — contribute it. Skills are short markdown files; adding one is a single PR. See `CONTRIBUTING.md`. The community library only gets sharp if working analysts share what they actually do. (The Anthropic equity-research bundle is upstream-mirrored, not directly contributed to here.)

---

## Getting started

### Installation

```bash
git clone https://github.com/fredtai/Fintech-research.git
cd Fintech-research
pip install -r requirements.txt
```

### Launch the MCP server

```bash
# The local MCP server starts automatically when you run:
claude

# Then in Claude Code, the MCP connection is established via:
/mcp
```

The MCP server runs as a local stdio process — no cloud authentication, no API keys required for basic functionality. Some optional data sources (FRED macro data, NewsAPI) support free tier API keys for higher rate limits, but the core functionality works out of the box.

### Skill library structure

```
community-skills/
├── probe/          # Idea generation & discovery
│   ├── themes/
│   ├── supply-chain/
│   ├── alt-plays/
│   └── gov-contracts/
├── dive/           # Single-company deep analysis
│   ├── earnings-scorecard/
│   ├── financial-forensics/
│   └── reporting-quality/
├── track/          # Position & thesis tracking
└── landscape/      # Macro economic research
```

---

## Where to start

Two natural entry points if you don't already have something specific in mind:

1. **Bring a ticker.** Hong Kong tickers like 0700.HK (Tencent), 9988.HK (Alibaba), 3690.HK (Meituan); US names like AAPL, TSLA, NVDA; or A-shares via AH comparison. Anything from "run forensics on 0700.HK" to "score 9988.HK's last call" to "is 1810.HK the best expression of the EV supply chain thesis" — name a ticker and I'll route to the right skill.

2. **Read recent market themes.** Don't know what's working right now? I can run the `themes` skill — clusters the top-performing names bottom-up over the last 1m / 3m / 6m windows, ignores GICS labels, and tells you which lenses to pull next.

**Which would you like — a specific ticker, or a read of recent market themes?**
