狀態：DRAFT  
版本：v0.5（9th master cleanup queue R10-MI-01 sweep — §1 維度 2/3 active checklist CH v0.2 → v0.3（R9-INFO-02 patch round 3 升）；header note 對齊當前事實；用一次性 sweep 處理避免「Fix one, find two」cascade）  
最後更新：2026-05-22  
適用範圍：Phase B Wave 8 B.9 task 啟動包 — Phase B 整體驗收 + 升 PHASE_B_COMPLETION_REPORT  
優先級：高

# CODEX_B9_STARTER — Phase B Wave 8 B.9：Phase B 整體驗收

# 0. 本檔用途

Wave 8 最後一條 task — Phase B 整體驗收 + 撰寫 `_design/PHASE_B_COMPLETION_REPORT.md`，對齊 TASKS v1.9 §B.9。

> **v0.1 → v0.2 D-050 對齊 patch 紀錄（2026-05-20）：**
>
> v0.1 寫作時 DECISIONS_LOG 為 v1.4（未含 D-050）；§1 維度 2 第 5 項驗收 line 92 引用「階段 4 拆分規則對齊 00_h §10.11（05_b/c/d/e + 06_a）」— **已 supersede**。正確驗收條件：
> - B.7 SKILL.md 階段 4 拆分規則對齊 **00_h §10.7** + 寫檔限 **`05_b` + `06_a`**（依 D-050 子裁決 2 CH 行）
> - 階段 4 frontmatter 規範對齊 **00_h §10.8**（非 §10.12）
> - B.7 SKILL.md 含 D-050 子裁決 1 + 子裁決 2 明示句（依 Wave 7 patch round 模式）
>
> Wave 7 patch round 已完成（git commit `27e78b1`）+ Round 2 PASS（git commit `da305a5`）+ B.7 SKILL.md 已對齊 D-050（git commit `399a526`） — B.9 CODEX 驗收應對齊 v0.2 patch 紀錄後的正確條件。

**前置條件：** Wave 8 前 2 條 DONE — B.7 ✓（/create-detailed-outline skill 已實作 + 5 階段可跑）+ B.8 ✓（Phase B 整體 REVIEW gate user 親跑完 + phase_b_review_log.md §1 entry 寫好）。

**B.9 PASS → Phase B 收尾 → Milestone 2 達成宣告 → 開放 Phase C 啟動條件聲明 → 寫 `HANDOFF_TO_8TH_MASTER.md` 接 Phase C。**

⚠ **B.9 兩段分工：**
- **CODEX 跑：** 5 skill 落地驗證 + 5 protocol v0.2 對齊驗證 + Wave 8 review consolidation + spec 對齊 + 寫 completion report
- **User 親跑（B.9 starter 明示為「user 親跑步驟」）：** 端到端 5 skill 鏈測試（接續 Phase A 測試 Instance → 跑 /create-character ≥ 2 次 + B.5.5 → /create-relationship → /create-outline + B.6.5 → /create-detailed-outline → /status）— CODEX 在 completion report 內保留 §6 placeholder 供 user 跑完後補入

⚠ **baseline 紀律（依 NEW_REQ_9 + NEW_REQ_10 教訓）：**
- `check_headers.py`：**0 ERROR / WARN ≤ 26 是 baseline**（Phase A 18 + Wave 6/7/8 累積 ≤ 8 增量；含本輪 Wave 8 新 starter / completion report）
- `check_paths.py`：**Windows baseline 254 ERROR 是 baseline**（NEW_REQ_9 紀錄）/ sandbox baseline 243 ERROR — CODEX 在 sandbox 跑驗「不增加新 ERROR」即可
- `build_repo_index('.')`：用 `.issues` 屬性篩 `severity == 'ERROR'`；要求 0 ERROR
- **baseline 設門檻紀律：** 依 NEW_REQ_9 教訓，B.9 starter 不寫死 baseline 數字；只規定「不增加 vs 當前 baseline」

⚠ **新慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer + verifier agent。

本輪是「Phase B Wave 8 B.9 task」— Phase B 整體驗收 + 撰寫 _design/PHASE_B_COMPLETION_REPORT.md，對齊 TASKS v1.9 §B.9。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + verifier — 本輪跑 5 skill 落地驗證 + 5 protocol 對齊驗證 + Wave 8 review consolidation + 撰寫 Phase B 完成報告
- 對應傳統：Wave 8 第三條 task（最終）；B.9 PASS → Phase B 收尾 + Milestone 2 達成 + 開放 Phase C 啟動

**重要邊界（嚴格 scope）：**

- ✗ 不改任何 LOCKED spec / registry / parser code
- ✗ 不改既有 27 模板 / 00_protocol/ 任何檔（含 Wave 6 patch 過的 4 protocol v0.2）
- ✗ 不改 .claude/skills/*/SKILL.md 任何檔（含 Wave 7/8 全 5 個 /create-* skill）
- ✗ 不改 Phase A SKILL.md / 4 中文 wrapper
- ✗ 不修補 check_paths baseline（屬未來 Phase A.X cleanup scope；NEW_REQ_9）
- ✗ 不跑真實 /create-* 寫檔（會污染 Template；端到端測試屬 user 親跑步驟）
- ✗ 不升任何檔狀態（屬 B.8 人類 gate；本輪只紀錄）
- ✗ 不寫 Phase C / Phase D skill 任何檔

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.9（line 1390-1403）+ Phase A 收尾 A.11 模式 + Wave 8 review consolidation。

### 任務目標

新建 1 個檔：
1. `_design/PHASE_B_COMPLETION_REPORT.md` v1.0（Phase B 完成報告；含 5 必填中文 header）

### B.9 驗收 4 個維度

**維度 1：技術驗證（CODEX 跑全部）**

1. **check_headers.py：** `python -X utf8 -B scripts/check_headers.py` 須報 0 ERROR；WARN 數 ≤ 當前 baseline +2（含 PHASE_B_COMPLETION_REPORT v1.0 可能 +1~2 WARN 屬既有 markdown header 慣例）
2. **check_paths.py：** `python -X utf8 -B scripts/check_paths.py` 報 ERROR；本輪不要求降低 baseline，但要求**不增加**（Wave 8 新建 PHASE_B_COMPLETION_REPORT 內 path reference 全採新慣例 — outer fence ~~~  / Instance-only path 加 <instance_root>/ 前綴）
3. **build_repo_index：**
   ```python
   from scripts.parse_frontmatter import build_repo_index
   result = build_repo_index('.')
   errors = [i for i in result.issues if getattr(i, 'severity', None) == 'ERROR']
   warnings = [i for i in result.issues if getattr(i, 'severity', None) == 'WARN']
   ```
   - 要求：errors == 0
   - perf：< 5s（A.0.10 已驗證 0.44s baseline）
4. **expected_entities.yaml 對齊：** 確認 `_design/expected_entities.yaml` 存在 + Wave 6/7/8 後仍可被 build_repo_index 載入 0 ERROR

**維度 2：Wave 8 review consolidation（依 TASKS v1.9 §B.7 / §B.8 / §B.9）**

5. **B.7 /create-detailed-outline skill 驗收：**
   - `.claude/skills/create-detailed-outline/SKILL.md` v0.3 存在 + frontmatter + 5 必填中文 header（含 R8-MA-01 prereq fix + R9-INFO-02 body D-050 子裁決 1+2 雙 block）
   - `.claude/skills/建立細綱/SKILL.md` v0.1 存在 + 極簡 wrapper
   - 5 階段流程完整對齊 00_h v0.2 protocol（含 §4.0 D-047 機制段 + §4.1 議題預設表 6 議題）
   - 階段 4 拆分規則對齊 00_h §10.7（05_b + 06_a；依 D-050 子裁決 2 CH 行 — 05_c/d/e 屬 P /create-outline scope）
   - frontmatter 規範對齊 00_h §10.8
   - 啟動前依賴檢查含 P REVIEW 條件（拒絕 DRAFT）
   - phase_log entry 含 status=completed + created_entities=[CH-*, S-*-*]
   - 階段 5 自動呼叫 /status
   - 禁止事項明示（不擅自跳階段 / 不擅自補完 / 不擅自呼叫其他 skill / 不擅自升 status）

6. **B.8 Phase B REVIEW gate 驗收：**
   - `_design/CODEX_B8_REVIEW_GATE_STARTER.md` v0.5 存在
   - `_design/phase_b_review_log.md` v0.5 存在（Template 內為骨架）
   - starter 內 §1 啟動 prompt 涵蓋 5 類實體（C-* / R-*-* / P / CH-* / S-*-*）grep 邏輯
   - starter 明示 user 親跑紀律（CODEX 不自行升 status）

**維度 3：Phase B 5 skill 整體鏈驗收**

7. **5 個 /create-* skill 全部落地：**
   - `.claude/skills/create-world/SKILL.md` v0.1（Phase A.6；非 Phase B 但屬上游 chain）
   - `.claude/skills/create-character/SKILL.md` v0.4（B.5；含 D-050 對齊 + Round 11 R11-CRITICAL-01 修補）
   - `.claude/skills/create-relationship/SKILL.md` v0.3（B.5b；含 D-050 對齊）
   - `.claude/skills/create-outline/SKILL.md` v0.3（B.6；含 D-050 對齊）
   - `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7；R8-MA-01 prereq fix + R9-INFO-02 body D-050 子裁決 1+2 雙 block）
   - 5 個對應中文 wrapper /SKILL.md v0.1
8. **5 個 /create-* protocol 全 v0.2（D-047 對齊）：**
   - 00_protocol/00_e_世界觀創建協議.md（Phase A.3；A.11 已 verify）
   - 00_protocol/00_f_角色創建協議.md v0.2（Wave 6 patch）
   - 00_protocol/00_g_大綱創建協議.md v0.2（Wave 6 patch）
   - 00_protocol/00_h_細綱創建協議.md v0.2（Wave 6 patch）
   - 00_protocol/00_l_關係創建協議.md v0.2（Wave 6 patch）
9. **5 個 review log 骨架全部落地：**
   - `_design/phase_a_review_log.md` v0.1（A.10）
   - `_design/phase_b_character_review_log.md` v0.3（B.5.5）
   - `_design/phase_b_outline_review_log.md` v0.4（B.6.5）
   - `_design/phase_b_review_log.md` v0.5（B.8 — Template 內為骨架）

**維度 4：4 個 REVIEW gate starter 對齊（含 A.10 inline-executed）**

10. **A.10 / B.5.5 / B.6.5 / B.8 starter 對齊：**
    - A.10 由 master 第六輪 inline-executed（無 starter 檔；紀錄在 phase_a_review_log.md §1）— 不在本維度驗
    - `_design/CODEX_B55_REVIEW_GATE_STARTER.md` v0.4 存在 + outer fence ~~~ + 對應 phase_b_character_review_log.md 骨架
    - `_design/CODEX_B65_REVIEW_GATE_STARTER.md` v0.4 存在 + outer fence ~~~ + Instance-only path 加 <instance_root>/ 前綴 + 對應 phase_b_outline_review_log.md 骨架
    - `_design/CODEX_B8_REVIEW_GATE_STARTER.md` v0.5 存在 + outer fence ~~~ + 5 類實體 grep 邏輯 + 對應 phase_b_review_log.md 骨架

### PHASE_B_COMPLETION_REPORT.md 內容規範

| 段 | 內容 |
|---|---|
| Header | 5 必填中文 header（狀態：DRAFT / 版本：v1.0 / 最後更新：YYYY-MM-DD / 適用範圍：Phase B 完成報告 / 優先級：高）|
| §0 文件目的 | 紀錄 Phase B 整體驗收結果 + Phase C 啟動條件聲明依據 |
| §1 驗收摘要 | 4 維度驗收結果 + Milestone 2 達成宣告 + repo SHA + 驗收 owner |
| §2 維度 1 技術驗證 | check_headers / check_paths / build_repo_index / expected_entities 結果表 |
| §3 維度 2 Wave 8 review consolidation | B.7 / B.8 starter + review_log 骨架驗收 |
| §4 維度 3 Phase B 5 skill 整體鏈驗收 | 5 skill + 5 protocol + 5 review_log + 4 wrapper 表格 |
| §5 維度 4 4 REVIEW gate starter 對齊 | A.10 inline + B.5.5 / B.6.5 / B.8 starter 對齊 |
| §6 端到端測試 placeholder | user 親跑步驟（接續 Phase A Instance → /create-character ≥ 2 + B.5.5 → /create-relationship → /create-outline + B.6.5 → /create-detailed-outline → /status）；CODEX 不跑寫檔；保留 placeholder |
| §7 Phase B 完成聲明 | 維度 1/2/3/4 全 PASS → Phase B PASS → Milestone 2 達成 |
| §8 後續：Phase C 啟動條件聲明 | 列出 Phase C 啟動所需條件 + 目前達成狀態 |
| §9 Cross-ref | 列出本報告依據的所有 spec / starter / review_log / SKILL.md |

### 文字長度建議

PHASE_B_COMPLETION_REPORT ~200-300 行（同 PHASE_A_COMPLETION_REPORT v1.1 規模 + 5 skill / 5 protocol / 4 wrapper / 3 review_log 表格擴充）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.9（§B.9 line 1390-1403 + §B.7 / §B.8 sub-task）
2. `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope + Wave 8 工作清單）
3. `_design/PHASE_A_COMPLETION_REPORT.md` v1.1（A.11 範本參考 — 4 維度結構 + master inline patch baseline 校正模式）

B. Wave 8 三 task 對齊
4. `_design/CODEX_B7_STARTER.md` v0.3（B.7 任務驗收條件）
5. `_design/CODEX_B8_REVIEW_GATE_STARTER.md` v0.5（B.8 任務驗收條件）
6. `_design/phase_b_review_log.md` v0.5（B.8 升級紀錄骨架）

C. Phase B 5 skill 鏈
7. `00_protocol/00_e / 00_f / 00_g / 00_h / 00_l`（5 個 v0.2 上游 protocol；Wave 6 patch）
8. `.claude/skills/create-world / create-character / create-relationship / create-outline / create-detailed-outline /SKILL.md`（5 個英文 skill；Phase A.6 + Wave 7 + 本輪 B.7）
9. `.claude/skills/建立世界觀 / 建立角色 / 建立關係 / 建立大綱 / 建立細綱 /SKILL.md`（5 個中文 wrapper）

D. baseline / NEW_REQ 紀律
10. `_design/POST_LOCK_PENDING.md` v0.14（NEW_REQ_9 baseline 校正 + NEW_REQ_10 fence 慣例 + NEW_REQ_11 翻譯工具提案 DEFERRED + NEW_REQ_12 RESOLVED via D-053 + NEW_REQ_13 RESOLVED via D-054 + NEW_REQ_14 §6 補入 AI-assisted DEFERRED + NEW_REQ_15 D-054 hybrid 迭代評估 DEFERRED + NEW_REQ_16/17/18 自動化 QA 3 層架構 DEFERRED + NEW_REQ_19 9th master cleanup queue 處理紀錄 PROCESSED）
11. `_design/DECISIONS_LOG.md` v2.0 §6.11.7（A.11 baseline 校正先例）+ §6.12.2 D-050 + §6.13.2 D-051 + §6.15.2 D-052 + §6.16.2 D-053 + §6.17.2 D-054（per-scene 檔 convention Hybrid）

E. 已 LOCKED 不可動文件
12. 所有 `_design/*.md`（含 PHASE_A_COMPLETION_REPORT）
13. `_design/registries/*.template.yaml`
14. `scripts/*.py`
15. 既有 27 模板
16. 所有 `00_protocol/` 檔
17. 所有 `.claude/skills/` 檔（Phase A + Wave 7 + Wave 8 B.7）
18. `_tools/frontend/*`

---

**你要交付的產物：**

新建 1 個檔：
1. `_design/PHASE_B_COMPLETION_REPORT.md` v1.0（依上述 §0~§9 結構）

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- PHASE_B_COMPLETION_REPORT.md 存在
- 5 必填中文 header 齊
- §0~§9 章節完整

B. 內容
- §1 驗收摘要含 Milestone 2 達成宣告 + repo SHA + 驗收 owner
- §2 維度 1 4 項技術驗證結果表 + 對齊 NEW_REQ_9 baseline 紀律
- §3 維度 2 Wave 8 B.7 / B.8 starter + review_log 驗收結果
- §4 維度 3 Phase B 5 skill / 5 protocol / 5 wrapper 表
- §5 維度 4 4 REVIEW gate（A.10 + B.5.5 + B.6.5 + B.8）對齊驗收
- §6 端到端測試保留 user 親跑 placeholder
- §7 Phase B 完成聲明（4 維度全 PASS 判定）
- §8 Phase C 啟動條件聲明
- §9 Cross-ref 完整

C. 不破壞既有
- 沒動既有 27 模板 / _design 既有檔 / scripts / 00_protocol / .claude/skills / _tools/frontend
- check_headers.py 0 ERROR 維持
- check_paths.py baseline +0 增量
- 採新慣例（outer fence ~~~ / Instance-only path 加 <instance_root>/ 前綴）

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一 ✗ 回 master

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX B.9 完成 → user commit/push → 回 master：

1. master 第七輪寫 `HANDOFF_TO_8TH_MASTER.md`（接 Phase C — /scene-task + /dialogue-write + /qa + 3 中文 wrapper）
2. user 可進行 M2 user-test 第二次點（跑完整 5 個 /create-\* skill 路徑 + 對齊 issue_type_registry 客製化議題 + 驗整體上游節奏）
3. M2 user-test 後續若有 finding → 緊急 patch round（同 D-049 / NEW_REQ_10 模式）

**Milestone 2 達成宣告�