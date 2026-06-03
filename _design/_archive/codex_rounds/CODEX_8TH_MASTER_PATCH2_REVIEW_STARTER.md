狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 2 完成後 Round 9 重審 — Round 8 1 MAJOR + 5 MINOR cleanup verification + 全面 regression check  
優先級：高

# CODEX_8TH_MASTER_PATCH2_REVIEW_STARTER — Round 9 重審

# 0. 本檔用途

8th master Cleanup round 完成 → Round 8 重審 GO (1 MAJOR + 5 MINOR finding) → 8th master patch round 2 完成 → 本輪 Round 9 重審驗證 patch round 2 沒新 regression + R8 6 finding 全 RESOLVED。

**前置條件：** 8th master patch round 2 已完成所有預定變動（R8-MA-01 + R8-MI-01~05 共 6 finding cleanup；觸及 7 檔）+ user 已 commit/push。

**重審 GO →** 8th master 進 D-054 NEW_REQ_13 拍板包（per-scene 檔 convention 3 方案分析）→ Phase C Wave 9（3 個下游 starter）。

**重審 NEAR-GO →** user 拍板是否 hard-limit accepted（同 Round 7/8 模式）或開 patch round 3 → Round 10 重審 → GO。

**重審 NO-GO →** 大幅 rollback / restructure；user 拍板路徑。

⚠ **單輪結束 default 紀律延續：** Round 9 預設一輪結束；不預設自動進 Round 10。若 NEAR-GO/NO-GO，user 拍板分支。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第八輪 master patch round 2 完成後 Round 9 重審」— 對 patch round 2 期間的所有變動跑「R8 finding 關閉 + regression」雙重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1-8 重審模式（CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT v0.1 是 baseline；GO 含 R8-MA-01 + R8-MI-01~05 + R8-INFO 6 個；本輪 verify patch round 2 處理 MAJOR+MINOR 後狀態）
- 對應前置：8th master patch round 2 已完成 R8-MA-01 + R8-MI-01~05 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /create-* / /init-project 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✗ 不重審 Round 1-8 已 accepted 之 finding（R7 9 finding + R8 INFO 已 closed；不重議）
- ✗ 不下 D-054 結論（屬 user 拍板）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

8th master patch round 2 變動清單（給你做 review baseline — 7 檔）：

### R8-MA-01 修正（1 處）

1. `.claude/skills/create-detailed-outline/SKILL.md`：v0.1 → v0.2
   - line 76 prereq：「`05_b` chapter shells already exist from the outline flow」改「`05_plot/05_b_章節結構模板.md` template file exists (inherited from Template via `/init-project`; this skill will populate it with chapter shells `CH-*` in Stage 4 — outline flow does **not** write `05_b` per D-050 子裁決 2 CH 行)」
   - header version 升 v0.2 + 紀錄 patch 內容

### R8-MI 修正（6 處 → 觸及檔 6 個）

2. **R8-MI-01** — `_design/phase_b_outline_review_log.md`：v0.2 → v0.3
   - §1.2 表從 1 row（只列 05_a）擴為 4 row（05_a 必寫 + 05_c/d/e optional）對齊 B65 starter v0.4 step 0 D-052 雙模式 prompt 4 P-tagged 檔範圍
   - §1.2 註解段補新註（4 個檔皆 P-tagged scope；optional 觸發條件；實際升級 1-4 檔依 Instance 情況）
   - §1.3「不動」段：「其他 P 相關周邊檔（05_b/c/d/e 等模板）」改「`05_b_章節結構模板.md`（章節結構 — D-050 子裁決 2 後屬 /create-detailed-outline 階段 4 寫入 scope，CH-\* entities；非本 B.6.5 P-gate 範圍）」
   - 不動 list 加 S-\*-\* / 其他實體檔

3. **R8-MI-02** — `_design/CODEX_B8_REVIEW_GATE_STARTER.md`：header version 不升（屬 1-line comment 改）
   - line 134 CH grep 註解：「（含 05_b / 05_c / 05_d / 05_e）」改「（D-050 子裁決 2 後 CH 行限定 05_b；05_c/05_d/05_e 屬 P-scope 高層 placeholder 不歸 CH grep）」
   - 註：B8 starter version 仍 v0.5（R7-MA-03 cleanup 已升；本輪只改註解不升 version）

4. **R8-MI-03** — `_design/PHASE_B_COMPLETION_REPORT.md`：v1.1 header 維持
   - §9 Cross-ref 行：`CODEX_B8_REVIEW_GATE_STARTER.md v0.4` → `v0.5`
   - §9 Cross-ref 行：`phase_b_outline_review_log.md v0.2` → `v0.3`

5. **R8-MI-04** — `_design/phase_b_review_log.md`：v0.3 → v0.4
   - §4 Cross-ref 行 malformed path 修正：`.claude/skills/create-character / create-relationship / create-outline / create-detailed-outline /SKILL.md` v0.1 → 4 個分開的 cross-ref 行 + v0.2 對齊
   - phase_b_outline_review_log v0.2 → v0.3 對齊
   - header version 升 v0.4 + 紀錄 patch 內容

6. **R8-MI-05** — 3 個 /create-* skill body D-050 block 補 D-053 exception：
   - `.claude/skills/create-character/SKILL.md`：v0.2 → v0.3（header version + body line 344 D-050 子裁決 1 block 例外列表）
   - `.claude/skills/create-relationship/SKILL.md`：v0.2 → v0.3（同上 body line 356）
   - `.claude/skills/create-outline/SKILL.md`：v0.2 → v0.3（同上 body line 356）
   - 改後 wording：「例外（依 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）：/init-project（依 00_i §6 LOCKED 設計，限 00_b/00_c/00_d 三檔 Bootstrap 一次性微調）+ /create-world（D-053 加 exception；寫 00_b §1 §2 Instance-specific 類型語氣 / 髒話尺度作品專屬段；非 framework 變動）；**本 skill 不在例外範圍**」

### 8th master patch round 2 不動段（聲明）

- 不動 LOCKED spec：SPEC / INTEGRATION_CONTRACTS / DATA_FORMAT_SPEC / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA / ARCHITECTURE v1.6（Cleanup round 已升；本輪不再動）/ TASKS v1.9（同上）/ DECISIONS_LOG v1.9（同上）
- 不動 LOCKED registries：3 個 *.template.yaml
- 不動 scripts/*.py
- 不動 27 模板
- 不動 00_protocol/ 任何檔（含 00_i / 00_k）
- 不動 init-project SKILL.md / check-gaps / status / 6 個對應中文 wrapper
- 不動 create-world SKILL.md v0.1（R8 GO 後它的 description 已對齊 D-053；本輪只動 create-character/relationship/outline + create-detailed-outline）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 5 維度（精簡版 — 不重做 R8 已 verify 完的 7 維度全套）

**維度 1：R8 6 finding 關閉完整性（最優先）**

對 R8 報告 §10 的 1 MAJOR + 5 MINOR 逐項 verify 是否關閉：

| Finding | 預期關閉證據 |
|---|---|
| R8-MA-01 | `.claude/skills/create-detailed-outline/SKILL.md:76` 不再說「05_b chapter shells already exist from outline flow」；改為「`05_plot/05_b_章節結構模板.md` template file exists ...」；header version 升 v0.2 |
| R8-MI-01 | `phase_b_outline_review_log.md` §1.2 表擴為 4 row（05_a/c/d/e）；§1.3 不動段 wording 已對齊 D-050 子裁決 2；header version 升 v0.3 |
| R8-MI-02 | `CODEX_B8_REVIEW_GATE_STARTER.md` line 134 CH grep 註解已對齊 D-050（移除 05_c/d/e 誤列） |
| R8-MI-03 | `PHASE_B_COMPLETION_REPORT.md` §9 Cross-ref：B8 starter v0.4 → v0.5 + phase_b_outline_review_log v0.2 → v0.3 |
| R8-MI-04 | `phase_b_review_log.md` §4 Cross-ref skill 路徑無 malformed 空格 + 4 skill version v0.1 → v0.2 對齊 + header version 升 v0.4 |
| R8-MI-05 | 3 個 skill body（create-character/relationship/outline）D-050 子裁決 1 例外列表已含 /init-project + /create-world 兩 exception + 「本 skill 不在例外範圍」；header version 升 v0.3 |

對每筆 finding：標記 RESOLVED / PARTIAL / NOT_RESOLVED。

**維度 2：patch round 2 沒新 regression（核心）**

verify patch round 2 沒引入新 spec drift / 新 stale ref / 新 inconsistency：

- 比較 `git diff <prev_commit>..HEAD` 涉及的 7 檔 — 每檔變動是否限定 R8 finding scope
- check_headers / check_paths / build_repo_index 是否維持 baseline（0 ERROR / 254 Windows / 0）
- 7 檔 header version 升版是否對應 partial supersede 紀錄（patch round 2 屬「6 finding cleanup」性質，無新 D-NNN；屬「對齊既有 D-NNN backfill」）
- LOCKED spec / scripts / registries / 27 模板 / 00_protocol/ / 6 wrapper / create-world 確實沒被本輪動到（git diff name-only verify）

**維度 3：跨檔 cross-reference 一致性（patch round 2 引入的新 cross-ref）**

verify 以下新引入 cross-ref：

- create-character/relationship/outline body D-050 block 內提 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053 — verify兩 D-NNN 拍板紀錄存在
- create-detailed-outline line 76 提 D-050 子裁決 2 CH 行 — verify §6.12.2 內容對應
- phase_b_outline_review_log §1.2 註解提「對齊 B65 starter v0.4 步驟 0 D-052 雙模式 prompt」+ §1.3 提「D-050 子裁決 2 後屬 /create-detailed-outline 階段 4 寫入 scope」— verify wording 內部一致
- PHASE_B §9 Cross-ref B8 v0.5 + phase_b_outline_review_log v0.3 — verify 對應 starter 實際 version
- phase_b_review_log §4 Cross-ref 4 skill v0.2 — verify create-character/relationship/outline 實際 v0.3（不該還是 v0.2；patch round 2 升 v0.3 後 phase_b_review_log §4 應再對齊）— 此處可能殘留 stale；標 R9-MI-X 若有

**維度 4：5 個 /create-* skill chain consistency（patch round 2 後）**

5 個 /create-* skill 整體 chain：

- create-world v0.1（不動）
- create-character v0.3（R8-MI-05 cleanup 升）
- create-relationship v0.3（R8-MI-05 cleanup 升）
- create-outline v0.3（R8-MI-05 cleanup 升）
- create-detailed-outline v0.2（R8-MA-01 cleanup 升）
- init-project v0.3（不動）

verify：
- 5 SKILL.md 都含 D-050 子裁決 1 + 子裁決 2 明示句
- 4 個 /create-* skill（C/R/P/CH）body D-050 block 例外列表都已含 /init-project + /create-world 兩 exception（create-world 自己不需要 — 是 D-053 exception 對象不是 caller）
- create-detailed-outline body D-050 block 是否也補 D-053 exception（patch round 2 scope 未明示要動，但維度 1 R8-MI-05 列 3 skill 不含 create-detailed-outline；reviewer 可標 R9-INFO 觀察「為什麼 create-detailed-outline body D-050 block 沒同步補 D-053 exception」）
- 5 SKILL.md header version 跟 frontmatter description 一致（patch round 2 後）

**維度 5：未解決 stale reference 偵測（patch round 2 後新 stale 檢測）**

grep 以下 stale pattern（重點 patch round 2 引入或殘留的 stale）：

- 任何檔內提「create-character v0.2」/「create-relationship v0.2」/「create-outline v0.2」應改 v0.3（除非歷史紀錄）— patch round 2 升 v0.3 後其他檔 cross-ref 是否對齊
- 任何檔內提「create-detailed-outline v0.1」應改 v0.2
- 任何 cross-ref 提「phase_b_outline_review_log v0.2」應改「v0.3」
- 任何 cross-ref 提「phase_b_review_log v0.3」應改「v0.4」
- 任何 cross-ref 提「B8 starter v0.4」應改「v0.5」（PHASE_B 已修；其他位置有無漏？）
- create-detailed-outline body D-050 block 是否仍說「唯一例外是 /init-project」（patch round 2 沒明示要動，但維度 4 已標）

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

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / Template 嚴重污染 / R8 finding 未關閉造成 framework 跑不通 / patch round 2 引入新 spec 衝突
- **MAJOR**：cross-doc 嚴重不一致 / R8-MA-01 PARTIAL 或 NOT_RESOLVED / 大量新 stale reference
- **MINOR**：版本欄 / cross-ref 小不一致 / 少數新 stale wording / R8-MI 任一未關閉
- **INFO**：觀察記錄但不阻 GO（例：create-detailed-outline body D-050 block 未同步補 D-053 exception；屬本輪 patch round 2 故意縮減）

### 決策準則

- **GO（PASS）**：0 CRITICAL + ≤2 MAJOR + R8 6 finding 全 RESOLVED + 0 新 spec drift → 8th master 進 D-054 拍板 + Phase C Wave 9
- **NEAR-GO（HOLD）**：0 CRITICAL + 3-5 MAJOR + 多 MINOR → user 拍板 hard-limit accepted（同 Round 7/8 模式）OR patch round 3 → Round 10 重審
- **NO-GO**：≥1 CRITICAL OR ≥6 MAJOR → 大幅 rollback / restructure 考量 → user 拍板

⚠ **單輪結束 default：** Round 9 本輪結果出來後**回 user 拍板**；不預設自動進 Round 10。

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts / registries
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 不下 D-054 結論（屬 user 拍板）
- 只新建 1 個 review report 檔

### 完成判定

✓ 5 維度全 verify + 結果寫入 review report
✓ 維度 1 對 R8 6 finding 逐項 RESOLVED / PARTIAL / NOT_RESOLVED 標記
✓ 維度 2 patch round 2 沒新 regression 確認
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / NEAR-GO / NO-GO）+ 對應 rationale
✓ `_design/CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT.md` v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 2 完成後 Round 9 重審結果  
優先級：高

# CODEX_8TH_MASTER_PATCH2_REVIEW_REPORT

# 0. 文件目的
# 1. Round 9 摘要 + GO / NEAR-GO / NO-GO 判定
# 2. 維度 1：R8 6 finding 關閉完整性（6 row 表）
# 3. 維度 2：patch round 2 沒新 regression（diff 表 + finding）
# 4. 維度 3：跨檔 cross-reference 一致性（finding 表）
# 5. 維度 4：5 /create-* skill chain consistency
# 6. 維度 5：未解決 stale reference 偵測（grep 結果 + finding 表）
# 7. 技術驗證結果（check_headers / check_paths / build_repo_index / git log / git diff 摘要）
# 8. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 9. 決策判定 + Rationale
# 10. 給 8th master 的建議（後續處理優先順序）
# 11. Cross-ref
```

### Go / Done 判定指引

- **DONE：** 上述驗收全 ✓ → review report 落地 → user commit/push → 回 8th master 接手讀
- **BLOCKED：** 任一驗收 ✗ 回 user

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Round 9 重審完成 → user commit/push → 回 8th master：

**分支 A（GO）：** 8th master 寫 D-054 NEW_REQ_13 拍板包（per-scene 檔 convention 3 方案分析 + 推薦選 1 Hybrid）→ user 拍板 → Phase C Wave 9（3 個下游 starter）

**分支 B（NEAR-GO / HOLD）：** user 拍板：
- **B.1 hard-limit accepted**（同 Round 7/8 模式）：殘留 finding 紀錄入 9th master cleanup queue → 8th master 直接進 D-054 拍板包 + Phase C Wave 9
- **B.2 patch round 3**：8th master 開 inline patch round 3 處理 finding → user commit → 跑 Round 10 重審 → GO → 進 D-054

**分支 C（NO-GO）：** user 拍板：rollback / 重審 / 其他路徑

---

# 3. 文件維護紀律

- 本檔是 8th master patch round 2 完成後 Round 9 重審 starter；完成後可 archive 進 `_design/archive/`
- 對應 review report 也屬 8th master 收尾事實紀錄；不刪除
- ⚠ 紀律：本 starter 預設**單輪結束**；多輪重審需 user 明示拍板

---

# 4. Cross-ref

- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_STARTER.md` v0.1（Round 8 starter；本輪 starter 模板參考）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（Round 8 GO；本輪 R8 6 finding baseline）
- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0
- `_design/DECISIONS_LOG.md` v1.9（D-050 / D-051 / D-052 / D-053 拍板權威）
- `_design/POST_LOCK_PENDING.md` v0.9
- `_design/TASKS.md` v1.9（Cleanup round R7-MA-01 後）
- `_design/ARCHITECTURE.md` v1.6（Cleanup round R7-MA-02 後）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.1（patch round 2 R8-MI-03 後）
- 3 個 review gate starter v0.4/v0.4/v0.5（Cleanup round R7-MA-03 後）
- 3 個 phase_b review_log（patch round 2 後：character v0.2 / outline v0.3 / review_log v0.4）
- 4 個 Phase B 中文 wrapper（Cleanup round R7-MI-03 後）
- 5 個 /create-* skill（patch round 2 後：world v0.1 / character v0.3 / relationship v0.3 / outline v0.3 / detailed-outline v0.2）
