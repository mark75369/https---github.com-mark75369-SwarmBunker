---
name: export-outline
description: "Compose P outline sources from 05_plot into DERIVED view/大綱.md. Same /view-outline logic; writes breadcrumb, optional TOC, source links, and phase_log per ARCH §4.2 while keeping Layer 3 Export separate."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/export-outline skill runtime instructions
優先級：中

# /export-outline Skill

## 用途

Use this skill when the user triggers `/export-outline` to generate a persistent static integration file for the project outline entity `P`.

The skill reads the same source set as `/view-outline`:

- main plot structure from `05_plot/05_a_主線大綱模板.md`
- chapter structure from `05_plot/05_b_章節結構模板.md`
- character arcs from `05_plot/05_c_角色弧線表.md`
- information reveal order from `05_plot/05_d_資訊揭露表.md`
- foreshadowing and payoff entries from `05_plot/05_e_伏筆與回收表.md`

Unlike `/view-outline`, this skill writes the assembled output to `view/大綱.md` with `狀態：DERIVED`, adds static-file navigation, and appends a `.protocol_version.phase_log` audit entry. It does not rewrite source files, does not update entity completion, and does not implement Layer 3 Export.

## 觸發語

- `/export-outline`
- Chinese alias: `/匯出大綱`, via `.claude/skills/匯出大綱/SKILL.md`

The slash command accepts no user parameters. If extra text follows `/export-outline`, ignore it for source selection and export the standard outline view.

## 觸發協議

There is no corresponding `00_protocol/` file for `/export-outline`.

`/export-outline` is a technical export skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.5
- `_design/ARCHITECTURE.md` v1.6 §4.2 for `/export-*` static integration files
- `_design/ARCHITECTURE.md` v1.6 §4.3 and `_design/UX_SPEC.md` v0.4 §7 for navigation and source-link rules
- `_design/SPEC.md` v1.2 §5.2, §13.4, and §16 for frontmatter, static integration files, and `DERIVED`
- `.claude/skills/view-outline/SKILL.md` v0.1 for shared outline-view source assembly logic
- `_design/DECISIONS_LOG.md` v2.0 P-004, P-005, §6.12.2 D-050, and §6.16.2 D-053

Do not modify, patch, or interpret any `00_protocol/` file while running this skill.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo; tell the user to run `/init-project` in a real Instance.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. Plot entity `P` must exist at `DRAFT` or above.
   - `05_plot/05_a_主線大綱模板.md` must exist, parse, have Chinese header status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` should include `P`.
4. `view/` must exist or be creatable.
   - If `view/` does not exist, create it during Stage 4.
   - If the directory cannot be created, stop before composing output.
5. Do not require `REVIEW` or higher. `/export-outline` is read-any-state and may export `DRAFT` material.
6. Do not run downstream pipeline interlock checks. This skill is read-source / write-DERIVED and does not affect active writing workflows.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If `P` cannot be found, stop with a missing-source list and tell the user to run `/create-outline`. After `P` exists, missing `05_b`, `05_c`, `05_d`, or `05_e` content is non-blocking; keep the export layout and insert `[source 缺漏]` or an empty-state sentence for that section.

## 流程

Run exactly five stages.

### Stage 1 - Diagnosis

Open with:

```md
/export-outline 將動態組合大綱整合視圖（主線結構 + 章節結構 + 角色弧線 + 資訊揭露 + 伏筆與回收）並寫入 `view/大綱.md` DERIVED 整合檔。本 skill 寫單一靜態整合檔；要更新請重跑本 skill。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- `P` entity source check
- `view/` directory availability check

For missing blocking prerequisites, stop before reading all source content.

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
   - `version`
   - `entities` observed when present

Do not read `06_scene_index/` scene details. Scene-level detail belongs to `/export-detailed-outline`.

### Stage 3 - Assemble, Breadcrumb, and Conditional TOC In Memory

Assemble a single Markdown document in memory before writing it to disk.

Frontmatter discipline:

- Use Chinese header extension fields `生成方式` and `組合來源`.
- Do not add the standard `entities` / `depends_on` / `weight` YAML block to the `DERIVED` file.
- Set `版本` to the highest version observed across usable sources.
- Set `最後更新` to the runtime date in `YYYY-MM-DD`.
- Keep `生成方式` fixed as `/export-outline`.

Use this structure:

```md
狀態：DERIVED
版本：<對應 source 的最高版本>
最後更新：<執行時的日期 YYYY-MM-DD>
適用範圍：大綱整合視圖
優先級：中
生成方式：/export-outline
組合來源：
  - 05_plot/05_a_主線大綱模板.md
  - 05_plot/05_b_章節結構模板.md
  - 05_plot/05_c_角色弧線表.md
  - 05_plot/05_d_資訊揭露表.md
  - 05_plot/05_e_伏筆與回收表.md

> 專案首頁 / 大綱 / 完整視圖

## 目錄 / Contents

<僅當預估 > 200 行時插入；含 GFM auto slug；skill 內驗證 slug 一致性 — P-005>

# 大綱 — /export-outline 靜態整合檔

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

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If a source body is empty, print an italic empty-state sentence explaining that the source exists but has no content to show.
- If a partial source is missing, print `[source 缺漏]` in that source position and keep assembling the rest.
- Add breadcrumb after frontmatter and before any TOC or first `#` heading.
- Add TOC only when the estimated integration file exceeds 200 lines.

### Stage 4 - Write `view/大綱.md`

Write the assembled Markdown to `<instance_root>/view/大綱.md`.

Write discipline:

- If `view/` does not exist, create it.
- If `view/大綱.md` already exists, overwrite it. `DERIVED` files are regenerated from source.
- Do not update `/view/README.md`; it is manually maintained per DECISIONS_LOG P-004.
- Do not write `export/`; that belongs to Layer 3 Export A1 prompt flow, not this skill.
- On write failure, roll back partial output and do not update `.protocol_version`.

### Stage 5 - Validate and Write `phase_log`

After the file write:

1. Verify the output has Chinese header fields plus `生成方式` and `組合來源`.
2. Verify `狀態：DERIVED` and `生成方式：/export-outline`.
3. Verify breadcrumb appears after frontmatter and before the first `#`.
4. If TOC was generated, validate every TOC link slug against the actual `##` / `###` headings using GitHub Flavored Markdown slug rules.
   - Do not add manual `{#anchor}` syntax.
   - If slug mismatch is found, fix the TOC links in the file and revalidate.
5. Verify every source-backed section ends with an italic `來源` line.
6. Verify no scene-level detail from `06_scene_index/` was pulled into the outline view.
7. Verify the final return link is exactly:

```md
[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

8. Append one `.protocol_version.phase_log` entry as described below.
9. Do not auto-trigger `/status`, `/check-gaps`, `/view-outline`, `/iterate-outline`, `/iterate-detailed-outline`, or any other skill.

Print the next-step suggestion:

```md
**下一步建議：**
整合檔已寫於 view/大綱.md；修改主線請跑 /iterate-outline 後重新 /export-outline。
```

## 呈現規則

Follow ARCH §4.2, ARCH §4.3, and UX_SPEC §7.

1. Breadcrumb is required for the exported file:
   - position: after frontmatter, before TOC and before the first `#`
   - exact text: `> 專案首頁 / 大綱 / 完整視圖`
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

This skill must append one `.protocol_version.phase_log` audit entry after `view/大綱.md` has been written and validated.

The entry must not update entity completion, entity status, `created_entities`, `entities_touched`, or any downstream pipeline state.

Required entry shape:

```yaml
- phase: export-outline
  date: YYYY-MM-DD
  skill: /export-outline
  status: completed
  target_entity: P
  read_sources:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_c_角色弧線表.md
    - 05_plot/05_d_資訊揭露表.md
    - 05_plot/05_e_伏筆與回收表.md
  output_path: view/大綱.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

If the output write succeeds but phase_log write fails, report the audit failure clearly. Do not mark the run as fully completed until the user decides whether to repair `.protocol_version`.

## 輸入

The skill accepts no user parameters.

Runtime inputs are fixed:

- `.protocol_version`
- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_b_章節結構模板.md`
- `05_plot/05_c_角色弧線表.md`
- `05_plot/05_d_資訊揭露表.md`
- `05_plot/05_e_伏筆與回收表.md`

Dynamic issue-list loading is not applicable. `/export-outline` is read-source / write-DERIVED assembly, not a creation or iteration protocol.

## 輸出

The output is a persistent Markdown file:

- `view/大綱.md`

The file must:

- start with Chinese header fields
- use `狀態：DERIVED`
- include `生成方式：/export-outline`
- include `組合來源` listing all source paths
- include breadcrumb
- include TOC only when estimated output exceeds 200 lines
- include source references after every source-backed section
- end with the required return link

`DERIVED` files are generated artifacts. Do not hand-edit `view/大綱.md`; update source files through the appropriate creation or iteration skill and rerun `/export-outline`.

This skill also writes:

- `.protocol_version.phase_log` audit entry for `phase: export-outline`

It writes nothing else.

## 邊界

`/export-outline` is a write-file skill that writes exactly one static integration file plus one audit entry. It uses the D-050 / D-053 boundary pattern adapted for `view/` exports.

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
| `view/` | ✅ 寫 | 寫 `view/大綱.md`（DERIVED；本 skill 唯一寫入目錄）|
| `.protocol_version` | ✅ 寫（phase_log entry 追加）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `05_plot/` | ✗ 不寫 | source 唯讀 |
| `01_world/` ~ `04_relationships/` | ✗ 不寫 | 不在本 skill scope |
| `06_scene_index/` ~ `09_quality_assurance/` | ✗ 不寫 | 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |
| `export/` | ✗ 不寫 | 屬 §4.2a Layer 3 Export A1 prompt 生成器 scope（separate path；不在本 skill scope）|

**寫 `view/` 目錄以外任何檔 → rollback + 拒絕。**
```

Additional boundaries:

- Do not implement `/export-world`, `/export-character`, or `/export-detailed-outline`.
- Do not implement §4.2a Layer 3 Export or write `export/<instance>_<timestamp>.{json,md}`.
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates.
- Do not upgrade, downgrade, or otherwise change entity status.
- Do not call `/view-outline` or other `/view-*` skills automatically.
- Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
- Do not write `LOCKED` source files.

## 錯誤處理 / Rollback

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- `P` source absent
- parser/frontmatter cannot confirm `P`
- `view/` cannot be created

For these, stop before assembling and writing output.

Partial source failures:

- If `05_b`, `05_c`, `05_d`, or `05_e` is missing after `P` exists, keep the output skeleton and print `[source 缺漏]` in that section.
- If a source body is empty, print an italic empty-state sentence instead of inventing content.
- Tell the user to run `/create-outline` when the outline foundation has not been created, `/iterate-outline` when existing outline sources need repair, or `/iterate-detailed-outline` when chapter-level sources need repair.

Write failure rollback:

1. Stop further writes.
2. Remove any partially written `view/大綱.md` from the current run when possible.
3. Do not append `.protocol_version.phase_log` if the output file did not validate.
4. Print the failing path and the next repair step.

Slug failure rollback:

- If TOC slug validation fails, fix the TOC links in memory or in the output file, rewrite `view/大綱.md`, and validate again.
- If validation still fails, roll back the file write and stop with an error. Do not append phase_log.

Phase log failure:

- If `view/大綱.md` is valid but `.protocol_version` cannot be updated, do not pretend the run is complete.
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

What: /export-outline 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /export-outline 需要已完成 Bootstrap 與既有 P source 才能寫出 DERIVED 整合檔。
下一步: 先執行 /init-project；若尚未建立主線大綱，執行 /create-outline。
```

Use this shape for partial source gaps:

```md
### ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏] placeholder 保留整合檔骨架。
Where: <missing source path>
Why: /export-outline 不會自行補寫 source，只能整合目前可讀資料。
下一步: 執行 /iterate-outline 或 /iterate-detailed-outline 修復缺漏 source，然後重新 /export-outline。
```
