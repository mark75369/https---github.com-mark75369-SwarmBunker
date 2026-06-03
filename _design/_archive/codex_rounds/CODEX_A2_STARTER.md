狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.2 task 啟動包 — 00_i 專案初始化協議寫作  
優先級：高

# CODEX_A2_STARTER — Phase A 後段 A.2：寫 00_i 專案初始化協議

# 0. 本檔用途

Wave 1（A.1 / A.4 / A.0F.0）全 PASS。本檔給 Wave 2 第一條 task — A.2 寫 `00_protocol/00_i_專案初始化協議.md` 啟動。

**前置條件：** Wave 1 三條全 DONE + push（A.1 必須先完成）。

**與 A.3 / A.0F.1 平行性：** A.2 / A.3 / A.0F.1 三條動的檔完全不重疊（A.2 新建 00_i / A.3 新建 00_e / A.0F.1 改 server.py）。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.2 task」— 寫 `00_protocol/00_i_專案初始化協議.md`（Instance Bootstrap 流程規範）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪寫一份新 markdown 檔（`00_protocol/00_i_專案初始化協議.md`）
- 對應傳統：Wave 2 第一條 task（與 A.3 / A.0F.1 平行可跑）
- documentation-style writer — protocol 撰寫工作，邏輯來源 100% 來自既有 spec

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板（已由 A.4 處理完）
- ✗ **不**改 `00_protocol/00_b_反ai味檢查表.md`（A.1 已建）
- ✗ **不**動 `_tools/frontend/` 任何檔（A.0F.0 範圍）
- ✗ **不**寫 /init-project skill 實作（屬 A.5）
- ✗ **不**允許 Bootstrap 微調 00_a / 00_e ~ 00_j / 01-09 模板（禁止項 — 嚴格鎖）
- ✗ **不**新建 00_c / 00_d 等其他 protocol 檔（屬本 protocol 提及但本輪不寫）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.2（line 565-584）+ SPEC v1.2 §8（Instance Bootstrap 流程）+ UD v0.5 §1.0.1（共通骨架 10 區段執行細則）。

### 任務目標

新建 `00_protocol/00_i_專案初始化協議.md` — 規範 Instance Bootstrap 流程（由 `/init-project` 觸發）。

### 具體做法

1. **讀 SPEC §8**（line 645-697）— Instance Bootstrap 生命週期 + 10 區段對應內容表 + `.protocol_version` YAML 範本
2. **讀 UD §1.0.1**（line 80 ~ §1.0.2 之前）— 共通骨架 10 區段執行細則
3. **讀 UD §1.0.2 / §1.0.3** — 觸發語字典 + 先決資料缺失處理
4. **沿用既有 27 模板的 markdown 風格**：
   - 中文 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）在前
   - YAML block 在 header 後（協議檔 entities=[] / depends_on=[] / weight={}）
   - 主要章節 # 1. ~ # 10. 對應 SPEC §8 表格
5. **章節結構**（依 SPEC §8 表 + 10 區段共通骨架）：
   ```
   # 1. 文件目的
   # 2. 啟動條件（先決資料）
   # 3. 階段 1：診斷模式
   # 4. 階段 2：探索 / 補洞對話
   # 5. 階段 3：收斂模式
   # 6. 階段 4：Codex 執行模式（含自動拆分）
   # 7. 階段 5：實體驗證（自動呼叫 /status）
   # 8. 禁止事項
   # 9. 缺漏處理
   # 10. Bootstrap 專屬區段
       ## 10.1 微調清單範本（限定 00_b / 00_c / 00_d）
       ## 10.2 `.protocol_version` YAML 格式規範（含 Bootstrap 後 phase_log 初始化）
       ## 10.3 Bootstrap 完成後的標準目錄狀態
       ## 10.4 registry copy 規範（D-043 entity_type_registry + qa_type_registry + D-047 issue_type_registry 三 registry 從 Template 複製到 Instance root）
   ```
6. **每階段細節**：
   - **階段 1 診斷**：使用者貼新專案基本資料（作品名、類型、長度、目標、語氣偏好、參考作品）
   - **階段 2 探索**：agent 列出**限定**可微調的 Template 文件 — 只有 00_b（反 AI 味檢查表） / 00_c（台詞輸出格式） / 00_d（情境設定）
   - **階段 3 收斂**：使用者逐項拍板微調
   - **階段 4 執行**：agent 套用微調 + 寫 `.protocol_version` + 從 Template 複製三 registry → Instance root + 建立 10_art_assets/ 目錄結構（7 subtype 子目錄）+ Instance root 加 `.gitignore` 列 `export/`
   - **階段 5 驗證**：報告 Bootstrap 完成 + 建議下一步 `/create-world`
7. **`.protocol_version` 範本**（SPEC §8 line 681-697 直接照搬，補 v0.4 註：含 issue_type_registry 拷貝紀錄）：
   ```yaml
   template_source: github.com/<user>/game-dialogue-bible-template
   template_commit: <commit SHA>
   bootstrap_date: <ISO date>
   project_name: <作品名>

   customizations:
     - file: 00_protocol/00_b_反ai味檢查表.md
       type: 專案化
       note: 從骨架擴充到《<作品名>》專屬版本

   bootstrapped_registries:        # D-047 + D-043 對齊
     - source: _design/registries/entity_type_registry.template.yaml
       target: entity_type_registry.yaml
       version: v0.3
     - source: _design/registries/qa_type_registry.template.yaml
       target: qa_type_registry.yaml
       version: v0.3
     - source: _design/registries/issue_type_registry.template.yaml
       target: issue_type_registry.yaml
       version: v0.1

   phase_log: []                   # 後續每個 skill 跑完 append（依 SPEC §5.4 + DF v0.4 §3.2）
   ```
8. **禁止事項**（第 8 區段必含）：
   - 不得擅自微調 `00_a 台詞生產協議` / `00_e ~ 00_j 上游創建協議` / `01-09 既有模板`（會破壞通用協議跨 Instance 一致性）
   - 不得跳過任何階段（5 階段順序鎖死）
   - 不得在 `.protocol_version` 之外另建 Instance metadata 檔
9. **header**：
   ```
   狀態：DRAFT
   版本：v0.1
   最後更新：2026-05-19
   適用範圍：全作品 Bootstrap 流程通用協議
   優先級：高
   ```
10. **frontmatter** YAML block（協議檔不貢獻實體）：
    ```yaml
    ---
    entities: []
    depends_on: []
    weight: {}
    ---
    ```

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（A.2 任務 line 565-584 + A.5 task 看 Bootstrap registry copy 需求 line 633-660）
2. `_design/SPEC.md` v1.2 §8（Instance Bootstrap 流程 line 645-697）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.0.1 / §1.0.2 / §1.0.3（共通骨架 10 區段 / 觸發語字典 / 先決缺失處理）

B. 對齊參考
4. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log schema）
5. `_design/DECISIONS_LOG.md` v1.1 §6.9.2（D-047 — issue_type_registry 三層機制）
6. `_design/registries/issue_type_registry.template.yaml`（v0.1 — copy target）
7. `_design/registries/entity_type_registry.template.yaml`（v0.3 — copy target）
8. `_design/registries/qa_type_registry.template.yaml`（v0.3 — copy target）

C. 風格參考
9. `00_protocol/00_b_反ai味檢查表.md`（A.1 剛完成 — 採同樣 header / yaml block / chapter 風格）

D. 已 LOCKED 不可動文件（明示禁區）
10. 所有 `_design/*.md`
11. `scripts/*.py`
12. 既有 27 模板
13. `_tools/frontend/*`

---

**你要交付的產物：**

唯一新建檔：`00_protocol/00_i_專案初始化協議.md`

**驗收條件（CODEX 自我驗證）：**

A. 結構驗證
- 中文 header 5 欄 + YAML block (entities=[]/depends_on=[]/weight={})
- 含 10 個主章節對應 SPEC §8 表
- §10.1 微調清單範本明確標「限定 00_b / 00_c / 00_d」
- §10.2 `.protocol_version` 範本完整 + 含 3 registry copy（含 issue_type_registry）+ phase_log 初始化
- §10.4 三 registry copy 規範對齊 D-047 + D-043

B. 內容驗證
- 5 階段順序與細節對齊 SPEC §8 表
- 禁止事項段明示 00_a / 00_e ~ 00_j / 01-09 不可微調
- 整檔搜尋無作品名 / 角色名 / 蟲潮孤堡相關詞

C. Parser 驗證
- 跑 `python scripts/check_headers.py` → 0 ERROR
- 跑 `python -c "from scripts.parse_frontmatter import parse_file; r = parse_file('00_protocol/00_i_專案初始化協議.md'); print(r.header, r.issues)"` → header 5 欄完整 / issues=[]

D. 不破壞既有
- `git diff --check` 通過
- 不動既有 27 模板 / _design / scripts / _tools/frontend
- 不動 00_protocol/00_b（A.1 範圍）

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A2_REPORT.md`（可選 — 因禁區明示不改 `_design/*.md`，可不交報告，inline 回 master 對話即可）

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件全 ✓
- **BLOCKED：** 任一驗收 ✗，回 master

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.2 完成 = 4 驗收 ✓ + 沒動禁區。User 手動 commit + push → 回 master 對話告訴我結果 → 我推 A.5（用 00_i）或繼續 A.3 / A.0F.1。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.2 task 啟動包；完成後 archive
