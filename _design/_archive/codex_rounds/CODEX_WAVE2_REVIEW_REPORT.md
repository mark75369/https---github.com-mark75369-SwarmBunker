狀態：REVIEW
版本：v0.1
最後更新：2026-05-20
適用範圍：CODEX Wave 2 (A.2 + A.3 + A.0F.1) 獨立 review
優先級：高

# CODEX_WAVE2_REVIEW_REPORT

## 0. 摘要

**結論：NO-GO**

3 task：
- A.2 (00_i) ✓
- A.3 (00_e) ✗
- A.0F.1 (server.py) △

NO-GO 理由：
- A.3 缺 D-047 / Contract D 的 `issue_type_registry.yaml` 啟動讀取與動態議題清單段，屬 blocking。
- A.0F.1 的 8 endpoint 與 parser API 整合已落地，但 Save / Save-as 邊界仍未完全覆蓋 Contract B.2 / UX §11.5.8 的 race guard / DRAFT proposal 細節，判 Partial。

## 1. 審查範圍

### 1.1 Files Read

對齊基準：
- `_design/TASKS.md`:565-609, 874-889
- `_design/SPEC.md`:645-704
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`:97-232, 420-691
- `_design/ARCHITECTURE.md`:1338-1386
- `_design/INTEGRATION_CONTRACTS.md`:1067-1154, 1261-1325, 1595-1622, 1672-1810
- `_design/DATA_FORMAT_SPEC.md`:335-645, 692-961, 993-1354, 1803-2036
- `_design/UX_SPEC.md`:2514-2632, 3053-3317, 3689-3815, 4081-4215, 4549-4556
- `_design/DECISIONS_LOG.md`:1064-1073, 1118-1131, 1257-1274

審查對象：
- `00_protocol/00_i_專案初始化協議.md`:1-506
- `00_protocol/00_e_世界觀創建協議.md`:1-384
- `_tools/frontend/server.py`:1-567

對齊參考：
- `_design/registries/entity_type_registry.template.yaml`:1-77
- `_design/registries/qa_type_registry.template.yaml`:1-50
- `_design/registries/issue_type_registry.template.yaml`:1-121, 324-356

驗證命令 / 狀態：
- `git status --short -uall`
- `git diff -- ...`
- `python -B -c "from scripts.parse_frontmatter import parse_file; ... 00_i ..."`
- `python -B -c "from scripts.parse_frontmatter import parse_file; ... 00_e ..."`
- `python -X utf8 -B scripts\check_headers.py`
- `python -B _tools\frontend\server.py --help`
- `python -B -c "from _tools.frontend.server import app; ... app.routes ..."`
- `rg -n "subprocess|os\.system|\bexec\b|\beval\b" _tools\frontend\server.py`
- `rg -n "/api/export/run|/api/skill/run|/api/qa/run" _tools\frontend\server.py`

### 1.2 Files NOT Modified

本輪未修改以下被審查或基準檔：
- `00_protocol/00_i_專案初始化協議.md`
- `00_protocol/00_e_世界觀創建協議.md`
- `_tools/frontend/server.py`
- `_tools/frontend/static/`
- `_tools/frontend/requirements.txt`
- `_tools/frontend/README.md`
- `_design/*.md` 基準檔
- `_design/registries/*.yaml`
- `scripts/*.py`

本報告是唯一新建檔：
- `_design/CODEX_WAVE2_REVIEW_REPORT.md`

## 2. 三任務逐項驗證

### Review-W2-A.2：00_i Bootstrap protocol

- 狀態：✓

證據：
- Header 5 欄 + YAML block 存在：`00_protocol/00_i_專案初始化協議.md`:1-10。
- 10 主章節對齊 SPEC §8 bootstrap 10 區段：SPEC baseline `SPEC.md`:666-679；目標檔 headings `00_i`:21,40,59,102,138,169,245,260,274,312。
- §6 階段 4 含 7 step：`00_i`:169-184。包含 `.protocol_version`、00_b / 00_c / 00_d 微調、三 registry copy、`10_art_assets/` 7 subtype + index stub、Instance root `.gitignore`。
- §6.1 寫檔順序 6 步：`00_i`:186-193。順序為 `.protocol_version` → 三 registry → `10_art_assets/` → `.gitignore` → 00_b/c/d 微調 → reread verify。
- §6.2 `.protocol_version` 最小格式含 `bootstrapped_registries`：`00_i`:195-229。
- §10.2 完整範本含 `bootstrapped_registries` / `bootstrapped_directories` / `bootstrapped_files`：`00_i`:334-370。
- §10.5 三 registry copy 規範：`00_i`:416-440；D-047 baseline `DECISIONS_LOG.md`:1257-1274。
- §10.6 `10_art_assets/` 7 subtype + `index.md` stub：`00_i`:442-469；D-044 baseline `DECISIONS_LOG.md`:1126-1131。
- §10.7 `.gitignore` 必含 `export/`：`00_i`:476-506；D-038 baseline `DECISIONS_LOG.md`:1064-1073。
- §8 禁止 00_a / 00_e-00_l / 01-09 微調：`00_i`:260-270。
- Parser 驗證：`parse_file('00_protocol/00_i_專案初始化協議.md')` 回 `[]`。
- 全 repo header 檢查：`python -X utf8 -B scripts\check_headers.py` 回 `errors: 0`，另有既存 warnings 15。

殘留：
- 非阻塞：`00_i`:422 將 entity registry 的 A-* 7 subtype cross-ref 寫成 D-043；A-* 7 subtype 的主決策是 D-044。§10.6 已正確對齊 D-044，不影響 A.2 主要驗收。
- 非阻塞：§6.1 只明示 step 5 失敗 rollback `.protocol_version`；若後續要更嚴格，可補 partial registry / art dir / `.gitignore` 的清理細節。

### Review-W2-A.3：00_e 世界觀創建 protocol

- 狀態：✗

證據：
- Header 5 欄 + 日期 + YAML block 存在：`00_protocol/00_e_世界觀創建協議.md`:1-10。
- 目標檔有 00_e 的 1-10 專屬流程區段與 §10.1-§10.12：`00_e`:20-369。
- §10.1-§10.10 每題有五欄表格結構：格式定義 `00_e`:226-236，題目內容 `00_e`:238-336。
- §10.11 拆分規則表存在：`00_e`:338-357。
- §10.12 Frontmatter 規範保留：`00_e`:359-369。
- 無具體作品 / 角色名 / 蟲潮孤堡詞：`rg "蟲潮|孤堡|主角A|主角B|《"` 無命中；檔內僅有泛稱「作品」「角色」作協議邊界語。
- Parser 驗證：`parse_file('00_protocol/00_e_世界觀創建協議.md')` 回 `[]`。
- 全 repo header 檢查：`python -X utf8 -B scripts\check_headers.py` 回 `errors: 0`，另有既存 warnings 15。

Blocking / Major findings：
- **A3-01 Blocking：D-047 / Contract D 未落入 00_e。**  
  D-047 要求 `/create-*` 啟動時讀 `<instance_root>/issue_type_registry.yaml`，以 `core + user_extensions - core_overrides` 動態構建議題清單：`DECISIONS_LOG.md`:1261-1272、`INTEGRATION_CONTRACTS.md`:1748-1761。目標 §2 只檢查 bootstrap / phase_log / LOCKED / W 實體：`00_e`:38-50；§4 仍 hardcode 「11 個議題逐項提問」：`00_e`:80-96。全檔未出現 `issue_type_registry`、`user_extensions`、`core_overrides`、`00_e_world`。
- **A3-02 Major：§4 把 10.11 拆分規則列為 user-facing 議題。**  
  Registry template 明示 00_e 只有 10 個 user-facing 議題，10.11 拆分規則不入 registry、屬階段 4 mechanic：`issue_type_registry.template.yaml`:20-22, 47-50。目標 §4 仍列第 11 題「拆分規則確認」：`00_e`:82-96。
- **A3-03 Major：UD §1.1.2 提問腳本被濃縮，未完整沿用。**  
  TASKS 要求不擅自更動 UD §1.1 提問腳本：`TASKS.md`:594-609。抽查三題：10.1 目標 `00_e`:242-246 vs UD `UPSTREAM_DOWNSTREAM_SPEC.md`:428-451；10.2 目標 `00_e`:252-256 vs UD `UPSTREAM_DOWNSTREAM_SPEC.md`:457-474；10.7 目標 `00_e`:302-306 vs UD `UPSTREAM_DOWNSTREAM_SPEC.md`:574-590。目標保留五欄結構，但多處把完整對話稿改成摘要。
- **A3-04 Minor：嚴格 10 主章節格式有殘留 extra top-level。**  
  目標檔在 10 區段後另有 `# 11. 與下游的銜接點` / `# 12. UX 標記`：`00_e`:373-391。內容可追溯 UD §1.1.3 / §1.1.4，但若按「10 個主章節」驗收，應併回或標明非主章節附錄。

殘留：
- A.3 需 patch 後 recheck；本輪不建議 Wave 3。

### Review-W2-A.0F.1：server.py 8 endpoint adapter

- 狀態：△

證據（按 A/B/C/D/E/F/G 7 維度）：

A. Endpoint 結構：Pass
- ARCH §13.2 要求 8 endpoint：`ARCHITECTURE.md`:1352-1363。
- `server.py` 8 endpoint 全在：`server.py`:369, 387, 425, 455, 475, 505, 528, 540。
- `app.routes` import 列舉有 8 個 API route；另有 FastAPI docs/openapi/redoc 與 static mount，不是禁用 endpoint。

B. Parser API 整合：Pass
- import 存在：`server.py`:22-23。
- `parse_file` 用於 scene 檔掃描：`server.py`:100-107。
- `build_repo_index` 用於 assets / usage / scope-counts endpoint：`server.py`:509, 531, 546。

C. Logic 完整性：Partial
- header 回 `{scene_id, path, header, mtime, issues}`：`server.py`:369-382。
- save 接 `{content, mtime_baseline}` 並偵測 mtime drift：`server.py`:387-418。
- save-as 接 `{content, proposal_suffix?}`，寫新檔且 target exists 回 409：`server.py`:425-448。
- versions 回 `{scene_id, versions: [{version, path, mtime, header}]}`：`server.py`:455-470。
- keys-lines 回 `{scene_id, key, lines: [{version, line_index, content, speaker, status}]}`：`server.py`:475-500。
- assets 支援 `scope=all|scene/<id>|subtype/<name>` 並回 `{scope, assets, total}`：`server.py`:505-523。
- asset-usage 回 `{asset_id, usage, total}`，usage 含 `{scene_id, key, field, version}`：`server.py`:195-231, 528-535。
- scope-counts 支援 `scope=full|scene/<id>|chapter/<ch>` 並回 `{scope, counts}`：`server.py`:292-347, 540-547。
- Partial 原因：Save / Save-as 詳見 findings A0F1-01 / A0F1-02。

D. D-029 alpha 禁止 command：Pass
- `rg "subprocess|os\.system|\bexec\b|\beval\b"` 無命中。
- `rg "/api/export/run|/api/skill/run|/api/qa/run"` 無命中。
- ARCH §13.3 明示禁用 endpoint：`ARCHITECTURE.md`:1365-1369。

E. 錯誤處理：Partial
- scene not found 404：`server.py`:373-374, 394-395, 431-432, 459-460, 479-480。
- asset not found 404：`server.py`:532-533。
- 內部例外 500 + `{"error": "<msg>"}`：`server.py`:383-384, 421-422, 451-452, 471-472, 501-502, 524-525, 536-537, 548-549。
- save mtime drift 409：`server.py`:397-410。
- proposal target exists 409：`server.py`:437-438。
- Partial 原因：409 conflict body 是單檔 mtime 簡化版，未含 UX §11.7.5 多版本 conflict modal 需要的 current content / conflict versions：`UX_SPEC.md`:4291-4300。

F. 既有啟動骨架：Pass
- `StaticFiles` mount：`server.py`:552-553。
- `uvicorn` + `argparse`：`server.py`:556-567。
- `python -B _tools\frontend\server.py --help` 成功，顯示 `--port` / `--host`。

G. 其他：Pass / Limited
- `_tools/frontend/static/`、`_tools/frontend/requirements.txt`、`_tools/frontend/README.md` 無 diff。
- 沒有啟動 listen；以 import `app.routes` 方式驗證 route 結構。嘗試 FastAPI TestClient 時本機缺 `httpx`，因此未做 HTTP-level request test。

殘留：
- **A0F1-01 Major：`POST /api/scene/{id}/save` 沒有 server-side LOCKED guard。**  
  Contract B.2 / UX §11.5.8 要求實際寫檔前重讀最新 source header，若最新 `狀態=LOCKED` 禁止 overwrite：`INTEGRATION_CONTRACTS.md`:1076-1104、`UX_SPEC.md`:3689-3719。目前 save endpoint 只做 mtime 比對，通過後直接 `write_text`：`server.py`:397-412。若前端漏掉 Step 3 pre-flight，server 端不會獨立擋 LOCKED overwrite。
- **A0F1-02 Major：save-as 未完整保證 DRAFT proposal contract。**  
  UX §11.5.8.2 B 選項要求 proposal 新檔為 DRAFT，並以原 LOCKED 檔為 base 補 `base_dialogue / iteration_note` 等資訊：`UX_SPEC.md`:3772-3792。A.0F.1 starter 允許簡化為 `{content, proposal_suffix?}`，目前 server 也只直接寫入傳入 content：`server.py`:428-440；這代表 server 不保證 header 狀態被改為 DRAFT。
- **A0F1-03 Minor：409 conflict response 為單檔簡化版。**  
  UX §11.7.5 描述多版本 payload 與 conflict versions / server current content：`UX_SPEC.md`:4291-4300。現行 endpoint 只回 `current_mtime` / `mtime_baseline` / `mtime_drift`：`server.py`:399-410。

## 3. 新發現的 finding

- A3-01 Blocking：00_e 未整合 D-047 / Contract D `issue_type_registry.yaml` 啟動與動態議題清單。
- A3-02 Major：00_e §4 仍把 10.11 拆分規則當 user-facing 議題。
- A3-03 Major：00_e §10.1 / §10.2 / §10.7 抽查顯示 UD 提問腳本被濃縮，未完整沿用。
- A0F1-01 Major：server save endpoint 缺 server-side LOCKED guard。
- A0F1-02 Major：server save-as 未保證 DRAFT proposal contract。
- A0F1-03 Minor：server 409 conflict body 未達 UX 多版本 conflict modal shape。

## 4. Go / No-Go 決定

- **NO-GO。**

判定規則：
- GO：3 task 全 ✓。
- NEAR-GO：2 ✓ + 1 △，且 △ 不涉結構性問題。
- NO-GO：≥ 1 ✗ 或 ≥ 2 △。

本輪結果為 1 ✓ + 1 ✗ + 1 △，且 A.3 是 blocking fail，因此不建議 master 直接推 Wave 3。建議先 patch A.3；A.0F.1 可同步補 Save / Save-as 契約後一起 recheck。

## 5. Source Limitations

- 本輪只審 A.2 / A.3 / A.0F.1；未重審 CODEX (c)/(d)/(d2)/(e)/(e2)、Gate 1 / A.0.10、Wave 1、D-001-D-047 拍板本身或 REQUIREMENTS_LOCK。
- `_design/*.md` 基準檔只作引用依據，未修改。
- `scripts/*.py` 只執行 parser/header 檢查，未修改。
- 未啟動本地 server listen；route verification 以 import `app.routes` 完成。
- FastAPI TestClient 因本機缺 `httpx` 未執行；因此沒有 HTTP client-level response test。
- `check_headers.py` 第一次在 cp950 終端輸出遇到 emoji encode error；已用 `python -X utf8 -B` 重跑，結果 `errors: 0`。
- `git status --short -uall` 在寫報告前為 clean；本報告是本輪唯一新增檔。
