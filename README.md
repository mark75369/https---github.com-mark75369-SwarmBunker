狀態：DRAFT  
版本：0.2-clean  
最後更新：2026-05-17  
適用範圍：repo 總覽與模板導航  
優先級：一般  

# game-dialogue-bible

本 repo 是商業級長篇遊戲劇本與台詞製作資料庫，用於維護世界觀、角色聲線、資訊揭露順序、場景任務、台詞輸出與品質檢查。

操作規則以 `AGENTS.md` 與 `00_protocol/` 為準。標記為 `LOCKED` 的文件優先於聊天紀錄，未經確認不得修改。

## 目前狀態

本目錄是 Template repo 的乾淨擷取版（v0.2-clean），尚非實際遊戲專案正式設定。Template 用於 clone 到具體作品 Instance repo 後，由 Bootstrap 流程展開作品專屬內容。

新架構設計文件（即將補入）：
- `_design/SPEC.md` — 設計規格、邏輯實體 schema、四份上游創建協議專屬區段、迭代協議、bootstrap 邏輯
- `_design/ARCHITECTURE.md` — Template/Instance 分層、檔案結構、frontmatter 規範、skill 清單、視圖層機制
- `_design/TASKS.md` — 4 階段拆解、每階段任務、驗收條件
- `_design/EXTRACTION_NOTES.md` — 本次乾淨擷取的變更紀錄
- `_design/references/` — Phase A 參考素材（含蟲潮孤堡專案版 00_b，供反推通用骨架）

## 資料夾結構

```text
game-dialogue-bible/
├─ 00_protocol/        ← 通用協議與工作流規範
├─ 01_world/           ← 世界觀（規則 / 語言 / 陣營階級）
├─ 02_vocabulary/      ← 詞彙系統
├─ 03_characters/      ← 角色（main / minor / npc 子目錄）
├─ 04_relationships/   ← 關係矩陣與時間線
├─ 05_plot/            ← 主線、章節、弧線、揭露、伏筆
├─ 06_scene_index/     ← 場景索引
├─ 07_scene_tasks/     ← 單場台詞任務包
├─ 08_dialogue_outputs/← 台詞輸出與版本管理
├─ 09_quality_assurance/← QA 模板
├─ archive/            ← 歷史紀錄
├─ scripts/            ← 檢查腳本（路徑、frontmatter）
├─ _design/            ← 重啟版設計文件
├─ AGENTS.md
└─ README.md
```

## 模板導航

### 00_protocol

- `00_protocol/00_a_台詞生產協議.md`
- `00_protocol/00_b_反ai味檢查表.md` —（**通用骨架待建**：Phase A 由 CODEX 從 `_design/references/` 的蟲潮孤堡專案版反推；目前缺檔）
- `00_protocol/00_c_台詞輸出格式.md`
- `00_protocol/00_d_工作流總覽.md`
- `00_protocol/00_e_世界觀創建協議.md` —（Phase A 由 CODEX 建立）
- `00_protocol/00_f_角色創建協議.md` —（Phase B 由 CODEX 建立）
- `00_protocol/00_g_大綱創建協議.md` —（Phase B 由 CODEX 建立）
- `00_protocol/00_h_細綱創建協議.md` —（Phase B 由 CODEX 建立）
- `00_protocol/00_i_專案初始化協議.md` —（Phase A 由 CODEX 建立，Instance bootstrap）
- `00_protocol/00_j_迭代協議.md` —（Phase C 由 CODEX 建立，通用迭代）
- `00_protocol/00_k_台詞生產流程協議.md` —（Phase D 由 CODEX 建立，下游 pipeline 統合）
- `00_protocol/00_l_關係創建協議.md` —（Phase B 由 CODEX 建立，C-7 新增第 5 個上游協議）

### 01_world

- `01_world/01_a_世界觀總覽.md`
- `01_world/01_b_世界語言規格.md`
- `01_world/01_c_陣營與階級語言.md`

### 02_vocabulary

- `02_vocabulary/02_a_專有名詞表.md`
- `02_vocabulary/02_b_俗稱與黑話表.md`
- `02_vocabulary/02_c_禁用詞與慎用詞表.md`

### 03_characters

- `03_characters/03_a_角色總表.md`
- `03_characters/03_b_主要角色聲線卡模板.md`
- `03_characters/03_c_次要角色與npc模板.md`
- `03_characters/main/`
- `03_characters/minor/`
- `03_characters/npc/`

### 04_relationships

- `04_relationships/04_a_角色關係矩陣.md`
- `04_relationships/04_b_關係變化時間線.md`

### 05_plot

- `05_plot/05_a_主線大綱模板.md`
- `05_plot/05_b_章節結構模板.md`
- `05_plot/05_c_角色弧線表.md`
- `05_plot/05_d_資訊揭露表.md`
- `05_plot/05_e_伏筆與回收表.md`

### 06_scene_index

- `06_scene_index/06_a_場景索引模板.md`

### 07_scene_tasks

- `07_scene_tasks/07_a_單場台詞任務包模板.md`

### 08_dialogue_outputs

- `08_dialogue_outputs/08_a_台詞版本管理規範.md`
- `08_dialogue_outputs/08_b_生成台詞檔案模板.md`

### 09_quality_assurance

- `09_quality_assurance/09_a_ai味qa報告模板.md`
- `09_quality_assurance/09_b_角色聲線一致性檢查模板.md`
- `09_quality_assurance/09_c_禁用詞檢查報告模板.md`
- `09_quality_assurance/09_d_資訊控制檢查報告模板.md`
- `09_quality_assurance/09_e_定稿變更紀錄模板.md`
- `09_quality_assurance/09_f_類型偏移檢查模板.md` —（Phase D 由 CODEX 建立）
