---
name: scene-task
description: "建立單場台詞任務包的 Phase C skill。依 00_k 階段 1 與 UD §2.3 跑診斷、探索、收斂、執行、驗證；支援 D-054 hybrid 讀檔 fallback：優先讀 per-scene 場景檔，不存在時 fallback aggregate 06_a row，寫入 07_scene_tasks 並記錄 read_source。"
---

狀態：DRAFT
版本：v0.2（STYLE_ANCHOR v0.1 implementation；D-055 拍板落地；§3.2 抽取來源表新增 W-style 行，對應 task pack §18.4 文風錨定子節；指紋來源 = 01_world/01_d_文風樣本與指紋.md；不擴大 D-050 寫檔邊界）
歷史紀錄：v0.1（2026-05-21 Phase C Wave 9 首實作；含 D-054 hybrid 讀檔 fallback）
最後更新：2026-05-28
適用範圍：Claude Code `/scene-task` skill runtime instructions
優先級：高

# /scene-task Skill

## 用途

Use this skill when the user triggers `/scene-task <scene_id>` to assemble a single-scene dialogue task pack for one existing scene entity `S-<ch>-<n>` in an already bootstrapped Instance repo.

This skill is the first downstream pipeline skill in Phase C. It converts the scene index baseline created by `/create-detailed-outline` into a concrete task pack under `07_scene_tasks/`, so `/dialogue-write` can later generate dialogue after the human D.2.5 REVIEW gate.

Runtime outputs may include:

- `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`
- `.protocol_version.phase_log`

The scene entity itself must already exist. This skill does not create new `S-*` scene entities; it creates only the task-pack artifact that raises the existing scene from indexed state toward task-pack readiness.

## 觸發語

- English trigger: `/scene-task <scene_id>`
- Chinese alias wrapper: `/場景任務包 <scene_id>`, via `.claude/skills/場景任務包/SKILL.md`

`scene_id` accepts exactly one scene argument in either form:

- `S-<ch>-<n>`, for example `S-01-03`
- `CH<n>_S<m>`, for example `CH01_S03`

Normalize both forms to canonical `S-<ch>-<n>` for entity and phase_log use, and to `CH<n>_S<m>` for task-pack filename use. Use two-digit zero padding for `CH` and `S` numbers unless the local Instance has an explicit different convention already present in `06_scene_index/`.

## 觸發協議

Primary authority:

- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3.1 to §2.3.5
- `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 1, used as pipeline context
- `_design/ARCHITECTURE.md` v1.6 §6.1

Required references:

- `_design/TASKS.md` v1.9 §D.2 and §D.2.5
- `_design/SPEC.md` v1.2 §5.1, §5.3, §12.3, §12.5
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.2, §2.3, §2.10.3
- `_design/ARCHITECTURE.md` v1.6 §3.2, §3.3, §3.3.0, §3.3.1, §3.3.2, §6.1
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050, §6.13.2 D-051, §6.16.2 D-053, §6.17.2 D-054
- `_design/POST_LOCK_PENDING.md` v0.12 NEW_REQ_13, NEW_REQ_15, NEW_REQ_19
- `_design/D054_DECISION_PACKAGE.md` v0.2
- `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode
- `07_scene_tasks/07_a_單場台詞任務包模板.md`
- `06_scene_index/06_a_場景索引模板.md`

Authority notes:

1. UD §2.3 is the authoritative behavior for the five internal sub-stages.
2. `00_k` v0.1 is DRAFT context. Its stale "5 QA reports" wording is R8-INFO-06 and must not be copied as authority. For QA count/order, defer to UD §2.5.3 v0.3 and the later `/qa` skill scope.
3. D-054 is authoritative for scene-index read behavior: per-scene file first, aggregate `06_a` fallback second.
4. D-047 dynamic issue loading is not used here. `/scene-task` is a data-assembly skill, not a user-facing issue-dialogue skill.

If chat instructions conflict with the files above, follow the stricter combined prerequisite. Write boundaries are controlled by D-050 and this SKILL.md, not by broader protocol examples.

## 啟動前檢查

Before Stage 1, verify all of the following. If any prerequisite fails, stop before Stage 1 and write nothing.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, and `09_quality_assurance/`.
2. **D-051 後 active single marker check:** no `.template_root` marker file exists at repo root.
3. `.protocol_version` exists.
4. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
5. `_design/expected_entities.yaml` exists.
6. Do not use the removed D-049 structural inference rule. Do not block merely because `_design/registries/*.template.yaml` exists while `.protocol_version` is absent; that second defense was superseded by D-051.

If `.template_root` is present, stop with:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: 偵測到 `.template_root` marker；此目錄仍被標識為 Template repo。
Where: repo root / .template_root
Why: /scene-task 只能在已 bootstrap 的 Instance repo 內建立任務包，不能污染 Template。
下一步: 若這是新 Instance，先完成 Template 轉 Instance 流程並移除 `.template_root`，再跑 /init-project。
```

### Scene and pipeline checks

1. Parse the user-provided `scene_id`. If it is not `S-<ch>-<n>` or `CH<n>_S<m>`, stop with `✗ 無法執行`.
2. `.protocol_version.phase_log` does not contain a completed `phase: scene-task` entry for the same canonical `scene_id`. If it exists, refuse and tell the user to use a future `/iterate-scene` path or delete/rebuild by explicit human decision.
3. No active or in-progress phase_log entry is currently writing the same `scene_id`, target task pack, or downstream artifact.
4. The target task pack path does not already exist. If it exists, stop before Stage 1 and ask for explicit overwrite or iteration instructions.
5. The target file, if present, is not `LOCKED`. If it is `LOCKED`, stop before writing and ask for explicit file-specific confirmation.

### Upstream entity REVIEW checks

Check all required upstream entities before proceeding:

1. `W-rules`, `V`, and `W-language` are at least `REVIEW`.
2. All `C-*` entities appearing in this scene are at least `REVIEW`.
3. All relevant `R-*-*` entities for character pairs in this scene are at least `REVIEW`; if no relationship applies, state that explicitly.
4. `P` is at least `REVIEW`.
5. The chapter entity `CH-<n>` for this scene is at least `REVIEW`.

If any upstream entity is below `REVIEW`, list it in the diagnostic report. Core prerequisite failures block Stage 1 unless the user explicitly invokes a waiver accepted by the local protocol. A waiver must be recorded in the preview and phase_log; it must not promote task-pack status or pipeline state.

### D-054 scene spec availability check

Run the D-054 hybrid read lookup before entering Stage 1:

1. Determine the canonical scene ID and filename prefix.
2. Locate the scene spec by the D-054 fallback sequence in `## D-054 hybrid 讀檔 fallback 規範`.
3. Proceed only if either a per-scene file exists or the aggregate `06_a` contains a matching row.
4. If both are absent, stop with `⏸ 條件未滿足` and tell the user to run `/create-detailed-outline` or check the scene ID spelling.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user and Stage 4 performs the final target re-check.

### Stage 1 - Diagnosis, per UD §2.3.1

Actions:

1. Parse and normalize `scene_id`.
2. Run the D-054 hybrid fallback lookup.
3. Read this scene's metadata:
   - scene name
   - chapter
   - location and time
   - appearing `C-*` characters
   - scene function, rhythm, text type, task-pack need, and risk markers if present
4. Check all upstream entity statuses:
   - `W-rules`
   - `V`
   - `W-language`
   - relevant `C-*`
   - relevant `R-*-*`
   - `P`
   - `CH-<n>`
5. Read `05_plot/05_d_資訊揭露表.md` and extract chapter-scoped candidates from `§各章節資訊狀態 §CH-<n>`:
   - must reveal
   - must not reveal
   - may only imply
6. Read `05_plot/05_e_伏筆與回收表.md` and extract chapter-scoped foreshadowing/payoff candidates from `§各章節伏筆狀態 §CH-<n>`.
7. Prepare or append a `phase: scene-task` in-progress entry only after prerequisites pass and Stage 1 actually starts. If the run aborts later, update the same entry to `status: aborted`.

Print a chat-only `診斷報告` containing:

- 場景元資訊
- 先決實體狀態, including warnings for anything below `REVIEW`
- 候選資訊揭露清單
- 候選伏筆與回收清單
- 候選任務包欄位草稿
- 讀檔來源: `per-scene` or `aggregate`
- D-054 fallback notes, including marker/file mismatch warnings

Do not write the task pack during Stage 1.

### Stage 2 - Exploration, per UD §2.3.2

Extract only scene-relevant slices from the approved upstream files.

| 來源 | 抽取內容 | 填入任務包欄位 |
|---|---|---|
| `W-rules` (`01_world/01_a_世界觀總覽.md`) | 本場需要的世界規則摘要 | `世界規則約束` |
| `W-language` (`01_world/01_b_世界語言規格.md`, `01_world/01_c_陣營與階級語言.md`) | 本場相關陣營 / 階級的語言層級摘要 | `語言層級` |
| `W-style` (`01_world/01_d_文風樣本與指紋.md`) | 本場出場角色的量化指紋 + 正例前 3 句 + 負例 + 跨層硬約束 | `§18.4 文風錨定` |
| `V` (`02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, `02_vocabulary/02_c_禁用詞與慎用詞表.md`) | 本場禁用詞 / 慎用詞 / 解禁詞 | `禁用詞與禁用句型` |
| `C-*` 聲線卡 | 出場角色聲線卡引用 + 偏移檢查重點 | `出場角色聲線卡引用` |
| `R-*-*` (`04_relationships/04_a_角色關係矩陣.md`, `04_relationships/04_b_關係變化時間線.md`) | 本場相關關係的當前狀態 + 稱呼規則 + 禁語 | `本場關係狀態` |
| `05_plot/05_b_章節結構模板.md` | 本章節節奏 high / mid / low | `章節節奏` and part of `風格要求` |
| `05_plot/05_c_角色弧線表.md` | 本場每個出場角色當前的弧線階段 | `角色弧線階段` |
| `05_plot/05_d_資訊揭露表.md` | 該章節該透露 / 禁止透露的清單 | `必須透露資訊` and `禁止透露資訊` |
| `05_plot/05_e_伏筆與回收表.md` | 本場潛伏的伏筆 / 回收任務 | `潛伏的伏筆` |
| 作品專屬 `00_protocol/00_b_反ai味檢查表.md` §6 | 高風險場景處理規則, only when this scene is high-risk | `§18.3 高風險場景處理` |

Exploration rules:

1. Keep extracted slices short and source-labeled.
2. Do not copy entire worldbuilding, character cards, relationships, or plot files into the task pack.
3. Do not invent unavailable material. Mark missing content as `TODO`.
4. Do not use D-047 issue registry loading. There is no dynamic issue conversation in this skill.
5. Do not write any file during Stage 2.

Print a chat-only extraction summary before moving to Stage 3.

### Stage 3 - Convergence, per UD §2.3.3

Assemble the extracted material into a task-pack draft following `07_scene_tasks/07_a_單場台詞任務包模板.md`.

The convergence preview must include:

1. Task-pack Markdown preview.
2. TODO field list.
3. Core field readiness:
   - 出場角色
   - 必須透露資訊
   - 禁止透露資訊
   - 出場角色聲線卡引用
   - 角色表層目標
   - 角色真實目標
4. Downstream impact notes: which missing fields would cause `/dialogue-write` or later QA to refuse or degrade.
5. D-054 `read_source` value that will be recorded.
6. Planned write list:
   - `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`
   - `.protocol_version.phase_log`

Ask the user:

```md
要補哪些 TODO？或是否接受帶 TODO 直接寫檔？
```

Allowed user responses:

- `通過`, `OK`, or `寫檔`: accept the current draft, including any TODO, and proceed to Stage 4.
- TODO content or correction: integrate the content, then reprint the convergence preview.
- `中止` or `取消`: stop without writing the task pack. If an in-progress phase_log entry already exists, mark it `status: aborted` with `abort_reason`.

Do not proceed to Stage 4 on implied approval.

### Stage 4 - Execution, per UD §2.3.4 and SPEC §12.5

Before writing:

1. Re-check target path existence, header status, and lock status.
2. Re-check that no completed same-scene `phase: scene-task` entry appeared after Stage 3.
3. Re-check write set: only the task pack and `.protocol_version.phase_log` may be written.
4. If the target file changed unexpectedly between Stage 3 and Stage 4, stop and ask for a decision.

Write the task pack to:

```text
07_scene_tasks/CH<n>_S<m>_台詞任務包.md
```

Use complete frontmatter:

```yaml
---
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：CH<n>_S<m> 台詞任務包
優先級：中

---
entities: [S-<ch>-<m>]
depends_on: [W-rules, V, W-language, <相關 C-*>, <相關 R-*-*>, P, CH-<n>]
weight: {S-<ch>-<m>: 1.0}
scene_id: S-<ch>-<m>
source_task: null
source_dialogue: null
source_dialogues: null
pipeline_state: TASK_DRAFT
mode_tag: null
qa_decision: null
qa_type: null
---
```

Task-pack body requirements:

1. Follow the `07_a` task-pack structure.
2. Include all SPEC §12.5 fields.
3. Include the full UD §2.10.3 list, including `本場使用的 00_a 模式`.
4. Keep missing content as `TODO`.
5. Do not promote `狀態` beyond `DRAFT`.
6. Do not promote `pipeline_state` beyond `TASK_DRAFT`.
7. Do not add real project-specific `.protocol_version` example values inside this SKILL.md.

Required task-pack field checklist, following SPEC §12.5 and UD §2.10.3 "19 大欄位" wording while preserving the actual listed items:

1. 場景 ID
2. 場景名稱
3. 出場角色
4. 地點與時間
5. 前情提要
6. 本場開始狀態
7. 本場結束狀態
8. 本場戲劇目的
9. 必須透露資訊
10. 禁止透露資訊
11. 潛伏的伏筆
12. 出場角色聲線卡引用
13. 本場關係狀態
14. 角色表層目標
15. 角色真實目標
16. 角色不能說出口的事
17. 台詞長度限制
18. 風格要求
19. 禁用詞與禁用句型
20. 本場使用的 00_a 模式

Core field validation:

| 核心欄位 | Source | Missing behavior |
|---|---|---|
| 出場角色 (`C-*` list) | D-054 scene source / `05_b` / `05_c` | Mark TODO and warn that `/dialogue-write` rejects if unresolved |
| 必須透露資訊 | `05_d` | Mark TODO and warn that information-control QA is blocked or degraded |
| 禁止透露資訊 | `05_d` | Mark TODO and warn that `/dialogue-write` rejects if unresolved |
| 出場角色聲線卡引用 | `03_characters/` | Mark TODO and warn that voice QA is blocked or degraded |
| 角色表層目標 | user-provided | Mark TODO and warn that `/dialogue-write` rejects if unresolved |
| 角色真實目標 | user-provided | Mark TODO and warn that `/dialogue-write` rejects if unresolved |

Write failure behavior:

1. Stop further writes immediately.
2. Roll back the partial task pack file if possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly what was written, rolled back, or requires manual inspection.

### Stage 5 - Verification, per UD §2.3.5

After Stage 4 writes succeed:

1. Automatically invoke `/status`.
2. Confirm that `S-<ch>-<m>` completion rises as expected for a task-pack artifact, typically from 20% to 35% when the indexed scene now has a task pack.
3. Update the same `.protocol_version.phase_log` entry to `status: completed`.
4. Print the written task path, TODO count, and `read_source`.
5. Print:

```md
下一步建議：D.2.5 task review gate（人類拍板任務包 -> REVIEW + pipeline_state -> TASK_REVIEW）-> /dialogue-write
```

6. Print these prohibitions:
   - Do not auto-trigger D.2.5 task review gate.
   - Do not auto-trigger `/dialogue-write`.
   - Do not auto-trigger `/qa`.

Stage 5 must not run downstream skills. It may only call `/status` for validation.

## D-054 hybrid 讀檔 fallback 規範

D-054 selects Hybrid: aggregate `06_a` remains the default, while future `/iterate-scene --split-to-file` may split selected scenes into per-scene files. This skill must support both without changing file organization.

When reading `scene_id S-<ch>-<n>`, use this sequence.

### Phase 1 - per-scene file first

1. Normalize scene ID to:
   - entity form: `S-<ch>-<n>`
   - filename prefix: `CH<n>_S<m>`
2. Read `06_scene_index/06_a_場景索引模板.md` only enough to locate:
   - the matching row
   - the scene name
   - an optional marker: `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->`
3. Compute the per-scene candidate path:
   - if marker exists, use the marker filename
   - otherwise derive `06_scene_index/CH<n>_S<m>_<scene_name>.md` from the row scene name
4. Check whether the per-scene file exists.
5. If it exists, read the whole per-scene file and set `read_source = "per-scene"`.
6. If it does not exist, proceed to Phase 2.

The initial `06_a` scan in this phase is a metadata lookup for filename resolution. It does not make the read source `aggregate` unless the skill actually falls back to the row content.

### Phase 2 - aggregate 06_a fallback

1. Read `06_scene_index/06_a_場景索引模板.md`.
2. Locate the row for canonical `S-<ch>-<n>` or equivalent `CH<n>_S<m>`.
3. If the row exists, read the row and immediately adjacent detail block if the local template stores scene detail below the table.
4. Set `read_source = "aggregate"`.
5. If the row has a `split-to-file` marker but the referenced per-scene file is missing, print `WARN`:
   - What: marker says the scene was split, but the target file is absent.
   - Where: `06_scene_index/06_a_場景索引模板.md` row marker and referenced path.
   - Why: downstream is falling back to aggregate row to avoid blocking a valid scene.
   - 下一步: inspect or restore the missing per-scene file before future scene iteration.

### Phase 3 - neither source exists

If neither a per-scene file nor an aggregate row exists, refuse:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: 場景 S-<ch>-<n> 找不到對應 spec。
Where: per-scene 檔不存在，且 06_scene_index/06_a_場景索引模板.md 內無對應 row。
Why: /create-detailed-outline 還沒跑、該場景尚未建立，或 scene_id 拼寫錯誤。
下一步: 先跑 /create-detailed-outline 建立 S-<ch>-<n>，或檢查 scene_id 拼寫後重跑 /scene-task。
```

### Read-source audit requirement

Record `read_source` in phase_log as exactly one of:

- `per-scene`
- `aggregate`

Do not record both. Do not record free-form explanations inside `read_source`; put warnings in the chat report.

### Future D-054 iteration tracking

This skill must not trigger split-to-file. Splitting belongs to future Phase D `/iterate-scene --split-to-file`.

If, during real Phase C/D usage, the user repeatedly splits scenes or reports that aggregate `06_a` is too large, report this as evidence for a future per-scene supersede decision (issue number was previously written as D-055; per DECISIONS_LOG §6.18.2 it is deferred to D-056 or the next unused number). Do not modify POST_LOCK_PENDING, D054_DECISION_PACKAGE, or DECISIONS_LOG from this skill.

Future iteration signals to mention in reports only:

- trigger A: user says they want all scenes to be per-scene, or aggregate `06_a` is too large to maintain.
- trigger B: after future `/iterate-scene --split-to-file` exists, the user splits 5 or more scenes.
- trigger C: multi-agent parallel scene work creates recurring conflict pressure.
- trigger D: real git diff or merge conflict friction repeatedly comes from aggregate `06_a`.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry only after all preflight prerequisites pass. At successful Stage 5 completion, update the same entry to completed.

Use concrete scene IDs only. Do not write wildcard IDs such as `S-*`, `S-<ch>-<n>`, or `CH-*` into runtime phase_log entries.

Completed entry shape:

```yaml
- phase: scene-task
  date: YYYY-MM-DD
  skill: /scene-task
  status: completed
  scene_id: S-<ch>-<m>
  task_path: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
  todo_count: <N>
  read_source: per-scene
  customizations: []
```

If aggregate fallback was used, set:

```yaml
  read_source: aggregate
```

If aborted after an in-progress entry exists, update the same entry:

```yaml
- phase: scene-task
  date: YYYY-MM-DD
  skill: /scene-task
  status: aborted
  scene_id: S-<ch>-<m>
  task_path: null
  todo_count: null
  read_source: per-scene
  abort_reason: <short reason>
  detail: <human-readable detail>
  customizations: []
```

Abort rules:

1. If prerequisites fail before Stage 1, write nothing.
2. If the user cancels in Stage 3 after an in-progress entry was recorded, mark it `aborted`.
3. If Stage 4 fails after a partial task pack write, roll back the file where possible and mark the entry `aborted`.
4. Do not count the task pack as created unless Stage 4 write and Stage 5 validation both succeed.

## 輸入

The user provides:

- `/scene-task <scene_id>`
- optional TODO content during Stage 3
- `通過`, `OK`, or `寫檔` to approve Stage 4
- `中止` or `取消` to stop

Scene ID parsing:

| User input | Canonical entity | Filename stem |
|---|---|---|
| `S-01-03` | `S-01-03` | `CH01_S03` |
| `CH01_S03` | `S-01-03` | `CH01_S03` |
| `S-1-3` | `S-01-03` | `CH01_S03` |
| `CH1_S3` | `S-01-03` | `CH01_S03` |

Reject ambiguous, branch, side, or multi-scene inputs unless the local scene index already defines a clear convention for them.

## 輸出

Runtime output includes:

- Stage 1 diagnostic report in chat.
- Stage 2 extraction summary in chat.
- Stage 3 convergence preview in chat.
- Stage 4 file write only after user approval.
- Stage 5 `/status` validation and next-step recommendation.

Runtime file outputs are limited to:

- `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`
- `.protocol_version.phase_log`

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `07_scene_tasks/CH<n>_S<m>_台詞任務包.md` | 主體；既有 `S-<ch>-<m>` 任務包寫檔位置 |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: scene-task` / `scene_id` / `task_path` / `todo_count` / `read_source` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/`, `_tools/frontend/`, `scripts/`, `_design/registries/`, existing `.claude/skills/` files | 任何寫入都屬 D-050 越界 |

## 邊界

The skill must not:

- modify LOCKED files without explicit file-specific confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, registry Template files, `_design/*.md`, or existing skill files
- modify existing Phase A / Phase B skills or wrappers
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scene index, dialogue, or QA reports
- create new `S-*` scene entities
- auto-trigger D.2.5 task review gate
- auto-trigger `/dialogue-write`
- auto-trigger `/qa`
- promote task pack `狀態` to `REVIEW` or beyond
- promote `pipeline_state` from `TASK_DRAFT`
- create new entity types, enum values, schemas, parser behavior, or registry behavior
- overwrite an existing same-scene task pack without explicit user confirmation
- write real project-specific `.protocol_version` values inside this `SKILL.md`
- patch `D054_DECISION_PACKAGE`, NEW_REQ_15, or future iteration tracking records

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**

- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**

- 本 skill 寫檔目錄嚴格限定為 `07_scene_tasks/` 一個目錄；任何超出範圍的寫入屬越界
- `.protocol_version.phase_log` 是 runtime tracking exception，只能記錄本 skill 的 `scene-task` entry，不得順手修其他 phase
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

## 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If a target file becomes `LOCKED` or changes unexpectedly between Stage 3 and Stage 4, stop before writing that file and ask for a decision.

If Stage 4 write fails:

1. Stop further writes.
2. Roll back the partial task pack file if possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly what was written, rolled back, or requires manual inspection.

If rollback is not possible, report the partial artifact path and tell the user to inspect it before retrying. Do not hide partial-write risk behind a success message.

## 錯誤呈現規則

Use these headings:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repository state or prerequisite problems.

Each error must include:

- `What`: what failed.
- `Where`: file, section, command, or stage.
- `Why`: why the skill cannot continue.
- `下一步`: one concrete action the user should take.

For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, enum keys, or raw YAML objects in user-facing errors.
