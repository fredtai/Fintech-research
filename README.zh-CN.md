# CC 股票研究工具集（CC Equity Research Toolkits）

[English](README.md) | [日本語](README.ja.md) | **简体中文**

**一个自包含的代码库，把你的 Claude Code 变成股票研究 Agent。让每位投资者都能用上 Anthropic 官方的股票研究 Skills——无需 15 万美元的机构数据栈，专业术语密度也会根据你的熟练度自动调整，而不是默认面向卖方专业人士。**

![/discover 运行人形机器人供应链 skill —— 并行 agent 在美股与日股 ticker 中梳理上游"卖铲人"标的](assets/screenshots/cc-equity.png)

三个组件构成整体：

1. **Skill 库。** 24 套分析工作流——Anthropic 官方采用 Apache 许可证的股票研究 bundle（9 个 skill），加上社区维护的扩展库（15 个 skill）。覆盖选股思路、单公司深度分析、持仓跟踪和宏观研究。

2. **可适配的交互层。** Claude 会根据你的金融熟练度和偏好调整语气、深度和术语密度——卖方分析师、组合经理、个人投资者、学术经济学家都能用。四个统一的斜杠命令——`/discover`、`/analyze`、`/monitor`、`/macro`——把自然语言请求自动路由到全部 24 个 skill。

3. **单一数据 MCP。** `drillr` 把所有 skill 需要的数据汇总在一起：结构化财务指标、SEC 文件、电话会议纪要、企业关系图谱（供应商 / 客户 / 竞争对手）、另类数据（联邦政府合同、招聘、专利、贸易流向），以及宏观与市场背景。**覆盖美股、日股以及中概股 ADR；港股和沪深 A 股即将上线。**个人用户享有充足的免费额度。

---

## 为什么做这个

Anthropic 最近开源了一套出色的[股票研究 skill bundle](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/equity-research)——九套机构级工作流模板（initiation note、earnings analysis、catalyst calendar、morning note、thesis tracker 等等），把 Claude Code 在股票研究领域的能力上限抬高了一大截。但仍有两个缺口。

1. **数据连接器太贵。** Anthropic 的 skill 是纯方法论——本身不带数据，需要自己接上数据源。Anthropic 官方的[参考仓库](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/.mcp.json)把这些 skill 连到了 **11 个机构级 MCP**——FactSet、LSEG、标普全球、Morningstar、Moody's、PitchBook 等——**每家通常每个席位每年 1.5–3 万美元**，合计远超 15 万美元。独立分析师、学术经济学家，以及任何没有机构预算却想跑严肃工作流的人,根本接触不到。

2. **默认面向卖方专业人士，没有可达性层。** Bundle 里的模板是按卖方研究部的日常输出搭的——首次覆盖报告、晨会纪要、业绩前瞻。**概念**是通用的；**术语**（实际/预期年份记号 A/E、bp 简写、卖方报告的特定结构）对个人投资者和做企业层面探索性研究的学者来说，显得隔行如隔山。开箱即用时，Agent 不会根据使用者的金融熟练度或偏好风格自动调整。

这个项目同时解决两点。`drillr` MCP 把 11 个 MCP 的栈整合成一个连接器并提供充足的免费额度；一个由记忆驱动的交互层让输出风格匹配键盘前的人。

---

## 安装

需要先安装 [Claude Code](https://claude.com/claude-code)。

```bash
git clone https://github.com/prof-little-bear/cc-equity-research.git
cd cc-equity-research
claude
```

在 Claude Code 中运行 `/mcp` 检查 `drillr` 连接，根据提示完成认证（仓库的 `.mcp.json` 已声明 server——Claude Code 启动时自动识别）。完成后即可直接输入需求，或调用四个斜杠命令之一。

---

## 交互——四个斜杠命令

每个命令会打开该类别下的一个简短菜单。按名称选，或者直接用自然语言描述需求，dispatcher 会自动路由。

| 命令 | 类别 | 涵盖范围 |
|---|---|---|
| `/discover` | 选股思路 | 主题、供应链、替代标的、联邦合同；外加 Anthropic 的 `idea-generation`（系统性筛选）和 `sector-overview` |
| `/analyze` | 单公司深度分析 | 商业模式、业绩记分卡、财务取证、披露质量漂移、管理层；外加 Anthropic 的 `initiating-coverage`、`earnings-preview`、`earnings-analysis`、`model-update` |
| `/monitor` | 持仓跟踪 | watchlist、thesis check、事件雷达；外加 Anthropic 的 `thesis-tracker`、`catalyst-calendar`、`morning-note` |
| `/macro` | 宏观研究 | 收益率曲线、贸易流向、劳动力市场 |

**自然语言同样可用。** *"对阿里巴巴 ADR 跑一遍 forensics"*、*"PLTR 接下来 6 周有哪些催化"*、*"美国劳动力市场在转弱吗"*——Claude 通过 `CLAUDE.md` 的意图映射直接路由到对应 skill。斜杠命令是发现层，自然语言是高阶用户层，底下是同一套 skill。

例子：`/analyze BABA forensics` → 对阿里巴巴跑财务取证。`/macro` → 打开宏观菜单。`/discover AI 基建里什么在跑赢` → 路由到 `themes`。

**无论 skill 数量增加到多少，斜杠命令始终保持四个**——新 skill 是加在 dispatcher 内部，而不是变成新命令。

---

## Modes——根据使用者自我调整

两个项目本地文件决定每次回应的形态。这就是解决 Problem #2 的层——同样的分析严谨度，针对键盘前的人切换语调。

- **`.claude/mode.md`** —— `new`（默认）会在会话开始时显示引导；`experienced` 跳过。可以直接编辑文件，或者告诉 Claude "我已经熟了" 来切换。
- **`.claude/style.md`** —— 四个字段控制 Claude 的表达方式：`experience`（experienced / intermediate / learning）、`depth`（quick / balanced / deep）、`tone`（professional / institutional / conversational / educational），以及可选的 `coverage`（你专注的行业）。默认是"专业但好懂"。

Claude 在会话开始时读取两者，每一轮回都应用，会话过程中也会吸收偏好变化。你随手开始用 A/E 记号，`tone` 自动升级到 `institutional`；你问某个术语是什么意思，`experience` 自动降到 `intermediate`。文件更新后会用一行确认。

> 注：这两个文件是*项目本地*的——存在仓库里，不在 Claude Code 的跨会话自动记忆中。换一台机器 clone，不同步仓库就是从默认开始。

---

## Skills

**Anthropic bundle**（`anthropic-equity-research-skills/`）—— 从 [`anthropics/financial-services`](https://github.com/anthropics/financial-services)（Apache 2.0）vendored 过来的九套工作流模板：`initiating-coverage`、`earnings-preview`、`earnings-analysis`、`model-update`、`morning-note`、`catalyst-calendar`、`thesis-tracker`、`idea-generation`、`sector-overview`。

**社区扩展**（`community-skills/`）—— 分析师贡献的 15 种视角，分四个领域：`discover/`（themes、supply-chain、alt-plays、gov-contracts）、`analyze/`（business-model、earnings-scorecard、financial-forensics、reporting-quality、management）、`monitor/`（watchlist、thesis-check、event-radar）、`economic-research/`（yield-curve、trade-flows、labor-market）。

每个 skill 都是一个简短的 markdown 文件——读一个就知道它具体做什么。

---

## 数据——`drillr` MCP

一个 MCP 支撑所有 skill。六大数据域：

- **结构化基本面数据** —— 三大报表、60 多个标准化指标、卖方一致预期
- **SEC 文件** —— 10-K、10-Q、8-K、proxy、S-1、S-4，全文检索；中概股的 20-F / 6-K 同样覆盖
- **业绩电话会** —— 纪要全文和结构化摘要
- **企业关系图谱** —— 供应商、客户、竞争对手、可比公司、创始人背景
- **另类数据** —— 联邦政府合同、招聘、Web / App 指标、专利、贸易流向、内部人交易
- **宏观与市场背景** —— 利率、信用、劳动力、情绪、指数、商品、外汇、加密货币

数据直接来自一手来源（SEC EDGAR、企业 IR 页面、政府数据库、海关申报数据、公开市场场所），通过 Agent 化 AI 抓取——**不是转售的专有 feed**。**个人用户享有充足的免费额度**；无需 FactSet、LSEG、标普全球或 Morningstar 订阅。

覆盖范围：美股、日股、中概股 ADR；港股和沪深 A 股即将上线。你不用写 SQL——描述你要什么，运行 skill 时 Claude 会自动取数。

---

## 贡献

非常欢迎社区 skill 贡献——这是工具集随着实战分析师分享方法、不断变锋利的部分。

新增一个社区 skill 涉及三处小改动：
1. 在 `community-skills/<area>/` 加上 skill 文件
2. 在 `CLAUDE.md` 的能力映射表中加一行
3. 在 `.claude/commands/<area>.md` 对应 dispatcher 的菜单中加一行

然后提 PR。Anthropic bundle 是从上游 vendored 进来的——对它的修改建议应该提到 [`anthropics/financial-services`](https://github.com/anthropics/financial-services)，不要提到本仓库。

skill 模板、合格 skill 的判断标准、review 期望，请参考 `CONTRIBUTING.md`。

---

## 许可

工具集本体（社区 skill、脚手架、dispatcher、文档）采用 Apache 2.0 许可证——见根目录的 `LICENSE` 文件。Vendored 的 Anthropic 股票研究 bundle 同样是 Apache 2.0；归属信息与上游同步命令见 `anthropic-equity-research-skills/NOTICE.md`。
