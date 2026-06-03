狀態：DRAFT  
版本：v1.0（9th master 第二段對話接手包；Wave 13 落地 + Round 1-4 review cycle 收尾後切換點；Wave 14-16 + 10th handoff scope）  
最後更新：2026-05-22  
適用範圍：給「9th master 第二段對話」接手 — Wave 14-16 + HANDOFF_TO_10TH_MASTER 撰寫 scope  
優先級：最高

# HANDOFF_9TH_MASTER_CONTINUATION — 9th master 第二段對話接手包

# 0. 文件目的

9th master 第一段對話（2026-05-22）已完成：cleanup queue + Wave 12 + Wave 13。期間經歷 Round 1-4 review cycle（4 輪 NO-GO/NEAR-GO + 3 輪 inline patch round + 1 輪 hard-limit accept）累積 ≥ 70-80% context window；依 user 拍板 Path A 切換新對話進 Wave 14-16 + 10th handoff。

**本檔限縮 scope（vs 完整 HANDOFF_TO_9TH_MASTER.md v1.0）：** 只覆蓋 9th master 剩餘工作 — Wave 14-16 + HANDOFF_TO_10TH_MASTER。Wave 12 / 13 / cleanup queue / Round 1-4 cycle 已完成不再覆蓋；新對話 master 不必重做。

---

# 1. 對話啟動指令（直接複製到新對話）

```
我是 game-dialogue-bible 專案的使用者。第九輪 master 第一段對話完成 cleanup queue + Wave 12 (00_j + 5 /iterate-* + /iterate-scene --split-to-file) + Round 1-4 review cycle + Wave 13 (4 個 /view-* skill)。

第一段對話累積 ≥ 70-80% context window 後切到新對話。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「9th master 第二段對話」。

**第一步必讀（按順序，4 份；比第一段 8 份大幅縮小）：**
1. _design/HANDOFF_9TH_MASTER_CONTINUATION.md（本檔；你的 scope）
2. _design/POST_LOCK_PENDING.md v0.18（含 9th master Round 1-4 完整處理紀錄 + 5 條教訓內化 + 未處理項推 10th master）
3. _design/HANDOFF_TO_9TH_MASTER.md v1.0（原 9th master 整體 scope；只看 §3.3-§3.5 Wave 13-15 範圍 + §4-§7 風險警示 + 教訓）
4. _design/D054_DECISION_PACKAGE.md v0.2（D-054 hybrid 拍板包；Wave 14 /export-* + Wave 15 Canon Delta 框架可能 reference）

**第二步精選讀（碰到才看）：**
5. _design/TASKS.md v1.9 §C.4 + §C.5 + §C.5a + §C.6 + §C.7（Wave 14 + 15 + 16 task spec）
6. _design/ARCHITECTURE.md v1.6 §4.2 (/export-*) + §4.2a (L3 Export prompt 生成器；屬 10th master scope 但 schema 確認屬 Wave 14)
7. _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2（Wave 14 schema 對齊）
8. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5 §5 Canon Delta（Wave 15 框架紀錄）

**第三步補充背景（第一段對話事實檔；碰到才看）：**
9. _design/CODEX_D6_STARTER.md v0.1（D6 完整 starter；Wave 14 D10/D14 寫類似完整 starter 時範本參考）
10. _design/CODEX_D_VIEW_BATCH_STARTER.md v0.1（Wave 13 batch starter；Wave 14/15 batch 寫範本參考）
11. _design/CODEX_9TH_MASTER_*_REVIEW_REPORT.md（Round 1-4 review reports；屬 immutable history）

**你的 scope（9th master 第二段；4 個 task）：**

1. **Wave 14**（4 個 /export-* starter + L3 Export schema 確認）：採新工作模式
   - Master 寫 D10 完整 starter（/export-world）
   - Master 寫 CODEX_D_EXPORT_BATCH_STARTER (D11-D13)
   - CODEX 跑兩輪寫 8 個 SKILL.md（含中文 wrapper）
   - L3 Export schema 確認（不實作；屬 10th master Phase A.0F.x）

2. **Wave 15**（/diagnose + /integrate + Canon Delta 框架紀錄）：
   - Master 寫 D14 完整 starter（/diagnose）或 batch starter for D14+D15
   - 寫 _design/CANON_DELTA_FRAMEWORK.md（屬 framework reference；不實作 skill）

3. **Wave 16**（Phase D 整體驗收 + PHASE_D_COMPLETION_REPORT v1.0）：
   - 寫 CODEX_D_FINAL_STARTER.md
   - CODEX 跑驗收 + 撰寫 PHASE_D_COMPLETION_REPORT v1.0
   - **Milestone 4 接近條件聲明**（非達成；Phase A.0F 屬 10th master scope）

4. **寫 HANDOFF_TO_10TH_MASTER.md**：
   - 接 Phase A.0F 前端工具補完（A.0F.3~A.0F.11 + 整體驗收）+ Milestone 4 真正封版

**禁止越界（沿用第一段 + 新增）：**
- 不重做設計（已 LOCKED）
- 不改 D-001~D-054 拍板結論
- 不擅啟 Phase A.0F 實作（屬 10th master scope）
- 不重審 9th master 第一段已 accepted finding（Round 1-4 cycle 結論不重議）
- 不擅自開新 inline patch round 處理 NEW_REQ_9 / R2-MAJOR-03 hard-limit accept 項（推 10th master）

**第一段對話 5 條教訓內化（你必須在 Wave 14+ 工作開始前 grok）：**
1. **Master 跑 baseline 必須以 Windows 端為權威**：sandbox virtiofs cache 在某些 check_paths case 會 false negative；sandbox 跑出的 ERROR 數可能低於 Windows 實測；只能作 noise 對照
2. **Cascade sweep 必須擴及 broader pattern grep**：CODEX review 列出的具體 hits 是 sample 抽樣；master inline patch sweep 必須對全 repo 跑 broader pattern grep 確保 cleanup
3. **Master 寫 starter 涉及 SPEC frontmatter 段須直接 grep SPEC §5.2 verify**：不可憑記憶寫具體欄位數字
4. **Master 寫 supersede note 要避免重複 finding 內精確詞串**：strict grep 不分否定句 / 歷史 narrative；wording 應描述「修補性質」而非重述被改的字串本身
5. **Master 寫 review starter 時 diff anchor 必須精確**：不要假設 user commit composition；推薦明示 commit hash 或 `HEAD~1..HEAD` 限定最後一個 commit

**新工作模式（9th master 第一段拍板；Wave 14-15 沿用）：**
- Master 寫 batch wave 的第 1 個完整 starter（D10 for Wave 14；D14 for Wave 15）
- Master 寫 batch starter for 其他 N 個（D11-D13 for Wave 14；D15 if needed for Wave 15）
- CODEX 跑兩輪：實作 D10/D14 完整 → 實作 batch
- Master 內部 review 一致性（grep 結構 + read 重點 section；不必跑 CODEX review starter — 第一段 Round 1-4 cycle 證明 review cycle 太長；trust but verify by master 端內部 grep）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 4 份必讀後對 scope + Wave 14-16 工作順序 + 5 條教訓內化的理解，再開始處理。
```

---

# 2. 當前狀態快照（9th master 第一段結束時 — 2026-05-22）

## 2.1 設計層狀態

| 檔 | 版本 | 狀態 | 9th master 第一段變動 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | FINAL | 不動 |
| `_design/DECISIONS_LOG.md` | v2.0 | FINAL | 不動（D-001~D-054 維持）|
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | LOCKED | 不動 |
| `_design/SPEC.md` | v1.2 | LOCKED | 不動 |
| `_design/ARCHITECTURE.md` | v1.6 | LOCKED | 不動 |
| `_design/TASKS.md` | v1.9 | LOCKED | 不動 |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | LOCKED | 不動 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | LOCKED | 不動 |
| `_design/UX_SPEC.md` | v0.4 | LOCKED | 不動（§11 屬 Phase A.0F；10th master scope）|
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | LOCKED | 不動；Wave 14 schema 對齊 reference |
| `_design/POST_LOCK_PENDING.md` | **v0.18** | DRAFT | 9th master 第一段大幅升版；含 NEW_REQ_19 處理紀錄 + Round 1-4 cycle 全紀錄 + 5 條教訓內化 |
| `_design/D054_DECISION_PACKAGE.md` | v0.2 | APPLIED | 不動 |
| `_design/PHASE_C_COMPLETION_REPORT.md` | v1.0 | DRAFT | 不動（Milestone 3 達成事實檔）|
| `_design/PHASE_B_COMPLETION_REPORT.md` | **v1.4** | DRAFT | 9th master 第一段升 v1.3 (cleanup) → v1.4 (Round 1 inline patch sweep) |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | DRAFT | 不動 |

## 2.2 Protocol + skill 落地狀態

| 檔 | 版本 | 9th master 第一段變動 |
|---|---|---|
| `00_protocol/00_a~00_l`（10 protocol）| mixed | **只動 00_k v0.1 → v0.2**（R8-INFO-06）+ **新建 00_j v0.2** |
| `08_dialogue_outputs/08_a` | **v0.4** | 9th master 第一段升 v0.2 → v0.3 (cleanup) → v0.4 (Round 1 sweep) |
| `.claude/skills/`（既有 16 個 SKILL.md）| mixed | 全不動 |
| **Wave 12 新建（6 SKILL.md 待 CODEX D.1-D.5 task 實作）** | — | starter v0.1 → v0.3/v0.4；SKILL.md 屬 CODEX implementer task 範圍 — 9th master 第二段不需要重做 |
| **Wave 13 新建（8 SKILL.md 已落地）** | v0.1 | view-world / view-character / view-outline / view-detailed-outline + 4 中文 wrapper（CODEX D.6 + batch task 跑完）|

## 2.3 Baseline（Windows 端權威）

- `check_headers.py`: 0 ERROR / 44 WARN / 162-165 files
- `check_paths.py`: **247 ERROR**（**R2-MAJOR-03 hard-limit accept**；NEW_REQ_9 既有 baseline debt 推 10th master）
- `build_repo_index('.')`: 0 ERROR / 81 WARN / 213-224 files

**Wave 14+ baseline 門檻：** `check_paths.py ≤ 247 ERROR`（與 9th master 第一段相同）。

## 2.4 9th master 第一段已完成（細節摘要；新對話不必重做）

### Phase 1：Cleanup queue（Task 1-6）

- 00_k v0.1 → v0.2（5→8 報告對齊 D-043 + UD §2.5.3 v0.3 序列 + FINAL gate 9-status）
- phase_b_review_log v0.5→v0.6 + PHASE_B v1.2→v1.3 + CODEX_B9_STARTER v0.4→v0.5（R10-MI-01/02/03 sweep）
- AGENTS.md / CLAUDE.md v0.1 → v0.2（Phase B+ skill table TBD → ✅）
- POST_LOCK_PENDING NEW_REQ_19 處理紀錄 + R10-MA-01 ack
- 08_a v0.2 → v0.3（§11.1 5 → 8 對齊 D-043）

### Phase 2：Wave 12 starter set（Task 7；含 D-054 NEW_REQ_15 落地）

- 00_protocol/00_j_迭代協議.md v0.2（共通基底）
- CODEX_D1_STARTER v0.3 (/iterate-world；共通範本)
- CODEX_D2/D3/D4_STARTER v0.3 (各引用 D1)
- CODEX_D5_STARTER v0.4 (/iterate-detailed-outline + /iterate-scene --split-to-file；D-054 落地)

### Phase 3：Round 1-4 review cycle + inline patch（Task 13-20 + 4 輪 trivial patch）

- Round 1 NO-GO (3 MAJOR + 7 MINOR + 3 INFO) → inline patch 全處理
- Round 2 NO-GO (3 MAJOR + 2 MINOR + 2 INFO) → inline patch + R2-MAJOR-03 hard-limit accept (baseline)
- Round 3 NEAR-GO (1 MAJOR trivial wording) → inline patch
- Round 4 NEAR-GO (1 MAJOR diff anchor 設定) → hard-limit accept
- POST_LOCK_PENDING v0.13 → v0.18（含完整處理紀錄 + 5 條教訓內化）

### Phase 4：Wave 13 starter set + CODEX implementer 兩輪（Task 8）

- CODEX_D6_STARTER v0.1 (/view-world；完整範本；採新工作模式)
- CODEX_D_VIEW_BATCH_STARTER v0.1 (D7-D9 batch)
- CODEX D.6 task → `view-world` + `查看世界觀` 2 SKILL.md
- CODEX batch task → `view-character` + `view-outline` + `view-detailed-outline` + 3 中文 wrapper（含 D9 D-054 hybrid fallback）
- Master 內部 verify：4 個 view-* skill 結構對齊 D6 範本 11 段；D9 D-054 hybrid fallback 完整實作（Phase 1 per-scene first + Phase 2 aggregate fallback + missing placeholder + read_source 紀錄 + 不觸發 split-to-file 紀律）

---

# 3. 9th master 第二段工作清單

## 階段 1：Wave 14 — 4 個 /export-* starter + L3 Export schema 確認

**對應 TASKS：** §C.5 + §C.5a

**對應 ARCH：** §4.2 (/export-*) + §4.2a (L3 Export prompt 生成器；屬 10th master)

### 新工作模式（沿用 Wave 13）

- Master 寫 D10 完整 starter (CODEX_D10_STARTER.md — /export-world；共通範本)
- Master 寫 CODEX_D_EXPORT_BATCH_STARTER.md (D11-D13)
- CODEX 跑 D.10 task → /export-world + /匯出世界觀 2 SKILL.md
- CODEX 跑 batch task → 6 SKILL.md (/export-character + /export-outline + /export-detailed-outline + 3 中文 wrapper)

### /export-* 與 /view-* 的差異（關鍵）

| 維度 | /view-* (Wave 13)| /export-* (Wave 14)|
|---|---|---|
| 輸出目標 | chat | `view/<entity>.md` 整合檔 |
| 寫檔 | 不寫檔 | 寫檔（DERIVED 狀態）|
| Breadcrumb | 不加 | **必加**（frontmatter 之後、第一個 `#` 之前）|
| TOC | 不加 | **預估 > 200 行加**（GFM slug；skill 內部驗證 slug 一致性 — DECISIONS_LOG P-005）|
| 返回連結 | 不加 | **末尾加** `[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)`（P-004）|
| 邊界 | 純讀取 7 條 | **D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2**（寫檔目錄表限 `view/`）|
| Source 反查 | 與 view 相同 | 與 view 相同（共用組合邏輯）|

### D10 starter 核心內容

對齊 D6 starter 結構但加：
- 寫檔目錄 `view/世界觀.md`（DERIVED 狀態）
- frontmatter 含「組合來源」段落（依 ARCH §4.2 line 753-769 範本）
- 邊界三 block（D-050 + D-053 + 寫檔目錄表）
- breadcrumb + TOC + 返回連結紀律

### L3 Export schema 確認（非實作）

- 對照 `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 §1.1（5 區塊：標題 + YAML 元資料 + 步驟 + 約束 + 完成回報）
- 確認 Wave 14 /export-* 寫出的 view/<entity>.md 結構跟 L3 schema 對得上
- L3 prompt 生成器本身屬 Phase A.0F.x（10th master scope）— 本 Wave 不實作

### 預估工時

- Master 寫 D10 完整 + batch starter：1.5-2h
- CODEX 跑 D.10 + batch（user 端外部）：~3-4h
- Master 內部 verify 一致性：5-15 分

## 階段 2：Wave 15 — /diagnose + /integrate + Canon Delta 框架紀錄

**對應 TASKS：** §C.6

### 工作切分

**選項 A（推薦）：** Master 寫 D14 完整 starter (/diagnose) + batch starter (D15 /integrate)
**選項 B：** Master 寫一份合併 starter for D14 + D15（兩 skill 一份）— 因為 /diagnose + /integrate 都不綁特定 protocol，relatively similar

### /diagnose vs /integrate 職責

- **/diagnose** 對應 00_a §3.3 診斷模式 — 跨檔診斷（找衝突 / LOCKED 變動 / orphan 實體）；**只找問題不修**
- **/integrate** 對應 00_a §3.4 整理模式 — 整合 merge 跨 source；**可寫檔但需 user 拍板**

### Canon Delta 框架紀錄（不實作 skill）

- 寫 `_design/CANON_DELTA_FRAMEWORK.md` v0.1
- 對齊 `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §5（含 5.1 識別 / 5.2 抽取演算法 / 5.3 提案流程 / 5.4 回寫執行 / 5.5 與既有實體互動）
- 屬「成熟期功能 framework reference」；後續 user 跑 09_e + /iterate-* 走真正 Canon Delta 回寫時 reference

### 預估工時

- Master 寫 D14/D15 starter（或合併 starter）：1-2h
- Master 寫 CANON_DELTA_FRAMEWORK.md：30-60 分
- CODEX 跑 D.14/D.15 task：~3h

## 階段 3：Wave 16 — Phase D 整體驗收 + PHASE_D_COMPLETION_REPORT v1.0

### 工作切分

- Master 寫 `CODEX_D_FINAL_STARTER.md` v0.1（同 Phase B/C COMPLETION_REPORT starter pattern）
- CODEX 跑驗收 + 撰寫 `_design/PHASE_D_COMPLETION_REPORT.md` v1.0
- §6 user 親跑 placeholder（同 PHASE_C；NEW_REQ_14 AI-assisted 機制可用）

### Milestone 4 紀律（嚴守 wording）

Phase D 完成 **≠** Milestone 4 達成。

- Phase D 完成宣告：4 維度 PASS（CODEX 端驗收）
- Milestone 4 達成需要 **Phase A.0F 前端工具補完**（屬 10th master scope）
- Wave 16 PHASE_D_COMPLETION_REPORT 應宣告 **「Milestone 4 接近條件達成」**（非達成）

### 預估工時

- Master 寫 D_FINAL_STARTER：1h
- CODEX 跑驗收 + report：~3h

## 階段 4：寫 HANDOFF_TO_10TH_MASTER.md

對齊 HANDOFF_TO_9TH_MASTER pattern：

- 9th master 全程已完成事實（cleanup + Wave 12-16 + 整輪 4 wave starter + 4 輪 review cycle 教訓內化）
- Phase A.0F 前端工具補完範圍（A.0F.3~A.0F.11 + 整體驗收；TASKS §A.0F + UX_SPEC §11 11 個 feature spec）
- Milestone 4 真正封版條件
- 5 條教訓內化 + 9th master 第一段 / 第二段教訓全紀錄
- NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18 推 11+ 輪 master scope 紀錄

### 預估工時

- 1.5-2h

---

# 4. 風險警示 + 紀律

## 4.1 Context window 管理

9th master 第二段對話內也要小心 context 累積。預估工作量：

| 階段 | Master 工時 | Context 消耗預估 |
|---|---|---|
| Wave 14（D10 完整 + batch + L3 schema）| 1.5-2h | 中（同 Wave 13；~25-30%）|
| Wave 15（D14/D15 + Canon Delta 框架）| 1.5-3h | 中（~25%）|
| Wave 16（D_FINAL_STARTER）| 1h | 小（~10%）|
| HANDOFF_TO_10TH_MASTER | 1.5-2h | 中（~20-25%）|

**total 預估 80-90% context**。可能需要再分一次切換。

**建議切換點：** Wave 14 完成 + Wave 15 完成 是自然的 commit checkpoint。若新對話跑到 Wave 15 後感覺 context 接近 70%，建議寫 `HANDOFF_9TH_MASTER_CONTINUATION_PART3.md` 切第三段對話。

## 4.2 嚴守新工作模式（避免重蹈 Wave 12 覆轍）

第一段 Wave 12 教訓：master 一輪寫 5 個 starter (~1500 行) → 後段品質下降 (D3/D4 兩層 indirection / D5 結構混亂) → Round 1-4 review cycle 4 輪修補。

**Wave 14 / 15 新工作模式紀律：**
- Master 寫第 1 個完整 starter（D10 / D14）
- Master 寫 batch starter for 其他 N 個（D11-D13 / D15）
- 不要一輪寫 4 個完整 starter；要善用 batch 模式

## 4.3 NEW_REQ_9 baseline debt 不在 9th master scope

- check_paths 247 ERROR 屬 27 模板 old-style filename reference (`01A/01B/02A/05D` 大寫格式)
- 9th master 第一段已 hard-limit accept；推 10th master 評估
- **第二段不要試圖修這 247 ERROR**（屬 LOCKED 模板；要動需新 D-NNN 拍板）
- 維持 baseline ≤ 247 ERROR 即可

## 4.4 5 條教訓內化（強制）

第一段 Round 1-4 cycle 證明：master 不嚴格紀律 → 4 輪 review cycle 反覆失敗。第二段必須在每個 wave 開始前 grok 5 條教訓：

1. **Windows baseline 權威**：跑 `check_paths.py` 看 sandbox 結果只當 noise 對照；POST_LOCK_PENDING v0.18 內 baseline 247 是 Windows 端權威
2. **Cascade sweep broader pattern**：每次 starter 寫好後跑 grep 全 _design/ 看 stale；不只看 review 列具體 hits
3. **SPEC frontmatter 段直接 grep verify**：寫 starter 涉及 frontmatter 描述前 grep SPEC §5.2；不憑記憶
4. **Supersede note 避免重複 finding 內精確詞串**：寫 patch round 紀錄時用「修補性質」描述；不重述被改字串
5. **Review starter diff anchor 精確**：如果跑 review starter 用明示 commit hash 或 `HEAD~1..HEAD`

## 4.5 9th master 第一段內部 review 模式（vs CODEX review starter）

第一段 Wave 13 跳過 CODEX review starter；改 master 端內部 verify（grep 結構 + read 重點 section）。理由：
- Round 1-4 cycle 4 輪 wall-time 證明 CODEX review starter cycle 太長
- View skill 結構簡單（11 段對齊 D6 範本）；內部 grep verify 夠
- 第一段 Wave 13 內部 verify PASS（4 個 SKILL.md 結構齊全 + D9 D-054 hybrid fallback 完整）

**第二段建議：**
- Wave 14（/export-*）：內部 verify（grep 結構 + check breadcrumb / TOC / 返回連結紀律）
- Wave 15（/diagnose + /integrate）：內部 verify
- Wave 16（PHASE_D_COMPLETION_REPORT）：跑 CODEX review starter（屬最終驗收；屬重要 milestone）

## 4.6 sandbox virtiofs cache stale（已知）

工作目錄 Windows 端為權威。Sandbox 端 baseline 結果偶爾 false negative。對重要 baseline assertion 一律以 Windows 端為準（或讓 CODEX 跑 baseline — CODEX 在 Codex 環境跑時是 Windows 端）。

---

# 5. 完成條件

9th master 第二段對話完成 = 以下全部 ✓：

```
✓ Wave 14 — D10 完整 starter + batch starter D11-D13 + CODEX 跑兩輪寫 8 SKILL.md + L3 Export schema 確認
✓ Wave 15 — D14/D15 starter（合併或拆）+ CODEX 跑寫 4 SKILL.md + CANON_DELTA_FRAMEWORK.md v0.1
✓ Wave 16 — CODEX_D_FINAL_STARTER + CODEX 跑 PHASE_D_COMPLETION_REPORT v1.0
✓ Milestone 4 接近條件聲明（非達成；Phase A.0F 推 10th master）
✓ 寫 HANDOFF_TO_10TH_MASTER.md
```

---

# 6. 文件維護紀律

- 本檔是「接手指南」，9th master 第二段對話讀完後**不需要更新本檔**
- 第二段完成後可把本檔 archive 進 `_design/archive/`
- 真正完整 HANDOFF_TO_10TH_MASTER.md 由第二段對話寫；對齊 HANDOFF_TO_9TH_MASTER v1.0 pattern

---

# 7. Cross-ref

- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master 整體 scope；本檔是其縮限版）
- `_design/POST_LOCK_PENDING.md` v0.18（Round 1-4 完整處理紀錄 + 5 條教訓內化 + 未處理項推 10th master）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.4 / `_design/PHASE_C_COMPLETION_REPORT.md` v1.0
- `_design/TASKS.md` v1.9 §C.4-§C.7（Wave 14-16 task spec）
- `_design/ARCHITECTURE.md` v1.6 §4.2 + §4.2a + §6 (Phase D 整體架構)
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（Wave 14 schema reference）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §5（Wave 15 Canon Delta framework）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 推 NEW_REQ_15 monitor）
- `_design/CODEX_D6_STARTER.md` v0.1 / `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1（Wave 13 範本參考）
- `.claude/skills/view-world/SKILL.md` v0.1 + 7 個 view-* / 中文 wrapper SKILL.md v0.1（Wave 13 落地參考）
- `_design/CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_REPORT.md` v0.1 + ROUND2/3/4 REPORTS（Round 1-4 cycle immutable history）
