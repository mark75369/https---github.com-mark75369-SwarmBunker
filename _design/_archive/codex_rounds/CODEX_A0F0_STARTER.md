狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A.0F alpha 第一個 task — A.0F.0 前端 build / package / 啟動規格  
優先級：高

# CODEX_A0F0_STARTER — Phase A.0F alpha A.0F.0：前端 build / package / 啟動規格

# 0. 本檔用途

Master 第五輪整合完成 + Milestone 1 啟動條件達成。Phase A.0F alpha 跟 Phase A 後段**可平行**。

本檔給「**Phase A.0F.0 task**」對話啟動時用。把 §1 完整 prompt 複製貼到新 CODEX 對話。

**本 task 在路線圖位置：**
- Phase A.0F alpha 第一個 task — 建前端 scaffold + Python FastAPI server skeleton + 靜態目錄結構
- 跟 A.1（00_b 通用骨架）+ A.4（27 模板 frontmatter）平行可跑
- 完成後是 A.0F.1（8 endpoint adapter）等後續前端任務的基底

**前置條件：**

- ✓ 設計層 10 spec LOCKED（含 UX v0.4 §11.8 / ARCH v1.3 §13）
- ✓ Phase A.0 parser baseline + A.0.10 patch（A.0F.1 之後會 import parser API；本 task 暫不依賴）
- ✓ master 第五輪整合對話 push 完成

**與 A.1 / A.4 平行性：**

| Task | 動到的檔 | 跟 A.0F.0 衝突？ |
|---|---|---|
| A.1 | **新建** `00_protocol/00_b_反ai味檢查表.md` | ✗ 完全不重疊 |
| A.4 | **修改** 既有 27 模板 frontmatter | ✗ 完全不重疊 |
| A.0F.0（本） | **新建** `_tools/frontend/` 目錄結構 | — |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A.0F alpha A.0F.0 task」— 建前端 build / package / 啟動規格（FastAPI server + 靜態目錄結構）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建新前端目錄 + Python FastAPI server skeleton + 啟動指令
- 你不是 reviewer — 本輪不審 LOCKED spec
- 你是 scaffold 工作者 — 任務是建「能跑得起來的最小骨架」，不是完整實作 UI
- 對應傳統：本輪是 Phase A.0F alpha 第一個 task；只建啟動基底，後續 A.0F.1 ~ A.0F.5 才補 endpoint / UI

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec（10 份設計檔 + 3 份 registry + parser code）
- ✗ **不**動既有 27 模板（屬 A.4 task）
- ✗ **不**動 `00_protocol/` 任何檔（屬 A.1 / A.2 / A.3 task）
- ✗ **不**寫 8 個 API endpoint 實際內容（屬 A.0F.1）
- ✗ **不**寫 UI 元件實際內容（屬 A.0F.2 ~ A.0F.5）
- ✗ **不**寫 Save guard 邏輯（屬 A.0F.6）
- ✗ **不**啟用 export / skill subprocess（永遠禁止，違反 D-029 α）

**本 task scope（嚴格限定 — 只建 scaffold）：**

依 TASKS v1.4 §A.0F.0（line 865-872）+ UX v0.4 §11.8（line 4472-4790）+ ARCH v1.3 §13.1（FastAPI server 啟動段）。

### 任務目標

建 `_tools/frontend/` 目錄結構 + Python FastAPI server skeleton + 靜態目錄 + requirements.txt + 啟動 README。確保「`python _tools/frontend/server.py` 能啟動，瀏覽器 `http://localhost:8765` 開到 Workspace Home 雛形」。

**注意命名一致性：** TASKS A.0F.0 line 868 寫 `serve.py`；UX §11.8.4 line 4586 寫 `server.py`（含 `if __name__ == "__main__"` skeleton 範例 line 4629 也用 `server.py`）。**採 UX §11.8 權威用 `server.py`**（TASKS 為 typo，本輪不修 TASKS 但 CODEX 用 server.py）。

### 具體做法

1. **讀 UX §11.8** — `_design/UX_SPEC.md` 整段 line 4472-4790
   - §11.8.1 技術選擇（FastAPI / vanilla JS / JSDoc / signal state / CSS variables）
   - §11.8.2 目錄結構（line 4490-4537 — 整段目錄樹照建）
   - §11.8.3 Server API 設計（line 4541-4576 — 8 endpoint 對照表；**A.0F.0 本輪只建 endpoint 路徑骨架，不寫實際邏輯**）
   - §11.8.4 啟動方式（line 4578-4638 — server.py 範本照抄）
   - §11.8.6 State 管理（signal/observable pattern；**本輪只建 `state.js` 骨架不寫實際 signal**）
   - §11.8.10 啟動文檔 README 內容
2. **讀 ARCH §13** — `_design/ARCHITECTURE.md` §13（含 §13.1 server 啟動段 + §13.2 8 endpoint 規格 ref）— 確認 endpoint URL pattern 對齊
3. **建目錄結構** — 依 UX §11.8.2 line 4490-4537 的樹狀圖完整建：
   ```
   _tools/frontend/
   ├── server.py                # FastAPI server 主檔（採 UX §11.8.4 line 4608-4638 範本）
   ├── requirements.txt         # python 依賴（fastapi/uvicorn/python-multipart/pyyaml/markdown）
   ├── README.md                # 啟動說明（依 UX §11.8.10）
   ├── static/
   │   ├── index.html           # 主 HTML — 含基本 HTML5 boilerplate + meta + hash routing 骨架（無實際 routing 邏輯）
   │   ├── css/
   │   │   ├── tokens.css       # 設計 token + dark mode（依 UX §11.8.7）
   │   │   ├── layout.css       # 空檔含 comment placeholder
   │   │   └── components.css   # 空檔含 comment placeholder
   │   ├── js/
   │   │   ├── state.js         # signal/observable 骨架（最小 implementation；A.0F.2+ 才補實際 signal）
   │   │   ├── api.js           # server API client 骨架（fetch wrapper；A.0F.1 才補 8 endpoint 實際呼叫）
   │   │   ├── router.js        # hash routing 骨架（最小 hashchange listener；A.0F.2+ 才補實際 route map）
   │   │   ├── main.js          # 入口；只 bind DOMContentLoaded + import 其他 module
   │   │   ├── components/      # 空目錄含 .gitkeep + README.md 列 A.0F.2+ 規劃元件
   │   │   └── pages/           # 空目錄含 .gitkeep + README.md
   │   └── assets/
   │       └── glossary.json    # 空 `{}` placeholder（A.0F.2+ 才補 13 術語）
   └── tests/                   # 可選；只建空目錄含 README.md（本輪不寫測試）
   ```
4. **server.py 骨架**：
   - 採 UX §11.8.4 line 4608-4638 範本（FastAPI + StaticFiles mount + uvicorn 啟動）
   - 8 endpoint 路徑**只建路由骨架**（每 endpoint 回 `{"status": "scaffold", "endpoint": "<name>", "todo": "A.0F.1"}`），**不寫實際邏輯**
   - 預設 bind `127.0.0.1`（不對外）
   - default port 8765
5. **requirements.txt**：fastapi / uvicorn[standard] / python-multipart / pyyaml / markdown（依 UX §11.8.4 line 4599-4606）
6. **README.md**（`_tools/frontend/README.md`）：
   - 啟動指令範例
   - 預期 output
   - 開瀏覽器位置
   - 結束方式
   - 對齊 UX §11.8.10
7. **index.html** Workspace Home 雛形：
   - 含 `<!DOCTYPE html>` / `<html lang="zh-Hant">` / `<head>` 含 meta charset UTF-8 / viewport / title「劇本開發工具」
   - `<body>` 含一個簡單 placeholder：「Phase A.0F alpha — A.0F.0 scaffold OK；A.0F.1+ pending」
   - link 到 css/tokens.css / css/layout.css / css/components.css
   - script 到 js/main.js（type="module" 或 plain；依 UX §11.8 建議）
8. **不啟用 export / skill subprocess endpoint**（依 ARCH §13.3 + D-029 α）：
   - **不**建 `POST /api/export/run`
   - **不**建 `POST /api/skill/run`
   - **不**建 `GET /api/qa/run`

### 自我驗證

CODEX 在交付前必須能跑成功：

```bash
cd D:/劇本開發工具/_tools/frontend
pip install -r requirements.txt    # 首次或在 CODEX sandbox 確認可安裝
python server.py --port 8765
# 預期 output:
# > Serving from D:/劇本開發工具
# > Open browser: http://127.0.0.1:8765
# > Press Ctrl-C to stop
```

然後 `curl http://127.0.0.1:8765/` → 回 index.html 內容（200 OK）。  
然後 `curl http://127.0.0.1:8765/api/scene/test/header` → 回 scaffold JSON（200 OK + `{"status":"scaffold","endpoint":"...","todo":"A.0F.1"}`）。

**注意 CODEX sandbox 環境：** 若 sandbox 不能跑 server 監聽，至少要：
- import 不報錯（`python -c "import server"` 在 _tools/frontend 目錄）
- 跑 `python server.py --help` 不報錯（argparse 應 work）
- 驗證 FastAPI app 可建（`from server import app`）

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（A.0F.0 任務 line 865-872 + A.0F.1 line 874-889 確認本輪不做）
2. `_design/UX_SPEC.md` v0.4 §11.8 整段（line 4472-4790；含 §11.8.1 ~ §11.8.12）
3. `_design/ARCHITECTURE.md` v1.3 §13（含 §13.1 server 啟動 + §13.2 endpoint 規格清單 + §13.3 不提供 endpoint）

B. 對齊參考
4. `_design/INTEGRATION_CONTRACTS.md` v2.1 Contract C.3（前端 adapter 從 markdown derive view）
5. `_design/DATA_FORMAT_SPEC.md` v0.4 §9（JSON 中介格式 — 知道前端不消費）

C. 已 LOCKED 不可動文件（明示禁區）
6. 所有 `_design/*.md`
7. `_design/registries/*.template.yaml`
8. `scripts/*.py`
9. 既有 27 模板（路徑見 ARCH §7.3 對照表）
10. `00_protocol/*` 任何檔

---

**你要交付的產物：**

新建檔案（全部位於 `_tools/frontend/` 下）：

```
_tools/frontend/
├── server.py
├── requirements.txt
├── README.md
└── static/
    ├── index.html
    ├── css/tokens.css
    ├── css/layout.css
    ├── css/components.css
    ├── js/state.js
    ├── js/api.js
    ├── js/router.js
    ├── js/main.js
    ├── js/components/.gitkeep
    ├── js/components/README.md
    ├── js/pages/.gitkeep
    ├── js/pages/README.md
    ├── assets/glossary.json
    └── tests/README.md
```

**驗收條件（CODEX 自我驗證）：**

A. 結構驗證
- `_tools/frontend/` 目錄 + 所有檔案存在
- 目錄結構對齊 UX §11.8.2 line 4490-4537

B. 啟動驗證
- `import server` 不報錯
- `from server import app` 可拿到 FastAPI instance
- `python server.py --help` 顯示 --port / --host 兩 arg
- （若 sandbox 允許）`python server.py --port 8765` 啟動成功，curl `/` 回 index.html

C. 內容驗證
- 8 endpoint 路由骨架全建（依 UX §11.8.3 line 4547-4556 對照表）
- 每 endpoint scaffold 回 JSON 含 `status`/`endpoint`/`todo` 三欄
- **不**建被禁的 3 endpoint（`/api/export/run` / `/api/skill/run` / `/api/qa/run`）
- index.html 含正確 meta + link + script
- README.md 含啟動指令

D. 不破壞既有
- `git diff --check` 通過
- 沒動既有 `_design/` / `scripts/` / 既有 27 模板 / `00_protocol/`
- `git status --short -uall` 預期：新檔在 `_tools/frontend/` 下 + （可選）報告

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A0F0_REPORT.md`（可選）

報告格式（如交付）：

```markdown
狀態：REVIEW
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：Phase A.0F alpha A.0F.0 task 完成報告
優先級：高

# CODEX_A0F0_REPORT — 前端 scaffold 完成

## 0. 摘要
**結論：[DONE / BLOCKED]**

## 1. 新建檔案清單
- `_tools/frontend/server.py`
- `_tools/frontend/requirements.txt`
- `_tools/frontend/README.md`
- `_tools/frontend/static/index.html`
- ...（逐檔列）

## 2. 啟動驗證結果
- import server: ✓/✗
- python server.py --help: ✓/✗
- 8 endpoint scaffold curl: ✓/✗ (列實際試的)
- 禁用 endpoint check: ✓ (確認不存在)

## 3. 驗收結果
- A 結構驗證 ✓/✗
- B 啟動驗證 ✓/✗
- C 內容驗證 ✓/✗
- D 不破壞既有 ✓/✗

## 4. 不在 scope 的觀察（如有）
- TASKS A.0F.0 `serve.py` vs UX §11.8 `server.py` 命名不一致（本輪採 server.py per UX 權威；TASKS 屬 typo，留 master 後續 patch round）
- 其他 spec 不一致發現

## 5. Source Limitations
```

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件全 ✓（A/B/C/D）
- **BLOCKED：** 任一驗收 ✗，回 master

請開始。
```

---

# 2. 平行跑時的合作紀律

若你（user）同時跑 A.1 + A.4 + A.0F.0 三個 CODEX 對話：

| 動作 | 影響 |
|---|---|
| A.1 新建 `00_protocol/00_b_反ai味檢查表.md` | 不影響 A.0F.0 frontend 目錄 |
| A.4 修改 27 模板 frontmatter | 不影響 A.0F.0 frontend 目錄 |
| A.0F.0 新建 `_tools/frontend/` | 不影響 A.1 protocol / A.4 既有模板 |

**commit 紀律：** 三個 task 完成後各自獨立 commit，**不要**混在同一 commit。

---

# 3. 完成條件 + 後續

CODEX A.0F.0 完成 = 4 驗收 ✓ + 報告（可選）+ 啟動測試通過。

CODEX 完成後：
- User 手動 commit + push（`git add _tools/frontend/` + 可選報告，commit + push）
- 你可以開 `http://localhost:8765` 看到雛形 placeholder 頁
- 回 master 對話告訴我結果 → 我會推薦 A.0F.1（8 endpoint adapter 實作）

---

# 4. 文件維護紀律

- 本檔是「**CODEX A.0F.0 task 啟動包**」；CODEX 完成後可 archive 進 `_design/archive/`
- 本檔產出後若需修補，改本檔 + 升 v0.2
