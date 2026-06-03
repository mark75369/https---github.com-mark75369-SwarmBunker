狀態：DRAFT  
版本：v0.3（8th master patch round 3 R9-MI-03 sweep — §4 Cross-ref create-character / create-relationship v0.2 → v0.3 對齊 patch round 2 升版事實）  
最後更新：2026-05-21  
適用範圍：Phase B 階段 B.5.5 角色（C-\*）人類 REVIEW gate 升級紀錄  
優先級：高

# phase_b_character_review_log — B.5.5 角色人類 REVIEW gate 升級紀錄

# 0. 文件目的

依 TASKS v1.9 §B.5.5「升級紀錄寫入 `_design/phase_b_character_review_log.md`（標準文件頭）」紀錄 Phase B 階段角色實體（C-\*）人類 REVIEW gate 通過時的升級事實。

本檔屬持續寫作（每次 B.5.5 過 gate 追加新 entry）。

**本檔在 Template repo 內為骨架（尚無實體 entry）**；user 在 Instance repo 跑 `/create-character` 建立至少 2 個 C-\* 後，依 `_design/CODEX_B55_REVIEW_GATE_STARTER.md` 親跑 B.5.5 → 在 Instance 端**追加** §1+ entry。

---

# 1. B.5.5 第一輪 — [INSTANCE 跑 /create-character 後 user 親跑時補填]

> **使用方式：** user 在 Instance 跑完 /create-character 至少 2 次（建立要建立關係的兩角色），依 `CODEX_B55_REVIEW_GATE_STARTER.md` §1 啟動 prompt 跑完印 C-\* 狀態清單後，**手動升級 frontmatter** + **填本段**。

## 1.1 拍板背景

[user 自填 — 例：「2 個主角聲線卡 / 偏移檢查 / 合規檢查已 review 完；對應 5 階段流程跑通；信任當前完成度；可升 REVIEW 為 /create-relationship 啟動條件鋪路」]

## 1.2 升級檔案 list

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `03_characters/<subtype>/<name1>.md` | DRAFT v0.1 | **REVIEW v0.1** | `[C-<name1>]` | YYYY-MM-DD | user (\<email\>) |
| 2 | `03_characters/<subtype>/<name2>.md` | DRAFT v0.1 | **REVIEW v0.1** | `[C-<name2>]` | YYYY-MM-DD | user (\<email\>) |

> 註：`<subtype>` ∈ `main` / `minor` / `npc`；依 /create-character 階段 4 分流決定。

## 1.3 執行細節

- 升級動作：依 D-052（DECISIONS_LOG v1.9 §6.15.2）雙模式 — **預設方案 A（AI-assisted）：** user 明示拍板「同意升 N 個檔 REVIEW + 拍板理由」後 agent 代執行 mechanical edits（C-\* frontmatter + 本 review_log §1 entry）；**方案 B（manual fallback）：** user 親身編輯。兩方案的 accountability anchor 都是「user 明示拍板」 — 不違反 TASKS §B.5.5「CODEX 不得**自行**升級」精神（「自行」=「未經 user 明示」；D-052 後 user 明示拍板後可代執行）
- 編輯內容：
  - 中文 5 欄 header 第 1 欄「狀態：DRAFT」→「狀態：REVIEW」
  - 中文 5 欄 header 第 3 欄「最後更新」更新為實際 review 日期（YYYY-MM-DD）
  - 版本欄不升（內容未改，只是 status 升）
  - YAML block `entities` / `depends_on` / `weight` 不動
  - body 內容不動
- 不動：
  - 其他 C-\* 檔（未升 REVIEW 的角色）
  - 任何 R-\* / P / CH-\* / W-\* / V-\* / 其他實體檔
  - protocol / spec / skill 任何檔

## 1.4 B.5b 啟動條件對應

依 TASKS v1.9 §B.5.5 + §B.5b 啟動條件「兩個 C-\* 都至少 REVIEW」：

- C-\<name1\>：✓ 已 REVIEW
- C-\<name2\>：✓ 已 REVIEW

**B.5.5 對 C-\* 配對 B.5b 啟動條件達成。**

---

# 2. 未升 REVIEW 的 DRAFT 檔（明示保留）

[user 若 Instance 有多於 2 個 C-\* 但本輪只升 2 個，在此明示哪些 C-\* 保留 DRAFT；避免後續混淆。例：「C-\<name3\> 暫保留 DRAFT — 配角設定未跑完聲線卡」]

---

# 3. 跨輪追加紀律

本檔屬持續寫作（同 `phase_a_review_log.md` 性質）：

- 每輪 B.5.5 review gate 完成後追加新 § entry（保留歷史）
- 每筆 entry 含：拍板背景 / 升級 list（含日期 + owner）/ 執行細節 / 對應 B.5b 啟動條件
- 不刪除歷史 entry（review 紀錄事實檔）
- Phase B 後期若再 review 新增 C-\*（例：第二批配角）→ 追加 §2 / §3 entry

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §B.5.5（B.5.5 人類 REVIEW gate 規範）
- `_design/CODEX_B55_REVIEW_GATE_STARTER.md`（本 gate 操作指引）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2（00_f 角色協議銜接點）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.5（00_l 關係協議啟動條件）
- `_design/phase_a_review_log.md` v0.1（同類型 review log 範本）
- `00_protocol/00_f_角色創建協議.md` v0.2（C-\* 創建協議）
- `00_protocol/00_l_關係創建協議.md` v0.2（R-\* 創建協議；引用 B.5.5 後升 REVIEW 之 C-\*）
- `.claude/skills/create-character/SKILL.md` v0.3（B.5 主 skill；含 D-050 對齊 + D-053 exception block）
- `.claude/skills/create-relationship/SKILL.md` v0.3（B.5b 主 skill；含 D-050 對齊 + D-053 exception block；啟動條件依 B.5.5 PASS）
- `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope 紀錄）
