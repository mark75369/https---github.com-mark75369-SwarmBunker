狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase B Wave 7 task 啟動包 — B.5 + B.5b + B.6 三 skill 實作  
優先級：高

# CODEX_WAVE7_SKILLS_STARTER — Phase B Wave 7：3 個 /create-* skill 實作

# 0. 本檔用途

Phase B Wave 7 task — 實作 3 個 /create-* skill（同 Wave 6 整合 starter 模式：1 條 CODEX 對話跑 3 skill）。

**前置條件：** Phase A 全部完成（A.0~A.12 + Wave 1~5 全 PASS）+ Wave 6 patch round 完成（00_f / 00_l / 00_g protocol v0.2 D-047 對齊）。

**與 Wave 8 的關係：** B.7 /create-detailed-outline 屬 Wave 8 範圍（依賴 B.6.5 主線 REVIEW gate；本 starter 不含 B.7）。

**人類 REVIEW gate 不含本 starter：** B.5.5（角色 REVIEW gate）+ B.6.5（主線 REVIEW gate）屬人類動作，由 user 在 CODEX 跑完本 starter 後親跑。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase B Wave 7 task」— 實作 3 個 /create-* skill（B.5 /create-character + B.5b /create-relationship + B.6 /create-outline），對齊 Wave 6 已 patch 的 protocol v0.2。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 6 個新 SKILL.md（3 英文主檔 + 3 中文 wrapper）
- 對應傳統：Wave 7 整合 task（B.5 + B.5b + B.6；B.5.5 / B.6.5 屬 user 人類 REVIEW gate 不在本輪 scope）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含本輪 Wave 6 patch 的 00_f / 00_l / 00_g — 已 v0.2 對齊不動）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 8 個 SKILL.md（init-project / create-world / status / check-gaps + 4 中文 wrapper）
- ✗ **不**寫 /create-detailed-outline（B.7 Wave 8 scope）
- ✗ **不**跑 user 拍板的 B.5.5 / B.6.5 REVIEW gate（屬人類 task）
- ✗ **不**新增 .claude/skills/<name>/INVOKE.md（D-048 否決候選 a）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.5 + §B.5b + §B.6 + ARCH v1.5 §3.3 / §3.3.0 / §3.3.2 + DECISIONS_LOG v1.9 §6.9.2 D-047 + §6.11.2 D-049 + §6.12.2 D-050 + §6.13.2 D-051 + §6.16.2 D-053 + 對應 protocol 00_f / 00_l / 00_g v0.2 + UD §1.2 / §1.3 / §1.5。（注：本 starter v0.1 為 Wave 7 起手歷史紀錄；後續 D-050 / D-052 / D-053 supersede 已在對應 SKILL.md v0.2 + 重審 patch round 對齊；本 starter scope text v1.8→v1.9 為 §6.16 stale ref cleanup。）

### 任務目標

新建 6 個 SKILL.md（3 主 + 3 wrapper）：

| # | 路徑 | 主檔 / wrapper | 對應 protocol | UD § |
|---|---|---|---|---|
| 1 | `.claude/skills/create-character/SKILL.md` | 英文主檔 | 00_f v0.2 | UD §1.2 |
| 2 | `.claude/skills/建立角色/SKILL.md` | 中文 wrapper | — | — |
| 3 | `.claude/skills/create-relationship/SKILL.md` | 英文主檔 | 00_l v0.2 | UD §1.5 |
| 4 | `.claude/skills/建立關係/SKILL.md` | 中文 wrapper | — | — |
| 5 | `.claude/skills/create-outline/SKILL.md` | 英文主檔 | 00_g v0.2 | UD §1.3 |
| 6 | `.claude/skills/建立大綱/SKILL.md` | 中文 wrapper | — | — |

### 3 主 SKILL.md 共用結構（依 ARCH §3.3）

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字）
- 中文 5 必填 header
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（英文 slash command + 中文別名 reference）
  - `## 觸發協議`（對應 00_f / 00_l / 00_g v0.2 + 必讀 references）
  - `## 啟動前檢查`（**D-049 Template-detect 兩道防線** + Bootstrap completed check + protocol 對應 prerequisite）
  - `## 流程`（5 階段對應 protocol §3-§7）
  - `## 議題清單動態載入`（**D-047 機制** — 讀 issue_type_registry.yaml 對應 skill key + Template fallback）
  - `## .protocol_version 寫入規範`（phase_log entry 含 `created_entities` 單數逐筆 / `skill` / `status: completed`）
  - `## 輸入`
  - `## 輸出`
  - `## 邊界`（明示禁止跨 Phase / 不擅啟下游 skill / 不寫超出 protocol scope 的內容）
  - `## 錯誤處理 / Rollback`
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### B.5 /create-character skill 差異規格

- **觸發語：** `/create-character <name>`（接 1 個 user 參數 — 角色名）
- **對應 protocol：** `00_protocol/00_f_角色創建協議.md` v0.2 全 5 階段
- **UD 權威：** UD §1.2.2（完整對話腳本）
- **議題 yaml key：** `00_f_character`（8 core 議題 — 詳 issue_type_registry.template.yaml v0.1）
- **寫檔目錄：** 依 `<name>` 分類：
  - 主要角色 → `03_characters/main/<name>_聲線卡.md`
  - 次要角色 → `03_characters/minor/<name>_聲線卡.md`
  - NPC → `03_characters/npc/<NPC類型>模板.md`
  - （由階段 1 user 拍板分類）
- **創建 entity：** `C-<name>`（單數逐筆寫進 phase_log.created_entities）
- **依賴：** Phase A 完成（W-rules / W-language / V 已 REVIEW）→ 對齊 Phase B 啟動條件
- **Phase A.10 對齊：** skill 啟動時必須驗 W-rules / W-language / V 至少 REVIEW；缺則 ⏸ 條件未滿足
- **下游：** 階段 5 印「下一步建議 /create-relationship 或 /create-outline」；**不**自動 trigger

### B.5b /create-relationship skill 差異規格

- **觸發語：** `/create-relationship <a> <b>`（接 2 個 user 參數 — 兩角色名）
- **對應 protocol：** `00_protocol/00_l_關係創建協議.md` v0.2 全 5 階段
- **UD 權威：** UD §1.5.2
- **議題 yaml key：** `00_l_relationship`（6 core 議題）
- **寫檔目錄：** `04_relationships/04_a_角色關係矩陣.md`（追加 row）+ `04_relationships/04_b_關係變化時間線.md`（如階段 2 議題 6 觸發）+ `03_characters/main/<a>_聲線卡.md` 與 `<b>_聲線卡.md` 各自關係段（merge）
- **創建 entity：** `R-<a>-<b>`（單數逐筆）
- **依賴：** B.5 至少 1 次 C-<a> / C-<b> 創建完成（兩角色都 ≥ REVIEW）+ B.5.5 角色 REVIEW gate PASS
- **下游：** 階段 5 印「下一步建議 /create-outline」；不自動 trigger

### B.6 /create-outline skill 差異規格

- **觸發語：** `/create-outline`（不接參數；屬「整體大綱」）
- **對應 protocol：** `00_protocol/00_g_大綱創建協議.md` v0.2 全 5 階段
- **UD 權威：** UD §1.3.2
- **議題 yaml key：** `00_g_outline`（6 core 議題）
- **寫檔目錄：** `05_plot/05_a_主線大綱模板.md`（主體）+ `05_plot/05_c_角色弧線表.md`（如 user 拍板含弧線分析）+ `05_plot/05_d_資訊揭露表.md` / `05_e_伏筆與回收表.md`（議題 4/5 觸發）
- **創建 entity：** `P`（單一，無 suffix；單數寫進 phase_log.created_entities）
- **依賴：** W-rules / V / C-* 至少 1 個 ≥ REVIEW
- **下游：** 階段 5 印「下一步建議 /create-detailed-outline（屬 Phase B Wave 8）+ B.6.5 主線 REVIEW gate」；不自動 trigger

### 3 主 SKILL.md 共用規範細項

#### 啟動前檢查（每 skill 必含；對齊 D-049 Template-detect + Bootstrap completed）

```
Before Stage 1, verify (對齊 00_<x> §2):

- current folder is the Instance repo root（含 00_protocol/ / 01_world/ 等目錄）
- `.protocol_version` 存在 + phase_log 含 bootstrap entry status=completed（依 D-042）
- `_design/expected_entities.yaml` 存在
- `_design/registries/issue_type_registry.template.yaml` 存在（fallback source）
- `<instance_root>/issue_type_registry.yaml` 可讀（含對應 skill key；缺則 Template fallback + WARN）
- **(D-049 第一道防線)** no `.template_root` marker file exists at repo root
- **(D-049 第二道防線)** NOT (`_design/registries/*.template.yaml` exists AND `.protocol_version` is absent)
- 對應 protocol 依賴的上游 entity 至少 REVIEW（C 需 W-rules / V / W-language；R 需 C；P 需 W-rules / V）
```

對應拒絕文案參考 init-project SKILL.md v0.2「⏸ 條件未滿足」格式 — 含 What / Where / Why / 下一步。

#### 議題清單動態載入段（每 skill 必含；D-047 機制）

```
Stage 2 starts with：
1. 讀 `<instance_root>/issue_type_registry.yaml` 對應 skill key（00_f_character / 00_l_relationship / 00_g_outline）
2. 依 `core + user_extensions − core_overrides` 動態構建（詳 00_<x> §4.0）
3. 對每議題依 required_level 處理（REQUIRED / STRONGLY_PREFERRED / OPTIONAL；詳 00_<x> §4.0 step 4）
4. 完整提問腳本：依 UD §1.<x>.2 對應段（不擅自重寫 / 不擅自濃縮）
5. `core[*].question_summary` 只作 opener
```

#### 邊界 / 禁止段（每 skill 必含）

```
The skill must not:
- modify LOCKED files
- allow Bootstrap customization（屬 /init-project scope）
- modify `00_protocol/` 任何 protocol（即使對應自己的 protocol）
- modify `scripts/` / `_tools/frontend/` / registry Template files
- 跨 Phase 寫檔（C skill 不寫 R 檔 / R skill 不寫 P 檔 / P skill 不寫 CH 檔）
- 自動 trigger 下游 skill（即使階段 5 建議了）
- 在已有同名 entity 的 Instance 上重寫（檢查 frontmatter `entities`；若衝突 → 觸發 Conflict modal 4 選項 — 但本 skill 階段 0 拒絕，由 user 改用 /iterate-* skill 或手動拍板 conflict resolution）
- 寫真實 .protocol_version 值在本 SKILL.md 內
```

#### 中文 wrapper 內容（3 個 wrapper 統一）

採極簡 wrapper 策略，對齊既有 4 個中文 wrapper（初始化專案 / 建立世界觀 / 進度 / 缺漏檢查）的風格：

```markdown
---
name: 建立<x>
description: /create-<x> 中文別名 — 觸發<功能描述>流程。實際邏輯參見 .claude/skills/create-<x>/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Claude Code `/建立<x>` 中文別名 wrapper
優先級：高

# 中文別名 - 建立<x>

本 skill 是 `/create-<x>` 的中文別名。當使用者以 `/建立<x>` 觸發時，等同於觸發 `/create-<x>`。

完整流程、五階段規則、`.protocol_version` schema、issue_type_registry 動態載入、D-049 Template-detect 兩道防線、rollback 與錯誤處理，全部以 `.claude/skills/create-<x>/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/create-<x>/SKILL.md`。
```

### 文字長度建議

每主 SKILL.md ~250-350 行 markdown（含 5 階段 + Template-detect + issue_registry 動態載入 + phase_log schema + 錯誤處理）；每中文 wrapper ~30 行（極簡）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§B.5 + §B.5b + §B.6）
2. `_design/ARCHITECTURE.md` v1.5 §3.2 wrapper / §3.3 skill 規範 / §3.3.0 multi-agent / §3.3.2 Template-detect
3. `_design/SPEC.md` v1.2 §5.1 entity / §5.3 完成度 / §5.4 phase_log / §16 文件狀態機
4. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2 / §1.3 / §1.5（C / P / R skill 上游權威 — 完整對話腳本）

B. 對齊依據（reference templates）
5. `_design/DECISIONS_LOG.md` v1.9 §6.9.2 D-047 + §6.11.2 D-049 + §6.11.7 baseline 校正 + §6.12.2 D-050 + §6.13.2 D-051 + §6.16.2 D-053
6. `_design/registries/issue_type_registry.template.yaml` v0.1（議題清單 source — 對應 4 skill 議題數）
7. `00_protocol/00_f_角色創建協議.md` v0.2 全 5 階段（B.5 觸發協議）
8. `00_protocol/00_l_關係創建協議.md` v0.2 全 5 階段（B.5b 觸發協議）
9. `00_protocol/00_g_大綱創建協議.md` v0.2 全 5 階段（B.6 觸發協議）
10. `.claude/skills/init-project/SKILL.md` v0.2（D-049 Template-detect + 5 階段範式）
11. `.claude/skills/create-world/SKILL.md`（既有 A.6 — 對齊 issue_registry 動態載入範式）
12. `.claude/skills/初始化專案/SKILL.md` + `建立世界觀/SKILL.md`（中文 wrapper 範式）

C. 已 LOCKED 不可動文件
13. 所有 `_design/*.md` 既有 spec
14. `scripts/*.py`
15. 既有 27 模板
16. `00_protocol/*` 全部（含本輪 Wave 6 patch 後的 00_f / 00_l / 00_g v0.2；不再 patch）
17. `_tools/frontend/*` 全部
18. 既有 8 個 SKILL.md（init-project / create-world / status / check-gaps + 4 wrapper）
19. `.template_root` marker / AGENTS.md / CLAUDE.md / _user_manual/skill_invocation_guide.md

---

**你要交付的產物：**

新建 6 個檔：
1. `.claude/skills/create-character/SKILL.md`
2. `.claude/skills/建立角色/SKILL.md`
3. `.claude/skills/create-relationship/SKILL.md`
4. `.claude/skills/建立關係/SKILL.md`
5. `.claude/skills/create-outline/SKILL.md`
6. `.claude/skills/建立大綱/SKILL.md`

不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 6 個 SKILL.md 存在
- 各自含 frontmatter（name + description）+ 中文 5 必填 header + markdown 主體
- 3 中文 wrapper 引用英文主檔為權威 + 不展開第二套流程

B. 內容（3 主 SKILL.md 各自）
- 5 階段流程對齊對應 protocol v0.2 §3-§7
- 啟動前檢查含 D-049 Template-detect 兩道防線 + Bootstrap completed check + 對應上游 entity REVIEW check
- 議題清單動態載入段含 D-047 機制 + 對應 yaml skill key + Template fallback + 完整提問腳本 ref UD §1.x.2
- phase_log.created_entities 寫法為單數逐筆（依 D-042 schema）+ status=completed
- 觸發語對應正確（/create-character <name> / /create-relationship <a> <b> / /create-outline）
- 寫檔目錄對齊（C → 03_characters/main+minor+npc/ / R → 04_relationships/ + 03_characters/<name>聲線卡關係段 / P → 05_plot/）
- 邊界明示禁止跨 Phase / 不自動 trigger 下游 / 不修改 00_protocol/

C. 不破壞既有
- 不動既有 8 SKILL.md / .claude/skills/init-project/ / create-world/ / status/ / check-gaps/ 等
- 不動 27 模板 / 00_protocol/ / _design/ 既有 spec
- 不新增 INVOKE.md（D-048 嚴禁）
- `python scripts/check_headers.py` 0 ERROR 維持

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 任一 skill 5 階段不對齊 protocol v0.2 → 修補 round

請開始。
```

---

# 2. 完成條件 + 後續

CODEX Wave 7 完成 → user commit/push → 回 master → master 推 B.5.5 角色 REVIEW gate（**人類**親跑；user 在 3_characters/ 子目錄內讀 C-* 模板檔讀完後親手升 frontmatter status DRAFT → REVIEW + 寫 `_design/phase_b_character_review_log.md`）→ B.5b skill 用 → B.6 skill 用 → B.6.5 主線 REVIEW gate → 進 W