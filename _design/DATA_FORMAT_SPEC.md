狀態：LOCKED
版本：v0.5（Batch 5 NEW_REQ_48 / D-075 — §7.1 計數 9→11 + §7.2 inline YAML 補 W-style + ORG + §7.6 core 紀錄鏡像補 W-style + ORG（registry 11 種對齊）+ 標題計數修正 + 鏡像/權威指標註；partial supersede，不 bump schema_version；本檔 v0.4 → v0.5）
最後更新：2026-06-03
適用範圍：資料格式 specialist 第二輪交付 — 4-Bucket 拍板基底 + CODEX (c) 審查 P0/P1 裁決 patch + master 第四輪 pre-LOCKED 細化（CC-04/06/07 校正）+ master 第五輪 NEW_REQ_4 範例對齊 + Batch 5 NEW_REQ_48 §7.1/§7.2/§7.6 鏡像對齊
優先級：最高

# v0.5 變動摘要（Batch 5 NEW_REQ_48 / D-075 — §7.1/§7.2/§7.6 鏡像對齊 registry 11 種 core）

**§7.1 三層職責表計數（i1 pre-existing drift 回填）：**
- Template 列內容 `本輪：7 既有 + A-* = 9 個 core` → `現行：9 敘事既有 + A-* 美術 + ORG 組織 = 11 個 core；權威以 entity_type_registry.template.yaml 為準`（修正 stale 計數，標明權威來源）

**§7.2 Template 層 inline YAML 鏡像（i1 pre-existing drift 回填 — D-055 W-style / D-071 ORG 後未回填本 inline 範例）：**
- inline `core:` 補 **W-style**（D-055；01_world/）+ **ORG**（D-071 / D-074；11_organizations/）兩筆，使 inline 鏡像對齊權威檔 11 種 core
- 區塊頂加 `[NON-AUTHORITATIVE MIRROR of ...]` 標記 + D-075 雙軌指標註：唯一權威為 `entity_type_registry.template.yaml`（以 `load_entity_type_registry()` 載入），應由權威檔再生、勿手工改出分歧，drift 由 `scripts/check_entity_type_consistency.py` 把關
- **不刪除 inline 鏡像（spec-doc 可讀性）、不 bump `schema_version`（仍 data_format_spec_v0.3）；本輪非 regression（D-055/D-071 既有 drift 回填）**

**§7.6 core 紀錄鏡像（i1 pre-existing drift 回填 — D-055 W-style / D-071 ORG 後未回填本鏡像）：**
- 標題 `既有 7 種 + A-*` → `11 種 core 紀錄（鏡像；權威見 entity_type_registry）`（修正 stale 計數）
- 表格補 **W-style**（來源 D-055）+ **ORG-\<name\>**（來源 D-071 / D-074）兩列，9 種 → registry core 全 11 種
- 加 D-075 雙軌指標註：標明本表為 human-readable 鏡像，單一權威為 `entity_type_registry.template.yaml`（以 `load_entity_type_registry()` 載入），不一致時以 registry 為準，`scripts/check_entity_type_consistency.py` 斷言鏡像 == registry core
- **不刪除鏡像（spec-doc 可讀性）、不 bump `schema_version`（仍 data_format_spec_v0.3）；本輪非 regression（D-055/D-071 既有 drift 回填）**

# v0.4 變動摘要（master 第五輪 NEW_REQ_4 + 同類擴充 cleanup）

**§7.2 entity_type_registry 範例（NEW_REQ_4 原 scope）：**
- Template 範例 schema_version `v0.1` → `v0.3`（對齊 entity_type_registry.template.yaml 權威）
- Template 範例 A `id_pattern` `^A-(portrait|bg|cg|icon|effect)-.+-.+$` → `^A-(portrait|bg|cg|sfx|bgm|voice|ui)-.+-.+$`（D-044 7 subtype）
- Template 範例 subtype 從 5 項 plain list 改成 nested `allowed_values` (7) + `reserved_subtypes` (4)，對齊 entity_type_registry.template.yaml line 64-77
- Instance 範例 schema_version `v0.1` → `v0.3`

**§8.2 / §8.3 qa_type_registry 範例（NEW_REQ_4 同類擴充 — master 第五輪同類 cleanup 一併修）：**
- §8.2 Template 範例 schema_version `v0.1` → `v0.3`（對齊 qa_type_registry.template.yaml 權威）
- §8.2 Template 範例 8 個 core qa_type `template_path` 從簡名（如 `09_a_AI_味檢查表.md`）改成完整相對路徑（`09_quality_assurance/09_a_ai味qa報告模板.md` 等 8 條），對齊 qa_type_registry.template.yaml line 13-50
- §8.3 Instance 範例 schema_version `v0.1` → `v0.3`

**§9.1 JSON export manifest（NEW_REQ_4 同類擴充）：**
- `"spec_version": "data_format_spec_v0.1"` → `"data_format_spec_v0.4"`（對齊本輪 DF 當前版本）

**§11.1.2 dialogue_keys parser（NEW_REQ_3 細化 — master 第五輪）：**
- 新增 v0.4 驗證規則：若 `dialogue_keys[<KEY>].status = deleted` 但內文仍有對應 `<!-- KEY: <KEY> -->` comment → parser **WARN**（非 ERROR）
- 寬鬆語意保留（漸進刪除友善），落地時機由 Phase A.X 後續 patch 補實作

**§7.3 target_dir schema 語意（NEW_REQ_5 細化 — master 第五輪）：**
- target_dir 型別：string（單一相對路徑 _或_ comma-separated list）
- 多目錄寫法限 S 場景類型（跨 `06_scene_index/` + `07_scene_tasks/` + `08_dialogue_outputs/`）；其他 core 類型一律單一目錄
- Parser split + trim 各段獨立驗證；不採 `target_dirs: list[str]` 變更（POST_LOCK_PENDING 選 b — 最小變動）

**§8.3 / §8.10 user_extensions 對齊（CODEX (e) recheck patch — Finding E-F1 + E-F2）：**
- §8.3 user_extensions 範例 line 1898 `template_path` 短路徑 → repo-root 完整相對路徑 `09_quality_assurance/09_j_設定一致性檢查.md`（對齊 §8.2 + UD §3.10.2 寫法）
- §8.3 Instance-only 欄位表 `template_path` 說明改「repo-root 完整相對路徑」（line 1912）
- §8.3 user_extensions 範例 + Instance-only 欄位表 **補 `algorithm` / `report_template` 為選填欄位**（對齊 UD §3.10.2 line 3650-3660 引入的 NEW_REQ_6 對齊新欄位 + UD §3.10.3 §2-§3 對應）
- §8.10 parser impact 補「algorithm / report_template 為選填，parser 不強驗內部結構」行為描述

**不在本輪 scope：**
- §5.1a v0.2 patch（D-044 7 subtype 主規格段）已 LOCKED — 本輪不動
- §3.10 NEW_REQ_6 由 stage 5 處理 UD 端（DF 端 §8 user_extensions schema 對齊由 CODEX (e) recheck patch 補）
- M1/M3/M4 + m1-m3 由 Gate 1 後續輪處理

# DATA_FORMAT_SPEC — Game Dialogue Bible 資料格式規格（第二輪）

# 0. 文件目的與閱讀者

## 0.1 文件性質

本檔是「**資料格式 specialist 第二輪交付**」。在 user 拍板 Bucket #1–#4（REQUIREMENTS_LOCK v1.0 / DECISIONS_LOG §6.6 D-021 ~ D-034）後的最終 schema 設計，承接：

- 第一輪 specialist starter（SPECIALIST_STARTER_DATA_FORMAT.md）提的 6 個強制檢視議題（D-018 promote 為最終）
- 第二輪 11 條任務（REVISED_WORK_ITEMS §7.3 DF-1 ~ DF-11）

**本檔不是：**

- 不是主 SPEC — 主 SPEC §5.1 / §5.2 仍是 canonical schema 權威來源（本檔只能提案擴充，不能 supersede 核心）
- 不是 protocol 檔 — 不寫 skill 流程（屬上下游 specialist UPSTREAM_DOWNSTREAM_SPEC）
- 不是 UI 設計 — 不寫呈現（屬 UX specialist UX_SPEC）
- 不是執行任務 — 不直接修改 SPEC / ARCHITECTURE / TASKS（由 master 第四輪整合）

## 0.2 閱讀者

| 閱讀者 | 用途 |
|---|---|
| 上下游 specialist 第二輪 | Contract A 真實介面 — UD-3 / UD-4 / UD-5 / UD-10 細化依據 |
| UX specialist 第二輪 | 前端工具呈現 F1–F7 的資料形狀依據 |
| Master 第四輪整合 | 升 INTEGRATION_CONTRACTS v2 + 整合進主 SPEC / ARCHITECTURE / TASKS |
| 未來重啟對話的接手 agent | 4-Bucket 拍板後資料層的權威快照 |
| user | rolling 確認 schema 對齊需求 |

## 0.3 與其他文件的關係

```
                    REQUIREMENTS_LOCK.md v1.0 (FINAL)
                              │ 衍生
                              ↓
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
   DATA_FORMAT_SPEC.md   UX_SPEC.md v0.2  UPSTREAM_DOWNSTREAM_SPEC.md v0.2
    （本檔，v0.1）       （平行 specialist） （平行 specialist）
            │
            │ Contract A 真實介面
            ↓
   上下游 specialist UD-3/4/5/10 細化
   UX specialist 前端工具資料形狀
            │
            └──→ Master 第四輪整合 → 升 INTEGRATION_CONTRACTS v2
                                  → 整合進主 SPEC / ARCHITECTURE / TASKS
                                  → promote 本檔提案為 D-NNN 或 supersede
```

## 0.4 版本歷史

| 版本 | 日期 | 變更 |
|---|---|---|
| v0.1 | 2026-05-18 | 初版交付，含 DF-1 ~ DF-11 全條 |
| **v0.2** | **2026-05-19** | **CODEX (c) 審查後 master 第四輪整合 P0/P1 patch：D-037（dialogue_keys list → Map）/ D-042（phase_log 補 5 新欄位）/ D-044（A-\* subtype 7 種）/ D-045（A-\* 不入 narrative `/status`）/ O-01（§12 語氣調整）** |

**v0.2 patch 來源：**
- `CODEX_REVIEW_REPORT.md`（C-01 / C-04 / C-05 / C-07 / C-09 / C-10 / C-13 / C-14 / O-01 識別衝突）
- `DECISIONS_LOG.md §6.7`（D-037 ~ D-046 master 第四輪整合拍板）
- `L3_EXPORT_PROMPT_SCHEMA.md v0.1`（D-038 附帶 prompt contract — 本檔 §9 JSON schema 是其引用 contract）

**v0.2 對 v0.1 的 partial supersede 範圍：**
- §4.2 `dialogue_keys` schema：list of objects → **Map (DICT)**（D-037）
- §4.5 KEY 生命週期：`[DELETED]` prefix → `status / deleted_at / deprecated_reason` metadata（D-037 + C-10）
- §3 phase_log：補 5 新欄位（D-042）
- §5.1 A-\* `id_pattern` subtype：5 種 → 7 種（D-044）
- §5.6 A-\* 完成度：移除 `/status` narrative completeness（D-045）
- §12 master 裁決清單：「無需 master 裁決」→「P0/P1 patch 完成，無新增議題」（O-01）

**v0.2 不變範圍：**
- 既有 §0.1-§0.3 / §1.1-§1.2 / §2 / §6 / §7 / §8 / §9 核心結構（僅 §9.5 dialogue_line record 對齊 Map shape）
- 主 SPEC §5.1 / §5.2 LOCKED 段（partial supersede 維持 v0.1 寫法）
- 既有 27 模板 frontmatter 零破壞原則
- CODEX tier 1 已寫的 9 份協議檔

---

# 1. 既有 schema 評估（基線回顧）

## 1.1 SPEC §5.2 canonical schema 評估（本輪不動核心）

**結論：核心結構維持不動，僅以「可選欄位 / 副節 / 機制」方式擴充。**

| 維度 | 既有狀態 | 本輪變動 |
|---|---|---|
| 中文 header 5 欄（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級） | LOCKED | **不動** |
| YAML 上游 3 欄（entities / depends_on / weight） | LOCKED | **不動** |
| YAML 下游 8 欄（scene_id / source_task / source_dialogue / source_dialogues / pipeline_state / mode_tag / qa_decision / qa_type） | LOCKED | **不動核心**；但 mode_tag enum 加 1 值（DF-8）/ qa_type 變可擴充 list（DF-6） |
| 狀態 enum 7 種（DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED） | LOCKED | **不動** |
| pipeline_state enum 9 種 | LOCKED | **不動** |
| mode_tag enum 5 種 | LOCKED | **partial supersede 加 SINGLE_ITER（DF-8）** |
| qa_decision enum 4 種 | LOCKED | **不動** |
| qa_type enum 5 種 | LOCKED | **partial supersede 加 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY（DF-8）+ 變可擴充 list（DF-6）** |
| §5.2.5 規則 6 條 | LOCKED | **不動核心**；A-\* entity 比照上游檔處理 |
| §5.2.6 場景 ID 分支後綴 | LOCKED | **不動** |

## 1.2 SPEC §5.1 既有 entity 類型評估

**結論：既有 7 種（W-rules / W-language / V / C-\* / R-\*-\* / P / CH-\<n\> / S-\<ch\>-\<n\>）維持 LOCKED；本輪新增 A-\* 美術資產（DF-4），並建立可擴充 registry 機制（DF-5）讓未來再加 I-\* / UI-\* / SKILL-\* 等不必動 SPEC §5.1。**

## 1.3 本輪改動總覽（v0.2 一覽）

| 區塊 | 性質 | 對應 DF | 對應 D/P | v0.2 patch |
|---|---|---|---|---|
| §2 D-018 6 項最終裁決 formalize | 整理 / 紀錄 | DF-1 | D-018 / P-006 / 含 D-022 / D-024 / D-026 partial supersede 標記 | — |
| §3 phase_log 擴充（status + import_source + **5 新欄位**） | 新增可選欄位 | DF-2 | P-012 / D-031 / **D-042** | **+5 新欄位 entities_touched / iteration_count / iteration_note / base_dialogue / conflict_resolutions** |
| §4 i18n KEY 機制 | 新增 frontmatter **Map** + 內文行內標記規範 | DF-3 | D-022 / P-022 / **D-037** | **list → Map (DICT)；KEY lifecycle metadata 取代 [DELETED] prefix** |
| §5 A-\* 美術資產 entity | 新增 entity 類型 + 目錄結構 + frontmatter 模板 | DF-4 | D-023 / P-021 / **D-044 / D-045** | **subtype 5→7 種（portrait/bg/cg/sfx/bgm/voice/ui）；完成度不入 `/status` narrative** |
| §6 mode_tag / qa_type 新 enum 值 | enum 擴值 + schema 級紀錄 | DF-8 | D-026 / D-028 | — |
| §7 可擴充 entity 類型 registry | 新增 registry 機制（Template / Instance / parser） | DF-5 | D-025 / P-023 | — |
| §8 可擴充 qa_type registry | 新增 registry 機制 + 00_p 接點 | DF-6 | D-027 / P-023 | — |
| §9 JSON 中介格式 schema | 新增 Layer 3 export 輸出 schema | DF-7 | D-024 / P-024 / **D-039** | **dialogue_line record 對齊 Map shape（含 portrait/bgm/sfx/status）** |
| §10 對既有 27 份模板遷移影響 | 衝擊評估 | DF-9 | 例行 | 對齊 v0.2 patch |
| §11 對 A.0 parser 影響 | 衝擊評估 | DF-10 | 例行 | **§11.1.2 / §11.1.4 對齊 v0.2 patch** |
| §12 需 master 裁決問題清單 | 升 master 議題 | DF-11 | 例行 / **O-01** | **語氣調整：v0.1「無需 master 裁決」→ v0.2「P0/P1 patch 完成，無新增議題」+ P-021~P-024 重新標 RESOLVED via D-037~D-044** |

---

# 2. D-018 6 項最終裁決 formalize（DF-1）

## 2.0 本節性質

本節正式 formalize SPEC §3.1「已確認不採的擴充提案（v1.3 — D-018 promote 為最終）」 6 項在第二輪資料格式 spec 內的最終結論。標記 partial supersede 處明示對應的新 D（D-022 / D-024 / D-026）。

**第一輪 specialist starter 第 2 節 6 個強制檢視議題（議題 A–F）一一對齊：**

## 2.1 議題 A：retcon vs supersede 區分 — 最終不採用（維持 D-018）

**第一輪提案：** 新增 `retcon_of` / `retcon_status` 欄位、新增 `RETCONNED` 狀態、新增 09_g_retcon_紀錄 模板。

**結論：最終不採用。**

**裁決理由：**
- 09_e「定稿變更紀錄」已涵蓋人類裁決層的 retcon 紀錄需求
- retcon 走 UPSTREAM §3.6.6 路徑：09_e 紀錄 + 原版降 DEPRECATED + 新版本走完整 pipeline
- 不擴充 frontmatter 欄位 / 不擴充狀態 enum / 不新增 QA 模板（09_g 編號已分配給「節奏感」見 D-026 / 本檔 §6）

**Schema 行為：**
- ✗ 不新增 `retcon_of: <path>` frontmatter 欄位
- ✗ 不新增 `retcon_status: ACTIVE | RETCONNED` frontmatter 欄位
- ✗ 不新增 `狀態: RETCONNED`（維持 7 狀態 enum LOCKED）
- ✗ 不新增 `09_g_retcon_紀錄` 模板（09_g 編號重新分配給「節奏感」）

**對既有 27 份模板遷移影響：** 無。

**對 A.0 parser 影響：** 無。

**Cross-ref：** D-018 #1 / SPEC §3.1 第 1 列 / UPSTREAM §3.6.6。

---

## 2.2 議題 B：多語言對白支援 — partial supersede via D-022（i18n KEY 機制）

**第一輪提案：** 新增 `language: zh-Hant | en | ja | ...` 欄位、新增 `translation_of: <path>` 欄位 / 同檔多區段 vs 不同檔 cross-reference。

**結論：partial supersede — 「不存多語本文」維持 D-018 #2 最終不採；但**新增每段台詞 unique i18n KEY 機制**（D-022），KEY 供外部 i18n 系統引用。**

**裁決理由：**
- D-022 確認「多語對白本文不存」維持（本檔不變 frontmatter `language` 欄位、不變 `translation_of` 欄位）
- 但「多段台詞 unique 識別」是 D 視覺化管理 + Layer 3 export 給外部轉檔的剛需 → 加 KEY 機制
- KEY 跟內容/編號完全解耦：場景重編號 / 台詞改寫 KEY 不變；KEY 命名空間全 repo unique
- 工具自動產語意可讀預設（如 `dlg.ch01.s03.l001`）+ user 可隨時改名 → 改名後預設名內部記為 alias

**Schema 行為：**
- ✗ 不新增 `language: <code>` frontmatter 欄位（同 D-018 #2）
- ✗ 不新增 `translation_of: <path>` frontmatter 欄位（同 D-018 #2）
- ✓ **新增 `dialogue_keys` block（frontmatter 內）+ 內文 HTML comment `<!-- KEY: <key> -->` 雙軌（詳見 §4 DF-3）**
- ✓ KEY alias mapping 在 `dialogue_keys` block 中表達（詳見 §4）

**對既有 27 份模板遷移影響：** 08_b 台詞模板需加 `dialogue_keys` block 範例（A.4 處理）；27 份既有上游模板無影響（KEY 只用於下游台詞檔）。

**對 A.0 parser 影響：** parser 需多解析 `dialogue_keys` block 與內文 `<!-- KEY: ... -->` 註解；KEY 全 repo unique 驗證。詳見 §11。

**Cross-ref：** D-018 #2 partial supersede / D-022 / P-022 / 本檔 §4。

---

## 2.3 議題 C：continuity_check 獨立實體 — partial supersede via D-026（跨場 QA 模板）

**第一輪提案：** 新增 entity 類型 `CC-<id>` / `CC-<topic>`、新增資料夾 `09_quality_assurance/continuity_checks/`。

**結論：partial supersede — 「不採 CC-\* 獨立 entity」維持 D-018 #3 最終不採；但**新增 09_g 節奏感 / 09_h 對話張力 / 09_i 跨場一致性 三份 QA 模板**（D-026），qa_type enum 加 3 種（DF-8）。**

**裁決理由：**
- D-018 #3 不採「continuity 獨立 entity」維持 — 不增 CC-\* 類型 / 不建 continuity_checks/ 資料夾
- 但跨集 / 跨場景一致性檢查的「散在 09_b（角色聲線）+ 09_d（資訊控制）內」這個問題，由 09_i 跨場一致性 QA 模板正式處理（不再「散在」）
- 同時 09_g 節奏感 / 09_h 對話張力 補齊更廣的 QA 維度
- 對應 09_g/h/i 的具體檢查 algorithm 屬上下游 specialist UD-6 範圍，本檔只負責 schema 級紀錄

**Schema 行為：**
- ✗ 不新增 entity 類型 `CC-<id>`（維持 SPEC §5.1 既有 7 種 LOCKED + 本輪新增 A-\* 為唯一新類型）
- ✗ 不新增資料夾 `09_quality_assurance/continuity_checks/`
- ✓ **qa_type enum 加 3 種：`RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY`（DF-8 細化）**
- ✓ **qa_type 變可擴充 list（DF-6 細化）** — 未來再加新 09_x 不必動 SPEC §5.2.4
- ✓ 既有 09_b / 09_d 模板維持原樣（不再承擔跨集統籌責任，但仍跑各自既有 algorithm）

**對既有 27 份模板遷移影響：** 09_b / 09_d 模板 frontmatter 不動；新增 09_g / 09_h / 09_i 三份模板（屬上下游 specialist UD-6 範圍，本檔只承諾 schema 容納 3 個新 qa_type 值）。

**對 A.0 parser 影響：** qa_type 從 LOCKED enum 變開放可擴充 list；parser 改驗證邏輯（詳見 §8 + §11）。

**Cross-ref：** D-018 #3 partial supersede / D-026 / D-027 / P-025 / 本檔 §6 + §8。

---

## 2.4 議題 D：scene 粒度（exchange-level） — 最終採策略 A（維持 D-018）

**第一輪提案：** 支援策略 B（exchange-level 細粒度）+ frontmatter 加 `exchange_in_scene: <number>` + 場景 ID 擴 `S-01-03-e2`。

**結論：最終採策略 A（一場戲一個 dialogue 檔），不採策略 B。**

**裁決理由：**
- D-018 #4 確定維持策略 A
- 長場景由人類拆分為主場景 + 分支（§5.2.6 分支後綴規則照舊 `S-01-03a` / `S-01-03sub`）
- 策略 B 的 `S-01-03-e2` ID 命名會跟既有分支後綴 `S-01-03a` 衝突

**Schema 行為：**
- ✗ 不新增 `exchange_in_scene: <int>` frontmatter 欄位
- ✗ 不擴 scene ID 命名規則 `S-<ch>-<n>-e<exchange>`
- ✓ 維持 §5.2.6 分支後綴規則：`S-01-03a` / `S-01-03b` / `S-01-03sub`

**對既有 27 份模板遷移影響：** 無。

**對 A.0 parser 影響：** 無。

**Cross-ref：** D-018 #4 / SPEC §5.2.6。

---

## 2.5 議題 E：protected_tier 多層保護 — 最終不採用（維持 D-018）

**第一輪提案：** 新增 `protected_tier: public | collaborator | internal | client | locked` 欄位。

**結論：最終不採用。**

**裁決理由：**
- D-002 / D-018 #5 確定不採（個人專案）
- LOCKED 狀態已涵蓋唯一保護需求

**Schema 行為：**
- ✗ 不新增 `protected_tier: <enum>` frontmatter 欄位
- ✓ LOCKED 狀態維持唯一保護手段（屬狀態 enum 既有值）

**對既有 27 份模板遷移影響：** 無。

**對 A.0 parser 影響：** 無。

**Cross-ref：** D-002 / D-018 #5 / SPEC §3.1 第 5 列。

---

## 2.6 議題 F：使用者的「特殊資料格式」 — partial supersede via D-024（JSON+MD 雙吐）

**第一輪提案：** 「不知道具體是什麼，在對話中釐清」 — 第一輪結論 Phase D 後另議。

**結論：partial supersede — 「Phase D 後另議」改為**本輪正式設計縮減版 export**（D-024）：Layer 3 export 一個 skill 吐 JSON + MD 雙檔；「轉檔到引擎」明確劃在工具外。**

**裁決理由：**
- user 在 Bucket #1 明確「採固定輸出一種格式 + 外部轉檔來限縮工具規模」
- D-024 確定：JSON 給外部轉檔 script 吃 / MD 給人讀 / 不做多套版 framework / 不做 `/create-template` skill
- 工具規模收斂；schema 範圍明確（JSON 中介格式 DF-7 細化）

**Schema 行為：**
- ✗ 不做多套版 framework（不增 `template_id` / `template_version` 等 frontmatter 欄位）
- ✗ 不做工具預設套版庫（不增 `_design/templates/` 套版範本目錄）
- ✗ 不做套版輸出預覽（屬 UX specialist 已排除 F9）
- ✗ 不做多套版同跑批次（屬 UX specialist 已排除 F10）
- ✓ **新增 Layer 3 export JSON 中介格式 schema（DF-7 詳見 §9）**
- ✓ JSON 含 records[] array + manifest header（單檔 dump，依 user 修正方向 #4）

**對既有 27 份模板遷移影響：** 無（既有模板 frontmatter 不動，export 是「讀取既有模板 → 吐 JSON+MD」單向流程）。

**對 A.0 parser 影響：** parser 不直接負責 export；export skill（屬上下游 UD-3 設計）讀已 parse 的資料結構產 JSON。詳見 §9 + §11。

**Cross-ref：** D-003 / D-018 #6 partial supersede / D-024 / P-016 / P-024 / 本檔 §9。

---

## 2.7 6 項裁決對既有設計衝擊總表

| # | 議題 | 裁決 | Schema 改動 | 27 模板遷移 | A.0 parser 改動 |
|---|---|---|---|---|---|
| A | retcon | 不採（維持 D-018） | 無 | 無 | 無 |
| B | 多語對白 | partial supersede via D-022 | 新增 `dialogue_keys` block + 內文 KEY 註解 | 08_b 加 KEY 範例 | 解析 KEY + 全 repo unique 驗證 |
| C | continuity 獨立 entity | partial supersede via D-026 | qa_type enum 加 3 種 + 變可擴充 | 09_b/d 不動；新增 09_g/h/i（上下游 owner） | qa_type 改開放驗證 |
| D | scene 粒度 | 不採（維持 D-018） | 無 | 無 | 無 |
| E | protected_tier | 不採（維持 D-018） | 無 | 無 | 無 |
| F | 特殊資料格式 | partial supersede via D-024 | 新增 JSON 中介格式（出口層 schema） | 無 | export 不在 parser 範圍 |

---

# 3. phase_log 微擴充（DF-2）

## 3.0 本節性質

formalize `.protocol_version.phase_log` 兩個新增欄位：

1. **`status`** — P-012 暫定原 D-014；SPEC §5.4 已寫入但標「暫定」；本檔正式 promote 為交付建議
2. **`import_source`** — 對應 D-031 跳階段機制做手稿導入；新建議欄位

兩欄位皆屬 `.protocol_version` 內部 phase_log entry 結構，**不動 SPEC §5.2 canonical schema（中文 header + YAML block）**。

## 3.1 phase_log 完整 entry schema（v0.2 提案）

**v0.2 變更（per D-042 + CODEX C-07 / C-09 / O-04 解決）：** v0.1 只 formalize `status + import_source` 兩欄；v0.2 全收 UD 已用的 5 新欄位（`entities_touched / iteration_count / iteration_note / base_dialogue / conflict_resolutions`）。SINGLE_ITER lineage **走獨立 `base_dialogue` 欄位**，**不重用 SPEC 鎖定的 `source_dialogues`**（SPEC §5.2.3 維持「`source_dialogues` 僅 --converge v02」鎖定語義）。

```yaml
phase_log:
  - phase: <phase_name>                # 既有：bootstrap / create-world / create-character / ... / scene-task / dialogue-write / qa
    date: YYYY-MM-DD                   # 既有
    skill: /<skill_name>               # 既有
    status: <status_enum>              # DF-2.1（formalize P-012）— completed | in_progress | aborted
    import_source: <import_enum>       # DF-2.2（v0.1，對應 D-031）— agent_assisted | external_llm | null
    created_entities: [<id>, ...]      # 既有（多數 phase）
    entities_touched: [<id>, ...]      # DF-2.3（v0.2 新，對應 D-042）— 多場景 mutex
    iteration_count: <int>             # DF-2.4（v0.2 新，對應 D-042）— SINGLE_ITER 第幾次
    iteration_note: <free text>        # DF-2.5（v0.2 新，對應 D-042）— 本次迭代意圖
    base_dialogue: <file_path>         # DF-2.6（v0.2 新，對應 D-042 + C-09 解決）— SINGLE_ITER lineage 來源；獨立欄位，不重用 source_dialogues
    conflict_resolutions: [<dict>, ...]# DF-2.7（v0.2 新，對應 D-042）— 手稿導入命名衝突 4 選項紀錄
    customizations: [...]              # 既有（bootstrap）
    scene_id: <S-id>                   # 既有（下游 phase）
    task_path: <path>                  # 既有（scene-task）
    dialogue_paths: [<path>, ...]      # 既有（dialogue-write）
    target_dialogue: <path>            # 既有（qa）
    qa_report_paths: [<path>, ...]     # 既有（qa）
    qa_decision: <qa_decision_enum>    # 既有（qa）
    mode_tag: <mode_tag_enum>          # 既有（dialogue-write）
    abort_reason: <enum>               # 既有（status=aborted）
    detail: <free text>                # 既有（status=aborted）
```

## 3.2 新欄位 1：`status`（DF-2.1，formalize P-012）

**值域 enum：**

| 值 | 意義 | 寫入時機 |
|---|---|---|
| `in_progress` | skill 進入階段 1 後寫入 | skill 階段 1 開始時 append 一筆 entry 並寫 `status: in_progress` |
| `completed` | skill 正常完成階段 5 | skill 階段 5 結束時把同一筆 entry 改為 `status: completed` |
| `aborted` | skill 因並行衝突 / rollback 等中止 | abort 發生時把同一筆 entry 改為 `status: aborted` + 寫 `abort_reason` + `detail` |

**規則：**
- 預設不省略；若無 `status` 欄位 parser 視為 `in_progress`（保守解讀）
- `status: aborted` 必填 `abort_reason` + `detail`（UPSTREAM §6.7 既有要求）
- `status` 從 `in_progress` → `completed` 或 `in_progress` → `aborted` 是 in-place 修改同一筆 entry，不另開新 entry

**對既有 SPEC §5.4 影響：** SPEC §5.4 phase_log schema 已預先寫入 `status` 欄位且標「P-012 暫定」；本檔 formalize 後即可移除「暫定」標記。詳見 §10 + §11。

## 3.3 新欄位 2：`import_source`（DF-2.2，對應 D-031）

**值域 enum：**

| 值 | 意義 | 寫入時機 |
|---|---|---|
| `null`（或省略） | 既有路徑 — user 依序跑 `/create-*` skill，無跳階段、無手稿導入 | 預設值 |
| `agent_assisted` | user 在外部 agent 工具編輯過手稿後跳階段導入；**僅紀錄上游來源；不提供品質 gate 豁免**（v0.3 master 第四輪 CC-06 校正）| user 在 `/create-world` 等 skill 對話中說「直接寫檔 --trust-level agent_assisted」（D-032 markdown structure 解析；D-033 命名衝突處理）後寫入 |
| `external_llm` | user 從外部 LLM 拿到未審手稿後跳階段導入；**僅紀錄上游來源；下游 pipeline 不受影響**（v0.3 master 第四輪 CC-06 校正）| user 在 `/create-world` 等 skill 對話中說「直接寫檔 --trust-level external_llm」後寫入 |

**規則：**
- 屬「該次 skill 呼叫的執行 context」紀錄；不是 phase 本身的屬性
- `null` 與「欄位省略」語意等價（向後相容既有路徑 — 既有 phase_log entry 不需追溯補欄位）
- 若 `import_source ≠ null` 但 skill 不是 `/create-*` 系列 → parser 視為錯誤（手稿導入只發生在上游創建 skill）
- `import_source` 不影響 `created_entities` 列表（手稿導入 vs 正常路徑都產同樣 entity 集合）

**trust-level 嚴格邊界（v0.3 master 第四輪 CC-06 校正；對齊 INTEGRATION_CONTRACTS Contract A.8 + UD §10.3 v0.3 + SPEC §5.4a）：**

- **trust-level 只記錄資料來源，不影響任何下游 pipeline 決策**
- agent **不得**依 `import_source: agent_assisted` 把下游 dialogue 升 `DIALOGUE_FINAL`
- agent **不得**依 `import_source: agent_assisted` 跳過 §6.2 / SPEC §12.7 的 8 份 QA 必跑流程
- 下游 `/scene-task` / `/dialogue-write` / `/qa` pipeline 永遠走標準 DRAFT → QA → REVIEW → FINAL
- 兩條 trust-level 路徑差別**僅在** phase_log 紀錄（`import_source` 值 + 可選 `recommended_followup`）

**v0.2 → v0.3 寫法變動（CC-06 解決）：**
- v0.2 寫法：「`agent_assisted` 路徑：對應 pipeline_state 可直接跳到 `DIALOGUE_FINAL`（跳 QA）」+「`external_llm` 路徑：必從 DRAFT 起跑完整 QA」
- **v0.3 寫法：兩條路徑下游 pipeline 行為相同（都走標準 pipeline）；trust-level 不提供品質 gate 豁免**
- 理由：CODEX C-08 + master 第四輪 CC-06 — trust-level 邊界嚴格限上游；下游 pipeline 不受影響

## 3.3a 新欄位 3：`entities_touched`（DF-2.3，v0.2 — 對應 D-042 + C-07 解決）

**用途：** 紀錄該次 skill 呼叫期間「讀 + 寫」的所有 entity ID，供多場景並行時的 mutex 機制使用。

**值域：** `List[entity_id]`（entity ID 必須符合 §7.1 entity_type_registry 中任一 type 的 `id_pattern`）

**規則：**
- 屬「該次 skill 呼叫的執行 context」紀錄
- `entities_touched` ⊇ `created_entities`（凡是有 created 的必有 touched；touched 還包含「只讀不寫」的 entity）
- 若無多場景並行需求，可省略；省略 → parser 視為空 list（保守解讀）
- `status: aborted` 時若有 `abort_reason: parallel_conflict`，`entities_touched` 必填（給並行衝突排查用）

**範例：** 跑 `/dialogue-write S-01-03` 期間讀了 `C-主角A` / `C-反派B` / `R-主角A-反派B` 三份聲線資料，且寫了 `S-01-03` 一份台詞檔 → `entities_touched: [C-主角A, C-反派B, R-主角A-反派B, S-01-03]`。

## 3.3b 新欄位 4：`iteration_count`（DF-2.4，v0.2 — 對應 D-042）

**用途：** 紀錄 `/dialogue-write --single-iter` 模式下這份 dialogue 檔是第幾次迭代產物。

**值域：** `int`（從 1 起算；非 SINGLE_ITER 模式時為 null 或省略）

**規則：**
- 僅 `mode_tag: SINGLE_ITER` 時有意義；其他 mode_tag 一律 null 或省略
- 第一次跑 SINGLE_ITER 寫 `iteration_count: 1`
- 後續每次迭代 `iteration_count` += 1
- 跟 `base_dialogue` 配對使用 — `iteration_count: N` 的檔指向 `iteration_count: N-1` 的檔作為 `base_dialogue`

## 3.3c 新欄位 5：`iteration_note`（DF-2.5，v0.2 — 對應 D-042）

**用途：** 紀錄本次 SINGLE_ITER 迭代的意圖（user 跟 agent 在迴圈中討論時的修改方向摘要）。

**值域：** free text（建議 1-3 句話）

**規則：**
- 僅 `mode_tag: SINGLE_ITER` 時有意義
- 內容由 `/dialogue-write --single-iter` 提示 user 輸入（屬上下游 UD-7 範圍）
- 無內容時 null 或省略
- export JSON 時保留（讓外部 i18n / 翻譯系統能追溯版本演化）

**範例：** `iteration_note: "user 要求把主角A 第 2 句改更冷峻，把反派B 第 4 句改得更挑釁"`。

## 3.3d 新欄位 6：`base_dialogue`（DF-2.6，v0.2 — 對應 D-042 + CODEX C-09 解決）

**用途：** 紀錄 SINGLE_ITER 模式下「上一輪迭代的檔案路徑」 — 提供 lineage 追溯。

**值域：** file_path（相對 Instance root）

**為何不重用 `source_dialogues`：**

- SPEC §5.2.3 明確鎖定 `source_dialogues: list[path]` 僅 `--converge` 產出的 v02 用，列出本次收斂引用的 trial 路徑
- 重用會造成「收斂 lineage vs SINGLE_ITER lineage 同欄位混語義」 — CODEX C-09 critical
- 採新獨立欄位 `base_dialogue: str` 解決：
  - SPEC §5.2.3 維持鎖定不變
  - SINGLE_ITER lineage 走 `base_dialogue`
  - 兩條 lineage 走不同欄位，前端 Z1 並排 / 收斂可視化 / SINGLE_ITER 迭代追溯不混用

**規則：**
- 僅 `mode_tag: SINGLE_ITER` 時有意義（其他 mode_tag null 或省略）
- 第一次跑 SINGLE_ITER（`iteration_count: 1`）時 `base_dialogue: null`（無上一輪）
- 第二次起（`iteration_count >= 2`）必填，指向 `iteration_count - 1` 的檔
- 不允許 cycle：`base_dialogue` 指向的檔的 `base_dialogue` 鏈條不能形成迴圈（parser ERROR 偵測）

## 3.3e 新欄位 7：`conflict_resolutions`（DF-2.7，v0.2 — 對應 D-042 + D-033）

**用途：** 紀錄手稿導入（D-031）時遇到 entity 命名衝突的 4 選項拍板紀錄（D-033 merge / overwrite / create-as-new / skip）。

**值域：** `List[dict]`，每個 dict schema：

```yaml
- entity_id: <衝突的 entity ID>            # 必填
  decision: <enum>                          # merge | overwrite | create-as-new | skip
  new_entity_id: <new ID>                   # 僅 decision=create-as-new 時填（如 C-主角A_v2）
  resolved_at: YYYY-MM-DD                   # 必填
  detail: <free text>                       # 可選；user 拍板理由
```

**規則：**
- 僅 `import_source ≠ null` 時有意義
- 無衝突時 null 或省略
- 一筆衝突一筆 dict；同次 skill 呼叫可累積多筆
- `decision: skip` 表示 user 拒絕導入該 entity；對應在 `created_entities` 中**不出現**該 entity ID
- `decision: create-as-new` 必填 `new_entity_id`；對應 `created_entities` 中出現 `new_entity_id`（不是原 `entity_id`）

**範例：**

```yaml
conflict_resolutions:
  - entity_id: C-主角A
    decision: merge
    resolved_at: 2026-05-19
    detail: 手稿版聲線描述併入既有聲線卡的「進階性格」段
  - entity_id: C-夥伴C
    decision: create-as-new
    new_entity_id: C-夥伴C_v2
    resolved_at: 2026-05-19
    detail: 手稿版跟既有 C-夥伴C 是不同角色（user 拍板分開）
  - entity_id: R-主角A-反派B
    decision: skip
    resolved_at: 2026-05-19
    detail: 既有 R-* 比手稿版更新；跳過導入
```

## 3.4 phase_log 完整範例（v0.2 — 含 7 個新欄位）

```yaml
phase_log:
  # 既有路徑（import_source 省略或 null）
  - phase: bootstrap
    date: 2026-05-17
    skill: /init-project
    status: completed
    created_entities: []
    customizations: [...]

  # 既有路徑（依序跑 /create-world）
  - phase: create-world
    date: 2026-05-18
    skill: /create-world
    status: completed
    entities_touched: [W-rules, W-language, V]  # v0.2 — 多場景 mutex
    created_entities: [W-rules, W-language, V]

  # 手稿導入路徑 1（agent_assisted）+ 命名衝突 4 選項紀錄
  - phase: create-character
    date: 2026-05-19
    skill: /create-character
    status: completed
    import_source: agent_assisted               # v0.1（DF-2.2）
    entities_touched: [C-主角A, C-反派B, C-夥伴C_v2]  # v0.2
    created_entities: [C-主角A, C-反派B, C-夥伴C_v2]  # 注意 C-夥伴C_v2（不是 C-夥伴C；衝突 4 選項 create-as-new 拍板）
    conflict_resolutions:                       # v0.2（DF-2.7）— D-033 4 選項拍板紀錄
      - entity_id: C-主角A
        decision: merge
        resolved_at: 2026-05-19
        detail: 手稿版聲線併入既有聲線卡「進階性格」段
      - entity_id: C-夥伴C
        decision: create-as-new
        new_entity_id: C-夥伴C_v2
        resolved_at: 2026-05-19
        detail: 手稿版跟既有 C-夥伴C 是不同角色（user 拍板分開）

  # 手稿導入路徑 2（external_llm）— 跳階段且必走 QA
  - phase: create-outline
    date: 2026-05-20
    skill: /create-outline
    status: completed
    import_source: external_llm                 # v0.1（DF-2.2）
    entities_touched: [P]
    created_entities: [P]

  # SINGLE_ITER 第 1 次迭代（v0.2 新欄位範例）
  - phase: dialogue-write
    date: 2026-05-22
    skill: /dialogue-write
    status: completed
    scene_id: S-01-03
    entities_touched: [C-主角A, C-反派B, R-主角A-反派B, S-01-03]
    mode_tag: SINGLE_ITER                       # v0.1 DF-8 新增
    iteration_count: 1                          # v0.2（DF-2.4）— 第 1 次
    iteration_note: 初版試寫，主角 A 採理性冷靜路線  # v0.2（DF-2.5）
    base_dialogue: null                         # v0.2（DF-2.6）— 第 1 次無 lineage 來源
    dialogue_paths:
      - 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01_iter1.md

  # SINGLE_ITER 第 2 次迭代（base_dialogue 指向第 1 次）
  - phase: dialogue-write
    date: 2026-05-23
    skill: /dialogue-write
    status: completed
    scene_id: S-01-03
    entities_touched: [C-主角A, C-反派B, R-主角A-反派B, S-01-03]
    mode_tag: SINGLE_ITER
    iteration_count: 2                          # v0.2 — 第 2 次
    iteration_note: user 要求把主角A 第 2 句改更冷峻，反派B 第 4 句更挑釁  # v0.2
    base_dialogue: 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01_iter1.md  # v0.2 — 指向上一輪
    dialogue_paths:
      - 08_dialogue_outputs/CH01_S03_xxx_dialogue_v01_iter2.md

  # in_progress 範例（skill 階段 1 進入時寫入）
  - phase: dialogue-write
    date: 2026-05-24
    skill: /dialogue-write
    status: in_progress                         # v0.1（DF-2.1）— skill 還在跑
    scene_id: S-01-04
    entities_touched: [C-主角A, C-夥伴C_v2, S-01-04]
    mode_tag: DRAFT_TRIAL

  # 並行衝突 abort 範例
  - phase: dialogue-write
    date: 2026-05-25
    skill: /dialogue-write
    status: aborted                             # v0.1（DF-2.1）— 含 abort_reason + detail
    scene_id: S-01-05
    entities_touched: [C-主角A, S-01-05]        # v0.2 — abort 時必填，給排查用
    abort_reason: parallel_conflict
    detail: phase_log.lock 等候 30 秒 timeout；另一個 /scene-task 正在執行
```

## 3.5 對既有 SPEC §5.4 既存 phase_log 範例的對齊

SPEC §5.4 既有範例（lines 337–398）已含 `status: completed` 與 `status: aborted` 兩種值的使用 — 屬 P-012 暫定範例範圍。本檔 formalize 後：

| SPEC §5.4 範例 | 本檔 formalize 後狀態 |
|---|---|
| `status: completed`（既有 bootstrap / create-world / create-character / 等） | ✓ 沿用，移除「P-012 暫定」標記 |
| `status: aborted`（既有並行衝突範例） | ✓ 沿用，移除「P-012 暫定」標記 |
| `status: in_progress`（既有 lines 402） | ✓ 沿用，移除「P-012 暫定」標記 |
| `import_source` | ✗ SPEC §5.4 既有範例尚未含此欄位 — 屬本檔新增；master 第四輪整合時補入 SPEC §5.4 範例 |

## 3.6 對既有 27 份模板遷移影響

phase_log 屬 `.protocol_version`，是 Instance 內部運行紀錄，**不是模板**。既有 27 份 Bible 模板與 9 份 CODEX 協議檔的 frontmatter 全不受影響。

A.0 parser 改 + 各 skill 階段 1 / 5 寫入邏輯需配合更新（屬上下游 UD-10 細化）。

## 3.7 對 A.0 parser 影響

詳見本檔 §11。摘要：
- 新欄位皆可選 — parser 接受省略
- `status` 預設視為 `in_progress`（保守解讀，避免誤判 skill 已完成）
- `import_source` 預設視為 `null`
- `status: aborted` 必有 `abort_reason` + `detail`，否則 parser ERROR

---

# 4. i18n KEY 機制（DF-3）

## 4.0 本節性質

實作 D-022「每段台詞需 unique KEY」最終裁決的 schema 層細節。本節決定：

- KEY 命名語法（§4.1）
- KEY 在台詞檔內的儲存位置（§4.2 frontmatter + §4.3 內文 HTML comment 雙軌）
- KEY alias mapping 結構（§4.4）
- KEY 生命週期與全 repo unique guarantee（§4.5 + §4.6）

**設計原則（依 D-022 / Bucket #1 拍板）：**

- 每段台詞 unique KEY（如 `dlg.ch01.s03.l001`）
- 工具自動產語意可讀預設 + user 可隨時改名
- 改名後預設名內部記為 alias；工具保證 alias mapping 不 break
- KEY 跟內容/編號完全解耦：場景重編號 / 台詞改寫 KEY 不變
- 不存多語對白本文（維持 D-018 #2）— KEY 只供外部 i18n 系統引用
- KEY 命名空間全 repo unique guarantee

**KEY 解決什麼 schema 問題：** D-022 partial supersede「不採多語本文」維持，但每段台詞 unique KEY 是 D 視覺化管理 + Layer 3 export 給外部轉檔的剛需。沒 KEY 時外部 i18n 系統無法引用「第 1 章第 3 場第 5 句台詞」（重編號 / 改寫後 line index 就 break）。

## 4.1 KEY 命名規則

**預設語法：**

```
dlg.<chapter>.<scene>.<line>
```

例：`dlg.ch01.s03.l001`、`dlg.ch12.s02.l045`

**欄位定義：**

| 欄位 | 格式 | 對應 |
|---|---|---|
| 前綴 | `dlg` 固定 | 識別為「dialogue 類 KEY」（未來如有 ui / item 類 KEY 用其他前綴；DF-5 entity registry 對應） |
| `<chapter>` | `ch<NN>`（兩位數補零） | 對應 SPEC §5.1 CH-\<n\> entity；如 `ch01` 對應 `CH-01` |
| `<scene>` | `s<NN>`（兩位數補零） | 對應 SPEC §5.1 S-\<ch\>-\<n\> entity 後段；如 `s03` 對應 `S-01-03` |
| `<line>` | `l<NNN>`（三位數補零） | 一場戲內第幾句台詞，從 `l001` 起 |

**保留字符規則：**

- 預設名：全 ASCII 小寫 + 數字 + `.`（避免外部 i18n 系統不相容大寫 / Unicode / 空格）
- user-defined 改名：可用 ASCII 小寫 + 數字 + `.` + `_`（多允許 `_` 給語意命名如 `boss_intro_line_2`）
- 一律不允許：大寫、空格、Unicode、`-` 以外的標點

**分支場景對應：** SPEC §5.2.6 分支後綴 `S-01-03a` 對應 KEY scene 欄位 `s03a`；支線 `S-01-03sub` 對應 `s03sub`。

## 4.2 frontmatter `dialogue_keys` block（v0.2 — Map shape per D-037）

**位置：** 下游台詞檔（`08_dialogue_outputs/` 下）的 YAML block 內，與既有 `scene_id` / `source_task` / `pipeline_state` 等欄位並列。

**v0.2 Schema — Map (DICT) 形式**（v0.1 list of objects partial superseded by D-037）：

```yaml
dialogue_keys:
  dlg.ch01.s03.l001:                 # KEY 作為 map key（unique guarantee 範圍見 §4.6）
    line_index: 1                    # 在本檔內第幾句台詞（1-based）
    speaker: C-主角A                 # 對應 SPEC §5.1 C-* entity；動作描述 / 旁白為 null
    aliases:                         # 改名歷史 list；首位永遠是預設名
      - dlg.ch01.s03.l001            # 預設名（KEY 未改時跟 map key 重複）
    portrait: A-portrait-主角A-anger # 該句台詞對應的 A-portrait-* asset（可省略）
    bgm: A-bgm-tension-01            # 該句台詞對應的 A-bgm-* asset（可省略）
    sfx:                             # 該句台詞對應的 A-sfx-* asset list（可省略）
      - A-sfx-glass-break
    status: active                   # active | deprecated | deleted；§4.5 KEY 生命週期
    created_at: 2026-05-22           # 該 KEY 首次寫入該檔的日期
    renamed_at: null                 # 改名日期；無改名時 null 或省略
    deleted_at: null                 # 刪除日期；status=deleted 時必填
    deprecated_reason: null          # 棄用原因；status=deprecated 時必填
  boss_intro_line_2:                 # user-defined KEY（改名後）
    line_index: 2
    speaker: C-反派B
    aliases:                         # 預設名 dlg.ch01.s03.l002 移到 aliases
      - dlg.ch01.s03.l002
    portrait: A-portrait-反派B-default
    bgm: A-bgm-tension-01            # 同段戲多句 BGM 可重複
    sfx: []                          # 無 sfx 時填空 list
    status: active
    created_at: 2026-05-22
    renamed_at: 2026-05-23
    deleted_at: null
    deprecated_reason: null
  dlg.ch01.s03.l003:                 # 動作描述行（speaker 為 null）
    line_index: 3
    speaker: null
    aliases:
      - dlg.ch01.s03.l003
    portrait: null                   # 動作描述通常不換立繪
    bgm: A-bgm-tension-01
    sfx: []
    status: active
    created_at: 2026-05-22
    renamed_at: null
    deleted_at: null
    deprecated_reason: null
```

**Map key 規則：**

- **Map key 就是當前生效的 KEY** — 不再有獨立 `key:` 欄位
- map key 改變 = user 改名（舊 KEY 移到 `aliases[]` 首位以下；新 KEY 移到 map key 位置）
- map key 的值必須符合 §4.1 KEY 命名規則

**Map value 欄位定義：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `line_index` | 是 | 在本檔內第幾句台詞（1-based，跟內文 KEY 註解的順序對應） |
| `speaker` | 是（值可為 null） | 對應 C-\* / R-\* entity；動作描述 / 旁白填 `null` |
| `aliases` | 是（至少 1 個） | 改名歷史 list；首位永遠是預設名（DF-3 工具自動產的初始 KEY） |
| `portrait` | **是（值可為 null）** | 該句對應的 A-portrait-\* asset_id；無立繪變化時 null（v0.2 — 句級 A-\* 引用權威來源 per C-02 解決） |
| `bgm` | **是（值可為 null）** | 該句對應的 A-bgm-\* asset_id；無 BGM 時 null |
| `sfx` | **是（值可為 \[\]）** | 該句對應的 A-sfx-\* asset_id list；無 SFX 時空 list |
| `status` | **是** | enum：`active` / `deprecated` / `deleted`（v0.2 — KEY lifecycle metadata 取代 v0.1 `[DELETED]` prefix per D-037 + C-10） |
| `created_at` | 是 | KEY 首次寫入該檔的日期 |
| `renamed_at` | 否（無改名時 null 或省略） | 最近一次改名日期 |
| `deleted_at` | 否（`status=deleted` 時必填，否則 null） | 刪除日期 |
| `deprecated_reason` | 否（`status=deprecated` 時必填，否則 null） | 棄用原因（自由文字） |
| `source_keys` | **否（值可為 null 或 list）** | **v0.3 新增 via master 第四輪 CC-04 校正** — 句級收斂 lineage；僅 v02 收斂版台詞檔的 dialogue_keys entry 有意義；list 含本 KEY 從哪些前版 KEY 合併而來（如 `[v01A.l005, v01B.l006]`）；v01 試寫 / SINGLE_ITER iter / FINAL 版填 null |

**規則：**

- `dialogue_keys` block 只在下游 `08_dialogue_outputs/` 台詞檔內出現
- 一份台詞檔內 map key 全部 unique（YAML 本身保證；違反 → parser ERROR）
- 全 repo unique guarantee：map key + 所有 `aliases[*]` 跨檔不可重複（§4.6）
- `aliases` 第一個元素永遠是預設名
- `line_index` 順序必須跟內文 HTML comment 的出現順序一致（§4.3）
- **句級 A-\* 引用權威來源：** `portrait` / `bgm` / `sfx` 欄位為 single source of truth；內文 HTML comment `<!-- 立繪：A-... -->` 僅為 view layer 提示（§4.3 規則更新）
- `status: active` 為預設值（若省略 → parser 視為 active；保守解讀）
- `status: deleted` 必有 `deleted_at`；`status: deprecated` 必有 `deprecated_reason`；違反 → parser ERROR
- **不再使用 `[DELETED]` prefix** — KEY 本身 immutable，lifecycle 由 metadata 表達（v0.2 vs v0.1 主要差異）

## 4.3 內文行內 HTML comment KEY 標記（v0.2 — view layer 提示，非權威來源）

**形式：** 在每段台詞前以 HTML comment 標記 KEY + 選用的 A-\* cross-reference 提示：

```markdown
<!-- KEY: dlg.ch01.s03.l001 -->
<!-- 立繪：A-portrait-主角A-anger -->     <!-- view-layer 提示；權威來源 = frontmatter dialogue_keys -->
<!-- BGM：A-bgm-tension-01 -->            <!-- view-layer 提示；權威來源 = frontmatter dialogue_keys -->
**主角A：** 你以為我會就這樣放棄？

<!-- KEY: boss_intro_line_2 -->
<!-- 立繪：A-portrait-反派B-default -->
<!-- BGM：A-bgm-tension-01 -->
**反派B：** 那就讓我看看你還能撐多久。

<!-- KEY: dlg.ch01.s03.l003 -->
（主角A 低頭沈思了三秒，然後抬頭直視反派B）
```

**v0.2 規則更新（per D-037 + C-02 解決）：**

- HTML comment 形式避免被誤讀為對白本文 — markdown 渲染時不顯示，但 parser 易解析
- **句級 A-\* 引用權威來源 = frontmatter `dialogue_keys[<KEY>].portrait/bgm/sfx`**（v0.2 新增）
- **內文 `<!-- 立繪：A-... -->` / `<!-- BGM：A-... -->` / `<!-- SFX：A-... -->` 是 view-layer 提示**，僅供讀者編輯時參考；不是 parser 解析 / export 的權威來源
- KEY comment（`<!-- KEY: ... -->`）仍是必填且權威 — 它對應 frontmatter map key
- parser 對「內文 art comment vs frontmatter dialogue_keys 不一致」→ WARN「內文提示與 frontmatter 權威來源不符，建議同步」（非 ERROR — 允許編輯期間暫時不同步）
- 一行 KEY comment 對應「下一段非 comment 行」是該 KEY 對應的台詞 / 動作描述
- 動作描述（如「（主角A 低頭...）」）也需 KEY — 對應 frontmatter `speaker: null`
- KEY comment 必須緊鄰其對應內容（中間不可有其他非空 / 非 comment 行 / 非 art comment 行）
- 順序必須跟 `dialogue_keys` map 內 `line_index` 順序一致

**為何 HTML comment 形式（保留 v0.1 設計理由）：**

| 候選 | 結論 | 理由 |
|---|---|---|
| ✓ **HTML comment**（採用） | 採用 | markdown 渲染不顯示；KEY 對讀者透明；parser 易解析 |
| ✗ 行尾 inline metadata `{key: ...}` | 拒 | 影響閱讀體驗；不同 renderer 行為不一致 |
| ✗ 純 frontmatter（不放內文） | 拒 | `line_index` 跟內文容易脫鉤；改寫台詞時 KEY 容易錯位 |
| ✗ 額外 `.keys.yaml` 同位檔 | 拒 | 破壞單檔自含性；user 編輯時要兩檔同步 |

**雙軌設計（v0.2 細化）：**
- frontmatter `dialogue_keys` Map：**權威來源 + 機器讀**（KEY 集合 / metadata 查詢 / portrait/bgm/sfx 句級資料）
- 內文 HTML comment：**人讀提示**（編輯時看得到 KEY + 美術 hint 不會誤刪）
- line_index 雙向驗證：frontmatter map `line_index` ↔ 內文 KEY comment 出現順序

## 4.4 KEY alias mapping 機制（v0.2 — 對齊 Map shape）

**用途：** user 改名後仍能追溯預設名 / 歷史 KEY。

**儲存位置：** 在 `dialogue_keys` map value 的 `aliases` list 內（§4.2）。

**改名流程（屬上下游 UD-5 範圍，本節只承諾 schema 容納；v0.2 對齊 Map shape）：**

1. user 在前端 F7 編輯界面把 KEY `dlg.ch01.s03.l002` 改為 `boss_intro_line_2`
2. 工具寫回 .md 時：
   - **將 map key 從 `dlg.ch01.s03.l002` 改為 `boss_intro_line_2`**（map 內 entry 整體 rekey）
   - `aliases` 維持原樣（首位仍是預設名 `dlg.ch01.s03.l002`）— 此時 aliases 跟原 map key 一致
   - 設定 `renamed_at: <today>`
   - 內文 HTML comment 同步改為 `<!-- KEY: boss_intro_line_2 -->`
3. 若 user 再改一次 KEY（如改為 `villain_first_line`）：
   - map key 改為 `villain_first_line`
   - `aliases` **append** 中間值：`[dlg.ch01.s03.l002, boss_intro_line_2]`（保留所有歷史；首位仍是預設名）
   - 更新 `renamed_at`

**改名行為示意：**

```yaml
# 改名前
dialogue_keys:
  dlg.ch01.s03.l002:           # ← 原預設名作為 map key
    aliases: [dlg.ch01.s03.l002]
    ...

# 第一次改名後
dialogue_keys:
  boss_intro_line_2:           # ← 新 KEY 取代 map key
    aliases: [dlg.ch01.s03.l002]   # 預設名移到 aliases
    renamed_at: 2026-05-23
    ...

# 第二次改名後
dialogue_keys:
  villain_first_line:          # ← 再改新 KEY
    aliases:
      - dlg.ch01.s03.l002      # 首位永遠是預設名
      - boss_intro_line_2      # 中間歷史 append
    renamed_at: 2026-05-24
    ...
```

**重複偵測：**

- 改為「另一段台詞當前的 KEY」（即現有 map key）→ parser ERROR（違反 §4.6 全 repo unique）
- 改為「另一段台詞的歷史 alias」→ parser WARN（建議改其他名，但不強制）

**反向查詢：** A.0 parser 建立全 repo `alias → 當前 KEY + 所在檔案路徑` 反向索引（§4.8）。

## 4.5 KEY 生命週期（v0.2 — status metadata 取代 `[DELETED]` prefix）

**v0.2 主要變更（per D-037 + C-10 解決）：**
- 廢棄 v0.1 設計的「KEY 前綴加 `[DELETED]`」
- 改用 `status: active | deprecated | deleted` metadata 表達生命週期
- `key` 本身（即 map key）永遠 immutable（除非 user 改名走 §4.4 流程）

**生命週期表：**

| 階段 | KEY 行為（v0.2） |
|---|---|
| `/dialogue-write` 生成台詞 | 工具自動產預設名（`dlg.ch<NN>.s<NN>.l<NNN>`）寫入 `dialogue_keys` map + 內文 HTML comment；`status: active` |
| user 改名 | map key 更新；舊名 append 到 `aliases`；`renamed_at` 更新；內文 HTML comment 同步；`status` 不變 |
| 場景重編號（如 CH-01 → CH-02 重組） | KEY **不變** — 即使檔案改名，原 map key 維持（KEY 與編號解耦） |
| 台詞改寫 | KEY **不變** — 即使內文完全重寫（KEY 與內容解耦） |
| **棄用台詞** | `status: deprecated`；必填 `deprecated_reason`；內文行**保留**（讓 reader 看得到棄用提示）；內文 HTML comment 加 `<!-- DEPRECATED: <reason> -->`（上下游 UD-5 細化） |
| **刪除台詞** | `status: deleted`；必填 `deleted_at`；map entry **保留**（給 alias lookup 用）；**內文行整段移除** |
| 整檔降 DEPRECATED | KEY 不主動改 status；frontmatter `狀態: DEPRECATED` 即可 |

**lifecycle status 矩陣：**

| `status` | `deleted_at` | `deprecated_reason` | 內文行 | 出現在 export | 出現在 cross-scene QA |
|---|---|---|---|---|---|
| `active` | null | null | 在 | 是 | 是 |
| `deprecated` | null | 必填 | 在（加 `<!-- DEPRECATED: ... -->` 提示） | 是（含 status flag） | **否**（跨場 QA 排除棄用句） |
| `deleted` | 必填 | null | **移除** | 否 | 否 |

**規則：**

- 「KEY 永遠不重用」 — 一旦某 KEY（或 alias）在 repo 內出現過，新台詞絕不可用同名 KEY；parser 在 KEY 生成時要查歷史 `aliases` 防衝突
- `status: deleted` entry 不刪除 — 保留供 alias lookup 與 export 歷史追溯；`status` 是「軟刪除」標記
- 內文 HTML comment 跟 frontmatter status 同步由上下游 UD-5 細化（屬寫入 algorithm 範圍）
- 從 v0.1 既有資料遷移：所有 v0.1 dialogue_keys list entry → v0.2 map entry；v0.1 `[DELETED]` prefix → v0.2 `status: deleted` + `deleted_at`（屬 master 第四輪整合期間 / CODEX tier 2 遷移範圍，本檔只規範新 schema）

## 4.6 全 repo unique guarantee（v0.2 — 對齊 Map shape）

**保證範圍：** 整個 Instance repo（不只單檔）。

**機制：**

- A.0 parser 啟動時掃描所有 `08_dialogue_outputs/**/*.md` 的 `dialogue_keys` map，建全 repo KEY 集合
- 全 repo 集合 = `⋃ (map key) ∪ ⋃ (entry.aliases[*])` for all dialogue files
- 任何新 KEY 生成 / 改名前先查集合
- KEY 衝突一律 ERROR，禁止寫入
- `status: deleted` entry 的 map key 與 aliases **仍計入** unique 集合（KEY 不重用原則）

**alias 也納入 unique：** 不只 map key unique；`aliases` 中每個歷史名也納入 unique 集合，防止「user 把 KEY 改成歷史 alias」造成追溯混亂。

**parser 啟動時的全集合建構（v0.2 — Map shape）：**

```
全 repo KEY 集合 = ⋃ (對每份 08_dialogue_outputs/**/*.md：
                        對每個 dialogue_keys 的 (map_key, entry)：
                          {map_key} ∪ entry.aliases[*])
```

## 4.7 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 上游 5 協議檔（00_e ~ 00_h / 00_l） | 無 | 不動 |
| 下游 00_a / 00_b / 00_c / 00_d / 00_k | 無 | 不動 |
| **08_b 台詞輸出模板** | **有** | 加 `dialogue_keys` **Map** 範例 + 內文 KEY 註解範例（屬上下游 UD-5 範圍；v0.2 對齊 Map shape） |
| 09_a ~ 09_f QA 模板 | 無 | QA 報告不含 KEY，引用台詞時用 `<key>` 即可 |
| 既有 03_characters / 04_relationships / 05_plot 等上游靜態檔 | 無 | 不含台詞，無 KEY 需求 |

（§10 統籌總表）

## 4.8 對 A.0 parser 影響（本節版 — v0.2）

- parser 多解析 frontmatter `dialogue_keys` **Map** + 內文 HTML comment `<!-- KEY: ... -->`
- 啟動時建全 repo KEY + alias 集合（§4.6）
- 驗證：
  - 一檔內 map key unique（YAML 本身保證；違反 = YAML parse error）
  - 全 repo (map key) ∪ aliases unique
  - frontmatter map `line_index` 順序 = 內文 KEY comment 順序
  - KEY 語法符合 §4.1
  - `aliases[0]` = 預設名格式（§4.1 預設語法）
  - `status` 值在 enum `active / deprecated / deleted` 內
  - `status: deleted` 必有 `deleted_at`；`status: deprecated` 必有 `deprecated_reason`
  - `portrait` / `bgm` 值（若非 null）必須對應到 valid A-\* asset_id（cross-check `art_metadata`）
  - `sfx` list 各元素（若非空）必須對應到 valid A-sfx-\* asset_id
- 建反向查詢：`alias → 當前 KEY + 檔案路徑`
- **內文 HTML comment 不一致警告**：parser 對「內文 `<!-- 立繪：A-... -->` vs frontmatter `portrait` 不符」→ WARN（非 ERROR；§4.3 規則）

（§11 統籌總表）

## 4.9 Cross-ref

- D-022 / REQUIREMENTS_LOCK §3.2 / 本檔 §2.2
- **D-037 / CODEX C-01 + C-02 + C-10**（v0.2 patch — list→Map / 句級 A-\* 權威來源 / lifecycle metadata）
- P-022 — RESOLVED via 本節 + D-037
- 上下游 UD-5（08_b 模板 + `/dialogue-write` 加 KEY 生成步驟）
- UX UX-12（前端 F7 編輯 + LOCKED 守門 — KEY 改名 UI）
- DF-7（JSON 中介格式）/ 本檔 §9 — JSON 輸出含 KEY 對應規則（v0.2 dialogue_line record 對齊 Map shape）

---

# 5. A-\* 美術資產 entity 規格（DF-4）

## 5.0 本節性質

實作 D-023「A-\* 美術資產 entity 只存 KEY」最終裁決的 schema 層細節。本節決定：

- A-\* entity ID 命名規則（§5.1）
- 目錄結構 `10_art_assets/`（§5.2）— master 確認對齊 01-09 整數編號延續
- A-\* metadata frontmatter schema（§5.3）
- 在台詞檔 / 場景任務包內引用 A-\* 的 cross-reference 語法（§5.4）
- KEY alias mapping 同 i18n（§5.5）
- 不存實檔 / 路徑 / URL 的強制規則（§5.7）

**設計原則（依 D-023 / Bucket #1 拍板）：**

- 新增 A-\<asset_id\> entity 類型（partial supersede SPEC §5.1 LOCKED — 是「7+1」而非「重寫 7」）
- 只存 KEY + metadata（名稱、所屬角色、表情/狀態標籤）
- 不存實檔、不存路徑、不存 URL — 實檔對應由外部系統處理
- KEY 機制同 i18n（自動產 + 可改名 + alias）
- source frontmatter / 內文用 KEY 引用

## 5.1 A-\* entity ID 命名規則（v0.2 — 7 種 subtype per D-044）

**預設語法：**

```
A-<subtype>-<owner>-<state>
```

例：`A-portrait-主角A-default`、`A-portrait-主角A-anger`、`A-bg-cafe-day`、`A-bgm-tension-01`、`A-sfx-glass-break`、`A-voice-主角A-line001`、`A-ui-button-confirm`

**v0.2 變更（per D-044 + CODEX C-13 解決）：**
- v0.1 subtype 範圍：`portrait / bg / cg / icon / effect`（5 種）
- v0.2 subtype 範圍：**`portrait / bg / cg / sfx / bgm / voice / ui`**（7 種）
- `icon` / `effect` 不採（合併進 `ui` / `cg`）
- v0.1 欄位 `<character>` 改名為 v0.2 `<owner>`（語意更廣 — 可對應 C-\* / S-\* / CH-\* / global）

**欄位定義（v0.2）：**

| 欄位 | 格式 | 說明 |
|---|---|---|
| 前綴 | `A-` 固定 | 識別為美術資產 entity |
| `<subtype>` | 7 種 enum：`portrait / bg / cg / sfx / bgm / voice / ui`（§5.1a subtype registry） | 資產類型；不再用 `<type>` 命名 |
| `<owner>` | 中文角色名 OR ASCII 識別字 | 該 asset 的「所屬實體」 — 可對應 C-\* / S-\* / CH-\* / global；不同 subtype 對應規則不同（§5.1b） |
| `<state>` | ASCII 小寫詞 | 狀態 / 變體標籤；如 `default` / `anger` / `day` / `01` / `line001` 等 |

## 5.1a A-\* subtype registry（v0.2 新增 per D-044）

**性質：** A-\* 的 subtype 是「受控的可擴充 list」 — core 7 種本輪 lock；未來新加經 master 裁決（屬 entity_type_registry §7 機制延伸）。

**Schema（在 §7.2 entity_type_registry.template.yaml 內 A entry 的 `subtype:` 子節）：**

```yaml
# 對應 §7.2 Template 中 A entry 的細節
- type: A
  description: 美術資產
  id_pattern: ^A-(portrait|bg|cg|sfx|bgm|voice|ui)-.+-.+$    # v0.2 — 7 種
  target_dir: 10_art_assets/
  cross_ref_allowed: true
  locked: true
  subtype:
    allowed_values:                          # v0.2 — 正式列為 allowed list
      - portrait
      - bg
      - cg
      - sfx        # v0.2 新（音效）
      - bgm        # v0.2 新（背景音樂）
      - voice      # v0.2 新（配音）
      - ui         # v0.2 新（UI 圖素 — 取代 v0.1 icon）
  reserved_subtypes:                         # v0.2 新 — 預留給未來新加 subtype，本輪不採
    - icon         # 合併進 ui（不獨立採）
    - effect       # 合併進 cg（不獨立採）
    - video        # 未來考慮（reserved）
    - shader       # 未來考慮（reserved）
```

**Subtype 加入流程（未來擴充）：**

- 從 `reserved_subtypes` 移除該值 + 加到 `allowed_values` + Bump entity_type_registry `version`
- 須走 master 裁決（D-NNN 紀錄）
- 屬「動 LOCKED core」操作；user 不可自行在 Instance 端 user_extensions 改 A subtype（A 是 core: true + locked: true）

**parser 行為（v0.2）：**

- A-\* ID 的 subtype 必須在 `allowed_values` 內 → 不在 → ERROR「未知 A-\* subtype」
- 在 `reserved_subtypes` 但不在 `allowed_values` 內 → ERROR + 提示「該 subtype 已預留但本輪不採」

## 5.1b A-\* `<owner>` 與其他 entity 的對應關係（v0.2 細化）

不同 subtype 的 `<owner>` 對應規則不同：

| subtype | `<owner>` 對應 | 範例 | parser 驗證 |
|---|---|---|---|
| `portrait` | **必對應 C-\* entity** | `A-portrait-主角A-anger` ↔ `C-主角A` | 不對應 → WARN「孤立立繪」 |
| `bg` | **必對應 S-\* / CH-\* / global** | `A-bg-cafe-day`（場景識別字）/ `A-bg-global-rain`（通用） | 不對應 → WARN |
| `cg` | 對應 S-\* / CH-\* / global | `A-cg-finale01-default` / `A-cg-global-victory` | 不對應 → WARN |
| `sfx` | 通常 global，可選對應 S-\* | `A-sfx-glass-break` / `A-sfx-cafe-bell` | 無強制對應 |
| `bgm` | 通常 global / CH-\* | `A-bgm-tension-01` / `A-bgm-ch01-main` | 無強制對應 |
| `voice` | **必對應 C-\* + dialogue KEY**（句級 voice line） | `A-voice-主角A-line001`（line001 對應該角色第 1 句 dialogue KEY） | 不對應 C-\* → WARN；對應的 dialogue KEY 不存在 → WARN |
| `ui` | 通常 global | `A-ui-button-confirm` / `A-ui-icon-warning` | 無強制對應 |

**保留字符規則：** 同 §4.1 — ASCII 小寫 + 數字 + `-`；user-defined 改名加 `_`。`<owner>` 欄位允許中文（給 C-\<中文角色名\> 用）。

**user 改名：** 同 i18n KEY — 工具自動產預設名 + user 改名後預設名記為 alias（§5.5）。

## 5.2 目錄結構 `10_art_assets/`（v0.2 — 7 種 subtype）

**位置：** Instance root 下，與既有 `01_*` ~ `09_*` 平行。Master 確認採整數編號延續（不是 hex `0A_*`），未來擴充：

```
Instance/
├── 01_world/
├── 02_vocabulary/
├── 03_characters/
├── 04_relationships/
├── 05_plot/
├── 06_scene_index/
├── 07_scene_tasks/
├── 08_dialogue_outputs/
├── 09_quality_assurance/
├── 10_art_assets/                  ← 本輪新增（DF-4）；v0.2 — 7 種 subtype
│   ├── 10_a_portrait_index.md          # A-portrait-* 索引
│   ├── 10_b_background_index.md        # A-bg-* 索引
│   ├── 10_c_cg_index.md                # A-cg-* 索引
│   ├── 10_d_sfx_index.md               # A-sfx-* 索引（v0.2 新）
│   ├── 10_e_bgm_index.md               # A-bgm-* 索引（v0.2 新）
│   ├── 10_f_voice_index.md             # A-voice-* 索引（v0.2 新）
│   ├── 10_g_ui_index.md                # A-ui-* 索引（v0.2 新 — 取代 v0.1 icon）
│   ├── portraits/                      # A-portrait-* 個別 metadata 檔（per character）
│   │   ├── 主角A.md
│   │   └── 反派B.md
│   ├── backgrounds/                    # A-bg-* 個別 metadata 檔（per scene / global）
│   │   ├── cafe.md
│   │   └── global.md
│   ├── cg/                             # A-cg-* 個別 metadata 檔
│   │   └── finale01.md
│   ├── sfx/                            # A-sfx-* 個別 metadata 檔（v0.2 新；通常 global，按主題分組）
│   │   ├── ambient.md                  # 環境音 group
│   │   └── action.md                   # 動作音 group
│   ├── bgm/                            # A-bgm-* 個別 metadata 檔（v0.2 新；按 mood / chapter 分組）
│   │   ├── tension.md
│   │   └── peaceful.md
│   ├── voice/                          # A-voice-* 個別 metadata 檔（v0.2 新；per character）
│   │   ├── 主角A.md                     # 含該角色所有 voice line（A-voice-主角A-line001, line002...）
│   │   └── 反派B.md
│   └── ui/                             # A-ui-* 個別 metadata 檔（v0.2 新；按 UI 區塊分組）
│       ├── buttons.md
│       └── icons.md
├── 11_items/                  ← 預留接口（本輪不實作；DF-5 registry 對應）
├── 12_ui_text/                ← 預留接口（注意：12_ui_text 是「UI 文字」未來 entity 類型；跟 10_art_assets/ui/ 的 A-ui-* 圖素 metadata 不衝突）
├── 13_skills/                 ← 預留接口
└── .protocol_version
```

**v0.2 索引檔變更：**
- v0.1 `10_d_icon_index.md` / `10_e_effect_index.md` → **廢棄**（icon/effect 不採）
- 新增 `10_d_sfx_index.md` / `10_e_bgm_index.md` / `10_f_voice_index.md` / `10_g_ui_index.md`

**為何「索引檔 + 個別 metadata 檔」雙層：**

- 索引檔（`10_a_portrait_index.md` 等）：全表式列出該 subtype 所有 A-\* entity ID + 一行 metadata 摘要；供 `/status` 與 前端 asset panel 快速 list
- 個別 metadata 檔（`portraits/<character>.md` / `voice/<character>.md` / `sfx/<group>.md` 等）：一份檔含同 owner / group 的所有 state；frontmatter `entities` 列所有對應 A-\* 集合

**v0.2 個別 metadata 檔組織原則：**

| subtype | 個別檔組織 | 範例檔名 |
|---|---|---|
| `portrait` | per character | `portraits/主角A.md` |
| `bg` | per scene / global | `backgrounds/cafe.md` / `backgrounds/global.md` |
| `cg` | per scene / global | `cg/finale01.md` / `cg/global.md` |
| `sfx` | per group（環境音 / 動作音 / UI 音 等） | `sfx/ambient.md` |
| `bgm` | per mood / chapter | `bgm/tension.md` |
| `voice` | per character（含該角色所有 voice line） | `voice/主角A.md` |
| `ui` | per UI 區塊 | `ui/buttons.md` |

**規則：** A-\* 必定有 metadata 檔；只在索引檔出現但無個別 metadata 檔 → parser ERROR。

## 5.3 A-\* metadata frontmatter schema

**範例：`10_art_assets/portraits/主角A.md`**

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：主角A 立繪資產 metadata
優先級：中

---
entities:
  - A-portrait-主角A-default
  - A-portrait-主角A-anger
  - A-portrait-主角A-smile
  - A-portrait-主角A-crying
depends_on:
  - C-主角A
weight:
  A-portrait-主角A-default: 1.0
  A-portrait-主角A-anger: 0.5
  A-portrait-主角A-smile: 0.5
  A-portrait-主角A-crying: 0.5
art_metadata:
  - asset_id: A-portrait-主角A-default
    display_name: 主角A 預設立繪
    subtype: portrait                 # v0.2 新欄位（per §5.1a 7 subtype enum）
    owner: C-主角A                    # v0.2 改名自 v0.1 `character`（per §5.1b owner 對應規則）
    state_tags: [default, neutral]
    aliases: [A-portrait-主角A-default]
    status: active                    # 對齊 D-037 status enum：active|deprecated|deleted
    deprecated_reason: null
    deleted_at: null
    created_at: 2026-05-22
  - asset_id: A-portrait-主角A-anger
    display_name: 主角A 憤怒立繪
    subtype: portrait
    owner: C-主角A
    state_tags: [anger, hostile, combat]
    aliases: [A-portrait-主角A-anger]
    status: active
    deprecated_reason: null
    deleted_at: null
    created_at: 2026-05-22
  ...
---

# 主角A 立繪資產 metadata

（自由文字區 — 描述該角色立繪設計理念 / 顏色 palette 約束 / 風格指引等）

## 表情狀態列表

| asset_id | 顯示名 | 標籤 |
|---|---|---|
| A-portrait-主角A-default | 主角A 預設立繪 | default / neutral |
| A-portrait-主角A-anger | 主角A 憤怒立繪 | anger / hostile / combat |
| ...
```

**`art_metadata` block 欄位定義：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `asset_id` | 是 | A-\* entity ID |
| `display_name` | 是 | 給 user 看的可讀名稱 |
| `subtype` | **是（v0.2 新）** | 該 asset 的 subtype：`portrait / bg / cg / sfx / bgm / voice / ui`（7 種 enum，per §5.1a） |
| `owner` | **視 subtype（v0.2 改名自 v0.1 `character`）** | A 該 asset 對應的「所屬 entity」 — 對應 C-\* / S-\* / CH-\* / global；對應規則見 §5.1b |
| `state_tags` | 是（可為空 list） | 表情 / 狀態 / 場景時段標籤 list |
| `aliases` | 是（至少 1 個） | 改名歷史，首位是預設名 |
| `created_at` | 是 | 該 asset_id 首次寫入日期 |
| `renamed_at` | 否 | 最近一次改名日期 |
| `deleted_at` | 否 | 標記刪除日期 |
| `dialogue_keys_ref` | **否（僅 `subtype: voice` 有意義）** | 該 voice line 對應的 dialogue KEY（如 `dlg.ch01.s03.l001`）；voice subtype 必填，其他 subtype 省略 |

**v0.2 欄位變動摘要：**
- v0.1 `character` → v0.2 `owner`（語意擴大）
- 新增 `subtype` 欄位（v0.2）
- 新增 `dialogue_keys_ref` 欄位（v0.2 — 給 A-voice-\* 用，連結到 §4.2 dialogue_keys map key）

**強制禁止欄位（§5.7）：** 不允許 `file_path` / `url` / `source_image` 等指向實檔的欄位 — parser ERROR。

## 5.4 在台詞檔 / 場景任務包內引用 A-\* 的 cross-reference 語法

**Frontmatter cross-reference（與既有 entity 並列）：**

下游台詞檔 / 場景任務包的 frontmatter 既有 `depends_on` 可含 A-\*：

```yaml
entities:
  - S-01-03
depends_on:
  - C-主角A
  - C-反派B
  - A-portrait-主角A-default       # ← 新增：依賴美術資產
  - A-portrait-主角A-anger
  - A-portrait-反派B-default
  - A-bg-cafe-day
```

**內文 cross-reference：** 在台詞檔內文 / 任務包內文用「`立繪：` / `背景：` 中文 prefix + A-\* KEY」標註，建議寫在每段台詞前（HTML comment 或一般行皆可）：

```markdown
<!-- KEY: dlg.ch01.s03.l001 -->
<!-- 立繪：A-portrait-主角A-anger -->
<!-- 背景：A-bg-cafe-day -->
**主角A：** 你以為我會就這樣放棄？

<!-- KEY: dlg.ch01.s03.l002 -->
<!-- 立繪：A-portrait-反派B-default -->
**反派B：** 那就讓我看看你還能撐多久。
```

**規則：**

- A-\* cross-reference 可任選 frontmatter（依賴宣告層）/ 內文 HTML comment（逐句呈現層）/ 兩者並用
- 內文標註不強制；若不標註則 parser 從 frontmatter `depends_on` 推斷
- A-\* KEY 出現在內文時必須是當前 `asset_id`（不是歷史 alias）
- 引用 alias 時 parser WARN（建議改用當前 ID）

## 5.5 A-\* KEY alias mapping

機制完全同 §4.4 i18n KEY alias mapping：

- 改名時 `asset_id` 更新；舊名 append 到 `aliases`
- 全 repo unique 範圍含 `aliases`
- parser 建反向索引 `alias → 當前 asset_id + metadata 檔路徑`

唯一差異：A-\* alias 在 `art_metadata[*].aliases` 內；i18n KEY alias 在 `dialogue_keys[*].aliases` 內。語義對等。

## 5.6 A-\* 完成度計算（v0.2 — 獨立 asset panel，不入 narrative `/status` per D-045）

**v0.2 變更（per D-045 + CODEX C-14 解決）：**
- v0.1：A-\* 完成度進 `/status` expected entity manifest 比對（與其他 entity 並列）
- **v0.2：A-\* 完成度不納入** narrative `/status`；改在前端 asset panel 獨立顯示

**裁決理由（per D-045）：** 大綱寫到一半時繪師才開工很正常，不該卡台詞 FINAL。把美術進度跟敘事進度切開呈現，避免「美術沒開工 → narrative completeness 卡 0%」的誤判。

**v0.2 公式（獨立計算）：**

- A-\* 出現在 metadata 檔的 `entities` list
- 該 metadata 檔的 `狀態`（DRAFT / REVIEW / FINAL / LOCKED）依 §5.3 映射為 0/25/75/100
- `weight` 提供 A-\*-by-A-\* 權重（如預設立繪 weight 1.0 / 變體 0.5）
- A-\* asset completeness = Σ(metadata 檔狀態 × weight) / Σ(weight)
- **不納入** SPEC §5.3 narrative entity 完成度公式的加總

**Narrative `/status` 與 Asset panel 對應：**

| 顯示位置 | 內容 |
|---|---|
| **Narrative `/status`** | 既有 7 種 entity（W-rules / W-language / V / C-\* / R-\*-\* / P / CH-\* / S-\*）完成度；**不含 A-\*** |
| **前端 asset panel（獨立）** | A-\* 完成度按 subtype 分組顯示（7 種 subtype 各自一段）；不影響 narrative readiness |

**A-\* 完成度只依 metadata 檔狀態，跟外部實檔是否存在 / 完成完全無關**（這個工具看不到實檔）。

**FINAL gate 行為（屬下游 UD 範圍，本檔只承諾 schema 容納）：**
- 台詞 FINAL gate 檢查 `narrative entity 完成度` + `9 種 QA status 齊全`（D-043）
- 台詞 FINAL gate **不檢查 A-\* asset completeness**（per D-045）
- A-\* asset 跟台詞解耦：可以「台詞 FINAL + 美術 DRAFT」並存，由前端 asset panel 提示 user 哪些美術還沒齊全

## 5.7 不存實檔 / 路徑 / URL 的強制規則

**Schema 級禁止欄位（parser ERROR 偵測）：**

| 禁止欄位 | 理由 |
|---|---|
| `file_path` | 工具看不到實檔；防止 user 誤以為工具會跟蹤實檔變動 |
| `url` | 同上；避免外部 URL rot 影響 schema |
| `source_image` | 同上 |
| `binary_data` / `base64_*` | 工具是「文字資料庫」，不存 binary |

**仍允許的「指引性文字」：** `display_name` / 自由文字區 / `state_tags` 等用於描述「這份立繪 metadata 對應外部哪份檔案」是 OK 的，但只能是 **descriptive prose**，不能是 **resolvable path**。

**外部系統責任邊界：** Unity / 引擎 / 美術 pipeline 自己拿 A-\* asset_id 去對應實檔（如查 Unity Addressables 表 / 自訂查表）— 不是本工具的事。

## 5.8 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 既有 7 entity 類型相關模板（03_characters / 04_relationships / 05_plot 等） | 無 | 不動 |
| 09_a ~ 09_f QA 模板 | 無 | A-\* 不在 QA 範圍 |
| **08_b 台詞輸出模板** | **有** | 加 A-\* cross-reference 範例（frontmatter + 內文 HTML comment）— 屬上下游 UD-5 範圍 |
| **07 任務包模板** | **有** | 加 A-\* 在 `depends_on` 列出範例 — 屬上下游 UD-2 / UD-5 範圍 |
| 新增模板 | **新增** | `10_a_portrait_index.md` / `10_b_background_index.md` / `10_c_cg_index.md` / `10_d_icon_index.md` / `10_e_effect_index.md` / `portraits/<character>.md` 範本（屬上下游 UD-4 設計範圍 — 對應協議候選編號 00_q） |

（§10 統籌總表）

## 5.9 對 A.0 parser 影響（本節版）

- parser 多解析 `art_metadata` frontmatter block
- 多識別 entity 類型前綴 `A-*`
- 多掃描 `10_art_assets/**/*.md`
- 驗證：
  - A-portrait-\* / A-cg-\* 的 `character` 必須對應既有 C-\* entity（否則 WARN）
  - 禁止欄位偵測（§5.7）
  - asset_id 全 repo unique（含 alias）
  - A-\* 完成度計算（§5.6 — v0.2 獨立計算，不入 narrative `/status`）
  - subtype 在 §5.1a allowed_values 內（v0.2）
  - subtype = voice 時必填 `dialogue_keys_ref`（v0.2）
- **v0.2：A-\* 不加入 narrative `/status` expected entity manifest 比對**（per D-045）；改在前端 asset panel 獨立顯示
- A-\* 完成度資料仍由 parser 提供（給 asset panel 用），但不參與 narrative readiness 計算

（§11 統籌總表）

## 5.10 Cross-ref

- D-023（A-\* 美術資產 entity 只存 KEY）/ REQUIREMENTS_LOCK §3.3
- **D-044（A-\* subtype 7 種正式擴）/ CODEX C-13**（v0.2 patch）
- **D-045（A-\* 不納入 narrative `/status` 完成度）/ CODEX C-14**（v0.2 patch）
- P-021 — RESOLVED via 本節 + D-041 + D-044
- D-025（資料類別範圍鎖定 + 留接口）/ 本檔 §7
- 上下游 UD-4（A-\* 美術資產對應協議 — 候選 00_q）
- 上下游 UD-12（跨 entity 類型的 cross-reference 規則）
- DF-7（JSON 中介格式）/ 本檔 §9 — JSON 輸出含 A-\* records
- UX 前端 asset panel（v0.2 — D-045 對應 UX 設計範圍）

---

# 6. mode_tag / qa_type 新增 enum 值（DF-8）

## 6.0 本節性質

實作 D-026 + D-028 對 SPEC §5.2.4 三維度狀態 enum 的擴充：

- **mode_tag enum 加 1 值**：`SINGLE_ITER`（對應 D-028 `/dialogue-write --single-iter` 模式）
- **qa_type enum 加 3 值**：`RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY`（對應 D-026 09_g/h/i 三份 QA 模板）

本節只做「enum 值加入 + schema 級紀錄」。qa_type 變「可擴充 list」機制屬 DF-6（本檔 §8）；具體 09_g/h/i algorithm 屬上下游 UD-6；具體 SINGLE_ITER algorithm 屬上下游 UD-7。

## 6.1 mode_tag enum 擴充：`SINGLE_ITER`

**SPEC §5.2.4 既有 5 種（LOCKED）：**

| 值 | 用途 |
|---|---|
| `ORGANIZED` | 整理過的台詞（既有） |
| `DRAFT_TRIAL` | 試寫 v01A/B/C（既有） |
| `EXPERIMENTAL` | 破格 v01D（既有） |
| `CONVERGENCE` | 收斂 v02（既有） |
| `FINAL_CANDIDATE` | final 候選（既有） |

**本輪新增（DF-8）：**

| 值 | 用途 | 對應 |
|---|---|---|
| `SINGLE_ITER` | 單版本迭代 — agent 寫一版 → user 跟 agent 迴圈改 → OK | D-028 `/dialogue-write --single-iter` |

**partial supersede SPEC §5.2.4 mode_tag LOCKED：** mode_tag 從 5 種擴為 6 種；其他 5 種完全不動。

**SINGLE_ITER 與既有 5 種的對應行為（屬上下游 UD-7 細化，本節只承諾 schema 容納）：**

- 產出形式：每次迭代寫一份檔（如 `CH01_S03_xxx_dialogue_v01_iter1.md` / `v01_iter2.md` ...）
- pipeline_state：對應 `DIALOGUE_TRIAL` 或 `DIALOGUE_CONVERGED`（屬上下游決定）
- mode_tag 在 `phase_log` 內紀錄（§3.4 範例既有）

## 6.2 qa_type enum 擴充：`RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY`

**SPEC §5.2.4 既有 5 種（LOCKED）：**

| 值 | 對應模板 |
|---|---|
| `AI_FLAVOR` | 09_a AI 味檢查（既有） |
| `VOICE_CONSISTENCY` | 09_b 角色聲線一致性（既有） |
| `FORBIDDEN_WORD` | 09_c 禁用詞（既有） |
| `INFO_CONTROL` | 09_d 資訊控制（既有） |
| `GENRE_DRIFT` | 09_f 類型偏移（既有；09_e 是 final-gating 紀錄不在 QA pipeline） |

**本輪新增（DF-8）：**

| 值 | 對應模板 | 對應 D |
|---|---|---|
| `RHYTHM` | 09_g 節奏感（句長分布 / 變異度 / 長短交替 / 段落呼吸感） | D-026 |
| `DRAMATIC_TENSION` | 09_h 對話張力（推進 / 讓步 / 揭穿 / 反擊頻率 + 攻防力度量化） | D-026 |
| `CROSS_SCENE_CONTINUITY` | 09_i 跨場一致性（跨場聲線漂移 / 跨場資訊洩漏 / 跨場節奏 arc） | D-026 |

**partial supersede SPEC §5.2.4 qa_type LOCKED：** qa_type 從 5 種擴為 8 種；其他 5 種完全不動。**+ DF-6 變「可擴充 list」機制**（§8）— 未來再加新 09_x 不必動 SPEC §5.2.4。

**新總計 QA 模板（依 REQUIREMENTS_LOCK §4.1）：** 8 份 QA 模板（09_a/b/c/d/f/g/h/i）+ 1 份 final-gating（09_e）= 9 份。

## 6.3 對 SPEC §5.2.4 既有 enum 表的衝擊

**SPEC §5.2.4「三維度互不混用」段：**

- A. `狀態` 7 種 — **不動**
- B. `pipeline_state` 9 種 — **不動**
- C. `mode_tag` — **partial supersede**：5 種 → 6 種（加 SINGLE_ITER）
- 加 `qa_type` enum 行 — **partial supersede**：5 種 → 8 種（加 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY）+ DF-6 變可擴充

**SPEC §5.2.4「對應關係」5 個範例：** 既有 5 個範例不動；本檔不新增 SINGLE_ITER 範例（屬上下游 UD-7 細化）。

**SPEC §5.2.3「欄位定義」`qa_type` 欄位描述：** 從「AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT」更新為「`AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT / RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY`（基線 8 種 + DF-6 可擴充）」— 由 master 第四輪整合落地。

## 6.4 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 既有 09_a / 09_b / 09_c / 09_d / 09_e / 09_f 模板 | 無 | 不動 |
| 既有 08_b 台詞輸出模板（mode_tag 範例） | 微 | SPEC §5.2.4 範例段更新即可，模板本身的 frontmatter 範例若有 mode_tag 也保留既有值；SINGLE_ITER 範例 / 09_g/h/i 範例由上下游 UD-6/7 處理 |
| **新增 09_g 節奏感 模板** | **新增** | 內容屬上下游 UD-6 範圍 |
| **新增 09_h 對話張力 模板** | **新增** | 內容屬上下游 UD-6 範圍 |
| **新增 09_i 跨場一致性 模板** | **新增** | 內容屬上下游 UD-6 範圍 |

（§10 統籌總表）

## 6.5 對 A.0 parser 影響（本節版）

- parser 加 `mode_tag` 值 `SINGLE_ITER` 進 valid set
- parser 加 `qa_type` 值 `RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY` 進 valid set（這個 set 本身在 DF-6 變開放可擴充）
- 不擴 `pipeline_state` / `狀態` / `qa_decision` enum

（§11 統籌總表）

## 6.6 Cross-ref

- D-026（新增 09_g/h/i 模板 — partial supersede D-018 #3）/ REQUIREMENTS_LOCK §4.1
- D-027（qa_type 變可擴充）/ 本檔 §8（DF-6）
- D-028（/dialogue-write 加 SINGLE_ITER — partial supersede P-010）/ REQUIREMENTS_LOCK §4.3
- P-025 / P-027 — 屬上下游 UD-6 / UD-7 細化（本檔只保 schema 容納）
- SPEC §5.2.4 — partial supersede mode_tag / qa_type LOCKED 描述

# 7. 可擴充 entity 類型 registry（DF-5）

## 7.0 本節性質

實作 D-025「本輪資料類別範圍鎖定 — 角色台詞 + A-\* 立繪；其他類別留接口」的 schema 機制。本節決定：

- 「接口」具體形式 — 可擴充 entity 類型 registry（§7.1 ~ §7.4）
- 既有 7 + A-\* 在 registry 內的標記方式（§7.5 ~ §7.6）
- user 加新類型（如未來 I-\* / UI-\* / SKILL-\*）的流程（§7.7）
- 對 SPEC §5.1 LOCKED 的 partial supersede 細則（§7.8）

**設計原則（依 D-025 / Bucket #1 拍板 + Master 確認方向）：**

- Template / Instance 三層結構（對齊 SPEC §7 既有分層架構）
- 既有 LOCKED 類型列 `core: true` 不可刪；user-added 列 `core: false`
- A.0 parser 從 Instance root 讀（user 在 Instance 內 user-extend）
- 未來新增 entity 類型不必動 SPEC §5.1 核心

## 7.1 三層架構總覽

```
                  Template repo                 Instance（user 專案）
                  ──────────────                ──────────────
                  D:\劇本開發工具\               D:\<user-instance>\
                  _design/registries/           entity_type_registry.yaml
                  entity_type_registry          ↑（user 在這裡 user-extend）
                  .template.yaml
                                                ↑ Instance bootstrap 時 copy
                                                  Template → Instance root
                  
                  (供範本傳承)                    (供 A.0 parser 讀)
                                                    ↑
                                                    │
                                                A.0 parser 啟動時讀
                                                  Instance root
                                                  entity_type_registry.yaml
```

**三層職責：**

| 層 | 位置 | 內容 | Owner |
|---|---|---|---|
| Template | `_design/registries/entity_type_registry.template.yaml` | 既有 core 類型範本（現行：9 敘事既有 + A-\* 美術 + ORG 組織 = 11 個 core；權威以 entity_type_registry.template.yaml 為準） | master / 資料格式 specialist |
| Instance bootstrap | `<instance_root>/entity_type_registry.yaml`（複製自 Template） | 該 Instance 啟用的類型清單 | `/init-project` 階段自動複製 |
| Instance user-extend | 同上檔案 `user_extensions:` 段 | user 加新類型 | user（前端 F7 或直接編輯 .yaml） |

**對齊 SPEC §7 既有 Template/Instance 分層架構：** Template 是「通用骨架」、Instance 是「clone + 專案微調」。本 registry 機制完全遵循。

## 7.2 Template 層 schema

**檔案：** `_design/registries/entity_type_registry.template.yaml`

**[v0.4 partial supersede via NEW_REQ_4 — 對齊 entity_type_registry.template.yaml v0.3 權威]**  
本節 v0.1 原範例（`schema_version: v0.1` / A subtype 5 項 `(portrait|bg|cg|icon|effect)`）已過時 — A.0.7 實作的 `entity_type_registry.template.yaml` 採 D-044 7 subtype + 4 reserved_subtypes 結構（DF §5.1a v0.2 patch 主規格段已 LOCKED）。下方範例**直接以 v0.3 權威寫法呈現**（schema 內容對齊 `_design/registries/entity_type_registry.template.yaml` line 6-77）：

**[v0.5 partial supersede via NEW_REQ_48 / D-075（Batch 5 registry DRY）— 下方 inline YAML 補 W-style + ORG，對齊 11 種 core 權威]**  
下方 inline YAML 區塊是 `_design/registries/entity_type_registry.template.yaml` 的**非權威鏡像（NON-AUTHORITATIVE MIRROR）**，僅供本節可讀性參考。**唯一真實來源（single source of truth）為 `_design/registries/entity_type_registry.template.yaml`**（以 `load_entity_type_registry()` 載入）；本鏡像應由該權威檔再生（regenerate），不得手工維護出分歧。本輪 D-075 補入先前遺漏的 `W-style`（D-055；01_world/）與 `ORG`（D-071 / D-074；11_organizations/）兩個 core，使本 inline 鏡像對齊權威檔的 11 種 core（9 敘事 + A 美術 + ORG 組織）。鏡像與 registry 不一致時以 registry 為準；drift 由 `scripts/check_entity_type_consistency.py` lint 把關。本輪不刪除鏡像（spec-doc 可讀性）、不 bump `schema_version`（仍 data_format_spec_v0.3）。

```yaml
# Entity Type Registry — Template
# [NON-AUTHORITATIVE MIRROR of _design/registries/entity_type_registry.template.yaml]
# 本區塊僅為 SPEC 可讀性鏡像；權威 schema 見上述檔案，應由其再生，勿手工改出分歧。
# 本檔是 Template repo 內的範本；Instance bootstrap 時自動複製到 Instance root
# Instance 端 user 可在 user_extensions: 段擴充新類型；core 段不可動

version: 1
schema_version: data_format_spec_v0.3

core:
  # SPEC §5.1 既有敘事 core + D-055 W-style + D-071/D-074 ORG — 共 11 種，本輪不動其驗證行為
  - type: W-rules
    description: 世界規則
    id_pattern: ^W-rules$
    target_dir: 01_world/
    cross_ref_allowed: true
    locked: true
  - type: W-language
    description: 世界語言
    id_pattern: ^W-language$
    target_dir: 01_world/
    cross_ref_allowed: true
    locked: true
  - type: W-style
    description: 文風樣本與指紋
    id_pattern: ^W-style$
    target_dir: 01_world/
    cross_ref_allowed: true
    locked: true
  - type: V
    description: 詞彙系統
    id_pattern: ^V$
    target_dir: 02_vocabulary/
    cross_ref_allowed: true
    locked: true
  - type: C
    description: 角色
    id_pattern: ^C-.+$                     # C-<name>，name 允許中文
    target_dir: 03_characters/
    cross_ref_allowed: true
    locked: true
  - type: R
    description: 關係
    id_pattern: ^R-.+-.+$                  # R-<a>-<b>，字典序
    target_dir: 04_relationships/
    cross_ref_allowed: true
    locked: true
  - type: P
    description: 主線
    id_pattern: ^P$
    target_dir: 05_plot/
    cross_ref_allowed: true
    locked: true
  - type: CH
    description: 章節
    id_pattern: ^CH-\d{2}$                 # CH-NN
    target_dir: 05_plot/
    cross_ref_allowed: true
    locked: true
  - type: S
    description: 場景
    id_pattern: ^S-\d{2}-\d{2}(?:[a-z]+|sub)?$  # §5.2.6 分支後綴
    target_dir: 06_scene_index/, 07_scene_tasks/, 08_dialogue_outputs/
    cross_ref_allowed: true
    locked: true

  # A-\* 美術資產（DF-4 / D-023 / D-044 7 subtype patch）
  - type: A
    description: 美術資產
    id_pattern: ^A-(portrait|bg|cg|sfx|bgm|voice|ui)-.+-.+$
    target_dir: 10_art_assets/
    cross_ref_allowed: true
    locked: true
    subtype:
      allowed_values:
        - portrait
        - bg
        - cg
        - sfx
        - bgm
        - voice
        - ui
      reserved_subtypes:
        - icon
        - effect
        - video
        - shader

  # ORG 組織 / 非人格反派 / 組織型對抗源（D-071 / D-074）
  - type: ORG
    description: 組織 / 非人格反派 / 組織型對抗源（公司 / 制度 / 機構 / 體系 / 殘留或已解散組織；不會說話、無聲線卡、不進 /dialogue-write 為說話者；可被 P / S / R / C 以穩定 ID depends_on / cross-ref 的一級節點）
    id_pattern: ^ORG-.+$
    target_dir: 11_organizations/
    cross_ref_allowed: true
    locked: true

reserved_prefixes:
  # 預留給未來 user 加 entity 類型的前綴；本輪不實作
  - prefix: I
    description: 物品 / 道具（reserved，本輪不實作）
  - prefix: UI
    description: UI 文案（reserved，本輪不實作）
  - prefix: SKILL
    description: 技能說明（reserved，本輪不實作）

user_extensions:
  # user 在 Instance bootstrap 後可在此段加新類型
  # Template 內保持空 list；Instance bootstrap copy 後維持空 list 等 user 填
  []
```

**Template 不變的 invariant：**

- `version` 是 registry schema 版本；資料格式 specialist 未來改 schema 時 bump
- `core[*].locked: true` 一律不動（即使 user-extend）
- `reserved_prefixes` 是「保留前綴清單」 — user 加新類型不可用這些 prefix（避免未來工具加同名類型衝突）

## 7.3 Instance 層 schema

**檔案：** `<instance_root>/entity_type_registry.yaml`

**Instance bootstrap 行為：** `/init-project` 跑時自動 copy Template → Instance root。

**user 在 Instance 內加新類型範例：**

```yaml
# Entity Type Registry — Instance
# 本檔由 /init-project 從 Template 複製產生
# core 段不可動（不論本檔狀態如何，A.0 parser 對 core 段一律依 Template 解讀，避免 user 誤刪 core 後 break）
# user_extensions 段可自由 append

version: 1
schema_version: data_format_spec_v0.3        # [v0.4 patch via NEW_REQ_4 — 對齊 Template 版本]

core:
  # 沿用 Template，本檔內可省略不寫（A.0 parser 從 Template 載入 core）
  # 若 user 寫了，parser 比對若有差異則 ERROR
  []

reserved_prefixes:
  []

user_extensions:
  # user 加新類型
  - type: I
    description: 物品（user 啟用）
    id_pattern: ^I-.+$
    target_dir: 11_items/
    cross_ref_allowed: true
    locked: false                          # user-added 預設 false
    added_at: 2026-06-15
    added_by: user
  - type: QUEST
    description: 任務（user 自訂類別）
    id_pattern: ^QUEST-.+$
    target_dir: 14_quests/
    cross_ref_allowed: true
    locked: false
    added_at: 2026-07-01
    added_by: user
```

**Instance-only 欄位：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `added_at` | 是 | user 加該類型的日期 |
| `added_by` | 是 | `user` / `agent-assisted`（agent 推薦後 user 拍板）/ `external`（從外部 LLM 導入） |
| `locked` | 是 | user-added 預設 `false`；改 `true` 表示「user lock 這個類型不再改」 |

**規則：**

- user_extensions 內 `type` 不可跟 Template `core` 任一 `type` 重複（parser ERROR）
- user_extensions 內 `type` 的 prefix 不可在 `reserved_prefixes` 內（parser WARN — 仍允許但提示 user）
- user_extensions 內 `id_pattern` 必須是 valid regex（parser ERROR 否則）
- user_extensions 內 `target_dir` 必須是 valid 相對路徑（parser WARN 若 dir 不存在）

**target_dir schema 語意（v0.4 — NEW_REQ_5 細化）：**

- `target_dir` 型別：**string**（單一相對路徑 _或_ 逗號分隔的多個相對路徑 — comma-separated list）
- 多目錄寫法限定：僅 `S` 場景類型本來就跨 `06_scene_index/` + `07_scene_tasks/` + `08_dialogue_outputs/` 三目錄（見 §7.2 Template core 範例 S row）；其他 core 類型一律單一目錄
- Parser 行為：parser 讀 `target_dir` 字串 → 遇 `,` 則 split + trim 各段 → 每段獨立 validate「relative path 存在性」
- user_extensions 端：允許多目錄寫法（parser 不阻擋）但建議單一目錄；多目錄需 user 自行確保各路徑 valid
- 不採選項 a（`target_dirs: list[str]`）— v0.4 維持單欄 csv 寫法以最小變動（POST_LOCK_PENDING NEW_REQ_5 推薦選 b）

## 7.4 Parser 讀取行為

**A.0 parser 啟動時：**

1. 讀 Instance root `entity_type_registry.yaml`
2. 若該檔不存在 → 從 Template fallback（warn user「Instance 缺 registry，從 Template 啟動」）
3. 載入 `core` + `user_extensions` 為 valid entity type set
4. 對該 Instance 所有 .md 檔的 frontmatter `entities` / `depends_on` 內每個 ID：
   - 取 prefix（`-` 前段）
   - 比對 entity type set
   - 不在 set 內 → parser ERROR「未知 entity 類型 `<prefix>`」
   - 在 set 內 → 依 `id_pattern` regex 驗證 ID 格式；不符 → parser ERROR

**registry 改變後的行為：** user 編輯 registry 後需 refresh — 重啟 A.0 parser 或 `/status` 主動 reload registry。屬上下游 UD-12 細化。

## 7.5 `core: true` vs `core: false` 規則

| 屬性 | core: true | core: false（user-added） |
|---|---|---|
| 來源 | Template registry | Instance user_extensions |
| 可否刪除 | 否（parser 強制 fallback Template） | 是（user 編輯 .yaml 移除） |
| 可否改 `id_pattern` | 否 | 是 |
| 可否改 `target_dir` | 否 | 是 |
| Locked 行為 | `locked: true` 永遠 | `locked` user 可切 true/false |
| `/status` 完成度計算 | 計入 | 計入 |

## 7.6 11 種 core 紀錄（鏡像；權威見 entity_type_registry）

**[v0.5 partial supersede via NEW_REQ_48 / D-075 — 補 W-style + ORG，對齊 11 種 core 權威]**
本表為 **human-readable 鏡像**，**單一權威為** `_design/registries/entity_type_registry.template.yaml`（Instance 端 root `entity_type_registry.yaml`），以 `load_entity_type_registry()` 載入。本節原列 9 種（缺 W-style / ORG）為 i1 pre-existing drift（D-055 加 W-style / D-071 加 ORG 後未回填本鏡像，非 Batch-5 regression）；本輪補齊至 registry core 全 11 種、修正標題計數。**鏡像與 registry 不一致時以 registry 為準**；`scripts/check_entity_type_consistency.py` 斷言本鏡像 == registry core，drift 時 CI 報錯（Batch 6 加 REGISTRY-MIRROR marker 後升 ERROR 級強制）。鏡像保留以維 spec-doc 可讀性，不刪除、不 bump `schema_version`。

<!-- REGISTRY-MIRROR: entity-types -->
core 11 種：W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG
<!-- /REGISTRY-MIRROR -->

| Entity 類型 | 來源 | core | locked |
|---|---|---|---|
| W-rules | SPEC §5.1 LOCKED | true | true |
| W-language | SPEC §5.1 LOCKED | true | true |
| **W-style** | **D-055（文風樣本與指紋）** | **true** | **true** |
| V | SPEC §5.1 LOCKED | true | true |
| C-\<name\> | SPEC §5.1 LOCKED | true | true |
| R-\<a\>-\<b\> | SPEC §5.1 LOCKED | true | true |
| P | SPEC §5.1 LOCKED | true | true |
| CH-\<n\> | SPEC §5.1 LOCKED | true | true |
| S-\<ch\>-\<n\> | SPEC §5.1 LOCKED | true | true |
| **A-\<type\>-\<character\>-\<state\>** | **D-023 / DF-4** | **true** | **true** |
| **ORG-\<name\>** | **D-071 / D-074（組織型對抗源節點）** | **true** | **true** |

A-\* / ORG-\* 同列 `core: true` + `locked: true` — 表示「本工具保證 schema 支援」的 entity 類型集合；未來新增走 `user_extensions`（`core: false`）。完整 `id_pattern` / `target_dir` / subtype 規則以 `entity_type_registry.template.yaml` 為權威，本表僅鏡像類型存在與 core/locked 旗標。

## 7.7 user extension flow

**user 加新 entity 類型流程（建議由前端 F7 引導，本節只承諾 schema 容納）：**

1. user 在前端「設定 → entity 類型」介面 / 直接編輯 `entity_type_registry.yaml`
2. 加新 entry 到 `user_extensions` list
3. 工具 / parser 驗證：
   - prefix 不在 `core` / `reserved_prefixes` 內
   - `id_pattern` 為 valid regex
   - `target_dir` 為 valid 相對路徑
4. 通過驗證後 → 該類型立刻可在 frontmatter `entities` / `depends_on` 內使用
5. `/status` / Layer 3 export 等下游自動處理新類型（無需修改 SPEC）

**「進入工具的 entity 類型」生命週期：**

- 加入：`user_extensions` append
- 改變語意：user 編輯 entry
- 移除：user 刪 entry；若該類型已有 .md 檔依賴 → parser ERROR「現存 X-\* entity 但類型 X 已從 registry 移除」（防 silent drop）

## 7.8 對 SPEC §5.1 LOCKED 的 partial supersede 細則

**partial supersede 範圍：**

- ✓ 既有 7 種維持 LOCKED 語意（W-rules / W-language / V / C / R / P / CH / S）— 不動
- ✓ 加入 A-\* 為 9th core 類型（本輪 D-023）
- ✓ 加入可擴充機制（reserved_prefixes + user_extensions）— 未來新增類型不必動 SPEC §5.1
- ✗ 不變既有命名規則段（C-\<name\> 等 ID 規則）
- ✗ 不變既有目錄對應段（target_dir 與 SPEC §5.1 完全對齊）

**SPEC §5.1 在 master 第四輪整合時的更新建議：**

- 加副節「§5.1.x 可擴充 entity 類型機制」指向本 registry
- 既有 7 種列表後加 A-\* 為第 8 條目
- 加註：「user 可在 Instance entity_type_registry.yaml `user_extensions` 段加新類型」

## 7.9 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 既有 27 份模板 | 無 | registry 是新加機制不影響既有模板 |
| 新增 Template `_design/registries/entity_type_registry.template.yaml` | **新增** | 本節 §7.2 schema |
| `/init-project` skill | 微 | 加「複製 registry Template → Instance root」一步（屬上下游 UD-10 範圍） |

（§10 統籌總表）

## 7.10 對 A.0 parser 影響（本節版）

- parser 啟動時讀 Instance root `entity_type_registry.yaml`（fallback Template）
- 對 frontmatter `entities` / `depends_on` 驗證使用 valid type set
- 對每個 ID 驗證 `id_pattern` regex
- user_extensions 加入後 parser 支援 refresh

（§11 統籌總表）

## 7.11 Cross-ref

- D-025（資料類別範圍鎖定 + 留接口）/ REQUIREMENTS_LOCK §3.1
- P-023 — RESOLVED via 本節 + §8
- D-023（A-\* entity）/ 本檔 §5（A-\* 入 registry 為 core）
- SPEC §5.1（partial supersede via 本節 + §5）
- SPEC §7（Template/Instance 分層 — 本機制對齊）
- 上下游 UD-10（/init-project 複製 registry）
- 上下游 UD-12（跨 entity 類型 cross-reference 規則）

---

# 8. 可擴充 qa_type registry（DF-6）

## 8.0 本節性質

實作 D-027「QA 機制變可擴充 — qa_type enum 不再 LOCKED」的 schema 機制。本節決定：

- qa_type registry 三層架構（同 DF-5）
- 既有 5 + 本輪 3 = 8 種為 core；未來 user 可 user-extend（§8.5 ~ §8.6）
- 「QA 模組擴充協議」00_p 接點 schema（§8.7）
- 對 SPEC §5.2.4 LOCKED 的 partial supersede 細則（§8.8）

**設計原則：** 對齊 DF-5（同 Template/Instance 三層 + core vs user-added）；加 QA 特化內容（必對應 09_x 模板）。

## 8.1 三層架構（同 DF-5）

```
                  Template repo                 Instance（user 專案）
                  ──────────────                ──────────────
                  D:\劇本開發工具\               D:\<user-instance>\
                  _design/registries/           qa_type_registry.yaml
                  qa_type_registry              ↑（user 在這裡 user-extend）
                  .template.yaml
                                                ↑ Instance bootstrap 時 copy
```

職責跟 DF-5 三層完全對應（§7.1）。

## 8.2 Template 層 schema

**檔案：** `_design/registries/qa_type_registry.template.yaml`

**[v0.4 partial supersede via NEW_REQ_4 — 對齊 qa_type_registry.template.yaml v0.3 權威]**  
本節 v0.1/v0.2 原範例（`schema_version: v0.1` + `template_path: 09_a_AI_味檢查表.md` 等簡名路徑）已過時 — A.0.8 實作的 `qa_type_registry.template.yaml` 採 `09_quality_assurance/09_<x>_<名稱>模板.md` 完整相對路徑（對齊 SPEC §12.7 與實際模板檔位置）。下方範例直接以 v0.3 權威寫法呈現（schema 內容對齊 `_design/registries/qa_type_registry.template.yaml` line 13-50）：

```yaml
# QA Type Registry — Template
version: 1
schema_version: data_format_spec_v0.3

core:
  # SPEC §5.2.4 既有 5 種 — 本輪不動
  - qa_type: AI_FLAVOR
    description: AI 味檢查
    template_path: 09_quality_assurance/09_a_ai味qa報告模板.md
    locked: true
  - qa_type: VOICE_CONSISTENCY
    description: 角色聲線一致性檢查
    template_path: 09_quality_assurance/09_b_角色聲線一致性檢查模板.md
    locked: true
  - qa_type: FORBIDDEN_WORD
    description: 禁用詞檢查
    template_path: 09_quality_assurance/09_c_禁用詞檢查報告模板.md
    locked: true
  - qa_type: INFO_CONTROL
    description: 資訊控制檢查
    template_path: 09_quality_assurance/09_d_資訊控制檢查報告模板.md
    locked: true
  - qa_type: GENRE_DRIFT
    description: 類型偏移檢查
    template_path: 09_quality_assurance/09_f_類型偏移檢查模板.md
    locked: true

  # 本輪新增 3 種（DF-8 / D-026）
  - qa_type: RHYTHM
    description: 節奏感檢查（句長分布 / 變異度 / 長短交替 / 段落呼吸感）
    template_path: 09_quality_assurance/09_g_節奏感檢查模板.md
    locked: true
  - qa_type: DRAMATIC_TENSION
    description: 對話張力檢查（推進 / 讓步 / 揭穿 / 反擊頻率 + 攻防力度量化）
    template_path: 09_quality_assurance/09_h_對話張力檢查模板.md
    locked: true
  - qa_type: CROSS_SCENE_CONTINUITY
    description: 跨場一致性檢查（跨場聲線漂移 / 跨場資訊洩漏 / 跨場節奏 arc）
    template_path: 09_quality_assurance/09_i_跨場一致性檢查模板.md
    locked: true

# 09_e final-gating 紀錄不在 QA pipeline，不入 registry（屬 UPSTREAM §3.5 範圍）

user_extensions:
  # user 加新 qa_type 必須對應一份 09_x 模板（§8.6 規則）
  []
```

## 8.3 Instance 層 schema

**檔案：** `<instance_root>/qa_type_registry.yaml`

**Instance bootstrap 行為：** 同 DF-5 — `/init-project` 從 Template 複製。

**user 加新 qa_type 範例：**

```yaml
version: 1
schema_version: data_format_spec_v0.3        # [v0.4 patch via NEW_REQ_4 — 對齊 Template 版本]

core:
  []                                        # 沿用 Template

user_extensions:
  - qa_type: LORE_CONSISTENCY
    description: 設定一致性檢查（與世界觀 W-rules 對齊）
    template_path: 09_quality_assurance/09_j_設定一致性檢查.md   # [v0.4 patch — 對齊 §8.2 + UD §3.10.2 repo-root 完整相對路徑]
    locked: false
    added_at: 2026-06-20
    added_by: user
    extension_protocol: 00_p_QA模組擴充協議.md  # 可選；對應 §8.7
    # v0.4 NEW_REQ_6 對齊 — UD §3.10.2 / §3.10.3 引入下列選填欄位（runtime 行為描述，非 schema 強驗）
    algorithm:                              # 選填 — 對應 09_x 模板 §2 algorithm 欄位；parser 不強驗內部結構
      - step: 句長變異度
        metric: CV
        threshold:
          pass: [0.4, 1.2]
          fail: '<0.3'
    report_template: |                       # 選填 — 對應 09_x 模板 §3 報告骨架；parser 不強驗內容
      ## 檢查對象
      ## 總結判定
      ...
```

**Instance-only 欄位（v0.4 — NEW_REQ_6 對齊擴充）：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `added_at` | 是 | user 加該 qa_type 日期 |
| `added_by` | 是 | `user` / `agent-assisted` / `external` |
| `locked` | 是 | user-added 預設 `false` |
| `template_path` | 是 | 對應 09_x 模板路徑（**repo-root 完整相對路徑**，如 `09_quality_assurance/09_j_...md`；對齊 §8.2 core 範例 + UD §3.10.2 寫法）|
| `extension_protocol` | 否 | 對應 00_p 協議檔（若 user 走完整擴充協議流程） |
| `algorithm` | 否 | **v0.4 新（NEW_REQ_6 對齊）** — runtime algorithm 規則的宣告式表達（對應 UD §3.10.3 5 必要區段 §2）；parser 不強驗內部結構，但偵測欄位存在 |
| `report_template` | 否 | **v0.4 新（NEW_REQ_6 對齊）** — runtime 報告骨架字串（對應 UD §3.10.3 5 必要區段 §3）；parser 不強驗內容 |

## 8.4 Parser 讀取行為

同 DF-5 §7.4 — A.0 parser 啟動時讀 Instance root `qa_type_registry.yaml` + fallback Template。

**對 frontmatter `qa_type` 欄位的驗證：**

- 載入 valid qa_type set（core ∪ user_extensions）
- QA 報告檔的 frontmatter `qa_type` 值必須在 set 內 → 不在 → parser ERROR

## 8.5 core vs user-extended

**Core qa_type（本輪共 8 種）：**

| qa_type | 來源 | template |
|---|---|---|
| AI_FLAVOR | SPEC §5.2.4 既有 | 09_a |
| VOICE_CONSISTENCY | SPEC §5.2.4 既有 | 09_b |
| FORBIDDEN_WORD | SPEC §5.2.4 既有 | 09_c |
| INFO_CONTROL | SPEC §5.2.4 既有 | 09_d |
| GENRE_DRIFT | SPEC §5.2.4 既有 | 09_f |
| **RHYTHM** | **本輪 DF-8 / D-026** | **09_g** |
| **DRAMATIC_TENSION** | **本輪 DF-8 / D-026** | **09_h** |
| **CROSS_SCENE_CONTINUITY** | **本輪 DF-8 / D-026** | **09_i** |

**User-extended：** 全部走 `user_extensions` 段。

## 8.6 user 新增 qa_type 流程 + 09_x 模板對應規則

**前置要求：**

- 必有對應 09_x 模板存在於 `09_quality_assurance/`（parser 驗證 `template_path` 對應檔案存在）
- 09_x 模板的 frontmatter 必含 `qa_type: <new_type>` 對應值

**流程（建議由前端 F7 引導 / 由 00_p 協議規範，屬上下游 UD-8 範圍）：**

1. user 撰寫 09_x 模板（如 `09_j_設定一致性檢查.md`）
2. user 在 `qa_type_registry.yaml` 的 `user_extensions` 加 entry
3. parser refresh → 新 qa_type 立即可用於 `/qa` 流程
4. 之後 `/qa` 跑該 type → 產生 QA 報告檔 `<base>_LORE_CONSISTENCY.md`

**對應「QA 模組擴充協議」00_p：** 此協議由上下游 UD-8 設計具體內容；本檔 §8.7 只承諾 schema 容納其接點。

## 8.7 「QA 模組擴充協議」00_p 接點 schema

**性質：** 00_p 是協議檔（如 00_a / 00_e 等），描述「user 怎麼加新 QA 模組」的完整流程。**本檔不寫 00_p 內容**（屬上下游 UD-8 範圍）。**本節只承諾資料層 schema 容納其接點。**

**接點：**

- `qa_type_registry.yaml` `user_extensions[*].extension_protocol` 欄位（§8.3）— 可指向 00_p
- 09_x 模板（user 新加）內 frontmatter 可含 `extension_protocol: 00_p` 標記（屬上下游決定，本檔不強制）
- A.0 parser 對 00_p 自身不做驗證（協議檔不在 entity 範圍）

**user 是否走 00_p 不影響 qa_type 加入結果：** registry entry 寫對 + 09_x 模板存在 + frontmatter `qa_type` 對應正確 → qa_type 即可生效。00_p 是「指引性」協議，非「強制」。

## 8.8 對 SPEC §5.2.4 LOCKED 的 partial supersede 細則

**partial supersede 範圍：**

- ✓ 既有 5 種 qa_type 維持語意 — 不動
- ✓ 加入 3 種 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY（§6.2 / DF-8）
- ✓ qa_type 從 LOCKED enum 變「可擴充 list（core ∪ user_extensions）」（本節 DF-6）
- ✗ 不變 mode_tag enum 機制（DF-8 只加 1 值，不變「可擴充」）
- ✗ 不變 `狀態` / `pipeline_state` / `qa_decision` 三項 LOCKED enum

**SPEC §5.2.4 在 master 第四輪整合時的更新建議：**

- 加副節「§5.2.4.x qa_type 可擴充機制」指向本 registry
- 既有「qa_type | 僅 QA 報告檔填：...」描述更新為「核心 8 種 + user_extensions 擴充」
- 加註：「user 可在 Instance qa_type_registry.yaml `user_extensions` 段加新 qa_type，必有對應 09_x 模板」

## 8.9 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 既有 09_a / 09_b / 09_c / 09_d / 09_e / 09_f 模板 | 無 | 不動（registry Template 將其 path 列入 core） |
| 既有 08_a / 08_b / 00_k 等 | 無 | 不動 |
| 新增 Template `_design/registries/qa_type_registry.template.yaml` | **新增** | 本節 §8.2 schema |
| `/init-project` skill | 微 | 加「複製 qa_type registry Template → Instance root」一步（屬上下游 UD-10） |
| 候選 00_p 協議檔 | **可能新增** | 屬上下游 UD-8 範圍；本節提供接點 |

（§10 統籌總表）

## 8.10 對 A.0 parser 影響（本節版）

- parser 啟動時讀 `qa_type_registry.yaml` + fallback Template
- 對 QA 報告檔 frontmatter `qa_type` 驗證
- 對 user_extensions[*].template_path 驗證對應檔案存在
- user 加新 qa_type 後支援 refresh
- **v0.4 NEW_REQ_6 對齊** — parser 對 `user_extensions[*].algorithm` 與 `user_extensions[*].report_template` 兩選填欄位：
  - 存在性偵測：parser 讀取後存入 RegistryEntry，但**不**強驗內部 schema（algorithm 為 list-of-step 結構，report_template 為自由字串）
  - runtime 由 09_x 模板執行者（Phase B+ /qa pipeline）消費，parser 端只負責讀取暴露
  - 若 user 漏填 algorithm 或 report_template → parser 不報錯（兩欄為選填）；下游若需求閾值會在 09_x 模板執行期報缺漏

（§11 統籌總表）

## 8.11 Cross-ref

- D-027（QA 機制變可擴充）/ REQUIREMENTS_LOCK §4.2
- P-023 / P-026 — 屬上下游 UD-8 細化（本節只保 schema 容納）
- DF-5 §7 — 同三層機制
- DF-8 §6 — 3 種新 qa_type 加入 registry core
- SPEC §5.2.4（partial supersede via 本節 + §6）
- 上下游 UD-8（00_p 協議內容）/ UD-10（/init-project 複製 registry）

---

# 9. JSON 中介格式 schema（DF-7）

## 9.0 本節性質

實作 D-024「套版機制大幅縮減 — 固定 JSON + MD 雙吐」中的 JSON schema。本節決定：

- 整體結構 — 單檔 dump（master 確認方向 #4）
- manifest header + records[] array（§9.1 ~ §9.3）
- 各類 record schema 對齊 SPEC §5.2 frontmatter（§9.4 ~ §9.6）
- 一對一映射規則（§9.7）

**設計原則（依 D-024 / Master 確認方向）：**

- 單檔 JSON dump（不是多檔 per-entity）— 對齊「一個 export skill 吐 JSON + MD 雙檔」
- 內含 `manifest`（metadata）+ `records[]`（所有 entity / dialogue line / A-\* asset 內容）
- 跟 SPEC §5.2 frontmatter 一對一映射 — 既有欄位完整映射 + 本輪新增 KEY / A-\* / phase_log 等同樣映射
- 「轉檔到引擎」是外部 script 責任（吃這份 JSON）— 不是本工具的事

## 9.1 整體結構（top-level）

```json
{
  "manifest": {
    "export_version": "1.0",
    "exported_at": "2026-05-22T14:30:00Z",
    "tool_version": "v0.1",
    "instance_id": "<work-name>",
    "spec_version": "data_format_spec_v0.4",
    "stats": {
      "total_entities": 47,
      "total_dialogue_lines": 1532,
      "total_art_assets": 23,
      "by_entity_type": {
        "C": 8, "R": 6, "S": 15, "CH": 12, "A": 23, "...": "..."
      }
    },
    "entity_type_registry": { "... snapshot": "..." },
    "qa_type_registry": { "... snapshot": "..." }
  },
  "records": [
    { "record_type": "entity", "...": "..." },
    { "record_type": "dialogue_line", "...": "..." },
    { "record_type": "art_metadata", "...": "..." }
  ]
}
```

**頂層欄位：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `manifest` | 是 | export metadata + stats + registry snapshot |
| `records` | 是 | 所有實體內容 array；每筆有 `record_type` 區分類型 |

## 9.2 manifest header schema

**完整欄位：**

| 欄位 | 必填 | 型別 | 說明 |
|---|---|---|---|
| `export_version` | 是 | string | 本 schema 版本（本檔 v0.1 對應 `"1.0"`） |
| `exported_at` | 是 | ISO 8601 datetime | export 執行時間 |
| `tool_version` | 是 | string | 跑 export 的工具版本 |
| `instance_id` | 是 | string | Instance 識別字（通常等於 Instance 資料夾名） |
| `spec_version` | 是 | string | DATA_FORMAT_SPEC 對齊版本 |
| `stats` | 是 | object | 統計概要（見下） |
| `entity_type_registry` | 是 | object | 本次 export 時的 entity_type_registry snapshot |
| `qa_type_registry` | 是 | object | 本次 export 時的 qa_type_registry snapshot |
| `instance_meta` | 否 | object | Instance 級 metadata（作品名、author、創建日等） |

**`stats` 子欄位：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `total_entities` | 是 | 全 entity 數（不含 dialogue line / art_metadata records） |
| `total_dialogue_lines` | 是 | 全 dialogue line 數 |
| `total_art_assets` | 是 | 全 A-\* asset 數 |
| `by_entity_type` | 是 | 每個 entity 類型的數量 map |

## 9.3 records[] array

**所有 record 共通欄位：**

| 欄位 | 必填 | 說明 |
|---|---|---|
| `record_type` | 是 | `entity` / `dialogue_line` / `art_metadata` |
| `source_file` | 是 | 對應 .md 檔的相對路徑（從 Instance root 起算） |

**Record 類型：**

- **entity** — 對應 SPEC §5.2 上游 / 靜態檔 frontmatter 一份
- **dialogue_line** — 對應 §4.2 `dialogue_keys` block 中一筆 entry（每段台詞一 record）
- **art_metadata** — 對應 §5.3 `art_metadata` block 中一筆 entry（每個 A-\* asset 一 record）

## 9.4 `record_type: entity` schema

**對應 SPEC §5.2 上游 / 靜態檔（如 03_characters/主角A_聲線卡.md）：**

```json
{
  "record_type": "entity",
  "source_file": "03_characters/main/主角A_聲線卡.md",
  "header": {
    "狀態": "REVIEW",
    "版本": "v0.2",
    "最後更新": "2026-05-18",
    "適用範圍": "主角A 聲線卡",
    "優先級": "高"
  },
  "frontmatter": {
    "entities": ["C-主角A", "R-主角A-反派B"],
    "depends_on": ["W-rules", "W-language"],
    "weight": {
      "C-主角A": 1.0,
      "R-主角A-反派B": 0.3
    }
  },
  "body": "（自由文字內容；markdown 原文，保留內文 HTML comment 如 <!-- KEY: ... -->）",
  "downstream_fields": {
    "scene_id": null,
    "pipeline_state": null,
    "mode_tag": null,
    "qa_decision": null,
    "qa_type": null
  }
}
```

**規則：**

- `header` 5 欄完整映射 SPEC §5.2 中文 header（鍵用中文）
- `frontmatter` 含 YAML block 上游 3 欄（entities / depends_on / weight）
- `body` 是自由文字（保留 markdown 原文，包括內文 HTML comment）
- `downstream_fields` 對應 SPEC §5.2 下游 8 欄；上游檔對應 null
- A-\* metadata 檔對應的 `entity` record 內含 `art_metadata` 子欄位（§9.6）

## 9.5 `record_type: dialogue_line` schema（v0.2 — 對齊 Map shape + lifecycle metadata）

**對應 §4.2 `dialogue_keys` Map 中每筆 entry：**

```json
{
  "record_type": "dialogue_line",
  "source_file": "08_dialogue_outputs/CH01_S03_xxx_dialogue_v02.md",
  "key": "dlg.ch01.s03.l001",
  "line_index": 1,
  "speaker": "C-主角A",
  "aliases": ["dlg.ch01.s03.l001"],
  "portrait": "A-portrait-主角A-anger",
  "bgm": "A-bgm-tension-01",
  "sfx": ["A-sfx-glass-break"],
  "status": "active",
  "created_at": "2026-05-22",
  "renamed_at": null,
  "deleted_at": null,
  "deprecated_reason": null,
  "source_keys": null,                              // v0.3 新增 via master 第四輪 CC-04 — 句級收斂 lineage；僅 v02 收斂版有意義（如 ["v01A.l005", "v01B.l006"]）
  "content": "你以為我會就這樣放棄？",
  "in_scene_context": {
    "scene_id": "S-01-03"
  }
}
```

**v0.2 變更：**
- 加 `portrait` / `bgm` / `sfx` / `status` / `deprecated_reason` 5 欄（v0.1 缺）— 對齊 §4.2 Map entry 完整欄位
- 移除 `in_scene_context.art_refs[]`（v0.1 寫法依「內文 HTML comment」抽取）— **權威來源改為 frontmatter dialogue_keys Map 內 `portrait/bgm/sfx`**（v0.2 per D-037 + C-02 解決）
- `in_scene_context` 簡化為只含 `scene_id`（其他句級 A-\* 資料移到 record 頂層）

**規則：**

- `key` 為 source file 中 `dialogue_keys` map key（v0.2）
- `line_index` / `speaker` / `aliases` / `portrait` / `bgm` / `sfx` / `status` / `created_at` / `renamed_at` / `deleted_at` / `deprecated_reason` 完整映射 §4.2 Map entry 欄位
- `content` 是該 KEY 對應的台詞本文（從內文 KEY comment 後面的下一段抓出，剝離 markdown 強調 `**主角A：**` 等說話人前綴）
- `status: deleted` 的 dialogue_line **預設不出現**在 records[]（v0.3 校正 CC-07：對齊 L3_EXPORT_PROMPT_SCHEMA `include_deleted: false` 預設行為；原「軟刪除原則仍輸出」supersede）；僅當 prompt 元資料 `include_deleted: true` 時才含；`content` 為內文移除後的存留（通常為 null 或 source file 寫入時的最後版本）
- `status: deprecated` 的 dialogue_line 仍出現在 records[]；`content` 保留；`deprecated_reason` 必填
- `in_scene_context.scene_id` 對應 source file 的 frontmatter `scene_id`

**「不存多語對白本文」原則仍維持：** `content` 是當前語言（zh-Hant）；不含 `content_en` / `content_ja` 等多語版本。外部 i18n 系統用 `key` 引用 + 維護自己的多語對照表。

## 9.6 `record_type: art_metadata` schema（v0.2 — 對齊 7 種 subtype）

**對應 §5.3 `art_metadata` block 中每筆 entry：**

```json
{
  "record_type": "art_metadata",
  "source_file": "10_art_assets/portraits/主角A.md",
  "asset_id": "A-portrait-主角A-anger",
  "display_name": "主角A 憤怒立繪",
  "subtype": "portrait",
  "owner": "C-主角A",
  "state_tags": ["anger", "hostile", "combat"],
  "aliases": ["A-portrait-主角A-anger"],
  "dialogue_keys_ref": null,
  "created_at": "2026-05-22",
  "renamed_at": null,
  "deleted_at": null
}
```

**v0.2 變更：**
- v0.1 `character` → v0.2 `owner`（語意擴大，per D-044 + §5.1）
- 新增 `subtype` 欄位（7 種 enum，per §5.1a）
- 新增 `dialogue_keys_ref` 欄位（僅 subtype=voice 有意義）

**規則：** 完整映射 §5.3 `art_metadata` schema（v0.2）。

**A-voice-\* record 範例：**

```json
{
  "record_type": "art_metadata",
  "source_file": "10_art_assets/voice/主角A.md",
  "asset_id": "A-voice-主角A-line001",
  "display_name": "主角A 第 1 句配音",
  "subtype": "voice",
  "owner": "C-主角A",
  "state_tags": [],
  "aliases": ["A-voice-主角A-line001"],
  "dialogue_keys_ref": "dlg.ch01.s03.l001",
  "created_at": "2026-05-22",
  "renamed_at": null,
  "deleted_at": null
}
```

**強制：** 不含 `file_path` / `url` / `source_image` / `binary_data` 等指向實檔欄位（§5.7 規則延伸至 JSON output）。

## 9.7 跟 SPEC §5.2 frontmatter 一對一映射規則（v0.2 — Map shape）

| SPEC §5.2 frontmatter 欄位 | JSON output 對應 |
|---|---|
| 中文 header 5 欄 | `entity` record 的 `header` 子物件 |
| YAML 上游 3 欄（entities / depends_on / weight） | `entity` record 的 `frontmatter` 子物件 |
| YAML 下游 8 欄（scene_id / source_task / source_dialogue / source_dialogues / pipeline_state / mode_tag / qa_decision / qa_type） | `entity` record 的 `downstream_fields` 子物件 |
| 內文 `<!-- KEY: ... -->` | `dialogue_line` record 的 `key`（與 frontmatter dialogue_keys map key 校驗一致） |
| **frontmatter `dialogue_keys[<KEY>].portrait/bgm/sfx`**（v0.2 權威來源） | `dialogue_line` record 的 `portrait` / `bgm` / `sfx` 三欄 |
| ~~內文 `<!-- 立繪：A-... -->` / `<!-- 背景：A-... -->`~~（v0.1 寫法廢） | 不再參與 JSON 映射（v0.2 — 純 view-layer 提示，per D-037） |
| `dialogue_keys` Map 中每筆 (key, entry) | 各自一筆 `dialogue_line` record |
| `art_metadata` block 每筆 entry | 各自一筆 `art_metadata` record |

**對齊規則：** JSON 是「frontmatter 的 1:1 結構化序列化」 — 不做 transform / 不做 derive；transform 是外部 script 責任。

## 9.8 輸出檔名 / 位置 / git 管理（指引）

**本節只給指引；具體 export skill 設計屬上下游 UD-3 範圍。**

**建議（v0.3 對齊 master 第四輪 CC-07 校正）：**

- 輸出檔名：`export/<instance_id>_<YYYYMMDD>_<HHMMSS>.json` + `export/<instance_id>_<YYYYMMDD>_<HHMMSS>.md`
- 位置：Instance root `export/` 目錄（建議加入 `.gitignore`，因為 export 是衍生產物）
- 同次 export 同時產 JSON + MD 兩檔（D-024 雙吐）
- **export 跑完後 phase_log 不寫入任何 entry**（v0.3 master 第四輪 CC-07 校正；L3 export 為純 read-only contract；不污染 phase_log；原「補一筆 phase: export entry」supersede）

## 9.9 對既有 27 份模板遷移影響（本節版）

| 模板區塊 | 衝擊 | 處理 |
|---|---|---|
| 既有 27 份模板 | 無 | export 是「讀取既有模板 → 吐 JSON+MD」單向流程 |
| `/export-*` 4 個 skill 設計 | 無 | 屬上下游 UD-3 範圍 |
| `.gitignore` | 微 | 加 `export/` 行（屬上下游 UD-3 / Master 整合） |

（§10 統籌總表）

## 9.10 對 A.0 parser 影響（本節版）

- A.0 parser 不直接負責 export
- export skill（屬上下游 UD-3）讀已 parse 的資料結構產 JSON
- parser 提供「結構化資料」API 給 export skill 用（屬 ARCHITECTURE 範圍）

（§11 統籌總表）

## 9.11 Cross-ref

- D-024（套版機制大幅縮減）/ REQUIREMENTS_LOCK §3.4
- P-024 — RESOLVED via 本節
- D-018 #6 partial supersede / 本檔 §2.6
- 上下游 UD-3（Layer 3 export skill 設計 — Contract A 出口）/ P-030
- DF-3 §4（KEY 機制）→ dialogue_line records
- DF-4 §5（A-\* entity）→ art_metadata records
- DF-5 §7 / DF-6 §8（registry）→ manifest snapshot

# 10. 對既有 27 份模板遷移影響（DF-9）

## 10.0 本節性質

把 §2.7 / §3.6 / §4.7 / §5.8 / §6.4 / §7.9 / §8.9 / §9.9 各節提到的遷移影響統一彙整成一張表，給 CODEX tier 2 寫實檔時作 checklist 使用。

**遷移影響分四類：**

- **A. 完全不動（既有 LOCKED）** — 既有模板保留原狀
- **B. 微調（既有模板加範例 / 加可選欄位範例）** — Master 第四輪整合 + CODEX tier 2 處理
- **C. 新增模板** — 由上下游 specialist 設計具體內容
- **D. 新增 registry / config 檔** — 由本 specialist（資料格式）提供 Template schema

## 10.1 27 份既有模板逐項影響表

| 模板 ID | 模板名稱 | 遷移類型 | 需新增欄位 | 需新增區段 | CODEX tier 2 checklist |
|---|---|---|---|---|---|
| 00_a | 台詞生產協議 | A | 無 | 無 | 不動 |
| 00_b | 反 AI 味檢查表 | A | 無 | 無 | 不動 |
| 00_c | 台詞輸出格式 | A | 無 | 無 | 不動 |
| 00_d | 工作流總覽 | A | 無 | 無 | 不動 |
| 00_e | 世界觀創建協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |
| 00_f | 角色創建協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |
| 00_g | 大綱創建協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |
| 00_h | 細綱創建協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |
| **00_i** | **專案初始化協議** | **B** | 無 | 加「§X 複製 registry Template → Instance root」段 | 屬上下游 UD-10 範圍；CODEX tier 2 對 00_i 加「Phase 0 複製 `_design/registries/*.template.yaml` 兩份到 Instance root 並去掉 `.template` 後綴」步驟 |
| 00_j | 迭代協議 | A | 無 | 無 | 不動 |
| 00_k | 台詞生產流程協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫；09_g/h/i 加入流程屬上下游 UD-6 範圍） |
| 00_l | 關係創建協議 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |
| 01_a | 世界觀總覽 | A | 無 | 無 | 不動 |
| 01_b | 世界語言規格 | A | 無 | 無 | 不動 |
| 01_c | 陣營與階級語言 | A | 無 | 無 | 不動 |
| 02_a | 詞彙系統 | A | 無 | 無 | 不動 |
| 03_a | 角色聲線卡（範本） | A | 無 | 無 | 不動 |
| 04_a | 角色關係矩陣 | A | 無 | 無 | 不動 |
| 05_a | 主線大綱 | A | 無 | 無 | 不動 |
| 05_b | 章節分布 | A | 無 | 無 | 不動 |
| 05_c | 角色弧線表 | A | 無 | 無 | 不動 |
| 05_d | 篇章節奏分布 | A | 無 | 無 | 不動 |
| 05_e | 衝突推進結構 | A | 無 | 無 | 不動 |
| 06_a | 場景索引（範本） | A | 無 | 無 | 不動 |
| **07_a** | **場景任務包（範本）** | **B** | frontmatter `depends_on` 範例加 A-\* | 無 | 加「`depends_on` 範例含 `A-portrait-主角A-default` / `A-bg-cafe-day`」（屬上下游 UD-5 範圍） |
| 08_a | 台詞輸出格式 | A | 無 | 無 | 不動 |
| **08_b** | **台詞輸出範本** | **B** | frontmatter 加 `dialogue_keys` **Map** 範例（v0.2 — list→Map）+ 內文加 `<!-- KEY: ... -->` 範例（view-layer 提示） | 加「§X i18n KEY 對應段」 | 屬上下游 UD-5 範圍；CODEX tier 2 對 08_b 加 dialogue_keys **Map** 完整範例（3-5 句台詞 + 對應 KEY 含 portrait/bgm/sfx/status），且每段台詞前加 `<!-- KEY: ... -->`（view-layer，權威來源為 frontmatter Map） |
| 09_a | AI 味檢查表 | A | 無 | 無 | 不動 |
| 09_b | 角色聲線一致性 | A | 無 | 無 | 不動（跨場 QA 由 09_i 處理，09_b 維持原 algorithm） |
| 09_c | 禁用詞檢查 | A | 無 | 無 | 不動 |
| 09_d | 資訊控制檢查 | A | 無 | 無 | 不動（跨場資訊洩漏由 09_i 處理） |
| 09_e | 定稿變更紀錄 | A | 無 | 無 | 不動 |
| 09_f | 類型偏移檢查 | A | 無 | 無 | 不動（CODEX tier 1 已寫） |

**統計：** 27 份既有模板中 25 份完全不動（類型 A）/ 2 份微調（類型 B：07_a + 08_b）/ 1 份 0_i 加一步（屬上下游 UD-10 範圍）。

## 10.2 本輪新增模板 / 新增 config 檔清單

| 新增項 | 類型 | Owner | 對應 D/P/DF |
|---|---|---|---|
| **09_g_節奏感檢查.md** | C | 上下游 UD-6 | D-026 / 本檔 §6.2 |
| **09_h_對話張力檢查.md** | C | 上下游 UD-6 | D-026 / 本檔 §6.2 |
| **09_i_跨場一致性檢查.md** | C | 上下游 UD-6 | D-026 / 本檔 §6.2 |
| **10_a_portrait_index.md** | C | 上下游 UD-4 | D-023 / 本檔 §5.2 |
| **10_b_background_index.md** | C | 上下游 UD-4 | D-023 / 本檔 §5.2 |
| **10_c_cg_index.md** | C | 上下游 UD-4 | D-023 / 本檔 §5.2 |
| **10_d_sfx_index.md**（v0.2 — 取代 v0.1 icon_index） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_e_bgm_index.md**（v0.2 — 取代 v0.1 effect_index） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_f_voice_index.md**（v0.2 新） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_g_ui_index.md**（v0.2 新） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_art_assets/portraits/\<character\>.md**（範本） | C | 上下游 UD-4 | D-023 / 本檔 §5.3 |
| **10_art_assets/backgrounds/\<scene\>.md**（範本） | C | 上下游 UD-4 | D-023 / 本檔 §5.3 |
| **10_art_assets/cg/\<scene\>.md**（v0.2 新範本） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_art_assets/sfx/\<group\>.md**（v0.2 新範本） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_art_assets/bgm/\<mood\>.md**（v0.2 新範本） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_art_assets/voice/\<character\>.md**（v0.2 新範本） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **10_art_assets/ui/\<block\>.md**（v0.2 新範本） | C | 上下游 UD-4 | D-044 / 本檔 §5.2 |
| **候選 00_p_QA模組擴充協議.md** | C（如本輪寫） | 上下游 UD-8 | D-027 / 本檔 §8.7 |
| **候選 00_q_美術資產對應協議.md** | C（如本輪寫） | 上下游 UD-4 | D-023 / 本檔 §5 整體 |
| **\_design/registries/entity\_type\_registry.template.yaml** | D | **資料格式（本檔）** | D-025 / 本檔 §7.2 |
| **\_design/registries/qa\_type\_registry.template.yaml** | D | **資料格式（本檔）** | D-027 / 本檔 §8.2 |
| **Instance root entity\_type\_registry.yaml**（bootstrap 複製產物） | D | 上下游 UD-10（/init-project） | 本檔 §7.3 |
| **Instance root qa\_type\_registry.yaml**（bootstrap 複製產物） | D | 上下游 UD-10（/init-project） | 本檔 §8.3 |

**CODEX tier 2 對應動作（本檔 owner 部分）：**

- 在 master 第四輪整合 / CODEX tier 2 階段，CODEX 從本檔 §7.2 / §8.2 摘出兩份 Template YAML 寫成實檔放到 `_design/registries/` 目錄

## 10.3 既有 27 份模板的 frontmatter 完全不需動的證明

| 既有 LOCKED 元件 | 影響 |
|---|---|
| 中文 header 5 欄（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級） | 本輪零變動 |
| YAML 上游 3 欄（entities / depends_on / weight） | 本輪零變動 |
| YAML 下游 8 欄（scene_id / source_task / source_dialogue / source_dialogues / pipeline_state / mode_tag / qa_decision / qa_type） | 本輪零變動（mode_tag / qa_type 是值域擴充而非欄位變動） |
| 狀態 7 enum / pipeline_state 9 enum / qa_decision 4 enum | 本輪零變動 |
| mode_tag enum | 加 1 值（SINGLE_ITER）— SPEC §5.2.4 範例段更新；frontmatter 結構不變 |
| qa_type enum | 加 3 值 + 變開放可擴充 — SPEC §5.2.4 範例段更新；frontmatter 結構不變 |

**結論：既有 27 份模板的 frontmatter 結構零破壞**。新增欄位（`dialogue_keys` / `art_metadata`）只在新場景使用（下游台詞檔 / A-\* metadata 檔），上游模板不受影響。

## 10.4 CODEX tier 2 對本檔 owner 部分的 checklist 摘要

CODEX tier 2 階段（在 master 第四輪整合 promote 本檔提案後）需處理：

```
☐ 1. 從 §7.2 摘 entity_type_registry.template.yaml → 寫到 _design/registries/entity_type_registry.template.yaml
☐ 2. 從 §8.2 摘 qa_type_registry.template.yaml → 寫到 _design/registries/qa_type_registry.template.yaml
☐ 3. 確認 _design/registries/ 目錄存在；若不存在則建
☐ 4. 確認兩份 .template.yaml 通過 YAML syntax check
☐ 5. 確認兩份 Template 的 core 段 entry 數量：entity=9（7 既有 + A-\*）/ qa_type=8（5 既有 + 3 本輪）
☐ 6. 確認兩份 Template 的 user_extensions 段為空 list `[]`
☐ 7. 確認 .gitignore 不排除 _design/registries/（registries Template 要進 git）
```

**其他部分（B / C 類型遷移）：** 屬上下游 UD-2/4/5/6/8/10 與 UX UX-12 範圍，CODEX tier 2 從各 owner spec 摘出。

---

# 11. 對 A.0 parser 影響（DF-10）

## 11.0 本節性質

把 §3.7 / §4.8 / §5.9 / §6.5 / §7.10 / §8.10 / §9.10 各節 parser 影響統籌成一份「parser 必處理項清單」給上下游 UD-2（parser 設計 owner）引用。

## 11.1 Parser 必處理項 9 大類清單

依本檔提案，A.0 parser 在 v0.1 schema 下必處理以下 9 大類事項：

### 11.1.1 phase_log 新欄位解析（DF-2）

- 解析 `.protocol_version.phase_log[*].status` enum：`completed` / `in_progress` / `aborted`
  - 預設視為 `in_progress`（保守解讀，避免誤判 skill 已完成）
  - `status: aborted` 必有 `abort_reason` + `detail`，否則 ERROR
- 解析 `.protocol_version.phase_log[*].import_source` enum：`agent_assisted` / `external_llm` / `null`
  - 預設視為 `null`
  - `import_source ≠ null` 但 skill 不是 `/create-*` 系列 → ERROR
- **v0.2 新增**（per D-042）：解析 5 個新欄位
  - `entities_touched: List[entity_id]` — 各 ID 須符合 §7 entity_type_registry valid set；省略 → 視為空 list
  - `iteration_count: int` — 僅 `mode_tag: SINGLE_ITER` 時有意義；其他 mode_tag 出現此欄 → WARN
  - `iteration_note: free text` — 僅 SINGLE_ITER 時有意義
  - `base_dialogue: file_path` — 僅 SINGLE_ITER 且 `iteration_count >= 2` 時必填；指向另一檔的 path；驗證 base_dialogue 鏈條不形成 cycle → ERROR 否則
  - `conflict_resolutions: List[dict]` — 僅 `import_source ≠ null` 時有意義；驗證 `decision` 在 enum `merge / overwrite / create-as-new / skip` 內；`decision: create-as-new` 必填 `new_entity_id`；違反 → ERROR

### 11.1.2 dialogue_keys Map 解析（DF-3，v0.2 — list→Map per D-037）

- 解析下游 `08_dialogue_outputs/**/*.md` frontmatter `dialogue_keys` **Map**
  - 各 map entry 欄位驗證：`line_index` / `speaker` / `aliases` / `portrait` / `bgm` / `sfx` / `status` / `created_at`（+ 選用 `renamed_at` / `deleted_at` / `deprecated_reason`）
- 解析內文 HTML comment `<!-- KEY: <key> -->`
  - KEY 必為 dialogue_keys map 的 key（map key）→ 不符 ERROR
  - 順序必須跟 map entry 的 `line_index` 順序一致 → 不一致 ERROR
- 驗證一檔內 map key unique（YAML 本身保證；違反 = YAML parse error）
- 驗證 KEY 語法符合 §4.1 預設語法（預設名）/ user-defined 規則
- 驗證 `aliases[0]` 為預設名格式
- **v0.2 新增驗證**：
  - `status` 值在 `active / deprecated / deleted` enum 內
  - `status: deleted` 必有 `deleted_at`；`status: deprecated` 必有 `deprecated_reason`
  - `portrait` / `bgm` 值（若非 null）必須對應 valid A-\* asset_id（cross-check `art_metadata`）
  - `sfx` list 各元素必須對應 valid A-sfx-\* asset_id
  - 內文 `<!-- 立繪：A-... -->` / `<!-- BGM：A-... -->` 提示與 frontmatter map entry 的 `portrait` / `bgm` 不一致 → WARN（非 ERROR，per §4.3）
- **v0.4 新增驗證**（per NEW_REQ_3 + master 第五輪細化）：
  - 若 `dialogue_keys[<KEY>].status = deleted` 但內文仍存在對應 `<!-- KEY: <KEY> -->` comment → parser **WARN**（非 ERROR）：「該 KEY status=deleted，建議從內文移除（漸進刪除友善 — 內文段落留存不阻擋 LOCKED）」
  - 寬鬆語意保留：A.0.2 採寬鬆解讀允許 deleted KEY 內文仍存在；本 WARN 僅作提示，不影響 build_repo_index ERROR 集計
  - 落地時機：A.0.10 patch 已完成 cross-ref validator 整合，本 WARN 規則由後續 patch round 或 Phase A.X 補實作（spec 端先定義）

### 11.1.3 全 repo KEY + alias unique 集合（DF-3，v0.2 — Map shape）

- parser 啟動時掃描所有 `08_dialogue_outputs/**/*.md`
- 建全 repo KEY 集合：`⋃ (map_key) ∪ ⋃ (entry.aliases[*])` for all dialogue files
- `status: deleted` entry 的 map key 與 aliases **仍計入** unique 集合（KEY 不重用原則）
- 任何新增 / 改名前先查集合；衝突 ERROR
- 建反向索引：`alias → 當前 KEY + 檔案路徑`（給「user 用舊 KEY 引用」走查路徑）

### 11.1.4 art_metadata block + A-\* prefix 識別（DF-4，v0.2 — 7 種 subtype + 不入 narrative `/status`）

- 識別 entity 類型 prefix `A-*` 加入 valid set
- 掃描 `10_art_assets/**/*.md` 目錄
- 解析 frontmatter `art_metadata` block：`asset_id` / `display_name` / `subtype`（v0.2 新）/ `owner`（v0.2 改自 `character`）/ `state_tags` / `aliases` / `created_at`（+ 選用 `renamed_at` / `deleted_at` / `dialogue_keys_ref`）
- **v0.2 subtype 驗證**（per D-044 + §5.1a）：
  - `subtype` 值必須在 `portrait / bg / cg / sfx / bgm / voice / ui` 7 種 allowed_values 內 → 不在 ERROR
  - 在 `reserved_subtypes`（icon / effect / video / shader）內 → ERROR + 提示「該 subtype 已預留但本輪不採」
- **v0.2 owner 驗證**（per §5.1b）：
  - `subtype: portrait` 的 `owner` 必對應既有 C-\* entity → 不存在 WARN「孤立立繪」
  - `subtype: voice` 的 `owner` 必對應既有 C-\* entity；`dialogue_keys_ref` 必填且對應既有 dialogue KEY（cross-check §4.2 map key + aliases） → 不存在 WARN
  - 其他 subtype 對應規則見 §5.1b
- **強制禁止欄位偵測**（§5.7）：`file_path` / `url` / `source_image` / `binary_data` / `base64_*` → ERROR
- 驗證 asset_id 全 repo unique（含 aliases，同 §11.1.3 機制延伸至 A-\*）
- **v0.2 完成度行為變更**（per D-045）：
  - A-\* 完成度計算（§5.6 獨立公式）仍由 parser 提供
  - **不納入** narrative `/status` expected entity manifest 比對（v0.1 此行為廢）
  - parser 提供獨立 API（建議 `get_asset_completeness_by_subtype()`）給前端 asset panel 用

### 11.1.5 內文 A-\* cross-reference 解析（DF-4，v0.2 — view-layer 提示）

- 解析下游台詞檔 / 任務包內文 `<!-- 立繪：A-... -->` / `<!-- 背景：A-... -->` / `<!-- BGM：A-... -->` / `<!-- SFX：A-... -->` 等 cross-reference HTML comment
- **v0.2 規則**（per §4.3 + D-037）：
  - 內文 art comment **僅 view-layer 提示**，非權威來源
  - 句級 A-\* 權威來源 = frontmatter `dialogue_keys[<KEY>].portrait/bgm/sfx`
  - 內文 art comment 與 frontmatter map entry 不一致 → WARN（非 ERROR）— 允許編輯期間暫時不同步
- 對照 frontmatter `depends_on` — 若內文引用 A-\* 但 `depends_on` 未列 → WARN「內文引用未宣告依賴」
- 引用歷史 alias（非當前 asset_id）→ WARN「建議改用當前 ID」

### 11.1.6 mode_tag / qa_type 擴充 enum 處理（DF-8）

- `mode_tag` valid set 加 `SINGLE_ITER`（基線 5 → 6 種）
- `qa_type` valid set 加 `RHYTHM` / `DRAMATIC_TENSION` / `CROSS_SCENE_CONTINUITY`（基線 5 → 8 種）
- `qa_type` set 變開放可擴充（屬 §11.1.8 registry 解析範圍）

### 11.1.7 entity_type_registry 讀取（DF-5）

- 啟動時讀 `<instance_root>/entity_type_registry.yaml`
- 不存在 → fallback Template `_design/registries/entity_type_registry.template.yaml` + WARN
- 載入 `core` + `user_extensions` 為 valid entity type set
- 對 frontmatter `entities` / `depends_on` 內每個 ID：
  - 取 prefix 比對 valid set → 不在 set 內 ERROR「未知 entity 類型」
  - 依 entry 的 `id_pattern` regex 驗證 ID 格式 → 不符 ERROR
- 對 user_extensions 驗證：
  - `type` 不可跟 core 重複（ERROR）
  - `type` prefix 不可在 `reserved_prefixes` 內（WARN）
  - `id_pattern` 為 valid regex（ERROR 否則）
  - `target_dir` 為 valid 相對路徑（WARN 若 dir 不存在）
- 偵測「現存 X-\* entity 但類型 X 已從 registry 移除」→ ERROR（防 silent drop）

### 11.1.8 qa_type_registry 讀取（DF-6）

- 啟動時讀 `<instance_root>/qa_type_registry.yaml`
- 不存在 → fallback Template + WARN
- 載入 `core` + `user_extensions` 為 valid qa_type set
- 對 QA 報告檔 frontmatter `qa_type` 驗證在 set 內
- 對 `user_extensions[*].template_path` 驗證對應檔案存在於 `09_quality_assurance/`（不存在 → ERROR）
- 對應 09_x 模板 frontmatter `qa_type` 值與 registry entry 對應（不對應 → WARN）

### 11.1.9 JSON export 結構化資料 API 提供（DF-7）

- parser 不直接負責 export，但提供「結構化資料」API 給 export skill（屬上下游 UD-3）使用
- API 形狀（建議，屬 ARCHITECTURE 範圍）：
  - `get_all_entities()` → list of entity records
  - `get_all_dialogue_lines()` → list of dialogue_line records（按 KEY 排序）
  - `get_all_art_metadata()` → list of art_metadata records
  - `get_manifest_snapshot()` → manifest 物件（含 registry snapshots）
- 對應 §9 JSON output schema 一對一映射

## 11.2 對 SPEC §5.4 既有 phase_log schema 描述的對齊（v0.2）

- SPEC §5.4 既有範例已含 `status` 三種值 → 本檔 §3.2 formalize 後可移除「P-012 暫定」標記
- SPEC §5.4 既有範例不含 `import_source` → 由 master 第四輪整合補入範例
- **v0.2 新增（per D-042）**：SPEC §5.4 範例補入 5 個新欄位（`entities_touched / iteration_count / iteration_note / base_dialogue / conflict_resolutions`）；補入 SINGLE_ITER lineage 範例（兩個 SINGLE_ITER entry，`base_dialogue` 形成 lineage）

## 11.3 對 SPEC §5.2.3 既有欄位定義表的對齊

- `mode_tag` 欄位描述更新值列（加 SINGLE_ITER）
- `qa_type` 欄位描述更新值列（加 3 種 + 標可擴充）
- 其他欄位描述不動
- **v0.2 注意**：SPEC §5.2.3 鎖定的 `source_dialogues` 不擴義 — SINGLE_ITER lineage 走獨立 `base_dialogue`（phase_log 欄位，非 frontmatter 下游欄位；per D-042 + C-09 解決）

## 11.4 給上下游 UD-2 引用的清單摘要（v0.2）

| 處理項 | 對應本檔節 | parser 行為類型 | v0.2 變更 |
|---|---|---|---|
| phase_log status / import_source | §3 / §11.1.1 | 解析 + 驗證 | — |
| **phase_log 5 新欄位（v0.2）** | **§3 / §11.1.1** | **解析 + 驗證 + cycle 偵測** | **D-042 新增** |
| dialogue_keys Map + 內文 KEY | §4 / §11.1.2 + §11.1.3 | 解析 + 全 repo unique + lifecycle metadata 驗證 | **list→Map shape（D-037）** |
| art_metadata + A-\* | §5 / §11.1.4 + §11.1.5 | 解析 + 強制禁止欄位偵測 + subtype 7 種驗證 | **subtype 5→7 種（D-044）** + **不入 narrative `/status`（D-045）** |
| mode_tag SINGLE_ITER | §6 / §11.1.6 | enum 擴值 | — |
| qa_type 3 種 + 可擴充 | §6 + §8 / §11.1.6 + §11.1.8 | enum 擴值 + registry 解析 | — |
| entity_type_registry | §7 / §11.1.7 | registry 解析 + entity ID 驗證 | A-\* `id_pattern` 7 種 subtype |
| qa_type_registry | §8 / §11.1.8 | registry 解析 + template_path 驗證 | — |
| JSON export API | §9 / §11.1.9 | 結構化資料 API | **dialogue_line record 對齊 Map shape** |
| Migration: 既有 27 模板 frontmatter | §10 / 無 parser 變動 | 27 份模板 frontmatter 結構零變動，parser 對既有檔解析行為不變 | 08_b dialogue_keys 改 Map 範例（屬上下游） |
| **Narrative vs Asset 完成度分離（v0.2）** | **§5.6 / §11.1.4** | **A-\* 不入 narrative `/status`；獨立 asset panel API** | **D-045 新增** |

---

# 12. 需 master 裁決問題清單（DF-11 — v0.2 語氣調整 per O-01）

## 12.0 本節性質

依 SPECIALIST_STARTER §3.2 + REVISED_WORK_ITEMS §7.3 DF-11 要求：「即使為空也明示」。本節列出本檔提案中需 master 第四輪整合裁決的議題（如有），與已 RESOLVED 的 P 條目對照。

**v0.2 語氣調整（per CODEX O-01 + master 第四輪整合）：**
- v0.1：「本檔提案無需 master 裁決議題」/「P-021~P-024 全 RESOLVED via 本檔」/「P-025~P-030 schema 容納由本檔保證」
- **v0.2 調整為：** 「本輪 patch 完成，無新增議題」/「P-021~P-024 RESOLVED via D-037~D-044（master 第四輪整合）」/「P-025~P-030 — 跨 spec 議題已由 master 在 §6.7 P0/P1 裁決中收斂；本檔提供 schema 級配合」

理由（per O-01）：DF v0.1 本身多處 partial supersede SPEC §5.1 / §5.2.4，且與 UD / UX 有 Contract A/C 衝突（CODEX 識出 C-01 ~ C-17 + O-01 ~ O-05），所以「RESOLVED」與「無需 master」的語氣應降為「資料格式初稿答案」+「待 / 已經 Contract A/C 跨 spec 裁決」。

## 12.1 結論：本輪 v0.2 patch 完成，無新增 master 裁決議題

**本檔 v0.2 patch 範圍對齊 DECISIONS_LOG §6.7 P0/P1 裁決（D-037 ~ D-046）；所有 patch 均為「master 第四輪整合已拍板，DF 落地」性質，不是「DF 提案待 master 裁決」。**

v0.2 patch 來源與對應：

| Patch | 對應 D | 來源 | 性質 |
|---|---|---|---|
| §4.2 dialogue_keys list → Map | D-037 | CODEX C-01 critical | master 已拍板，DF 落地 |
| §4.5 KEY lifecycle metadata（status/deleted_at/deprecated_reason） | D-037 | CODEX C-10 major | master 已拍板，DF 落地 |
| §3 phase_log 補 5 新欄位 | D-042 | CODEX C-07 / C-09 / O-04 | master 已拍板，DF 落地 |
| §5.1 A-\* subtype 7 種 | D-044 | CODEX C-13 major | master 已拍板，DF 落地 |
| §5.6 A-\* 不入 narrative `/status` | D-045 | CODEX C-14 major | master 已拍板，DF 落地 |
| §12 語氣調整 | O-01 | CODEX O-01 越界嫌疑 | master 識出後 DF 自修 |
| §9.5 dialogue_line record 對齊 Map | D-037 + D-039 | 由 §4.2 變動衍生 | DF 自我一致性對齊 |

**本輪 v0.2 patch 不再有「待 master 裁決」議題** — master 第四輪整合對話已在 §6.7 把 CODEX 識出的衝突全部收斂為 D-037 ~ D-046；本檔 v0.2 是該等裁決的 DF 端落地。

## 12.2 P-021 ~ P-026 RESOLVED 對照表（v0.2 — 對應 master §6.7.3）

REQUIREMENTS_LOCK §8.1 + DECISIONS_LOG §6.6.5 列出本輪交給資料格式 specialist 細化的 Pending 議題 P-021 ~ P-024；master 第四輪整合對話新解 P-025 / P-026：

| Pending ID | 議題 | RESOLVED via | 本檔節（v0.2） |
|---|---|---|---|
| **P-021** | A-\* entity registry / metadata 形狀 | **D-041 + D-044**（master 第四輪整合）+ DF §5 落地 | §5 / §5.1 / §5.1a / §5.2 / §5.3 |
| **P-022** | i18n KEY 機制 | **D-037**（master 第四輪整合）+ DF §4 落地 | §4 / §4.2 Map shape / §4.5 lifecycle metadata |
| **P-023** | entity registry / qa_type registry | DF Phase 3 §7+§8 + **D-043**（QA 8 份 + 09_e 必跑） | §7 / §8 |
| **P-024** | JSON 中介格式 | **D-039**（master 第四輪整合 — DF records[] 為權威）+ DF §9 落地 | §9 |
| **P-025** | phase_log 擴充 | **D-042**（master 第四輪整合）+ DF §3 落地 | §3 / §3.1 / §3.3a~e |
| **P-026** | LOCKED Save guard | **D-040**（master 第四輪整合 — UX 負責 Save flow） | 不在 DF 範圍（UX UD-15） |

**v0.2 改動摘要（per O-01）：**
- v0.1：把 P-021~P-024 寫成「RESOLVED via 本檔 DF-N」（過早宣稱 resolved）
- **v0.2：** 統一寫成「RESOLVED via D-037~D-044（master 第四輪整合）」+ 對應 DF 章節是「落地點」而非「答案來源」
- master 第四輪整合對話在 DECISIONS_LOG §6.7.3 已完整對照表 — 本表是 DF 端的引用副本

## 12.3 對其他 specialist 範圍 Pending 的影響（v0.2 — 對齊 master §6.7.3）

| Pending ID | 議題 | Owner | 本檔影響（v0.2） | 狀態 |
|---|---|---|---|---|
| **P-027** | /dialogue-write SINGLE_ITER 模式具體 algorithm | 上下游 UD-7 | 本檔 §6.1（mode_tag SINGLE_ITER）+ §3.3b/c/d（iteration_count/note/base_dialogue 欄位）提供 schema 級保證；具體 algorithm 不在本檔 | 仍 Pending — Phase A.0 後 v0.9+ 處理（per §6.7.3） |
| **P-028** | 手稿導入細節（markdown structure 解析 / 命名衝突 4 選項） | 上下游 UD-2 | 本檔 §3.3（import_source）+ §3.3e（conflict_resolutions 欄位）提供 schema 級保證；具體解析 algorithm 不在本檔 | 仍 Pending |
| **P-029** | 前端工具 UX 細節 | UX | 本檔 §4-§9 提供前端可消費的 schema；UX 細節不在本檔 | 仍 Pending |
| **P-030** | L3 export 觸發方式 | 上下游 UD-3 + UX | 本檔 §9（JSON schema）+ L3_EXPORT_PROMPT_SCHEMA.md 提供觸發 contract；具體前端 UI 不在本檔 | **RESOLVED via D-038**（A1 prompt + CC/CODEX）/ master §6.7.3 |

**本檔對所有 P-025 ~ P-030 議題提供 schema 級配合**；不變更其 Pending / RESOLVED 狀態（屬 master 範圍）。

P-027 ~ P-030 詳細狀態見 DECISIONS_LOG §6.7.3：「P-027 ~ P-030 仍 Pending：屬 UX 細節 / canon delta / glossary / multi-medium future，留待 Phase A.0 後 v0.9+ 處理」。

## 12.4 Master 第四輪整合 + 後續 CODEX tier 2 工作清單（v0.2）

下列項目不是「裁決議題」（user 不必拍板）— master 第四輪整合對話已在 §6.7 拍板完畢；這是後續落地工作的「機械式 checklist」：

| 工作項 | 落地點 | 對應本檔節 | 狀態 |
|---|---|---|---|
| SPEC §5.1 加 A-\* 為第 8 類 + 加副節「§5.1.x 可擴充 entity 類型機制」指向 entity_type_registry | SPEC §5.1 | §5 / §7 | master 第四輪整合落地 |
| SPEC §5.2.3 `mode_tag` 欄位描述加 SINGLE_ITER | SPEC §5.2.3 | §6.1 | master 第四輪整合落地 |
| SPEC §5.2.3 `qa_type` 欄位描述加 3 種 + 標可擴充 | SPEC §5.2.3 | §6.2 / §8 | master 第四輪整合落地 |
| SPEC §5.2.4 mode_tag enum 標記 partial supersede（5 → 6） | SPEC §5.2.4 | §6.3 | master 第四輪整合落地 |
| SPEC §5.2.4 qa_type enum 加副節「§5.2.4.x 可擴充機制」 | SPEC §5.2.4 | §8.8 | master 第四輪整合落地 |
| SPEC §5.4 phase_log schema 移除 `status` 的「P-012 暫定」標記 | SPEC §5.4 | §3.2 | master 第四輪整合落地 |
| SPEC §5.4 phase_log schema 補入 `import_source` + 5 個 v0.2 新欄位範例 | SPEC §5.4 | §3 全節 | master 第四輪整合落地（per D-042） |
| **SPEC §5.4 補入 SINGLE_ITER lineage 範例（`base_dialogue` 鏈條）** | SPEC §5.4 | §3.4 範例 | **v0.2 新增（per D-042 + C-09 解決）** |
| ARCHITECTURE 加「結構化資料 API」段（parser 提供給 export 用） | ARCHITECTURE | §11.1.9 | master 第四輪整合落地 |
| **ARCHITECTURE 加「asset panel 獨立 completeness API」段** | ARCHITECTURE | §11.1.4 v0.2 | **v0.2 新增（per D-045）** |
| TASKS A.0 parser 工作項加 §11.1.1 ~ §11.1.9 9 大類 + **v0.2 各 patch 對應** | TASKS A.0 | §11 | master 第四輪整合落地 |
| TASKS A.4 模板 frontmatter 統一補完任務加「08_b dialogue_keys **Map** 範例 + 07_a A-\* depends_on 範例」（屬上下游 UD-5） | TASKS A.4 | §10.1 | master 第四輪整合落地 |
| INTEGRATION_CONTRACTS v2 升級 — Contract A 更新為「本檔 v0.2 為真實介面」 | INTEGRATION_CONTRACTS | §0.3 | master 第四輪整合落地（v0.2 對齊） |
| promote P-021 ~ P-026 為 D-NNN（或標 supersedes 本檔）— 已在 DECISIONS_LOG §6.7.3 完成 | DECISIONS_LOG | §12.2 | **已完成（v0.2）** |
| 移除 DECISIONS_LOG 中 P-021 ~ P-026 的「Pending」標記 — 已在 DECISIONS_LOG §6.7.3 完成 | DECISIONS_LOG | §12.2 | **已完成（v0.2）** |
| CODEX tier 2 從本檔 §7.2 / §8.2 摘 2 份 registry Template YAML 寫實檔到 `_design/registries/`（含 §5.1a 的 subtype registry） | _design/registries/ | §7.2 / §8.2 / §5.1a | CODEX tier 2 處理 |
| **CODEX tier 2 摘 §5.1a subtype registry 進 entity_type_registry.template.yaml 的 A entry** | _design/registries/entity_type_registry.template.yaml | §5.1a | **v0.2 新增** |
| **UD 對齊：UD §11 dialogue_keys 寫法統一為 Map shape；UD §12 sub schema 補 portrait/bgm/sfx/status 欄位定義** | UPSTREAM_DOWNSTREAM_SPEC | §4.2 / §9.5 | master 派工給上下游 specialist patch round |
| **UD 對齊：UD §10.3 trust-level 限縮至上游 `/create-*`，不下游推 DIALOGUE_FINAL** | UPSTREAM_DOWNSTREAM_SPEC | §3.3（import_source） | master 派工給上下游 specialist patch round（per D-038 / C-08 解決） |
| **UX 對齊：F1 dashboard 補 asset panel 獨立顯示 A-\* completeness（不入 narrative）** | UX_SPEC §11 | §5.6 / §11.1.4 v0.2 | master 派工給 UX specialist patch round（per D-045） |

**總計：18 個落地工作項；全部屬 Master 整合 / CODEX tier 2 / 跨 specialist patch round 機械式操作；無需 user 拍板。**

## 12.5 若未來有議題升 master 的格式範本

（即使本輪為空，仍保留範本給未來 v0.3+ 使用）

```markdown
### 議題 X：<簡要名稱>

- **涉及 scope：** （影響哪些 SPEC / DECISIONS / 既有 D / P）
- **提案方向：** （資料格式 specialist 建議的最佳方案）
- **替代方案：** （其他 viable option，含 trade-off）
- **等待裁決原因：** （為何 specialist 無法獨立決定 — 動到 LOCKED 核心 / 跨 specialist 影響 / user value judgment）
- **建議裁決時點：** （Master 第五輪整合 / 後續輪）
```

**本輪為空，無範本實例。**

---

# 13. Cross-ref 總表 + 文件維護紀律

## 13.0 本節性質

本檔內外 cross-reference 的統籌總表，供：

- 上下游 specialist 第二輪（UD-1 ~ UD-12）引用
- UX specialist 第二輪（UX-1 ~ UX-17）引用
- Master 第四輪整合（主 SPEC / ARCHITECTURE / TASKS 對齊）
- 未來新 master 對話接手時的快速定位

加 §13.4 文件維護紀律段（短）。

## 13.1 DF-N ↔ D / P / REQUIREMENTS_LOCK / SPEC 對照表（v0.2 — 含 P0/P1 patch）

| DF | 本檔節 | 對應 D（v0.1 + v0.2） | 對應 P（RESOLVED） | REQUIREMENTS_LOCK 段 | 影響 SPEC 段 |
|---|---|---|---|---|---|
| DF-1 | §2 | D-018 | P-006 | §1.3 / §7 表第 1, 5, 6 列 | §3.1 / §5.1 |
| DF-2 | §3 | P-012 + D-031 + **D-042（v0.2 — 5 新欄位）** | P-025 | §4.4 路徑 1/2 | §5.4 |
| DF-3 | §4 | D-022 + **D-037（v0.2 — list→Map + lifecycle metadata）** | P-022 | §3.2 | §5.2（partial via D-022） |
| DF-4 | §5 | D-023 + D-041 + **D-044（v0.2 — subtype 7 種）** + **D-045（v0.2 — 不入 narrative `/status`）** | P-021 | §3.3 | §5.1（partial via D-023） |
| DF-5 | §7 | D-025 | P-023 | §3.1 | §5.1（+ 可擴充副節） |
| DF-6 | §8 | D-027 + D-043 | P-023 | §4.2 | §5.2.4（+ 可擴充副節） |
| DF-7 | §9 | D-024 + **D-039（v0.2 — manifest+records[] 為權威）** | P-024 | §3.4 | — |
| DF-8 | §6 | D-026 + D-028 | — | §4.1 / §4.3 | §5.2.4 |
| DF-9 | §10 | — | — | — | — |
| DF-10 | §11 | — | — | — | — |
| DF-11 | §12 | **O-01（v0.2 — 語氣調整）** | — | — | — |

## 13.2 DF-N → 下游 specialist 消費點（Contract A 出口）

| DF | 上下游消費點 | UX 消費點 |
|---|---|---|
| DF-1（formalize D-018） | 無新消費（純整理） | 無 |
| DF-2（phase_log 擴充） | **UD-10**（00_k / 00_i 配合）/ **UD-2**（手稿導入 trust-level 紀錄） | UX §11.7（多場景並行衝突） |
| DF-3（i18n KEY） | **UD-5**（08_b 模板 + `/dialogue-write` 加 KEY 生成步驟） | **UX-12**（前端 F7 編輯 + LOCKED 守門 — KEY 改名 UI） |
| DF-4（A-\* entity） | **UD-4**（A-\* 對應協議候選 00_q）/ **UD-5**（08_b + 07_a 加 A-\* 範例）/ **UD-12**（跨 entity cross-reference） | UX §11.4（搜尋 facet 加 A-\*）/ UX §11.1（看板加 A-\* 完成度） |
| DF-5（entity registry） | **UD-10**（/init-project 複製 Template）/ **UD-12**（registry refresh 機制） | UX §11.6（複製指令）/ UX §11.4（搜尋 facet 對新類型 dynamic） |
| DF-6（qa_type registry） | **UD-8**（00_p 協議內容）/ **UD-10**（/init-project 複製 Template） | UX-6（QA 報告閱讀體驗）/ UX §11.4（搜尋 facet 對 qa_type dynamic） |
| DF-7（JSON 中介格式） | **UD-3**（Layer 3 export skill 設計） | UX-3（/export-\* 檔案 layout）/ UX §11.1（看板加 export 入口按鈕） |
| DF-8（新 enum 值） | **UD-6**（09_g/h/i algorithm）/ **UD-7**（SINGLE_ITER algorithm） | UX-6（QA 報告閱讀 — 8 種 + 9_e） |
| DF-9 ~ DF-11 | 全 specialist 引用（統籌段） | 全 specialist 引用 |

## 13.3 DF-N → 主 SPEC / ARCHITECTURE / TASKS 整合落地點

對應 §12.4「Master 整合工作清單」中的具體落地點 — 完整表格見 §12.4。摘要：

| 主文件 | 改動段 | 對應 DF |
|---|---|---|
| SPEC §5.1 | 加 A-\* 為第 8 類 + 加可擴充副節 | DF-4 + DF-5 |
| SPEC §5.2.3 | `mode_tag` / `qa_type` 欄位描述更新值列 | DF-8 + DF-6 |
| SPEC §5.2.4 | mode_tag / qa_type enum partial supersede 標記 + 可擴充副節 | DF-6 + DF-8 |
| SPEC §5.4 | phase_log schema 移除 P-012 暫定 + 補 import_source 範例 | DF-2 |
| ARCHITECTURE | 結構化資料 API 段 | DF-7 + DF-10 |
| TASKS A.0 | parser 9 大類處理項 | DF-10 / §11 |
| TASKS A.4 | 模板 frontmatter 統一補完任務加 08_b / 07_a 範例 | DF-3 + DF-4 / §10 |
| INTEGRATION_CONTRACTS v2 | Contract A 更新真實介面 | 全 DF |
| DECISIONS_LOG | promote P-021 ~ P-024 為 D-NNN | DF-3 + DF-4 + DF-5 + DF-6 + DF-7 |
| `_design/registries/` 新增 | 2 份 Template YAML 寫實檔 | DF-5 + DF-6 / §7.2 + §8.2 |

## 13.4 文件維護紀律（v0.2）

- 本檔是「**資料格式 specialist 第二輪交付**」 — v0.1 初版 + v0.2 master 第四輪整合 P0/P1 patch
- 每個提案須能對應到 REQUIREMENTS_LOCK + DECISIONS_LOG §6.6 / §6.7 中的明確 D / P 條目（§13.1 對照表）
- 不擅自 supersede SPEC §5.1 / §5.2 核心；無法獨立決定者進 §12 升 master（v0.2 為空，§12.1 明示）
- 後續變更觸發 v0.3：(a) Phase A.0 實作期間發現 schema 落地問題；(b) P-027 ~ P-030 細化期間發現本檔遺漏；(c) 上下游 / UX specialist patch round 暴露本檔需配合的真實衝突
- 本檔 v0.1 交付後三輪流程：
  - **(a)** 上下游 + UX specialist 第二輪細化（消費本檔 schema 為 Contract A 出口；§13.2 對照）
  - **(b)** master 第四輪整合（落地 §12.4 工作清單 13 項）
  - **(c)** 升 INTEGRATION_CONTRACTS v2 + 整合進主 SPEC / ARCHITECTURE / TASKS
- 本檔 v0.1 是 P-021 ~ P-024 4 個 Pending 議題的 RESOLVED 來源（§12.2）；master 第四輪可 promote 為 D-NNN
- 後續變更觸發 v0.2：(a) 第二輪上下游 / UX 細化過程暴露真實衝突；(b) Master 第四輪整合期間發現本檔遺漏；(c) Phase A.0+ 實作期間發現 schema 落地問題
