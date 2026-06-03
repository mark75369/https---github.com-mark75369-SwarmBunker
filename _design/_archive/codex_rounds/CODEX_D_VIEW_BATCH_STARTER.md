狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 13 batch task — D7 (/view-character) + D8 (/view-outline) + D9 (/view-detailed-outline) skill 實作（採 batch 模式 — CODEX 一輪寫 3 個 starter 的 6 個 SKILL.md）  
優先級：高

# CODEX_D_VIEW_BATCH_STARTER — Phase D Wave 13 batch task (D7-D9)

# 0. 本檔用途

Phase D Wave 13 後 3 條 task — CODEX 在乾淨對話一次寫 D7 (/view-character) + D8 (/view-outline) + D9 (/view-detailed-outline) 三個 view-* skill（共 6 個 SKILL.md：3 個英文主檔 + 3 個中文 wrapper）。

**前置條件：** D.6 (/view-world) PASS（已建 master 端 starter 範本 `_design/CODEX_D6_STARTER.md` v0.1）+ CODEX 已熟悉 view-* 共通設計。

**Wave 13 工作模式（9th master 新模式 — 對應 Wave 12 後教訓內化）：**
- Master 寫 D6 完整 starter（共通範本；已落地 v0.1）
- Master 寫本 batch starter（CODEX_D_VIEW_BATCH_STARTER.md；本檔）
- CODEX 在乾淨對話跑本 batch starter → 寫 D7/D8/D9 三個 starter 的 6 個 SKILL.md
- Master review 4 個 view-* SKILL.md 一致性（或寫 Wave 13 review starter 給 CODEX 跑）

⚠ **本檔 = 給 CODEX 跑 batch task 的指引**：CODEX 拿本檔 + D6 starter + 必讀 spec → 一次寫 D7/D8/D9 的 6 個 SKILL.md。

⚠ **view vs export 邊界（同 D6）：** view 純讀取；不寫檔；不寫 view/ 整合檔（屬 Wave 14 scope）。

⚠ **慣例：** outer agent-prompt fence 用 `~~~`；Instance-only path 前綴 `<instance_root>/`。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 13 batch task (D7-D9)」— 實作 3 個 view-* skill：/view-character + /view-outline + /view-detailed-outline（含 3 個中文 wrapper；共 6 個 SKILL.md）；對齊 TASKS v1.9 §C.3 + ARCH v1.6 §4.1 動態組合 + §4.4 呈現規則 + UX_SPEC §7。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**共通範本：** 本 task 採與 D6 (/view-world) 相同的 starter pattern。**先讀 `_design/CODEX_D6_STARTER.md` v0.1** 對齊：
- 主 SKILL.md 結構（11 段：frontmatter + 中文 5 header + 用途 / 觸發語 / 觸發協議 / 啟動前檢查 / 流程 / 呈現規則 / phase_log / 輸入 / 輸出 / 邊界 / 錯誤處理 / 錯誤呈現）
- 5 階段流程（適配 view：診斷 / 反查 source / 組合 / 呈現 / 驗證）
- 呈現規則（chat 動態組合不加 breadcrumb；source italic；跨檔 link / 開頭；單向 reference）
- phase_log entry 範例（可選寫；含 `read_sources` + `output_target: chat`）
- 啟動前檢查 4 項（D-049 + Bootstrap + 目標 entity ≥ DRAFT 存在；不要求 ≥ REVIEW）
- 純讀取邊界 7 條（不寫檔 / 不寫 view/ 整合檔 / 不擴 source / 不升 entity / 不擅自呼叫其他 view-* / 不擅自重新組織 source / 不寫 LOCKED）
- 中文 wrapper 極簡模式

依下方「D7-D9 各 skill 差異規格」針對每個 skill 修改 entity 類型 / source 範圍 / 組合結構 / 觸發語。

**你的身份與職責：**
- 你是 implementer — 本輪建 6 個新 SKILL.md（3 英文主檔 + 3 中文 wrapper）
- D7-D9 batch PASS → Wave 13 整體 PASS；可進 Wave 14（/export-* 系列）

**重要邊界（沿用 D6 + batch）：**
- ✗ 不改 LOCKED spec / registry / parser
- ✗ 不改既有 24 個 SKILL.md（含 /view-world + /查看世界觀 — D6 剛建；本輪不改）
- ✗ 不寫 /export-* (Wave 14 scope) / /diagnose / /integrate (Wave 15 scope)
- ✗ 不寫任何 view/<entity>.md 整合檔
- ✗ 不改 00_j / 00_k / 任何 protocol
- ✗ 不改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE

### 任務目標（6 個 SKILL.md — batch 寫完）

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/view-character/SKILL.md` | 英文主檔（D7）|
| 2 | `.claude/skills/查看角色/SKILL.md` | 中文 wrapper |
| 3 | `.claude/skills/view-outline/SKILL.md` | 英文主檔（D8）|
| 4 | `.claude/skills/查看大綱/SKILL.md` | 中文 wrapper |
| 5 | `.claude/skills/view-detailed-outline/SKILL.md` | 英文主檔（D9）|
| 6 | `.claude/skills/查看細綱/SKILL.md` | 中文 wrapper |

---

# 2. D7 (/view-character) 差異規格（vs D6）

- **觸發語：** `/view-character <name>`（**接 1 user 參數** — 角色名）
- **對應 protocol：** 無（view 屬純技術 skill）
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取單一 C-<name>）
- **依賴：** C-<name> 至少 DRAFT 存在；不要求 ≥ REVIEW
- **下游：** 階段 5 印「下一步建議：持久化整合檔請跑 /export-character <name>；修改角色請跑 /iterate-character <name>」

### Source 反查預期（D7）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `03_characters/main/<name>_聲線卡.md` 或 `03_characters/minor/<name>_*.md` 或 `03_characters/npc/<name>_*.md` | C-<name> 主聲線卡（依 frontmatter entities 反查實際路徑）| "## 聲線卡" 段 |
| `04_relationships/04_a_角色關係矩陣.md` | 含 R-<name>-* / R-*-<name> 的關係 entry | "## 關係" 段（grep entities `R-<name>-*` 或 `R-*-<name>` 的 entry section）|
| `04_relationships/04_b_關係變化時間線.md` | 含本角色的時間線 entry | "## 時間線" 段（grep 本角色 reference 的 entry section）|
| `05_plot/05_c_角色弧線表.md` | 含本角色的弧線階段 | "## 弧線" 段（grep 本角色 entries section）|
| `06_scene_index/06_a_場景索引模板.md` + 已存在 per-scene 拆檔（D-054 hybrid fallback）| 含本角色出場場景列表 | "## 出場場景" 段（grep entities 含 C-<name> 的 S-*-* row）|

**抽取段落依據（依 ARCH §4.1 line 740）：** 透過 entities `C-<name>` 或 `R-<name>-*` / `R-*-<name>` 在 frontmatter 中的對應，或透過文件內 `## <角色名>` 等 anchor。

### 組合結構（D7）

```markdown
# 角色：<name> — /view-character 動態整合視圖

## 聲線卡
<03_characters/.../$name 聲線卡內容>
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
<06_a (或 per-scene 拆檔) 抽取本角色出場 S-*-* 列表>
*來源：[/06_scene_index/06_a_場景索引模板.md](/06_scene_index/06_a_場景索引模板.md) (含 per-scene 拆檔；D-054 hybrid)*

---

**下一步建議：**
- 持久化整合檔 → /export-character <name>
- 修改角色 → /iterate-character <name>
- 修改關係 → /iterate-relationship <name> <other>
```

### 啟動前檢查（D7 — 加 C-<name> 存在檢查）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 / Bootstrap | 同 D6 | 同 D6 |
| **C-<name> 存在** | `03_characters/.../<name>_*.md` frontmatter 含 `entities: [C-<name>]`；狀態 ≥ DRAFT | 拒絕並提示用 /create-character <name> 建立 |

### phase_log entry 範例（D7）

```yaml
- phase: view-character
  date: YYYY-MM-DD
  skill: /view-character
  status: completed
  target_entity: C-<name>
  read_sources:
    - 03_characters/main/<name>_聲線卡.md  # 或對應 minor/npc 路徑
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_c_角色弧線表.md
    - 06_scene_index/06_a_場景索引模板.md  # + per-scene 拆檔 list（D-054 hybrid）
  output_lines: <估算組合輸出行數>
  output_target: chat
  customizations: []
```

---

# 3. D8 (/view-outline) 差異規格（vs D6）

- **觸發語：** `/view-outline`（不接 user 參數）
- **對應 protocol：** 無
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取 P）
- **依賴：** P 至少 DRAFT 存在
- **下游：** 階段 5 印「下一步建議：持久化請跑 /export-outline；修改主線請跑 /iterate-outline」

### Source 反查預期（D8）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `05_plot/05_a_主線大綱模板.md` | P 主分拆 | "## 主線結構" 段 |
| `05_plot/05_b_章節結構模板.md` | CH-* entries | "## 章節結構" 段 |
| `05_plot/05_c_角色弧線表.md` | 角色弧線階段 | "## 角色弧線" 段 |
| `05_plot/05_d_資訊揭露表.md` | 章節揭露順序 | "## 資訊揭露" 段 |
| `05_plot/05_e_伏筆與回收表.md` | 伏筆與回收 | "## 伏筆與回收" 段 |

### 組合結構（D8）

```markdown
# 大綱 — /view-outline 動態整合視圖

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

**下一步建議：**
- 持久化整合檔 → /export-outline
- 修改主線 → /iterate-outline
- 修改章節細綱 → /iterate-detailed-outline
```

### phase_log entry 範例（D8）

```yaml
- phase: view-outline
  date: YYYY-MM-DD
  skill: /view-outline
  status: completed
  target_entity: P
  read_sources:
    - 05_plot/05_a_主線大綱模板.md
    - 05_plot/05_b_章節結構模板.md
    - 05_plot/05_c_角色弧線表.md
    - 05_plot/05_d_資訊揭露表.md
    - 05_plot/05_e_伏筆與回收表.md
  output_lines: <估算>
  output_target: chat
  customizations: []
```

---

# 4. D9 (/view-detailed-outline) 差異規格（vs D6；含 D-054 hybrid fallback 讀檔）

- **觸發語：** `/view-detailed-outline` 或 `/view-detailed-outline <CH-ID>`（**可選 1 user 參數** — 章節 ID；若不傳 = 顯示全部章節）
- **對應 protocol：** 無
- **議題清單動態載入：** 不適用
- **modify entity 範圍：** 無（純讀取 CH-* / S-*-*）
- **依賴：** CH-* / S-*-* 至少 DRAFT 存在（透過 05_b 或 06_a 反查）
- **下游：** 階段 5 印「下一步建議：持久化請跑 /export-detailed-outline；修改章節請跑 /iterate-detailed-outline <CH-ID>；單場 split 請跑 /iterate-scene <S-ID> --split-to-file」

### Source 反查預期（D9 — 含 D-054 hybrid）

| Source | 內容 | 在組合視圖內的位置 |
|---|---|---|
| `05_plot/05_b_章節結構模板.md` | CH-* entries (含 CH 摘要) | "## 章節 CH<n>：<chapter_name>" 各章節層 |
| `06_scene_index/06_a_場景索引模板.md` | S-*-* row（聚合 mode；含 split-to-file marker）| 各章節層內 "### 場景 S-<ch>-<n>" 子段 |
| `06_scene_index/CH<n>_S<m>_<scene_name>.md`（per-scene 拆檔；若存在）| 個別場景內容（D-054 hybrid fallback） | 各章節層內 "### 場景 S-<ch>-<n>" 子段（per-scene 檔優先讀；否則 fallback 06_a row）|

**D-054 hybrid fallback 讀檔（D9 必含 — 同 /scene-task v0.1 邏輯）：**

對每個 S-<ch>-<n>：
1. 先 check `06_scene_index/CH<n>_S<m>_<scene_name>.md` 是否存在
2. 存在 → 讀 per-scene 檔（優先）
3. 不存在 → fallback 讀 `06_a` 對應 row
4. 兩者皆無 → 印「[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]」placeholder

### 組合結構（D9）

```markdown
# 細綱 — /view-detailed-outline 動態整合視圖（CH=<指定 CH 或全部>）

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

**下一步建議：**
- 持久化整合檔 → /export-detailed-outline
- 修改章節 → /iterate-detailed-outline <CH-ID>
- 單場拆檔 → /iterate-scene <S-ID> --split-to-file
- 修改主線 → /iterate-outline
```

### 啟動前檢查（D9 — 加 CH-ID 參數驗證）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 / Bootstrap | 同 D6 | 同 D6 |
| **CH-<n> / S-*-* 存在**（若 user 傳 CH-ID 參數）| 對應 05_b CH-<n> entry 或 06_a row 或 per-scene 檔；任一 | 拒絕並提示用 /create-detailed-outline 建立 |
| **不傳參數 = 顯示全部** | 至少有 1 個 CH-* 存在於 05_b | 拒絕並提示用 /create-detailed-outline 建立 |

### phase_log entry 範例（D9）

```yaml
- phase: view-detailed-outline
  date: YYYY-MM-DD
  skill: /view-detailed-outline
  status: completed
  target_entity: CH-<n>  # 或 "all" 若不傳參數
  scope_choice: <CH-<n>>  # 或 "all_chapters"
  read_sources:
    - 05_plot/05_b_章節結構模板.md
    - 06_scene_index/06_a_場景索引模板.md
    - 06_scene_index/CH<n>_S<m>_<scene_name>.md  # per-scene 拆檔 list（D-054 hybrid fallback）
  d054_per_scene_files_detected: [<list>]  # 本輪 detect 的 per-scene 檔
  output_lines: <估算>
  output_target: chat
  customizations: []
```

---

# 5. 中文 wrapper SKILL.md 結構（3 個 wrapper — 同 D6 極簡模式）

每個 wrapper 結構：

```markdown
---
name: <中文 wrapper name 如 查看角色>
description: "<英文 skill> skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：<英文 skill> skill 中文觸發 wrapper  
優先級：中

# /<中文 wrapper> （/<英文 skill> wrapper）

本 wrapper 是 `/<英文 skill>` 的中文別名。執行時以英文主檔 `.claude/skills/<英文 skill>/SKILL.md` 為權威。

請參考 `.claude/skills/<英文 skill>/SKILL.md`。
```

對應 3 個 wrapper：
- `/查看角色` → `/view-character`
- `/查看大綱` → `/view-outline`
- `/查看細綱` → `/view-detailed-outline`

---

# 6. CODEX 工作流程

1. **讀必讀 spec**（按順序；含 D6 共通範本）：
   - `_design/CODEX_D6_STARTER.md` v0.1（共通範本；先讀）
   - `_design/TASKS.md` v1.9 §C.3
   - `_design/ARCHITECTURE.md` v1.6 §4.1（/view-character 動態組合 line 724-740）+ §4.4（呈現規則）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則）
   - `.claude/skills/view-world/SKILL.md` v0.1（D6 落地的 view-world 參考；D7-D9 結構對齊）
   - `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid fallback；D9 必含此 logic）
   - `.claude/skills/scene-task/SKILL.md` v0.1（含 D-054 fallback；D9 hybrid 讀檔範本）

2. **寫 6 個 SKILL.md**（依本 starter §1 任務目標表 + §2/§3/§4 差異規格 + §5 wrapper 結構）：
   - 先寫 D7 (/view-character + /查看角色)
   - 再寫 D8 (/view-outline + /查看大綱)
   - 最後寫 D9 (/view-detailed-outline + /查看細綱；含 D-054 hybrid fallback)

3. **跑 baseline 驗證**：對齊 9th master Round 1-4 收尾後 baseline（check_paths ≤ 247）

4. **不跑真實 view-* skill 寫檔**（Template 內無 Instance entity）

5. **撰寫 batch report**（可選；推 9th master Wave 13 整體驗收 starter）

---

# 7. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | baseline | check_paths ≤ 247；無新 ERROR |
| 2. SKILL.md 落地 | 6 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 結構對齊 D6 範本 | 3 個英文主檔 11 段結構齊全；3 個 wrapper 極簡模式 | 對齊 D6 |
| 4. 5 階段 + 呈現規則 | 各 SKILL.md 含 5 階段對齊 ARCH §4.1 + 呈現規則對齊 §4.4 | 完整 |
| 5. 純讀取邊界 7 條 | 各 SKILL.md 含「邊界區段（純讀取邊界）」7 條完整 | 一致 |
| 6. **D-054 hybrid fallback (D9 only)** | /view-detailed-outline 含 D-054 兩階段 fallback：先 check per-scene 檔；fallback 06_a row | 對齊 D054_DECISION_PACKAGE v0.2 + scene-task v0.1 |
| 7. phase_log entry 規範 | 3 個英文主檔含 phase_log entry 範例（含 read_sources + output_target: chat）| 對齊 D6 |

---

# 8. 邊界與紀律提醒（給 CODEX — 沿用 D6 + 教訓 5 條）

- **不**寫任何檔（除可選 phase_log audit entry）
- **不**寫 view/ 整合檔（屬 Wave 14 /export-* scope）
- **不**升 entity 狀態
- **不**呼叫其他 skill
- **不**改 LOCKED spec / registry / parser / 既有 24 個 SKILL.md（含 view-world v0.1）
- **不**改 00_j / 00_k / 任何 protocol
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING

「Fix one, find two」cascade pattern 預防 + 9th master 5 條教訓內化（沿用 D6 §4）：

- 寫好 6 個 SKILL.md 後跑 grep 全掃 stale cross-ref
- 寫 path reference 前先 ls 實際 repo 對齊（特別 D9 的 D-054 per-scene 檔路徑）
- 寫 SPEC frontmatter 引用前直接 grep SPEC §5.2 verify
- 寫 supersede note（如有）避免重複 finding 內精確詞串

---

# 9. Cross-ref

- `_design/CODEX_D6_STARTER.md` v0.1（共通範本；先讀）
- `_design/TASKS.md` v1.9 §C.3
- `_design/ARCHITECTURE.md` v1.6 §4.1 + §4.4
- `_design/SPEC.md` v1.2 §5.2
- `_design/UX_SPEC.md` v0.4 §7
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 設計推理；D9 必含）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054
- `.claude/skills/scene-task/SKILL.md` v0.1（D-054 hybrid 讀檔範本；D9 對照）
- `.claude/skills/view-world/SKILL.md` v0.1（D6 落地；D7-D9 結構對齊）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master Round 1-4 收尾 + 5 條教訓內化）
