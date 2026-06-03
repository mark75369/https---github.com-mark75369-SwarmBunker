狀態：LOCKED
版本：v0.2（master 第四輪 pre-LOCKED CC-07 校正完成 + CODEX (d2) PASS）
最後更新：2026-05-19
適用範圍：L3 export 觸發 prompt 的 canonical schema（D-038 A1 流程 + CC-07 純 read-only 細化：rerun_qa 移除 + include_deleted 補 + phase_log 不 append）
優先級：高

# L3_EXPORT_PROMPT_SCHEMA — Layer 3 Export Prompt 規範

# 0. 文件目的

定義 L3 export 觸發 prompt 的鎖定形狀，作為前端與外部 agent（Claude Code / CODEX APP / 未來本地 LLM）之間的 contract。

**為什麼需要 schema：**
- D-038 拍板 export 走「前端產 prompt → 使用者貼到 CC/CODEX → agent 跑」(A1 模式)
- prompt 本身就是介面 — 任何能讀 prompt 的 LLM endpoint 都能接
- 未來自動推送（POST 到本地 LLM endpoint / Claude API / OpenAI API）要靠 prompt schema 穩定
- 沒有 schema = 介面 fluctuates = 接 LLM 一次破一次

**設計原則：**
- prompt 是 contract，不是隨手寫人看的指令
- 結構固定、欄位明確、未來機器可解析
- agent 收到 prompt 後行為可預測（read-only / 寫到 export/ / 強制路徑）

---

# 1. Prompt canonical 結構

## 1.1 必填區塊（依序）

| 區塊 | 必填 | 內容 |
|---|---|---|
| 1. 標題行 | ✅ | `# Layer 3 Export Task — <project_id> — <YYYY-MM-DD HH:MM>` |
| 2. 元資料區（YAML block） | ✅ | repo_root / scope / formats / output_paths / mode |
| 3. 執行步驟 | ✅ | 編號 1~N 的步驟清單 |
| 4. 約束規則 | ✅ | read-only / 禁止改 source / 路徑限制 |
| 5. 完成回報格式 | ✅ | agent 應該回報什麼（路徑、size、records 數） |

## 1.2 元資料 YAML block 完整 schema

```yaml
---
schema_version: "1.0"
project_id: "game-dialogue-bible"
repo_root: "D:\\劇本開發工具"
timestamp: "2026-05-19T14:32:00+08:00"

scope:
  type: "full" | "outline_only" | "scene"
  scene_id: "CH01_S03"  # 僅 type=scene 時填，否則 null
  entity_filter:  # optional
    types: ["W-rules", "C-*", "S-*"]  # 包含的 entity 類型
    exclude: ["A-*"]  # 排除類型

formats:
  json: true
  md: true
  # v0.2 master 第四輪 CC-07 校正：rerun_qa 欄位移除
  # 理由：read-only mode 禁止執行 /qa（§1.4 constraints）；rerun_qa 屬 pipeline action 跟 read-only 衝突
  # 若需重跑 QA，user 切外部 chat 跑 /qa skill 後再 export

include_deleted: false  # v0.2 新增 via CC-07 — 是否含 status: deleted 的 dialogue_line（預設 false；export 預設不含）

output_paths:
  json: "export/2026-05-19_full.json"
  md: "export/2026-05-19_full.md"

mode: "read_only"  # 鎖死

contract_refs:
  data_format_spec: "_design/DATA_FORMAT_SPEC.md §9"
  upstream_downstream_spec: "_design/UPSTREAM_DOWNSTREAM_SPEC.md §12"
---
```

## 1.3 執行步驟 — 標準 5 步驟（agent 必須照走）

```
1. 讀 contract_refs 中指向的 DATA_FORMAT_SPEC §9（manifest + records[] schema）。
2. 依 scope 掃描 repo_root 下所有相關 entity 檔（W-rules/W-language/W-style/V/C/R/P/CH/S/A/ORG — 鏡像；型別權威見 entity_type_registry，full 以「所有 entity」為準）。
   - scope.type=full：所有 entity（含 W-style `01_d` / ORG `11_organizations/`）
   - scope.type=outline_only：W-rules + W-language + V + C-* + R-*-* + P + CH-*
   - scope.type=scene：僅該 scene_id 與其 depends_on
3. 依 §9.2 寫 manifest header（entity_type_registry / qa_type_registry snapshot + scope + counts）。
4. 依 §9.3-§9.6 將每筆轉為 records[]：
   - frontmatter → record fields
   - 內文（保留段落結構）→ record.body
   - dialogue 檔的 dialogue_keys block 完整保留
5. 寫 JSON 到 output_paths.json；同時寫 MD 雙吐到 output_paths.md（消費端易讀版）。
6. 完成回報（見 §1.5）。
```

## 1.4 約束規則（read-only mode 強制；v0.2 對齊 CC-07）

```
[CONSTRAINTS — strict, do not violate]
- read_only: true → 不得改動任何 source entity 檔（W/V/C/R/P/CH/S/A-* 全 read-only）
- output_paths 限定 repo_root/export/ 下，不可寫到其他目錄
- 不執行任何 /create-* /dialogue-write /qa /scene-task 等 skill
- **不修改 phase_log，不寫入任何 phase_log entry**（v0.2 CC-07 校正 — export 不 append `phase: export` 紀錄；Layer 3 Export 純 read-only，不視為 pipeline event）
- 不升級任何狀態
- 不刪除任何檔案（即使是過期 export 也不動）
- 若遇到無法讀的檔（loop / permission），記入 export warnings，不阻塞整體
- mode != "read_only" 的 prompt 一律拒跑（檢查到 mode 不是 read_only 就 return error）
- 已有 status: deleted 的 dialogue_line：預設**不**含於 JSON records[]；只有當 `include_deleted: true` 時才含（§1.2 schema 對應欄位）
```

## 1.5 完成回報格式（agent 應該回報什麼）

```
[COMPLETION REPORT — 必須包含]
- output_paths.json 的絕對路徑與檔案大小（bytes）
- output_paths.md 的絕對路徑與檔案大小
- records[] 總筆數 + 各 record_type 分布（entity: N1, dialogue_line: N2, ...）
- 掃描到的 entity 總數
- warnings 清單（含路徑 + 原因）
- 整體運行時間（agent 自報）
- manifest.export_id（agent 生成的 UUID）
```

---

# 2. 前端 UI 對應規範

## 2.1 Export panel 必要元件

```
┌─────────────────────────────────────────────────┐
│ Layer 3 Bundle Export                            │
├─────────────────────────────────────────────────┤
│ 範圍：   ⦿ 全部                                  │
│          ○ 僅大綱                                │
│          ○ 僅本場景  [CH01_S03 ▼]               │
│                                                  │
│ 格式：   ☑ JSON  ☑ MD  ☐ 含已刪除 KEY            │
│                                                  │
│ 路徑：   export/2026-05-19_full.{json,md}        │
│          [改路徑...]                             │
│                                                  │
│ 推送方式：                                       │
│          ⦿ 複製到 clipboard（預設）              │
│          ○ POST 到本地 LLM endpoint              │
│              URL: [____________________]         │
│              Auth: [Bearer __________]           │
│              Model: [llama3.1-70b____]           │
│              [測試連線]                          │
│          ○ POST 到 Claude API (TODO)             │
│          ○ POST 到 OpenAI API (TODO)             │
│                                                  │
│ [預覽 Prompt]  [複製 / 推送]                     │
└─────────────────────────────────────────────────┘
```

## 2.2 預覽 Prompt 行為

點「預覽 Prompt」彈出 modal，內容是依使用者選項組裝出的完整 prompt（§1.1 5 區塊全顯示）。讓使用者在貼出前能審視。

## 2.3 複製 / 推送行為

| 推送方式 | 點按鈕後行為 |
|---|---|
| clipboard | 把 prompt 全文寫到 clipboard；顯示 toast「已複製，請貼到 Claude Code / CODEX APP」 |
| POST endpoint | fetch POST 到 user 設的 URL；payload 為 prompt 全文 + format=json；等回應或顯示「已推送（無回應）」 |

---

# 3. 對接的 spec / D-NNN

| 項 | 對接點 |
|---|---|
| D-038 | 本檔是 D-038 附帶第 1 項的具體實作 |
| DATA_FORMAT_SPEC §9 | manifest + records[] JSON schema 來源 |
| UPSTREAM_DOWNSTREAM_SPEC §12 | export skill / CLI 入口（v0.8 起改為「複製 Export Prompt」按鈕，不新增 skill） |
| UX_SPEC §11 (F4 / F6 export panel) | 前端 Export panel UI 規範 |

---

# 4. 推送方式 lifecycle（未來開發路線）

| 階段 | 推送方式 | 狀態 |
|---|---|---|
| Phase A.0 | clipboard | 必做 |
| Phase B 後 | POST 到本地 LLM endpoint（Ollama / vLLM / 自架） | 必做（D-038 附帶第 2 項） |
| Phase C+ | POST 到 Claude API / OpenAI API（含 auth + retry） | 選做 |
| 未來 | webhook / 觸發 GitHub Action | 待議 |

每階段都必須維持 prompt schema v1.0 兼容 — schema 不破壞，只能加新欄位（schema_version: "1.1" / "2.0" 視變動類型）。

---

# 5. 文件維護紀律

- 本檔是 prompt contract，不是教學文件
- 改 prompt 結構必須升 schema_version
- 推送方式擴充不算 schema 變動（屬 UI 設定）
- 任何破壞性變動須走 master 裁決（D-NNN 紀錄）
