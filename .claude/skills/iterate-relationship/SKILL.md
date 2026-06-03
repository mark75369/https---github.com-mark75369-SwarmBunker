---
name: iterate-relationship
description: "Iterate one concrete R-a-b relationship entity through the 00_j v0.2 five-stage iteration protocol and 00_l relationship context. Loads 00_l_relationship issue guidance, requires impact backtrace across both characters, timelines, scenes, dialogue, and QA before writes, permits only the D-050 relationship matrix/timeline plus narrow voice-card relationship-section merges, and does not write 00_b."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-relationship skill runtime instructions
優先級：高

# /iterate-relationship

## 用途

`/iterate-relationship` 用於迭代單一 `R-<a>-<b>` 關係實體，包含關係矩陣、關係變化時間線，以及兩端角色聲線卡中的關係段。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2 與 `00_protocol/00_l_關係創建協議.md` v0.2；關係張力變動會影響共同出場場景、台詞與 QA。本 skill 不寫 `00_b`。

## 觸發語

- `/iterate-relationship <a> <b>`
- 中文別名：`/迭代關係 <a> <b>`

`<a>`、`<b>` 是兩個角色名。缺任一參數時，階段 1 先要求 user 明示，不得猜測。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2。
- `00_protocol/00_l_關係創建協議.md` v0.2。
- `_design/ARCHITECTURE.md` v1.6 §5、§6.7。
- `_design/SPEC.md` v1.2 §5.2、§11。
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050、§6.16 D-053。
- `<instance_root>/issue_type_registry.yaml` 的 `00_l_relationship` key；缺漏時 fallback 讀 `_design/registries/issue_type_registry.template.yaml` 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。

`00_l_relationship` 是 D-047 後的 canonical key；不得使用舊 key 名。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 bootstrap completed。
3. `C-<a>` 與 `C-<b>` 皆存在，且可定位各自聲線卡。
4. `R-<a>-<b>` 或等價雙向 row 已存在於 `04_relationships/04_a_角色關係矩陣.md`，或 user 明示本次要修補既有關係 entry；若關係不存在且 user 要新增，提示應使用 `/create-relationship <a> <b>`。
5. 目標 `04_a`、可能的 `04_b`、兩端聲線卡關係段不是 `LOCKED`。
6. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用 `R-<a>-<b>` 或兩角色共同場景；若有，階段 2 先拒絕並列衝突 skill。
7. registry 可讀且含 `00_l_relationship`。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 目標關係 canonical id：`R-<a>-<b>`。
- 要改的部分：關係基調、權力差、動態時間線、稱呼、衝突點、和解/破裂條件、共同場景需求。
- 是否需要更新兩端角色聲線卡的「關係段」。
- 是否影響已產出的共同場景台詞與 QA。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做 direct / depends / indirect。若關係張力變動且已產出共同場景台詞，標示 `/qa` 09_h 對話張力重跑建議。若 pipeline 互鎖存在，等 user 拍板才進階段 3。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 `R-<a>-<b>` 與本輪結論。
- 本輪要處理的完整檔案清單。
- `04_a` row、`04_b` event、兩端聲線卡關係段的修改摘要。
- 下游共同場景、台詞、QA 受影響清單。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

寫檔順序：`04_a` → `04_b`（若需要 timeline event）→ 兩端 `03_characters` 聲線卡「關係段」section-level merge → `.protocol_version.phase_log`。03_characters 寫入只限兩端角色的關係段；不得重寫整張聲線卡。每檔寫前重讀 LOCKED 狀態；任一步出錯 rollback。

### 階段 5：實體驗證

驗證：

- `04_a` / `04_b` / 兩端關係段一致。
- `.protocol_version.phase_log` 含 `phase: iterate-relationship` 與 `modified_entity: R-<a>-<b>`。
- 未寫 `00_b` 或其他非 D-050 範圍檔。
- 下一步建議：重新看兩端角色視圖可跑 `/view-character <a>` / `/view-character <b>`；若共同場景台詞已產出，重跑 `/qa` 09_h。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 Markdown frontmatter。
2. direct：`entities` 含 `R-<a>-<b>` 的 `04_a` row 或關係檔。
3. depends：`depends_on` 含 `R-<a>-<b>`、`C-<a>` 或 `C-<b>` 的檔案。
4. indirect：從共同出場 `S-*-*` 擴張到 `07/08/09`。
5. 若 frontmatter 不完整，以角色名、雙人場景、關係段 anchor 補漏並提示補 `depends_on`。
6. 列出 LOCKED / FINAL / pipeline lock。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `04_relationships/04_a_角色關係矩陣.md` |
| depends | `04_relationships/04_b_關係變化時間線.md`、`03_characters/<a>_聲線卡.md` 關係段、`03_characters/<b>_聲線卡.md` 關係段 |
| indirect | `07_scene_tasks/*`（兩角色共同出場）、`08_dialogue_outputs/*`、`09_quality_assurance/*` |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-relationship
  date: YYYY-MM-DD
  skill: /iterate-relationship
  status: completed
  modified_entity: R-<a>-<b>
  modified_files:
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 03_characters/main/<a>_聲線卡.md
    - 03_characters/main/<b>_聲線卡.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [04_relationships/04_a_角色關係矩陣.md]
    depends: [04_relationships/04_b_關係變化時間線.md, 03_characters/main/<a>_聲線卡.md, 03_characters/main/<b>_聲線卡.md]
    indirect: [07_scene_tasks/CH<n>_S<m>_台詞任務包.md, 08_dialogue_outputs/<dialogue>.md]
  prereq_changed: false
  qa_recheck_recommended: [09_h]
  external_action_required: null
  abort_reason: null
  customizations: []
```

## 輸入

- `/iterate-relationship <a> <b>` 的兩個角色名。
- User 的關係變更意圖。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、影響範圍表、收斂預告稿、驗證報告。
- `04_relationships/04_a_角色關係矩陣.md`。
- `04_relationships/04_b_關係變化時間線.md`（若議題觸發 timeline event）。
- 兩端 `03_characters/<...>_聲線卡.md` 的「關係段」section-level merge。
- `.protocol_version.phase_log`。

不寫 `00_protocol/`、非兩端角色聲線卡其他 section、`05_plot/`、`06_scene_index/`、`07/08/09`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section。本 skill 不在 D-053 例外範圍；不可寫 `00_b` 任何段。若 user 跑本 skill 時需要對 `00_b` 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `04_relationships/04_a_角色關係矩陣.md`
- `04_relationships/04_b_關係變化時間線.md`（若 timeline event 需要）
- `03_characters/<a>_聲線卡.md` 與 `03_characters/<b>_聲線卡.md` 的「關係段」merge
- `.protocol_version.phase_log`（runtime tracking）

03_characters 關係段 merge 是 `R-<a>-<b>` scope 的合法跨檔寫入；不得改整張聲線卡。

## 錯誤處理 / Rollback

若任一角色不存在、關係不存在但 user 未切換到 `/create-relationship`、目標 section 找不到、LOCKED 未授權、或 pipeline 互鎖未解，停止不寫。階段 4 任一步失敗時還原已寫檔案，不更新 completed phase_log；必要時標 aborted。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。對 section-level merge 錯誤，Where 必須指到具體角色檔與 section 名稱；階段 4 前錯誤不落地 completed phase_log。
