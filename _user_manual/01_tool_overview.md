狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：工具完整定位 + 三層架構 + 26 個 skill 全表  
優先級：最高

# 01 工具總覽

# 1. 工具定位

**個人遊戲劇本工作室** — 你一個人 + AI agent，從零產出一款遊戲完整劇本，並交付給下游工種。

## 1.1 適合用什麼

| 適合 | 不適合 |
|---|---|
| 視覺小說（VN）| 開放世界（線性對話為主才合適） |
| 互動小說（IF） | 即時動作 RPG |
| 對話遊戲（如逆轉裁判類）| 純玩法遊戲（無劇本）|
| 角色扮演線性主線 | 多分支劇情樹（v1.0 支援單線；多分支屬未來擴充）|
| 單作品（一個 Instance）| 大型遊戲共用世界觀（Template 機制 v1.0 初步支援，Phase D+ 細化）|

## 1.2 工具不做的事（明確邊界）

- ❌ 不寫實作程式碼 — 工具只產資料（JSON + MD）
- ❌ 不轉檔到遊戲引擎 — JSON 給 Unity 工程師寫 5 分鐘 script 轉
- ❌ 不做翻譯 — 工具產 KEY + content，翻譯系統吃 JSON 處理
- ❌ 不做配音 — 工具產對話 + 立繪 / BGM 引用，錄音流程在外
- ❌ 不畫立繪 — 工具只存立繪 KEY metadata，繪師獨立作業
- ❌ 不取代你 — agent 給 3 版供選，你拍板

---

# 2. 三層架構

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1：Authoring（撰寫層）                                    │
│  agent 對話 + /dialogue-write + /qa + Markdown source            │
│  ← agent 對話 in Claude Code / Cowork                            │
└─────────────────────────────────────────────────────────────────┘
                                ↓ source 寫好 / 改好
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2：前端工具（管理 + 編輯）                                 │
│  HTML web UI / 本地 web server / 手動 Save                       │
│  F1 看板 + F2 切換 + F3 並排 + F6 搜尋 + F7 編輯                  │
│  跟 agent 完全分離（雙視窗工作流）                                │
└─────────────────────────────────────────────────────────────────┘
                                ↓ 要交付時
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3：Export（輸出層）                                       │
│  一個 export 動作 → 吐 JSON + MD 雙檔                            │
│  「轉檔到引擎」明確劃在工具外                                     │
└─────────────────────────────────────────────────────────────────┘
```

## 2.1 典型 user session

```
1. Terminal：python serve.py 啟動前端 server
2. 瀏覽器：localhost:8765 開 Dashboard
3. F1 看實體完成度 + 該做什麼
4. F2 切到某場景 → 看現有台詞 / 立繪 / QA 狀態
5. 想改 → F7 直接編輯 → Save → 寫回 .md
6. 想跟 agent 討論 → 開外部 Claude Code / Cowork → agent 改寫回 .md
7. 切回前端瀏覽器 refresh → 看到 agent 結果
8. 結束時手動 git commit + push
```

---

# 3. 26 個 Skill 全表

依用途分 4 組：

## 3.1 一次性 skill

| Skill | 中文別名 | 用途 |
|---|---|---|
| `/init-project` | `/初始化專案` | Bootstrap — 建新專案結構（每個專案只跑一次）|

## 3.2 上游 — 建設定（5 個 create + 5 個 iterate + 5 個 view + 5 個 export）

### Create — 建立新設定（5 個）

| Skill | 中文別名 | 議題數 | 工時 |
|---|---|---|---|
| `/create-world` | `/建立世界觀` | 11 | 2-3h（手稿導入 10 分） |
| `/create-character <name>` | `/建立角色 <name>` | 9 | 30-60 分 / 角色 |
| `/create-relationship <a> <b>` | `/建立關係 <a> <b>` | 6 | 30 分 / 關係 |
| `/create-outline` | `/建立大綱` | 7 | 1-2h |
| `/create-detailed-outline` | `/建立細綱` | 7 | 半天 |

### Iterate — 改既有設定（5 個）

| Skill | 中文別名 | 行為 |
|---|---|---|
| `/iterate-world` | `/迭代世界觀` | 改世界觀；自動反查依賴 |
| `/iterate-character <name>` | `/迭代角色 <name>` | 改角色聲線；提醒受影響的對白檔 |
| `/iterate-relationship <a> <b>` | `/迭代關係 <a> <b>` | 改關係矩陣 |
| `/iterate-outline` | `/迭代大綱` | 改主線；提醒受影響的章節 |
| `/iterate-detailed-outline` | `/迭代細綱` | 改章節細綱 |

### View — 動態組合視圖（4 個；chat 內呈現，不寫檔）

| Skill | 中文別名 | 行為 |
|---|---|---|
| `/view-world` | `/查看世界觀` | chat 內動態組合完整世界觀視圖 |
| `/view-character <name>` | `/查看角色 <name>` | chat 內動態組合角色完整資料 |
| `/view-outline` | `/查看大綱` | chat 內動態組合主線 + 章節 |
| `/view-detailed-outline` | `/查看細綱` | chat 內動態組合章節 + 場景 |

### Export — 靜態整合檔（4 個；寫到 `view/`）

| Skill | 中文別名 | 行為 |
|---|---|---|
| `/export-world` | `/匯出世界觀` | 寫 `view/世界觀.md`（DERIVED 狀態）|
| `/export-character <name>` | `/匯出角色 <name>` | 寫 `view/角色_<name>.md` |
| `/export-outline` | `/匯出大綱` | 寫 `view/大綱.md` |
| `/export-detailed-outline` | `/匯出細綱` | 寫 `view/細綱.md` |

⚠ **這 4 個 `/export-*` 寫 `view/` 給人讀**。要給程式 / 翻譯 / 配音吃的 JSON 不是這 4 個 — 是前端 Export Panel 走 A1 prompt 流程（見 §5）。

## 3.3 下游 — 寫對白 pipeline（3 個）

| Skill | 中文別名 | 模式 | 行為 |
|---|---|---|---|
| `/scene-task <scene_id>` | `/場景任務包 <scene_id>` | — | 為一場戲產任務包（context 自動裝載）|
| `/dialogue-write <scene_id>` | `/生成台詞 <scene_id>` | 試寫 / 破格 / 收斂 / SINGLE_ITER 4 種 | 產 3 版對白 / 收斂 v02 / 單版本迭代 |
| `/qa <dialogue_path>` | `/檢查 <dialogue_path>` | — | 跑 8 份 QA 報告 |

### `/dialogue-write` 4 種模式

```
模式 1：試寫（預設）
  /dialogue-write S-01-03
  → 產 v01A 克制 / v01B 衝突 / v01C 情緒 三版

模式 2：破格
  /dialogue-write S-01-03 --experimental
  → 產 v01D 詩化 / 黑色幽默 / 等大膽版本

模式 3：收斂（user 挑亮點後）
  /dialogue-write S-01-03 --converge --picks "v01A.l001,v01B.l003,..."
  → 整合亮點產 v02

模式 4：單版本迭代（D-027 新增）
  /dialogue-write S-01-03 --single-iter --note "主角第 2 句更冷峻"
  → 跟 user 迴圈改 v01_iter1 → iter2 → ... 直到 OK
```

## 3.4 管理 / 監控（5 個）

| Skill | 中文別名 | 用途 |
|---|---|---|
| `/status` | `/進度` | 看整體完成度 + 下一步建議 |
| `/check-gaps` | `/缺漏檢查` | 找出所有 TODO + 缺檔 + 過期 view |
| `/diagnose` | `/診斷` | 純診斷模式入口（不寫檔）|
| `/integrate` | `/整理` | 純整理模式入口（把資料轉成模板欄位）|
| `/init-project` | `/初始化專案` | 已列在 §3.1 |

---

# 4. 資料類別範圍

## 4.1 v1.0 實作的 entity 類型

| Prefix | 類型 | 對應目錄 |
|---|---|---|
| `W-rules` / `W-language` | 世界規則 / 語言 | `01_world/` |
| `V` | 詞彙系統 | `02_vocabulary/` |
| `C-<name>` | 角色 | `03_characters/` |
| `R-<a>-<b>` | 關係 | `04_relationships/` |
| `P` | 主線 | `05_plot/` |
| `CH-<n>` | 章節 | `05_plot/` |
| `S-<ch>-<n>` | 場景 | `06_scene_index/` `07_scene_tasks/` `08_dialogue_outputs/` |
| `A-<subtype>-<owner>-<state>` | 美術資產（7 subtype）| `10_art_assets/<subtype>/<group>.md` |

## 4.2 A-* 美術資產 7 subtype

| Subtype | 用途 |
|---|---|
| `portrait` | 角色立繪（必對應 C-*） |
| `bg` | 背景 |
| `cg` | 事件圖 |
| `sfx` | 音效 |
| `bgm` | 背景音樂 |
| `voice` | 配音 line |
| `ui` | UI 文案 |

## 4.3 預留接口（v1.0 不實作，未來擴充）

| Prefix | 類型 | 計畫 |
|---|---|---|
| `I-*` | 物品 / 道具 | Phase D+ |
| `UI-*` | UI 文案 entity（跟 A-ui 不同） | 未來 |
| `SKILL-*` | 技能說明 | 未來 |

---

# 5. Layer 3 Export 流程

Export 給程式 / 翻譯 / 配音 吃的 JSON 走 **A1 prompt 流程**（不是上面 4 個 `/export-*` skill）：

```
1. 前端開 Export Panel
2. 選範圍 / 格式 / 推送方式
3. 點「複製 Prompt」
4. 切到 Claude Code 貼上
5. agent 跑 export → 產 export/<instance>_<date>.{json,md}
6. JSON 給下游工種
```

**為什麼這樣設計：** 前端不執行 agent（D-029 α 完全分離原則）。export 跑在外部 agent process 中。

詳見 [03 下游 skill](03_downstream_skills.md) §3.x。

---

# 6. 全域文件狀態機

每個 .md 檔有「狀態」欄位：

```
DRAFT  ────► REVIEW  ────► FINAL  ────► LOCKED
  │             │             │             │
  └─────────────┴─────────────┴─────────────► DEPRECATED
                                              （任何狀態都可廢棄）
```

| 狀態 | 完成度權重 | 規則 |
|---|---|---|
| DRAFT | 25% | 草稿，可大幅修改 |
| REVIEW | 75% | 可使用但需審核 |
| FINAL | 100% | 人類確認定稿（需 QA 通過）|
| LOCKED | 100% | 已鎖定，不得擅自改動 |
| DEPRECATED | 不計入 | 已棄用 |
| APPLIED | 不計入 | 補丁類已套用 |
| DERIVED | 不計入 | 衍生整合檔（view/ 下）|

**升級限制：** AI / CODEX **不得自行**升級狀態 — 必須 user 明示。

---

# 7. 接下來

| 想了解什麼 | 看哪章 |
|---|---|
| 第一次用怎麼啟動 | [00 快速入門](00_quick_start.md) |
| 每個 skill 詳細語法 | [02 上游 skill](02_upstream_skills.md) / [03 下游 skill](03_downstream_skills.md) / [04 管理 skill](04_management_skills.md) |
| 前端工具怎麼用 | [05 前端工具](05_frontend_tools.md) |
| 檔案結構怎麼存 | [06 資料結構](06_data_structure.md) |
| 想自訂議題清單 / entity 類型 | [07 客製化](07_customization.md) |
| 典型工作流情境 | [08 工作流](08_workflows/README.md) |
