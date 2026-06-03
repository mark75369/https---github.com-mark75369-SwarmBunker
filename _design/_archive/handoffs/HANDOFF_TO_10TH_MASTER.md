狀態：DRAFT  
版本：v1.0（9th master 第三段對話收尾交接包；Phase D 接近條件達成 + Wave 13/14/15 SKILL.md 全落地 + PHASE_D_COMPLETION_REPORT v1.0 落地 + Round 1-4 review cycle hard-limit accepted + 9th master 全程教訓 7 條內化；Milestone 4 真正封版交棒 10th master）  
最後更新：2026-05-22  
適用範圍：給「第十輪整合 master」對話的接手包 — Phase A.0F 前端工具 audit 收尾 + Wave 12 SKILL.md 實作 + AGENTS.md / CLAUDE.md Phase D metadata cleanup + Milestone 4 真正封版宣告 + NEW_REQ deferred backlog 重新評估  
優先級：最高

# HANDOFF_TO_10TH_MASTER — 第十輪整合 master 對話接手包

# 0. 文件目的

第九輪 master 對話（2026-05-21 → 2026-05-22）跨三段完成 **Phase D 接近條件達成宣告 + Milestone 4 接近條件達成（非達成）**：

- **第一段（2026-05-21）：** 9th master cleanup queue (NEW_REQ_19) Path A hard-limit accept + Phase D Wave 12 starter set（5 個 D starter + 00_j 迭代協議 v0.2 + `/iterate-scene --split-to-file` D-054 NEW_REQ_15 落地）+ Phase D Wave 13 4 個 /view-* SKILL.md + 4 中文 wrapper 落地 + Round 1-4 review cycle 4 輪 inline patch（含 R10-MA-01 / R1-MA-02 設計拍板 a / R2-MAJOR-03 hard-limit accept / R4-MAJOR-01 hard-limit accept 等）→ 視為 GO 進 Wave 14
- **第二段（2026-05-22）：** Phase D Wave 14（4 個 /export-* SKILL.md + 4 中文 wrapper + CODEX_D10_STARTER §Z L3 schema 對齊備忘）+ Phase D Wave 15（/diagnose + /integrate + 2 中文 wrapper + CANON_DELTA_FRAMEWORK v0.1 framework reference）+ Wave 16 Step 1-2（CODEX_D_FINAL_STARTER + PHASE_D_COMPLETION_REPORT v1.0 落地；4 維度全 PASS + Wave 12 SKILL.md partial state 明示 + Milestone 4 接近條件達成宣告非達成）+ filesystem corruption incident 修復（cloud sync / 防毒監控導致 .git/*.lock + truncation；修復後內化新紀律 — 寫長 multi-byte 檔用 cat heredoc / Python script via bash）
- **第三段（2026-05-22 收尾）：** Wave 16 Step 3 CODEX_D_FINAL_REVIEW_STARTER v0.1 落地（用明示 6 個 commit hash diff anchor 教訓 5）+ Wave 16 Step 4 三 finding 處理（Finding 1 master ref 對齊由 user 接續 cherry-pick / Finding 2 AGENTS.md / CLAUDE.md Phase D metadata drift 推 10th master / Finding 3 Wave 12 SKILL.md 實作排序推 10th master priority 1）+ 本檔 HANDOFF_TO_10TH_MASTER v1.0 落地

期間累積 NEW_REQ deferred backlog：NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18 / NEW_REQ_19（9th master cleanup queue 已 Path A hard-limit accept 結案）。

第十輪 master 對話接手 **Milestone 4 真正封版** 的最後缺口：

1. **Phase A.0F 前端工具 audit 收尾**（平行對話進行中；Round 2 review 階段；10th master 接手時 actual A.0F state 應 verify via git log）
2. **Wave 12 SKILL.md 實作**（5 個 /iterate-* + /iterate-scene --split-to-file = 6 SKILL.md + 5 中文 wrapper；建議 10th master 起手 priority 1）
3. **AGENTS.md / CLAUDE.md Phase D metadata drift cleanup**（Phase D Wave 13/14/15 落地 + Wave 12 partial state 同步）
4. **Milestone 4 真正封版宣告**（PHASE_D_COMPLETION_REPORT v1.x partial supersede 把「接近條件達成」升「達成」）
5. **NEW_REQ deferred backlog 重新評估**（NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18）

**預估第十輪總工時：** Phase A.0F audit 收尾 1-3h（依當前 audit Round 2 review 結果而定）+ Wave 12 SKILL.md master 對話 3-5h + CODEX 跑 Wave 12 6 skill 6-10h（可並行）+ AGENTS.md / CLAUDE.md cleanup 30-60 分 + Milestone 4 封版宣告 30-60 分 + NEW_REQ backlog 重新評估 30-60 分

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。9th master 對話跨三段完成 Phase D 接近條件達成宣告 + Milestone 4 接近條件達成（非達成）：Wave 13/14/15 SKILL.md 全落地（10 個英文主檔 + 10 個中文 wrapper）+ Wave 12 starter set 落地（5 個 D starter + 00_j v0.2；6 個 SKILL.md 推 10th master）+ PHASE_D_COMPLETION_REPORT v1.0 4 維度 PASS + CANON_DELTA_FRAMEWORK v0.1 framework reference + L3 schema 對齊備忘。

期間 Phase A.0F 平行對話跑得很快，已完成 A.0F.3-A.0F.11（11 個 feature）+ 整體驗收 + integration test + user manual v0.2，目前在 A.0F audit cycle Round 2 review 階段。10th master 接手時請 verify actual A.0F audit cycle state via git log。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第十輪整合 master」對話。

**第一步必讀（按順序，8 份）：**
1. _design/HANDOFF_TO_10TH_MASTER.md（本檔；你的 scope）
2. _design/PHASE_D_COMPLETION_REPORT.md v1.0（Phase D 接近條件達成事實檔；含 §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制 + §8 三 finding 處理紀錄）
3. _design/CODEX_D_FINAL_REVIEW_REPORT.md v0.1（9th master 第三段 Wave 16 Step 3 review report；GO / NEAR-GO / NO-GO 判定紀錄；若為 NEAR-GO hard-limit accept 或 NO-GO patch round 結果應確認）
4. _design/POST_LOCK_PENDING.md v0.18（NEW_REQ 整體狀態；含 NEW_REQ_19 9th master cleanup queue Path A hard-limit accepted + Round 1-4 教訓內化）
5. _design/DECISIONS_LOG.md v2.0（D-001~D-054 全部 LOCKED）
6. _design/REQUIREMENTS_LOCK.md v1.0 FINAL（north star 不動）
7. _design/CANON_DELTA_FRAMEWORK.md v0.1（成熟期功能 framework reference；11+ 輪 master / 工具 B 翻譯工具 fork 用；不實作 skill）
8. _design/HANDOFF_TO_9TH_MASTER.md v1.0（9th master 整體 scope；本檔接續；§4 風險警示與紀律仍適用）

**第二步精選讀（碰到才看）：**
9. _design/TASKS.md v1.9 §A.0F + §C（Phase A.0F 前端工具 spec + Phase D 視圖/迭代/匯出/整合 task spec）
10. _design/CODEX_D1_STARTER.md v0.3 ~ _design/CODEX_D5_STARTER.md v0.4（Wave 12 starter set 5 個；Wave 12 SKILL.md 實作的權威 reference）
11. _design/UX_SPEC.md v0.4 §11（Phase A.0F 11 個 feature spec；audit cycle close-out reference）
12. _design/CODEX_PHASE_A0F_REVIEW_REPORT.md（Phase A.0F audit cycle review report；最新狀態）
13. _design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md（Phase A.0F audit cycle Round 2 review starter；當前 review 階段）
14. _design/ARCHITECTURE.md v1.6 §6.4 + §6.5 + §6.6 + §6.7（Phase D 整體架構 — view / iterate / export / diagnose+integrate）
15. _design/D054_DECISION_PACKAGE.md v0.2（D-054 拍板包 APPLIED；Wave 12 /iterate-scene --split-to-file 設計）
16. _design/HANDOFF_9TH_MASTER_CONTINUATION.md v1.0 + _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md v1.0（9th master 第二段 + 第三段接手包；context only — archive 候選）

**你的 scope（10th master；5 個主軸 + 1 個可選）：**

1. **Phase A.0F 前端工具 audit 收尾**（依當前 git log actual state 而定）：
   - 確認 audit cycle Round 2 review 結果（PASS / NEAR-GO / NO-GO）
   - 若 PASS → A.0F 整體驗收已 land；可直接進主軸 2
   - 若 NEAR-GO / NO-GO → 跑 patch round 收尾（依當前 audit pattern）
   - 完成後寫 PHASE_A0F_COMPLETION_REPORT.md（或在 PHASE_D_COMPLETION_REPORT v1.x partial supersede 內納入）

2. **Wave 12 SKILL.md 實作（建議 priority 1）：**
   - 5 個 /iterate-* SKILL.md（iterate-world / iterate-character / iterate-relationship / iterate-outline / iterate-detailed-outline）+ 5 個中文 wrapper（迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱）
   - 1 個 /iterate-scene --split-to-file SKILL.md（D-054 NEW_REQ_15 落地；依 D5 starter 無中文 wrapper）
   - 對齊 D1-D5 starter（_design/CODEX_D1_STARTER.md v0.3 ~ _design/CODEX_D5_STARTER.md v0.4）+ 00_protocol/00_j_迭代協議.md v0.2 共通基底
   - 嚴守 D-050 子裁決 1+2 邊界（不寫 00_protocol；exception block 對齊 D-053；寫檔目錄表）
   - 嚴守 D-054 hybrid fallback（aggregate 06_a 預設 + /iterate-scene --split-to-file 拆出選項；對齊 scene-task 既有範本）
   - 含 frontmatter（name / description）+ 中文 5 必填 header + 11 段結構對齊 D1 範本

3. **AGENTS.md / CLAUDE.md Phase D metadata drift cleanup：**
   - Phase D Wave 13/14/15 SKILL.md 從 TBD → ✅ 已實作
   - Wave 12 6 個 SKILL.md（5 /iterate-* + /iterate-scene + 5 wrapper）依 10th master 實作進度逐步更新
   - 對齊 PHASE_D_COMPLETION_REPORT v1.0 §8 Finding 2
   - 不要動 LOCKED spec / SKILL.md 內容；只動 metadata 表格

4. **Milestone 4 真正封版宣告：**
   - 寫 _design/PHASE_D_COMPLETION_REPORT.md v1.x partial supersede 或 _design/PHASE_A0F_COMPLETION_REPORT.md（10th master 依 audit close-out 結果決定 wording 策略）
   - 「Milestone 4 接近條件達成」→「Milestone 4 真正達成」
   - 條件達成判定：Phase A.0F 11 個 feature + 整體驗收 全 PASS + Wave 12 6 個 SKILL.md + 5 wrapper 全落地 + AGENTS.md / CLAUDE.md Phase D metadata 對齊
   - §6 user 親跑 placeholder 待 user 跑 M4 chain（可選 NEW_REQ_14 AI-assisted §6 補入機制）

5. **NEW_REQ deferred backlog 重新評估：**
   - NEW_REQ_9（check_paths Windows vs sandbox baseline 差異 + 既有 baseline debt 27 模板 old-style filename reference 大寫格式 01A/01B/02A/05D 等）— 屬 LOCKED 模板需 D-055+ 拍板；10th master 評估是否動 LOCKED 模板（風險高）或設計 lint script 緩解（NEW_REQ_16 路徑）
   - NEW_REQ_11（翻譯工具分支提案）— DEFERRED 至工具 A 真正封版後（屬 11+ 輪 master scope；本輪不啟動）
   - NEW_REQ_15（D-054 hybrid 迭代評估）— DEFERRED 至 user 實際使用後 trigger（10th master 期間 monitor trigger A/B/C/D 達成情況）
   - NEW_REQ_16（自動化 QA Layer 1 cross-ref consistency lint script）— DEFERRED 至 Phase D / 維護期；10th master 可考慮起手實作（屬封版後維護期 ROI 高）
   - NEW_REQ_17（自動化 QA Layer 2 auto-patcher）— DEFERRED 至 NEW_REQ_16 落地後（11+ 輪 master scope）
   - NEW_REQ_18（自動化 QA Layer 3 nightly AI-driven semantic review）— DEFERRED 至 NEW_REQ_16/17 落地後 + 翻譯工具 fork 前評估（11+ 輪 master scope）

6. **（可選）若 user 有新 finding → 緊急 patch round**（同 D-049 / D-051 / D-053 / D-054 模式；如有新議題 → 10th master 才開 D-055+ 拍板）

**禁止越界（嚴守 LOCKED spec + 9th master 全程教訓）：**
- ✗ 不重做設計（已 LOCKED v1.0~v2.0）
- ✗ 不改 D-001~D-054 拍板結論（要動需 user 拍板新 D-055+）
- ✗ 不重審 9th master 第一段 Round 1-4 + 第二段 Wave 14/15 內部 verify + 第三段 Wave 16 Step 3 review 已 accepted finding
- ✗ 不重審 Wave 13/14/15 SKILL.md 結構（已 PASS；本輪只動 metadata）
- ✗ 不寫 Phase E / 工具 B 任何檔（屬 11+ 輪 master scope）
- ✗ 不擅自啟動新 D-NNN 拍板（如有新議題 → 先回升 user 拍板）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 8 份必讀後對 scope + 5 主軸工作順序 + 9th master 全程教訓 7 條內化的理解，再開始處理。
```

---

# 2. 當前狀態快照（9th master 第三段對話結束時 — 2026-05-22）

## 2.1 設計層狀態（spec 版本；9th master 全程不動 LOCKED）

| 檔 | 版本 | 狀態 | 9th master 全程變動 |
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
| `_design/POST_LOCK_PENDING.md` | v0.18 | DRAFT | 第一段升 v0.14 → v0.18（4 輪 NEAR-GO inline patch + 教訓 5 條內化）；第二段/第三段不動 |
| `_design/D054_DECISION_PACKAGE.md` | v0.2 | **APPLIED** | 不動 |
| `_design/PHASE_C_COMPLETION_REPORT.md` | v1.0 | DRAFT | 不動 |
| `_design/PHASE_B_COMPLETION_REPORT.md` | v1.4 | DRAFT | 不動 |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | DRAFT | 不動 |
| **`_design/PHASE_D_COMPLETION_REPORT.md`** | **v1.0** | **DRAFT** | **9th master 第二段 Wave 16 Step 2 新建（401 lines / 25309 bytes）** |
| **`_design/CANON_DELTA_FRAMEWORK.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 15 新建（framework reference；不實作 skill）** |
| **`_design/CODEX_D1_STARTER.md`** | **v0.3** | **DRAFT** | **9th master 第一段 Wave 12 新建 + Round 1-4 patch** |
| **`_design/CODEX_D2_STARTER.md`** | **v0.3** | **DRAFT** | **9th master 第一段 Wave 12 新建 + Round 1-4 patch** |
| **`_design/CODEX_D3_STARTER.md`** | **v0.3** | **DRAFT** | **9th master 第一段 Wave 12 新建 + Round 1-4 patch** |
| **`_design/CODEX_D4_STARTER.md`** | **v0.2** | **DRAFT** | **9th master 第一段 Wave 12 新建 + Round 1-4 patch** |
| **`_design/CODEX_D5_STARTER.md`** | **v0.4** | **DRAFT** | **9th master 第一段 Wave 12 新建 + Round 1-4 patch（D-054 /iterate-scene --split-to-file 落地）** |
| **`_design/CODEX_D6_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第一段 Wave 13 新建（D6 完整範本）** |
| **`_design/CODEX_D_VIEW_BATCH_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第一段 Wave 13 新建（D7-D9 batch）** |
| **`_design/CODEX_D10_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 14 新建（含 §Z L3 schema 對齊備忘）** |
| **`_design/CODEX_D_EXPORT_BATCH_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 14 新建（D11-D13 batch）** |
| **`_design/CODEX_D14_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 15 新建** |
| **`_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 15 新建** |
| **`_design/CODEX_D_FINAL_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第二段 Wave 16 Step 1 新建（340 lines / 24558 bytes）** |
| **`_design/CODEX_D_FINAL_REVIEW_STARTER.md`** | **v0.1** | **DRAFT** | **9th master 第三段 Wave 16 Step 3 新建（539 lines / 34695 bytes；用明示 6 commit hash diff anchor 教訓 5）** |
| **`00_protocol/00_j_迭代協議.md`** | **v0.2** | **DRAFT** | **9th master 第一段 Wave 12 升 v0.1 → v0.2（5+1 iterate 共通基底）** |

## 2.2 SKILL.md 落地狀態（Phase A/B/C 全落地；Phase D 13/14/15 落地；Wave 12 partial）

| Phase | Wave | 英文主檔 | 中文 wrapper | 狀態 |
|---|---|---|---|---|
| A | 1-5 | /init-project / /create-world / /status / /check-gaps | 初始化專案 / 建立世界觀 / 進度 / 缺漏檢查 | ✓ Milestone 1 達成 |
| B | 6-8 | /create-character / /create-relationship / /create-outline / /create-detailed-outline | 建立角色 / 建立關係 / 建立大綱 / 建立細綱 | ✓ Milestone 2 達成 |
| C | 9-11 | /scene-task / /dialogue-write / /qa | 場景任務包 / 生成台詞 / 檢查 | ✓ Milestone 3 達成 |
| D | **12** | iterate-world / iterate-character / iterate-relationship / iterate-outline / iterate-detailed-outline / iterate-scene | 迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱 | **⏳ Starter only；6 SKILL.md + 5 wrapper 待 10th master 實作（priority 1）**|
| D | 13 | view-world / view-character / view-outline / view-detailed-outline | 查看世界觀 / 查看角色 / 查看大綱 / 查看細綱 | ✓ 落地（9th master 第一段）|
| D | 14 | export-world / export-character / export-outline / export-detailed-outline | 匯出世界觀 / 匯出角色 / 匯出大綱 / 匯出細綱 | ✓ 落地（9th master 第二段）|
| D | 15 | diagnose / integrate | 診斷 / 整理 | ✓ 落地（9th master 第二段）|

**統計：**
- Phase A/B/C：12 個英文主檔 + 8 中文 wrapper = 20 SKILL.md
- Phase D Wave 13/14/15：10 個英文主檔 + 10 中文 wrapper = 20 SKILL.md
- Phase D Wave 12：⏳ 6 個英文主檔 + 5 中文 wrapper = 11 SKILL.md（10th master scope）
- **總落地：40 SKILL.md（不含 Wave 12 deferred）**

## 2.3 Phase A.0F 前端工具狀態（平行對話進行中；10th master 接手時應 verify actual git state）

frontend-tools-a0f branch 最新 commit history（截至 2026-05-22 ~10:20）：

| commit | feature | status |
|---|---|---|
| 1735d0a | audit-codex-patch-starter: NO-GO 後 patch round starter | ⏳ audit cycle Round 2 進行中 |
| 3829d48 | Phase A.0F.audit-codex-patch-starter | ⏳ patch round 進行中 |
| 2f7a1c1 | Phase A.0F.audit-codex-starter: CODEX REVIEW STARTER (user 拍板跨 scope) | ⏳ |
| e37cd3e | Phase A.0F.audit-test: regression locks (D-046 #5 引導文字 anchor + Bug 1 regression) | ✓ |
| 8afab68 | Phase A.0F.audit-doc: spec compliance disclosure (C1-C4) | ✓ |
| 32e15df | Phase A.0F.audit-P2: cleanup (dark mode hardcode + 3 dead code + .gitignore) | ✓ |
| 50348f7 | Phase A.0F.audit-P1: 修 Bug 1 + Bug 2 | ✓ |
| 499bc13 | 9th master 第二段對話收尾：PART3 handoff + D_FINAL starter | ✓ |
| a13ce5a | Phase A.0F 整體驗收：5 必要功能 + Export + Asset 全 land + integration test + user manual v0.2 | ✓ |
| 4c0c36e | Phase A.0F.6 + A.0F.7 + A.0F.8: F3 Scene Editor + LOCKED race guard + mtime conflict | ✓ |
| 1ea2b7c | Phase A.0F.9: 4 保留元件 — Workspace Home + Glossary + theme + 入口 | ✓ |
| 1357247 | Phase A.0F.10: 🌟 L3 Export panel + Prompt 生成器 (核心) | ✓ |
| 7b72454 | Phase A.0F.11: Asset Panel 完整版 — 7 subtype + 缺檔警示 | ✓ |
| 25d919f | Phase A.0F.4: F6 搜尋 + 篩選 facet (Scene Queue) | ✓ |
| e4721e9 | Phase A.0F.3: F2 Scene Queue + Scene Detail (cockpit, read-only) | ✓ |
| 989de19 | Phase A.0F.5: CopyCommandButton 通用元件 + delegated click handler | ✓ |

**重要 update（vs HANDOFF_TO_9TH_MASTER §4.4 + PART3 handoff §2.3）：**

- 9th master 第二段對話結束時：Phase A.0F 平行對話進度為 A.0F.3 + A.0F.4 + A.0F.5 + A.0F.10 + A.0F.11
- 9th master 第三段對話結束時（**本檔落地**）：Phase A.0F **11 個 feature 全 land + 整體驗收 + integration test + user manual v0.2** 已完成；目前在 **audit cycle Round 2 review** 階段
- 10th master 接手時應 verify `git log frontend-tools-a0f --oneline -30` actual state；audit cycle 可能已 PASS

**Milestone 4 真正封版條件已大幅推進：**
- 原 10th master scope（HANDOFF_TO_9TH_MASTER §4.4 預期）= A.0F.3-A.0F.11 全部（11 個 feature）+ Wave 12 SKILL.md
- 9th master 第二段對話結束時 scope = A.0F.6-A.0F.9 + 整體驗收 + Wave 12 SKILL.md
- 9th master 第三段對話結束時 scope（**本檔當前**）= **A.0F audit 收尾**（若 Round 2 PASS 則直接 close-out；NEAR-GO/NO-GO 走 patch round）+ Wave 12 SKILL.md

## 2.4 Baseline（Windows 端權威；9th master 第三段對話結束時 — 對齊 PHASE_D_COMPLETION_REPORT v1.0 §2 + 本檔 §3）

- `check_headers.py`: **0 ERROR / 49 WARN / ~176 files**（第三段新增 CODEX_D_FINAL_REVIEW_STARTER + HANDOFF_TO_10TH_MASTER + 第二段 PHASE_D_COMPLETION_REPORT + PART3 handoff + 多 starter 共 +3-4 WARN 屬既有 markdown header 長 note pattern；可接受）
- `check_paths.py`: **247 ERROR**（R2-MAJOR-03 hard-limit accept；NEW_REQ_9 既有 baseline debt 27 模板 old-style filename reference 推 10th master 評估）
- `build_repo_index('.')`: **0 ERROR / 85 WARN / ~246 files**

**10th master baseline 門檻：** check_paths.py ≤ 247 ERROR（同 9th master 全程；Windows 端權威）；若 10th master 動 NEW_REQ_9 LOCKED 模板需新 D-NNN 拍板。

## 2.5 9th master 第二段已寫入但 master 未 cherry-pick 的內容（10th master 接手時必確認）

第三段對話 Wave 16 Step 3 review starter 維度 3 已 flag 出 master ref 對齊狀態：

| ref | HEAD | 包含 |
|---|---|---|
| `master` / `origin/master` | `140af34` | ✓ Wave 14 SKILL.md（b94f741 / bd0920d）/ ✓ Wave 14 starters（f17d567）/ ✓ Wave 15 starters + CANON_DELTA（140af34 HEAD）/ ✗ Wave 15 SKILL.md / ✗ PHASE_D_COMPLETION_REPORT / ✗ CODEX_D_FINAL_STARTER / ✗ PART3 handoff / ✗ Wave 16 Step 3 review starter / ✗ 本 HANDOFF v1.0 |
| `frontend-tools-a0f` | （第三段對話結束時 HEAD）| ✓ 全部 9th master 第二段 + 第三段內容 + 全部 Phase A.0F.3-A.0F.11 + audit cycle |

**10th master 接手前 user 應決定的 ref 對齊策略：**

1. **選 A：master cherry-pick 模式** — 把 9th master 第二段 + 第三段所有 commit 從 frontend-tools-a0f cherry-pick 到 master；A.0F commit 不 cherry-pick（讓 A.0F merge 完後一次性 merge）
2. **選 B：完整 merge 模式** — 等 Phase A.0F audit close-out 後一次性把 frontend-tools-a0f merge 到 master；屆時所有第二段 + 第三段 + A.0F 全部一次性對齊
3. **選 C：rebase 模式** — 把 9th master commits rebase 到 master HEAD 後 push；不建議（破壞 immutable history）

**建議：選 B**（完整 merge）— 對齊 git 工作流 best practice；10th master 接手時 master 已含完整 Phase D + Phase A.0F；對 PHASE_D_COMPLETION_REPORT v1.x partial supersede 撰寫最 clean。

---

# 3. 第十輪工作清單（按建議執行順序）

## 階段 1：讀完 8 份必讀 + 接受 9th master handoff（30-60 分）

按順序讀 + 確認對 scope / 5 主軸工作順序 / 9th master 全程 7 條教訓內化的理解。

## 階段 2：Phase A.0F audit cycle 收尾（依當前 audit state；1-3h）

跑 `git log frontend-tools-a0f --oneline -30` verify actual A.0F audit cycle 狀態。

### 場景 A：audit cycle Round 2 review PASS

- 直接進階段 3
- 寫 PHASE_A0F_COMPLETION_REPORT.md（或在 PHASE_D_COMPLETION_REPORT v1.x partial supersede 內納入）

### 場景 B：audit cycle Round 2 NEAR-GO / NO-GO

- 依 audit pattern 跑 patch round（沿用 9th master 第一段 Round 1-4 cycle 模式 + 第二段 internal verify 模式）
- patch round 完成後重跑 review；若 PASS 進階段 3；若還是 NEAR-GO/NO-GO 走 hard-limit accept 或繼續 patch round

### 場景 C：audit cycle 已 close-out（很可能 — 因第三段對話結束時 audit-codex-patch-starter 1735d0a 已落地）

- 確認 A.0F 11 個 feature 全 PASS + integration test 全綠
- 直接進階段 3

## 階段 3：Wave 12 SKILL.md 實作（建議 priority 1；3-5h master + 6-10h CODEX 可並行）

### 工作模式（建議參考 9th master 第二段 Wave 14 batch 模式）

第八輪 / 9th master 第一段 Wave 12 教訓：一輪寫 5 個 starter (~1500 行) 品質下降。9th master 第二段 Wave 14 採新工作模式（master 寫 D10 完整 + batch starter D11-D13）成功避免 cascade。

10th master Wave 12 建議工作模式：

1. Master 寫 1 個完整 CODEX_D_W12_STARTER（含 6 個 SKILL.md 結構範本 + D-050/D-053 邊界 block + D-054 hybrid fallback 對齊 + frontmatter / 中文 header 紀律）
2. CODEX 跑 batch 一次性實作 6 個 SKILL.md + 5 wrapper（11 檔）
3. Master 內部 verify（grep 結構 + Read 重點 section；對齊 D1-D5 starter）

### 預期 6 SKILL.md 結構（對齊 D1 範本 + 00_j v0.2 共通基底）

每個 SKILL.md 含 11 段：
1. ## 用途
2. ## 觸發語
3. ## 觸發協議（指向 00_j v0.2 共通基底）
4. ## 啟動前檢查
5. ## 流程（5 階段 + 對齊 00_j：變更點識別 / 影響範圍評估 / 修改執行 / 跨檔同步 / 驗證 + phase_log 寫入）
6. ## 呈現規則
7. ## .protocol_version 寫入規範
8. ## 輸入
9. ## 輸出（寫檔 + phase_log audit entry）
10. ## 邊界（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表）
11. ## 錯誤處理 / Rollback

### Wave 12 特殊紀律

- `/iterate-scene --split-to-file`：D-054 NEW_REQ_15 落地；無中文 wrapper（依 D5 starter v0.4）；對齊 D-054 hybrid fallback per-scene first 寫法；scene-task / view-detailed-outline / export-detailed-outline 既有 read_source enum (per-scene / aggregate / missing) 應 cross-check
- 5 個 /iterate-* 對應上游 entity（W/V/C/R/P/CH/S）；對齊 Phase B /create-* 嚴格邊界（不擅自跨 entity）
- frontmatter `name` 對齊 directory name（kebab-case）
- 5 個中文 wrapper 採極簡模式（指向英文主檔為權威）

## 階段 4：AGENTS.md / CLAUDE.md Phase D metadata cleanup（30-60 分）

### 對齊範圍

PHASE_D_COMPLETION_REPORT v1.0 §8 Finding 2：Phase D metadata drift

| 表格區 | 變動前 | 變動後 |
|---|---|---|
| Phase D /view-* row | TBD | ✅ 已實作（Wave 13）|
| Phase D /export-* row | TBD | ✅ 已實作（Wave 14）|
| Phase D /diagnose row | TBD | ✅ 已實作（Wave 15）|
| Phase D /integrate row | TBD | ✅ 已實作（Wave 15）|
| Phase D /iterate-* row | TBD | ⏳ 10th master 實作後標 ✅ |
| Phase D /iterate-scene row | TBD | ⏳ 10th master 實作後標 ✅ |

### 邊界（嚴格）

- 不動 LOCKED spec / SKILL.md 內容
- 只動 AGENTS.md / CLAUDE.md 的 skill table metadata
- 對齊 PHASE_D_COMPLETION_REPORT v1.0 + CANON_DELTA_FRAMEWORK v0.1 reference

## 階段 5：Milestone 4 真正封版宣告（30-60 分）

### 寫檔策略（兩選一）

**選 A：PHASE_D_COMPLETION_REPORT v1.x partial supersede**
- §1 / §7 / §8 「接近條件達成」→「真正達成」
- §8 三 finding 全標 ✅ RESOLVED
- 新增 §10 Milestone 4 真正封版宣告

**選 B：新建 PHASE_A0F_COMPLETION_REPORT.md v1.0 + MILESTONE_4_SEAL_REPORT.md v1.0**
- 分離關注點；Phase A.0F 單獨 report；Milestone 4 封版單獨 report
- 對齊 PHASE_A/B/C_COMPLETION_REPORT pattern

**建議：選 A**（partial supersede；對齊 Phase A/B/C 既有 pattern；不額外新建 report 檔）。

### Milestone 4 真正達成條件 checklist

- ✓ Phase A.0F 11 個 feature 全 PASS + 整體驗收 + integration test + user manual v0.2
- ✓ Phase A.0F audit cycle close-out
- ✓ Wave 12 6 個 SKILL.md + 5 中文 wrapper 全落地
- ✓ Phase D Wave 13/14/15 SKILL.md 已落地（9th master）
- ✓ Canon Delta framework + L3 schema 對齊備忘紀錄（9th master）
- ✓ AGENTS.md / CLAUDE.md Phase D metadata 對齊
- ✓ baseline 維持 ≤ 247 ERROR
- ⏳ §6 user 親跑 M4 chain（可選 NEW_REQ_14 AI-assisted §6 補入機制）

## 階段 6：NEW_REQ deferred backlog 重新評估（30-60 分）

依 POST_LOCK_PENDING v0.18：

| NEW_REQ | 性質 | 10th master 評估動作 |
|---|---|---|
| **NEW_REQ_9** check_paths Windows vs sandbox baseline 差異 + 既有 baseline debt 27 模板 old-style filename | 既有 baseline debt | 評估：動 LOCKED 模板（風險高需 D-055+）vs 設計 lint script 緩解（NEW_REQ_16 路徑）vs 維持 hard-limit accept；建議**維持 hard-limit accept**直到 NEW_REQ_16 lint script 落地 |
| **NEW_REQ_11** 翻譯工具分支 fork tool B | Future fork | DEFERRED 至工具 A 真正封版後（屬 11+ 輪 master scope）；本輪不動 |
| **NEW_REQ_15** D-054 hybrid 迭代評估 | Monitor trigger | 10th master 期間 monitor trigger A/B/C/D 是否達成；若達成則開 D-055 拍板 |
| **NEW_REQ_16** 自動化 QA Layer 1 lint script | Future 自動化 | 10th master 可考慮起手實作（屬封版後維護期 ROI 高）；spec 規劃可在本輪完成；實作可推 11+ 輪 |
| **NEW_REQ_17** Auto-patcher | DEFERRED 至 NEW_REQ_16 落地後 | 11+ 輪 master scope；本輪不動 |
| **NEW_REQ_18** Nightly AI-driven Semantic Review | DEFERRED 至 NEW_REQ_16/17 落地 + 翻譯工具 fork 前評估 | 11+ 輪 master scope；本輪不動 |
| **NEW_REQ_19** 9th master cleanup queue | RESOLVED via Path A hard-limit accept | 9th master 第一段已結案；本輪不動 |

## 階段 7（可選）：archive 9th master 期間 handoff packages

10th master 完成後可把以下 archive 進 `_design/archive/`：

- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0
- `_design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md` v1.0
- `_design/HANDOFF_TO_10TH_MASTER.md` v1.0（本檔；完成後 archive）

---

# 4. 風險警示 + 重要紀律

## 4.1 9th master 全程 7 條教訓內化（強制；10th master 必 grok）

### 第一段對話 5 條（review cycle 收尾紀律）

1. **Windows baseline 權威** — sandbox virtiofs cache 在某些 check_paths case 會產 false negative；sandbox 跑出的 ERROR 數低於實際；只能作 noise 對照；以 Windows 端為事實
2. **Cascade sweep broader pattern** — CODEX review 列出的具體 hits 是「sample 抽樣」；master inline patch sweep 必須對全 repo 跑 broader pattern grep 確保 cleanup；不只看 review 列出的具體 hits
3. **SPEC frontmatter 段直接 grep verify** — 寫 starter 涉及 frontmatter 描述前直接 grep SPEC §5.2 verify；不可憑記憶寫具體欄位數字
4. **Supersede note 避免重複 finding 內精確詞串** — strict grep 不分否定句 / 歷史 narrative；wording 應描述「修補性質」而非重述被改的字串本身（Round 3 R3-MAJOR-01 教訓）
5. **Review starter diff anchor 必須精確** — 不要假設 user commit composition；`HEAD~N..HEAD` 的 N 設定可能含 review report commit；推薦改用「明示 commit hash」（如 `<round-N-baseline-commit>..HEAD`）或「`HEAD~1..HEAD` 限定最後一個 commit」；避免 diff window 多框住 immutable history 造成 false MAJOR finding（Round 4 R4-MAJOR-01 + 第三段 Wave 16 Step 3 教訓）

### 第二段對話新增 2 條（filesystem / corruption 紀律）

6. **寫長 multi-byte 檔請用 Python script via bash 或 cat heredoc** — 不用 Write/Edit tool（Cowork tool 對長中文檔有截斷風險；本檔本身亦用 cat heredoc 寫入）；寫完跑 Python 驗 bytes / null bytes / utf-8 decode
7. **Cloud sync / 防毒不得監控 working tree** — `D:\劇本開發工具` 必須加白名單；OneDrive / Dropbox / Google Drive sync **不能監控**；Windows Defender / 防毒軟體 **加白名單**（特別 `.git/` 目錄）；若發現 `.git/index.lock` + `.git/index.lock.tmp` + `.git/HEAD.lock` 反覆出現 → 立刻暫停 cloud sync + 防毒實時掃描

### Filesystem corruption 修復步驟（已驗證 work；第二段對話實證）

```
1. 暫停 cloud sync + 防毒實時掃描
2. Kill git.exe / bash.exe / wsl.exe process
3. del .git\*.lock / .git\*.lock.tmp
4. git stash push -u -m "pre-restore"
5. git checkout HEAD -- .
6. git status verify clean
7. 依 stash 內容判斷恢復 untracked 檔
```

## 4.2 9th master 第三段對話新增工作模式（10th master 沿用）

### 4.2.1 Master / CODEX / user 三方分工

第三段對話 Wave 16 Step 3 拍板採新工作模式（沿用第二段 Wave 14-15）：

- **Master 寫 starter**（review starter / HANDOFF）— context 消耗 ~20-30%
- **CODEX 跑 review task / user 端 git 操作** — wall-time ~2-3h；不消耗 master context
- **Master 內部 verify**（grep 結構 + Read 重點 section）— context 消耗 ~5%

vs 9th master 第一段 Round 1-4 cycle 4 輪 wall-time 證明全 CODEX review starter cycle 太長。

**10th master 工作模式建議：**
- Phase A.0F audit cycle 收尾：依當前 audit pattern（CODEX REVIEW + patch round）
- Wave 12 SKILL.md 實作：Master 寫 1 個完整 batch starter + CODEX 跑 batch + master 內部 verify
- AGENTS.md / CLAUDE.md metadata cleanup：master 直接 patch（不需 CODEX）
- Milestone 4 封版宣告：master 直接寫（partial supersede 或新建 report）
- NEW_REQ backlog 重新評估：master 直接寫（POST_LOCK_PENDING v0.19 partial supersede）

### 4.2.2 整合過程發現新衝突 → 立刻停手回升 user 拍板

9th master 全程沿用紀律；10th master 必沿用。

## 4.3 NEW_REQ deferred 清單（給 10th master 處理時機）

| NEW_REQ | 性質 | 推薦處理時機 | 10th master action |
|---|---|---|---|
| NEW_REQ_9 | check_paths Windows vs sandbox baseline 差異 + 既有 baseline debt | 屬 LOCKED 模板需 D-055+ 拍板 | **建議維持 hard-limit accept** 直到 NEW_REQ_16 lint script 落地；本輪不動 |
| NEW_REQ_11 | 翻譯工具分支 fork tool B | DEFERRED 至工具 A 真正封版後 | 11+ 輪 master scope；本輪不動 |
| NEW_REQ_14 | PHASE_X §6 AI-assisted 補入 | 同 D-052 模式 | 10th master 期間若 user 跑 M4 chain → 可使用 AI-assisted §6 補入機制 |
| NEW_REQ_15 | D-054 hybrid 迭代評估 monitor | Phase D 期間 monitor | 10th master 期間 monitor trigger A/B/C/D 達成情況；若達成則開 D-055 |
| NEW_REQ_16 | 自動化 QA Layer 1 cross-ref consistency lint script | Future 自動化（封版後維護期 ROI 高）| 10th master 可考慮起手實作 spec 規劃；實作可推 11+ 輪 |
| NEW_REQ_17 | 自動化 QA Layer 2 auto-patcher | DEFERRED 至 NEW_REQ_16 落地後 | 11+ 輪 master scope；本輪不動 |
| NEW_REQ_18 | 自動化 QA Layer 3 nightly AI-driven semantic review | DEFERRED 至 NEW_REQ_16/17 落地 + 翻譯工具 fork 前評估 | 11+ 輪 master scope；本輪不動 |
| NEW_REQ_19 | 9th master cleanup queue | RESOLVED via Path A hard-limit accept | 9th master 第一段已結案；本輪不動 |

## 4.4 D-054 NEW_REQ_15 迭代條件 monitor（給 10th master 沿用追蹤）

第八輪 master 拍板 D-054 選 1 Hybrid 同時記錄未來迭代 trigger 條件。10th master Wave 12 SKILL.md 落地後需 monitor：

| trigger | 條件 | 對應評估動作 |
|---|---|---|
| **A** | user 寫 ≥ 30 場後回報「聚合 06_a 太大」 | 評估 D-055 全 per-scene supersede |
| **B** | `/iterate-scene --split-to-file` 實作後 user 連續 ≥ 5 次拆檔 | 評估「per-scene 變預設」（hybrid 反向）|
| **C** | 工具 B 翻譯 / 其他多 agent 並行需求出現 | 評估 per-scene 對 race condition 緩解 |
| **D** | 聚合 06_a 持續發生 git merge friction | 評估拆檔降低 conflict |

任一 trigger 達成 → 10th master 或更晚輪開 D-055 拍板包（3 候選選項：A per-scene 變預設 / B 強制全 per-scene / C 維持 hybrid + `/iterate-aggregate-to-split-all`）。

詳見 `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_15。

## 4.5 sandbox virtiofs cache stale 已知問題（沿用第一段 + 第二段 + 第三段）

工作目錄 Windows 端為權威。Sandbox 端 git status / wc -l / ls mtime 偶爾顯示 stale。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 4.6 「Fix one, find two」cascade pattern 預防紀律（9th master 內化沿用）

9th master 第一段 Round 1-4 cycle 4 輪 inline patch 出現同類型 version cross-ref sequencing cascade。根因：

1. 同 patch round 內 sequential task 寫 cross-ref 時不知道後面 task 會升版
2. 缺自動化 cross-ref checker（NEW_REQ_16 lint script 規劃中）

**10th master 紀律建議：**

- **patch round 開始前**：用 grep 全掃版本 cross-ref；列出所有 active stale；一次性 sweep
- **每個 patch task 開始前**：先決定本輪所有檔案的目標版本；統一 cascade
- **patch round 結束前**：再跑 grep 全掃 verify 沒新 stale 引入
- **未來**：等 NEW_REQ_16 lint script 實作後自動化

## 4.7 Master starter 對 spec enum 紀律（沿用第八輪 + 9th master 全程）

寫 starter 含 spec enum 引用時：先 grep SPEC / parser code verify enum 列表完整 + 拼字正確（教訓 3 + 教訓 7 對齊）。

10th master Wave 12 SKILL.md 實作時：
- /iterate-* enum 對齊 SPEC §5.2 frontmatter 6 enum（pipeline_state / mode_tag / qa_decision / qa_type / source_*；對應上游 entity）
- /iterate-scene split-to-file mode 對齊 D-054 hybrid fallback read_source enum (per-scene / aggregate / missing)
- 寫 starter 前直接 grep SPEC verify

## 4.8 不擅自越界

- ✗ 不重做設計（已 LOCKED v1.0~v2.0）
- ✗ 不改 D-001~D-054 拍板結論
- ✗ 不重審 9th master 全程已 accepted finding
- ✗ 不重審 Wave 13/14/15 SKILL.md 結構（只動 metadata）
- ✗ 不寫 Phase E / 工具 B 任何檔（屬 11+ 輪 master scope）
- ✗ 不擅自啟動新 D-NNN 拍板（如有新議題 → 先回升 user 拍板）

---

## 4.9 STYLE_ANCHOR batch K-NN pattern（10th master D-055 落地期間累積；2026-05-28）

10th master 第十輪 D-055 拍板 pre-generation 文風錨定機制 batch（8 處 Template-side 變更 + 4 sub-T Instance-side 落地）期間，累積 9 條 K-NN（known-issue）跨 Template / Instance 雙對話分工架構。**K-NN ≥ 7 觸發本段紀錄**（T7 review 拍板紀律）。

### 4.9.1 K-NN 三類分群

**類 1：file-tool truncation / mount sync lag（K-01 / K-03）**
- K-01：`entity_type_registry.yaml` 5/19 pre-existing truncation（Template 端；5 行 tail loss；T3 hot-fix bash append 修復）
- K-03：Edit tool 寫 `_design/expected_entities.yaml` truncation（56 行 / 1597 bytes 中斷在「surfac」；T4 救援用 git HEAD restore + bash awk）
- **延伸 §4.5 sandbox virtiofs cache stale 已知問題** — 確認 Edit/Write file-tool acknowledge 在 mount sync lag 下會 silently corrupt；不可單純依賴 tool 回報

**類 2：starter bug（K-02 / K-04）**
- K-02：STYLE_ANCHOR_IMPL_STARTER §1 變更 3「7 個 core 條目」實為 9（10th master 預讀 entity_type_registry.yaml 僅 head -50 行抽樣導致）
- K-04：RFC §7.3 隱含假設 07_a §18 已名「風格要求」，實則為「文本長度與格式限制」（T5 5a 順手 align fix）
- **延伸 §4.7 Master starter 對 spec enum 紀律** — 寫 starter / RFC 前 grep 整檔 target structure 完整 vs 抽樣讀

**類 3：pre-existing alignment（K-06）**
- K-06：scene-task SKILL.md §3.2 00_b §6 row column 3「風格要求」粒度與 T5 落地後 W-style row 子節 anchor 不一致（T6 6c 順手 fix）
- **延伸 §4.6 cascade pattern 預防紀律** — pre-existing 不一致在 patch 落地時容易暴露；patch round 開始 + 結束都跑 grep 全掃

**類 4：carry-over（K-05 RESOLVED via N/A / K-07 / K-09）**
- K-05：既有 instance task packs 不會自動升 §18.3 §18.4 — **RESOLVED via T10-d N/A**（Instance 端 0 個既有 task packs；無實質升級需求；NEW_REQ_21 子項 9 同步落地 N/A）
- K-07：Instance `_design/` 是否與 Template `_design/` 同步議題（architecture decision pending；user 拍板項；T11 batch completion report 列入 follow-up）
- K-09：RFC §6.4「17 個技術詞」stated 17 / listed 16 — RFC 自身 inconsistency；本 batch byte-perfect 保留；屬 future RFC patch round 處理

**類 5：implementer self typo（K-08）**
- K-08：Part 2 heredoc 寫 20 處半形冒號（part 1 同類 typo 教訓沒在 part 2 落實 pre-write grep 紀律；K-04 enhanced verify 自抓自修；perl mass-fix 修復）

### 4.9.2 K-04 enhanced 紀律演化（給 11+ 輪 master 沿用）

本 batch 期間 K-03 file-tool truncation 觸發紀律演化 — Edit/Write tool 不可信賴；改採 **enhanced K-04 7 步**：

1. `git show HEAD:<path> > /tmp/<file>.original` ← backup
2. `/tmp` 版完整 parsing 驗證
3. **Multi-match pre-grep**（target pattern 在整檔出現幾次；> 1 處必加 only-first-match flag；K-06 加入此步）
4. bash awk / sed 重構新版到 `/tmp/<file>.new`
5. **Hunk-by-hunk diff verify**（print 全 hunks；逐 hunk 確認沒誤動 sample block / template region；K-06 加入此步）
6. `cp /tmp/<file>.new` 寫回 working tree
7. fresh read 驗證 disk state（不依賴 Edit/Write tool report）

**特別注意點：**
- 對含 sample block 的 SKILL.md（如 scene-task SKILL.md 內 task pack frontmatter sample；dialogue-write SKILL.md 內 phase_log entry sample）— awk pattern 必須加 `only-first-match flag`（`!done_flag` + `done_flag=1` 副作用），否則 anchor 在 sample 內會被誤改
- 對含 frontmatter YAML block + markdown 內 `---` 分隔線的檔（如 01_d 含 frontmatter `---` + markdown 章節間 `---`）— **絕對禁止** mass-fix（`perl -i -pe 's/:/：/g'` 之類）；會破壞 YAML syntax
- heredoc 寫中文檔 — quoted delimiter（如 `<< '_EOF_UNIQUE_'`）防 shell 展開 + pre-write mental check 全/半形冒號 + 寫後 grep verify

### 4.9.3 雙對話分工模式（10th master STYLE_ANCHOR batch 首例）

本 batch 採「Template 對話（mount = Template repo）+ Instance 對話（mount = Instance repo）」雙 Cowork 對話分工：
- Template 對話：T1-T9 Template-side（9 處變更）+ T11 batch completion verify
- Instance 對話：T10 Instance-side 落地（4 sub-T）+ T11-Instance verify
- user 橋接兩對話 + 收斂 batch completion report

此模式給 11+ 輪 master 參考 — 適用「同一 batch 跨 Template + Instance 雙 repo 落地」情境（如 Phase E / 工具 B / 跨 instance fork 等）。模式優點：避免 transcription 風險 / 直接 mount access / K-NN 表跨 scope 收斂統一。

### 4.9.4 待 user 拍板 follow-up（K-07）

**K-07 Instance `_design/` 同步議題**屬 architecture decision pending：
- Instance 端有獨立 `_design/` copy（含 DECISIONS_LOG.md / POST_LOCK_PENDING.md / 大量 CODEX_* historic review reports）
- Template 對話 T8/T9 已落地 D-055 / NEW_REQ_21 到 Template `_design/`
- Instance `_design/` 對應檔案沒有 sync

三選一策略待 user 拍板：
- 路徑 1：Instance `_design/` 是 active mirror — 後續手動 sync 所有 master 拍板（high maintenance cost）
- 路徑 2：Instance `_design/` 是 historic snapshot — 清空除 CODEX_* 之外的 active files；future 一律走 cross-repo reference Template
- 路徑 3：hybrid — LOCKED spec sync、其他 transient artifact 不 sync；需明確定義邊界

處理時機：本 batch 完成後 user 決策；11+ 輪 master / 後續 patch round 執行。

---

# 5. 完成條件

第十輪整合對話完成 = Milestone 4 真正封版條件全部 ✓：

```
✓ Phase A.0F audit cycle close-out（11 個 feature + 整體驗收 + integration test + user manual v0.2 全 PASS）
✓ Wave 12 6 個 SKILL.md + 5 中文 wrapper 全落地（/iterate-* 5 + /iterate-scene --split-to-file 1）
✓ AGENTS.md / CLAUDE.md Phase D metadata 對齊（Wave 13/14/15 標 ✅；Wave 12 標 ✅）
✓ Milestone 4 真正封版宣告（PHASE_D_COMPLETION_REPORT v1.x partial supersede 或 MILESTONE_4_SEAL_REPORT）
✓ NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18 重新評估紀錄
✓ baseline check_headers 0 ERROR / check_paths ≤ 247 ERROR / build_repo_index 0 ERROR 維持
✓ （可選）9th master handoff packages archive 進 _design/archive/
✓ （可選）寫 HANDOFF_TO_11TH_MASTER.md 接 Phase E / 工具 B / 維護期 scope
```

---

# 6. 文件維護紀律

- 本檔是「接手指南」，第十輪 master 對話讀完後**不需要更新本檔**
- 若第十輪發現本檔不準確 → 標 errata 在第 11 輪接手包（如有）
- 第十輪完成後可把本檔 archive 進 `_design/archive/`
- 真正完整 HANDOFF_TO_11TH_MASTER.md（如有）由第十輪寫；對齊 HANDOFF_TO_9TH_MASTER / HANDOFF_TO_10TH_MASTER pattern

---

# 7. 對 user 的最終建議（9th master 第三段對話結束時）

## 7.1 立即可做的事

1. **commit + push 9th master 第三段所有變更**（CODEX_D_FINAL_REVIEW_STARTER v0.1 + 本 HANDOFF v1.0）
2. **跑 CODEX_D_FINAL_REVIEW_STARTER v0.1**（依 Wave 16 Step 3 流程；wall-time ~2-3h）— 若 GO → 進 Wave 16 Step 4 / 10th master 接手；若 NEAR-GO/NO-GO → 走 inline patch 或 patch round
3. **決定 master ref 對齊策略**（選 A cherry-pick / 選 B 完整 merge / 選 C rebase）— 建議**選 B**（完整 merge）對齊 best practice
4. **準備 10th master 對話**（用本檔 §1 對話啟動指令；建議 wall-time 在 Phase A.0F audit cycle close-out 後）

## 7.2 Milestone 4 真正封版的條件達成

- ✓ Phase D Wave 13/14/15 SKILL.md 全落地（9th master）
- ✓ Canon Delta framework + L3 schema 對齊備忘紀錄（9th master）
- ✓ PHASE_D_COMPLETION_REPORT v1.0 4 維度 PASS（9th master 第二段）
- ✓ Milestone 4 接近條件達成宣告（9th master 第二段；非達成）
- ⏳ Phase A.0F 11 個 feature + 整體驗收 + audit cycle close-out（Phase A.0F 平行對話 + 10th master）
- ⏳ Wave 12 6 個 SKILL.md + 5 wrapper（10th master）
- ⏳ AGENTS.md / CLAUDE.md Phase D metadata 對齊（10th master）
- ⏳ Milestone 4 真正封版宣告（10th master）

達成後 user 可進入：

```
Milestone 4 真正封版（10th master）
   ↓
M4 user-test 第四次點（user 親跑全 pipeline）
   ↓
（可選）Phase E / 工具 B 路徑（11+ 輪 master scope）
   ↓
NEW_REQ_16/17/18 自動化 QA 工具階段性實作（維護期）
   ↓
NEW_REQ_11 翻譯工具分支 fork（11+ 輪 master scope）
```

## 7.3 user-test 第四次點時機（M4）

10th master Milestone 4 真正封版宣告後可做 M4 user-test：跑完整工具 A pipeline（從 /init-project → 5 個 /create-* → /scene-task → /dialogue-write → /qa → /view-* → /export-* → /iterate-* → /diagnose+integrate）+ 前端工具實際使用。

M4 user-test 完成 → 走 NEW_REQ_14 AI-assisted §6 補入機制更新 PHASE_D_COMPLETION_REPORT v1.x §6 placeholder。

## 7.4 Phase E / 工具 B / 維護期路徑（第 11+ 輪之後）

- **第 11 輪 master（optional）：** NEW_REQ_16 lint script 階段性實作 + NEW_REQ_15 D-054 迭代評估（若 trigger 達成）
- **第 12+ 輪 master（optional）：** NEW_REQ_11 翻譯工具分支 fork（工具 B：`game-dialogue-translator`）+ NEW_REQ_17 auto-patcher 實作
- **維護期：** NEW_REQ_18 nightly AI-driven semantic review 階段性實作 + Canon Delta framework skill 化（11+ 輪 master 或工具 B fork 時啟用）

詳見第八輪 master 對話內展開的全 lifecycle 地圖（user 已要求整理為「完整後續開發地圖」）。

---

**祝第十輪 master 整合順利。Milestone 4 接近 → Milestone 4 真正封版的關鍵是把 Phase A.0F 前端工具 audit close-out + Wave 12 SKILL.md 全落地；前面 Phase A + B + C + D Wave 13/14/15 已把「資料庫 + 上游 + 下游 + 視圖 + 匯出 + 通用模式」全鏈打通。Wave 12 /iterate-* 補完後工具 A 全 feature land；Phase A.0F 補完後工具 A 真正可用。**

# 8. Cross-ref

- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master 整體 scope；本檔接續；§4 風險警示與紀律仍適用）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話接手包；第二段完成後 archive 候選）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md` v1.0（9th master 第三段對話接手包；第三段完成後 archive 候選）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.0（Phase D 接近條件達成事實檔；含 §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制 + §8 三 finding 處理紀錄）
- `_design/CODEX_D_FINAL_STARTER.md` v0.1（9th master 第二段 Wave 16 Step 1 落地的 starter）
- `_design/CODEX_D_FINAL_REVIEW_STARTER.md` v0.1（9th master 第三段 Wave 16 Step 3 落地的 review starter；用明示 6 commit hash diff anchor）
- `_design/CODEX_D_FINAL_REVIEW_REPORT.md` v0.1（9th master 第三段 Wave 16 Step 3 review report；GO / NEAR-GO / NO-GO 判定紀錄）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（pattern 對齊範本）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.4 / `_design/PHASE_A_COMPLETION_REPORT.md` v1.1（pattern 對照）
- `_design/POST_LOCK_PENDING.md` v0.18（NEW_REQ 整體狀態；含 Round 1-4 教訓內化 5 條 + NEW_REQ_9/11/14/15/16/17/18/19 狀態）
- `_design/DECISIONS_LOG.md` v2.0 §6.10-§6.17（D-047 ~ D-054 全部 LOCKED；含 D-050 + D-052 + D-053 + D-054 Wave 12/14/15 對齊邊界）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED；Wave 12 /iterate-scene --split-to-file 設計權威）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（9th master 第二段 Wave 15 新建；framework reference；不實作 skill；11+ 輪 master / 工具 B fork reference）
- `_design/REQUIREMENTS_LOCK.md` v1.0 FINAL（north star；不動）
- `_design/INTEGRATION_CONTRACTS.md` v2.1 LOCKED / `_design/SPEC.md` v1.2 LOCKED / `_design/ARCHITECTURE.md` v1.6 LOCKED / `_design/TASKS.md` v1.9 LOCKED / `_design/DATA_FORMAT_SPEC.md` v0.4 LOCKED / `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 LOCKED / `_design/UX_SPEC.md` v0.4 LOCKED / `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 LOCKED（10 個 LOCKED spec；不動）
- `_design/CODEX_D1_STARTER.md` v0.3 ~ `_design/CODEX_D5_STARTER.md` v0.4（Wave 12 starter set 5 個；10th master Wave 12 SKILL.md 實作的權威 reference）
- `_design/CODEX_D6_STARTER.md` v0.1 + `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1（Wave 13 starter）
- `_design/CODEX_D10_STARTER.md` v0.1（含 §Z L3 schema 對齊備忘）+ `_design/CODEX_D_EXPORT_BATCH_STARTER.md` v0.1（Wave 14 starter）
- `_design/CODEX_D14_STARTER.md` v0.1 + `_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` v0.1（Wave 15 starter）
- `00_protocol/00_j_迭代協議.md` v0.2（9th master 第一段升 v0.1 → v0.2；5+1 iterate 共通基底；Wave 12 SKILL.md 實作的權威 reference）
- `00_protocol/00_a_台詞生產協議.md`（不動；/diagnose §3.3 + /integrate §3.4 對應 protocol）
- `.claude/skills/view-*/SKILL.md` v0.1 + 4 中文 wrapper（Wave 13 落地）
- `.claude/skills/export-*/SKILL.md` v0.1 + 4 中文 wrapper（Wave 14 落地）
- `.claude/skills/diagnose/SKILL.md` v0.1 + `.claude/skills/integrate/SKILL.md` v0.1 + 2 中文 wrapper（Wave 15 落地）
- `.claude/skills/iterate-*/SKILL.md`（6 個；10th master Wave 12 實作目標）+ 5 中文 wrapper（10th master Wave 12 實作目標）
