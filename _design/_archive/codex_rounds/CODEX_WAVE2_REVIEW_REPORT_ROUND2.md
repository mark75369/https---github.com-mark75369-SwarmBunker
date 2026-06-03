狀態：REVIEW
版本：v0.1
最後更新：2026-05-20
適用範圍：CODEX Wave 2 Round 2 重審 (A.2 + A.3 + A.0F.1) — 修補後驗證
優先級：高

# CODEX_WAVE2_REVIEW_REPORT_ROUND2

## 0. 摘要

**結論：NEAR-GO**

本輪為 Round 2 — Round 1 NO-GO 修補後重審。對 Round 1 已 PASS 項目快查；對 Round 1 △/✗ 項目重點驗 7 finding 修補。

3 task：
- A.2 (00_i) ✓ PASS (Round 1: ✓ PASS；本輪 sanity check 維持)
- A.3 (00_e) △ PARTIAL (Round 1: ✗ FAIL；本輪驗 A3-01/02/03/04，A3-02 有 2 處文字殘留)
- A.0F.1 (server.py) ✓ PASS (Round 1: △ Partial；本輪驗 A0F1-01/02/03 均補完)

NEAR-GO 理由：A.3 的實際機制已改為 10 個 user-facing 議題 + §10.11 mechanic，但仍有兩處文字寫「11 個/11 項議題」。此為語意殘留，未見結構性阻斷；依本輪規則屬 2 ✓ + 1 △。

## 1. 審查範圍

### 1.1 Files Read

- `_design/TASKS.md`：565-609、874-889
- `_design/SPEC.md`：645-681；另快查 10_art_assets / registry / export 對齊關鍵詞
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`：97-229、358-692
- `_design/ARCHITECTURE.md`：1299-1310、1352-1369
- `_design/INTEGRATION_CONTRACTS.md`：1067-1120、1261、1595-1622、1672-1784
- `_design/DATA_FORMAT_SPEC.md`：333-637、643-961、972-1358、1803-2029
- `_design/UX_SPEC.md`：2514-2636、3053-3172、3674-3818、4081-4215、4282-4321、4541-4562
- `_design/CODEX_WAVE2_REVIEW_REPORT.md`：9-20、111-188、192-197
- `_design/CODEX_A0F1_PATCH_STARTER.md`：11-17、56-150、207-223
- `00_protocol/00_i_專案初始化協議.md`：1-10、169-231、334-370、416-501
- `00_protocol/00_e_世界觀創建協議.md`：1-10、38-125、135-145、253-435
- `_tools/frontend/server.py`：1-23、105、208-223、488-619、622-734
- `_design/registries/entity_type_registry.template.yaml`：6-87 quick check
- `_design/registries/qa_type_registry.template.yaml`：13-50 quick check
- `_design/registries/issue_type_registry.template.yaml`：33-355 quick check

### 1.2 Files NOT Modified

- 未修改 `00_protocol/00_i_專案初始化協議.md`
- 未修改 `00_protocol/00_e_世界觀創建協議.md`
- 未修改 `_tools/frontend/server.py`
- 未修改任何 `_design/*.md` 基準文件、`scripts/*.py`、`_tools/frontend/static/`、`requirements.txt`、`README.md`
- 本報告 `_design/CODEX_WAVE2_REVIEW_REPORT_ROUND2.md` 是唯一新增檔案

## 2. 三任務逐項驗證

### Review-W2-A.2：00_i Bootstrap protocol（Round 1 ✓ — 本輪 sanity check 維持）

- 狀態：✓ PASS
- 證據：
  - Header 5 欄 + YAML block 存在：`00_i`:1-10。
  - §6 階段 4 有 7 step，含 `.protocol_version`、00_b/00_c/00_d 微調、三 registry copy、`10_art_assets/` 7 subtype、root `.gitignore`：`00_i`:169-184。
  - §6.1 寫檔順序 6 步，含 registry 失敗 rollback：`00_i`:186-193。
  - §6.2 `.protocol_version` 最小格式含 `bootstrapped_registries` 三 registry source/target/version：`00_i`:195-217。
  - §10.2 完整範本含 `bootstrapped_registries` / `bootstrapped_directories` / `bootstrapped_files`：`00_i`:334-370。
  - §10.5 三 registry copy 對齊 D-043 + D-047：`00_i`:416-438。
  - §10.6 建 `10_art_assets/portrait bg cg sfx bgm voice ui` + index stub，對齊 D-044：`00_i`:442-474。
  - §10.7 `.gitignore` 至少含 `export/`：`00_i`:476-501。
  - 禁止事項明示不可微調 `00_a`、`00_e`-`00_l`：`00_i`:260-266。
- 驗證：
  - `parse_file('00_protocol/00_i_專案初始化協議.md')` → `[]`
  - `PYTHONIOENCODING=utf-8 python scripts/check_headers.py` → `errors: 0`、`warnings: 15`（既有 WARN，非本輪 ERROR）
- 殘留：無。

### Review-W2-A.3：00_e 世界觀創建 protocol（Round 1 ✗ — 本輪重點驗 4 finding 修補）

- 狀態：△ PARTIAL
- A3-01 D-047 機制段 (§2 + §4.0)：驗 ✓
  - §2 啟動條件要求 `<instance_root>/issue_type_registry.yaml` 可讀，缺檔 fallback、schema 異常拒絕：`00_e`:47-50。
  - §4.0 動態構建明示讀 `00_e_world`，依 `core + user_extensions - core_overrides`，locked=true 不可 SKIP，required_level 行為也有定義：`00_e`:85-104。
- A3-02 議題清單 11→10 + mechanic：驗 △
  - 已補 10 個 user-facing 議題：`00_e`:108-121。
  - 已明示 §10.11 拆分規則是 agent-side execution mechanic、非 user-facing：`00_e`:100、123、387-389。
  - 殘留 1：階段 3 仍寫「11 個議題的最終結論，每題一句話」：`00_e`:141。
  - 殘留 2：§10 標題仍寫「11 項議題 agent 提問腳本」：`00_e`:253。
- A3-03 §10 UD line ref 對照表 + Phase B skill 行為說明（hybrid 策略）：驗 ✓
  - §10 開頭明示 UD §1.1.2 為完整提問腳本權威，本檔為 5-column speed reference：`00_e`:255-285。
  - 對照表覆蓋 §10.1-§10.11：`00_e`:261-273。
  - Phase B 行為明示啟動時讀 registry，再 fetch UD 對應段，不擅自重寫 / 不擅自濃縮：`00_e`:275。
- A3-04 §11/§12 改 附錄 A / 附錄 B + 格式說明：驗 ✓
  - 原下游銜接與 UX 標記已改為「附錄 A / 附錄 B」，且明示非主流程章節：`00_e`:422-435。
- 其他檢查：
  - Header 5 欄 + 最後更新 2026-05-19 + YAML block：`00_e`:1-10。
  - §10.1-§10.10 均為 5 欄結構：`00_e`:287-385。
  - §10.11 拆分規則保留固定寫檔表：`00_e`:387-407。
  - §10.12 Frontmatter 規範保留：`00_e`:408-418。
  - `rg` 未命中 `蟲潮孤堡|主角A|女主|男主|蟲潮|孤堡`，未見具體作品 / 角色污染。
  - `parse_file('00_protocol/00_e_世界觀創建協議.md')` → `[]`
- 整體證據 / 殘留：
  - 4 個 Round 1 finding 中 A3-01/A3-03/A3-04 已補完；A3-02 機制補完但文字殘留 2 處。
  - 建議 patch：`00_e`:141 改為「10 個 user-facing 議題的最終結論 + §10.11 拆分計畫」；`00_e`:253 改為「10 個 user-facing 議題 + 1 項拆分 mechanic」。

### Review-W2-A.0F.1：server.py（Round 1 △ — 本輪重點驗 3 finding 修補）

- 狀態：✓ PASS
- A0F1-01 LOCKED guard：驗 ✓
  - `save` endpoint 重讀 `parse_file(path)`：`server.py`:516-518。
  - LOCKED 時先於 mtime drift 回 409 `LOCKED_OVERWRITE_DENIED`：`server.py`:519-529。
  - mtime drift 檢查在 LOCKED guard 後：`server.py`:531-546。
- A0F1-02 DRAFT proposal contract：驗 ✓
  - `save-as` 接 `content`、`proposal_suffix`、`base_scene_id` / fallback `base_dialogue`、`iteration_note`：`server.py`:561-570。
  - target 已存在則 409，不覆蓋：`server.py`:576-579。
  - 自動 patch header 狀態為 DRAFT：`server.py`:581-584；helper：`server.py`:208-223。
  - 補 `base_dialogue` / `iteration_note` 到 YAML block，並回傳 `proposal_status` 等欄位：`server.py`:586-609。
- A0F1-03 conflict body shape：驗 ✓
  - mtime drift 409 回 `error: MTIME_DRIFT`、`server_content`、`server_header`、`mtime_drift`、`client_content_length`：`server.py`:531-546。
- A-G 7 維度其他項目：
  - 8 endpoint 全在：`server.py`:488、506、561、622、642、672、695、707；import route list 也列出這 8 條。
  - 禁用 endpoint `/api/export/run`、`/api/skill/run`、`/api/qa/run` 不存在；route list `disabled=[]`，`rg` 無命中。
  - Parser API 整合：`from scripts.parse_frontmatter import build_repo_index, parse_file`：`server.py`:23；`parse_file` 用於 resolve / save：`server.py`:105、517；`build_repo_index` 用於 assets / usage / scope-counts：`server.py`:676、698、713。
  - header endpoint 回 `{scene_id, path, header, mtime, issues}`：`server.py`:488-501。
  - versions endpoint 回 versions list：`server.py`:622-637。
  - keys-lines endpoint 回 lines list：`server.py`:642-667。
  - assets / usage / scope-counts endpoint shape 對齊：`server.py`:672-714。
  - 無 `subprocess` / `os.system` / `exec` / `eval` 命中。
  - `python _tools/frontend/server.py --help` 顯示 `--port` / `--host`；argparse + uvicorn + StaticFiles 保留：`server.py`:720-734。
- 整體證據 / 殘留：
  - 無 blocking residual finding。
  - 未啟動 live server，也未對 save/save-as 做 curl POST 寫檔 smoke；本輪以 import route list、help、grep、靜態邏輯與 parser/header 驗證為準。

## 3. 新發現的 finding（若有）

- **A3-R2-01 Minor：A3-02 修補後仍有兩處「11 個/11 項議題」文字殘留。**
  - `00_protocol/00_e_世界觀創建協議.md`:141：階段 3 預告稿仍要求「11 個議題的最終結論」。
  - `00_protocol/00_e_世界觀創建協議.md`:253：§10 標題仍寫「11 項議題 agent 提問腳本」。
  - 影響：與 Round 2 目標「10 user-facing + §10.11 mechanic」語意不完全一致；但 §4.0 / §4.1 / §10.11 實際機制已正確，未見結構性阻斷。

## 4. Go / No-Go 決定

- **GO：** 否。A.3 仍有 1 個 minor Partial。
- **NEAR-GO：** 是。A.2 ✓ + A.0F.1 ✓ + A.3 △；A.3 △ 不涉結構性問題，屬文字殘留。
- **NO-GO：** 否。未見任一 ✗，也未達 ≥ 2 △。

建議 master 在 Wave 3 前自行做 2 行文字 patch，或接受 NEAR-GO 後於下一個文案清理 round 修正。

## 5. Source Limitations

- 本輪只做 A.2 / A.3 / A.0F.1 targeted review，未重審 CODEX (c)/(d)/(d2)/(e)/(e2)、Gate 1/A.0.10、Wave 1、D-001~D-047 拍板本身。
- `_design/*.md` LOCKED/FINAL 文件僅作引用基準，未修改。
- `scripts/*.py` 僅執行驗證，未修改。
- `check_headers.py` 第一次在 Windows cp950 console 下因既有勾選符號輸出發生 `UnicodeEncodeError`；以 `PYTHONIOENCODING=utf-8` 重跑後完成，結果 `errors: 0`、`warnings: 15`。
- A.0F.1 未跑會寫檔的 POST smoke；避免 reviewer round 對 review 對象或 fixture 產生副作用。已用 app route import、help、grep 與靜態 line review 替代。
