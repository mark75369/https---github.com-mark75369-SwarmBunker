---
name: create-detailed-outline
description: "把主線 P 拆成章節 CH-* 與場景索引 S-*-* 的 Phase B skill。依 00_h 細綱創建協議 v0.2 跑 5 階段，動態讀 issue_type_registry.yaml 的 00_h_detailed_outline 議題清單；依 D-050 寫檔邊界只寫 05_b 與 06_a，並更新 .protocol_version.phase_log。"
---

狀態：DRAFT
版本：v0.4（Batch 2 大綱鏈 D-067+D-068+D-069 — D-067 加 pattern pack 載入（可選 mode）+ Required references + Stage 2 scene_types + Stage 4 06_a scene_type note；D-068/D-069 加 Stage 1 讀 05_f + 個人線消耗檢查 + ## 邊界 05_f/05_g 唯讀條 + 成人段降權條；本檔 v0.3 → v0.4。歷史：v0.3 8th master patch round 3 R9-INFO-02 D-050 雙 block 對齊）
最後更新：2026-06-02
適用範圍：/create-detailed-outline skill runtime instructions
優先級：高

# /create-detailed-outline Skill

## 用途

Use this skill when the user triggers `/create-detailed-outline` to turn an approved main plot `P` into chapter entities `CH-*` and scene-index entities `S-*-*` in an already bootstrapped Instance repo.

This skill expands the main plot into chapter rhythm and scene-index structure, while using the full `00_h` issue flow to keep character arcs, information reveals, foreshadowing, and high-risk handling aligned. By D-050, this skill may write only `05_b` and `06_a`; broader `00_h` write targets remain protocol context, not runtime write authority here.

Runtime outputs may include:

- `05_plot/05_b_章節結構模板.md`
- `06_scene_index/06_a_場景索引模板.md`
- `.protocol_version.phase_log`

The required entities created by this skill are concrete `CH-<nn>` chapter entities and concrete `S-<ch>-<n>` scene-index entities. Do not write wildcard entities such as `CH-*` or `S-*` into runtime phase_log entries.

## 觸發語

- English trigger: `/create-detailed-outline`
- Chinese alias wrapper: `/建立細綱`, via `.claude/skills/建立細綱/SKILL.md`

This command accepts no direct user parameters. The user provides detailed-outline material during the five-stage conversation.

## 觸發協議

Primary authority:

- `00_protocol/00_h_細綱創建協議.md` v0.2, all five stages and sections 1-12

Required references:

- `_design/TASKS.md` §B.7
- `_design/ARCHITECTURE.md` §3.2, §3.3, §3.3.0, §3.3.1, §3.3.2
- `_design/SPEC.md` §5.1, §5.3, §5.4, §17
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.4 and §1.4.2 full question scripts
- `_design/INTEGRATION_CONTRACTS.md` §4a Contract D
- `_design/DECISIONS_LOG.md` §6.9.2 D-047 and §6.12.2 D-050
- `_design/registries/issue_type_registry.template.yaml`
- `_design/registries/pattern_pack_registry.template.yaml` (read-only; optional pattern pack mode — D-067)

If chat instructions conflict with the files above, follow the stricter combined prerequisite. TASKS gives the B.7 summary; UD and `00_h` define detailed protocol behavior; D-047 defines dynamic issue construction; D-050 supersedes broader write targets and limits B.7 runtime writes to `05_b` and `06_a`. The `00_h` v0.2 implementation references split/frontmatter sections as §10.7 and §10.8; those are the active section numbers even if a starter prompt mentions §10.11 or §10.12.

## 啟動前檢查

Before Stage 1, verify all of the following.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, and `06_scene_index/`.
2. **D-049 first defense:** no `.template_root` marker file exists at repo root.
3. **D-049 second defense:** it is not true that `_design/registries/*.template.yaml` exists while `.protocol_version` is absent.
4. `.protocol_version` exists.
5. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
6. `.protocol_version.phase_log` contains `phase: create-outline` with `status: completed`.
7. `_design/expected_entities.yaml` exists.
8. `_design/registries/issue_type_registry.template.yaml` exists and is readable.

If `.template_root` is present, stop with `⏸ 條件未滿足` and tell the user this directory is still marked as the Template repo. If `.protocol_version` is absent while registry templates are present, stop with `⏸ 條件未滿足` and tell the user to run `/init-project` only in a real Instance after the Template marker decision is resolved.

### Protocol-specific prerequisites

1. `W-rules`, `V`, `W-language`, and `P` each exist and are at least `REVIEW`.
2. The `P` entity must be at least `REVIEW`. If `05_plot/05_a_主線大綱模板.md` or the local `P` contribution is still `DRAFT`, refuse and tell the user to run the B.6.5 main-plot REVIEW gate first.
3. All main `C-*` entities are at least `REVIEW`; if not, list the missing or under-reviewed characters and ask for a decision.
4. Project-specific `00_b §3` and `00_b §4` exist.
5. `05_plot/05_b_章節結構模板.md` template file exists (inherited from Template via `/init-project`; this skill will populate it with chapter shells `CH-*` in Stage 4 — outline flow does **not** write `05_b` per D-050 子裁決 2 CH 行).
6. No `phase: create-detailed-outline` entry with `status: completed` exists. If it exists, stop and suggest future `/iterate-detailed-outline` rather than overwriting.
7. Target files are not `LOCKED`. If any target file is `LOCKED`, stop before Stage 1 and ask for explicit file-by-file authorization.
8. No active or in-progress phase_log entry is currently writing `CH-*`, `S-*`, `05_b`, or `06_a`.
9. `<instance_root>/issue_type_registry.yaml` is readable, or `_design/registries/issue_type_registry.template.yaml` is readable as fallback with `WARN`.
10. The registry contains the `00_h_detailed_outline` skill key under `core`, `user_extensions`, and `core_overrides`.

`/create-detailed-outline` should be conservative about waivers. The `P` REVIEW gate is mandatory for B.7 and must not be waived by casual confirmation. If the user insists on a broader waiver for other prerequisites, record it in the convergence preview and phase_log.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user.

### Stage 1 - Diagnosis

Start with this prompt:

```md
細綱是把主線從一句話變成章節 × 場景的骨幹。請告訴我你希望這次做到哪個程度：(a) 章節節奏 + 弧線對齊，把每章功能定下來；(b) 上述 + 場景索引（每章拆幾場戲、每場一句話）；(c) 完整細綱（含資訊揭露 / 伏筆 / 高風險場景的處理方式）。預設我們跑 (c) 完整版。
```

If the user already has a detailed-outline draft, ask them to paste it before diagnosis.

**Raw-detail preservation read-in (D-069, F16):** Before diagnosis, if `05_plot/05_f_*_原始細節備忘.md` exists, read it together with `05_a` as a read-only data source and prefer it to recover raw level motivation, side-plot hooks, gameplay conditions, and pre/post-battle information that the `05_a` spine compressed. Never rewrite that file. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.4.1.

After the user responds, produce a chat-only diagnostic report using `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode.

Diagnose at least:

- chapter rhythm distribution: high / mid / low density
- protagonist arc alignment with the `P` want-vs-need baseline
- other main-character arc turning points or stable states
- information reveal timing and possible early leaks
- foreshadowing and payoff density, including unrecovered or overexplained items
- high-risk scene density, especially farewell, sacrifice, revelation, relationship rupture, and awakening scenes

End Stage 1 by previewing that Stage 2 will dynamically load the `00_h_detailed_outline` registry issue list. Say that the core registry currently contains six user-facing issues and that split rules are Stage 4 mechanics, not user-facing questions.

### Stage 2 - Exploration

At the start of Stage 2, load and print the dynamic issue list from `00_h_detailed_outline`.

Ask at most three questions at a time. Each question must include why it matters and which file or section the answer may affect. Allow `跳這題`, `先跳到議題 X`, and `中止`.

For every issue, present the five required parts:

1. `為什麼問`
2. `agent 怎麼問`
3. `使用者預期答什麼`
4. `agent 怎麼整理寫檔`
5. `拒答 / 跳題處理`

Core issue script mapping:

| id | issue | full script authority |
|---|---|---|
| 1 | 章節節奏分布 | UD §1.4.2 §10.1 |
| 2 | 角色弧線 × 章節矩陣對齊 | UD §1.4.2 §10.2 |
| 3 | 資訊揭露時間軸 | UD §1.4.2 §10.3 |
| 4 | 伏筆與回收佈點 | UD §1.4.2 §10.4 |
| 5 | 高風險場景識別 | UD §1.4.2 §10.5 |
| 6 | 高風險場景的「作品專屬正確處理方式」 | UD §1.4.2 §10.6 |

Do not ask about split rules as a user-facing issue. Split rules are Stage 4 mechanics and appear only in the Stage 3 preview.

Required issue handling:

- Issue 1 is required: each chapter must have a rhythm label or an explicit INFERENCE draft that the user confirms.
- Issue 2 is required at the protagonist-arc level. Other main-character rows may be TODO only when the user explicitly skips them.
- Issue 3 is required: the run needs a core information list, reveal timing, and reveal method before Stage 4.
- Issue 5 is required: the user must identify high-risk scenes or explicitly confirm that no high-risk scenes exist yet.
- Issues 4 and 6 are strongly preferred: skipping them is allowed only with phase_log gap records and TODO markers in the relevant preview or file section.

### Stage 3 - Convergence

Create a chat-only detailed-outline convergence preview and wait for explicit user confirmation.

The preview must include:

1. Chapter list and concrete `CH-<nn>` entity IDs.
2. Scene-index list and concrete `S-<ch>-<n>` entity IDs.
3. A chapter × scene × character-arc matrix.
4. Information reveal preview: per chapter, what may be revealed and what must remain hidden, for chat approval and `05_b` / `06_a` summary only.
5. Foreshadowing and payoff preview: per chapter, what to plant, recover, or avoid saying, for chat approval and `05_b` / `06_a` summary only.
6. High-risk scene list with `risk_type`, including items the user confirmed and items still only suggested.
7. High-risk handling preview, with an explicit note that D-050 blocks writing `00_b §6` in this skill.
8. Stage 4 split plan with target files and write modes.
9. `TODO`, `INFERENCE`, and `CONFLICT` lists.
10. Skipped `STRONGLY_PREFERRED` issues and downstream impact.
11. A `P` alignment check showing that no new chapter, main-plot turn, or character-core decision has been invented.
12. A not-handled list for material that belongs to `/iterate-character`, `/create-relationship`, `/scene-task`, `/dialogue-write`, or `/qa`.
13. **Personal-line boundary check (D-068, F19):** in the chapter × character-arc matrix, mark which entries are "the main plot uses a character function" versus "consumes a personal-line climax". The latter needs explicit user confirmation that it is intended and is not written out automatically here. Any recorded result goes only to the existing `05_b` chapter-section notes. Adult-content / personal-line climax segments may only be referenced, not expanded, in the detailed-outline flow; if a segment would be expanded, mark `<!-- TODO(個人線): belongs to that character's dedicated personal-line flow -->`. The 12-段 baseline is read, when present, from the user-maintained `05_plot/05_g_<角色>_個人線結構備忘.md`. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.4.2.

Allowed user replies:

- `通過`, `OK`, or `寫檔`: proceed to Stage 4.
- requested changes: revise and reprint the convergence preview.
- `中止` or `取消`: stop without writing, or rollback if Stage 4 has already started.

If any unresolved `CONFLICT` remains, do not enter Stage 4. If any `REQUIRED` issue lacks the minimum required answer, do not enter Stage 4.

### Stage 4 - Execution

Before writing, re-check target file headers and lock status. Do not overwrite `LOCKED` content without explicit file-by-file authorization.

Write in this fixed order:

1. `05_plot/05_b_章節結構模板.md`
2. `06_scene_index/06_a_場景索引模板.md`

Use local section replacement or append only. Do not rewrite unrelated sections. Do not create scene task packs, dialogue drafts, QA reports, characters, relationships, parser/schema files, `05_c`, `05_d`, `05_e`, or any `00_protocol/` edits.

#### Split Rules

Apply the `00_h` §10.7 and UD §1.4.2 §10.7 issue semantics inside the D-050 write boundary:

| source | target | write mode |
|---|---|---|
| 10.1 章節節奏分布 | `05_b §各章節奏` and `05_b §全局節奏曲線` | complete existing chapter shells |
| 10.2 角色弧線 × 章節矩陣 | `05_b` chapter sections and Stage 3 chat matrix | summarize approved arc stage per chapter; no `05_c` write |
| 10.3 資訊揭露時間軸 | `05_b` chapter sections and `06_a` scene rows | summarize reveal constraints; no `05_d` write |
| 10.4 伏筆與回收 | `05_b` chapter sections and `06_a` scene rows | summarize plant/payoff constraints; no `05_e` write |
| 10.5 高風險場景識別 | `06_a` scene index rows with `risk_type` notes | create or overwrite approved rows |
| 10.6 高風險處理方式 | `06_a` scene rows and Stage 5 TODO if needed | summarize handling notes; no `00_b §6` write |

**Pattern pack scene-type note (D-067, F18):** when an optional pattern pack is enabled, record each scene's `scene_type` (e.g. 劇情場 / 戰鬥前場 / 戰鬥場 / 戰鬥後場 / UI語音場) and any `auto_dialogue:false` flag as inline text notes on the `06_a` scene row — the same mechanism as the existing `risk_type` note. This adds no frontmatter field, enum, entity, or parser behavior, and stays inside the `05_b` + `06_a` write boundary. A 戰鬥場 marked `auto_dialogue:false` should not be auto-routed to `/dialogue-write` (the downstream `/scene-task` wiring is a later batch).

If a local Instance has adopted per-scene scene-index files, do not switch file organization during this skill. Follow the existing local `06_scene_index` convention unless the user gives an explicit migration instruction outside B.7.

#### Frontmatter Rules

When creating or repairing target frontmatter, preserve the Chinese five-field header and apply protocol-aligned YAML blocks:

```yaml
---
entities: [CH-01, CH-02]
depends_on: [P]
weight:
  CH-01: 0.3
  CH-02: 0.3
---
```

Target-specific rules:

- `05_b`: `entities` lists all concrete `CH-<nn>` entities; `depends_on: [P]`; `weight` gives each chapter `0.3`.
- `06_a`: `entities` lists concrete `S-<ch>-<n>` scene IDs; `depends_on` includes `P` and concrete `CH-<nn>`; `weight` gives each scene `0.2`.

Scene-index entities receive only 20% completion from this skill. Formal scene task packs and dialogue flows complete the rest.

#### Missing, Inference, and Conflict Markers

Use these markers exactly when needed:

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

Rules:

- Missing any `REQUIRED` issue blocks Stage 4.
- Skipped `STRONGLY_PREFERRED` content may proceed only with TODO markers and phase_log issue-completion records.
- If issue 4 is skipped, mark missing foreshadowing/payoff baselines in the Stage 3 preview and relevant `05_b` / `06_a` TODO notes instead of inventing them.
- If issue 6 is skipped, mark the missing high-risk handling baseline in the Stage 5 report. D-050 blocks writing `00_b §6` either way.
- Do not turn inferred chapter, character-arc, reveal, or risk material into confirmed canon without user confirmation.

### Stage 5 - Validation

After Stage 4 writes succeed, automatically invoke `/status`.

Show:

1. Files created or updated by this skill.
2. Concrete `CH-<nn>` and `S-<ch>-<n>` entities created.
3. Current completion level for each created chapter and scene entity.
4. Whether `.protocol_version.phase_log` contains `phase: create-detailed-outline`, `skill: /create-detailed-outline`, `status: completed`, and concrete `created_entities`.
5. Whether `05_b` and `06_a` were updated according to the approved split plan, and confirmation that `05_c`, `05_d`, `05_e`, and `00_protocol/` were not modified.
6. Remaining TODO / INFERENCE / CONFLICT markers.
7. Next suggested action: human B.8 Phase B REVIEW gate, then later `/scene-task <S-ID>` when the relevant Phase C skill is implemented.

Do not automatically invoke `/scene-task`, `/dialogue-write`, `/qa`, `/iterate-character`, `/create-relationship`, or the B.8 review gate.

## pattern pack 載入（可選 mode，D-067）

This skill may load an optional, read-only genre pattern pack to support genre-specific scene structure. It never writes or modifies the registry.

- **Source / fallback / activation:** same as `/create-outline` — load `<instance_root>/pattern_pack_registry.yaml`, else fall back to `_design/registries/pattern_pack_registry.template.yaml` with `WARN`, else skip and run the normal flow. Activation is opt-in: `00_b §1` is only a hint; the user enables a pack in the instance registry or confirms in Stage 1. No enabled/matching pack → normal flow (non-game works unaffected).
- **Consumption (F18):** when an enabled pack carries `scene_types`, use its `enum` to extend scene-type options in Stage 2 issue 5 (high-risk scene identification), and use `per_unit_structure` to suggest a per-unit layout (e.g. 每關 = 戰鬥前場 + 戰鬥場 + 戰鬥後場). In Stage 4, record the chosen scene type and any `dialogue_routing.auto_dialogue_false` flag as inline text notes on the `06_a` scene row (the same mechanism as the existing `risk_type` note) — never as a new frontmatter field, enum, entity, or parser behavior.
- **戰鬥場 routing:** a 戰鬥場 / UI語音場 row carries an `auto_dialogue:false` note meaning it should not automatically go to `/dialogue-write`. The real consumer of this routing is downstream `/scene-task`; this skill only records the note + semantics and does not change downstream skills (downstream wiring is a later batch — not claimed closed here).
- **File organization unchanged:** loading a pack and splitting a unit into 戰鬥前/戰鬥/戰鬥後場 still follows the existing `06_a` aggregate / per-scene (D-054 hybrid) convention; do not switch file organization. Write boundary stays `05_b` + `06_a` only. See `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.4.2 §10.5.

## 議題清單動態載入

This skill must use D-047 dynamic issue construction. Do not hardcode the final Stage 2 issue list as the live list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` once before Stage 2.

- If the Instance registry is missing, load `_design/registries/issue_type_registry.template.yaml` once as fallback and print `WARN`.
- If both are missing or unreadable, stop before Stage 2.
- If the user edits the registry during the session, tell them to restart `/create-detailed-outline`.
- Do not create or modify `issue_type_registry.yaml` from this skill; registry editing is the user's responsibility.

### Skill Key

Use only the `00_h_detailed_outline` skill key.

Expected sections:

- `core.00_h_detailed_outline`
- `user_extensions.00_h_detailed_outline`
- `core_overrides.00_h_detailed_outline`

### Dynamic Issue List Algorithm

Build Stage 2 issue list as:

```text
core + user_extensions - core_overrides
```

Execution details:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_h_detailed_outline[*].skip_id`.
3. Ignore and warn for locked core overrides.
4. Remove unlocked skipped core issues.
5. Warn and ignore a `skip_id` that does not match any core issue.
6. Sort `user_extensions.00_h_detailed_outline` by ascending `id` and append after core.
7. Use `question_summary` only as opener.
8. For core issues, use `protocol_ref` to fetch the complete script from UD §1.4.2.
9. For user extensions, ask from `question_summary`, record the answer, and do not invent write authority unless the user confirms how it maps into Stage 4.

### Required Level Behavior

- `REQUIRED`: user must answer before Stage 4; missing required content blocks writing.
- `STRONGLY_PREFERRED`: user may skip; record the gap in phase_log and mark TODO in the relevant file or preview.
- `OPTIONAL`: user may skip without phase_log gap detail.

Reject before Stage 2 if YAML parsing fails, the `00_h_detailed_outline` key is missing, a user extension id is below 100, ids collide, `required_level` is invalid, `locked` is not boolean, any required issue field is missing, or any skill key is outside the legal five-key set.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed.

Use concrete entity IDs only. Do not write wildcard IDs such as `CH-*` or `S-*`.

```yaml
- phase: create-detailed-outline
  date: <ISO date>
  skill: /create-detailed-outline
  status: completed
  created_entities:
    - CH-01
    - CH-02
    - S-01-01
    - S-01-02
  entities_touched:
    - P
    - CH-01
    - CH-02
    - S-01-01
    - S-01-02
  prereq_waived: <true|false>
  issue_completions:
    "<issue id>": <answered|skipped|required_blocked>
```

If aborted, set `status: aborted`, include `abort_reason` and `detail`, and do not count partially written entities as successfully created unless the rollback report explicitly says they remain.

## 輸入

The user provides:

- `/create-detailed-outline` with no direct parameters.
- Long-form detailed-outline material.
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

### B.7 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `05_plot/05_b_章節結構模板.md` | 補完章節結構與節奏；產生 `CH-<nn>` 貢獻 |
| 合法寫檔 | `06_scene_index/06_a_場景索引模板.md` | 場景索引與 `risk_type`；產生 `S-<ch>-<n>` 貢獻 |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: create-detailed-outline` / `created_entities` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/05_a_主線大綱模板.md`, `05_plot/05_c_角色弧線表.md`, `05_plot/05_d_資訊揭露表.md`, `05_plot/05_e_伏筆與回收表.md`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/`, `_tools/frontend/`, `scripts/`, `_design/registries/` | 任何寫入都屬 D-050 越界 |

## 邊界

The skill must not:

- modify LOCKED files without explicit file-by-file confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file, including `00_b`
- modify `scripts/`, `_tools/frontend/`, registry Template files, `_design/*.md`, or existing skill files
- modify existing Phase A skills, Wave 7 skills, or wrappers
- create vocabulary, character, relationship, main-plot, detailed `05_c` / `05_d` / `05_e`, scene task, dialogue, or QA report content
- create new chapter counts or new main-plot turns that were not confirmed by the user
- mark a scene as high-risk without user confirmation
- auto-trigger downstream skills or human REVIEW gates
- promote `P`, `CH-*`, or `S-*` status to `REVIEW`, `FINAL`, or `LOCKED`
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing completed detailed outline in `/create-detailed-outline`
- treat inference, examples, or skipped answers as confirmed canon
- write real project-specific `.protocol_version` values inside this `SKILL.md`
- write or modify `05_plot/05_f_*_原始細節備忘.md` or `05_plot/05_g_*_個人線結構備忘.md`; these are user-maintained DRAFT data sources and this skill is strictly read-only to them (D-069 / D-068)
- consume, expand, or write out a character's personal-line climax (including adult-content segments) in the detailed-outline flow; it may only mark "the main plot uses this character function here". A personal-line climax segment contributes 0 to chapter completion here (convention only; no weight/parser change) (D-068, F19)

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為 `05_b_章節結構模板.md` + `06_a_場景索引模板.md` 兩檔（CH 行）；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 流程 Stage 4」段

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

For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, enum keys, raw YAML objects, or internal parser data in user-facing errors.
