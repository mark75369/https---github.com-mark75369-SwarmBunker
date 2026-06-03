狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：master 第五輪整合 partial supersede 升版完成後的 CODEX (e) 短審查啟動包  
優先級：高

# CODEX_REVIEW_STARTER_E — Master 第五輪 partial supersede 升版完成後的 CODEX 短審查

# 0. 本檔用途

Master 第五輪整合對話完成：
- Stage 0 A.0.10 parser patch PASS（已 CODEX 跑完）
- 階段 3-7 設計層升版完成
- 階段 6 NEW_REQ_3/5 細化完成

把本檔 §1 內的 prompt 整段複製貼到新 CODEX 對話，啟動「**CODEX (e) 短審查**」— 確認本輪 partial supersede / D-047 / NEW_REQ_3/4/5/6 對齊一致，可升 LOCKED。

**前置條件（必須先完成）：**

- ✓ Stage 0 A.0.10 patch PASS（CODEX_A010_PATCH_REPORT.md 已產出）
- ✓ master 第五輪階段 3-7 全部完成
- ✓ 5 spec 升版完成：IC v2.0→v2.1 / SPEC v1.1→v1.2 / ARCH v1.2→v1.3 / TASKS v1.3→v1.4 / DECISIONS_LOG v1.0→v1.1
- ✓ 2 specialist spec 升版完成：DF v0.3→v0.4 / UD v0.4→v0.5
- ✓ 新建 _design/registries/issue_type_registry.template.yaml v0.1
- ✓ POST_LOCK_PENDING NEW_REQ_1/3/4/5/6 處理完（標 RESOLVED 屬 stage 9 範圍，本審查不要求）

**本檔跟既有 starter 的差別：**

| 維度 | CODEX_REVIEW_STARTER_D / RECHECK_STARTER_D2 / A010_PATCH_STARTER | **本檔 CODEX_REVIEW_STARTER_E** |
|---|---|---|
| 觸發時機 | 第四輪 / Phase A.0 收束 | **第五輪 partial supersede 升版完成** |
| CODEX 身份 | reviewer / implementer / patcher | **reviewer（不改檔；獨立眼睛 review）** |
| Scope | 全 spec 一致性 / 13 finding 修補 / parser patch | **D-047 + NEW_REQ_3-6 + 4 主 spec 升版一致性** |
| 預估時數 | 2-3 小時 / 45-90 分 / 1-2 小時 | **30-45 分（嚴限 scope）** |
| 預期產出 | review report v0.1 | **CODEX_REVIEW_REPORT_E.md（GO / NEAR-GO / NO-GO）** |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「Master 第五輪 partial supersede 升版完成後、升 LOCKED 前」的 CODEX (e) 短審查。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔、不改 spec
- 你是 targeted reviewer — 只驗證 D-047 完整性 + NEW_REQ_3/4/5/6 修補對齊 + 4 主 spec partial supersede 升版一致性
- 你是升 LOCKED 前 final-check — 通過 → master 直接進階段 9 升 LOCKED + Milestone 1；不通過 → 再一輪 partial supersede patch
- 對應傳統：本輪是第 8 輪 CODEX 審查（前 7 輪：時期 A 4 輪 + (c) 1 輪 + (d) 1 輪 + (d2 Part1/2/3) 3 輪 + Gate 1 / A.0.10 patch）

**重要邊界（嚴格 scope）：**

- ✗ **不**重審 CODEX (c) 17 衝突 / 5 越界（已 RESOLVED via D-037~D-046）
- ✗ **不**重審 CODEX (d) / (d2) 已 RESOLVED 議題
- ✗ **不**重審 Gate 1 NO-GO + A.0.10 patch round（已 PASS）
- ✗ **不**動 D-001 ~ D-047 拍板結論
- ✗ **不**動 REQUIREMENTS_LOCK.md（v1.0 FINAL）
- ✗ **不**重審 Phase A.0 parser code（屬 Stage 0 範圍，已 PASS）
- ✗ **不**重審 UD §1.x.2 議題清單內文（屬 Phase B 實作前 spec partial supersede 範圍）

**本輪 scope（嚴格限定 — 5 個 review item）：**

### Review-E-1：D-047 issue_type_registry 完整性

**檢查對象：**
- `_design/registries/issue_type_registry.template.yaml` v0.1（新建）
- `_design/DECISIONS_LOG.md` §6.9.2（D-047 拍板紀錄）
- `_design/INTEGRATION_CONTRACTS.md` §4a 全新章節（Contract D — D.1 ~ D.5）

**必看：**
- 5 個 skill key 對齊 UD LOCKED 權威：00_e_world / 00_f_character / 00_g_outline / 00_h_detailed_outline / 00_l_relationship
- 議題總數 36（10+8+6+6+6 user-facing；拆分規則不入 registry）
- 每議題 6 欄位完整（id / name / required_level / locked / question_summary / protocol_ref）
- REQUIRED ↔ locked=true 對齊；STRONGLY_PREFERRED / OPTIONAL ↔ locked=false
- user_extensions + core_overrides 5 個 skill key 對應且全空 list
- D-047 拍板紀錄 5 欄位完整（日期 / 議題 / 決策 / 影響 / Owner）
- Contract D §4a 章節結構：4a.1 schema / 4a.2 Phase B 行為 / 4a.3 衝突處理 / 4a.4 A.0F 對齊 / 4a.5 Pending

**判定：** ✓ Pass / ✗ Fail / △ Partial（含證據 + line ref）

### Review-E-2：NEW_REQ_4 + 同類 cleanup（DF §7.2 / §8.2 / §8.3 / §9.1）對齊

**檢查對象：**
- `_design/DATA_FORMAT_SPEC.md` v0.4（header changelog + §7.2 + §8.2 + §8.3 + §9.1 + §11.1.2 + §7.3）

**必看：**
- DF v0.3 → v0.4 升版 + changelog 完整列 4 區塊（§7.2 NEW_REQ_4 原 scope / §8.2-§8.3 同類擴充 / §9.1 同類擴充 / §11.1.2-§7.3 NEW_REQ_3+5 細化 / 不在本輪 scope 段）
- §7.2 Template 範例對齊 `entity_type_registry.template.yaml`（schema_version v0.3 / A id_pattern 7 subtype / nested allowed_values+reserved_subtypes）
- §7.2 Instance 範例 schema_version v0.3
- §8.2 Template 範例對齊 `qa_type_registry.template.yaml`（schema_version v0.3 / 8 個 template_path 完整相對路徑 `09_quality_assurance/...`）
- §8.3 Instance 範例 schema_version v0.3
- §9.1 JSON export manifest spec_version v0.4
- §7.2 / §8.2 各保留 [v0.4 partial supersede via NEW_REQ_4] 標註
- 整檔搜尋無實際 stale `data_format_spec_v0.1` / 5 subtype `(portrait|bg|cg|icon|effect)` / 簡名 template_path `09_a_AI_味檢查表.md` 殘留（只允許 changelog + supersede 註中文字描述）

**判定：** ✓ Pass / ✗ Fail / △ Partial

### Review-E-3：NEW_REQ_6（UD §3.10.4 .qa_extension 寫法 → user_extensions:）對齊

**檢查對象：**
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5（header changelog + §3.10.2 + §3.10.3 + §3.10.4 + §3.10.5）

**必看：**
- UD v0.4 → v0.5 升版 + changelog 完整列 NEW_REQ_6 patch 範圍
- §3.10.2 選項 a yaml 範例對齊 `qa_type_registry.yaml user_extensions:` 段寫法（不再 `.qa_extension/<name>.yaml` 獨立檔）
- §3.10.2 選項 b agent 寫入目標 = `qa_type_registry.yaml user_extensions:`
- §3.10.2 選項 c catalog 範本 copy 目標 = `qa_type_registry.yaml user_extensions:`
- §3.10.3 line 3725 閾值來源 = `qa_type_registry.yaml user_extensions[*].algorithm` 欄
- §3.10.4 接點要求表：
  - 「工具預設 enum: 8 core + user_extensions 動態擴充（不含通配）」
  - 「A.0 parser 讀 `qa_type_registry.yaml` 載入 core + user_extensions」
  - 衝突偵測 3 條（重複 ERROR / 命名違反 ERROR / template_path 缺檔 WARN）
- §3.10.5 對齊表「寫 .qa_extension yaml」→「在 `qa_type_registry.yaml user_extensions:` 段加 entry」
- 整檔搜尋無實際 operative `.qa_extension/*.yaml` 寫法殘留（只允許 changelog + supersede 註）
- 整檔搜尋無 `<USER_DEFINED>` 通配殘留（只允許 supersede 註）

**判定：** ✓ Pass / ✗ Fail / △ Partial

### Review-E-4：4 主 spec partial supersede 升版一致性

**檢查對象：**
- `_design/INTEGRATION_CONTRACTS.md` v2.1（header + §0.3 + §1 + §4a + §8.2）
- `_design/SPEC.md` v1.2（header changelog only — body 不動）
- `_design/ARCHITECTURE.md` v1.3（header + §12.6 + §12.A.0.10）
- `_design/TASKS.md` v1.4（header + A.0.10 task entry）
- `_design/DECISIONS_LOG.md` v1.1（§6.9 全新章節 10 sub-sections）

**必看：**
- 5 spec header 版本 + 狀態 + 最後更新日期一致（2026-05-19 / LOCKED / vX.X）
- 5 spec 內 D-047 cross-ref 都指向正確章節（DECISIONS_LOG §6.9.2 / IC §4a / SPEC v1.2 摘要 / ARCH §12.6 + §12.A.0.10 / TASKS A.0.10 / DF §11.1.2 + §7.3 / UD §3.10）
- partial supersede 紀律：所有 v1.x → v1.y 升版段都保留原段內容 + 加 v1.y 標註，**不**刪除原段
- IC v2.1 Contract D（§4a）4 sub-section（D.1 ~ D.4）+ §4a.5 Pending 完整
- ARCH §12.6 issue_type_registry parser 規格 + §12.A.0.10 A.0.10 patch 紀錄完整
- TASKS A.0.10 task entry 含驗收條件 + cross-ref 到 Stage 0 報告
- DECISIONS_LOG §6.9 10 sub-sections（6.9.1 變動摘要 / 6.9.2 D-047 / 6.9.3 NEW_REQ_3 / 6.9.4 NEW_REQ_4 / 6.9.5 NEW_REQ_5 / 6.9.6 NEW_REQ_6 / 6.9.7 Stage 0 / 6.9.8 升版文件清單 / 6.9.9 升 v1.1 後紀律 / 6.9.10 Milestone 1 可進入聲明）

**判定：** ✓ Pass / ✗ Fail / △ Partial

### Review-E-5：跨檔 cross-ref 完整性

**必跑檢查（grep-based）：**

1. `D-047` 出現於：DECISIONS_LOG §6.9.2 / IC §0.3 + §1 + §4a / SPEC v1.2 header / ARCH v1.3 header + §12.6 / TASKS v1.4 header + A.0.10 / issue_type_registry.template.yaml header — 7 個檔有 ref（DF + UD **不要求** D-047 ref — D-047 contract 落在 IC §4a；DF/UD 議題清單 partial supersede 屬 Phase B 實作前下一輪，本輪不動）
2. `NEW_REQ_3` / `NEW_REQ_4` / `NEW_REQ_5` 出現於 DF v0.4 changelog 對應段；`NEW_REQ_6` 出現於 UD v0.5 changelog + DF v0.4 §3.10 NEW_REQ_6 不在 DF 範圍 mention
3. `issue_type_registry` filename 出現於：DECISIONS_LOG §6.9.2 / IC §4a / ARCH §12.6 / TASKS v1.4 header（不要求 A.5 task 內文已 mention — TASKS v1.4 header changelog 已標 A.5 「補拷貝」屬未來 task description patch）
4. `Stage 0` / `A.0.10 patch` 出現於：DECISIONS_LOG §6.9.7 / ARCH §12.A.0.10 / TASKS A.0.10
5. POST_LOCK_PENDING NEW_REQ 狀態欄位（本輪 master 第五輪未必更新到 RESOLVED — 屬 stage 9 範圍；CODEX 不要求 verify RESOLVED 狀態，只 verify spec 端對齊）

**判定：** ✓ Pass / ✗ Fail / △ Partial

---

**必讀文件（按順序）：**

A. 對齊基準（不審；當 spec 依據；只看引用段落）
1. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL — north star）
2. _design/POST_LOCK_PENDING.md（v0.1 — NEW_REQ_1/3/4/5/6 原描述）
3. _design/CODEX_DEV_ORDER_EVALUATION.md（master 第五輪時機建議）
4. _design/CODEX_GATE_1_REVIEW_REPORT.md（Gate 1 NO-GO 報告）
5. _design/CODEX_A010_PATCH_REPORT.md（Stage 0 PASS）

B. 本輪審查對象（核心）
6. _design/DECISIONS_LOG.md（v1.1 — §6.9 全新章節 10 sub-sections）
7. _design/INTEGRATION_CONTRACTS.md（v2.1 — §0.3 + §1 + §4a + §8.2）
8. _design/SPEC.md（v1.2 — header changelog only）
9. _design/ARCHITECTURE.md（v1.3 — header + §12.6 + §12.A.0.10）
10. _design/TASKS.md（v1.4 — header + A.0.10 task entry）

C. Specialist spec 升版（partial supersede patch）
11. _design/DATA_FORMAT_SPEC.md（v0.4 — header + §7.2 + §8.2 + §8.3 + §9.1 + §7.3 + §11.1.2）
12. _design/UPSTREAM_DOWNSTREAM_SPEC.md（v0.5 — header + §3.10.2 + §3.10.3 + §3.10.4 + §3.10.5）

D. 新建檔（核心）
13. _design/registries/issue_type_registry.template.yaml（v0.1 DRAFT — D-047 落地）

E. 既有 registry 對齊基準
14. _design/registries/entity_type_registry.template.yaml（v0.3 — DF §7.2 範例對齊依據）
15. _design/registries/qa_type_registry.template.yaml（v0.3 — DF §8.2 範例對齊依據）

---

**你要交付的產物：**

新建：`_design/CODEX_REVIEW_REPORT_E.md`

報告格式：

```markdown
狀態：REVIEW  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX (e) 短審查 — master 第五輪 partial supersede 升版驗證  
優先級：高  

# CODEX_REVIEW_REPORT_E — Master 第五輪升版 review

## 0. 摘要

**結論：[GO / NO-GO / NEAR-GO（仍有 1-2 minor 殘留）]**

5 review item：
- E-1 D-047 完整性：✓/✗/△
- E-2 NEW_REQ_4 + 同類 cleanup：✓/✗/△
- E-3 NEW_REQ_6：✓/✗/△
- E-4 4 主 spec 升版一致性：✓/✗/△
- E-5 跨檔 cross-ref：✓/✗/△

## 1. 審查範圍

### 1.1 Files Read
（列你實際讀的檔案 + line range）

### 1.2 Files NOT Modified
（明示沒動的檔案；應為所有檔；報告本身是唯一新建）

## 2. 5 review item 逐項驗證

### Review-E-1：D-047 issue_type_registry 完整性
- 狀態：✓/✗/△
- 證據：（line ref + 評語）
- 殘留：（如有）

### Review-E-2：NEW_REQ_4 + 同類 cleanup
...

### Review-E-3：NEW_REQ_6
...

### Review-E-4：4 主 spec partial supersede 升版一致性
...

### Review-E-5：跨檔 cross-ref 完整性
...

## 3. 新發現的 finding（若有）

不期望出現新衝突；若 partial supersede 引入新問題列在這。

## 4. 升 LOCKED 條件評估

對 DECISIONS_LOG §6.9.10 Milestone 1 可進入聲明：
- Gate 1 NO-GO 修補完成（Stage 0 PASS）→ ✓
- D-047 + NEW_REQ_3/4/5/6 全 RESOLVED → 本輪結果決定
- IC v2.1 + SPEC v1.2 + ARCH v1.3 + TASKS v1.4 升版完成 → 本輪結果決定
- POST_LOCK_PENDING NEW_REQ_1/3/4/5/6 標 RESOLVED → 屬 stage 9（本輪不審）

## 5. Go / No-Go 決定

- **GO：** 5 項全 ✓ → master 可直接進階段 9 升 LOCKED + Milestone 1 通知
- **NEAR-GO：** 4+ 項 ✓，1-2 minor 殘留可在升 LOCKED 同時修 → master 自決
- **NO-GO：** 任一必修項仍 ✗ → 一輪 partial supersede patch 後再 recheck

## 6. Source Limitations

（你實際讀的檔；不審的 spec 區段；任何依靠假設的判斷）
```

---

**Go / No-Go 判定指引：**

- **GO：** 5 項全 ✓
- **NEAR-GO：** 4 ✓ + 1 △，△ 不涉 D-047 / Contract D 結構性問題
- **NO-GO：** ≥ 1 ✗ 或 ≥ 2 △

請開始。
```

---

# 2. 額外給 CODEX 的提示（可選 — CODEX 提問時可參考）

## 2.1 為什麼是 5 個 review item 不是 10 個

本輪 partial supersede 嚴限 D-047 + NEW_REQ_3/4/5/6 + Stage 0 對齊。其他過往 finding（CODEX (c) / (d) / (d2) / Gate 1）已 RESOLVED 不重審。5 個 item 對應：
- E-1: D-047 主議題
- E-2: NEW_REQ_4（+ master 第五輪 user 拍板擴 scope 的 §8.2/§8.3/§9.1 同類 cleanup）
- E-3: NEW_REQ_6
- E-4: 4 主 spec + DECISIONS_LOG 升版
- E-5: 跨檔 cross-ref

NEW_REQ_3 + NEW_REQ_5 屬 minor 細化（DF §11.1.2 + §7.3）— 已併入 E-2 範圍（DF v0.4 整體）。

## 2.2 不要為了「全面 review」擴大 scope

CODEX 看 partial supersede 容易想去掃整本 spec。本輪只 verify 5 item 列出的具體段落 / 範圍；其他段落屬 LOCKED 不審。若 CODEX 在 5 item 以外發現問題，列在 §3「新發現的 finding」段，不擋本輪 GO/NO-GO。

## 2.3 commit 紀律

CODEX 完成後**不要**自己 commit / push — 由 user 手動執行。CODEX 只負責生報告。

---

# 3. 完成條件 + master 第五輪後續

CODEX (e) 完成 = 以下全部 ✓：

```
✓ _design/CODEX_REVIEW_REPORT_E.md 產出
✓ 5 review item 全逐項給 ✓/✗/△ + 證據
✓ §3 新發現 finding（若無，明示 None）
✓ §4 升 LOCKED 條件評估
✓ §5 GO / NEAR-GO / NO-GO 結論
✓ 沒動任何 spec 文件
```

CODEX 完成後：
- User 手動 commit + push `_design/CODEX_REVIEW_REPORT_E.md`
- master 第五輪整合 master 接手 read report
- 若 GO → 進階段 9 升 LOCKED + Milestone 1 通知
- 若 NEAR-GO / NO-GO → master 第五輪依殘留決定一輪 partial supersede patch + 再 recheck

---

# 4. 文件維護紀律

- 本檔是「**CODEX 短審查啟動包**」；CODEX 完成後可 archive 進 `_design/archive/`
- 本檔產出後若需修補，改本檔 + 升 v0.2，**不**重發 prompt（CODEX 對話內就地補丁）
