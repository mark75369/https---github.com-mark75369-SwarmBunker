狀態：DRAFT  
版本：v0.4（8th master patch round 3 R9-MI-04 sweep — §4 Cross-ref create-outline v0.2 → v0.3 + character_review_log v0.2 → v0.3 對齊 patch round 2/3 升版事實）  
最後更新：2026-05-21  
適用範圍：Phase B 階段 B.6.5 主線（P）人類 REVIEW gate 升級紀錄  
優先級：高

# phase_b_outline_review_log — B.6.5 主線人類 REVIEW gate 升級紀錄

# 0. 文件目的

依 TASKS v1.9 §B.6.5「升級紀錄寫入 `_design/phase_b_outline_review_log.md`（標準文件頭）」紀錄 Phase B 階段主線實體（P）人類 REVIEW gate 通過時的升級事實。

本檔屬持續寫作（每次 B.6.5 過 gate 追加新 entry — 雖然 P 通常只有 1 個實體，但 iterate-outline 後若再次升 REVIEW 也追加 entry）。

**本檔在 Template repo 內為骨架（尚無實體 entry）**；user 在 Instance repo 跑 `/create-outline` 建立 P 後，依 `_design/CODEX_B65_REVIEW_GATE_STARTER.md` 親跑 B.6.5 → 在 Instance 端**追加** §1+ entry。

---

# 1. B.6.5 第一輪 — [INSTANCE 跑 /create-outline 後 user 親跑時補填]

> **使用方式：** user 在 Instance 跑完 /create-outline 建立 P 主線（寫入 05_a_主線大綱.md），依 `CODEX_B65_REVIEW_GATE_STARTER.md` §1 啟動 prompt 跑完印 P 狀態確認後，**手動升級 frontmatter** + **填本段**。

## 1.1 拍板背景

[user 自填 — 例：「主線骨架已過 5 階段對話 + 7 議題拍板（含起承轉合節奏 / 主題承載 / 主要轉折 / 結局基線 / 規模定位 / 篇幅 / 章節數）；資訊揭露順序與角色弧線對齊；信任當前完成度；可升 REVIEW 為 /create-detailed-outline 啟動條件鋪路」]

## 1.2 升級檔案 list

對齊 B65 starter v0.4 步驟 0 D-052 雙模式 prompt（4 個 P-tagged 檔範圍）：

| # | 檔 | 升級前 status | 升級後 status | entities | 升級日期 | 拍板 owner |
|---|---|---|---|---|---|---|
| 1 | `<instance_root>/05_plot/05_a_主線大綱.md` | DRAFT v0.1 | **REVIEW v0.1** | `[P]` | YYYY-MM-DD | user (\<email\>) |
| 2 | `<instance_root>/05_plot/05_c_角色弧線表.md`（optional — /create-outline 議題 4 觸發才寫）| DRAFT v0.1 | **REVIEW v0.1** | `[P]` | YYYY-MM-DD | user (\<email\>) |
| 3 | `<instance_root>/05_plot/05_d_資訊揭露表.md`（optional — /create-outline 議題 4 觸發才寫）| DRAFT v0.1 | **REVIEW v0.1** | `[P]` | YYYY-MM-DD | user (\<email\>) |
| 4 | `<instance_root>/05_plot/05_e_伏筆與回收表.md`（optional — /create-outline 議題 5 觸發才寫）| DRAFT v0.1 | **REVIEW v0.1** | `[P]` | YYYY-MM-DD | user (\<email\>) |

> 註：
> - 上述 4 個檔皆屬 P-tagged scope（`entities: [P]`）；高層 placeholder 性質（不含 CH-\* / S-\*-\* 等下游實體）。
> - 05_a 為必寫；05_c/05_d/05_e 為 /create-outline 議題 4/5 觸發的 optional 高層 placeholder（若 issue 4/5 沒觸發寫入則該檔仍為 Template 內 placeholder 不在升級 scope 內）。
> - 實際升級檔數依 /create-outline 階段 4 寫入結果決定（1-4 檔）；user 拍板時依該 Instance 實際情況選升幾個。
> - `05_a_主線大綱.md` 是 /create-outline 階段 4 從 Template `05_a_主線大綱模板.md` 衍生 + 填入 Instance 內容後的實體檔；同時 `00_b_*.md`（作品專屬資料）§3 規模定位 / §4 篇幅 / 章節數會被 /create-outline 寫回，但屬作品專屬段落不算 P 實體 frontmatter 升級範圍。

## 1.3 執行細節

- 升級動作：依 D-052（DECISIONS_LOG v1.9 §6.15.2）雙模式 — **預設方案 A（AI-assisted）：** user 明示拍板「同意升 P REVIEW + 拍板理由」後 agent 代執行 mechanical edits（4 個 P-tagged 檔 frontmatter + 本 review_log §1 entry）；**方案 B（manual fallback）：** user 親身編輯。兩方案的 accountability anchor 都是「user 明示拍板」 — 不違反 TASKS §B.6.5「CODEX 不得**自行**升級 P 的狀態」精神（「自行」=「未經 user 明示」；D-052 後 user 明示拍板後可代執行）
- 編輯內容：
  - 中文 5 欄 header 第 1 欄「狀態：DRAFT」→「狀態：REVIEW」
  - 中文 5 欄 header 第 3 欄「最後更新」更新為實際 review 日期（YYYY-MM-DD）
  - 版本欄不升（內容未改，只是 status 升）
  - YAML block `entities` / `depends_on` / `weight` 不動
  - body 內容不動
- 不動：
  - `05_b_章節結構模板.md`（章節結構 — D-050 子裁決 2 後屬 /create-detailed-outline 階段 4 寫入 scope，CH-\* entities；非本 B.6.5 P-gate 範圍）
  - 任何 C-\* / R-\* / CH-\* / S-\*-\* / W-\* / V-\* / 其他實體檔
  - protocol / spec / skill 任何檔
  - 作品專屬 00_b §3/§4 段落（屬 /create-outline 階段 4 已寫；不屬本 gate 升 status 範圍）

## 1.4 B.7 啟動條件對應

依 TASKS v1.9 §B.6.5 + §B.7 啟動條件「P 至少 REVIEW」：

- P（`<instance_root>/05_plot/05_a_主線大綱.md`）：✓ 已 REVIEW

**B.6.5 對 P B.7 /create-detailed-outline 啟動條件達成。**

---

# 2. 未升 REVIEW 的 DRAFT 檔（明示保留）

P 實體通常每 Instance 只有 1 個 — 若 user 暫不升 REVIEW（例：要先回去迭代 /create-character 才能定主線），在此明示保留：

[例：「P 暫保留 DRAFT — 主線結局基線待定，等迭代 C-反派 後再升」]

---

# 3. 跨輪追加紀律

本檔屬持續寫作（同 `phase_a_review_log.md` 性質）：

- 每輪 B.6.5 review gate 完成後追加新 § entry（保留歷史）
- 每筆 entry 含：拍板背景 / 升級 list（含日期 + owner）/ 執行細節 / 對應 B.7 啟動條件
- 不刪除歷史 entry（review 紀錄事實檔）
- iterate-outline（Phase C `/iterate-*` skill）後若 P 重新進 DRAFT → REVIEW，追加 §2 / §3 entry

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §B.6.5（B.6.5 人類 REVIEW gate 規範權威）
- `_design/CODEX_B65_REVIEW_GATE_STARTER.md`（本 gate 操作指引）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.3（00_g 大綱協議銜接點）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.4（00_h 細綱協議啟動條件 — P REVIEW）
- `_design/phase_a_review_log.md` v0.1（A.10 範本參考）
- `_design/phase_b_character_review_log.md` v0.3（B.5.5 同類型 review log 對照）
- `00_protocol/00_g_大綱創建協議.md` v0.2（P 創建協議）
- `00_protocol/00_h_細綱創建協議.md` v0.2（CH-\* / S-\*-\* 創建協議；引用 B.6.5 後升 REVIEW 之 P）
- `.claude/skills/create-outline/SKILL.md` v0.3（B.6 主 skill；含 D-050 對齊 + D-053 exception block）
- TASKS v1.9 §B.7（B.7 啟動條件依 B.6.5 PASS — 屬 Wave 8 scope）
- `_design/HANDOFF_TO_7TH_MASTER.md` v1.1（第七輪 master scope 紀錄）
