狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master 收尾完整 review starter — Phase C + D-054 + Cleanup round + patch round 2/3 + Wave 9-11 + C4 patch + Wave 11 patch 全變動 review + 8 維度檢查；單輪結束 default  
優先級：高

# CODEX_8TH_MASTER_FINAL_REVIEW_STARTER — 第八輪 master 收尾完整 review

# 0. 本檔用途

第八輪 master 對話完成 Phase C 收尾 + Milestone 3 達成宣告 + HANDOFF_TO_9TH_MASTER 交付。在 9th master 對話啟動接 Phase D 之前，對第八輪 master 期間累積的所有變動跑 **8 維度完整 review checkpoint**。

**對齊傳統：** 同 7th master 收尾 Round 1-7 重審模式（CODEX_7TH_MASTER_FINAL_REVIEW_STARTER v0.1 + Round 1-7 系列 review report 已存在參考）。本輪是第八輪 master 對應的單輪收尾 review — 用 CODEX 抓 8th master 期間累積的 inconsistency / spec 衝突 / Template 污染 / cascade 殘留 / starter typo 殘留。

**前置條件：** 第八輪 master 已完成所有預定變動（13 個主要 work items；詳 §1 內 scope）+ user 已 commit/push 全部。

**Review GO → 9th master 對話啟動接 Phase D**（用 HANDOFF_TO_9TH_MASTER.md 內的對話啟動 prompt 開新對話）

**Review NEAR-GO →** user 拍板 hard-limit accept（殘留 finding 入 9th master cleanup queue NEW_REQ_19）OR 8th master 開緊急 patch round 4 處理 finding → Round 12 重審 → GO

**Review NO-GO →** 大幅 rollback / restructure 考量；user 拍板路徑

⚠ **單輪結束 default（紀律延續）：** 本輪 review 預設一輪結束；不預設自動進 Round 12。若 NEAR-GO/NO-GO，user 拍板分支。避免第七輪 master 7 round 迴圈再次發生。

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- 不涉 Instance-only path（本 review scope 全 Template repo 內）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第八輪 master 對話收尾前完整 review」— 對第八輪 master 在 Phase C 收尾期間累積的所有變動跑 8 維度檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 7th master Round 1-7 重審模式 + 8th master Round 8-10 模式
- 對應前置：第八輪 master 已完成 Phase C 收尾全部變動 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /scene-task / /dialogue-write / /qa / /create-* / /init-project 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✗ 不重審 Round 8/9/10/Wave 11 已 accepted 之 finding（已 closed / hard-limit accept / NEW_REQ_19 紀錄；不重議）
- ✗ 不下 D-054 結論（已 RESOLVED via D-054 in DECISIONS_LOG v2.0 §6.17）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_8TH_MASTER_FINAL_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

第八輪 master 對話期間累積變動清單（給你做 review baseline — 13 個主要 work items）：

### A. Cleanup round（17 檔；Round 7 NEAR-GO 殘留處理）

對齊 Round 7 報告 §10 9 finding 全處理：R7-MA-01/02/03 + R7-MI-01~06。詳 `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO 紀錄）。

### B. Patch round 2（8 檔；R8 6 finding cleanup）

- R8-MA-01：`.claude/skills/create-detailed-outline/SKILL.md` v0.1 → v0.2 prereq line 76 修正
- R8-MI-01/02/03/04/05：phase_b_outline_review_log / B8 starter grep 註解 / PHASE_B §9 / phase_b_review_log §4 / 3 skill body D-050 block

詳 `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1（Round 9 NEAR-GO 紀錄）。

### C. D-054 拍板落地（3 檔）

- `_design/DECISIONS_LOG.md` v1.9 → v2.0：§6.17 D-054 拍板紀錄（per-scene 檔 convention 選 1 Hybrid + 未來迭代條件紀錄）
- `_design/POST_LOCK_PENDING.md` v0.9 → v0.10：NEW_REQ_13 RESOLVED via D-054 + 新增 NEW_REQ_15「per-scene 拆檔 convention 迭代評估」DEFERRED
- `_design/D054_DECISION_PACKAGE.md` v0.1 → v0.2：標 APPLIED + §0 拍板結果摘要（user 拍板原文紀錄）

### D. Patch round 3（6 檔；R9 finding sweep + R9-INFO-02）

- R9-MI-01：`_design/phase_b_review_log.md` v0.4 → v0.5（§4 Cross-ref 4 skill 分行 + C/R/P v0.3 + CH v0.2）
- R9-MI-02：`_design/PHASE_B_COMPLETION_REPORT.md` v1.1 → v1.2（§3.2/§4.1/§9 多處版本對齊）
- R9-MI-03：`_design/phase_b_character_review_log.md` v0.2 → v0.3
- R9-MI-04：`_design/phase_b_outline_review_log.md` v0.3 → v0.4
- R9-MI-05：`_design/CODEX_B9_STARTER.md` v0.3 → v0.4（13 處版本 stale sweep）
- R9-INFO-02：`.claude/skills/create-detailed-outline/SKILL.md` v0.2 → v0.3（body 加 D-050 子裁決 1+2 雙 block 對齊 C/R/P 格式）

詳 `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO 紀錄）。

### E. Round 10 hard-limit accept + NEW_REQ_19（1 檔）

`_design/POST_LOCK_PENDING.md` v0.10 → v0.12（user 平行加 NEW_REQ_16/17/18 自動化 QA 工具 3 層架構 → v0.11；8th master Round 10 hard-limit accept 新增 NEW_REQ_19 9th master cleanup queue → v0.12）。

### F. Phase C Wave 9 三 starter（3 檔）

- `_design/CODEX_C1_STARTER.md` v0.1（/scene-task 含 D-054 hybrid fallback 規範）
- `_design/CODEX_C2_STARTER.md` v0.1（/dialogue-write 4 模式 + D.2.5 gate + **註：含 master starter typo FINAL → 已在 Wave 11 patch 修補為 ORGANIZED**）
- `_design/CODEX_C3_STARTER.md` v0.1（/qa 8 報告必跑 + R8-INFO-06 處理策略）

### G. Phase C Wave 10 三 skill 實作（6 檔；CODEX 跑出）

- `.claude/skills/scene-task/SKILL.md` v0.1 + `.claude/skills/場景任務包/SKILL.md` v0.1
- `.claude/skills/dialogue-write/SKILL.md` v0.1 → v0.2（**Wave 11 master inline patch mode_tag enum**）+ `.claude/skills/生成台詞/SKILL.md` v0.1
- `.claude/skills/qa/SKILL.md` v0.1 + `.claude/skills/檢查/SKILL.md` v0.1

### H. C4 patch round + NEW_REQ_19 補註（4 檔）

- `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1（qa_type=RHYTHM；UD §3.7）
- `09_quality_assurance/09_h_對話張力檢查模板.md` v0.1（qa_type=DRAMATIC_TENSION；UD §3.8）
- `09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.1（qa_type=CROSS_SCENE_CONTINUITY；UD §3.9）
- `_design/POST_LOCK_PENDING.md` v0.12 → v0.13（NEW_REQ_19 補註 09_g/h/i 提前處理）+ `_design/CODEX_C4_PATCH_STARTER.md` v0.1

### I. Wave 11 整體驗收 starter（1 檔）

`_design/CODEX_C_FINAL_STARTER.md` v0.1（4 維度驗收 + §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制 + Milestone 3 達成宣告條件）

### J. Wave 11 master inline patch — mode_tag enum blocker 修補（1 檔）

`.claude/skills/dialogue-write/SKILL.md` v0.1 → v0.2（line 450 locked set FINAL → ORGANIZED；補齊 6 enum + 寫權限段補 ORGANIZED reserved scope + 明示「狀態 FINAL 屬狀態 enum 不屬 mode_tag」防混淆；對齊 SPEC §5.2.4 line 356 + scripts/parse_frontmatter.py VALID_MODE_TAGS）

**根因：master CODEX_C2_STARTER v0.1 typo — 把 ORGANIZED 誤寫成 FINAL；CODEX 忠實實作；Wave 11 對齊 SPEC + parser 抓出。**

### K. Wave 11 PHASE_C_COMPLETION_REPORT（1 檔；CODEX 跑 2 次：BLOCKED → PASS）

`_design/PHASE_C_COMPLETION_REPORT.md` v1.0（4 維度全 PASS；Milestone 3 達成宣告；含 §6 user 親跑 placeholder + §8 9th master cleanup queue 處理優先序 + AGENTS.md TBD out-of-scope 標註）

### L. 第八輪 4 個 review report（CODEX 跑出）

- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO）
- `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1（Round 9 NEAR-GO）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO；4 finding 入 NEW_REQ_19）
- 1 Wave 11 PASS report（含在 PHASE_C_COMPLETION_REPORT v1.0；非獨立 review report 性質）

### M. HANDOFF_TO_9TH_MASTER（1 檔）

`_design/HANDOFF_TO_9TH_MASTER.md` v1.0（第九輪 master 對話接手包；含對話啟動 prompt + Phase D scope + 9th master cleanup queue 處理優先序 + cascade pattern + master starter typo 教訓 + NEW_REQ_15 D-054 迭代條件 monitor）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_8TH_MASTER_FINAL_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 8 維度

**維度 1：第八輪 13 work items 落地完整性**

逐項驗證 §A~§M 13 個 work items 全部落地：

| Work Item | 預期 evidence | Check |
|---|---|---|
| A Cleanup round | 17 檔 R7-MA-01/02/03 + R7-MI-01~06 全 RESOLVED | git log 含 "Cleanup round" commit + 對應 17 檔 |
| B Patch round 2 | 8 檔 R8 6 finding closure | git log + Round 9 report 5 RESOLVED 1 PARTIAL |
| C D-054 拍板 | DECISIONS_LOG §6.17 + POST_LOCK_PENDING NEW_REQ_13/15 + D054 package APPLIED | DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.10+ / D054 v0.2 APPLIED |
| D Patch round 3 | 6 檔 R9 sweep | git log + Round 10 report 5 MINOR + 1 INFO |
| E NEW_REQ_19 | POST_LOCK_PENDING v0.10 → v0.12 | NEW_REQ_19 完整 + R10 4 finding 列項 |
| F Phase C Wave 9 starter | C1/C2/C3 v0.1 | _design/ 內 3 starter 存在 |
| G Phase C Wave 10 skill | 3 SKILL.md + 3 wrapper | .claude/skills/ 內 6 檔 |
| H C4 patch | 3 QA 模板 + starter + NEW_REQ_19 v0.13 補註 | 09_quality_assurance/ 內 09_g/h/i + POST_LOCK_PENDING v0.13 |
| I Wave 11 starter | CODEX_C_FINAL_STARTER v0.1 | _design/ 內存在 |
| J Wave 11 patch | dialogue-write v0.1 → v0.2 mode_tag fix | SKILL.md header v0.2 + line 450 含 ORGANIZED |
| K PHASE_C_COMPLETION_REPORT v1.0 | 4 維度 PASS + Milestone 3 達成 | _design/ 內存在 + §7 Milestone 3 達成宣告 |
| L 4 review report | Round 8/9/10 + Wave 11 | _design/ 內 3 review report 存在 |
| M HANDOFF_TO_9TH_MASTER | v1.0 含對話啟動 prompt + Phase D scope | _design/ 內存在 + §1 對話啟動指令 |

**維度 2：D-054 拍板落地完整性（per-scene 檔 convention Hybrid）**

對 D-054 拍板逐項 verify 落地：

- DECISIONS_LOG §6.17.2 D-054 拍板紀錄完整（5 欄：日期 / 議題 / 決策 / 影響 / Owner）
- §6.17.2 含「未來迭代條件紀錄」段（user 拍板原文 + trigger A/B/C/D + D-055 候選預留）
- §6.17.3 升版文件清單（DECISIONS_LOG v1.9 → v2.0 / POST_LOCK_PENDING v0.9 → v0.10 / D054 v0.1 → v0.2）
- §6.17.4「未來迭代追蹤紀律」首例
- POST_LOCK_PENDING NEW_REQ_13 標 ✅ RESOLVED via D-054
- POST_LOCK_PENDING NEW_REQ_15 完整（trigger A/B/C/D + D-055 候選預留 + 處理時機）
- D054_DECISION_PACKAGE v0.2 標 APPLIED + §0 拍板結果摘要（user 拍板原文紀錄）
- `.claude/skills/scene-task/SKILL.md` v0.1 含「## D-054 hybrid 讀檔 fallback 規範」段（per-scene → aggregate 兩階段 + 拒絕 fallback）
- 既有 `.claude/skills/create-detailed-outline/SKILL.md` v0.3 line 198 escape hatch wording 維持（自然承接 D-054）
- **0 LOCKED spec supersede 驗證：** D-050 子裁決 / 00_h v0.2 / TASKS v1.9 / UD §2.3 / SPEC §5.1 全不動

**維度 3：Phase C 3 skill chain consistency**

下游 pipeline 3 skill 對齊檢查：

| Skill | Header | D-054 fallback | D.x.5 gate dep | D-050 block | mode_tag/qa_type alignment | Wrapper |
|---|---|---|---|---|---|---|
| /scene-task | v0.1 | ✓ 含規範段 | D.2.5（產出 TASK_DRAFT；不擅升）| ✓ 雙 block | n/a | 場景任務包 v0.1 |
| /dialogue-write | v0.2 (patched) | n/a（不讀 06_scene_index）| D.2.5（要求 TASK_REVIEW）+ D.3.5（收斂）| ✓ 雙 block | **mode_tag 6 enum 對齊 SPEC §5.2.4 + parser VALID_MODE_TAGS（ORGANIZED/DRAFT_TRIAL/EXPERIMENTAL/CONVERGENCE/FINAL_CANDIDATE/SINGLE_ITER；line 450 應為 ORGANIZED 不 FINAL）** | 生成台詞 v0.1 |
| /qa | v0.1 | n/a（不讀 06_scene_index）| D.3.5（要求 DIALOGUE_CONVERGED；trial 路徑 B 例外）| ✓ 雙 block + 不產 09_e | qa_type 8 enum 對齊 D-043（09_a/b/c/d/f/g/h/i；9 種含 09_e final-gating）+ 8 報告序列順序對齊 UD §2.5.3 v0.3 | 檢查 v0.1 |

pipeline_state 9 狀態完整 verify：SCENE_INDEXED → TASK_DRAFT → TASK_REVIEW → DIALOGUE_TRIAL → DIALOGUE_CONVERGED → QA_PASSED/QA_FAILED → DIALOGUE_FINAL → DIALOGUE_LOCKED

**維度 4：8 個 QA 模板齊全 + 09_g/h/i 新建完整性**

09_quality_assurance/ 目錄 verify：

- 09_a 既有（AI_FLAVOR）+ 09_b 既有（VOICE_CONSISTENCY）+ 09_c 既有（FORBIDDEN_WORD）+ 09_d 既有（INFO_CONTROL）+ 09_e 既有（final-gating；不在 8 報告必跑）+ 09_f 既有（GENRE_DRIFT）
- **09_g 新（C4 patch round；qa_type=RHYTHM；對齊 UD §3.7）**
- **09_h 新（C4 patch round；qa_type=DRAMATIC_TENSION；對齊 UD §3.8）**
- **09_i 新（C4 patch round；qa_type=CROSS_SCENE_CONTINUITY；對齊 UD §3.9）**

3 個新模板 verify：
- 5 必填中文 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
- YAML block (`qa_type` / `entities` / `depends_on` / `weight`)
- 5 層檢查框架完整（用途 / qa_type / 框架 / algorithm / 通用化原則 / 輸出格式）
- algorithm 對齊 UD §3.7/§3.8/§3.9
- 不含作品專屬內容（無「林思羽」/「陳則安」/「情緒感知體質」/「my-test-instance」/ 任何具體角色）

**維度 5：Cleanup round + patch round 2/3 + Wave 11 finding closure 完整性**

對 8th master 4 輪 review + 1 wave 1 個 blocker 逐項 verify closure：

| Round | Finding | 預期狀態 |
|---|---|---|
| Round 8 GO | R8-MA-01 + R8-MI-01~05 + R8-INFO-01~06 | 9 finding 全處理（patch round 2）；R8-INFO-06 推 9th master |
| Round 9 NEAR-GO | R9-MI-01~05 + R9-INFO-01~02 | 6 finding 處理（patch round 3 + R9-INFO-02 補 CH skill D-053 exception block） |
| Round 10 NEAR-GO | R10-MA-01 + R10-MI-01~03 | 4 finding 入 NEW_REQ_19 (hard-limit accept) |
| Wave 11 BLOCKED → PASS | C.2 mode_tag enum blocker | master inline patch（dialogue-write v0.1 → v0.2）；Wave 11 第 2 跑 PASS |

**維度 6：NEW_REQ_19 9th master cleanup queue 完整紀錄**

POST_LOCK_PENDING v0.13 NEW_REQ_19 verify：

- R10-MA-01 ack（user 加 NEW_REQ_16/17/18 屬正當作業；無需 patch）
- R10-MI-01 列項（CH skill v0.3 但多處 cross-ref 仍寫 v0.2）
- R10-MI-02 列項（phase_b_review_log §4 review-log 版本 stale）
- R10-MI-03 列項（PHASE_B 仍引用 CODEX_B9_STARTER v0.3 應為 v0.4）
- R8-INFO-06 列項（00_k v0.1 5→8 報告 stale）
- 09_g/h/i 提前處理註記（v0.13 補註）
- 3 個 cleanup trigger 條件（A 9th master Phase D 啟動時 / B NEW_REQ_16 lint script 實作後 / C 封版前最終 cleanup round）
- 註：D-054 hybrid 迭代追蹤的 4 個 trigger A/B/C/D（A 使用規模 / B split 頻率 / C 並行需求 / D merge conflict）屬 **POST_LOCK_PENDING NEW_REQ_15**（D-054 future iteration evaluation）— **非 NEW_REQ_19 範圍**；本維度 verify NEW_REQ_15 含此 4 trigger（屬維度 2 D-054 落地完整性範圍）

**維度 7：LOCKED 文件不動合規性 + 第八輪 master 升版檔合規性**

verify LOCKED 文件**確實不動**：

- _design/SPEC.md / INTEGRATION_CONTRACTS.md / DATA_FORMAT_SPEC.md / UPSTREAM_DOWNSTREAM_SPEC.md / UX_SPEC.md / REQUIREMENTS_LOCK.md / L3_EXPORT_PROMPT_SCHEMA.md
- _design/registries/*.template.yaml（3 個）
- scripts/*.py
- 27 既有模板（01_world/ ~ 09_quality_assurance/ — 09_g/h/i 新建是 D-026/D-043 task §D.1a；不算動既有；總數 27 → 30 模板）
- 00_protocol/ 任何檔（含 00_k v0.1 stale 不本輪 patch）
- 既有 Phase A / Phase B SKILL.md + 6 中文 wrapper（init-project / create-* x5 / status / check-gaps / 中文 wrapper x5 + 建立世界觀）

verify 第八輪 master 升版檔合規性：
- ARCH v1.5 → v1.6：D-051 partial supersede ledger backfill（R7-MA-02 cleanup；§3.3.2 active wording 對齊；不引新 D-NNN）
- TASKS v1.9（不升 — top ledger backfill；R7-MA-01 cleanup；不引新 D-NNN）
- DECISIONS_LOG v1.9 → v2.0：D-054 新拍板（§6.17 新增）
- POST_LOCK_PENDING v0.9 → v0.13：NEW_REQ_15/19 新增 + NEW_REQ_13 RESOLVED + NEW_REQ_16/17/18 user 平行加 + 09_g/h/i 提前處理註記
- D054_DECISION_PACKAGE v0.1 → v0.2：拍板 APPLIED
- 5 個 Phase C 新 SKILL.md（scene-task / dialogue-write v0.2 / qa + 3 wrapper）
- 3 個 09_g/h/i 新 QA 模板
- 多份 PHASE_B / phase_b_*_review_log / CODEX_B9_STARTER cross-ref version sweep（patch round 2/3）

**維度 8：Template vs Instance 邊界 + cascade pattern + master starter typo 教訓**

#### 8.1 Template vs Instance 邊界（沿用 Round 1-7 + Round 8 模式）

grep Template 內所有 _design/ + 00_protocol/ + .claude/skills/ + 30 模板，搜：
- 「林思羽」/「陳則安」/「情緒感知體質」/ 任何具體 testing Instance 角色名
- 「my-test-instance」/ Instance-only concrete paths（除 `<instance_root>/` 前綴 + generic `<name>` 範例外）
- PHASE_C_COMPLETION_REPORT §6 是否採 generic placeholder（不嵌入 specific test data）
- 任何 review_log Template 骨架是否仍 placeholder（不該有 actual Instance entry）

#### 8.2 cascade pattern 教訓紀錄完整性

「Fix one, find two」cascade pattern 紀錄 verify：
- POST_LOCK_PENDING NEW_REQ_16/17/18 user 平行加（v0.11；user 預料到 cascade 問題的自我意識設計）
- POST_LOCK_PENDING NEW_REQ_19 9th master cleanup queue 紀錄（v0.12；hard-limit accept Round 10 4 finding）
- HANDOFF_TO_9TH_MASTER §4.6「Fix one, find two」cascade pattern 教訓 + 9th master 紀律建議

#### 8.3 master starter typo 教訓（Wave 11 blocker 啟示）

dialogue-write SKILL.md v0.2 header note 明示 typo 修補 + HANDOFF_TO_9TH_MASTER §4.7 master starter typo 教訓 + 9th master 紀律建議（寫 starter 含 spec enum 引用時先 grep verify）

### 技術驗證命令

跑以下並紀錄結果：

```bash
python -X utf8 -B scripts/check_headers.py 2>&1 | tail -10
python -X utf8 -B scripts/check_paths.py 2>&1 | tail -10
```

```python
from scripts.parse_frontmatter import build_repo_index
result = build_repo_index('.')
errors = [i for i in result.issues if getattr(i, 'severity', None) == 'ERROR']
warnings = [i for i in result.issues if getattr(i, 'severity', None) == 'WARN']
print(f"errors: {len(errors)}, warnings: {len(warnings)}")
for e in errors[:10]:
    print(f"  {e}")
```

```bash
git log --oneline -25
git diff fb09c6a HEAD --name-only 2>&1 | head -50
```

（`fb09c6a` 是第七輪 master 收尾 commit；本 review window 全範圍 = `fb09c6a..HEAD`）

### Finding 分類

每個發現的 issue 分類：

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / Template 嚴重污染（specific test data 殘留 active 檔）/ Phase C 3 skill chain 嚴重斷裂 / D-054 落地不完整造成 framework 跑不通 / mode_tag enum 仍 stale 違反 SPEC §5.2.4
- **MAJOR**：cross-doc 嚴重不一致 / 任一 work item §A~§M 嚴重缺失 / 大量新 stale reference / D-054 NEW_REQ_15 未來迭代追蹤殘缺 / Wave 11 blocker 未真修補（dialogue-write line 450 仍寫 FINAL）
- **MINOR**：版本欄 / cross-ref 小不一致 / 少數 stale wording / NEW_REQ_19 列項小缺漏 / NEW_REQ_19 已收錄之 finding 不另列（屬第八輪 master hard-limit accept 範圍）
- **INFO**：觀察記錄但不阻 GO（含已 hard-limit accept 之 NEW_REQ_19 收錄項；只記不阻）

### 決策準則

- **GO（PASS）**：0 CRITICAL + ≤2 MAJOR + 13 work items 全 RESOLVED + D-054 落地完整 + Phase C 3 skill chain consistent + 0 新 spec drift → 第八輪 master 可直接寫 HANDOFF_TO_9TH_MASTER（已寫；本 review 屬 closure verification）→ 9th master 對話可啟動接 Phase D
- **NEAR-GO（HOLD）**：0 CRITICAL + 3-5 MAJOR + 多 MINOR → user 拍板：(a) hard-limit accept（殘留入 NEW_REQ_19 已存在的 queue 一起處理）OR (b) 8th master 開緊急 patch round 4 → Round 12 重審 → GO
- **NO-GO**：≥1 CRITICAL OR ≥6 MAJOR → 大幅 rollback / restructure 考量 → user 拍板路徑（patch round 4 / rollback / 其他）

⚠ **單輪結束 default：** Round 11 本輪結果出來後**回 user 拍板**；不預設自動進 Round 12。避免第七輪 7 round 迴圈再次發生。

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts / registries
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 不下 D-054 結論（已 RESOLVED）
- 不重審 Round 8/9/10 已 accepted finding（不重議）
- 只新建 1 個 review report 檔

### 完成判定

✓ 8 維度全 verify + 結果寫入 review report
✓ 維度 1 對 13 work items 逐項 RESOLVED / PARTIAL / NOT_RESOLVED 標記
✓ 維度 2 D-054 拍板落地完整性 verify（含 NEW_REQ_15 未來迭代追蹤）
✓ 維度 3 Phase C 3 skill chain consistency mapping 表（含 mode_tag enum 對齊 verify）
✓ 維度 4 8 個 QA 模板齊全 + 09_g/h/i 新建完整性
✓ 維度 5 4 輪 review + 1 wave blocker closure 完整性
✓ 維度 6 NEW_REQ_19 9th master cleanup queue 紀錄
✓ 維度 7 LOCKED 不動合規性 + 升版檔合規性
✓ 維度 8 Template vs Instance 邊界 + cascade pattern + master starter typo 教訓紀錄
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / NEAR-GO / NO-GO）+ 對應 rationale
✓ `_design/CODEX_8TH_MASTER_FINAL_REVIEW_REPORT.md` v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master 收尾完整 review 結果 — Phase C + D-054 + Cleanup + patch round 2/3 + Wave 9-11 + C4 patch + Wave 11 patch 全變動  
優先級：高

# CODEX_8TH_MASTER_FINAL_REVIEW_REPORT

# 0. 文件目的
# 1. Round 11 摘要 + GO / NEAR-GO / NO-GO 判定
# 2. 維度 1：第八輪 13 work items 落地完整性（13 row 表）
# 3. 維度 2：D-054 拍板落地完整性
# 4. 維度 3：Phase C 3 skill chain consistency（含 mode_tag enum 對齊）
# 5. 維度 4：8 個 QA 模板齊全 + 09_g/h/i 新建完整性
# 6. 維度 5：4 輪 review + 1 wave blocker closure 完整性
# 7. 維度 6：NEW_REQ_19 9th master cleanup queue 紀錄完整性
# 8. 維度 7：LOCKED 不動合規性 + 升版檔合規性
# 9. 維度 8：Template vs Instance 邊界 + cascade pattern + master starter typo 教訓
# 10. 技術驗證結果（check_headers / check_paths / build_repo_index / git log / git diff 摘要）
# 11. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 12. 決策判定 + Rationale
# 13. 給第八輪 master 收尾的建議 / 9th master 接手準備
# 14. Cross-ref
```

### Go / Done 判定指引

- **DONE：** 上述驗收全 ✓ → review report 落地 → user commit/push → 回 user 拍板 GO / NEAR-GO / NO-GO 分支
- **BLOCKED：** 任一驗收 ✗ 回 user

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Round 11 重審完成 → user commit/push → 回 user 拍板：

**分支 A（GO — 預期）：** 第八輪 master 對話收尾結束 → user 用 HANDOFF_TO_9TH_MASTER.md 內的對話啟動 prompt 開新對話啟動第九輪 master 接 Phase D

**分支 B（NEAR-GO / HOLD）：** user 拍板：
- **B.1 hard-limit accept**（推薦；同 Round 10 模式）：殘留 finding 入 NEW_REQ_19 已存在的 9th master cleanup queue 一起處理 → 第八輪 master 對話收尾結束 → 9th master 對話啟動
- **B.2 patch round 4**：第八輪 master 開 inline patch round 4 處理 finding → user commit → 跑 Round 12 重審 → GO → 第八輪結束

**分支 C（NO-GO）：** user 拍板：rollback / 重審 / 其他路徑

---

# 3. 文件維護紀律

- 本檔是第八輪 master 對話收尾完整 review starter；完成後可 archive 進 `_design/archive/`
- 對應 review report 也屬第八輪 master 收尾事實紀錄；不刪除
- ⚠ 紀律：本 starter 預設**單輪結束**；多輪重審需 user 明示拍板（避免第七輪 7 round 迴圈再次發生）
- 未來 9th / 10th master 收尾前若需類似 review，可採同 starter pattern 寫對應 starter

---

# 4. Cross-ref

- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（第八輪 master 收尾 handoff；本 review 確認 handoff 完整性）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_STARTER.md` v0.1（第七輪 master 收尾 review starter；本 starter 模板參考）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO；review baseline 一部分）
- `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1（Round 9 NEAR-GO；review baseline 一部分）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO；review baseline 一部分）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Phase C 完成 + Milestone 3 達成；review baseline 一部分）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054（拍板 + 未來迭代條件紀錄）
- `_design/POST_LOCK_PENDING.md` v0.13（NEW_REQ_13~19 整體狀態）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED）
- `_design/TASKS.md` v1.9 + `_design/ARCHITECTURE.md` v1.6 + `_design/SPEC.md` v1.2（spec context）
- Phase C 3 skill：`.claude/skills/scene-task/SKILL.md` v0.1 + `.claude/skills/dialogue-write/SKILL.md` v0.2 + `.claude/skills/qa/SKILL.md` v0.1
- 09_g/h/i 三 QA 模板（C4 patch round 新建）
- 4 Phase C Wave 9-10 starter（C1/C2/C3/C4 patch）+ Wave 11 starter（C_FINAL）
