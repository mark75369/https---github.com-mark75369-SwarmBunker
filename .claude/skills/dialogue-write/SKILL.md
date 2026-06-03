---
name: dialogue-write
description: "Generate single-scene dialogue outputs from reviewed task packs. Use when the user triggers /dialogue-write with trial, experimental, convergence, or SINGLE_ITER mode. Requires the D.2.5 task review gate before writing, supports v01A/B/C, v01D, v02, and v01-iter outputs, and never auto-runs D.3.5 or /qa."
---

狀態：DRAFT
版本：v0.3（STYLE_ANCHOR v0.1 implementation；D-055 拍板落地；Stage 1 診斷報告新增「文風錨定狀態」項，對應 task pack §18.4；指紋來源 = 01_world/01_d_文風樣本與指紋.md；不擴大 D-050 寫檔邊界）
歷史紀錄：v0.2（Wave 11 抓 blocker 修補 — mode_tag locked set 從錯誤的 「DRAFT_TRIAL/EXPERIMENTAL/CONVERGENCE/FINAL_CANDIDATE/FINAL/SINGLE_ITER」 改為 SPEC §5.2.4 + parser VALID_MODE_TAGS 正確「ORGANIZED/DRAFT_TRIAL/EXPERIMENTAL/CONVERGENCE/FINAL_CANDIDATE/SINGLE_ITER」；FINAL 屬狀態 enum 不屬 mode_tag；ORGANIZED 屬 /scene-task 上游 task pack scope）
最後更新：2026-05-28
適用範圍：Claude Code `/dialogue-write` skill runtime instructions
優先級：高

# /dialogue-write Skill

## 用途

Use this skill when the user triggers `/dialogue-write` to generate dialogue files for one existing scene entity `S-<ch>-<n>` from an already reviewed single-scene task pack.

This is the second downstream Phase C skill. It reads a task pack created by `/scene-task`, verifies the D.2.5 human task review gate, then writes dialogue derivatives under `08_dialogue_outputs/`.

Runtime outputs may include:

- trial drafts: `v01A`, `v01B`, `v01C`
- experimental draft: `v01D`
- convergence draft: `v02`
- single-iteration draft: `v01-iter`
- `.protocol_version.phase_log` runtime tracking

This skill creates no new `S-*` entity. Dialogue files are derivatives for an existing scene. This skill does not create task packs, QA reports, final-gating records, parser behavior, schemas, or new mode enum values.

## 觸發語

English trigger:

- `/dialogue-write <task_path | scene_id>`
- `/dialogue-write <input> --experimental`
- `/dialogue-write <task_input> --converge <v01A_path> <v01B_path> [...]`
- `/dialogue-write <task_input> --single-iter`

Chinese alias wrapper:

- `/生成台詞 <input>`, via `.claude/skills/生成台詞/SKILL.md`

Accepted input modes are locked to these four shapes:

| Mode | User input | Output |
|---|---|---|
| Trial default | `/dialogue-write <task_path | scene_id>` or no args | `v01A`, `v01B`, `v01C` with `mode_tag: DRAFT_TRIAL` |
| Experimental | `/dialogue-write <input> --experimental` | `v01D` with `mode_tag: EXPERIMENTAL` |
| Convergence | `/dialogue-write <task_input> --converge <trial_path> <trial_path> [...]` | `v02` with `mode_tag: CONVERGENCE` |
| SINGLE_ITER | `/dialogue-write <input> --single-iter` | `v01-iter` with `mode_tag: SINGLE_ITER` |

Mode flags are mutually exclusive. If more than one of `--experimental`, `--converge`, and `--single-iter` appears, refuse with `✗ 無法執行`.

No-argument mode uses the latest completed `/scene-task` entry in `.protocol_version.phase_log`. If no unambiguous previous task pack can be found, refuse and ask the user to provide a task pack path or scene ID.

## 觸發協議

Primary authority:

- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.4 and §4
- `_design/TASKS.md` v1.9 §D.3, with §D.2.5 and §D.3.5 dependencies
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.3 for `SINGLE_ITER`

Protocol context:

- `00_protocol/00_k_台詞生產流程協議.md` v0.1 stage 2
- `00_protocol/00_a_台詞生產協議.md` §3.5, §3.6, §3.7, §3.8

Required references:

- `_design/SPEC.md` v1.2 §5.2, §5.4, §12.3, §12.6
- `_design/ARCHITECTURE.md` v1.6 §3.3, §3.3.1, §3.3.2, §6.2
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050, §6.13.2 D-051, §6.16.2 D-053, §6.17.2 D-054
- `_design/POST_LOCK_PENDING.md` v0.12 NEW_REQ_12, NEW_REQ_13, NEW_REQ_19
- `.claude/skills/scene-task/SKILL.md` v0.1
- `.claude/skills/init-project/SKILL.md` v0.3
- `.claude/skills/create-character/SKILL.md`, `.claude/skills/create-relationship/SKILL.md`, `.claude/skills/create-outline/SKILL.md`, `.claude/skills/create-detailed-outline/SKILL.md` for D-050 boundary block style
- `07_scene_tasks/07_a_單場台詞任務包模板.md`
- live `08_b` template: `08_dialogue_outputs/08_b_生成台詞檔案模板.md`

Authority notes:

1. UD §2.4 and §4 are authoritative for `/dialogue-write` behavior.
2. `00_k` v0.1 is context. Its stale QA-count wording is R8-INFO-06 and must not be copied as current `/qa` authority.
3. The live `08_b` template is body-layout context. For frontmatter and downstream fields, use SPEC §5.2 and UD §2.4/§4.
4. D-047 dynamic issue loading is not used here. `/dialogue-write` reads a task pack and writes dialogue.
5. D-054 scene-index hybrid read behavior belongs to `/scene-task`; this skill reads task packs directly.
6. Write boundaries are controlled by D-050 and this SKILL.md, not by broader protocol examples.

## 啟動前檢查

Before Stage 1, verify all prerequisites below. If any prerequisite fails, stop before Stage 1 and write nothing.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `07_scene_tasks/`, `08_dialogue_outputs/`, and `09_quality_assurance/`.
2. **D-051 後 active single marker check:** no `.template_root` marker file exists at repo root.
3. `.protocol_version` exists.
4. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
5. `_design/expected_entities.yaml` exists.
6. Do not use the removed D-049 structural inference rule. Do not block only because `_design/registries/*.template.yaml` exists.

If `.template_root` is present, stop with:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: 偵測到 `.template_root` marker；此目錄仍被標識為 Template repo。
Where: repo root / .template_root
Why: /dialogue-write 只能在已 bootstrap 的 Instance repo 寫台詞，不能污染 Template。
下一步: 若這是新 Instance，先完成 Template 轉 Instance 流程並移除 `.template_root`，再跑 /init-project。
```

### Input and mode checks

1. Parse user input into exactly one of the four locked modes.
2. Reject unknown flags, multiple mode flags, multiple task inputs, or ambiguous scene IDs.
3. Resolve the task pack:
   - task path input: use that path after validating it is under `07_scene_tasks/`
   - scene ID input: locate the matching `07_scene_tasks/CH<n>_S<m>_台詞任務包.md` or matching latest phase_log task path
   - no args: use the latest completed `/scene-task` phase_log entry with a concrete task path
4. For `--converge`, require one task input plus at least two trial paths, and verify every path exists before entering Stage 1.
5. For `--single-iter`, require a resolvable task pack and the same core field checks as trial mode.

### Task pack review gate

The task pack must satisfy both conditions:

- Chinese header `狀態: REVIEW`
- YAML `pipeline_state: TASK_REVIEW`

If either is missing or mismatched, refuse with `⏸ 條件未滿足` and tell the user that D.2.5 task review gate must be completed first. Do not promote the task pack automatically.

For this C.2 runtime, `FINAL` or `LOCKED` task packs do not authorize bypassing the D.2.5 evidence check. If the local controller wants to permit a finalized task pack, require explicit file-specific confirmation and still do not modify the task pack.

### Core field checks

The six core task-pack fields must have substantive content:

- 出場角色
- 必須透露資訊
- 禁止透露資訊
- 出場角色聲線卡引用
- 角色表層目標
- 角色真實目標

Treat a field as missing if it is absent, blank, only `TODO`, only an HTML TODO comment, `待補`, `？`, or equivalent placeholder. Any missing core field refuses execution.

Non-core TODO fields do not block execution. List them in the diagnostic report and record them in phase_log as `incomplete_fields`.

### Upstream entity checks

From the task pack `depends_on` list and body references, verify related upstream entities are at least `REVIEW`:

- relevant `C-*` voice cards
- relevant `R-*-*` relationships
- relevant plot or chapter entities listed by the task pack
- any A-* art asset references if the task pack requires portraits, BGM, SFX, CG, or UI cues

If any prerequisite entity is below `REVIEW`, refuse unless the user explicitly provides an accepted waiver. A waiver must be recorded as `prereq_waived: true` with a short reason in the preview and phase_log. A waiver must not promote any entity or task pack.

### Target write checks

Before writing any dialogue file:

1. Derive concrete target paths under `08_dialogue_outputs/`.
2. Verify no target path already exists. If it exists, stop and ask for explicit overwrite or iteration instructions.
3. If a target exists and is `LOCKED`, stop and ask for a file-specific decision.
4. Verify the write set contains only `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v*.md` and `.protocol_version.phase_log`.

## 流程

Run six stages. Stage 3, Stage 4, Stage 5, and Stage 5a are mutually exclusive execution branches after Stage 1 and optional Stage 2.

Do not write files before showing the planned write list and receiving explicit user approval (`通過`, `OK`, or `寫檔`). Do not treat silence or discussion as approval.

### Stage 1 - Diagnosis, per UD §2.4.2

Actions:

1. Parse the input form and mode.
2. Resolve the task pack path from user input, scene ID, or the latest `/scene-task` phase_log entry.
3. Read the task pack.
4. Verify `狀態: REVIEW` and `pipeline_state: TASK_REVIEW`.
5. Verify the six core fields.
6. Verify `depends_on` upstream entity status and any A-* references.
7. In convergence mode, read each provided trial path enough to validate:
   - file exists
   - same `scene_id`
   - `pipeline_state: DIALOGUE_TRIAL`
   - `mode_tag` is `DRAFT_TRIAL` or `EXPERIMENTAL`
8. List all non-core TODO fields.
9. Derive concrete output filenames and planned phase_log shape.

Print a chat-only `診斷報告` containing:

- mode
- task pack path
- scene ID
- task-pack review-gate result
- six core field readiness
- non-core TODO list
- upstream entity status list
- 文風錨定狀態（task pack §18.4 是否齊全；指紋是否覆蓋本場出場角色；如缺漏標 WARN 但不 block 執行）
- planned write targets
- warnings, waivers, or experimental-source notes

Stop on any blocking issue. Do not write during Stage 1.

### Stage 2 - Exploration, optional, per UD §2.4.3

Run only when the user explicitly asks to run exploration.

Actions:

1. Generate one or two short exploratory voice fragments.
2. Mark them clearly as exploration only.
3. Do not write files.
4. Ask the user which direction is closest to the scene goal.
5. Carry the selected direction into the chosen execution branch.

Exploration must not change the task pack, character cards, reveal table, relationship files, or protocol files.

### Stage 3 - Trial Writing, default, per UD §2.4.4 and §4.2

Run when no mode flag is provided.

Generate exactly three default trial versions unless the task pack explicitly requests additional non-experimental directions:

| Version | Direction | Sentence length | Subtext density | Attack/defense | Emotion exposure |
|---|---|---|---|---|---|
| v01A | 克制、短句、強潛台詞 | short | high | medium | low |
| v01B | 攻防更強、衝突更尖 | medium | medium | high | medium |
| v01C | 情緒更重、但避免直說 | medium to long | medium to high | medium | medium to high |

Each default trial file uses:

- `狀態: DRAFT`
- `pipeline_state: DIALOGUE_TRIAL`
- `mode_tag: DRAFT_TRIAL`
- `source_dialogue: null`
- `source_dialogues: null`
- `qa_decision: null`
- `qa_type: null`

Before writing, print a preview summary and planned write list:

- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01B.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01C.md`
- any extra DRAFT_TRIAL directions requested by the task pack
- `.protocol_version.phase_log`

Ask for explicit approval. After approval, write the files and proceed to Stage 6.

### Stage 4 - Experimental, optional, per UD §2.4.5 and §4.4

Run only when the user provides `--experimental` or clearly says to run 破格.

Generate one experimental version:

- output suffix: `v01D`
- `狀態: DRAFT`
- `pipeline_state: DIALOGUE_TRIAL`
- `mode_tag: EXPERIMENTAL`
- not mixed into v01A/v01B/v01C

The file must contain these body sections when applicable:

- `## 破格方向`
- `## 版本內容`
- `## 可能有效的亮點`
- `## 不可直接使用的原因`
- `## 若要收斂，建議保留什麼`

Experimental mode may loosen safe style, but it must not violate locked canon, reveal forbidden information, change timelines, or ignore task-pack prohibitions.

Before writing, print a preview summary and planned write list:

- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01D.md`
- `.protocol_version.phase_log`

Ask for explicit approval. After approval, write the file and proceed to Stage 6.

### Stage 5 - Convergence, optional, per UD §2.4.6 and §4.3

Run only when the user provides `--converge`.

Convergence requirements:

1. One task-pack input is present.
2. Two or more existing trial paths are present.
3. Every trial path exists.
4. Every trial has the same `scene_id` as the task pack.
5. Every trial has `pipeline_state: DIALOGUE_TRIAL`.
6. Every trial has `mode_tag: DRAFT_TRIAL` or `EXPERIMENTAL`.
7. Experimental sources require an explicit warning in the preview.

Convergence mode must not re-run trial writing. It integrates provided trial files into one `v02` file.

Convergence algorithm:

1. List each trial's retained-highlight section.
2. Identify common scene skeleton beats across trials.
3. Place user-selected highlights into the skeleton.
4. Ask for user decision on conflicting same-position highlights.
5. Fill missing beats only from the task pack and confirmed voice constraints.
6. Smooth rhythm without flattening irregular but effective lines.
7. Warn if a retained line violates type, voice, or information-control rules.

The output file uses:

- suffix: `v02`
- `狀態: REVIEW`
- `pipeline_state: DIALOGUE_CONVERGED`
- `mode_tag: CONVERGENCE`
- `source_dialogue: null`
- `source_dialogues: [<trial paths>]`

Before writing, print the convergence preview and planned write list:

- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v02.md`
- `.protocol_version.phase_log`

Ask for explicit approval. After approval, write the file and proceed to Stage 6.

### Stage 5a - SINGLE_ITER, optional, per REQUIREMENTS_LOCK §4.3

Run only when the user provides `--single-iter`.

SINGLE_ITER is for one-version iteration inside `/dialogue-write`. It does not create a new `/iterate-dialogue` skill.

This C.2 implementation uses the task-pack input form from the command:

- `/dialogue-write <task_path | scene_id> --single-iter`
- no-arg fallback to latest `/scene-task` is allowed only when unambiguous

SINGLE_ITER process:

1. Diagnose the same D.2.5 task-pack gate and six core fields.
2. Generate one `v01-iter` version from the reviewed task pack.
3. Show the version preview and ask the user for one of:
   - approve write
   - continue chat iteration with concrete changes
   - cancel
4. If the user continues iteration, keep changes in chat memory until approval.
5. On approval, write one file.

The output file uses:

- suffix: `v01-iter`
- `狀態: DRAFT`
- `pipeline_state: DIALOGUE_TRIAL`
- `mode_tag: SINGLE_ITER`
- `source_dialogue: null`
- `source_dialogues: null`
- `qa_decision: null`
- `qa_type: null`

Lineage is recorded in phase_log:

- first iteration: `base_dialogue: null`, `iteration_count: 1`
- later same-scene iteration, if the user provides a prior iter path as context: `base_dialogue: <prior path>`, increment `iteration_count`

Do not write `base_dialogue` into dialogue frontmatter. `source_dialogues` remains locked to `--converge`.

Before writing, print a preview summary and planned write list:

- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01-iter.md`
- `.protocol_version.phase_log`

Ask for explicit approval. After approval, write the file and proceed to Stage 6.

### Stage 6 - Verification, per UD §2.4.7

After the execution branch writes succeed:

1. Automatically invoke `/status`.
2. Confirm the scene completion target:
   - trial or experimental: `S-<n>-<m>` should rise toward 60%
   - convergence: `S-<n>-<m>` should rise toward 75%
   - SINGLE_ITER: `S-<n>-<m>` should remain or rise toward 60% until QA
3. Append or update one `.protocol_version.phase_log` entry with `status: completed`.
4. Print written paths.
5. Print mode-specific next-step advice.
6. Print the prohibition that this skill does not auto-trigger D.3.5 gate or `/qa`.

Next-step advice by `mode_tag`:

| mode_tag | Next-step advice |
|---|---|
| `DRAFT_TRIAL` | 人類挑亮點 + run `/dialogue-write <task_input> --converge <trial paths>` for D.3.5 path A; path B exception is direct `/qa` by explicit user order |
| `EXPERIMENTAL` | 保留為實驗版本；不進 v01A/B/C；可獨立跑 `/qa` 或丟棄 |
| `CONVERGENCE` | 人類確認後跑 `/qa <v02_path>` |
| `SINGLE_ITER` | user 跟 agent 迴圈改完後跑 `/qa <v01-iter_path>` |

## 4 模式詳細 algorithm

### Trial algorithm - v01A/v01B/v01C

1. Use task-pack constraints as hard input.
2. Apply `00_a` §3.6 trial mode and SPEC §12.6 directions.
3. Generate v01A first, then v01B, then v01C.
4. Keep versions comparable: the same scene beats should appear in roughly corresponding order unless the task pack requires otherwise.
5. Assign or preserve `dialogue_keys` according to the local schema when the Instance supports sentence keys.
6. Do not merge the three versions into one file unless the local output convention explicitly requires one combined draft. Default is one file per version.
7. Do not label any trial version `REVIEW`, `FINAL`, or `LOCKED`.

Extra task-pack directions such as poetic, colloquial, or black-humor variants are still `mode_tag: DRAFT_TRIAL`. Experimental mode is the only path that writes `mode_tag: EXPERIMENTAL`.

### Experimental algorithm - v01D

1. Use task-pack constraints as hard input.
2. Generate one deliberate style-risk version.
3. Mark risks clearly in the file body.
4. Do not alter plot facts, locked voice facts, relationship timeline, or information reveal order.
5. Do not write v01D into the normal v01A/v01B/v01C group.
6. If the user later wants to use it in convergence, require explicit trial path inclusion.

### Convergence algorithm - v02

1. Require at least two provided trial paths.
2. Validate same scene and valid trial states.
3. Treat user-highlighted lines as inputs, not automatic approvals.
4. Preserve effective irregularities unless they violate locked constraints.
5. Write `source_dialogues` as the complete provided trial-path list.
6. Write one v02 file only after approval.
7. Mark the v02 file `狀態: REVIEW`, `pipeline_state: DIALOGUE_CONVERGED`, and `mode_tag: CONVERGENCE`.

### SINGLE_ITER algorithm - v01-iter

1. Use the reviewed task pack as the input anchor.
2. Generate one version and let the user iterate in chat.
3. Do not produce v01A/v01B/v01C in this mode.
4. Do not run D.3.5 convergence gate in this mode.
5. Write one `v01-iter` file only after approval.
6. Mark the output `狀態: DRAFT`, `pipeline_state: DIALOGUE_TRIAL`, and `mode_tag: SINGLE_ITER`.
7. Record `iteration_count`, `iteration_note`, and `base_dialogue` in phase_log when available.

### Cross-mode state table

| Mode | Output suffix | 狀態 | pipeline_state | mode_tag | source_dialogues |
|---|---|---|---|---|---|
| Trial | `v01A/B/C` | DRAFT | DIALOGUE_TRIAL | DRAFT_TRIAL | null |
| Experimental | `v01D` | DRAFT | DIALOGUE_TRIAL | EXPERIMENTAL | null |
| Convergence | `v02` | REVIEW | DIALOGUE_CONVERGED | CONVERGENCE | trial path list |
| SINGLE_ITER | `v01-iter` | DRAFT | DIALOGUE_TRIAL | SINGLE_ITER | null |

Mode-tag discipline:

- Current locked set referenced by SPEC §5.2.4 + parser VALID_MODE_TAGS: `ORGANIZED`, `DRAFT_TRIAL`, `EXPERIMENTAL`, `CONVERGENCE`, `FINAL_CANDIDATE`, `SINGLE_ITER` (6 種 enum; D-027 新增 SINGLE_ITER).
- This skill may write only `DRAFT_TRIAL`, `EXPERIMENTAL`, `CONVERGENCE`, and `SINGLE_ITER` (4 of the 6).
- `ORGANIZED` is reserved for `/scene-task` task pack outputs (upstream); this skill must not write `ORGANIZED`.
- `FINAL_CANDIDATE` is the downstream human/QA lifecycle value (after /qa PASS + human final-gating); this skill must not write it.
- 狀態 `FINAL` 屬文件 狀態 enum (DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED) not mode_tag; do not confuse the two dimensions.
- Do not add new mode_tag values.

## 輸入鎖定（O6 + M8 contract）

`/dialogue-write` accepts only the following input shapes.

### A. 試寫模式（預設）

Accepted:

1. Full task-pack path: `/dialogue-write 07_scene_tasks/CH01_S03_台詞任務包.md`
2. Scene ID: `/dialogue-write S-01-03`
3. No args: use the previous `/scene-task` task pack from phase_log

Result:

- write v01A/v01B/v01C
- `pipeline_state: DIALOGUE_TRIAL`
- `mode_tag: DRAFT_TRIAL`

### B. 破格模式

Accepted:

- `/dialogue-write <input> --experimental`

Result:

- write v01D
- `pipeline_state: DIALOGUE_TRIAL`
- `mode_tag: EXPERIMENTAL`

### C. 收斂模式（M8 + #7 clarification）

Accepted:

- `/dialogue-write <task_input> --converge <v01A_path> <v01B_path> [...]`

Rules:

- requires one task-pack input
- requires at least two existing trial paths
- does not run trial writing again
- must cite existing trial files as material
- refuses if the user provides only a task pack and no trial paths

Refusal text for missing trials:

```md
## ✗ 無法執行 / Cannot Proceed

What: `--converge` 模式沒有收到至少 2 個 trial 路徑。
Where: /dialogue-write command arguments
Why: 收斂模式必須引用既有 trial 版本，不重新試寫。
下一步: 請先跑試寫模式產 trial 版本，或提供既有 trial 路徑後重跑。
```

### D. SINGLE_ITER 模式

Accepted:

- `/dialogue-write <input> --single-iter`

Rules:

- writes one `v01-iter`
- user and agent may loop in chat before write approval
- does not run convergence
- after user approval, may go directly to `/qa`

## TODO 拒絕條件量化（O5）

Refuse when any core task-pack field is missing:

| Core field | Missing examples |
|---|---|
| 出場角色 | absent, blank, TODO, 待補, only a placeholder |
| 必須透露資訊 | absent, blank, TODO, 待補, only a placeholder |
| 禁止透露資訊 | absent, blank, TODO, 待補, only a placeholder |
| 出場角色聲線卡引用 | absent, blank, TODO, missing file path or character reference |
| 角色表層目標 | absent, blank, TODO, 待補, only a placeholder |
| 角色真實目標 | absent, blank, TODO, 待補, only a placeholder |

Use this refusal shape:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: 任務包核心欄位未補齊。
Where: <task pack path>
Why: /dialogue-write 需要 6 個核心欄位齊全，否則台詞會靠通用文風補洞。
下一步: 補完列出的核心欄位，完成 D.2.5 task review gate 後重跑 /dialogue-write。
```

Do not start a D.2.5 re-review flow from this skill. Tell the user what is missing and stop.

## .protocol_version 寫入規範

If prerequisites fail before Stage 1, write nothing.

After a successful write, append or update exactly one `dialogue-write` entry. Use concrete entity IDs and concrete file paths only. Do not write wildcard IDs such as `S-*`, `S-<n>-<m>`, or `CH-*` into runtime phase_log entries.

Common completed entry:

```yaml
- phase: dialogue-write
  date: YYYY-MM-DD
  skill: /dialogue-write
  status: completed
  scene_id: S-01-03
  dialogue_paths:
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01A.md
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01B.md
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01C.md
  mode_tag: DRAFT_TRIAL
  converge_sources: null
  incomplete_fields: []
  prereq_waived: false
```

Convergence entry:

```yaml
- phase: dialogue-write
  date: YYYY-MM-DD
  skill: /dialogue-write --converge
  status: completed
  scene_id: S-01-03
  dialogue_paths:
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v02.md
  mode_tag: CONVERGENCE
  converge_sources:
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01A.md
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01B.md
  incomplete_fields: []
  prereq_waived: false
```

Experimental entry:

```yaml
- phase: dialogue-write
  date: YYYY-MM-DD
  skill: /dialogue-write --experimental
  status: completed
  scene_id: S-01-03
  dialogue_paths:
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01D.md
  mode_tag: EXPERIMENTAL
  converge_sources: null
  incomplete_fields: []
  prereq_waived: false
```

SINGLE_ITER entry:

```yaml
- phase: dialogue-write
  date: YYYY-MM-DD
  skill: /dialogue-write --single-iter
  status: completed
  scene_id: S-01-03
  dialogue_paths:
    - 08_dialogue_outputs/CH01_S03_<short>_dialogue_v01-iter.md
  mode_tag: SINGLE_ITER
  converge_sources: null
  incomplete_fields: []
  prereq_waived: false
  iteration_count: 1
  iteration_note: "<user-agent iteration summary or null>"
  base_dialogue: null
```

Abort entry, when an in-progress write already began:

```yaml
- phase: dialogue-write
  date: YYYY-MM-DD
  skill: /dialogue-write
  status: aborted
  scene_id: S-01-03
  dialogue_paths: []
  mode_tag: DRAFT_TRIAL
  abort_reason: <short reason>
  detail: <human-readable detail>
```

Do not write real project-specific `.protocol_version` values inside this SKILL.md.

## 輸入

The user provides one of:

- a task-pack path under `07_scene_tasks/`
- a scene ID such as `S-01-03`
- no args, if the last completed `/scene-task` entry is unambiguous
- one allowed mode flag
- convergence trial paths when using `--converge`
- iteration instructions in chat when using `--single-iter`

Scene ID parsing:

| User input | Canonical scene ID | Filename stem |
|---|---|---|
| `S-01-03` | `S-01-03` | `CH01_S03` |
| `CH01_S03` | `S-01-03` | `CH01_S03` |
| `S-1-3` | `S-01-03` | `CH01_S03` |
| `CH1_S3` | `S-01-03` | `CH01_S03` |

Reject multi-scene, branch, side-scene, or range inputs unless the local task pack explicitly defines that convention.

## 輸出

Runtime output includes:

- Stage 1 diagnostic report in chat.
- Stage 2 exploration fragments in chat, only if requested.
- Stage 3 trial preview, approval request, and v01A/v01B/v01C writes after approval.
- Stage 4 experimental preview, approval request, and v01D write after approval.
- Stage 5 convergence preview, approval request, and v02 write after approval.
- Stage 5a SINGLE_ITER preview, chat iteration, approval request, and v01-iter write after approval.
- Stage 6 `/status` validation and next-step recommendation.

Runtime file outputs are limited to:

- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01B.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01C.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01D.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v02.md`
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01-iter.md`
- `.protocol_version.phase_log`

Dialogue file frontmatter must include the Chinese five-field header plus downstream YAML fields:

```yaml
---
entities: [S-01-03]
depends_on: [C-<name>, R-<a>-<b>]
weight: {S-01-03: 1.0}
scene_id: S-01-03
source_task: 07_scene_tasks/CH01_S03_台詞任務包.md
source_dialogue: null
source_dialogues: null
pipeline_state: DIALOGUE_TRIAL
mode_tag: DRAFT_TRIAL
qa_decision: null
qa_type: null
dialogue_keys: {}
---
```

For convergence, set `source_dialogues` to the trial path list and `pipeline_state` to `DIALOGUE_CONVERGED`.

When the local schema requires populated `dialogue_keys`, assign stable keys for each line and store A-* references under the relevant key fields such as `portrait`, `bgm`, or `sfx`. If a referenced A-* asset does not exist, refuse and ask the user to create or correct the asset reference. Do not auto-create `10_art_assets/`.

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v*.md` | 主體；trial / experimental / converged / SINGLE_ITER 台詞檔 |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: dialogue-write`, `scene_id`, `dialogue_paths`, `mode_tag`, `converge_sources`, and runtime log fields |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/`, `_tools/frontend/`, `scripts/`, `_design/`, `_design/registries/`, existing `.claude/skills/` files | 任何寫入都屬 D-050 越界 |
| 不改 | `07_scene_tasks/CH<n>_S<m>_台詞任務包.md` | 任務包屬 /scene-task scope；本 skill 只讀不改 |

## 邊界

The skill must not:

- modify LOCKED files without explicit file-specific confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, registry Template files, parser code, `_design/*.md`, or existing skill files
- modify existing Phase A, Phase B, or Phase C C.1 skills or wrappers
- create `/qa` or any C.3 scope artifact
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scenes, task packs, or QA reports
- modify the task pack file
- auto-trigger D.3.5 human convergence gate
- auto-trigger `/qa`
- write `_design/phase_d_dialogue_review_log.md`
- promote dialogue `狀態` to `FINAL` or `LOCKED`
- promote trial dialogue `狀態` beyond `DRAFT`
- promote convergence dialogue beyond `REVIEW`
- promote `pipeline_state` to `QA_PASSED`, `QA_FAILED`, or `DIALOGUE_FINAL`
- create new entity types, enum values, schemas, parser behavior, or registry behavior
- write experimental output into the formal v01A/v01B/v01C group
- skip the six-core-field refusal logic
- delete user-marked retained lines without explicit user instruction
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**

- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**

- 本 skill 寫檔目錄嚴格限定為 `08_dialogue_outputs/` 一個目錄；任何超出範圍的寫入屬越界
- `.protocol_version.phase_log` 是 runtime tracking exception，只能記錄本 skill 的 `dialogue-write` entry，不得順手修其他 phase
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

## 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If the task pack six core fields are missing, refuse and tell the user to complete the task pack before rerunning. Do not start D.2.5 review from this skill.

If a target file becomes `LOCKED` or changes unexpectedly between preview approval and write, stop before writing that file and ask for a decision.

If any Stage 3, Stage 4, Stage 5, or Stage 5a write fails:

1. Stop further writes immediately.
2. Roll back files written by this skill in the current run when possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly which files were written, rolled back, or require manual inspection.

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
