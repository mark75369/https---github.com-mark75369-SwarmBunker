狀態：LOCKED
版本：v1.3（11th master frontend Batch 5 — D-075 registry DRY doc-sync partial supersede：§5.1b core 列舉補 W-style + ORG（7→11 種）+ 標「（鏡像；權威見 entity_type_registry）」+ §5.1a「第 8 種」一致性註；不移除列舉、無 schema_version bump；待 L3 簽字；本檔 v1.2 → v1.3）
歷史紀錄：v1.2（第五輪整合 partial supersede via D-047 + 議題 registry 機制 mention + Stage 0 A.0.10 對齊）
最後更新：2026-06-03
適用範圍：Game Dialogue Bible 重啟版設計規格 / CODEX 實作依據
優先級：最高

# SPEC — Game Dialogue Bible 重啟設計規格

> **v1.1 → v1.2 partial supersede 變動摘要（2026-05-19，master 第五輪整合）：**
>
> 本輪 SPEC v1.2 對 v1.1 LOCKED 內容做 **partial supersede（非 supersede）** — 保留原段內容 + 加 v1.2 標註說明擴充範圍。
>
> | SPEC 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §5.1 entity 類型 registry 段 | D-047 | 新增第 4 條 registry（issue_type_registry）— 與 entity_type_registry / qa_type_registry 並列為三層機制；既有 §5.1 兩條 registry 段不動，文末補 v1.2 mention |
> | §10 26 個 skill 清單對應 | D-047 | 5 個 /create-* skill 議題清單動態化（讀 issue_type_registry）— 不改 skill 清單本身，但 §10.4 ~ §10.8 對應段補 v1.2 「議題清單從 registry 讀」mention |
>
> **v1.2 不動段（保留 v1.1 LOCKED 原狀）：**
> - §0 ~ §4 / §6 ~ §9 / §11 ~ §16 全部
> - §5.1a / §5.1b（D-024 + D-044 + D-041 + D-025）保留
> - §5.2 ~ §5.7 保留
> - §10.1 ~ §10.3 + §10.9 ~ §10.26（不涉 D-047 的 21 個 skill）保留
> - §12 ~ §16 保留
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-046 拍板不變；本輪只加 D-047 新議題。
>
> Master 第五輪整合 owner：D-047 拍板 + 議題 registry Template + 4 主 spec partial supersede。

---

> **v1.0 → v1.1 partial supersede 變動摘要（2026-05-19，master 第四輪整合）：**
>
> 本輪 SPEC v1.1 對 v1.0 原 LOCKED 內容做 **partial supersede（非 supersede）** — 保留原段內容 + 加 v1.1 標註說明擴充範圍。涉及段落：
>
> | SPEC 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §5.1 → §5.1a / §5.1b 新增 | D-024 + D-044 + D-041 + D-025 | 新增第 8 種 entity A-* + 可擴充 entity 類型 registry 三層架構 |
> | §5.2.3 欄位定義表 | D-037 + D-024 + D-044 | 表末加 2 列（`dialogue_keys` Map + `art_metadata` List）；其他欄位順序不動 |
> | §5.2.4 三維度 enum | D-027 + D-026 + D-043 + D-028 | mode_tag 5→6（+ SINGLE_ITER）；qa_type 5→8（+ RHYTHM/DRAMATIC_TENSION/CROSS_SCENE_CONTINUITY）+ 標可擴充 |
> | §5.4 phase_log + 新增 §5.4a | D-042（含 C-07/C-09/O-04 解決） | status 從「P-012 暫定」升正式；補 5 新欄位（entities_touched / iteration_count / iteration_note / base_dialogue / conflict_resolutions）+ import_source；補 SINGLE_ITER + 手稿導入範例 |
> | §12.7 QA 報告構成 | D-043（含 C-11 解決） | 5 份 → 8 份必跑；09_e 仍不屬 QA 但補 LOCKED 降級用途 |
> | §13 新增 §13a Layer 3 Export | D-024 + D-038 + D-039（含 C-03/C-04 解決） | 新章節描述 A1 prompt 流程；不擴既有 4 個 /export-* |
> | §14 末加 §14a | D-038 + D-046 #4（含 C-12/O-02 解決） | 既有 4 個 /export-* 不擴 JSON 輸出 + 不存在 skill 不新增 |
> | §16 末加 §16a | D-040 + D-046 #5（含 C-15/C-16/O-03 解決） | LOCKED → DEPRECATED 降級流程；走 09_e 不加 frontmatter 三欄位；Save race guard |
>
> **不動段落：** §4 18 項設計決策匯總 / §5.2 canonical schema 核心 / §5.2.5 規則 / §5.2.6 場景 ID 分支 / §5.3 完成度公式 / §6-§11 / §12.1-§12.6 / §12.8-§12.10 / §13.1-§13.5 / §14 既有 26 skill 清單 / §15 模式系統 / §16 既有狀態機 7 種狀態 / §17 作品專屬 00_b 擴充策略
>
> **north-star 對齊原則：** REQUIREMENTS_LOCK v1.0 > D-037~D-046 > D-001~D-036 > specialist v0.3 一致性。所有 v1.1 標註段都明確標 D-NNN 對應 + 理由。
>
> 完整跨段對齊參考 `_design/INTEGRATION_CONTRACTS.md` v2.0（master 第四輪整合產出）。

# 0. 文件目的與閱讀者

本文件是 Game Dialogue Bible（簡稱 Bible）重啟版的**設計規格**，涵蓋專案目標、需求、所有設計決策、邏輯模型、協議結構、流程與 skill 清單。

**閱讀者：**
1. CODEX APP（執行 Phase A–D 實作的主要 agent）
2. 未來接手任何修改本系統的人或 agent

**搭配文件：**
- `ARCHITECTURE.md`：實作層細節（檔案結構、frontmatter 規範、skill 實作方式）
- `TASKS.md`：4 階段拆解後的具體實作任務與驗收條件
- `EXTRACTION_NOTES.md`：本次乾淨擷取的變更紀錄
- `references/`：Phase A 參考素材（含蟲潮孤堡專案版 00_b）

**本文件不是：**
- 實際作品設定（世界觀、角色、主線、台詞）
- 操作手冊（操作層在 AGENTS.md、00_protocol/）
- 實作程式碼

---

# 1. 專案一句話定位

```text
Game Dialogue Bible 是一套以 Markdown 為儲存層、以 agent 對話為操作介面（Claude Code / CODEX APP）
的長篇遊戲劇本與高品質台詞生產系統。

它不是獨立 GUI 應用，沒有後端 server，沒有資料庫。
它的「介面」是 Claude Code / CODEX APP 的 chat；它的「狀態」是 Git 與 frontmatter。
```

**核心命題：**
- 上游：把作品的世界觀、角色、大綱、細綱整理成結構化、agent 可讀的 Bible
- 下游：依 Bible 生成風格穩定、合規可控、可 QA、可版本管理的遊戲台詞
- 全程在 agent 對話介面中操作，agent 透過 skill 觸發、按協議執行、把結果寫回 Markdown

---

# 2. 需求總覽

## 2.1 上游創作模組（全新）

| # | 模組 | 主要產出 |
|---|---|---|
| 1 | 世界觀創立工具 | `01_world/01_a–c`、`02_vocabulary/*`、作品專屬 `00_b` 骨架 |
| 2 | 角色人設建立工具 | `03_characters/main|minor|npc/*` |
| 3 | 大綱設計工具 | `05_plot/05_a 主線大綱` |
| 4 | 細綱設計工具 | `05_plot/05_b–e`、`06_scene_index/*` |

## 2.2 下游約束與生成模組（部分已實作）

| # | 模組 | 主要產出 |
|---|---|---|
| 5 | 世界觀切片注入 | 透過任務包手動／半自動抽取（不靠 RAG） |
| 6 | 人設切片注入 | 透過任務包手動／半自動抽取 |
| 7 | 大綱／細綱／規範 → 台詞 | `07_scene_tasks/*` → `08_dialogue_outputs/*` |

## 2.3 橫向支援模組

| # | 模組 | 主要產出 |
|---|---|---|
| 8 | 專案追蹤 | `/status` skill 動態看板，依邏輯實體聚合 |
| 9 | 介面 | Claude Code / CODEX APP 對話 + skill 觸發 |

## 2.4 基礎設施

- 多 LLM provider 抽象（Claude / GPT；agent 透過 host environment 抽象）
- Git 為版本控制
- Frontmatter `entities:` + `depends_on:` 雙欄位為實體歸屬與依賴宣告（詳見 5.2 Canonical Schema）
- 文件狀態機（DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED；詳見 §16）

---

# 3. 不做的事（負面定義）

| 不做 | 原因 |
|---|---|
| 獨立 GUI 應用 | agent 對話介面已足夠；做 GUI 是維護負擔 |
| 後端 server / 資料庫 | Markdown + Git 是 source of truth |
| RAG / 向量索引 | 切片用「任務包」手動／半自動，避免一致性問題 |
| 自動把 DRAFT 升 FINAL / LOCKED | 違反「人類保留最終裁決權」原則 |
| 多人協作 | 目前只給一人使用 |
| 跨 LLM 的功能對等承諾 | host environment 抽象，但不擔保所有 skill 在所有 LLM 上行為一致 |
| 多語言對白支援 | DECISIONS_LOG D-001a 暫定；schema 不擴充 `language` / `translation_of` |
| Retcon 獨立狀態 / 欄位 | DECISIONS_LOG D-001a 暫定；用 `09_e 定稿變更紀錄` 處理 |
| Continuity_check 獨立實體 | DECISIONS_LOG D-001a 暫定；留在 `09_b` / `09_d` 處理 |
| Exchange-level scene 細粒度 | DECISIONS_LOG D-001a 暫定；採策略 A 一場一檔 |
| Protected_tier 多層保護 | DECISIONS_LOG D-002；個人專案 LOCKED 已足夠 |

## 3.1 已確認不採的擴充提案（v1.3 — D-018 promote 為最終）

以下擴充提案在 specialist 第一輪內被審視（references/CREATIVE_SCHEMA_PROPOSAL_FROM_HARNESS.md 衍生 6 議題），結論為**最終不採用**。

**v1.3 更新：** 初代 master 對話以 **D-018 (supersedes D-001a / D-007 / D-016)** 將下列 6 項從「暫定」promote 為「最終裁決」。詳細裁決紀錄見 `DECISIONS_LOG.md` D-001a / D-002 / D-003 / **D-018**。

| 提案 | 結論 | 裁決理由 | 確認等級 |
|---|---|---|---|
| Retcon vs supersede 區分（新增 `retcon_of` 欄位 / `RETCONNED` 狀態 / `09_g` 模板） | **最終不採用** | 09_e 定稿變更紀錄已涵蓋人類裁決層的 retcon 紀錄需求；retcon 走 UPSTREAM §3.6.6 路徑（09_e 紀錄 + 原版降 DEPRECATED + 新版本走完整 pipeline） | 最終（D-018） |
| 多語言對白支援（新增 `language` / `translation_of`） | **最終不採用** | 當前個人專案無多語需求；`/dialogue-write` 拒絕含 `language: en` 等的任務包 | 最終（D-018） |
| Continuity_check 獨立實體（新增 `CC-<id>` / `09_quality_assurance/continuity_checks/`） | **最終不採用** | 跨集／跨場景一致性檢查留在 09_b 角色聲線一致性 + 09_d 資訊控制處理 | 最終（D-018） |
| Scene 粒度策略 B（exchange-level，`S-01-03-e2`） | **最終採策略 A 一場一檔** | 維持策略 A；長場景由人類拆分為主場景 + 分支（§5.2.6 分支後綴規則照舊） | 最終（D-018） |
| Protected_tier 多層保護（5 層權限） | **最終不採用** | 個人專案；LOCKED 已足夠 | 最終（D-002 / D-018） |
| 「特殊資料格式」鉤子預留（遊戲引擎匯出 / 配音 / 玩家分支 / 本地化） | **最終 Phase D 後另議** | 當前無實際需求；schema 對 unknown user-defined 欄位只 WARN 不 ERROR、entity 類型保留新增空間 | 最終（D-003 / D-018） |

**第二輪資料格式 specialist 補完責任：** 即使全沿用「不採用」最終結論，仍須正式交付 `_design/DATA_FORMAT_SPEC.md` formalize 上述 6 條，並提供 §7「需 master 裁決問題清單」（即使為空）。本表 6 項在 D-018 後已不再「暫定」，第二輪資料格式 specialist 不需重新審視，僅需正式紀錄與引用。

---

# 4. 設計決策匯總（18 項，已對齊）

| # | 決策議題 | 結果 |
|---|---|---|
| 1 | 部署形式 | 無獨立 GUI，agent 對話介面（Claude Code / CODEX APP）即 UI |
| 2 | 使用者規模 | 單人使用 |
| 3 | 資料儲存 | 純 Markdown + Git + frontmatter 狀態 |
| 4 | 切片注入 | 「任務包」手動／半自動抽取，不靠 RAG |
| 5 | Repo 結構（Q1） | A+：Template / Instance 分開，Instance 內放 `.protocol_version` 追溯 |
| 6 | 進度追蹤粒度（Q2） | 邏輯實體粒度（非檔案粒度） |
| 7 | Frontmatter Canonical Schema | 中文 header 5 欄 + YAML block（`entities` / `depends_on` / `weight` / 下游 metadata），見 5.2 |
| 8 | 完成度公式（Q6） | DRAFT=25 / REVIEW=75 / FINAL\|LOCKED=100 / 不存在=0；實體=加權平均 |
| 9 | 上游引導風格（Q10） | 場景化對話：使用者貼長段假設 → 診斷 → 來回討論 → 定案寫檔 |
| 10 | 上游創建協議（Q3） | 文件 + skill 雙軌 |
| 11 | 共通骨架（Q7） | 4 份協議共用 10 區段骨架，各自加專屬區段 |
| 12 | 跳階段機制（Q8） | 預設順序但允許使用者明說跳階段 |
| 13 | 自動實體驗證（Q9） | 每份協議跑完自動呼叫 `/status` |
| 14 | 通用／作品專屬分層（Q11） | Template 純骨架；Instance 是 clone + 專案微調，bootstrap 階段微調限定 `00_b/00_c/00_d` |
| 15 | Bootstrap 紀錄格式（Q12-2） | YAML 格式 `.protocol_version` |
| 16 | 視圖層機制（Q13） | 創建時自動拆分（C 模式）；平時 `/view-*` 動態組合（A 模式）；需離線分享時 `/export-*` 產靜態檔（B 模式） |
| 17 | 迭代協議結構（Q14-2） | 通用迭代協議 `00_j_迭代協議.md` 通吃所有實體類型 |
| 18 | 影響範圍評估（Q14-3） | 迭代協議階段 2 強制跑，雙路反查：`entities` 找貢獻者、`depends_on` 找依賴者 |

**其他附加決策：**

- 4 階段分批策略（Q16=A）：A 地基+Bootstrap+世界觀 → B 其餘上游 → C 視圖+迭代 → D 台詞生產+QA+對外
- Phase 順序（Q17=B）：大致按序，可微跳
- Skill 雙語別名（Q14-1=C）：英文主名稱 + 中文別名
- 16 份「缺漏」清單修正：原以為缺很多，實際上 27 份模板已在，真正全新的是 00_e–00_j 六份協議與 09_f 類型偏移檢查模板

---

# 5. 邏輯實體（Logical Entity）規格

## 5.1 實體類型

```
W-rules         世界規則     對應 01_world/01_a 世界觀總覽
W-language      世界語言     對應 01_world/01_b 世界語言規格 + 01_c 陣營與階級語言
V               詞彙系統     對應 02_vocabulary/*
C-<name>        角色         每個角色一個實體，對應 03_characters/main|minor|npc/<name>_*.md
R-<a>-<b>       關係         每對重要關係一個實體，對應 04_relationships/* 中提及該對的段落
P               主線         對應 05_plot/05_a 主線大綱
CH-<n>          章節         每章一個實體，對應 05_plot/05_b–e 中該章相關段落
S-<ch>-<n>      場景         每場一個實體，對應 06_scene_index、07_scene_tasks、08_dialogue_outputs 中相關檔
```

**命名規則：**
- 中文角色名直接用：`C-主角A`、`C-反派B`、`C-夥伴C`
- 關係實體用左右兩端按字典序排：`R-主角A-反派B`、`R-主角A-夥伴C`
- 章節用兩位數：`CH-01`、`CH-12`
- 場景用三層：`S-01-03`（第 1 章第 3 場）

### 5.1a A-* 美術資產實體（v1.1 partial supersede via D-024 + D-044 + D-041）

> **v1.1 partial supersede via D-024（A-* 引入；只存 KEY + metadata）+ D-044（subtype 7 種正式擴大）+ D-041（SoT = `10_art_assets/`）+ D-045（不納入 narrative `/status`）**  
> **適用範圍：** §5.1 entity 類型表新增第 8 種 A-*；原 7 種類型保留不動  
> **（D-075 一致性註，2026-06-03）：** 此處「第 8 種」為 A-* 引入當下（v1.1）相對既有 7 種的歷史框架；A-* 引入順序不變。core 型別現實全集（含後續 W-style / ORG）共 11 種，權威見 `entity_type_registry`，完整列舉見 §5.1b。  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §3.1「A-* 美術資產 metadata」為本輪實作，留接口給未來 I-* / UI-* / SKILL-*；7 subtype 正式擴大解決 CODEX C-13（A-* subtype 範圍不足）+ C-05（A-* registry SoT 衝突）

新增第 8 種 entity 類型 A-*：

```
A-<subtype>-<owner>-<state>   美術資產   對應 10_art_assets/<subtype>/<group>.md（per-file metadata）
```

**A-\* subtype 7 種 enum（D-044 + DF §5.1a）：**

| subtype | `<owner>` 對應 | 範例 |
|---|---|---|
| `portrait`（立繪） | 必對應 C-* | `A-portrait-主角A-anger` |
| `bg`（背景） | 必對應 S-* / CH-* / global | `A-bg-cafe-day` |
| `cg`（事件圖） | 對應 S-* / CH-* / global | `A-cg-finale01-default` |
| `sfx`（音效） | 通常 global，可選 S-* | `A-sfx-glass-break` |
| `bgm`（背景音樂） | 通常 global / CH-* | `A-bgm-tension-01` |
| `voice`（配音） | **必對應 C-* + dialogue KEY**（句級）| `A-voice-主角A-line001` |
| `ui`（UI 文案） | 通常 global | `A-ui-button-confirm` |

**reserved_subtypes（未來擴充，本輪不採）：** `icon`（合併進 ui）/ `effect`（合併進 cg）/ `video`（reserved）/ `shader`（reserved）。

**Source of truth：** `10_art_assets/<subtype>/<group>.md` 個別 metadata file（D-041 partial supersede「`_assets/registry.yaml`」設計）。

**不存實檔 / 路徑 / URL：** A-* 只存 KEY + metadata；實檔由外部系統（Unity / 引擎）對應。

**完成度不入 `/status`（D-045）：** A-* 完成度由 parser 提供獨立 API `get_asset_completeness_by_subtype()`，前端 Asset Panel 獨立顯示；**不**納入 narrative `/status` expected entity manifest 比對。

**Schema 細節：** 見 `_design/DATA_FORMAT_SPEC.md` §5 + Contract A.3。

### 5.1b 可擴充 entity 類型 registry（v1.1 新增 via D-025）

> **v1.1 partial supersede via D-025（其他 entity 類別留接口）**  
> **適用範圍：** §5.1 entity 類型由 LOCKED 7 種擴為「core 8 種（含 A-*） + reserved prefixes + user_extensions」三層架構  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §3.1「schema 必須支援未來新增 entity 類型不必動 SPEC §5.1 核心」

> **§5.1b D-075 doc-sync partial supersede（2026-06-03，registry DRY 重構 / NEW_REQ_49）：**
> **變更理由（top-priority rule 4）：** §5.1b core 列舉自 v1.1 起停在「7 種 + A-*」，registry 已先後納入 W-style（D-055）與 ORG（D-071 / D-074）共 11 core 型別，列舉與 registry 形成 pre-existing drift。D-075 採「保留鏡像 + drift-lint」雙軌：補列舉至 11 種、列舉處標「（鏡像；權威見 entity_type_registry）」，不移除列舉（契約規格需 inline 可讀性）。
> **影響範圍：** 僅同步本段 core 列舉文字至 registry 現狀；**不移除列舉、無 `schema_version` bump、0 entity 語意改動、0 既有型別驗證行為改動**（驗證 SoT 仍為 registry + parser）。§5.1a「第 8 種 A-*」框架同步加一致性註（A-* 仍為 v1.1 引入，僅澄清 core 不止 8 種）。
> **LOCKED 處置：** §5.1 為 LOCKED-tier；本註為謹慎 doc-sync partial supersede（保留原段 + 加 v1.1 歷史溯源），需 L3 簽字後正式生效。
> **Owner：** 第十一輪 master frontend 過夜自主長跑（`feat/f8p3-audit-batch5`）+ user L3 拍板。
> **Cross-ref：** DECISIONS_LOG §6.26（D-075）/ `BATCH5_REGISTRY_DRY_REFACTOR.md` / `BATCH4_POSTLAND_AUDIT_REPORT.md` i1 / D-055 / D-071 / D-074。

**三層架構（DF §7 entity_type_registry）：**

- **core 段：** core 共 11 種 — W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG；標 `locked: true`；user 不可動
  <!-- REGISTRY-MIRROR: entity-types -->
  core 11 種：W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG
  <!-- /REGISTRY-MIRROR -->
  - **（鏡像；權威見 `entity_type_registry`）** — 本列舉為可讀性鏡像，型別清單之單一真相源（SoT）為 `_design/registries/entity_type_registry.template.yaml`（Instance 端 `<instance_root>/entity_type_registry.yaml`），以 `load_entity_type_registry()` 載入。鏡像與 registry 之一致性由 `scripts/check_entity_type_consistency.py` 在 CI lint **強制比對**（Batch 6 加 REGISTRY-MIRROR marker 後由 INFO 升 ERROR 級）；如有歧異以 registry `core` 段為準。
  - 歷史溯源：原 v1.1 列舉為「既有 7 種（W-rules / W-language / V / C / R / P / CH / S）+ A-*」；W-style（D-055 起源）+ ORG（D-071 / D-074）後續加入 registry 但列舉未同步，形成 pre-existing drift，D-075 雙軌補回（見下方 §5.1b D-075 doc-sync 註）。
- **reserved_prefixes 段：** 預留前綴清單（`I-` 物品 / `UI-` UI 文案 / `SKILL-` 技能說明）；user 加新類型不可用這些前綴
- **user_extensions 段：** Instance 端 user 自訂 entity 類型；Instance bootstrap 後可 append

**Schema 檔案位置：**
- Template 範本：`_design/registries/entity_type_registry.template.yaml`
- Instance 實檔：`<instance_root>/entity_type_registry.yaml`（Instance bootstrap 時自動複製）

**Schema 細節：** 見 DF §7 + Contract A.5（同套 registry 機制延伸至 qa_type）。

## 5.2 Frontmatter Canonical Schema（鎖定）

**唯一格式：** 每份 `.md` 必須使用以下混合 header 格式 — 既有中文 header 行 + 後續 YAML block。**三份設計文件以此為準**，CODEX 不另行選擇。

### 5.2.1 上游／靜態檔案範例（角色聲線卡）

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-17
適用範圍：主角A 聲線卡
優先級：高

---
entities:
  - C-主角A
  - R-主角A-反派B
depends_on:
  - W-rules
  - W-language
weight:
  C-主角A: 1.0
  R-主角A-反派B: 0.3
---
```

### 5.2.2 下游／pipeline 產物範例（單場台詞檔）

```markdown
狀態：DRAFT
版本：v01A
最後更新：2026-05-17
適用範圍：CH01_S03 台詞 — 試寫 A 版
優先級：中

---
entities:
  - S-01-03
depends_on:
  - C-主角A
  - C-反派B
  - R-主角A-反派B
weight:
  S-01-03: 1.0
scene_id: S-01-03
source_task: 07_scene_tasks/CH01_S03_台詞任務包.md
source_dialogue: null
pipeline_state: DIALOGUE_TRIAL
mode_tag: DRAFT_TRIAL
qa_decision: null
---
```

### 5.2.3 欄位定義（M7 + M10：狀態分層 + 跨檔 link）

| 欄位 | 必填 | 來源 | 說明 |
|---|---|---|---|
| `狀態` | 是 | 中文 header | 文件成熟度：DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED |
| `版本` | 是 | 中文 header | `vN.N` 或 `N.N`，可附 `-suffix` |
| `最後更新` | 是 | 中文 header | YYYY-MM-DD |
| `適用範圍` | 是 | 中文 header | 自由文字 |
| `優先級` | 是 | 中文 header | 最高 / 高 / 中 / 低 / 一般 |
| `entities` | 視檔案 | YAML | 本檔案「貢獻給」哪些實體；協議檔（00_*）可省略 |
| `depends_on` | 視檔案 | YAML | 本檔案「依賴」哪些實體（迭代協議反查用） |
| `weight` | 視檔案 | YAML | 對 entity 完成度的貢獻權重；scalar 或 map |
| `scene_id` | 下游 | YAML | 場景 ID（如 `S-01-03`）；僅下游 pipeline 檔有 |
| `source_task` | 下游 | YAML | 對應的任務包檔案相對路徑；台詞檔／QA 報告必填 |
| `source_dialogue` | 下游 | YAML | 對應的**單一**台詞檔案相對路徑；QA 報告必填，其他可 null |
| `source_dialogues` | 下游 | YAML | **複數版本**：list[path]，僅 `--converge` 產出的 v02 用，列出本次收斂引用的 trial 路徑；非收斂版填 null 或省略 |
| `pipeline_state` | 下游 | YAML | 場景在下游 pipeline 的狀態（見 5.2.4） |
| `mode_tag` | 下游 | YAML | 產物 mode（見 5.2.4） |
| `qa_decision` | 下游 | YAML | QA 結論：PASS / FAIL / ARBITRATE_REQUIRED / null |
| `qa_type` | 下游 | YAML | 僅 QA 報告檔填：**8 種 enum**（v1.1 / D-043；原 5 種 supersede）— AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT / RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY；可擴充由 qa_type_registry 支援（DF §8 + Contract A.5）|
| `dialogue_keys` | 下游 | YAML（Map）| **v1.1 新增 via D-037** — 僅下游台詞檔（08_dialogue_outputs）含；Map shape，每 KEY 一個 entry 含 `line_index / speaker / aliases / portrait / bgm / sfx / status / created_at / renamed_at / deleted_at / deprecated_reason`；句級 A-\* 引用權威來源；Schema 細節見 DF §4.2 + Contract A.1 |
| `art_metadata` | 視檔案（A-* metadata 檔） | YAML（List of dict）| **v1.1 新增 via D-024 + D-044** — 僅 `10_art_assets/<subtype>/<group>.md` 含；每個 A-* asset 一個 entry 含 `asset_id / display_name / subtype / owner / state_tags / aliases / created_at / renamed_at / deleted_at / status / deprecated_reason / dialogue_keys_ref`；Schema 細節見 DF §5.3 + Contract A.3 |

> **v1.1 partial supersede via D-037 + D-024 + D-044：** 表格末尾新增 2 列（`dialogue_keys` / `art_metadata`），其他欄位順序與內容**完全不動**；既有 LOCKED 欄位順序鎖定不變。  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §3.2 + §3.3 要求 i18n KEY 機制 + A-* metadata；新欄位是「補入下游檔專屬欄位」（並列既有 `scene_id / source_task / pipeline_state` 等），非順序變更或語義 supersede；既有 27 模板**無**現存 `dialogue_keys` / `art_metadata` block（dialogue 檔 / A-* metadata 檔本身屬 Phase D / Phase A.0 後才開始產），故無遷移衝突。  
> **`source_dialogues` 鎖定不擴義：** SINGLE_ITER lineage 走獨立 `base_dialogue` 欄位（屬 phase_log 內部結構，非 SPEC §5.2.3 frontmatter 下游欄位）— 詳見 §5.4 + DF §3.3d + Contract A.6（D-042 + CODEX C-09 解決）。

### 5.2.4 狀態分層（M7：避免狀態混用）

三個維度互不混用：

**A. `狀態` — 文件成熟度（共用所有檔案）：**
DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED

**B. `pipeline_state` — 場景在下游 pipeline 走到哪（僅下游檔案）：**
SCENE_INDEXED / TASK_DRAFT / TASK_REVIEW / DIALOGUE_TRIAL / DIALOGUE_CONVERGED / QA_PASSED / QA_FAILED / DIALOGUE_FINAL / DIALOGUE_LOCKED

**C. `mode_tag` — 產物的試寫模式（僅 /dialogue-write 產物）：**
ORGANIZED / DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / FINAL_CANDIDATE **/ SINGLE_ITER**（v1.1 新增 via D-027）

> **v1.1 partial supersede via D-027 + D-028（partial supersede P-010）：** `mode_tag` 從 5 種擴為 6 種，新增 `SINGLE_ITER`。  
> **理由：** REQUIREMENTS_LOCK §4.3 新增「單版本迭代模式」— agent 寫一版 → user 跟 agent 迴圈改 → OK。  
> **不新增 `/iterate-dialogue` skill**（partial supersede P-010）— 採 `/dialogue-write --single-iter` 旗標啟動。  
> **SINGLE_ITER lineage 走 phase_log `base_dialogue` 欄位**（DF §3.3d）— 不重用 SPEC 鎖定的 `source_dialogues`（CODEX C-09 解決）。

**D. `qa_type` — QA 報告檔的 QA 類型（僅 QA 報告檔填）：**
AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT **/ RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY**（v1.1 新增 via D-026 + D-043）

> **v1.1 partial supersede via D-026 + D-043（partial supersede D-018 #3）：** `qa_type` 從 5 種擴為 8 種，新增 `RHYTHM`（09_g 節奏感）/ `DRAMATIC_TENSION`（09_h 對話張力）/ `CROSS_SCENE_CONTINUITY`（09_i 跨場一致性）。  
> **`qa_type` enum 變可擴充：** 由 `qa_type_registry` Template/Instance/parser 三層架構支援；`core` 段 8 種 lock，`user_extensions` 段 user 可加新類型（DF §8 + Contract A.5）。  
> **D-018 #3 partial supersede：** 「continuity_check 不採獨立實體」維持，但**新增跨場 QA 模板 + 可擴充機制**（REQUIREMENTS_LOCK §4.2）。

**對應關係：**
- 一份試寫 v01A 台詞檔：`狀態=DRAFT`、`pipeline_state=DIALOGUE_TRIAL`、`mode_tag=DRAFT_TRIAL`、`qa_decision=null`
- 一份破格 v01D 台詞檔：`狀態=DRAFT`、`pipeline_state=DIALOGUE_TRIAL`、`mode_tag=EXPERIMENTAL`、`qa_decision=null`
- 一份收斂 v02 台詞檔：`狀態=REVIEW`、`pipeline_state=DIALOGUE_CONVERGED`、`mode_tag=CONVERGENCE`、`qa_decision=null`
- 一份 QA 通過待 final：`狀態=REVIEW`、`pipeline_state=QA_PASSED`、`mode_tag=CONVERGENCE`、`qa_decision=PASS`
- 一份人類已 final：`狀態=FINAL`、`pipeline_state=DIALOGUE_FINAL`、`mode_tag=FINAL_CANDIDATE`、`qa_decision=PASS`
- **一份 SINGLE_ITER iter1 台詞檔（v1.1 新增）：** `狀態=DRAFT`、`pipeline_state=DIALOGUE_TRIAL`、`mode_tag=SINGLE_ITER`、`qa_decision=null`；phase_log 含 `iteration_count: 1` + `base_dialogue: null`
- **一份 SINGLE_ITER iter2 台詞檔（v1.1 新增）：** `狀態=DRAFT`、`pipeline_state=DIALOGUE_TRIAL`、`mode_tag=SINGLE_ITER`、`qa_decision=null`；phase_log 含 `iteration_count: 2` + `base_dialogue: <iter1 path>`

### 5.2.5 規則

- 中文 header 必填 5 欄位
- 上游／靜態檔案 YAML 三欄：entities + depends_on + weight
- 下游 pipeline 檔（07/08/09 目錄下）另加：scene_id / source_task / source_dialogue / pipeline_state / mode_tag / qa_decision（QA 報告再加 qa_type）
- 沒有 `entities` 的協議檔（如 00_a–00_l）的 YAML block 可全部省略
- `weight` 為 scalar 時表示「所有 entities 共用此 weight」；為 map 時表示「每 entity 各自 weight」
- `depends_on` 可為空 list `[]`，初期可逐步補完
- Phase A 由 parser/helper 任務先建立解析能力（見 TASKS A.0）
- 既有 27 份模板的 YAML block 在 Phase A.4 統一補完（只補 entities/depends_on/weight；下游欄位不適用）

### 5.2.6 場景 ID 分支支援（O7）

支援分支／支線場景的 ID 後綴：
- 主場景：`S-01-03`（第 1 章第 3 場主場景）
- 分支變體：`S-01-03a`、`S-01-03b`、`S-01-03c`（同一場景的分支版本）
- 支線場景：`S-01-03sub`（從 S-01-03 衍生的支線）

對應檔名：`CH01_S03a_xxx.md`、`CH01_S03sub_xxx.md`

Parser 與 `/status` 把分支視為獨立實體（`S-01-03` 與 `S-01-03a` 是不同實體），但 `/iterate-detailed-outline` 應把同章節的分支群一起影響範圍評估。

## 5.3 完成度公式

```
單檔案完成度：
  不存在 / 空檔   → 0%
  DRAFT          → 25%
  REVIEW         → 75%
  FINAL / LOCKED → 100%
  DEPRECATED     → 不計入

單實體完成度：
  Σ(檔案完成度 × weight) / Σ(weight)
  其中只計算 entities 包含該實體的檔案
```

**範例：**
角色 C-主角A 的完成度由以下檔案貢獻：
- `03_characters/main/主角A_聲線卡.md`（entities: [C-主角A], weight: 1.0, status: REVIEW）→ 75 × 1.0 = 75
- `04_relationships/04_a_角色關係矩陣.md`（entities: [R-主角A-反派B, R-主角A-夥伴C, C-主角A], weight: 0.3 for C-主角A, status: DRAFT）→ 25 × 0.3 = 7.5
- `05_plot/05_c_角色弧線表.md`（entities: [C-主角A, C-反派B, ...], weight: 0.5 for C-主角A, status: DRAFT）→ 25 × 0.5 = 12.5

C-主角A 完成度 = (75 × 1.0 + 25 × 0.3 + 25 × 0.5) / (1.0 + 0.3 + 0.5) = 95 / 1.8 ≈ **52.8%**

## 5.4 Expected Entity Manifest（解決 CODEX 審查的「`/status` 缺 expected 來源」問題）

每個 phase 完成後應該存在哪些實體？`/status` 用這份 manifest 比對缺漏。

| 階段 | Expected Entities | 來源 |
|---|---|---|
| Bootstrap 跑完 | （無實體；只有 `.protocol_version` 與初始目錄） | `/init-project` |
| 00_e 世界觀跑完 | `W-rules`、`W-language`、`V` | `/create-world` |
| 00_f 角色跑完（每跑一次） | 新增一個或多個 `C-<name>` | `/create-character` |
| 00_l 關係跑完（每跑一次） | 新增一個 `R-<a>-<b>` | `/create-relationship` |
| 00_g 大綱跑完 | `P` | `/create-outline` |
| 00_h 細綱跑完 | 多個 `CH-<n>`、多個 `S-<ch>-<n>`（依場景索引） | `/create-detailed-outline` |
| 場景任務包跑完（每跑一次） | 該 `S-<ch>-<n>` 對應一個任務包檔 | `/scene-task` |
| 台詞生成跑完（每跑一次） | 該 `S-<ch>-<n>` 對應 ≥3 個台詞檔 | `/dialogue-write` |
| QA 跑完（每跑一次） | 該台詞檔對應 **8 份** QA 報告（v1.1 / D-043；原 5 份 supersede）| `/qa` |

**`/status` 用 manifest 的方式（M4 鎖定流程）：**

1. 讀 `_design/expected_entities.yaml`（Phase A.0 由 CODEX 建立，鎖定 manifest 規則）
2. 讀 Instance 根目錄的 `.protocol_version` 的 `phase_log` 段落（紀錄已跑過的 phase 與每次 skill 呼叫產出的 entity ID）
3. 比對兩者推導**具體 expected set**（不只是「W-rules 應該存在」，而是「依 phase_log，C-主角A、C-反派B、R-主角A-反派B 都應該存在」）
4. 對每個 expected entity：
   - 若 frontmatter 中找得到貢獻檔 → 跑 5.3 完成度公式
   - 若找不到貢獻檔 → 計為 0% 並標「缺漏，建議跑 `<對應 skill>`」
5. 不在 expected set 的實體（使用者手動建的）→ 也納入計算，但標「未追蹤實體」

**`.protocol_version` 的 `phase_log` schema（M4 加下游可追蹤欄位）：**

```yaml
phase_log:
  - phase: bootstrap
    date: 2026-05-17
    skill: /init-project
    status: completed         # P-012（暫定，原 D-014）新增：completed / aborted / in_progress
    created_entities: []
    customizations: [...]
  - phase: create-world
    date: 2026-05-18
    skill: /create-world
    status: completed
    created_entities: [W-rules, W-language, V]
  - phase: create-character
    date: 2026-05-19
    skill: /create-character
    status: completed
    created_entities: [C-主角A]
  - phase: create-relationship
    date: 2026-05-20
    skill: /create-relationship
    status: completed
    created_entities: [R-主角A-反派B]
  - phase: scene-task
    date: 2026-05-21
    skill: /scene-task
    status: completed
    scene_id: S-01-03
    task_path: 07_scene_tasks/CH01_S03_台詞任務包.md
  - phase: dialogue-write
    date: 2026-05-22
    skill: /dialogue-write
    status: completed
    scene_id: S-01-03
    dialogue_paths:
      - 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01A.md
      - 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01B.md
      - 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01C.md
    mode_tag: DRAFT_TRIAL
  - phase: qa
    date: 2026-05-23
    skill: /qa
    status: completed
    scene_id: S-01-03
    target_dialogue: 08_dialogue_outputs/CH01_S03_xxx_dialogue_v02.md
    qa_report_paths:
      - 09_quality_assurance/<base>_AI_FLAVOR.md
      - 09_quality_assurance/<base>_VOICE_CONSISTENCY.md
      - 09_quality_assurance/<base>_FORBIDDEN_WORD.md
      - 09_quality_assurance/<base>_INFO_CONTROL.md
      - 09_quality_assurance/<base>_GENRE_DRIFT.md
      # v1.1 新增（D-043）：09_g/h/i 三份
      - 09_quality_assurance/<base>_RHYTHM.md
      - 09_quality_assurance/<base>_DRAMATIC_TENSION.md
      - 09_quality_assurance/<base>_CROSS_SCENE_CONTINUITY.md
    qa_decision: PASS                            # 8 份全 PASS 才 PASS（v1.1 / D-043）
  # 並行衝突 abort 範例（依 UPSTREAM §6.7）
  - phase: dialogue-write
    date: 2026-05-24
    skill: /dialogue-write
    status: aborted
    scene_id: S-01-04
    abort_reason: parallel_conflict
    detail: phase_log.lock 等候 30 秒 timeout；另一個 /scene-task 正在執行
    entities_touched: [S-01-04, C-主角A]         # v1.1 / D-042 — 並行衝突排查必填
  # SINGLE_ITER 第 1 次範例（v1.1 新增 via D-042）
  - phase: dialogue-write
    date: 2026-05-25
    skill: /dialogue-write
    status: completed
    scene_id: S-01-05
    dialogue_paths: [08_dialogue_outputs/CH01_S05_v01_iter1.md]
    mode_tag: SINGLE_ITER                        # v1.1 / D-027
    iteration_count: 1                           # v1.1 / D-042
    iteration_note: "第一次 SINGLE_ITER 起跑"      # v1.1 / D-042
    base_dialogue: null                          # v1.1 / D-042 — 第 1 次無 base
  # SINGLE_ITER 第 2 次範例（base_dialogue 指 iter1）
  - phase: dialogue-write
    date: 2026-05-26
    skill: /dialogue-write
    status: completed
    scene_id: S-01-05
    dialogue_paths: [08_dialogue_outputs/CH01_S05_v01_iter2.md]
    mode_tag: SINGLE_ITER
    iteration_count: 2                                                   # v1.1
    iteration_note: "user 要求主角A 第 2 句更冷峻；反派B 第 4 句更挑釁"      # v1.1
    base_dialogue: 08_dialogue_outputs/CH01_S05_v01_iter1.md             # v1.1
  # 手稿導入路徑範例（v1.1 新增 via D-042）
  - phase: create-character
    date: 2026-05-27
    skill: /create-character
    status: completed
    import_source: agent_assisted                # v1.1 / D-042
    skipped_stages: [1_diagnosis, 2_exploration]
    imported_manuscript_lines: 124
    entities_touched: [C-主角B, C-夥伴D, R-主角A-夥伴D]   # v1.1
    created_entities: [C-主角B, C-夥伴D_v2]
    conflict_resolutions:                        # v1.1 / D-042 + D-033
      - entity_id: C-夥伴D
        decision: create-as-new
        new_entity_id: C-夥伴D_v2
        resolved_at: 2026-05-27
        detail: 手稿版跟既有 C-夥伴D 是不同角色
  ...
```

**`status` 欄位（v1.1 partial supersede via D-042 — 升從「P-012 暫定」為正式；保留原文字「P-012 暫定」標註僅為歷史紀錄）：**

- `completed` — skill 正常完成階段 5
- `in_progress` — skill 進入階段 1 後寫入；正常完成階段 5 時改為 `completed`
- `aborted` — skill 因並行衝突 / rollback 等原因中止；含 `abort_reason` 與 `detail` 欄位

此欄位屬 `.protocol_version` 內部結構微擴充，不動 SPEC §5.2 frontmatter canonical schema 核心。**DATA_FORMAT_SPEC v0.2 §3.2 已 formalize；P-012 RESOLVED via D-042（DECISIONS_LOG §6.7.3）。**

### 5.4a phase_log 5 新欄位（v1.1 新增 via D-042 + CODEX C-07 / C-09 / O-04 解決）

> **v1.1 partial supersede via D-042：** §5.4 phase_log entry schema 新增 5 個欄位以支援多場景並行 mutex + SINGLE_ITER lineage + 手稿導入命名衝突紀錄。  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §4.4「手稿導入路徑分支」+ §4.3「SINGLE_ITER 新增」+ UPSTREAM §6.7「並行衝突 phase_log 紀錄」全部需要對應 schema 容納；既有 27 模板無 phase_log（屬 Instance bootstrap 後產生），無遷移衝突。

5 新欄位定義（schema 細節 + 寫入規則見 DF §3.3a~e + Contract A.2 + A.6 + A.8）：

| 欄位 | 用途 |
|---|---|
| `entities_touched: List[entity_id]` | 多場景並行 mutex；該次 skill 呼叫期間讀+寫的 entity ID（⊇ `created_entities`）|
| `iteration_count: int` | SINGLE_ITER 第幾次（從 1 起算）；其他 mode_tag 為 null |
| `iteration_note: str` | 本次 SINGLE_ITER 迭代意圖（user 跟 agent 迴圈討論摘要）|
| `base_dialogue: file_path` | SINGLE_ITER lineage 上一輪路徑；**獨立欄位不重用 SPEC 鎖定的 `source_dialogues`**（C-09 解決）|
| `conflict_resolutions: List[dict]` | 手稿導入 entity 命名衝突 4 選項紀錄（D-033 + D-042）|

**`import_source` 欄位（v1.1 含；formalize via D-031）：**

- `agent_assisted` — user 已在外部 agent 工具編輯過手稿；品質可信
- `external_llm` — user 從外部 LLM 直接得到，未經審；品質未驗證
- `null`（或省略）— 既有路徑

**trust-level 限上游邊界（v1.1 對齊 C-08）：** `import_source` 只在上游 `/create-*` skill 跳階段路徑有效；**不影響**下游 `/scene-task` / `/dialogue-write` / `/qa` pipeline_state。下游永遠走標準 DRAFT → QA → REVIEW → FINAL（Contract A.8）。

**下游追蹤欄位用途：**
- `task_path`：`/scene-task` 產出的任務包路徑（讓 `/status` 知道該場景的任務包在哪）
- `dialogue_paths`：`/dialogue-write` 產出的多版本台詞檔路徑清單
- `target_dialogue`：`/qa` 檢查的目標台詞檔（不是 source_task）
- `qa_report_paths`：`/qa` 產出的 **8 份**報告路徑（v1.1 / D-043；原「5 份」supersede；讓 `/status` 驗證「該台詞檔應有 8 份報告」）
- `mode_tag` / `qa_decision`：當次 skill 寫入時的下游狀態

`/init-project` 跑完後初始化此 schema；後續每個 skill 結束時 append 一筆 phase_log entry（這是 `.protocol_version` 的責任，每個 skill 在階段 5 寫入）。

`/status` 用這些下游欄位驗證閉環（M4）：
- 若 phase_log 有 dialogue-write 紀錄但找不到 dialogue_paths 列的檔案 → 標「下游檔案缺失」
- 若 phase_log 有 qa 紀錄但找不到 qa_report_paths 列的 **8 份**報告 → 標「QA 報告不完整」（v1.1 / D-043）

---

# 6. 通用 vs 作品專屬分層

| 檔案 | Template 提供 | Instance 補完 |
|---|---|---|
| `00_a 台詞生產協議` | 完整方法論 | 通常不改 |
| `00_b 反 AI 味檢查表` | 骨架（檢查分類、QA 格式） | 作品專屬類型偏移、高風險詞、角色偏移清單、髒話風格 |
| `00_c 台詞輸出格式` | 通用格式 + 模式列表 | 作品專屬輸出模式 |
| `00_d 工作流總覽` | 通用工作流 | 通常不改 |
| `00_e–00_h、00_l` 上游創建協議 | 完整協議（共 5 份） | 通常不改 |
| `00_i 專案初始化協議` | 完整協議 | 不改 |
| `00_j 迭代協議` | 完整協議 | 通常不改 |
| `00_k 台詞生產流程協議` | 完整協議 | 通常不改 |
| `01_world ~ 08_dialogue_outputs` | 模板骨架 | 作品實際內容 |
| `09_quality_assurance` | 通用 QA 報告模板 | 作品專屬類型偏移 QA |

**Bootstrap 允許微調的 Template 文件**（Q12-1=B）：
- `00_b`、`00_c`、`00_d` 三份

其他 Template 文件在 Bootstrap 階段不允許微調，避免通用協議在多個 Instance 間發散。

---

# 7. Repo 結構（Template / Instance）

**Q1=A+ 模式：** GitHub Template Repo + `.protocol_version` 追溯。

```
Template repo（純骨架，永遠不含作品專屬內容）
   github.com/<user>/game-dialogue-bible-template

  ↓ GitHub 點 "Use this template"

Instance repo（具體作品，含 Bootstrap 微調與所有作品內容）
   github.com/<user>/<作品名>-dialogue-bible
   含 .protocol_version 紀錄 Template commit SHA 與微調清單
```

**多 Instance 升級策略：** 不自動同步。Instance 想升級 Template 時，使用者手動 cherry-pick 或 copy，或重新跑 Bootstrap。

---

# 8. Instance Bootstrap 流程

Bootstrap 是「Instance 誕生那一刻」的特殊事件，由 `00_protocol/00_i_專案初始化協議.md` 規範，由 `/init-project`（中文別名 `/初始化專案`）觸發。

**生命週期：**
```
Template repo（純骨架）
    ↓ /init-project 觸發
Instance repo（clone Template + 專案微調 + .protocol_version）
    ↓ /create-world  觸發 00_e
Instance repo（W-rules、W-language、V、作品專屬 00_b 骨架）
    ↓ /create-character  觸發 00_f
Instance repo（+ C-* 角色聲線卡）
    ↓ /create-outline  觸發 00_g
Instance repo（+ P 主線，修正作品專屬 00_b）
    ↓ /create-detailed-outline  觸發 00_h
Instance repo（+ CH-*、S-* 索引，修正作品專屬 00_b）
    ↓ 持續使用
場景任務包、台詞、QA 持續累積
```

**Bootstrap 協議結構**（沿用 10 區段共通骨架，第 10 區段為 bootstrap 專屬）：

| 區段 | 內容 |
|---|---|
| 1 文件目的 | 一次性 Instance 初始化流程 |
| 2 啟動條件 | Template repo 已 clone；尚未填任何作品內容 |
| 3 階段 1：診斷 | 使用者貼新專案基本資料（作品名、類型、長度、目標、語氣偏好、參考作品） |
| 4 階段 2：探索 | AI 列出哪些 Template 文件可能需要微調 |
| 5 階段 3：收斂 | 使用者拍板每個微調 |
| 6 階段 4：執行 | Codex 套用微調、寫 `.protocol_version`、初始化空模板 |
| 7 階段 5：驗證 | 列出已 ready 的入口，建議下一步跑 `/create-world` |
| 8 禁止事項 | 不得擅自微調 `00_a`、`00_e–00_j`、`01–09` 模板 |
| 9 缺漏處理 | 使用者未提供完整基本資料時的處理 |
| 10 專屬區段 | 微調清單範本、`.protocol_version` 格式規範、Bootstrap 完成後標準目錄狀態 |

**`.protocol_version` YAML 格式：**

```yaml
template_source: github.com/<user>/game-dialogue-bible-template
template_commit: abc123def456
bootstrap_date: 2026-05-17
project_name: <作品名>

customizations:
  - file: 00_protocol/00_b_反ai味檢查表.md
    type: 專案化
    note: 從骨架擴充到《<作品名>》專屬版本

  - file: 00_protocol/00_c_台詞輸出格式.md
    type: 新增模式
    note: 新增「<作品專屬輸出模式 1>」「<作品專屬輸出模式 2>」
```

---

# 9. 上游創建協議共通骨架（00_e ~ 00_h、00_l）

**Q7=B：共用大架構，各自加專屬區段。**

**10 個區段（預設順序，可跳階段）：**

```
1. 文件目的與適用範圍
2. 啟動條件（先決資料）
3. 階段 1：診斷模式
4. 階段 2：探索 / 補洞對話
5. 階段 3：收斂模式
6. 階段 4：Codex 執行模式（含「自動拆分」邏輯）
7. 階段 5：實體驗證（自動呼叫 /status）
8. 禁止事項
9. 缺漏處理規則（TODO / INFERENCE / CONFLICT 標記）
10. 專屬區段（每份協議自行擴充）
```

**跳階段機制（Q8=B）：**
- 使用者觸發語：「進入階段 X」「跳階段」「只跑階段 X」「執行寫檔」
- AI 跳階段前必須複述當前已確認的資料，請使用者確認再跳
- AI 不得自行決定跳階段

**自動實體驗證（Q9=A）：**
- 階段 5 自動呼叫 `/status`
- 列出本次新建或更新的實體完成度
- 列出後續仍需補的項目

**自動拆分邏輯（階段 4 的關鍵）：**
- 使用者貼的長段假設是「完整版」（依 Q13 的 C 模式）
- AI 在階段 3 收斂後，依實體邊界把整合內容**自動拆分**到對應分拆檔
- 拆分規則寫在每份協議的「專屬區段」內
- 拆分完成後可選擇性產 `view/<entity>.md` 整合檔（依 Q13 的 B 模式）

---

# 10. 五份協議的專屬區段（含 C-7 新增的 00_l）

## 10.1 世界觀創建協議（00_e）

**對應實體：** W-rules、W-language、V，以及產出作品專屬 `00_b` 骨架

**先決資料：** 無（這是上游第一份協議）

**專屬區段內容：**

1. **世界類型快速分類**（架空／半架空／現實+元素／賽博／後啟示錄／恐怖／其他）
2. **世界規則最小集**：
   - 時間觀（線性／循環／非線性）
   - 能量觀（魔法／科技／神性／無）
   - 神／魔法／科技邊界
   - 社會結構基底（封建／資本／部落／後現代）
3. **科技水平**：
   - 技術等級基準
   - 誰擁有先進技術、誰用不起
   - 技術階級差
4. **人民生活水準**：
   - 基層生活樣貌
   - 中層生活樣貌
   - 上層生活樣貌
   - 是否存在「外圍 vs 核心」「前線 vs 後方」等對立
5. **各項價值觀**：
   - 生死觀（死亡儀式、生命價值）
   - 勞動觀（工作意義、剝削邏輯）
   - 家族觀（血緣、宗族、繼承）
   - 權威觀（服從／抵抗）
   - 自由觀（個人 vs 集體）
6. **宗教**：
   - 信仰體系（一神／多神／泛靈／無神）
   - 宗教階級
   - 宗教與政治關係
   - 是否進入日常用語
7. **語言層級切片**（產出 W-language）：
   - 官方語
   - 民間語
   - 階級語
8. **陣營與階級語言**（產出 01_c）：
   - 主要陣營識別語感
   - 階級差異在語言上的痕跡
9. **類型語氣定位**（直接決定作品專屬 `00_b` 的骨架）：
   - 黑色幽默／史詩／文藝／寫實／恐怖／其他
   - 髒話尺度（高／中／低）
   - 死亡處理偏好（煽情／流程化／殘留化）
10. **越界禁區**（協議本身的邊界）：
    - 本協議不建角色（屬於 00_f）
    - 本協議不建劇情（屬於 00_g）
11. **拆分規則**（給階段 4 的執行指南）：
    - 世界規則／科技／生活水準／價值觀／宗教 → `01_a 世界觀總覽`
    - 語言層級／官方語／民間語 → `01_b 世界語言規格`
    - 陣營與階級語言 → `01_c 陣營與階級語言`
    - 詞彙（專有名詞、俗稱黑話、禁用詞） → `02_a/b/c`
    - 類型語氣 → 作品專屬 `00_b` 骨架（覆寫 Template 的通用骨架）

## 10.2 角色創建協議（00_f）

**對應實體：** C-<name>（每跑一次協議建一個或多個角色）

**先決資料：** W-rules、V、W-language 至少 REVIEW

**專屬區段內容：**

1. **角色類型分類**：
   - 主角（深度模板：聲線卡 + 偏移檢查 + 與類型氣質合規）
   - 副主／反派／夥伴（中度模板）
   - NPC 群類（輕量模板）
2. **聲線測試題**：給 AI 5 個極端場景，看能否寫出該角色該說的話
   - 範例：「角色失去重要物品的當下會說什麼？」「角色被冒犯時的第一反應？」
3. **去名測試前置**：用同情境跑既有角色，確認聲線分得開
4. **與 W-rules / V / W-language 合規性檢查**：
   - 角色用詞是否違反 V（禁用詞或未解禁名詞）
   - 是否使用了世界不存在的概念
   - 是否符合該角色所屬階級／陣營的語言層級
5. **髒話來源欄位**（若作品語氣允許）：
   - 該角色的髒話觸發點
   - 髒話頻率
   - 髒話強度
6. **偏移檢查欄位**：
   - 該角色不得偏移成 X
   - 該角色應保留 Y
7. **聲線污染檢查**：
   - 該角色是否會被誤寫成系統／AI／旁白／其他角色聲音
8. **與類型氣質合規性檢查**：
   - 該角色的設定是否會把作品拖向類型偏移（例：黑色幽默作品的角色不該寫成熱血救世主）
9. **拆分規則**：
   - 主角／重要副主 → `03_characters/main/<name>_聲線卡.md`
   - 次要角色 → `03_characters/minor/<name>_次要角色卡.md`
   - NPC 類型 → `03_characters/npc/<type>_模板.md`
   - 該角色出現於關係矩陣的部分 → `04_relationships/04_a` 對應段落
   - 該角色出現於角色弧線表的部分 → `05_plot/05_c` 對應段落
   - 偏移風險寫入作品專屬 `00_b`

## 10.3 大綱創建協議（00_g）

**對應實體：** P（主線）

**先決資料：** W-rules、V、W-language 至少 REVIEW；至少有主角的 C-* 已 DRAFT

**專屬區段內容：**

1. **必先三件事**：
   - 主線一句話
   - 核心衝突
   - 主題
2. **想要 vs 需要測試**（戲劇經典原則）：
   - 主角「想要」什麼（表層目標）
   - 主角「需要」什麼（內在成長）
   - 兩者如何衝突
3. **結構選擇**：
   - 三幕／多幕／自訂
   - 章節數估計
4. **與世界規則、角色合規性檢查**：
   - 主線是否違反 W-rules
   - 主角的需要弧線是否符合 C-主角A 已建立的聲線
5. **規模定位**（從反 AI 味檢查表抽出的核心問題）：
   - 對世界要命 vs 對角色要命、對世界不重要
   - 這決定整個敘事尺度，避免被寫成史詩化
6. **類型偏移風險清單**（提前列出本作不允許走的方向）：
   - 範例：「不要把 X 寫成巨大陰謀」「不要把 Y 寫成最終反派」「不要把 Z 寫成救世故事」
7. **拆分規則**：
   - 主線一句話、核心衝突、主題 → `05_a 主線大綱`
   - 規模定位、類型偏移風險清單 → 寫回作品專屬 `00_b`

## 10.4 細綱創建協議（00_h）

**對應實體：** CH-<n>（章節）、S-<ch>-<n>（場景索引層）

**先決資料：** W-rules、V、W-language、所有主要 C-*、P 至少 REVIEW

**專屬區段內容：**

1. **章節節奏分布**（high／mid／low 情緒節奏）：
   - 每章的情緒等級
   - 全局節奏曲線
2. **角色弧線 × 章節矩陣對齊**：
   - 每章每角色處於哪個弧線階段
3. **資訊揭露時間軸**：
   - 哪個資訊在哪一章解禁
   - 哪些資訊永遠不直接揭露
4. **伏筆與回收佈點**：
   - 伏筆放在哪一章
   - 回收放在哪一章
5. **高風險場景識別**：
   - 標記告別／和解／背叛／犧牲／告白／主角覺醒／反派理念／世界觀揭露／關係破裂／重大資訊揭露／結局前對話
6. **高風險場景的「作品專屬正確處理方式」**（從反 AI 味檢查表 16.x 衍生）：
   - 死亡結果場景 → 本作怎麼處理（殘留／流程化／諷刺 vs 臨死遺言／英雄犧牲）
   - 真相揭露場景 → 本作怎麼處理（拼湊式 vs 一次交代）
   - 關係推進場景 → 本作怎麼處理（行動／稱呼／不承認 vs 直接告白式）
   - 系統／AI 對話場景（若作品有）→ 本作怎麼處理
7. **拆分規則**：
   - 章節結構 → `05_b 章節結構`
   - 角色弧線 × 章節 → `05_c 角色弧線表`
   - 資訊揭露 → `05_d 資訊揭露表`
   - 伏筆與回收 → `05_e 伏筆與回收表`
   - 場景索引 → `06_a 場景索引`
   - 高風險場景處理規則 → 寫回作品專屬 `00_b §6`

## 10.5 關係創建協議（00_l，新增第 5 個上游協議）

**對應實體：** R-<a>-<b>（每對關係一個實體）

**先決資料：** 涉及的兩個 C-* 都至少 REVIEW

**設計動機（由 CODEX 審查 C-7 議題裁決：選 B 獨立協議）：**
- 關係建立與角色建立耦合度高，但全併入 00_f 會讓 00_f 過大且不能單獨更新某對關係
- 獨立 00_l 讓使用者：在新建角色時不需立刻決定所有關係；後續可單獨呼叫補完；既有角色之間新形成的關係可獨立建立

**專屬區段內容：**

1. **關係類型分類**：
   - 對立／合作／血緣／戀愛／師徒／同袍／敵友／其他
   - 表面關係 vs 真實關係（是否一致？哪邊在演？）
2. **權力差**：
   - 兩人之間誰擁有更多籌碼（資訊／武力／社會地位／情緒主動權）
3. **稱呼系統**：
   - 預設稱呼
   - 在特定條件下會切換的稱呼（例：受傷時、生氣時、單獨時）
4. **情緒債**：
   - 誰欠誰什麼（救命之恩、背叛、未還的承諾等）
5. **不能說出口的事**：
   - 兩人之間預設禁止戳破的話題
6. **關係時間線錨點**：
   - 在哪一章關係狀態變化（如有大綱已建立，從 05_b 抽取）
7. **拆分規則**：
   - 關係矩陣段落 → `04_a 角色關係矩陣` 中該對對應段落
   - 關係變化錨點 → `04_b 關係變化時間線`
   - frontmatter 標 `entities: [R-<a>-<b>]`、`depends_on: [C-<a>, C-<b>, W-rules]`

**對應 skill：** `/create-relationship` `/建立關係`（含中文別名）

**典型流程：**
1. 使用者：`/create-relationship 主角A 反派B`
2. 協議跑 5 階段：診斷（兩角色狀態） → 探索（關係可能性） → 收斂（拍板）→ 執行（寫 04_a 對應段落 + 04_b 時間線）→ 驗證（/status 確認 R-主角A-反派B 出現）

## 10.6 五份協議內容展開來源（時期 C 整合）

五份協議（00_e / 00_f / 00_g / 00_h / 00_l）的具體 **agent 提問腳本、使用者預期答什麼、寫檔規則、拆分 algorithm** 由 `_design/UPSTREAM_DOWNSTREAM_SPEC.md`（上下游 specialist 第一輪交付，≈90% 完成）展開：

| 協議 | 內容權威來源 |
|---|---|
| 00_e 世界觀（11 議題） | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.1（agent 提問腳本 10.1–10.11、拆分規則表、frontmatter 規範） |
| 00_f 角色（11 議題） | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.2 |
| 00_g 大綱（7 議題） | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.3 |
| 00_h 細綱（7 議題） | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.4 |
| 00_l 關係（6 議題） | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.5 |
| 5 份共通骨架執行細則 | `UPSTREAM_DOWNSTREAM_SPEC.md` §1.0.1 / §1.0.2 觸發語字典 / §1.0.3 先決資料缺失流程 |

本 SPEC §10.1–§10.5 列出**專屬區段的議題清單與拆分規則綱要**；上述 UPSTREAM 章節提供**agent 實際執行所需的提問腳本與細部 algorithm**。CODEX 在 Phase A.3 / B.0 / B.1 / B.2 / B.3 寫對應協議檔時，**以 UPSTREAM_DOWNSTREAM_SPEC §1.x 為權威來源**。

---

# 11. 通用迭代協議（00_j）

**Q14-2=C：** 不在每份上游協議裡寫迭代邏輯，而是抽出一份通用迭代協議通吃所有實體類型。

**檔案位置：** `00_protocol/00_j_迭代協議.md`

**呼叫方式：** `/iterate-world`、`/iterate-character`、`/iterate-outline`、`/iterate-detailed-outline`（+ 中文別名）都共用底層的 `00_j`。

**結構（沿用 10 區段共通骨架，內容調整為迭代邏輯）：**

| 區段 | 迭代專屬內容 |
|---|---|
| 1 文件目的 | 通用迭代邏輯，被 `/iterate-*` 系列 skill 呼叫 |
| 2 啟動條件 | 要迭代的實體必須存在且至少 DRAFT |
| 3 階段 1：變更點識別 | 使用者明說要改什麼，AI 確認變更落點（哪個分拆檔、哪個段落） |
| 4 階段 2：★ **強制影響範圍評估** | AI 依 entity tagging 反查，列出此變更可能影響的其他實體，使用者拍板要連動處理哪些 |
| 5 階段 3：收斂 | 使用者確認最終變更清單 |
| 6 階段 4：Codex 執行 | 改分拆檔、視需要連動修改、重新生成 view |
| 7 階段 5：實體驗證 | 自動 `/status` 列出受影響實體的新完成度 |
| 8 禁止事項 | 不得擅自擴大變更範圍、不得動 LOCKED、不得忽略影響範圍評估 |
| 9 缺漏處理 | 連動修改若資料不足 → 標 TODO，不擅自補 |
| 10 各上游協議的迭代呼叫指南 | W、C、P、CH 等不同實體迭代細節 |

**Q14-3=A 強制影響範圍評估邏輯：**

1. 使用者改 W-rules → AI 掃 frontmatter，找出所有 `entities:` 包含 `W-rules` 的檔案，列為「直接受影響」
2. 進一步找這些檔案中提及的其他實體（例如某角色聲線卡 frontmatter 標了 `W-rules`，該 `C-*` 即為「間接受影響」）
3. 使用者拍板：哪些連動實體要在本輪一起改、哪些留待下輪
4. 不得忽略評估結果而直接改

**各上游協議的迭代呼叫指南（區段 10 內容）：**

`00_e–00_h` 與 `00_l` 每份協議內部需新增一個「迭代呼叫」段落，指向 `00_j`：

```
若要迭代本協議產出的實體，請改用 /iterate-* skill，
詳見 00_protocol/00_j_迭代協議.md。

本協議產出的實體：W-rules、W-language、V
迭代特別注意事項：
- 修改 W-rules 通常會影響 V 與 W-language；強制檢查
- 修改 W-language 通常會影響 V 與所有 C-* 的聲線；強制檢查
```

---

# 12. 下游台詞生產 Pipeline

下游台詞生產是「Bible 完成後的日常作業」— 從選定場景到產出可定稿的台詞，是一條多階段串連流程，由三個 skill 組合而成：

```text
場景索引中的某場戲
    ↓ /scene-task CHxx Sxx
任務包（07_scene_tasks/CHxx_Sxx_台詞任務包.md）
    ↓ /dialogue-write
多版本台詞（08_dialogue_outputs/CHxx_Sxx_<簡稱>_dialogue_v01A.md 等）
    ↓ /qa <台詞檔>
**八份** QA 報告（v1.1 / D-043 — 09_a/b/c/d/f/g/h/i 對該台詞檔的檢查報告；原「五份 09_a/b/c/d/f」supersede）
    ↓ 修稿 / 重生 / 人類裁決
進入下一版（v02、v03）或定稿（FINAL/LOCKED）
```

## 12.1 統一執行協議 00_k

下游 pipeline 由一份統一協議 `00_protocol/00_k_台詞生產流程協議.md` 規範，類似於上游 5 份協議（00_e–00_h、00_l），但聚焦在「跨 skill 的執行流程」而非單一動作。

**00_k 與既有相關文件的分工：**

| 文件 | 回答 |
|---|---|
| `00_a 台詞生產協議` | What — 什麼算好台詞、什麼禁止、有哪些模式 |
| `00_k 台詞生產流程協議` | How — pipeline 怎麼跑、skill 怎麼串、狀態怎麼轉（新增） |
| `07_a 單場任務包模板` | What — 任務包的欄位格式 |
| `08_a 台詞版本管理規範` | What — 版本標記、檔名規則 |
| `08_b 生成台詞檔案模板` | What — 台詞檔的格式 |
| `09_*` QA 模板 | What — 各 QA 報告的格式 |

## 12.2 00_k 結構（沿用 10 區段共通骨架 + 下游專屬）

| 區段 | 內容 |
|---|---|
| 1 文件目的 | 統合下游 pipeline，被 /scene-task、/dialogue-write、/qa 三個 skill 共同引用 |
| 2 啟動條件 | 場景對應的 W、V、C、R、P、CH 等實體至少 REVIEW；該場 S-<ch>-<n> 在 06_a 場景索引中存在 |
| 3 階段 1：任務包建立 | /scene-task 內部執行（仿共通骨架 5 內部階段） |
| 4 階段 2：多版本試寫 | /dialogue-write 內部執行（含「試寫 → 破格選項 → 收斂」三層次） |
| 5 階段 3：QA | /qa 內部執行（跑 **8 份**報告，v1.1 / D-043；原「5 份」supersede） |
| 6 階段 4：修稿與定稿 | 人類確認 + 升級到 FINAL/LOCKED |
| 7 階段 5：實體驗證 | 自動 /status，確認 S-<ch>-<n> 完成度 |
| 8 禁止事項 | 不得擅自把 DRAFT 直接升 FINAL；不得跳過 QA；不得讓 AI 自行定案高風險場景 |
| 9 缺漏處理 | 任務包不完整時的處理；上游實體尚未 REVIEW 時的拒絕 |
| 10 專屬區段 | 場景狀態機 + 與 00_a 模式對應 + 任務包必填 + 多版本方向 + **八份** QA 報告閱讀順序（v1.1 / D-043；原「五份」supersede）|

## 12.3 場景狀態機（用 `pipeline_state` 表達，避免與文件 `狀態` 混用）

每個場景實體 `S-<ch>-<n>` 的 `pipeline_state` 在以下狀態間轉換：

```text
SCENE_INDEXED
   （在 06_a 場景索引中存在；文件 狀態=DRAFT）
   ↓ /scene-task
TASK_DRAFT
   （任務包 DRAFT；任務包檔 狀態=DRAFT、pipeline_state=TASK_DRAFT）
   ↓ ★ 人類審任務包 REVIEW gate（D.2.5；CODEX 不得自動升）
TASK_REVIEW
   （任務包 REVIEW；任務包檔 狀態=REVIEW、pipeline_state=TASK_REVIEW）
   ↓ /dialogue-write
DIALOGUE_TRIAL
   （多版本 v01A/B/C；台詞檔 狀態=DRAFT、pipeline_state=DIALOGUE_TRIAL、mode_tag=DRAFT_TRIAL）
   ↓ ★ 人類挑亮點 + 收斂 gate（D.3.5；可選擇直接讓 trial 進 QA，或先收斂）
DIALOGUE_CONVERGED
   （收斂版 v02；台詞檔 狀態=REVIEW、pipeline_state=DIALOGUE_CONVERGED、mode_tag=CONVERGENCE）
   ↓ /qa
QA_PASSED 或 QA_FAILED
   （**8 份** QA 報告；台詞檔 pipeline_state 對應更新、qa_decision=PASS|FAIL；v1.1 / D-043）
   ↓ QA_PASSED → 人類確認 + 填 09_e 定稿變更紀錄
DIALOGUE_FINAL
   （v0X 升 FINAL；台詞檔 狀態=FINAL、pipeline_state=DIALOGUE_FINAL、mode_tag=FINAL_CANDIDATE）
   ↓ 人類確認 LOCKED
DIALOGUE_LOCKED
   （台詞檔 狀態=LOCKED、pipeline_state=DIALOGUE_LOCKED）
```

**QA_FAILED 處理：**
- 修稿：產生 v0X 修稿版，回到 DIALOGUE_CONVERGED（須再跑 /qa）
- 重生：回到 DIALOGUE_TRIAL，跑新一輪 /dialogue-write
- 人類裁決：可保留違規但有價值的版本（在 09_e 紀錄裁決理由）

**「Trial 直接進 QA」例外規則（解決下游閉環問題 M8）：**

預設流程要求 DIALOGUE_TRIAL → 收斂 → QA，但允許下列例外：
- 使用者明確命令「直接對 v01A 跑 QA」時，可跳過收斂、直接 QA trial 版
- 此時 mode_tag 保持 `DRAFT_TRIAL`，pipeline_state 升 QA_PASSED/QA_FAILED 但**不能直接升 DIALOGUE_FINAL**（必須先回到 CONVERGENCE 整合）

## 12.4 與既有 00_a 模式系統的對應

00_k 不重新發明模式，而是把既有 00_a 的 10 種模式映射到 pipeline 各階段：

| 00_a 模式 | 在 pipeline 哪裡用 | 對應 skill |
|---|---|---|
| 診斷模式 | /scene-task 階段 1 內部 | /scene-task |
| 整理模式 | /scene-task 階段 4 寫任務包 | /scene-task |
| 探索模式 | /dialogue-write 階段 1 內部（可選） | /dialogue-write |
| 試寫模式 | /dialogue-write 主流程 | /dialogue-write |
| 破格模式 | /dialogue-write 內可選分支 | /dialogue-write |
| 收斂模式 | /dialogue-write 階段 3 整合 | /dialogue-write |
| QA 模式 | /qa 主流程 | /qa |
| 交稿模式 | 人類確認後升 FINAL | 人類 |
| Codex 執行模式 | 各 skill 階段 4 寫檔 | 所有 skill |
| 人類裁決模式 | QA_FAILED 時、定稿前 | 人類 |

## 12.5 任務包必填欄位

依 07_a 模板，建立任務包時必填以下資訊；`/scene-task` 會自動從各實體抽取填入：

```text
場景 ID（S-<ch>-<n>）
場景名稱
出場角色（C-* 清單）
地點與時間
前情提要
本場開始狀態
本場結束狀態
本場戲劇目的
必須透露資訊（從 05_d 抽取）
禁止透露資訊（從 05_d 抽取）
潛伏的伏筆（從 05_e 抽取）
出場角色聲線卡引用（從 03_characters/main 等抽取）
本場關係狀態（從 04_a 抽取）
角色表層目標
角色真實目標
角色不能說出口的事
台詞長度限制
風格要求
禁用詞與禁用句型（從 02_c 抽取）
本場使用的 00_a 模式
```

缺漏項標 TODO，不擅自補完。

## 12.6 多版本方向規範

`/dialogue-write` 預設產 3 版本，方向依 00_a 試寫模式建議：

| 版本 | 方向 |
|---|---|
| v01A | 克制、短句、強潛台詞 |
| v01B | 攻防更強、衝突更尖 |
| v01C | 情緒更重、但避免直說 |

任務包可指定額外方向（v01D 詩化、v01E 口語、v01F 黑色幽默等，依作品專屬 00_c 的擴充而定）。

破格模式版本另外標 `mode_tag: EXPERIMENTAL`，不混入正式 v01A/B/C。

## 12.7 QA 報告構成（M9 鎖定：09_e 不屬於 QA；v1.1 partial supersede via D-043：5→8 份）

> **v1.1 partial supersede via D-026 + D-043（partial supersede D-018 #3）：** `/qa` skill 必跑報告從 **5 份擴為 8 份**（新增 09_g 節奏感 / 09_h 對話張力 / 09_i 跨場一致性）；09_e 仍不屬於 QA（M9 鎖定維持）。原 v1.0 「5 份」段落內容保留作歷史。  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §4.1 / §4.2「9 份 QA 模板 + 1 份 final-gating」；D-018 #3 partial supersede（不採 continuity_check 獨立實體維持，但加跨場 QA + 可擴充）。

**`/qa` skill 必跑 8 份報告**（v1.1，依 D-043 + UD §2.5.3 序列順序）：

```text
（並行檢查，序列印出）
1. 類型偏移檢查（09_f / GENRE_DRIFT）           → 最優先：類型跑掉影響其他判定
2. 資訊控制檢查（09_d / INFO_CONTROL）           → 資訊洩漏先於 character 層
3. 對話張力檢查（09_h / DRAMATIC_TENSION）      → v1.1 新；張力強度標準依類型
4. 聲線一致性（09_b / VOICE_CONSISTENCY）       → 角色 OOC 判定
5. 節奏感檢查（09_g / RHYTHM）                  → v1.1 新；節奏依賴聲線
6. AI 味檢查（09_a / AI_FLAVOR）                → 表層字面層
7. 禁用詞檢查（09_c / FORBIDDEN_WORD）          → 機械詞表比對
8. 跨場一致性檢查（09_i / CROSS_SCENE_CONTINUITY）→ v1.1 新；最後 — 需所有 per-scene 結果交叉比對
```

**`qa_decision` 計算（v1.1 D-043）：**
- **PASS：** 8 份全 PASS
- **FAIL：** 任一份 FAIL
- **ARBITRATE_REQUIRED：** 人類保留違規亮點（不由 agent 自動產生，user 後續在 09_e 標）

**FINAL gate logic（v1.1 D-043）：** 需 9 種 status 齊全（8 QA + 09_e final-gating 紀錄）。

每份報告 frontmatter 標 `qa_type` 對應 8 種 enum：`GENRE_DRIFT / INFO_CONTROL / DRAMATIC_TENSION / VOICE_CONSISTENCY / RHYTHM / AI_FLAVOR / FORBIDDEN_WORD / CROSS_SCENE_CONTINUITY`。

**qa_type 可擴充：** 由 `qa_type_registry` Template/Instance/parser 三層架構支援（DF §8）— `core` 段 8 種 lock，`user_extensions` 段 user 可加新類型 + 對應 09_x 模板（由「QA 模組擴充協議」00_p 規範新模板結構；DF §8.7 接點 schema，本輪不寫實檔）。

**`09_e 定稿變更紀錄` 不是 QA 報告**（M9 裁決維持；v1.1 對齊 D-046 #5 補 LOCKED → DEPRECATED 降級紀錄用途）：
- `09_e` 是「人類在升 FINAL 前的裁決紀錄」，紀錄人類保留違規亮點、破格句的理由、QA_FAILED 但仍 final 的例外確認
- **v1.1 新增用途（D-046 #5）：** LOCKED → DEPRECATED 降級時，**降級理由 / 日期 / 操作人 / 影響**全部寫到 09_e 紀錄；**不**新增 frontmatter 三欄位（partial supersede UX_SPEC v0.2 §11.5.3 舊寫法）
- `/qa` skill 不產生 `09_e`；`09_e` 由人類在 final-gating 時手動填寫或由 final-skill（未來）產生
- **既有 `08_a 台詞版本管理規範` v1.1 對齊：** 「final 前檢查 09_a/b/c/d + 09_e」描述需修正為「QA = 09_a/b/c/d/f/g/h/i 八份；09_e 在 QA 通過後 final-gating 時填」（任務由 D.4 / D.5 處理；對齊 UD §9.1.1 Pending）

**原 v1.0 5 份報告段落保留作歷史紀錄：**

> 原 v1.0 寫法：「`/qa` skill 必跑 5 份報告，依優先順序：1. 09_f / 2. 09_d / 3. 09_b / 4. 09_a / 5. 09_c。如果 1 命中重大問題，後面 4 份報告可能要重看（因為類型偏移會影響聲線判定）。」  
> v1.1 partial supersede via D-043 — 擴為 8 份必跑；序列順序見上述。

## 12.8 影響範圍：下游 → 上游的 canon delta（成熟期功能）

定稿後的台詞可能揭露之前 Bible 沒寫清楚的設定（角色細節、世界觀延伸、新詞彙）。理想流程：

- **不要**直接把台詞中的新設定當成 canon 寫回 Bible
- **應該**抽取「confirmed canon delta」交由使用者裁決後寫回 Bible 對應實體
- 這是「Canon Delta 流程」，屬於 Phase D 之後的成熟期功能；本次 SPEC 不展開實作

## 12.9 跨 skill 的呼叫關係

| Skill | 觸發協議 | 沿用 00_a 模式 | 主要產出 |
|---|---|---|---|
| `/scene-task` | 00_k 階段 1 | 診斷模式 + 整理模式 | `07_scene_tasks/<ID>_台詞任務包.md` |
| `/dialogue-write` | 00_k 階段 2 | 試寫 / 破格 / 收斂 模式 | `08_dialogue_outputs/<ID>_dialogue_vXX.md`（多版本） |
| `/qa` | 00_k 階段 3 | QA 模式 | `09_*/<ID>_<QA 類型>_報告.md`（**8 份**，v1.1 / D-043；原「5 份」supersede）|

三者由 00_k 統一規範，但各自獨立可呼叫。例如：
- 只想跑任務包，使用者後續手動寫台詞 → 只跑 /scene-task
- 已有任務包，想再跑一輪試寫 → 直接 /dialogue-write
- 已定稿版要重新跑 QA → 只跑 /qa

## 12.10 下游 pipeline 與 canon delta 內容展開來源（時期 C 整合）

下游 pipeline 的具體 **agent 執行 algorithm、場景狀態機觸發條件、8+1 QA 模板內容（v1.1 / D-043；原「5+1」supersede）、`/dialogue-write` 三模式 algorithm、canon delta 框架、多場景並行處理** 由 `_design/UPSTREAM_DOWNSTREAM_SPEC.md`（上下游 specialist 第一輪交付）展開：

| 內容 | 權威來源 |
|---|---|
| 00_k 完整內容（10 區段 + 場景狀態機觸發、與 00_a 模式對應、任務包必填、多版本方向、QA 閱讀順序、跨 skill 呼叫、多場景並行）| `UPSTREAM_DOWNSTREAM_SPEC.md` §2.1–§2.10 |
| **9 份** QA 模板內容（v1.1 / D-043；原「6 份」supersede — 09_a / 09_b / 09_c / 09_d / 09_f / **09_g / 09_h / 09_i** 各自的檢查 algorithm + 09_e final-gating 紀錄）| `UPSTREAM_DOWNSTREAM_SPEC.md` §3.1–§3.9 |
| `/dialogue-write` 三模式 algorithm（試寫 / 破格 / 收斂；含 `--converge` 三輸入形態、輸入解析分發、收斂演算法、break 規則） | `UPSTREAM_DOWNSTREAM_SPEC.md` §4.1–§4.6 |
| Canon delta 抽取演算法、提案流程、回寫執行、與 LOCKED 互動、phase_log 紀錄、UX 標記 | `UPSTREAM_DOWNSTREAM_SPEC.md` §5.1–§5.8 |
| 多場景並行處理（容忍度總表、phase_log 寫入鎖、場景狀態升級鎖、串行約束、跨場景依賴檢查、並行行為、abort 紀錄） | `UPSTREAM_DOWNSTREAM_SPEC.md` §6.1–§6.9 |

本 SPEC §12.1–§12.9 列出**框架與規範綱要**；上述 UPSTREAM 章節提供 **agent 執行所需的具體 algorithm**。CODEX 在 Phase D.0–D.4 與相關下游任務（D.4 / D.5 / 未來 canon delta 任務）寫對應檔時，**以 UPSTREAM_DOWNSTREAM_SPEC §2–§6 為權威來源**。

### 12.10.1 既有 08_a §11.1 修正（P-009 暫定，原 D-011）

UPSTREAM §3.6.2 / DECISIONS_LOG P-009 指出既有 `08_a 台詞版本管理規範 §11.1` 對「必要 QA」描述與 M9 鎖定衝突，須修正：

- **舊（誤）：** 必要 QA = 09_a / 09_b / 09_c / 09_d / 09_e
- **新（正，v1.1 / D-043 + 原 v1.0）：** 必要 QA（由 `/qa` 產出）= 09_a / 09_b / 09_c / 09_d / 09_f / **09_g / 09_h / 09_i**（**8 份**，對應 8 種 qa_type；v1.1 從 5 份擴為 8 份）；09_e 不屬 QA pipeline，是 QA 通過後 final-gating 時由人類填寫

此修正任務由 Phase D.4 或 D.5 執行（見 TASKS）。

### 12.10.2 `/iterate-dialogue` 不新增（P-010 暫定，原 D-012）

UPSTREAM §4.3.4 提及第二次 `--converge` 時 agent 應建議 `/iterate-dialogue`，但此 skill 不在當前 26 個 skill 清單。**master 暫定（等第二輪 §9 正式提案）：不新增**。多次 `--converge`（將 v02 作為 trial 引用）已涵蓋此需求；保留 26 個 skill 清單不變。

---

# 13. 視圖層機制

**Q13：** 創建拆分（C 模式）、平時用 A+B 模式組合。

## 13.1 Source of Truth：分拆檔案

實際資料以分拆檔案為 source of truth，例如世界觀拆成 `01_a 世界觀總覽`、`01_b 世界語言規格`、`01_c 陣營與階級語言`。

理由：
- 便於 entity tagging
- 便於切片注入（任務包只抓必要段落）
- Git diff 清晰
- 迭代時只需動局部

## 13.2 創建階段：自動拆分

使用者在 `00_e`–`00_h` 創建協議中**貼完整版假設**，AI 在階段 4 依協議的「拆分規則」自動拆到分拆檔。

這次性事件只發生在創建那一次，迭代不需要拆分判斷。

## 13.3 閱讀階段：動態組合（A 模式）

平時要看「完整世界觀／完整角色」時，呼叫 skill：
- `/view-world` `/查看世界觀` — 即時 read `01_a + 01_b + 01_c + 02_*`，組合後印在 chat
- `/view-character <name>` `/查看角色 <name>` — 即時組合該角色的聲線卡、關係矩陣中該角色部分、弧線表中該角色部分
- `/view-outline` `/查看大綱` — 即時組合主線、章節、弧線
- `/view-detailed-outline` `/查看細綱` — 即時組合章節結構、揭露、伏筆、場景索引

組合結果不存實體檔，每次 `/view-*` 都動態拼。

## 13.4 分享階段：靜態整合檔（B 模式）

要把完整版分享給其他工具或人類時，呼叫 skill：
- `/export-world` `/匯出世界觀` — 寫 `view/世界觀.md`
- `/export-character <name>` `/匯出角色 <name>` — 寫 `view/角色_<name>.md`
- 其餘以此類推

迭代後使用者可手動重跑 `/export-*` 更新整合檔。`view/` 資料夾在 Template repo 是空的，Instance 跑過 export 後才會有內容。

## 13.5 倒推結論：不做反向自動拆分

不做「使用者編輯整合檔，agent 自動拆回分拆檔」（這是 Q13 選項 C，已被排除）。理由：拆分判斷對 agent 太困難、容易出錯。

---

## 13a. Layer 3 Export — JSON + MD 雙吐機制（v1.1 新增 via D-024 + D-038 + D-039）

> **v1.1 新增章節 via D-024（套版機制大幅縮減）+ D-038（A1 prompt 流程）+ D-039（JSON `manifest + records[]` 為權威）+ CODEX C-03 / C-04 解決**  
> **north-star 對齊理由：** REQUIREMENTS_LOCK §3.4「套版機制縮減為 JSON+MD 雙吐」+ §2 三層架構 Layer 3 Export；本章節描述 Layer 3 Export 流程，**不擴**既有 §13 / §14 的 4 個 `/export-*` skill；兩條 export 路徑共存（既有 4 skill 服務「人讀」場景；Layer 3 Export 服務「機器讀」場景）

### 13a.1 Layer 3 Export 不新增 skill — 走 A1 prompt 流程（D-038）

依 D-038 拍板 + CODEX C-03 critical 解決：

- 維持 26 skill 清單不動（D-031）
- Layer 3 Export 實作為「**前端 Export 按鈕產 A1 prompt → user 貼到 Claude Code / CODEX APP → agent 跑**」
- **不**用 CLI / **不**新增 skill / **不**前端執行 export

**v1.1 確認：** D-029 α「完全分離」**包含**禁止 local non-LLM tool action — 前端不執行任何 agent action / local CLI。Export 動作的「執行」全在外部 agent 的 process 中發生。

### 13a.2 A1 prompt 三層觸發路徑

| 路徑 | user 動作 | 開發 phase |
|---|---|---|
| 1. clipboard（預設） | 點前端「複製 Export Prompt」按鈕 → 切到 CC/CODEX APP 貼 → agent 跑 | Phase A.0 必做 |
| 2. POST 到本地 LLM endpoint | 設定 endpoint URL → 點推送按鈕 → 前端 POST prompt → 本地 LLM endpoint 跑 → 回 export 結果 | Phase B 後必做（D-038 附帶第 2 項） |
| 3. POST 到 Claude API / OpenAI API | 同上，但對應雲端 API | Phase C+ 選做 |

**所有路徑共用同一 prompt schema**（見 §13a.3）。

### 13a.3 Prompt schema 引用 `_design/L3_EXPORT_PROMPT_SCHEMA.md`

Prompt schema 由 master 在 `_design/L3_EXPORT_PROMPT_SCHEMA.md`（v0.1，本輪 master 新建）規範；本節**不重複定義**，只列接點要求：

| 區塊 | 必填 | 內容 |
|---|---|---|
| 1. 標題行 | ✅ | `# Layer 3 Export Task — <project_id> — <YYYY-MM-DD HH:MM>` |
| 2. 元資料區（YAML block） | ✅ | repo_root / scope / formats / output_paths / mode |
| 3. 執行步驟 | ✅ | 編號 1~N 的步驟清單（5 步驟標準） |
| 4. 約束規則 | ✅ | read-only / 禁止改 source / 路徑限制 |
| 5. 完成回報格式 | ✅ | agent 應回報的內容（路徑、size、records 數） |

完整 schema 見 `_design/L3_EXPORT_PROMPT_SCHEMA.md` + Contract B.3。

### 13a.4 JSON 權威結構（D-039 + DF §9）

```
{
  "manifest": { ... },
  "records": [
    { "record_type": "entity", ... },
    { "record_type": "dialogue_line", ... },
    { "record_type": "art_metadata", ... }
  ]
}
```

- **權威 schema = DF §9**（D-039 + CODEX C-04 解決）
- record_type 三類（entity / dialogue_line / art_metadata）
- 一對一映射 SPEC §5.2 frontmatter（DF §9.7）
- UD 六區降為 **derived adapter view**（非 export 權威；UD §12.7）

詳見 Contract A.7。

### 13a.5 輸出檔位置 + git 管理（D-038 附帶第 3 項；v1.1 校正 CC-07）

- 建議檔名：`export/<instance_id>_<YYYYMMDD>_<HHMMSS>.json` + `export/<instance_id>_<YYYYMMDD>_<HHMMSS>.md`
- 位置：Instance root `export/` 目錄
- 加入 `.gitignore`（export 是衍生產物）
- 同次 export 同時產 JSON + MD 兩檔（D-024 雙吐）
- **export 跑完後 phase_log 不寫入任何 entry**（v1.1 master 第四輪 CC-07 校正；對齊 L3_EXPORT_PROMPT_SCHEMA §1.4 read-only constraints；原「補一筆 phase: export entry」supersede）
- **理由：** Layer 3 Export 為純 read-only contract；不視為 pipeline event；export 紀錄由外部 agent 在 chat 中回報（L3_EXPORT_PROMPT_SCHEMA §1.5 完成回報格式），不污染 phase_log

### 13a.6 與既有 §13 / §14 4 個 /export-* 的區分

| 維度 | 既有 §13.4 / §14 4 個 `/export-*` skill | v1.1 Layer 3 Export（A1 prompt） |
|---|---|---|
| 觸發 | Claude skill | 前端 Export 按鈕產 prompt → user 貼 → agent 跑 |
| 輸出格式 | 單一 .md 整合檔（view/<topic>.md） | JSON + MD 雙吐（export/） |
| 用途 | 給人讀 / 離線分享 | 給外部轉檔（引擎 / i18n / 工具鏈） |
| 涵蓋 entity | 上游 Bible（W / C / P / CH） | 全 Instance entity（含 dialogue / A-* / phase_log） |
| 狀態 | DERIVED（重 export 即更新） | 同概念但分開命名（見 §13a.5） |
| 是否新增 skill | 否（既有 4 個維持） | **否**（不新增；用 A1 prompt 流程） |

**兩條 export 路徑共存** — 不互相取代。

### 13a.7 Pending（無）

Layer 3 Export 流程完整對齊 D-038 + D-039 + UX §11.6.11 + L3_EXPORT_PROMPT_SCHEMA。

---

# 14. Skill 清單與雙語別名

**Q14-1=C：** 英文主名稱 + 中文別名（兩者指向同一個 skill 實作）。

| 英文主名稱 | 中文別名 | 觸發 | 模式 |
|---|---|---|---|
| `/init-project` | `/初始化專案` | 00_i | 一次性 |
| `/create-world` | `/建立世界觀` | 00_e | 創建 |
| `/iterate-world` | `/迭代世界觀` | 00_j（W） | 迭代 |
| `/view-world` | `/查看世界觀` | 動態組合 | 閱讀 |
| `/export-world` | `/匯出世界觀` | 寫 view/ | 閱讀 |
| `/create-character` | `/建立角色` | 00_f | 創建 |
| `/iterate-character` | `/迭代角色` | 00_j（C） | 迭代 |
| `/view-character` | `/查看角色` | 動態組合 | 閱讀 |
| `/export-character` | `/匯出角色` | 寫 view/ | 閱讀 |
| `/create-relationship` | `/建立關係` | 00_l（C-7 新增） | 創建 |
| `/iterate-relationship` | `/迭代關係` | 00_j（R） | 迭代 |
| `/create-outline` | `/建立大綱` | 00_g | 創建 |
| `/iterate-outline` | `/迭代大綱` | 00_j（P） | 迭代 |
| `/view-outline` | `/查看大綱` | 動態組合 | 閱讀 |
| `/export-outline` | `/匯出大綱` | 寫 view/ | 閱讀 |
| `/create-detailed-outline` | `/建立細綱` | 00_h | 創建 |
| `/iterate-detailed-outline` | `/迭代細綱` | 00_j（CH） | 迭代 |
| `/view-detailed-outline` | `/查看細綱` | 動態組合 | 閱讀 |
| `/export-detailed-outline` | `/匯出細綱` | 寫 view/ | 閱讀 |
| `/diagnose` | `/診斷` | 通用模式 | 分析 |
| `/integrate` | `/整理` | 通用模式 | 寫檔 |
| `/scene-task` | `/場景任務包` | 00_k 階段 1 | 執行 |
| `/dialogue-write` | `/生成台詞` | 00_k 階段 2 | 執行 |
| `/qa` | `/檢查` | 00_k 階段 3 | QA |
| `/status` | `/進度` | 動態掃 frontmatter | 監控 |
| `/check-gaps` | `/缺漏檢查` | 動態掃 frontmatter | 監控 |

**雙語實作策略**（C-10 裁決：選 A wrapper + smoke test）：
- Skill 主實作只寫一份（英文名）
- 中文別名透過 wrapper（symlink 或 redirect 內容）指向主實作
- Phase A 新增 wrapper smoke test 任務，實際驗證中文觸發時 agent 確實執行英文主 skill 的流程
- 跨 host（Claude Code / CODEX APP）相容性問題在 smoke test 暴露
- 不重複內容、不需要同步維護

### 14a. 既有 4 個 `/export-*` skill 不擴 JSON 輸出（v1.1 對齊 D-038）

> **v1.1 附註 via D-038（partial supersede 否決選項）：** §14 既有 4 個 `/export-*` skill（`/export-world` / `/export-character` / `/export-outline` / `/export-detailed-outline`）**維持單一 .md 整合檔輸出（view/）**；**不擴 JSON 輸出**。  
> **理由：** Layer 3 Export JSON+MD 雙吐走獨立 A1 prompt 流程（§13a），不擾動既有 4 skill 的「人讀視圖」用途。  
> **對應 D-046 #4 + CODEX C-12 / O-02 解決：** 不存在的 `/export-dialogue` skill 不新增；前端「複製 /export-* 指令」按鈕全部移除（UX §11.6.11.7），改為「開啟 Export panel」（Layer 3 Export A1 prompt 流程）。

---

# 15. 模式系統（既有 10 種模式）

既有 `00_a 台詞生產協議` 已定義完整模式系統，重啟版**直接沿用**，不需重新設計。

| 模式 | 用途 | 是否可產出正式內容 |
|---|---|---|
| 診斷模式 | 分析資料、判斷風格、找缺漏 | 否 |
| 整理模式 | 將資料轉成模板欄位 | 可產出 DRAFT |
| 探索模式 | 開放式發想、尋找可能性 | 否 |
| 試寫模式 | 產出可比較台詞草稿 | 否 |
| 破格模式 | 故意突破安全寫法尋找亮點 | 否 |
| 收斂模式 | 整合亮點、修正偏離 | 可產出 REVIEW 候選 |
| QA 模式 | 檢查 AI 味、聲線、資訊、禁用詞 | 否 |
| 交稿模式 | 輸出乾淨可保存版本 | 可產出 FINAL 候選 |
| Codex 執行模式 | 將已確認結論寫入 repo | 視任務 |
| 人類裁決模式 | 決定例外、風格核心、final / locked | 是 |

**模式與上游創建協議的關係：**
- 協議的「階段 1 診斷」對應模式系統的「診斷模式」
- 協議的「階段 2 探索／補洞」對應模式系統的「探索模式」
- 協議的「階段 3 收斂」對應模式系統的「收斂模式」
- 協議的「階段 4 Codex 執行」對應模式系統的「Codex 執行模式」

**模式與下游台詞生產 pipeline 的關係：**（見第 12.4 節完整對應表）
- `/scene-task` 內部：診斷模式 + 整理模式
- `/dialogue-write` 內部：試寫模式 / 破格模式 / 收斂模式
- `/qa` 內部：QA 模式
- 定稿階段：交稿模式 + 人類裁決模式

`/diagnose`、`/integrate` 兩個通用 skill 是「直接呼叫某個模式」的入口，不綁定特定協議。

---

# 16. 文件狀態機

```text
                       人類確認
DRAFT  ────────►  REVIEW  ────────►  FINAL  ────────►  LOCKED
  │                  │                  │                  │
  │                  │                  │                  │
  └──────────────────┴──────────────────┴─────────►  DEPRECATED
                                                       （任何狀態都可廢棄）
```

| 狀態 | 完成度 | 規則 | 作用範圍 |
|---|---|---|---|
| DRAFT | 25% | 草稿，可大幅修改 | 全域 |
| REVIEW | 75% | 可使用，但需審核 | 全域 |
| FINAL | 100% | 人類確認定稿（需 QA 通過） | 全域 |
| LOCKED | 100% | 已鎖定，不得擅自改動核心內容 | 全域 |
| DEPRECATED | 不計入 | 已棄用，不得正式引用 | 全域 |
| APPLIED | 不計入 | 補丁類已套用，僅供溯源 | `archive/` 補丁專用 |
| DERIVED | 不計入 | 衍生整合檔（由 `/export-*` 產生），不可手改 | `view/` 目錄專用 |

**狀態升級限制：**
- AI / CODEX **不得自行**把 DRAFT 升 REVIEW、REVIEW 升 FINAL、FINAL 升 LOCKED
- 升級必須由人類審查後執行（見 TASKS 各 phase 結尾的「REVIEW gate」任務）
- LOCKED 文件的核心內容不得擅自修改
- DEPRECATED 文件不得正式引用，除非任務明確要求溯源
- DERIVED 文件**不可被直接修改**，要更新就重跑 `/export-*`

### 16a. LOCKED → DEPRECATED 降級流程（v1.1 新增 via D-040 + D-046 #5）

> **v1.1 partial supersede via D-040（LOCKED Save guard）+ D-046 #5（降級欄位改 09_e）+ CODEX C-15 / C-16 / O-03 解決**  
> **適用範圍：** §16 既有狀態機 7 種狀態維持；本子節補「LOCKED → DEPRECATED 降級的具體流程 + 紀錄位置」  
> **north-star 對齊理由：** SPEC §16 既有「LOCKED 文件的核心內容不得擅自修改」但未明示降級流程；UX 前端工具需具體規範（Save race guard）；DF 強調「既有 frontmatter 零破壞」，故降級紀錄不擅加 frontmatter 欄位

**降級流程 — 兩步（v1.1 確認）：**

1. **修改 frontmatter `狀態` 欄位** — 只動既有合法欄位 `狀態：LOCKED → 狀態：DEPRECATED`（這個欄位本身在 §5.2.1 中文 header 5 欄位內）
2. **在 09_e final-gating 紀錄檔補一條完整降級紀錄** — 含降級理由 / 日期 / 操作人 / 影響

**禁止：**
- **不新增** frontmatter 欄位（如「降級理由」「降級日期」「降級人」） — partial supersede UX v0.2 §11.5.3 舊寫法（CODEX C-16 + O-03 + DF「既有 frontmatter 零破壞」原則）
- **不走 skill** — 無 `/deprecate-scene` 之類（D-031「本輪不新增 skill」）
- **狀態機由人類控制** — agent / CODEX 不擅自降級

**LOCKED Save race guard（D-040 + CODEX C-15 解決）：**

前端 Save flow 必須在實際寫檔前**重讀最新 source header**；若最新 `狀態=LOCKED` 則禁止 overwrite，僅允許三選項：
- (A) 複製降級指令 — 走上述兩步降級流程
- (B) 另存為 DRAFT proposal — 新檔不違反 §16 升級限制
- (C) 取消 — 留 Editor 不 Save

詳見 Contract B.2 + UX §11.5.7-9。

**降級紀錄 schema：** 09_e final-gating 紀錄段落格式（含 LOCKED → DEPRECATED 條目）由上下游 specialist 在 UD §3.6.3 / §3.6.6 細化（NS-NEW-1 Pending；前端引導必對齊最終格式）。

---

# 17. 作品專屬 00_b 的擴充策略

上游 4 個協議（00_e、00_f、00_g、00_h）跑完後，都會貢獻內容到 Instance 的作品專屬 `00_b 反 AI 味檢查表`。為避免互相覆寫，採用「**固定 section anchors + 各協議只能寫自己的 section**」策略。

## 17.1 00_b 固定 Section Anchors（鎖定）

Template 的通用骨架 `00_b` 在 Phase A 由 CODEX 建立時必須包含以下固定 section（順序鎖定，名稱鎖定）：

```text
## 1. 作品類型語氣定位          ← 00_e 寫入
## 2. 髒話尺度與死亡處理偏好    ← 00_e 寫入
## 3. 規模定位                  ← 00_g 寫入
## 4. 類型偏移風險清單          ← 00_g 寫入
## 5. 角色偏移檢查清單          ← 00_f 寫入（每角色一個 ### 子節）
## 6. 高風險場景的處理方式      ← 00_h 寫入（每場景類型一個 ### 子節）
## 7. 經驗累積的偏移案例        ← 日常使用 / 人類手動寫入
```

## 17.2 寫入規則

| 協議 | 可寫 section | 寫入方式 |
|---|---|---|
|---|---|---|
| 00_e 世界觀 | §1、§2 | **覆寫**（每跑一次協議重寫此區段，含「上次跑此協議的時間戳」） |
| 00_f 角色 | §5 | **append 子節**（新角色 → 新增 `### <角色名>`；既有角色 → 更新該子節） |
| 00_g 大綱 | §3、§4 | **覆寫** |
| 00_h 細綱 | §6 | **append 子節**（新場景類型 → 新增；既有 → 更新） |
| 人類手動 | §7 | 自由編輯 |

## 17.3 衝突標記

當協議偵測到「自己負責的 section 已有內容，但與本次想寫的差異 > 50%」時：
- 不擅自覆寫
- 標 `<!-- CONFLICT: 上次寫入 YYYY-MM-DD，本次想改為... -->` 並請人類確認
- 待人類拍板後再執行

## 17.4 跨 repo 規則

- Template 的 `00_b`：通用骨架，只列 7 個 section 標題與簡短說明
- Instance 的 `00_b`：完整作品專屬內容
- Template 升級時，Instance 不自動同步（需手動 cherry-pick）

跑完上游後，Instance repo 的 `00_b` 已從通用骨架擴充為作品專屬版，可用於後續下游 `/qa` 的類型偏移檢查（09_f）。

---

# 18. 給 CODEX 審查者的提醒（第二輪修正完成）

本文件搭配 `ARCHITECTURE.md` 與 `TASKS.md` 一起閱讀。三份文件分工：

| 文件 | 回答什麼 |
|---|---|
| `SPEC.md`（本文件） | What & Why — 設計目標、決策、邏輯模型 |
| `ARCHITECTURE.md` | How — 檔案結構、frontmatter、skill 實作方式 |
| `TASKS.md` | When & In What Order — 4 階段拆解、任務、驗收條件 |

**第二輪修正已吸收 CODEX 全部 10 必修 + 7 優化：**

**A 類（純不一致）：**
- M1：SPEC 前段舊術語已清（5.2 改為 canonical schema、第 4 節決策表更新、第 2.4 節 `entity:` 改 `entities:`）
- M2：A.4 依賴改為 A.0，引用 SPEC 5.2 / ARCHITECTURE 2.2 / ARCHITECTURE 7.3
- 狀態機補 DERIVED 且明確作用範圍
- C.4/C.5 對調並改為「測試 DERIVED 只允許 view/」

**B 類（新增內容）：**
- M3：B.5.5、D.2.5、D.3.5 三個 REVIEW gate 任務已新增
- M4：A.5 `.protocol_version` schema 含 `phase_log`、A.7 `/status` 讀 manifest + phase_log
- M6：A.4 同時補 entities + depends_on + weight；ARCHITECTURE 7.3 表已加 depends_on 欄位
- A.0 parser/helper 前置任務（含 O1 normalized return spec）

**C 類（設計決策）：**
- C-7=B：00_l 關係創建協議 + /create-relationship + 04_a/04_b 才標 R-* （而非 00_l 自身）
- C-9=C：depends_on frontmatter 欄位 + ARCHITECTURE 5 雙路反查邏輯
- C-10=A：wrapper + smoke test

**M7 狀態分層（新增）：**
- `狀態` = 文件成熟度
- `pipeline_state` = 場景在下游 pipeline 走到哪
- `mode_tag` = 試寫模式
- `qa_decision` = QA 結論
- 12.3 場景狀態機已用 `pipeline_state` 改寫

**M8 下游閉環（新增）：**
- D.3.5 收斂 gate：trial → 收斂 → QA 為預設路徑
- 例外路徑（trial 直接 QA）明確規範

**M9 QA 鎖定（新增）：**
- `/qa` 必跑 **8 份**（09_a/b/c/d/f/g/h/i；v1.1 / D-043 — 從 5 份擴為 8 份）
- `09_e` 拆出，不由 `/qa` 產生（人類在 final-gating 時填）

**M10 跨檔 link（新增）：**
- canonical schema 加入 scene_id / source_task / source_dialogue / qa_type
- `.protocol_version.phase_log` 加入 task_path / dialogue_paths / target_dialogue / qa_report_paths（M4 下游追蹤）

**第三輪追加修正（CODEX 第三輪回饋）：**
- 9 項必修全部落地（M7/M10 三份對齊、A.0 parser 下游欄位、phase_log 下游追蹤、A.9 依賴 A.5-A.8、B.6.5 主線 REVIEW gate、B.5 依賴 B.4、C.2 移除 view 重生驗收、D.3 `--converge` contract、TASKS 1.4 全域文件頭規則、SPEC 2.4 狀態列表補 APPLIED/DERIVED）

**本輪設計提交審查項：**

1. 第一、二、三輪所有回饋是否實質吸收？
2. M7 狀態分層三維度（狀態 / pipeline_state / mode_tag / qa_decision）parser 是否能穩定區分？
3. M10 跨檔 link（source_task / source_dialogue + phase_log 下游追蹤）是否真的可實作？
4. REVIEW gates 共 6 個（A.10、B.5.5、B.6.5、B.8、D.2.5、D.3.5）順序與覆蓋是否完整？
5. `--converge` 三輸入形態（試寫／破格／收斂）對 parser 與 skill 都清楚？
6. A.0 parser 的 enum 驗證是否涵蓋所有狀態？
7. 是否還有任何阻塞問題？或可以開始 Phase A.0 實作？

審查通過後，從 A.0 開始實作。
