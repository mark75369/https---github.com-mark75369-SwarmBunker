狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase A 後段 A.7 task 啟動包 — /status skill 實作  
優先級：高

# CODEX_A7_STARTER — Phase A 後段 A.7：/status skill 實作

# 0. 本檔用途

Wave 4 第一條 task — 實作 `/status` skill（含中文別名 `/進度`），對應 ARCH §2.3 完成度公式 + SPEC §5.3 + §5.4 phase_log + A.0 parser API（`build_repo_index` / `parse_file` accessor）。

**前置條件：** Wave 1+2+3 全 DONE + push（含 A.5 ✓ init-project / A.6 ✓ create-world / A.0F.2 ✓ Dashboard）。

**與 A.8 / A.12 平行性：** A.7 動 `.claude/skills/status/` + `.claude/skills/進度/`；A.8 動 `.claude/skills/check-gaps/` + `.claude/skills/缺漏檢查/`；A.12 動 root `AGENTS.md` / `CLAUDE.md` + `_user_manual/skill_invocation_guide.md`。三條完全不重疊。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.7 task」— 實作 `/status` skill（含中文 wrapper），對應 ARCH §2.3 完成度計算 + SPEC §5.3/§5.4 + Phase A.0 parser API。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（英文 skill + 中文 wrapper）
- 對應傳統：Wave 4 第一條 task（與 A.8 / A.12 平行可跑）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code（scripts/*.py 不動）
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**動 `.claude/skills/init-project/` 或 `.claude/skills/create-world/`（屬 A.5/A.6 已完成）
- ✗ **不**寫 `/check-gaps` skill（屬 A.8）
- ✗ **不**寫 root AGENTS.md / CLAUDE.md / _user_manual/（屬 A.12）
- ✗ **不**讀寫任何 Instance `.protocol_version`（純讀取行為由 skill 跑時動作；不是 SKILL.md 內容）
- ✗ skill 本身**只讀**：不寫任何檔（依 A.7 TASKS 規範「純讀取」）

**本 task scope（嚴格限定）：**

依 TASKS v1.5 §A.7（line 727-764，含 v1.5 partial supersede 不動段）+ ARCH §2.3 完成度公式 + SPEC §5.3 完成度規格 + SPEC §5.4 phase_log + Phase A.0 parser API (build_repo_index / parse_file)。

### 任務目標

新建 2 個 SKILL.md：
1. `.claude/skills/status/SKILL.md` — 英文 skill 主檔
2. `.claude/skills/進度/SKILL.md` — 中文 wrapper（觸發語 `/進度`）

### SKILL.md 內容規範（依 ARCH §3.3）

每個 SKILL.md 在頂部含：
- frontmatter 區（at minimum）:
  ```
  ---
  name: status
  description: 列出 Instance repo 內所有實體（W/V/C/R/P/CH/S/A）的完成度百分比 + 缺漏實體建議下一步 skill。對齊 ARCH §2.3 完成度公式 + SPEC §5.3。純讀取，不寫任何檔。
  ---
  ```
- 主體 markdown 內容

### 英文 skill（`.claude/skills/status/SKILL.md`）內容結構

依 TASKS A.7 §做法（M4 鎖定）+ ARCH §2.3 公式，明示：

1. **觸發語：** `/status`（不接 user 參數；自動掃 repo 全 .md）

2. **依賴：**
   - `_design/SPEC.md` v1.2 §5.3（完成度公式定義）+ §5.4 + §5.4a（phase_log schema）
   - `_design/ARCHITECTURE.md` v1.4 §2.3（伪碼 + 輸出範例格式）
   - `_design/expected_entities.yaml`（manifest 規則，A.0 已建）
   - `scripts/parse_frontmatter.py`（A.0.10 patched；`build_repo_index` 為主要 API）
   - Instance root `.protocol_version`（讀 phase_log 段）

3. **5 階段對應（依 ARCH §3.3 skill 內容規範）：**
   
   - **階段 1 診斷：** 確認 Instance 已 bootstrap（讀 `.protocol_version` 必存在 + phase_log 含 bootstrap entry status=completed）；若無 → 印「⏸ 條件未滿足 / Prerequisites Not Met」（What/Where/Why/下一步建議跑 /init-project）並停止
   
   - **階段 2 探索：** 讀以下 input：
     1. `_design/expected_entities.yaml`（manifest）
     2. `.protocol_version` phase_log（推導 expected set）
     3. `scripts/parse_frontmatter.build_repo_index('.')` 取全 repo .md frontmatter index
   
   - **階段 3 推導 expected set：** 依 phase_log 已跑過的 phase + 每 entry 的 `created_entities`（單數逐筆）與 `scene_id`（單數逐筆，scene-task / dialogue-write / qa 各 phase 都用單數 scene_id），aggregate 成「實際應存在的實體 set」。bootstrap entry 的 `scene_ids: []` 是特例（複數空陣列，未來不再使用，僅保留向下相容）
   
   - **階段 4 計算完成度：** 對 expected set 每實體跑 ARCH §2.3 完成度公式：
     ```
     score_map = {DRAFT: 25, REVIEW: 75, FINAL: 100, LOCKED: 100}
     對每個 contributing 檔：
       score = score_map[file.status]
       weight = file.frontmatter.get('weight', {})[entity_id] 或 1.0
     entity_completion = Σ(score * weight) / Σ(weight)
     ```
     對有 expected 但無 contributing 檔的實體計 0% + 標「缺漏，建議跑 `<對應 skill>`」
     對不在 expected set 但 frontmatter entities 內出現的實體 → 也計算，但標「未追蹤（手動建）」
   
   - **階段 5 輸出：** 依 ARCH §2.3 line 359-378 輸出範例格式：
     ```
     === 邏輯實體完成度 ===
     W-rules               100%  (FINAL)
     W-language             75%  (1 REVIEW)
     V                      50%  (3 DRAFT)
     ...
     === 缺漏實體 ===
     - P：主線尚未建立，建議跑 /create-outline
     ```

4. **時期 C 呈現規則（依 TASKS A.7 line 755-758）：**
   - 遵循 §1.5「不暴露 enum 鍵」：`pipeline_state` 等內部值不直接顯示給使用者，改為人類可讀詞
   - 遵循 §1.6.1「G1：badge 不單獨呈現」：實體狀態不只一個 badge，必須附完成度數字或檔案清單
   - 遵循 §1.6.1「G2：流程視覺化僅為閱讀順序」：若 status 列出「下游 pipeline 階段」，須加注「閱讀順序用，不代表強制執行步驟」

5. **缺漏 entity → 建議 skill 對應表：**
   - W-* → /create-world
   - V → /create-world（V 屬於世界觀建立階段；TASKS line 750-752）
   - C-* → /create-character（Phase B+）
   - R-* → /create-relationship（Phase B+）
   - P → /create-outline（Phase B+）
   - CH-* → /create-detailed-outline（Phase B+）
   - S-* → /scene-task（Phase C+）
   - A-* → 手動編輯 10_art_assets/<subtype>/index.md（無對應 skill）

6. **錯誤處理：**
   - parse_frontmatter import 失敗 → ✗ 無法執行（What/Where/Why/下一步：補 scripts/parse_frontmatter.py path）
   - `.protocol_version` 缺檔 → ⏸ 條件未滿足（建議跑 /init-project）
   - `_design/expected_entities.yaml` 缺檔 → ✗ 無法執行
   - build_repo_index 報 ERROR → 列前 5 條 ERROR + 建議跑 `python scripts/check_headers.py`

7. **禁止事項：**
   - **不**修改任何檔（純讀取，TASKS A.7 line 762-763）
   - **不**擅自更新 `.protocol_version`（只有對應 skill 在自己階段 5 寫入）

### 中文 wrapper（`.claude/skills/進度/SKILL.md`）內容

採極簡 wrapper 策略：
- frontmatter：
  ```
  ---
  name: 進度
  description: /status 中文別名 — 列出實體完成度與缺漏建議。實際邏輯參見 .claude/skills/status/SKILL.md。
  ---
  ```
- 主體：1-2 段說明「本 wrapper 觸發 /status skill 同樣流程；所有規範以英文版 SKILL.md 為權威」

### 5 階段流程文字長度建議

英文 skill 主檔 ~200-300 行 markdown（足以描述 5 階段 + parser API 用法 + 公式 + 缺漏建議對照 + 錯誤處理 + 呈現規則）；中文 wrapper ~20-30 行。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.5（§A.7 line 727-764）
2. `_design/ARCHITECTURE.md` v1.4 §2.3（完成度公式偽碼 + 輸出範例）+ §3.3（skill 內容規範）+ §3.3.0（multi-agent invocation 慣例 — 對應 A.12 是別 task，A.7 不動 root 檔）
3. `_design/SPEC.md` v1.2 §5.3（完成度公式定義）+ §5.4 / §5.4a（phase_log schema）
4. `_design/expected_entities.yaml`（manifest）

B. 對齊依據
5. `scripts/parse_frontmatter.py`（A.0.10 patched — 確認 `build_repo_index('.')` 和 `parse_file(path)` 兩個函數 signature）
6. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2 / §3.3（phase_log 5 新欄位 + status enum + base_dialogue）
7. `_design/DECISIONS_LOG.md` v1.2 §6.9.2（D-047 三 registry copy）+ §6.7.x（D-042 phase_log status formalize）
8. `.claude/skills/init-project/SKILL.md`（A.5 已完成 — 對齊 SKILL.md 結構慣例 + frontmatter 格式 + 5 階段風格）
9. `.claude/skills/create-world/SKILL.md`（A.6 已完成 — 同上）

C. 已 LOCKED 不可動文件
10. 所有 `_design/*.md`
11. `scripts/*.py`
12. 既有 27 模板
13. `00_protocol/*` 全部
14. `_tools/frontend/*` 全部
15. `.claude/skills/init-project/` + `.claude/skills/初始化專案/`（A.5）
16. `.claude/skills/create-world/` + `.claude/skills/建立世界觀/`（A.6）

---

**你要交付的產物：**

新建 2 個檔：
1. `.claude/skills/status/SKILL.md`
2. `.claude/skills/進度/SKILL.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 2 個 SKILL.md 存在
- 各自含 frontmatter（name / description）+ markdown 主體
- 中文 wrapper 引用英文 skill 為權威
- 無新建其他檔（如 .py / .yaml / 其他 .md）

B. 內容
- 5 階段流程完整對齊 ARCH §3.3 skill 規範
- 階段 4 完成度公式對齊 ARCH §2.3 偽碼 + SPEC §5.3
- expected set 推導邏輯依 phase_log（單數 scene_id 與 created_entities）
- 缺漏實體 → 對應 skill 建議表
- 階段 5 輸出格式對齊 ARCH §2.3 line 359-378 範例
- 時期 C 三條呈現規則明示遵循
- 錯誤處理含 4 個失敗 case
- 禁止事項明示「純讀取」

C. 不破壞既有
- 沒動既有 27 模板 / _design / scripts / 00_protocol / _tools/frontend / .claude/skills/init-project / .claude/skills/create-world
- `git diff --check` 通過

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master
- **NO-GO：** 5 階段對齊不到位 → 修補 round（同 Wave 2 A.0F.1 模式）

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.7 完成 → user commit/push → 回 master → Wave 4 三條完成後跑 review checkpoint（建議）→ Wave 5。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.7 task 啟動包；完成後可 archive 進 `_design/archive/`
- 若 A.7 NO-GO patch round → 開 CODEX_A7_PATCH_STARTER.md（同 A.0F.1 模式）
