狀態：DRAFT
版本：v0.1-proposal
最後更新：2026-05-17
適用範圍：劇本工具創作內容資料格式 — 來自另一個 HARNESS-side 對話的提案，作為資料格式 specialist 的 reference 起點
優先級：中（advisory only）

---

# Creative Content Schema Proposal — HARNESS-side 對話來源

## 0. 本檔案的特殊性質與歷史脈絡

**這份文件不是本專案的設計成果**，而是來自另一個系統（HARNESS 治理工具）的 Claude 對話，在不知道本專案已通過 4 輪 CODEX 審查的設計（SPEC.md / ARCHITECTURE.md / TASKS.md）的前提下，從零提案的「劇本工具」資料格式。

**對本專案的價值：**

- 它代表「另一個獨立來源」對劇本工具 schema 的思考路徑
- 兩條獨立路徑的**共識**部分大概率是對的（例如 Markdown + YAML、不刪除舊版、明確 type 系統、selective read 等）
- 兩條路徑的**分歧**部分需要由資料格式 specialist 對話裁決
- 它指出我們既有設計可能漏掉的盲點（retcon vs supersede、多語言、continuity_check 獨立等）

**使用規則（給資料格式 specialist 對話）：**

1. 本檔案是 **reference，非 canon**
2. 提到的 HARNESS / F1 schema / Mode B / Z / Adapter 等術語**不應整套引入本專案**
3. 不要採用「`_creative/` 整套 folder 重組」這類會打掉現有結構的建議
4. 可吸收的概念請走「議題盤點 → 對齊現有 SPEC → 提案 → master 裁決」流程，不擅自寫入

---

## 1. 原始提案內容（完整保留）

以下為 HARNESS-side Claude 在那份對話中的原始輸出，未經修改。

---

狀態：DRAFT / REFERENCE only
版本：0.1-proposal（未經 Mode B activation gate）
撰寫者：Claude（HARNESS-side conversation 內提案）  
適用範圍：劇本工具創作內容資料格式 — 提供給跨專案同步偵察員 Z 作對映基準
優先級：中（advisory only）

# 劇本工具創作內容資料格式提案（Creative Content Schema Proposal）

## 0. 這份文件的性質

- **不是** HARNESS Mode B 啟動文件
- **不是** 劇本工具的官方 schema
- **不是** authority；任何條款都可被 Z 的盤點結果推翻
- **是** 基於 HARNESS F1 schema 模式延伸的創作內容版本草案
- **是** Z 用來對映實際資料結構的參考起點
- **是** 之後 Mode B activation 設計的輸入候選

Z 使用本文件的方式：

1. 讀完取得 schema 概念
2. 進劇本工具 folder 盤點實際資料
3. 比對「實際資料形狀 vs 本文件提案」
4. 列出 alignment / divergence / missing 三類差異
5. 不要把本文件當 canon；如果劇本工具現有結構更合理，以實際為準提反提案

## 1. 設計繼承

本提案沿用 F1 schema 設計模式，主要繼承：

- markdown + YAML frontmatter 檔案格式
- frontmatter 必填 / 條件必填 / 可選 三層
- record_status / decision_effect 拆分概念（轉為創作 domain 的 canon_status / change_effect）
- selective read 規則（只讀任務需要的檔，不全讀）
- supersede 鏈（不刪除舊版，留 audit trail）
- 自動 index regen 模式
- protected source 分層
- non_authority_boundary 強制每檔聲明

不繼承的部分：
- F1 的 8 種 governance type 枚舉（替換為創作 domain type）
- HARNESS 的 gate level（創作 domain 用 canon tier 替代）

## 2. 建議的 folder 佈局

```
<劇本工具 root>/
  _creative/                # 創作內容主目錄
    characters/             # 角色卡
      voice_cards/          # 角色聲音卡（細部 voice tone reference）
    scenes/                 # 場景
    dialogue/               # 台詞（每場戲一檔，或更細）
    world/                  # 世界觀 / 設定 / lore
    plots/                  # 劇情線 / 大綱
    episodes/               # 集數 metadata
    continuity_checks/      # 一致性檢核紀錄
    index/                  # 自動產生索引
      master_index.md
      characters_index.md
      scenes_index.md
      ...
  _coordination/            # 治理 / 對齊資料（Z 工作空間）
    inventory/              # 盤點報告
    workflow_notes/         # 提案 / 設計 note
  _archive/                 # 歷史版本（不刪除，supersede 鏈用）
  _drafts/                  # 草稿區（pre-canon）
  _finals/                  # 完成稿（locked）
  _clients/                 # 客戶 IP（strict protected）
```

**重要**：本佈局是提案，劇本工具現有結構可能完全不同。Z 應盤點後決定如何 reconcile。

## 3. 共用 frontmatter base（所有 type 共享）

```yaml
schema_version: 0.1                    # schema 版本，目前 "0.1"
id: 20260517T235900_b3f2_character     # <timestamp>_<4-hex>_<type>
type: character                        # 8 種閉集枚舉
canon_status: draft                    # 6 種閉集枚舉
created_at: 2026-05-17T23:59:00+08:00
created_by: <writer_name or system>
last_modified_at: 2026-05-17T23:59:00+08:00
last_modified_by: <writer_name or system>
protected_tier: collaborator           # 5 種閉集枚舉
supersedes: null                       # 前一版 id 或 null
superseded_by: null                    # 取代本檔的 id 或 null
related: []                            # [<type>:<id>] cross-reference
tags: []                               # 自由格式
non_authority_boundary: "本檔記載 X；evidence-only；最終 canon 由 user 在 final review 決定。"
```

## 4. Type 閉集枚舉（8 種）

| type | 用途 |
|---|---|
| `character` | 角色完整檔（背景 / 個性 / 關係） |
| `voice_card` | 角色聲音卡（語氣 / 用詞 / 禁忌） |
| `scene` | 場景（敘事單元 / 拍攝單元） |
| `dialogue` | 台詞集合（依場景或依角色） |
| `world` | 世界觀 / 設定 / 規則 / lore |
| `plot` | 劇情線 / arc / 大綱 |
| `episode` | 集數 metadata（一集的索引） |
| `continuity_check` | 跨場景 / 跨集 一致性檢核紀錄 |

## 5. canon_status 閉集（6 種）

```
draft         草稿，未進 canon
proposal      提案中，等 user / showrunner 決議
canon         已入 canon，後續可參考
final         鎖定為當前發稿版本
locked        硬鎖（需 strict gate 才能改）
superseded    被另一版取代（不可改但保留 audit）
retconned     創作層 retcon（不同於 superseded，是創作決策不是修正）
```

## 6. protected_tier 閉集（5 種）

```
public          行銷可看
collaborator    編劇 / 工具操作員可看（預設）
internal        製作團隊可看（不含外包）
client          客戶 IP，限主筆 + 製作人
locked          archived，需 strict gate 才能讀 body
```

## 7–8. Type-specific 欄位 / Cross-reference 格式

完整 type-specific 欄位設計請參考原始輸出（character / voice_card / scene / dialogue / world / plot / episode / continuity_check 各 type 的 YAML 範例），Cross-reference 一律用 `<type>:<id>` 格式。

## 9. Selective Read 規則

**寫一場戲對白時的必讀**：

1. 該場 scene 檔
2. 該場 `characters_present` 全部對應的 voice_card 檔
3. 該場 `plot_threads` 對應的 plot 檔（摘要）
4. 前一場 scene 檔（continuity）
5. 該場 location 對應的 world 檔（如有特殊規則）

**禁止**：
- 全讀 `_creative/`
- 推測「相關角色」並擴張
- 跨集讀其他集對白

## 10. Versioning / Supersede / Retcon

| 動作 | 觸發 | 處理 |
|---|---|---|
| **修正** | 發現錯字 / 設定 typo | 直接編輯或 supersede |
| **Supersede** | 創作版本演進（角色 v2 取代 v1） | 新檔 + supersedes 指向舊 id |
| **Retcon** | 創作決策反轉（第 10 集說第 1 集那場戲沒發生） | 新檔 canon_status=canon，舊檔 canon_status=retconned |

## 13. Open Questions（給 Z 與 user 決定）

1. **檔案粒度**：dialogue 策略 A（一場一檔）vs 策略 B（一交換一檔）？
2. **ID 格式**：保留實際工具現有 ID 還是改 timestamp+hex？
3. **canon_status 是否夠**？
4. **voice_card 是否獨立**？
5. **retcon 跨檔影響**：自動標記 affected scenes？
6. **角色關係是否獨立檔**？
7. **多語言**：對白多語版本如何在 schema 表達？
8. **劇本工具現有資料**：實際盤點後，本提案哪些欄位「強加上去」反而扭曲現有結構？

## 15. 不批准 / 邊界

本文件 **不批准**：
- Mode B activation
- 劇本工具任何檔案修改
- HARNESS Adapter 修改
- protected creative content read
- canon_status 升格
- 任何 commit / push
- Z 把本文件當 authority

---

## 2. 給資料格式 specialist 對話的使用指南

**強烈建議的吸收項目（3 項）：**

1. **retcon vs supersede 的區分** — 創作層反轉 ≠ 修正錯字。我們現有設計沒做此區分，Phase D canon delta 機制可能受益。
2. **多語言對白** — 我們完全沒考慮。如要做雙語版本，現有 schema 撐不住。
3. **continuity_check 作為一級實體** — 我們把跨集一致性檢查散在 09_quality_assurance/，沒獨立實體。

**可選議題（看作品需求）：**

4. **scene-level vs exchange-level dialogue** — 細粒度選擇。
5. **protected_tier 多層保護** — 個人專案不必，IP 合作要。

**直接拒絕：**

- HARNESS / Mode B / F1 schema / Z / Adapter 術語
- `_creative/` 整套 folder 重組
- canon_status 取代我們的 7 狀態系統
- timestamp+hex+type ID 取代實體名稱

---

## 3. 與本專案既有設計的對照

| 議題 | HARNESS 提案 | 本專案 SPEC |
|---|---|---|
| 整體模式 | F1 schema 延伸 | 自有 canonical schema（4 輪審查通過） |
| folder | `_creative/` 一條樹 | `00_protocol/` ~ `09_quality_assurance/` 多目錄 |
| frontmatter | YAML frontmatter 13 欄 | 中文 header 5 欄 + YAML block（上游 3 + 下游 8） |
| type 系統 | type: character / scene / etc.（內容類型） | entities: W-rules / C-* / etc.（實體關聯） |
| 狀態 | canon_status 6 種 | 狀態 7 種 + pipeline_state 9 種 + mode_tag 5 種 |
| 保護 | protected_tier 5 種 | LOCKED 狀態（單層） |
| 跨檔引用 | `<type>:<id>` 通用 | depends_on / source_task / source_dialogue 多種 |
| ID | timestamp+hex+type | 實體名稱（C-主角A、S-01-03） |
| 版本 | supersede + retcon | 版本後綴 v01A/B/C + 狀態升降 |
| 索引 | master_index + sub-index | `/status` skill 動態掃 |

**本專案維持自有設計，吸收上述 3 項建議概念，不採用提案的術語與整體架構。**
