狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.6 task 啟動包 — /create-world skill 實作  
優先級：高

# CODEX_A6_STARTER — Phase A 後段 A.6：/create-world skill 實作

# 0. 本檔用途

Wave 3 第二條 task — 實作 `/create-world` skill（含中文別名 `/建立世界觀`），對應 00_e 世界觀創建 protocol 跑 5 階段 + D-047 動態議題清單機制。

**前置條件：** A.3 ✓（00_e 含 §4.0 D-047 機制段）+ issue_type_registry.template.yaml ✓ LOCKED v0.1。

**與 A.5 / A.0F.2 平行性：** 三條動的檔完全不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.6 task」— 實作 `/create-world` skill（含中文 wrapper），對應 00_e 世界觀創建 protocol + D-047 動態議題清單機制。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（英文 skill + 中文 wrapper）
- 對應傳統：Wave 3 第二條 task（與 A.5 / A.0F.2 平行可跑）
- skill 為 Phase B `/create-*` 第一個落地 D-047 機制的實作

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改 `00_protocol/00_e_世界觀創建協議.md`（已 master patched）
- ✗ **不**改既有 27 模板 / 其他 `00_protocol/` 檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**寫其他 /create-* skill（屬 Phase B）
- ✗ **不**寫 W-rules / W-language / V 實際內容（skill 跑時動作，不是 SKILL.md 內容）
- ✗ **不**提及任何具體作品 / 角色名

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.6（line 705-725）+ 00_protocol/00_e 完整 protocol + INTEGRATION_CONTRACTS v2.1 §4a Contract D（D-047 D.1-D.4）+ `_design/registries/issue_type_registry.template.yaml` v0.1。

### 任務目標

新建 2 個 SKILL.md：
1. `.claude/skills/create-world/SKILL.md` — 英文 skill 主檔
2. `.claude/skills/建立世界觀/SKILL.md` — 中文 wrapper

### SKILL.md 內容規範

frontmatter（at minimum）：
```
---
name: create-world
description: 建立作品世界觀（W-rules / W-language / V 三實體 + 作品專屬 00_b §1/§2）。依 00_e_世界觀創建協議 跑 5 階段：診斷 → 探索（動態讀 issue_type_registry.yaml 構建議題清單）→ 收斂 → 執行寫檔（自動拆分到 01_a/01_b/01_c/02_a/02_b/02_c + 00_b §1/§2）→ 驗證 + 自動呼叫 /status。對齊 D-047 議題清單動態構建機制。
---
```

### 英文 skill 內容結構（依 00_e protocol）

1. **觸發語：** `/create-world`（對話式引導，不直接接 user 參數）
2. **依賴：**
   - `.protocol_version` 已存在（即已 bootstrap）— 若無，提示 user 先跑 `/init-project`
   - `.protocol_version.phase_log` 不存在 `phase: create-world` + `status: completed`（若有，改建議跑 `/iterate-world`）
   - `<instance_root>/issue_type_registry.yaml` 可讀（D-047 對齊；若不存在從 Template fallback + WARN）
3. **5 階段流程（依 00_e §3 ~ §7）：**
   - **階段 1 診斷**：依 00_e §3 — agent 開場提示 + user 貼長段世界觀想法 + agent 用 00_a 診斷模式產出診斷報告（chat-only，不寫檔）
   - **階段 2 探索（D-047 動態議題清單核心）：**
     - **必須**讀 `<instance_root>/issue_type_registry.yaml` `00_e_world` skill key 區段
     - 按 `core + user_extensions − core_overrides` 動態構建議題清單
     - 套用 core_overrides 過濾：對 locked=true 議題的 skip → 忽略 + WARN；對 locked=false 議題的 skip → 移除；不存在於 core 的 skip_id → WARN ignore
     - 議題順序：先 core 依 id 升序（id 1-99）→ 再 user_extensions 依 id 升序（id ≥ 100）
     - 對每議題依 `required_level` 決定行為（REQUIRED → 缺漏拒進階段 4；STRONGLY_PREFERRED → 跳過時 phase_log 紀錄 + 對應分拆檔標 TODO；OPTIONAL → 允許跳）
     - 完整提問腳本以 `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.1.2 對應段為**權威來源**（不擅自重寫 / 不擅自濃縮）；本檔 00_e §10 為 speed reference
     - 拆分規則（§10.11）**不**對 user 提問，屬階段 4 mechanic
   - **階段 3 收斂**：agent 把累積答案整合成「世界觀收斂預告稿」（依 00_e §5；含拆分計畫 + 00_b §1/§2 覆寫預覽 + TODO/INFERENCE/CONFLICT 清單 + 即將新建實體 + 不處理清單）
   - **階段 4 執行（依 00_e §10.11 拆分規則）：**
     - 把答案依 §10.11 拆分計畫表寫到對應檔：
       - 10.1 世界類型 → `01_world/01_a_世界觀總覽.md §1 世界類型` 覆寫
       - 10.2 世界規則 → `01_a §2` 覆寫
       - 10.3 科技水平 → `01_a §3` 覆寫 + 衍生詞 → `02_c §現代違和詞` append
       - 10.4 人民生活 → `01_a §4` 覆寫
       - 10.5 價值觀 → `01_a §5` 覆寫 + 禁忌話題 → `01_a §5 §禁忌話題彙整` append
       - 10.6 宗教 → `01_a §6` 覆寫 + 宗教用語 → `02_b §宗教衍生詞` append
       - 10.7 語言層級 → `01_world/01_b_世界語言規格.md §1-3` 覆寫 + 衍生詞 → `02_c §語言層級詞` append
       - 10.8 陣營階級語 → `01_world/01_c_陣營與階級語言.md §1-2` 覆寫 + 陣營禁忌詞 → `02_c §陣營詞` append
       - 10.9 類型語氣 → `00_protocol/00_b_反ai味檢查表.md §1 §2` 覆寫 + `01_a §7` 覆寫
       - 10.10 越界禁區（無寫檔；agent 收斂預告稿提醒）
     - 寫檔順序：`01_a` → `01_b` → `01_c` → `02_a` / `02_b` / `02_c` → `00_b` §1 / §2
     - frontmatter 規範（依 00_e §10.12）：`01_a` entities=[W-rules]、`01_b/c` entities=[W-language] + depends_on=[W-rules]、`02_*` entities=[V] + depends_on=[W-rules, W-language]
     - phase_log entry append：
       ```yaml
       - phase: create-world
         date: <ISO date>
         skill: /create-world
         status: completed
         created_entities: [W-rules, W-language, V]
         issue_completions: {<議題 id>: <答完/跳過>, ...}
       ```
   - **階段 5 驗證**：依 00_e §7 — 自動呼叫 `/status` skill 顯示 W-rules / W-language / V 完成度 + 建議下一步 `/create-character`
4. **D-047 對齊（必含段）：**
   - skill 啟動時必須讀 `<instance_root>/issue_type_registry.yaml`
   - 異常 fallback：registry 不存在 → Template fallback + WARN；schema 異常 → 拒絕進階段 2
   - registry hot-reload：本 skill 啟動讀一次；不支持 mid-session reload（user 改 registry 需 restart skill）
5. **禁止事項：**
   - 不得擅自跳階段（5 階段順序鎖死）
   - 不得擅自補完 user 未提供的設定（標 TODO 或 INFERENCE）
   - 不得擅自更動 issue_type_registry.yaml（user 修改責任）
   - 不得擅自覆寫 LOCKED 檔（檢查 header.狀態）
   - 不得在本協議建角色 / 主線 / 場景 / 關係 / 台詞（屬其他 /create-* / /scene-task）
   - 不擅自呼叫其他 /create-* skill（即使階段 5 建議了下一步）

### 中文 wrapper（`.claude/skills/建立世界觀/SKILL.md`）

採極簡 wrapper：
- frontmatter：name: 建立世界觀 / description: /create-world 中文別名
- 主體：引用英文版 SKILL.md 為權威

### 文字長度建議

英文 skill ~200-300 行；中文 wrapper ~20-30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（§A.6 line 705-725）
2. `00_protocol/00_e_世界觀創建協議.md`（完整 §1-§10 + §10.11 拆分規則 + §10.12 frontmatter 規範 + §4.0 D-047 機制段）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.1（11 議題完整提問腳本權威來源；line 341-690）
4. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D（D.1 schema / D.2 Phase B 行為 / D.3 衝突處理）

B. D-047 對齊核心
5. `_design/registries/issue_type_registry.template.yaml` v0.1（00_e_world 區段 line 50-119）
6. `_design/DECISIONS_LOG.md` v1.1 §6.9.2（D-047 拍板紀錄）

C. 對齊參考
7. `_design/ARCHITECTURE.md` v1.3 §3.3（skill 內容規範）
8. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log + status enum）
9. `_design/SPEC.md` v1.2 §17（00_b 7 anchor）

D. 已 LOCKED 不可動文件
10. 所有 `_design/*.md`
11. `_design/registries/*.template.yaml`
12. `scripts/*.py`
13. 既有 27 模板
14. `00_protocol/00_e_世界觀創建協議.md`（A.3 master patched）
15. `00_protocol/00_i_專案初始化協議.md`（A.2 master patched）
16. `00_protocol/00_b_反ai味檢查表.md`（A.1 done）
17. `_tools/frontend/*`

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/create-world/SKILL.md`
2. `.claude/skills/建立世界觀/SKILL.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name / description）+ markdown 主體
- 中文 wrapper 引用英文版

B. 內容
- 5 階段流程完整對齊 00_e protocol
- 階段 2 完整 D-047 機制段（讀 registry / core + user_extensions − core_overrides / locked 規則 / required_level 行為 / UD 為權威）
- 階段 4 拆分規則完整對齊 00_e §10.11
- 階段 4 frontmatter 規範對齊 00_e §10.12
- phase_log entry 含 status=completed + created_entities=[W-rules, W-language, V]
- 階段 5 自動呼叫 /status
- 禁止事項明示（不擅自跳階段 / 不擅自補完 / 不擅自覆寫 LOCKED / 不擅自呼叫其他 skill）
- 整檔無作品 / 角色名

C. 不破壞既有
- 沒動既有 27 模板 / _design / scripts / 00_protocol / _tools/frontend
- `git diff --check` 通過

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.6 完成 → user commit/push → 回 master → 推 Wave 4 或 master Milestone 1 整合驗收。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.6 task 啟動包；完成後 archive
