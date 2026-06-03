---
name: iterate-org
description: "Iterate one concrete ORG-<name> organization entity through the 00_j v0.2 five-stage iteration protocol and 00_n organization context. Loads 00_n_organization issue guidance from issue_type_registry (7 issues → ORG card 7 sections), requires impact backtrace across relationships, plot, scenes, and dependents before writes, updates only the target ORG card in 11_organizations/ plus phase_log, never builds a voice card, never feeds the ORG into /dialogue-write, and does not write 00_protocol/ or 00_b."
---

狀態：DRAFT
版本：v0.2（F8 Phase 3 / D-074 amendment — 對齊 00_n v0.2：issue-ful（載 00_n_organization issue guidance）+ ORG card 6→7 段（加組織結構/層級）；本檔 v0.1 → v0.2）
歷史紀錄：v0.1（F8 Phase 3 3a — D-074 拍板；clone iterate-character、ORG scope、issue-less、無聲線卡）
最後更新：2026-06-03
適用範圍：/iterate-org skill runtime instructions
優先級：高

# /iterate-org

## 用途

`/iterate-org` 用於迭代單一 `ORG-<name>` 組織卡，包含組織本質、對抗性質、組織結構/層級、殘留型態、影響範圍、下游 hooks、文件語體 hint 7 段的調整。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2 與 `00_protocol/00_n_組織創建協議.md` v0.2（issue-ful，載 `00_n_organization` issue guidance）。ORG 變更可能影響關係矩陣、主線 / 章節 / 場景對該 ORG 的 `depends_on`、下游 hooks。本 skill 不寫 `00_b`、不建聲線卡。

**核心不變量：** ORG-* 永無聲線卡、不進 `/dialogue-write` 為說話者；§7 文件語體只留 hint，方向 B 才正式做。

## 觸發語

- `/iterate-org <name>`
- 中文別名：`/迭代組織 <name>`

`<name>` 是 user 指定的組織名。若缺少參數，階段 1 先要求 user 明示目標 ORG，不得猜測。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2。
- `00_protocol/00_n_組織創建協議.md` v0.2（issue-ful；7 段）。
- `_design/ARCHITECTURE.md` §5、§3.4。
- `_design/DECISIONS_LOG.md` §6.25 D-074、§6.23.2 D-071、§6.12 D-050。
- `<instance_root>/issue_type_registry.yaml` 的 `00_n_organization` key；若缺漏，讀 `_design/registries/issue_type_registry.template.yaml` 作 fallback 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。
- `entity_type_registry.yaml`（ORG core 型別權威）。

> **issue-ful（D-074 amendment）：** 本 skill **載** `<instance_root>/issue_type_registry.yaml`（Instance-first，缺則 template fallback）的 `00_n_organization` issue guidance（比照 `/iterate-character` 載 `00_f_character`），用於識別 7 段對應議題的 required_level / 缺漏處理。

> **00_j 適用範圍說明（對齊 ARCH §3.4 / Step 2 稽核 m4）：** `00_j` v0.2 為 **type-agnostic 五階段迭代基底協議**；其 §適用範圍 / §17 實體列舉早於 D-074、未含 ORG（D-074 刻意不動 00_j）。ORG 的迭代「scope 權威」為本 skill + `00_n` context，00_j 僅提供五階段骨架——兩者不衝突。

D-050 / D-074 寫檔邊界優先於任何較寬語境。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 `phase_log` 有 completed bootstrap。
3. `<name>` 對應 `ORG-<name>` 已存在，可定位到 `11_organizations/<name>.md`。
4. 目標 ORG card 不是 `LOCKED`；若為 `LOCKED`，停止並要求 file-specific confirmation。
5. `W-rules` 上游來源至少可讀；若缺失，提示先補世界觀或跑 `/iterate-world`。
6. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa`、`/create-relationship` 引用此 `ORG-<name>`；若有，階段 2 先拒絕並列衝突 skill。
7. `<instance_root>/issue_type_registry.yaml` 或 template registry 可讀且含 `00_n_organization` key；若不可讀 / 缺 key，拒絕進階段 2 並請 user 修補 registry。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 目標 `ORG-<name>` 與現有 card 路徑。
- 要改的段：§1 組織本質 / §2 對抗性質 / §3 組織結構/層級 / §4 殘留型態 / §5 影響範圍 / §6 下游 hooks / §7 文件語體 hint。
- 是否可能影響已建立的 `R-<C>-<ORG>` 關係、主線 / 章節 / 場景對該 ORG 的 `depends_on`。
- 若變更牽涉 §7 文件語體，agent 可讀 `<instance_root>/_source_materials/`（可讀不可寫）對齊殘留文件素材；讀取不擴大寫檔範圍。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做雙路反查。階段 2 結尾要求 user 選擇 scope_choice，不得直接進階段 4。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 `ORG-<name>` 與本輪結論。
- 本輪要處理的完整檔案清單（通常僅 ORG card 自身）。
- ORG card 變更摘要與 frontmatter `depends_on` 補完。
- 受影響的 `04_a`（含 `R-<C>-<ORG>` row）、`05_plot/*`、`06_*`、`07_*` 清單（**只列影響不寫**；跨檔調整改用對應 iterate skill）。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

只寫目標 ORG card（`11_organizations/<name>.md`）與 phase_log。每檔寫前重讀 LOCKED 狀態；失敗即 rollback。若 user scope 需要調整某 `R-<C>-<ORG>` 關係，改用 `/iterate-relationship <C> <ORG>`，本 skill 不代寫 `04_*`。

### 階段 5：實體驗證

驗證：

- ORG card header/frontmatter 合法。
- `.protocol_version.phase_log` 含 `phase: iterate-org`、`modified_entity: ORG-<name>`。
- 未寫 `00_protocol/`、`03_characters/`、`04_relationships/`、`05_plot/`、`07/08/09`。
- 印下一步建議：若影響範圍變動且已有 `R-<C>-<ORG>`，建議跑 `/iterate-relationship`；若需重看本 ORG，目前直接讀 `11_organizations/<name>.md`（view-world ORG compose / 獨立 view-org 為後續批，D-074 §13 Q5 決策佇列；勿指引跑 /view-world 看 ORG）。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 repo Markdown frontmatter。
2. direct：`entities` 含 `ORG-<name>` 的 card。
3. depends：`depends_on` 含 `ORG-<name>` 的檔案（`04_a` 關係 row、`05_plot/*`、`06_*`、`07_*`）。
4. indirect：從 direct 的其他 entities 擴張，找相關 `R-<C>-<ORG>`、`P`、`CH-*`、`S-*-*`。
5. 若 frontmatter 不完整，用檔名 / 組織名補漏，但必須提示補 `depends_on`。
6. 對所有候選檔標記 LOCKED / FINAL / 下游 pipeline 狀態。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `11_organizations/<name>.md` |
| depends | `04_relationships/04_a_角色關係矩陣.md`（含 `R-<C>-<ORG>` row）、`05_plot/*`（`depends_on:[ORG-<name>]`）、`06_scene_index/*`、`07_scene_tasks/*` |
| indirect | 相關 `R-<C>-<ORG>`、`_source_materials/`（殘留文件，可讀不可寫） |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-org
  date: YYYY-MM-DD
  skill: /iterate-org
  status: completed
  modified_entity: ORG-<name>
  modified_files:
    - 11_organizations/<name>.md
  scope_choice: 1
  affected_files_evaluated:
    direct: [11_organizations/<name>.md]
    depends: [04_relationships/04_a_角色關係矩陣.md]
    indirect: []
  prereq_changed: false
  external_action_required: null
  abort_reason: null
```

## 輸入

- `/iterate-org <name>` 的組織名。
- User 的 ORG 變更意圖。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、影響範圍表、收斂預告稿、驗證報告。
- `11_organizations/<name>.md`。
- 必要時補目標 card frontmatter `depends_on`。
- `.protocol_version.phase_log`。

不寫 `00_protocol/`、`03_characters/`、`04_relationships/`、`05_plot/`、`06_scene_index/`、`07_scene_tasks/`、`08_dialogue_outputs/`、`09_quality_assurance/`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。唯一例外是 `/init-project` + `/create-world`（D-053）；本 skill 不在例外範圍。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `11_organizations/<name>.md`
- `.protocol_version.phase_log`（runtime tracking）

不含 `03_characters/`（ORG 無聲線卡）、`04_relationships/`、`00_protocol/`。

## 錯誤處理 / Rollback

若目標 ORG 不存在、目標檔 `LOCKED`、`issue_type_registry`（含 fallback template）不可讀或缺 `00_n_organization` key、或 pipeline 互鎖未解，停止且不寫檔。若階段 4 寫入失敗，還原已寫的 card 內容，不更新 completed phase_log；必要時標 `status: aborted` 與 `abort_reason`。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。多錯誤時先列 blocking error，再列 warning。階段 4 前錯誤不落地 completed phase_log；階段 4 後錯誤只能標 aborted 或請 user 決定修復。
