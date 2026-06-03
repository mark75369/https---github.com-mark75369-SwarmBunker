---
name: export-world
description: "Compose W-rules / V / W-language, vocabulary, and 00_b §1/§2 into DERIVED view/世界觀.md. Same /view-world logic; writes breadcrumb, optional TOC, source links, and phase_log per ARCH §4.2."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/export-world skill runtime instructions
優先級：中

# /export-world Skill

## 用途

Use this skill when the user triggers `/export-world` to generate a persistent static integration file for the project world view.

The skill reads the same source set as `/view-world`:

- `W-rules` from `01_world/01_a_世界觀總覽.md`
- `W-language` from `01_world/01_b_世界語言規格.md` and `01_world/01_c_陣營與階級語言.md`
- `V` from `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, and `02_vocabulary/02_c_禁用詞與慎用詞表.md`
- project-specific anti-AI-flavor baseline from `00_protocol/00_b_反ai味檢查表.md` §1 and §2

Unlike `/view-world`, this skill writes the assembled output to `view/世界觀.md` with `狀態：DERIVED`, adds static-file navigation, and appends a `.protocol_version.phase_log` audit entry. It does not rewrite source files, does not update entity completion, and does not implement Layer 3 Export.

## 觸發語

- `/export-world`
- Chinese alias: `/匯出世界觀`, via `.claude/skills/匯出世界觀/SKILL.md`

The slash command accepts no user parameters. If extra text follows `/export-world`, ignore it for source selection and export the standard world view.

## 觸發協議

There is no corresponding `00_protocol/` file for `/export-world`.

`/export-world` is a technical export skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.5
- `_design/ARCHITECTURE.md` v1.6 §4.2 for `/export-*` static integration files
- `_design/ARCHITECTURE.md` v1.6 §4.3 and `_design/UX_SPEC.md` v0.4 §7 for navigation and source-link rules
- `_design/SPEC.md` v1.2 §5.2, §13.4, and §16 for frontmatter, static integration files, and `DERIVED`
- `.claude/skills/view-world/SKILL.md` v0.1 for shared world-view source assembly logic
- `_design/DECISIONS_LOG.md` v2.0 P-004, P-005, §6.12.2 D-050, and §6.16.2 D-053

Do not modify, patch, or interpret any `00_protocol/` file while running this skill. `00_protocol/00_b_反ai味檢查表.md` is read only for §1 and §2 source content.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo; tell the user to run `/init-project` in a real Instance.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. Core world source families exist at `DRAFT` or above.
   - `W-rules`: `01_world/01_a_世界觀總覽.md` exists, parses, has Chinese header status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `W-rules`.
   - `W-language`: `01_world/01_b_世界語言規格.md` and `01_world/01_c_陣營與階級語言.md` exist or the missing section can be represented as a partial source gap; usable files must parse, have status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `W-language`.
   - `V`: `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, and `02_vocabulary/02_c_禁用詞與慎用詞表.md` exist or the missing section can be represented as a partial source gap; usable files must parse, have status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `V`.
4. `view/` exists or can be created.
   - If `view/` does not exist, create it during Stage 4.
   - If the directory cannot be created, stop before composing output.
5. Do not require `REVIEW` or higher. `/export-world` is read-any-state and may export `DRAFT` material.
6. Do not run downstream pipeline interlock checks. This skill is read-source / write-DERIVED and does not affect active writing workflows.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If all source files for one required entity family are absent or unusable, stop with a missing-source list and tell the user to run `/create-world`. If a partial source gap is discovered after the required family exists, keep the export layout, insert `[source 缺漏 — 跑 /create-world 或 /iterate-world 補]` for that source section, and tell the user to use `/create-world` or `/iterate-world` to repair the source.

## 流程

Run exactly five stages.

### Stage 1 - Diagnosis

Open with:

```md
/export-world 將動態組合世界觀整合視圖（W-rules / V / W-language + 02_vocabulary 詞彙系統 + 00_b §1/§2 反 AI 味基線）並寫入 `view/世界觀.md` DERIVED 整合檔。本 skill 寫單一靜態整合檔；要更新請重跑本 skill。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- required entity family source check
- `view/` directory availability check

For missing blocking prerequisites, stop before reading all source content.

### Stage 2 - Source Backtrace

Read source files in this exact order:

| Source | Content | Output position |
|---|---|---|
| `01_world/01_a_世界觀總覽.md` | `W-rules` main split | `## 世界規則` |
| `01_world/01_b_世界語言規格.md` | `W-language` main split | `## 世界語言` |
| `01_world/01_c_陣營與階級語言.md` | `W-language` extension | `## 陣營與階級語言` |
| `02_vocabulary/02_a_專有名詞表.md` | `V` proper nouns | `### 專有名詞` |
| `02_vocabulary/02_b_俗稱與黑話表.md` | `V` slang | `### 俗稱與黑話` |
| `02_vocabulary/02_c_禁用詞與慎用詞表.md` | `V` forbidden and cautious words | `### 禁用詞與慎用詞` |
| `00_protocol/00_b_反ai味檢查表.md` §1 / §2 | Project-specific anti-AI-flavor baseline | `## 反 AI 味基線（作品專屬）` |

For each source:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Verify the expected entity for `01_world/` and `02_vocabulary/` files.
4. For `00_protocol/00_b_反ai味檢查表.md`, do not require `entities`; protocol files may omit YAML.
5. Extract main content only:
   - skip YAML frontmatter
   - skip the Chinese five-field header
   - preserve the remaining source text verbatim
6. Record the extracted line range for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `version`
   - `entities` observed when present

For `00_b`, extract only §1 and §2. Do not quote, summarize, or include unrelated sections.

### Stage 3 - Assemble, Breadcrumb, and Conditional TOC In Memory

Assemble a single Markdown document in memory before writing it to disk.

Frontmatter discipline:

- Use Chinese header extension fields `生成方式` and `組合來源`.
- Do not add the standard `entities` / `depends_on` / `weight` YAML block to the `DERIVED` file.
- Set `版本` to the highest version observed across usable sources.
- Set `最後更新` to the runtime date in `YYYY-MM-DD`.
- Keep `生成方式` fixed as `/export-world`.

Use this structure:

```md
狀態：DERIVED
版本：<對應 source 的最高版本>
最後更新：<執行時的日期 YYYY-MM-DD>
適用範圍：世界觀整合視圖
優先級：中
生成方式：/export-world
組合來源：
  - 01_world/01_a_世界觀總覽.md
  - 01_world/01_b_世界語言規格.md
  - 01_world/01_c_陣營與階級語言.md
  - 02_vocabulary/02_a_專有名詞表.md
  - 02_vocabulary/02_b_俗稱與黑話表.md
  - 02_vocabulary/02_c_禁用詞與慎用詞表.md
  - 00_protocol/00_b_反ai味檢查表.md

> 專案首頁 / 世界觀 / 完整視圖

## 目錄 / Contents

<僅當預估 > 200 行時插入；含 GFM auto slug；skill 內驗證 slug 一致性 — P-005>

# 世界觀 — /export-world 靜態整合檔

## 世界規則

<01_world/01_a content>

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md)*

## 世界語言

<01_world/01_b content>

*來源：[/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md)*

## 陣營與階級語言

<01_world/01_c content>

*來源：[/01_world/01_c_陣營與階級語言.md](/01_world/01_c_陣營與階級語言.md)*

## 詞彙系統

### 專有名詞

<02_vocabulary/02_a content>

*來源：[/02_vocabulary/02_a_專有名詞表.md](/02_vocabulary/02_a_專有名詞表.md)*

### 俗稱與黑話

<02_vocabulary/02_b content>

*來源：[/02_vocabulary/02_b_俗稱與黑話表.md](/02_vocabulary/02_b_俗稱與黑話表.md)*

### 禁用詞與慎用詞

<02_vocabulary/02_c content>

*來源：[/02_vocabulary/02_c_禁用詞與慎用詞表.md](/02_vocabulary/02_c_禁用詞與慎用詞表.md)*

## 反 AI 味基線（作品專屬）

<00_b §1 content>

<00_b §2 content>

*來源：[/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1 / §2*

---

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

Assembly rules:

- Use the fixed section skeleton above.
- Preserve source body text verbatim after removing only source frontmatter and the Chinese five-field header.
- Do not summarize, simplify, reword, reorder, or normalize source content.
- If a source body exists but is empty, print an italic empty-state sentence explaining that the source exists but has no content to show.
- If a partial source file is missing, print `[source 缺漏 — 跑 /create-world 或 /iterate-world 補]` in that source position and keep assembling the rest.
- Add breadcrumb after frontmatter and before any TOC or first `#` heading.
- Add TOC only when the estimated integration file exceeds 200 lines.

### Stage 4 - Write `view/世界觀.md`

Write the assembled Markdown to `<instance_root>/view/世界觀.md`.

Write discipline:

- If `view/` does not exist, create it.
- If `view/世界觀.md` already exists, overwrite it. `DERIVED` files are regenerated from source.
- Do not write any other `view/<entity>.md`.
- Do not update `/view/README.md`; it is manually maintained per DECISIONS_LOG P-004.
- Do not write `export/`; that belongs to Layer 3 Export A1 prompt flow, not this skill.
- On write failure, roll back partial output and do not update `.protocol_version`.

### Stage 5 - Validate and Write `phase_log`

After the file write:

1. Verify the output has Chinese header fields plus `生成方式` and `組合來源`.
2. Verify `狀態：DERIVED` and `生成方式：/export-world`.
3. Verify breadcrumb appears after frontmatter and before the first `#`.
4. If TOC was generated, validate every TOC link slug against the actual `##` / `###` headings using GitHub Flavored Markdown slug rules.
   - Do not add manual `{#anchor}` syntax.
   - If slug mismatch is found, fix the TOC links in the file and revalidate.
5. Verify every source-backed section ends with an italic `來源` line.
6. Verify the final return link is exactly:

```md
[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

7. Append one `.protocol_version.phase_log` entry as described below.
8. Do not auto-trigger `/status`, `/check-gaps`, `/view-world`, `/iterate-world`, or any other skill.

Print the next-step suggestion:

```md
**下一步建議：**
整合檔已寫於 view/世界觀.md；要修改世界觀請跑 /iterate-world 後重新 /export-world。
```

## 呈現規則

Follow ARCH §4.2, ARCH §4.3, and UX_SPEC §7.

1. Breadcrumb is required for the exported file:
   - position: after frontmatter, before TOC and before the first `#`
   - exact text: `> 專案首頁 / 世界觀 / 完整視圖`
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

This skill must append one `.protocol_version.phase_log` audit entry after `view/世界觀.md` has been written and validated.

The entry must not update entity completion, entity status, `created_entities`, `entities_touched`, or any downstream pipeline state.

Required entry shape:

```yaml
- phase: export-world
  date: YYYY-MM-DD
  skill: /export-world
  status: completed
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 00_protocol/00_b_反ai味檢查表.md  # §1/§2
  output_path: view/世界觀.md
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
- `01_world/01_a_世界觀總覽.md`
- `01_world/01_b_世界語言規格.md`
- `01_world/01_c_陣營與階級語言.md`
- `02_vocabulary/02_a_專有名詞表.md`
- `02_vocabulary/02_b_俗稱與黑話表.md`
- `02_vocabulary/02_c_禁用詞與慎用詞表.md`
- `00_protocol/00_b_反ai味檢查表.md` §1 and §2

Dynamic issue-list loading is not applicable. `/export-world` is read-source / write-DERIVED assembly, not a creation or iteration protocol.

## 輸出

The output is a persistent Markdown file:

- `view/世界觀.md`

The file must:

- start with Chinese header fields
- use `狀態：DERIVED`
- include `生成方式：/export-world`
- include `組合來源` listing all source paths
- include breadcrumb
- include TOC only when estimated output exceeds 200 lines
- include source references after every source-backed section
- end with the required return link

`DERIVED` files are generated artifacts. Do not hand-edit `view/世界觀.md`; update source files through the appropriate creation or iteration skill and rerun `/export-world`.

This skill also writes:

- `.protocol_version.phase_log` audit entry for `phase: export-world`

It writes nothing else.

## 邊界

`/export-world` is a write-file skill that writes exactly one static integration file plus one audit entry. It uses the D-050 / D-053 boundary pattern adapted for `view/` exports.

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
| `view/` | ✅ 寫 | 寫 `view/世界觀.md`（DERIVED；本 skill 唯一寫入目錄）|
| `.protocol_version` | ✅ 寫（phase_log entry 追加）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `01_world/` | ✗ 不寫 | source 唯讀 |
| `02_vocabulary/` | ✗ 不寫 | source 唯讀 |
| `03_characters/` ~ `09_quality_assurance/` | ✗ 不寫 | 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |
| `export/` | ✗ 不寫 | 屬 §4.2a Layer 3 Export A1 prompt 生成器 scope（separate path；不在本 skill scope）|

**寫 `view/` 目錄以外任何檔 → rollback + 拒絕。**
```

Additional boundaries:

- Do not implement `/export-character`, `/export-outline`, or `/export-detailed-outline`.
- Do not implement §4.2a Layer 3 Export or write `export/<instance>_<timestamp>.{json,md}`.
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates.
- Do not upgrade, downgrade, or otherwise change entity status.
- Do not call `/view-world` or other `/view-*` skills automatically.
- Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
- Do not write `LOCKED` source files.

## 錯誤處理 / Rollback

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- all files for a required world entity family are absent or unusable
- parser/frontmatter cannot confirm a required entity family
- `view/` cannot be created

For these, stop before assembling and writing output.

Partial source failures:

- If one source file is missing but the required entity family still has usable source evidence, keep the output skeleton and print `[source 缺漏 — 跑 /create-world 或 /iterate-world 補]` in that section.
- If `00_b` §1 or §2 cannot be found, keep `## 反 AI 味基線（作品專屬）` and print the same placeholder for the missing subsection.
- End the affected section with the source line when the file exists; if the file itself is missing, print the intended source path as the location to repair.

Write failure rollback:

1. Stop further writes.
2. Remove any partially written `view/世界觀.md` from the current run when possible.
3. Do not append `.protocol_version.phase_log` if the output file did not validate.
4. Print the failing path and the next repair step.

Slug failure rollback:

- If TOC slug validation fails, fix the TOC links in memory or in the output file, rewrite `view/世界觀.md`, and validate again.
- If validation still fails, roll back the file write and stop with an error. Do not append phase_log.

Phase log failure:

- If `view/世界觀.md` is valid but `.protocol_version` cannot be updated, do not pretend the run is complete.
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

What: /export-world 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /export-world 需要已完成 Bootstrap 與既有 W-rules / W-language / V source 才能寫出 DERIVED 整合檔。
下一步: 先執行 /init-project；若尚未建立世界觀，執行 /create-world。
```

Use this shape for partial source gaps:

```md
### ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏 — 跑 /create-world 或 /iterate-world 補] placeholder 保留整合檔骨架。
Where: <missing source path>
Why: /export-world 不會自行補寫 source，只能整合目前可讀資料。
下一步: 執行 /create-world 或 /iterate-world 修復缺漏 source，然後重新 /export-world。
```
