狀態：REVIEW  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX (e) NO-GO 3 finding 修補 targeted recheck  
優先級：高  

# CODEX_RECHECK_REPORT_E2 — CODEX (e) NO-GO 修補驗證

## 0. 摘要

**結論：GO**

3 finding：
- E-F1 DF §8.3 template_path 路徑修補：✓
- E-F2 DF §8.3 + §8.10 algorithm/report_template 承接：✓
- E-F3 DECISIONS_LOG FINAL 慣例澄清：✓

## 1. 審查範圍

### 1.1 Files Read

- `_design/CODEX_REVIEW_REPORT_E.md`：lines 140-159（E-F1 / E-F2 / E-F3 原 finding 描述）；另以 targeted search 確認本輪 E report 摘要與 NO-GO 判定相關行。
- `_design/DATA_FORMAT_SPEC.md`：lines 1-45（v0.4 changelog）、1834-1878（§8.2 core template_path 基準）、1886-1935（§8.3 user_extensions + 欄位表）、2016-2028（§8.10 parser impact）。
- `_design/DECISIONS_LOG.md`：lines 1-5（header）、1371-1383（§6.9.11 慣例澄清）。
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`：lines 3624-3666（§3.10.2 user_extensions 範例）、3713-3726（§3.10.3 algorithm 欄位來源）。
- `_design/registries/qa_type_registry.template.yaml`：lines 13-50（core qa_type template_path 基準）。

### 1.2 Files NOT Modified

- 未修改 `_design/DATA_FORMAT_SPEC.md`。
- 未修改 `_design/DECISIONS_LOG.md`。
- 未修改 `_design/UPSTREAM_DOWNSTREAM_SPEC.md`。
- 未修改 `_design/registries/qa_type_registry.template.yaml`。
- 未修改 `_design/CODEX_REVIEW_REPORT_E.md`。
- 本輪唯一新建檔案：`_design/CODEX_RECHECK_REPORT_E2.md`。

## 2. 3 finding 驗證

### Recheck-E2-F1：DF §8.3 template_path 路徑

- 狀態：✓
- 證據：
  - 原 finding 指出 DF §8.3 `template_path` 使用短路徑，與 §8.2、UD §3.10.2、registry template 的 repo-root 完整相對路徑不一致（`_design/CODEX_REVIEW_REPORT_E.md` lines 140-144）。
  - DF v0.4 changelog 已記錄 E-F1 修補：§8.3 範例 `template_path` 短路徑改為 `09_quality_assurance/09_j_設定一致性檢查.md`，欄位表說明改為 repo-root 完整相對路徑（`_design/DATA_FORMAT_SPEC.md` lines 32-34）。
  - DF §8.2 core 範例已使用 `09_quality_assurance/...` 完整相對路徑（`_design/DATA_FORMAT_SPEC.md` lines 1834-1878）。
  - DF §8.3 user_extensions 範例 line 1904 已是 `09_quality_assurance/09_j_設定一致性檢查.md`；欄位表 line 1929 明示 `template_path` 是 repo-root 完整相對路徑，並對齊 §8.2 core 範例 + UD §3.10.2 寫法。
  - UD §3.10.2 line 3646 與 `qa_type_registry.template.yaml` lines 19-47 也維持 `09_quality_assurance/...` 路徑風格。

### Recheck-E2-F2：DF §8.3 + §8.10 algorithm/report_template

- 狀態：✓
- 證據：
  - 原 finding 指出 UD §3.10 已引入 `user_extensions[*].algorithm` / `report_template`，但 DF §8.3 與 §8.10 尚未承接（`_design/CODEX_REVIEW_REPORT_E.md` lines 146-150）。
  - DF v0.4 changelog 已記錄 NEW_REQ_6 對齊：§8.3 範例 + Instance-only 欄位表補 `algorithm` / `report_template` 為選填欄位，§8.10 parser impact 補「選填、parser 不強驗內部結構」描述（`_design/DATA_FORMAT_SPEC.md` lines 35-36）。
  - DF §8.3 user_extensions 範例 lines 1909-1919 已含 `algorithm:` 區塊，子結構含 `step` / `metric` / `threshold`，並含 `report_template: |` 多行字串。
  - DF §8.3 Instance-only 欄位表 lines 1931-1932 已新增 `algorithm` / `report_template` 兩列，均標示非必填；`algorithm` 說明 parser 不強驗內部結構，`report_template` 說明 parser 不強驗內容。
  - DF §8.10 lines 2022-2025 已明示兩欄為選填，parser 做存在性偵測、存入 RegistryEntry、不強驗內部 schema，runtime 由 09_x 模板執行者消費，漏填不報錯。
  - UD §3.10.2 lines 3650-3660 的 `algorithm` / `report_template` 與 UD §3.10.3 lines 3724-3726 的 algorithm 欄位來源，已被 DF §8.3 / §8.10 承接。

### Recheck-E2-F3：DECISIONS_LOG FINAL 慣例

- 狀態：✓
- 證據：
  - 原 finding 指出 DECISIONS_LOG header 為 `狀態：FINAL`，但 checklist wording 可能被解讀為應是 LOCKED，因此需明示例外或改狀態（`_design/CODEX_REVIEW_REPORT_E.md` lines 152-156）。
  - DECISIONS_LOG header 維持 `狀態：FINAL`（`_design/DECISIONS_LOG.md` line 1），符合本輪要求「不改 LOCKED」。
  - §6.9.11 標題已新增「文件狀態慣例澄清（CODEX (e) recheck Finding E-F3 — 2026-05-19）」（`_design/DECISIONS_LOG.md` line 1371）。
  - §6.9.11 明示 DECISIONS_LOG 是「決策事實紀錄」且持續追加，對齊 §0 / §7 維護紀律（line 1375）。
  - §6.9.11 明示 `狀態：FINAL` 表示 v1.1 已紀錄項目 final，D-001 ~ D-047 + P-019 + P-021~P-030 拍板結論不再翻案，新議題開新 §6.x + 新 D-NNN；同句明示不等同 SPEC.md / ARCH.md 這類 spec 體 LOCKED（line 1376）。
  - §6.9.11 明示 LOCKED gate 對 DECISIONS_LOG 的 PASS 等價條件為 `status=FINAL + 當前版本 v1.1 已含 §6.9 升 v1.1 紀錄`（line 1377）。
  - §6.9.11 明示同 REQUIREMENTS_LOCK 慣例 FINAL，兩者皆為「決策 / 需求事實檔」非 spec 體（lines 1378-1380）。

## 3. Go / No-Go 決定

- **GO：** 3 finding 全 ✓ → master 進階段 9 升 LOCKED + Milestone 1
- **NO-GO：** 不成立；本輪未見 ≥ 1 ✗。

## 4. Source Limitations

- 本輪是 targeted recheck，只驗證 CODEX_REVIEW_REPORT_E.md §3 所列 3 個 minor finding：E-F1 / E-F2 / E-F3。
- 未重審 Review-E-1（D-047 完整性）、Review-E-5（跨檔 cross-ref），也未重審 Review-E-2 / E-3 / E-4 已 PASS 的完整證據項。
- 未重審 D-001 ~ D-047 拍板結論。
- 未讀、未修改 `REQUIREMENTS_LOCK.md`；本輪僅依 DECISIONS_LOG §6.9.11 對其 FINAL 慣例的引用作 E-F3 判斷。
- 未重審 Phase A.0 parser code；DF §8.10 parser impact 僅檢查文字承接是否存在。
- 未開新 finding；僅檢查 patch 是否引入與 3 finding 直接相關的新衝突。本輪未見此類衝突。
