狀態：DRAFT  
版本：v0.4（8th master Cleanup round R7-MA-03 — 性質 / 身份與職責 / 不變範圍 段同步對齊 D-052 雙模式 active wording；v0.3 §1 步驟 0 雙模式 prompt 維持）  
最後更新：2026-05-21  
適用範圍：Phase B Wave 7 B.5.5 task 啟動包 — 角色（C-\*）人類 REVIEW gate  
優先級：高

# CODEX_B55_REVIEW_GATE_STARTER — Phase B Wave 7 B.5.5：角色 REVIEW gate

# 0. 本檔用途

> **v0.1 → v0.2 D-052 supersede 註記（2026-05-20）：**
>
> 既有 v0.1 採 manual-only flow（user 親身編輯 frontmatter + review_log）— M2 testing 期間觀察到 friction（user 易誤覆蓋整檔 / 累積編輯時間 ~5-10 分鐘 per gate）。
>
> **D-052（DECISIONS_LOG v1.8 §6.15.2）拍板：** partial supersede TASKS §B.5.5「禁止 CODEX 自行升 status」段加 user 明示拍板後 AI-execute exception。
>
> **本 starter v0.2 加雙模式流程：**
> - **方案 A（D-052 後預設）：AI-assisted upgrade** — user 明示拍板「同意升 + 拍板理由」後，AI 代為執行 mechanical edits（frontmatter + review_log §1 entry 寫入）+ 跑 /status verify + 給 user 看 git diff
> - **方案 B（manual fallback）：** user 親身編輯 — 沿用 v0.1 流程
>
> Accountability：兩方案的「user 明示拍板」是 accountability anchor；review_log §1.1 紀錄 user 拍板原話 + email + 時間戳。

Wave 7 第二條 task — **B.5.5 角色（C-\*）人類 REVIEW gate**，對齊 TASKS v1.9 §B.5.5。

**性質：人類拍板 REVIEW gate**（同 A.10 模式）— 不是 CODEX implement task。CODEX 印 C-\* 狀態清單供 user 人工檢視；**升級 frontmatter 動作走 D-052 雙模式 — 預設方案 A AI-assisted（user 明示拍板「同意升 N 個檔 REVIEW + 拍板理由」後 agent 代執行 mechanical edits）；方案 B manual 為 fallback**。

**前置條件：** Wave 7 B.5 DONE（/create-character skill 已實作 + 5 階段可跑）；user 已在 Instance repo 跑 `/create-character` 建立**至少 2 個 C-\* 角色**（為 B.5b /create-relationship 啟動條件兩 C-\* REVIEW 鋪路）。

**B.5.5 PASS → Wave 7 可進 B.5b /create-relationship → B.6 /create-outline → B.6.5。**

⚠ **本 task 不在 Template repo 跑**（Template 沒有 C-\* 實體）— **user 必須在 Instance repo 內跑**（即 `git clone` Template → 刪 `.template_root` → 跑 /init-project / /create-world → 跑 /create-character ≥ 2 次 → 跑本 gate）。

⚠ **三大紀律（依 TASKS §B.5.5）：**

- CODEX **不得「自行」升級任何 C-\* 狀態** — 「自行」精細化（D-052 後）：CODEX 未經 user 明示拍板不得擅自升級；但 user 明示拍板「同意升 + 拍板理由」後可代為執行 mechanical edits（方案 A AI-assisted）
- 不得直接跳到 B.5b（要先過此 gate）
- user 拍板「全升」/「選升」/「保留 DRAFT」均屬合法選項，CODEX 依 user 拍板執行（方案 A）或 user 親手編輯（方案 B fallback）

---

# 1. 啟動 prompt（user 在 Instance repo 內複製整段到 agent 對話）

```
你是 game-dialogue-bible 專案 Instance 的 agent（Claude Code CLI / Codex CLI / Codex App / Cowork 任一環境）。

本輪是「Phase B Wave 7 B.5.5 task」— 角色（C-*）人類 REVIEW gate，對齊 TASKS v1.9 §B.5.5。

工作資料夾：<instance_root>（user 親跑時自填，例：D:\my-novel-instance）

**你的身份與職責：**

- 你是 review gate facilitator — 本輪印 C-* 狀態清單 + 提示 user 拍板升 REVIEW（D-052 雙模式：預設 AI-assisted / manual fallback）+ 引導升級紀錄寫入 _design/phase_b_character_review_log.md
- 對應傳統：Wave 7 第二條 task；B.5.5 PASS → 可進 B.5b 建立關係實體

**重要邊界（嚴格 scope；依 TASKS §B.5.5 三大禁止項）：**

- ✗ 不得自行升級任何 C-* 檔的 status（frontmatter 編輯由 user 親跑或 user 拍板後執行）
- ✗ 不得直接跳到 B.5b /create-relationship（要先過此 gate）
- ✗ 不得改任何 R-* / P / CH-* / W-* / V-* / 其他實體檔
- ✗ 不得改 protocol / spec / skill 任何檔
- ✗ 不得跑真實 /create-character / /create-relationship 寫檔（屬另一輪 user 操作）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §B.5.5（D-052 partial supersede 後）：

1. **印 C-* 清單供 user 人工檢視**
2. **提示啟動條件 + 升級操作指引**
3. **依 D-052 雙模式之一執行升級**：
   - **方案 A（預設）：AI-assisted upgrade** — user 明示拍板後 agent 執行 mechanical edits
   - **方案 B（fallback）：manual upgrade** — user 親身編輯

### 步驟 0：D-052 雙模式選擇（TASKS v1.9 後預設）

印完步驟 1 清單後 + 印步驟 2 提示後，問 user：

```
[D-052 雙模式選擇]

預設走方案 A（AI-assisted）：你給我「同意升 [N 個檔] REVIEW + 拍板理由：[一句話]」，我代執行：
  - 對 N 個檔 frontmatter「狀態：DRAFT」→「狀態：REVIEW」+「最後更新」→ 今天
  - patch _design/phase_b_character_review_log.md §1 entry（精確邊界 — 不全檔覆蓋）
  - 跑 /status verify
  - 給你 git diff 看

或回「我自己手動改」走方案 B（manual fallback；走後續步驟 1-3）。
```

依 user 明示回應決定走方案 A 或方案 B。

**方案 A 執行紀律：**
- AI 執行的 frontmatter edit 限定為 status 第 1 欄 + 最後更新第 3 欄 — 不動 entities/depends_on/weight/版本/適用範圍/優先級/body
- AI 執行的 review_log §1 patch 必須採「精確邊界 patch」— 找「# 1. B.5.5 第一輪 — [...]」標題 + 替換到第一個 `---` 之前；不全檔覆蓋
- §1.1 拍板背景必含 user 明示拍板原文 + email + 時間戳
- 完成後 git diff 完整給 user 看 — user 確認才算 PASS

**方案 B 走以下步驟 1-3（原 manual flow）：**

### 步驟 1：印 C-* 清單

跑以下命令找出所有 entities: [C-*] 的檔，列出 path / status / version / entities：

```bash
# 找所有 frontmatter 含 entities: [C-*] 的檔
grep -lE "^entities:\s*\[C-" 03_characters/**/*.md 2>/dev/null | sort
```

對每個檔，print 以下 4 個欄位（從 frontmatter 抓）：

| 路徑 | status | version | entities |
|---|---|---|---|
| `03_characters/main/<name1>.md` | DRAFT / REVIEW | v0.1 | `[C-<name1>]` |
| `03_characters/main/<name2>.md` | DRAFT / REVIEW | v0.1 | `[C-<name2>]` |
| ... | ... | ... | ... |

也可用 build_repo_index：

```python
from scripts.parse_frontmatter import build_repo_index
result = build_repo_index('.')
c_entities = [e for e in result.entities if e.entity_id.startswith('C-')]
for e in c_entities:
    print(f"{e.path}  |  {e.status}  |  {e.version}  |  {e.entity_id}")
```

### 步驟 2：印提示文案（一字不漏給 user）

```
[B.5.5 角色 REVIEW gate 提示]

依 TASKS v1.9 §B.5.5 + §B.5b 啟動條件：

  /create-relationship 需要兩個 C-* 都至少 REVIEW；
  請手動把要建立關係的兩角色 frontmatter 狀態升 REVIEW。

升級動作（user 親跑）：
  1. 開啟對應 C-* 檔（例：03_characters/main/<name1>.md）
  2. 把中文 5 欄 header 第 1 欄「狀態：DRAFT」改為「狀態：REVIEW」
  3. 把第 3 欄「最後更新」改為今天日期（YYYY-MM-DD）
  4. 版本欄不升（內容未改，只是 status 升）
  5. YAML block entities / depends_on / weight 不動
  6. body 內容不動
  7. 對第二個 C-* 重複步驟 1-6

升完 ≥ 2 個 C-* 後：
  8. 開啟 _design/phase_b_character_review_log.md
  9. 在 §1 填入 1.1 拍板背景 / 1.2 升級檔案 list / 1.3 執行細節 / 1.4 B.5b 啟動條件對應
  10. （可選）§2 列未升 REVIEW 的 DRAFT C-*

不要直接跳到 /create-relationship — 先把上述完成。
```

### 步驟 3：等 user 回報

user 完成升級後會回報「已升完 C-<name1> + C-<name2> + 寫好 phase_b_character_review_log.md」。

agent 此時應：

1. 再跑步驟 1 的 grep / build_repo_index 驗證至少 2 個 C-* status == REVIEW
2. 讀 _design/phase_b_character_review_log.md 驗證 §1 已填（不再是 placeholder）
3. 回報「B.5.5 PASS — 可進 B.5b /create-relationship」

### 不變範圍（嚴格）

- 不改 LOCKED spec / registry / parser code
- 不改既有 27 模板 / 00_protocol/ 任何檔
- 不改 .claude/skills/*/SKILL.md 任何檔
- 不擅自升任何檔狀態（未經 user 明示拍板）；user 明示拍板後可走方案 A AI-assisted 代執行 mechanical edits（限 status + 最後更新欄，不動 body / entities / depends_on / weight / 版本）
- 不跑真實 /create-relationship 寫檔

### 完成判定

✓ ≥ 2 個 C-* status == REVIEW
✓ _design/phase_b_character_review_log.md §1 已 user 親填（拍板背景 + 升級 list + 執行細節 + B.5b 啟動條件對應）
✓ user 拍板「B.5.5 PASS — 可進 B.5b」

請依上述步驟跑。
```

---

# 2. 對 user 的補充說明（不在 agent prompt 內）

## 2.1 為什麼 B.5.5 是人類 gate

- C-\* 是長期創作資產：聲線 / 偏移 / 合規 / 動機 / 弧線等屬「對劇本世界的承諾」— 升 REVIEW 等於正式承認此角色定稿基線
- AI 無法替 user 拍板「這角色我想清楚了」 — 必須人類拍板
- 對齊 SPEC §5.3 完成度公式：DRAFT 25 → REVIEW 75 — REVIEW 表「絕大部分內容定稿；剩 LOCKED 才 100」

## 2.2 升 REVIEW 後可以做什麼

- 跑 `/create-relationship <name1> <name2>` 建 R-\<name1\>-\<name2\> 實體
- 跑 `/iterate-character <name>` 對 REVIEW C-\* 做有監督迭代（Phase C `/iterate-*` skill 實作後）
- 跑 `/view-character <name>` 看整合視圖（Phase D `/view-*` skill 實作後）

## 2.3 多角色狀況

如果 Instance 已建 3+ 個 C-\*（例：主角 + 反派 + 重要配角）：

- 可一輪 B.5.5 全升 3+ 個 C-\* REVIEW（一次 entry）
- 也可分輪升（第一輪先升主角 + 反派為 /create-relationship 主反派鋪路；第二輪後續升配角）
- 兩種模式均合法 — 依 user 創作節奏

每輪追加 phase_b_character_review_log.md 新 § entry（同 §3 跨輪追加紀律）。

## 2.4 如果只想升 1 個 C-\*（不到 B.5b 啟動條件）

依 TASKS §B.5b 啟動條件「兩個 C-\* 都至少 REVIEW」— 升 1 個不夠跑 /create-relationship。但 user 仍可：

- 升 1 個 C-\* REVIEW 也合法（寫 §1 entry 紀錄；§1.4 B.5b 啟動條件對應段標「未達成 — 仍欠 1 個 REVIEW」）
- 之後再升第 2 個時追加 §2 entry，標「B.5b 啟動條件達成」
- B.5.5 gate 整體 PASS 條件是「≥ 2 個 C-\* REVIEW」 — 不滿足時 master 對話應引導 user 回去再升 1 個 / 多建 1 個 C-\* 再升

## 2.5 B.5.5 與 A.10 的差異

| 維度 | A.10（Phase A） | B.5.5（Phase B Wave 7）|
|---|---|---|
| 升的對象 | Template 內既有 W/V 模板檔 | Instance 內 user 創建的 C-\* 實體檔 |
| 跑的地點 | Template repo（即此 D:\劇本開發工具）| Instance repo（user 自己的專案目錄）|
| 升的數量 | 4 檔（W-rules / W-language / V × 2）| ≥ 2 個 C-\*（為 B.5b 鋪路）|
| 對齊 Phase 啟動條件 | Phase B 啟動條件 W/V REVIEW | B.5b /create-relationship 啟動條件 |
| 紀錄檔 | `_design/phase_a_review_log.md` | `_design/phase_b_character_review_log.md` |

## 2.6 下一步（B.5.5 PASS 後）

1. user 跑 `/create-relationship <name1> <name2>` 建 R-\<name1\>-\<name2\>（B.5b skill 已實作 by Wave 7）
2. user 跑 `/create-outline` 建主線 P（B.6 skill 已實作 by Wave 7）
3. user 跑 B.6.5 主線 REVIEW gate（同 B.5.5 模式；屆時 master 第七輪會印 B.6.5 starter）
4. 然後進 Wave 8 — B.7 /create-deta