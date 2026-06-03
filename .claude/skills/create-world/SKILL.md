---
name: create-world
description: "建立作品世界觀（W-rules / W-language / V 三實體 + 作品專屬 00_b §1/§2）。依 00_e_世界觀創建協議 跑 5 階段：診斷 → 探索（動態讀 issue_type_registry.yaml 構建議題清單）→ 收斂 → 執行寫檔（自動拆分到 01_a/01_b/01_c/02_a/02_b/02_c + 00_b §1/§2）→ 驗證 + 自動呼叫 /status。對齊 D-047 議題清單動態構建機制；寫 00_b §1/§2 Instance-specific 段屬 D-053 partial supersede D-050 子裁決 1 加 /create-world exception 範圍（其他 00_protocol/ 段嚴禁寫）。"
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：/create-world skill runtime instructions
優先級：高

# /create-world Skill

## 用途

Use this skill when the user triggers `/create-world` to build the first upstream world foundation for an Instance repo.

This skill guides the user through `00_protocol/00_e_世界觀創建協議.md` and produces or updates:

- `01_world/01_a_世界觀總覽.md`
- `01_world/01_b_世界語言規格.md`
- `01_world/01_c_陣營與階級語言.md`
- `02_vocabulary/02_a_專有名詞表.md`
- `02_vocabulary/02_b_俗稱與黑話表.md`
- `02_vocabulary/02_c_禁用詞與慎用詞表.md`
- `00_protocol/00_b_反ai味檢查表.md` §1 and §2 only
- `.protocol_version.phase_log`

The created entity groups are `W-rules`, `W-language`, and `V`. This skill also creates the project-specific `00_b` §1/§2 baseline used by later QA.

## 觸發協議

- Trigger phrase: `/create-world`
- Chinese alias wrapper: `/建立世界觀`
- Authority protocol: `00_protocol/00_e_世界觀創建協議.md`
- Full question script authority: `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.1.2
- D-047 registry contract: `_design/INTEGRATION_CONTRACTS.md` §4a Contract D
- Registry fallback template: `_design/registries/issue_type_registry.template.yaml`

`/create-world` is conversational. Do not accept direct user parameters as a substitute for the five stages.

## 啟動條件

Before Phase 1, confirm the current working root is an Instance root.

Required checks:

1. `.protocol_version` exists.
   - If missing, stop and tell the user to run `/init-project` first.
2. `.protocol_version.phase_log` does not contain an entry with `phase: create-world` and `status: completed`.
   - If such an entry exists, stop and tell the user to run `/iterate-world` instead.
3. `<instance_root>/issue_type_registry.yaml` is readable.
   - If missing, load `_design/registries/issue_type_registry.template.yaml` as fallback and print a WARN before Phase 2.
   - If both registry and template are missing or unreadable, stop before Phase 2.
4. No active or in-progress protocol is currently operating on `W-rules`, `W-language`, or `V`.
5. Target files are not `LOCKED` in the sections this skill must write.
   - If a target file has `狀態：LOCKED`, do not overwrite it.
   - Prepare a blocked-write report path as defined by `00_e` and ask the user for a decision.

Use this condition failure format:

```md
## 條件未滿足 / Prerequisites Not Met

What:
Where:
Why:
下一步:
```

Do not expose stack traces, parser internals, or enum keys in user-facing errors.

## D-047 Registry Alignment

This skill must use D-047 dynamic issue construction. Do not hardcode the final Phase 2 issue list.

### Registry Load Timing

Load `<instance_root>/issue_type_registry.yaml` exactly once at skill startup.

- No mid-session hot reload.
- If the user edits the registry during the session, tell them to restart `/create-world`.
- If the Instance registry does not exist, use the Template fallback once, print WARN, and continue only if the fallback schema is valid.

### Skill Key

Use only the `00_e_world` skill key.

Expected registry sections:

- `core.00_e_world`
- `user_extensions.00_e_world`
- `core_overrides.00_e_world`

`user_extensions` and `core_overrides` may be empty. `core.00_e_world` must exist.

### Schema Validation

Reject before Phase 2 if any ERROR condition is present:

- Missing `core.00_e_world`.
- Any core issue id is outside `1-99`.
- Any `user_extensions.00_e_world[*].id` is lower than `100`.
- Any user extension id duplicates a core id.
- Any issue has invalid `required_level`; allowed values are `REQUIRED`, `STRONGLY_PREFERRED`, `OPTIONAL`.
- Any `locked` value is not boolean.
- Any issue is missing `id`, `name`, `required_level`, `locked`, `question_summary`, or `protocol_ref`.
- Any unsupported skill key appears where the parser treats it as invalid.
- YAML parse failure.

WARN but continue:

- `user_extensions[*].locked = true`: treat as `false`.
- `core_overrides[*].skip_id` points to a `locked=true` core issue: ignore the override and warn.
- `core_overrides[*].skip_id` does not exist in core: ignore the override and warn.
- Instance registry missing and Template fallback is used.

### Dynamic Issue List Algorithm

Build Phase 2 issue list as:

```text
core + user_extensions - core_overrides
```

Execution details:

1. Sort core issues by ascending `id`.
2. Apply `core_overrides.00_e_world[*].skip_id`.
   - If the target core issue has `locked: true`, ignore the override and print:
     `WARN: locked 議題 id=<n> 不可 SKIP，core_overrides 條目被忽略`
   - If the target core issue has `locked: false`, remove it from the Phase 2 issue list.
   - If `skip_id` is absent from core, print:
     `WARN: core_overrides skip_id=<n> 找不到對應 core 議題；條目被忽略`
3. Sort `user_extensions.00_e_world` by ascending `id`.
4. Append sorted user extensions after core.
5. For each issue, use `question_summary` only as the opener.
6. For core issues, use `protocol_ref` to fetch the complete script from `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.1.2.
7. For user extensions, treat `protocol_ref: user-defined` as project-local; ask from `question_summary`, record the answer, and do not invent upstream write authority unless the user confirms how it maps into Phase 4.
8. Do not rewrite, condense, or replace the UD §1.1.2 core scripts. `00_e` §10 is only a speed reference.

### Required Level Behavior

For every issue in the dynamic list:

- `REQUIRED`: the user must answer before Phase 4. Missing REQUIRED content blocks Phase 4.
- `STRONGLY_PREFERRED`: the user may skip; if skipped, record the gap in `phase_log.issue_completions` and mark TODO in the relevant split file or preview.
- `OPTIONAL`: the user may skip without phase_log gap detail.

Protocol-specific guard:

- The boundary reminder issue (`00_e` §10.10) must be confirmed before Phase 3. If the user does not confirm the protocol boundary, stop before convergence even if the registry marks it as `STRONGLY_PREFERRED`.

### Registry Boundaries

The registry contains only user-facing issues. It does not contain:

- Phase 4 split rules.
- Frontmatter rules.
- File write order.
- Section anchors.
- Entity completion formulas.

Those mechanics remain fixed in `00_e` and this SKILL.md.

## 流程

Run the five stages in order. Do not skip or merge stages unless `00_e` explicitly permits it and the user has confirmed.

### Phase 1: Diagnostic

Start with this prompt:

```md
世界觀是這個專案的第一塊基石。請貼出一段你對這個世界的完整想法，可以包含類型、規則、能量觀、社會結構、人民生活、價值觀、宗教、語言、語感等任何你已經想過的。越長越好；空白處我會幫你補洞。
```

After the user responds, produce a chat-only diagnostic report using `00_a` diagnostic mode. Do not write files.

The report must include:

1. Initial world type and narrative tone reading.
2. Confirmed world-rule material.
3. World-language and dialogue-style hypotheses.
4. Confirmed content.
5. Unconfirmed content needing human confirmation.
6. Suggested next step and Phase 2 issue-list preview.

Phase 1 prohibitions:

- Do not write any file.
- Do not create characters, plotlines, scenes, relationships, tasks, or dialogue.
- Do not turn inference into official setting.
- Do not fill missing world rules on behalf of the user.

### Phase 2: Exploration

At the start of Phase 2, print the dynamic issue list built from `00_e_world`.

For each issue:

- Ask at most three questions at a time.
- Include why the question matters.
- Include which split file or section the answer will affect.
- Allow `跳這題`, `先跳到議題 X`, and `中止`.
- Print issue progress after each completed issue.
- If the answer conflicts with existing settings, stop and discuss the `CONFLICT`; do not continue as if it is confirmed.

Core issue scripts:

- `10.1 世界類型快速分類`: use UD §1.1.2 §10.1 as the full script.
- `10.2 世界規則最小集`: use UD §1.1.2 §10.2 as the full script.
- `10.3 科技水平`: use UD §1.1.2 §10.3 as the full script.
- `10.4 人民生活水準`: use UD §1.1.2 §10.4 as the full script.
- `10.5 各項價值觀`: use UD §1.1.2 §10.5 as the full script.
- `10.6 宗教`: use UD §1.1.2 §10.6 as the full script.
- `10.7 語言層級切片`: use UD §1.1.2 §10.7 as the full script.
- `10.8 陣營與階級語言`: use UD §1.1.2 §10.8 as the full script.
- `10.9 類型語氣定位`: use UD §1.1.2 §10.9 as the full script.
- `10.10 越界禁區`: use UD §1.1.2 §10.10 as the full script.

Do not ask the user about §10.11 split rules as a standalone issue. Split rules are Phase 4 mechanics and appear only in the Phase 3 convergence preview for confirmation.

### Phase 3: Convergence

Create a chat-only "world convergence preview" and wait for user confirmation before writing.

The preview must include:

1. Final one-sentence conclusion for each user-facing issue.
2. The Phase 4 split plan with target files and sections.
3. The preview of `00_protocol/00_b_反ai味檢查表.md` §1 and §2 replacements.
4. `TODO`, `INFERENCE`, and `CONFLICT` lists.
5. The entities to create or update: `W-rules`, `W-language`, `V`.
6. Default frontmatter weights for the three entity groups.
7. A list of user-provided material this protocol will not process.

Allowed user replies:

- `通過`, `OK`, or `寫檔`: proceed to Phase 4.
- A requested modification: revise the preview and print it again.
- `中止` or `取消`: do not write files; if needed, record `status: aborted`.

If any `CONFLICT` remains unresolved, do not enter Phase 4.

### Phase 4: Execution

Before writing, re-check target file headers. Do not overwrite `LOCKED` content.

Write in this fixed order:

1. `01_world/01_a_世界觀總覽.md`
2. `01_world/01_b_世界語言規格.md`
3. `01_world/01_c_陣營與階級語言.md`
4. `02_vocabulary/02_a_專有名詞表.md`
5. `02_vocabulary/02_b_俗稱與黑話表.md`
6. `02_vocabulary/02_c_禁用詞與慎用詞表.md`
7. `00_protocol/00_b_反ai味檢查表.md` §1 and §2 only

Use local section replacement or append only. Do not rewrite unrelated sections.

#### Split Rules

Apply this fixed `00_e` §10.11 split table. **Target sections are identified by their heading TEXT — the real headings shipped in the templates — not by ordinal number.** Locate each section by matching its heading text, fill the user-confirmed content inside it, and preserve the section's existing subsection scaffolding.

| Source | Target file | Target section (match by heading text) | Write mode |
|---|---|---|---|
| 10.1 世界類型 | `01_world/01_a_世界觀總覽.md` | `# 4. 作品基本定位`（含 `## 4.1 類型參考`） | fill |
| 10.2 世界規則 | `01_world/01_a_世界觀總覽.md` | `# 6. 世界運作規則`（§6.1–§6.3） | fill |
| 10.3 科技水平 | `01_world/01_a_世界觀總覽.md` | `# 13. 魔法、科技或超自然系統` | fill |
| 10.3 derived modern-mismatch terms | `02_vocabulary/02_c_禁用詞與慎用詞表.md` | `§現代違和詞`（無則新增子節） | append |
| 10.4 人民生活 | `01_world/01_a_世界觀總覽.md` | `# 15. 日常生活`（必要時併 `# 11. 經濟與資源`） | fill |
| 10.5 價值觀 | `01_world/01_a_世界觀總覽.md` | `# 17. 道德結構`（兼填 `# 5. 世界基調`） | fill |
| 10.5 derived taboo topics | `01_world/01_a_世界觀總覽.md` | `# 22. 世界觀禁區` | append |
| 10.6 宗教 | `01_world/01_a_世界觀總覽.md` | `# 12. 宗教、信仰與禁忌` | fill |
| 10.6 derived religious terms | `02_vocabulary/02_b_俗稱與黑話表.md` | `§宗教衍生詞`（無則新增子節） | append |
| 10.7 語言層級 | `01_world/01_b_世界語言規格.md` | `# 3. 整體語言基調`（§3.1–§3.4）＋ `# 5. 本作品應該像什麼` | fill |
| 10.7 derived language-level terms | `02_vocabulary/02_c_禁用詞與慎用詞表.md` | `§語言層級詞`（無則新增子節） | append |
| 10.8 陣營階級語 | `01_world/01_c_陣營與階級語言.md` | `# 4. 陣營語言總表` ＋ `# 6. 階級語言總表` | fill |
| 10.8 derived faction taboo terms | `02_vocabulary/02_c_禁用詞與慎用詞表.md` | `§陣營詞`（無則新增子節） | append |
| 10.9 類型語氣 | `00_protocol/00_b_反ai味檢查表.md` ＋ `01_world/01_a_世界觀總覽.md` | `00_b` §1/§2 ＋ `01_a` `## 4.1 類型參考`、`# 5. 世界基調` | fill |
| 10.10 越界禁區 | no file write | — | list ignored material in the preview |

Section-anchor guard:

- Locate every target section by matching its heading text exactly. Do NOT target sections by ordinal number alone; the shipped `01_a` template has 24 sections and its numbering does not match the issue numbers above.
- `fill` means: replace the placeholder / example content inside the matched section with the user-confirmed content, keeping the section heading and all its subsection headings intact. Do not delete subsection scaffolding and do not rewrite unrelated sections.
- If a listed heading cannot be found in the current template, stop and report `CONFLICT(<file>:<heading>)` and ask the user to confirm the correct section. Do NOT create a new top-level section (for example a `# 0. 本作基線` section) and do NOT overwrite a different section as a substitute.

`02_vocabulary/02_a_專有名詞表.md` participates in the write pass for `V`; write only confirmed proper-noun vocabulary that the user explicitly supplied during Phase 2. If none exists, preserve the file and do not invent terms.

#### Frontmatter Rules

When creating or repairing target frontmatter, preserve the Chinese 5-field header and apply this YAML block:

| File | entities | depends_on | weight |
|---|---|---|---|
| `01_world/01_a_世界觀總覽.md` | `[W-rules]` | `[]` | `{W-rules: 1.0}` |
| `01_world/01_b_世界語言規格.md` | `[W-language]` | `[W-rules]` | `{W-language: 1.0}` |
| `01_world/01_c_陣營與階級語言.md` | `[W-language]` | `[W-rules]` | `{W-language: 0.5}` |
| `02_vocabulary/02_a_專有名詞表.md` | `[V]` | `[W-rules, W-language]` | `{V: <part_weight>}` |
| `02_vocabulary/02_b_俗稱與黑話表.md` | `[V]` | `[W-rules, W-language]` | `{V: <part_weight>}` |
| `02_vocabulary/02_c_禁用詞與慎用詞表.md` | `[V]` | `[W-rules, W-language]` | `{V: <part_weight>}` |
| `00_protocol/00_b_反ai味檢查表.md` | none | none | none |

`00_b` is a protocol file and may omit the YAML entity block.

#### Status Bump（解除下游 prereq 卡關）

`/create-character` 的啟動條件要求 `W-rules` / `W-language` / `V` 三實體各自至少為 `REVIEW`。本 skill 寫檔後，必須把本次實際寫入且 REQUIRED 內容已完成的目標檔 `狀態` 由 `DRAFT` 升為 `REVIEW`（已是 `REVIEW` / `FINAL` / `LOCKED` 者不動）：

- `01_a` / `01_b` / `01_c`：前提為對應議題（§10.2/§10.7/§10.8 等）未被跳過且已寫入確認內容。
- `02_a` / `02_b` / `02_c`：前提為有使用者確認的內容寫入。
- 因議題被跳過而未寫入的檔案，保留原 `狀態` 並依下方「Missing, Inference, and Conflict Markers」標記為不完整，**不**做升級。
- 升級僅修改 `狀態` 與 `最後更新` 兩個 header 欄位，不更動其他 header 欄位、不更動 YAML block。

此步驟讓 `/create-world` 正常完成後，`W-rules` / `W-language` / `V` 直接達到下游門檻，使用者不需再手動改狀態。若任一 REQUIRED 實體因跳題而停在 DRAFT，於 Phase 5 明確提示該實體尚未達 REVIEW、下游 `/create-character` 會被擋。

#### Missing, Inference, and Conflict Markers

Use these markers exactly when needed:

```md
<!-- TODO(<issue_id>): <what is missing and when it may be completed> -->
<!-- INFERENCE: <basis>; 待人類確認 -->
<!-- CONFLICT(<file>:<section>): 既有=<existing>, 本次想寫=<new>. 請人類拍板 -->
```

Rules:

- Do not use `INFERENCE` as a replacement for `TODO`.
- Record skipped `STRONGLY_PREFERRED` issues in the convergence preview and phase_log.
- If a `REQUIRED` issue is incomplete, refuse Phase 4.
- If §10.9 is skipped, do not write `00_b` §1/§2 and mark TODO.
- If §10.7 is skipped, do not write `01_b`; mark `W-language` as incomplete.
- If §10.8 is skipped, do not write `01_c`; mark the faction-language baseline as missing.
- If §10.10 is not confirmed, stop before Phase 3.

#### Phase Log

At Phase 1 start, append or prepare an in-progress entry.

At successful Phase 5 completion, update the same entry to:

```yaml
- phase: create-world
  date: <ISO date>
  skill: /create-world
  status: completed
  created_entities: [W-rules, W-language, V]
  issue_completions: {<議題 id>: <答完/跳過>, ...}
```

If aborted, update the same entry to `status: aborted` and include `abort_reason` plus `detail`.

If any write step fails, rollback this skill's changes and do not mark the phase completed.

### Phase 5: Validation

After Phase 4 writes succeed, automatically invoke `/status`.

Show:

1. Files created or updated by this skill.
2. Whether `W-rules`, `W-language`, and `V` now appear.
3. Current completion level for each of those entity groups.
4. Expected entity manifest comparison.
5. Whether `.protocol_version.phase_log` contains `phase: create-world` and `status: completed`.
6. Next suggested skill: `/create-character`.

Do not automatically invoke `/create-character`.

## 輸入

The user provides worldbuilding material through conversation during Phase 1 and Phase 2.

Acceptable input includes:

- Long-form initial world idea.
- Answers to issue questions.
- Explicit skips.
- Conflict decisions.
- Confirmation to write.

Do not treat command-line arguments, slash-command suffixes, or one-line parameter lists as a substitute for the protocol conversation.

## 輸出

Runtime output includes:

- Phase 1 diagnostic report in chat.
- Phase 2 dynamic issue list and progress updates in chat.
- Phase 3 convergence preview in chat.
- Phase 4 file writes only after user approval.
- Phase 5 `/status` validation output.

Runtime file outputs may include only the files listed in `## 用途`, plus blocked-write or conflict reports required by `00_e`.

## 邊界

Hard prohibitions:

- Do not skip stages.
- Do not complete missing user settings on your own.
- Do not edit `issue_type_registry.yaml`; registry edits are the user's responsibility.
- Do not overwrite `LOCKED` files.
- Do not change `00_protocol/00_e_世界觀創建協議.md`.
- Do not create characters, relationships, plotlines, chapters, scenes, task packs, or dialogue.
- Do not call any other `/create-*` skill.
- Do not add entity types, enum values, protocols, schemas, or parser code.
- Do not write project-specific content into the Template repo.
- Do not treat examples, inferred material, or skipped answers as confirmed settings.

## 錯誤呈現規則

Use one of these headings:

- `## 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## 條件未滿足 / Prerequisites Not Met` for repository state problems.

Each error must include:

- `What`: what failed.
- `Where`: file, section, or phase.
- `Why`: why the skill cannot continue.
- `下一步`: one concrete action the user should take.

For multiple errors, summarize the count first, then list each item.
