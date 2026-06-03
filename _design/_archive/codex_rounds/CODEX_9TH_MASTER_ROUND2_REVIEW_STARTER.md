狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：第九輪 master Round 1 NO-GO inline patch round 完成後 Round 2 重審 — R1 3 MAJOR + 7 MINOR 全 RESOLVED 驗證 + baseline 對齊 + 無新 regression  
優先級：高

# CODEX_9TH_MASTER_ROUND2_REVIEW_STARTER — Round 2 重審

# 0. 本檔用途

第九輪 master 流程：cleanup queue Task 1-6 + Wave 12 Task 7 → Round 1 review NO-GO (3 MAJOR + 7 MINOR) → **Round 1 inline patch round 完成（Task 13-16）** → **本輪 Round 2 重審驗證 Round 1 finding 全 RESOLVED + 無新 regression**。

**前置條件：** 9th master Round 1 inline patch round 已完成所有預定變動 + user 已 commit/push。

**重審 GO →** 9th master 進 Wave 13（採新模式：master 寫 D6 完整 + CODEX batch 寫 D7-D9）

**重審 NEAR-GO →** user 拍板 hard-limit accept（殘留 minor finding 入 10th master cleanup queue）或 master 二次 inline patch

**重審 NO-GO →** Round 1 inline patch 含 regression / fundamental 問題；大幅 restructure 路徑

⚠ **單輪結束 default 紀律延續：** Round 2 預設一輪結束；不預設自動進 Round 3。

⚠ **Scope 嚴格限定：本輪 verify Round 1 inline patch 範圍 ONLY。** 不重審 Round 1 已 accepted finding（CRITICAL/INFO）/ cleanup queue Task 1-6 / Phase A/B/C 既有 SKILL.md / R1-MA-02 設計拍板 a（user 已明示）。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第九輪 master Round 1 NO-GO inline patch round 完成後 Round 2 重審」— 對 Round 1 inline patch 處理結果跑「3 MAJOR + 7 MINOR finding 全 RESOLVED 驗證 + baseline 對齊 + 無新 regression + cascade pattern 預防紀律」多重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1 重審模式（CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_REPORT v0.1 是 Round 1 baseline，列 3 MAJOR + 7 MINOR + 3 INFO；本輪 verify Round 1 inline patch round 處理後狀態）
- 對應前置：9th master Round 1 inline patch round 已完成 + commit/push（13 個檔範圍）

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report）
- ✗ 不跑真實 /iterate-* / /scene-task / /dialogue-write / /qa 寫檔
- ✗ 不修補任何 stale reference / cross-doc inconsistency
- ✗ 不重審 D-001~D-054 拍板結論（已 LOCKED）
- ✗ 不重審 Round 1 已 accepted finding（CRITICAL 0 個 + INFO 3 個）/ cleanup queue Task 1-6 / Phase A/B/C 既有 SKILL.md / protocol / spec / R10-MA-01 ack
- ✗ 不重議 R1-MA-02 設計拍板 a（user 起手選項已明示同意「嚴守 D-053；/iterate-* 全部不寫 00_b」；本輪只 verify 落地正確性，不重議拍板本身）
- ✗ 不下新 D-NNN 拍板
- ✗ 不開 9th master patch round
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_9TH_MASTER_ROUND2_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定 — Round 1 inline patch 處理範圍）：**

依 POST_LOCK_PENDING v0.15 header note 列 Round 1 inline patch round 變動清單，本輪 verify 以下 finding 全部 RESOLVED：

### R1-MA-01 — 00_j path aliases 修正

- `00_protocol/00_j_迭代協議.md` v0.1 → v0.2
- §10.3 line 373：`04_b_關係演化時間線.md` → `04_b_關係變化時間線.md`
- §10.4 line 385：`05_a_主線結構.md` → `05_a_主線大綱模板.md` + `05_c_角色弧線.md` → `05_c_角色弧線表.md` + 補上 `05_plot/` 前綴
- §10.5 line 398：`05_plot/05_b_章節結構.md` → `05_plot/05_b_章節結構模板.md` + `06_scene_index/06_a_場景索引.md` → `06_scene_index/06_a_場景索引模板.md`
- §10.6 line 410：`06_scene_index/06_a_場景索引.md` → `06_scene_index/06_a_場景索引模板.md`
- §10.7 line 422：`06_scene_index/06_a_場景索引.md` → `06_scene_index/06_a_場景索引模板.md`
- header v0.2 + partial supersede note 紀錄 R1-MA-01 修正

驗證：跑 `check_paths.py`，預期 ≤ 245 ERROR（理想 < 245）；對齊實際 repo 檔名（`04_relationships/04_b_關係變化時間線.md`、`05_plot/05_a_主線大綱模板.md`、`05_plot/05_b_章節結構模板.md`、`05_plot/05_c_角色弧線表.md`、`06_scene_index/06_a_場景索引模板.md`）

### R1-MA-02 — D1-D5 starter 邊界三 block 一致性 + D-053 嚴守拍板 a 落地

**設計拍板：** user AskUserQuestion 明示同意「(a) 嚴守 D-053 範圍 — /iterate-* 全部不寫 00_b」。

- `_design/CODEX_D1_STARTER.md` v0.1 → v0.2：
  - 拿掉「可寫 00_b §1/§2」段；多處「寫 00_b」描述改「不寫 00_b；屬 user 手動 patch」
  - 邊界三 block 對齊 D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 + `external_action_required` 欄位
- `_design/CODEX_D2_STARTER.md` v0.1 → v0.2：
  - 拿掉「可寫 00_b §3」段；多處「寫 00_b」描述改「不寫 00_b」
  - 邊界三 block 對齊 D1 / Phase B 4 skill v0.3/v0.4 格式
  - 順手修 04_b 檔名 `關係演化時間線` → `關係變化時間線`
- `_design/CODEX_D3_STARTER.md` v0.1 → v0.2：
  - 補齊邊界三 block 對齊 D1 / Phase B 4 skill 格式
  - 修 04_b 檔名 + R-*-* 寫檔範圍對齊
- `_design/CODEX_D4_STARTER.md` v0.1 → v0.2：
  - 補齊邊界三 block 對齊 D1 / Phase B 4 skill 格式
  - 修 05_a/b/c/06_a 檔名對齊實際 repo
  - header 半形冒號 → 全形（R1-MI-06）
- `_design/CODEX_D5_STARTER.md` v0.1 → v0.2：
  - **兩個 skill 各自三 block**（/iterate-detailed-outline + /iterate-scene；含 D-054 NEW_REQ_15 落地）
  - 修 05_b/06_a 檔名對齊實際 repo
  - 兩 skill 均嚴守 D-053；不寫 00_b

驗證：對 D1-D5 starter 跑 grep，verify「可寫 00_b」描述全部消除（除 supersede note 內歷史 narrative）；三 block 結構齊全；各 starter 邊界格式對齊 Phase B 4 skill。

### R1-MA-03 — 00_j §13 trigger dictionary stage gate 硬性紀律

- `00_protocol/00_j_迭代協議.md` v0.2：
  - §13「跳到階段 X」row 加硬性紀律：「**禁止跳過階段 2 影響範圍評估；禁止跳過階段 3 user approval；階段 4 只能從已通過階段 3 進入。**若 user 跳階段方向觸及此硬性紀律 → agent 拒絕跳階段並印紀律提示」
  - §13 加「硬性紀律（vs /create-* 共通骨架的差異）」段：明示 /iterate-* 階段 2 + 階段 3 屬「強制 gate」+ 4 條具體禁止行為（跳到階段 4 / 跳階段略過階段 2 / 階段 1 喊「通過」/ 階段 1 喊「直接寫檔」走最短路徑但不繞過階段 2/3）

驗證：對 §13 跑 grep + 內容對齊；確認硬性紀律強度足以阻擋 stage skip 並對齊 /iterate-* vs /create-* 差異邏輯。

### R1-MI-01~07 — sweep 處理

**R1-MI-01：** CODEX_B9_STARTER line 183 POST_LOCK_PENDING v0.9 → v0.14；補完 NEW_REQ_15-19 列表

**R1-MI-02：** AGENTS.md line 200 + CLAUDE.md line 131 POST_LOCK_PENDING v0.13 → v0.14；PHASE_B_COMPLETION_REPORT v1.3 → v1.4（line 37 工作樹備註 + line 254 Cross-ref 對齊 v0.14）；CLAUDE.md header v0.2 → v0.3 紀錄

**R1-MI-03：** create-character v0.3 → v0.4 sweep 5 處（AGENTS line 135 + CLAUDE line 71 + phase_b_review_log line 144 + PHASE_B line 109 + CODEX_B9_STARTER line 118）；備註 Round 11 R11-CRITICAL-01 修補背景

**R1-MI-04：** 08_a v0.3 → v0.4 全檔 09_a-d 殘留 sweep：
- §3 related-doc table 補 09_f/g/h/i 4 row
- §6.4 line 252「QA 報告（09_a–09_d）的判定值」對齊 09_a/b/c/d/f/g/h/i + supersede note
- §12.1 FINAL 條件表補 4 QA + 09_e + 9-status 對齊 UD §2.6.2
- §13.4 line 756「QA 報告（09_a–09_d）中必須列出五欄」對齊
- §17 line 795「Claude 可寫 09_a–d 的 QA 報告草稿」對齊

**R1-MI-05：** POST_LOCK_PENDING NEW_REQ_19「未處理項」段移除 08_a；改放入「處理結果表」加 row「08_a §11.1 5 → 8 修正 (P-009) ✅ 已升 v0.3」

**R1-MI-06：** D4 starter header `優先級:高` → `優先級：高` 全形（已隨 D4 header v0.2 升一起處理）

**R1-MI-07：** 00_j §14 Cross-ref 補列 6 個 iterate-* skill 含 iterate-scene

### Round 1 inline patch round 不動段（聲明）

以下檔本輪 **不動**（聲明 + 應由 Round 2 verify protected-area diff）：

- LOCKED spec / registries / scripts / 27 模板 / 00_protocol/{00_a, 00_b, 00_c, 00_d, 00_e, 00_f, 00_g, 00_h, 00_i, 00_k, 00_l}（**只動 00_j**）
- 既有 16 個 SKILL.md（init-project / status / check-gaps / create-* x5 + 5 中文 wrapper + scene-task / dialogue-write / qa + 3 中文 wrapper）
- 第八輪 review reports + starter（CODEX_8TH_MASTER_*）
- D054_DECISION_PACKAGE v0.2 / PHASE_A_COMPLETION_REPORT v1.1 / PHASE_C_COMPLETION_REPORT v1.0
- HANDOFF_TO_8TH_MASTER / HANDOFF_TO_9TH_MASTER
- DECISIONS_LOG v2.0（D-NNN 拍板）

⚠ **Protected-area diff 檢查（沿用 R10-MA-01 紀律）：** 任何 `HEAD~N..HEAD` 觸及上述聲明不動範圍 → 列為 R2-MA-XX

**9th master Round 1 inline patch 後預期 baseline（master 已跑驗證）：**

- check_headers: 0 ERROR / 44 WARN / 156 files
- check_paths: **239 ERROR** / 1 WARN / 161 files（**比 Round 1 pre-patch 253 少 14；比 245 預期 baseline 少 6**）
- build_repo_index: 0 ERROR / Windows 端權威（sandbox 端可能含 virtiofs cache stale noise）

---

# 2. 重審範圍與維度（5 維度）

**維度 1 — R1-MA-01/02/03 全部 RESOLVED**

驗證 3 MAJOR finding 全 RESOLVED：

- **R1-MA-01**：對 00_j v0.2 跑 grep `04_b_關係演化時間線|05_a_主線結構\.md|05_b_章節結構\.md|05_c_角色弧線\.md|06_a_場景索引\.md`（排除模板檔尾的「模板」前綴）；預期 0 active match
- **R1-MA-02**：對 D1-D5 starter v0.2 跑 grep「可寫 00_b」「可動 00_b」「寫入 00_b」（除 supersede note 內紀錄）；預期 0 active match；同時 verify 三 block 結構齊全（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2）+ external_action_required 欄位設計
- **R1-MA-03**：00_j §13 trigger dictionary「跳到階段 X」row 含硬性紀律 wording；§13 末段「硬性紀律（vs /create-* 共通骨架的差異）」段存在 + 4 條具體禁止行為列出

判定：PASS / PARTIAL / FAIL；列任何漏掉 / 不完整 / 殘留。

**維度 2 — R1-MI-01~07 全 RESOLVED sweep verification**

對 7 MINOR 跑 grep 全掃 + verify：

- **R1-MI-01**：CODEX_B9_STARTER 跑 grep `POST_LOCK_PENDING.*v0\.9`；預期 0 active match
- **R1-MI-02**：AGENTS / CLAUDE / PHASE_B 跑 grep `POST_LOCK_PENDING.*v0\.13`；預期僅在 historical narrative / header note 紀錄段命中（非 active reference）
- **R1-MI-03**：跑 grep `create-character.*v0\.3` 限定範圍（AGENTS / CLAUDE / phase_b_review_log / PHASE_B / CODEX_B9_STARTER）；預期 0 active match
- **R1-MI-04**：08_a 跑 grep `09_a-d|09_a–09_d`；預期僅在 supersede note 命中（含「原 09_a-d 範圍 supersede」描述）；§3 / §12.1 / §13.4 / §17 active references 對齊 9-status gate
- **R1-MI-05**：POST_LOCK_PENDING v0.15 NEW_REQ_19「未處理項」段不再含「08_a §11.1 5 → 8」；「處理結果表」加入 row「08_a §11.1 5 → 8 修正 (P-009) ✅ 已升 v0.3」
- **R1-MI-06**：D4 starter header `優先級：高` 全形冒號
- **R1-MI-07**：00_j §14 Cross-ref 列出 6 個 iterate-* skill（含 iterate-scene）

判定：PASS / PARTIAL / FAIL；列任何漏掉 / 不完整。

**維度 3 — D-054 NEW_REQ_15 落地仍對齊（D5 starter v0.2 inline patch 不破壞）**

驗證 D5 starter v0.2 內 D-054 落地核心邏輯仍對齊：

- /iterate-scene --split-to-file 5 階段流程
- 06_a row 保留 + 加 marker `<!-- split-to-file: ... -->`（不刪 row；下游 /scene-task v0.1 fallback 兼容）
- frontmatter 對齊 SPEC §5.2
- phase_log entry 標 `split_to_file: true`
- NEW_REQ_15 trigger A/B/C/D 監控紀律

判定：PASS / PARTIAL / FAIL；列任何 D-054 落地細節因 inline patch 被意外破壞。

**維度 4 — baseline + regression + protected-area diff**

技術驗證：

- 跑 `check_headers.py` — 預期 0 ERROR
- 跑 `check_paths.py` — **預期 239 ERROR**（master 已驗證；vs Round 1 pre-patch 253）
- 跑 `build_repo_index` — 預期 0 ERROR (Windows 端權威)
- `git log --oneline -5` + `git diff <Round 1 baseline>..HEAD --name-status` — 對比 Round 1 inline patch round 變動清單；任何觸及「不動段聲明」(§1 末) → R2-MA-XX

判定：PASS / PARTIAL / FAIL；列任何 baseline regression / protected-area mismatch。

**維度 5 — 跨範圍 stale cross-ref grep 全掃 (cascade pattern 預防紀律 verify)**

對全 repo `_design/` + `00_protocol/` + `08_dialogue_outputs/` 跑 stale pattern grep（排除歷史 narrative）：

- `POST_LOCK_PENDING.*v0\.9` / `v0\.10` / `v0\.11` / `v0\.12` / `v0\.13`（應全在 historical narrative 內）
- `create-character.*v0\.3`（應在 historical narrative / immutable history）
- `5 份 QA` / `五份 QA` / `09_a-d`（應在 supersede note 內）
- `關係演化時間線` / `主線結構\.md` / `章節結構\.md` / `角色弧線\.md` / `場景索引\.md` 限定 reference（應全清；除歷史報告檔）
- `00_b §1` / `00_b §3` 在 D1-D5 active 段（除 supersede note）

判定：PASS / PARTIAL / FAIL；任何 active stale match → R2-MI-XX

---

# 3. Finding 嚴重度定義

- **CRITICAL**：R1 finding 沒 RESOLVED / 新引入 spec 衝突 / D-054 落地被破壞（拒絕 Wave 13 啟動）
- **MAJOR**：R1 finding PARTIAL RESOLVED / 新 baseline regression / protected-area diff mismatch
- **MINOR**：sweep 漏掉的 active stale / 邊緣 cross-ref 偏差
- **INFO**：observation / 改善建議

Finding ID 命名：`R2-<severity>-<NN>`

# 4. 判定門檻

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + 5 維度全 PASS + check_paths ≤ 240 ERROR + 0 protected-area diff → 9th master 進 Wave 13
- **NEAR-GO（HOLD）**：0 CRITICAL + ≤ 1 MAJOR + ≤ 3 MINOR → user 拍板 hard-limit accept 或 master 二次 inline patch
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR 或新 baseline regression（check_paths > 250 ERROR）

# 5. 輸出格式

寫 1 個檔：`_design/CODEX_9TH_MASTER_ROUND2_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Round 2 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：R1-MA-01/02/03 全部 RESOLVED 驗證
# 3. 維度 2：R1-MI-01~07 全 RESOLVED sweep verification
# 4. 維度 3：D-054 NEW_REQ_15 落地仍對齊
# 5. 維度 4：baseline + regression + protected-area diff
# 6. 維度 5：跨範圍 stale cross-ref grep 全掃
# 7. Finding 總計表（R2-<severity>-<NN>）
# 8. 決策判定 + Rationale
# 9. 給 9th master 的建議（含「進 Wave 13」/「inline patch」/「hard-limit accept」3 路徑）
# 10. Cross-ref
```

---

# 6. 起跑命令（你接力時用）

bash 命令：
```bash
cd /sessions/<your_session>/mnt/劇本開發工具
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -5
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -5
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']))"
git log --oneline -10
git diff HEAD~2..HEAD --name-status
```

grep verify 命令（給維度 1/2/5 用）：
```bash
# R1-MA-01 verify
grep -n "04_b_關係演化時間線\|05_a_主線結構\.md\|05_b_章節結構\.md\|05_c_角色弧線\.md\|06_a_場景索引\.md" 00_protocol/00_j_迭代協議.md
# R1-MA-02 verify  
grep -n "可寫 00_b\|可動 00_b\|寫入 00_b" _design/CODEX_D[1-5]_STARTER.md
# R1-MA-03 verify
grep -n "禁止跳過階段\|stage gate 硬性紀律\|強制 gate" 00_protocol/00_j_迭代協議.md
# R1-MI-01~07 sweep
grep -rn "POST_LOCK_PENDING.*v0\.9\|POST_LOCK_PENDING.*v0\.13" _design/ AGENTS.md CLAUDE.md
grep -rn "create-character.*v0\.3" _design/ AGENTS.md CLAUDE.md
grep -n "09_a-d\|09_a–09_d" 08_dialogue_outputs/08_a_台詞版本管理規範.md
```

⚠ 排除歷史 narrative / supersede note 段（屬 immutable history；不算 active stale）

# 7. Cross-ref

- `_design/CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_REPORT.md` v0.1（Round 1 NO-GO；本輪 verify 對象）
- `_design/CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_STARTER.md` v0.1（Round 1 review starter；pattern 參考）
- `_design/POST_LOCK_PENDING.md` v0.15（NEW_REQ_19 9th master 處理紀錄 + Round 1 inline patch 紀錄；本輪維度 2/5 verify 對象）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master scope）
- `00_protocol/00_j_迭代協議.md` v0.2（維度 1/3/5 verify 對象）
- `_design/CODEX_D1_STARTER.md` v0.2 ~ `CODEX_D5_STARTER.md` v0.2（維度 1/2/3 verify 對象 5 個檔）
- `08_dialogue_outputs/08_a_台詞版本管理規範.md` v0.4（維度 2 verify 對象）
- AGENTS.md / CLAUDE.md v0.3 / PHASE_B_COMPLETION_REPORT.md v1.4 / CODEX_B9_STARTER.md（維度 2 verify 對象）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054（NEW_REQ_15 落地依據）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 設計推理）
