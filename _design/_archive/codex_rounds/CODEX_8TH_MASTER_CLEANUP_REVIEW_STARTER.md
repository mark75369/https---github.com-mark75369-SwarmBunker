狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master Cleanup round 完成後 CODEX 全面重審 — Round 7 9 finding cleanup verification + 7 維度檢查（含 D-054 NEW_REQ_13 pending state audit）  
優先級：高

# CODEX_8TH_MASTER_CLEANUP_REVIEW_STARTER — 第八輪 master Cleanup round 完成後全面重審

# 0. 本檔用途

第八輪 master 對話接手後第一個動作：對 Round 7 NEAR-GO 殘留 9 個 finding（3 MAJOR R7-MA-01/02/03 + 6 MINOR R7-MI-01~06）做 inline patch round。Cleanup 完成 → 在進 Phase C Wave 9（D-054 拍板 + 3 starter）之前，對所有 cleanup 變動跑 **Round 8 全面重審 checkpoint**。

**對齊傳統：** 同 7th master Round 1-7 重審模式（CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND1~7 已存在參考）。本輪是 8th master Cleanup round 接著的第一個 checkpoint — 用 CODEX 抓任何 Cleanup 期間累積的新 inconsistency / 殘留未關閉 finding / 新 drift。

**前置條件：** 8th master Cleanup round 已完成所有預定變動 + user 已 commit/push（含 R7-MA-01/02/03 三 MAJOR 落地 + R7-MI-01~06 六 MINOR 落地）。

**重審 GO →** 8th master 寫 D-054 NEW_REQ_13 拍板包（per-scene 檔 convention 3 方案分析；user 拍板）→ Phase C Wave 9（3 個下游 starter）。

**重審 NEAR-GO →** user 拍板是否 hard-limit accepted（同 Round 7 模式）或開 8th master inline patch round 2 → Round 9 重審 → GO。

**重審 NO-GO →** 大幅 rollback / restructure；user 拍板路徑。

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- 不涉 Instance-only path（本重審 scope 全 Template repo 內）

⚠ **單輪結束 default：** Round 8 預設一輪結束；不預設自動進 Round 9。若 NEAR-GO，user 拍板決定 hard-limit / patch round 2 / abort。避免 Round 7 那種 7 輪意外迴圈。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第八輪 master Cleanup round 完成後 Round 8 全面重審」— 對 8th master Cleanup round 期間的所有變動跑 7 維度檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1-7 7th master 重審模式（CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND7 v0.1 是 baseline；NEAR-GO accepted 含 3 MAJOR + 6 MINOR 殘留交 8th master cleanup）
- 對應前置：8th master Cleanup round 已完成 17 檔變動 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /create-* / /init-project 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch scope）
- ✗ 不重審 Round 1-7 已 accepted 之 finding（Round 7 NEAR-GO hard-limit accepted；之前 Round 已關閉的 finding 不重議）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定）：**

8th master Cleanup round 變動清單（給你做 review baseline — 17 檔）：

### MAJOR cleanup 落地（3 處）

1. **R7-MA-03** — 3 個 review gate starter active wording 對齊 D-052 雙模式：
   - `_design/CODEX_B55_REVIEW_GATE_STARTER.md`：v0.3 → v0.4（性質 / 身份與職責 / 不變範圍 三段）
   - `_design/CODEX_B65_REVIEW_GATE_STARTER.md`：v0.3 → v0.4（同上）
   - `_design/CODEX_B8_REVIEW_GATE_STARTER.md`：v0.4 → v0.5（同上 + 強烈推薦方案 A wording）

2. **R7-MA-02** — ARCH §3.3.2 active wording 對齊 D-051 後單 marker：
   - `_design/ARCHITECTURE.md`：LOCKED v1.5 → v1.6 partial supersede via D-051
   - 變動點：行 633「三道檢測 PASS」改「兩道檢測 PASS（D-051 後 active #1 marker + #3 bootstrap completed；#2 廢除）」+ 行 639-640「三維度檢測 / 取代 marker + structural inference」改「兩維度檢測 / 取代 marker 檢測；不引入 D-051 已廢除的 #2 structural inference」+ 行 642 Cross-ref pin 升 00_i v0.3 / init-project v0.3 + 加 DECISIONS_LOG §6.13.2 D-051 ref
   - 加 v1.5 → v1.6 partial supersede 摘要區塊在 top（保留既有 v1.4 → v1.5 區塊）

3. **R7-MA-01** — TASKS top 補 v1.8 → v1.9 partial supersede ledger：
   - `_design/TASKS.md`：LOCKED v1.9（header line 2 維持；新增 top 摘要區塊）
   - 變動點：top 加 v1.8 → v1.9 partial supersede ledger 段，列 D-052 §A.10/B.5.5/B.6.5/B.8 四 gate + D-050/D-053 §B.7 兩處

### MINOR cleanup 落地（6 處 → 觸及檔可能多於 6）

4. **R7-MI-01** — `_design/PHASE_B_COMPLETION_REPORT.md` §3.2 驗收表：`phase_b_review_log.md v0.1` → `v0.3`（同行也順手對齊 B.8 starter v0.4 → v0.5 + user 親跑欄改 D-052 雙模式 wording）

5. **R7-MI-02** — `_design/PHASE_B_COMPLETION_REPORT.md` §6.2 D-052 row：DECISIONS_LOG v1.8 → v1.9 + 3 starter v0.2/v0.3 → v0.2~v0.5 + CR-02 backfill 紀錄

6. **R7-MI-03** — 4 個 Phase B 中文 wrapper line 16 wording：
   - `.claude/skills/建立角色/SKILL.md`：「D-049 Template-detect 兩道防線」→「D-051 後 active 單 marker Template-detect（`.template_root` marker；原 D-049 #2 結構推斷防線已 partial supersede 廢除，詳 DECISIONS_LOG §6.13.2）」
   - `.claude/skills/建立大綱/SKILL.md`：同上
   - `.claude/skills/建立關係/SKILL.md`：同上
   - `.claude/skills/建立細綱/SKILL.md`：同上

7. **R7-MI-04** — 3 個 /create-* skill frontmatter description 加 D-050/D-053 mention：
   - `.claude/skills/create-world/SKILL.md` description：加 D-053 partial supersede D-050 子裁決 1 加 /create-world exception 寫 00_b §1/§2
   - `.claude/skills/create-character/SKILL.md` description：加 D-050 子裁決 2 限定 03_characters/ + D-053 exception 不擴及本 skill
   - `.claude/skills/create-relationship/SKILL.md` description：加 D-050 子裁決 2 限定 04_relationships/ + 03_characters/ 兩聲線卡段 + D-053 exception 不擴及本 skill

8. **R7-MI-05** — 3 個 phase_b review_log skeleton §1.3 升級動作改 D-052 雙模式：
   - `_design/phase_b_character_review_log.md` §1.3
   - `_design/phase_b_outline_review_log.md` §1.3
   - `_design/phase_b_review_log.md` §1.3
   - 改後 wording：「依 D-052（DECISIONS_LOG v1.9 §6.15.2）雙模式 — **預設方案 A（AI-assisted）**：user 明示拍板 + 拍板理由後 agent 代執行 mechanical edits；**方案 B（manual fallback）**：user 親身編輯。accountability anchor 為「user 明示拍板」」

9. **R7-MI-06** — `_design/POST_LOCK_PENDING.md` NEW_REQ_8 補 D-051 partial supersede note + 落地檔版本升至 00_i v0.3 / SKILL.md v0.3 / ARCH v1.6 / DECISIONS_LOG v1.9 §6.11 + §6.13

### 8th master Cleanup round 不動段（聲明）

- 不動 LOCKED spec：SPEC / INTEGRATION_CONTRACTS / DATA_FORMAT_SPEC / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA
- 不動 LOCKED registries：3 個 *.template.yaml
- 不動 scripts/*.py
- 不動 27 模板（01_world/ ~ 09_quality_assurance/ 內模板檔）
- 不動 00_protocol/ 任何檔（00_i 已在 D-051 時升 v0.3；本輪 cleanup 不再動）
- 不動 init-project SKILL.md / check-gaps / status SKILL.md / 5 個對應中文 wrapper（初始化專案 / 進度 / 缺漏檢查 / 建立世界觀 — 注意：建立世界觀 wrapper 不含 D-049 wording，未在 R7-MI-03 之 4 wrapper 內）
- 不動 create-outline / create-detailed-outline / init-project 3 個 /create-* skill 的 frontmatter description（R7-MI-04 只針對 create-world / create-character / create-relationship 三檔；create-outline + create-detailed-outline + init-project description 未對齊 D-050/D-053 mention 屬 8th master Cleanup round 故意 scope 縮減；reviewer 可標 INFO 觀察）

---

### 任務目標

新建 1 個檔：
1. `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（重審報告；含 5 必填中文 header）

### 重審 7 維度

**維度 1：R7 9 finding 關閉完整性（最優先）**

對 Round 7 報告 §10 9 個 finding 逐項 verify 是否關閉：

| Finding | 預期關閉證據 |
|---|---|
| R7-MA-01 | TASKS top 是否多了一段 v1.8 → v1.9 partial supersede ledger 列 D-052 四 gate + D-050/D-053 §B.7；位置應在現有 v1.7 → v1.8 區塊之上 |
| R7-MA-02 | ARCH header version v1.5 → v1.6 + top 有 v1.5 → v1.6 ledger 區塊 + §3.3.2 行 633 「三道檢測」改「兩道檢測」+ 行 639-640 stale wording 改 D-051 後表述 + 行 642 Cross-ref pin 升 00_i v0.3 / init-project v0.3 / 加 §6.13.2 ref |
| R7-MA-03 | 3 個 review gate starter（B55 / B65 / B8）header version 升 + 性質段含「D-052 雙模式 — 預設方案 A AI-assisted / 方案 B manual fallback」+ 身份與職責段含「拍板升 REVIEW（D-052 雙模式）」+ 不變範圍段含「不擅自升任何檔狀態（未經 user 明示拍板）；user 明示拍板後可走方案 A AI-assisted」 |
| R7-MI-01 | PHASE_B report §3.2 review_log version 是否從 v0.1 改 v0.3 |
| R7-MI-02 | PHASE_B report §6.2 D-052 row 是否從 v1.8 改 v1.9 + 含 CR-02 backfill 紀錄 |
| R7-MI-03 | 4 個 Phase B 中文 wrapper line 16「D-049 Template-detect 兩道防線」是否改 D-051 後 wording |
| R7-MI-04 | 3 個 /create-* skill frontmatter description 是否提 D-050/D-053；create-outline / create-detailed-outline / init-project description 未對齊屬故意 scope 縮減（INFO 觀察） |
| R7-MI-05 | 3 個 phase_b review_log §1.3「升級動作」是否改 D-052 雙模式 wording |
| R7-MI-06 | POST_LOCK_PENDING NEW_REQ_8 是否補 D-051 partial supersede note + 落地檔版本對齊 v1.6 / v0.3 / v1.9 |

對每筆 finding：標記 RESOLVED / PARTIAL / NOT_RESOLVED。

**維度 2：跨檔 cross-reference 一致性（Cleanup 引入的新 cross-ref 是否對齊）**

verify 以下新引入 cross-ref：
- ARCH v1.6 top ledger 內提 DECISIONS_LOG §6.13 D-051 — verify §6.13 確實存在且內容對應
- TASKS v1.9 top ledger 內提 D-052 DECISIONS_LOG v1.8 §6.15.2 + v1.9 §6.15.2 CR-02 backfill — verify兩處皆存在
- 3 個 phase_b review log §1.3 內提 DECISIONS_LOG v1.9 §6.15.2 D-052 — verify §6.15.2 existed 並含 CR-02 backfill
- POST_LOCK_PENDING NEW_REQ_8 內提 ARCH v1.6 §3.3.2 — verify v1.6 已升
- POST_LOCK_PENDING NEW_REQ_8 內提 DECISIONS_LOG v1.9 §6.11 + §6.13 — verify兩節都存在
- 3 個 /create-* skill description 內提 D-050 子裁決 2 / D-053 — verify DECISIONS_LOG §6.12.2 + §6.16.2 對應
- 4 wrapper 內提 DECISIONS_LOG §6.13.2 — verify §6.13.2 內容對齊

**維度 3：LOCKED 文件動過合規性（v1.5 → v1.6 ARCH + TASKS top ledger）**

verify Cleanup round 動到的 LOCKED 檔變動有 D-NNN 拍板背書 + partial supersede 紀錄完整：

- ARCH v1.5 → v1.6：D-051 拍板背書 ✓（D-051 已在 DECISIONS_LOG v1.6 §6.13 拍板；ARCH v1.5 同時期已加 §3.3.2 partial supersede note；v1.6 屬「對 v1.5 既有 D-051 標記後 active wording 殘留 cleanup」非新 supersede）— verify 此邏輯成立
- TASKS v1.9（line 2 維持；top 加 ledger 段）：屬 partial supersede ledger backfill（R7-MA-01 cleanup）；無新 D-NNN 但需 verify ledger 內容對應實際 DECISIONS_LOG v1.8/v1.9 §6.15.2 D-052 + §6.16.2 D-053 拍板紀錄

verify 以下 LOCKED 檔**確實不動**：
- _design/SPEC.md
- _design/INTEGRATION_CONTRACTS.md
- _design/DATA_FORMAT_SPEC.md
- _design/UPSTREAM_DOWNSTREAM_SPEC.md
- _design/UX_SPEC.md
- _design/REQUIREMENTS_LOCK.md
- _design/L3_EXPORT_PROMPT_SCHEMA.md
- _design/registries/*.template.yaml（3 個）
- scripts/*.py
- 既有 27 模板（01_world/ / 02_vocabulary/ / 03_characters/ / 04_relationships/ / 05_plot/ / 06_scene_index/ / 07_scene_tasks/ / 08_dialogue_outputs/ / 09_quality_assurance/）
- 00_protocol/ 任何檔（含 00_i 不再動 — D-051 階段已升 v0.3）

可用 `git diff fb09c6a HEAD --name-only`（fb09c6a = 第七輪 master 收尾交付 commit）verify。

**維度 4：Template vs Instance 邊界污染檢查**

verify Template repo（D:\劇本開發工具）內**沒有新混入 Instance-specific data**：
- grep Template 內所有 _design/ + 00_protocol/ + .claude/skills/ + 27 模板，搜「林思羽」/「陳則安」/「情緒感知體質」/「my-test-instance」/ 任何具體作品角色名（Round 7 維度 4 已 PASS；本輪 verify 8th master Cleanup round 沒新引入）
- 任何 review_log Template 骨架是否仍是 placeholder（不該有 actual Instance entry）
- 3 個 phase_b review_log §1.3 Cleanup 改 wording 是否仍純骨架不嵌 Instance data
- 3 個 review gate starter 性質/身份/不變範圍段改 wording 是否仍純框架描述不嵌 specific test data

**維度 5：5 個 /create-* skill chain consistency（cleanup 後 description drift 檢查）**

cleanup 對 3 個 /create-* skill description 動了 → verify 5 skill chain 仍 consistent：
- create-world / create-character / create-relationship description：含 D-050/D-053 mention（cleanup 已加）
- create-outline / create-detailed-outline description：未含 D-050/D-053 mention（cleanup 故意縮減 scope；reviewer 可標 INFO「為什麼 5 skill description 不對齊」觀察）
- init-project description：未含 D-050/D-053 mention（同上）
- 5 SKILL.md body 「## 邊界」段是否仍含 D-050 子裁決 1 + 子裁決 2 明示句（Round 7 已 verify；本輪 verify 沒被 cleanup 動到）
- 5 SKILL.md header version 維持（cleanup 不升 version；只改 description）— verify

**維度 6：未解決 stale reference 偵測（cleanup 後新 stale 檢測）**

grep 以下 stale pattern（重點 cleanup 引入或殘留的 stale）：
- 任何檔內提「ARCH v1.5」應改「v1.6」（除非歷史紀錄）— ARCH v1.6 升版後其他檔 cross-ref 是否對齊
- 任何 cross-ref 內提「DECISIONS_LOG v1.8」應改「v1.9」（除非歷史紀錄）
- 任何 cross-ref 內提「init-project v0.2」/「00_i v0.2」應改「v0.3」
- 任何 starter 提「三道檢測 / structural inference」殘留（ARCH 已清；其他檔有無延伸？）
- 任何文檔提「D-049 Template-detect 兩道防線」未標 D-051 supersede（4 wrapper 已清；其他位置有無漏？— 例如 ARCH §3.3.2 strikethrough block 內容 / DECISIONS_LOG §6.11 D-049 拍板紀錄屬歷史保留不改）
- 任何 starter 內提「TASKS v1.8」應改「v1.9」（除非歷史紀錄）

**維度 7：D-054 NEW_REQ_13 pending state audit（per-scene 檔 convention 上下文 — 為 D-054 拍板提供 audit）**

8th master 將在 Round 8 之後 open D-054 拍板 NEW_REQ_13（per-scene 檔 convention）。本維度為該拍板提供 audit baseline。

verify 並列出以下檔對「CH-* / S-*-* 寫檔 convention」的當前描述（不修補；只 audit）：

| 檔 | 期待 audit 內容 |
|---|---|
| `_design/SPEC.md` §5.1 | CH-* / S-*-* entity 定義；scene_id 命名規則 |
| `_design/SPEC.md` §12.5 | 任務包必填欄位 — scene_id 引用 |
| `_design/DATA_FORMAT_SPEC.md` §3.2 | phase_log scene_id 欄位 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.3.2 | /scene-task 讀檔來源（含「讀 06_a 場景索引」描述）|
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.3.4 | /scene-task 寫檔目標（含「07_scene_tasks/CH<n>_S<m>_*」描述）|
| `_design/TASKS.md` §D.2 + §D.3 + §D.4 | /scene-task + /dialogue-write + /qa 對 scene_id 路徑期望 |
| `00_protocol/00_h_細綱創建協議.md` v0.2 | /create-detailed-outline 寫 05_b / 06_a 規格（聚合 vs per-scene 描述）|
| `00_protocol/00_k_台詞生產流程協議.md` | 下游 pipeline 對 scene file 期望 |
| `.claude/skills/create-detailed-outline/SKILL.md` v0.1 | 階段 4 寫檔 — 聚合 06_a 還是 per-scene |
| `_design/registries/issue_type_registry.template.yaml` | 00_h_detailed_outline 議題（含拆分相關項？）|

對每個檔記錄當前描述採聚合 06_a / per-scene / hybrid / 模糊未定。

**並補 audit 觀察：**
- 當前聚合 06_a vs per-scene 在現存 spec 間是否有矛盾（例：00_h 寫聚合但 UD §2.3 寫 per-scene 路徑模板）
- /create-detailed-outline SKILL.md「D-050 寫檔目錄表」CH 行寫 `05_b + 06_a only`（聚合式）vs UD §2.3.4 範例 `07_scene_tasks/CH01_S03_台詞任務包.md`（per-scene）— 是否前後不一致或屬不同 phase 路徑
- 觀察是否有 spec 已暗示 hybrid convention（per-scene 拆 + 06_a 索引）

**對 D-054 拍板的影響：**
- 若 audit 顯示「現存 spec 全聚合」→ D-054 選 1 Hybrid 改動範圍最小（保留聚合預設 + 加 split 選項）
- 若 audit 顯示「現存 spec 已暗示 hybrid」→ D-054 選 1 落地最自然
- 若 audit 顯示「現存 spec 全 per-scene」→ D-054 選 2 全 per-scene 最 align（但與當前 /create-detailed-outline 衝突）
- 若 audit 顯示「現存 spec 完全模糊」→ D-054 任一選項都可

**Reviewer 不下 D-054 結論**，只提供 audit 表 + 觀察給 8th master 拍 D-054 時參考。

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
git diff fb09c6a HEAD --name-only 2>&1 | head -30
```

### Finding 分類

每個發現的 issue 分類：

- **CRITICAL**：spec 違反 / LOCKED 檔變動無 D-NNN 背書 / Template 嚴重污染（specific test data） / Round 7 已 accepted finding 被 Cleanup 破壞
- **MAJOR**：cross-doc 嚴重不一致 / Cleanup finding 未關閉（R7-MA-01/02/03 任一 PARTIAL 或 NOT_RESOLVED）/ 大量新 stale reference
- **MINOR**：版本欄 / cross-ref 小不一致 / 少數新 stale wording / R7-MI 未關閉
- **INFO**：觀察記錄但不阻 GO（例：create-outline / create-detailed-outline / init-project description 未對齊 D-050/D-053 — 屬 cleanup 故意縮減）

### 決策準則

- **GO（PASS）**：0 CRITICAL + ≤2 MAJOR + 9 finding 全 RESOLVED 或 INFO → 8th master 可直接進 D-054 拍板 + Phase C Wave 9
- **NEAR-GO（HOLD）**：0 CRITICAL + 3-5 MAJOR + 多 MINOR → user 拍板是否 hard-limit accepted（同 Round 7 模式；殘留交 9th master cleanup）OR 8th master 開 patch round 2 → Round 9 重審 → GO
- **NO-GO**：≥1 CRITICAL OR ≥6 MAJOR → 大幅 rollback / restructure 考量 → user 拍板路徑（patch round 2 / rollback Cleanup / 其他）

⚠ **單輪結束 default：** Round 8 本輪結果出來後**回 user 拍板**；不預設自動進 Round 9。避免 Round 1-7 那種 7 輪意外迴圈。

### 不變範圍（嚴格）

- 不改任何 spec / SKILL.md / starter / protocol / 模板 / scripts / registries
- 不跑真實 skill
- 不修補 finding（紀錄即可；patch 屬 master 動作）
- 不下 D-054 結論（屬 user 拍板）
- 只新建 1 個 review report 檔

### 完成判定

✓ 7 維度全 verify + 結果寫入 review report
✓ 維度 1 對 R7 9 finding 逐項 RESOLVED / PARTIAL / NOT_RESOLVED 標記
✓ 維度 7 D-054 NEW_REQ_13 pending state audit 表完整 + 觀察提供
✓ 技術驗證 3 命令跑 + 結果記
✓ Finding 分類（含計數：CRITICAL / MAJOR / MINOR / INFO）
✓ 決策判定（GO / NEAR-GO / NO-GO）+ 對應 rationale
✓ `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1 5 中文 header 齊 + 報告完整

### 報告結構建議

```
狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：第八輪 master Cleanup round 完成後 Round 8 全面重審結果  
優先級：高

# CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT

# 0. 文件目的
# 1. Round 8 摘要 + GO / NEAR-GO / NO-GO 判定
# 2. 維度 1：R7 9 finding 關閉完整性（9 row 表）
# 3. 維度 2：跨檔 cross-reference 一致性（finding 表）
# 4. 維度 3：LOCKED 文件動過合規性（ARCH v1.6 + TASKS top ledger 合規 + 應不動列表 verify）
# 5. 維度 4：Template vs Instance 邊界污染（grep 結果 + finding 表）
# 6. 維度 5：5 skill chain consistency（5 skill description audit）
# 7. 維度 6：未解決 stale reference（grep 結果 + finding 表）
# 8. 維度 7：D-054 NEW_REQ_13 pending state audit（10 row 表 + 觀察）
# 9. 技術驗證結果（check_headers / check_paths / build_repo_index / git log / git diff 摘要）
# 10. Finding 總計（CRITICAL / MAJOR / MINOR / INFO 計數）
# 11. 決策判定 + Rationale
# 12. 給 8th master 的建議（後續處理優先順序 + D-054 拍板 audit 重點）
# 13. Cross-ref
```

### Go / Done 判定指引

- **DONE：** 上述驗收全 ✓ → review report 落地 → user commit/push → 回 8th master 接手讀
- **BLOCKED：** 任一驗收 ✗ 回 user

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX Round 8 重審完成 → user commit/push → 回 8th master：

**分支 A（GO）：** 8th master 進 D-054 拍板包寫作（NEW_REQ_13 per-scene 檔 convention 3 方案分析 + 推薦選 1 Hybrid）→ user 拍板 → Phase C Wave 9（3 個下游 starter）

**分支 B（NEAR-GO / HOLD）：** user 拍板：
- **B.1 hard-limit accepted**（同 Round 7 模式）：殘留 finding 紀錄入 9th master cleanup queue → 8th master 直接進 D-054 拍板包 + Phase C Wave 9
- **B.2 patch round 2**：8th master 開 inline patch round 2 處理 finding → user commit → 跑 Round 9 重審（重貼 starter v0.2）→ GO → 進 D-054

**分支 C（NO-GO）：** user 拍板：
- **C.1 patch round 2 + Round 9**（同 B.2）
- **C.2 rollback Cleanup round + 從 Round 7 NEAR-GO accepted 狀態進 D-054**（接受 R7 殘留 + 不做 Cleanup）
- **C.3 其他 user 路徑**

---

# 3. 文件維護紀律

- 本檔是 8th master Cleanup round 完成後 Round 8 全面重審 starter；完成後可 archive 進 `_design/archive/`
- 對應 review report 也屬 8th master 收尾事實紀錄；不刪除
- 未來 9th / 10th master 收尾前若需類似重審，可採同 starter pattern 寫對應 starter
- ⚠ 紀律：本 starter 預設**單輪結束**；避免 Round 1-7 那種 7 輪意外迴圈。多輪重審需 user 明示拍板

---

# 4. Cross-ref

- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0（第八輪 master scope）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_STARTER.md` v0.1（Round 1-7 starter 模板參考）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND7.md` v0.1（Round 7 NEAR-GO accepted；本輪 R7 9 finding cleanup baseline）
- `_design/DECISIONS_LOG.md` v1.9（D-049 / D-050 / D-051 / D-052 / D-053 拍板權威）
- `_design/POST_LOCK_PENDING.md` v0.9（NEW_REQ_10/11/12/13/14；NEW_REQ_8 已補 D-051 note via R7-MI-06）
- `_design/TASKS.md` v1.9（R7-MA-01 cleanup 後）
- `_design/ARCHITECTURE.md` v1.6（R7-MA-02 cleanup 後）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.1（R7-MI-01/02 cleanup 後）
- 3 個 review gate starter v0.4/v0.4/v0.5（R7-MA-03 cleanup 後）
- 3 個 phase_b review_log（R7-MI-05 cleanup 後）
- 4 個 Phase B 中文 wrapper（R7-MI-03 cleanup 後）
- 3 個 /create-* skill（R7-MI-04 cleanup 後）
