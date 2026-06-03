狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 4 完成後 Round 12 重審 — Round 11 4 finding closure + 無新 regression；單輪結束 default  
優先級：高

# CODEX_8TH_MASTER_PATCH4_REVIEW_STARTER — Round 12 重審

# 0. 本檔用途

第八輪 master 流程進展：Cleanup round → Round 8 GO → patch round 2 → Round 9 NEAR-GO → D-054 拍板 → patch round 3 → Round 10 NEAR-GO → Phase C Wave 9-10 → C4 patch → Wave 11 BLOCKED → mode_tag patch → Wave 11 PASS → Milestone 3 達成 → HANDOFF_TO_9TH_MASTER → Round 11 final review NO-GO（1 CRITICAL + 1 MAJOR + 2 MINOR）→ **patch round 4 完成（4 finding 修補）** → **本輪 Round 12 重審驗證 patch round 4 沒新 regression + R11 4 finding 全 RESOLVED**。

**前置條件：** 8th master patch round 4 已完成所有預定變動（R11-CR-01 + R11-MA-01 + R11-MI-01 + R11-MI-02 共 4 finding cleanup；觸及 4 檔）+ user 已 commit/push。

**重審 GO →** 第八輪 master 對話真正收尾結束 → 9th master 對話啟動接 Phase D

**重審 NEAR-GO →** user 拍板 hard-limit accepted（殘留 finding 入 9th master cleanup queue NEW_REQ_19）OR 8th master 開緊急 patch round 5 → Round 13 重審

**重審 NO-GO →** 大幅 rollback / restructure 考量；user 拍板路徑

⚠ **單輪結束 default 紀律延續：** Round 12 預設一輪結束；不預設自動進 Round 13。

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第八輪 master patch round 4 完成後 Round 12 重審」— 對 patch round 4 期間的所有變動跑「R11 4 finding 關閉 + 無新 regression」雙重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1-11 重審模式（CODEX_8TH_MASTER_FINAL_REVIEW_REPORT v0.1 是 baseline — 4 finding 含 1 CRITICAL + 1 MAJOR + 2 MINOR；本輪 verify patch round 4 處理 4 finding 後狀態）
- 對應前置：8th master patch round 4 已完成 R11-CR-01 + R11-MA-01 + R11-MI-01 + R11-MI-02 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 skill 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✗ 不重審 Round 8/9/10/Wave 11/Round 11 已 accepted 之 finding（已 closed / hard-limit accept / NEW_REQ_19 紀錄；不重議）
- ✗ 不下 D-054 結論（已 RESOLVED via D-054 in DECISIONS_LOG v2.0 §6.17）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_8TH_MASTER_PATCH4_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

8th master patch round 4 變動清單（給你做 review baseline — 4 檔）：

### R11-CR-01 修補（1 檔）

`.claude/skills/create-character/SKILL.md` v0.3 → v0.4
- 修補 line 371 之後因 sandbox cache stale + bash python write 截斷的尾段 wording
- 補回「Each error must include: What/Where/Why/下一步 4 欄」+「For multiple errors, summarize the count first...」標準 wording
- 對齊既有 create-relationship/create-outline v0.3 §錯誤呈現規則段
- header version v0.3 → v0.4 紀錄 root cause（sandbox cache stale + bash python write 風險；patch round 2 R8-MI-05 時誤觸）

### R11-MA-01 修補（1 檔）

`09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.1 → v0.2
- 移除我 C4 starter scope creep 加的第 4 面向「跨場伏筆對齊 FORESHADOW_ALIGNMENT」整段（lines 145-156）
- 移除 §總結判定 內「- 伏筆對齊：<...>」line
- 移除「## 4. 跨場伏筆對齊」section + 重新編號 §5 → §4 修改建議 / §6 → §5 與其他 QA 的協調
- 對齊 UD §3.9 三 facet（跨場聲線漂移 / 跨場資訊洩漏 / 跨場節奏 arc）— 不擴張 UD spec
- header version v0.1 → v0.2 紀錄 root cause（master C4 starter scope creep；未授權 UD §3.9 擴張）

### R11-MI-01 修補（1 檔）

`_design/CODEX_8TH_MASTER_FINAL_REVIEW_STARTER.md` v0.1（line 231 wording fix；不升 version）
- 維度 6 段「4 個 trigger 條件 A/B/C/D」改為「3 個 cleanup trigger 條件（A 9th master Phase D 啟動時 / B NEW_REQ_16 lint script 實作後 / C 封版前最終 cleanup round）」
- 補註：D-054 hybrid 迭代追蹤的 4 個 trigger A/B/C/D（A 使用規模 / B split 頻率 / C 並行需求 / D merge conflict）屬 NEW_REQ_15 D-054 future iteration evaluation；本維度 verify NEW_REQ_15 含此 4 trigger 屬維度 2 D-054 落地完整性範圍

### R11-MI-02 修補（1 檔）

`_design/HANDOFF_TO_9TH_MASTER.md` v1.0（line 395 wording fix；不升 version）
- 「`D:\my-test-instance`」改「`<instance_root>/`（user 之前 M2 testing 用的本地 Instance repo 即可）」
- 對齊 NEW_REQ_10 紀律（Instance-only concrete path 不寫死；用 `<instance_root>/` generic 前綴）

### 8th master patch round 4 不動段（聲明）

- 不動 LOCKED spec：SPEC / INTEGRATION_CONTRACTS / DATA_FORMAT_SPEC / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA / ARCHITECTURE v1.6 / TASKS v1.9
- 不動 D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.13 / D054_DECISION_PACKAGE v0.2）
- 不動 LOCKED registries：3 個 *.template.yaml
- 不動 scripts/*.py
- 不動 26 既有模板（09_i 是 C4 patch round 新建；本輪只動 09_i v0.1 → v0.2）
- 不動 00_protocol/ 任何檔（含 00_k v0.1 stale R8-INFO-06）
- 不動 init-project SKILL.md / check-gaps / status / 6 個對應中文 wrapper
- 不動 Phase A / Phase B 既有 SKILL.md（除 create-character v0.3 → v0.4 修 truncation）
- 不動 Phase C 3 個下游 SKILL.md（scene-task / dialogue-write v0.2 / qa）+ 3 中文 wrapper
- 不動 4 個 Phase C Wave 9-10 starter（C1/C2/C3/C4）
- 不動 PHASE_C_COMPLETION_REPORT v1.0
- 不動 Round 8/9/10/11 review report（含 CODEX_8TH_MASTER_FINAL_REVIEW_REPORT v0.1）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_8TH_MASTER_PATCH4_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 3 維度（精簡版 — Round 11 已 verify 全 13 work items；本輪只 verify patch round 4 closure）

**維度 1：R11 4 finding 關閉完整性（最優先）**

對 R11 報告 §11 4 finding 逐項 verify 是否關閉：

| Finding | 預期關閉證據 |
|---|---|
| R11-CR-01 | `.claude/skills/create-character/SKILL.md:7` header 升 v0.4；`:368-380` 含完整「Each error must include: What/Where/Why/下一步 4 欄」+「For multiple errors...」尾段；不再以「prerequisit」mid-word 截斷 |
| R11-MA-01 | `09_quality_assurance/09_i_跨場一致性檢查模板.md:2` header 升 v0.2；無「面向 4」/「FORESHADOW_ALIGNMENT」/「跨場伏筆對齊」段（除 ## 9_i scope 段內可能提及 05_e 作為 INFO_LEAK 之輔助資料源 — 屬合法 reference 非 facet）；§總結判定無「伏筆對齊」line；§4 改為「修改建議」；§5 改為「與其他 QA 的協調」；對齊 UD §3.9 三 facet |
| R11-MI-01 | `_design/CODEX_8TH_MASTER_FINAL_REVIEW_STARTER.md` 維度 6 段不再寫「4 個 trigger 條件 A/B/C/D」；改寫「3 個 cleanup trigger 條件」+ 註明 4 個 D-054 迭代 trigger 屬 NEW_REQ_15 範圍 |
| R11-MI-02 | `_design/HANDOFF_TO_9TH_MASTER.md` line 395（或附近）不再含 concrete path `D:\my-test-instance`；改為 `<instance_root>/` generic wording |

對每筆 finding：標記 RESOLVED / PARTIAL / NOT_RESOLVED。

**維度 2：patch round 4 沒新 regression（核心）**

verify patch round 4 沒引入新 spec drift / 新硬錯 / 新 protected area 污染：

- `git diff HEAD~1 HEAD --name-only`（或 `HEAD~N..HEAD` 看 N=1 或 N=2 看包不包 patch round 4 commit）列出 patch round 4 變動檔（預期 4 檔；其他不動）
- check_headers / check_paths / build_repo_index 是否維持 baseline（baseline 範圍：check_headers 0 ERROR / check_paths sandbox baseline 252 ± 0 / build_repo_index 0 ERROR）
- LOCKED spec / scripts / registries / 27 既有模板 / 00_protocol/ / 既有 SKILL.md（除 create-character）/ D-054 落地檔 / Round 8-11 review report / PHASE_C_COMPLETION_REPORT 確實沒被本輪動到
- create-character SKILL.md v0.4 內容對齊（line 1-370 同 v0.3；line 371-380 為修補新增 wording；無其他語義變動）
- 09_i v0.2 內容對齊（除移除 4th facet 三處 + 重新編號 + header note；其他內容對 UD §3.9 三 facet 保持完整）

**維度 3：R11-CR-01 truncation root cause 紀錄 + cascade pattern 教訓**

verify create-character v0.4 header note 含 truncation root cause（sandbox cache stale + bash python write 風險）— 為未來 master 對話提供教訓（同 mode_tag typo 教訓 / cascade pattern 教訓並列）。

verify 09_i v0.2 header note 含 master starter scope creep root cause（C4 starter 自行加第 4 facet；未授權 UD §3.9 擴張）— 為未來 master 對話提供教訓。

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
git log --oneline -5
git diff HEAD~1 HEAD --name-only 2>&1 | head -10
```

### Finding 分類

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / runtime skill 檔截斷未修補 / R11 4 finding 任一 NOT_RESOLVED
- **MAJOR**：cross-doc 嚴重不一致 / R11 finding PARTIAL / 新 spec 衝突
- **MINOR**：版本欄 / cross-ref 小不一致 / 少數新 stale wording
- **INFO**：觀察記錄但不阻 GO

### 決策準則

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + R11 4 finding 全 RESOLVED + 0 新 spec drift → **第八輪 master 對話真正收尾結束** → 9th master 對話可啟動接 Phase D
- **NEAR-GO（HOLD）**：0 CRITICAL + 1-2 MAJOR + 少數 MINOR → user 拍板 hard-limit accepted OR patch round 5 → Round 13 重審
- **NO-GO**：≥1 CRITICAL OR ≥3 MAJOR → 大幅 rollback / restructure 考量 → user 拍板

⚠ **單輪結束 default：** Round 12 本輪結果出來後**回 user 拍板**；不預設自動進 Round 13。

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts / registries
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 只新建 1 個 review report 檔

### 完成判定

✓ 3 維度全 verify + 結果寫入 review report
✓ 維度 1 對 R11 4 finding 逐項 RESOLVED / PARTIAL / NOT_RESOLVED 標記
✓ 維度 2 patch round 4 沒新 regression 確認
✓ 維度 3 truncation root cause + master starter scope creep 教訓紀錄 verify
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / NEAR-GO / NO-GO）+ 對應 rationale
✓ `_design/CODEX_8TH_MASTER_PATCH4_REVIEW_REPORT.md` v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master patch round 4 完成後 Round 12 重審結果  
優先級：高

# CODEX_8TH_MASTER_PATCH4_REVIEW_REPORT

# 0. 文件目的
# 1. Round 12 摘要 + GO / NEAR-GO / NO-GO 判定
# 2. 維度 1：R11 4 finding 關閉完整性（4 row 表）
# 3. 維度 2：patch round 4 沒新 regression（diff 表 + finding）
# 4. 維度 3：truncation root cause + master starter scope creep 教訓紀錄
# 5. 技術驗證結果（check_headers / check_paths / build_repo_index / git log / git diff 摘要）
# 6. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 7. 決策判定 + Rationale
# 8. 給第八輪 master 收尾的建議
# 9. Cross-ref
```

### Go / Done 判定指引

- **DONE：** 上述驗收全 ✓ → review report 落地 → user commit/push → 回 user 拍板 GO / NEAR-GO / NO-GO 分支
- **BLOCKED：** 任一驗收 ✗ 回 user

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Round 12 重審完成 → user commit/push → 回 user 拍板：

**分支 A（GO — 預期）：** 第八輪 master 對話**真正結束** → user 用 HANDOFF_TO_9TH_MASTER.md 內的對話啟動 prompt 開新對話啟動第九輪 master 接 Phase D

**分支 B（NEAR-GO / HOLD）：** user 拍板：
- **B.1 hard-limit accepted**（同前模式）：殘留 finding 入 NEW_REQ_19 9th master cleanup queue → 第八輪結束 → 9th master 啟動
- **B.2 patch round 5**：第八輪 master 開 inline patch round 5 → user commit → 跑 Round 13 重審 → GO

**分支 C（NO-GO）：** user 拍板：rollback / 重審 / 其他路徑

---

# 3. 文件維護紀律

- 本檔是第八輪 master patch round 4 完成後 Round 12 重審 starter；完成後可 archive
- ⚠ 紀律：本 starter 預設**單輪結束**；多輪重審需 user 明示拍板
- patch round 4 教訓沿用 cascade pattern 教訓 + master starter typo 教訓 — 未來 master 寫 starter 含 spec scope reference 時務必 grep verify SPEC / parser 對齊

---

# 4. Cross-ref

- `_design/CODEX_8TH_MASTER_FINAL_REVIEW_STARTER.md` v0.1（Round 11 starter；本 starter 模板參考）
- `_design/CODEX_8TH_MASTER_FINAL_REVIEW_REPORT.md` v0.1（Round 11 NO-GO；本輪 R11 4 finding baseline）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（含 patch round 4 line 395 R11-MI-02 修補）
- `_design/DECISIONS_LOG.md` v2.0（D-054 拍板權威）
- `_design/POST_LOCK_PENDING.md` v0.13（NEW_REQ 整體狀態）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §3.9（09_i 三 facet 權威）
- `.claude/skills/create-character/SKILL.md` v0.4（R11-CR-01 truncation 修補）
- `09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.2（R11-MA-01 移除 4th facet）
