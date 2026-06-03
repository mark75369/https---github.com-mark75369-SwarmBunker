狀態：DRAFT  
版本：v0.3（9th master Round 2 NO-GO inline patch round — R2-MINOR-01 line 69 / line 95 indirect 反查表 + 寫檔範圍 sweep（05_a/06_a/04_b 對齊實際 repo）；歷史紀錄：v0.1 → v0.2 為 Round 1 inline patch 補齊邊界三 block + 修 04_b 檔名）  
最後更新：2026-05-22  
適用範圍：Phase D Wave 12 task — /iterate-relationship skill + 中文 wrapper 實作  
優先級：高

# CODEX_D3_STARTER — Phase D Wave 12 D.3：/iterate-relationship skill 實作

# 0. 本檔用途

Phase D Wave 12 第三條 task — 實作 `/iterate-relationship` skill（迭代 R-*-* 角色關係實體）。對齊 TASKS v1.9 §C.2 + 00_protocol/00_j_迭代協議.md v0.1 §10.3 + 00_protocol/00_l_關係創建協議.md v0.2。

**前置條件：** D.2 PASS（/iterate-character；或可獨立並行）。

**共通範本：** 沿用 D.1 starter pattern；CODEX 跑本 task 前必先讀 `_design/CODEX_D1_STARTER.md` v0.1。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 D.3 task」— 實作 /iterate-relationship skill；對齊 TASKS v1.9 §C.2 + 00_protocol/00_j v0.1 §10.3 + 00_protocol/00_l v0.2。

工作資料夾：D:\劇本開發工具

**共通範本：** 先讀 `_design/CODEX_D1_STARTER.md` v0.1 對齊 starter pattern；依下方差異規格實作。

### 任務目標

| # | 路徑 |
|---|---|
| 1 | `.claude/skills/iterate-relationship/SKILL.md`（英文主檔）|
| 2 | `.claude/skills/迭代關係/SKILL.md`（中文 wrapper）|

### /iterate-relationship 差異規格（vs /iterate-world）

- **觸發語：** `/iterate-relationship <character_a> <character_b>`（**接 2 個 user 參數**；可選，若不傳則 chat 對話確認 R-*-*）
- **對應 protocol：** `00_j v0.1` + `00_protocol/00_l_關係創建協議.md v0.2`
- **議題清單動態載入：** **適用**（registry key = `00_l_relationship`）
- **modify entity 範圍：** 單一 R-<a>-<b>（user 在階段 1 明示）
- **依賴下游：** 兩端 C-* 聲線卡的「關係描述段」+ 04_a / 04_b 對應 entry
- **下游：** 階段 5 印「下一步建議：若需視圖跑 /view-character <a> 或 <b>；若關係變動含禁語 → 建議重跑 /qa 09_b VOICE_CONSISTENCY」

### 5 階段流程差異

#### 階段 1：變更點識別

agent 開場：

> 請說明你想改 R-<a>-<b> 角色關係的什麼？可以是：
> - 關係性質（敵 / 友 / 上下 / 戀慕 / 拮抗 / ...）
> - 稱呼規則（A 怎麼叫 B / B 怎麼叫 A）
> - 禁語（A 不能對 B 說的話 / 反之）
> - 動態時間線（早期 / 中期 / 結局狀態轉變）
> - 隱藏動機（A 對 B 的真實感受）
> 
> 越具體越好。

#### 階段 2：強制影響範圍評估

R-*-* 反查預期清單：

| 路徑 | 預期檔案 |
|---|---|
| direct | `04_relationships/04_a_角色關係矩陣.md`（特定 R-*-* entry）|
| depends | `04_relationships/04_b_關係變化時間線.md`（含本關係的時間線 entry）+ `03_characters/<a>_聲線卡.md` 的關係段 + `03_characters/<b>_聲線卡.md` 的關係段 |
| indirect | `05_plot/05_a_主線大綱模板.md`（含 R 演化主線）+ `06_scene_index/06_a_場景索引模板.md`（含兩角色同場場景）+ 已產出的 `08_dialogue_outputs/*`（若兩角色已寫對話）|

**特別注意（依 00_j §10.3）：** R-*-* 變動需確認兩端 C-* 都 ≥ REVIEW；04_b 時間線連帶更新（user 拍板要不要平行動）。

#### 階段 3：收斂

差異：「本輪要處理的檔案清單」典型含 04_a R-entry + 兩端 C-* 聲線卡關係段 + （optional）04_b 時間線。

#### 階段 4：執行

寫檔順序：04_a → 04_b（optional）→ 兩端 C-* 聲線卡關係段 → phase_log

#### 階段 5：實體驗證

- 後續建議：「若視圖請跑 /view-character <a/b>」/「若禁語變動 → /qa 09_b」

### phase_log entry 範例

```yaml
- phase: iterate-relationship
  date: YYYY-MM-DD
  skill: /iterate-relationship
  status: completed
  modified_entity: R-<a>-<b>
  modified_files:
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 03_characters/<a>_聲線卡.md
    - 03_characters/<b>_聲線卡.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  prereq_changed: false
  qa_recheck_recommended: [09_b]
  abort_reason: null
  customizations: []
```

### 啟動前檢查（差異）

加 1 項：**R-<a>-<b> 存在**（`04_relationships/04_a` frontmatter 含 R 實體 + 04_a 含對應 entry section；否則拒絕並提示用 /create-relationship <a> <b>）；**兩端 C-* ≥ REVIEW**（必要前置；用 /iterate-character 升 REVIEW 或確認）。

### 邊界區段（依 D-050 + D-053；9th master Round 1 inline patch — 嚴守 D-053 範圍）

三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式：

1. **D-050 子裁決 1：** 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。
2. **D-053 /create-world exception 紀錄（本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-relationship) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。R-*-* 屬作品個別關係，與 00_b 反 AI 味基線通則無直接關聯；若 user 跑本 skill 時需對 00_b 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。
3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `04_relationships/04_a_角色關係矩陣.md`
   > - `04_relationships/04_b_關係變化時間線.md`（optional）
   > - `03_characters/<a>_聲線卡.md` + `<b>_聲線卡.md`（兩端關係描述段；不動其他聲線維度）
   > - `.protocol_version.phase_log`
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053）

### 中文 wrapper（迭代關係）

採極簡模式，指向 `.claude/skills/iterate-relationship/SKILL.md` 為權威。

---

# 2. CODEX 工作流程

1. 讀必讀（沿用 D.1 §2，外加 D.2 / 00_l / create-relationship）
2. 寫 2 個 SKILL.md
3. 跑 baseline 驗證
4. 不跑真實寫檔

---

# 3. 驗收條件（沿用 D.1 §3 5 維度）

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §C.2
- `_design/CODEX_D1_STARTER.md` v0.1（共通範本）
- `00_protocol/00_j_迭代協議.md` v0.1 §10.3
- `00_protocol/00_l_關係創建協議.md` v0.2
- `.claude/skills/create-relationship/SKILL.md` v0.3（結構範例）
- `_design/ARCHITECTURE.md` v1.6 §5 + §6.7
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050 + §6.16 D-053
