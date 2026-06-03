狀態：DEPRECATED
版本：v0.2（11th master 對話 A reframe 戰略落地 partial supersede — header note + 新增 §0.5 並行模式廢止紀錄 — 對話 A 跑到 NEW_REQ_20 patch 一半時 user reframe 11th master scope 成「工具角色轉換 + Claude Code Dynamic Workflows audit 路徑」；對話 B + C 退場；本 setup 包 §1-§5 內容仍可作為「並行模式設計參考」歷史紀錄；對應 NEW_REQ_22 + SANDBOX_REFACTOR_PLAN v0.1 + HANDOFF_TO_11TH_MASTER v1.1 §9 + POST_LOCK_PENDING v0.22；本檔 v0.1 → v0.2）
歷史紀錄：v0.1（10th master 第十輪整合對話收尾後 11+ 輪 master 並行模式 setup 包；user 拍板選甲 1（新建 separate Instance repo）+ 甲 b（Codex CLI 量產對話）；3 個並行對話分割：Cowork A 前端 NEW_REQ_20 patch / Cowork B M4 user-test follow-up / Codex CLI C 量產台詞）
最後更新：2026-06-01
適用範圍：⚠ **本 setup 包並行模式已廢止**（詳 §0.5；對話 A reframe / 對話 B C 退場）；§1-§5 內容保留為歷史紀錄 + 並行模式設計參考；後續 master 接手 reference HANDOFF_TO_11TH_MASTER v1.1 §9 新路徑 F + SANDBOX_REFACTOR_PLAN v0.1
優先級：低（已廢止之歷史 setup 包；Batch 5 補齊缺漏 header 欄位，內容不動）

# HANDOFF_11TH_PARALLEL_SETUP — 11+ 輪 master 並行模式 setup 包

# 0. 文件目的

10th master 第十輪整合對話完成 Milestone 4 真正封版宣告 + NEW_REQ_20 紀錄後，user 拍板採並行模式：

- 對話 A：Claude Cowork — 跑 NEW_REQ_20 frontend patch（11th master sub-scope 1；3-5 小時 master 對話時間）
- 對話 B：Claude Cowork — 跑 M4 user-test follow-up（11th master sub-scope 2；持續 monitor 量產期間 finding；隨時可開隨時可暫停）
- 對話 C：Codex CLI — user 親跑量產台詞 skill chain（讀 AGENTS.md skill 清單；持續使用直到一場戲完整跑通）

三對話互不直接溝通；user 是中央協調者。三對話動的目錄完全分離，git commit 不衝突。

本檔提供：(1) user bootstrap 指令（5-10 分一次性 setup）+ (2) 3 對話的完整啟動 prompt（user 直接複製貼到各對話）+ (3) 並行協調機制 + (4) 推薦執行順序。

---


# 0.5 11th master 對話 A reframe 後 — 並行模式廢止紀錄（v0.2 新增）

⚠ **本 setup 包 §1-§5 規劃的並行模式已廢止。**

## 0.5.1 廢止背景

11th master 對話 A（Cowork）依本 setup 包 §2 啟動 prompt 開跑 NEW_REQ_20 frontend patch 6 步驟到一半時，user 觀察到並 reframe 11th master scope：

- 工具 A 寫作 pipeline 受 base model 品質 ceiling 限制
- 11+ 輪累積 tech debt 規模大（含本檔 §1.1 master ref 對齊操作期間 commit 235debb 對 POST_LOCK_PENDING §5.3-§5.12 意外截斷 ~110 行設計史；屬「並行模式 setup 同期 manifest」的副作用 finding 之一）
- frontend dashboard 三欄區 patch 屬「為短期 polish 做的 work 可能被覆蓋」

結論：工具 A 後續定位 = QA + 初始資料建置 + 專案管理 + 外接寫作；用 Claude Code Dynamic Workflows 跑 sandbox 大重構（詳 NEW_REQ_22 + SANDBOX_REFACTOR_PLAN v0.1）。

## 0.5.2 三對話 scope 退場 / reframe

| 對話 | 原本 scope（v0.1）| v0.2 reframe 後狀態 |
|---|---|---|
| A Cowork frontend patch | 跑 NEW_REQ_20 6 步驟 | **reframe**；改成「寫戰略落地交接文件 + 後續 REVIEW Claude Code 產出」；6-task 包：SANDBOX_REFACTOR_PLAN v0.1 + POST_LOCK_PENDING v0.22 + HANDOFF_TO_11TH_MASTER v1.1 + 本 HANDOFF v0.2 + 根 .gitignore + _sandbox/README.md |
| B Cowork M4 user-test follow-up | 跑 NEW_REQ_14 §6 補入 + 紀錄 finding | **退場**（如尚未開）；M4 user-test 屬「為將被替換的 in-tool 寫作 pipeline 做 test」ROI 大降；推延到大重構完成 + 工具新角色定型後再跑；機制本身保留 |
| C Codex CLI 量產台詞 | 跑 1-2 場戲 skill chain 量產 | **退場**（如尚未開）；外接寫作後此量產 path 即將被替換 |

## 0.5.3 §5 並行協調機制廢止

§5 並行協調機制（三對話資料夾分工 / 衝突風險點 / user 拍板時機 / commit + push 順序）整段廢止。三對話資料夾衝突風險不再存在（因為三對話都不跑）。

新單對話模式：**單對話 A（Cowork）戰略落地 + user 親跑 Claude Code sandbox audit + master REVIEW 路徑**。

詳 `_design/HANDOFF_TO_11TH_MASTER.md` v1.1 §9.5 新路徑 F（Sandbox Dynamic Workflows audit 路徑 Stage 1-6）。

## 0.5.4 §1 user bootstrap 部分有效性

§1 user bootstrap 指令仍部分有效：

| §1 子節 | v0.2 後狀態 |
|---|---|
| §1.1 master ref 對齊（git merge frontend-tools-a0f → master） | **仍有效**；user 可在 11th master 對話 A 戰略落地 6-task 包 commit 後跑 |
| §1.2 建 separate Instance repo（git clone Writing-tools.git → D:\劇本開發工具-test） | **退場**；對話 C 退場後不需要 Instance repo；user 可不 bootstrap 或保留現有 Instance repo 作為未來參考 |
| §1.3 移除 .template_root | **退場**；對應 §1.2 退場 |
| §1.4 確認 setup 完成 | **退場**；對應 §1.2/§1.3 退場 |

## 0.5.5 新 user bootstrap（替代 §1）

11th master 對話 A 戰略落地 6-task 包 commit 後，user 跑 SANDBOX 新 bootstrap（詳 `_design/SANDBOX_REFACTOR_PLAN.md` §2.2 PowerShell 指令）：

```powershell
cd D:\劇本開發工具

# 建 sandbox 子目錄
mkdir _sandbox
mkdir _sandbox\snapshot
mkdir _sandbox\audit-reports

# cp production 內容進 snapshot（推薦 robocopy）
robocopy . _sandbox\snapshot /E /XD .git _sandbox node_modules .venv __pycache__ /XF *.pyc

# verify
cd _sandbox\snapshot
ls _design\ | Measure-Object
test-path .git    # 應該 False

# 回 production 跑 git status verify .gitignore 排除生效
cd D:\劇本開發工具
git status   # 應該看不到 _sandbox/ 條目
```

然後切 Claude Code 跑 first-run audit（A1 + B4 + C1）。

## 0.5.6 Cross-ref

- `_design/HANDOFF_TO_11TH_MASTER.md` v1.1 §9（reframe amendment；本 §0.5 對應）
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（新 bootstrap 指引 + 11 audit 任務 spec + first-run 建議）
- `_design/POST_LOCK_PENDING.md` v0.22（NEW_REQ_22 + §5.13-§5.15）
- 根 `.gitignore`（11th master 對話 A 新建；加 `/_sandbox/` 排除）
- `_sandbox/README.md`（11th master 對話 A 新建）
- §1.1 master ref 對齊操作期間 commit 235debb manifest（CLAUDE.md 教訓 6 truncation；詳 POST_LOCK_PENDING §5.15 audit trail）

---
# 1. user bootstrap 指令（一次性；5-10 分）

## 1.1 master ref 對齊（先把 10th master 全成果 merge 到 master）

```powershell
cd D:\劇本開發工具
git status
```

預期看到 `M _design/POST_LOCK_PENDING.md` + 6 個 CRLF false-dirty + `??  _design/HANDOFF_11TH_PARALLEL_SETUP.md`（本檔；待你 add）。

```powershell
git add _design\POST_LOCK_PENDING.md _design\HANDOFF_11TH_PARALLEL_SETUP.md

git diff --cached --stat
```

預期 2 檔 staged（POST_LOCK_PENDING v0.20 + 新 setup 包）。

```powershell
git commit -m "10th master M4 user-test follow-up + 11+ 輪並行 setup 包：

- POST_LOCK_PENDING v0.19 → v0.20 partial supersede：新增 NEW_REQ_20（Phase A.0F F1 Dashboard 三欄區 spec drift + data 過時 + 入口待後續 UI；推 11+ 輪 master patch）+ §5.11 評估 + §5.12 紀律
- 新增 HANDOFF_11TH_PARALLEL_SETUP v0.1：user 拍板選甲 1 + 甲 b 並行模式；含 user bootstrap 指令 + 3 對話啟動 prompt（Cowork A 前端 patch / Cowork B M4 user-test follow-up / Codex CLI C 量產）+ 並行協調機制

baseline 維持：check_headers 0/56 / check_paths 247/1 / build_repo_index 0/92"

git push origin frontend-tools-a0f
```

push 完成後對齊 master：

```powershell
git checkout master
git merge frontend-tools-a0f
git push origin master
```

merge 完成後 master 含全部 10th master 成果 + Milestone 4 真正封版宣告 + NEW_REQ_20 + 本 setup 包。

## 1.2 建 separate Instance repo

```powershell
cd D:\
git clone https://github.com/mark75369/Writing-tools.git 劇本開發工具-test
cd D:\劇本開發工具-test
```

verify clone 完成：

```powershell
git status
git log --oneline -3
```

預期看到 `On branch master` + latest commit 是你剛 push 的「10th master M4 user-test follow-up + 11+ 輪並行 setup 包」（或 merge commit）。

## 1.3 移除 Template marker（準備跑 /init-project）

```powershell
del .template_root
git status
```

預期看到 `deleted: .template_root`。

**注意：** 暫不 commit 這個 deletion；先讓 /init-project 跑完看是否 agent 會處理。如果 agent 沒 handle，後續手動 commit。

## 1.4 確認 setup 完成

```powershell
ls _design\HANDOFF_TO_11TH_MASTER.md
ls _design\HANDOFF_11TH_PARALLEL_SETUP.md
ls _design\PHASE_D_COMPLETION_REPORT.md
ls _design\POST_LOCK_PENDING.md
```

4 個檔都存在 → 你準備好開 3 個對話。

---

# 2. 對話 A：Claude Cowork — NEW_REQ_20 frontend patch

## 2.1 用途

11th master sub-scope 1 — 把 F1 Dashboard 三欄區 spec drift + 入口待後續 UI placeholder patch 對齊 UX_SPEC §11.1.6 status snapshot。預估工時：frontend 1-2h + backend 2-3h + test 1-2h = 4-7h 累計。

## 2.2 啟動 prompt（複製整段貼到新 Claude Cowork 對話）

```
我是 game-dialogue-bible 專案的使用者。10th master 第十輪整合對話完成 Milestone 4 真正封版宣告（commit 2fc21f8）+ NEW_REQ_20 紀錄 F1 Dashboard 3 條 finding（POST_LOCK_PENDING v0.20）。

user 拍板採並行模式：你跑這條對話 NEW_REQ_20 frontend patch；同時 user 在 Codex CLI 對話跑量產台詞。詳 _design/HANDOFF_11TH_PARALLEL_SETUP.md §2。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「11th master 對話 A — frontend patch sub-scope」。

**第一步必讀（按順序，5 份）：**

1. _design/HANDOFF_11TH_PARALLEL_SETUP.md（並行 setup 包；§2 是你的 scope）
2. _design/HANDOFF_TO_11TH_MASTER.md v1.0（11th master 整體 scope；§3 路徑 B + §4 紀律仍適用）
3. _design/POST_LOCK_PENDING.md v0.20 §1 NEW_REQ_20 entry（你要處理的 finding；含完整提議方案 3 選 + 推薦選 1）
4. _design/UX_SPEC.md v0.4 §11.1.5 模組狀態總覽 + §11.1.6 三欄區（要對齊的規格）
5. _design/PHASE_D_COMPLETION_REPORT.md v1.1 §10.6 封版紀律確認（紀律框架）

**第二步精選讀（碰到才看）：**

6. _tools/frontend/static/js/components/ProjectDashboard.js（要 patch 的主檔；line 292-335 renderModuleStatus + line 337-377 renderTriColumn）
7. _tools/frontend/server.py（要加 endpoint 的 backend）
8. _tools/frontend/static/js/state.js（dashboard 資料流；如有需要）
9. _design/DECISIONS_LOG.md v2.0（D-001~D-054 全 LOCKED；不動）

**你的 scope（嚴格限定）：**

跑 NEW_REQ_20 提議方案選 1（推薦；完整 patch + 接 backend）：

1. 改寫 ProjectDashboard.js line 339-353 renderTriColumn() 三欄
   - column 1 從「Phase A 後段任務」改成「待人類裁決 / Pending Human Decisions」+ 反查 09_e 待裁決紀錄 bullet list + action「跳轉 09_e 編輯入口」或 placeholder if 09_e edit UI 未實作
   - column 2 從「Phase A.0F UI 進度」改成「QA Pending」+ 反查 09_a-i 未跑場景 bullet list + action「複製 /qa <scene_id> 指令」CopyCommandButton
   - column 3 從「Wave 3 狀態」改成「Canon Δ Pending」+ 反查 Canon Delta 候選清單 bullet list + action「跳轉 Canon Delta」或 placeholder（屬成熟期功能 framework reference）

2. 在 server.py 新增 endpoint 反查 status data：
   - /api/dashboard/pending-status 回傳 JSON: { "pending_hd": [...], "qa_pending": [...], "canon_delta_pending": [...] }
   - pending_hd：掃 09_e 模板找 status: pending 紀錄
   - qa_pending：掃 06_a 場景索引找未跑 QA 報告的 S-*-* 場景
   - canon_delta_pending：placeholder（Canon Delta 真正實作屬 13+ 輪 scope；此 endpoint 暫回空陣列 + warning note）

3. 改 ProjectDashboard.js 各 module row 「入口待後續 UI」action（line 325）為更友善 placeholder：
   - 接 CopyCommandButton 複製對應 /view-<module> 指令（如 /view-world / /view-character / /view-outline / /view-detailed-outline）
   - 7 個 entity row 對應 7 個 module；C / R 用 generic 「複製 /view-character <name>」（user 自己填 name）

4. 跑 unit test verify：
   - cd _tools/frontend
   - python -m pytest tests/（如有 dashboard 相關 test 看是否仍 PASS）
   - 啟動 server 跑 python server.py --port 8765；瀏覽器 localhost:8765 視覺 verify 三欄區內容對齊 UX_SPEC §11.1.6

5. 跑 baseline verify：
   - python -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
   - python -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
   - python -X utf8 -B -c "import sys; sys.path.insert(0, 'scripts'); from parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('build_repo_index ERROR:', len([i for i in r.issues if i.severity == 'ERROR']), 'WARN:', len([i for i in r.issues if i.severity == 'WARN']))"
   - 對齊 10th master baseline 範圍：check_headers ≤ 60 WARN / check_paths ≤ 247 ERROR / build_repo_index ≤ 100 WARN

6. patch 完成後寫 POST_LOCK_PENDING v0.20 → v0.21 partial supersede：
   - NEW_REQ_20 標 ✅ RESOLVED
   - §5.11 NEW_REQ_20 紀錄補入 patch 落地紀錄
   - 升 v0.21 header note

**重要邊界（嚴格 scope）：**

- ✗ 不改任何 LOCKED spec / registry / parser code（10 LOCKED spec 全不動）
- ✗ 不改 D-001~D-054 拍板結論
- ✗ 不改 00_protocol / 既有 27 模板 / 既有 51 SKILL.md 任何檔
- ✗ 不動 Instance 內容（Instance 在 D:\劇本開發工具-test\；你在 D:\劇本開發工具\ 即 Template repo）
- ✗ 不跑量產 skill（屬對話 C 範圍）
- ✗ 不擅自啟新 D-NNN 拍板

**並行協調機制：**

- 你動 _tools/frontend/ 目錄 + POST_LOCK_PENDING.md；不會跟對話 C（動 Instance repo）撞檔
- 你需要 user 拍板時 → 印「需要 user 拍板」清單；user 從量產對話切過來看
- 你 patch 完 + commit 完成 → 通知 user；user 重啟 frontend server 視覺 verify

**完成條件：**

✓ ProjectDashboard.js 三欄區對齊 UX_SPEC §11.1.6（待人類裁決 / QA Pending / Canon Δ Pending）
✓ server.py /api/dashboard/pending-status endpoint 落地（即使 stub 也可）
✓ 7 個 module 「入口待後續 UI」改成 /view-* CopyCommandButton 或友善 placeholder
✓ frontend unit test PASS
✓ baseline 維持範圍內
✓ POST_LOCK_PENDING v0.20 → v0.21 partial supersede NEW_REQ_20 標 RESOLVED
✓ GIT SUMMARY 給 user（user 手動 commit + push）

請先回報你讀完 5 份必讀後對 scope + 6 個 patch 步驟的理解，再開始處理。
```

## 2.3 完成條件 + 收尾

對話 A 完成 = 6 patch 步驟全 ✓ + POST_LOCK_PENDING v0.21 + user push 完成。

---

# 3. 對話 B：Claude Cowork — M4 user-test follow-up

## 3.1 用途

11th master sub-scope 2 — 持續監控 user 量產期間發現的 finding；跟對話 C（Codex CLI 量產）配對協同；發現新 finding 時記錄為 NEW_REQ_21+ 或標 PHASE_D §6 補入機制 candidate。預估工時：依量產時間而定；可隨時開隨時暫停。

## 3.2 啟動 prompt（複製整段貼到新 Claude Cowork 對話）

```
我是 game-dialogue-bible 專案的使用者。10th master 第十輪整合對話完成 Milestone 4 真正封版宣告（commit 2fc21f8）。

user 拍板採並行模式：你跑這條對話 M4 user-test follow-up（紀錄量產期間 finding + 觸發 NEW_REQ_14 §6 補入機制 candidate）；同時 user 在 Codex CLI 對話跑量產台詞（對話 C）；另一條 Claude Cowork 對話 A 跑 NEW_REQ_20 frontend patch。詳 _design/HANDOFF_11TH_PARALLEL_SETUP.md §3。

工作資料夾：D:\劇本開發工具（Template repo；只動 _design/ POST_LOCK_PENDING 或新 NEW_REQ entry）+ D:\劇本開發工具-test\（Instance repo；只讀；不寫；user 量產的場域）

GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「11th master 對話 B — M4 user-test follow-up sub-scope」。

**第一步必讀（按順序，5 份）：**

1. _design/HANDOFF_11TH_PARALLEL_SETUP.md（並行 setup 包；§3 是你的 scope + §5 並行協調機制）
2. _design/HANDOFF_TO_11TH_MASTER.md v1.0（11th master 整體 scope；§3 路徑 A 純 monitor + §7 對 user 的建議；§4 紀律仍適用）
3. _design/PHASE_D_COMPLETION_REPORT.md v1.1 §6 端到端測試（user 親跑步驟 placeholder；你要 reconstruct 草稿；§10.2 條件 8 M4 user-test）
4. _design/POST_LOCK_PENDING.md v0.20+（NEW_REQ_14 PHASE_X §6 AI-assisted 補入機制 + NEW_REQ_20 為先例 sister case；可能已升 v0.21 if 對話 A 已 patch RESOLVED）
5. _design/CANON_DELTA_FRAMEWORK.md v0.1（成熟期功能 framework；user 量產期間若撞到 Canon Delta 觸發 trigger 你紀錄）

**第二步精選讀（碰到才看）：**

6. _design/UX_SPEC.md v0.4（前端 11 feature spec；若 user 跑前端撞到 finding 你查 spec verify）
7. _design/SPEC.md v1.2 + _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5（skill 行為 spec；若 skill 跑出來行為跟 spec 不對 verify）
8. _design/DECISIONS_LOG.md v2.0 D-050~D-054（skill 寫檔邊界 + D-054 hybrid；若量產撞到 boundary verify）
9. _design/ARCHITECTURE.md v1.6 §5 + §6.7（影響範圍評估 + 共通骨架；若 /iterate-* 跑出來不對 verify）

**你的 scope（嚴格 monitor + 紀錄性質）：**

1. 等 user 量產期間回報 finding（user 從 Codex CLI 對話切到你這 chat 回報）
2. 對每個 finding：
   - 讀對應 spec / SKILL.md / frontend code verify 是合理還是 bug
   - 分類：✓ 合理 / deferred placeholder / spec drift bug / runtime bug / design gap
   - 紀錄到本對話 scratch table
3. user 量產一段時間後（建議至少完成 1 場戲完整 pipeline 跑通）→ 整理 scratch 統一處理：
   - finding 屬「frontend / skill runtime bug」→ 開新 NEW_REQ_21+ 寫進 POST_LOCK_PENDING.md（用 NEW_REQ_20 為 template）
   - finding 屬「PHASE_D §6 親跑紀錄補入」→ 觸發 NEW_REQ_14 AI-assisted §6 補入機制：你 reconstruct §6 草稿（從 Instance repo `.protocol_version.phase_log` + git log + Codex CLI 對話記錄）→ user 拍板「採」/「修改後採」/「棄」→ patch PHASE_D §6 placeholder
4. 量產跑完一場戲 + 整理完 finding + 補入 §6 → 你寫 11th master 階段性 summary 給 user（可選寫成 _design/M4_USER_TEST_REPORT.md）

**重要邊界（嚴格 scope）：**

- ✗ 不動 Instance repo D:\劇本開發工具-test\ 任何檔（純讀；user 在對話 C 跑 skill 寫；你不重複跑）
- ✗ 不動 _tools/frontend/ 任何檔（屬對話 A scope）
- ✗ 不改任何 LOCKED spec / registry / parser code
- ✗ 不改 D-001~D-054 拍板結論
- ✗ 不擅自啟新 D-NNN 拍板（finding 屬 spec drift / 設計層衝突等需新 D-NNN 拍 → 回升 user）
- ✗ 不跑真實 skill（你在 Cowork 對話內也不 simulate skill 執行；屬對話 C 範圍）

**並行協調機制：**

- 你只動 POST_LOCK_PENDING.md（加 NEW_REQ_21+ entry）+ 可能寫 _design/M4_USER_TEST_REPORT.md；不會跟對話 A（動 _tools/frontend/）撞檔
- 你跟對話 C（Codex CLI）資訊流：user 是中介；user 看到 Codex CLI 跑出 finding → 切到你這 chat 回報 → 你 verify + 紀錄
- 你需要 user 拍板「採」/「棄」每個 finding 處理方式 → 印 finding 清單等 user 拍板
- 你 patch POST_LOCK_PENDING / 寫新檔 → 給 user GIT SUMMARY 手動 commit + push

**完成條件（依 user 拍板的工作量）：**

最小工時版（單一場戲跑通）：
✓ user 在 Codex CLI 跑完 1 場戲完整 pipeline（/init-project → /create-* → /scene-task → /dialogue-write → /qa → 升 FINAL）
✓ 量產期間 finding 全紀錄到本對話 scratch
✓ NEW_REQ_14 §6 AI-assisted 補入機制執行 1 次（reconstruct §6 草稿 + user 拍板 + patch PHASE_D §6 placeholder）
✓ POST_LOCK_PENDING 升 v0.X partial supersede（如有新 NEW_REQ_21+）+ user push

中工時版（完整 Bible 建構 + 多場戲量產）：
✓ user 在 Codex CLI 跑完整 pipeline 2-3 天密集
✓ 累積 finding 寫成 _design/M4_USER_TEST_REPORT.md（reference 用）

請先回報你讀完 5 份必讀後對 scope + monitor + 紀錄機制的理解，再等 user 從量產對話回報第一個 finding。
```

## 3.3 完成條件 + 收尾

對話 B 完成 = user 完成至少 1 場戲量產 + 對應 finding 全紀錄 + NEW_REQ_14 §6 補入機制執行 1 次 + user push。可隨時暫停（量產暫停期間對話 B 就 idle）。

---

# 4. 對話 C：Codex CLI — 量產台詞 skill chain

## 4.1 用途

user 親跑量產台詞；用 Codex CLI 環境（讀 AGENTS.md skill 清單）；user 主動發起 skill 對話；agent 依 SKILL.md 5 階段流程執行；產出實際 Instance repo 內容。

## 4.2 啟動指令（PowerShell + Codex CLI）

```powershell
# 1. 切到 Instance repo
cd D:\劇本開發工具-test

# 2. 確認 .template_root 已移除 + 看當前 git state
ls .template_root  # 應該 not found
git status  # 應該看到 deleted: .template_root + 其他可能 placeholder
git log --oneline -3  # latest commit 應該是 master ref 對齊後的 10th master 收尾

# 3. 啟動 Codex CLI（依你環境裝法；如 codex 或 codex-cli 命令）
codex

# 4. agent 啟動後自動讀 AGENTS.md skill 清單；你在 chat 內提 skill name + 5 階段對話
```

## 4.3 量產流程建議（最小可跑通版本；1-2 場戲）

依 user manual `_user_manual/08_workflows/從零開始建專案.md` + `寫單場戲完整流程.md` 改寫成最小版：

### 4.3.1 Bootstrap + 上游 Bible（30-60 分）

```
1. /init-project
   - bootstrap .protocol_version + 3 registry copy + 10_art_assets/ 結構 + .gitignore
   - .template_root 應自動移除（或已被 user 手動 del）

2. /create-world
   - 11 議題；簡化版每題答 1-2 句即可（測試 pipeline 跑通不求完整 Bible）
   - 寫 01_world/01_a/b/c + 02_vocabulary/02_a/b/c + 00_b §1/§2

3. /create-character 主角A
   - 9 議題簡化版
   - 寫 03_characters/main/主角A_聲線卡.md

4. /create-character 反派B
   - 同上；對齊量產測試

5. /create-relationship 主角A 反派B
   - 6 議題簡化版
   - 寫 04_relationships/04_a 矩陣 + 兩個聲線卡的「關係段」merge

6. /create-outline
   - 7 議題簡化版
   - 寫 05_plot/05_a 主體

7. /create-detailed-outline
   - 簡化版 1 章 2 場
   - 寫 05_plot/05_b + 06_scene_index/06_a 場景索引

→ 期間任何 finding（agent 行為跟 SKILL.md 描述不對、寫錯檔、跨 boundary、enum 跑錯等）→ 切到對話 B 回報
```

### 4.3.2 下游 1 場戲完整 pipeline（30-60 分）

```
8. /scene-task S-01-01
   - 寫 07_scene_tasks/CH01_S01_*.md 任務包

9. /dialogue-write S-01-01
   - 試寫 mode；產 v01A / v01B / v01C 三版（mode_tag = ORGANIZED）
   - 寫 08_dialogue_outputs/CH01_S01_v01A.md / v01B.md / v01C.md

10. /dialogue-write S-01-01 --converge
    - 收斂 mode；簡化版（agent 自己挑或 user 隨便挑 1-2 句）→ 產 v02
    - 寫 08_dialogue_outputs/CH01_S01_v02.md

11. /qa S-01-01 v02
    - 並行跑 8 份 QA 報告（09_a 到 09_i 不含 09_e）
    - 寫 09_quality_assurance/CH01_S01_v02_09_a.md ~ 09_i.md

12. 手動填 09_e 人類拍板紀錄（簡化版即可）

13. 升 FINAL

→ 期間任何 finding（QA 報告格式不對、影響範圍評估漏實體、phase_log 寫錯欄位等）→ 切到對話 B 回報
```

### 4.3.3 視圖 + 匯出測試（10-15 分）

```
14. /view-world / /view-character 主角A / /view-outline / /view-detailed-outline
    - chat 印整合視圖；不寫檔；驗證 Wave 13 view-* skill 對 D-054 hybrid 是否 work

15. /export-world / /export-character 主角A / /export-outline / /export-detailed-outline
    - 寫 view/世界觀.md / view/角色_主角A.md / view/大綱.md / view/細綱.md DERIVED 7 欄
    - 驗證 Wave 14 export-* skill

→ 期間任何 finding（view 印錯 / export 寫錯 / D-054 hybrid 沒抓到 per-scene 檔等）→ 切到對話 B 回報
```

### 4.3.4 迭代測試（10-15 分；驗證 Wave 12 SKILL.md）

```
16. /iterate-world
    - 改 W-rules 一個小設定（如禁用詞加 1 個）
    - 驗證 影響範圍評估 + 雙路反查 + LOCKED status check + 下游 pipeline 互鎖
    - 寫 01_world/01_a + 02_c

17. /iterate-character 主角A
    - 改聲線卡某段（如語氣 cold → cold + 自嘲）
    - 驗證影響範圍評估 + 下游台詞 alerts

18. /iterate-scene S-01-01 --split-to-file
    - 把 S-01-01 從聚合 06_a 拆為獨立 06_scene_index/CH01_S01_*.md per-scene 檔
    - 驗證 D-054 NEW_REQ_15 落地 + marker + frontmatter 上游三欄 + phase_log split_to_file: true

19. 重跑 /scene-task S-01-01
    - 驗證 D-054 hybrid fallback：應該優先讀 per-scene 檔（拆檔後）而非 aggregate 06_a row

→ 期間任何 finding → 切到對話 B 回報
```

### 4.3.5 診斷 + 整理測試（5-10 分；驗證 Wave 15 SKILL.md）

```
20. /diagnose
    - Mode A 廣掃 Instance；chat 印 6 段診斷報告
    - 驗證對齊 00_a §3.3.4

21. /integrate <target>（如 /integrate character）
    - 餵一段隨便的人物素材；驗證 Stage 4a 印 diff → user 拍板 → Stage 4b 寫檔流程

→ 期間任何 finding → 切到對話 B 回報
```

## 4.4 量產期間 git 操作

user 每跑完一個 phase（如 Bootstrap + 上游 / 下游 1 場戲 / 迭代測試）→ PowerShell 切到 D:\劇本開發工具-test 跑 git add + commit + push。建議 commit message 模式：

```
M4 user-test phase X：<phase name>

跑完 skill 清單：
- /init-project（commit hash）
- /create-world（commit hash）
- ...

期間 finding（已切對話 B 回報）：
- finding 1: ...
- finding 2: ...
```

## 4.5 完成條件

對話 C 完成 = 至少跑完 4.3.1 + 4.3.2（Bootstrap + 1 場戲）+ 期間 finding 全切對話 B 回報 + Instance repo commit + push。可隨時繼續加跑 4.3.3 ~ 4.3.5（依你時間）。

---

# 5. 並行協調機制

## 5.1 三對話動的目錄

| 對話 | 目錄 | 寫檔範圍 |
|---|---|---|
| A Claude Cowork frontend | D:\劇本開發工具\_tools\frontend\ + _design\POST_LOCK_PENDING.md | ProjectDashboard.js / server.py / state.js / unit test / POST_LOCK_PENDING v0.21 |
| B Claude Cowork M4 follow-up | D:\劇本開發工具\_design\POST_LOCK_PENDING.md（新 NEW_REQ_21+）+ 可能 D:\劇本開發工具\_design\M4_USER_TEST_REPORT.md + D:\劇本開發工具\_design\PHASE_D_COMPLETION_REPORT.md（§6 placeholder 補入）| 純 spec 檔；不動 frontend code 不動 Instance |
| C Codex CLI 量產 | D:\劇本開發工具-test\ Instance repo | .protocol_version + 01_world/ + 02_vocabulary/ + 03_characters/ + 04_relationships/ + 05_plot/ + 06_scene_index/ + 07_scene_tasks/ + 08_dialogue_outputs/ + 09_quality_assurance/ + view/ |

## 5.2 衝突風險點 + fallback

| 衝突點 | 風險 | fallback |
|---|---|---|
| A + B 同時動 POST_LOCK_PENDING.md | A 升 v0.21 標 NEW_REQ_20 RESOLVED；B 加 NEW_REQ_21+ entry；可能 git merge conflict | user 先 push A 的 v0.21 → B 從 latest pull → 加 NEW_REQ_21+ → push v0.22；或反過來 |
| frontend server 重啟 | A 改完 server.py 後 user 必重啟才能看新版；user 跑量產時開瀏覽器看新 dashboard 會中斷 | 量產期間以 Codex CLI skill 對話為主；不開瀏覽器 dashboard；A 改完 user push 後一次性重啟看新版 |
| user 多視窗切換注意力 | 三對話同時跑可能 user 注意力分散；某對話卡關等 user 拍板被遺忘 | 對話 A / B 卡關時印「需要 user 拍板」清單；user 量產對話跑到一段落（如完成一個 skill 階段）切過去看 |

## 5.3 user 拍板時機

| 時機 | 從哪個對話 | 拍板什麼 |
|---|---|---|
| 對話 A patch 完成需要 verify | A 通知 user | user 重啟 frontend server + 視覺 verify 三欄區內容對齊 → user 拍板 ✓ 收尾 / ✗ 補修 |
| 對話 C 量產撞到 finding | C 跑 skill 期間 | user 切到對話 B 回報 finding；對話 B 等 user 拍板處理方式（紀錄 NEW_REQ_21+ / 加 §6 補入 / 暫不處理） |
| 對話 B reconstruct §6 草稿完成 | B 印草稿 | user 拍板「採」/「改 [...]」/「棄」 |
| 對話 A / B 想升新 D-NNN 拍板（如 finding 屬設計層衝突）| A / B 印議題 | user 拍板 D-056+；如不拍板則 finding 推 12+ 輪 |

## 5.4 commit + push 順序

user 是 git 操作中央調度者。建議 commit 順序：

1. **量產 commit（C 那邊；最頻繁）**：每跑完一個 skill 階段 git add + commit + push（在 D:\劇本開發工具-test）
2. **A patch commit（每完成一個 patch 步驟）**：A 給 GIT SUMMARY；user push（在 D:\劇本開發工具）
3. **B 紀錄 commit（每加一個 NEW_REQ_21+ 或補 §6）**：B 給 GIT SUMMARY；user push（同 A）
4. **A / B 之間若撞 POST_LOCK_PENDING merge conflict**：依 5.2 fallback 處理

---

# 6. 推薦執行順序

## 6.1 第 1 階段：user bootstrap（5-10 分；只你做）

依本檔 §1 一次性跑完：
- 1.1 master ref 對齊 + push 含本 setup 包
- 1.2 git clone separate Instance repo
- 1.3 del .template_root
- 1.4 verify setup OK

## 6.2 第 2 階段：開 3 個對話並行（你時間決定）

| 對話 | 開啟時機 | 預估 wall-time |
|---|---|---|
| A Claude Cowork frontend patch | 立即（第 1 階段完成後）；A 跑 patch 期間 user 可開 B + C | 4-7h 累積 |
| B Claude Cowork M4 follow-up | 立即；idle 等 C 回報 finding | 依 C 量產時間而定 |
| C Codex CLI 量產 | 立即；隨時可跑可暫停 | 4.3.1 + 4.3.2 約 1-2h；完整 4.3.1-4.3.5 約 3-5h |

實務上 user 可能：
- 先開 A 跑 patch（user 在旁邊看；卡關時拍板）
- A 跑到 backend API 設計階段時 user 切去開 C 量產（Codex CLI 跑 /init-project + /create-world）
- A 跑完 patch + user push + 重啟 server
- user 開 B；同時繼續 C 量產
- 量產撞 finding → 切 B 回報
- A 收尾 + B 收尾 + C 至少跑完 1 場戲

## 6.3 第 3 階段：收尾 + 整理（30-60 分）

- A patch RESOLVED + POST_LOCK_PENDING v0.21 push
- B reconstruct PHASE_D §6 草稿 + user 拍板 + patch PHASE_D §6 + 升 v1.2 partial supersede
- B 整理量產期間累積 finding 寫 _design/M4_USER_TEST_REPORT.md（如有；可選）
- B 寫 11th master 階段性 summary（可選；或推 12+ 輪寫 HANDOFF_TO_12TH_MASTER.md）
- user push 全部變動

## 6.4 完成 11+ 輪並行模式 = 第 1-3 階段全 ✓

完成後工具 A 進入「user 實際量產 + 維護期」階段。後續按 user 需求啟動 12+ 輪 master 對話（NEW_REQ_16 lint script 實作 / NEW_REQ_17/18 / NEW_REQ_11 翻譯工具 fork / Canon Delta skill 等）。

---

# 7. Cross-ref

- `_design/HANDOFF_TO_11TH_MASTER.md` v1.0（11th master 整體 scope；本檔擴展為並行模式 setup）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.1（Milestone 4 真正封版宣告事實檔；§10 七 subsection）
- `_design/POST_LOCK_PENDING.md` v0.20（§5.11 NEW_REQ_20 紀錄；本檔執行後 A 升 v0.21 標 RESOLVED + B 可能升 v0.22 加 NEW_REQ_21+）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（成熟期功能 framework；對話 B monitor 對象）
- `_design/UX_SPEC.md` v0.4 §11.1.5 + §11.1.6（對話 A 對齊規格）
- `_design/DECISIONS_LOG.md` v2.0（D-001~D-054；三對話皆不改）
- `_tools/frontend/static/js/components/ProjectDashboard.js`（對話 A 主要 patch 對象）
- `_tools/frontend/server.py`（對話 A 加 endpoint 對象）
- `_user_manual/08_workflows/從零開始建專案.md` + `寫單場戲完整流程.md`（對話 C 量產參考）
- `AGENTS.md`（對話 C Codex CLI 讀的 skill 清單）

