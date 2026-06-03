狀態：DRAFT
版本：v0.3（Phase A.0F master 平行對話完成 + CODEX audit-doc 對齊修補）
最後更新：2026-05-22
適用範圍：HTML web UI 前端工具 — 11 feature + Asset Panel + Export Panel + 整合驗收
優先級：高
歷史：v0.2 → v0.3（audit-doc — C1 SceneQueue facet 對照表 / C2 SceneDetail 改 MVP 標 / C3 Asset Panel 分母 single source / C4 Glossary 13 vs 40 註明）

# 05 前端工具

> **v0.2 (2026-05-22) — Phase A.0F master 平行對話完成**：11 feature 全部 land + 38 unit test + 2 stage A integration test PASS。
> 詳見 feature branch `frontend-tools-a0f`（7 commit）；本檔同步補完整內容。

# 1. 啟動

```bash
cd D:/劇本開發工具/_tools/frontend
pip install -r requirements.txt
python server.py --port 8765
```

開瀏覽器到 `http://localhost:8765`。

設計：**本地 server，只 bind 127.0.0.1，外部不可達**。

入口頁：直接到 Project Dashboard (`#/`)；也可從 `#/home` 開 Workspace Home 看主要入口卡片。

---

# 2. 11 feature 完成度（v0.2 — Phase A.0F 完成）

對應 REQUIREMENTS_LOCK §5 + UX_SPEC §11。

| Feature | UX 對應 | A.0F 對應 | 狀態 | 主檔 |
|---|---|---|---|---|
| **F1 Project Dashboard** | §11.1 | A.0F.2 | ✅ FINAL | `static/js/components/ProjectDashboard.js` |
| **F2 Scene Queue** | §11.2.1 + §11.4 facet | A.0F.3 + A.0F.4 | ✅ FINAL | `static/js/pages/SceneQueue.js` |
| **F2 Scene Detail (cockpit)** | §11.2.2-§11.2.12 | A.0F.3 | ✅ **MVP** — cockpit 骨架 + Quick Actions + LOCKED 守門入口完成；**Required Context 6 子分區 / Beat Preview / QA Findings full modal 仍為 placeholder**（待 backend 反查 API — [BLOCKED:UPSTREAM_DOWNSTREAM]） | `static/js/pages/SceneDetail.js` |
| **F3 Scene Editor 三欄並排** | §11.3 | A.0F.6 | ✅ FINAL (details pane / Required Context 抽屜 留後續) | `static/js/pages/SceneEditor.js` |
| **F6 搜尋 + 篩選 facet** | §11.4 | A.0F.4 | ✅ FINAL (6 維 facet + fuzzy search; mode_tag/characters 維待 backend 擴) | `static/js/pages/SceneQueue.js` |
| **F7 直接編輯 + LOCKED 守門 + Save race guard** | §11.5 | A.0F.7 | ✅ FINAL | `static/js/pages/SceneEditor.js` |
| **多分頁 + mtime 衝突** | §11.7 | A.0F.8 | ✅ FINAL (二選 modal: reload / 強制覆寫) | `static/js/pages/SceneEditor.js` |
| **A-\* Asset Panel** | §11.1.6a | A.0F.11 | ✅ FINAL (7 subtype + 缺檔警示 UPS-UX-70) | `static/js/components/ProjectDashboard.js` |
| **🌟 L3 Export Panel** | §11.6.11 + L3_EXPORT_PROMPT_SCHEMA v0.2 | A.0F.10 | ✅ FINAL (核心；含 prompt 生成器 + 28 unit test) | `static/js/pages/ExportPanel.js` + `components/promptAssembler.js` |
| **CopyCommandButton 通用元件** | §11.6 | A.0F.5 | ✅ FINAL (D-029 α 完全分離核心元件) | `static/js/components/CopyCommandButton.js` |
| **Workspace Home / Glossary / Theme** | §11.9 | A.0F.9 | ✅ FINAL (Harness 屬 prototype 拒絕類 §4.3, 不補) | `static/js/pages/WorkspaceHome.js` + `pages/Glossary.js` |

---

# 3. F1 Project Dashboard

7 段順序（依 §11.1.1）：HERO Next Actions → HERO Blockers → 場景就緒度 → 模組狀態 → 三欄區 → A-\* Asset Panel → 模組導航 → Footer。

頁首 actions：🏠 Home / 📖 Glossary / 切換明暗 / 手動 refresh。

**A-\* Asset Panel（§11.1.6a，D-044 + D-045）**：
- 7 subtype 卡片（portrait / bg / cg / sfx / bgm / voice / ui）
- 每卡四桶 ✓◐○✗ + 覆蓋率 + hasMissing ⚠ 警示框
- 整體 % + 缺檔總數 badge
- 對齊 D-045：獨立於 narrative 完成度

---

# 4. F2 Scene Queue + Scene Detail

## 4.1 Scene Queue (`#/scene-queue`)

- 頁首 controls + 7 維 facet 控制列 + chapter group + scene card grid
- **6 維 facet 可用**：Chapter / Pipeline State / Task Status (multi-select OR) + Has Dialogue / Has QA / Has LOCKED Version (tri-state)
- 全文 fuzzy search (scene_id / chapter / pipeline_state / task_path / task_status)
- localStorage `scene-queue-facets-v1` persisted state
- 篩選結果批次 export：CopyCommandButton 複製批次 `/qa <id1>,<id2>,...` (前 20 場)
- 每張 scene card 顯示：scene_id / pipeline_state badge / 任務包狀態 / dialogue 版本數 / QA 報告數 / 實體數 / 最後修改 / Next Fix 簡易推導

## 4.2 Scene Detail cockpit (`#/scene/<id>`)

read-only 雙欄（D-035）：
- **Main**：Scene Readiness Panel + Required Context 6 子分區 + Beat Preview + Dialogue Draft Preview + QA Findings 摘要
- **Side (sticky)**：Active QA findings + Active HD/Canon Δ + Quick Actions（LOCKED 守門 + 多個 CopyCommandButton + 進入編輯入口）

**LOCKED 守門入口**（§11.5.2 + §11.5.3 v0.3）：
- DRAFT/REVIEW → 直接跳 Editor
- LOCKED → 顯示降級引導 + 複製 Z2 candidate α 引導文字
- DEPRECATED → 跳 Editor + 顯示 warning banner
- 未啟動 → 顯示「跑 /dialogue-write 起首版」CopyCommandButton

---

# 5. F3 Scene Editor 三欄並排 (`#/scene/<id>/edit`)

依 §11.3，**唯一進入路徑**：從 Scene Detail Quick Actions「進入編輯」按鈕跳。

## 5.1 layout

```
頁首 breadcrumb + version badge + [← 返回] + [💾 Save 全部]
─────────────────────────────────────────────────────────────
N 欄並排 (v01A / v01B / v01C / v02 自適應):
┌────────┬────────┬────────┬────────┐
│ v01A   │ v01B   │ v01C   │ v02    │ ← 視覺區隔: trial 藍邊 / convergence 綠邊
│ DRAFT  │ DRAFT  │ DRAFT  │ FINAL  │
│ mtime  │ mtime  │ mtime  │ mtime  │
│ [📋QA] │ [📋QA] │ [📋QA] │ [📋QA] │
│┌──────┐│┌──────┐│┌──────┐│┌──────┐│
││edit  │││edit  │││edit  │││edit  ││ ← textarea, monospace,
││...   │││...   │││...   │││...   ││   whitespace-pre, 行級 i18n KEY
│└──────┘│└──────┘│└──────┘│└──────┘│
└────────┴────────┴────────┴────────┘
─────────────────────────────────────────────────────────────
sticky bottom: ● Dirty: v01A / v01B  [💾 Save 全部 (2)]
```

## 5.2 鍵盤快捷鍵

- `Ctrl/Cmd-S` = Save 全部（觸發 Diff Preview Modal）
- `Esc` = 關 modal（dirty 守門 / Diff Preview / LOCKED race / mtime conflict 任一）

## 5.3 Save 流程（§11.5.8 D-040 5 步）

```
1. User 點「💾 Save 全部」
   ↓
2. 跳 Diff Preview Modal（§11.3.8）— 每個 dirty version 顯示 line-by-line +/-
   ↓
3. User 點「確認寫回」
   ↓
4. 前端對每個 dirty version 送 POST /api/scene/<id>/save (含 mtime_baseline)
   ↓
5. server.py 內建 race guard:
   - 若最新 狀態=LOCKED → 409 + LOCKED_OVERWRITE_DENIED → 跳 LOCKED race modal (§11.5.8.2)
   - 若 mtime 不符 → 409 + MTIME_DRIFT + server_content → 跳 mtime conflict modal (§11.7.6)
   - 否則寫檔 + 200 → dirty 清除
   ↓
6. Save 後留 Editor (Q4 / D-035 §5.3) — 不自動跳回 Scene Detail
```

## 5.4 LOCKED race modal（§11.5.8.2，D-040 三選項）

當 Step 5 偵測最新狀態升 LOCKED，跳 modal：

- **(A) 📋 複製降級指令** → buildDowngradeGuide() 組 §11.5.3 v0.3 引導文字（純 09_e 紀錄 + frontmatter 只改狀態一行，不擅自加 schema 不認的欄位 — D-046 #5 / C-16 / O-03）
- **(B) 💾 另存為 DRAFT proposal** → saveSceneAs() 含 D-042 base_dialogue + iteration_note，寫新檔 `vN_proposal_<timestamp>.md` (DRAFT 狀態)
- **(C) 取消** — 編輯留前端 state，可手動 copy 出去

## 5.5 mtime conflict modal（§11.7.6，二選不混用 LOCKED race）

- **Reload** — 棄改、重抓 baseline
- **強制覆寫** — fetchSceneHeader 重抓 mtime → 用新 baseline 重 saveScene

跟 LOCKED race 分開原因：state machine 守則 ≠ 內容衝突。LOCKED race 禁止 overwrite；mtime drift 容許 overwrite。

## 5.6 離開時 dirty 守門（§11.5.6）

點「← 返回」如有 dirty → confirm dialog 三選：儲存後返回 / 捨棄變更返回 / 取消（留 Editor）。

---

# 6. F6 搜尋 + 篩選

詳見 §4.1 Scene Queue。

## 6.1 ⚠ 實作 facet 維度 vs UX_SPEC §11.4.3 命名 7 維對照

**重要 disclosure**：實作的 6 facet 跟 spec §11.4.3 命名的 7 維**只有 2 維 1:1 對齊**。
其他 5 維屬 [BLOCKED:UPSTREAM_DOWNSTREAM]（需 backend 反查 API 才能落地），
我用前端可直接從 `/api/scenes` summary 推導的替代維度填位。

| spec §11.4.3 命名 7 維 | 實作對應 | 狀態 |
|---|---|---|
| Chapter | `chapters` (multi-select OR) | ✅ 1:1 對齊 |
| Pipeline State | `pipelineStates` (multi-select OR) | ✅ 1:1 對齊 |
| Mode Tag (DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / SINGLE_ITER 等) | ❌ 未實作 | 待 backend 暴露每場 dialogue mode_tag 反查 API |
| Stage (Authoring / Trial / QA / Final) | ❌ 未實作 | 待 backend 提供 stage 反查 |
| QA Type (09_a~i 各 type 是否跑過) | ❌ 未實作 | 待 backend 開放 D-027 qa_type 動態 registry |
| Readiness (✓全綠 / ~部分 / ⚠卡點 / ✗未啟動) | ❌ 未實作 | 對齊 §11.2.3 完整 readiness 規則後實作 |
| Characters (出場 C-*) | ❌ 未實作 | 待 backend 提供 entities 反查 |
| **(前端推導替代維度)** | `taskStatuses` / `hasDialogue` / `hasQa` / `hasLocked` | ✅ 實作 — 從 `/api/scenes` summary 直接推導，不需 backend 擴充 |

**為什麼這樣處置（v0.2 設計理由）**：
- spec §11.4.3 列的 7 維有 5 維需要 backend 提供反查 API，但本輪 backend 只新增 1 個 endpoint (`/api/scenes`)，沒擴 entities/mode_tag/stage/qa_type 反查
- 為了讓 facet 區「立刻有用」，挑了 4 個可從 summary 直接推的維度替代，讓 user 至少能依「任務包狀態 / 有沒有 dialogue / 有沒有 QA / 有沒有 LOCKED 版」篩選
- spec 5 維留待 A.0F 後續或 Phase D Wave 13 `/view-*` 整合時補（backend 擴反查 API 後實作）

---

# 7. F7 編輯 + LOCKED 守門

詳見 §5。

---

# 8. A-\* Asset Panel

詳見 §3 Dashboard 內，§11.1.6a 完整 7 subtype 落地。

---

# 9. 🌟 L3 Export Panel (`#/export`)

**核心 feature**（user 標）— 對齊 `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 + D-038 A1 prompt 流程 + ARCH §4.2a。

## 9.1 UI

```
┌──── Layer 3 Bundle Export — schema v1.0 ─────────┐
│ 範圍：⦿ 全部 / ○ 僅大綱 / ○ 僅本場景 / ○ 僅本章節 │
│ 格式：☑ JSON  ☑ MD  ☐ 含已刪除 KEY (include_deleted) │
│ 路徑：自訂 toggle (default: export/YYYY-MM-DD_<scope>.{}) │
│ 推送方式：⦿ Clipboard / ○ POST 到本地 LLM endpoint  │
│         (Claude/OpenAI API: disabled in panel, Phase C+) │
│ 📊 stats: { entities, dialogue_lines, art_assets, qa_reports } │
│ [👁 預覽 Prompt]  [📋 複製 Prompt]  [📤 推送到 endpoint]    │
└──────────────────────────────────────────────────────┘
```

## 9.2 Prompt schema（嚴格 contract）

必填 5 區塊（依 L3_EXPORT_PROMPT_SCHEMA §1.1）：
1. **標題**：`# Layer 3 Export Task — <project_id> — YYYY-MM-DD HH:MM`
2. **YAML 元資料**：`schema_version: "1.0"` + `project_id` + `repo_root` + `timestamp` + `scope` + `formats` + `include_deleted` + `output_paths` + `mode: "read_only"` + `contract_refs`
3. **執行步驟**：標準 5 步
4. **約束規則**：read_only / output 限定 / 禁 skill / **不修改 phase_log**（CC-07）/ 不升狀態 / 不刪檔
5. **完成回報**：JSON 含 output_paths + records_total + records_by_type + entities_scanned + warnings + runtime_seconds + export_id

**CC-07 校正內化**：
- ❌ 無 `rerun_qa` 欄（跟 read_only 衝突）
- ✓ 新增 `include_deleted`（預設 false）
- ✓ 約束含「不修改 phase_log，不寫入任何 phase_log entry」

## 9.3 Push mode lifecycle（對齊 L3_EXPORT_PROMPT_SCHEMA §4）

| Mode | Phase | 狀態 |
|---|---|---|
| clipboard | Phase A.0 必做 | ✅ 已落地 |
| local_llm_endpoint (URL + Bearer + model + 30s timeout) | Phase B 後必做 | ✅ 已落地 |
| claude_api | Phase C+ 選做 | ⏳ disabled in panel |
| openai_api | Phase C+ 選做 | ⏳ disabled in panel |

localStorage `export-panel-state-v1` 持久化（**Bearer Auth token 不存**）。

## 9.4 Schema contract 驗收

`_tools/frontend/tests/prompt_assembler.test.mjs` 28 個 unit test：
- 5 區塊存在 + 順序 + YAML schema 必填 key
- CC-07 校正全條款
- 4 scope 變體含必填驗證 + 各自 step 文案
- formats 至少一 / output_paths 預設規約 / contract_refs / completion report 10 必填欄

跑法：`node _tools/frontend/tests/prompt_assembler.test.mjs`

---

# 10. CopyCommandButton 通用元件（§11.6）

D-029 α 完全分離核心元件 — 整個前端不執行 agent，所有 agent action 都走「複製指令」按鈕到剪貼簿。

## 10.1 API

```js
import { renderCopyCommandButton } from "./components/CopyCommandButton.js";

renderCopyCommandButton({
  command: "/dialogue-write S-01-03",        // 必填
  contextSummary: "W-rules 14/27\nC-主角A REVIEW",
  contextRefs: ["/01_world/...", "/03_characters/..."],
  contextNotes: "本場 v01A trial 後預期單一 iter convergence。",
  source: "Scene Detail S-01-03 / Quick Actions",
  targetAgent: "claude-code" | "cowork" | "codex" | "any",
  variant: "primary" | "secondary" | "ghost",
  size: "sm" | "md" | "lg",
})
```

全 app 用 `installCopyCommandDelegate(document)` 全域 delegated click handler 捕捉。

## 10.2 剪貼簿格式（§11.6.3）

```
─── [前端工具產生] ───
指令：
  /dialogue-write S-01-03

已有 Context 摘要：
- W-rules 14/27
- C-主角A REVIEW

相關檔案引用：
- /01_world/01_a_世界觀總覽.md
- /03_characters/main/主角A_聲線卡.md

備註：
本場 v01A trial 後預期單一 iter convergence。

來源：
  前端工具 / Scene Detail S-01-03 / Quick Actions / 2026-05-22 14:32
─── /[前端工具產生] ───
```

10 unit test 對齊：`_tools/frontend/tests/copy_command_button.test.mjs`

---

# 11. 整合驗收 / Integration smoke test

`_tools/frontend/tests/test_endpoints_smoke.py` — 兩階段：

## 11.1 Stage A — stdlib AST endpoint inventory（沙箱可跑）

純 stdlib：parse server.py AST，verify 9 endpoint 都定義了 + 檢測 truncation。

## 11.2 Stage B — FastAPI TestClient（需 `pip install -r requirements.txt`）

In-process call 全 endpoint：
- `/api/scope-counts` full + 拒絕 invalid scope
- `/api/assets?scope=all` + subtype filter
- `/api/scenes` + chapter filter
- 4 個 404 path（不存在的 scene_id / asset_id / KEY）
- POST `/api/scene/<id>/save` 缺 body → 4xx

跑法：

```bash
cd _tools/frontend
pip install -r requirements.txt
python tests/test_endpoints_smoke.py
```

預期：Stage A 2/2 PASS + Stage B 11/11 PASS（host 端）；沙箱只能跑 Stage A。

## 11.3 JS unit test

```bash
node _tools/frontend/tests/copy_command_button.test.mjs   # 10/10 PASS
node _tools/frontend/tests/prompt_assembler.test.mjs       # 28/28 PASS
```

---

# 12. Backend API endpoint 列表

對齊 ARCH §13.2 + A.0F.3 自加：

| # | Method | Path | 用途 |
|---|---|---|---|
| 1 | GET | `/api/scene/<id>/header` | 取單一場景 header + mtime |
| 2 | POST | `/api/scene/<id>/save` | 寫回（含 D-040 LOCKED race + mtime drift 偵測） |
| 3 | POST | `/api/scene/<id>/save-as` | 另存 DRAFT proposal（D-042 base_dialogue + iteration_note） |
| 4 | GET | `/api/scenes/<id>/versions` | 取所有版本 |
| 5 | GET | `/api/scenes/<id>/keys/<key>/lines` | 跨版本 KEY 行對照 |
| 6 | GET | `/api/assets?scope=...` | all / scene/&lt;id&gt; / subtype/&lt;name&gt; |
| 7 | GET | `/api/assets/<id>/usage` | 反查 KEY usage |
| 8 | GET | `/api/scope-counts?scope=...` | full / scene/&lt;id&gt; / chapter/&lt;ch&gt; (給 L3 prompt stats) |
| 9 | GET | `/api/scenes?chapter=...` | **A.0F.3 自加** — list 所有 S-* 場景 summary |

---

# 13. 路由總覽

| Route | 頁面 |
|---|---|
| `#/` 或 `#/dashboard` | F1 Project Dashboard |
| `#/home` | Workspace Home |
| `#/scene-queue` | F2 + F6 Scene Queue + facet |
| `#/scene/<id>` | F2 Scene Detail cockpit |
| `#/scene/<id>/edit` | F3 + F7 Scene Editor + Save race guard |
| `#/export` | 🌟 L3 Export Panel |
| `#/glossary` | Glossary 詞彙頁 |

---

# 14. localStorage 持久化 keys

| Key | 用途 |
|---|---|
| `dashboard-theme` | light / dark 主題 |
| `scene-queue-facets-v1` | F6 facet state（chapter / pipeline / task / has-*）+ search |
| `export-panel-state-v1` | Export panel form state（**Bearer Auth token 不存**） |

---

# 15. 對齊 D-NNN 拍板（內化清單）

| D-NNN | 落地處 |
|---|---|
| D-027 | F6 qa_type facet 動態讀（本輪先固定 6 維；qa_type 待 backend registry 擴） |
| D-028 | mode_tag 6 種 / SINGLE_ITER 入 Glossary |
| D-029 (α) | CopyCommandButton 通用元件 — 完全分離 |
| D-035 | Scene Detail (read-only cockpit) + Scene Editor 雙頁面 |
| D-037 | dialogue_keys.<KEY>.portrait/bgm/sfx Map shape — Asset Panel 覆蓋率反查 |
| D-038 | L3 Export A1 prompt 流程 — 前端產 prompt + clipboard/POST |
| D-040 | Save flow 5 步 LOCKED race guard + Step 3 pre-flight |
| D-041 | 10_art_assets/ source of truth — Asset Panel 連結 |
| D-042 | base_dialogue + iteration_note 欄位 — save-as 用 |
| D-044 | A-* 7 subtype canonical — Asset Panel + Glossary |
| D-045 | A-* 不納入 narrative /status — Asset Panel 明示獨立 |
| D-046 #5 | LOCKED 降級走 09_e 紀錄，不擅自加 frontmatter 欄位 |
| L3 schema v0.2 + CC-07 | promptAssembler.js 嚴格內化 + 28 unit test |
| SPEC §16 | 文件狀態機 — 前端 race guard 守人類控狀態原則 |
| §1.4.3 G1/G2/G3 | 全頁對齊（badge 不單獨 / 流程僅閱讀順序 / grouping 非資料層必要） |

---

# 15a. Glossary 詞庫（補充）

**Disclosure**：`static/assets/glossary.json` 目前含 40 個 term，
比 UX_SPEC §11.9.3 起點 13 詞多 27 個補充詞彙。spec 明示「未來可擴」放行此擴展。

| 來源 | 數量 |
|---|---|
| spec §11.9.3 v0.2 起點 13 詞 | 13 |
| 補充：實體類型 (W-rules / W-language / V / C-\* / R-\*-\* / P / CH-\* / S-\* / A-\*) | 9 |
| 補充：Mode Tag 6 種 (D-028) | 6 |
| 補充：QA 模板 9 個 (09_a-i) | 9 |
| 補充：設計守則 / D-NNN 拍板 | 8 |
| **合計** | **45**（部分重疊；實際 unique terms 40） |

如需精簡回 spec 13 詞起點，可刪除 `glossary.json` 中對應 categories。

---

# 16. 已知限制（後續可擴）

- **Required Context 6 子分區** (§11.2.4) — placeholder；待 backend 反查 API (W-rules / 角色聲線卡 / 跨場 query 等) [BLOCKED:UPSTREAM_DOWNSTREAM]
- **Beat Preview** (§11.2.7) — placeholder；待 06_detailed_outline scene anchor 反查
- **QA Finding full modal** (§11.2.10) — 數量摘要 placeholder；待 backend 09_quality_assurance/ finding parser
- **行級 details pane** (§11.3.5) — 未落地；後續可加（行首 🔑 icon → 右側 panel）
- **Required Context 抽屜** (§11.3.6) — 未落地；後續可加（Editor 左側 toggle）
- **i18n KEY label per segment in diff** (§11.3.8) — Diff Preview Modal placeholder；待 i18n table 串接 [NEEDS_SCHEMA_SUPPORT]
- **mode_tag / Characters facet** (§11.4) — 待 backend dialogue mode_tag 讀取 + entities 反查 API 擴
- **Harness** (§11.9) — 屬 prototype 拒絕類 §4.3，本輪不補
- **qa_type 動態 facet** — 待 backend registry dynamic fetch
