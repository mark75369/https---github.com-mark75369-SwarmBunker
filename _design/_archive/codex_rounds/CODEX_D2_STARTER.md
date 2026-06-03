狀態：DRAFT  
版本：v0.3（9th master Round 2 NO-GO inline patch round — R2-MINOR-01 line 97 indirect 反查表檔名 sweep（05_c/06_a 對齊實際 repo）；R2-MINOR-02 line 180/205 create-character v0.3 → v0.4；歷史紀錄：v0.1 → v0.2 為 Round 1 inline patch 嚴守 D-053 拍板 a + 邊界三 block + 修 04_b 檔名）  
最後更新：2026-05-22  
適用範圍：Phase D Wave 12 task — /iterate-character skill + 中文 wrapper 實作  
優先級：高

# CODEX_D2_STARTER — Phase D Wave 12 D.2：/iterate-character skill 實作

# 0. 本檔用途

Phase D Wave 12 第二條 task — 實作 `/iterate-character` skill（迭代 C-* 角色聲線實體）。對齊 TASKS v1.9 §C.2（第 2 個 /iterate-* skill）+ 00_protocol/00_j_迭代協議.md v0.1 §10.2 + 00_protocol/00_f_角色創建協議.md。

**前置條件：** D.1 PASS（/iterate-world skill 落地；確認 starter pattern 可運作）。

**D.2 PASS → 進 D.3 /iterate-relationship**（可與 D.3-D.5 大幅並行；都共用 00_j 基底）。

⚠ **D-054：** /iterate-character 不動 06_scene_index；不需 D-054 hybrid fallback。

⚠ **慣例：** 本 starter outer agent-prompt fence 用 `~~~`；Instance-only path 加 `<instance_root>/` 前綴。

⚠ **與 D.1 共通骨架：** 本 starter 採「引用 D.1 為共通範本」 + 列差異模式；CODEX 跑本 task 時必先讀 `_design/CODEX_D1_STARTER.md` v0.1 對齊共通結構，再依本 starter 差異規格實作。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 D.2 task」— 實作 /iterate-character skill（含中文 wrapper）；對齊 TASKS v1.9 §C.2 + 00_protocol/00_j_迭代協議.md v0.1 §10.2 + 00_protocol/00_f_角色創建協議.md v0.2。

工作資料夾：D:\劇本開發工具

**共通範本：** 本 task 採與 D.1 (/iterate-world) 相同的 starter pattern。**先讀 `_design/CODEX_D1_STARTER.md` v0.1** 對齊：
- 主 SKILL.md 結構（frontmatter + 中文 5 header + markdown 主體 11 段）
- 5 階段流程（00_j §3 ~ §7）
- 影響範圍評估規範（雙路反查 ARCH §5）
- 邊界區段（D-050 子裁決 1+2 + D-053 紀錄）
- phase_log entry 範例（含 `phase: iterate-character`）
- 啟動前檢查 5 項
- 中文 wrapper 極簡模式

依下方「D.2 差異規格」修改 entity 類型 / protocol 對齊 / 讀寫位置。

**你的身份與職責：**
- 你是 implementer — 本輪建 2 個新 SKILL.md
- D.2 PASS → 可進 D.3 /iterate-relationship

**重要邊界（沿用 D.1）：**
- ✗ 不改 LOCKED spec / registry / parser
- ✗ 不改既有 17 個 SKILL.md（含 /iterate-world v0.1 — 本輪剛建）
- ✗ 不寫 /iterate-relationship（D.3）/ /iterate-outline（D.4）/ /iterate-detailed-outline（D.5）
- ✗ 不重生 view（O3 鎖定）
- ✗ 不改 00_j v0.1

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/iterate-character/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/迭代角色/SKILL.md` | 中文 wrapper |

### /iterate-character 差異規格（vs /iterate-world）

- **觸發語：** `/iterate-character <character_name>`（**接 1 個 user 參數** — 角色名；可選，若 user 不傳則 chat 對話確認目標）
- **對應 protocol：** `00_j v0.1`（共通）+ `00_protocol/00_f_角色創建協議.md v0.2`（C-* 創建協議；當變更涉及 00_f 議題清單時參考）
- **議題清單動態載入：** **適用**（registry key = `00_f_character`）
- **modify entity 範圍：** 單一 C-<character_name>（user 在階段 1 明示）。**00_b §3 屬影響範圍但本 skill 不寫**（依 D-053 嚴守拍板 R1-MA-02；若需動 00_b 屬 user 手動 patch / 開新 D-NNN 拍板擴大 D-053 例外）
- **依賴下游：** 影響範圍主要是 R-*-*（含本角色的關係 entry）+ P / CH-* / S-*-* 間接（弧線 / 出場場景）
- **下游：** 階段 5 印「下一步建議：若需重新看視圖請跑 /view-character <name>；若聲線變動建議重跑 /qa 09_b VOICE_CONSISTENCY」

### 5 階段流程差異（vs /iterate-world）

#### 階段 1：變更點識別

agent 開場（差異 — 明示角色名 + 聲線維度）：

> 請說明你想改角色 C-<name> 的什麼？可以是：
> - 聲線描述（如 cold → cold + 自嘲）
> - 句長偏好 / 標點習慣 / 禁用句型 / 慎用詞
> - 弧線階段（早期 / 中期 / 結局狀態）
> - 角色目標 / 隱藏動機
> - 出場場景偏移
> 
> 越具體越好；空白處我會幫你補洞。

#### 階段 2：強制影響範圍評估

C-* 反查預期清單（給 CODEX 設計時參考；不寫死）：

| 路徑 | 預期檔案 |
|---|---|
| direct | `03_characters/<character_name>_聲線卡.md` |
| depends | `04_relationships/04_a_角色關係矩陣.md`（含本角色的 R-*-* entry）+ `04_relationships/04_b_關係變化時間線.md`（含本角色的時間線 entry）+ `00_b §3`（若有作品專屬規範；屬反查影響範圍，本 skill 不寫 — 依 D-053 嚴守）|
| indirect | `05_plot/05_c_角色弧線表.md`（含本角色的弧線階段）+ `06_scene_index/06_a_場景索引模板.md`（含本角色出場場景）+ 已產出的 `07_scene_tasks/CH<n>_S<m>_*` / `08_dialogue_outputs/*`（若本角色已寫台詞）|

**特別注意（依 00_j §10.2）：** C-* 迭代必含 R-*-* 反查（user 通常忘記 — agent 主動提示）。

下游 pipeline 互鎖：若本角色已產出台詞（08_dialogue_outputs 有 entry），階段 2 必印「以下台詞檔可能因聲線變動需重跑 09_b VOICE_CONSISTENCY」。

#### 階段 3：收斂

依 D.1 共通結構 5 欄位；差異：

- 「本輪要處理的檔案清單」典型含主聲線卡 + 04_a R-entry + （optional）04_b 時間線。**不含 00_b §3**（依 D-053 嚴守；若需動 00_b 屬 user 手動 patch）
- TODO 清單需含「若本角色 LOCKED 場景未跑過 /iterate-scene，建議拍板是否平行解除」

#### 階段 4：執行

寫檔順序：主聲線卡 → 04_a R-entry → 04_b 時間線 entry → phase_log。**不寫 00_b**（依 D-053 嚴守；若需動 00_b §3 → phase_log 標 `external_action_required: 00_b §3 manual patch`）

#### 階段 5：實體驗證

- 列本次更新的 C-* entity ID + 完成度（**不**升新等級）
- 後續建議：「若需重新看視圖請跑 /view-character <name>」/「若聲線變動 → 建議重跑 /qa 09_b」

### .protocol_version phase_log entry 範例

```yaml
- phase: iterate-character
  date: YYYY-MM-DD
  skill: /iterate-character
  status: completed
  modified_entity: C-<character_name>
  modified_files:
    - 03_characters/<character_name>_聲線卡.md
    - 04_relationships/04_a_角色關係矩陣.md
  scope_choice: 2
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  prereq_changed: false
  qa_recheck_recommended: [09_b]  # 若聲線變動
  abort_reason: null
  customizations: []
```

### 啟動前檢查（差異 — 多加 1 項）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在 | 拒絕 |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕 |
| **C-<character_name> 存在** | `03_characters/<character_name>_聲線卡.md` 存在 + frontmatter 含目標 entity ID | 拒絕並提示用 /create-character <name> 建立 |
| LOCKED status check | 目標 C-* 狀態 ≠ LOCKED | 拒絕並印 LOCKED 解除流程 |
| W-rules / V / W-language ≥ REVIEW | 對應分拆檔狀態 | 拒絕並提示先跑 /iterate-world 或確認上游 |
| 下游 pipeline 互鎖 | phase_log 無進行中 /scene-task / /dialogue-write / /qa 引用本 C-* | 拒絕並列衝突 skill |

### 邊界區段（依 D-050 + D-053；對齊 D.1）

含三 block：

三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式：

1. **D-050 子裁決 1：** 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。
2. **D-053 /create-world exception 紀錄（本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-character) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**（含 §3）。若 user 跑 /iterate-character 時需要對 00_b §3 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 00_b §3 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。
3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `03_characters/<character_name>_聲線卡.md`
   > - `04_relationships/04_a_角色關係矩陣.md`（對應 R entry）
   > - `04_relationships/04_b_關係變化時間線.md`（對應時間線 entry；optional）
   > - `.protocol_version.phase_log`
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053）

### 中文 wrapper SKILL.md（迭代角色）

採極簡模式，沿用 D.1 中文 wrapper 結構，指向 `.claude/skills/iterate-character/SKILL.md` 為權威。

---

# 2. CODEX 工作流程

1. 讀必讀（沿用 D.1 §2，外加）：
   - `_design/CODEX_D1_STARTER.md` v0.1（共通範本）
   - `00_protocol/00_f_角色創建協議.md` v0.2
   - `.claude/skills/create-character/SKILL.md` v0.4（/create-character 結構範例 + D-050 + D-053 exception block 對齊；Round 11 R11-CRITICAL-01 修補）
2. 寫 2 個 SKILL.md
3. 跑 baseline 驗證
4. 不跑真實寫檔

---

# 3. 驗收條件（沿用 D.1 §3 5 維度）

| 維度 | 判準 |
|---|---|
| 1. 技術驗證 | 對齊 9th master cleanup 後 baseline |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 |
| 3. 影響範圍評估 | 雙路反查 algorithm + C-* 預期清單表 |
| 4. 邊界紀律 | D-050 + D-053 對齊 Phase B 4 skill 格式 |
| 5. phase_log entry 規範 | 對齊 00_j §6.1 |

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §C.2
- `_design/CODEX_D1_STARTER.md` v0.1（共通範本）
- `00_protocol/00_j_迭代協議.md` v0.1 §10.2（C-* 迭代呼叫指南）
- `00_protocol/00_f_角色創建協議.md` v0.2（對應 entity 創建協議）
- `.claude/skills/create-character/SKILL.md` v0.4（結構範例；Round 11 R11-CRITICAL-01 修補）
- `_design/ARCHITECTURE.md` v1.6 §5 + §6.7
- `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050 + §6.16 D-053
