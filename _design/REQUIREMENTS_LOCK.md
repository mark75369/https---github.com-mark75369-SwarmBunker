狀態：FINAL
版本：v1.0
最後更新：2026-05-18
適用範圍：需求 refresh 後 4 bucket 拍板的完整需求快照 / 設計修補的權威來源
優先級：最高

# REQUIREMENTS_LOCK — 需求 refresh + 4 Bucket 拍板快照

# 0. 文件性質與使用方式

本檔是「**需求面 lock 文件**」 — 把使用者在新 master 對話中經過 4 個 Bucket 討論後的所有需求 + 設計拍板**完整凍結**，作為後續所有設計修補的權威依據。

**閱讀對象：**
- 新 master 對話（自己；後續輪迭代時 ground truth）
- 三個 specialist 第二輪對話（依此 lock 細化各自 scope）
- 未來重啟 master 整合對話的接手 agent
- user 自己（rolling 確認需求對齊）

**對其他文件的關係：**

```
                    REQUIREMENTS_LOCK.md（本檔）
                          │
                          ↓ 衍生 / 對齊
       ┌──────────────────┼──────────────────────┐
       ▼                  ▼                      ▼
GAP_ANALYSIS.md   REVISED_WORK_ITEMS.md   DECISIONS_LOG.md
（缺口分析）        （任務拆解）            （決策紀錄）
       │                  │                      │
       └──────────────────┴──────────────────────┘
                          ↓
              PHASE_3_COMPLETION_REPORT.md
                  （階段完成度判定）
```

**本檔不是：** 實作規格（屬 specialist spec）/ 操作手冊（屬 protocol） / 任務拆解（屬 TASKS）。

**本檔狀態：** **FINAL** — 4 個 bucket 已逐項 user 拍板；本輪不再變動；若有後續變更開新版本（v1.1+）。

---

# 1. 整體需求 refresh 摘要（user 原意）

來源：`REQUIREMENTS_REFRESH` v0.1（user 提供）+ 4 個 Bucket 追問深化。

## 1.1 工具需求分階段

| 階段 | 內容 | 優先級 |
|---|---|---|
| **A** | 與 AGENT 討論、整理世界觀 / 人設 / 大綱細綱 | **低** — user 可用外部 GPT/Claude 處理，但有 context 導入問題；工具仍要設計但實作延後 |
| **B** | 將世界觀 / 人設放入工具後，分析拆解成台詞生成判斷與評測標準 | 中 |
| **C** | 大綱、細綱、人設、世界觀就位後，依資訊產出符合世界觀、人物設定、低 AI 味的台詞 + 客製化輸出 | 高 |
| **D** | 視覺化管理專案進度與各種世界觀、人設、劇本、台詞資料 | **最高** |

## 1.2 四大關鍵使用情境

| # | 情境 | 對應實作 |
|---|---|---|
| A | 與 AGENT 討論生成世界觀 / 人設 / 大綱細綱 | 既有 `/create-*` 5 階段對話（≈ 90% 完整）|
| B | 將世界觀 / 人設 / 大綱細綱放入工具，拆解成可迭代文件 | 既有 `/scene-task` + 拆分邏輯（≈ 100% 完整）|
| C | 利用 B 的文件產出高品質台詞 + 輸出指定格式 | 既有 `/dialogue-write` + `/qa`（≈ 100% 完整） + **本輪新增 export 機制** |
| D | 方便管理文件 + 方便在 AGENT 產出討論文件和台詞 | **本輪新增前端工具（重大）** |

## 1.3 工具定位（scope 重新校準）

| 維度 | 原既有設計假設 | 需求 refresh 後 |
|---|---|---|
| 工具用途 | 長篇遊戲劇本 + 台詞生產 | **遊戲文字資料庫 + 多格式輸出** |
| 資料類別 | 敘事相關（W/V/C/R/P/CH/S） | 敘事 + 美術資產 + 留接口給未來類別 |
| 輸出端 | chat 內呈現 + 08_b 固定 dialogue 模板 | **JSON + Markdown 雙吐固定中介格式**；引擎特定轉檔工具外處理 |
| 上游入口 | 對話建立 | **對話建立 + 跳階段機制做手稿導入**（雙路徑） |
| 視覺化呈現 | 純 Markdown agent 對話 + view/export | **+ HTML web UI 前端工具**（含 F1/F2/F3/F6/F7 5 必要功能） |

---

# 2. 整體三層架構（Bucket #1 拍板）

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1：Authoring（撰寫層）                                    │
│  agent 對話 + /dialogue-write + /qa + Markdown source           │
│  ← 既有設計沿用 + i18n KEY 機制 + 跳階段手稿導入                  │
└─────────────────────────────────────────────────────────────────┘
                                ↓ source 寫好 / 改好
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2：前端工具（管理 + 編輯）                                 │
│  HTML web UI / 本地 web server / 手動 Save                       │
│  必要功能：F1 看板 + F2 切換 + F3 並排對比 + F6 搜尋篩選 + F7 編輯  │
│  跟 agent 完全分離（雙視窗工作流）                                │
└─────────────────────────────────────────────────────────────────┘
                                ↓ 要交付時
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3：Export（輸出層）                                       │
│  一個 export skill → 吐 JSON + MD 雙檔                          │
│  「轉檔到引擎」明確劃在工具外                                      │
└─────────────────────────────────────────────────────────────────┘
```

**典型 user session：**

1. Terminal: `python serve.py` 啟動前端 server
2. 瀏覽器: `localhost:xxxx` 開前端 UI
3. F1 看板看實體完成度 + 該做什麼
4. F2 切到場景 → 看現有台詞 / 立繪 KEY / QA 狀態
5. 想改 → F7 直接編輯 → Save → 寫回 .md
6. 想跟 agent 討論 → 開外部 Claude Code / Cowork → agent 改寫回 .md
7. 切回前端瀏覽器 refresh → 看到 agent 結果
8. 結束時手動 `git commit`

---

# 3. 資料層拍板（Bucket #1）

## 3.1 資料類別範圍

| 類別 | 本輪實作 | 來源 |
|---|---|---|
| 敘事相關（W/V/C/R/P/CH/S） | ✓ **既有沿用** | SPEC §5.1 |
| **A-\* 美術資產 metadata** | ✓ **本輪新增** | 需求 refresh + Bucket #1 |
| I-\* 物品 / 道具 | ✗ 本輪不實作，**留接口** | 需求 refresh 提到但 user 1.3 / 1.6 拍板 reserved |
| UI-\* UI 文案 | ✗ 本輪不實作，**留接口** | 預想擴充 |
| SKILL-\* 技能說明 | ✗ 本輪不實作，**留接口** | 預想擴充 |
| 其他未來類別 | ✗ 本輪不實作，**留接口** | 預想擴充 |

**接口設計需求：** schema 必須支援「**未來新增 entity 類型不必動 SPEC §5.1 核心**」的擴充機制（user-defined entity type registry）。

## 3.2 i18n KEY 機制

| 項目 | 拍板內容 |
|---|---|
| **每段台詞需 unique KEY** | 是 |
| **KEY 產生方式** | 工具自動產語意可讀預設（如 `dlg.ch01.s03.l001`）；user 可隨時改名 |
| **KEY 改名後** | 預設名內部記為 alias；工具保證 alias mapping 不 break |
| **KEY 穩定性** | KEY 跟內容/編號完全解耦；場景重編號 / 台詞改寫 KEY 不變 |
| **多語言對白** | **不存** — 仍維持 D-018 #2「不採多語對白」；KEY 只供外部 i18n 系統引用 |
| **KEY 命名空間** | 全 repo unique guarantee |

## 3.3 A-\* 美術資產 entity

| 項目 | 拍板內容 |
|---|---|
| **存什麼** | KEY + metadata（名稱、所屬角色、表情/狀態標籤）|
| **不存什麼** | 實檔（.png/.jpg 等）、檔案路徑、URL — 一律不存 |
| **怎麼用** | source frontmatter / 內文用 KEY 引用（如 `立繪：A-portrait-主角A-default`）|
| **實檔對應** | 由外部系統（Unity / 引擎 / 等）自己對應 |
| **A-\* 命名** | 工具自動產預設 + user 可改名；同 i18n KEY 機制 |

## 3.4 套版機制 scope 縮減

| 項目 | 拍板內容 |
|---|---|
| **原 P-016 彈性多套版** | **大幅 scope 縮減** |
| **本輪實作** | 一個 export skill → 吐 JSON + MD 雙檔 |
| **JSON 用途** | 給外部轉檔 script 吃，產引擎要的格式 |
| **MD 用途** | 給人讀的版本 |
| **不做** | 多套版 framework / `/create-template` skill / 工具預設提供常見套版 / 套版輸出預覽 / 多套版同跑批次 |
| **「轉檔到引擎」責任** | 明確劃在**工具外** |

---

# 4. QA 評測層拍板（Bucket #2）

## 4.1 QA 模板擴充

| 既有 | 本輪新增 | 用途 |
|---|---|---|
| 09_a AI 味 | — | 不動 |
| 09_b 聲線一致性 | — | 不動 |
| 09_c 禁用詞 | — | 不動 |
| 09_d 資訊控制 | — | 不動 |
| 09_e final-gating 紀錄（不在 QA pipeline） | — | 不動 |
| 09_f 類型偏移 | — | 不動 |
| — | **09_g 節奏感** | 句長分布 / 句長變異度 / 長短句交替 / 段落呼吸感 |
| — | **09_h 對話張力** | 推進 / 讓步 / 揭穿 / 反擊頻率 + 攻防力度量化 |
| — | **09_i 跨場一致性** | 跨場聲線漂移 / 跨場資訊洩漏 / 跨場節奏 arc |

**新總計：8 份 QA 模板 + 1 份 final-gating（09_e）= 9 份**

**新 qa_type enum：** `RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY`

## 4.2 可擴充 QA 機制

| 項目 | 拍板內容 |
|---|---|
| **目的** | 未來 user 可追加 / 調整評測標準 |
| **schema** | qa_type enum 變**可擴充 list**（不再 LOCKED 的 5 種）|
| **新增「QA 模組擴充協議」** | 候選編號 00_p；定義新 09_x 怎麼接入 pipeline |
| **既有 QA 模組微調** | 沿用既有「作品專屬 00_b」設計（Instance 微調已涵蓋）|
| **partial supersede** | D-018 #3 continuity_check 不採 — 不採「獨立實體」維持，但**新增跨場 QA pipeline** 與**可擴充機制** |

## 4.3 /dialogue-write 模式擴充

| 既有 3 模式 | 本輪新增 |
|---|---|
| 試寫 v01A/B/C（`DRAFT_TRIAL`）| — 沿用 |
| 破格 v01D（`EXPERIMENTAL`）| — 沿用 |
| 收斂 v02（`CONVERGENCE`）| — 沿用 |
| — | **單版本迭代（`SINGLE_ITER`）** — agent 寫一版 → user 跟 agent 迴圈改 → OK |

**新 mode_tag enum：** `SINGLE_ITER`

**partial supersede P-010** — 原「不新增 /iterate-dialogue」改為「**沿用既有 /dialogue-write + 加 `--single-iter` 參數**」；不新增 skill。

## 4.4 手稿導入路徑分支

| 路徑 1：agent_assisted | 路徑 2：external_llm |
|---|---|
| user 已在外部用 agent 工具編輯過 | user 從外部 LLM 直接得到，未經審 |
| 導入後**可跳 QA**，直接進 `DIALOGUE_FINAL` 之類後段 pipeline_state | 導入後**必走完整 QA pipeline**，先進 `DRAFT` |
| 假設品質可信 | 假設品質未驗證 |
| phase_log 紀錄 `import_source: agent_assisted` | phase_log 紀錄 `import_source: external_llm` |

---

# 5. 前端工具層拍板（Bucket #3）

## 5.1 Form factor 與必要功能

| 項目 | 拍板內容 |
|---|---|
| **Form factor** | **HTML web UI**（partial supersede UX_SPEC §1.4「HTML 整層廢棄」）|
| **F1 全局看板** | ✓ 必要 — 含實體完成度進度條 |
| **F2 場景切換 + 自動 context** | ✓ 必要 |
| **F3 多版本並排對比** | ✓ 必要 — 前端工具的「真正價值」之一 |
| F4 立繪預覽 | ✗ 不做 — 跟「只存 KEY」一致；工具不知實檔在哪 |
| F5 圈選傳 agent | ✗ 不做 — 用文字描述「我要 A 第 2 句」 |
| **F6 快速搜尋 + 篩選** | ✓ 必要 |
| **F7 直接點台詞編輯 + LOCKED 守門** | ✓ 必要 — 前端工具的「真正價值」之一 |
| F8 依賴反查視覺化 | ✗ 不做 |
| F9 套版輸出預覽 | ✗ 不做（套版機制已縮減）|
| F10 批次篩選多套版同跑 | ✗ 不做 |

## 5.2 內部架構

| 維度 | 拍板內容 |
|---|---|
| **回寫機制** | **(c) 手動 Save** — 改完按 Save 才寫回 .md；git history 乾淨 |
| **跟 agent 整合度** | **(α) 完全分離** — 前端 = viewer/editor；agent 對話另外開（Claude Code / Cowork）；雙視窗工作流 |
| **執行模型** | **(ii) 本地 web server** — python `http.server` 或 FastAPI；瀏覽器開 `localhost`；可讀寫檔 |

## 5.3 A 路徑入口（從 Bucket #4 對齊）

| 項目 | 拍板內容 |
|---|---|
| **前端有沒有 A 對話入口** | 有 — 但是「**複製指令**」按鈕 |
| **點按鈕的行為** | 複製 `/create-world` 等指令 + context（已有設定摘要）到剪貼簿 |
| **user 接著做** | 切到外部 chat（Claude Code / Cowork）貼上去跑 |
| **為什麼這樣** | 符合 (α) 完全分離 — 前端不主動執行 agent；user 控節奏 |

---

# 6. A 路徑 + 手稿導入拍板（Bucket #4）

## 6.1 A 路徑 5 個 `/create-*` skill

| 項目 | 拍板內容 |
|---|---|
| **設計內容** | UPSTREAM §1.1-§1.5 既有 ≈ 90% **完全保留不動** |
| **實作優先級** | **低**（D-019：Phase D 後或與 D 並行）|
| **跑在哪** | **外部 chat** — Claude Code / Cowork（Bucket #3 (α) 完全分離） |

## 6.2 手稿導入機制

| 項目 | 拍板內容 |
|---|---|
| **機制** | **重用既有跳階段機制** — 不新增 `/import-*` skill |
| **觸發方式** | user 在 `/create-world` 對話中說「**直接寫檔**」 → agent 跳階段 4 自動拆分 |
| **手稿格式要求** | **至少要有 markdown structure**（`#` / `##` 段落分割）；frontmatter 工具自動補；純文字不吃 |
| **trust-level 分支** | `--trust-level agent_assisted`（跳 QA）/ `external_llm`（走完整 QA） |
| **entity 命名衝突** | **偵測同名 → 問 user**：merge / overwrite / create-as-new / skip 四選；user 逐項拍板 |

> **註（master 第四輪 CC-06 細化 / CODEX d2 NF-D2-01 對齊；不改 v1.0 lock 原文）：** v1.0 lock 的「trust-level 分支」描述為 v1.0 寫法。後續 D-031 + D-038 細化 + CODEX C-08 拍板：`--trust-level` **嚴格限上游 `/create-*` skill**，**不影響下游 pipeline**；下游 `/scene-task` / `/dialogue-write` / `/qa` 永遠走標準 DRAFT → QA → REVIEW → FINAL，**兩條 trust-level 路徑下游皆走完整 8 份 QA**。詳見 Contract A.8 + UD §10.3 v0.3 + SPEC §5.4a + DF §3.3 v0.3。本表 v1.0 lock 原文保留不動。

---

# 7. 對既有設計的衝擊總覽（partial supersede 清單）

下列既有設計條目本輪有衝擊；衝擊形式與處理方式如下：

| # | 既有設計 | 衝擊類型 | 處理 |
|---|---|---|---|
| 1 | SPEC §5.1 邏輯實體類型 7 種（LOCKED） | partial supersede — 新增 A-\* | 漸進式擴充；未來類別接口預留 |
| 2 | SPEC §5.2.4 狀態三維度 enum（5 種 qa_type LOCKED） | partial supersede — qa_type 增 3 種變可擴充 | qa_type 不再 LOCKED |
| 3 | SPEC §5.2.4 狀態三維度 enum（5 種 mode_tag LOCKED） | partial supersede — mode_tag 增 SINGLE_ITER | mode_tag 不再 LOCKED |
| 4 | D-003「特殊資料格式 Phase D 後另議」 | partial supersede — 本輪設計 JSON+MD 雙吐 | scope 縮減版 |
| 5 | D-018 #2「多語言不採」 | partial supersede — 不存多語本文維持，但加 KEY 機制 | 區分對待 |
| 6 | D-018 #3「continuity_check 不採」 | partial supersede — 不採獨立實體維持，但加跨場 QA + 可擴充 | 區分對待 |
| 7 | D-018 #6「特殊資料格式 Phase D 後另議」 | partial supersede — 本輪設計縮減版 export | 同 #4 |
| 8 | P-010「不新增 /iterate-dialogue」 | partial supersede — 改成 /dialogue-write `--single-iter` | 改實作方式 |
| 9 | UX_SPEC §1.4「HTML 整層廢棄」 | partial supersede — HTML web UI 為前端工具 form factor | HTML 回歸 |
| 10 | UX_SPEC §2/§3/§4/§5/§6 補完任務 | scope 擴大 — 拆兩塊：純 Markdown layout + HTML 前端工具 layout | 任務拆分 |
| 11 | P-016「客製化輸出表現格式機制」 | scope 大幅縮減 | 改寫為 JSON+MD 固定雙吐 |
| 12 | P-019「手稿導入路徑」 | 細化 — 沿用跳階段機制 + trust-level 分支 | 不新增 skill |
| 13 | P-020「HTML 路徑可行性」 | promoted | 已 lock HTML web UI |

**完全不衝擊的核心（明示）：**
- SPEC §4 18 項設計決策匯總
- SPEC §5.2 canonical schema 核心（中文 header + YAML）
- SPEC §5.3 完成度公式
- SPEC §5.4 expected entity manifest
- SPEC §16 文件狀態機（7 種狀態）
- SPEC §17 作品專屬 00_b 擴充策略
- 6 個 REVIEW gate（A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5）
- ARCHITECTURE 全部框架
- TASKS §1.4 / §1.5 / §1.6
- D-001 ~ D-017（時期 B/C 既有）
- D-018 #1 retcon / #4 scene 粒度 / #5 protected_tier（維持 4 項最終不採）
- UPSTREAM §0-§8 substantive 內容（≈ 90% 不動）
- UX_SPEC §0 / §1 / §7 / §8 已交付段
- 既有 27 份 Bible 模板

---

# 8. 留給 specialist 第二輪的細節清單

下列項目 user 不必拍板，標 `[SPECIALIST_TBD]` 留給對應 specialist 第二輪設計：

## 8.1 給資料格式 specialist

- A-\* entity 的具體 frontmatter schema（命名規則、metadata 欄位、cross-reference 語法）
- i18n KEY 在台詞檔內的具體標記方式（行內註解 / frontmatter / metadata block）
- KEY 命名規則細節（如 `dlg.<chapter>.<scene>.<line>` vs `dlg.<scene_id>.<line>`）
- KEY alias mapping 的內部表現結構
- qa_type 變「可擴充 list」的 schema 機制
- 「user-defined entity type registry」schema 設計
- JSON 中介格式具體欄位（DF-5 設計）
- phase_log 新增 `import_source` 欄位
- 跳階段機制下 trust-level 紀錄

## 8.2 給上下游 specialist

- 09_g / 09_h / 09_i 各自的具體檢查 algorithm
- 跨場 QA 的「跨」範圍：跨章 / 跨集 / 主角 arc 全長
- 可擴充 QA 機制 user-defined 門檻：user 寫 yaml 規則 / agent 助攻 / 工具預設範本
- /dialogue-write `--single-iter` mode 具體 algorithm
- 手稿導入 markdown structure 解析 algorithm（哪些 `##` 對應哪個分拆檔）
- entity 命名衝突 4 選項（merge / overwrite / create-as-new / skip）具體行為定義
- /scene-task 反查精度（太多 / 太少時怎麼辦）
- L3 export 觸發方式（CLI / 前端按鈕 / agent 指令）
- 「QA 模組擴充協議」00_p 內容（如本輪要寫）

## 8.3 給 UX specialist

- F1 看板「下一步建議」邏輯（純展示 raw status vs 工具自動推薦）
- F3 並排對比的視覺結構（並列幾欄、捲動行為、亮點 highlight）
- F6 搜尋 / 篩選的 facet 設計（按 entity 類型 / 狀態 / qa_type / 等）
- F7 直接編輯的 UI 細節（行內編輯 / popup editor / 模態框）
- LOCKED 守門在前端呈現：警示 modal / 標灰不可點 / 引導跑 `/iterate-*`
- 多場景並行：tab / 多瀏覽器分頁 / 單一視圖
- 編輯衝突偵測機制（user 改 + agent 同時改）
- 「複製指令」按鈕 context 該複製哪些資訊
- 前端 build / package / 分發方式
- L3 export 的前端入口與預覽（如有）

---

# 9. 整體優先級（依本檔 lock）

## 9.1 概念層優先級

```
D（視覺化管理 / 前端工具）   ━━━━━━━━━━━━━━━━━  最高
C（高品質台詞 + 客製化輸出）  ━━━━━━━━━━━━━━     高
B（拆解成評測標準）          ━━━━━━━━━━           中
A（與 AGENT 對話建立）       ━━━━━━              低
```

## 9.2 實作層優先級（依 specialist 第二輪工作）

```
階段 1（並行可行）：
  1A — 資料格式 specialist 第二輪
       含 A-* schema / i18n KEY / 可擴充 entity 類型 / 可擴充 qa_type / phase_log 擴充
  1B — UX specialist 第二輪
       含純 Markdown layout（§2-§6 補完）+ HTML 前端工具 UX 設計
  1C — 上下游 specialist 第二輪
       含 09_g/h/i / SINGLE_ITER mode / 手稿導入細化 / entity 名稱衝突 / L3 export 機制

階段 2：master 第三輪整合
  整合三個 specialist 交付 → 升 INTEGRATION_CONTRACTS v2 → 更新主 SPEC/ARCHITECTURE/TASKS
  → 修訂 PHASE_3_COMPLETION_REPORT v4.0 為 final
  → 重評可進 A.0 條件

階段 3：可進 A.0（如裁決通過）
  Phase 0.5（手稿導入快速路徑）vs Phase A.0+（正規實作）
```

---

# 10. 文件維護紀律

- 本檔是「**需求 lock 快照**」 — 一旦版本 lock 後不修改條目；後續變更開新版本（v1.1+）
- 每個條目須能對應到 Bucket #1-#4 的明確討論段落
- specialist 第二輪交付前不變動本檔；交付後若有真實需求衝突由 master 第三輪整合處理
- 本檔的 §7「partial supersede 清單」是 DECISIONS_LOG 新增 D-NNN 的依據
- §8「specialist TBD 清單」是 REVISED_WORK_ITEMS specialist 任務的依據
