狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A Wave 2 完成後的 CODEX 獨立 review 啟動包  
優先級：高

# CODEX_WAVE2_REVIEW_STARTER — Wave 2 (A.2 + A.3 + A.0F.1) 獨立 review

# 0. 本檔用途

Wave 2 三條任務全 DONE：
- **A.2** `00_protocol/00_i_專案初始化協議.md` — master 直接 patch（CODEX 原本 BLOCKED 因檔已 tracked 存在；master 補 6 處 — §6 階段 4 step 5-7 + §6.1 寫檔順序 + §6.2 / §10.2 .protocol_version + §10.5 / §10.6 / §10.7 三新段）
- **A.3** `00_protocol/00_e_世界觀創建協議.md` — master 直接 patch（CODEX 寫到一半截斷被 git discard 救回 + master 補 YAML block + 日期；其餘 372 行原本即對齊 A.3 spec — 含 §4 D-047 對齊段 + §10.1~§10.12）
- **A.0F.1** `_tools/frontend/server.py` — CODEX 完整實作（80 行 scaffold → 567 行真實 adapter；8 endpoint 全實裝 + parser API 整合）

本檔給 CODEX 對話「Wave 2 reviewer」啟動用 — 獨立眼睛驗證三條任務落地是否對齊 spec + 是否有未發現 issue。

**前置條件：**
- ✓ Wave 1（A.1 / A.4 / A.0F.0）全 DONE + push
- ✓ Wave 2 三條全 DONE（檔在 working tree；可能尚未 commit/push）
- ✓ Stage 0 A.0.10 parser baseline 維持 0 ERROR

**本檔跟既有 review starter 的差別：**

| 維度 | CODEX_REVIEW_STARTER_E / RECHECK_STARTER_E2 | **本檔 WAVE2_REVIEW_STARTER** |
|---|---|---|
| Phase | 設計層 / partial supersede 升版 review | **Phase A 後段 + A.0F alpha 實作層 review** |
| CODEX 身份 | reviewer | reviewer（同） |
| Scope | 5 review item / 3 finding recheck | **3 任務 × 各自驗證**（A.2 / A.3 / A.0F.1） |
| 預估時數 | 30-45 分 / 15-25 分 | **30-45 分** |
| 預期產出 | review report | **CODEX_WAVE2_REVIEW_REPORT.md（GO / NEAR-GO / NO-GO）** |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「Phase A Wave 2 完成後」的 CODEX 獨立 review — 對 A.2 / A.3 / A.0F.1 三條任務做眼睛獨立 review。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支或 working tree 上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔、不改 spec、不改任何被 review 對象
- 你是 targeted reviewer — 只驗證 A.2 / A.3 / A.0F.1 三個 task 的落地對齊 + 找潛在 finding
- 你是 Wave 2 ↔ Wave 3 之間的 checkpoint — 通過 → master 推 Wave 3 (A.5 / A.6 / A.0F.2)；不通過 → 各自 patch
- 對應傳統：本輪是第 10 輪 CODEX 審查（前 9 輪：時期 A 4 輪 + (c) + (d) + (d2 Part1/2/3) + Gate 1/A.0.10 + (e)/(e2)）

**重要邊界（嚴格 scope）：**

- ✗ **不**重審 CODEX (c) / (d) / (d2) / (e) / (e2) 已 RESOLVED 議題
- ✗ **不**重審 Gate 1 NO-GO + A.0.10 patch round（已 PASS）
- ✗ **不**重審 Wave 1（A.1 / A.4 / A.0F.0）（已 PASS）
- ✗ **不**動 D-001 ~ D-047 拍板結論
- ✗ **不**動 REQUIREMENTS_LOCK.md（v1.0 FINAL）
- ✗ **不**寫實作；reviewer only
- ✗ **不**做 Wave 3 預測 / 計畫

**本輪 scope（嚴格限定 — 3 個 task 獨立 review）：**

### Review-W2-A.2：`00_protocol/00_i_專案初始化協議.md`

**檢查對象：** `00_protocol/00_i_專案初始化協議.md`（master 第五輪直接 patch 後的版本）

**必看：**
- Header 5 欄 + YAML block (entities=[] / depends_on=[] / weight={})
- 10 個主章節對齊 SPEC §8 Bootstrap 流程表
- §6 階段 4 含 7 step（寫 .protocol_version / 00_b/00_c/00_d 微調 / 三 registry copy / 10_art_assets/ 7 subtype 子目錄 / .gitignore）
- §6.1 寫檔順序 6 步 + rollback 規則
- §6.2 `.protocol_version` 最小格式含 `bootstrapped_registries:` 段（含 entity_type / qa_type / issue_type 三 registry 對應 source/target/version）
- §10.2 `.protocol_version` 完整範本同含 `bootstrapped_registries:` / `bootstrapped_directories:` / `bootstrapped_files:` 三段
- §10.5 三 registry copy 規範對齊 D-043 + D-047
- §10.6 10_art_assets/ 7 subtype 子目錄 + index.md stub 規範對齊 D-044
- §10.7 Instance root `.gitignore` 規範對齊 D-038 附帶第 3 項（export/ 必含）
- 禁止事項 §8 明示 00_a / 00_e ~ 00_l / 01-09 不可微調
- Parser 驗證：跑 `python -c "from scripts.parse_frontmatter import parse_file; r = parse_file('00_protocol/00_i_專案初始化協議.md'); print(r.issues)"` → 預期 `[]`
- 全 repo `python scripts/check_headers.py` → 0 ERROR

**對齊基準：** TASKS v1.4 §A.2 + SPEC v1.2 §8 + DECISIONS_LOG v1.1 §6.9.2（D-047）

**判定：** ✓ Pass / ✗ Fail / △ Partial（含證據 + line ref）

### Review-W2-A.3：`00_protocol/00_e_世界觀創建協議.md`

**檢查對象：** `00_protocol/00_e_世界觀創建協議.md`（master 第五輪 minimal patch — 補 YAML block + 升日期；原 372 行已對齊 A.3 spec）

**必看：**
- Header 5 欄 + 最後更新 = 2026-05-19 + YAML block (entities=[] / depends_on=[] / weight={})
- 10 個主章節對齊 UD §1.0.1 共通骨架
- §2 啟動條件含 issue_type_registry.yaml 讀取（D-047 對齊）
- §4 階段 2 含完整 D-047 對齊段（讀 `<instance_root>/issue_type_registry.yaml` 00_e_world 區段 / Contract D §4a.2 / core + user_extensions - core_overrides 動態構建 / locked=true 不可 SKIP）
- §4 11 議題 + required_level + locked 對齊表（10.1~10.11 + N/A 拆分規則）
- §10 專屬區段含 11 議題 §10.1 ~ §10.11
- §10.1 ~ §10.10 每議題含 5 欄結構（為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答跳題）
- §10.1 ~ §10.10 內容跟 UD §1.1.2 對應段對照 — 隨機抽 3 個議題確認文字一致（不擅自重寫）
- §10.11 拆分規則對齊 UD §1.1.2 §10.11 拆分計畫表
- §10.12 Frontmatter 規範段（00_e 原檔有的 extra 段，A.3 spec 沒明示要但保留 OK）
- 整檔無作品 / 角色名 / 蟲潮孤堡相關詞
- Parser 驗證：`r = parse_file(...)` → issues = []
- 全 repo `check_headers.py` 0 ERROR

**對齊基準：** TASKS v1.4 §A.3 + UD v0.5 §1.1 全段 + DECISIONS_LOG v1.1 §6.9.2 + INTEGRATION_CONTRACTS v2.1 §4a Contract D

**判定：** ✓ Pass / ✗ Fail / △ Partial

### Review-W2-A.0F.1：`_tools/frontend/server.py`

**檢查對象：** `_tools/frontend/server.py`（A.0F.0 scaffold 80 行 → A.0F.1 真實實作 567 行）

**必看：**

A. Endpoint 結構
- 8 endpoint 全在（對應 ARCH §13.2）：
  - GET /api/scene/{scene_id}/header
  - POST /api/scene/{scene_id}/save
  - POST /api/scene/{scene_id}/save-as
  - GET /api/scenes/{scene_id}/versions
  - GET /api/scenes/{scene_id}/keys/{key}/lines
  - GET /api/assets
  - GET /api/assets/{asset_id}/usage
  - GET /api/scope-counts
- 禁用 endpoint 不存在（grep `app.routes` 確認 0 個）：
  - /api/export/run / /api/skill/run / /api/qa/run

B. Parser API 整合
- `from scripts.parse_frontmatter import build_repo_index, parse_file` import 存在
- `build_repo_index` 在 endpoint 內使用（不只是 stub）
- `parse_file` 在 endpoint 內使用

C. Logic 完整性（按 starter §1 規範對齊）
- header endpoint 回 `{scene_id, path, header, mtime, issues}`
- save endpoint 接 `{content, mtime_baseline}` + mtime drift 偵測（409 conflict）
- save-as endpoint 接 `{content, proposal_suffix?}` + 寫新檔 + 不覆蓋原檔
- versions endpoint 回 `{scene_id, versions: [{version, path, mtime, header}, ...]}`
- keys-lines endpoint 回 `{scene_id, key, lines: [{version, line_index, content, speaker, status}, ...]}`
- assets endpoint 接 `scope=all|scene/<id>|subtype/<name>` + 回 `{scope, assets, total}`
- asset-usage endpoint 回 `{asset_id, usage: [{scene_id, key, field, version}, ...], total}`
- scope-counts endpoint 接 `scope=full|scene/<id>|chapter/<ch>` + 回 `{scope, counts: {entities, dialogue_lines, art_assets, qa_reports}}`

D. 對齊 D-029 α
- **無** subprocess 呼叫（grep `subprocess` / `os.system` / `exec` / `eval` → 預期 0）
- **無** export / skill / qa command line 觸發
- 純 read markdown / write markdown / parser API call

E. 錯誤處理
- 找不到 scene → 404
- 內部例外 → 500 + JSON `{"error": "<msg>"}`
- mtime drift（POST /save 時 baseline ≠ server-side current）→ 409 conflict

F. 不破壞既有
- server.py 啟動骨架（uvicorn / argparse / StaticFiles mount）保留
- `python server.py --help` 顯示 --port / --host

G. 其他
- 不動 `_tools/frontend/static/` / requirements.txt / README.md
- 8 endpoint 至少跑得起來（CODEX 若 sandbox 不能 listen，import server + app routes 列舉即可）

**對齊基準：** TASKS v1.4 §A.0F.1 + ARCH v1.3 §13.2 + INTEGRATION_CONTRACTS v2.1 Contract B.2 / B.4 / C.3 + UX v0.4 §11.5.8 / §11.1.6a / §11.3.3 / §11.3.5 / §11.6.11

**判定：** ✓ Pass / ✗ Fail / △ Partial

---

**必讀文件（按順序）：**

A. 對齊基準（不審；當依據；只看引用段落）
1. `_design/TASKS.md` v1.4（§A.2 line 565-584 + §A.3 line 586-609 + §A.0F.1 line 874-889）
2. `_design/SPEC.md` v1.2 §8（Bootstrap 流程）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.0.1 / §1.1（共通骨架 + 完整 11 議題提問腳本）
4. `_design/ARCHITECTURE.md` v1.3 §13.2 / §13.3
5. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D / §3.2 B.2 / §3.4 B.4 / §4.3 C.3
6. `_design/DATA_FORMAT_SPEC.md` v0.4 §3 / §4 / §5 / §8（dialogue_keys / art_metadata / qa_type schema）
7. `_design/UX_SPEC.md` v0.4 §11.5.8 / §11.1.6a / §11.3.3 / §11.3.5 / §11.6.11

B. 本輪審查對象（核心）
8. `00_protocol/00_i_專案初始化協議.md`（A.2 — master patched）
9. `00_protocol/00_e_世界觀創建協議.md`（A.3 — master patched）
10. `_tools/frontend/server.py`（A.0F.1 — CODEX implementation）

C. 對齊參考
11. `_design/registries/entity_type_registry.template.yaml`（v0.3 — Bootstrap copy 來源）
12. `_design/registries/qa_type_registry.template.yaml`（v0.3 — 同上）
13. `_design/registries/issue_type_registry.template.yaml`（v0.1 — D-047 落地，A.3 §4 依此動態構建議題清單）

D. 已 LOCKED 不可動（明示禁區，CODEX 本輪不審）
14. 所有 `_design/*.md`（除前述引用段）
15. `scripts/*.py`
16. Wave 1 產出物（`00_protocol/00_b_反ai味檢查表.md` + 27 模板 frontmatter + `_tools/frontend/static/`）

---

**你要交付的產物：**

新建：`_design/CODEX_WAVE2_REVIEW_REPORT.md`

報告格式：

```markdown
狀態：REVIEW  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX Wave 2 (A.2 + A.3 + A.0F.1) 獨立 review  
優先級：高  

# CODEX_WAVE2_REVIEW_REPORT

## 0. 摘要

**結論：[GO / NO-GO / NEAR-GO]**

3 task：
- A.2 (00_i) ✓/✗/△
- A.3 (00_e) ✓/✗/△
- A.0F.1 (server.py) ✓/✗/△

## 1. 審查範圍

### 1.1 Files Read
（列實際讀的檔 + line range）

### 1.2 Files NOT Modified
（明示沒動的檔；report 本身是唯一新建）

## 2. 三任務逐項驗證

### Review-W2-A.2：00_i Bootstrap protocol
- 狀態：✓/✗/△
- 證據：（line ref + 評語）
- 殘留：（如有）

### Review-W2-A.3：00_e 世界觀創建 protocol
- 狀態：✓/✗/△
- 證據：
- 殘留：

### Review-W2-A.0F.1：server.py 8 endpoint adapter
- 狀態：✓/✗/△
- 證據（按 A/B/C/D/E/F/G 7 維度逐項報告）：
- 殘留：

## 3. 新發現的 finding（若有）

不期望出現新衝突；若 Wave 2 引入新問題列在這。

## 4. Go / No-Go 決定

- **GO：** 3 task 全 ✓ → master 推 Wave 3 (A.5 / A.6 / A.0F.2)
- **NEAR-GO：** 2 ✓ + 1 △，△ 不涉結構性問題 → master 自決
- **NO-GO：** ≥ 1 ✗ 或 ≥ 2 △ → 對應 task patch 後再 recheck

## 5. Source Limitations

（你實際讀的檔；不審範圍；任何依靠假設的判斷）
```

---

**Go / No-Go 判定指引：**

- **GO：** 3 task 全 ✓
- **NEAR-GO：** 2 ✓ + 1 △（△ minor 不涉結構）
- **NO-GO：** ≥ 1 ✗ 或 ≥ 2 △

請開始。
```

---

# 2. 完成條件 + 後續

CODEX Wave 2 review 完成 = 報告產出 + GO/NO-GO 結論 + 沒動任何被 review 檔。

CODEX 完成後：
- User commit + push report
- master 接 review report → 若 GO 推 Wave 3；若 NEAR-GO/NO-GO 對應 task patch

---

# 3. 文件維護紀律

- 本檔是 CODEX Wave 2 review 啟動包；完成後可 archive
