狀態：DRAFT  
版本：v0.2  
最後更新：2026-05-18  
適用範圍：依需求 refresh + Bucket #1-#4 拍板重新拆分三個 specialist 第二輪工作項  
優先級：最高  

**v0.2 修訂說明：** Bucket #1-#4 user 拍板完成後，§7「v0.2 修訂節」**supersede** §2 specialist 任務表 + §3 user 拍板項；§1 / §4 / §5 仍有效；後續 specialist 第二輪以 §7 為準。

# REVISED_WORK_ITEMS — 需求 refresh 後的修訂工作項拆解

# 0. 文件目的

依 `GAP_ANALYSIS.md` 結論，重新拆分：

1. 三個 specialist 第二輪各自的具體任務（≤ 10 條 per specialist）
2. user 可直接拍板項目（不用 specialist 評估）
3. 既有產物可整批繼承不動的項目
4. 新優先順序與啟動條件

**閱讀順序：** §1 新優先順序 → §3 user 直接拍板項（要先處理）→ §2 specialist 任務 → §4 繼承不動項 → §5 啟動條件。

**搭配文件：** `GAP_ANALYSIS.md`（本檔的依據）、`DECISIONS_LOG.md`（新增 D-NNN / P-NNN）。

---

# 1. 新優先順序

## 1.1 概念層優先順序（依需求 refresh 四大情境）

```
D（視覺化管理）      ━━━━━━━━━━━━━  最高 — 影響 user 對「目前到哪了」的掌控
C（高品質台詞 + 客製化輸出）  ━━━━━━━━━━━  高 — 核心生產目的
B（拆解成評測標準 / 可迭代文件） ━━━━━━━━  中 — 銜接 A 跟 C
A（與 AGENT 對話建立）        ━━━━━━     低 — 可被「手稿導入」+ 外部 AI 替代
```

## 1.2 實作層優先順序（依依賴關係調整）

依賴關係不能違反，因此實作順序仍維持 Phase A → B → C → D 骨架，但**內部任務優先級重排** + **新增手稿導入快速路徑**：

```
Phase 0.5（新增）：手稿導入快速路徑
  └ /import-world / /import-character / /import-outline
  └ 重用 /create-* 階段 4「自動拆分」邏輯
  └ 讓 user 繞過 A 的對話流程，B/C/D 仍能消費

Phase A（原計畫，優先級降低）：
  └ /create-* 5 階段對話 skill
  └ user 可選擇用此路徑或用 Phase 0.5 路徑
  └ 實作可放到最後

Phase B / C / D（原計畫）：
  └ Phase C 視 D 視覺化需求順序可微調
  └ Phase D 視覺化管理升優先級（與資料層任務並行可行的部分）
```

## 1.3 Specialist 第二輪啟動順序

**舊順序（PHASE_3_COMPLETION_REPORT v3.0）：** 資料格式 → 上下游 → UX（嚴格序）

**新順序：** **三個並行可行**，理由：

- 資料格式第二輪需求**大幅增加**（新增 entity 類型 + i18n KEY + export template schema），但與 UX 與上下游無依賴
- 上下游第二輪需求**大幅增加**（手稿導入 skill + 輸出模板 skill + 對應協議），與資料格式有部分依賴（新 entity 類型確定後才能寫對應協議）
- UX 第二輪需求**升優先級**（D 視覺化），與資料格式 / 上下游無強依賴（UX §2–§6 既有規則 §0/§1/§7/§8 已建立）

**建議並行策略：**
- UX **立即啟動** — UX §2–§6 完全不依賴另兩個 specialist 第二輪
- 資料格式 **立即啟動** — 新議題（§4.1–§4.3）獨立可推進
- 上下游 **等資料格式拋出新 entity 類型清單後啟動**（短延遲，不必等資料格式全完成）

---

# 2. 三個 Specialist 第二輪任務拆解

## 2.1 資料格式 Specialist 第二輪（短—中工期）

**Owner：** 資料格式 specialist  
**產出：** `_design/DATA_FORMAT_SPEC.md`（v0.1）  
**任務數：** 8 條（≤ 10）

| # | 任務 | 對應 GAP / 議題 | 工期 | 優先級 |
|---|---|---|---|---|
| DF-1 | 正式 formalize D-018 6 項最終裁決，§2「強制檢視議題的結論」明文交付 | 既有 D-018 / P-006 | S | 中 |
| DF-2 | 正式提案 `.protocol_version.phase_log` 加 `status` 欄位（promote P-012） | 既有 P-012 | S | 中 |
| **DF-3** | **設計「客製化輸出表現格式」schema 機制** — Export template 對應的 frontmatter 欄位、template 檔案格式、output adapter contract（partial supersede D-018 #6 / D-003） | **GAP §4.1 / P-016（新）** | **L** | **高** |
| **DF-4** | **設計 i18n KEY 機制 schema** — 每段台詞 KEY 欄位（行內註解 / metadata block）、KEY 命名規則、全 repo unique guarantee、canon delta / retcon 下 KEY 處理（partial supersede D-018 #2） | **GAP §4.2 / P-017（新）** | **M** | **高** |
| **DF-5** | **設計新 entity 類型擴充** — I-`<item_id>` / A-`<asset_id>` / UI-`<element_id>` 等（依 user 拍板範圍）；命名規則、目錄結構、frontmatter 欄位、與既有 C-* / V 等的 cross-reference 規則（partial supersede SPEC §5.1） | **GAP §4.3 / P-018（新）** | **L** | **高** |
| DF-6 | §5「對既有 27 份模板 frontmatter 的遷移影響」— 新 schema 變動是否影響既有檔（預期：最小影響） | 例行 | S | 中 |
| DF-7 | §6「對 A.0 parser 的影響」— 新欄位 / 新 entity 類型如何影響 parse_frontmatter.py 設計 | 例行 + GAP §4.1–§4.3 | M | 高 |
| DF-8 | §7「需 master 裁決問題清單」— 任何 schema 設計過程中無法獨立決定的議題 | 例行 | S | 中 |

**禁止越界（重申）：**
- 不擅自決定「客製化輸出 template 的具體內容」（屬上下游）— 只設計 schema 與機制
- 不擅自設計呈現（屬 UX）
- 不擅自 supersede D-018 / SPEC LOCKED 項目 — 必須在 §7 列為「建議 master 裁決」並引用 P-016/017/018

**Cross-ref：** DECISIONS_LOG D-018 / D-019（新）/ P-006 / P-012 / P-016 / P-017 / P-018

## 2.2 上下游 Specialist 第二輪（中工期）

**Owner：** 上下游 specialist  
**產出：** 補完 `_design/UPSTREAM_DOWNSTREAM_SPEC.md` § 9 + 新增章節  
**任務數：** 9 條（≤ 10）

| # | 任務 | 對應 GAP / 議題 | 工期 | 優先級 |
|---|---|---|---|---|
| UD-1 | 補 §9「需 master 裁決問題清單」集中段，對齊 P-009 ~ P-015 七項暫定方案，每項給正式提案（方案 / 替代 / 等待裁決理由） | 既有 P-009 ~ P-015 | S | 中 |
| **UD-2** | **設計手稿導入快速路徑** — 評估 `/import-world` `/import-character` `/import-outline` 新 skill vs `/create-* --from-draft` 參數重用；含 algorithm（解析手稿 → 分塊 → 拆分 → 補 frontmatter → 寫檔）；輸出 §10「手稿導入」新章節 | **GAP §4.4 / P-019（新）** | **M** | **高** |
| **UD-3** | **設計輸出模板協議（00_m）** — 客製化輸出表現格式的 skill 行為、template 檔案結構、output adapter 流程；對應 GAP §4.1 / DF-3 schema 機制 | **GAP §4.1 / P-016（新）** | **L** | **高** |
| **UD-4** | **設計新 entity 類型對應的創建協議** — 依資料格式 DF-5 結論的 entity 類型，撰寫 00_x 創建協議（如 00_n 物品創建協議、00_o 資產 metadata 協議）；含 5 階段共通骨架 + 專屬區段 | **GAP §4.3 / P-018（新）** | **L** | **高** |
| **UD-5** | **新增 dialogue 檔的 i18n KEY 寫入規範** — 08_b 模板更新、`/dialogue-write` algorithm 加 KEY 生成步驟、KEY 命名規則對應；對應 DF-4 schema | **GAP §4.2 / P-017（新）** | **M** | **高** |
| UD-6 | A 優先級降低後，調整 §1.1–§1.5 各 `/create-*` 5 階段協議的「optional / required」標記 — 標明哪些議題在「手稿導入路徑」下可省略 | GAP §3.1 + §3.3 | S | 中 |
| UD-7 | 更新 §2「下游 00_k」— 新增 output template 整合在 `pipeline_state` 末段（如 `EXPORT_PENDING` / `EXPORTED` 是否需要新狀態，需 master 裁決） | GAP §4.1 | M | 中 |
| UD-8 | 既有 P-009（08_a §11.1 修正）落地 — 寫入 D.4 / D.5 任務的具體 patch | 既有 P-009 | S | 中 |
| UD-9 | 新增 §11「跨 entity 類型的 cross-reference 規則」— 物品被角色使用、立繪歸屬角色、台詞引用立繪等的引用語法 | GAP §4.3 | M | 中 |

**禁止越界（重申）：**
- 不擅動 SPEC §5.2 canonical schema 核心 — 任何 schema 變動由資料格式 specialist 設計
- 不擅自設計呈現 — 凡涉及「使用者看到什麼」標 `[UX]`
- 不擅自新增 entity 類型 enum — 由資料格式 specialist 統一

**Cross-ref：** DECISIONS_LOG P-009 ~ P-015 + P-016 / P-017 / P-018 / P-019

## 2.3 UX Specialist 第二輪（中工期，升優先級）

**Owner：** UX specialist  
**產出：** 補完 `_design/UX_SPEC.md` §2 / §3 / §4 / §5 / §6 / §9 / §10  
**任務數：** 10 條（含本輪新增）

| # | 任務 | 對應 GAP / 議題 | 工期 | 優先級 |
|---|---|---|---|---|
| UX-1 | 補完 §2「`/view-*` 4 個 skill Markdown 模板」（world / character / outline / detailed-outline） | 既有 Batch 2 | M | 高 |
| UX-2 | 補完 §3「`/export-*` 檔案 layout 與 `/view-*` 差異」 | 既有 Batch 2 | M | 高 |
| UX-3 | 補完 §4「`/status` 看板格式」依 §1.1 / §1.2 平移條目；含進度條 + 實體完成度雙層呈現 | 既有 Batch 3 | M | **最高（D 視覺化核心）** |
| UX-4 | 補完 §5「6 個 REVIEW gate 清單格式」依 §1.2 通用骨架 | 既有 Batch 3 | M | 高 |
| UX-5 | 補完 §6「QA 5+1 報告閱讀體驗 + 彙整版」依 §1.1 Severity 在前、§1.2 Affected 精確到行 | 既有 Batch 4 | M | 高 |
| UX-6 | 對齊 UPSTREAM §7 53 個 [UX] 標記（UX-1 ~ UX-53），每個標記給呈現設計 | 既有 Batch 5 | L | 高 |
| **UX-7** | **設計手稿導入 skill 的視覺化呈現** — 「工具吃進了什麼、拆解成什麼」的 chat layout + 預覽段；對應 UD-2 手稿導入路徑 | **GAP §4.4** | **M** | **中** |
| **UX-8** | **設計新 entity 類型的視覺化呈現** — `/view-item` / `/view-asset` 等新 view skill 的 Markdown 模板（依 UD-4 確定的新類型範圍） | **GAP §4.3** | **M** | **中** |
| **UX-9** | **設計「客製化輸出表現格式」的 chat 預覽呈現** — `/export-<template>` 跑完後在 chat 中顯示什麼摘要、template 衝突時如何呈現 | **GAP §4.1** | **M** | **中** |
| UX-10 | 補 §9 [NEEDS_SCHEMA_SUPPORT] 集中清單 + §10 需 master 裁決問題清單；含 **P-020 HTML 路徑可行性議題** 的呈現選項清單（給 user 之後拍板用） | 既有 + GAP §5.4 / P-020 | S | 中 |

**禁止越界（重申）：**
- 不引入 GUI 元件 — HTML 路徑等 P-020 拍板後再決定（本輪維持純 Markdown）
- 不更動 canonical schema — 凡需要新欄位標 `[NEEDS_SCHEMA_SUPPORT]`
- 不設計 skill 觸發機制 — 屬上下游

**對 P-020 的特殊責任：** UX specialist 在 §10 列出「若恢復 HTML 路徑，純 Markdown 設計哪些部分會被取代、哪些仍保留」 — 讓 user 之後拍板時有對照基準；本輪不實際做 HTML 設計。

**Cross-ref：** DECISIONS_LOG P-020（新） + UPSTREAM §7 53 個 UX 標記

---

# 3. User 可直接拍板項目（不用 specialist 評估）

**理由：** 下列議題涉及 scope 取捨或 user 主觀偏好，由 user 直接決定比 specialist 推導快且準。

## 3.1 GAP §5 五項衝突的最終裁決（必須）

| # | 衝突 | 候選方案 | master 暫定 | 需 user 拍板 |
|---|---|---|---|---|
| H1 | 客製化輸出格式 vs D-018 #6 / D-003 | (a) partial supersede / (b) 最小可行版 / (c) 完全不做 | (a) | ✗ |
| H2 | i18n KEY vs D-018 #2 | (a) partial supersede / (b) 維持不動 | (a) | ✗ |
| H3 | 新 entity 類型 vs SPEC §5.1 LOCKED | (a) 正式增列 / (b) 自訂類型機制 / (c) 漸進式擴充 | (c) | ✗ |
| H4 | HTML 路徑 vs UX_SPEC §1.4 | (a) 恢復 / (b) 維持純 Markdown / (c) 暫不拍板 | user 已答 (c) | ✓ |
| H5 | A 優先級降低 vs Phase 依賴 | (a) 新增手稿導入 / (b) 改 Phase 序 / (c) A 與 D 並行 | (a) | ✗ |

## 3.2 GAP §4.3 新 entity 類型本輪納入範圍（必須）

依 user 提到的具體類別，本輪建議納入哪些？user 拍板後資料格式 DF-5 與上下游 UD-4 才能精確設計。

候選類型：
- `I-<item_id>` — 物品 / 道具（user 明示）
- `A-<asset_id>` — 美術資產 metadata：立繪、圖片、SE、配音檔等引用（user 明示「立繪」）
- `UI-<element_id>` — UI 文案：按鈕、教學、提示等（master 推測，user 未明示）
- `SKILL-<id>` — 技能說明（master 推測，user 未明示）
- 其他 user 想到的類別

**user 需明示：** 本輪納入哪幾類？哪些先 reserve 等下次 refresh？

## 3.3 GAP §4.1 客製化輸出 template 本輪納入範圍（必須）

user 已明示兩種 template：
- 角色台詞 + 立繪 + i18n KEY
- 物品名 + 物品說明 + 物品圖片

候選擴充：
- UI 文案輸出
- 字幕 / 配音稿
- 遊戲引擎特定格式（Unity / Unreal / RPG Maker / Twine 等）
- 玩家分支條件 metadata
- 本地化導出（PO / JSON i18n / Excel）

**user 需明示：** 本輪 export template 涵蓋哪幾種？哪些先 reserve？

## 3.4 GAP §3.1 Phase A 實作排序（可選但建議拍板）

A 路徑（`/create-*` 5 階段對話）的 skill 實作：
- (i) Phase D 後再做
- (ii) 跟 Phase D 並行做
- (iii) 跟手稿導入路徑（Phase 0.5）一起做
- (iv) 完全跳過，只保留設計

**user 暫定建議：** (i) 或 (ii) — 因 user 表示「可以先設計，但實作優先度低」

## 3.5 GAP §6.4 A.0 解除條件更新（必須）

舊解除條件（PHASE_3_COMPLETION_REPORT v3.0）：
1. UX §2–§6 補完
2. 上下游 §9 補完
3. DATA_FORMAT 釐清

新解除條件建議（依需求 refresh）：
1. UX §2–§6 補完
2. 上下游 §9 + 手稿導入 + 輸出模板 + 新 entity 創建協議補完
3. DATA_FORMAT 正式交付（含新 schema 擴充）
4. **新增：** §3.2 / §3.3 user 拍板新 scope 範圍

**user 需確認：** 是否同意新解除條件，或要更嚴格 / 更寬鬆？

---

# 4. 既有產物可整批繼承不動

下列產物在需求 refresh 後**完全不動**，繼續使用：

## 4.1 主文件 LOCKED 段（除 §5.1 partial supersede 待 H3 拍板）

- SPEC §1（專案定位）/ §2（需求總覽 — 但需在 §2.4 注記新 scope 擴充）/ §4（18 項設計決策匯總）
- SPEC §5.2（canonical schema）/ §5.3（完成度公式）/ §5.4（expected entity manifest）
- SPEC §16（文件狀態機）/ §17（作品專屬 00_b）
- ARCHITECTURE 全文（會有局部追加，但既有內容不刪不改）
- TASKS §1.4（全域文件頭）/ §1.5（錯誤呈現）/ §1.6（全文呈現）/ §1.7（A.0 暫停）
- 6 個 REVIEW gate 編號 + 26 個 skill 清單（會新增，但既有不動）

## 4.2 既有 D / P 條目

- D-001 ~ D-010 全部維持
- **D-018** 6 項中 4 項維持最終不採（retcon / continuity_check / scene 粒度 / protected_tier）
- D-018 第 2 項（多語言）partial supersede — 不存多語本文維持，但需提供 i18n KEY
- D-018 第 6 項（特殊資料格式）partial supersede — 客製化輸出機制本輪設計
- P-001 ~ P-005 維持 Pending（與本次需求 refresh 無關）
- P-009 ~ P-015 維持 Pending（待 UD-1 補 §9 後對齊）

## 4.3 UPSTREAM_DOWNSTREAM_SPEC.md substantive 內容

- §0–§8 全部 ≈90% 交付內容**完全不動**
- §1.1–§1.5 五份協議的 40 議題提問腳本完整保留
- §2 下游 00_k 全內容保留
- §3 6 份 QA 模板保留
- §4 dialogue-write 三模式 algorithm 保留
- §5 canon delta 框架保留
- §6 多場景並行保留
- §7 53 個 UX 標記保留

## 4.4 UX_SPEC.md 已交付段

- §0 全文約束（純 Markdown / 中文主＋英文 sub / 三守則）
- §1 prior draft 吸收結論（含 1.4 HTML 廢棄 — 但 P-020 預留可行性討論）
- §7 跨檔導航設計（連結基準 / breadcrumb / TOC / source 引用 / 單向 reference）
- §8 錯誤呈現結構（四件套 / 兩種口氣 / 空狀態 / 多錯誤彙整 / 不暴露 enum）

## 4.5 既有 Bible 27 份模板

- 不刪不改；A.4 frontmatter 補完任務維持（schema 微擴充後重評工作量，但既有目標不變）

---

# 5. 啟動條件與里程碑

## 5.1 第二輪 specialist 啟動條件（修訂）

| Specialist | 舊條件 | 新條件 |
|---|---|---|
| 資料格式 | 等使用者釐清 P-006 | **user 對 §3.1 H1/H2/H3 + §3.2 + §3.3 拍板後立即啟動** |
| 上下游 | 等資料格式完成 | **user 對 §3.1 H1/H2/H3/H5 + §3.2 + §3.3 拍板後立即啟動；可與資料格式並行** |
| UX | 等資料格式 + 上下游完成 | **user 對 §3.1 H4 確認後立即啟動；可與資料格式 + 上下游並行** |

## 5.2 第二輪交付里程碑

```
M1：user 拍板 §3.1–§3.5 全部
   ↓
M2：三個 specialist 第二輪並行啟動
   ↓
M3.1：UX §2–§6 + §9 + §10 補完（升優先級）
M3.2：DATA_FORMAT_SPEC.md v0.1 交付（含新 schema 擴充）
M3.3：UPSTREAM §9 對齊 + 新 §10/§11 手稿導入 + 輸出模板 + 新 entity 創建協議交付
   ↓
M4：master 第三輪整合對話
   - 升 INTEGRATION_CONTRACTS v1 → v2
   - 整合到主 SPEC / ARCHITECTURE / TASKS
   - promote P-009~P-015 / P-016~P-020 為 D-NNN（或 supersede）
   - 修訂 PHASE_3_COMPLETION_REPORT v4.0
   ↓
M5：宣告是否可進 Phase A.0（含新 Phase 0.5 手稿導入路徑）
```

## 5.3 預估工期（粗估，純 specialist 工作時間）

| 階段 | 估計 |
|---|---|
| §3 user 拍板 | 1 個對話回合（本回合或下回合） |
| 資料格式第二輪 | 5–8 小時 specialist 對話 |
| 上下游第二輪 | 6–10 小時 specialist 對話（含手稿導入 + 輸出模板 + 新 entity 協議） |
| UX 第二輪 | 5–8 小時 specialist 對話 |
| master 第三輪整合 | 3–5 小時對話 |

**總計：** 約 20–32 小時 specialist + master 工作；可並行壓縮至 12–20 小時。

---

# 6. 文件維護紀律

- 本檔由 master 對話維護；任何修訂須記入版本欄
- §2 三個 specialist 任務一旦啟動，task ID（DF-N / UD-N / UX-N）即鎖定，編號不重排
- §3 user 拍板項目一經 user 明示，記入 DECISIONS_LOG D-NNN（新編號 D-019+）
- 本檔 v0.1 → v0.2 升版：§7 supersede §2 / §3；§1/§4/§5 仍有效；後續 specialist 第二輪以 §7 為準
- 本檔升 REVIEW 條件：specialist 第二輪交付對齊本檔結論
- 本檔升 FINAL 條件：master 第四輪整合完成

---

# 7. v0.2 修訂：Bucket #1–#4 lock 後的任務重整

依 Bucket #1-#4 user 拍板（記入 `DECISIONS_LOG.md` v0.6 §6.6 / `REQUIREMENTS_LOCK.md` v1.0），本節 supersede §2 specialist 任務表 + §3 user 拍板項目。三 specialist 對話以本節為準。

## 7.1 §3 user 直接拍板項目的解決狀態（v0.2 終結）

| # | 衝突 | v0.1 狀態 | v0.2 終結 |
|---|---|---|---|
| H1 | 客製化輸出格式 vs D-018 #6 / D-003 | 暫定 (a) | **RESOLVED via D-024** — scope 大幅縮減為 JSON+MD 雙吐 |
| H2 | i18n KEY vs D-018 #2 | 暫定 (a) | **RESOLVED via D-022** — KEY 機制本輪設計 |
| H3 | 新 entity 類型 vs SPEC §5.1 LOCKED | 暫定 (c) | **RESOLVED via D-023 + D-025** — A-\* 本輪 + 其他類別接口 |
| H4 | HTML 路徑 vs UX_SPEC §1.4 | 暫定 (c) | **RESOLVED via D-029 + D-030** — HTML web UI 拍板 |
| H5 | A 優先級降低 vs Phase 依賴 | 暫定 (a) | **RESOLVED via D-031** — 改用既有跳階段機制 |
| §3.2 | 新 entity 類型本輪範圍 | 待 user 拍板 | **RESOLVED via D-025** — 本輪：角色台詞 + A-\*；I-\*/UI-\*/SKILL-\* 留接口 |
| §3.3 | 客製化輸出 template 本輪範圍 | 待 user 拍板 | **RESOLVED via D-024** — 一個 export skill 吐 JSON+MD 雙檔；不做多 template |
| §3.4 | Phase A 實作排序 | 候選 (i)/(ii)/(iii)/(iv) | **RESOLVED via D-019** — A 優先級低；Phase D 後或與 D 並行 |
| §3.5 | A.0 新解除條件 | 待 user 確認 | **RESOLVED**：三 specialist 第二輪並行完成 + master 第四輪整合（細節見 §7.5）|

## 7.2 §1.3 specialist 啟動順序更新（v0.2）

舊（v0.1 §1.3）：UX 立即 + 資料格式立即 + 上下游短延遲

新（v0.2）：**三 specialist 全部並行可行**（user 已對所有 H1-H5 + §3.2/3.3 拍板）

```
階段 1A：資料格式 specialist 第二輪    立即啟動
階段 1B：UX specialist 第二輪          立即啟動
階段 1C：上下游 specialist 第二輪      立即啟動（部分等資料格式 JSON schema）
                                          ↓ 三者全交付後
階段 2：master 第四輪整合對話
```

## 7.3 資料格式 Specialist v0.2 任務（supersede §2.1）

**Owner：** 資料格式 specialist  
**產出：** `_design/DATA_FORMAT_SPEC.md` v0.1  
**核心輸入：** REQUIREMENTS_LOCK §3 + §8.1

| # | 任務 | 對應 D/P | 工期 |
|---|---|---|---|
| DF-1 | 正式 formalize D-018 6 項最終裁決於 §2「強制檢視議題的結論」 | D-018 / P-006 | S |
| DF-2 | 正式提案 `.protocol_version.phase_log` 加 `status` 欄位 + `import_source` 欄位 | P-012 / D-031 | S |
| **DF-3** | **設計 i18n KEY 機制 schema** — KEY 在 frontmatter / 行內註解 / metadata block 哪一處；命名規則細節（如 `dlg.<chapter>.<scene>.<line>`）；alias mapping 內部結構；全 repo unique guarantee 機制 | **D-022 / P-022** | **M** |
| **DF-4** | **設計 A-\* entity schema** — 命名規則（如 `A-portrait-<character>-<state>`）、目錄結構、frontmatter 欄位（metadata 含名稱/所屬角色/標籤）、與 C-\* cross-reference 語法、KEY 機制（同 i18n） | **D-023 / P-021** | **M** |
| **DF-5** | **設計可擴充 entity 類型 registry** — schema 機制讓 user 在 Instance bootstrap 時自訂類型（如未來加 I-\* / UI-\* / SKILL-\*）；A.0 parser 配合改動 | **D-025 / P-023** | **M** |
| **DF-6** | **設計可擴充 qa_type enum 機制** — 變開放 list；含「QA 模組擴充協議」（00_p）對應 schema 接點 | **D-027 / P-023** | **S—M** |
| **DF-7** | **設計 JSON 中介格式 schema**（Layer 3 export 輸出） — 對齊 SPEC §5.2 既有 frontmatter；含 KEY + A-\* metadata + 全 entity 類型 | **D-024 / P-024** | **M** |
| **DF-8** | **新增 mode_tag enum 增 SINGLE_ITER** + qa_type 增 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY 的 schema 級紀錄 | **D-026 + D-028** | **S** |
| DF-9 | §5「對既有 27 份模板 frontmatter 遷移影響」 — 新 schema 變動是否影響既有 | 例行 | S |
| DF-10 | §6「對 A.0 parser 影響」 — 完整對照表 | 例行 | S |
| DF-11 | §7「需 master 裁決問題清單」（即使為空也明示） | 例行 | S |

**禁止越界：**
- 不擅自決定「JSON 中介格式具體欄位」之外的 schema 變動
- 不擅自設計呈現（屬 UX）
- 不擅自 supersede 既有 D；無法獨立決定者升 §7 master 裁決

## 7.4 上下游 Specialist v0.2 任務（supersede §2.2）

**Owner：** 上下游 specialist  
**產出：** 補完 `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §9 + 新增章節  
**核心輸入：** REQUIREMENTS_LOCK §4 + §6 + §8.2

| # | 任務 | 對應 D/P | 工期 |
|---|---|---|---|
| UD-1 | 補 §9「需 master 裁決問題清單」集中段，對齊既有 P-009 ~ P-015 七項暫定，每項給正式提案 | P-009 ~ P-015 | S |
| **UD-2** | **文件化「跳階段機制做手稿導入」use case** — 不是新 skill；在 UPSTREAM §1.0.2 跳階段觸發語字典補使用案例 + trust-level 參數行為（`agent_assisted` / `external_llm`）；定義 entity 命名衝突 4 選項處理（merge / overwrite / create-as-new / skip） | **D-031 + D-032 + D-033 / P-028** | **M** |
| **UD-3** | **設計 Layer 3 export skill** — 一個 export skill 吐 JSON + MD 雙檔；對齊資料格式 DF-7；觸發方式（CLI / 前端按鈕 / agent 指令）；輸出檔放哪 / git 管理 | **D-024 / P-030** | **M** |
| **UD-4** | **設計 A-\* 美術資產對應協議** — 候選編號 00_q（如本輪要寫）；含創建 / 修改 / 刪除流程；對齊資料格式 DF-4 schema | **D-023 / D-025** | **M** |
| **UD-5** | **新增 dialogue 檔的 i18n KEY 寫入規範** — 08_b 模板更新；`/dialogue-write` algorithm 加 KEY 生成步驟；KEY 改名工作流 | **D-022 / P-022** | **M** |
| **UD-6** | **新增 09_g / 09_h / 09_i QA 模板內容** — 各自 algorithm（節奏感 / 對話張力 / 跨場一致性）；跨場 QA 的「跨」範圍定義 | **D-026 / P-025** | **L** |
| **UD-7** | **新增 `/dialogue-write --single-iter` 模式 algorithm** — 跟既有三模式如何切換 / 共用元件；mode_tag 在 phase_log 紀錄 | **D-028 / P-027** | **M** |
| **UD-8** | **評估可擴充 QA 機制 + 00_p 可擴充 QA 協議是否本輪撰寫** — user-defined 門檻（user 寫 yaml / agent 助攻 / 工具預設範本） | **D-027 / P-026** | **S—M** |
| UD-9 | A 優先級降低後調整 §1.1-§1.5 各 `/create-*` 協議「optional / required」標記 | D-019 | S |
| UD-10 | 更新 §2 下游 00_k — 對齊新 pipeline_state 行為 + import_source 紀錄 | D-031 | M |
| UD-11 | 既有 P-009（08_a §11.1 修正）落地寫入 D.4 / D.5 任務 | P-009 | S |
| UD-12 | 新增 §11「跨 entity 類型的 cross-reference 規則」 — 含 A-\* 與 C-\* 引用 | D-023 / D-025 | M |

**禁止越界：**
- 不擅動 SPEC §5.2 canonical schema 核心（屬資料格式）
- 不擅自設計呈現（標 `[UX]`）
- 不擅自新增 skill — 跨議題涉及新 skill 升 master

## 7.5 UX Specialist v0.2 任務（supersede §2.3）

**Owner：** UX specialist  
**產出：** 補完 `_design/UX_SPEC.md` §2-§6 + §9-§10 + **新增 §11「HTML 前端工具設計」大塊**  
**核心輸入：** REQUIREMENTS_LOCK §5 + §8.3

| # | 任務 | 對應 D/P | 工期 |
|---|---|---|---|
| **UX-1** | **§1.4 partial supersede 重寫** — 明示「HTML 整層廢棄」適用範圍縮小至 L1 chat + L3 export；L2 前端工具採 HTML web UI 為例外 | **D-030** | **S** |
| UX-2 | 補完 §2「`/view-*` 4 個 skill Markdown 模板」（仍適用 L1 純 Markdown 場景） | 既有 | M |
| UX-3 | 補完 §3「`/export-*` 檔案 layout」 — **v0.2 scope 縮減**：只設計「JSON + MD 雙吐」export 的 chat 與檔案呈現 | 既有 + D-024 | S—M |
| UX-4 | 補完 §4「`/status` 看板格式」依 §1.1 / §1.2 平移條目 | 既有 | M |
| UX-5 | 補完 §5「6 個 REVIEW gate 清單格式」 | 既有 | M |
| UX-6 | 補完 §6「QA 報告閱讀體驗 + 彙整版」 — **v0.2 scope 擴大**：含 09_a-i 共 8 份 + 09_e 彙整版 | 既有 + D-026 | M |
| UX-7 | 對齊 UPSTREAM §7 53 個 [UX] 標記（UX-1 ~ UX-53），每標記給呈現設計 | 既有 | L |
| **UX-8** | **新增 §11.1「F1 全局看板」前端設計** — 含實體完成度進度條 / 「下一步建議」邏輯 / 「複製指令」按鈕（A 路徑入口） | **D-029 + D-034 / P-029** | **L** |
| **UX-9** | **新增 §11.2「F2 場景切換 + 自動 context 裝載」前端設計** | **D-029 / P-029** | **M** |
| **UX-10** | **新增 §11.3「F3 多版本並排對比」前端設計** — 並列幾欄 / 捲動行為 / 亮點 highlight | **D-029 / P-029** | **L** |
| **UX-11** | **新增 §11.4「F6 搜尋 + 篩選」前端設計** — facet 設計（按 entity 類型 / 狀態 / qa_type） | **D-029 / P-029** | **M** |
| **UX-12** | **新增 §11.5「F7 直接編輯 + LOCKED 守門」前端設計** — 編輯 UI（行內 / popup / modal）；LOCKED 警示呈現；手動 Save 互動 | **D-029 / P-029** | **L** |
| **UX-13** | **新增 §11.6「前端跟 agent 完全分離」UX 邊界規範** — 雙視窗工作流；「複製指令」按鈕 context 內容；refresh 機制 | **D-029 + D-034 / P-029** | **M** |
| **UX-14** | **新增 §11.7「多場景並行 + 編輯衝突偵測」前端 UX** — tab / 多分頁 / save 時 checksum 偵測 | **D-029 / P-029** | **M** |
| **UX-15** | **新增 §11.8「前端 build / package / 分發」規格** — 本地 web server 啟動方式 + 依賴安裝 | **D-029 / P-029** | **S** |
| UX-16 | 補 §9 [NEEDS_SCHEMA_SUPPORT] 集中清單（即使全「無」也要明示） | 既有 | S |
| UX-17 | 補 §10 需 master 裁決問題清單（即使為空也要明示） | 既有 | S |

**禁止越界：**
- 不擅自更動 canonical schema — 凡需要新欄位標 `[NEEDS_SCHEMA_SUPPORT]`
- 不設計 skill 觸發機制（屬上下游）
- L1/L3 純 Markdown 設計與 L2 HTML 前端設計**邏輯分開**，但同份文件交付（UX_SPEC v0.2）

## 7.6 啟動條件與里程碑（v0.2，supersede §5）

```
M1：user 對 H1-H5 + §3.2/3.3/3.4/3.5 全部拍板    ✓ 已完成（Bucket #1-#4）
   ↓
M2：三 specialist 第二輪並行啟動                  ← 當前狀態
   ↓
M3.1：資料格式 DATA_FORMAT_SPEC.md v0.1 交付（含 DF-1 ~ DF-11）
M3.2：UX UX_SPEC.md v0.2 交付（含 UX-1 ~ UX-17，新增 §11 前端工具大塊）
M3.3：上下游 UPSTREAM_DOWNSTREAM_SPEC.md v0.2 交付（含 UD-1 ~ UD-12）
   ↓
M4：master 第四輪整合對話
   - 升 INTEGRATION_CONTRACTS v1 → v2
   - 整合到主 SPEC / ARCHITECTURE / TASKS（含 §5.1 entity 擴 A-\* / §5.2.4 enum 擴展 / 三層架構入 §2）
   - promote P-021 ~ P-030 為 D-NNN（或 supersede）
   - 修訂 PHASE_3_COMPLETION_REPORT v4.0 為 final
   - 重評可進 A.0 條件
   ↓
M5：宣告是否可進 Phase A.0 / Phase 0.5（手稿導入 use case）
```

**預估工期（粗估）：**

| 階段 | 估計 |
|---|---|
| 資料格式第二輪 | 8–12 小時（DF-3/4/5/6/7 加重） |
| 上下游第二輪 | 12–18 小時（UD-2/3/4/5/6/7/8 加重；09_g/h/i 算 6-8 小時） |
| UX 第二輪 | 15–25 小時（UX-8 ~ UX-15 前端工具新增大塊） |
| Master 第四輪整合 | 4–6 小時 |

**總計：** 約 40–60 小時 specialist + master；並行可壓縮至 25–40 小時。

## 7.7 §4 既有產物可整批繼承不動清單（v0.2 確認）

§4 既有產物清單**完全有效**，本輪不變動。明示維持的核心：
- SPEC §4 18 項 + §5.2 canonical schema 核心 + §5.3 + §5.4 + §16 + §17
- ARCHITECTURE 全部框架
- TASKS §1.4 / §1.5 / §1.6 / §1.7
- 6 個 REVIEW gate
- UPSTREAM §0-§8 substantive 內容 ≈ 90%
- UX_SPEC §0 / §1（除 §1.4）/ §7 / §8
- 既有 27 份 Bible 模板
- **26 個 skill 清單**（v0.2 確認不新增 skill — D-031 確立改用既有跳階段機制）

## 7.8 v0.2 結論

- 三個 specialist 第二輪可立即並行啟動
- 任務拆解完整、依賴清晰、編號連續
- 預估工期合理（40-60 小時，並行壓縮可達 25-40 小時）
- A.0 暫停仍維持，解除條件 = M2 + M3.1/2/3 + M4 全部完成
- specialist 啟動建議使用對應 `_design/SPECIALIST_STARTER_*.md` 啟動包，**外加閱讀本檔 §7 + REQUIREMENTS_LOCK + DECISIONS_LOG §6.6**
