狀態：DEPRECATED
版本：v0.1（11th master 對話 A 落地 — 前端 follow-up 交接文件；給「frontend dialogue」承接前端後續項目；同樣用 CLAUDE_CODE_AUDIT_PROTOCOL 3-stage workflow 跟 Claude Code 對接）
最後更新：2026-06-01
適用範圍：給 user 開新 Cowork dialogue（暫稱「frontend dialogue」）承接 `_tools/frontend/` 後續工作 — 含 NEW_REQ_20 dashboard 3 finding + NEW_REQ_24 角色檔名 design + 工具角色 reframe 後 frontend 角色重塑評估；本檔屬該 dialogue 啟動入口
優先級：高

# FRONTEND_HANDOFF — 前端 follow-up 交接給 frontend dialogue

# 0. 文件目的

11th master 對話 A 完成 first-run + second-run sandbox audit cycle + 5 採納 transcribe（POST_LOCK_PENDING v0.24 §5.18）後，**前端後續工作交接給新開的 Cowork dialogue（暫稱「frontend dialogue」）**。本檔為該 dialogue 啟動入口，承載：

1. 前端目前未處理的 specific finding（NEW_REQ_20 + NEW_REQ_24）
2. 工具角色 reframe（NEW_REQ_22）對 frontend 的 implication — frontend 應如何重塑
3. 同樣用 `_sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md` 3-stage workflow 跑（AUDIT → REVIEW → APPLY）
4. Cowork frontend dialogue 與 Claude Code 對接機制
5. 本對話（11th master 對話 A）與 frontend dialogue 的工作分隔線

11th master 對話 A reframe 後角色：sandbox audit transcribe + strategic direction holder + AUDIT_2026Q2_REPORT.md 維護者。**不**接手 frontend 實作。

Frontend dialogue 接手範圍：所有 `_tools/frontend/` 相關工作 + 兩個 NEW_REQ 議題 + frontend 角色重塑評估 + 對應的 audit cycle。

---

# 1. 接手前必讀（按順序）

## 1.1 戰略上下文（理解 frontend 為什麼要 reframe）

| # | 檔 | 章節 / line | 為什麼必讀 |
|---|---|---|---|
| 1 | `_design/POST_LOCK_PENDING.md` v0.24 | §1 NEW_REQ_22（line 1149+）| 工具角色轉換戰略 + Dynamic Workflows audit 路徑；frontend reframe 的 root cause |
| 2 | `_design/POST_LOCK_PENDING.md` v0.24 | §1 NEW_REQ_20（line 965-1029）| frontend dashboard 三欄區 + module row「入口待後續 UI」3 finding；BLOCKED on NEW_REQ_22 outcome；frontend dialogue 解 block 後動手 |
| 3 | `_design/POST_LOCK_PENDING.md` v0.24 | §1 NEW_REQ_24（剛開）| 角色檔名 hyphen vs underscore design 議題；27 hyphen refs vs 13 underscore；含 Wave 14 explicit directive；frontend audit cycle 處理 candidate |
| 4 | `_design/AUDIT_2026Q2_REPORT.md` v0.1 | §1-§8 全 | 11th master 對話 A 兩 cycle 完整紀錄；frontend dialogue 接手第 N cycle 的 reference baseline |
| 5 | `_design/HANDOFF_TO_11TH_MASTER.md` v1.1 | §9 amendment + §9.5 路徑 F | 整體 11th master 戰略 + 路徑 F Stage 1-6（本 dialogue 屬 Stage 5-6 後續延伸）|

## 1.2 Workflow / Protocol（理解工作模式）

| # | 檔 | 為什麼必讀 |
|---|---|---|
| 6 | `_sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md` v0.1 | 完整 3-stage（AUDIT / REVIEW / APPLY）workflow 規格 + pre-flight + 紀律邊界 + error recovery；本 dialogue 跑前端 audit cycle 沿用此 protocol |
| 7 | `_design/SANDBOX_REFACTOR_PLAN.md` v0.1 | sandbox bootstrap 指引 + 11 audit 任務 spec base + 結論回流流程 |
| 8 | `_sandbox/SECOND_RUN_PROMPT.md` | second-run prompt 範例（reference 用；frontend cycle 寫自己的 prompt）|

## 1.3 Frontend code 現況（接手前掃一眼）

| # | 位置 / 檔 | 為什麼掃 |
|---|---|---|
| 9 | `_tools/frontend/` | 整個 frontend codebase；接手前看 directory tree 知道 scope |
| 10 | `_tools/frontend/static/js/components/ProjectDashboard.js` | NEW_REQ_20 主要對象（line 292-335 renderModuleStatus + line 337-377 renderTriColumn）|
| 11 | `_tools/frontend/server.py` | NEW_REQ_20 backend endpoint candidate（`/api/dashboard/pending-status`）|
| 12 | `_tools/frontend/static/js/state.js` | dashboard 資料流；如需要 state subscription 變更涉此檔 |
| 13 | `_tools/frontend/tests/` | 既有 frontend test；audit 期間 verify 用 |
| 14 | `.claude/skills/export-character/SKILL.md` L231 | NEW_REQ_24 Wave 14 explicit directive 原文（理解 hyphen 設計選擇歷史）|

---

# 2. Frontend follow-up 三大 scope 議題

frontend dialogue 開新 Cowork 對話時，應理解這三個 scope candidate；user 拍板實際做哪些。

## 2.1 scope A — NEW_REQ_20 dashboard 3 finding（窄 scope；明確需求）

10th master M4 user-test 發現 3 條 finding，BLOCKED on NEW_REQ_22 outcome；現在 NEW_REQ_22 first+second cycle 完成，可解 block：

| Finding | 性質 | Patch 建議（依 NEW_REQ_20 提議方案選 1）|
|---|---|---|
| F1-1 W=2 V=1 P=1 模組狀態總覽數字 | ✓ 合理（per SPEC §5.1；ENTITY_MODULES 定義）| **不動** |
| F1-2 7 個 entity row「入口待後續 UI」aria-disabled link | 設計性 placeholder | 接 `/view-*` CopyCommandButton 複製指令 — 7 個 module row 對應 7 個 view skill |
| F1-3 三欄區「Phase A 後段任務 / Phase A.0F UI 進度 / Wave 3 狀態」mock content | 規格漂移 + 資料過時 | 改寫成 UX_SPEC §11.1.6 規格：column 1「待人類裁決」+ column 2「QA Pending」+ column 3「Canon Δ Pending」+ 接 backend `/api/dashboard/pending-status` endpoint |

**估工時：** frontend 1-2h + backend 2-3h + test 1-2h = 4-7h。

**但 reframe 後須思考：** 工具角色變成 QA + 初始資料 + 專案管理；dashboard 應該強化 QA 視角（待人類裁決 / QA Pending / Canon Δ Pending 三欄正好對齊新角色）；F1-2「入口待後續 UI」改為 `/view-*` CopyCommandButton 也符合新角色（user 切外部寫作工具時複製指令過去）。**所以 scope A 的 patch 對 reframe 後角色仍有效，不算 sunk cost。**

## 2.2 scope B — NEW_REQ_24 角色檔名 design 拍板（design 議題；不是 mechanical fix）

詳 NEW_REQ_24 entry 完整 3 option pros/cons：

- Option 1 — hyphen → underscore（27 refs；含 reverse Wave 14 directive）
- Option 2 — underscore → hyphen（14 refs；modify 5 LOCKED spec）  
- Option 3 — defer / 不處理（drift 持續）

**Frontend audit cycle 期間建議：** 在 AUDIT Stage 1 加 1 task — 對 git blame `export-character/SKILL.md` L231 「Wave 14 directive」做 historical reasoning audit（Wave 14 implementer 為什麼選 hyphen？）。Stage 2 REVIEW 帶 reasoning 來決定 Option 1/2/3。

如 audit 不揭示新 reasoning → 推薦 Option 1（對齊 LOCKED spec 權威；接受 27 refs scope）。

## 2.3 scope C — frontend 全 reframe per 工具新角色（大 scope；可選；建議先 audit）

工具角色 reframe 對 frontend 11 個 Phase A.0F feature 的 implication：

| Feature | 原設計目的 | 新角色下的存廢評估 |
|---|---|---|
| F1 Project Dashboard | 整體狀態總覽 | ✓ 保留 + 強化 QA 視角（即 scope A）|
| F2 Scene Queue + Detail | 場景管理 + 寫作上下文 | ⚠ 重點變了：原為「in-tool 寫作流程指引」；新角色下變「外接寫作流程接回後 QA 入口」 |
| F3 Scene Editor + Convergence | in-tool 多版本編輯 + 收斂 | ⚠ 可能廢除 / 大改：外接寫作後 in-tool editor 失去主要 use case |
| F4 LOCKED race guard | 並發保護 | ✓ 保留（QA / 拍板期間仍需要）|
| F5 09_e 拍板紀錄 | 人類裁決流程 | ✓ 保留 + 強化（新角色核心功能）|
| F6 L3 Export Panel | 對外 export | ⚠ 可能重新定義：原為對讀者 export；新角色可能變對外接寫作工具的 export prompt 給予 |
| F7 QA finding modal | QA 8 模板 finding 展開 | ✓ 保留 + 強化（新角色核心功能）|
| F8 (其他)| ... | (依實際 codebase 評估) |

**Scope C 建議 audit-first**：跑 frontend AUDIT_PROTOCOL Stage 1 + 加 1 task「11 feature 在新角色下的存廢評估」；Stage 2 REVIEW 結論後 user 拍板。

---

# 3. Frontend dialogue 啟動指令（複製貼到新 Cowork dialogue）

```
我是 game-dialogue-bible 專案的使用者。11th master 對話 A 完成 first-run + second-run sandbox audit cycle + 5 採納 transcribe（POST_LOCK_PENDING v0.24）後，前端後續工作交接給你這條 dialogue。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「11th master frontend dialogue」承接 _tools/frontend/ 後續工作。

**第一步必讀（按順序）：**

1. _design/FRONTEND_HANDOFF.md v0.1（本檔；你的 scope）
2. _design/POST_LOCK_PENDING.md v0.24 §1 NEW_REQ_20 + NEW_REQ_22 + NEW_REQ_24（你要處理的 finding）
3. _design/AUDIT_2026Q2_REPORT.md v0.1 §1-§8（前兩 cycle 全紀錄；你接手 cycle N）
4. _sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md v0.1（3-stage workflow 規格 — 你跟 Claude Code 對接的 protocol）
5. _design/SANDBOX_REFACTOR_PLAN.md v0.1（sandbox audit 戰略落地核心檔）

**第二步精選讀（碰到才看）：**

6. _design/HANDOFF_TO_11TH_MASTER.md v1.1 §9（11th master 整體戰略 reframe）
7. _design/UX_SPEC.md v0.4 §11.1.5/§11.1.6（NEW_REQ_20 要對齊的規格）
8. _tools/frontend/static/js/components/ProjectDashboard.js（NEW_REQ_20 主要 patch 對象）
9. _tools/frontend/server.py（backend endpoint 候選）
10. .claude/skills/export-character/SKILL.md L231（NEW_REQ_24 Wave 14 explicit directive 原文）

**你的 scope：**

frontend dialogue 接手所有 _tools/frontend/ 相關工作 + 兩個 NEW_REQ 議題 + frontend 角色重塑評估 + 對應的 audit cycle。

具體 work 走以下三條路徑（user 拍板）：

- 路徑 W（窄 scope）：純 NEW_REQ_20 dashboard 3 finding patch（依 NEW_REQ_20 提議方案選 1）
- 路徑 M（中 scope）：W + NEW_REQ_24 角色檔名 design 拍板（含 audit-first reasoning collection）
- 路徑 F（全 scope）：M + scope C frontend 11 feature 全 reframe 評估（audit + 大型 refactor）

**Workflow 模式：用 CLAUDE_CODE_AUDIT_PROTOCOL.md 3-stage**

跟原 11th master 對話 A second-run 一樣的模式：

- Stage 1 AUDIT — Claude Code Dynamic Workflows 並行 audit（read-only）
- Stage 2 REVIEW — Claude Code single-agent cross-check + 採納建議 + memo
- Stage 3 APPLY — Claude Code 寫 production；Ask permissions mode；每個 edit explicit gate
- Stage 4 收尾 — append AUDIT_2026Q2_REPORT.md / POST_LOCK_PENDING 升 v0.X

**重要邊界（嚴格 scope）：**

- ✗ 不重做 LOCKED spec 設計（10 LOCKED spec / D-001~D-055 全不動，除非 user 拍板新 D-056+）
- ✗ 不擅自啟新 D-NNN 拍板（如有新議題回升 user 拍板）
- ✗ 不動 _design/POST_LOCK_PENDING.md NEW_REQ_22 entry 主體（屬 11th master 對話 A 維護；你只能 patch §5 評估紀錄總表新加 subsection）
- ✗ 不動 _design/AUDIT_2026Q2_REPORT.md §1-§8（11th master 對話 A 已寫；你 append §9+ 新 cycle 紀錄）
- ✗ 不重做 11th master 對話 A 已完成的 work
- ✓ 你可以 patch _tools/frontend/ 任何檔（你的 scope）
- ✓ 你可以開新 NEW_REQ_25+ entry 紀錄 frontend cycle 新議題
- ✓ 你可以動 CLAUDE.md / AGENTS.md frontend 相關 row（如 dashboard 完成度狀態更新）

**Cowork master（11th master 對話 A）與你的關係：**

- 11th master 對話 A 是 strategic consultant + AUDIT_2026Q2_REPORT.md 維護者
- 你（frontend dialogue）是 frontend follow-up executor + 對應 audit cycle owner
- 你跑你的 cycle；遇到「需 Cowork master 諮詢」議題（如新 D-NNN 拍板需求 / 跨 frontend boundary 設計議題）→ user 切回 11th master 對話 A 諮詢
- 你跑完 cycle 後 user 可選擇帶 cycle 結論回 11th master 對話 A 做戰略 reflect

請先回報你讀完 5 份必讀後對 scope + 三條路徑 + workflow 模式的理解，再等 user 拍板實際走哪條路徑。
```

---

# 4. 推薦路徑（給 frontend dialogue + user 拍板參考）

**推薦：路徑 M（中 scope）— 解 NEW_REQ_20 block + audit NEW_REQ_24 + 不啟動 scope C 大 refactor**

理由：

1. NEW_REQ_20 patch 對 reframe 後 dashboard 角色仍有效（QA Pending / 待人類裁決 / Canon Δ Pending 對齊新角色）→ 不算 sunk cost
2. NEW_REQ_24 design 議題現在處理時機對（frontend audit cycle 可順手 collect Wave 14 reasoning）→ 比推到下一 cycle 高 ROI
3. scope C 全 reframe 規模大（11 feature 重新設計）→ 應等實際 user 用幾週 / 跑通外接寫作 1-2 場戲後再做（更多 user evidence 支持決策）→ 不本 cycle 啟動

**反推薦：scope C 不本 cycle 啟動**

scope C 11 feature reframe 等同 Phase A.0F 重做。沒有 user 實際使用 evidence 之前重做風險高（可能設計出不符合實際需求的新 UI）。建議：

1. 本 cycle 只跑 W + audit C（不 apply C）
2. user 用幾週 + 跑通外接寫作 1-2 場戲
3. evidence 累積後決定 scope C 大小（可能只是小 patch / 可能整個重做）

---

# 5. Frontend dialogue 第一階段建議工作流（依路徑 M）

## 5.1 Pre-flight（依 CLAUDE_CODE_AUDIT_PROTOCOL §2）

```powershell
cd D:\劇本開發工具

# verify production git 狀態乾淨
git status --short

# 重 bootstrap sandbox（11th master 對話 A 後可能 stale；不重 bootstrap audit 會報已修議題）
rm -r -force _sandbox\snapshot, _sandbox\audit-reports, _sandbox\review-reports, _sandbox\apply-reports 2>$null
mkdir _sandbox\snapshot, _sandbox\audit-reports, _sandbox\review-reports, _sandbox\apply-reports
robocopy . _sandbox\snapshot /E /XD .git _sandbox node_modules .venv __pycache__ /XF *.pyc

# pre-cycle git commit snapshot
git log -1 --format="%H" > _sandbox\PRE_CYCLE_COMMIT.txt
```

## 5.2 Stage 1 AUDIT — frontend cycle 第一輪建議 task

| Task | scope | 對應 NEW_REQ |
|---|---|---|
| F-A1 — `_tools/frontend/` codebase dead code / unused module audit | _tools/frontend/ 全掃 | 通用前端 cleanup（無對應 NEW_REQ）|
| F-A2 — ProjectDashboard.js NEW_REQ_20 三 finding cross-check production state | line 292-335 + 337-377 | NEW_REQ_20 |
| F-A3 — server.py 與 frontend state.js cross-ref drift | server.py + state.js | NEW_REQ_20 dependent |
| F-B1 — `角色檔名 hyphen vs underscore` 全 repo scan + git blame reasoning | 全 repo .md/.py + export-character/SKILL.md history | NEW_REQ_24（含 reasoning collection）|
| F-C1 — 11 Phase A.0F feature 在新角色下的存廢評估（read-only；不 apply）| 全 frontend + UX_SPEC §11 | scope C audit-only |

估 token：~200K-400K / 耗時 ~25-50 分。

## 5.3 Stage 2 REVIEW — Claude Code single-agent

依 CLAUDE_CODE_AUDIT_PROTOCOL §4 prompt 範本 + 跑 5 task review；產出 REVIEW report。

## 5.4 Stage 3 APPLY — Ask permissions mode

依 CLAUDE_CODE_AUDIT_PROTOCOL §5 prompt 範本 + Ask permissions mode + 每個 edit explicit gate。

## 5.5 Stage 4 收尾

- append AUDIT_2026Q2_REPORT.md §9 (frontend cycle N)
- POST_LOCK_PENDING.md 升 v0.25 加新 §5.20 + 視需要新 NEW_REQ_25+
- GIT SUMMARY 給 user 手動 commit + push

---

# 6. 與 11th master 對話 A 的工作分隔線

| 內容 | 11th master 對話 A | frontend dialogue |
|---|---|---|
| sandbox audit cycle 主檔（11 audit task spec）| ✓ 維護 SANDBOX_REFACTOR_PLAN | 沿用；可加 frontend-specific task spec patch |
| AUDIT_2026Q2_REPORT.md §1-§8 | ✓ 維護 + 不動 | 不動；append §9+ 新 cycle |
| POST_LOCK_PENDING.md NEW_REQ_22 entry 主體 | ✓ 維護 | 不動；可加 §5 新 subsection 紀錄 frontend cycle |
| POST_LOCK_PENDING.md NEW_REQ_20 entry | 不動 | ✓ 處理（標 RESOLVED via frontend cycle）|
| POST_LOCK_PENDING.md NEW_REQ_24 entry | 不動 | ✓ 處理（apply 任 option）|
| POST_LOCK_PENDING.md 新 NEW_REQ_25+ | 諮詢角色 | ✓ 開新 entry |
| _tools/frontend/ | 不動 | ✓ patch / refactor |
| CLAUDE.md / AGENTS.md frontend 相關 row | 諮詢 | ✓ patch（如 dashboard 完成度）|
| 10 LOCKED spec | 不動 | 不動（除非 user 拍板新 D-056+）|
| 既有 51 SKILL.md / 27 模板 / 9 QA 模板 / 3 registry | 不動 | 不動（除非新 D-NNN）|

---

# 7. user 啟動 frontend dialogue 流程

1. **打開新 Cowork 對話**（不要在 11th master 對話 A 內跑 frontend；分離 context）
2. **複製 §3 整段啟動指令** 貼進新對話對話欄
3. 等 frontend dialogue master 回報「讀完 5 份必讀 + 對 scope + 三路徑 + workflow 模式的理解」
4. **拍板路徑** W / M（推薦）/ F
5. 依拍板路徑跑 Stage 1 AUDIT（user 在 Claude Code 跑）
6. 帶 audit report 回 frontend dialogue 跑 Stage 2 REVIEW
7. user 拍板 each finding → Stage 3 APPLY
8. 跑完 cycle 給 frontend dialogue 寫 §4 收尾 + GIT SUMMARY
9. user commit + push 收尾

---

# 8. Cross-ref

- `_design/POST_LOCK_PENDING.md` v0.24（NEW_REQ_20 / NEW_REQ_22 / NEW_REQ_24 / §5.16-§5.19；frontend dialogue 處理 NEW_REQ_20 + NEW_REQ_24，不動 NEW_REQ_22 主體）
- `_design/AUDIT_2026Q2_REPORT.md` v0.1（§1-§8 11th master 對話 A 兩 cycle 完整紀錄；frontend dialogue append §9 新 cycle）
- `_sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md` v0.1（3-stage workflow protocol；frontend dialogue 沿用此 protocol 跑 audit cycle）
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（sandbox 戰略落地核心檔；可能需要 patch 加 frontend-specific audit task）
- `_design/HANDOFF_TO_11TH_MASTER.md` v1.1 §9（11th master 整體戰略 + 路徑 F；frontend dialogue 屬該路徑延伸）
- `_design/UX_SPEC.md` v0.4 §11（11 Phase A.0F feature 規格；frontend dialogue 對齊用）
- `_tools/frontend/` 全目錄（frontend dialogue 主要 patch 對象）
- `.claude/skills/export-character/SKILL.md` L231（NEW_REQ_24 Wave 14 directive 原文）

---

# 9. 文件維護紀律

- 本檔屬 11th master 對話 A 落地交接文件；frontend dialogue 接手後**不需要更新本檔**
- 若 frontend dialogue 發現本檔不準確 → 標 errata 在 frontend cycle §4 收尾紀錄
- frontend cycle 跑通後可把本檔 archive 進 `_design/archive/`（或 frontend dialogue 寫類似 HANDOFF_TO_NEXT_FRONTEND_DIALOGUE.md 等）
- 11th master 對話 A 後續若需要 patch 本檔 → 升 v0.X+1 + 透過 11th master 對話 A 路徑

---

**11th master 對話 A → frontend dialogue 完整交接 → frontend dialogue 跑 cycle → cycle 收尾後 user 可選擇帶結論回 11th master 對話 A 戰略 reflect 或繼續 frontend follow-up cycle。**
