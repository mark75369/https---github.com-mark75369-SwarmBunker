狀態：DEPRECATED
版本：v1.1（11th master 對話 A reframe 戰略落地 partial supersede — §9 amendment 紀錄 scope 從原「路徑 A/B/C 純 monitor + NEW_REQ_16 spec / 自動化 QA 層級實作」轉成「工具角色轉換 + Claude Code Dynamic Workflows audit 路徑 + 三對話並行 setup 廢止」；對應 NEW_REQ_22 + SANDBOX_REFACTOR_PLAN v0.1 + HANDOFF_11TH_PARALLEL_SETUP v0.2 + POST_LOCK_PENDING v0.22；本檔 v1.0 → v1.1）
歷史紀錄：v1.0（10th master 第十輪整合對話收尾交接包；Milestone 4 真正封版宣告完成；11+ 輪 master 接手「封版後維護期」+「NEW_REQ deferred backlog 階段性實作」+「M4 user-test follow-up」+「可選工具 B 翻譯工具 fork 評估啟動」）
最後更新：2026-06-01
適用範圍：給「第十一輪整合 master」對話的接手包 — Milestone 4 已真正封版；本檔屬封版後維護期 master 接手入口；本 v1.1 partial supersede 後 11th master 對話 A 已 reframe scope（詳 §9）；後續 12+ 輪 master 接手仍可 reference 本檔 §1-§8 為歷史紀錄
優先級：低（歷史接手包；Batch 5 補齊缺漏 header 欄位，內容不動）

# HANDOFF_TO_11TH_MASTER — 第十一輪整合 master 對話接手包

# 0. 文件目的

第十輪 master 對話（2026-05-23）完成 **Milestone 4 真正封版宣告**：

- **階段 1-2**：讀 8 份必讀 + verify Phase A.0F audit Round 4 GO close-out（commit `2ed48f3`）+ Wave 16 Step 4 inline patch 5 finding 全修（commit `1274a5d`）+ master HEAD vs frontend-tools-a0f HEAD 對齊狀態（落後 22 commits；user 拍板選 B 完整 merge 策略）+ baseline 維持
- **階段 3**：寫 `_design/CODEX_D_W12_STARTER.md` v0.1（10th master Wave 12 batch task starter；6 SKILL.md + 5 wrapper 一次性實作；對齊 D1-D5 starter + 00_j v0.2 共通基底 + D-050 三 block + D-054 hybrid fallback；commit `2efeecd`）+ user 跑 CODEX batch 落地 11 SKILL.md（commit `fa21b65`）+ master 內部 8 維度 verify PASS
- **階段 4**：AGENTS.md / CLAUDE.md Phase D Wave 13/14/15 metadata cleanup（CLAUDE.md v0.3 → v0.4；Wave 12 row 含 starter 落地註記）
- **階段 5**：PHASE_D_COMPLETION_REPORT v1.0 → v1.1 partial supersede 真正封版宣告（§10 Milestone 4 真正封版宣告 7 個 subsection 落地）
- **階段 6**：POST_LOCK_PENDING v0.18 → v0.19 partial supersede（§5 10th master 評估紀錄總表；7 個 deferred NEW_REQ 全有明確結論 + 推薦處理時機 + trigger 條件）
- **階段 7**：本 HANDOFF v1.0 落地 + archive 9th master handoff packages

工具 A `game-dialogue-bible` 結構性開發完成：51 SKILL.md（25 英文 + 26 中文 wrapper）+ 9 QA 模板 + 27 Bible 模板 + 3 registry yaml + 11 個 Phase A.0F feature + 10 LOCKED spec + DECISIONS_LOG v2.0 D-001~D-054 + REQUIREMENTS_LOCK v1.0 FINAL。

第十一輪 master 對話接手 **封版後維護期** 範圍：

1. **M4 user-test follow-up**（NEW_REQ_14 AI-assisted §6 補入機制執行；user 跑完 M4 chain 後啟動）
2. **NEW_REQ_16 lint script spec 規劃 + 階段性實作**（10th master 評估建議起手；屬封版後維護期 ROI 最高 item）
3. **NEW_REQ_15 D-054 hybrid iterate trigger 監控**（依 user 實際使用情況；A/B/C/D 任一達成則開 D-056+ 拍板評估；議題號原預留為 D-055；§6.18.2 順延）
4. **NEW_REQ_9 baseline 老債清理**（等 NEW_REQ_16 落地後自動 / 半自動處理）
5. **（可選）NEW_REQ_11 工具 B 翻譯工具 fork 評估啟動**（M4 + 6 個月 + 4 個前置條件達成 + user 拍板）
6. **（可選）Canon Delta skill 真正實作**（C-1~C-5 task；屬成熟期功能；CANON_DELTA_FRAMEWORK v0.1 framework reference 已預備）
7. **（可選）任何新議題 → 緊急 patch round**（依 D-049 / D-051 / D-053 / D-054 / D-055 模式；如有新議題 → 開 D-056+ 拍板）

**預估第十一輪總工時：** 依 user 拍板 scope 決定 — 最小工時（純 monitor + 無新實作）30-60 分；中工時（NEW_REQ_16 spec 規劃落地 1 份 ~300 行 spec）2-3h master + 6-8h 後續實作 + 2-4h testing；大工時（NEW_REQ_16 + 17 + 18 全層級實作）20-30h 累計

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。10th master 第十輪整合對話完成 Milestone 4 真正封版宣告（2026-05-23）：

- Phase D Wave 12 11 SKILL.md（6 個 /iterate-* + 5 中文 wrapper；含 D-054 NEW_REQ_15 /iterate-scene --split-to-file 落地）全 land
- Phase A.0F audit cycle Round 4 GO close-out
- AGENTS.md / CLAUDE.md Phase D Wave 13/14/15 metadata 對齊（Wave 12 row 待後續 cleanup partial supersede 升 ✅）
- PHASE_D_COMPLETION_REPORT v1.0 → v1.1 partial supersede 真正封版宣告（§10 七 subsection）
- POST_LOCK_PENDING v0.18 → v0.19 partial supersede（§5 七 deferred NEW_REQ 評估紀錄總表）
- HANDOFF_TO_11TH_MASTER v1.0 落地 + 9th master 3 份 handoff package archive

工具 A 結構性封版完成：51 SKILL.md + 9 QA 模板 + 27 Bible 模板 + 3 registry + 11 個 Phase A.0F feature + 10 LOCKED spec + D-001~D-054 拍板 + 完整 design layer。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第十一輪整合 master」對話。

**第一步必讀（按順序，6 份）：**

1. _design/HANDOFF_TO_11TH_MASTER.md（本檔；你的 scope）
2. _design/PHASE_D_COMPLETION_REPORT.md v1.1（Milestone 4 真正封版宣告事實檔；§10 七 subsection 含封版基準 / 達成 checklist / 工具 A 完整 pipeline 鏈 / user 後續路徑 / 11th master scope preview / 封版紀律 / 致謝）
3. _design/POST_LOCK_PENDING.md v0.19（§5 10th master 階段 6 評估紀錄總表；7 個 deferred NEW_REQ 明確結論 + trigger 條件 + 推薦處理時機）
4. _design/CANON_DELTA_FRAMEWORK.md v0.1（成熟期功能 framework reference；屬 11+ 輪 master / 工具 B fork 可選實作對象；不實作 skill）
5. _design/DECISIONS_LOG.md v2.1（D-001~D-055 全 LOCKED；若有新 D-056+ 拍板需求才動）
6. _design/REQUIREMENTS_LOCK.md v1.0 FINAL（north star 不動）

**第二步精選讀（碰到才看）：**

7. _design/HANDOFF_TO_10TH_MASTER.md v1.0（10th master 整體 scope；本檔接續；§4 風險警示與紀律仍適用；可能已 archive 進 _design/archive/）
8. _design/CODEX_D_W12_STARTER.md v0.1（10th master Wave 12 batch starter；含 D-050/D-053/D-054 邊界 reference）
9. _design/TASKS.md v1.9 §C（Phase D 視圖+迭代+匯出+整合 task spec）
10. _design/ARCHITECTURE.md v1.6（10 LOCKED spec 之一）
11. _design/SPEC.md v1.2（10 LOCKED spec 之一）
12. _design/INTEGRATION_CONTRACTS.md v2.1（10 LOCKED spec 之一）
13. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5（10 LOCKED spec 之一；§5 Canon Delta framework）
14. _design/UX_SPEC.md v0.4（10 LOCKED spec 之一；Phase A.0F feature spec）
15. _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2（10 LOCKED spec 之一）
16. _design/DATA_FORMAT_SPEC.md v0.4（10 LOCKED spec 之一）
17. _design/D054_DECISION_PACKAGE.md v0.2（D-054 拍板包 APPLIED）

**你的 scope（11th master；7 個 candidate 主軸 — user 拍板實際範圍）：**

1. **M4 user-test follow-up（NEW_REQ_14 AI-assisted §6 補入機制執行）：**
   - user 跑完 M4 chain（/init-project → /create-* → /scene-task → /dialogue-write → /qa → /view-* → /export-* → /iterate-* → /diagnose+integrate + 前端工具）後 trigger
   - agent 從 phase_log / git log / review_log 等 reconstruct PHASE_D §6 placeholder 草稿
   - user 拍板「採」/「改」/「棄」→ agent patch PHASE_D §6 placeholder
   - 對齊 D-052 AI-assisted + user 拍板紀律
   
2. **NEW_REQ_16 lint script spec 規劃（10th master 階段 6 建議起手）：**
   - 寫 200-400 行 Python `scripts/cross_ref_lint.py` spec（含 schema / findings JSON 結構 / 白名單檔範圍 / pre-commit hook / GitHub Actions 整合）
   - 重新完整設計（不直接按 NEW_REQ_16 v0.18 entry 提議方案 code）
   - spec PASS → 推 12+ 輪實作（6-8h Python + 2-4h testing）
   - ROI：自動抓 ~80% master 期間 MINOR finding → 後續每輪省 30-60 分鐘 cleanup
   
3. **NEW_REQ_15 D-054 hybrid iterate trigger 監控：**
   - 監控 user 寫量產 dialogue 期間 4 個 trigger（A: ≥ 30 場後想全 per-scene / B: /iterate-scene --split-to-file 連續 ≥ 5 次 / C: 多 agent 並行需求 / D: git merge conflict 持續）
   - 任一達成 → 開 D-056+ 拍板評估（候選選項 A/B/C 詳 NEW_REQ_15 entry；議題號原預留為 D-055；§6.18.2 順延）
   
4. **NEW_REQ_9 baseline 老債清理（依賴 NEW_REQ_16 落地）：**
   - 等 NEW_REQ_16 lint script 落地後可自動偵測 27 模板 old-style filename
   - 動 LOCKED 模板 rename 需開 D-056+ 拍板（風險高 ROI 低）
   - 或者用 NEW_REQ_16 lint script 加白名單跳過老式檔名
   
5. **（可選）NEW_REQ_17/18 自動化 QA Layer 2/3 實作：**
   - NEW_REQ_17 auto-patcher 依賴 NEW_REQ_16；屬 12+ 輪 scope
   - NEW_REQ_18 nightly AI semantic review 依賴 NEW_REQ_16/17 + 觀察 6 個月語意 drift；屬 13+ 輪 scope
   
6. **（可選）NEW_REQ_11 工具 B 翻譯工具 fork 評估啟動：**
   - 屬 11+ 輪 scope；啟動條件：Milestone 4（✓ 達成）+ L3_EXPORT_PROMPT_SCHEMA v1.0 穩定 + 至少 1 個完整作品 corpus + user 明確翻譯需求 + 工具 A 維護期穩定 6 個月以上
   - 完整提案見 `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` v0.1
   - 工時 80-130h master + CODEX（跟工具 A 累積工時類似量級）
   
7. **（可選）Canon Delta skill 真正實作：**
   - 屬成熟期功能；CANON_DELTA_FRAMEWORK v0.1 framework reference 已預備
   - 5 task：C-1 寫 /canon-delta-extract sub-skill + C-2 擴 /qa + C-3 擴 /iterate-* + C-4 D-NNN 拍板細化 + C-5 PHASE_E_COMPLETION_REPORT
   - 啟動 trigger A/B/C/D 詳 CANON_DELTA_FRAMEWORK §3.3
   - 工時 20-35h master + CODEX

**禁止越界（嚴守 LOCKED spec + 9th + 10th master 累積教訓）：**

- ✗ 不重做設計（10 LOCKED spec v1.0~v2.0 全不動）
- ✗ 不改 D-001~D-055 拍板結論（要動需 user 拍板新 D-056+）
- ✗ 不重審 10th master Milestone 4 真正封版宣告 + 階段 1-6 已 accepted finding
- ✗ 不修改 51 個既有 SKILL.md / 27 個既有 Bible 模板 / 9 個 QA 模板 / 3 個 registry / 00_protocol/ 任何檔內容（除非 user 明示拍板修改某特定檔）
- ✗ 不寫 Phase E / 工具 B 任何檔（除非 user 明示啟動 NEW_REQ_11 工具 B fork）
- ✗ 不擅自啟新 D-NNN 拍板（如有新議題 → 先回升 user 拍板）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 6 份必讀後對 scope + 7 個 candidate 主軸 + 9th + 10th master 累積教訓的理解，再開始處理。
```


---

# 2. 當前狀態快照（10th master 對話結束時 — 2026-05-23）

## 2.1 設計層狀態（spec 版本；10th master 全程不動 LOCKED）

| 檔 | 版本 | 狀態 | 10th master 全程變動 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | 不動 |
| `_design/DECISIONS_LOG.md` | v2.0 | **FINAL** | 不動（D-001~D-054 維持）|
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | **LOCKED** | 不動 |
| `_design/SPEC.md` | v1.2 | **LOCKED** | 不動 |
| `_design/ARCHITECTURE.md` | v1.6 | **LOCKED** | 不動 |
| `_design/TASKS.md` | v1.9 | **LOCKED** | 不動 |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | **LOCKED** | 不動 |
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 不動 |
| `_design/POST_LOCK_PENDING.md` | **v0.19** | DRAFT | **10th master 階段 6 升 v0.18 → v0.19；§5 評估總表 10 個 subsection 新增** |
| `_design/PHASE_D_COMPLETION_REPORT.md` | **v1.1** | DRAFT | **10th master 階段 5 升 v1.0 → v1.1；§7 + §8 wording 升「真正達成」+ 新增 §10 真正封版宣告 7 個 subsection** |
| `_design/CANON_DELTA_FRAMEWORK.md` | v0.1 | DRAFT | 不動（9th master 第二段 Wave 15 落地）|
| `_design/CODEX_D_W12_STARTER.md` | **v0.1** | DRAFT | **10th master 階段 3.1 新建；含 6 SKILL.md 共通結構 + 6 個 sub-skill 個別差異規格 + D-050 三 block + D-054 hybrid fallback** |
| `_design/D054_DECISION_PACKAGE.md` | v0.2 | **APPLIED** | 不動 |
| `_design/PHASE_C_COMPLETION_REPORT.md` | v1.0 | DRAFT | 不動 |
| `_design/PHASE_B_COMPLETION_REPORT.md` | v1.4 | DRAFT | 不動 |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | DRAFT | 不動 |
| `_design/CODEX_D1_STARTER.md` ~ `CODEX_D5_STARTER.md` | v0.3/v0.4 | DRAFT | 不動（9th master 第一段 Wave 12 starter set）|
| `_design/CODEX_D6_STARTER.md` ~ `CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` | v0.1 | DRAFT | 不動（9th master Wave 13/14/15 starter）|
| `_design/CODEX_D_FINAL_STARTER.md` / `CODEX_D_FINAL_REVIEW_STARTER.md` / `CODEX_D_FINAL_REVIEW_REPORT.md` | v0.1 | DRAFT | 不動（9th master 第二/三段 Wave 16 starter + report）|
| `00_protocol/00_j_迭代協議.md` | v0.2 | DRAFT | 不動（9th master 第一段 Wave 12 升 v0.1 → v0.2）|
| `AGENTS.md` | n/a | n/a | **10th master 階段 4 patch — Phase D Wave 13/14/15 row TBD → ✅；Wave 12 row 含 starter 落地註記** |
| `CLAUDE.md` | **v0.4** | DRAFT | **10th master 階段 4 升 v0.3 → v0.4；同步 AGENTS.md 變動** |
| `HANDOFF_TO_10TH_MASTER.md` | v1.0 | DRAFT | 10th master 全程 reference；本輪結束後 archive 進 `_design/archive/`（可選）|

## 2.2 SKILL.md 落地完整狀態（51 個全 land）

| Phase | Wave | 英文主檔 | 中文 wrapper | 統計 | 狀態 |
|---|---|---|---|---|---|
| A | 1-5 | /init-project / /create-world / /status / /check-gaps | 初始化專案 / 建立世界觀 / 進度 / 缺漏檢查 | 4 + 4 = 8 | ✓ Milestone 1（6th master）|
| B | 6-8 | /create-character / /create-relationship / /create-outline / /create-detailed-outline | 建立角色 / 建立關係 / 建立大綱 / 建立細綱 | 4 + 4 = 8 | ✓ Milestone 2（7th master）|
| C | 9-11 | /scene-task / /dialogue-write / /qa | 場景任務包 / 生成台詞 / 檢查 | 3 + 3 = 6 | ✓ Milestone 3（8th master；2026-05-21）|
| D | **12** | iterate-world / iterate-character / iterate-relationship / iterate-outline / iterate-detailed-outline / iterate-scene | 迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱 | 6 + 5 = 11 | ✓ **Milestone 4 真正封版（10th master；2026-05-23；commit fa21b65）** — `/iterate-scene` 含 D-054 NEW_REQ_15 split-to-file 落地；無中文 wrapper（依 D5 starter）|
| D | 13 | view-world / view-character / view-outline / view-detailed-outline | 查看世界觀 / 查看角色 / 查看大綱 / 查看細綱 | 4 + 4 = 8 | ✓（9th master 第一段）|
| D | 14 | export-world / export-character / export-outline / export-detailed-outline | 匯出世界觀 / 匯出角色 / 匯出大綱 / 匯出細綱 | 4 + 4 = 8 | ✓（9th master 第二段）|
| D | 15 | diagnose / integrate | 診斷 / 整理 | 2 + 2 = 4 | ✓（9th master 第二段）|

**總統計：** 25 英文主檔 + 26 中文 wrapper = **51 SKILL.md** + 9 QA 模板 + 27 Bible 模板 + 3 registry yaml + 11 Phase A.0F feature

## 2.3 Phase A.0F 前端工具狀態（Milestone 4 已 close-out）

| 項目 | 狀態 | Evidence |
|---|---|---|
| A.0F.3-A.0F.11 11 個 feature | ✓ all land | commit chain `e4721e9` → `4c0c36e` → `1ea2b7c` → `1357247` → `7b72454` → `25d919f` → `989de19` |
| 整體驗收 + integration test + user manual v0.2 | ✓ | commit `a13ce5a` |
| audit cycle Round 1-4 | ✓ Round 4 GO close-out | commit chain `50348f7` (P1) → `32e15df` (P2) → `8afab68` (doc) → `e37cd3e` (test) → `2f7a1c1` (R1 starter) → `3829d48` / `1735d0a` (R2 patch) → `bef5516` / `52c03c9` / `c0640be` / `772fcc8` / `9d2814a` / `2cfb651` / `a996ad5` / `393229f` / `5ec77a5` / `fc2948b` → `2ed48f3` (R4 GO close-out report) |

## 2.4 Baseline（Milestone 4 封版時 — 對齊 PHASE_D_COMPLETION_REPORT v1.1 §10.2 條件 7）

- `check_headers.py`: **0 ERROR / 55 WARN / ~187 files**（10th master 全程 +2 WARN — PHASE_D v1.1 partial supersede + POST_LOCK_PENDING v0.19 partial supersede；屬可接受 markdown long note pattern）
- `check_paths.py`: **247 ERROR / 1 WARN**（R2-MAJOR-03 hard-limit accept；NEW_REQ_9 既有 baseline debt 27 模板 old-style filename reference 推 11+ 輪評估）
- `build_repo_index('.')`: **0 ERROR / 91 WARN / ~248 files**

**11th master baseline 門檻：** check_paths.py ≤ 247 ERROR（同 9th + 10th master；Windows 端權威）；若 11th master 動 NEW_REQ_9 LOCKED 模板需新 D-NNN 拍板；若 NEW_REQ_16 lint script 落地後自動清理屬常規 cleanup 範圍。

## 2.5 git 狀態（10th master 對話結束時）

| ref | HEAD | 包含 |
|---|---|---|
| `master` / `origin/master` | `140af34` | ⚠ **落後 ~27 commits**（不含 9th master 第二/三段 Wave 15 SKILL.md / PHASE_D v1.0 / Wave 16 / 10th master 全部 commit）|
| `frontend-tools-a0f` / `origin/frontend-tools-a0f` | `<10th master 收尾 HEAD>` | ✓ 全部 9th master + 10th master + Phase A.0F.3-11 + audit cycle |

**11th master 接手前 user 必做：** 依 user 拍板選 B 完整 merge 策略 — 手動跑 `git checkout master + git merge frontend-tools-a0f` 一次性對齊。11th master 對話接手時應從 master ref 跑（屆時 master 已含全部 10th master 變動）。

如未 merge，11th master 仍從 `frontend-tools-a0f` 跑（同 10th master 模式）；建議 user 在 Milestone 4 真正封版 commit + push 後立即 merge → master，把 frontend-tools-a0f 屬「完成性質 branch」轉為「歷史 branch」。


---

# 3. 第十一輪工作清單（按 user 拍板 scope 決定）

11th master 屬「封版後維護期」性質；不同 user 拍板路徑導致實際工時差異很大。下列 5 個推薦路徑供 user 選擇：

## 路徑 A：純 monitor + M4 user-test follow-up（最小工時 30-60 分）

- 階段 1：讀完 6 份必讀 + 接受 10th master handoff
- 階段 2：M4 user-test follow-up（NEW_REQ_14 AI-assisted §6 補入機制執行；user 跑完 M4 chain 才 trigger）
- 階段 3：monitor 7 個 deferred NEW_REQ trigger 條件（純讀取；無寫檔）
- 11th master 對話結束（推 12+ 輪實際實作）

## 路徑 B：NEW_REQ_16 lint script spec 規劃（建議；中工時 2-3h）

- 階段 1：讀完 6 份必讀 + 接受 10th master handoff
- 階段 2-3：同路徑 A
- 階段 4：寫 `_design/NEW_REQ_16_LINT_SCRIPT_SPEC.md` v0.1（~300 行 spec 規劃）
   - schema 設計（findings JSON 結構）
   - 白名單檔範圍（哪些檔可被 lint / 哪些不能）
   - rule 設計（version cross-ref / D-NNN supersede 鏈 / TASKS partial supersede ledger / POST_LOCK_PENDING NEW_REQ status）
   - test fixtures 規劃
   - 整合進 build / CI（pre-commit hook / GitHub Actions）
- 階段 5：11th master 寫 HANDOFF_TO_12TH_MASTER（接 lint script 實作 + 後續維護期）

## 路徑 C：NEW_REQ_16 + 17 自動化 QA Layer 1+2 全層級實作（大工時 20-30h）

- 階段 1-4：同路徑 B
- 階段 5：寫 CODEX starter 給 CODEX 跑 lint script 實作（200-400 行 Python；6-8h CODEX wall-time + 2-4h testing）
- 階段 6：寫 CODEX starter 給 CODEX 跑 auto-patcher 實作（300-500 行 Python + safety net；8-12h CODEX wall-time + 4-8h testing）
- 階段 7：master 內部 verify + baseline 對齊 + 寫 HANDOFF_TO_12TH_MASTER

## 路徑 D：NEW_REQ_11 工具 B 翻譯工具 fork 評估啟動（極大工時 80-130h）

- 啟動條件：M4 + 6 個月使用 + 至少 1 個完整作品 corpus + user 明確翻譯需求 + 工具 A 維護期穩定 6 個月以上
- 完整提案見 `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` v0.1
- 11th master 不啟動本路徑除非 user 明示拍板（屬 12+ 輪 master scope）

## 路徑 E：Canon Delta skill 真正實作（中-大工時 20-35h）

- 啟動 trigger A/B/C/D 詳 CANON_DELTA_FRAMEWORK §3.3
- 5 task：C-1 寫 /canon-delta-extract sub-skill + C-2 擴 /qa + C-3 擴 /iterate-* x5 + C-4 D-NNN 拍板細化 + C-5 PHASE_E_COMPLETION_REPORT
- 11th master 不啟動本路徑除非 user 明示拍板 + trigger 達成

## 路徑選擇建議

**user 拍板前考慮：**
- 你想做什麼？立即跑 M4 user-test？開始量產台詞？實作自動化 QA？啟動工具 B fork？
- 你期待 11th master 對話的工時投入？30 分 / 2-3h / 半天 / 一天 / 數週？
- 你期待的 ROI 順序？節省未來 master 對話 cleanup 時間（NEW_REQ_16）？提升量產效率（NEW_REQ_14 + 自動化 lint）？翻譯品質（NEW_REQ_11）？設計層自我修補（Canon Delta）？

**11th master 建議 default：路徑 B**（NEW_REQ_16 lint script spec 規劃；2-3h 工時；ROI 極高；屬封版後維護期最先實作 item；不需立即跑 CODEX 實作）。

---

# 4. 風險警示 + 重要紀律（9th master 7 條教訓 + 10th master 新增）

## 4.1 9th master 全程 7 條教訓內化（強制；11th master 必沿用；對齊 HANDOFF_TO_10TH_MASTER §4.1）

### 第一段對話 5 條（review cycle 收尾紀律）

1. **Windows baseline 權威** — sandbox virtiofs cache 在某些 check_paths case 會產 false negative；以 Windows 端為事實
2. **Cascade sweep broader pattern** — CODEX review 列出的具體 hits 是「sample 抽樣」；master inline patch sweep 必須對全 repo 跑 broader pattern grep
3. **SPEC frontmatter 段直接 grep verify** — 寫 starter 涉及 frontmatter 描述前直接 grep SPEC verify；不可憑記憶寫具體欄位數字
4. **Supersede note 避免重複 finding 內精確詞串** — strict grep 不分否定句 / 歷史 narrative；wording 應描述「修補性質」而非重述被改的字串
5. **Review starter diff anchor 必須精確** — 不要假設 user commit composition；推薦改用「明示 commit hash」或「`HEAD~1..HEAD` 限定最後一個 commit」

### 第二段對話新增 2 條（filesystem / corruption 紀律）

6. **寫長 multi-byte 檔請用 Python script via bash 或 cat heredoc** — 不用 Write/Edit tool（Cowork tool 對長中文檔有截斷風險）；寫完跑 Python 驗 bytes / null bytes / utf-8 decode
7. **Cloud sync / 防毒不得監控 working tree** — `D:\劇本開發工具` 必須加 OneDrive/Dropbox/Google Drive 排除清單 + Windows Defender 白名單（特別 `.git/`）

## 4.2 10th master 新增 3 條教訓（11th master 沿用）

### 教訓 8：sandbox virtiofs cache stale 比預期更嚴重

10th master 階段 5 寫 PHASE_D v1.1 § 8 表 + § 10 期間，sandbox `wc -l` / `tail` / `git diff` 反覆顯示 truncated 版本（CLAUDE.md 110/137 / AGENTS.md 184/205 / PHASE_D_COMPLETION_REPORT 498/549）。 用 Read tool（Windows 端權威）驗證 100% 確認檔案完整。

**紀律：** 所有「檔案被 truncate」恐慌前先 Read tool 驗 Windows 端真實狀態；不要依賴 sandbox `wc -l` / `tail` / `git diff` 結論立即 panic patch。教訓 1（Windows baseline 權威）擴展到「Windows file content 權威」。

### 教訓 9：Edit tool 對 Chinese 字 boundary 敏感

10th master 階段 4 patch AGENTS.md 期間，Edit tool old_string 含 `;` (half-width semicolon) 但實際 file 是 `；` (full-width)；first Edit attempt failed with "String to replace not found"。

**紀律：** Edit tool 涉及 Chinese-heavy old_string 時，若 first attempt 失敗，先用 Read tool 取得精確 byte-level context 再重做；不要連續嘗試多個 wording 變體（會浪費 context + 增加 truncation 風險）。

### 教訓 10：可用既有 batch starter 慣例對齊 wording 而非自創

10th master 階段 3.1 寫 CODEX_D_W12_STARTER 時自造「Token 不是限制」wording；user 拍板要求對齊既有 9th master Wave 14-15 batch starter 既有慣例。

**紀律：** 寫新 starter / spec / handoff 前先 grep 既有同類檔 verify 慣例 wording（含 Token / 邊界 block / 中文 wrapper 結構 / 必讀清單格式 / cross-ref 寫法等）；對齊既有 pattern 而非自創。屬 NEW_REQ_16 lint script 未來可自動偵測的 wording-consistency 範圍。

## 4.3 NEW_REQ deferred 清單（給 11th master 處理時機 reference）

詳 `_design/POST_LOCK_PENDING.md` v0.19 §5「10th master 評估紀錄總表」— 7 個 deferred NEW_REQ 全有明確結論 + 推薦處理時機 + trigger 條件。

11th master 建議優先順序：

1. **路徑 B：NEW_REQ_16 lint script spec 規劃**（建議起手；ROI 最高）
2. **monitor：NEW_REQ_15 D-054 hybrid trigger A/B/C/D**（純讀取；user 跑量產時撞到）
3. **M4 user-test follow-up：NEW_REQ_14 AI-assisted §6 補入**（user trigger）
4. **後續：NEW_REQ_17/18/9**（依賴 NEW_REQ_16 落地後處理）
5. **可選大型：NEW_REQ_11 工具 B fork + Canon Delta skill**（屬 12+ 輪或更晚 scope）

## 4.4 sandbox virtiofs cache stale 已知問題（沿用 9th + 10th master 內化）

工作目錄 Windows 端為權威。Sandbox 端 git status / wc -l / ls mtime / tail / git diff 偶爾顯示 stale（10th master 階段 5 多次撞到）。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準；bash grep / wc / tail / git diff 結果若衝突要用 Read 驗。

## 4.5 不擅自越界

- ✗ 不重做設計（10 LOCKED spec 全不動）
- ✗ 不改 D-001~D-054 拍板結論
- ✗ 不重審 10th master 已 accepted finding（含 Milestone 4 真正封版宣告）
- ✗ 不修改 51 個既有 SKILL.md / 27 個 Bible 模板 / 9 QA 模板 / 3 registry / 00_protocol 任何檔（除非 user 明示拍板修改）
- ✗ 不寫 Phase E / 工具 B 任何檔（屬 12+ 輪 scope；除非 user 明示啟動 NEW_REQ_11）
- ✗ 不擅自啟新 D-NNN 拍板（如有新議題回升 user 拍板）


---

# 5. 完成條件

第十一輪整合對話完成 = 依 user 拍板 scope 達成對應條件：

| 路徑 | 完成條件 |
|---|---|
| A 純 monitor | 讀完 6 份必讀 + monitor 紀錄 + M4 user-test follow-up（若 user trigger）|
| B NEW_REQ_16 spec 規劃（建議）| 同 A + 寫 `_design/NEW_REQ_16_LINT_SCRIPT_SPEC.md` v0.1 ~300 行 + baseline 維持 + 寫 HANDOFF_TO_12TH_MASTER |
| C 自動化 QA Layer 1+2 全實作 | 同 B + CODEX 跑 lint script + auto-patcher 落地 + baseline 維持 + 寫 HANDOFF_TO_12TH_MASTER |
| D 工具 B 翻譯工具 fork | 新建 `game-dialogue-translator` repo + 完整 Phase 1 setup + 寫工具 B 第 1 輪 master handoff |
| E Canon Delta skill 真正實作 | 5 task C-1~C-5 全落地 + PHASE_E_COMPLETION_REPORT v1.0 + 寫 HANDOFF_TO_12TH_MASTER |

所有路徑都要：
- ✓ baseline 維持 check_paths ≤ 247 ERROR / check_headers 0 ERROR / build_repo_index 0 ERROR
- ✓ 不擅自越界 LOCKED spec / D-001~D-054 / 51 既有 SKILL.md
- ✓ 若有新議題 → 回升 user 拍板 D-056+

---

# 6. 文件維護紀律

- 本檔是「接手指南」，第十一輪 master 對話讀完後**不需要更新本檔**
- 若第十一輪發現本檔不準確 → 標 errata 在第 12 輪接手包（如有）
- 第十一輪完成後可把本檔 archive 進 `_design/archive/`
- 真正完整 HANDOFF_TO_12TH_MASTER.md（如有）由第十一輪寫；對齊 HANDOFF_TO_10TH_MASTER / HANDOFF_TO_11TH_MASTER pattern

---

# 7. 對 user 的最終建議（10th master 對話結束時）

## 7.1 立即可做的事

1. **commit + push 10th master 階段 5-7 變更**（PHASE_D v1.1 + POST_LOCK_PENDING v0.19 + 本 HANDOFF v1.0 + archive 9th master 3 份 handoff）
2. **跑 git checkout master + git merge frontend-tools-a0f**（選 B 完整 merge 策略；對齊 master ref 把所有 9th + 10th master 變動一次性 merge）
3. **跑 M4 user-test（建議）：** 在你的實際作品 Instance 內跑完整 pipeline — /init-project → 5 個 /create-* → /scene-task → /dialogue-write → /qa → /view-* → /export-* → /iterate-* → /diagnose+integrate + 前端工具實際使用。發現任何摩擦記下來，準備 11th master 對話啟動時用 NEW_REQ_14 AI-assisted §6 補入機制更新 PHASE_D v1.x §6 placeholder
4. **準備 11th master 對話（依需求）：** 用本檔 §1 對話啟動指令；建議 wall-time 在 M4 user-test 跑一段時間後（讓 11th master 有實際 user-test feedback 可處理）

## 7.2 Milestone 4 真正封版的條件達成（已 ✓）

詳 PHASE_D_COMPLETION_REPORT v1.1 §10.2 達成 checklist — 7/8 ✓ + 1 ⏳ user-test（封版後 user-side 活動）。

## 7.3 user-test 第四次點時機（M4）

10th master Milestone 4 真正封版宣告後可立即做 M4 user-test：跑完整工具 A pipeline（從 /init-project → 5 個 /create-* → /scene-task → /dialogue-write → /qa → /view-* → /export-* → /iterate-* → /diagnose+integrate）+ 前端工具實際使用。

M4 user-test 完成 → 走 NEW_REQ_14 AI-assisted §6 補入機制 update PHASE_D v1.x §6 placeholder（11th master 對話內執行）。

## 7.4 後續路徑（11+ 輪 master + 維護期 + 可選 fork）

詳 PHASE_D_COMPLETION_REPORT v1.1 §10.4「Milestone 4 真正達成後的 user 後續路徑」+ §10.5「11th master scope preview」。

簡要：
- **11th master：** 路徑 B NEW_REQ_16 lint script spec 規劃（建議 default）
- **12+ 輪 master（可選）：** NEW_REQ_16 實作完成 → NEW_REQ_17 auto-patcher → NEW_REQ_18 nightly review
- **13+ 輪 master（可選）：** Canon Delta skill 真正實作 + 工具 B 翻譯工具 fork（如達成 trigger）
- **維護期：** 持續寫實際作品 + 監控 NEW_REQ_15 trigger + 任何新議題開新 master 拍 D-056+

## 7.5 工具 A 完整 lifecycle 預覽

```
[已達成] 設計層（1-4 master）
    ↓
[已達成] Milestone 0：10 LOCKED spec（4th master）
    ↓
[已達成] Milestone 1：Phase A 基礎 4 skill（6th master）
    ↓
[已達成] Milestone 2：Phase B 上游 5 skill（7th master）
    ↓
[已達成] Milestone 3：Phase C 下游 3 skill + 8 QA 模板（8th master）
    ↓
[已達成] Milestone 4：Phase D 12 skill + Phase A.0F 前端 + 真正封版（10th master 2026-05-23）
    ↓
[現在位置] 維護期 + M4 user-test + 量產台詞（11+ 輪 master + user）
    ↓
[可選] Phase E / Canon Delta skill / 工具 B 翻譯工具 fork（13+ 輪 master）
```

---

# 8. Cross-ref

- `_design/HANDOFF_TO_10TH_MASTER.md` v1.0（10th master 整體 scope；本檔接續；§4 風險警示與紀律仍適用；本輪結束後 archive 進 `_design/archive/`）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.1（Milestone 4 真正封版宣告事實檔；§10 七 subsection 含封版基準 / 達成 checklist / 工具 A 完整 pipeline 鏈 / user 後續路徑 / 11th master scope preview / 封版紀律 / 致謝）
- `_design/POST_LOCK_PENDING.md` v0.19（§5 10th master 階段 6 評估紀錄總表；7 個 deferred NEW_REQ 明確結論 + trigger 條件 + 推薦處理時機）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（成熟期功能 framework reference；屬 11+ 輪 / 工具 B fork 可選實作對象）
- `_design/DECISIONS_LOG.md` v2.1（D-001~D-055 全 LOCKED；若有新 D-056+ 拍板需求才動）
- `_design/REQUIREMENTS_LOCK.md` v1.0 FINAL（north star；不動）
- `_design/CODEX_D_W12_STARTER.md` v0.1（10th master Wave 12 batch starter；含 D-050/D-053/D-054 邊界 reference）
- `_design/CODEX_D1_STARTER.md` v0.3 ~ `_design/CODEX_D5_STARTER.md` v0.4（9th master 第一段 Wave 12 starter set；reference only）
- `_design/CODEX_D6_STARTER.md` ~ `_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md`（9th master Wave 13/14/15 starter；reference only）
- `_design/CODEX_D_FINAL_STARTER.md` / `CODEX_D_FINAL_REVIEW_STARTER.md` / `CODEX_D_FINAL_REVIEW_REPORT.md`（9th master 第二/三段 Wave 16；reference only）
- `_design/D054_DECISION_PACKAGE.md` v0.2 APPLIED（D-054 拍板包；含 hybrid 設計推理）
- `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` v0.1（NEW_REQ_11 工具 B 翻譯工具完整提案）
- `_design/TASKS.md` v1.9 LOCKED + `_design/ARCHITECTURE.md` v1.6 LOCKED + `_design/SPEC.md` v1.2 LOCKED + `_design/INTEGRATION_CONTRACTS.md` v2.1 LOCKED + `_design/DATA_FORMAT_SPEC.md` v0.4 LOCKED + `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 LOCKED + `_design/UX_SPEC.md` v0.4 LOCKED + `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 LOCKED（10 LOCKED spec；不動）
- `_design/PHASE_A_COMPLETION_REPORT.md` v1.1 + `_design/PHASE_B_COMPLETION_REPORT.md` v1.4 + `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（前三個 Milestone 達成事實檔；reference only）
- `00_protocol/00_a_台詞生產協議.md` ~ `00_l_關係創建協議.md`（既有 13 protocol；屬 LOCKED 性質不動）
- `00_protocol/00_j_迭代協議.md` v0.2（5+1 iterate 共通基底；Wave 12 SKILL.md 對應 protocol）
- `.claude/skills/iterate-*/SKILL.md` v0.1 + 5 中文 wrapper（10th master Wave 12 落地）
- `.claude/skills/view-*/SKILL.md` v0.1 + 4 中文 wrapper（9th master Wave 13 落地）
- `.claude/skills/export-*/SKILL.md` v0.1 + 4 中文 wrapper（9th master Wave 14 落地）
- `.claude/skills/diagnose/SKILL.md` + `integrate/SKILL.md` v0.1 + 2 中文 wrapper（9th master Wave 15 落地）

---

**祝第十一輪 master 維護期順利。Milestone 4 真正封版完成 → 工具 A 進入「能跑量產 + 維護期」階段；11+ 輪 master 可彈性選擇路徑 B（NEW_REQ_16 lint script spec 規劃）或更晚 master 啟動 NEW_REQ_11 工具 B 翻譯工具 fork / Canon Delta skill 真正實作。**


---

# 9. 11th master 對話 A reframe amendment（v1.1 partial supersede）

## 9.1 reframe 背景

10th master Milestone 4 真正封版宣告完成後，11th master 對話 A（Cowork）依本檔 §1 對話啟動指令啟動，原預期跑「路徑 B：NEW_REQ_16 lint script spec 規劃」或「M4 user-test follow-up」。

但對話 A 啟動後立即承接 HANDOFF_11TH_PARALLEL_SETUP v0.1（user 拍板選並行模式甲 1 + 甲 b）：對話 A 跑 NEW_REQ_20 frontend patch 6-task 包；對話 B 跑 M4 user-test follow-up；對話 C 跑 Codex CLI 量產台詞。

對話 A 跑到一半，user 觀察到並 reframe 11th master scope（詳 NEW_REQ_22）：

- 工具 A 寫作 pipeline 受 base model 品質 ceiling 限制
- 11+ 輪累積 tech debt 規模大（NEW_REQ_9 baseline 老債 + NEW_REQ_16 未實作 + 51 SKILL.md dead code 風險 + POST_LOCK_PENDING 多項 DEFERRED 未巡檢 + K-NN 表跨 batch 累積 + D-055 編號衝突 manifest + commit 235debb 對 POST_LOCK_PENDING §5.3-§5.12 意外截斷 ~110 行設計史等）
- frontend dashboard 三欄區（NEW_REQ_20）等 alpha 階段 placeholder patch 屬「為短期 polish 做的 work 可能被覆蓋」

結論：工具 A 後續定位 = QA + 初始資料建置 + 專案管理 + 外接寫作；用 Claude Code 2026-05-28 ship 的 Dynamic Workflows 跑 sandbox 大重構。

## 9.2 對 §1 對話啟動指令的影響

§1 對話啟動指令所列「7 個 candidate 主軸」由 11th master 對話 A 重新分類：

| 原 §1 candidate 主軸 | v1.1 reframe 後狀態 |
|---|---|
| 1. M4 user-test follow-up（NEW_REQ_14 §6 補入）| **退場**；M4 user-test 屬「為將被替換的 in-tool 寫作 pipeline 做 test」ROI 大降；推延到大重構完成 + 工具新角色定型後再跑；機制本身保留待未來新 phase 結束時用 |
| 2. NEW_REQ_16 lint script spec 規劃 | **暫推延**；sandbox audit 結論可能對 lint script spec 提供需求輸入；屬未來 master scope |
| 3. NEW_REQ_15 D-054 hybrid trigger 監控 | **保留 monitor**；sandbox audit A3（大綱/細綱對齊）可能附帶觀察到 trigger 達成證據 |
| 4. NEW_REQ_9 baseline 老債清理 | **轉入 sandbox audit B1 / B3 範圍** |
| 5.（可選）NEW_REQ_11 工具 B 翻譯工具 fork | **不變**；M4 + 6 個月 + 4 個前置條件達成 + user 拍板後啟動 |
| 6.（可選）Canon Delta skill 真正實作 | **不變**；屬成熟期功能；CANON_DELTA_FRAMEWORK v0.1 framework reference 已預備 |
| 7.（可選）任何新議題 → 緊急 patch round | **不變**；如有新議題回升 user 拍板 D-056+ |

11th master 對話 A 新增主軸 8（reframe 後即本檔 v1.1 對應）：

8. **工具角色轉換 + Claude Code Dynamic Workflows audit 路徑**（NEW_REQ_22）
   - 戰略落地交接包：SANDBOX_REFACTOR_PLAN v0.1 + 本 HANDOFF v1.1 + HANDOFF_11TH_PARALLEL_SETUP v0.2 + POST_LOCK_PENDING v0.22 + 根 .gitignore + _sandbox/README.md
   - user 親跑 Claude Code Dynamic Workflows sandbox audit（first-run A1 + B4 + C1）
   - master REVIEW + 人工 transcribe 結論回 production
   - 11 audit 任務全跑完 → 工具 A 進入「QA + 初始資料 + 專案管理工具」穩定維護期

## 9.3 對 §3 路徑 A-E 的影響

§3 列「5 個推薦路徑供 user 選擇」全部被 v1.1 partial supersede：

| 原 §3 路徑 | v1.1 reframe 後狀態 |
|---|---|
| 路徑 A 純 monitor + M4 user-test follow-up | 退場；M4 user-test 推延 |
| 路徑 B NEW_REQ_16 lint script spec 規劃（原推薦 default） | 推延；屬未來 master scope |
| 路徑 C NEW_REQ_16 + 17 自動化 QA 全層級實作 | 推延；依賴路徑 B |
| 路徑 D NEW_REQ_11 工具 B 翻譯工具 fork | 不變；長期 trigger |
| 路徑 E Canon Delta skill 真正實作 | 不變；長期 trigger |

新路徑 F（v1.1 新增）：**Sandbox Dynamic Workflows audit 路徑**
- Stage 1：11th master 對話 A 戰略落地 6-task 包（已 land）
- Stage 2：user bootstrap sandbox + 親跑 Claude Code Dynamic Workflows first-run
- Stage 3：master REVIEW + 人工 transcribe + user 拍板採納 finding
- Stage 4：擴大 second-run / third-run audit；跑完 11 任務
- Stage 5：工具 A 進入穩定維護期 / 評估啟動路徑 D 或 E

## 9.4 對 §4 風險警示 + 重要紀律的影響

§4 既有 10th master 教訓 8-10 仍適用。11th master 對話 A 新增教訓 11：

**教訓 11（11th master 對話 A 新增；2026-06-01）：Edit tool 對 ~100 行以上中文新增內容仍有截斷風險**

- 11th master 對話 A 寫 POST_LOCK_PENDING v0.22 期間，用 Edit tool 插入 ~100 行 NEW_REQ_22 entry → 觸發 file mid-content truncation（§5.7 NEW_REQ_18 row 中斷在「屬 11+ 輪 master scope」處 UTF-8 broken）
- 對應 CLAUDE.md 教訓 6（長 multi-byte 檔 truncation 風險）
- **紀律：** 長中文 patch（~100 行以上）一律改用 Python script via bash 一次性 `open(path, "w")` write file 取代；不依賴 Edit tool partial replace；不依賴 cat heredoc（heredoc 對 Chinese-heavy content 可靠但缺邏輯化錯誤處理）
- 教訓 6 (cat heredoc) → 教訓 11 (Python script with utf-8 explicit + error handling) 升級

## 9.5 對 §5 完成條件的影響

§5 既有「5 個路徑各自完成條件」被新路徑 F 覆蓋。新完成條件：

| 階段 | 完成條件 |
|---|---|
| Stage 1 戰略落地（已達成）| 6-task 包全 land：SANDBOX_REFACTOR_PLAN v0.1 + POST_LOCK_PENDING v0.22 + 本 HANDOFF v1.1 + HANDOFF_11TH_PARALLEL_SETUP v0.2 + 根 .gitignore + _sandbox/README.md；GIT SUMMARY 給 user |
| Stage 2 sandbox bootstrap（user 拍板開始）| user 跑 PowerShell bootstrap + verify _sandbox/snapshot/ 完整 + .gitignore 排除生效 |
| Stage 3 first-run audit（user 親跑 Claude Code）| A1 + B4 + C1 三 audit 跑完 + audit-reports/ 內檔輸出 + user 帶 report 回 Cowork 11th master 對話 A |
| Stage 4 master REVIEW + transcribe（11th master 對話 A 繼續）| master cross-check + 標 fabricated finding + 採納建議 + user 拍板 + transcribe 採納 finding 進 production NEW_REQ_23+ 或 audit report |
| Stage 5 擴大 audit / 收尾（依 user 拍板擴大）| second-run / third-run 跑完 11 audit 任務；或 ROI 評估不佳則 stop |
| Stage 6 工具 A 維護期入口（長期）| audit pipeline 全跑完 + cleanup 完成 + 工具 A 角色穩定 = QA + 初始資料 + 專案管理 |

## 9.6 對 §7 對 user 的最終建議的影響

§7「立即可做的事」依 11th master 對話 A reframe 更新：

1. **commit + push 11th master 對話 A 戰略落地 6-task 包**（SANDBOX_REFACTOR_PLAN v0.1 + POST_LOCK_PENDING v0.22 + HANDOFF v1.1 + HANDOFF_11TH_PARALLEL_SETUP v0.2 + 根 .gitignore + _sandbox/README.md）→ Stage 1 收尾
2. **PowerShell sandbox bootstrap**（依 SANDBOX_REFACTOR_PLAN §2.2 指令；建 _sandbox/snapshot/ + audit-reports/）→ Stage 2
3. **切 Claude Code 跑 first-run audit**（A1 + B4 + C1；read-only mode；估 50K-130K token / 10-30 分）→ Stage 3
4. **帶 audit report 回 Cowork 11th master 對話 A**→ Stage 4 master REVIEW 起點
5. **不跑 M4 user-test**（屬退場 scope；不啟動原路徑 A）
6. **不啟動 NEW_REQ_16 lint script 實作**（屬暫推延；audit 結論可能對 spec 提供需求輸入）

## 9.7 Cross-ref

- `_design/POST_LOCK_PENDING.md` v0.22（NEW_REQ_22 + §5.13 評估 + §5.14 升 v0.22 紀律 + §5.15 §5.3-§5.12 restoration audit trail；本 v1.1 對應）
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（戰略落地核心檔；含 11 audit 任務 spec + sandbox bootstrap + first-run 建議 + 結論回流流程；本 §9.5 路徑 F Stage 2-5 對應）
- `_design/HANDOFF_11TH_PARALLEL_SETUP.md` v0.2（並行模式廢止 header note；對話 A reframe / 對話 B C 退場）
- 根 `.gitignore`（11th master 對話 A 新建；加 `/_sandbox/` 排除）
- `_sandbox/README.md`（11th master 對話 A 新建；sandbox 根目錄指引）
- 既有 §1-§8 仍有效（屬歷史紀錄；本 §9 amendment 為 partial supersede 不重寫）
- 教訓 11 對 CLAUDE.md 教訓 6 升級（Python script with utf-8 explicit + error handling）

---

**11th master 對話 A reframe 戰略落地完成 → 後續工作流：user bootstrap sandbox → user 親跑 Claude Code Dynamic Workflows → user 帶 audit report 回對話 A → master REVIEW + 人工 transcribe → user commit production → 重複 audit pipeline 直到 11 任務完。**
