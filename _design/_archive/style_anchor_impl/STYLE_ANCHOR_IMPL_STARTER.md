狀態：APPLIED
版本：v0.1 APPLIED（2026-05-28 batch 落地完成；採雙對話分工模式 — Template 對話 T1-T9 + T11 / Instance 對話 T10；K-NN 9 條累積詳見 HANDOFF_TO_10TH_MASTER §4.9；實際落地 vs starter 推測對照見文末 §8 歷史紀錄）
最後更新：2026-05-28
適用範圍：另一個 Claude / CODEX 對話 implementer 一次性實作 STYLE_ANCHOR_PROPOSAL v0.1 所定義的 8 檔變更
優先級：高

---

# STYLE_ANCHOR_IMPL_STARTER — pre-generation 文風錨定機制實作 batch task

# 0. 文件用途

本檔是給「另一個 Claude / CODEX implementer 對話」的啟動 starter。把本檔 §1 啟動 prompt **整段複製**到新對話即可。

implementer 一次性處理 8 處變更（對應 STYLE_ANCHOR_PROPOSAL v0.1 §10 acceptance criteria）：

| # | 路徑 | 性質 | 動作 |
|---|---|---|---|
| 1 | `00_protocol/00_b_反ai味檢查表.md` | instance-write zone 擴充 | append §1.1 §1.2（在既有 §1 之後、§2 之前） |
| 2 | `01_world/01_d_文風樣本與指紋.md` | **新建** | 從 RFC §4 §5 §6 拷貝 source-of-truth |
| 3 | `entity_type_registry.yaml` | instance registry 擴充 | 新增 `W-style` 條目 |
| 4 | `_design/expected_entities.yaml` | design registry 擴充 | 新增 W-style 註冊（如該 registry 走此檔） |
| 5 | `07_scene_tasks/07_a_單場台詞任務包模板.md` | 模板擴欄位 | §18 新增 `§18.3 高風險場景處理` + `§18.4 文風錨定`（既有 §18.1 §18.2 不動） |
| 6 | `.claude/skills/scene-task/SKILL.md` | skill 升版 v0.1 → v0.2 | §3.2 抽取來源表新增 `W-style` 行；header note + 變更摘要 |
| 7 | `.claude/skills/dialogue-write/SKILL.md` | skill 升版 v0.2 → v0.3 | Stage 1 診斷報告新增「文風錨定狀態」項；header note + 變更摘要 |
| 8 | `_design/DECISIONS_LOG.md` + `POST_LOCK_PENDING.md` | 拍板紀錄 | D-NNN 新拍板 + NEW_REQ_20（或下一個未用編號）追蹤 |

**前置條件：**

- STYLE_ANCHOR_PROPOSAL v0.1（位於 `_design/STYLE_ANCHOR_PROPOSAL.md`）是 source of truth；implementer 必讀完整 752 行
- fingerprint_analyzer.py（`_tools/fingerprint_analyzer.py`）是支援工具，不需執行（指紋數據已內嵌在 RFC §4）
- 既有 corpus 樣本 `台詞/Script_Level_07/08/09_adjusted.tsv` 由 RFC §6 已抽取代表性正例；implementer 不需重新抽
- 不要動 4 角色既有人設（`03_characters/男_*_人設v_0_1.md`、`女_*_人設v_0_1.md`）

**Batch 工作模式（採 9th master Wave 14-15 + 10th master Wave 12 batch 模式）：**

- master（本對話）寫本 starter（含 RFC reference + acceptance criteria）
- implementer 在乾淨對話**一次性**讀本 starter + RFC，完成 8 處變更
- implementer 在每處變更前先 print preview，由 user 拍板再寫檔
- implementer 完成後 commit + 印變更摘要回報 master
- master 端 verify（grep 結構一致性 + 對照 RFC §10 checklist）

⚠ **「Fix one, find two」cascade pattern 預防：**

- 寫完 8 處變更後跑 grep 全掃 stale cross-ref（含版本 reference / file path / 子節編號）
- 特別檢查既有 07_a §18.1 §18.2 是否被誤改編號
- 一次性 sweep；不局部修補

⚠ **長中文檔 truncation 預防：**

- `01_d_文風樣本與指紋.md` 預計 400-600 行；建議用 Write tool 一次性寫入；寫完跑 `wc -l <path>` + `python3 -c "open(path, 'rb').read().decode('utf-8')"` 驗 utf-8 decode 無 null bytes
- 若單檔超過 600 行建議分段寫（cat heredoc via bash 或多次 Edit append）

⚠ **慣例：**

- 本 starter outer agent-prompt fence 用 `~~~`（內部 nest ``` 不會 toggle 它）
- 路徑引用一律用 Instance root 完整相對路徑（如 `00_protocol/00_b_反ai味檢查表.md`，非絕對路徑）

---

# 1. 啟動 prompt（複製整段到新 Claude / CODEX 對話）

~~~
你是 game-script-A 專案的 STYLE_ANCHOR implementer agent。

本輪是「pre-generation 文風錨定機制實作 batch task」— 一次性實作 8 處變更（含新建 1 檔 / 擴充 5 檔 / skill 升版 2 檔）；對齊 `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1 § 10 acceptance criteria + DECISIONS_LOG v2.0 §6.12 D-050 + §6.16 D-053。

工作資料夾：D:\劇本開發\game-script-A

**重要：本任務的 source of truth 是 `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1（752 行）。你必須先完整讀完整份 RFC，再開始任何變更。**

**Token 不是限制** — 如有需要可開子對話跑 verify（grep 結構一致性 / RFC §10 checklist 對照 / D-050 邊界檢查 / 既有 07_a §18 既有子節保護檢查）。優先選擇能提升品質的工作切分。

**你的身份與職責：**
- 你是 implementer — 本輪做 8 處變更（不設計）
- 設計層已 freeze 在 STYLE_ANCHOR_PROPOSAL v0.1；implementer 不得改 RFC 設計，只搬規範到目標檔
- 任何 RFC 內 spec 拍板（D-050 邊界 / D-053 紀錄 / W-style entity 設計 / §18.4 子節編號）必須完整落地，不擅自簡化

**必讀 context（依序）：**

1. `D:\劇本開發\game-script-A\CLAUDE.md` — 專案總規則與 skill 索引
2. `D:\劇本開發\game-script-A\_design\STYLE_ANCHOR_PROPOSAL.md` — 本任務 source of truth（752 行；全讀）
3. `D:\劇本開發\game-script-A\_design\SPEC.md` §17.1（instance-write zone authority）+ §5.2（frontmatter canonical schema）
4. `D:\劇本開發\game-script-A\_design\DECISIONS_LOG.md` §6.12 D-050（skill 寫檔邊界）+ §6.16 D-053（D-053 partial supersede）
5. `D:\劇本開發\game-script-A\00_protocol\00_b_反ai味檢查表.md` §1（既有 instance-write 內容；不可破壞）
6. `D:\劇本開發\game-script-A\07_scene_tasks\07_a_單場台詞任務包模板.md` §18 既有結構（§18.1 §18.2 已被佔用；保護）
7. `D:\劇本開發\game-script-A\.claude\skills\scene-task\SKILL.md` v0.1 §3.2 抽取來源表（10 行；新增 1 行）
8. `D:\劇本開發\game-script-A\.claude\skills\dialogue-write\SKILL.md` v0.2 Stage 1 診斷段（新增「文風錨定狀態」項）
9. `D:\劇本開發\game-script-A\entity_type_registry.yaml`（既有 W-rules / W-language / V / C / R / P / CH 條目；新增 W-style）

**重要邊界（嚴格 scope）：**

- ✗ **不**改 RFC 設計（STYLE_ANCHOR_PROPOSAL v0.1 freeze）
- ✗ **不**改 既有 LOCKED spec（SPEC / IC / ARCH / TASKS / DF / UD / UX / L3 / REQUIREMENTS_LOCK / DECISIONS_LOG 全 LOCKED）
- ✗ **不**改 既有 D-001~D-054 拍板結論（新 D-NNN 屬本輪新增）
- ✗ **不**改 既有 07_a §18.1 §18.2 子節編號（向後兼容）
- ✗ **不**改 既有 4 角色人設（`03_characters/男_*_人設v_0_1.md` / `女_*_人設v_0_1.md`）
- ✗ **不**改 既有 03_b 主要角色聲線卡模板（per-character voice spec 留在原處）
- ✗ **不**重新抽取 corpus 指紋（已內嵌在 RFC §4）
- ✗ **不**重寫 RFC §6 樣本（複製即可；不擅自改正例 / 負例）
- ✗ **不**擴大 `/dialogue-write` 寫檔邊界（D-050 子裁決 2 嚴守）
- ✗ **不**擅自擴 D-053 scope（`/create-world` 不自動授權寫 01_d；本輪走 path A 人類直接編輯）
- ✗ **不**動 `_tools/fingerprint_analyzer.py`（屬支援工具，已在位）
- ✗ **不**改 `.protocol_version`（屬 runtime artifact，不在本 batch scope）
- ✗ **不**動 `_design/PHASE_C_COMPLETION_REPORT.md` / `PHASE_D_COMPLETION_REPORT.md` / `CANON_DELTA_FRAMEWORK.md` / `HANDOFF_TO_10TH_MASTER.md`（屬 milestone artifact，本 batch 不涉及）
- ✗ **不**改本 starter（`STYLE_ANCHOR_IMPL_STARTER.md`）

**本 task scope（嚴格限定 8 處變更；對齊 RFC §10）：**

### 變更 1：`00_protocol/00_b_反ai味檢查表.md` 擴充 §1.1 §1.2

在既有 §1 內容之後、`---` 分隔線之前 append 兩段：

```markdown
## 1.1 既有腳本文風基線聲明

本作品已寫過 3 個 Level（`台詞/Script_Level_07/08/09_adjusted.tsv`，共 171 行），確立作品文風基準。

下游 `/dialogue-write` 生成新台詞時，**必須以該基準為文風錨點**。

具體量化指紋與正例 / 負例樣本見：

- `01_world/01_d_文風樣本與指紋.md`

`/scene-task` 在抽 task pack §18 風格要求 欄位時，必須 reference `01_d`，並把適用本場的指紋條目（句長範圍、標點密度、特徵詞、禁用句型）抽進任務包 §18.4 文風錨定子節。

## 1.2 三層聲線規範總綱

本作品台詞含三層敘事結構，比例硬約束：

| 層 | 內容 | 比例 | 主要負責 |
|---|---|---|---|
| 層 A 對話 | 「」直角引號內 | 60-70% | 4 角色 |
| 層 B 主角旁白 / 內心 OS | （）內，第一人稱「我們」/「我」視角 | 20-25% | 男主角清道夫 |
| 層 C 環境描述 | （）內，被層 B 涵蓋 | 同層 B | （無獨立全知敘述者） |

跨層硬約束：

1. 零破折號（——）— 永久禁用
2. 旁白優先歸主角；其他角色旁白比例 < 5%
3. 主角內心 OS 寫在旁白層（）內，不寫成口說對話「」內
4. 旁白絕無心理標籤（「他憂愁地」「她悲傷地」）、絕無回憶插入、絕無全知敘事

詳細規範與 per 角色硬約束見 `01_world/01_d_文風樣本與指紋.md`。
```

**保護：** 既有 §1 由 `/create-world` 於 2026-05-25 寫入的「《蟲潮孤堡》是黑色幽默...」段落必須保留，不可改寫。

### 變更 2：**新建** `01_world/01_d_文風樣本與指紋.md`

整檔內容 source-of-truth = `STYLE_ANCHOR_PROPOSAL.md` §4 §5 §6（拷貝；不改寫；不重新抽指紋）。

檔案 header + frontmatter：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD（implementer 跑當天）
適用範圍：全作品 / 下游台詞生產 pre-generation guard
優先級：高

---
entities: [W-style]
depends_on: [W-rules, V, W-language]
weight: {W-style: 1.0}
---

# 01_d 文風樣本與指紋

（本檔內容拷貝自 `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1 §4 §5 §6；不改寫設計；不重新抽指紋）
```

主體分 5 個 `# N. ...` 章節，對應 RFC schema（見 RFC §7.2 sample schema 段）：

1. `# 1. 三層敘事結構比例`（拷貝 RFC §4.1）
2. `# 2. 全局文風指紋`（拷貝 RFC §4.2 §4.4 §4.6）
3. `# 3. Per 角色聲線樣本師`（4 子節：3.1 清道夫 / 3.2 瑟琳 / 3.3 莉娜 / 3.4 諾拉；各自拷貝 RFC §6.1-§6.4 完整內容含正例 + 負例）
4. `# 4. /scene-task 抽取規則`（從 RFC §7.2 maintenance 段拷貝）
5. `# 5. 維護規則`（從 RFC §7.2 maintenance 段拷貝）

### 變更 3：`entity_type_registry.yaml` 新增 W-style 條目

在既有 `core:` 區塊內、`W-language` 條目之後、`V` 條目之前 insert：

```yaml
  - type: W-style
    description: 文風樣本與指紋
    id_pattern: ^W-style$
    target_dir: 01_world/
    cross_ref_allowed: true
    locked: true
```

**保護：** 不改既有 7 個 core 條目（W-rules / W-language / V / C / R / P / CH）。

### 變更 4：`_design/expected_entities.yaml` 註冊 W-style

依該 yaml 既有結構，把 `W-style` 加入 expected entities 清單。如該檔結構 implementer 不清楚 → 先 cat 該檔，依既有結構（key/list 風格）追加，不破壞既有條目。

### 變更 5：`07_scene_tasks/07_a_單場台詞任務包模板.md` §18 擴充

⚠ **關鍵保護：** 既有 §18.1（長度限制）+ §18.2（格式限制）**不可改編號 / 不可改內容**。

在既有 §18.2 之後 append 兩個子節：

```markdown
### 18.3 高風險場景處理（來源：00_b §6；既有粗欄位「風格要求」抽出為獨立子節）

（本子節由 `/scene-task` 階段 2 從 `00_b §6` 抽取對應該場景類型的處理規則填入；若本場非告別/犧牲/和解高風險類型，留 `N/A`）

### 18.4 文風錨定（來源：01_d 文風樣本與指紋；新增）

**三層敘事比例（硬約束）：** 對話 60-70% / 旁白 20-25% / 其他 10-15%

**跨層硬約束：** 零破折號 / 旁白歸主角 / 內心 OS 寫旁白層

**本場出場角色指紋：**

（本子節由 `/scene-task` 階段 2 從 `01_world/01_d_文風樣本與指紋.md` 抽取對應本場出場角色的「量化指紋 + 正例前 3 句 + 負例全部」填入）

- 出場角色 X：
  - 對話句長：mean __ / median __
  - 標點密度：軟停 __ / 硬停 __ / 省略 __ / 破折 0
  - 特徵詞：__
  - 正例：__
  - 負例：__
```

### 變更 6：`.claude/skills/scene-task/SKILL.md` v0.1 → v0.2

在 §3.2 抽取來源表（10 行），在 `W-language` 行之後 insert 1 行（共 11 行）：

```diff
| `W-language` (`01_world/01_b_世界語言規格.md`, `01_world/01_c_陣營與階級語言.md`) | 本場相關陣營 / 階級的語言層級摘要 | `語言層級` |
+ | `W-style` (`01_world/01_d_文風樣本與指紋.md`) | 本場出場角色的量化指紋 + 正例前 3 句 + 負例 + 跨層硬約束 | `§18.4 文風錨定` |
| `V` (`02_vocabulary/02_a_專有名詞表.md`, ...) | 本場禁用詞 / 慎用詞 / 解禁詞 | `禁用詞與禁用句型` |
```

`header note` 升 v0.1 → v0.2：

```markdown
版本：v0.2（STYLE_ANCHOR v0.1 implementation；§3.2 抽取來源表新增 W-style 行；對應 task pack §18.4 文風錨定子節；指紋來源 = 01_world/01_d_文風樣本與指紋.md）
```

**邊界：** §3.2 表既有 10 行不可改編號、不可改內容；只新增 1 行。

### 變更 7：`.claude/skills/dialogue-write/SKILL.md` v0.2 → v0.3

在 Stage 1 診斷報告清單（既有 9 項）的 `upstream entity status list` 後、`planned write targets` 前 insert 1 項：

```diff
診斷報告：
- mode
- task pack path
- scene ID
- task-pack review-gate result
- six core field readiness
- non-core TODO list
- upstream entity status list
+ - 文風錨定狀態（task pack §18.4 是否齊全；指紋是否覆蓋本場出場角色；如缺漏標 WARN 但不 block 執行）
- planned write targets
- warnings, waivers, or experimental-source notes
```

`header note` 升 v0.2 → v0.3：

```markdown
版本：v0.3（STYLE_ANCHOR v0.1 implementation；Stage 1 診斷報告新增「文風錨定狀態」項；對應 task pack §18.4；不擴大寫檔邊界）
```

**邊界：** Stage 1 既有 9 項不動；只新增 1 項；不擴大 D-050 子裁決 2 寫檔範圍。

### 變更 8：`_design/DECISIONS_LOG.md` + `POST_LOCK_PENDING.md`

#### 8a. DECISIONS_LOG.md 新增 D-NNN

找 DECISIONS_LOG 既有 D-054 之後的下一個未用編號（推測為 D-055）。新增條目：

```markdown
### §6.18 D-055（pre-generation 文風錨定機制 / 01_d 新建 / 00_b §1.1 §1.2 擴充）

**日期：** YYYY-MM-DD（implementer 跑當天）
**提案：** `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1
**拍板：** user 第 10 輪選擇方案 A 重量級

**內容：**
- 新建 `01_world/01_d_文風樣本與指紋.md`（W-style entity）
- 擴 `00_b §1.1` `§1.2` instance-write zone
- 新增 `07_a §18.3` `§18.4` 子節
- `/scene-task` 抽 W-style → task pack §18.4；`/dialogue-write` Stage 1 加文風錨定狀態項
- D-053 scope **不擴大**；01_d 寫入走人類直接編輯（path A）

**邊界 reaffirm：**
- D-050 子裁決 2：`/dialogue-write` 寫檔範圍仍嚴格限 `08_dialogue_outputs/`，本拍板不擴大
- D-053：`/create-world` 寫 00_b §1/§2 exception 不延伸到 §1.1 §1.2；§1.1 §1.2 由人類編輯

**未涵蓋（屬未來 NEW_REQ 候選）：**
- QA 自動量化驗證
- /anchor-style 新 skill
- 第三方全知敘述者規範
- 跨作品文風樣本庫
```

#### 8b. POST_LOCK_PENDING.md 新增 NEW_REQ_20

找 POST_LOCK_PENDING 既有 NEW_REQ_19 之後的下一個未用編號（推測為 NEW_REQ_20）。新增條目：

```markdown
### NEW_REQ_20：pre-generation 文風錨定機制後續維護

**來源：** `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1 + D-055 拍板
**狀態：** PROCESSING（核心實作已透過 D-055 落地；以下為後續維護與擴張議題）

**子項：**
1. **指紋校準頻率**：每 5 個新增 Level 重跑 `_tools/fingerprint_analyzer.py` 校準 01_d 指紋；偏差 > 15% 須拍板是否更新基線
2. **QA 自動量化驗證**（未來 NEW_REQ）：句長/標點/特徵詞偏差自動 FAIL — 屬未來增強，當前 09_b 仍走定性檢查
3. **/anchor-style 新 skill**（未來 NEW_REQ）：自動更新 01_d 指紋 — 屬 D-053 scope 擴張議題
4. **第三方全知敘述者規範**（未來 NEW_REQ）：序章/終章/cut-scene 若需全知，另立 01_e 或併入 01_d 第四層
5. **諾拉 17 個技術詞同步 02_a 專有名詞表**（小修）：需檢查交叉一致性

**處理時機：** 視作品擴張到 Level 10+ 後逐項評估
```

**完成回報格式：**

完成 8 處變更後，print 摘要回報：

```markdown
## STYLE_ANCHOR_IMPL_STARTER batch 完成摘要

- 變更 1（00_b §1.1 §1.2）：✅ 寫檔 / lines: X
- 變更 2（01_world/01_d 新建）：✅ 寫檔 / lines: X / utf-8 decode OK
- 變更 3（entity_type_registry W-style）：✅ 新增條目
- 變更 4（expected_entities W-style）：✅ 新增條目
- 變更 5（07_a §18.3 §18.4）：✅ 既有 §18.1 §18.2 未動
- 變更 6（scene-task SKILL.md v0.2）：✅ §3.2 表 10 → 11 行
- 變更 7（dialogue-write SKILL.md v0.3）：✅ Stage 1 9 → 10 項
- 變更 8a（D-055 拍板）：✅ DECISIONS_LOG append
- 變更 8b（NEW_REQ_20 追蹤）：✅ POST_LOCK_PENDING append

## Verification

- grep 全 repo W-style reference 數：__（應該至少 5 處：01_d frontmatter / entity_type_registry / expected_entities / scene-task §3.2 / D-055 條目）
- 既有 07_a §18.1 §18.2 內容 hash 比對：unchanged ✅
- `01_world/01_d_文風樣本與指紋.md` 含本場 4 角色（清道夫 / 瑟琳 / 莉娜 / 諾拉）全名：✅
- Stage 1 診斷報告 mock：（貼一個 mock 範例 print 結果）

## Open questions 待 user 拍板

（如有遇到不確定的細節，列在這裡，否則寫 None）
```

**錯誤呈現規則：**

- 任何拒絕 / 越界 / 找不到的情況：印 `## ⏸ 條件未滿足 / Prerequisites Not Met`，列 What / Where / Why / 下一步，停止後續變更，等 user 拍板
- 不擅自越界、不擅自簡化、不擅自合併變更

**寫檔授權：**

- 每處變更前先 print preview（要寫的內容 + 路徑），等 user 回 `通過` / `OK` / `寫檔` 再寫
- 不要 batch 寫 8 處 — 每處單獨確認，避免一處錯全部 rollback

~~~

---

# 2. 個別檔案差異規格

本段是 §1 啟動 prompt 內已涵蓋的 8 處變更的擴充說明（implementer 如需更深背景參考）。所有設計權威 = STYLE_ANCHOR_PROPOSAL v0.1。

## 2.1 變更 1：`00_b §1.1` `§1.2` 完整內容

source = RFC §7.1 段落範例。implementer 直接拷貝該範例為 00_b §1.1 §1.2 落地內容；不擅自改寫。

既有 §1 內容（`/create-world` 寫入「《蟲潮孤堡》是黑色幽默...」）位置 ≠ §1.1 §1.2 — 不衝突。append 在既有 §1 段落之後、`---` 分隔線之前。

## 2.2 變更 2：`01_d` 完整章節結構

5 個 `# N. ...` 章節：

1. `# 1. 三層敘事結構比例` ← RFC §4.1（含 table：對話 64% / 旁白 22% / 其他 14%；含 ⚠ 發現 1+2）
2. `# 2. 全局文風指紋` ← RFC §4.2 + §4.4 + §4.6（含男主角雙層特殊性 / 標點密度表 / 旁白模式）
3. `# 3. Per 角色聲線樣本師`
   - `## 3.1 男主角_清道夫（MainCharacter）` ← RFC §6.1 全文（量化指紋 + 5 正例對話 + 5 正例旁白 + 3 負例對話 + 3 負例旁白）
   - `## 3.2 瑟琳（MainGirlA）` ← RFC §6.2 全文
   - `## 3.3 莉娜（MainGirlB）` ← RFC §6.3 全文
   - `## 3.4 諾拉（MainGirlC）` ← RFC §6.4 全文
4. `# 4. /scene-task 抽取規則` ← RFC §7.2 maintenance 段（5 項抽取規則）
5. `# 5. 維護規則` ← RFC §7.2 maintenance 段（4 項維護紀律）

預計檔案 400-600 行；建議用 Write tool 一次性寫入。寫完跑 `wc -l` + utf-8 decode 驗證。

## 2.3 變更 3 + 4：entity registry 雙寫

`entity_type_registry.yaml` 是 instance registry；`_design/expected_entities.yaml` 是 design registry（如該檔存在且為 entity 註冊 source）。

兩處都要加 W-style，否則 `/status` / `/check-gaps` 可能誤判 01_d 為未註冊實體。

## 2.4 變更 5：07_a §18 擴充

既有 §18.1 §18.2 由 user 在過去某輪寫入；不知道是否有 protocol-level 拍板保護。**保守處理：完全不動**，只在後面 append。

§18.3 §18.4 子節 stub 填法見 §1 啟動 prompt 內。

## 2.5 變更 6 + 7：skill 升版

兩個 skill 升版規則一致：

- 只新增 1 行/項，不改既有結構
- header note 寫變更摘要 + 對應 RFC 段
- 不擴大 D-050 寫檔範圍
- 不改 SKILL.md 的 `用途` / `觸發語` / `觸發協議` / `啟動前檢查` / `輸入` / `輸出` / `邊界` / `錯誤處理` 主要段

## 2.6 變更 8：拍板紀錄

D-055 + NEW_REQ_20 編號是推測（implementer 跑時請先確認 DECISIONS_LOG / POST_LOCK_PENDING 既有最大編號 + 1）。

D-055 條目格式對齊既有 D-050~D-054 條目體例（implementer 跑時請先 cat 既有條目 確認）。

---

# 3. 驗收條件（master 端 verify checklist）

master 收到 implementer 完成回報後，依下列 checklist verify：

## 3.1 grep 全 repo 一致性

- [ ] `grep -r "W-style" .` 至少 5 處命中（01_d / entity_type_registry / expected_entities / scene-task SKILL §3.2 / D-055）
- [ ] `grep -r "01_d_文風樣本與指紋" .` 至少 4 處命中（00_b §1.1 / scene-task SKILL §3.2 / dialogue-write SKILL 診斷段 / D-055）
- [ ] `grep -rn "§18.4" 07_scene_tasks/` 1 處命中
- [ ] `grep -rn "§18.1" 07_scene_tasks/` 仍存在（既有未動）

## 3.2 既有檔案保護驗證

- [ ] `00_b §1`「《蟲潮孤堡》是黑色幽默...」段落內容 unchanged（diff vs implementer 跑前版本）
- [ ] `07_a §18.1` 「長度限制」 + `§18.2` 「格式限制」內容 unchanged
- [ ] `entity_type_registry.yaml` 既有 7 個 core 條目 unchanged
- [ ] `scene-task SKILL.md` §3.2 表既有 10 行 unchanged
- [ ] `dialogue-write SKILL.md` Stage 1 既有 9 項 unchanged
- [ ] `03_b 主要角色聲線卡模板.md` v0.1 unchanged（per-character voice spec 留在原處）

## 3.3 內容完整性

- [ ] `01_d` 含 4 角色（清道夫 / 瑟琳 / 莉娜 / 諾拉）名字全出現
- [ ] `01_d` 含 RFC §4.1 三層比例表（64% / 22% / 14%）
- [ ] `01_d` 含 4 角色各自的量化指紋表 + 正例 + 負例
- [ ] `01_d` frontmatter 含 `entities: [W-style]`
- [ ] D-055 條目含「方案 A」「D-053 scope 不擴大」「path A 人類直接編輯」字樣

## 3.4 mock 跑驗證

- [ ] 對任一既有場景手動跑 `/scene-task`（或 dry-run），確認 mock task pack §18.4 出現完整指紋條目
- [ ] mock 跑 `/dialogue-write`，驗證 Stage 1 診斷報告含「文風錨定狀態」項

## 3.5 utf-8 decode

- [ ] `python3 -c "open('01_world/01_d_文風樣本與指紋.md', 'rb').read().decode('utf-8')"` 不報錯
- [ ] `wc -l 01_world/01_d_文風樣本與指紋.md` 在 400-600 行範圍

---

# 4. Open questions 待 user 拍板（implementer 跑前確認）

implementer 跑本 batch 前，user 應先決定下列問題：

## Q1（RFC §11.2 Q1）：00_b §1.x 寫入路徑

- **路徑 A（推薦）：** 人類直接編輯 00_b §1.1 §1.2；implementer 只 print preview 給 user 確認後落地
- **路徑 B：** 拍 D-NNN（與 D-055 合併或單獨拍）擴大 `/create-world` D-053 scope 涵蓋 §1.1 §1.2；implementer 落地時透過 `/create-world` 寫入

**本 starter 預設路徑 A**（implementer 直接寫，user 拍板確認）。

## Q2（RFC §11.2 Q2）：§10.4 量化驗證閾值

- 「mock 跑文風偏差度下降 ≥ 30%」門檻 implementer 是否要實際跑量化驗證？
- 或 user 接受任意定性改善都算 PASS？

**本 starter 預設定性 PASS**（implementer 不跑量化驗證；mock 跑只看 task pack §18.4 是否成功填入 + Stage 1 報告是否含新項）。

## Q3（RFC §11.2 Q3）：第三方全知敘述者

- 本次 implementer 不處理（屬未來 NEW_REQ）
- 但是否要在 01_d `# 1. 三層敘事結構比例` 加註「未來如需第四層全知敘事，另立 01_e」？

**本 starter 預設加註**（在 01_d # 1 章節結尾加 1 句）。

## Q4（RFC §11.2 Q4）：諾拉 17 個技術詞同步 02_a

- 諾拉指紋的 17 個技術詞（材料/實驗/控制/能源/核心/系統/研究/效率/修復/晶片/設備/物資/...）是否要交叉檢查 `02_vocabulary/02_a_專有名詞表.md`？
- 如不在 02_a 出現，是否要本 batch 順手加？

**本 starter 預設不處理**（屬 NEW_REQ_20 子項 5；scope 外）。

## Q5（RFC §11.2 Q5）：負例樣本來源

- 本提案 §6 負例是 design-time 寫的反模式（user 寫得太好，corpus 沒有真實負例）
- 是否要 implementer 手動跑一次 LLM 預設輸出，從中抽真實負例貼進 01_d？

**本 starter 預設不處理**（implementer 直接拷貝 RFC §6 負例；如未來需要真實負例，列入 NEW_REQ_20 子項）。

---

# 5. 相關 spec

- `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1（本 starter 的 source of truth）
- `_design/SPEC.md` §5.2 frontmatter canonical schema + §17.1 instance-write zone authority
- `_design/DECISIONS_LOG.md` §6.12 D-050（skill 寫檔邊界）+ §6.16 D-053（D-053 partial supersede）
- `_design/POST_LOCK_PENDING.md` v0.18（NEW_REQ 追蹤；本 batch 落地後升 v0.19）
- `_design/CODEX_D_W12_STARTER.md` v0.1（本 starter 採其 batch 模式 + 啟動 prompt 結構）
- `_design/HANDOFF_TO_10TH_MASTER.md` v1.0（本 batch 屬 10th master 加碼 scope；可加在主軸 1-5 後當補丁項）
- `_tools/fingerprint_analyzer.py`（量化分析工具；本 batch 不執行；維護階段才重跑）
- `00_protocol/00_a_台詞生產協議.md` §4.1 必備文件清單（本 batch 落地後可選擇是否新增 01_d 為必讀；屬可選的後續優化）

---

# 6. 附錄：implementer 對話開頭 quick-start

implementer 在新對話一打開先做下列 3 件事：

1. `Read` `_design/STYLE_ANCHOR_IMPL_STARTER.md`（本檔）— 看 §1 啟動 prompt
2. `Read` `_design/STYLE_ANCHOR_PROPOSAL.md`（752 行 RFC）— 全讀
3. `Read` `CLAUDE.md` 或 `AGENTS.md` — 看專案總規則

然後依 §1 啟動 prompt 內 8 處變更，**每處先 print preview，等 user 拍板再寫檔**。

# 7. 版本歷史

| 版本 | 日期 | 變更 |
|---|---|---|
| v0.1 | 2026-05-28 | 初版；對應 STYLE_ANCHOR_PROPOSAL v0.1；採 CODEX_D_W12_STARTER v0.1 batch 模式 |

# 8. 歷史紀錄 — 實際落地 vs starter 推測（2026-05-28）

本 starter 內含預測編號 — 落地時依實際 DECISIONS_LOG / POST_LOCK_PENDING 最近未用編號實際採用值如下：

| Starter 推測 | 實際落地 | 來源 |
|---|---|---|
| D-NNN（推測為 D-055）| **D-055** | DECISIONS_LOG §6.18 |
| NEW_REQ_20（推測下一個未用編號）| **NEW_REQ_21**（NEW_REQ_20 被 10th master M4 user-test follow-up 佔用）| POST_LOCK_PENDING line 964 |
| 既有 7 個 core 條目 | 實際 9 個 core 條目（W-rules / W-language / V / C / R / P / CH / S / A）| entity_type_registry.yaml |
| NEW_REQ_21 8 子項（5 + 3）| 落地時 9 子項（5 + 3 + 1 T10-d carry-over）| POST_LOCK_PENDING NEW_REQ_21 |

K-NN 表完整 9 條收斂入 HANDOFF_TO_10TH_MASTER §4.9（10th master patch round）。本 starter 內文不修保歷史 audit accuracy；status 改 APPLIED 標明 batch 已落地完成。
