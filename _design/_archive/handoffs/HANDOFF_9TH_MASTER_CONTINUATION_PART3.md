狀態：DRAFT  
版本：v1.0（9th master 第三段對話接手包；第二段 Wave 14-16 落地後切換點；Wave 16 Step 3 review + Step 4 finding 處理 + HANDOFF_TO_10TH_MASTER 撰寫 scope）  
最後更新：2026-05-22  
適用範圍：給「9th master 第三段對話」接手 — Wave 16 Step 3-4 + HANDOFF_TO_10TH_MASTER scope  
優先級：最高

# HANDOFF_9TH_MASTER_CONTINUATION_PART3 — 9th master 第三段對話接手包

# 0. 文件目的

9th master 第二段對話（2026-05-22）已完成：
- Wave 14（4 個 /export-* + 4 wrapper）
- Wave 15（/diagnose + /integrate + 2 wrapper + CANON_DELTA_FRAMEWORK v0.1）
- Wave 16 Step 1-2（CODEX_D_FINAL_STARTER + PHASE_D_COMPLETION_REPORT v1.0）

期間經歷一次嚴重 filesystem corruption incident（cloud sync / 防毒干擾 working tree + .git/）；user 修復後繼續。第二段對話累積 ~85% context 後切到第三段對話。

**本檔限縮 scope（vs PART2）：** 只覆蓋 9th master 第三段對話剩餘工作 — Wave 16 Step 3-4 + 三個 finding 處理 + HANDOFF_TO_10TH_MASTER 撰寫。Wave 12-15 / Wave 16 Step 1-2 已完成不再覆蓋。

---

# 1. 對話啟動指令（直接複製到新對話）

\`\`\`
我是 game-dialogue-bible 專案的使用者。9th master 第二段對話完成 Wave 14 + Wave 15 + Wave 16 Step 1-2 (PHASE_D_COMPLETION_REPORT v1.0 落地)。期間 Phase A.0F 平行對話跑得很快，已完成 A.0F.3 + A.0F.4 + A.0F.5 + A.0F.10 (L3 Export 核心) + A.0F.11 (Asset Panel)。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「9th master 第三段對話」。

**第一步必讀（按順序，4 份；最小化）：**
1. _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md（本檔；你的 scope）
2. _design/PHASE_D_COMPLETION_REPORT.md v1.0（第二段 Step 1-2 落地的事實檔；含 §8 三個 finding）
3. _design/POST_LOCK_PENDING.md v0.18（5 條教訓 + NEW_REQ 清單）
4. _design/HANDOFF_9TH_MASTER_CONTINUATION.md v1.0（PART2 接手包；含原 Wave 14-16 scope；只看 §4 風險警示）

**第二步精選讀（碰到才看）：**
5. _design/CODEX_D_FINAL_STARTER.md v0.1（第二段 Step 1 落地的 starter；含完整 4 維度驗收 + PHASE_D 9 段結構）
6. _design/HANDOFF_TO_9TH_MASTER.md v1.0（原 9th master 整體 scope；只看 §3.4-§3.5 Wave 14-15 範圍 + §4 風險警示）

**你的 scope（9th master 第三段；3 個 task）：**

1. **Wave 16 Step 3 — 跑 CODEX review starter（最終 milestone 完整 review）：**
   - 寫 _design/CODEX_D_FINAL_REVIEW_STARTER.md v0.1
   - 對齊 9th master 第二段對話 Round 1-4 review cycle pattern（POST_LOCK_PENDING v0.18 教訓 5 條內化）
   - diff anchor 必須用明示 commit hash 或 HEAD~1..HEAD（教訓 5）
   - CODEX 跑 4-6 維度重審
   - 若有 finding 走 inline patch 或 hard-limit accept 流程

2. **Wave 16 Step 4 — Milestone 4 接近條件聲明確認 + §8 三個 finding 處理：**
   - Finding 1（master ref 對齊）— 第二段對話結束前 user 已執行 cherry-pick；確認 master 含 4 個 Wave 15 SKILL.md
   - Finding 2（AGENTS.md / CLAUDE.md Phase D metadata drift）— 推 10th master scope；列入 PART3 + HANDOFF_TO_10TH_MASTER cleanup queue
   - Finding 3（Wave 12 SKILL.md 實作排序）— 推 10th master scope；建議 10th master 起手 priority 1

3. **寫 _design/HANDOFF_TO_10TH_MASTER.md v1.0：**
   - 對齊 HANDOFF_TO_9TH_MASTER.md v1.0 pattern
   - 接 Phase A.0F.6-A.0F.9 (4 個 feature) + 整體驗收 + Wave 12 SKILL.md 實作 + Milestone 4 真正封版宣告
   - 含 9th master 全程 (PART1 + PART2 + PART3) 教訓內化
   - 含 NEW_REQ_9/11/15/16/17/18/19 deferred 清單推 10th master 評估

**禁止越界（沿用 + 新增）：**
- 不重做設計（已 LOCKED）
- 不改 D-001~D-054 拍板結論
- 不擅啟 Phase A.0F 實作（A.0F 平行對話 scope；本對話不介入）
- 不重審 9th master 第一段/第二段已 accepted finding
- 不擅自實作 Wave 12 6 個 SKILL.md（屬 10th master scope）
- 不擅自啟動新 D-NNN 拍板（如有新議題 → 列入 HANDOFF_TO_10TH_MASTER 「待 10th 評估」）

**9th master 第一段 5 條教訓 + 第二段新增紀律（你必須在 Wave 16 Step 3 開始前 grok）：**
1. Master 跑 baseline 必須以 Windows 端為權威；sandbox virtiofs cache 屬 noise 對照
2. Cascade sweep 必須擴及 broader pattern grep
3. Master 寫 starter 涉 SPEC frontmatter 段須直接 grep SPEC §5.2 verify
4. Master 寫 supersede note 要避免重複 finding 內精確詞串
5. Master 寫 review starter 時 diff anchor 必須精確（用明示 commit hash 或 HEAD~1..HEAD）

**新紀律（第二段對話內化）：**
6. **寫長 multi-byte 檔請用 Python script via bash 或 cat heredoc**；不用 Write/Edit tool（Cowork tool 對長中文檔有截斷風險；本檔本身亦用 cat heredoc 寫入）
7. **Cloud sync / 防毒不得監控 working tree** — D:\劇本開發工具 必須加白名單；OneDrive 不能 sync 整個 repo；若發現 .git/*.lock + .lock.tmp + HEAD.lock 反覆出現 → 立刻暫停 cloud sync + 防毒實時掃描

**新工作模式（沿用第二段拍板）：**
- Master 寫 starter（review starter / HANDOFF）
- CODEX 跑 review task / user 端 git 操作
- Master 內部 verify

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 4 份必讀後對 scope + Wave 16 Step 3-4 工作順序 + 教訓 7 條內化的理解，再開始處理。
\`\`\`

---

# 2. 當前狀態快照（9th master 第二段對話結束時 — 2026-05-22）

## 2.1 設計層狀態

| 檔 | 版本 | 狀態 | 9th master 第二段對話變動 |
|---|---|---|---|
| _design/REQUIREMENTS_LOCK.md | v1.0 | FINAL | 不動 |
| _design/DECISIONS_LOG.md | v2.0 | FINAL | 不動（D-001~D-054 維持）|
| _design/INTEGRATION_CONTRACTS.md | v2.1 | LOCKED | 不動 |
| _design/SPEC.md | v1.2 | LOCKED | 不動 |
| _design/ARCHITECTURE.md | v1.6 | LOCKED | 不動 |
| _design/TASKS.md | v1.9 | LOCKED | 不動 |
| _design/DATA_FORMAT_SPEC.md | v0.4 | LOCKED | 不動 |
| _design/UPSTREAM_DOWNSTREAM_SPEC.md | v0.5 | LOCKED | 不動 |
| _design/UX_SPEC.md | v0.4 | LOCKED | 不動 |
| _design/L3_EXPORT_PROMPT_SCHEMA.md | v0.2 | LOCKED | 不動 |
| _design/POST_LOCK_PENDING.md | v0.18 | DRAFT | 不動（第二段不動 NEW_REQ；屬第一段已升 v0.18）|
| _design/D054_DECISION_PACKAGE.md | v0.2 | APPLIED | 不動 |
| _design/PHASE_C_COMPLETION_REPORT.md | v1.0 | DRAFT | 不動 |
| _design/PHASE_B_COMPLETION_REPORT.md | v1.4 | DRAFT | 不動 |
| _design/PHASE_A_COMPLETION_REPORT.md | v1.1 | DRAFT | 不動 |
| **_design/PHASE_D_COMPLETION_REPORT.md** | **v1.0** | **DRAFT** | **第二段 Step 1-2 新建（401 lines / 25309 bytes）** |
| **_design/CANON_DELTA_FRAMEWORK.md** | **v0.1** | **DRAFT** | **第二段 Wave 15 新建（framework reference；不實作 skill）** |
| **_design/CODEX_D10_STARTER.md** | **v0.1** | **DRAFT** | **第二段 Wave 14 新建** |
| **_design/CODEX_D_EXPORT_BATCH_STARTER.md** | **v0.1** | **DRAFT** | **第二段 Wave 14 新建** |
| **_design/CODEX_D14_STARTER.md** | **v0.1** | **DRAFT** | **第二段 Wave 15 新建** |
| **_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md** | **v0.1** | **DRAFT** | **第二段 Wave 15 新建** |
| **_design/CODEX_D_FINAL_STARTER.md** | **v0.1** | **DRAFT** | **第二段 Wave 16 Step 1 新建（340 lines / 24558 bytes）** |

## 2.2 SKILL.md 落地狀態

| Wave | 英文主檔 | 中文 wrapper | 狀態 |
|---|---|---|---|
| 12 (5 + split-to-file) | iterate-world / iterate-character / iterate-relationship / iterate-outline / iterate-detailed-outline | 迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱 | ⏳ Starter only；SKILL.md 待 10th master 實作 |
| 13 (4) | view-world / view-character / view-outline / view-detailed-outline | 查看世界觀 / 查看角色 / 查看大綱 / 查看細綱 | ✅ 落地（9th master 第一段）|
| **14 (4)** | **export-world / export-character / export-outline / export-detailed-outline** | **匯出世界觀 / 匯出角色 / 匯出大綱 / 匯出細綱** | **✅ 落地（第二段 Wave 14）**|
| **15 (2)** | **diagnose / integrate** | **診斷 / 整理** | **✅ 落地（第二段 Wave 15）**|

## 2.3 Phase A.0F 平行對話進度（第二段對話結束時 — 重要 update）

frontend-tools-a0f branch commit history（latest first）：

| commit | feature | status |
|---|---|---|
| 1357247 | **A.0F.10 🌟 L3 Export panel + Prompt 生成器（核心）** | ✅ 落地 |
| 7b72454 | A.0F.11 Asset Panel 完整版（7 subtype + 缺檔警示）| ✅ 落地 |
| 25d919f | A.0F.4 F6 搜尋 + 篩選 facet（Scene Queue）| ✅ 落地 |
| e4721e9 | A.0F.3 F2 Scene Queue + Scene Detail（cockpit, read-only）+ GET /api/scenes endpoint | ✅ 落地 |
| 989de19 | A.0F.5 CopyCommandButton 通用元件 | ✅ 落地 |
| d6ec085 | **Wave 15 SKILL.md (×4) — 跨入 frontend-tools-a0f branch**（user 第二段結束前 cherry-pick 到 master）| ✅ 落地 |

**Milestone 4 真正封版條件已大幅推進**：
- 原 10th master scope = A.0F.3-A.0F.11 全部 (11 feature) + Wave 12 SKILL.md
- 現在 10th master scope = A.0F.6 ~ A.0F.9 (4 feature) + 整體驗收 + Wave 12 SKILL.md

## 2.4 Baseline（Windows 端權威）

- check_headers.py: 0 ERROR / 46 WARN / 173-174 files（第二段對話新增 4 個檔 + Wave 15 落地 +1 WARN long note pattern）
- check_paths.py: **247 ERROR**（R2-MAJOR-03 hard-limit accept 維持；NEW_REQ_9 既有 baseline debt 推 10th master）
- build_repo_index('.'): 0 ERROR / 83 WARN / ~244 files

**第三段對話 baseline 門檻：** check_paths.py ≤ 247 ERROR（同第二段；Windows 端權威）

## 2.5 第二段對話已完成（細節摘要；第三段不必重做）

### Phase 1：Wave 14 — 4 個 /export-* + L3 schema 對齊備忘
- CODEX_D10_STARTER.md v0.1（共通範本；含 §Z 前端工具友好性紀律 + L3 schema 對齊備忘）
- CODEX_D_EXPORT_BATCH_STARTER.md v0.1（D11-D13 batch starter）
- 8 SKILL.md 落地（export-world / export-character / export-outline / export-detailed-outline + 4 中文 wrapper）
- D13 含 D-054 hybrid fallback 完整 3 Phase

### Phase 2：Wave 15 — /diagnose + /integrate + Canon Delta framework
- CODEX_D14_STARTER.md v0.1（共通範本）
- CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md v0.1（D15 batch starter）
- CANON_DELTA_FRAMEWORK.md v0.1（framework reference；對齊 UD §5；不實作 skill）
- 4 SKILL.md 落地（diagnose / integrate + 診斷 / 整理 wrapper）
- /diagnose 對齊 00_a §3.3（6 段診斷報告 + 三種使用模式 + 純讀取邊界 8 條）
- /integrate 對齊 00_a §3.4（Stage 4a 印 diff / 4b 寫檔 + 邊界四 block + D-054 hybrid 保留）

### Phase 3：Wave 16 Step 1-2 — Phase D 整體驗收 starter + report
- CODEX_D_FINAL_STARTER.md v0.1（4 維度驗收 + PHASE_D_COMPLETION_REPORT 9 段結構 + §8 10th master scope）
- PHASE_D_COMPLETION_REPORT.md v1.0（401 lines / 25309 bytes；4 維度全 PASS + Milestone 4 雙判定 + §8 三 finding）

### Phase 4：Filesystem corruption incident + 修復
- Phase A.0F 平行對話 inventory 發現 26 個檔 truncated + 2 個 null bytes corruption
- 根因：cloud sync / 防毒實時掃描 working tree + .git/
- 修復：暫停 sync + git stash + git checkout HEAD -- . + 刪 .lock 檔
- 新紀律：寫長 multi-byte 檔用 Python via bash / cat heredoc；不用 Write/Edit tool

---

# 3. 9th master 第三段對話工作清單

## 階段 1：讀完 4 份必讀 + 接受第二段 handoff（15-30 分）

按順序讀 + 確認對 scope / Wave 16 Step 3-4 工作順序 / 教訓 7 條內化的理解。

## 階段 2：Wave 16 Step 3 — 跑 CODEX review starter（最終 milestone 完整 review）

### 新工作模式（沿用第二段 Wave 14-15）

- Master 寫完整 CODEX_D_FINAL_REVIEW_STARTER.md
- CODEX 跑 4-6 維度重審
- Master 內部 verify review report

### CODEX_D_FINAL_REVIEW_STARTER 核心內容

對齊 Round 1-4 review cycle 4 輪 starter pattern（第二段對話沒寫 review starter；第一段對話寫過 4 輪）+ Phase B/C 收尾 review 模式。

關鍵 review 範圍：
- 4 維度驗收 PHASE_D_COMPLETION_REPORT v1.0 內容是否嚴謹
- §8 三 finding 是否覆蓋全部議題
- master ref 對齊狀態（cherry-pick 後）
- baseline 是否真實對齊（Windows 端 247 ERROR）
- 邊界 5 條是否完整明示（含本 Wave 不擅自實作 Wave 12 SKILL.md + 不擅自寫 HANDOFF_TO_10TH_MASTER）
- 9 段結構是否齊全 + 跟 PHASE_C/PHASE_B/PHASE_A 對齊度

**diff anchor 紀律（教訓 5）：** 用明示 commit hash 或 HEAD~1..HEAD 限定最後一個 commit；避免框住 immutable history。

### 預估工時

- Master 寫 review starter：30-60 分
- CODEX 跑 review（user 端外部）：~2-3h
- Master 內部 review report：15-30 分

## 階段 3：Wave 16 Step 4 — Milestone 4 接近條件聲明確認 + 三個 finding 處理

### Finding 1：master ref 對齊（第二段對話結束前 user 已執行 cherry-pick）

確認 master HEAD 包含 4 個 Wave 15 SKILL.md：
\`\`\`
git log master --oneline -10
git show <new-commit-hash> --stat
\`\`\`

若 cherry-pick 成功 → Finding 1 RESOLVED；PHASE_D_COMPLETION_REPORT v1.0 §8 Finding 1 可標 ✅ 處理完。

### Finding 2：AGENTS.md / CLAUDE.md Phase D metadata drift

推 10th master scope（列入 HANDOFF_TO_10TH_MASTER cleanup queue）。本 Wave 不擅自改 AGENTS.md / CLAUDE.md。

### Finding 3：Wave 12 SKILL.md 實作排序

推 10th master scope（建議 10th master 起手 priority 1；列入 HANDOFF_TO_10TH_MASTER）。本 Wave 不擅自實作。

### 預估工時

- 30-60 分

## 階段 4：寫 _design/HANDOFF_TO_10TH_MASTER.md v1.0

### 對齊 HANDOFF_TO_9TH_MASTER.md v1.0 pattern

| 章節 | 做什麼 |
|---|---|
| §0 文件目的 | 9th master 全程已完成事實（PART1 + PART2 + PART3）|
| §1 對話啟動指令 | 複製到新對話的 prompt |
| §2 當前狀態快照 | 設計層 / SKILL.md / Phase A.0F / baseline / 已完成事實 |
| §3 10th master 工作清單 | A. Phase A.0F.6-A.0F.9 + 整體驗收 / B. Wave 12 SKILL.md 實作 / C. Milestone 4 真正封版宣告 / D. NEW_REQ backlog 重新評估 |
| §4 風險警示 | 7 條教訓（5 條第一段 + 2 條第二段 corruption / Python via bash）+ Phase A.0F 平行對話 commit history + NEW_REQ deferred 清單 |
| §5 完成條件 | Milestone 4 真封版 checklist |
| §6 文件維護紀律 | archive 規則 |
| §7 對 user 最終建議 | Phase E / 工具 B 路徑 + 維護期建議 |
| §8 Cross-ref | 所有相關檔 |

### 關鍵 wording 紀律

- **Milestone 4 真正封版** ≠ Milestone 4 接近條件達成
- 真正封版 = Phase A.0F 整體驗收完成 + Wave 12 SKILL.md 全落地
- 10th master 完成後寫 PHASE_D_COMPLETION_REPORT v1.x partial supersede 「接近條件達成」→「達成」

### 預估工時

- 1.5-2h

## 階段 5：（可選）完成後 archive PART2 + PART3 接手包

第三段對話完成後可把：
- _design/HANDOFF_9TH_MASTER_CONTINUATION.md（PART2）→ _design/archive/
- _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md（本檔）→ _design/archive/

---

# 4. 風險警示 + 紀律

## 4.1 Context window 管理

第三段對話內也要小心 context 累積。預估工作量：

| 階段 | Master 工時 | Context 消耗預估 |
|---|---|---|
| Wave 16 Step 3（review starter + CODEX 跑 + verify report）| 1-2h | ~25-30% |
| Wave 16 Step 4（finding 處理）| 30-60 分 | ~5% |
| HANDOFF_TO_10TH_MASTER | 1.5-2h | ~30-35% |

**total 預估 60-70% context**。應在第三段對話內 fit 得下；不必再切第四段。

## 4.2 嚴守第二段新增紀律

### 4.2.1 寫長 multi-byte 檔用 Python via bash 或 cat heredoc

\`\`\`bash
# 用 cat heredoc 寫長 markdown 檔
cat > /sessions/.../mnt/劇本開發工具/_design/CODEX_D_FINAL_REVIEW_STARTER.md << 'UNIQUE_SENTINEL_2026'
... 完整內容（含中文 / 特殊符號全部 literal 不被 expand）...
UNIQUE_SENTINEL_2026

# 寫完跑 verify
python3 -c "
data = open('path', 'rb').read()
print(f'bytes: {len(data)}')
print(f'null bytes: {data.count(bytes([0]))}')
try:
    data.decode('utf-8')
    print('utf8: PASS')
except UnicodeDecodeError as e:
    print(f'utf8: FAIL - {e}')
"
\`\`\`

**不用 Write/Edit tool 寫長中文檔**（Cowork tool 對長 multi-byte 檔有截斷風險）。

### 4.2.2 Cloud sync / 防毒不得監控 working tree

D:\劇本開發工具 必須加白名單：
- OneDrive / Dropbox / Google Drive sync **不能監控**
- Windows Defender / 防毒軟體 **加白名單**（特別 .git/ 目錄）

若發現以下症狀 → 立刻暫停 cloud sync + 防毒：
- .git/index.lock 反覆出現
- .git/index.lock.tmp 出現
- .git/HEAD.lock 出現
- working tree 檔被截斷或填 null bytes

修復步驟（已驗證 work）：
\`\`\`
1. 暫停 cloud sync + 防毒實時掃描
2. Kill git.exe / bash.exe / wsl.exe process
3. del .git\*.lock / .git\*.lock.tmp
4. git stash push -u -m "pre-restore"
5. git checkout HEAD -- .
6. git status verify clean
7. 依 stash 內容判斷恢復 untracked 檔
\`\`\`

## 4.3 嚴守第一段 5 條教訓內化

1. **Windows baseline 權威**：sandbox virtiofs cache 在某些 case false negative；以 Windows 端為準
2. **Cascade sweep broader pattern**：寫好檔後跑 grep 全掃 stale cross-ref
3. **SPEC frontmatter 段直接 grep verify**：寫 starter 涉 frontmatter 描述前直接 grep SPEC §5.2
4. **Supersede note 避重複精確詞串**：用「修補性質」描述
5. **Review starter diff anchor 精確**：用明示 commit hash 或 HEAD~1..HEAD

## 4.4 9th master 第二段 review 模式（vs 第一段 CODEX review starter）

第二段對話 Wave 14/15 跳過 CODEX review starter；改 master 端內部 verify（grep 結構 + Read 重點 section）。理由：
- Round 1-4 cycle 4 輪 wall-time 證明 CODEX review starter cycle 太長
- 第二段 Wave 14/15 內部 verify PASS（4+8 個 SKILL.md 結構齊全）

**第三段建議：**
- Wave 16 Step 3 跑 CODEX review starter（屬最終 milestone；屬重要 gate；不省略）
- diff anchor 用 master HEAD~3..HEAD（cherry-pick + PHASE_D report + 第二段最後 commit）或明示 commit hash 限定 PHASE_D_COMPLETION_REPORT v1.0 落地段

## 4.5 sandbox virtiofs cache stale（已知）

工作目錄 Windows 端為權威。Sandbox 端 git status / wc -l / ls mtime 偶爾顯示 stale。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 4.6 不擅自越界

- ✗ 不重做設計（已 LOCKED v1.0~v2.0）
- ✗ 不改 D-001~D-054 拍板結論
- ✗ 不擅啟 Phase A.0F 實作（屬 A.0F 平行對話 scope；本對話不介入）
- ✗ 不重審第一段/第二段已 accepted finding
- ✗ 不擅自實作 Wave 12 6 個 SKILL.md（屬 10th master scope）
- ✗ 不擅自啟動新 D-NNN 拍板
- ✗ 不擅自改 LOCKED 模板 / AGENTS.md / CLAUDE.md（屬 10th master cleanup queue）

---

# 5. 完成條件

9th master 第三段對話完成 = 以下全部 ✓：

\`\`\`
✓ Wave 16 Step 3 — CODEX_D_FINAL_REVIEW_STARTER.md 寫好 + CODEX 跑 review + master verify
✓ Wave 16 Step 4 — Milestone 4 接近條件聲明確認 + 三 finding 處理 (Finding 1 RESOLVED；Finding 2/3 推 10th master)
✓ HANDOFF_TO_10TH_MASTER.md v1.0 落地（對齊 HANDOFF_TO_9TH_MASTER pattern）
✓ （可選）PART2 + PART3 接手包 archive
\`\`\`

---

# 6. 文件維護紀律

- 本檔是「接手指南」；第三段對話讀完後**不需要更新本檔**
- 第三段完成後可把本檔 archive 進 _design/archive/
- 真正完整 HANDOFF_TO_10TH_MASTER.md 由第三段對話寫；對齊 HANDOFF_TO_9TH_MASTER v1.0 pattern

---

# 7. Cross-ref

- _design/HANDOFF_9TH_MASTER_CONTINUATION.md v1.0（PART2 接手包；含原 Wave 14-16 scope）
- _design/HANDOFF_TO_9TH_MASTER.md v1.0（原 9th master 整體 scope；Wave 14-15 範圍可參考）
- _design/PHASE_D_COMPLETION_REPORT.md v1.0（第二段 Step 1-2 落地的事實檔；含 §8 三個 finding）
- _design/POST_LOCK_PENDING.md v0.18（5 條教訓 + NEW_REQ 清單）
- _design/CODEX_D_FINAL_STARTER.md v0.1（第二段 Step 1 落地的 starter）
- _design/PHASE_C_COMPLETION_REPORT.md v1.0（pattern 對齊範本）
- _design/PHASE_B_COMPLETION_REPORT.md v1.4
- _design/PHASE_A_COMPLETION_REPORT.md v1.1
- _design/CANON_DELTA_FRAMEWORK.md v0.1（第二段 Wave 15 新建）
- _design/CODEX_D10_STARTER.md v0.1 + CODEX_D_EXPORT_BATCH_STARTER.md v0.1（Wave 14 starter）
- _design/CODEX_D14_STARTER.md v0.1 + CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md v0.1（Wave 15 starter）
- _design/CODEX_C_FINAL_STARTER.md v0.1（review starter pattern 對齊）
- _design/D054_DECISION_PACKAGE.md v0.2（D-054 hybrid 拍板包）
- .claude/skills/export-*/SKILL.md v0.1 + 4 中文 wrapper（Wave 14 落地）
- .claude/skills/diagnose/SKILL.md v0.1 + 診斷 wrapper v0.1（Wave 15 落地）
- .claude/skills/integrate/SKILL.md v0.1 + 整理 wrapper v0.1（Wave 15 落地）
