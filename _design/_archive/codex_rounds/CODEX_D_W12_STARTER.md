狀態：DRAFT  
版本：v0.1（10th master 第十輪整合對話 Wave 12 batch task starter；6 SKILL.md + 5 wrapper 一次性實作；對齊 D1-D5 + 00_j v0.2 + Phase B /create-* 既有範本；嚴守 D-050 子裁決 1+2 + D-053 紀錄 + D-054 hybrid fallback；採 9th master 第二段 Wave 14-15 batch 模式）  
最後更新：2026-05-23  
適用範圍：Phase D Wave 12 batch task — CODEX 在乾淨對話 batch 寫 6 個 /iterate-* SKILL.md + 5 個中文 wrapper（共 11 檔）  
優先級：高

# CODEX_D_W12_STARTER — Phase D Wave 12 batch task

# 0. 本檔用途

Phase D Wave 12 收尾條 task — CODEX 在乾淨對話**一次性**寫 11 檔：

| # | 路徑 | 性質 | 對應 9th master 第一段 starter |
|---|---|---|---|
| 1 | `.claude/skills/iterate-world/SKILL.md` | 英文主檔 | `_design/CODEX_D1_STARTER.md` v0.3 |
| 2 | `.claude/skills/迭代世界觀/SKILL.md` | 中文 wrapper | 同上 |
| 3 | `.claude/skills/iterate-character/SKILL.md` | 英文主檔 | `_design/CODEX_D2_STARTER.md` v0.3 |
| 4 | `.claude/skills/迭代角色/SKILL.md` | 中文 wrapper | 同上 |
| 5 | `.claude/skills/iterate-relationship/SKILL.md` | 英文主檔 | `_design/CODEX_D3_STARTER.md` v0.3 |
| 6 | `.claude/skills/迭代關係/SKILL.md` | 中文 wrapper | 同上 |
| 7 | `.claude/skills/iterate-outline/SKILL.md` | 英文主檔 | `_design/CODEX_D4_STARTER.md` v0.2 |
| 8 | `.claude/skills/迭代大綱/SKILL.md` | 中文 wrapper | 同上 |
| 9 | `.claude/skills/iterate-detailed-outline/SKILL.md` | 英文主檔 | `_design/CODEX_D5_STARTER.md` v0.4 |
| 10 | `.claude/skills/迭代細綱/SKILL.md` | 中文 wrapper | 同上 |
| 11 | `.claude/skills/iterate-scene/SKILL.md` | 英文主檔 | `_design/CODEX_D5_STARTER.md` v0.4（D-054 NEW_REQ_15 落地；**無中文 wrapper**）|

**前置條件：**
- 9th master 第二段 Wave 14-15 SKILL.md 全落地（10 英文主檔 + 10 中文 wrapper；參考其結構）
- Phase A.0F audit cycle Round 4 GO close-out（commit `2ed48f3`）
- Wave 16 Step 4 inline patch 5 findings 全修（commit `1274a5d`）
- D1-D5 starter v0.3/v0.4 + 00_j v0.2 已 freeze（本輪不動）

**Wave 12 工作模式（10th master 對話採；對齊 9th master 第二段 Wave 14-15 batch 模式）：**
- Master 第十輪寫本 batch starter（本檔；含 6 SKILL.md 結構範本 + 個別差異規格）
- CODEX 在乾淨對話**一次性**跑本 batch starter → 寫 6 個 /iterate-* SKILL.md + 5 個中文 wrapper（共 11 檔）
- Master 端內部 verify 11 個 SKILL.md 一致性（grep 結構 + Read 重點 section；不跑 CODEX review starter — Wave 12 設計層已在 D1-D5 freeze）

**設計層 freeze 紀律：**
- D1-D5 starter（v0.3/v0.4）+ 00_j v0.2 已是 Wave 12 設計權威；本 batch starter 不重新設計，只把 D1-D5 既有設計搬到 11 個 SKILL.md
- D1-D5 starter 內部 stale wording（如「00_j v0.1」應為 v0.2；本 starter 已修正引用為 v0.2）不修補（屬 archive 性質；本輪只動 SKILL.md 落地）
- 任何 D1-D5 starter 內 spec 拍板（D-050 子裁決 1+2 / D-053 exception / D-054 hybrid fallback / 議題清單動態載入 / phase_log entry）必須完整落地到對應 SKILL.md，不擅自簡化

⚠ **「Fix one, find two」cascade pattern 預防（9th master 教訓 1-5 + 10th master 內化）：**
- 寫好 11 個 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 reference / file path / D-NNN 引用 / SPEC enum 拼字）
- 一次性 sweep；不局部修補
- 寫 starter 含 spec enum 引用前，直接 grep SPEC §5.2 / parser code verify enum 列表完整 + 拼字正確（教訓 3）

⚠ **長中文檔 truncation 預防（9th master 教訓 6 內化）：**
- 11 個 SKILL.md 每個約 300-500 行；個別檔屬中等長度可用 Write tool；但若單檔超過 600 行建議分段寫（cat heredoc via bash 或多次 Edit append）
- 寫完每個 SKILL.md 跑 `wc -l <path>` + `python3 -c "open(path, 'rb').read().decode('utf-8')"` 驗 utf-8 decode 無 null bytes

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`（內部 nest ``` 不會 toggle 它）
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

⚠ **9th master 教訓 7 內化（cloud sync / 防毒紀律）：**
- `D:\劇本開發工具` 工作目錄已加 OneDrive/Dropbox/Google Drive 排除清單 + Windows Defender 白名單（特別 `.git/`）
- 若 CODEX 跑 task 期間遇 `.git/index.lock` + `.git/index.lock.tmp` + `.git/HEAD.lock` 反覆出現 → 暫停 + 依 HANDOFF_TO_10TH_MASTER §4.1 修復步驟 7 步處理

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 batch task」— 一次性實作 6 個 /iterate-* SKILL.md + 5 個中文 wrapper（共 11 檔）；對齊 TASKS v1.9 §C.2 + 00_protocol/00_j_迭代協議.md v0.2 + 對應 entity creation protocol（00_e/00_f/00_g/00_h/00_l）+ DECISIONS_LOG v2.0 §6.12 D-050 + §6.16 D-053 + §6.17 D-054。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

**重要：請從 `frontend-tools-a0f` 分支讀取（master 落後；10th master 期間 user 將於 Milestone 4 封版宣告後一次性 merge frontend-tools-a0f → master，對齊 HANDOFF_TO_10TH_MASTER §2.5 選 B 完整 merge 策略）。**

**Token 不是限制** — 如有需要你可以 spawn 多個次要 CODEX 對話做使用增加品質和效率。例如：可以開子對話跑 grep verify 11 SKILL.md 結構一致性 / 對照 D1-D5 starter vs 落地 SKILL.md 的拍板映射 / 對照 D-050 三 block vs iterate-* 寫檔紀律 / 對照 00_j v0.2 5 階段流程 vs 各 SKILL.md 流程段是否齊全，再回主對話彙整。優先選擇能提升品質的工作切分。

**你的身份與職責：**
- 你是 implementer — 本輪建 11 個新 SKILL.md（6 英文主檔 + 5 中文 wrapper）
- 對應 9th master 第二段 Wave 14-15 batch 模式（Wave 14 batch 寫 8 檔 export-* / Wave 15 batch 寫 4 檔 diagnose+integrate）
- Wave 12 batch PASS → Phase D Wave 12 整體 PASS → 10th master 進主軸 4（Milestone 4 真正封版宣告）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec（SPEC v1.2 / IC v2.1 / ARCH v1.6 / TASKS v1.9 / DF v0.4 / UD v0.5 / UX v0.4 / L3 v0.2 / REQUIREMENTS_LOCK v1.0 / DECISIONS_LOG v2.0 全 LOCKED 不動）
- ✗ **不**改任何 registry（3 個 LOCKED template yaml 不動）
- ✗ **不**改 scripts/parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_j v0.2；本輪不改 protocol）
- ✗ **不**動 `_tools/frontend/` 任何檔（屬 Phase A.0F scope）
- ✗ **不**動既有 40 個 SKILL.md：
  - Phase A 4 + 4 wrapper（init-project / create-world / status / check-gaps + 4 中文）
  - Phase B 4 + 4 wrapper（create-character / create-relationship / create-outline / create-detailed-outline + 4 中文）
  - Phase C 3 + 3 wrapper（scene-task / dialogue-write / qa + 3 中文）
  - Phase D Wave 13 4 + 4 wrapper（view-world / view-character / view-outline / view-detailed-outline + 4 中文）
  - Phase D Wave 14 4 + 4 wrapper（export-world / export-character / export-outline / export-detailed-outline + 4 中文）
  - Phase D Wave 15 2 + 2 wrapper（diagnose / integrate + 2 中文）
- ✗ **不**改 D1-D5 starter / 00_j / D054_DECISION_PACKAGE / DECISIONS_LOG / POST_LOCK_PENDING / PHASE_D_COMPLETION_REPORT / CANON_DELTA_FRAMEWORK / HANDOFF_TO_10TH_MASTER / 本 starter
- ✗ **不**自動 trigger 階段 4 寫檔（屬 user 拍板；屬 runtime 動作）
- ✗ **不**跑真實 /iterate-* 寫檔（會污染 Template；端到端 M4 testing 屬 user 親跑）
- ✗ **不**重生 view 整合檔（O3 鎖定；屬 /export-* scope）
- ✗ **不**改 D-001~D-055 拍板結論（要動需 user 拍板新 D-056+）
- ✗ **不**擅自把 D-054 hybrid 改成「per-scene 變預設」（屬未來 D-056+ 候選；議題號原預留為 D-055；§6.18.2 順延；user 拍板才能改）
- ✗ **不**自動批量拆全 Instance（D-054 拍板明示 split-to-file 為 user 主動 trigger per S-ID）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.2（5 個 /iterate-* skill task spec）+ D-054 §6.17.2 拍板（/iterate-scene --split-to-file 落地）+ 00_j v0.2 §10.1-§10.7（共通基底 + 個別 entity 迭代呼叫指南）+ ARCH v1.6 §5 影響範圍評估 + §6.7 共通骨架 + SPEC §5.2 frontmatter canonical schema + §11 影響範圍評估規範。

### 共通 SKILL.md 結構（12 段；對齊 D1 starter §1「主 SKILL.md 結構」）

每個英文主檔頂部含：

1. **frontmatter**（YAML；name + description）：
   - `name`: 對齊 directory name（kebab-case；例 `iterate-world`）
   - `description`: 50-200 字；明示對應 entity 類型 + 對齊 00_j 基底協議 5 階段 + 嚴守 D-053 不寫 00_b（iterate-scene 例外 — 描述「D-054 NEW_REQ_15 落地」+ split-to-file 功能）

2. **中文 5 必填 header**：
   - 狀態：DRAFT
   - 版本：v0.1
   - 最後更新：2026-05-23（或 CODEX 跑當天日期）
   - 適用範圍：`/iterate-<entity_type>` skill runtime instructions
   - 優先級：高

3. **markdown 主體含 12 段（依 D1 §1 範本）：**

   1. `## 用途`：一段話描述 skill 目的（迭代什麼 entity / 對齊哪個 protocol / D-054 hybrid fallback if 適用）
   2. `## 觸發語`：英文 slash command + 中文別名 reference（iterate-scene 無中文 wrapper）
   3. `## 觸發協議`：對應 00_j v0.2 + 對應 entity creation protocol + 必讀 references
   4. `## 啟動前檢查`：D-049 Template-detect（`.template_root` 不存在）+ Bootstrap completed（`.protocol_version` 存在）+ 目標 entity 存在 + LOCKED status check + 下游 pipeline 互鎖檢查（per 00_k §10.7.5）
   5. `## 流程`：5 階段對應 00_j v0.2 §3-§7（變更點識別 / 強制影響範圍評估 / 收斂 / 執行 / 實體驗證）
   6. `## 影響範圍評估規範`：**核心段 — 不可省略**；含雙路反查 algorithm（依 ARCH §5 + 00_j v0.2 §4）+ 預期清單表（per skill 差異）
   7. `## .protocol_version 寫入規範`：phase_log entry 對應 00_j v0.2 §6.1（含 phase / date / skill / status / modified_entity / modified_files / scope_choice / affected_files_evaluated / prereq_changed / qa_recheck_recommended / abort_reason / customizations）
   8. `## 輸入`：user 變更意圖（chat 對話接受 + 可選參數明示）
   9. `## 輸出`：寫檔範圍（依 D-050 子裁決 2）+ frontmatter `depends_on` 補完 + phase_log audit entry
   10. `## 邊界`：D-050 三 block（子裁決 1 + D-053 紀錄 + 子裁決 2 寫檔目錄表）對齊 Phase B 4 個 /create-* skill v0.3/v0.4 格式
   11. `## 錯誤處理 / Rollback`：沿用 00_j v0.2 §6 階段 4 rollback 紀律（任一步出錯 → 還原已寫變更 + 印錯訊息 + 不更新 phase_log + 提示 user 重試 / 拍板降級）
   12. `## 錯誤呈現規則`：沿用 ARCH §3.3.1 四件套（錯誤訊息結構 / 建議 / 可選下一步 / phase_log entry 是否落地）

### 共通 phase_log entry 範例

```yaml
- phase: iterate-<entity_type>
  date: YYYY-MM-DD
  skill: /iterate-<entity_type>
  status: completed
  modified_entity: <entity_id>  # 例 W-rules / C-林夜 / S-3-2
  modified_files:
    - <檔案 1 完整 Instance 路徑>
    - <檔案 2 完整 Instance 路徑>
  scope_choice: 2  # 1/2/3/4 對應階段 2 user 拍板範圍
  affected_files_evaluated:
    direct: [<檔案清單>]
    depends: [<檔案清單>]
    indirect: [<檔案清單>]
  prereq_changed: false  # 若強制迭代且有進行中下游 → true
  qa_recheck_recommended: []  # 若涉 V/C/W-rules 變動且已產出台詞 → 列建議重跑的 09_x
  external_action_required: null  # 若需 user 手動 patch 00_b 等 D-053 外範圍 → 標明
  abort_reason: null
  customizations: []
```

### 共通邊界 block 範例（D-050 三 block；對齊 D1-D5 v0.3/v0.4）

```markdown
## 邊界

### D-050 子裁決 1：本 skill 嚴禁寫 00_protocol/

本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1（DECISIONS_LOG v2.0 §6.12.2）規定唯一例外是 `/init-project` skill；本 skill 不在例外範圍。

### D-053 /create-world exception 紀錄（本 skill 不在例外範圍）

D-053（DECISIONS_LOG v2.0 §6.16.2）partial supersede D-050 子裁決 1 — **`/create-world` 可寫 00_b §1/§2** Instance-specific section（類型語氣 / 髒話尺度）。本 skill **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。若 user 跑本 skill 時需要對 00_b §1/§2 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 00_b §1/§2 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。

### D-050 子裁決 2：本 skill 寫檔目錄表（嚴格限定）

本 skill 寫檔範圍嚴格限：
- `<列出該 skill 對應寫檔目錄；對齊 D-050 子裁決 2 + Phase B /create-* 對應 skill 寫檔範圍>`
- `.protocol_version.phase_log`（runtime tracking）

**不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053；/iterate-* 全部不寫 00_b）
```

### 中文 wrapper SKILL.md 結構（極簡模式；對齊 Phase A/B/C/Wave 13/14/15 既有中文 wrapper）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 迭代<中文 entity 名>
description: "/iterate-<entity_type> skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/iterate-<entity_type> skill 中文觸發 wrapper  
優先級：高

# /迭代<中文 entity 名>（/iterate-<entity_type> wrapper）

本 wrapper 是 `/iterate-<entity_type>` 的中文別名。執行時以英文主檔 `.claude/skills/iterate-<entity_type>/SKILL.md` 為權威。

請參考 `.claude/skills/iterate-<entity_type>/SKILL.md`。
```

**不建立第二套流程；不複製英文主檔的 5 階段 / 影響範圍評估 / 邊界 block。**

**/iterate-scene 無中文 wrapper**（D-054 拍板原文未指定中文別名；屬 hybrid escape hatch 性質的開發者工具；user 用英文 slash command + S-ID）。


---

# 1.1 個別 skill 差異規格

依 D1-D5 starter v0.3/v0.4 既有設計搬到 SKILL.md。每個 skill 僅列「跟共通結構不同」的差異規格；共通段（5 階段 / 共通 phase_log / 共通邊界 block 範例）採共通範本。

## 1.1.1 /iterate-world（對應 D1 v0.3）

- **觸發語：** `/iterate-world`（不接 user 參數；變更目標由 chat 對話確認）+ 中文別名 `/迭代世界觀`
- **對應 protocol：** `00_protocol/00_j_迭代協議.md` v0.2（共通基底）+ `00_protocol/00_e_世界觀創建協議.md` v0.1（對應 entity 創建協議）
- **議題清單動態載入：** **適用**（registry key = `00_e_world`；若 user 變更目標含新增 issue → 從 `<instance_root>/issue_type_registry.yaml` 的 `00_e_world` key 讀；user_extensions / core_overrides 一併讀）
- **modify entity 範圍：** W-rules / V / W-language（任一或多個；user 在階段 1 明示）
- **依賴下游：** 影響範圍最廣 — 含 C-* / R-*-* / P / CH-* / S-*-* 全依賴 W-rules（per 00_j v0.2 §10.1）
- **D-050 子裁決 2 寫檔範圍：**
  - `01_world/01_a_世界觀總覽.md`
  - `01_world/01_b_世界語言規格.md`
  - `01_world/01_c_陣營與階級語言.md`
  - `02_vocabulary/02_a_專有名詞表.md`
  - `02_vocabulary/02_b_俗稱與黑話表.md`
  - `02_vocabulary/02_c_禁用詞與慎用詞表.md`
  - `.protocol_version.phase_log`
- **影響範圍評估預期清單（雙路反查）：**
  - direct: `01_world/01_a`
  - depends: `01_world/01_b` / `01_c` / `02_vocabulary/02_a` / `02_b` / `02_c` / `03_characters/*_聲線卡.md`（所有 C-*）/ 可能 `04_relationships/04_a`
  - indirect: `05_plot/05_a` / `05_b` / `06_scene_index/06_a` / `00_b §1/§2`（影響範圍但本 skill 不寫；屬 user 手動 patch）
- **下游 pipeline 互鎖：** 若 W-rules 改動影響 V 禁用詞 / 句型 → 進行中的 /qa 受影響 → 階段 2 拒絕並列出衝突 skill
- **階段 5 印「下一步建議」：** 若需重新看視圖請跑 `/view-world` 或 `/export-world`；若 02_c 禁用詞變動建議重跑 `/qa` 09_c

## 1.1.2 /iterate-character（對應 D2 v0.3）

- **觸發語：** `/iterate-character <name>`（接 1 user 參數 — 角色名；對齊 /create-character pattern）+ 中文別名 `/迭代角色 <name>`
- **對應 protocol：** `00_j v0.2` + `00_protocol/00_f_角色創建協議.md` v0.2
- **議題清單動態載入：** **適用**（registry key = `00_f_character`）
- **modify entity 範圍：** C-<name>（單一角色；user 在 slash command 接 name 明示）
- **依賴下游：** 影響範圍含 R-*-<name> 關係 / 該角色出場場景 task / 該角色對應台詞 / 該角色弧線階段
- **D-050 子裁決 2 寫檔範圍：**
  - `03_characters/main/<name>_聲線卡.md`（若主要角色）
  - `03_characters/minor/<name>_聲線卡.md`（若次要角色）
  - `03_characters/npc/<NPC類型>模板.md`（若 NPC）
  - `.protocol_version.phase_log`
- **影響範圍評估預期清單（雙路反查）：**
  - direct: `03_characters/<聲線卡 path>`
  - depends: `04_relationships/04_a`（含 C-<name> 的 row）/ `04_b`（含 C-<name> 的 timeline event）/ `05_plot/05_c_主線弧線階段.md`（含 C-<name> 弧線）/ `07_scene_tasks/*`（含 C-<name> 出場場景）
  - indirect: `08_dialogue_outputs/*`（已產出台詞）/ `09_quality_assurance/*`（已產出 QA 報告）
- **下游 pipeline 互鎖：** 若 C-<name> 聲線描述變動 → 進行中的 /dialogue-write / /qa 受影響 → 階段 2 拒絕並列出衝突 skill
- **階段 5 印「下一步建議」：** 若需重新看角色視圖請跑 `/view-character <name>` 或 `/export-character <name>`；若聲線變動且已產出該角色台詞建議重跑 `/qa` 09_b 聲線一致性

## 1.1.3 /iterate-relationship（對應 D3 v0.3）

- **觸發語：** `/iterate-relationship <a> <b>`（接 2 user 參數 — 兩個角色名；對齊 /create-relationship pattern）+ 中文別名 `/迭代關係 <a> <b>`
- **對應 protocol：** `00_j v0.2` + `00_protocol/00_l_關係創建協議.md` v0.2
- **議題清單動態載入：** **適用**（registry key = `00_l_relationship`；對齊 D-047 yaml key 修正）
- **modify entity 範圍：** R-<a>-<b>（單一關係；user 在 slash command 接 兩名 明示）
- **依賴下游：** 影響範圍含 C-<a> + C-<b> 聲線卡關係段 / 04_b 時間線 event / 兩角色共同出場場景
- **D-050 子裁決 2 寫檔範圍：**
  - `04_relationships/04_a_角色關係矩陣.md`（matrix row append/update）
  - `04_relationships/04_b_關係時間線.md`（若議題 6 觸發 timeline event）
  - `03_characters/<a>_聲線卡.md` 與 `<b>_聲線卡.md` 的**「關係段」merge**（必要輸出 — 跨檔寫入但限定該 section）
  - `.protocol_version.phase_log`
- **影響範圍評估預期清單（雙路反查）：**
  - direct: `04_relationships/04_a`
  - depends: `04_relationships/04_b` / `03_characters/<a>_聲線卡.md` 關係段 / `03_characters/<b>_聲線卡.md` 關係段
  - indirect: `07_scene_tasks/*`（兩角色共同出場）/ `08_dialogue_outputs/*` / `09_quality_assurance/*`
- **D-050 跨檔寫入合法性：** 03_characters 關係段 merge 是 R skill 的**合法**跨檔寫入（屬 R-<a>-<b> entity scope 的一部分；不是寫整個聲線卡 — 對齊 D-050 子裁決 2 R 行）
- **階段 5 印「下一步建議」：** 若需重新看角色視圖請跑 `/view-character <a>` / `/view-character <b>`；若關係張力變動且已產出共同場景台詞建議重跑 `/qa` 09_h 對話張力

## 1.1.4 /iterate-outline（對應 D4 v0.2）

- **觸發語：** `/iterate-outline`（不接 user 參數；變更目標由 chat 對話確認）+ 中文別名 `/迭代大綱`
- **對應 protocol：** `00_j v0.2` + `00_protocol/00_g_大綱創建協議.md` v0.2
- **議題清單動態載入：** **適用**（registry key = `00_g_outline`；對齊 D-047 yaml key 修正）
- **modify entity 範圍：** P（單一專案大綱實體；user 在階段 1 明示變更段：主線 / 章節弧線 / 資訊揭露 / 伏筆等）
- **依賴下游：** 影響範圍含 CH-* 章節結構 / 主要 C-* 弧線 / S-*-* 場景索引
- **D-050 子裁決 2 寫檔範圍：**
  - `05_plot/05_a_主線大綱模板.md`（主體）
  - `05_plot/05_c_主線弧線階段.md`（若議題 4 / 5 觸發）
  - `05_plot/05_d_資訊揭露順序.md`（若議題 5 觸發）
  - `05_plot/05_e_伏筆與回收.md`（若議題 5 觸發）
  - `.protocol_version.phase_log`
- **影響範圍評估預期清單（雙路反查）：**
  - direct: `05_plot/05_a` / `05_c` / `05_d` / `05_e`
  - depends: `05_plot/05_b_章節結構模板.md`（CH-* 屬 CH skill scope；本 skill 不寫但需評估）/ `06_scene_index/06_a` / 受弧線影響的 `03_characters/*_聲線卡.md`
  - indirect: `07_scene_tasks/*` / `08_dialogue_outputs/*` / `09_quality_assurance/*`
- **D-050 邊界明示：** 本 skill **不寫** 05_b 章節結構 + CH-* / S-*-* 詳細內容（屬 /iterate-detailed-outline scope）
- **階段 5 印「下一步建議」：** 若需重新看大綱視圖請跑 `/view-outline` 或 `/export-outline`；若主線 / 弧線變動需 propagate 到細綱建議跑 `/iterate-detailed-outline`

## 1.1.5 /iterate-detailed-outline（對應 D5 v0.4）

- **觸發語：** `/iterate-detailed-outline` 或 `/iterate-detailed-outline <CH-ID>`（可選 1 user 參數 — 章節 ID；若不傳則 chat 對話確認）+ 中文別名 `/迭代細綱`
- **對應 protocol：** `00_j v0.2` + `00_protocol/00_h_細綱創建協議.md` v0.2
- **議題清單動態載入：** **適用**（registry key = `00_h_detailed_outline`；對齊 D-047 yaml key 修正）
- **modify entity 範圍：** CH-* 章節 / S-*-* 場景索引（user 在階段 1 明示）
- **依賴下游：** 影響範圍含對應 06_a row + 已存在 per-scene 拆檔（D-054 hybrid）+ 已 generate 的 07_scene_tasks / 08_dialogue_outputs / 09_quality_assurance
- **D-050 子裁決 2 寫檔範圍：**
  - `05_plot/05_b_章節結構模板.md`（CH-* entry）
  - `06_scene_index/06_a_場景索引模板.md`（S-*-* row）
  - `06_scene_index/CH<n>_S<m>_<scene_name>.md`（若 D-054 hybrid fallback 抓到 per-scene 檔）
  - `.protocol_version.phase_log`
- **D-054 hybrid fallback 讀檔（本 skill 與 /scene-task / /view-detailed-outline / /export-detailed-outline 共用此邏輯）：**
  - 先 check 對應 per-scene 檔 `06_scene_index/CH<n>_S<m>_*.md` 是否存在
  - 存在 → 讀 per-scene 檔（優先）
  - 不存在 → fallback 讀 aggregate `06_a` 對應 row
  - 兩者皆無 → 拒絕並提示先跑 `/create-detailed-outline` 建立
- **影響範圍評估預期清單（雙路反查）：**
  - direct: `05_plot/05_b`（CH-* entry）/ `06_scene_index/06_a`（S-*-* row；含 D-054 fallback per-scene 檔）
  - depends: 已存在 per-scene `06_scene_index/CH<n>_S<m>_*.md` 拆檔 + `07_scene_tasks/CH<n>_S<m>_*` 任務包（若 generate）
  - indirect: `08_dialogue_outputs/*`（若已產出台詞）+ `09_quality_assurance/*`（若已產出 QA 報告）
- **per-scene 拆檔需求拒絕：** 階段 1 若 user 明示「per-scene 拆檔需求」→ 本 skill 拒絕並提示「per-scene 拆檔屬 /iterate-scene --split-to-file scope；請改用 /iterate-scene <S-ID> --split-to-file」
- **階段 5 印「下一步建議」：** 若需重新看細綱視圖請跑 `/view-detailed-outline` 或 `/export-detailed-outline`；若 S-*-* 變動且已產出台詞建議重跑全 8 份 `/qa`

## 1.1.6 /iterate-scene（D-054 NEW_REQ_15 落地；對應 D5 v0.4；**無中文 wrapper**）

- **觸發語：** `/iterate-scene <S-ID>` 或 `/iterate-scene <S-ID> --split-to-file`（接 1 user 參數 + 可選 flag）
- **對應 protocol：** `00_j v0.2` §10.7（split-to-file 設計詳述）
- **議題清單動態載入：** **不適用**（split-to-file 屬 file organization 操作；不涉議題對話）
- **modify entity 範圍：** 單一 S-<ch>-<n>（user 在 slash command 接 S-ID 明示）
- **`--split-to-file` 行為（D-054 hybrid 落地）：**
  - 把指定場景從聚合 `06_scene_index/06_a_場景索引模板.md` 對應 row split 為獨立 `06_scene_index/CH<n>_S<m>_<scene_name>.md` 檔
  - 在原 06_a row 加 `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->` marker（**不刪除 row** — 保留 fallback 兼容；下游 /scene-task 兩階段 fallback 邏輯依此判定優先讀 per-scene 檔）
  - 寫新 per-scene 檔 frontmatter 對齊 SPEC §5.2 **上游/靜態檔三欄**：`entities: [S-<ch>-<n>]` / `depends_on` / `weight: {S-<ch>-<n>: 1.0}`（繼承原 row 設定）
  - **不擴充 07/08/09 pipeline 專屬 frontmatter 欄位**（pipeline_state / mode_tag / qa_decision / qa_type / source_task / source_dialogue / source_dialogues / scene_id 等屬下游 07_scene_tasks / 08_dialogue_outputs / 09_quality_assurance 範圍；06_scene_index per-scene 屬上游/靜態檔；對齊 06_a 場景索引模板 frontmatter 規範；D5 v0.4 R2-MAJOR-02 + R3-MAJOR-01 修補對齊）
- **不帶 flag 行為：** `/iterate-scene <S-ID>` 不帶 `--split-to-file` → 純 S-*-* 內容迭代（修改 06_a 對應 row 或既有 per-scene 檔內容；同 /iterate-detailed-outline 子模式）
- **D-050 子裁決 2 寫檔範圍：**
  - `06_scene_index/06_a_場景索引模板.md`（row 更新 / split marker）
  - `06_scene_index/CH<n>_S<m>_<scene_name>.md`（split-to-file 新建 / 既有 per-scene 檔修改）
  - `.protocol_version.phase_log`
- **影響範圍評估預期清單（雙路反查；split-to-file 子模式）：**
  - direct: `06_scene_index/06_a` 對應 row
  - depends: 所有引用本 S-*-* 的檔（含 `07_scene_tasks/CH<n>_S<m>_*` / `08_dialogue_outputs/*` / `09_quality_assurance/*`）
  - indirect: 通常無（split-to-file 是 file org；路徑不變 — 下游 /scene-task 自動 detect 新 per-scene 檔）
- **啟動前檢查（差異）：**
  - 目標 S-<ch>-<n> 存在（06_a row 或 per-scene 檔；任一；D-054 hybrid fallback）
  - 對應 CH-* 存在
  - **split-to-file 子模式額外檢查：** 對應 per-scene 檔**尚未存在**（避免重複拆檔）
- **phase_log entry 差異：** 含 `split_to_file: true` 標記（D-054 NEW_REQ_15 落地專屬欄位）
- **階段 4 寫檔順序（split-to-file 子模式）：**
  1. 寫新 per-scene 檔（完整 row 內容 + frontmatter 對齊上游三欄）
  2. 在原 06_a row 加 `<!-- split-to-file: ... -->` marker（不刪除 row）
  3. phase_log entry 標 `split_to_file: true`
  4. 任一步出錯 rollback：刪 per-scene 檔 + 還原 06_a row marker
- **階段 5 印「下一步建議」：**
  - split-to-file 完成；下次 `/scene-task <S-ID>` 跑時會自動 detect per-scene 檔優先（D-054 hybrid 兩階段 fallback）
  - **NEW_REQ_15 trigger B monitor：** 若連續 ≥ 5 次拆檔請通知 master 啟動 D-056+ 評估（per-scene 是否變預設？；議題號原預留為 D-055；§6.18.2 順延）
~~~

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：

   共通必讀：
   - `_design/CODEX_D1_STARTER.md` v0.3（共通範本 — 完整 SKILL.md 結構 + 12 段 skeleton + D-050 三 block + 5 階段流程；本 batch 沿用）
   - `_design/CODEX_D2_STARTER.md` v0.3（C-* 差異規格）
   - `_design/CODEX_D3_STARTER.md` v0.3（R-*-* 跨檔關係段 merge）
   - `_design/CODEX_D4_STARTER.md` v0.2（P 差異規格）
   - `_design/CODEX_D5_STARTER.md` v0.4（CH-* + S-*-* + /iterate-scene split-to-file；D-054 NEW_REQ_15 落地）
   - `00_protocol/00_j_迭代協議.md` v0.2（共通基底 — 5 階段 / 影響範圍評估 / phase_log entry 規範；本輪不修改）
   - `00_protocol/00_e_世界觀創建協議.md` v0.1（W 對應 entity 創建協議）
   - `00_protocol/00_f_角色創建協議.md` v0.2（C 對應）
   - `00_protocol/00_g_大綱創建協議.md` v0.2（P 對應）
   - `00_protocol/00_h_細綱創建協議.md` v0.2（CH/S 對應；line 198 escape hatch 為 D-054 hybrid 設計源頭）
   - `00_protocol/00_l_關係創建協議.md` v0.2（R 對應）

   結構範例必讀（Phase B v0.3/v0.4 + Phase D Wave 13-15 為主）：
   - `.claude/skills/create-world/SKILL.md` v0.1（最早 /create-* skill；frontmatter / 中文 header 範例）
   - `.claude/skills/create-character/SKILL.md` v0.4（最新 v0.4；含 D-050 + D-053 雙 block 完整範例）
   - `.claude/skills/create-relationship/SKILL.md` v0.3（含 R 跨檔關係段 merge 範例）
   - `.claude/skills/create-outline/SKILL.md` v0.3（含 D-050 + D-053 雙 block）
   - `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 結構範例；含 R8-MA-01 prereq fix + R9-INFO-02 body D-053 exception block）
   - `.claude/skills/view-world/SKILL.md` v0.1（9th master Wave 13 落地；12 段結構新範例 — 9th master 第一段 batch starter 模式產出）
   - `.claude/skills/export-world/SKILL.md` v0.1（9th master Wave 14 落地；含寫檔 SKILL.md 範例）
   - `.claude/skills/integrate/SKILL.md` v0.1（9th master Wave 15 落地；含「寫檔但 user 拍板」紀律範例 — 對 iterate-* 的「寫檔需 user 拍板」可作參考；雖然 iterate-* 是 user 跑 slash command 就進迭代流程，但階段 3 收斂預告稿 + 階段 4 寫檔仍需 user 明示「通過/OK」才執行）

   D-NNN 拍板必讀：
   - `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050（寫檔邊界子裁決 1+2）+ §6.16 D-053（/create-world exception）+ §6.17 D-054（per-scene hybrid 拍板）+ §6.7 C-9（depends_on frontmatter）
   - `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED；含完整 hybrid 設計推理）
   - `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_15（D-054 未來迭代追蹤 trigger A/B/C/D）

   spec 規範必讀：
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）+ §11（影響範圍評估規範）+ §16（文件狀態機 7 種）
   - `_design/ARCHITECTURE.md` v1.6 §3.3（skill 內容規範）+ §3.3.1（錯誤呈現規則四件套）+ §5（影響範圍評估）+ §6.7（共通骨架 5 階段）
   - `_design/TASKS.md` v1.9 §C.1（00_j 已實作；不修改）+ §C.2（5 個 /iterate-* skill task spec）
   - `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1（5 上游 protocol 對應 entity 創建協議）

2. **依次寫 11 個 SKILL.md**（建議順序；可平行 spawn 子 CODEX 對話）：

   - **Pass 1（5 英文主檔，先建主軸）：** iterate-world → iterate-character → iterate-relationship → iterate-outline → iterate-detailed-outline
   - **Pass 2（1 英文主檔，D-054 落地）：** iterate-scene（含 --split-to-file 子模式）
   - **Pass 3（5 中文 wrapper，極簡模式）：** 迭代世界觀 → 迭代角色 → 迭代關係 → 迭代大綱 → 迭代細綱

   每個 SKILL.md 結構對齊本 starter §1「共通 SKILL.md 結構（12 段）」+ §1.1.X 個別差異規格。

3. **跑 baseline 驗證**（不寫實際 .protocol_version 紀錄；Template repo 端）：

   ```bash
   python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -5
   python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -5
   python3 -X utf8 -B -c "import sys; sys.path.insert(0, 'scripts'); from parse_frontmatter import build_repo_index; r = build_repo_index('.'); errs = [i for i in r.issues if i.severity == 'ERROR']; warns = [i for i in r.issues if i.severity == 'WARN']; print(f'ERROR={len(errs)} WARN={len(warns)}')"
   ```

   對齊 10th master baseline（HANDOFF_TO_10TH_MASTER §2.4）：
   - `check_headers.py`: **0 ERROR / ≤ 60 WARN**（current snapshot 53；本 batch 加 11 個新檔可能 +3-5 WARN 屬 markdown header 長 note pattern；可接受）
   - `check_paths.py`: **≤ 247 ERROR**（hard-limit；不新增 active missing path；本輪不修 NEW_REQ_9 舊債）
   - `build_repo_index('.')`: **0 ERROR / ≤ 100 WARN**（current snapshot 89；本 batch 加 11 個新檔可能 +5-10 WARN 屬新 SKILL.md 補完未引用情況）

4. **不跑真實 /iterate-* 寫檔**（會污染 Template；M4 testing 屬 user 親跑）

5. **撰寫 batch review report**（可選；10th master 內部 verify 採 grep 結構 + Read 重點 section 模式，不開新 CODEX review starter；Wave 12 設計層已在 D1-D5 freeze 不重審）

---

# 3. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index baseline | 對齊 10th master baseline；無新 ERROR；WARN 增量 ≤ 10 |
| 2. SKILL.md 落地 | 11 個 SKILL.md 存在（6 英文主檔 + 5 中文 wrapper；iterate-scene 無中文 wrapper） | 結構齊全 |
| 3. frontmatter / 中文 header | 11 個檔含 YAML frontmatter（name + description）+ 中文 5 必填 header | 對齊 SPEC §5.2 + Phase A/B/C/Wave 13-15 既有 pattern |
| 4. 12 段主檔結構 | 6 個英文主檔含 12 段（用途 / 觸發語 / 觸發協議 / 啟動前檢查 / 流程 / 影響範圍評估規範 / .protocol_version 寫入規範 / 輸入 / 輸出 / 邊界 / 錯誤處理 / Rollback / 錯誤呈現規則）| 對齊 D1 §1「主 SKILL.md 結構」+ 9th master Wave 13-15 落地範本 |
| 5. 邊界紀律 | D-050 三 block（子裁決 1 + D-053 紀錄 + 子裁決 2 寫檔目錄表）| 對齊 Phase B v0.3/v0.4 + 9th master Wave 13-15 落地範本 |
| 6. 影響範圍評估 | 6 個英文主檔含 `## 影響範圍評估規範` 段 + 雙路反查 algorithm + 預期清單表（per skill 差異）| 對齊 ARCH §5 + 00_j v0.2 §4 |
| 7. phase_log entry 規範 | 6 個英文主檔含 phase_log entry 範例 + 對應 entity 類型 / `external_action_required` 欄位 | 對齊 00_j v0.2 §6.1 |
| 8. **D-054 hybrid fallback 落地** | iterate-detailed-outline + iterate-scene 含 D-054 兩階段 fallback 讀檔邏輯 + iterate-scene 含 split-to-file 子模式（含 marker + frontmatter 上游三欄 + phase_log `split_to_file: true`）| 對齊 D-054 拍板原文 + D054_DECISION_PACKAGE §2.1 + D5 v0.4 |
| 9. **/scene-task / /view-detailed-outline / /export-detailed-outline 既有 fallback 兼容** | iterate-scene 寫的 per-scene 檔被既有 3 個 skill 兩階段 fallback 邏輯自動 detect | 對齊既有 scene-task v0.1 + view-detailed-outline v0.1 + export-detailed-outline v0.1 |
| 10. 中文 wrapper 極簡模式 | 5 個中文 wrapper 為 thin wrapper 指向英文主檔；不複製第二套流程 | 對齊 Phase A/B/C/Wave 13-15 既有中文 wrapper |
| 11. cross-ref stale grep | 11 個 SKILL.md 無 stale version reference（00_j v0.2 / Phase B v0.3/v0.4 / DECISIONS_LOG v2.0 等）| 對齊 10th master 教訓 1+2 broader sweep |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**自動 trigger 階段 4 寫檔（屬 user 拍板；屬 runtime 動作）
- **不**重生 view 整合檔（O3 鎖定；屬 /export-* scope）
- **不**升 entity 狀態
- **不**呼叫其他 skill
- **不**改 LOCKED spec / registry / parser code
- **不**改既有 40 個 SKILL.md（含 D-054 落地依賴的 scene-task / view-detailed-outline / export-detailed-outline；本 batch 新建 11 個檔不動既有）
- **不**改 00_j / 00_e/f/g/h/l 任何 protocol（00_j 是本 skill 對應 protocol；只讀為權威）
- **不**改 D1-D5 starter / D054_DECISION_PACKAGE / DECISIONS_LOG / POST_LOCK_PENDING / CANON_DELTA_FRAMEWORK / PHASE_D_COMPLETION_REPORT / HANDOFF_TO_10TH_MASTER / 本 starter
- **不**擅自把 D-054 hybrid「per-scene 變預設」（屬未來 D-056+ 候選；議題號原預留為 D-055；§6.18.2 順延；user 拍板才能改）
- **不**自動批量拆全 Instance（D-054 拍板明示 split-to-file 為 user 主動 trigger per S-ID）

**「Fix one, find two」cascade pattern 預防（10th master 教訓 1-5 內化）：**

- 寫好 11 個 SKILL.md 後跑 grep 全掃 stale cross-ref（含 00_j 版本 / Phase B SKILL.md 版本 / D-NNN 引用 / SPEC enum 拼字 / file path）
- 一次性 sweep 避免局部修補導致 cascade
- 寫 SKILL.md 含 spec enum 引用前直接 grep SPEC §5.2 / parser code verify enum 列表完整 + 拼字正確（教訓 3）
- 寫 SKILL.md 含 wave_X SKILL.md cross-ref 前直接 ls `.claude/skills/` verify directory name 拼字（避開 typo cascade）

**長中文檔 truncation 預防（10th master 教訓 6 內化）：**

- 11 個 SKILL.md 每個約 300-500 行；個別檔屬中等長度可用 Write tool 整檔寫
- 若單檔超過 600 行建議分段寫（cat heredoc via bash 或多次 Edit append）
- 寫完每個 SKILL.md 跑 `wc -l <path>` 驗行數預期 + `python3 -c "open(path, 'rb').read().decode('utf-8')"` 驗 utf-8 decode 無 null bytes

---

# 5. Cross-ref

- `_design/CODEX_D1_STARTER.md` v0.3（共通範本；/iterate-world 個別規格）
- `_design/CODEX_D2_STARTER.md` v0.3（/iterate-character 個別規格）
- `_design/CODEX_D3_STARTER.md` v0.3（/iterate-relationship 個別規格）
- `_design/CODEX_D4_STARTER.md` v0.2（/iterate-outline 個別規格）
- `_design/CODEX_D5_STARTER.md` v0.4（/iterate-detailed-outline + /iterate-scene 個別規格；D-054 NEW_REQ_15 落地）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED；hybrid 設計推理）
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050 + §6.16 D-053 + §6.17 D-054 + §6.7 C-9
- `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_15 trigger A/B/C/D
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.0（Phase D 接近條件達成事實檔；§3.1 Wave 12 partial 狀態 — 本 batch task PASS 後可標 ✅）
- `_design/HANDOFF_TO_10TH_MASTER.md` v1.0（10th master scope；本 batch 屬主軸 2 priority 1）
- `00_protocol/00_j_迭代協議.md` v0.2（共通基底；本輪不修改）
- `00_protocol/00_e_世界觀創建協議.md` v0.1（W 對應）
- `00_protocol/00_f_角色創建協議.md` v0.2（C 對應）
- `00_protocol/00_g_大綱創建協議.md` v0.2（P 對應）
- `00_protocol/00_h_細綱創建協議.md` v0.2（CH/S 對應；含 D-054 hybrid 設計源頭 line 198 escape hatch）
- `00_protocol/00_l_關係創建協議.md` v0.2（R 對應）
- `.claude/skills/create-world/SKILL.md` v0.1（frontmatter / 中文 header 範例）
- `.claude/skills/create-character/SKILL.md` v0.4（D-050 + D-053 雙 block 完整範例）
- `.claude/skills/create-relationship/SKILL.md` v0.3（R 跨檔關係段 merge 範例）
- `.claude/skills/create-outline/SKILL.md` v0.3
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 + D-050 + D-053 範本）
- `.claude/skills/view-detailed-outline/SKILL.md` v0.1（D-054 hybrid fallback 範本 — 9th master Wave 13 落地）
- `.claude/skills/export-detailed-outline/SKILL.md` v0.1（D-054 hybrid 三 phase 完整範本 — 9th master Wave 14 落地）
- `.claude/skills/scene-task/SKILL.md` v0.1（D-054 hybrid 兩階段 fallback 讀檔範本 — Phase C 落地）
- `.claude/skills/integrate/SKILL.md` v0.1（「寫檔但 user 拍板」紀律範本 — 9th master Wave 15 落地）
- `_design/ARCHITECTURE.md` v1.6 §3.3 + §3.3.1 + §5 + §6.7
- `_design/SPEC.md` v1.2 §5.2 + §11 + §16
- `_design/TASKS.md` v1.9 §C.1 + §C.2
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1 + §5（Canon Delta 對齊；iterate-* 未來實作 partial supersede target）
