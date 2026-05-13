# CC Equity Research Toolkits

[English](README.md) | **日本語** | [简体中文](README.zh-CN.md)

**Claude Code を株式リサーチ用のエージェントに変える、自己完結型のリポジトリ。Anthropic 公式の株式リサーチスキルをすべての投資家に開放します — 年額 15 万ドル超の機関投資家向けデータスタックを置き換える単一のデータ MCP と、セルサイドアナリスト、ポートフォリオマネージャー、個人投資家、アカデミックエコノミストのいずれにも対応する個人化レイヤーを組み合わせました。**

<br>

![/discover でヒューマノイドロボット供給網スキルを実行 — 並列エージェントが日米のティッカーから川上のピック＆ショベル銘柄を抽出](assets/screenshots/cc-equity.png)

3 つのコンポーネントで構成されています。

1. **スキルライブラリ。** 24 種類の分析ワークフロー。Anthropic 公式の Apache 2.0 ライセンス株式リサーチバンドル（9 スキル）と、コミュニティが育てている拡張ライブラリ（15 スキル）。アイデア発掘、個別企業の深掘り、ポジション管理、マクロ・リサーチを一通りカバーします。

2. **誰でも使えるインターフェース。** Claude は使い手の金融リテラシーと好みに合わせて、トーン・深さ・専門用語の濃度を切り替えます。セルサイドアナリスト、ポートフォリオマネージャー、個人投資家、アカデミックエコノミストのいずれにも対応。`/discover`、`/analyze`、`/monitor`、`/macro` の 4 つの統合スラッシュコマンドが、自然言語の依頼を 24 スキルへ自動でルーティングします。

3. **単一のデータ MCP。** `drillr` がスキルに必要なデータをすべて集約します。構造化された財務指標、SEC 提出書類、決算説明会トランスクリプト、企業オントロジー（取引先・顧客・競合）、オルタナティブデータ（連邦政府契約、採用、特許、貿易フロー）、マクロ・市場コンテキスト。**米国株式と日本株式（東証プライム／スタンダード／グロース、TOPIX、日経 225 構成銘柄）をカバー**。個人ユーザー向けに充実した無料枠を用意しています。

---

## なぜこれを作ったか

Anthropic は先日、優れた[株式リサーチ・スキルバンドル](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/equity-research)をオープンソース化しました。イニシエーション・ノート、決算分析、カタリストカレンダー、モーニングノート、テーゼ・トラッカーなど、9 種類の機関投資家向けワークフローテンプレートです。Claude Code の株式リサーチ能力の上限を一気に引き上げる内容ですが、課題が 2 つ残ります。

1. **データコネクタが高額。** Anthropic のスキルはあくまで方法論であり、データは同梱されていません。コネクタは自前で用意する必要があります。Anthropic 公式の[リファレンスリポジトリ](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/.mcp.json)は、これらのスキルを **11 種類の機関投資家向け MCP** に接続しています。FactSet、LSEG、S&P Global、Morningstar、Moody's、PitchBook など、**1 シートあたり年額 1.5〜3 万ドル**が相場で、合計すると 15 万ドルを優に超えます。独立系アナリスト、アカデミックエコノミスト、機関投資家予算なしで本格的なリサーチを回したい人には手が届きません。

2. **セルサイド前提で、可搬性のあるインターフェースがない。** バンドルのテンプレートは、株式リサーチデスクの日々のアウトプット（イニシエーション・ノート、モーニングノート、決算プレビュー）を前提に設計されています。**概念**は普遍ですが、**用語**（実績／予想を示す A/E 表記、ベーシスポイント (bp) の略記、セルサイドレポート固有の構成）は、個人投資家やアカデミックの探索的な企業調査には敷居が高く映ります。デフォルトの状態では、エージェントが使い手のリテラシーや好みに合わせてくれません。

このプロジェクトは両方を解決します。`drillr` MCP が 11 種類の MCP スタックを 1 つのコネクタに統合し、充実した無料枠で提供。記憶駆動のインターフェース層が、出力の語り口をキーボードの先にいる人に合わせます。

---

## インストール

[Claude Code](https://claude.com/claude-code) のインストールが必要です。

```bash
git clone https://github.com/prof-little-bear/cc-equity-research.git
cd cc-equity-research
claude
```

Claude Code 内で `/mcp` を実行し、`drillr` の接続状況を確認してください。認証を求められたらその場で済ませます（リポジトリの `.mcp.json` に server が宣言済みのため、Claude Code は起動時にこれを自動で拾います）。準備ができたら、やりたいことをそのまま入力するか、4 つのスラッシュコマンドのいずれかを叩いてください。

---

## インターフェース — 4 つのスラッシュコマンド

各コマンドは、そのカテゴリ内の短いレンズメニューを開きます。名前で選んでもいいですし、やりたいことを自然言語で書けばディスパッチャーが自動でルーティングします。

| コマンド | カテゴリ | カバー範囲 |
|---|---|---|
| `/discover` | アイデア発掘 | テーマ、サプライチェーン、代替プレー、連邦政府契約。Anthropic の `idea-generation`（システマティック・スクリーン）、`sector-overview` を含む |
| `/analyze` | 個別企業の深掘り | ビジネスモデル、決算スコアカード、フォレンジック、開示クオリティ、経営陣。Anthropic の `initiating-coverage`、`earnings-preview`、`earnings-analysis`、`model-update` を含む |
| `/monitor` | ポジション・トラッキング | ウォッチリスト、テーゼ・チェック、イベント・レーダー。Anthropic の `thesis-tracker`、`catalyst-calendar`、`morning-note` を含む |
| `/macro` | マクロ・リサーチ | イールドカーブ、貿易フロー、労働市場 |

**自然言語でもそのまま通ります。**「トヨタ（7203）にフォレンジックをかけて」「ソニー（6758）の今後 6 週間のカタリストは？」「日銀の利上げサイクルで国内労働市場は緩んでいるか」といった依頼に対し、Claude は `CLAUDE.md` のインテントマップから該当スキルへ直接ルーティングします。スラッシュコマンドは発見性のレイヤー、自然言語はパワーユーザーのレイヤーで、下にあるのは同じスキルです。

例：`/analyze 7203 forensics` でトヨタにフォレンジックを実行。`/macro` でマクロメニューを開く。`/discover 半導体製造装置で何が効いているか` だと `themes` にルーティングされます。

**スキルが増えても、スラッシュコマンドは 4 つのまま。**新しいスキルはディスパッチャー内部に追加され、コマンド自体が増えることはありません。

---

## モード — 使い手に合わせる

2 つのプロジェクトローカル・ファイルが、すべての応答の形を決めます。これが課題 2、つまり同じ分析的厳密さを相手に合った語り口で返すためのレイヤーです。

- **`.claude/mode.md`** — `new`（デフォルト）はセッション開始時にオリエンテーションを表示し、`experienced` はそれをスキップします。ファイルを編集するか、Claude に「もう慣れた」と伝えれば切り替わります。
- **`.claude/style.md`** — 4 つのフィールドで Claude の話し方を制御します。`experience`（experienced / intermediate / learning）、`depth`（quick / balanced / deep）、`tone`（professional / institutional / conversational / educational）、任意の `coverage`（カバーセクター）。デフォルトは「専門的だが、わかりやすい」設定です。

Claude はセッション開始時に両方を読み、毎ターン適用しつつ、会話の途中でも好みの変化を吸収します。A/E 表記をカジュアルに使い始めれば `tone` は `institutional` に昇格。用語の意味を尋ねれば `experience` は `intermediate` にシフト。ファイルが更新され、変更点は 1 行で伝えられます。

> 補足：これらのファイルは*プロジェクトローカル*です。リポジトリ内に置かれており、Claude Code のセッション横断オートメモリには入りません。別のマシンで clone する場合、リポジトリを同期しない限り、まっさらな状態から始まります。

---

## スキル

**Anthropic バンドル**（`anthropic-equity-research-skills/`）— [`anthropics/financial-services`](https://github.com/anthropics/financial-services)（Apache 2.0）から取り込んだ 9 種類のワークフローテンプレート：`initiating-coverage`、`earnings-preview`、`earnings-analysis`、`model-update`、`morning-note`、`catalyst-calendar`、`thesis-tracker`、`idea-generation`、`sector-overview`。

**コミュニティ拡張**（`community-skills/`）— アナリストが寄稿した 15 種類のレンズを 4 領域に整理：`discover/`（themes、supply-chain、alt-plays、gov-contracts）、`analyze/`（business-model、earnings-scorecard、financial-forensics、reporting-quality、management）、`monitor/`（watchlist、thesis-check、event-radar）、`economic-research/`（yield-curve、trade-flows、labor-market）。

各スキルは短い Markdown ファイルです。1 つ読めば、何をするか正確に分かります。

---

## データ — [`drillr`](https://drillr.ai) MCP

1 つの MCP がすべてのスキルを支えます。6 つのデータドメイン：

- **構造化された財務データ** — 損益計算書／貸借対照表／キャッシュフロー計算書、60 以上の標準化指標、コンセンサス予想
- **法定開示書類** — 米国は 10-K、10-Q、8-K、プロキシ、S-1、S-4 を全文検索可能。日本企業は EDINET の有価証券報告書／四半期報告書／適時開示、ADR 銘柄は 20-F／6-K に対応
- **決算説明会** — トランスクリプトと構造化サマリー
- **企業オントロジー** — 取引先、顧客、競合、ピアグループ、創業者のバックグラウンド
- **オルタナティブデータ** — 連邦政府契約、採用、Web／アプリ指標、特許、貿易フロー、インサイダー取引
- **マクロ・市場コンテキスト** — 金利、クレジット、労働、センチメント、指数、コモディティ、為替、暗号資産

データは一次ソース（SEC EDGAR、EDINET、企業 IR ページ、政府データベース、税関データ、公開市場）から、エージェント型 AI で直接取得しています。再販ベースのプロプライエタリ・フィードではありません。**個人ユーザー向けに充実した無料枠**を用意しており、FactSet、LSEG、S&P Global、Morningstar の購読契約は不要です。

カバー範囲：米国株式、日本株式（東証プライム／スタンダード／グロース、TOPIX、日経 225 全構成銘柄）、ADR。SQL を書く必要はありません。欲しいものを言葉で伝えれば、スキル実行時に Claude が裏でデータを取得します。

---

## コントリビュート

コミュニティスキルへの貢献は大歓迎です。実務アナリストが自分の手の内を共有することで、ツールキットの切れ味が磨かれていく領域です。

新しいコミュニティスキルを追加する際は、3 つの小さな編集をお願いします。

1. `community-skills/<area>/` にスキルファイル本体を追加
2. `CLAUDE.md` のキャパビリティマップに 1 行追加
3. `.claude/commands/<area>.md` のディスパッチャーメニューに 1 行追加

その上で PR を送ってください。Anthropic バンドルはアップストリームから取り込んだものなので、そちらへの変更提案は [`anthropics/financial-services`](https://github.com/anthropics/financial-services) に出してください。

スキルテンプレート、良いスキルの基準、レビューの観点については `CONTRIBUTING.md` を参照してください。

---

## ライセンス

ツールキット本体（コミュニティスキル、スキャフォルディング、ディスパッチャー、ドキュメント）は Apache 2.0 ライセンスです。トップレベルの `LICENSE` ファイルを参照してください。取り込んでいる Anthropic 株式リサーチバンドルも Apache 2.0 です。帰属表示とアップストリーム同期コマンドは `anthropic-equity-research-skills/NOTICE.md` を参照してください。

---

## About

本プロジェクトが基盤としているもの：

- **[anthropics/financial-services](https://github.com/anthropics/financial-services)** — Anthropic 公式のオープンソース株式リサーチスキルバンドル。`anthropic-equity-research-skills/` に取り込んでいます（Apache 2.0）
- **[Drillr](https://drillr.ai)** — すべてのスキルを支える単一のデータ MCP（財務データ、SEC 提出書類、企業オントロジー、オルタナティブデータ、マクロ・市場シグナル）
