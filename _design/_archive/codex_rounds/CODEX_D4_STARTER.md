狀態：DRAFT  
版本：v0.2（9th master Round 1 NO-GO inline patch round — R1-MA-02 補齊邊界三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式；R1-MA-01 sweep 順手修檔名 05_a/b/c/06_a 對齊實際 repo；R1-MI-06 header 半形冒號 → 全形）  
最後更新：2026-05-22  
適用範圍：Phase D Wave 12 task — /iterate-outline skill + 中文 wrapper 實作  
優先級：高

# CODEX_D4_STARTER — Phase D Wave 12 D.4：/iterate-outline skill 實作

# 0. 本檔用途

Phase D Wave 12 第四條 task — 實作 `/iterate-outline` skill（迭代 P 主線實體）。對齊 TASKS v1.9 §C.2 + 00_protocol/00_j_迭代協議.md v0.1 §10.4 + 00_protocol/00_g_大綱創建協議.md v0.2。

**前置條件：** D.3 PASS（或獨立並行）。

**共通範本：** 沿用 D.1 starter pattern；CODEX 跑本 task 前必先讀 `_design/CODEX_D1_STARTER.md` v0.1。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 D.4 task」— 實作 /iterate-outline skill；對齊 TASKS v1.9 §C.2 + 00_protocol/00_j v0.1 §10.4 + 00_protocol/00_g v0.2。

工作資料夾：D:\劇本開發工具

**共通範本：** 先讀 `_design/CODEX_D1_STARTER.md` v0.1 對齊 starter pattern；依下方差異規格實作。

### 任務目標

| # | 路徑 |
|---|---|
| 1 | `.claude/skills/iterate-outline/SKILL.md`（英文主檔）|
| 2 | `.claude/skills/迭代大綱/SKILL.md`（中文 wrapper）|

### /iterate-outline 差異規格（vs /iterate-world）

- **觸發語：** `/iterate-outline`（不接 user 參數；變更目標由 chat 對話確認 — 主要動 P）
- **對應 protocol：** `00_j v0.1` + `00_protocol/00_g_大綱創建協議.md v0.2`
- **議題清單動態載入：** **適用**（registry key = `00_g_outline`）
- **modify entity 範圍：** P（主線；user 在階段 1 明示具體變更點）
- **依賴下游：** 影響範圍**極廣** — 含 05_b 章節結構 / 05_c 弧線 / 05_d 揭露 / 05_e 伏筆 / 06_a 場景索引 / 07_scene_tasks/* / 08_dialogue_outputs/*
- **下游：** 階段 5 印「下一步建議：05_d / 05_e 改動可能 trigger 多個 09_d 資訊控制 QA recheck；若需視圖跑 /view-outline」

### 5 階段流程差異

#### 階段 1：變更點識別

agent 開場：

> 請說明你想改主線 P 的什麼？可以是：
> - 主線結構（如三幕轉折點 / 章節數）
> - 角色弧線階段（早期 / 中期 / 結局）
> - 資訊揭露順序（哪些章節該透露 / 禁止透露什麼）
> - 伏筆位置與回收章節
> - 主線轉折處理
> 
> 主線改動影響範圍極廣，請務必明示具體變更點。
> 越具體越好。

#### 階段 2：強制影響範圍評估

P 反查預期清單（**通常 ≥ 20 個檔**）：

| 路徑 | 預期檔案 |
|---|---|
| direct | `05_plot/05_a_主線大綱模板.md` |
| depends | `05_plot/05_b_章節結構模板.md`（依 P 拆章）+ `05_plot/05_c_角色弧線表.md`（依 P）+ `05_plot/05_d_資訊揭露表.md`（依 P）+ `05_plot/05_e_伏筆與回收表.md`（依 P）+ `06_scene_index/06_a_場景索引模板.md` + 已存在 per-scene 拆檔（若有）|
| indirect | `07_scene_tasks/*`（所有已 generate 的任務包）+ `08_dialogue_outputs/*`（所有已產出的台詞）+ `03_characters/*_聲線卡.md`（含弧線階段引用的角色）|

**特別注意（依 00_j §10.4）：**

- 影響範圍**極廣**；強烈建議分批處理
- user 可分多次 `/iterate-outline` 處理不同 sub-scope（例：第一輪只動 05_a + 05_b；第二輪動 05_d / 05_e）
- 階段 2 結尾印「建議拆分為多輪處理；每輪 commit 一次」

下游 pipeline 互鎖：影響範圍含已產出台詞 → 階段 2 必印「以下台詞檔可能因主線變動需重跑全 8 份 QA」。

#### 階段 3：收斂

差異：強烈建議分批；收斂預告稿可以含「本輪只處理子範圍 X；後續輪處理 Y / Z」。

#### 階段 4：執行

寫檔順序：05_a 主分拆 → 05_b/c/d/e 衍生分拆 → 06_a（若 P 結構變動影響場景索引）→ phase_log

#### 階段 5：實體驗證

- 後續建議：「05_d / 05_e 變動 → 多個 09_d QA recheck」/「若需視圖跑 /view-outline」

### phase_log entry 範例

```yaml
- phase: iterate-outline
  date: YYYY-MM-DD
  skill: /iterate-outline
  status: completed
  modified_entity: P
  modified_files:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_d_資訊揭露表.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  prereq_changed: true  # P 改動通常影響下游
  qa_recheck_recommended: [09_d, 09_f]  # 資訊控制 + 類型偏移
  downstream_review_required: true  # 若已產出台詞
  abort_reason: null
  customizations: []
```

### 啟動前檢查（差異）

加 1 項：**P 存在**（`05_plot/05_a` frontmatter 含 P 實體；否則拒絕並提示用 /create-outline 建立）；W-rules + 主要 C-* 全 ≥ REVIEW。

### 邊界區段（依 D-050 + D-053；9th master Round 1 inline patch — 嚴守 D-053 範圍）

三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式：

1. **D-050 子裁決 1：** 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。
2. **D-053 /create-world exception 紀錄（本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-outline) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。P 主線屬作品個別敘事結構，與 00_b 反 AI 味基線通則無直接關聯；若 user 跑本 skill 時需對 00_b 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。
3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `05_plot/05_a_主線大綱模板.md`（主分拆）
   > - `05_plot/05_b_章節結構模板.md`（衍生）
   > - `05_plot/05_c_角色弧線表.md`（衍生）
   > - `05_plot/05_d_資訊揭露表.md`（衍生）
   > - `05_plot/05_e_伏筆與回收表.md`（衍生）
   > - `06_scene_index/06_a_場景索引模板.md`（若 P 結構變動影響場景索引；optional）
   > - `.protocol_version.phase_log`
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053）
   > 對齊 P /create-outline 寫檔範圍（05_a/b/c/d/e；含 06_a 因 P 結構連動）

### 中文 wrapper（迭代大綱）

採極簡模式，指向 `.claude/skills/iterate-outline/SKILL.md` 為權威。

---

# 2. CODEX 工作流程

1. 讀必讀（沿用 D.1 §2，外加 00_g / create-outline）
2. 寫 2 個 SKILL.md
3. 跑 baseline 驗證
4. 不跑真實寫檔

---

# 3. 驗收條件（沿用 D.1 §3 5 維度）

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §C.2
- `_design/CODEX_D1_STARTER.md` v0.1（共通範本）
- `00_protocol/00_j_迭代協議.md` v0.1 §10.4
- `00_protocol/00_g_大綱創建協議.md` v0.2
- `.claude/skills/create-outline/SKILL.md` v0.3（結構範例）
- `_design/ARCHITECTURE.md` v1.6 §5 + §6.7
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050 + §6.16 D-053
