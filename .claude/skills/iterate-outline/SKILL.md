---
name: iterate-outline
description: "Iterate the project-level P outline entity through the 00_j v0.2 five-stage iteration protocol and 00_g outline context. Loads 00_g_outline issue guidance, requires impact backtrace across chapters, arcs, information reveal, foreshadowing, scene index, dialogue, and QA before writes, updates only D-050 outline files plus phase_log, and does not write 00_b."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-outline skill runtime instructions
優先級：高

# /iterate-outline

## 用途

`/iterate-outline` 用於迭代單一專案大綱實體 `P`，包含主線、角色弧線、資訊揭露與伏筆回收等上層結構。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2 與 `00_protocol/00_g_大綱創建協議.md` v0.2；主線變動影響極廣，會波及 CH-*、S-*-*、任務包、台詞與 QA。本 skill 不寫 `05_b` 章節結構、不寫 CH/S 詳細內容、不寫 `00_b`。

## 觸發語

- `/iterate-outline`
- 中文別名：`/迭代大綱`

此指令不接固定參數；變更段落在階段 1 由 chat 確認。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2。
- `00_protocol/00_g_大綱創建協議.md` v0.2。
- `_design/ARCHITECTURE.md` v1.6 §5、§6.7。
- `_design/SPEC.md` v1.2 §5.2、§11。
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050、§6.16 D-053。
- `<instance_root>/issue_type_registry.yaml` 的 `00_g_outline` key；缺漏時 fallback 讀 `_design/registries/issue_type_registry.template.yaml` 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 bootstrap completed。
3. `P` 已存在，可在 `05_plot/05_a_主線大綱模板.md` 或相關 `05_c/05_d/05_e` 來源定位。
4. 目標 `05_a`、`05_c`、`05_d`、`05_e` 不是 `LOCKED`。
5. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用受影響 `P` / `CH-*` / `S-*-*`；若有，階段 2 先拒絕並列衝突 skill。
6. registry 可讀且含 `00_g_outline`。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 要改的主線段落、章節弧線、資訊揭露、伏筆或角色弧線。
- 變更是否要求調整 `05_b` 章節結構或 `06_a` 場景索引；若是，先列為影響範圍，告知實際寫入屬 `/iterate-detailed-outline`。
- 是否影響已產出台詞或 QA。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做雙路反查。主線改動影響範圍通常很廣，必須分 direct / depends / indirect 呈現，並建議 user 分批處理。若已產出台詞，提示可能需重跑全 8 份 `/qa`。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 `P` 與本輪結論。
- 本輪要寫的 `05_a/05_c/05_d/05_e` 檔案清單。
- 不寫但受影響的 `05_b`、`06_a`、`07/08/09` 清單。
- 建議後續是否跑 `/iterate-detailed-outline`。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

寫檔順序：`05_a` → `05_c` → `05_d` → `05_e` → `.protocol_version.phase_log`。只寫階段 3 通過且在 D-050 表內的檔案。不得寫 `05_b`、`06_a` 或場景詳細內容；那些只列入 affected files。

### 階段 5：實體驗證

驗證：

- `05_a/05_c/05_d/05_e` header/frontmatter 合法。
- `.protocol_version.phase_log` 含 `phase: iterate-outline`。
- 未寫 `05_b`、`06_a`、`00_b`。
- 下一步建議：重看大綱可跑 `/view-outline` 或 `/export-outline`；若主線 / 弧線變動需 propagate 到細綱，跑 `/iterate-detailed-outline`。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 Markdown frontmatter。
2. direct：`entities` 含 `P` 的 `05_a/05_c/05_d/05_e`。
3. depends：`depends_on` 含 `P` 的 CH/S/scene/task/dialogue/QA 檔。
4. indirect：從受影響 CH-*、C-*、S-*-* 擴張到對應檔。
5. 若 frontmatter 不完整，以章節 ID、場景 ID、伏筆/揭露 anchor 補漏並提示補 `depends_on`。
6. 標記 LOCKED / FINAL / pipeline lock / QA 重跑建議。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `05_plot/05_a_主線大綱模板.md`、`05_plot/05_c_角色弧線表.md`、`05_plot/05_d_資訊揭露表.md`、`05_plot/05_e_伏筆與回收表.md` |
| depends | `05_plot/05_b_章節結構模板.md`（本 skill 不寫）、`06_scene_index/06_a_場景索引模板.md`、受弧線影響的 `03_characters/*_聲線卡.md` |
| indirect | `07_scene_tasks/*`、`08_dialogue_outputs/*`、`09_quality_assurance/*` |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-outline
  date: YYYY-MM-DD
  skill: /iterate-outline
  status: completed
  modified_entity: P
  modified_files:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_c_角色弧線表.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [05_plot/05_a_主線大綱模板.md, 05_plot/05_c_角色弧線表.md]
    depends: [05_plot/05_b_章節結構模板.md, 06_scene_index/06_a_場景索引模板.md]
    indirect: [07_scene_tasks/CH<n>_S<m>_台詞任務包.md, 08_dialogue_outputs/<dialogue>.md]
  prereq_changed: false
  qa_recheck_recommended: []
  external_action_required: null
  abort_reason: null
  customizations: []
```

若 `05_b` 或 `06_a` 必須跟進，將其列在 affected_files_evaluated，並在 Stage 5 建議 `/iterate-detailed-outline`。

## 輸入

- User 的主線 / 大綱迭代意圖。
- 可選：指定主線、角色弧線、資訊揭露、伏筆段落。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、影響範圍表、收斂預告稿、驗證報告。
- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_c_角色弧線表.md`
- `05_plot/05_d_資訊揭露表.md`
- `05_plot/05_e_伏筆與回收表.md`
- `.protocol_version.phase_log`

不寫 `05_b`、`06_scene_index/`、`00_protocol/`、`07/08/09`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section。本 skill 不在 D-053 例外範圍；不可寫 `00_b` 任何段。若 user 跑本 skill 時需要對 `00_b` 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_c_角色弧線表.md`（若弧線議題觸發）
- `05_plot/05_d_資訊揭露表.md`（若資訊揭露議題觸發）
- `05_plot/05_e_伏筆與回收表.md`（若伏筆議題觸發）
- `.protocol_version.phase_log`（runtime tracking）

本 skill 不寫 `05_plot/05_b_章節結構模板.md`、CH-*、S-*-* 或 `06_scene_index/06_a_場景索引模板.md`；那些屬 `/iterate-detailed-outline` scope。

## 錯誤處理 / Rollback

若 `P` 不存在、目標檔 LOCKED、registry 缺漏、或 pipeline 互鎖未解，停止不寫。階段 4 任一步失敗時，還原已寫 `05_plot` 檔，不更新 completed phase_log；必要時標 aborted。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。若 user 要求本 skill 寫 `05_b` 或 `06_a`，拒絕並提示改用 `/iterate-detailed-outline`。
