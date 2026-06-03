---
name: create-character
description: "建立角色 C-<name> 的 Phase B skill。依 00_f 角色創建協議 v0.2 跑 5 階段，動態讀 issue_type_registry.yaml 的 00_f_character 議題清單，建立角色聲線卡、偏移檢查、合規檢查，並更新 .protocol_version.phase_log。寫檔嚴格依 D-050 子裁決 2 限定 03_characters/ 目錄；嚴禁寫 00_protocol/ 任何段（D-053 /create-world exception 不擴及本 skill）。"
---

狀態：DRAFT
版本：v0.6（F8 Phase 3 — Stage 1.0 gate 第 3 選項由「/create-org 待 Phase 3」改指 live `/create-org`（D-074；依 00_n 跑、寫 11_organizations/、無聲線卡）；gate 拒絕行為 + D-050 邊界不動；本檔 v0.5 → v0.6）
歷史紀錄：v0.5（F8 Phase 2 — Stage 1.0 gate 第 3 選項改指 live ORG-* 型別（D-071；手動 author 11_organizations/ 或 /integrate；/create-org 待 Phase 3）+ 修 2 處 stale ref（line 92 D-064 待補 → §6.19.3；line 147 D-063 待補 → §6.19.2）；本檔 v0.4 → v0.5）
歷史紀錄：v0.4（Round 11 R11-CRITICAL-01 修補 — 還原 §錯誤呈現規則 line 371 之後因 sandbox cache stale + bash python write 截斷的尾段 wording（What/Where/Why/下一步 4 欄 + 多錯誤彙整指引）；對齊既有 create-relationship/create-outline v0.3 標準 wording）
最後更新：2026-06-02
適用範圍：/create-character skill runtime instructions
優先級：高

# /create-character Skill

## 用途

Use this skill when the user triggers `/create-character <name>` to create one or more `C-<name>` character entities in an already bootstrapped Instance repo.

This skill creates the character baseline needed by later relationship, outline, scene-task, dialogue, and QA flows. It produces character voice cards with voice drift checks and compliance checks. It does not create relationship content, plot, chapters, scenes, task packs, QA reports, vocabulary tables, or dialogue.

Runtime outputs may include:

- `03_characters/main/<name>_聲線卡.md`
- `03_characters/minor/<name>_聲線卡.md`
- `03_characters/npc/<NPC類型>模板.md`
- `.protocol_version.phase_log`

## 觸發語

- English trigger: `/create-character <name>`
- Chinese alias wrapper: `/建立角色 <name>`, via `.claude/skills/建立角色/SKILL.md`
- The user may name multiple characters in one command, but each created entity must be recorded as a concrete `C-<name>` item.

The command argument is only the target character name list. It does not replace the five-stage conversation.

## 觸發協議

Primary authority:

- `00_protocol/00_f_角色創建協議.md` v0.2, all five stages and sections 1-12

Required references:

- `_design/TASKS.md` §B.5
- `_design/ARCHITECTURE.md` §3.2, §3.3, §3.3.0, §3.3.1, §3.3.2
- `_design/SPEC.md` §5.1, §5.3, §5.4, §16
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.2 and §1.2.2 full question scripts
- `_design/DECISIONS_LOG.md` §6.9.2 D-047, §6.11.2 D-049, and §6.12.2 D-050
- `_design/registries/issue_type_registry.template.yaml`

If chat instructions conflict with the files above, follow the files above. For write boundaries, D-050 supersedes any broader write set described by `00_f` v0.2. If the target file is `LOCKED`, stop and ask for explicit confirmation before any write attempt.

## 啟動前檢查

Before Stage 1, verify all of the following.

### Instance and Template-detect checks

1. Current folder is an Instance repo root and contains `00_protocol/`, `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, and `09_quality_assurance/`.
2. **D-049 first defense:** no `.template_root` marker file exists at repo root.
3. **D-049 second defense:** it is not true that `_design/registries/*.template.yaml` exists while `.protocol_version` is absent.
4. `.protocol_version` exists.
5. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
6. `_design/expected_entities.yaml` exists.
7. `_design/registries/issue_type_registry.template.yaml` exists and is readable.

If `.template_root` is present, stop with `⏸ 條件未滿足` and tell the user this directory is still marked as the Template repo. If `.protocol_version` is absent while registry templates are present, stop with `⏸ 條件未滿足` and tell the user to run `/init-project` only in a real Instance after the Template marker decision is resolved.

### Protocol-specific prerequisites

1. `W-rules`, `V`, and `W-language` each exist and are at least `REVIEW`.
2. The command includes at least one explicit character name.
3. For every target `C-<name>`, no existing frontmatter already claims that same entity.
4. Target voice-card files are not `LOCKED`.
5. No active or in-progress phase_log entry is currently writing the same `C-<name>`.

If the target entity already exists, stop before Stage 1 and tell the user to use `/iterate-character` or provide an explicit conflict-resolution decision. Do not overwrite an existing same-name entity in `/create-character`.

## 流程

Run exactly five stages. Do not write files before Stage 3 is explicitly approved by the user.

### Stage 1 - Diagnosis

Start with this prompt:

```md
我們要建立 `<角色名清單>`。請貼出你對這 `<N>` 個角色的長段想法，包含身份、年齡、職業、外觀、語言習慣、人格、創傷、目標、與其他角色的關係。關係內容此輪只會記為提及，不建立關係。可以全部貼一起，也可以一個一個來。
```

#### Stage 1.0 - 目標可說話性檢查（non-character refusal gate）

After the user responds and before producing the diagnostic report, run this gate for every target name. This is a content-level semantic judgement on the user description; it is separate from the structural prerequisites in `## 啟動前檢查` and must not be merged into them. This gate lives only in this SKILL.md as a 短期措施 (F8 non-character gate；SKILL-only，對應 D-064 / DECISIONS_LOG §6.19.3；其正向落點 ORG-* 實體型別已於 D-071 落地，見下方選項 3); it does not modify `00_protocol/00_f_角色創建協議.md`.

For each target, judge whether it is a speaking subject that can carry character voice. Treat a target as a 非角色目標 (non-character target) when the user description shows any of the following:

- a bankrupt, liquidated, or dissolved organization or company that only leaves documents or remains and does not actively speak
- an institution, statute, system, or mechanism that is an abstract rule-like existence
- a pure background faction with no concrete speaking representative
- a place, object, or event itself that is not personified

Detection signals (any one triggers a confirmation question; never refuse arbitrarily):

- the description contains 公司 / 組織 / 勢力 / 制度 / 體系 / 機構 and does not name a specific speaking representative
- the description contains 已破產 / 已清算 / 已解散 / 只剩文件 / 不會說話 / 沒有人格
- the target name is itself an organization name rather than a person name, and the user has not stated a personified speaking voice

Handling (three steps):

1. Do not refuse arbitrarily. When a signal is detected, first ask one confirmation:

```md
`<target>` 看起來是組織/制度而非會說話的角色。請確認：
(a) 它有一個會說話的代表人物（請給人名，我改建那個人為 C-*）
(b) 它本身不會說話，只是對抗來源/背景設定
```

2. If the user picks (b) or confirms it is a non-character, refuse to create `C-<target>` and output the standard refusal plus three alternatives:

```md
⏸ 條件未滿足：`<target>` 不是會說話的角色，/create-character 不建立 C-<target>。

建議改用：
1. 若它與某會說話角色有對抗/從屬關係 → 用 `/create-relationship <會說話角色> <該角色相關方>`，
   把該組織的影響寫進關係，或在 01_a §9「勢力與組織」記為 W-rules 子段。
2. 若它有可發聲的代言人 → 改 `/create-character <代言人名>`，把組織背景寫進該角色 source。
3. 若它是需要獨立追蹤的「組織/勢力」對抗源 → 建 `ORG-<name>` 實體（D-071 已新增 ORG-* core 型別）：
   用 `/create-org <name>` 引導建立（F8 Phase 3 / D-074 已落地；依 00_n 組織創建協議跑 5 階段、寫 `11_organizations/<name>.md`、無聲線卡）；
   亦可手動 author 至 `11_organizations/<name>.md`（frontmatter `entities: [ORG-<name>]`）或整理素材走 `/integrate`。
```

3. If the user picks (a) and supplies a representative person name, replace the target with that person name and continue into the diagnostic report normally.

After the user responds, produce a chat-only diagnostic report using `00_protocol/00_a_台詞生產協議.md` §3.3 diagnostic mode.

For each character, diagnose at least:

- identity register, faction, education, and likely vocabulary source
- initial voice contour: sentence length, attack/defense tendency, emotional masking
- W-rules compliance
- V compliance
- W-language and faction-language fit
- boundary reminders for material that belongs to relationship, outline, scene, or dialogue flows

#### 既有素材查找路徑（F7 / D-063=A）

When the user references existing source material (人設稿 / 既有劇本 / 設定文件) for a target, the default lookup root is the repo-root directory `_source_materials/` (D-063 方案 A：全域單一素材根，下分 `characters/ world/ outline/ dialogue/`；D-063 已記 DECISIONS_LOG §6.19.2). This directory is read-only for this skill: source material may be read for context but is never written by `/create-character` (D-050 子裁決 2 限定寫檔於 `03_characters/`；讀取不擴大寫檔範圍).

Rules:

- Default discovery root is `<instance_root>/_source_materials/`; the user may also paste a path or content directly.
- `_source_materials/` 為 user 原始素材區，可讀不可寫；本 skill 永不寫該目錄。
- 既有劇本台詞 source 的合法讀取根包含 `<instance_root>/_source_materials/dialogue/` 與既有 `08_dialogue_outputs/`；兩者皆「可讀不可寫」（讀取不擴大寫檔範圍，寫檔仍嚴格限 `03_characters/`；D-063 source 慣例 + D-065 D-050 讀邊界 clarification）。
- **Speaker alias matching**：source 內角色別名（例：MainGirlA / 代號 / 暱稱）須先與目標 `C-<name>` 建立對照，再擷取該角色台詞；對照不明時於 Stage 1 向 user 確認，不臆測歸屬。
- If a referenced `.docx` cannot be parsed in the current runtime, print `WARN：docx 無法自動解析，請改貼純文字或用副對話轉述` and continue. Never silently skip an unreadable source file.
- 既有劇本台詞萃取進聲線卡 `§B 既有劇本台詞聲線基準` / `§C 既有劇本聲線使用規則` 屬本批 F11+F13（D-065）落地範圍：input 讀取掛在 Stage 1/2，output 骨架見 `## 輸出 → §聲線卡固定段骨架（§A / §B / §C / §D）`，Stage 3 預覽、Stage 4 寫入。

#### 合法讀取來源表（read-only；與 D-050 寫檔目錄表並列）

下表列出本 skill 允許**讀取**的來源；讀取不擴大寫檔範圍，寫檔仍嚴格限 `## 輸出 → D-050 寫檔目錄表`。

| 類別 | 路徑 / 來源 | 讀寫 | 用途 |
|---|---|---|---|
| 合法讀取 | `<instance_root>/_source_materials/`（含 `characters/ world/ outline/ dialogue/`）| 可讀不可寫 | user 原始素材：人設稿 / 既有劇本 / 設定文件（D-063 方案 A）|
| 合法讀取 | `08_dialogue_outputs/` | 可讀不可寫 | 既有已產出台詞，作 §B 聲線基準對齊（D-065 讀邊界 clarification；維持 D-050 子裁決 2「不寫」）|
| 合法讀取 | user 直接貼的路徑 / 內容 | 可讀不可寫 | docx 無法解析時改貼純文字 |

> docx 無法解析時印 `WARN：docx 無法自動解析，請改貼純文字或用副對話轉述`，不靜默跳過。

End Stage 1 by previewing that Stage 2 will dynamically load the `00_f_character` issue list. If more than one character is in scope, ask the user to choose depth-first or breadth-first exploration. For more than three characters, explain that breadth-first makes voice comparison easier.

### Stage 2 - Exploration

At the start of Stage 2, load and print the dynamic issue list from `00_f_character`.

Ask at most three questions at a time. Each question must include why it matters and which file or section the answer may affect. Allow `跳這題`, `先跳到議題 X`, and `中止`.

Core issue script mapping:

| id | issue | full script authority |
|---|---|---|
| 1 | 角色類型分類 | UD §1.2.2 §10.1 |
| 2 | 聲線測試題 | UD §1.2.2 §10.2 |
| 3 | 去名測試前置 | UD §1.2.2 §10.3 |
| 4 | 與 W-rules / V / W-language 合規性檢查 | UD §1.2.2 §10.4 |
| 5 | 髒話來源欄位 | UD §1.2.2 §10.5 |
| 6 | 偏移檢查欄位 | UD §1.2.2 §10.6 |
| 7 | 聲線污染檢查 | UD §1.2.2 §10.7 |
| 8 | 與類型氣質合規檢查 | UD §1.2.2 §10.8 |
| 9 | 既有劇本台詞聲線基準萃取 | UD §1.2.2 §10.13 |
| 10 | 既有劇本聲線使用規則 | UD §1.2.2 §10.14 |

When an issue answer benefits from existing source material, read it from the legal read sources defined in Stage 1 `#### 合法讀取來源表`: `<instance_root>/_source_materials/`（含 `dialogue/`）and existing `08_dialogue_outputs/` (read-only; docx 無法解析時印 WARN，不靜默跳過; speaker alias 須先對照再擷取). Reading source never authorizes a write outside `03_characters/`.

Do not ask about split rules as a user-facing issue. Split rules are Stage 4 mechanics and appear only in the Stage 3 preview.

### Stage 3 - Convergence

Create a chat-only character convergence preview and wait for explicit user confirmation.

The preview must include:

1. Target character list and concrete entity IDs.
2. Character level, function, and expected file path for each character.
3. One voice-card draft per character.
4. Cross-character no-name test result when multiple characters are in the same run.
5. W-rules / V / W-language compliance findings.
6. Voice-card drift baseline preview for each character. This must also include the `§A 個性拆解` 10-subsection breakdown that Stage 4 will write into the voice card, so the user can confirm or correct each subsection before it is written.
6b. 既有劇本聲線預覽（僅當該角色有既有劇本 source 時）: preview the `§B 既有劇本台詞聲線基準`（speaker alias 對照 + 8-12 句覆蓋 8 場景類型 + 萃取出的聲線規律）與 `§C 既有劇本聲線使用規則`（可直接複用 / 需調整 / 不可直接當台詞）that Stage 4 will write into the voice card, so the user can confirm before write. 若無既有劇本 source，於預覽標註「無既有劇本 source，§B/§C 留 TODO」。Section order in preview and on-card must stay `§A → §B → §C → §D`.
7. Downstream notes（將寫入聲線卡 `§D Source Coverage / 下游 Hooks`，不寫任何下游檔）: relationship / outline / scene-task / QA hooks are recorded into the voice card `§D` section in Stage 4, not written into `04_*` / `05_*` / `07_*`. The Stage 3 preview must show these notes under the heading `§D Source Coverage / 下游 Hooks` so the chat preview matches what Stage 4 actually writes.
8. Stage 4 split plan with target files and write modes.
9. `TODO`, `INFERENCE`, and `CONFLICT` lists.
10. Skipped `STRONGLY_PREFERRED` issues and expected downstream impact.

Allowed user replies:

- `通過`, `OK`, or `寫檔`: proceed to Stage 4.
- requested changes: revise and reprint the convergence preview.
- `中止` or `取消`: stop without writing, or rollback if Stage 4 has already started.

If any unresolved `CONFLICT` remains, do not enter Stage 4.

### Stage 4 - Execution

Before writing, re-check target file headers and lock status. Do not overwrite `LOCKED` content.

Write in this fixed order:

1. Character voice card in `03_characters/main/`, `03_characters/minor/`, or `03_characters/npc/`.

Use local section replacement or append only. Do not rewrite unrelated sections.

#### Split Rules

Apply `00_f` §10.9:

| source | target | write mode |
|---|---|---|
| 10.1 角色類型分類 | voice card `角色定位` | create or overwrite |
| 10.2 聲線測試題 | voice card `聲線輪廓` and `聲線範例` | overwrite |
| 10.3 去名測試 | voice card `去名測試紀錄` | append |
| 10.4 合規性檢查 | voice card `合規檢查紀錄` and voice-card allow/block notes | overwrite |
| 10.5 髒話來源 | voice card `髒話來源` | overwrite |
| 10.6 偏移檢查 | voice card `偏移檢查` | overwrite |
| 10.7 聲線污染 | voice card `聲線污染檢查` | overwrite |
| 10.8 類型氣質合規 | voice card `與類型氣質合規` | overwrite |
| 個性拆解（agent-side mechanic；無 registry 議題；agent 由議題 1-8 答案綜合，Stage 3 user 確認）| voice card `§A 個性拆解` | overwrite |
| id 9 既有劇本台詞聲線基準萃取（registry core id 9 / UD §10.13；讀 `_source_materials/dialogue/` + `08_dialogue_outputs/` 只讀；speaker alias 對照後擷取 8-12 句覆蓋 8 場景類型）| voice card `§B 既有劇本台詞聲線基準` | overwrite |
| id 10 既有劇本聲線使用規則（registry core id 10 / UD §10.14；由 §B 基準歸納可複用 / 需調整 / 不可直接當台詞）| voice card `§C 既有劇本聲線使用規則` | overwrite |
| Source coverage / 下游 hooks（agent-side mechanic；無 registry 議題；agent 由議題 1-8 答案 + source 綜合，Stage 3 user 確認）| voice card `§D Source Coverage / 下游 Hooks` | overwrite |

#### §A 個性拆解 / §B/§C 既有劇本聲線 / §D Source Coverage 寫入規則

`§A 個性拆解` and `§D Source Coverage / 下游 Hooks` are agent-side Stage-4 mechanics — they do NOT add a user-facing registry issue (consistent with the Wave-1 decision that §A/§D stay mechanics). The agent synthesizes them from the existing issue 1-8 answers (plus any read-only source material for §D), previews them in Stage 3 for the user to confirm, and writes them into the voice card in Stage 4. Both write only the target voice card under `03_characters/`.

`§B 既有劇本台詞聲線基準` maps to registry core `00_f_character` id 9 (full script UD §1.2.2 §10.13); `§C 既有劇本聲線使用規則` maps to registry core id 10 (full script UD §1.2.2 §10.14). These are the F11+F13 (NEW_REQ_35+37 / D-065 + D-066) new registry issues. The agent extracts them from the legal read sources (`_source_materials/dialogue/` + `08_dialogue_outputs/`, read-only; speaker alias matched; 8-12 句 covering 8 場景類型), previews them in Stage 3, and writes them into the voice card in Stage 4. They write only the target voice card under `03_characters/` and never write `08_dialogue_outputs/`.

`§D Source Coverage / 下游 Hooks` carries five subsections. It only registers hooks; it does not authorize this skill to write any downstream file:

1. **已吸收進聲線主體的 source 資訊**: source material already turned into other voice-card sections.
2. **交給 /create-relationship 的 hooks**: relationship leads (not written to `04_*` by this skill).
3. **交給 /create-outline / /create-detailed-outline 的 hooks**: plot / arc leads (not written to `05_*` / `06_*` by this skill).
4. **交給 /scene-task 的 hooks**: scene / task-pack leads (not written to `07_*` by this skill).
5. **不應直接當台詞使用的 source 資訊**: background / author notes; for understanding only, must not enter dialogue.

#### Frontmatter Rules

When creating a voice card, preserve the Chinese five-field header and add the YAML block:

```yaml
---
entities: [C-<name>]
depends_on: [W-rules, V, W-language]
weight:
  C-<name>: 1.0
---
```

For NPC group files, use the confirmed NPC type in `C-<type_npc>`. This skill must not touch `04_a` or `05_c` row headers; those belong to relationship and outline flows.

#### Missing, Inference, and Conflict Markers

Use these markers exactly when needed:

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

Rules:

- Missing `REQUIRED` content blocks Stage 4.
- Skipped `STRONGLY_PREFERRED` content may proceed only with TODO markers and phase_log issue-completion records.
- If issue 6 is skipped, leave the voice-card drift baseline as TODO; do not write `00_b` §5.
- Do not turn relationship mentions into `04_a` or `04_b` relationship content.

### Stage 5 - Validation

After Stage 4 writes succeed, automatically invoke `/status`.

Show:

1. Files created or updated by this skill.
2. Concrete `C-<name>` entities created, one by one.
3. Current completion level for each created character.
4. Whether `.protocol_version.phase_log` contains `phase: create-character`, `skill: /create-character`, `status: completed`, and concrete `created_entities`.
5. Remaining TODO / INFERENCE / CONFLICT markers.
6. Next suggested skill: `/create-relationship` to add relationship sections, or `/create-outline` when relationship planning is not needed yet.

Do not automatically invoke `/create-relationship` or `/create-outline`.

## 議題清單動態載入

This skill must use D-047 dynamic issue construction. Do not hardcode the final Stage 2 issue list as the live list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` once before Stage 2.

- If the Instance registry is missing, load `_design/registries/issue_type_registry.template.yaml` once as fallback and print `WARN`.
- If both are missing or unreadable, stop before Stage 2.
- If the user edits the registry during the session, tell them to restart `/create-character`.

### Skill Key

Use only the `00_f_character` skill key.

Expected sections:

- `core.00_f_character`
- `user_extensions.00_f_character`
- `core_overrides.00_f_character`

### Dynamic Issue List Algorithm

Build Stage 2 issue list as:

```text
core + user_extensions - core_overrides
```

Execution details:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_f_character[*].skip_id`.
3. Ignore and warn for locked core overrides.
4. Remove unlocked skipped core issues.
5. Sort `user_extensions.00_f_character` by ascending `id` and append after core.
6. Use `question_summary` only as opener.
7. For core issues, use `protocol_ref` to fetch the complete script from UD §1.2.2.
8. For user extensions, ask from `question_summary`, record the answer, and do not invent write authority unless the user confirms how it maps into Stage 4.

### Required Level Behavior

- `REQUIRED`: user must answer before Stage 4.
- `STRONGLY_PREFERRED`: user may skip; record the gap in phase_log and mark TODO in the relevant file or preview.
- `OPTIONAL`: user may skip without phase_log gap detail.

Reject before Stage 2 if YAML parsing fails, the `00_f_character` key is missing, a user extension id is below 100, ids collide, `required_level` is invalid, `locked` is not boolean, or any required issue field is missing.

## .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed.

Use concrete entity IDs only. Do not write wildcard IDs such as `C-*`.

```yaml
- phase: create-character
  date: <ISO date>
  skill: /create-character
  status: completed
  created_entities:
    - C-<name>
  entities_touched:
    - C-<name>
  issue_completions:
    "<issue id>": <answered|skipped|required_blocked>
```

If multiple characters are created in one run, list each `C-<name>` as its own item under `created_entities`; do not compress them into one aggregate entry. If aborted, set `status: aborted`, include `abort_reason`, and do not count the entity as created.

## 輸入

The user provides:

- `/create-character <name>` with one or more explicit names.
- Long-form character material.
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
| 合法寫檔 | `03_characters/main/<name>_聲線卡.md` | 主角色聲線卡 |
| 合法寫檔 | `03_characters/minor/<name>_聲線卡.md` | 次角色聲線卡 |
| 合法寫檔 | `03_characters/npc/<NPC類型>模板.md` | NPC 類型模板；複用模板 |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: create-character` / `created_entities` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/` | 任何寫入都屬 D-050 越界 |

Relationship mentions, vocabulary candidates, plot hooks, and QA risks may appear only in the Stage 3 preview or Stage 5 next-step advice. They do not authorize file writes outside `03_characters/`.

### 聲線卡固定段骨架（§A / §B / §C / §D）

In addition to the eight technical sections (角色定位 / 聲線輪廓 / 聲線範例 / 去名測試紀錄 / 合規檢查紀錄 / 髒話來源 / 偏移檢查 / 聲線污染檢查 / 與類型氣質合規), each voice card carries these four fixed appended sections in the order `§A → §B → §C → §D`. They use fixed anchor titles and are written in Stage 4 per the §Split Rules above; their content is previewed in Stage 3. Stage 3 preview, Stage 4 write, and this output structure must stay consistent. `§B` / `§C` are written only when the character has existing-script source; otherwise leave a TODO placeholder.

`§A 個性拆解` is placed near the front of the card (after 角色定位 conceptually; appended with a fixed anchor title in practice) and contains 10 fixed subsections:

```md
## §A 個性拆解
1. **表層個性**（聽得到的那一面）：<玩家第一耳聽到什麼>
2. **內在個性**（驅動台詞的那一面）：<真正決定他說什麼的底層>
3. **自尊來源**：<他的價值感建立在什麼上>
4. **核心恐懼**：<他最怕失去/變成什麼>
5. **情緒遮掩**：<他如何藏情緒；用什麼掩飾>
6. **魅力來源**（可愛/吸引點）：<讓人喜歡這角色的具體聲線點>
7. **努力與缺陷表現**：<他怎麼努力、缺陷怎麼在台詞露出>
8. **壓力變形**：<壓力下聲線怎麼變；與「偏移檢查 / 聲線污染」呼應，此處給總綱、細節指向對應技術段>
9. **角色差異**：<與哪些角色易混；差別在哪>（與「去名測試」「聲線污染」呼應，人物層總結不重複技術段）
10. **不可偏移人格模板**：<3-5 條「無論劇情怎麼推都不能變的人格核心」>（人格層；與聲線層的「偏移檢查」呼應）
```

`§B 既有劇本台詞聲線基準` is placed after `§A` and保存「從既有劇本台詞萃取」的角色聲線基準，供 /dialogue-write 對齊文筆（F11+F13 / D-065）。它只**讀** `08_dialogue_outputs/` + `_source_materials/dialogue/`（docx/.txt/.csv/.json），**永不寫** `08_dialogue_outputs/`：

```md
## §B 既有劇本台詞聲線基準
> 本段保存「從既有劇本台詞萃取」的角色聲線基準，供 /dialogue-write 對齊文筆。
> D-050 / D-065：本段只**讀** `08_dialogue_outputs/` + 既有劇本 source（docx/.txt/.csv/.json），**永不寫** 08。
> cross-ref STYLE_ANCHOR W-style（D-055）：voice card §B 繼承 W-style 作品級文風指紋 + 加 character-specific 聲線特徵。

1. **speaker alias 對照**：<別名 → C-<name> 對照表，例 MainGirlA=瑟琳 / MainGirlB=莉娜 / MainGirlC=諾拉>
2. **8-12 句代表台詞**（覆蓋 8 場景類型）：初登場 / 危機反應 / 任務前準備 / 戰後反應 / 日常互動 / 被肯定被吐槽 / 關係推進 / 中後期成長語氣
3. **萃取出的聲線規律**：<由代表台詞歸納，例：罵人綁定具體技術問題、不宜搶其他角色定位>
4. **與人設 source 的差異**：<只讀人設 vs 補讀劇本的聲線落差紀錄>
```

`§C 既有劇本聲線使用規則` is placed after `§B` and規範既有劇本聲線如何帶進新台詞（F11+F13 / D-065）：

```md
## §C 既有劇本聲線使用規則
1. **可直接複用的聲線特徵**：<哪些已驗證可直接帶進新台詞>
2. **需調整後使用**：<舊台詞中過時 / 偏移 / 與當前 canon 衝突者>
3. **不可直接當台詞使用的 source**：<僅供理解，不入正式台詞；與 §D 第 5 子段呼應不重複>
```

`§D Source Coverage / 下游 Hooks` is always placed at the card tail and contains 5 fixed subsections:

```md
## §D Source Coverage / 下游 Hooks
> 本段保存「source 檔中有價值但不屬本卡主體」的資訊，供下游 skill 承接。
> D-050：本段只是登錄 hooks，不授權本 skill 寫任何下游檔。

1. **已吸收進聲線主體的 source 資訊**：<已轉化進本卡各段的素材清單>
2. **交給 /create-relationship 的 hooks**：<關係相關線索（不在本 skill 寫 04）>
3. **交給 /create-outline / /create-detailed-outline 的 hooks**：<劇情/弧線線索（不在本 skill 寫 05/06）>
4. **交給 /scene-task 的 hooks**：<場景/任務包線索（不在本 skill 寫 07）>
5. **不應直接當台詞使用的 source 資訊**：<背景設定/作者筆記等，僅供理解不可入台詞>
```

## 邊界

The skill must not:

- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, or registry Template files
- modify existing Phase A skills or wrappers
- create vocabulary tables, relationship content, outline content, chapters, scenes, task packs, dialogue, or QA reports
- auto-trigger downstream skills
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing same-name entity in `/create-character`
- treat inference, examples, or skipped answers as confirmed canon
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
