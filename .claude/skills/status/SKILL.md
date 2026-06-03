---
name: status
description: "列出 Instance repo 內所有實體（型別集權威見 entity_type_registry：W-rules/W-language/W-style/V/C/R/P/CH/S/A/ORG）的完成度百分比 + 缺漏實體建議下一步 skill。對齊 ARCH §2.3 完成度公式 + SPEC §5.3。純讀取，不寫任何檔。"
---

狀態：DRAFT
版本：v0.4（Batch 5 registry DRY — 型別列舉與 Template skeleton 範圍改述為「讀 registry 衍生」指標寫法（description / Stage 3 / Stage 4 case-(b)）：指示 agent 從 build_repo_index().entity_registry（all_valid_types() / core[].target_dir）衍生型別集與 per-dir skeleton 範圍，殘留文字列舉一律標「（鏡像；權威見 entity_type_registry）」使 drift 可稽核；完成度公式與 opt-in/ORG（D-071）語義 behavior-identical；本檔為文件，改指標非執行碼；本檔 v0.3 → v0.4）
歷史紀錄：v0.3（F8 Phase 3 — 修 3 處 stale「/create-org 待 Phase 3」→ live /create-org（D-074）+ 修 ORG opt-in rule「不在 expected_entities」斷言（Phase 3 已加 create_org opt-in block，repeatable，present-only 不報 missing）；對齊 Step 2 稽核 m1/m2；v0.2 → v0.3）；v0.2（F8 Phase 2 — 加 ORG-* 入 entity 列舉（description + missing→next-skill 表）+ ORG opt-in rule（present 計入完成度、不報 missing-expected；/create-org 待 Phase 3）；對齊 D-071；v0.1 → v0.2）；v0.1（初版）
最後更新：2026-06-03
適用範圍：/status skill runtime instructions
優先級：高

# /status Skill

## 用途

Use this skill when the user triggers `/status` and wants a read-only progress report for the current Instance repo.

The skill scans the repo, derives the expected logical entity set from `.protocol_version.phase_log`, calculates completion for each entity from Markdown frontmatter, and prints missing or untracked entities with the next suggested skill.

掃描範圍說明：`_source_materials/` 為 user 原始素材區，不計實體進度、不報 header 缺漏（該目錄已從 build_repo_index 全 repo 掃描排除）。

This skill is diagnostic only. It must not write, create, update, move, delete, or normalize any file.

## 觸發語

- `/status`
- Chinese alias: `/進度`, via `.claude/skills/進度/SKILL.md`

Do not accept direct user parameters. If the user appends extra text after `/status`, ignore it for entity selection and scan the whole repo automatically.

## 觸發協議

There is no mutable `00_protocol/` file for this skill. The runtime authority is this design stack:

- `_design/TASKS.md` v1.5 §A.7
- `_design/ARCHITECTURE.md` v1.4 §2.3, §3.3, and §3.3.1
- `_design/SPEC.md` v1.2 §5.3, §5.4, and §5.4a
- `_design/expected_entities.yaml`
- `scripts/parse_frontmatter.py`, especially `build_repo_index(repo_root)` and `parse_file(path, repo_root=None, qa_type_registry=None)`
- `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2 and §3.3a-e
- `_design/DECISIONS_LOG.md` §6.7.2 / §6.7.3 for D-042 and §6.9.2 for D-047

If chat instructions conflict with these files, follow the files above.

## 啟動條件

Before Stage 1, confirm the current folder is the Instance repo root.

Required state:

1. `.protocol_version` exists at the Instance root.
2. `.protocol_version.phase_log` contains a Bootstrap entry with `phase: bootstrap` and `status: completed`.
3. `_design/expected_entities.yaml` exists.
4. `scripts/parse_frontmatter.py` can be imported.
5. `build_repo_index(".")` can scan the repo without blocking import/runtime failure.

If `.protocol_version` is missing or Bootstrap is not completed, stop with `## ⏸ 條件未滿足 / Prerequisites Not Met` and tell the user to run `/init-project`.

## 流程

Run exactly five stages. Keep every stage read-only.

### Stage 1 - Diagnosis

Check that the Instance has been bootstrapped.

Read only enough to answer:

- Is `.protocol_version` present?
- Is `phase_log` present and parseable?
- Does `phase_log` include `phase: bootstrap`, `skill: /init-project`, and `status: completed`?

Do not calculate completion before these prerequisites pass.

If prerequisites fail, print:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: Instance 尚未完成 Bootstrap。
Where: .protocol_version / phase_log
Why: /status 需要 phase_log 才能知道哪些 entity 應該存在。
下一步: 先執行 /init-project。
```

If Bootstrap is completed, continue to Stage 2.

### Stage 2 - Exploration

Read these inputs:

1. `_design/expected_entities.yaml`
2. `.protocol_version` `phase_log`
3. Full Markdown frontmatter index from `scripts/parse_frontmatter.build_repo_index(".")`

Expected parser usage:

```python
from scripts.parse_frontmatter import build_repo_index, parse_file

repo_index = build_repo_index(".")
all_files = repo_index.all_files_parsed
phase_log_entries = repo_index.phase_log_result.entries
issues = repo_index.issues
```

`parse_file(path, repo_root=None, qa_type_registry=None)` is available for single-file checks, but `build_repo_index(".")` is the main API.

**Entity type set is registry-derived (Batch 5 DRY).** The authoritative set of entity types (W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG) and each type's `target_dir` come from the loaded registry, not from any literal list restated in this SKILL. Read them from `repo_index.entity_registry`:

```python
registry = repo_index.entity_registry
valid_types = registry.all_valid_types()          # type names, e.g. {"W-rules", ..., "ORG"}
target_dirs = {t: registry.core[t].target_dir for t in registry.core}  # per-type target_dir(s)
```

Anywhere this SKILL spells out a type list or a per-directory scope inline below, treat that literal as a **mirror (鏡像；權威見 entity_type_registry)** kept only for human readability. If the registry and an inline mirror disagree (a type/dir was added or renamed), the registry wins; do not let a stale literal narrow the scan. `scripts/check_entity_type_consistency.py` asserts the **parser-side** mirrors stay equal to registry `core`; this SKILL's inline mirrors are currently human / L1-guarded (machine enforcement pending `<!-- REGISTRY-MIRROR -->` markers — NEW_REQ_49 尾巴).

For each `ParsedMarkdown` item, read:

- `path`
- `header["狀態"]`
- `yaml_data["entities"]`
- `yaml_data["depends_on"]`
- `yaml_data["weight"]`
- downstream YAML fields such as `scene_id`, `pipeline_state`, `mode_tag`, and `qa_decision`

If `yaml_data` is absent or not a mapping, treat `entities`, `depends_on`, and `weight` as empty.

### Stage 3 - Derive Expected Set

Derive the concrete expected entity set from completed `phase_log` entries plus `_design/expected_entities.yaml`.

Rules:

1. Consider only entries with `status: completed`.
2. If `status` is missing, treat it as not completed for expected-set purposes.
3. Normalize phase keys when matching the manifest: `create-world` and `create_world` refer to the same manifest phase.
4. Add every actual entity ID listed in `created_entities`.
5. Add the single `scene_id` value for `scene-task`, `dialogue-write`, and `qa` entries.
6. Do not use `entities_touched` to create expected entities. It is mutex/debug context, not creation evidence.
7. For literal manifest entries without placeholders, such as `W-rules`, `W-language`, `V`, and `P`, include them when their completed phase appears.
8. For placeholder manifest entries, such as `C-<name>`, `R-<a>-<b>`, `CH-<n>`, and `S-<ch>-<n>`, do not invent IDs. Use only concrete IDs from `created_entities`, `scene_id`, or a referenced scene index if a future LOCKED spec explicitly requires it.
9. Bootstrap is a special case. `scene_ids: []` may appear for backward compatibility, but Bootstrap creates no logical entity.
10. `dialogue_paths`, `target_dialogue`, and `qa_report_paths` are artifact checks for existing scene entities. They are not new logical entity IDs.

Recommended phase mapping:

| phase_log phase | Expected entity source |
|---|---|
| `bootstrap` | none |
| `create-world` / `create_world` | literal manifest entities and `created_entities` |
| `create-character` / `create_character` | `created_entities` |
| `create-relationship` / `create_relationship` | `created_entities` |
| `create-outline` / `create_outline` | literal manifest `P` and `created_entities` |
| `create-detailed-outline` / `create_detailed_outline` | concrete `created_entities`; do not invent placeholder CH/S IDs |
| `scene-task` / `scene_task` | single `scene_id`; `task_path` is an artifact check |
| `dialogue-write` / `dialogue_write` | single `scene_id`; `dialogue_paths` are artifact checks |
| `qa` | single `scene_id`; `qa_report_paths` are artifact checks |

### Stage 4 - Calculate Completion

Calculate completion for every entity in:

- the expected set
- frontmatter `entities` that are not in the expected set

Use the ARCH §2.3 / SPEC §5.3 formula:

```python
score_map = {
    "DRAFT": 25,
    "REVIEW": 75,
    "FINAL": 100,
    "LOCKED": 100,
}

for each contributing file:
    score = score_map[file.status]
    weight = file.frontmatter.get("weight", {}).get(entity_id, 1.0)

entity_completion = sum(score * weight) / sum(weight)
```

Implementation details:

1. A contributing file is any parsed Markdown file whose YAML `entities` contains the entity ID.
2. If `weight` is a mapping and contains the entity ID, use that value.
3. If `weight` is a single number, use that value for this entity.
4. If no weight is provided, use `1.0`.
5. Ignore `DEPRECATED` files completely. They do not add score or weight.
6. For any other status outside `score_map`, do not label it as a narrative progress state. Treat it as non-scoring and include it only in a diagnostic note if needed.
7. If an expected entity has no contributing file, completion is `0%` and the entity is missing.
8. If an entity appears in frontmatter but is not in the expected set, decide between two cases before scoring it:
   - **(a) Genuine manual entity** — at least one contributing file is an instance file (not a Template skeleton file). Calculate normally and mark it as `未追蹤（手動建）`.
   - **(b) Un-activated Template scaffolding** — ALL contributing files are Template skeleton files (defined registry-derived below) and no completed `phase_log` entry created this entity. Do NOT report this as narrative progress. Report it as `尚未建立（範本骨架）0%` and treat it like a missing expected entity for the next-skill suggestion. This prevents a freshly bootstrapped repo from showing phantom progress (for example `W-rules 75%`) just because the shipped templates carry default `entities` frontmatter.

Template skeleton scope (case (b) set), **derived from the registry, not from a frozen literal list**: a contributing file counts as a Template skeleton file when it is a shipped default scaffold sitting directly under one of the registry-declared entity `target_dir` roots (each type's `registry.core[t].target_dir`, comma-split for multi-dir types such as `S`). Build the per-directory scope at runtime:

```python
skeleton_dirs = set()
for entry in registry.core.values():
    for d in (p.strip() for p in entry.target_dir.split(",")):
        if d:
            skeleton_dirs.add(d)        # e.g. 01_world/, 02_vocabulary/, ..., 11_organizations/
# A contributing file is "Template skeleton" if it is a shipped default scaffold whose
# path falls directly under one of skeleton_dirs and was not created by a completed phase_log entry.
```

Deriving from `target_dir` means a newly added or renamed type/dir (e.g. `10_art_assets/`, `11_organizations/`) is automatically in scope without re-listing files here.

For human auditability, the current shipped scaffolds these directories contain are mirrored below (鏡像；權威見 entity_type_registry 的 `target_dir` + Template 的實際 skeleton 檔；若 registry 與此列舉分歧，以 registry 為準；parser 端鏡像由 `scripts/check_entity_type_consistency.py` 強制，本 SKILL 列舉目前人工 / L1 守護（machine 強制待 REGISTRY-MIRROR marker — NEW_REQ_49 尾巴）):

> `01_world/01_a|01_b|01_c`, `02_vocabulary/02_a|02_b|02_c`, `03_characters/03_a|03_b|03_c`, `04_relationships/04_a|04_b`, `05_plot/05_a|05_b|05_c|05_d|05_e`, `06_scene_index/06_a`, `07_scene_tasks/07_a`, `08_dialogue_outputs/08_a|08_b`, every `09_quality_assurance/09_*` template, `10_art_assets/` 各 subtype 的 `index.md`，與 `11_organizations/` 範本骨架。

A real entity created by a skill enters the expected set via `phase_log` (Stage 3) and is scored through the expected-set path, so it is unaffected by this rule.

Status summary examples:

- `100%  (FINAL)`
- `75%  (1 REVIEW)`
- `52.8%  (1 REVIEW + 2 DRAFT)`
- `0%  (尚未建立)`
- `25%  (未追蹤；1 DRAFT)`

#### Missing Entity to Next Skill Mapping

Use this mapping for missing expected entities. The `Entity pattern` column is a **mirror (鏡像；權威見 entity_type_registry)** of the registry type set (`registry.all_valid_types()`); every type a missing entity can carry must have a row here. If a type is added/renamed in the registry, add/rename its row (parser-side drift is flagged by `scripts/check_entity_type_consistency.py`; this SKILL's inline list is human / L1-guarded until REGISTRY-MIRROR markers land — NEW_REQ_49 尾巴). Match a missing entity's ID against `registry.core[t].id_pattern` to pick its type, then look up the row:

| Entity pattern | Next suggestion |
|---|---|
| `W-*` | `/create-world` |
| `V` | `/create-world` |
| `C-*` | `/create-character` |
| `R-*` | `/create-relationship` |
| `P` | `/create-outline` |
| `CH-*` | `/create-detailed-outline` |
| `S-*` | `/scene-task` |
| `A-*` | manually edit `10_art_assets/<subtype>/index.md` |
| `ORG-*` | `/create-org`（F8 Phase 3 已落地；亦可手動 author `11_organizations/<name>.md`）|

Asset rule:

- Per D-045, `A-*` does not block or roll into narrative `/status` completion.
- If `A-*` appears in expected data or frontmatter, show it in a separate non-blocking asset section and suggest the manual `10_art_assets/<subtype>/index.md` path.

ORG rule (D-071):

- `ORG-*`（組織 / 非人格反派 / 組織型對抗源）是 opt-in / repeatable 敘事節點：**present 時計入完成度**（weight 1.0，per-entity 正規化，對既有實體 % 零位移）；`expected_entities.yaml` 的 `create_org` phase 為 **opt-in / repeatable**（present-only），故**不報為 missing-expected**（同 `/create-character`·`/create-relationship` 等 repeatable phase 的 present-only 語義；不同於 `A-*` 之 non-blocking asset）。
- 僅當其他實體 `depends_on` 一個不存在的 `ORG-*` 時，才依上表建議跑 `/create-org`（F8 Phase 3 已落地）或手動 author。

#### Downstream Artifact Checks

Also report downstream artifact gaps found in completed `phase_log` entries:

- If a completed `scene-task` entry has `task_path` but the file is missing, mark the scene as `下游檔案缺失`.
- If a completed `dialogue-write` entry lists `dialogue_paths` but one or more files are missing, mark the scene as `下游檔案缺失`.
- If a completed `qa` entry has fewer than 8 `qa_report_paths`, or any listed QA report is missing, mark the scene as `QA 報告不完整`.

These artifact checks supplement entity completion. They do not create additional expected entity IDs.

### Stage 5 - Output

Print a user-facing report in the ARCH §2.3 shape:

```md
=== 邏輯實體完成度 ===

W-rules               100%  (FINAL)
W-language             75%  (1 REVIEW)
V                      50%  (3 DRAFT)
C-主角A                75%  (1 REVIEW + 1 DRAFT in 04_a)
P                       0%  (尚未建立)
CH-01                  25%
CH-02                   0%

=== 缺漏實體 ===
- P：主線尚未建立，建議跑 /create-outline
- CH-03：章節尚未建立，建議完成主線後跑 /create-detailed-outline
```

If there are no tracked entities after Bootstrap, print:

```md
=== 邏輯實體完成度 ===

_目前只有 Bootstrap 紀錄，尚無應追蹤的劇本實體。這是剛初始化後的正常狀態。_

=== 缺漏實體 ===
_無。下一步可執行 /create-world。_
```

If untracked entities exist, add:

```md
=== 未追蹤實體（手動建） ===
- C-臨時角色：25% (1 DRAFT)
```

If asset entities exist, add a separate non-blocking section:

```md
=== 素材追蹤（非 narrative 完成度） ===
- A-portrait-主角A-default：100% (FINAL)
```

If downstream artifact gaps exist, add:

```md
=== 下游檔案檢查 ===
- S-01-03：QA 報告不完整，phase_log 需要 8 份 QA report。
```

## 時期 C 呈現規則

Follow these presentation rules:

1. §1.5 不暴露 enum key: do not expose internal enum keys to the user. For example, do not print `pipeline_state: DIALOGUE_TRIAL`; print a human-readable phrase such as `台詞試寫中`.
2. §1.6.1 G1 badge 不單獨呈現: do not show a status badge by itself. Every entity state must include a completion number or contributing file summary.
3. §1.6.1 G2 流程視覺化僅為閱讀順序: if the report lists downstream pipeline stages, add: `下游階段僅供閱讀順序參考，不代表強制執行步驟。`
4. Do not show stack traces, Python exception dumps, parser internals, or raw implementation objects.

## 輸入

The skill accepts no user parameters.

Runtime inputs are read from the repo:

- `.protocol_version`
- `_design/expected_entities.yaml`
- Markdown frontmatter across the repo via `build_repo_index(".")`

## 輸出

Runtime output is chat-only:

- logical entity completion table
- missing entity list with next suggested skill
- untracked entity list, when present
- optional non-blocking asset section, when `A-*` entities appear
- downstream artifact gap list, when present
- parser ERROR summary, when present

The skill creates and modifies no files.

## 邊界

Hard prohibitions:

- Do not write any file.
- Do not update `.protocol_version`.
- Do not repair headers or frontmatter.
- Do not modify LOCKED files.
- Do not modify `_design/`, `scripts/`, `00_protocol/`, `_tools/frontend/`, templates, or existing skills.
- Do not create `/check-gaps` or any other skill.
- Do not infer missing placeholder IDs such as `C-<name>`, `R-<a>-<b>`, `CH-<n>`, or `S-<ch>-<n>` without concrete phase_log evidence.
- Do not treat `entities_touched` as created entities.
- Do not treat `import_source: agent_assisted` as quality approval.
- Do not include `A-*` in narrative completion roll-up.

## 錯誤呈現規則

Use the ARCH §3.3.1 four-part shape.

Use `## ✗ 無法執行 / Cannot Proceed` for user-correctable or missing-file execution errors.

Use `## ⏸ 條件未滿足 / Prerequisites Not Met` for repo state that has not reached the required prerequisite.

Every error must include:

- `What`
- `Where`
- `Why`
- `下一步`

### parse_frontmatter import failure

```md
## ✗ 無法執行 / Cannot Proceed

What: 無法載入 frontmatter parser。
Where: scripts/parse_frontmatter.py
Why: /status 需要 build_repo_index(".") 才能掃描 repo 內所有 .md frontmatter。
下一步: 補回 scripts/parse_frontmatter.py，或確認目前工作目錄是 Instance repo root。
```

### .protocol_version missing or Bootstrap incomplete

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: Instance 尚未完成 Bootstrap。
Where: .protocol_version / phase_log
Why: /status 需要已完成的 bootstrap phase_log 才能推導 expected set。
下一步: 先執行 /init-project。
```

### expected_entities.yaml missing

```md
## ✗ 無法執行 / Cannot Proceed

What: 找不到 expected entity manifest。
Where: _design/expected_entities.yaml
Why: /status 需要 manifest 對照 phase_log 才能判斷哪些 entity 應存在。
下一步: 從 Template 補回 _design/expected_entities.yaml 後重新執行 /status。
```

### build_repo_index reports ERROR

If `repo_index.issues` contains `severity == "ERROR"`, print the first five errors and stop before producing a completion table:

```md
## ✗ 無法執行 / Cannot Proceed — parser 發現 5 項以上 ERROR

What: repo frontmatter 或 phase_log 有 parser ERROR。
Where: 見下列前 5 項。
Why: 完成度計算需要可信 frontmatter index；ERROR 會讓 entity / weight / phase_log 結果不可靠。
下一步: 執行 python scripts/check_headers.py，修正 ERROR 後重新執行 /status。

1. <path>: <message>
2. <path>: <message>
3. <path>: <message>
4. <path>: <message>
5. <path>: <message>
```

If there are fewer than five ERROR entries, list all of them.
