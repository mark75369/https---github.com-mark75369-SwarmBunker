狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：Phase C Wave 9 task — /scene-task skill + 中文 wrapper 實作（含 D-054 hybrid fallback 讀檔邏輯）  
優先級：高

# CODEX_C1_STARTER — Phase C Wave 9 C.1：/scene-task skill 實作

# 0. 本檔用途

Phase C Wave 9 起手第一條 task — 實作 `/scene-task` skill（下游台詞生產 pipeline 的第一個 skill；建立場景任務包）。對齊 TASKS v1.9 §D.2 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.3 + 00_protocol/00_k v0.1 階段 1 + ARCH §6.1 + D-054 hybrid 讀檔 fallback 邏輯。

**前置條件：** Phase B 收尾 + Cleanup round + patch round 2 + patch round 3 + Round 10 GO + D-054 拍板選 1 Hybrid 落地（DECISIONS_LOG v2.0 §6.17）。

**C.1 PASS → Phase C Wave 9 進 C.2 /dialogue-write skill 實作**（C.1 → C.2 → C.3 依序不可平行；C.1 產出的任務包 → C.2 讀任務包寫台詞 → C.3 讀台詞寫 QA）。

⚠ **D-054 拍板對齊（DECISIONS_LOG v2.0 §6.17.2）：**
- /create-detailed-outline 預設寫聚合 06_a（不變）
- **本 skill 必須含 D-054 兩階段 fallback 讀檔邏輯**：先 check `06_scene_index/CH<n>_S<m>_<scene_name>.md` per-scene 檔；不存在 → fallback 讀 aggregate `06_a` 對應 row
- 既有 00_h SKILL.md line 198 escape hatch wording 自然承接此設計

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase C Wave 9 C.1 task」— 實作 /scene-task skill（含中文 wrapper）；對齊 TASKS v1.9 §D.2 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.3 + 00_protocol/00_k v0.1 階段 1 + ARCH §6.1 + D-054 hybrid 讀檔 fallback 邏輯（DECISIONS_LOG v2.0 §6.17.2）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase C Wave 9 第一條 task（C.1 → C.2 → C.3 依序）；/scene-task 是下游 pipeline 第一個 skill
- C.1 PASS → 可進 C.2 /dialogue-write skill 實作

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_k v0.1；它含 5 報告 stale 屬 R8-INFO-06 待後續 patch；本 skill 直接 reference UD §2.5.3 v0.3 為權威）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 13 個 SKILL.md（init-project / create-* x5 / status / check-gaps / 5 中文 wrapper / 建立世界觀）
- ✗ **不**寫 /dialogue-write（C.2 scope）/ /qa（C.3 scope）
- ✗ **不**自動 trigger D.2.5 任務包 REVIEW gate（屬人類 task）
- ✗ **不**跑真實 /scene-task 寫檔（會污染 Template；端到端測試屬 user 親跑 M3）
- ✗ **不**改 D054_DECISION_PACKAGE / NEW_REQ_15 / 未來迭代追蹤紀錄

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §D.2（line 1674-1701）+ UD v0.5 §2.3 五個內部子階段 + 00_k v0.1 階段 1 + SPEC §12.5 任務包必填欄位 + D-054 拍板選 1 Hybrid 讀檔 fallback。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/scene-task/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/場景任務包/SKILL.md` | 中文 wrapper |

### /scene-task 主 SKILL.md 結構（依 ARCH §3.3 + Wave 7 範式）

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；含 D-054 hybrid fallback mention）
- 中文 5 必填 header
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（英文 slash command + 中文別名 reference）
  - `## 觸發協議`（對應 00_k v0.1 階段 1 + UD §2.3 + 必讀 references；註：00_k DRAFT v0.1 / 8 報告 stale 屬 R8-INFO-06 — 本 skill 不直接 reference 00_k 的 8 報告段，改 ref UD §2.5.3 v0.3）
  - `## 啟動前檢查`（D-049 Template-detect + Bootstrap completed + 對應上游 entity REVIEW check + 場景 ID 解析）
  - `## 流程`（5 階段對應 UD §2.3.1~§2.3.5）
  - `## D-054 hybrid 讀檔 fallback 規範`（**本 skill 獨有 — 詳下方規格**）
  - `## .protocol_version 寫入規範`（phase_log entry 對應 UD §2.3.5）
  - `## 輸入`（scene_id 解析）
  - `## 輸出`（07_scene_tasks/CH<n>_S<m>_台詞任務包.md + D-050 寫檔目錄表）
  - `## 邊界`（D-050 子裁決 1 + 子裁決 2 雙 block 對齊 4 Phase B skill 格式）
  - `## 錯誤處理 / Rollback`
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### /scene-task 差異規格

- **觸發語：** `/scene-task <scene_id>`（接 1 個 user 參數 — scene ID，例：`S-01-03` 或 `CH01_S03`）
- **對應 protocol：** `00_protocol/00_k v0.1 階段 1`（任務包建立段；本 skill 對齊 UD §2.3 為 authoritative 內容；00_k v0.1 5→8 報告 stale 屬 R8-INFO-06 標 INFO 不阻 C.1）
- **UD 權威：** UD v0.5 §2.3.1 ~ §2.3.5（5 個內部子階段；本 skill 直接展開）
- **議題清單動態載入：** **不適用**（/scene-task 不採 D-047 議題對話模式；它是 data assembly skill 從上游實體抽取資訊）
- **創建 entity：** `S-<ch>-<n>` task pack（任務包是 S entity 的 20% completion 衍生物；entity 本身已由 /create-detailed-outline 在 06_a 建立）
- **依賴：** Phase B 完成 — W-rules / V / C-* / R-*-* / P / CH-* 全 ≥ REVIEW（per UD §2.2 啟動條件）
- **下游：** 階段 5 印「下一步建議 D.2.5 任務包 REVIEW gate（人類拍板 task pack → REVIEW + pipeline_state → TASK_REVIEW）→ /dialogue-write」；**不**自動 trigger 任何 gate 或 skill

### 5 階段流程（對齊 UD §2.3 + ARCH §6.1）

#### 階段 1：診斷（依 UD §2.3.1）

agent 行為：
1. 解析 user 輸入的 scene_id（支援 `S-<ch>-<n>` / `CH<n>_S<m>` 兩種格式；統一轉成 canonical `S-<ch>-<n>`）
2. **D-054 hybrid 兩階段 fallback 讀檔（詳「## D-054 hybrid 讀檔 fallback 規範」段）：**
   - 先 check per-scene `<instance_root>/06_scene_index/CH<n>_S<m>_<scene_name>.md`
   - 不存在 → fallback 讀 aggregate `<instance_root>/06_scene_index/06_a_場景索引.md` 對應 row
   - 兩者皆無 → 拒絕（⏸ 條件未滿足；提示 user 先跑 /create-detailed-outline）
3. 讀本場景元資訊：場景名 / 出場角色 C-* 清單 / 地點時間 / 章節
4. 檢查所有先決實體狀態（W / V / C / R / P / CH）— 任何 < REVIEW 列警示
5. 從 `05_d 資訊揭露表 §各章節資訊狀態 §CH-<n>` 抽本場「必須透露 / 禁止透露」候選
6. 從 `05_e 伏筆與回收表 §各章節伏筆狀態 §CH-<n>` 抽本場伏筆候選

印「診斷報告」貼 chat，含：
- 場景元資訊
- 先決實體狀態（含警示）
- 候選資訊揭露 / 伏筆清單
- 候選任務包欄位草稿（agent 預填）
- 讀檔來源（per-scene vs aggregate；D-054 fallback 結果）

#### 階段 2：探索（從各實體抽取資訊，依 UD §2.3.2）

agent 從以下來源抽取本場必要資訊：

| 來源 | 抽取內容 | 填入任務包欄位 |
|---|---|---|
| `W-rules`（01_a） | 本場需要的世界規則摘要 | 「世界規則約束」段 |
| `W-language`（01_b、01_c） | 本場相關陣營 / 階級的語言層級摘要 | 「語言層級」段 |
| `V`（02_a/b/c） | 本場禁用詞 / 慎用詞 / 解禁詞 | 「禁用詞與禁用句型」段 |
| `C-*`（聲線卡） | 出場角色的聲線卡引用 + 偏移檢查重點 | 「出場角色聲線卡引用」段 |
| `R-*-*`（04_a / 04_b） | 本場相關關係的當前狀態 + 稱呼規則 + 禁語 | 「本場關係狀態」段 |
| `05_b 章節結構模板` | 本章節節奏（high/mid/low） | 「章節節奏」段 |
| `05_c 角色弧線表` | 本場每個出場角色當前的弧線階段 | 「角色弧線階段」段 |
| `05_d 資訊揭露表` | 該章節該透露 / 禁止透露的清單 | 「必須透露資訊」+「禁止透露資訊」段 |
| `05_e 伏筆與回收表` | 本場潛伏的伏筆 / 回收任務 | 「潛伏的伏筆」段 |
| 作品專屬 `00_b §6` | 若本場是高風險場景，對應的處理規則 | 「風格要求」段（自動貼） |

#### 階段 3：收斂（依 UD §2.3.3）

agent 行為：
1. 把抽取的資料整合成任務包草稿，依 07_a 模板填寫
2. 缺漏欄位標 TODO
3. 印「收斂預告稿」給 user，含：
   - 任務包 markdown 預覽
   - TODO 欄位清單
   - 缺哪些欄位影響哪些下游 QA
4. 詢問 user：「要補哪些 TODO？或是否接受帶 TODO 直接寫檔？」

允許的 user 回應：
- `通過` / `OK` / `寫檔`：接受帶 TODO 寫檔，進階段 4
- 補 TODO 內容：agent 整合後重印收斂預告稿
- `中止` / `取消`：停止不寫檔

#### 階段 4：執行（寫檔，依 UD §2.3.4 + SPEC §12.5）

依 SPEC §12.5 / 07_a 模板寫入 `<instance_root>/07_scene_tasks/CH<n>_S<m>_台詞任務包.md`，含完整 frontmatter（M7/M10 對齊）：

```yaml
---
狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CH<n>_S<m> 台詞任務包  
優先級：中  

---
entities: [S-<n>-<m>]
depends_on: [W-rules, V, W-language, <相關 C-*>, <相關 R-*-*>, P, CH-<n>]
weight: {S-<n>-<m>: 1.0}
scene_id: S-<n>-<m>
source_task: null
source_dialogue: null
source_dialogues: null
pipeline_state: TASK_DRAFT
mode_tag: null
qa_decision: null
qa_type: null
---
```

寫檔失敗即 rollback（不留半成品檔）。

**任務包必填欄位（依 SPEC §12.5 + UD §2.10.3 19 大欄位）：**

詳見 SPEC §12.5 完整清單；agent 須驗證以下 6 個核心欄位齊全（缺則下游 /dialogue-write 拒絕；本 skill 允許 TODO 但需明示）：

1. 出場角色（C-* 清單）
2. 必須透露資訊（從 05_d 抽取）
3. 禁止透露資訊（從 05_d 抽取）
4. 出場角色聲線卡引用（03_*/）
5. 角色表層目標（TODO — user 提供）
6. 角色真實目標（TODO — user 提供）

#### 階段 5：驗證（依 UD §2.3.5）

agent 行為：
1. 自動 `/status` — 確認 `S-<n>-<m>` 完成度上升（應從 20% → 35%）
2. 在 `<instance_root>/.protocol_version.phase_log` append 一筆：
   ```yaml
   - phase: scene-task
     date: YYYY-MM-DD
     skill: /scene-task
     status: completed
     scene_id: S-<n>-<m>
     task_path: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
     todo_count: <N>
     read_source: per-scene 或 aggregate  # D-054 fallback 結果
     customizations: []
   ```
3. 印「下一步建議：D.2.5 task review gate（人類拍板任務包 → REVIEW + pipeline_state → TASK_REVIEW）→ /dialogue-write」
4. 印禁止：**不**自動 trigger D.2.5 gate；**不**自動 trigger /dialogue-write

### D-054 hybrid 讀檔 fallback 規範（**本 skill 獨有；對齊 DECISIONS_LOG v2.0 §6.17.2**）

D-054 拍板選 1 Hybrid：aggregate 06_a 預設 + `/iterate-scene --split-to-file` 拆出選項（屬 Phase D 範圍延後實作）。**本 skill 必須含兩階段 fallback 讀檔邏輯：**

```
讀 scene_id S-<ch>-<n> 對應 spec 時，依以下順序：

階段 1：per-scene 檔優先
  1. 計算 per-scene 檔路徑：`<instance_root>/06_scene_index/CH<n>_S<m>_<scene_name>.md`
     - <scene_name> 從 06_a 對應 row 抽取（先掃 06_a 取場景名）；或 user 在 /iterate-scene --split-to-file 時指定的場景名
  2. check 檔是否存在
  3. 若存在 → 讀整檔（per-scene mode）；read_source = "per-scene"
  4. 若不存在 → 進階段 2

階段 2：aggregate 06_a fallback
  1. 讀 `<instance_root>/06_scene_index/06_a_場景索引.md`
  2. 在 06_a 內 grep S-<ch>-<n> 對應 row（依 06_a 表格結構抽取）
  3. 若找到 → 讀對應 row + 標 read_source = "aggregate"
  4. 若 06_a 對應 row 標 `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->` marker（表示已 split 但檔不存在）→ WARN（marker 與檔不一致）+ fallback 讀 06_a row

階段 3：兩者皆無
  → 拒絕（⏸ 條件未滿足 / Prerequisites Not Met）
  → What: 場景 S-<ch>-<n> 找不到對應 spec
  → Where: per-scene 檔不存在 + 06_a 內無對應 row
  → Why: /create-detailed-outline 還沒跑或場景未建立
  → 下一步：請先跑 /create-detailed-outline 建立 S-<ch>-<n>，或檢查 scene_id 拼寫
```

紀錄到 phase_log 的 `read_source` 欄位（per-scene / aggregate）供下游 audit。

**「未來 D-054 迭代條件」追蹤（依 POST_LOCK_PENDING NEW_REQ_15）：** 若 user 在 Phase C/D 期間多次拆檔（trigger B ≥ 5 次）或反映「想全 per-scene」（trigger A）— 下一輪 master 可開 D-056+ 重新評估（議題號原預留為 D-055；§6.18.2 順延）。本 skill **不**主動觸發拆檔；拆檔屬 `/iterate-scene --split-to-file` Phase D scope。

### 啟動前檢查（對齊 D-051 後單 marker + Bootstrap completed + Phase C 啟動條件）

```
Before Stage 1, verify (對齊 00_k v0.1 階段 1 啟動段 + UD §2.2):

- current folder is the Instance repo root（含 00_protocol/ / 01_world/ ~ 09_quality_assurance/ 等目錄）
- `.protocol_version` 存在 + phase_log 含 bootstrap entry status=completed（依 D-042）
- `_design/expected_entities.yaml` 存在
- **(D-051 後 active 單 marker)** no `.template_root` marker file exists at repo root
- **(D-042 既有)** `.protocol_version.phase_log` 不含本場景 scene_id 的 phase: scene-task 已 completed entry（若有 → 拒絕；提示 user 用 /iterate-scene 或刪除後重跑）
- 對應上游 entity 至少 REVIEW：
  - W-rules / V / W-language ≥ REVIEW
  - 本場相關 C-* 全 ≥ REVIEW
  - 本場相關 R-*-* 全 ≥ REVIEW（若有）
  - P ≥ REVIEW
  - 本場相關 CH-<n> ≥ REVIEW
- D-054 hybrid 讀檔 fallback 啟動條件（per-scene 檔 OR 06_a row 存在；詳「## D-054 hybrid 讀檔 fallback 規範」段）
```

對應拒絕文案參考 init-project SKILL.md v0.3「⏸ 條件未滿足」格式 — 含 What / Where / Why / 下一步。

### .protocol_version 寫入規範

At Stage 1 start, append or prepare an in-progress entry. At successful Stage 5 completion, update the same entry to completed.

Use concrete entity IDs only. Do not write wildcard IDs such as `S-*`.

```yaml
- phase: scene-task
  date: <ISO date>
  skill: /scene-task
  status: completed
  scene_id: S-<n>-<m>
  task_path: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
  todo_count: <N>          # 0 表全欄位齊；> 0 表帶 TODO 寫檔
  read_source: per-scene 或 aggregate   # D-054 fallback 結果
  customizations: []
```

If aborted, set `status: aborted`, include `abort_reason`, and do not count the task pack as created.

### 輸入

The user provides:
- `/scene-task <scene_id>` — scene_id 支援 `S-<ch>-<n>` 或 `CH<n>_S<m>` 格式
- 階段 3 TODO 補入 / 修改建議 / 通過 / 中止
- 階段 4 寫檔前最後確認

### 輸出

Runtime output includes:
- 階段 1 診斷報告（chat-only）
- 階段 2 探索抽取摘要（chat-only）
- 階段 3 收斂預告稿（chat-only）
- 階段 4 file write only after user approval
- 階段 5 /status validation + 下一步建議

Runtime file outputs are limited to:
- `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`
- `.protocol_version.phase_log`

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `07_scene_tasks/CH<n>_S<m>_台詞任務包.md` | 主體；S-<n>-<m> 任務包寫檔位置 |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: scene-task` / `scene_id` / `task_path` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `08_dialogue_outputs/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/` | 任何寫入都屬 D-050 越界 |

### 邊界

The skill must not:
- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, or registry Template files
- modify existing Phase A / Phase B skills or wrappers
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scenes, dialogue, or QA reports
- create new `S-*` scene entities（場景由 /create-detailed-outline 建立；本 skill 只建立任務包）
- auto-trigger D.2.5 task review gate / /dialogue-write / /qa
- promote task pack `狀態` to `REVIEW` or beyond（屬 D.2.5 人類 gate scope）
- promote `pipeline_state` from `TASK_DRAFT`（屬 D.2.5 人類 gate scope）
- create new entity types, enum values, schemas, or parser behavior
- overwrite an existing same-scene task pack without explicit user confirmation
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為 `07_scene_tasks/` 一個目錄；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

### 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If a target file becomes `LOCKED` or changes unexpectedly between Stage 3 and Stage 4, stop before writing that file and ask for a decision.

If Stage 4 write fails:
1. Stop further writes.
2. Roll back the partial task pack file if possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly what was written, rolled back, or requires manual inspection.

Do not hide partial-write risk behind a success message.

### 錯誤呈現規則

Use these headings:
- `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems.
- `## ⏸ 條件未滿足 / Prerequisites Not Met` for repository state or prerequisite problems.

Each error must include:
- `What`: what failed.
- `Where`: file, section, command, or stage.
- `Why`: why the skill cannot continue.
- `下一步`: one concrete action the user should take.

For multiple errors, summarize the count first, then list each item. Do not expose stack traces, parser internals, enum keys, or raw YAML objects in user-facing errors.

### 中文 wrapper 內容（場景任務包）

採極簡 wrapper 策略，對齊既有中文 wrapper 風格：

```markdown
---
name: 場景任務包
description: /scene-task 中文別名 — 觸發場景任務包建立流程。實際邏輯參見 .claude/skills/scene-task/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/場景任務包` 中文別名 wrapper
優先級：高

# 中文別名 - 場景任務包

本 skill 是 `/scene-task` 的中文別名。當使用者以 `/場景任務包 <scene_id>` 觸發時，等同於觸發 `/scene-task <scene_id>`。

完整流程、五階段規則、`.protocol_version` schema、D-054 hybrid 讀檔 fallback（per-scene → aggregate）、D-051 後 active 單 marker Template-detect（`.template_root` marker）、rollback 與錯誤處理，全部以 `.claude/skills/scene-task/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/scene-task/SKILL.md`。
```

### 文字長度建議

主 SKILL.md ~400-500 行 markdown（含 5 階段 + D-054 hybrid fallback 規範 + D-050 雙 block + 啟動前檢查 + phase_log schema + 錯誤處理）；中文 wrapper ~30 行（極簡）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§D.2 + §D.2.5 dependency）
2. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3 全 5 子階段（**本 skill 主要 reference**）+ §2.10.3 19 大欄位 + §2.2 啟動條件
3. `_design/SPEC.md` v1.2 §5.1 entity / §5.3 完成度 / §12.3 場景狀態機 / §12.5 任務包必填欄位
4. `_design/ARCHITECTURE.md` v1.6 §3.2 wrapper / §3.3 skill 規範 / §3.3.0 multi-agent / §3.3.1 錯誤呈現 / §3.3.2 D-051 後 single marker / §6.1 /scene-task 內部架構
5. `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 / §6.13.2 D-051 / §6.16.2 D-053 / **§6.17.2 D-054**（per-scene 檔 convention Hybrid 拍板 — 本 skill 必對齊）

B. 對齊依據（reference templates）
6. `_design/POST_LOCK_PENDING.md` v0.10（NEW_REQ_13 RESOLVED via D-054 + NEW_REQ_15 未來迭代追蹤）
7. `_design/D054_DECISION_PACKAGE.md` v0.2（拍板包；含完整 hybrid 設計推理）
8. `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 1（context；註：00_k v0.1 5→8 報告 stale 屬 R8-INFO-06 — 本 skill 不直接 ref 8 報告段，改 ref UD §2.5.3 v0.3）
9. `00_protocol/00_a_台詞生產協議.md`（§3.3 診斷模式 — 階段 1 用）
10. `_design/registries/issue_type_registry.template.yaml` v0.1（context only — 本 skill 不採 D-047 議題對話模式）
11. `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 上游 — 寫 06_a；本 skill 讀 06_a fallback）
12. `.claude/skills/init-project/SKILL.md` v0.3（D-051 後 single marker 範式）
13. `.claude/skills/status/SKILL.md`（階段 5 自動呼叫範式）
14. 5 個 /create-* SKILL.md v0.3 / v0.1（D-050 子裁決 1+2 雙 block body 格式範式）

C. 必讀模板 / 既有檔
15. `07_scene_tasks/07_a_單場台詞任務包模板.md`（任務包格式範本；本 skill 階段 4 寫檔依此）
16. `06_scene_index/06_a_場景索引模板.md`（aggregate fallback 讀檔來源範本）

D. 已 LOCKED 不可動文件
17. 所有 `_design/*.md` 既有 spec（含 PHASE_B_COMPLETION_REPORT / 3 個 phase_b review_log / Round 1-10 review report 全部）
18. `scripts/*.py`
19. 既有 27 模板（01_world/ ~ 09_quality_assurance/ 內 — 含 07_a 模板）
20. 所有 `00_protocol/` 檔（含 00_k v0.1；本 skill 不 patch 00_k 即使有 R8-INFO-06 stale）
21. `_tools/frontend/*` 全部
22. 既有 13 個 SKILL.md（init-project / create-* x5 / status / check-gaps / 5 中文 wrapper / 建立世界觀）
23. `.template_root` marker / AGENTS.md / CLAUDE.md / `_user_manual/skill_invocation_guide.md`
24. D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.10 / D054_DECISION_PACKAGE v0.2 — 本 skill reference 但不改）

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/scene-task/SKILL.md` v0.1
2. `.claude/skills/場景任務包/SKILL.md` v0.1

不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name + description）+ 中文 5 必填 header + markdown 主體
- 中文 wrapper 引用英文主檔為權威 + 不展開第二套流程

B. 內容（英文主 SKILL.md）
- 5 階段流程對齊 UD §2.3.1~§2.3.5
- **D-054 hybrid 讀檔 fallback 規範段完整**（per-scene → aggregate 兩階段 + 拒絕 fallback；對齊 DECISIONS_LOG v2.0 §6.17.2）
- 啟動前檢查含 D-051 後 single marker（不要寫「D-049 兩道防線」— stale）+ Bootstrap completed + 上游 entity REVIEW check（W/V/C/R/P/CH）
- phase_log entry 含 `phase: scene-task` + `scene_id` + `task_path` + `todo_count` + `read_source`（D-054 fallback 結果）+ `status: completed`
- 觸發語對應正確（/scene-task <scene_id>；支援 S-<ch>-<n> + CH<n>_S<m> 兩格式）
- 寫檔目錄嚴格限 `07_scene_tasks/`（D-050 子裁決 2 對齊）
- 邊界含 D-050 子裁決 1 + 子裁決 2 雙 block 對齊 4 Phase B skill 格式 + 含 D-053 exception 雙 list +「本 skill 不在例外範圍」
- 不自動 trigger D.2.5 gate / /dialogue-write / /qa
- 不擅升 task pack 狀態（屬 D.2.5 人類 gate scope）

C. 不破壞既有
- 不動既有 13 SKILL.md / .claude/skills 結構
- 不動 27 模板 / 00_protocol/ / _design/ 既有 spec（含 00_k v0.1 — R8-INFO-06 stale 不處理）
- 不動 D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.10 / D054_DECISION_PACKAGE v0.2）
- `python scripts/check_headers.py` 0 ERROR 維持
- `check_paths.py` baseline +0 增量

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** /scene-task 5 階段不對齊 UD §2.3 OR D-054 hybrid fallback 邏輯缺失 → 修補 round

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX C.1 完成 → user commit/push → 回 master：

1. master 進 Phase C Wave 9 C.2 task（寫 `CODEX_C2_STARTER.md` 給 user 跑 /dialogue-write skill 實作）
2. **C.1 → C.2 → C.3 依序不可平行**（依賴鏈：/scene-task 產出 task pack → /dialogue-write 讀 task pack 寫台詞 → /qa 讀台詞寫 QA）
3. 3 個 skill 全 DONE 後進 Wave 11 — 整體驗收 + 寫 PHASE_C_COMPLETION_REPORT.md → Milestone 3 達成

**M3 user-test 第三次點時機（依 HANDOFF §7.3）：** Milestone 3 達成後可做 M3 user-test — 對任一 Phase B 建好的場景跑 /scene-task → /dialogue-write → /qa 完整 chain。

---

# 3. 文件維護紀律

- 本檔是 Phase C Wave 9 C.1 起手 starter；完成後可 archive 進 `_design/archive/`
- ⚠ /scene-task 是下游 pipeline 第一個 skill；對齊 D-054 hybrid 設計直接影響 user 創作體驗
- ⚠ 00_k v0.1 5→8 報告 stale (R8-INFO-06) 不在本 starter 處理範圍；C3 starter 或 future patch round 處理

---

# 4. Cross-ref

- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0 §3 Phase C Wave 9 規劃
- `_design/TASKS.md` v1.9 §D.2（/scene-task task spec）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3（5 階段細節）
- `_design/SPEC.md` v1.2 §12.3 / §12.5
- `_design/ARCHITECTURE.md` v1.6 §6.1
- `_design/DECISIONS_LOG.md` v2.0 §6.17.2 D-054（hybrid fallback 拍板）
- `_design/POST_LOCK_PENDING.md` v0.10 NEW_REQ_13 RESOLVED + NEW_REQ_15
- `_design/D054_DECISION_PACKAGE.md` v0.2
- `00_protocol/00_k_台詞生產流程協議.md` v0.1（context；R8-INFO-06 stale 不本輪處理）
- `_design/CODEX_WAVE7_SKILLS_STARTER.md` v0.1（Wave 7 起手 starter 模板參考）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 上游 — 寫 06_a）
- `07_scene_tasks/07_a_單場台詞任務包模板.md`（07_a 任務包格式範本）
