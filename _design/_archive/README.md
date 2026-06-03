狀態：DRAFT
版本：v1.0（設計文件凍結歸檔 — 2026-06-02；自 _design/ 根目錄移入 130 份純歷史過程紀錄，依賴分析 + 對抗式 QA workflow 雙重驗證後執行）
最後更新：2026-06-02
適用範圍：_design/_archive/ 歸檔索引 — 說明哪些設計文件被凍結、為何安全、未來如何撈用
優先級：一般

# _design/_archive/ 歸檔索引

> 本目錄存放 **純歷史過程紀錄**：開發到今天為止累積的 task starter、review report、舊輪交接包、早期規劃、被取代的草稿、里程碑報告。它們對「實際使用工具」沒有作用，但保留供「未來迭代或修復時撈文件」。
>
> **凍結原則**：這裡的檔不再更新、不被 runtime 引用。需要查歷史脈絡時來這裡找；正式權威內容請看 `_design/` 根目錄的現役規格與追蹤檔。

## 為什麼這些檔可以安全歸檔（驗證紀錄）

歸檔前做了兩層驗證：

1. **依賴分析**：grep 全 repo，確認這 130 檔**沒有任何一個**被 runtime 檔（`.claude/skills/**`、`AGENTS.md`、`CLAUDE.md`、`_user_manual/**`、`scripts/**`、`00_protocol/**`）或內容資料夾（`01_world`–`10_art_assets`、`台詞/`）以路徑依賴方式引用。殘存的提及都是現役文件內的「文字敘述」，不影響工具運作。
2. **對抗式 QA workflow**（6 並行驗證 agent + 綜合）：逐分類複查引用、狀態 header、內容唯一性。其結論為——這 130 檔的可行動內容已全部沉澱進現役的 `DECISIONS_LOG.md` / `POST_LOCK_PENDING.md` / `HANDOFF_TO_11TH_MASTER.md` / `TASKS.md`。

### QA 從原歸檔名單中「撤回」的檔（仍留在原地，未歸檔）

- `_design/refactor_reference/UI_UX_SPEC.md`、`_design/refactor_reference/narrative_workspace_prototype_v2.1.html` — LOCKED `UX_SPEC.md` §11.0.2 以完整路徑指其為前端章節「細節層權威」，屬現役引用。
- `_design/STYLE_ANCHOR_PROPOSAL.md` — 現役 `01_world/01_d` 指其為文風內容 source-of-truth。
- `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` — 翻譯工具 fork 的活躍未來計畫（HANDOFF_TO_11TH / POST_LOCK_PENDING NEW_REQ_11 待辦依據）。

## 目錄結構

| 子目錄 | 數量 | 內容 |
|---|---|---|
| `codex_rounds/` | 100 | 全部 `CODEX_*`：各 wave 的 task starter 與 review report（裁決結論已入 DECISIONS_LOG）|
| `handoffs/` | 9 | 第 4–10 輪 master 交接包 + 9th master 續接包 ×2（已被 HANDOFF_TO_11TH 接續）|
| `planning_superseded/` | 11 | 早期規劃（MASTER_PLAN、GAP_ANALYSIS、REVISED_WORK_ITEMS、3 份 SPECIALIST_STARTER）+ 被正式版取代的草稿（UX_PRIOR_DRAFT、UX_PROTOTYPE_ANALYSIS、INTEGRATION_CONTRACTS_v2_SKELETON、STAGE_7 checklist、UPSTREAM_DOWNSTREAM_SPEC.md.bak.round1）|
| `milestone_logs/` | 9 | PHASE_3/A/B 完成報告（PHASE_3 狀態 LOCKED，經 user 明確同意歸檔）、tier_1 報告、4 份 review log、wrapper smoke test |
| `style_anchor_impl/` | 1 | STYLE_ANCHOR_IMPL_STARTER.md（狀態 APPLIED，施工已完成）|

**合計 130 檔。**

## 已知無害副作用

- 部分現役文件（如 `DECISIONS_LOG.md`）內文會以文字提到這些檔名。歸檔後那些只是「文字提及」，仍可閱讀，不影響工具；未逐一改寫上百處歷史引用（風險高且無必要）。
- 被移動的 CODEX 檔內含對舊式檔名的引用，這些屬 `check_paths.py` 既有 baseline debt（NEW_REQ_9），歸檔前後 ERROR 總數不變（225 / 1），本次移動**未新增任何錯誤**。

## 如何撈用

直接瀏覽對應子目錄即可；git 歷史完整保留（用 `git mv` 搬移）。若未來迭代需要回溯某輪設計理由，先查 `DECISIONS_LOG.md`，再來此處找對應 `CODEX_*` 或 `HANDOFF_*` 原始紀錄。
