---
name: iterate-detailed-outline
description: "Iterate CH-* chapter and S-*-* scene-index detailed-outline entities through the 00_j v0.2 five-stage iteration protocol and 00_h context. Loads 00_h_detailed_outline issue guidance, applies D-054 hybrid lookup with per-scene file first and aggregate 06_a fallback, rejects split-to-file requests in favor of /iterate-scene, updates only 05_b, 06_a, existing per-scene scene files, and phase_log, and does not write 00_b."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-detailed-outline skill runtime instructions
優先級：高

# /iterate-detailed-outline

## 用途

`/iterate-detailed-outline` 用於迭代 CH-* 章節結構與 S-*-* 場景索引實體。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2、`00_protocol/00_h_細綱創建協議.md` v0.2，並承接 D-054 hybrid fallback：已拆 per-scene 檔優先，否則 fallback aggregate `06_a` row。若 user 要把場景拆為 per-scene 檔，必須改用 `/iterate-scene <S-ID> --split-to-file`。

## 觸發語

- `/iterate-detailed-outline`
- `/iterate-detailed-outline <CH-ID>`
- 中文別名：`/迭代細綱`

`<CH-ID>` 可選。若未提供，階段 1 由 chat 確認目標 CH-* 或 S-*-*。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2。
- `00_protocol/00_h_細綱創建協議.md` v0.2。
- `_design/ARCHITECTURE.md` v1.6 §5、§6.7。
- `_design/SPEC.md` v1.2 §5.2、§11。
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050、§6.16 D-053、§6.17 D-054。
- `_design/D054_DECISION_PACKAGE.md` v0.2。
- `.claude/skills/scene-task/SKILL.md` v0.1 的 D-054 per-scene-first / aggregate-fallback pattern。
- `<instance_root>/issue_type_registry.yaml` 的 `00_h_detailed_outline` key；缺漏時 fallback 讀 template registry 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 bootstrap completed。
3. `P` 與目標 `CH-*` / `S-*-*` 已存在；若兩者皆無，提示先跑 `/create-detailed-outline`。
4. 目標 `05_b`、`06_a` 或既有 per-scene 檔不是 `LOCKED`。
5. D-054 hybrid lookup 可定位目標：per-scene 檔存在，或 aggregate `06_a` 有對應 row。
6. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用目標 CH/S；若有，階段 2 先拒絕並列衝突 skill。
7. registry 可讀且含 `00_h_detailed_outline`。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 目標是 CH-* 章節、S-*-* 場景 row、或兩者。
- 變更內容：章節目標、節點順序、場景功能、開始/結束狀態、出場角色、資訊揭露、風險標記等。
- 是否明示 per-scene 拆檔需求；若是，拒絕本 skill 路徑並提示 `/iterate-scene <S-ID> --split-to-file`。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做雙路反查。必須執行 D-054 hybrid lookup，列出每個 S-*-* 的 source 是 per-scene、aggregate 或 missing。若 S-*-* 變動且已有台詞，建議重跑全 8 份 `/qa`。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 CH/S 與本輪結論。
- 本輪要寫的 `05_b`、`06_a` row 或既有 per-scene 檔清單。
- D-054 read_source 與 fallback 狀態。
- 受影響 `07/08/09` 清單與 QA 建議。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

寫檔順序：`05_b` CH entry → `06_a` S row 或既有 per-scene 檔 → `.protocol_version.phase_log`。如果某 S-*-* 已有 per-scene 檔，優先更新該檔；若沒有，更新 aggregate `06_a` row。不得在此 skill 新建 per-scene split 檔；新建 split 屬 `/iterate-scene --split-to-file`。

### 階段 5：實體驗證

驗證：

- `05_b`、`06_a` 或 per-scene 檔 header/frontmatter 合法。
- D-054 source mode 一致。
- `.protocol_version.phase_log` 含 `phase: iterate-detailed-outline`。
- 下一步建議：重看細綱可跑 `/view-detailed-outline` 或 `/export-detailed-outline`；若 S-*-* 變動且已有台詞，重跑全 8 份 `/qa`。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 Markdown frontmatter。
2. direct：`entities` 含目標 `CH-*` 或 `S-*-*` 的 `05_b` / `06_a` / per-scene 檔。
3. depends：`depends_on` 含目標 CH/S 的 `07_scene_tasks`、`08_dialogue_outputs`、`09_quality_assurance`。
4. indirect：從出場 C-*、R-*-*、P 擴張回場景相關檔。
5. D-054 lookup：先查 `06_scene_index/CH<n>_S<m>_*.md`，存在則讀 per-scene；不存在則 fallback `06_scene_index/06_a_場景索引模板.md` 對應 row；兩者皆無則拒絕並提示先跑 `/create-detailed-outline`。
6. 標記 LOCKED / FINAL / pipeline lock / QA 重跑建議。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `05_plot/05_b_章節結構模板.md`（CH-* entry）、`06_scene_index/06_a_場景索引模板.md`（S-*-* row）、既有 `06_scene_index/CH<n>_S<m>_<scene_name>.md` |
| depends | 已存在 per-scene `06_scene_index/CH<n>_S<m>_*.md`、`07_scene_tasks/CH<n>_S<m>_*` 任務包 |
| indirect | `08_dialogue_outputs/*`、`09_quality_assurance/*` |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-detailed-outline
  date: YYYY-MM-DD
  skill: /iterate-detailed-outline
  status: completed
  modified_entity: CH-01
  modified_files:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [05_plot/05_b_章節結構模板.md, 06_scene_index/06_a_場景索引模板.md]
    depends: [07_scene_tasks/CH01_S01_台詞任務包.md]
    indirect: [08_dialogue_outputs/<dialogue>.md, 09_quality_assurance/<qa>.md]
  prereq_changed: false
  qa_recheck_recommended: [09_a, 09_b, 09_c, 09_d, 09_f, 09_g, 09_h, 09_i]
  external_action_required: null
  abort_reason: null
  customizations: []
```

若更新既有 per-scene 檔，將該檔列入 `modified_files`。若 user 要 split-to-file，停止並不寫 phase_log completed entry。

## 輸入

- 可選 `<CH-ID>`。
- User 的 CH/S 變更意圖。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、D-054 lookup 報告、影響範圍表、收斂預告稿、驗證報告。
- `05_plot/05_b_章節結構模板.md`
- `06_scene_index/06_a_場景索引模板.md`
- 既有 `06_scene_index/CH<n>_S<m>_<scene_name>.md`（若 D-054 fallback 抓到 per-scene 檔）
- `.protocol_version.phase_log`

不新建 split-to-file per-scene 檔；不寫 `00_protocol/`、`05_a/05_c/05_d/05_e`、`07/08/09`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section。本 skill 不在 D-053 例外範圍；不可寫 `00_b` 任何段。若 user 跑本 skill 時需要對 `00_b` 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `05_plot/05_b_章節結構模板.md`
- `06_scene_index/06_a_場景索引模板.md`
- `06_scene_index/CH<n>_S<m>_<scene_name>.md`（若 D-054 hybrid fallback 抓到既有 per-scene 檔）
- `.protocol_version.phase_log`（runtime tracking）

不含 `00_protocol/00_b_反ai味檢查表.md`。per-scene 拆檔新建屬 `/iterate-scene --split-to-file`，不是本 skill。

## 錯誤處理 / Rollback

若目標 CH/S 不存在、D-054 lookup 兩種來源皆無、目標 LOCKED、或 pipeline 互鎖未解，停止不寫。若 user 在階段 1 明示 per-scene 拆檔需求，拒絕並提示 `/iterate-scene <S-ID> --split-to-file`。階段 4 任一步失敗時還原已寫檔，不更新 completed phase_log。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。D-054 missing source 錯誤必須列 per-scene candidate path 與 aggregate `06_a` row 查找結果。
