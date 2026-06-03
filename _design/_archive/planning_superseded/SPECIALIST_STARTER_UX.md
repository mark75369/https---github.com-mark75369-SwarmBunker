狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-17  
適用範圍：UI/UX specialist 對話的啟動包  
優先級：高  

# SPECIALIST_STARTER — UI/UX

# 0. 對話啟動指令（直接複製貼到新對話）

```
我有一個 game-dialogue-bible 專案，進入並行 specialist 設計階段。
你是「UI/UX specialist」對話。

工作資料夾：<搬遷後的新路徑>

**第一步必讀（按順序）：**
1. _design/MASTER_PLAN.md（你的 scope 邊界）
2. _design/INTEGRATION_CONTRACTS.md（你跟其他 specialist 的介面）
3. _design/SPEC.md 第 12 節、第 13 節（下游 pipeline、視圖層機制）
4. _design/SPEC.md 第 14 節（24 個 skill 清單，含 /view-*、/export-*、/status）
5. _design/ARCHITECTURE.md 第 4 節（視圖層實作）
6. _design/TASKS.md 第 4 節 C.3 / C.5（/view-* 與 /export-* 任務）
7. _design/UX_PRIOR_DRAFT.md（使用者另一個 claude-UX 對話的整理稿，啟動前由 user 提供）
8. 本檔案（你的 starter）

**前提：本專案沒有獨立 GUI。**
所有「使用者介面」都是 agent 對話中的 Markdown 呈現，或匯出到 view/ 的整合檔。
不要設計 GUI 元件（沒有 button、沒有 form）；要設計「資料如何用 Markdown 呈現給使用者直白檢視」。

**你的 scope（OWNS）：**
- /view-*（world / character / outline / detailed-outline）的呈現格式設計
- /export-* 整合檔的 Markdown 結構與閱讀體驗
- /status 看板的視覺呈現（Markdown）
- 6 個 REVIEW gate 印給使用者的清單格式
- QA 報告的閱讀體驗（5 份 + 彙整版的視覺結構）
- 跨檔導航設計
- 使用者輸入錯誤時的提示格式

**禁止越界：**
- 不設計下游 pipeline 流程（屬於上下游 specialist）
- 不更動 canonical schema（屬於資料格式 specialist）
- 不設計 skill 觸發機制與內部邏輯
- 不引入 GUI 元件（這是 agent 對話介面，不是 web app）

**最終產出：**
- _design/UX_SPEC.md（含「需 master 裁決問題清單」結尾段）

請先告訴我讀完上述文件後對 scope 的理解，再開始展開。
```

---

# 1. 你的 scope 詳細

## 1.1 主任務：8 大呈現情境的設計

| 情境 | Skill | 呈現挑戰 |
|---|---|---|
| 查看完整世界觀 | `/view-world` | 多份分拆檔組合，要清晰閱讀 |
| 查看單一角色 | `/view-character <name>` | 聲線卡 + 關係矩陣段落 + 弧線整合 |
| 查看大綱 | `/view-outline` | 主線 + 章節結構 + 弧線 |
| 查看細綱 | `/view-detailed-outline` | 章節節奏 + 揭露時間軸 + 伏筆佈點 |
| 進度看板 | `/status` | 邏輯實體完成度的視覺呈現 |
| REVIEW gate | A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5 | 印給使用者「待升級檔案」清單 |
| QA 報告閱讀 | `/qa` | 5 份報告 + 彙整版的閱讀順序 |
| 錯誤提示 | 各 skill | 缺先決條件、TODO 過多、衝突等 |

## 1.2 用「Markdown 呈現」這個約束的價值

agent 對話介面有限制，但也有優勢：
- 可用表格、清單、代碼塊、層級標題
- 可用 emoji 標示狀態（✅⏸️⚠️❌）
- 可用 markdown link 跨檔導航（雖然 agent 對話中點不到，但匯出後可用）
- 可用 frontmatter 在整合檔頭部標 metadata

## 1.3 禁止越界（再次強調）

- 不引入「按鈕」「表單」「下拉選單」等 GUI 元件
- 不設計 skill 觸發機制（不能說「按某鈕觸發 X」— 觸發只能是 slash command 或對話）
- 不更動 canonical schema 來服務呈現需求（如真有需要，標 `[NEEDS_SCHEMA_SUPPORT]` 回饋資料格式 specialist）

---

# 2. 強制檢視議題

## 2.1 議題 A：`/status` 看板的視覺結構

**現況：** ARCHITECTURE 2.3 已給範例：

```
=== 邏輯實體完成度 ===

W-rules               100%  (FINAL)
W-language             75%  (1 REVIEW)
V                      50%  (3 DRAFT)
...
```

**你要回答：**
- 這個格式可讀嗎？
- 是否要分組（依 Phase / 依實體類型）？
- 是否要視覺化（如 `[████░░░░░░]` 進度條）？
- 是否要 highlight 缺漏實體？

## 2.2 議題 B：REVIEW gate 印給使用者的清單

**現況：** TASKS 各 gate 描述為「印出 DRAFT 待升 REVIEW 的檔案」

**你要回答：**
- 純清單還是表格？
- 是否要含「升級指令範本」讓使用者直接複製？
- 是否要顯示每份檔案的「為什麼要升級」（依 phase 啟動條件）？

## 2.3 議題 C：QA 5 份報告的閱讀體驗

**現況：** SPEC 12.7 已定優先順序（09_f → 09_d → 09_b → 09_a → 09_c）

**你要回答：**
- 彙整版的格式 — 是 5 份報告的 summary 還是 cross-cut 視圖？
- 高優先問題如何 highlight？
- 報告之間如何 cross-reference？
- 是否要有「修稿建議」段落？

## 2.4 議題 D：跨檔導航

**現況：** 整合視圖（`/view-*`）動態組合多份分拆檔

**你要回答：**
- 整合視圖內怎麼標出「這段來自哪個 source 檔」？
- 是否要在每段尾加 source 引用？
- markdown link（雖在 chat 中點不到）是否還是寫進去（供匯出後用）？

## 2.5 議題 E：錯誤提示格式

**現況：** TASKS 各 skill 提到「拒絕並提示」但未定義提示格式

**你要回答：**
- 標準錯誤訊息結構（錯誤類型 / 原因 / 修正建議 / 替代命令）？
- 是否要區分「使用者錯誤」（提供修正）vs「系統錯誤」（提供 debug 資訊）？

## 2.6 議題 F：claude-UX 對話歷史的吸收

**user 在另一個 claude-UX 對話中設計過 UI/UX**，會提供整理稿 `UX_PRIOR_DRAFT.md`。

**你要做：**
- 讀完該稿
- 對照本 starter 的 scope，分類為「可採用」「需調整」「衝突」「我們不做」
- 在 UX_SPEC.md 中明確繼承哪些、為什麼不採用哪些

---

# 3. UX_SPEC.md 必含結構

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：UI/UX specialist 結論
優先級：最高

# UX_SPEC

## 0. 摘要

## 1. claude-UX prior draft 吸收結論
（採用 / 調整 / 拒絕 各分類，附理由）

## 2. /view-* 呈現設計（4 個 skill）

### 2.1 /view-world
（具體 Markdown 模板）

### 2.2 /view-character
...

## 3. /export-* 整合檔結構

## 4. /status 看板格式

## 5. REVIEW gate 清單格式

## 6. QA 報告閱讀體驗

## 7. 跨檔導航設計

## 8. 錯誤提示格式

## 9. [NEEDS_SCHEMA_SUPPORT] 回饋資料格式 specialist 的清單

## 10. 需 master 裁決問題清單
```

---

# 4. 給 specialist agent 的提醒

1. **這不是 GUI 設計** — 是「資料如何在 agent 對話與 markdown 中清晰呈現」
2. 所有設計都要能用純 markdown 表達（agent 對話中 render）
3. 不要設計需要互動的元素（沒有 button / form / dropdown）
4. **整合 claude-UX prior draft 是重要任務** — 不要重新發明
5. 如果 UX 需要的資料不在現有 schema 中，**不要擅自決定加欄位** — 標 `[NEEDS_SCHEMA_SUPPORT]` 回饋
6. 對話結束時交完整 UX_SPEC.md
