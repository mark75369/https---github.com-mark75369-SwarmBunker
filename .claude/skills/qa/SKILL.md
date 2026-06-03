---
name: qa
description: "Run the Phase C /qa quality-assurance pipeline for one dialogue version. Use when the user triggers /qa with a dialogue path, a scene_id plus version, or no argument. The skill performs the five UD §2.5 stages, requires all eight QA reports from D-043, writes only approved QA reports plus two dialogue frontmatter fields, and records R8-INFO-06 by treating 00_k v0.1 five-report wording as stale."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/qa` skill runtime instructions
優先級：高

# /qa Skill

## 用途

Use this skill when the user triggers `/qa` to run quality assurance for one existing dialogue version tied to a scene entity `S-<ch>-<n>`.

This is the final downstream Phase C skill. It reads a dialogue file produced by `/dialogue-write`, resolves its task pack and upstream entity context, runs the eight mandatory QA checks, then writes exactly eight QA report files after explicit user approval.

Runtime outputs may include:

- `09_quality_assurance/<base>_<QA_類型>_報告.md` x 8
- target dialogue frontmatter updates for `pipeline_state` and `qa_decision`
- `.protocol_version.phase_log` runtime tracking

This skill creates no new scene, character, relationship, plot, vocabulary, world, art, parser, schema, enum, or final-gating artifact. It does not create `09_e`; `09_e` remains the human final-gating record.

## QA 立場宣告（Adversarial Stance）

`/qa` 是對抗式審查，不是確認。執行時 agent 必須採以下立場，且此立場為預設、不依賴任何偵測：

1. **對抗式預設**：QA agent 的預設立場是「這個版本有問題，我要把它找出來」，而非「證明它可以過」。不得以「看起來沒問題」當作 PASS 理由。
2. **審≠寫隔離原則**：執行 `/qa` 時，agent 必須以「我沒有寫過這份台詞、我是外部審查者」的視角運作。禁止引用「我剛才寫這句時的意圖」作為通過理由；只能引用台詞檔落地的字面內容 + 上游 LOCKED/FINAL 事實。
3. **冷啟動重讀**：Stage 1 必須從磁碟重新讀取目標台詞檔與所有上游來源，不得依賴同對話 context 中生成階段的記憶。若偵測到本次 `/qa` 與產出該台詞的 `/dialogue-write` 在同一 runtime context，必須在 Stage 1 元資訊印出 `審查隔離警示：本次 QA 與生成同源，已強制冷啟動重讀`。
4. **舉證責任反轉**：每份報告的 PASS 不是預設。agent 必須主動列出「我嘗試攻擊本項的切角 + 為何攻不破」才允許判 PASS；只列「看起來沒問題」而無實際攻擊切角的報告視為審查不完整，該報告計為 FAIL。

協議對齊註記（stale，協議回填延後）：`00_protocol/00_a_台詞生產協議.md` §3.9 現僅規範「只檢查不大改 / 生命力保護 / 禁止事項」，尚未寫入「對抗式立場 / 審≠寫隔離」原則句。本宣告先於 SKILL.md runtime 層落地；待 D-B1（草擬 D-060）拍板後回填 00_a §3.9，屆時本段改為引用協議。比照本檔 R8-INFO-06 既有 stale 處理風格，協議與本 skill 行為以本段為準，不因協議尚未更新而失效。

## 觸發語

English trigger:

- `/qa <input>`

Accepted input modes are locked to these three shapes:

| Mode | User input | Resolution |
|---|---|---|
| Full dialogue path | `/qa 08_dialogue_outputs/CH01_S03_<short>_dialogue_v02.md` | Use the exact target dialogue file |
| Scene ID + version | `/qa S-01-03 v02` | Resolve the dialogue path from `.protocol_version.phase_log` |
| No args | `/qa` | Use the previous `/dialogue-write` converged output from `.protocol_version.phase_log` |

Chinese alias wrapper:

- `/檢查 <input>`, via `.claude/skills/檢查/SKILL.md`

Reject all other input forms, including multiple dialogue files, ranges, branch labels without a concrete file, unknown flags except `--scope` for 09_i, or a bare version without `scene_id`.

`--scope` is optional only for 09_i cross-scene range and must be one of `chapter`, `arc`, or `all`. It is not an on/off switch; 09_i is always part of the eight-report run.

## 觸發協議

Primary authority:

- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.5.1-§2.5.6 for the five internal `/qa` stages
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §3.1-§3.9 for the eight QA algorithms
- `_design/TASKS.md` v1.9 §D.4 and §D.3.5
- `_design/SPEC.md` v1.2 §12.3 and §12.7
- `_design/ARCHITECTURE.md` v1.6 §6.3, §3.3.1, and §3.3.2

Required references:

- `_design/DECISIONS_LOG.md` v2.0 §6.7-§6.9 D-043, §6.12.2 D-050, §6.13.2 D-051, §6.16.2 D-053, §6.17.2 D-054
- `_design/POST_LOCK_PENDING.md` v0.12
- `_design/registries/qa_type_registry.template.yaml` v0.1
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1 and §4.2
- `00_protocol/00_a_台詞生產協議.md` §3.9 QA mode methods
- `.claude/skills/scene-task/SKILL.md` v0.1
- `.claude/skills/dialogue-write/SKILL.md` v0.1
- `.claude/skills/init-project/SKILL.md` v0.3
- `.claude/skills/create-character/SKILL.md`, `.claude/skills/create-relationship/SKILL.md`, `.claude/skills/create-outline/SKILL.md`, `.claude/skills/create-detailed-outline/SKILL.md` for D-050 boundary block style
- `09_quality_assurance/09_a_ai味qa報告模板.md`
- `09_quality_assurance/09_b_角色聲線一致性檢查模板.md`
- `09_quality_assurance/09_c_禁用詞檢查報告模板.md`
- `09_quality_assurance/09_d_資訊控制檢查報告模板.md`
- `09_quality_assurance/09_f_類型偏移檢查模板.md`
- `09_quality_assurance/09_g_節奏感檢查模板.md`
- `09_quality_assurance/09_h_對話張力檢查模板.md`
- `09_quality_assurance/09_i_跨場一致性檢查模板.md`
- `09_quality_assurance/09_e_定稿變更紀錄模板.md` for context only; do not produce it
- `08_dialogue_outputs/08_a_台詞版本管理規範.md` for version-management context only; do not patch it from this skill

Authority notes:

1. UD §2.5.3 v0.3 plus D-043 is the authority for the eight-report run and sequence order.
2. `/qa` does not use D-047 dynamic issue loading. It runs the existing eight QA templates and rejects if any required template is missing.
3. The registry-backed QA pipeline set is the eight core `qa_type` values: `AI_FLAVOR`, `VOICE_CONSISTENCY`, `FORBIDDEN_WORD`, `INFO_CONTROL`, `GENRE_DRIFT`, `RHYTHM`, `DRAMATIC_TENSION`, `CROSS_SCENE_CONTINUITY`.
4. `09_e` is a final-gating record, not a `/qa` output. Do not assign it a `/qa` PASS/FAIL report decision.
5. Write boundaries are controlled by D-050 and this SKILL.md, not by broader protocol examples.

**R8-INFO-06 註記：** 本 skill 對齊 UD §2.5.3 v0.3 + D-043 8 報告為權威；`00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3 仍寫 5 報告屬 pre-D-043 stale，不影響本 skill 行為。`00_k` v0.2 升版屬 9th master cleanup queue；本 skill 不 patch `00_k`。

## 啟動前檢查

Before Stage 1, verify all prerequisites below. If any prerequisite fails, stop before Stage 1 and write nothing.

### Instance and Template-detect checks

1. Current folder is the Instance repo root and contains `00_protocol/`, `08_dialogue_outputs/`, and `09_quality_assurance/`.
2. **D-051 後 active single marker check:** no `.template_root` marker file exists at repo root.
3. `.protocol_version` exists.
4. `.protocol_version.phase_log` contains `phase: bootstrap` with `status: completed`.
5. `_design/expected_entities.yaml` exists.
6. Do not use the removed D-049 structural inference rule. Do not block only because `_design/registries/*.template.yaml` exists.

If `.template_root` is present, stop with:

```md
## ⏸ 條件未滿足 / Prerequisites Not Met

What: 偵測到 `.template_root` marker；此目錄仍被標識為 Template repo。
Where: repo root / .template_root
Why: /qa 只能在已 bootstrap 的 Instance repo 寫 QA 報告，不能污染 Template。
下一步: 若這是新 Instance，先完成 Template 轉 Instance 流程並移除 `.template_root`，再跑 /qa。
```

### Input and dialogue checks

1. Parse user input into exactly one of the three locked forms in `## 輸入鎖定（O6）`.
2. Resolve the target dialogue file and verify it exists under `08_dialogue_outputs/`.
3. Read the target dialogue file header and YAML frontmatter.
4. Verify the target dialogue `狀態` is at least `DRAFT` and is not `DEPRECATED`.
5. Verify `pipeline_state` is one of:
   - `DIALOGUE_CONVERGED`: standard path after the D.3.5 convergence gate.
   - `DIALOGUE_TRIAL`: path B exception; user must explicitly say they want direct QA on the trial version.
6. If `pipeline_state: DIALOGUE_TRIAL`, print the warning that `QA_PASSED` after this run cannot directly become `DIALOGUE_FINAL`; it must return to `DIALOGUE_CONVERGED` first.
7. Reject any target already marked `FINAL`, `LOCKED`, `DIALOGUE_FINAL`, or `DIALOGUE_LOCKED`. This skill is for pre-final QA, not final/locked retcon or audit.
8. Read `source_task` from the dialogue frontmatter and verify the task pack exists.
9. Read `entities` and `depends_on`; verify every concrete upstream entity required by the dialogue exists and is at least `REVIEW`.
10. From `source_task`, read the task pack and extract scene specs, required information, forbidden information, character voice-card references, relationship references, rhythm, risk_type, and scene goals.

If a `DIALOGUE_TRIAL` target is supplied without explicit path B wording, refuse with:

```md
## ✗ 無法執行 / Cannot Proceed

What: 目標台詞檔仍是 trial 版本，但本次指令沒有明示「直接對 trial 跑 QA」。
Where: <target dialogue path>
Why: D.3.5 預設要求先收斂為 `DIALOGUE_CONVERGED`；trial 直接 QA 是路徑 B 例外。
下一步: 請改跑 `/dialogue-write --converge ...` 產生 v02，或明確指示「直接對 v01A 跑 QA」後重跑。
```

### QA template checks

Verify all eight required templates exist before Stage 1:

| Template | qa_type |
|---|---|
| `09_quality_assurance/09_a_ai味qa報告模板.md` | `AI_FLAVOR` |
| `09_quality_assurance/09_b_角色聲線一致性檢查模板.md` | `VOICE_CONSISTENCY` |
| `09_quality_assurance/09_c_禁用詞檢查報告模板.md` | `FORBIDDEN_WORD` |
| `09_quality_assurance/09_d_資訊控制檢查報告模板.md` | `INFO_CONTROL` |
| `09_quality_assurance/09_f_類型偏移檢查模板.md` | `GENRE_DRIFT` |
| `09_quality_assurance/09_g_節奏感檢查模板.md` | `RHYTHM` |
| `09_quality_assurance/09_h_對話張力檢查模板.md` | `DRAMATIC_TENSION` |
| `09_quality_assurance/09_i_跨場一致性檢查模板.md` | `CROSS_SCENE_CONTINUITY` |

If any template is missing, refuse with `⏸ 條件未滿足` and tell the user to restore the missing template or check Phase A template inheritance. Do not silently run fewer reports.

### Write-set checks

Before asking for Stage 4 approval, compute the planned write set and verify it contains only:

- `09_quality_assurance/<base>_<QA_類型>_報告.md` x 8
- the target `08_dialogue_outputs/*.md` frontmatter fields `pipeline_state` and `qa_decision`
- `.protocol_version.phase_log`

Any other planned write is D-050 out of scope and must refuse before writing.

## 流程

Run the Stage 0 gate first, then exactly five stages. Do not skip stages. Do not write before Stage 4 is explicitly approved.

### Stage 0 - 上游交付真實性驗證（Upstream Delivery Verification, UDV）

This gate runs before Stage 1 and catches silent upstream failures: an upstream skill (typically `/dialogue-write`) may have only printed beats or a summary in chat while claiming the file was written, when the artifact does not actually exist on disk, is an empty shell, or its declared status does not match reality. If any of the five checks below fails, stop with `⏸ 條件未滿足`, write nothing except an `aborted` phase_log entry with the matching `abort_reason`, and do not enter Stage 1.

Run all five checks in adversarial mode (do not trust any claimed value without verifying it against the actual file on disk):

1. **台詞檔內容缺陷（empty-shell / no-op delivery）**：目標台詞檔不只必須存在，還必須含實際台詞 body（有具體對白行），而非只有 frontmatter + 標題 + 節拍/大綱/TODO 佔位。掃描無聲失敗指紋——整檔只有 `（此處待補）` / `TODO` / 「以下為節拍」「beat 1/2/3」而無對白，或 body 行數異常少於任務包戲劇目的所需。命中 → 標記 `SUSPECTED_NO_OP_DELIVERY`，abort，`abort_reason: upstream_delivery_unverified`。
   - 白名單：若 frontmatter `mode_tag` 屬大綱/節拍類，或 user 明示「這是節拍/大綱稿」，改印 WARN 不 abort（破格/節拍稿本就不該進標準 QA）。
2. **phase_log 謊報（claimed-vs-actual 交叉比對）**：phase_log 最近一筆 `/dialogue-write` 若宣稱 `status: completed` 並列出 `dialogue_paths`，逐一驗證磁碟真的存在這些檔。phase_log 說 completed 但檔不在 → abort，列出哪些宣稱檔缺失，`abort_reason: upstream_delivery_unverified`。
3. **pipeline_state 狀態謊報**：frontmatter `pipeline_state` 若宣稱 `DIALOGUE_CONVERGED`，但 phase_log 找不到對應 `/dialogue-write --converge` 的 completed 紀錄 → 判狀態謊報，abort，`abort_reason: upstream_delivery_unverified`。同理 `entities` / `depends_on` 宣稱的依賴狀態若與檔內實際 `狀態` 不符（宣稱 >= REVIEW 但實際 DRAFT）→ 一併判謊報。
4. **上游 gate 跳步**：`source_task` 指的任務包不只必須存在，還必須含核心欄位非空（場景規格 / 必要資訊 / 禁止資訊 / 戲劇目的等）且任務包 `狀態 >= REVIEW`。任務包是空殼或仍 DRAFT → 判上游 gate 跳步（`/dialogue-write` 不該在任務包未過 review gate 時產出），abort，`abort_reason: upstream_gate_skipped`。
5. **宣稱已寫外部檔但檔不存在**：phase_log 或 frontmatter 任何「已寫入 / 已產出」的外部檔路徑宣稱，逐一驗證磁碟存在。宣稱已寫但檔不存在 → abort，列出缺失路徑，`abort_reason: upstream_delivery_unverified`。

Stage 0 abort 文案沿用 `⏸ 條件未滿足` 的 What/Where/Why/下一步 四件套，明寫命中哪一條 UDV 檢查與對應 `abort_reason`。Stage 0 為純讀取 gate，未命中即進 Stage 1；命中只寫一筆 `aborted` phase_log。

### Stage 1 - Diagnosis, per UD §2.5.2

1. Parse the user input into full path, scene ID + version, or no-argument phase_log fallback.
2. Read the target dialogue file.
3. From `source_task`, resolve and read the task pack.
4. From `entities` and `depends_on`, resolve C-* voice cards, R-*-* relationship matrices, and other relevant upstream context.
5. Verify `狀態 >= DRAFT` and valid `pipeline_state`.
6. Identify whether this is the standard `DIALOGUE_CONVERGED` path or the explicit `DIALOGUE_TRIAL` path B exception.
7. Print "本次 QA 對象元資訊" to chat:
   - scene_id
   - target dialogue path
   - dialogue status
   - pipeline_state
   - mode_tag
   - source_task
   - relevant entities
   - relevant depends_on
   - path type: standard or trial path B
   - 09_i scope
   - depth layer（試寫層 / 標準層 / 定稿層，依 `## 按深度分層的嚴格度` 由 pipeline_state + user 明示加嚴意圖推導；8 份全跑不變）
   - 審查隔離警示（若本次 QA 與生成 `/dialogue-write` 同源，依 `## QA 立場宣告` 第 3 條印出冷啟動重讀警示）
8. Stop after diagnosis if prerequisites fail.

### Stage 2 - Run eight reports, per UD §2.5.3 v0.3 + D-043

Run all eight checks. They may be analyzed in parallel, but the user-facing report summary must be printed in the sequence defined in `## 8 報告序列印出順序（UD §2.5.3 v0.3 + D-043）`.

**多視角（multi-lens）執行原則**：每份報告不得只用單一視角問一次「OK 嗎」。每份報告必須以一對對立 lens 各查一面（lens 對見 `## 8 報告詳細 algorithm` 表的「Lens 對」欄）：lens A 為嚴格/規則派、lens B 為生命力/創作派。兩 lens 必跑。每份報告的輸出必須含四項：`lens A 結論` / `lens B 結論` / `是否分歧` / `分歧時的 escalate 結果`，而非單一 PASS/FAIL。**若兩 lens 結論不一致，不得取寬鬆者收斂**，必須 escalate（折疊為該報告 FAIL）並列出分歧點交人類；lens B 的「生命力辯護」結果直接填 00_a §3.9.3 既有的「可保留不規則亮點 / 不建議機械修正項」兩表，與既有協議無縫接。多 lens 為 SKILL.md runtime 執行方法細化，不改 UD 八演算法定義、不新增協議概念。

Parallel check set:

| # | Template | qa_type | Algorithm source |
|---|---|---|---|
| 1 | `09_a_ai味qa報告模板.md` | `AI_FLAVOR` | UD §3.1 |
| 2 | `09_b_角色聲線一致性檢查模板.md` | `VOICE_CONSISTENCY` | UD §3.2 |
| 3 | `09_c_禁用詞檢查報告模板.md` | `FORBIDDEN_WORD` | UD §3.3 |
| 4 | `09_d_資訊控制檢查報告模板.md` | `INFO_CONTROL` | UD §3.4 |
| 5 | `09_f_類型偏移檢查模板.md` | `GENRE_DRIFT` | UD §3.5 |
| 6 | `09_g_節奏感檢查模板.md` | `RHYTHM` | UD §3.7 |
| 7 | `09_h_對話張力檢查模板.md` | `DRAMATIC_TENSION` | UD §3.8 |
| 8 | `09_i_跨場一致性檢查模板.md` | `CROSS_SCENE_CONTINUITY` | UD §3.9 |

`09_e` is not part of Stage 2. Do not generate it, draft it, or count it as one of the eight.

### Stage 3 - Aggregate, per UD §2.5.4 v0.3 + D-043

1. Aggregate the highest-priority issues from all eight reports in the user-facing sequence order.
2. Calculate overall `qa_decision` using `## qa_decision 計算規則`.
3. Print "彙整摘要" to chat:
   - overall qa_decision
   - per-report decision table
   - top issues, ordered by 09_f -> 09_d -> 09_h -> 09_b -> 09_g -> 09_a -> 09_c -> 09_i
   - whether the target dialogue will become `QA_PASSED` or `QA_FAILED`
   - planned report file paths
4. Ask for explicit approval before Stage 4 writes.

### Stage 4 - Write files, per UD §2.5.5 v0.3 + D-043

Only after user approval:

1. Write exactly eight QA report files under `09_quality_assurance/`.
2. Use filenames shaped as `<base>_<QA_類型>_報告.md`.
3. Give every report the Chinese five-field header.
4. Give every report the full downstream YAML block:

```yaml
---
entities: [S-<n>-<m>]
depends_on: [<相關 C-*、R-*-*>]
weight: {S-<n>-<m>: 0.125}
scene_id: S-<n>-<m>
source_task: <任務包路徑>
source_dialogue: <目標台詞檔路徑>
source_dialogues: null
pipeline_state: QA_PASSED
mode_tag: null
qa_decision: PASS
qa_type: AI_FLAVOR
---
```

5. Set report `pipeline_state` and `qa_decision` according to the overall result:
   - overall PASS -> `pipeline_state: QA_PASSED`, `qa_decision: PASS`
   - overall FAIL -> `pipeline_state: QA_FAILED`, `qa_decision: FAIL`
6. Set each report `qa_type` to its own enum value.
7. Update the target dialogue frontmatter only for:
   - `pipeline_state: QA_PASSED` or `QA_FAILED`
   - `qa_decision: PASS` or `FAIL`
8. Do not modify the dialogue body.
9. Do not create `09_e`.
10. If the target dialogue becomes `LOCKED` between Stage 1 and Stage 4, stop before writing and ask for a decision.

### Stage 5 - Verification, per UD §2.5.6 v0.3 + D-043

After Stage 4 writes succeed:

1. Automatically invoke `/status` for validation.
2. Confirm the target scene completion change:
   - `QA_PASSED` should raise `S-<n>-<m>` toward 90%.
   - `QA_FAILED` should be visible as incomplete QA state and must not be treated as final.
3. Append or update one `.protocol_version.phase_log` entry with `status: completed`.
4. Print written report paths and the updated target dialogue path.
5. Print the QA conclusion and next-step advice:
   - If this run was at 試寫層 (`DIALOGUE_TRIAL`): print `早期試寫薄檢的 PASS 不等於可升 FINAL；升 FINAL 前須回 DIALOGUE_CONVERGED 重跑標準層或定稿層`.
   - PASS: `人類確認可定稿 -> 填 09_e final-gating 紀錄 -> 升 狀態: FINAL + pipeline_state: DIALOGUE_FINAL`
   - FAIL: `修稿路徑 A（修稿後重跑 /qa）/ 重生路徑 B（回 DIALOGUE_TRIAL 跑新一輪 /dialogue-write）/ 人類裁決保留路徑 C（保留違規亮點；填 09_e 留證）`
6. Print the prohibitions:
   - Do not auto-promote to `FINAL`.
   - Do not auto-create `09_e`.
   - Do not auto-promote to `LOCKED`.
   - Do not auto-trigger any downstream gate or skill.

## 8 報告詳細 algorithm

Use each live template for output structure. Use these UD algorithm summaries as execution guardrails. Every report runs the dual-lens method from Stage 2: lens A (strict / rule) and lens B (life-force / creative) each query once; divergence escalates to FAIL.

| Report | qa_type | Algorithm summary | Lens 對（A 嚴格 / B 生命力；雙 lens 必跑；分歧 → escalate）|
|---|---|---|---|
| 09_a AI 味 | `AI_FLAVOR` | Read dialogue lines, project `00_b` style baselines, and character anti-drift lists; check sentence templates, abstract-word density, system-like voice, exposition tone, direct emotion, rhythm density, and retainable irregular highlights; coordinate with 09_b/09_d/09_f. | A=句型/抽象詞密度超標即 AI 味；B=風格核心派，這是作品語感非 AI 味（對齊 00_a §3.9.4 禁止把風格核心誤判 AI 味）。分歧 → 強制保留 + 標人類確認，計 FAIL。|
| 09_b 角色聲線一致性 | `VOICE_CONSISTENCY` | Read target dialogue, voice cards, `00_b §5`, relationship voice rules, and representative prior FINAL/LOCKED dialogue; test per-character voice profile, remove-name recognition, role arc timing, relationship diction, and cross-scene voice drift; coordinate with 09_a/09_c/09_d. | A=OOC 嚴判，偏離聲線卡即 FAIL；B=角色成長派，弧線階段允許聲線演化。分歧 → 標「聲線演化 vs OOC 爭議」交人類，計 FAIL。|
| 09_c 禁用詞 | `FORBIDDEN_WORD` | Mechanically scan dialogue, player options, UI, and task text against 02_a/02_b/02_c vocabularies, reveal timing, character-specific forbidden words, relationship taboos, arc-stage words, spoiler terms, modern mismatch terms, and frequency warnings; 09_c handles mechanical matches, not semantic intent. | A=機械/數據派，命中詞表即 FAIL；B=例外辯護派，檢視禁用詞的解禁時點是否已到。分歧 → 列證據交人類，計 FAIL。|
| 09_d 資訊控制 | `INFO_CONTROL` | Read task pack, 05_d information reveal table, 05_e foreshadow table, role knowledge boundaries, player knowledge state, branch information differences, forbidden topics, and prior FINAL/LOCKED dialogue facts; detect premature reveal, repeated reveal, hidden-knowledge violations, and semantic contradictions. | A=洩漏零容忍，任何疑似提前揭露即 FAIL；B=敘事需要派，這是必要鋪陳非洩漏。分歧 → 標「資訊邊界爭議」，計 FAIL。|
| 09_f 類型偏移 | `GENRE_DRIFT` | Read dialogue, project `00_b §1 §2 §3 §4 §6`, task pack, and 06_a risk_type; apply five-layer genre baseline checks, character x genre temperament checks, and classify drift as none/local/high-level/severe. This report controls the top priority because genre drift changes other report baselines. | A=嚴格類型守門，任何偏離基準即偏移；B=風格冒險辯護，這是刻意破格亮點。分歧 → 列為人類裁決（呼應 00_a §3.9.3 生命力保護），計 FAIL。|
| 09_g 節奏感 | `RHYTHM` | Compute sentence-length distribution, average, standard deviation, coefficient of variation, long/short swing score, paragraph breathing, pause density, and task-pack rhythm fit; use character voice preferences from 09_b context and feed scene-level rhythm metrics to 09_i. | A=機械/數據派，節奏指標超標即 FAIL；B=留白派，克制節奏是本場刻意設計。分歧 → 列證據交人類，計 FAIL。|
| 09_h 對話張力 | `DRAMATIC_TENSION` | Label each dialogue line as PUSH, YIELD, EXPOSE, or COUNTER; compute action proportions, tension_total, softness_total, intensity, task-goal alignment, high-risk pattern fit, and genre-adjusted tension strength; coordinate with 09_f, 09_g, 09_b, and 09_d. | A=張力不足即弱場；B=留白派，克制是本場刻意設計。分歧 → 標 NEEDS_REVIEW（折疊為 FAIL）交人類。|
| 09_i 跨場一致性 | `CROSS_SCENE_CONTINUITY` | Always run. Use `--scope=chapter` by default unless the user selects `arc` or `all`; exclude DRAFT/REVIEW/DEPRECATED/deleted and the current scene itself; compare cross-scene voice drift, information leaks/repeated reveals, implication conflicts, and rhythm/tension arcs using prior FINAL/LOCKED scenes and per-scene QA data. | A=機械/數據派，跨場指標衝突即 FAIL；B=例外辯護派，跨場差異是否真衝突。分歧 → 列證據交人類，計 FAIL。|

Per-report result values for this skill collapse into `PASS` or `FAIL` for the overall write. If a template has internal `NEEDS_REVIEW` wording, or if the two lenses diverge and the divergence has not been resolved by a human, treat it as `FAIL` for `/qa` frontmatter unless the user later handles it through human 09_e final-gating. The agent must not collapse a lens divergence to the more lenient lens on its own.

## 8 報告序列印出順序（UD §2.5.3 v0.3 + D-043）

Print user-facing report summaries in this exact order:

```text
1. 09_f 類型偏移檢查報告      （最優先 — 類型跑掉影響其他判定）
2. 09_d 資訊控制檢查報告      （資訊洩漏先於 character 層）
3. 09_h 對話張力檢查報告      （張力強度標準依類型；09_f 之後跑）
4. 09_b 角色聲線一致性報告    （角色 OOC 判定）
5. 09_g 節奏感檢查報告        （節奏依賴聲線；09_b 之後）
6. 09_a AI 味檢查報告         （表層字面層）
7. 09_c 禁用詞檢查報告        （機械詞表比對）
8. 09_i 跨場一致性檢查報告    （最後 — 需所有 per-scene 結果交叉比對）
```

Sequence logic:

- 09_f remains first because genre drift changes the baseline for all other judgments.
- 09_d remains before character-level checks because information leakage invalidates later voice judgments.
- 09_h is inserted after 09_f because dramatic tension standards depend on genre.
- 09_b precedes 09_g because character voice determines sentence-length and rhythm preferences.
- 09_a and 09_c remain late because they are surface/mechanical checks.
- 09_i is last because cross-scene continuity needs the per-scene results.

## 按深度分層的嚴格度（Depth Layering — 不破 D-043 八報告硬規）

D-043「8 份 QA 全跑、8 份全 PASS 才 PASS」是硬規，本 skill 不改變報告張數、不新增 pipeline_state / mode_tag enum。分層感放在「每份報告的嚴格度」，而非「跑哪幾份」——無論 tier 為何，永遠 8 份全跑、序列順序不變、qa_decision 仍需 8 份全 PASS。

依目標台詞檔的 `pipeline_state`（既有 enum，不新增）推導本次的嚴格度層級，並在 Stage 1 元資訊印出本次層級：

| 層級 | 觸發（既有 pipeline_state）| 8 份是否全跑 | 每份報告的深度 |
|---|---|---|---|
| 試寫層（lighter depth）| `DIALOGUE_TRIAL`（路徑 B 例外，user 明示直接對 trial 跑 QA）| 是，8 份全跑 | 每份報告允許簡化深度：聚焦該報告最硬傷的指標，lens 對仍雙跑但攻擊切角數可精簡；目的是快速回饋早期試寫，不放鬆 D-043 張數。|
| 標準層（standard depth）| `DIALOGUE_CONVERGED`（預設路徑）| 是，8 份全跑 | 每份報告依 `## 8 報告詳細 algorithm` 完整執行（現行行為，向後相容）。|
| 定稿層（stricter depth）| `DIALOGUE_CONVERGED` 且 user 明示要求加嚴（pre-FINAL 把關）| 是，8 份全跑 | 每份報告加嚴：09_i 至少 `--scope=arc` 起跳、`## QA 立場宣告` 的對抗式自檢逐項書面、lens 對全展開不得精簡、攻擊切角數需多於標準層。|

規則：

- 分層只調整「每份報告內部的審查深度與攻擊力度」，不調整報告張數、不調整序列、不調整 PASS 門檻（仍 8 份全 PASS）。
- 試寫層不得因簡化深度而靜默跳過任一份報告；簡化是「該份報告內部少跑幾個攻擊切角」，不是「少跑一份報告」。
- 試寫層 PASS 後，Stage 5 next-step 必須提醒：早期試寫薄檢的 PASS 不等於可升 FINAL，升 FINAL 前須回 `DIALOGUE_CONVERGED` 重跑標準層或定稿層。
- 不新增任何 enum 值（不新增 `--tier` 旗標對應的新 pipeline_state、不新增 mode_tag）；層級純由既有 `pipeline_state` + user 明示加嚴意圖推導，屬 SKILL.md runtime 判斷。

## qa_decision 計算規則

- **PASS:** all eight reports are PASS.
- **FAIL:** any one report is FAIL, missing, aborted, unparsable, not generated, **or has an unresolved lens divergence** (its two lenses disagree and no human has arbitrated). The agent must not self-collapse a lens divergence to the more lenient lens to manufacture a PASS.
- **ARBITRATE_REQUIRED:** only a later human final-gating decision may use this status through `09_e`; this skill never writes `ARBITRATE_REQUIRED`.

Overall state mapping:

| qa_decision | Target dialogue pipeline_state | QA report pipeline_state |
|---|---|---|
| `PASS` | `QA_PASSED` | `QA_PASSED` |
| `FAIL` | `QA_FAILED` | `QA_FAILED` |

Do not mark PASS when seven reports pass and one is missing. D-043 requires all eight reports.

## .protocol_version 寫入規範

If prerequisites fail before Stage 1, write nothing.

After successful Stage 4 writes and Stage 5 verification, append or update exactly one `qa` entry. Use concrete entity IDs and concrete file paths only. Do not write wildcard IDs such as `S-*`, `S-<n>-<m>`, or `CH-*` into runtime phase_log entries.

Completed entry shape:

```yaml
- phase: qa
  date: YYYY-MM-DD
  skill: /qa
  status: completed
  scene_id: S-01-03
  target_dialogue: 08_dialogue_outputs/CH01_S03_<short>_dialogue_v02.md
  qa_report_paths:
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_AI味_報告.md      # qa_type: AI_FLAVOR
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_聲線_報告.md      # qa_type: VOICE_CONSISTENCY
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_禁用詞_報告.md    # qa_type: FORBIDDEN_WORD
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_資訊控制_報告.md  # qa_type: INFO_CONTROL
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_類型偏移_報告.md  # qa_type: GENRE_DRIFT
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_節奏感_報告.md    # qa_type: RHYTHM
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_對話張力_報告.md  # qa_type: DRAMATIC_TENSION
    - 09_quality_assurance/CH01_S03_<short>_dialogue_v02_QA_跨場一致性_報告.md # qa_type: CROSS_SCENE_CONTINUITY
  qa_decision: PASS
```

Abort entry, when a Stage 0 UDV check fails or writes already began:

```yaml
- phase: qa
  date: YYYY-MM-DD
  skill: /qa
  status: aborted
  scene_id: S-01-03
  target_dialogue: 08_dialogue_outputs/CH01_S03_<short>_dialogue_v02.md
  qa_report_paths: []
  qa_decision: FAIL
  abort_reason: <short reason>
  detail: <human-readable detail>
```

`abort_reason` accepts a short free-text reason, plus these two Stage 0 UDV runtime tracking values (these are runtime log strings only; they are not new pipeline_state, mode_tag, or qa_type enum values, and do not change any registry):

- `upstream_delivery_unverified`: 上游宣稱已寫檔/完成，但磁碟實體缺失、空殼、或狀態謊報（UDV 第 1/2/3/5 條）。
- `upstream_gate_skipped`: 上游 gate 跳步，任務包空殼或未過 review gate 即產出台詞（UDV 第 4 條）。

Do not write real project-specific `.protocol_version` values inside this SKILL.md.

## 輸入鎖定（O6）

`/qa` accepts only these three input shapes.

### A. Full dialogue file path

Accepted:

- `/qa 08_dialogue_outputs/CH01_S03_<短名>_dialogue_v02.md`
- `/qa 08_dialogue_outputs/CH01_S03_<短名>_dialogue_v01A.md` only with explicit trial path B wording

Rules:

- Path must exist.
- Path must be under `08_dialogue_outputs/`.
- File must contain `scene_id`, `source_task`, `pipeline_state`, `mode_tag`, `qa_decision`, and `qa_type`.

### B. scene_id + version

Accepted:

- `/qa S-01-03 v02`
- `/qa S-1-3 v01A` after normalization

Rules:

- Normalize the scene ID to `S-01-03`.
- Resolve the concrete dialogue path from `.protocol_version.phase_log`.
- If multiple matching paths exist, refuse and ask for the full dialogue path.
- If no matching completed `/dialogue-write` entry exists, refuse and ask for the full dialogue path.

### C. No arguments

Accepted:

- `/qa`

Rules:

- Use the latest completed `/dialogue-write` entry that produced exactly one converged dialogue path.
- If the latest entry is trial with multiple paths, refuse and ask the user to choose a concrete path or explicitly invoke path B.
- If there is no unambiguous previous `/dialogue-write` result, refuse and ask for a full dialogue path.

Reject all other forms with `✗ 無法執行`.

## 輸出

Runtime output includes:

- Stage 1 diagnostic report in chat.
- Stage 2 eight-report progress in chat.
- Stage 3 aggregation summary in chat.
- Stage 4 write preview, approval request, eight QA report writes, and target dialogue frontmatter update after approval.
- Stage 5 `/status` validation, QA conclusion, and next-step advice.

Runtime file outputs are limited to:

- `09_quality_assurance/<base>_<QA_類型>_報告.md` x 8.
- Target `08_dialogue_outputs/*.md` frontmatter updates for `pipeline_state` and `qa_decision` only.
- `.protocol_version.phase_log`.

Required report frontmatter shape:

```yaml
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：CH<n>_S<m>_<short>_dialogue_vXX <QA 類型> QA 報告
優先級：中

---
entities: [S-01-03]
depends_on: [C-<name>, R-<a>-<b>]
weight: {S-01-03: 0.125}
scene_id: S-01-03
source_task: 07_scene_tasks/CH01_S03_台詞任務包.md
source_dialogue: 08_dialogue_outputs/CH01_S03_<short>_dialogue_v02.md
source_dialogues: null
pipeline_state: QA_PASSED
mode_tag: null
qa_decision: PASS
qa_type: AI_FLAVOR
---
```

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `09_quality_assurance/<base>_<QA_類型>_報告.md` x 8 | 8 份 QA 報告主體；D-043 必跑 |
| 合法 frontmatter 更新 | `08_dialogue_outputs/CH<n>_S<m>_<短名>_dialogue_v*.md` | 只動 `pipeline_state` + `qa_decision` 兩欄；不動 body |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: qa`, `scene_id`, `target_dialogue`, `qa_report_paths`, `qa_decision`, runtime log fields |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `10_art_assets/`, `00_protocol/`, `_tools/frontend/`, `scripts/`, `_design/`, `_design/registries/`, existing `.claude/skills/` files | 任何寫入都屬 D-050 越界 |
| 不寫 | `09_quality_assurance/09_e_*.md` | `09_e` 屬 final-gating 紀錄；人類在 D.4 後填；本 skill 嚴禁產生 |
| 不改 body | `08_dialogue_outputs/*.md` | 只動 frontmatter；不刪/改 user 保留的句子 |

## 邊界

The skill must not:

- modify LOCKED files without explicit file-specific confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, registry Template files, parser code, `_design/*.md`, or existing skill files
- modify existing Phase A, Phase B, Phase C C.1, or Phase C C.2 skills or wrappers
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scenes, task packs, or dialogue
- modify dialogue body content
- delete sentences marked `保留` by the user
- produce `09_e`
- skip any of the eight QA reports
- promote dialogue `狀態` to `FINAL` or `LOCKED`
- promote `pipeline_state` to `DIALOGUE_FINAL` or `DIALOGUE_LOCKED`
- auto-trigger D.4 final-gating, human FINAL/LOCKED gates, `/dialogue-write`, `/scene-task`, `/status` except Stage 5 validation, or any other skill
- create new entity types, enum values, schemas, parser behavior, or registry behavior
- add JSON export behavior or frontend behavior
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**

- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**

- 本 skill 寫檔目錄嚴格限定為 `09_quality_assurance/` 8 報告 + `08_dialogue_outputs/` frontmatter 兩欄更新。
- `.protocol_version.phase_log` 是 runtime tracking exception，只能記錄本 skill 的 `qa` entry，不得順手修其他 phase。
- 任何超出範圍的寫入屬越界。
- 越界寫入觸發 `⏸ 條件未滿足` 拒絕 + WARN，不靜默越界。
- 詳寫檔目錄表見本 SKILL.md `## 輸出` 段。

## 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If the target dialogue file becomes `LOCKED` between Stage 1 and Stage 4, stop before writing and ask for a decision.

If any of the eight reports cannot generate because a template is missing, parsing fails, required source context is unreadable, or report writing fails:

1. Stop further reports.
2. Roll back any partial reports written in the current run when possible.
3. Restore the target dialogue frontmatter if it was already changed in the current run.
4. Mark or keep the phase_log entry as `aborted`, not `completed`.
5. Report exactly which reports were attempted, written, rolled back, or require manual inspection.
6. Do not mark `qa_decision: PASS` even if the other seven reports passed.

If rollback is not possible, report the partial artifact path and tell the user to inspect it before retrying. Do not hide partial-write risk behind a success message.

If `/status` validation fails after successful writes, keep the written artifacts, print a validation warning in chat, and do not invent a new phase_log `status` value. Do not rewrite reports to hide the warning.

## 錯誤呈現規則

Use these headings:

- `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repository state or prerequisite problems.

Each error must include:

- `What`: what failed.
- `Where`: file, section, command, or stage.
- `Why`: why the skill cannot continue.
- `下一步`: one concrete action the user should take.

For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, raw enum-validation internals, or raw YAML objects in user-facing errors.
