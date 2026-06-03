---
name: iterate-world
description: "Iterate W-rules, V, and W-language worldbuilding entities through the 00_j v0.2 five-stage iteration protocol. Loads 00_e_world issue guidance, requires impact backtrace before writes, updates only world/vocabulary files plus phase_log, and strictly records that D-053 does not allow this skill to write 00_b."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-world skill runtime instructions
優先級：高

# /iterate-world

## 用途

`/iterate-world` 用於迭代既有世界觀、詞彙、世界語言規則實體，涵蓋 `W-rules`、`V`、`W-language` 任一或多個目標。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2 的 5 階段流程與 `00_protocol/00_e_世界觀創建協議.md` v0.1；世界觀變更常會 cascade 到角色、關係、大綱、細綱與已產出台詞，因此必須先做影響範圍評估。本 skill 不寫 `00_b`。

## 觸發語

- `/iterate-world`
- 中文別名：`/迭代世界觀`

此指令不接固定參數；變更目標在階段 1 由 chat 對話確認，並明示是 `W-rules`、`V`、`W-language` 或多個目標。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2：共通 5 階段、影響範圍評估、phase_log 規範。
- `00_protocol/00_e_世界觀創建協議.md` v0.1：世界觀實體內容語境。
- `_design/ARCHITECTURE.md` v1.6 §5、§6.7：影響範圍反查與 5 階段骨架。
- `_design/SPEC.md` v1.2 §5.2、§11：frontmatter canonical schema 與影響範圍評估。
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050、§6.16 D-053、§6.17 D-054。
- `<instance_root>/issue_type_registry.yaml` 的 `00_e_world` key；若 Instance registry 不存在，讀 `_design/registries/issue_type_registry.template.yaml` 作 fallback 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。

若 chat 指示與上述文件衝突，採更嚴格的寫檔邊界；D-050/D-053 優先於 broader protocol examples。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在；若存在，停止並說明此目錄仍標記為 Template repo，不得執行 runtime iteration。
2. `.protocol_version` 存在，且 `phase_log` 內有 `phase: bootstrap` / `status: completed`。
3. 目標實體存在：`W-rules`、`V` 或 `W-language` 可在 `01_world/` 或 `02_vocabulary/` 來源 frontmatter / 內容中定位。
4. 目標檔案狀態不是 `LOCKED`；若為 `LOCKED`，停止並要求 file-specific confirmation，不得直接寫。
5. 下游 pipeline 互鎖：依 `00_k` §10.7.5 檢查 `.protocol_version.phase_log` 是否有進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用相關 `W-rules` / `V` / `W-language`；若有，階段 2 必須拒絕並列出衝突 skill，等待 user 拍板等待完成、中止下游、或強制迭代。
6. `issue_type_registry.yaml` 或 template registry 可讀，且含 `00_e_world` key。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。要求 user 明示：

- 要改的 entity：`W-rules`、`V`、`W-language` 或多個。
- 具體變更點：世界規則、類型語氣、命名規則、禁用詞、俗稱黑話、陣營階級語言等。
- 變更理由與預期效果。
- 目標 entity 當前狀態與是否涉及 `00_b §1/§2` 影響範圍。

階段 1 結尾預告階段 2 會強制做影響範圍評估，不得跳過。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 執行雙路反查，並列 direct / depends / indirect。呈現 4 個處理範圍選項：

1. 只改 direct。
2. direct + depends。
3. direct + depends + indirect。
4. user 自訂檔案清單。

若 `02_c_禁用詞與慎用詞表.md` 或句型規則變動，且已有台詞或 QA，標出建議重跑 `/qa` 09_c。若影響進行中的下游 pipeline，先處理互鎖，等 user 拍板才進階段 3。

### 階段 3：收斂

整合階段 1/2，產出 chat-only 收斂預告稿，至少包含：

- 變更目標 entity 與最終結論一句話。
- 本輪要處理的完整檔案清單。
- 每檔的預期修改摘要與 frontmatter `depends_on` 補完計畫。
- 影響範圍預告與 `qa_recheck_recommended`。
- `00_b` 若受影響，列為 external action，不列入寫檔清單。

必須等 user 明確說「通過」、「OK」或「寫檔」才進階段 4。

### 階段 4：執行

只寫階段 3 通過的檔案。寫檔順序：`01_world/` 主分拆檔 → `02_vocabulary/` 衍生分拆檔 → `.protocol_version.phase_log`。每檔寫前重讀 header 與 LOCKED 狀態；任一步出錯，依 rollback 規則還原已寫變更，不更新 completed phase_log。

### 階段 5：實體驗證

驗證：

- 目標 world/vocabulary 檔 header 與 frontmatter 合法。
- 寫入檔案都在 D-050 允許範圍內。
- `.protocol_version.phase_log` 含 `phase: iterate-world`、`skill: /iterate-world`、`status: completed`。
- 若 `02_c` 變動，印下一步建議：重跑 `/qa` 09_c；若需重新看視圖，跑 `/view-world` 或 `/export-world`。

不得自動 trigger 下一個 skill、不得自動升 entity 狀態、不得重生 view。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析所有可讀 Markdown frontmatter，取得 `entities`、`depends_on`、`weight`。
2. direct：找出 `entities` 含 modified entity 的檔案。
3. depends：找出 `depends_on` 含 modified entity 的檔案。
4. indirect：從 direct 檔案中的其他 entities 擴張，反查那些 secondary entities 的 direct/depends 檔。
5. 若 `depends_on` 反查空但內容或檔名明顯引用目標 entity，列為 indirect 並提示補 frontmatter。
6. 對 direct / depends / indirect 分別標出 `LOCKED`、`FINAL`、下游 pipeline 是否進行中、是否建議 QA 重跑。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `01_world/01_a_世界觀總覽.md` |
| depends | `01_world/01_b_世界語言規格.md`、`01_world/01_c_陣營與階級語言.md`、`02_vocabulary/02_a_專有名詞表.md`、`02_vocabulary/02_b_俗稱與黑話表.md`、`02_vocabulary/02_c_禁用詞與慎用詞表.md`、`03_characters/*_聲線卡.md`、可能的 `04_relationships/04_a_角色關係矩陣.md` |
| indirect | `05_plot/05_a_主線大綱模板.md`、`05_plot/05_b_章節結構模板.md`、`06_scene_index/06_a_場景索引模板.md`、`00_b §1/§2`（只列影響，不寫） |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-world
  date: YYYY-MM-DD
  skill: /iterate-world
  status: completed
  modified_entity: W-rules
  modified_files:
    - 01_world/01_a_世界觀總覽.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [01_world/01_a_世界觀總覽.md]
    depends: [01_world/01_b_世界語言規格.md, 02_vocabulary/02_c_禁用詞與慎用詞表.md]
    indirect: [05_plot/05_a_主線大綱模板.md, 06_scene_index/06_a_場景索引模板.md]
  prereq_changed: false
  qa_recheck_recommended: [09_c]
  external_action_required: null
  abort_reason: null
  customizations: []
```

若變更涉及 `00_b §1/§2`，不寫 `00_b`，改填 `external_action_required: "00_b §1/§2 manual patch or new D-NNN decision"`。

## 輸入

- User 的世界觀迭代意圖，可由 chat 描述。
- 可選：指定 entity 類型 `W-rules` / `V` / `W-language`。
- 可選：user 對階段 2 scope_choice 的拍板。
- 階段 3 後的明確「通過 / OK / 寫檔」。

## 輸出

允許輸出：

- chat 中的階段 1 診斷、階段 2 影響範圍表、階段 3 收斂預告稿、階段 5 驗證報告。
- D-050 允許範圍內的 `01_world/`、`02_vocabulary/` 來源檔更新。
- 必要時補完來源檔 frontmatter `depends_on`。
- `.protocol_version.phase_log` runtime tracking entry。

不得輸出或修改 `00_protocol/`、registry、parser、frontend、既有 skill、view 整合檔。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section（類型語氣 / 髒話尺度）。本 skill 不在 D-053 例外範圍；不可寫 `00_b` 任何段。若 user 跑本 skill 時需要同步調整 `00_b §1/§2`，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 00_b §1/§2 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `01_world/01_a_世界觀總覽.md`
- `01_world/01_b_世界語言規格.md`
- `01_world/01_c_陣營與階級語言.md`
- `02_vocabulary/02_a_專有名詞表.md`
- `02_vocabulary/02_b_俗稱與黑話表.md`
- `02_vocabulary/02_c_禁用詞與慎用詞表.md`
- `.protocol_version.phase_log`（runtime tracking）

不含 `00_protocol/00_b_反ai味檢查表.md`；/iterate-* 全部不寫 `00_b`。

## 錯誤處理 / Rollback

若 prerequisites 在階段 1 前失敗，寫入 0 檔且不更新 phase_log。若階段 4 任一步失敗，還原本輪已寫檔案到階段 4 前狀態；若無法完整還原，停止並明列需要 user 手動檢查的檔案。任何未完成執行不得寫 `status: completed` phase_log，可保留或補 `status: aborted` 與 `abort_reason`。

## 錯誤呈現規則

錯誤訊息必須包含：

- What：發生什麼事。
- Where：檔案、entity、階段。
- Why：違反哪個 prerequisite、LOCKED、D-050/D-053、pipeline lock、或資料缺漏。
- 下一步：user 可選等待、補檔、解除 LOCKED、重跑階段、縮小 scope、或開新 D-NNN。

若錯誤發生於階段 4 前，不落地 phase_log completed entry；若階段 4 已開始，phase_log 只能標 aborted 或保留待 user 決定。
