---
name: view-outline
description: "Read 05_plot outline sources and compose an in-chat outline view covering main plot, chapter structure, character arcs, information reveal, and foreshadowing. This skill is read-only, writes no files, and follows ARCH §4.1 dynamic assembly."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/view-outline skill runtime instructions
優先級：中

# /view-outline Skill

## 用途

Use this skill when the user triggers `/view-outline` to dynamically assemble the project outline reading surface from existing `05_plot/` source files.

The skill reads:

- main plot structure from `05_plot/05_a_主線大綱模板.md`
- chapter structure from `05_plot/05_b_章節結構模板.md`
- character arcs from `05_plot/05_c_角色弧線表.md`
- information reveal order from `05_plot/05_d_資訊揭露表.md`
- foreshadowing and payoff entries from `05_plot/05_e_伏筆與回收表.md`

This skill prints one combined Markdown view in chat. It does not write `view/` files, does not update entity status, and does not rewrite source wording.

## 觸發語

- `/view-outline`
- Chinese alias: `/查看大綱`, via `.claude/skills/查看大綱/SKILL.md`

The slash command accepts no user parameters. If extra text follows `/view-outline`, ignore it for source selection and assemble the standard outline view.

## 觸發協議

There is no corresponding `00_protocol/` file for `/view-outline`.

`/view-outline` is a pure technical read-only skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.3
- `_design/ARCHITECTURE.md` v1.6 §4.1 for dynamic assembly
- `_design/ARCHITECTURE.md` v1.6 §4.3 / §4.4 and `_design/UX_SPEC.md` v0.4 §7 for presentation rules
- `_design/SPEC.md` v1.2 §5.2 for frontmatter and entity metadata

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. Plot entity `P` must exist at `DRAFT` or above.
   - `05_plot/05_a_主線大綱模板.md` must exist, parse, have Chinese header status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` should include `P`.
4. Do not require `REVIEW` or higher. `/view-outline` is read-any-state and may show `DRAFT` material.
5. Do not run downstream pipeline interlock checks. This skill is read-only and does not affect any active writing workflow.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If `P` cannot be found, stop with a missing-source list and tell the user to run `/create-outline`.

After `P` exists, missing `05_b`, `05_c`, `05_d`, or `05_e` content is non-blocking. Keep the view layout, insert `[source 缺漏]` or an empty-state sentence for that section, and tell the user which upstream skill can repair it.

## 流程

Run exactly five stages. Keep every stage read-only unless the user has explicitly enabled the optional `.protocol_version.phase_log` audit entry described below.

### Stage 1 - Diagnosis

Open with:

```md
/view-outline 將動態組合大綱整合視圖（主線結構 + 章節結構 + 角色弧線 + 資訊揭露 + 伏筆與回收）。本 skill 純讀取，不寫任何檔。執行後在 chat 印出整合視圖。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- `P` entity source check

For missing prerequisites, stop before reading all source content.

### Stage 2 - Source Backtrace

Read source files in this exact order:

| Source | Content | Output position |
|---|---|---|
| `05_plot/05_a_主線大綱模板.md` | `P` main plot split | `## 主線結構` |
| `05_plot/05_b_章節結構模板.md` | `CH-*` entries | `## 章節結構` |
| `05_plot/05_c_角色弧線表.md` | character arc stages | `## 角色弧線` |
| `05_plot/05_d_資訊揭露表.md` | chapter reveal order | `## 資訊揭露` |
| `05_plot/05_e_伏筆與回收表.md` | foreshadowing and payoff | `## 伏筆與回收` |

For each source:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Verify expected entities when the source has usable frontmatter.
4. Extract main content only:
   - skip YAML frontmatter
   - skip the Chinese five-field header
   - preserve the remaining source text verbatim
5. Record the extracted line range for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `entities` observed when present

Do not read `06_scene_index/` scene details. Scene-level detail belongs to `/view-detailed-outline`.

### Stage 3 - Assemble In Memory

Assemble a single Markdown document in memory. Do not write it to disk.

Use this structure:

```md
# 大綱 - /view-outline 動態整合視圖

## 主線結構

<05_a content>

*來源：[/05_plot/05_a_主線大綱模板.md](/05_plot/05_a_主線大綱模板.md)*

## 章節結構

<05_b content>

*來源：[/05_plot/05_b_章節結構模板.md](/05_plot/05_b_章節結構模板.md)*

## 角色弧線

<05_c content>

*來源：[/05_plot/05_c_角色弧線表.md](/05_plot/05_c_角色弧線表.md)*

## 資訊揭露

<05_d content>

*來源：[/05_plot/05_d_資訊揭露表.md](/05_plot/05_d_資訊揭露表.md)*

## 伏筆與回收

<05_e content>

*來源：[/05_plot/05_e_伏筆與回收表.md](/05_plot/05_e_伏筆與回收表.md)*

---

**下一步建議：**
- 持久化整合檔 -> /export-outline
- 修改主線 -> /iterate-outline
- 修改章節細綱 -> /iterate-detailed-outline
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If a source body is empty, print an italic empty-state sentence explaining that the source exists but has no content to show.
- If a partial source is missing, print `[source 缺漏]` in that source position and keep assembling the rest.

### Stage 4 - Present in Chat

Print the assembled Markdown directly in chat.

Do not write:

- `view/大綱.md`
- any other `view/<entity>.md`
- any report file
- any source file

### Stage 5 - Read-Only Audit

After output, verify that:

- all required source sections were either printed or explicitly marked `[source 缺漏]`
- every source-backed section ends with an italic `來源` line
- no breadcrumb was added
- no TOC was added
- no source file was modified
- no entity status or completion state was updated
- no scene-level detail from `06_scene_index/` was pulled into the outline view

Print the next-step suggestions exactly once:

```md
**下一步建議：**
- 持久化整合檔 -> /export-outline
- 修改主線 -> /iterate-outline
- 修改章節細綱 -> /iterate-detailed-outline
```

Do not automatically trigger `/status`, `/check-gaps`, `/export-outline`, `/iterate-outline`, `/iterate-detailed-outline`, or any other skill.

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
- phase: view-outline
  date: YYYY-MM-DD
  skill: /view-outline
  status: completed
  target_entity: P
  read_sources:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_c_角色弧線表.md
    - 05_plot/05_d_資訊揭露表.md
    - 05_plot/05_e_伏筆與回收表.md
  output_lines: <estimated assembled output line count>
  output_target: chat
  customizations: []
```

If the user says view reads are frequent or requests audit-log skip, do not write this optional entry.

## 輸入

The skill accepts no user parameters.

Runtime inputs are fixed:

- `.protocol_version`
- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_b_章節結構模板.md`
- `05_plot/05_c_角色弧線表.md`
- `05_plot/05_d_資訊揭露表.md`
- `05_plot/05_e_伏筆與回收表.md`

Dynamic issue-list loading is not applicable. `/view-outline` is read-only data assembly, not a creation or iteration protocol.

## 輸出

The output is one chat Markdown view.

This skill writes no persistent integration file. If the user wants a persisted `view/` integration file, tell them to run `/export-outline`.

Output must include:

- the assembled outline view
- source references after every source-backed section
- the next-step suggestions

## 邊界

`/view-outline` is a pure read-only skill. It is strictly limited to:

1. Do not write any file, except the optional `.protocol_version.phase_log` audit entry when explicitly enabled.
2. Do not write a `view/` integration file. That is `/export-outline` Wave 14 scope.
3. Do not expand source scope beyond the five listed `05_plot/` sources. Do not add `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, or `_tools/frontend/`.
4. Do not upgrade, downgrade, or otherwise change entity status.
5. Do not call other `/view-*` skills automatically.
6. Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
7. Do not write `LOCKED` status or modify any `LOCKED` source.

Unlike `/create-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, and `/qa`, this skill does not include the D-050 three write-boundary blocks. The governing boundary is this read-only section.

## 錯誤處理 / Rollback

Because `/view-outline` is read-only by default, rollback normally means: no source files were changed, no generated files need deletion, and the user can rerun the skill after fixing missing prerequisites.

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- `P` source absent
- parser/frontmatter cannot confirm `P`

For these, stop before assembling output.

Partial source failures:

- If `05_b`, `05_c`, `05_d`, or `05_e` is missing after `P` exists, keep the output skeleton and print `[source 缺漏]` in that section.
- If a source body is empty, print an italic empty-state sentence instead of inventing content.
- Tell the user to run `/create-outline` when the outline foundation has not been created, `/iterate-outline` when existing outline sources need repair, or `/iterate-detailed-outline` when chapter-level sources need repair.

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

What: /view-outline 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /view-outline 需要已完成 Bootstrap 與既有 P source 才能組合視圖。
下一步: 先執行 /init-project；若尚未建立主線大綱，執行 /create-outline。
```

Use this shape for partial source gaps:

```md
## ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏] placeholder 保留視圖骨架。
Where: <missing source path>
Why: /view-outline 不會自行補寫 source，只能呈現目前可讀資料。
下一步: 執行 /iterate-outline 或 /iterate-detailed-outline 修復缺漏 source。
```
