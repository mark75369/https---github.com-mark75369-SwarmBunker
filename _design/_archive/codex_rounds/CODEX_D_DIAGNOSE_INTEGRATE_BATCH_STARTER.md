狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 15 batch task — D15 (/integrate) skill 實作（依 D14 /diagnose 範本批次寫；含中文 wrapper）  
優先級：高

# CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER — Phase D Wave 15 batch task (D15)

# 0. 本檔用途

Phase D Wave 15 後 1 條 task — CODEX 在乾淨對話寫 D15 `/integrate` skill（含中文 wrapper；共 2 個 SKILL.md：1 個英文主檔 + 1 個中文 wrapper）。

**前置條件：** D.14 (/diagnose) PASS（已建 master 端 starter 範本 `_design/CODEX_D14_STARTER.md` v0.1）+ CODEX 已熟悉 diagnose-* / integrate-* 共通設計（純讀取 vs 寫檔需 user 拍板的差異）。

**Wave 15 工作模式（9th master 第二段對話沿用 Wave 13/14 模式）：**
- Master 寫 D14 完整 starter（共通範本；已落地 v0.1）
- Master 寫本 batch starter（CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md；本檔）
- CODEX 在乾淨對話跑本 batch starter → 寫 D15 (/integrate + /整理) 2 個 SKILL.md
- Master 端內部 verify diagnose-* / integrate-* 系列共 4 個 SKILL.md 一致性（grep 結構 + Read 重點 section；不跑 CODEX review starter — Wave 16 才動用完整 CODEX review）

⚠ **本檔 = 給 CODEX 跑 batch task 的指引**：CODEX 拿本檔 + D14 starter + 必讀 spec → 寫 D15 的 2 個 SKILL.md。

⚠ **/diagnose vs /integrate 邊界差異（關鍵；vs Wave 14 export-* 全寫檔的差異）：**

| 維度 | /diagnose (D.14) | /integrate (D.15；本 batch) |
|---|---|---|
| 對應 protocol | 00_a §3.3 診斷模式 | 00_a §3.4 整理模式 |
| 是否寫檔 | **不寫**（除可選 phase_log audit） | **可寫但必須 user 拍板**（對齊 D-052 紀律 — AI-assisted + user 明示拍板）|
| 寫檔目標 | 無（chat 印報告）| 寫對應 entity 檔 / template 模板欄位（依 user 指定的 target） |
| 邊界 | 純讀取 8 條（對齊 D6 view-world 7 條 + §3.3.3 5 條延伸）| **D-050 三 block + 「寫檔前先印 diff 給 user 拍板」階段** |
| 議題清單動態載入 | 不適用（通用模式）| 不適用（通用模式）|
| 觸發語 | `/diagnose` / `/diagnose <file>` / `/diagnose <inline text>` | `/integrate <target>` / `/integrate <file> --target=<entity>` |
| 5 階段流程 | 診斷準備 / 反查 source / 組合 6 段報告 / 印 chat / phase_log audit | 整理準備 / 反查 source / 組合結構化結論 / **印 diff + 等 user 拍板** / 寫檔 + phase_log |

⚠ **/integrate 對齊 00_a §3.4 為權威：**
- 「使用時機」（line 244-249）：將世界觀文件整理成 01_world / 將角色設定整理成聲線卡 / 將主線大綱整理成章節結構 / 將原始資料抽取成詞彙表 + 關係矩陣 + 資訊揭露表
- 「任務目標」（line 252-261）：把原始資料轉結構化模板欄位；優先保留原始設定意思；不確定內容標 TODO；矛盾內容標 CONFLICT；AI 推測標 INFERENCE
- 「允許事項」（line 264-271）：重新分類資料 / 合併重複內容 / 建立索引表 / 抽取專有名詞陣營地名制度角色關係 / 建議缺漏欄位
- 「禁止事項」（line 274-280）：不為了填滿模板而編造設定 / 不將原始設定改得更戲劇化 / 不自動新增角色死亡背叛血緣結局反派真相 / 不把 DRAFT 內容標 REVIEW / LOCKED

⚠ **Wave 15 不實作 Canon Delta skill**（屬「成熟期功能」；本 Wave 寫 `_design/CANON_DELTA_FRAMEWORK.md` v0.1 framework reference；CODEX **不需**讀此檔；該檔屬 11+ 輪 master 範圍未來實作 reference）。

⚠ **慣例：** outer agent-prompt fence 用 `~~~`；Instance-only path 前綴 `<instance_root>/`。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 15 batch task (D15)」— 實作 /integrate skill（含中文 wrapper；共 2 個 SKILL.md）；對齊 TASKS v1.9 §C.6 + 00_protocol/00_a v0.1 §3.4 整理模式 + ARCH v1.6 §3.3 表（line 693）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
請從 master 分支 pull 最新後讀取。

**Token 不是限制** — 如有需要你可以 spawn 多個次要 CODEX 對話做使用增加品質和效率。例如：可以開子對話跑 grep verify / 對照 00_a §3.4 vs 落地 SKILL.md 的紀律映射 / 對照 D-050 三 block vs integrate 寫檔紀律 / 對照 D-052 AI-assisted + user 拍板紀律是否完整實作，再回主對話彙整。優先選擇能提升品質的工作切分。

**共通範本：** 本 task 採與 D14 (/diagnose) 相同的 starter pattern 為基礎，**但寫檔紀律完全不同**。**先讀 `_design/CODEX_D14_STARTER.md` v0.1** 對齊：
- 主 SKILL.md 結構（11 段：frontmatter + 中文 5 header + 用途 / 觸發語 / 觸發協議 / 啟動前檢查 / 流程 / 呈現規則 / phase_log / 輸入 / 輸出 / 邊界 / 錯誤處理 / 錯誤呈現）
- 中文 wrapper 極簡模式

依下方「D15 /integrate 差異規格」針對 5 階段流程 / 邊界 / 寫檔紀律修改。

**你的身份與職責：**
- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- D15 PASS → Wave 15 整體 PASS（D14 已 PASS + D15 PASS + Canon Delta framework master 端已寫）；可進 Wave 16（Phase D 整體驗收）

**重要邊界（沿用 D14 + batch + integrate-specific）：**
- ✗ 不改 LOCKED spec / registry / parser
- ✗ 不改既有 40 個 SKILL.md（含 D14 的 /diagnose + /診斷 — 本輪不改；含 Wave 14 的 4 個 /export-* + 4 個中文 wrapper；含 Wave 13 view-* / 中文 wrapper；含 Phase A/B/C 所有 SKILL.md）
- ✗ 不改 00_a / 00_b / 00_c / 00_j / 00_k / 任何 protocol（00_a 是本 skill 對應 protocol；只讀為權威）
- ✗ 不寫 view/<entity>.md / export/<...>（屬 Wave 14 /export-* + §4.2a L3 Export scope）
- ✗ 不實作 Canon Delta skill（屬「成熟期功能」；本 Wave master 端已寫 `_design/CANON_DELTA_FRAMEWORK.md` v0.1；CODEX 不必讀也不擴 framework；屬 11+ 輪 master 範圍）
- ✗ 不改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE / CANON_DELTA_FRAMEWORK

### 任務目標（2 個 SKILL.md — batch 寫完）

| # | 路徑 | 主檔 / wrapper | 寫檔紀律 |
|---|---|---|---|
| 1 | `.claude/skills/integrate/SKILL.md` | 英文主檔（D15）| **可寫但必須 user 拍板**（對齊 D-052 紀律 — AI-assisted + user 明示拍板）|
| 2 | `.claude/skills/整理/SKILL.md` | 中文 wrapper | — |

---

# 2. D15 (/integrate) 差異規格（vs D14 /diagnose）

### 對應 protocol

- **/integrate 對應 `00_protocol/00_a v0.1 §3.4 整理模式`**（line 240-280）為權威
- 本 skill 不修改 00_a；只讀為權威；是 §3.4 的 Phase D 階段 runtime 實踐

### 觸發語

- **`/integrate <target>`**：把素材整理成指定 entity 目標（target = `world` / `character` / `relationship` / `outline` / `detailed-outline` / `vocabulary` 等；對齊 00_a §3.4.1 使用時機列舉）
- **`/integrate <file> --target=<entity>`**：把指定 file 內容整理到指定 entity 目標
- 中文 wrapper：`/整理 <target>` 或 `/整理 <file> --target=<entity>`

### 議題清單動態載入

不適用（/integrate 屬通用模式；不綁特定議題清單 registry）

### modify entity 範圍

依 target 參數決定：
- `--target=world` → 可寫 01_world/ + 02_vocabulary/ + 00_b §1/§2（D-053 例外允許僅限 /create-world；/integrate 對 00_b 仍嚴禁寫）
- `--target=character` → 可寫 03_characters/
- `--target=relationship` → 可寫 04_relationships/
- `--target=outline` → 可寫 05_plot/05_a~e
- `--target=detailed-outline` → 可寫 05_plot/05_b + 06_scene_index/06_a（D-054 hybrid；本 skill 不擅自 split-to-file）
- `--target=vocabulary` → 可寫 02_vocabulary/02_a~c

**所有寫檔動作必須先印 diff 給 user 拍板（對齊 D-052 紀律；user 拍板「採」才實際寫入）**

### 依賴

- 不要求任何 entity 預先存在（/integrate 適用「把原始資料整理進空 Instance」場景）
- **但必須有 target 參數**（不接受「掃廣整理」模式 — 因為「整理」要明確 target 才不會誤寫到錯目錄）

### 下游

階段 5 印「下一步建議」段（如：「跑 /view-<target> 看整理結果 / 跑 /qa 跑品質檢查 / 跑 /iterate-<target> 後續迭代」等可選建議）

### 5 階段流程（適配 integrate）

#### 階段 1：整理準備（read-only diagnostic setup）

agent 開場：

> /integrate <target> 將把素材整理成 <target> 對應的結構化模板欄位（對齊 00_protocol/00_a §3.4 整理模式）。本 skill **寫檔但必須 user 拍板**；agent 先印 diff，等 user 拍板「採」才實際寫入。
> 
> 開始讀取 source...

agent 檢查啟動前條件（D-049 Template-detect + Bootstrap completed + target 參數正確 + target 對應目錄存在或可建立）；任何缺漏拒絕並印缺漏清單。

#### 階段 2：反查 source

依 target 決定讀取範圍：

| target | 讀取範圍 |
|---|---|
| `world` | 既有 01_world/ + 02_vocabulary/ 為參照（若已部分建立）+ user 提供的素材 |
| `character` | 既有 03_characters/ 為參照（C-* 命名衝突檢測）+ user 提供的素材 |
| `relationship` | 既有 04_relationships/ + 03_characters/ entity 為參照 + user 提供的素材 |
| `outline` | 既有 05_plot/05_a~e 為參照 + user 提供的素材 |
| `detailed-outline` | 既有 05_plot/05_b + 06_scene_index/06_a + 既有 per-scene 拆檔（D-054 hybrid）為參照 + user 提供的素材 |
| `vocabulary` | 既有 02_vocabulary/02_a~c 為參照 + user 提供的素材 |

對每個 source / 素材：
- 解析（若 source 有 frontmatter；user 素材可為純文字）
- 對齊 00_a §3.4.2 任務目標：優先保留原始設定意思 / 不確定內容標 TODO / 矛盾內容標 CONFLICT / AI 推測標 INFERENCE

#### 階段 3：組合結構化結論（in-memory；不寫檔）

agent 把素材整理成 target 對應的結構化模板欄位：

```markdown
# 整理結果預覽（/integrate <target>）

## 一、整理摘要

- target: <target>
- 來源素材：<file path 或 inline text excerpt>
- 既有參照：<列出讀取的既有 entity 檔>

## 二、擬寫入的 entity / 模板欄位 diff

### Entry 1: <entity_id 或 template field>

**目標檔：** `<path>`

**擬寫入內容：**

```yaml
entities:
  - <entity>
depends_on:
  - <related>
weight:
  <entity>: <weight>
```

```markdown
<擬寫入的 main content；對齊既有 template 結構>
```

**標記：**
- TODO: <列出不確定內容>
- CONFLICT: <列出矛盾內容；含既有 vs 擬寫入對比>
- INFERENCE: <列出 AI 推測內容>

### Entry 2: ...

（依素材豐富度有 N 個 entry）

## 三、整理紀律對齊（00_a §3.4）

- ✅ 優先保留原始設定意思（未改寫戲劇化）
- ✅ 不確定內容標 TODO
- ✅ 矛盾內容標 CONFLICT
- ✅ AI 推測標 INFERENCE
- ✅ 保留 template 結構
- ✗ 未編造設定 / 未新增死亡背叛血緣結局 / 未把 DRAFT 標 REVIEW

## 四、user 拍板區（必填）

對每個 Entry，user 拍板：

| Entry | 拍板 | 備註 |
|---|---|---|
| Entry 1: <entity_id> | 採 / 棄 / 修改後採 | <user 填> |
| Entry 2: ... | 採 / 棄 / 修改後採 | <user 填> |

**拍板規則：**
- **採**：agent 階段 4 寫入該 entry 對應檔；frontmatter 狀態：DRAFT
- **棄**：agent 階段 4 不寫該 entry；不留 phase_log entry
- **修改後採**：user 提供修改內容；agent 階段 4 改用 user 修改版寫入
```

#### 階段 4：印 diff + 等 user 拍板 + 寫檔

階段 4 拆兩個子階段：

**階段 4a — 印 diff（對齊 D-052 AI-assisted + user 明示拍板紀律）：**

agent 把階段 3 組合的結構化結論 + diff 印 chat，等待 user 拍板。

**階段 4b — 寫檔（user 拍板「採」後才執行）：**

依 user 拍板結果：
- 對每個拍板「採」的 entry → 寫入對應檔（frontmatter 狀態：DRAFT；對齊 SPEC §5.2 frontmatter canonical schema）
- 對每個拍板「棄」的 entry → 不寫；不留 phase_log entry
- 對每個拍板「修改後採」的 entry → 用 user 修改版寫入

**寫檔紀律（對齊 D-050 三 block 寫檔目錄表）：**
- 對 target=world：寫 `01_world/` + `02_vocabulary/`；**不寫 00_protocol/**（D-050 子裁決 1；D-053 例外僅限 /create-world）
- 對 target=character：寫 `03_characters/<main|minor|npc>/`
- 對 target=relationship：寫 `04_relationships/`
- 對 target=outline：寫 `05_plot/05_a~e`
- 對 target=detailed-outline：寫 `05_plot/05_b` + `06_scene_index/06_a`（**本 skill 不擅自 split-to-file**；屬未來 /iterate-scene --split-to-file scope；D-054 hybrid 維持 aggregate 06_a 為預設）
- 對 target=vocabulary：寫 `02_vocabulary/02_a~c`

#### 階段 5：驗證 + 寫 phase_log

階段 5 驗證 + 寫 phase_log：

- 驗證每個寫入檔 frontmatter 對齊 SPEC §5.2
- 驗證每個寫入檔狀態：DRAFT（**不**升 REVIEW / LOCKED — 對齊 00_a §3.4.4 禁止事項）
- 寫 `.protocol_version.phase_log` entry（必寫；含 `target` + `read_sources` + `user_accepted_entries` + `user_rejected_entries` + `user_modified_entries`）
- **不**自動 trigger /status / /check-gaps / /view-* / /iterate-*（user 要跑請手動）
- 印「下一步建議」段（如：「跑 /view-<target> 看整理結果 / 跑 /qa 跑品質檢查 / 跑 /iterate-<target> 後續迭代」等可選建議）

### .protocol_version phase_log entry 範例（必寫；對齊 SPEC §5.4a）

```yaml
- phase: integrate
  date: YYYY-MM-DD
  skill: /integrate
  status: completed
  target: <world|character|relationship|outline|detailed-outline|vocabulary>
  source_input: <file path 或 "inline_text">
  read_sources:
    - <既有參照 source 1>
    - <既有參照 source 2>
  proposed_entries: <N>  # 階段 3 組合的 entry 總數
  user_accepted_entries: <N>  # user 拍板「採」的 entry 數
  user_rejected_entries: <N>  # user 拍板「棄」的 entry 數
  user_modified_entries: <N>  # user 拍板「修改後採」的 entry 數
  written_files:
    - <寫入檔 path 1>
    - <寫入檔 path 2>
  customizations: []
```

### 啟動前檢查（嚴格條件）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在（屬 Instance）| 拒絕並提示用 /init-project |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕並提示用 /init-project |
| **target 參數正確** | `<world|character|relationship|outline|detailed-outline|vocabulary>` 七選一 | 拒絕並提示正確 target 列表 |
| **target 對應目錄存在或可建立** | `01_world/` / `03_characters/` 等存在或 agent 可建立 | 不可建立 → 拒絕並印權限錯誤 |
| 不要求 entity 預先存在 | /integrate 適用「把原始資料整理進空 Instance」場景 | — |
| 不要求下游 pipeline 互鎖檢查 | /integrate 是上游整理；不影響 downstream | — |

### 邊界區段（D-050 三 block + AI-assisted 紀律；對齊 D-052）

`/integrate` 是寫檔 skill（寫對應 entity 檔），但**寫檔前必須 user 拍板**（對齊 D-052 紀律）。邊界對齊 D-050 + D-053 三 block + 加 D-052 紀律：

**Block 1 — D-050 子裁決 1（00_protocol/ 寫入禁制；本 skill 強化）：**

```md
本 skill 不寫 `00_protocol/` 任何檔。

D-050 子裁決 1 規範「所有 /create-* / /iterate-* / /scene-task / /dialogue-write / /qa
skill 嚴禁寫 00_protocol/」；本 skill 同樣適用。

例外（D-053）：/create-world 可寫 00_b §1 §2（Instance-specific section）— 本 skill **不**屬於該例外。
若 user 要用 /integrate --target=world 整理作品類型語氣 / 髒話尺度 → 請改跑 /create-world（D-053 例外）或 /iterate-world。
```

**Block 2 — D-053 紀錄（exception 紀律承接）：**

```md
本 skill 不觸發 D-053 /create-world exception；本 skill 不寫 00_protocol/ 任何段。
若 user 要修改 00_b §1/§2（作品類型語氣 / 髒話尺度），請走 /create-world（D-053 例外）或 /iterate-world（屬 Wave 12 scope）。
```

**Block 3 — D-050 子裁決 2（寫檔目錄表；本 skill 限定）：**

```md
本 skill 寫檔目錄表（依 target 動態決定）：

| 目錄 | 是否寫入 | 條件 |
|---|---|---|
| `01_world/` | 條件 ✅（user 拍板「採」後）| target=world |
| `02_vocabulary/` | 條件 ✅（user 拍板「採」後）| target=world 或 target=vocabulary |
| `03_characters/` | 條件 ✅（user 拍板「採」後）| target=character |
| `04_relationships/` | 條件 ✅（user 拍板「採」後）| target=relationship |
| `05_plot/` | 條件 ✅（user 拍板「採」後）| target=outline 或 target=detailed-outline |
| `06_scene_index/06_a` | 條件 ✅（user 拍板「採」後）| target=detailed-outline；**不寫 per-scene 拆檔（D-054 維持 aggregate 06_a 預設）** |
| `.protocol_version` | ✅ 寫（phase_log entry 追加；user 拍板後）| 寫 phase_log audit entry |
| `00_protocol/` | ✗ 不寫 | 對齊 D-050 子裁決 1 |
| `06_scene_index/CH<n>_S<m>_*.md` | ✗ 不寫（不擅自 split-to-file）| D-054 split-to-file 屬未來 /iterate-scene --split-to-file scope |
| `07_scene_tasks/` ~ `09_quality_assurance/` | ✗ 不寫 | 下游 pipeline 不在本 skill scope |
| `10_art_assets/` | ✗ 不寫 | 不在本 skill scope |
| `view/` / `export/` | ✗ 不寫 | 屬 Wave 14 /export-* + §4.2a L3 Export scope |
| `_design/` | ✗ 不寫 | LOCKED spec 不擅動 |
| `_tools/` / `scripts/` / `_user_manual/` | ✗ 不寫 | 工具與文件層 |
| `archive/` | ✗ 不寫 | 屬補丁歷史 |

**寫 target 對應目錄以外任何檔 → rollback + 拒絕。**
**user 拍板「棄」的 entry → 不寫；不留 phase_log entry。**
```

**Block 4 — D-052 AI-assisted + user 明示拍板紀律（本 skill 特有）：**

```md
本 skill 採 D-052 AI-assisted + user 明示拍板紀律：

1. agent 階段 3 組合結構化結論 → 印 diff（chat 內展示擬寫入內容）
2. agent **不**擅自寫入任何檔；等待 user 拍板
3. user 對每個 entry 拍板「採 / 棄 / 修改後採」
4. agent 階段 4b 依 user 拍板結果寫檔（「採」/「修改後採」才寫；「棄」不寫）
5. user 拍板必須明示記錄在 phase_log entry（`user_accepted_entries` / `user_rejected_entries` / `user_modified_entries` 計數）

不允許：
- agent 擅自寫檔（即使整理結果看起來無害）
- agent 不印 diff 直接寫
- agent 在拍板前升 entity 狀態
- agent 把整理結果標 REVIEW / LOCKED（必為 DRAFT）

對齊 D-052 PHASE_X_COMPLETION_REPORT §6 AI-assisted + user 拍板原型；diff-driven workflow。
```

**Additional boundaries:**

- Do not implement `/diagnose`（屬 D.14 scope；本 skill 不擅 trigger /diagnose）
- Do not implement §4.2a Layer 3 Export
- Do not implement Canon Delta skill（屬「成熟期功能」；屬 11+ 輪 master scope；本 Wave master 端已寫 `_design/CANON_DELTA_FRAMEWORK.md` v0.1 framework reference；本 skill 不必讀也不擴 framework）
- Do not modify `scripts/`, `_tools/frontend/`, registries, specs, existing skills, or existing templates
- Do not upgrade, downgrade, or otherwise change entity status to REVIEW / LOCKED（必為 DRAFT；對齊 00_a §3.4.4）
- Do not call other skills automatically
- Do not write `LOCKED` source files
- Do not trigger `/iterate-scene --split-to-file`（D-054 維持 aggregate 06_a 預設）

### 中文 wrapper SKILL.md 結構（整理）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 整理
description: "/integrate skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/integrate skill 中文觸發 wrapper  
優先級：中

# /整理（/integrate wrapper）

本 wrapper 是 `/integrate` 的中文別名。執行時以英文主檔 `.claude/skills/integrate/SKILL.md` 為權威。

請參考 `.claude/skills/integrate/SKILL.md`。
```

---

# 3. CODEX 工作流程

1. **讀必讀 spec**（按順序；含 D14 共通範本）：
   - `_design/CODEX_D14_STARTER.md` v0.1（共通範本；先讀；對齊 11 段結構 + 5 階段流程 pattern）
   - `_design/TASKS.md` v1.9 §C.6（/diagnose + /integrate task spec）
   - `00_protocol/00_a_台詞生產協議.md` v0.1 §3.4 整理模式（line 240-280；本 skill 對應 protocol；只讀為權威）+ §3.4.4 禁止事項（line 274-280）
   - `_design/ARCHITECTURE.md` v1.6 §3.3 表（line 693 — /integrate 對應 00_a 整理模式）+ §3.3.1（錯誤呈現規則四件套）+ §4.3（呈現規則）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema — 寫 entity 檔必對齊）+ §5.4a（phase_log entry 新欄位）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則）
   - `.claude/skills/diagnose/SKILL.md` v0.1（D14 落地的 /diagnose 參考；本 skill pattern 對齊 + 邊界差異）
   - `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 子裁決 1+2（寫檔目錄表）+ §6.16.2 D-053（/create-world exception）+ §6.15.2 D-052（AI-assisted + user 明示拍板紀律精神 — 原拍板適用 review gate；本 skill 套用同精神到「寫檔前 user 拍板」）

2. **寫 SKILL.md 2 個**（依本 starter §1 任務目標表 + §2 差異規格）：
   - 英文主檔 `.claude/skills/integrate/SKILL.md`（依本 starter §2 全部設計）
   - 中文 wrapper `.claude/skills/整理/SKILL.md`（依本 starter §2 中文 wrapper 結構）

3. **跑 baseline 驗證**：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - 對齊 9th master 第二段 Wave 14 收尾後 baseline：`check_paths ≤ 247 ERROR`（Windows 端權威）

4. **不跑真實 /integrate 寫檔**（Template repo 內無 Instance entity；本輪 implementer 只寫 SKILL.md 不執行）

5. **撰寫 batch report**（可選；推 9th master 第二段對話 Wave 15 整體驗收 starter）

---

# 4. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | baseline | check_paths ≤ 247；無新真實 ERROR |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 結構對齊 D14 範本 | 1 個英文主檔 11 段結構齊全；1 個 wrapper 極簡模式 | 對齊 D14 |
| 4. 5 階段流程 + 對齊 00_a §3.4 | SKILL.md 含 5 階段（含**階段 4a 印 diff** + **階段 4b 寫檔**兩子階段）+ 整理紀律對齊 00_a §3.4.2/§3.4.3/§3.4.4 | 完整 |
| 5. **D-052 AI-assisted + user 明示拍板紀律** | SKILL.md 含「Block 4 — D-052 AI-assisted + user 明示拍板紀律」段；明示「agent 不擅自寫；等 user 拍板」 | 嚴格對齊 D-052 |
| 6. 邊界四 block | SKILL.md 含 D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表 + D-052 AI-assisted 紀律四 block 完整 | 與 D14 純讀取邊界 8 條不同 |
| 7. phase_log entry 規範 | SKILL.md 含 phase_log entry 範例（必寫；含 `target` + `read_sources` + `proposed_entries` + `user_accepted_entries` + `user_rejected_entries` + `user_modified_entries` + `written_files`）| 對齊 integrate 寫檔 audit pattern |
| 8. D-054 hybrid 保留 | SKILL.md 明示「target=detailed-outline 寫 06_a 但**不擅自 split-to-file**」+「D-054 維持 aggregate 06_a 預設」 | 對齊 Wave 14 D13 + view-detailed-outline 紀律 |
| 9. 跟 /diagnose / Canon Delta 邊界明示 | SKILL.md 邊界區段明示「不擅自 trigger /diagnose」+「不實作 Canon Delta skill」 | 對齊 Wave 15 整體 scope |

---

# 5. 邊界與紀律提醒（給 CODEX — 沿用 D14 + 9th master 第一段 5 條教訓）

- **必須印 diff + 等 user 拍板才寫檔**（D-052 紀律）
- **不**寫 target 對應目錄以外任何檔（除 `.protocol_version.phase_log` audit）
- **不**升 entity 狀態到 REVIEW / LOCKED（必為 DRAFT；對齊 00_a §3.4.4）
- **不**呼叫其他 skill 自動（含 /diagnose / /status / /check-gaps / /view-* / /export-* / /iterate-* / /scene-task / /dialogue-write / /qa / /create-*）
- **不**改 LOCKED spec / registry / parser / 既有 40 個 SKILL.md（含 D14 /diagnose）
- **不**動 `scripts/check_headers.py` VALID_STATUS（屬 Phase A.0F 平行對話 scope）
- **不**實作 §4.2a Layer 3 Export
- **不**實作 Canon Delta skill（屬 11+ 輪 master scope；本 Wave master 端已寫 framework reference）
- **不**改 00_a / 00_b / 00_c / 00_j / 00_k / 任何 protocol
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE / CANON_DELTA_FRAMEWORK
- **不**擅自 trigger `/iterate-scene --split-to-file`（D-054 維持 aggregate 06_a 預設）

「Fix one, find two」cascade pattern 預防 + 9th master 5 條教訓內化（沿用 D14 §4）：

- 寫好 2 個 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 / file path / D-NNN 引用 / D-052 紀律 wording 一致性）
- 寫 path reference 前先 ls 實際 repo 對齊（特別 target 對應目錄的實際 path）
- 寫 SPEC frontmatter 引用前直接 grep SPEC §5.2 verify（/integrate 寫 entity 檔需嚴格對齊 standard YAML block：entities + depends_on + weight）
- 寫 supersede note（如有）避免重複 finding 內精確詞串
- Wave 15 不跑 CODEX review starter（master 內部 verify；Wave 16 才動用完整 CODEX review）

---

# 6. Cross-ref

- `_design/CODEX_D14_STARTER.md` v0.1（共通範本；先讀；對齊 11 段結構 + 5 階段流程 pattern）
- `_design/TASKS.md` v1.9 §C.6
- `00_protocol/00_a_台詞生產協議.md` v0.1 §3.4 整理模式（line 240-280；本 skill 對應 protocol；只讀為權威）
- `_design/ARCHITECTURE.md` v1.6 §3.3 表（line 693）+ §3.3.1 + §4.3
- `_design/SPEC.md` v1.2 §5.2 + §5.4a
- `_design/UX_SPEC.md` v0.4 §7
- `.claude/skills/diagnose/SKILL.md` v0.1（D14 落地；本 skill 共用 11 段結構 + 5 階段 pattern；邊界差異明示）
- `_design/DECISIONS_LOG.md` v2.0 §6.12.2 D-050 子裁決 1+2 + §6.16.2 D-053 + §6.15.2 D-052（AI-assisted + user 明示拍板紀律精神 — 原拍板適用 review gate；本 skill 套用同精神到「寫檔前 user 拍板」）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（Wave 15 master 端 framework reference；本 skill **不必讀也不擴**；屬 11+ 輪 master 範圍）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master 第一段 Round 1-4 收尾 + 5 條教訓內化）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話 scope）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid；本 skill target=detailed-outline 維持 aggregate 06_a 預設）
