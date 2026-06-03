狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-17  
適用範圍：重啟設計專案的並行協調主計畫 / Master 對話 owns  
優先級：最高  

# MASTER_PLAN — 並行 specialist 設計協調主計畫

# 0. 文件目的

本文件是「master + parallel specialists」架構下的 master 文件，定義：

1. 現有設計盤點（哪些已通過 4 輪 CODEX 審查、哪些是缺口）
2. 三個 specialist 對話的明確 scope 邊界
3. master 對話保留的整合區議題
4. 迭代節奏與衝突處理機制

**閱讀對象：**
- 使用者（協調人，跨對話搬決策）
- 三個 specialist 對話的啟動 agent
- 未來重啟整合 master 對話的 agent

---

# 1. 現有設計盤點

## 1.1 已通過 4 輪 CODEX 審查的設計（穩固，不擅動）

| 範疇 | 文件 | 狀態 |
|---|---|---|
| 設計目標與決策 | `SPEC.md` | LOCKED 設計層 |
| 實作架構 | `ARCHITECTURE.md` | LOCKED 設計層 |
| 任務拆解 | `TASKS.md` | LOCKED 設計層 |
| 擷取變更紀錄 | `EXTRACTION_NOTES.md` | LOCKED 紀錄 |

**已涵蓋的議題：**
- Frontmatter canonical schema（中文 header 5 欄 + YAML block 上游 3 欄 + 下游 8 欄）
- 7 種文件狀態 + 9 種 pipeline_state + 5 種 mode_tag + 4 種 qa_decision + 5 種 qa_type
- 邏輯實體類型（W / V / C-* / R-*-* / P / CH-* / S-*-*）
- 上游 5 份協議框架（00_e / 00_f / 00_g / 00_h / 00_l）
- Bootstrap 協議（00_i）+ 迭代協議（00_j）+ 下游 pipeline 協議（00_k 框架）
- 24 個 skill + 中文別名（雙語 wrapper + smoke test）
- 6 個 REVIEW gates（A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5）
- Phase A–D 任務拆解（含 A.0 parser/helper 前置）
- 作品專屬 00_b 的 7 個 section anchors + merge 策略
- `--converge` skill contract
- `.protocol_version.phase_log` 下游追蹤欄位

## 1.2 已部分涵蓋但需細節展開

| 範疇 | 涵蓋程度 | 待 specialist 展開 |
|---|---|---|
| 上游 5 份協議內容 | 框架已定，內容未展開 | 上下游 specialist |
| 下游 00_k 內容 | 結構已定，具體流程未展開 | 上下游 specialist |
| 6 份 QA 模板（09_a/b/c/d/e/f；5 份跑 QA + 09_e 為 final-gating 紀錄） | 列表已定，內容未展開 | 上下游 specialist |
| 任務包 07_a 模板 | 既有版本，需對齊 pipeline_state | 上下游 specialist |
| `/dialogue-write` 多版本生成細節 | 概念已定，algorithm 未展開 | 上下游 specialist |

## 1.3 完全未涵蓋

| 範疇 | 缺口性質 |
|---|---|
| UI/UX 視圖層呈現 | 「使用者直白檢視資料」的方式未設計 |
| Canon delta 回寫機制 | SPEC 12.8 提到但未設計 |
| 特殊資料格式 | 未來作品可能需要的 schema 擴充（多語言 / retcon / etc.） |
| 多場景並行處理 | TASKS 提到 `--converge` 但跨場景 race 未處理 |
| Instance bootstrap 微調反向同步 | Template 升級時 Instance 怎麼跟進未設計 |

---

# 2. Specialist 對話劃分

## 2.1 上下游完整設計 specialist（取 Q1=A 路線：保守版）

**Scope（Owns）：**
- 00_e（世界觀）/ 00_f（角色）/ 00_g（大綱）/ 00_h（細綱）/ 00_l（關係）5 份協議的**內容展開**（每份協議的 10 區段共通骨架填具體規則）
- 00_k 台詞生產流程協議的**完整內容展開**
- `/dialogue-write` 的多版本試寫 algorithm 細節
- `/qa` 的 5 份報告生成細節 + 09_a–f QA 模板**內容展開**
- 09_e 定稿變更紀錄模板內容
- Canon delta 回寫機制設計（Phase D 後的成熟期功能）

**禁止越界：**
- 不改 frontmatter canonical schema（屬於資料格式 specialist）
- 不設計 UI 呈現方式（屬於 UX specialist）
- 不更動 SPEC 已通過 4 輪審查的部分（如有需要必須回報 master 裁決）

**產出：**
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
- 跨界議題清單（給 master）

## 2.2 資料格式 specialist

**Scope（Owns）：**
- 評估現有 canonical schema 的擴充需求
- 處理 references/CREATIVE_SCHEMA_PROPOSAL_FROM_HARNESS.md 提到的可吸收議題：
  - **retcon vs supersede 區分** — 是否要在 frontmatter 加新欄位
  - **多語言對白** — 如要支援雙語版本，schema 怎麼擴充
  - **continuity_check 作為一級實體** — 是否獨立為新 entity 類型
  - **scene 粒度** — exchange-level dialogue 是否要支援
  - **protected_tier** — 個人專案是否需要（看作品需求）
- 設計新增實體類型（若需要）
- 設計 Instance 特殊資料格式（user 之前提到的 #4）

**禁止越界：**
- 不設計下游 pipeline 流程
- 不設計 UI 呈現
- 不擅自更動已鎖定的 canonical schema 7+9+5+4+5 enum

**產出：**
- `_design/DATA_FORMAT_SPEC.md`
- 跨界議題清單

## 2.3 UI/UX specialist

**Scope（Owns）：**
- `/view-*`（world / character / outline / detailed-outline）的呈現格式設計
- `/export-*` 整合檔的 Markdown 結構與閱讀體驗
- `/status` 看板的視覺呈現
- 6 個 REVIEW gate 印給使用者的清單格式
- QA 報告的閱讀體驗（5 份 + 彙整版的視覺結構）
- 跨檔導航設計（如何在多個分拆檔之間移動）
- 使用者輸入錯誤時的提示格式

**Bootstrap 任務（specialist 對話啟動時）：**
- 先讀本專案 `_design/SPEC.md` 第 13 節（視圖層機制）
- **整合既有 claude-UX 對話的設計** — 使用者會提供該對話的整理稿（`_design/UX_PRIOR_DRAFT.md`）

**禁止越界：**
- 不設計下游 pipeline 流程
- 不更動 canonical schema
- 不設計 skill 觸發機制（屬於上下游 specialist）

**產出：**
- `_design/UX_SPEC.md`
- 跨界議題清單

---

# 3. Master 保留決策權的整合區

以下議題**跨多個 specialist scope**，由 master 對話裁決：

1. **新增 frontmatter 欄位**（資料格式 specialist 提案，但需確認上下游與 UX 都能處理）
2. **新增實體類型**（影響 schema + pipeline + UX）
3. **新增 pipeline_state / mode_tag enum 值**
4. **跨 specialist 衝突**
5. **既有 SPEC/ARCHITECTURE/TASKS 的修改**（4 輪審查的成果，要動需 master 確認）
6. **新增 skill**（影響 TASKS 與 UX）

---

# 4. 迭代節奏

```
Phase 1（master 起手，已在做）：
  └ 產出 MASTER_PLAN.md + INTEGRATION_CONTRACTS.md（v0）+ 3 份 SPECIALIST_STARTER
  └ 把 _clean/ 搬遷到新乾淨資料夾

Phase 2（specialist 平行第一輪）：
  └ 三個對話各自跑，產出 *_SPEC.md
  └ 每份 spec 必須含「需 master 裁決問題清單」

Phase 3（master 整合對話，新開）：
  └ 讀三份 spec + 各自的問題清單
  └ 解決衝突，更新 INTEGRATION_CONTRACTS 為 v1
  └ 回饋給 specialist 對話

Phase 4（specialist 平行第二輪，視需要）：
  └ 各自依 INTEGRATION_CONTRACTS v1 收尾

Phase 5（master 終審）：
  └ 把所有 specialist spec 整合進主 SPEC/ARCHITECTURE/TASKS
  └ 升 LOCKED
```

---

# 5. 衝突處理

**衝突類型與處理：**

| 衝突 | 處理方式 |
|---|---|
| Specialist A 提案影響 Specialist B 的 scope | A 標為「跨界議題」加入問題清單；不擅自決定 |
| Specialist 提案動到 SPEC 已鎖定部分 | 標為「需 master 裁決」，且必須附理由 |
| 兩個 specialist 同時對某議題下結論且結論不一致 | master 介入仲裁，根據 INTEGRATION_CONTRACTS 判定 owner |
| 提案違反現有 canonical schema | 拒絕，除非有強烈理由（standard 是 schema 已通過 4 輪審查） |

**升級機制：**
- Specialist 對話結束時必須交「需 master 裁決問題清單」
- 清單格式：`議題 | 涉及 scope | 提案方向 | 等待裁決原因`

---

# 6. 完成標準

**全專案設計階段完成 = 以下全部成立：**

1. 三份 specialist spec 已通過 master 整合（無 outstanding 衝突）
2. INTEGRATION_CONTRACTS 升 v1（含全部 specialist 完成後的真實介面）
3. 主 SPEC/ARCHITECTURE/TASKS 已整合 specialist 產出
4. `_design/` 目錄結構乾淨，無散落的草稿
5. 可以進 Phase A.0 實作（如尚未開始）或繼續 Phase A.0+（如已開始）

---

# 7. 給協調人（使用者）的提醒

1. 每個 specialist 對話結束時，**檢查是否有「需 master 裁決問題清單」**。沒有清單代表 specialist 可能擅自越界，要警惕。
2. 不要把同一個議題同時丟給兩個 specialist 對話 — 一定會 conflict。
3. INTEGRATION_CONTRACTS 是活的 — 隨 specialist 進展更新版本（v0 → v1 → ...）。
4. 如果某 specialist 對話卡住或要做大改動，先暫停其他 specialist，回到 master 對話評估影響。
5. 三個 specialist 對話**不必同時啟動**。建議順序：資料格式 → 上下游 → UX（後者依賴前兩者的結論）。
