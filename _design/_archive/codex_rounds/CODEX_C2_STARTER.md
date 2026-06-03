狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：Phase C Wave 9 task — /dialogue-write skill + 中文 wrapper 實作（含三模式：試寫/破格/收斂 + SINGLE_ITER；D.2.5 + D.3.5 gate 對齊）  
優先級：高

# CODEX_C2_STARTER — Phase C Wave 9 C.2：/dialogue-write skill 實作

# 0. 本檔用途

Phase C Wave 9 第二條 task — 實作 `/dialogue-write` skill（下游台詞生產 pipeline 的第二個 skill；依任務包寫多版本台詞 + 收斂 + 單版迭代）。對齊 TASKS v1.9 §D.3 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.4 + §4 + 00_protocol/00_k v0.1 階段 2 + ARCH §6.2。

**前置條件：** C.1 PASS（/scene-task SKILL.md + 中文 wrapper 已落地）+ D.2.5 task review gate 概念已存在於 spec（本 skill 啟動時 check）。

**C.2 PASS → Phase C Wave 9 進 C.3 /qa skill 實作**（依賴鏈：/scene-task → /dialogue-write → /qa）

⚠ **D-054 影響：** **本 skill 不直接受 D-054 hybrid 拍板影響**（讀 task pack 直接，不讀 06_scene_index）— 但若任務包在 source 引用 per-scene 06_scene_index 檔，agent 應沿用 task pack 內的 source_task 路徑直接 resolve。

⚠ **mode_tag enum 擴充對齊 D-027 + REQUIREMENTS_LOCK §4.3：**
- 既有 5 種：`DRAFT_TRIAL` / `EXPERIMENTAL` / `CONVERGENCE` / `FINAL_CANDIDATE` / `FINAL`
- 新增 `SINGLE_ITER`（partial supersede P-010 — 改用 `/dialogue-write --single-iter` 參數而非新 skill；對齊 REQUIREMENTS_LOCK §4.3 + D-027 mode_tag 可擴充）

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase C Wave 9 C.2 task」— 實作 /dialogue-write skill（含中文 wrapper）；對齊 TASKS v1.9 §D.3 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.4 + §4 + 00_protocol/00_k v0.1 階段 2 + ARCH §6.2。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase C Wave 9 第二條 task（C.1 → C.2 → C.3 依序）；/dialogue-write 是下游 pipeline 第二個 skill
- C.2 PASS → 可進 C.3 /qa skill 實作

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_k v0.1；它含 5 報告 stale 屬 R8-INFO-06 — 本 skill 直接 reference UD §2.4/§4 為權威）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 SKILL.md（含 C.1 /scene-task + 中文 wrapper）
- ✗ **不**寫 /qa（C.3 scope）
- ✗ **不**自動 trigger D.3.5 收斂版人類選版 gate（屬人類 task）
- ✗ **不**跑真實 /dialogue-write 寫檔（會污染 Template；端到端測試屬 user 親跑 M3）
- ✗ **不**新增 mode_tag enum 值（除既有 5 種 + SINGLE_ITER）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §D.3（line 1723-1827）+ UD v0.5 §2.4 五個內部子階段 + UD §4 三模式 algorithm 細節 + REQUIREMENTS_LOCK §4.3 SINGLE_ITER mode 新增。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/dialogue-write/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/生成台詞/SKILL.md` | 中文 wrapper |

### /dialogue-write 主 SKILL.md 結構

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；含三模式 + D.2.5 gate dependency mention）
- 中文 5 必填 header
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（英文 slash command + 4 種輸入模式 + 中文別名 reference）
  - `## 觸發協議`（對應 00_k v0.1 階段 2 + UD §2.4/§4 + 必讀 references）
  - `## 啟動前檢查`（D-051 後 single marker + Bootstrap completed + D.2.5 task review gate check + task pack 核心欄位 check）
  - `## 流程`（6 階段對應 UD §2.4.1~§2.4.7；含可選探索 + 必跑試寫 + 可選破格 + 收斂 + 驗證）
  - `## 4 模式詳細 algorithm`（試寫 v01A/B/C / 破格 v01D / 收斂 v02 / SINGLE_ITER；對齊 UD §4.2~§4.6）
  - `## 輸入鎖定（O6 + M8 contract）`（4 種輸入形態：A. 試寫預設 / B. 破格 / C. 收斂 --converge / D. SINGLE_ITER --single-iter）
  - `## TODO 拒絕條件量化（O5）`（6 核心欄位缺則拒絕）
  - `## .protocol_version 寫入規範`（phase_log entry 對應 UD §2.4.7）
  - `## 輸入`
  - `## 輸出`（08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A/B/C/D/v02.md + D-050 寫檔目錄表）
  - `## 邊界`（D-050 子裁決 1 + 子裁決 2 雙 block）
  - `## 錯誤處理 / Rollback`
  - `## 錯誤呈現規則`

### /dialogue-write 差異規格

- **觸發語：** 4 種輸入模式（詳「## 輸入鎖定」段）：
  - `/dialogue-write <task_path | scene_id>` — 試寫預設（產 v01A/B/C 三版本）
  - `/dialogue-write <input> --experimental` — 破格（產 v01D EXPERIMENTAL）
  - `/dialogue-write <task_input> --converge <v01A_path> <v01B_path> [...]` — 收斂（產 v02 CONVERGENCE；需 ≥2 trial 路徑）
  - `/dialogue-write <task_input> --single-iter` — 單版迭代（產 v01-iter SINGLE_ITER；user 跟 agent 迴圈改）
- **對應 protocol：** `00_protocol/00_k v0.1 階段 2`（本 skill 對齊 UD §2.4 + §4 為 authoritative；00_k 5→8 報告 stale 屬 R8-INFO-06 不本輪處理）
- **UD 權威：** UD v0.5 §2.4（5+ 內部子階段框架）+ UD §4（三模式 algorithm；§4.2 試寫 / §4.3 收斂 / §4.4 破格 / §4.5 跨模式狀態總表 / §4.6 與資料格式假設對齊）
- **議題清單動態載入：** **不適用**（/dialogue-write 不採 D-047 議題對話模式；它讀 task pack 直接寫台詞）
- **創建 entity：** 衍生物（台詞檔；不創新 S-* entity；task pack 引用既有 S entity）
- **依賴：** 
  - task pack `狀態=REVIEW` **AND** `pipeline_state=TASK_REVIEW`（D.2.5 gate 完成）
  - task pack 6 核心欄位齊（依 SPEC §D.3 量化）
- **下游：** 階段 6 印「下一步建議 D.3.5 收斂版人類選版 gate（path A 推薦：人類挑亮點 + --converge / path B 例外：直接 /qa）」；**不**自動 trigger

### 6 階段流程（對齊 UD §2.4 + ARCH §6.2）

#### 階段 1：診斷（依 UD §2.4.2）

agent 行為：
1. 解析 user 輸入（4 種輸入模式之一）
2. 讀 task pack：
   - 試寫 / 破格 / SINGLE_ITER 模式：從 user 輸入或 scene_id 找對應 task pack
   - 收斂模式：從 user 輸入找 task pack + 驗 ≥2 個 trial 路徑
3. 檢查 task pack `狀態=REVIEW` AND `pipeline_state=TASK_REVIEW`（D.2.5 完成證據）
4. 檢查 task pack 6 核心欄位齊（依「## TODO 拒絕條件量化」段）：
   - 出場角色
   - 必須透露資訊
   - 禁止透露資訊
   - 出場角色聲線卡引用
   - 角色表層目標
   - 角色真實目標
5. 任一核心欄位缺 → 拒絕（⏸ 條件未滿足；提示 user 補 task pack 後重跑）
6. 列出非核心 TODO 欄位（不阻擋執行；記錄到 phase_log）

印「診斷報告」貼 chat。

#### 階段 2：探索（可選；依 UD §2.4.3）

僅當 user 明示「跑探索」才執行：
- 產 1-2 段短篇探索片段（語氣方向實驗，不寫檔）
- 印給 user「這幾個方向哪個比較對」
- user 選定後進階段 3 試寫

#### 階段 3：試寫（主流程；依 UD §2.4.4 + §4.2）

**試寫模式（預設）—** 依 SPEC §12.6 多版本方向規範產 3 版本（對齊 00_a §3.6）：

| 版本 | 方向 | 句長偏好 | 潛台詞密度 | 攻防強度 | 情緒外露 |
|---|---|---|---|---|---|
| v01A | 克制、短句、強潛台詞 | 短 | 高 | 中 | 低 |
| v01B | 攻防更強、衝突更尖 | 中 | 中 | 高 | 中 |
| v01C | 情緒更重、但避免直說 | 中—長 | 中—高 | 中 | 中—高 |

任務包可在「輸出模式要求」欄擴充版本方向（v01D / v01E / v01F）— 常見擴充：詩化 / 口語 / 黑色幽默。

每版本依 08_b 模板生成，frontmatter（依 SPEC §5.2 + M7/M10）：

```yaml
---
entities: [S-<n>-<m>]
depends_on: [<本場相關 C-*, R-*-*>]
weight: {S-<n>-<m>: 1.0}
scene_id: S-<n>-<m>
source_task: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
source_dialogue: null
source_dialogues: null
pipeline_state: DIALOGUE_TRIAL
mode_tag: DRAFT_TRIAL
qa_decision: null
qa_type: null
---
```

#### 階段 4：破格（可選；依 UD §2.4.5 + §4.4）

僅當 user 明示「跑破格」`--experimental` 才執行：
- 依 00_a §3.7 破格模式產 v01D
- frontmatter：`mode_tag: EXPERIMENTAL`、`pipeline_state: DIALOGUE_TRIAL`、`狀態: DRAFT`
- **不**混入正式 v01A/B/C

#### 階段 5：收斂（D.3.5 gate 觸發 + --converge 模式；依 UD §2.4.6 + §4.3）

僅當 user 明示 `--converge <v01A_path> <v01B_path> [...]` 模式才執行：
- 接受 task pack 輸入 + **2 個以上既有 trial 版本路徑**
- **不**重新試寫（跳過階段 3）；直接整合既有 trial 為 v02
- 寫入 `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v02.md`
- frontmatter：`狀態: REVIEW`、`pipeline_state: DIALOGUE_CONVERGED`、`mode_tag: CONVERGENCE`、`source_dialogues: [v01A_path, v01B_path, ...]`（複數欄位）

#### 階段 5a：SINGLE_ITER（可選；REQUIREMENTS_LOCK §4.3 + D-027）

僅當 user 明示 `--single-iter` 才執行：
- agent 寫一版（v01-iter）→ user 跟 agent chat 迴圈改 → user 拍板 OK
- frontmatter：`狀態: DRAFT`、`pipeline_state: DIALOGUE_TRIAL`、`mode_tag: SINGLE_ITER`、`source_dialogues: null`
- 寫入 `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01-iter.md`
- SINGLE_ITER 不走收斂；user 認可後直接走 QA → FINAL gate

#### 階段 6：驗證（依 UD §2.4.7）

agent 行為：
1. 自動 `/status` — 確認 `S-<n>-<m>` 完成度上升（試寫 → 60% / 收斂 → 75% / SINGLE_ITER → 60%）
2. 在 `<instance_root>/.protocol_version.phase_log` append 一筆：
   ```yaml
   - phase: dialogue-write
     date: YYYY-MM-DD
     skill: /dialogue-write
     status: completed
     scene_id: S-<n>-<m>
     dialogue_paths: [<v01A 路徑>, <v01B 路徑>, <v01C 路徑>]  # 或單路徑 if 收斂/破格/SINGLE_ITER
     mode_tag: DRAFT_TRIAL  # 或 CONVERGENCE / EXPERIMENTAL / SINGLE_ITER
     converge_sources: null  # 若 mode_tag=CONVERGENCE 則填 [v01A_path, v01B_path, ...]
   ```
3. 印「下一步建議」依 mode_tag 不同：
   - **DRAFT_TRIAL：** 「人類挑亮點 + 跑 `/dialogue-write --converge` (D.3.5 gate)」或「（例外路徑 B）直接跑 /qa」
   - **EXPERIMENTAL：** 「保留為實驗版本；不進 v01A/B/C；可獨立跑 /qa 或丟棄」
   - **CONVERGENCE：** 「人類確認後跑 /qa」
   - **SINGLE_ITER：** 「user 跟 agent 迴圈改完後跑 /qa」
4. 印禁止：**不**自動 trigger D.3.5 gate / /qa

### 輸入鎖定（O6 + M8 `--converge` contract）

`/dialogue-write` 接受以下輸入形態，其他拒絕：

**A. 試寫模式（預設）：**
1. 完整任務包檔案路徑：`/dialogue-write 07_scene_tasks/CH01_S03_台詞任務包.md`
2. scene_id：`/dialogue-write S-01-03`（從 06_a 或 per-scene 06_scene_index 推導任務包路徑）
3. 無參數：使用上一輪 /scene-task 產出的任務包

→ 產 v01A/B/C，`pipeline_state: DIALOGUE_TRIAL`、`mode_tag: DRAFT_TRIAL`

**B. 破格模式：**
`/dialogue-write <輸入> --experimental` → 產 v01D，`mode_tag: EXPERIMENTAL`

**C. 收斂模式（M8 + #7 釐清）：**
`/dialogue-write <任務包輸入> --converge <v01A_path> <v01B_path> [...]` → 產 v02 收斂版

輸入規則：
- 必須含 1 個任務包輸入（A 的三種形態之一）+ **2 個以上既有 trial 版本路徑**
- 收斂模式**不再重新試寫**（跳過試寫階段），但**必須引用既有 trial 檔**作為素材
- 若 user 只提供任務包而無 trial 路徑 → 拒絕並提示「請先跑試寫模式產 trial 版本，或提供既有 trial 路徑」

**D. SINGLE_ITER 模式（D-027 + REQUIREMENTS_LOCK §4.3）：**
`/dialogue-write <輸入> --single-iter` → 產 v01-iter，`mode_tag: SINGLE_ITER`、`pipeline_state: DIALOGUE_TRIAL`

→ user 跟 agent chat 迴圈改 → user 拍板 OK 後可直接跑 /qa（不走收斂）

### TODO 拒絕條件量化（O5）

任務包以下「核心欄位」缺任一即拒絕：
- 出場角色
- 必須透露資訊
- 禁止透露資訊
- 出場角色聲線卡引用
- 角色表層目標
- 角色真實目標

（非核心欄位的 TODO 不阻擋執行，但會在報告中列出 + phase_log 標 `incomplete_fields: [...]`）

### 啟動前檢查

```
Before Stage 1, verify:

- current folder is the Instance repo root
- `.protocol_version` 存在 + phase_log 含 bootstrap entry status=completed
- `_design/expected_entities.yaml` 存在
- **(D-051 後 active 單 marker)** no `.template_root` marker file exists at repo root
- task pack `狀態=REVIEW` AND `pipeline_state=TASK_REVIEW`（D.2.5 gate 完成證據；不齊 → 拒絕並提示「需先過 D.2.5 task review gate」）
- task pack 6 核心欄位齊（依「## TODO 拒絕條件量化」段）
- 對應上游 entity 至少 REVIEW（依任務包 depends_on 列；任一缺 REVIEW → 拒絕或 `prereq_waived: true` 例外路徑）
- 若 `--converge` 模式：≥2 個 trial 版本路徑提供 + 對應檔存在
- 若 `--single-iter` 模式：task pack 6 核心欄位齊（同預設）
```

對應拒絕文案參考 init-project SKILL.md v0.3「⏸ 條件未滿足」格式。

### .protocol_version 寫入規範

詳「## 階段 6：驗證」段 phase_log entry 範例。Use concrete entity IDs only.

### 輸入

詳「## 輸入鎖定」段。

### 輸出

Runtime output includes:
- 階段 1 診斷報告（chat-only）
- 階段 2 探索片段（chat-only；如執行）
- 階段 3 試寫版本（v01A/B/C 寫檔 only after user approval）
- 階段 4 破格版本（v01D 寫檔 if --experimental）
- 階段 5 收斂版本（v02 寫檔 if --converge）
- 階段 5a SINGLE_ITER 版本（v01-iter 寫檔 if --single-iter）
- 階段 6 /status validation + 下一步建議

Runtime file outputs are limited to:
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A.md` / `v01B.md` / `v01C.md` / `v01D.md` / `v02.md` / `v01-iter.md`
- `.protocol_version.phase_log`

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v*.md` | 主體；台詞檔（trial / experimental / converged / single_iter）|
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: dialogue-write` / `scene_id` / `dialogue_paths` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `09_quality_assurance/`, `10_art_assets/`, `00_protocol/` | 任何寫入都屬 D-050 越界 |
| 不改 | `07_scene_tasks/CH<n>_S<m>_台詞任務包.md` | 任務包屬 /scene-task scope；本 skill 只讀不改 |

### 邊界

The skill must not:
- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, registry Template files
- modify existing Phase A / Phase B / Phase C C.1 skills or wrappers
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scenes, task packs, or QA reports
- modify the task pack file（task pack 屬 /scene-task scope；本 skill 只讀）
- auto-trigger D.3.5 review gate / /qa
- promote dialogue 狀態 to `REVIEW`, `FINAL`, or `LOCKED`（除收斂版自動標 REVIEW；FINAL/LOCKED 屬 D.4 後人類 gate scope）
- promote `pipeline_state` to `QA_PASSED` / `QA_FAILED` / `DIALOGUE_FINAL`（屬 /qa + 人類 gate scope）
- create new entity types, enum values, schemas, or parser behavior
- write破格版混入正式 v01A/B/C（必須標 mode_tag=EXPERIMENTAL）
- 跳過核心欄位拒絕邏輯
- 擅自刪除 user 標記「保留」的句子
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為 `08_dialogue_outputs/` 一個目錄；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

### 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If task pack 6 核心欄位缺 → 拒絕；提示 user 補 task pack 後重跑（不啟 D.2.5 重審）。

If a target file becomes `LOCKED` between Stage 3-5 and write, stop and ask for decision.

If any Stage 3/4/5/5a write fails:
1. Stop further writes.
2. Roll back files written by this skill in the current run when possible.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly which files were written, rolled back, or require manual inspection.

### 錯誤呈現規則

Use `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems and `## ⏸ 條件未滿足 / Prerequisites Not Met` for state problems. Each error includes What / Where / Why / 下一步.

### 中文 wrapper 內容（生成台詞）

```markdown
---
name: 生成台詞
description: /dialogue-write 中文別名 — 觸發台詞生成（試寫 v01A/B/C / 破格 / 收斂 / 單版迭代）流程。實際邏輯參見 .claude/skills/dialogue-write/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/生成台詞` 中文別名 wrapper
優先級：高

# 中文別名 - 生成台詞

本 skill 是 `/dialogue-write` 的中文別名。當使用者以 `/生成台詞 <input>` 觸發時，等同於觸發 `/dialogue-write <input>`。

完整流程、6 階段規則、4 模式（試寫 / 破格 / 收斂 / SINGLE_ITER）、`.protocol_version` schema、D.2.5 task review gate dependency、rollback 與錯誤處理，全部以 `.claude/skills/dialogue-write/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/dialogue-write/SKILL.md`。
```

### 文字長度建議

主 SKILL.md ~500-600 行 markdown（含 6 階段 + 4 模式 algorithm + 輸入鎖定 + D-050 雙 block + 啟動前檢查 + phase_log schema + 錯誤處理）；中文 wrapper ~30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§D.3 + §D.2.5 dependency + §D.3.5 收斂 gate dependency）
2. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.4 全 5+ 子階段 + §4 三模式 algorithm 細節（**本 skill 主要 reference**）
3. `_design/SPEC.md` v1.2 §12.3 場景狀態機 / §12.6 多版本方向規範 / §D.3 TODO 拒絕條件量化
4. `_design/ARCHITECTURE.md` v1.6 §6.2 /dialogue-write 內部架構 / §3.3.1 錯誤呈現 / §3.3.2 D-051 後 single marker
5. `_design/REQUIREMENTS_LOCK.md` v1.0 §4.3（SINGLE_ITER mode 新增 — partial supersede P-010）
6. `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 / §6.13.2 D-051 / §6.16.2 D-053 / §6.17.2 D-054（context only — 本 skill 不直接受影響）

B. 對齊依據（reference templates）
7. `_design/POST_LOCK_PENDING.md` v0.10（NEW_REQ 整體狀態）
8. `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 2（context；註：00_k v0.1 5→8 報告 stale 屬 R8-INFO-06 — 本 skill 不 ref 8 報告段，C.3 starter 處理）
9. `00_protocol/00_a_台詞生產協議.md`（§3.5 探索模式 / §3.6 試寫模式 / §3.7 破格模式 / §3.8 收斂模式）
10. `.claude/skills/scene-task/SKILL.md` v0.1（C.1 上游 — 寫 task pack；本 skill 讀 task pack）
11. `.claude/skills/init-project/SKILL.md` v0.3（D-051 後 single marker 範式）
12. 5 個 /create-* SKILL.md v0.3 / v0.1（D-050 子裁決 1+2 雙 block body 格式範式）

C. 必讀模板 / 既有檔
13. `07_scene_tasks/07_a_單場台詞任務包模板.md`（task pack 格式範本；本 skill 讀此）
14. `08_dialogue_outputs/08_b_單場台詞模板.md`（dialogue 檔格式範本；本 skill 階段 3/4/5/5a 寫此）

D. 已 LOCKED 不可動文件
15. 所有 `_design/*.md` 既有 spec（含 Phase B/C 既有 starter / completion report）
16. `scripts/*.py`
17. 既有 27 模板（含 07_a / 08_b）
18. 所有 `00_protocol/` 檔（含 00_k v0.1；本 skill 不 patch）
19. `_tools/frontend/*` 全部
20. 既有 SKILL.md（init-project / create-* x5 / status / check-gaps / 6 中文 wrapper / scene-task / 場景任務包）
21. `.template_root` marker / AGENTS.md / CLAUDE.md / skill_invocation_guide.md

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/dialogue-write/SKILL.md` v0.1
2. `.claude/skills/生成台詞/SKILL.md` v0.1

不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name + description）+ 中文 5 必填 header + markdown 主體
- 中文 wrapper 引用英文主檔為權威 + 不展開第二套流程

B. 內容（英文主 SKILL.md）
- 6 階段流程對齊 UD §2.4.1~§2.4.7
- 4 模式 algorithm 對齊 UD §4.2（試寫）/ §4.3（收斂）/ §4.4（破格）+ REQUIREMENTS_LOCK §4.3（SINGLE_ITER）
- 啟動前檢查含 D-051 後 single marker + Bootstrap completed + D.2.5 gate check（task pack 狀態=REVIEW + pipeline_state=TASK_REVIEW）+ 6 核心欄位 check
- 輸入鎖定 4 形態（A. 試寫預設 / B. --experimental / C. --converge / D. --single-iter）+ 收斂模式 ≥2 trial 路徑要求
- phase_log entry 含 `phase: dialogue-write` + `scene_id` + `dialogue_paths` + `mode_tag` + `status: completed`
- 寫檔目錄嚴格限 `08_dialogue_outputs/`（D-050 子裁決 2 對齊）
- 邊界含 D-050 子裁決 1 + 子裁決 2 雙 block 對齊 4 Phase B skill 格式
- 不自動 trigger D.3.5 gate / /qa
- 不擅升 dialogue 狀態（除收斂版自動標 REVIEW）
- mode_tag 6 種 enum（DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / FINAL_CANDIDATE / FINAL / SINGLE_ITER）

C. 不破壞既有
- 不動既有 SKILL.md（含 C.1 /scene-task）
- 不動 27 模板 / 00_protocol/ / _design/ 既有 spec
- `python scripts/check_headers.py` 0 ERROR 維持
- `check_paths.py` baseline +0 增量

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 6 階段不對齊 UD §2.4 OR 4 模式 algorithm 缺失 OR 輸入鎖定 4 形態不完整 → 修補 round

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX C.2 完成 → user commit/push → 回 master：

1. master 進 Phase C Wave 9 C.3 task（寫 `CODEX_C3_STARTER.md` 給 user 跑 /qa skill 實作 + 處理 R8-INFO-06 00_k v0.1 5→8 報告 stale）
2. C.1 → C.2 → C.3 依序不可平行
3. 3 個 skill 全 DONE 後進 Wave 11 整體驗收

---

# 3. 文件維護紀律

- 本檔是 Phase C Wave 9 C.2 起手 starter；完成後可 archive
- ⚠ /dialogue-write 是台詞生產核心 skill；4 模式設計影響 user 創作體驗
- ⚠ 00_k v0.1 5→8 報告 stale (R8-INFO-06) 不本輪處理；C3 starter 處理

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §D.3 + §D.2.5 + §D.3.5
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.4 + §4
- `_design/SPEC.md` v1.2 §12.3 / §12.6 / §D.3
- `_design/ARCHITECTURE.md` v1.6 §6.2
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.3（SINGLE_ITER）
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 / §6.13.2 / §6.16.2 / §6.17.2（context）
- `_design/POST_LOCK_PENDING.md` v0.10
- `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 2（R8-INFO-06 stale 不本輪處理）
- `00_protocol/00_a_台詞生產協議.md`
- `.claude/skills/scene-task/SKILL.md` v0.1（C.1 上游 — task pack 生產）
- `07_scene_tasks/07_a_單場台詞任務包模板.md`
- `08_dialogue_outputs/08_b_單場台詞模板.md`
