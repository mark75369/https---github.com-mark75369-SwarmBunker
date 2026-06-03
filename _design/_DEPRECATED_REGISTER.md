狀態：FINAL
版本：v1.0（Batch 6 技術債清掃 — 封存登記：把已 applied / superseded 的規劃·交接·稽核·設計包文件標 DEPRECATED 的索引）
最後更新：2026-06-03
適用範圍：_design/ 已封存（DEPRECATED）文件的單一索引；給「這份文件還算數嗎？」的快速判定
優先級：中

# _DEPRECATED_REGISTER — 已封存設計文件索引

> **用途：** 下列文件已 **applied / superseded**，狀態欄已改 `DEPRECATED`。依 CLAUDE.md「DEPRECATED 文件不得引用，除非任務明確要求」——**它們只存歷史，不得當活躍指引**。權威活躍紀錄請看各列指向的帳本 / 程式碼。
>
> **封存方式（Batch 6 判定）：** 採**原地標 DEPRECATED**（非實體移檔）。理由：這些文件被 `DECISIONS_LOG` / `POST_LOCK_PENDING` 等活躍帳本以歷史 cross-ref 大量引用，實體移走會破壞引用（check_paths ERROR）並違反本 repo「不刪歷史」紀律；DEPRECATED 狀態即本 repo 定義的封存語意，已足夠。

## 1. 本次過夜鏈（F8 Phase 3 + 稽核 + Batch 5）產出的 applied 文件

| 文件 | 性質 | 活躍紀錄在哪 |
|---|---|---|
| `OVERNIGHT_RUN_F8P3_AUDIT_BATCH5.md` | 過夜自主執行計畫（已執行完） | git log / 本 register |
| `OVERNIGHT_WAKEUP_REPORT.md` | wake-up 報告 + 決策佇列 + L3 包（L3 已簽、已 merge） | DECISIONS_LOG §6.25-§6.27 |
| `QA_HANDOFF_F8P3_BATCH5.md` | 獨立 QA 交接包（QA 已複驗 GO） | DECISIONS_LOG / 本 register |
| `BATCH4_POSTLAND_AUDIT.md` | 稽核啟動文件（workflow 已跑） | BATCH4_POSTLAND_AUDIT_REPORT（亦 DEPRECATED） |
| `BATCH4_POSTLAND_AUDIT_REPORT.md` | Step 2 稽核報告（findings 已修） | DECISIONS_LOG / 程式碼 |
| `FINAL_AUDIT_REPORT_F8P3_BATCH5.md` | Step 4 最終稽核報告（findings 已修） | DECISIONS_LOG / 程式碼 |
| `D074_DECISION_PACKAGE.md` | F8 Phase 3 設計包 + §13 七題（已拍板落地） | **DECISIONS_LOG §6.25 D-074 + §6.27 amendment** |
| `BATCH5_REGISTRY_DRY_REFACTOR.md` | Batch 5 重構交付文件（已執行） | **DECISIONS_LOG §6.26 D-075** / POST_LOCK NEW_REQ_49 |
| `HANDOFF_F8_PHASE3_AND_REGISTRY_DRY.md` | F8 Phase 3 + Batch 5 冷啟動交接（已消化） | 本 register |
| `BATCH4_RESUME_PHASE4-7_AUTONOMOUS.md` | ⚠ **編號已作廢**（Phase 4-7 併入 Phase 3；Step 0 reconcile） | DECISIONS_LOG §6.25.1（reconcile 紀錄） |

## 2. 更早期已消化的交接 / 設計包

| 文件 | 性質 | 活躍紀錄在哪 |
|---|---|---|
| `D071_DECISION_PACKAGE.md` | F8 Phase 1 ORG core 設計包（已拍板落地） | DECISIONS_LOG §6.23 D-071 |
| `HANDOFF_11TH_PARALLEL_SETUP.md` | 11+ 輪並行模式 setup（已自述廢止） | — |
| `HANDOFF_TO_11TH_MASTER.md` | 第十一輪 master 接手包（已消化） | — |
| `HANDOFF_BATCH1_IMPL_SESSION.md` | Batch 1 實作交接（已消化） | — |
| `HANDOFF_BATCH2_BATCH4_PARALLEL.md` | Batch 2/4 並行交接（已消化） | DECISIONS_LOG §6.20-§6.23 |
| `FRONTEND_HANDOFF.md` | 前端 cycle 交接（已消化） | POST_LOCK §5.22 |

## 3. 刻意**未**封存（仍 live / 有參考價值，勿誤刪）

| 文件 | 狀態 | 為什麼留 |
|---|---|---|
| `PROPOSAL_TRANSLATION_TOOL_FORK.md` | DRAFT（保留） | 翻譯工具 fork = **NEW_REQ_11 DEFERRED 未來提案**，尚待啟動條件，非無效 |
| `SANDBOX_REFACTOR_PLAN.md` | DRAFT（保留） | workflow/audit 方法論 + sandbox bootstrap 指引，仍有 reference 價值 |
| `STYLE_ANCHOR_PROPOSAL.md` | DRAFT（保留） | D-055 STYLE_ANCHOR 的 acceptance criteria / RFC，仍可回查 |
| 活躍帳本/規格（DECISIONS_LOG / POST_LOCK_PENDING / REVIEW_LOOP_PROTOCOL / expected_entities / 10 份 LOCKED spec / TASKS / SPEC / ARCHITECTURE …） | LOCKED/FINAL/DRAFT | 工具活躍權威，**非封存對象** |

## 4. Cross-ref
- 封存判定 + 本 register：Batch 6 技術債清掃（feat/batch6-techdebt-archive）
- 活躍決策帳本：`DECISIONS_LOG.md`（v2.10）/ `POST_LOCK_PENDING.md`（v0.37）
