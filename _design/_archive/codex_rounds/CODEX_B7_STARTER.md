狀態：DRAFT  
版本：v0.3（D-050 supersede + §6.16 重審 MA-02 — §1 內文 §10.11/§10.12 stale ref 全修為 §10.7/§10.8）  
最後更新：2026-05-21  
適用範圍：Phase B Wave 8 B.7 task 啟動包 — /create-detailed-outline skill 實作  
優先級：高

# CODEX_B7_STARTER — Phase B Wave 8 B.7：/create-detailed-outline skill 實作

# 0. 本檔用途

Wave 8 第一條 task — 實作 `/create-detailed-outline` skill（含中文別名 `/建立細綱`），對應 00_h 細綱創建協議 v0.2 跑 5 階段 + D-047 動態議題清單機制 + B.6.5 PASS 啟動條件檢查。

> **v0.1 → v0.3 D-050 supersede + stale ref cleanup 註記（2026-05-21）：**
>
> v0.1 寫作時 DECISIONS_LOG 為 v1.4（未含 D-050）；§1 啟動 prompt 內原本引用 00_h §10.11 拆分規則 + §10.12 frontmatter + 寫檔範圍 05_b/c/d/e + 06_a。**這些引用已被 DECISIONS_LOG v1.5 §6.12.2 D-050 supersede。**
>
> v0.2 加 supersede header note 標明；v0.3（本輪 §6.16 重審 MA-02 patch）把 §1 內文 stale reference 一併修正：
> - §10.11 → **§10.7**（00_h v0.2 實際拆分規則章節）
> - §10.12 → **§10.8**（00_h v0.2 實際 frontmatter 章節）
>
> **D-050 正確 scope（CH `/create-detailed-outline`）：**
> - 寫檔目錄：**`05_plot/05_b`（章節結構）+ `06_scene_index/06_a`（場景索引）only**
> - 不寫：`05_c`（屬 P /create-outline）/ `05_d` / `05_e`（屬 P /create-outline 議題 4/5）/ `00_protocol/`（D-050 子裁決 1 嚴禁）
>
> B.7 CODEX 對話中讀最新 DECISIONS_LOG v1.5 後**自主對齊 D-050 + 00_h §10.7/§10.8**，產出 `.claude/skills/create-detailed-outline/SKILL.md` v0.1 完整對齊 D-050。Round 2 review 已 PASS（git commit `da305a5`）。
>
> 本 starter v0.3 屬 archive 性質；未來 cross-ref 應同時讀本 supersede note + D-050 §6.12.2 + 既有 SKILL.md v0.1 為權威。

**前置條件：**
- Wave 6 ✓（00_h v0.2 含 §2 啟動條件 issue_type_registry + §4.0 動態構建 + §4.1 議題預設表 6 議題）
- Wave 7 ✓（B.5 / B.5b / B.6 三 skill 已實作；B.5.5 / B.6.5 起手包已交付）
- issue_type_registry.template.yaml ✓ LOCKED v0.1（含 00_h_detailed_outline skill key 區段）

**與 B.8 / B.9 的並行性：** B.7 必須先於 B.8 / B.9（B.8 需 CH-\* / S-\*-\* 實體 existing 才能 review；B.9 需全套 5 skill PASS 才能整體驗收）。Wave 8 三 task **不可平行**，依序跑 B.7 → B.8 → B.9。

⚠ **新慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`（避免內部 nest ` ``` ` 觸發 FENCE_RE toggle 錯亂）
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴（PATH_RE lookbehind 阻擋 match）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase B Wave 8 B.7 task」— 實作 `/create-detailed-outline` skill（含中文 wrapper），對應 00_h 細綱創建協議 v0.2 + D-047 動態議題清單機制 + B.6.5 PASS 啟動條件檢查。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（英文 skill + 中文 wrapper）
- 對應傳統：Wave 8 第一條 task（B.8 / B.9 依序在後）
- 本 skill 為 Phase B 最後一個 /create-* skill；其產出 CH-* + S-*-* 是 Phase C /scene-task + /dialogue-write 的上游

**重要邊界（嚴格 scope）：**

- ✗ 不改任何 LOCKED spec / registry / parser code
- ✗ 不改 00_protocol/00_h_細綱創建協議.md（Wave 6 已 patch v0.2）
- ✗ 不改既有 27 模板 / 其他 00_protocol/ 檔
- ✗ 不動 _tools/frontend/ 任何檔
- ✗ 不改 Wave 7 既有 .claude/skills/create-character / create-relationship / create-outline / 中文 wrapper（已實作 v0.1）
- ✗ 不寫 W-rules / W-language / V / C-* / R-* / P / CH-* / S-* 實際內容（skill 跑時動作，不是 SKILL.md 內容）
- ✗ 不提及任何具體作品 / 角色名

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.7（line 1349-1364）+ 00_protocol/00_h v0.2 完整 protocol + INTEGRATION_CONTRACTS v2.1 §4a Contract D（D-047）+ `_design/registries/issue_type_registry.template.yaml` v0.1 `00_h_detailed_outline` 區段 + DECISIONS_LOG v1.9 §6.12.2 D-050 子裁決 2 + §6.16.2 D-053 supersede。

### 任務目標

新建 2 個 SKILL.md：
1. `.claude/skills/create-detailed-outline/SKILL.md` — 英文 skill 主檔
2. `.claude/skills/建立細綱/SKILL.md` — 中文 wrapper

### SKILL.md 內容規範

frontmatter（at minimum）：

```
---
name: create-detailed-outline
description: 把主線 P 拆成章節（CH-*）與場景索引（S-*-*）的 Phase B skill。依 00_h 細綱創建協議 v0.2 跑 5 階段：診斷 → 探索（動態讀 issue_type_registry.yaml 的 00_h_detailed_outline 議題清單）→ 收斂 → 執行寫檔（D-050 子裁決 2 CH 行限定：05_b 章節結構 + 06_a 場景索引 only；不寫 05_c/d/e 屬 P /create-outline scope）→ 驗證 + 自動呼叫 /status。啟動條件：P 至少 REVIEW（B.6.5 PASS）；對齊 D-047 議題清單動態構建機制。
---
```

### 英文 skill 內容結構（依 00_h v0.2 protocol）

1. **觸發語：** `/create-detailed-outline`（對話式引導，不直接接 user 參數）

2. **啟動前依賴檢查（依 00_h §2）：**
   - `<instance_root>/.protocol_version` 已存在（即 Instance 已 bootstrap）— 若無提示先跑 /init-project
   - `.protocol_version.phase_log` 至少含 `phase: create-outline` + `status: completed` — 若無提示先跑 /create-outline
   - P 實體（`05_plot/05_a_主線大綱.md`）frontmatter status 至少 REVIEW（B.6.5 PASS）— 若仍 DRAFT 拒絕並提示「請先跑 B.6.5 主線 REVIEW gate（依 CODEX_B65_REVIEW_GATE_STARTER）」
   - `.protocol_version.phase_log` 不存在 `phase: create-detailed-outline` + `status: completed`（若有改建議跑 /iterate-detailed-outline，Phase C skill 屆時實作）
   - `<instance_root>/issue_type_registry.yaml` 可讀（D-047 對齊；若不存在從 _design/registries/issue_type_registry.template.yaml fallback + WARN）；對應 `00_h_detailed_outline` skill key 必須存在

3. **5 階段流程（依 00_h §3 ~ §7）：**

   - **階段 1 診斷**：依 00_h §3 — agent 開場提示 + user 貼長段細綱想法（章節劃分 / 場景節奏 / 角色弧線進度 / 資訊揭露順序 / 伏筆回收等）+ agent 用 00_a 診斷模式產出診斷報告（chat-only，不寫檔）。診斷報告須預告階段 2 會跑 registry core 預設 6 個 user-facing 議題。

   - **階段 2 探索（D-047 動態議題清單核心）：**
     - **必須**讀 `<instance_root>/issue_type_registry.yaml` `00_h_detailed_outline` skill key 區段
     - 按 `core + user_extensions − core_overrides` 動態構建議題清單
     - 套用 core_overrides 過濾：對 `locked=true` 議題的 skip → 忽略 + WARN；對 `locked=false` 議題的 skip → 移除；不存在於 core 的 skip_id → WARN ignore
     - 議題順序：先 core 依 id 升序（id 1-99）→ 再 user_extensions 依 id 升序（id ≥ 100）
     - 對每議題依 `required_level` 決定行為（REQUIRED → 缺漏拒進階段 4；STRONGLY_PREFERRED → 跳過時 phase_log 紀錄 + 對應分拆檔標 TODO；OPTIONAL → 允許跳）
     - 完整提問腳本以 `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.4.2 對應段為**權威來源**（不擅自重寫 / 不擅自濃縮）；本檔 00_h §10 為 speed reference
     - 拆分規則（§10.7）**不**對 user 提問，屬階段 4 mechanic

   - **階段 3 收斂**：agent 把累積答案整合成「細綱收斂預告稿」（依 00_h §5；含拆分計畫 + 章節清單 + 各章節下場景索引清單 + TODO/INFERENCE/CONFLICT 清單 + 即將新建實體 CH-* / S-*-* + 不處理清單 + 與 P 主線對齊驗證）

   - **階段 4 執行（依 00_h §10.7 拆分規則 + D-050 子裁決 2 CH 行限定）：**
     - 把答案依 §10.7 拆分計畫表寫到 **D-050 允許的 2 個位置 only**（具體 mapping 以 00_h §10 + UD §1.4 + D-050 為權威）：
       - 章節結構主檔：`05_plot/05_b_章節結構.md`（覆寫；frontmatter entities=[CH-*] 多個）— **章節 + 角色弧線 + 資訊揭露 + 伏筆全部寫進此檔的對應段，不分拆到 05_c/05_d/05_e**
       - 場景索引：`06_scene_index/06_a_場景索引模板.md`（聚合式寫入；frontmatter entities=[S-*-*]）— per-scene 拆檔屬未來 NEW_REQ_13 deferred 範圍
     - **不寫**（D-050 子裁決 2 CH 行越界）：
       - `05_plot/05_c_角色弧線表.md`（屬 P /create-outline 議題 4 觸發的高層 placeholder；entities=[P]）
       - `05_plot/05_d_資訊揭露表.md`（屬 P /create-outline 議題 4）
       - `05_plot/05_e_伏筆與回收表.md`（屬 P /create-outline 議題 5）
       - `00_protocol/` 任何檔（D-050 子裁決 1 嚴禁）
     - 寫檔順序：05_b → 06_a（章節結構 → 場景索引）
     - frontmatter 規範（依 00_h §10.8 + skill 規則）：
       - `05_b`：entities=[CH-01, CH-02, ...]、depends_on=[P]、weight CH=0.3
       - `06_a`：entities=[S-01-01, S-01-02, ...]、depends_on=[P, CH-*]、weight S=0.2
     - phase_log entry append：
       ```yaml
       - phase: create-detailed-outline
         date: <ISO date>
         skill: /create-detailed-outline
         status: completed
         created_entities: [CH-1, CH-2, ..., S-1-1, S-1-2, ..., S-n-m]
         issue_completions: {<議題 id>: <答完/跳過>, ...}
       ```

   - **階段 5 驗證**：依 00_h §7 — 自動呼叫 `/status` skill 顯示 CH-* / S-*-* 完成度 + P 完成度連動 + 建議下一步 Phase C `/scene-task <scene_id>`（屆時實作）

4. **D-047 對齊（必含段）：**
   - skill 啟動時必須讀 `<instance_root>/issue_type_registry.yaml`
   - 異常 fallback：registry 不存在 → Template fallback + WARN；schema 異常 → 拒絕進階段 2
   - registry hot-reload：本 skill 啟動讀一次；不支持 mid-session reload（user 改 registry 需 restart skill）

5. **禁止事項：**
   - 不得擅自跳階段（5 階段順序鎖死）
   - 不得擅自補完 user 未提供的章節結構（標 TODO 或 INFERENCE）
   - 不得擅自更動 issue_type_registry.yaml（user 修改責任）
   - 不得擅自覆寫 LOCKED 檔（檢查 header.狀態）
   - 不得在 P 還是 DRAFT 時繼續（必須先 B.6.5 PASS）
   - 不得在本協議建角色 / 關係 / 主線 / 台詞（屬其他 /create-* / /scene-task）
   - 不擅自呼叫其他 /create-* skill（即使階段 5 建議了下一步）
   - 不得擅自升 P / CH-* / S-*-* status（升 status 屬 B.8 人類 REVIEW gate 範圍）

### 中文 wrapper（.claude/skills/建立細綱/SKILL.md）

採極簡 wrapper：
- frontmatter：name: 建立細綱 / description: /create-detailed-outline 中文別名
- 主體：引用英文版 SKILL.md 為權威

### 文字長度建議

英文 skill ~250-350 行（含 5 階段詳細指引 + D-047 機制段 + frontmatter 規範 + 禁止事項）；中文 wrapper ~20-30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§B.7 line 1349-1364）
2. `00_protocol/00_h_細綱創建協議.md` v0.2（完整 §1-§10 + §10.7 拆分規則 + §10.8 frontmatter 規範 + §4.0 D-047 機制段 + §4.1 議題預設表 6 議題）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.4（7 議題完整提問腳本權威來源；§1.4.1 區段 1-9 + §1.4.2 區段 10 7 議題 agent 提問腳本）
4. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D（D.1 schema / D.2 Phase B 行為 / D.3 衝突處理）

B. D-047 對齊核心
5. `_design/registries/issue_type_registry.template.yaml` v0.1（00_h_detailed_outline 區段）
6. `_design/DECISIONS_LOG.md` v1.9 §6.9.2 D-047 + §6.12.2 D-050 + §6.16.2 D-053

C. 對齊參考（Wave 7 同模式 skill）
7. `.claude/skills/create-outline/SKILL.md` v0.1（Wave 7 B.6 既有 — 同模式 implementation 範本）
8. `.claude/skills/create-character/SKILL.md` v0.1（Wave 7 B.5 既有 — D-047 機制段範本）

D. 對齊參考（spec 框架）
9. `_design/ARCHITECTURE.md` v1.5 §3.3（skill 內容規範）+ §3.3.0（multi-agent invocation 慣例）
10. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log + status enum）
11. `_design/SPEC.md` v1.2 §5.1（CH-* / S-*-* entity 定義）+ §5.3（完成度公式）+ §17（00_b 7 anchor）

E. 已 LOCKED 不可動文件
12. 所有 `_design/*.md`
13. `_design/registries/*.template.yaml`
14. `scripts/*.py`
15. 既有 27 模板
16. 所有 `00_protocol/` 檔（Wave 6 全部 patch v0.2 已 master patched）
17. Wave 7 既有 `.claude/skills/create-character / create-relationship / create-outline / 建立角色 / 建立關係 / 建立大綱/SKILL.md` v0.1
18. Wave 7 既有 Phase A `.claude/skills/init-project / create-world / status / check-gaps / 4 中文 wrapper /SKILL.md`
19. `_tools/frontend/*`

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/create-detailed-outline/SKILL.md` v0.1
2. `.claude/skills/建立細綱/SKILL.md` v0.1

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name / description）+ 5 必填中文 header
- 中文 wrapper 引用英文版

B. 內容
- 5 階段流程完整對齊 00_h v0.2 protocol
- 啟動前依賴檢查含 P REVIEW 條件（拒絕 DRAFT）
- 階段 2 完整 D-047 機制段（讀 registry / core + user_extensions − core_overrides / locked 規則 / required_level 行為 / UD §1.4.2 為權威）
- 階段 4 拆分規則完整對齊 00_h §10.7；寫檔範圍依 D-050 子裁決 2 CH 行限定 05_b + 06_a only（不寫 05_c/d/e — 屬 P /create-outline scope）
- 階段 4 frontmatter 規範對齊 00_h §10.8
- phase_log entry 含 status=completed + created_entities=[CH-*, S-*-*]
- 階段 5 自動呼叫 /status
- 禁止事項明示（不擅自跳階段 / 不擅自補完 / P 仍 DRAFT 時拒絕 / 不擅自呼