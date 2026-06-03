狀態：DRAFT
版本：v0.1
最後更新：2026-05-17
適用範圍：擷取變更紀錄 / CODEX 審查參考
優先級：高

# EXTRACTION_NOTES — 乾淨擷取變更紀錄

本文件記錄從原 `C:\Users\001\game-dialogue-bible\` 擷取到 `_clean/` 的變更，供 CODEX 審查時參考。

原資料夾保持原狀不動，所有變更只發生在 `_clean/` 子目錄。

---

# 1. 擷取範圍總覽

原資料夾的內容分三類：

| 類別 | 處理 | 範圍 |
|---|---|---|
| 純台詞聖經內容 | 完整複製到 `_clean/` | 00 ~ 09 模板、archive 歷史補丁 |
| meta 文件（含 HARNESS 污染） | 微調後複製 | AGENTS.md、README.md |
| 工具腳本（含 HARNESS 污染） | 清整後複製 | scripts/check_paths.py、scripts/check_headers.py |
| 純 HARNESS 工具污染 | 完全不複製 | _coordination/、_docs/、_reports/、_prototypes/、scripts/ 其餘檔案 |
| 作品專屬內容 | 暫存為 reference 素材 | 00_b 反 AI 味檢查表（蟲潮孤堡專案版） |

---

# 2. 完整複製清單（30 份）

完全沒有修改，直接從原資料夾複製：

```
_clean/00_protocol/00_a_台詞生產協議.md
_clean/00_protocol/00_c_台詞輸出格式.md
_clean/00_protocol/00_d_工作流總覽.md
_clean/01_world/01_a_世界觀總覽.md
_clean/01_world/01_b_世界語言規格.md
_clean/01_world/01_c_陣營與階級語言.md
_clean/02_vocabulary/02_a_專有名詞表.md
_clean/02_vocabulary/02_b_俗稱與黑話表.md
_clean/02_vocabulary/02_c_禁用詞與慎用詞表.md
_clean/03_characters/03_a_角色總表.md
_clean/03_characters/03_b_主要角色聲線卡模板.md
_clean/03_characters/03_c_次要角色與npc模板.md
_clean/04_relationships/04_a_角色關係矩陣.md
_clean/04_relationships/04_b_關係變化時間線.md
_clean/05_plot/05_a_主線大綱模板.md
_clean/05_plot/05_b_章節結構模板.md
_clean/05_plot/05_c_角色弧線表.md
_clean/05_plot/05_d_資訊揭露表.md
_clean/05_plot/05_e_伏筆與回收表.md
_clean/06_scene_index/06_a_場景索引模板.md
_clean/07_scene_tasks/07_a_單場台詞任務包模板.md
_clean/08_dialogue_outputs/08_a_台詞版本管理規範.md
_clean/08_dialogue_outputs/08_b_生成台詞檔案模板.md
_clean/09_quality_assurance/09_a_ai味qa報告模板.md
_clean/09_quality_assurance/09_b_角色聲線一致性檢查模板.md
_clean/09_quality_assurance/09_c_禁用詞檢查報告模板.md
_clean/09_quality_assurance/09_d_資訊控制檢查報告模板.md
_clean/09_quality_assurance/09_e_定稿變更紀錄模板.md
_clean/archive/00_protocol_模式系統公版補丁_v_0_2.md
_clean/_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md
```

---

# 3. 微調文件清單

## 3.1 AGENTS.md

**變更：**

1. 整段移除「Harness 架構參考」（原第 8–12 行）— 該段指向 `_docs/harness_usage_order_and_agent_mvp_plan.md`，屬於 HARNESS 工具開發資料污染。
2. 「禁止修改區域」（原第 60–67 行）改為更通用的描述：
   - 原：列出 `00_protocol/`、`01_world/` 中 LOCKED 文件、`03_characters/main/` 中 LOCKED 聲線卡、`05_plot/` 中 LOCKED 資訊揭露表、`archive/`
   - 改：「任何狀態為 LOCKED 的文件」「`00_protocol/` 中的協議文件（屬於通用骨架）」「`archive/`」

**其餘內容（台詞品質規則、禁止傾向、文件頭格式、修改流程）原樣保留。**

## 3.2 README.md

**變更：**

1. 移除原第 11 行：「本 repo 也是 Narrative Dialogue Production Harness…」整段及指向 `_docs/harness_usage_order_and_agent_mvp_plan.md` 的連結。
2. 更新版本標記：`0.1` → `0.2-clean`、更新日期：`2026-05-17`。
3. 新增「目前狀態」區段，說明 `_clean/` 是 Template 乾淨擷取版、提示 `_design/` 三份設計文件即將補入。
4. 更新「資料夾結構」與「模板導航」：
   - 標註 `00_b` 為「通用骨架待建」（Phase A 由 CODEX 從專案版反推）
   - 標註 `00_e`–`00_h`、`00_i`、`00_j` 為待建（依 Phase 分配）
   - 標註 `09_f 類型偏移檢查模板` 為待建（Phase D）
   - 移除 `Baseline 摘要` 中具體模板數量描述（Phase A 後再更新）

## 3.3 scripts/check_paths.py

**變更：**

1. 從 `IGNORE_DIR_NAMES` 移除：`_projects`、`tasks`、`_logs`、`_source_materials`（HARNESS 概念）
2. 從 `ACTIVE_DIRS` 移除：`_docs`（HARNESS 概念），新增：`_design`
3. 從 `FUTURE_PREFIXES` 移除：`tasks/`、`_logs/`、`_source_materials/`，改為 `_design/`
4. 從 `HISTORICAL_PREFIXES` 移除：`_reports/`（HARNESS 概念）
5. 從 `ACTIVE_PREFIXES` 移除：`_docs/`，新增：`_design/`
6. `PATH_RE` 簡化，移除 `_docs|tasks|_logs|_source_materials` 引用
7. 移除 `check_stale_labels` 函式（綁定 HARNESS `_docs/` 的「待建」標記檢查）
8. Header docstring 與註解全面中文化、加入 clean 版本說明
9. **核心邏輯（舊式檔名偵測、路徑存在性檢查）保留**

## 3.4 scripts/check_headers.py

**變更：**

1. 移除 `DOC_PATTERNS`（HARNESS 概念）
2. 移除 `TRIO_DOCS`、`OTHER_DOCS` 集合（HARNESS 特定的 docs 文件清單）
3. 移除 `is_doc_high_severity` 函式（綁定上面被移除的集合）
4. `TEMPLATE_PATTERNS` 新增 `_design/*.md`
5. `TEMPLATE_DIR_PREFIXES` 新增 `_design/`
6. `VERSION_RE` 放寬以接受 `0.2-clean` 這類後綴格式
7. Header docstring 與註解全面中文化、加入 clean 版本說明
8. **核心邏輯（5 欄位完整性檢查、格式驗證、INFO summary）保留**

---

# 4. 暫存的 Reference 素材

## 4.1 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`

**來源：** 原 `00_protocol/00_b_反ai味檢查表.md`（DRAFT v0.2，已專案化到《蟲潮孤堡》）

**用途：** 供 CODEX 在 Phase A 從這份專案版反推出「通用骨架版本」`00_protocol/00_b_反ai味檢查表.md`。

**規格要求：**
- Template repo 應保留**結構骨架**（檢查表分類、QA 報告格式、模式差異表等）
- **不得保留任何作品專屬內容**（不得提及《蟲潮孤堡》、黑翼、蟲災、瑟琳、莉娜、諾拉等）
- 作品專屬內容是 Instance repo 的責任（00_e 世界觀協議跑完後，會把作品專屬偏移風險、高風險詞、角色偏移清單寫回 Instance 的 `00_b`）

**Phase D 最後一步：** 把這份蟲潮孤堡專案版搬到 Instance repo（`蟲潮孤堡-dialogue-bible`）的 `00_protocol/00_b_反ai味檢查表.md`。

---

# 5. 完全未複製（污染歸檔在原資料夾）

以下內容**完全沒有複製到 `_clean/`**，永遠保留在原 `C:\Users\001\game-dialogue-bible\` 作為歷史備份：

```
_coordination/        整個資料夾（HARNESS workflow notes、task packets、runner results 等 60+ 份檔案）
_docs/                整個資料夾（5 份 HARNESS 文件）：
                      - harness_usage_order_and_agent_mvp_plan.md
                      - game_dialogue_bible_handoff_and_implementation_plan.md
                      - gpt_interaction_handoff_preferences_for_game_dialogue_bible.md
                      - gpt_handoff_full_context_for_game_dialogue_bible.md
                      - api_usage_logging_spec.md
                      - harness_architecture.md
                      - agent_roles.md
                      - mvp_workflow.md
_reports/             整個資料夾（HARNESS readiness audit、baseline audit）
_prototypes/          整個資料夾（HARNESS UI 原型 narrative_workspace）
scripts/ 其餘檔案     ~20 個 workflow_*.py、claude_task_helper.py、codex_inbox_helper.py、
                      partial_read_validator_v1.py 等
```

---

# 6. 後續流程

`_clean/` 目錄是 Template repo 的乾淨擷取基底。後續流程：

1. 我將在 `_clean/_design/` 寫入三份核心設計文件：`SPEC.md`、`ARCHITECTURE.md`、`TASKS.md`
2. 使用者把 `_clean/` 整個目錄推上 GitHub 成為 Template repo
3. CODEX 依 `TASKS.md` 從 Phase A 開始實作
4. Phase D 最後一步：建立 Instance repo（《蟲潮孤堡》）並把 `references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md` 搬過去

---

# 7. 給 CODEX 審查者的提醒

- 請確認 `_clean/` 內所有檔案**沒有殘留 HARNESS 概念**（如 `harness`、`_coordination`、`workflow_runner`、`task_packet`、`narrative_workspace`、`_docs trio` 等）
- 請確認 `AGENTS.md`、`README.md` 的微調沒有破壞既有規範
- 請確認 `scripts/` 內兩支腳本仍可正常執行（語法、imports 正常）
- 請確認 `archive/00_protocol_模式系統公版補丁_v_0_2.md` 確實是 APPLIED 狀態的歷史紀錄（不需再套用）
- 如果發現任何遺漏的污染或不該保留的內容，請列出後請使用者裁決
