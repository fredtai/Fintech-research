---
name: fintech-research
description: >
  100% free, self-hosted equity research toolkit for Claude Code with native
  Hong Kong stock support. Provides 24 analysis skills across 4 command families
  (/probe, /dive, /track, /landscape) backed by a local MCP server connecting to
  yfinance, HKEX, FRED, NewsAPI, and RSS — all free, zero subscription required.
  Supports .HK tickers, AH spread analysis, and HKEX regulatory filings.
version: 2.0.1
license: Apache-2.0
metadata:
  openclaw:
    tags:
      - fintech
      - equity-research
      - hong-kong-stocks
      - hkex
      - yfinance
      - free-data
      - claude-code
      - mcp
      - finance
      - investing
    category: Data & APIs
    languages:
      - en
      - zh-CN
      - ja
    requires:
      - description: "Python 3.10+ with pip"
        command: "python3 --version"
      - description: "Claude Code CLI"
        command: "claude --version"
    env:
      - name: FRED_API_KEY
        description: "Optional. Free API key from fred.stlouisfed.org for macro data"
        required: false
      - name: NEWS_API_KEY
        description: "Optional. Free API key from newsapi.org for news signals"
        required: false
---

# Fintech Research Toolkit

Transform Claude Code into a professional equity research agent with **native Hong Kong stock support** — all 100% free and self-hosted.

## What This Skill Provides

### 4 Command Families

| Command | Purpose | Trigger Keywords |
|---------|---------|-----------------|
| `/probe` | Thematic discovery, supply-chain scanning, alt-plays | "screen", "find ideas", "theme", "discover" |
| `/dive` | Single-company deep analysis | "analyze", "deep dive", "business model", "forensics" |
| `/track` | Position tracking, thesis validation, event radar | "monitor", "watchlist", "track", "thesis check" |
| `/landscape` | Macro research across CN-HK-US | "macro", "yield curve", "trade flows", "rates" |

### 24 Analysis Skills

- **9 Anthropic official skills** (Apache 2.0): initiating-coverage, earnings-preview, earnings-analysis, model-update, morning-note, catalyst-calendar, thesis-tracker, idea-generation, sector-overview
- **14 Community skills**: themes, supply-chain, alt-plays, business-model, financial-forensics, earnings-scorecard, reporting-quality, management, watchlist, thesis-check, event-radar, yield-curve, trade-flows, labor-market

### Free Data MCP Server

A local MCP server (`mcp-server/server.py`) providing 10 tools:

| Tool | Data Source | Free Basis |
|------|-------------|------------|
| `get_ticker_info` | yfinance | Open source |
| `get_price_history` | yfinance | Open source |
| `batch_ticker_info` | yfinance | Open source |
| `get_ah_spread` | yfinance | Open source |
| `get_hkex_disclosures` | HKEX News | Public access |
| `get_sec_filings` | SEC EDGAR | Official free API |
| `get_macro_data` | FRED | Official free API |
| `get_news_signals` | NewsAPI + RSS | Free tier |
| `fiscal_calendar` | Local JSON | Self-maintained |
| `run_sql` | SQLite cache | Local |

## HK Equity Support

- **65 pre-configured .HK tickers** covering Hang Seng Top 50 + tech leaders
- Tencent (0700.HK), Alibaba (9988.HK), Meituan (3690.HK), Xiaomi (1810.HK), BYD (1211.HK), Kuaishou (1024.HK), Li Auto (2015.HK), and more
- AH spread analysis (A-share vs H-share premium/discount)
- HKEX regulatory announcements scraping
- Stock Connect flow context

## Setup

```bash
# 1. Clone and install dependencies
git clone https://github.com/fredtai/Fintech-research.git
cd Fintech-research
pip install -r requirements.txt

# 2. Start Claude Code
claude

# 3. Verify MCP server is connected
/mcp

# 4. Start researching
/probe AI infrastructure in HK
/dive 0700.HK
/track 0700.HK
/landscape CN-HK-US rates
```

## Optional API Keys

The toolkit works **without any API keys** for all core features. Optional keys for enhanced data:

- `FRED_API_KEY` — Get a free key at [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html) for macro data
- `NEWS_API_KEY` — Get a free key at [newsapi.org](https://newsapi.org/register) for news signals (100 req/day)

## Customization

- **`.claude/mode.md`** — `new` or `experienced`
- **`.claude/style.md`** — Control depth (quick/balanced/deep), tone (professional/conversational), coverage (global/hk-only/us-only)

## License

Apache 2.0 — Community skills and scaffolding. Anthropic skills bundle is also Apache 2.0 (vendored from `anthropics/financial-services`).
