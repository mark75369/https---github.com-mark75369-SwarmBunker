狀態：DRAFT
版本：v0.1（11th master 對話 A 起草 — NEW_REQ_44 backend pending-status endpoint 前置 3-schema 拍板包；供 user 拍板 D-062；落地後才開 frontend+backend 實作 task）
最後更新：2026-06-01
適用範圍：定義 dashboard `/api/dashboard/pending-status` endpoint 所需的 3 個資料 schema（09_e 待裁決標記 / Canon Δ 候選儲存 / QA-pending 判定）；屬 NEW_REQ_44 前置 design gate；對應 frontend cycle F1-3b 拆出項
優先級：高

# D-062 DECISION PACKAGE — dashboard pending-status 3-schema 拍板包

> **議題號說明：** 本包初稿曾暫編 D-056，但 D-056~D-061 已由 11th master 對話 B（M4 follow-up）預留給 NEW_REQ_25-43（D-056 = NEW_REQ_27 `/create-world` split rule）。故順延至**下一個未用號 D-062**（D-062/D-063 全 repo 0 refs）。拍板後進 DECISIONS_LOG D-062 專屬 section（接於對話 B D-056~D-061 之後）。

## 0. 目的與觸發來源

11th master frontend dialogue cycle 處理 NEW_REQ_20 dashboard 三欄區時，F1-3a（前端顯示對齊 UX_SPEC §11.1.6 + 移除過時 mock）已落地；但 F1-3b（接 backend 真實 pending 資料）**被拆成 NEW_REQ_44**，因為 F-A3 audit 揭示：`/api/dashboard/pending-status` endpoint 要能實作，必須先定義 3 個目前不存在的資料 schema。這 3 個 schema 都落在 `09_quality_assurance/` 模板 + 協議層（可能觸及 LOCKED spec），依本專案治理慣例（D-001~D-055：定義新資料契約走 D-NNN 拍板），不能由 frontend cycle 擅自定義。

本包供 user 拍板 **D-062**。拍板前 backend endpoint 不實作；dashboard 維持目前「誠實標『待 backend』空狀態」的暫態。

**這份是「拍板包」不是「實作」**：D-062 拍板定 3 schema 形狀後，才開後續 frontend + backend 實作 task。

---

## 1. 背景（F-A3 audit 現況事實）

`_tools/frontend/server.py`（984 行）10 個現有 endpoint 中**不存在** `/api/dashboard/pending-status`。UX_SPEC §11.1.6 要求三欄區反查：左欄「待人類裁決 HD」、中欄「QA pending」、右欄「Canon Δ pending」。三欄的資料來源都缺機器可讀的 schema：

| 欄 | 要顯示什麼 | 現況缺口 |
|---|---|---|
| 左：待人類裁決 | 09_e 內待拍板項計數 + 項名 | 09_e 是純文字模板，無「待裁決 vs 已裁決」狀態標記 |
| 中：QA Pending | 哪些場景未跑完 09_a-i 全 8 類 QA | 無「完成 QA」定義；`qa_report_count()` 只計檔案數不算缺漏清單 |
| 右：Canon Δ Pending | Canon Delta 候選清單 | 無儲存位置規範、無 schema、無 lifecycle |

> 補記：frontend `state.js` 的 `dashboardData$` signal 也需加 `pendingStatus` 欄、`api.js` `fetchDashboardData()` 需並行加載此 endpoint — 但那屬「實作」，不屬本拍板（schema 定了照做即可）。

---

## 2. 待拍板的 3 個 schema

### Schema 1 — 09_e 待裁決標記（Pending Human Decision marker）

**問題：** backend 怎麼從 `09_quality_assurance/09_e_定稿變更紀錄.md` 識別「此項尚未人類拍板」？

| 選項 | 做法 | 優 | 缺 |
|---|---|---|---|
| **1A（推薦）** | 每筆 09_e 紀錄加 frontmatter / 表格欄 `decision_status: pending \| decided`（enum） | 機器可讀明確；對齊既有 frontmatter canonical schema（SPEC §5.2）；易擴充 | 需改 09_e 模板 + 既有紀錄補欄 |
| 1B | 用 HTML comment 標 `<!-- 待拍板 -->` | 對既有純文字侵入小 | 非結構化；易漏標；解析脆弱 |
| 1C | 沿用既有 TODO / INFERENCE / CONFLICT 標記反查 | 不動模板 | 語意錯位（那些是內容缺口標記，不是「人類裁決待辦」）；會誤計 |

**推薦 1A**：`decision_status` enum 欄。對齊專案既有 frontmatter 紀律，且 backend 掃描成本低（讀 frontmatter 即可）。

### Schema 2 — Canon Δ 候選儲存位置 + schema（Canon Delta candidates）

**問題：** Canon Delta 候選存哪、長什麼樣、何時標「已決」？目前 frontend 只有 placeholder，全 repo 無實際資料流。

| 選項 | 做法 | 優 | 缺 |
|---|---|---|---|
| **2A（推薦）** | 新建獨立檔 `09_quality_assurance/09_j_canon_delta候選表.md`，frontmatter + 表格（欄：`delta_id` / `source_scene` / `description` / `status: candidate\|accepted\|rejected` / `created_by` / `created_at`） | 單一權威來源；不污染 09_e；對齊 CANON_DELTA_FRAMEWORK v0.1 既有 framework | 新增一個 09_* 檔（需 user 同意，CLAUDE.md §6「不主動建無關文件」— 但此為功能必需，屬 D-062 授權範圍）|
| 2B | Canon Δ 候選內嵌在 09_e 內另一段 | 不新增檔 | 09_e 職責混淆（定稿變更 vs canon 候選是兩件事）|
| 2C | 暫不實作右欄，dashboard 右欄長期顯示 N/A | 0 成本 | NEW_REQ_20 三欄殘缺；UX_SPEC §11.1.6 不滿足 |

**推薦 2A**：獨立 `09_j` 檔。與 `_design/CANON_DELTA_FRAMEWORK.md` v0.1 對齊（該 framework 屬「成熟期功能 reference」，正好此處落地其儲存層）。**注意：** 2A 需 user 在 D-062 一併授權新建 09_j（否則撞 CLAUDE.md §6 不主動建檔規則）。

### Schema 3 — QA-pending 判定（QA completeness）

**問題：** 「某場景 QA 完成」的定義是什麼？怎麼算「缺哪些 QA type」？

| 選項 | 「完成」定義 | 優 | 缺 |
|---|---|---|---|
| **3A（推薦）** | 場景需跑齊 8 必跑類型（09_a/b/c/d/f/g/h/i；09_e 屬人類 final-gating 不計）才算完成；缺漏 = 8 集合 − 已存在報告集合 | 對齊 CLAUDE.md「8 報告必跑」+ D-043；缺漏清單明確可反查 | backend 需按 scene_id × qa_type 聚合（比現有 count 重）|
| 3B | 有任一 QA 報告即算「已開始」，只分 0 / 非0 | 實作最輕 | 不滿足「缺哪些」需求；資訊量低 |
| 3C | 自訂 per-專案必跑集合（可設定） | 彈性 | 過度設計；無當前需求支撐 |

**推薦 3A**：對齊既有「8 必跑」契約（CLAUDE.md QA 模板落地表 + D-043）。backend 把 `qa_report_count()` 升級成「按 scene × qa_type 反查缺漏集合」。

---

## 3. 影響範圍（哪些檔會動 — 拍板後才動）

| 層 | 檔 | 動作 | LOCKED? |
|---|---|---|---|
| 模板 | `09_quality_assurance/09_e_定稿變更紀錄模板.md` | 加 `decision_status` 欄（Schema 1A）| 需確認 09_e LOCKED 狀態 → D-062 授權 |
| 模板 | 新建 `09_quality_assurance/09_j_canon_delta候選表.md` | 新增（Schema 2A）| 新檔；需 D-062 一併授權（CLAUDE.md §6）|
| 協議 | `09_a-i` QA 完成定義可能需寫進 00_* 協議或 SPEC §QA 段 | 文件化「8 必跑 = 完成」（Schema 3A）| 視落點可能觸 DATA_FORMAT_SPEC / INTEGRATION_CONTRACTS |
| backend | `_tools/frontend/server.py` | 新增 `/api/dashboard/pending-status` route + QA 缺漏反查 | 非 LOCKED（frontend scope）|
| frontend | `state.js` + `api.js` + `ProjectDashboard.js` | 加 `pendingStatus` state 欄 + 並行加載 + 三欄取真實資料 | 非 LOCKED（frontend scope）|

**為什麼必須走 D-062 而非直接做：** 上表前 3 列（09_e 模板改欄 / 新建 09_j / QA 完成定義文件化）都改動 LOCKED 治理下的協議 / 模板層，定義的是新的機器可讀資料契約。本專案 D-001~D-055 慣例是這類「新資料 schema」一律 user 拍板。後 2 列（backend / frontend）是 schema 定了之後的純實作，可直接做。

---

## 4. 推薦組合（一句話）

**Schema 1A（`decision_status` enum）+ 2A（新建 09_j Canon Δ 候選表）+ 3A（8 必跑 = 完成，反查缺漏集合）**，並在 D-062 一併授權新建 09_j。三者都對齊既有契約（frontmatter 紀律 / CANON_DELTA_FRAMEWORK / D-043 8 必跑），擴充性好，backend 反查成本可控。

---

## 5. 拍板後的實作順序（D-062 → 實作）

1. **D-062 拍板**（user）→ 寫進 DECISIONS_LOG D-062 專屬 section（接於對話 B D-056~D-061 之後）
2. **schema 落地**：09_e 加欄 + 新建 09_j + QA 完成定義文件化（屬協議/模板層；對話 A 或下一 cycle）
3. **backend 實作**：server.py 加 `/api/dashboard/pending-status` + QA 缺漏反查（frontend dialogue 後續 cycle）
4. **frontend 接線**：state.js / api.js / ProjectDashboard.js 取真實三欄資料 → NEW_REQ_20 完全 RESOLVED
5. **POST_LOCK_PENDING**：NEW_REQ_44 標 RESOLVED via D-062

---

## 6. 不拍板的後果

dashboard 右/中/左三欄長期停在「誠實空狀態」placeholder（功能不殘缺但不完整）；NEW_REQ_20 停在「前端部分 RESOLVED」；NEW_REQ_44 持續 OPEN。可接受作為暫態，但 dashboard 的 QA / 裁決視角（reframe 後工具核心角色）無法發揮。

---

## 7. Cross-ref

- `_design/POST_LOCK_PENDING.md` NEW_REQ_44（backend pending-status；本包為其前置 design gate）+ NEW_REQ_20（F1-3b 拆出來源）
- `_design/AUDIT_2026Q2_REPORT.md` §9.3/§9.5（frontend cycle finding 拆分 + backend 越界防護紀錄）
- `_sandbox/audit-reports/audit-F-A3-backend-state.md`（3 schema 缺口的完整 file:line 證據）
- `_design/UX_SPEC.md` §11.1.6（三欄區規格 — 本包要滿足的目標）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（Schema 2A 的 framework 對齊來源）
- `CLAUDE.md` QA 模板落地表 + `_design/DECISIONS_LOG.md` §D-043（Schema 3A「8 必跑」契約來源）
- `_design/DECISIONS_LOG.md` §6.18 D-055（最近一筆已批 D-NNN 格式參考；D-056~D-061 為對話 B 預留候選；D-062 為本包順延後的下一個未用號）
