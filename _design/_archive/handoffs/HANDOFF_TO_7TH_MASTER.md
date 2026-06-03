狀態：DRAFT  
版本：v1.1（master 第六輪延伸完成 — Phase A 收尾 + Wave 6 D-047 patch round + Wave 7 starter ready）  
最後更新：2026-05-20  
適用範圍：給「第七輪整合 master」對話的接手包 — Wave 7 CODEX 跑完後的人類 REVIEW gate + Wave 8 啟動  
優先級：最高

> **v1.0 → v1.1 erratum（master 第六輪延伸；2026-05-20）：**
>
> 原 v1.0 寫「Phase A 收尾後的 Phase B Wave 6 啟動」— 第六輪 master 對話延伸後**已跑完 Wave 6 + Wave 7 starter**。第七輪 master 實際接手範圍縮小：
>
> | Wave / Task | 第六輪延伸完成度 | 第七輪 master 接手 |
> |---|---|---|
> | Wave 6 (B.0~B.4) | ✓ DONE（4 protocol D-047 對齊 patch via CODEX + B.4 verify）| — |
> | Wave 7 CODEX (B.5/B.5b/B.6 三 skill 實作) | ✓ DONE（6 個 SKILL.md 落地 via CODEX_WAVE7_SKILLS_STARTER）| — |
> | **B.5.5 角色 REVIEW gate**（人類）| ⏸ 待 user 親跑 | **第七輪 master 接手寫 review checklist** |
> | **B.6.5 主線 REVIEW gate**（人類）| ⏸ 待 user 親跑 | **第七輪 master 接手寫 review checklist** |
> | Wave 8 (B.7 + B.8 + B.9) | ⏸ 未啟動 | **第七輪 master scope** |
>
> 第七輪 master 第一步：印 B.5.5 角色 REVIEW gate checklist 給 user 親跑（同 A.10 模式）。

# HANDOFF_TO_7TH_MASTER — 第七輪整合 master 對話接手包

# 0. 文件目的

Master 第六輪整合對話完成 — **Milestone 1 → Milestone 2 過渡達成（Phase A 全 PASS）**。

第七輪 master 對話接手 Phase B（Wave 6 + Wave 7） — 5 個 /create-* protocol writing + skill 實作。

**第七輪預期工作（Phase B Wave 6 + Wave 7）：**
1. 接收第六輪 handoff + 接受 master 第六輪所有拍板（D-001 ~ D-049 + §6.11.7 baseline 校正裁決）
2. 推 Wave 6：B.0~B.4 protocol writing（00_l 關係 / 00_f 角色 / 00_g 大綱 / 00_h 細綱 + 03_characters/ 子目錄結構）— 4 條可平行
3. 推 Wave 7：B.5/B.5b/B.6 implementation skill（含 B.5.5 / B.6.5 人類 REVIEW gate）
4. （Wave 8）：B.7 /create-detailed-outline + B.8 Phase B REVIEW gate + B.9 整體驗收
5. Phase B 收尾後升 Milestone 2（**全上游 skills 完成 → user-test 第二次點**）

**預估第七輪總工時：** 6-10 小時 master 對話工時 + 5-7 條 CODEX 對話（Wave 6 4 條平行 + Wave 7 3 條 + 可選 review checkpoints）

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。第六輪 master 對話完成 Phase A 收尾（含 M1 user-test 處理 / D-048 NEW_REQ_7 / D-049 NEW_REQ_8 Template-detect / Wave 4 A.7+A.8+A.12 / Wave 5 A.9+A.10+A.11 全 PASS），Milestone 1 → Milestone 2 過渡達成（2026-05-20）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第七輪整合 master」對話。

**第一步必讀（按順序，精簡 — 7 份）：**
1. _design/HANDOFF_TO_7TH_MASTER.md（本檔，你的 scope）
2. _design/PHASE_A_COMPLETION_REPORT.md v1.1（Phase A 完成事實檔；含 §6 end-to-end placeholder — user 後續親跑補）
3. _design/DECISIONS_LOG.md §6.11 v1.4（master 第六輪 Critical patch + A.11 baseline 校正裁決）
4. _design/TASKS.md v1.7（B Phase B.0~B.9 任務拆解）
5. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5（5 個 /create-* skill 上游規範權威 — §1.1~§1.5）
6. _design/REQUIREMENTS_LOCK.md v1.0 FINAL（north star 不動）
7. _design/POST_LOCK_PENDING.md v0.4（NEW_REQ_2 持續寫作 / NEW_REQ_9 DEFERRED）

**第二步精選讀（碰到才看）：**
8. _design/ARCHITECTURE.md v1.5（§3.3 skill 內容規範 / §3.3.0 multi-agent / §3.3.2 Template-detect）
9. _design/SPEC.md v1.2（§5.1 entity / §5.3 完成度 / §17 7 anchor）
10. _design/INTEGRATION_CONTRACTS.md v2.1（§4a Contract D D-047 issue_type_registry）
11. _design/DATA_FORMAT_SPEC.md v0.4（§3.2 phase_log / §3.3 base_dialogue / §7.2 entity_type_registry / §8 qa_type_registry）
12. _design/wrapper_smoke_test_report.md（A.9 △ PARTIAL — 後續 host 補測）
13. _design/phase_a_review_log.md（A.10 4 模板 REVIEW 升級紀錄）

**你的 scope（master 第七輪整合）：**
1. **接收第六輪 handoff** + 接受 D-001~D-049 + §6.11.7 baseline 校正裁決
2. **推 Wave 6：B.0~B.4 protocol writing（4 條可平行）**
   - B.0 寫 00_l 關係創建協議
   - B.1 寫 00_f 角色創建協議
   - B.2 寫 00_g 大綱創建協議
   - B.3 寫 00_h 細綱創建協議
   - B.4 確認 03_characters/ 子目錄結構
3. **Wave 6 完成後推 Wave 7：B.5 + B.5b + B.6 skill 實作（含 B.5.5 / B.6.5 人類 REVIEW gate）**
4. **Wave 8：B.7 + B.8 Phase B REVIEW gate + B.9 整體驗收**
5. **Phase B 收尾後升 Milestone 2**（全上游 skills 完成 — user-test 第二次點）
6. （optional）若 user 有新 finding → 緊急 patch round（同 D-049 模式）

**禁止越界：**
- 不重做設計（已 LOCKED v1.0 ~ v1.5）
- 不改 D-001 ~ D-049 拍板結論（要動需 user 拍板新 D-050+）
- 不擅啟 Phase C 實作（屬下一階段 user 操作）
- 不重審 CODEX (c) / (d) / (d2) / (e) / (e2) / Wave 2 review / Wave 4 master sanity / A.10 / A.11 已 RESOLVED 議題
- B.5.5 / B.6.5 / B.8 三個人類 REVIEW gate 必須 user 親跑拍板

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

**[第六輪 user-test finding 全 RESOLVED — 第七輪無 finding 段]**

請先回報你讀完 7 份必讀後對 scope + Wave 6 + Wave 7 工作順序的理解，再開始處理。
```

---

# 2. 當前狀態快照（master 第六輪結束時）

## 2.1 設計層狀態（spec 版本）

| 檔 | 版本 | 狀態 | 備註 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | north star，不動 |
| `_design/DECISIONS_LOG.md` | v1.4 | **FINAL** | D-001 ~ D-049 + §6.11.7 baseline 校正裁決 |
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | **LOCKED** | Contract A/B/C/D（D-047 issue_type_registry）|
| `_design/SPEC.md` | v1.2 | **LOCKED** | D-047 supersede |
| `_design/ARCHITECTURE.md` | v1.5 | **LOCKED** | §3.3.0 multi-agent + §3.3.2 Template-detect |
| `_design/TASKS.md` | v1.7 | **LOCKED** | A.5b + A.11 Wave 4 consolidation + A.12 |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | **LOCKED** | Phase B 5 /create-* skill 上游權威 |
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 不動 |
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 不動 |
| `_design/PHASE_3_COMPLETION_REPORT.md` | v4.0 FINAL | **LOCKED** | Phase 3 完成；不動 |
| `_design/PHASE_A_COMPLETION_REPORT.md` | v1.1 | **DRAFT** | Phase A 完成（master inline patch baseline 校正後 PASS）|
| `_design/POST_LOCK_PENDING.md` | v0.4 | DRAFT | NEW_REQ_1/3/4/5/6/7/8 RESOLVED；NEW_REQ_2 持續寫作；NEW_REQ_9 DEFERRED |
| `_design/registries/*.template.yaml` | 3 個 LOCKED | **LOCKED** | entity / qa / issue (D-047) |
| `scripts/parse_frontmatter.py` | A.0.10 patched | DONE | 3 critical fix |
| `_design/phase_a_review_log.md` | v0.1 | DRAFT | A.10 升級紀錄 |
| `_design/wrapper_smoke_test_report.md` | v0.1 | DRAFT | A.9 PARTIAL Codex App PASS |
| `.template_root` marker | v1.0 | 新建 | D-049 Template-detect 第一道防線 |
| `AGENTS.md` | （root，無 header）| 擴充 | D-048 Codex skill 清單 |
| `CLAUDE.md` | v0.1 | DRAFT | D-048 Anthropic 慣例 |
| `_user_manual/skill_invocation_guide.md` | v0.1 | DRAFT | D-048 Cowork / Codex App fallback |

## 2.2 Wave 1~5 全部完成

**Wave 1 (Phase A 後段 + A.0F alpha 第一波)：** A.1 ✓ + A.4 ✓ + A.0F.0 ✓  
**Wave 2 (Phase A 後段 + A.0F alpha 第二波)：** A.2 ✓ + A.3 ✓ + A.0F.1 ✓（Round 2 review NEAR-GO + 殘留修補後 GO）  
**Wave 3 (Milestone 1 達成)：** A.5 ✓ + A.6 ✓ + A.0F.2 ✓  
**Wave 4 (M1 user-test 處理後)：** A.7 ✓ + A.8 ✓ + A.12 ✓（M1-D-01 master inline + D-048 NEW_REQ_7 + D-049 NEW_REQ_8）  
**Wave 5 (Phase A 收尾)：** A.9 ✓ △ PARTIAL + A.10 ✓ + A.11 ✓ PASS（master inline patch v1.1 baseline 校正後）  

**Milestone 1 達成（DECISIONS_LOG §6.9.10）+ Milestone 2 啟動條件達成（Phase A 完成）。**

## 2.3 Phase B 任務拆解（依 TASKS v1.7）

| Task | 內容 | 依賴 | Wave |
|---|---|---|---|
| **B.0** | 寫 `00_protocol/00_l_關係創建協議.md`（C-7 新增）| 無 | Wave 6 |
| **B.1** | 寫 `00_protocol/00_f_角色創建協議.md` | 無 | Wave 6 |
| **B.2** | 寫 `00_protocol/00_g_大綱創建協議.md` | 無 | Wave 6 |
| **B.3** | 寫 `00_protocol/00_h_細綱創建協議.md` | 無 | Wave 6 |
| **B.4** | 確認 `03_characters/` 子目錄結構存在 | 無 | Wave 6（可放 Wave 6 末或獨立）|
| **B.5** | 實作 /create-character skill（含中文別名 /建立角色）| B.0 + B.1 | Wave 7 |
| **B.5.5** | 角色 REVIEW Gate（人類；M3 在 B.5b 之前）| B.5 | Wave 7（**人類 REVIEW gate**）|
| **B.5b** | 實作 /create-relationship skill（含中文 /建立關係）| B.0 + B.5.5 | Wave 7 |
| **B.6** | 實作 /create-outline skill（含中文 /建立大綱）| B.2 | Wave 7 |
| **B.6.5** | 主線 REVIEW Gate（人類；M3 在 B.7 之前）| B.6 | Wave 7（**人類 REVIEW gate**）|
| **B.7** | 實作 /create-detailed-outline skill（含中文 /建立細綱）| B.3 + B.6.5 | Wave 8 |
| **B.8** | Phase B REVIEW Gate（人類 + agent）| B.5 ~ B.7 | Wave 8（**人類 REVIEW gate**）|
| **B.9** | Phase B 整體驗收 | B.0 ~ B.8 | Wave 8 |

**建議 Wave 拆分：**
- Wave 6 = B.0 + B.1 + B.2 + B.3 + B.4（4 條 protocol writing + 1 條目錄檢查，B.0~B.3 4 條可平行）
- Wave 7 = B.5 + B.5.5 + B.5b + B.6 + B.6.5（含 2 個人類 REVIEW gate）
- Wave 8 = B.7 + B.8 + B.9（含 1 個人類 REVIEW gate + 整體驗收）

---

# 3. 第七輪工作清單（按執行順序）

## 階段 1：讀完 7 份必讀 + 接受第六輪 handoff（30-60 分）

按順序讀 7 份必讀 + 確認對 scope / Wave 6 / Wave 7 工作順序的理解。

## 階段 2：Wave 6 啟動 — B.0/B.1/B.2/B.3 並行 + B.4

四條 protocol writing starter 寫法同 Wave 4 模式（依 ARCH §3.3 + UD §1.1~§1.5 規範）：

- B.0 / B.1 / B.2 / B.3 寫各自的 00_l / 00_f / 00_g / 00_h 協議 .md 檔
- 每條 starter 引用 UD §1.x（對應上游 skill 規範）+ DECISIONS_LOG §6.9.2 D-047（issue_type_registry 動態載入規範）
- 4 條可平行（4 個獨立 protocol 檔，不重疊）
- B.4 是輕量 task — 確認 03_characters/main 03_characters/minor 03_characters/npc 子目錄存在（Template 應已 init）

## 階段 3：Wave 6 review checkpoint（建議跑）

依本輪 Wave 4 review consolidation 教訓：寫 Wave 6 review starter 同 Wave 2 模式跑 review 檢查。Wave 6 4 個 protocol 檔上線後驗：
- 5 欄中文 header + YAML block（如需）
- 5 階段流程對齊 UD §1.x 權威
- 議題清單對齊 issue_type_registry.template.yaml v0.1 範本

## 階段 4：Wave 7 啟動 — B.5/B.5b/B.6 skill 實作 + B.5.5/B.6.5 REVIEW gate

- B.5 /create-character skill 實作（CODEX 對話）
- B.5.5 角色 REVIEW gate（**人類**；user 親跑 + 寫 phase_b_character_review_log.md）
- B.5b /create-relationship skill 實作（CODEX 對話）
- B.6 /create-outline skill 實作（CODEX 對話）
- B.6.5 主線 REVIEW gate（**人類**；user 親跑）

## 階段 5：Wave 8 — B.7 + B.8 + B.9 收尾

- B.7 /create-detailed-outline skill 實作
- B.8 Phase B REVIEW gate（**人類**；同 A.10 模式）
- B.9 Phase B 整體驗收 + 升 PHASE_B_COMPLETION_REPORT.md

## 階段 6：升 Milestone 2 + 寫 8th master handoff

Phase B PASS → Milestone 2「全上游 skills 完成」達成 → user 可進 user-test 第二次點 → 寫 HANDOFF_TO_8TH_MASTER.md 接 Phase C（/scene-task / /dialogue-write / /qa）

---

# 4. 風險警示

## 4.1 baseline 設門檻紀律（master 第六輪教訓）

寫 baseline gate 時必須用 user 環境跑 baseline，不能只用 master sandbox 跑（因 Windows vs Linux filesystem case-sensitivity 差異）。詳 DECISIONS_LOG §6.11.7 / POST_LOCK_PENDING NEW_REQ_9。

## 4.2 protocol 寫作對齊 D-047 issue_type_registry

B.0 ~ B.3 寫 protocol 時必須引用 `_design/registries/issue_type_registry.template.yaml` v0.1 之議題清單；不可 hardcode 議題清單到 protocol 內（屬 D-047 拍板規範）。

## 4.3 人類 REVIEW gate 不可跳

B.5.5 / B.6.5 / B.8 三個人類 REVIEW gate 必須 user 親跑 + 寫對應 review log。Master 不得代勞跳過。

## 4.4 sandbox virtiofs cache stale 已知問題（HANDOFF §5.4 既有警示）

工作目錄 Windows 端是權威。Sandbox 端 git status / wc -l / ls mtime 偶爾顯示 stale。所有 git commit + push 由 user 手動執行，不靠 sandbox bash。Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 4.5 file-already-exists pattern（CODEX BLOCKED 警示）

CODEX A.2 / A.3 中過 file-already-exists BLOCKED。Master 寫 starter 前必須 grep `git ls-files` 確認新建檔路徑不存在（針對 B.0~B.3 寫 00_l / 00_f / 00_g / 00_h；前面 00_e / 00_i 已存在）。

## 4.6 第六輪 PARTIAL 項目持續處理

- `_design/wrapper_smoke_test_report.md` △ PARTIAL：後續 user 在 Claude Code CLI / Codex CLI / Cowork 各 host 補跑後追加 entry（不阻 Phase B）
- `_design/PHASE_A_COMPLETION_REPORT.md` §6 end-to-end placeholder：等 user 親跑 8 step 端到端後補入（不阻 Phase B 啟動，但建議在進 B.5 前跑一次以驗 init-project + create-world 5 階段在 fresh Instance work）

---

# 5. 完成條件

第七輪整合對話完成 = 以下全部 ✓：

```
✓ Wave 6 全 DONE（B.0 ~ B.4 + 可選 review checkpoint）
✓ Wave 7 全 DONE（B.5 + B.5.5 + B.5b + B.6 + B.6.5 含 2 個人類 REVIEW gate）
✓ Wave 8 全 DONE（B.7 + B.8 + B.9 含 1 個人類 REVIEW gate + 整體驗收）
✓ PHASE_B_COMPLETION_REPORT.md v1.0 升 PASS
✓ 5 個 /create-* skill 全可跑（init-project + create-world + create-character + create-relationship + create-outline + create-detailed-outline + 對應 6 個中文 wrapper）
✓ user 通知可以進 Phase C Wave 9（C.1 /scene-task + C.2 /dialogue-write + C.3 /qa）
```

---

# 6. 文件維護紀律

- 本檔是「接手指南」，第七輪 master 對話讀完後**不需要更新本檔**
- 若第七輪發現本檔不準確 → 標 errata 在第八輪接手包（如有）
- 第七輪完成後可把本檔 archive 進 `_design/archive/`

---

# 7. 對 user 的最終建議（master 第六輪結束時）

## 7.1 立即可做的事

1. **commit + push 本輪所有變更**（用之前 master 提供的 GIT SUMMARY 命令）
2. **可選：** 跑一次 end-to-end test 補 PHASE_A_COMPLETION_REPORT §6（在新目錄 clone Template → 刪 .template_root → 跑 /init-project → /create-world → /status → /check-gaps）
3. **可選：** 在其他 agent 環境（Claude Code CLI / Codex CLI / Cowork）跑 wrapper smoke test 補 wrapper_smoke_test_report.md

## 7.2 進 Phase B 的條件達成

- ✓ Phase A 五 skill 全可跑（4 主 + 4 wrapper）
- ✓ 27 模板 frontmatter 對齊
- ✓ 4 模板檔 W/V 升 REVIEW（A.10 已落地）
- ✓ A.11 PASS（v1.1 master inline patch 校正後）

達成後 user 可進入：

```
Phase B（B.0 ~ B.9）
  B.0 寫 00_l 關係創建 protocol  ┐
  B.1 寫 00_f 角色創建 protocol  │ Wave 6 並行
  B.2 寫 00_g 大綱創建 protocol  │
  B.3 寫 00_h 細綱創建 protocol  ┘
  B.4 確認 03_characters/ 子目錄
   ↓
  B.5 實作 /create-character skill ┐
  B.5.5 Character REVIEW gate（人類）│ Wave 7
  B.5b 實作 /create-relationship   │
  B.6 實作 /create-outline         │
  B.6.5 Outline REVIEW gate（人類） ┘
   ↓
  B.7 實作 /create-detailed-outline ┐
  B.8 Phase B REVIEW gate（人類）   │ Wave 8
  B.9 Phase B 整體驗收             ┘
   ↓
🟡 Milestone 2：全上游 skills 完成（user-test 第二次點）
```

## 7.3 user-test 第二次點時機

Milestone 2 達成後可做 M2 user-test：跑完整 5 個 /create-* skill 路徑 + 對齊 issue_type_registry 客製化議題 + 驗整體上游節奏。

預期 M2 finding：
- skill UX 細節（user 5 階段對話節奏感）
- registry 客製化機制（user 加自訂議題 vs 跳 core 議題）
- C/R/P/CH 實體 frontmatter 對齊度
- 跨 skill chain（W → V → C → R → P → CH）資料流順暢度

---

**祝第七輪 master 整合順利。Milestone 1 → Milestone 2 過渡的關鍵是把上游 5 個 /create-* skill 全部上線；前面 Phase A 已把基礎設施全鋪好。**
