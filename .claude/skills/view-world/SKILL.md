---
name: view-world
description: "Read W-rules / V / W-language plus 02_vocabulary and compose an in-chat world view. This skill is read-only, writes no files, and follows ARCH §4.1 dynamic assembly."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/view-world skill runtime instructions
優先級：中

# /view-world Skill

## 用途

Use this skill when the user triggers `/view-world` to dynamically assemble the world-view reading surface from existing source files.

The skill reads:

- `W-rules` from `01_world/01_a_世界觀總覽.md`
- `W-language` from `01_world/01_b_世界語言規格.md` and `01_world/01_c_陣營與階級語言.md`
- `V` from `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, and `02_vocabulary/02_c_禁用詞與慎用詞表.md`
- project-specific anti-AI-flavor baseline from `00_protocol/00_b_反ai味檢查表.md` §1 and §2

This skill prints one combined Markdown view in chat. It does not write `view/` files, does not update entity status, and does not rewrite source wording.

## 觸發語

- `/view-world`
- Chinese alias: `/查看世界觀`, via `.claude/skills/查看世界觀/SKILL.md`

The slash command accepts no user parameters. If extra text follows `/view-world`, ignore it for source selection and assemble the standard world view.

## 觸發協議

There is no corresponding `00_protocol/` file for `/view-world`.

`/view-world` is a pure technical read-only skill. Runtime authority is:

- `_design/TASKS.md` v1.9 §C.3
- `_design/ARCHITECTURE.md` v1.6 §4.1 for dynamic assembly
- `_design/ARCHITECTURE.md` v1.6 §4.3 / §4.4 and `_design/UX_SPEC.md` v0.4 §7 for presentation rules
- `_design/SPEC.md` v1.2 §5.2 for frontmatter and entity metadata

Do not modify, patch, or interpret any `00_protocol/` file while running this skill. `00_protocol/00_b_反ai味檢查表.md` is read only for §1 and §2 source content.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo, not the Template repo.

Required checks:

1. D-049 Template-detect: `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed: `.protocol_version` must exist and include a completed Bootstrap entry.
   - Accept only `phase: bootstrap` with `status: completed`.
3. Core world source families exist at `DRAFT` or above.
   - `W-rules`: `01_world/01_a_世界觀總覽.md` exists, parses, has Chinese header status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `W-rules`.
   - `W-language`: `01_world/01_b_世界語言規格.md` and `01_world/01_c_陣營與階級語言.md` exist, parse, have status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `W-language`.
   - `V`: `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, and `02_vocabulary/02_c_禁用詞與慎用詞表.md` exist, parse, have status `DRAFT`, `REVIEW`, `FINAL`, or `LOCKED`, and frontmatter `entities` includes `V`.
4. Do not require `REVIEW` or higher. `/view-world` is read-any-state and may show `DRAFT` material.
5. Do not run downstream pipeline interlock checks. This skill is read-only and does not affect any active writing workflow.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

If all source files for one required entity family are absent or unusable, stop with a missing-source list and tell the user to run `/create-world`. If a partial source gap is discovered after the required family exists, keep the view layout, insert the `[source 缺漏]` placeholder for that source section, and tell the user to use `/create-world` or `/iterate-world` to repair the source.

## 流程

Run exactly five stages. Keep every stage read-only unless the user has explicitly enabled the optional `.protocol_version.phase_log` audit entry described below.

### Stage 1 - Diagnosis

Open with:

```md
/view-world 將動態組合世界觀整合視圖（W-rules / V / W-language + 02_vocabulary 詞彙系統 + 00_b §1/§2 反 AI 味基線）。本 skill 純讀取，不寫任何檔。執行後在 chat 印出整合視圖。

開始讀取 source...
```

Then perform the startup checks:

- Template marker check
- Bootstrap completed check
- Required entity family source check

For missing prerequisites, stop before reading all source content.

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
   - `entities` observed when present

For `00_b`, extract only §1 and §2. Do not quote or summarize unrelated sections.

### Stage 3 - Assemble In Memory

Assemble a single Markdown document in memory. Do not write it to disk.

Use this structure:

```md
# 世界觀 - /view-world 動態整合視圖

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

**下一步建議：**
- 持久化整合檔 -> /export-world
- 修改世界觀 -> /iterate-world
- 補洞 -> /iterate-world
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

- `view/世界觀.md`
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

Print the next-step suggestions exactly once:

```md
**下一步建議：**
- 持久化整合檔 -> /export-world
- 修改世界觀 -> /iterate-world
- 補洞 -> /iterate-world
```

Do not automatically trigger `/status`, `/check-gaps`, `/export-world`, `/iterate-world`, or any other skill.

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
- phase: view-world
  date: YYYY-MM-DD
  skill: /view-world
  status: completed
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 00_protocol/00_b_反ai味檢查表.md  # §1/§2
  output_lines: <estimated assembled output line count>
  output_target: chat
  customizations: []
```

If the user says view reads are frequent or requests audit-log skip, do not write this optional entry.

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

Dynamic issue-list loading is not applicable. `/view-world` is read-only data assembly, not a creation or iteration protocol.

## 輸出

The output is one chat Markdown view.

This skill writes no persistent integration file. If the user wants a persisted `view/` integration file, tell them to run `/export-world`.

Output must include:

- the assembled world view
- source references after every source-backed section
- the next-step suggestions

## 邊界

`/view-world` is a pure read-only skill. It is strictly limited to:

1. Do not write any file, except the optional `.protocol_version.phase_log` audit entry when explicitly enabled.
2. Do not write a `view/` integration file. That is `/export-world` Wave 14 scope.
3. Do not expand source scope beyond the seven listed sources. Do not add `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, or `_tools/frontend/`.
4. Do not upgrade, downgrade, or otherwise change entity status.
5. Do not call other `/view-*` skills automatically.
6. Do not reorganize source content. Extract verbatim body content and place it under the fixed assembly skeleton.
7. Do not write `LOCKED` status or modify any `LOCKED` source.

Unlike `/create-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, and `/qa`, this skill does not include the D-050 three write-boundary blocks. The governing boundary is this read-only section.

## 錯誤處理 / Rollback

Because `/view-world` is read-only by default, rollback normally means: no source files were changed, no generated files need deletion, and the user can rerun the skill after fixing missing prerequisites.

Blocking prerequisite failures:

- Template repo detected
- Bootstrap missing or incomplete
- required world entity family absent
- parser/frontmatter cannot confirm the required entity family

For these, stop before assembling output.

Partial source failures:

- If one source file is missing but the required entity family still has usable source evidence, keep the output skeleton and print `[source 缺漏]` in that section.
- If `00_b` §1 or §2 cannot be found, keep `## 反 AI 味基線（作品專屬）` and print `[source 缺漏]` for the missing subsection.
- End the affected section with the source line when the file exists; if the file itself is missing, print the intended source path as the location to repair.
- Tell the user to run `/create-world` when the world foundation has not been created, or `/iterate-world` when existing world sources need repair.

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

What: /view-world 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /view-world 需要已完成 Bootstrap 與既有 W-rules / W-language / V source 才能組合視圖。
下一步: 先執行 /init-project；若尚未建立世界觀，執行 /create-world。
```

Use this shape for partial source gaps:

```md
## ⚠ 需注意 / Warning

What: 部分 source 缺漏，已用 [source 缺漏] placeholder 保留視圖骨架。
Where: <missing source path>
Why: /view-world 不會自行補寫 source，只能呈現目前可讀資料。
下一步: 執行 /create-world 或 /iterate-world 修復缺漏 source。
```
