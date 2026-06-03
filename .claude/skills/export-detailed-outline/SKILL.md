---
name: export-detailed-outline
description: "Compose CH-* and S-*-* detailed outline sources into DERIVED view/細綱.md for all chapters or one CH-ID. Includes D-054 hybrid scene lookup: per-scene file first, aggregate 06_a fallback second, with placeholder on missing."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/export-detailed-outline skill runtime instructions
優先級：中

# /export-detailed-outline Skill

## 用途

Use this skill when the user triggers `/export-detailed-outline` or `/export-detailed-outline <CH-ID>` to generate a persistent static integration file for detailed outline content.

The skill reads the same source set as `/view-detailed-outline`:

- chapter structure from `05_plot/05_b_章節結構模板.md`
- aggregate scene rows from `06_scene_index/06_a_場景索引模板.md`
- existing per-scene files from `06_scene_index/CH<n>_S<m>_<scene_name>.md` when D-054 split files already exist

Unlike `/view-detailed-outline`, this skill writes the assembled output to `view/細綱.md` with `狀態：DERIVED`, adds static-file navigation, and appends a `.protocol_version.phase_log` audit entry. It does not rewrite source files, does not update entity completion, does not split scene files, and does not implement Layer 3 Export.

## 觸發語

- `/export-detailed-outline`
- `/export-detailed-outline <CH-ID>`
- Chinese alias: `/匯出細綱`, via `.claude/skills/匯出細綱/SKILL.md`

The slash command accepts zero or one user parameter:

- no parameter: export all chapters found in `05_plot/05_b_章節結構模板.md`
- `<CH-ID>`: export only one chapter, normalized to `CH-<n>` for entity checks and `CH<n>` for filename prefixes

If more than one parameter is supplied and it cannot be normalized as one chapter ID, stop and ask the user to rerun with either no parameter or one `CH-ID`.

## 觸發協議

There is no corresponding `00_protocol/` file for `/export-detailed-outline`.

`/export-detailed-outline` is a technical export skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.5
- `_design/ARCHITECTURE.md` v1.6 §4.2 for `/export-*` static integration files
- `_design/ARCHITECTURE.md` v1.6 §4.3 and `_design/UX_SPEC.md` v0.4 §7 for navigation and source-link rules
- `_design/SPEC.md` v1.2 §5.2, §13.4, and §16 for frontmatter, static integration files, and `DERIVED`
- `_design/D054_DECISION_PACKAGE.md` v0.2 for D-054 hybrid scene-index reads
- `.claude/skills/view-detailed-outline/SKILL.md` v0.1 for shared detailed-outline assembly and D-054 behavior
- `.claude/skills/scene-task/SKILL.md` v0.1 for the existing D-054 per-scene-first, aggregate-fallback pattern
- `_design/DECISIONS_LOG.md` v2.0 P-004, P-005, §6.12.2 D-050, §6.16.2 D-053, and §6.17 D-054

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo; tell the user to run `/init-project` in a real Instance.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. If the user supplies `<CH-ID>`, normalize it to canonical chapter entity form `CH-<n>`.
   - The chapter must be found in `05_plot/05_b_章節結構模板.md`, or in `06_scene_index/06_a_場景索引模板.md`, or in at least one matching per-scene file under `06_scene_index/CH<n>_S<m>_*.md`.
4. If the user supplies no parameter, at least one `CH-*` entry must exist in `05_plot/05_b_章節結構模板.md`.
5. Scene entities `S-*-*` shown in the export must be at `DRAFT` or above when their source file exposes a Chinese header status.
6. `view/` must exist or be creatable.
   - If `view/` does not exist, create it during Stage 4.
   - If the directory cannot be created, stop before composing output.
7. Do not require `REVIEW` or higher. `/export-detailed-outline` is read-any-state and may export `DRAFT` material.
8. Do not run downstream pipeline interlock checks. This skill is read-source / write-DERIVED and does not affect active writing workflows.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If no target chapter can be found, stop with a missing-source list and tell the user to run `/create-detailed-outline`. If individual scenes are missing after the target chapter exists, keep the chapter layout and print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]` at the scene position.

## 流程

Run exactly five stages.

### Stage 1 - Diagnosis

Open with:

```md
/export-detailed-outline 將動態組合細綱整合視圖（章節結構 + 場景索引；D-054 hybrid：per-scene 檔優先，06_a row fallback）並寫入 `view/細綱.md` DERIVED 整合檔。本 skill 寫單一靜態整合檔；要更新請重跑本 skill。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- optional `CH-ID` normalization
- target chapter existence check
- `view/` directory availability check

For missing blocking prerequisites, stop before reading all source content.

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
   - `version`
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
   - Why: `/export-detailed-outline` is falling back to aggregate row to avoid blocking a valid scene.
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

Do not record both `per-scene` and `aggregate` for one scene. Put marker mismatch warnings in the run report, not inside `read_source`.

#### Future D-054 iteration tracking

This skill must not trigger split-to-file. Splitting belongs to future Phase D `/iterate-scene <S-ID> --split-to-file`.

If, during real Phase D usage, the user repeatedly splits scenes or reports that aggregate `06_a` is too large, report this as evidence for a future per-scene supersede decision (issue number was previously written as D-055; per DECISIONS_LOG §6.18.2 it is deferred to D-056 or the next unused number). Do not modify POST_LOCK_PENDING, D054_DECISION_PACKAGE, or DECISIONS_LOG from this skill.

### Stage 3 - Assemble, Breadcrumb, and Conditional TOC In Memory

Assemble a single Markdown document in memory before writing it to disk.

Frontmatter discipline:

- Use Chinese header extension fields `生成方式` and `組合來源`.
- Do not add the standard `entities` / `depends_on` / `weight` YAML block to the `DERIVED` file.
- Set `版本` to the highest version observed across usable sources.
- Set `最後更新` to the runtime date in `YYYY-MM-DD`.
- Keep `生成方式` fixed as `/export-detailed-outline`.
- If the user supplied a `CH-ID`, set `適用範圍` to `細綱整合視圖（CH=<CH-ID>）`; otherwise set it to `細綱整合視圖（CH=全部）`.

Use this structure:

```md
狀態：DERIVED
版本：<對應 source 的最高版本>
最後更新：<執行時的日期 YYYY-MM-DD>
適用範圍：細綱整合視圖（CH=<指定 CH 或全部>）
優先級：中
生成方式：/export-detailed-outline
組合來源：
  - 05_plot/05_b_章節結構模板.md
  - 06_scene_index/06_a_場景索引模板.md
  - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene 拆檔（D-054 hybrid；實際偵測到才列）

> 專案首頁 / 細綱 / 完整視圖

## 目錄 / Contents

<僅當預估 > 200 行時插入；含 GFM auto slug；skill 內驗證 slug 一致性 — P-005>

# 細綱 — /export-detailed-outline 靜態整合檔（CH=<指定 CH 或全部>）

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

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

If the user supplied a `CH-ID`, use breadcrumb text:

```md
> 專案首頁 / 細綱 / 章節 CH<n>
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If the user supplied a `CH-ID`, include only that chapter and its scenes.
- If the user supplied no parameter, include all chapters found in `05_b`, in file order.
- If a chapter has no scenes, print an italic empty-state sentence explaining that the chapter exists but has no scene rows yet.
- If a scene is missing from both per-scene file and aggregate `06_a`, print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]`.
- Add breadcrumb after frontmatter and before any TOC or first `#` heading.
- Add TOC only when the estimated integration file exceeds 200 lines.

### Stage 4 - Write `view/細綱.md`

Write the assembled Markdown to `<instance_root>/view/細綱.md`.

Write discipline:

- If `view/` does not exist, create it.
- If `view/細綱.md` already exists, overwrite it. `DERIVED` files are regenerated from source.
- If the user supplied a `CH-ID`, still write `view/細綱.md`; mark the narrowed chapter scope in frontmatter and title.
- Do not write `view/細綱_<CH-ID>.md` or any per-chapter variant.
- Do not update `/view/README.md`; it is manually maintained per DECISIONS_LOG P-004.
- Do not write `export/`; that belongs to Layer 3 Export A1 prompt flow, not this skill.
- On write failure, roll back partial output and do not update `.protocol_version`.

### Stage 5 - Validate and Write `phase_log`

After the file write:

1. Verify the output has Chinese header fields plus `生成方式` and `組合來源`.
2. Verify `狀態：DERIVED` and `生成方式：/export-detailed-outline`.
3. Verify breadcrumb appears after frontmatter and before the first `#`.
4. If TOC was generated, validate every TOC link slug against the actual `##` / `###` headings using GitHub Flavored Markdown slug rules.
   - Do not add manual `{#anchor}` syntax.
   - If slug mismatch is found, fix the TOC links in the file and revalidate.
5. Verify every source-backed chapter or scene section ends with an italic `來源` line.
6. Verify every scene used the D-054 lookup sequence: per-scene first, aggregate `06_a` fallback second, missing placeholder third.
7. Verify each scene audit record has exactly one `read_source` value: `per-scene`, `aggregate`, or `missing`.
8. Verify the final return link is exactly:

```md
[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

9. Append one `.protocol_version.phase_log` entry as described below.
10. Do not auto-trigger `/status`, `/check-gaps`, `/view-detailed-outline`, `/iterate-detailed-outline`, `/iterate-scene`, `/iterate-outline`, or any other skill.

Print the next-step suggestion:

```md
**下一步建議：**
整合檔已寫於 view/細綱.md；修改章節請跑 /iterate-detailed-outline <CH-ID> 後重新 /export-detailed-outline；單場拆檔請跑 /iterate-scene <S-ID> --split-to-file。
```

## 呈現規則

Follow ARCH §4.2, ARCH §4.3, and UX_SPEC §7.

1. Breadcrumb is required for the exported file:
   - all-chapter exact text: `> 專案首頁 / 細綱 / 完整視圖`
   - single-chapter exact text: `> 專案首頁 / 細綱 / 章節 CH<n>`
   - position: after frontmatter, before TOC and before the first `#`
   - no arrows, dates, or status badges
2. TOC is conditional:
   - add only when estimated output exceeds 200 lines
   - position: after frontmatter and breadcrumb, before the first `#`
   - title: `## 目錄 / Contents`
   - links use GFM auto slugs
   - validate slug consistency inside this skill per DECISIONS_LOG P-005
3. Return link is required at file end:
   - `[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)`
   - do not check for or create `/view/README.md`; it is user-maintained per P-004
4. Every source-backed section ends with one italic source line:
   - `*來源：[/path/to/source.md](/path/to/source.md)*`
   - for multi-source sections, list sources separated by commas
5. Cross-file links must be project-root based and start with `/`.
6. Same-file anchors use `#slug` and do not start with `/`.
7. Use one-way references. The exported view may link to source files; source files do not need reverse links.
8. Keep the file pure Markdown. Do not introduce GUI concepts, frontend widgets, or tool-runner behavior.
9. Do not expose parser stack traces, raw Python objects, or internal implementation details.

## .protocol_version 寫入規範

This skill must append one `.protocol_version.phase_log` audit entry after `view/細綱.md` has been written and validated.

The entry must not update entity completion, entity status, `created_entities`, `entities_touched`, or any downstream pipeline state.

Required entry shape:

```yaml
- phase: export-detailed-outline
  date: YYYY-MM-DD
  skill: /export-detailed-outline
  status: completed
  target_entity: CH-<n>  # or "all" when no parameter is supplied
  scope_choice: <CH-<n>>  # or "all_chapters"
  read_sources:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
    - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene file list when detected
  d054_per_scene_files_detected: [<list>]
  d054_scene_read_sources:
    - scene_id: S-<ch>-<m>
      read_source: <per-scene|aggregate|missing>
  output_path: view/細綱.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

If the output write succeeds but phase_log write fails, report the audit failure clearly. Do not mark the run as fully completed until the user decides whether to repair `.protocol_version`.

## 輸入

The skill accepts zero or one user parameter:

- no parameter: export all chapters
- `<CH-ID>`: export one chapter

Runtime inputs are fixed after scope selection:

- `.protocol_version`
- `05_plot/05_b_章節結構模板.md`
- `06_scene_index/06_a_場景索引模板.md`
- existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files when the D-054 lookup finds them

Dynamic issue-list loading is not applicable. `/export-detailed-outline` is read-source / write-DERIVED assembly, not a creation or iteration protocol.

## 輸出

The output is a persistent Markdown file:

- `view/細綱.md`

The file must:

- start with Chinese header fields
- use `狀態：DERIVED`
- include `生成方式：/export-detailed-outline`
- include `組合來源` listing all source paths used for the selected detailed-outline scope
- include breadcrumb
- include TOC only when estimated output exceeds 200 lines
- include source references after every source-backed chapter or scene section
- preserve D-054 source mode behavior for every scene
- end with the required return link

`DERIVED` files are generated artifacts. Do not hand-edit `view/細綱.md`; update source files through the appropriate creation or iteration skill and rerun `/export-detailed-outline`.

This skill also writes:

- `.protocol_version.phase_log` audit entry for `phase: export-detailed-outline`

It writes nothing else.

## 邊界

`/export-detailed-outline` is a write-file skill that writes exactly one static integration file plus one audit entry. It uses the D-050 / D-053 boundary pattern adapted for `view/` exports.

**Block 1 — D-050 子裁決 1（00_protocol/ 寫入禁制；本 skill 強化）：**

```md
本 skill 不寫 `00_protocol/` 任何檔。

D-050 子裁決 1 規範「所有 /create-* / /iterate-* / /scene-task / /dialogue-write / /qa
skill 嚴禁寫 00_protocol/」；本 skill 同樣適用。

例外（D-053）：/create-world 可寫 00_b §1 §2（Instance-specific section）— 本 skill 不屬於該例外。
```

**Block 2 — D-053 紀錄（exception 紀律承接）：**

```md
本 skill 不觸發 D-053 /create-world exception；本 skill 不寫 00_protocol/ 任何段。
若 user 要修改 00_b §1/§2（作品類型語氣 / 髒話尺度），請走 /iterate-world（屬 Wave 12 scope；
本 skill 純粹組合 source 寫整合檔，不擅自反向回寫 source）。
```

**Block 3 — D-050 子裁決 2（寫檔目錄表；本 skill 限定）：**

```md
本 skill 寫檔目錄表：

| 目錄 | 是否寫入 | 說明 |
|---|---|---|
| `view/` | ✅ 寫 | 寫 `view/細綱.md`（DERIVED；本 skill 唯一寫入目錄）|
| `.protocol_version` | ✅ 寫（phase_log entry 追加）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `05_plot/` | ✗ 不寫 | source 唯讀 |
| `06_scene_index/` | ✗ 不寫 | source 唯讀；不觸發 split-to-file |
| `01_world/` ~ `04_relationships/` | ✗ 不寫 | 不在本 skill scope |
| `07_scene_tasks/` ~ `09_quality_assurance/` | ✗ 不寫 | 下游 pipeline 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |
| `export/` | ✗ 不寫 | 屬 §4.2a Layer 3 Export A1 prompt 生成器 scope（separate path；不在本 skill scope）|

**寫 `view/` 目錄以外任何檔 → rollback + 拒絕。**
```

Additional boundaries:

- Do not implement `/export-world`, `/export-character`, or `/export-outline`.
- Do not implement §4.2a Layer 3 Export or write `export/<instance>_<timestamp>.{json,md}`.
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates.
- Do not upgrade, downgrade, or otherwise change entity status.
- Do not call `/view-detailed-outline` or other `/view-*` skills automatically.
- Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
- Do not trigger `/iterate-scene --split-to-file`; this skill only reads existing per-scene files when present.
- Do not write `LOCKED` source files.

## 錯誤處理 / Rollback

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- malformed or ambiguous `CH-ID`
- no `CH-*` entries in `05_plot/05_b_章節結構模板.md` when no parameter is supplied
- requested `CH-ID` absent from `05_b`, `06_a`, and per-scene files
- `view/` cannot be created

For these, stop before assembling and writing output.

Partial source failures:

- If `06_a` is missing but per-scene files exist for the selected chapter, assemble from per-scene files and warn that aggregate fallback cannot be used.
- If a per-scene marker points to a missing file but `06_a` has a matching row, use aggregate fallback and print a `WARN`.
- If neither source exists for a scene, print `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]` and keep the export layout.
- Tell the user to run `/create-detailed-outline` when the detailed outline foundation has not been created, `/iterate-detailed-outline <CH-ID>` when chapter sources need repair, or `/iterate-scene <S-ID> --split-to-file` when the user wants to split one aggregate scene into a per-scene file.

Write failure rollback:

1. Stop further writes.
2. Remove any partially written `view/細綱.md` from the current run when possible.
3. Do not append `.protocol_version.phase_log` if the output file did not validate.
4. Print the failing path and the next repair step.

Slug failure rollback:

- If TOC slug validation fails, fix the TOC links in memory or in the output file, rewrite `view/細綱.md`, and validate again.
- If validation still fails, roll back the file write and stop with an error. Do not append phase_log.

Phase log failure:

- If `view/細綱.md` is valid but `.protocol_version` cannot be updated, do not pretend the run is complete.
- Report that the integration file exists but audit logging failed, and ask the user whether to repair `.protocol_version`.

### 錯誤呈現規則

Follow ARCH §3.3.1.

Use:

- `## ✗ 無法執行 / Cannot Proceed` for missing files, unreadable files, malformed frontmatter, parser failures, write failures, or slug validation failures that the user can fix.
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
### ⏸ 條件未滿足 / Prerequisites Not Met

What: /export-detailed-outline 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /export-detailed-outline 需要已完成 Bootstrap 與既有 CH-* / S-*-* source 才能寫出 DERIVED 整合檔。
下一步: 先執行 /init-project；若尚未建立細綱，執行 /create-detailed-outline。
```

Use this shape for D-054 partial source gaps:

```md
### ⚠ 需注意 / Warning

What: D-054 per-scene 檔缺漏，已 fallback 讀取 aggregate 06_a row 或以 placeholder 保留場景位置。
Where: <missing per-scene path>；fallback source: /06_scene_index/06_a_場景索引模板.md
Why: /export-detailed-outline 支援 hybrid 讀檔，但不會自行補寫或拆分 source。
下一步: 檢查 split-to-file marker，或執行 /iterate-scene <S-ID> --split-to-file 重新建立 per-scene 檔，然後重新 /export-detailed-outline。
```
