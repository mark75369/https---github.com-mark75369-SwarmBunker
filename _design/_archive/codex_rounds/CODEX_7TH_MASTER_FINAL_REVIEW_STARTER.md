狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：第七輪 master 收尾前 CODEX 全面重審 — Phase B Wave 7+8 全變動 + D-049/050/051/052 落地完整性 + 跨檔一致性檢查  
優先級：高

# CODEX_7TH_MASTER_FINAL_REVIEW_STARTER — 第七輪 master 收尾全面重審

# 0. 本檔用途

第七輪 master 對話接手 Phase B Wave 7+8 + 期間發現 2 個設計缺陷（D-049 #6 over-broad / B.5.5+B.6.5+B.8 manual upgrade 過嚴）+ 處理 4 個 deferred 項（NEW_REQ_10/11/12/13/14；NEW_REQ_11 是 6th master 平行加的）。在 8th master 對話接手 Phase C 之前，對所有變動跑**全面重審 checkpoint**。

**對齊傳統：** 同 Wave 6+7 review checkpoint 模式（6th master 寫 `CODEX_WAVE67_REVIEW_STARTER` 給 7th master 跑 → 抓出 D-050 邊界 bug → 觸發 Wave 7 patch round）。本輪重審類似 — 用 CODEX 抓任何 7th master 期間累積的 inconsistency / stale reference / 邊界破壞。

**前置條件：** 第七輪 master 已完成所有預定變動 + push（含 D-052 patch round + PHASE_B_COMPLETION_REPORT v1.0 §6 補入 + NEW_REQ_14）。

**重審 PASS（GO）→** 寫 `HANDOFF_TO_8TH_MASTER.md`（接 Phase C — /scene-task / /dialogue-write / /qa）。

**重審 HOLD / NO-GO →** master inline patch round 處理 finding → 重審 → GO → handoff。

⚠ **新慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- 不涉 Instance-only path（本重審 scope 全 Template repo 內）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第七輪 master 對話收尾前全面重審」— 對第七輪 master 在 Phase B Wave 7+8 期間累積的所有變動跑 6 維度檢查，產出 GO / HOLD / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Wave 6+7 review checkpoint 模式（CODEX_WAVE67_REVIEW_REPORT v0.1 已存在參考）
- 對應前置：第七輪 master 接手後的所有 inline patch + new file + spec change

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /create-* / /init-project 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

第七輪 master 對話期間累積變動清單（給你做 review baseline）：

### 設計層 spec 變動
1. `_design/DECISIONS_LOG.md`：v1.5 → v1.8（新增 §6.13 D-051 / §6.15 D-052 + footer history append；§6.14 是 6th master 平行加的翻譯工具提案）
2. `_design/POST_LOCK_PENDING.md`：v0.4 → v0.8（NEW_REQ_10 fence convention + NEW_REQ_12 D-050 vs /create-world 00_b 衝突 + NEW_REQ_13 per-scene 檔 + NEW_REQ_14 §6 補入 AI-assisted；NEW_REQ_11 翻譯工具是 6th master 平行加）
3. `_design/TASKS.md`：v1.8 → v1.9 partial supersede §A.10 + §B.5.5 + §B.6.5 + §B.8「禁止」段加 D-052 exception clause

### Protocol 層變動
4. `00_protocol/00_i_專案初始化協議.md`：v0.2 → v0.3 partial supersede（§2 條件 #6 移除 + 改為 D-051 紀錄；§2 註釋更新）

### Skill 層變動
5. `.claude/skills/init-project/SKILL.md`：v0.2 → v0.3 master inline patch（line 56 防線 #6 bullet 改 D-051 紀錄 + line 72-83 error block 改 D-051 supersede HTML comment）

### Starter 層變動
6. `_design/CODEX_B55_REVIEW_GATE_STARTER.md`：v0.1 → v0.2（D-052 雙模式流程 supersede note）
7. `_design/CODEX_B65_REVIEW_GATE_STARTER.md`：v0.1 → v0.2（D-052 雙模式流程 supersede note）
8. `_design/CODEX_B8_REVIEW_GATE_STARTER.md`：v0.1 → v0.2（D-050 對齊）→ v0.3（D-052 雙模式流程）
9. `_design/CODEX_B7_STARTER.md`：v0.1 → v0.2（D-050 對齊 supersede note）
10. `_design/CODEX_B9_STARTER.md`：v0.1 → v0.2（D-050 對齊 supersede note）

### 新建檔
11. `_design/phase_b_character_review_log.md` v0.1
12. `_design/phase_b_outline_review_log.md` v0.1
13. `_design/phase_b_review_log.md` v0.1
14. `_design/CODEX_B7_STARTER.md`（本身是新建 — Wave 8 起手）
15. `_design/CODEX_B8_REVIEW_GATE_STARTER.md`（同上）
16. `_design/CODEX_B9_STARTER.md`（同上）
17. `_design/CODEX_B55_REVIEW_GATE_STARTER.md`（同上 — Wave 7 起手）
18. `_design/CODEX_B65_REVIEW_GATE_STARTER.md`（同上）
19. `_design/PHASE_B_COMPLETION_REPORT.md` v1.0（B.9 CODEX 產出 + 第七輪 master §6 補入）

### 6th master 平行加（不在本重審 scope 但需確認沒衝突）
20. `_design/CODEX_WAVE7_PATCH_STARTER.md`（給 7th master 跑 Wave 7 patch — 已跑完）
21. `_design/CODEX_WAVE67_REVIEW_REPORT.md`（Wave 6+7 review 結果）
22. `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md`（翻譯工具分支提案）
23. 5 個 /create-* SKILL.md：create-character / create-relationship / create-outline v0.1 → v0.2（Wave 7 patch round 對齊 D-050；7th master 期間 verify 過但不改）；create-world / init-project（後者 7th master 改過 v0.3）
24. `.claude/skills/create-detailed-outline/SKILL.md` v0.1（B.7 CODEX 對話內產出；7th master 期間 verify 過 + 確認 D-050 對齊）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 6 維度

**維度 1：D-NNN 落地完整性**

對 D-049 / D-050 / D-051 / D-052 四個拍板，逐項 verify 落地內容：

對 D-049：
- 00_i §2 條件 #5（.template_root marker）+ 條件 #6（雙重檢測）是否仍存在 → 條件 #6 應已被 D-051 supersede 移除
- 跟 D-051 supersede 是否對齊（00_i v0.3 應該不含舊 #6 error block）

對 D-050：
- DECISIONS_LOG §6.12.2 子裁決 1 + 子裁決 2 表內容
- 5 個 /create-* SKILL.md 是否對齊 D-050 子裁決 2 寫檔目錄表 + 都有「## 邊界」段含 D-050 明示句
- 5 個 /create-* SKILL.md frontmatter description 是否提 D-050

對 D-051：
- 00_i v0.3 + init-project SKILL.md v0.3 是否實際移除防線 #6 block + 都標明 D-051 supersede 紀錄
- DECISIONS_LOG §6.13 D-051 拍板紀錄完整性（5 欄：日期/議題/決策/影響/Owner）

對 D-052：
- TASKS v1.9 §A.10 + §B.5.5 + §B.6.5 + §B.8「禁止」段都加 D-052 exception clause
- 3 個 review gate starter（B55 / B65 / B8）都有 D-052 supersede note + 雙模式流程描述
- DECISIONS_LOG §6.15 D-052 拍板紀錄完整性

**維度 2：跨檔 cross-reference 一致性**

verify 以下 mapping：
- DECISIONS_LOG §6.15.3 升版文件清單 vs 實際各 starter / spec header 的 version 是否對齊
- DECISIONS_LOG §6.14.7 升版文件清單（6th master）vs 實際 vs 對齊
- TASKS §A.10 / §B.5.5 / §B.6.5 / §B.8 「禁止」段引用 DECISIONS_LOG §6.15.2 D-052 — version 標 v1.8 是否正確
- POST_LOCK_PENDING NEW_REQ_10/12/13/14 引用 DECISIONS_LOG / starter / spec — 版本對齊
- 4 個 review_log（phase_a / phase_b_character / phase_b_outline / phase_b）內 Cross-ref 段引用是否準確
- 3 個 review gate starter Cross-ref 段是否引用最新 spec 版本（不該還有 "TASKS v1.8" 之類 stale ref）
- PHASE_B_COMPLETION_REPORT v1.0 §9 Cross-ref 對齊
- 6 個 starter（B7/B8/B9/B55/B65/Wave7_patch）的「必讀文件」/「Cross-ref」段沒有指向不存在或廢檔

**維度 3：LOCKED 文件動過的合規性**

verify 以下 LOCKED 檔變動都有 D-NNN 拍板背書 + partial supersede 紀錄完整：
- TASKS v1.8 → v1.9（partial supersede 4 處「禁止」段）— D-052 拍板背書 ✓
- 00_i v0.2 → v0.3（partial supersede §2 條件 #6）— D-051 拍板背書 ✓
- 任何其他 LOCKED 檔（_design/SPEC.md / _design/INTEGRATION_CONTRACTS.md / _design/ARCHITECTURE.md / _design/UPSTREAM_DOWNSTREAM_SPEC.md / _design/UX_SPEC.md / _design/DATA_FORMAT_SPEC.md / _design/REQUIREMENTS_LOCK.md / _design/L3_EXPORT_PROMPT_SCHEMA.md）— 應該**不動**
- registries 三 yaml.template（_design/registries/*.template.yaml）— 應該**不動**
- scripts/*.py — 應該**不動**
- 既有 27 模板（01_world/*.md / 02_vocabulary/*.md / 03_characters/*.md 等）— 應該**不動**

**維度 4：Template vs Instance 邊界污染檢查**

verify Template repo（D:\劇本開發工具）內**沒有混進 Instance-specific data**：
- grep Template 內所有 _design/ + 00_protocol/ + .claude/skills/ + 27 模板，搜「林思羽」/「陳則安」/「情緒感知體質」/「my-test-instance」/ 任何具體作品角色名（**這些屬 testing Instance 端內容，不該在 Template**）
- PHASE_B_COMPLETION_REPORT §6 是否採 generic 版本（Option A — 不嵌入 specific test 角色名 / 世界觀 / 主線細節）
- 任何 review_log Template 骨架是否仍是 placeholder（不該有 actual Instance entry — Instance entry 該在 Instance repo 內 review_log）
- 任何 starter / spec 內是否殘留 specific test data reference

**維度 5：5 個 /create-\* skill chain consistency**

5 個 /create-* skill（含 init-project）對齊檢查：
- 5 SKILL.md header version 一致性
- 5 SKILL.md description 是否提 D-047 / D-050 + 對應 protocol vXXX
- 5 SKILL.md frontmatter rule 一致性（entities / depends_on / weight 規範描述）
- 5 SKILL.md 「## 邊界」段是否都含 D-050 子裁決 1 + 子裁決 2 明示句
- 5 個對應 protocol（00_e / 00_f / 00_g / 00_h / 00_l）v0.2 + 00_i v0.3 對齊
- 5 個對應中文 wrapper（建立世界觀 / 建立角色 / 建立關係 / 建立大綱 / 建立細綱）是否仍極簡指向英文主檔（不該加邏輯）
- create-character / create-relationship / create-outline 是否仍有 D-049 #6 dead code check（DECISIONS_LOG §6.13.2 紀錄為「dead code 無害；future cleanup」— verify 確實 dead code 不阻 /init-project + 不影響 other skill 行為）

**維度 6：未解決 stale reference 偵測**

grep 以下 stale pattern：
- 任何檔內提「TASKS v1.8」應改為 v1.9（除非 v1.8 是歷史紀錄不該改）
- 任何檔內提「DECISIONS_LOG v1.6」/「v1.7」應改為 v1.8（除非歷史紀錄）
- 任何檔內提「POST_LOCK_PENDING v0.7」應改為 v0.8（除非歷史紀錄）
- 任何 starter 內提「§10.11 / §10.12」應改為「§10.7 / §10.8」（B.7 starter v0.2 supersede note 已標註 — 但內文若沒對齊算 stale）
- 任何 SKILL.md 提「D-049 第二道防線」應改為「D-051 supersede D-049 第二道防線」標註
- 任何文檔提舊 spec 版本（pre-v0.2 protocol / pre-v0.x starter 等）

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
```

```bash
git log --oneline -20
```

### Finding 分類

每個發現的 issue 分類：

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / Template 嚴重污染（specific test data） / D-NNN 落地不完整造成 framework 跑不通
- **MAJOR**：cross-doc 嚴重不一致 / 5 skill chain 嚴重斷裂 / 大量 stale reference
- **MINOR**：版本欄 / cross-ref 小不一致 / 少數 stale wording
- **INFO**：觀察記錄但不阻 GO

### 決策準則

- **GO（PASS）**：0 CRITICAL + ≤2 MAJOR + 任意 MINOR/INFO → 7th master 可直接寫 HANDOFF_TO_8TH_MASTER
- **HOLD（NEAR-GO）**：0 CRITICAL + 3-5 MAJOR + 多 MINOR → master patch round 處理 MAJOR 後重審 → GO
- **NO-GO**：≥1 CRITICAL OR ≥6 MAJOR → 大幅 rollback / restructure 考量 → 不可直接 handoff

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 只新建 1 個 review report 檔

### 完成判定

✓ 6 維度全 verify + 結果寫入 review report
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / HOLD / NO-GO）+ 對應 rationale
✓ _design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT.md v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：第七輪 master 收尾全面重審結果 — Phase B Wave 7+8 全變動  
優先級：高

# CODEX_7TH_MASTER_FINAL_REVIEW_REPORT

# 0. 文件目的
# 1. 重審摘要 + GO / HOLD / NO-GO 判定
# 2. 維度 1：D-NNN 落地完整性（4 D-NNN 各自檢查表）
# 3. 維度 2：跨檔 cross-reference 一致性（finding 表）
# 4. 維度 3：LOCKED 文件動過合規性（finding 表）
# 5. 維度 4：Template vs Instance 邊界污染（finding 表 + grep 結果）
# 6. 維度 5：5 skill chain consistency（mapping 表）
# 7. 維度 6：未解決 stale reference（grep 結果 + finding 表）
# 8. 技術驗證結果（check_headers / check_paths / build_repo_index / git log 摘要）
# 9. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 10. 決策判定 + Rationale
# 11. 給 7th master 的建議（後續處理優先順序）
# 12. Cross-ref
```

### Go / Done 判定指引

- **DONE：** A/B/C 驗收全 ✓ → review report 落地 → master 接手讀
- **BLOCKED：** 任一驗收 ✗ 回 master

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX 重審完成 → user commit/push → 回 master：

**分支 A（GO）：** master 寫 HANDOFF_TO_8TH_MASTER.md（內含「重審 GO」紀錄）→ 第七輪 master 對話結束

**分支 B（HOLD / NO-GO）：** master inline patch round 處理 finding → user 跑 round 2 重審（重貼此 starter）→ GO → handoff

---

# 3. 文件維護紀律

- 本檔是第七輪 master 收尾全面重審 starter；完成後可 archive 進 `_design/archive/`
- 對應 review report 也屬 7th master 收尾事實紀錄；不刪除
- 未來 8th / 9th master 收尾前若需類似重審，可採同 starter pattern 寫對應 starter

---

# 4. Cross-ref

- `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope）
- `_design/CODEX_WAVE67_REVIEW_REPORT.md`（6th master 寫的 Wave 6+7 review；本重審的模板參考）
- `_design/CODEX_WAVE7_PATCH_STARTER.md`（6th master 寫的 Wave 7 patch starter；對齊紀律參考）
- `_design/DECISIONS_LOG.md` v1.8（D-049 / D-050 / D-051 / D-052 拍板權威）
- `_design/POST_LOCK_PENDING.md` v0.8（NEW_REQ_10/11/12/13/14）
- `_design/TASKS.md` v1.9
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.0
- `00_protocol/00_i_專案初始化協議.md` v0.3
- `.claude/skills/init-project/SKILL.md` v0.3
- 5 個 /create-\* SKILL.md（v0.1 / v0.2 D-050 對齊版）
- 6 個 starter（B55 v0.2 / B65 v0.2 / B7 v0.2 / B8 v0.3 / B9 v0.2 / Wave7_patch v0.1）
- 4 個 review_log（phase_a v0.1 / phase_b_character v0.1 / phase_b_outline v0.1 / phase_b v0.1）
