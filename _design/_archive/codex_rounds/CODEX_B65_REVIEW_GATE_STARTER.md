狀態：DRAFT  
版本：v0.4（8th master Cleanup round R7-MA-03 — 性質 / 身份與職責 / 不變範圍 段同步對齊 D-052 雙模式 active wording；v0.3 §1 步驟 0 雙模式 prompt 維持）  
最後更新：2026-05-21  
適用範圍：Phase B Wave 7 B.6.5 task 啟動包 — 主線（P）人類 REVIEW gate  
優先級：高

# CODEX_B65_REVIEW_GATE_STARTER — Phase B Wave 7 B.6.5：主線 REVIEW gate

# 0. 本檔用途

> **v0.1 → v0.2 D-052 supersede 註記（2026-05-20）：**
>
> 既有 v0.1 採 manual-only flow — M2 testing 期間累積 user friction（特別是 P 4 個 contributing 檔的 frontmatter status 升 + review_log §1 patch；user 易誤覆蓋整檔）。
>
> **D-052（DECISIONS_LOG v1.8 §6.15.2）拍板：** partial supersede TASKS §B.6.5「禁止 CODEX 自行升 P 狀態」段加 user 明示拍板後 AI-execute exception。
>
> **本 starter v0.2 加雙模式流程：**
> - **方案 A（D-052 後預設）：AI-assisted upgrade** — user 明示拍板「同意升 P + 拍板理由」後，AI 代為執行 mechanical edits（4 個 P-tagged 檔 frontmatter + phase_b_outline_review_log §1 entry 寫入）+ 跑 /status verify
> - **方案 B（manual fallback）：** user 親身編輯 — 沿用 v0.1 流程

Wave 7 最後一條 task — **B.6.5 主線（P）人類 REVIEW gate**，對齊 TASKS v1.9 §B.6.5（D-052 後）。

**性質：人類拍板 REVIEW gate**（同 A.10 / B.5.5 模式）— 不是 CODEX implement task。CODEX 印 P 狀態確認供 user 人工檢視；**升級 frontmatter 動作走 D-052 雙模式 — 預設方案 A AI-assisted（user 明示拍板「同意升 P REVIEW + 拍板理由」後 agent 代執行 4 個 P-tagged 檔 frontmatter + review_log §1 entry mechanical edits）；方案 B manual 為 fallback**。

**前置條件：**
- Wave 7 B.6 DONE（/create-outline skill 已實作 + 5 階段可跑）
- user 已在 Instance repo 跑完 B.5（建至少 2 個 C-\*） + B.5.5（升 ≥ 2 個 C-\* REVIEW）+ B.5b（建 R-\*-\*） + B.6（建 P 主線；寫入 `<instance_root>/05_plot/05_a_主線大綱.md`）

**B.6.5 PASS → Wave 7 結束 → 開放 Wave 8（B.7 /create-detailed-outline + B.8 Phase B REVIEW gate + B.9 整體驗收）。**

⚠ **本 task 不在 Template repo 跑**（Template 沒有 P 實體；05_a 只有 `05_a_主線大綱模板.md` 為 Template 範本）— **user 必須在 Instance repo 內跑**（即 user Instance 已有 `<instance_root>/05_plot/05_a_主線大綱.md` 為 P 實體檔）。

⚠ **三大紀律（依 TASKS §B.6.5）：**

- CODEX **不得「自行」升級 P 的狀態** — 「自行」精細化（D-052 後）：CODEX 未經 user 明示拍板不得擅自升級；但 user 明示拍板「同意升 + 拍板理由」後可代為執行 mechanical edits（方案 A AI-assisted；4 個 P-tagged 檔 frontmatter + review_log §1 entry）
- 不得直接跳到 B.7 /create-detailed-outline（要先過此 gate）
- user 拍板「升 REVIEW」/「保留 DRAFT 並回去迭代上游」均屬合法選項，CODEX 依 user 拍板執行（方案 A）或 user 親手編輯（方案 B fallback）

---

# 1. 啟動 prompt（user 在 Instance repo 內複製整段到 agent 對話）

~~~
你是 game-dialogue-bible 專案 Instance 的 agent（Claude Code CLI / Codex CLI / Codex App / Cowork 任一環境）。

本輪是「Phase B Wave 7 B.6.5 task」— 主線（P）人類 REVIEW gate，對齊 TASKS v1.9 §B.6.5。

工作資料夾：<instance_root>（user 親跑時自填，例：D:\my-novel-instance）

**你的身份與職責：**

- 你是 review gate facilitator — 本輪印 P 狀態確認 + 提示 user 拍板升 REVIEW（D-052 雙模式：預設 AI-assisted / manual fallback）+ 引導升級紀錄寫入 _design/phase_b_outline_review_log.md
- 對應傳統：Wave 7 第四條 task（最終）；B.6.5 PASS → 可進 Wave 8（B.7 細綱實作）

**重要邊界（嚴格 scope；依 TASKS §B.6.5 三大禁止項）：**

- ✗ 不得自行升級 P 檔（05_plot/05_a_主線大綱.md）的 status
- ✗ 不得直接跳到 B.7 /create-detailed-outline（要先過此 gate）
- ✗ 不得改任何 C-* / R-* / CH-* / W-* / V-* / 其他實體檔
- ✗ 不得改 05_b / 05_c / 05_d / 05_e 模板檔（屬 B.7 階段 4 才會動）
- ✗ 不得改作品專屬 00_b §3 規模定位 / §4 篇幅 / 章節數段落（屬 B.6 階段 4 已寫；不在本 gate 升 status 範圍）
- ✗ 不得改 protocol / spec / skill 任何檔
- ✗ 不得跑真實 /create-detailed-outline 寫檔（屬 Wave 8 user 操作）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.6.5（D-052 partial supersede 後）：

1. **印 P 狀態確認供 user 人工檢視**
2. **提示啟動條件 + 升級操作指引**
3. **依 D-052 雙模式之一執行升級**：
   - **方案 A（預設）：AI-assisted upgrade** — user 明示拍板後 agent 執行 mechanical edits（4 個 P-tagged 檔 frontmatter + review_log §1 entry）
   - **方案 B（fallback）：manual upgrade**

### 步驟 0：D-052 雙模式選擇（TASKS v1.9 後預設）

印完步驟 1 清單後 + 印步驟 2 提示後，問 user：

```
[D-052 雙模式選擇]

預設走方案 A（AI-assisted）：你給我「同意升 P REVIEW + 拍板理由：[一句話]」，我代執行：
  - 對 4 個 P-tagged 檔（05_a / 05_c / 05_d / 05_e）frontmatter「狀態：DRAFT」→「狀態：REVIEW」+「最後更新」→ 今天
  - patch _design/phase_b_outline_review_log.md §1 entry（精確邊界 — 不全檔覆蓋）
  - 跑 /status verify
  - 給你 git diff 看

或回「我自己手動改」走方案 B（manual fallback；走後續步驟 1-3）。
```

依 user 明示回應決定走方案 A 或方案 B。

**方案 A 執行紀律：** 同 B.5.5 starter 步驟 0「方案 A 執行紀律」（AI 限改 frontmatter status + 最後更新；精確邊界 patch review_log；§1.1 含 user 拍板原文 + email + 時間戳；git diff 給 user 看）。

**方案 B 走以下步驟 1-3（原 manual flow）：**

### 步驟 1：印 P 狀態確認

跑以下命令找出 entities: [P] 的檔，列出 path / status / version / entities：

```bash
# 找 frontmatter 含 entities: [P] 的檔（通常只有 05_plot/05_a_主線大綱.md）
grep -lE "^entities:\s*\[P\]" 05_plot/*.md 2>/dev/null
```

對找到的檔，print 以下 4 個欄位（從 frontmatter 抓）：

| 路徑 | status | version | entities |
|---|---|---|---|
| `05_plot/05_a_主線大綱.md` | DRAFT / REVIEW | v0.1 | `[P]` |

也可用 build_repo_index：

```python
from scripts.parse_frontmatter import build_repo_index
result = build_repo_index('.')
p_entities = [e for e in result.entities if e.entity_id == 'P']
for e in p_entities:
    print(f"{e.path}  |  {e.status}  |  {e.version}  |  {e.entity_id}")
```

如果找到 0 個 P 實體 — 表示 user 還沒跑 /create-outline；agent 應拒絕進行本 gate 並提示 user 回去跑 /create-outline。

如果找到 > 1 個 P 實體 — 屬資料異常（P 唯一性違反 SPEC §5.1）；agent 應 WARN 並列出所有 P 檔，等 user 處理後重跑。

### 步驟 2：印提示文案（一字不漏給 user）

```
[B.6.5 主線 REVIEW gate 提示]

依 TASKS v1.9 §B.6.5 + §B.7 啟動條件：

  /create-detailed-outline 需要 P 至少 REVIEW；
  請人類審完後手動把 frontmatter 狀態升 REVIEW。

審查重點建議（user 親審；非 strict 清單）：
  ☐ 起承轉合節奏對齊主題
  ☐ 主要轉折邏輯通順
  ☐ 結局基線拍板（含主題承載）
  ☐ 規模定位（短篇 / 中篇 / 長篇）已寫回作品 00_b §3
  ☐ 篇幅 / 章節數已寫回作品 00_b §4
  ☐ 資訊揭露順序對齊主角弧線
  ☐ 主要角色（C-*）在主線各幕的位置已明確

升級動作（user 親跑）：
  1. 開啟 05_plot/05_a_主線大綱.md
  2. 把中文 5 欄 header 第 1 欄「狀態：DRAFT」改為「狀態：REVIEW」
  3. 把第 3 欄「最後更新」改為今天日期（YYYY-MM-DD）
  4. 版本欄不升（內容未改，只是 status 升）
  5. YAML block entities / depends_on / weight 不動
  6. body 內容不動（主線骨架已在 /create-outline 階段 4 寫入）

升完後：
  7. 開啟 _design/phase_b_outline_review_log.md
  8. 在 §1 填入 1.1 拍板背景 / 1.2 升級檔案 list / 1.3 執行細節 / 1.4 B.7 啟動條件對應

不要直接跳到 /create-detailed-outline — 先把上述完成。

如果審查時發現主線需要回去迭代：
  - 保留 DRAFT 不升
  - 回去跑 /iterate-outline（Phase C skill 實作後可用）
  - 或手動編輯 05_a 後再回來跑 B.6.5
  - §2 「未升 REVIEW 的 DRAFT 檔」段落明示保留理由
```

### 步驟 3：等 user 回報

user 完成升級後會回報「已升 P REVIEW + 寫好 phase_b_outline_review_log.md」。

agent 此時應：

1. 再跑步驟 1 的 grep / build_repo_index 驗證 P status == REVIEW
2. 讀 _design/phase_b_outline_review_log.md 驗證 §1 已填（不再是 placeholder）
3. 回報「B.6.5 PASS — Wave 7 結束 — 可進 Wave 8（B.7 /create-detailed-outline）」

### 不變範圍（嚴格）

- 不改 LOCKED spec / registry / parser code
- 不改既有 27 模板 / 00_protocol/ 任何檔
- 不改 .claude/skills/*/SKILL.md 任何檔
- 不擅自升任何檔狀態（未經 user 明示拍板）；user 明示拍板後可走方案 A AI-assisted 代執行 mechanical edits（限 status + 最後更新欄，不動 body / entities / depends_on / weight / 版本）
- 不跑真實 /create-detailed-outline 寫檔

### 完成判定

✓ P（05_plot/05_a_主線大綱.md）status == REVIEW
✓ _design/phase_b_outline_review_log.md §1 已 user 親填（拍板背景 + 升級 list + 執行細節 + B.7 啟動條件對應）
✓ user 拍板「B.6.5 PASS — Wave 7 結束 — 可進 Wave 8」

請依上述步驟跑。
~~~

---

# 2. 對 user 的補充說明（不在 agent prompt 內）

## 2.1 為什麼 B.6.5 是人類 gate（而非 CODEX 跑）

- P 主線是「對作品結構的最高承諾」 — 升 REVIEW 等於正式承認此主線定稿基線；下游 B.7 細綱會把 P 拆成 CH-\* 章節 + S-\*-\* 場景索引，一旦拆完回頭改 P 代價高
- AI 無法替 user 拍板「我這部作品就是要寫成這個主線」 — 必須人類拍板（同 B.5.5 模式：人類對長期創作資產的承諾）
- 對齊 SPEC §5.3 完成度公式：DRAFT 25 → REVIEW 75 — REVIEW 表「主線骨架定稿；剩細節 LOCKED 才 100」

## 2.2 升 REVIEW 後可以做什麼

- 跑 `/create-detailed-outline` 把 P 拆成 CH-\* + S-\*-\*（B.7 skill，屬 Wave 8）
- 跑 `/iterate-outline` 對 REVIEW P 做有監督迭代（Phase C `/iterate-*` skill 實作後）
- 跑 `/view-outline` 看整合視圖（Phase D `/view-*` skill 實作後）
- 跑 `/export-outline` 寫出 `view/outline.md` 整合檔（Phase D `/export-*` skill 實作後）

## 2.3 B.6.5 跟 B.5.5 的差異

| 維度 | B.5.5（角色 gate）| B.6.5（主線 gate）|
|---|---|---|
| 升的對象 | C-\* 多個（≥ 2）| P 單一 |
| 對應檔位置 | `03_characters/<subtype>/<name>.md` | `<instance_root>/05_plot/05_a_主線大綱.md` |
| 升的數量門檻 | ≥ 2 個 REVIEW（為 /create-relationship 鋪路）| 1 個 REVIEW（P 唯一）|
| 對齊下游啟動條件 | B.5b /create-relationship | B.7 /create-detailed-outline |
| 紀錄檔 | `phase_b_character_review_log.md` | `phase_b_outline_review_log.md` |
| 跨輪追加典型情境 | 第二批配角後追加 | iterate-outline 後 P 重升時追加 |

## 2.4 如果 user 還沒跑 /create-outline

啟動條件不滿足 — 應該回去跑 Wave 7 前序：

```
B.5（/create-character）≥ 2 次 → B.5.5（C-* review gate）→ B.5b（/create-relationship）→ B.6（/create-outline）→ B.6.5（本 gate）
```

跳階段機制（SPEC §10 / D-019 / D-031）允許 user 用「手稿導入」路徑直接補 P 實體骨架（不跑 /create-outline 5 階段對話），但仍要走 B.6.5 review gate 升 REVIEW 才能進 B.7。

## 2.5 如果 P 還在 DRAFT 但 user 想直接跑 /create-detailed-outline

依 B.7 啟動條件「P 至少 REVIEW」 — Wave 7 B.6 skill 與 Wave 8 B.7 skill 都有啟動前檢查機制：

- /create-detailed-outline 啟動時會驗 P status
- P 仍是 DRAFT 時 skill 應拒絕並提示「請先跑 B.6.5 主線 REVIEW gate」
- user 不應 bypass 此檢查；強制跑會違反 Phase B 設計紀律

## 2.6 下一步（B.6.5 PASS 後 → Wave 8）

Wave 7 結束 → Wave 8 啟動三條 task：

1. **B.7 /create-detailed-outline skill 跑**（user 在 Instance 跑；CODEX agent 跑 5 階段）— 需第七輪 master 寫 `CODEX_B7_STARTER.md`（後續交付）
2. **B.8 Phase B REVIEW gate**（人類；同 A.10 / B.5.5 / B.6.5 模式）— 需第七輪 master 寫 `CODEX_B8_REVIEW_GATE_STARTER.md` + `phase_b_review_log.md` 骨架
3. **B.9 Phase B 整體驗收**（CODEX 跑；同 A.11 模式）— 需第七輪 master 寫 `CODEX_B9_STARTER.md` + 升 `PHASE_B_COMPLETION_REPORT.md`

完成 Wave 8 → Milestone 2 達成 → 寫 `HANDOFF_TO_8TH_MASTER.md` 接 Phase C。

---

# 3. Cross-ref

- `_design/TASKS.md` v1.9 §B.6.5（B.6.5 人類 REVIEW gate 規範權威）
- `_design/TASKS.md` v1.9 