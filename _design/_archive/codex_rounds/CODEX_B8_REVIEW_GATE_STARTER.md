狀態：DRAFT  
版本：v0.5（8th master Cleanup round R7-MA-03 — 性質 / 身份與職責 / 不變範圍 段同步對齊 D-052 雙模式 active wording；v0.4 §1 步驟 0 雙模式 prompt 維持）  
最後更新：2026-05-21  
適用範圍：Phase B Wave 8 B.8 task 啟動包 — Phase B 整體人類 REVIEW gate  
優先級：高

# CODEX_B8_REVIEW_GATE_STARTER — Phase B Wave 8 B.8：Phase B 整體 REVIEW gate

# 0. 本檔用途

> **v0.1 → v0.2 D-050 對齊 patch 紀錄（2026-05-20）：**
>
> v0.1 寫作時 DECISIONS_LOG 為 v1.4（未含 D-050）；§1 步驟 1 註解「CH-\* 章節實體（含 05_b / 05_c / 05_d / 05_e）」 — 依 D-050 子裁決 2 patch 後 supersede：
> - **CH-\* entities 在 D-050 後僅由 /create-detailed-outline 寫於 `05_b_章節結構模板.md`**（屬 CH skill scope）
> - `05_c / 05_d / 05_e` 屬 **P /create-outline** 議題 4/5 觸發的高層 placeholder（不含 CH-\* entities）— B.6 PASS 後可能 status 升 REVIEW，但 frontmatter `entities` 應為 `[P]` 非 `[CH-*]`
> - B.8 review gate 印 CH-\* entities 時應主要 grep `05_plot/05_b_*.md`；`05_c/d/e` 屬 P entity 寫檔範圍，應在 P 那段審
>
> 對應 git commit：`27e78b1`（Wave 7 patch round）/ `da305a5`（Round 2 PASS）/ `399a526`（B.7 SKILL.md D-050 對齊）。

> **v0.2 → v0.3 D-052 supersede 註記（2026-05-20）：**
>
> 既有 v0.2 採 manual-only flow — M2 testing 期間累積 user friction（特別是 B.8 要升 4 個檔 + 寫 phase_b_review_log §1 entry 含 5 個 §1.2.X 子段，markdown 複雜度最高 → user error 風險最大；user 已在 B.5.5 階段碰過整檔覆蓋 error）。
>
> **D-052（DECISIONS_LOG v1.8 §6.15.2）拍板：** partial supersede TASKS §B.8「禁止 CODEX 自行升 status」段加 user 明示拍板後 AI-execute exception。
>
> **本 starter v0.3 加雙模式流程：**
> - **方案 A（D-052 後預設）：AI-assisted upgrade** — user 明示拍板「同意升 N 個檔 + 拍板理由」後，AI 代為執行 mechanical edits（5 類實體 frontmatter + phase_b_review_log §1 entry 寫入；5 個 §1.2.X 子段都涵蓋）+ 跑 /status verify
> - **方案 B（manual fallback）：** user 親身編輯 — 沿用 v0.2 流程

Wave 8 第二條 task — **B.8 Phase B 整體（C-\* / R-\*-\* / P / CH-\* / S-\*-\*）人類 REVIEW gate**，對齊 TASKS v1.9 §B.8（D-052 後）。

**性質：人類拍板 REVIEW gate**（同 A.10 / B.5.5 / B.6.5 模式）— 不是 CODEX implement task。CODEX 印 5 類實體狀態清單供 user 人工檢視；**升級 frontmatter 動作走 D-052 雙模式 — 預設方案 A AI-assisted（user 明示拍板「同意升 N 個檔 + 拍板理由」後 agent 代執行 mechanical edits 含 5 個 §1.2.X 子段全填）；方案 B manual 為 fallback（B.8 markdown 複雜度最高，強烈推薦方案 A）**。

**前置條件：**
- Wave 8 B.7 DONE（/create-detailed-outline skill 已實作 + 5 階段可跑）
- user 已在 Instance repo 跑完全套 Phase B 上游 chain：
  - B.5（/create-character）≥ 2 次（建至少 2 個 C-\*）
  - B.5.5（C-\* review gate；升 ≥ 2 個 C-\* REVIEW）
  - B.5b（/create-relationship）建立 R-\*-\*
  - B.6（/create-outline）建立 P
  - B.6.5（P review gate；升 P REVIEW）
  - B.7（/create-detailed-outline）建立 CH-\* + S-\*-\*

**B.8 PASS → Wave 8 可進 B.9 Phase B 整體驗收 + 升 PHASE_B_COMPLETION_REPORT.md → Milestone 2 達成。**

⚠ **本 task 不在 Template repo 跑**（Template 沒有 C-\* / R-\*-\* / CH-\* / S-\*-\* 實體）— **user 必須在 Instance repo 內跑**。

⚠ **三大紀律（依 TASKS §B.8）：**

- CODEX **不得「自行」升級任何檔案狀態** — 「自行」精細化（D-052 後）：CODEX 未經 user 明示拍板不得擅自升級；但 user 明示拍板「同意升 N 個檔 + 拍板理由」後可代為執行 mechanical edits（方案 A AI-assisted；5 類實體 frontmatter + phase_b_review_log §1 entry 5 個 §1.2.X 子段全填）
- 必須涵蓋全部 5 類實體（C-\* / R-\*-\* / P / CH-\* / S-\*-\*）— Phase D 整體驗收要求 S-\*-\* 也 ≥ REVIEW
- user 拍板「全升」/「選升」/「明示保留 DRAFT」均屬合法選項；保留 DRAFT 需在 review_log §2 明示理由；執行方式採方案 A（AI-assisted）或方案 B（manual fallback）

⚠ **新慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only concrete path 引用前加 `<instance_root>/` 前綴

---

# 1. 啟動 prompt（user 在 Instance repo 內複製整段到 agent 對話）

~~~
你是 game-dialogue-bible 專案 Instance 的 agent（Claude Code CLI / Codex CLI / Codex App / Cowork 任一環境）。

本輪是「Phase B Wave 8 B.8 task」— Phase B 整體（C-* / R-*-* / P / CH-* / S-*-*）人類 REVIEW gate，對齊 TASKS v1.9 §B.8。

工作資料夾：<instance_root>（user 親跑時自填）

**你的身份與職責：**

- 你是 review gate facilitator — 本輪印 5 類實體狀態清單 + 提示 user 拍板升 REVIEW（D-052 雙模式：預設 AI-assisted / manual fallback；B.8 強烈推薦 AI-assisted）+ 引導升級紀錄寫入 _design/phase_b_review_log.md
- 對應傳統：Wave 8 第二條 task；B.8 PASS → 可進 B.9 Phase B 整體驗收

**重要邊界（嚴格 scope；依 TASKS §B.8 三大禁止項）：**

- ✗ 不得自行升級任何檔的 status（frontmatter 編輯由 user 親跑或 user 拍板後執行）
- ✗ 不得直接跳到 B.9 Phase B 整體驗收（要先過此 gate）
- ✗ 不得改任何 W-* / V-* 已 REVIEW 檔（A.10 已升；本輪不重複動）
- ✗ 不得改 protocol / spec / skill 任何檔
- ✗ 不得跑真實 /create-* / /iterate-* / /scene-task 寫檔（屬另一輪 user 操作）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.8（D-052 partial supersede 後）：

1. **印 5 類實體狀態清單供 user 人工檢視**
2. **提示啟動條件 + 升級操作指引**
3. **依 D-052 雙模式之一執行升級**：
   - **方案 A（預設）：AI-assisted upgrade** — user 明示拍板後 agent 執行 mechanical edits（多檔 frontmatter + review_log §1 entry 含 5 個 §1.2.X 子段）
   - **方案 B（fallback）：manual upgrade**

### 步驟 0：D-052 雙模式選擇（TASKS v1.9 後預設 — B.8 markdown 複雜度最高 → AI-assisted 最省力）

印完步驟 1 清單後 + 印步驟 2 提示後，問 user：

```
[D-052 雙模式選擇 — B.8 強烈推薦走方案 A]

預設走方案 A（AI-assisted）：你給我「同意升 [N 個檔 / 列哪些] REVIEW + 拍板理由：[一句話]」，我代執行：
  - 對 N 個目標檔 frontmatter「狀態：DRAFT」→「狀態：REVIEW」+「最後更新」→ 今天（涵蓋 C-* 配角 / R-*-* / CH-* / S-*-* — B.5.5/B.6.5 已升的不重複）
  - patch _design/phase_b_review_log.md §1 entry（精確邊界 — 不全檔覆蓋；5 個 §1.2.X 子段全填）
  - 跑 /status verify
  - 給你 git diff 看

或回「我自己手動改」走方案 B（manual fallback；走後續步驟 1-3 — 但 B.8 markdown 複雜度高 / user error 風險最大）。
```

依 user 明示回應決定走方案 A 或方案 B。**強烈推薦方案 A**（B.8 是 4 gate 中 markdown 最複雜的；M2 testing 期間 user 已在 B.5.5 階段碰過整檔覆蓋 error）。

**方案 A 執行紀律：** 同 B.5.5 starter 步驟 0「方案 A 執行紀律」 + 額外要求：
- 5 個 §1.2.X 子段（C-\* / R-\*-\* / P 維持 / CH-\* / S-\*-\*）都要寫；空子段標「無新增」
- §2 未升 REVIEW 的 DRAFT 段若 user 拍板「全升」則填「無」；若選升則紀錄保留理由
- §1.4 Phase C/D 啟動條件對應段必驗 W/V/C/R/P/CH/S 全 ≥ REVIEW

**方案 B 走以下步驟 1-3（原 manual flow）：**

### 步驟 1：印 5 類實體狀態清單

跑 5 個 grep / build_repo_index 命令找出所有 5 類實體 frontmatter 並列出 path / status / version / entities。

```bash
# C-* 角色實體
echo "=== C-* 角色實體 ==="
grep -lE "^entities:\s*\[C-" 03_characters/**/*.md 2>/dev/null | sort

# R-*-* 關係實體
echo "=== R-*-* 關係實體 ==="
grep -lE "^entities:\s*\[R-" 04_relationships/*.md 2>/dev/null | sort

# P 主線實體
echo "=== P 主線實體 ==="
grep -lE "^entities:\s*\[P\]" 05_plot/*.md 2>/dev/null | sort

# CH-* 章節實體（D-050 子裁決 2 後 CH 行限定 05_b；05_c/05_d/05_e 屬 P-scope 高層 placeholder 不歸 CH grep）
echo "=== CH-* 章節實體 ==="
grep -lE "^entities:\s*\[CH-" 05_plot/*.md 2>/dev/null | sort

# S-*-* 場景索引實體
echo "=== S-*-* 場景索引實體 ==="
grep -lE "^entities:\s*\[S-" 06_scene_index/*.md 2>/dev/null | sort
```

對每類實體列以下 4 欄表格（從 frontmatter 抓 status / version）：

| 類別 | 路徑 | status | version | entities |
|---|---|---|---|---|
| C-* | 03_characters/main/<name1>.md | DRAFT / REVIEW | v0.1 | [C-<name1>] |
| ... | ... | ... | ... | ... |

也可用 build_repo_index：

```python
from scripts.parse_frontmatter import build_repo_index
result = build_repo_index('.')

# 5 類實體分群
c_entities  = [e for e in result.entities if e.entity_id.startswith('C-')]
r_entities  = [e for e in result.entities if e.entity_id.startswith('R-')]
p_entities  = [e for e in result.entities if e.entity_id == 'P']
ch_entities = [e for e in result.entities if e.entity_id.startswith('CH-')]
s_entities  = [e for e in result.entities if e.entity_id.startswith('S-')]

for label, group in [('C-*', c_entities), ('R-*-*', r_entities), ('P', p_entities), ('CH-*', ch_entities), ('S-*-*', s_entities)]:
    print(f"=== {label} ===")
    for e in group:
        print(f"  {e.path}  |  {e.status}  |  {e.version}  |  {e.entity_id}")
```

**啟動條件檢查：**

如果任一類實體 grep 出 0 個 — 表示 user 還沒跑對應 skill；agent 應拒絕本 gate 並提示對應上游：
- C-* 0 個 → 拒絕；提示先跑 /create-character ≥ 2 次 + B.5.5
- R-*-* 0 個 → 拒絕；提示先跑 /create-relationship + B.5.5
- P 0 個 → 拒絕；提示先跑 /create-outline + B.6.5
- CH-* 或 S-*-* 0 個 → 拒絕；提示先跑 /create-detailed-outline

如果 P 還在 DRAFT — 不阻 B.8 起手（B.5.5 / B.6.5 都該已過），但 §1.4 啟動條件對應段需明示「P 仍 DRAFT；本輪 B.8 順便升 REVIEW」。

### 步驟 2：印提示文案（一字不漏給 user）

```
[B.8 Phase B 整體 REVIEW gate 提示]

依 TASKS v1.9 §B.8 + Phase C / Phase D 啟動條件：

  Phase C /scene-task + /dialogue-write 需要 W/V/C/R/P/CH 全 ≥ REVIEW；
  Phase D 整體驗收（D.7）再加 S-*-* ≥ REVIEW；
  請人類審完所有 5 類實體後手動升 REVIEW。

審查重點建議（user 親審；非 strict 清單）：
  C-* 角色：聲線 / 偏移 / 合規 / 動機 / 弧線
  R-*-* 關係：本質 / 起點 / 關鍵節點 / 終態
  P 主線：起承轉合 / 主題承載 / 結局基線（B.6.5 已審；本輪維持）
  CH-* 章節：各章節主題 / 角色出場 / 資訊揭露密度 / 伏筆配置
  S-*-* 場景索引：場景目的 / 角色 / 衝突焦點 / 資訊揭露點 / 連接前後場景

升級動作（user 親跑）：對每個目標檔：
  1. 開啟對應 .md 檔
  2. 把中文 5 欄 header 第 1 欄「狀態：DRAFT」改為「狀態：REVIEW」
  3. 把第 3 欄「最後更新」改為今天日期（YYYY-MM-DD）
  4. 版本欄不升（內容未改，只是 status 升）
  5. YAML block entities / depends_on / weight 不動
  6. body 內容不動

升完後：
  7. 開啟 _design/phase_b_review_log.md
  8. 在 §1 填入 1.1 拍板背景 / 1.2.1~1.2.5 5 類實體升級 list / 1.3 執行細節 / 1.4 Phase C/D 啟動條件對應
  9. （可選）§2 列未升 REVIEW 的 DRAFT 實體 + 保留理由

不要直接跳到 B.9 Phase B 整體驗收 — 先把上述完成。

如果審查時發現某類實體需要回去迭代：
  - 該類保留 DRAFT 不升
  - 回去跑對應 /iterate-* skill（Phase C 屆時實作）
  - 或手動編輯後再回來跑 B.8
  - §2 「未升 REVIEW 的 DRAFT 檔」段落明示保留理由
  - Phase D 整體驗收（D.7）屆時會卡未升 REVIEW 的實體；保留 DRAFT 需在 Phase D 前處理
```

### 步驟 3：等 user 回報

user 完成升級後會回報「已升完 N 個 C-* + M 個 R-* + P 維持 + K 個 CH-* + L 個 S-* + 寫好 phase_b_review_log.md」。

agent 此時應：

1. 重跑步驟 1 的 grep / build_repo_index 驗證 5 類實體 status 對齊 user 回報
2. 讀 _design/phase_b_review_log.md 驗證 §1 已填（5 個 §1.2.X 子段不再是 placeholder）
3. 統計：
   - W/V/C/R/P/CH 是否全 ≥ REVIEW（Phase C 啟動條件）
   - S-*-* 是否全 ≥ REVIEW（Phase D 整體驗收條件）
   - 若 user 在 §2 明示保留某些 DRAFT — 確認該保留不影響 Phase C 啟動（C-* / R-*-* / P / CH-* 必須全 REVIEW；S-*-* 在 Phase C 階段可仍有 DRAFT 但 Phase D 前須升）
4. 回報「B.8 PASS — 可進 B.9 Phase B 整體驗收（依 CODEX_B9_STARTER）」

### 不變範圍（嚴格）

- 不改 LOCKED spec / registry / parser code
- 不改既有 27 模板 / 00_protocol/ 任何檔
- 不改 .claude/skills/*/SKILL.md 任何檔
- 不擅自升任何檔狀態（未經 user 明示拍板）；user 明示拍板後可走方案 A AI-assisted 代執行 mechanical edits（限 status + 最後更新欄，不動 body / entities / depends_on / weight / 版本）
- 不跑真實 /create-* / /iterate-* / /scene-task 寫檔

### 完成判定

✓ C-* / R-*-* / P / CH-* 全 ≥ REVIEW（含 B.5.5 / B.6.5 已升的；本輪不重複動）
✓ S-*-* 至少全 ≥ REVIEW（Phase D 整體驗收要求）— 若保留 DRAFT 必須在 review_log §2 明示理由
✓ _design/phase_b_review_log.md §1 已 user 親填（5 個 §1.2.X 子段全填 + 拍板背景 + 執行細節 + Phase C/D 啟動條件對應）
✓ user 拍板「B.8 PASS — 可進 B.9」

請依上述步驟跑。
~~~

---

# 2. 對 user 的補充說明（不在 agent prompt 內）

## 2.1 為什麼 B.8 是整體 gate（B.5.5 / B.6.5 各自 gate 還不夠）

- B.5.5 只升 ≥ 2 個 C-\*（為 /create-relationship 鋪路；剩餘配角 + R-\* + CH-\* + S-\* 不在 scope）
- B.6.5 只升 P（為 /create-detailed-outline 鋪路；C-\* 配角 + R-\* + CH-\* + S-\* 不在 scope）
- B.8 是 Phase B 收尾的「全套整體 review」 — 把 B.5.5 / B.6.5 後剩餘的 + B.7 新建的 CH-\* / S-\*-\* 一次審完
- 對齊 Phase C / Phase D 啟動條件 — Phase C 需 W/V/C/R/P/CH 全 ≥ REVIEW；Phase D 再加 S-\*-\* ≥ REVIEW

## 2.2 5 類實體的審查順序建議

雖然 step 1 步驟同時印 5 類，user 審查時建議**由淺至深**：

1. **先審 S-\*-\* 場景索引**（最 granular；場景目的 / 衝突 / 揭露點明確比較容易判斷）
2. **再審 CH-\* 章節**（場景審完後章節整體節奏才看得清）
3. **再審 R-\*-\* 關係**（主反派 + 副線關係審查；對應 4 議題）
4. **再審剩餘 C-\* 角色**（配角 / NPC；B.5.5 已審的主角不重複動）
5. **最後維持 P**（B.6.5 已審 + B.7 拆完細綱後若仍滿意 P 維持 REVIEW）

倒序審理由：場景索引最具體；具體決定抽象 — 場景 OK 表章節 OK；章節 OK 表主線 OK。

## 2.3 如果 5 類實體有任一類「全 DRAFT」

對應上游 skill 還沒跑通；agent 應拒絕本 gate 並導向：

| 類別缺失 | user 動作 |
|---|---|
| C-\* 全 DRAFT 或 0 個 | 跑 /create-character ≥ 2 次 + B.5.5 |
| R-\*-\* 全 DRAFT 或 0 個 | 跑 /create-relationship（依賴 B.5.5 PASS）|
| P 全 DRAFT 或 0 個 | 跑 /create-outline + B.6.5 |
| CH-\* 全 DRAFT 或 0 個 | 跑 /create-detailed-outline（依賴 B.6.5 PASS）|
| S-\*-\* 全 DRAFT 或 0 個 | 跑 /create-detailed-outline 階段 4 應產出 |

## 2.4 B.8 跟 A.10 / B.5.5 / B.6.5 的差異

| 維度 | A.10 | B.5.5 | B.6.5 | **B.8** |
|---|---|---|---|---|
| Phase | Phase A 收尾 | Phase B 中段 | Phase B 中段 | **Phase B 收尾** |
| 升的對象 | W/V 模板 | C-\* 部分 | P