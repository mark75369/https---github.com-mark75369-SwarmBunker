狀態：DRAFT  
版本：v2.0-skeleton  
最後更新：2026-05-19  
適用範圍：三 specialist v0.3 patch 完成後的 Contract A/B/C 真實形狀骨架，給第四輪整合 master 對話填內容用  
優先級：最高

# INTEGRATION_CONTRACTS v2 SKELETON — Contract A/B/C 真實介面骨架

# 0. 文件目的

本檔是 **INTEGRATION_CONTRACTS v0 → v2 升級的「骨架佔位」版**，給第四輪整合 master 對話接手時直接填內容用。

v0 版本是「設計初期、specialist 還沒交付」時的契約佔位；v2 是「三 specialist v0.3 patch 完成 + CODEX (c) 審查 + master 第四輪 P0/P1 拍板」後的真實介面。

**為什麼用骨架不寫完：**
- 三 patch 雖然交付，但有 12 條 UD §9 / UX §10 Pending 議題 + DF §12.4 18 項機械落地工作 尚未跨 spec 對齊
- 主 SPEC / ARCHITECTURE / TASKS 升級時會發現「兩個 specialist 對同一介面有不同寫法」的細節
- 骨架先佔位，內容由下個 master 對話對齊三 spec v0.3 後填

**閱讀對象：**
1. **第四輪整合 master 對話的 agent**（主消費者）
2. 未來重啟整合的 master 對話

---

# 1. 三 spec v0.3 patch 後的 Contract 概述

```
┌─────────────────────────────────────────────────────────────┐
│ Contract A：DF ↔ UD（資料形狀 ↔ 上下游消費）                  │
├─────────────────────────────────────────────────────────────┤
│ A.1  dialogue_keys Map shape（D-037）                        │
│ A.2  phase_log 8 欄位 schema（D-042 + DF-2 基礎 2 + DF-3）   │
│ A.3  A-* metadata 7 subtype + 個別 metadata files（D-041/D-044）│
│ A.4  i18n KEY status enum + alias mapping（D-037）            │
│ A.5  qa_type 8 種 + extensible registry（D-043）             │
│ A.6  mode_tag SINGLE_ITER + base_dialogue lineage（D-042）   │
│ A.7  JSON `manifest + records[]` source of truth（D-039）    │
│ A.8  trust-level 限上游 /create-* 範圍（C-08）               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Contract B：UD ↔ UX（上下游邏輯 ↔ 前端呈現）                  │
├─────────────────────────────────────────────────────────────┤
│ B.1  UX-1~UX-80 標記覆蓋（D-046 #1+#2）                      │
│ B.2  Save race guard for LOCKED（D-040）                     │
│ B.3  Export Prompt panel UI（D-038 + L3_EXPORT_PROMPT_SCHEMA）│
│ B.4  Asset Panel for A-* 獨立顯示（D-045）                   │
│ B.5  8 QA execution order UI 對齊（D-043）                   │
│ B.6  KEY status enum dropdown（D-037）                       │
│ B.7  trust-level 上游 import 路徑 UI（C-08）                 │
│ B.8  Conflict modal for entity 命名衝突（D-033 + D-046 #5）  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Contract C：DF ↔ UX（資料形狀 ↔ 前端呈現）                    │
├─────────────────────────────────────────────────────────────┤
│ C.1  A-* subtype 7 種 → UI dropdown / chip（D-044）           │
│ C.2  KEY status enum → UI dropdown / badge（D-037）          │
│ C.3  JSON export `manifest + records[]` → 前端不消費（D-038 A1）│
│ C.4  phase_log new fields → /status & details pane（D-042）  │
│ C.5  A-* completeness → asset panel only, 不入 narrative status（D-045）│
└─────────────────────────────────────────────────────────────┘
```

---

# 2. Contract A 詳細（給 master 填）

## 2.1 A.1 dialogue_keys Map shape

**Schema 來源：** DF `_design/DATA_FORMAT_SPEC.md` §4.2（v0.2）

**Map 形式：**
```yaml
dialogue_keys:
  <KEY>:
    line_index: int
    speaker: <entity_id | null>
    aliases: [<KEY history list>]
    portrait: <A-portrait-* | null>
    bgm: <A-bgm-* | null>
    sfx: [<A-sfx-* list>]
    status: active | deprecated | deleted
    created_at: date
    renamed_at: date | null
    deleted_at: date | null
    deprecated_reason: str | null
```

**UD 消費端對齊：** §11 cross-ref / §2.11 i18n KEY writing 都已用 mapping `dialogue_keys.<KEY>.*`。✓

**UX 消費端對齊：** §11.3.5 details pane / §11.1.6a Asset Panel 都已對齊。✓

**[FILL-IN]** 跨 spec 全文搜尋是否仍有 list-of-objects 殘留 → 待 master 整合驗證

## 2.2 A.2 phase_log 8 欄位 schema

**完整欄位（DF §3）：**
- `pipeline_state` (DF-1 基礎)
- `mode_tag` (DF-1 基礎)
- `status` (DF-2.1)
- `import_source` (DF-2.2)
- `entities_touched` (DF-2.3，D-042)
- `iteration_count` (DF-2.4，D-042)
- `iteration_note` (DF-2.5，D-042)
- `base_dialogue` (DF-2.6，D-042)
- `conflict_resolutions` (DF-2.7，D-042)

**[FILL-IN]** 主 SPEC §5.4 phase_log sub-schema 是否補完 → master 整合時動

## 2.3 A.3 A-* metadata source of truth

**結構：** `10_art_assets/<subtype>/<A-id>.md` 個別 metadata file（**無**統一 registry.yaml）

**Subtype 7 種（D-044）：** portrait / bg / cg / sfx / bgm / voice / ui
**Reserved（未來擴充）：** icon / effect / video / shader

**[FILL-IN]** A-* metadata 內 frontmatter schema 完整定義 → master 從 DF §5.3 拷貝

## 2.4 ~ 2.8 略（同樣 pattern — 待 master 填）

---

# 3. Contract B 詳細（給 master 填）

## 3.1 B.1 UX-1~UX-80 覆蓋

**UX_SPEC §7.8（UX-1~53）+ §7.9（UX-54~80）= 80 個 [UX] 標記全覆蓋。**

**[FILL-IN]** 待 master 拷貝完整對照表 → 從 UX §7.9 抓進來，作為 frontend 開發 backlog

## 3.2 B.2 Save race guard

**位置：** UX §11.5.7~11.5.9

**5 步流程：**
1. user 按 Save
2. 前端 fetch 最新 file header
3. **Step 3 必行：if 最新 `狀態=LOCKED` → 進入 race guard 對話框（三選項：複製降級指令 / 另存 DRAFT proposal / 取消）**
4. else → 正常 Save
5. Save 後刷新

**[FILL-IN]** 待對齊 D-040 + 主 ARCHITECTURE frontend handler

## 3.3 B.3 Export Prompt panel

**位置：** UX §11.6.11；對齊 `_design/L3_EXPORT_PROMPT_SCHEMA.md` §2

**UI 元件：** 範圍選擇 / 格式選擇 / 路徑 / 推送方式 / 預覽 prompt modal / 複製/推送按鈕

**推送方式 lifecycle：**
- 今天：clipboard 預設
- Phase B+：POST 到本地 LLM endpoint
- Phase C+：POST 到 Claude API / OpenAI API
- 未來：webhook / GitHub Action

**[FILL-IN]** 主 TASKS 是否新增 phase A.0 之外的 frontend integration tasks → 由整合 master 對話判定

## 3.4 ~ 3.8 略（同樣 pattern）

---

# 4. Contract C 詳細（給 master 填）

略 — 同樣 pattern，待 master 填

---

# 5. Master 第四輪整合對話的工作清單

## 5.1 升 INTEGRATION_CONTRACTS v0 → v2（基於本骨架填內容）

每個 Contract 條目都標 `[FILL-IN]` → master 對話需逐條填，產出真實 v2 文件。

## 5.2 升主 SPEC

依 DF §12.4 18 項機械落地工作 + UD §9 RESOLVED 5 條 + UX §10 對應對照表，把以下段落升級：

- SPEC §5.1：A-* entity + 預留 user_extensions（已部分由 D-024 + D-044 動）
- SPEC §5.2.3：`mode_tag` 5→6 + SINGLE_ITER 行為定義
- SPEC §5.2.4：`qa_type` 5→8 + extensible registry
- SPEC §5.4：phase_log sub-schema 補 5 新欄位（D-042）
- SPEC §12：QA pipeline 5→8 + 09_e final-gating（D-043）
- SPEC §13 / §14：L3 export A1 流程（D-038）；既有 4 個 `/export-*` 不擴充
- SPEC §16：LOCKED → DEPRECATED 降級流程（無 frontmatter 三欄位，走 09_e）

## 5.3 升主 ARCHITECTURE

- A.0 parser 9 大類處理項（DF §11）
- Frontend adapter 8 個 API endpoint（從 UX NS-1~33 Query-API 類抽取）
- Export prompt 生成器（前端內嵌，無 server）

## 5.4 升主 TASKS

- A.0 9 項 parser tasks 對應 DF §11
- 新 A.5 init-project 用 entity_type_registry / qa_type_registry Template
- C.5 export prompt 生成（前端 only）
- D.4 QA pipeline 5→8 改寫
- 前端工具任務群（F1 / F2 / F3 / F6 / F7 + Export panel + Asset panel）

## 5.5 升 PHASE_3_COMPLETION_REPORT v4.0 為 FINAL

包含完整 Phase 3 設計收斂統計 + 進 Phase A.0 準備度評估。

## 5.6 觸發 CODEX (d) 短審查（可選但建議）

範圍只看 Contract A/B/C v2 是否收斂 + SPEC/ARCH/TASKS 一致性。預估 CODEX 1-2 小時。

## 5.7 升 LOCKED + 開 Phase A.0

最後一個關卡：所有設計檔升 LOCKED + DECISIONS_LOG 升 v1.0 + 開 Phase A.0 第一個 parser task。

---

# 6. 跨 spec 仍 Pending 議題彙整（給 master 排程）

## 6.1 DF Pending（從 §12 master TBD 抽出）

DF 本輪宣稱 0 master TBD。但 §12.4 列了 18 項機械落地工作（不算 TBD 但要做）。

## 6.2 UD Pending（§9，12 條）

| Pending | 優先級 | 對齊 |
|---|---|---|
| 9.1.1 P-009（08_a §11.1 patch） | 高 | CODEX tier 2 寫 |
| 9.1.3 P-011（canon delta） | 低 / 成熟期 | Phase D+ |
| 9.1.5 P-013（LOCKED retcon） | 中 | 對齊 D-040 後再議 |
| 9.1.7 P-015（file mutex） | 中 | A.0 parser 後 |
| 9.2.1 v0.2-A 00_q 實檔 | — | CODEX tier 2 邊界 |
| 9.2.2 v0.2-B 00_p 實檔 | — | CODEX tier 2 邊界 |
| 9.2.4 v0.2-D 衝突 merge UI | — | [TBD-UX-CONFIRM] |
| 9.2.5 v0.2-E §2.10.3 19 vs 20 欄 | 低 | master 整合對齊 |
| 9.3.1 高風險場景 enum | 中 | 對齊 09_h |
| 9.3.2 D.3.5 路徑 B 後處理 | 高 | 對齊 D-043 |
| 9.3.3 05_b 章節空殼 weight | 低 |  |
| 9.3.4 00_b anchors 擴充 | 低 |  |
| 9.3.5 下游 pipeline 解讀權威 | 中 | 對齊 D-039 |

## 6.3 UX Pending（§9 NS 三分類）

- Schema 類 11 RESOLVED / 11 PARTIAL
- Query-API-Adapter 類 9 條（屬 parser service / frontend adapter）
- Algorithm 類 2 條

加上 NS-NEW-1（09_e schema）— 待 UD §3.6.3 / §3.6.6 細化後回填。

## 6.4 Master 整合對話原生的議題

| Pending | 說明 |
|---|---|
| P-027 ~ P-030 | DECISIONS_LOG §6.6.5 仍 Pending（UX 細節 / canon delta / glossary / multi-medium future） |
| 版本號統一 | DF v0.2 = UD/UX v0.3 — 不是 bug，但下個 master 對話要對應好 |

---

# 7. 給第四輪整合 master 對話的提醒

1. 本骨架是「結構保證」，不是「內容保證」 — 每個 `[FILL-IN]` 都要動手填
2. 三 spec v0.3 是「pattern lock」狀態 — 不要回頭改 spec，只把結論搬進主 SPEC / ARCH / TASKS
3. 若發現主 SPEC partial supersede 涉及 LOCKED 段，先暫停，找 user 拍板
4. CODEX tier 2（寫 00_protocol / 09_qa 實檔）的事不在你 scope — 屬 Phase A.0 之後
5. INTEGRATION_CONTRACTS v2 是活的 — 寫完後若主 SPEC 升級發現新衝突，回來修
