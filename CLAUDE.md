狀態：DRAFT
版本：v0.7（11th master frontend 過夜自主長跑 — F8 Phase 3 / D-074：skill 索引表 B 上游加 /create-org（建立組織）+ D 迭代加 /iterate-org；補 agent-discovery 索引 drift（最終稽核 MAJOR）；本檔 v0.6 → v0.7）
歷史紀錄：v0.6（11th master frontend Batch 4 — F10 / NEW_REQ_34 via D-072：新增「副對話 / Sub-conversation 慣例」短指標段，8 條規則精簡列 + 指回 ARCH §3.3.3 權威全文；本檔 v0.5 → v0.6）；v0.5（F14 context-budget 瘦身 — 完整 skill 清單 / 版本落地狀態 / QA 模板表 / Phase 里程碑 / 相關 spec 清單移出至 `_user_manual/skill_registry_full.md`；本檔僅保留核心規則 + 精簡 skill 索引；本檔 v0.4 → v0.5）；v0.4（10th master Phase D Wave 13/14/15 metadata partial supersede）；v0.2 → v0.3（9th master Round 1 NO-GO inline patch）；v0.1 → v0.2（9th master cleanup queue — Phase B/C skill TBD → ✅ 已實作）
最後更新：2026-06-02
適用範圍：Claude Code CLI / Anthropic ecosystem agent discovery
優先級：高

# CLAUDE.md

## 專案目的

本 repo 是商業級長篇遊戲劇本與台詞製作資料庫。
所有 AI 操作必須以維護劇本一致性、角色聲線、資訊揭露順序、台詞品質為目標。

## 最高優先級規則

1. LOCKED 文件高於聊天紀錄。
2. DEPRECATED 文件不得引用，除非任務明確要求。
3. 不得擅自改動 LOCKED 文件。
4. 若需要修改 LOCKED 文件，必須先提出變更理由與影響範圍。
5. 所有新增 .md 文件必須包含文件頭。
6. 本 repo 是劇本與台詞資料庫，不是一般軟體專案；不得主動建立 LICENSE、schema.md、database-config 等無關文件。

## 文件頭格式

每份 .md 文件必須包含中文 header 5 必填欄位：

狀態：DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED
版本：
最後更新：
適用範圍：
優先級：

**狀態作用範圍：**
- 全域：DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED
- `archive/` 補丁專用：APPLIED
- `view/` 整合檔專用：DERIVED

需要實體追蹤的檔案，header 後另加 YAML block 標記 `entities` / `depends_on` / `weight`（詳見 SPEC 第 5.2 節 Frontmatter Canonical Schema）。協議檔（00_*）可省略 YAML block。

## 素材區（`_source_materials/`）

`_source_materials/` 是 user 原始輸入素材區（人設、既有劇本台詞、世界觀筆記等），供 `/create-*` 等 skill 讀取參考，本質不屬於任一模組產物、不是實體。其下 `.md` 素材檔**不需** 5 欄 header（唯一例外為該目錄的 `README.md`），且被所有 frontmatter 掃描器排除、不計入實體進度、不報 header 缺漏。非 `.md` 素材（`.docx` / `.txt` / `.csv` / `.json`）本就不被掃描。

## 審核迴圈（四層防線）

對本 repo 的工具 / `_design` / 協議檔做任何 Batch 修改，必跑四層防線：
L0 執行 → L1 外部審（獨立 agent 查內容錯）→ L2 自動檢查（`check_paths` / `check_headers` / `git status` 查機械錯）→ L3 人工確認（master 真抽查後簽字）。
四層不可跳、L1 必須由與 L0 不同的 agent 執行、L3 簽字只有真抽查才有效。
完整判準、Batch 狀態機、landing record 格式見 `_design/REVIEW_LOOP_PROTOCOL.md`。

## 副對話 / Sub-conversation 慣例

消化大量既有素材（既有劇本 / docx / 長人設）時可另開**副對話**只做讀取萃取，主對話保留 skill 階段推進。8 條規則（權威全文見 `_design/ARCHITECTURE.md` §3.3.3）：

1. 副對話只讀不寫；一切寫檔只能由主對話經 SKILL.md 階段執行。
2. 明列實際讀過的檔（含 docx / txt / csv / json）。
3. 明列沒讀到 / 讀不全的部分（環境不支援 / 抽樣 / 解析失敗）。
4. 只回 evidence 摘要，不把 raw material 整段貼回主對話（保護 context）。
5. skill stage 由主對話持有推進；副對話不代寫、不代拍板。
6. **不主動關閉副對話，除非 user 明示可收。**
7. 同一 ingestion 任務 reuse 既有副對話，不每次另開重讀。
8. 主對話用明確 wording 標示分工與生命週期（範例見 ARCH §3.3.3）。

## Skill 清單（精簡索引）

本 repo 含 `.claude/skills/<name>/SKILL.md` 自訂 skill 集合。Claude Code CLI 自動 discovery `.claude/skills/`；user 可直接用 slash command 觸發已實作 skill；對應的中文 wrapper 觸發時以英文主檔為權威。

**完整 path 表、各 skill 版本與落地狀態、QA 模板清單、Phase 里程碑、相關 spec 清單 → 按需讀取 `_user_manual/skill_registry_full.md`（不必每次對話載入）。**

| Phase | Slash command（中文 wrapper） |
|---|---|
| A 整備 | `/init-project`（初始化專案）、`/create-world`（建立世界觀）、`/status`（進度）、`/check-gaps`（缺漏檢查） |
| B 上游 | `/create-character`（建立角色）、`/create-relationship`（建立關係）、`/create-org`（建立組織）、`/create-outline`（建立大綱）、`/create-detailed-outline`（建立細綱） |
| C 下游 | `/scene-task`（場景任務包）、`/dialogue-write`（生成台詞）、`/qa`（檢查） |
| D 視圖 | `/view-world` `/view-character` `/view-outline` `/view-detailed-outline`（查看＊） |
| D 迭代 | `/iterate-world` `/iterate-character` `/iterate-relationship` `/iterate-org` `/iterate-outline` `/iterate-detailed-outline` `/iterate-scene`（迭代＊） |
| D 匯出 | `/export-world` `/export-character` `/export-outline` `/export-detailed-outline`（匯出＊） |
| D+ 輔助 | `/diagnose`（診斷）、`/integrate`（整理） |

若 slash command 對應的 SKILL.md 尚未存在，agent 必須停止並回報「尚未實作」，不得用本檔摘要或 user manual 骨架替代正式 SKILL.md。
