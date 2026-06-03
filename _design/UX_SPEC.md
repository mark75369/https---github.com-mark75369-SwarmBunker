狀態：LOCKED
版本：v0.4（master 第四輪整合 pre-LOCKED patch 完成 + CODEX (d2) PASS）
最後更新：2026-05-19
適用範圍：UI/UX specialist 對話的設計結論（含第二輪 §11 HTML 前端工具大塊 + 第四輪整合 patch + pre-LOCKED CC-01/07/08/09 校正）
優先級：最高

**v0.3 變更摘要（CODEX 審查後 master 第四輪 D-046 派工 patch）：**
- 全文 `/iterate-dialogue` → `/dialogue-write --single-iter`（對齊 D-028 / C-12 / O-02）
- 全文 `/export-dialogue` skill 引用改為 A1「複製 Export Prompt」按鈕 + 路徑（對齊 D-038 / L3_EXPORT_PROMPT_SCHEMA）
- §3 mode_tag 用語修正：mode_tag **鎖定 6 種不可擴充**（對齊 D-027 / O-05）
- §11.1 新增 §11.1.7 A-\* Asset Panel（對齊 D-045 / C-14 — A-\* 不納入 narrative `/status`，獨立 panel 顯示 7 subtype 完成度）
- §11.3 / §11.5 / §11.6 Export 相關段全面對齊 L3_EXPORT_PROMPT_SCHEMA §2 UI 規範（含「推送方式」欄位）
- §11.5.3 LOCKED → DEPRECATED 降級引導**刪除「降級理由 / 降級日期 / 降級人」三 frontmatter 欄位**（對齊 D-046 #5 / C-16 / O-03），改寫為「降級紀錄寫到 09_e final-gating 紀錄檔」
- §11.5 新增 §11.5.7 **Save race guard**：Save 前必重讀檔頭，最新 `狀態=LOCKED` 拒絕 overwrite + 三選項對話框（對齊 D-040 / C-15）
- §7.9 新增 **UX-54~80 對照表（25 筆，合併 UX-54/55 + UX-64/65 兩對重複）**（對齊 D-046 #1+#2 / C-06）
- §9 NS-1~NS-33 重新拆 **三類**：schema / query-API-adapter / upstream-algorithm（對齊 D-046 #6 / C-17）
- §6 QA 8 模板**全預設必跑**明示對齊（對齊 D-043 / C-11）
- §10 master 裁決清單對齊 D-040/043/045/046 + 已 RESOLVED 條目標註

**v0.2 → v0.3 不動：**
- §0/§1（除 §1.4 partial supersede 已決）/ §7.1~§7.8 substantive 段
- §11 主結構（§11.0~§11.9 子節）— 僅 §11.1.7 新增、§11.5 race guard 新增、§11.3/§11.5/§11.6 Export 相關段修

**依據文件：**
`REQUIREMENTS_LOCK.md` v1.0（4 bucket 需求快照）  
`DECISIONS_LOG.md` v0.8 §6.6 + §6.6.4a + §6.7（D-021~D-046）  
`UX_PROTOTYPE_ANALYSIS.md` v0.1（prototype 拆解 + §11 設計起點）  
`REVISED_WORK_ITEMS.md` v0.2 §7.5（UX-1~UX-17 17 條任務）  
`CODEX_REVIEW_REPORT.md` v0.1（CODEX 識出 C-06/C-12/C-15/C-16/C-17 + O-02/O-03/O-05 牽涉 UX）  
`L3_EXPORT_PROMPT_SCHEMA.md` v0.1（D-038 A1 流程 prompt contract）  
`UPSTREAM_DOWNSTREAM_SPEC.md` v0.2 §10/§11/§12/§13（UX-54~80 標記來源）

# UX_SPEC — UI/UX specialist 設計結論

# 0. 摘要

本專案沒有獨立 GUI。所有「使用者介面」都是 agent 對話中的 Markdown 呈現，或 `/export-*` 寫到 `view/` 的整合檔。本文件規範 8 個呈現情境的 Markdown layout 與閱讀體驗：

1. `/view-*` 四個 skill 的 chat 動態組合呈現
2. `/export-*` 寫 `view/<entity>.md` 的檔案 layout
3. `/status` 看板的視覺結構
4. 六個 REVIEW gate（A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5）的清單格式
5. `/qa` 五份報告 + 彙整版的閱讀體驗
6. 跨檔導航（breadcrumb / source 引用 / 相對連結基準路徑）
7. 錯誤提示通用結構（區分使用者錯誤與系統狀態未滿足）
8. （含）對其他 specialist 的回饋清單與需 master 裁決事項

**三條核心設計守則**（沿用 prior draft 的 G1 / G2 / G3，整套保留）：

- **G1：badge 不單獨呈現**——任何狀態 badge 必須搭配 checklist 或計數，避免單一狀態欄位收斂多重狀態信號。
- **G2：流程視覺化僅為閱讀順序，不是 state machine**——任何 `/status` 或 view 中的階段順序，旁邊明寫「閱讀順序用，不代表強制執行步驟」。
- **G3：UX grouping 不是資料層必要單位**——beat、章節分組等可用於排版，但格式不能假設「每場必有 beat」「每份角色必有弧線段」。

**全文呈現約束（硬規則）：**

- 純 Markdown，無 GUI 元件、無 `<details>` 展開、無內嵌 HTML（除非 GitHub flavored Markdown 廣泛支援且非互動）
- 中文主＋英文 sub 命名：標題與一級區塊用「中文 / English」格式（例「邏輯實體完成度 / Entity Completion」）；表格欄位、代碼塊內、頻繁重複的次級標籤可省 sub
- 跨檔 link 以 **project root 為基準**（`/01_world/01_a_世界觀總覽.md`），不用相對路徑
- 文件越長越靠前頭放「下一步」「重點摘要」「TOC」

---

# 1. UX_PRIOR_DRAFT 吸收結論

對 `_design/UX_PRIOR_DRAFT.md` 各條目的處置分類。本節是 prior draft 與本 spec 之間的權威對照表，後續 §2–§8 不再重複理由。

## 1.1 採用（A 級：直接平移到 Markdown）

| Prior draft 條目 | 平移到本 spec |
|---|---|
| 「下一步永遠在最前」 | §4 `/status` 第一個 section 是「下一步 / Next Actions」；§5 REVIEW gate 清單頂部也是「下一步 fix」 |
| badge + checklist 雙層（G1）— 不用單一狀態欄位收斂多重狀態 | §4 `/status` 看板的 readiness 用「主狀態 + 細項清單」；§5 gate 清單用「總體 badge + 逐檔 status」 |
| Next Fix 白話祈使句 | §5、§6、§8 各處的「下一步」段落一律用祈使句（例「審 3 條 DRAFT 後升 REVIEW」），不用模糊狀態詞 |
| 錯誤訊息四件套（What / Where / Why / How to fix） | §8 錯誤提示通用結構直接採用 |
| 區分使用者錯誤 vs 系統狀態未滿足 | §8 兩種錯誤分別有不同口氣與修復路徑 |
| 中文主 + 英文 sub 命名（Round 2.1） | §0 全文約束採用，但「次級重複標籤可省 sub」 |
| Workspace / Project / Scene 三層思考 | 本專案是 single-project repo，三層退化為「Project / Scene」兩層；§4 看板與 §7 導航沿用此分層 |
| Required Context 六分類 | §6 QA 彙整版與 §2.2 `/view-character` 採用此分類作為 context 段落骨架 |
| Severity 在最前（QA finding 標題用 `[HIGH]` / `[MEDIUM]` 前綴） | §6 QA finding 標題格式採用 |
| Affected 引用要精確到行（如 `Beat 1 / Line 2 / 角色：主角`） | §6 QA finding affected 欄位採用此粒度 |
| 「Suggested actions 純列舉，不是按鈕」 | §6 QA finding 與 §8 錯誤提示的「建議下一步」皆為純列舉 Markdown |
| Empty state 不只說「無 X」，要補「為什麼是正常 / 下一步可考慮」 | §8 空狀態文案規則採用 |
| Breadcrumb 引導列 | §7 導航在每份 export 檔頂部加 breadcrumb |
| 「← 回 X」相對連結（但相對基準改為 project root） | §7 採用，路徑改為以 `/` 開頭的 project-root 基準 |
| 單向 reference（不雙向維護） | §7 跨檔引用原則 |
| Production Loop 敘事骨架 | §4 看板把生產循環階段（原始資料 → Bible → Scene Task → Dialogue → QA → Human Decision → Canon Δ → Bible 回流）作為「模組狀態總覽」順序 |
| 三層核心守則 G1 / G2 / G3 | §0 全文守則 |

## 1.2 調整（B 級：核心可平移，需在 Markdown 環境調適）

| Prior draft 條目 | 調整方式 |
|---|---|
| Icon 系統（✓ ◐ ○ ⚠ ◑ —） | 改用純文字符號：`✓` / `~` / `✗` / `⚠` / `?` / `—`。理由：跨環境一致渲染、不依賴特殊字型 |
| Scene Readiness 10 項 checklist | 平移到 §5 REVIEW gate **通用骨架**（總體 badge + 逐項 checklist + Next Fix）；具體 10 項依本專案實際 6 個 gate 重新對應，**不照搬 prior draft 的 scene-level 10 項** |
| QA finding 5 欄位（severity / title / affected / summary / suggested actions） | §6 採用，但「Suggested actions」明確標為「閱讀建議」而非「可執行動作」（因為 prior draft 中為 button） |
| Project Dashboard 七段順序（身份頭 / HERO 下一步 / HERO 卡點 / 場景就緒度 / 模組狀態 / 三欄區 / 模組導航） | §4 `/status` 採用順序，但因本專案是 single-project repo，「跨專案 chip」省略；「模組導航」段在 Markdown 中改為「相關 view 連結清單」 |
| Status 文字保持人類可讀（不暴露 enum 鍵） | 採用，但本專案保留兩種使用情境：(a) `/status` 文字看板用人類可讀詞、(b) `/check-gaps` 與 frontmatter 引用維持 enum 鍵；§4 表格明列轉換對照 |

## 1.3 拒絕（C 級：明確拒絕並附理由）

| Prior draft 條目 | 拒絕理由 |
|---|---|
| `場景列隊 / Scene Queue` 命名 | 本專案沒有「卡片化的場景頁面」概念。場景索引 = `06_a 場景索引.md`，直接稱「場景索引」 |
| `單場控制台 / Scene Detail / Scene Production Cockpit` | 本專案沒有「單場 main + side cockpit」頁面。場景相關呈現分散到 `/view-detailed-outline`（看細綱中的章節節奏）與下游任務包檔本身 |
| `公版 Harness / 模板管理` | Template / Instance 兩 repo 架構在 SPEC 已定，使用者直接讀檔，無需「管理頁」 |
| `人類裁決收件匣` | 本專案沒有 inbox 模組。Human Decision 透過 `/status` 看板的「卡點」段落與 09_e 定稿變更紀錄處理 |
| 跨專案 summary chip（workspace 層） | 本專案是 single-project repo，無 cross-project 概念 |
| Glossary tooltip / `?` icon | 互動式元素，整體已廢棄（§1.4） |

## 1.4 已廢棄 / 適用範圍縮減（D 級：對應 prior draft §2 — HTML/CSS/JS 整層）

**v0.2 partial supersede（依 D-030 + 對齊 D-029 + 對齊 REQUIREMENTS_LOCK §5.1）：**

v0.1 原文「HTML 整層廢棄」一刀切的範圍被 **partial supersede**。新的適用範圍如下：

### 1.4.1 三層架構下的 form factor 分工

| Layer | Form factor | 規範章節 | GUI 元件 |
|---|---|---|---|
| **L1 Authoring（agent 對話 + Markdown source）** | **純 Markdown，無 GUI 元件** | §0 / §1 / §2 / §3 / §4 / §5 / §6 / §7 / §8 | 不得使用 button / form / modal / dropdown / hover / theme toggle / hash routing / localStorage 等任何 GUI 概念 |
| **L2 前端工具（HTML web UI）** | **HTML web UI（D-029 拍板）** | **§11**（v0.2 新增大塊） | 必要的 GUI 元件全許可；設計起點為既有 prototype Round 2.1（見 `UX_PROTOTYPE_ANALYSIS.md`） |
| **L3 Export（寫 `view/<entity>.md`）** | **純 Markdown，無 GUI 元件** | §3 / §7 | 同 L1 限制 |

### 1.4.2 v0.1「整層廢棄」適用範圍 — 縮減後

- **仍適用 L1 + L3：** prior draft §2 列舉的所有 GUI 元件、UI 系統、工程結構在 L1（`/view-*`、`/status`、`/qa` 等 agent 對話呈現）與 L3（`/export-*` 寫的 `view/` 整合檔）**整體仍廢棄**。Specialist agent 在 §2 / §3 / §4 / §5 / §6 / §7 / §8 設計中**不得**提及 button、form、modal、dropdown、hover、theme toggle、hash routing、localStorage 等任何 GUI 概念。如有違反，視為設計缺陷需重寫。
- **不再適用 L2：** L2 前端工具的 HTML web UI 設計由 §11 重新給出規範。§11 容許並要求使用 GUI 元件，**但仍受三守則 G1 / G2 / G3 + D-029 (α) 完全分離 + 中文主+英文 sub 命名 + 錯誤訊息四件套等橫切規範拘束**（這些守則跨 L1/L2/L3 一致）。

### 1.4.3 跨 L1/L2 一致的橫切規範（不被 partial supersede）

下列 §0 / §1 / §8 已定的規範**繼續適用 L2 §11**，§11 設計時不得違反：

- 三守則 **G1 / G2 / G3**（§0）
- **中文主 + 英文 sub** 命名約束（§0）
- 「**下一步永遠在最前**」（§1.1）
- 「**badge + checklist 雙層**」原則（§1.1 / §1.2）
- 「**Next Fix 白話祈使句**」（§1.1）
- **錯誤訊息四件套** What / Where / Why / How to fix（§8.1）
- 「**Suggested actions 純列舉，不是按鈕**」（§1.1）— **§11 例外明示：** L2 前端有「複製指令」按鈕屬「user 主動 trigger 切外部 chat」的合法互動，**不是**自動執行 agent action，仍符合 D-029 (α) 完全分離精神；通用元件規範見 §11.6。
- **單向 reference 原則**（§1.1 / §7.5）
- Empty state 文案規則（§8.3）

### 1.4.4 v0.1 §1.3 拒絕清單的處置

§1.3 表中曾以「整體已廢棄」為理由拒絕的下列項目，因 L2 form factor 回歸，部分回歸：

| §1.3 原拒絕項 | v0.2 處置 |
|---|---|
| `場景列隊 / Scene Queue` 命名 | **L1 仍拒絕**（場景索引仍是 `06_a 場景索引.md`）；**L2 採用** prototype Scene Queue 概念，見 §11.2 / §11.4 |
| `單場控制台 / Scene Detail / Scene Production Cockpit` | **L1 仍拒絕**；**L2 採用** Scene Detail (cockpit, read-only) 與 Scene Editor 雙頁（D-035），見 §11.2 / §11.3 / §11.5 |
| `公版 Harness / 模板管理` | **L1 仍拒絕**（Template/Instance 兩 repo 由 user 直讀檔）；**L2 採用** preview 形式（D-036），見 §11.9 |
| `人類裁決收件匣` | **全層拒絕**（沿用 v0.1 — 卡點透過 `/status` + 09_e 處理） |
| 跨專案 summary chip | **L1 仍拒絕**；**L2 採用** Workspace Home single-project 退化形式（D-036），見 §11.9 |
| Glossary tooltip | **L1 仍拒絕**（無 hover）；**L2 採用**（D-036），見 §11.9 |

→ §1.3 表中各項要看 L1 vs L2，**不是**「全部 v0.2 復活」，user 與 specialist 在後續對話引用時須加上 form factor 限定詞。

## 1.5 未討論（E 級：prior draft 沒碰，由本 spec 從零設計）

prior draft §3 列了 12 項，逐項本 spec 處置：

| 未討論項 | 本 spec 對應章節 |
|---|---|
| `/view-world` 完整 Markdown 結構 | §2.1 |
| `/view-character` 完整視角 | §2.2 |
| `/view-outline` 與 `/view-detailed-outline` 差異化 | §2.3 / §2.4 |
| `/export-*` 整合檔閱讀體驗 | §3 |
| 6 個正式 REVIEW gate | §5 |
| 5 份 QA 報告 + 彙整版 | §6 |
| skill 內錯誤提示文案模板 | §8 |
| 長文件 TOC / anchor / heading slug | §7.3 |
| 跨檔相對路徑根目錄假設 | §7.1（已決：project root） |
| 多 medium 輸出形式 | **本 spec 不展開**，列入 §10 master 裁決清單作為 future 議題 |
| 對話中「臨時呈現」 vs `/view-*` 正式呈現差異 | §2.5 |
| i18n 中英 sub 字級規則 | §0 統一規範（中文主＋英文 sub，無字級概念，純 Markdown 不控字級） |

---

# 2. /view-* 四個 skill 的 Markdown 模板

對應 §1.5 未討論清單之 §2.1-§2.5。**範圍：L1（agent 對話呈現），純 Markdown，無 GUI 元件（§1.4.2）。**

四個 skill 對齊 SPEC §14 既有清單：`/view-world` / `/view-character` / `/view-outline` / `/view-detailed-outline`。所有 skill 都動態組合多份 source 為一份**閱讀視圖**，**不寫檔**（寫檔是 `/export-*` §3 的職責）。

## 2.1 /view-world

**用途：** 把 `01_world/` 全部 source（01_a 世界觀總覽 / 01_b 世界語言 / 01_c 陣營與階級語言 等）動態組合為「世界觀完整視圖」。

**範本 layout：**

```markdown
# 世界觀 / World — 完整視圖

**下一步 / Next Actions**

*目前 W-rules 14/27 完成，仍缺戰鬥規則 / 異界規則。可考慮跑 /iterate-world 補完缺漏項。*

---

## 重點摘要 / Highlights

- 世界規則：14/27 項已建（核心 5 項齊全）
- 世界語言：8/15 項已建
- 陣營與階級語言：3/6 項已建
- 詞彙系統：禁用詞 12 項 / 慎用詞 8 項

---

## 世界規則 / World Rules

[從 /01_world/01_a_世界觀總覽.md 動態組合的內容]

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md)*

---

## 世界語言 / World Language

[從 /01_world/01_b_世界語言規格.md 動態組合的內容]

*來源：[/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md)*

---

## 陣營與階級語言 / Faction and Class Language

[從 /01_world/01_c_*.md 動態組合]

*來源：[/01_world/01_c_陣營與階級語言.md](/01_world/01_c_陣營與階級語言.md)*

---

## 詞彙系統 / Vocabulary

### 專有名詞 / Proper Nouns
[列表]

### 俗稱與黑話 / Slang
[列表]

### 禁用詞與慎用詞 / Forbidden and Cautious Words
[列表]

*來源：[/01_world/01_b_世界語言規格.md#詞彙系統-vocabulary](/01_world/01_b_世界語言規格.md#詞彙系統-vocabulary)*
```

**規則：**
- 「下一步」放第一個 section（§1.4.3）
- 「重點摘要」立刻接上（依 §0 「文件越長越靠前頭放下一步 / 重點摘要 / TOC」）
- 每個主 section 結尾加 `*來源：...*` italic 引用（§7.4）
- TOC **不**在 chat 動態組合內加（依 §7.3 — TOC 是 `/export-*` 整合檔的功能）
- chat 中 link 點不到，純文字仍提供定位線索

**G3 守則：** 規則 / 語言 / 陣營 / 詞彙四段是「閱讀骨架」，**不**假設 source 必填滿四項。空段套用 §8.3 empty state 文案。

## 2.2 /view-character

**用途：** 把單一角色的聲線卡 + 跨檔引用（出場場景 / 關係 / 立繪 KEY）動態組合。

**範本 layout：**

```markdown
# 角色 / Character — 主角A 完整視圖

**下一步 / Next Actions**

*聲線卡狀態 REVIEW；可考慮跑 /qa-character 主角A 確認聲線一致性。*

---

## 重點摘要 / Highlights

- 角色 ID：C-主角A
- 聲線卡狀態：REVIEW
- 出場場景：S-01-01 / S-01-02 / S-01-03 / S-02-01（4 場）
- 立繪 KEY：A-portrait-主角A-default / A-portrait-主角A-angry / A-portrait-主角A-surprise

---

## 聲線卡 / Voice Card

[從 /03_characters/main/主角A_聲線卡.md 動態組合]

*來源：[/03_characters/main/主角A_聲線卡.md](/03_characters/main/主角A_聲線卡.md)*

---

## 角色關係 / Relationships

- 主角A ↔ 反派B：對手 / 過去師生情誼

*來源：[/04_relationships/主角A_反派B.md](/04_relationships/主角A_反派B.md)*

---

## 立繪 KEY 清單 / Portrait Keys

| KEY | 狀態 / 表情 | 用途說明 |
|---|---|---|
| A-portrait-主角A-default | 平常 | 預設 |
| A-portrait-主角A-angry | 憤怒 | 對峙 / 質問 |
| A-portrait-主角A-surprise | 驚訝 | 揭穿時 |

*來源：[/01_world/A_assets/portrait_主角A.md](...)*

**注意：** 工具不存實檔，KEY 對應實檔由外部系統處理（依 D-023）。

---

## Required Context（出場場景反查）

依 prior draft 「Required Context 六分類」骨架：

### 1. Bible 引用
- 本角色相關 W-rules：[列出]
- 本角色相關 V-vocab：[列出]

### 2. 角色關係
[與其他角色關係列表]

### 3. 出場場景
- S-01-01：主角覺醒（DRAFT）
- S-01-02：相遇（REVIEW）
- S-01-03：質問（DRAFT）
- S-02-01：分歧（未啟動）

### 4. 跨場聲線注意
- S-01-02 已用過「我懂了」— 後續場避免重複

### 5. 資訊揭露時序
- S-01-01：揭露「異能存在」
- S-01-03 暗示「異能上限」
- S-02-01 揭露「主角異能等級」

### 6. 跨場警示
- 聲線漂移：聲線卡未鎖定，每場 dialogue 需檢查一致性
```

**規則：**
- Required Context 6 分類沿 §1.1 採用骨架
- 出場場景列表是動態反查 source frontmatter `entities` 的結果（單向 reference 例外，§7.5）
- A-\* 立繪 KEY 表格只展示 KEY + metadata（依 D-023）

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 「出場場景反查」的 query algorithm 由上下游 specialist 在 `/view-character` skill 實作時確認。

## 2.3 /view-outline

**用途：** 顯示**大綱**層次（不含每場細節）。組合 `05_outline/` 各章主線。

**範本 layout：**

```markdown
# 大綱 / Outline — 完整視圖

**下一步 / Next Actions**

*所有章節大綱已建立。可考慮跑 /create-detailed-outline 細化第二章。*

---

## 重點摘要 / Highlights

- 共 3 章 / 26 場
- 第一章：8 場（已細化）
- 第二章：10 場（待細化）
- 第三章：8 場（待細化）

---

## 第一章：覺醒 / Chapter 1: Awakening

**主軸：** 主角A 在神殿廢墟覺醒異能，與反派B 初次對峙。

**節奏：** 緩開場 → 高潮對峙 → 留懸念

**主線情節 (P-arc)：**
- 揭露「異能存在」
- 主角A 接收「靈魂之路」首次召喚

**場景數：** 8 場（S-01-01 ~ S-01-08）

*來源：[/05_outline/CH01_第一章.md](/05_outline/CH01_第一章.md)*

[→ 詳見細綱](/06_detailed_outline/CH01_第一章細綱.md)

---

## 第二章：尋路 / Chapter 2: Searching

[類似格式]

*來源：[/05_outline/CH02_第二章.md](/05_outline/CH02_第二章.md)*

---

## 第三章：抉擇 / Chapter 3: Choice

[類似格式]
```

**規則：**
- 每章一個 section，含「主軸 / 節奏 / 主線情節 / 場景數」四項
- 結尾「[→ 詳見細綱]」連到對應 `/06_detailed_outline/CH<n>_*.md`
- **不**列每場細節（屬 `/view-detailed-outline` §2.4 職責）

## 2.4 /view-detailed-outline

**用途：** 顯示某章節的**細綱**（每場 beat 結構 + 出場角色 + 揭露資訊）。

**範本 layout：**

```markdown
# 第一章細綱 / Chapter 1 Detailed Outline — 完整視圖

**下一步 / Next Actions**

*S-01-03 任務包 REVIEW；可跑 /dialogue-write S-01-03 啟動試寫。*

---

## 重點摘要 / Highlights

- 章節：第一章 — 覺醒
- 場景數：8 場
- 完成度：5/8 場 ≥ DRAFT
- 卡點：S-01-04 任務包 frontmatter「真實目標」未填

---

## 場景 S-01-01：主角覺醒 / Awakening

**Pipeline State：** DRAFT
**Mode Tag：** TRIAL（試寫 3 版）

**出場角色：** 主角A

**Beat 結構（建議分 3 拍）：**
- Beat 1：環境鋪陳（神殿廢墟）
- Beat 2：覺醒瞬間（異能首次顯現）
- Beat 3：定位反應（主角A 自問自答）

**揭露資訊：** 「異能存在」首次出現

**跨場連結：**
- 後續 S-01-02：主角A 第一次外出尋路
- 後續 S-01-03：與反派B 對峙引用本場「靈魂之路」概念

*來源：[/06_detailed_outline/CH01_第一章細綱.md#s-01-01](/06_detailed_outline/CH01_第一章細綱.md#s-01-01)*

[→ 跳場景任務包](/07_scene_tasks/CH01_S01_台詞任務包.md)

---

## 場景 S-01-02：相遇 / Encounter

[類似格式]

---

[共 8 場]
```

**規則：**
- 每場一個 section，含「Pipeline State / Mode Tag / 出場角色 / Beat 結構 / 揭露資訊 / 跨場連結」六項
- Beat 結構標註「建議分 X 拍」 — G3 守則對齊（不假設每場必有 N beat）
- 「跨場連結」段顯示前後 scene 的關係（依 §7.5 單向 reference — 只列下游引用，不列上游被引用）

**與 §2.3 /view-outline 的差異：**
- §2.3 章節層 — 一章一段，無場景細節
- §2.4 場景層 — 一場一段，含 beat / context

## 2.5 對話中「臨時呈現」 vs `/view-*` 正式呈現差異

對應 §1.5 未討論清單末項。

**「臨時呈現」定義：** user 在 agent 對話中問「世界觀目前進度？」或「主角A 出場幾場？」時，agent 不需跑完整 `/view-world` / `/view-character`，直接從記憶中組答案。

**規範：**

| 維度 | 臨時呈現 | 正式 /view-\* |
|---|---|---|
| 觸發 | user 隨口問 | user 明確跑 skill |
| 範圍 | 答問題所需的最小範圍 | 完整視圖 |
| 格式 | 自由 prose / 簡短列表 | 本節 §2.1-§2.4 規範格式 |
| 來源引用 | 可省（agent 從 context 已知） | 必加 `*來源：...*` |
| 是否顯示「下一步」 | 不需要 | 必有 |
| 結束語 | 可加「需要完整視圖跑 /view-\*」hint | 不需 hint |

**典型臨時呈現範例：**

```markdown
主角A 目前出場 4 場：S-01-01 / S-01-02 / S-01-03 / S-02-01。
聲線卡狀態 REVIEW。

如果要完整視圖含關係 / 立繪 KEY / Required Context，可跑 /view-character 主角A。
```

**規則：**
- 臨時呈現**不**走 §2.1-§2.4 範本骨架
- 結尾**建議**加一行「可跑 /view-\* 取完整視圖」hint，讓 user 知道有正式 skill 可用
- 不假設 user 一定要跑 `/view-\*` — 臨時答案有用就夠

---

---

# 3. /export-* 檔案 layout 與 /view-* 差異

對應 §1.5 未討論清單之 §3。**範圍：L3（寫 `view/<entity>.md` 整合檔），純 Markdown，無 GUI 元件（§1.4.2）。**

`/export-*` 跟 `/view-*` 同樣動態組合多份 source，但**寫到檔案**而非顯示在 chat。寫到 `/view/<entity>.md` 後可在編輯器 / GitHub 預覽。

## 3.1 整合檔的閱讀體驗 vs chat /view-* 的差異

| 維度 | chat `/view-*` | 整合檔 `/export-*` |
|---|---|---|
| 渲染環境 | agent chat | 編輯器 / GitHub markdown preview |
| 跨檔 link | 點不到但給定位線索 | 點得到，跳對應 source 檔（§7.1） |
| Frontmatter | 無 | **有**（§3.2） |
| Breadcrumb | 無 | **有**（§7.2） |
| TOC | 無 | 長文件（> 200 行）有（§7.3） |
| Source 引用 | italic 行 | italic 行（§7.4） |
| 末尾「← 回 X」 | 無 | **有**（§7.2） |
| 「下一步」 | 必有 | 可選（看 export 目的） |

整合檔比 chat 多了**結構導航**（frontmatter / breadcrumb / TOC / 「← 回 X」），因為閱讀環境是「靜態檔，user 隨時開啟」。

## 3.2 整合檔 Frontmatter

每份 `/view/<entity>.md` 必含 frontmatter：

```yaml
---
title: 世界觀 / World — 完整視圖
generated_by: /export-world
generated_at: 2026-05-18T13:42:00Z
source_files:
  - /01_world/01_a_世界觀總覽.md
  - /01_world/01_b_世界語言規格.md
  - /01_world/01_c_陣營與階級語言.md
view_type: world
freshness: ok    # 或 stale（依 §7.7 偵測 source mtime > generated_at）
---
```

**規則：**
- `generated_by` 紀錄哪個 skill 生成（可追溯）
- `generated_at` ISO 8601 timestamp
- `source_files` 列出全部 source（供 `/check-gaps` 反查 stale，§7.7）
- `view_type` 跟 SPEC §5.4 entity 對齊（world / character / outline / detailed-outline）
- `freshness` 由生成時 set ok；後續 `/check-gaps` 偵測 stale 時可更新

**[NEEDS_SCHEMA_SUPPORT]** — `freshness` 欄位是否動態維護（每次 source 改自動 sync 此欄位）— 收 §9。

## 3.3 整合檔 layout 範本

```markdown
---
[§3.2 frontmatter]
---

> 專案首頁 / 世界觀 / 完整視圖

## 目錄 / Contents（> 200 行才出現）

- [世界規則 / World Rules](#世界規則-world-rules)
- [世界語言 / World Language](#世界語言-world-language)
- ...

---

# 世界觀 / World — 完整視圖

[§2.1 /view-world 的完整內容，含 source 引用]

---

[← 回 `/view-*` 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

**規則：**
- frontmatter → breadcrumb → TOC（如有）→ 主標題 → 主內容 → 末尾「← 回」
- 主內容**完全沿用 §2.1-§2.4 範本**，差別只在外殼（frontmatter / 導航）

## 3.4 不同 `/export-*` 的對應檔名

| Skill | 輸出檔 |
|---|---|
| `/export-world` | `/view/世界觀.md` |
| `/export-character <角色>` | `/view/角色_<角色>.md` |
| `/export-outline` | `/view/大綱.md` |
| `/export-detailed-outline [<CH-ID>]` | `/view/細綱.md` |
| `/export-dialogue <場景>` ⚠ **v0.3 移除** | ~~`/view/場景_<S-XX-XX>.md`~~ — 改走 D-038 A1 「複製 Export Prompt」按鈕，見 §11.6.5 / §11.6.6 |

**檔名規則：**
- 中文 entity 名直接用（純 Markdown 環境支援 unicode 檔名）
- 不加日期 / 版本後綴（versioned 由 git history 處理）
- 「下一步」「卡點」這類 status 看板**不**走 `/export-*`，走 `/status`（§4）

## 3.5 整合檔 stale 偵測

依 §7.7 規則 — source mtime > view 匯出時間 → 標 stale。

**stale 在整合檔本身的呈現：**

```markdown
---
[frontmatter]
freshness: stale
---

> 專案首頁 / 世界觀 / 完整視圖

> ⚠ **此整合檔已 stale** — source 於 2026-05-18 修改，本檔最後匯出 2026-05-15。
> 重跑 `/export-world` 更新。

[正常內容...]
```

**規則：**
- frontmatter `freshness: stale`
- breadcrumb 之下、TOC 之上加一條 stale warning（GitHub flavored quote block）
- warning 不阻擋 user 讀內容 — 只提醒「資料可能過時」

**「下一步」段（如有）：**
```markdown
**下一步 / Next Actions**

*本整合檔 stale，可考慮跑 /export-world 更新。*
```

## 3.6 `/view/README.md` — 系列總覽

`/view/README.md` 是 user 累積 ≥ 1 份 `/export-*` 後**手動**建立的索引檔（不自動生成；§7.2）。

**建議內容：**

```markdown
---
title: View 系列總覽
---

# `/view/` 系列總覽 / Generated Views Index

本目錄存放 `/export-*` 生成的整合檔。各檔自動 sync source；如顯示 stale 請重跑對應 export。

## 世界觀 / World
- [世界觀完整視圖](/view/世界觀.md) — 由 `/export-world` 生成

## 角色 / Characters
- [角色_主角A](/view/角色_主角A.md)
- [角色_反派B](/view/角色_反派B.md)

## 大綱 / Outline
- [大綱完整視圖](/view/大綱.md) — 由 `/export-outline` 生成

## 細綱 / Detailed Outline
- [細綱完整視圖](/view/細綱.md)

## 場景 / Scenes
- [場景_S-01-01](/view/場景_S-01-01.md)
- [場景_S-01-03](/view/場景_S-01-03.md)
```

**規則：**
- user 手動維護（不自動生成）
- 建議分組（世界觀 / 角色 / 大綱 / 細綱 / 場景）
- 每條附「由 `/export-*` 生成」hint

**[NEEDS_SCHEMA_SUPPORT]** — `/view/README.md` 自動生成的時機判定（user 累積 ≥ 1 份時提示）— 收 §10 作為 future master 裁決議題。

---

---

# 4. /status 看板格式

對應 §1.5 未討論清單之 §4 + §1.2 「Project Dashboard 七段順序」B 級調整。**範圍：L1（agent 對話呈現），純 Markdown，無 GUI 元件。**

`/status` skill 是 user 在 agent chat 跑「看目前狀態」的入口。產出**一份 Markdown 報告**直接顯示在 chat。相當於 §11.1 Project Dashboard 的純 Markdown 版本（兩者資料同源，差別只在 form factor — L1 vs L2）。

## 4.1 看板整體 7 段順序（依 §1.2）

```
1. 身份頭（專案簡名 + 時間戳）
2. HERO：下一步 / Next Actions
3. HERO：卡點 / Blockers
4. 場景就緒度 / Scene Readiness Overview
5. 模組狀態總覽 / Module Status
6. 三欄區 / Tri-column Snapshot（待裁決 / QA pending / Canon Δ pending）
7. 相關 view 連結清單（§1.2 「模組導航」B 級調整）
```

**partial supersede §1.2 prior draft「模組導航」：** prior draft 是 GUI 元件，本 spec 純 Markdown 改為「相關 view 連結清單」純文字。

**single-project repo 場景：** 跨專案 chip 省略（§1.2）。

## 4.2 範本

````markdown
# /status — 劇本開發工具 / 2026-05-18 13:42

---

## 下一步 / Next Actions

1. **跑 `/dialogue-write S-01-03`** — 任務包已升 REVIEW，啟動試寫。
2. **跑 `/iterate-world` 補 W-rules** — 仍缺戰鬥規則 / 異界規則 共 13 項。
3. **審 3 條 DRAFT 任務包** — `/07_scene_tasks/CH01_S04` / `S-01-05` / `S-01-07`。

---

## 卡點 / Blockers

### ⚠ Blocker 1：場景 S-01-04 無法跑 `/dialogue-write`

- **What**：任務包核心欄位「真實目標」為 TODO
- **Where**：`/07_scene_tasks/CH01_S04_台詞任務包.md`
- **Why**：核心欄位 TODO 依 D.3 規則拒絕執行
- **下一步**：補齊「真實目標」欄位後重跑 `/dialogue-write S-01-04`

### ⚠ Blocker 2：角色 C-反派B 聲線卡尚未升 REVIEW

- **What**：聲線卡狀態為 DRAFT
- **Where**：`/03_characters/main/反派B_聲線卡.md` frontmatter
- **Why**：依 00_k 階段 1 啟動條件需所有出場角色 ≥ REVIEW
- **下一步**：審完聲線卡後升 REVIEW，或跑 `/iterate-character 反派B`

---

## 場景就緒度 / Scene Readiness Overview

整體 58%（15/26 場）

| pipeline_state | 場數 | 占比 |
|---|---|---|
| DRAFT | 8 | 31% |
| REVIEW | 6 | 23% |
| LOCKED | 1 | 4% |
| DEPRECATED | 0 | 0% |
| （未啟動） | 11 | 42% |

*順序為閱讀順序，不代表強制執行步驟（G2）*

---

## 模組狀態總覽 / Module Status

| 階段 / Stage | 模組 | 狀態 | 細項 | 下一步 |
|---|---|---|---|---|
| A 對話建立 | W / V / C / R / P / CH / S | ~ Authoring | W 14/27 / V 8/15 | 跑 `/iterate-world` |
| B 拆解任務 | `/07_scene_tasks/*` | ~ Authoring | 11 任務包 DRAFT、5 REVIEW | 審 3 條 DRAFT |
| C 試寫 | `/08_dialogue_outputs/CH*_S*/v01*` | ~ Drafting | 6 場 trial 完成 | 跑 `/dialogue-write S-01-03` |
| D 收斂 | `/08_dialogue_outputs/CH*_S*/v02` | ✗ Pending | 0 場 v02 | 等試寫完成 |
| E QA | `/09_qa_reports/*` | ~ Pending | 8/9 模板可用 | 跑 `/qa S-01-01` |
| F 人類裁決 | `/09_e_定稿變更紀錄.md` | ✓ Idle | 0 待裁決 | — |
| G Canon Δ | `/09_d_*.md` | ✓ Idle | 0 待回流 | — |
| H Export | `/view/*` | ~ Stale | 3 份 view stale | 跑 `/export-world` |

*階段順序為閱讀順序，不代表強制執行步驟（G2）*

---

## 三欄區 / Tri-column Snapshot

### 待人類裁決 / Pending Human Decisions

- 場景 S-01-03：破格保留 vs 不採（QA 09_f 命中）
- 角色重命名：NPC-村民甲 與 NPC-村民乙 命名衝突

詳見 `/09_qa_reports/09_e_定稿變更紀錄.md`

### QA Pending

- `09_a` AI 味檢查：3 場待跑（S-01-01 / S-01-02 / S-01-05）
- `09_g` 節奏感：全章節待跑（Bucket #2 新增模板）

跑 `/qa S-XX-XX` 對應場景

### Canon Δ Pending

*目前無待回流 Canon Δ — 上次回流 2026-05-15*

---

## 相關 view 連結清單 / Related Views

- [世界觀完整視圖](/view/世界觀.md) ✓ ok
- [角色_主角A](/view/角色_主角A.md) ⚠ stale（source 已改）
- [大綱完整視圖](/view/大綱.md) ✓ ok
- [細綱完整視圖](/view/細綱.md) ✓ ok

跑 `/export-character 主角A` 更新 stale view。

---

*狀態：截至 2026-05-18 13:42。重跑 `/status` 取最新。*

````

## 4.3 各 section 規則

### 4.3.1 身份頭 + 時間戳

```markdown
# /status — 劇本開發工具 / 2026-05-18 13:42
```

- 第一行 `#` 標題
- 專案簡名（讀 root README.md 或 SPEC.md 取）
- 時間戳精準到分鐘
- single-project repo — 不顯示 workspace 跨專案資訊

### 4.3.2 下一步段（HERO）

- 用**有序 list**（1. 2. 3. ...）強調優先級
- 每條祈使句 + bold key action（如 `**跑 /dialogue-write S-01-03**`）+ 一句說明
- 最多 5 條（依 §11.1.1 同樣原則）；超過 5 條優先級降階入「模組狀態」段
- **不**顯示 `[複製指令]` 按鈕（L1 純 Markdown，無 GUI 元件）— user 自己 copy paste

### 4.3.3 卡點段（HERO）

- 用 `### ⚠ Blocker N` 標題
- 內含**錯誤訊息四件套**（What / Where / Why / 下一步）依 §8.1
- 空狀態（§8.3）：

```markdown
*目前無卡點 — 所有實體已通過先決條件檢查。可考慮跑 `/scene-task` 啟動下一場 dialogue 生產。*
```

### 4.3.4 場景就緒度段

- 整體 % + 細分表格
- **G1 守則：** 整體 % 不獨立呈現，必搭配 pipeline_state 細分
- **G2 守則：** 表格下方明示 `*順序為閱讀順序，不代表強制執行步驟*`

### 4.3.5 模組狀態總覽段

- 表格 8 行對應 Production Loop 8 階段
- 「狀態」列用純文字符號 + 階段語意（如 `~ Authoring` 不只 `~`）
- 「下一步」列祈使句（不寫「應該」「可能」）
- **G2 守則：** 表格下方明示順序為閱讀順序

### 4.3.6 三欄區段

- 用 `###` 三個 subsection
- 每段內容用 bullet list；空狀態用 italic + 灰調 hint
- 不用 GUI 元件（無 column layout — 純 markdown subsection 縱向）

### 4.3.7 相關 view 連結清單段

- bullet list 每條 `[/view/X.md](/view/X.md) ✓ ok` 或 `⚠ stale`
- stale 條目在末尾加 hint「跑 `/export-X` 更新 stale view」

### 4.3.8 結尾

```markdown
*狀態：截至 2026-05-18 13:42。重跑 `/status` 取最新。*
```

italic 灰調，避免 user 把時間戳誤以為自動更新。

## 4.4 三層守則對齊

| 守則 | §4 對應 |
|---|---|
| G1 badge 不單獨呈現 | 整體 58% 進度條 + pipeline_state 細分 + Next Fix；不單獨顯示 % |
| G2 流程視覺化僅閱讀順序 | 「順序為閱讀順序」標語在 §4.3.4 / §4.3.5 |
| G3 UX grouping 不是資料層必要單位 | 「Production Loop 8 階段」是看板分組，不代表每場必走 8 階段 |
| 下一步永遠在最前 | §4.3.2 「下一步」段是身份頭後第一段 |
| 中文主+英文 sub | 所有主標題雙語 |
| 純 Markdown | 無 button / modal / GUI |

## 4.5 跟 §11.1 Project Dashboard 的職責分工（複述）

| 維度 | §4 /status (L1) | §11.1 Dashboard (L2) |
|---|---|---|
| 表現 form | agent chat 中 Markdown 報告 | 瀏覽器中 HTML web UI |
| 觸發 | user 跑 `/status` skill | user 開 localhost 瀏覽器 |
| GUI 元件 | ✗ 純 Markdown | ✓ button / facet / 卡片 |
| 「複製指令」 | user 自己 copy 文字 | 按鈕一鍵複製（§11.6） |
| Stale 警示 | 在 view 連結後標 `⚠ stale` 文字 | 在 §11.1.7 模組導航區用 ⚠ icon + colored badge |
| 跳轉 | 文字 link 點不到 | link 點得到，§11.7 多分頁 |
| 即時 | user 重跑 skill 取新版 | 點 refresh 即時更新 |

兩者**內容同源**（同一份 source markdown），呈現方式不同。

---

---

# 5. 六個 REVIEW gate 清單格式

對應 §1.5 未討論清單之 §5 + §1.2 「Scene Readiness 10 項 checklist」B 級調整（具體 10 項依本專案實際 6 個 gate 重新對應）。**範圍：L1（agent 對話呈現），純 Markdown。**

本專案 6 個 REVIEW gate：**A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5**。

## 5.1 通用骨架

每個 gate 清單格式統一：

```markdown
# REVIEW Gate — A.10 / 階段 A 完成判定

---

## 下一步 / Next Fix

**升 REVIEW：** 跑 `/check-gaps` 確認以下 5 項全綠後，將 frontmatter `狀態` 從 `DRAFT` 改為 `REVIEW`。

---

## 總體 Badge

**目前：** ⚠ 3/5 項就緒

---

## 逐項 Checklist

| # | 檢查項 | 狀態 | 下一步 |
|---|---|---|---|
| 1 | 27 項 W-rules 全數建立或標 N/A | ⚠ 14/27 | 補 13 項或標 N/A |
| 2 | 15 項 V-vocab 全數建立或標 N/A | ✓ 15/15 | — |
| 3 | C-\* 主要角色（主角 + 反派）≥ 2 個 | ✓ 2/2 | — |
| 4 | A-\* 立繪 KEY 對主要角色 ≥ 1 個 / 角色 | ⚠ 1/2 主角缺 | 補主角A 立繪 KEY |
| 5 | 00_b 作品專屬 LOCK 已設 | ✗ 未設 | 跑 `/iterate-instance` 設 LOCK |

---

## 進入條件 / Prerequisites

- W / V / C / R / P 五個 Bible 子項齊全
- A-\* 美術資產 entity 開始建立（D-023）

## 失敗條件 / Failure Modes

- 任一 ✗ 或 ⚠ 項未補齊 → 不可升 REVIEW
- 升 REVIEW 後若觸發回流（D-018 #1 不採 — 無 retcon），則 source 改動需重審本 gate

---

*來源：SPEC §16 文件狀態機 + 00_k 台詞生產流程協議*
```

**骨架規則：**
- 「下一步 / Next Fix」放最前（§1.4.3）
- 「總體 Badge」用「⚠ 3/5 項就緒」格式 — badge 必搭配計數（G1）
- 「逐項 Checklist」用表格 — 每行：項次 / 檢查項 / 狀態符號 / 下一步祈使句
- 狀態符號：`✓` / `~` / `✗` / `⚠` / `?` / `—`（§1.2 B 級調整）
- 結尾標 source 引用

## 5.2 6 個 gate 各自簡述

每個 gate 套用 §5.1 骨架，內容依 SPEC §16 + 各 phase 協議檔。

### 5.2.1 A.10 — Bible 階段完成判定

**目的：** 確認 W/V/C/R/P/CH/S 七種 Bible entity 齊全，可進 B 拆解任務階段。

**主要檢查項：**
- W-rules / V-vocab 建立狀態
- C-\* 主要角色 + A-\* 立繪 KEY 對齊（D-023）
- R-relationship 關係建立
- P-plot 主線情節骨架
- 00_b 作品專屬 LOCK 設置

### 5.2.2 B.5.5 — 大綱完成判定

**目的：** 確認 `/05_outline/` 章節大綱完整，可進細綱。

**主要檢查項：**
- 全章節大綱建立
- 主線情節 P-arc 對齊
- 跨章節節奏 (G2) 標註
- 場景數估計與場景索引 06_a 對齊

### 5.2.3 B.6.5 — 細綱完成判定

**目的：** 確認 `/06_detailed_outline/` 各章節細綱完整，可進任務包拆解。

**主要檢查項：**
- 每章節場景數細化
- 每場 beat 結構建議
- 揭露資訊時序
- 跨場連結

### 5.2.4 B.8 — 任務包完成判定

**目的：** 確認 `/07_scene_tasks/` 場景任務包完整，可進試寫。

**主要檢查項：**
- 任務包核心欄位齊全（依 D.3 規則）
- 出場角色聲線卡引用
- 出場立繪 KEY 標註（D-023）
- 角色真實目標欄位
- 場景偏移 / Beat 結構建議

### 5.2.5 D.2.5 — 試寫完成判定

**目的：** 確認 `/08_dialogue_outputs/CH*_S*/v01A,B,C/` 試寫齊全，可進收斂。

**主要檢查項：**
- v01A / v01B / v01C 三版**或** SINGLE_ITER 單版完成（依 D-028 mode）
- 每版 i18n KEY 唯一性（D-022）
- 立繪 KEY 對齊（D-023）
- 待 QA 標記齊全

**SINGLE_ITER 例外：** 走 SINGLE_ITER 模式時，只需單版完成即可進 D.3.5；本 gate 對 SINGLE_ITER 場景的 3 版檢查降為 1 版檢查。

### 5.2.6 D.3.5 — 收斂完成判定

**目的：** 確認 v02 收斂版完成（或 SINGLE_ITER 最終版），可進 QA。

**主要檢查項：**
- v02 完成且引用清楚（source_dialogues 紀錄 v01A/B/C — Z1 並排對齊）
- 收斂理由紀錄
- 跨版本 KEY 一致性
- 破格保留判定（如有 EXPERIMENTAL）

## 5.3 多個 gate 同顯示時的彙整

當 user 跑 `/status` 或 `/check-gaps`，可能同時看多個 gate 狀態。彙整呈現：

```markdown
## 6 個 REVIEW Gate 狀態總覽

| Gate | 對應階段 | 狀態 | 下一步 |
|---|---|---|---|
| A.10 | Bible 完成 | ⚠ 3/5 項 | 補 W-rules + 設 00_b LOCK |
| B.5.5 | 大綱完成 | ✓ 全綠 | — |
| B.6.5 | 細綱完成 | ~ 2/3 章 | 細化第三章 |
| B.8 | 任務包完成 | ~ 11/26 場 | 補 15 場任務包 |
| D.2.5 | 試寫完成 | ✗ 0 場 | 等 B.8 升 REVIEW |
| D.3.5 | 收斂完成 | ✗ 0 場 | 等 D.2.5 升 REVIEW |

跑 `/check-gaps --gate <gate-id>` 看單一 gate 詳細 checklist。
```

## 5.4 gate fail 後的呈現

如果跑 `/check-gaps --gate A.10` 偵測到失敗：

```markdown
# REVIEW Gate — A.10 / 階段 A 完成判定 — ✗ 失敗

## 下一步 / Next Fix

**修補後重跑 `/check-gaps --gate A.10` 確認。**

依以下 fail 項優先處理：
1. 補 W-rules 戰鬥規則 6 項
2. 補 W-rules 異界規則 5 項
3. 補主角A 立繪 KEY 至少 1 個

## 失敗項清單

### ✗ Item 1：W-rules 缺漏 13 項
- **Where**：`/01_world/01_a_世界觀總覽.md`
- **Why**：A.10 要求 27 項全建或標 N/A，目前只有 14 項
- **下一步**：跑 `/iterate-world --section 戰鬥規則` + `/iterate-world --section 異界規則`

### ✗ Item 2：00_b 作品專屬 LOCK 未設
- **Where**：`/00_protocols/00_b_作品專屬.md` frontmatter
- **Why**：A.10 要求 Instance 微調已 LOCK 才可升 REVIEW
- **下一步**：跑 `/iterate-instance` 完成 00_b 並設 LOCK

[與 §5.1 通用骨架其餘段落...]
```

**規則：**
- 標題加「— ✗ 失敗」後綴
- Next Fix 段明示「修補後重跑 `/check-gaps --gate <id>` 確認」
- 失敗項用 `### ✗ Item N` 標題 + 四件套（What 在標題、Where / Why / 下一步 在 bullet）

## 5.5 三層守則對齊

| 守則 | §5 對應 |
|---|---|
| G1 badge 不單獨呈現 | 總體 badge `⚠ 3/5 項就緒` — 包含計數 + 細項 checklist + Next Fix 三層 |
| G2 流程視覺化僅閱讀順序 | 6 個 gate 順序（A.10 → B.5.5 → B.6.5 → B.8 → D.2.5 → D.3.5）是「設計流程順序」，本節 §5.3 彙整表下方加 hint「順序為閱讀用，不代表強制執行步驟」 |
| G3 UX grouping 不是資料層必要單位 | 「逐項 Checklist」格式是排版單位，gate 內項目可不齊（如不適用 N/A） |

---

---

# 6. QA 八份報告閱讀體驗 + 彙整版

對應 §1.5 未討論清單之 §6 + Bucket #2 拍板 D-026（09_g/h/i 新增 — partial supersede 「五份報告」舊範圍）。

**範圍：L1（agent 對話呈現），純 Markdown。**

依 REQUIREMENTS_LOCK §4.1，本輪 QA 模板數量：
- **8 份 QA 模板**：09_a / 09_b / 09_c / 09_d / 09_f / 09_g / 09_h / 09_i
- **1 份 final-gating**：09_e（不在 QA pipeline，是定稿變更紀錄）
- **總計：9 份**

注意：v0.1 §1.5「5 份 QA 報告」是舊規範；v0.2 partial supersede 升為 8 份（依 D-026）。

## 6.1 QA Finding 5 欄位格式

**沿用 §1.2 prior draft 5 欄位（severity / title / affected / summary / suggested actions）+ 調整：**「suggested actions」明確標為「閱讀建議」而非「可執行動作」（L1 純 Markdown 無按鈕）。

```markdown
### [HIGH] 對話張力不足 / Dramatic Tension Low

**Affected：**
- Beat 2 / Line 4 / 角色：主角A
- i18n KEY：`dlg.ch01.s03.l004`

**Summary：**
反擊頻率 0/3，預期 ≥ 1。本場兩方核心衝突，主角A 在被反派B 反問後沒任何反擊台詞，缺攻防力度。

**閱讀建議 / Suggested Reading（非可執行動作）：**

1. 在 Line 4 後補一條主角A 反擊台詞
2. 把 Line 4 從疑問句改為陳述句以反擊
3. 整段重寫 Beat 2 用「揭穿 / 反擊」結構

**處理方式：** 跑 `/dialogue-write S-01-03 --single-iter --note "補主角A反擊"` 後重審本 finding。

---
```

**規則：**
- 標題：`### [SEVERITY] 中文 / English` — severity 在最前（§1.2）
- Severity 三級：`[HIGH]` / `[MEDIUM]` / `[LOW]`
- Affected：精確到 Beat / Line / 角色 + i18n KEY（§1.2 + D-022 對齊）
- Summary：問題說明 + 量化指標（如「反擊頻率 0/3」）
- 閱讀建議：**純列舉**（§1.4.3 — L1 無按鈕）
- 處理方式：祈使句指向對應 skill 或下游動作

## 6.2 各 QA 模板閱讀體驗

### 6.2.1 09_a — AI 味檢查（qa_type: `AI_FLAVOR`）

```markdown
# QA Report — 09_a AI 味 / S-01-03

---

## 下一步 / Next Fix

**跑 `/dialogue-write S-01-03 --single-iter --note "修 3 條 HIGH"` 修補後重跑 09_a。**

---

## 總體 / Overall

- 場景：S-01-03
- 跑時版本：v01A
- Severity 分布：HIGH 3 / MEDIUM 5 / LOW 2
- 整體判定：⚠ 未通過（HIGH > 0）

---

## 詳細 Findings

### [HIGH] 重複句首「老實說」 / Repeated phrase opener
[5 欄格式]

### [HIGH] 過度禮貌結尾「希望這對你有幫助」 / Over-polite closure
[5 欄格式]

### [MEDIUM] 過度使用「事實上」 / Overuse of "actually"
[5 欄格式]

---

*來源：[/09_qa_reports/09_a_AI味檢查.md](/09_qa_reports/09_a_AI味檢查.md)*
*來源：跑 `/qa S-01-03 --templates 09_a`*
```

**重點：** AI 味檢查偏「字面用詞」分析；finding affected 多在「行內」。

### 6.2.2 09_b — 聲線一致性（`VOICE_CONSISTENCY`）

```markdown
# QA Report — 09_b 聲線一致性 / S-01-03

[同上骨架]

## 重點摘要

- 跑時對比：v01A vs 聲線卡 `主角A_聲線卡.md`
- 漂移度：0.18（< 0.30 算通過）
- 整體判定：✓ 通過

## 詳細 Findings

### [LOW] 主角A 句長平均偏短 / Avg sentence shortened
- **Affected**：全場 24 行
- **Summary**：聲線卡規範平均 18 字 / 句，本場 14.2 字
- **閱讀建議**：適度增加複雜句以匹配聲線
```

**重點：** 聲線一致性偏「對比聲線卡」；不限定行，可全場 affected。

### 6.2.3 09_c — 禁用詞（`FORBIDDEN_TERMS`）

```markdown
# QA Report — 09_c 禁用詞 / S-01-03

[骨架]

## 重點摘要

- 比對禁用詞表：12 項
- 命中：1 項
- 整體判定：⚠ 未通過（命中 > 0）

## 詳細 Findings

### [HIGH] 「魔法」是禁用詞 / Forbidden term used
- **Affected**：Beat 1 / Line 2 / 角色：反派B
- **i18n KEY**：`dlg.ch01.s03.l002`
- **Summary**：本世界用「異能」取代「魔法」（W-rules §2.1）
- **閱讀建議**：把「魔法」改為「異能」
- **處理方式**：跑 `/dialogue-write S-01-03 --single-iter --note "把魔法改異能"`（D-028 SINGLE_ITER；不新增 `/iterate-dialogue` skill）
```

**重點：** 禁用詞是 binary（命中 / 沒命中），finding 必為 HIGH。

### 6.2.4 09_d — 資訊控制（`INFO_REVEAL`）

```markdown
# QA Report — 09_d 資訊控制 / S-01-03

[骨架]

## 重點摘要

- 應揭露：1 項（主角異能上限為 3 階）
- 應保密：1 項（反派B 是主角舊師父）
- 整體判定：⚠ 未通過（過早揭露 1 項）

## 詳細 Findings

### [HIGH] 過早揭露「反派B 是舊師父」 / Premature reveal
- **Affected**：Beat 3 / Line 18 / 角色：反派B
- **i18n KEY**：`dlg.ch01.s03.l018`
- **Summary**：細綱規範本場保密此資訊，留到第 7 場再揭；當前對白「就像當年教你那樣」暗示師生關係
- **閱讀建議**：改為更模糊的對白如「就像很久以前那樣」
```

**重點：** 資訊控制看「應揭 / 應藏」雙向。

### 6.2.5 09_e — 定稿變更紀錄（非 QA pipeline）

**注意：** 09_e **不**是 QA 模板（依 REQUIREMENTS_LOCK §4.1），是「最終 gate 紀錄」。不走 §6.2 骨架。

格式參考 SPEC §17 + REQUIREMENTS_LOCK 對 09_e 的描述。**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 09_e 具體格式由上下游 specialist 設計 — 收 §9。

UX 對 09_e 的接觸點：
- §11.1.6 Tri-column 「Pending Human Decisions」連到 09_e
- §11.5.3 LOCKED 降級引導文字提到「09_e 紀錄降級理由」
- §11.2.6 Active HD modal「複製拍板紀錄到 09_e」

不在本子節 §6 規範 09_e 內容。

### 6.2.6 09_f — 類型偏移（`GENRE_DRIFT`）

```markdown
# QA Report — 09_f 類型偏移 / S-01-03

[骨架]

## 重點摘要

- 本作類型：寫實奇幻 (Realistic Fantasy)
- 偏移檢測：1 處（喜劇感）
- 整體判定：~ 部分

## 詳細 Findings

### [MEDIUM] Beat 2 出現喜劇 timing / Comedic timing in Beat 2
- **Affected**：Beat 2 / Line 7 / 角色：反派B
- **Summary**：「（冷笑）你還沒明白嗎？」加「冷笑」標記偏喜劇調，跟本作沉重對峙風格有距離
- **閱讀建議**：改為「（淡淡看著主角）」較適合 type
```

**重點：** 類型偏移看「跟 P-arc / 作品類型 LOCK 對齊」。

### 6.2.7 09_g — 節奏感（`RHYTHM`，D-026 新增）

```markdown
# QA Report — 09_g 節奏感 / S-01-03

[骨架]

## 重點摘要

- 句長分布：mean 14.2 字 / std 4.3
- 長短句交替：✓（標準差 > 3）
- 段落呼吸感：~（Beat 2 過密）
- 整體判定：~ 部分

## 詳細 Findings

### [MEDIUM] Beat 2 段落過密 / Beat 2 too dense
- **Affected**：Beat 2（共 8 行連續對話）
- **Summary**：Beat 2 連續 8 行短句缺呼吸，預期 5-6 行為宜
- **閱讀建議**：在第 4 行後加 1 條情境描寫行或 1 條停頓行
```

**重點：** 節奏感量化指標（句長分布 / 標準差 / 段落呼吸）+ 範圍 affected。

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 09_g 具體 algorithm（句長閾值 / 段落呼吸定義）由上下游 specialist 設計 — 收 §9。

### 6.2.8 09_h — 對話張力（`DRAMATIC_TENSION`，D-026 新增）

```markdown
# QA Report — 09_h 對話張力 / S-01-03

[骨架]

## 重點摘要

- 推進 / 讓步 / 揭穿 / 反擊頻率：3 / 1 / 2 / 0
- 攻防力度：6.4 / 10
- 整體判定：⚠ 反擊缺失

## 詳細 Findings

### [HIGH] 反擊頻率 0 / No counter-attack
[§6.1 範例已示範]
```

**重點：** 4 行為類別量化 + 攻防力度評分。

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 4 類別判定 algorithm 由上下游 specialist 設計 — 收 §9。

### 6.2.9 09_i — 跨場一致性（`CROSS_SCENE_CONTINUITY`，D-026 新增）

```markdown
# QA Report — 09_i 跨場一致性 / S-01-03

[骨架]

## 重點摘要

- 對比範圍：CH01 第一章全章（S-01-01 ~ S-01-08）
- 跨場聲線漂移：0.22
- 跨場資訊洩漏：✓ 無
- 跨場節奏 arc：~ 部分偏快
- 整體判定：~ 部分

## 詳細 Findings

### [MEDIUM] 跟 S-01-02 風格重疊 / Style overlap with S-01-02
- **Affected**：本場 vs S-01-02
- **Summary**：本場主角A 句首「為什麼...」在 S-01-02 已用過 3 次
- **閱讀建議**：避免「為什麼」開頭，改用「告訴我...」「我得知道...」等變體

### [MEDIUM] 章節節奏偏快 / Chapter pacing too fast
- **Affected**：本場在 CH01 中的位置
- **Summary**：本場 = S-01-03 / 8 場，本作高潮預設 S-01-05；過早將張力拉滿
- **閱讀建議**：考慮降低本場攻防力度，留空間給 S-01-04 + S-01-05
```

**重點：** 跨場分析 — affected 可橫跨多場景；對比範圍可指定「跨章 / 跨集 / 主角 arc 全長」（**[BLOCKED:UPSTREAM_DOWNSTREAM]** 由上下游 specialist 確認）。

## 6.3 彙整版 / Combined Report

跑 `/qa S-01-03 --all` 觸發**彙整版**：8 份 QA 模板合一報告。

```markdown
# QA Combined Report — S-01-03

---

## 下一步 / Next Fix

**修補以下 4 條 HIGH 後重跑 `/qa S-01-03 --all`：**

1. 09_c：「魔法」改「異能」（dlg.ch01.s03.l002）
2. 09_d：暗示「舊師父」改模糊（dlg.ch01.s03.l018）
3. 09_h：補主角A 反擊台詞（Beat 2 / Line 4 後）
4. 09_a：「老實說」重複句首 — 句首多樣化

---

## 總體 Badge

⚠ 4 HIGH / 7 MEDIUM / 2 LOW — 未通過

---

## Required Context（彙整版 6 子分區）

依 §1.1 「Required Context 六分類」骨架（§11.2.4 同源）：

[6 子分區內容]

---

## 各模板狀態總覽

| 模板 | qa_type | 整體判定 | HIGH | MEDIUM | LOW |
|---|---|---|---|---|---|
| 09_a | AI_FLAVOR | ⚠ 未通過 | 3 | 5 | 2 |
| 09_b | VOICE_CONSISTENCY | ✓ 通過 | 0 | 0 | 1 |
| 09_c | FORBIDDEN_TERMS | ⚠ 未通過 | 1 | 0 | 0 |
| 09_d | INFO_REVEAL | ⚠ 未通過 | 1 | 0 | 0 |
| 09_f | GENRE_DRIFT | ~ 部分 | 0 | 1 | 0 |
| 09_g | RHYTHM | ~ 部分 | 0 | 1 | 0 |
| 09_h | DRAMATIC_TENSION | ⚠ 未通過 | 1 | 0 | 0 |
| 09_i | CROSS_SCENE_CONTINUITY | ~ 部分 | 0 | 2 | 0 |

---

## 詳細 Findings（按 severity 排序）

### HIGH（4 條）

[各 finding 5 欄格式]

### MEDIUM（7 條）

[各 finding 5 欄格式]

### LOW（2 條）

[各 finding 5 欄格式]

---

*來源：跑 `/qa S-01-03 --all` 於 2026-05-18 13:42*
*各模板：[09_a](/09_qa_reports/09_a_AI味檢查.md), [09_b](...), [09_c](...), [09_d](...), [09_f](...), [09_g](...), [09_h](...), [09_i](...)*
```

**規則：**
- 「下一步」段優先列 HIGH 修補（依優先級降序）
- 「Required Context」段在中間（user 看 finding 時可參考）
- 「各模板狀態總覽」表格 + 「詳細 Findings」按 severity 排序
- 不重複每模板的 finding 個別段（彙整版 = 8 份 findings 按 severity 串）

## 6.4 三層守則對齊

| 守則 | §6 對應 |
|---|---|
| G1 badge 不單獨呈現 | 總體 badge `⚠ 4 HIGH...` — 包含 severity 細分 + Next Fix 三層 |
| G2 流程視覺化僅閱讀順序 | 8 模板表格順序為閱讀順序，不代表必跑全部 |
| G3 UX grouping 不是資料層必要單位 | Required Context 6 子分區是排版骨架 |
| 中文主+英文 sub | 全標題雙語 |
| Severity 在最前 | finding 標題 `[HIGH] / [MEDIUM] / [LOW]` 前綴 |
| Affected 精確到行 | Beat / Line / 角色 + i18n KEY 四欄 |
| 純 Markdown | finding 「閱讀建議」純列舉，無按鈕 |

## 6.5 跟 §11.2.10 QA finding modal 的關係（複述）

| 維度 | §6 L1 chat 報告 | §11.2.10 L2 modal |
|---|---|---|
| Form factor | 純 Markdown 報告 | 中央 modal HTML |
| 觸發 | user 跑 `/qa` skill | user 點 Scene Detail 側欄 [展開] |
| 多 finding | 完整列出 | 摘要 + 點開單一 finding 看 modal |
| 「複製指令」 | user 自己 copy `/dialogue-write ... --single-iter` | 按鈕（§11.6） |
| 閱讀建議 | 純列舉 Markdown | 純列舉 + 末尾 1 個複製 iterate 按鈕 |

兩者**內容同源**（同一份 source markdown），呈現方式不同。

---

---

# 7. 跨檔導航設計

## 7.1 跨檔連結路徑基準

**規則：以 project root 為基準，連結以 `/` 開頭。**

理由：
- 任何 `/view-*` 動態組合輸出在 chat 中，使用者不會點連結；連結是給 `/export-*` 寫到 `view/` 後在編輯器 / GitHub 預覽中用
- 相對路徑會因為 `view/` 與 source 檔深度不同（`/view/世界觀.md` vs `/01_world/01_a_xxx.md`）造成混亂
- project root 為基準是唯一既能在 `view/` 又能在 source 檔互通的寫法

**寫法：**

```markdown
詳見 [世界規則總覽](/01_world/01_a_世界觀總覽.md)
本場相關角色：[主角A](/03_characters/main/主角A_聲線卡.md) / [反派B](/03_characters/main/反派B_聲線卡.md)
```

**例外：** Markdown 內部 anchor 引用（同檔內跳轉）用 `#anchor-slug`，不加 `/`：

```markdown
詳見 [世界規則章節](#世界規則)
```

## 7.2 Breadcrumb 引導列

**規則：每份 `/export-*` 整合檔在 frontmatter 之後、第一個 `#` 標題之前，加一行 breadcrumb。`/view-*` chat 動態組合不加。**

格式：

```markdown
> 專案首頁 / 世界觀 / 完整視圖
```

不加箭頭符號、不加日期、不加狀態 badge（這些都在 frontmatter）。Breadcrumb 純粹回答「我在文件結構的哪裡」。

**「← 回 X」連結：** 整合檔末尾加一行：

```markdown
---
[← 回 `/view-*` 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

`/view/README.md` 在 `/export-*` 累積 ≥1 份檔案後由使用者手動建立（不自動生成；列為 §10 master 裁決議題）。

## 7.3 長文件 TOC 與 anchor 規則

**TOC 觸發條件：** 整合檔（`/export-*` 產出）任一份預估 > 200 行時，在 frontmatter 與 breadcrumb 之後、第一個 `#` 標題之前加 TOC。

**TOC 格式：**

```markdown
## 目錄 / Contents

- [世界規則 / World Rules](#世界規則-world-rules)
- [世界語言 / World Language](#世界語言-world-language)
- [陣營與階級語言 / Faction and Class Language](#陣營與階級語言-faction-and-class-language)
- [詞彙系統 / Vocabulary](#詞彙系統-vocabulary)
  - [專有名詞 / Proper Nouns](#專有名詞-proper-nouns)
  - [俗稱與黑話 / Slang](#俗稱與黑話-slang)
  - [禁用詞與慎用詞 / Forbidden and Cautious Words](#禁用詞與慎用詞-forbidden-and-cautious-words)
```

**Anchor slug 規則：**

- 中文主＋英文 sub 標題 `世界規則 / World Rules` → slug `世界規則-world-rules`（GitHub flavored MD 自動行為）
- 全形空白與 `/` 在 slug 中替換為單一 `-`
- 不手動寫 `{#anchor}`，依賴自動生成
- specialist agent 在生成 TOC 時，必須與實際標題對應的 slug 一致（**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 由上下游 specialist 在 `/view-*` skill 實作時驗證 slug 一致性）

## 7.4 Source 引用：整合視圖內如何標出「這段來自哪個檔」

**規則：每個 source 段落結束時，最末加一行 italic 引用，標出來源。** 不用 `>` 引用塊，避免跟一般引用混淆。

格式：

```markdown
## 世界規則 / World Rules

[組合後的內容]

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md)*
```

**多 source 合併段落：** 列出全部來源，逗號分隔：

```markdown
*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md), [/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md)*
```

**chat 動態組合：** 同樣加 source 引用（即使連結點不到，純文字仍提供定位線索）。

## 7.5 單向 reference 原則

- A 引用 B 時，A 內寫 `[B 標題](/path/to/B.md)`
- **B 不必反向列出所有引用它的文件**（避免雙向維護成本）
- 例外：`/view-character` 的角色聲線卡可在末尾列「出場場景」（這是 frontmatter `entities` 反查的結果，由 `/view-*` 動態生成，非手動維護）

## 7.6 view/ 內部錨點命名

**已於 §7.3 涵蓋（自動 slug，不手動命名）。**

## 7.7 view 檔的 update / regenerate 失效提示

當 source 檔變動但 `view/` 整合檔未重新 `/export-*` 時：

- **`/check-gaps`** 或 **`/status`** 應加一段警告（**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 確認 `/check-gaps` 是否處理此偵測；UX 只負責提示文案）：

```markdown
## ⚠ view/ 整合檔需更新 / View Files Need Refresh

下列 view/ 檔案的 source 已修改，但整合檔未重新匯出：

- `/view/世界觀.md`（source `/01_world/01_a_世界觀總覽.md` 於 2026-05-18 修改，view 最後匯出 2026-05-15）
- `/view/角色_主角A.md`（source `/03_characters/main/主角A_聲線卡.md` 於 2026-05-17 修改，view 最後匯出 2026-05-10）

**下一步：** 對受影響 entity 重跑 `/export-*` 更新整合檔。
```

---

## 7.8 對齊 UPSTREAM_DOWNSTREAM_SPEC §7 53 個 [UX] 標記

對應 UX-7 任務 + INTEGRATION_CONTRACTS §3 Contract B（上下游 → UX 配對）。

本子節列出 UPSTREAM_DOWNSTREAM_SPEC §7 的 53 個 [UX] 標記（編號沿用 UPSTREAM 命名 UX-1 ~ UX-53，**跟本 spec REVISED_WORK_ITEMS §7.5 的 UX-1~UX-17 任務編號區隔**），及其在本 spec 中的對應章節。

**呈現粒度說明：** UPSTREAM 標記的「呈現需求」依本專案 form factor（純 Markdown L1 / HTML L2 / Markdown export L3）三層分流處理 — 多數需求在 L1 純 Markdown 與 L2 HTML 都有對應呈現章節，本表標兩處。

### 7.8.1 UPSTREAM §7.1 — 上游協議共通互動（UX-1 ~ UX-6）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-1 | 議題進度條的呈現 | §4 `/status` 場景就緒度進度條（§4.3.4） | §11.1.4 場景就緒度區 |
| UPS-UX-2 | 觸發語提示行 | §4 `/status` 看板「下一步」段（§4.3.2） | §11.1.2 HERO 下一步建議卡 |
| UPS-UX-3 | 缺失流程「跑 skill / 跳過 / 取消」三選 | §8.1 錯誤訊息四件套 + 純列舉建議（§1.4.3） | §11.2.10 QA modal「閱讀建議純列舉」+ §11.6 複製指令按鈕 |
| UPS-UX-4 | 收斂預告稿版面（議題結論 + TODO/INFERENCE/CONFLICT 標籤） | §2.3 / §2.4 `/view-outline` `/view-detailed-outline` 模板 | §11.2.7 Beat / Outline Preview |
| UPS-UX-5 | 階段轉換提示 | §4 `/status` 模組狀態總覽（§4.3.5） | §11.1.5 模組狀態總覽 |
| UPS-UX-6 | `/status` 印出後「下一步建議」 | §4 整段就是這個（§4.3.2） | §11.1.2 HERO 下一步建議 |

### 7.8.2 UPSTREAM §7.2 — 00_e 世界觀協議（UX-7 ~ UX-9）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-7 | 11 議題進度條 | §4 `/status` 場景就緒度延伸 | §11.1.4 進度條（按 entity type 細分） |
| UPS-UX-8 | 收斂預告稿（含 00_b 預覽） | §2.1 `/view-world` + Glossary tooltip (§11.9.3) | §11.9.2 Harness Preview |
| UPS-UX-9 | 觸發語提示行視覺差異 | §4 `/status` 內各階段標 emoji（如「~ Authoring」） | §11.1.5 模組狀態列「狀態 + 細項」分層（G1） |

### 7.8.3 UPSTREAM §7.3 — 00_f 角色協議（UX-10 ~ UX-13）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-10 | N 角色 × 9 議題進度條 | §4 `/status` 模組狀態 + §2.2 `/view-character`（每角色一段） | §11.1.4 + §11.1.5 進度條（**[NEEDS_SCHEMA_SUPPORT]** 9 議題 per character 的 query API） |
| UPS-UX-11 | 5 題聲線測試 + 答案並排 | §2.2 `/view-character` 聲線卡段表格 | §11.2.4 Required Context 「2. 出場角色」展開 + §11.3.5 details pane 角色 metadata |
| UPS-UX-12 | 兩角色聲線去名測試對比 | §6.2.2 09_b 聲線一致性報告 finding | §11.2.10 QA modal 09_b 展開 |
| UPS-UX-13 | 多角色合規列表 | §6.2.2 09_b 報告彙整 + §4 `/status` | §11.1.5 模組狀態列「C/* 角色」行細項 |

### 7.8.4 UPSTREAM §7.4 — 00_g 大綱協議（UX-14 ~ UX-17）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-14 | 主線一句話 + 核心衝突 + 主題確認介面 | §2.3 `/view-outline` 重點摘要段 | §11.2.7 Beat / Outline Preview |
| UPS-UX-15 | 想要 vs 需要兩條軸並排 | §2.3 `/view-outline` 章節 section 內表格 | §11.2.7 內並排表格 |
| UPS-UX-16 | 規模定位 a/b/c/d 視覺呈現 | §2.3 `/view-outline` 章節 metadata 段 | §11.2.7 Beat preview metadata |
| UPS-UX-17 | 類型偏移風險清單（含來源標） | §6.2.6 09_f 類型偏移報告 finding | §11.2.10 QA modal 09_f 展開 |

### 7.8.5 UPSTREAM §7.5 — 00_h 細綱協議（UX-18 ~ UX-22）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-18 | 逐章節奏標籤（時間軸 + 顏色） | §2.4 `/view-detailed-outline` Beat 結構段 | §11.2.7 Beat preview（HTML 顏色映射） |
| UPS-UX-19 | 弧線 × 章節矩陣 | §2.4 章節「主線情節 P-arc」表格 | §11.2.7 矩陣表格 |
| UPS-UX-20 | 資訊揭露時間軸 | §2.4 「揭露資訊」段 | §11.2.4 Required Context「5. 資訊揭露控制」+ §11.2.7 時間軸 |
| UPS-UX-21 | 伏筆 / 回收配對 | §2.4 「跨場連結」段 | §11.2.4 Required Context「6. 跨場警示」 |
| UPS-UX-22 | 高風險場景密度警示 | §2.4 + §6.2.9 09_i 跨場一致性 | §11.1.3 卡點 + §11.2.5 Active QA |

### 7.8.6 UPSTREAM §7.6 — 00_l 關係協議（UX-23 ~ UX-26）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-23 | 權力四維評估（雷達 / 表格） | §2.2 `/view-character` 「角色關係」段表格 | §11.2.4 Required Context「3. 角色關係」+ 表格化呈現（HTML 雷達非必要 — 表格已足） |
| UPS-UX-24 | 稱呼系統「情境 → 稱呼」 | §2.2 `/view-character` 內表格 | §11.3.5 details pane 角色 metadata 補欄位 |
| UPS-UX-25 | 不能說出口的事的表 | §2.2 + §2.4「資訊揭露控制」 | §11.2.4「5. 資訊揭露控制」+「6. 跨場警示」 |
| UPS-UX-26 | 關係時間線錨點 vs 05_b 並排 | §2.3 / §2.4 章節 section 內並排表格 | §11.2.7 Beat preview 並排 |

### 7.8.7 UPSTREAM §7.7 — 下游 00_k pipeline（UX-27 ~ UX-34）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-27 | 任務包收斂預告稿（含 TODO 清單） | §2.4 細綱「Beat 結構」+ §5 B.8 任務包 gate | §11.2.3 Scene Readiness Panel + §11.2.7 Beat preview |
| UPS-UX-28 | 任務包 frontmatter 呈現 | §3.2 整合檔 frontmatter 格式 | §11.2.2 Scene Detail 主欄頂部 + §11.3.5 details pane |
| UPS-UX-29 | 多版本生成進度條 | §4 `/status` Trial / Convergence 行 | §11.3.3 版本標頭列（N 欄 + 標頭 mode_tag / pipeline_state） |
| UPS-UX-30 | 8 份 QA 並行檢查、序列印出 | §6.3 彙整版 Combined Report | §11.2.10 QA modal 多 finding 展開 |
| UPS-UX-31 | 09_f 重大命中「後 4 份判定基準警示」 | §6.3 彙整版內顯示 09_f 命中後 affect 註記 | §11.2.5 Active QA 09_f finding 卡片附 warning |
| UPS-UX-32 | 場景狀態機 (pipeline_state) 可視化 | §5 6 REVIEW gates + §4 `/status` 場景就緒度 | §11.2.3 Scene Readiness Panel + §11.4 facet「Pipeline State」 |
| UPS-UX-33 | QA_FAILED 三條路徑（修稿 / 重生 / 保留） | §8.2 系統狀態未滿足 + §6 finding 「處理方式」段 | §11.2.10 QA modal「閱讀建議」+ §11.6 複製指令 |
| UPS-UX-34 | FINAL 時填 09_e 引導 | §11.5.3 Z2 candidate α 引導文字（複製到剪貼簿）— L1 / L2 共用 | 同左 + §11.2.6 Active HD modal「複製拍板紀錄到 09_e」 |

### 7.8.8 UPSTREAM §7.8 — QA 報告（UX-35 ~ UX-38）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-35 | 8 份 QA 報告閱讀體驗（升 5 → 8） | §6.2.1 ~ §6.2.9 各模板閱讀體驗 | §11.2.10 QA modal 各模板展開 |
| UPS-UX-36 | co-flagged 共同命中視覺標籤 | §6.3 彙整版內 finding 加「co-flagged」前綴標籤 | §11.2.10 QA modal 加 badge「同 finding 命中 2 模板：09_a + 09_c」 |
| UPS-UX-37 | 09_e 定稿變更紀錄填寫表單視覺 | §11.5.3 Z2 candidate α 引導文字（L1 / L2 共用） | 同左 |
| UPS-UX-38 | retcon 紀錄在 09_e 的特殊呈現 | **超出 v0.2 scope**（D-018 #1 retcon 不採） | 同左 — **不適用** |

**UPS-UX-38 處理：** v0.2 不做（依 D-018 #1 retcon 維持不採）；未來若採 retcon 需在新版 UX_SPEC 補設計 — 收 §10。

### 7.8.9 UPSTREAM §7.9 — /dialogue-write（UX-39 ~ UX-41）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-39 | 三方向生成進度條 | §4 `/status` Trial 行細項 | §11.3.3 版本標頭列 |
| UPS-UX-40 | --converge 模式多版本並排 + 點選保留 | **L1 無**（純 Markdown 不支援點選保留）— 走 §11 L2 | §11.3 Scene Editor N 欄並排（核心功能）+ §11.3.5 details pane 版本對照 |
| UPS-UX-41 | 破格版「破格方向」「不可直接使用」呈現 | §6.2.6 09_f 類型偏移 finding + Mode Tag `EXPERIMENTAL` 標 | §11.3.3 版本標頭加 badge「EXPERIMENTAL — 不可直接使用」 |

### 7.8.10 UPSTREAM §7.10 — Canon delta（UX-42 ~ UX-45）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-42 | delta 候選清單（表格 / 卡片） | §4 `/status` 「Canon Δ pending」段 | §11.1.6 三欄區「Canon Δ pending」+ 點開 modal |
| UPS-UX-43 | 拍板介面（採 / 棄 / 修改 / 衝突） | §8.1 + §6 純列舉建議 + 「複製指令」走外部 chat | §11.2.6 Active Canon Δ modal「複製拍板紀錄」按鈕（§11.6） |
| UPS-UX-44 | 影響範圍評估視覺化（樹狀） | §2 view-\* 「跨場連結」/「跨檔引用」段 | **超出 v0.2 scope**（依 §1.3 + UX_PROTOTYPE_ANALYSIS §4.3 拒絕「F8 依賴反查視覺化」）— **不做** |
| UPS-UX-45 | LOCKED 檔案衝突的 retcon 介面 | §11.5 LOCKED 守門（Z2 candidate α）— retcon 不採時用 DEPRECATED 路徑 | 同左 |

**UPS-UX-44 處理：** v0.2 不做（依 Bucket #3 F8 不做）；未來若需要走 P-NNN 新議題 — 收 §10。

### 7.8.11 UPSTREAM §7.11 — 多場景並行（UX-46 ~ UX-49）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-46 | 多 skill 並行分頁 / 分卡片呈現 | §4 `/status` 模組狀態總覽各行（不分頁） | §11.7 多場景並行（多分頁工作流） |
| UPS-UX-47 | 鎖等待「請稍候」提示 | §8.2 系統狀態未滿足 | §11.7.7 多分頁同編 hint + §11.7.6 conflict modal |
| UPS-UX-48 | 並行衝突 abort 後下一步 | §8.1 錯誤訊息四件套 | §11.7.6 conflict modal「reload 棄改 / 強制覆寫」二選 |
| UPS-UX-49 | 上游 iterate 啟動「下游正在用此實體」清單 | §8.2 系統狀態未滿足 + 卡點段 | §11.1.3 卡點 HERO + §11.7.7 hint |

### 7.8.12 UPSTREAM §7.12 — 跨節共通（UX-50 ~ UX-53）

| UPS 編號 | 需求 | L1 對應 | L2 對應 |
|---|---|---|---|
| UPS-UX-50 | TODO / INFERENCE / CONFLICT 三類標籤視覺差異 | §6 finding severity 三級 + §2 view-\* 內標籤（**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 三類定義由上下游確認） | §11.2.10 QA modal 加 badge / §11.3.5 details pane 加 label |
| UPS-UX-51 | phase_log 閱讀介面（時間軸 + 篩選） | §4 `/status` 結尾「狀態：截至 X 時間」 + 跑 `/status --since X` 時間範圍 | §11.4 facet「Stage」+「Pipeline State」+ §11.7 多分頁讓 user 開 phase_log 檔 |
| UPS-UX-52 | frontmatter 編輯介面 | **L1 無**（純讀） | §11.5 LOCKED 守門時「複製手動編輯引導文字」（Z2 candidate α）— frontmatter 不在前端直接編，走外部編輯器 |
| UPS-UX-53 | 跳階段時「當前已確認資料快照」呈現 | §6.2.5 09_e 區域 + §3 整合檔 frontmatter | §11.9.2 Harness Preview「Instance 微調紀錄」 |

### 7.8.13 對齊總結

| 維度 | 數字 |
|---|---|
| UPSTREAM §7 列出 [UX] 標記 | 53 個 |
| 在 v0.2 對應呈現章節已展開 | 51 個 |
| 在 v0.2 標**不適用 / 超出 scope** | 2 個（UPS-UX-38 retcon / UPS-UX-44 依賴樹狀圖） |
| 在 v0.2 標 **[BLOCKED:UPSTREAM_DOWNSTREAM]** | 6 個（具體 algorithm 由上下游決） |
| 在 v0.2 標 **[NEEDS_SCHEMA_SUPPORT]** | 跨多項，集中在 §9 |

**確認：** UX-7 任務完成。本子節是上下游 specialist 在第二輪交付後與 master 第四輪整合時的核心對照表 — 53 個 marker 全部覆蓋（含 2 個明示「v0.2 不做」）。

---

## 7.9 對齊 UPSTREAM_DOWNSTREAM_SPEC §10/§11/§12/§13 — UX-54~80 對照表（v0.3 新增）

對應 D-046 #1+#2 / CODEX C-06 / O-04 派工。

UD spec v0.2 增加 §10（手稿導入）/ §11（dialogue_keys + KEY UI）/ §12（export 路徑）/ §13（A-\* lifecycle）— 共新增 27 個 [UX] 標記（UX-54~80）。v0.2 §7.8 只覆蓋舊 UX-1~53，**未覆蓋這 27 個**，CODEX 標為主要缺口。

**v0.3 補表 + 合併重複：** 依 UD §10.5.3 與 §1.0.4 對齊聲明（「UX-64/65 跟 UX-54/55 為同一 UX 元件」），把 UX-54+55、UX-64+65 合併為兩筆，**淨增 25 筆**。

### 7.9.1 UD §10 手稿導入路徑（UX-54+55 合併 / UX-56 / UX-64+65 合併 / UX-66 / UX-67 / UX-68）

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| **UPS-UX-54+55**（合併）| 跳階段路徑下「議題對應表」呈現 — 手稿哪段對應哪個議題編號 + 抽取信心度 + REQUIRED 缺漏的「請補在手稿後重貼」清單 | §2.5 對話中臨時呈現 + §8.1 錯誤訊息四件套 | §11.2.10 modal「議題對應預覽」+ §11.6 複製指令按鈕 | UD §10.5.3 確認跟 §1.0.4 UX-54/55 為同一元件 — 合併 |
| UPS-UX-56 | STRONGLY_PREFERRED 缺漏的 TODO 標記預覽 | §2.3 / §2.4 view 模板 + 「重點摘要」段 | §11.2.7 Beat / Outline Preview 加 ⚠ TODO badge | — |
| **UPS-UX-64+65**（合併）| 同 UX-54+55 但在前端工具 §11 編輯介面（不在 chat） | （L1 不適用）| §11.3 Editor 內 manuscript-import session modal — 顯示議題對應 + REQUIRED 缺漏清單 + 抽取信心度 + 「請補在手稿後重貼」引導 | UD §10.5.3 / §5.1 確認重複 — 合併 |
| UPS-UX-66 | 衝突偵測表呈現（手稿導入時與既有 entity 命名衝突） | §6.3 彙整版 QA report 「co-flagged」共同命中表（類比） | §11.7.6 Conflict Modal 延伸支援「entity 命名衝突 4 選項」（merge / overwrite / create-as-new / skip 依 D-033） | UD §10.5.3 + §9.2.4 — 跟 §11.7.6 sibling，4 選項對應 D-033 |
| UPS-UX-67 | trust-level 選擇的 chat 互動 | §2.5 臨時呈現 + agent 提示文案（「請指定 trust-level： --trust-level agent_assisted / external_llm」） | §11.6 複製指令按鈕 — 依 D-031 trust-level 走外部 chat，不在前端 UI 選 | trust-level 限上游 `/create-*`（D-038 細化 + C-08）；不影響下游 |
| UPS-UX-68 | 導入完成後 phase_log 摘要呈現 | §4 `/status` 內可加「最近導入」段 | §11.1.6 三欄區可加「最近導入」卡 + §11.1.6a A-\* asset panel 對齊（若導入含 A-\*）| 對齊 D-042 phase_log 全收 5 新欄位 |

### 7.9.2 UD §11 dialogue_keys + KEY UI（UX-60 ~ UX-63）

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| UPS-UX-60 | `dialogue_keys` frontmatter block 編輯時的呈現 — 不該讓 user 直接看 YAML 鍵值 | （L1 不適用 — 編輯是 L2 職責） | §11.3 Editor 內 details pane（§11.3.5 KEY metadata）— 不顯示 raw YAML，**改顯示**「KEY: dlg.ch01.s03.l001 / 說話者: 主角A / 立繪: A-portrait-主角A-default」等可讀分欄；YAML 細節由前端 parse | 對齊 D-037 Map (DICT) shape — 前端從 frontmatter block 解析後分欄顯示 |
| UPS-UX-61 | 內文 `<!-- KEY: -->` 在 view-only 模式的顯示策略 | §2.5 view 模板 — 預設**隱藏** comment（純讀人類友善版） | §11.2.9 Dialogue Draft Preview / §11.3.4 Editor textarea — **預設隱藏**；hover 該行可顯示 KEY；切換「顯示 KEY」按鈕 toggle 全文 KEY 顯示 | 對齊 §11.3.5 details pane 是 KEY 詳細看的地方，inline 不顯示 |
| UPS-UX-62 | user 改 KEY 名時的互動 | （L1 不適用） | §11.3 Editor — **不在 textarea 直接編 KEY**；改在 §11.3.5 details pane 內提供「rename KEY」按鈕 → 開 modal 輸入新 KEY + 自動把舊 KEY 加入 aliases | 對齊 D-022 KEY alias mapping；D-037 `aliases` list 在 Map shape 內 |
| UPS-UX-63 | DEPRECATED KEY 在前端 view-only 的呈現 | §6.3 彙整版 QA report 內 DEPRECATED KEY 用刪除線 + label「DEPRECATED」 | §11.2.9 Preview / §11.3.4 Editor — DEPRECATED KEY 用灰色 + 刪除線；details pane 顯示 `status: deprecated / deprecated_reason / deleted_at` | 對齊 D-037 KEY lifecycle metadata `status: active\|deprecated\|deleted` |

### 7.9.3 UD §11 SINGLE_ITER 迭代版本（UX-57 / UX-58 / UX-59）

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| UPS-UX-57 | 「迭代版本預覽」+「相對原版的 diff 摘要」呈現 | §6.1 QA finding affected + §6.3 彙整版 | §11.3.3 Editor 標頭加 `base_dialogue → v01A_iter1` chain；§11.3.5 details pane「版本對照」段對 base 顯 diff | 對齊 D-042 `base_dialogue` 欄位（**不重用 `source_dialogues`**） |
| UPS-UX-58 | iter 鏈視覺化（從 v02 → iter1 → iter2 → iter3 時間線 / 樹狀） | §2.4 view-detailed-outline「跨場連結」段可顯示版本鏈 | §11.3.3 Editor 上方加 lineage timeline 條（chain 顯示） | 對齊 D-042 `iteration_count` / `base_dialogue` 串成 chain |
| UPS-UX-59 | 連續 ≥ 3 次 iter 後 agent 主動建議跑 QA 的呈現 | §8.2 系統狀態未滿足 hint「您已 iter 3 次，建議跑 /qa」 | §11.3.3 Editor 標頭浮顯 ⚠ hint banner「您已 iter 3 次，建議跑 QA」 + 「[📋 複製 /qa 指令]」按鈕 | iteration_count 從 D-042 phase_log 讀 |

### 7.9.4 UD §11 entity ID + cross-ref UI（UX-69 / UX-70 / UX-71）

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| UPS-UX-69 | entity ID 視覺化（`C-主角A` / `A-portrait-...` / KEY hover 描述 / 點擊跳轉） | §2 view 模板內 entity ID 加 `[](/path)` link | §11.2.4 Required Context / §11.3.5 details pane — entity ID 為可 hover token，顯示 tooltip 含完整描述 + 點擊跳 source 檔（§11.7 多分頁） | 整個 entity ID 可作 §11.9.3 Glossary tooltip 的延伸 |
| UPS-UX-70 | cross-ref 失效警示（dialogue 引用的 A-\* 在 repo 不存在） | §6.3 QA report finding 升級 — 增 `[HIGH] dlg.X.Y 引用 A-Z 但 entity 不存在` | §11.2.4 Required Context 內失效引用標 ⚠ 紅 badge / §11.3.5 details pane「⚠ 缺檔」/ §11.1.6a A-\* asset panel ⚠「缺檔」狀態 | 對齊 §11.1.6a.1 缺檔警示 |
| UPS-UX-71 | A-\* 立繪 cross-ref 在 dialogue 編輯時的選擇 UI | （L1 不適用 — 編輯是 L2） | §11.3.5 details pane 內「立繪 KEY」欄位**改為 dropdown** — 從 `10_art_assets/portraits/` registry 動態載；可手動輸入新 KEY（**但前端不建檔**，需 user 切外部跑 agent 或手動編輯 `10_art_assets/<subtype>/<group>.md`（v0.4 master 第四輪 CC-01 校正 — 採 DF subtype/group canonical 模型；原 `10_art_assets/<key>/metadata.md` 寫法 supersede）） | Bucket #3 F4 立繪預覽 ✗（前端不知實檔）— 但仍需 registry browse；對齊 D-041 source of truth |

### 7.9.5 UD §12 Export 路徑（UX-72 ~ UX-75）

⚠ **重要 v0.3 變更：** UX-72/73/74/75 原 UD 設計假設前端按鈕跑 server-side CLI（C-03 critical）。D-038 拍板採 A1 prompt + CC/CODEX 後，**「export」不再是前端動作**，而是 prompt 產生 + clipboard / POST。UX-72~75 全部改對齊 §11.6.11 Export Prompt panel。

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| UPS-UX-72 | 前端「匯出」按鈕的 scope / filter 選擇 UI | （L1 不適用） | §11.6.11.1 **Export panel 範圍 / 格式 / 推送方式** 全部 UI 欄位 | 對齊 L3_EXPORT_PROMPT_SCHEMA §2 |
| UPS-UX-73 | export dry-run 結果預覽 | （L1 不適用） | §11.6.11.3 **預覽 Prompt modal** — 顯示完整組裝後的 prompt 含 scope counts | dry-run 在 A1 模型下退化為「預覽 prompt」— 不是真跑 export，是預覽 instruction |
| UPS-UX-74 | export 完成後「下載連結 / 開啟資料夾」按鈕 | （L1 不適用） | §11.6.11.4「複製 / 推送」後 toast「✓ 已複製 — 請貼到 CC / 推送到本地 LLM」+ 不顯示「下載連結」（**因為 export 不在前端執行**，user 切外部 chat 跑） | A1 模型下「export 完成」是在外部 agent 那邊 — 前端不知道何時完成；只能顯示「prompt 已送出」 |
| UPS-UX-75 | agent chat 中 export 完成後「stdout 摘要 + 輸出檔路徑」呈現 | §4 `/status` 內可顯示「最近 export」段 | §11.1.7 Module Navigation Views 列表 — agent 完成後 user 切回前端 refresh，列表會出現新 `export/2026-05-19_full.{json,md}` | 對齊 L3_EXPORT_PROMPT_SCHEMA §1.5「完成回報格式」由 agent 回吐 |

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — UD §12 需配合 D-038 改寫（移除 server-side CLI 假設）。本對照表暫以 §11.6.11 為對應；待 UD §12 修訂後重新對齊。

### 7.9.6 UD §13 A-\* lifecycle（UX-76 ~ UX-80）

| UPS 編號 | 需求 | L1 對應 | L2 對應 | 備註 |
|---|---|---|---|---|
| UPS-UX-76 | 編輯 dialogue 時的 A-\* 引用 UI（registry 下拉 / 直接輸入 / 新建按鈕） | （L1 不適用） | §11.3.5 details pane「立繪 KEY」欄位 — dropdown from registry + 手動輸入 + 「新建（複製建檔指令）」按鈕 | 同 UX-71；對齊 D-041 `10_art_assets/` 為 registry |
| UPS-UX-77 | A-\* registry 在 §11.4 搜尋篩選介面的呈現（subtype / owner / state facet） | §4 `/status` 篩選簡述 | §11.4 facet 第 8 維 **A-\* asset**（subtype / owner / state 三層 sub-facet） | 對齊 D-044 7 subtype + D-041 |
| UPS-UX-78 | A-\* DEPRECATED 引用視覺警示 | §6 QA report finding「dialogue 引用 DEPRECATED A-\*」 | §11.3.4 Editor textarea 該行 hover 顯示 ⚠ + §11.3.5 details pane 顯示「⚠ 該 A-\* 已 DEPRECATED — 建議改 [新 KEY]」 | 對齊 D-037 KEY lifecycle metadata 同精神 |
| UPS-UX-79 | A-\* lifecycle 互動（建立 / 改名 / DEPRECATE）對話腳本格式 | §2.5 臨時呈現 + 「複製 4 選項」按鈕對應 D-033 | §11.6.11 Export panel + §11.6 通用「複製指令」按鈕（4 選項合併進 ConflictModal 延伸 / 或獨立 A-\* lifecycle modal） | 對齊 D-033 4 選項（merge/overwrite/create-as-new/skip）+ D-031 不新增 skill |
| UPS-UX-80 | A-\* 對 dialogue 影響的視覺化（如「換立繪會影響 N 句」）| §6 QA report finding affected scope | §11.3.5 details pane「立繪 KEY 影響範圍」段顯示「本 KEY 被 X 句引用」 + §11.1.6a A-\* asset panel 子表「覆蓋」欄 | 對齊 §11.1.6a.1 `dialogue_keys.<KEY>.portrait` 反查 |

### 7.9.7 對齊總結 — UX-1~UX-80 全覆蓋

| 維度 | 數字 |
|---|---|
| UPSTREAM §7 + §10/§11/§12/§13 列出 [UX] 標記 | UX-1~UX-80 共 80 個 |
| 重複 / 合併後 | 78 個獨立 UX 元件（合併 UX-54+55 / UX-64+65 兩對） |
| v0.3 本對照表覆蓋 | 78 個獨立元件全覆蓋（§7.8 收 UX-1~53 共 51 項展開 + 2 項不做；§7.9 收 UX-54~80 合併後 25 項） |
| 標 **[BLOCKED:UPSTREAM_DOWNSTREAM]** | 8 個（具體 algorithm / UD §12 改寫等由上下游決） |
| 標 **[NEEDS_SCHEMA_SUPPORT]** | 跨多項，集中在 §9（v0.3 已按三類拆分） |

**確認：** D-046 #1+#2 派工完成。本子節 + §7.8 構成 UX-1~UX-80 完整對照表，可作 Contract B 完成證明。

---

# 8. 錯誤提示通用結構

## 8.1 錯誤訊息四件套（沿用 prior draft）

任何 skill 拒絕執行或回報錯誤時，輸出必含四欄：

```markdown
## ✗ 無法執行 / Cannot Proceed

- **What**：缺先決條件，`/dialogue-write` 拒絕執行
- **Where**：任務包 `/07_scene_tasks/CH01_S03_台詞任務包.md`，欄位「出場角色聲線卡引用」
- **Why**：核心欄位為 TODO，依 D.3 規則 TODO 缺核心欄位即拒絕
- **下一步**：補齊聲線卡引用（從 `/03_characters/main/` 對應角色檔複製）；補完後重跑 `/dialogue-write S-01-03`
```

**對應 frontmatter 規則：**

- 標題用 `## ✗ 無法執行 / Cannot Proceed` 或 `## ⚠ 需注意 / Warning`
- 四個欄位以 bullet list 呈現
- 「下一步」永遠用祈使句，不用「應該」「可能」「建議考慮」等模糊詞
- 不顯示 stack trace、不顯示 enum 鍵（前述 §1.2 規則）

## 8.2 使用者錯誤 vs 系統狀態未滿足（兩種口氣）

**(A) 使用者錯誤**（指令拼錯、ID 不存在、參數缺失）：

```markdown
## ✗ 無法執行 / Cannot Proceed

- **What**：找不到場景 `S-09-99`
- **Where**：`/06_a_場景索引.md` 中無此 ID
- **Why**：指令 `/scene-task S-09-99` 中的場景 ID 不在場景索引內
- **下一步**：用 `/view-detailed-outline` 查當前已建場景 ID；或先在細綱中新增場景再跑 `/scene-task`
```

口氣：客觀、可操作、不指責。

**(B) 系統狀態未滿足**（先決條件不夠成熟、需等其他階段完成）：

```markdown
## ⏸ 條件未滿足 / Prerequisites Not Met

- **What**：本場 Bible context 尚未備齊
- **Where**：場景 `S-01-03` 涉及角色 `C-主角A`、`C-反派B`
- **Why**：`C-反派B` 聲線卡狀態為 DRAFT，依 00_k 階段 1 啟動條件需 ≥ REVIEW
- **下一步**：跑 `/iterate-character 反派B` 完成聲線卡迭代，或人類審完後升 REVIEW；其後重跑 `/scene-task S-01-03`
```

口氣：說明等什麼條件解除、條件解除後做什麼。**不要寫成像使用者犯錯**。

## 8.3 空狀態（empty state）文案

**規則：不只說「無 X」，要說「為什麼是正常」或「下一步可考慮」。**

範例：

```markdown
## 卡點 / Blockers

*目前無卡點 — 所有實體已通過先決條件檢查。可考慮跑 `/scene-task` 啟動下一場 dialogue 生產。*
```

```markdown
## 待人類裁決 / Pending Human Decisions

*目前無待裁決事項。下一波預期出現在 D.3.5 收斂 gate 或 QA_FAILED 後的破格保留判定。*
```

**italic + 灰調文案**：用 `*斜體*` 包覆，跟正式內容區隔。

## 8.4 多錯誤累積的彙整呈現

當單次執行命中多個錯誤時，**不平鋪四件套四次**，而用「彙整 + 逐項展開」：

```markdown
## ✗ 無法執行 / Cannot Proceed — 3 項問題

**彙整：** 任務包有 2 個核心欄位缺漏，且場景索引有 1 項衝突。需先處理才能啟動 `/dialogue-write`。

### 問題 1：核心欄位「出場角色聲線卡引用」為 TODO
- **Where**：`/07_scene_tasks/CH01_S03_台詞任務包.md`
- **下一步**：補齊聲線卡引用（從 `/03_characters/main/` 對應檔）

### 問題 2：核心欄位「角色真實目標」為 TODO
- **Where**：同上
- **下一步**：跟使用者對齊本場主角真實目標後填入

### 問題 3：場景索引中 `S-01-03` 與 `S-01-03a` 命名衝突
- **Where**：`/06_a_場景索引.md`
- **下一步**：依 O7 規則確認 a 變體是否獨立場景，必要時改 ID

**整體下一步：** 處理上述 3 項後重跑 `/dialogue-write S-01-03`
```

**規則：**

- 標題前置「— N 項問題」讓使用者知道規模
- 每問題保留 Where + 下一步兩欄（What/Why 在標題與彙整段已說）
- 末尾加「整體下一步」收束

## 8.5 不寫日誌 / debug 資訊給使用者

**規則：使用者看到的是 Markdown，不是 console。**

- 不顯示 stack trace
- 不顯示 error code（如 `ERR_404`）
- 不顯示內部 enum 鍵（如 `pipeline_state: TASK_REVIEW`），改為人類可讀詞（「任務包已升 REVIEW」）
- 若 skill 需要 debug 紀錄，寫入 log 檔（`_design/<phase>_review_log.md` 或 `.protocol_version.phase_log`），**不**印在 chat

**例外：** 使用者主動跑 `--verbose` 或 `--debug` 旗標時，可附技術細節（但本 spec 不規範此模式的具體輸出，由各 skill SKILL.md 自行定義）。

---

# 9. [NEEDS_SCHEMA_SUPPORT] 三類拆分清單（v0.3 重構）

對應 UX-16 + D-046 #6 + CODEX C-17。

**v0.2 → v0.3 結構變更：** v0.2 §9 把 33 項 NS 全部混在一起當作「DF schema 議題」回饋資料格式 specialist。CODEX C-17 識出問題：很多項實際上是 **parser service / frontend adapter / upstream algorithm**，不屬 DF schema 本身。將這些都丟給 DF specialist 會：

1. DF owner 被要求承擔不屬於 schema 的 runtime / API 設計
2. master 難以判斷哪些真要改 SPEC §5

v0.3 依 D-046 #6 拍板把 NS-1~NS-33 重分**三類**：

| 類別 | Owner | 數量 | 對應 spec |
|---|---|---|---|
| **§9.1 Schema 類** | 資料格式 specialist | 22 項 | DATA_FORMAT_SPEC.md |
| **§9.2 Query / API / Adapter 類** | parser service / frontend adapter（A.0 / `_tools/frontend/server.py`） | 9 項 | ARCHITECTURE.md + 本 §11.8 |
| **§9.3 Upstream Algorithm 類** | 上下游 specialist | 2 項 | UPSTREAM_DOWNSTREAM_SPEC.md |

**Resolved 標記：** v0.3 中 RESOLVED 項對應 D-037~D-046 拍板。標 ✓ RESOLVED 的，DF / UD / master 已給答案；標 △ PARTIAL 的，方向定但細節未填；標 ✗ PENDING 的待後續解決。

依 INTEGRATION_CONTRACTS §2.3 禁區：本 spec 仍**不擅自決定** schema enum / 欄位名 / 路徑等資料層細節。

## 9.1 Schema 類（22 項）— 交資料格式 specialist

DF schema 直接欄位 / 結構 / 命名規則。Owner = `DATA_FORMAT_SPEC.md`。

### 9.1.1 A-\* 美術資產 schema（4 項，多數 RESOLVED）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-1 | A-\* entity 命名規則 + KEY 結構（如 `A-portrait-<角色>-<表情>`）| §2.2 / §11.2.4 / §11.3.5 / §11.1.6a | ✓ **RESOLVED**（D-044 7 subtype + DF §5 預留 reserved） |
| NS-3 | A-\* metadata 欄位（名稱、所屬角色、表情標籤）| §2.2 / §11.1.6a.1 | △ PARTIAL（D-044 confirms 7 subtype；具體欄位 schema 由 DF §5 補 subtype registry） |
| NS-4 | A-\* 跟 C-\* cross-reference 語法 | §11.2.4 Required Context | △ PARTIAL（D-037 `dialogue_keys.<KEY>.portrait/bgm/sfx` Map shape 對齊；A-\* entity → dialogue 反向反查由 DF §5 / §9 補） |
| — | A-\* source of truth = `10_art_assets/` | §11.1.6a / §11.7.5 | ✓ **RESOLVED**（D-041） |

### 9.1.2 i18n KEY schema（4 項，多數 RESOLVED）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-5 | i18n KEY 在 markdown source 內標記方式 | §6.1 / §11.3.4 行首 KEY 顯示 | ✓ **RESOLVED**（D-037 — `dialogue_keys` frontmatter Map shape + 內文 `<!-- KEY: ... -->` comment 為可讀提示） |
| NS-6 | KEY 命名規則細節（`dlg.<ch>.<s>.<line>`）| §11.3.4 / §11.3.5 | ✓ **RESOLVED**（D-022 / D-037 — KEY 命名規則 + 自動產預設 + alias 機制） |
| NS-7 | KEY alias mapping 內部表現結構 | §11.3.5 details pane | ✓ **RESOLVED**（D-037 — `dialogue_keys.<KEY>.aliases: List[str]` 在 Map shape 內） |
| NS-8 | KEY 跟 SPEC §5.2 frontmatter 對齊 | §3.2 整合檔 frontmatter | ✓ **RESOLVED**（D-037 Map shape + D-039 records[] 含 dialogue_line record_type） |

### 9.1.3 可擴充 entity 類型 + qa_type schema（2 項，全 RESOLVED）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-9 | user-defined entity type registry schema | §11.0.7 / §11.4.3 | ✓ **RESOLVED**（DF Phase 3 §7 — Template/Instance YAML + reserved_prefixes） |
| NS-10 | qa_type 可擴充 list schema | §11.4.3 / §6 | ✓ **RESOLVED**（DF Phase 3 §8 — Template 含 8 core qa_type + user_extensions + 00_p 接點） |

### 9.1.4 JSON 中介格式 + phase_log schema（3 項，全 RESOLVED）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-12 | JSON 中介格式具體欄位 | §3 / §11.8.3 / §11.6.11 | ✓ **RESOLVED**（D-039 — DF `manifest + records[]` 為權威；UD 六區降為 derived adapter view） |
| NS-13 | phase_log 新增 import_source 欄位 | §11.5 LOCKED 守門 Z2 candidate α | ✓ **RESOLVED**（D-042 全收 5 新欄位含 import_source） |
| NS-14 | trust-level (agent_assisted / external_llm) frontmatter 結構 | §11.5.3 | △ PARTIAL（D-042 phase_log 5 欄位含；trust-level 限上游 `/create-*` 由 C-08 / D-038 細化） |

### 9.1.5 多版本 / source_dialogues / base_dialogue（2 項，全 RESOLVED）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-16 | SPEC §5.2.3 source_dialogues 欄位語義 | §11.3.3 N=4 Z1 並排 | ✓ **RESOLVED**（D-042 — `source_dialogues` 維持鎖定「僅 --converge v02」；SINGLE_ITER lineage 用**新 `base_dialogue` 欄位**，不重用 source_dialogues） |
| NS-17 | 版本獨立 frontmatter（trial vs convergence pipeline_state） | §11.3.3 每欄標頭 | △ PARTIAL（每版本獨立 frontmatter 是現有設計，D-037 + D-042 不衝突；具體 schema 由 DF §3 / §4 補） |

### 9.1.6 詞彙與資訊揭露 frontmatter（2 項）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-18 | 「本場可用 / 禁用 / 慎用詞彙」markdown 標記方式 | §11.2.4「4. 世界詞彙與禁用詞」 | ✗ PENDING（任務包 frontmatter 欄位由 DF Phase 4 補；建議欄位 `scene_vocab_allowed / forbidden / cautious`） |
| NS-19 | 「本場應揭露 / 必須保密」資訊標記方式 | §11.2.4「5. 資訊揭露控制」 | ✗ PENDING（同上；建議欄位 `info_reveal_required / info_reveal_blocked`） |

### 9.1.7 mtime / 衝突偵測 schema（3 項）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-22 | mtime 在 markdown source / server 端的權威記錄方式 | §11.7.5 / §11.5.8 | △ PARTIAL（建議：disk fstat 為 server-side 權威；前端 baseline 記憶體 cache；D-040 Save guard 多一道 Step 3 LOCKED header check）|
| NS-23 | content-hash 升級備案 | §11.7.5 | ✗ PENDING（DF 可加 frontmatter `content_hash` 欄位或留 server runtime 計算；v0.3 範圍仍採 mtime） |
| NS-24 | freshness 欄位是否動態維護 | §3.2 整合檔 frontmatter / §3.5 stale 偵測 | ✗ PENDING（建議 view 整合檔 frontmatter `freshness: ok\|stale`，由 `/export-*` 寫 / `/check-gaps` 偵測；具體 schema 由 DF Phase 4 補） |

### 9.1.8 Template / Instance / multi-project schema（3 項）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-26 | Template / Instance 跨 repo cross-reference 機制 | §11.9.2 Harness Preview | ✗ PENDING（DF Phase 4 + 整合 master plan） |
| NS-27 | Instance 微調紀錄結構（00_b 作品專屬 LOCK 欄位） | §11.9.2 / §5.2.1 A.10 gate | ✗ PENDING（DF Phase 4） |
| NS-28 | multi-project schema（未來擴充） | §11.9.1 Workspace Home | ✗ PENDING（後期，現 single-project repo） |

### 9.1.9 09_e final-gating schema（v0.3 新增，C-16 / D-046 #5）

| # | 議題 | 出現位置 | v0.3 狀態 |
|---|---|---|---|
| NS-NEW-1 | 09_e 定稿變更紀錄段落格式（LOCKED → DEPRECATED 降級條目） | §11.5.3 Z2 candidate α 引導文字 | ✗ PENDING（UPS-UX-37 對應；由上下游 specialist 在 §3.6.3 / §3.6.6 細化；前端引導必對齊最終格式） |

### 9.1.10 §9.1 彙整

**Schema 類共 22 項：** NS-1, NS-3~9, NS-10, NS-12, NS-13, NS-14, NS-16, NS-17, NS-18, NS-19, NS-22, NS-23, NS-24, NS-26, NS-27, NS-28, NS-NEW-1 + 1 個 A-\* source-of-truth resolved。

**狀態分布：** ✓ RESOLVED 11 / △ PARTIAL 4 / ✗ PENDING 7。

**第四輪整合接點：** 11 個 RESOLVED 項由 DF Phase 3 + D-037~D-046 拍板覆蓋；4 個 PARTIAL 待 DF Phase 4 細節；7 個 PENDING 進 §10 master 裁決或 DF Phase 4。

---

## 9.2 Query / API / Adapter 類（9 項）— 交 parser service / frontend adapter

**不屬 DF schema 本身**，而是 runtime / API 設計。Owner = `ARCHITECTURE.md` + 本 spec §11.8 `_tools/frontend/server.py`。

| # | 議題 | 出現位置 | Owner | v0.3 狀態 |
|---|---|---|---|---|
| NS-2 | A-\* entity manifest query API（場景反查所有可用立繪 KEY） | §11.2.4 / §11.3.5 / §11.3.6 / §11.1.6a | parser service（依 D-041 從 `10_art_assets/` 讀） | △ PARTIAL（schema 已定，query API 由 §11.8.3 server endpoint 補：`GET /api/assets?scope=scene&id=S-01-03`） |
| NS-11 | A.0 parser 對未知 qa_type 驗證邏輯 | §11.4.8 fallback | A.0 parser 邏輯 | △ PARTIAL（DF §8 Template/Instance YAML 定 enum；parser 行為：未知 qa_type → 警告但通過，不拒絕） |
| NS-15 | 多版本 entity manifest query（一場景 → 版本 list） | §11.3.3 N 欄判定 | parser service + server endpoint | △ PARTIAL（schema 從 `08_dialogue_outputs/<scene_id>/` 目錄掃；server endpoint `GET /api/scenes/<id>/versions` 由 §11.8.3 補） |
| NS-20 | 跨場聲線漂移 query API | §11.2.4「6. 跨場警示」 | upstream 09_b/i query | ✗ PENDING（屬上下游 algorithm，見 §9.3） |
| NS-21 | 跨場資訊洩漏 query API | 同上 | upstream 09_d/i query | ✗ PENDING（屬上下游 algorithm，見 §9.3） |
| NS-25 | 多分頁同編 edit-lock 機制 | §11.7.7 | server-side advisory lock | ✗ PENDING（v0.3 容許不強制；server 端可實作 client_session_id 註冊；見 §11.7.7） |
| NS-29 | server API JSON shape vs frontmatter mapping | §11.8.3 server API | frontend adapter | △ PARTIAL（D-039 records[] 為主 schema；UD 六區 derived view 由 adapter 算；前端 endpoint shape 由 §11.8.3 補） |
| NS-30 | 場景行查 query API（依 i18n KEY 找跨版本 line content） | §11.3.5 details pane「版本對照」 | parser service + server endpoint | △ PARTIAL（schema 從 dialogue_keys Map 反查；server endpoint `GET /api/scenes/<id>/keys/<key>/lines` 由 §11.8.3 補） |
| NS-31 | 全域 search index | §11.4.2 fuzzy 搜尋 | server-side full-text index 或前端 lunr.js | ✗ PENDING（個人工具，v0.3 容許 client-side full-scan fallback；large repo 才升級 index） |

**§9.2 彙整：** 9 項全部不屬 DF schema 本身。

**第四輪整合接點：**
- ARCHITECTURE.md 補 parser service / frontend server API contracts（含 NS-2/11/15/29/30/31）
- 上下游 specialist 補 NS-20/21 algorithm
- 本 spec §11.7.7 / §11.8.3 已標 advisory lock 容許不強制

---

## 9.3 Upstream Algorithm 類（2 項）— 交上下游 specialist

**屬上游 algorithm**，不是 schema 或 API。Owner = `UPSTREAM_DOWNSTREAM_SPEC.md`。

| # | 議題 | 出現位置 | Owner | v0.3 狀態 |
|---|---|---|---|---|
| NS-32 | 9 議題 per character 進度 query | UPS-UX-10 對應（§7.8.3） / §11.1.5 | UD §1.2.4 算法 | ✗ PENDING（UD Phase 2 §1.2 + UPS-UX-10 對應；前端從 query API 讀，algorithm 屬 UD） |
| NS-33 | 11 議題 per world 進度 query | UPS-UX-7 對應 / §11.1.5 | UD §1.1.4 算法 | ✗ PENDING（UD Phase 2 §1.1 + UPS-UX-7 對應；algorithm 屬 UD） |

（補 NS-20 / NS-21 跨場 query 屬本類別交叉 — 結算在 §9.2 標 PENDING，algorithm 細節由本類解。）

**§9.3 彙整：** 2 項屬上下游 algorithm 設計。前端 UI 只負責「呈現結果」，不負責計算邏輯。

---

## 9.4 三類拆分後 v0.3 彙整

| 類別 | 數量 | RESOLVED | PARTIAL | PENDING |
|---|---|---|---|---|
| §9.1 Schema | 22 | 11 | 4 | 7 |
| §9.2 Query/API/Adapter | 9 | 0 | 5 | 4 |
| §9.3 Upstream Algorithm | 2 | 0 | 0 | 2 |
| **總計** | **33** | **11** | **9** | **13** |

**v0.2 → v0.3 結構修正紀錄：**
- v0.2 NS-1~NS-33 全部混在 9.1~9.10 子節下作為「DF schema 議題」
- v0.3 拆三類 + 補 NS-NEW-1（C-16 / D-046 #5 新增）
- v0.2 中分類錯位的（混進 DF 的 query/API/algorithm）有 NS-2 / NS-11 / NS-15 / NS-20 / NS-21 / NS-25 / NS-29 / NS-30 / NS-31 / NS-32 / NS-33 共 11 項，v0.3 移到 §9.2 / §9.3
- v0.3 中 11 項 RESOLVED 來自 D-022 / D-037 / D-039 / D-041 / D-042 / DF Phase 3 §7+§8 拍板覆蓋

**禁區（依 INTEGRATION_CONTRACTS §2.3）：**
- 本 spec **不擅自決定** schema enum / 欄位名 / 路徑等資料層細節
- 本 spec **僅描述需要 schema 支援的呈現點**，不指定如何實作 schema
- 三類拆分後 owner 清楚，UX **不**為 §9.2 / §9.3 細節背書

依 D-018 #2/#3/#5 partial supersede 後的精神（D-022 / D-026 / D-027），可擴充性是核心需求，schema 不應再 LOCKED。

---

---

# 10. 需 master 裁決問題清單

對應 UX-17 任務。彙整本 spec v0.2 撰寫過程中發現的需 master 第四輪整合裁決的議題。每項標：背景、UX 角度判斷、需 master 裁決的具體點。

## 10.1 多 medium 輸出形式

**背景：** §1.5 v0.1 已將「多 medium 輸出形式」列入 §10。v0.2 partial supersede 後 L2 已有 HTML web UI，但跨 medium（chat / HTML / PDF / etc.）的設計仍未完整。

**UX 角度判斷：** 本 spec v0.2 涵蓋 L1 純 Markdown + L2 HTML + L3 純 Markdown 三個 form factor。其他 medium（PDF / EPUB / Notion 等）超出 v0.2 scope。

**需 master 裁決：**
1. v0.2 後是否將 multi-medium 列入 v0.3 範圍
2. 如要納入，先 PDF 還是 EPUB
3. 跟 Bucket #3 D-024 「JSON + MD 固定雙吐」是否衝突（單一固定中介格式 vs 多 medium）

## 10.2 `/view/README.md` 自動生成的時機

**背景：** §3.6 / §7.2 將 `/view/README.md` 列為 user 累積 ≥1 份 view 後**手動**建立。

**UX 角度判斷：** 自動生成有兩種候選：
- (a) `/export-*` 第一次跑時自動生 README skeleton
- (b) 提供 `/build-view-index` skill 主動跑

兩者都改變 SPEC §14 skill 清單；依 D-031 「本輪不新增 skill」可能衝突。

**需 master 裁決：**
1. v0.2 維持手動 OK 嗎？
2. 如未來加自動生成，是否新增 `/build-view-index` skill（需推翻 D-031）

## 10.3 UPS-UX-38 retcon 紀錄與 UPS-UX-44 依賴樹狀圖 — v0.2 不做的確認

**背景：** §7.8.8 + §7.8.10 標兩項 UPSTREAM marker「v0.2 不做」：
- UPS-UX-38：retcon 紀錄在 09_e 特殊呈現 — 不做因 D-018 #1 retcon 不採
- UPS-UX-44：影響範圍評估視覺化（樹狀圖）— 不做因 Bucket #3 F8 不做

**UX 角度判斷：** 兩項都是「scope 縮減」結果，跟 Bucket 拍板對齊。

**需 master 裁決：**
1. 第四輪整合時確認這 2 項「不做」OK 嗎
2. 若未來開新議題討論 retcon / F8 → 升 UX_SPEC 新版本

## 10.4 Glossary 13 術語具體文字內容

**背景：** §11.9.3 列出 13 術語清單但「具體文字內容 [BLOCKED:UPSTREAM_DOWNSTREAM]」。

**UX 角度判斷：** 13 術語的「定義文字」必須跟 SPEC §5.1 + §5.2 enum 對齊；UX 不擅自寫定義文字。

**需 master 裁決：**
1. 13 術語定義文字由誰寫（上下游 specialist / UX specialist / master 自寫）
2. 第四輪整合時是否補完文字 → 存到 `_tools/frontend/static/assets/glossary.json`

## 10.5 L3 export 觸發方式（P-030）

**背景：** P-030 在 DECISIONS_LOG §6.6.5 列出，由「上下游 specialist + UX specialist」共同處理。本 spec §3 + §11.1.7 已假設「user 手動跑 `/export-*` skill」+ 「前端按鈕複製指令」。

**UX 角度判斷：** 三種觸發方式都不衝突：
- (a) CLI / agent 對話跑 `/export-*` skill — L1
- (b) 前端按鈕 → 複製 `/export-*` 指令到剪貼簿 — L2，依 D-029 α
- (c) 前端按鈕直接跑 server-side CLI script — **本 spec 拒絕**（違反 D-029 α 完全分離）

**需 master 裁決：**
1. v0.2 採 (a) + (b) 兩條路徑 OK 嗎
2. (c) 路徑是否未來允許（user 信賴自動化）— 若允許，需重評 D-029 α 精神

## 10.6 Z1 混合並排對 source_dialogues 欄位的需求

**背景：** §11.3.3 Z1 拍板情境（v02 + v01A/B/C 並排 sanity check）需要從 v02 反查 v01A/B/C 路徑。NS-16 已標 [NEEDS_SCHEMA_SUPPORT]。

**UX 角度判斷：** SPEC §5.2.3 `source_dialogues` 欄位若不存在或粒度不足，Z1 並排會做不到。

**需 master 裁決：**
1. SPEC §5.2.3 是否已有 `source_dialogues` 欄位
2. 若有但粒度不足（如只記 ID 不記具體路徑） → 補欄位細節
3. 若無 → 補欄位 + 升 SPEC 一個 minor 版本

## 10.7 前端 build / framework 選擇

**背景：** §11.8.1 列「FastAPI vs http.server」「無 framework vs Vite」候選但未終拍。

**UX 角度判斷：** v0.2 留漸進選項是合理（個人工具不需要前期過度設計）。

**需 master 裁決：**
1. 第一次實作時定哪個 baseline（建議 FastAPI + 無 framework）
2. 跟 user 確認 python / node 版本

## 10.8 UPS-UX-29 多版本生成進度條 — L1 純 Markdown 受限

**背景：** UPS-UX-29 要求「多版本生成進度條」。L2 §11.3.3 版本標頭已涵蓋。L1 純 Markdown chat 中**做不到 dynamic progress bar**（agent chat 是逐 token 流式輸出，無 live update）。

**UX 角度判斷：** L1 唯一替代呈現是「結束後印靜態進度條」（如 `[已完成 v01A] [已完成 v01B] [跑 v01C 中...]`），這跟「進度條」精神有落差。

**需 master 裁決：**
1. L1 純 Markdown 是否能接受「靜態階段進度顯示」當作 UPS-UX-29 對應
2. 若不接受 → 升 §10 補設計 streaming 呈現方式

## 10.9 UPS-UX-52 frontmatter 編輯介面 — 不在前端編

**背景：** UPS-UX-52 要求「frontmatter 編輯介面」。本 spec §11.5.3 已拍板「前端不直接編 frontmatter，走外部編輯器」（Z2 candidate α）。

**UX 角度判斷：** 為對齊 D-029 α + SPEC §16 文件狀態升級限制（人類控狀態機），不在前端做 frontmatter 編輯介面是合理。

**需 master 裁決：**
1. UPS-UX-52 接受「走外部編輯器手動改」這條對應方案 OK 嗎
2. 若不接受 → 需重新設計前端 frontmatter editor（含 LOCKED 守門）

## 10.10 跨 specialist 對 LOCKED → DEPRECATED 降級流的對齊

**背景：** §11.5.3 Z2 candidate α 引導文字提到「09_e 紀錄降級理由」、「frontmatter 加降級理由 / 降級日期 / 降級人」三欄位。NS-13 已標需資料格式 specialist 對齊。

**UX 角度判斷：** 降級流跨資料格式（frontmatter 欄位） + 上下游（09_e 紀錄結構） + UX（引導文字內容）三 specialist 共同職責。

**需 master 裁決：**
1. 第四輪整合時將降級流端到端定義
2. 含 frontmatter 欄位（資料格式）+ 09_e 結構（上下游）+ 前端引導文字（UX）
3. 三者必須一致

## 10.11 彙整 + v0.3 D-037~D-046 拍板對照

**v0.3 變更：** 第四輪整合對話已拍板 D-037~D-046（DECISIONS_LOG.md §6.7），原 §10.1~§10.10 多項已 RESOLVED。

### 10.11.1 v0.2 → v0.3 RESOLVED 對照表

| §10.x 議題 | v0.3 處置 | 依據 |
|---|---|---|
| §10.1 多 medium 輸出形式 | **PARTIAL → Phase B+ POST endpoint 已在 §11.6.11.5 lifecycle 排路線**（D-038 附帶第 2 項）；其他 medium（PDF/EPUB）仍 v0.3 不採 | D-038 + L3_EXPORT_PROMPT_SCHEMA §4 |
| §10.2 `/view/README.md` 自動生成時機 | **PENDING**（v0.3 不變更，沿用「手動建立」）| 待 §10.2 後續處理 |
| §10.3 UPS-UX-38 retcon / UPS-UX-44 依賴樹狀圖 | **CONFIRMED**「v0.2 不做」決定持續到 v0.3 | D-018 #1 + Bucket #3 F8 不變 |
| §10.4 Glossary 13 術語具體文字 | **PENDING**（v0.3 不變更）| 待後續 SPEC §5.1 對齊 |
| §10.5 L3 export 觸發方式（P-030） | ✓ **RESOLVED**：採 A1 prompt + CC/CODEX | D-038 + L3_EXPORT_PROMPT_SCHEMA |
| §10.6 Z1 混合並排對 `source_dialogues` 欄位 | ✓ **RESOLVED**：`source_dialogues` 維持鎖定「僅 --converge v02」；SINGLE_ITER 用**新 `base_dialogue` 欄位** | D-042 |
| §10.7 前端 build / framework 選擇 | **PENDING**（v0.3 維持漸進選項；FastAPI + 無 framework + JSDoc + signal state 為建議 baseline）| 第一次實作時定 |
| §10.8 UPS-UX-29 多版本生成進度條 L1 受限 | **PENDING**（v0.3 L1 維持「結束後印靜態進度條」）| 沿用 v0.2 處理 |
| §10.9 UPS-UX-52 frontmatter 編輯介面 — 不在前端編 | ✓ **RESOLVED**：對齊 D-046 #5 + Z2 candidate α；frontmatter 編輯走外部編輯器 | D-046 #5 |
| §10.10 跨 specialist 對 LOCKED → DEPRECATED 降級流的對齊 | ✓ **RESOLVED**（部分）：D-046 #5 + C-16 / O-03 — UX patch §11.5.3 刪三 frontmatter 欄位；降級紀錄全進 09_e（NS-NEW-1 仍 PENDING 待 UD §3.6.3 細化） | D-046 #5 + UPS-UX-37 |

### 10.11.2 v0.3 新增 / 仍 PENDING 議題

| 議題 | 狀態 | 依據 |
|---|---|---|
| 09_e final-gating 段落 schema（NS-NEW-1，§9.1.9） | **PENDING** | UPS-UX-37 + D-046 #5 — 待上下游 specialist 在 §3.6.3 / §3.6.6 細化 |
| UD §12 改寫對齊 D-038（移除 server-side CLI 假設） | **PENDING** | D-038 / C-03 — UD specialist 主修；本 spec §7.9.5 / §11.6.11 已對齊但 UD 文檔層需補 |
| Phase B+ POST endpoint 推送方式（D-038 附帶第 2 項）| **計畫中** | D-038 + L3_EXPORT_PROMPT_SCHEMA §4 — Phase A.0 clipboard 為 v0.3 範圍，Phase B+ 啟用 |

### 10.11.3 整合排序建議（v0.3 修訂）

- 高優先級（v0.3 已 RESOLVED，僅需第四輪整合時把 D-037~D-046 promote 進 SPEC / ARCHITECTURE / TASKS）：§10.3 / §10.5 / §10.6 / §10.9
- 中優先級（v0.3 PARTIAL，待 PROMPT_SCHEMA / DF Phase 4 + 後續細化）：§10.1 / §10.10
- 低優先級（仍 PENDING，可延後）：§10.2 / §10.4 / §10.7 / §10.8

---

# 11. HTML 前端工具完整 UX 設計（L2 form factor）

## 11.0 章節導論 / Scope and Ground Rules

### 11.0.1 適用範圍

本章節規範 **Layer 2 — 前端工具（HTML web UI）** 的完整 UX 設計。對應 REQUIREMENTS_LOCK §2 三層架構中的 L2，與 §0-§8 規範的 L1（agent 對話 + Markdown source）+ L3（`/export-*` 寫 `view/<entity>.md`）並列。

依 D-030 partial supersede + §1.4.1 form factor 分工，**本章節容許並要求使用 GUI 元件**（button / form / modal / dropdown / hover / theme toggle / hash routing / localStorage 等），但仍受跨 L1/L2/L3 一致的橫切規範拘束（見 §1.4.3 + §11.0.4）。

### 11.0.2 起點文件

本章節**不從零畫**。設計起點為既有 Narrative Workspace Prototype Round 2.1：

- `_design/refactor_reference/UI_UX_SPEC.md`（prototype 自身 631 行規格，**細節層權威**）
- `_design/refactor_reference/narrative_workspace_prototype_v2.1.html`（2297 行 self-contained HTML 實作）
- `_design/UX_PROTOTYPE_ANALYSIS.md` v0.1（prototype 拆解 + 平移 / 調整 / 拒絕分類 + §9 設計起點 + §10 deliverable map）

UX_PROTOTYPE_ANALYSIS §4 已把 prototype 元件分三類：🟢 可直接平移 / 🟡 需調整後平移 / 🔴 拒絕。本章節各子節（§11.1~§11.9）對應 UX_PROTOTYPE_ANALYSIS §9 / §10。

### 11.0.3 雙頁架構（D-035）

D-035 拍板 **Cockpit + 獨立 Editor 雙頁面**，解決 UI_UX_SPEC §12 #4/#7「Scene Detail = cockpit, Dialogue Draft Preview 必須 read-only」 vs Bucket #3 F7「直接點台詞編輯」的表面衝突：

```
┌─────────────────────────────────────────────────────────────────┐
│ Scene Detail（cockpit, read-only）— §11.2                       │
│ 主欄：Scene Readiness / Required Context / Dialogue Preview /   │
│       Beat Outline / QA 摘要                                     │
│ 側欄：Active QA / HD / Canon Δ / Quick Actions / 進入編輯入口     │
└─────────────────────────────────────────────────────────────────┘
                          ↓ Quick Action「進入編輯」
┌─────────────────────────────────────────────────────────────────┐
│ Scene Editor（D-035 新頁面）— §11.3 + §11.5                     │
│ 中央 N 欄並排（F3）：v01A / v01B / v01C / v02 自適應顯示        │
│  + 行級 metadata icon → details pane                            │
│  + 浮動 Required Context 抽屜                                    │
│  + 手動 Save + diff preview modal                               │
│  + LOCKED 場景級守門在入口處擋                                    │
└─────────────────────────────────────────────────────────────────┘
```

### 11.0.4 §11 必須遵守的橫切規範

依 §1.4.3 + 三守則 G1/G2/G3，下列規範**§11 各子節設計時不得違反**：

| 規範 | 對 §11 的具體影響 |
|---|---|
| **G1 badge 不單獨呈現** | 任何 status badge 必須搭配 checklist / 計數 / next fix；§11.1 HERO 區、§11.2 Scene Readiness Panel、§11.4 facet filter 都遵守 |
| **G2 流程視覺化僅閱讀順序** | §11.1 模組狀態總覽 + §11.2 Required Context 6 子分區 + §11.5 LOCKED 守門訊息都明示「閱讀順序用，不代表強制執行步驟」 |
| **G3 UX grouping 不是資料層必要單位** | §11.3 三欄並排 + §11.4 chapter grouping 都不假設「每場必有 beat」「每份角色必有弧線段」；mock_data 結構**絕不**照搬為 schema 提案 |
| **D-029 (α) 完全分離** | 前端跟 agent 完全分離；所有 agent action（`/dialogue-write` / `/qa` / `/create-*` / LOCKED 降級等）由通用「複製指令」按鈕引導切外部 chat，前端絕不主動執行 agent；通用元件 spec 見 §11.6 |
| **D-029 (c) 手動 Save** | §11.3 / §11.5 / §11.7 的編輯操作明確需要 user 按 Save 才寫回 .md；無自動 save / draft 自動同步 |
| **中文主 + 英文 sub** | 全部標籤、按鈕、區塊標題遵守，例如「進入編輯 / Enter Editor」、「下一步 / Next Actions」、「卡點 / Blockers」 |
| **下一步永遠在最前** | §11.1 HERO 順序「下一步建議 → 卡點 → 場景就緒度」；§11.2 Scene Detail Quick Actions 區放在 user 視線可第一眼掃到處 |
| **錯誤訊息四件套** | §11.3 Save 失敗 / §11.5 LOCKED 守門訊息 / §11.7 衝突 modal 都用 What / Where / Why / How to fix 四欄結構 |
| **Suggested actions 純列舉**（§11 例外見 §1.4.3） | QA finding modal 內「建議下一步」維持純列舉文字；「複製指令」按鈕是 user 主動切外部 chat 的合法 trigger，**不是**「Suggested actions 變按鈕」 |

### 11.0.5 三類 Fidelity 規則

UX_PROTOTYPE_ANALYSIS §4.3 拒絕 prototype 的「Mock action alert + disabled button + tooltip 三層混用」做法。我們的 fidelity 統一規則：

| 操作類型 | Fidelity | 實作 |
|---|---|---|
| **read-only 顯示**（看 Scene Detail / Project Dashboard / QA 報告等） | **真資料** | 前端從 markdown source 動態讀（FastAPI / http.server endpoint） |
| **寫操作**（Scene Editor Save / 註解修改等） | **真寫** | 前端按鈕 → 本地 server API → 寫回 .md 檔；含 diff preview modal + mtime checksum 衝突偵測（§11.7） |
| **Agent action**（跑 `/dialogue-write` / `/qa` / `/create-*` / LOCKED 降級等） | **複製指令** | 通用「複製指令」按鈕（§11.6）→ 剪貼簿 → user 切外部 chat 貼上去跑 |

**不採用 prototype 的：**
- `alert("功能即將啟用")` 假按鈕
- `disabled` button + tooltip「等之後啟用」（這暗示按鈕未來會自動執行，違反 D-029 α）
- Mock fidelity 三層混用（路由真做 / modal 真做 / 元件 alert）

### 11.0.6 §11 子節索引

| 子節 | 內容 | 對應 UX_PROTOTYPE_ANALYSIS §10 |
|---|---|---|
| §11.1 | F1 Project Dashboard（平移 + A 路徑「複製指令」按鈕） | §10 row 1 |
| §11.2 | F2 Scene Queue + Scene Detail (cockpit, read-only) | §10 row 2 |
| §11.3 | **F3 Scene Editor 三欄並排（新頁，D-035）** | §10 row 3 |
| §11.4 | F6 搜尋 + 篩選 facet | §10 row 4 |
| §11.5 | F7 編輯 + LOCKED 守門 + Detail→Editor 導航 | §10 row 5 |
| §11.6 | 通用「複製指令」按鈕 component spec | §10 row 6（升格為通用元件） |
| §11.7 | 多場景並行 + 編輯衝突偵測 | §10 row 7 |
| §11.8 | Build / package / 啟動規格 | §10 row 8 |
| §11.9 | 4 個保留元件對齊（Workspace Home / Harness / Glossary / Theme toggle） | §10 row「額外」 |

### 11.0.7 與資料格式 specialist 的邊界

依 UX_PROTOTYPE_ANALYSIS §7.4 警告 + G3 守則，**UX specialist 在 §11 設計時絕不照搬 prototype 的 `mock_data` shape 為 schema 提案**。

下列在本章節中若有設計需求但屬資料層責任者，一律以 `[NEEDS_SCHEMA_SUPPORT]` 標記，並收進 §9 給資料格式 specialist 第二輪：

- 行級 i18n KEY 在 markdown 內的具體標記方式（§11.3 details pane 顯示 i18n KEY metadata 需要這個）
- A-\* 立繪 KEY 的 entity manifest 與 query API（§11.2 Required Context A-\* 顯示需要）
- pipeline_state 的可枚舉清單（§11.4 facet filter 維度需要）
- 多版本（v01A/B/C/v02）的 entity manifest（§11.3 N 欄並排需要知道版本有幾個）
- mtime / content-hash 在 markdown source 的存放方式（§11.7 衝突偵測需要）

具體清單見 §9。

### 11.0.8 與上下游 specialist 的邊界

下列在本章節有設計需求但屬上下游 algorithm 責任者，以 `[BLOCKED:UPSTREAM_DOWNSTREAM]` 標記：

- 前端「複製指令」按鈕複製的 prompt 內容（agent 端怎麼吃這個 context）— `[BLOCKED:UPSTREAM_DOWNSTREAM]`
- `/dialogue-write --single-iter` 的多版本管理 algorithm 影響 §11.3 N 欄顯示策略 — `[BLOCKED:UPSTREAM_DOWNSTREAM]`
- LOCKED → DEPRECATED 降級的引導文字內容（§11.5 Z2 candidate α）需要上下游確認 09_e 降級紀錄欄位 — `[BLOCKED:UPSTREAM_DOWNSTREAM]`
- L3 export 的前端入口按鈕複製哪個指令（P-030）— `[BLOCKED:UPSTREAM_DOWNSTREAM]`

---

## 11.1 F1 Project Dashboard / 全局看板

對應 Bucket #3 必要功能 F1。起點 = prototype Project Dashboard Round 2 重排後的 7 段順序（UX_PROTOTYPE_ANALYSIS §4.1 平移類）+ D-034 A 路徑「複製指令」按鈕（§4.2 調整類）+ §10.3 「上半資訊過載」review queue 處理。

### 11.1.1 頁面結構 / 7 段順序

依「下一步永遠在最前」原則（§1.4.3），自上而下：

```
┌─────────────────────────────────────────────────────────────────┐
│ 頁首 / Header                                                    │
│  - 專案名稱 + breadcrumb：專案首頁 / Dashboard                   │
│  - Light/Dark mode toggle（§11.9）                              │
│  - Glossary 入口（§11.9）                                        │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.2 HERO：下一步建議 / Next Actions                          │
│  - 3-5 條祈使句卡片，每張卡含「複製指令」按鈕（§11.6）            │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.3 HERO：卡點 / Blockers                                    │
│  - 紅色 badge 卡 + 阻塞描述 + 解除路徑（祈使句）                  │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.4 場景就緒度區 / Scene Readiness Overview                  │
│  - 整體完成度進度條 + 分階段細分 + 跳轉 Scene Queue 入口          │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.5 模組狀態總覽 / Module Status                             │
│  - 8 階段 Production Loop 各模組狀態行                           │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.6 三欄區 / Tri-column Snapshot                             │
│  - 左欄：待人類裁決 HD / 中欄：QA pending / 右欄：Canon Δ pending │
├─────────────────────────────────────────────────────────────────┤
│ §11.1.7 模組導航 / Module Navigation                             │
│  - Project repo 主目錄連結 + view/ 整合檔連結 + 工具入口          │
├─────────────────────────────────────────────────────────────────┤
│ 頁尾 / Footer                                                    │
│  - 最後 refresh 時間 + 手動 refresh 按鈕                         │
└─────────────────────────────────────────────────────────────────┘
```

§10.3 review queue 處理「上半資訊過載」：HERO 兩段（§11.1.2 + §11.1.3）採**緊湊卡片** + **每段最多 5 條**規則。超過 5 條時自動降階到 §11.1.5 模組狀態區，HERO 只放最高優先級項。

### 11.1.2 HERO：下一步建議 / Next Actions

依 §1.4.3 「下一步永遠在最前」 + 「Next Fix 白話祈使句」：

**Layout：** 卡片陣列（≤ 5 張），每張：

```
┌───────────────────────────────────────────────┐
│ ▎下一步 / Next Action                          │
│                                                 │
│ 跑 /create-world 完成世界觀第一輪              │
│                                                 │
│ 為什麼：W-rules 缺漏 14/27 項                  │
│                                                 │
│ [📋 複製 /create-world 指令]  [跳轉到相關檔]   │
└───────────────────────────────────────────────┘
```

**欄位：**
- 主標題：祈使句（不含「應該」「可能」「考慮」等模糊詞）
- 為什麼：一行說明此 next action 對應的具體缺口
- 複製指令按鈕：通用元件（§11.6），複製指令 + 已有 context 摘要到剪貼簿
- 跳轉連結：跳到 §11.7 多分頁工作流的相關檔頁

**A 路徑入口（D-034）：** 當 next action 對應 `/create-world` / `/create-character` / `/create-outline` / `/create-detailed-outline` / `/create-scene-task` 5 個 A 路徑 skill 時，卡片右下「複製指令」按鈕**必出現**，按鈕 label 動態顯示為「📋 複製 /create-world 指令」之類。

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 「next action 推薦邏輯」由上下游 specialist 設計（純展示 raw status vs 工具自動推薦），前端只負責顯示。

### 11.1.3 HERO：卡點 / Blockers

**Layout：** 縱向卡片堆，每張紅底 + ⚠ icon：

```
┌───────────────────────────────────────────────┐
│ ⚠ 卡點 / Blocker                                │
│                                                 │
│ 場景 S-01-03 無法跑 /dialogue-write             │
│                                                 │
│ Where：/07_scene_tasks/CH01_S03_台詞任務包.md   │
│ Why：核心欄位「出場角色聲線卡引用」為 TODO       │
│ How：補齊聲線卡引用（從 /03_characters/main/...) │
│                                                 │
│ [跳轉到該任務包]                                │
└───────────────────────────────────────────────┘
```

**欄位：** 採 §8.1 錯誤訊息四件套（What / Where / Why / How to fix）。

**空狀態（§8.3）：**

```
*目前無卡點 — 所有實體已通過先決條件檢查。可考慮跑 /scene-task 啟動下一場 dialogue 生產。*
```

斜體 + 灰調，跟正式卡點區隔。

**G1 守則對齊：** 紅色 ⚠ badge 必搭配四件套清單；不允許「⚠ 3 卡點」只顯示數字。

### 11.1.4 場景就緒度區 / Scene Readiness Overview

**Layout：** 上方整體進度條 + 下方分階段細分。

```
場景就緒度 / Scene Readiness — 整體 58% (15/26 場)

DRAFT     ████████░░░░░░░░░░░░  8 場
REVIEW    ██████░░░░░░░░░░░░░░  6 場
LOCKED    ░░░░░░░░░░░░░░░░░░░░  1 場
DEPRECATED  ░░░░░░░░░░░░░░░░░░  0 場
（未啟動）  ████████████░░░░░░░░  11 場

[→ 進入 Scene Queue]
```

**G1 守則對齊：** 整體 58% 進度條 + 分階段細分 + 「未啟動」明示，**不只**單一進度條。

**G2 守則對齊：** 階段順序旁註 `*階段順序為閱讀用，不代表必須走完一階段才能進下一階段*`。

### 11.1.5 模組狀態總覽 / Module Status

**Layout：** 表格，8 階段一階段一行，依 Production Loop 順序：

| 階段 / Stage | 模組 / Module | 狀態 / Status | 細項 / Detail | 動作 / Action |
|---|---|---|---|---|
| A 對話建立 / Authoring | W / V / C / R / P / CH / S | ~ Authoring | W 14/27 / V 8/15 ... | [跳轉 §11.7 對應檔] / [複製指令] |
| B 拆解任務 / Task Breakdown | /07_scene_tasks/* | ~ Authoring | 11 任務包 DRAFT、5 REVIEW | [跳轉 Scene Queue] |
| C 試寫 / Trial Drafting | /08_dialogue_outputs/CH*_S*/v01* | ~ Drafting | 6 場 trial 完成 | [跳轉場景] |
| D 收斂 / Convergence | /08_dialogue_outputs/CH*_S*/v02 | ✗ Pending | 0 場 v02 | [複製 /dialogue-write 指令] |
| E QA | /09_qa_reports/* | ~ Pending | 8/9 模板可用 | [跳轉 QA 報告] |
| F 人類裁決 / Human Decision | /09_e_定稿變更紀錄.md | ✓ Idle | 0 待裁決 | — |
| G Canon Δ | /09_d_*.md（Canon Delta 紀錄） | ✓ Idle | 0 待回流 | — |
| H Export | /view/* | ~ Stale | 3 份 view stale | [複製 /export-* 指令] |

**G1 守則對齊：** 每行「狀態 + 細項 + 動作」三層，**狀態 badge 不獨立呈現**。

**G3 守則對齊：** 「Production Loop 順序」旁註 `*生產循環順序為閱讀用，不代表強制執行步驟*`（§1.4.3）。

### 11.1.6 三欄區 / Tri-column Snapshot

依 prototype 平移 + G3 守則「不假設每場必有 X」精神：

```
┌──────────────────┬──────────────────┬──────────────────┐
│ 待人類裁決 / HD   │ QA pending       │ Canon Δ pending  │
│                  │                  │                  │
│ • 場景 S-01-03   │ • 09_a AI 味      │ • C-反派B 弧線   │
│   破格保留決定    │   待跑 3 場       │   待回流 W       │
│ • C-NPC 重命名   │ • 09_g 節奏感     │                  │
│   合併 vs 新建    │   待跑 全 chapter │                  │
│                  │                  │                  │
│ [跳轉 09_e]      │ [跳轉 QA 報告]   │ [跳轉 09_d]      │
└──────────────────┴──────────────────┴──────────────────┘
```

每欄空狀態（§8.3）：

```
*目前無待裁決事項。下一波預期出現在 D.3.5 收斂 gate 或 QA_FAILED 後的破格保留判定。*
```

### 11.1.6a A-\* Asset Panel — 美術資產獨立進度（v0.3 新增，D-045 / C-14）

依 D-045 拍板：**A-\* 完成度不納入 narrative `/status` 整體完成度**（理由：大綱寫到一半時繪師才開工很正常，不該卡台詞 FINAL）。前端 Dashboard 仍要有獨立 panel 顯示 A-\* 進度，方便監控資產進度，**但跟 §11.1.4 場景就緒度 + §11.1.5 模組狀態完全分離**。

**Layout — 7 subtype 分組（依 D-044 拍板 7 種 subtype）：**

```
┌─────────────────────────────────────────────────────────────────┐
│ A-\* 美術資產進度 / Asset Panel                                  │
│ ─── 獨立於 narrative 完成度（D-045）─── 整體 35%（87/247）       │
│                                                                  │
│ ┌─ portrait（立繪）────────────────────────┐                    │
│ │ ✓ 完成 12  ◐ 製作中 4  ○ 未啟動 8  ✗ 缺  3│  27 KEYs (52%)   │
│ │ 角色覆蓋：5/7 主要角色已有預設立繪           │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ bg（背景）──────────────────────────────┐                    │
│ │ ✓ 完成 8  ◐ 製作中 2  ○ 未啟動 15        │  25 KEYs (40%)    │
│ │ 場景覆蓋：8/26 場景已綁定背景               │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ cg（事件圖）────────────────────────────┐                    │
│ │ ✓ 完成 3  ○ 未啟動 12                    │  15 KEYs (20%)    │
│ │ 高潮場景覆蓋：1/4 已綁定 CG                 │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ sfx（音效）─────────────────────────────┐                    │
│ │ ✓ 完成 24  ◐ 製作中 5  ○ 未啟動 36        │  65 KEYs (37%)    │
│ │ 場景覆蓋：12/26 場景已綁定 ≥ 1 個 SFX       │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ bgm（背景音樂）─────────────────────────┐                    │
│ │ ✓ 完成 6  ○ 未啟動 8                     │  14 KEYs (43%)    │
│ │ 章節覆蓋：3/3 章節已綁定主題曲              │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ voice（配音）───────────────────────────┐                    │
│ │ ✗ 未啟動 全部                            │  0/85 KEYs (0%)   │
│ │ * 配音預設 Phase D 後啟動                  │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ ┌─ ui（UI 文案）───────────────────────────┐                    │
│ │ ✓ 完成 6  ◐ 製作中 0  ○ 未啟動 0          │  6 KEYs (100%)    │
│ │ * UI 文案完成（不可擴；I-\* UI-\* 留接口）   │                    │
│ └────────────────────────────────────────────┘                  │
│                                                                  │
│ [→ 進入 Asset Registry 完整視圖]                                 │
│ [📤 開啟 Export panel — 含 A-\*（依 scope）]                     │
└─────────────────────────────────────────────────────────────────┘
```

**7 subtype 列表（對齊 D-044）：** `portrait` / `bg` / `cg` / `sfx` / `bgm` / `voice` / `ui`。`icon` / `effect` 不採（合併進 `ui` / `cg`）。

**位置：** Project Dashboard 中，**在 §11.1.6 三欄區與 §11.1.7 模組導航之間**。理由：三欄區是 narrative 卡點 / pending；本 panel 是平行的 asset 維度資訊，跟 narrative 並列但概念分離。

**互動：**
- 點任一 subtype 區塊 → 展開到 §11.1.6a.1 詳細子表（每個 KEY 一行 + state）
- 點「進入 Asset Registry 完整視圖」 → 跳新分頁開 `10_art_assets/` 索引頁（A-\* registry source of truth，依 D-041 / C-05）
- 點「開啟 Export panel」 → 跳 §11.6.11 Export panel（依 D-038 / §11.6.11）

**狀態符號：** 沿用 §1.2 B 級調整 — `✓` / `◐` / `○` / `✗`。

**G1 守則：** 整體 35% badge + 7 subtype 各自細項 + 「角色覆蓋」/「場景覆蓋」清單 — **三層**並列，不只顯示百分比。

**G3 守則：** 7 subtype 分組是 UX 排版骨架；資料層仍以 `10_art_assets/` 目錄 + 各 entity 的 metadata 為權威（D-041）。

#### 11.1.6a.1 子表 — A-\* KEY 詳細展開

點某 subtype 展開後：

```
┌─ portrait subtype 詳細 ──────────────────────────────────┐
│                                                            │
│ KEY                                  Owner   State  覆蓋   │
│ ────────────────────────────────────────────────────────  │
│ A-portrait-主角A-default            C-主角A  ✓ 完成  18 場 │
│ A-portrait-主角A-angry              C-主角A  ✓ 完成  6 場  │
│ A-portrait-主角A-surprise           C-主角A  ◐ 製作  3 場  │
│ A-portrait-主角A-cry                C-主角A  ○ 未啟  0 場  │
│ A-portrait-反派B-smirk              C-反派B  ✓ 完成  4 場  │
│ A-portrait-反派B-default            C-反派B  ○ 未啟  0 場  │
│ ⚠ A-portrait-NPC村民甲-default     C-NPC村民甲 ✗ 缺檔 2 場 │
│ ...                                                       │
│                                                            │
│ [→ 進入 /10_art_assets/portrait/]                          │
│ [📤 Export 此 subtype（依 §11.6.11）]                      │
└────────────────────────────────────────────────────────────┘
```

**Owner 欄位：** 對齊 D-044 + UD §13 — A-\* 可 owner 為 `C-*` / `S-*` / `CH-*` / `global`。

**State：** `✓ 完成` / `◐ 製作中` / `○ 未啟動` / `✗ 缺檔` 四桶（v0.4 master 第四輪 CC-01 校正 — State 從 `10_art_assets/<subtype>/<group>.md` 內 `art_metadata[*].status` 反查；採 DF subtype/group canonical 模型；原 `<key>/metadata.md` 寫法 supersede）。

**覆蓋：** 動態反查「該 KEY 被多少場景引用」（從 `dialogue_keys.<KEY>.portrait/bgm/sfx` 反查；D-037 對齊）。

**⚠ 缺檔警示（UPS-UX-70 對應；v0.4 master 第四輪 CC-01 校正）：** 若某 KEY 被引用但 `10_art_assets/<subtype>/<group>.md` 內 `art_metadata` block 不含對應 asset_id，badge 變紅 ⚠ + 顯示「✗ 缺檔」+ 引用場景數。

**[NEEDS_SCHEMA_SUPPORT]** — 「KEY 被多少場景引用」反查 query API — 收 §9 query-API 類。

#### 11.1.6a.2 跟 §11.1.4 場景就緒度 + §11.1.5 模組狀態的分工

| 維度 | §11.1.4/5 narrative | §11.1.6a A-\* asset |
|---|---|---|
| 對象 | W/V/C/R/P/CH/S（7 entity types） | A-\* 美術資產（7 subtype） |
| 完成度 | 「整體 58%」**包含**所有 narrative entity | 「整體 35%」**僅** A-\* — 跟 narrative 完全獨立 |
| 影響 FINAL gate | ✓ — REVIEW gate (A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5) 全部要求 | **✗**（D-045）— A-\* 缺漏不阻塞 dialogue FINAL |
| Cross-ref | dialogue 引用立繪 KEY 時用 §11.2.4 Required Context | 完整反查在 §11.1.6a.1 |
| Source of truth | source markdown frontmatter / 內文 | `10_art_assets/` registry（D-041） |

> **（D-075 doc-sync 指標）：** 上表「W/V/C/R/P/CH/S（7 entity types）」為 v1.0 基底敘事 entity 集；`W-style`（D-055）/ `ORG`（D-071/D-074）為後加 opt-in 型別，present 時亦計入 narrative 完成度。entity 型別權威見 `entity_type_registry`（現 11 種 core）；本表計數為歷史框架，不重寫。

**重點：** §11.1.6a 是「監控用」panel，不擋 narrative 進度。User 可以 dialogue FINAL 在沒立繪的情況下 — 立繪由繪師後續補（D-045 設計理由）。

#### 11.1.6a.3 對齊 D-NNN 拍板

| 拍板 | §11.1.6a 對應 |
|---|---|
| D-044 | 7 subtype 分組（portrait/bg/cg/sfx/bgm/voice/ui） |
| D-045 | 不納入 narrative `/status` + 獨立 panel |
| D-041 | source of truth = `10_art_assets/` |
| D-037 | 「覆蓋」反查依賴 `dialogue_keys.<KEY>.portrait/bgm/sfx` Map shape |
| C-13 | 完整解決 A-\* subtype 範圍 |
| C-14 | 完整解決 A-\* 是否進 `/status` |

### 11.1.7 模組導航 / Module Navigation

**Layout：** 兩列 grid：

```
┌────────────────────────────────┬─────────────────────────────────┐
│ Source 目錄 / Source Tree       │ View 整合檔 / View Files          │
│                                 │                                  │
│ 📁 /01_world/                  │ 📄 /view/世界觀.md                │
│ 📁 /02_voice_bible/            │ 📄 /view/角色_主角A.md            │
│ 📁 /03_characters/             │ 📄 /view/角色_反派B.md            │
│ 📁 /04_relationships/          │ 📄 /view/細綱.md                 │
│ 📁 /05_outline/                │ ⚠ /view/角色_主角A.md（stale）   │
│ 📁 /06_detailed_outline/       │                                  │
│ 📁 /07_scene_tasks/            │                                  │
│ 📁 /08_dialogue_outputs/       │                                  │
│ 📁 /09_qa_reports/             │                                  │
│ 📁 /10_art_assets/             │                                  │
│                                 │                                  │
│ [→ 進入 Scene Queue]            │ [📤 開啟 Export panel]           │
└────────────────────────────────┴─────────────────────────────────┘
```

`⚠ stale` 偵測依 §7.7 規則（source mtime > view 匯出時間）。

**v0.3 變更：**
- 新增 `📁 /10_art_assets/` 目錄入口（對齊 D-041 A-\* source of truth）
- 「[複製 /export-* 指令]」按鈕**移除**（依 D-046 #4 + C-12 — `/export-dialogue` skill 不存在），改為「[📤 開啟 Export panel]」（依 D-038 A1 + §11.6.11）

### 11.1.8 §10.3 review queue 對應的設計決策

| §10.3 議題 | 本子節處置 |
|---|---|
| Project Dashboard 上半資訊過載 | HERO 兩段每段限 ≤ 5 條，超過降階到 §11.1.5；§11.1.4 進度條折疊未啟動類 |
| HD blocking vs non-blocking 用 danger/warning badge 反邏輯 | 統一規則：紅 ⚠ = 卡點（HERO §11.1.3）；黃 ! = 提醒（§11.1.5 / §11.1.6）；不混用 |
| Future module 灰階是否清楚（dark mode） | §11.5 / §11.9 dark mode 子節覆蓋；模組狀態總覽 §11.1.5「未啟動」狀態用淡灰 + 「（未啟動）」明示文字標籤，**不靠純色階** |

### 11.1.9 互動規範

- **點卡片內主標題** → 不做任何事（純文字）
- **點「跳轉」連結** → 開新分頁載入對應檔（§11.7 多分頁工作流）
- **點「複製指令」按鈕** → 複製到剪貼簿 + 顯示 toast「已複製到剪貼簿，請切到 Claude Code / Cowork 貼上」（§11.6 通用元件）
- **點手動 refresh 按鈕** → re-fetch markdown source + 重渲染（不全頁 reload）
- **點 dark mode toggle** → §11.9 規範

### 11.1.10 RWD

- ≥ 1280px：完整三欄區（§11.1.6）並排
- 920px - 1280px：三欄區折成 1 欄縱向
- < 920px：所有區塊單欄縱向；模組狀態表格水平 scroll
- < 768px：顯示 hint「Dashboard 建議桌面瀏覽器使用」+ 提供精簡版（僅 HERO + 場景就緒度）

---

## 11.2 F2 Scene Queue + Scene Detail (cockpit, read-only)

對應 Bucket #3 必要功能 F2「場景切換 + 自動 context 裝載」。起點 = prototype Scene Queue + Scene Detail (main + side) 雙層導航（UX_PROTOTYPE_ANALYSIS §9.2）。Scene Detail 維持 **read-only cockpit**（D-035 + UI_UX_SPEC §12 #4/#7 critical preserve），編輯入口跳轉到 §11.3 Scene Editor。

本子節只規範 Scene Queue 的 layout + Scene Detail 的 cockpit 結構；搜尋 / 篩選 facet 細節見 §11.4，編輯入口導航流見 §11.5。

### 11.2.1 Scene Queue 頁面結構

```
┌─────────────────────────────────────────────────────────────────┐
│ 頁首：breadcrumb 專案首頁 / Scene Queue | 搜尋框 | 篩選 facet    │
├─────────────────────────────────────────────────────────────────┤
│ Filter Summary：目前 11/26 場（依 篩選：DRAFT + Ch01）           │
├─────────────────────────────────────────────────────────────────┤
│ Chapter Group：第一章 / Chapter 1                                │
│  ┌────────────────────────────────────────────────────┐         │
│  │ S-01-01 — 主角覺醒                                  │         │
│  │ DRAFT / Trial Drafting / 卡點 1                    │         │
│  │ Required Context 完整度：5/6  / QA 0/3              │         │
│  │ Next Fix：審 3 條 DRAFT 後升 REVIEW                 │         │
│  │ [→ 進入場景 cockpit]                                │         │
│  └────────────────────────────────────────────────────┘         │
│  ┌────────────────────────────────────────────────────┐         │
│  │ S-01-02 — ...                                       │         │
│  └────────────────────────────────────────────────────┘         │
│ Chapter Group：第二章 / Chapter 2                                │
│  ...                                                              │
└─────────────────────────────────────────────────────────────────┘
```

**Scene card 欄位：**
- 場景 ID + 簡名（主角覺醒）
- pipeline_state badge + 階段 badge + 卡點數字（G1 守則：badge 必搭配清單）
- Required Context 完整度 X/6（§11.2.4 6 子分區）+ QA 完成 Y/N
- Next Fix 祈使句（§1.4.3）
- 跳轉按鈕「→ 進入場景 cockpit」

**Chapter Group：** prototype 平移 + G3 守則（不假設每場必有 chapter — 無 chapter 場景歸到「未分章 / Unassigned」分組）。

**互動：** 點卡片任何位置 → 跳到 Scene Detail（不再 expand-in-place）。card 內按鈕 → §11.7 多分頁打開。

### 11.2.2 Scene Detail (cockpit) 頁面結構 — main + side 雙欄

依 prototype Round 2 production cockpit 平移 + D-035 read-only 性質：

```
┌─────────────────────────────────────────────────────────────────┐
│ 頁首：breadcrumb 專案首頁 / Scene Queue / S-01-03 主角質問        │
│       | [→ 進入編輯 / Enter Editor]（§11.5 LOCKED 守門入口）      │
├──────────────────────────────────────┬──────────────────────────┤
│ 主欄 / Main                          │ 側欄 / Side (sticky)     │
│                                       │                          │
│ §11.2.3 Scene Readiness Panel        │ §11.2.5 Active QA        │
│  (badge + 10 項 checklist + Next Fix) │  - QA finding 摘要清單   │
│                                       │  - 點開 → modal（§11.2.7）│
│ §11.2.4 Required Context (6 子分區)  │                          │
│  1. Bible refs (W/V)                  │ §11.2.6 Active HD        │
│  2. Characters (C)                    │  - HD pending 清單       │
│  3. Relationships (R)                 │  - 點開 → modal          │
│  4. World vocab (W terms / forbidden) │                          │
│  5. Info reveal control (P)           │ §11.2.6 Active Canon Δ   │
│  6. Warnings (cross-scene / leak)     │  - Δ pending 清單        │
│                                       │  - 點開 → modal          │
│ §11.2.7 Beat / Outline Preview        │                          │
│  (read-only 細綱片段)                 │ §11.2.8 Quick Actions    │
│                                       │  - [→ 進入編輯]          │
│ §11.2.9 Dialogue Draft Preview        │  - [複製 /qa 指令]       │
│  (read-only 多版本)                   │  - [複製 /dialogue-write]│
│                                       │  - [跳轉任務包]          │
│ §11.2.10 QA Findings 摘要             │                          │
│  (點開 → §11.2.7 modal)               │                          │
└──────────────────────────────────────┴──────────────────────────┘
```

**Sticky side：** 側欄滾動時固定，main 區內容 scroll。

### 11.2.3 Scene Readiness Panel

依 §1.2 「Scene Readiness 10 項 checklist」調整版 — 本專案實際對應 6 個 REVIEW gate（§5）+ Scene 層次補項。

```
場景就緒度 / Scene Readiness — DRAFT （4/10 完成）

✓ 任務包核心欄位齊全
✓ 出場角色聲線卡引用完整
✓ 出場立繪 KEY 標註
✗ 角色真實目標欄位 — 為 TODO
~ Beat 結構建議：3 拍
✗ Dialogue Draft v01A 待產
✗ Dialogue Draft v01B 待產
✗ Dialogue Draft v01C 待產
— Convergence v02 等 v01A/B/C 完成
— QA 5 模板待跑

下一步 / Next Fix：補齊「角色真實目標」欄位後跑 /dialogue-write S-01-03
        [📋 複製 /dialogue-write S-01-03 指令]
```

**G1 守則：** badge `DRAFT` + 10 項 checklist + Next Fix 三層。

**Status symbol（§1.2 B 級調整）：** `✓` / `~` / `✗` / `⚠` / `?` / `—` 純文字符號。

### 11.2.4 Required Context — 6 子分區（prototype 核心保留）

依 prototype §12 #5 critical preserve + UX_PROTOTYPE_ANALYSIS §4.1。對齊 Bucket #1 i18n KEY + A-\* 立繪：

```
Required Context / 必要 Context

─ 1. Bible 引用 / Bible References ──────────────────
  W-rules：
    • 世界規則 §2.3「異能上限」 — [/01_world/01_a_世界觀總覽.md#世界規則-world-rules]
    • 世界語言 §1.1「禁用詞表」 — [/01_world/01_b_世界語言規格.md]
  V-vocab：
    • 詞彙「靈魂之路」 — [/01_world/01_b_世界語言規格.md#詞彙系統]

─ 2. 出場角色 / Characters ──────────────────────────
  • C-主角A — [/03_characters/main/主角A_聲線卡.md]
    立繪 KEY：A-portrait-主角A-default / A-portrait-主角A-angry
  • C-反派B — [/03_characters/main/反派B_聲線卡.md]
    立繪 KEY：A-portrait-反派B-smirk

─ 3. 角色關係 / Relationships ────────────────────────
  • 主角A ↔ 反派B：對手 / 過去師生情誼 — [/04_relationships/...]

─ 4. 世界詞彙與禁用詞 / World Vocab & Forbidden Terms
  • 本場可用：靈魂之路 / 異能 / 試煉
  • 本場禁用：魔法 / 法術 / 異界
  • 慎用：神 / 魂魄（每場 ≤ 1 次）

─ 5. 資訊揭露控制 / Info Reveal Control ───────────────
  • 本場應揭露：主角異能上限為「3 階」
  • 本場必須保密：反派B 是主角的舊師父（留到第 7 場）

─ 6. 跨場警示 / Cross-scene Warnings ──────────────────
  • 跨場聲線漂移：主角A 在 S-01-02 用過「我懂了」，本場避免重複
  • 跨場資訊洩漏：S-01-02 已揭露「異能存在」，本場不必再揭
```

**A-\* 立繪 KEY 顯示（D-023 對齊）：** 在「2. 出場角色」每個角色名下方列出立繪 KEY。**只顯示 KEY，不顯示實檔**（依 D-023 + REQUIREMENTS_LOCK §3.3 工具不知實檔位置）。

**[NEEDS_SCHEMA_SUPPORT]** — A-\* entity manifest 的 query API（怎麼從場景反查所有可用立繪 KEY）— 收 §9。

**[NEEDS_SCHEMA_SUPPORT]** — 「本場可用 / 禁用 / 慎用詞彙」的 markdown source 標記方式 — 收 §9。

**G3 守則：** 6 子分區是**閱讀骨架，不是資料層必要單位**。子分區若全空也照常顯示（empty state 文案，§8.3），不假設每場必填滿 6 區。

### 11.2.5 Active QA findings 摘要（側欄）

依 §6 QA finding 5 欄位（severity / title / affected / summary / suggested actions），側欄顯示**摘要**，點開到 modal 顯示完整。

```
Active QA Findings (3)

⚠ [HIGH] 對話張力不足
  Beat 2 / Line 4 / 主角A
  反擊頻率 0/3，預期 ≥ 1
  [展開]

! [MEDIUM] 跨場聲線漂移
  Beat 3 / Line 7 / 反派B
  跟 S-01-02 用詞風格差距 0.32
  [展開]

! [MEDIUM] AI 味 ...
  [展開]
```

**[展開] 點 → §11.2.10 中央 modal**（依 UI_UX_SPEC §12 #8 critical preserve「QA / HD / Canon Δ 用中央 modal」）。

**空狀態：**
```
*目前無 QA finding — 本場 QA 全綠或尚未跑 QA*
[📋 複製 /qa S-01-03 指令]
```

### 11.2.6 Active HD / Canon Δ（側欄）

同 §11.2.5 結構 — 摘要 + [展開] modal。HD modal 內列出 ⓐ 待裁決問題 ⓑ 候選選項 ⓒ 跳轉 09_e 連結。

**注意（依 §1.4.3 「Suggested actions 純列舉」+ D-029 α）：** modal 內**不**提供「採用候選 A」按鈕；改成「複製 candidate A 拍板紀錄到 09_e」按鈕（§11.6 通用元件） — user 切外部 chat 編 09_e。

### 11.2.7 Beat / Outline Preview

依 §6 與細綱 cross-ref。read-only Markdown 渲染：

```
Beat 結構 / Beat Structure（建議分 3 拍）

Beat 1：質問前（establishing）
  - 主角A 主動找反派B
  - 對峙位置：神殿廢墟

Beat 2：質問核心（confrontation）
  - 主角A 質問反派B 為何背叛
  - 反派B 揭穿主角A 的盲點

Beat 3：質問後（resolution）
  - 雙方各自離開
  - 主角A 內心動搖

*來源：[/06_detailed_outline/CH01_第一章細綱.md](/06_detailed_outline/CH01_第一章細綱.md#s-01-03)*
```

**G3 守則：** Beat 結構是「建議分 3 拍」，**不是**「本場必有 3 beat」。下方提示「依場景實際內容可加減」。

### 11.2.8 Quick Actions（側欄）

對齊 D-029 α 完全分離精神，所有 agent action 走「複製指令」按鈕（§11.6）：

```
Quick Actions

┌─────────────────────────────────────┐
│ [→ 進入編輯 / Enter Editor]         │  ← 跳 §11.3 Scene Editor
└─────────────────────────────────────┘
（如場景 LOCKED：）
┌─────────────────────────────────────┐
│ ⚠ 此場景已 LOCKED                   │
│ [📋 複製降級引導文字]                │  ← §11.5 Z2 candidate α
│ 詳見「LOCKED 守門」§11.5             │
└─────────────────────────────────────┘

─────────────────────────────────────

[📋 複製 /dialogue-write S-01-03 指令]
[📋 複製 /qa S-01-03 指令]
[📋 開啟 Export panel → 複製 Export Prompt（D-038 A1）]

─────────────────────────────────────

[跳轉任務包 → /07_scene_tasks/CH01_S03]
[跳轉 view 整合檔 → /view/場景_S-01-03]
```

**「進入編輯」按鈕的 LOCKED 守門：** 詳見 §11.5。

### 11.2.9 Dialogue Draft Preview（read-only）

依 UI_UX_SPEC §12 #7 critical preserve「Dialogue Draft Preview 必須 read-only」。本子節維持 **read-only 單一版本預覽**（或多版本 tab 切換）；多版本**並排對比**屬於 Scene Editor 職責（§11.3）。

```
Dialogue Draft Preview / 台詞稿預覽（read-only）

[ v01A ] [ v01B ] [ v01C ] [ v02 ]   ← tab 切換
        ──────

dlg.ch01.s03.l001  主角A：「你為什麼背叛我們？」
dlg.ch01.s03.l002  反派B：「（冷笑）你還沒明白嗎？」
dlg.ch01.s03.l003  主角A：「你說啊。」
...

*來源：[/08_dialogue_outputs/CH01_S03/v01A.md](...)*

[→ 進入編輯 / Enter Editor]（觸發 §11.3 + §11.5 LOCKED 守門）
```

- 顯示 i18n KEY（dlg.\<ch\>.\<s\>.\<line\>）+ 角色 + 內容
- read-only — 不可點台詞編輯
- tab 切換不同版本
- 立繪 KEY metadata 在 §11.3 Editor 內以 details pane 顯示，不在 Scene Detail 內顯示

### 11.2.10 QA Findings 摘要 + 中央 modal

主欄底部摘要 + 點「展開」開中央 modal：

```
┌────────── QA Finding Detail Modal ──────────┐
│ ⚠ [HIGH] 對話張力不足 / Dramatic Tension Low │
│                                              │
│ Affected:                                    │
│   • Beat 2 / Line 4 / 角色：主角A            │
│   • i18n KEY: dlg.ch01.s03.l004              │
│                                              │
│ Summary:                                     │
│   反擊頻率 0/3，預期 ≥ 1。本場兩方核心衝突， │
│   主角A 在被反派B 反問後沒任何反擊台詞，     │
│   缺攻防力度。                               │
│                                              │
│ Suggested actions（閱讀建議）:               │
│   1. 在 Line 4 後補一條主角A 反擊台詞        │
│   2. 把 Line 4 從疑問句改為陳述句以反擊      │
│   3. 整段重寫 Beat 2 用「揭穿 / 反擊」結構    │
│                                              │
│ [📋 複製 /dialogue-write S-01-03 --single-iter 指令]│
│ [關閉]                                       │
└──────────────────────────────────────────────┘
```

**規則對齊：**
- 「Suggested actions」純列舉文字（§1.4.3 + §1.1）
- 點「複製 /dialogue-write --single-iter 指令」走 §11.6 通用元件（依 D-028，不新增 /iterate-dialogue skill）
- modal 自身**不**提供「採用建議」按鈕（依 D-029 α + §1.4.3 「複製指令」例外明示）
- 點「關閉」回 Scene Detail

### 11.2.11 互動規範

- Scene Queue 點卡片 → 跳 Scene Detail（新分頁，§11.7）
- Scene Detail 點 Required Context 內 link → 跳對應 Bible / 角色檔（新分頁）
- Scene Detail 側欄 QA / HD / Canon Δ 摘要 [展開] → 中央 modal
- Scene Detail 任何主欄區塊**不可點編輯** — 編輯走「進入編輯」按鈕跳 §11.3
- 「進入編輯」按鈕在 LOCKED 場景變成 §11.5 Z2 candidate α「複製降級引導文字」

### 11.2.12 RWD

- ≥ 1280px：完整 main + side cockpit 雙欄
- 920px-1280px：side 縮為單獨折疊區，main 全寬
- < 920px：side 摺到 main 下方
- < 768px：hint「Scene Detail 建議桌面瀏覽器使用」+ 提供 Required Context + Scene Readiness 兩區精簡版

依 UX_PROTOTYPE_ANALYSIS §4.2 與 §7.2，個人桌面使用 — 保留現有 @920px 切換為主。

---

## 11.3 F3 Scene Editor 三欄並排 — 新頁面（D-035）

對應 Bucket #3 必要功能 F3「多版本並排對比」+ F7「直接點台詞編輯」的編輯區。**本頁是 D-035 新拍板的獨立頁面，prototype 完全沒有**，UX_PROTOTYPE_ANALYSIS §9.3 標為「**新設計**」。

本子節規範 layout + 行級 metadata + 浮動側抽屜；Save 流 + LOCKED 守門入口 + 導航流見 §11.5；衝突偵測見 §11.7。

### 11.3.1 進入路徑

唯一進入路徑：**從 Scene Detail (§11.2) 側欄「Quick Actions」的「進入編輯 / Enter Editor」按鈕跳轉**。

URL 約定（hash routing 沿用 prototype 慣例）：
- Scene Detail：`#/scene/S-01-03`
- Scene Editor：`#/scene/S-01-03/edit`

不允許直連 Scene Editor（除非透過 §11.7 多分頁打開 — 但 URL 仍走 hash）。

**LOCKED 守門：** 進入 Editor 前的 LOCKED 檢查在 Scene Detail 側欄處理（§11.5）。Editor 頁本身假設「已通過 LOCKED 守門」。

### 11.3.2 頁面整體 layout

```
┌─────────────────────────────────────────────────────────────────┐
│ 頁首 / Header                                                    │
│  breadcrumb：專案首頁 / Scene Queue / S-01-03 / 編輯              │
│  [← 返回 Scene Detail]  [💾 Save 全部]  [📂 Required Context 抽屜]│
├─────────────────────────────────────────────────────────────────┤
│ §11.3.3 版本標頭列 / Version Headers                             │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐    │
│  │ v01A        │ v01B        │ v01C        │ v02         │    │
│  │ TRIAL/DRAFT │ TRIAL/DRAFT │ TRIAL/DRAFT │ CONVERG./...│    │
│  │ [📋 跑 QA]  │ [📋 跑 QA]  │ [📋 跑 QA]  │ [📋 跑 QA]  │    │
│  └─────────────┴─────────────┴─────────────┴─────────────┘    │
├─────────────────────────────────────────────────────────────────┤
│ §11.3.4 中央 N 欄並排（可編輯 textarea + 行級 metadata icon）     │
│                                                                  │
│  Column 1 (v01A)         Column 2 (v01B)    Column 3 (v01C)    │
│  🔑 主角A：「你為什麼...」 🔑 主角A：「為什麼... 🔑 主角A：「為什麼  │
│  🔑 反派B：「（冷笑）...」 🔑 反派B：「（笑）...」 🔑 反派B：「（冷笑│
│  ...                       ...                  ...              │
│                                                                  │
│  ─── 點 🔑 → details pane 在右側滑入（§11.3.5）                  │
├─────────────────────────────────────────────────────────────────┤
│ §11.3.6 浮動 Required Context 抽屜（預設關，左側 toggle 開）      │
├─────────────────────────────────────────────────────────────────┤
│ §11.3.7 底部狀態列                                               │
│  [Dirty: v01A v01B] [📋 複製 /dialogue-write 指令] [上次 Save：xx]│
└─────────────────────────────────────────────────────────────────┘
```

### 11.3.3 版本標頭列 / Version Headers

依 Q1 拍板 + Z1 補充：**N 欄自適應 + 混合 trial 版 + 收斂版**。

**N 欄判定邏輯：**
- N = 1：只有 v01A（或單 SINGLE_ITER 版）— 全寬單欄
- N = 2：v01A + v01B / 或 v01A + v02（trial + convergence 混合）
- N = 3：v01A + v01B + v01C
- N = 4（Z1 拍板情境）：v02 + v01A + v01B + v01C（收斂後 sanity check）
- N ≥ 5（極少見）：水平 scroll，不再每欄等寬

**[NEEDS_SCHEMA_SUPPORT]** — 多版本 entity manifest（場景反查所有版本）需要資料層 query API — 收 §9。

**[NEEDS_SCHEMA_SUPPORT]** — SPEC §5.2.3 `source_dialogues` 欄位的存放方式（Z1 混合並排需要從 v02 反查引用的 v01A/B/C） — 收 §9。

**每欄標頭欄位：**

```
┌──────────────────────────────────────┐
│ v01A                                  │
│ mode_tag：DRAFT_TRIAL                 │
│ pipeline_state：DIALOGUE_TRIAL         │
│ 最後修改：2026-05-15 (agent)          │
│ 行數：24                              │
│                                       │
│ [📋 跑 v01A QA 指令]                  │
│ [📋 跑 v01A iterate 指令]             │
└──────────────────────────────────────┘
```

**G1 守則：** badge（mode_tag + pipeline_state）必搭配「最後修改 + 行數」清單，**不只**顯示 badge。

**視覺區隔（Z1 混合並排所需）：**
- v01A/B/C（trial 類）：藍色邊框
- v02（convergence 類）：綠色邊框
- 不靠純色階分辨（dark mode 需可讀）：搭配文字 label `[Trial]` / `[Convergence]`

**每欄 QA 按鈕：** 依「跑 QA 按鈕 B 自決定項」拍板 — per-version 各自有「📋 複製跑 QA 指令」按鈕，**不做一鍵跑全部**。複製指令格式（[BLOCKED:UPSTREAM_DOWNSTREAM]）：

```
/qa S-01-03 --version v01A --templates 09_a,09_b,09_c,09_d,09_e,09_g,09_h,09_i
```

具體 query 參數由上下游 specialist 在 §8 SINGLE_ITER mode + QA pipeline 設計時確認。

### 11.3.4 中央 N 欄並排編輯區

每欄是**可編輯 textarea**（F7 直接編輯）。行為：

- **點 textarea 任意處** → focus 編輯（不開 details pane）
- **點 textarea 左側 🔑 icon** → 右側 details pane 滑入顯示該行 metadata（Q2 refinement）
- **textarea 內換行 = 新台詞 line**（依 markdown source line-by-line 編輯）
- **編輯時** column 標頭出現 `● dirty` 標記
- **編輯不會立刻寫回** — 等 Save（§11.3.7 / §11.5）
- **跨欄選取 / 複製貼上** 直接走瀏覽器原生支援

**每行顯示：**

```
🔑 dlg.ch01.s03.l001  主角A：「你為什麼背叛我們？」
🔑 dlg.ch01.s03.l002  反派B：「（冷笑）你還沒明白嗎？」
🔑 dlg.ch01.s03.l003  主角A：「你說啊。」
```

- 行首 i18n KEY 顯示為灰色淡字（reference 用，不可編輯）
- 編輯只動「主角A：」之後的內容
- 角色名稱「主角A：」是可編輯的 prefix（user 可改說話者）

**[NEEDS_SCHEMA_SUPPORT]** — i18n KEY 在 markdown source 內的具體標記方式（行內註解 / frontmatter / metadata block）— 收 §9。

**G3 守則：** 「行」是排版單位，不是資料層必要單位 — Editor 不假設「每場必有 N 行」「i18n KEY 必須密集連號」。

**LOCKED 守門粒度（Q3 拍板）：** 場景級 only。Editor 內**不做**行級 LOCKED 灰底 — 全場景能進 Editor 就能改每行。

### 11.3.5 行級 details pane（右側滑入）

**觸發：** 點該行行首 🔑 icon。

**Layout：** 右側滑入 panel（約 360px），不遮中央 N 欄；textarea 自動微縮。

```
┌────────────── Details: dlg.ch01.s03.l001 ──────────────┐
│                                                          │
│ i18n KEY：dlg.ch01.s03.l001                              │
│   別名 / aliases：（無）                                 │
│                                                          │
│ 說話者：C-主角A                                          │
│ 立繪 KEY：A-portrait-主角A-default                       │
│   候選：default / angry / surprise / cry                 │
│   [複製 A-portrait-主角A-angry 到剪貼簿]                 │
│                                                          │
│ Beat 歸屬：Beat 1 (建議)                                  │
│ 場景偏移：第 1 拍 第 1 句                                 │
│                                                          │
│ 跨場引用：本句首次出現「靈魂之路」詞彙                    │
│                                                          │
│ 版本對照（其他 column 同 line）：                         │
│   v01B：「為什麼你要走？」                                │
│   v01C：「為什麼你會選這條路？」                          │
│                                                          │
│ [關閉]                                                    │
└──────────────────────────────────────────────────────────┘
```

**欄位來源：**
- i18n KEY / aliases：**[NEEDS_SCHEMA_SUPPORT]** — D-022 alias mapping 內部結構未定
- 說話者 / 立繪 KEY：**[NEEDS_SCHEMA_SUPPORT]** — A-\* entity manifest
- Beat 歸屬 / 場景偏移：依 §11.2.7 read-only Beat preview，這裡反查行屬於哪個 beat
- 跨場引用：**[NEEDS_SCHEMA_SUPPORT]** — 跨場一致性 query API
- 版本對照：對應 column 同 line 對照

**互動：**
- 點「複製 A-portrait-... 到剪貼簿」 → §11.6 通用元件
- 點 i18n KEY → 高亮目前 textarea 內該行
- 點「關閉」 → 收回 pane
- 切到另一行 🔑 → pane 不關，內容換成新行

**Q2 refinement 對齊：** trigger 是 icon click 不是 row click — 避免「想編輯但意外開 metadata」誤觸（§1.4.3 守則精神）。

### 11.3.6 浮動 Required Context 抽屜（Q5 拍板）

**目的：** Editor 內 user 臨時要查 Bible refs / 角色聲線卡禁用詞時用，不必切回 Scene Detail。

**Layout：** 左側 toggle 按鈕「📂 Required Context」，點開後左側滑入抽屜（約 320px），中央 N 欄稍微右擠。

```
┌─────── Required Context ───────┐
│ ⟳ 上次同步：2026-05-18 13:42    │
│ [⟳ Refresh]                     │
│                                  │
│ 1. Bible 引用                    │
│    • W-rules §2.3「異能上限」    │
│    • V-vocab「靈魂之路」         │
│ 2. 出場角色                      │
│    • C-主角A                     │
│      立繪 KEY：A-portrait-...    │
│    • C-反派B                     │
│      立繪 KEY：A-portrait-...    │
│ 3. 角色關係                      │
│    ...                           │
│ 4. 世界詞彙 / 禁用詞              │
│    可用：靈魂之路 / 異能 ...     │
│    禁用：魔法 / 法術 / 異界      │
│ 5. 資訊揭露控制                  │
│    ...                           │
│ 6. 跨場警示                      │
│    ...                           │
│                                  │
│ [關閉抽屜]                       │
└─────────────────────────────────┘
```

**內容來源：** 同 §11.2.4 Required Context 6 子分區。read-only — 不可編輯，編輯要切外部 chat 跑 `/iterate-*`。

**Cache + Refresh 策略（Q5 拍板）：**

| 時機 | 行為 |
|---|---|
| 進入 Editor 時 | Prefetch Required Context 快取於前端 state，**不**等 user 點開抽屜才 fetch |
| User 第一次點開抽屜 | 顯示快取內容（即時） |
| User 重複點開且距上次 fetch ≤ N 秒（建議 N=300） | 顯示快取（不 refetch） |
| User 重複點開且距上次 fetch > N 秒 | 自動 refetch + 顯示「⟳ 同步中」spinner |
| User 主動點「⟳ Refresh」 | 強制 refetch |

抽屜頂部顯示「⟳ 上次同步：HH:MM」讓 user 知道資料新鮮度。

**理由（Q5 reflect）：**
- 即時讀 + 進 Editor 時 prefetch：兼顧效能與初次開啟速度
- 自動 refetch 閾值：避免 user 長時間編輯後參照已過時 context
- Refresh 按鈕：agent 在外部 chat 改 Bible 後 user 主動同步

### 11.3.7 底部狀態列 + Save 流程

**Layout：**

```
┌─────────────────────────────────────────────────────────────────┐
│ Dirty status：v01A ● v01B ●  ｜ v01C ○ v02 ○                    │
│ 上次 Save：2026-05-18 13:20  ｜ mtime 同步：通過                 │
│                                                                  │
│ [💾 Save 全部]  [📋 複製 /dialogue-write S-01-03 指令]            │
└─────────────────────────────────────────────────────────────────┘
```

**Save 流程（依 Q4 拍板 + C 自決定 mtime checksum）：**

1. User 點「💾 Save 全部」
2. 前端跳出 **diff preview modal**（§11.3.8）
3. User 在 modal 內確認 → 點「確認寫回」
4. 前端送請求到本地 server：`POST /api/scene/S-01-03/save`，body 含所有 dirty version 的 markdown + 每個檔的 client-side mtime checksum
5. Server 比對 each file 的 disk mtime checksum
   - 全部相符 → 寫檔 + 回 200 + 新 mtime
   - 任一不符 → 回 409 → 前端跳 §11.7 conflict modal
6. Save 成功後：
   - column dirty 標記清除（● → ○）
   - 「上次 Save」時間更新
   - **不**自動跳回 Scene Detail（依 D-035 §5.3 + Q4 拍板「Save 後留 Editor」— user 自己用 breadcrumb / 返回按鈕決定）

**Save 全部範圍：** 所有 dirty version 一次寫（D-029 (c) 手動 Save + git history 乾淨）。**不**做 per-version Save。

**不做：**
- 自動 save draft（依 D-029 (c)）
- 30-秒 auto save
- 離頁警告（只在有 dirty 且 user 嘗試導航時跳 confirm dialog）
- Optimistic UI（必須等 server 200 才清 dirty）

### 11.3.8 Diff Preview Modal

**Layout：** 中央 modal（依 UI_UX_SPEC §12 #8 critical preserve「modal 用中央 overlay」）。

```
┌──────── Save 前確認 / Confirm Save ────────────────────┐
│ 場景 S-01-03，要寫回以下變更：                          │
│                                                          │
│ ─── v01A（3 行修改） ────────────────────────────────  │
│   dlg.ch01.s03.l001                                      │
│   - 主角A：「你為什麼背叛我們？」                        │
│   + 主角A：「你為什麼背叛了我們？」                      │
│                                                          │
│   dlg.ch01.s03.l004                                      │
│   - 主角A：「你說啊。」                                  │
│   + 主角A：「你給我說清楚。」                            │
│                                                          │
│   dlg.ch01.s03.l007（新增行）                            │
│   + 主角A：「不要逃避。」                                │
│                                                          │
│ ─── v01B（1 行修改） ────────────────────────────────  │
│   dlg.ch01.s03.l002                                      │
│   - 反派B：「（笑）你還沒明白嗎？」                      │
│   + 反派B：「（冷笑）你還沒明白嗎？」                    │
│                                                          │
│ ─── v01C（未修改）─────────────────────────────────── │
│ ─── v02（未修改）──────────────────────────────────── │
│                                                          │
│ ┌─ Save 後動作 ─────────────────┐                       │
│ │ ☐ 寫完後自動複製 /qa 指令      │                       │
│ │   到剪貼簿                     │                       │
│ └────────────────────────────────┘                      │
│                                                          │
│ [取消]                          [確認寫回 / Confirm]     │
└──────────────────────────────────────────────────────────┘
```

**規則對齊（Q4 拍板 + i18n KEY label per segment）：**
- 紅綠對比：`-` 紅 / `+` 綠
- **每段 diff 旁標 i18n KEY**（讓 user 知道改的是哪個 KEY，未來 i18n table 同步用）
- 新增行明示「（新增行）」
- 刪除行明示「（刪除行）」
- 未修改 version 列在最後，顯示「未修改」省略 diff
- Save 後動作：可選「寫完後自動複製 /qa 指令」便利選項（**選了仍是複製到剪貼簿** — 不直接執行 agent，依 D-029 α）

**Save 失敗（如 409 衝突）：** 關 diff preview modal → 跳 §11.7 conflict modal。

### 11.3.9 互動規範總覽

| 操作 | 行為 |
|---|---|
| 點 textarea | focus 編輯 |
| 點行首 🔑 icon | 右側 details pane 滑入 |
| 點 column 標頭 [📋 跑 QA 指令] | §11.6 通用元件 — 複製到剪貼簿 |
| 點頁首 [← 返回 Scene Detail] | 若有 dirty → confirm dialog；否則直接返回 |
| 點頁首 [💾 Save 全部] | 跳 §11.3.8 diff preview modal |
| 點頁首 [📂 Required Context] | 左側抽屜 toggle |
| 點底部 [📋 複製 /dialogue-write] | §11.6 通用元件 |
| 鍵盤 Ctrl/Cmd-S | 同「Save 全部」 |
| 鍵盤 Esc | 關 details pane / 關抽屜 / 關 modal（依優先級） |

### 11.3.10 RWD（A 自決定項）

依 §11.0 A 自決定項：
- ≥ 1280px：完整 N 欄並排（N ≤ 4 各自等寬）
- 920px-1280px：**水平 scroll** N 欄（而非降為單欄）— 保留並排語意
- < 920px：仍水平 scroll；details pane 改成中央 modal
- < 768px：顯示 hint「Scene Editor 建議桌面瀏覽器使用」，提供唯讀單欄 fallback view（建議 user 切回 Scene Detail）

### 11.3.11 對齊三守則 / 拍板項回顧

| 拍板項 | §11.3 對應 |
|---|---|
| Q1 N 欄自適應（不留 placeholder） | §11.3.3 N 欄判定邏輯；不留空欄「新增此版本」誘導 |
| Z1 混合 trial+convergence 並排 | §11.3.3 N=4 情境 + 視覺區隔（藍 trial / 綠 convergence） |
| Q2 (X) details pane + icon click trigger | §11.3.5 — trigger 是 🔑 icon 不是 row click |
| Q3 場景級 LOCKED only | §11.3.4 「Editor 內**不做**行級 LOCKED」 |
| Q4 diff preview modal + i18n KEY label per segment | §11.3.8 |
| Q4 Save 後留 Editor | §11.3.7 「不自動跳回 Scene Detail」 |
| Q5 cache + refresh + auto refetch on stale | §11.3.6 抽屜策略表 |
| B per-version 跑 QA 按鈕 | §11.3.3 每欄標頭 [📋 跑 v01A QA] |
| C mtime checksum 衝突偵測 | §11.3.7 Save 流程 + §11.7 conflict modal |

### 11.3.12 跟 §11.2 Scene Detail 的職責分工（複述）

| 職責 | Scene Detail (§11.2) | Scene Editor (§11.3) |
|---|---|---|
| 看單一版本 read-only 預覽 | ✓（tab 切換多版本） | ✗（編輯態 — 不專門 read-only） |
| 看 Required Context 全文 | ✓（主欄 6 子分區） | △（抽屜，預設關） |
| 看 QA findings 完整 modal | ✓（側欄展開 → 中央 modal） | ✗（要看 QA 切回 Scene Detail） |
| 看 Beat / 細綱 preview | ✓ | ✗ |
| 看 HD / Canon Δ 列表 | ✓ | ✗ |
| **多版本並排對比** | ✗ | ✓（N 欄並排，§11.3.3） |
| **編輯台詞** | ✗ | ✓（F7 直接編輯，§11.3.4） |
| **行級 metadata 詳檢** | ✗ | ✓（details pane，§11.3.5） |
| 進入 Editor 入口 | ✓（側欄按鈕） | — |
| 跳轉外部 chat（複製指令） | ✓（多處） | ✓（標頭 + 底部） |
| LOCKED 守門展示 | ✓（§11.5 入口擋） | ✗（已過守門） |

---

## 11.4 F6 Scene Queue 搜尋 + 篩選 facet

對應 Bucket #3 必要功能 F6「快速搜尋 + 篩選」。起點 = prototype Scene Queue filter + chapter grouping（UX_PROTOTYPE_ANALYSIS §9.4）+ 補 facet 維度 + 對齊 D-027 可擴充 qa_type。

### 11.4.1 整體 layout — Scene Queue 頁面上方搜尋區

接續 §11.2.1 Scene Queue 頁面結構，頁面頂部新增搜尋 + facet 控制列：

```
┌─────────────────────────────────────────────────────────────────┐
│ Search & Filter / 搜尋與篩選                                     │
│                                                                  │
│ 🔍 [輸入 ID / 簡名 / 角色 / 詞彙...]                              │
│                                                                  │
│ Facet：                                                          │
│ ├─ Chapter ▾  [全部] [Ch01 (8)] [Ch02 (10)] [Ch03 (8)]           │
│ ├─ Pipeline State ▾  [全部] [DRAFT (8)] [REVIEW (6)] [LOCKED (1)]│
│ ├─ Mode Tag ▾  [全部] [TRIAL] [EXPERIMENT] [CONVERG] [SINGLE_ITER]│
│ ├─ Stage ▾  [全部] [Authoring] [Trial] [QA] [Final]               │
│ ├─ QA Type ▾  [全部] [09_a 8] [09_b 6] [09_g 0] ... [09_i 0]      │
│ ├─ Readiness ▾  [全部] [✓全綠] [~部分] [⚠卡點] [✗未啟動]         │
│ └─ Characters ▾  [全部] [主角A] [反派B] [NPC1]...                 │
│                                                                  │
│ [清除所有篩選]   ｜  已套用 3 個 facet — 顯示 11/26 場            │
└─────────────────────────────────────────────────────────────────┘
```

下方接 chapter grouping 場景卡列表（§11.2.1）。

### 11.4.2 搜尋輸入

**單一搜尋框** + 全文 fuzzy 搜尋。

**搜尋範圍：**
- 場景 ID（如 `S-01-03`、`01-03`）
- 場景簡名（如「主角覺醒」）
- 出場角色 ID + 名稱（如 `C-主角A`、「主角A」）
- 任務包內 frontmatter 與正文
- i18n KEY（如 `dlg.ch01`）
- 行內台詞內容（如「靈魂之路」搜尋出所有提到的場）

**互動：**
- 輸入時 debounce 300ms 才觸發 filter
- 結果分組顯示（標明匹配位置：場景 / 角色 / 行內等）
- 點搜尋結果 → 跳該 scene card / Scene Detail 對應 anchor

**清除：** 輸入框右側 `×` icon 一鍵清除。

**搜尋與 facet 互動：** 搜尋 + facet **AND 合併**（同時套用）。例如「Ch01 + DRAFT + 搜尋『靈魂』」= 第一章中 DRAFT 狀態的場景中包含「靈魂」的。

### 11.4.3 Facet 維度 — 7 維

依 prototype + Bucket #1 / #2 / #3 拍板 + D-027 可擴充 qa_type：

| Facet | 維度 | 來源 | 可擴充？ |
|---|---|---|---|
| **Chapter** | 章別（Ch01 / Ch02 / ...） + 未分章 | 場景索引 `06_a_場景索引.md` | 隨章節增長 |
| **Pipeline State** | DRAFT / REVIEW / LOCKED / DEPRECATED / 未啟動 | SPEC §16 + §5.2.4 | **不可擴充**（依 SPEC §16 LOCKED） |
| **Mode Tag** | DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / SINGLE_ITER / DIALOGUE_FINAL / META（鎖定 6 種） | SPEC §5.2.4 + D-028 | **不可擴充**（D-028 只把 mode_tag 從 5 種擴 1 種到 6 種，未解除 LOCKED；唯一可擴充的是 qa_type — 見 D-027） |
| **Stage** | Authoring / Task / Trial / Convergence / QA / Final | Production Loop（§11.1.5 模組狀態） | 隨 phase 擴充 |
| **QA Type** | 09_a~i 各 type 是否跑過 / 跑出 finding | SPEC §5.2.4 qa_type | **可擴充**（依 D-027 LOCKED 解除） |
| **Readiness** | ✓全綠 / ~部分 / ⚠卡點 / ✗未啟動 | §11.2.3 Scene Readiness | 固定 4 桶 |
| **Characters** | 出場角色（C-\*） | 任務包 frontmatter `entities` | 隨 C-\* 擴充 |

**[NEEDS_SCHEMA_SUPPORT]** — qa_type 可擴充 list 的 schema 機制（D-027）— 收 §9。前端 facet 必須能從 schema 動態列出當前可用 qa_type，不可寫死。

**[NEEDS_SCHEMA_SUPPORT]** — pipeline_state 的 enum 從哪 source 讀（如 frontmatter `狀態`）— 收 §9。

### 11.4.4 Facet 互動

**單一 facet 內：**
- 預設「全部」
- 點某選項 → 切換選中
- 多選（OR 合併）— 例如同時選 DRAFT + REVIEW

**Facet 之間：** AND 合併（如 Ch01 AND DRAFT AND 09_a 有 finding）。

**Facet 選項顯示：**
- 旁邊顯示 count（[Ch01 (8)] 表示 Ch01 有 8 場）
- count = 0 的選項仍顯示但 disabled + 灰色

**Facet 展開 / 折疊：** 預設折疊到「選了 → 顯示」收摺；點 ▾ 展開所有選項。

**清除：** 「清除所有篩選」按鈕清除全部 facet + 搜尋框。

**Persisted state：** 進入 Queue 時記住上次的 facet 選擇（用 `localStorage` 儲存最後一組 facet — 依 §11.0.1 L2 容許 localStorage）。提供「重置為預設」按鈕。

### 11.4.5 G1 守則對齊

每場 scene card 上的 badge 不單獨呈現：
- pipeline_state badge + Required Context 完整度 X/6 + QA 完成 Y/N + Next Fix 祈使句 — **四層**並列（§11.2.1）

facet 上的 count 也是 badge + 數字搭配，不是純 badge。

### 11.4.6 Empty state（無結果）

```
*目前篩選條件下無場景符合。*

可考慮：
- 清除部分 facet（如取消 Ch01 限制）
- 用 fuzzy 搜尋替代精確 ID 搜尋
- 確認場景索引 06_a_場景索引.md 是否包含目標場景
```

依 §1.4.3 + §8.3 empty state 文案規則。

### 11.4.7 篩選結果 export 入口

facet 套用後，提供「複製當前篩選結果為 ID 清單」按鈕（§11.6 通用元件）：

```
[📋 複製 11 個場景 ID（S-01-01, S-01-02, ...）到剪貼簿]
```

用途：user 切外部 chat 跑批次指令時用，例如「跑這 11 個場景的 09_g」。

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 批次跑 QA / dialogue-write 的具體 invocation 格式 — 收 §9。

### 11.4.8 對齊 D-027（QA Type 可擴充）

前端 facet 中 QA Type 維度的選項**動態從資料層讀**，不可寫死。資料格式 specialist 第二輪需要：
- 提供「當前可用 qa_type list」query API
- 提供「新增 qa_type 時前端如何同步」協議（**[NEEDS_SCHEMA_SUPPORT]**）

前端應在 fetch 失敗時 gracefully degrade：fallback 顯示 SPEC §5.2.4 的固定列表（09_a/b/c/d/e/f/g/h/i），並提示 user「QA Type 動態讀取失敗，顯示靜態 fallback」。

### 11.4.9 RWD

- ≥ 1280px：facet 橫向 7 維展開
- 920px-1280px：facet 折成 2 列
- < 920px：facet 折成「篩選」按鈕 → 點開展開 modal 含全部 facet
- < 768px：同 < 920px

---

## 11.5 F7 直接編輯 + LOCKED 守門 + Scene Detail → Editor 導航

對應 Bucket #3 必要功能 F7「直接點台詞編輯 + LOCKED 守門」。本子節對應 UX_PROTOTYPE_ANALYSIS §9.5 + UX-12b 任務（D-035 拍板拆出）。

**職責劃分（複述）：**
- Scene Editor 頁面 layout（F3 三欄並排 + F7 textarea + Save）→ §11.3（UX-12a）
- **Scene Detail → Editor 導航流 + LOCKED 守門入口 → 本子節（UX-12b）**

### 11.5.1 LOCKED 守門 — 進入 Editor 前的檢查

依 D-035 拍板 + Q3 「場景級 LOCKED only」 + Z2 candidate α，**LOCKED 守門擋在 Scene Detail 側欄「進入編輯」按鈕**，**不**在 Editor 內逐行守。

**Scene 三種 pipeline_state 對應 UX：**

| pipeline_state | Scene Detail 側欄 Quick Actions 顯示 | 點按鈕行為 |
|---|---|---|
| **DRAFT / REVIEW**（未鎖） | `[→ 進入編輯 / Enter Editor]` | 直接跳 §11.3 Scene Editor (`#/scene/<id>/edit`) |
| **LOCKED** | `⚠ 此場景已 LOCKED — 不可直接編輯`<br>`[📋 複製降級引導文字]`<br>`詳見「降級流程」（內嵌說明）` | 不跳 Editor；點按鈕複製 Z2 candidate α 引導文字到剪貼簿 |
| **DEPRECATED** | `~ 此場景已 DEPRECATED — 編輯不影響定稿`<br>`[→ 進入編輯 / Enter Editor]` | 跳 Editor；Editor 頁首加 warning banner「此場景已 DEPRECATED」 |

**[NEEDS_SCHEMA_SUPPORT]** — pipeline_state 在 markdown source 的存放方式（frontmatter `狀態`） — 收 §9。

### 11.5.2 LOCKED 場景的入口呈現

```
┌──── Scene Detail 側欄 Quick Actions（LOCKED 場景）────┐
│                                                          │
│ ⚠ 此場景已 LOCKED                                       │
│                                                          │
│ What：此場景 pipeline_state 為 LOCKED                    │
│ Where：/08_dialogue_outputs/CH01_S03/v02.md frontmatter │
│ Why：依 SPEC §16 文件狀態機規則，LOCKED 場景的台詞      │
│       不可直接編輯，必須先降級為 DEPRECATED 並紀錄理由   │
│ How to fix（降級流程，3 步）：                           │
│   1. 點下方「複製降級引導文字」按鈕                     │
│   2. 切到外部編輯器手動改 frontmatter 狀態欄位          │
│   3. 在 09_e 紀錄降級理由後重整本頁                     │
│                                                          │
│ [📋 複製降級引導文字]                                    │
│                                                          │
│ ─── 替代動作 ───                                         │
│                                                          │
│ [→ 進入 read-only 預覽]（已在當前頁）                    │
│ [跳轉 09_e 定稿變更紀錄]                                  │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

依 §1.4.3 「錯誤訊息四件套」格式 — What / Where / Why / How to fix。**重點：**
- 不用 `disabled` button + tooltip「等之後啟用」（UX_PROTOTYPE_ANALYSIS §4.3 拒絕）
- 用 「降級至 DEPRECATED 才能改」明示路徑
- 不直接執行降級操作（依 D-029 α + Z2 candidate α 拍板）

### 11.5.3 Z2 candidate α — LOCKED 降級引導文字（v0.3 修正：純 09_e 紀錄，不動 frontmatter 三欄位）

**v0.3 變更（依 D-046 #5 / C-16 / O-03）：**

v0.2 原文要求 user 在 frontmatter 補「降級理由 / 降級日期 / 降級人」三欄位。但 SPEC canonical schema **沒有這三欄**，DF 也強調「既有 frontmatter 零破壞」。前端引導**不得**指示使用者擅自加 schema 不認的欄位。

**v0.3 正解：** 降級理由 / 日期 / 操作人**全部寫到 09_e final-gating 紀錄檔內**；frontmatter **只動一個合法欄位** `狀態：LOCKED → DEPRECATED`（這個欄位本身在 SPEC §16 文件狀態機內）。

**前端按鈕複製到剪貼簿的內容（v0.3 修正版）：**

```
─── 場景 S-01-03 從 LOCKED 降級為 DEPRECATED ───

此場景目前 pipeline_state 為 LOCKED，依 SPEC §16 文件狀態機規則
不可直接編輯。請手動執行下列兩步（不新增 frontmatter 欄位）：

1. 編輯 frontmatter（外部編輯器，如 VS Code）：
   檔案：D:/劇本開發工具/08_dialogue_outputs/CH01_S03/v02.md
   只改一行：
     狀態：LOCKED  →  狀態：DEPRECATED
   不要新增「降級理由」「降級日期」「降級人」等欄位 —
   這些欄位不在 SPEC §5.2 canonical schema 內，請放到下一步的 09_e。

2. 在 09_e final-gating 紀錄檔補一條完整降級紀錄：
   檔案：D:/劇本開發工具/09_qa_reports/09_e_定稿變更紀錄.md
   附加段落：
     ## S-01-03 LOCKED → DEPRECATED 降級 / 2026-05-19
     - 場景：S-01-03（v02.md）
     - 原狀態：LOCKED
     - 新狀態：DEPRECATED
     - 降級日期：2026-05-19
     - 降級人：[user 名稱]
     - 降級理由：[具體理由，如「Bible W-rules §2.3 異能上限改為 5 階，本場 v02 暗示
                  3 階上限與新 canon 衝突」]
     - 影響：v02 不再為定稿；如要新版定稿請跑
            /dialogue-write S-01-03 --single-iter --note "依新 W-rules 重做"

3. 回到 Scene Detail 重整頁面（按 F5 或頁尾 refresh 按鈕）。
   重整後「進入編輯」按鈕應啟用。

─── 注意 ───
- 降級操作**不走 skill**（無 /deprecate-scene 之類；D-031「本輪不新增 skill」）
- frontmatter **只改 `狀態：DEPRECATED` 一行** — 不擅自加 schema 不認的欄位
- 完整降級紀錄（理由、日期、操作人、影響）全部進 09_e，由人類追溯
- 依 SPEC §16「文件狀態升級限制」原則，狀態機由人類控制
```

**對齊：**
- D-046 #5（刪除三 frontmatter 欄位，改寫 09_e）
- CODEX C-16 / O-03（前端不擅自加 schema 不認的 frontmatter）
- Z2 candidate α 拍板（純引導文字，無 skill）
- D-031「本輪不新增 skill」
- SPEC §16「文件狀態升級限制」（人類控狀態機）

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 09_e 定稿變更紀錄段落 schema 由上下游 specialist 在 §3.6.3 / §3.6.6 細化（UPS-UX-37）— 收 §9。前端按鈕複製的引導文字格式須最終對齊 09_e schema。

**動態替換：** 引導文字內的：
- `S-01-03` / `v02.md` / `CH01_S03` 等場景識別 — 由前端 fill-in
- `2026-05-19` — 當前日期由前端 fill-in
- `[user 名稱]` / `[具體理由]` — 留給 user 自己填

### 11.5.4 DEPRECATED 場景的入口呈現

DEPRECATED 場景**仍可進入 Editor**（已不影響定稿），但 Editor 頁首加 warning banner：

```
┌─ Scene Editor — S-01-03 ────────────────────────────────┐
│ ⚠ Warning：此場景已 DEPRECATED                           │
│   編輯不影響定稿。如要新版定稿，建議跑                    │
│   /dialogue-write 產新版本。                              │
│   [📋 複製 /dialogue-write S-01-03 指令]                  │
└──────────────────────────────────────────────────────────┘
```

不阻擋編輯，只警示。

### 11.5.5 Scene Detail → Editor 導航流

**入口：** 唯一進入 Scene Editor 的路徑（依 §11.3.1）：

```
Workspace Home（§11.9.1）
  → Project Dashboard（§11.1）
      → Scene Queue（§11.2.1 + §11.4）
          → Scene Detail（§11.2.2，cockpit）
              → Quick Actions 側欄「進入編輯」按鈕（§11.2.8）
                  ↓ 通過 LOCKED 守門檢查（§11.5.1）
              → Scene Editor（§11.3）
                  ↓ Save 後（§11.3.7）
              → 留在 Scene Editor（依 Q4 + D-035 §5.3）
                  ↓ user 自行決定
              → 點頁首「← 返回 Scene Detail」（§11.3.2）
                  ↓ 有 dirty 跳 confirm
              → Scene Detail
```

**不允許：**
- 從 Scene Queue 直接跳 Scene Editor（必先過 Scene Detail）
- 從 URL 直連 Scene Editor（除非透過 §11.7 多分頁打開，URL 仍走 hash）
- 從 Project Dashboard 直跳 Editor

**理由：** 強制 user「先看 cockpit context → 確認要編 → 才進編輯態」，跟 D-035 §5.2「審視 vs 編輯是不同心智狀態」對齊。

### 11.5.6 Editor 內離開時的 dirty 守門

User 在 Editor 內若有 dirty：

**離開方式 1：點「← 返回 Scene Detail」**
```
┌──────── 確認返回 / Confirm Navigation ────────┐
│ 您有未儲存的變更（v01A v01B）                  │
│                                                 │
│ 選擇下一步：                                    │
│ [儲存後返回]  [捨棄變更返回]  [取消（留 Editor）]│
└─────────────────────────────────────────────────┘
```

**離開方式 2：點 breadcrumb 任一層 / 點瀏覽器 ← / Cmd-W**
- 同上 confirm dialog
- 瀏覽器原生 `beforeunload` event 攔截

**離開方式 3：意外瀏覽器 crash / 關閉**
- **不**做 auto-recover（依 D-029 (c) 手動 Save + git history 乾淨）
- 由 user 重做 — 但 §11.7 編輯衝突偵測會確保 source 沒被破壞

### 11.5.7 LOCKED 守門 in Scene Editor — 行級不做，**Save race guard 必做**

依 Q3 「場景級 LOCKED only」拍板，Editor **內**不做**行級**守門：
- 沒有「行級 LOCKED 灰底 textarea」
- 沒有「LOCKED beat 不可編輯警告」
- Editor textarea 編輯態下假設「能進來就能改」

行級 mock_data lock 屬 UX_PROTOTYPE_ANALYSIS §4.3 拒絕類別，不在本輪 scope。

---

**但是場景級 LOCKED Save race 必須擋（v0.3 新增，對齊 D-040 / CODEX C-15 critical）：**

User 進入 Editor 時場景是 DRAFT，編輯期間外部 agent / VS Code / 另一分頁把 source 升 LOCKED 的情境**真實存在**。原 v0.2 設計把 LOCKED 守門只放在「進入 Editor 前」入口，**留下 race window 讓 Save 覆寫最新 LOCKED**，違反 SPEC §16 文件狀態機規則。

### 11.5.8 Save flow 必經 LOCKED race guard（v0.3 新增，D-040）

**對齊 D-040 拍板規格：Save flow 必須在實際寫檔前重讀最新 source header，若最新 `狀態=LOCKED` 則禁止 overwrite。**

#### 11.5.8.1 Save flow 修訂版（5 步，原 §11.3.7 流程的 race guard 增強）

```
User 點「💾 Save 全部」
   │
   ▼
Step 1：前端組 dirty diff（沿 §11.3.8 diff preview modal）
   │
   ▼
Step 2：User 在 diff preview modal 點「確認寫回」
   │
   ▼
Step 3：前端送 pre-flight 請求到本地 server：
   GET /api/scene/<id>/header  (回傳 frontmatter 最新狀態 + mtime checksum)
   │
   ├─── Step 3a：若最新 `狀態 != LOCKED`（DRAFT / REVIEW / DEPRECATED）：
   │       前端進 Step 4 正常 Save flow
   │
   └─── Step 3b：若最新 `狀態 == LOCKED`：
           前端**禁止 overwrite** → 跳 §11.5.8.2 LOCKED race modal
           → User 三選項處理 → flow 終止 / 另存 proposal / 取消
   │
   ▼
Step 4：前端送 Save 請求（含 mtime checksum，沿 §11.7.5 衝突偵測）
   │
   ▼
Step 5：Server 寫檔成功 → 200 / 衝突 → 409 → §11.7.6 conflict modal
```

**關鍵：** Step 3 是 D-040 新增的 race guard，**在 Step 4 mtime checksum 之前**先做 LOCKED 檢查。理由：
- mtime checksum 偵測「外部修改」但不分辨修改類型
- 若外部修改是「升 LOCKED」，前端不該即使 mtime 對齊也覆寫
- LOCKED race 比 mtime drift 嚴重 — 一個是內容衝突可由 user 選 reload，一個是狀態機破壞

#### 11.5.8.2 LOCKED race modal — 三選項對話框（D-040 拍板）

當 Step 3b 觸發（最新 `狀態=LOCKED`），前端跳 modal：

```
┌──── 此場景已升 LOCKED — Save 被擋下 ────────────────┐
│                                                       │
│ ⚠ 您 Editor 內的編輯**未寫回**。                       │
│                                                       │
│ What：場景 S-01-03（v02.md）在您編輯期間被外部升 LOCKED │
│ Where：/08_dialogue_outputs/CH01_S03/v02.md            │
│ Why：依 SPEC §16 + D-040 race guard，前端不得 overwrite│
│       LOCKED 場景（即使您進 Editor 時是 DRAFT）         │
│ How：請選擇下一步處理方式（您的編輯內容會保留在前端     │
│       state，不會立刻丟失）                            │
│                                                       │
│ ┌─ 三選項 ─────────────────────────────────────┐    │
│ │                                                │    │
│ │ (A) [📋 複製降級指令 → 切外部 chat 跑]          │    │
│ │     依 §11.5.3 candidate α 引導，降級為         │    │
│ │     DEPRECATED 後重新進 Editor、重新 Save。      │    │
│ │     ⚠ 您本次編輯內容必須手動重輸（不會自動接續） │    │
│ │                                                │    │
│ │ (B) [💾 另存為 DRAFT proposal]                  │    │
│ │     把您本次編輯寫成新檔                        │    │
│ │     /08_dialogue_outputs/CH01_S03/v02_proposal_ │    │
│ │     2026-05-19.md（DRAFT 狀態）。               │    │
│ │     原 LOCKED v02.md 不動。                     │    │
│ │     User 之後可決定要不要 promote / merge。     │    │
│ │                                                │    │
│ │ (C) [取消 — 留 Editor 不 Save]                  │    │
│ │     編輯內容留前端 state；user 自己決定下一步    │    │
│ │     （可手動 copy paste 出去 / 等場景重新降級）  │    │
│ │                                                │    │
│ └────────────────────────────────────────────────┘   │
│                                                       │
│ [關閉 modal 但留 Editor]                              │
└───────────────────────────────────────────────────────┘
```

**三選項拍板對應 D-040：**
- (A) 複製降級指令：走 §11.5.3 Z2 candidate α 流程 — user 切外部 chat 跑 frontmatter 改動 + 09_e 紀錄，回前端重來
- (B) 另存 DRAFT proposal：前端可直接寫一份**新檔**（不覆蓋原 LOCKED）— 因為新檔是 DRAFT 狀態的全新檔不違反 SPEC §16 升級限制
- (C) 取消：純 client-side 動作，不寫檔

**「另存 DRAFT proposal」(B 選項) 行為細節：**

```
前端送請求：
  POST /api/scene/<id>/save-as
  body: {
    target_path: "08_dialogue_outputs/CH01_S03/v02_proposal_2026-05-19.md",
    content: <editor 內容>,
    initial_status: "DRAFT",
    base_dialogue: "08_dialogue_outputs/CH01_S03/v02.md",  // D-042 base_dialogue 欄位
    mode_tag: "SINGLE_ITER",   // 視作 SINGLE_ITER 衍生
    iteration_note: "從 LOCKED v02 race 中救回的 proposal"
  }

Server 行為：
  1. 確認 target_path 不存在 (避免覆蓋)
  2. 從 base_dialogue（原 LOCKED v02）複製 frontmatter base
  3. 改 `狀態：DRAFT`
  4. 補 `base_dialogue / iteration_note` 欄位（D-042 phase_log 欄位）
  5. 寫入 content
  6. 回 201 + new_path
```

**[NEEDS_SCHEMA_SUPPORT]** — `base_dialogue` / `iteration_note` 欄位由 D-042 phase_log 全收 5 新欄位 RESOLVED；§11.5.8 (B) 流程直接使用。

#### 11.5.8.3 為什麼 Step 3 LOCKED race guard 跟 Step 4 mtime checksum 都要做

| 情境 | Step 3 LOCKED guard | Step 4 mtime checksum |
|---|---|---|
| 外部改了內容但狀態維持 DRAFT | pass | 偵測到 mtime drift → §11.7.6 conflict modal |
| 外部升狀態 DRAFT → LOCKED | **block + §11.5.8.2 三選 modal** | （不到 Step 4） |
| 外部沒改任何東西 | pass | pass → 正常 Save |
| 外部同時改內容 + 升 LOCKED | **block + §11.5.8.2** | （不到 Step 4） |
| 外部改名 / 刪檔 | Step 3 GET header 回 404 → 跳「source 不存在」error | — |

**G1 守則：** LOCKED race modal 中 `⚠` badge + What/Where/Why/How 四件套 + 三選項清單 — badge 必搭配清單。

### 11.5.9 跟 §11.7.6 conflict modal 的差別

兩者**不混用**，分別處理不同情境：

| Modal | 觸發 | 互動模型 |
|---|---|---|
| **§11.5.8.2 LOCKED race modal** | Step 3 偵測最新狀態升 LOCKED | 三選項：複製降級指令 / 另存 DRAFT proposal / 取消（**禁止 overwrite**） |
| **§11.7.6 mtime conflict modal** | Step 4 mtime 不符（外部改內容） | 二選：reload 棄改 / 強制覆寫（**容許 overwrite**，但 LOCKED 場景永不會走到這） |

LOCKED race 比 mtime drift **嚴重**：state machine 由人類控制（SPEC §16），不可被前端 mtime guard 蓋過。

### 11.5.10 互動規範總覽

| 入口 | 條件 | 行為 |
|---|---|---|
| Scene Detail [→ 進入編輯] | DRAFT / REVIEW | 跳 §11.3 Editor |
| Scene Detail [→ 進入編輯] | LOCKED | 改顯示「複製降級引導文字」按鈕（§11.5.2） |
| Scene Detail [→ 進入編輯] | DEPRECATED | 跳 §11.3 Editor + 顯示 warning banner（§11.5.4） |
| Scene Detail [→ 進入編輯] | 未啟動（無 dialogue 檔） | 改顯示「[📋 複製 /dialogue-write 指令]」按鈕（§11.6） |
| Scene Detail [📋 複製降級引導文字] | LOCKED | 複製 Z2 candidate α 內容到剪貼簿 + toast |
| Scene Editor [← 返回] | 無 dirty | 直接返回 |
| Scene Editor [← 返回] | 有 dirty | 跳 §11.5.6 confirm dialog |

### 11.5.11 對齊 D-035 §5.3 雙頁面間導航

```
Workspace Home → Project Dashboard → Scene Queue → Scene Detail (cockpit, F1+F2)
                                                       ↓ 點「進入編輯」
                                                   Scene Editor (F3+F7)
                                                       ↓ Save 後
                                                   留在 Editor / 或返回 Scene Detail / 或回 Queue
```

- 從 Scene Detail 進 Editor：one click（DRAFT/REVIEW）或被 LOCKED 守門擋（LOCKED）
- Editor 內無 deep navigation（避免迷路）— 唯一導航是「← 返回 Scene Detail」
- Save 後留在 Editor（Q4），由 user 自選返回

### 11.5.12 對齊 D-029 (α) 完全分離

LOCKED 守門 + 降級流程明示「不走 skill 自動執行」— 全部走「複製引導文字」按鈕 → user 切外部編輯器手動改 frontmatter。

跟 SPEC §16 文件狀態機規則對齊：**人類控狀態機**，agent / 前端工具都不自動降級。

---

## 11.6 通用「複製指令」按鈕 component spec

本子節定義 **整個 §11 共用的單一元件規範**，涵蓋所有「前端要 user 切到外部 chat 跑 agent」的場景。**不在每個出現處重新設計**。

### 11.6.1 為什麼要通用元件

依 D-029 (α) 完全分離拍板，前端跟 agent 完全分離。所有 agent action（`/dialogue-write` / `/qa` / `/create-*` / `/iterate-*` / `/export-*` / LOCKED 降級引導 / 篩選結果批次跑等）都不在前端直接執行，而是：

```
[user 點前端按鈕]
      ↓
[前端組 prompt + context]
      ↓
[複製到剪貼簿]
      ↓
[user 切外部 chat (Claude Code / Cowork)]
      ↓
[user 貼上 + 跑]
      ↓
[agent 改 markdown source]
      ↓
[user 切回前端 refresh 看結果]
```

跨多處重用（§11.1 / §11.2 / §11.3 / §11.4 / §11.5 / §11.9 等），通用元件規範統一才能保證 UX 一致 + 降低重複設計成本。

### 11.6.2 元件 API

**Component 名稱：** `CopyCommandButton`

**Props（建議）：**

```typescript
interface CopyCommandButtonProps {
  // 必填
  command: string;        // 主指令，如 "/dialogue-write S-01-03"
  
  // 可選 context
  contextSummary?: string;    // 已有 context 摘要（如「W-rules 已建 14/27 項，主角A 聲線卡 REVIEW」）
  contextRefs?: string[];     // 跨檔 ref list（如 ["/01_world/...", "/03_characters/..."]）
  contextNotes?: string;      // 自由文字註解（如 LOCKED 降級的多步引導）
  
  // 顯示
  label?: string;         // 按鈕 label，預設「📋 複製 ${command} 指令」
  variant?: "primary" | "secondary" | "ghost";   // 視覺權重
  size?: "sm" | "md" | "lg";
  
  // 行為
  onCopySuccess?: () => void;  // copy 成功 callback（可選，預設只顯示 toast）
  toastMessage?: string;       // 自訂 toast，預設「已複製到剪貼簿，請切到 Claude Code / Cowork 貼上」
  
  // Agent target hint（讓 user 知道該切哪）
  targetAgent?: "claude-code" | "cowork" | "any";   // 預設 "any"
}
```

### 11.6.3 剪貼簿內容 format

複製到剪貼簿的內容統一格式：

```
─── [前端工具產生] ───
指令：
  /dialogue-write S-01-03

已有 Context 摘要：
- W-rules 14/27（缺：戰鬥規則 / 異界規則 / ...）
- C-主角A 聲線卡狀態：REVIEW
- C-反派B 聲線卡狀態：REVIEW
- 細綱：第一章已建 8 場
- 任務包 CH01_S03_台詞任務包.md 已升 REVIEW

相關檔案引用：
- /01_world/01_a_世界觀總覽.md
- /03_characters/main/主角A_聲線卡.md
- /03_characters/main/反派B_聲線卡.md
- /07_scene_tasks/CH01_S03_台詞任務包.md

來源：前端工具 / Scene Detail S-01-03 / 2026-05-18 13:42
─── /[前端工具產生] ───
```

**規則：**
- 開頭結尾 `─── [前端工具產生] ───` 分隔線（agent 端 prompt parsing 用 marker）
- 「指令」段：主 command + 參數
- 「已有 Context 摘要」段：可選，由 `contextSummary` prop 提供
- 「相關檔案引用」段：可選，由 `contextRefs` prop 提供
- 「來源」段：自動加，前端產生資訊 + 時間戳

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — agent 端是否需要 parse 這個 marker 與內部結構，由上下游 specialist 在 `/create-*` / `/dialogue-write` / `/qa` skill 設計時對齊 — 收 §9。

### 11.6.4 按鈕視覺規範

**Primary variant**（HERO / 主要 action）：

```
┌────────────────────────────────────────┐
│ 📋 複製 /dialogue-write S-01-03 指令  │
│ ╳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╳ │
└────────────────────────────────────────┘
```

**Secondary variant**（次要 / inline）：

```
[📋 複製 /qa S-01-03 指令]
```

**Ghost variant**（極輕量 / 行內提示）：

```
📋 複製指令
```

**Label 規則：**
- 預設 label：`📋 複製 ${command} 指令`
- 中文主 + 英文 sub（§1.4.3）：完整版「📋 複製 /xxx 指令 / Copy /xxx command」（長按鈕）；短按鈕只用中文
- emoji 📋 強制（讓 user 從滿屏按鈕中一眼識別「這是複製到外部跑」類）

### 11.6.5 Toast 反饋

按鈕點擊後 → 複製剪貼簿 → 顯示 toast：

```
┌───────────────────────────────────┐
│ ✓ 已複製到剪貼簿                  │
│                                    │
│ 請切到 Claude Code / Cowork       │
│ 貼上 (Ctrl+V / Cmd+V) 後執行       │
│                                    │
│ [關閉]                             │
└───────────────────────────────────┘
```

**自動消失：** 5 秒後 fade out（user 可手動點關閉立即消失）。

**錯誤情境：** 剪貼簿 API 失敗（瀏覽器權限拒絕等）：

```
┌───────────────────────────────────┐
│ ⚠ 複製失敗                         │
│                                    │
│ 瀏覽器不允許自動複製。請手動選取：  │
│ ┌─────────────────────────────┐  │
│ │ /dialogue-write S-01-03     │  │
│ │ 已有 Context 摘要：...        │  │
│ │ ...                          │  │
│ └─────────────────────────────┘  │
│ [關閉]                             │
└───────────────────────────────────┘
```

依 §1.4.3 + §8.1 錯誤訊息四件套精神 — 直接給 user fallback 路徑。

### 11.6.6 使用清單（§11 各子節對應）

| 出現位置 | 對應 command | targetAgent |
|---|---|---|
| §11.1.2 HERO 下一步建議 | `/create-world` / `/create-character` / `/create-outline` / `/create-detailed-outline` / `/create-scene-task` | any |
| §11.1.5 模組狀態 / Authoring 行 | A 路徑 5 個 `/create-*` | any |
| §11.1.5 模組狀態 / Trial 行 | `/dialogue-write S-xx-xx --mode trial` | any |
| §11.1.5 模組狀態 / Convergence 行 | `/dialogue-write S-xx-xx --mode converge` | any |
| §11.1.5 模組狀態 / QA 行 | `/qa S-xx-xx` | any |
| §11.1.5 模組狀態 / Export 行 | **D-038 A1 Export Prompt**（不複製 skill 指令，改開 Export panel 產 prompt）— 詳見 §11.6.5 + L3_EXPORT_PROMPT_SCHEMA §2 | claude-code / codex / 本地 LLM endpoint |
| §11.2.6 Active HD modal | 「複製拍板紀錄到 09_e」（純引導文字） | any |
| §11.2.8 Scene Detail Quick Actions | 多個 — 跑 dialogue-write / qa / export | any |
| §11.2.10 QA finding modal | `/dialogue-write S-xx-xx --single-iter --note "..."`（依 D-028） | any |
| §11.3.3 Editor 版本標頭 | `/qa S-xx-xx --version v01A` | any |
| §11.3.5 details pane 立繪 KEY | 純複製 KEY 到剪貼簿（非 command） — **特例見 §11.6.7** |
| §11.3.7 Editor 底部狀態列 | `/dialogue-write S-xx-xx` | any |
| §11.3.8 diff preview modal 「Save 後自動複製 /qa」 | `/qa S-xx-xx` | any |
| §11.4.7 篩選結果 export | 批次 `/qa S-xx-xx,S-yy-yy,...` | any |
| §11.5.2 LOCKED 場景守門 | （Z2 candidate α 純引導文字，**非 command**）— **特例見 §11.6.7** |

### 11.6.7 特例：純引導文字 / 純 KEY 複製

兩種特例**不**走 §11.6.3 的 `─── [前端工具產生] ───` 包裝：

**特例 1：純 KEY / 識別字串複製**（§11.3.5 立繪 KEY）

```
A-portrait-主角A-angry
```

直接複製 KEY 文字本身，不加 marker、不加 context。toast 改為「✓ 已複製 A-portrait-主角A-angry 到剪貼簿」。

**特例 2：純引導文字複製**（§11.5.3 Z2 candidate α LOCKED 降級）

複製 §11.5.3 內列出的完整引導文字（含三步驟）。不加 `─── [前端工具產生] ───` 包裝 — 因為這段是給 user 自己看的步驟，不是給 agent parse 的 prompt。

**規範：** 元件 props 加 `mode?: "command" | "raw" | "guide"`：
- `command`（預設）：用 §11.6.3 包裝
- `raw`：直接複製 `command` prop 內容（純 KEY 用）
- `guide`：直接複製 `contextNotes` prop 內容（純引導用）

### 11.6.8 多按鈕同時存在的 UI 約束

依 §11.0.4 + §1.4.3 「Suggested actions 純列舉，不是按鈕」精神：

**限制：**
- 同一卡片 / 區塊內 ≤ 3 個 `CopyCommandButton`，超過要折成 dropdown 或下拉清單
- 「複製指令」按鈕不能跟「執行 agent action」按鈕並列出現（後者不存在 — 依 D-029 α）
- QA finding modal「Suggested actions」段純列舉文字，**只有最末**加 1 個 `CopyCommandButton`（跑 iterate）— 不為每條 suggestion 加按鈕

### 11.6.9 「複製指令」按鈕 vs 「跳轉檔案」連結 區別

容易混淆，明示：

| 類型 | 例 | 行為 | UI 區別 |
|---|---|---|---|
| 複製指令按鈕 | `[📋 複製 /qa S-01-03 指令]` | 複製到剪貼簿 → 用戶切外部 chat | emoji 📋 必有 |
| 跳轉檔案連結 | `[→ /07_scene_tasks/CH01_S03]` | 開新分頁載入該檔（§11.7） | emoji `→` 或無 emoji |

兩者**永不**用同一視覺 component。

### 11.6.10 對齊三守則

| 守則 | §11.6 對應 |
|---|---|
| G1 badge 不單獨呈現 | 按鈕本身不是 badge；按鈕周圍卡片有完整 context（卡點原因 / 完成狀態等） |
| G2 流程視覺化僅閱讀順序 | 「複製指令」按鈕**不**暗示流程下一步必執行（user 可選不點） |
| G3 UX grouping 不是資料層必要單位 | 按鈕分組（多個並列時的折疊邏輯）純展示，不暗示後端結構 |
| D-029 (α) 完全分離 | 本元件**就是**完全分離的具體實現 |
| D-029 (c) 手動 Save | 跟 Save 互動：§11.3.8 diff preview modal 內「Save 後自動複製 /qa 指令」是**複製到剪貼簿不是執行 agent** |

---

### 11.6.11 Export Prompt panel — D-038 A1 特例（L3 export 專用，跟其他「複製指令」分開）

對應 D-038 + CODEX C-03 拍板 + L3_EXPORT_PROMPT_SCHEMA v0.1。**v0.3 新增** — 取代 v0.2 中的「複製 /export-dialogue 指令」按鈕（C-12 / O-02 該 skill 不存在）。

**為什麼 Export 是特例：** 一般 `CopyCommandButton`（§11.6.1~§11.6.10）複製**單一 skill 指令**（如 `/dialogue-write S-01-03`）。Export 不一樣 — 它複製**完整的 prompt contract**（含 scope / formats / output_paths / mode / 步驟 / 約束），讓任何 LLM endpoint（CC / CODEX APP / 本地 LLM / Claude API / OpenAI API）都能執行。Prompt 本身就是介面（D-038 設計原則）。

#### 11.6.11.1 Export panel 必要元件（沿 L3_EXPORT_PROMPT_SCHEMA §2.1）

```
┌─────────────────────────────────────────────────┐
│ Layer 3 Bundle Export                            │
├─────────────────────────────────────────────────┤
│ 範圍 / Scope：                                   │
│          ⦿ 全部 / Full repo                       │
│          ○ 僅大綱 / Outline only                  │
│          ○ 僅本場景 / Scene  [CH01_S03 ▼]        │
│                                                  │
│ 格式 / Formats：                                  │
│          ☑ JSON  ☑ MD  ☐ 含已刪除 KEY            │
│                                                  │
│ 輸出路徑 / Output：                               │
│          export/2026-05-19_full.{json,md}        │
│          [改路徑...]                             │
│                                                  │
│ 推送方式 / Push Mode：                            │
│          ⦿ 複製到 clipboard（預設）              │
│          ○ POST 到本地 LLM endpoint              │
│              URL: [____________________]         │
│              Auth: [Bearer __________]           │
│              Model: [llama3.1-70b____]           │
│              [測試連線]                          │
│          ○ POST 到 Claude API (TODO — Phase C+)  │
│          ○ POST 到 OpenAI API (TODO — Phase C+)  │
│                                                  │
│ [預覽 Prompt]   [複製 / 推送]                    │
└─────────────────────────────────────────────────┘
```

完整 UI 規範對齊 `L3_EXPORT_PROMPT_SCHEMA.md §2`（master 新建檔，UX specialist 不擅自改 schema，本子節只規範 UI 對接）。

#### 11.6.11.2 跟一般 `CopyCommandButton` 的差別

| 維度 | 一般 `CopyCommandButton`（§11.6.2） | `ExportPromptPanel`（§11.6.11） |
|---|---|---|
| 複製內容 | 單一 skill command + context 摘要（§11.6.3 包裝） | 完整 prompt contract（標題 + YAML 元資料 + 步驟 + 約束 + 完成回報，依 L3_EXPORT_PROMPT_SCHEMA §1.1 5 區塊） |
| 觸發方式 | 按鈕 one-click 直接複製 | 開 panel → 選 scope / formats / push mode → 預覽 → 複製 / 推送 |
| Push mode | clipboard only | **clipboard + POST endpoint**（推送方式可擴） |
| 目標 agent | claude-code / cowork 任意 chat | claude-code / CODEX APP / 本地 LLM endpoint / Claude API / OpenAI API（任何能讀 prompt 的） |
| 對應 skill | 多個 `/create-*`、`/dialogue-write`、`/qa` 等 | **無 skill** — L3 export 走 prompt contract 不走 skill（D-038 + D-031） |
| Schema version | n/a | 對應 `L3_EXPORT_PROMPT_SCHEMA.md` `schema_version` 欄位 |

#### 11.6.11.3 預覽 Prompt modal

點「預覽 Prompt」按鈕 → 中央 modal 顯示完整組裝後的 prompt（依使用者選項實時組）：

```
┌── Export Prompt Preview / 匯出 Prompt 預覽 ─────────┐
│                                                       │
│ ┌─ Prompt 全文（依 L3_EXPORT_PROMPT_SCHEMA §1.1） ─┐│
│ │ # Layer 3 Export Task — game-dialogue-bible      ││
│ │   — 2026-05-19 14:32                              ││
│ │                                                    ││
│ │ ```yaml                                            ││
│ │ schema_version: "1.0"                              ││
│ │ project_id: "game-dialogue-bible"                  ││
│ │ repo_root: "D:\\劇本開發工具"                       ││
│ │ scope:                                             ││
│ │   type: "full"                                     ││
│ │ formats:                                           ││
│ │   json: true                                       ││
│ │   md: true                                         ││
│ │ output_paths:                                      ││
│ │   json: "export/2026-05-19_full.json"              ││
│ │   md: "export/2026-05-19_full.md"                  ││
│ │ mode: "read_only"                                  ││
│ │ contract_refs:                                     ││
│ │   data_format_spec: "_design/DATA_FORMAT_SPEC.md §9"│
│ │   upstream_downstream_spec: "_design/UPSTREAM... §12"│
│ │ ```                                                ││
│ │                                                    ││
│ │ [執行步驟 5 條依 PROMPT_SCHEMA §1.3]               ││
│ │ [約束規則依 PROMPT_SCHEMA §1.4]                    ││
│ │ [完成回報格式依 PROMPT_SCHEMA §1.5]                ││
│ └────────────────────────────────────────────────────┘│
│                                                       │
│ [關閉]                       [複製 / 推送]            │
└───────────────────────────────────────────────────────┘
```

User 可在貼出前審視 prompt 是否正確。

#### 11.6.11.4 「複製 / 推送」按鈕行為

依使用者「推送方式」單選，按鈕標籤動態變：

| Push mode | 按鈕 label | 行為 |
|---|---|---|
| `clipboard`（預設） | `[📋 複製 Prompt]` | 把組裝完成的 prompt 全文寫到 clipboard；toast「已複製，請貼到 Claude Code / CODEX APP」 |
| `local_llm_endpoint` | `[🚀 推送到 ${user-set-URL}]` | fetch POST 到 URL，body 為 `{ prompt, format: "json" }`；等回應 → 顯示「✓ 推送成功（含回應摘要）」或 30 秒超時「⚠ 已推送（無回應）」 |
| `claude_api`（TODO） | `[🚀 推送到 Claude API]` (disabled, tooltip「Phase C+ 啟用」) | — |
| `openai_api`（TODO） | `[🚀 推送到 OpenAI API]` (disabled, tooltip「Phase C+ 啟用」) | — |

#### 11.6.11.5 推送方式 lifecycle（沿 L3_EXPORT_PROMPT_SCHEMA §4）

| 階段 | 推送方式 | 狀態 |
|---|---|---|
| Phase A.0 | clipboard | **必做**（v0.3 範圍） |
| Phase B 後 | POST 到本地 LLM endpoint（Ollama / vLLM / 自架） | **必做**（D-038 附帶第 2 項） |
| Phase C+ | POST 到 Claude API / OpenAI API（含 auth + retry） | 選做 |
| 未來 | webhook / 觸發 GitHub Action | 待議 |

#### 11.6.11.6 對齊 D-029 α 完全分離（再確認）

依 D-038 對 D-029 α 的細化：「完全分離 = 前端不執行任何 agent action / local CLI；local non-LLM tool action 也不採（仍需 terminal）」。

Export panel **本身**只組 prompt + 複製 / POST — 不執行 export。實際 export 由 user 切到 CC / CODEX / 本地 LLM 跑。**符合 D-029 α 精神**。

POST 推送模式是「prompt 直送 LLM endpoint」— 仍是 LLM agent 在做事，**不是本地 CLI**，仍對齊 α。

#### 11.6.11.7 Export panel 入口位置

Export panel 從以下位置開啟（D-038 + UX_PROTOTYPE_ANALYSIS §10 row 1+8）：

| 位置 | 按鈕 label | 預設 scope |
|---|---|---|
| §11.1.5 模組狀態 H Export 行 | `[📤 開啟 Export panel]` | type: "full" |
| §11.1.7 Module Navigation View Files 區（**v0.3 修正**） | `[📤 開啟 Export panel]` | type: "full" |
| §11.2.2 Scene Detail Quick Actions | `[📤 Export 本場景]` | type: "scene", scene_id: 當前 |
| §11.4.7 篩選結果區（**v0.3 修正**） | `[📤 Export 篩選結果（11 場）]` | type: "scene" 多選或 batch |

舊「複製 /export-* 指令」按鈕**全部移除**（依 D-046 #4 + C-12）。

#### 11.6.11.8 標 BLOCKED / NEEDS_SCHEMA_SUPPORT

- **[BLOCKED:L3_EXPORT_PROMPT_SCHEMA]** — Prompt schema 由 master 新建檔權威，UI 對接以該檔為準；本 §11.6.11 任何不對齊處由 L3_EXPORT_PROMPT_SCHEMA 蓋過。
- **[NEEDS_SCHEMA_SUPPORT]** — N/A（D-039 已 RESOLVED JSON schema = DF `manifest + records[]`）

---

## 11.7 多場景並行 + 編輯衝突偵測

對應 UX_PROTOTYPE_ANALYSIS §9.7（prototype 沒做，從零設計）+ C 自決定項（mtime checksum + 409 + conflict modal 二選）。

### 11.7.1 多場景並行 — 工作流模式

User 同時編多個場景的常見情境：
- 跨場一致性檢查 — 看 S-01-02 同時編 S-01-03
- 大幅 refactor — 跨章節同步修改
- Bible 變更後同步多場 — 跑完 `/iterate-world` 後逐場套用

**支援方式：多瀏覽器分頁（multi-tab）。**

### 11.7.2 「在新分頁開啟」規則

各頁面導航點的處理：

| 入口 | 點擊行為 | 開新分頁觸發條件 |
|---|---|---|
| Project Dashboard 場景卡 | 預設：當前分頁切換 | Shift-click / Ctrl-click / Cmd-click → 新分頁 |
| Scene Queue 場景卡「→ 進入場景 cockpit」 | 同上 | 同上 |
| Scene Detail Quick Actions「跳轉任務包」 | **預設：新分頁** | 不可關閉新分頁行為 |
| Scene Detail Quick Actions「跳轉 view 整合檔」 | **預設：新分頁** | 同上 |
| Scene Detail Required Context 內 link | **預設：新分頁** | 同上 |
| Scene Detail [→ 進入編輯] | 當前分頁切換 | Shift-click → 新分頁 |
| Editor 內「← 返回 Scene Detail」 | 當前分頁切換 | 不可開新（避免迷路） |

**規則：**
- **編輯類動作**（進入 Editor、返回 Detail）預設當前分頁，避免分頁爆炸
- **參照類動作**（跳檔、Required Context link）預設新分頁，方便對照
- Shift / Ctrl / Cmd-click 一律觸發新分頁（瀏覽器原生行為）

### 11.7.3 多分頁狀態管理

各分頁是**獨立 web app instance**（localStorage / hash state 共用 origin 下）：

| 共用 | 不共用 |
|---|---|
| localStorage（theme / facet 上次選擇 / glossary 開關等） | hash route 當前位置 |
| 本地 server 端的 markdown source（同一份 disk file） | 前端 dirty state（Editor 內未 save 變更） |
| Required Context cache（§11.3.6 抽屜）— 各分頁各自 cache | — |

**重要：** 不做 BroadcastChannel / SharedWorker 跨分頁同步 — 個人桌面工具，不必。

### 11.7.4 編輯衝突 — 何時可能發生

**情境 A：多分頁同時編同一場景**
- 分頁 1 開 S-01-03 Editor，改 v01A
- 分頁 2 開 S-01-03 Editor，改 v01A
- 分頁 1 Save 成功，markdown mtime 更新
- 分頁 2 Save 時偵測 mtime 不符 → 衝突

**情境 B：agent 在外部 chat 同時改**
- 前端開 S-01-03 Editor，未 save
- User 切外部 Claude Code 跑 `/dialogue-write S-01-03 --single-iter --note "..."`，agent 寫回 v01A
- 前端 Save 時偵測 mtime 不符 → 衝突

**情境 C：手動編輯器（VS Code）同時改**
- 前端開 Editor 預備改
- User 同時用 VS Code 編 v01A
- VS Code save 後，前端 Save 時衝突

### 11.7.5 衝突偵測機制（依 C 自決定 + 拍板）

**機制：mtime checksum**

**Save 時 client-side：**
1. 前端進入 Editor 時記住每個 version 檔案的 `mtime`（從 server 取）
2. User 編輯 textarea（dirty 累積）
3. Save 時前端送 request：
   ```json
   POST /api/scene/S-01-03/save
   {
     "versions": {
       "v01A": {"content": "...", "expected_mtime": "2026-05-18T13:20:00.000Z"},
       "v01B": {"content": "...", "expected_mtime": "2026-05-18T13:20:00.000Z"}
     }
   }
   ```

**Server-side：**
1. 對每個 version 比對 disk mtime
2. 若有任一不符 → 回 409 + body 含「衝突的 versions 清單 + server 當前 content」
3. 全部相符 → 寫檔 + 回 200 + 新 mtime

**容忍範圍：** mtime 比對精準到秒（避免毫秒級 race 誤判）。

**False positive：** mtime 變但 content 沒變（如 git checkout 同 file 同內容）。處理方式：
- 前端 409 後拿到 server 當前 content
- 自動 diff（client local vs server current）
- 若 diff 為空 → 自動跳「mtime 變但內容沒變」 silent recover（直接重 Save）
- 否則跳 §11.7.6 conflict modal

依 C 自決定項：「對個人單機桌面工具 mtime 足夠，false positive 多時再升級 content hash」 — v0.2 先採 mtime + diff fallback；若實際使用發現 false positive 多再升級。

**[NEEDS_SCHEMA_SUPPORT]** — mtime 在 markdown source / server 端的權威記錄方式（disk fstat vs frontmatter mtime field）— 收 §9。

### 11.7.6 Conflict Modal（依 C 自決定 拍板）

依拍板「reload 棄改 / 強制覆寫」二選不自動 merge。

**v0.3 補充（對齊 D-040 / §11.5.8 LOCKED race guard）：** 本 modal**只處理 mtime drift（外部改內容但狀態未升 LOCKED）**。若外部修改包含「狀態升 LOCKED」，**前端在 §11.5.8 Step 3 LOCKED race guard 就已擋下**，永遠不會走到本 modal 的「強制覆寫」選項。本 modal 二選一**僅適用 non-LOCKED 狀態**的衝突。

```
┌────── 編輯衝突 / Edit Conflict ──────────────────────┐
│ ⚠ Save 失敗：v01A 在您編輯期間被外部修改             │
│                                                        │
│ What：v01A 檔案 mtime 從預期的 13:20 變成 13:42       │
│ Where：/08_dialogue_outputs/CH01_S03/v01A.md          │
│ Why：可能是另一分頁 / agent / 外部編輯器同時修改      │
│                                                        │
│ ─── 您的編輯（client local）─── 24 行 ────────────   │
│   [紅綠 diff vs server 當前 content]                  │
│                                                        │
│ ─── 外部修改（server current）── 26 行 ──────────   │
│   [紅綠 diff vs 您進入 Editor 時的 baseline]          │
│                                                        │
│ 如何處理：                                             │
│ ┌────────────────────────────────────────────────┐  │
│ │ ⚠ 不自動合併 — 二選一                            │  │
│ │                                                  │  │
│ │ (A) [Reload — 棄您的改]                          │  │
│ │     載入 server 當前 content 到 Editor，          │  │
│ │     您的編輯丟失。                                │  │
│ │                                                  │  │
│ │ (B) [強制覆寫 — 蓋外部改]                         │  │
│ │     用您的編輯覆蓋 server，外部修改丟失。         │  │
│ │     [📋 複製外部修改片段到剪貼簿（保險用）]      │  │
│ └────────────────────────────────────────────────┘  │
│                                                        │
│ [取消（留在 Editor 不 save）]                          │
└────────────────────────────────────────────────────────┘
```

**規則對齊（依 C 拍板）：**
- **不自動 merge** — 文字 merge 對 dialogue 太危險（agent 可能改 i18n KEY，merge 易破結構）
- **二選一**：A (Reload 棄改) / B (強制覆寫蓋外部改)
- **保險選項**：選 B 前先「複製外部修改片段到剪貼簿」（§11.6 元件 raw mode），避免外部好改被永久丟
- **取消**：不執行任何寫操作，留在 Editor 讓 user 自己 copy paste 處理

**Multi-version 衝突：** 同 Save 內多個 version 衝突 → 一個 modal 內逐 version 列出，每個 version 獨立選 A/B/取消，最後一起 confirm。

### 11.7.6a Entity 命名衝突 Modal — 4 選項（v0.4 新增 via master 第四輪 CC-09 + Contract B.8）

**v0.4 新增 — 對應 D-033（entity 命名衝突 4 選項）+ CODEX (d) CC-09 解決 — 跟 §11.7.6 mtime drift modal 分拆。**

本 modal **只處理「手稿導入 entity 命名衝突」**（D-031 + D-033）— 不處理 mtime drift（§11.7.6 處理）。觸發時機：user 在外部 chat 跑 `/create-* --trust-level=...` 含手稿導入時，agent 偵測到 entity ID 命名衝突，回前端產 Conflict Modal 供 user 選擇處理方式。

**Modal layout：**

```
┌──── entity 命名衝突 — 4 選項處理 ─────────────────┐
│                                                     │
│ ⚠ 偵測到衝突：手稿中 entity `C-主角A` 跟既有 entity │
│   `C-主角A`（最後更新 2026-05-15）同名。            │
│                                                     │
│ 既有版本摘要（按 hover 查看）：                      │
│   - 聲線：克制、短句、強潛台詞                       │
│   - 性格：內向、責任感重                             │
│                                                     │
│ 手稿版本摘要：                                       │
│   - 聲線：（手稿描述）                               │
│   - 性格：（手稿描述）                               │
│                                                     │
│ ─── 4 選項處理（對齊 D-033）──                       │
│ ┌────────────────────────────────────────────────┐ │
│ │ (1) [📋 複製 merge 指令]                        │ │
│ │     把手稿版內容併入既有 entity；entity_id 不變 │ │
│ │                                                  │ │
│ │ (2) [📋 複製 overwrite 指令]                    │ │
│ │     用手稿版完全覆蓋既有 entity；entity_id 不變 │ │
│ │                                                  │ │
│ │ (3) [📋 複製 create-as-new 指令]                │ │
│ │     手稿版作為新 entity；agent 自動產 new_id    │ │
│ │     如 `C-主角A_v2`；既有不動                   │ │
│ │                                                  │ │
│ │ (4) [📋 複製 skip 指令]                         │ │
│ │     拒絕導入該 entity；既有不動                 │ │
│ └────────────────────────────────────────────────┘ │
│                                                     │
│ [關閉 modal]                                        │
└─────────────────────────────────────────────────────┘
```

**關鍵差別（vs §11.7.6 mtime conflict）：**

| 維度 | §11.7.6 mtime conflict | §11.7.6a entity naming conflict |
|---|---|---|
| 觸發 | Save flow 時偵測 mtime drift | 外部 chat 跑 `/create-*` 手稿導入時 agent 識出命名衝突 |
| 對象 | 單一 dialogue / entity 檔內容 | entity ID 重複（C-* / R-* / S-* 等） |
| 選項數 | 2（reload / 強制覆寫）+ 取消 | 4（merge / overwrite / create-as-new / skip）+ 關閉 |
| 前端動作 | 直接 client-side 寫檔（強制覆寫）或 reload | 只**複製指令**到剪貼簿（D-029 α — 前端不執行 agent action）|
| 紀錄 | 無 phase_log 紀錄（mtime drift 是 race condition）| phase_log `conflict_resolutions` list append 4 選項拍板紀錄（D-033 + DF §3.3e）|

**動態替換：** modal 內的 entity ID（`C-主角A`）+ 摘要內容 + 日期由前端依 agent 回傳的 conflict context fill-in。

**對齊：**
- D-033（4 選項 merge / overwrite / create-as-new / skip）
- D-031（不新增 `/import-*` skill — 走外部 chat agent）
- D-029 α 完全分離（前端不執行 agent action — 只複製指令）
- Contract B.8（entity naming conflict 4 options spec）
- DF §3.3e（conflict_resolutions phase_log schema）

### 11.7.7 多分頁同編 Editor 的 in-page hint

由於不做跨分頁 BroadcastChannel，前端進 Editor 時不知道「另一分頁是否也在編」。但 server 端可實作軟提醒：

**Hint mechanism（可選實作）：**
- Editor 進入時 POST `/api/scene/<id>/edit-lock` 註冊「我在編這場」（含 client_session_id）
- Server 5 秒以內若已有其他 client 註冊 → 回 hint
- Editor 頁首顯示 warning：「⚠ 偵測到另一分頁可能也在編 S-01-03，請小心同時 Save 衝突」
- **不阻擋編輯** — 只是 hint，避免假鎖

**[NEEDS_SCHEMA_SUPPORT]** — 是否實作此 hint mechanism 由 §11.8 build / server design 決定 — 收 §9。本子節**容許但不強制**。

### 11.7.8 衝突偵測涵蓋範圍

| 操作 | 衝突偵測 |
|---|---|
| Scene Editor Save dialogue 檔 | ✓（§11.7.5 mtime checksum） |
| Required Context 抽屜（read-only，不寫） | ✗（無寫操作不需衝突偵測） |
| Scene Detail 內任何操作（read-only） | ✗ |
| QA finding modal「複製指令」 | ✗（純複製，不寫） |
| 「複製降級引導文字」 | ✗（純複製） |
| L3 export（**[BLOCKED:UPSTREAM_DOWNSTREAM]**） | 待定 |

### 11.7.9 G1 / G2 / G3 守則對齊

| 守則 | §11.7 對應 |
|---|---|
| G1 badge 不單獨呈現 | conflict modal 內「⚠ 衝突」badge 必搭配 What/Where/Why/How 四件套 + diff 預覽 |
| G2 流程視覺化僅閱讀順序 | 多分頁工作流圖只描述「可能的 user pattern」，不暗示「必須開幾個分頁」 |
| G3 UX grouping 不是資料層必要單位 | 「多分頁」是 UX 排版選擇；資料層仍是 single source — markdown file on disk |

### 11.7.10 與 §11.3 Editor 的接合點

- Editor 進入時：記住 baseline mtime（每 version 各一）
- Save 前：diff preview modal（§11.3.8）只顯示 client local vs baseline（不查 server）
- Save 中：mtime checksum 比對由 server 做
- Save 後成功：更新 baseline mtime → 後續編輯以新 mtime 為比對基準
- Save 後 409：跳 conflict modal（§11.7.6）

### 11.7.11 不做的（明示）

- 不做自動 3-way merge
- 不做 OT / CRDT
- 不做即時協作（個人工具，不必）
- 不做 file lock — 純 advisory（依 §11.7.7 hint 機制）
- 不做 history rollback — 那是 git 的職責，user 用 git 自己處理

---

## 11.8 Build / package / 啟動規格

對應 UX_PROTOTYPE_ANALYSIS §9.8 + §7.1 工程結構面（單檔過大 / 無建置 / 無型別 / state 散落）+ Bucket #3 D-029 (ii) 本地 web server 拍板。

### 11.8.1 整體技術選擇

| 維度 | 拍板選擇 | 理由 |
|---|---|---|
| **執行模型** | **本地 web server + 瀏覽器 localhost** | D-029 (ii) 拍板；可讀寫 .md 檔 |
| **Server 後端** | **python FastAPI**（候選 1）或 **python http.server + WSGI handler**（候選 2） | python 已是專案 dependency；FastAPI 對寫操作 + JSON API 比 http.server 更舒服 |
| **前端 framework** | **無 framework + 輕量 vanilla JS**（沿 prototype）→ 視需求引入 | prototype Round 2.1 已 self-contained；保留瀏覽器直開可能性 |
| **建置流程** | **可選 Vite**，預設 plain HTML 直接 serve | 漸進；不強制 build step |
| **型別保護** | **JSDoc**（不上 TypeScript） | UX_PROTOTYPE_ANALYSIS §7.1 「個人專案，JSDoc 就夠」 |
| **State 管理** | **輕量 signal / observable**（pure-vanilla pattern） | UX_PROTOTYPE_ANALYSIS §7.1 「重構時引入輕量 state」 |
| **CSS** | **CSS variables + dark mode token**（沿 prototype §5） | 直接平移 |
| **測試** | **不做完整測試框架**（UX_PROTOTYPE_ANALYSIS §7.1） | 個人工具 |
| **Distribution** | **repo 內 + python script 啟動**，不打包 binary | 個人桌面工具 |

### 11.8.2 Repo 結構建議

新增 `_tools/frontend/` 目錄，跟 SPEC §6 既有目錄結構並列：

```
劇本開發工具/
├── 01_world/          ← 既有
├── 02_voice_bible/    ← 既有
├── ...
├── 09_qa_reports/     ← 既有
├── _design/           ← 既有
├── _tools/
│   └── frontend/
│       ├── server.py             # FastAPI server 主檔
│       ├── requirements.txt      # python 依賴
│       ├── README.md             # 啟動說明
│       ├── static/
│       │   ├── index.html        # 主 HTML（hash routing 各頁）
│       │   ├── css/
│       │   │   ├── tokens.css    # 設計 token + dark mode
│       │   │   ├── layout.css
│       │   │   └── components.css
│       │   ├── js/
│       │   │   ├── state.js      # signal/observable
│       │   │   ├── api.js        # server API client
│       │   │   ├── router.js     # hash routing
│       │   │   ├── components/
│       │   │   │   ├── CopyCommandButton.js    # §11.6 通用元件
│       │   │   │   ├── SceneCard.js
│       │   │   │   ├── ProjectDashboard.js     # §11.1
│       │   │   │   ├── SceneQueue.js           # §11.2.1 + §11.4
│       │   │   │   ├── SceneDetail.js          # §11.2.2
│       │   │   │   ├── SceneEditor.js          # §11.3
│       │   │   │   ├── RequiredContextDrawer.js # §11.3.6
│       │   │   │   ├── DiffPreviewModal.js     # §11.3.8
│       │   │   │   ├── ConflictModal.js        # §11.7.6
│       │   │   │   ├── GlossaryTooltip.js      # §11.9.3
│       │   │   │   └── ...
│       │   │   ├── pages/
│       │   │   │   ├── WorkspaceHome.js        # §11.9.1
│       │   │   │   ├── HarnessPreview.js       # §11.9.2
│       │   │   │   └── ...
│       │   │   └── main.js
│       │   └── assets/
│       │       └── glossary.json # §11.9.3 13 術語
│       └── tests/                # 可選；不強制
│           └── README.md
```

**`_tools/frontend/` 跟其他 `_design/` 平級。** 不放到 `_design/` 因為前端**是工具實作**，不是設計文件。

### 11.8.3 Server API 設計（v0.4 master 第四輪 CC-08 校正 — 權威指向 ARCHITECTURE §13.2）

**v0.4 變動（master 第四輪 CC-08 解決）：** Frontend adapter API endpoint 權威定義已搬至 `_design/ARCHITECTURE.md` §13.2（8 個 endpoint 完整規格）。本子節以 ARCH §13.2 為**權威**，列出對應對照。

**權威 endpoint 清單（對齊 ARCHITECTURE §13.2 v1.2 + Contract C.3 + ARCH §13）：**

| Endpoint | 用途 | 對應 Contract / UX |
|---|---|---|
| `GET /api/scene/<id>/header` | Save race guard pre-flight（讀 frontmatter `狀態` + mtime checksum）| B.2 / §11.5.8 |
| `POST /api/scene/<id>/save` | Save flow Step 5（含 mtime checksum）| B.2 / §11.5.8 |
| `POST /api/scene/<id>/save-as` | LOCKED race modal B 選項「另存 DRAFT proposal」 | B.2 / §11.5.8.2 |
| `GET /api/scenes/<id>/versions` | 多版本 manifest（NS-15）| §11.3.3 多版本 |
| `GET /api/scenes/<id>/keys/<key>/lines` | 場景行查 query（NS-30）| §11.3.5 details pane |
| `GET /api/assets?scope=...` | A-* manifest query（NS-2 + Contract B.4）| §11.1.6a Asset Panel |
| `GET /api/assets/<id>/usage` | A-* 反查場景引用（UPS-UX-80 + Contract B.4）| §11.1.6a 子表「覆蓋」欄 |
| `GET /api/scope-counts?scope=...` | Export prompt 元資料供應（Contract A.7 + ARCH §4.2a）| §11.6.11 Export panel |

**ARCH §13.3 不提供的 endpoint（明示對齊 D-029 α + D-038）：**

- **不**提供 `POST /api/export/run`（export 不在前端執行）
- **不**提供 `POST /api/skill/run`（agent 不在前端執行）
- **不**提供 `GET /api/qa/run`（QA 由外部 agent 執行）

**v0.3 → v0.4 變動紀錄（CC-08 解決）：**

v0.3 §11.8.3 列舊 endpoint 清單（含 `GET /api/project/status`、`GET /api/qa/findings`、`GET /api/glossary` 等），但缺 `GET /api/scene/<id>/header`、`POST /api/scene/<id>/save-as`、`GET /api/assets` 系列、`GET /api/scope-counts`，且 `scene` / `scenes` path 命名不一致。CODEX (d) CC-08 識出此衝突。v0.4 master 第四輪校正：以 ARCH §13.2 為權威，本節改為對照表 + 補完整 endpoint 清單。

**舊 endpoint 不再列權威（屬補充 viewer / glossary 類，依需求由 frontend adapter 額外提供，不在 Contract 級鎖定範圍）：**
- ~~`GET /api/project/status`~~ → 改由前端從 `GET /api/scenes` + `GET /api/assets` 組合 derive
- ~~`GET /api/qa/findings`~~ → 改由前端讀 source markdown 直接 derive
- ~~`GET /api/glossary`~~ → 屬 §11.9.3 glossary tooltip 補充 endpoint，非 Contract 鎖定
- ~~`GET /api/health`~~ → 屬 liveness，非 Contract

**Auth：** 無 — 本地 server，預設只 bind `127.0.0.1`，外部不可達。CORS 同 origin only。

**JSON schema：** 各 endpoint 回傳 JSON shape 對齊 ARCH §13 + Contract C；前端 adapter 從 source markdown derive view（Contract C.3 — 前端不消費 Layer 3 Export JSON records[]）。

### 11.8.4 啟動方式

**典型啟動序列（依 REQUIREMENTS_LOCK §2 典型 user session）：**

```bash
# Step 1：terminal 啟動 server
cd D:/劇本開發工具/_tools/frontend
pip install -r requirements.txt    # 首次或更新時
python server.py --port 8765

# Step 2：output 顯示
# > Serving from D:/劇本開發工具
# > Open browser: http://localhost:8765
# > Press Ctrl-C to stop

# Step 3：瀏覽器開 http://localhost:8765
# Step 4：照常使用前端工具
# Step 5：結束時 Ctrl-C 停 server + 手動 git commit
```

**`requirements.txt` 範本：**

```
fastapi>=0.104
uvicorn[standard]>=0.24
python-multipart>=0.0.6
pyyaml>=6.0           # 讀 frontmatter
markdown>=3.5         # render markdown for preview
```

**`server.py` 啟動 skeleton：**

```python
"""
劇本開發工具 前端 server
"""
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import argparse

PROJECT_ROOT = Path(__file__).parent.parent.parent  # 劇本開發工具/

app = FastAPI(title="劇本開發工具前端")

# API routes（見 §11.8.3）
# ...

# Static assets
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="127.0.0.1")  # 不對外
    args = parser.parse_args()
    print(f"> Serving from {PROJECT_ROOT}")
    print(f"> Open browser: http://{args.host}:{args.port}")
    uvicorn.run(app, host=args.host, port=args.port)
```

### 11.8.5 開發模式 vs Production 模式

由於是個人工具，**不嚴格分 dev/prod**：

| 模式 | 啟動 | 用途 |
|---|---|---|
| **預設模式** | `python server.py --port 8765` | 日常使用；HTML 直接 serve，無 build step |
| **可選 dev 模式** | `python server.py --port 8765 --reload` | uvicorn `--reload`，server 改動自動重啟（前端不需要 hot reload，瀏覽器 F5 即可） |
| **可選 Vite 模式** | `vite dev` + `python server.py` 並跑 | 引入 ES modules / Vue / React 後才需要 |

### 11.8.6 State 管理（輕量 signal）

依 UX_PROTOTYPE_ANALYSIS §7.1「重構時引入輕量 state」+「不上 framework」：

**`static/js/state.js` 範本：**

```js
// 輕量 signal pattern
export function createSignal(initial) {
  let value = initial;
  const subs = new Set();
  return {
    get value() { return value; },
    set value(v) {
      if (v === value) return;
      value = v;
      subs.forEach(fn => fn(v));
    },
    subscribe(fn) {
      subs.add(fn);
      fn(value);
      return () => subs.delete(fn);
    }
  };
}

// 全域 state
export const state = {
  currentScene: createSignal(null),         // §11.2 / §11.3
  facetSelection: createSignal({}),         // §11.4
  themeMode: createSignal('light'),         // §11.9.4
  glossaryOpen: createSignal(false),        // §11.9.3
  editorDirty: createSignal({}),            // §11.3 dirty tracking
  requiredContextCache: createSignal(null), // §11.3.6
};
```

**用：**

```js
state.themeMode.subscribe(mode => {
  document.body.dataset.theme = mode;
  localStorage.setItem('theme', mode);
});
```

**理由：** 不上 Redux / MobX / Zustand — 個人工具，signal pattern 30 行夠用。

### 11.8.7 dark mode token（§5 prototype 平移）

直接平移 prototype `static/css/tokens.css`：

```css
:root {
  /* light theme tokens */
  --color-bg: #fff;
  --color-text: #1a1a1a;
  --color-primary: #2563eb;
  --color-warning: #d97706;
  --color-danger: #dc2626;
  --color-success: #16a34a;
  --color-border: #e5e5e5;
  --color-bg-elevated: #f9f9f9;
  /* ... 沿 prototype §5 ... */
}

[data-theme="dark"] {
  --color-bg: #1a1a1a;
  --color-text: #f5f5f5;
  /* ... */
}
```

`§11.9.4` Theme toggle 切換 `data-theme` attribute。

### 11.8.8 Build script（可選）

預設**不**需要 build。若未來引入 Vite / TypeScript / 等：

```bash
# 可選 build
cd _tools/frontend/static
vite build              # 產 dist/
# server.py 改 mount dist/ 而非 static/
```

本 v0.2 規範**不強制**引入 build。沿 prototype 「瀏覽器直開」精神。

### 11.8.9 分發

**個人工具不打包成 binary。** Distribution = repo 本身：

```bash
git clone https://github.com/.../劇本開發工具.git
cd 劇本開發工具/_tools/frontend
pip install -r requirements.txt
python server.py
```

如果 user 同時跨機（如桌面 + 筆電），透過 git pull 同步。

### 11.8.10 啟動文檔 `_tools/frontend/README.md` 內容

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — README 內容由本子節提架構，具體 onboarding 步驟由實作 phase 補。

預期內容：
- 啟動 3 步（依 §11.8.4）
- 故障排除（port 衝突 / python 版本 / pip install 失敗）
- 跟 Claude Code / Cowork 配合的「雙視窗工作流」說明（§11.0.5 fidelity 規則）
- repo git workflow（手動 commit 紀律 — 對齊 D-029 (c)）
- 連結回 SPEC.md + UX_SPEC.md §11

### 11.8.11 載入效能 expectations

個人工具，不必過度優化：

| 載入維度 | 目標 |
|---|---|
| 初次載入 Project Dashboard | < 3 秒（fetch markdown + parse） |
| Scene Detail 切換 | < 1 秒 |
| Scene Editor 進入 + Required Context prefetch | < 2 秒 |
| Save + diff preview generation | < 500ms |
| Theme toggle | 瞬時（< 100ms） |

不做 lazy load / code splitting — 個人工具不必。

### 11.8.12 對齊整體 v0.2 拍板

| 拍板 | §11.8 對應 |
|---|---|
| D-029 (ii) 本地 web server | §11.8.1 + §11.8.4 |
| D-029 (α) 完全分離 | server 不會主動跑 agent；所有 agent action 走 §11.6 複製指令 |
| D-029 (c) 手動 Save | §11.8.3 `/api/scenes/{id}/save` endpoint 對應 §11.3.7 Save 流 |
| UX_PROTOTYPE_ANALYSIS §7.1 重構建議 | §11.8.6 signal + §11.8.7 token + §11.8.1 JSDoc |
| Bucket #3 必要功能 F1/F2/F3/F6/F7 | §11.8.2 components/* 對應每個子節 |

---

## 11.9 4 個保留元件對齊（D-036）

對應 D-036 拍板：UX_PROTOTYPE_ANALYSIS §6 的 4 個保留元件適用 single-project repo 場景。

| 元件 | 子節 | 用途 |
|---|---|---|
| Workspace Home 多專案選擇器 | §11.9.1 | 未來多專案；現在 single-project entry |
| 公版 Harness / 模板管理 preview | §11.9.2 | 服務 SPEC §7 Template/Instance 架構 |
| Glossary tooltip 13 術語 | §11.9.3 | 個人長期記憶輔助 |
| Light / Dark mode toggle + 雙主題 | §11.9.4 | 跨日夜使用 |

### 11.9.1 Workspace Home（multi-project 入口的 single-project 退化形式）

**位置：** 進前端工具的第一頁，URL `#/` 或 `#/home`。

**Layout（single-project 場景）：**

```
┌─────────────────────────────────────────────────────────────────┐
│ Workspace Home / 工作區首頁                                      │
│                                                                  │
│ 目前專案 / Current Project                                       │
│ ┌──────────────────────────────────────────────────┐            │
│ │ 🎮 劇本開發工具                                    │            │
│ │ ────────────────                                  │            │
│ │ 共 26 場景 / 進度 58%                              │            │
│ │ 最後修改：2026-05-18                              │            │
│ │                                                    │            │
│ │ [→ 進入 Project Dashboard]                        │            │
│ └──────────────────────────────────────────────────┘            │
│                                                                  │
│ ─── 未來功能 ───                                                  │
│                                                                  │
│ [➕ 新增其他專案]（未來啟用 — 灰顯）                              │
│                                                                  │
│ ─── 工具 ───                                                      │
│                                                                  │
│ [📖 Glossary]（§11.9.3）  [⚙ 設定]（含 §11.9.4 theme toggle）   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**設計重點：**
- single-project 場景下，「目前專案」就一個 entry — 點即進 Dashboard
- 「新增其他專案」按鈕**灰顯**並 tooltip 「未來支援多專案；現在請手動建另一個 repo」（依 G2 守則「不暗示流程必走」）
- **不**自動跳 Dashboard — 留 Workspace Home 作為入口頁，user 第一次進工具可看 overview

**未來多專案擴充（不在 v0.2 scope）：**
- list 多個 project entry
- 各 entry 點進去獨立 Dashboard
- cross-project chip / summary（**[NEEDS_SCHEMA_SUPPORT]** — multi-project schema）

### 11.9.2 公版 Harness / 模板管理 preview

依 D-036 + UX_PROTOTYPE_ANALYSIS §6「服務 SPEC §7 Template/Instance 架構」。

**位置：** Workspace Home 「工具」區的子入口，或 Project Dashboard 「模組導航」區的入口。URL `#/harness`。

**Layout：**

```
┌─────────────────────────────────────────────────────────────────┐
│ 公版 Harness / 模板管理                                          │
│ Breadcrumb：Workspace / Harness                                  │
│                                                                  │
│ 目前 Instance：劇本開發工具                                      │
│ 對應 Template：v1.0（2026-04 升版）                              │
│ Instance 微調紀錄：3 處（見 00_b 作品專屬 LOCK）                 │
│                                                                  │
│ ─── Template 模板總覽 ───                                         │
│                                                                  │
│ ┌─ 系統協議 ────────────────────────────────────┐              │
│ │ 00_a 工具總協議  ✓ 在 Template 內                │              │
│ │ 00_b 作品專屬    ◐ Instance 微調 3 處             │              │
│ │ 00_c 世界觀協議  ✓ 在 Template 內                │              │
│ │ ...（共 26+ 個協議檔）                            │              │
│ └─────────────────────────────────────────────────┘              │
│                                                                  │
│ ┌─ 操作 ───────────────────────────────────────────┐            │
│ │ [📋 複製 Template 升級指令]                       │            │
│ │   （將從 v1.0 升 v1.1 並同步 Instance）           │            │
│ │ [📋 複製 Instance 微調指令]                       │            │
│ │   （改 00_b 作品專屬內容）                         │            │
│ │ [跳轉 _design/MASTER_PLAN.md]                     │            │
│ └─────────────────────────────────────────────────┘              │
│                                                                  │
│ [← 返回 Workspace Home]                                          │
└─────────────────────────────────────────────────────────────────┘
```

**設計重點：**
- **preview 性質** — 不允許前端直接改 Template / Instance 內容
- 所有變更走「複製指令」按鈕（§11.6）切外部 chat 跑（依 D-029 α）
- Template 模板總覽是 read-only list
- Instance 微調紀錄連到 00_b 作品專屬 LOCK 檔

**對齊 SPEC §7 Template/Instance：**
- Template = 跨專案可重用的 26+ 協議檔（在另一 repo）
- Instance = 本 repo（劇本開發工具）+ 00_b 微調

**[NEEDS_SCHEMA_SUPPORT]** — Template / Instance 兩 repo 的 cross-reference 機制（Instance 怎麼指向 Template 版本）— 收 §9。

**[BLOCKED:UPSTREAM_DOWNSTREAM]** — Template 升級流的 skill（如 `/template-upgrade`）是否存在 — 收 §9。

### 11.9.3 Glossary tooltip — 13 術語

依 UX_PROTOTYPE_ANALYSIS §6 + prototype 平移。

**Glossary 來源檔：** `_tools/frontend/static/assets/glossary.json`

**13 術語預期清單**（v0.2 起點；未來可擴）：

| # | 術語 | 簡述 |
|---|---|---|
| 1 | W-rules | 世界規則 entity |
| 2 | V-vocab | 世界詞彙 entity |
| 3 | C-character | 角色 entity |
| 4 | R-relationship | 關係 entity |
| 5 | P-plot | 主線情節 entity |
| 6 | CH-chapter | 章節 entity |
| 7 | S-scene | 場景 entity |
| 8 | A-asset | 美術資產 entity（D-023 新增） |
| 9 | i18n KEY | 每段台詞 unique KEY（D-022 新增） |
| 10 | mode_tag | 試寫 / 破格 / 收斂 / SINGLE_ITER（D-028 新增） |
| 11 | qa_type | 09_a~i 等 QA 模板 type |
| 12 | pipeline_state | DRAFT / REVIEW / LOCKED / DEPRECATED |
| 13 | LOCKED | 文件鎖定狀態（SPEC §16） |

**Tooltip UX：**

```
─── 文本中遇到 [W-rules]（虛線下標） ───────

User hover / focus →

   ┌──── Glossary ────┐
   │ W-rules           │
   │ ─────────         │
   │ 世界規則 entity： │
   │ 此世界內的「物理 │
   │ 法則」「能量規則」│
   │ 「社會階層」等    │
   │ 不可違反的規範。  │
   │                   │
   │ 詳見 SPEC §5.1    │
   │ [→ 跳 SPEC]        │
   └───────────────────┘
```

**規範：**
- Glossary 在 §11.1 / §11.2 / §11.3 / §11.4 / §11.9 各頁全域可用
- 觸發方式：hover（桌面）+ focus / tap-and-hold（觸控）
- 顯示位置：自動 anchor 到觸發 element 旁，避免遮擋
- 不在 L1 / L3 用（L1 / L3 是純 Markdown，無 hover — 依 §1.4.4）
- Tooltip 內可放「跳 SPEC §X」連結，user 點 → 新分頁開 SPEC.md anchor
- 13 術語的具體文字內容**[BLOCKED:UPSTREAM_DOWNSTREAM]** — 由 SPEC § 對齊 — 收 §9

**Glossary 整頁入口（§11.9.1 Workspace Home / §11.1.0 頁首均有）：**

URL `#/glossary` — 完整 13 術語縱向 list，每條附「詳見 SPEC §X」連結。供 user 主動查時用。

### 11.9.4 Light / Dark mode toggle + 雙主題

依 D-036 + UX_PROTOTYPE_ANALYSIS §6 + prototype §5 平移。

**位置：** 每頁頁首右上角 + Workspace Home 「設定」內。

**UI：**

```
[☀ Light]  [🌙 Dark]  [⚙ System]
   ↑ 當前選擇
```

3 選 1：
- ☀ Light：強制 light
- 🌙 Dark：強制 dark
- ⚙ System：跟 `prefers-color-scheme` 系統設定

**Token 切換：** 透過 `data-theme="light"` / `data-theme="dark"` attribute on `<html>` 元素，CSS variables 自動切換（§11.8.7）。

**Persisted：** 選擇存 `localStorage.theme`（§11.0.1 L2 容許 localStorage）；下次進工具自動套用。

**dark mode 細節對齊（UX_PROTOTYPE_ANALYSIS §10.3 review queue）：**
- Future module 灰階（§11.1.5「未啟動」狀態）在 dark mode 下用淡灰 + 「（未啟動）」文字標籤雙保險
- 紅 ⚠ 危險色在 dark mode 用較高飽和（如 `#f87171` 而非 `#dc2626`）保持對比
- 綠 ✓ 完成色在 dark mode 用 `#4ade80` 而非 `#16a34a`
- 立繪 KEY 灰色淡字（§11.3.4 行首）在 dark mode 用 `--color-text-muted-dark`

**a11y / contrast：**
- 對齊 WCAG AA（個人工具不強求 AAA）
- 紅綠 diff（§11.3.8 diff preview）用色 + 符號（`-` 紅 / `+` 綠）雙保險，色盲友好

### 11.9.5 4 元件互動約束

| 元件 | 在哪頁出現 | 互動約束 |
|---|---|---|
| Workspace Home | `#/` 唯一一頁 | 進工具的入口；不放別頁的 nav 入口 |
| Harness Preview | `#/harness` + Workspace Home 入口 + Dashboard 模組導航入口 | 全 read-only；agent action 走複製指令 |
| Glossary tooltip | 全頁全域可用（除 L1 / L3） | Hover / focus 觸發；不阻擋 user 操作 |
| Glossary 整頁 | `#/glossary` 一頁 | read-only list |
| Theme toggle | 每頁頁首 + Workspace Home 設定 | 切換即時生效；不需 confirm |

### 11.9.6 對齊 G1 / G2 / G3 守則

| 守則 | §11.9 對應 |
|---|---|
| G1 badge 不單獨呈現 | Workspace Home 「目前專案」卡：「26 場景 / 進度 58% / 最後修改」三層；Harness 「Template v1.0 / Instance 微調 3 處」二層 |
| G2 流程視覺化僅閱讀順序 | Workspace Home 不暗示「必先進 Glossary / Harness 才能進 Dashboard」；Harness 不暗示「必先升 Template 才能改 Instance」 |
| G3 UX grouping 不是資料層必要單位 | 4 元件是 UX 入口排版；不對應任何 schema 結構 |

### 11.9.7 跟 v0.1 §1.3 拒絕清單的對照（複述 §1.4.4）

| §1.3 原拒絕 | v0.2 / §11.9 處置 |
|---|---|
| `公版 Harness / 模板管理` | **L2 採用** preview 形式（§11.9.2） |
| `跨專案 summary chip` | **L2 採用** Workspace Home single-project 退化（§11.9.1） |
| `Glossary tooltip / ? icon` | **L2 採用**（§11.9.3）；L1 / L3 仍拒絕 |
| `Workspace 層三層思考` | **L2 採用** Workspace Home → Dashboard → Queue → Detail → Editor 五層導航；L1 / L3 仍退化為 Project / Scene 兩層 |

依 §1.4.4 規則 — 各項要看 L1 vs L2，不是「全部 v0.2 復活」。

### 11.9.8 4 元件 + 主 §11.1-§11.8 的關係

```
Workspace Home（§11.9.1）
   ↓ 主入口
Project Dashboard（§11.1）
   ↓ 跳場景
Scene Queue（§11.2.1 + §11.4）
   ↓ 跳場景
Scene Detail (cockpit)（§11.2.2）
   ↓ 「進入編輯」+ LOCKED 守門（§11.5）
Scene Editor（§11.3）+ §11.7 衝突偵測

橫切：
- Glossary tooltip（§11.9.3）— 全頁可用
- Theme toggle（§11.9.4）— 全頁可用
- CopyCommandButton（§11.6）— 全頁可用
- Harness Preview（§11.9.2）— 從 Workspace Home / Dashboard 跳入
- 多分頁工作流（§11.7.1-§11.7.3）— 全頁可用
```

---

# 11 章節結束 — §11 整體交付完成檢核表

對齊 UX_PROTOTYPE_ANALYSIS §9 / §10 + REVISED_WORK_ITEMS §7.5 UX-8~15 子任務：

| Deliverable | 子節 | 拍板對齊 |
|---|---|---|
| §11.0 章節導論 + 結構索引 | §11.0 | UX-8 + 跨 L1/L2 守則對齊 |
| §11.1 F1 Project Dashboard | §11.1 | UX-8 + D-034 複製指令按鈕 + §10.3 review queue |
| §11.2 F2 Scene Queue + Detail (cockpit, read-only) | §11.2 | UX-9 + UI_UX_SPEC §12 #4/#7 critical preserve |
| §11.3 F3 Scene Editor 三欄並排（D-035 新頁） | §11.3 | UX-10 / UX-12a + Q1/Q2/Q3/Q4/Q5/Z1 拍板 |
| §11.4 F6 搜尋 + 篩選 facet | §11.4 | UX-11 + D-027 可擴充 qa_type |
| §11.5 F7 編輯 + LOCKED 守門 + Detail→Editor 導航 | §11.5 | UX-12 / UX-12b + Q3 + Z2 candidate α |
| §11.6 通用「複製指令」按鈕 component spec | §11.6 | UX-13 + D-029 (α) 完全分離通用化 |
| §11.7 多場景並行 + 編輯衝突偵測 | §11.7 | UX-14 + C 自決定 mtime checksum |
| §11.8 build / 啟動規格 | §11.8 | UX-15 + D-029 (ii) 本地 web server |
| §11.9 4 保留元件對齊（D-036） | §11.9 | D-036 + UX_PROTOTYPE_ANALYSIS §6 |

---

# 附錄 A：v0.2 交付完成檢核（保留歷史）

對應 REVISED_WORK_ITEMS §7.5 UX-1~UX-17 任務：

| 任務 | 對應章節 | 狀態 |
|---|---|---|
| UX-1 §1.4 partial supersede 重寫 | §1.4.1~§1.4.4 | ✓ 完成 |
| UX-2 §2 view-\* 補完 | §2.1~§2.5 | ✓ 完成 |
| UX-3 §3 export-\* 補完 | §3.1~§3.6 | ✓ 完成 |
| UX-4 §4 /status 看板補完 | §4.1~§4.5 | ✓ 完成 |
| UX-5 §5 6 REVIEW gate 補完 | §5.1~§5.5 | ✓ 完成 |
| UX-6 §6 QA 8 報告 + 彙整版補完 | §6.1~§6.5 | ✓ 完成 |
| UX-7 對齊 UPSTREAM §7 53 [UX] 標記 | §7.8.1~§7.8.13 | ✓ 完成 |
| UX-8 §11 章節導論 + F1 Dashboard | §11.0 + §11.1 | ✓ 完成 |
| UX-9 §11.2 F2 Scene Queue + Scene Detail | §11.2 | ✓ 完成 |
| UX-10 §11.3 F3 Scene Editor 三欄並排（D-035） | §11.3 | ✓ 完成（含 Z1） |
| UX-11 §11.4 F6 搜尋 + 篩選 facet | §11.4 | ✓ 完成 |
| UX-12a §11.5 Scene Editor layout 細節（已併入 §11.3） | §11.3 | ✓ 完成 |
| UX-12b §11.5 Scene Detail→Editor 導航 + LOCKED 守門 | §11.5 | ✓ 完成（含 Z2 candidate α） |
| UX-13 §11.6 通用「複製指令」按鈕 component spec | §11.6 | ✓ 完成（升格為通用元件） |
| UX-14 §11.7 多場景並行 + 編輯衝突偵測 | §11.7 | ✓ 完成 |
| UX-15 §11.8 build / 啟動規格 | §11.8 | ✓ 完成 |
| UX-16 §9 [NEEDS_SCHEMA_SUPPORT] 清單 | §9.1~§9.11 | ✓ 完成（33 項 NS-1~NS-33） |
| UX-17 §10 master 裁決問題清單 | §10.1~§10.11 | ✓ 完成（10 項） |
| 額外 §11.9 4 個保留元件對齊（D-036） | §11.9 | ✓ 完成 |

**v0.2 總計：** 17 個任務 + 1 個額外子節全部交付。

---

# 附錄 B：v0.3 patch 交付完成檢核（CODEX 審查 + D-046 派工）

對應 DECISIONS_LOG §6.7 D-046 列的 7 項 UX patch + master 第四輪整合新增 1 項：

| Patch # | 議題 | 對應章節 / Section | 狀態 | 依據 |
|---|---|---|---|---|
| **P0** | frontmatter v0.2→v0.3 + 變更摘要 | 文件頭 | ✓ 完成 | D-046 派工 |
| **1** | UX-54~80 對照表進 §7（合併 54/55 + 64/65）| §7.9（25 筆，淨增） | ✓ 完成 | D-046 #1+#2 / CODEX C-06 |
| **2** | 全文 `/iterate-dialogue` → `/dialogue-write --single-iter` | §2.2 / §6.1 / §6.2.1 / §6.2.3 / §6.5 / §11.2.10 / §11.6.9 / §11.7.4 / §11.6.6 | ✓ 完成（8 處替換） | D-046 #3 / D-028 / C-12 / O-02 |
| **3** | `/export-dialogue` → A1「複製 Export Prompt」按鈕 | §3.4 修為註記 / §11.1.5 / §11.1.7 / §11.6.6 / §11.6.11 新增（含 §11.6.11.1~§11.6.11.8） | ✓ 完成 | D-046 #4 / D-038 / L3_EXPORT_PROMPT_SCHEMA / C-12 |
| **4** | §11.5.3 LOCKED 降級指引刪三 frontmatter 欄位 | §11.5.3（改寫為「09_e final-gating 紀錄」） | ✓ 完成 | D-046 #5 / C-16 / O-03 |
| **5** | §11.5.x Save race guard 補完 | §11.5.7 / §11.5.8（新增「Save flow 5 步」+「三選項對話框」） + §11.7.6 補充 | ✓ 完成 | D-040 / C-15 |
| **6** | §9 NEEDS_SCHEMA_SUPPORT 拆三類 | §9.1 Schema 22 項 / §9.2 Query-API-Adapter 9 項 / §9.3 Algorithm 2 項 + NS-NEW-1 | ✓ 完成（總 34 項，含新增 NS-NEW-1） | D-046 #6 / C-17 |
| **7** | mode_tag 用語修正（不可擴充）| §11.4.3 facet 表 | ✓ 完成 | D-046 #7 / O-05 / D-027 |
| **8** | §11.1 F1 Dashboard 補 A-\* asset panel | §11.1.6a 新增（含 §11.1.6a.1~§11.1.6a.3） | ✓ 完成（7 subtype 分組依 D-044） | D-045 / D-044 / C-14 |
| **P-final** | §10 對齊 D-037~D-046 + RESOLVED 對照 | §10.11.1~§10.11.3（10 項議題重新分類） | ✓ 完成 | D-046 整體派工收尾 |

**v0.3 總計：** 9 個 patch + 1 個 frontmatter 升版 + 1 個彙整 = **10 個交付項全完成**。

---

# 附錄 C：v0.3 對齊 D-037~D-046 全表

| D-NNN | 議題 | UX v0.3 影響章節 | 處置 |
|---|---|---|---|
| D-037 | `dialogue_keys` Map shape | §11.3.5 details pane 欄位呈現 + §9.1.2 NS-5~8 RESOLVED + §7.9.2 UPS-UX-60 | ✓ 對齊 |
| D-038 | L3 export A1 prompt 流程 | §3.4 / §11.1.5 / §11.1.7 / §11.6.11 / §7.9.5 UPS-UX-72~75 | ✓ 對齊 |
| D-039 | JSON schema = DF `manifest + records[]` | §9.1.4 NS-12 RESOLVED + §11.6.11 對齊 | ✓ 對齊 |
| D-040 | LOCKED Save guard | §11.5.7 / §11.5.8 新增 + §11.7.6 補充 | ✓ 對齊 |
| D-041 | A-\* source of truth = `10_art_assets/` | §11.1.6a / §11.1.7 / §7.9.6 UPS-UX-71 + §9.1.1 RESOLVED | ✓ 對齊 |
| D-042 | phase_log 5 新欄位 + base_dialogue | §11.5.8 (B) / §11.3.5 + §9.1.4 / §9.1.5 RESOLVED + §10.6 RESOLVED | ✓ 對齊 |
| D-043 | 09_g/h/i 全預設必跑 | §6 / §6.3 + §10.6 RESOLVED + 附錄 C 對齊 | ✓ 對齊 |
| D-044 | A-\* subtype 7 種 | §11.1.6a 分組 + §7.9.6 UPS-UX-77 | ✓ 對齊 |
| D-045 | A-\* 不納入 narrative `/status` | §11.1.6a / §11.1.6a.2 + §10.x | ✓ 對齊 |
| D-046 | UX patch 整體派工 | 本附錄 B 全 8 項 | ✓ 對齊 |

---

**待第四輪整合（v0.3 後續）：**
- 升 INTEGRATION_CONTRACTS v1 → v2 對齊 D-037~D-046
- 整合到主 SPEC / ARCHITECTURE / TASKS
- promote P-021 ~ P-026 為 D-NNN（已對應到 D-037~D-046）
- 修訂 PHASE_3_COMPLETION_REPORT v4.0 為 final
- 重評可進 A.0
- UD specialist 補 §3.6.3 / §3.6.6 09_e final-gating schema（NS-NEW-1 對齊）
- UD specialist §12 改寫對齊 D-038（移除 server-side CLI 假設）
