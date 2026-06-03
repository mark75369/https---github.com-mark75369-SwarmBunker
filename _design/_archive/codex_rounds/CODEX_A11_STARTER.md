狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase A 後段 A.11 task 啟動包 — Phase A 整體驗收 + 升 PHASE_A_COMPLETION_REPORT  
優先級：高

# CODEX_A11_STARTER — Phase A 後段 A.11：Phase A 整體驗收

# 0. 本檔用途

Wave 5 最後一條 task — Phase A 整體驗收 + 撰寫 `_design/PHASE_A_COMPLETION_REPORT.md`，對齊 TASKS v1.7 §A.11（含 Wave 4 review consolidation 子節）。

**前置條件：** Wave 5 前 2 條 DONE（A.9 wrapper smoke test △ PARTIAL Codex App PASS + A.10 人類 REVIEW gate 升 4 模板檔 REVIEW + phase_a_review_log.md 寫好）。

**A.11 PASS → Phase A 收尾 → 開放 Phase B 啟動條件聲明。**

⚠ **A.11 兩段分工：**
- **CODEX 跑：** 技術驗證 + Wave 4 review consolidation + spec 對齊 + 寫 completion report
- **User 親跑（A.11 starter 明示為「user 親跑步驟」）：** 端到端 skill 測試（clone Template → 刪 marker → 跑 /init-project → /create-world → /status → /check-gaps）— CODEX 在 completion report 內保留 placeholder 段供 user 跑完後補入

⚠ **baseline 校正（重要）：**
- `check_headers.py`：**0 ERROR / 18 WARN 是 baseline**（必須維持；18 WARN 屬既有中文 markdown header 慣例）
- `check_paths.py`：**243 ERROR 是 Template 既有 baseline**（範例引用未建檔 + 舊命名殘留；Phase A 不要求 0 ERROR）— CODEX 驗「不增加新 ERROR」即可
- `build_repo_index('.')`：用 `.issues` 屬性篩 `severity == 'ERROR'`（不是 `.get()`）；要求 0 ERROR

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.11 task」— Phase A 整體驗收 + 撰寫 PHASE_A_COMPLETION_REPORT.md，對齊 TASKS v1.7 §A.11（含 Wave 4 review consolidation 子節）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + verifier — 本輪跑技術驗證 + Wave 4 review consolidation + 撰寫 Phase A 完成報告
- 對應傳統：Wave 5 第三條 task（最終）；A.11 PASS → Phase A 收尾 + 開放 Phase B 啟動

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**改 `.claude/skills/*/SKILL.md` 任何檔
- ✗ **不**修補 check_paths 243 ERROR（是 baseline；屬未來 Phase A.X cleanup scope）
- ✗ **不**跑真實 /init-project 寫檔（會污染 Template；端到端測試屬 user 親跑步驟）
- ✗ **不**升任何檔狀態（屬 A.10 人類 gate；本輪只紀錄）

**本 task scope（嚴格限定）：**

依 TASKS v1.7 §A.11（line 833-870）+ Wave 4 review consolidation 子節 + PHASE_3 §6.2 五項解除條件。

### 任務目標

新建 1 個檔：
1. `_design/PHASE_A_COMPLETION_REPORT.md`（v1.0 — Phase A 完成報告；含 5 必填中文 header）

### A.11 驗收 4 個維度

**維度 1：技術驗證（CODEX 跑全部）**

1. **check_headers.py：** `python scripts/check_headers.py` 須報 0 ERROR；WARN 數應 ≤ 20（baseline 18，新增 starter / report 檔可能 +1~2 WARN 屬既有 markdown header 慣例）
2. **check_paths.py：** `python scripts/check_paths.py` baseline 243 ERROR — 本輪不要求降低，但要求**不增加**（CODEX 跑後驗 ERROR 數 ≤ 245）
3. **build_repo_index：**
   ```python
   from scripts.parse_frontmatter import build_repo_index
   result = build_repo_index('.')
   errors = [i for i in result.issues if getattr(i, 'severity', None) == 'ERROR']
   warnings = [i for i in result.issues if getattr(i, 'severity', None) == 'WARN']
   ```
   - 要求：errors == 0
   - perf：< 5s（A.0.10 已驗證 0.44s baseline）
4. **expected_entities.yaml 對齊：** 確認 `_design/expected_entities.yaml` 存在 + 內容可被 build_repo_index 載入
5. **POST_LOCK_PENDING：** 確認 `_design/POST_LOCK_PENDING.md` v0.3 內 NEW_REQ_1~8 全標 RESOLVED（NEW_REQ_2 例外：持續寫作）

**維度 2：Wave 4 review consolidation（依 TASKS v1.7 §A.11 子節）**

對 Wave 4 三產出做正式 review：

| 產出 | 對齊 starter | 驗證要點 |
|---|---|---|
| A.7 `/status` skill | `_design/CODEX_A7_STARTER.md` | 5 階段流程 / `build_repo_index` `parse_file` API / expected set 推導 / 完成度公式對齊 ARCH §2.3 / 缺漏 entity 對應 skill 表 / 時期 C 三條呈現規則 / 4 類錯誤處理 |
| A.8 `/check-gaps` skill | `_design/CODEX_A8_STARTER.md` | 5 階段流程 / TODO·INFERENCE·CONFLICT 掃描 / 空 entities 偵測 / expected-but-missing / view/ mtime 失效偵測對齊 P-003 + UX §7.7 / 4 段輸出 |
| A.12 multi-agent invocation | `_design/CODEX_A12_STARTER.md` | AGENTS.md 既有規範保留 + skill 擴充對齊 ARCH §3.3.0 / CLAUDE.md 含 4 主 skill + 4 中文 wrapper / skill_invocation_guide.md 4 段 copy-paste prompt / 嚴禁 INVOKE.md（grep 0 命中）|

對每產出判定 ✓ / △ / ✗。三產出全 ✓ → Wave 4 review consolidation PASS。

中文 wrapper（極簡）驗證項：frontmatter `name` + `description` 對齊 + 指向英文主檔權威 + 不展開第二套流程。

**維度 3：Phase A 基礎設施完整性**

| 範疇 | 驗證 |
|---|---|
| 5 protocol（00_e/f/g/h/i/k/l）| 全部 .md 檔存在 + 5 必填 header + frontmatter（00_i v0.2 D-049 patch 落地）|
| 5 skill 對應 SKILL.md（init-project / create-world / status / check-gaps + 4 中文 wrapper）| 全 8 個 SKILL.md 存在 + frontmatter |
| 27 模板 frontmatter | A.4 補完；check_headers 0 ERROR baseline |
| 前端 A.0F.0~A.0F.2 | `_tools/frontend/` server.py + static + 8 endpoint adapter；M1-D-01 patch 落地（ProjectDashboard.js 不含 stageLabel）|
| 9 spec 文件 LOCKED 鏈 | SPEC v1.2 / IC v2.1 / DF v0.4 / UD v0.5 / UX_SPEC v0.4 / REQUIREMENTS_LOCK v1.0 / ARCH v1.5 / TASKS v1.7 / DECISIONS_LOG v1.3 / POST_LOCK_PENDING v0.3 |
| `.template_root` marker | root 存在（D-049 落地）|

**維度 4：A.10 review_log + A.9 wrapper smoke test 紀錄完整**

- `_design/phase_a_review_log.md` 存在 + 含 §1 升 4 模板 REVIEW 紀錄
- `_design/wrapper_smoke_test_report.md` 存在 + 含 4 wrapper Codex App PASS 結果

### Phase A 通過判定條件（CODEX 自己跑後判定）

A.11 PASS = 維度 1 + 維度 2 + 維度 3 + 維度 4 全部 PASS。

若任一維度 PARTIAL → A.11 標 PARTIAL（不阻 Phase B 啟動但需補修）。

若任一維度 FAIL → A.11 NO-GO → 開 patch round。

### PHASE_A_COMPLETION_REPORT.md 結構（v1.0 模板）

```markdown
狀態：DRAFT  
版本：v1.0  
最後更新：YYYY-MM-DD  
適用範圍：Phase A 完成報告（master 第六輪 Wave 5 A.11 整體驗收）  
優先級：高

# PHASE_A_COMPLETION_REPORT — Phase A 完成報告

# 0. 文件目的

紀錄 Phase A 整體驗收結果，作為 Phase B 啟動條件聲明依據。

# 1. 驗收摘要

- A.11 task 結果：✓ PASS / △ PARTIAL / ✗ FAIL
- 驗收日期：YYYY-MM-DD
- repo SHA：<commit-sha>
- 驗收 owner：CODEX A.11 對話

# 2. 維度 1：技術驗證

| 檢查 | 結果 | baseline | 驗收 |
|---|---|---|---|
| check_headers.py errors | X | 0 | ✓/✗ |
| check_headers.py warnings | X | 18 (≤ 20) | ✓/✗ |
| check_paths.py errors | X | 243 (≤ 245) | ✓/✗ |
| build_repo_index errors | X | 0 | ✓/✗ |
| build_repo_index perf | X.Xs | < 5s | ✓/✗ |
| expected_entities.yaml 對齊 | ✓/✗ |
| POST_LOCK_PENDING NEW_REQ 1/3/4/5/6/7/8 RESOLVED | ✓/✗ |

# 3. 維度 2：Wave 4 review consolidation

## 3.1 A.7 /status skill

[逐項驗收 + ✓/△/✗ + 理由]

## 3.2 A.8 /check-gaps skill

[逐項驗收 + ✓/△/✗ + 理由]

## 3.3 A.12 multi-agent invocation

[逐項驗收 + ✓/△/✗ + 理由]

## 3.4 4 中文 wrapper（極簡）

[逐項驗收 + ✓/△/✗]

# 4. 維度 3：Phase A 基礎設施

[逐項列驗收結果]

# 5. 維度 4：A.10 / A.9 紀錄

[review_log + smoke_test_report 對齊驗收]

# 6. 端到端測試（user 親跑步驟 — placeholder）

Phase A.11 task 規定 8 step 端到端測試屬「user 親跑」性質（CODEX 無 live agent 環境）：

1. `git clone <template-url> <new-instance-dir>`
2. `cd <new-instance-dir>` + `rm .template_root`
3. 跑 /init-project 完成 bootstrap
4. 確認 .protocol_version 產生
5. 跑 /create-world 5 階段
6. 確認 01_a / 01_b / 01_c / 02_* / 作品 00_b 內容
7. 跑 /status 確認完成度
8. 跑 /check-gaps 確認 TODO 清單合理

**user 親跑結果待補：** [user 跑完後在本檔 §6 補入結果摘要]

# 7. Phase A 完成聲明

- 維度 1-5 全部 PASS（含 end-to-end placeholder） + ✓ Phase A 收尾
- 廣義 Phase A 基礎設施 review 由 A.10 user 拍板「全升」涵蓋
- Phase B 啟動條件達成宣告：[依驗收結果填]

# 8. 後續：Phase B 啟動條件聲明

- Phase B = B.0 ~ B.9（5 個 /create-* skill + REVIEW gates）
- 啟動前置條件：
  - ✓ Phase A 五 skill 可跑（init-project / create-world / status / check-gaps + 4 中文 wrapper）
  - ✓ 27 模板 frontmatter 對齊
  - ✓ 4 模板檔 W/V 升 REVIEW
  - ✓ A.11 PASS

# 9. Cross-ref

- _design/TASKS.md v1.7 §A.11 + Wave 4 review consolidation
- _design/DECISIONS_LOG.md v1.3 §6.10 / §6.11
- _design/phase_a_review_log.md（A.10 升級紀錄）
- _design/wrapper_smoke_test_report.md（A.9 PARTIAL Codex App PASS）
- _design/POST_LOCK_PENDING.md v0.3（NEW_REQ_1~8 status）
- _design/PHASE_3_COMPLETION_REPORT.md v4.0 FINAL（Phase 3 完成；不變）
```

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.7（§A.11 line 833-870 + Wave 4 review consolidation 子節）
2. `_design/ARCHITECTURE.md` v1.5（§2.3 完成度 + §3.2 wrapper + §3.3.0 multi-agent + §3.3.2 Template-detect）
3. `_design/SPEC.md` v1.2（§5.1 entity / §5.3 完成度 / §5.4 phase_log / §10 缺漏偵測 / §16 文件狀態機）
4. `_design/PHASE_3_COMPLETION_REPORT.md` v4.0 FINAL（範式參考；本檔不動）

B. 對齊依據
5. `_design/CODEX_A7_STARTER.md`（A.7 starter 規範）
6. `_design/CODEX_A8_STARTER.md`（A.8 starter 規範）
7. `_design/CODEX_A12_STARTER.md`（A.12 starter 規範）
8. `_design/CODEX_A9_STARTER.md`（A.9 starter 規範）
9. `_design/phase_a_review_log.md`（A.10 升級紀錄）
10. `_design/wrapper_smoke_test_report.md`（A.9 PARTIAL 結果）
11. `_design/POST_LOCK_PENDING.md` v0.3（NEW_REQ_1~8 RESOLVED 狀態）
12. `_design/DECISIONS_LOG.md` v1.3（§6.10 / §6.11 master 第六輪紀錄）
13. `scripts/parse_frontmatter.py`（build_repo_index API）
14. `scripts/check_headers.py` / `scripts/check_paths.py`
15. `_design/expected_entities.yaml`
16. `.claude/skills/*/SKILL.md`（8 個 SKILL.md — Wave 3 + Wave 4 落地）
17. `00_protocol/00_i_專案初始化協議.md` v0.2（D-049 patch）

C. 已 LOCKED 不可動文件
18. 所有 `_design/*.md` 既有 spec（除新建 PHASE_A_COMPLETION_REPORT.md 外不動）
19. `scripts/*.py`
20. 既有 27 模板
21. `00_protocol/*` 全部
22. `_tools/frontend/*` 全部
23. 所有 `.claude/skills/*/SKILL.md`
24. `.template_root` marker
25. `_user_manual/` 既有 11 章 + skill_invocation_guide.md
26. `AGENTS.md` / `CLAUDE.md`
27. `phase_a_review_log.md` + `wrapper_smoke_test_report.md`（A.10 / A.9 紀錄；不動）

---

**你要交付的產物：**

新建 1 個檔：
1. `_design/PHASE_A_COMPLETION_REPORT.md`（v1.0 — 含 9 段全部）

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- `_design/PHASE_A_COMPLETION_REPORT.md` 存在
- 5 必填中文 header
- 9 段全部（§0~§9）含內容；§6 end-to-end 段含 placeholder 等 user 補

B. 內容
- 維度 1 四項全部驗證 + ✓/✗ 標示
- 維度 2 Wave 4 三產出 + 4 wrapper 全部驗證
- 維度 3 Phase A 基礎設施全項目驗證
- 維度 4 A.10 review_log + A.9 smoke_test_report 對齊驗收
- Phase A 完成判定明確（PASS / PARTIAL / FAIL）
- Phase B 啟動條件聲明明確

C. 不破壞既有
- 不動所有 LOCKED 文件
- 不修補 check_paths 既有 243 ERROR
- 不跑寫檔的端到端 step（保留 user 親跑）
- `python scripts/check_headers.py` 0 ERROR 維持

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓ + Phase A 完成判定明確
- **BLOCKED：** 任一 ✗ 回 master
- **NO-GO：** 維度 1/2/3/4 任一 FAIL → 修補 round
- **PARTIAL：** 端到端段 placeholder 等 user 補；屬正常 PARTIAL（不阻 Phase B 啟動）

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.11 完成 → user commit/push → 回 master → master 印 Phase B 啟動條件聲明 + 寫 HANDOFF_TO_7TH_MASTER.md（如本輪將結束）→ user 可進 Phase B Wave 6（B.0~B.4 protocol writing）。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.11 task 啟動包；完成後可 archive 進 `_design/archive/`
- A.11 報告 `PHASE_A_COMPLETION_REPORT.md` 屬 Phase A 完成事實檔（不 archive；類似 PHASE_3_COMPLETION_REPORT）
- 若 A.11 NO-GO patch round → 開 CODEX_A11_PATCH_STARTER.md
