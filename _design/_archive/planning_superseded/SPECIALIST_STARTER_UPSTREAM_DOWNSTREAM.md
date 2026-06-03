狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-17  
適用範圍：上下游完整設計 specialist 對話的啟動包  
優先級：高  

# SPECIALIST_STARTER — 上下游完整設計

# 0. 對話啟動指令（直接複製貼到新對話）

```
我有一個 game-dialogue-bible 專案，進入並行 specialist 設計階段。
你是「上下游完整設計 specialist」對話。

工作資料夾：<搬遷後的新路徑>

**第一步必讀（按順序）：**
1. _design/MASTER_PLAN.md（你的 scope 邊界）
2. _design/INTEGRATION_CONTRACTS.md（你跟其他 specialist 的介面）
3. _design/SPEC.md 全部（你的工作基礎）
4. _design/ARCHITECTURE.md 第 6 節（下游 skill 實作框架）
5. _design/TASKS.md 第 5 節（Phase D 任務）
6. 既有檔案：00_protocol/00_a 台詞生產協議.md（既有 1400+ 行方法論，必讀）
7. 既有檔案：07_scene_tasks/07_a 單場台詞任務包模板.md
8. 既有檔案：08_dialogue_outputs/08_a 台詞版本管理規範.md、08_b 生成台詞檔案模板.md
9. 既有檔案：09_quality_assurance/09_a–09_e（既有 QA 模板）
10. 本檔案（你的 starter）

**你的 scope（OWNS）：**
- 5 份上游創建協議（00_e / 00_f / 00_g / 00_h / 00_l）的內容展開
- 下游 00_k 台詞生產流程協議的內容展開
- /dialogue-write 多版本生成 algorithm 細節
- /qa 的 5 份報告生成細節 + 09_a–f QA 模板內容展開
- 09_e 定稿變更紀錄模板內容
- Canon delta 回寫機制設計（Phase D 後成熟期功能）

**禁止越界：**
- 不改 frontmatter canonical schema（屬於資料格式 specialist）
- 不設計 UI 呈現（屬於 UX specialist）
- 不更動 SPEC 已通過 4 輪審查的部分（需要動就回報 master 裁決）
- 不新增 pipeline_state / mode_tag enum 值（升級 master）

**最終產出：**
- _design/UPSTREAM_DOWNSTREAM_SPEC.md（含「需 master 裁決問題清單」結尾段）

請先告訴我讀完上述文件後對 scope 的理解，再開始展開。
```

---

# 1. 你的 scope 詳細

## 1.1 上游 5 份協議的內容展開

對每份協議，把 SPEC 第 9 節「共通骨架 10 區段」+ 第 10 節「專屬區段」轉成可執行的協議內容。

| 協議 | SPEC 對應 | 展開重點 |
|---|---|---|
| 00_e 世界觀創建協議 | 10.1（11 項專屬區段） | 把 11 項從清單變成具體引導步驟 |
| 00_f 角色創建協議 | 10.2（9 項） | 同上 |
| 00_g 大綱創建協議 | 10.3（7 項） | 同上 |
| 00_h 細綱創建協議 | 10.4（7 項） | 同上 |
| 00_l 關係創建協議 | 10.5（7 項） | 同上 |

**展開的具體做法：**
- 每個專屬區段定義「對話 agent 應該怎麼問使用者」「使用者預期回答什麼」「agent 怎麼把回答整理成檔案內容」
- 結合 00_a 既有方法論（10 種模式、台詞品質規則、禁用句型等）
- 各協議的拆分規則（把整合內容拆到具體分拆檔的邏輯）

## 1.2 下游 00_k 台詞生產流程協議的完整展開

SPEC 第 12 節已定義框架，你要把它展開為可執行協議。

**重點：**
- 場景狀態機（SPEC 12.3）的轉移觸發條件與檢查項
- 與 00_a 模式系統的完整對應（SPEC 12.4）
- 多版本方向規範（SPEC 12.6）的具體 algorithm
- 5 份 QA 報告閱讀順序的執行邏輯（SPEC 12.7）

## 1.3 6 份 QA 模板內容展開（D-004 / D-008 修正：原誤寫「9 份」）

| 模板 | 對應 qa_type | 展開重點 |
|---|---|---|
| 09_a AI 味 QA | AI_FLAVOR | 高風險詞、句型、套路的檢查清單 |
| 09_b 角色聲線一致性 | VOICE_CONSISTENCY | 去名測試的具體執行 |
| 09_c 禁用詞檢查 | FORBIDDEN_WORD | 機械詞表比對的演算法 |
| 09_d 資訊控制檢查 | INFO_CONTROL | 提前劇透 / 視角超出檢查 |
| 09_e 定稿變更紀錄 | （不屬 QA） | 人類在 final-gating 時的紀錄格式 |
| 09_f 類型偏移檢查 | GENRE_DRIFT | 作品專屬偏移檢查（從 00_b 衍生） |

## 1.4 Canon delta 回寫機制（SPEC 12.8 成熟期功能）

當台詞定稿後揭露之前 Bible 沒寫清楚的設定時：
- 怎麼識別 canon delta？
- 怎麼把 delta 提案給使用者？
- 使用者拍板後怎麼寫回 Bible？
- 寫回時跟原 Bible 的 supersede / retcon 機制怎麼互動？

## 1.5 多場景並行處理（TASKS 提到但 race condition 未處理）

當使用者同時對多個場景跑 `/scene-task` 或 `/dialogue-write`：
- 怎麼避免 `.protocol_version.phase_log` 寫入衝突？
- 怎麼避免兩個 skill 同時想升級同一份檔案的狀態？

## 1.6 禁止越界（再次強調）

- 不改 frontmatter canonical schema 的核心 enum
- 不擅自新增實體類型（升級 master）
- 不設計 UI 呈現方式（用 `[UX]` 標記回報，留給 UX specialist）

---

# 2. 強制檢視議題

## 2.1 與資料格式 specialist 的依賴

**等待資料格式 specialist 對以下議題的結論：**

- retcon 機制 → 影響 09_a–f 是否需要新類型、canon delta 怎麼處理 retcon
- 多語言對白 → 影響 /dialogue-write 是否要產多語版本
- continuity_check 獨立實體 → 影響 QA pipeline
- scene 粒度 → 影響 07_a 任務包與 08_b 台詞檔結構

**如果資料格式 specialist 先跑完，你拿到結論再展開。**
**如果平行跑，把這些議題標為「等資料格式 specialist」**，先做不依賴的部分。

## 2.2 各協議的「使用者引導風格」決策

SPEC 上游 10 區段共通骨架已定，但「agent 應該怎麼問問題」的細節風格未定。

例：問世界觀時，是「直接列 30 題」還是「先讓使用者貼長假設、agent 反問補洞」？

- 第一種：問答精靈式
- 第二種：場景化對話式（SPEC Q10=B 已選此）

確認你採用後者，並設計具體 agent 提問腳本。

---

# 3. UPSTREAM_DOWNSTREAM_SPEC.md 必含結構

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：上下游 specialist 結論
優先級：最高

# UPSTREAM_DOWNSTREAM_SPEC

## 0. 摘要

## 1. 上游 5 份協議展開
### 1.1 00_e 世界觀創建協議（完整內容）
### 1.2 00_f 角色創建協議（完整內容）
### 1.3 00_g 大綱創建協議（完整內容）
### 1.4 00_h 細綱創建協議（完整內容）
### 1.5 00_l 關係創建協議（完整內容）

## 2. 下游 00_k 完整內容

## 3. 6 份 QA 模板內容
### 3.1 09_a 至 09_f 各模板的具體欄位與檢查邏輯
### 3.2 09_e 定稿變更紀錄格式

## 4. Canon delta 機制

## 5. 多場景並行處理

## 6. 與 UI/UX specialist 的 [UX] 標記清單
（給 UX specialist 處理）

## 7. 與資料格式 specialist 的依賴項目
（明列等待哪些議題的結論）

## 8. 需 master 裁決問題清單
```

---

# 4. 給 specialist agent 的提醒

1. 你的工作量是 3 個 specialist 中最大的（多份協議要展開）
2. **不要把 00_a 既有方法論重寫** — 它已 1400+ 行，是參考來源
3. **完整內容**意思是「可以直接給 CODEX 在 Phase A.3 / B.1–3 / B.5b / D.0 / D.1 使用」，不是抽象描述
4. 對話結束時要交完整的 UPSTREAM_DOWNSTREAM_SPEC.md
5. 如果發現 SPEC 已鎖定部分有問題，標清楚，升級 master
