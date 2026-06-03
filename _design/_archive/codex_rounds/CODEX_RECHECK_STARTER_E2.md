狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX (e) NO-GO 3 minor finding 修補後的 targeted recheck 啟動包  
優先級：高

# CODEX_RECHECK_STARTER_E2 — CODEX (e) NO-GO 修補後的 targeted recheck

# 0. 本檔用途

CODEX (e) 短審查（CODEX_REVIEW_REPORT_E.md v0.1）判定 **NO-GO**：5 review item 中 E-1 / E-5 ✓，E-2 / E-3 / E-4 △，共 3 個 minor finding：

- **E-F1**：DF §8.3 user extension template_path 短路徑（與 §8.2 core / UD §3.10.2 不一致）
- **E-F2**：UD §3.10.2 引入 `user_extensions[*].algorithm` / `report_template` 欄位但 DF §8 schema/parser 未承接
- **E-F3**：DECISIONS_LOG header `狀態：FINAL` vs CODEX (e) checklist 要求 `LOCKED` wording 不一致

Master 第五輪已完成 3 finding 修補。本檔給「CODEX (e) recheck」對話啟動時用，scope **嚴限**驗證 3 finding 已修，不重審其他 review item。

**前置條件（必須先完成）：**

- ✓ CODEX (e) NO-GO 報告產出（CODEX_REVIEW_REPORT_E.md v0.1）
- ✓ Master 第五輪修補 3 finding 完成：
  - DF v0.4 §8.3 line 1904 template_path 改 repo-root 完整路徑
  - DF v0.4 §8.3 user_extensions 範例 + Instance-only 欄位表補 `algorithm` + `report_template` 為選填欄位
  - DF v0.4 §8.10 parser impact 補 algorithm / report_template parser 行為（不強驗內部結構）
  - DF v0.4 changelog 擴 §8.3 / §8.10 對齊紀錄
  - DECISIONS_LOG v1.1 §6.9.11 新增「文件狀態慣例澄清」段
- ✓ DF header 維持 v0.4（patch 屬同輪 cleanup，不再 bump）
- ✓ DECISIONS_LOG header 維持 v1.1

**本檔跟既有 starter 的差別：**

| 維度 | CODEX_REVIEW_STARTER_E | **本檔 CODEX_RECHECK_STARTER_E2** |
|---|---|---|
| 觸發時機 | partial supersede 升版完成 | **CODEX (e) NO-GO 修補完成** |
| Scope | 5 review item 全範圍 | **3 finding 驗證 only** |
| 預估時數 | 30-45 分 | **15-25 分**（嚴限 3 點）|
| 預期產出 | CODEX_REVIEW_REPORT_E.md | **CODEX_RECHECK_REPORT_E2.md（GO / NO-GO）** |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「CODEX (e) NO-GO 3 minor finding 修補後」的 targeted recheck（CODEX (e) 後續審查）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔、不改 spec
- 你是 targeted reviewer — 只驗證 CODEX_REVIEW_REPORT_E.md §3 列的 3 個 finding (E-F1 / E-F2 / E-F3) 已修
- 你是升 LOCKED 前 final-check — 通過 → master 進階段 9 升 LOCKED + Milestone 1；不通過 → 再一輪 patch
- 對應傳統：本輪是第 9 輪 CODEX 審查（前 8 輪：時期 A 4 輪 + (c) + (d) + (d2 Part1/2/3) + Gate 1/A.0.10 + (e)）

**重要邊界（嚴格 scope）：**

- ✗ **不**重審 Review-E-1（D-047 完整性）— 已 PASS ✓
- ✗ **不**重審 Review-E-5（跨檔 cross-ref）— 已 PASS ✓
- ✗ **不**重審 Review-E-2 / E-3 / E-4 已 PASS 的證據項，**只** verify §5 列的 3 patches 是否落地
- ✗ **不**動 D-001 ~ D-047 拍板結論
- ✗ **不**動 REQUIREMENTS_LOCK.md（v1.0 FINAL）
- ✗ **不**重審 Phase A.0 parser code（屬 Stage 0 範圍，已 PASS）
- ✗ **不**再列新 finding（除非 patch 引入新衝突；本輪不開 scope）

**本輪 scope（嚴格限定 — 3 個 finding 驗證）：**

### Recheck-E2-F1：DF §8.3 user extension template_path 路徑修補

**檢查對象：** `_design/DATA_FORMAT_SPEC.md` §8.3（line 1900-1935 附近）

**必看：**
- §8.3 user_extensions 範例 line 1904 `template_path` 值：應為 `09_quality_assurance/09_j_設定一致性檢查.md`（repo-root 完整相對路徑），**不是** v0.1 短路徑 `09_j_設定一致性檢查.md`
- §8.3 Instance-only 欄位表 `template_path` 列說明：應為「**repo-root 完整相對路徑**，如 `09_quality_assurance/09_j_...md`；對齊 §8.2 core 範例 + UD §3.10.2 寫法」
- 對齊一致性：與 §8.2 core 範例（template_path: 09_quality_assurance/09_a_ai味qa報告模板.md 等）+ UD §3.10.2 line 3646（也用 09_quality_assurance/ 完整路徑）+ qa_type_registry.template.yaml line 19-50（也用完整路徑）保持一致
- DF v0.4 changelog 應有對應紀錄段

**判定：** ✓ Pass / ✗ Fail

### Recheck-E2-F2：DF §8.3 + §8.10 補 `algorithm` / `report_template` schema/parser 承接

**檢查對象：** `_design/DATA_FORMAT_SPEC.md` §8.3 + §8.10

**必看：**
- §8.3 user_extensions 範例 (line 1909-1919 附近) 應含選填欄位：
  - `algorithm:` 區塊（含 step / metric / threshold 子結構）
  - `report_template: |` 區塊（多行字串）
- §8.3 Instance-only 欄位表應有兩列新增（line 1931-1932）：
  - `algorithm` | 否 | runtime algorithm 規則的宣告式表達（對應 UD §3.10.3 §2）；parser 不強驗內部結構
  - `report_template` | 否 | runtime 報告骨架字串（對應 UD §3.10.3 §3）；parser 不強驗內容
- §8.10 parser impact 段應補 algorithm / report_template parser 行為描述（不強驗、選填、存在性偵測、runtime 由 09_x 模板執行者消費）
- 對齊：UD v0.5 §3.10.2 lines 3650-3660 引入的這兩欄位現在已被 DF §8 user_extensions schema 承接
- DF v0.4 changelog 應明示 NEW_REQ_6 對齊擴充（line 33-37 範圍）

**判定：** ✓ Pass / ✗ Fail

### Recheck-E2-F3：DECISIONS_LOG header `狀態：FINAL` 慣例澄清

**檢查對象：** `_design/DECISIONS_LOG.md` §6.9.11（line 1371-1383 附近）

**必看：**
- §6.9.11 新增段，標題「文件狀態慣例澄清（CODEX (e) recheck Finding E-F3 — 2026-05-19）」
- 內文應明示：
  - DECISIONS_LOG 性質是「決策事實紀錄」+ 持續追加（對齊 §0 / §7 紀律）
  - `狀態：FINAL` 表示「v1.1 已紀錄項目 final」（D-001 ~ D-047 + P-019 + P-021~P-030 拍板結論不再翻案，新議題開新 §6.x + 新 D-NNN）
  - **不**等同 spec 體 LOCKED（如 SPEC.md / ARCH.md 「整檔內容凍結」）
  - LOCKED gate 檢查條件對 DECISIONS_LOG 應視為「status=FINAL + 當前版本 v1.1 已含 §6.9」為 PASS 等價條件
  - 同 REQUIREMENTS_LOCK.md 慣例 FINAL（兩者皆「決策 / 需求事實檔」非 spec 體）
- DECISIONS_LOG header 維持 `狀態：FINAL`（**不**改 LOCKED — 此為慣例）

**判定：** ✓ Pass / ✗ Fail

---

**必讀文件（按順序）：**

A. 對齊基準
1. _design/CODEX_REVIEW_REPORT_E.md（v0.1 — 3 finding 描述基準）

B. 本輪審查對象（核心）
2. _design/DATA_FORMAT_SPEC.md（v0.4 — §8.3 line 1900-1935 / §8.10 line 1997-2010 / changelog line 1-45）
3. _design/DECISIONS_LOG.md（v1.1 — §6.9.11 line 1371-1383 附近 + header line 1-5 確認 FINAL）

C. 對齊參考（不審；當依據）
4. _design/UPSTREAM_DOWNSTREAM_SPEC.md（v0.5 — §3.10.2 line 3630-3666 / §3.10.3 line 3726；確認 algorithm / report_template 欄位在 UD 端的原始位置）
5. _design/registries/qa_type_registry.template.yaml（v0.3 — line 13-50 完整 template_path 對齊基準）

---

**你要交付的產物：**

新建：`_design/CODEX_RECHECK_REPORT_E2.md`

報告格式：

```markdown
狀態：REVIEW  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX (e) NO-GO 3 finding 修補 targeted recheck  
優先級：高  

# CODEX_RECHECK_REPORT_E2 — CODEX (e) NO-GO 修補驗證

## 0. 摘要

**結論：[GO / NO-GO]**

3 finding：
- E-F1 DF §8.3 template_path 路徑修補：✓/✗
- E-F2 DF §8.3 + §8.10 algorithm/report_template 承接：✓/✗
- E-F3 DECISIONS_LOG FINAL 慣例澄清：✓/✗

## 1. 審查範圍

### 1.1 Files Read
（列你實際讀的檔案 + line range）

### 1.2 Files NOT Modified
（明示沒動的檔案；應為所有檔；報告本身是唯一新建）

## 2. 3 finding 驗證

### Recheck-E2-F1：DF §8.3 template_path 路徑
- 狀態：✓/✗
- 證據：（line ref + 評語）

### Recheck-E2-F2：DF §8.3 + §8.10 algorithm/report_template
- 狀態：✓/✗
- 證據：

### Recheck-E2-F3：DECISIONS_LOG FINAL 慣例
- 狀態：✓/✗
- 證據：

## 3. Go / No-Go 決定

- **GO：** 3 finding 全 ✓ → master 進階段 9 升 LOCKED + Milestone 1
- **NO-GO：** ≥ 1 ✗ → 再一輪 patch + 第三輪 recheck

## 4. Source Limitations

（你實際讀的檔；不審範圍；任何依靠假設的判斷）
```

---

**Go / No-Go 判定指引：**

- **GO：** 3 finding 全 ✓
- **NO-GO：** ≥ 1 ✗

請開始。
```

---

# 2. 完成條件 + master 第五輪後續

CODEX (e) recheck 完成 = 以下全部 ✓：

```
✓ _design/CODEX_RECHECK_REPORT_E2.md 產出
✓ 3 finding 全逐項給 ✓/✗ + 證據
✓ §3 GO / NO-GO 結論
✓ 沒動任何 spec 文件
```

CODEX 完成後：
- User 手動 commit + push report
- master 第五輪 read 報告
- 若 GO → 進階段 9 升 LOCKED + Milestone 1 通知
- 若 NO-GO → master 看殘留 + 一輪 patch + recheck E3

---

# 3. 文件維護紀律

- 本檔是「**CODEX recheck 啟動包**」；完成後 archive 進 `_design/archive/` 或留作歷史
- 本檔產出後若需修補，改本檔 + 升 v0.2，**不**重發 prompt
