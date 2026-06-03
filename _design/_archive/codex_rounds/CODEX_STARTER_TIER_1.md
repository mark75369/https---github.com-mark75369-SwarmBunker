狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-18  
適用範圍：CODEX 啟動包 — 級別 1（9 份協議檔撰寫）  
優先級：最高  

# CODEX_STARTER — 級別 1：協議檔撰寫線

# 0. 啟動指令（直接複製貼到新 CODEX 對話）

```
我有一個 game-dialogue-bible 專案，目前處於設計階段已 lock、實作分批啟動的狀態。
你是這個專案的 CODEX 實作 agent，本輪 scope 鎖定為「**級別 1：9 份協議檔撰寫**」。

工作資料夾：D:\劇本開發工具

**本輪 scope（嚴格限定）：**

只做下面 9 個 TASKS 項目；其他項目本輪一律不碰：

| TASKS | 產出檔案 | 內容權威來源 |
|---|---|---|
| A.1 | 00_protocol/00_b_反ai味檢查表.md（通用骨架） | _design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md 反推；移除全部蟲潮孤堡專屬內容 |
| A.2 | 00_protocol/00_i_專案初始化協議.md | SPEC.md §8「Instance Bootstrap 流程」+ 共通骨架 10 區段 |
| A.3 | 00_protocol/00_e_世界觀創建協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §1.1（11 議題完整 agent 提問腳本）+ §1.0.1-§1.0.3 共通細則 |
| B.0 | 00_protocol/00_l_關係創建協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §1.5（6 議題）+ §1.0.1-§1.0.3 |
| B.1 | 00_protocol/00_f_角色創建協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §1.2（9 議題）+ §1.0.1-§1.0.3 |
| B.2 | 00_protocol/00_g_大綱創建協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §1.3（7 議題）+ §1.0.1-§1.0.3 |
| B.3 | 00_protocol/00_h_細綱創建協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §1.4（7 議題）+ §1.0.1-§1.0.3 |
| D.0 | 00_protocol/00_k_台詞生產流程協議.md | UPSTREAM_DOWNSTREAM_SPEC.md §2（完整內容）+ §6 多場景並行 |
| D.1 | 09_quality_assurance/09_f_類型偏移檢查模板.md（通用骨架） | UPSTREAM_DOWNSTREAM_SPEC.md §3.5 |

**禁止越界（嚴重）：**

1. 不寫 scripts/parse_frontmatter.py（A.0 parser）— 等資料格式 specialist 第二輪交付
2. 不改 既有 27 份 Bible 模板的 frontmatter（A.4）— 等資料格式 specialist 確定 A-* schema
3. 不寫任何 .claude/skills/（A.5/6/7/8 起所有 skill 實作）— 等三 specialist + master 第四輪
4. 不寫前端工具任何檔案（HTML / JS / server）— 等 UX specialist 第二輪
5. 不擅自新增 entity 類型、不擅自新增 enum 值、不擅自新增 skill
6. 不擅動 SPEC.md / ARCHITECTURE.md / TASKS.md 內容
7. 不擅自把任何檔案狀態從 DRAFT 升 REVIEW
8. 不擅自補 Bucket lock 的新需求（i18n KEY / A-* / 09_g/h/i / SINGLE_ITER / 手稿導入細化等）— 那些屬其他 specialist 工作

**必讀文件（按順序）：**

1. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL；理解整個專案需求） 
2. _design/SPEC.md（v1.3；設計核心；本輪不動）
3. _design/ARCHITECTURE.md（v1.1；實作架構；本輪不動）
4. _design/TASKS.md（v1.2；任務拆解；本輪做其中 9 項）
5. _design/UPSTREAM_DOWNSTREAM_SPEC.md（≈ 3500 行；§1.0–§3 是 9 份協議檔的權威內容來源）
6. _design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md（A.1 反推來源）
7. 既有 00_protocol/ 內已存在的協議檔（如 00_a_台詞生產協議.md；理解現有風格）
8. 本檔（你的 starter）

**完成標準（每份協議檔）：**

- 標準中文 header 5 欄（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）依 TASKS §1.4
- YAML block：協議檔通常不貢獻實體，可省略 entities/depends_on/weight（依 SPEC §5.2.5）
- 內容完整對應 UPSTREAM 對應節（不擅自刪減 / 增補）
- 結構遵循「共通骨架 10 區段」（區段 1-9 沿用 §1.0.1，區段 10 為各協議專屬）
- 跑 python scripts/check_paths.py（如可跑）0 error
- 跑 python scripts/check_headers.py（如可跑）0 error

**Commit 慣例：**

每完成一份協議檔 commit 一次，message 格式：
- `A.1: add 00_b 反 AI 味檢查表 通用骨架`
- `A.2: add 00_i 專案初始化協議`
- `A.3: add 00_e 世界觀創建協議`
- ... 依此類推

**進度回報：**

每 commit 後簡短回報：
- 哪份檔案完成、行數、frontmatter 是否完整
- 對 UPSTREAM 對應節有無偏離（若有理由說明）
- 下一份是哪個

**全部完成後：**

- 在 _design/codex_tier_1_completion_report.md 寫驗收報告（每份檔的 commit hash + 行數 + 與 UPSTREAM 對應節對照）
- 此報告本身也要有標準中文 header（依 TASKS §1.4）

請先讀完上述 1-7 號文件，然後告訴我你對本輪 scope 的理解 + 預計執行順序，再開始寫第一份。
```

---

# 1. 你執行時要遵守的規則（CODEX 內部紀律）

## 1.1 一份協議檔的標準結構

依 SPEC §9「共通骨架 10 區段」：

```
1. 文件目的與適用範圍
2. 啟動條件（先決資料）
3. 階段 1：診斷模式
4. 階段 2：探索 / 補洞對話
5. 階段 3：收斂模式
6. 階段 4：Codex 執行模式（含「自動拆分」邏輯）
7. 階段 5：實體驗證（自動呼叫 /status）
8. 禁止事項
9. 缺漏處理規則（TODO / INFERENCE / CONFLICT 標記）
10. 專屬區段（各協議自行擴充）
```

區段 1-9 內容**直接從 UPSTREAM_DOWNSTREAM_SPEC §1.0.1 / §1.0.2 / §1.0.3 抽取**並對齊各協議專屬條件填入。

區段 10 從 UPSTREAM_DOWNSTREAM_SPEC 對應節（§1.1 / §1.2 / §1.3 / §1.4 / §1.5）抽取完整內容（每個議題的「為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答 跳題」5 欄）。

## 1.2 範例：A.3 寫 00_e 世界觀創建協議

對應 UPSTREAM §1.1（含 11 議題完整提問腳本）+ §1.0.1-§1.0.3 共通骨架。

骨架：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-18
適用範圍：世界觀創建協議 — /create-world skill 對應
優先級：最高

# 00_e 世界觀創建協議

# 1. 文件目的與適用範圍
[從 UPSTREAM §1.1.1 抽取]

# 2. 啟動條件
[從 UPSTREAM §1.1.1 抽取]

# 3. 階段 1：診斷模式
[從 UPSTREAM §1.1.1 + §1.0.1 抽取，含 11 議題預告]

# 4. 階段 2：探索 / 補洞對話
[從 UPSTREAM §1.1.1 抽取 11 議題順序表]

# 5. 階段 3：收斂模式
[從 UPSTREAM §1.1.1 收斂特殊事項抽取]

# 6. 階段 4：Codex 執行模式
[從 UPSTREAM §1.1.1 拆分執行抽取]

# 7. 階段 5：實體驗證
[從 UPSTREAM §1.1.1 抽取]

# 8. 禁止事項
[從 UPSTREAM §1.1.1 + §1.0.1 §8 抽取]

# 9. 缺漏處理
[從 UPSTREAM §1.1.1 + §1.0.1 §9 抽取]

# 10. 專屬區段 — 11 項議題 agent 提問腳本

## 10.1 世界類型快速分類
[完整對應 UPSTREAM §10.1：為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答 跳題]

## 10.2 世界規則最小集
[完整對應 UPSTREAM §10.2]

...

## 10.11 拆分規則確認
[完整對應 UPSTREAM §10.11]
```

## 1.3 A.1 通用骨架反 AI 味檢查表的特殊性

A.1 跟其他 8 份不同：來源不是 UPSTREAM，是反推。流程：

1. 完整讀 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`
2. 對每個段落判定：是「結構性內容」（保留）還是「作品專屬內容」（移除）
3. 把作品專屬部分替換為通用占位符（`<作品名>`、`<角色 A>`、`<反派 B>` 等）
4. 確認 SPEC §17.1 的 **7 個固定 section anchors** 全部含且順序正確：
   - `## 1. 作品類型語氣定位`
   - `## 2. 髒話尺度與死亡處理偏好`
   - `## 3. 規模定位`
   - `## 4. 類型偏移風險清單`
   - `## 5. 角色偏移檢查清單`
   - `## 6. 高風險場景的處理方式`
   - `## 7. 經驗累積的偏移案例`

**禁止：** 加任何作品專屬內容（蟲潮孤堡 / 黑翼 / 蟲災 / 瑟琳 / 莉娜 / 諾拉等都不可出現）。

## 1.4 D.0 寫 00_k 台詞生產流程協議的特殊性

00_k 是「下游流程協議」，UPSTREAM §2 完整內容約 600+ 行。對齊：

- 直接平移 UPSTREAM §2 全部內容到 00_k
- 含 10 區段共通骨架 + 下游專屬區段（場景狀態機 / 模式系統對應 / 多版本方向 / 5 份 QA 閱讀順序）
- 多場景並行（UPSTREAM §6）的相關內容也納入 00_k 對應段落

**注意：** 本輪 00_k **不含**：
- ✗ SINGLE_ITER mode（D-028，待第二輪上下游 specialist 設計具體 algorithm）
- ✗ i18n KEY 寫入規範（D-022，待第二輪資料格式 specialist 設計 schema）
- ✗ 手稿導入跳階段 use case（D-031，待第二輪上下游 specialist 文件化）
- ✗ 09_g / 09_h / 09_i QA 模板（D-026，本輪 D.1 只寫 09_f）

→ 寫 00_k 時這些「之後會加」的條目**標 TODO 註解**保留位置，例如：

```markdown
## 12.6 多版本方向規範

[本節描述既有三模式：試寫 / 破格 / 收斂]

<!-- TODO(D-028): SINGLE_ITER 模式 algorithm 待上下游 specialist 第二輪 UD-7 交付後補入 -->
```

## 1.5 D.1 寫 09_f 通用骨架的特殊性

09_f 是 QA 模板，UPSTREAM §3.5 完整提供模板結構（§3.5.1 通用版骨架 + §3.5.2 algorithm + §3.5.3 frontmatter + §3.5.4 蟲潮孤堡對齊）。

對齊：
- 直接平移 §3.5.1 通用版骨架
- §3.5.4「與蟲潮孤堡專案版的對齊」段在 09_f 模板裡可省略（因為是給 specialist 看的 meta 資訊，不是模板實際內容）

---

# 2. 你不要做的事（再次強調）

## 2.1 絕對不碰

- `scripts/parse_frontmatter.py`（A.0 — 等資料格式 specialist）
- 既有 27 份 Bible 模板的 frontmatter（A.4 — 同上）
- 任何 `.claude/skills/` 內檔案（A.5+ — 等三 specialist + master 第四輪）
- 任何前端工具相關檔（HTML / JS / server / 等）
- `_design/SPEC.md` / `ARCHITECTURE.md` / `TASKS.md` 內容修改

## 2.2 跨議題禁區

不要在本輪寫進去的內容（即使 UPSTREAM 有提到也標 TODO 留位）：

- 任何 **i18n KEY 機制**（屬 P-017 / D-022，待第二輪資料格式）
- 任何 **A-\* / I-\* / UI-\* / 新 entity 類型**（屬 D-023 / D-025）
- 任何 **09_g 節奏感 / 09_h 對話張力 / 09_i 跨場一致性**（屬 D-026，本輪只有 D.1 的 09_f）
- 任何 **SINGLE_ITER mode**（屬 D-028）
- 任何 **手稿導入 trust-level 細節**（屬 D-031）
- 任何 **entity 命名衝突 4 選項具體行為**（屬 D-033）
- 任何 **HTML 前端工具**（屬 D-029）
- 任何 **JSON+MD 雙吐 export skill**（屬 D-024）

## 2.3 升狀態紀律

- 所有新建檔案狀態 = `DRAFT`
- 不擅自升 REVIEW
- 不擅自升 FINAL
- 不擅自升 LOCKED
- 升狀態屬 REVIEW gate 任務（A.10 等），本輪不做

---

# 3. 你完成後該做的事

## 3.1 每份協議檔完成後

```bash
# 跑檢查腳本（如可跑）
python scripts/check_paths.py
python scripts/check_headers.py

# Commit
git add 00_protocol/<檔名>.md
git commit -m "<TASKS 編號>: add <檔名> ..."

# 進度回報到 chat
報告：
- 完成檔案：路徑
- 行數
- frontmatter 完整性
- 對 UPSTREAM §X.Y 對應節有無偏離（若有理由說明）
- 下一份：哪個 TASKS 項目
```

## 3.2 9 份全部完成後

寫 `_design/codex_tier_1_completion_report.md`：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：CODEX 級別 1 任務驗收報告 — 9 份協議檔
優先級：高

# CODEX_TIER_1_COMPLETION_REPORT

## 0. 摘要

本報告紀錄 CODEX 級別 1 任務（A.1, A.2, A.3, B.0-B.3, D.0, D.1）的完成狀態。

## 1. 完成檔案清單

| TASKS | 檔案 | Commit Hash | 行數 | 對應 UPSTREAM 節 | 對齊狀態 |
|---|---|---|---|---|---|
| A.1 | 00_protocol/00_b_反ai味檢查表.md | abc123 | 480 | references | 通用骨架完整 |
| A.2 | 00_protocol/00_i_專案初始化協議.md | def456 | 320 | SPEC §8 | 完整 |
| A.3 | 00_protocol/00_e_世界觀創建協議.md | ghi789 | 850 | UPSTREAM §1.1 + §1.0 | 11 議題全 |
| B.0 | 00_protocol/00_l_關係創建協議.md | ... | ... | UPSTREAM §1.5 + §1.0 | 6 議題全 |
| B.1 | 00_protocol/00_f_角色創建協議.md | ... | ... | UPSTREAM §1.2 + §1.0 | 9 議題全 |
| B.2 | 00_protocol/00_g_大綱創建協議.md | ... | ... | UPSTREAM §1.3 + §1.0 | 7 議題全 |
| B.3 | 00_protocol/00_h_細綱創建協議.md | ... | ... | UPSTREAM §1.4 + §1.0 | 7 議題全 |
| D.0 | 00_protocol/00_k_台詞生產流程協議.md | ... | ... | UPSTREAM §2 + §6 | 完整 |
| D.1 | 09_quality_assurance/09_f_類型偏移檢查模板.md | ... | ... | UPSTREAM §3.5 | 通用骨架完整 |

## 2. 對 UPSTREAM 對應節的偏離紀錄

[列出任何偏離 + 理由；理想是 0 偏離]

## 3. TODO 標記清單

[列出協議檔內標 TODO 留位的部分，與對應 D-NNN]

例：
- 00_k §12.6 SINGLE_ITER mode → TODO(D-028)
- 00_k §X i18n KEY → TODO(D-022)
- ...

## 4. 跑 check 腳本結果

[paste check_paths.py / check_headers.py 輸出]

## 5. 下一步

- 等資料格式 specialist 第二輪交付 → 進級別 2（A.0 parser + A.4 補完 + A.5 Bootstrap skill）
- 等三 specialist + master 第四輪整合 → 進級別 3（所有 skill 實作 + 前端工具）
```

---

# 4. 預估工期與里程碑

| 階段 | 工期估計 |
|---|---|
| 讀完必讀文件 + 確認 scope 理解 | 0.5-1 小時 |
| A.1 寫 00_b 通用骨架 | 1-1.5 小時 |
| A.2 寫 00_i Bootstrap | 0.5-1 小時 |
| A.3 寫 00_e 世界觀 | 1.5-2.5 小時 |
| B.0 寫 00_l 關係 | 1-1.5 小時 |
| B.1 寫 00_f 角色 | 1.5-2 小時 |
| B.2 寫 00_g 大綱 | 1-1.5 小時 |
| B.3 寫 00_h 細綱 | 1-1.5 小時 |
| D.0 寫 00_k 流程 | 1.5-2.5 小時 |
| D.1 寫 09_f 類型偏移 | 0.5-1 小時 |
| 驗收報告 | 0.5 小時 |
| **總計** | **10-15 小時** |

---

# 5. 給 CODEX 的提醒

1. **scope 嚴格限定** — 看到 UPSTREAM 提了 SINGLE_ITER 之類本輪外的東西，不要實作，標 TODO 留位
2. **不擅動 UPSTREAM** — 你的角色是「把 UPSTREAM 翻成可執行的協議檔」，不是「重新設計」
3. **保持 DRAFT** — 所有檔案狀態 DRAFT，不擅自升級
4. **commit 頻繁** — 每份一個 commit，message 對應 TASKS 編號
5. **進度可見** — 每完成一份就回報，user 才好驗證對齊
6. **遇到衝突上報** — 如果 UPSTREAM 跟 SPEC 衝突，不擅自決定，回報給 user 裁決
7. **跑得到的 check 腳本就跑** — check_paths.py / check_headers.py 如可跑就跑；若不能跑或不存在，標明跳過
