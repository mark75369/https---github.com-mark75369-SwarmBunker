---
name: export-character
description: "Compose one C-<name> character voice card plus relationship, timeline, arc, and scene appearance sources into DERIVED view/角色_<name>.md. Same /view-character logic; writes breadcrumb, optional TOC, source links, and phase_log per ARCH §4.2."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/export-character skill runtime instructions
優先級：中

# /export-character Skill

## 用途

Use this skill when the user triggers `/export-character <name>` to generate a persistent static integration file for one character entity `C-<name>`.

The skill reads the same source set as `/view-character`:

- the resolved character voice card from `03_characters/main/`, `03_characters/minor/`, or `03_characters/npc/`
- relationship entries from `04_relationships/04_a_角色關係矩陣.md`
- relationship timeline entries from `04_relationships/04_b_關係變化時間線.md`
- character arc entries from `05_plot/05_c_角色弧線表.md`
- scene appearances from `06_scene_index/06_a_場景索引模板.md` plus existing D-054 per-scene files when present

Unlike `/view-character`, this skill writes the assembled output to `view/角色_<name>.md` with `狀態：DERIVED`, adds static-file navigation, and appends a `.protocol_version.phase_log` audit entry. It does not rewrite source files, does not update entity completion, and does not implement Layer 3 Export.

## 觸發語

- `/export-character <name>`
- Chinese alias: `/匯出角色 <name>`, via `.claude/skills/匯出角色/SKILL.md`

The slash command requires exactly one user parameter: the character display name used to resolve `C-<name>`.

If `<name>` is missing, stop and ask the user to rerun with a character name. If extra tokens are supplied, treat them as part of the name only when they clearly form one multi-token character name; otherwise stop and ask for one unambiguous name.

## 觸發協議

There is no corresponding `00_protocol/` file for `/export-character`.

`/export-character` is a technical export skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.5
- `_design/ARCHITECTURE.md` v1.6 §4.2 for `/export-*` static integration files
- `_design/ARCHITECTURE.md` v1.6 §4.3 and `_design/UX_SPEC.md` v0.4 §7 for navigation and source-link rules
- `_design/SPEC.md` v1.2 §5.2, §13.4, and §16 for frontmatter, static integration files, and `DERIVED`
- `.claude/skills/view-character/SKILL.md` v0.1 for shared character-view source assembly logic
- `_design/D054_DECISION_PACKAGE.md` v0.2 for D-054 hybrid scene-index reads
- `_design/DECISIONS_LOG.md` v2.0 P-004, P-005, §6.12.2 D-050, §6.16.2 D-053, and §6.17 D-054

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo; tell the user to run `/init-project` in a real Instance.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. A character name parameter must be present and normalize to `C-<name>`.
4. `C-<name>` must exist at `DRAFT` or above.
   - Locate it by parsing frontmatter `entities` in `03_characters/main/<name>_聲線卡.md`, `03_characters/main/<name>_*.md`, `03_characters/minor/<name>_*.md`, or `03_characters/npc/<name>_*.md`.
   - Accepted Chinese header statuses are `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`.
5. `view/` must exist or be creatable.
   - If `view/` does not exist, create it during Stage 4.
   - If the directory cannot be created, stop before composing output.
6. Do not require `REVIEW` or higher. `/export-character` is read-any-state and may export `DRAFT` material.
7. Do not run downstream pipeline interlock checks. This skill is read-source / write-DERIVED and does not affect active writing workflows.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If `C-<name>` cannot be found, stop with a missing-source list and tell the user to run `/create-character <name>`. Relationship, timeline, arc, or scene-appearance gaps are non-blocking after the voice card exists; keep the export layout and insert `[source 缺漏]` or an empty-state sentence in that section.

## 流程

Run exactly five stages.

### Stage 1 - Diagnosis

Open with:

```md
/export-character <name> 將動態組合角色整合視圖（聲線卡 + 關係 + 時間線 + 弧線 + 出場場景）並寫入 `view/角色_<name>.md` DERIVED 整合檔。本 skill 寫單一靜態整合檔；要更新請重跑本 skill。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- `C-<name>` parameter and entity existence check
- `view/` directory availability check

For missing blocking prerequisites, stop before reading all source content.

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
   - `version`
   - `entities` observed when present

For relationship extraction, match both directions:

- `R-<name>-*`
- `R-*-<name>`

For scene appearances, use D-054-compatible scene-index discovery:

1. Scan `06_scene_index/06_a_場景索引模板.md` for rows or adjacent detail blocks that mention `C-<name>` or the display name.
2. Scan existing `06_scene_index/CH<n>_S<m>_<scene_name>.md` files for frontmatter or body references to `C-<name>`.
3. List matched scene IDs once. If a per-scene file and an aggregate row describe the same scene, prefer the per-scene file as the displayed source and note that aggregate `06_a` also indexed the scene.
4. Do not read downstream `07_scene_tasks/`, `08_dialogue_outputs/`, or `09_quality_assurance/` files.

### Stage 3 - Assemble, Breadcrumb, and Conditional TOC In Memory

Assemble a single Markdown document in memory before writing it to disk.

Frontmatter discipline:

- Use Chinese header extension fields `生成方式` and `組合來源`.
- Do not add the standard `entities` / `depends_on` / `weight` YAML block to the `DERIVED` file.
- Set `版本` to the highest version observed across usable sources.
- Set `最後更新` to the runtime date in `YYYY-MM-DD`.
- Keep `生成方式` fixed as `/export-character`.

Use this structure:

```md
狀態：DERIVED
版本：<對應 source 的最高版本>
最後更新：<執行時的日期 YYYY-MM-DD>
適用範圍：角色 <name> 整合視圖
優先級：中
生成方式：/export-character
組合來源：
  - 03_characters/<scope>/<name>_聲線卡.md
  - 04_relationships/04_a_角色關係矩陣.md
  - 04_relationships/04_b_關係變化時間線.md
  - 05_plot/05_c_角色弧線表.md
  - 06_scene_index/06_a_場景索引模板.md

> 專案首頁 / 角色 / <name> / 完整視圖

## 目錄 / Contents

<僅當預估 > 200 行時插入；含 GFM auto slug；skill 內驗證 slug 一致性 — P-005>

# 角色：<name> — /export-character 靜態整合檔

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

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If a source body exists but the requested character has no relevant slice, print an italic empty-state sentence explaining that no matching entry was found.
- If a partial source is missing, print `[source 缺漏]` in that source position and keep assembling the rest.
- Add breadcrumb after frontmatter and before any TOC or first `#` heading.
- Add TOC only when the estimated integration file exceeds 200 lines.

### Stage 4 - Write `view/角色_<name>.md`

Write the assembled Markdown to `<instance_root>/view/角色_<name>.md`.

Write discipline:

- If `view/` does not exist, create it.
- If `view/角色_<name>.md` already exists, overwrite it. `DERIVED` files are regenerated from source.
- Do not write `view/角色-<name>.md` (hyphenated). Per NEW_REQ_24 Option 1 (11th master frontend cycle, 2026-06-01) the canonical view filename uses an underscore — `角色_<name>.md` — aligning the 5 LOCKED spec (INTEGRATION_CONTRACTS / SPEC / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / ARCHITECTURE). This reverses the original Wave 14 hyphen directive (commit b94f741), which carried no documented rationale.
- Do not update `/view/README.md`; it is manually maintained per DECISIONS_LOG P-004.
- Do not write `export/`; that belongs to Layer 3 Export A1 prompt flow, not this skill.
- On write failure, roll back partial output and do not update `.protocol_version`.

### Stage 5 - Validate and Write `phase_log`

After the file write:

1. Verify the output has Chinese header fields plus `生成方式` and `組合來源`.
2. Verify `狀態：DERIVED` and `生成方式：/export-character`.
3. Verify breadcrumb appears after frontmatter and before the first `#`.
4. If TOC was generated, validate every TOC link slug against the actual `##` / `###` headings using GitHub Flavored Markdown slug rules.
   - Do not add manual `{#anchor}` syntax.
   - If slug mismatch is found, fix the TOC links in the file and revalidate.
5. Verify every source-backed section ends with an italic `來源` line.
6. Verify scene appearances are deduplicated when both `06_a` and per-scene files mention the same scene.
7. Verify the final return link is exactly:

```md
[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

8. Append one `.protocol_version.phase_log` entry as described below.
9. Do not auto-trigger `/status`, `/check-gaps`, `/view-character`, `/iterate-character`, `/iterate-relationship`, or any other skill.

Print the next-step suggestion:

```md
**下一步建議：**
整合檔已寫於 view/角色_<name>.md；修改角色請跑 /iterate-character <name> 後重新 /export-character <name>。
```

## 呈現規則

Follow ARCH §4.2, ARCH §4.3, and UX_SPEC §7.

1. Breadcrumb is required for the exported file:
   - position: after frontmatter, before TOC and before the first `#`
   - exact text: `> 專案首頁 / 角色 / <name> / 完整視圖`
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

This skill must append one `.protocol_version.phase_log` audit entry after `view/角色_<name>.md` has been written and validated.

The entry must not update entity completion, entity status, `created_entities`, `entities_touched`, or any downstream pipeline state.

Required entry shape:

```yaml
- phase: export-character
  date: YYYY-MM-DD
  skill: /export-character
  status: completed
  target_entity: C-<name>
  read_sources:
    - 03_characters/main/<name>_聲線卡.md  # or resolved minor/npc path
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_c_角色弧線表.md
    - 06_scene_index/06_a_場景索引模板.md  # plus per-scene file list when detected
  output_path: view/角色_<name>.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

If the output write succeeds but phase_log write fails, report the audit failure clearly. Do not mark the run as fully completed until the user decides whether to repair `.protocol_version`.

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

Dynamic issue-list loading is not applicable. `/export-character` is read-source / write-DERIVED assembly, not a creation or iteration protocol.

## 輸出

The output is a persistent Markdown file:

- `view/角色_<name>.md`

The file must:

- start with Chinese header fields
- use `狀態：DERIVED`
- include `生成方式：/export-character`
- include `組合來源` listing all source paths used for the character view
- include breadcrumb
- include TOC only when estimated output exceeds 200 lines
- include source references after every source-backed section
- end with the required return link

`DERIVED` files are generated artifacts. Do not hand-edit `view/角色_<name>.md`; update source files through the appropriate creation or iteration skill and rerun `/export-character <name>`.

This skill also writes:

- `.protocol_version.phase_log` audit entry for `phase: export-character`

It writes nothing else.

## 邊界

`/export-character` is a write-file skill that writes exactly one static integration file plus one audit entry. It uses the D-050 / D-053 boundary pattern adapted for `view/` exports.

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
| `view/` | ✅ 寫 | 寫 `view/角色_<name>.md`（DERIVED；本 skill 唯一寫入目錄）|
| `.protocol_version` | ✅ 寫（phase_log entry 追加）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `03_characters/` | ✗ 不寫 | source 唯讀 |
| `04_relationships/` | ✗ 不寫 | source 唯讀 |
| `05_plot/` | ✗ 不寫 | source 唯讀 |
| `06_scene_index/` | ✗ 不寫 | source 唯讀；不觸發 split-to-file |
| `01_world/` / `02_vocabulary/` / `07_scene_tasks/` ~ `09_quality_assurance/` | ✗ 不寫 | 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |
| `export/` | ✗ 不寫 | 屬 §4.2a Layer 3 Export A1 prompt 生成器 scope（separate path；不在本 skill scope）|

**寫 `view/` 目錄以外任何檔 → rollback + 拒絕。**
```

Additional boundaries:

- Do not implement `/export-world`, `/export-outline`, or `/export-detailed-outline`.
- Do not implement §4.2a Layer 3 Export or write `export/<instance>_<timestamp>.{json,md}`.
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates.
- Do not upgrade, downgrade, or otherwise change entity status.
- Do not call `/view-character` or other `/view-*` skills automatically.
- Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
- Do not write `LOCKED` source files.

## 錯誤處理 / Rollback

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- missing or ambiguous character name parameter
- `C-<name>` voice-card source absent
- parser/frontmatter cannot confirm `C-<name>`
- `view/` cannot be created

For these, stop before assembling and writing output.

Partial source failures:

- If `04_a`, `04_b`, `05_c`, or `06_a` is missing, keep the output skeleton and print `[source 缺漏]` in that section.
- If a relationship, timeline, arc, or scene appearance is simply not found for the character, print an italic empty-state sentence instead of inventing content.
- If a per-scene file cannot be opened but `06_a` has a usable row, display the aggregate row and warn that per-scene read failed.

Write failure rollback:

1. Stop further writes.
2. Remove any partially written `view/角色_<name>.md` from the current run when possible.
3. Do not append `.protocol_version.phase_log` if the output file did not validate.
4. Print the failing path and the next repair step.

Slug failure rollback:

- If TOC slug validation fails, fix the TOC links in memory or in the output file, rewrite `view/角色_<name>.md`, and validate again.
- If validation still fails, roll back the file write and stop with an error. Do not append phase_log.

Phase log failure:

- If `view/角色_<name>.md` is valid but `.protocol_version` cannot be updated, do not pretend the run is complete.
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

What: /export-character 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /export-character 需要已完成 Bootstrap 與既有 C-<name> source 才能寫出 DERIVED 整合檔。
下一步: 先執行 /init-project；若尚未建立角色，執行 /create-character <name>。
```

Use this shape for partial source gaps:

```md
### ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏] placeholder 保留整合檔骨架。
Where: <missing source path>
Why: /export-character 不會自行補寫 source，只能整合目前可讀資料。
下一步: 執行 /iterate-character <name> 或 /iterate-relationship <name> <other> 修復缺漏 source，然後重新 /export-character <name>。
```
