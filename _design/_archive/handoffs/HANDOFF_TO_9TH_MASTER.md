狀態：DRAFT  
版本：v1.0（第八輪 master 收尾交接包；Phase C + Milestone 3 達成 + Wave 11 PASS + D-054 拍板 + 11 輪 CODEX 互動 hard-limit accepted；Phase D handoff）  
最後更新：2026-05-21  
適用範圍：給「第九輪整合 master」對話的接手包 — Phase D 啟動（視圖 + 迭代 + 匯出 + 整合）+ 9th master cleanup queue (NEW_REQ_19) 處理  
優先級：最高

# HANDOFF_TO_9TH_MASTER — 第九輪整合 master 對話接手包

# 0. 文件目的

第八輪 master 對話完成 — **Milestone 3 達成宣告（Phase C 下游 3 skill 全落地 + 8 QA 模板齊全 + D-054 hybrid fallback 拍板 + PHASE_C_COMPLETION_REPORT v1.0 PASS）**。

第八輪 master 期間經 **10+ 輪 CODEX 互動**（4 輪 review + 3 輪 patch round + Wave 9-10-11 + C4 patch + Wave 11 blocker 修補），hard-limit accept Round 10 NEAR-GO。期間發現 + 處理重大議題：
- D-054 NEW_REQ_13 per-scene 檔 convention → 拍板選 1 Hybrid + 未來迭代追蹤 NEW_REQ_15
- R8-INFO-06 00_k v0.1 5→8 報告 stale → 推 9th master cleanup queue
- TASKS §D.1a 09_g/h/i 三模板未實作 → C4 patch round 提前處理（Phase C 收尾範圍）
- 「Fix one, find two」cascade pattern → user 加 NEW_REQ_16/17/18 自動化 QA 工具 3 層架構規劃
- Round 10 殘留 4 finding → hard-limit accepted 入 NEW_REQ_19 9th master cleanup queue
- Wave 11 C.2 mode_tag enum blocker（master starter typo FINAL → 應為 ORGANIZED）→ master inline patch 解除

第九輪 master 對話接手 **Phase D（視圖 + 迭代 + 匯出 + 整合）** + **9th master cleanup queue (NEW_REQ_19) 處理**。

**第九輪預期工作（Phase D — 視圖 + 迭代 + 匯出 + 整合）：**

1. 接收第八輪 handoff + 接受 D-001 ~ D-054 + 所有 §6.X 拍板
2. **9th master cleanup queue 處理（NEW_REQ_19）** — Round 10 殘留 4 finding + R8-INFO-06 + 00_k v0.1 升 v0.2 + AGENTS.md Phase C skill table 補完（30-90 分 inline patch；可一次跑完或分散處理）
3. **Phase D 主軸（Wave 12 ~ 17）：**
   - Wave 12：寫 `/iterate-*` 5 skill + `/iterate-scene --split-to-file`（D-054 NEW_REQ_15 落地）
   - Wave 13：寫 `/view-*` 4 skill
   - Wave 14：寫 `/export-*` 4 skill + L3 Export prompt 生成器
   - Wave 15：寫 `/diagnose` + `/integrate` 2 skill
   - Wave 16：9th master cleanup queue 整體 verify
   - Wave 17（optional）：NEW_REQ_16 lint script 階段性實作（建議推 10th master）
4. Phase D 收尾 + Milestone 4 接近條件聲明（封版需要 Phase A.0F 前端工具補完 — 屬 10th master）
5. 寫 HANDOFF_TO_10TH_MASTER.md 接 Milestone 4 封版

**預估第九輪總工時：** Cleanup queue 處理 30-90 分 + Phase D master 對話 3-5 小時 + CODEX 跑各 skill 6-10 小時 + user 親跑各 phase 端到端 testing 3-5 小時

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。第八輪 master 對話完成 Phase C 收尾（Wave 9-11 全 PASS + 3 個下游 skill 全落地 + C4 patch 補 09_g/h/i 三模板 + D-054 per-scene 檔 convention 拍板選 1 Hybrid + Wave 11 PASS + master starter typo 修補），Milestone 3 達成（2026-05-21）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第九輪整合 master」對話。

**第一步必讀（按順序，8 份）：**
1. _design/HANDOFF_TO_9TH_MASTER.md（本檔，你的 scope）
2. _design/PHASE_C_COMPLETION_REPORT.md v1.0（Phase C 完成事實檔；含 §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制 + §8 9th master cleanup queue 處理優先序）
3. _design/DECISIONS_LOG.md §6.17 D-054（per-scene 檔 convention Hybrid 拍板背景 + 未來迭代條件紀錄）
4. _design/POST_LOCK_PENDING.md v0.13（NEW_REQ 整體狀態；含 NEW_REQ_13 RESOLVED via D-054 + NEW_REQ_14 §6 AI-assisted + NEW_REQ_15 D-054 迭代追蹤 + NEW_REQ_16/17/18 自動化 QA 工具 + NEW_REQ_19 9th master cleanup queue + 09_g/h/i 提前處理註記）
5. _design/TASKS.md v1.9 §C（視圖+迭代+匯出+整合）— 你的下一個主軸；註：master 詞彙 Phase D = TASKS 詞彙 Phase C
6. _design/REQUIREMENTS_LOCK.md v1.0 FINAL（north star 不動）
7. _design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md v0.1（Round 10 NEAR-GO；4 finding 入 NEW_REQ_19）
8. _design/D054_DECISION_PACKAGE.md v0.2（D-054 拍板包 APPLIED；含完整 hybrid 設計推理）

**第二步精選讀（碰到才看）：**
9. _design/ARCHITECTURE.md v1.6（§6.4 /view-* 內部架構 + §6.5 /iterate-* + §6.6 /export-* + §6.7 /diagnose+integrate）
10. _design/SPEC.md v1.2（§5.1 entity / §16 文件狀態機 / §16a 09_e LOCKED 降級紀錄）
11. _design/INTEGRATION_CONTRACTS.md v2.1（§5 Contract D L3 Export）
12. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5 §5 Canon Delta（D.6.5 framework）
13. _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2（C.5a Layer 3 Export 規格）
14. _design/UX_SPEC.md v0.4（前端工具 11 個 feature — 預期 10th master 處理；context only）

**你的 scope（master 第九輪整合）：**

1. **接收第八輪 handoff** + 接受 D-001~D-054 全部拍板（含 §6.13 / §6.15 / §6.16 / §6.17）

2. **9th master cleanup queue 處理（推薦先做 — 30-90 分 inline patch；詳 §4.1）：**
   - R8-INFO-06: 00_protocol/00_k v0.1 → v0.2（5→8 報告對齊）+ 階段 3 重寫對齊 D-043 + UD §2.5.3 v0.3
   - R10-MI-01/02/03: 版本 cross-ref sequencing stale（C/R/P/CH skill / phase_b_review_log / PHASE_B）— 用 NEW_REQ_16 lint script 思路一次掃完
   - R10-MA-01 ack（明示 user 加 NEW_REQ_16/17/18 屬正當作業；無需 patch）
   - AGENTS.md / CLAUDE.md Phase C skill table TBD → DONE 標記（C.1/C.2/C.3 + 3 wrapper + 09_g/h/i 模板已落地）
   - 08_a 台詞版本管理規範 §11.1 必要 QA：5 → 8 修正（P-009 對應）

3. **Phase D 主軸（Wave 12 + 13 + 14 + 15）：**
   - Wave 12（5 個 /iterate-* skill + /iterate-scene --split-to-file）：寫 5 個 starter + CODEX 跑 5 skill 實作
   - Wave 13（4 個 /view-* skill）：寫 4 個 starter + CODEX 跑 4 skill 實作
   - Wave 14（4 個 /export-* skill + L3 Export prompt 生成器）：寫 4 個 starter + CODEX 跑 4 skill 實作
   - Wave 15（/diagnose + /integrate + Canon Delta 框架紀錄）：寫 2 個 starter + CODEX 跑 2 skill 實作

4. **Phase D 收尾 + Milestone 4 接近條件聲明（Wave 16）：**
   - 寫 CODEX_D_FINAL_STARTER.md
   - CODEX 跑 Phase D 整體驗收 + 撰寫 PHASE_D_COMPLETION_REPORT.md v1.0
   - 註：Milestone 4 封版完整條件需 Phase A.0F 前端工具補完（屬 10th master 範圍）

5. **寫 HANDOFF_TO_10TH_MASTER.md** 接 Milestone 4 封版（Phase A.0F 前端工具補完 + 真正封版宣告）

6. **（optional）若 user 有新 finding → 緊急 patch round**（同 D-049 / D-051 / D-053 / D-054 模式）

**禁止越界：**
- 不重做設計（已 LOCKED v1.0~v2.0）
- 不改 D-001~D-054 拍板結論（要動需 user 拍板新 D-055+）
- 不擅啟 Phase A.0F 實作（屬 10th master scope；除非 user 明示要在第九輪平行起手）
- 不重審 CODEX 已 accepted 之 finding（Round 8 GO / Round 10 NEAR-GO hard-limit / Wave 11 PASS；殘留 4 finding 入 9th master cleanup queue 一次處理）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 8 份必讀後對 scope + 9th master cleanup queue + Phase D 工作順序的理解，再開始處理。
```

---

# 2. 當前狀態快照（master 第八輪結束時）

## 2.1 設計層狀態（spec 版本）

| 檔 | 版本 | 狀態 | 備註 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | north star，不動 |
| `_design/DECISIONS_LOG.md` | v2.0 | **FINAL** | D-001~D-054 + §6.13 D-051 + §6.15 D-052 + §6.16 D-053 + §6.17 D-054 |
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | **LOCKED** | Contract A/B/C/D（D-047）|
| `_design/SPEC.md` | v1.2 | **LOCKED** | D-047 supersede |
| `_design/ARCHITECTURE.md` | v1.6 | **LOCKED** | §3.3.2 含 D-051 partial supersede note；R7-MA-02 cleanup 已 done |
| `_design/TASKS.md` | v1.9 | **LOCKED** | partial supersede 兩處：D-052 §A.10/§B.5.5/§B.6.5/§B.8 + D-050/D-053 §B.7；含 v1.8→v1.9 ledger backfill |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | **LOCKED** | §2 下游 00_k pipeline 為 Phase C 權威（已落地） |
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 不動；§11 11 個 feature 屬 Phase A.0F 10th master scope |
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 不動；Phase D Wave 14 reference |
| `_design/PHASE_3_COMPLETION_REPORT.md` | v4.0 FINAL | **LOCKED** | 不動 |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | **DRAFT** | Phase A PASS（master 第六輪）|
| `_design/PHASE_B_COMPLETION_REPORT.md` | v1.2 | **DRAFT** | Phase B PASS（含 §6 user 親跑事實摘要 + R9 sweep cleanup）|
| `_design/PHASE_C_COMPLETION_REPORT.md` | v1.0 | **DRAFT** | Phase C PASS（Wave 11 PASS；§6 placeholder 等 user 親跑補入 via NEW_REQ_14 AI-assisted）|
| `_design/POST_LOCK_PENDING.md` | v0.13 | DRAFT | NEW_REQ 整體狀態；NEW_REQ_19 9th master cleanup queue 待 9th master 處理 |
| `_design/D054_DECISION_PACKAGE.md` | v0.2 | **APPLIED** | D-054 拍板包；含 hybrid 設計推理 + 未來 D-055 候選預留 |
| `_design/registries/*.template.yaml` | 3 個 LOCKED | **LOCKED** | entity / qa / issue (D-047) |
| `scripts/parse_frontmatter.py` | A.0.10 patched | DONE | 3 critical fix |
| `00_protocol/00_b ~ 00_l` 8 protocol | mixed | DRAFT | 00_e v0.1 + 00_f/g/h/l v0.2（Wave 6 D-047 patch）+ 00_i v0.3（D-051 patch）+ 00_k v0.1（**5→8 報告 stale 待 9th master cleanup queue 升 v0.2**）|
| `.claude/skills/` 16 skill + 8 wrapper | mixed | DRAFT | Phase A 4 + Phase B 5（含 D-050/D-053 對齊版）+ Phase C 3（scene-task v0.1 / dialogue-write v0.2 / qa v0.1）+ 8 中文 wrapper |
| `09_quality_assurance/` | 9 模板 | DRAFT | 09_a/b/c/d/e/f 既有 + 09_g/h/i 新建（C4 patch round；D-043 8 報告齊全）|

## 2.2 Phase A + Phase B + Phase C 全部完成（Milestone 1 + 2 + 3 達成）

- **Phase A**（Milestone 1）：Wave 1-5 全 PASS（init-project + create-world + status + check-gaps + 4 中文 wrapper + 27 模板 frontmatter）
- **Phase B**（Milestone 2）：Wave 6-8 全 PASS（5 上游 protocol v0.2 + 5 /create-\* skill + 3 REVIEW gate + B.9 整體驗收 + user M2 端到端 testing PASS）
- **Phase C**（Milestone 3）：Wave 9-11 全 PASS（3 個下游 skill /scene-task + /dialogue-write + /qa + 8 個 QA 模板 + D-054 hybrid fallback 落地 + Wave 11 整體驗收 PASS）

## 2.3 第八輪 master 期間累積變動

### Inline patch round 紀錄

| Round | 觸發 | 動作 | 落地 |
|---|---|---|---|
| Cleanup round | Round 7 NEAR-GO 殘留 3 MAJOR + 6 MINOR | R7-MA-01/02/03 + R7-MI-01~06 全處理 | 17 檔 cleanup |
| Round 8 重審 | Cleanup round 後驗證 | CODEX 跑 7 維度檢查 → GO（1 MAJOR + 5 MINOR + 6 INFO）| 1 review report |
| Patch round 2 | Round 8 GO 後處理 R8 finding | R8-MA-01 + R8-MI-01~05 + R8-INFO-02 全處理 | 8 檔 patch |
| Round 9 重審 | Patch round 2 後驗證 | CODEX 跑 5 維度檢查 → NEAR-GO（5 MINOR + 2 INFO）| 1 review report |
| D-054 拍板 | NEW_REQ_13 per-scene 檔 convention 議題 | user 拍板選 1 Hybrid + 未來迭代追蹤 NEW_REQ_15 | DECISIONS_LOG v2.0 §6.17 + POST_LOCK_PENDING v0.10 + D054_DECISION_PACKAGE v0.2 |
| Patch round 3 | Round 9 NEAR-GO 後 R9 finding sweep | R9-MI-01~05 + R9-INFO-02 全處理（用 sweep 模式避免 cascade）| 6 檔 patch |
| Round 10 重審 | Patch round 3 後驗證 | CODEX 跑 4 維度檢查 → NEAR-GO（1 MAJOR + 3 MINOR）；user 拍板 Path A hard-limit accept | 1 review report + POST_LOCK_PENDING v0.12 NEW_REQ_19 |
| Phase C Wave 9 | master 寫 3 starter | C1/C2/C3 starter v0.1 | 3 starter |
| Phase C Wave 10 | CODEX 依序跑 C.1 → C.2 → C.3 | 3 個下游 skill 落地 + 3 中文 wrapper | 6 SKILL.md |
| C4 patch round | C.3 抓出 09_g/h/i 模板缺 → 提前處理 D-043 §D.1a debt | CODEX 建 3 QA 模板 + master starter | 3 模板 + 1 starter |
| Wave 11 第 1 跑 | CODEX 跑整體驗收 | 抓出 C.2 mode_tag enum blocker（master starter typo FINAL → 應 ORGANIZED）| BLOCKED 版本 PHASE_C_COMPLETION_REPORT |
| C.2 mode_tag patch | master inline 修 dialogue-write SKILL.md v0.1 → v0.2 | line 450 FINAL → ORGANIZED + 寫權限段補 ORGANIZED scope | 1 檔 patch |
| Wave 11 第 2 跑 | 修補後重跑 | 4 維度全 PASS | PHASE_C_COMPLETION_REPORT v1.0 PASS |

### 第八輪 master 重要拍板（除 D-054 外無新 D-NNN）

- **D-054**（DECISIONS_LOG v2.0 §6.17）：per-scene 檔 convention 選 1 Hybrid + `/iterate-scene --split-to-file` 屬 Phase D 範圍延後實作 + `/scene-task` 兩階段 fallback；**0 LOCKED spec supersede**（純新增拍板，不動 D-050/00_h/TASKS/UD/SPEC）
- D-001~D-053 全部維持不動

---

# 3. 第九輪工作清單（按執行順序）

## 階段 1：讀完 8 份必讀 + 接受第八輪 handoff（30-60 分）

按順序讀 + 確認對 scope / 9th master cleanup queue / Phase D 工作順序的理解。

## 階段 2：9th master cleanup queue 處理（推薦先做；30-90 分 inline patch）

依 NEW_REQ_19 + R8-INFO-06 + AGENTS.md TBD + 08_a §11.1 等項：

### 必處理項（30-60 分）

1. **00_k v0.1 → v0.2（R8-INFO-06）：**
   - 階段 3 從「5 份 QA」改「8 份 QA」對齊 D-043
   - 序列順序對齊 UD §2.5.3 v0.3（09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i）
   - 9 種 status 齊全 FINAL gate 條件
   - 升 header v0.1 → v0.2 + partial supersede note via D-043

2. **R10-MI-01/02/03 版本 cross-ref sequencing stale（用 sweep 模式）：**
   - phase_b_review_log §4：4 skill version 對齊（CH v0.3 等）
   - PHASE_B_COMPLETION_REPORT §3.2/§4.1/§9：5 skill 版本對齊
   - phase_b_character_review_log Cross-ref：C/R v0.3
   - phase_b_outline_review_log Cross-ref：outline v0.3
   - CODEX_B9_STARTER active checklist：B8/log/skill 版本對齊
   - **方法：用 grep 全掃一次性 sweep，避免 cascade**

3. **R10-MA-01 ack 紀錄：** POST_LOCK_PENDING NEW_REQ_19 已紀錄；無需新 patch（僅 handoff 時明示 user 加 NEW_REQ_16/17/18 屬正當作業）

4. **AGENTS.md / CLAUDE.md Phase C skill table TBD → DONE：**
   - C.1 /scene-task + /場景任務包 標 ✓
   - C.2 /dialogue-write + /生成台詞 標 ✓
   - C.3 /qa + /檢查 標 ✓
   - 09_g/h/i 三模板 標 ✓
   - D-054 hybrid fallback 設計落地 標 ✓

5. **08_a 台詞版本管理規範 §11.1（P-009 對應）：**
   - 必要 QA「5 份」改「8 份」對齊 D-043
   - 屬 LOCKED 模板 — 需 user 明示同意才能改

### 可選項（推 10th master）

6. **NEW_REQ_16 lint script 規劃文檔細化：** 若 9th master 有 wall-time，可寫 spec 文檔；不一定要實作

## 階段 3：Phase D 主軸（Wave 12 + 13 + 14 + 15）

依 TASKS v1.9 §C（注意：master 詞彙的 "Phase D" = TASKS 詞彙的 "Phase C" — 視圖+迭代+匯出+整合 phase）：

### Wave 12：寫 5 個 /iterate-* skill + /iterate-scene --split-to-file

| Skill | 對應 entity | 對應 protocol |
|---|---|---|
| `/iterate-world` | W-rules / V / W-language | 00_protocol/00_j_迭代協議.md（**本 wave 順手寫**）|
| `/iterate-character <name>` | C-* | 同上 |
| `/iterate-relationship <a> <b>` | R-*-* | 同上 |
| `/iterate-outline` | P | 同上 |
| `/iterate-detailed-outline` | CH-* / S-*-* | 同上 |
| **`/iterate-scene <S-ID> --split-to-file`** | S-*-* split 拆檔 | **D-054 NEW_REQ_15 落地**；對齊 hybrid fallback |

工時：master 寫 5 starter + 寫 00_j（2-3 小時）；CODEX 跑 5 skill（2-3 小時 × 5 = 10-15 小時，可並行）

### Wave 13：寫 4 個 /view-* skill

| Skill | 對應 entity |
|---|---|
| `/view-world` | W/V 整合視圖 |
| `/view-character <name>` | C-* + R-* 整合視圖（聲線 + 偏移 + 關係 + 出場場景）|
| `/view-outline` | P 整合視圖 |
| `/view-detailed-outline` | CH-* + S-*-* 整合視圖 |

特殊紀律（O3 鎖定）：視圖屬 `DERIVED` 狀態；只允許寫在 `view/` 目錄；不污染既有實體檔

工時：master 寫 4 starter（2-3 小時）；CODEX 跑 4 skill（2 小時 × 4 = 8 小時）

### Wave 14：寫 4 個 /export-* skill + L3 Export prompt 生成器

| Skill | 對應 |
|---|---|
| `/export-world` | W/V |
| `/export-character <name>` | C-* |
| `/export-outline` | P |
| `/export-detailed-outline` | CH-* + S-*-* |

L3 Export prompt 生成器：屬前端工具範圍（Phase A.0F.x；10th master scope），但 schema 應在本 Wave 確認 / 寫範例

工時：master 寫 4 starter（2-3 小時）；CODEX 跑 4 skill（2 小時 × 4 = 8 小時）

### Wave 15：寫 /diagnose + /integrate + Canon Delta 框架紀錄

| Skill | 目的 |
|---|---|
| `/diagnose` | 跨檔診斷（找衝突 / LOCKED 變動 / orphan 實體）|
| `/integrate` | 整合（merge 跨 source）|

Canon Delta 框架紀錄（TASKS §D.6.5；不實作 skill）：寫 `_design/CANON_DELTA_FRAMEWORK.md`（或入 TASKS 末附錄）

工時：master 寫 2 starter + Canon Delta 框架（2-3 小時）；CODEX 跑 2 skill（2 小時 × 2 = 4 小時）

## 階段 4：Phase D 收尾 + Milestone 4 接近條件聲明（Wave 16）

- 寫 `CODEX_D_FINAL_STARTER.md`
- CODEX 跑 Phase D 整體驗收 + 撰寫 `_design/PHASE_D_COMPLETION_REPORT.md` v1.0
- §6 user 親跑端到端 placeholder（NEW_REQ_14 AI-assisted §6 補入機制可使用；NEW_REQ_14 設計時已預留）
- **Milestone 4 接近條件聲明（非達成宣告）：** Phase D 完成；剩 Phase A.0F 前端工具補完 = 真正 Milestone 4 封版（屬 10th master 範圍）

## 階段 5：升 Milestone 4 接近條件 + 寫 10th master handoff

Phase D PASS → 接近 Milestone 4 封版 → 寫 `HANDOFF_TO_10TH_MASTER.md` 接 Phase A.0F 前端工具補完 + 封版宣告（Milestone 4 達成）

---

# 4. 風險警示 + 重要紀律

## 4.1 9th master cleanup queue 詳細列表（NEW_REQ_19）

| Finding | 嚴重程度 | Cleanup 優先 | 內容 |
|---|---|---|---|
| R8-INFO-06 | INFO（影響範圍中）| 高 | 00_protocol/00_k v0.1 → v0.2（5→8 報告 + 序列順序對齊 D-043 + 9 種 status FINAL gate 條件）|
| R10-MI-01 | MINOR | 中 | phase_b_review_log §4 + PHASE_B §3.2/§4.1 + CODEX_B9_STARTER 多處 CH v0.2 應為 v0.3（patch round 3 sequencing cascade）|
| R10-MI-02 | MINOR | 中 | phase_b_review_log §4 review-log 版本 stale（character v0.2 / outline v0.3 應為 v0.3 / v0.4）|
| R10-MI-03 | MINOR | 中 | PHASE_B 仍引用 CODEX_B9_STARTER v0.3（應 v0.4）|
| R10-MA-01 ack | MAJOR ack | 高 | user 加 NEW_REQ_16/17/18 屬正當作業；明示 authorize；無需 patch |
| AGENTS.md / CLAUDE.md Phase C skill table | INFO（PHASE_C_COMPLETION_REPORT §8 標）| 高 | Phase C 3 skill + 3 wrapper + 09_g/h/i 模板補完後標 ✓ DONE |
| 08_a §11.1 P-009 | MINOR | 低 | 必要 QA「5 份」→「8 份」對齊 D-043；屬 LOCKED 模板需 user 明示同意才能改 |

詳見 `_design/POST_LOCK_PENDING.md` v0.13 NEW_REQ_19 + Round 10 report §7。

**警示：** 9th master cleanup queue 不阻 Phase D 主軸啟動（屬文檔層級 stale）— 但建議優先處理 R8-INFO-06 (00_k v0.1)，因 00_k 是 /qa skill 對應 protocol，若 9th master 進 Phase D Wave 12 後仍是 stale，會 propagate 到 /iterate-* / /view-* / /export-* / /diagnose / /integrate 新 skill 設計時的 ref。

## 4.2 NEW_REQ deferred 清單（給 9th master 處理時機）

| NEW_REQ | 性質 | 推薦處理時機 |
|---|---|---|
| **NEW_REQ_11** 翻譯工具分支 | Future fork tool B | DEFERRED 至工具 A 封版後（屬 11+ 輪 master scope）|
| **NEW_REQ_12** RESOLVED via D-053 | 已解決 | — |
| **NEW_REQ_13** RESOLVED via D-054 | 已解決 | — |
| **NEW_REQ_14** PHASE_X §6 AI-assisted 補入 | UX 改進；同 D-052 模式 | 9th master Phase D Wave 16 / 收尾驗收 starter 設計時實作 |
| **NEW_REQ_15** D-054 hybrid 迭代評估 | Future D-055 候選追蹤 | Phase D 期間 monitor trigger A/B/C/D；達成則開 D-055 |
| **NEW_REQ_16** Cross-ref Consistency Lint Script | Future 自動化 | Phase D 期間考慮實作（11th master 也可）|
| **NEW_REQ_17** Auto-patcher | DEFERRED 至封版後 | 11+ 輪 master scope |
| **NEW_REQ_18** Nightly AI-driven Semantic Review | DEFERRED 至翻譯工具 fork 前 | 11+ 輪 master scope |
| **NEW_REQ_19** 9th master cleanup queue | DEFERRED — Round 10 殘留 | **9th master Phase D 啟動前處理（推薦）** |

## 4.3 D-054 NEW_REQ_15 迭代條件 monitor（給 9th master 追蹤）

第八輪 master 拍板 D-054 選 1 Hybrid 同時記錄未來迭代 trigger 條件。9th master Phase D 期間需 monitor：

| trigger | 條件 | 對應評估動作 |
|---|---|---|
| **A** | user 寫 ≥ 30 場後回報「聚合 06_a 太大」 | 評估 D-055 全 per-scene supersede |
| **B** | `/iterate-scene --split-to-file` 實作後 user 連續 ≥ 5 次拆檔 | 評估「per-scene 變預設」（hybrid 反向）|
| **C** | 工具 B 翻譯 / 其他多 agent 並行需求出現 | 評估 per-scene 對 race condition 緩解 |
| **D** | 聚合 06_a 持續發生 git merge friction | 評估拆檔降低 conflict |

任一 trigger 達成 → 9th master 開 D-055 拍板包（3 候選選項：A per-scene 變預設 / B 強制全 per-scene / C 維持 hybrid + `/iterate-aggregate-to-split-all`）。

詳見 `_design/POST_LOCK_PENDING.md` v0.13 NEW_REQ_15。

## 4.4 Phase A.0F 前端工具未處理（10th master 必處理）

封版條件之一。當前狀態：A.0F.0~A.0F.2 alpha 完成；A.0F.3~A.0F.11 + 整體驗收未做。

**推薦在第 10 輪 master 對話處理**（Phase D 完成後；屬 Milestone 4 封版必須）。

詳見 TASKS v1.9 §A.0F.3~A.0F.11 + UX_SPEC §11 11 個 feature spec。

## 4.5 sandbox virtiofs cache stale 已知問題（HANDOFF §4.5 既有警示沿用）

工作目錄 Windows 端為權威。Sandbox 端 git status / wc -l / ls mtime 偶爾顯示 stale。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 4.6 「Fix one, find two」cascade pattern 教訓（給 9th master 紀律）

第八輪 master 連 3 輪 patch round 都出現同類型 version cross-ref sequencing cascade（Round 9 5 MINOR / Round 10 4 finding / Wave 11 1 blocker）。根因：

1. 同 patch round 內 sequential task 寫 cross-ref 時不知道後面 task 會升版
2. 缺自動化 cross-ref checker（NEW_REQ_16 lint script 規劃中）

**9th master 紀律建議：**

- **patch round 開始前**：用 grep 全掃版本 cross-ref；列出所有 active stale；一次性 sweep（vs patch round 2 局部修補導致 cascade）
- **每個 patch task 開始前**：先決定本輪所有檔案的目標版本；統一 cascade（vs 邊改邊升 cascade）
- **patch round 結束前**：再跑 grep 全掃 verify 沒新 stale 引入
- **未來**：等 NEW_REQ_16 lint script 實作後自動化

## 4.7 master starter typo 教訓（第八輪 Wave 11 blocker 啟示）

第八輪 master 寫 CODEX_C2_STARTER 時 mode_tag enum typo（FINAL 應為 ORGANIZED）— CODEX 忠實實作 → Wave 11 對齊 SPEC 抓出 → master inline patch 修補。

**9th master 紀律建議：**

- **寫 starter 含 spec enum 引用時**：先 grep SPEC / parser code verify enum 列表完整 + 拼字正確
- **CODEX 對 spec enum 屬「忠實實作」性質**：starter 寫錯 = skill 寫錯 = blocker；責任在 master 寫 starter
- **驗收時 CODEX 對 spec enum 屬「rigorous verify」性質**：能抓出 starter typo 是 review 的價值

---

# 5. 完成條件

第九輪整合對話完成 = 以下全部 ✓：

```
✓ 9th master cleanup queue 處理（推薦先做）— NEW_REQ_19 + R8-INFO-06 + AGENTS.md TBD 全處理完
✓ Phase D Wave 12 — 5 個 /iterate-* + /iterate-scene --split-to-file starter 寫好 + skill 跑通
✓ Phase D Wave 13 — 4 個 /view-* starter 寫好 + skill 跑通
✓ Phase D Wave 14 — 4 個 /export-* starter 寫好 + skill 跑通 + L3 Export schema 確認
✓ Phase D Wave 15 — /diagnose + /integrate + Canon Delta 框架紀錄
✓ Phase D Wave 16 — PHASE_D_COMPLETION_REPORT v1.0 PASS
✓ user 通知接近 Milestone 4（剩 Phase A.0F 前端工具補完 = 10th master 範圍）
✓ Milestone 4 接近條件聲明
✓ 寫 HANDOFF_TO_10TH_MASTER.md 接 Phase A.0F + 封版
```

---

# 6. 文件維護紀律

- 本檔是「接手指南」，第九輪 master 對話讀完後**不需要更新本檔**
- 若第九輪發現本檔不準確 → 標 errata 在第十輪接手包（如有）
- 第九輪完成後可把本檔 archive 進 `_design/archive/`

---

# 7. 對 user 的最終建議（master 第八輪結束時）

## 7.1 立即可做的事

1. **commit + push 第八輪所有變更**（用 master 提供的 GIT SUMMARY 命令）
2. **M3 user-test（可選但推薦）：** 在 Phase B M2 testing Instance（`<instance_root>/`；user 之前 M2 testing 用的本地 Instance repo 即可）內跑完整 3 下游 skill chain（/scene-task → D.2.5 gate → /dialogue-write → D.3.5 gate → /qa 8 報告）
3. **NEW_REQ_14 AI-assisted §6 補入（可選）：** M3 testing 跑完後告訴 8th master（或 9th master 接手前）— master 用 D-052 同模式從 phase_log / git log / review_log reconstruct §6 事實 → user 拍板 OK → 落地

## 7.2 進 Phase D 的條件達成

- ✓ Phase C 3 個下游 skill 全可跑
- ✓ 8 個 QA 模板齊全（含 09_g/h/i C4 patch round 補建）
- ✓ D-054 hybrid fallback 設計落地
- ✓ Milestone 3 達成（PHASE_C_COMPLETION_REPORT v1.0 PASS）
- ✓ 50+ entities 全 ≥ REVIEW（含 W/V/C/R/P/CH/S）
- ✓ 9th master cleanup queue 明示 handoff 範圍

達成後 user 可進入：

```
Phase D（Wave 12 ~ Wave 16）
  9th master cleanup queue 處理（推薦先做）
   ↓
  Wave 12 — /iterate-* 5 skill + /iterate-scene --split-to-file
   ↓
  Wave 13 — /view-* 4 skill
   ↓
  Wave 14 — /export-* 4 skill + L3 Export 規格
   ↓
  Wave 15 — /diagnose + /integrate + Canon Delta 框架
   ↓
  Wave 16 — Phase D 整體驗收
   ↓
🟡 Milestone 4 接近條件達成（剩 Phase A.0F 前端工具 = 10th master 範圍）
```

## 7.3 user-test 第四次點時機（M4）

Phase D 完成 + Phase A.0F 完成後可做 M4 user-test：跑完整工具 A pipeline（從 /init-project → 5 個 /create-* → /scene-task → /dialogue-write → /qa → /view-* / /export-* / /iterate-* / /diagnose+integrate）+ 前端工具實際使用。

## 7.4 Phase E / 工具 B 路徑（第 11+ 輪之後）

- **第 10 輪 master：** Phase A.0F 前端工具補完 + 真正 Milestone 4 封版宣告
- **第 11+ 輪 master（optional）：** NEW_REQ_11 翻譯工具分支 fork（工具 B：`game-dialogue-translator`）
- **維護期：** NEW_REQ_16/17/18 自動化 QA 工具階段性實作 + NEW_REQ_15 D-054 迭代評估 monitor

詳見第八輪 master 對話內展開的全 lifecycle 地圖（user 已要求整理為「完整後續開發地圖」）。

---

**祝第九輪 master 整合順利。Milestone 3 → Milestone 4 接近的關鍵是把 Phase D 視圖 / 迭代 / 匯出 / 整合 全部上線；前面 Phase A + B + C 已把「資料庫 + 上游 + 下游」全鏈打通。**

# 8. Cross-ref

- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0（第八輪 master scope 紀錄；本檔接續）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Phase C 完成事實檔；Milestone 3 達成宣告）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054（per-scene 檔 convention Hybrid 拍板背景）
- `_design/POST_LOCK_PENDING.md` v0.13（NEW_REQ 整體狀態；NEW_REQ_19 9th master cleanup queue）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 拍板包 APPLIED）
- `_design/TASKS.md` v1.9（含 D-054 紀錄 + Phase D §C task scope）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO 紀錄 — 9th master cleanup queue 起點）
- `_design/CODEX_C_FINAL_STARTER.md` v0.1（Wave 11 整體驗收 starter）
- `_design/CODEX_C1_STARTER.md` v0.1 / `_design/CODEX_C2_STARTER.md` v0.1 / `_design/CODEX_C3_STARTER.md` v0.1 / `_design/CODEX_C4_PATCH_STARTER.md` v0.1（Phase C Wave 9-10 starter）
- `00_protocol/00_k_台詞生產流程協議.md` v0.1（下游 protocol；R8-INFO-06 5→8 報告 stale 待 9th master 升 v0.2）
- `.claude/skills/scene-task/SKILL.md` v0.1 + `.claude/skills/dialogue-write/SKILL.md` v0.2 + `.claude/skills/qa/SKILL.md` v0.1（Phase C 3 下游 skill）
- `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1 + `09_h_對話張力檢查模板.md` v0.1 + `09_i_跨場一致性檢查模板.md` v0.1（C4 patch round 補建）
