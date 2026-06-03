狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：第九輪 master Round 3 NEAR-GO trivial inline patch 完成後 Round 4 重審 — R3-MAJOR-01 RESOLVED 驗證 + 無新 regression + 進 Wave 13 GO 確認  
優先級：高

# CODEX_9TH_MASTER_ROUND4_REVIEW_STARTER — Round 4 重審

# 0. 本檔用途

第九輪 master 流程：cleanup queue → Wave 12 → Round 1 NO-GO → Round 1 inline patch → Round 2 NO-GO → Round 2 inline patch → Round 3 NEAR-GO (1 MAJOR R3-MAJOR-01) → **Round 3 trivial wording inline patch 完成** → **本輪 Round 4 重審驗證 R3-MAJOR-01 RESOLVED + 進 Wave 13 GO 確認**。

**前置條件：** 9th master Round 3 trivial inline patch 完成 + user commit/push。

**重審 GO →** 9th master 進 Wave 13（採新模式：master 寫 D6 完整 + CODEX batch 寫 D7-D9）

**重審 NEAR-GO / NO-GO →** 出乎意料；繼續 inline patch 或 hard-limit accept

⚠ **Scope 極度縮小：本輪 verify Round 3 inline patch 範圍 ONLY（D5 + POST_LOCK_PENDING 兩檔）。**

⚠ **Baseline gate：** 沿用 Round 3 hard-limit accept — check_paths ≤ 247 ERROR；不重審 R2-MAJOR-03。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第九輪 master Round 3 NEAR-GO trivial inline patch 完成後 Round 4 重審」— 對 Round 3 inline patch 處理結果跑「R3-MAJOR-01 RESOLVED 驗證 + 無新 regression + 進 Wave 13 GO 確認」多重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 3 重審模式縮小（CODEX_9TH_MASTER_ROUND3_REVIEW_REPORT v0.1 是 Round 3 baseline 列 1 MAJOR；本輪 verify Round 3 trivial inline patch 後狀態）
- 對應前置：9th master Round 3 trivial inline patch 已完成 + commit/push（2 個檔範圍）

**重要邊界（極度嚴格 scope）：**

- ✗ 不改任何檔（純檢查）
- ✗ 不跑真實 /iterate-* / /scene-task / /dialogue-write / /qa 寫檔
- ✗ 不重審 D-001~D-054 拍板結論
- ✗ 不重審 Round 1 / Round 2 / Round 3 已 accepted finding（R10-MA-01 / R1-MA-02 設計拍板 a / R2-MAJOR-03 hard-limit accept / R3 INFO 等）
- ✗ 不重審 R2-MAJOR-03（hard-limit accept；屬 NEW_REQ_9 baseline debt；本輪 verify check_paths ≤ 247 即可）
- ✗ 不重審 R1-MA-01/02/03 / R1-MI-01~07（Round 2 已 verify RESOLVED）
- ✗ 不重審 R2-MAJOR-01/02 / R2-MINOR-01/02（Round 3 已 verify RESOLVED）
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec
- ✗ 不下新 D-NNN 拍板
- ✓ 可跑技術驗證命令
- ✓ 可建本 review report 1 個檔（_design/CODEX_9TH_MASTER_ROUND4_REVIEW_REPORT.md v0.1）

**本 task scope（極度縮小 — Round 3 inline patch 處理範圍 = 2 個檔）：**

依 POST_LOCK_PENDING v0.17 header note + Round 3 處理紀錄段：

### R3-MAJOR-01 — D5 line 76 + line 245 + header note wording

- `_design/CODEX_D5_STARTER.md` v0.3 → v0.4
- line 76 / line 245 / header note：拿掉「下游 8 欄」精確詞串
- 改為具體 7+1 欄位列舉（pipeline_state / mode_tag / qa_decision / qa_type / source_task / source_dialogue / source_dialogues / scene_id）
- header note 也避用「下游 8 欄」字串

驗證：跑 grep `下游 8 欄` 在 D5 starter；預期 **0 matches**（含 header note + line 76/245 + 任何位置）

### R3 後 POST_LOCK_PENDING 紀錄

- `_design/POST_LOCK_PENDING.md` v0.16 → v0.17
- 加 Round 3 處理紀錄段（R3-MAJOR-01 row）
- 加教訓內化第 4 條（避免 supersede note 重複 finding 內精確詞串）
- 紀錄 Round 3 NEAR-GO 視為 GO 條件（依 user 拍板路徑）

驗證：POST_LOCK_PENDING v0.17 header note 含 R3-MAJOR-01 紀錄；§Round 3 處理紀錄段存在；教訓內化第 4 條存在

### Round 3 inline patch round 不動段（聲明）

以下檔本輪 **不動**：

- LOCKED spec / registries / scripts / 27 模板 / 00_protocol/全部
- 既有 16 個 SKILL.md
- 所有第八輪 review reports + starter
- D054_DECISION_PACKAGE / PHASE_A/C_COMPLETION_REPORT / HANDOFF
- DECISIONS_LOG v2.0
- R1/R2 階段已升版檔（00_k v0.2 / 08_a v0.4 / phase_b_review_log v0.6 / PHASE_B v1.4 / CODEX_B9_STARTER v0.5 / AGENTS.md / CLAUDE.md v0.3 / 00_j v0.2 / D1/D2/D3 starter v0.3）
- Round 1/2/3 review reports（屬 immutable history）

⚠ **Protected-area diff 檢查：** 任何 `HEAD~N..HEAD` 觸及上述聲明不動範圍 → 列為 R4-MA-XX

**9th master Round 3 trivial inline patch 後預期 baseline（Windows 端權威）：**

- check_headers: 0 ERROR / ≤ 50 WARN / ≤ 170 files
- check_paths: **≤ 247 ERROR**（hard-limit accept R2-MAJOR-03 維持）
- build_repo_index: 0 ERROR (Windows 端權威)

---

# 2. 重審範圍與維度（3 維度 — 極度縮小）

**維度 1 — R3-MAJOR-01 RESOLVED**

對 D5 starter v0.4 跑 grep `下游 8 欄`；預期 0 matches。

判定：PASS / PARTIAL / FAIL

**維度 2 — baseline + regression + protected-area diff**

- 跑 check_headers.py / check_paths.py / build_repo_index
- check_paths 目標：≤ 247 ERROR
- `git diff HEAD~2..HEAD --name-status` — 對比 Round 3 inline patch 變動清單（預期 2 檔範圍 + 可能 1 個 Round 4 starter）
- protected-area diff PASS

判定：PASS / PARTIAL / FAIL

**維度 3 — POST_LOCK_PENDING v0.17 處理紀錄 + 教訓內化第 4 條對齊**

- POST_LOCK_PENDING v0.17 含 Round 3 處理紀錄段 (R3-MAJOR-01 row)
- 教訓內化第 4 條存在
- Round 3 NEAR-GO 視為 GO 條件紀錄存在

判定：PASS / PARTIAL / FAIL

---

# 3. Finding 嚴重度 + 判定門檻

- **CRITICAL**：R3-MAJOR-01 沒 RESOLVED / 新 spec 衝突 / 新 regression
- **MAJOR**：R3-MAJOR-01 PARTIAL RESOLVED / protected-area diff
- **MINOR**：邊緣 cross-ref 偏差
- **INFO**：observation

Finding ID 命名：`R4-<severity>-<NN>`

判定門檻：

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + 3 維度全 PASS + check_paths ≤ 247 ERROR + 0 protected-area diff → **9th master 進 Wave 13**
- **NEAR-GO**：0 CRITICAL + ≤ 1 MAJOR → user 拍板 hard-limit accept
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR

# 4. 輸出格式

寫 1 個檔：`_design/CODEX_9TH_MASTER_ROUND4_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Round 4 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：R3-MAJOR-01 RESOLVED
# 3. 維度 2：baseline + regression + protected-area diff
# 4. 維度 3：POST_LOCK_PENDING v0.17 + 教訓內化
# 5. Finding 總計表（R4-<severity>-<NN>）
# 6. 決策判定 + Rationale
# 7. 給 9th master 的建議（GO → 進 Wave 13 / NEAR-GO → hard-limit / NO-GO → 路徑）
# 8. Cross-ref
```

# 5. 起跑命令

```bash
cd /sessions/<your_session>/mnt/劇本開發工具
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']))"
git log --oneline -5
git diff HEAD~2..HEAD --name-status
grep -n "下游 8 欄" _design/CODEX_D5_STARTER.md
```

# 6. Cross-ref

- `_design/CODEX_9TH_MASTER_ROUND3_REVIEW_REPORT.md` v0.1（Round 3 NEAR-GO baseline）
- `_design/CODEX_9TH_MASTER_ROUND3_REVIEW_STARTER.md` v0.1
- `_design/POST_LOCK_PENDING.md` v0.17（Round 3 處理紀錄 + 教訓內化第 4 條）
- `_design/CODEX_D5_STARTER.md` v0.4（R3-MAJOR-01 verify 對象）
