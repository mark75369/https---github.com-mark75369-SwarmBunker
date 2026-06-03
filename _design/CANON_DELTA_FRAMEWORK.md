狀態：DRAFT
版本：v0.1（9th master 第二段對話 Wave 15 framework reference 落地；對齊 UPSTREAM_DOWNSTREAM_SPEC v0.5 §5；不實作 skill；屬「成熟期功能」 future implementation reference）
最後更新：2026-05-22
適用範圍：Canon Delta 回寫機制 framework reference — 給 11+ 輪 master / 工具 B 翻譯工具 fork / 未來「成熟期功能」實作對話 reference
優先級：高

# CANON_DELTA_FRAMEWORK — Canon Delta 回寫機制框架紀錄

# 0. 本檔用途

**本檔是 framework reference，不是 LOCKED spec，不實作 skill。**

當 user 跑量產台詞累積後，09_e 定稿變更紀錄會出現「**定稿台詞揭露之前 Bible 沒寫清楚的設定**」 — 這是 Canon Delta 現象。Canon Delta 是「下游回饋上游」的回饋環機制。

工具 A（game-dialogue-bible）的設計從 Phase A 開始就預留 Canon Delta 機制（依 SPEC §12.8 + UD §5 + REQUIREMENTS_LOCK §4.4），但**本工具 Phase D 不實作 Canon Delta skill**。本檔為「framework reference」性質：

- 對齊 UD v0.5 §5 完整 framework
- 給未來實作對話（11+ 輪 master / 工具 B 翻譯工具 fork / Canon Delta skill 真正落地時）一個明確的 single source of truth
- 紀錄當前已 LOCKED 的設計選擇 + 未決細節 + 啟動條件 + 預期實作 scope

**Wave 15 紀律：** 本檔屬 master 端設計層紀錄；不寫 .claude/skills/canon-delta/SKILL.md；不寫 /canon-delta 觸發語；不擴 SPEC §12.8 或 UD §5 既有 wording。

---

# 1. 框架核心（對齊 UD v0.5 §5）

## 1.1 設計原則

依 SPEC §12.8 + REQUIREMENTS_LOCK §4.4：

- 定稿台詞揭露之前 Bible 沒寫清楚的設定時，**不直接**回寫
- 抽取 canon delta 候選 → 交 user 裁決
- user 拍板「採」才走對應 `/iterate-*` 寫回 Bible
- 違反此原則的 wording / mechanism 不入 framework

**為什麼不直接回寫：**
- 自動回寫風險高（agent 可能誤解台詞語境；可能編造設定）
- LOCKED 檔案需 user 拍板才能動（紀律）
- Canon Delta 屬「設定演進」性質；需 user 在「修台詞」vs「修 Bible」vs「retcon」三選一拍板（CONFLICT 類型尤其重要）

## 1.2 Canon Delta 四類型（依 UD §5.1）

| 類型 | 性質 | 處理 |
|---|---|---|
| **A 補充型** | Bible 已模糊涵蓋，台詞給出具體（例：Bible 寫「主角失去親人」，台詞中主角說「我女兒被燒死了」）| 候選回寫；不影響既有 Bible 內容 |
| **B 擴張型** | Bible 未涉及，台詞建立新事實（例：Bible 沒寫主角故鄉，台詞中主角說「我從『北霜城』來」）| 候選回寫；若涉新詞需 append 02_a 並標 INFERENCE |
| **C 衝突型** | 台詞與 Bible 既有設定衝突（例：Bible 寫「主角不會魔法」，台詞中主角施法）| **不直接回寫**；標 CANON_CONFLICT；user 三選一拍板（修台詞 / 修 Bible / retcon）|
| **D 暗示型** | 台詞暗示但未明說（例：主角與反派暗示有血緣）| 候選回寫標 INFERENCE；未來迭代再確認 candidate |

## 1.3 抽取演算法（依 UD §5.2）

```
function extract_canon_deltas(dialogue_path, task_path):
  dialogue = read_dialogue(dialogue_path)
  task = read_task(task_path)
  bible_entities = collect_referenced_entities(task)  # W / V / C / R / P / CH

  deltas = []
  for line in dialogue.lines:
    for entity in bible_entities:
      assertion = extract_assertion(line, entity)
      if assertion is None:
        continue
      bible_state = read_entity_state(entity)
      delta_type = classify_delta(assertion, bible_state)
      if delta_type != None:
        deltas.append({line, entity, delta_type, assertion, bible_state})

  return deltas
```

**演算法依賴：**
- agent 必須能讀 Bible 既有檔案的 frontmatter + 內容做比對
- 比對是語義層 — 用 00_a §3.3 診斷模式紀律（不過度抽取）
- 重要性 threshold（UD §5.6）：實體類型 ≤ C/R/V 抽取；具體屬性抽取；世界規則抽取；一次性場景細節不抽取；單純情緒表達不抽取

## 1.4 提案流程（依 UD §5.3）

agent 在台詞升 FINAL 時 **自動跑** delta 抽取（不需 user 主動觸發），結果寫入 09_e §9「上游文件回寫檢查」段：

```markdown
## 上游文件回寫檢查（自動抽取）

### Delta 候選清單

| # | 類型 | 涉及實體 | 台詞片段 | Bible 現況 | 建議處理 |
|---|---|---|---|---|---|
| 1 | A 補充 | C-主角A | 「我女兒被燒死了」 | 聲線卡未提親人具體細節 | 候選寫回 03_characters/main/主角A_聲線卡.md §背景 |
| 2 | B 擴張 | V | 「北霜城」 | 02_a 中無此詞 | 候選寫回 02_a §地名，標 INFERENCE 解禁章節 |
| 3 | C 衝突 | W-rules | 「（主角施法）」 | 01_a §2 寫「主角不會魔法」 | 衝突 — 使用者必須拍板 |

### 使用者拍板紀錄

- 候選 1: 採 / 棄 / 修改後採（請填）
- 候選 2: 採 / 棄 / 修改後採（請填）
- 候選 3: 衝突處理 — 修台詞 / 修 Bible / retcon
```

user 必須在 09_e §9 對每個 delta 候選做拍板才能升 FINAL。

## 1.5 回寫執行（依 UD §5.4）

**觸發：** user 在 09_e §9 拍板後，手動跑 `/iterate-<target_entity>`。

**執行流程：**

1. agent 從 09_e §9 讀已拍板的 delta 清單
2. 對每個拍板「採」的 delta：
   - 對應 entity 跑 00_j 迭代協議（變更點識別 / 影響範圍評估 / 收斂 / 執行 / 驗證）
   - 影響範圍評估標明「來自 09_e §9 canon delta」
3. 對每個拍板「衝突 — 修 Bible」的 delta：
   - 跑 00_j 迭代 + 完整影響範圍評估
   - 警告：可能會牽動既有 FINAL / LOCKED 台詞
4. 對每個拍板「衝突 — retcon」的 delta：
   - 走 UD §3.6.6 retcon 路徑（原版降 DEPRECATED，產生新版本）

## 1.6 與既有實體互動（依 UD §5.5）

- **W-rules**：變更影響大量下游；必須跑完整 00_j 雙路反查（貢獻者反查 + 依賴者反查）
- **C-***：變更只影響該角色相關檔案（聲線卡 / 04_a 關係段 / 05_c 弧線階段 / 該角色出場任務包與台詞）
- **LOCKED 檔案**：若 delta 涉及修改 LOCKED 檔 → 預設拒絕；user 明示「強制修改」時走 retcon 路徑（原 LOCKED 降 DEPRECATED）

## 1.7 phase_log 紀錄（依 UD §5.7）

```yaml
- phase: canon-delta-extract
  date: YYYY-MM-DD
  skill: /qa  # 自動觸發，子流程
  source_dialogue: <FINAL 台詞檔路徑>
  delta_candidates: <N>
  delta_path: <09_e §9 對應段落 anchor>

- phase: canon-delta-iterate
  date: YYYY-MM-DD
  skill: /iterate-world  # 或其他 iterate skill
  source_delta_record: <09_e 路徑 + §9 anchor>
  affected_entities: [...]
```

## 1.8 禁止事項（依 UD §5.6）

- agent **不得**自動寫回 Bible（即使類型 A/B 看似無害）— 必須 user 拍板
- agent **不得**在抽取階段就寫入實體檔案 — 抽取只寫入 09_e §9
- agent **不得**抽取過度瑣碎的 delta（一次性場景細節 / 單純情緒表達）

---

# 2. 框架使用情境（什麼時候會真正用到）

## 2.1 使用前提

Canon Delta 框架真正啟用需以下條件全達成：

| 前提 | 說明 |
|---|---|
| Milestone 4 已達成 | 工具 A 進入「production release」狀態；user 開始真實作品撰寫 |
| 至少 10+ 場 dialogue 進入 DIALOGUE_FINAL | 累積足夠多 final 台詞才會出現 canon delta 現象 |
| 09_e 定稿變更紀錄已在使用 | 09_e §9「上游文件回寫檢查」段需要實際 entry |
| User 主動跑量產 dialogue | Phase D 主軸完成 + Phase A.0F 前端工具完成後的「實際使用期」|

## 2.2 觸發時機

依 UD §5.2：**台詞檔 `pipeline_state` 升 `DIALOGUE_FINAL` 時，09_e 填寫過程中執行**。

具體 use case：
1. User 跑 /qa 對某場景台詞 PASS → user 跑 09_e final-gating → agent 抽取 delta 候選 → user 拍板 09_e §9 → user 跑 /iterate-<entity> → Bible 更新

## 2.3 對工具 B 翻譯工具（NEW_REQ_11）的關聯

若工具 B 啟動（翻譯工具 fork）：
- 翻譯員看到原作 source 時可能發現 Bible 缺漏（例：source 引用「北霜城」但 Bible V 沒此詞）
- 工具 B 可生成「翻譯端 canon delta 候選」回饋給工具 A
- 屬「跨工具回饋環」性質；本 framework 預留此擴充可能性

---

# 3. 未來實作 scope（給 11+ 輪 master / 工具 B 啟動時 reference）

## 3.1 本 Wave 15 不做的事

明示 scope 邊界（避免未來 master 誤解）：

- ✗ 不實作 `/canon-delta` skill
- ✗ 不擴 SPEC §12.8 / UD §5 既有 wording
- ✗ 不擴 09_e 模板的 §9 結構（既有 09_e 已含 §9 placeholder）
- ✗ 不擴 /qa skill（既有 /qa 不自動觸發 canon-delta-extract）
- ✗ 不擴 /iterate-* skill（既有 /iterate-* 不自動讀 09_e §9 delta 清單）

**現況：** 框架已 LOCKED 在 UD §5；09_e 模板已預留 §9 placeholder；但**自動抽取演算法 + 自動觸發機制屬未來實作 scope**。

## 3.2 未來實作預期 scope（成熟期；非本 Wave）

預期實作 task list（給未來 master 拍板 reference）：

| Task | scope | 預估工時 |
|---|---|---|
| **C-1** 寫 /canon-delta-extract sub-skill（屬 /qa 子流程） | 對應 UD §5.2 演算法；自動抽取 delta 候選寫 09_e §9 | 5-10h |
| **C-2** 擴 /qa skill：DIALOGUE_FINAL 時自動 trigger /canon-delta-extract | partial supersede /qa skill 9_e 階段 | 2-3h |
| **C-3** 擴 /iterate-* 5 個 skill：可讀 09_e §9 delta 清單作為 source | partial supersede /iterate-* 階段 2「變更點識別」 | 5-10h |
| **C-4** 寫 D-NNN 拍板（重要性 threshold 細化 + 衝突類型 retcon 路徑細化）| user 拍板 | 2-3h master 對話 |
| **C-5** 補 PHASE_E_COMPLETION_REPORT（屬「成熟期功能」phase）| Milestone 5 達成事實檔 | 3-5h |

**total 預估：** 20-35h master + CODEX 時間（不含 user-test）

## 3.3 啟動條件（未來 master 對話起手 reference）

當以下任一達成，未來 master 可啟動 Canon Delta 實作 phase：

| 啟動 trigger | 條件 |
|---|---|
| **A — Milestone 4 + 6 個月使用期** | 工具 A production release 後 6 個月；user 累積真實作品撰寫一段時間 |
| **B — 工具 B 翻譯工具 fork 前置** | NEW_REQ_11 工具 B 翻譯工具啟動前 — 翻譯員需要「跨工具 canon delta」機制 |
| **C — user 主動回報 canon delta 摩擦** | user 在跑量產 dialogue + /qa + 09_e 過程中明確回報「想自動抽取 Bible delta」需求 |
| **D — 跟 NEW_REQ_16/17/18 自動化 QA 工具同步實作** | 若 NEW_REQ_16 lint script 啟動實作 → 順手實作 canon-delta-extract sub-skill ROI 翻倍 |

---

# 4. UI/UX 對應規範（依 UD §5.8）

對 Phase A.0F 前端工具補完 / Phase A.0F 平行對話的設計接口：

- `[UX]` delta 候選清單的呈現格式（表格 vs 卡片式）
- `[UX]` user 拍板介面（一鍵採 / 棄 / 修改 / 衝突）
- `[UX]` 衝突 delta 的「修台詞 vs 修 Bible vs retcon」三選一視覺呈現
- `[UX]` 影響範圍評估的視覺化（樹狀圖式）

**Phase A.0F 平行對話可預留 09_e §9 viewer 元件**（即使本 Wave 不實作 /canon-delta skill；前端 viewer 可以解析 09_e §9「上游文件回寫檢查」段顯示給 user）。屬「對未來 friendly」設計選擇；不必本 Wave 落地。

---

# 5. 跟 Phase D 既有 skill 的關聯

## 5.1 跟 /qa 的關聯

- 既有 /qa skill 跑 8 報告（09_a/b/c/d/f/g/h/i）；09_e 屬 human final-gating 非 /qa scope（D-046 #5）
- 未來實作 /canon-delta-extract sub-skill 時，**屬 /qa skill 的擴充**（C-2 task）；對齊 UD §5.2「台詞檔 pipeline_state 升 DIALOGUE_FINAL 時，09_e 填寫過程中執行」
- /qa skill 本 Wave 不擴；屬未來 partial supersede scope

## 5.2 跟 /iterate-* 的關聯

- Wave 12 starter 已落地（D1-D5 + 00_j v0.2）；/iterate-* 6 個 SKILL.md（含 /iterate-scene --split-to-file）+ 5 個中文 wrapper **待 10th master 實作**（屬 deferred runtime；對齊 PHASE_D_COMPLETION_REPORT v1.0 §3 Wave 12 partial 紀錄）
- 未來 /iterate-* 實作時將含階段 2「變更點識別」step；屆時 **partial supersede /iterate-* 階段 2** 加「可讀 09_e §9 delta 清單作為 source」
- /iterate-* skill 本 Wave 不擴；屬未來 partial supersede scope（10th master scope）

## 5.3 跟 /diagnose / /integrate（Wave 15 新落地）的關聯

- /diagnose 屬「跨檔診斷」純讀取；**可能用於診斷 09_e §9 delta 清單健康度**（如：列出 user 拍板「待填」的 delta 候選）但屬於通用診斷模式應用 — 不擴 /diagnose specific 功能
- /integrate 屬「整理素材成模板欄位」；**不**屬 canon delta 機制；兩者 scope 區隔清晰

## 5.4 跟 09_e LOCKED 模板的關聯

09_e 模板已有 §9「上游文件回寫檢查」placeholder 段；未來實作 /canon-delta-extract sub-skill 時不需新增 09_e 模板 section（直接寫入 §9）。

---

# 6. 給未來 master 的提示

## 6.1 啟動前必讀

未來 master 對話啟動 Canon Delta 實作 phase 前必讀：

1. **本檔** `_design/CANON_DELTA_FRAMEWORK.md` v0.1
2. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §5（5.1-5.8 全節）
3. `_design/SPEC.md` v1.2 §12.8（影響範圍：下游 → 上游的 canon delta）
4. `_design/REQUIREMENTS_LOCK.md` v1.0 §4.4（Canon Delta 設計要求）
5. 既有 09_e 模板 §9 placeholder
6. 既有 /qa SKILL.md（屆時版本）
7. 既有 /iterate-* x5 SKILL.md（屆時版本）

## 6.2 設計選擇紀錄（已 LOCKED；不變動）

- ✅ Canon Delta 不直接回寫 Bible（user 拍板必經）
- ✅ 抽取演算法依 00_a §3.3 診斷模式紀律（不過度抽取）
- ✅ 4 類型分類（A 補充 / B 擴張 / C 衝突 / D 暗示）
- ✅ 衝突 delta 三選一拍板（修台詞 / 修 Bible / retcon）
- ✅ Bible 變更需走 00_j 迭代協議（含影響範圍評估）
- ✅ LOCKED 檔案 delta 預設拒絕；user 強制修改走 retcon 路徑

## 6.3 未決細節（待未來 master 拍板）

- **重要性 threshold 細化**：UD §5.6 列舉建議規則；具體實作時是 hard rule 還是 user-configurable
- **抽取演算法效能**：實體類型多時抽取速度（每場景跑多少次語意比對）
- **delta 候選 UI 呈現**：表格 vs 卡片 vs 樹狀圖
- **retcon 路徑與 Canon Delta 的整合**：UD §3.6.6 retcon 與 UD §5.4 「衝突 retcon」處理的精確 mechanic

---

# 7. Cross-ref

- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §5（Canon Delta 完整 framework — 本檔權威來源）
- `_design/SPEC.md` v1.2 §12.8（下游 → 上游的 canon delta；成熟期功能）
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.4（Canon Delta 設計要求）
- `_design/INTEGRATION_CONTRACTS.md` v2.1（如有相關 contract — 主要在 Contract A 系列）
- `_design/DECISIONS_LOG.md` v2.0 §6.X.X D-NNN（如有 canon-delta 相關拍板 — 目前 D-001~D-054 未含 specific D-NNN 拍板 canon-delta；未來可能新增）
- `_design/POST_LOCK_PENDING.md` v0.18 NEW_REQ_11 翻譯工具分支（潛在 reuse 對象）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid；Canon Delta 與 detailed-outline per-scene 拆檔的潛在互動）
- 既有 `09_quality_assurance/09_e_定稿變更紀錄模板.md`（含 §9 placeholder 段；本檔不擴模板）
- 既有 `.claude/skills/qa/SKILL.md` v0.X（未來擴充 /canon-delta-extract sub-skill 的 host）
- 既有 `.claude/skills/iterate-*/SKILL.md`（未來可讀 09_e §9 delta 清單作 source）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話 scope；本檔為 Wave 15 範圍）
- 未來 `_design/HANDOFF_TO_10TH_MASTER.md`（10th master 接手；屆時應 reference 本檔；含 Phase A.0F 結束後 Canon Delta 實作條件 trigger）

---

# 8. 維護紀律

- 本檔屬 framework reference；可持續追加未決細節（屬「未來 master 拍板待議題目」性質）
- **不**升 LOCKED（除非未來 master 對話完整實作 Canon Delta skill 後）
- 若 UD v0.5 §5 升版（partial supersede）→ 本檔同步對齊
- 若 /qa / /iterate-* / 09_e 任一 LOCKED 變更涉及 Canon Delta → 本檔加變更紀錄
- 不擅自擴 framework；UD §5 為權威；本檔只重述 + 加實作建議 scope + 跟 Phase D 既有 skill 的關聯
