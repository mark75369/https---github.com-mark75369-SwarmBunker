狀態：DRAFT  
版本：v0.4（9th master Round 3 NEAR-GO inline patch — R3-MAJOR-01 line 76 + line 245 拿掉 R2-MAJOR-02 修補時使用的 8-欄字串（strict grep 即使在否定句仍命中）→ 改為「07/08/09 pipeline 專屬 frontmatter 欄位」具體列舉 (pipeline_state / mode_tag / qa_decision / qa_type / source_task / source_dialogue / source_dialogues / scene_id)；歷史紀錄：v0.2 → v0.3 為 Round 2 inline patch（R2-MAJOR-01 補 external_action_required + R2-MAJOR-02 frontmatter wording）；v0.1 → v0.2 為 Round 1 inline patch）  
最後更新：2026-05-22  
適用範圍：Phase D Wave 12 task — /iterate-detailed-outline skill + /iterate-scene --split-to-file（D-054 NEW_REQ_15 落地）+ 中文 wrapper 實作  
優先級：高

# CODEX_D5_STARTER — Phase D Wave 12 D.5：/iterate-detailed-outline + /iterate-scene --split-to-file skill 實作

# 0. 本檔用途

Phase D Wave 12 第五條 task — 實作 `/iterate-detailed-outline` skill（迭代 CH-* + S-*-* 細綱實體）+ **`/iterate-scene --split-to-file`（D-054 NEW_REQ_15 落地；第 6 個 /iterate-* skill）**。對齊 TASKS v1.9 §C.2（第 5 個 /iterate-* skill）+ 00_protocol/00_j_迭代協議.md v0.1 §10.5 + §10.6 + §10.7 + 00_protocol/00_h_細綱創建協議.md v0.2 + **DECISIONS_LOG v2.0 §6.17 D-054 + POST_LOCK_PENDING v0.18 NEW_REQ_15**。

**前置條件：** D.4 PASS（或獨立並行）。

**Wave 12 收尾 task — 最複雜 starter**：含兩個 skill + D-054 hybrid fallback 落地 split-to-file 邏輯。

⚠ **D-054 拍板對齊（核心 — 本 starter 主軸之一）：**
- DECISIONS_LOG v2.0 §6.17 D-054：per-scene 檔 convention 選 1 Hybrid 拍板
- POST_LOCK_PENDING v0.18 NEW_REQ_15：未來迭代條件追蹤（trigger A/B/C/D）
- 既有 00_h SKILL.md line 198 escape hatch wording 自然承接此設計
- 既有 .claude/skills/scene-task/SKILL.md v0.1 含 D-054 hybrid 兩階段 fallback 讀檔邏輯
- 本 starter 落地 `/iterate-scene --split-to-file` — 把指定場景從聚合 06_a split 為獨立 per-scene 檔

**共通範本：** 沿用 D.1 starter pattern；CODEX 跑本 task 前必先讀 `_design/CODEX_D1_STARTER.md` v0.1 + `_design/D054_DECISION_PACKAGE.md` v0.2。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 D.5 task」— 實作 /iterate-detailed-outline skill + /iterate-scene --split-to-file 落地（D-054 NEW_REQ_15）。

工作資料夾：D:\劇本開發工具

**權威來源（必讀；按順序）：**
- `_design/CODEX_D1_STARTER.md` v0.1（共通範本；starter pattern）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 — 含完整 hybrid 設計推理）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054
- `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_15（未來迭代追蹤）
- `_design/TASKS.md` v1.9 §C.2（5 個 /iterate-* skill 中第 5 個）
- `00_protocol/00_j_迭代協議.md` v0.1 §10.5 / §10.6 / §10.7（CH-* / S-*-* / split-to-file 迭代呼叫指南）
- `00_protocol/00_h_細綱創建協議.md` v0.2（對應 entity 創建協議；line 198 escape hatch）
- `.claude/skills/scene-task/SKILL.md` v0.1（含 D-054 hybrid 讀檔 fallback；本 skill 寫的 per-scene 檔自動被它優先讀取）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 結構範例 + D-050 子裁決 1+2 雙 block + R8-MA-01 prereq fix + R9-INFO-02 body D-053 exception block）

### 任務目標（本 task 雙 skill — Wave 12 唯一）

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/iterate-detailed-outline/SKILL.md` | 英文主檔（CH-* + S-*-* 迭代）|
| 2 | `.claude/skills/迭代細綱/SKILL.md` | 中文 wrapper |
| 3 | `.claude/skills/iterate-scene/SKILL.md` | 英文主檔（**D-054 NEW_REQ_15 落地** — split-to-file 子模式）|

**注意：** /iterate-scene 不建中文 wrapper（D-054 拍板原文未指定中文別名；屬 hybrid escape hatch 性質的開發者工具，user 多用英文 slash command）。

### /iterate-detailed-outline 差異規格（vs /iterate-world）

- **觸發語：** `/iterate-detailed-outline` 或 `/iterate-detailed-outline <CH-ID>`（**可選 1 user 參數** — 章節 ID；若不傳則 chat 對話確認目標）
- **對應 protocol：** `00_j v0.1` + `00_protocol/00_h_細綱創建協議.md v0.2`
- **議題清單動態載入：** **適用**（registry key = `00_h_detailed_outline`）
- **modify entity 範圍：** CH-* 章節 / S-*-* 場景索引（user 在階段 1 明示）
- **依賴下游：** 影響範圍含對應 06_a row + 已存在 per-scene 拆檔 + 已 generate 的 07_scene_tasks / 08_dialogue_outputs / 09_quality_assurance
- **下游：** 階段 5 印「下一步建議：若需視圖跑 /view-detailed-outline；若 S-*-* 變動且已產出台詞 → 建議重跑全 8 份 QA」

### /iterate-scene 差異規格（D-054 NEW_REQ_15 落地）

- **觸發語：** `/iterate-scene <S-ID>` 或 `/iterate-scene <S-ID> --split-to-file`（**接 1 user 參數 + 可選 flag**）
- **對應 protocol：** `00_j v0.1` §10.7（split-to-file 設計詳述）
- **議題清單動態載入：** 不適用（split-to-file 屬 file organization 操作；不涉議題對話）
- **modify entity 範圍：** 單一 S-<ch>-<n>（user 在 slash command 接 S-ID 明示）
- **`--split-to-file` 行為（D-054 hybrid 落地）：**
  - 把指定場景從聚合 `06_scene_index/06_a_場景索引模板.md` 對應 row split 為獨立 `06_scene_index/CH<n>_S<m>_<scene_name>.md` 檔
  - 在原 06_a row 加 `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->` marker（**不刪除 row** — 保留 fallback 兼容；下游 /scene-task 兩階段 fallback 邏輯依此判定優先讀 per-scene 檔）
  - 寫新 per-scene 檔 frontmatter 對齊 SPEC §5.2（**上游/靜態檔三欄：entities / depends_on / weight**；繼承原 row 的設定）— **不擴充 07/08/09 pipeline 專屬 frontmatter 欄位**（pipeline_state / mode_tag / qa_decision / qa_type / source_task / source_dialogue / source_dialogues / scene_id 等屬下游 07_scene_tasks / 08_dialogue_outputs / 09_quality_assurance 範圍；06_scene_index per-scene 屬上游/靜態檔；對齊 06_a 場景索引模板.md frontmatter 規範；R2-MAJOR-02 + R3-MAJOR-01 修補）
- **不帶 flag 行為：** /iterate-scene <S-ID> 不帶 --split-to-file → 純 S-*-* 內容迭代（修改 06_a 對應 row 或既有 per-scene 檔內容；同 /iterate-detailed-outline 子模式）
- **下游：** 階段 5 印「split-to-file 完成；/scene-task <S-ID> 下次跑時會自動 detect per-scene 檔優先；NEW_REQ_15 trigger B monitor — 連續 ≥ 5 次拆檔請通知 master 啟動 D-056+ 評估（議題號原預留為 D-055；§6.18.2 順延）」

### 5 階段流程差異 — /iterate-detailed-outline

#### 階段 1：變更點識別

agent 開場：

> 請說明你想改細綱（CH-* 章節 / S-*-* 場景索引）的什麼？可以是：
> - 章節結構（如把 CH3 拆成兩章 / 合併兩章）
> - 章節節奏（high / mid / low）
> - 場景索引內單一 S-*-* 內容（出場角色 / 地點 / 時間 / risk_type）
> - 多個 S-*-* 順序重組
> - per-scene 拆檔需求（屬 /iterate-scene --split-to-file scope；本 skill 拒絕並提示用 /iterate-scene）
> 
> 越具體越好。

#### 階段 2：強制影響範圍評估

CH-* / S-*-* 反查預期清單：

| 路徑 | 預期檔案 |
|---|---|
| direct | `05_plot/05_b_章節結構模板.md`（CH-* entry）/ `06_scene_index/06_a_場景索引模板.md`（S-*-* row；含 D-054 fallback per-scene 檔）|
| depends | 已存在的 per-scene `06_scene_index/CH<n>_S<m>_*.md` 拆檔 + `07_scene_tasks/CH<n>_S<m>_*` 任務包（若 generate）|
| indirect | `08_dialogue_outputs/*`（若已產出台詞）+ `09_quality_assurance/*`（若已產出 QA 報告）|

**D-054 fallback 讀檔（本 skill 與 /scene-task 共用此邏輯）：**
- 先 check 對應 per-scene 檔是否存在
- 存在 → 讀 per-scene 檔
- 不存在 → fallback 讀 aggregate 06_a 對應 row
- 兩者皆無 → 拒絕並提示先跑 /create-detailed-outline 建立

#### 階段 3-5：沿用 D.1 共通結構

寫檔順序：05_b → 06_a（或 per-scene 檔）→ phase_log

### 5 階段流程差異 — /iterate-scene

#### 階段 1：變更點識別

agent 開場（差異 — split-to-file 為主軸）：

> 請說明你想對場景 <S-ID> 做什麼？
> - 內容迭代（修改場景索引欄位 / 出場角色 / 地點 / risk_type 等）
> - **per-scene 拆檔（--split-to-file）**：把本場從聚合 06_a 拆為獨立檔，方便 git diff 乾淨 / per-scene LOCKED 粒度 / 多 agent 並行
> 
> 如為 split-to-file，請確認本場尚未拆檔（per-scene 檔不存在）。

#### 階段 2：強制影響範圍評估（split-to-file 子模式）

- 反查所有引用本 S-*-* 的檔（含 07_scene_tasks / 08_dialogue_outputs / 09_quality_assurance）
- user 拍板是否需要更新引用路徑（典型情況下「路徑不變」 — 下游 /scene-task 自動 detect 新 per-scene 檔）

#### 階段 3：收斂（split-to-file 子模式）

預告 split 動作：
- 從 06_a row 完整移到 per-scene 檔 `06_scene_index/CH<n>_S<m>_<scene_name>.md`
- 在 06_a 內保留 row + 加 marker `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->`（下游 fallback 兼容）
- frontmatter 對齊 SPEC §5.2（per-scene 檔的 entities: [S-<ch>-<n>] / depends_on / weight: {S-<ch>-<n>: 1.0}）

#### 階段 4：執行（split-to-file 子模式）

寫檔順序：
1. 寫新 per-scene 檔（完整 row 內容；繼承原 row 的 frontmatter 設定）
2. 在原 06_a row 加 `<!-- split-to-file: ... -->` marker（不刪除 row）
3. phase_log entry 標 `split_to_file: true`

任一步出錯 rollback：刪 per-scene 檔 + 還原 06_a row marker。

#### 階段 5：實體驗證（split-to-file 子模式）

- `/status` 確認 S-*-* 完成度**不變**（split-to-file 屬 file organization；不改 entity 完成度）
- phase_log entry 標 `split_to_file: true`
- 印「下次 /scene-task <S-ID> 跑時會自動 detect per-scene 檔（D-054 hybrid 兩階段 fallback）」
- 印「NEW_REQ_15 trigger B monitor：若連續 ≥ 5 次 split-to-file，請通知 master 評估 D-056+（per-scene 變預設？；議題號原預留為 D-055；§6.18.2 順延）」

### phase_log entry 範例

`/iterate-detailed-outline`：

```yaml
- phase: iterate-detailed-outline
  date: YYYY-MM-DD
  skill: /iterate-detailed-outline
  status: completed
  modified_entity: CH-<n>  # 或 S-<ch>-<n>
  modified_files:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  prereq_changed: false
  qa_recheck_recommended: [09_d, 09_f, 09_i]  # 若 S-*-* 變動且已產出台詞
  task_pack_stale: false  # 若 07_scene_tasks 已存在 → 標 true
  abort_reason: null
  customizations: []
```

`/iterate-scene --split-to-file`（D-054 NEW_REQ_15 落地）：

```yaml
- phase: iterate-scene
  date: YYYY-MM-DD
  skill: /iterate-scene
  status: completed
  modified_entity: S-<ch>-<n>
  modified_files:
    - 06_scene_index/06_a_場景索引模板.md           # 加 split-to-file marker
    - 06_scene_index/CH<n>_S<m>_<scene_name>.md # 新建 per-scene 檔
  scope_choice: 1  # split-to-file 屬 file organization；scope_choice = 1
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  split_to_file: true       # **D-054 NEW_REQ_15 落地標記**
  prereq_changed: false
  abort_reason: null
  customizations: []
```

### 啟動前檢查（差異）

**/iterate-detailed-outline：**
- D-049 Template-detect + Bootstrap completed
- **目標 CH-* / S-*-* 存在**（05_b CH-* row 或 06_a S-*-* row 或 per-scene 檔；任一）
- P / W-rules / 主要 C-* 全 ≥ REVIEW
- LOCKED status check（拒絕 LOCKED 場景）
- 下游 pipeline 互鎖

**/iterate-scene（含 --split-to-file）：**
- D-049 Template-detect + Bootstrap completed
- **目標 S-<ch>-<n> 存在**（06_a row 或 per-scene 檔；任一；D-054 hybrid fallback）
- 對應 CH-* 存在
- LOCKED status check
- **split-to-file 子模式額外檢查：** 對應 per-scene 檔**尚未存在**（避免重複拆檔）
- 下游 pipeline 互鎖

### 邊界區段（依 D-050 + D-053；9th master Round 1 inline patch — 嚴守 D-053 範圍）

兩個 skill 各自三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式：

#### /iterate-detailed-outline 邊界

1. **D-050 子裁決 1：** 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。
2. **D-053 /create-world exception 紀錄（本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-detailed-outline) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。CH-* / S-*-* 屬作品個別細綱結構，與 00_b 反 AI 味基線通則無直接關聯；若 user 跑本 skill 時需對 00_b 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。
3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `05_plot/05_b_章節結構模板.md`（CH-* entry）
   > - `06_scene_index/06_a_場景索引模板.md`（S-*-* row）
   > - `06_scene_index/CH<n>_S<m>_<scene_name>.md`（若 D-054 fallback 抓到 per-scene 檔）
   > - `.protocol_version.phase_log`
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053）
   > 對應 CH /create-detailed-outline 寫檔範圍（05_b + 06_a；含 per-scene 檔因 D-054 hybrid）

#### /iterate-scene 邊界

1. **D-050 子裁決 1：** 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。
2. **D-053 /create-world exception 紀錄（本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-scene) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。S-*-* 場景索引 + split-to-file 屬 file organization 操作，與 00_b 反 AI 味基線通則無直接關聯。若 user 跑本 skill 時需對 00_b 做同步調整（理論上極不可能 — split-to-file 是純 file org），agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。**R2-MAJOR-01 修補：對齊其他 D5 + D1-D4 starter D-053 紀錄 block 一致性。**
3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `06_scene_index/06_a_場景索引模板.md`（row 更新 / split marker）
   > - `06_scene_index/CH<n>_S<m>_<scene_name>.md`（split-to-file 新建 / 既有 per-scene 檔修改；frontmatter 對齊 SPEC §5.2 **上游/靜態檔三欄**：entities / depends_on / weight；**不擴充 07/08/09 pipeline 專屬欄位**）
   > - `.protocol_version.phase_log`
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053）

兩個 skill 均不寫 05_a/c/d/e（屬 P scope；用 /iterate-outline）、不寫 03_characters（屬 C scope；用 /iterate-character）。

### 中文 wrapper SKILL.md（迭代細綱）

採極簡模式，指向 `.claude/skills/iterate-detailed-outline/SKILL.md` 為權威。

**/iterate-scene 無中文 wrapper**（屬 hybrid escape hatch 性質；user 用英文 slash command + S-ID）。

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：
   - 共通：D1 STARTER + ARCH §5 + §6.7 + SPEC §5.2 + §11 + 00_j + 00_h + create-detailed-outline v0.3 + DECISIONS_LOG D-050 / D-053
   - **D-054 專用：** D054_DECISION_PACKAGE v0.2 + DECISIONS_LOG §6.17 + POST_LOCK_PENDING NEW_REQ_15 + scene-task SKILL.md v0.1（D-054 fallback 讀檔邏輯範本）

2. **寫 SKILL.md 3 個**：
   - `.claude/skills/iterate-detailed-outline/SKILL.md`
   - `.claude/skills/迭代細綱/SKILL.md`
   - `.claude/skills/iterate-scene/SKILL.md`（含 --split-to-file 子模式 + D-054 NEW_REQ_15 落地標記）

3. **跑 baseline 驗證**：對齊 9th master cleanup 後 baseline（check_headers 0 ERROR / check_paths ≤ 243 ERROR / build_repo_index 0 ERROR on Windows）

4. **不跑真實寫檔**（會污染 Template；M4 testing 屬 user 親跑）

5. **撰寫 D5 review report**（可選；推 9th master Wave 12 統合驗收）

---

# 3. 驗收條件（沿用 D.1 §3 + D-054 專屬）

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index | 對齊 9th master cleanup 後 baseline |
| 2. SKILL.md 落地 | 3 個 SKILL.md 存在 | 結構齊全 |
| 3. 影響範圍評估 | 雙路反查 + CH-* / S-*-* 預期清單表 + D-054 hybrid fallback | 對齊 ARCH §5 + 00_j §4 + §10.5/§10.6/§10.7 |
| 4. 邊界紀律 | D-050 子裁決 1+2 + D-053 紀錄 + D-054 hybrid 邏輯 | 對齊 |
| 5. phase_log entry 規範 | 兩個 skill 各有 phase_log 範例 | 對齊 00_j §6.1；/iterate-scene 含 `split_to_file: true` 標記 |
| 6. **D-054 NEW_REQ_15 落地** | `/iterate-scene --split-to-file` 子模式：寫新 per-scene 檔 + 06_a marker + frontmatter 對齊 SPEC §5.2 | 對齊 D-054 拍板原文 + D054_DECISION_PACKAGE §2.1 |
| 7. **/scene-task fallback 兼容** | 本 skill 寫的 per-scene 檔被 /scene-task v0.1 兩階段 fallback 邏輯自動 detect | scene-task SKILL.md line ~ 450 + D-054 hybrid 邏輯 |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**自動 trigger 階段 4 寫檔
- **不**重生 view（O3 鎖定）
- **不**升 entity 狀態
- **不**呼叫其他 skill
- **不**改 LOCKED spec
- **不**改既有 SKILL.md（含 scene-task v0.1 + create-detailed-outline v0.3）
- **不**改 00_j / 00_h / DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE
- **不**擅自把 D-054 hybrid「per-scene 變預設」（屬未來 D-056+ 候選；議題號原預留為 D-055；§6.18.2 順延；user 拍板才能改）
- **不**自動批量拆全 Instance（D-054 拍板明示 split-to-file 為 user 主動 trigger）

「Fix one, find two」cascade pattern 預防：

- 寫好 3 個 SKILL.md 後跑 grep 全掃 stale cross-ref
- 一次性 sweep；不局部修補

---

# 5. Cross-ref

- `_design/TASKS.md` v1.9 §C.2（5 個 /iterate-* skill）
- `_design/CODEX_D1_STARTER.md` v0.1（共通範本）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054
- `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_15（未來迭代追蹤）
- `00_protocol/00_j_迭代協議.md` v0.1 §10.5 / §10.6 / §10.7
- `00_protocol/00_h_細綱創建協議.md` v0.2（line 198 escape hatch）
- `.claude/skills/scene-task/SKILL.md` v0.1（D-054 hybrid 讀檔 fallback 範本）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 結構範例）
- `_design/ARCHITECTURE.md` v1.6 §5 + §6.7
- `_design/SPEC.md` v1.2 §5.2 + §11
- `_design/DECISIONS_LOG.md` v2.0 §6.7 C-9 + §6.12 D-050 + §6.16 D-053
