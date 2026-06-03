狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 13 task — /view-world skill + 中文 wrapper 實作（Wave 13 共通範本）  
優先級：高

# CODEX_D6_STARTER — Phase D Wave 13 D.6：/view-world skill 實作（Wave 13 共通範本）

# 0. 本檔用途

Phase D Wave 13 起手第一條 task — 實作 `/view-world` skill（純讀取 W-rules / V / W-language 整合視圖）。對齊 TASKS v1.9 §C.3（第 1 個 /view-* skill）+ ARCH v1.6 §4.1 動態組合 + §4.4 呈現規則（時期 C 整合 UX_SPEC §7）。

**前置條件：** 9th master Round 1-4 review cycle 收尾 + R4-MAJOR-01 hard-limit accept；Wave 12 starter set 全 v0.4（D5）/ v0.3（D1/D2/D3）/ v0.2（D4）+ 00_j v0.2。

**D.6 PASS → Wave 13 進 batch mode：** D7-D9（/view-character / /view-outline / /view-detailed-outline）採 CODEX batch starter 模式（不用 master 逐一寫；本 D6 是共通範本）。

**Wave 13 新工作模式（依 user 拍板）：**
- Master 寫 D6 完整 starter（本檔；提供完整 starter pattern + view-* 共通設計）
- Master 寫 CODEX_D_VIEW_BATCH_STARTER.md（依 D6 範本批次寫 D7-D9）
- CODEX 在乾淨對話跑 batch starter 寫 D7-D9 三個 SKILL.md
- Master review 四個 SKILL.md 一致性

⚠ **view vs export 邊界（關鍵差異）：**
- `/view-*` = **純讀取**；組合後**只印在 chat**；**不寫檔**
- `/export-*` = 與 view 邏輯相同，但寫 view/<entity>.md 整合檔（DERIVED 狀態）→ 屬 Wave 14 scope；本 skill **不寫 view/ 整合檔**
- ARCH §4.1 vs §4.2 對齊

⚠ **view-* 不需要 D-050 子裁決邊界三 block：** 純讀取 skill 不寫檔（除 phase_log audit entry）；邊界規範限「不寫 view/ 整合檔 / 不升 entity / 不擴 source / 不擅自呼叫其他 view-*」。

⚠ **「Fix one, find two」cascade pattern + 9th master Round 1-4 教訓全內化（HANDOFF 教訓內化 5 條）：**
- 寫 starter 含 spec 段引用前先 grep verify
- 寫 starter 含 path reference 前先 ls 實際 repo 對齊
- 寫 starter 涉及 SPEC frontmatter 段直接 grep SPEC §5.2 verify
- 寫 supersede note 避免重複 finding 內精確詞串
- 寫 review starter（if applicable）diff anchor 精確（用明示 commit hash 或 HEAD~1..HEAD）

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only path 前綴 `<instance_root>/`

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 13 D.6 task」— 實作 /view-world skill（含中文 wrapper）；對齊 TASKS v1.9 §C.3 + ARCH v1.6 §4.1 動態組合 + §4.4 呈現規則 + UX_SPEC §7。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase D Wave 13 第一條 task（D.6 → D.7/D.8/D.9 採 batch 模式）；/view-world 是 4 個 /view-* 系列共通範本
- D.6 PASS → 可進 Wave 13 batch（D.7-D.9 由 CODEX 跑 CODEX_D_VIEW_BATCH_STARTER 在另一個乾淨對話寫）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_j v0.2；本輪 view skill 不修改 protocol）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動既有 22 個 SKILL.md（init-project / status / check-gaps / create-* x5 + 5 中文 wrapper + scene-task / dialogue-write / qa + 3 中文 wrapper + iterate-* x6 / 5 中文 wrapper；後者 Wave 12 已寫但 SKILL.md 尚未實作 — 屬 CODEX D.1-D.5 task 範圍）
- ✗ **不**寫 /view-character（D.7 scope）/ /view-outline（D.8）/ /view-detailed-outline（D.9）
- ✗ **不**寫任何 view/<entity>.md 整合檔（屬 /export-* Wave 14 scope）
- ✗ **不**跑真實 /view-world（會印 chat output 但不污染 Template；Template 內無 Instance entity；本輪 implementer 只寫 SKILL.md 不執行）
- ✗ **不**修改 D-001~D-054 / NEW_REQ_15 / 任何 DECISIONS_LOG 拍板紀錄

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.3 + ARCH v1.6 §4.1 + §4.4 + UX_SPEC §7（如可訪問）。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/view-world/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/查看世界觀/SKILL.md` | 中文 wrapper |

### /view-world 主 SKILL.md 結構（11 段；vs /iterate-* / /create-* 差異：純讀取，不含邊界 D-050 三 block）

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；明示「讀取 W-rules / V / W-language + 02_vocabulary 組合視圖；不寫檔；對齊 ARCH §4.1」）
- 中文 5 必填 header（狀態：DRAFT / 版本：v0.1 / 最後更新：YYYY-MM-DD / 適用範圍：/view-world skill runtime instructions / 優先級：中）
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（`/view-world` + 中文 `/查看世界觀` reference）
  - `## 觸發協議`（無對應 00_protocol/ — view 是純技術 skill 無協議；對齊 ARCH §4.1 動態組合邏輯為權威）
  - `## 啟動前檢查`（D-049 Template-detect + Bootstrap completed + W-rules / V / W-language 至少 DRAFT 存在；不要求 ≥ REVIEW）
  - `## 流程`（5 階段：診斷 / 反查 source / 組合 / 呈現 / 驗證）
  - `## 呈現規則`（chat 動態組合**不加 breadcrumb**；不加 TOC（chat 無需）；每段尾加 source italic；跨檔 link `/` 開頭；單向 reference）
  - `## .protocol_version 寫入規範`（純讀取 skill 可選寫 phase_log audit entry；含 `read_sources` 清單 + `output_lines` 估算；不更新 entity 完成度）
  - `## 輸入`（無 user 參數）
  - `## 輸出`（chat Markdown 印；**不寫任何檔**；明示「若要持久化整合檔請用 /export-world」）
  - `## 邊界`（**純讀取邊界**：不寫檔 / 不寫 view/ 整合檔 / 不擴 source 範圍 / 不升 entity 狀態 / 不擅自呼叫其他 view-* / 不擅自重新組織 source 內容 — 只 verbatim 抽取）
  - `## 錯誤處理 / Rollback`（source 缺漏處理：印警示但仍盡量組合可讀視圖；某 source 完全不存在 → 印對應段「[source 缺漏]」placeholder + 提示用 /create-world 或 /iterate-world）
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### /view-world 差異規格

- **觸發語：** `/view-world`（不接 user 參數）
- **對應 protocol：** 無（view 屬純技術 skill；ARCH §4.1 為權威；無 00_protocol/ 對應）
- **議題清單動態載入：** **不適用**（view 是 read-only data assembly）
- **modify entity 範圍：** 無（純讀取；不修任何 entity）
- **依賴：** W-rules / V / W-language 至少 DRAFT 存在（不要求 ≥ REVIEW；view 是 read-any-state）
- **下游：** 階段 5 印「下一步建議：若要持久化整合檔請跑 /export-world；若要修改世界觀請跑 /iterate-world」；**不**自動 trigger 任何 skill

### 5 階段流程（適配 view；對齊 ARCH §4.1）

#### 階段 1：診斷（read-only diagnostic）

agent 開場：

> /view-world 將動態組合世界觀整合視圖（W-rules / V / W-language + 02_vocabulary 詞彙系統 + 00_b §1/§2 反 AI 味基線）。本 skill 純讀取，不寫任何檔。執行後在 chat 印出整合視圖。
> 
> 開始讀取 source...

agent 檢查啟動前條件（D-049 / Bootstrap / 目標 entity 至少 DRAFT 存在）；任何缺漏拒絕並印缺漏清單。

#### 階段 2：反查 source（依 ARCH §4.1 pseudocode）

agent 讀以下 source（依序）：

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `01_world/01_a_世界觀總覽.md` | W-rules 主分拆 | "## 世界規則" 段 |
| `01_world/01_b_世界語言規格.md` | W-language 主分拆 | "## 世界語言" 段 |
| `01_world/01_c_陣營與階級語言.md` | W-language 延伸 | "## 陣營與階級語言" 段 |
| `02_vocabulary/02_a_專有名詞表.md` | V 專有名詞 | "### 專有名詞" 子段 |
| `02_vocabulary/02_b_俗稱與黑話表.md` | V 俗稱黑話 | "### 俗稱與黑話" 子段 |
| `02_vocabulary/02_c_禁用詞與慎用詞表.md` | V 禁用詞 | "### 禁用詞與慎用詞" 子段 |
| `00_protocol/00_b_反ai味檢查表.md` §1/§2 | 作品專屬反 AI 味基線（W 對應段）| "## 反 AI 味基線（作品專屬）" 段 |

agent 對每個 source 讀取後：
- 解析 frontmatter（驗證 entity 對應）
- 抽取 main content（跳過 frontmatter + 中文 5 header）
- 標記抽取位置（line 起訖；給 audit 用）

#### 階段 3：組合（in-memory；不寫檔）

agent 把 source 組合成單一 Markdown 結構：

```markdown
# 世界觀 — /view-world 動態整合視圖

## 世界規則

<01_world/01_a 內容>

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md)*

## 世界語言

<01_world/01_b 內容>

*來源：[/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md)*

## 陣營與階級語言

<01_world/01_c 內容>

*來源：[/01_world/01_c_陣營與階級語言.md](/01_world/01_c_陣營與階級語言.md)*

## 詞彙系統

### 專有名詞
<02_a 內容>
*來源：[/02_vocabulary/02_a_專有名詞表.md](/02_vocabulary/02_a_專有名詞表.md)*

### 俗稱與黑話
<02_b 內容>
*來源：[/02_vocabulary/02_b_俗稱與黑話表.md](/02_vocabulary/02_b_俗稱與黑話表.md)*

### 禁用詞與慎用詞
<02_c 內容>
*來源：[/02_vocabulary/02_c_禁用詞與慎用詞表.md](/02_vocabulary/02_c_禁用詞與慎用詞表.md)*

## 反 AI 味基線（作品專屬）

<00_b §1 內容>
<00_b §2 內容>

*來源：[/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1 / §2*

---

**下一步建議：**
- 持久化整合檔 → /export-world
- 修改世界觀 → /iterate-world
- 補洞 → /iterate-world
```

#### 階段 4：呈現（chat 印；不寫檔）

agent 把組合結果直接印在 chat。

**呈現規則（對齊 ARCH §4.4）：**
- chat 動態組合**不加 breadcrumb**（breadcrumb 僅 /export-* 整合檔加；ARCH §4.4 line 833）
- chat 動態組合**不加 TOC**（chat 介面無需）
- 每段尾加 source italic 引用 `*來源：[/path](/path)*`
- 跨檔 link 一律以 project root 為基準（`/` 開頭）；同檔 anchor `#slug` 不加 `/`
- 單向 reference：本 skill 引用 source 時加連結；source 不必反向列
- chat 動態組合也加 source 引用（即使連結點不到，純文字仍提供定位線索）

#### 階段 5：驗證（read-only audit）

階段 5 純 audit：

- **不**自動 trigger /status（view 是 read-only；不影響實體狀態）
- 可選寫 `.protocol_version.phase_log` audit entry（含 `read_sources` 清單 + `output_lines` 估算）；若 user 跑 view-* 頻繁可設「audit log skip」flag 不寫
- 印「下一步建議」段

### .protocol_version phase_log entry 範例（可選寫）

```yaml
- phase: view-world
  date: YYYY-MM-DD
  skill: /view-world
  status: completed
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 00_protocol/00_b_反ai味檢查表.md  # §1/§2
  output_lines: <估算組合輸出行數>
  output_target: chat
  customizations: []
```

### 啟動前檢查（嚴格條件 — 沿用 D1 modes 但寬鬆）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在（屬 Instance）| 拒絕並提示用 /init-project |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕並提示用 /init-project |
| W-rules / V / W-language 存在 | 對應分拆檔存在 + frontmatter 含目標 entity；**狀態 ≥ DRAFT 即可**（不要求 ≥ REVIEW；view 屬 read-any-state）| 拒絕並印缺漏清單；提示用 /create-world |
| 不要求下游 pipeline 互鎖檢查 | view 是 read-only；不影響任何進行中 skill | — |

### 邊界區段（純讀取邊界；不含 D-050 子裁決三 block）

`/view-world` 是純讀取 skill。本 skill 嚴格限：

1. **不寫任何檔**（除可選 phase_log audit entry）
2. **不寫 view/ 整合檔**（屬 /export-world Wave 14 scope；本 skill 跟 export 邏輯相同但僅印 chat）
3. **不擴 source 範圍**（嚴格限上述 7 個 source；不擅自加 03_characters / 04_relationships 等屬其他 view-* scope）
4. **不升 entity 狀態**（view 屬 read-only；任何 W-rules / V / W-language 狀態升級需走 /iterate-world 或 /create-world）
5. **不擅自呼叫其他 view-***（user 要看角色視圖請手動跑 /view-character）
6. **不擅自重新組織 source 內容**（agent 只 verbatim 抽取 + 套組合結構；不改 wording / 不總結 / 不簡化）
7. **不寫 LOCKED 狀態**（view 不涉及 entity 狀態變動）

**vs Phase B/C 寫檔 skill 的差異：** /create-* / /iterate-* / /scene-task / /dialogue-write / /qa 含 D-050 子裁決三 block（D-050 子裁決 1 禁寫 00_protocol + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表）；本 skill 純讀取**不含**該三 block，但用「純讀取邊界 7 條」對應規範。

### 中文 wrapper SKILL.md 結構（查看世界觀）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 查看世界觀
description: "/view-world skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/view-world skill 中文觸發 wrapper  
優先級：中

# /查看世界觀（/view-world wrapper）

本 wrapper 是 `/view-world` 的中文別名。執行時以英文主檔 `.claude/skills/view-world/SKILL.md` 為權威。

請參考 `.claude/skills/view-world/SKILL.md`。
```

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：
   - `_design/TASKS.md` v1.9 §C.3（4 個 /view-* skill task spec）
   - `_design/ARCHITECTURE.md` v1.6 §4.1（/view-* 動態組合）+ §4.4（呈現規則）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema — read 對齊）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則 — 跨檔 link / source 引用 / 單向 reference）
   - `.claude/skills/status/SKILL.md` v0.1 / `.claude/skills/check-gaps/SKILL.md` v0.1（既有 read-only skill 範例；不寫檔 pattern 參考）
   - `_design/DECISIONS_LOG.md` v2.0 §6.X（如有 view 相關拍板）

2. **寫 SKILL.md 2 個**：
   - 英文主檔 `.claude/skills/view-world/SKILL.md`（依本 starter §1 「主 SKILL.md 結構」+ 「差異規格」+ 「5 階段流程」+ 「邊界區段」）
   - 中文 wrapper `.claude/skills/查看世界觀/SKILL.md`（依本 starter §1 「中文 wrapper SKILL.md 結構」）

3. **跑 baseline 驗證**：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - `python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; ..."`
   - 對齊 9th master Round 1-4 收尾後 baseline（check_paths ≤ 247 ERROR；hard-limit accept R2-MAJOR-03）

4. **不跑真實 /view-world 寫檔**（Template repo 內無 Instance entity；本輪 implementer 只寫 SKILL.md 不執行）

---

# 3. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index baseline | 對齊 9th master Round 1-4 收尾後 baseline；無新 ERROR；check_paths ≤ 247 |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 5 階段流程 + 呈現規則 | SKILL.md 含 5 階段對齊 ARCH §4.1 pseudocode + 呈現規則對齊 §4.4 | 完整 |
| 4. 純讀取邊界 7 條 | SKILL.md 含「邊界區段（純讀取邊界）」7 條完整 | 與 D1 D-050 三 block 模式不同 — view 用純讀取邊界 |
| 5. phase_log entry 規範（audit）| SKILL.md 含 phase_log entry 範例（可選寫；含 `read_sources` + `output_target: chat`）| 對齊 view-* read-only pattern |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**寫任何檔（除可選 phase_log audit entry）
- **不**寫 view/ 整合檔
- **不**升 entity 狀態
- **不**呼叫其他 skill
- **不**改 LOCKED spec / registry / parser code
- **不**改既有 22 個 SKILL.md
- **不**改 00_j / 00_k / 任何 protocol
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE

「Fix one, find two」cascade pattern 預防（HANDOFF §4.6 + 9th master 5 條教訓內化）：

- 寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 reference / file path / D-NNN 引用）
- 寫 starter 涉及 path reference 前先 ls 實際 repo 對齊（避免再現 R1-MA-01 path aliases 錯）
- 寫 starter 涉及 SPEC frontmatter 段直接 grep SPEC §5.2 verify（避免再現 R2-MAJOR-02）

---

# 5. Wave 13 batch mode 預告

D.6 PASS → Wave 13 後續 task 採 batch 模式：

- master 將寫 `CODEX_D_VIEW_BATCH_STARTER.md` v0.1
- 內容：「依 D6 範本 + ARCH §4.1 + UX_SPEC §7 + TASKS §C.3 寫 D7/D8/D9 三個 starter」
- CODEX 在乾淨對話跑 batch starter → 寫 D7 (/view-character) + D8 (/view-outline) + D9 (/view-detailed-outline) 三組 SKILL.md
- master review 4 個 starter 一致性

---

# 6. Cross-ref

- `_design/TASKS.md` v1.9 §C.3（4 個 /view-* skill task spec）
- `_design/ARCHITECTURE.md` v1.6 §4.1（動態組合）+ §4.4（呈現規則）+ §6.7（共通骨架）
- `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）
- `_design/UX_SPEC.md` v0.4 §7（跨檔 link / source 引用 / 呈現規則）
- `_design/CODEX_D1_STARTER.md` v0.3（/iterate-world starter；對照「Phase D 寫檔 skill」格式參考；本 D6 為純讀取 skill 採不同結構）
- `.claude/skills/status/SKILL.md` v0.1 + `.claude/skills/check-gaps/SKILL.md` v0.1（既有 read-only skill 範例）
- `_design/DECISIONS_LOG.md` v2.0（如有 view 相關拍板）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master Round 1-4 review cycle 收尾 + 5 條教訓內化）
- `_design/HANDOFF_TO_9TH_MASTER.md` v1.0（9th master scope）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Milestone 3 達成事實檔）
