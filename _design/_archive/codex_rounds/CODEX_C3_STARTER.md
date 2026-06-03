狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：Phase C Wave 9 task — /qa skill + 中文 wrapper 實作（含 8 報告必跑 D-043 + R8-INFO-06 處理策略）  
優先級：高

# CODEX_C3_STARTER — Phase C Wave 9 C.3：/qa skill 實作

# 0. 本檔用途

Phase C Wave 9 第三條 task — 實作 `/qa` skill（下游台詞生產 pipeline 的最後一個 skill；對台詞跑 8 份 QA 報告）。對齊 TASKS v1.9 §D.4 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.5 + ARCH §6.3 + D-043 8 報告必跑（partial supersede D-018 #3）。

**前置條件：** C.1 PASS + C.2 PASS（/scene-task + /dialogue-write SKILL.md 已落地）+ D.3.5 收斂版 gate 概念已存在於 spec（本 skill 啟動時 check）。

**C.3 PASS → Phase C Wave 9 完 → 進 Wave 11 整體驗收**（Wave 10 由 CODEX 跑 3 skill 實作；C.1→C.2→C.3 依序；Wave 11 整體驗收後 → Milestone 3 達成 → 寫 HANDOFF_TO_9TH_MASTER）

⚠ **R8-INFO-06 處理策略（重要設計拐點）：**

`00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3 仍寫「5 份 QA」（pre-D-043 內容），但 D-043（DECISIONS_LOG §6.7~§6.9 partial supersede D-018 #3）已升級為 **8 份必跑**（09_a/b/c/d/f/g/h/i）。本 skill 設計**直接對齊 UD §2.5.3 v0.3 為權威**（含 8 報告 + 序列印出順序），**不**直接 ref 00_k v0.1 5 報告段。

00_k v0.1 → v0.2 升版屬 9th master cleanup queue（或本 starter scope 外另開 patch round）— 本 skill SKILL.md 內含註記說明 00_k v0.1 5 報告 stale 不影響本 skill 對齊 D-043。

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase C Wave 9 C.3 task」— 實作 /qa skill（含中文 wrapper）；對齊 TASKS v1.9 §D.4 + UPSTREAM_DOWNSTREAM_SPEC v0.5 §2.5 + ARCH §6.3 + D-043 8 報告必跑（partial supersede D-018 #3）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase C Wave 9 第三條 task（C.1 → C.2 → C.3 依序）；/qa 是下游 pipeline 最後 skill
- C.3 PASS → Phase C Wave 9 完 → 進 Wave 11 整體驗收 → Milestone 3

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_k v0.1；R8-INFO-06 5→8 報告 stale 屬本 starter 註記範圍但**不**本輪 patch 00_k）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 SKILL.md（含 C.1 /scene-task + C.2 /dialogue-write + 中文 wrapper）
- ✗ **不**自動 trigger QA_PASSED → DIALOGUE_FINAL（屬 D.4 後人類 gate scope；本 skill 只更新 pipeline_state 到 QA_PASSED / QA_FAILED）
- ✗ **不**跑真實 /qa 寫檔（會污染 Template；端到端測試屬 user 親跑 M3）
- ✗ **不**產生 09_e（M9 鎖定 — 09_e 是人類在 final-gating 時填）
- ✗ **不**直接 ref 00_k v0.1 的 5 報告段（屬 R8-INFO-06 stale；本 skill 對齊 UD §2.5.3 v0.3 為 8 報告權威）
- ✗ **不**修補 00_k（屬 9th master cleanup queue）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §D.4（line 1829-1896）+ UD v0.5 §2.5（5 個內部子階段；v0.3 對齊 D-043 8 報告）+ ARCH §6.3 + D-043 8 報告序列順序。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/qa/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/檢查/SKILL.md` | 中文 wrapper |

### /qa 主 SKILL.md 結構

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；含 8 報告必跑 mention + R8-INFO-06 處理註記）
- 中文 5 必填 header
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（英文 slash command + 3 種輸入模式 + 中文別名 reference）
  - `## 觸發協議`（對應 UD §2.5 + 必讀 references；**R8-INFO-06 註記**：「本 skill 對齊 UD §2.5.3 v0.3 + D-043 8 報告為權威；00_k v0.1 階段 3 仍寫 5 報告屬 pre-D-043 stale，不影響本 skill 行為。00_k v0.2 升版屬 9th master cleanup queue。」）
  - `## 啟動前檢查`（D-051 後 single marker + Bootstrap completed + 目標台詞檔 pipeline_state check + D.3.5 gate / 路徑 B 例外處理）
  - `## 流程`（5 階段對應 UD §2.5.1~§2.5.6）
  - `## 8 報告詳細 algorithm`（對應 UD §3.1~§3.9；每報告 qa_type + 檢查 algorithm 摘要）
  - `## 8 報告序列印出順序（UD §2.5.3 v0.3 + D-043）`
  - `## qa_decision 計算規則`
  - `## .protocol_version 寫入規範`（phase_log entry 對應 UD §2.5.6）
  - `## 輸入鎖定（O6）`（3 種輸入形態：完整台詞檔路徑 / scene_id + 版本 / 無參數）
  - `## 輸出`（9_quality_assurance/*_QA_*.md × 8 + D-050 寫檔目錄表）
  - `## 邊界`（D-050 子裁決 1 + 子裁決 2 雙 block + 不產生 09_e + 不擅升 FINAL）
  - `## 錯誤處理 / Rollback`
  - `## 錯誤呈現規則`

### /qa 差異規格

- **觸發語：** `/qa <input>`（接 1 個 user 參數；3 種輸入形態詳「## 輸入鎖定」段）
- **對應 protocol：** **UD v0.5 §2.5.1~§2.5.6（v0.3 對齊 D-043 為權威）** — 註：00_k v0.1 階段 3 仍寫 5 報告屬 R8-INFO-06 stale，本 skill 不 ref 00_k 8 報告段
- **8 報告序列順序權威：** UD §2.5.3 v0.3 + D-043（CODEX C-11 解決）
- **9 種 qa_type enum 對齊：** `_design/registries/qa_type_registry.template.yaml` v0.1（含 AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT / RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY / **9_e final-gating 紀錄** — 09_e 不在本 skill 範圍）
- **議題清單動態載入：** **不適用**（/qa 不採 D-047 議題對話模式；它跑既有 8 個 QA 模板）
- **創建 entity：** 8 個 QA 報告檔（非新 entity；reference 既有 S 台詞檔）
- **依賴：** 
  - 目標台詞檔 `狀態 ≥ DRAFT` AND `pipeline_state ∈ {DIALOGUE_CONVERGED, DIALOGUE_TRIAL}` 
  - DIALOGUE_TRIAL 路徑 B 例外（user 明示「直接對 v01A 跑 QA」）；QA_PASSED 後**不能**直接升 FINAL
- **下游：** 階段 5 印「下一步建議」依 qa_decision 不同：
  - PASS：「人類確認 + 填 09_e final-gating 紀錄 → 升 DIALOGUE_FINAL」
  - FAIL：「修稿路徑 A / 重生路徑 B / 人類裁決保留路徑 C」（依 UD §2.6.1）
- **不**自動 trigger 任何 gate / skill

### 5 階段流程（對齊 UD §2.5 + ARCH §6.3）

#### 階段 1：診斷（依 UD §2.5.2）

agent 行為：
1. 解析 user 輸入（3 種輸入形態之一）
2. 讀目標台詞檔
3. 從 `source_task` 反查任務包，讀本場規格
4. 從 `entities` / `depends_on` 反查 C-* / R-*-* 等實體聲線卡 / 關係矩陣
5. 檢查台詞檔 `狀態 ≥ DRAFT` AND `pipeline_state` 合法（DIALOGUE_CONVERGED 標準路徑 / DIALOGUE_TRIAL 路徑 B 例外）
6. 印「本次 QA 對象元資訊」貼 chat

#### 階段 2：執行 8 份報告（依 UD §2.5.3 v0.3 + D-043）

依 D-043 拍板的閱讀優先順序，**並行檢查、序列印出**：

**並行檢查（同時跑 — 8 份）：**

| # | 模板檔 | qa_type | algorithm 來源 |
|---|---|---|---|
| 1 | 09_quality_assurance/09_a_AI味檢查模板.md | AI_FLAVOR | UD §3.1 |
| 2 | 09_quality_assurance/09_b_角色聲線一致性模板.md | VOICE_CONSISTENCY | UD §3.2 |
| 3 | 09_quality_assurance/09_c_禁用詞檢查模板.md | FORBIDDEN_WORD | UD §3.3 |
| 4 | 09_quality_assurance/09_d_資訊控制檢查模板.md | INFO_CONTROL | UD §3.4 |
| 5 | 09_quality_assurance/09_f_類型偏移檢查模板.md | GENRE_DRIFT | UD §3.5 |
| 6 | 09_quality_assurance/09_g_節奏感檢查模板.md | RHYTHM | UD §3.7（v0.3 新增）|
| 7 | 09_quality_assurance/09_h_對話張力檢查模板.md | DRAMATIC_TENSION | UD §3.8（v0.3 新增）|
| 8 | 09_quality_assurance/09_i_跨場一致性檢查模板.md | CROSS_SCENE_CONTINUITY | UD §3.9（v0.3 新增）|

**09_e 不在此 skill 範圍**（09_e 是定稿變更紀錄，由人類在 final-gating 時填；M9 鎖定）

#### 8 報告序列印出順序（UD §2.5.3 v0.3 + master 確認方向 + D-043）

```
序列印出（給 user 看 — v0.3 新順序）：
  1. 09_f 類型偏移檢查報告      （最優先 — 類型跑掉影響其他判定）
  2. 09_d 資訊控制檢查報告      （資訊洩漏先於 character 層）
  3. 09_h 對話張力檢查報告      （張力強度標準依類型；09_f 之後跑）
  4. 09_b 角色聲線一致性報告    （角色 OOC 判定）
  5. 09_g 節奏感檢查報告        （節奏依賴聲線；09_b 之後）
  6. 09_a AI 味檢查報告         （表層字面層）
  7. 09_c 禁用詞檢查報告        （機械詞表比對）
  8. 09_i 跨場一致性檢查報告    （最後 — 需所有 per-scene QA 結果交叉比對）
```

**序列邏輯（v0.3 對齊 master 確認方向）：**

- 09_f 仍最優先（既有）— 類型偏移影響其他判定基準
- 09_h **新插在 09_f 之後**：不同類型的張力強度標準不同
- 09_g **新插在 09_b 之後**：角色聲線決定句子長短偏好
- 09_i **新最後**：需要所有 per-scene QA 結果才能交叉比對
- 09_a / 09_c 維持後段（表層字面檢查）

每份報告依 09_a/b/c/d/f/g/h/i 各自模板生成，frontmatter 含完整下游 8 欄。

#### 階段 3：彙整（依 UD §2.5.4 v0.3 + D-043）

agent 行為：
1. 統合 **8 份報告**中的「最高優先問題」（依序列順序）
2. 計算整體 `qa_decision`（詳「## qa_decision 計算規則」段）
3. 印「彙整摘要」貼 chat

#### 階段 4：寫檔（依 UD §2.5.5 v0.3 + D-043）

依 SPEC §12.7（v1.1 對齊 8 份序列順序）寫 **8 份報告** 到 `<instance_root>/09_quality_assurance/`，檔名 `<base>_<QA_類型>_報告.md`：

每份報告 frontmatter **完整含下游 8 欄**：
```yaml
---
entities: [S-<n>-<m>]
depends_on: [<相關 C-*、R-*-*>]
weight: {S-<n>-<m>: 0.125}      # v1.1 / D-043 — 8 份各 0.125 加總 1.0
scene_id: S-<n>-<m>
source_task: <任務包路徑>
source_dialogue: <目標台詞檔路徑>
source_dialogues: null
pipeline_state: QA_PASSED       # 或 QA_FAILED
mode_tag: null                  # M7 對齊：QA 報告自身無 mode_tag
qa_decision: PASS               # 或 FAIL（v1.1：8 份全 PASS 才 PASS）
qa_type: AI_FLAVOR              # 8 種之一
---
```

中文 header 5 欄齊全。

**同步更新目標台詞檔 frontmatter 的 `pipeline_state` 與 `qa_decision`（只動 frontmatter，不動內容）：**
- pipeline_state: `QA_PASSED` 或 `QA_FAILED`
- qa_decision: `PASS` 或 `FAIL`

**不產生 09_e**（M9 鎖定）

#### 階段 5：驗證（依 UD §2.5.6 v0.3 + D-043）

agent 行為：
1. 自動 `/status` — 確認 `S-<n>-<m>` 完成度上升（QA_PASSED 應到 90%）
2. 在 `<instance_root>/.protocol_version.phase_log` append 一筆：
   ```yaml
   - phase: qa
     date: YYYY-MM-DD
     skill: /qa
     status: completed
     scene_id: S-<n>-<m>
     target_dialogue: <台詞檔路徑>
     qa_report_paths:
       - <09_a 報告路徑>      # qa_type: AI_FLAVOR
       - <09_b 報告路徑>      # qa_type: VOICE_CONSISTENCY
       - <09_c 報告路徑>      # qa_type: FORBIDDEN_WORD
       - <09_d 報告路徑>      # qa_type: INFO_CONTROL
       - <09_f 報告路徑>      # qa_type: GENRE_DRIFT
       - <09_g 報告路徑>      # qa_type: RHYTHM
       - <09_h 報告路徑>      # qa_type: DRAMATIC_TENSION
       - <09_i 報告路徑>      # qa_type: CROSS_SCENE_CONTINUITY
     qa_decision: PASS  # 或 FAIL（8 份全 PASS 才 PASS）
   ```
3. 印 QA 結論 + 下一步建議：
   - **qa_decision=PASS：** 「人類確認可定稿 → 填 09_e final-gating 紀錄 → 升 `狀態: FINAL` + `pipeline_state: DIALOGUE_FINAL`」
   - **qa_decision=FAIL：** 「修稿路徑 A（修稿後重跑 /qa）/ 重生路徑 B（回 DIALOGUE_TRIAL 跑新一輪 /dialogue-write）/ 人類裁決保留路徑 C（保留違規亮點；填 09_e 留證）」
4. 印禁止：**不**自動升 FINAL / 不自動產 09_e / 不擅升 LOCKED

### qa_decision 計算規則

- **PASS：** 8 份全 PASS
- **FAIL：** 任一份 FAIL
- **ARBITRATE_REQUIRED：** 人類保留違規亮點等情境（不由 agent 自動產生，由 user 後續在 09_e 標）— 本 skill 不自動標 ARBITRATE_REQUIRED；只標 PASS 或 FAIL

### 輸入鎖定（O6）

`/qa` 接受以下三種輸入，其他拒絕：
1. 完整台詞檔路徑：`/qa 08_dialogue_outputs/CH01_S03_<簡稱>_dialogue_v02.md`
2. scene_id + 版本：`/qa S-01-03 v02`（從 phase_log 推導路徑）
3. 無參數：使用上一輪 /dialogue-write 收斂後產出的版本（從 phase_log 最後 entry 推導）

### 啟動前檢查

```
Before Stage 1, verify:

- current folder is the Instance repo root
- `.protocol_version` 存在 + phase_log 含 bootstrap entry status=completed
- `_design/expected_entities.yaml` 存在
- **(D-051 後 active 單 marker)** no `.template_root` marker file exists at repo root
- 目標台詞檔存在
- 目標台詞檔 `狀態 ≥ DRAFT` AND `pipeline_state` ∈ {`DIALOGUE_CONVERGED`, `DIALOGUE_TRIAL`}
  - DIALOGUE_CONVERGED：標準路徑（D.3.5 收斂 gate 完成）
  - DIALOGUE_TRIAL：路徑 B 例外（user 必須明示「直接對 trial 跑 QA」；QA_PASSED 後不能直接升 FINAL；必須先回 DIALOGUE_CONVERGED 才可升）
- 8 個 QA 模板存在：`09_quality_assurance/09_a / b / c / d / f / g / h / i_*.md`
  - 若任一缺 → 拒絕（⏸ 條件未滿足；提示 user 補模板或檢查 Phase A 模板繼承）
- task pack 存在（從台詞檔 `source_task` 反查）
- 對應上游 entity 至少 REVIEW（依台詞檔 depends_on 列）
```

對應拒絕文案參考 init-project SKILL.md v0.3「⏸ 條件未滿足」格式。

### .protocol_version 寫入規範

詳「## 階段 5：驗證」段 phase_log entry 範例。Use concrete entity IDs only.

### 輸入

詳「## 輸入鎖定」段。

### 輸出

Runtime output includes:
- 階段 1 診斷報告（chat-only）
- 階段 2 並行檢查（chat-only progress；報告寫檔在階段 4）
- 階段 3 彙整摘要（chat-only）
- 階段 4 8 份報告寫檔 + 同步更新目標台詞檔 frontmatter（only after user approval）
- 階段 5 /status validation + 下一步建議

Runtime file outputs are limited to:
- `09_quality_assurance/<base>_<QA_類型>_報告.md` × 8（恰好 8 份；不多不少；**不產 09_e**）
- 目標台詞檔 frontmatter `pipeline_state` + `qa_decision` 更新（不動內容）
- `.protocol_version.phase_log`

### D-050 寫檔目錄表

| 類別 | 路徑 / 行為 | 規則 |
|---|---|---|
| 合法寫檔 | `09_quality_assurance/<base>_<QA_類型>_報告.md` × 8 | 8 份 QA 報告主體（D-043 必跑） |
| 合法 frontmatter 更新 | `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v*.md` | 只動 frontmatter `pipeline_state` + `qa_decision` 兩欄；不動 body |
| 追蹤紀錄 | `.protocol_version.phase_log` | 只記錄 `phase: qa` / `scene_id` / `target_dialogue` / `qa_report_paths` / `qa_decision` 等 runtime log |
| 不寫 | `01_world/`, `02_vocabulary/`, `03_characters/`, `04_relationships/`, `05_plot/`, `06_scene_index/`, `07_scene_tasks/`, `10_art_assets/`, `00_protocol/` | 任何寫入都屬 D-050 越界 |
| 不寫 | `09_quality_assurance/09_e_*.md` | 09_e 屬 final-gating 紀錄；人類在 D.4 後填；本 skill **嚴禁產生** |
| 不改 body | `08_dialogue_outputs/*.md` | 只動 frontmatter；不刪/改 user 保留的句子 |

### 邊界

The skill must not:
- modify LOCKED files without explicit confirmation
- allow Bootstrap customization
- modify any `00_protocol/` file
- modify `scripts/`, `_tools/frontend/`, registry Template files
- modify existing Phase A / Phase B / Phase C C.1 / C.2 skills or wrappers
- create or rewrite worldbuilding, vocabulary, characters, relationships, plot, chapters, scenes, task packs, or dialogue
- modify dialogue body content（只動 frontmatter `pipeline_state` + `qa_decision`）
- delete sentences marked 「保留」 by user
- **produce 09_e**（M9 鎖定；屬人類 final-gating scope）
- **skip any of the 8 QA reports**（D-043 必跑；09_a/b/c/d/f/g/h/i 全部）
- promote dialogue 狀態 to `FINAL` / `LOCKED`（屬人類 D.4 後 final-gating gate scope）
- auto-trigger D.4 後 final-gating gate / FINAL/LOCKED 升級
- create new entity types, enum values, schemas, or parser behavior
- write real project-specific `.protocol_version` values inside this `SKILL.md`

**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為 `09_quality_assurance/` (8 報告) + `08_dialogue_outputs/` frontmatter 兩欄更新；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段

### R8-INFO-06 處理註記（重要設計拐點）

`00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3 仍寫「5 份 QA」（pre-D-043 內容），但本 skill 對齊 **D-043 8 報告必跑** + **UD §2.5.3 v0.3 序列順序為權威**。

**本 skill 行為：**
- 跑 8 份 QA 報告（不 5 份）
- 序列順序對齊 UD §2.5.3 v0.3（09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i）
- frontmatter `weight: 0.125` 每份（8 × 0.125 = 1.0；非 5 × 0.2）
- 不 ref 00_k v0.1 階段 3 的 5 報告段（屬 stale）

**00_k v0.1 → v0.2 升版屬未來 patch round scope（9th master cleanup queue 或本 8th master scope 外另開 patch）— 本 skill SKILL.md 內含本註記說明此設計拐點，避免下游 reviewer 誤解。**

### 錯誤處理 / Rollback

If any prerequisite fails, stop before Stage 1 and write nothing.

If a target dialogue file becomes `LOCKED` between Stage 1-4 and write, stop and ask for decision.

If any of the 8 reports cannot generate（模板缺 / 解析失敗等）：
1. Stop further reports.
2. Roll back any partial reports written this run.
3. Mark or keep the phase_log entry as `aborted`, not `completed`.
4. Report exactly which reports were attempted, rolled back, or require manual inspection.
5. **不**標 qa_decision=PASS 即使其他 7 份 PASS（D-043 必跑 8 份；缺一不可 PASS）

### 錯誤呈現規則

Use `## ✗ 無法執行 / Cannot Proceed` for user-correctable input problems and `## ⏸ 條件未滿足 / Prerequisites Not Met` for state problems. Each error includes What / Where / Why / 下一步.

### 中文 wrapper 內容（檢查）

```markdown
---
name: 檢查
description: /qa 中文別名 — 觸發 8 份 QA 報告必跑（D-043）。實際邏輯參見 .claude/skills/qa/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/檢查` 中文別名 wrapper
優先級：高

# 中文別名 - 檢查

本 skill 是 `/qa` 的中文別名。當使用者以 `/檢查 <input>` 觸發時，等同於觸發 `/qa <input>`。

完整流程、5 階段規則、8 份 QA 報告必跑（D-043；09_a/b/c/d/f/g/h/i）+ UD §2.5.3 v0.3 序列順序、`.protocol_version` schema、D.3.5 收斂 gate dependency、rollback 與錯誤處理，全部以 `.claude/skills/qa/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/qa/SKILL.md`。
```

### 文字長度建議

主 SKILL.md ~500-600 行 markdown（含 5 階段 + 8 報告 algorithm 表 + 8 報告序列印出順序 + qa_decision 規則 + R8-INFO-06 註記 + D-050 雙 block + 啟動前檢查 + phase_log schema + 錯誤處理）；中文 wrapper ~30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源（**本 skill 主要 reference**）
1. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.5 全 5+ 子階段（v0.3 對齊 D-043 8 報告）+ §3.1~§3.9 8 個 QA 模板 algorithm（**最重要**）
2. `_design/TASKS.md` v1.9 §D.4（含 D-043 partial supersede 註記）+ §D.3.5 收斂 gate dependency
3. `_design/SPEC.md` v1.2 §12.3 場景狀態機 + §12.7 8 份序列順序（v1.1 對齊 D-043）
4. `_design/ARCHITECTURE.md` v1.6 §6.3 /qa 內部架構 + §3.3.1 錯誤呈現 + §3.3.2 D-051 後 single marker
5. `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043（8 報告必跑 partial supersede D-018 #3）+ §6.12.2 D-050 + §6.13.2 D-051 + §6.16.2 D-053 + §6.17.2 D-054（context）

B. 對齊依據
6. `_design/POST_LOCK_PENDING.md` v0.10
7. `_design/registries/qa_type_registry.template.yaml` v0.1（9 種 qa_type enum + 9_e final-gating 紀錄獨立 enum）
8. `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1（QA 模板擴充）+ §4.2（可擴充 QA 機制）
9. `00_protocol/00_a_台詞生產協議.md`（§3.9 QA 模式 — 階段 2 用）
10. `.claude/skills/scene-task/SKILL.md` v0.1 + `.claude/skills/dialogue-write/SKILL.md` v0.1（C.1 + C.2 上游 — task pack + dialogue；本 skill 反查）
11. `.claude/skills/init-project/SKILL.md` v0.3（D-051 後 single marker 範式）
12. 5 個 /create-* SKILL.md v0.3 / v0.1（D-050 子裁決 1+2 雙 block body 格式範式）

C. 必讀模板 / 既有檔
13. `09_quality_assurance/09_a_AI味檢查模板.md` ~ `09_i_跨場一致性檢查模板.md`（8 個 QA 模板；本 skill 階段 2 跑這 8 個）
14. `09_quality_assurance/09_e_定稿變更紀錄模板.md`（context only — 本 skill **不**產生 09_e；屬人類 final-gating 範圍）
15. `08_dialogue_outputs/08_a_台詞版本管理規範.md`（**附加任務 P-009 對應：可在本 skill 完成時順手修正 §11.1「必要 QA」從 5 份 → 8 份；屬可選 scope。** 若選擇做，需 user 明示同意才能改既有 LOCKED 模板。預設**不做** — 留 9th master cleanup queue）

D. R8-INFO-06 context（重要 — 本 skill 直接面對的議題）
16. `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3（**註：5 報告 stale；本 skill 不 ref 此段，改 ref UD §2.5.3 v0.3 為權威**）
17. `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1 R8-INFO-06 finding 紀錄

E. 已 LOCKED 不可動文件
18. 所有 `_design/*.md` 既有 spec
19. `scripts/*.py`
20. 既有 27 模板（含 09_a~09_i / 09_e）
21. 所有 `00_protocol/` 檔（含 00_k v0.1；本 skill **不 patch** 即使 R8-INFO-06 stale）
22. `_tools/frontend/*` 全部
23. 既有 SKILL.md（init-project / create-* x5 / status / check-gaps / 6 中文 wrapper / scene-task / 場景任務包 / dialogue-write / 生成台詞）
24. `.template_root` marker / AGENTS.md / CLAUDE.md / skill_invocation_guide.md
25. D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.10 / D054_DECISION_PACKAGE v0.2 — context）

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/qa/SKILL.md` v0.1
2. `.claude/skills/檢查/SKILL.md` v0.1

不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name + description）+ 中文 5 必填 header + markdown 主體
- 中文 wrapper 引用英文主檔為權威 + 不展開第二套流程

B. 內容（英文主 SKILL.md）
- 5 階段流程對齊 UD §2.5.1~§2.5.6 v0.3
- **8 份 QA 報告 algorithm 表完整**（09_a/b/c/d/f/g/h/i；對齊 UD §3.1~§3.9）
- **8 報告序列印出順序**對齊 UD §2.5.3 v0.3（09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i）
- qa_decision 規則：8 全 PASS 才 PASS / 任一 FAIL 即 FAIL
- 啟動前檢查含 D-051 後 single marker + Bootstrap + 目標台詞檔 pipeline_state check + 8 模板存在 check
- 輸入鎖定 3 形態（完整路徑 / scene_id + 版本 / 無參數）
- phase_log entry 含 `phase: qa` + `scene_id` + `target_dialogue` + `qa_report_paths`（**8 個路徑**）+ `qa_decision` + `status: completed`
- 寫檔目錄嚴格限 `09_quality_assurance/` (8 報告) + 目標台詞檔 frontmatter 兩欄更新（D-050 子裁決 2 對齊）
- 邊界含 D-050 子裁決 1 + 子裁決 2 雙 block + 不產 09_e + 不擅升 FINAL + 不修 dialogue body
- **R8-INFO-06 處理註記段完整**（明示本 skill 對齊 UD §2.5.3 v0.3；00_k v0.1 5 報告 stale 不影響）
- 不自動 trigger D.4 後 final-gating / FINAL/LOCKED 升級

C. 不破壞既有
- 不動既有 SKILL.md（含 C.1 / C.2）
- 不動 27 模板 / 00_protocol/ / _design/ 既有 spec（含 00_k v0.1 — R8-INFO-06 stale 不處理）
- `python scripts/check_headers.py` 0 ERROR 維持
- `check_paths.py` baseline +0 增量

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 5 階段不對齊 UD §2.5 OR 8 報告序列順序錯 OR 09_e 被產生 → 修補 round

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX C.3 完成 → user commit/push → 回 master：

1. master 進 Phase C Wave 11 整體驗收（寫 `CODEX_C_FINAL_STARTER.md` 給 user 跑 PHASE_C_COMPLETION_REPORT v1.0）
2. **C.1 → C.2 → C.3 依序不可平行**（依賴鏈完成）
3. C.3 + Wave 11 全 DONE → Milestone 3 達成 → master 寫 `HANDOFF_TO_9TH_MASTER.md` 接 Phase D（視圖 + 迭代 + 匯出 + 整合）

**M3 user-test 第三次點時機（依 HANDOFF §7.3）：** Milestone 3 達成後可做 M3 user-test — 對任一 Phase B 建好的場景跑 /scene-task → /dialogue-write → /qa 完整 chain。

**00_k v0.1 升版 v0.2（R8-INFO-06）：** 本 starter 不處理；推 9th master cleanup queue 或 8th master 收尾另開 patch round。優先級不高（本 skill 直接 ref UD §2.5.3 v0.3 已對齊 D-043；00_k 是 narrative protocol，不直接影響 skill runtime）。

---

# 3. 文件維護紀律

- 本檔是 Phase C Wave 9 C.3 起手 starter；完成後可 archive
- ⚠ /qa 是台詞生產 pipeline 最後 skill；8 報告必跑 + 序列順序正確 = M3 user-test 成敗關鍵
- ⚠ R8-INFO-06 (00_k v0.1 5 報告 stale) 不本輪 patch；本 skill 直接 ref UD §2.5.3 v0.3

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §D.4 + §D.3.5
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.5 + §3.1~§3.9
- `_design/SPEC.md` v1.2 §12.3 / §12.7
- `_design/ARCHITECTURE.md` v1.6 §6.3
- `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043 + §6.12.2 / §6.13.2 / §6.16.2 / §6.17.2
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1 / §4.2
- `_design/POST_LOCK_PENDING.md` v0.10
- `_design/registries/qa_type_registry.template.yaml` v0.1
- `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3（R8-INFO-06 stale 註記）
- `00_protocol/00_a_台詞生產協議.md` §3.9 QA 模式
- `.claude/skills/scene-task/SKILL.md` v0.1（C.1 上游）
- `.claude/skills/dialogue-write/SKILL.md` v0.1（C.2 上游）
- `09_quality_assurance/09_a ~ 09_i 模板`（8 個 QA 模板 + 1 個 09_e final-gating 紀錄模板）
- `08_dialogue_outputs/08_a_台詞版本管理規範.md`（P-009 附加任務 — 可選 5→8 修正；預設不做）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1 R8-INFO-06
