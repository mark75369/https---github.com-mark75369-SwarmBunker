狀態：DRAFT  
版本：v0.3（9th master Round 2 NO-GO inline patch round — R2-MINOR-01 line 139 indirect 反查表檔名 sweep（05_a/05_b/06_a 對齊實際 repo）；R2-MINOR-02 line 292 create-character v0.3 → v0.4；歷史紀錄：v0.1 → v0.2 為 Round 1 inline patch 嚴守 D-053 拍板 a + 邊界三 block）  
最後更新：2026-05-22  
適用範圍：Phase D Wave 12 task — /iterate-world skill + 中文 wrapper 實作  
優先級：高

# CODEX_D1_STARTER — Phase D Wave 12 D.1：/iterate-world skill 實作

# 0. 本檔用途

Phase D Wave 12 起手第一條 task — 實作 `/iterate-world` skill（迭代上游 W-rules / V / W-language 三類實體；**00_b §1/§2 屬影響範圍但不寫**，依 D-053 嚴守拍板 R1-MA-02）。對齊 TASKS v1.9 §C.2（第 1 個 /iterate-* skill）+ ARCH v1.6 §5 影響範圍評估 + §6.7 共通骨架 + 00_protocol/00_j_迭代協議.md v0.2 + 00_protocol/00_e_世界觀創建協議.md（對應 entity 創建協議）。

**前置條件：** Phase C 收尾 + Milestone 3 達成 + 9th master cleanup queue 處理完（00_k v0.2 / AGENTS / CLAUDE 等對齊）+ 00_j v0.1 已寫好。

**D.1 PASS → Phase D Wave 12 進 D.2 /iterate-character skill 實作**（D.1 → D.2 → D.3 → D.4 → D.5 可大幅並行；都共用 00_j 基底）。

⚠ **D-054 拍板對齊（無直接落地需求）：** /iterate-world 不動 06_scene_index；不需 D-054 hybrid fallback。

⚠ **「Fix one, find two」cascade pattern 預防（HANDOFF §4.6 紀律；9th master 已內化）：**
- 寫 starter 含 spec enum 引用前，先 grep SPEC / parser code / UD verify enum 列表完整 + 拼字正確
- 寫好 starter 後跑 grep 全掃 stale cross-ref

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 12 D.1 task」— 實作 /iterate-world skill（含中文 wrapper）；對齊 TASKS v1.9 §C.1 + §C.2 + ARCH v1.6 §5 影響範圍評估 + §6.7 共通骨架 + 00_protocol/00_j_迭代協議.md v0.1 + 00_protocol/00_e_世界觀創建協議.md。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase D Wave 12 第一條 task（D.1 → D.2 → D.3 → D.4 → D.5 共用 00_j 基底）；/iterate-world 是 5 個 /iterate-* 系列的第一個
- D.1 PASS → 可進 D.2 /iterate-character skill 實作

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_j v0.1；它是本 skill 對應 protocol — 本輪不修改）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 16 個 SKILL.md（init-project / status / check-gaps / create-* x5 + 5 中文 wrapper + scene-task / dialogue-write / qa + 3 中文 wrapper）
- ✗ **不**寫 /iterate-character（D.2 scope）/ /iterate-relationship（D.3）/ /iterate-outline（D.4）/ /iterate-detailed-outline（D.5）
- ✗ **不**自動 trigger 階段 4 寫檔（屬 user 拍板）
- ✗ **不**跑真實 /iterate-world 寫檔（會污染 Template；端到端測試屬 user 親跑 M4）
- ✗ **不**重生 view 整合檔（O3 鎖定；屬 /export-* scope）
- ✗ **不**改 D-054 / NEW_REQ_15 / 任何 DECISIONS_LOG 拍板紀錄

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.2（line 1463-1486）+ 00_j v0.1 §10.1（W-rules 迭代呼叫指南）+ ARCH §5 雙路反查 + SPEC §11 影響範圍評估。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/iterate-world/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/迭代世界觀/SKILL.md` | 中文 wrapper |

### /iterate-world 主 SKILL.md 結構（依 ARCH §3.3 + 沿用 Wave 7 + Wave 9 範式）

每主 SKILL.md 頂部含：

- frontmatter（name + description 50-200 字；明示「迭代 W-rules / V / W-language；對齊 00_j 基底協議 5 階段；嚴守 D-053 不寫 00_b」）
- 中文 5 必填 header（狀態：DRAFT / 版本：v0.1 / 最後更新：YYYY-MM-DD / 適用範圍：/iterate-world skill runtime instructions / 優先級：高）
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（英文 slash command `/iterate-world` + 中文別名 `/迭代世界觀` reference）
  - `## 觸發協議`（對應 00_j v0.1 5 階段 + 00_e v0.1 對應 entity 創建協議 + 必讀 references）
  - `## 啟動前檢查`（D-049 Template-detect + Bootstrap completed + W-rules / V / W-language 既有實體存在 + LOCKED status check + 下游 pipeline 互鎖檢查 per 00_k §10.7.5）
  - `## 流程`（5 階段對應 00_j §3 ~ §7：變更點識別 / 強制影響範圍評估 / 收斂 / 執行 / 實體驗證）
  - `## 影響範圍評估規範`（**本 skill 核心 — 詳下方規格；不可省略**）
  - `## .protocol_version 寫入規範`（phase_log entry 對應 00_j §6.1）
  - `## 輸入`（user 變更意圖 — chat 對話接受 + 可選 modified_entity 明示）
  - `## 輸出`（修改 01_world/ + 02_vocabulary/；**不寫 00_b**；含 frontmatter `depends_on` 補完；若需動 00_b §1/§2 則 phase_log 標 `external_action_required: 00_b §1/§2 manual patch`）
  - `## 邊界`（D-050 子裁決 1 + 子裁決 2 + D-053 exception block 對齊 Phase B skill 格式）
  - `## 錯誤處理 / Rollback`（沿用 00_j §6 階段 4 rollback 紀律）
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### /iterate-world 差異規格

- **觸發語：** `/iterate-world`（不接 user 參數；變更目標由 chat 對話確認）
- **對應 protocol：** `00_protocol/00_j_迭代協議.md v0.1`（共通基底）+ `00_protocol/00_e_世界觀創建協議.md v0.1`（對應 entity 創建協議；當變更涉及 00_e 議題清單時參考）
- **議題清單動態載入：** **適用**（若 user 變更目標含新增 issue → 從 `<instance_root>/issue_type_registry.yaml` 的 `00_e_world` key 讀；user_extensions / core_overrides 一併讀）
- **modify entity 範圍：** W-rules / V / W-language（任一或多個；user 在階段 1 明示）。**00_b §1/§2 屬影響範圍但本 skill 不寫**（依 D-053 嚴守拍板 R1-MA-02；若需動 00_b 屬 user 手動 patch / 開新 D-NNN 拍板擴大 D-053 例外）
- **依賴下游：** 影響範圍最廣 — 含 C-* / R-*-* / P / CH-* / S-*-* 全依賴 W-rules（per 00_j §10.1 特別注意）
- **下游：** 階段 5 印「下一步建議：若需重新看視圖請跑 /export-world；若 02_c 禁用詞變動建議重跑 /qa」；**不**自動 trigger

### 5 階段流程（對齊 00_j §3 ~ §7）

#### 階段 1：變更點識別（依 00_j §3）

agent 開場：

> 請說明你想改世界觀（W-rules / V / W-language）的什麼？可以是：
> - 新增世界規則 / 語言層級 / 詞彙
> - 修改既有設定（如某個禁用詞改慎用詞）
> - 補洞（針對某 entity 加更細節）
> - Canon Delta 回寫（從 09_e §9 紀錄某場台詞建立的新事實）
> 
> 越具體越好；空白處我會幫你補洞。

agent 產出**變更點識別報告**（6 必含項；詳 00_j §3）：

1. 變更目標 entity（W-rules / V / W-language 之一或多個）
2. 變更類型分類（新增 / 修改 / 刪除 / 重組）
3. 變更具體內容
4. 既有實體當前狀態（DRAFT / REVIEW / FINAL / LOCKED）
5. 預估影響範圍（粗略）
6. 建議下一步

#### 階段 2：強制影響範圍評估（依 00_j §4）

**這是 /iterate-* 核心差異 — 不可省略，即使 user 明示「直接寫檔」。**

agent 對每個變更目標 entity 跑雙路反查：

- 路徑 A：`entities` 含 modified_entity 的檔案（直接受影響 — 「貢獻」關係）
- 路徑 B：`depends_on` 含 modified_entity 的檔案（依賴受影響 — 「使用」關係）
- 路徑 C：間接受影響（兜底）

W-rules 反查預期清單（給 CODEX 設計時參考；不寫死）：

| 路徑 | 預期檔案 |
|---|---|
| direct | `01_world/01_a_世界觀總覽.md` |
| depends | `01_world/01_b_世界語言規格.md` / `01_world/01_c_陣營與階級語言.md` / `02_vocabulary/02_a_專有名詞表.md` / `02_vocabulary/02_b_俗稱與黑話表.md` / `02_vocabulary/02_c_禁用詞與慎用詞表.md` / `03_characters/*_聲線卡.md`（所有 C-*）/ 可能 `04_relationships/04_a_角色關係矩陣.md` |
| indirect | `05_plot/05_a_主線大綱模板.md` / `05_plot/05_b_章節結構模板.md` / `06_scene_index/06_a_場景索引模板.md` / `00_b_反ai味檢查表.md` §1/§2（影響範圍但本 skill 不寫；屬 user 手動 patch）|

agent 在 chat 印影響範圍評估表（依 00_j §4.3 格式），問 user 拍板處理範圍（4 個選項）。

下游 pipeline 互鎖：若 W-rules 改動影響 V 禁用詞 / 句型 → 進行中的 /qa 受影響 → 階段 2 拒絕並列出衝突 skill；user 拍板等待 / 中止 / 強制。

#### 階段 3：收斂（依 00_j §5）

agent 整合階段 2 user 拍板範圍 → 產出**收斂預告稿**（5 欄位；詳 00_j §5）：

1. 變更目標 entity + 最終結論一句話
2. 本輪要處理的檔案清單（含完整路徑）
3. 每檔案的具體變更動作（新增段落 / 修改欄位 / 刪除內容 / frontmatter 更新）
4. TODO 清單（無法完成需後續補的項）
5. 影響範圍預告（LOCKED 檢查、FINAL 處理、phase_log prereq_changed）

等 user 「通過 / OK / 寫檔」才進階段 4。

#### 階段 4：執行（依 00_j §6）

寫檔順序：主分拆檔 → 衍生分拆檔 → phase_log。任一步出錯 rollback。**不寫 00_b**（依 D-053 嚴守）。

- 寫 `01_world/01_a` 等主分拆
- 寫 `02_vocabulary/02_*` 衍生分拆
- **不寫** `00_b §1/§2`（若 user 變更涉及 00_b §1/§2 → phase_log 標 `external_action_required: 00_b §1/§2 manual patch`；agent 印「請 user 手動 patch 00_b 或開新 D-NNN 拍板擴大 D-053 例外」）
- frontmatter 補完 `depends_on`
- `.protocol_version.phase_log` append（依 00_j §6.1 格式；含 `phase: iterate-world`）

#### 階段 5：實體驗證（依 00_j §7）

自動 `/status`：

- 列本次更新的 W-rules / V / W-language entity ID + 完成度
- 列寫入檔案清單
- expected entity manifest 對照
- 後續建議：「若需重新看視圖請跑 /export-world」/「若 02_c 變動 → 建議重跑 /qa 09_c 禁用詞檢查」

**不可：** 自動跑下一個 skill / 自動升 entity 狀態 / 自動重生 view。

### .protocol_version phase_log entry 範例

```yaml
- phase: iterate-world
  date: YYYY-MM-DD
  skill: /iterate-world
  status: completed
  modified_entity: W-rules  # 或 V / W-language / 多個
  modified_files:
    - 01_world/01_a_世界觀總覽.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
  scope_choice: 2  # 1/2/3/4 對應階段 2 user 拍板範圍
  affected_files_evaluated:
    direct: [...]
    depends: [...]
    indirect: [...]
  prereq_changed: false
  qa_recheck_recommended: [09_c]  # 若 02_c 變動
  abort_reason: null
  customizations: []
```

### 啟動前檢查（嚴格條件）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在（屬 Instance）| 拒絕並提示用 /init-project 建 Instance |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕並提示用 /init-project |
| W-rules / V / W-language 存在 | 對應分拆檔 frontmatter 含目標 entity | 拒絕並提示用 /create-world 建立 |
| LOCKED status check | 目標 entity 狀態 ≠ LOCKED | 拒絕並印 LOCKED 解除流程（00_j §9.3）|
| 下游 pipeline 互鎖 | phase_log 無進行中 /scene-task / /dialogue-write / /qa 引用本 entity | 拒絕並列衝突 skill；user 拍板（00_j §4.4）|

### 邊界區段（依 D-050 + D-053；9th master Round 1 inline patch — 嚴守 D-053 範圍）

含三 block 對齊 Phase B 4 個 /create-* skill v0.3/v0.4 格式：

1. **D-050 子裁決 1（all /create-* + /iterate-* skill 嚴禁寫 00_protocol/）：**
   > 本 skill 嚴禁寫入 `00_protocol/` 任何檔（含 00_b）。D-050 子裁決 1 規定唯一例外是 /init-project skill；本 skill 不在例外範圍。

2. **D-053 /create-world exception（紀錄但本 skill 不在例外範圍）：**
   > D-053 partial supersede D-050 子裁決 1 — **/create-world 可寫 00_b §1/§2** Instance-specific section。本 skill (/iterate-world) **不在 D-053 例外範圍**；**不可寫 00_b 任何段**。若 user 跑 /iterate-world 時需要對 00_b §1/§2 做同步調整，agent 必須印「00_b 不在本 skill 寫檔範圍；請 user 手動 patch 00_b §1/§2 或開新 D-NNN 拍板擴大 D-053 例外」並列入 phase_log 的 `external_action_required` 欄位。

3. **D-050 子裁決 2（寫檔目錄表）：**
   > 本 skill 寫檔範圍嚴格限：
   > - `01_world/01_a_世界觀總覽.md`
   > - `01_world/01_b_世界語言規格.md`
   > - `01_world/01_c_陣營與階級語言.md`
   > - `02_vocabulary/02_a_專有名詞表.md`
   > - `02_vocabulary/02_b_俗稱與黑話表.md`
   > - `02_vocabulary/02_c_禁用詞與慎用詞表.md`
   > - `.protocol_version.phase_log` runtime tracking
   > **不含 `00_protocol/00_b_反ai味檢查表.md`**（依 9th master Round 1 R1-MA-02 拍板 a 嚴守 D-053；/iterate-* 全部不寫 00_b）

### 中文 wrapper SKILL.md 結構（迭代世界觀）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 迭代世界觀
description: "/iterate-world skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/iterate-world skill 中文觸發 wrapper  
優先級：高

# /迭代世界觀（/iterate-world wrapper）

本 wrapper 是 `/iterate-world` 的中文別名。執行時以英文主檔 `.claude/skills/iterate-world/SKILL.md` 為權威。

請參考 `.claude/skills/iterate-world/SKILL.md`。
```

不建立第二套流程。

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：
   - `_design/TASKS.md` v1.9 §C.1（00_j 已實作；不修改）+ §C.2（5 個 /iterate-* skill task spec）
   - `_design/ARCHITECTURE.md` v1.6 §3.3（skill 內容規範）+ §5（影響範圍評估）+ §6.7（共通骨架 5 階段）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）+ §11（影響範圍評估規範）
   - `00_protocol/00_j_迭代協議.md` v0.1（本 skill 對應 protocol；共通基底）
   - `00_protocol/00_e_世界觀創建協議.md` v0.1（對應 entity 創建協議；本 skill iterate 對應實體）
   - `.claude/skills/create-world/SKILL.md` v0.1（/create-world 結構範例；本 skill 沿用同 frontmatter / 中文 header / 結構規範）
   - `_design/DECISIONS_LOG.md` v2.0 §6.12 D-050（寫檔邊界）+ §6.16 D-053（/create-world exception；本 skill 不在例外但需紀錄）+ §6.7 C-9（depends_on frontmatter）

2. **寫 SKILL.md 2 個**（依 §1 「任務目標」表）：
   - 英文主檔 `.claude/skills/iterate-world/SKILL.md`（依本 starter §1「主 SKILL.md 結構」 + 「差異規格」 + 「5 階段流程」 + 「邊界區段」）
   - 中文 wrapper `.claude/skills/迭代世界觀/SKILL.md`（依本 starter §1「中文 wrapper SKILL.md 結構」）

3. **跑 baseline 驗證**（不寫實際 .protocol_version 紀錄；Template repo 端）：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - `python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; ..."`
   - 對比 9th master cleanup 後 baseline（check_headers 0 ERROR / check_paths ≤ 243 ERRORS / build_repo_index 0 ERROR on Windows）

4. **不跑真實 /iterate-world 寫檔**（會污染 Template；M4 testing 屬 user 親跑）

5. **撰寫 review report**（可選；若 D.2-D.5 task 待跑，可推 9th master 對話統合驗收）

---

# 3. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index baseline | 對齊 9th master cleanup 後 baseline；無新 ERROR |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 影響範圍評估 | SKILL.md 含 `## 影響範圍評估規範` 段 + 雙路反查 algorithm + 預期清單表 | 對齊 ARCH §5 + 00_j §4 |
| 4. 邊界紀律 | D-050 子裁決 1 + 子裁決 2 + D-053 紀錄 block 對齊 Phase B 4 skill 格式 | 與 create-character v0.4 / create-relationship v0.3 / create-outline v0.3 / create-detailed-outline v0.3 對齊 |
| 5. phase_log entry 規範 | SKILL.md 含 phase_log entry 範例 | 對齊 00_j §6.1 |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**自動 trigger 階段 4 寫檔（屬 user 拍板）
- **不**重生 view 整合檔（O3 鎖定）
- **不**升 entity 狀態
- **不**呼叫其他 skill
- **不**改 LOCKED spec / registry / parser code
- **不**改既有 SKILL.md（含 create-world v0.1；本 skill 是新建，不動既有）
- **不**改 00_j（本輪不修改 protocol 基底）

「Fix one, find two」cascade pattern 預防（HANDOFF §4.6）：

- 寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 reference / file path / D-NNN 引用）
- 一次性 sweep 避免局部修補導致 cascade

---

# 5. Cross-ref

- `_design/TASKS.md` v1.9 §C.1（00_j 已實作）+ §C.2（5 個 /iterate-* skill）
- `_design/ARCHITECTURE.md` v1.6 §5（影響範圍評估）+ §6.7（共通骨架）
- `_design/SPEC.md` v1.2 §5.2 + §11
- `00_protocol/00_j_迭代協議.md` v0.1（共通基底；本輪不修改）
- `00_protocol/00_e_世界觀創建協議.md` v0.1（對應 entity 創建協議）
- `.claude/skills/create-world/SKILL.md` v0.1（/create-world 結構範例）
- `_design/DECISIONS_LOG.md` v2.0 §6.7 C-9 + §6.12 D-050 + §6.16 D-053 + §6.17 D-054（NEW_REQ_15）
- `_design/POST_LOCK_PENDING.md` v0.14 NEW_REQ_15 trigger A/B/C/D（D-054 hybrid 迭代評估）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（第九輪 master scope）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Milestone 3 達成事實檔）
