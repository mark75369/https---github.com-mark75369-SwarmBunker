---
name: create-org
description: "建立組織 ORG-<name> 的 Phase B skill。依 00_n 組織創建協議 v0.2 跑 5 階段，動態讀 issue_type_registry.yaml 的 00_n_organization 議題清單（7 議題對應 ORG card 7 段），建立非人格組織 / 制度 / 體系對抗源節點。寫檔嚴格依 D-050 子裁決 2 限定 11_organizations/ 目錄；不建聲線卡、不進 /dialogue-write 為說話者、嚴禁寫 00_protocol/ 與 03_characters/。"
---

狀態：DRAFT
版本：v0.2（F8 Phase 3 / D-074 amendment — user 拍板 §13 Q1 7 段 + Q2 issue-ful：改動態讀 issue_type_registry 00_n_organization key（比照 create-character）+ ORG card 6→7 段（加組織結構/層級）；本檔 v0.1 → v0.2）
歷史紀錄：v0.1（F8 Phase 3 3a — D-074 拍板；clone create-character 形狀、issue-less、ORG 6 段 card、無聲線卡）
最後更新：2026-06-03
適用範圍：/create-org skill runtime instructions
優先級：高

# /create-org Skill

## 用途

Use this skill when the user triggers `/create-org <name>` to create one `ORG-<name>` organization entity (組織 / 非人格反派 / 組織型對抗源：公司 / 制度 / 機構 / 體系 / 殘留或已解散組織) in an already bootstrapped Instance repo.

This skill creates an organization node that downstream `P` / `S` / `R` / `C` entities can depend on or cross-reference by stable ID. It does NOT create characters, voice cards, relationships, plot, scenes, task packs, dialogue, or QA reports.

Runtime outputs may include:

- `11_organizations/<name>.md`
- `.protocol_version.phase_log`

**核心不變量（不可違反）：**
- **ORG-* 永無聲線卡**；本 skill 不寫 `03_characters/`。
- **ORG-* 不進 `/dialogue-write` 為說話者**（組織不會說話）；殘留文件語體僅在 card §7 留 hint，方向 B 才正式做。

## 觸發語

- English trigger: `/create-org <name>`
- Chinese alias wrapper: `/建立組織 <name>`, via `.claude/skills/建立組織/SKILL.md`

The command argument is only the organization name. It does not replace the five-stage conversation. One run creates one `ORG-<name>`; for multiple organizations, split into separate runs.

## 觸發協議

Primary authority:

- `00_protocol/00_n_組織創建協議.md` v0.2, all five stages and sections 1-13

Required references:

- `_design/ARCHITECTURE.md` §3.2, §3.3, §3.4
- `_design/SPEC.md` §5.1, §5.3, §5.4
- `_design/DECISIONS_LOG.md` §6.25 D-074, §6.23.2 D-071, §6.12.2 D-050
- `_design/registries/issue_type_registry.template.yaml`（`00_n_organization` key）
- `entity_type_registry.yaml`（ORG core 型別權威）

If chat instructions conflict with the files above, follow the files above. For write boundaries, D-050 supersedes any broader write set. If the target file is `LOCKED`, stop and ask for explicit confirmation before any write attempt.

> **issue-ful（D-074 amendment；§13 Q2 user 拍板）：** 本 skill **讀** `issue_type_registry.yaml` 的 `00_n_organization` key，動態構建 Stage 2 議題清單（比照 `/create-character` 讀 `00_f_character`）。7 個 core 議題對應 ORG card 7 段。

## 啟動前檢查

Before Stage 1, verify all of the following.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `01_world/`, and `_design/`.
2. **D-049 first defense:** no `.template_root` marker file exists at repo root.
3. `.protocol_version` exists.
4. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
5. `_design/expected_entities.yaml` exists.
6. `_design/registries/issue_type_registry.template.yaml` exists and is readable.

If `.template_root` is present, stop with `⏸ 條件未滿足` and tell the user this directory is still marked as the Template repo.

### Protocol-specific prerequisites

1. `W-rules` exists and is at least `REVIEW` (ORG needs world context to judge antagonism).
2. The command includes an explicit organization name.
3. The target `ORG-<name>` is not already claimed by existing frontmatter.
4. The target file `11_organizations/<name>.md` is not `LOCKED`.
5. No active or in-progress phase_log entry is currently writing the same `ORG-<name>`.

If the target entity already exists, stop before Stage 1 and tell the user to use `/iterate-org`. Do not overwrite an existing same-name `ORG-<name>` in `/create-org`.

**目標可建性檢查（non-character / non-place gate）：** judge whether the target is a non-personified organization / system / institution. If the description shows it is actually a speaking character, stop and recommend `/create-character` instead (呼應 `/create-character` Stage 1.0 gate 的反向落點). Never build an ORG for a target that can carry character voice.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user.

### Stage 1 - Diagnosis

Start with this prompt:

```md
我們要建立組織 `ORG-<name>`。請先貼出你對這個組織的長段想法；可以包含它是什麼組織 / 制度 / 體系、為什麼是對抗源、內部結構或層級、現在以什麼形式存在（文件 / 條文 / 設施 / 流程 / 已破產解散）、影響哪些角色與地點、未來在主線怎麼被引用。
```

After the user responds, produce a chat-only diagnostic report using `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode and `00_n` §3.2:

- whether the target is truly a non-personified ORG (not a speaking character)
- clarity of its antagonism source and form
- internal structure / hierarchy if any
- residual form / dissolved status
- W-rules compliance
- downstream landing (which characters / places / plot segments it affects)

既有素材：when the user references existing source material (殘留文件 / 設定文件), read it from `<instance_root>/_source_materials/`（可讀不可寫；本 skill 永不寫該目錄）. docx 無法解析時印 `WARN：docx 無法自動解析，請改貼純文字或用副對話轉述`，不靜默跳過。

End Stage 1 by previewing that Stage 2 will dynamically load the `00_n_organization` issue list (7 core issues → ORG card 7 sections).

### Stage 2 - Exploration

At the start of Stage 2, load and print the dynamic issue list from `00_n_organization` (per `00_n` §4.0). Ask at most three questions at a time; each must state why it matters and which downstream skill / ORG card section it affects. Allow `跳這題`, `先跳到議題 X`, and `中止`.

Core issue → card-section mapping (full scripts in `00_n` §4.1):

| id | issue | required_level | ORG card 段 |
|---|---|---|---|
| 1 | 組織本質 | REQUIRED | §1 |
| 2 | 對抗性質與來源 | REQUIRED | §2 |
| 3 | 組織結構/層級 | STRONGLY_PREFERRED | §3 |
| 4 | 殘留型態 | STRONGLY_PREFERRED | §4 |
| 5 | 影響範圍 | STRONGLY_PREFERRED | §5 |
| 6 | 下游 hooks | STRONGLY_PREFERRED | §6 |
| 7 | 文件語體 hint | OPTIONAL | §7 |

Do not invent台詞 for the ORG; §6 hooks register downstream leads only and do not authorize downstream writes.

### Stage 3 - Convergence

Create a chat-only convergence preview and wait for explicit user confirmation. The preview must include:

1. The ORG ID `ORG-<name>` and one-sentence positioning (from issues 1/2).
2. ORG card 7-section write preview for `11_organizations/<name>.md`.
3. Frontmatter preview (`entities` / `depends_on` / `weight` / 5-field header).
4. `TODO`, `INFERENCE`, and `CONFLICT` lists.
5. Skipped `STRONGLY_PREFERRED` issues and downstream impact.

Allowed user replies: `通過` / `OK` / `寫檔` → Stage 4; requested changes → revise and reprint; `中止` / `取消` → stop without writing (or rollback if Stage 4 started). If any unresolved `CONFLICT` remains, do not enter Stage 4.

### Stage 4 - Execution

Before writing, re-check target file header and lock status. If `11_organizations/` does not exist, create it on-demand (同 `10_art_assets/` 慣例).

Write only `11_organizations/<name>.md` in the fixed 7-section order. Use local section replacement or append only.

#### Frontmatter Rules

```yaml
---
entities: [ORG-<name>]
depends_on: [W-rules]
weight:
  ORG-<name>: 1.0
---
```

Preserve the Chinese five-field header (狀態 DRAFT). Extend `depends_on` with related `C-*` / `V` per issue 5 影響範圍.

#### Missing, Inference, and Conflict Markers

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

- Missing REQUIRED issue (id 1 / 2) blocks Stage 4.
- Skipped `STRONGLY_PREFERRED` issue may proceed only with TODO markers and phase_log gap records.

### Stage 5 - Validation

After Stage 4 writes succeed, automatically invoke `/status`. Show:

1. Files created or updated by this skill.
2. The concrete `ORG-<name>` entity created.
3. Current completion level for the created ORG.
4. Whether `.protocol_version.phase_log` contains `phase: create-org`, `skill: /create-org`, `status: completed`, and `created_entities: [ORG-<name>]`.
5. Remaining TODO / INFERENCE / CONFLICT markers.
6. Next suggested skill: `/create-relationship <C-*> <ORG-*>` to wire a C↔ORG antagonism endpoint, or `/iterate-org` to refine.

Do not automatically invoke any downstream skill.

## 議題清單動態載入

This skill must use D-047 dynamic issue construction. Do not hardcode the final Stage 2 issue list as the live list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` once before Stage 2.

- If the Instance registry is missing, load `_design/registries/issue_type_registry.template.yaml` once as fallback and print `WARN`.
- If both are missing or unreadable, stop before Stage 2.
- If the user edits the registry during the session, tell them to restart `/create-org`.

### Skill Key

Use only the `00_n_organization` skill key. Expected sections: `core.00_n_organization` / `user_extensions.00_n_organization` / `core_overrides.00_n_organization`.

### Dynamic Issue List Algorithm

Build Stage 2 issue list as `core + user_extensions - core_overrides`:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_n_organization[*].skip_id`.
3. Ignore and warn for locked core overrides (id 1 / 2 are `locked: true`).
4. Remove unlocked skipped core issues.
5. Sort `user_extensions.00_n_organization` by ascending `id` and append after core.
6. Use `question_summary` only as opener; fetch the complete script from `00_n` §4.1 via `protocol_ref`.
7. For user extensions, ask from `question_summary`; do not invent write authority unless the user confirms how it maps into a Stage 4 section.

### Required Level Behavior

- `REQUIRED`: user must answer before Stage 4.
- `STRONGLY_PREFERRED`: user may skip; record the gap in phase_log and mark TODO in the relevant ORG card section.
- `OPTIONAL`: user may skip without phase_log gap detail.

Reject before Stage 2 if YAML parsing fails, the `00_n_organization` key is missing, a user extension id is below 100, ids collide, `required_level` is invalid, `locked` is not boolean, or any required issue field is missing.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed. Use concrete entity IDs only; do not write wildcard IDs such as `ORG-*`.

```yaml
- phase: create-org
  date: <ISO date>
  skill: /create-org
  status: completed
  created_entities:
    - ORG-<name>
  entities_touched:
    - ORG-<name>
  issue_completions:
    "1": <answered|skipped|required_blocked>
    "2": <answered|skipped|required_blocked>
```

If aborted, set `status: aborted`, include `abort_reason`, and do not count the entity as created.

## 輸入

The user provides: `/create-org <name>`; long-form organization material; answers to the dynamic issue questions; explicit skip decisions; conflict decisions; confirmation to write.

## 輸出

Runtime output includes Stage 1 diagnostic report, Stage 2 dynamic issue list + exploration, Stage 3 convergence preview, Stage 4 file writes (only after approval), and Stage 5 `/status` validation — all in chat except the single file write. Runtime file outputs are limited to the files listed in `## 用途`.

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `11_organizations/<name>.md` | ORG card 7 段 + frontmatter |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: create-org` / `created_entities` 等 runtime log |
| 合法讀取 | `<instance_root>/_source_materials/` | 可讀不可寫；殘留文件素材 |
| 合法讀取 | `<instance_root>/issue_type_registry.yaml`（fallback template）| 可讀不可寫；動態議題清單 |
| 不寫 | `00_protocol/`, `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, registry / template | 任何寫入都屬 D-050 越界 |

### ORG card 固定段骨架（§1–§7）

```md
## §1 組織本質
<是什麼組織 / 制度 / 體系；一句話定位 + 補充>

## §2 對抗性質與來源
<為何是對抗源；對抗形式：制度壓迫 / 殘留債務 / 體系慣性 / 其他>

## §3 組織結構/層級
<內部結構 / 層級：高層 / 執行層 / 殘留網絡 / 派系；哪一層是對抗主體>

## §4 殘留型態
<以什麼形式存在 / 被引用：文件 / 條文 / 設施 / 流程；是否已破產 / 解散>

## §5 影響範圍
<影響哪些角色 / 地點 / 主線段>

## §6 下游 hooks
<交給 /create-outline·/scene-task·/create-relationship 的鉤子（不含台詞）>

## §7 文件語體 hint
> 僅 hint；正式文件語體卡待方向 B（W-language 文件語體擴充）。
<殘留文件「讀起來」的語體線索：官腔 / 條文體 / 公告體…>
```

## 邊界

The skill must not:

- modify LOCKED files without explicit confirmation
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, or registry files
- modify existing skills or wrappers
- create characters, voice cards, relationships, vocabulary, outline, chapters, scenes, task packs, dialogue, or QA reports
- write `03_characters/` or build any voice card for the ORG
- treat the ORG as a speaking subject or feed it into `/dialogue-write`
- auto-trigger downstream skills
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing same-name `ORG-<name>`
- write a formal W-language document-style card in §7 (that is 方向 B; §7 keeps a hint only)
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG §6.12.2）：** 嚴禁修改任何 `00_protocol/` 內檔。例外為 `/init-project` + `/create-world`（D-053）；**本 skill 不在例外範圍**。

**D-050 子裁決 2（DECISIONS_LOG §6.12.2 + §6.25 D-074 新增 /create-org 列）：** 本 skill 寫檔目錄嚴格限 `11_organizations/`；越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）。

## 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing. If the target file becomes `LOCKED` or changes unexpectedly between Stage 3 and Stage 4, stop before writing and ask for a decision.

If the Stage 4 write fails:

1. Stop further writes.
2. Roll back the file written by this skill in the current run when possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly which file was written, rolled back, or requires manual inspection.

Do not hide partial-write risk behind a success message.

## 錯誤呈現規則

Use these headings:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repository state or prerequisite problems.

Each error must include `What` / `Where` / `Why` / `下一步`. For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, enum keys, or raw YAML objects in user-facing errors.
