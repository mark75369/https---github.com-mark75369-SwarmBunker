狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase A 後段 A.8 task 啟動包 — /check-gaps skill 實作  
優先級：高

# CODEX_A8_STARTER — Phase A 後段 A.8：/check-gaps skill 實作

# 0. 本檔用途

Wave 4 第二條 task — 實作 `/check-gaps` skill（含中文別名 `/缺漏檢查`），對應 SPEC §10 缺漏偵測 + DECISIONS_LOG P-003 view/ 失效偵測 + A.0 parser API。

**前置條件：** Wave 1+2+3 全 DONE + push（含 A.5 / A.6 / A.0F.2 完成）。**A.8 與 A.7 平行可跑**（兩條 skill 邏輯類似但實作獨立）。

**與 A.7 / A.12 平行性：** A.8 動 `.claude/skills/check-gaps/` + `.claude/skills/缺漏檢查/`；A.7 動 `.claude/skills/status/` + `.claude/skills/進度/`；A.12 動 root + manual 檔。三條不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.8 task」— 實作 `/check-gaps` skill（含中文 wrapper），對應 SPEC §10 缺漏偵測 + view/ 失效偵測 + Phase A.0 parser API。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（英文 skill + 中文 wrapper）
- 對應傳統：Wave 4 第二條 task（與 A.7 / A.12 平行可跑）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**動 `.claude/skills/init-project/` / `create-world/` / `status/`（屬 A.5/A.6/A.7）
- ✗ **不**寫 root AGENTS.md / CLAUDE.md / _user_manual/（屬 A.12）
- ✗ skill 本身**只讀**：不寫任何檔

**本 task scope（嚴格限定）：**

依 TASKS v1.5 §A.8（line 765-783）+ SPEC §10 缺漏偵測 + DECISIONS_LOG P-003 view/ 失效偵測 + Phase A.0 parser API。

### 任務目標

新建 2 個 SKILL.md：
1. `.claude/skills/check-gaps/SKILL.md` — 英文 skill 主檔
2. `.claude/skills/缺漏檢查/SKILL.md` — 中文 wrapper（觸發語 `/缺漏檢查`）

### SKILL.md 內容規範（依 ARCH §3.3）

每個 SKILL.md 在頂部含：
- frontmatter 區（at minimum）:
  ```
  ---
  name: check-gaps
  description: 掃描 Instance repo 全 .md frontmatter + 內文，列出 TODO/INFERENCE/CONFLICT 標記、空 entities 檔、缺漏實體檔、view/ 失效檔。純讀取，不寫任何檔。
  ---
  ```
- 主體 markdown 內容

### 英文 skill（`.claude/skills/check-gaps/SKILL.md`）內容結構

依 TASKS A.8 §做法，明示：

1. **觸發語：** `/check-gaps`（不接 user 參數；自動掃 repo 全 .md）

2. **依賴：**
   - `_design/SPEC.md` v1.2 §10（缺漏偵測規格 — 含 TODO/INFERENCE/CONFLICT 標記語意）
   - `_design/ARCHITECTURE.md` v1.4 §3.3（skill 內容規範）
   - `_design/expected_entities.yaml`（manifest 規則）
   - `scripts/parse_frontmatter.py`（A.0.10 patched）
   - Instance root `.protocol_version`（讀 phase_log 段）
   - 既有 `view/` 整合檔（如已存在）

3. **5 階段對應（依 ARCH §3.3 skill 內容規範）：**

   - **階段 1 診斷：** 確認 Instance 已 bootstrap（`.protocol_version` 存在 + phase_log 含 bootstrap entry status=completed）；若無 → ⏸ 條件未滿足 + 建議跑 /init-project + 停止

   - **階段 2 探索（5 維度掃描）：**
     
     a. **TODO/INFERENCE/CONFLICT 標記偵測：**
        - 掃所有 .md frontmatter（用 `parse_frontmatter.build_repo_index('.')`）
        - 對每檔 frontmatter `keys[*]` 或內文段落找：`TODO:` / `INFERENCE:` / `CONFLICT:` 三種標記
        - 紀錄：檔 path / line 號 / 標記類型 / 後續文字
     
     b. **空 entities 偵測：**
        - 對每檔 frontmatter，若 `entities: []` 但檔有 KEY content（內文有 dialogue lines / 段落）→ 列為「entities 漏標」
     
     c. **缺漏實體檔偵測：**
        - 讀 `_design/expected_entities.yaml` manifest
        - 對 phase_log 已跑過的 phase + 推導 expected entity set（同 A.7 邏輯）
        - 對每 expected entity，掃 expected target_dir 是否有對應 .md
        - 缺檔 → 列「expected but missing」+ 對應 skill 建議

   - **階段 3 view/ 失效偵測（整合 DECISIONS_LOG P-003）：**
     
     對 `view/` 目錄下每個 `<entity>.md` 整合檔：
     1. 讀 view/ 檔 header `組合來源` 段（列出哪些 source 檔組合而成；如 view/world.md 含 01_world/01_a / 01_b / 01_c / 02_*）
     2. 取 view 檔 `mtime`（`os.path.getmtime()`）
     3. 對每 source 檔取 `mtime`
     4. 若任一 source `mtime > view mtime` → 列「view/ 整合檔需更新」+ 印 UX §7.7 警告文案標題段：
        ```
        ## ⚠ view/ 整合檔需更新 / View Files Need Refresh
        ```
        + 列每個受影響的 view/ 檔 + 標出 source 比 view 新的具體檔
     
     若 view/ 目錄不存在或為空 → 跳過（不報錯）

   - **階段 4 缺漏實體 → 對應 skill 建議（同 A.7 §做法）：**
     - W-* → /create-world
     - V → /create-world
     - C-* → /create-character（Phase B+）
     - R-* → /create-relationship（Phase B+）
     - P → /create-outline（Phase B+）
     - CH-* → /create-detailed-outline（Phase B+）
     - S-* → /scene-task（Phase C+）

   - **階段 5 輸出：** 整理 4 段報告：
     
     ```
     === TODO / INFERENCE / CONFLICT 標記 ===
     [檔 path] (line N): TODO: <文字>
     [檔 path] (line N): CONFLICT: <文字>
     ...
     
     === entities 漏標（空 entities 但檔有 KEY 內文）===
     [檔 path]: 內文有 X 段台詞但 frontmatter entities 為空
     ...
     
     === 缺漏實體（expected but missing）===
     - W-rules：應由 /create-world 階段 4 寫到 01_world/01_a；目前不存在
     - V：應由 /create-world 階段 4 寫到 02_vocabulary/02_a；目前不存在
     ...
     
     === view/ 整合檔需更新 ===
     ## ⚠ view/ 整合檔需更新 / View Files Need Refresh
     - view/world.md（mtime: ...）— 比下列 source 舊：
       - 01_world/01_a_世界觀總覽.md（mtime: ...，比 view 新 X 分鐘）
     ...
     ```

4. **時期 C 呈現規則（依 TASKS A.8 line 783）：**
   - 遵循 §1.5「錯誤呈現四件套」（What / Where / Why / 下一步）
   - 遵循 §1.6「全文呈現約束」
   - 不暴露 enum 鍵 / stack trace

5. **錯誤處理：**
   - parse_frontmatter import 失敗 → ✗ 無法執行
   - `.protocol_version` 缺檔 → ⏸ 條件未滿足（建議跑 /init-project）
   - `_design/expected_entities.yaml` 缺檔 → ✗ 無法執行
   - build_repo_index 報 ERROR → 列前 5 條 ERROR + 建議跑 `python scripts/check_headers.py`
   - view/ 目錄不存在 → 跳過（normal case，不報錯）

6. **禁止事項：**
   - **不**修改任何檔（純讀取，TASKS A.8 同邏輯如 A.7）
   - **不**擅自更新 `.protocol_version`
   - **不**自動 trigger /create-* skill；只給建議

### 中文 wrapper（`.claude/skills/缺漏檢查/SKILL.md`）內容

採極簡 wrapper 策略：
- frontmatter：
  ```
  ---
  name: 缺漏檢查
  description: /check-gaps 中文別名 — 列出 TODO 標記 / 缺漏實體 / view/ 失效。實際邏輯參見 .claude/skills/check-gaps/SKILL.md。
  ---
  ```
- 主體：1-2 段說明「本 wrapper 觸發 /check-gaps skill 同樣流程；所有規範以英文版 SKILL.md 為權威」

### 5 階段流程文字長度建議

英文 skill 主檔 ~250-350 行 markdown（足以描述 5 階段 + 5 維度掃描 + view/ 失效邏輯 + 輸出格式 + 錯誤處理 + 呈現規則）；中文 wrapper ~20-30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.5（§A.8 line 765-783）
2. `_design/SPEC.md` v1.2 §10（缺漏偵測規格 — 全段）
3. `_design/ARCHITECTURE.md` v1.4 §3.3（skill 內容規範）
4. `_design/expected_entities.yaml`

B. 對齊依據
5. `scripts/parse_frontmatter.py`（`build_repo_index` / `parse_file` API）
6. `_design/UX_SPEC.md` v0.4 §7.7（view/ 整合檔需更新警告文案）
7. `_design/DECISIONS_LOG.md` v1.2 P-003（view/ 失效偵測暫定機制）
8. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2 / §3.3（phase_log + base_dialogue）
9. `.claude/skills/init-project/SKILL.md`（A.5 — 對齊風格）
10. `.claude/skills/create-world/SKILL.md`（A.6 — 對齊風格）

C. 已 LOCKED 不可動文件
11. 所有 `_design/*.md`
12. `scripts/*.py`
13. 既有 27 模板
14. `00_protocol/*` 全部
15. `_tools/frontend/*` 全部
16. `.claude/skills/init-project/` + `初始化專案/`
17. `.claude/skills/create-world/` + `建立世界觀/`
18. `.claude/skills/status/` + `進度/`（如 A.7 已先完成；A.8 不動）

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/check-gaps/SKILL.md`
2. `.claude/skills/缺漏檢查/SKILL.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name / description）+ markdown 主體
- 中文 wrapper 引用英文 skill 為權威
- 無新建其他檔

B. 內容
- 5 階段流程完整對齊 ARCH §3.3
- 階段 2 含 3 維度（TODO 標記 / 空 entities / 缺漏實體）
- 階段 3 view/ 失效偵測完整對齊 P-003 + UX §7.7 文案
- 階段 4 缺漏 entity → 對應 skill 對照表完整
- 階段 5 4 段輸出格式範例完整
- 錯誤處理含 5 個 case
- 禁止事項明示「純讀取」+「不自動 trigger」

C. 不破壞既有
- 沒動既有 27 模板 / _design / scripts / 00_protocol / _tools/frontend / 其他 .claude/skills/*
- `git diff --check` 通過

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master
- **NO-GO：** 5 階段對齊不到位 → 修補 round

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.8 完成 → user commit/push → 回 master → Wave 4 三條全完成後跑 review checkpoint（建議）→ Wave 5。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.8 task 啟動包；完成後可 archive 進 `_design/archive/`
- 若 A.8 NO-GO patch round → 開 CODEX_A8_PATCH_STARTER.md
