狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 14 batch task — D11 (/export-character) + D12 (/export-outline) + D13 (/export-detailed-outline) skill 實作（採 batch 模式 — CODEX 一輪寫 3 個 starter 的 6 個 SKILL.md）  
優先級：高

# CODEX_D_EXPORT_BATCH_STARTER — Phase D Wave 14 batch task (D11-D13)

# 0. 本檔用途

Phase D Wave 14 後 3 條 task — CODEX 在乾淨對話一次寫 D11 (/export-character) + D12 (/export-outline) + D13 (/export-detailed-outline) 三個 export-* skill（共 6 個 SKILL.md：3 個英文主檔 + 3 個中文 wrapper）。

**前置條件：** D.10 (/export-world) PASS（已建 master 端 starter 範本 `_design/CODEX_D10_STARTER.md` v0.1）+ CODEX 已熟悉 export-* 共通設計。

**Wave 14 工作模式（9th master 第二段對話沿用 Wave 13 模式）：**
- Master 寫 D10 完整 starter（共通範本；已落地 v0.1）
- Master 寫本 batch starter（CODEX_D_EXPORT_BATCH_STARTER.md；本檔）
- CODEX 在乾淨對話跑本 batch starter → 寫 D11/D12/D13 三個 starter 的 6 個 SKILL.md
- Master 端內部 verify 4 個 export-* SKILL.md 一致性（grep 結構 + Read 重點 section；不跑 CODEX review starter — Wave 16 才動用完整 CODEX review）

⚠ **本檔 = 給 CODEX 跑 batch task 的指引**：CODEX 拿本檔 + D10 starter + 必讀 spec → 一次寫 D11/D12/D13 的 6 個 SKILL.md。

⚠ **view vs export 邊界（同 D10）：** export 與 view 邏輯相同但**寫 `view/<entity>.md` 整合檔 DERIVED 狀態**；邊界含 D-050 三 block（不是 view-* 純讀取邊界 7 條）。

⚠ **本 Wave 不實作 §4.2a Layer 3 Export A1 prompt 生成器**（屬 Phase A.0F.x；10th master scope；對齊 ARCH §4.2a.4）。

⚠ **慣例：** outer agent-prompt fence 用 `~~~`；Instance-only path 前綴 `<instance_root>/`。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 14 batch task (D11-D13)」— 實作 3 個 export-* skill：/export-character + /export-outline + /export-detailed-outline（含 3 個中文 wrapper；共 6 個 SKILL.md）；對齊 TASKS v1.9 §C.5 + ARCH v1.6 §4.2 靜態整合檔 + §4.3 跨檔導航統一規則 + UX_SPEC §7。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**共通範本：** 本 task 採與 D10 (/export-world) 相同的 starter pattern。**先讀 `_design/CODEX_D10_STARTER.md` v0.1** 對齊：
- 主 SKILL.md 結構（11 段：frontmatter + 中文 5 header + 用途 / 觸發語 / 觸發協議 / 啟動前檢查 / 流程 / 呈現規則 / phase_log / 輸入 / 輸出 / 邊界 / 錯誤處理 / 錯誤呈現）
- 5 階段流程（適配 export：診斷 / 反查 source / 組合+breadcrumb+條件 TOC / 寫檔 / 驗證+slug+phase_log）
- DERIVED frontmatter 範本（7 欄：狀態 DERIVED / 版本 / 最後更新 / 適用範圍 / 優先級 / 生成方式 / 組合來源 — 對齊 ARCH §4.2 line 753-769；不用 SPEC §5.2 standard YAML block）
- 呈現規則（**含 breadcrumb 必加** / **TOC > 200 行條件加** / **返回連結末尾必加** / source italic / 跨檔 link `/` 開頭 / slug 一致性 skill 內驗證 P-005）
- phase_log entry 範例（必寫；含 `output_path` + `output_lines` + `breadcrumb_added` + `toc_added` + `slug_validation_result` + `read_sources`）
- 啟動前檢查 5 項（D-049 + Bootstrap + 目標 entity ≥ DRAFT + `view/` 目錄存在 / 可建立 + 不要求下游互鎖）
- 邊界三 block（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表）
- 中文 wrapper 極簡模式

依下方「D11-D13 各 skill 差異規格」針對每個 skill 修改 entity 類型 / source 範圍 / 組合結構 / 觸發語 / 寫檔目標 / breadcrumb 文案。

**你的身份與職責：**
- 你是 implementer — 本輪建 6 個新 SKILL.md（3 英文主檔 + 3 中文 wrapper）
- D11-D13 batch PASS → Wave 14 整體 PASS；可進 Wave 15（/diagnose + /integrate）

**重要邊界（沿用 D10 + batch）：**
- ✗ 不改 LOCKED spec / registry / parser
- ✗ 不改既有 32 個 SKILL.md（含 /export-world + /匯出世界觀 — D10 剛建；本輪不改）
- ✗ 不寫 /diagnose / /integrate（Wave 15 scope）
- ✗ 不動 /view/README.md（屬 user 手動建立；DECISIONS_LOG P-004）
- ✗ 不實作 §4.2a Layer 3 Export A1 prompt 生成器（屬 Phase A.0F.x；10th master scope）
- ✗ 不動 `scripts/check_headers.py` VALID_STATUS（DERIVED 加入屬 Phase A.0F / 10th master scope）
- ✗ 不改 00_j / 00_k / 任何 protocol
- ✗ 不改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE

### 任務目標（6 個 SKILL.md — batch 寫完）

| # | 路徑 | 主檔 / wrapper | 寫檔目標 |
|---|---|---|---|
| 1 | `.claude/skills/export-character/SKILL.md` | 英文主檔（D11）| `view/角色_<name>.md` |
| 2 | `.claude/skills/匯出角色/SKILL.md` | 中文 wrapper | — |
| 3 | `.claude/skills/export-outline/SKILL.md` | 英文主檔（D12）| `view/大綱.md` |
| 4 | `.claude/skills/匯出大綱/SKILL.md` | 中文 wrapper | — |
| 5 | `.claude/skills/export-detailed-outline/SKILL.md` | 英文主檔（D13）| `view/細綱.md`（**含 D-054 hybrid fallback**）|
| 6 | `.claude/skills/匯出細綱/SKILL.md` | 中文 wrapper | — |

---

# 2. D11 (/export-character) 差異規格（vs D10）

- **觸發語：** `/export-character <name>`（**接 1 user 參數** — 角色名）
- **對應 protocol：** 無（export 屬純技術 skill）
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取單一 C-<name>；只寫 `view/角色_<name>.md` DERIVED）
- **依賴：** C-<name> 至少 DRAFT 存在；不要求 ≥ REVIEW
- **下游：** 階段 5 印「下一步建議：整合檔已寫於 view/角色_<name>.md；修改角色請跑 /iterate-character <name> 後重新 /export-character <name>」
- **寫檔目標：** `view/角色_<name>.md`（**檔名含 user 參數**；slug 規則：中文名稱 GFM 自動轉換）
- **Breadcrumb 文案：** `> 專案首頁 / 角色 / <name> / 完整視圖`

### Source 反查預期（D11）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `03_characters/main/<name>_聲線卡.md` 或 `03_characters/minor/<name>_*.md` 或 `03_characters/npc/<name>_*.md` | C-<name> 主聲線卡（依 frontmatter entities 反查實際路徑）| "## 聲線卡" 段 |
| `04_relationships/04_a_角色關係矩陣.md` | 含 R-<name>-* / R-*-<name> 的關係 entry | "## 關係" 段（grep entities `R-<name>-*` 或 `R-*-<name>` 的 entry section）|
| `04_relationships/04_b_關係變化時間線.md` | 含本角色的時間線 entry | "## 時間線" 段（grep 本角色 reference 的 entry section）|
| `05_plot/05_c_角色弧線表.md` | 含本角色的弧線階段 | "## 弧線" 段（grep 本角色 entries section）|
| `06_scene_index/06_a_場景索引模板.md` + 已存在 per-scene 拆檔（D-054 hybrid fallback）| 含本角色出場場景列表 | "## 出場場景" 段（grep entities 含 C-<name> 的 S-*-* row）|

### 組合結構（D11）

```markdown
狀態：DERIVED  
版本：<對應 source 的最高版本>  
最後更新：<YYYY-MM-DD>  
適用範圍：角色 <name> 整合視圖  
優先級：中  
生成方式：/export-character
組合來源:
  - 03_characters/<scope>/<name>_聲線卡.md
  - 04_relationships/04_a_角色關係矩陣.md
  - 04_relationships/04_b_關係變化時間線.md
  - 05_plot/05_c_角色弧線表.md
  - 06_scene_index/06_a_場景索引模板.md

> 專案首頁 / 角色 / <name> / 完整視圖

## 目錄 / Contents
<僅當 > 200 行；GFM slug；skill 內驗 P-005>

# 角色：<name> — /export-character 靜態整合檔

## 聲線卡
<03_characters/.../<name> 聲線卡內容>
*來源：[/03_characters/<path>](/03_characters/<path>)*

## 關係
<04_a 抽取本角色相關 R-entry section>
*來源：[/04_relationships/04_a_角色關係矩陣.md](/04_relationships/04_a_角色關係矩陣.md)*

## 時間線
<04_b 抽取本角色時間線 entry>
*來源：[/04_relationships/04_b_關係變化時間線.md](/04_relationships/04_b_關係變化時間線.md)*

## 弧線
<05_c 抽取本角色弧線階段>
*來源：[/05_plot/05_c_角色弧線表.md](/05_plot/05_c_角色弧線表.md)*

## 出場場景
<06_a (或 per-scene 拆檔) 抽取本角色出場 S-*-* 列表；D-054 hybrid fallback>
*來源：[/06_scene_index/06_a_場景索引模板.md](/06_scene_index/06_a_場景索引模板.md) (含 per-scene 拆檔；D-054 hybrid)*

---

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

### 啟動前檢查（D11 — 加 C-<name> 存在檢查）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 / Bootstrap | 同 D10 | 同 D10 |
| **C-<name> 存在** | `03_characters/.../<name>_*.md` frontmatter 含 `entities: [C-<name>]`；狀態 ≥ DRAFT | 拒絕並提示用 /create-character <name> 建立 |
| **`view/` 目錄存在或可建立** | 同 D10 | 同 D10 |

### phase_log entry 範例（D11）

```yaml
- phase: export-character
  date: YYYY-MM-DD
  skill: /export-character
  status: completed
  target_entity: C-<name>
  read_sources:
    - 03_characters/main/<name>_聲線卡.md  # 或對應 minor/npc 路徑
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_c_角色弧線表.md
    - 06_scene_index/06_a_場景索引模板.md  # + per-scene 拆檔 list（D-054 hybrid）
  output_path: view/角色_<name>.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

---

# 3. D12 (/export-outline) 差異規格（vs D10）

- **觸發語：** `/export-outline`（不接 user 參數）
- **對應 protocol：** 無
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取 P；只寫 `view/大綱.md` DERIVED）
- **依賴：** P 至少 DRAFT 存在
- **下游：** 階段 5 印「下一步建議：整合檔已寫於 view/大綱.md；修改主線請跑 /iterate-outline 後重新 /export-outline」
- **寫檔目標：** `view/大綱.md`
- **Breadcrumb 文案：** `> 專案首頁 / 大綱 / 完整視圖`

### Source 反查預期（D12）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `05_plot/05_a_主線大綱模板.md` | P 主分拆 | "## 主線結構" 段 |
| `05_plot/05_b_章節結構模板.md` | CH-* entries | "## 章節結構" 段 |
| `05_plot/05_c_角色弧線表.md` | 角色弧線階段 | "## 角色弧線" 段 |
| `05_plot/05_d_資訊揭露表.md` | 章節揭露順序 | "## 資訊揭露" 段 |
| `05_plot/05_e_伏筆與回收表.md` | 伏筆與回收 | "## 伏筆與回收" 段 |

### 組合結構（D12）

```markdown
狀態：DERIVED  
版本：<對應 source 的最高版本>  
最後更新：<YYYY-MM-DD>  
適用範圍：大綱整合視圖  
優先級：中  
生成方式：/export-outline
組合來源:
  - 05_plot/05_a_主線大綱模板.md
  - 05_plot/05_b_章節結構模板.md
  - 05_plot/05_c_角色弧線表.md
  - 05_plot/05_d_資訊揭露表.md
  - 05_plot/05_e_伏筆與回收表.md

> 專案首頁 / 大綱 / 完整視圖

## 目錄 / Contents
<僅當 > 200 行；GFM slug；skill 內驗 P-005>

# 大綱 — /export-outline 靜態整合檔

## 主線結構
<05_a 內容>
*來源：[/05_plot/05_a_主線大綱模板.md](/05_plot/05_a_主線大綱模板.md)*

## 章節結構
<05_b 內容>
*來源：[/05_plot/05_b_章節結構模板.md](/05_plot/05_b_章節結構模板.md)*

## 角色弧線
<05_c 內容>
*來源：[/05_plot/05_c_角色弧線表.md](/05_plot/05_c_角色弧線表.md)*

## 資訊揭露
<05_d 內容>
*來源：[/05_plot/05_d_資訊揭露表.md](/05_plot/05_d_資訊揭露表.md)*

## 伏筆與回收
<05_e 內容>
*來源：[/05_plot/05_e_伏筆與回收表.md](/05_plot/05_e_伏筆與回收表.md)*

---

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

### phase_log entry 範例（D12）

```yaml
- phase: export-outline
  date: YYYY-MM-DD
  skill: /export-outline
  status: completed
  target_entity: P
  read_sources:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_c_角色弧線表.md
    - 05_plot/05_d_資訊揭露表.md
    - 05_plot/05_e_伏筆與回收表.md
  output_path: view/大綱.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

---

# 4. D13 (/export-detailed-outline) 差異規格（vs D10；**含 D-054 hybrid fallback 讀檔**）

- **觸發語：** `/export-detailed-outline` 或 `/export-detailed-outline <CH-ID>`（**可選 1 user 參數** — 章節 ID；若不傳 = 寫含全部章節的整合檔）
- **對應 protocol：** 無
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取 CH-* / S-*-*；只寫 `view/細綱.md` DERIVED）
- **依賴：** CH-* / S-*-* 至少 DRAFT 存在（透過 05_b 或 06_a 反查）
- **下游：** 階段 5 印「下一步建議：整合檔已寫於 view/細綱.md；修改章節請跑 /iterate-detailed-outline <CH-ID> 後重新 /export-detailed-outline；單場拆檔請跑 /iterate-scene <S-ID> --split-to-file」
- **寫檔目標：** `view/細綱.md`（**整合檔含全部章節**；若 user 傳 CH-ID 參數，**僅寫該章節**並 frontmatter `適用範圍` 標明）
- **Breadcrumb 文案：** `> 專案首頁 / 細綱 / 完整視圖`（或 `> 專案首頁 / 細綱 / 章節 CH<n>` 若傳參數）

### Source 反查預期（D13 — 含 D-054 hybrid）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `05_plot/05_b_章節結構模板.md` | CH-* entries (含 CH 摘要) | "## 章節 CH<n>：<chapter_name>" 各章節層 |
| `06_scene_index/06_a_場景索引模板.md` | S-*-* row（聚合 mode；含 split-to-file marker）| 各章節層內 "### 場景 S-<ch>-<n>" 子段 |
| `06_scene_index/CH<n>_S<m>_<scene_name>.md`（per-scene 拆檔；若存在）| 個別場景內容（D-054 hybrid fallback） | 各章節層內 "### 場景 S-<ch>-<n>" 子段（per-scene 檔優先讀；否則 fallback 06_a row）|

**D-054 hybrid fallback 讀檔（D13 必含 — 同 D9 /view-detailed-outline + /scene-task v0.1 邏輯）：**

對每個 S-<ch>-<n>：
1. 先 check `06_scene_index/CH<n>_S<m>_<scene_name>.md` 是否存在
2. 存在 → 讀 per-scene 檔（優先）
3. 不存在 → fallback 讀 `06_a` 對應 row
4. 兩者皆無 → 寫入「[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]」placeholder（**整合檔不中止；仍寫但缺漏段標 placeholder**）

### 組合結構（D13）

```markdown
狀態：DERIVED  
版本：<對應 source 的最高版本>  
最後更新：<YYYY-MM-DD>  
適用範圍：細綱整合視圖（CH=<指定 CH 或全部>）  
優先級：中  
生成方式：/export-detailed-outline
組合來源:
  - 05_plot/05_b_章節結構模板.md
  - 06_scene_index/06_a_場景索引模板.md
  - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene 拆檔（D-054 hybrid）

> 專案首頁 / 細綱 / 完整視圖

## 目錄 / Contents
<僅當 > 200 行；GFM slug；skill 內驗 P-005>

# 細綱 — /export-detailed-outline 靜態整合檔（CH=<指定 CH 或全部>）

## 章節 CH<n>：<chapter_name>

<05_b CH-<n> entry 摘要>

### 場景 S-<n>-<m>：<scene_name>
<per-scene 檔內容 或 06_a row 內容（D-054 hybrid）>
*來源：[/06_scene_index/CH<n>_S<m>_<scene_name>.md](/06_scene_index/CH<n>_S<m>_<scene_name>.md) (per-scene) 或 [/06_scene_index/06_a_場景索引模板.md](/06_scene_index/06_a_場景索引模板.md) row*

### 場景 S-<n>-<m+1>：<scene_name>
<...>

## 章節 CH<n+1>：<chapter_name>
<...>

---

[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)
```

### 啟動前檢查（D13 — 加 CH-ID 參數驗證 + D-054 fallback ready）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 / Bootstrap | 同 D10 | 同 D10 |
| **CH-<n> / S-*-* 存在**（若 user 傳 CH-ID 參數）| 對應 05_b CH-<n> entry 或 06_a row 或 per-scene 檔；任一 | 拒絕並提示用 /create-detailed-outline 建立 |
| **不傳參數 = 寫全部章節整合檔** | 至少有 1 個 CH-* 存在於 05_b | 拒絕並提示用 /create-detailed-outline 建立 |
| **`view/` 目錄存在或可建立** | 同 D10 | 同 D10 |

### phase_log entry 範例（D13）

```yaml
- phase: export-detailed-outline
  date: YYYY-MM-DD
  skill: /export-detailed-outline
  status: completed
  target_entity: CH-<n>  # 或 "all" 若不傳參數
  scope_choice: <CH-<n>>  # 或 "all_chapters"
  read_sources:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
    - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene 拆檔 list（D-054 hybrid fallback）
  d054_per_scene_files_detected: [<list>]  # 本輪 detect 的 per-scene 檔
  output_path: view/細綱.md
  output_lines: <整合檔實際行數>
  breadcrumb_added: true
  toc_added: <true|false>
  slug_validation_result: <pass|fixed>
  customizations: []
```

---

# 5. 中文 wrapper SKILL.md 結構（3 個 wrapper — 同 D10 極簡模式）

每個 wrapper 結構：

```markdown
---
name: <中文 wrapper name 如 匯出角色>
description: "<英文 skill> skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：<英文 skill> skill 中文觸發 wrapper  
優先級：中

# /<中文 wrapper>（/<英文 skill> wrapper）

本 wrapper 是 `/<英文 skill>` 的中文別名。執行時以英文主檔 `.claude/skills/<英文 skill>/SKILL.md` 為權威。

請參考 `.claude/skills/<英文 skill>/SKILL.md`。
```

對應 3 個 wrapper：
- `/匯出角色` → `/export-character`
- `/匯出大綱` → `/export-outline`
- `/匯出細綱` → `/export-detailed-outline`

---

# 6. CODEX 工作流程

1. **讀必讀 spec**（按順序；含 D10 共通範本）：
   - `_design/CODEX_D10_STARTER.md` v0.1（共通範本；先讀）
   - `_design/TASKS.md` v1.9 §C.5
   - `_design/ARCHITECTURE.md` v1.6 §4.2（/export-* 靜態整合檔；DERIVED frontmatter 範本）+ §4.3（跨檔導航統一規則）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema — 注意 DERIVED 用「生成方式 + 組合來源」延伸欄位）+ §13.4（分享階段：靜態整合檔 B 模式）+ §16（DERIVED `view/` 目錄專用）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則 — 跨檔 link / source 引用 / breadcrumb / TOC / slug）
   - `.claude/skills/export-world/SKILL.md` v0.1（D10 落地的 export-world 參考；D11-D13 結構對齊）
   - `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid fallback；**D13 必含**此 logic）
   - `.claude/skills/view-detailed-outline/SKILL.md` v0.1（含 D-054 hybrid fallback；D13 對照範本）
   - `.claude/skills/scene-task/SKILL.md` v0.1（含 D-054 fallback；D13 hybrid 讀檔範本）
   - `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 子裁決 1+2（寫檔目錄表）+ §6.16.2 D-053 + P-004（/view/README.md）+ P-005（slug 一致性）

2. **寫 6 個 SKILL.md**（依本 starter §1 任務目標表 + §2/§3/§4 差異規格 + §5 wrapper 結構）：
   - 先寫 D11 (/export-character + /匯出角色)
   - 再寫 D12 (/export-outline + /匯出大綱)
   - 最後寫 D13 (/export-detailed-outline + /匯出細綱；**含 D-054 hybrid fallback**)

3. **跑 baseline 驗證**：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - 對齊 9th master 第一段 Round 1-4 收尾後 baseline：`check_paths ≤ 247 ERROR`（Windows 端權威）
   - DERIVED 加入 `check_headers.py VALID_STATUS` 不在本 task scope（ARCH §4.2 line 773 註「Phase C 同步更新」屬未來 patch）

4. **不跑真實 export-* skill 寫檔**（Template 內無 Instance entity 也無 `view/` 目錄）

5. **撰寫 batch report**（可選；推 9th master 第二段對話 Wave 14 整體驗收 starter）

---

# 7. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | baseline | check_paths ≤ 247；無新真實 ERROR |
| 2. SKILL.md 落地 | 6 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 結構對齊 D10 範本 | 3 個英文主檔 11 段結構齊全；3 個 wrapper 極簡模式 | 對齊 D10 |
| 4. 5 階段 + DERIVED frontmatter + 呈現規則 | 各 SKILL.md 含 5 階段對齊 ARCH §4.2 + DERIVED frontmatter 範本（7 欄；對齊 line 753-769）+ 呈現規則對齊 §4.3 | 完整 |
| 5. Breadcrumb / TOC / 返回連結 | 各 SKILL.md 明示位置 + 格式 + 觸發條件（TOC > 200 行 / slug 一致性 P-005 / 末尾返回連結 P-004）| 對齊 ARCH §4.2-§4.3 |
| 6. 邊界三 block | 各 SKILL.md 含 D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表三 block 完整（**寫檔目錄表 limit 寫 view/<entity>.md 對應檔**）| 與 view-* 純讀取邊界 7 條模式不同 |
| 7. **D-054 hybrid fallback (D13 only)** | /export-detailed-outline 含 D-054 兩階段 fallback：先 check per-scene 檔；fallback 06_a row；兩者皆無 → placeholder 不中止 | 對齊 D054_DECISION_PACKAGE v0.2 + view-detailed-outline v0.1 + scene-task v0.1 |
| 8. phase_log entry 規範 | 3 個英文主檔含 phase_log entry 範例（必寫；含 `output_path` + `output_lines` + `breadcrumb_added` + `toc_added` + `slug_validation_result` + `read_sources`）| 對齊 export-* 寫檔 audit pattern |
| 9. 兩條 export 路徑區分 | 各 SKILL.md 明示「不實作 §4.2a Layer 3 Export A1 prompt 生成器」| 對齊 ARCH §4.2a.4 區分表 |

---

# 8. 邊界與紀律提醒（給 CODEX — 沿用 D10 + 9th master 第一段 5 條教訓）

- **不**寫 `view/` 目錄以外任何檔（除 `.protocol_version.phase_log` audit）
- **不**升 entity 狀態
- **不**呼叫其他 skill（包括 /view-* 系列 — 本 skill 共用組合邏輯但不 chain call）
- **不**改 LOCKED spec / registry / parser / 既有 32 個 SKILL.md（含 export-world v0.1）
- **不**動 `scripts/check_headers.py` VALID_STATUS（屬 Phase A.0F / 10th master scope）
- **不**實作 §4.2a Layer 3 Export A1 prompt 生成器（屬 Phase A.0F.x / 10th master scope）
- **不**改 00_j / 00_k / 任何 protocol
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE

「Fix one, find two」cascade pattern 預防 + 9th master 5 條教訓內化（沿用 D10 §4）：

- 寫好 6 個 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 / file path / D-NNN 引用 / 兩條 export 路徑混用 wording）
- 寫 path reference 前先 ls 實際 repo 對齊（特別 D13 的 D-054 per-scene 檔路徑 + view/ 寫檔目標）
- 寫 SPEC frontmatter 引用前直接 grep SPEC §5.2 verify（DERIVED 用延伸欄位非 standard YAML block）
- 寫 supersede note（如有）避免重複 finding 內精確詞串
- Wave 14 不跑 CODEX review starter（master 內部 verify；Wave 16 才動用完整 CODEX review）— 不必寫 review report

---

# 9. Cross-ref

- `_design/CODEX_D10_STARTER.md` v0.1（共通範本；先讀）
- `_design/TASKS.md` v1.9 §C.5
- `_design/ARCHITECTURE.md` v1.6 §4.2（/export-* 靜態整合檔；DERIVED frontmatter 範本）+ §4.2a（L3 Export A1 prompt 生成器；separate path；本 Wave 不實作）+ §4.3（跨檔導航統一規則）
- `_design/SPEC.md` v1.2 §5.2 + §13.4 + §13a + §16
- `_design/UX_SPEC.md` v0.4 §7
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（Layer 3 Export prompt schema；本 batch **不**實作，僅 reference）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 設計推理；D13 必含）
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 子裁決 1+2 + §6.16.2 D-053 + §6.17 D-054 + P-004 + P-005
- `.claude/skills/export-world/SKILL.md` v0.1（D10 落地；D11-D13 結構對齊）
- `.claude/skills/view-detailed-outline/SKILL.md` v0.1（含 D-054 hybrid fallback；D13 對照範本）
- `.claude/skills/scene-task/SKILL.md` v0.1（D-054 hybrid 讀檔範本；D13 對照）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master 第一段 Round 1-4 收尾 + 5 條教訓內化）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話 scope）
