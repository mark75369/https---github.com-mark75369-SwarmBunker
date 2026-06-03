狀態：DRAFT  
版本：v1.0（第七輪 master 收尾交接包；Phase B + Milestone 2 達成 + 7 輪 CODEX 重審 hard-limit accepted；Phase C handoff）  
最後更新：2026-05-21  
適用範圍：給「第八輪整合 master」對話的接手包 — Phase C 啟動 + Round 7 NEAR-GO 殘留 cleanup 起手  
優先級：最高

# HANDOFF_TO_8TH_MASTER — 第八輪整合 master 對話接手包

# 0. 文件目的

第七輪 master 對話完成 — **Milestone 2 達成宣告（Phase B 全 5 上游 /create-\* skill + 3 REVIEW gate + Wave 8 收尾全 PASS）**。

第七輪 master 期間經 **7 輪 CODEX 全面重審**，hard-limit Round 7 NEAR-GO accepted。期間發現 + 處理重大議題：
- D-049 第二道防線 over-broad bug → **D-051 partial supersede** 解決
- D-050 vs /create-world 衝突 → **D-053 partial supersede** 解決
- B.5.5/B.6.5/B.8 review gate manual upgrade UX friction → **D-052 AI-assisted 雙模式** 解決
- DECISIONS_LOG + PHASE_B truncation incident（§6.16 round 1）→ git history recovery 解決

第八輪 master 對話接手 **Phase C（下游台詞生產）** + Round 7 殘留 cleanup。

**第八輪預期工作（Phase C — 下游台詞生產）：**
1. 接收第七輪 handoff + 接受 D-001 ~ D-053 + 所有 §6.X 拍板
2. **Cleanup round（推薦先做）：** 處理 Round 7 殘留 3 MAJOR + 6 MINOR（30-60 分鐘）
3. **Phase C 主軸：** 寫 3 個下游 skill starter（/scene-task + /dialogue-write + /qa + 3 中文 wrapper）
4. CODEX 跑 3 個 skill 實作
5. Phase C 整體驗收 → **Milestone 3 達成**（user 可開始量產台詞）

**預估第八輪總工時：** Cleanup 30-60 分鐘 + Phase C master 對話 1-2 小時 + CODEX 3-5 小時 + user 量產台詞 75-150 小時（依作品規模）

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。第七輪 master 對話完成 Phase B 收尾（Wave 7-8 + B.5.5/B.6.5/B.7/B.8/B.9 全 PASS + 5 個 /create-* skill 全落地 + D-051 + D-052 + D-053 inline patch round + 7 輪 CODEX 全面重審 hard-limit Round 7 NEAR-GO accepted），Milestone 2 達成（2026-05-21）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第八輪整合 master」對話。

**第一步必讀（按順序，8 份）：**
1. _design/HANDOFF_TO_8TH_MASTER.md（本檔，你的 scope）
2. _design/PHASE_B_COMPLETION_REPORT.md v1.1（Phase B 完成事實檔；含 §6 user 親跑端到端完整紀錄）
3. _design/DECISIONS_LOG.md §6.13 / §6.15 / §6.16（D-051 + D-052 + D-053 拍板背景）+ §6.16.4 升 v1.9 後紀律
4. _design/TASKS.md v1.9（B Phase 完成；C Phase 任務拆解 — 你的下一個主軸）
5. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5 §2（00_k 下游 protocol 完整內容）
6. _design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND7.md v0.1（重審最終狀態 + 殘留 finding 清單）
7. _design/REQUIREMENTS_LOCK.md v1.0 FINAL（north star 不動）
8. _design/POST_LOCK_PENDING.md v0.9（NEW_REQ_11 翻譯工具 DEFERRED / NEW_REQ_12 RESOLVED via D-053 / NEW_REQ_13 per-scene 檔 DEFERRED / NEW_REQ_14 §6 AI-assisted DEFERRED）

**第二步精選讀（碰到才看）：**
9. _design/ARCHITECTURE.md v1.5（§3.3.2 D-051 partial supersede note 後狀態）
10. _design/SPEC.md v1.2（§5.1 entity / §5.3 完成度 / §17 7 anchor）
11. _design/INTEGRATION_CONTRACTS.md v2.1（§2 Contract A / §3 Contract B / §4a Contract D D-047）
12. _design/DATA_FORMAT_SPEC.md v0.4（§3.2 phase_log / §4.2 dialogue_keys / §7.2 entity_type_registry / §8 qa_type_registry）

**你的 scope（master 第八輪整合）：**

1. **接收第七輪 handoff** + 接受 D-001~D-053 全部拍板（含 §6.13 / §6.15 / §6.16）

2. **推薦先做 Cleanup round** — 處理 Round 7 殘留 finding（30-60 分鐘 inline patch；詳 §4.1）
   - R7-MA-01: TASKS top summary partial supersede ledger
   - R7-MA-02: ARCH §3.3.2 完整 cleanup
   - R7-MA-03: 3 review gate starter active wording reconciliation
   - R7-MI-01~06: docs MINOR cleanup

3. **Phase C 主軸（Wave 9 + Wave 10 + Wave 11）：**
   - Wave 9：寫 3 個 starter（/scene-task + /dialogue-write + /qa）+ 對應 protocol（00_k 已 LOCKED；不寫新 protocol）
   - Wave 10：CODEX 依序跑 3 個 skill 實作（不可平行 — /scene-task → /dialogue-write → /qa 依賴鏈）
   - Wave 11：Phase C 整體驗收 + 升 PHASE_C_COMPLETION_REPORT.md v1.0 → Milestone 3

4. **Phase C 收尾後升 Milestone 3**（下游 3 skill 全 PASS → user 可量產台詞）

5. **寫 HANDOFF_TO_9TH_MASTER.md** 接 Phase D（視圖 + 迭代 + 匯出 + 整合）

6. **（optional）若 user 有新 finding → 緊急 patch round**（同 D-049 / D-051 / D-053 模式）

**禁止越界：**
- 不重做設計（已 LOCKED v1.0~v1.9）
- 不改 D-001~D-053 拍板結論（要動需 user 拍板新 D-054+）
- 不擅啟 Phase D 實作（屬下一階段 master scope）
- 不重審 7 輪 CODEX 重審已 accepted 之 finding（Round 7 NEAR-GO 已 hard-limit accepted；殘留入 8th master cleanup）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

請先回報你讀完 8 份必讀後對 scope + Cleanup + Phase C 工作順序的理解，再開始處理。
```

---

# 2. 當前狀態快照（master 第七輪結束時）

## 2.1 設計層狀態（spec 版本）

| 檔 | 版本 | 狀態 | 備註 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | north star，不動 |
| `_design/DECISIONS_LOG.md` | v1.9 | **FINAL** | D-001~D-053 + §6.13 D-051 + §6.15 D-052 + §6.16 D-053 |
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | **LOCKED** | Contract A/B/C/D（D-047）|
| `_design/SPEC.md` | v1.2 | **LOCKED** | D-047 supersede |
| `_design/ARCHITECTURE.md` | v1.5 | **LOCKED** | §3.3.2 含 D-051 partial supersede note；R7-MA-02 殘留待 cleanup |
| `_design/TASKS.md` | v1.9 | **LOCKED** | partial supersede 兩處：D-052 §A.10/§B.5.5/§B.6.5/§B.8 + D-050/D-053 §B.7；R7-MA-01 top summary 殘留 |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | **LOCKED** | §2 下游 00_k 為 Phase C 權威 |
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 不動 |
| `_design/PHASE_3_COMPLETION_REPORT.md` | v4.0 FINAL | **LOCKED** | 不動 |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | **DRAFT** | Phase A PASS（master 第六輪）|
| `_design/PHASE_B_COMPLETION_REPORT.md` | v1.1 | **DRAFT** | Phase B PASS（含 §6 user 親跑事實摘要 + §6.16 重審 cross-ref 更新）|
| `_design/POST_LOCK_PENDING.md` | v0.9 | DRAFT | NEW_REQ_1~12 RESOLVED；NEW_REQ_2 持續寫作；NEW_REQ_11 / 13 / 14 DEFERRED；NEW_REQ_9 / 10 紀錄 |
| `_design/registries/*.template.yaml` | 3 個 LOCKED | **LOCKED** | entity / qa / issue (D-047) |
| `scripts/parse_frontmatter.py` | A.0.10 patched | DONE | 3 critical fix |
| `00_protocol/00_b ~ 00_l` 8 protocol | mixed | DRAFT | 00_e v0.1 + 00_f/g/h/l v0.2（Wave 6 D-047 patch）+ 00_i v0.3（D-051 patch）+ 其他 |
| `.claude/skills/` 11 skill + 6 wrapper | mixed | DRAFT | Phase A 4 + Phase B 5（含 D-050 對齊版）+ 6 中文 wrapper |

## 2.2 Phase A + Phase B 全部完成（Milestone 1 + 2 達成）

- **Phase A**（Milestone 1）：Wave 1-5 全 PASS（init-project + create-world + status + check-gaps + 4 中文 wrapper + 27 模板 frontmatter）
- **Phase B**（Milestone 2）：Wave 6-8 全 PASS（5 上游 protocol v0.2 + 5 /create-\* skill + 3 REVIEW gate + B.9 整體驗收 + user M2 端到端 testing PASS）

## 2.3 第七輪 master 期間累積變動

### Inline patch round 紀錄

| Round | 觸發 | 動作 | 落地 |
|---|---|---|---|
| Wave 7 起手 | HANDOFF v1.1 erratum | B.5.5 + B.6.5 起手包 + 2 review_log 骨架 | 4 檔新建 |
| Wave 8 三 starter | 同上 | B.7 + B.8 + B.9 starter + phase_b_review_log 骨架 | 4 檔新建 |
| **D-049 patch** | user M2 testing 跑 /init-project 被擋 | **D-051 partial supersede D-049 第二道防線** | 00_i v0.3 + init-project SKILL.md v0.3 + DECISIONS_LOG v1.6 |
| **D-052 patch** | user M2 testing review gate UX friction | **AI-assisted review gate 雙模式** | TASKS v1.9 + 3 starter v0.2/v0.3 + DECISIONS_LOG v1.8 + POST_LOCK_PENDING v0.5~v0.8 |
| **§6.16 truncation incident** | Round 1 §6.16 patch 截斷 810 行 | git history recovery + 重新 apply | DECISIONS_LOG 恢復 + 重做 patch |
| **D-053 patch** | Round 1 重審抓 CR-01 critical | **D-053 partial supersede D-050 子裁決 1** | DECISIONS_LOG v1.9 + POST_LOCK_PENDING v0.9 NEW_REQ_12 RESOLVED |
| **Round 2-7 patch rounds** | 7 輪 CODEX 重審 | Cross-ref / stale ref / starter / spec cleanup | 多檔 partial supersede |

### 7 輪 CODEX 重審收斂軌跡

| Round | 結果 | MAJOR 變化 | 性質 |
|---|---|---|---|
| 1 | NO-GO | 4 MAJOR + 2 CRITICAL | 真實 spec 衝突 + 合規破洞 |
| 2 | NO-GO | 6 MAJOR | truncation incident（已 recovery）|
| 3 | NO-GO | 6 MAJOR | cross-doc drift / 殘留 reference |
| 4 | NEAR-GO | 3 MAJOR | starter body 殘留 |
| 5 | NEAR-GO | 4 MAJOR | LOCKED spec stale wording 新檢出 |
| 6 | NEAR-GO | 4 MAJOR | LOCKED partial supersede 標記不完整 |
| 7 | **NEAR-GO accepted** | 3 MAJOR + 6 MINOR | hard-limit accepted；給 8th master cleanup |

---

# 3. 第八輪工作清單（按執行順序）

## 階段 1：讀完 8 份必讀 + 接受第七輪 handoff（30-60 分）

按順序讀 + 確認對 scope / Cleanup / Phase C 工作順序的理解。

## 階段 2：Cleanup round（推薦先做；30-60 分鐘 inline patch）

依 Round 7 報告 §12 處理殘留 3 MAJOR + 6 MINOR：

### 3 MAJOR cleanup（依優先序）

1. **R7-MA-03（最優先）：** 3 review gate starter（B.55 / B.65 / B.8）「性質」「身份與職責」「不變範圍 / 完成判定」段全面對齊 D-052 雙模式 — 未經 user 拍板不得自行升；user 明示拍板後可 AI-assisted；manual 是 fallback
2. **R7-MA-02：** ARCH §3.3.2 行 633 / 639-642 — 完整 cleanup D-049 兩道防線 active wording → D-051 後單 marker；或明確標 historical-only
3. **R7-MA-01：** TASKS v1.9 header 補一段 partial supersede ledger — 列 D-052 四 gate + D-050/D-053 §B.7 兩項

### 6 MINOR cleanup（可一併處理）

- R7-MI-01: PHASE_B report §3.2 `phase_b_review_log.md v0.1 存在` → v0.3
- R7-MI-02: PHASE_B report D-052 row `DECISIONS_LOG v1.8` → v1.9
- R7-MI-03: 4 個 Phase B 中文 wrapper 仍用「D-049 Template-detect 兩道防線」概括 → 改 D-051 後單 marker 描述
- R7-MI-04: create-world / create-character / create-relationship frontmatter description 加 D-050/D-053 mention
- R7-MI-05: phase_b review_log skeleton usage text 加 D-052 雙模式 wording
- R7-MI-06: POST_LOCK_PENDING NEW_REQ_8 描述補 D-051 partial supersede note

### Cleanup 工時 + 驗證

- 工時：**30-60 分鐘** inline patch
- 跑完 `python -X utf8 scripts/check_headers.py`（0 ERROR 維持）+ `python -X utf8 scripts/check_paths.py`（baseline +0）
- push cleanup commit
- （optional）dispatch CODEX 跑 Round 8 重審驗證 — **但屬可選；user 可直接接受並進 Phase C**

## 階段 3：Phase C Wave 9 — 3 個下游 skill starter（master 寫）

依 TASKS v1.9 §C（注意：TASKS §C 暫未細寫；以 UPSTREAM_DOWNSTREAM_SPEC §2 + 00_k protocol 為權威）：

| Starter | 對應 skill | 對應 protocol | UD § |
|---|---|---|---|
| `_design/CODEX_C1_STARTER.md` | /scene-task `<S-ID>` + /場景任務包 wrapper | 00_protocol/00_k_台詞生產流程協議 | §2.1-§2.4 |
| `_design/CODEX_C2_STARTER.md` | /dialogue-write `<S-ID>` + /生成台詞 wrapper | 00_k §4 多版本生成 | §2.5-§2.8 |
| `_design/CODEX_C3_STARTER.md` | /qa `<dialogue_path>` + /檢查 wrapper | 09_a~09_i QA 模板 + 00_k §3 | §2.9-§2.11 |

**重要設計拐點（D-052 後沿用）：**
- starter 採 outer agent-prompt fence `~~~`（NEW_REQ_10 慣例）
- Instance-only path 前綴 `<instance_root>/`
- 若有 user 拍板 review gate（例：dialogue REVIEW gate），採 D-052 雙模式預設

**NEW_REQ_13 per-scene 檔 convention 必處理：** Phase C /scene-task 需先拍板 per-scene vs aggregate convention（D-054 候選）— 詳 POST_LOCK_PENDING NEW_REQ_13。

## 階段 4：Phase C Wave 10 — CODEX 跑 3 skill 實作

依序跑（依賴鏈不可平行）：

1. CODEX 跑 /scene-task starter → 寫 `.claude/skills/scene-task/SKILL.md` + 中文 wrapper
2. CODEX 跑 /dialogue-write starter → 寫 `.claude/skills/dialogue-write/SKILL.md` + 中文 wrapper
3. CODEX 跑 /qa starter → 寫 `.claude/skills/qa/SKILL.md` + 中文 wrapper

每 skill CODEX 對話 30-60 分鐘。

## 階段 5：Phase C Wave 11 — Phase C 整體驗收

- 寫 `CODEX_C_FINAL_STARTER.md`（同 B.9 模式）
- CODEX 跑驗收 + 撰寫 `_design/PHASE_C_COMPLETION_REPORT.md` v1.0
- §6 user 親跑端到端 placeholder（NEW_REQ_14 AI-assisted §6 補入機制可順手實作）
- Milestone 3 達成

## 階段 6：升 Milestone 3 + 寫 9th master handoff

Phase C PASS → Milestone 3「下游 3 skill 完成 → user 可量產台詞」達成 → 寫 `HANDOFF_TO_9TH_MASTER.md` 接 Phase D（視圖 + 迭代 + 匯出 + 整合）

---

# 4. 風險警示 + 重要紀律

## 4.1 Round 7 NEAR-GO 殘留 finding（hard-limit accepted）

| Finding | 嚴重程度 | Cleanup 優先 |
|---|---|---|
| R7-MA-01 TASKS top summary partial supersede ledger | MAJOR | 高 |
| R7-MA-02 ARCH §3.3.2 active wording cleanup | MAJOR | 高 |
| R7-MA-03 3 review gate starter active wording reconciliation | MAJOR | **最高（影響未來 review gate 跑法）** |
| R7-MI-01~06 docs MINOR | MINOR | 中 |

詳見 `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND7.md` v0.1 §10-§12。

**警示：** Round 7 殘留**不阻 Phase C 啟動**（runtime 已 PASS）— 但**未 cleanup 會持續累積文檔 drift**；建議 8th master 先 cleanup 再 Phase C。

## 4.2 NEW_REQ deferred 清單（給 8th master 處理時機）

| NEW_REQ | 性質 | 推薦處理時機 |
|---|---|---|
| **NEW_REQ_11** 翻譯工具分支 | Future fork tool B | DEFERRED 至工具 A 封版後（屬第 11+ 輪 master scope）|
| **NEW_REQ_12** RESOLVED via D-053 | 已解決 | — |
| **NEW_REQ_13** per-scene 檔 convention | Phase C /scene-task 設計拐點 | **Phase C Wave 9 起手時 — open D-054 拍板** |
| **NEW_REQ_14** §6 補入 AI-assisted | Phase C 收尾 starter 設計 | Phase C Wave 11 (CODEX_C_FINAL_STARTER) 設計時實作 |

## 4.3 Phase A.0F 前端工具 — 封版前必處理

**第七輪 master 期間 lifecycle 規劃漏記：Phase A.0F 前端工具 phase。**

當前狀態：
- A.0F.0~A.0F.2 alpha 完成（Project Dashboard / 8 API endpoint / build 規格）
- **A.0F.3~A.0F.10 + A.0F.11 整體驗收 — 未做**（8 個 frontend feature + 整體驗收）

封版條件（Milestone 4）必包含 Phase A.0F 完成。

**推薦在第 11 輪 master 對話處理**（與 Phase D 平行；前後端解耦可平行跑）。

詳見 TASKS v1.9 §A.0F.3~A.0F.11 + UX_SPEC §11 11 個 feature spec。

## 4.4 baseline 設門檻紀律（NEW_REQ_9 教訓）

未來新 baseline gate 設定務必：
- 用 user 環境（Windows）跑 baseline 而非 master sandbox（Linux）
- check_paths.py Windows baseline 254 ERROR / sandbox 242-243 ERROR — diff 屬環境差異
- starter 內 baseline 數字寫死前須 verify 兩端差異

## 4.5 sandbox virtiofs cache stale 已知問題（HANDOFF §4.4 既有警示沿用）

工作目錄 Windows 端為權威。Sandbox 端 git status / wc -l / ls mtime 偶爾顯示 stale。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 4.6 §6.16 truncation incident 教訓（紀律）

第七輪 master 期間發生過 1 次嚴重 truncation：Round 1 §6.16 patch 把 DECISIONS_LOG + PHASE_B 截斷 810+50 行。原因：Python sed 批量處理同檔 + UnicodeDecodeError exception 容易截斷。

**新紀律（已紀錄 DECISIONS_LOG §6.16.3）：**
- 大型 inline patch 不用 Python sed 批量處理（exception 容易截斷）
- 用 Edit tool 逐個 patch + 每次 wc -l verify 行數差
- 大檔 patch 後立刻用 Read / Grep tool（Windows 端權威）verify 完整性

## 4.7 review gate starter 雙模式（D-052）— Phase C 啟動前確認

D-052 後 review gate starter 採「AI-assisted 預設 / manual fallback」雙模式。若 Phase C 設計新 review gate（例：dialogue REVIEW gate），採同雙模式 + 加 D-052 cross-ref。

---

# 5. 完成條件

第八輪整合對話完成 = 以下全部 ✓：

```
✓ Cleanup round（推薦先做）— Round 7 3 MAJOR + 6 MINOR 處理完
✓ Phase C Wave 9 — 3 starter 寫好
✓ Phase C Wave 10 — 3 skill 跑通 + commit/push
✓ Phase C Wave 11 — PHASE_C_COMPLETION_REPORT v1.0 升 PASS
✓ 3 個 /scene-task / /dialogue-write / /qa skill 全可跑（+ 3 個中文 wrapper）
✓ user 通知可以進 Phase D Wave 12（C.1 /view-* + C.2 /export-* + C.3 /iterate-* + C.4 /diagnose+integrate）
✓ Milestone 3 達成宣告
✓ 寫 HANDOFF_TO_9TH_MASTER.md 接 Phase D
```

---

# 6. 文件維護紀律

- 本檔是「接手指南」，第八輪 master 對話讀完後**不需要更新本檔**
- 若第八輪發現本檔不準確 → 標 errata 在第九輪接手包（如有）
- 第八輪完成後可把本檔 archive 進 `_design/archive/`

---

# 7. 對 user 的最終建議（master 第七輪結束時）

## 7.1 立即可做的事

1. **commit + push 第七輪所有變更**（用 master 提供的 GIT SUMMARY 命令）
2. **可選：** Cleanup round 推薦在 8th master 對話內做（30-60 分鐘 + 一個 patch commit）
3. **可選：** 用 Phase B M2 testing Instance（`D:\my-test-instance`）直接接著做 Phase C testing — 不必重 clone

## 7.2 進 Phase C 的條件達成

- ✓ Phase B 5 個上游 skill 全可跑
- ✓ 5 protocol v0.2 D-047 對齊
- ✓ 3 個 REVIEW gate starter 含 D-052 雙模式
- ✓ Milestone 2 達成（PHASE_B_COMPLETION_REPORT v1.1 + §6 user 親跑事實摘要）
- ✓ 50+ entities 全 ≥ REVIEW（含 W/V/C/R/P/CH/S）
- ✓ Round 7 NEAR-GO accepted（runtime PASS；殘留 cleanup 推 8th master）

達成後 user 可進入：

```
Phase C（C.1 ~ C.3）
  Cleanup round（推薦先做）
   ↓
  Wave 9 — 3 starter 寫好
   ↓
  Wave 10 — CODEX 跑 3 skill
    /scene-task → /dialogue-write → /qa（依序）
   ↓
  Wave 11 — Phase C 整體驗收
   ↓
🟡 Milestone 3：下游 3 skill 完成（user 可量產台詞）
```

## 7.3 user-test 第三次點時機

Milestone 3 達成後可做 M3 user-test：對任一 Phase B 建好的場景跑 /scene-task → /dialogue-write → /qa 完整 chain。

預期 M3 finding：
- /scene-task task pack 涵蓋度（含 C-\* / R-\* / W-rules / V 切片是否齊）
- /dialogue-write 多版本生成（試寫 / 破格 / 收斂三模式）UX
- /qa 8 份 QA pipeline（依 D-043 順序）執行順暢度
- 對話量產實際工時 / 場景

## 7.4 Phase A.0F 前端工具未處理（封版前必補）

封版條件之一。可在第 11 輪 master 對話處理（與 Phase D 平行），或更早任一輪 master 平行啟動。

## 7.5 Phase D / Phase E 路徑（第九輪 + 之後）

- **第 9-10 輪 master：** Phase D（視圖 + 迭代 + 匯出 + 整合）→ Milestone 4 封版
- **第 11+ 輪 master（optional）：** Phase E（翻譯工具分支 fork；NEW_REQ_11）

詳見第七輪 master 對話內展開的全 lifecycle 地圖。

---

**祝第八輪 master 整合順利。Milestone 2 → Milestone 3 過渡的關鍵是把下游 3 個 /scene-task + /dialogue-write + /qa skill 全部上線；前面 Phase A + B 已把上游資料庫全部建好。**

# 8. Cross-ref

- `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope 紀錄；本檔接續）
- `_design/PHASE_B_COMPLETION_REPORT.md` v1.1（Phase B 完成事實檔）
- `_design/DECISIONS_LOG.md` v1.9 §6.13 D-051 + §6.15 D-052 + §6.16 D-053（第七輪 master inline patch 拍板紀錄）
- `_design/POST_LOCK_PENDING.md` v0.9（NEW_REQ 11~14）
- `_design/TASKS.md` v1.9（含 D-052 + D-050/D-053 partial supersede）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND7.md` v0.1（殘留 finding 清單 — 8th master cleanup 起點）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT.md` v0.1（Round 1）
- `_design/CODEX_7TH_MASTER_FINAL_REVIEW_REPORT_ROUND2.md` v0.1 ~ Round6 v0.1（重審歷史）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2（下游 00_k 為 Phase C 權威）
- `00_protocol/00_k_台詞生產流程協議.md`（下游 protocol；Phase C 對應）
- 9 份 QA 模板 `09_quality_assurance/09_a~09_i`（Phase C /qa 對應）
