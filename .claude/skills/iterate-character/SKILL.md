---
name: iterate-character
description: "Iterate one concrete C-name character voice-card entity through the 00_j v0.2 five-stage iteration protocol and 00_f character context. Loads 00_f_character issue guidance, requires impact backtrace across relationships, arcs, scenes, dialogue, and QA before writes, updates only the target voice-card scope plus phase_log, and records that D-053 does not allow 00_b writes."
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：/iterate-character skill runtime instructions
優先級：高

# /iterate-character

## 用途

`/iterate-character` 用於迭代單一 `C-<name>` 角色聲線卡，包含聲線、禁用語氣、行動傾向、弧線階段與已建立關係段的調整。此 skill 對齊 `00_protocol/00_j_迭代協議.md` v0.2 與 `00_protocol/00_f_角色創建協議.md` v0.2；角色變更會影響關係矩陣、關係時間線、出場場景、台詞與 QA。本 skill 不寫 `00_b`。

## 觸發語

- `/iterate-character <name>`
- 中文別名：`/迭代角色 <name>`

`<name>` 是 user 指定的角色名。若缺少參數，階段 1 先要求 user 明示目標角色，不得猜測。

## 觸發協議

必讀並遵守：

- `00_protocol/00_j_迭代協議.md` v0.2。
- `00_protocol/00_f_角色創建協議.md` v0.2。
- `_design/ARCHITECTURE.md` v1.6 §5、§6.7。
- `_design/SPEC.md` v1.2 §5.2、§11。
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050、§6.16 D-053。
- `<instance_root>/issue_type_registry.yaml` 的 `00_f_character` key；若缺漏，讀 `_design/registries/issue_type_registry.template.yaml` 作 fallback 並印 `WARN`。同時讀 `user_extensions` 與 `core_overrides`。

D-050/D-053 寫檔邊界優先於 `00_f` 內較寬的歷史語境。

## 啟動前檢查

進階段 1 前必須確認：

1. `.template_root` 不存在。
2. `.protocol_version` 存在，且 `phase_log` 有 completed bootstrap。
3. `<name>` 對應 `C-<name>` 已存在，且可定位到主要、次要或 NPC 聲線卡。
4. 目標聲線卡不是 `LOCKED`；若為 `LOCKED`，停止並要求 file-specific confirmation。
5. W-rules / V / W-language 上游來源至少可讀；若缺失，提示先補世界觀或跑 `/iterate-world`。
6. `.protocol_version.phase_log` 無進行中的 `/scene-task`、`/dialogue-write`、`/qa` 引用此 `C-<name>`；若有，階段 2 先拒絕並列衝突 skill。
7. `issue_type_registry.yaml` 或 template registry 可讀且含 `00_f_character`。

## 流程

### 階段 1：變更點識別

只做診斷，不寫檔。確認：

- 目標 `C-<name>` 與現有聲線卡路徑。
- 要改的欄位：聲線、句型、禁用詞、稱呼、行動傾向、角色弧線、與某角色的關係段，以及聲線卡固定段 `§A 個性拆解` / `§B 既有劇本台詞聲線基準` / `§C 既有劇本聲線使用規則` / `§D Source Coverage / 下游 Hooks`（Wave2 D-065/D-066 落地）等。
- 是否可能影響已產出台詞或 QA。
- 若變更牽涉 §B/§C 既有劇本聲線基準，agent 可讀 `<instance_root>/_source_materials/dialogue/` 與既有 `08_dialogue_outputs/`（**可讀不可寫**；D-065 D-050 讀邊界 clarification）對齊既有劇本台詞；讀取不擴大寫檔範圍。
- 是否牽涉 `00_b §3` 作品風格規範；若牽涉，只列影響不寫。

### 階段 2：強制影響範圍評估

依本檔 `## 影響範圍評估規範` 做雙路反查。聲線描述變動時，若已有 `/dialogue-write` 或 `/qa` 進行中或已產出，必須標示 09_b 聲線一致性重跑建議。階段 2 結尾要求 user 選擇 scope_choice，不得直接進階段 4。

### 階段 3：收斂

印 chat-only 收斂預告稿：

- 目標 `C-<name>` 與本輪結論。
- 本輪要處理的完整檔案清單。
- 聲線卡變更摘要與 frontmatter `depends_on` 補完。
- 受影響的 `04_a`、`04_b`、`05_c`、`07/08/09` 清單。
- 若 `00_b §3` 需同步調整，列為 external action，不列入寫檔。

等 user 明確「通過 / OK / 寫檔」才進階段 4。

### 階段 4：執行

只寫目標聲線卡與 phase_log。聲線卡寫檔 scope 納入固定段 `§A` / `§B` / `§C` / `§D`（與 /create-character 輸出骨架一致；維持 `§A → §B → §C → §D` 順序）；§B/§C 更新只能寫進目標聲線卡，永不寫 `08_dialogue_outputs/`。若 user scope 需要調整關係段，僅允許在目標角色聲線卡內更新該角色相關 section；跨角色雙邊關係應改用 `/iterate-relationship <a> <b>`。每檔寫前重讀 LOCKED 狀態；失敗即 rollback。

### 階段 5：實體驗證

驗證：

- 聲線卡 header/frontmatter 合法。
- `.protocol_version.phase_log` 含 `phase: iterate-character`、`modified_entity: C-<name>`。
- 未寫 `00_b`、`04_relationships/`、`05_plot/`、`07/08/09`。
- 若聲線變動且已有該角色台詞，印下一步建議：重跑 `/qa` 09_b；若需重看角色，跑 `/view-character <name>` 或 `/export-character <name>`。

## 影響範圍評估規範

雙路反查 algorithm：

1. 解析 repo Markdown frontmatter。
2. direct：`entities` 含 `C-<name>` 的聲線卡。
3. depends：`depends_on` 含 `C-<name>` 的檔案。
4. indirect：從 direct 檔案的其他 entities 擴張，找相關 R-*-*、P、CH-*、S-*-*。
5. 若 frontmatter 不完整，使用檔名、角色名、關係段 anchor 作補漏，但必須提示補 `depends_on`。
6. 對所有候選檔標記 LOCKED / FINAL / 下游 pipeline 狀態。

預期清單：

| 類型 | 預期檔案 |
|---|---|
| direct | `03_characters/main/<name>_聲線卡.md` 或 `03_characters/minor/<name>_聲線卡.md` 或 `03_characters/npc/<NPC類型>模板.md` |
| depends | `04_relationships/04_a_角色關係矩陣.md`（含 `C-<name>` row）、`04_relationships/04_b_關係變化時間線.md`（含 `C-<name>` event）、`05_plot/05_c_角色弧線表.md`、`07_scene_tasks/*`（含 `C-<name>` 出場場景） |
| indirect | `08_dialogue_outputs/*`（已產出台詞；§B/§C 對齊時**可讀不可寫**，D-065 讀邊界）、`_source_materials/dialogue/*`（既有劇本 source，可讀不可寫）、`09_quality_assurance/*`（已產出 QA 報告）、可能的 `00_b §3`（只列影響，不寫） |

## .protocol_version 寫入規範

階段 4 成功後 append：

```yaml
- phase: iterate-character
  date: YYYY-MM-DD
  skill: /iterate-character
  status: completed
  modified_entity: C-<name>
  modified_files:
    - 03_characters/main/<name>_聲線卡.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [03_characters/main/<name>_聲線卡.md]
    depends: [04_relationships/04_a_角色關係矩陣.md, 05_plot/05_c_角色弧線表.md]
    indirect: [08_dialogue_outputs/<dialogue>.md, 09_quality_assurance/<qa>.md]
  prereq_changed: false
  qa_recheck_recommended: [09_b]
  external_action_required: null
  abort_reason: null
  customizations: []
```

若需 `00_b §3` manual patch，填入 `external_action_required`。

## 輸入

- `/iterate-character <name>` 的角色名。
- User 的角色變更意圖。
- 階段 2 scope_choice。
- 階段 3 後明確 approval。

## 輸出

允許輸出：

- chat 診斷、影響範圍表、收斂預告稿、驗證報告。
- `03_characters/main/<name>_聲線卡.md`、`03_characters/minor/<name>_聲線卡.md` 或 `03_characters/npc/<NPC類型>模板.md`。
- 必要時補目標聲線卡 frontmatter `depends_on`。
- `.protocol_version.phase_log`。

不寫 `00_protocol/`、`04_relationships/`、`05_plot/`、`07_scene_tasks/`、`08_dialogue_outputs/`、`09_quality_assurance/`、registry、parser、frontend、既有 skill。

## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 `00_b`）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1：`/create-world` 可寫 `00_b §1/§2` Instance-specific section。本 skill不在 D-053 例外範圍；不可寫 `00_b` 任何段（含 §3）。若 user 跑本 skill 時需要對 `00_b §3` 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 00_b §3 或開新 D-NNN 拍板擴大 D-053 例外」，並列入 phase_log 的 `external_action_required`。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：

- `03_characters/main/<name>_聲線卡.md`（主要角色）
- `03_characters/minor/<name>_聲線卡.md`（次要角色）
- `03_characters/npc/<NPC類型>模板.md`（NPC）
- `.protocol_version.phase_log`（runtime tracking）

不含 `00_protocol/00_b_反ai味檢查表.md`。

## 錯誤處理 / Rollback

若目標角色不存在、registry 不可讀、目標檔 `LOCKED`、或 pipeline 互鎖未解，停止且不寫檔。若階段 4 寫入失敗，還原已寫的聲線卡內容，不更新 completed phase_log；必要時標 `status: aborted` 與 `abort_reason`。

## 錯誤呈現規則

錯誤訊息必須包含 What / Where / Why / 下一步。多錯誤時先列 blocking error，再列 warning。階段 4 前錯誤不落地 completed phase_log；階段 4 後錯誤只能標 aborted 或請 user 決定修復。
