狀態：REVIEW  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX (e) 短審查 — master 第五輪 partial supersede 升版驗證  
優先級：高  

# CODEX_REVIEW_REPORT_E — Master 第五輪升版 review

## 0. 摘要

**結論：NO-GO**

5 review item：
- E-1 D-047 完整性：✓
- E-2 NEW_REQ_4 + 同類 cleanup：△
- E-3 NEW_REQ_6：△
- E-4 4 主 spec 升版一致性：△
- E-5 跨檔 cross-ref：✓

NO-GO 理由：本輪有 3 個 △。其中 E-2 / E-3 是 DF §8.3 與 UD §3.10 的 user_extensions schema / path 表達殘留；E-4 是 checklist 要求 5 spec header 狀態一致為 LOCKED，但 DECISIONS_LOG 仍為 FINAL。依本輪判定規則，≥2 △ 即 NO-GO，建議一輪小型 partial supersede patch 後再 recheck。

## 1. 審查範圍

### 1.1 Files Read

- `_design/REQUIREMENTS_LOCK.md`：lines 1-30, 161-190, 254-266, 276-313
- `_design/POST_LOCK_PENDING.md`：lines 1-40, 137-223, 237-256
- `_design/CODEX_DEV_ORDER_EVALUATION.md`：lines 285-355, 373-382
- `_design/CODEX_GATE_1_REVIEW_REPORT.md`：lines 1-20, 149-170
- `_design/CODEX_A010_PATCH_REPORT.md`：lines 1-13, 42-58
- `_design/DECISIONS_LOG.md`：lines 1-5, 1244-1370, grep refs at 1386
- `_design/INTEGRATION_CONTRACTS.md`：lines 1-30, 70-85, 120-145, 1672-1812, 1960-1995
- `_design/SPEC.md`：lines 1-30, 247-263, 935-950
- `_design/ARCHITECTURE.md`：lines 1-30, 1225-1244, 1299-1332
- `_design/TASKS.md`：lines 1-31, 498-533, 633-670, 705-719, 979-1018, 1042-1115, 1145-1160
- `_design/DATA_FORMAT_SPEC.md`：lines 1-35, 1512-1688, 1824-1915, 1939-1956, 1997-2002, 2035-2070, 2441-2461
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`：lines 1-23, 3628-3772, 6235-6245
- `_design/registries/issue_type_registry.template.yaml`：lines 1-45, 50-121, 125-181, 186-228, 233-275, 280-321, 323-360
- `_design/registries/entity_type_registry.template.yaml`：grep refs lines 7, 60-77, 87
- `_design/registries/qa_type_registry.template.yaml`：grep refs lines 14, 19-50

Repository state checked:
- `git status --short -b` → `## master...origin/master`
- `git remote -v` → `origin https://github.com/mark75369/Writing-tools.git`
- `_design/CODEX_REVIEW_REPORT_E.md` did not exist before creation.

### 1.2 Files NOT Modified

All existing repo files were kept read-only. The only new file is this report:

- `_design/REQUIREMENTS_LOCK.md`
- `_design/POST_LOCK_PENDING.md`
- `_design/CODEX_DEV_ORDER_EVALUATION.md`
- `_design/CODEX_GATE_1_REVIEW_REPORT.md`
- `_design/CODEX_A010_PATCH_REPORT.md`
- `_design/DECISIONS_LOG.md`
- `_design/INTEGRATION_CONTRACTS.md`
- `_design/SPEC.md`
- `_design/ARCHITECTURE.md`
- `_design/TASKS.md`
- `_design/DATA_FORMAT_SPEC.md`
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
- `_design/registries/issue_type_registry.template.yaml`
- `_design/registries/entity_type_registry.template.yaml`
- `_design/registries/qa_type_registry.template.yaml`

## 2. 5 review item 逐項驗證

### Review-E-1：D-047 issue_type_registry 完整性

- 狀態：✓
- 證據：
  - `issue_type_registry.template.yaml` header 完整，且 D-047 / 三層機制 / locked 規則明示於 lines 1-31。
  - schema_version = `data_format_spec_v0.3`，且 5 skill key 權威命名列於 lines 33-42。
  - core 內容為 5 skill key：`00_e_world` lines 50-119、`00_f_character` lines 125-180、`00_g_outline` lines 186-227、`00_h_detailed_outline` lines 233-274、`00_l_relationship` lines 280-321。
  - grep/parse count：10+8+6+6+6 = 36 entries；每 entry 都有 `id / name / required_level / locked / question_summary / protocol_ref`；REQUIRED ↔ locked=true、STRONGLY_PREFERRED/OPTIONAL ↔ locked=false 無 mismatch；locked=true 共 15。
  - `user_extensions` 5 key 全空 list，lines 335-340；`core_overrides` 5 key 全空 list，lines 355-360。
  - D-047 拍板紀錄有日期 / 議題 / 決策 / 影響 / Owner：DECISIONS_LOG lines 1259-1277。
  - Contract D §4a 完整：schema lines 1683-1722；Phase B 行為 lines 1742-1765；衝突處理 lines 1767-1782；A.0F 對齊 lines 1784-1804；Pending lines 1806-1810。
- 殘留：無計分殘留。

### Review-E-2：NEW_REQ_4 + 同類 cleanup

- 狀態：△
- 證據：
  - DF v0.4 header / changelog 已列 §7.2、§8.2-§8.3、§9.1、§11.1.2、§7.3 範圍，lines 1-35。
  - §7.2 Template 範例已對齊 `entity_type_registry.template.yaml`：`schema_version: data_format_spec_v0.3` line 1525；A id_pattern 7 subtype line 1581；nested `allowed_values` / `reserved_subtypes` lines 1585-1598。
  - §7.3 Instance 範例 schema_version 已為 v0.3，line 1636；NEW_REQ_5 target_dir csv 語意補齊 lines 1681-1687。
  - §8.2 Template 範例已對齊 `qa_type_registry.template.yaml`：schema_version line 1834；8 個完整 `09_quality_assurance/...` template_path lines 1840-1870；`09_e` 不入 registry line 1873。
  - §8.3 Instance 範例 schema_version 已為 v0.3，line 1890。
  - §9.1 manifest `spec_version` 已為 `data_format_spec_v0.4`，line 2044。
  - stale grep：`data_format_spec_v0.1` / 5 subtype `(portrait|bg|cg|icon|effect)` / `09_a_AI_味檢查表.md` 僅在 changelog 或 supersede 註記命中，未見 operative 舊範例。
- 殘留：
  - DF §8.3 user extension 範例仍寫短路徑 `template_path: 09_j_設定一致性檢查.md`，line 1898；同段欄位說明又寫 template_path 是「相對 `09_quality_assurance/`」，line 1912。這與 §8.2 cleanup 後採 repo-root 完整相對路徑 `09_quality_assurance/...` 的風格不一致，也與 UD §3.10.2 新範例 line 3646 不一致。此為 minor，但仍在本輪 DF §8.3 同類 cleanup 範圍內。

### Review-E-3：NEW_REQ_6

- 狀態：△
- 證據：
  - UD v0.5 header / changelog 明列 NEW_REQ_6 patch 範圍，lines 1-23。
  - §3.10.2 選項 a 已改為在 `qa_type_registry.yaml user_extensions:` append entry，lines 3630-3666。
  - §3.10.2 選項 b agent 寫入目標已改為 append 到 `qa_type_registry.yaml user_extensions:`，lines 3671-3678。
  - §3.10.2 選項 c catalog 目標已改為 append 到 `qa_type_registry.yaml user_extensions:`，lines 3697-3703。
  - §3.10.3 閾值來源已改為 `qa_type_registry.yaml user_extensions[*].algorithm`，line 3726。
  - §3.10.4 接點要求表已明示 8 core + user_extensions 動態擴充、不含通配，lines 3751-3753；衝突偵測三條列於 line 3754。
  - §3.10.5 對齊表已改為在 `qa_type_registry.yaml user_extensions:` 段加 entry，line 3765。
  - `.qa_extension` / `<USER_DEFINED>` grep 命中僅在 changelog 或 supersede 註記；未見 operative `.qa_extension/*.yaml` 掃描規則殘留。`qa_type: <USER_DEFINED_VALUE>` 未命中舊通配字串，屬 placeholder，不是 `<USER_DEFINED>` enum 通配。
- 殘留：
  - UD §3.10.2 的 user_extensions entry 新增 `algorithm` 與 `report_template` 欄位，lines 3650-3660；§3.10.3 又要求從 `user_extensions[*].algorithm` 載入閾值，line 3726。
  - DF §8.3 Instance-only 欄位只列 `added_at / added_by / locked / template_path / extension_protocol`，lines 1907-1913；DF §8.10 parser 影響也只要求驗 `user_extensions[*].template_path`，lines 1997-2002。
  - 因此 NEW_REQ_6 雖完成 `.qa_extension` → `user_extensions:` 的方向修補，但 UD 新增的 `algorithm` 欄位未在 DF §8 user_extensions schema/parser 接點承接。這是 schema contract 層的 minor drift。

### Review-E-4：4 主 spec partial supersede 升版一致性

- 狀態：△
- 證據：
  - IC header：LOCKED v2.1 / 2026-05-19，lines 1-5；§0.3 D-047 row lines 79-83；§1 Contract D box lines 129-141；§4a D.1-D.4 + Pending lines 1672-1810；§8.2 升版紀錄 lines 1960-1995。
  - SPEC header：LOCKED v1.2 / 2026-05-19，lines 1-5；v1.2 摘要明示 partial supersede、保留原段、D-047 owner，lines 9-27。本輪 scope 標明 SPEC 只審 header changelog。
  - ARCH header：LOCKED v1.3 / 2026-05-19，lines 1-5；§12.6 issue_type_registry parser 規格 lines 1299-1311；§12.A.0.10 patch 紀錄 lines 1313-1332。
  - TASKS header：LOCKED v1.4 / 2026-05-19，lines 1-5；A.0.10 task 含 DONE、依賴、做法、驗收、不在 scope、cross-ref，lines 498-529。
  - DECISIONS_LOG §6.9 有 10 sub-sections：6.9.1 lines 1248-1255；6.9.2 lines 1257-1277；6.9.3 lines 1279-1285；6.9.4 lines 1287-1299；6.9.5 lines 1301-1307；6.9.6 lines 1309-1315；6.9.7 lines 1317-1330；6.9.8 lines 1332-1348；6.9.9 lines 1350-1360；6.9.10 lines 1362-1369。
  - partial supersede discipline：IC lines 15-23 / 1979-1984、SPEC lines 9-27、ARCH lines 9-28、TASKS lines 9-31 都明示保留既有段，不重寫舊段。
- 殘留：
  - checklist 要求「5 spec header 版本 + 狀態 + 最後更新日期一致（2026-05-19 / LOCKED / vX.X）」；但 DECISIONS_LOG header 為 `狀態：FINAL`，line 1。若 DECISIONS_LOG 作為決策紀錄慣例允許 FINAL，此點可視為非阻塞；若嚴格照本輪 checklist，則狀態不一致，判 △。
  - 不計分觀察：次要 reviewer 指出 SPEC/TASKS header 摘要宣稱部分 D-047 body 補點，但正文未全面承接。因本輪明確限定 SPEC 為 header changelog only，且 E-5 明示不要求 TASKS A.5 task 內文已 mention，本報告不把此點計入 E-4 fail。

### Review-E-5：跨檔 cross-ref 完整性

- 狀態：✓
- 證據：
  - `D-047` grep 出現在本輪命名集合：`DECISIONS_LOG.md`、`INTEGRATION_CONTRACTS.md`、`SPEC.md`、`ARCHITECTURE.md`、`TASKS.md`、`issue_type_registry.template.yaml`。DF / UD 未要求 D-047 ref，未列為缺口。註：checklist 文句寫「7 個檔」，但列名集合實際為 6 個檔；6 個命名檔全命中。
  - DF changelog 有 NEW_REQ_3 / NEW_REQ_4 / NEW_REQ_5，lines 7-34；並明示 NEW_REQ_6 不在 DF 範圍，line 34。UD changelog 有 NEW_REQ_6，lines 7-23。
  - `issue_type_registry` filename 出現在 DECISIONS_LOG §6.9.2 / IC §4a / ARCH §12.6 / TASKS v1.4 header：DECISIONS_LOG lines 1251, 1255, 1271, 1274；IC lines 1672-1680；ARCH lines 1299-1311；TASKS lines 17-20。
  - Stage 0 / A.0.10 patch 出現在 DECISIONS_LOG §6.9.7 lines 1317-1330、ARCH §12.A.0.10 lines 1313-1332、TASKS A.0.10 lines 498-529。
  - POST_LOCK_PENDING NEW_REQ 狀態欄位未要求本輪 verify RESOLVED；只讀原描述作對齊基準。
- 殘留：無計分殘留。

## 3. 新發現的 finding（若有）

### Finding E-F1：DF §8.3 user extension template_path 仍是短路徑

- Severity：Minor / blocks GO under this checklist
- Evidence：DF §8.3 line 1898 uses `template_path: 09_j_設定一致性檢查.md`; line 1912 says the path is relative to `09_quality_assurance/`.
- Why it matters：§8.2 cleanup and `qa_type_registry.template.yaml` use repo-root relative paths `09_quality_assurance/...`; UD §3.10.2 line 3646 also uses that style. Leaving §8.3 short path can reintroduce path-shape ambiguity for Instance user_extensions.

### Finding E-F2：UD §3.10 introduces `user_extensions[*].algorithm` without DF schema/parser承接

- Severity：Minor / blocks GO under this checklist
- Evidence：UD lines 3650-3660 include `algorithm` and `report_template`; UD line 3726 says thresholds load from `user_extensions[*].algorithm`. DF §8.3 fields lines 1907-1913 do not include `algorithm`; DF §8.10 parser impact lines 1997-2002 only validates `template_path`.
- Why it matters：NEW_REQ_6 resolved the file-location conflict, but the new field-level contract is split between UD and DF. Parser / authoring implementation may not know whether `algorithm` is allowed, required, ignored, or validated.

### Finding E-F3：DECISIONS_LOG header status differs from checklist wording

- Severity：Minor / checklist interpretation issue
- Evidence：DECISIONS_LOG line 1 is `狀態：FINAL`, while E-4 checklist says 5 spec headers should be `LOCKED`.
- Why it matters：This may be intentional project convention for a decisions log. If so, no content patch is needed, but the LOCKED gate checklist should explicitly exempt DECISIONS_LOG or require changing it.

## 4. 升 LOCKED 條件評估

對 DECISIONS_LOG §6.9.10 Milestone 1 可進入聲明：

- Gate 1 NO-GO 修補完成（Stage 0 PASS）→ ✓  
  Evidence：CODEX_A010_PATCH_REPORT lines 9-13, 42-58；DECISIONS_LOG lines 1317-1330；ARCH lines 1313-1332；TASKS lines 498-529。
- D-047 + NEW_REQ_3/4/5/6 全 RESOLVED → △  
  D-047 registry 本體 PASS；NEW_REQ_3/4/5 主體已對齊；NEW_REQ_4 same-class cleanup 與 NEW_REQ_6 field-level alignment 仍有 2 個 minor drift。
- IC v2.1 + SPEC v1.2 + ARCH v1.3 + TASKS v1.4 升版完成 → △  
  四主 spec version/date/header 基本完成；DECISIONS_LOG status 與 checklist wording 不一致。
- POST_LOCK_PENDING NEW_REQ_1/3/4/5/6 標 RESOLVED → Not reviewed / stage 9  
  本輪只把 POST_LOCK_PENDING 當原需求描述來源；不要求 verify RESOLVED 欄位。

## 5. Go / No-Go 決定

- **GO：** 不成立。5 項未全 ✓。
- **NEAR-GO：** 不成立。不是 4 ✓ + 1 △。
- **NO-GO：** 成立。E-2、E-3、E-4 共 3 項 △；依本輪規則，≥2 △ 即 NO-GO。

建議 patch 範圍保持很小：

1. DF §8.3 user extension example 改為 repo-root relative `09_quality_assurance/09_j_設定一致性檢查.md`，並把 line 1912 語意改成「相對 repo root」或明確統一 path contract。
2. 決定 `user_extensions[*].algorithm` / `report_template` 是否屬 `qa_type_registry.yaml` schema；若是，DF §8.3 欄位表與 §8.10 parser impact 應補；若不是，UD §3.10 應改成 template 內部欄位，不放 registry。
3. 決定 DECISIONS_LOG 是否應維持 FINAL；若維持，LOCKED gate checklist 加例外，不要要求它與四主 spec 同為 LOCKED。

## 6. Source Limitations

- 本輪未重審 CODEX (c) / (d) / (d2) 已 RESOLVED 議題，只在必要 line range 驗證新 patch 對齊。
- 本輪未重審 Gate 1 NO-GO + A.0.10 parser code；只讀 Gate 1 report 與 A.0.10 PASS report 作 Stage 0 狀態依據。
- 本輪未重審 UD §1.x.2 議題清單內文；`issue_type_registry.template.yaml` 的 `protocol_ref` 只驗到章節引用與 36 題抽取結果。
- SPEC 依任務邊界只審 header changelog；TASKS 依任務邊界只要求 header / A.0.10 entry / cross-ref，不要求 A.5 / B.x task body 已全面補 D-047。
- 沒有 fetch remote；本機狀態為 `master...origin/master`，remote URL 符合指定 repo。
