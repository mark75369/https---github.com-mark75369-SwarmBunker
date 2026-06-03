---
name: iterate-scene
description: "Iterate one concrete S-ch-n scene-index entity through the 00_j v0.2 five-stage iteration protocol and D-054 NEW_REQ_15 hybrid scene-file support. Handles normal S-row or existing per-scene content edits, and with --split-to-file creates one upstream/static per-scene scene-index file plus a 06_a split marker. It does not load issue registry guidance and does not write 00_b."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-scene skill runtime instructions
優先級：高

# /iterate-scene

## 用途

`/iterate-scene` 用於迭代單一 `S-<ch>-<n>` 場景索引實體，並落地 D-054 NEW_REQ_15：`/iterate-scene <S-ID> --split-to-file` 可把 aggregate `06_a` 中的單場拆成 `06_scene_index/CH<n>_S<m>_<scene_name>.md` per-scene 檔，同時在原 row 加 split marker 並保留 fallback 兼容。不帶 flag 時，作為單場 S-*-* 內容迭代，寫 aggregate row 或既有 per-scene 檔。

## 觸發語

- `/iterate-scene <S-ID>`
- `/iterate-scene <S-ID> --split-to-file`

本 skill 無中文 wrapper。`<S-ID>` 必須是具體場景 ID，例如 `S-01-02`。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2 §10.7。
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054。
- `_design/D054_DECISION_PACKAGE.md` v0.2 §2.1。
- `_design/POST_LOCK_PENDING.md` NEW_REQ_15 trigger A/B/C/D。
- `_design/SPEC.md` v1.2 §5.2：per-scene 檔屬上游/靜態檔，只用 `entities` / `depends_on` / `weight` 三欄。
- `.claude/skills/scene-task/SKILL.md` v0.1、`.claude/skills/view-detailed-outline/SKILL.md` v0.1、`.claude/skills/export-detailed-outline/SKILL.md` v0.1 的 D-054 fallback pattern。

議題清單動態載入不適用；split-to-file 是 file organization 操作，不讀 issue registry。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 bootstrap completed。
3. `<S-ID>` 是具體 `S-<ch>-<n>`，不是 wildcard。
4. 對應 `CH-*` 存在於 `05_plot/05_b_章節結構模板.md` 或相關 scene index。
5. 目標 S-ID 存在：per-scene 檔存在，或 aggregate `06_a` 有對應 row。
6. 目標 `06_a` row 或 per-scene 檔不是 `LOCKED`。
7. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用此 S-ID；若有，階段 2 先拒絕並列衝突 skill。
8. `--split-to-file` 子模式額外檢查：對應 per-scene 檔尚未存在，避免重複拆檔。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 目標 S-ID 與目前來源：per-scene 或 aggregate。
- 模式：內容迭代，或 `--split-to-file`。
- 若 `--split-to-file`：確認 scene_name、目標檔名、原 row 是否可完整抽取。
- 若內容迭代：確認要改的場景功能、開始/結束狀態、出場角色、資訊揭露、risk_type 等。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做雙路反查。split-to-file 子模式仍須列出引用此 S-ID 的 `07_scene_tasks`、`08_dialogue_outputs`、`09_quality_assurance`，讓 user 拍板是否需要更新引用或只保留 D-054 fallback。不得因為是 file organization 就跳過階段 2。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 S-ID 與模式。
- 本輪要寫的檔案清單。
- `--split-to-file` 時列出：新 per-scene path、原 `06_a` row marker、frontmatter 三欄。
- 影響範圍與是否建議 QA 重跑。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

內容迭代模式：

1. 若 per-scene 檔存在，更新 per-scene 檔。
2. 否則更新 `06_scene_index/06_a_場景索引模板.md` 對應 row。
3. append `.protocol_version.phase_log`。

`--split-to-file` 子模式：

1. 寫新 per-scene 檔，包含完整 row 內容與上游/靜態檔三欄 frontmatter：`entities`、`depends_on`、`weight`。
2. 在原 `06_a` row 加 `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->` marker；不刪除 row。
3. append `.protocol_version.phase_log`，標 `split_to_file: true`。
4. 任一步失敗 rollback：刪除新 per-scene 檔，還原 `06_a` marker。

### 階段 5：實體驗證

驗證：

- S-ID 完成度不因 split-to-file 改變。
- per-scene 檔 frontmatter 只含上游/靜態檔三欄，不擴充 07/08/09 pipeline 專屬欄位。
- `06_a` row 保留且 marker 正確。
- `.protocol_version.phase_log` 含 `phase: iterate-scene`，若 split 則 `split_to_file: true`。
- 下一步建議：下次 `/scene-task <S-ID>` 會自動 detect per-scene 檔優先；若連續 >= 5 次拆檔，通知 master 啟動 per-scene supersede 評估（議題號原預留為 D-055；依 DECISIONS_LOG §6.18.2 順延至 D-056 或當時最近未用編號）。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 Markdown frontmatter。
2. direct：`entities` 含目標 S-ID 的 `06_a` 或 per-scene 檔。
3. depends：`depends_on` 含目標 S-ID 的 `07_scene_tasks`、`08_dialogue_outputs`、`09_quality_assurance`。
4. indirect：split-to-file 子模式通常無；若內容變更牽涉 C-* / R-*-* / P / CH-*，擴張反查那些 entities。
5. D-054 lookup：先查 `06_scene_index/CH<n>_S<m>_*.md`；不存在則查 `06_scene_index/06_a_場景索引模板.md` row；兩者皆無則拒絕。
6. 標記 LOCKED / FINAL / pipeline lock / QA 重跑建議。

split-to-file 子模式預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `06_scene_index/06_a_場景索引模板.md` 對應 row |
| depends | `07_scene_tasks/CH<n>_S<m>_*`、`08_dialogue_outputs/*`、`09_quality_assurance/*` |
| indirect | 通常無；split-to-file 是 file organization，路徑由下游 D-054 fallback 自動 detect |

## .protocol_version 寫入規範

內容迭代模式：

```yaml
- phase: iterate-scene
  date: YYYY-MM-DD
  skill: /iterate-scene
  status: completed
  modified_entity: S-01-02
  modified_files:
    - 06_scene_index/06_a_場景索引模板.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [06_scene_index/06_a_場景索引模板.md]
    depends: [07_scene_tasks/CH01_S02_台詞任務包.md]
    indirect: []
  prereq_changed: false
  qa_recheck_recommended: []
  external_action_required: null
  abort_reason: null
  customizations: []
```

`--split-to-file` 子模式：

```yaml
- phase: iterate-scene
  date: YYYY-MM-DD
  skill: /iterate-scene
  status: completed
  modified_entity: S-01-02
  modified_files:
    - 06_scene_index/CH01_S02_<scene_name>.md
    - 06_scene_index/06_a_場景索引模板.md
  scope_choice: 1
  affected_files_evaluated:
    direct: [06_scene_index/06_a_場景索引模板.md]
    depends: [07_scene_tasks/CH01_S02_台詞任務包.md, 08_dialogue_outputs/<dialogue>.md, 09_quality_assurance/<qa>.md]
    indirect: []
  prereq_changed: false
  qa_recheck_recommended: []
  split_to_file: true
  external_action_required: null
  abort_reason: null
  customizations: []
```

## 輸入

- 必填：`<S-ID>`。
- 可選：`--split-to-file`。
- User 的單場變更意圖。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、D-054 lookup、影響範圍表、收斂預告稿、驗證報告。
- `06_scene_index/06_a_場景索引模板.md`（row 更新 / split marker）。
- `06_scene_index/CH<n>_S<m>_<scene_name>.md`（split-to-file 新建 / 既有 per-scene 檔修改）。
- `.protocol_version.phase_log`。

不寫 `00_protocol/`、`05_plot/`、`07_scene_tasks/`、`08_dialogue_outputs/`、`09_quality_assurance/`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section。本 skill 不在 D-053 例外範圍；不可寫 `00_b` 任何段。S-*-* 場景索引與 split-to-file 屬 file organization / scene-index 操作，與 `00_b` 反 AI 味基線通則無直接關聯。若 user 要同步調整 `00_b`，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `06_scene_index/06_a_場景索引模板.md`
- `06_scene_index/CH<n>_S<m>_<scene_name>.md`（split-to-file 新建 / 既有 per-scene 檔修改）
- `.protocol_version.phase_log`（runtime tracking）

per-scene 檔 frontmatter 只用 SPEC §5.2 上游/靜態檔三欄：

```yaml
entities: [S-<ch>-<n>]
depends_on: [...]
weight: {S-<ch>-<n>: 1.0}
```

不得加入 07/08/09 pipeline 專屬 frontmatter 欄位：`pipeline_state`、`mode_tag`、`qa_decision`、`qa_type`、`source_task`、`source_dialogue`、`source_dialogues`、`scene_id`。

## 錯誤處理 / Rollback

若 S-ID 不存在、CH 不存在、目標 LOCKED、per-scene 檔已存在卻要求 split、或 pipeline 互鎖未解，停止不寫。split-to-file 階段 4 任一步失敗時，刪除新 per-scene 檔並還原 `06_a` marker；不更新 completed phase_log。內容迭代失敗時還原 row 或 per-scene 檔。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。split-to-file 錯誤必須明列新 per-scene path、`06_a` row marker 狀態、是否已 rollback。若連續拆檔需求達 NEW_REQ_15 trigger B，僅回報 evidence，不修改 DECISIONS_LOG、POST_LOCK_PENDING 或 D054_DECISION_PACKAGE。
