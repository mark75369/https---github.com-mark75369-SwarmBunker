---
name: view-character
description: "Read one C-<name> character's voice card plus relationship, timeline, arc, and scene-appearance sources, then compose a read-only in-chat character view. Writes no files and follows ARCH §4.1 dynamic assembly."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/view-character skill runtime instructions
優先級：中

# /view-character Skill

## 用途

Use this skill when the user triggers `/view-character <name>` to dynamically assemble the reading surface for one character entity `C-<name>`.

The skill reads:

- the character voice card from `03_characters/main/`, `03_characters/minor/`, or `03_characters/npc/`
- relationship entries from `04_relationships/04_a_角色關係矩陣.md`
- relationship timeline entries from `04_relationships/04_b_關係變化時間線.md`
- character arc entries from `05_plot/05_c_角色弧線表.md`
- scene appearances from `06_scene_index/06_a_場景索引模板.md` plus existing D-054 per-scene files when present

This skill prints one combined Markdown view in chat. It does not write `view/` files, does not update entity status, and does not rewrite source wording.

## 觸發語

- `/view-character <name>`
- Chinese alias: `/查看角色 <name>`, via `.claude/skills/查看角色/SKILL.md`

The slash command requires exactly one user parameter: the character display name used to resolve `C-<name>`.

If `<name>` is missing, stop and ask the user to rerun the skill with a character name. If extra parameters are supplied, treat them as part of the name only when they are clearly a multi-token character name; otherwise stop and ask for one unambiguous name.

## 觸發協議

There is no corresponding `00_protocol/` file for `/view-character`.

`/view-character` is a pure technical read-only skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.3
- `_design/ARCHITECTURE.md` v1.6 §4.1 for dynamic assembly
- `_design/ARCHITECTURE.md` v1.6 §4.3 / §4.4 and `_design/UX_SPEC.md` v0.4 §7 for presentation rules
- `_design/SPEC.md` v1.2 §5.2 for frontmatter and entity metadata
- `_design/D054_DECISION_PACKAGE.md` v0.2 for optional per-scene scene-index reads

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. A character name parameter must be present and normalize to `C-<name>`.
4. `C-<name>` must exist at `DRAFT` or above.
   - Locate it by parsing frontmatter `entities` in `03_characters/main/<name>_聲線卡.md`, `03_characters/main/<name>_*.md`, `03_characters/minor/<name>_*.md`, or `03_characters/npc/<name>_*.md`.
   - Accepted Chinese header statuses are `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`.
5. Do not require `REVIEW` or higher. `/view-character` is read-any-state and may show `DRAFT` material.
6. Do not run downstream pipeline interlock checks. This skill is read-only and does not affect any active writing workflow.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If `C-<name>` cannot be found, stop with a missing-source list and tell the user to run `/create-character <name>`.

Relationship, timeline, arc, or scene-appearance gaps are non-blocking after the character card exists. Keep the view layout, insert `[source 缺漏]` or an empty-state sentence for that section, and tell the user which upstream skill can repair it.

## 流程

Run exactly five stages. Keep every stage read-only unless the user has explicitly enabled the optional `.protocol_version.phase_log` audit entry described below.

### Stage 1 - Diagnosis

Open with:

```md
/view-character <name> 將動態組合角色整合視圖（聲線卡 + 關係 + 時間線 + 弧線 + 出場場景）。本 skill 純讀取，不寫任何檔。執行後在 chat 印出整合視圖。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- `C-<name>` parameter and entity existence check

For missing prerequisites, stop before reading all source content.

### Stage 2 - Source Backtrace

Read source files in this exact order:

| Source | Content | Output position |
|---|---|---|
| `03_characters/main/<name>_聲線卡.md` or `03_characters/main/<name>_*.md` or `03_characters/minor/<name>_*.md` or `03_characters/npc/<name>_*.md` | primary `C-<name>` voice card resolved by frontmatter | `## 聲線卡` |
| `04_relationships/04_a_角色關係矩陣.md` | entries whose frontmatter or section content matches `R-<name>-*` or `R-*-<name>` | `## 關係` |
| `04_relationships/04_b_關係變化時間線.md` | timeline entries that reference `C-<name>` or the display name | `## 時間線` |
| `05_plot/05_c_角色弧線表.md` | character arc stages for `C-<name>` | `## 弧線` |
| `06_scene_index/06_a_場景索引模板.md` plus existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files | scene rows or per-scene files whose entities, depends_on, appearing-character field, or body references include `C-<name>` | `## 出場場景` |

For each source:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Verify expected entities when the source has usable frontmatter.
4. Extract relevant content only:
   - skip YAML frontmatter
   - skip the Chinese five-field header
   - preserve the remaining source text verbatim
   - for aggregate files, extract only the section, row, or adjacent detail block relevant to `C-<name>`
5. Record extracted line ranges for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `entities` observed when present

For relationship extraction, match both directions:

- `R-<name>-*`
- `R-*-<name>`

For scene appearances, use D-054-compatible scene-index discovery:

1. Scan `06_scene_index/06_a_場景索引模板.md` for rows or adjacent detail blocks that mention `C-<name>` or the display name.
2. Scan existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files for frontmatter or body references to `C-<name>`.
3. List matched scene IDs once. If a per-scene file and an aggregate row describe the same scene, prefer the per-scene file as the displayed source and note that aggregate `06_a` also indexed the scene.
4. Do not read downstream `07_scene_tasks/`, `08_dialogue_outputs/`, or `09_quality_assurance/` files.

### Stage 3 - Assemble In Memory

Assemble a single Markdown document in memory. Do not write it to disk.

Use this structure:

```md
# 角色：<name> - /view-character 動態整合視圖

## 聲線卡

<03_characters/.../<name> voice card content>

*來源：[/03_characters/<path>](/03_characters/<path>)*

## 關係

<04_a extracted relationship entries for R-<name>-* / R-*-<name>>

*來源：[/04_relationships/04_a_角色關係矩陣.md](/04_relationships/04_a_角色關係矩陣.md)*

## 時間線

<04_b extracted timeline entries>

*來源：[/04_relationships/04_b_關係變化時間線.md](/04_relationships/04_b_關係變化時間線.md)*

## 弧線

<05_c extracted arc entries>

*來源：[/05_plot/05_c_角色弧線表.md](/05_plot/05_c_角色弧線表.md)*

## 出場場景

<06_a rows and/or per-scene entries that reference C-<name>>

*來源：[/06_scene_index/06_a_場景索引模板.md](/06_scene_index/06_a_場景索引模板.md) (含 per-scene 拆檔；D-054 hybrid)*

---

**下一步建議：**
- 持久化整合檔 -> /export-character <name>
- 修改角色 -> /iterate-character <name>
- 修改關係 -> /iterate-relationship <name> <other>
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If a source body exists but the requested character has no relevant slice, print an italic empty-state sentence explaining that no matching entry was found.
- If a partial source is missing, print `[source 缺漏]` in that source position and keep assembling the rest.

### Stage 4 - Present in Chat

Print the assembled Markdown directly in chat.

Do not write:

- `view/角色_<name>.md`
- any other `view/<entity>.md`
- any report file
- any source file

### Stage 5 - Read-Only Audit

After output, verify that:

- all source-backed sections were either printed or explicitly marked `[source 缺漏]`
- every source-backed section ends with an italic `來源` line
- no breadcrumb was added
- no TOC was added
- no source file was modified
- no entity status or completion state was updated
- scene appearances were deduplicated when both `06_a` and per-scene files mentioned the same scene

Print the next-step suggestions exactly once:

```md
**下一步建議：**
- 持久化整合檔 -> /export-character <name>
- 修改角色 -> /iterate-character <name>
- 修改關係 -> /iterate-relationship <name> <other>
```

Do not automatically trigger `/status`, `/check-gaps`, `/export-character`, `/iterate-character`, `/iterate-relationship`, or any other skill.

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
- phase: view-character
  date: YYYY-MM-DD
  skill: /view-character
  status: completed
  target_entity: C-<name>
  read_sources:
    - 03_characters/main/<name>_聲線卡.md  # or resolved minor/npc path
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_c_角色弧線表.md
    - 06_scene_index/06_a_場景索引模板.md  # plus per-scene file list when detected
  output_lines: <estimated assembled output line count>
  output_target: chat
  customizations: []
```

If the user says view reads are frequent or requests audit-log skip, do not write this optional entry.

## 輸入

The skill accepts one required user parameter:

- `<name>`: character display name, normalized to `C-<name>`

Runtime inputs are fixed after the character entity resolves:

- `.protocol_version`
- the resolved `03_characters/.../<name>_*.md` voice card
- `04_relationships/04_a_角色關係矩陣.md`
- `04_relationships/04_b_關係變化時間線.md`
- `05_plot/05_c_角色弧線表.md`
- `06_scene_index/06_a_場景索引模板.md`
- existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files when they already exist and mention `C-<name>`

Dynamic issue-list loading is not applicable. `/view-character` is read-only data assembly, not a creation or iteration protocol.

## 輸出

The output is one chat Markdown view.

This skill writes no persistent integration file. If the user wants a persisted `view/` integration file, tell them to run `/export-character <name>`.

Output must include:

- the assembled character view
- source references after every source-backed section
- the next-step suggestions

## 邊界

`/view-character` is a pure read-only skill. It is strictly limited to:

1. Do not write any file, except the optional `.protocol_version.phase_log` audit entry when explicitly enabled.
2. Do not write a `view/` integration file. That is `/export-character` Wave 14 scope.
3. Do not expand source scope beyond the listed character, relationship, plot-arc, and scene-index sources. Do not add `01_world/`, `02_vocabulary/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, or `_tools/frontend/`.
4. Do not upgrade, downgrade, or otherwise change entity status.
5. Do not call other `/view-*` skills automatically.
6. Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
7. Do not write `LOCKED` status or modify any `LOCKED` source.

Unlike `/create-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, and `/qa`, this skill does not include the D-050 three write-boundary blocks. The governing boundary is this read-only section.

## 錯誤處理 / Rollback

Because `/view-character` is read-only by default, rollback normally means: no source files were changed, no generated files need deletion, and the user can rerun the skill after fixing missing prerequisites.

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- missing or ambiguous character name parameter
- `C-<name>` voice-card source absent
- parser/frontmatter cannot confirm `C-<name>`

For these, stop before assembling output.

Partial source failures:

- If `04_a`, `04_b`, `05_c`, or `06_a` is missing, keep the output skeleton and print `[source 缺漏]` in that section.
- If a relationship, timeline, arc, or scene appearance is simply not found for the character, print an italic empty-state sentence instead of inventing content.
- If a per-scene file cannot be opened but `06_a` has a usable row, display the aggregate row and warn that per-scene read failed.
- Tell the user to run `/create-character <name>` when the character foundation has not been created, `/iterate-character <name>` when existing character sources need repair, or `/iterate-relationship <name> <other>` when relationship sources need repair.

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

What: /view-character 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /view-character 需要已完成 Bootstrap 與既有 C-<name> source 才能組合視圖。
下一步: 先執行 /init-project；若尚未建立角色，執行 /create-character <name>。
```

Use this shape for partial source gaps:

```md
## ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏] placeholder 保留視圖骨架。
Where: <missing source path>
Why: /view-character 不會自行補寫 source，只能呈現目前可讀資料。
下一步: 執行 /iterate-character <name> 或 /iterate-relationship <name> <other> 修復缺漏 source。
```
