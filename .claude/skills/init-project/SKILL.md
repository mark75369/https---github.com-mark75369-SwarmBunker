---
name: init-project
description: 建立新 Instance repo 的 Bootstrap 流程。從 Template clone 後執行，引導使用者完成專案初始化、Template 微調（限 00_b/00_c/00_d）、三 registry 拷貝、10_art_assets/ 目錄結構、Instance root .gitignore 建立、`.protocol_version` 紀錄。對齊 00_protocol/00_i_專案初始化協議.md 全 5 階段流程。
---

狀態：DRAFT
版本：v0.3（D-051 partial supersede D-049 — 移除第二道防線 over-broad block）
最後更新：2026-05-20
適用範圍：Claude Code `/init-project` skill 定義；Instance Bootstrap 流程
優先級：高

# /init-project Skill

## 用途

Use this skill when the user triggers `/init-project` in a freshly cloned Instance repo. The skill runs the one-time Bootstrap flow for a concrete project Instance.

This skill is dialogue-guided. It does not accept direct user parameters in the slash command.

## 觸發語

- `/init-project`
- Chinese alias: `/初始化專案`, via `.claude/skills/初始化專案/SKILL.md`

## 觸發協議

Primary authority:

- `00_protocol/00_i_專案初始化協議.md`, all 10 sections

Required references:

- `_design/TASKS.md` v1.4 §A.5
- `_design/SPEC.md` §5.4 / §5.4a and §8
- `_design/ARCHITECTURE.md` §3.3
- `_design/DATA_FORMAT_SPEC.md` §3.2
- `_design/DECISIONS_LOG.md` §6.7.2 / §6.7.3 for D-042
- `_design/DECISIONS_LOG.md` §6.9.2 for D-047
- `_design/registries/entity_type_registry.template.yaml`
- `_design/registries/qa_type_registry.template.yaml`
- `_design/registries/issue_type_registry.template.yaml`

If chat instructions conflict with these files, follow the files above.

## 啟動前檢查

Before Stage 1, verify (對齊 `00_i §2`):

- current folder is the Instance repo root
- `AGENTS.md`, `README.md`, `00_protocol/`, and `01_world/` through `09_quality_assurance/` exist
- `00_protocol/00_b_反ai味檢查表.md`, `00_protocol/00_c_台詞輸出格式.md`, and `00_protocol/00_d_工作流總覽.md` exist
- the three Template registry sources under `_design/registries/` exist
- `.protocol_version` is absent, or present without a completed Bootstrap entry
- no obvious project content has already been written under `01_world/`, `03_characters/`, `05_plot/`, `07_scene_tasks/`, or `08_dialogue_outputs/`
- **(D-049 第一道防線)** no `.template_root` marker file exists at repo root
- **(D-051 supersede D-049 第二道防線)** ~~原 D-049 第二道防線 over-broad block，移除~~（D-051；詳 DECISIONS_LOG v1.9 §6.13.2 D-051 + §6.16.2 D-053；本 skill 僅依 00_i §2 條件 #5 marker（`.template_root`）為 explicit Template-detect 信號）

If `.template_root` marker is present, stop and print:

```
## ⏸ 條件未滿足 / Prerequisites Not Met

**What：** 偵測到 `.template_root` 標記檔；此目錄被標識為 Template repo。
**Where：** repo root (cwd)
**Why：** 不允許在 Template repo 上跑 /init-project（會污染 Template）。
**下一步：** 若此目錄已 git clone 為新 Instance 並決定初始化：
  1. 移除 `.template_root` 標記檔（`rm .template_root` 或在 IDE / file explorer 內刪檔）
  2. 重新跑 `/init-project`
若此目錄是 Template repo 本身：請先 `git clone <template-url> <new-project-dir>` 到新目錄後在新目錄內跑。
```

<!-- D-051 supersede D-049 第二道防線：移除「registries-template 存在 + .protocol_version 不存在 → BLOCK」error block。原 D-049 block 在 fresh Instance clone 場景必然 false-positive；改以 00_i §2 條件 #5（`.template_root` marker）為唯一 explicit 信號。詳 DECISIONS_LOG v1.9 §6.13.2 D-051 + §6.16.2 D-053。 -->

If `.protocol_version.phase_log` already contains `phase: bootstrap` with `status: completed`, stop. Do not rerun Bootstrap. Suggest reviewing `.protocol_version` or moving to `/create-world`.

If `.protocol_version` exists but has no completed Bootstrap entry, list that fact and ask whether to abort. Do not overwrite silently.

## 流程

Run exactly five stages. Do not skip stages. Do not write before Stage 3 is explicitly approved.

### Stage 1 - Diagnosis

Follow `00_i` §3.

Print the prerequisite check summary, then ask the user for:

- project name
- repo name
- Template source
- Template commit, or `TODO`
- Bootstrap date, defaulting to today
- initial type description
- expected length / scale
- tone preference
- output format preference
- reference works

Return this report and do not write files:

```md
# Bootstrap 診斷報告

## 一、已確認基本資料

## 二、缺漏資料

## 三、可能需要微調的 Template 文件

## 四、不可在 Bootstrap 階段處理的內容

## 五、建議下一步
```

Do not turn project type, tone preference, or reference works into formal canon.

### Stage 2 - Exploration / Customization Candidates

Follow `00_i` §4.

Bootstrap customization is limited to:

| File | Allowed | Forbidden |
|---|---|---|
| `00_protocol/00_b_反ai味檢查表.md` | project-name placeholder, type/tone TODO, profanity scale candidate, death-handling preference candidate | formal world rules, characters, scenes |
| `00_protocol/00_c_台詞輸出格式.md` | Instance output preference note, naming preference, delivery-format TODO | new skill, engine export framework |
| `00_protocol/00_d_工作流總覽.md` | Instance usage order note, daily operation note | changes to general workflow principles |

Ask at most three questions at a time. Each question must state why it is asked and which file it may affect.

Everything outside `00_b` / `00_c` / `00_d` goes to the not-handled list.

### Stage 3 - Convergence

Follow `00_i` §5.

Print a "Bootstrap 收斂預告稿" containing:

- final basic data: `project_name`, `template_source`, `template_commit`, `bootstrap_date`
- approved customization list, limited to `00_b` / `00_c` / `00_d`
- not-handled list for worldbuilding, characters, relationships, outline, scene, dialogue, QA, or reference material
- files to be created or modified
- `TODO` / `INFERENCE` / `CONFLICT` counts

Do not enter Stage 4 until the user explicitly says `通過`, `OK`, or `寫檔`.

If the user changes anything, update and reprint the convergence draft. If the user says `中止` or `取消`, stop without writing, or rollback if Stage 4 has already begun.

### Stage 4 - Codex Execution

Follow `00_i` §6 and §6.1.

Execute this seven-step write order:

1. Write `.protocol_version`.
2. Copy `_design/registries/entity_type_registry.template.yaml` to `entity_type_registry.yaml`.
3. Copy `_design/registries/qa_type_registry.template.yaml` to `qa_type_registry.yaml`.
4. Copy `_design/registries/issue_type_registry.template.yaml` to `issue_type_registry.yaml`.
5. Create `10_art_assets/portrait/`, `bg/`, `cg/`, `sfx/`, `bgm/`, `voice/`, and `ui/`, each with `index.md` stub.
6. Create or update Instance root `.gitignore`, which must contain `export/`.
7. Apply approved `00_b` / `00_c` / `00_d` local customizations, then reread and verify all written files and headers.

Registry rules:

- pure copy only; do not edit registry content
- if any target registry already exists, stop and ask for a decision
- all three registries are required for Bootstrap completion

Asset directory rules:

- create only the seven D-044 subtypes: `portrait`, `bg`, `cg`, `sfx`, `bgm`, `voice`, `ui`
- do not create reserved subtypes such as `icon`, `effect`, `video`, or `shader`
- each `index.md` stub must contain the Chinese five-field header with `狀態：DRAFT`, `版本：v0.1`, Bootstrap date, subtype scope, and priority

`.gitignore` must include at least:

```text
# Export 產物不入版控（D-038 附帶第 3 項）
export/
```

`00_b` / `00_c` / `00_d` customization rules:

- `00_b`: only fill TODO or project-name placeholders inside existing anchors; do not rename or reorder anchors
- `00_c`: only add an "Instance 輸出偏好" note or TODO; do not add a skill or engine export framework
- `00_d`: only add an "Instance 使用備註" note or TODO; do not change the general workflow
- if any target file is LOCKED, stop that file edit and report a CONFLICT

### Stage 5 - Verification

Follow `00_i` §7.

Report:

- `.protocol_version` exists
- `project_name`, `template_source`, `template_commit`, and `bootstrap_date` exist
- `phase_log` has `phase: bootstrap` with `status: completed`
- three root registries exist
- seven `10_art_assets/` subtype directories and seven `index.md` stubs exist
- root `.gitignore` exists and contains `export/`
- `00_b` / `00_c` / `00_d` still have the Chinese five-field header
- actual customizations match the approved list
- recommended next step is `/create-world`

Do not automatically run `/create-world`.

## `.protocol_version` 寫入規範

Write YAML aligned to `00_i` §10.2:

```yaml
template_source: github.com/<user>/game-dialogue-bible-template
template_commit: <commit-sha-or-TODO>
bootstrap_date: YYYY-MM-DD
project_name: <作品名>

customizations:
  - file: 00_protocol/00_b_反ai味檢查表.md
    type: 專案化
    action: append_todo
    note: <已拍板微調摘要>

bootstrapped_registries:
  - source: _design/registries/entity_type_registry.template.yaml
    target: entity_type_registry.yaml
    version: v0.3
  - source: _design/registries/qa_type_registry.template.yaml
    target: qa_type_registry.yaml
    version: v0.3
  - source: _design/registries/issue_type_registry.template.yaml
    target: issue_type_registry.yaml
    version: v0.1

bootstrapped_directories:
  - path: 10_art_assets/portrait/
  - path: 10_art_assets/bg/
  - path: 10_art_assets/cg/
  - path: 10_art_assets/sfx/
  - path: 10_art_assets/bgm/
  - path: 10_art_assets/voice/
  - path: 10_art_assets/ui/

bootstrapped_files:
  - path: .gitignore
    content_summary: "至少含 export/ 一行"

phase_log:
  - phase: bootstrap
    date: <ISO date>
    skill: /init-project
    status: completed
    created_entities: []
    scene_ids: []
    customizations:
      - file: 00_protocol/00_b_反ai味檢查表.md
        type: 專案化
        action: append_todo
        note: <已拍板微調摘要>
```

Rules:

- `status` is formalized by D-042; it is not tentative.
- Valid `phase_log.status` values are `completed`, `in_progress`, and `aborted`.
- The first completed Bootstrap entry must be `phase: bootstrap`, `skill: /init-project`, and `status: completed`.
- Detect the Template commit, but guard against recording the Instance's own commit as the Template commit. Write a real SHA only if ALL hold: git is available, the Instance has its own `.git`, AND the Instance has made no local commits since clone (so `git rev-parse HEAD` still points at the cloned Template commit; ideally corroborate via `git remote -v` matching `template_source`). Otherwise — git unavailable, `.git` missing, local commits already exist, or HEAD cannot be confirmed as the Template commit — write `template_commit: TODO` and emit a WARN in the validation report so the user backfills the real Template SHA (per 00_i §8 #9). (F5 / NEW_REQ_29)
- Do not put real project-specific `.protocol_version` values in this SKILL.md file.

## 輸入

Required: project name, repo name, Template source, Bootstrap date.

Recommended: Template commit, type description, expected length, tone preference, output format preference, reference works.

Missing required fields block Stage 4. An unknown or unconfirmable Template commit may proceed only as `TODO` (see the detection guard above).

## 輸出

May create:

- `.protocol_version`
- `entity_type_registry.yaml`
- `qa_type_registry.yaml`
- `issue_type_registry.yaml`
- `.gitignore`
- `10_art_assets/<portrait|bg|cg|sfx|bgm|voice|ui>/index.md`

May modify only after approval:

- `00_protocol/00_b_反ai味檢查表.md`
- `00_protocol/00_c_台詞輸出格式.md`
- `00_protocol/00_d_工作流總覽.md`

## 邊界

The skill must not:

- modify LOCKED files
- allow Bootstrap customization of `00_a`, `00_e` through `00_l`, or `01_world/` through `09_quality_assurance/`
- modify `00_protocol/00_i_專案初始化協議.md`
- modify `scripts/`, `_tools/frontend/`, or registry Template files
- create worldbuilding, characters, relationships, outlines, scene tasks, dialogue, QA reports, or final-gating records
- create `/create-world`, `/status`, `/check-gaps`, or any other skill
- run `/create-world` or downstream skills automatically
- rerun on an Instance whose `.protocol_version.phase_log` already has completed Bootstrap
- write real `.protocol_version` project values inside this SKILL.md

## 錯誤處理 / Rollback

Before Stage 4 writes, record what existed and what this run creates. Rollback only this run's changes.

Rollback requirements:

- any Stage 4 failure rolls back already written Stage 4 files
- registry copy failure rolls back `.protocol_version`
- later failures roll back copied registries, created `10_art_assets/`, `.gitignore` changes made by this run, and approved `00_b` / `00_c` / `00_d` edits
- rollback failure must list remaining paths for manual cleanup

If `.protocol_version` already exists, list it and ask whether to abort; do not overwrite. If a target registry exists, stop and ask for a decision.

If an abort entry is written to `phase_log`, use `status: aborted` with `abort_reason` and `detail`, per D-042.

## 錯誤呈現規則

Use the `ARCHITECTURE.md` §3.3.1 four-part shape:

- `## ✗ 無法執行 / Cannot Proceed` for user-action errors
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for unmet system state
- include What / Where / Why / 下一步
- do not show stack traces, raw enum keys, or parser internals
