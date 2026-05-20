# CC Fintech Research Toolkits

> **100% free, self-hosted, Claude Code native equity research agent with HK equity support**

[English](#english) | [简体中文](#simplified-chinese)

---

## <a name="english"></a>English

## About

**CC Fintech Research Toolkits** transforms Claude Code into a professional equity research agent with **native Hong Kong stock support**. It combines 24 analysis skills, a free data MCP server, and a personalization layer — all 100% self-hosted with **zero subscriptions**.

## Three Components

| Component | What It Does |
|-----------|-------------|
| **Skill Library** | 24 reusable analysis skills organized across 4 command families (`/probe`, `/dive`, `/track`, `/landscape`) |
| **Accessible Interface** | Claude Code native commands with configurable depth, tone, and coverage |
| **Free Data MCP** | Local MCP server connecting to yfinance, HKEX, FRED, NewsAPI, RSS — all free |

## Quick Start

1. Install Claude Code: `npm install -g @anthropics/claude-code`
2. `git clone https://github.com/fredtai/Fintech-research.git`
3. `cd Fintech-research`
4. `pip install -r requirements.txt`
5. `claude`
6. In Claude Code, run `/mcp` to verify local server is connected
7. Use `/probe`, `/dive`, `/track`, `/landscape` directly

## Command Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `/probe` | Thematic discovery, screening, idea generation | "Find HK EV supply chain plays" |
| `/dive` | Deep fundamental analysis on a single ticker | "Dive into 0700.HK business model" |
| `/track` | Ongoing monitoring, thesis check, watchlist | "Track my HK portfolio" |
| `/landscape` | Macro analysis across CN-HK-US | "Show CN-HK-US yield curves" |

## HK Equity Support

Native `.HK` ticker support covering:

- **Hang Seng Top 50**: All major constituents pre-configured
- **Tech Leaders**: Tencent (0700.HK), Alibaba (9988.HK), Meituan (3690.HK), Xiaomi (1810.HK), BYD (1211.HK), Kuaishou (1024.HK), Li Auto (2015.HK)
- **A-Share Connect**: AH spread analysis, Stock Connect flow tracking
- **HKEX Regulatory**: Announcements and filings scraping from HKEX News

## Free Data Sources

| Priority | Source | Cost | Coverage |
|----------|--------|------|----------|
| P0 Core | yfinance | Free | Global equities incl. .HK |
| P0 Core | HKEX News | Free | HKEX announcements |
| P1 Macro | FRED | Free | US rates, FX, macro |
| P1 Macro | HKMA | Free | HK monetary data |
| P2 News | NewsAPI | Free tier (100/day) | Global news |
| P2 News | RSS Feeds | Free | Financial news |

All data sources are **100% free** with **zero subscription** required. No paid APIs, no external project dependencies.

## Configuration

### Modes (`.claude/mode.md`)
- `new` — Claude presents orientation and capability map at session start
- `experienced` — Claude skips orientation, commands execute directly

### Style (`.claude/style.md`)
- **Experience**: `beginner` / `intermediate` / `advanced`
- **Depth**: `quick` (≤500 chars) / `balanced` (≤1500) / `deep` (unlimited)
- **Tone**: `professional` / `conversational`
- **Coverage**: `global` (US+HK+CN) / `us-only` / `hk-only`

## Contributing

Contributions are welcome! Please ensure:
- All data sources used are free with public documentation
- HK equity support is preserved or enhanced
- No external project dependencies are introduced
- Code passes `python -m py_compile` on all Python files

## License

Apache License 2.0 — see [LICENSE](LICENSE) for details.

---

## <a name="simplified-chinese"></a>简体中文

## 关于

**CC Fintech Research Toolkits** 将 Claude Code 转变为具有**原生港股支持**的专业股票研究 Agent。它包含 24 个分析技能、免费数据 MCP 服务器和个性化层 —— 全部 100% 自托管，**零订阅费用**。

## 三大组件

| 组件 | 说明 |
|------|------|
| **技能库** | 24 个可复用的分析技能，按 4 个命令族组织（`/probe`, `/dive`, `/track`, `/landscape`） |
| **交互界面** | Claude Code 原生命令，支持可配置的深度、语气和覆盖范围 |
| **免费数据 MCP** | 本地 MCP 服务器，连接 yfinance、港交所、FRED、NewsAPI、RSS —— 全部免费 |

## 快速开始

1. 安装 Claude Code: `npm install -g @anthropics/claude-code`
2. `git clone https://github.com/fredtai/Fintech-research.git`
3. `cd Fintech-research`
4. `pip install -r requirements.txt`
5. `claude`
6. 在 Claude Code 中运行 `/mcp` 验证本地服务器已连接
7. 直接使用 `/probe`, `/dive`, `/track`, `/landscape`

## 命令说明

| 命令 | 用途 | 示例 |
|------|------|------|
| `/probe` | 主题发现、筛选、创意生成 | "Find HK EV supply chain plays" |
| `/dive` | 单个股票的深度基本面分析 | "Dive into 0700.HK business model" |
| `/track` | 持续监控、论点验证、观察名单 | "Track my HK portfolio" |
| `/landscape` | 中港美三地宏观分析 | "Show CN-HK-US yield curves" |

## 港股支持

原生 `.HK` 股票代码支持，覆盖：

- **恒生指数前50**: 所有主要成份股已预配置
- **科技龙头**: 腾讯 (0700.HK)、阿里巴巴 (9988.HK)、美团 (3690.HK)、小米 (1810.HK)、比亚迪 (1211.HK)、快手 (1024.HK)、理想汽车 (2015.HK)
- **A股通**: AH 价差分析、互联互通资金流向追踪
- **港交所监管**: 从港交所披露易抓取公告和备案文件

## 免费数据源

| 优先级 | 来源 | 费用 | 覆盖范围 |
|--------|------|------|----------|
| P0 核心 | yfinance | 免费 | 全球股票含 .HK |
| P0 核心 | 港交所披露易 | 免费 | 港交所公告 |
| P1 宏观 | FRED | 免费 | 美国利率、汇率、宏观 |
| P1 宏观 | 香港金管局 | 免费 | 香港货币数据 |
| P2 新闻 | NewsAPI | 免费版 (100次/天) | 全球新闻 |
| P2 新闻 | RSS 订阅 | 免费 | 财经新闻 |

所有数据源均 **100% 免费**，**无需任何订阅**。没有付费 API，没有外部项目依赖。

## 配置

### 模式 (`.claude/mode.md`)
- `new` — Claude 在会话开始时展示功能和导览
- `experienced` — Claude 跳过导览，命令直接执行

### 风格 (`.claude/style.md`)
- **经验水平**: `beginner` / `intermediate` / `advanced`
- **深度**: `quick` (≤500字) / `balanced` (≤1500字) / `deep` (无限制)
- **语气**: `professional` / `conversational`
- **覆盖范围**: `global` (美股+港股+A股) / `us-only` / `hk-only`

## 贡献

欢迎贡献！请确保：
- 使用的所有数据源都是免费的，并有公开文档
- 保持或增强港股支持
- 不引入外部项目依赖
- 所有 Python 文件通过 `python -m py_compile` 编译检查

## 许可证

Apache License 2.0 — 详见 [LICENSE](LICENSE)。
