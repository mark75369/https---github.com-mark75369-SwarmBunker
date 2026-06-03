狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 14 task — /export-world skill + 中文 wrapper 實作（Wave 14 共通範本）  
優先級：高

# CODEX_D10_STARTER — Phase D Wave 14 D.10：/export-world skill 實作（Wave 14 共通範本）

# 0. 本檔用途

Phase D Wave 14 起手第一條 task — 實作 `/export-world` skill（寫 `view/世界觀.md` DERIVED 靜態整合檔）。對齊 TASKS v1.9 §C.5（第 1 個 /export-* skill）+ ARCH v1.6 §4.2 靜態整合檔 + §4.3 跨檔導航統一規則（時期 C 整合 UX_SPEC §7）。

**前置條件：** 9th master 第一段對話 Wave 13 4 個 /view-* skill 已落地（D6 /view-world + D7 /view-character + D8 /view-outline + D9 /view-detailed-outline 含 D-054 hybrid fallback）。第二段對話接手後 Round 1-4 review cycle 收尾 + R4-MAJOR-01 hard-limit accept 內化 5 條教訓。

**D.10 PASS → Wave 14 進 batch mode：** D11-D13（/export-character / /export-outline / /export-detailed-outline）採 CODEX batch starter 模式（不用 master 逐一寫；本 D10 是共通範本）。

**Wave 14 新工作模式（沿用 Wave 13 拍板；9th master 第二段對話內化）：**
- Master 寫 D10 完整 starter（本檔；提供完整 starter pattern + export-* 共通設計）
- Master 寫 `CODEX_D_EXPORT_BATCH_STARTER.md`（依 D10 範本批次寫 D11-D13）
- CODEX 在乾淨對話跑 batch starter 寫 D11-D13 三組 SKILL.md
- Master 端內部 verify（grep 結構 + Read 重點 section；不跑 CODEX review starter — Wave 16 才動用完整 CODEX review）

⚠ **view vs export 邊界（關鍵差異 — vs D6）：**
- `/view-*` (Wave 13)：純讀取；組合後**只印在 chat**；**不寫檔**；邊界 7 條純讀取
- `/export-*` (Wave 14；本 skill)：與 view 邏輯相同，但**寫 `view/<entity>.md` 整合檔 DERIVED 狀態**；邊界含 **D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表三 block**（對齊 Phase B/C 寫檔 skill pattern）

⚠ **/export-* 與 §4.2a Layer 3 Export 是 separate paths（嚴格區分；對齊 ARCH §4.2a.4）：**
- 本 skill (`/export-world`) 寫 `view/<entity>.md`（Markdown 整合視圖；DERIVED 狀態；human-readable）
- §4.2a L3 Export 寫 `export/<instance>_<timestamp>.{json,md}`（JSON + MD 雙吐；給 LLM 消化；走前端 panel A1 prompt 生成器）
- 兩條 export 路徑共存不取代；本 Wave **只實作** /export-*；L3 Export 屬 Phase A.0F.x（10th master scope；本 Wave 不實作 + 不擴 §4.2 既有 4 個 /export-*）

⚠ **9th master 5 條教訓內化（第一段對話 Round 1-4 cycle 結論；嚴格紀律）：**
1. **Windows baseline 權威**：sandbox virtiofs cache 在某些 check_paths case false negative；sandbox 結果只當 noise 對照；以 Windows 端 `python -X utf8 -B scripts/check_paths.py` 結果為準（baseline 門檻 ≤ 247 ERROR）
2. **Cascade sweep broader pattern**：寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（版本 / file path / D-NNN 引用 / 兩條 export 路徑混用 wording）；不只看具體 hits
3. **SPEC frontmatter 段直接 grep verify**：寫 starter 涉及 frontmatter 描述前 grep SPEC §5.2 verify；不憑記憶寫具體欄位數字（DERIVED 用「生成方式 + 組合來源」延伸欄位 — 不用 entities/depends_on/weight standard YAML block）
4. **Supersede note 避重複 finding 精確詞串**：strict grep 不分否定句 / 歷史 narrative；wording 用「修補性質」描述而非重述被改字串本身
5. **Review starter diff anchor 精確**：用明示 commit hash 或 `HEAD~1..HEAD` 限定最後一個 commit（Wave 14 不跑 review starter；本條 Wave 16 用）

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only path 前綴 `<instance_root>/`

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 14 D.10 task」— 實作 /export-world skill（含中文 wrapper）；對齊 TASKS v1.9 §C.5 + ARCH v1.6 §4.2 靜態整合檔 + §4.3 跨檔導航統一規則 + UX_SPEC §7。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase D Wave 14 第一條 task（D.10 → D.11/D.12/D.13 採 batch 模式）；/export-world 是 4 個 /export-* 系列共通範本
- D.10 PASS → 可進 Wave 14 batch（D.11-D.13 由 CODEX 跑 CODEX_D_EXPORT_BATCH_STARTER 在另一個乾淨對話寫）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔（含 `check_headers.py` DERIVED 加入 VALID_STATUS — 屬 Phase A.0F 範圍）
- ✗ **不**動既有 30 個 SKILL.md（init-project / status / check-gaps / create-* x5 + 5 中文 wrapper + scene-task / dialogue-write / qa + 3 中文 wrapper + iterate-* x6 + 6 中文 wrapper + view-* x4 + 4 中文 wrapper）
- ✗ **不**寫 /export-character（D.11 scope）/ /export-outline（D.12）/ /export-detailed-outline（D.13）
- ✗ **不**動 /view/README.md（屬 user 手動建立；DECISIONS_LOG P-004）
- ✗ **不**實作 §4.2a Layer 3 Export A1 prompt 生成器（屬 Phase A.0F.x；10th master scope）
- ✗ **不**跑真實 /export-world（會寫真實檔；Template 內無 Instance entity；本輪 implementer 只寫 SKILL.md 不執行）
- ✗ **不**修改 D-001~D-054 / NEW_REQ_15 / 任何 DECISIONS_LOG 拍板紀錄

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.5 + ARCH v1.6 §4.2 + §4.3 + UX_SPEC §7（如可訪問）。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/export-world/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/匯出世界觀/SKILL.md` | 中文 wrapper |

### /export-world 主 SKILL.md 結構（11 段；vs D6 view-world 的 6 維度差異）

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；明示「組合 W-rules / V / W-language 寫入 `view/世界觀.md` DERIVED 整合檔；與 /view-world 邏輯相同但寫檔；對齊 ARCH §4.2」）
- 中文 5 必填 header（狀態：DRAFT / 版本：v0.1 / 最後更新：YYYY-MM-DD / 適用範圍：/export-world skill runtime instructions / 優先級：中）
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（`/export-world` + 中文 `/匯出世界觀` reference）
  - `## 觸發協議`（無對應 00_protocol/ — export 是純技術 skill 無協議；對齊 ARCH §4.2 邏輯為權威）
  - `## 啟動前檢查`（D-049 Template-detect + Bootstrap completed + W-rules / V / W-language 至少 DRAFT 存在 + `view/` 目錄存在 / 可建立）
  - `## 流程`（5 階段：診斷 / 反查 source / 組合 + 加 breadcrumb + 條件加 TOC / 寫檔 view/世界觀.md / 驗證）
  - `## 呈現規則`（**含 breadcrumb**；**條件加 TOC** > 200 行；**末尾加返回連結**；每段尾加 source italic；跨檔 link `/` 開頭；slug 內驗證 P-005）
  - `## .protocol_version 寫入規範`（寫 phase_log entry：`output_path` + `output_lines` + `breadcrumb_added` + `toc_added` + `slug_validation_result`；不更新 entity 完成度）
  - `## 輸入`（無 user 參數）
  - `## 輸出`（**寫 `view/世界觀.md` DERIVED 狀態**；明示「DERIVED 檔不可手動修改；要更新請重跑 /export-world」）
  - `## 邊界`（**邊界三 block**：D-050 子裁決 1 / D-053 紀錄 / D-050 子裁決 2 寫檔目錄表 — 對齊 Phase B/C 寫檔 skill pattern）
  - `## 錯誤處理 / Rollback`（source 缺漏處理：印警示 + 仍寫整合檔但缺漏段填 `[source 缺漏 — 跑 /create-world 或 /iterate-world 補]` placeholder；寫檔失敗 → rollback；slug 衝突 → 修檔內 anchor 後重新驗證）
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### /export-world 差異規格（vs /view-world）

| 維度 | /view-world (Wave 13) | /export-world (本 skill) |
|---|---|---|
| 輸出目標 | chat | `view/世界觀.md` 整合檔（DERIVED 狀態）|
| 是否寫檔 | 不寫檔（除可選 phase_log audit）| **寫檔**（必寫 phase_log + output_path）|
| Breadcrumb | 不加（chat 動態組合）| **必加**（frontmatter 之後、第一個 `#` 之前；格式 `> 專案首頁 / 世界觀 / 完整視圖`）|
| TOC | 不加 | **條件加**（預估 > 200 行；位置：frontmatter + breadcrumb 之後、第一個 `#` 之前；標題 `## 目錄 / Contents`；GFM slug；skill 內驗 P-005）|
| 返回連結 | 不加 | **末尾必加** `[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)`（P-004）|
| 邊界 | 純讀取 7 條 | **D-050 三 block**（子裁決 1 + D-053 + 子裁決 2 寫檔目錄表）|
| Source 反查 | 同 view（共用組合邏輯）| 同 view（共用組合邏輯）|
| 觸發語 | `/view-world` | `/export-world`（不接 user 參數）|
| 對應 protocol | 無 | 無 |
| 議題清單動態載入 | 不適用 | 不適用 |
| modify entity 範圍 | 無 | 無（只寫 view/ 整合檔；不修任何 entity）|
| 依賴 | W-rules / V / W-language 至少 DRAFT | W-rules / V / W-language 至少 DRAFT（同 view）|
| 下游 | 印「下一步建議」 | 寫檔後印「整合檔已寫於 view/世界觀.md；要修改世界觀請跑 /iterate-world 後重新 /export-world」|

### 5 階段流程（適配 export；對齊 ARCH §4.2）

#### 階段 1：診斷（與 view-world 同）

agent 開場：

> /export-world 將動態組合世界觀整合視圖（W-rules / V / W-language + 02_vocabulary 詞彙系統 + 00_b §1/§2 反 AI 味基線）並**寫入 `view/世界觀.md` DERIVED 整合檔**。本 skill 寫單一靜態整合檔；要更新請重跑本 skill。
> 
> 開始讀取 source...

agent 檢查啟動前條件（D-049 / Bootstrap / 目標 entity 至少 DRAFT 存在 / `view/` 目錄存在 / 可建立）；任何缺漏拒絕並印缺漏清單。

#### 階段 2：反查 source（同 view-world；共用組合邏輯）

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
- 解析 frontmatter（驗證 entity 對應；抽 source 最高 `版本` 給整合檔 frontmatter 用）
- 抽取 main content（跳過 frontmatter + 中文 5 header）
- 標記抽取位置（line 起訖；給 audit 用）

#### 階段 3：組合 + 加 breadcrumb + 條件加 TOC（in-memory）

agent 把 source 組合成單一 Markdown 結構：

```markdown
狀態：DERIVED  
版本：<對應 source 的最高版本>  
最後更新：<執行時的日期 YYYY-MM-DD>  
適用範圍：世界觀整合視圖  
優先級：中  
生成方式：/export-world  
組合來源：
  - 01_world/01_a_世界觀總覽.md
  - 01_world/01_b_世界語言規格.md
  - 01_world/01_c_陣營與階級語言.md
  - 02_vocabulary/02_a_專有名詞表.md
  - 02_vocabulary/02_b_俗稱與黑話表.md
  - 02_vocabulary/02_c_禁用詞與慎用詞表.md
  - 00_protocol/00_b_反ai味檢查表.md

> 專案首頁 / 世界觀 / 完整視圖

## 目錄 / Contents

<僅當預估 > 200 行時插入；含 GFM auto slug；skill 內驗證 slug 一致性 — P-005>

# 世界觀 — /export-world 靜態整合檔

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

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

**Frontmatter 紀律（嚴格對齊 ARCH §4.2 line 753-769）：**
- DERIVED 用「生成方式 + 組合來源」延伸欄位（中文 header 延伸；**不用** entities/depends_on/weight standard YAML block — 對齊 SPEC §5.2.5 第 4 條協議檔可省略 + §16 DERIVED `view/` 目錄專用）
- `組合來源:` block 以 list 形式列出所有 source；YAML-like 但屬中文 header 延伸欄位（與 SPEC §5.2.3 表列 11 個正式欄位區分；屬 §13a.5 延伸用法）
- `版本` 欄寫「對應 source 的最高版本」（agent 階段 2 抽 source frontmatter 後比對取最高）
- `最後更新` 寫執行當下日期

**Breadcrumb 紀律（對齊 ARCH §4.2 line 777 + §4.3 line 833）：**
- 位置：frontmatter 之後、第一個 `#` 之前（**也在 TOC 之前**）
- 格式：`> 專案首頁 / 世界觀 / 完整視圖`
- 不加箭頭符號 / 不加日期 / 不加狀態 badge
- 用半形空格 / 分隔（不用全形）

**TOC 紀律（對齊 ARCH §4.2 line 779 + §4.3 line 836）：**
- 觸發：預估 > 200 行時插入
- 位置：frontmatter + breadcrumb 之後、第一個 `#` 之前
- 標題：`## 目錄 / Contents`
- Slug：依 GFM 自動規則（中文主＋英文 sub `世界規則 / World Rules` → slug `世界規則-world-rules`）；**不手動寫 `{#anchor}`**
- 一致性驗證：skill 階段 5 內驗證（P-005）— 不擴大 `check_headers.py` global linter scope

**返回連結紀律（對齊 ARCH §4.2 line 778 + §4.3 line 834）：**
- 位置：整合檔末尾（最後一行 `---` 分隔後）
- 格式：`[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)`（含中文寬間隔符 `｜`）
- `/view/README.md` 由 user 手動建立（DECISIONS_LOG P-004）— skill 不檢查目標檔存在；只寫連結

#### 階段 4：寫檔 view/世界觀.md

agent 把組合結果寫入 `view/世界觀.md`。

**寫檔紀律：**
- 路徑：`<instance_root>/view/世界觀.md`（Instance scope；不寫到 _design / 00_protocol / 01_world / 等其他目錄）
- 若 `view/` 目錄不存在 → agent 建立目錄
- 若 `view/世界觀.md` 已存在 → 直接覆寫（DERIVED 檔本來就應隨 source 更新重寫）
- 寫檔失敗 → rollback（刪除部分寫入的檔；印錯誤；不更新 phase_log）

#### 階段 5：驗證 + 寫 phase_log

階段 5 驗證 + 寫 phase_log：

- **Slug 一致性驗證（P-005）**：若階段 3 加了 TOC，agent 對所有 `##` / `###` 標題用 GFM 規則生成 slug；與 TOC 連結比對；不一致 → 修檔內 anchor 後重新寫檔
- **寫 `.protocol_version.phase_log` entry**（必寫；含 `output_path` + `output_lines` + `breadcrumb_added` + `toc_added` + `slug_validation_result` + `read_sources` 清單）
- **不**自動 trigger /status（export 是 read-source / write-DERIVED；不影響實體狀態）
- 印「下一步建議」段：「整合檔已寫於 view/世界觀.md；要修改世界觀請跑 /iterate-world 後重新 /export-world」

### .protocol_version phase_log entry 範例（必寫）

```yaml
- phase: export-world
  date: YYYY-MM-DD
  skill: /export-world
  status: completed
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 00_protocol/00_b_反ai味檢查表.md  # §1/§2
  output_path: view/世界觀.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

### 啟動前檢查（嚴格條件）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在（屬 Instance）| 拒絕並提示用 /init-project |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕並提示用 /init-project |
| W-rules / V / W-language 存在 | 對應分拆檔存在 + frontmatter 含目標 entity；**狀態 ≥ DRAFT 即可**（同 view；不要求 ≥ REVIEW；export 屬 read-any-state + write-DERIVED）| 拒絕並印缺漏清單；提示用 /create-world |
| `view/` 目錄存在或可建立 | `<instance_root>/view/` 存在或 agent 可建立 | 不可建立 → 拒絕並印權限錯誤 |
| 不要求下游 pipeline 互鎖檢查 | export 是 read-source / write-DERIVED；不影響任何進行中 skill | — |

### 邊界區段（D-050 三 block；對齊 Phase B/C 寫檔 skill pattern）

`/export-world` 是寫檔 skill（寫 `view/<entity>.md` DERIVED 整合檔）。邊界對齊 D-050 + D-053 三 block：

**Block 1 — D-050 子裁決 1（00_protocol/ 寫入禁制；本 skill 強化）：**

```
本 skill 不寫 `00_protocol/` 任何檔。

D-050 子裁決 1 規範「所有 /create-* / /iterate-* / /scene-task / /dialogue-write / /qa
skill 嚴禁寫 00_protocol/」；本 skill 同樣適用。

例外（D-053）：/create-world 可寫 00_b §1 §2（Instance-specific section）— 本 skill **不**屬於該例外。
```

**Block 2 — D-053 紀錄（exception 紀律承接）：**

```
本 skill 不觸發 D-053 /create-world exception；本 skill 不寫 00_protocol/ 任何段。
若 user 要修改 00_b §1/§2（作品類型語氣 / 髒話尺度），請走 /iterate-world（屬 Wave 12 scope；
本 skill 純粹組合 source 寫整合檔，不擅自反向回寫 source）。
```

**Block 3 — D-050 子裁決 2（寫檔目錄表；本 skill 限定）：**

```
本 skill 寫檔目錄表：

| 目錄 | 是否寫入 | 說明 |
|---|---|---|
| `view/` | ✅ 寫 | 寫 `view/世界觀.md`（DERIVED；本 skill 唯一寫入目錄）|
| `.protocol_version` | ✅ 寫（phase_log entry 追加）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `01_world/` | ✗ 不寫 | source 唯讀 |
| `02_vocabulary/` | ✗ 不寫 | source 唯讀 |
| `03_characters/` ~ `09_quality_assurance/` | ✗ 不寫 | 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |
| `export/` | ✗ 不寫 | 屬 §4.2a Layer 3 Export A1 prompt 生成器 scope（separate path；不在本 skill scope）|

**寫 `view/` 目錄以外任何檔 → rollback + 拒絕。**
```

**vs Wave 13 view-* 7 條純讀取邊界的差異：**
- view-* 用「不寫檔 / 不擴 source / 不升 entity / 不擅自呼叫其他 view-* / 不擅自重新組織 / 不寫 LOCKED 狀態」7 條（純讀取性質）
- export-* 改用 D-050 三 block（寫檔性質；對齊 Phase B/C 寫檔 skill pattern）
- 共通：兩者都不擅自重新組織 source 內容（只 verbatim 抽取 + 套組合結構）

### 中文 wrapper SKILL.md 結構（匯出世界觀）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 匯出世界觀
description: "/export-world skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/export-world skill 中文觸發 wrapper  
優先級：中

# /匯出世界觀（/export-world wrapper）

本 wrapper 是 `/export-world` 的中文別名。執行時以英文主檔 `.claude/skills/export-world/SKILL.md` 為權威。

請參考 `.claude/skills/export-world/SKILL.md`。
```

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：
   - `_design/TASKS.md` v1.9 §C.5（4 個 /export-* skill task spec）
   - `_design/ARCHITECTURE.md` v1.6 §4.2（/export-* 靜態整合檔；DERIVED frontmatter 範本 line 753-769）+ §4.3（跨檔導航統一規則；breadcrumb / TOC / 返回連結 / slug / source 引用 / 單向 reference / view 失效偵測）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema — 對齊 + 注意 DERIVED 用「生成方式 + 組合來源」延伸欄位，不用 standard YAML block）+ §13.4（分享階段：靜態整合檔 B 模式）+ §16（文件狀態機；DERIVED `view/` 目錄專用）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則 — 跨檔 link / source 引用 / 單向 reference / breadcrumb / TOC / slug）
   - `.claude/skills/view-world/SKILL.md` v0.1（Wave 13 view-world skill；本 skill 共用組合邏輯；對齊 5 階段流程 stage 1-2）
   - `.claude/skills/查看世界觀/SKILL.md` v0.1（Wave 13 中文 wrapper 範例）
   - `_design/DECISIONS_LOG.md` v2.0（P-004 /view/README.md 暫定 + P-005 slug 一致性暫定 + §6.12.2 D-050 子裁決 1+2 + §6.16.2 D-053）

2. **寫 SKILL.md 2 個**：
   - 英文主檔 `.claude/skills/export-world/SKILL.md`（依本 starter §1 「主 SKILL.md 結構」+ 「差異規格」+ 「5 階段流程」+ 「邊界區段三 block」）
   - 中文 wrapper `.claude/skills/匯出世界觀/SKILL.md`（依本 starter §1 「中文 wrapper SKILL.md 結構」）

3. **跑 baseline 驗證**：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - `python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; ..."`
   - 對齊 9th master 第一段 Round 1-4 收尾後 baseline：`check_paths ≤ 247 ERROR`（R2-MAJOR-03 hard-limit accept；以 Windows 端為權威）
   - **注意：DERIVED 加入 `check_headers.py VALID_STATUS` 不在本 task scope**（ARCH §4.2 line 773 註「Phase C 同步更新」屬未來 patch；本 skill 不擅動 scripts/）；若 baseline 因此報新 ERROR → 屬已知 deferred；視為 baseline noise 不算 regression

4. **不跑真實 /export-world**（Template repo 內無 Instance entity 也無 `view/` 目錄；本輪 implementer 只寫 SKILL.md 不執行）

---

# 3. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index baseline | 對齊 9th master 第一段 Round 1-4 收尾後 baseline；無新真實 ERROR；check_paths ≤ 247 |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 5 階段流程 + 呈現規則 | SKILL.md 含 5 階段對齊 ARCH §4.2 + 呈現規則對齊 §4.3 | 完整 |
| 4. DERIVED frontmatter 紀律 | SKILL.md 階段 3 範本對齊 ARCH §4.2 line 753-769（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級 / 生成方式 / 組合來源 7 欄）| 與 SPEC §5.2 standard YAML block 區分 |
| 5. Breadcrumb / TOC / 返回連結紀律 | SKILL.md 明示位置 + 格式 + 觸發條件（TOC > 200 行 / slug 一致性 P-005 / 末尾返回連結 P-004）| 對齊 ARCH §4.2-§4.3 |
| 6. 邊界三 block | SKILL.md 含 D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表三 block 完整 | 與 view-* 純讀取邊界 7 條模式不同 |
| 7. phase_log entry 規範 | SKILL.md 含 phase_log entry 範例（必寫；含 `output_path` + `output_lines` + `breadcrumb_added` + `toc_added` + `slug_validation_result` + `read_sources`）| 對齊 export-* 寫檔 audit pattern |
| 8. 兩條 export 路徑區分 | SKILL.md 明示「不實作 §4.2a Layer 3 Export A1 prompt 生成器」| 對齊 ARCH §4.2a.4 區分表 |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**寫 `view/` 目錄以外任何檔（除 `.protocol_version.phase_log` audit）
- **不**升 entity 狀態
- **不**呼叫其他 skill（包括 /view-world — 本 skill 共用組合邏輯但不 chain call）
- **不**改 LOCKED spec / registry / parser code
- **不**改既有 30 個 SKILL.md
- **不**改 00_protocol/ 任何檔
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE
- **不**動 `scripts/check_headers.py` VALID_STATUS（屬 Phase A.0F / 10th master scope）
- **不**實作 §4.2a Layer 3 Export A1 prompt 生成器（屬 Phase A.0F.x；10th master scope）

「Fix one, find two」cascade pattern 預防（HANDOFF §4.6 + 9th master 第一段 5 條教訓內化）：

- 寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 reference / file path / D-NNN 引用 / 兩條 export 路徑混用 wording）
- 寫 starter 涉及 path reference 前先 ls 實際 repo 對齊
- 寫 starter 涉及 SPEC frontmatter 段直接 grep SPEC §5.2 verify（DERIVED 用延伸欄位非 standard YAML block）

---

# 5. Wave 14 batch mode 預告

D.10 PASS → Wave 14 後續 task 採 batch 模式：

- master 將寫 `CODEX_D_EXPORT_BATCH_STARTER.md` v0.1
- 內容：「依 D10 範本 + ARCH §4.2 + §4.3 + UX_SPEC §7 + TASKS §C.5 寫 D11/D12/D13 三組 SKILL.md」
- CODEX 在乾淨對話跑 batch starter → 寫 D11 (/export-character) + D12 (/export-outline) + D13 (/export-detailed-outline) 三組英文主檔 + 3 個中文 wrapper
- D13 /export-detailed-outline **必含 D-054 hybrid fallback**（per-scene 檔 → aggregate 06_a fallback；對齊 Wave 13 D9 /view-detailed-outline pattern）
- master 端內部 verify（grep 結構 + Read 重點 section；不跑 CODEX review starter）

---

# 6. Cross-ref

- `_design/TASKS.md` v1.9 §C.5（4 個 /export-* skill task spec）
- `_design/ARCHITECTURE.md` v1.6 §4.2（/export-* 靜態整合檔；DERIVED frontmatter 範本）+ §4.2a（L3 Export A1 prompt 生成器；separate path）+ §4.3（跨檔導航統一規則）+ §6.7（共通骨架）
- `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）+ §13.4（分享階段：靜態整合檔 B 模式）+ §13a（Layer 3 Export JSON+MD 雙吐機制；separate path）+ §16（文件狀態機；DERIVED）
- `_design/UX_SPEC.md` v0.4 §7（跨檔 link / source 引用 / 呈現規則）
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（Layer 3 Export prompt schema；本 skill **不**實作，僅 §Z L3 schema 對齊備忘 reference）
- `_design/CODEX_D6_STARTER.md` v0.1（/view-world starter；本 D10 共用組合邏輯）
- `.claude/skills/view-world/SKILL.md` v0.1（Wave 13 落地 view-world skill；本 skill 共用組合邏輯參考）
- `.claude/skills/查看世界觀/SKILL.md` v0.1（中文 wrapper 範例）
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 子裁決 1+2（寫檔目錄表）+ §6.16.2 D-053（/create-world exception）+ P-004（/view/README.md 暫定）+ P-005（slug 一致性暫定）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master 第一段 Round 1-4 review cycle 收尾 + 5 條教訓內化 + NEW_REQ_10 outer fence 慣例）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話 scope）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Milestone 3 達成事實檔）

---

# §Z 前端工具友好性紀律（Phase A.0F 平行對話備忘）

> **Wave 14 完成後**，user 將開「Phase A.0F 平行對話」起手 A.0F.x L3 prompt 生成器 + 層 2/3 feature。本 §Z 段為本 D10 starter 對「前端工具友好性」的設計紀律：確保 view/<entity>.md 結構未來可被前端 viewer 消化。

## §Z.1 view/<entity>.md 對前端友好的結構紀律

| 結構元素 | 紀律 | 對前端的價值 |
|---|---|---|
| Frontmatter「生成方式」欄 | 固定為 `/export-world`（不寫具體日期）| 前端可依 `生成方式` 欄判斷檔案類型 |
| Frontmatter「組合來源」欄 | List 形式（YAML-like）| 前端 viewer 可解析 source dependency 顯示「點 source 跳轉」 |
| Frontmatter「狀態」 | 必為 `DERIVED` | 前端 editor 可標 read-only 防誤改 |
| Breadcrumb | 固定位置（frontmatter 之後、第一個 `#` 之前；TOC 之前）| 前端 navigation panel 可解析顯示 |
| TOC | 固定位置（frontmatter + breadcrumb 之後）+ GFM slug | 前端 sidebar TOC 可解析 |
| 返回連結 | 固定位置（最後一個 `---` 之後）+ 固定格式 | 前端 router 可正確 dispatch |
| Source 引用 | 每段尾 italic `*來源：[/path](/path)*` | 前端可解析「點 source 連結跳轉」 |

## §Z.2 L3 Export schema 對齊備忘（**不實作**）

對照 `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 §1.1 必填 5 區塊（標題 / YAML 元資料 / 步驟 / 約束 / 完成回報）：

| L3 區塊 | 本 skill 對應 | 對齊狀況 |
|---|---|---|
| 標題 | view/世界觀.md 第一個 `#` 標題（`# 世界觀 — /export-world 靜態整合檔`）| ✅ 對齊（人類可讀；L3 prompt 生成器可解析）|
| YAML 元資料 | frontmatter 7 欄（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級 / 生成方式 / 組合來源）| △ 部分對齊（L3 schema §1.2 含 `schema_version / repo_root / scope / formats / output_paths / mode / contract_refs` 等屬 L3 特有；本 skill frontmatter 是 SPEC §5.2 + §13a.5 延伸 — L3 prompt 生成器讀本 view/<entity>.md 時把它當「source 之一」消化，不直接套用 L3 §1.2 YAML schema）|
| 步驟 | 本 skill 5 階段流程 | ✅ 對齊（L3 prompt 5 步驟對應 read → manifest → records → write JSON/MD → 回報；本 skill 對應 診斷 → 反查 → 組合 → 寫檔 → 驗證）|
| 約束 | 邊界三 block | ✅ 對齊（L3 約束 read_only + 限定 output_paths；本 skill D-050 子裁決 2 寫檔目錄表限 view/）|
| 完成回報 | phase_log entry（output_path + output_lines + ...）| ✅ 對齊（L3 完成回報含 output_paths + size + records 數；本 skill phase_log 含 output_path + output_lines + slug_validation_result）|

**結論：** Wave 14 /export-* 寫出的 `view/<entity>.md` 結構**可被未來 L3 prompt 生成器消化為 source 之一**；不直接套用 L3 §1.2 YAML schema（兩條 export 路徑共存不取代；對齊 ARCH §4.2a.4）。本 §Z.2 段為對齊備忘紀錄；不擴 §4.2 既有 4 個 /export-* + 不實作 L3 prompt 生成器（屬 Phase A.0F.x；10th master scope）。

## §Z.3 對 Phase A.0F 平行對話的友好性

本 D10 starter 寫法已預留：
- view/<entity>.md frontmatter 欄位穩定 → 前端 viewer 可長期消化
- breadcrumb / TOC / 返回連結結構標準化 → 前端 navigation panel 可解析
- DERIVED 狀態明示 → 前端 editor 可標 read-only 防誤改
- slug 一致性 skill 內驗證（P-005）→ 前端 anchor 跳轉穩定

Phase A.0F 平行對話起手 A.0F.x feature 時可 reference 本 §Z 段；不必回頭改 Wave 14 spec。
