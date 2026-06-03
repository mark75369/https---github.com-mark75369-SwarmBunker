狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：第九輪 master Round 2 NO-GO inline patch round 完成後 Round 3 重審 — R2-MAJOR-01/02 + R2-MINOR-01/02 全 RESOLVED 驗證 + R2-MAJOR-03 hard-limit accept ack + baseline 對齊  
優先級：高

# CODEX_9TH_MASTER_ROUND3_REVIEW_STARTER — Round 3 重審

# 0. 本檔用途

第九輪 master 流程：cleanup queue → Wave 12 → Round 1 NO-GO → Round 1 inline patch → Round 2 NO-GO (3 MAJOR + 2 MINOR + 2 INFO) → **Round 2 inline patch round 完成** → **本輪 Round 3 重審驗證 R2 finding 全 RESOLVED + baseline 對齊（含 R2-MAJOR-03 hard-limit accept）**。

**前置條件：** 9th master Round 2 inline patch round 已完成 + user 已 commit/push。

**重審 GO →** 9th master 進 Wave 13（採新模式：master 寫 D6 完整 + CODEX batch 寫 D7-D9）

**重審 NEAR-GO →** user 拍板 hard-limit accept

**重審 NO-GO →** 大幅 restructure 路徑

⚠ **單輪結束 default 紀律延續：** Round 3 預設一輪結束。

⚠ **Scope 嚴格縮小（vs Round 1/2）：本輪 verify Round 2 inline patch 範圍 ONLY。**

⚠ **Baseline 認知校正：** Windows 端權威；sandbox 跑出的 ERROR 數可能低於 Windows 實測（屬 virtiofs cache false negative）。本輪 GO 門檻為 **check_paths.py ≤ 247 ERROR + 無 regression**（接受 NEW_REQ_9 既有 baseline debt 推 10th master）。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第九輪 master Round 2 NO-GO inline patch round 完成後 Round 3 重審」— 對 Round 2 inline patch 處理結果跑「R2-MAJOR-01/02 + R2-MINOR-01/02 全 RESOLVED 驗證 + R2-MAJOR-03 hard-limit accept ack + baseline 對齊」多重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 2 重審模式（CODEX_9TH_MASTER_ROUND2_REVIEW_REPORT v0.1 是 Round 2 baseline 列 3 MAJOR + 2 MINOR + 2 INFO；本輪 verify Round 2 inline patch round 處理後狀態）
- 對應前置：9th master Round 2 inline patch round 已完成 + commit/push（5 個檔範圍）

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查）
- ✗ 不跑真實 /iterate-* / /scene-task / /dialogue-write / /qa 寫檔
- ✗ 不重審 D-001~D-054 拍板結論
- ✗ 不重審 Round 1 / Round 2 已 accepted finding（CRITICAL 0 + INFO；R10-MA-01 / R1-MA-02 設計拍板 a / R2-MAJOR-03 hard-limit accept 等）
- ✗ 不重審 R2-MAJOR-03（user 已明示 hard-limit accept；屬 NEW_REQ_9 既有 baseline debt 推 10th master；本輪 verify check_paths ≤ 247 即可，不要求 ≤ 240）
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec
- ✗ 不下新 D-NNN 拍板
- ✗ 不開 9th master patch round
- ✓ 可跑技術驗證命令
- ✓ 可建本 review report 1 個檔（_design/CODEX_9TH_MASTER_ROUND3_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定 — Round 2 inline patch 處理範圍）：**

依 POST_LOCK_PENDING v0.16 header note + Round 2 處理紀錄段：

### R2-MAJOR-01 — D5 /iterate-scene 邊界 block external_action_required

- `_design/CODEX_D5_STARTER.md` v0.2 → v0.3
- /iterate-scene D-053 block（原 line 241 附近）補 external_action_required phase_log 指示
- 對齊 /iterate-detailed-outline + D1-D4 一致 wording

驗證：跑 grep `external_action_required` 在 D5 starter；預期 ≥ 2 處（/iterate-detailed-outline + /iterate-scene 各 1 處）

### R2-MAJOR-02 — D5 line 76 + line 245 frontmatter wording

- D5 line 76 + line 245：「下游 8 欄」→「上游/靜態檔三欄：entities / depends_on / weight」
- 對齊 SPEC §5.2 + 06_a 場景索引模板.md 實際 frontmatter

驗證：跑 grep `下游 8 欄` 在 D5 starter；預期僅 supersede note 命中（非 active reference）

### R2-MAJOR-03 — baseline 247 hard-limit accept

- POST_LOCK_PENDING v0.16 header note + Round 2 處理紀錄段紀錄 hard-limit accept
- 教訓內化：master 跑 baseline 以 Windows 端為權威；sandbox 屬 noise 對照
- NEW_REQ_9 既有 baseline debt（27 模板 old-style filename reference）推 10th master

驗證：跑 check_paths.py 並對比 R2 baseline 247；預期 ≤ 247 ERROR（接受不變或略降；不要求降到 240）

### R2-MINOR-01 — D1/D2/D3 active 段舊檔名 sweep

- D1 line 139（indirect 反查表）：3 處 (05_a/05_b/06_a) 對齊「主線大綱模板 / 章節結構模板 / 場景索引模板」
- D2 line 97（indirect 反查表）：2 處 (05_c/06_a) 對齊「角色弧線表 / 場景索引模板」
- D3 line 69（indirect 反查表）：2 處 (05_a/06_a) 對齊
- D3 line 95（寫檔範圍）：1 處 (04_b) 對齊「關係變化時間線」
- D1/D2/D3 header v0.2 → v0.3

驗證：跑 grep `05_a_主線結構\.md|05_b_章節結構\.md|05_c_角色弧線\.md|06_scene_index/06_a_場景索引\.md|04_b_關係演化時間線` 限定 D1-D5 starter；預期 active reference 0 match（除 supersede note / 歷史 narrative）

### R2-MINOR-02 — D1/D2 create-character v0.4 sweep

- D1 line 292：create-character v0.3 → v0.4
- D2 line 180/205：create-character v0.3 → v0.4

驗證：跑 grep `create-character.*v0\.3` 限定 D1-D5 starter；預期 active reference 0 match（除歷史 narrative）

### Round 2 inline patch round 不動段（聲明）

以下檔本輪 **不動**（聲明 + 應由 Round 3 verify protected-area diff）：

- LOCKED spec / registries / scripts / 27 模板 / 00_protocol/{00_a~00_l 全部}（**包括 00_j — Round 2 沒動 00_j**）
- 既有 16 個 SKILL.md
- 第八輪 review reports + starter
- D054_DECISION_PACKAGE / PHASE_A/C_COMPLETION_REPORT / HANDOFF
- DECISIONS_LOG v2.0
- R1 階段已升版檔：00_k v0.2 / 08_a v0.4 / phase_b_review_log v0.6 / PHASE_B v1.4 / CODEX_B9_STARTER v0.5 / AGENTS.md / CLAUDE.md v0.3（Round 2 沒動）
- Round 1/2 review reports（屬 immutable history）

⚠ **Protected-area diff 檢查：** 任何 `HEAD~N..HEAD` 觸及上述聲明不動範圍 → 列為 R3-MA-XX

**9th master Round 2 inline patch 後預期 baseline（Windows 端權威）：**

- check_headers: 0 ERROR / ≤ 50 WARN / ≤ 165 files
- check_paths: **≤ 247 ERROR**（R2-MAJOR-03 hard-limit accept；NEW_REQ_9 既有 debt 不阻 9th master）
- build_repo_index: 0 ERROR (Windows 端權威)

---

# 2. 重審範圍與維度（4 維度 — 縮小 vs Round 1/2）

**維度 1 — R2-MAJOR-01/02 全 RESOLVED**

- 對 D5 starter v0.3 跑 grep `external_action_required`；預期 ≥ 2 處
- 對 D5 starter v0.3 line 76 + line 245 跑 verify：「上游/靜態檔三欄」wording 存在；「下游 8 欄」僅在 supersede note 命中

判定：PASS / PARTIAL / FAIL

**維度 2 — R2-MINOR-01/02 全 RESOLVED sweep**

- D1-D5 starter 跑 grep `04_b_關係演化時間線|05_a_主線結構\.md|05_b_章節結構\.md|05_c_角色弧線\.md|06_scene_index/06_a_場景索引\.md`；預期 0 active reference match
- D1-D5 starter 跑 grep `create-character.*v0\.3`；預期僅在 supersede note / 歷史 narrative / D1 line 292「v0.4 / v0.3 / v0.3 / v0.3 對齊」對應 row 命中（其中 v0.3 屬 create-relationship / create-outline / create-detailed-outline，正確）

判定：PASS / PARTIAL / FAIL

**維度 3 — baseline + regression + protected-area diff**

- 跑 check_headers.py / check_paths.py / build_repo_index
- check_paths 目標：≤ 247 ERROR（hard-limit accept R2-MAJOR-03 確立的新基準）
- `git diff HEAD~2..HEAD --name-status` — 對比 Round 2 inline patch round 變動清單（預期 5 檔範圍：D1/D2/D3/D5 starter + POST_LOCK_PENDING）

判定：PASS / PARTIAL / FAIL

**維度 4 — D-054 NEW_REQ_15 落地 + R2-MAJOR-03 hard-limit accept ack**

- D5 starter v0.3 內 D-054 落地核心邏輯仍對齊（06_a row 保留 + marker + per-scene 檔 frontmatter 3 欄 + phase_log split_to_file + NEW_REQ_15 trigger）
- POST_LOCK_PENDING v0.16 header note + Round 2 處理紀錄段對 R2-MAJOR-03 hard-limit accept 紀錄正當性
- HANDOFF_TO_10TH_MASTER 教訓內化 wording 存在於 POST_LOCK_PENDING v0.16

判定：PASS / PARTIAL / FAIL

---

# 3. Finding 嚴重度 + 判定門檻

- **CRITICAL**：R2 finding 沒 RESOLVED / 新 spec 衝突 / D-054 落地破壞
- **MAJOR**：R2 finding PARTIAL RESOLVED / 新 regression / protected-area diff
- **MINOR**：sweep 漏掉的 active stale
- **INFO**：observation

Finding ID 命名：`R3-<severity>-<NN>`

判定門檻：

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + 4 維度全 PASS + check_paths ≤ 247 ERROR + 0 protected-area diff → 9th master 進 Wave 13
- **NEAR-GO**：0 CRITICAL + ≤ 1 MAJOR + ≤ 3 MINOR → user 拍板 hard-limit accept
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR

# 4. 輸出格式

寫 1 個檔：`_design/CODEX_9TH_MASTER_ROUND3_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Round 3 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：R2-MAJOR-01/02 全 RESOLVED
# 3. 維度 2：R2-MINOR-01/02 全 RESOLVED sweep
# 4. 維度 3：baseline + regression + protected-area diff
# 5. 維度 4：D-054 落地對齊 + R2-MAJOR-03 hard-limit accept ack
# 6. Finding 總計表（R3-<severity>-<NN>）
# 7. 決策判定 + Rationale
# 8. 給 9th master 的建議
# 9. Cross-ref
```

# 5. 起跑命令

```bash
cd /sessions/<your_session>/mnt/劇本開發工具
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']))"
git log --oneline -5
git diff HEAD~2..HEAD --name-status
```

grep verify：
```bash
grep -n "external_action_required" _design/CODEX_D5_STARTER.md
grep -n "下游 8 欄" _design/CODEX_D5_STARTER.md
grep -rn "04_b_關係演化時間線\|05_a_主線結構\.md\|05_b_章節結構\.md\|05_c_角色弧線\.md\|06_scene_index/06_a_場景索引\.md" _design/CODEX_D[1-5]_STARTER.md
grep -rn "create-character.*v0\.3" _design/CODEX_D[1-5]_STARTER.md
```

⚠ 排除歷史 narrative / supersede note 段

# 6. Cross-ref

- `_design/CODEX_9TH_MASTER_ROUND2_REVIEW_REPORT.md` v0.1（Round 2 NO-GO baseline）
- `_design/CODEX_9TH_MASTER_ROUND2_REVIEW_STARTER.md` v0.1
- `_design/POST_LOCK_PENDING.md` v0.16（Round 2 處理紀錄 + R2-MAJOR-03 hard-limit accept）
- `_design/CODEX_D1_STARTER.md` v0.3 ~ `CODEX_D5_STARTER.md` v0.3（維度 1/2 verify 對象）
- `_design/SPEC.md` v1.2 §5.2（R2-MAJOR-02 frontmatter wording 對齊依據）
- `06_scene_index/06_a_場景索引模板.md`（R2-MAJOR-02 實際 frontmatter 參考）
