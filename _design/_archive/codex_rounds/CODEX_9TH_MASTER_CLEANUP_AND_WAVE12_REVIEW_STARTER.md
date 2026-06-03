狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：第九輪 master cleanup queue + Phase D Wave 12 完成後 Round 1 重審 — R8-INFO-06 / R10-MI-01/02/03 / AGENTS+CLAUDE / R10-MA-01 ack / 08_a §11.1 / 00_j 迭代協議 / 5+1 個 /iterate-* starter 整體完整性 + regression  
優先級：高

# CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_STARTER — Round 1 重審

# 0. 本檔用途

第九輪 master 流程進展：cleanup queue Task 1-6 完成 → Phase D Wave 12 starter set Task 7 完成 → **本輪 Round 1 重審驗證 9th master cleanup queue 處理 + Wave 12 starter set 完整性 + regression**。

**前置條件：** 9th master 已完成 Cleanup Task 1-6 + Wave 12 Task 7 預定變動（14 個檔範圍）+ user 已 commit/push。

**重審 GO →** 9th master 進 Wave 13（4 個 /view-* starter）

**重審 NEAR-GO →** user 拍板 hard-limit accepted（殘留 finding 入下一輪 cleanup queue 或當輪 master inline patch）

**重審 NO-GO →** 大幅 rollback / restructure；user 拍板路徑

⚠ **單輪結束 default 紀律延續（沿用第八輪教訓 §4.6/§4.7）：** Round 1 預設一輪結束；不預設自動進 Round 2。

⚠ **9th master 用「grep 全掃 sweep 模式」處理 cleanup queue：** Round 1 應驗證 sweep 是否真乾淨（cascade pattern 預防紀律是否內化）。

⚠ **Wave 12 starter set 採「D1 完整 + D2-D4 引用 D1 + D5 含 D-054 落地」模式：** Round 1 應驗證跨 starter cross-ref 一致性 + D-054 NEW_REQ_15 落地正確性。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第九輪 master cleanup queue + Phase D Wave 12 完成後 Round 1 重審」— 對 9th master 期間所有變動跑「cleanup queue 完整性 + Wave 12 starter set 一致性 + D-054 落地正確性 + regression + cascade pattern 預防紀律」多重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同第八輪 Round 1-10 重審模式（CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT v0.1 是參考 baseline；Round 10 NEAR-GO 含 1 MAJOR + 3 MINOR；hard-limit accept 入 9th master cleanup queue NEW_REQ_19）
- 對應前置：9th master Cleanup Task 1-6 + Wave 12 Task 7 已完成 + commit/push

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report 給 master 處理）
- ✗ 不跑真實 /iterate-* / /scene-task / /dialogue-write / /qa 寫檔（會污染 Template；端到端測試屬 user 親跑 M4）
- ✗ 不修補任何 stale reference / cross-doc inconsistency（屬 master inline patch / 下一輪 cleanup queue scope）
- ✗ 不重審 D-001~D-054 拍板結論（已 LOCKED；本輪只 verify 落地 correctness 不質疑拍板）
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec（已 PASS in PHASE_A/B/C_COMPLETION_REPORT；本輪只 verify 9th master 新動範圍）
- ✗ 不重審 R10-MA-01 user 平行加 NEW_REQ_16/17/18 屬正當作業（user 已明示同意；本輪只 verify 9th master 對其 ack 紀錄正當性，不重議 ack 本身）
- ✗ 不下新 D-NNN 拍板（屬 user 拍板範圍）
- ✗ 不開 9th master patch round（屬 master 對話內處理；本輪純檢查）
- ✓ 可跑技術驗證命令（check_headers / check_paths / build_repo_index / git log / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定 — 14 個檔範圍）：**

### Part A — 9th master cleanup queue（Task 1-6；8 個既有檔改動）

依 POST_LOCK_PENDING v0.14 NEW_REQ_19「9th master 處理紀錄」段：

1. **Task 1 — R8-INFO-06**：`00_protocol/00_k_台詞生產流程協議.md` v0.1 → v0.2
   - 階段 3 從「5 份 QA」改「8 份 QA」對齊 D-043
   - 序列印出順序對齊 UD §2.5.3 v0.3：09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i
   - §6.2 QA_PASSED 到 FINAL 段補 FINAL gate 9-status 齊全條件（8 份 /qa + 09_e）
   - §5.3 表格 / §5.4 qa_decision PASS 條件 / §5.5 寫檔規則 / §5.6 phase_log entry 範例 / §8 禁止事項 / §10.5 / §10.6 全對齊 8 份必跑
   - header v0.1 → v0.2 含 partial supersede note via D-043

2. **Task 2 — R10-MI-01/02/03 sweep**：grep 全掃 sweep 模式一次性處理
   - `_design/phase_b_review_log.md` v0.5 → v0.6（line 140 character_review_log v0.2 → v0.3；line 141 outline_review_log v0.3 → v0.4；line 147 create-detailed-outline v0.2 → v0.3）
   - `_design/PHASE_B_COMPLETION_REPORT.md` v1.2 → v1.3（line 13/15 CODEX_B9_STARTER v0.3 → v0.4；line 37 工作樹備註升級至 v1.3 對齊 + historical narrative 段；line 112 CH skill v0.2 → v0.3；line 114 補 R9-INFO-02 紀錄；line 244 B9 starter v0.4；line 254 POST_LOCK_PENDING v0.9 → v0.13）
   - `_design/CODEX_B9_STARTER.md` v0.4 → v0.5（line 98 / line 121 CH SKILL.md v0.2 → v0.3）

3. **Task 3 — AGENTS.md / CLAUDE.md Phase C skill table TBD → DONE**：
   - CLAUDE.md header v0.1 → v0.2
   - Phase B+ skill table 重做（22 row）：Phase B 4 個 /create-* + Phase C 3 個下游 skill + 3 中文 wrapper 全標 ✅ 已實作；Phase D /iterate-* / /view-* / /export-* / /diagnose / /integrate 明示 TBD（Phase D Wave 12-15 範圍）；含 /iterate-scene <S-ID> --split-to-file row 標 NEW_REQ_15 落地
   - QA 模板表新增（9 row 含 09_g/h/i 標 C4 patch round 補建）
   - Phase 階段對應段更新（Milestone 1/2/3 達成）
   - 相關 spec 版本對齊：ARCH v1.4 → v1.6 / DECISIONS_LOG v1.2 → v2.0 / TASKS v1.5 → v1.9 / 新增 PHASE_C_COMPLETION_REPORT v1.0 + POST_LOCK_PENDING v0.13~v0.14
   - AGENTS.md 同樣結構更新（無 5 欄 header；Codex CLI 不需要）

4. **Task 4 — R10-MA-01 ack + POST_LOCK_PENDING v0.14**：
   - `_design/POST_LOCK_PENDING.md` v0.13 → v0.14
   - NEW_REQ_19 末加「9th master 處理紀錄」段（cleanup queue 處理結果表 + 未處理項推 10th master + cascade pattern 預防紀律內化記錄 + 9th master Owner ack）
   - 狀態更新：🟡 DEFERRED → 🟢 PROCESSED（待 cleanup verify baseline 確認後可標 ✅ RESOLVED）
   - R10-MA-01 ack：9th master 明示 authorize user 平行加 NEW_REQ_16/17/18/19 屬正當作業

5. **Task 5 — 08_a §11.1 5→8 (P-009)**：`08_dialogue_outputs/08_a_台詞版本管理規範.md` v0.2 → v0.3
   - §11.1 表格從 5 必跑（09_a/b/c/d/e）改 8 必跑（09_a/b/c/d/f/g/h/i）+ 09_e 必要前置（final-gating；非 /qa）
   - 補序列印出順序（依 UD §2.5.3 v0.3）+ qa_decision PASS 條件（8 份全 PASS）+ FINAL gate 9-status 齊全條件
   - header v0.2 → v0.3 含 partial supersede note via D-043
   - user 明示同意動 LOCKED 性質模板（trace 在 AskUserQuestion「Cleanup queue 全做（含 08_a）」拍板）

6. **Task 6 — baseline verify**：cleanup queue 處理完跑 baseline；對齊 R10 baseline（check_headers 0 ERROR；check_paths 254 → 243 ERROR 比 baseline 還少 11）

### Part B — Phase D Wave 12 starter set（Task 7；6 個新建檔）

依 TASKS v1.9 §C.1（00_j 迭代協議）+ §C.2（5 個 /iterate-* skill）+ DECISIONS_LOG v2.0 §6.17 D-054（NEW_REQ_15）：

7. **00_protocol/00_j_迭代協議.md v0.1**（共通基底協議；新建）
   - 14 段：文件目的 / 啟動條件 / 階段 1 變更點識別 / 階段 2 強制影響範圍評估 / 階段 3 收斂 / 階段 4 執行 / 階段 5 實體驗證 / 禁止事項 / 缺漏處理 / 專屬區段 §10.1-§10.7 / 下游 pipeline 互鎖 / Canon Delta 互動 / 觸發語字典 / Cross-ref
   - §4.1 雙路反查 algorithm 對齊 ARCH §5
   - §4.3 影響範圍呈現格式對齊 ARCH §5 範例
   - §4.4 下游 pipeline 互鎖對齊 00_k §10.7.5
   - §10.7 /iterate-scene <S-ID> --split-to-file（D-054 NEW_REQ_15 落地專屬段）

8. **_design/CODEX_D1_STARTER.md v0.1**（/iterate-world starter；共通範本）
   - 結構：本檔用途 / 啟動 prompt / CODEX 工作流程 / 驗收條件 / 邊界紀律 / Cross-ref
   - 任務目標：2 個 SKILL.md（`.claude/skills/iterate-world/SKILL.md` + `.claude/skills/迭代世界觀/SKILL.md`）
   - 主 SKILL.md 結構（11 段）+ 差異規格 + 5 階段流程 + phase_log entry 範例 + 啟動前檢查 5 項 + 邊界 D-050+D-053 三 block + 中文 wrapper 極簡模式
   - W-rules 反查預期清單表 + qa_recheck_recommended: [09_c] 對齊紀律

9. **_design/CODEX_D2_STARTER.md v0.1**（/iterate-character starter）
   - 採「引用 D1 為共通範本 + 列差異」模式
   - 任務目標：2 個 SKILL.md
   - C-* 差異：觸發語接 1 user 參數；registry key `00_f_character`；modify 範圍 C-<name>；下游 04_a / 04_b / 00_b §3；qa_recheck_recommended: [09_b]

10. **_design/CODEX_D3_STARTER.md v0.1**（/iterate-relationship starter）
    - 採同 D2 引用 D1 模式
    - R-*-* 差異：觸發語接 2 user 參數；registry key `00_l_relationship`；兩端 C-* 聲線卡關係段同步；下游 04_a / 04_b / 兩端 C-*

11. **_design/CODEX_D4_STARTER.md v0.1**（/iterate-outline starter）
    - 採同 D2 引用 D1 模式
    - P 差異：影響範圍**極廣** ≥ 20 檔；強烈建議分批；registry key `00_g_outline`；下游 05_a/b/c/d/e + 06_a + 已產出台詞；qa_recheck_recommended: [09_d, 09_f]；downstream_review_required: true

12. **_design/CODEX_D5_STARTER.md v0.1**（/iterate-detailed-outline + /iterate-scene --split-to-file starter；含 D-054 NEW_REQ_15 落地）
    - 兩個 skill 一份 starter — 3 個 SKILL.md（/iterate-detailed-outline + 迭代細綱 wrapper + /iterate-scene；/iterate-scene 無中文 wrapper 屬 hybrid escape hatch 性質）
    - /iterate-detailed-outline：CH-* / S-*-* 迭代；D-054 hybrid fallback 讀檔（先 check per-scene 檔；fallback 06_a row）
    - **/iterate-scene --split-to-file（D-054 NEW_REQ_15 落地核心）：**
      - 把 06_a row split 為 per-scene 檔
      - 06_a 內**保留 row** + 加 marker `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->`（下游 /scene-task v0.1 fallback 兼容）
      - frontmatter 對齊 SPEC §5.2（entities/depends_on/weight）
      - phase_log entry 標 `split_to_file: true`（NEW_REQ_15 trigger B monitor）

**8th master patch round 3 + Round 10 同類驗證 baseline：**
- R10 期間 check_headers 0 ERROR / 35 WARN
- R10 期間 check_paths 254 ERROR / 1 WARN
- R10 期間 build_repo_index 0 ERROR / 70 WARN (Windows 端)

**9th master 預期 baseline（master 已跑驗證）：**
- 9th cleanup 後 check_headers 0 ERROR / 38 WARN
- 9th cleanup 後 check_paths 243 ERROR / 1 WARN（比 R10 baseline 少 11 個 — cross-ref 對齊讓些 path stale 自動解決）
- 9th Wave 12 後 check_headers 0 ERROR / 38 WARN / 154 files
- 9th Wave 12 後 check_paths 245 ERROR / 1 WARN / 159 files（比 cleanup 後 +2 屬新 starter 帶入 reference）

### 9th master 不動段（聲明）

以下檔本輪 cleanup queue + Wave 12 **不動**（聲明 + 應由 Round 1 verify protected-area diff）：

- LOCKED spec：REQUIREMENTS_LOCK v1.0 / DECISIONS_LOG v2.0 / INTEGRATION_CONTRACTS v2.1 / SPEC v1.2 / ARCHITECTURE v1.6 / TASKS v1.9 / DATA_FORMAT_SPEC v0.4 / UPSTREAM_DOWNSTREAM_SPEC v0.5 / UX_SPEC v0.4 / L3_EXPORT_PROMPT_SCHEMA v0.2
- LOCKED registries：entity_type_registry.template.yaml v0.1 / qa_type_registry.template.yaml v0.1 / issue_type_registry.template.yaml v0.1
- scripts：parse_frontmatter.py / check_headers.py / check_paths.py 不動
- 27 模板（含 06_a 場景索引模板 + 04_a 關係矩陣模板等）不動
- 00_protocol/00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_l 不動（**只動 00_k v0.1 → v0.2 + 新建 00_j v0.1**）
- 既有 16 個 SKILL.md（init-project / status / check-gaps / create-* x5 + 5 中文 wrapper + scene-task / dialogue-write / qa + 3 中文 wrapper）不動
- 第八輪 review reports + starter（CODEX_8TH_MASTER_*）不動 — 屬 immutable history
- D054_DECISION_PACKAGE v0.2 不動 — APPLIED 紀錄
- PHASE_A_COMPLETION_REPORT v1.1 / PHASE_C_COMPLETION_REPORT v1.0 不動
- HANDOFF_TO_8TH_MASTER + HANDOFF_TO_9TH_MASTER 不動

⚠ **Protected-area diff 檢查（沿用 R10-MA-01 紀律）：** 任何 `HEAD~N..HEAD` 觸及上述聲明不動範圍 → 列為 R1-MA-XX

---

# 2. 重審範圍與維度（7 維度）

**維度 1：R8-INFO-06 (00_k v0.2) 升級正確性 + 完整性（最優先）**

驗證 `00_protocol/00_k_台詞生產流程協議.md` v0.1 → v0.2 各段是否完整對齊 D-043 + UD §2.5.3 v0.3：

- §1 文件目的「5 份 QA」→「8 份 QA」+ partial supersede note
- §5 階段 3：QA 標題 + 副標題對齊
- §5.3 內部子階段 2：執行 8 份報告（序列順序 09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i；對應 qa_type 完整 8 個）
- §5.4 qa_decision PASS 條件「8 份全 PASS」
- §5.5 寫檔規則「8 份報告各寫一份」
- §5.6 phase_log entry 範例（8 條 qa_report_paths + 對應 qa_type 註解）
- §6.2 QA_PASSED 到 FINAL 補 FINAL gate 9-status 齊全表（9 row + 通過條件 + Gate 行為）
- §8 禁止事項 #9「8 份」
- §10.1 場景狀態機表「8 份報告完整」
- §10.5 八份 QA 報告閱讀順序（標題 + 8 row + qa_type 對應 + v0.2 supersede note）
- §10.6 跨 skill 呼叫關係「8 份 QA 報告 .md」
- 全檔無「5 份」/「五份」/「5 份報告」殘留（除 supersede note 內歷史 narrative）

**判定：** PASS / PARTIAL / FAIL；列任何漏掉的對齊點。

**維度 2：R10-MI-01/02/03 sweep 完整性（active stale 全清驗證）**

對 9th master sweep 的 3 個目標檔跑 grep 全掃，驗證 active stale 是否真乾淨：

- `_design/phase_b_review_log.md` v0.6：line 140-141 + line 147 對齊；header note 含 9th master cleanup queue 紀錄
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.3：line 13/15 + line 37 + line 112/114 + line 244/254 對齊；header note 對齊
- `_design/CODEX_B9_STARTER.md` v0.5：line 98 + line 121 對齊；header note 對齊

跑 grep stale pattern：
```
grep -n "create-detailed-outline.*v0\.2|character_review_log.*v0\.2|outline_review_log.*v0\.3|CODEX_B9_STARTER.*v0\.3" 3 個檔
```

預期：3 個檔內無 active stale match（matches 限歷史 narrative / supersede note 內歷史紀錄段；明示為 historical 才算 PASS）。

**Cascade pattern 預防紀律驗證（9th master 是否真的內化教訓）：**

- 第八輪 patch round 2/3 連續 sequential cascade — 9th master sweep 後 grep 全掃驗證
- 任何新引入的 sequential cross-ref stale → R1-CR-XX cascade regression

**判定：** PASS / PARTIAL / FAIL；列任何漏掉的 sweep target + 新引入的 cascade。

**維度 3：AGENTS.md / CLAUDE.md skill table 對齊事實 + spec 版本 cross-ref**

驗證兩檔 skill table + Phase 階段對應 + 相關 spec 版本：

- CLAUDE.md / AGENTS.md：14 個已實作 skill（Phase A 4 + Phase B 4 + Phase C 3 + 3 中文 wrapper）標 ✅；對齊實際 SKILL.md 版本
- Phase D /iterate-* / /view-* / /export-* / /diagnose / /integrate 標 TBD（Phase D Wave 12-15 範圍）— 對齊本輪 Wave 12 starter 範圍但 SKILL.md 未實作（屬 CODEX 跑 Wave 12 D.1-D.5 task 才實作）
- /iterate-scene <S-ID> --split-to-file row 標 TBD（Phase D Wave 12 範圍；D-054 NEW_REQ_15 落地）
- QA 模板表 9 row（09_a/b/c/d/e/f/g/h/i）全 ✅；09_g/h/i 標「C4 patch round 補建」
- Phase 階段對應段：Milestone 1/2/3 達成宣告（對齊 PHASE_A v1.1 / PHASE_B v1.2 / PHASE_C v1.0）；Phase D 對應 TASKS §C
- 相關 spec 版本：ARCH v1.6 / DECISIONS_LOG v2.0 / TASKS v1.9 / POST_LOCK_PENDING v0.14 / PHASE_C_COMPLETION_REPORT v1.0 — 對齊實際 header

**判定：** PASS / PARTIAL / FAIL；列任何 stale skill status / stale 版本 / 漏掉的 skill row。

**維度 4：R10-MA-01 ack + POST_LOCK_PENDING v0.14 NEW_REQ_19 處理紀錄 + 08_a §11.1 修正正當性**

驗證紀錄性 task 完整性：

- POST_LOCK_PENDING v0.13 → v0.14 header note 對齊 9th master cleanup queue 處理範圍
- NEW_REQ_19「9th master 處理紀錄」段：
  - 狀態更新「🟡 DEFERRED → 🟢 PROCESSED」
  - 處理時點 2026-05-22
  - 處理結果表（6 row：R8-INFO-06 / R10-MI-01 / R10-MI-02 / R10-MI-03 / R10-MA-01 ack / AGENTS+CLAUDE skill table）
  - 未處理項推 10th master 紀錄（NEW_REQ_16 lint script + 08_a 已處理註記）
  - Cascade pattern 預防紀律內化 4 條
  - Owner ack 9th master
- 08_a v0.2 → v0.3 對齊 D-043（5 → 8 必跑 + 09_e final-gating 必要前置 + 序列順序 + qa_decision PASS 條件 + FINAL gate 9-status 齊全）

**user 明示同意 trace：** AskUserQuestion「Cleanup queue 全做（含 08_a）」拍板 = user 對 08_a 動 LOCKED 性質模板的明示同意。

**判定：** PASS / PARTIAL / FAIL；列任何漏掉的 ack 紀錄 / 不完整的處理結果 / 08_a 殘留 stale。

**維度 5：00_j 迭代協議 v0.1 完整性（5 階段框架 + 雙路反查 + §10 各 entity 迭代指南 + §10.7 D-054 落地）**

驗證新建 `00_protocol/00_j_迭代協議.md` v0.1 是否完整支撐 5 個 /iterate-* skill + /iterate-scene --split-to-file：

- 14 段全齊：§1 文件目的 / §2 啟動條件 / §3-§7 五階段 / §8 禁止事項 / §9 缺漏處理 / §10 專屬區段 / §11 下游 pipeline 互鎖 / §12 Canon Delta 互動 / §13 觸發語字典 / §14 Cross-ref
- §3 階段 1 變更點識別：6 必含項 + 4 變更類型分類
- §4 階段 2 強制影響範圍評估：4.1 雙路反查 algorithm 對齊 ARCH §5 + 4.2 雙路反查紀律 + 4.3 影響範圍呈現格式對齊 ARCH §5 範例 + 4.4 下游 pipeline 互鎖對齊 00_k §10.7.5
- §5 階段 3 收斂：5 欄位收斂預告稿
- §6 階段 4 執行：寫檔順序 + 6.1 phase_log entry 範例（含 modified_entity / modified_files / scope_choice / affected_files_evaluated 三路 / prereq_changed / abort_reason 欄位）+ 6.2 View 重生紀律（O3 鎖定）
- §7 階段 5 實體驗證：自動 /status 4 項；不可 3 項
- §8 禁止事項 10 條
- §9 缺漏處理：9.1 depends_on 不完整 / 9.2 CONFLICT / 9.3 LOCKED 實體迭代請求 / 9.4 過時依賴
- §10 各 entity 迭代呼叫指南：§10.1 W-rules / §10.2 C-* / §10.3 R-*-* / §10.4 P / §10.5 CH-* / §10.6 S-*-* / §10.7 /iterate-scene --split-to-file（**D-054 NEW_REQ_15 落地專屬段**）
- §10.7 詳細落地：5 階段對應 split-to-file 子模式 + 06_a row 保留 + marker 加入 + frontmatter 對齊 SPEC §5.2 + phase_log entry 標 split_to_file + NEW_REQ_15 trigger 監控
- §11 下游 pipeline 互鎖對齊 00_k §10.7.5
- §12 Canon Delta 互動對齊 UPSTREAM §5.1-§5.5
- §13 觸發語字典對齊 ARCH §6.7.2
- §14 Cross-ref 對齊（ARCH v1.6 / SPEC v1.2 / UPSTREAM v0.5 / DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.14 / TASKS v1.9 / 00_e ~ 00_h + 00_l / 00_k v0.2）

**特別注意：** §10.7 /iterate-scene --split-to-file 設計對齊 D-054 拍板（DECISIONS_LOG v2.0 §6.17.2）+ D054_DECISION_PACKAGE v0.2 §2.1。

**判定：** PASS / PARTIAL / FAIL；列任何漏掉的段 / 不完整的對齊。

**維度 6：5+1 個 /iterate-* starter set 一致性（D1 範本 / D2-D4 引用 / D5 D-054 NEW_REQ_15 落地 / D-050+D-053 邊界對齊）**

驗證 6 個 Wave 12 starter（D1-D5 + 含 D5 內 /iterate-scene）：

**D1 共通範本**（CODEX_D1_STARTER v0.1）：
- 主 SKILL.md 結構 11 段齊全（frontmatter / 中文 5 header / 用途 / 觸發語 / 觸發協議 / 啟動前檢查 / 流程 / 影響範圍評估規範 / .protocol_version / 輸入 / 輸出 / 邊界 / 錯誤處理 / 錯誤呈現）
- 5 階段差異對應 00_j §3-§7
- W-rules 反查預期清單表完整
- 邊界 3 block（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔範圍）對齊 Phase B 4 個 /create-* skill v0.3 格式
- 中文 wrapper 極簡模式

**D2-D4 引用 D1 紀律**：
- 各 starter 開頭明示「沿用 D1 starter pattern」
- 差異規格只列「entity 類型 / 觸發語 / 對應 protocol / registry key / modify 範圍 / 依賴下游 / 下游建議」
- 5 階段差異段（不重複大段 substantive；只列 D2/D3/D4 entity 特性差異）
- phase_log entry 範例對齊 00_j §6.1 + 各 entity 類型專屬欄位
- 邊界 3 block 對齊 D1 + entity-specific 寫檔範圍

**D5 D-054 NEW_REQ_15 落地（核心）：**
- 2 個 skill / 3 個 SKILL.md（/iterate-detailed-outline + 迭代細綱 + /iterate-scene；/iterate-scene 無中文 wrapper）
- /iterate-detailed-outline：CH-* + S-*-* 迭代；D-054 hybrid fallback 讀檔
- /iterate-scene 完整流程：
  - 階段 1 變更點識別含「split-to-file」選項提示
  - 階段 2 影響範圍評估反查所有引用本 S-*-* 的檔
  - 階段 3 收斂預告 split 動作 + 06_a marker 設計
  - 階段 4 執行寫檔順序：寫新 per-scene 檔 → 在 06_a row 加 marker（**不刪除 row**；fallback 兼容）→ phase_log
  - 階段 5 實體驗證：`split_to_file: true` 標記 + NEW_REQ_15 trigger 監控
- phase_log entry 範例 2 個（/iterate-detailed-outline + /iterate-scene）對齊 00_j §6.1
- 啟動前檢查：6 項（D-049 + Bootstrap + 目標 S 存在 + 對應 CH 存在 + LOCKED check + split-to-file 子模式額外檢查 per-scene 檔尚未存在）
- 邊界 3 block 對齊 Phase B 4 skill 格式

**跨 starter cross-ref 一致性：**
- D2-D5 對「先讀 D1 為共通範本」的引用一致（5 個 starter cross-ref 對齊）
- 00_j ↔ 5+1 starter cross-ref 一致（00_j §10.1 → D1 / §10.2 → D2 / §10.3 → D3 / §10.4 → D4 / §10.5+§10.6+§10.7 → D5）

**判定：** PASS / PARTIAL / FAIL；列任何 starter 結構不一致 / D-054 落地不完整 / 邊界 block 對齊偏差。

**維度 7：跨 cleanup + Wave 12 範圍的 baseline + regression + stale cross-ref 殘留**

技術驗證：

- 跑 `python -X utf8 -B scripts/check_headers.py` — 對齊 9th master Wave 12 後預期 baseline（0 ERROR / ≤ 40 WARN / 154 files）
- 跑 `python -X utf8 -B scripts/check_paths.py` — 對齊 9th master Wave 12 後預期 baseline（≤ 250 ERROR / 1 WARN / 159 files）
- 跑 `build_repo_index('.')` — 對齊 0 ERROR（Windows 端權威；sandbox 端可能含 virtiofs cache stale noise）

Protected-area diff 檢查（沿用 R10-MA-01 紀律）：

- `git log --oneline -5` 確認 9th master commit hash
- `git diff <9th master baseline>..HEAD --name-status` 列所有 9th master 觸及檔
- 對比「9th master 不動段聲明」(§1 末) — 任何觸及不動段 → R1-MA-XX

跨範圍 stale grep 全掃：

- `create-detailed-outline.*v0\.2` / `CH skill.*v0\.2`
- `character_review_log.*v0\.2` / `outline_review_log.*v0\.3`
- `CODEX_B9_STARTER.*v0\.3`
- `POST_LOCK_PENDING.*v0\.9` 或 `v0\.10` 或 `v0\.11` 或 `v0\.12` 或 `v0\.13`
- `5 份 QA` / `五份 QA`
- `ARCH.*v1\.4` 或 `v1\.5`
- `DECISIONS_LOG.*v1\.[1-9]`（應 v2.0）
- `TASKS.*v1\.[1-8]`（應 v1.9）

任何 active stale match（排除歷史 narrative / supersede note 內紀錄段）→ R1-MI-XX。

**判定：** PASS / PARTIAL / FAIL；列任何 baseline regression / protected-area mismatch / 新 stale 引入。

---

# 3. Finding 嚴重度定義

- **CRITICAL**：spec 自相矛盾 / 邏輯衝突 / D-054 落地錯誤 / runtime blocker（拒絕 Wave 13 啟動）
- **MAJOR**：跨檔不一致 / 維度 PASS 但 fundamental 對齊偏差 / protected-area diff mismatch（強烈建議處理）
- **MINOR**：版本欄 / cross-ref 小不一致 / sweep 漏掉的 active stale（可入下一輪 cleanup 或當輪 master inline patch）
- **INFO**：observation / 改善建議 / spec polish（不必處理也可）

# 4. 判定門檻

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + R8-INFO-06 / R10-MI-01-03 / R10-MA-01 ack / 08_a §11.1 / 00_j / 5+1 starter 全 PASS + 0 baseline regression + 0 protected-area diff → 9th master 進 Wave 13
- **NEAR-GO（HOLD）**：0 CRITICAL + ≤ 1 MAJOR + ≤ 5 MINOR + 0 baseline regression → user 拍板 hard-limit accept 或 master inline patch
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR 或 0 baseline regression → 大幅 rollback / restructure

# 5. 輸出格式

寫 1 個檔：`_design/CODEX_9TH_MASTER_CLEANUP_AND_WAVE12_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Round 1 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：R8-INFO-06 (00_k v0.2) 升級正確性 + 完整性
# 3. 維度 2：R10-MI-01/02/03 sweep 完整性
# 4. 維度 3：AGENTS.md / CLAUDE.md skill table 對齊事實 + spec 版本
# 5. 維度 4：R10-MA-01 ack + POST_LOCK_PENDING v0.14 NEW_REQ_19 + 08_a §11.1
# 6. 維度 5：00_j 迭代協議 v0.1 完整性
# 7. 維度 6：5+1 個 /iterate-* starter set 一致性（D1 / D2-D4 / D5 D-054 落地）
# 8. 維度 7：baseline + regression + stale cross-ref grep 全掃
# 9. Finding 總計表（CRITICAL / MAJOR / MINOR / INFO 個別 row）
# 10. 決策判定 + Rationale
# 11. 給 9th master 的建議（含「進 Wave 13」/「inline patch」/「hard-limit accept」3 路徑）
# 12. Cross-ref
```

⚠ 必含 finding ID 命名規範：`R1-<severity>-<NN>`（例：`R1-MA-01` / `R1-MI-03` / `R1-INFO-02`）

✓ 必含維度 1-7 對 14 個檔 + cleanup queue + Wave 12 各 task 的 PASS / PARTIAL / FAIL 標記
✓ 必含維度 7 跨範圍 stale grep 全掃結果（含 grep 命令 + 結果摘要）
✓ 必含 D-054 落地正確性的明確 PASS / FAIL（D5 starter §10.7 + 00_j §10.7 + /iterate-scene SKILL.md 設計意圖）

---

# 6. 起跑命令（你接力時用）

bash 命令：
```bash
cd /sessions/<your_session>/mnt/劇本開發工具
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -5
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -5
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']))"
git log --oneline -10
git diff HEAD~2..HEAD --name-status   # 對比 9th master cleanup + Wave 12 commit 範圍
```

grep 全掃 sweep（給維度 2/7 用；可調整）：
```bash
grep -rn "create-detailed-outline.*v0\.2" _design/ 00_protocol/ --include='*.md'
grep -rn "character_review_log.*v0\.2" _design/ 00_protocol/ --include='*.md'
grep -rn "outline_review_log.*v0\.3" _design/ 00_protocol/ --include='*.md'
grep -rn "CODEX_B9_STARTER.*v0\.3" _design/ --include='*.md'
grep -rn "5 份 QA\|五份 QA\|5 份報告" 00_protocol/ 08_dialogue_outputs/ --include='*.md'
grep -rn "ARCH.*v1\.4\|ARCH.*v1\.5" _design/ --include='*.md' | grep -v "history\|歷史\|supersede"
grep -rn "DECISIONS_LOG.*v1\.[1-9]" _design/ --include='*.md' | grep -v "history\|歷史\|supersede"
```

⚠ 排除歷史 narrative / supersede note 段（屬 immutable history；不算 active stale）

# 7. Cross-ref

- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（第八輪 Round 10 NEAR-GO；9th master cleanup queue 起點）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_STARTER.md` v0.1（pattern 參考）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master scope；含 cleanup queue 詳細列表 §4.1）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Milestone 3 達成事實檔；§8 9th master cleanup queue 處理優先序）
- `_design/POST_LOCK_PENDING.md` v0.14（NEW_REQ_19 9th master 處理紀錄；本輪驗證對象之一）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054（D-054 拍板原文；本輪 §10.7 落地驗證對象）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED；含完整 hybrid 設計推理）
- `_design/TASKS.md` v1.9 §C.1 + §C.2（Wave 12 task spec）
- `_design/ARCHITECTURE.md` v1.6 §5 + §6.7（雙路反查 + 共通骨架）
- `00_protocol/00_j_迭代協議.md` v0.1（本輪維度 5 驗證對象）
- `00_protocol/00_k_台詞生產流程協議.md` v0.2（本輪維度 1 驗證對象）
- `_design/CODEX_D1_STARTER.md` v0.1 ~ `CODEX_D5_STARTER.md` v0.1（本輪維度 6 驗證對象 5 個檔）
- `_design/phase_b_review_log.md` v0.6 + `PHASE_B_COMPLETION_REPORT.md` v1.3 + `CODEX_B9_STARTER.md` v0.5（本輪維度 2 驗證對象 3 個檔）
- `08_dialogue_outputs/08_a_台詞版本管理規範.md` v0.3（本輪維度 4 驗證對象）
- AGENTS.md + CLAUDE.md（本輪維度 3 驗證對象）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.5.3 v0.3 + §5（Canon Delta；維度 1 + 維度 5 §12 對齊參考）
