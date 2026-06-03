狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase A 後段 A.12 task 啟動包 — NEW_REQ_7 落地（root AGENTS.md + CLAUDE.md + _user_manual/skill_invocation_guide.md）  
優先級：高

# CODEX_A12_STARTER — Phase A 後段 A.12：NEW_REQ_7 Multi-agent invocation 落地

# 0. 本檔用途

Wave 4 第三條 task — 落地 D-048 拍板（候選 b + c）：補 root `AGENTS.md` 擴充段 + 新建 root `CLAUDE.md` + 新建 `_user_manual/skill_invocation_guide.md`，對齊 4 個 agent 環境（Claude Code CLI / Codex CLI / Codex App / Cowork）。

**前置條件：** Wave 1+2+3 全 DONE + push（含 A.5 / A.6 / A.0F.2 完成）；M1 user-test 完成（M1-D-01 patch 已 master inline 落地，本 task 不動 frontend）。

**與 A.7 / A.8 平行性：** A.12 動 root `AGENTS.md` / `CLAUDE.md` + `_user_manual/skill_invocation_guide.md`；A.7 動 `.claude/skills/status/`；A.8 動 `.claude/skills/check-gaps/`。三條完全不重疊。

⚠ **既有檔狀態（重要）：**
- `AGENTS.md`（root）：**已存在**（含 repo meta-rule 規範：LOCKED 文件規則 / 文件頭格式 / 等）。本 task **不重寫**，只在既有內容後**擴充**「skill 清單 + Codex invocation」新段
- `CLAUDE.md`（root）：**不存在**，本 task 新建
- `_user_manual/skill_invocation_guide.md`：**不存在**，本 task 新建（屬 NEW_REQ_2 manual 第 4 章補充或獨立檔；CODEX 依 manual 既有結構決定）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.12 task」— 落地 NEW_REQ_7 D-048 拍板（候選 b + c）：multi-agent invocation 慣例。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪擴充 1 個既有檔（AGENTS.md）+ 新建 2 個檔（CLAUDE.md + skill_invocation_guide.md）
- 對應傳統：Wave 4 第三條 task（與 A.7 / A.8 平行可跑）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code（scripts/*.py 不動）
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**動任何 `.claude/skills/*/SKILL.md`（屬 A.5/A.6/A.7/A.8）
- ✗ **不**新增 `.claude/skills/<name>/INVOKE.md`（D-048 否決候選 a — 嚴禁加 26 個 INVOKE.md）
- ✗ **不**重寫既有 AGENTS.md（只擴充新段；既有內容保留不動）
- ✗ **不**寫 CI / pre-commit hook 強制檢查（屬未來 NEW_REQ_8+）

**本 task scope（嚴格限定）：**

依 TASKS v1.5 §A.12 + ARCH v1.4 §3.3.0（Multi-agent invocation 慣例）+ POST_LOCK_PENDING NEW_REQ_7 + DECISIONS_LOG v1.2 §6.10.2（D-048）。

### 任務目標

3 個產出：

1. **`AGENTS.md`（root，既有檔擴充）：** 在既有規範段後加新段「## Skill 清單與 invocation 範本（Codex ecosystem）」
2. **`CLAUDE.md`（root，新建檔）：** Anthropic Claude Code CLI 慣例自動 discovery 檔；與 AGENTS.md 新加段 90% 內容共享
3. **`_user_manual/skill_invocation_guide.md`（新建檔）：** 給 Cowork / Codex App user 的 copy-paste prompt fallback；屬 NEW_REQ_2 user_manual 範疇

### 內容規格

#### 1. AGENTS.md 擴充段

在既有 AGENTS.md 結尾**追加**（不動既有內容）下列新段：

```markdown
---

## Skill 清單與 invocation 範本（Codex ecosystem）

本 repo 含 `.claude/skills/<name>/SKILL.md` 自訂 skill 集合。對 OpenAI Codex CLI / Codex App user：本檔提供 skill discovery；agent 啟動時自動讀 AGENTS.md 取得 skill 清單，user 在 chat 內提 skill name + 對話確認，agent 從本檔對應 path 讀 SKILL.md 後執行。

### 本輪 5 skill（含中文 wrapper）

| Skill | Path | 觸發語 | 用途摘要 |
|---|---|---|---|
| init-project | .claude/skills/init-project/SKILL.md | (Codex CLI 對話確認) | 從 Template clone 建新 Instance：bootstrap `.protocol_version` + 三 registry copy + 10_art_assets/ 結構 + .gitignore |
| 初始化專案 | .claude/skills/初始化專案/SKILL.md | 同上中文 | /init-project 中文 wrapper |
| create-world | .claude/skills/create-world/SKILL.md | (Codex CLI 對話確認) | 建立世界觀（10 user-facing 議題 + §10.11 拆分 mechanic）：寫 01_world/ / 02_vocabulary/ + 對應作品 00_b |
| 建立世界觀 | .claude/skills/建立世界觀/SKILL.md | 同上中文 | /create-world 中文 wrapper |
| status | .claude/skills/status/SKILL.md | (Codex CLI 對話確認) | 列實體完成度 + 缺漏建議；純讀取 |
| 進度 | .claude/skills/進度/SKILL.md | 同上中文 | /status 中文 wrapper |
| check-gaps | .claude/skills/check-gaps/SKILL.md | (Codex CLI 對話確認) | 掃 TODO / 缺漏實體 / view/ 失效；純讀取 |
| 缺漏檢查 | .claude/skills/缺漏檢查/SKILL.md | 同上中文 | /check-gaps 中文 wrapper |

### Phase B+ skill（未實作 — 標 TBD）

預定 22 個 skill（5 個 /create-* 部分本輪 5 已完成；其他 17 個含 /iterate-* x 5、/view-* x 4、/export-* x 4、/diagnose、/integrate、/scene-task、/dialogue-write、/qa 等）將在 Phase B / C / D 落地。屆時補入本表。

### Codex CLI / Codex App invocation 範本

user 跟 agent 對話時，請按下列順序：

1. user 提 skill name（如「跑 init-project」/「我要建立世界觀」）
2. agent 讀本表對應 Path 取 SKILL.md，**完整讀完**後再對 user 確認啟動意圖
3. agent 依 SKILL.md 5 階段流程執行（不擅自跳階段、不擅自輸出邏輯）
4. 階段 4 寫檔前列出寫檔清單再確認；階段 5 驗證後印「下一步建議」

### Phase 階段對應

- Phase A（本輪）：init-project / create-world / status / check-gaps + 4 中文 wrapper
- Phase B：/create-character / /create-relationship / /create-outline / /create-detailed-outline + 對應 wrapper（B.5 / B.5b / B.6 / B.7）
- Phase C：/scene-task / /dialogue-write / /qa
- Phase D：/view-* x 4 / /export-* x 4

### 相關 spec

- _design/ARCHITECTURE.md v1.4 §3.3（skill 內容規範）+ §3.3.0（multi-agent invocation 慣例）
- _design/DECISIONS_LOG.md v1.2 §6.10.2（D-048 拍板紀錄）
- _user_manual/skill_invocation_guide.md（對 Cowork / Codex App user 的 copy-paste 範本）
```

⚠ 注意：既有 AGENTS.md 的「最高優先級規則」「文件頭格式」「狀態作用範圍」等規範段**完全保留**；新段加在原內容最後（用 `---` 分隔）。

#### 2. CLAUDE.md 新建檔（root）

新檔結構：

```markdown
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Claude Code CLI / Anthropic ecosystem agent discovery  
優先級：高

# CLAUDE.md

## 專案目的

（同 AGENTS.md「專案目的」段內容；本 repo 是商業級長篇遊戲劇本與台詞製作資料庫）

## 最高優先級規則

（同 AGENTS.md「最高優先級規則」6 條）

## 文件頭格式

（同 AGENTS.md「文件頭格式」段）

## Skill 清單與 invocation 範本（Claude Code CLI）

本 repo 含 `.claude/skills/<name>/SKILL.md` 自訂 skill 集合。Claude Code CLI 自動 discovery `.claude/skills/`；user 可直接用 slash command 觸發：

### 本輪 5 skill（slash command 表）

| Slash Command | Path | 用途 |
|---|---|---|
| /init-project | .claude/skills/init-project/SKILL.md | 建立新 Instance bootstrap |
| /初始化專案 | .claude/skills/初始化專案/SKILL.md | /init-project 中文別名 |
| /create-world | .claude/skills/create-world/SKILL.md | 建立世界觀 5 階段 |
| /建立世界觀 | .claude/skills/建立世界觀/SKILL.md | /create-world 中文別名 |
| /status | .claude/skills/status/SKILL.md | 列實體完成度 |
| /進度 | .claude/skills/進度/SKILL.md | /status 中文別名 |
| /check-gaps | .claude/skills/check-gaps/SKILL.md | 缺漏偵測 |
| /缺漏檢查 | .claude/skills/缺漏檢查/SKILL.md | /check-gaps 中文別名 |

### Phase B+ skill（未實作）

（同 AGENTS.md 對應段）

### Claude Code CLI 自動觸發

跟 Codex CLI 不同，Claude Code CLI **自動 discovery** `.claude/skills/`；user 直接用 `/init-project` 等 slash command，agent 會自動讀對應 SKILL.md 5 階段流程執行。

不需要對話確認；不需要 user 貼長 prompt 引導。

### Phase 階段對應

（同 AGENTS.md 對應段）

### 相關 spec

（同 AGENTS.md 對應段）
```

#### 3. _user_manual/skill_invocation_guide.md 新建檔

依 `_user_manual/` 既有 11 章 + 5 workflow 子檔結構：本檔可以放在 `_user_manual/04b_skill_invocation_guide.md`（屬 04 management_skills.md 補充）或直接 `_user_manual/skill_invocation_guide.md`（top-level）。CODEX 依既有 manual 結構選一個；建議放 `_user_manual/skill_invocation_guide.md` top-level（同層既有 11 章）。

新檔結構：

```markdown
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Cowork / Codex App user 的 skill copy-paste prompt 範本  
優先級：中

# Skill Invocation Guide — Cowork / Codex App user 用 copy-paste 範本

## 0. 本檔用途

對 Claude Code CLI user：slash command 直接觸發（看 CLAUDE.md）。
對 Codex CLI user：agent 自動讀 AGENTS.md 後 user 對話啟動。
**對 Cowork / Codex App user：** agent **不**自動讀 `.claude/skills/`；user 需要手動貼 prompt 引導 agent 讀對應 SKILL.md。

本檔提供每 skill 的標準 copy-paste prompt — user 一次貼，agent 即能識別 skill 並執行 SKILL.md 5 階段流程。

## 1. 使用方法

1. 找到下方對應 skill 的「給 agent 的 prompt」段
2. 整段 copy
3. 貼到 Cowork / Codex App chat 內
4. agent 自動讀 SKILL.md 後跟 user 確認啟動意圖
5. 跟 agent 對話跑完 5 階段流程

## 2. /init-project — 初始化專案

### 給 agent 的 prompt（整段 copy）

```
請讀取本 repo 內 .claude/skills/init-project/SKILL.md 的完整內容，依該檔規範執行 /init-project skill 流程。

本 skill 用於建立新 Instance repo 的 bootstrap：
- 階段 1: 對 user 詢問新專案基本資料（作品名、類型、目標長度、語氣偏好、參考作品）
- 階段 2: 列限定 00_b/00_c/00_d 微調候選
- 階段 3: user 拍板每個微調
- 階段 4: 嚴格 6 步寫檔（.protocol_version / 三 registry copy / 10_art_assets/ / .gitignore / 微調 / verify）
- 階段 5: 驗證並建議下一步 /create-world

請完整對齊 SKILL.md 規範，不擅自跳階段、不擅自微調 00_a / 00_e ~ 00_l / 01-09 模板。
```

## 3. /create-world — 建立世界觀

（同樣結構：給 agent 的 prompt + 用途摘要 + 5 階段預告）

## 4. /status — 進度查詢

（同樣結構；強調「純讀取，不寫檔」）

## 5. /check-gaps — 缺漏檢查

（同樣結構；強調「純讀取，列 4 段報告」）

## 6. 已 implemented 4 skill 對照中文 wrapper

| 英文 skill | 中文 wrapper | 觸發內容對照 |
|---|---|---|
| /init-project | /初始化專案 | 同流程，中文 description |
| /create-world | /建立世界觀 | 同流程 |
| /status | /進度 | 同流程 |
| /check-gaps | /缺漏檢查 | 同流程 |

中文 wrapper 在 Cowork 內 user 也可貼上述「給 agent 的 prompt」段（agent 對齊主 skill）。

## 7. Phase B+ skill 未實作

預定 22 個 skill 將在 Phase B / C / D 落地。屆時補入本檔。

## 8. 相關文件

- 對 Claude Code CLI user：直接用 slash command（看 `CLAUDE.md`）
- 對 Codex CLI user：看 `AGENTS.md`
- 各 skill SKILL.md 權威：`.claude/skills/<name>/SKILL.md`
- 詳細 multi-agent 慣例：`_design/ARCHITECTURE.md` v1.4 §3.3.0
```

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.5（§A.12 — 含 v1.5 partial supersede 段）
2. `_design/ARCHITECTURE.md` v1.4 §3.3 + §3.3.0（multi-agent invocation 慣例）
3. `_design/DECISIONS_LOG.md` v1.2 §6.10.2（D-048 拍板紀錄）
4. `_design/POST_LOCK_PENDING.md` v0.2 NEW_REQ_7 段

B. 對齊依據（讀取對齊）
5. 既有 `AGENTS.md`（root；完整讀；確認既有規範段保留）
6. `.claude/skills/init-project/SKILL.md`（A.5 完成）
7. `.claude/skills/create-world/SKILL.md`（A.6 完成）
8. `.claude/skills/status/SKILL.md`（A.7 完成 — 如同時平行跑；如未完成則先標 TBD「待 A.7 完成後同步補入」）
9. `.claude/skills/check-gaps/SKILL.md`（A.8 完成 — 同上）
10. `_user_manual/README.md`（manual 既有結構導讀）
11. `_user_manual/01_tool_overview.md`（既有 11 章配置）

C. 已 LOCKED 不可動文件
12. 所有 `_design/*.md`（除 POST_LOCK_PENDING 和 DECISIONS_LOG 已 v1.2 升版外都不動）
13. `scripts/*.py`
14. 既有 27 模板
15. `00_protocol/*` 全部
16. `_tools/frontend/*` 全部
17. `.claude/skills/init-project/` + `create-world/` + 對應中文 wrapper

---

**你要交付的產物：**

1. **改動 `AGENTS.md`**（既有檔擴充，**不重寫**既有內容；用 `---` 分隔加新段）
2. 新建 `CLAUDE.md`（root）
3. 新建 `_user_manual/skill_invocation_guide.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- AGENTS.md 既有規範段保留（grep 「最高優先級規則」「文件頭格式」應命中且內容未改）
- AGENTS.md 結尾新加段「## Skill 清單與 invocation 範本（Codex ecosystem）」存在
- CLAUDE.md 新檔存在 + 含 5 必填中文 header 欄位
- _user_manual/skill_invocation_guide.md 新檔存在 + 含 5 必填中文 header 欄位

B. 內容對齊
- AGENTS.md 新加段 + CLAUDE.md skill 清單一致（兩份檔 grep skill name 完全對齊）
- 對 A.7 / A.8 skill：若已完成則列；若未完成則標 TBD
- skill_invocation_guide.md 每 skill 段含「給 agent 的 prompt（整段 copy）」
- 3 份檔內容對齊 ARCH §3.3.0 規定的 4 agent 環境職責

C. 不破壞既有
- 沒動既有 27 模板 / _design 既有 spec / scripts / 00_protocol / _tools/frontend / .claude/skills/init-project / .claude/skills/create-world
- 沒新增 `.claude/skills/<name>/INVOKE.md`（D-048 否決候選 a；嚴禁）
- 既有 AGENTS.md 既有規範段內容未改（line-by-line diff 確認）
- `git diff --check` 通過

D. 對齊驗證
- `python scripts/check_headers.py` 0 ERROR 維持（baseline 15 WARN）

---

**Go / Done 判定指引：**

- **DONE：** A/B/C/D 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master
- **NO-GO：** AGENTS.md 既有內容被改動 / 新加段格式不對 → 修補 round

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.12 完成 → user commit/push → 回 master → Wave 4 三條全完成後跑 review checkpoint（建議）→ Wave 5。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.12 task 啟動包；完成後可 archive 進 `_design/archive/`
- 若 A.12 NO-GO patch round → 開 CODEX_A12_PATCH_STARTER.md
- 後續加新 skill 時必須同步更新 AGENTS.md + CLAUDE.md + skill_invocation_guide.md（屬 ARCH §3.3.0 規定）
