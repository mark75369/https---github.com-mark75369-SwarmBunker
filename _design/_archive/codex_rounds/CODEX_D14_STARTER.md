狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 15 task — /diagnose skill + 中文 wrapper 實作（Wave 15 共通範本）  
優先級：高

# CODEX_D14_STARTER — Phase D Wave 15 D.14：/diagnose skill 實作（Wave 15 共通範本）

# 0. 本檔用途

Phase D Wave 15 起手第一條 task — 實作 `/diagnose` skill（跨檔診斷；對應 00_a §3.3 診斷模式 — 只找問題不修）。對齊 TASKS v1.9 §C.6 + 00_protocol/00_a §3.3 + ARCH v1.6 §3.3 表（line 692）。

**前置條件：** 9th master 第二段對話 Wave 14 完成（8 個 /export-* SKILL.md 落地 + L3 schema 對齊備忘）。

**D.14 PASS → Wave 15 進 D.15 batch：** D15 (/integrate) 採 CODEX batch starter 模式（不用 master 逐一寫；本 D14 是共通範本）。

**Wave 15 新工作模式（沿用 Wave 13/14 拍板；9th master 第二段對話內化）：**
- Master 寫 D14 完整 starter（本檔；提供完整 starter pattern + diagnose/integrate 共通設計）
- Master 寫 `CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md`（依 D14 範本批次寫 D15 /integrate）
- CODEX 在乾淨對話跑 batch starter 寫 D15 SKILL.md（含中文 wrapper）
- Master 端內部 verify（grep 結構 + Read 重點 section；不跑 CODEX review starter — Wave 16 才動用完整 CODEX review）

⚠ **diagnose vs integrate vs view/export 邊界（關鍵差異）：**
- `/view-*` (Wave 13)：純讀取單一 entity 視圖；組合後印 chat；不寫檔
- `/export-*` (Wave 14)：與 view 邏輯相同但寫 view/<entity>.md DERIVED 整合檔
- `/diagnose` (本 skill；Wave 15)：**跨檔診斷**（非單一 entity；掃廣 source 找缺漏 / 矛盾 / cross-ref stale / orphan 實體 / view 失效）；組合後印 chat **診斷報告**；不寫檔
- `/integrate` (Wave 15 batch；D.15)：把原始資料轉結構化模板欄位；**可寫檔但必須 user 拍板**（對齊 D-052 紀律 — AI-assisted + user 明示拍板）

⚠ **/diagnose 對齊 00_a §3.3 為權威：**
- 對齊「使用時機」（line 184-190）：初次讀取 / 判斷通用模板適配性 / 找設定缺漏與矛盾 / 判斷哪些通用限制需保留放寬
- 對齊「任務目標」（line 196-204）：作品類型 / 敘事氣質 / 世界語言風格 / 台詞美學需求 / 通用規則適配性 / 需人類確認的問題 / 後續文件整理建議
- 對齊「禁止事項」（line 208-214）：不直接改寫正式模板 / 不擅自補完世界觀 / 不把推測寫成已確認設定 / 不產生 final / locked 文件 / 不直接生成正式台詞
- 對齊「建議輸出格式」（line 218-236）：6 段診斷報告（作品類型與敘事氣質 / 世界語言與台詞風格推測 / 目前資料可確認的內容 / 不可確認 / 需人類確認的內容 / 通用規則適配性 / 建議下一步）

⚠ **Phase D 階段使用情境（不擴 00_a §3.3.4 6 段格式；建議「跨檔健康度檢查」入「六、建議下一步」段）：**

00_a §3.3.4 原意是「作品診斷」格式（適用於初次讀取作品資料）；Phase D 階段使用 /diagnose 也可能含「跨檔健康度檢查」需求（cross-ref stale / LOCKED 變動 propagate / orphan 實體 / view 失效）。

本 skill 採紀律保守設計：
- 主軸對齊 §3.3.4 6 段格式（不擅啟 partial supersede 00_a；新需求屬 Phase D 自然延伸）
- 「五、通用規則適配性」表保留原 3 欄（規則 | 建議 | 原因）— 適配 00_a 原意
- 「六、建議下一步」段內可包含「跨檔健康度建議」（如：「跑 /check-gaps 看 INFERENCE / TODO 累積」「跑 /view-* 看實體 wholeness」「pre-check /qa 之前先跑 /diagnose 預掃」等）
- 若未來需擴 6 段格式 → 屬下一輪 master partial supersede 00_a §3.3.4 範圍；本 Wave 不擅啟

⚠ **9th master 5 條教訓內化（沿用 Wave 13/14）：**
1. Windows baseline 權威：sandbox 比 Windows 少 ~8 ERROR 屬已知 false negative；以 Windows 為準
2. Cascade sweep broader pattern grep：寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 / file path / D-NNN / 兩條 export 路徑混用 wording）
3. SPEC frontmatter 段直接 grep verify：不憑記憶（本 skill 不寫檔；不需 DERIVED frontmatter；但確認其他 spec wording 仍要 grep）
4. Supersede note 避重複精確詞串
5. Review starter diff anchor 精確（本 Wave 不跑 review starter；Wave 16 用）

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only path 前綴 `<instance_root>/`

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase D Wave 15 D.14 task」— 實作 /diagnose skill（含中文 wrapper）；對齊 TASKS v1.9 §C.6 + 00_protocol/00_a v0.1 §3.3 診斷模式 + ARCH v1.6 §3.3 表（line 692）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
請從 master 分支 pull 最新後讀取。

**Token 不是限制** — 如有需要你可以 spawn 多個次要 CODEX 對話做使用增加品質和效率。例如：可以開子對話跑 grep verify / 對照 00_a §3.3 vs 落地 SKILL.md 的紀律映射 / 對照 view-world 邊界 7 條 vs diagnose 邊界，再回主對話彙整。優先選擇能提升品質的工作切分。

**你的身份與職責：**

- 你是 implementer — 本輪建 2 個新 SKILL.md（1 英文主檔 + 1 中文 wrapper）
- 對應傳統：Phase D Wave 15 第一條 task（D.14 → D.15 採 batch 模式）；/diagnose 是 Wave 15 共通範本
- D.14 PASS → 可進 Wave 15 batch（D.15 /integrate 由 CODEX 跑 CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER 在另一個乾淨對話寫）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 38 個 SKILL.md（含 Wave 14 的 4 個 /export-* + 4 個中文 wrapper；含 Wave 13 view-* / 中文 wrapper；含 Phase A/B/C 所有 SKILL.md）
- ✗ **不**改 `00_protocol/00_a v0.1 §3.3 / §3.4` 任何段（00_a 是本 skill 對應 protocol；只讀為權威；不修改）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔（屬 Phase A.0F 平行對話 scope）
- ✗ **不**寫 /integrate（D.15 scope）
- ✗ **不**寫任何 view/<entity>.md / export/<...> 檔（屬 Wave 14 /export-* 與 §4.2a L3 Export scope）
- ✗ **不**寫 entity 檔 / 整理 source 為 frontmatter（屬 /integrate D.15 scope）
- ✗ **不**擅自 trigger 其他 skill（含 /status / /check-gaps / /view-* / /export-* / /iterate-* / /scene-task / /dialogue-write / /qa / /create-* / /integrate）
- ✗ **不**修改 D-001~D-054 / NEW_REQ_15 / 任何 DECISIONS_LOG 拍板紀錄

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.6 + 00_protocol/00_a §3.3 + ARCH v1.6 §3.3 表。

### 任務目標

新建 2 個 SKILL.md：

| # | 路徑 | 主檔 / wrapper |
|---|---|---|
| 1 | `.claude/skills/diagnose/SKILL.md` | 英文主檔 |
| 2 | `.claude/skills/診斷/SKILL.md` | 中文 wrapper |

### /diagnose 主 SKILL.md 結構（11 段；對齊 D6 view-world 純讀取 pattern）

每主 SKILL.md 頂部含：
- frontmatter（name + description 50-200 字；明示「對齊 00_a §3.3 診斷模式 — 跨檔診斷；只分析不改寫；輸出 6 段診斷報告印 chat；不寫檔」）
- 中文 5 必填 header（狀態：DRAFT / 版本：v0.1 / 最後更新：YYYY-MM-DD / 適用範圍：/diagnose skill runtime instructions / 優先級：中）
- markdown 主體含下列段：
  - `## 用途`
  - `## 觸發語`（`/diagnose` + 中文 `/診斷` reference；可選 user-supplied 素材：file path 或 inline text；不必填）
  - `## 觸發協議`（對應 `00_protocol/00_a §3.3 診斷模式` 為權威；不修改 00_a；本 skill 是 §3.3 的 Phase D 階段 runtime 實踐）
  - `## 啟動前檢查`（D-049 Template-detect + Bootstrap completed；不要求任何 entity 存在 — /diagnose 適用「初次讀取」場景）
  - `## 流程`（5 階段：診斷準備 / 反查 source / 在記憶中組合診斷報告 / 印 chat / phase_log audit）
  - `## 呈現規則`（**對齊 00_a §3.3.4 6 段格式**；不加 breadcrumb；不加 TOC；每段尾加 source italic；跨檔 link `/` 開頭；單向 reference）
  - `## .protocol_version 寫入規範`（純讀取 skill 可選寫 phase_log audit entry；含 `read_sources` 清單 + `report_sections` 計數 + `findings_summary`；不更新 entity 完成度）
  - `## 輸入`（可選 user 參數：素材 file path 或 inline text；不必填則掃廣 Instance）
  - `## 輸出`（**chat Markdown 印 6 段診斷報告**；**不寫任何檔**；明示「若要把整理結果寫入正式模板請用 /integrate」）
  - `## 邊界`（**純讀取邊界 8 條** — 對齊 D6 view-world 7 條 + 「不出 §3.3.3 5 條禁止事項」第 8 條）
  - `## 錯誤處理 / Rollback`（source 缺漏處理：印警示但仍盡量寫診斷報告；某 source 完全不存在 → 「三、目前資料可確認的內容」段印「[source 缺漏 — 跑 /create-world 或 /create-character 建立基底]」placeholder）
  - `## 錯誤呈現規則`（沿用 ARCH §3.3.1 四件套）

### /diagnose 差異規格

- **觸發語：** `/diagnose`（不接參數時掃廣 Instance）或 `/diagnose <file_path>`（單檔診斷）或 `/diagnose <inline text>`（user 貼一段內容診斷）
- **對應 protocol：** `00_protocol/00_a §3.3 診斷模式`（line 180-236）— 本 skill **不**改 00_a；只是 Phase D 階段的 runtime 實踐
- **議題清單動態載入：** 不適用（/diagnose 屬通用模式；不綁特定議題清單 registry）
- **modify entity 範圍：** 無（純讀取；不修任何 entity）
- **依賴：** 不要求任何 entity 存在（適用「初次讀取」場景；可在空 Instance 跑）
- **下游：** 階段 5 印「下一步建議」段（內含「跑 /integrate 把資料整理進模板 / 跑 /check-gaps 看 INFERENCE TODO / 跑 /view-* 看實體 wholeness / pre-check /qa 之前先跑 /diagnose 預掃」等可選建議）

### 5 階段流程

#### 階段 1：診斷準備（read-only diagnostic setup）

agent 開場：

> /diagnose 將跨檔分析 Instance 資料，輸出 6 段診斷報告（對齊 00_protocol/00_a §3.3.4 格式）：作品類型與敘事氣質 / 世界語言與台詞風格推測 / 目前資料可確認的內容 / 不可確認或需人類確認的內容 / 通用規則適配性 / 建議下一步。本 skill 純讀取，不寫任何檔（除可選 phase_log audit entry）。
> 
> 開始讀取 source...

agent 檢查啟動前條件（D-049 Template-detect + Bootstrap completed）；任何缺漏拒絕並印缺漏清單。

若 user 傳 `<file_path>` 參數 → 限定診斷該檔（含 frontmatter 解析）；若傳 `<inline text>` 參數 → 限定診斷該段（不需 frontmatter）；若不傳 → 掃廣 Instance（讀 01_world / 02_vocabulary / 03_characters / 04_relationships / 05_plot 為主；下游 06/07/08/09 視情況讀）。

#### 階段 2：反查 source（依使用模式）

**模式 A — 不傳參數（掃廣 Instance 診斷）：**

| Source | 內容 | 在診斷報告內的位置 |
|---|---|---|
| `01_world/01_a_世界觀總覽.md` | W-rules 主分拆 | 一、作品類型與敘事氣質 / 二、世界語言與台詞風格推測 |
| `01_world/01_b_世界語言規格.md` + `01_c_陣營與階級語言.md` | W-language | 二、世界語言與台詞風格推測 |
| `02_vocabulary/02_a~c` | V 詞彙系統 | 二、世界語言與台詞風格推測 / 三、目前資料可確認的內容 |
| `03_characters/*` | C-* 聲線卡（掃廣） | 三、目前資料可確認的內容（角色清單）|
| `04_relationships/04_a` + `04_b` | R-*-* 關係 | 三、目前資料可確認的內容（關係清單）|
| `05_plot/05_a~e` | P / CH-* 大綱 | 三、目前資料可確認的內容（主線結構）|
| `00_protocol/00_b §1/§2` | 作品專屬反 AI 味基線（W 對應段）| 五、通用規則適配性（00_b §1 類型語氣 / §2 髒話尺度作為作品專屬規則）|

**模式 B — `<file_path>` 限定診斷：**

agent 限定讀該 file path + 對應 entity 反查鏈（透過 frontmatter `entities` / `depends_on` 跳到相關檔）。

**模式 C — `<inline text>` 限定診斷：**

agent 直接對 user 貼的文字做 §3.3 診斷邏輯（無 frontmatter；僅做語意分析）；輸出 6 段格式但「三、目前資料可確認的內容」段印「[本次屬 inline text 診斷；無 Instance 資料參照]」。

agent 對每個 source 讀取後：
- 解析 frontmatter（含中文 5 header + YAML block）
- 抽取 main content（跳過 frontmatter + 中文 5 header）
- 標記抽取位置（line 起訖；給 audit 用）

#### 階段 3：在記憶中組合診斷報告（in-memory；不寫檔）

agent 把 source 分析結果組合成單一 Markdown 結構（對齊 00_a §3.3.4 6 段格式 + 加 source italic）：

```markdown
# 診斷報告

## 一、作品類型與敘事氣質

<依 source 分析（W-rules 觀察 + 00_b §1 作品類型語氣對照）>

*來源：[/01_world/01_a_世界觀總覽.md](/01_world/01_a_世界觀總覽.md) / [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1*

## 二、世界語言與台詞風格推測

<依 source 分析（W-language + V + 00_b §2 髒話尺度）>

*來源：[/01_world/01_b_世界語言規格.md](/01_world/01_b_世界語言規格.md) / [/01_world/01_c_陣營與階級語言.md](/01_world/01_c_陣營與階級語言.md) / [/02_vocabulary/02_a~c.md] / [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §2*

## 三、目前資料可確認的內容

依現有 source 列出可確認的設定：

- **角色：** <掃 03_characters/ 列出已建 C-*>
- **關係：** <掃 04_relationships/04_a 列出已建 R-*-*>
- **主線結構：** <掃 05_plot/05_a~e 列出 P + CH-*>
- **詞彙：** <掃 02_vocabulary/ 列出已建 V 條目數>

*來源：（依各 source 路徑）*

## 四、不可確認 / 需人類確認的內容

依現有 source 找出 TODO / INFERENCE / CONFLICT 標記 + 缺漏實體：

- **TODO 累積：** <grep 全 Instance `TODO:` count + 列出前 5 個>
- **INFERENCE 推測：** <grep 全 Instance `INFERENCE:` count + 列出前 5 個>
- **CONFLICT 矛盾：** <grep 全 Instance `CONFLICT:` count + 列出前 5 個>
- **缺漏實體：** <跟 expected manifest 對比；列出尚未建立的 W/V/C/R/P/CH/S>

*來源：（依各標記出現位置）*

## 五、通用規則適配性

| 規則 | 建議 | 原因 |
|---|---|---|
| <依 00_a / 00_b / 00_c 通用規則逐一評估> | <保留 / 放寬 / 條件式 / 刪除 / 待確認> | <一句話原因> |

例：

| 00_a §2.1 高品質台詞定義 | 保留 | 普適性；本作品無明確排除理由 |
| 00_a §2.2 角色不直說自己 | 放寬（高反差場景例外）| 本作品為複雜雙主角；某些場景需直白獨白 |
| 00_b §1 作品類型語氣 | 待確認 | 00_b §1 仍標 TODO；user 需先拍板 |
| 00_b §2 髒話尺度 | 待確認 | 同上 |
| 00_c 台詞輸出格式 | 保留 | 標準格式無作品特殊性 |

*來源：[/00_protocol/00_a_台詞生產協議.md](/00_protocol/00_a_台詞生產協議.md) §2 / [/00_protocol/00_b_反ai味檢查表.md](/00_protocol/00_b_反ai味檢查表.md) §1~§2 / [/00_protocol/00_c_台詞輸出格式.md](/00_protocol/00_c_台詞輸出格式.md)*

## 六、建議下一步

依本次診斷結果建議：

1. **若 00_b §1/§2 標 TODO → ** 跑 /create-world（含 00_b §1/§2 寫入；D-053 例外允許）或請 user 先拍板作品類型 + 髒話尺度
2. **若有大量缺漏實體 → ** 跑對應 `/create-*` skill 建立基底
3. **若想把 inline text 整理成模板欄位 → ** 跑 /integrate（不直接 trigger；user 手動）
4. **若想看實體完成度 → ** 跑 /status
5. **若想看 INFERENCE / TODO 累積與缺漏 → ** 跑 /check-gaps
6. **若想看單一實體整合視圖 → ** 跑 /view-* 系列
7. **若想持久化某實體整合視圖 → ** 跑 /export-* 系列

---

**注意：** 本診斷報告由 /diagnose 自動產出（對齊 00_a §3.3 診斷模式）；屬 read-only analysis；不寫任何模板 / source / view / export。
```

#### 階段 4：印 chat（不寫檔）

agent 把組合結果直接印在 chat。

**呈現規則（對齊 ARCH §4.3 + UX_SPEC §7）：**
- chat 動態組合**不加 breadcrumb**（breadcrumb 僅 /export-* 寫檔加）
- chat 動態組合**不加 TOC**（chat 介面無需）
- 每段尾加 source italic 引用 `*來源：[/path](/path)*`（可多 source 逗號分隔）
- 跨檔 link 一律以 project root 為基準（`/` 開頭）
- 單向 reference：本 skill 引用 source 時加連結；source 不必反向列

#### 階段 5：驗證 + 寫 phase_log audit

階段 5 純 audit：

- **不**自動 trigger /status / /check-gaps / /view-* / /integrate（/diagnose 是 read-only；不影響任何進行中 skill）
- 可選寫 `.protocol_version.phase_log` audit entry（含 `read_sources` 清單 + `report_sections` 計數 + `findings_summary`）；若 user 跑 /diagnose 頻繁可設「audit log skip」flag 不寫
- 印「下一步建議」段（屬報告六、不是 audit）

### .protocol_version phase_log entry 範例（可選寫）

```yaml
- phase: diagnose
  date: YYYY-MM-DD
  skill: /diagnose
  status: completed
  mode: <scan_all | file_path | inline_text>
  scope: <"all_instance" | "<file_path>" | "inline_text_excerpt">
  read_sources:
    - 01_world/01_a_世界觀總覽.md
    - 01_world/01_b_世界語言規格.md
    - 01_world/01_c_陣營與階級語言.md
    - 02_vocabulary/02_a_專有名詞表.md
    - 02_vocabulary/02_b_俗稱與黑話表.md
    - 02_vocabulary/02_c_禁用詞與慎用詞表.md
    - 03_characters/*  # 列實際讀的清單
    - 04_relationships/04_a_角色關係矩陣.md
    - 04_relationships/04_b_關係變化時間線.md
    - 05_plot/05_a~e.md
    - 00_protocol/00_a_台詞生產協議.md  # §2 + §3.3 reference
    - 00_protocol/00_b_反ai味檢查表.md  # §1 + §2
    - 00_protocol/00_c_台詞輸出格式.md
  report_sections: 6  # 對齊 00_a §3.3.4
  findings_summary:
    todo_count: <N>
    inference_count: <N>
    conflict_count: <N>
    missing_entity_count: <N>
  output_target: chat
  customizations: []
```

### 啟動前檢查（嚴格條件 — 寬鬆 view-* pattern）

| 檢查項 | 條件 | 失敗行為 |
|---|---|---|
| D-049 Template-detect | `.template_root` 不存在（屬 Instance）| 拒絕並提示用 /init-project |
| Bootstrap completed | `.protocol_version` 存在 | 拒絕並提示用 /init-project |
| 不要求任何 entity 存在 | /diagnose 適用「初次讀取」場景；可在空 Instance 跑 | — |
| 不要求下游 pipeline 互鎖檢查 | /diagnose 是 read-only；不影響任何進行中 skill | — |

### 邊界區段（純讀取邊界 8 條；對齊 D6 view-world 7 條 + 加 §3.3.3 紀律第 8 條）

`/diagnose` 是純讀取 skill（對齊 00_a §3.3）。本 skill 嚴格限：

1. **不寫任何檔**（除可選 phase_log audit entry）
2. **不寫 view/<entity>.md / export/<...>**（屬 Wave 14 /export-* + §4.2a L3 Export scope）
3. **不擴 source 範圍**（依使用模式限定；模式 A 掃廣 Instance；模式 B 單檔 + 反查鏈；模式 C inline text only）
4. **不升 entity 狀態**（/diagnose 屬 read-only；任何狀態升級需走對應 /iterate-* 或 /create-*）
5. **不擅自呼叫其他 skill**（user 要跑 /integrate / /status / /check-gaps / /view-* 請手動）
6. **不擅自重新組織 source 內容**（agent 只 verbatim 抽取 + 套 6 段格式；不改 wording / 不總結成 final 結論）
7. **不寫 LOCKED 狀態**（/diagnose 不涉及 entity 狀態變動）
8. **嚴守 00_a §3.3.3 五條禁止事項**：
   - 不直接改寫正式模板
   - 不擅自補完重大世界觀設定
   - 不把推測寫成已確認設定（INFERENCE 必須明示標記 + 留 user 拍板）
   - 不產生 final 或 locked 文件
   - 不直接生成正式台詞

**vs Wave 14 export-* 邊界三 block 的差異：** /export-* 寫 view/<entity>.md 用 D-050 三 block（寫檔性質）；/diagnose 純讀取用 8 條邊界（read-only 性質；對齊 D6 view-world + §3.3.3 5 條延伸）。

### 中文 wrapper SKILL.md 結構（診斷）

採極簡模式，指向英文主檔為權威：

```markdown
---
name: 診斷
description: "/diagnose skill 的中文 wrapper；執行時以英文主檔為權威。"
---

狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：/diagnose skill 中文觸發 wrapper  
優先級：中

# /診斷（/diagnose wrapper）

本 wrapper 是 `/diagnose` 的中文別名。執行時以英文主檔 `.claude/skills/diagnose/SKILL.md` 為權威。

請參考 `.claude/skills/diagnose/SKILL.md`。
```

---

# 2. CODEX 工作流程

1. **讀必讀 spec**（按順序）：
   - `_design/TASKS.md` v1.9 §C.6（/diagnose + /integrate task spec）
   - `00_protocol/00_a_台詞生產協議.md` §3.3 診斷模式（line 180-236）+ §3.3.4 建議輸出格式（line 218-236；6 段格式為權威）
   - `_design/ARCHITECTURE.md` v1.6 §3.3 表（line 692 — /diagnose 對應 00_a 診斷模式）+ §3.3.1（錯誤呈現規則四件套）
   - `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema — read 對齊；本 skill 不寫 entity 檔）
   - `_design/UX_SPEC.md` v0.4 §7（呈現規則 — 跨檔 link / source 引用 / 單向 reference）
   - `.claude/skills/view-world/SKILL.md` v0.1 / `.claude/skills/status/SKILL.md` v0.1 / `.claude/skills/check-gaps/SKILL.md` v0.1（既有 read-only skill 範例；不寫檔 pattern 參考）
   - `_design/DECISIONS_LOG.md` v2.0（如有 diagnose 相關拍板）

2. **寫 SKILL.md 2 個**：
   - 英文主檔 `.claude/skills/diagnose/SKILL.md`（依本 starter §1 「主 SKILL.md 結構」+ 「差異規格」+ 「5 階段流程」+ 「邊界區段」）
   - 中文 wrapper `.claude/skills/診斷/SKILL.md`（依本 starter §1 「中文 wrapper SKILL.md 結構」）

3. **跑 baseline 驗證**：
   - `python -X utf8 -B scripts/check_headers.py 2>&1 | tail -5`
   - `python -X utf8 -B scripts/check_paths.py 2>&1 | tail -5`
   - `python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; ..."`
   - 對齊 9th master 第二段 Wave 14 收尾後 baseline：`check_paths ≤ 247 ERROR`（Windows 端權威；R2-MAJOR-03 hard-limit accept）

4. **不跑真實 /diagnose**（Template repo 內無 Instance entity；本輪 implementer 只寫 SKILL.md 不執行）

---

# 3. 驗收條件

| 維度 | 範圍 | 判準 |
|---|---|---|
| 1. 技術驗證 | check_headers / check_paths / build_repo_index baseline | 對齊 Wave 14 收尾後 baseline；無新 ERROR；check_paths ≤ 247 |
| 2. SKILL.md 落地 | 2 個 SKILL.md 存在 + frontmatter + 中文 5 header | 結構齊全 |
| 3. 5 階段流程 + 呈現規則 | SKILL.md 含 5 階段對齊 00_a §3.3 + 呈現規則對齊 §3.3.4 + ARCH §4.3 | 完整 |
| 4. 6 段診斷報告格式 | SKILL.md 階段 3 範本對齊 00_a §3.3.4 line 218-236 全 6 段 + 加 source italic | 嚴格對齊 |
| 5. 三種使用模式 | SKILL.md 階段 2 含 模式 A (掃廣 Instance) + 模式 B (file path) + 模式 C (inline text) 三種 | 完整支援 00_a §3.3「初次讀取 / 找缺漏與矛盾 / 風格判斷」三種使用時機 |
| 6. 純讀取邊界 8 條 | SKILL.md 含「邊界區段（純讀取邊界）」8 條完整（含 §3.3.3 5 條禁止事項對齊）| 對齊 D6 view-world 7 條 + 第 8 條延伸 |
| 7. phase_log entry 規範 | SKILL.md 含 phase_log entry 範例（可選寫；含 `mode` + `scope` + `read_sources` + `report_sections` + `findings_summary` + `output_target: chat`）| 對齊 diagnose read-only pattern |
| 8. 跟 /integrate / /view-* / /export-* 邊界明示 | SKILL.md 邊界區段明示「不擅自 trigger /integrate / /status / /check-gaps / /view-* / /export-*」+ 與三者 scope 區分 | 對齊 D.15 scope 預留 + Wave 13/14 既有 scope |

---

# 4. 邊界與紀律提醒（給 CODEX）

- **不**寫任何檔（除可選 phase_log audit entry）
- **不**寫 view/<entity>.md / export/<...>
- **不**升 entity 狀態
- **不**呼叫其他 skill（含 /integrate / /status / /check-gaps / /view-* / /export-* / /iterate-* / /scene-task / /dialogue-write / /qa / /create-*）
- **不**改 LOCKED spec / registry / parser code
- **不**改既有 38 個 SKILL.md
- **不**改 00_a / 00_b / 00_c / 00_j / 00_k / 任何 protocol（00_a 是本 skill 對應 protocol；只讀為權威）
- **不**改 DECISIONS_LOG / POST_LOCK_PENDING / D054_DECISION_PACKAGE

「Fix one, find two」cascade pattern 預防（HANDOFF §4.6 + 9th master 5 條教訓內化）：

- 寫好 SKILL.md 後跑 grep 全掃 stale cross-ref（含版本 reference / file path / D-NNN 引用 / 00_a §3.3.X 段標題）
- 寫 starter 涉及 path reference 前先 ls 實際 repo 對齊
- 寫 starter 涉及 SPEC frontmatter 段直接 grep SPEC §5.2 verify（雖然本 skill 不寫 entity 檔 frontmatter，但 phase_log entry 寫法仍要對齊 SPEC §5.4a）

---

# 5. Wave 15 batch mode 預告

D.14 PASS → Wave 15 後續 task 採 batch 模式：

- master 將寫 `CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md` v0.1
- 內容：「依 D14 範本 + 00_a §3.4 + TASKS §C.6 寫 D15 /integrate starter」
- CODEX 在乾淨對話跑 batch starter → 寫 D15 (/integrate + /整理) 2 個 SKILL.md
- D.15 /integrate 跟 D.14 /diagnose 關鍵差異：**/integrate 可寫檔但必須 user 拍板**（對齊 D-052 紀律）；邊界改用 D-050 三 block + 「寫檔前先印 diff 給 user 拍板」階段
- master 端內部 verify（grep 結構 + Read 重點 section；不跑 CODEX review starter）

---

# 6. Cross-ref

- `_design/TASKS.md` v1.9 §C.6（/diagnose + /integrate task spec）
- `00_protocol/00_a_台詞生產協議.md` §3.3 診斷模式（line 180-236；本 skill 對應 protocol；只讀為權威）
- `_design/ARCHITECTURE.md` v1.6 §3.3 表（line 692 — /diagnose 對應 00_a 診斷模式）+ §3.3.1（錯誤呈現規則四件套）+ §4.3（呈現規則）
- `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）+ §5.4a（phase_log entry 新欄位）
- `_design/UX_SPEC.md` v0.4 §7（呈現規則）
- `_design/CODEX_D6_STARTER.md` v0.1（/view-world starter；本 D14 共用「純讀取邊界」pattern 參考 — 但 view 是單一 entity 視圖，diagnose 是跨檔診斷）
- `.claude/skills/view-world/SKILL.md` v0.1（Wave 13 落地 view-world skill；本 skill 共用 read-only pattern 參考）
- `.claude/skills/status/SKILL.md` v0.1 + `.claude/skills/check-gaps/SKILL.md` v0.1（既有 read-only skill 範例）
- `_design/DECISIONS_LOG.md` v2.0（如有 diagnose 相關拍板；D-052 AI-assisted + user 拍板紀律參考）
- `_design/POST_LOCK_PENDING.md` v0.18（9th master 第一段 Round 1-4 review cycle 收尾 + 5 條教訓內化 + NEW_REQ_10 outer fence 慣例）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話 scope）
- `_design/PHASE_C_COMPLETION_REPORT.md` v1.0（Milestone 3 達成事實檔）
