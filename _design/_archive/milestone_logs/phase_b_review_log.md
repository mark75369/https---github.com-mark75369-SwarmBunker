狀態：DRAFT  
版本：v0.6（9th master cleanup queue R10-MI-01/02 sweep — §4 Cross-ref active stale 對齊當前事實：create-detailed-outline v0.2 → v0.3（CH skill R9-INFO-02 patch round 3 升 v0.3）+ phase_b_character_review_log v0.2 → v0.3 + phase_b_outline_review_log v0.3 → v0.4；用一次性 sweep 處理避免「Fix one, find two」cascade）  
最後更新：2026-05-22  
適用範圍：Phase B 後 B.8 整體人類 REVIEW gate 升級紀錄  
優先級：高

# phase_b_review_log — B.8 Phase B 整體人類 REVIEW gate 升級紀錄

# 0. 文件目的

依 TASKS v1.9 §B.8「升級紀錄寫入 `_design/phase_b_review_log.md`（標準文件頭）」紀錄 Phase B 收尾整體 REVIEW gate 通過時的所有實體升級事實 — 涵蓋 C-\* / R-\*-\* / P / CH-\* / S-\*-\* 五類實體。

本檔屬持續寫作（每次 B.8 過 gate 追加新 entry — 雖然 B.8 通常每個 Instance 只跑一次，但若 Phase C `/iterate-*` 後重新 review 也追加 entry）。

**本檔在 Template repo 內為骨架（尚無實體 entry）**；user 在 Instance repo 跑完整 5 個 /create-\* skill 鏈 + B.5.5 + B.6.5 後，依 `_design/CODEX_B8_REVIEW_GATE_STARTER.md` 親跑 B.8 → 在 Instance 端**追加** §1+ entry。

**與 B.5.5 / B.6.5 review log 的關係：**
- B.5.5（`phase_b_character_review_log.md`）：B.5 → B.5b 中段 gate；升 ≥ 2 個 C-\* REVIEW
- B.6.5（`phase_b_outline_review_log.md`）：B.6 → B.7 中段 gate；升 P REVIEW
- B.8（本檔）：Phase B 整體收尾 gate；升**所有剩餘** DRAFT 實體（包含 B.5.5 / B.6.5 後仍 DRAFT 的配角 C-\* + B.7 新建的 CH-\* / S-\*-\* + 連帶要升 REVIEW 的 R-\*-\*）

---

# 1. B.8 第一輪 — [INSTANCE 跑完 5 個 /create-\* skill 後 user 親跑時補填]

> **使用方式：** user 在 Instance 跑完 /create-character ≥ 2 次 + B.5.5 + /create-relationship + /create-outline + B.6.5 + /create-detailed-outline 後，依 `CODEX_B8_REVIEW_GATE_STARTER.md` §1 啟動 prompt 跑完印 5 類實體狀態清單後，**手動升級所有目標 frontmatter** + **填本段**。

## 1.1 拍板背景

[user 自填 — 例：「Phase B 5 個上游 skill 全跑完；C-\* 配角 / R-\* 副線關係 / CH-\* / S-\*-\* 待補 REVIEW；信任當前完成度；可整體升 REVIEW 為 Phase C /scene-task + /dialogue-write 啟動條件鋪路（Phase D 整體驗收需 W/V/C/R/P/CH/S 全 ≥ REVIEW）」]

## 1.2 升級檔案 list

### 1.2.1 C-\* 角色實體（B.5.5 後剩餘 + 第二批 C-\*）

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/03_characters/<subtype>/<name3>.md` | DRAFT v0.1 | **REVIEW v0.1** | `[C-<name3>]` | YYYY-MM-DD | user (\<email\>) |
| ... | ... | ... | ... | ... | ... | ... |

> 註：B.5.5 已升的 C-\* 不在本段重複列；本段只列 B.5.5 後剩餘 / 後續新建的 C-\*。

### 1.2.2 R-\*-\* 關係實體

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/04_relationships/04_a_<a>_<b>_關係.md` | DRAFT v0.1 | **REVIEW v0.1** | `[R-<a>-<b>]` | YYYY-MM-DD | user (\<email\>) |
| ... | ... | ... | ... | ... | ... | ... |

> 註：R-\*-\* 實際檔名與分拆位置以 /create-relationship skill 階段 4 拆分產物為準（含 04_a 對應段落 + 04_b 時間線）。

### 1.2.3 P 主線實體（B.6.5 後若仍需重升或不變動）

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/05_plot/05_a_主線大綱.md` | REVIEW v0.1 | REVIEW v0.1（**B.6.5 已升；本輪維持**）| `[P]` | YYYY-MM-DD | user (\<email\>) |

> 註：B.6.5 已升 P REVIEW；本段通常不再動 P 狀態，列出為「整體 review 確認 P 狀態」。若 B.6.5 後 user 跑 /iterate-outline 把 P 退回 DRAFT 又重升 REVIEW，在此追加紀錄。

### 1.2.4 CH-\* 章節實體（B.7 新建 — D-050 子裁決 2 CH 行限定 05_b 唯一寫檔位置）

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/05_plot/05_b_章節結構.md` | DRAFT v0.1 | **REVIEW v0.1** | `[CH-1, CH-2, ..., CH-n]` | YYYY-MM-DD | user (\<email\>) |

> 註：**05_c / 05_d / 05_e 不屬本表**（不是 CH-\* 章節實體寫檔範圍）— 它們是 P /create-outline 議題 4/5 觸發的高層 P-scoped placeholder，entities=[P]；對應升 REVIEW 屬 §1.2.3 P 段範圍（B.6.5 已升）。D-050 子裁決 2 CH 行明示 /create-detailed-outline runtime 寫檔限 `05_b` + `06_a` only。

### 1.2.5 S-\*-\* 場景索引實體（B.7 新建；每場景一檔）

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/06_scene_index/CH1_S1_<scene_name>.md` | DRAFT v0.1 | **REVIEW v0.1** | `[S-1-1]` | YYYY-MM-DD | user (\<email\>) |
| 2 | `<instance_root>/06_scene_index/CH1_S2_<scene_name>.md` | DRAFT v0.1 | **REVIEW v0.1** | `[S-1-2]` | YYYY-MM-DD | user (\<email\>) |
| ... | ... | ... | ... | ... | ... | ... |

> 註：S-\*-\* 場景索引一場一檔；命名規則依 SPEC §5.1 + 00_h §10.8 為準。Phase D 整體驗收要求 S-\*-\* 至少 REVIEW（依 TASKS v1.9 §B.8 line 1379 補 #5）。

## 1.3 執行細節

- 升級動作：依 D-052（DECISIONS_LOG v1.9 §6.15.2）雙模式 — **預設方案 A（AI-assisted）：** user 明示拍板「同意升 N 個檔 + 拍板理由」後 agent 代執行 mechanical edits（5 類實體 frontmatter + 本 review_log §1 entry 5 個 §1.2.X 子段全填）；**方案 B（manual fallback）：** user 親身編輯。兩方案的 accountability anchor 都是「user 明示拍板」 — 不違反 TASKS §B.8「CODEX 不得**自行**升級」精神（「自行」=「未經 user 明示」；D-052 後 user 明示拍板後可代執行）
- 編輯內容：
  - 中文 5 欄 header 第 1 欄「狀態：DRAFT」→「狀態：REVIEW」
  - 中文 5 欄 header 第 3 欄「最後更新」更新為實際 review 日期（YYYY-MM-DD）
  - 版本欄不升（內容未改，只是 status 升）
  - YAML block `entities` / `depends_on` / `weight` 不動
  - body 內容不動
- 不動：
  - W-\* / V-\*（已在 A.10 升 REVIEW；本輪不重複升）
  - 已在 B.5.5 / B.6.5 升 REVIEW 的 C-\* / P（本輪 §1.2.3 列為「維持」）
  - protocol / spec / skill 任何檔
  - 作品專屬 00_b §1-§7 任何段落（屬各 /create-\* skill 階段 4 已寫；不在本 gate 升 status 範圍）

## 1.4 Phase C / Phase D 啟動條件對應

依 TASKS v1.9 §B.8 + Phase C / Phase D 啟動條件「W/V/C/R/P/CH/S 全部至少 REVIEW」：

- W-rules：✓ A.10 已 REVIEW
- W-language：✓ A.10 已 REVIEW
- V：✓ A.10 已 REVIEW
- C-\*（含主角 / 反派 / 配角全套）：✓ B.5.5 + 本輪 §1.2.1 共同覆蓋
- R-\*-\*（含主反派 / 副線關係全套）：✓ 本輪 §1.2.2 覆蓋
- P：✓ B.6.5 已 REVIEW（本輪 §1.2.3 維持）
- CH-\*（全章節）：✓ 本輪 §1.2.4 覆蓋
- S-\*-\*（全場景索引）：✓ 本輪 §1.2.5 覆蓋

**B.8 對全套 W/V/C/R/P/CH/S Phase C / Phase D 啟動條件達成。**

---

# 2. 未升 REVIEW 的 DRAFT 檔（明示保留）

[user 若有特定實體暫不升 REVIEW，在此明示理由 + 影響範圍]

例：
- 「C-\<minor_npc1\> 暫保留 DRAFT — 配角設定預期 Phase C /iterate-character 後再升；不影響 Phase D 整體驗收（minor npc 屬選擇性 REVIEW）」
- 「S-3-5 暫保留 DRAFT — 該場景結局走向待 user 審 P 結局後決定」

> 註：B.8 整體 PASS 條件依 TASKS v1.9 §B.8 是「人類完成所有需要升級的檔案」 — user 可依創作節奏選擇保留哪些 DRAFT。但 Phase D 整體驗收（D.7）會再卡 W/V/C/R/P/CH/S 整套 ≥ REVIEW 要求；本檔保留的 DRAFT 屆時需處理。

---

# 3. 跨輪追加紀律

本檔屬持續寫作（同 `phase_a_review_log.md` / `phase_b_character_review_log.md` / `phase_b_outline_review_log.md` 性質）：

- 每輪 B.8 review gate 完成後追加新 § entry（保留歷史）
- 每筆 entry 含：拍板背景 / 5 類實體升級 list（含日期 + owner）/ 執行細節 / 對應 Phase C/D 啟動條件
- 不刪除歷史 entry（review 紀錄事實檔）
- Phase C `/iterate-*` 後若某些實體重新進 DRAFT → REVIEW，追加 §2 / §3 entry
- Phase D 完成後（dialogue 內容定稿）追加對應升級紀錄（屆時可能合併入 `_design/phase_d_dialogue_review_log.md`）

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §B.8（B.8 Phase B 整體 REVIEW gate 規範權威）
- `_design/CODEX_B8_REVIEW_GATE_STARTER.md`（本 gate 操作指引）
- `_design/TASKS.md` v1.9 §B.9（B.8 後續 — Phase B 整體驗收）
- `_design/phase_a_review_log.md` v0.1（A.10 W/V 升級先例）
- `_design/phase_b_character_review_log.md` v0.3（B.5.5 C-\* 升級紀錄；不重複升）
- `_design/phase_b_outline_review_log.md` v0.4（B.6.5 P 升級紀錄；不重複升）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2~§1.5（5 上游 protocol 銜接點）
- `00_protocol/00_f / 00_g / 00_h / 00_l` v0.2（4 上游 protocol）
- `.claude/skills/create-character/SKILL.md` v0.4（B.5 主 skill；含 D-050 對齊 + D-053 exception + Round 11 R11-CRITICAL-01 修補）
- `.claude/skills/create-relationship/SKILL.md` v0.3（B.5b 主 skill；含 D-050 對齊 + D-053 exception）
- `.claude/skills/create-outline/SKILL.md` v0.3（B.6 主 skill；含 D-050 對齊 + D-053 exception）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（B.7 主 skill；D-050 對齊 + R8-MA-01 prereq fix + R9-INFO-02 body D-050 子裁決 1+2 雙 block）
- `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope）
