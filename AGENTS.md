# AGENTS.md

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

## 台詞品質規則

1. 不直接說出角色心理總結。
2. 不使用主題宣言式台詞。
3. 不讓角色替玩家整理劇情。
4. 不把潛台詞寫成明台詞。
5. 不用抽象詞代替具體行動。
6. 每句台詞至少有一個功能：攻擊、防禦、試探、隱瞞、命令、拒絕、確認、拖延、誤導、安撫。
7. 主要角色必須遵守角色聲線卡。
8. 場景必須有開始狀態與結束狀態。
9. 若一段台詞刪掉三分之一仍不影響理解，應壓縮。

## 禁止傾向

避免：
- 命運
- 羈絆
- 守護
- 真正重要的是
- 我終於明白
- 這不只是A，更是B
- 不是A，而是B
- 我不想再逃避
- 我一直都相信你
- 你一定要活下去
- 這就是我們的選擇

## 禁止修改區域

除非任務明確要求，不得擅自修改：
- 任何狀態為 LOCKED 的文件
- `00_protocol/` 中的協議文件（屬於通用骨架，新專案建置時透過 Bootstrap 流程微調，不在日常作業中隨意修改）
- `archive/`（歷史紀錄區）

## 素材區（`_source_materials/`）

`_source_materials/` 是 user 原始輸入素材區（人設、既有劇本台詞、世界觀筆記等），供 `/create-*` 等 skill 讀取參考，本質不屬於任一模組產物、不是實體。其下 `.md` 素材檔**不需** 5 欄 header（唯一例外為該目錄的 `README.md`），且被所有 frontmatter 掃描器排除、不計入實體進度、不報 header 缺漏。非 `.md` 素材（`.docx` / `.txt` / `.csv` / `.json`）本就不被掃描。

## 修改流程

每次修改前：
1. 先說明會讀哪些文件。
2. 先列出預計修改哪些文件。
3. 若涉及 LOCKED 文件，先停止並要求確認。

每次修改後：
1. 列出修改文件。
2. 摘要修改內容。
3. 標出可能影響的角色、章節、場景。
4. 若有檢查腳本，執行檢查。
5. 不得只說「已完成」，必須提供具體變更摘要。

## 修改後報告格式

### 修改檔案

- 

### 修改摘要

- 

### 影響範圍

角色：  
章節：  
場景：  
規則：  

### 後續建議

-

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

---

## Skill 清單（精簡索引）

本 repo 含 `.claude/skills/<name>/SKILL.md` 自訂 skill。Claude Code CLI 自動 discovery `.claude/skills/`，user 直接用 slash command 觸發；Codex CLI / App 由本索引 + 對話確認後讀對應 SKILL.md 執行。

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

### Skill 執行慣例（Codex CLI / App）

1. user 提 skill name → agent 從 `_user_manual/skill_registry_full.md` 查對應 `.claude/skills/<name>/SKILL.md` path。
2. 若檔案不存在或狀態未實作，停止並回報尚未實作，不得用骨架自行替代。
3. 讀完對應 SKILL.md 後向 user 確認啟動意圖，再依其 5 階段流程執行，不擅自跳階段。
4. 階段 4 寫檔前列出寫檔清單再確認；階段 5 驗證後印「下一步建議」。
