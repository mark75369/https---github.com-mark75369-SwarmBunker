狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A.0F alpha A.0F.1 task 啟動包 — 8 endpoint adapter 實作  
優先級：高

# CODEX_A0F1_STARTER — Phase A.0F alpha A.0F.1：frontend adapter 8 endpoint 實作

# 0. 本檔用途

A.0F.0 已建好 server.py + 8 個 endpoint scaffold（回 placeholder JSON）。A.0F.1 把 scaffold 換成真實 adapter — 8 endpoint 各自從 markdown source 讀取，回傳 Contract C 規範的 JSON shape。

**前置條件：** A.0F.0 已 DONE + push（server.py + static/ 目錄 + 8 scaffold endpoint）。

**與 A.2 / A.3 平行性：** A.0F.1 動 `_tools/frontend/server.py`；A.2 / A.3 動 `00_protocol/00_i` / `00_protocol/00_e` — 完全不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A.0F alpha A.0F.1 task」— 8 個 frontend adapter API endpoint 實作（取代 A.0F.0 scaffold placeholder）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪修改既有 `_tools/frontend/server.py`（把 8 scaffold endpoint 換成真實邏輯）
- 對應傳統：Wave 2 第三條 task（與 A.2 / A.3 平行可跑）
- code 工作 — 跟 A.2 / A.3 documentation 工作不同類；CODEX 對話切換時要切換思路

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry template / parser code（`scripts/parse_frontmatter.py` 是 read-only dep）
- ✗ **不**動既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/static/`（屬 A.0F.2+ UI 任務）
- ✗ **不**啟用 export / skill subprocess endpoint（永遠禁止，違反 D-029 α）
- ✗ **不**寫 Save race guard 完整邏輯（屬 A.0F.6；本輪 POST /save 接 mtime check + 純 write，race modal 觸發 / Save guard 流程留 A.0F.6）
- ✗ **不**寫 Conflict modal 邏輯（屬 A.0F.9）
- ✗ **不**改 server.py 啟動骨架 / index.html / static/* （只動 8 endpoint 內部邏輯）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.0F.1（line 874-889）+ ARCH v1.3 §13.2（8 endpoint 規格清單）+ Contract C.3 + Contract B.2 / B.4 + UX v0.4 §11.5.8（Save flow）+ §11.1.6a（Asset Panel） + §11.3.3（多版本）+ §11.3.5（行查 details pane） + §11.6.11（Export Prompt）。

### 任務目標

替換 `_tools/frontend/server.py` 內 8 個 scaffold endpoint 實作（A.0F.0 placeholder `{"status":"scaffold", "endpoint":..., "todo":"A.0F.1"}` → 真實邏輯）。

### 8 個 endpoint 各自規範

依 ARCH §13.2 + Contract C：

#### 1. `GET /api/scene/{scene_id}/header` → B.2 Save guard pre-flight

- 用途：Save guard pre-flight — 讀 scene 對應 markdown 的 frontmatter `狀態` + mtime checksum
- 邏輯：
  1. 從 scene_id resolve 到對應 markdown 路徑（如 `S-01-03` → 08_dialogue_outputs/<path>/CH01_S03_*.md；本輪實作可用 glob + parse 首行 header 比對）
  2. 跑 `parse_frontmatter.parse_file(path)` → 取 header 5 欄 + frontmatter yaml_data
  3. 算 mtime checksum（`os.stat(path).st_mtime`）
  4. 回 JSON：
     ```json
     {
       "scene_id": "<id>",
       "path": "<rel path>",
       "header": {"狀態": "...", "版本": "...", "最後更新": "...", "適用範圍": "...", "優先級": "..."},
       "mtime": <float epoch>,
       "issues": [<parser issue list>]
     }
     ```
  5. 找不到 → 404
- 對應 Contract B.2 / UX §11.5.8

#### 2. `POST /api/scene/{scene_id}/save` → B.2 Save flow Step 5

- 用途：Save flow — 接 client body (markdown content + client-side mtime checksum) → 寫回
- 邏輯：
  1. 接 request body：`{"content": "<full markdown>", "mtime_baseline": <float>}`
  2. resolve 對應 markdown 路徑
  3. **本輪簡化**：純寫 `Path(path).write_text(body.content, encoding="utf-8")` + 更新 mtime
  4. **不**做 race guard ERROR / modal trigger（屬 A.0F.6）— 但要回 mtime baseline 給 client，並若 server-side 當前 mtime ≠ baseline 回 409 conflict（純偵測，不彈 modal）
  5. 回 JSON：
     ```json
     {
       "scene_id": "<id>",
       "saved": true,
       "new_mtime": <float>,
       "mtime_drift": false
     }
     ```
- 對應 Contract B.2 / UX §11.5.8

#### 3. `POST /api/scene/{scene_id}/save-as` → B.2 LOCKED race modal B 選項

- 用途：「另存為 DRAFT proposal」— 將 content 寫到新檔（檔名加 `_proposal_<timestamp>` 後綴）
- 邏輯：
  1. 接 body：`{"content": "<full markdown>", "proposal_suffix": "<optional name>"}`
  2. resolve 原 scene_id 路徑 → 算新檔名（如 `S-01-03_proposal_2026-05-19.md`）
  3. 寫新檔（不覆蓋原檔）
  4. 回 JSON：
     ```json
     {
       "original_scene_id": "<id>",
       "saved_as_path": "<rel path of new file>",
       "saved": true
     }
     ```
- 對應 Contract B.2 / UX §11.5.8.2

#### 4. `GET /api/scenes/{scene_id}/versions` → 多版本 manifest

- 用途：依 scene_id 列出所有版本檔（v01A / v01B / v01C / v02 等）
- 邏輯：
  1. resolve scene_id → 找到 `08_dialogue_outputs/` 下對應 CH/S 目錄
  2. glob 對應 scene 的所有 `*_dialogue_v*.md` 檔
  3. 回 JSON：
     ```json
     {
       "scene_id": "<id>",
       "versions": [
         {"version": "v01A", "path": "...", "mtime": <float>, "header": {...}},
         ...
       ]
     }
     ```
- 對應 NS-15 / UX §11.3.3

#### 5. `GET /api/scenes/{scene_id}/keys/{key}/lines` → 場景行查 details pane

- 用途：依 scene_id + KEY 找跨版本 line content
- 邏輯：
  1. resolve scene_id → 找版本檔
  2. 對每版本檔跑 `parse_frontmatter.parse_file` → 從 `dialogue_keys` map 找 `key` entry → 從 body 抓對應 line
  3. 回 JSON：
     ```json
     {
       "scene_id": "<id>",
       "key": "<key>",
       "lines": [
         {"version": "v01A", "line_index": 3, "content": "<line text>", "speaker": "<name>", "status": "active"},
         ...
       ]
     }
     ```
- 對應 NS-30 / UX §11.3.5

#### 6. `GET /api/assets?scope=...` → Asset Panel manifest

- 用途：依 scope 列 A-* asset manifest
- 邏輯：
  1. 接 query：`scope=all` / `scope=scene/<id>` / `scope=subtype/<name>`
  2. 跑 `build_repo_index('.')` → 取 `art_metadata_index`
  3. 依 scope filter
  4. 回 JSON：
     ```json
     {
       "scope": "<query>",
       "assets": [
         {"asset_id": "A-portrait-...", "subtype": "portrait", "display_name": "...", "owner": "...", "state_tags": [...], "aliases": [...]},
         ...
       ],
       "total": <int>
     }
     ```
- 對應 Contract B.4 / NS-2 / UX §11.1.6a

#### 7. `GET /api/assets/{asset_id}/usage` → asset 反查場景引用

- 用途：依 asset_id 反查「該 KEY 被多少場景引用」
- 邏輯：
  1. resolve asset_id → 從 `art_metadata_index` 找對應 entry
  2. 反查 `dialogue_keys.<KEY>.portrait/bgm/sfx` 引用該 asset_id 的所有 KEY
  3. 回 JSON：
     ```json
     {
       "asset_id": "<id>",
       "usage": [
         {"scene_id": "S-01-03", "key": "narrator_001", "field": "portrait", "version": "v01A"},
         ...
       ],
       "total": <int>
     }
     ```
- 對應 Contract B.4 / UPS-UX-80

#### 8. `GET /api/scope-counts?scope=...` → Export prompt 元資料

- 用途：Export prompt 用「組 prompt 所需的元資料」
- 邏輯：
  1. 接 query：`scope=full` / `scope=scene/<id>` / `scope=chapter/<ch>`
  2. 跑 `build_repo_index('.')` → 算 counts
  3. 回 JSON：
     ```json
     {
       "scope": "<query>",
       "counts": {
         "entities": {"C": 8, "R": 6, "S": 15, "CH": 12, "A": 23},
         "dialogue_lines": 1532,
         "art_assets": 23,
         "qa_reports": 0
       }
     }
     ```
- 對應 §C.5a / ARCH §4.2a

### 通用實作策略

1. **import parser API**：
   ```python
   import sys
   sys.path.insert(0, str(PROJECT_ROOT))
   from scripts.parse_frontmatter import parse_file, build_repo_index
   ```
2. **cache**：build_repo_index 結果可 cache 在 process memory（簡單 dict cache）+ mtime invalidation；本輪實作可不 cache（每次 endpoint 呼叫重新 build），效能優化留 A.0F.x
3. **錯誤處理**：endpoint 內部例外 → return 500 + JSON `{"error": "<msg>"}`；找不到資源 → 404
4. **CORS**：維持 A.0F.0 預設（同 origin only；本地 127.0.0.1 不對外）

### 自我驗證

CODEX 在交付前必須能跑：

```bash
cd D:/劇本開發工具/_tools/frontend
python server.py --port 8765
```

然後對每個 endpoint 至少跑 1 個 curl test（用既有 repo 內 data 或 mock）：

- `curl http://127.0.0.1:8765/api/scene/non_existent/header` → 404
- `curl http://127.0.0.1:8765/api/assets?scope=all` → 200 + valid JSON（即使 assets=[] 也算 OK）
- `curl http://127.0.0.1:8765/api/scope-counts?scope=full` → 200 + valid JSON

**注意 sandbox 環境：** 若無法跑 uvicorn 監聽，至少：
- import server 不報錯
- 8 endpoint route 全註冊（`app.routes` count = 8 + StaticFiles mount）
- 禁用 endpoint 不在 routes（grep `app.routes` 沒有 `/api/export/run` / `/api/skill/run` / `/api/qa/run`）

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（A.0F.1 任務 line 874-889）
2. `_design/ARCHITECTURE.md` v1.3 §13.2（8 endpoint 完整規格 line 1352-1364）+ §13.3（禁用 endpoint）
3. `_design/INTEGRATION_CONTRACTS.md` v2.1 §3.2（Contract B.2 / Save race guard）+ §3.4（Contract B.4 / Asset Panel）+ §4.3（Contract C.3 / 前端 derive view）

B. UX 細節
4. `_design/UX_SPEC.md` v0.4 §11.5.8（Save flow 5 步）+ §11.1.6a（Asset Panel）+ §11.3.3（多版本）+ §11.3.5（行查 details pane）+ §11.6.11（Export Prompt panel）

C. Parser API
5. `scripts/parse_frontmatter.py`（read-only — 用 parse_file / build_repo_index API）
6. `_design/DATA_FORMAT_SPEC.md` v0.4 §3 / §4 / §5（dialogue_keys map shape / art_metadata structure）

D. 既有實作基礎
7. `_tools/frontend/server.py`（A.0F.0 scaffold — 你要改的檔；保留 8 endpoint route 路徑與 method，只換內部邏輯）
8. `_tools/frontend/requirements.txt`（依賴清單 — 不動或補必要新依賴）

E. 已 LOCKED 不可動文件
9. 所有 `_design/*.md`
10. `_design/registries/*.template.yaml`
11. `scripts/*.py`
12. 既有 27 模板
13. `00_protocol/*`
14. `_tools/frontend/static/*`（A.0F.2+ 動）
15. `_tools/frontend/README.md` / `requirements.txt`（可補新 dep 但建議不動；若補要在報告說明）

---

**你要交付的產物：**

修改：`_tools/frontend/server.py`（8 endpoint 真實邏輯）

可能修改（若需要新依賴）：`_tools/frontend/requirements.txt`（補 dependency，如 `aiofiles` for async write 等；建議**先不要**新增 dep，FastAPI + uvicorn[standard] 足夠）

**驗收條件（CODEX 自我驗證）：**

A. Route 結構驗證
- server.py 8 endpoint 全在（GET /api/scene/<id>/header / POST /api/scene/<id>/save / POST /api/scene/<id>/save-as / GET /api/scenes/<id>/versions / GET /api/scenes/<id>/keys/<key>/lines / GET /api/assets / GET /api/assets/<id>/usage / GET /api/scope-counts）
- 禁用 endpoint 不存在（grep `app.routes` 確認）
- import server 不報錯

B. 邏輯驗證
- 每 endpoint 回 JSON shape 對齊本檔規範
- 至少 5 個 endpoint 跑 curl 測試 PASS（含 200 / 404 各一）
- parser import 成功（`from scripts.parse_frontmatter import build_repo_index, parse_file`）
- build_repo_index('.') 在 endpoint 內可呼叫且不報錯

C. 不破壞既有
- `git diff --check` 通過
- 沒動既有 27 模板 / _design / scripts / 00_protocol / _tools/frontend/static / index.html / README.md
- 不動 server.py 啟動骨架（uvicorn.run / argparse / StaticFiles mount）
- `python server.py --help` 仍 work
- Forbidden endpoint check 維持（不存在）

D. 對齊 D-029 α
- **不**啟用任何 subprocess 呼叫
- **不**有任何 endpoint 觸發 export / skill / qa command line tool
- 純 read markdown / write markdown / parser API call

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A0F1_REPORT.md`（可選 — 因禁區明示不改 `_design/*.md`，可不交報告，inline 回 master 即可）

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件全 ✓
- **BLOCKED：** 任一驗收 ✗，回 master

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.0F.1 完成 → user commit/push → 回 master → 我推 A.0F.2（F1 Project Dashboard）或繼續 Phase A 後段（A.5 等）。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.0F.1 task 啟動包；完成後 archive
