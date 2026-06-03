狀態：DRAFT  
版本：v1.0（M1 達成後 — Wave 1/2/3 全 DONE + user-test 待整合）  
最後更新：2026-05-19  
適用範圍：給「第六輪整合 master」對話的接手包 — Milestone 1 達成後的 master 第六輪整合工作  
優先級：最高

# HANDOFF_TO_6TH_MASTER — 第六輪整合 master 對話接手包

# 0. 文件目的

Master 第五輪整合 + Wave 1 + Wave 2（含 NO-GO recovery + Round 2 review）+ Wave 3 全部完成。**Milestone 1：第一個能跑版本** 達成（2026-05-19）。

User 在第五輪對話末做了第一次 M1 user-test。本檔給「**第六輪整合 master 對話**」啟動時用。

**第六輪預期工作：**
1. 接收 M1 user-test 發現的 finding（user 在啟動 prompt 內貼）
2. 判斷 finding 範圍：小→ inline patch / 大→ 拆 NEW_REQ → Wave 4 處理
3. 推 Wave 4：A.7 `/status` + A.8 `/check-gaps` 兩 skill 實作
4. 推 Wave 5：A.9 wrapper smoke test + A.10 Phase A REVIEW Gate + A.11 Phase A 整體驗收（含 user 人類 REVIEW）
5. Phase A 收尾後，準備 Phase B 啟動條件

**預估第六輪總工時：** 4-6 小時 master 對話工時（依 user-test finding 數量決定）+ 3-5 條 CODEX 對話。

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。第五輪 master 對話完成設計層整合（D-047 + NEW_REQ_3/4/5/6）+ Stage 0 A.0.10 parser patch + Wave 1 (A.1/A.4/A.0F.0) + Wave 2 (A.2/A.3/A.0F.1 含 NO-GO 修補 + Round 2 review) + Wave 3 (A.5/A.6/A.0F.2)，**Milestone 1 已達成**（2026-05-19）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git

你是「第六輪整合 master」對話。

**第一步必讀（按順序，精簡 — 7 份）：**
1. _design/HANDOFF_TO_6TH_MASTER.md（本檔，你的 scope）
2. _design/CODEX_WAVE2_REVIEW_REPORT_ROUND2.md（Wave 2 review Round 2 NEAR-GO + 殘留 finding 修補後現況）
3. _design/CODEX_A0F1_PATCH_REPORT.md（A.0F.1 patch round PASS 報告，如存在）
4. _design/DECISIONS_LOG.md §6.9（v1.1 — D-047 + NEW_REQ_3/4/5/6 + Stage 0 紀錄）
5. _design/TASKS.md v1.4（看 A.7 ~ A.11 任務待辦 + Phase B 啟動條件）
6. _design/ARCHITECTURE.md v1.3 §3.3（skill 內容規範 — A.7/A.8 / A.9 wrapper smoke test 對應）
7. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL — north star 不動）

**第二步精選讀（碰到才看，不必整讀）：**
8. _design/SPEC.md v1.2（含 §17 7 anchor）
9. _design/INTEGRATION_CONTRACTS.md v2.1（§4a Contract D D-047）
10. _design/UPSTREAM_DOWNSTREAM_SPEC.md v0.5（§1.1 ~ §1.5 議題清單；尤其 A.6 跑完後可能要回看 §1.1）
11. _design/UX_SPEC.md v0.4（前端 §11 全段；A.0F real-data acceptance 才會碰）

**你的 scope（master 第六輪整合）：**

1. **接收 M1 user-test finding（必做第一步）：** user 在本啟動 prompt 末會貼 user-test 跑完 6 phase 的結果摘要（Phase 0-6）。你必須先讀完才開始任何工作
2. 依 finding 嚴重度分流：
   - **Minor**（typo / wording / 單檔小邏輯）→ master inline patch
   - **Major**（spec 對齊問題 / D-NNN 規模新議題）→ 拍 D-048 / 加 POST_LOCK_PENDING NEW_REQ_7+
   - **Critical**（M1 路徑 broken / skill 無法跑）→ 緊急 patch + 短審查
3. 推 Wave 4：A.7 `/status` skill 實作 + A.8 `/check-gaps` skill 實作（可平行）
4. （Wave 4 完成後）推 Wave 5：A.9 wrapper smoke test + A.10 + A.11
5. Phase A 收尾後升 LOCKED + 拍板 Phase B 啟動條件
6. **若有重大 spec 對齊問題：** 升 7 spec 主 partial supersede（IC v2.2 / SPEC v1.3 / ARCH v1.4 / TASKS v1.5 / DECISIONS_LOG v1.2 / DF v0.5 / UD v0.6）

**禁止越界：**
- 不重做設計（已 LOCKED v1.0）
- 不改 D-001 ~ D-047 拍板結論（要動需 user 拍板新 D-048+）
- 不擅啟 Phase B 實作（屬下一階段 user 操作）
- 不重審 CODEX (c) / (d) / (d2) / (e) / (e2) / Wave 2 review Round 1/2 已 RESOLVED 議題
- 不擅自跨 Wave 4 → Wave 5（人類 REVIEW gate 必須 user 拍板）

**整合過程若發現新衝突，立刻停手回升 user 拍板。**

**[USER-TEST FINDING 段]** 我（user）跑 M1 user-test 結果如下：

[user 在此貼 Phase 0-6 跑完的問題清單；如無問題則寫「全部 Phase pass，無 finding」]

請先回報你讀完 7 份必讀 + 我的 user-test finding 後對 scope + Wave 4 + Wave 5 工作順序的理解，再開始處理。
```

---

# 2. 當前狀態快照

## 2.1 設計層狀態（spec 版本）

| 檔 | 版本 | 狀態 | 備註 |
|---|---|---|---|
| `_design/REQUIREMENTS_LOCK.md` | v1.0 | **FINAL** | north star，不動 |
| `_design/DECISIONS_LOG.md` | v1.1 | **FINAL** | D-001 ~ D-047 + §6.9 master 第五輪紀錄 |
| `_design/INTEGRATION_CONTRACTS.md` | v2.1 | **LOCKED** | Contract A/B/C + 新 §4a Contract D（D-047 issue_type_registry）|
| `_design/SPEC.md` | v1.2 | **LOCKED** | partial supersede via D-047 |
| `_design/ARCHITECTURE.md` | v1.3 | **LOCKED** | §12.6 issue_registry parser + §12.A.0.10 Stage 0 紀錄 |
| `_design/TASKS.md` | v1.4 | **LOCKED** | A.0.10 task + B Phase /create-* 對齊 + A.0F 兩段制 |
| `_design/DATA_FORMAT_SPEC.md` | v0.4 | **LOCKED** | §7.2/§8.2/§8.3/§9.1 cleanup + algorithm/report_template 補入 §8.3 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | v0.5 | **LOCKED** | §3.10 全部對齊 user_extensions: 段 |
| `_design/UX_SPEC.md` | v0.4 | **LOCKED** | 不動（master 第五輪不涉）|
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | v0.2 | **LOCKED** | 不動 |
| `_design/PHASE_3_COMPLETION_REPORT.md` | v4.0 FINAL | **LOCKED** | 不動 |
| `_design/POST_LOCK_PENDING.md` | v0.1 DRAFT | DRAFT | NEW_REQ_1/3/4/5/6 全 RESOLVED；NEW_REQ_2 持續寫作 |
| `_design/registries/issue_type_registry.template.yaml` | v0.1 | **LOCKED** | 5 skill × 36 user-facing 議題 |
| `scripts/parse_frontmatter.py` | — | A.0.10 patched | 3 critical fix done |

## 2.2 Wave 1 + 2 + 3 任務完成狀態

**Wave 1（Phase A 後段 + A.0F alpha 第一波）：**

| Task | 狀態 | 產出 |
|---|---|---|
| A.1 寫 00_b 通用骨架 | ✅ DONE | `00_protocol/00_b_反ai味檢查表.md`（含 SPEC §17.1 7 anchor）|
| A.4 補 27 模板 frontmatter | ✅ DONE | 25 檔 frontmatter 補入（09_f 既有不動）|
| A.0F.0 前端 scaffold | ✅ DONE | `_tools/frontend/` 17 檔（server.py + 8 endpoint placeholder + static skeleton）|

**Wave 2（Phase A 後段 + A.0F alpha 第二波）：**

| Task | 狀態 | 產出 / 修補 |
|---|---|---|
| A.2 00_i Bootstrap protocol | ✅ DONE | master 直接 patch（補 6 處：§6 階段 4 + §10.5 / §10.6 / §10.7）|
| A.3 00_e 世界觀協議 | ✅ DONE | master 直接 patch（補 §2 §4.0 D-047 機制 + 議題清單表 + §10 UD line ref 對照 + 附錄 A/B）|
| A.0F.1 8 endpoint adapter | ✅ DONE | CODEX 跑（含 NO-GO patch round：LOCKED guard + DRAFT proposal contract + conflict body shape）|

Wave 2 review：Round 1 NO-GO → 修補 → Round 2 NEAR-GO → 2 處 wording 修補後達 GO。

**Wave 3（Milestone 1 達成）：**

| Task | 狀態 | 產出 |
|---|---|---|
| A.5 /init-project skill | ✅ DONE | 2 個 SKILL.md（init-project + 初始化專案 wrapper）|
| A.6 /create-world skill | ✅ DONE | 2 個 SKILL.md（create-world + 建立世界觀 wrapper；D-047 動態議題清單機制落地）|
| A.0F.2 F1 Dashboard | ✅ DONE | 9 個檔（7 改 + 2 新；7 段 layout + 真 API 整合）|

**🟡 Milestone 1 達成條件全達標**（DECISIONS_LOG §6.9.10）：
- ✅ Gate 1 NO-GO 修補（Stage 0 PASS）
- ✅ D-047 + NEW_REQ_3/4/5/6 RESOLVED
- ✅ Wave 1 + 2 + 3 全部完成
- ✅ Wave 2 Round 2 review GO（NEAR-GO 修補後）
- ✅ user 可實際試用世界觀建立

## 2.3 Phase A 後段剩餘任務（Wave 4 + Wave 5）

依 TASKS v1.4：

| Task | 內容 | 依賴 | 規模 |
|---|---|---|---|
| **A.7** `/status` skill 實作 | 依 ARCH §2.3 / SPEC §5.3 + §5.4 phase_log + A.0 parser API | A.0 ✓ + A.4 ✓ + A.5 ✓ | 中-重 |
| **A.8** `/check-gaps` skill 實作 | 缺漏 entity 偵測 + 對應 skill 建議 | A.7 | 中 |
| **A.9** wrapper smoke test | 跑 A.5/A.6/A.7/A.8 五階段 + 中文 wrapper trigger | A.5 ✓ + A.6 ✓ + A.7 + A.8 | 中 |
| **A.10** Phase A REVIEW Gate | 人類 REVIEW gate — user 拍板 Phase A 是否完整 | A.0 ~ A.9 | 小（user 行為）|
| **A.11** Phase A 整體驗收 | 依 PHASE_3 §6.2 五項解除條件再驗一輪 | A.0 ~ A.10 | 小 |

Wave 4 = A.7 + A.8（可平行）  
Wave 5 = A.9 + A.10 + A.11（依序：A.9 → A.10 → A.11；A.10/A.11 含人類 REVIEW gate）

**Phase A 收尾後 = Phase B 啟動條件達成。**

---

# 3. 第六輪工作清單（按執行順序）

## 階段 1：讀完 7 份必讀 + 接收 user-test finding（30-60 分）

跟第五輪一樣的開場 — 但**加 user-test finding 處理**：

- User 在啟動 prompt 末會貼 M1 user-test 跑完 6 phase 的結果摘要
- master 必須先讀完 finding 才能規劃 Wave 4
- 依 finding 嚴重度分流：

| 嚴重度 | 行為 |
|---|---|
| **Minor**（typo / wording / 單檔 patch）| master inline patch |
| **Major**（spec 對齊問題 / skill 邏輯 gap）| 拍 D-048 / 加 POST_LOCK_PENDING NEW_REQ_7+ / patch round |
| **Critical**（M1 路徑 broken）| 緊急 patch + 短審查（同 A.0F.1 NO-GO patch 模式）|

## 階段 2：finding patch（如有，視 finding 數量定）

按嚴重度個別處理。Critical 必修；Major 可決定本輪或下輪；Minor 順帶。

## 階段 3：Wave 4 啟動 — A.7 + A.8 平行

A.7 / A.8 兩條 starter 寫法同 Wave 1/2/3 模式：

- A.7 `/status` skill：依 ARCH §2.3 + SPEC §5.3 完成度公式 + parser API（`build_repo_index` → `get_*` accessor）；含中文 wrapper `/進度`
- A.8 `/check-gaps` skill：依 SPEC §10 缺漏偵測 + expected_entities.yaml；含中文 wrapper `/檢查缺漏`

A.7 / A.8 互不依賴（A.8 概念上用 A.7 邏輯但實作上獨立）— 可三條 CODEX 平行或先後跑。

## 階段 4：Wave 4 review（可選但建議）

依 Wave 2 review 經驗，Wave 4 完成後跑一輪 review checkpoint 比較穩。CODEX_WAVE4_REVIEW_STARTER 同 Wave 2 模式。

## 階段 5：Wave 5 啟動 — A.9 wrapper smoke test

A.9 task：CODEX 跑 5 個 skill（init-project / create-world / status / check-gaps + 對應中文 wrapper）測啟動 trigger 正常。屬功能性整合 test。

## 階段 6：A.10 Phase A REVIEW Gate（**人類 REVIEW gate**）

User 拍板 Phase A 是否完整：
- Phase A 五 skill（init-project / create-world / status / check-gaps + 中文 wrapper）全可跑
- 27 模板 frontmatter 全對齊
- 00_b 通用骨架 + 00_e/00_i protocol 全寫好
- 前端 A.0F alpha 6 task 全完成（A.0F.0/1/2 + 剩下 A.0F.3/4/5 可選；本輪不要求）
- 跑通典型 use case（建專案 → /create-world → /status 看完成度 → 前端看 Dashboard）

⚠ master **不**自動跑 A.10；必須 user 親自跑「典型 use case」+ 在 chat 內明示拍板（同 D.2.5 / D.3.5 / B.5.5 / B.6.5 模式）。

## 階段 7：A.11 Phase A 整體驗收 + 升 LOCKED

依 PHASE_3 §6.2 五項解除條件再驗一輪：
- 所有 LOCKED 文件無 ERROR
- check_headers + build_repo_index 0 ERROR baseline 維持
- expected_entities.yaml 對齊
- POST_LOCK_PENDING 不殘留 critical NEW_REQ
- master 升 PHASE_A_COMPLETION_REPORT.md（同 PHASE_3 完成報告模式）

A.11 PASS → **Phase A 收尾**。

## 階段 8：拍板 Phase B 啟動條件 + 通知 user

Phase B = 5 個 /create-* skill 全做完。Phase A 完成後 user 可啟動 B Phase。

Master 第六輪本輪可：
- 把 Phase B 任務 mapping 寫進 next handoff doc
- 整理 Phase B 5 個 /create-* skill 對應 protocol 狀態（哪個 done、哪個還沒）
- 列 Phase B 第一波建議 task 順序（Wave 6 = B.0~B.4 protocol writing；Wave 7 = B.5/B.6 first skill；等等）

---

# 4. 對 user 的最終建議（master 第六輪完成後）

**Phase B 啟動條件：**
- ✓ Phase A 五 skill 全可跑（init / create-world / status / check-gaps + 中文 wrapper）
- ✓ 27 模板 frontmatter 對齊
- ✓ Phase A 五項解除條件 PASS
- ✓ A.11 Phase A 整體驗收 GO

達成後 user 可進入：

```
Phase B（B.0 ~ B.9）
  B.0 寫 00_l 關係創建 protocol
  B.1 寫 00_f 角色創建 protocol
  B.2 寫 00_g 大綱創建 protocol
  B.3 寫 00_h 細綱創建 protocol
  B.4 建 03_characters 子目錄結構
  B.5 實作 /create-character skill
  B.5.5 Character REVIEW gate（人類）
  B.5b 實作 /create-relationship skill
  B.6 實作 /create-outline skill
  B.6.5 Outline REVIEW gate（人類）
  B.7 實作 /create-detailed-outline skill
  B.8 Phase B REVIEW gate（人類）
  B.9 Phase B 整體驗收
   ↓
🟡 Milestone 2：全上游 skills 完成（user-test 第二次點）
```

---

# 5. 風險警示

## 5.1 user-test 可能引出新議題

第一次跑 user-test 必然會發現問題 — 預期：
- skill 對話腳本可能太冗 / 太精
- 某些議題 user 沒實感 / 答不出
- agent 寫檔結果跟 user 預期有落差
- Dashboard 某些段沒邏輯 / 無實質資料

第六輪 master 對話需要**有彈性**接這些 finding。

## 5.2 A.10 / A.11 是人類 REVIEW gate

不要 master 跳過。違反 SPEC §16 文件狀態升級限制 + Phase A 整體驗收紀律。

## 5.3 partial supersede 紀律

第六輪如需動 LOCKED spec（如 D-048 + new NEW_REQ）：
- 走 v1.x → v1.y partial supersede 模式
- 保留原段內容 + 加 v1.y 標註說明擴充範圍
- 跟 master 第五輪同模式

## 5.4 sandbox virtiofs cache stale 已知問題

工作目錄 Windows 端是權威。Sandbox 端 git status / wc -l 偶爾顯示 stale（A.3 復原事件已驗）。**所有 git commit + push 由 user 手動執行**，不靠 sandbox bash。

Master 對話讀檔以 Read tool（Windows 端權威）為準，bash grep / wc 結果若衝突要用 Read 驗。

## 5.5 file-already-exists pattern（CODEX BLOCKED）

A.2 / A.3 兩條都中過：CODEX starter 寫「新建檔」但檔已 tracked 在 git。CODEX 正確 BLOCK。Master 應提前 grep `git ls-files` 避免重蹈。

A.5 / A.6 / A.0F.2 都通過了（新建檔不存在或修改既有檔範圍清楚）。Wave 4 寫 A.7 / A.8 starter 時要先 check `.claude/skills/status/` / `.claude/skills/check-gaps/` 是否存在。

---

# 6. 完成條件

第六輪整合對話完成 = 以下全部 ✓：

```
✓ M1 user-test finding 全處理（patch / 升 D-NNN / 加 NEW_REQ）
✓ Wave 4：A.7 /status + A.8 /check-gaps 全 DONE
✓ Wave 5：A.9 wrapper smoke test + A.10 Phase A REVIEW Gate + A.11 整體驗收全 DONE
✓ Phase A 五項解除條件再驗 GO
✓ （可選）升新版 spec partial supersede（若有 D-048+ 拍板）
✓ user 通知可以進 Phase B Wave 6（B.0~B.4 protocol writing）
```

---

# 7. 文件維護紀律

- 本檔是「**接手指南**」，第六輪 master 對話讀完後**不需要更新本檔**
- 若第六輪發現本檔不準確 → 標 errata 在第七輪接手包（如有）
- 第六輪完成後可把本檔 archive 進 `_design/archive/`

---

# 8. POST_LOCK_PENDING 對照

| NEW_REQ | 內容 | 第五輪處理 | 第六輪後續 |
|---|---|---|---|
| NEW_REQ_1 議題 registry | ✅ RESOLVED via D-047 | — |
| NEW_REQ_2 使用說明書 | 持續寫作 | M1 user-test 後可補 quick_start 章 / customization 章 D-047 例子 |
| NEW_REQ_3 deleted KEY 內文 | ✅ RESOLVED（WARN）| Phase A.X parser patch round 落地 |
| NEW_REQ_4 DF §7.2 範例 | ✅ RESOLVED | — |
| NEW_REQ_5 target_dir csv | ✅ RESOLVED（選 b）| — |
| NEW_REQ_6 .qa_extension → user_extensions: | ✅ RESOLVED | — |
| NEW_REQ_7+（如 user-test 發現）| — | **第六輪 master 接** |

---

**祝第六輪 master 第一步順利。M1 是個重要里程碑 — 從這裡開始 user-test 反饋會持續影響後續設計。**
