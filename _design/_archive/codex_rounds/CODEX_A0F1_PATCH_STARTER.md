狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX Wave 2 review NO-GO 後 A.0F.1 server.py patch round 啟動包  
優先級：高

# CODEX_A0F1_PATCH_STARTER — A.0F.1 server.py 3 finding patch round

# 0. 本檔用途

CODEX Wave 2 review 對 A.0F.1（`_tools/frontend/server.py`）判定 △ Partial，列 3 個 finding：

- **A0F1-01 Major**：`POST /api/scene/{id}/save` 缺 server-side LOCKED guard（只做 mtime 比對，未獨立擋 LOCKED overwrite）
- **A0F1-02 Major**：`POST /api/scene/{id}/save-as` 未保證 DRAFT proposal contract（不改 header status / 不補 base_dialogue / iteration_note）
- **A0F1-03 Minor**：409 conflict body 單檔簡化版，未達 UX §11.7.5 multi-version conflict modal shape

本檔給 focused CODEX patch round 用 — scope **嚴限** 3 finding 修補 + curl smoke test 驗證。

**前置條件：**
- ✓ Wave 2 review report 已產出（CODEX_WAVE2_REVIEW_REPORT.md）
- ✓ A.3 patches 已 master 直接補完
- ✓ `_tools/frontend/server.py` 維持 A.0F.1 567 行實作 baseline（不要 discard）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「A.0F.1 server.py 3 finding patch round」— Wave 2 review NO-GO 後的 targeted patch。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支或 working tree 上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + self-verifier — 本輪改 `_tools/frontend/server.py`（不重寫整檔，targeted patch 3 處）
- 你 NOT 是 reviewer — 不審 LOCKED spec / 不改其他檔
- 你是 patch-round only — 只修 3 finding；其他 Wave 2 finding（A.2 / A.3）已 master 補完
- 對應傳統：本輪是 A.0F.1 patch round（類比 Stage 0 A.0.10 patch round 模式）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry template / parser code
- ✗ **不**動 `_tools/frontend/static/` / `requirements.txt` / `README.md`
- ✗ **不**動 `00_protocol/*` / 既有 27 模板 / `_design/*`
- ✗ **不**改 server.py 啟動骨架（uvicorn / argparse / StaticFiles mount / FastAPI app 建立 / parser API import）
- ✗ **不**改其他 6 endpoint 邏輯（header / versions / keys-lines / assets / asset-usage / scope-counts 不在本輪 scope；只動 save / save-as + 加 helper）
- ✗ **不**啟用 subprocess / export / skill subprocess（永遠禁止）
- ✗ **不**寫 frontend UI 對接邏輯（A.0F.6 / A.0F.9 範圍）

**本 task scope（嚴格限定 — 3 finding）：**

### Patch-A0F1-01：`POST /api/scene/{scene_id}/save` 加 server-side LOCKED guard

**對齊基準：**
- INTEGRATION_CONTRACTS v2.1 §3.2 Contract B.2 line 1076-1104（Save race guard 5 步流程）
- UX_SPEC v0.4 §11.5.8 line 3689-3719（前端 Save flow Step 3 pre-flight）

**當前邏輯（A.0F.1 baseline）：** `server.py:387-418` — 只做 mtime 比對，通過後直接 `write_text`。前端 Step 3 pre-flight 漏掉時 server 不獨立擋 LOCKED。

**修補要求：**
1. 在 `write_text` 之前，**重新 parse 目標檔的 frontmatter header**（用 `parse_file(path)`）
2. 檢查 `header.狀態` — 若為 `LOCKED`：
   - 拒絕寫入
   - 回 **409 Conflict** + JSON：
     ```json
     {
       "error": "LOCKED_OVERWRITE_DENIED",
       "scene_id": "<id>",
       "current_status": "LOCKED",
       "current_mtime": <float>,
       "suggestion": "用 /api/scene/<id>/save-as 另存 DRAFT proposal"
     }
     ```
3. 若 `header.狀態 != LOCKED`：照原 mtime drift 邏輯繼續（mtime drift → 409 with current shape；mtime OK → 寫入 + 200）
4. 順序：先驗 LOCKED → 再驗 mtime drift → 再寫入（任一失敗 short-circuit return）

**驗證：**
- tempfile 建一個 `狀態：LOCKED` 的 scene 檔 → `POST /save` 應 409 + `error: LOCKED_OVERWRITE_DENIED`
- 同檔改成 `狀態：DRAFT` → `POST /save` 應 200 + 寫入成功

### Patch-A0F1-02：`POST /api/scene/{scene_id}/save-as` 保證 DRAFT proposal contract

**對齊基準：**
- UX_SPEC v0.4 §11.5.8.2 line 3772-3792（LOCKED race modal B 選項 — 另存 DRAFT proposal）
- DATA_FORMAT_SPEC v0.4 §3.2（phase_log + base_dialogue / iteration_note 欄位）

**當前邏輯（A.0F.1 baseline）：** `server.py:425-448` — 接 `{content, proposal_suffix?}` 直接寫入；不改 status / 不補 base_dialogue / iteration_note。

**修補要求：**
1. Body schema 擴充（向後相容；舊欄位仍接受）：
   ```json
   {
     "content": "<full markdown>",
     "proposal_suffix": "<optional>",
     "base_scene_id": "<原 LOCKED 檔 scene_id>",
     "iteration_note": "<選填 — user 對 proposal 的說明>"
   }
   ```
2. 在 write 前，**自動 patch content 的 frontmatter header**：
   - 若 content 內含 `狀態：LOCKED` 或 `狀態：FINAL` 等高階 status → 改成 `狀態：DRAFT`（DRAFT proposal contract）
   - 若 content 缺 frontmatter 5 欄 → 警示 + 跳過 patch（user 責任）
3. 同步 patch content 的 YAML block（若存在），加 / 更新 `base_dialogue` 欄位：
   - 值 = `base_scene_id`（若 body 有提供）
   - 若 body 沒提供 `base_scene_id`，從 URL path scene_id 推導（即原 scene 的 id）
4. 若 body 含 `iteration_note`，加到 content frontmatter YAML block 的 `iteration_note` 欄
5. 寫新檔 + 不覆蓋原檔（既有邏輯保留）

**回 JSON 擴充：**
```json
{
  "original_scene_id": "<id>",
  "saved_as_path": "<rel path>",
  "saved": true,
  "proposal_status": "DRAFT",
  "base_dialogue": "<base_scene_id>",
  "iteration_note_recorded": <bool>
}
```

**驗證：**
- tempfile 建 LOCKED 場景 → `POST /save-as` with content 含 `狀態：LOCKED` → 寫新檔 + 新檔 header `狀態：DRAFT` + frontmatter `base_dialogue: <原 id>`
- 不傳 `base_scene_id` → server 自動從 URL 推導

### Patch-A0F1-03：409 conflict response 擴 UX §11.7.5 shape

**對齊基準：**
- UX_SPEC v0.4 §11.7.5 line 4291-4300（multi-version conflict modal payload）

**當前邏輯（A.0F.1 baseline）：** `server.py:399-410` — 409 body 只回 `current_mtime / mtime_baseline / mtime_drift`。

**修補要求：**
mtime drift 409 response body 擴充為（向後相容；既有欄位保留 + 加新欄位）：

```json
{
  "error": "MTIME_DRIFT",
  "scene_id": "<id>",
  "current_mtime": <float>,
  "mtime_baseline": <float>,
  "mtime_drift": true,
  "server_content": "<full markdown of current file on disk>",
  "server_header": {<5 欄 header dict>},
  "client_content_length": <int>,
  "suggestion": "前端 Conflict modal 應顯示 server_content vs client_content 兩版差異"
}
```

**驗證：**
- tempfile 建 scene → 先 GET /header 拿 mtime baseline → 在 disk 上手動改檔 + sleep → POST /save with stale baseline → 應 409 + body 含 server_content / server_header / mtime_drift=true

### 通用實作策略

1. **不破壞既有 6 endpoint** — header / versions / keys-lines / assets / asset-usage / scope-counts 不動
2. **保留既有 helper** — `parse_file` / `resolve_scene_file` / `header_payload` 等可重用
3. **新增 helper（可選）：**
   - `is_locked(parsed) -> bool` — 從 parsed header 判斷
   - `patch_proposal_status(content) -> tuple[str, bool]` — 改 LOCKED→DRAFT，回 (new_content, was_patched)
   - `patch_frontmatter_field(content, field, value) -> str` — 加 / 更新 yaml block 欄位
4. **錯誤處理一致**：所有 409 都用相同 base shape + `error` 欄位區分原因

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/CODEX_WAVE2_REVIEW_REPORT.md`（NO-GO 報告 — finding 描述基準；§2 Review-W2-A.0F.1 殘留段）
2. `_design/TASKS.md` v1.4（§A.0F.1 line 874-889）
3. `_design/ARCHITECTURE.md` v1.3 §13.2 / §13.3
4. `_design/INTEGRATION_CONTRACTS.md` v2.1 §3.2 Contract B.2（LOCKED Save guard 5 步）
5. `_design/UX_SPEC.md` v0.4 §11.5.8 / §11.5.8.2 / §11.7.5
6. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log + base_dialogue）

B. 本輪修補對象（核心 — 你動的檔）
7. `_tools/frontend/server.py`（A.0F.1 baseline 567 行 — 你做 targeted patch；只動 save / save-as + 加 helper）

C. 對齊依據
8. `scripts/parse_frontmatter.py`（read-only — parse_file API 用法；已有 `header.狀態` 欄位）

D. 已 LOCKED 不可動文件（明示禁區）
9. 所有 `_design/*.md`（除前述引用段）
10. `_design/registries/*.template.yaml`
11. `scripts/*.py`
12. 既有 27 模板
13. `00_protocol/*` 所有檔
14. `_tools/frontend/static/*` / `requirements.txt` / `README.md`
15. server.py 中其他 6 endpoint（header / versions / keys-lines / assets / asset-usage / scope-counts）+ 啟動骨架

---

**你要交付的產物：**

修改：`_tools/frontend/server.py`（3 處 patch + 必要 helper；無新檔）

**驗收條件（CODEX 自我驗證）：**

A. 結構驗證
- save / save-as endpoint 還在原位置（line ~387 / ~425）
- 其他 6 endpoint 不動（grep diff 確認）
- 啟動骨架不動（uvicorn / argparse / StaticFiles）
- import server / `from server import app` 不報錯
- `python server.py --help` 顯示 --port / --host

B. A0F1-01 LOCKED guard 驗證
- tempfile LOCKED 檔 → POST /save → 409 + `error: LOCKED_OVERWRITE_DENIED`
- tempfile DRAFT 檔 → POST /save → 200 + 寫入成功
- response JSON 含 current_status / current_mtime / suggestion

C. A0F1-02 DRAFT proposal contract 驗證
- POST /save-as with content 含 LOCKED status → new file header 為 DRAFT
- new file frontmatter 含 `base_dialogue: <id>`
- response JSON 含 proposal_status / base_dialogue / iteration_note_recorded

D. A0F1-03 conflict body shape 驗證
- POST /save with stale mtime_baseline → 409 + body 含 server_content / server_header / mtime_drift=true
- 既有 mtime_drift / current_mtime / mtime_baseline 欄位保留

E. D-029 α 維持
- 無 subprocess / os.system / exec / eval（grep 0）
- 無 /api/export/run / /api/skill/run / /api/qa/run

F. 不破壞既有
- git diff --check 通過
- 沒動 _design / scripts / 00_protocol / 既有 27 模板 / _tools/frontend/static / requirements.txt / README.md
- 其他 6 endpoint 邏輯一字不動

G. 啟動 + curl smoke
- `python server.py --port 8765` 啟動成功
- 至少 4 個 curl test 跑過：
  1. POST /save 對 LOCKED file → 409 LOCKED_OVERWRITE_DENIED
  2. POST /save 對 DRAFT file → 200 + 寫入
  3. POST /save-as → 200 + 新檔 status=DRAFT
  4. POST /save with stale mtime → 409 含 server_content

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A0F1_PATCH_REPORT.md`（可選；同 Stage 0 A.0.10 patch report 模式）

報告格式（如交付）：

```markdown
狀態：REVIEW
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：A.0F.1 server.py 3 finding patch round 完成報告
優先級：高

# CODEX_A0F1_PATCH_REPORT

## 0. 摘要
**結論：[DONE / PARTIAL / FAIL]**
A0F1-01 ✓/✗ / A0F1-02 ✓/✗ / A0F1-03 ✓/✗

## 1. 修補檔案 + 行範圍
- _tools/frontend/server.py：（列各 patch 位置）

## 2. 3 finding 修補逐項
### A0F1-01 LOCKED guard
- 修補位置：line X-Y
- 修補摘要：（變動描述）
- curl test：[✓/✗]
- 殘留：

### A0F1-02 DRAFT proposal contract
- 修補位置：line X-Y
- 修補摘要：
- curl test：[✓/✗]
- 殘留：

### A0F1-03 conflict body shape
- 修補位置：line X-Y
- 修補摘要：
- curl test：[✓/✗]
- 殘留：

## 3. 驗收結果（A-G 7 維度）

## 4. 不在 scope 的觀察（如有）

## 5. Source Limitations
```

---

**Go / Done 判定指引：**

- **DONE：** A-G 7 驗收全 ✓ + 4 curl test 全 PASS
- **PARTIAL：** 1 finding △ 但其他 2 ✓ + curl test 對 ✓ 部分 PASS
- **FAIL：** ≥ 1 finding ✗ 或 curl test ✗

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.0F.1 patch round 完成後：
- User 手動 commit + push（server.py + 可選 report）
- 回 master 對話貼結果
- master read 報告 → 推 Wave 2 recheck CODEX（同 CODEX (e) recheck E2 模式 — 驗 A.3 master patch + A.0F.1 CODEX patch 是否落地）

---

# 3. 文件維護紀律

- 本檔是 CODEX A.0F.1 patch round 啟動包；完成後 archive
