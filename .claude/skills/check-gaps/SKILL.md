---
name: check-gaps
description: "掃描 Instance repo 全 .md frontmatter + 內文，列出 TODO/INFERENCE/CONFLICT 標記、空 entities 檔、缺漏實體檔、view/ 失效檔。純讀取，不寫任何檔。"
---

狀態：DRAFT
版本：v0.2（F8 Phase 3 / D-074 — Stage 4 gap-to-skill 表加 ORG-* → /create-org（懸空 depends_on:[ORG-*] 建議；opt-in）；掃描天然含 11_organizations/（build_repo_index glob 全 repo）。純讀取行為不變）
歷史紀錄：v0.1（初版）
最後更新：2026-06-03
適用範圍：/check-gaps skill runtime instructions
優先級：高

# /check-gaps Skill

## 用途

Use this skill when the user triggers `/check-gaps` to inspect an initialized Instance repo for unresolved gaps.

This skill is a read-only monitoring tool. It does not accept user parameters in the slash command. It scans the whole repo and reports:

- `TODO:` / `INFERENCE:` / `CONFLICT:` markers in frontmatter or body text
- files with meaningful content but `entities: []`
- expected entities or artifacts that are missing after completed workflow phases
- stale `view/` integration files whose sources are newer than the exported view

掃描範圍說明：`_source_materials/` 為 user 原始素材區，不計實體進度、不報 header 缺漏（該目錄已從 build_repo_index 全 repo 掃描排除）。

## 觸發語

- `/check-gaps`
- Chinese alias: `/缺漏檢查`, via `.claude/skills/缺漏檢查/SKILL.md`

## 觸發協議

`/check-gaps` has no write protocol. It is a pure technical monitoring skill.

Primary authority:

- `_design/TASKS.md` v1.5 §A.8
- `_design/SPEC.md` §5.2, §5.4, §9, and §10 for frontmatter, phase expectations, and upstream entity families
- `_design/ARCHITECTURE.md` §3.3 for SKILL.md structure
- `_design/expected_entities.yaml`
- `scripts/parse_frontmatter.py`
- `_design/UX_SPEC.md` §7.7 and §8
- `_design/DATA_FORMAT_SPEC.md` §3.2 / §3.3

If chat instructions conflict with the files above, follow the files above. LOCKED files remain higher priority than chat history.

## 啟動條件

Before Stage 1, confirm the current working root is an Instance repo.

Required checks:

1. `.protocol_version` exists.
   - If missing, stop and tell the user to run `/init-project` first.
2. `.protocol_version.phase_log` contains a completed Bootstrap entry.
   - Accept only an entry with `phase: bootstrap` and `status: completed`.
   - If absent, stop and tell the user to complete `/init-project` first.
3. `_design/expected_entities.yaml` exists and is readable.
   - If missing, stop; the expected-entity comparison cannot run.
4. `scripts/parse_frontmatter.py` exists and can be imported.
   - If import fails, stop; do not replace the parser with ad hoc parsing.
5. `view/` is optional.
   - If absent or empty, skip the view-refresh section and report it as a normal empty state.

Use this condition failure format:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

- **What**：
- **Where**：
- **Why**：
- **下一步**：
```

Do not expose stack traces, Python exception dumps, parser internals, or raw enum keys in user-facing output.

## 流程

Run exactly five stages. The skill is read-only in every stage.

### Stage 1 - Diagnosis

Load the parser from `scripts/parse_frontmatter.py` and build the repo index:

```python
from scripts.parse_frontmatter import build_repo_index, parse_file

repo_index = build_repo_index(".")
```

If `build_repo_index(".")` returns any `ValidationIssue` with severity `ERROR`, stop and print:

```md
## ✗ 無法執行 / Cannot Proceed

- **What**：repo frontmatter / registry / phase_log 解析有錯誤，`/check-gaps` 無法產生可信報告。
- **Where**：列出前 5 條 ERROR 的檔案、行號與人類可讀訊息。
- **Why**：缺漏檢查依賴 A.0 parser index；parser index 不可信時，後續 gap list 可能誤報。
- **下一步**：先執行 `python scripts/check_headers.py` 修正 header/frontmatter 錯誤，再重跑 `/check-gaps`。
```

If parser import fails, stop and print:

```md
## ✗ 無法執行 / Cannot Proceed

- **What**：無法載入 Phase A.0 frontmatter parser。
- **Where**：`scripts/parse_frontmatter.py`
- **Why**：`/check-gaps` 必須使用 A.0 parser API 建立 repo index；不能改用臨時解析規則。
- **下一步**：修復或恢復 `scripts/parse_frontmatter.py` 後重跑 `/check-gaps`。
```

### Stage 2 - Exploration: five scan dimensions

Scan all markdown files through `repo_index.all_files_parsed`. Use normalized repo-relative paths with `/`.

#### 2a. TODO / INFERENCE / CONFLICT markers

For every parsed markdown file, inspect `ParsedMarkdown.source_text` line by line.

Detect these literal markers anywhere in frontmatter or body:

- `TODO:`
- `INFERENCE:`
- `CONFLICT:`

This includes HTML comments, YAML string values, list values, body paragraphs, and dialogue/task text.

For each match, record:

- file path
- 1-based line number
- marker type
- marker text after the marker, trimmed to one concise line

Do not reinterpret the marker. Report exactly what remains unresolved.

#### 2b. Empty `entities` with meaningful content

For every parsed markdown file:

1. Check `ParsedMarkdown.yaml_data`.
2. Only consider files whose YAML block is a mapping and contains `entities`.
3. If `entities: []`, inspect the body text after the Chinese header and YAML block.
4. If the body contains meaningful content, list the file as `entities` missing.

Treat the body as meaningful when any of the following are present:

- body KEY comments or dialogue-key text
- non-empty paragraphs beyond headings, separators, and placeholder-only lines
- scene, character, world, relationship, plot, dialogue, QA, or asset content

Skip files that legitimately omit YAML, such as protocol skeleton files where the canonical schema permits no `entities` block.

For each finding, record:

- file path
- observed content signal, such as `body paragraphs`, `KEY comments`, or `dialogue lines`
- current frontmatter state: `entities: []`

#### 2c. Expected but missing entities

Read `_design/expected_entities.yaml` and `.protocol_version.phase_log`.

Build the expected set from completed phase entries only:

- ignore entries whose `status` is not completed
- use each completed entry's `created_entities` when present
- for static manifest phases such as `/create-world`, include the manifest's fixed entities if the completed entry identifies that phase
- for repeatable placeholder phases such as `C-<name>` or `R-<a>-<b>`, use concrete IDs from `created_entities`; do not invent IDs from placeholders
- for downstream phase entries, use `scene_id`, `task_path`, `dialogue_paths`, `target_dialogue`, and `qa_report_paths` as artifact expectations when present

Then compare expected entities against parsed frontmatter:

- An expected entity is present when at least one parsed file has a frontmatter `entities` list containing that ID.
- If no contributing file exists, list it as `expected but missing`.
- If the entity registry exposes target directories, include the expected target directory in the report.
- If target directory cannot be derived from current parser/manifest data, say `target path not derivable from current manifest`; do not invent a file path.

For expected artifacts:

- If `task_path` is recorded, check that file exists.
- If `dialogue_paths` are recorded, check each listed path exists.
- If `qa_report_paths` are recorded, check each listed path exists.
- If the manifest declares an artifact count rule, include a human-readable count mismatch when the recorded paths are fewer than required.

### Stage 3 - `view/` refresh detection

If `view/` does not exist or contains no `.md` files, skip this stage and later print an empty state:

```md
=== view/ 整合檔需更新 ===
*目前沒有 view/ 整合檔可檢查；若尚未跑過 `/export-*`，這是正常狀態。*
```

For each `view/*.md` file:

1. Read the file as UTF-8.
2. Find the `組合來源` section.
3. Extract source paths from that section.
   - Prefer paths wrapped in backticks.
   - Also accept Markdown list items that look like repo-relative `.md` paths.
   - Stop at the next heading of the same or higher level.
4. Normalize paths as repo-relative paths.
5. Ignore external URLs.
6. For each source path that exists, compare mtimes with `os.path.getmtime()`.
7. If any source mtime is later than the view file mtime, mark the view as stale.
8. If a listed source path is missing, include it as a gap under the same view file.

When any stale view exists, print the UX §7.7 warning title exactly:

```md
## ⚠ view/ 整合檔需更新 / View Files Need Refresh
```

Then list each affected file:

```md
- `view/world.md`（view mtime: YYYY-MM-DD HH:MM）
  - source `01_world/01_a_世界觀總覽.md`（mtime: YYYY-MM-DD HH:MM，比 view 新 X 分鐘）
```

End the view section with: `**下一步：** 對受影響 entity 重跑 `/export-*` 更新整合檔。`

If a view file lacks a readable `組合來源` section, report What / Where / Why / 下一步 and tell the user to rerun the corresponding `/export-*`.

### Stage 4 - Gap-to-skill suggestions

For every missing expected entity or artifact, suggest the next user-triggered skill. Do not trigger it automatically.

Use this mapping:

| Missing ID / artifact | Suggested skill |
|---|---|
| `W-*` | `/create-world` |
| `V` | `/create-world` |
| `C-*` | `/create-character` |
| `R-*` | `/create-relationship` |
| `P` | `/create-outline` |
| `CH-*` | `/create-detailed-outline` |
| `ORG-*` | `/create-org`（懸空 `depends_on:[ORG-*]` 但 `11_organizations/<name>.md` 不存在時建議；ORG-* opt-in，無 org 的專案不報缺漏） |
| `S-*` | `/scene-task` for task packages; `/dialogue-write` or `/qa` only when the missing artifact is specifically dialogue or QA output |
| `task_path` missing | `/scene-task` |
| `dialogue_paths` missing or too few | `/dialogue-write` |
| `qa_report_paths` missing or too few | `/qa` |

If the repo is only bootstrapped and no later phase has completed, report that there are no expected narrative entities yet. Do not suggest running every downstream skill.

### Stage 5 - Output

Print one read-only report in this exact order.

```md
=== TODO / INFERENCE / CONFLICT 標記 ===
[`path/to/file.md`] (line N): TODO: <文字>
[`path/to/file.md`] (line N): CONFLICT: <文字>
...

=== entities 漏標（空 entities 但檔有 KEY 內文）===
[`path/to/file.md`]: 內文有 X 段內容但 frontmatter entities 為空
...

=== 缺漏實體（expected but missing）===
- `W-rules`：phase_log 顯示 `/create-world` 已完成，但沒有任何 frontmatter entities 包含此 ID；下一步：跑 `/create-world` 或修復對應檔 frontmatter
- `task_path`：phase_log `scene-task` entry 記錄的任務包不存在；下一步：重跑 `/scene-task <scene_id>`
...

=== view/ 整合檔需更新 ===
## ⚠ view/ 整合檔需更新 / View Files Need Refresh

下列 view/ 檔案的 source 已修改，但整合檔未重新匯出：

- `view/world.md`（view mtime: ...）
  - source `01_world/01_a_世界觀總覽.md`（mtime: ...，比 view 新 X 分鐘）

**下一步：** 對受影響 entity 重跑 `/export-*` 更新整合檔。
```

Empty sections must still be printed with one italic sentence explaining why no finding may be normal.

## 輸入

No slash-command parameters.

The skill reads repo root `.protocol_version`, `_design/expected_entities.yaml`, all repo `.md` files through `scripts/parse_frontmatter.py`, and `view/*.md` if present.

## 輸出

The skill outputs a chat report only.

It creates no files and modifies no files.

## 邊界

Strict prohibitions:

- Do not modify any file, update `.protocol_version`, or create reports on disk.
- Do not run `/create-*`, `/scene-task`, `/dialogue-write`, `/qa`, `/status`, or `/export-*` automatically.
- Do not modify LOCKED files, `_design/`, `scripts/`, `00_protocol/`, `_tools/frontend/`, existing 27 templates, or other skill directories.
- Do not infer missing canon, fill missing entities on behalf of the user, or delete manual/untracked entity files.

`/check-gaps` reports evidence and next actions. It does not approve, repair, or dispatch work.

## 錯誤呈現規則

Follow `_design/UX_SPEC.md` §8 and `_design/ARCHITECTURE.md` §3.3.1.

Use:

- `## ✗ 無法執行 / Cannot Proceed` for user-facing errors or unusable required files
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for missing bootstrap or unmet repo state
- `## ⚠ 需注意 / Warning` only for non-blocking warnings

Every blocking error must include:

- **What**
- **Where**
- **Why**
- **下一步**

Presentation rules: put next steps in imperative language; do not use vague wording such as "應該", "可能", or "建議考慮" for the required next step line; do not expose stack traces, parser exception dumps, or raw internal enum keys; summarize multiple errors before individual items; explain empty states.
