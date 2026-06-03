狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.5 task 啟動包 — /init-project skill 實作  
優先級：高

# CODEX_A5_STARTER — Phase A 後段 A.5：/init-project skill 實作

# 0. 本檔用途

Wave 2 GO 後 Wave 3 第一條 task — 實作 `/init-project` skill（含中文別名 `/初始化專案`），依 00_i Bootstrap protocol 跑 5 階段。

**前置條件：** Wave 1+2 全 DONE + push（含 A.2 ✓ 00_i / A.4 ✓ 27 模板 frontmatter / Wave 2 review GO）。

**與 A.6 / A.0F.2 平行性：** A.5 動 `.claude/skills/init-project/` + `.claude/skills/初始化專案/`；A.6 動 `.claude/skills/create-world/` + `.claude/skills/建立世界觀/`；A.0F.2 動 `_tools/frontend/static/`。完全不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.5 task」— 實作 `/init-project` skill（含中文 wrapper），對應 00_i Bootstrap protocol。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（英文 skill + 中文 wrapper）
- 對應傳統：Wave 3 第一條 task（與 A.6 / A.0F.2 平行可跑）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**寫 `/create-world` / `/status` / `/check-gaps` 等其他 skill（屬 A.6/A.7/A.8）
- ✗ **不**寫 `.protocol_version` 真實內容（屬 skill 跑時動作，不是 skill 本身的 SKILL.md 內容）
- ✗ **不**允許 Bootstrap 微調 00_a / 00_e ~ 00_l / 01-09 模板（嚴格鎖）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.5（line 633-704）+ 00_protocol/00_i 完整 5 階段流程 + ARCH §3.3 skill 內容規範 + SPEC §5.4 phase_log。

### 任務目標

新建 2 個 SKILL.md：
1. `.claude/skills/init-project/SKILL.md` — 英文 skill 主檔
2. `.claude/skills/初始化專案/SKILL.md` — 中文 wrapper（觸發語 `/初始化專案`）

### SKILL.md 內容規範（依 ARCH §3.3）

每個 SKILL.md 在頂部含：
- frontmatter 區（at minimum）:
  ```
  ---
  name: init-project
  description: 建立新 Instance repo 的 Bootstrap 流程。從 Template clone 後執行，引導使用者完成專案初始化、Template 微調（限 00_b/00_c/00_d）、三 registry 拷貝、10_art_assets/ 目錄結構、Instance root .gitignore 建立、`.protocol_version` 紀錄。對齊 00_protocol/00_i_專案初始化協議.md 全 5 階段流程。
  ---
  ```
- 主體 markdown 內容（描述 skill 行為 + 階段流程 + 規範指令）

### 英文 skill（`.claude/skills/init-project/SKILL.md`）內容結構

依 00_i protocol 5 階段流程，明示：

1. **觸發語：** `/init-project`（這個 skill 不直接接 user 參數，採對話式引導）
2. **依賴：** 00_protocol/00_i_專案初始化協議.md 全部 10 區段 + SPEC §8 + DECISIONS_LOG §6.9.2 (D-047)
3. **5 階段對應 00_i protocol：**
   - **階段 1 診斷**：依 00_i §3 行為，請 user 貼新專案基本資料（作品名/類型/長度/目標/語氣偏好/參考作品）
   - **階段 2 探索 / 微調候選**：依 00_i §4 行為，列限定 00_b/00_c/00_d 微調選項
   - **階段 3 收斂**：依 00_i §5 行為，user 拍板每個微調
   - **階段 4 執行（7 step 寫檔順序）：** 依 00_i §6 + §6.1 嚴格 6 步寫檔順序：
     1. 寫 `.protocol_version`（schema 依 §6.2 + §10.2）
     2. 從 Template `_design/registries/` 複製三 registry → Instance root（entity_type_registry / qa_type_registry / issue_type_registry）— 失敗 rollback `.protocol_version`
     3. 建 `10_art_assets/` 7 subtype 子目錄 + `index.md` stub
     4. 寫 Instance root `.gitignore`（至少含 `export/`）
     5. 套用 00_b / 00_c / 00_d 微調
     6. reread verify 全部寫檔成功 + header 未破壞
   - **階段 5 驗證**：依 00_i §7 列檢查項 + 建議下一步「/create-world」
4. **`.protocol_version` 寫入規範：**
   - schema 完整對齊 00_i §10.2 範本（含 bootstrapped_registries / bootstrapped_directories / bootstrapped_files / phase_log）
   - 第一筆 phase_log entry：
     ```yaml
     - phase: bootstrap
       date: <ISO date>
       skill: /init-project
       status: completed
       created_entities: []
       scene_ids: []
       customizations: [<已拍板項>]
     ```
   - `status` 欄為 D-042 已 formalize（不是暫定）
5. **禁止事項：**（明示 — agent 不可違反）
   - 不得允許 user 微調 00_a / 00_e ~ 00_l / 01-09 模板
   - 不得跳階段
   - 不得自動跑 `/create-world` 或其他下游 skill（即使階段 5 建議了）
   - 不得在已 bootstrap 的 Instance 上重跑（檢查 `.protocol_version.phase_log` 是否已含 bootstrap entry with completed）
6. **錯誤處理 / rollback：**
   - 階段 4 任一 step 失敗 → rollback 已寫 step（清除 `.protocol_version` + 已 copy 的 registry 檔等）
   - `.protocol_version` 已存在 → 列出且詢問是否要 abort（不擅自覆寫）

### 中文 wrapper（`.claude/skills/初始化專案/SKILL.md`）內容

採極簡 wrapper 策略：
- frontmatter：
  ```
  ---
  name: 初始化專案
  description: /init-project 中文別名 — 觸發新專案初始化流程。實際邏輯參見 .claude/skills/init-project/SKILL.md。
  ---
  ```
- 主體：1-2 段說明「本 wrapper 觸發 /init-project skill 同樣流程；所有規範以英文版 SKILL.md 為權威」

### 5 階段流程文字長度建議

英文 skill 主檔 ~150-250 行 markdown（足以描述 5 階段細節 + 寫檔 schema + 錯誤處理 + 禁止事項）；中文 wrapper ~20-30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（§A.5 line 633-704）
2. `00_protocol/00_i_專案初始化協議.md`（完整 5 階段 + §10.2 .protocol_version 範本 + §10.5 三 registry copy + §10.6 10_art_assets + §10.7 .gitignore）
3. `_design/SPEC.md` v1.2 §5.4 / §5.4a（phase_log schema）+ §8（Bootstrap 流程）
4. `_design/ARCHITECTURE.md` v1.3 §3.3（skill 內容規範）

B. 對齊依據
5. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log 5 新欄位 + status enum + base_dialogue）
6. `_design/DECISIONS_LOG.md` v1.1 §6.9.2（D-047 三 registry copy）+ §6.7.x（D-042 phase_log status formalize）
7. `_design/registries/` 三 template yaml（copy 來源）

C. 已 LOCKED 不可動文件
8. 所有 `_design/*.md`
9. `scripts/*.py`
10. 既有 27 模板
11. `00_protocol/*` 全部
12. `_tools/frontend/*` 全部

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/init-project/SKILL.md`
2. `.claude/skills/初始化專案/SKILL.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name / description）+ markdown 主體
- 中文 wrapper 引用英文 skill 為權威

B. 內容
- 5 階段流程完整對齊 00_i protocol
- §4 階段 4 含 7 step 寫檔順序（registry copy / 10_art_assets / .gitignore 等）
- `.protocol_version` schema 對齊 00_i §10.2 範本
- 第一筆 phase_log entry 含 status=completed + D-042 formalize 註記
- 禁止事項明示 00_a / 00_e~00_l / 01-09 不可微調
- 錯誤處理 / rollback 規範完整

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

CODEX A.5 完成 → user commit/push → 回 master → 推 Wave 4 或 master Milestone 1 驗收。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.5 task 啟動包；完成後可 archive
