狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 3 完成後 Round 10 重審 — Round 9 5 MINOR + R9-INFO-02 cleanup verification + 版本 cross-ref 全 sweep verification  
優先級：高

# CODEX_8TH_MASTER_PATCH3_REVIEW_STARTER — Round 10 重審

# 0. 本檔用途

8th master 流程進展：Cleanup round → Round 8 GO → patch round 2 → Round 9 NEAR-GO (5 MINOR + 2 INFO) → patch round 3 完成 → **本輪 Round 10 重審驗證 patch round 3 沒新 regression + R9 finding 全 RESOLVED**。

**前置條件：** 8th master patch round 3 已完成所有預定變動（R9-MI-01~05 + R9-INFO-02 共 6 finding；觸及 6 檔）+ user 已 commit/push。

**重審 GO →** 8th master 進 Phase C Wave 9 — 寫 3 個下游 starter（C1 /scene-task + C2 /dialogue-write + C3 /qa；含 D-054 hybrid fallback 邏輯設計）

**重審 NEAR-GO →** user 拍板 hard-limit accepted（殘留 finding 入 9th master cleanup queue）或開 patch round 4 → Round 11 重審

**重審 NO-GO →** 大幅 rollback / restructure；user 拍板路徑

⚠ **單輪結束 default 紀律延續：** Round 10 預設一輪結束；不預設自動進 Round 11。

⚠ **patch round 3 設計意圖：** 一次性 sweep 全 active 版本 cross-ref stale（vs patch round 2 局部修補導致 cascade）— Round 10 應驗證 sweep 是否真乾淨

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第八輪 master patch round 3 完成後 Round 10 重審」— 對 patch round 3 期間的所有變動跑「R9 finding 關閉 + sweep 完整性 + regression」三重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1-9 重審模式（CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT v0.1 是 baseline；NEAR-GO 含 5 MINOR R9-MI-01~05 + 2 INFO；本輪 verify patch round 3 處理 5 MINOR + 1 INFO 後狀態）
- 對應前置：8th master patch round 3 已完成 R9-MI-01~05 + R9-INFO-02 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /create-* / /init-project 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✗ 不重審 Round 1-9 已 accepted 之 finding（R7 9 finding + R8 INFO + R9 INFO-01 已 closed；不重議）
- ✗ 不下 D-054 結論（已 RESOLVED via D-054 in DECISIONS_LOG v2.0 §6.17）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

8th master patch round 3 變動清單（給你做 review baseline — 6 檔）：

### R9 MINOR 修正（5 處 → 觸及檔 5 個）

1. **R9-MI-01** — `_design/phase_b_review_log.md`：v0.4 → v0.5
   - §4 Cross-ref 4 skill 行從合併單行 + v0.2 → 分行重列 + C/R/P v0.3 + CH v0.2
   - header version 升 v0.5 + 對齊 patch round 3 sweep 結果

2. **R9-MI-02** — `_design/PHASE_B_COMPLETION_REPORT.md`：v1.1 → v1.2
   - §3.2 驗收表 `phase_b_review_log.md v0.3` → `v0.5`
   - §4.1 5 skill 表 C/R/P v0.2 → v0.3、CH v0.1 → v0.2 + 加 D-053 exception block 註記 + R8-MA-01 prereq fix 註記
   - §9 Cross-ref `phase_b_review_log v0.3 → v0.5` + `phase_b_character_review_log v0.2 → v0.3` + `phase_b_outline_review_log v0.3 → v0.4`
   - 說明段補 R8-MI-05 patch round 2 升 C/R/P v0.3 含 D-053 exception 同步紀錄
   - header version 升 v1.2 + 對齊 patch round 3 sweep 結果

3. **R9-MI-03** — `_design/phase_b_character_review_log.md`：v0.2 → v0.3
   - §4 Cross-ref `create-character/SKILL.md v0.2` → `v0.3` + `create-relationship/SKILL.md v0.2` → `v0.3`（兩行；含 D-050 對齊 + D-053 exception block 註記）
   - header version 升 v0.3 + 對齊 patch round 2/3 升版事實

4. **R9-MI-04** — `_design/phase_b_outline_review_log.md`：v0.3 → v0.4
   - §4 Cross-ref `create-outline/SKILL.md v0.2` → `v0.3`（含 D-050 對齊 + D-053 exception block 註記） + `phase_b_character_review_log v0.2` → `v0.3`
   - header version 升 v0.4 + 對齊 patch round 2/3 升版事實

5. **R9-MI-05** — `_design/CODEX_B9_STARTER.md`：v0.3 → v0.4
   - active checklist 13 處版本 stale sweep 修正：
     - line 109: B8 starter v0.4 → v0.5
     - line 110: phase_b_review_log v0.3 → v0.5
     - line 118-121: C/R/P v0.2 → v0.3、CH v0.1 → v0.2
     - line 131: phase_b_character_review_log v0.2 → v0.3
     - line 132: phase_b_outline_review_log v0.2 → v0.4
     - line 133: phase_b_review_log v0.3 → v0.5
     - line 139-140: B55/B65 v0.3 → v0.4
     - line 141: B8 v0.4 → v0.5 + phase_b_review_log 骨架 v0.5
     - line 174-175: cross-ref B8 v0.4 → v0.5 + phase_b_review_log v0.3 → v0.5
   - header version 升 v0.4 + 最後更新 2026-05-21

### R9-INFO 修正（1 處 — 故意納入 patch round 3 scope）

6. **R9-INFO-02** — `.claude/skills/create-detailed-outline/SKILL.md`：v0.2 → v0.3
   - 「## 邊界」段最後加 **D-050 子裁決 1** block + **D-050 子裁決 2** block 對齊 C/R/P body 格式
   - D-050 子裁決 1 block 含 D-053 /create-world exception 雙 exception list（同 C/R/P 格式）+「本 skill 不在例外範圍」
   - D-050 子裁決 2 block 限定本 skill 寫檔範圍 `05_b_章節結構模板.md + 06_a_場景索引模板.md` 兩檔
   - header version 升 v0.3 + 紀錄 R9-INFO-02 patch 內容

### 8th master patch round 3 不動段（聲明）

- 不動 LOCKED spec：SPEC / INTEGRATION_CONTRACTS / DATA_FORMAT_SPEC / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA
- 不動 ARCH v1.6（Cleanup round 已升；本輪不動）
- 不動 TASKS v1.9（同上）
- 不動 DECISIONS_LOG v2.0（D-054 拍板已落地 in §6.17；本輪不動）
- 不動 POST_LOCK_PENDING v0.10（D-054 落地時已升；本輪不動）
- 不動 D054_DECISION_PACKAGE v0.2（D-054 落地時已升；本輪不動）
- 不動 LOCKED registries：3 個 *.template.yaml
- 不動 scripts/*.py
- 不動 27 模板
- 不動 00_protocol/ 任何檔
- 不動 init-project SKILL.md / check-gaps / status / 6 個對應中文 wrapper
- 不動 create-world / create-character / create-relationship / create-outline SKILL.md（patch round 2 已升 v0.3；本輪不動）
- 不動 B55/B65/B8 review gate starter（Cleanup round 已升 v0.4/v0.4/v0.5；本輪不動）
- 不動 4 個 Phase B 中文 wrapper（Cleanup round 已對齊；本輪不動）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 4 維度（精簡版 — 不重做 Round 8/9 已 verify 完的維度）

**維度 1：R9 6 finding 關閉完整性（最優先）**

對 R9 報告 §10 的 5 MINOR + R9-INFO-02 逐項 verify 是否關閉：

| Finding | 預期關閉證據 |
|---|---|
| R9-MI-01 | `phase_b_review_log.md:2` header 升 v0.5；`:144-147` 4 skill 分行重列 + C/R/P v0.3 + CH v0.2 |
| R9-MI-02 | `PHASE_B_COMPLETION_REPORT.md:2` header 升 v1.2；`:94` review_log v0.5；`:109-112` 5 skill 表 C/R/P v0.3 + CH v0.2；`:249-252` §9 Cross-ref 對齊 |
| R9-MI-03 | `phase_b_character_review_log.md:2` header 升 v0.3；`:87-88` Cross-ref C/R v0.3 |
| R9-MI-04 | `phase_b_outline_review_log.md:2` header 升 v0.4；`:95` character_review_log v0.3；`:98` outline v0.3 |
| R9-MI-05 | `CODEX_B9_STARTER.md:2` header 升 v0.4；line 109/110/118-121/131-133/139-141/174-175 全對齊事實版本 |
| R9-INFO-02 | `create-detailed-outline/SKILL.md:7` header 升 v0.3；「## 邊界」段後加 D-050 子裁決 1 + 子裁決 2 雙 block，含 D-053 exception 雙 list |

對每筆 finding：標記 RESOLVED / PARTIAL / NOT_RESOLVED。

**維度 2：版本 cross-ref sweep 完整性（patch round 3 核心目標）**

verify patch round 3 真的一次性 sweep 全 active 版本 cross-ref stale（vs patch round 2 cascade 問題）：

grep 全 `_design/` + `.claude/skills/` active 檔案，找剩餘 stale 版本 cross-ref：

- `create-character/SKILL.md v0.2` 應為 v0.3
- `create-relationship/SKILL.md v0.2` 應為 v0.3
- `create-outline/SKILL.md v0.2` 應為 v0.3
- `create-detailed-outline/SKILL.md v0.1` 或 `v0.2` 應為 v0.3
- `CODEX_B8_REVIEW_GATE_STARTER.md v0.4` 應為 v0.5
- `CODEX_B55_REVIEW_GATE_STARTER.md v0.3` 應為 v0.4
- `CODEX_B65_REVIEW_GATE_STARTER.md v0.3` 應為 v0.4
- `phase_b_character_review_log.md v0.2` 應為 v0.3
- `phase_b_outline_review_log.md v0.2` 或 `v0.3` 應為 v0.4
- `phase_b_review_log.md v0.3` 或 `v0.4` 應為 v0.5
- `PHASE_B_COMPLETION_REPORT.md v1.1` 應為 v1.2
- `CODEX_B9_STARTER.md v0.3` 應為 v0.4

**排除範圍（不算 stale）：**
- 任何 historical review report（CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND* / CODEX_WAVE67_REVIEW_REPORT / 等）紀錄當時版本
- 任何 historical starter（CODEX_WAVE7_PATCH_STARTER / CODEX_WAVE7_SKILLS_STARTER / 等）紀錄當時版本
- DECISIONS_LOG / POST_LOCK_PENDING 紀錄歷史升版時的版本
- 本 Round 10 starter 自身的 task scope 描述

**新 stale 標 R10-MI-X 若有。**

**維度 3：patch round 3 沒新 regression**

verify patch round 3 沒引入新 spec drift / 新硬錯 / 新 protected area 污染：

- `git diff HEAD~1 HEAD --name-only` 列 patch round 3 變動檔
- check_headers / check_paths / build_repo_index 是否維持 baseline
- LOCKED spec / scripts / registries / 27 模板 / 00_protocol/ / 6 wrapper / B55/B65/B8 starter / D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.10 / D054_DECISION_PACKAGE v0.2）確實沒被本輪動到

**維度 4：D-053 exception block 4 skill 一致性（R9-INFO-02 補完後檢查）**

verify 4 個 Phase B `/create-*` skill body D-050 子裁決 1 block 全部含 D-053 exception 對齊格式：

| Skill | D-050 子裁決 1 block 存在 | D-053 exception 雙 list |
|---|---|---|
| create-character v0.3 | ✓ (patch round 2 R8-MI-05) | ✓ |
| create-relationship v0.3 | ✓ (patch round 2 R8-MI-05) | ✓ |
| create-outline v0.3 | ✓ (patch round 2 R8-MI-05) | ✓ |
| create-detailed-outline v0.3 | ✓ (patch round 3 R9-INFO-02 新增) | ✓ |

create-world v0.1 屬 D-053 exception 對象（不是 caller），不需要此 block — 跳過 verify。

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
git log --oneline -10
git diff HEAD~1 HEAD --name-only 2>&1 | head -30
```

### Finding 分類

每個發現的 issue 分類：

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / Template 嚴重污染 / R9 finding 未關閉造成 framework 跑不通
- **MAJOR**：cross-doc 嚴重不一致 / R9-MI-01 ~ 05 任一 PARTIAL 或 NOT_RESOLVED / 大量新 stale reference
- **MINOR**：版本欄 / cross-ref 小不一致 / 維度 2 sweep 漏掉的 active stale
- **INFO**：觀察記錄但不阻 GO

### 決策準則

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + R9 6 finding 全 RESOLVED + 維度 2 sweep verification 全 PASS + 0 新 spec drift → 8th master 進 Phase C Wave 9
- **NEAR-GO（HOLD）**：0 CRITICAL + 1-2 MAJOR + 少數 MINOR → user 拍板 hard-limit accepted OR patch round 4 → Round 11 重審
- **NO-GO**：≥1 CRITICAL OR ≥3 MAJOR → 大幅 rollback / restructure 考量 → user 拍板

⚠ **單輪結束 default：** Round 10 本輪結果出來後**回 user 拍板**；不預設自動進 Round 11。

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts / registries
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 只新建 1 個 review report 檔

### 完成判定

✓ 4 維度全 verify + 結果寫入 review report
✓ 維度 1 對 R9 6 finding 逐項 RESOLVED / PARTIAL / NOT_RESOLVED 標記
✓ 維度 2 sweep verification grep 結果完整 + 任何剩餘 active stale 標 R10-MI-X
✓ 維度 4 D-053 exception block 4 skill 一致性 mapping 表
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / NEAR-GO / NO-GO）+ 對應 rationale
✓ `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 3 完成後 Round 10 重審結果  
優先級：高

# CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT

# 0. 文件目的
# 1. Round 10 摘要 + GO / NEAR-GO / NO-GO 判定
# 2. 維度 1：R9 6 finding 關閉完整性（6 row 表）
# 3. 維度 2：版本 cross-ref sweep 完整性（grep 結果 + 新 stale 表）
# 4. 維度 3：patch round 3 沒新 regression（diff 表 + finding）
# 5. 維度 4：D-053 exception block 4 skill 一致性（mapping 表）
# 6. 技術驗證結果（check_headers / check_paths / build_repo_index / git log / git diff 摘要）
# 7. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 8. 決策判定 + Rationale
# 9. 給 8th master 的建議（後續處理優先順序）
# 10. Cross-ref
```

### Go / Done 判定指引

- **DONE：** 上述驗收全 ✓ → review report 落地 → user commit/push → 回 8th master 接手讀
- **BLOCKED：** 任一驗收 ✗ 回 user

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Round 10 重審完成 → user commit/push → 回 8th master：

**分支 A（GO — 預期）：** 8th master 進 Phase C Wave 9 — 寫 3 個下游 starter（CODEX_C1_STARTER /scene-task 含 D-054 hybrid fallback + CODEX_C2_STARTER /dialogue-write + CODEX_C3_STARTER /qa 含 R8-INFO-06 00_k v0.1 5→8 報告對齊）

**分支 B（NEAR-GO / HOLD）：** user 拍板：
- **B.1 hard-limit accepted**（同 Round 7/8 模式；R10 殘留交 9th master cleanup queue）→ Phase C Wave 9
- **B.2 patch round 4**：8th master 開 inline patch round 4 處理 finding → user commit → 跑 Round 11 重審 → GO → Phase C Wave 9

**分支 C（NO-GO）：** user 拍板：rollback / 重審 / 其他路徑

---

# 3. 文件維護紀律

- 本檔是 8th master patch round 3 完成後 Round 10 重審 starter；完成後可 archive 進 `_design/archive/`
- ⚠ 紀律：本 starter 預設**單輪結束**；多輪重審需 user 明示拍板
- patch round 3 設計教訓（給未來 patch round 參考）：版本升版時務必同時 sweep 全 active cross-ref，避免 cascade

---

# 4. Cross-ref

- `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_STARTER.md` v0.1（Round 9 starter；模板參考）
- `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1（Round 9 NEAR-GO；本輪 R9 6 finding baseline）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO；歷史 baseline）
- `_design/DECISIONS_LOG.md` v2.0（D-054 拍板 + §6.12.2 / §6.16.2）
- `_design/POST_LOCK_PENDING.md` v0.10（NEW_REQ_13 RESOLVED + NEW_REQ_15 DEFERRED）
- `_design/D054_DECISION_PACKAGE.md` v0.2（拍板紀錄）
- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0
- 5 個 /create-* skill：world v0.1 / character v0.3 / relationship v0.3 / outline v0.3 / detailed-outline v0.3
- 3 個 review gate starter：B55 v0.4 / B65 v0.4 / B8 v0.5
- 3 個 phase_b review log：character v0.3 / outline v0.4 / review_log v0.5
- 4 個 Phase B 中文 wrapper（Cleanup round R7-MI-03 後）
- PHASE_B_COMPLETION_REPORT v1.2
- CODEX_B9_STARTER v0.4
