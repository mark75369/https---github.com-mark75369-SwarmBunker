狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A.0F alpha A.0F.2 task 啟動包 — F1 Project Dashboard 全局看板  
優先級：高

# CODEX_A0F2_STARTER — Phase A.0F alpha A.0F.2：F1 Project Dashboard

# 0. 本檔用途

Wave 3 第三條 task — 實作 F1 Project Dashboard 全局看板（第一個視覺 UI，依 UX §11.1 規範）。

**前置條件：** A.0F.1 ✓（8 endpoint adapter + LOCKED guard + DRAFT proposal contract）。

**與 A.5 / A.6 平行性：** A.5 / A.6 動 `.claude/skills/`；A.0F.2 動 `_tools/frontend/static/`。完全不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A.0F alpha A.0F.2 task」— F1 Project Dashboard 全局看板實作（第一個視覺 UI）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪改 `_tools/frontend/static/` 內既有 index.html + css + js
- 對應傳統：Wave 3 第三條 task（與 A.5 / A.6 平行可跑）
- frontend UI 工作 — 跟 A.5/A.6 documentation skill 不同類

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code / 27 模板 / 00_protocol
- ✗ **不**改 `_tools/frontend/server.py`（A.0F.1 done；A.0F.2 只動 frontend static）
- ✗ **不**改 `_tools/frontend/requirements.txt` / `README.md`
- ✗ **不**動 `.claude/skills/`（屬 A.5 / A.6 範圍）
- ✗ **不**寫 F2 Scene Queue（屬 A.0F.3）/ F3 Editor（屬 A.0F.4）/ F6 Search facet（屬 A.0F.5）/ F7 直接編輯（屬 A.0F.6）/ Asset Panel 完整（屬 A.0F.7）/ Export panel（屬 A.0F.8）等其他 UI
- ✗ **不**啟用任何 export / skill / qa subprocess 觸發（D-029 α）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.0F.2（line 891-895）+ UX_SPEC v0.4 §11.1 全段（從 line 2354 開始）。

### 任務目標

擴 `_tools/frontend/static/index.html` 從 A.0F.0 placeholder 雛形改為 F1 Project Dashboard（依 UX §11.1）— 含以下七段（UX §11.1 順序）：

1. **身份頭（Project Identity Header）** — 顯示 project_name + 最後更新時間
2. **HERO 下一步 / Next Actions** — 顯示「目前該跑什麼 skill」（從 phase_log 推導）
3. **HERO 卡點 / Blockers** — 顯示卡住的議題（缺漏 entity / dependency 等）
4. **場景就緒度 / Scene Readiness Overview** — 進度條 + 計數
5. **模組狀態 / Module Status** — entity type 完成度（W / V / C / R / P / CH / S / A）
6. **三欄區** — 內容依 UX §11.1 細節
7. **Asset Panel** — A-* 7 subtype 簡要顯示（不是 A.0F.7 完整版；本輪 minimum viable）

對應 A.0F.1 8 endpoint 的 API 整合：
- `GET /api/scope-counts?scope=full` — 取整體 counts
- `GET /api/assets?scope=all` — 取 asset manifest

### 具體做法

1. **讀 UX §11.1 整段** — `_design/UX_SPEC.md` line 2354 開始（讀完整子節 §11.1.1 ~ §11.1.6a）
2. **保留 A.0F.0 scaffold 結構** — index.html / css/ / js/ 既有檔位置不動，內容擴
3. **修改檔案：**
   - `_tools/frontend/static/index.html` — 把 placeholder body 改為 Dashboard layout（7 段）
   - `_tools/frontend/static/css/layout.css` — Dashboard layout + responsive grid（RWD per UX）
   - `_tools/frontend/static/css/components.css` — 進度條 / 卡片 / chip 等 component 樣式
   - `_tools/frontend/static/js/components/ProjectDashboard.js`（新建）— Dashboard 主元件
   - `_tools/frontend/static/js/pages/WorkspaceHome.js`（新建）— 對應 §11.9.1 Workspace Home 入口
   - `_tools/frontend/static/js/api.js` — 補 fetch helper（如 `fetchScopeCounts()` / `fetchAssets()`）
   - `_tools/frontend/static/js/main.js` — 入口擴：DOMContentLoaded 後 mount ProjectDashboard
   - `_tools/frontend/static/js/state.js` — 補 dashboard 用 signal（如 `dashboardData$`）
   - `_tools/frontend/static/js/router.js` — 加 `/` route mount Dashboard（其他 route 留 A.0F.3+）
4. **保持技術風格：**
   - vanilla JS（無 framework）
   - JSDoc 型別註解
   - signal/observable pattern（A.0F.0 既有 state.js 風格）
   - CSS variables + dark mode token（A.0F.0 既有 tokens.css）
5. **API 整合：**
   - DOMContentLoaded 後 fetch `/api/scope-counts?scope=full` + `/api/assets?scope=all`
   - 把結果 store 到 state.js signal
   - ProjectDashboard component 讀 signal 渲染
6. **錯誤處理：**
   - fetch fail → 顯示 fallback message「無法連到 server，請確認 server 已啟動」
   - 不要 crash whole page

### 七段內容細節（依 UX §11.1）

對每段，CODEX 從 UX §11.1 對應子節讀規範。本 starter 不重複寫細節（避免跟 spec drift）— CODEX 直接讀 UX §11.1.1 ~ §11.1.6a。

### 七段最小可運作版本

本輪是 alpha scaffold，**真實資料 + 完整 UI 留 real-data acceptance phase**（B.9 後）：

- 身份頭：可從 `/api/scope-counts` 取 instance_id 或顯示「Local Workspace」
- HERO 下一步：靜態 placeholder（如「先跑 /init-project」或「Wave 3 done → 試試 /create-world」）；真實「依 phase_log 推導」邏輯留 real-data acceptance
- HERO 卡點：靜態 placeholder 或從 scope-counts 簡單 derive（如 entities 為 0 顯示「請開始建專案」）
- 場景就緒度：dialogue_lines / total counts 進度條（直接從 scope-counts 取）
- 模組狀態：8 entity type 計數 bar（依 scope-counts.entities）
- 三欄區：placeholder「Phase A 後段任務」、「Phase A.0F UI 進度」、「Wave 3 狀態」（簡述）
- Asset Panel：A-* 7 subtype 計數（依 scope-counts.art_assets）

### 不在本輪 scope

- 完整「依 phase_log 推導下一步」邏輯（留 A.0F real-data acceptance）
- A-* Asset Panel 7 subtype 完整顯示（屬 A.0F.7）
- Conflict modal / Save guard / Editor 等（屬 A.0F.6 / A.0F.9）
- Glossary tooltip（屬 §11.9.3）

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（§A.0F.2 line 891-895）
2. `_design/UX_SPEC.md` v0.4 §11.1 全段（從 line 2354 開始；含 §11.1.1 ~ §11.1.6a）
3. `_design/UX_SPEC.md` v0.4 §11.8 整段（A.0F.0 scaffold 規範；確認既有檔結構不動）

B. API 對接
4. `_tools/frontend/server.py`（A.0F.1 done 567 行 + LOCKED guard patches；read-only — 看 8 endpoint 規格）
5. `_design/ARCHITECTURE.md` v1.3 §13.2 / §13.3（8 endpoint 對照 + 禁用）
6. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4.3 Contract C.3（前端 derive view）

C. 既有實作 baseline
7. `_tools/frontend/static/index.html`（A.0F.0 placeholder — 你要擴的檔）
8. `_tools/frontend/static/css/tokens.css`（A.0F.0 既有 design tokens；read-only）
9. `_tools/frontend/static/css/layout.css`（A.0F.0 placeholder；你要擴的檔）
10. `_tools/frontend/static/css/components.css`（A.0F.0 placeholder；你要擴的檔）
11. `_tools/frontend/static/js/{state,api,router,main}.js`（A.0F.0 skeleton；你要擴的檔）

D. 已 LOCKED 不可動
12. 所有 `_design/*.md`（除前述引用段）
13. `scripts/*.py`
14. 既有 27 模板
15. `00_protocol/*`
16. `_tools/frontend/server.py`（A.0F.1 done；本輪不動）
17. `_tools/frontend/requirements.txt` / `README.md`

---

**你要交付的產物：**

修改：
- `_tools/frontend/static/index.html`
- `_tools/frontend/static/css/layout.css`
- `_tools/frontend/static/css/components.css`
- `_tools/frontend/static/js/state.js`
- `_tools/frontend/static/js/api.js`
- `_tools/frontend/static/js/router.js`
- `_tools/frontend/static/js/main.js`

新建：
- `_tools/frontend/static/js/components/ProjectDashboard.js`
- `_tools/frontend/static/js/pages/WorkspaceHome.js`

**驗收條件（CODEX 自我驗證）：**

A. 結構驗證
- 9 個檔（7 改 + 2 新）全寫好
- 既有 A.0F.0 scaffold 樹狀結構不動（沒新增 / 刪除 top-level 目錄）
- server.py 不動（grep diff = 0）

B. UI 完整性
- 7 段 Dashboard layout 對齊 UX §11.1.1 ~ §11.1.6a
- API 整合：fetch /api/scope-counts + /api/assets 並渲染
- fetch fail 不 crash + 顯示 fallback

C. 啟動驗證（CODEX 自跑）
- `python _tools/frontend/server.py --port 8765` 啟動
- 瀏覽器（或 curl `http://localhost:8765/`）開到 Dashboard 而非 A.0F.0 placeholder
- 至少 1 個段顯示真實 API 資料（如 entities count）
- 至少 1 個段顯示 placeholder（HERO 下一步 etc）

D. 不破壞既有
- `git diff --check` 通過
- 不動 _design / scripts / 27 模板 / 00_protocol / server.py / requirements.txt / README.md
- 8 endpoint 仍 work（A.0F.1 baseline 不被破壞）

E. D-029 α 維持
- index.html / js 不含 `/api/export/run` / `/api/skill/run` / `/api/qa/run` 呼叫
- 不寫 subprocess / shell command

---

**Go / Done 判定指引：**

- **DONE：** A-E 5 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.0F.2 完成 → user commit/push → 你開瀏覽器看 Dashboard 雛形 → 回 master → 推 Milestone 1 整合驗收（A.0F.2 + A.5 + A.6 整合）。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.0F.2 task 啟動包；完成後 archive
