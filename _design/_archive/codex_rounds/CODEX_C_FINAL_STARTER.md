狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：Phase C Wave 11 整體驗收 starter — 撰寫 PHASE_C_COMPLETION_REPORT v1.0 + Milestone 3 達成宣告  
優先級：高

# CODEX_C_FINAL_STARTER — Phase C Wave 11：Phase C 整體驗收

# 0. 本檔用途

Phase C Wave 11 最後一條 task — Phase C 整體驗收 + 撰寫 `_design/PHASE_C_COMPLETION_REPORT.md` v1.0 + 寫入 Milestone 3 達成宣告。

**對齊傳統：** 同 Phase A `CODEX_A11_STARTER` + Phase B `CODEX_B9_STARTER` 模式（4 維度驗收 + master inline patch baseline 校正模式）。

**前置條件：** Phase C Wave 9 + Wave 10（含 C4 patch）全 DONE：
- C.1 /scene-task SKILL.md v0.1 + 中文 wrapper（含 D-054 hybrid fallback）
- C.2 /dialogue-write SKILL.md v0.1 + 中文 wrapper（4 模式 + D.2.5 gate dependency）
- C.3 /qa SKILL.md v0.1 + 中文 wrapper（8 報告必跑 + R8-INFO-06 處理策略）
- C4 patch round — 09_g/h/i 三 QA 模板補建（解除 /qa prerequisite 阻塞）

**Wave 11 PASS → Milestone 3 達成宣告 → master 寫 HANDOFF_TO_9TH_MASTER.md 接 Phase D**

⚠ **B.9 / A.11 兩段分工沿用：**
- **CODEX 跑：** 3 下游 skill 落地驗證 + 3 QA 模板補建驗證 + Wave 10 review consolidation + spec 對齊 + 寫 completion report
- **User 親跑（保留 §6 placeholder）：** 端到端 3 skill 鏈測試（接續 Phase B 測試 Instance → 跑 /scene-task → D.2.5 gate → /dialogue-write → D.3.5 gate → /qa 8 報告）— CODEX 在 completion report 內保留 §6 placeholder；NEW_REQ_14 AI-assisted §6 補入機制可在 user 親跑完後啟用

⚠ **baseline 紀律（依 NEW_REQ_9 + NEW_REQ_10 + R10 cascade 教訓）：**
- `check_headers.py`：**0 ERROR 維持是 baseline**；WARN 數 ≤ 當前 baseline +1（含 PHASE_C_COMPLETION_REPORT v1.0 可能 +1 WARN 屬既有 markdown header 慣例）
- `check_paths.py`：**Windows baseline 254 / sandbox baseline 241** — CODEX 在 sandbox 跑要求「不增加新 ERROR」即可（C4 patch round 已從 255 → 252）
- `build_repo_index('.')`：要求 0 ERROR
- **baseline 設門檻紀律：** B.9 教訓沿用，不寫死 baseline 數字；只規定「不增加 vs 當前 baseline」

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer + verifier agent。

本輪是「Phase C Wave 11 task」— Phase C 整體驗收 + 撰寫 _design/PHASE_C_COMPLETION_REPORT.md，對齊 TASKS v1.9 §D.7（Phase D 整體驗收 — 註：master 詞彙的 "Phase C" = TASKS 詞彙的 "Phase D"；下游台詞生產 phase）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + verifier — 本輪跑 3 下游 skill 落地驗證 + 3 QA 模板補建驗證 + Wave 10 review consolidation + 撰寫 Phase C 完成報告
- 對應傳統：Wave 11 最終 task；Wave 11 PASS → Phase C 收尾 + Milestone 3 達成 + 開放 Phase D 啟動
- 注意 master vs TASKS 詞彙錯位：master 「Phase C」（下游台詞生產 = 8th master scope）= TASKS 「Phase D」（D.0~D.7）。本 starter 用 master 詞彙；TASKS reference 用 §D.x。

**重要邊界（嚴格 scope）：**

- ✗ 不改任何 LOCKED spec / registry / parser code
- ✗ 不改既有 27 模板 / 00_protocol/ 任何檔（含 Wave 6 patch 過的 5 protocol v0.2 + 00_k v0.1 stale R8-INFO-06 不本輪處理）
- ✗ 不改 .claude/skills/*/SKILL.md 任何檔（含 Wave 10 C.1/C.2/C.3 + 中文 wrapper）
- ✗ 不改既有 Phase A / Phase B SKILL.md
- ✗ 不改 D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.13 / D054_DECISION_PACKAGE v0.2）
- ✗ 不修補 check_paths baseline（屬 9th master cleanup queue NEW_REQ_19 範圍）
- ✗ 不跑真實 /scene-task / /dialogue-write / /qa 寫檔（會污染 Template；端到端測試屬 user 親跑 M3）
- ✗ 不升任何檔狀態（屬人類 D.2.5 / D.3.5 / final-gating gate scope）
- ✗ 不寫 Phase D 9th master scope 任何檔（含 /view-* / /iterate-* / /export-* / /diagnose / /integrate）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §D.7 + Phase A 收尾 A.11 + Phase B B.9 模式 + Wave 10 review consolidation。

### 任務目標

新建 1 個檔：
1. `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Phase C 完成報告；含 5 必填中文 header）

### Wave 11 驗收 4 個維度

**維度 1：技術驗證（CODEX 跑全部）**

1. **check_headers.py：** `python -X utf8 -B scripts/check_headers.py` 須報 0 ERROR；WARN 數 ≤ 當前 baseline +1（含 PHASE_C_COMPLETION_REPORT v1.0 可能 +1 WARN 屬既有 markdown header 慣例）
2. **check_paths.py：** `python -X utf8 -B scripts/check_paths.py` 報 ERROR；本輪不要求降低 baseline，但要求**不增加**（Wave 11 新建 PHASE_C_COMPLETION_REPORT 內 path reference 全採新慣例 — outer fence ~~~ / Instance-only path 加 <instance_root>/ 前綴）
3. **build_repo_index：**
   ```python
   from scripts.parse_frontmatter import build_repo_index
   result = build_repo_index('.')
   errors = [i for i in result.issues if getattr(i, 'severity', None) == 'ERROR']
   warnings = [i for i in result.issues if getattr(i, 'severity', None) == 'WARN']
   ```
   - 要求：errors == 0
   - perf：< 5s
4. **expected_entities.yaml 對齊：** 確認 `_design/expected_entities.yaml` 存在 + Wave 10 後仍可被 build_repo_index 載入 0 ERROR

**維度 2：Wave 10 review consolidation（依 TASKS v1.9 §D.2 / §D.3 / §D.4 + C4 patch round 補建）**

5. **C.1 /scene-task skill 驗收：**
   - `.claude/skills/scene-task/SKILL.md` v0.1 存在 + frontmatter + 5 必填中文 header
   - `.claude/skills/場景任務包/SKILL.md` v0.1 存在 + 極簡 wrapper
   - 5 階段流程完整對齊 UD §2.3.1~§2.3.5
   - **D-054 hybrid 讀檔 fallback 規範段完整**（per-scene → aggregate；對齊 DECISIONS_LOG v2.0 §6.17.2）
   - 啟動前檢查含 D-051 後 single marker + Bootstrap completed + 上游 entity REVIEW check
   - phase_log entry 含 scene_id + task_path + todo_count + read_source（D-054 fallback 結果）
   - 寫檔目錄嚴格限 `07_scene_tasks/`（D-050 子裁決 2 對齊）
   - 邊界含 D-050 子裁決 1 + 子裁決 2 雙 block + 含 D-053 exception 雙 list

6. **C.2 /dialogue-write skill 驗收：**
   - `.claude/skills/dialogue-write/SKILL.md` v0.1 存在 + 中文 wrapper（生成台詞）
   - 6 階段流程對齊 UD §2.4.1~§2.4.7
   - 4 模式 algorithm 對齊 UD §4.2（試寫）/ §4.3（收斂）/ §4.4（破格）+ REQUIREMENTS_LOCK §4.3（SINGLE_ITER）
   - 輸入鎖定 4 形態（A. 試寫預設 / B. --experimental / C. --converge / D. --single-iter）+ 收斂模式 ≥2 trial 路徑要求
   - 啟動前檢查含 D.2.5 gate check（task pack 狀態=REVIEW + pipeline_state=TASK_REVIEW）+ 6 核心欄位 check
   - mode_tag 6 種 enum（DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / FINAL_CANDIDATE / FINAL / SINGLE_ITER）
   - 寫檔目錄嚴格限 `08_dialogue_outputs/`

7. **C.3 /qa skill 驗收：**
   - `.claude/skills/qa/SKILL.md` v0.1 存在 + 中文 wrapper（檢查）
   - 5 階段流程對齊 UD §2.5.1~§2.5.6 v0.3
   - **8 份 QA 報告 algorithm 表完整**（09_a/b/c/d/f/g/h/i；對齊 UD §3.1~§3.9）
   - **8 報告序列印出順序**對齊 UD §2.5.3 v0.3（09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i）
   - qa_decision 規則：8 全 PASS 才 PASS / 任一 FAIL 即 FAIL
   - phase_log entry 含 qa_report_paths（**8 個路徑**；不 5）+ qa_decision
   - 寫檔目錄嚴格限 `09_quality_assurance/` (8 報告) + `08_dialogue_outputs/` frontmatter 兩欄更新
   - 邊界含「**不產 09_e**」+「**不擅升 FINAL**」+「**不修 dialogue body**」
   - **R8-INFO-06 處理註記段完整**（明示本 skill 對齊 UD §2.5.3 v0.3；00_k v0.1 5 報告 stale 不影響）

8. **C4 patch round 09_g/h/i 模板補建驗收：**
   - `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1 存在 + qa_type=RHYTHM + 對齊 UD §3.7
   - `09_quality_assurance/09_h_對話張力檢查模板.md` v0.1 存在 + qa_type=DRAMATIC_TENSION + 對齊 UD §3.8
   - `09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.1 存在 + qa_type=CROSS_SCENE_CONTINUITY + 對齊 UD §3.9
   - 3 模板採同 09_a/b/c/d/f 風格（5 層檢查框架 + 通用化原則 + 不含作品專屬內容）
   - check_paths baseline 從 255 降至 252（C4 patch 後）

**維度 3：Phase C 3 skill 整體鏈驗收**

9. **3 個下游 skill 全部落地（對齊上游 chain）：**
   - `.claude/skills/scene-task/SKILL.md` v0.1
   - `.claude/skills/dialogue-write/SKILL.md` v0.1
   - `.claude/skills/qa/SKILL.md` v0.1
   - 3 個對應中文 wrapper（場景任務包 / 生成台詞 / 檢查）v0.1
10. **8 個 QA 模板全部落地（5 既有 + 3 新）：**
    - 09_a 既有 / 09_b 既有 / 09_c 既有 / 09_d 既有 / 09_f 既有
    - 09_e 既有（final-gating；不在 8 報告必跑範圍）
    - **09_g 新（C4 patch round）/ 09_h 新（C4 patch round）/ 09_i 新（C4 patch round）**
11. **下游 pipeline 依賴鏈完整：**
    - /scene-task → D.2.5 task review gate → /dialogue-write → D.3.5 收斂 gate → /qa → 人類 final-gating + 09_e
    - 5 階段 / 6 階段 / 5 階段對應 UD §2.3 / §2.4 / §2.5
    - pipeline_state 全 9 狀態 enum 覆蓋（SCENE_INDEXED → TASK_DRAFT → TASK_REVIEW → DIALOGUE_TRIAL → DIALOGUE_CONVERGED → QA_PASSED/QA_FAILED → DIALOGUE_FINAL → DIALOGUE_LOCKED）

**維度 4：D-054 hybrid fallback 落地驗證 + Phase C 啟動條件**

12. **D-054 hybrid fallback 設計落地驗證（依 DECISIONS_LOG v2.0 §6.17.2）：**
    - /scene-task SKILL.md 含「## D-054 hybrid 讀檔 fallback 規範」段
    - 兩階段 fallback 完整（per-scene check → aggregate fallback → 拒絕）
    - 既有 /create-detailed-outline SKILL.md v0.3 line 198 escape hatch wording 維持（自然承接 D-054 拍板；不衝突）
    - NEW_REQ_15「per-scene 拆檔 convention 迭代評估」DEFERRED 紀錄完整（POST_LOCK_PENDING v0.13）
13. **Phase C 啟動條件 → Milestone 3 達成判定：**
    - W-rules / W-language / V ≥ REVIEW（Phase A.10）
    - C-* / R-*-* / P / CH-* ≥ REVIEW（Phase B B.5.5 / B.6.5 / B.8）
    - 3 個下游 skill 全落地 + 8 個 QA 模板齊全
    - Phase D 整體驗收 S-*-* ≥ REVIEW 條件 → 屬 user 親跑 M3 testing 範圍（§6 placeholder）
14. **Milestone 3 達成判定：** 4 維度全 PASS → Phase C PASS → Milestone 3「下游 3 skill 完成 → user 可量產台詞」達成

### PHASE_C_COMPLETION_REPORT.md 內容規範

| 段 | 內容 |
|---|---|
| Header | 5 必填中文 header（狀態：DRAFT / 版本：v1.0 / 最後更新：YYYY-MM-DD / 適用範圍：Phase C 完成報告 / 優先級：高）|
| §0 文件目的 | 紀錄 Phase C 整體驗收結果 + Milestone 3 達成宣告依據 + Phase D 啟動條件聲明 |
| §1 驗收摘要 | 4 維度驗收結果 + Milestone 3 達成宣告 + repo SHA + 驗收 owner |
| §2 維度 1 技術驗證 | check_headers / check_paths / build_repo_index / expected_entities 結果表 |
| §3 維度 2 Wave 10 review consolidation | C.1 / C.2 / C.3 skill + C4 patch round 3 QA 模板驗收 |
| §4 維度 3 Phase C 3 skill 整體鏈驗收 | 3 skill + 6 中文 wrapper + 8 QA 模板 + pipeline 依賴鏈表格 |
| §5 維度 4 D-054 hybrid fallback 落地 + Phase C 啟動條件 | D-054 落地驗證 + Phase D 整體驗收 S-*-* 條件聲明 + NEW_REQ_15 追蹤 |
| §6 端到端測試 placeholder | user 親跑步驟（接續 Phase B Instance → /scene-task → D.2.5 gate → /dialogue-write → D.3.5 gate → /qa）；CODEX 不跑寫檔；保留 placeholder；**NEW_REQ_14 AI-assisted §6 補入機制**：user 親跑完後可走 D-052 同模式（master 對話內 user 明示拍板 + agent 從 phase_log / git log / review_log reconstruct §6 內容；user 拍板 OK 後落地）|
| §7 Phase C 完成聲明 | 維度 1/2/3/4 全 PASS → Phase C PASS → Milestone 3 達成 |
| §8 後續：Phase D 啟動條件聲明 | 列出 Phase D 啟動所需條件 + 目前達成狀態 + 9th master cleanup queue 處理優先序 |
| §9 Cross-ref | 列出本報告依據的所有 spec / starter / review_log / SKILL.md / 模板 |

### 文字長度建議

PHASE_C_COMPLETION_REPORT ~250-350 行（同 PHASE_B_COMPLETION_REPORT v1.2 規模 + 3 skill / 8 QA 模板 / 6 wrapper / D-054 hybrid fallback 落地 + NEW_REQ_14 §6 機制 + 9th master cleanup queue 追蹤）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§D.2 + §D.3 + §D.4 + §D.7 + §D.1a 對應）
2. `_design/HANDOFF_TO_8TH_MASTER.md` v1.0（第八輪 master scope + Wave 9-11 工作清單）
3. `_design/PHASE_B_COMPLETION_REPORT.md` v1.2（B.9 範本參考 — 4 維度結構 + §6 user 親跑 placeholder 模式）
4. `_design/PHASE_A_COMPLETION_REPORT.md` v1.1（A.11 範本參考；早期模式）

B. Wave 10 + C4 patch 對齊（**本 task 主要 reference**）
5. `_design/CODEX_C1_STARTER.md` v0.1（C.1 任務驗收條件）
6. `_design/CODEX_C2_STARTER.md` v0.1（C.2 任務驗收條件）
7. `_design/CODEX_C3_STARTER.md` v0.1（C.3 任務驗收條件）
8. `_design/CODEX_C4_PATCH_STARTER.md` v0.1（C4 patch round 09_g/h/i 補建驗收條件）
9. `.claude/skills/scene-task/SKILL.md` v0.1（C.1 落地檔；本 Wave 11 驗收對象）
10. `.claude/skills/dialogue-write/SKILL.md` v0.1（C.2 落地檔）
11. `.claude/skills/qa/SKILL.md` v0.1（C.3 落地檔）
12. `.claude/skills/場景任務包/SKILL.md` v0.1 + `.claude/skills/生成台詞/SKILL.md` v0.1 + `.claude/skills/檢查/SKILL.md` v0.1（3 中文 wrapper）
13. `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1 + `09_h_對話張力檢查模板.md` v0.1 + `09_i_跨場一致性檢查模板.md` v0.1（C4 patch 新建）

C. Phase C upstream / D-NNN 拍板
14. `00_protocol/00_k_台詞生產流程協議.md` v0.1（下游 pipeline；註：R8-INFO-06 5 報告 stale 不本輪 patch）
15. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3 / §2.4 / §2.5 / §3.1~§3.9 / §4
16. `_design/SPEC.md` v1.2 §12.3 場景狀態機 / §12.5 任務包必填 / §12.6 多版本方向 / §12.7 8 報告序列順序
17. `_design/ARCHITECTURE.md` v1.6 §6.1 / §6.2 / §6.3
18. `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043 + §6.12.2 D-050 + §6.13.2 D-051 + §6.16.2 D-053 + §6.17.2 D-054
19. `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1 / §4.2 / §4.3
20. `_design/POST_LOCK_PENDING.md` v0.13（NEW_REQ 整體狀態；含 NEW_REQ_13 RESOLVED via D-054 + NEW_REQ_14 §6 AI-assisted + NEW_REQ_15 D-054 迭代追蹤 + NEW_REQ_19 9th master cleanup queue）
21. `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包；APPLIED）

D. baseline / NEW_REQ 紀律
22. `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO 紀錄；4 finding 入 NEW_REQ_19）
23. `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO；R8-INFO-06 來源）

E. 已 LOCKED 不可動文件
24. 所有 `_design/*.md`（含 Phase B/C 既有 starter / completion report）
25. `_design/registries/*.template.yaml`
26. `scripts/*.py`
27. 既有 27 模板（01_world/ ~ 09_quality_assurance/ 內；含 9 個 QA 模板 09_a~09_i）
28. 所有 `00_protocol/` 檔
29. `_tools/frontend/*`
30. 既有 SKILL.md 全部（Phase A + Phase B + Phase C C.1/C.2/C.3 + 中文 wrappers）

---

**你要交付的產物：**

新建 1 個檔：
1. `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（依上述 §0~§9 結構）

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- PHASE_C_COMPLETION_REPORT.md 存在
- 5 必填中文 header 齊
- §0~§9 章節完整

B. 內容
- §1 驗收摘要含 Milestone 3 達成宣告 + repo SHA + 驗收 owner
- §2 維度 1 4 項技術驗證結果表 + 對齊 NEW_REQ_9 baseline 紀律
- §3 維度 2 Wave 10 C.1/C.2/C.3 + C4 patch round 驗收結果（含 4 子段表格）
- §4 維度 3 Phase C 3 skill / 8 QA 模板 / 6 wrapper / pipeline 依賴鏈表
- §5 維度 4 D-054 hybrid fallback 落地 + Phase C 啟動條件聲明 + NEW_REQ_15 追蹤
- §6 端到端測試保留 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制描述
- §7 Phase C 完成聲明（4 維度全 PASS 判定 + Milestone 3 達成宣告）
- §8 Phase D 啟動條件聲明 + 9th master cleanup queue 處理優先序（NEW_REQ_19 列項）
- §9 Cross-ref 完整

C. 不破壞既有
- 沒動既有 27 模板（含 09_a~09_i 全 9 個 QA 模板）/ _design 既有檔 / scripts / 00_protocol / .claude/skills / _tools/frontend
- 沒動 D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.13 / D054_DECISION_PACKAGE v0.2）
- check_headers.py 0 ERROR 維持
- check_paths.py baseline +0 增量（C4 已從 255 → 252）
- 採新慣例（outer fence ~~~ / Instance-only path 加 <instance_root>/ 前綴）

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master
- **NO-GO：** Wave 11 maintenance dimension 任何維度抓出 LOCKED 變動 / spec 衝突 → 修補 round

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Wave 11 完成 → user commit/push → 回 master：

1. master 寫 `HANDOFF_TO_9TH_MASTER.md`（接 Phase D — /view-* + /iterate-* + /export-* + /diagnose + /integrate）
2. user 可進行 M3 user-test 第三次點（跑完整 3 下游 skill chain；M3 finding 處理同 D-049 / D-052 / D-053 / D-054 模式）
3. M3 user-test 後續若有 finding → 緊急 patch round（同模式）
4. user 親跑完 M3 testing 後 → master 啟動 NEW_REQ_14 AI-assisted §6 補入機制：
   - user 明示拍板「我跑完 M3 chain；補入 §6」
   - master 從 phase_log / git log / review_log / DECISIONS_LOG / POST_LOCK_PENDING reconstruct testing 事實摘要
   - user 拍板 OK 後落地 PHASE_C_COMPLETION_REPORT §6 補入

**Milestone 3 達成宣告條件：**
- Wave 11 PHASE_C_COMPLETION_REPORT v1.0 4 維度全 PASS
- §6 端到端測試 placeholder 等 user 親跑補入（不阻 Milestone 3 宣告；屬 user follow-up）
- 3 個下游 skill 可被 discovery + 8 個 QA 模板齊全
- D-054 hybrid fallback 設計落地 + NEW_REQ_15 追蹤
- 9th master cleanup queue（NEW_REQ_19）明示 handoff 範圍

---

# 3. 文件維護紀律

- 本檔是 Phase C Wave 11 整體驗收 starter；完成後可 archive 進 `_design/archive/`
- 對應 PHASE_C_COMPLETION_REPORT 也屬第八輪 master 收尾事實紀錄；不刪除
- 未來 9th master 收尾前若需類似驗收，可採同 starter pattern 寫 `CODEX_D_FINAL_STARTER.md`

---

# 4. Cross-ref

- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0（第八輪 master scope + Wave 9-11 工作清單）
- `_design/TASKS.md` v1.9 §D.2 + §D.3 + §D.4 + §D.7 + §D.1a
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3 + §2.4 + §2.5 + §3.1~§3.9 + §4
- `_design/SPEC.md` v1.2 §12.3 / §12.5 / §12.6 / §12.7
- `_design/ARCHITECTURE.md` v1.6 §6.1 / §6.2 / §6.3
- `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043 + §6.12.2 D-050 + §6.13.2 D-051 + §6.16.2 D-053 + §6.17.2 D-054
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1 / §4.2 / §4.3
- `_design/POST_LOCK_PENDING.md` v0.13（NEW_REQ_13 RESOLVED + NEW_REQ_14 AI-assisted §6 + NEW_REQ_15 D-054 迭代追蹤 + NEW_REQ_19 9th master cleanup queue + 09_g/h/i 提前處理註記）
- `_design/D054_DECISION_PACKAGE.md` v0.2（APPLIED）
- `_design/CODEX_C1_STARTER.md` v0.1 / `CODEX_C2_STARTER.md` v0.1 / `CODEX_C3_STARTER.md` v0.1 / `CODEX_C4_PATCH_STARTER.md` v0.1
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.2（範本參考）
- `_design/PHASE_A_COMPLETION_REPORT.md` v1.1（早期範本參考）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO；NEW_REQ_19 來源）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO；R8-INFO-06 來源）
- `00_protocol/00_k_台詞生產流程協議.md` v0.1（context；R8-INFO-06 5 報告 stale 不本輪 patch）
- `.claude/skills/scene-task/SKILL.md` v0.1 + `dialogue-write/SKILL.md` v0.1 + `qa/SKILL.md` v0.1
- `.claude/skills/場景任務包/SKILL.md` v0.1 + `生成台詞/SKILL.md` v0.1 + `檢查/SKILL.md` v0.1
- `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1 + `09_h_對話張力檢查模板.md` v0.1 + `09_i_跨場一致性檢查模板.md` v0.1（C4 patch 新建）
- 既有 5 個 QA 模板（09_a/b/c/d/f）+ 09_e（final-gating）
