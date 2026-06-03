狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-17  
適用範圍：資料格式 specialist 對話的啟動包  
優先級：高  

# SPECIALIST_STARTER — 資料格式

# 0. 對話啟動指令（直接複製貼到新對話）

```
我有一個 game-dialogue-bible 專案，進入並行 specialist 設計階段。
你是「資料格式 specialist」對話。

工作資料夾：<搬遷後的新路徑>

**第一步必讀（按順序）：**
1. _design/MASTER_PLAN.md（你的 scope 邊界）
2. _design/INTEGRATION_CONTRACTS.md（你跟其他 specialist 的介面契約）
3. _design/SPEC.md 第 5.2 節（既有 canonical schema，鎖定不擅動）
4. _design/SPEC.md 第 5.1、5.4 節（實體類型與 Expected Entity Manifest）
5. _design/references/CREATIVE_SCHEMA_PROPOSAL_FROM_HARNESS.md（另一份提案，reference only）
6. 本檔案（你的 starter）

**你的 scope（OWNS）：**
- 評估現有 canonical schema 是否需要擴充
- 處理本 starter 第 2 節列出的「強制檢視議題」
- 設計新增實體類型（若需要）
- 設計 Instance 特殊資料格式

**禁止越界：**
- 不設計下游 pipeline 流程（屬於上下游 specialist）
- 不設計 UI 呈現（屬於 UX specialist）
- 不擅自更動既有 canonical schema 的 7 種狀態 / 9 種 pipeline_state / 5 種 mode_tag / 4 種 qa_decision / 5 種 qa_type enum

**最終產出：**
- _design/DATA_FORMAT_SPEC.md（含「需 master 裁決問題清單」結尾段）

請先告訴我讀完上述文件後對 scope 的理解，再開始展開。
```

---

# 1. 你的 scope 詳細

## 1.1 主任務

評估並提案以下事項：

1. **現有 canonical schema 是否足夠** — 既有 SPEC 5.2 定義的中文 header 5 欄 + YAML block 上游 3 欄 + 下游 8 欄，是否能涵蓋所有實際使用情境
2. **強制檢視議題**（見第 2 節）
3. **新增實體類型的提案**（若需要）
4. **Instance 特殊資料格式**（user 提到的特殊需求；目前未知具體內容，需在對話中與 user 對齊）

## 1.2 禁止越界（再次強調）

- 不動 SPEC 已鎖定的 schema 核心：7 狀態、9 pipeline_state、5 mode_tag、4 qa_decision、5 qa_type
- 不設計 `/scene-task` `/dialogue-write` `/qa` 的流程細節
- 不設計呈現格式（包括 `/view-*` `/export-*`）

---

# 2. 強制檢視議題（必須在 SPEC 結尾回答結論）

以下議題來自 references/CREATIVE_SCHEMA_PROPOSAL_FROM_HARNESS.md 的分析，是另一個獨立思考路徑指出的真實盲點。

## 2.1 議題 A：retcon vs supersede 區分

**現有設計：** 用版本後綴（v01A、v02）+ 狀態升降（DRAFT → REVIEW → FINAL → LOCKED → DEPRECATED）

**問題：** 創作層的「retcon」（第 10 集說第 1 集那場戲沒發生）跟「修正錯字」是不同性質的變更，但現有狀態系統都用 DEPRECATED 表達。

**你要回答：**
- 是否要新增 frontmatter 欄位 `retcon_of: <被 retcon 的檔案路徑>` 或 `retcon_status: ACTIVE / RETCONNED`？
- 是否要新增狀態 `RETCONNED`（會影響 7 狀態 enum，需 master 裁決）？
- 是否在 09_quality_assurance/ 加一個 09_g_retcon_紀錄模板？

## 2.2 議題 B：多語言對白

**現有設計：** 完全沒考慮多語言

**問題：** 如果作品要做雙語版本（中／英），現有 schema 撐不住

**你要回答：**
- 是否要新增 frontmatter 欄位 `language: zh-Hant / en / ja / ...`？
- 多語言版本是「同一檔案多區段」還是「不同檔案 cross-reference」？
- 如果是後者，需要新欄位 `translation_of: <原檔案路徑>` 嗎？
- 若不支援，要在 SPEC 明確聲明「不支援多語言」嗎？

## 2.3 議題 C：continuity_check 是否獨立實體

**現有設計：** 跨集一致性檢查散在 09_quality_assurance/ 09_b（角色聲線）09_d（資訊控制），沒有獨立實體

**問題：** 跨集／跨場景的一致性檢查（例：第 3 集主角髮色黑色、第 7 集棕色）找不到統一的紀錄位置

**你要回答：**
- 是否新增實體類型 `CC-<id>` 或 `CC-<topic>`（continuity check）？
- 是否新增資料夾 `09_quality_assurance/continuity_checks/`？
- 若新增，跟現有 09_b/09_d 怎麼分工？

## 2.4 議題 D：scene 粒度

**現有設計：** 預設策略 A（一場戲一個 dialogue 檔）

**問題：** 高戲劇張力的長場景可能有 50+ 行對白，難以管理／引用

**你要回答：**
- 是否支援策略 B（exchange-level 細粒度），讓使用者選擇？
- 若支援，frontmatter 是否加 `exchange_in_scene: <number>` 欄位？
- 場景 ID 是否要擴充：`S-01-03-e2`（第 2 個 exchange）？
- 跟現有 O7 分支場景（`S-01-03a`）的 ID 命名是否衝突？

## 2.5 議題 E：protected_tier 多層保護

**現有設計：** 只有 LOCKED 狀態作為單層保護

**問題：** 商業專案／IP 合作可能需要分層權限（客戶可看 vs 編劇可看 vs 製作可看）

**你要回答：**
- **如果作品是個人專案**：明確聲明「不需要 protected_tier，LOCKED 已足夠」
- **如果作品是商業 / IP 合作**：是否新增 frontmatter 欄位 `protected_tier: public / collaborator / internal / client / locked`？
- 若新增，跟現有 LOCKED 狀態如何整合？

**這個議題使用者必須回答**：作品場景是個人還是商業。

## 2.6 議題 F：使用者的「特殊資料格式」需求

**user 之前提到：** 「這個工具會有特殊的資料格式需要設計和處理」

**現況：** 我們不知道具體是什麼

**你要回答：**
- 在對話中向 user 釐清具體是什麼資料格式（例：遊戲引擎匯出？玩家分支？配音資訊？本地化？）
- 設計對應的擴充方案

---

# 3. 必須產出的格式

## 3.1 DATA_FORMAT_SPEC.md 結構

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：資料格式 specialist 對話的結論
優先級：最高

# DATA_FORMAT_SPEC

## 0. 摘要
（一段話講清楚這份文件結論）

## 1. 既有 schema 評估
（5.2 是否足夠？哪些已涵蓋？）

## 2. 強制檢視議題的結論

### 2.1 議題 A：retcon vs supersede
- 結論：採用 / 不採用 / 部分採用
- 具體 schema 變更（若採用）
- 對既有檔案的遷移影響

### 2.2 議題 B：多語言對白
... 同上

### 2.3 議題 C：continuity_check 獨立實體
... 同上

### 2.4 議題 D：scene 粒度
... 同上

### 2.5 議題 E：protected_tier
... 同上

### 2.6 議題 F：使用者的特殊資料格式
... 同上

## 3. 新增 frontmatter 欄位清單（若有）
| 欄位 | 用途 | 出現條件 | 預設值 |

## 4. 新增實體類型清單（若有）
| 類型 | 用途 | ID 命名規則 |

## 5. 對既有 27 份模板 frontmatter 的遷移影響
（A.4 任務需要的補欄位）

## 6. 對 A.0 parser 的影響
（parser 要新增解析什麼）

## 7. 需 master 裁決問題清單
### 議題 1：<名稱>
- 涉及 scope：
- 提案方向：
- 替代方案：
- 等待裁決原因：
```

## 3.2 結尾必須有「需 master 裁決問題清單」

任何**動到既有鎖定 schema 的提案**、**新增 enum 值**、**新增實體類型**都必須升級 master。

---

# 4. 給 specialist agent 的提醒

1. 你的角色不是「重新設計整套 schema」 — 既有設計已通過 4 輪 CODEX 審查，是穩固基底
2. 你的角色是「**找出真實缺口、提案具體擴充**」
3. 拿不準時，標為「需 master 裁決」往上推，**不要擅自決定**
4. 對話結束時，要交一份結構化的 SPEC + 清單，不要交對話紀錄
5. 任何提案都要附「對既有 27 份模板的遷移影響」與「對 A.0 parser 的影響」
