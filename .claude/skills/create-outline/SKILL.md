---
name: create-outline
description: "建立主線 P 的 Phase B skill。依 00_g 大綱創建協議 v0.2 跑 5 階段，動態讀 issue_type_registry.yaml 的 00_g_outline 議題清單，建立 05_a 主線骨架與 D-050 允許的 05_c/05_d/05_e 高層補充，並更新 phase_log。"
---

狀態：DRAFT
版本：v0.4（Batch 2 大綱鏈 D-067+D-068+D-069 — D-067 加 pattern pack 載入（可選 mode）+ Required references + Stage 2 outline table；D-068/D-069 加保全層提示 + 個人線消耗檢查 + ## 邊界 05_f/05_g 唯讀條 + 個人線降權條；本檔 v0.3 → v0.4。歷史：v0.3 8th master patch round 2 R8-MI-05 D-050 子裁決 1 block 例外列表補 D-053 /create-world exception）
最後更新：2026-06-02
適用範圍：/create-outline skill runtime instructions
優先級：高

# /create-outline Skill

## 用途

Use this skill when the user triggers `/create-outline` to create the top-level plot entity `P` in an already bootstrapped Instance repo.

This skill builds the main plot spine: one-line premise, core conflict, theme, want-vs-need, structure, compliance checks, scale positioning, and genre-drift risk baseline. It does not create detailed chapter outlines, scene indexes, scene task packs, or dialogue.

Runtime outputs may include:

- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_c_角色弧線表.md` only when issue 4 triggers a high-level character-arc alignment note
- `05_plot/05_d_資訊揭露表.md` only when issue 4 triggers a high-level information-control note
- `05_plot/05_e_伏筆與回收表.md` only when issue 5 triggers a high-level foreshadowing-scale note
- `.protocol_version.phase_log`

The required entity created by this skill is the single entity `P`. This skill does not create `CH-*` entities or write `05_b` chapter shells; those belong to `/create-detailed-outline`.

## 觸發語

- English trigger: `/create-outline`
- Chinese alias wrapper: `/建立大綱`, via `.claude/skills/建立大綱/SKILL.md`

This command accepts no direct user parameters. The user provides outline material during the five-stage conversation.

## 觸發協議

Primary authority:

- `00_protocol/00_g_大綱創建協議.md` v0.2, all five stages and sections 1-12

Required references:

- `_design/TASKS.md` §B.6
- `_design/ARCHITECTURE.md` §3.2, §3.3, §3.3.0, §3.3.1, §3.3.2
- `_design/SPEC.md` §5.1, §5.3, §5.4, §16
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.3 and §1.3.2 full question scripts
- `_design/DECISIONS_LOG.md` §6.9.2 D-047, §6.11.2 D-049, and §6.12.2 D-050
- `_design/registries/issue_type_registry.template.yaml`
- `_design/registries/pattern_pack_registry.template.yaml` (read-only; optional pattern pack mode — D-067)

If chat instructions conflict with the files above, follow the stricter combined prerequisite. TASKS gives the B.6 summary; UD and `00_g` define the detailed protocol behavior. For write boundaries, D-050 supersedes any broader write set described by `00_g` v0.2.

## 啟動前檢查

Before Stage 1, verify all of the following.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `01_world/`, `03_characters/`, and `05_plot/`.
2. **D-049 first defense:** no `.template_root` marker file exists at repo root.
3. **D-049 second defense:** it is not true that `_design/registries/*.template.yaml` exists while `.protocol_version` is absent.
4. `.protocol_version` exists.
5. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
6. `_design/expected_entities.yaml` exists.
7. `_design/registries/issue_type_registry.template.yaml` exists and is readable.

### Protocol-specific prerequisites

1. `W-rules`, `V`, and `W-language` each exist and are at least `REVIEW`.
2. At least one main `C-*` exists at `DRAFT` or above. If no main character exists, print the `00_g` warning and require explicit `prereq_waived: true` user confirmation before continuing.
3. No existing completed `P` entity is already present in frontmatter or phase_log. If it exists, stop and suggest `/iterate-outline`.
4. Target files are not `LOCKED`.
5. No active or in-progress phase_log entry is currently writing `P`.

`/create-outline` should be conservative about waivers. The world and vocabulary prerequisites should not be bypassed casually; if the user insists, the waiver must be explicit and recorded in the convergence preview and phase_log.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user.

### Stage 1 - Diagnosis

Start with this prompt:

```md
主線是這個作品的骨幹。請貼出你對主線的長段想法，至少包含一句話定位、核心衝突、想表達的主題、開頭結尾、可能的章節節奏。如果你還在發散階段，貼草稿也行，我會幫你診斷哪些已成型、哪些是空的。
```

After the user responds, produce a chat-only diagnostic report using `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode.

Diagnose at least:

- whether the main plot sentence shows protagonist, want, and resistance
- whether want and need are implied
- whether the structure can carry the expected length
- W-rules and V compliance
- character-voice compliance for the main character
- genre-drift risks against `00_b`

**Raw-detail preservation prompt (D-069, F16):** If the user supplies a large batch of level- or chapter-level raw detail that the concise `05_a` spine will compress, state in the diagnostic report that compressed raw motivation, side-plot hooks, gameplay conditions, and pre/post-battle information can be preserved by the user in a DRAFT file `05_plot/05_f_<topic>_原始細節備忘.md` (default `05_plot/05_f_關卡原始細節備忘.md`). That file must carry the Chinese five-field header with 狀態：DRAFT (it is scanned by `check_headers`), `entities: []`, `depends_on: [P]`, `weight: {}`; it is never logged in `.protocol_version`, never creates `CH-*`/`S-*`, and stays DRAFT. This skill never writes it (not on the D-050 write list); it is a user-maintained, read-only data source. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.3.3.

End Stage 1 by previewing that Stage 2 will dynamically load the `00_g_outline` issue list.

### Stage 2 - Exploration

At the start of Stage 2, load and print the dynamic issue list from `00_g_outline`.

If an optional pattern pack is enabled (see `## pattern pack 載入（可選 mode，D-067）`) and it carries an `outline_table`, you may organize the exploration in game-design language using that table's columns (e.g. 關卡 / 開戰前功能 / 戰鬥功能 / 戰鬥後功能 / 玩家新增資訊 / 後續鉤子 / 禁止提前揭露) and defer heavy literary analysis. This is an optional output mode only; it does not add issues and does not change the D-050 write boundary.

Ask at most three questions at a time. Each question must include why it matters and which file or section the answer may affect. Allow `跳這題`, `先跳到議題 X`, and `中止`.

Core issue script mapping:

| id | issue | full script authority |
|---|---|---|
| 1 | 必先三件事 | UD §1.3.2 §10.1 |
| 2 | 想要 vs 需要測試 | UD §1.3.2 §10.2 |
| 3 | 結構選擇 | UD §1.3.2 §10.3 |
| 4 | 與世界規則、角色合規性檢查 | UD §1.3.2 §10.4 |
| 5 | 規模定位 | UD §1.3.2 §10.5 |
| 6 | 類型偏移風險清單 | UD §1.3.2 §10.6 |

Do not ask about split rules as a user-facing issue. Split rules are Stage 4 mechanics and appear only in the Stage 3 preview.

### Stage 3 - Convergence

Create a chat-only outline convergence preview and wait for explicit user confirmation.

The preview must include:

1. Final main plot sentence for word-by-word approval.
2. Final core conflict sentence for word-by-word approval.
3. Final theme sentence for word-by-word approval.
4. Want-vs-need summary.
5. Structure preview: act model and chapter count range, without `05_b` chapter-shell writes.
6. Scale positioning preview for `05_a §5`, plus any D-050-legal `05_e` high-level foreshadowing-scale placeholder.
7. Genre-drift risk preview for `05_a §6`.
8. Any approved high-level TODO placeholders for `05_c`, `05_d`, or `05_e` that are triggered by issue 4 or issue 5.
9. Stage 4 split plan with target files and write modes.
10. `TODO`, `INFERENCE`, and `CONFLICT` lists.
11. Skipped `STRONGLY_PREFERRED` issues and downstream impact.
12. **Personal-line consumption check (D-068, F19):** per chapter or chapter-range, list which character functions the main plot uses and whether it touches and consumes that character's personal-line climax. If a main-plot chapter would write content that belongs to a character's personal line, mark `<!-- INFERENCE: ...; 待人類確認 -->` or `<!-- CONFLICT(...): 請人類拍板 -->` and ask the user; do not write it as canon. This is a chat-only check; any recorded result is appended only to the existing `05_a §4` compliance section. The 12-段 personal-line structure baseline is read, when present, from the user-maintained DRAFT file `05_plot/05_g_<角色>_個人線結構備忘.md`. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.3.2.
13. **Raw-detail preservation reminder (D-069, F16):** list raw details left out of `05_a` due to spine concision this run and suggest the user store them in `05_plot/05_f_*_原始細節備忘.md`. This skill does not write that file.

Allowed user replies:

- `通過`, `OK`, or `寫檔`: proceed to Stage 4.
- requested changes: revise and reprint the convergence preview.
- `中止` or `取消`: stop without writing, or rollback if Stage 4 has already started.

If any unresolved `CONFLICT` remains, do not enter Stage 4.

### Stage 4 - Execution

Before writing, re-check target file headers and lock status. Do not overwrite `LOCKED` content.

Write in this fixed order:

1. `05_plot/05_a_主線大綱模板.md`
2. `05_plot/05_c_角色弧線表.md`, only if issue 4 triggers a high-level character-arc alignment note.
3. `05_plot/05_d_資訊揭露表.md`, only if issue 4 triggers a high-level information-control note.
4. `05_plot/05_e_伏筆與回收表.md`, only if issue 5 triggers a high-level foreshadowing-scale placeholder.

Do not write `05_b` chapter shells, `CH-*` entities, `00_protocol/`, chapter details, scene indexes, scene task packs, detailed information-reveal schedules, detailed foreshadowing plans, or dialogue. Detailed outline content belongs to Wave 8 `/create-detailed-outline`.

#### Split Rules

Apply `00_g` §10.7:

| source | target | write mode |
|---|---|---|
| 10.1 必先三件事 | `05_a §1` three subsections | overwrite |
| 10.2 想要 vs 需要 | `05_a §2` three subsections | overwrite |
| 10.3 結構選擇 | `05_a §3` only | overwrite |
| 10.4 合規檢查 | `05_a §4`, optional high-level `05_c` / `05_d` TODO placeholder if explicitly approved | overwrite and optional append |
| 10.5 規模定位 | `05_a §5`, optional high-level `05_e` foreshadowing-scale placeholder if explicitly approved | overwrite and optional append |
| 10.6 類型偏移風險 | `05_a §6` only | overwrite |

`05_c`, `05_d`, and `05_e` writes must stay high-level and P-scoped. They must not create chapter rows, scene rows, detailed reveal schedules, or `CH-*` entities.

#### Frontmatter Rules

When creating or repairing target frontmatter, preserve the Chinese five-field header and apply protocol-aligned YAML blocks:

```yaml
---
entities: [P]
depends_on: [W-rules, V, W-language, C-<main-character>]
weight:
  P: 1.0
---
```

Do not create `CH-*` frontmatter in this skill. `05_c`, `05_d`, and `05_e` may only be touched when the approved Stage 3 plan keeps the contribution P-scoped and follows the local file pattern.

#### Missing, Inference, and Conflict Markers

Use these markers exactly when needed:

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

Rules:

- Missing any part of issue 1 blocks Stage 3.
- Missing issue 2 may proceed only with `05_a §2` TODO.
- Missing issue 3 means `05_a §3` records the structural gap; do not write `05_b` chapter shells.
- Missing issue 4 means `05_a §4` must mark compliance unchecked.
- Missing issue 5 means do not write the optional `05_e` high-level foreshadowing-scale placeholder.
- Missing issue 6 means `05_a §6` records the genre-drift risk gap.
- Do not turn inferred main-character arc material into confirmed character-card content.

### Stage 5 - Validation

After Stage 4 writes succeed, automatically invoke `/status`.

Show:

1. Files created or updated by this skill.
2. Whether `P` now appears.
3. Current completion level for `P`.
4. Confirmation that `created_entities` is the single literal `P` and no `CH-*` entities were created.
5. Whether `.protocol_version.phase_log` contains `phase: create-outline`, `skill: /create-outline`, `status: completed`, and `created_entities: [P]`.
6. Remaining TODO / INFERENCE / CONFLICT markers.
7. Next suggested actions: human B.6.5 main-plot REVIEW gate, then `/create-detailed-outline` in Phase B Wave 8 to add `05_b` chapter shells and `CH-*` entities.

Do not automatically invoke `/create-detailed-outline` and do not run the B.6.5 human REVIEW gate.

## pattern pack 載入（可選 mode，D-067）

This skill may load an optional, read-only genre pattern pack to offer a game-design-language output mode. It never writes or modifies the registry.

- **Source / fallback:** load `<instance_root>/pattern_pack_registry.yaml` if the user has copied and customized it; otherwise fall back to `_design/registries/pattern_pack_registry.template.yaml` and print `WARN`. If both are missing or YAML parsing fails, skip the pattern pack mechanism and run the normal flow (packs are opt-in value-add, not required — unlike the issue registry, a missing pattern pack never blocks).
- **Activation (opt-in):** read `00_b §1` 作品類型語氣定位 only as a hint to suggest a candidate pack; actual activation requires the user to mark `enabled: true` in the instance registry or to confirm in Stage 1. Never auto-apply a pack from `00_b §1` free-text. If no pack is enabled or none matches, run the normal flow (zero behavior change; non-game works are unaffected).
- **Consumption (F17):** when an enabled pack carries `outline_table`, offer it in Stage 1/2 as an optional structured output mode — organize level/chapter function in game-design language first and defer heavy literary analysis. The user may choose table-first or literary-first.
- **Write boundary unchanged:** any table content lands only in the existing D-050 targets (`05_a`, and conditional `05_c`/`05_d`/`05_e`). Loading a pack never adds a write target, never creates an enum/entity, and never writes the registry. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.3.2 §10.3.

## 議題清單動態載入

This skill must use D-047 dynamic issue construction. Do not hardcode the final Stage 2 issue list as the live list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` once before Stage 2.

- If the Instance registry is missing, load `_design/registries/issue_type_registry.template.yaml` once as fallback and print `WARN`.
- If both are missing or unreadable, stop before Stage 2.
- If the user edits the registry during the session, tell them to restart `/create-outline`.

### Skill Key

Use only the `00_g_outline` skill key.

Expected sections:

- `core.00_g_outline`
- `user_extensions.00_g_outline`
- `core_overrides.00_g_outline`

### Dynamic Issue List Algorithm

Build Stage 2 issue list as:

```text
core + user_extensions - core_overrides
```

Execution details:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_g_outline[*].skip_id`.
3. Ignore and warn for locked core overrides.
4. Remove unlocked skipped core issues.
5. Sort `user_extensions.00_g_outline` by ascending `id` and append after core.
6. Use `question_summary` only as opener.
7. For core issues, use `protocol_ref` to fetch the complete script from UD §1.3.2.
8. For user extensions, ask from `question_summary`, record the answer, and do not invent write authority unless the user confirms how it maps into Stage 4.

### Required Level Behavior

- `REQUIRED`: user must answer before Stage 4.
- `STRONGLY_PREFERRED`: user may skip; record the gap in phase_log and mark TODO in the relevant file or preview.
- `OPTIONAL`: user may skip without phase_log gap detail.

Reject before Stage 2 if YAML parsing fails, the `00_g_outline` key is missing, a user extension id is below 100, ids collide, `required_level` is invalid, `locked` is not boolean, or any required issue field is missing.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed.

Use concrete entity IDs only. For this skill the created entity is the literal `P`.

```yaml
- phase: create-outline
  date: <ISO date>
  skill: /create-outline
  status: completed
  created_entities:
    - P
  entities_touched:
    - P
    - C-<main-character>
  prereq_waived: <true|false>
  issue_completions:
    "<issue id>": <answered|skipped|required_blocked>
```

If aborted, set `status: aborted`, include `abort_reason`, and do not count `P` as created.

## 輸入

The user provides:

- `/create-outline` with no direct parameters.
- Long-form main-plot material.
- Answers to dynamic issue questions.
- Explicit skip decisions.
- Conflict decisions.
- Confirmation to write.

## 輸出

Runtime output includes:

- Stage 1 diagnostic report in chat.
- Stage 2 dynamic issue list and progress updates in chat.
- Stage 3 convergence preview in chat.
- Stage 4 file writes only after user approval.
- Stage 5 `/status` validation output.

Runtime file outputs are limited to the files listed in `## 用途`.

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `05_plot/05_a_主線大綱模板.md` | 主體；`P` entity 主要寫檔位置 |
| 合法寫檔 | `05_plot/05_c_角色弧線表.md` | 僅 issue 4 觸發的高層角色弧線 alignment note |
| 合法寫檔 | `05_plot/05_d_資訊揭露表.md` | 僅 issue 4 觸發的高層資訊控制 note |
| 合法寫檔 | `05_plot/05_e_伏筆與回收表.md` | 僅 issue 5 觸發的高層伏筆規模 placeholder |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: create-outline` / `created_entities: [P]` 等 runtime log |
| 不寫 | `05_plot/05_b_章節結構模板.md` | chapter shell 屬 CH skill B.7 `/create-detailed-outline` scope |
| 不寫 | `00_protocol/` | `/create-*` skill 嚴禁修改 protocol；唯一例外不是本 skill |
| 不創 | `CH-*` entities | `P` skill 只創單一 `P`；CH entities 屬 `/create-detailed-outline` |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/` | 任何寫入都屬 D-050 越界 |

## 邊界

The skill must not:

- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, or registry Template files
- modify existing Phase A skills or wrappers
- create or rewrite characters, relationships, detailed chapters, chapter shells, scenes, task packs, or dialogue
- create `CH-*` entities
- populate `05_c`, `05_d`, or `05_e` with detailed chapter, reveal, or foreshadowing content
- auto-trigger downstream skills
- run B.6.5 human REVIEW gate
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing `P` in `/create-outline`
- write real project-specific `.protocol_version` values inside this `SKILL.md`
- write or modify `05_plot/05_f_*_原始細節備忘.md` or `05_plot/05_g_*_個人線結構備忘.md`; these are user-maintained DRAFT data sources and this skill is strictly read-only to them (D-069 / D-068)
- consume or write out a character's personal-line climax (including adult-content segments) in the main-plot flow; it may only mark "the main plot uses this character function here" and must leave personal-line content to that character's dedicated flow. Main-plot completion contributes 0 to a personal-line climax segment (convention only; no weight/parser change) (D-068, F19)

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為下列範圍；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

## 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If a target file becomes `LOCKED` or changes unexpectedly between Stage 3 and Stage 4, stop before writing that file and ask for a decision.

If any Stage 4 write fails:

1. Stop further writes.
2. Roll back files written by this skill in the current run when possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly which files were written, rolled back, or require manual inspection.

Do not hide partial-write risk behind a success message.

## 錯誤呈現規則

Use these headings:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repository state or prerequisite problems.

Each error must include:

- `What`: what failed.
- `Where`: file, section, command, or stage.
- `Why`: why the skill cannot continue.
- `下一步`: one concrete action the user should take.

For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, enum keys, or raw YAML objects in user-facing errors.

