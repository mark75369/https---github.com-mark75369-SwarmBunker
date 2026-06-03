狀態：DRAFT
版本：v1.0
最後更新：2026-05-22
適用範圍：Phase C 完成報告
優先級：高

# PHASE_C_COMPLETION_REPORT — Phase C 完成報告

# 0. 文件目的

本報告紀錄 Phase C Wave 11 的整體驗收結果，作為 Phase C 收尾、Milestone 3 達成宣告，以及下一輪 Phase D 啟動條件聲明的依據。

本報告使用 master 詞彙的 Phase C：下游台詞生產 pipeline。對照 TASKS v1.9，這一段落對應 TASKS §D.0-§D.7。後續 master 詞彙的 Phase D 指 9th master scope：view / export / iterate / diagnose / integrate 等後續能力。

本輪依 `_design/CODEX_C_FINAL_STARTER.md` v0.1 執行。CODEX 在 Template repo 內只做落地驗證、baseline 驗證與報告寫作；不在 Template repo 內跑真實 `/scene-task`、`/dialogue-write`、`/qa` 寫檔流程，不修改 LOCKED spec、registry、parser、protocol、既有模板或 skill。

本輪唯一寫入目標為本報告。既有 in-flight 變動包含 C.2 mode_tag enum patch、POST_LOCK_PENDING v0.13、C4 patch round 09_g/h/i 三模板與本 starter；本報告將其作為 Wave 11 驗收 evidence，不改動其內容。

# 1. 驗收摘要

- Wave 11 task 結果：**✓ PASS**
- 驗收日期：2026-05-22
- repo SHA：`0a87fe99dd6284e80a1faa9712f514e32b349716`
- 驗收 owner：CODEX implementer + verifier agent
- repo 性質：Template repo；不是 Instance
- 寫檔範圍：只覆寫本報告

| 維度 | 範圍 | 結果 |
|---|---|---|
| 維度 1 | 技術驗證：headers / paths / repo index / expected entities | ✓ PASS |
| 維度 2 | Wave 10 review consolidation：C.1 / C.2 / C.3 + C4 patch round | ✓ PASS |
| 維度 3 | Phase C 3 downstream skill 整體鏈 | ✓ PASS |
| 維度 4 | D-054 hybrid fallback 落地 + Phase C 啟動條件 | ✓ PASS |

Milestone 3 達成宣告：**✓ 達成**。Phase C 的下游 3 個 skill、3 個中文 wrapper、8 個 `/qa` 必跑模板與 D-054 hybrid fallback 已落地並通過 Template 端驗收。

補充說明：§6 端到端 3 skill 鏈測試保留 user 親跑 placeholder。CODEX 本輪不在 Template 內執行真實 `/scene-task`、`/dialogue-write`、`/qa` 寫檔，以避免污染 Template。user 親跑完成後，可依 NEW_REQ_14 使用 AI-assisted §6 補入機制，把 M3 testing 結果補入本報告。

# 2. 維度 1：技術驗證

| 檢查 | 本輪結果 | baseline / 判準 | 驗收 |
|---|---:|---|---|
| `check_headers.py` errors | 0 | 必須 0 | ✓ |
| `check_headers.py` warnings | 35 | 當前 baseline；本報告 header 採簡潔 v1.0，不新增特殊版本 WARN | ✓ |
| `check_paths.py` errors | 252 | C4 patch 後 baseline 252；本報告後 +0 | ✓ |
| `check_paths.py` warnings | 1 | 非阻塞；本輪未新增 ERROR | ✓ |
| `build_repo_index('.')` errors | 0 | 必須 0 | ✓ |
| `build_repo_index('.')` warnings | 71 | WARN allowed；無 ERROR | ✓ |
| `build_repo_index('.')` perf | 0.606s | < 5s | ✓ |
| `_design/expected_entities.yaml` | 存在；含 `scene_task` / `dialogue_write` / `qa` phase；repo index 0 ERROR | 可讀且被 repo index 流程承接 | ✓ |

執行命令：

- `python -X utf8 -B scripts/check_headers.py`
- `python -X utf8 -B scripts/check_paths.py`
- `build_repo_index('.')` 並篩 `result.issues` 中 `severity == "ERROR"`
- `Test-Path _design/expected_entities.yaml`

baseline 紀律：

- `check_paths.py` 以 exit code 1 回報既有 baseline ERROR，符合本輪預期；本輪判準是不增加。
- C4 patch round 前缺 09_g/h/i 時曾造成較高 baseline；三模板補建後目前為 252 ERROR。
- 本報告不修補 `check_paths.py` 舊債；NEW_REQ_9 / NEW_REQ_19 仍屬後續 cleanup queue。
- 本報告引用 Instance-only 路徑時使用 `<instance_root>/` 前綴，避免把 Template repo 內不存在的 runtime 產物誤列 active missing path。
- 本報告不新增 nested prompt fence；如需描述 starter fence 慣例，只以文字描述 `~~~`。

# 3. 維度 2：Wave 10 Review Consolidation

## 3.1 C.1 `/scene-task` Skill

判定：✓ PASS

| 驗收項 | 驗證結果 | 驗收 |
|---|---|---|
| 英文主檔存在 | `.claude/skills/scene-task/SKILL.md` 存在，含 YAML frontmatter 與中文 5 欄 header | ✓ |
| 版本 | `版本：v0.1` | ✓ |
| 中文 wrapper | `.claude/skills/場景任務包/SKILL.md` 存在，極簡指向英文主檔 | ✓ |
| 5 階段流程 | Stage 1-5 對齊 UD §2.3.1-§2.3.5：診斷、探索、收斂、執行、驗證 | ✓ |
| D-054 fallback | 含 `## D-054 hybrid 讀檔 fallback 規範`；per-scene file first、aggregate 06_a fallback、雙失敗即拒絕 | ✓ |
| 啟動前檢查 | 含 D-051 後 single marker、Bootstrap completed、上游 W/V/C/R/P/CH ≥ REVIEW check | ✓ |
| phase_log | entry 含 `scene_id`、`task_path`、`todo_count`、`read_source`、`status: completed` | ✓ |
| 寫檔目錄 | 嚴格限 `<instance_root>/07_scene_tasks/` + `.protocol_version.phase_log` runtime tracking | ✓ |
| D-050 / D-053 邊界 | 含 D-050 子裁決 1 + 子裁決 2 雙 block，並列 D-053 exception；本 skill 不在例外範圍 | ✓ |

結論：C.1 落地檔能從 `06_scene_index` 的 D-054 hybrid convention 讀取單場規格，輸出單場 task pack，並在 D.2.5 人類 REVIEW gate 前停止。

## 3.2 C.2 `/dialogue-write` Skill

判定：✓ PASS

| 驗收項 | 驗證結果 | 驗收 |
|---|---|---|
| 英文主檔存在 | `.claude/skills/dialogue-write/SKILL.md` 存在，含 YAML frontmatter 與中文 5 欄 header | ✓ |
| 版本 | `版本：v0.2`，Wave 11 inline patch 修正 mode_tag enum blocker | ✓ |
| 中文 wrapper | `.claude/skills/生成台詞/SKILL.md` 存在，極簡指向英文主檔 | ✓ |
| 6 階段流程 | Stage 1-6 對齊 UD §2.4.1-§2.4.7；含可選探索、試寫、破格、收斂、SINGLE_ITER、驗證 | ✓ |
| 4 模式 algorithm | 試寫、破格、收斂、SINGLE_ITER 對齊 UD §4.2 / §4.3 / §4.4 + REQUIREMENTS_LOCK §4.3 | ✓ |
| 輸入鎖定 | A 試寫預設、B `--experimental`、C `--converge`、D `--single-iter`；收斂要求 ≥2 trial path | ✓ |
| 啟動前檢查 | 含 D.2.5 gate：task pack `狀態=REVIEW` 且 `pipeline_state=TASK_REVIEW`；6 核心欄位缺則拒絕 | ✓ |
| mode_tag enum | 對齊 SPEC §5.2.4 + parser `VALID_MODE_TAGS`：`ORGANIZED` / `DRAFT_TRIAL` / `EXPERIMENTAL` / `CONVERGENCE` / `FINAL_CANDIDATE` / `SINGLE_ITER` | ✓ |
| 寫檔目錄 | 嚴格限 `<instance_root>/08_dialogue_outputs/` + `.protocol_version.phase_log` runtime tracking | ✓ |
| 邊界 | 不自動 D.3.5、不自動 `/qa`、不升 FINAL、不修改 task pack | ✓ |

補丁說明：C.2 starter v0.1 的自檢列舉曾保留 `FINAL` 且缺 `ORGANIZED`；本輪驗收以已 patched 的實際 skill v0.2、LOCKED SPEC §5.2.4 與 parser `VALID_MODE_TAGS` 為準。v0.2 已明示 `FINAL` 是文件狀態 enum，不是 `mode_tag`。

## 3.3 C.3 `/qa` Skill

判定：✓ PASS

| 驗收項 | 驗證結果 | 驗收 |
|---|---|---|
| 英文主檔存在 | `.claude/skills/qa/SKILL.md` 存在，含 YAML frontmatter 與中文 5 欄 header | ✓ |
| 版本 | `版本：v0.1` | ✓ |
| 中文 wrapper | `.claude/skills/檢查/SKILL.md` 存在，極簡指向英文主檔 | ✓ |
| 5 階段流程 | Stage 1-5 對齊 UD §2.5.1-§2.5.6 v0.3 | ✓ |
| 8 報告 algorithm | 09_a/b/c/d/f/g/h/i 全列入；對齊 UD §3.1-§3.9 | ✓ |
| 序列印出順序 | 09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i | ✓ |
| qa_decision | 8 份全 PASS 才 PASS；任一 FAIL 即 FAIL；ARBITRATE_REQUIRED 留給後續人類 09_e | ✓ |
| phase_log | `qa_report_paths` 明示 8 個路徑，不是 5；含 `qa_decision` | ✓ |
| 寫檔目錄 | 嚴格限 `<instance_root>/09_quality_assurance/` 8 報告 + `<instance_root>/08_dialogue_outputs/` frontmatter 兩欄更新 | ✓ |
| 邊界 | 不產 09_e、不擅升 FINAL、不修 dialogue body | ✓ |
| R8-INFO-06 | 明示 00_k v0.1 5 報告文字為 stale；本 skill 直接對齊 UD §2.5.3 v0.3 | ✓ |

結論：C.3 落地檔能以 D-043 8 報告為權威完成 QA 設計，不被 00_k v0.1 的 5 報告 stale wording 阻塞。

## 3.4 C4 Patch Round：09_g / 09_h / 09_i 模板

判定：✓ PASS

| 模板 | qa_type | UD 權威 | 主要驗收 | 結果 |
|---|---|---|---|---|
| `09_quality_assurance/09_g_節奏感檢查模板.md` | RHYTHM | UD §3.7 | header + YAML；5 層框架；句長 / 節奏 algorithm；通用 Template | ✓ |
| `09_quality_assurance/09_h_對話張力檢查模板.md` | DRAMATIC_TENSION | UD §3.8 | header + YAML；5 層框架；PUSH / YIELD / EXPOSE / COUNTER algorithm；通用 Template | ✓ |
| `09_quality_assurance/09_i_跨場一致性檢查模板.md` | CROSS_SCENE_CONTINUITY | UD §3.9 | header + YAML；5 層框架；跨場聲線 / 資訊 / 節奏 arc algorithm；通用 Template | ✓ |

3 份模板均使用 `entities: []`、`depends_on: []`、`weight: {}` 作為 Template 端預設，不含作品專屬內容。C4 patch round 已解除 C.3 `/qa` 的 8 模板 prerequisite 阻塞。

# 4. 維度 3：Phase C 3 Skill 整體鏈驗收

## 4.1 3 個英文 Skill

| Skill | 檔案 | 實際版本 | 主要驗收點 | 驗收 |
|---|---|---:|---|---|
| `/scene-task` | `.claude/skills/scene-task/SKILL.md` | v0.1 | D-054 fallback、5 階段、task pack、phase_log | ✓ |
| `/dialogue-write` | `.claude/skills/dialogue-write/SKILL.md` | v0.2 | 4 模式、D.2.5 gate、mode_tag enum patch、08 outputs | ✓ |
| `/qa` | `.claude/skills/qa/SKILL.md` | v0.1 | 8 報告、序列順序、qa_decision、09_e 邊界 | ✓ |

## 4.2 3 個中文 Wrapper

| Wrapper | 檔案 | 實際版本 | 驗收 |
|---|---|---:|---|
| `/場景任務包` | `.claude/skills/場景任務包/SKILL.md` | v0.1 | ✓ |
| `/生成台詞` | `.claude/skills/生成台詞/SKILL.md` | v0.1 | ✓ |
| `/檢查` | `.claude/skills/檢查/SKILL.md` | v0.1 | ✓ |

3 個中文 wrapper 均採極簡模式，指向英文主檔為權威，不建立第二套流程。合計 6 個 Phase C entrypoints：3 個英文 skill + 3 個中文 wrapper。

## 4.3 QA 模板落地狀態

| 類別 | 模板 | 狀態 |
|---|---|---|
| `/qa` 必跑既有 | 09_a / 09_b / 09_c / 09_d / 09_f | ✓ 存在 |
| final-gating 既有 | 09_e | ✓ 存在；不在 `/qa` 8 報告範圍 |
| C4 patch 新增 | 09_g / 09_h / 09_i | ✓ 存在 |

`_design/registries/qa_type_registry.template.yaml` 已含 8 種 `/qa` enum：AI_FLAVOR、VOICE_CONSISTENCY、FORBIDDEN_WORD、INFO_CONTROL、GENRE_DRIFT、RHYTHM、DRAMATIC_TENSION、CROSS_SCENE_CONTINUITY。09_e 不入 registry，符合 final-gating 邊界。

## 4.4 Pipeline 依賴鏈

| 順序 | Gate / Skill | 輸入狀態 | 輸出狀態 | 驗收 |
|---:|---|---|---|---|
| 1 | `/scene-task` | 上游 W/V/C/R/P/CH ≥ REVIEW | `TASK_DRAFT` task pack | ✓ |
| 2 | D.2.5 task review gate | task pack DRAFT | task pack REVIEW + `TASK_REVIEW` | user gate |
| 3 | `/dialogue-write` trial | `TASK_REVIEW` task pack | `DIALOGUE_TRIAL` outputs | ✓ |
| 4 | D.3.5 convergence gate | trial outputs | `DIALOGUE_CONVERGED` or explicit path B | user gate |
| 5 | `/qa` | converged output or path B trial | `QA_PASSED` / `QA_FAILED` | ✓ |
| 6 | human final-gating + 09_e | QA result | `DIALOGUE_FINAL` then `DIALOGUE_LOCKED` | user gate |

Pipeline state 覆蓋 9 狀態：SCENE_INDEXED、TASK_DRAFT、TASK_REVIEW、DIALOGUE_TRIAL、DIALOGUE_CONVERGED、QA_PASSED、QA_FAILED、DIALOGUE_FINAL、DIALOGUE_LOCKED。

結論：下游 pipeline 的 skill 實作與人類 gate 邊界完整；CODEX skill 不擅自越過 D.2.5、D.3.5、final-gating。

# 5. 維度 4：D-054 Hybrid Fallback 落地 + Phase C 啟動條件

## 5.1 D-054 hybrid fallback

判定：✓ PASS

| 驗收項 | 驗證結果 | 驗收 |
|---|---|---|
| D-054 段落 | `/scene-task` SKILL.md 含 `## D-054 hybrid 讀檔 fallback 規範` | ✓ |
| 兩階段 fallback | Phase 1 per-scene file first；Phase 2 aggregate 06_a fallback | ✓ |
| 拒絕條件 | per-scene 不存在且 aggregate row 不存在時拒絕，不擅自建場景 | ✓ |
| audit 欄位 | `read_source` 僅允許 `per-scene` 或 `aggregate`，寫入 phase_log | ✓ |
| 00_h escape hatch | `.claude/skills/create-detailed-outline/SKILL.md` v0.3 line 198 保留 local per-scene convention wording；自然承接 D-054 | ✓ |
| NEW_REQ_15 | POST_LOCK_PENDING v0.13 保留 D-054 未來 per-scene 拆檔 convention 迭代評估 | ✓ |

D-054 仍是 0 LOCKED spec supersede 的拍板：不改 D-050、00_h、TASKS、UD、SPEC，只要求 `/scene-task` 支援 per-scene → aggregate fallback。

## 5.2 Phase C 啟動條件

| 條件 | 目前狀態 | 說明 |
|---|---|---|
| W-rules / W-language / V ≥ REVIEW | ✓ 達成於 Phase A.10 / A.11 | Phase A completion 已宣告可進 Phase B |
| C-* / R-*-* / P / CH-* ≥ REVIEW | ✓ 達成於 Phase B B.5.5 / B.6.5 / B.8 | Phase B completion v1.2 已宣告 M2 達成 |
| 3 個下游 skill 全落地 | ✓ 達成 | `/scene-task`、`/dialogue-write`、`/qa` |
| 8 個 `/qa` 必跑模板齊全 | ✓ 達成 | 09_a/b/c/d/f/g/h/i |
| D-054 fallback | ✓ 達成 | `/scene-task` 已落地 |
| S-*-* ≥ REVIEW | §6 user M3 testing 範圍 | TASKS §D.7 端到端驗收條件，不由 Template 端本輪代跑 |

結論：Template 端 Phase C 啟動條件已滿足。S-*-* 真實 Instance gate 仍保留給 user 親跑 M3 testing。

# 6. 端到端測試（user 親跑步驟 — placeholder）

Phase C Wave 11 規定端到端 3 skill chain 測試屬 user 親跑性質。CODEX 本輪不在 Template repo 內跑真實寫檔流程，避免產生 runtime task pack、dialogue output、QA report 污染 Template。

M3 user-test 建議接續 Phase B testing Instance：

| 步驟 | Skill / Gate | 預期結果 |
|---:|---|---|
| 1 | 確認 Phase B Instance 內 W/V/C/R/P/CH/S ≥ REVIEW | 下游 prerequisites 滿足 |
| 2 | `/scene-task <scene_id>` | 寫 `<instance_root>/07_scene_tasks/CH<n>_S<m>_台詞任務包.md` |
| 3 | D.2.5 task review gate | 人類確認 task pack 後升 REVIEW + `TASK_REVIEW` |
| 4 | `/dialogue-write <task_input>` | 產 v01A/B/C trial outputs |
| 5 | D.3.5 convergence gate | 人類挑亮點；跑 `--converge` 產 v02，或明示 path B |
| 6 | `/qa <dialogue_path>` | 產 8 份 QA 報告，不產 09_e |
| 7 | `/status` | 確認 S-*、dialogue、QA 完成度與 `qa_decision` |
| 8 | 檢查 `.protocol_version.phase_log` | 包含 `task_path`、`dialogue_paths`、`target_dialogue`、`qa_report_paths` |

**user 親跑結果待補：** [user 跑完 M3 chain 後在本檔 §6 補入結果摘要]

NEW_REQ_14 AI-assisted §6 補入機制：

1. user 在 master 對話內明示拍板：「我已跑完 M3 chain；請補入 §6」。
2. agent 讀 Instance 的 `.protocol_version.phase_log`、git log、review_log、實際 runtime 檔案清單。
3. agent reconstruct §6 事實摘要：步驟、結果、發現議題、是否需 D-NNN / NEW_REQ。
4. agent 先列草稿與 evidence，等待 user 拍板 OK。
5. user OK 後，agent 才把 §6 placeholder 更新為實際 M3 testing 結果。

此流程沿用 D-052 的 AI-assisted / manual fallback 精神：user 做權威拍板，agent 只做 mechanical reconstruction 與報告落地。

# 7. Phase C 完成聲明

- 維度 1：✓ PASS
- 維度 2：✓ PASS
- 維度 3：✓ PASS
- 維度 4：✓ PASS
- §6 端到端測試：placeholder 等 user 親跑，依 starter 明示不阻 Wave 11 Template 端 completion

Phase C 完成判定：**✓ PASS**

Milestone 3 達成判定：**✓ 達成**

Phase C 的可交付範圍已完成：3 個下游 skill 與中文 wrapper 可被 skill discovery 讀取，8 個 `/qa` 必跑模板齊全，D-054 hybrid fallback 已在 `/scene-task` 內實作，Template 端 baseline 檢查維持。

# 8. 後續：Phase D 啟動條件聲明

Phase D 可由下一輪 master 接手啟動。此處 Phase D 指 9th master scope：`/view-*`、`/export-*`、`/iterate-*`、`/diagnose`、`/integrate` 與相關 cleanup。

| 條件 | 目前狀態 | 說明 |
|---|---|---|
| Phase C Template 端 completion | ✓ 達成 | 本報告 4 維度 PASS |
| 下游 3 skill 已落地 | ✓ 達成 | `/scene-task`、`/dialogue-write`、`/qa` |
| 3 中文 wrapper 已落地 | ✓ 達成 | `/場景任務包`、`/生成台詞`、`/檢查` |
| 8 個 QA 必跑模板 | ✓ 達成 | C4 patch round 補齊 09_g/h/i |
| D-054 hybrid fallback | ✓ 達成 | `/scene-task` 支援 per-scene → aggregate |
| M3 Instance end-to-end | 待 user 親跑 | §6 placeholder；不阻 Template 端 Milestone 3 宣告 |

9th master cleanup queue 建議優先序：

| 優先序 | 項目 | 狀態 |
|---:|---|---|
| 1 | R8-INFO-06：`00_protocol/00_k` v0.1 仍寫 5 報告；UD/TASKS/SKILL 已以 8 報告為權威 | DEFERRED；可於 9th cleanup 升 00_k v0.2 |
| 2 | NEW_REQ_19 R10-MI-01 / R10-MI-02 / R10-MI-03 stale cross-ref cascade | DEFERRED；適合 lint / mechanical cleanup |
| 3 | NEW_REQ_16 cross-ref consistency lint script | DEFERRED；可降低後續 cascade 成本 |
| 4 | AGENTS.md skill discovery table 仍列 Phase B+ skill 為 TBD | Observed out-of-scope doc residue；若 Codex App invocation readiness 要完全同步，建議 9th cleanup 更新 |
| 5 | check_paths baseline debt / NEW_REQ_9 | DEFERRED；不阻 Phase D，但封版前需重新評估 |

09_g/h/i 三模板原屬 TASKS §D.1a debt，但已由 C4 patch round 提前完成；POST_LOCK_PENDING v0.13 已明示這不是 NEW_REQ_19 原 scope，而是為避免 Milestone 3 阻塞而提前處理。

# 9. Cross-ref

- `_design/CODEX_C_FINAL_STARTER.md` v0.1
- `_design/TASKS.md` v1.9 §D.1a / §D.2 / §D.3 / §D.4 / §D.7
- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.2
- `_design/PHASE_A_COMPLETION_REPORT.md` v1.1
- `_design/CODEX_C1_STARTER.md` v0.1
- `_design/CODEX_C2_STARTER.md` v0.1
- `_design/CODEX_C3_STARTER.md` v0.1
- `_design/CODEX_C4_PATCH_STARTER.md` v0.1
- `.claude/skills/scene-task/SKILL.md` v0.1
- `.claude/skills/dialogue-write/SKILL.md` v0.2
- `.claude/skills/qa/SKILL.md` v0.1
- `.claude/skills/場景任務包/SKILL.md` v0.1
- `.claude/skills/生成台詞/SKILL.md` v0.1
- `.claude/skills/檢查/SKILL.md` v0.1
- `09_quality_assurance/09_a_ai味qa報告模板.md`
- `09_quality_assurance/09_b_角色聲線一致性檢查模板.md`
- `09_quality_assurance/09_c_禁用詞檢查報告模板.md`
- `09_quality_assurance/09_d_資訊控制檢查報告模板.md`
- `09_quality_assurance/09_e_定稿變更紀錄模板.md`
- `09_quality_assurance/09_f_類型偏移檢查模板.md`
- `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1
- `09_quality_assurance/09_h_對話張力檢查模板.md` v0.1
- `09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.1
- `00_protocol/00_k_台詞生產流程協議.md` v0.1
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3 / §2.4 / §2.5 / §3.1-§3.9 / §4
- `_design/SPEC.md` v1.2 §5.2.4 / §12.3 / §12.5 / §12.6 / §12.7
- `_design/ARCHITECTURE.md` v1.6 §6.1 / §6.2 / §6.3
- `_design/DECISIONS_LOG.md` v2.0 §6.7-§6.9 / §6.12.2 / §6.13.2 / §6.16.2 / §6.17.2
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1 / §4.2 / §4.3
- `_design/POST_LOCK_PENDING.md` v0.13 NEW_REQ_13 / NEW_REQ_14 / NEW_REQ_15 / NEW_REQ_19
- `_design/D054_DECISION_PACKAGE.md` v0.2
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1 R8-INFO-06
- `_design/expected_entities.yaml`
- `_design/registries/qa_type_registry.template.yaml`
- `scripts/parse_frontmatter.py` `VALID_MODE_TAGS`
