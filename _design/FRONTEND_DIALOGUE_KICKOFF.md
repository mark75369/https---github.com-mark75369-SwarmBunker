狀態：DRAFT
版本：v0.1（從 FRONTEND_HANDOFF.md §3 抽取 + 補 Dynamic Workflows Stage 1 並行 audit 任務分派；交付給 Claude Code）
最後更新：2026-06-01
適用範圍：交付給 Claude Code 用 Dynamic Workflows 跑 frontend follow-up audit cycle 的啟動指令；user 開新對話/啟動 Claude Code 時直接複製本檔內容
優先級：高

# FRONTEND_DIALOGUE_KICKOFF — 交付 Claude Code（Dynamic Workflows）

> 用法：本檔 §A 是給「frontend dialogue」master 的啟動指令；§B 是把 Stage 1 AUDIT 拆成 Dynamic Workflows 並行子任務的派工表，直接交給 Claude Code 執行。先讀 §0 注意事項。

---

# 0. 交付前注意事項（重要）

1. **缺檔警告：** 啟動指令原本列為必讀 #4 的 `_sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md` 與精選讀 #8 的 `_sandbox/SECOND_RUN_PROMPT.md` **目前不存在**。`/_sandbox/` 已被 `.gitignore` 排除且已清空（git 歷史中也沒有）。在跑 Stage 1 之前，需先用 `_design/SANDBOX_REFACTOR_PLAN.md`（這份在 git 裡、仍存在）重建 3-stage workflow 規格，或請 11th master 對話 A 補回 protocol 檔。本檔 §B 已把 Stage 1 的 3-stage 精神內聯，可在 protocol 缺檔時暫時頂用。
2. **執行位置：** Dynamic Workflows audit 在 `_sandbox/snapshot/` 內跑（read-only 快照），不要直接動 production。Pre-flight 重 bootstrap 見 §C。
3. **路徑拍板：** 啟動後等 master 回報理解，再由 user 拍板路徑 W / M（推薦）/ F。§B 的派工表預設為**路徑 M**。

---

# A. 啟動指令（複製貼到新 Cowork 對話 / 交給 Claude Code）

```
我是 game-dialogue-bible 專案的使用者。11th master 對話 A 完成 first-run + second-run sandbox audit cycle + 5 採納 transcribe（POST_LOCK_PENDING v0.24 §5.18）後，前端後續工作交接給你這條 dialogue。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「11th master frontend dialogue」承接 _tools/frontend/ 後續工作。

第一步必讀（按順序）：
1. _design/FRONTEND_HANDOFF.md v0.1（你的 scope 入口）
2. _design/POST_LOCK_PENDING.md v0.24 §1 NEW_REQ_20 + NEW_REQ_22 + NEW_REQ_24（你要處理的 finding）
3. _design/AUDIT_2026Q2_REPORT.md v0.1 §1-§8（前兩 cycle 全紀錄；你接手 cycle N）
4. _design/SANDBOX_REFACTOR_PLAN.md v0.1（sandbox audit 戰略落地核心檔 + 3-stage workflow base）
   ※ 注意：原列的 _sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md 目前缺檔（sandbox 已清），3-stage 規格改以本檔 + KICKOFF §B 為準。

第二步精選讀（碰到才看）：
5. _design/HANDOFF_TO_11TH_MASTER.md v1.1 §9（11th master 整體戰略 reframe）
6. _design/UX_SPEC.md v0.4 §11.1.5/§11.1.6（NEW_REQ_20 要對齊的規格）
7. _tools/frontend/static/js/components/ProjectDashboard.js（NEW_REQ_20 主要 patch 對象，line 292-335 + 337-377）
8. _tools/frontend/server.py（backend endpoint 候選 /api/dashboard/pending-status）
9. .claude/skills/export-character/SKILL.md L231（NEW_REQ_24 Wave 14 directive 原文）

你的 scope：
接手所有 _tools/frontend/ 相關工作 + NEW_REQ_20 + NEW_REQ_24 兩議題 + frontend 角色重塑評估 + 對應 audit cycle。三條路徑由 user 拍板：
- 路徑 W（窄）：純 NEW_REQ_20 dashboard 3 finding patch
- 路徑 M（中，推薦）：W + NEW_REQ_24 角色檔名 design 拍板（含 audit-first reasoning collection）
- 路徑 F（全）：M + frontend 11 feature 全 reframe 評估（audit + 大型 refactor）

Workflow 模式：3-stage（用 Claude Code Dynamic Workflows 跑 Stage 1）
- Stage 1 AUDIT — Dynamic Workflows 並行子代理 audit（read-only；派工表見 KICKOFF §B）
- Stage 2 REVIEW — single-agent cross-check + 採納建議 + memo
- Stage 3 APPLY — 寫 production；Ask permissions mode；每個 edit explicit gate
- Stage 4 收尾 — append AUDIT_2026Q2_REPORT.md §9 + POST_LOCK_PENDING 升 v0.25 + GIT SUMMARY

重要邊界（嚴格 scope）：
- ✗ 不重做 10 LOCKED spec / D-001~D-055（除非 user 拍板新 D-056+）
- ✗ 不擅自啟新 D-NNN 拍板（有新議題回升 user）
- ✗ 不動 POST_LOCK_PENDING NEW_REQ_22 entry 主體 + AUDIT_2026Q2_REPORT §1-§8（屬 11th master 對話 A；你只能 append）
- ✗ 不重做 11th master 對話 A 已完成的 work
- ✓ 可 patch _tools/frontend/ 任何檔
- ✓ 可開新 NEW_REQ_25+ entry
- ✓ 可動 CLAUDE.md / AGENTS.md frontend 相關 row（如 dashboard 完成度）

請先回報你讀完必讀後對 scope + 三條路徑 + workflow 模式的理解，再等 user 拍板實際走哪條路徑。
```

---

# B. Stage 1 AUDIT — Dynamic Workflows 並行派工表（預設路徑 M）

> 交給 Claude Code：在 `_sandbox/snapshot/` 內，用 Dynamic Workflows 開以下並行子代理任務，全部 **read-only**（只讀、只產 audit report，不寫 production）。每個子任務輸出一份 markdown audit report 到 `_sandbox/audit-reports/`。

| 子任務 ID | scope（讀取範圍） | 要查什麼 | 對應 NEW_REQ | 輸出 report |
|---|---|---|---|---|
| **F-A1** | `_tools/frontend/` 全目錄 | dead code / 未使用 module / 殘留 alpha placeholder 盤點 | 通用 cleanup | `audit-F-A1-deadcode.md` |
| **F-A2** | `ProjectDashboard.js` line 292-335（renderModuleStatus）+ 337-377（renderTriColumn） | NEW_REQ_20 三 finding 對 production 現況 cross-check：F1-1 數字是否合理 / F1-2 七個 entity row「入口待後續 UI」現狀 / F1-3 三欄區 mock content 與 UX_SPEC §11.1.6 落差 | NEW_REQ_20 | `audit-F-A2-dashboard.md` |
| **F-A3** | `server.py` + `static/js/state.js` | backend endpoint `/api/dashboard/pending-status` 是否存在 / dashboard 資料流 drift / state subscription 影響面 | NEW_REQ_20 dependent | `audit-F-A3-backend-state.md` |
| **F-B1** | 全 repo `.md`/`.py` + `.claude/skills/export-character/SKILL.md` git blame | 角色檔名 hyphen `角色-<name>` vs underscore `角色_<name>` 全 scan（統計 refs）+ git blame L231 Wave 14 directive 的 historical reasoning | NEW_REQ_24（reasoning collection） | `audit-F-B1-filename.md` |
| **F-C1** | 全 frontend + `UX_SPEC.md` §11 | 11 個 Phase A.0F feature 在「工具新角色（QA + 初始資料 + 專案管理 + 外接寫作）」下的存廢評估（**read-only；只評估不 apply**） | scope C audit-only | `audit-F-C1-reframe.md` |

估算：~200K-400K token / ~25-50 分。

**Stage 1 完成準則：** 5 份 audit report 全產出於 `_sandbox/audit-reports/`，每份含「現況事實 / finding / 建議（但不 apply）」三段。完成後帶 report 回 frontend dialogue 跑 Stage 2 REVIEW。

---

# C. Pre-flight（跑 Stage 1 前；PowerShell）

```powershell
cd D:\劇本開發工具

# 1. verify production git 狀態乾淨
git status --short

# 2. 重 bootstrap sandbox（避免拿 stale 快照 audit 報已修議題）
rm -r -force _sandbox\snapshot, _sandbox\audit-reports, _sandbox\review-reports, _sandbox\apply-reports 2>$null
mkdir _sandbox\snapshot, _sandbox\audit-reports, _sandbox\review-reports, _sandbox\apply-reports
robocopy . _sandbox\snapshot /E /XD .git _sandbox node_modules .venv __pycache__ /XF *.pyc

# 3. pre-cycle commit snapshot
git log -1 --format="%H" > _sandbox\PRE_CYCLE_COMMIT.txt
```

---

# D. 後續 Stage 流程（摘要）

- **Stage 2 REVIEW** — Claude Code single-agent 跨查 5 份 audit report + 帶 reasoning 對每個 finding 給採納建議 + 寫 REVIEW memo 到 `_sandbox/review-reports/`。NEW_REQ_24 在此決定 Option 1（hyphen→underscore，推薦對齊 LOCKED spec）/ 2 / 3。
- **Stage 3 APPLY** — Ask permissions mode；user 逐 finding 拍板後才寫 production；每個 edit explicit gate。
- **Stage 4 收尾** — append `AUDIT_2026Q2_REPORT.md` §9（frontend cycle N）+ `POST_LOCK_PENDING.md` 升 v0.25（NEW_REQ_20 標 RESOLVED / NEW_REQ_24 標 apply 結果 / 視需要開 NEW_REQ_25+）+ 產 GIT SUMMARY 給 user 手動 commit + push。

---

# E. Cross-ref

- 來源：`_design/FRONTEND_HANDOFF.md` v0.1 §3（啟動指令）+ §5.2（Stage 1 task）+ §5.1（pre-flight）
- `_design/POST_LOCK_PENDING.md` v0.24（NEW_REQ_20 / NEW_REQ_22 / NEW_REQ_24）
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（3-stage workflow base；protocol 缺檔時的權威來源）
- `_design/AUDIT_2026Q2_REPORT.md` v0.1（§1-§8 前兩 cycle；append §9）
