狀態：DRAFT  
版本：v0.1（9th master 第三段對話 Wave 16 Step 3 — Phase D 最終 milestone CODEX review starter）  
最後更新：2026-05-22  
適用範圍：第九輪 master 第三段對話 Wave 16 Step 3 — Phase D 整體驗收最終重審；對 PHASE_D_COMPLETION_REPORT v1.0 + Wave 14 4 個 /export-* + Wave 15 /diagnose + /integrate + CANON_DELTA_FRAMEWORK v0.1 + CODEX_D_FINAL_STARTER v0.1 + PART3 handoff 全 scope 4 維度重審  
優先級：高

# CODEX_D_FINAL_REVIEW_STARTER — Phase D 最終 milestone CODEX review starter

# 0. 本檔用途

9th master 對話進行流程：第一段（Wave 12 starter + Round 1-4 review cycle + Wave 13）→ 第二段（Wave 14 + Wave 15 + Wave 16 Step 1-2 PHASE_D_COMPLETION_REPORT v1.0 落地）→ **本輪：第三段 Wave 16 Step 3 — 跑 CODEX 對 Phase D 全 scope 做最終 milestone 重審**。

本 review 是 Milestone 4 接近條件聲明前的最後守門關卡。9th master 第二段對話 Wave 14/15 採 master 端內部 verify（grep 結構 + Read 重點 section）跳過 CODEX review starter；Wave 16 因屬最終 milestone，動用完整 CODEX 4 維度重審（依 HANDOFF_9TH_MASTER_CONTINUATION v1.0 §4.5 第二段建議）。

**重審 GO →** 9th master 第三段對話進 Wave 16 Step 4（finding 處理 + Milestone 4 接近條件聲明確認）+ 寫 HANDOFF_TO_10TH_MASTER.md v1.0

**重審 NEAR-GO →** master 拍板 hard-limit accept 或 inline patch（沿用 Round 1-4 cycle 處理模式）

**重審 NO-GO →** master 端 patch round（依嚴重度決定 scope）

**前置條件（第二段對話結束時實際 git 狀態 — 2026-05-22 14:00 範圍快照）：**

| ref | HEAD commit | 含 Wave 14 SKILL.md | 含 Wave 15 SKILL.md | 含 PHASE_D_COMPLETION_REPORT | 備註 |
|---|---|---|---|---|---|
| `master` / `origin/master` | `140af34` | ✓ 含 (b94f741 / bd0920d) | ✗ 不含（在 d6ec085；frontend-tools-a0f only）| ✗ 不含（在 499bc13；frontend-tools-a0f only）| Wave 15 starters + CANON_DELTA_FRAMEWORK 已到 master；SKILL.md 與 PHASE_D report 未 cherry-pick 到 master |
| `frontend-tools-a0f` | `1735d0a` | ✓ 含 | ✓ 含 (d6ec085) | ✓ 含 (499bc13) | 9th master 第二段對話收尾 + Phase A.0F.3-A.0F.11 平行對話 + audit cycle 全在此 branch |

**重要：** PART3 handoff §1 寫「第二段對話結束前 user 已執行 cherry-pick；確認 master 含 4 個 Wave 15 SKILL.md」— 此假設**尚未 verify**；本 review 維度 3 必須以 `git log master --oneline -10` + `git show 140af34 --stat` 為事實基準確認真實狀態。若 cherry-pick 未發生 → Finding 1 維持 ⏳ pending（推 Wave 16 Step 4 處理）+ 本 review 改以 frontend-tools-a0f branch 為驗收 ref（沿用 PHASE_D_COMPLETION_REPORT v1.0 §1 caveat wording）。

⚠ **教訓 5 條內化（9th master 第一段 + 第二段）：**
1. **Windows baseline 權威** — sandbox virtiofs cache 屬 noise 對照
2. **Cascade sweep broader pattern** — grep 全 `_design/` 看 stale；不只看 review 列具體 hits
3. **SPEC frontmatter 段直接 grep verify** — 不憑記憶
4. **Supersede note 避重複 finding 內精確詞串** — 用「修補性質」描述
5. **Review starter diff anchor 必須精確** — 本 starter 用**明示 commit hash**（6 個第二段 Wave 14/15/16 落地 commit），不用 `HEAD~N..HEAD`；排除介於其中的 989de19 (Phase A.0F.5) commit（屬 Phase A.0F 平行對話 scope；不在本 review 範圍）

⚠ **新紀律（9th master 第二段對話內化）：**
6. **寫長 multi-byte 檔請用 Python script via bash 或 cat heredoc** — 不用 Write/Edit tool（避截斷風險）
7. **Cloud sync / 防毒不得監控 working tree** — `D:\劇本開發工具` 必須加白名單；若發現 `.git/*.lock` + `.lock.tmp` + `HEAD.lock` 反覆出現 → 立刻暫停 cloud sync + 防毒實時掃描

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「9th master 第三段對話 Wave 16 Step 3 — Phase D 最終 milestone 重審」— 對 Wave 14 + Wave 15 + Wave 16 Step 1-2 + Wave 12 starter set + CANON_DELTA_FRAMEWORK + L3 schema 對齊備忘做完整 4 維度重審，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 frontend-tools-a0f 分支上（master 尚未 cherry-pick Wave 15 SKILL.md + PHASE_D_COMPLETION_REPORT；屬 Finding 1 pending；本 review 以 frontend-tools-a0f 為驗收 ref）。

**Token 不是限制** — 如需可 spawn 多個次要 CODEX 對話分工 verify Wave 12 / 13 / 14 / 15 各自落地狀態 / 跑 baseline / grep frontmatter 對齊 SPEC §5.2 / 對照 D-054 hybrid fallback 一致性，再回主對話彙整撰寫 review report。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 9th master 第一段 Round 1-4 review cycle + Wave 13 review pattern，但 scope 限縮到 Phase D 整體最終 milestone；對 PHASE_D_COMPLETION_REPORT v1.0 + Wave 14/15 SKILL.md + CANON_DELTA + CODEX_D_FINAL_STARTER + PART3 handoff 6 個 commit 範圍做 strict verify
- 對應前置：9th master 第二段對話已落地 Wave 14（4 export-* + 4 wrapper）+ Wave 15（/diagnose + /integrate + 2 wrapper + CANON_DELTA_FRAMEWORK）+ Wave 16 Step 1-2（CODEX_D_FINAL_STARTER + PHASE_D_COMPLETION_REPORT）；第二段對話內部 verify 跳過 CODEX review starter；本輪補回最終 milestone 完整 CODEX review

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report）
- ✗ 不跑真實 /view-* / /export-* / /diagnose / /integrate / /iterate-* 寫檔（Template 內無 Instance entity；端到端測試屬 user 親跑 M4 chain）
- ✗ 不重審 D-001~D-054 拍板結論（含 D-050 / D-052 / D-053 / D-054）
- ✗ 不重審 9th master 第一段 Round 1-4 review cycle 已 accepted finding（R10-MA-01 / R1-MA-02 / R2-MAJOR-03 hard-limit accept / R4-MAJOR-01 hard-limit accept / R-W13-* 等）
- ✗ 不重審 9th master 第二段 Wave 14/15 內部 verify 已 PASS finding
- ✗ 不重審 cleanup queue (Task 1-6) / Wave 12 starter set (Task 7) 落地（屬 Round 1-4 cycle 範圍）
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec
- ✗ 不重審 Phase A.0F.3 ~ A.0F.11 前端工具 commit（屬 Phase A.0F 平行對話 scope；diff anchor 已排除 989de19 + 後續 A.0F commit）
- ✗ 不擅自實作 Wave 12 缺漏的 6 個 SKILL.md（屬 10th master scope）
- ✗ 不擅自寫 HANDOFF_TO_10TH_MASTER.md（屬本 review PASS 後 master 寫的另一個 task）
- ✗ 不擅自改 AGENTS.md / CLAUDE.md Phase D metadata（屬 PHASE_D_COMPLETION_REPORT v1.0 §8 Finding 2 推 10th master cleanup queue）
- ✗ 不下新 D-NNN 拍板（如有新議題 → 列在 review report §10「待 10th master 評估」）
- ✓ 可跑技術驗證命令
- ✓ 可建本 review report 1 個檔（`_design/CODEX_D_FINAL_REVIEW_REPORT.md` v0.1）

**本 task scope（嚴格限定 — Phase D 整體 最終 milestone）：**

依 9th master 第二段對話 Wave 14 + Wave 15 + Wave 16 Step 1-2 落地的 6 個 commit + Wave 12 starter set 5 個 starter + 00_j 迭代協議 v0.2（屬 9th master 第一段已落地；本輪只 verify 落地狀態不重審結構）。

### 本輪 review 對象（6 個 commit + Wave 12 starter set）

| # | commit | wave / task | 寫入檔案 | 落地狀態 |
|---|---|---|---|---|
| 1 | `f17d567` | Wave 14 starters | `_design/CODEX_D10_STARTER.md` v0.1 + `_design/CODEX_D_EXPORT_BATCH_STARTER.md` v0.1 | ✓ master |
| 2 | `bd0920d` | Wave 14 D.10 SKILL.md | `.claude/skills/export-world/SKILL.md` v0.1 + `.claude/skills/匯出世界觀/SKILL.md` v0.1 | ✓ master |
| 3 | `b94f741` | Wave 14 batch D11-D13 SKILL.md | `.claude/skills/export-character/SKILL.md` + `.claude/skills/export-outline/SKILL.md` + `.claude/skills/export-detailed-outline/SKILL.md` + 3 中文 wrapper | ✓ master |
| 4 | `140af34` | Wave 15 starters + CANON_DELTA | `_design/CODEX_D14_STARTER.md` v0.1 + `_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` v0.1 + `_design/CANON_DELTA_FRAMEWORK.md` v0.1 | ✓ master (HEAD) |
| 5 | `d6ec085` | Wave 15 SKILL.md | `.claude/skills/diagnose/SKILL.md` v0.1 + `.claude/skills/integrate/SKILL.md` v0.1 + `.claude/skills/診斷/SKILL.md` + `.claude/skills/整理/SKILL.md` | ⚠ frontend-tools-a0f only；master 未 cherry-pick |
| 6 | `499bc13` | Wave 16 Step 1-2 | `_design/CODEX_D_FINAL_STARTER.md` v0.1 + `_design/PHASE_D_COMPLETION_REPORT.md` v1.0 + `_design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md` v1.0 | ⚠ frontend-tools-a0f only；master 未 cherry-pick |

**Wave 12 starter set 範圍（屬 9th master 第一段已落地；本輪 verify 落地狀態 only）：**

| # | path | 版本 | 落地狀態 |
|---|---|---|---|
| 7 | `_design/CODEX_D1_STARTER.md` | v0.3 | ✓ 已落地（第一段）|
| 8 | `_design/CODEX_D2_STARTER.md` | v0.3 | ✓ 已落地 |
| 9 | `_design/CODEX_D3_STARTER.md` | v0.3 | ✓ 已落地 |
| 10 | `_design/CODEX_D4_STARTER.md` | v0.2 | ✓ 已落地 |
| 11 | `_design/CODEX_D5_STARTER.md` | v0.4 | ✓ 已落地 |
| 12 | `00_protocol/00_j_迭代協議.md` | v0.2 | ✓ 已落地 |

⚠ Wave 12 SKILL.md（6 個 /iterate-* + /iterate-scene + 5 中文 wrapper = 11 檔）**尚未實作**；屬 10th master scope。本 review 維度 2 必須明示這個 deferred 狀態 + 不擅自實作。

### Phase D 整體 review 不動段（聲明）

以下檔本輪 **不動**（聲明 + 應由本輪 verify protected-area diff）：

- LOCKED spec / registries / scripts / 27 模板 / 00_protocol/全部 (含 00_j v0.2 / 00_k v0.2 / 00_a)
- Phase A/B/C 既有 16 個 SKILL.md（含 /init-project / /create-* / /scene-task / /dialogue-write / /qa + 中文 wrapper）
- Wave 13 已落地 8 個 view-* SKILL.md（屬 9th master 第一段；本輪不重審）
- Round 1-4 已落地檔（POST_LOCK_PENDING v0.18 / DECISIONS_LOG v2.0 / AGENTS.md / CLAUDE.md v0.3）
- 9th master 第一段 review reports (Round 1-4 + Wave 13)（屬 immutable history）
- D054_DECISION_PACKAGE / PHASE_A/B/C_COMPLETION_REPORT / HANDOFF_TO_9TH_MASTER
- Phase A.0F.3 ~ A.0F.11 commit（屬 Phase A.0F 平行對話 scope；diff anchor 排除）

⚠ **Protected-area diff 檢查（沿用第 5 條教訓 — 用明示 commit hash 6 個 + path filter）：**

````bash
for h in f17d567 bd0920d b94f741 140af34 d6ec085 499bc13; do
  echo "=== $h ==="
  git show $h --stat
done
````

任何觸及上述「不動段」範圍 → 列為 `R-W16-F-MA-XX`

**Phase D 後預期 baseline（Windows 端權威）：**

- check_headers: 0 ERROR / ≤ 50 WARN / ≤ 174 files（PHASE_D_COMPLETION_REPORT v1.0 + PART3 handoff +2 檔）
- check_paths: **≤ 247 ERROR**（hard-limit accept R2-MAJOR-03；屬 NEW_REQ_9 既有 baseline debt 推 10th master）
- build_repo_index: 0 ERROR / WARN allowed / perf < 5s

---

# 2. 重審範圍與維度（4 維度對齊 PHASE_D_COMPLETION_REPORT v1.0 4 維度）

## 維度 1 — PHASE_D_COMPLETION_REPORT v1.0 內容嚴謹度 + 9 段結構齊全

對 `_design/PHASE_D_COMPLETION_REPORT.md` v1.0 跑 strict structural verify：

**A. 9 段結構齊全（對齊 CODEX_D_FINAL_STARTER §B.PHASE_D 9 段結構 + PHASE_C_COMPLETION_REPORT v1.0 pattern）：**

1. §0 文件目的（含 PHASE_C/B/A 同 pattern + 本檔特殊性：Wave 12 partial + Milestone 4 接近條件非達成）
2. §1 驗收摘要（4 維度表 + repo SHA + 驗收日期 + repo 性質 + 寫檔範圍 + Milestone 4 接近條件達成宣告）
3. §2 維度 1：技術驗證（baseline 表 + 紀律 5 條對齊 PHASE_C §2 pattern）
4. §3 維度 2：Wave 12-15 review consolidation（4 個 sub-section §3.1-§3.4）
5. §4 維度 3：Phase D 整體鏈驗收（§4.1-§4.4）
6. §5 維度 4：Canon Delta + L3 schema + Phase D 啟動條件
7. §6 端到端測試 placeholder + NEW_REQ_14 AI-assisted 機制
8. §7 Phase D 完成聲明（4 維度 PASS + Milestone 4 接近條件達成 + 真正達成 ⏳ 未達成）
9. §8 10th master 啟動條件聲明 + 接手 scope 表 + 需要 master 拍板議題
10. §9 Cross-ref

**B. 4 維度宣告嚴謹度：**

- 維度 1（技術驗證）：check_headers 0 ERROR / check_paths ≤ 247 ERROR（hard-limit accept R2-MAJOR-03）/ build_repo_index 0 ERROR / expected_entities.yaml 存在
- 維度 2（Wave 12-15 review consolidation）：Wave 12 partial / Wave 13/14/15 落地 PASS 描述精確
- 維度 3（Phase D 整體鏈驗收）：英文主檔 10 個落地 + 中文 wrapper 10 個落地 + Wave 12 6 SKILL.md + 5 wrapper deferred 明示
- 維度 4（Canon Delta + L3 schema + Phase D 啟動條件）：framework reference / 對齊備忘 / 啟動條件 8 項表

**C. §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制（沿用 PHASE_C pattern）：**

- 9 步 M4 chain 表完整（W/V/C/R/P/CH/S prerequisites → /view-* → /export-* → /diagnose → /integrate → /iterate-* placeholder → /status + /check-gaps）
- 「user 親跑結果待補」標示完整
- NEW_REQ_14 5 步驟流程紀錄

**D. §7 + §8 wording 嚴謹度（關鍵）：**

- 嚴守「Milestone 4 接近條件達成 ≠ Milestone 4 真正達成」 wording
- 真正達成原因列 3 項：Wave 12 SKILL.md 待實作 / Phase A.0F 補完 / master ref 對齊
- §8 三 finding 覆蓋（Finding 1 master ref / Finding 2 metadata drift / Finding 3 Wave 12 排序）
- §8 10th master 接手 scope 表完整（A/B/C/D/E/F）

判定：PASS / PARTIAL / FAIL；列任何漏段 / wording 偏離。

## 維度 2 — Wave 14/15 SKILL.md 落地對齊 starter set + 邊界紀律

### A. Wave 14 4 個 /export-* SKILL.md + 4 中文 wrapper（共 8 檔）

對以下 4 個英文主檔 + 4 個中文 wrapper 跑 grep + 結構 verify：

- `.claude/skills/export-world/SKILL.md` v0.1 + `.claude/skills/匯出世界觀/SKILL.md` v0.1
- `.claude/skills/export-character/SKILL.md` v0.1 + `.claude/skills/匯出角色/SKILL.md` v0.1
- `.claude/skills/export-outline/SKILL.md` v0.1 + `.claude/skills/匯出大綱/SKILL.md` v0.1
- `.claude/skills/export-detailed-outline/SKILL.md` v0.1 + `.claude/skills/匯出細綱/SKILL.md` v0.1

預期含 11 段結構（對齊 CODEX_D10_STARTER §3 範本）：
1. `## 用途`
2. `## 觸發語`
3. `## 觸發協議`（指向 ARCH §4.2 + §4.4；無 00_protocol/ 對應）
4. `## 啟動前檢查`
5. `## 流程`（5 階段：診斷 / 反查 source / 組合 / 寫檔 view/<entity>.md / 驗證）
6. `## 呈現規則`（DERIVED 7 欄 / breadcrumb / 條件 TOC > 200 行 / 末尾返回連結 / source italic / GFM slug 驗證）
7. `## .protocol_version 寫入規範`（phase_log entry 含 output_path + output_lines + breadcrumb_added + toc_added + slug_validation_result）
8. `## 輸入`
9. `## 輸出`（寫檔 `<instance_root>/view/<entity>.md`；DERIVED 整合檔）
10. `## 邊界`（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表）
11. `## 錯誤處理 / Rollback`

**特別 verify：**

- 4 個英文主檔含 DERIVED frontmatter 7 欄完整描述（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級 / 生成方式 / 組合來源）
- `export-detailed-outline/SKILL.md` 含 **D-054 hybrid fallback 完整 3 Phase**（Phase 1 per-scene first / Phase 2 aggregate 06_a fallback / Missing handling；對齊 `scene-task/SKILL.md` 既有範本）
- 4 個中文 wrapper 採極簡模式（指向英文主檔為權威；不重複大段 substantive）
- 4 個英文主檔 frontmatter `name` 對齊 directory name
- §4.2a Layer 3 Export A1 prompt 生成器**明示不實作**（屬 Phase A.0F.x / 10th master scope）

### B. Wave 15 /diagnose + /integrate SKILL.md + 2 中文 wrapper（共 4 檔）

對以下 2 個英文主檔 + 2 個中文 wrapper 跑 grep + 結構 verify：

- `.claude/skills/diagnose/SKILL.md` v0.1 + `.claude/skills/診斷/SKILL.md` v0.1
- `.claude/skills/integrate/SKILL.md` v0.1 + `.claude/skills/整理/SKILL.md` v0.1

**/diagnose 對齊 00_a §3.3 診斷模式：**
- 6 段診斷報告格式對齊 §3.3.4（作品類型與敘事氣質 / 世界語言與台詞風格推測 / 目前資料可確認 / 不可確認或需人類確認 / 通用規則適配性 / 建議下一步）
- 三種使用模式（Mode A scan_all / Mode B file_path / Mode C inline_text）
- 純讀取邊界 8 條（D6 7 條 + §3.3.3 5 條延伸）
- phase_log optional audit 預設不寫
- 不自動觸發 /integrate 或其他 skill

**/integrate 對齊 00_a §3.4 整理模式：**
- Stage 1-4a read-only / Stage 4a 印 diff preview only
- Stage 4b 必須等 user 對每個 entry 明示「採」或「修改後採」後才寫檔
- target 必填；不接受 broad "scan and integrate everything"
- 邊界四 block（D-050 三 + D-052 AI-assisted 紀律精神）
- D-054 hybrid 維持 aggregate 06_a 預設；不擅自 split-to-file（屬 Wave 12 future）

### C. Wave 12 SKILL.md partial 狀態 verify

⚠ **本維度 sub-task 不擅自實作 Wave 12 SKILL.md**；只 verify 以下 6 檔**不存在**：

- `.claude/skills/iterate-world/SKILL.md` ✗ 不存在（待 10th master）
- `.claude/skills/iterate-character/SKILL.md` ✗ 不存在
- `.claude/skills/iterate-relationship/SKILL.md` ✗ 不存在
- `.claude/skills/iterate-outline/SKILL.md` ✗ 不存在
- `.claude/skills/iterate-detailed-outline/SKILL.md` ✗ 不存在
- `.claude/skills/iterate-scene/SKILL.md` ✗ 不存在
- 5 中文 wrapper（迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱）✗ 不存在

若任一檔存在 → `R-W16-F-CR-XX`（屬越界實作）。

判定：PASS / PARTIAL / FAIL；列任何結構漏段 / DERIVED 7 欄不齊 / D-054 hybrid 不完整 / 越界實作。

## 維度 3 — master ref 對齊狀態 + baseline + protected-area diff + repo 性質

### A. master ref 對齊狀態（Finding 1 真相確認）

跑以下命令以實際 git 狀態為準：

````bash
git log master --oneline -10
git log frontend-tools-a0f --oneline -20
git log origin/master --oneline -5
git show master --stat | head -3
````

對照 PART3 handoff §1 + PHASE_D_COMPLETION_REPORT v1.0 §1 描述：

| 描述位置 | 內容 | 實際 git 狀態 |
|---|---|---|
| PART3 handoff §1 task 2 Finding 1 | 「第二段對話結束前 user 已執行 cherry-pick；確認 master 含 4 個 Wave 15 SKILL.md」| ⏳ 待 verify |
| PHASE_D_COMPLETION_REPORT v1.0 §1 | current checkout SHA `e4721e9...`；fetched master / origin/master SHA `140af34...` | ⏳ 待 verify |
| PHASE_D_COMPLETION_REPORT v1.0 §1 caveat | 「需 master 端確認後續 merge / ref 對齊」| ⏳ 待 verify |

**判定要求：**

- 若 `master` HEAD = `140af34`（**不含** Wave 15 SKILL.md + PHASE_D_COMPLETION_REPORT）→ Finding 1 維持 ⏳ pending；本 review 改以 `frontend-tools-a0f` branch 為驗收 ref；列為 `R-W16-F-INFO-XX`（PART3 handoff §1 的 cherry-pick 假設未實現；推 Wave 16 Step 4 由 master 主導 cherry-pick 或正式 merge plan）
- 若 `master` HEAD ≠ `140af34` 但**已含** Wave 15 SKILL.md（d6ec085 + 同等 commit）→ Finding 1 RESOLVED；本 review 直接以 master 為驗收 ref
- 若 `master` HEAD 已含 d6ec085 但**未含** 499bc13（PHASE_D_COMPLETION_REPORT 仍在 frontend-tools-a0f）→ partial cherry-pick；列為 `R-W16-F-MA-XX`（master ref 部分對齊 — 須 master 拍板 follow-up plan）

### B. baseline + regression

技術驗證（用 frontend-tools-a0f branch 為基準，因 master 可能未 cherry-pick）：

````bash
python -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
python -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']), 'WARN:', len([i for i in r.issues if i.severity == 'WARN']))"
````

baseline 門檻：

- check_headers: 0 ERROR / ≤ 50 WARN（PHASE_D_COMPLETION_REPORT v1.0 + PART3 handoff +2 檔可能 +1-2 WARN 屬既有 markdown header 慣例）
- check_paths: **≤ 247 ERROR**（R2-MAJOR-03 hard-limit accept；屬 NEW_REQ_9 既有 baseline debt）
- build_repo_index: 0 ERROR

任何**新** baseline regression → `R-W16-F-MA-XX`

### C. protected-area diff 6 個 commit + path filter

用明示 6 個 commit hash + path filter（教訓 5）：

````bash
for h in f17d567 bd0920d b94f741 140af34 d6ec085 499bc13; do
  echo "=== $h ==="
  git show $h --name-status
done
````

預期變動範圍：

- f17d567：新建 `_design/CODEX_D10_STARTER.md` + `_design/CODEX_D_EXPORT_BATCH_STARTER.md`
- bd0920d：新建 `.claude/skills/export-world/SKILL.md` + `.claude/skills/匯出世界觀/SKILL.md`
- b94f741：新建 `.claude/skills/export-character/SKILL.md` + `.claude/skills/export-outline/SKILL.md` + `.claude/skills/export-detailed-outline/SKILL.md` + 3 中文 wrapper
- 140af34：新建 `_design/CODEX_D14_STARTER.md` + `_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` + `_design/CANON_DELTA_FRAMEWORK.md`
- d6ec085：新建 `.claude/skills/diagnose/SKILL.md` + `.claude/skills/integrate/SKILL.md` + `.claude/skills/診斷/SKILL.md` + `.claude/skills/整理/SKILL.md`
- 499bc13：新建 `_design/CODEX_D_FINAL_STARTER.md` + `_design/PHASE_D_COMPLETION_REPORT.md` + `_design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md`（+ 可能 `_tools/frontend/__cache_test.txt` / `__pycache__/server.cpython-310.pyc` 屬 sandbox cache 副作用，不阻 review）

任何觸及「不動段」範圍 → `R-W16-F-MA-XX`

### D. repo 性質聲明

- Template repo；不是 Instance
- 寫檔範圍只新增本 review report `_design/CODEX_D_FINAL_REVIEW_REPORT.md` v0.1
- 不跑真實 /view-* / /export-* / /diagnose / /integrate skill（會污染 Template）

判定：PASS / PARTIAL / FAIL

## 維度 4 — Canon Delta framework + L3 schema 對齊備忘 + 邊界 5 條 + cross-ref stale grep

### A. CANON_DELTA_FRAMEWORK v0.1 對齊 UD §5

對 `_design/CANON_DELTA_FRAMEWORK.md` v0.1 跑 grep + 結構 verify：

- 5 必填中文 header 齊全（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
- 8 個 sub-section 對齊 UD §5（5.1 識別 / 5.2 抽取演算法 / 5.3 提案流程 / 5.4 回寫執行 / 5.5 與既有實體互動 / 5.6 禁止事項 / 5.7 phase_log / 5.8 UI/UX 標記）
- 啟動條件 4 trigger 明示（A Milestone 4+6 個月 / B 工具 B 啟動 / C user 主動回報 / D 跟 NEW_REQ_16/17/18 自動化 QA 工具同步）
- 既有 Phase D /qa / /iterate-* / 09_e LOCKED 模板的關聯紀錄
- **明示「framework reference；不實作 skill」** — 不擴 09_e 模板 / 不擴 /iterate-* / 不自動抽取或回寫上游 Bible

### B. L3 Export schema 對齊備忘

對 `_design/CODEX_D10_STARTER.md` v0.1 §Z 跑 grep + 結構 verify：

- §Z.1 前端工具友好性紀律（breadcrumb / TOC / 返回連結 / GFM slug / DERIVED frontmatter 7 欄）
- §Z.2 L3 schema 對齊備忘（對齊 `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 §1.1 5 區塊）
- 兩條 export path 共存不取代（§4.2 4 個 /export-* skill → `view/<entity>.md`；§4.2a Layer 3 Export → `export/<instance>_<timestamp>.{json,md}`）
- **明示「不實作 L3 prompt generator；不擴 4 個 /export-* skill」** — 屬 Phase A.0F.x / 10th master scope

### C. 邊界 5 條完整明示（本 review 範圍紀律）

對 PHASE_D_COMPLETION_REPORT v1.0 §8（Phase D 完成聲明後續邊界）+ CODEX_D_FINAL_STARTER §B Wave 16 不允許 + PART3 handoff §0 / §4.6 跑邊界紀律 cross-check：

1. 不重做設計（D-001~D-054 LOCKED）
2. 不擅啟 Phase A.0F 實作（A.0F 平行對話 scope）
3. 不擅自實作 Wave 12 6 個 SKILL.md（10th master scope）
4. 不擅自啟動新 D-NNN 拍板（新議題列入 HANDOFF「待 10th 評估」）
5. 不擅自改 AGENTS.md / CLAUDE.md Phase D metadata（10th master cleanup queue）

任一邊界 wording 在 PHASE_D_COMPLETION_REPORT 或 PART3 handoff 內**缺失或偏離** → `R-W16-F-MA-XX`

### D. cross-ref stale grep 全掃

對 Wave 14/15/16 6 個 commit 範圍 + Wave 12 starter 5 個檔跑 stale pattern grep：

````bash
# 舊檔名 stale（屬 NEW_REQ_19 9th master cleanup queue 範圍）
grep -rn "01A_世界觀總覽\|01B_世界語言\|02A_專有名詞\|05D_資訊揭露\|04_b_關係演化時間線" \
  .claude/skills/export-*/ .claude/skills/diagnose/ .claude/skills/integrate/ \
  .claude/skills/匯出*/ .claude/skills/診斷/ .claude/skills/整理/ \
  _design/CODEX_D10_STARTER.md _design/CODEX_D_EXPORT_BATCH_STARTER.md \
  _design/CODEX_D14_STARTER.md _design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md \
  _design/CANON_DELTA_FRAMEWORK.md _design/CODEX_D_FINAL_STARTER.md \
  _design/PHASE_D_COMPLETION_REPORT.md _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md

# 版本 stale
grep -rn "POST_LOCK_PENDING.*v0\.\(9\|10\|11\|12\|13\|14\|15\|16\|17\)\|DECISIONS_LOG.*v1\.[0-9]\|TASKS.*v1\.[1-8]\|ARCH.*v1\.[1-5]" \
  .claude/skills/export-*/ .claude/skills/diagnose/ .claude/skills/integrate/ \
  .claude/skills/匯出*/ .claude/skills/診斷/ .claude/skills/整理/ \
  _design/CODEX_D10_STARTER.md _design/CODEX_D_EXPORT_BATCH_STARTER.md \
  _design/CODEX_D14_STARTER.md _design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md \
  _design/CANON_DELTA_FRAMEWORK.md _design/CODEX_D_FINAL_STARTER.md \
  _design/PHASE_D_COMPLETION_REPORT.md _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md

# stale skill 描述
grep -rn "5 份 QA\|五份 QA\|09_a-d\|09_a–09_d" \
  .claude/skills/export-*/ .claude/skills/diagnose/ .claude/skills/integrate/ \
  .claude/skills/匯出*/ .claude/skills/診斷/ .claude/skills/整理/
````

預期 0 active match（除 supersede note / 歷史 narrative 段）。任何 active match → `R-W16-F-MI-XX`（屬 NEW_REQ_19 cleanup queue 範圍；本 review 列示不擅自 patch）。

判定：PASS / PARTIAL / FAIL

---

# 3. Finding 嚴重度 + 判定門檻

**Finding ID 命名：** `R-W16-F-<severity>-<NN>`（F = Final milestone review）

**嚴重度定義：**

- **CRITICAL**：spec 違反 / SKILL.md frontmatter 不可用 / Wave 14/15 SKILL.md 未授權寫檔 / Milestone 4 wording 真誤 / 越界實作 Wave 12 SKILL.md
- **MAJOR**：9 段結構漏段 / 4 維度宣告不嚴謹 / master ref 對齊狀態 misreport / baseline 新 regression / protected-area diff mismatch / 邊界 5 條 wording 缺失或偏離 / 中文 5 header 不齊全
- **MINOR**：sweep 漏掉的 active stale / cross-ref 邊緣偏差 / wording polish / DERIVED 7 欄描述不完整 / phase_log entry 欄位漏列
- **INFO**：observation / 改善建議 / master ref 對齊 pending 紀錄

**判定門檻：**

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + 4 維度全 PASS + check_paths ≤ 247 ERROR + protected-area diff 限 6 commits scope → 9th master 第三段對話進 Wave 16 Step 4（finding 處理 + Milestone 4 接近條件聲明確認）+ HANDOFF_TO_10TH_MASTER.md v1.0 撰寫
- **NEAR-GO**：0 CRITICAL + ≤ 1 MAJOR + ≤ 3 MINOR → master 拍板 hard-limit accept 或 inline patch（沿用 Round 1-4 cycle 處理模式）
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR → master 端 patch round（依嚴重度決定 scope）

---

# 4. 輸出格式

寫 1 個檔：`_design/CODEX_D_FINAL_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Phase D 最終 milestone 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：PHASE_D_COMPLETION_REPORT v1.0 內容嚴謹度 + 9 段結構齊全
# 3. 維度 2：Wave 14/15 SKILL.md 落地對齊 starter set + 邊界紀律
# 4. 維度 3：master ref 對齊狀態 + baseline + protected-area diff + repo 性質
# 5. 維度 4：CANON_DELTA + L3 schema 對齊備忘 + 邊界 5 條 + cross-ref stale grep
# 6. Finding 總計表（R-W16-F-<severity>-<NN>；含 finding 描述 + evidence + 建議處理）
# 7. 決策判定 + Rationale（含對 PART3 handoff §1 Finding 1 真實狀態的觀察）
# 8. 給 9th master 第三段對話的建議（進 Wave 16 Step 4 / inline patch / hard-limit accept / patch round）
# 9. master ref 對齊 follow-up plan 建議（若 Finding 1 pending）
# 10. 待 10th master 評估議題（如有；不擅自下 D-NNN 拍板）
# 11. Cross-ref
```

**完成回報：**

CODEX 寫完 review report 後請回報：

- report 路徑：`_design/CODEX_D_FINAL_REVIEW_REPORT.md`
- 行數 / bytes
- 4 維度結果（PASS / PARTIAL / FAIL 個別宣告）
- Finding 總計（CRITICAL / MAJOR / MINOR / INFO 各 NN 個）
- 判定（GO / NEAR-GO / NO-GO）
- master ref 對齊狀態（Finding 1 RESOLVED / partial / pending）
- baseline 跑後結果（check_headers + check_paths + build_repo_index）
- 是否有需要 master 拍板的議題
- 建議下一步（進 Wave 16 Step 4 / master inline patch / patch round）

---

# 5. 起跑命令

````bash
cd /sessions/<your_session>/mnt/劇本開發工具

# baseline
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']), 'WARN:', len([i for i in r.issues if i.severity == 'WARN']))"

# ref 狀態
git log master --oneline -10
git log frontend-tools-a0f --oneline -20
git log origin/master --oneline -5

# 6 個 commit verify
for h in f17d567 bd0920d b94f741 140af34 d6ec085 499bc13; do
  echo "=== $h ==="
  git show $h --name-status
done

# 維度 1 PHASE_D_COMPLETION_REPORT verify
grep -n "^# " _design/PHASE_D_COMPLETION_REPORT.md
grep -n "Milestone 4\|接近條件\|真正" _design/PHASE_D_COMPLETION_REPORT.md
grep -n "Wave 12\|deferred\|partial" _design/PHASE_D_COMPLETION_REPORT.md
grep -n "Finding [123]" _design/PHASE_D_COMPLETION_REPORT.md
grep -n "NEW_REQ_14" _design/PHASE_D_COMPLETION_REPORT.md

# 維度 2 Wave 14 export-* 結構
for f in .claude/skills/export-world/SKILL.md .claude/skills/export-character/SKILL.md .claude/skills/export-outline/SKILL.md .claude/skills/export-detailed-outline/SKILL.md; do
  echo "=== $f ==="
  grep -n "^## " "$f" | head -20
done
grep -n "DERIVED\|breadcrumb\|TOC\|slug\|生成方式\|組合來源" .claude/skills/export-world/SKILL.md
grep -n "D-054\|per-scene\|06_a\|hybrid\|fallback\|read_source" .claude/skills/export-detailed-outline/SKILL.md

# 維度 2 Wave 15 diagnose + integrate 結構
grep -n "^## " .claude/skills/diagnose/SKILL.md | head -20
grep -n "^## " .claude/skills/integrate/SKILL.md | head -20
grep -n "Mode A\|Mode B\|Mode C\|scan_all\|file_path\|inline_text\|6 段診斷" .claude/skills/diagnose/SKILL.md
grep -n "Stage 4a\|Stage 4b\|採\|修改後採\|target 必填\|D-050\|D-052\|D-054" .claude/skills/integrate/SKILL.md

# 維度 2 Wave 12 SKILL.md 不存在 verify（屬 deferred）
for d in iterate-world iterate-character iterate-relationship iterate-outline iterate-detailed-outline iterate-scene 迭代世界觀 迭代角色 迭代關係 迭代大綱 迭代細綱; do
  if [ -f ".claude/skills/$d/SKILL.md" ]; then echo "VIOLATION: $d EXISTS (should be deferred)"; else echo "OK: $d deferred"; fi
done

# 維度 4 CANON_DELTA + L3 schema
grep -n "^## \|^### " _design/CANON_DELTA_FRAMEWORK.md | head -30
grep -n "framework reference\|不實作 skill\|trigger A\|trigger B\|trigger C\|trigger D" _design/CANON_DELTA_FRAMEWORK.md
grep -n "§Z\|L3 schema\|不實作\|L3 prompt generator" _design/CODEX_D10_STARTER.md

# stale grep（維度 4）
grep -rn "01A_世界觀總覽\|01B_世界語言\|02A_專有名詞\|05D_資訊揭露\|04_b_關係演化時間線" \
  .claude/skills/export-*/ .claude/skills/diagnose/ .claude/skills/integrate/ \
  .claude/skills/匯出*/ .claude/skills/診斷/ .claude/skills/整理/ \
  _design/CODEX_D10_STARTER.md _design/CODEX_D_EXPORT_BATCH_STARTER.md \
  _design/CODEX_D14_STARTER.md _design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md \
  _design/CANON_DELTA_FRAMEWORK.md _design/CODEX_D_FINAL_STARTER.md \
  _design/PHASE_D_COMPLETION_REPORT.md _design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md 2>/dev/null
````

⚠ 排除歷史 narrative / supersede note 段

---

# 6. Cross-ref

- `_design/CODEX_D_FINAL_STARTER.md` v0.1（第二段 Wave 16 Step 1 落地的 starter；本 review 對象之一）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.0（第二段 Wave 16 Step 2 落地的事實檔；本 review 對象之一；含 §8 三 finding）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION_PART3.md` v1.0（本 review 對象之一；含 task 1 Wave 16 Step 3 scope）
- `_design/CODEX_D10_STARTER.md` v0.1 + `_design/CODEX_D_EXPORT_BATCH_STARTER.md` v0.1（Wave 14 starter）
- `_design/CODEX_D14_STARTER.md` v0.1 + `_design/CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` v0.1（Wave 15 starter）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（Wave 15 framework reference）
- `_design/CODEX_D1_STARTER.md` v0.3 ~ `_design/CODEX_D5_STARTER.md` v0.4（Wave 12 starter set；本 review verify partial 落地狀態 only）
- `00_protocol/00_j_迭代協議.md` v0.2（Wave 12 共通基底；屬第一段已落地）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（pattern 對齊範本）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.4 / `_design/PHASE_A_COMPLETION_REPORT.md` v1.1（pattern 對照）
- `_design/CODEX_C_FINAL_STARTER.md` v0.1（同最終 milestone starter pattern 對照）
- `_design/CODEX_9TH_MASTER_WAVE13_REVIEW_STARTER.md` v0.1 + `_design/CODEX_9TH_MASTER_WAVE13_REVIEW_REPORT.md` v0.1（9th master 第一段 review pattern 對照）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（PART2 接手包；§4 風險警示）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master 整體 scope；§3.4-§3.5 Wave 14-15 範圍 + §4 風險警示）
- `_design/POST_LOCK_PENDING.md` v0.18（5 條教訓內化 + NEW_REQ deferred 清單）
- `_design/DECISIONS_LOG.md` v2.0 §6.12 / §6.15 / §6.16 / §6.17（D-050 / D-052 / D-053 / D-054 拍板）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 拍板包）
- `_design/ARCHITECTURE.md` v1.6 §4.2 / §4.2a / §4.4 / §6（Phase D 整體架構）
- `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §5（Canon Delta framework 對齊）
- `_design/UX_SPEC.md` v0.4 §7（呈現規則）+ §11（Phase A.0F 11 個 feature spec — 不在本 review 範圍）
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 §1.1（L3 schema 對齊備忘 reference）
- `.claude/skills/export-world/SKILL.md` v0.1 ~ `.claude/skills/export-detailed-outline/SKILL.md` v0.1 + 4 中文 wrapper（Wave 14 落地）
- `.claude/skills/diagnose/SKILL.md` v0.1 + `.claude/skills/integrate/SKILL.md` v0.1 + 2 中文 wrapper（Wave 15 落地）
