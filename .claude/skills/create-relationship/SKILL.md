---
name: create-relationship
description: "建立關係 R-<a>-<b> 的 Phase B skill。依 00_l 關係創建協議 v0.3 跑 5 階段，兩端至少 REVIEW（容許一端為 ORG-*：C↔C 或 C↔ORG，至多一端 ORG；D-074），動態讀 issue_type_registry.yaml 的 00_l_relationship 議題清單，寫入 04_a/04_b 與聲線卡關係段（ORG 端無聲線卡、跳過）。寫檔嚴格依 D-050 子裁決 2 限定 04_relationships/ + 03_characters/<name>/ 聲線卡段；嚴禁寫 00_protocol/ 任何段（D-053 /create-world exception 不擴及本 skill）。"
---

狀態：DRAFT
版本：v0.4（F8 Phase 3 / D-074 — 容許 C↔ORG endpoint：一端可為 ORG-*（至多一端；不允許 ORG↔ORG）；ORG 端無聲線卡 → 不寫 ORG 端聲線卡關係段；對齊 00_l v0.3 §2.2。既有 C↔C 行為不變）
歷史紀錄：v0.3（8th master patch round 2 R8-MI-05 — D-050 子裁決 1 block 例外列表補 D-053 /create-world 寫 00_b §1/§2 exception；對齊 DECISIONS_LOG v1.9 §6.16.2）
最後更新：2026-06-03
適用範圍：/create-relationship skill runtime instructions
優先級：高

# /create-relationship Skill

## 用途

Use this skill when the user triggers `/create-relationship <a> <b>` to create one relationship entity `R-<a>-<b>` between two already reviewed endpoints. **An endpoint may be a character `C-*` or an organization `ORG-*`** (F8 Phase 3 / D-074): the legal endpoint shapes are `C↔C` (既有) and `C↔ORG` (one end `C-*`, one end `ORG-*`; e.g. `C-瑟琳 ↔ ORG-清道夫`). **ORG↔ORG is not allowed** (至多一端 ORG).

This skill captures relationship type, power balance, address rules, emotional debt, unsaid topics, and timeline anchors. It writes relationship baselines for later scene-task, dialogue, and QA flows. It does not create characters, organizations, voice cards, plot, scenes, or dialogue.

> **C↔ORG endpoint（D-074；對齊 00_l v0.3 §2.2）：** ORG-* 永無聲線卡。當一端為 ORG-* 時，**只寫 C 端聲線卡的關係段，ORG 端不寫聲線卡**（ORG 無聲線卡可寫）；`04_a` / `04_b` 照舊寫。6 議題照跑但以「角色對組織」視角理解（組織不回話、不虛構 ORG 台詞）。

Runtime outputs may include:

- `04_relationships/04_a_角色關係矩陣.md`
- `04_relationships/04_b_關係變化時間線.md`
- `03_characters/<a>_聲線卡.md` relationship section merge only
- `03_characters/<b>_聲線卡.md` relationship section merge only
- `.protocol_version.phase_log`

## 觸發語

- English trigger: `/create-relationship <a> <b>`
- Chinese alias wrapper: `/建立關係 <a> <b>`, via `.claude/skills/建立關係/SKILL.md`

The user must name exactly one pair. If the user wants multiple pairs, split them into separate `/create-relationship` runs.

## 觸發協議

Primary authority:

- `00_protocol/00_l_關係創建協議.md` v0.3, all five stages and sections 1-12 (含 §2.2 C↔ORG endpoint 規則)

Required references:

- `_design/TASKS.md` §B.5b and B.5.5 dependency
- `_design/ARCHITECTURE.md` §3.2, §3.3, §3.3.0, §3.3.1, §3.3.2
- `_design/SPEC.md` §5.1, §5.3, §5.4, §16
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.5 and §1.5.2 full question scripts
- `_design/DECISIONS_LOG.md` §6.9.2 D-047, §6.11.2 D-049, §6.12.2 D-050, and §6.25 D-074（C↔ORG endpoint）
- `_design/registries/issue_type_registry.template.yaml`

If chat instructions conflict with the files above, follow the files above. For write boundaries, D-050 supersedes any broader write set described by `00_l` v0.3.

## 啟動前檢查

Before Stage 1, verify all of the following.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `03_characters/`, `04_relationships/`, and `05_plot/`.
2. **D-049 first defense:** no `.template_root` marker file exists at repo root.
3. **D-049 second defense:** it is not true that `_design/registries/*.template.yaml` exists while `.protocol_version` is absent.
4. `.protocol_version` exists.
5. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
6. `_design/expected_entities.yaml` exists.
7. `_design/registries/issue_type_registry.template.yaml` exists and is readable.

### Protocol-specific prerequisites

1. The command includes exactly two explicit endpoint names (each a `C-*` character or an `ORG-*` organization).
2. Convert the pair to relationship ID `R-<a>-<b>` using lexicographic order of the bare endpoint names (drop the `C-` / `ORG-` prefix for the ID; track the full endpoint IDs in frontmatter).
3. Both endpoints exist and are at least `REVIEW`, **and at most one endpoint is `ORG-*`** (C↔C or C↔ORG; reject ORG↔ORG with `⏸ 條件未滿足`, citing 00_l v0.3 §2.2 / DECISIONS_LOG §6.25.2 item 6).
4. B.5.5 REVIEW gate has passed for the involved character endpoint(s). Evidence may be frontmatter status plus the project review log if present. An `ORG-*` endpoint is gated on its ORG card being at least `REVIEW`.
5. No existing frontmatter already claims the same `R-<a>-<b>`.
6. Target files are not `LOCKED`.
7. No active or in-progress phase_log entry is currently writing the same relationship.

If the same relationship already exists, stop before Stage 1 and tell the user to use `/iterate-relationship`. Do not overwrite an existing `R-<a>-<b>` in `/create-relationship`.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user.

### Stage 1 - Diagnosis

Start with this prompt (C↔C):

```md
我們要建立 `<C-a>` 與 `<C-b>` 的關係。請先貼出你對這兩人之間關係的長段想法；可以包含他們怎麼相遇、現在的狀態、為什麼會這樣、有沒有秘密、關係未來會怎麼變。可以從任一視角寫。
```

**C↔ORG endpoint 變體（對齊 00_l v0.3 §2.1；當一端為 `ORG-*` 時改用）：**

```md
我們要建立角色 `<C-a>` 與組織 `<ORG-b>` 的關係。請貼出你對這個角色與這個組織之間關係的長段想法；可以包含對抗 / 從屬 / 受其影響的形式、現在的狀態、未來在主線怎麼推進。
```

When one endpoint is `ORG-*`, frame all Stage 2 issues as **character-toward-organization** (the organization does not speak back; never fabricate ORG dialogue or voice). Do not ask人格化 questions of the ORG end.

After the user responds, produce a chat-only diagnostic report using `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode.

Diagnose at least:

- surface relationship vs true relationship
- power balance across information, force, status, and emotional leverage
- whether both perspectives are represented
- existing address rules, taboos, and unsaid material
- timeline clarity and whether chapter anchors are available

End Stage 1 by previewing that Stage 2 will dynamically load the `00_l_relationship` issue list. If `05_plot/05_b_章節結構模板.md` has no valid chapter skeleton yet, warn that timeline-anchor issue 6 may be skipped and later completed through `/iterate-relationship`.

### Stage 2 - Exploration

At the start of Stage 2, load and print the dynamic issue list from `00_l_relationship`.

Ask at most three questions at a time. Each question must include why it matters and which file or section the answer may affect. Allow `跳這題`, `先跳到議題 X`, and `中止`.

Core issue script mapping:

| id | issue | full script authority |
|---|---|---|
| 1 | 關係類型分類 | UD §1.5.2 §10.1 |
| 2 | 權力差 | UD §1.5.2 §10.2 |
| 3 | 稱呼系統 | UD §1.5.2 §10.3 |
| 4 | 情緒債 | UD §1.5.2 §10.4 |
| 5 | 不能說出口的事 | UD §1.5.2 §10.5 |
| 6 | 關係時間線錨點 | UD §1.5.2 §10.6 |

Do not ask about split rules as a user-facing issue. Split rules are Stage 4 mechanics and appear only in the Stage 3 preview.

### Stage 3 - Convergence

Create a chat-only relationship convergence preview and wait for explicit user confirmation.

The preview must include:

1. The sorted relationship ID `R-<a>-<b>`.
2. The relationship one-sentence statement for user approval.
3. `04_a` write preview for the relationship section.
4. `04_b` write preview for timeline anchors, or a TODO reason if skipped.
5. `<a>` voice-card `關係` section merge preview, limited to the relationship with `<b>`.
6. `<b>` voice-card `關係` section merge preview, limited to the relationship with `<a>`.
7. Stage 4 split plan with target files and write modes.
8. `TODO`, `INFERENCE`, and `CONFLICT` lists.
9. Skipped `STRONGLY_PREFERRED` issues and downstream impact.

Allowed user replies:

- `通過`, `OK`, or `寫檔`: proceed to Stage 4.
- requested changes: revise and reprint the convergence preview.
- `中止` or `取消`: stop without writing, or rollback if Stage 4 has already started.

If any unresolved `CONFLICT` remains, do not enter Stage 4.

### Stage 4 - Execution

Before writing, re-check target file headers and lock status. Do not overwrite `LOCKED` content.

Write in this fixed order:

1. `04_relationships/04_a_角色關係矩陣.md`
2. `04_relationships/04_b_關係變化時間線.md`, only if issue 6 timeline anchors are confirmed.
3. `03_characters/<a>_聲線卡.md` `關係` section merge for `<b>` only — **skip if endpoint `<a>` is `ORG-*`** (ORG has no voice card).
4. `03_characters/<b>_聲線卡.md` `關係` section merge for `<a>` only — **skip if endpoint `<b>` is `ORG-*`** (ORG has no voice card).

`04_a` and `04_b` are the relationship products. The voice-card writes are section-level merges on the **character endpoint(s) only**: update only the `關係` subsection for this pair, and do not rewrite voice core, biography, speech examples, compliance, drift checks, vocabulary, or any other character-card section. For a `C↔ORG` relationship exactly one voice-card merge is written (the C end); the ORG end writes no voice card.

#### Split Rules

Apply `00_l` §10.7:

| source | target | write mode |
|---|---|---|
| 10.1 關係類型 | `04_a §<R-a-b> §1` | overwrite |
| 10.2 權力差 | `04_a §<R-a-b> §2` | overwrite |
| 10.3 稱呼系統 | `04_a §<R-a-b> §3` and both voice-card `關係` subsections | overwrite and section-level merge |
| 10.4 情緒債 | `04_a §<R-a-b> §4` and `04_b §<R-a-b> §情緒債` | overwrite and append |
| 10.5 不能說出口的事 | `04_a §<R-a-b> §5`, both voice-card `關係` subsections, and `04_b §<R-a-b> §破戒錨點` | overwrite, section-level merge, and append |
| 10.6 時間線錨點 | `04_b §<R-a-b> §章節錨點`, `04_a §<R-a-b> §6 不變的部分`, and both voice-card `關係` subsections | overwrite, append, and section-level merge |

Voice-card relationship-section merge must be narrow:

- locate the existing `關係` section or create that section only if the voice card has no relationship section
- add or update only the entry for the other character and this `R-<a>-<b>`
- preserve all other sections and ordering
- never write `C-*` voice core, dialogue examples, character facts, or plot conclusions

#### Frontmatter Rules

Maintain target frontmatter according to local file patterns:

| target | entities | depends_on | weight |
|---|---|---|---|
| `04_a` | accumulated `R-*` and related `C-*` | `W-rules`, `V`, related `C-*` | `R-*` around 0.6, related `C-*` around 0.1 |
| `04_b` | accumulated `R-*-*` | `P`, `CH-*`, related `R-*-*` when available | `R-*` around 0.3 |
| `03_characters/<a>_聲線卡.md` relationship section | preserve existing `C-<a>` and add this `R-<a>-<b>` only if the local schema tracks relationship entities in voice cards | preserve existing dependencies unless local schema requires the new relationship | preserve local pattern |
| `03_characters/<b>_聲線卡.md` relationship section | preserve existing `C-<b>` and add this `R-<a>-<b>` only if the local schema tracks relationship entities in voice cards | preserve existing dependencies unless local schema requires the new relationship | preserve local pattern |

TASKS shorthand lists `depends_on: [C-<a>, C-<b>, W-rules]`; apply the stricter protocol-aware dependency set when maintaining `04_a` and `04_b`.

#### Missing, Inference, and Conflict Markers

Use these markers exactly when needed:

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

Rules:

- Missing issue 1 blocks Stage 3.
- Missing issue 3 blocks Stage 4.
- Skipped issues 2, 4, or 5 may proceed only with TODO markers and downstream-impact notes.
- Missing issue 6 skips `04_b`; suggest `/iterate-relationship` after chapter structure exists if needed.
- Missing target voice-card `關係` section may create that section only; it must not rewrite other voice-card sections.
- Do not fill unsaid motives or future events from inference.

### Stage 5 - Validation

After Stage 4 writes succeed, automatically invoke `/status`.

Show:

1. Files created or updated by this skill.
2. Concrete `R-<a>-<b>` entity created.
3. Current completion level for `R-<a>-<b>`.
4. Expected completion impact for `C-<a>` and `C-<b>`.
5. Whether `.protocol_version.phase_log` contains `phase: create-relationship`, `skill: /create-relationship`, `status: completed`, and `created_entities: [R-<a>-<b>]`.
6. Whether each involved voice-card `關係` section received the narrow merge.
7. Remaining TODO / INFERENCE / CONFLICT markers.
8. Next suggested skill: `/create-outline` if core relationships are ready.

Do not automatically invoke `/create-outline`, `/create-detailed-outline`, or `/scene-task`.

## 議題清單動態載入

This skill must use D-047 dynamic issue construction. Do not hardcode the final Stage 2 issue list as the live list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` once before Stage 2.

- If the Instance registry is missing, load `_design/registries/issue_type_registry.template.yaml` once as fallback and print `WARN`.
- If both are missing or unreadable, stop before Stage 2.
- If the user edits the registry during the session, tell them to restart `/create-relationship`.

### Skill Key

Use only the `00_l_relationship` skill key.

Expected sections:

- `core.00_l_relationship`
- `user_extensions.00_l_relationship`
- `core_overrides.00_l_relationship`

### Dynamic Issue List Algorithm

Build Stage 2 issue list as:

```text
core + user_extensions - core_overrides
```

Execution details:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_l_relationship[*].skip_id`.
3. Ignore and warn for locked core overrides.
4. Remove unlocked skipped core issues.
5. Sort `user_extensions.00_l_relationship` by ascending `id` and append after core.
6. Use `question_summary` only as opener.
7. For core issues, use `protocol_ref` to fetch the complete script from UD §1.5.2.
8. For user extensions, ask from `question_summary`, record the answer, and do not invent write authority unless the user confirms how it maps into Stage 4.

### Required Level Behavior

- `REQUIRED`: user must answer before Stage 4.
- `STRONGLY_PREFERRED`: user may skip; record the gap in phase_log and mark TODO in the relevant file or preview.
- `OPTIONAL`: user may skip without phase_log gap detail.

Reject before Stage 2 if YAML parsing fails, the `00_l_relationship` key is missing, a user extension id is below 100, ids collide, `required_level` is invalid, `locked` is not boolean, or any required issue field is missing.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed.

Use concrete entity IDs only. Do not write wildcard IDs such as `R-*`.

```yaml
- phase: create-relationship
  date: <ISO date>
  skill: /create-relationship
  status: completed
  created_entities:
    - R-<a>-<b>
  entities_touched:
    - R-<a>-<b>
    - C-<a>
    - C-<b>
  issue_completions:
    "<issue id>": <answered|skipped|required_blocked>
```

If aborted, set `status: aborted`, include `abort_reason`, and do not count the relationship as created.

## 輸入

The user provides:

- `/create-relationship <a> <b>` with exactly two explicit names.
- Long-form relationship material.
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
| 合法寫檔 | `04_relationships/04_a_角色關係矩陣.md` | matrix row / section append for `R-<a>-<b>` |
| 合法寫檔 | `04_relationships/04_b_關係變化時間線.md` | timeline only if issue 6 triggers |
| 合法寫檔 | `03_characters/<a>_聲線卡.md` | `關係` section-level merge only；**ORG-* 端跳過**（ORG 無聲線卡）；no other section |
| 合法寫檔 | `03_characters/<b>_聲線卡.md` | `關係` section-level merge only；**ORG-* 端跳過**（ORG 無聲線卡）；no other section |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: create-relationship` / `created_entities` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/` | 任何寫入都屬 D-050 越界 |
| 不寫 | `03_characters/<x>_聲線卡.md` 的其他段 | 不改聲線核心、角色事實、範例台詞、合規、偏移或其他非關係段 |

Relationship taboo, forbidden-address, or plot-state notes may appear in Stage 3 preview or Stage 5 next-step advice only. They do not authorize writes to `02_vocabulary/` or `05_plot/`.

## 邊界

The skill must not:

- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify `00_protocol/` files
- modify `scripts/`, `_tools/frontend/`, or registry Template files
- modify existing Phase A skills or wrappers
- create characters or decide missing character facts
- rewrite `C-*` voice-card core content; the `關係` section merge is the only legal voice-card edit
- design complete plot, chapters, scenes, task packs, or dialogue
- auto-trigger downstream skills
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing same-pair relationship in `/create-relationship`
- write concrete future events beyond confirmed relationship timeline anchors
- write real project-specific `.protocol_version` values inside this `SKILL.md`

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

