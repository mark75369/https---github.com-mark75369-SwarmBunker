---
name: diagnose
description: "Run 00_a §3.3 diagnostic mode across an Instance repo, a supplied file, or pasted text. This skill performs cross-file diagnosis only: it analyzes gaps, contradictions, style fit, and rule adaptability; prints the six-section diagnostic report in chat; and writes no files except an optional phase_log audit entry."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：/diagnose skill runtime instructions
優先級：中

# /diagnose Skill

## 用途

Use this skill when the user triggers `/diagnose` and wants the `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode applied to the current Instance, one source file, or a pasted excerpt.

`/diagnose` is a cross-file diagnostic surface. It finds missing evidence, unresolved TODO / INFERENCE / CONFLICT markers, stale or orphaned references, rule-fit risks, and questions that need human confirmation. It does not organize material into formal templates, does not rewrite source, and does not create `view/` or export files.

The output is always one chat Markdown diagnostic report using the six sections from `00_a` §3.3.4.

## 觸發語

- `/diagnose`
- `/diagnose <file_path>`
- `/diagnose <inline text>`
- Chinese alias: `/診斷`, via `.claude/skills/診斷/SKILL.md`

If no parameter is provided, scan broadly across the initialized Instance. If a repo-relative file path is provided, diagnose that file plus its frontmatter dependency chain. If inline text is provided, diagnose only the pasted text and do not treat it as confirmed Instance canon.

## 觸發協議

The governing protocol is `00_protocol/00_a_台詞生產協議.md` §3.3 診斷模式.

Runtime authority:

- `_design/TASKS.md` v1.9 §C.6 for `/diagnose` / `/integrate` task scope
- `00_protocol/00_a_台詞生產協議.md` v0.1 §3.3, especially §3.3.1-§3.3.4
- `_design/ARCHITECTURE.md` v1.6 §3.3, §3.3.1, §3.3.2, §3.4, and §4.3
- `_design/SPEC.md` v1.2 §5.2, §5.4, and §5.4a
- `_design/UX_SPEC.md` v0.4 §7
- `scripts/parse_frontmatter.py` when repo scanning or single-file frontmatter parsing is needed

`/diagnose` is the Phase D runtime implementation of `00_a` §3.3. It must not modify `00_a`, `00_b`, `00_c`, any `00_protocol/` file, any LOCKED spec, any registry, any parser code, or any existing skill.

Dynamic issue-list registry loading is not applicable. `/diagnose` is a general diagnostic mode and is not bound to a specific issue registry.

## 啟動前檢查

Before Stage 1, confirm the current folder is an initialized Instance repo.

Required checks:

1. D-049 / D-051 Template-detect:
   - `.template_root` must not exist at repo root.
   - If `.template_root` exists, stop. This is a Template repo.
2. Bootstrap completed:
   - `.protocol_version` must exist.
   - `.protocol_version.phase_log` must contain `phase: bootstrap` with `status: completed`.
3. Parser availability for repo or file mode:
   - `scripts/parse_frontmatter.py` should be used when frontmatter must be parsed.
   - If parser import fails, stop for repo-wide or file-path mode; do not replace it with ad hoc parsing.
4. No entity prerequisite:
   - Do not require any W / V / C / R / P / CH / S / A entity to exist.
   - `/diagnose` is valid immediately after Bootstrap and is suitable for initial reading.
5. No downstream interlock:
   - Do not check task/dialogue/QA pipeline locks before running.
   - This skill is read-only and must not affect an active writing workflow.

If Template detection or Bootstrap fails, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met`.

## 流程

Run exactly five stages. Keep every stage read-only unless the user has explicitly enabled the optional `.protocol_version.phase_log` audit entry described below.

### Stage 1 - Diagnostic Setup

Open with:

```md
/diagnose 將跨檔分析 Instance 資料，輸出 6 段診斷報告（對齊 00_protocol/00_a §3.3.4 格式）：作品類型與敘事氣質 / 世界語言與台詞風格推測 / 目前資料可確認的內容 / 不可確認或需人類確認的內容 / 通用規則適配性 / 建議下一步。本 skill 純讀取，不寫任何檔（除可選 phase_log audit entry）。

開始讀取 source...
```

Then:

1. Run the startup checks.
2. Determine mode:
   - Mode A: no parameter -> broad Instance scan.
   - Mode B: `<file_path>` -> single-file diagnosis plus related dependency chain.
   - Mode C: `<inline text>` -> inline-only diagnosis.
3. For broad scans, exclude `DEPRECATED` files unless the user explicitly asks to inspect them.
4. Do not start any other skill while diagnosing.

### Stage 2 - Source Backtrace

Use the source strategy that matches the trigger mode.

#### Mode A - Broad Instance Scan

Read these source families when present. Missing sources are warnings, not automatic blockers.

| Source | Content | Diagnostic report position |
|---|---|---|
| `01_world/01_a_世界觀總覽.md` | W-rules main source | 一、作品類型與敘事氣質 / 二、世界語言與台詞風格推測 |
| `01_world/01_b_世界語言規格.md` + `01_world/01_c_陣營與階級語言.md` | W-language | 二、世界語言與台詞風格推測 |
| `02_vocabulary/02_a_專有名詞表.md`, `02_vocabulary/02_b_俗稱與黑話表.md`, `02_vocabulary/02_c_禁用詞與慎用詞表.md` | V vocabulary system | 二、世界語言與台詞風格推測 / 三、目前資料可確認的內容 |
| `03_characters/**.md` | C-* voice cards and character materials | 三、目前資料可確認的內容 |
| `04_relationships/04_a_角色關係矩陣.md` + `04_relationships/04_b_關係變化時間線.md` | R-*-* relationship evidence | 三、目前資料可確認的內容 |
| `05_plot/05_a_主線大綱模板.md` through `05_plot/05_e_伏筆與回收表.md` | P / CH-* outline evidence | 三、目前資料可確認的內容 |
| `00_protocol/00_b_反ai味檢查表.md` §1 / §2 | Project-specific anti-AI-flavor baseline | 五、通用規則適配性 |
| `00_protocol/00_a_台詞生產協議.md` §2 / §3.3 and `00_protocol/00_c_台詞輸出格式.md` | General dialogue and format rules | 五、通用規則適配性 |

Also scan parsed Markdown source text for literal markers:

- `TODO:`
- `INFERENCE:`
- `CONFLICT:`

Record at least the first five occurrences of each marker type for the report. Keep the marker text faithful; do not reinterpret it as a resolved decision.

When `scripts/parse_frontmatter.build_repo_index(".")` is available, use it for broad frontmatter scan and expected-entity evidence. Treat parser ERRORs as diagnostic evidence and report the first five in section four instead of silently ignoring them.

#### Mode B - File Path Diagnosis

Read only:

1. The requested repo-relative file.
2. Files referenced by its YAML `depends_on` list.
3. Files whose YAML `entities` list overlaps the requested file's `entities`, when needed to explain contradiction or missing context.
4. `00_protocol/00_a_台詞生產協議.md` §3.3 for output discipline.

Do not broaden to a whole-repo scan unless the user explicitly changes the request.

If the requested file is `DEPRECATED`, warn that it is deprecated and continue only because the user explicitly supplied that path.

#### Mode C - Inline Text Diagnosis

Use only:

1. The user's pasted text.
2. `00_protocol/00_a_台詞生產協議.md` §3.3 for output discipline.

Do not infer that inline text is confirmed Instance canon. In section three, print:

```md
[本次屬 inline text 診斷；無 Instance 資料參照]
```

#### Per-Source Extraction Rules

For every Markdown source that is read:

1. Parse the Chinese five-field header.
2. Parse the YAML block when present.
3. Extract body content after skipping:
   - the YAML frontmatter at file top, if present
   - the Chinese five-field header
4. Preserve source wording in evidence notes. Do not rewrite the source into formal canon.
5. Record source path and extracted line range for audit use:
   - `source_path`
   - `start_line`
   - `end_line`
   - `status`
   - `entities`
   - `depends_on`

### Stage 3 - Assemble Diagnostic Report In Memory

Assemble one Markdown report in memory. Do not write it to disk.

Use this exact six-section skeleton from `00_a` §3.3.4, with source italic lines added:

```md
# 診斷報告

## 一、作品類型與敘事氣質

<依 source 分析：作品類型、敘事氣質、已確認 evidence、仍屬推測的判斷。不得把推測寫成已確認設定。>

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md), [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1*

## 二、世界語言與台詞風格推測

<依 W-language / V / 00_b §2 分析語彙、稱呼、階級語言、髒話尺度、台詞美學需求。INFERENCE 必須明示。>

*來源：[/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md), [/01_world/01_c_陣營與階級語言.md](/01_world/01_c_陣營與階級語言.md), [/02_vocabulary/02_a_專有名詞表.md](/02_vocabulary/02_a_專有名詞表.md), [/02_vocabulary/02_b_俗稱與黑話表.md](/02_vocabulary/02_b_俗稱與黑話表.md), [/02_vocabulary/02_c_禁用詞與慎用詞表.md](/02_vocabulary/02_c_禁用詞與慎用詞表.md), [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §2*

## 三、目前資料可確認的內容

依現有 source 列出可確認的設定：

- **角色：** <掃 `03_characters/` 列出已建 C-*；缺漏時印 source placeholder>
- **關係：** <掃 `04_relationships/04_a_角色關係矩陣.md` / `04_relationships/04_b_關係變化時間線.md` 列出已建 R-*-*>
- **主線結構：** <掃 `05_plot/05_a_主線大綱模板.md` through `05_plot/05_e_伏筆與回收表.md` 列出 P / CH-* evidence>
- **詞彙：** <掃 `02_vocabulary/` 列出已建 V 條目或檔案 evidence>

If a needed source family is completely absent, print:

`[source 缺漏 — 跑 /create-world 或 /create-character 建立基底]`

*來源：<依實際讀取 source 列出 project-root links>*

## 四、不可確認 / 需人類確認的內容

依現有 source 找出 unresolved evidence：

- **TODO 累積：** <count + first 5 locations>
- **INFERENCE 推測：** <count + first 5 locations>
- **CONFLICT 矛盾：** <count + first 5 locations>
- **缺漏實體：** <expected evidence vs parsed frontmatter；不要 invent placeholder IDs>
- **cross-ref stale / orphan：** <如果掃到 stale view、missing depends_on、orphan entity，列 evidence；不要修>

*來源：<依各標記或缺漏 evidence 的 source 路徑>*

## 五、通用規則適配性

| 規則 | 建議 | 原因 |
|---|---|---|
| 00_a §2 高品質台詞定義 | 保留 / 放寬 / 條件式 / 刪除 / 待確認 | <一句話原因；必須有 source evidence 或標待確認> |
| 00_a §3.3 診斷模式禁止事項 | 保留 | /diagnose 本身必須遵守 |
| 00_b §1 作品類型語氣 | 保留 / 放寬 / 條件式 / 刪除 / 待確認 | <依 00_b §1 狀態與內容> |
| 00_b §2 髒話尺度 | 保留 / 放寬 / 條件式 / 刪除 / 待確認 | <依 00_b §2 狀態與內容> |
| 00_c 台詞輸出格式 | 保留 / 放寬 / 條件式 / 刪除 / 待確認 | <依作品資料是否需要例外> |

*來源：[/00_protocol/00_a_台詞生產協議.md](/00_protocol/00_a_台詞生產協議.md) §2 / §3.3, [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1~§2, [/00_protocol/00_c_台詞輸出格式.md](/00_protocol/00_c_台詞輸出格式.md)*

## 六、建議下一步

依本次診斷結果給出 user-triggered next steps. Do not trigger them automatically.

1. **若 00_b §1/§2 標 TODO：** 跑 `/create-world`，或請 user 先拍板作品類型與髒話尺度。
2. **若有大量缺漏實體：** 跑對應 `/create-*` skill 建立基底。
3. **若想把 inline text 整理成模板欄位：** 跑 `/integrate`。
4. **若想看實體完成度：** 跑 `/status`。
5. **若想看 INFERENCE / TODO 累積與缺漏：** 跑 `/check-gaps`。
6. **若想看單一實體整合視圖：** 跑 `/view-*` 系列。
7. **若想持久化某實體整合視圖：** 跑 `/export-*` 系列。

---

**注意：** 本診斷報告由 `/diagnose` 自動產出（對齊 00_a §3.3 診斷模式）；屬 read-only analysis；不寫任何模板 / source / view / export。
```

Assembly rules:

- Keep the six `00_a` §3.3.4 sections. Do not add a seventh top-level diagnostic section.
- Phase D cross-file health findings such as stale view, orphan entity, missing dependency, or parser issue belong in section four or section six, not in a new section.
- Use explicit epistemic labels:
  - `可確認`
  - `INFERENCE`
  - `CONFLICT`
  - `待人類確認`
- Do not convert inferred observations into confirmed canon.
- Do not produce formal dialogue lines.

### Stage 4 - Present in Chat

Print the assembled Markdown report directly in chat.

Do not write:

- `view/<entity>.md`
- `export/<...>`
- any report file
- any source file
- any entity file
- any formal template field

### Stage 5 - Verification and Optional Audit

After output, verify:

- the report has exactly the six `00_a` §3.3.4 sections
- every source-backed section ends with an italic `來源` line
- no breadcrumb was added
- no TOC was added
- no file was written, except optional `.protocol_version.phase_log` audit entry when explicitly enabled
- no entity status or completion state was updated
- no other skill was triggered

The "下一步建議" belongs to section six of the report. Do not print a second standalone next-step list unless the user asks for a separate operational summary.

## 呈現規則

Follow `00_a` §3.3.4, `ARCHITECTURE.md` §4.3, and `UX_SPEC.md` §7.

1. Output is chat Markdown only.
2. Use `# 診斷報告` plus the six fixed sections from `00_a` §3.3.4.
3. Do not add breadcrumb. Breadcrumb belongs only to `/export-*` integration files.
4. Do not add TOC. TOC belongs only to long `/export-*` integration files.
5. Every source-backed section ends with one italic source line:
   - `*來源：[/path/to/source.md](/path/to/source.md)*`
   - For multi-source sections, list sources separated by commas.
6. Cross-file links must be project-root based and start with `/`.
7. Same-file anchors use `#slug` and do not start with `/`.
8. Use one-way references. The report may link to source files; source files do not need reverse links.
9. Empty states must be italic and explain why the empty state can be normal.
10. Do not expose parser stack traces, raw Python objects, internal enum keys, or implementation details.

## .protocol_version 寫入規範

Default behavior: do not write `.protocol_version`.

Optional audit behavior: if the user explicitly asks to log diagnostic reads, or the runtime environment has an explicit audit-log setting enabled, append one read-only audit entry to `.protocol_version.phase_log`.

The optional entry must not update entity completion, entity status, `created_entities`, `entities_touched`, `pipeline_state`, `mode_tag`, `qa_decision`, or any downstream artifact state.

SPEC §5.4a mutation-oriented fields are not meaningful for `/diagnose`. Omit them by default. If a local runtime schema requires explicit nullable fields, use empty or null values only, such as `entities_touched: []`, `iteration_count: null`, `iteration_note: null`, `base_dialogue: null`, and `conflict_resolutions: []`; do not use them as evidence of read/write authority.

Audit entry shape:

```yaml
- phase: diagnose
  date: YYYY-MM-DD
  skill: /diagnose
  status: completed
  mode: <scan_all | file_path | inline_text>
  scope: <"all_instance" | "<file_path>" | "inline_text_excerpt">
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 03_characters/main/<actual>.md
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_c_角色弧線表.md
    - 05_plot/05_d_資訊揭露表.md
    - 05_plot/05_e_伏筆與回收表.md
    - 00_protocol/00_a_台詞生產協議.md  # §2 / §3.3
    - 00_protocol/00_b_反ai味檢查表.md  # §1 / §2
    - 00_protocol/00_c_台詞輸出格式.md
  report_sections: 6
  findings_summary:
    todo_count: <N>
    inference_count: <N>
    conflict_count: <N>
    missing_entity_count: <N>
  output_target: chat
  customizations: []
  # Optional only if the local phase_log schema requires explicit §5.4a fields:
  # entities_touched: []
  # iteration_count: null
  # iteration_note: null
  # base_dialogue: null
  # conflict_resolutions: []
```

If the user says diagnostics are frequent or requests audit-log skip, do not write this optional entry.

## 輸入

Accepted user inputs:

- no parameter: scan the initialized Instance broadly
- `<file_path>`: diagnose one repo-relative Markdown file plus related dependency evidence
- `<inline text>`: diagnose pasted text only

Runtime inputs may include:

- `.protocol_version`
- `scripts/parse_frontmatter.py`
- `01_world/`
- `02_vocabulary/`
- `03_characters/`
- `04_relationships/`
- `05_plot/`
- `00_protocol/00_a_台詞生產協議.md` §3.3
- `00_protocol/00_b_反ai味檢查表.md` §1 / §2
- `00_protocol/00_c_台詞輸出格式.md`
- `view/*.md` only as stale-view evidence when already present; do not create or update it

## 輸出

Runtime output is one chat Markdown diagnostic report:

- `# 診斷報告`
- six sections from `00_a` §3.3.4
- source references after every source-backed section
- "下一步建議" inside section six

This skill writes no persistent report and no integration file. If the user wants to turn diagnostic observations into structured source/template fields, tell them to run `/integrate`. If the user wants a persisted view, tell them to run the relevant `/export-*` skill.

## 邊界

`/diagnose` is a pure read-only skill aligned with `00_a` §3.3. It is strictly limited to:

1. Do not write any file, except the optional `.protocol_version.phase_log` audit entry when explicitly enabled.
2. Do not write `view/<entity>.md` or `export/<...>` files. Those belong to `/export-*` and Layer 3 Export scope.
3. Do not expand source scope beyond the selected mode:
   - Mode A scans broad Instance source.
   - Mode B reads one file plus dependency/evidence chain.
   - Mode C reads inline text only.
4. Do not upgrade, downgrade, approve, or otherwise change entity status.
5. Do not automatically call `/integrate`, `/status`, `/check-gaps`, `/view-*`, `/export-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, `/qa`, `/create-*`, or any other skill.
6. Do not reorganize source content into formal canon. Extract evidence faithfully, apply the six-section diagnostic frame, and keep conclusions provisional when evidence is incomplete.
7. Do not write `LOCKED` status, produce FINAL / LOCKED files, modify LOCKED files, or modify any `00_protocol/` file.
8. Strictly obey `00_a` §3.3.3 diagnostic prohibitions:
   - do not directly rewrite formal templates
   - do not invent or complete major worldbuilding settings
   - do not write inference as confirmed canon
   - do not produce final or locked files
   - do not directly generate formal dialogue

Unlike `/create-*`, `/iterate-*`, `/scene-task`, `/dialogue-write`, and `/qa`, this skill does not use D-050 write-boundary blocks. Unlike `/export-*`, it does not write DERIVED views, breadcrumb, TOC, return links, or mandatory phase_log entries.

## 錯誤處理 / Rollback

Because `/diagnose` is read-only by default, rollback normally means: no source files were changed, no generated files need deletion, and the user can rerun the skill after fixing missing prerequisites.

Blocking prerequisite failures:

- Template repo detected by `.template_root`
- Bootstrap missing or incomplete
- parser unavailable in repo-wide or file-path mode
- requested file path is outside repo root
- requested file path does not exist

For these, stop before assembling output.

Partial source failures:

- If one expected source is missing in broad scan mode, keep the report skeleton and print a warning plus `[source 缺漏]` at the affected position.
- If a source family is completely absent, print `[source 缺漏 — 跑 /create-world 或 /create-character 建立基底]` in section three where applicable.
- If `00_b` §1 or §2 cannot be found, keep the rule-fit table and mark those rows `待確認`.
- If `build_repo_index(".")` reports parser ERRORs but still returns usable evidence, list the first five in section four and continue only when the report can remain truthful.

If the optional audit entry write fails, do not retry with ad hoc file writes. Print a warning that the chat report succeeded but audit logging failed.

## 錯誤呈現規則

Follow `_design/ARCHITECTURE.md` §3.3.1 and `_design/UX_SPEC.md` §8.

Use:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable execution errors such as missing requested files, unreadable files, malformed frontmatter, or parser failures.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repo state that has not reached the required prerequisite, such as Template repo detection or incomplete Bootstrap.
- `## ⚠ 需注意 / Warning` only for non-blocking partial source gaps.

Every blocking error must include:

- `What`
- `Where`
- `Why`
- `下一步`

For multiple errors, summarize first, then list each item. Do not expose stack traces, raw enum keys, parser exception dumps, or internal implementation objects.

Use this shape for missing prerequisites:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: /diagnose 無法啟動，因為 Instance 尚未滿足必要前置條件。
Where: <path or condition>
Why: /diagnose 需要已完成 Bootstrap 才能安全判斷目前資料是 Instance 資料，而不是 Template 骨架。
下一步: 先執行 /init-project；若這是新 Instance 且已決定使用，先依 Bootstrap 流程移除 .template_root。
```

Use this shape for partial source gaps:

```md
## ⚠ 需注意 / Warning

What: 部分 source 缺漏，診斷報告已用 [source 缺漏] placeholder 保留位置。
Where: <missing source path>
Why: /diagnose 不會自行補寫 source，只能呈現目前可讀資料。
下一步: 依缺漏類型手動觸發 /create-world、/create-character、/create-outline、/create-detailed-outline、/status、或 /check-gaps。
```
