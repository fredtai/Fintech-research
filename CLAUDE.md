# CC Fintech Research Toolkits — 100% Free, Self-Hosted, HK Equity Ready

## Project Introduction

This project transforms Claude Code into a stock research agent with native Hong Kong equity support. It provides 24 analysis skills, a free data MCP server, and a personalization layer — all 100% self-contained with zero external dependencies on paid services.

## Intent Map

| Command | Trigger Keywords | What It Does | Example |
|---------|-----------------|-------------|---------|
| `/probe` | "discover", "thematic", "themes", "screen", "find ideas", "what to buy" | Scans HK/US markets for thematic opportunities, supply-chain plays, and alternative ideas | "Find EV supply chain plays in HK" |
| `/dive` | "analyze", "deep dive", "business model", "earnings", "financial forensics" | Deep fundamental analysis on a single ticker (business model, financials, management, reporting quality) | "Analyze 0700.HK business model" |
| `/track` | "monitor", "watchlist", "track", "thesis check", "event radar" | Ongoing monitoring: price alerts, thesis validation, event tracking for portfolio holdings | "Track my HK watchlist" |
| `/landscape` | "macro", "yield curve", "trade flows", "labor market", "rates" | Macro landscape analysis across CN-HK-US tri-polar framework | "Show CN-HK-US yield curves" |

## Data Sources — All Free

| Tier | Source | Cost | Coverage |
|------|--------|------|----------|
| P0 Core | yfinance | Free (MIT) | Global equities incl. .HK |
| P0 Core | HKEX News | Free (public) | HKEX announcements, filings |
| P1 Macro | FRED | Free (official API) | US macro, rates, FX |
| P1 Macro | HKMA | Free (public) | HK monetary statistics |
| P2 News | NewsAPI | Free tier (100/day) | Global news headlines |
| P2 News | RSS Feeds | Free | Financial news feeds |
| P2 SEC | SEC EDGAR | Free (official API) | US filings (US-only) |

## HK Equity Support Statement

This toolkit provides **native support for .HK tickers**, covering:
- All HKEX-listed stocks via yfinance `.HK` suffix
- Hang Seng Index top 50 constituents pre-configured
- HK tech leaders: Tencent (0700.HK), Alibaba (9988.HK), Meituan (3690.HK), Xiaomi (1810.HK), BYD (1211.HK), Kuaishou (1024.HK), Li Auto (2015.HK)
- A-share connect flows and AH spread analysis
- HKEX regulatory announcements and filings scraping

## Constraint: No External Projects / Paid Services

- **All code is self-contained** in this repository
- **No calls to external projects** or paid APIs — all functionality is self-contained
- **All data sources are free** with zero subscription requirement
- MCP server runs locally via stdio transport

## Anthropic Skill Path

Skill definitions are loaded from `.claude/commands/` directory:
- `.claude/commands/probe.md`
- `.claude/commands/dive.md`
- `.claude/commands/track.md`
- `.claude/commands/landscape.md`

Mode and style settings are read from `.claude/mode.md` and `.claude/style.md`.

## Routing Example

**User says**: "analyze 0700.HK"

**Claude routing**:
1. Parse ticker: `0700.HK` → recognized as HKEX-listed stock (Tencent Holdings)
2. Keyword match: "analyze" → maps to `/dive` command
3. Execute: Load `dive` skill → call MCP tool `get_ticker_info(0700.HK)` → call `get_price_history(0700.HK)` → perform business model + financial analysis
4. Output: Structured deep-dive report with HK-specific context (AH spread, connect flow, HKEX filings)
