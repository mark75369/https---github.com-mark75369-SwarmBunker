---
name: integrate
description: "Convert raw notes or files into target template fields under 00_a §3.4. Print a diff preview, wait for entry-level user approval, then write only approved DRAFT entity files and phase_log."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/integrate skill runtime instructions
優先級：中

# /integrate Skill

## 用途

Use this skill when the user triggers `/integrate` and wants raw material organized into structured template fields under `00_protocol/00_a_台詞生產協議.md` §3.4 整理模式.

`/integrate` is a controlled write skill. It may write target entity files, but only after it has printed the proposed diff in chat and the user has explicitly approved each entry with `採` or `修改後採`. Before approval, every operation is read-only.

This skill is for organizing source material into existing project structures. It does not diagnose broadly, does not run Canon Delta, does not export `view/` files, and does not rewrite protocol files.

## 觸發語

- `/integrate <target>`
- `/integrate <file_path> --target=<target>`
- `/integrate <inline text> --target=<target>`
- Chinese alias: `/整理 <target>` or `/整理 <file_path> --target=<target>`, via `.claude/skills/整理/SKILL.md`

Supported targets:

- `world`
- `character`
- `relationship`
- `outline`
- `detailed-outline`
- `vocabulary`

The target parameter is required. Do not accept a broad "scan and integrate everything" mode, because integration writes files and must know the intended write boundary before proposing changes.

## 觸發協議

The governing protocol is `00_protocol/00_a_台詞生產協議.md` §3.4 整理模式.

Runtime authority:

- `_design/TASKS.md` v1.9 §C.6 for `/diagnose` and `/integrate` as independent `00_a` mode entries
- `00_protocol/00_a_台詞生產協議.md` v0.1 §3.4.1-§3.4.4
- `_design/ARCHITECTURE.md` v1.6 §3.3, §3.3.1, §3.4, and §4.3
- `_design/SPEC.md` v1.2 §5.2 and §5.4a
- `_design/UX_SPEC.md` v0.4 §7 and §8
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050, §6.15.2 D-052, §6.16.2 D-053, and §6.17 D-054
- `scripts/parse_frontmatter.py` when source or target frontmatter must be parsed

`/integrate` is the Phase D runtime implementation of `00_a` §3.4. It must not modify `00_a`, `00_b`, `00_c`, any `00_protocol/` file, any LOCKED spec, any registry, parser code, existing skills, or existing templates outside the approved target entity files.

Dynamic issue-list registry loading is not applicable. `/integrate` is a general organization mode and is not bound to a specific issue registry.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo and the requested integration target is explicit.

Required checks:

1. D-049 / D-051 Template-detect:
   - `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed:
   - `.protocol_version` must exist.
   - `.protocol_version.phase_log` must contain `phase: bootstrap` with `status: completed`.
3. Target parameter:
   - The target must be one of `world`, `character`, `relationship`, `outline`, `detailed-outline`, or `vocabulary`.
   - If target is missing or unknown, stop and print the supported target list.
4. Target write boundary:
   - Determine the allowed write directories from the target before reading source.
   - Do not create directories or files during startup checks. Directory creation is a write and may occur only in Stage 4b after user approval.
5. Parser availability:
   - Use `scripts/parse_frontmatter.py` when parsing existing Markdown frontmatter.
   - If parser import fails and target conflict detection depends on frontmatter, stop; do not replace it with ad hoc parsing.
6. No entity prerequisite:
   - Do not require any W / V / C / R / P / CH / S entity to already exist.
   - `/integrate` is valid for organizing raw material into an otherwise empty initialized Instance.
7. No downstream interlock:
   - Do not check task/dialogue/QA pipeline locks before running unless the selected target is `detailed-outline` and the proposed write would touch an existing LOCKED scene-index source.

If Template detection, Bootstrap, parser, or target validation fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met` or `## ✗ 無法執行 / Cannot Proceed` as appropriate.

If an intended target file already exists with `狀態：LOCKED`, stop before proposing writes to that file. Do not modify LOCKED files through `/integrate`.

## 流程

Run exactly five stages. Stage 1 through Stage 4a are read-only. Stage 4b and Stage 5 may write only after explicit user approval.

### Stage 1 - Integration Setup

Open with:

```md
/integrate <target> 將把素材整理成 <target> 對應的結構化模板欄位（對齊 00_protocol/00_a §3.4 整理模式）。本 skill 寫檔但必須 user 拍板；agent 先印 diff，等 user 拍板「採」或「修改後採」才實際寫入。

開始讀取 source...
```

Then:

1. Run startup checks.
2. Confirm the trigger mode:
   - Mode A: `<target>` plus inline material in chat.
   - Mode B: `<file_path> --target=<target>`.
   - Mode C: `<inline text> --target=<target>`.
3. Determine the allowed write set for the target:

| Target | Allowed writes after approval |
|---|---|
| `world` | `01_world/` and `02_vocabulary/` only |
| `character` | `03_characters/main/`, `03_characters/minor/`, or `03_characters/npc/` |
| `relationship` | `04_relationships/` only |
| `outline` | `05_plot/05_a_主線大綱模板.md` through `05_plot/05_e_伏筆與回收表.md` |
| `detailed-outline` | `05_plot/05_b_章節結構模板.md` and `06_scene_index/06_a_場景索引模板.md` only |
| `vocabulary` | `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, and `02_vocabulary/02_c_禁用詞與慎用詞表.md` |

4. Confirm no proposed target is inside a prohibited area:
   - `00_protocol/`
   - `view/`
   - `export/`
   - `07_scene_tasks/` through `09_quality_assurance/`
   - `10_art_assets/`
   - `_design/`
   - `_tools/`
   - `scripts/`
   - `_user_manual/`
   - `archive/`
5. Do not start `/diagnose`, `/status`, `/check-gaps`, `/view-*`, `/export-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, `/qa`, `/create-*`, or any other skill.

### Stage 2 - Source Backtrace

Read source based on the selected target. Missing existing target sources are warnings unless they make conflict detection impossible.

| Target | Read scope |
|---|---|
| `world` | Existing `01_world/`, existing `02_vocabulary/`, and user-supplied material |
| `character` | Existing `03_characters/` for C-* naming and voice-card conflicts, plus user-supplied material |
| `relationship` | Existing `04_relationships/`, related `03_characters/` entity evidence, and user-supplied material |
| `outline` | Existing `05_plot/05_a` through `05_plot/05_e`, plus user-supplied material |
| `detailed-outline` | Existing `05_plot/05_b`, `06_scene_index/06_a`, any existing per-scene `06_scene_index/CH<n>_S<m>_*.md` files as read-only convention evidence, and user-supplied material |
| `vocabulary` | Existing `02_vocabulary/02_a` through `02_vocabulary/02_c`, plus user-supplied material |

For every existing Markdown source that is read:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Extract body content after skipping:
   - top YAML frontmatter, if present
   - the Chinese five-field header
4. Record source path and extracted line range for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `entities`
   - `depends_on`
5. If a file is `DEPRECATED`, do not use it as authority unless the user explicitly supplied that file path.
6. If a file is `LOCKED`, it may be read as authority but must not be proposed as a write target.

For user-supplied material:

1. Treat file-path input as source material and parse frontmatter if it is Markdown.
2. Treat inline text as raw source. Do not infer it is confirmed canon until the user approves the integration entry.
3. Preserve original setting meaning.
4. Mark uncertainty and conflicts according to `00_a` §3.4.2:
   - `TODO:` for uncertain or missing content
   - `CONFLICT:` for contradictions between source and target
   - `INFERENCE:` for AI inference that must not be mixed into confirmed setting

### Stage 3 - Assemble Structured Conclusion In Memory

Assemble one Markdown preview in memory. Do not write files.

Use this preview structure:

~~~md
# 整理結果預覽（/integrate <target>）

## 一、整理摘要

- target: <target>
- 來源素材：<file path 或 inline text excerpt>
- 既有參照：<列出讀取的既有 entity 檔>
- 寫檔邊界：<列出本 target 允許寫入的目錄 / 檔案>

## 二、擬寫入的 entity / 模板欄位 diff

### Entry 1: <entity_id 或 template field>

**目標檔：** `<path>`

**擬寫入內容：**

```yaml
entities:
  - <entity>
depends_on:
  - <related>
weight:
  <entity>: <weight>
```

```markdown
<擬寫入的 main content；對齊既有 template 結構>
```

**標記：**
- TODO: <列出不確定內容>
- CONFLICT: <列出矛盾內容；含既有 vs 擬寫入對比>
- INFERENCE: <列出 AI 推測內容>

### Entry 2: ...

## 三、整理紀律對齊（00_a §3.4）

- ✅ 優先保留原始設定意思（未改寫戲劇化）
- ✅ 不確定內容標 TODO
- ✅ 矛盾內容標 CONFLICT
- ✅ AI 推測標 INFERENCE
- ✅ 保留 template 結構
- ✗ 未編造設定 / 未新增死亡背叛血緣結局反派真相 / 未把 DRAFT 標 REVIEW 或 LOCKED

## 四、user 拍板區（必填）

對每個 Entry，user 拍板：

| Entry | 拍板 | 備註 |
|---|---|---|
| Entry 1: <entity_id> | 採 / 棄 / 修改後採 | <user 填> |
| Entry 2: ... | 採 / 棄 / 修改後採 | <user 填> |

**拍板規則：**
- **採**：agent Stage 4b 寫入該 entry 對應檔；frontmatter 狀態：DRAFT
- **棄**：agent Stage 4b 不寫該 entry；不留該 entry 的 phase_log write record
- **修改後採**：user 提供修改內容；agent Stage 4b 改用 user 修改版寫入
~~~

Assembly rules:

- Do not add a seventh operational stage.
- Keep source-backed evidence tied to project-root links when showing where conflicts came from.
- Do not convert `INFERENCE` into confirmed canon.
- Do not fill template fields by inventing setting.
- Do not upgrade any file to `REVIEW`, `FINAL`, or `LOCKED`.
- If all proposed entries are uncertain, still print the preview and ask for user approval instead of silently writing.

### Stage 4 - Print Diff, Wait for Approval, Then Write

Stage 4 has two mandatory sub-stages.

#### Stage 4a - Print Diff and Wait

Print the Stage 3 preview in chat.

Then stop and wait for the user to approve each entry with one of:

- `採`
- `棄`
- `修改後採`

Do not write files during Stage 4a. Do not create directories. Do not append `.protocol_version.phase_log`.

If the user response is ambiguous, ask for explicit entry-level approval. Do not infer approval from silence, positive tone, or general agreement.

#### Stage 4b - Write Approved Entries

Run Stage 4b only after explicit user approval.

For each entry:

- `採`: write the exact proposed content.
- `棄`: do not write this entry and do not include it in `written_files`.
- `修改後採`: write the user-modified version, preserving the target template structure.

Write rules:

1. Write only target-approved directories and files.
2. Newly written or modified entity files must use `狀態：DRAFT`.
3. Every new Markdown entity file must include:
   - Chinese five-field header
   - YAML block when the file needs entity tracking
   - `entities`, `depends_on`, and `weight` per SPEC §5.2 for upstream/static files
4. Existing target files may be merged only in the relevant template section or table row. Do not rewrite unrelated sections.
5. If the target file exists and is `LOCKED`, stop and report. Do not patch it.
6. For `detailed-outline`, write aggregate `06_scene_index/06_a_場景索引模板.md` by default. Do not create `06_scene_index/CH<n>_S<m>_*.md` per-scene files.
7. If a local Instance already has per-scene scene-index files, read them as convention evidence but do not switch organization or create new per-scene split files through this skill.

### Stage 5 - Verification, phase_log, and Next Steps

After at least one approved or modified entry is written:

1. Verify every written file has the required Chinese five-field header.
2. Verify every written entity file follows SPEC §5.2 frontmatter:
   - `entities`
   - `depends_on`
   - `weight`
3. Verify every written file remains `狀態：DRAFT`.
4. Verify no prohibited path was written.
5. Append one `.protocol_version.phase_log` entry for the completed `/integrate` run.
6. Print a concise completion report with:
   - written files
   - accepted / rejected / modified entry counts
   - target
   - next-step suggestions

If the user rejects every entry, write nothing and do not append a phase_log entry. Report that no persistent integration occurred.

Do not automatically trigger `/status`, `/check-gaps`, `/view-*`, `/export-*`, `/iterate-*`, `/diagnose`, `/scene-task`, `/dialogue-write`, `/qa`, or `/create-*`. The user must invoke follow-up skills manually.

## 呈現規則

Follow `ARCHITECTURE.md` §4.3 and `UX_SPEC.md` §7.

1. Stage 3 and Stage 4a output is chat Markdown.
2. Cross-file links must be project-root based and start with `/`.
3. Same-file anchors use `#slug` and do not start with `/`.
4. Source-backed evidence lines use italic source references:
   - `*來源：[/path/to/source.md](/path/to/source.md)*`
5. Do not add breadcrumb. Breadcrumb belongs only to `/export-*` integration files.
6. Do not add TOC. TOC belongs only to long `/export-*` integration files.
7. Use one-way references. The preview may link to source files; source files do not need reverse links.
8. Empty states must be italic and explain why the empty state can be normal.
9. Do not expose parser stack traces, raw Python objects, internal enum keys, or implementation details.
10. The diff preview must be concrete enough for user approval: include target path, proposed frontmatter, proposed body or row changes, and TODO / CONFLICT / INFERENCE markers.

## .protocol_version 寫入規範

Default behavior before user approval: do not write `.protocol_version`.

After Stage 4b writes at least one approved or user-modified entry, append one required audit entry to `.protocol_version.phase_log`.

The entry must record the user approval outcome and written files. It must not upgrade entity status, trigger review gates, or imply human approval beyond the specific entries the user approved.

Entry shape:

```yaml
- phase: integrate
  date: YYYY-MM-DD
  skill: /integrate
  status: completed
  target: <world|character|relationship|outline|detailed-outline|vocabulary>
  source_input: <file path 或 "inline_text">
  read_sources:
    - <既有參照 source 1>
    - <既有參照 source 2>
  proposed_entries: <N>
  user_accepted_entries: <N>
  user_rejected_entries: <N>
  user_modified_entries: <N>
  written_files:
    - <寫入檔 path 1>
    - <寫入檔 path 2>
  customizations: []
```

If local phase_log schema requires SPEC §5.4a fields, include them only when meaningful:

```yaml
  entities_touched:
    - <entity_id>
  iteration_count: null
  iteration_note: null
  base_dialogue: null
  conflict_resolutions: []
```

Do not write a phase_log entry for entries the user rejected. If all entries are rejected, do not append a completed `/integrate` entry.

## 輸入

Accepted user inputs:

- `/integrate <target>` plus raw material in the conversation
- `/integrate <file_path> --target=<target>`
- `/integrate <inline text> --target=<target>`

Required target values:

- `world`
- `character`
- `relationship`
- `outline`
- `detailed-outline`
- `vocabulary`

Runtime inputs may include:

- `.protocol_version`
- `scripts/parse_frontmatter.py`
- `01_world/`
- `02_vocabulary/`
- `03_characters/`
- `04_relationships/`
- `05_plot/`
- `06_scene_index/06_a_場景索引模板.md`
- existing per-scene `06_scene_index/CH<n>_S<m>_*.md` files as read-only convention evidence only
- user-supplied file material
- user-supplied inline text
- `00_protocol/00_a_台詞生產協議.md` §3.4 as protocol authority

## 輸出

Stage 4a output is one chat Markdown integration preview with:

- target
- source input
- read sources
- proposed entries
- target file paths
- proposed frontmatter / body / row diff
- TODO / CONFLICT / INFERENCE markers
- entry-level user approval table

Stage 4b output, only after user approval, may include:

- approved DRAFT entity files in the target write set
- one `.protocol_version.phase_log` entry
- a concise completion report in chat

This skill does not write:

- `00_protocol/`
- `view/`
- `export/`
- `07_scene_tasks/`
- `08_dialogue_outputs/`
- `09_quality_assurance/`
- `10_art_assets/`
- `_design/`
- `_tools/`
- `scripts/`
- `_user_manual/`
- `archive/`

If the user wants a read-only diagnostic report, tell them to run `/diagnose`. If the user wants a persisted integration view, tell them to run the relevant `/export-*` skill after the source entity files are approved.

## 邊界

`/integrate` is a write-capable skill, but every write is gated by explicit user approval. Its write boundary is stricter than general design discussion and must be enforced at runtime.

### Block 1 - D-050 子裁決 1：00_protocol/ 寫入禁制

This skill does not write any file under `00_protocol/`.

D-050 establishes that runtime skills must not modify `00_protocol/` framework files. `/integrate` applies that ban directly.

Do not write:

- `00_protocol/00_a_台詞生產協議.md`
- `00_protocol/00_b_反ai味檢查表.md`
- `00_protocol/00_c_台詞輸出格式.md`
- `00_protocol/00_d_工作流總覽.md`
- `00_protocol/00_e` through `00_protocol/00_l`

If target `world` material includes project-specific type tone or profanity scale that appears to belong in `00_b` §1 / §2, do not write `00_b`. Ask the user to use `/create-world` or `/iterate-world` for that protocol-specific path.

### Block 2 - D-053 Exception Does Not Apply

D-053 adds a narrow `/create-world` exception that permits `/create-world` to write `00_b` §1 / §2 as Instance-specific setup.

`/integrate` is not `/create-world`, so it does not inherit that exception. `/integrate --target=world` may write `01_world/` and `02_vocabulary/` only. It must not write any `00_protocol/` section.

### Block 3 - D-050 子裁決 2：Target Write Directory Table

| Directory or file family | Write? | Condition |
|---|---|---|
| `01_world/` | Conditional yes | user approved entry and `target=world` |
| `02_vocabulary/` | Conditional yes | user approved entry and `target=world` or `target=vocabulary` |
| `03_characters/` | Conditional yes | user approved entry and `target=character` |
| `04_relationships/` | Conditional yes | user approved entry and `target=relationship` |
| `05_plot/` | Conditional yes | user approved entry and `target=outline` or `target=detailed-outline` |
| `06_scene_index/06_a_場景索引模板.md` | Conditional yes | user approved entry and `target=detailed-outline` |
| `.protocol_version` | Yes after writes | append phase_log entry after at least one approved write |
| `00_protocol/` | No | D-050 / D-053 boundary |
| `06_scene_index/CH<n>_S<m>_*.md` | No | D-054 split-to-file belongs to future `/iterate-scene --split-to-file` scope |
| `07_scene_tasks/` through `09_quality_assurance/` | No | downstream pipeline not in scope |
| `10_art_assets/` | No | art asset scope not in this skill |
| `view/` / `export/` | No | Wave 14 `/export-*` and Layer 3 Export scope |
| `_design/` | No | design/spec layer |
| `_tools/` / `scripts/` / `_user_manual/` | No | tooling and documentation layer |
| `archive/` | No | historical patch area |

Writing any target-corresponding directory outside the approved row is a boundary violation. Stop and refuse rather than patching an out-of-scope file.

### Block 4 - D-052 AI-Assisted User Approval Discipline

This skill adopts D-052's human accountability principle: AI may perform mechanical edits only after explicit user approval.

Required flow:

1. Assemble structured conclusion in Stage 3.
2. Print the concrete diff preview in Stage 4a.
3. Do not write any file before user approval.
4. Wait for entry-level user approval: `採`, `棄`, or `修改後採`.
5. Write only entries approved as `採` or `修改後採`.
6. Record approval counts in phase_log:
   - `user_accepted_entries`
   - `user_rejected_entries`
   - `user_modified_entries`

Not allowed:

- writing before the user has approved
- treating a general "looks good" as entry-level approval when multiple entries exist
- writing a rejected entry
- upgrading any entity status to `REVIEW` or `LOCKED`
- inventing missing setting to fill a template
- omitting the diff preview because the change appears small

### Additional Boundaries

- Do not implement or trigger `/diagnose`; it is D.14 scope.
- Do not implement Layer 3 Export.
- Do not implement Canon Delta skill.
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates outside the approved target files.
- Do not call other skills automatically.
- Do not write `LOCKED` source files.
- Do not trigger `/iterate-scene --split-to-file`; D-054 keeps aggregate `06_a` as the default and reserves split-to-file for future iterate-scene scope.

## 錯誤處理 / Rollback

Before Stage 4b, rollback normally means no files were changed.

Blocking prerequisite failures:

- Template repo detected by `.template_root`
- Bootstrap missing or incomplete
- target missing or unsupported
- requested source file path is outside repo root
- requested source file path does not exist
- parser unavailable when frontmatter parsing is required
- proposed target file is `LOCKED`
- proposed write path is outside the target write table

For these, stop before assembling or writing output.

Partial source failures:

- If an existing target source family is missing, keep the preview but mark missing evidence as `TODO`.
- If the source contradicts existing target material, mark `CONFLICT` and show both sides.
- If a needed value is inferred from context, mark `INFERENCE` and leave it for user approval.
- If the user supplies a `DEPRECATED` file path, warn that it is deprecated and continue only because the user explicitly supplied it.

Rollback after Stage 4b:

1. If a write fails before any file is changed, report failure and write no phase_log entry.
2. If some approved files are written and a later write fails, stop, list the files already written, and do not continue to unrelated writes.
3. Do not use destructive reset commands as rollback.
4. If phase_log append fails after file writes, report that source writes succeeded but audit logging failed; do not retry with ad hoc broad rewrites.
5. If any prohibited path was accidentally written, stop immediately and report the exact path, intended target, and next recovery step for human review.

## 錯誤呈現規則

Follow `_design/ARCHITECTURE.md` §3.3.1 and `_design/UX_SPEC.md` §8.

Use:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable execution errors such as missing target, unsupported target, missing requested source, malformed frontmatter, parser failures, or ambiguous approval.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repo state that has not reached the required prerequisite, such as Template repo detection or incomplete Bootstrap.
- `## ⚠ 需注意 / Warning` only for non-blocking partial source gaps or deprecated user-supplied files.

Every blocking error must include:

- `What`
- `Where`
- `Why`
- `下一步`

For multiple errors, summarize first, then list each item. Do not expose stack traces, raw enum keys, parser exception dumps, or internal implementation objects.

Use this shape for missing target:

```md
## ✗ 無法執行 / Cannot Proceed

What: /integrate 無法啟動，因為缺少必要 target。
Where: 觸發語 `/integrate`
Why: /integrate 是寫檔 skill；必須先知道寫入邊界，才能避免誤寫錯目錄。
下一步: 重新執行 `/integrate <target>`，target 使用 world / character / relationship / outline / detailed-outline / vocabulary 其中一項。
```

Use this shape for missing approval:

```md
## ✗ 無法執行 / Cannot Proceed

What: /integrate 尚未寫檔，因為 user 拍板不完整。
Where: Stage 4a user 拍板區
Why: D-052 紀律要求每個 entry 在寫檔前取得明示拍板。
下一步: 對每個 entry 回覆 `採`、`棄`、或 `修改後採`；若要修改，直接提供修改內容。
```

Use this shape for prohibited target paths:

```md
## ✗ 無法執行 / Cannot Proceed

What: /integrate 拒絕寫入越界路徑。
Where: <proposed path>
Why: 該路徑不在 target=<target> 的 D-050 寫檔目錄表內。
下一步: 改用正確 target，或手動啟動對應 skill；若需求確實需要新寫入範圍，先回 master 端做設計拍板。
```
