---
name: view-detailed-outline
description: "Read chapter and scene-index sources to compose an in-chat detailed outline view for all chapters or one CH-ID. Supports D-054 hybrid scene-index lookup: per-scene file first, aggregate 06_a fallback second. Writes no files."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/view-detailed-outline skill runtime instructions
優先級：中

# /view-detailed-outline Skill

## 用途

Use this skill when the user triggers `/view-detailed-outline` or `/view-detailed-outline <CH-ID>` to dynamically assemble the detailed outline reading surface from existing chapter and scene-index sources.

The skill reads:

- chapter structure from `05_plot/05_b_章節結構模板.md`
- aggregate scene rows from `06_scene_index/06_a_場景索引模板.md`
- existing per-scene files from `06_scene_index/CH<n>_S<m>_<scene_name>.md` when D-054 split files already exist

This skill prints one combined Markdown view in chat. It does not write `view/` files, does not update entity status, does not split scene files, and does not rewrite source wording.

## 觸發語

- `/view-detailed-outline`
- `/view-detailed-outline <CH-ID>`
- Chinese alias: `/查看細綱`, via `.claude/skills/查看細綱/SKILL.md`

The slash command accepts zero or one user parameter:

- no parameter: show all chapters found in `05_plot/05_b_章節結構模板.md`
- `<CH-ID>`: show only one chapter, normalized to `CH-<n>` for entity checks and `CH<n>` for filename prefixes

If more than one parameter is supplied and it cannot be normalized as one chapter ID, stop and ask the user to rerun with either no parameter or one `CH-ID`.

## 觸發協議

There is no corresponding `00_protocol/` file for `/view-detailed-outline`.

`/view-detailed-outline` is a pure technical read-only skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.3
- `_design/ARCHITECTURE.md` v1.6 §4.1 for dynamic assembly
- `_design/ARCHITECTURE.md` v1.6 §4.3 / §4.4 and `_design/UX_SPEC.md` v0.4 §7 for presentation rules
- `_design/SPEC.md` v1.2 §5.2 for frontmatter and entity metadata
- `_design/D054_DECISION_PACKAGE.md` v0.2 for D-054 hybrid scene-index reads
- `.claude/skills/scene-task/SKILL.md` v0.1 for the existing D-054 per-scene-first, aggregate-fallback pattern

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. If the user supplies `<CH-ID>`, normalize it to canonical chapter entity form `CH-<n>`.
   - The chapter must be found in `05_plot/05_b_章節結構模板.md`, or in `06_scene_index/06_a_場景索引模板.md`, or in at least one matching per-scene file under `06_scene_index/CH<n>_S<m>_*.md`.
4. If the user supplies no parameter, at least one `CH-*` entry must exist in `05_plot/05_b_章節結構模板.md`.
5. Scene entities `S-*-*` shown in the view must be at `DRAFT` or above when their source file exposes a Chinese header status.
6. Do not require `REVIEW` or higher. `/view-detailed-outline` is read-any-state and may show `DRAFT` material.
7. Do not run downstream pipeline interlock checks. This skill is read-only and does not affect any active writing workflow.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If no target chapter can be found, stop with a missing-source list and tell the user to run `/create-detailed-outline`.

If individual scenes are missing after the target chapter exists, keep the chapter layout and print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]` at the scene position.

## 流程

Run exactly five stages. Keep every stage read-only unless the user has explicitly enabled the optional `.protocol_version.phase_log` audit entry described below.

### Stage 1 - Diagnosis

Open with:

```md
/view-detailed-outline 將動態組合細綱整合視圖（章節結構 + 場景索引；D-054 hybrid：per-scene 檔優先，06_a row fallback）。本 skill 純讀取，不寫任何檔。執行後在 chat 印出整合視圖。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- optional `CH-ID` normalization
- target chapter existence check

For missing prerequisites, stop before reading all source content.

### Stage 2 - Source Backtrace

Read source files in this exact order:

| Source | Content | Output position |
|---|---|---|
| `05_plot/05_b_章節結構模板.md` | `CH-*` entries, including chapter summaries | `## 章節 CH<n>：<chapter_name>` |
| `06_scene_index/06_a_場景索引模板.md` | aggregate `S-*-*` rows, including split-to-file markers | `### 場景 S-<ch>-<n>` |
| `06_scene_index/CH<n>_S<m>_<scene_name>.md` | per-scene detailed content when the D-054 split file exists | `### 場景 S-<ch>-<n>` |

For each source:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Verify expected `CH-*` or `S-*-*` entities when the source has usable frontmatter.
4. Extract relevant content only:
   - skip YAML frontmatter
   - skip the Chinese five-field header
   - preserve the remaining source text verbatim
   - for aggregate `06_a`, extract only the matching row and immediately adjacent detail block if one exists
5. Record the extracted line range for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `entities` observed when present
   - `read_source`: `per-scene`, `aggregate`, or `missing`

Do not read `07_scene_tasks/`, `08_dialogue_outputs/`, or `09_quality_assurance/`. Those downstream files are not detailed-outline sources.

### D-054 hybrid 讀檔 fallback 規範

D-054 selects Hybrid: aggregate `06_a` remains the default, while future `/iterate-scene --split-to-file` may split selected scenes into per-scene files. This skill must support both without changing file organization.

For each scene `S-<ch>-<n>` in the selected chapter scope, use this sequence.

#### Phase 1 - per-scene file first

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

#### Phase 2 - aggregate 06_a fallback

1. Read `06_scene_index/06_a_場景索引模板.md`.
2. Locate the row for canonical `S-<ch>-<n>` or equivalent `CH<n>_S<m>`.
3. If the row exists, read the row and immediately adjacent detail block if the local template stores scene detail below the table.
4. Set `read_source = "aggregate"`.
5. If the row has a `split-to-file` marker but the referenced per-scene file is missing, print `WARN`:
   - What: marker says the scene was split, but the target file is absent.
   - Where: `06_scene_index/06_a_場景索引模板.md` row marker and referenced path.
   - Why: `/view-detailed-outline` is falling back to aggregate row to avoid blocking a valid scene.
   - 下一步: inspect or restore the missing per-scene file before future scene iteration.

#### Phase 3 - neither source exists

If neither a per-scene file nor an aggregate row exists, keep the output structure and print this placeholder in the scene position:

```md
[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]
```

Do not synthesize scene content from downstream task packs or dialogue files.

#### Read-source audit requirement

For each scene, record one of:

- `per-scene`
- `aggregate`
- `missing`

Do not record both `per-scene` and `aggregate` for one scene. Put marker mismatch warnings in the chat report, not inside `read_source`.

#### Future D-054 iteration tracking

This skill must not trigger split-to-file. Splitting belongs to future Phase D `/iterate-scene <S-ID> --split-to-file`.

If, during real Phase D usage, the user repeatedly splits scenes or reports that aggregate `06_a` is too large, report this as evidence for a future per-scene supersede decision (issue number was previously written as D-055; per DECISIONS_LOG §6.18.2 it is deferred to D-056 or the next unused number). Do not modify POST_LOCK_PENDING, D054_DECISION_PACKAGE, or DECISIONS_LOG from this skill.

### Stage 3 - Assemble In Memory

Assemble a single Markdown document in memory. Do not write it to disk.

Use this structure:

```md
# 細綱 - /view-detailed-outline 動態整合視圖（CH=<specified CH or all>）

## 章節 CH<n>：<chapter_name>

<05_b CH-<n> entry summary>

*來源：[/05_plot/05_b_章節結構模板.md](/05_plot/05_b_章節結構模板.md)*

### 場景 S-<n>-<m>：<scene_name>

<per-scene file content or 06_a row content; D-054 hybrid>

*來源：[/06_scene_index/CH<n>_S<m>_<scene_name>.md](/06_scene_index/CH<n>_S<m>_<scene_name>.md) (per-scene)*

### 場景 S-<n>-<m+1>：<scene_name>

<aggregate fallback content>

*來源：[/06_scene_index/06_a_場景索引模板.md](/06_scene_index/06_a_場景索引模板.md) row*

## 章節 CH<n+1>：<chapter_name>

<...>

---

**下一步建議：**
- 持久化整合檔 -> /export-detailed-outline
- 修改章節 -> /iterate-detailed-outline <CH-ID>
- 單場拆檔 -> /iterate-scene <S-ID> --split-to-file
- 修改主線 -> /iterate-outline
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If the user supplied a `CH-ID`, include only that chapter and its scenes.
- If the user supplied no parameter, include all chapters found in `05_b`, in file order.
- If a chapter has no scenes, print an italic empty-state sentence explaining that the chapter exists but has no scene rows yet.
- If a scene is missing from both per-scene file and aggregate `06_a`, print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]`.

### Stage 4 - Present in Chat

Print the assembled Markdown directly in chat.

Do not write:

- `view/細綱_<CH-ID>.md`
- `view/細綱.md`
- any other `view/<entity>.md`
- any report file
- any source file

### Stage 5 - Read-Only Audit

After output, verify that:

- all selected chapters were either printed or explicitly marked missing
- every source-backed chapter or scene section ends with an italic `來源` line
- every scene used the D-054 lookup sequence: per-scene first, aggregate `06_a` fallback second, missing placeholder third
- per-scene detections and aggregate fallbacks are internally consistent
- no breadcrumb was added
- no TOC was added
- no source file was modified
- no entity status or completion state was updated
- no split-to-file action was performed

Print the next-step suggestions exactly once:

```md
**下一步建議：**
- 持久化整合檔 -> /export-detailed-outline
- 修改章節 -> /iterate-detailed-outline <CH-ID>
- 單場拆檔 -> /iterate-scene <S-ID> --split-to-file
- 修改主線 -> /iterate-outline
```

Do not automatically trigger `/status`, `/check-gaps`, `/export-detailed-outline`, `/iterate-detailed-outline`, `/iterate-scene`, `/iterate-outline`, or any other skill.

## 呈現規則

Follow ARCH §4.1 and UX_SPEC §7.

1. Chat dynamic assembly does not add breadcrumb. Breadcrumb belongs only to `/export-*` integration files.
2. Chat dynamic assembly does not add TOC. TOC belongs only to long `/export-*` integration files.
3. Every source-backed section ends with one italic source line:
   - `*來源：[/path/to/source.md](/path/to/source.md)*`
   - For multi-source sections, list sources separated by commas.
4. Cross-file links must be project-root based and start with `/`.
5. Same-file anchors use `#slug` and do not start with `/`.
6. Use one-way references. The assembled view may link to source files; source files do not need reverse links.
7. Chat links may not be clickable in every agent UI. Keep them anyway as plain-text source location hints.
8. Do not expose parser stack traces, raw Python objects, or internal implementation details.

## .protocol_version 寫入規範

Default behavior: do not write `.protocol_version`.

Optional audit behavior: if the user explicitly asks to log view reads, or the runtime environment has an explicit audit-log setting enabled, append one read-only audit entry to `.protocol_version.phase_log`.

The optional entry must not update entity completion, entity status, `created_entities`, `entities_touched`, or any downstream pipeline state.

Audit entry shape:

```yaml
- phase: view-detailed-outline
  date: YYYY-MM-DD
  skill: /view-detailed-outline
  status: completed
  target_entity: CH-<n>  # or "all" when no parameter is supplied
  scope_choice: <CH-<n>>  # or "all_chapters"
  read_sources:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
    - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene file list when detected
  d054_per_scene_files_detected: [<list>]
  output_lines: <estimated assembled output line count>
  output_target: chat
  customizations: []
```

If the user says view reads are frequent or requests audit-log skip, do not write this optional entry.

## 輸入

The skill accepts zero or one user parameter:

- no parameter: assemble all chapters
- `<CH-ID>`: assemble one chapter

Runtime inputs are fixed after scope selection:

- `.protocol_version`
- `05_plot/05_b_章節結構模板.md`
- `06_scene_index/06_a_場景索引模板.md`
- existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files when the D-054 lookup finds them

Dynamic issue-list loading is not applicable. `/view-detailed-outline` is read-only data assembly, not a creation or iteration protocol.

## 輸出

The output is one chat Markdown view.

This skill writes no persistent integration file. If the user wants a persisted `view/` integration file, tell them to run `/export-detailed-outline`.

Output must include:

- the assembled detailed outline view
- source references after every source-backed chapter or scene section
- D-054 source mode behavior when per-scene files or aggregate fallbacks are involved
- the next-step suggestions

## 邊界

`/view-detailed-outline` is a pure read-only skill. It is strictly limited to:

1. Do not write any file, except the optional `.protocol_version.phase_log` audit entry when explicitly enabled.
2. Do not write a `view/` integration file. That is `/export-detailed-outline` Wave 14 scope.
3. Do not expand source scope beyond `05_plot/05_b_章節結構模板.md`, `06_scene_index/06_a_場景索引模板.md`, and existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` per-scene files. Do not add `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/05_a`, `05_plot/05_c`, `05_plot/05_d`, `05_plot/05_e`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, or `_tools/frontend/`.
4. Do not upgrade, downgrade, or otherwise change entity status.
5. Do not call other `/view-*` skills automatically.
6. Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
7. Do not write `LOCKED` status or modify any `LOCKED` source.

Unlike `/create-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, and `/qa`, this skill does not include the D-050 three write-boundary blocks. The governing boundary is this read-only section.

## 錯誤處理 / Rollback

Because `/view-detailed-outline` is read-only by default, rollback normally means: no source files were changed, no generated files need deletion, and the user can rerun the skill after fixing missing prerequisites.

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- malformed or ambiguous `CH-ID`
- no `CH-*` entries in `05_plot/05_b_章節結構模板.md` when no parameter is supplied
- requested `CH-ID` absent from `05_b`, `06_a`, and per-scene files

For these, stop before assembling output.

Partial source failures:

- If `06_a` is missing but per-scene files exist for the selected chapter, assemble from per-scene files and warn that aggregate fallback cannot be used.
- If a per-scene marker points to a missing file but `06_a` has a matching row, use aggregate fallback and print a `WARN`.
- If neither source exists for a scene, print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]`.
- Tell the user to run `/create-detailed-outline` when the detailed outline foundation has not been created, `/iterate-detailed-outline <CH-ID>` when chapter sources need repair, or `/iterate-scene <S-ID> --split-to-file` when the user wants to split one aggregate scene into a per-scene file.

If the optional audit entry write fails, do not retry with ad hoc file writes. Print a warning that the chat output succeeded but audit logging failed.

## 錯誤呈現規則

Follow ARCH §3.3.1.

Use:

- `## ✗ 無法執行 / Cannot Proceed` for missing files, unreadable files, malformed frontmatter, or parser failures that the user can fix.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for Template repo detection or incomplete Bootstrap.
- `## ⚠ 需注意 / Warning` only for non-blocking partial source gaps.

Every blocking error must include:

- `What`
- `Where`
- `Why`
- `下一步`

For multiple errors, summarize first, then list each item. Do not expose stack traces, raw enum keys, Python exceptions, or parser internals.

Use this shape for missing prerequisites:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: /view-detailed-outline 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /view-detailed-outline 需要已完成 Bootstrap 與既有 CH-* / S-*-* source 才能組合視圖。
下一步: 先執行 /init-project；若尚未建立細綱，執行 /create-detailed-outline。
```

Use this shape for D-054 partial source gaps:

```md
## ⚠ 需注意 / Warning

What: D-054 per-scene 檔缺漏，已 fallback 讀取 aggregate 06_a row。
Where: <missing per-scene path>；fallback source: /06_scene_index/06_a_場景索引模板.md
Why: /view-detailed-outline 支援 hybrid 讀檔，但不會自行補寫或拆分 source。
下一步: 檢查 split-to-file marker，或執行 /iterate-scene <S-ID> --split-to-file 重新建立 per-scene 檔。
```
