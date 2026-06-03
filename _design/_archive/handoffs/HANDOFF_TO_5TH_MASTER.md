狀態：✅ COMPLETED（master 第五輪整合對話 2026-05-19 完成 — 詳 DECISIONS_LOG §6.9）  
版本：v1.1（補 Stage 0：Gate 1 review NO-GO 必修項）  
最後更新：2026-05-19  
適用範圍：給「第五輪整合 master」對話的接手包 — Phase A.0 完成後的 master 第五輪整合工作  
優先級：歷史紀錄（已歸檔）

# HANDOFF_TO_5TH_MASTER — 第五輪整合 master 對話接手包

# 0. 文件目的

第四輪 master 對話完成設計層 LOCKED（10 spec）+ 4 輪 pre-LOCKED patch + Phase A.0 9 個 parser sub-task 實作。

**本檔給「第五輪整合 master 對話」啟動時用的接手包。**

第五輪預期工作：處理 POST_LOCK_PENDING 累積的 NEW_REQ 1-6（議題 registry D-047 + 使用說明書持續寫作 + 4 個 minor finding 修補），升 v2.1 系列 spec patch。

**預估第五輪總工時：** 3-5 小時 master 對話工時 + 1-2 小時 CODEX (e) 短審查（可選）。

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。第四輪 master 對話完成設計層 LOCKED + Phase A.0 9 個 parser sub-task 實作 + Gate 1 CODEX review，把接手包寫好交給你。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第五輪整合 master」對話。

**第一步必讀（按順序，精簡 — 7 份）：**
1. _design/HANDOFF_TO_5TH_MASTER.md（本檔，你的 scope）
2. _design/POST_LOCK_PENDING.md（你的待辦：NEW_REQ_1 ~ NEW_REQ_6）
3. _design/CODEX_DEV_ORDER_EVALUATION.md（執行路線評估報告 + master 第五輪時點建議）
4. _design/CODEX_RECHECK_REPORT_D2_PART3.md（最後一輪 CODEX (d2) PASS 結論）
5. _design/CODEX_GATE_1_REVIEW_REPORT.md（Phase A.0 收束 review；如有 finding 必處理）
6. _design/DECISIONS_LOG.md §6.8（v1.0 升 LOCKED 紀錄）
7. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL — north star，不動）

**第二步精選讀（碰到才看，不必整讀）：**
8. _design/INTEGRATION_CONTRACTS.md（v2.0 — 你要升 v2.1）
9. _design/SPEC.md / ARCHITECTURE.md / TASKS.md（v1.1/v1.2/v1.3 — 你要 partial supersede 升 v1.2/v1.3/v1.4）
10. _design/DATA_FORMAT_SPEC.md / UPSTREAM_DOWNSTREAM_SPEC.md / UX_SPEC.md / L3_EXPORT_PROMPT_SCHEMA.md（specialist spec — 你要 targeted patch 解 NEW_REQ_4/6）

**你的 scope（master 第五輪整合）：**

1. 拍板 D-047 議題 registry（NEW_REQ_1）— 新增 issue_type_registry 三層機制
2. 修 DF §7.2 範例殘留（NEW_REQ_4）— v0.1 → v0.3 + 5 subtype → 7 subtype
3. 修 UD §3.10.4 .qa_extension 寫法（NEW_REQ_6）— 改對齊 DF §8 qa_type_registry user_extensions
4. 細化 NEW_REQ_3 deleted KEY 內文存在性處理（minor）
5. 細化 NEW_REQ_5 target_dir csv schema（minor）
6. 處理 Gate 1 CODEX review 的 finding（如有）
7. 升 INTEGRATION_CONTRACTS v2.1 + 主 SPEC v1.2 + ARCH v1.3 + TASKS v1.4
8. 升 DECISIONS_LOG v1.1（補 §6.9 — 新增 D-047 + NEW_REQ_3/4/5/6 RESOLVED）
9. （可選）觸發 CODEX (e) 短審查
10. 升 LOCKED + 通知 user 進 Milestone 1（Phase A.0F alpha + Phase A 後段啟動）

**禁止越界：**
- 不重做設計（已 LOCKED v1.0）
- 不改 D-001 ~ D-046 拍板結論（要動需 user 拍板）
- 不擅啟 Phase A.0F / Phase B 實作（屬下一階段 user 操作）
- 不重審 CODEX (c) / (d) / (d2) 已 RESOLVED 議題
- partial supersede 段保留原段 + 加 v1.2 supersede 標記

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 7 份必讀後對 scope + master 第五輪工作順序的理解，再開始拍板 D-047。
```

---

# 2. 當前狀態快照

## 2.1 設計層狀態

| 檔 | 版本 | 狀態 | 備註 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | 不動 — north star |
| `_design/DECISIONS_LOG.md` | v1.0 | **FINAL** | D-001 ~ D-046 完整 + §6.8 升 LOCKED 紀錄 |
| `_design/DATA_FORMAT_SPEC.md` | v0.3 | **LOCKED** | 你升 v0.4（修 §7.2 / §3.10 NEW_REQ_4/6）|
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.4 | **LOCKED** | 你升 v0.5（修 §3.10.4 NEW_REQ_6）|
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 可能不動（依 D-047 影響範圍判定）|
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 可能不動 |
| `_design/INTEGRATION_CONTRACTS.md` | v2.0 | **LOCKED** | 你升 **v2.1**（加 D-047 + issue_type_registry contract）|
| `_design/SPEC.md` | v1.1 | **LOCKED** | 你升 **v1.2**（partial supersede via D-047 + 5.1 issue registry）|
| `_design/ARCHITECTURE.md` | v1.2 | **LOCKED** | 你升 **v1.3**（補 A.0.x issue registry parser 規格）|
| `_design/TASKS.md` | v1.3 | **LOCKED** | 你升 **v1.4**（補 A.0.10 issue registry parser task + B Phase /create-* 對齊）|
| `_design/PHASE_3_COMPLETION_REPORT.md` | v4.0 FINAL | **LOCKED** | 不動 |
| `_design/POST_LOCK_PENDING.md` | v0.1 | DRAFT | 你處理；解決完標 RESOLVED |
| `_design/CODEX_DEV_ORDER_EVALUATION.md` | v0.1 | REVIEW | 不動（歷史紀錄）|

## 2.2 Phase A.0 實作狀態

| sub-task | 狀態 | 對應 ARCH | 對應 Contract |
|---|---|---|---|
| A.0.1 frontmatter parser 基線 + phase_log | ✅ commit | §12.1.1 | A.2 |
| A.0.2 dialogue_keys Map + 內文 KEY 一致性 | ✅ commit | §12.1.2 | A.1 |
| A.0.3 全 repo KEY unique 集合 | ✅ commit | §12.1.3 | A.1 + A.4 |
| A.0.7 entity_type_registry | ✅ commit | §12.1.7 | A.5 |
| A.0.8 qa_type_registry | ✅ commit | §12.1.8 | A.5 |
| A.0.4 art_metadata + A-* prefix 識別 | ✅ commit | §12.1.4 | A.3 + C.5 |
| A.0.6 mode_tag / qa_type registry-driven | ✅ commit | §12.1.6 | A.5 + A.6 |
| A.0.5 內文 A-* cross-reference | ✅ commit | §12.1.5 | A.1 + A.3 |
| A.0.9 JSON export 結構化資料 API | ✅ commit | §12.1.9 | A.7 |

**Parser 累積：**
- `scripts/parse_frontmatter.py` — 21 dataclass + 29 public function
- `scripts/check_headers.py` — 0 ERROR baseline
- `_design/registries/` — entity_type_registry.template.yaml + qa_type_registry.template.yaml
- `_design/expected_entities.yaml` + `_design/entity_exempt.yaml`

## 2.3 Gate 1 CODEX Review

**狀態：** 第四輪 master 對話完成 A.0.9 後產出 review starter（`CODEX_GATE_1_REVIEW_STARTER.md`），由 user 觸發 CODEX (e) 評估。

**預期結論：**
- GO：parser 乾淨 + spec 落地一致 → 第五輪直接做 D-047
- NEAR-GO：1-3 minor 整合問題 → 第五輪一併處理
- NO-GO：critical 整合問題 → 第五輪先 patch parser 再做 D-047

**若 Gate 1 報告（`_design/CODEX_GATE_1_REVIEW_REPORT.md`）存在：** 第五輪必讀，先處理 finding 再進 D-047。

---

# 3. 第五輪工作清單（按執行順序）

## 階段 1：讀完 7 份必讀 + 回報理解（30 分）

跟第四輪一樣的開場 — 不要急著動工。

## 階段 2：⚠ Stage 0 — Gate 1 NO-GO 必修 parser patch（1-2 小時）

**Gate 1 review 結論為 NO-GO**，3 個 critical parser integration gap **必須先修補才能進 D-047**：

### Stage 0 必修項

讀 `_design/CODEX_GATE_1_REVIEW_REPORT.md` 完整 finding 列表 + line ref。**3 個 critical 摘要：**

1. **A.0.5 cross-ref validator 未整合 `build_repo_index()`**
   - A.0.5 `validate_body_vs_frontmatter_consistency()` 在 A.0.9 build_repo_index 中沒被 invoke
   - 結果：跑 build_repo_index 對全 repo 時，內文 vs frontmatter 不一致不會被偵測
   - 修：build_repo_index 對每個 dialogue file 同時跑 dialogue_keys 解析 + body art refs 解析 + 雙軌一致性檢查；issues 統一聚合到 RepoIndex.issues

2. **A.0.7 entity registry 一般 ID 驗證未在 index 跑**
   - validate_entity_id() 存在但 build_repo_index 沒對每個 parsed_markdown 的 `entities` / `depends_on` ID 跑驗證
   - 結果：未知 entity 類型 / ID 格式不符不會在 RepoIndex.issues 出現
   - 修：build_repo_index 對每個 parsed_markdown 的 entity ID 跑 validate_entity_id，issues 聚合

3. **Windows UTF-8 BOM header 漏讀風險**
   - parse_file 讀檔時若檔開頭有 BOM (`﻿`)，中文 header 「狀態：DRAFT」可能因 BOM 而 prefix match 失敗
   - 修：parse_file 加 `encoding='utf-8-sig'` 或在 parse_markdown_text 內 strip BOM

### Stage 0 流程

**選項 A（推薦）：** 開新 CODEX 對話跑「A.0.10 parser patch round」task
- prompt scope：只修 3 critical finding；不做其他改動
- 預估 CODEX 1-2 小時
- 完成後 user 跑 mini-recheck（用 Gate 1 starter 但 scope 縮限為「驗證 3 項已修」）

**選項 B：** master 第五輪對話自己 patch（如果你有 implementer ability + 時間）
- 直接 Edit scripts/parse_frontmatter.py
- 跑 tempfile 驗證
- user 手動 commit + push

### Stage 0 完成條件

- 3 個 critical 全 ✓ PASS
- check_headers.py 0 ERROR 維持
- build_repo_index('.') 不引入新 ERROR
- mini-recheck CODEX 確認

**Stage 0 PASS 後才進階段 3 拍板 D-047。**

## 階段 2.5：處理 Gate 1 其他 finding（如有）

依 Gate 1 報告處理 major / minor。可在階段 3-9 過程中順帶處理。

## 階段 3：拍板 D-047 議題 registry（1-1.5 小時）

依 POST_LOCK_PENDING NEW_REQ_1 提議方案：

- 新增 `_design/registries/issue_type_registry.template.yaml`（Template — 5 個 skill 議題清單）
  - 00_e_world: 11 議題（id / name / required_level / locked: true / question prompt）
  - 00_f_character: 9 議題
  - 00_g_relationship: 6 議題  
  - 00_h_outline: 7 議題
  - 00_l_detailed_outline: 7 議題
- `user_extensions:` 段 user 可加自訂議題
- `core_overrides:` 段 user 可標 SKIP（如純愛遊戲跳「越界禁區」）
- 對應 `_design/registries/issue_type_registry.yaml`（Instance 端）

**D-047 紀錄：**
- 議題：5 個 /create-* skill 議題清單客製化機制
- 決策：採 issue_type_registry 三層機制（同 entity_type_registry / qa_type_registry pattern）
- 影響：Phase B /create-* skill 實作時讀 registry，不硬編議題
- Owner：master 第五輪 + Phase B specialist

## 階段 4：修 DF §7.2 殘留（30 分）

依 POST_LOCK_PENDING NEW_REQ_4：
- DF §7.2 line 1492：`schema_version: data_format_spec_v0.1` → `data_format_spec_v0.3`
- DF §7.2 line 1548：`^A-(portrait|bg|cg|icon|effect)-.+-.+$` → `^A-(portrait|bg|cg|sfx|bgm|voice|ui)-.+-.+$`
- DF §7.2 line 1552-1557 subtype list：改 5 種 → 7 種 + 補 reserved_subtypes 段

## 階段 5：修 UD §3.10.4 .qa_extension 寫法（30 分）

依 POST_LOCK_PENDING NEW_REQ_6：
- UD §3.10.4 line 3613/3643/3663/3690：`.qa_extension/*.yaml` 寫法 supersede
- 改寫成「qa_type_registry.yaml user_extensions: 段加 entry」pattern（對齊 DF §8 + Contract A.5）
- line 3714 「9 種含 USER_DEFINED」改「8 種 core + user_extensions 動態擴充」

## 階段 6：細化 NEW_REQ_3 / NEW_REQ_5（minor，30 分）

- NEW_REQ_3 deleted KEY 內文存在性：補 WARN「該 KEY status=deleted，建議從內文移除」（或維持寬鬆 — 拍板）
- NEW_REQ_5 target_dir csv schema：選 b（維持 csv 但 schema 明示「comma-separated list」）

## 階段 7：升 spec 版本（1-1.5 小時）

依 §2.1 表格升 v2.1 / v1.2 / v1.3 / v1.4 / v1.1（DECISIONS_LOG）。

partial supersede 紀律：保留原段 + 加 v1.x supersede 標記。

## 階段 8：（可選）觸發 CODEX (e) 短審查

scope 只看：
- D-047 issue_type_registry 機制完整性
- DF §7.2 + UD §3.10.4 修補對齊
- 升 v2.1 / v1.2 / v1.3 / v1.4 一致性

預估 CODEX 30-45 分。

## 階段 9：升 LOCKED + 通知 user 進 Milestone 1

- 升新版 spec LOCKED
- 升 POST_LOCK_PENDING NEW_REQ_1/3/4/6 標 RESOLVED
- 通知 user 可以進 A.0F alpha + Phase A 後段（A.1 - A.11）

---

# 4. 對 user 的最終建議（master 第五輪完成後）

**Phase A.0F alpha + Phase A 後段（A.1-A.11）啟動條件：**
- spec 升 v2.1 series LOCKED ✓
- D-047 issue_type_registry 落地（Template + 機制）✓
- POST_LOCK_PENDING 累積項目處理完 ✓

完成後 user 可進入：

```
A.0F alpha（scaffold + fixture data 前端）— 可平行
Phase A 後段：
  A.1 寫 00_b 通用骨架
  A.2 寫 00_i init protocol
  A.3 寫 00_e create-world protocol
  A.4 補完 27 模板 frontmatter
  A.5 實作 /init-project skill（+ registry 拷貝）
  A.6 實作 /create-world skill（用 issue_type_registry）
  A.7 實作 /status skill
  A.8 實作 /check-gaps skill
  A.9 wrapper smoke test
  A.10 Phase A REVIEW Gate
  A.11 Phase A 整體驗收
   ↓
🟡 Milestone 1：第一個能跑的版本（user 可實際試用世界觀建立）
```

到 Milestone 1 後 user 可第一次 user-test，根據反饋決定是否需要 master 第六輪。

---

# 5. 風險警示

## 5.1 D-047 議題 registry 設計細節

CODEX 開發順序評估報告（§5）已警告：

- 議題 registry 機制要早做（不能等 Phase A 全結束）— 否則 A.2 / A.3 / A.5 / A.6 + Phase B 會硬編議題
- 第五輪是**最後機會**早做

## 5.2 A.0F 拆兩段制

CODEX 開發順序評估報告（§3）強調：

- **A.0F 不可作為 Phase B 前完整 gate**
- A.0F alpha 在 A.0.9 後做（scaffold + fixture）
- A.0F real-data acceptance 留到 B.9 後做

第五輪整合時若動 TASKS A.0F 段，**必須保留兩段制**。

## 5.3 LOCKED 段 partial supersede 紀律

所有 v1.1 → v1.2 / v0.4 → v0.5 等都走 partial supersede：
- 保留原段內容
- 加 `[v1.2 partial supersede via D-047 — north-star 對齊理由：...]` 標註
- 不刪除原段

## 5.4 sandbox virtiofs cache 已知問題

工作目錄 Windows 端是權威。Sandbox 端 git status 偶爾顯示 stale（含 stale "renamed/deleted" 條目）。**所有 git commit + push 由 user 手動執行**，不靠 sandbox bash。

---

# 6. POST_LOCK_PENDING 對照

| NEW_REQ | 內容 | 第五輪處理 |
|---|---|---|
| NEW_REQ_1 | 議題 registry D-047 | 階段 3 拍板 |
| NEW_REQ_2 | 使用說明書 | 不阻擋第五輪；持續累積 |
| NEW_REQ_3 | deleted KEY 內文細化 | 階段 6 細化 |
| NEW_REQ_4 | DF §7.2 殘留 | 階段 4 修 |
| NEW_REQ_5 | target_dir csv schema | 階段 6 細化 |
| NEW_REQ_6 | UD §3.10.4 .qa_extension 殘留 | 階段 5 修 |

---

# 7. 完成條件

第五輪整合對話完成 = 以下全部 ✓：

```
✓ Gate 1 review finding（如有）全 RESOLVED
✓ D-047 拍板 + DECISIONS_LOG §6.9 紀錄
✓ _design/registries/issue_type_registry.template.yaml 新建
✓ DF v0.4 + UD v0.5 修補 NEW_REQ_4/6
✓ NEW_REQ_3/5 minor 細化
✓ INTEGRATION_CONTRACTS v2.1 + 主 SPEC v1.2 + ARCH v1.3 + TASKS v1.4 升版
✓ DECISIONS_LOG v1.0 → v1.1
✓ POST_LOCK_PENDING NEW_REQ_1/3/4/5/6 標 RESOLVED（NEW_REQ_2 維持持續寫作）
✓ 升新版 spec LOCKED
✓ （可選）CODEX (e) 短審 clean
✓ user 通知可以進 Phase A.0F alpha + Phase A 後段
```

---

# 8. 文件維護紀律

- 本檔是「**接手指南**」，第五輪 master 對話讀完後**不需要更新本檔**
- 若第五輪發現本檔不準確 → 標 errata 在第六輪接手包（如有）
- 第五輪完成後可把本檔 archive 進 `_design/archive/`
