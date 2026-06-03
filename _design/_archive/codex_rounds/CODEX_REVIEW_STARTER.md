狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-18  
適用範圍：CODEX 第二輪深度審查 (c) 時機的啟動包  
優先級：高  

# CODEX_REVIEW_STARTER — 三 specialist v0.x 全交付後的跨 spec 深度審查

# 0. 本檔用途

當以下三件事**全部成立**時，把本檔 §1 內的 prompt 整段複製貼到新 CODEX 對話，啟動「**跨 spec 深度審查**」（時序對應 master 規劃的「(c) 時機」）：

- [ ] DATA_FORMAT_SPEC.md v0.1 交付 + git push
- [ ] UPSTREAM_DOWNSTREAM_SPEC.md v0.2 交付 + git push
- [x] UX_SPEC.md v0.2 交付 + git push（已完成）

→ 三項全勾後 → 啟動本啟動包

**本檔不取代** master 第四輪整合對話 — CODEX 深度審查產出後，master 第四輪要消化 CODEX 報告再做整合。

**搭配傳統：** 跟之前 SPEC/ARCH/TASKS 經歷的 4 輪 CODEX 審查模式對齊。本輪是「第二代 SPEC 雛形 + 第二輪 specialist 交付」後的第 5 輪 CODEX 審查。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「三 specialist 第二輪 spec 交付完成後、master 第四輪整合對話開始前」的**跨 spec 深度審查**。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 main / master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔
- 你是 cross-spec auditor — 檢視三 specialist 第二輪 spec 之間 + 跟既有 SPEC/ARCH/TASKS LOCKED 段落的一致性
- 你是 master 第四輪整合的 prep — 你的報告是 master 重啟整合對話的核心輸入
- 對應傳統：本輪是「第二代 SPEC 雛形」的第 5 輪 CODEX 審查（前 4 輪在時期 A 已完成）

---

**必讀文件（按順序，最新權威優先）：**

A. 最高權威 — 需求 + 決策層
1. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL — 4 bucket 拍板的需求快照）
2. _design/DECISIONS_LOG.md（v0.7+ — 含 D-001~D-036 + P-001~P-030）

B. 設計層 — 4 輪 CODEX 審查 LOCKED 的基底
3. _design/SPEC.md（v1.3 — 18 項設計決策 + canonical schema + 邏輯實體）
4. _design/ARCHITECTURE.md（v1.1）
5. _design/TASKS.md（v1.2）

C. Specialist 第二輪交付（本輪審查重點）
6. _design/DATA_FORMAT_SPEC.md（v0.1 — 資料格式 specialist 新交付）
7. _design/UPSTREAM_DOWNSTREAM_SPEC.md（v0.2 — 上下游 specialist 第二輪交付）
8. _design/UX_SPEC.md（v0.2 — UX specialist 第二輪交付，4381+ 行含 §11 HTML 前端工具大塊）

D. Specialist 啟動包與分析素材（參考）
9. _design/UX_PROTOTYPE_ANALYSIS.md（v0.1 — D-035 雙頁架構 + D-036 保留 4 元件）
10. _design/refactor_reference/UI_UX_SPEC.md（既有 Prototype Round 2.1 spec）
11. _design/INTEGRATION_CONTRACTS.md（v1 過渡版 — Contract A/B/C 介面狀態）
12. _design/REVISED_WORK_ITEMS.md（v0.2 §7 — 三 specialist 第二輪 39 條任務清單）

E. CODEX Tier 1 已寫的 9 份協議檔（一致性對照基底）
13. 00_protocol/00_b_反ai味檢查表.md
14. 00_protocol/00_e_世界觀創建協議.md
15. 00_protocol/00_f_角色創建協議.md
16. 00_protocol/00_g_大綱創建協議.md
17. 00_protocol/00_h_細綱創建協議.md
18. 00_protocol/00_i_專案初始化協議.md
19. 00_protocol/00_k_台詞生產流程協議.md
20. 00_protocol/00_l_關係創建協議.md
21. 09_quality_assurance/09_f_類型偏移檢查模板.md

F. 過渡完成度報告與 starter（參考）
22. _design/PHASE_3_COMPLETION_REPORT.md（v4.0 草稿）
23. _design/GAP_ANALYSIS.md（v0.2）

---

**審查 scope — 五大檢查維度：**

**1. 跨 spec 一致性（Contract A/B/C 真實介面對齊）**
- 資料格式 DF-3/4/5/6/7 設計的 schema vs 上下游 UD-2/5/6 / UX §9 [NEEDS_SCHEMA_SUPPORT] 的引用 — 對得上嗎？
- 上下游 UD-3 export skill 設計 vs 資料格式 DF-7 JSON schema — 形狀一致嗎？
- 上下游 UD-2 跳階段手稿導入 vs UX §11.5 LOCKED 守門引導 — 流程銜接嗎？
- UX §11.3 F3 三欄並排 vs 上下游 UD-7 SINGLE_ITER + UD-6 09_g/h/i — 場景一致嗎？
- UX §11.6 通用 CopyCommandButton 範圍 vs 各 specialist 對 A 路徑「複製指令」的需求 — 一致嗎？

**2. 跟 SPEC LOCKED 段落的細節衝突**
- specialist 的方案有沒有不小心動到 SPEC §5.2 canonical schema 核心欄位？
- SPEC §5.1 既有 7 種 entity 類型有沒有被超出（除 A-* 已拍板）？
- SPEC §5.2.4 三維度狀態 enum 擴展（qa_type 加 RHYTHM/DRAMATIC_TENSION/CROSS_SCENE_CONTINUITY、mode_tag 加 SINGLE_ITER）有沒有跟既有 9 種 pipeline_state 對齊？
- SPEC §16 文件狀態機 LOCKED→DEPRECATED 路徑 vs UX §11.5 「手動降級引導」一致嗎？
- SPEC §17 作品專屬 00_b 7 個 section anchors vs CODEX Tier 1 寫的 00_b 對得上嗎？

**3. specialist 漏項 / 越界**
- DF-1~11 / UD-1~12 / UX-1~17 各自 owned 的任務有沒有漏 deliverable？
- 有沒有 specialist 越界改了不屬於自己 scope 的東西？（凡 spec 內標 [NEEDS_SCHEMA_SUPPORT] / [UX] / 升 master 都 OK；直接改才算越界）
- D-021~D-036 + P-021~P-030 在 spec 內有沒有被正確消化或回應？

**4. 實作可行性（從 CODEX Tier 1 出發看 Tier 2 能不能跑）**
- A.0 parser 拿 DF-7 JSON schema + DF-5 entity registry + DF-3 i18n KEY schema — 能不能寫得出來？
- A.5 `/init-project` 拿 DF-2 phase_log 加 status + import_source 欄位 — 能不能寫得出來？
- 09_g/h/i 拿 UD-6 algorithm — 能不能由 CODEX 對應寫 09_g/h/i.md 模板？
- HTML 前端工具拿 UX §11 完整設計 — 能不能由 CODEX 直接動工寫前端 code？
- 任何「specialist 寫得太抽象，CODEX 看不懂怎麼實作」的地方都要標出

**5. master 第四輪整合的優先處理建議**
- 哪些議題是必須 master 拍板才能推進的（給 master 整合對話排優先序）
- 哪些 P-021~P-030 已被 specialist 提案 → promote 為 D-NNN 的優先序
- 哪些 spec 之間的衝突需要 master 仲裁
- 哪些 SPEC/ARCH/TASKS 段落需要在第四輪整合時補入新內容（specialist spec 已成熟可整合）

---

**禁止：**

- 不擅自修改任何 spec 檔 / SPEC / ARCHITECTURE / TASKS / 9 份協議檔
- 不擅自做 master 整合工作（整合屬第四輪 master 對話，本輪只審不改）
- 不擅自 supersede 任何已 LOCKED 決策
- 不重新設計（reviewer 不是 designer）
- 不在報告內塞「建議重新討論的議題」當作主體 — 你的工作是找問題，不是設計問題

---

**產出：** `_design/codex_round_5_deep_review.md`

結構：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：CODEX 第 5 輪深度審查報告 — 三 specialist v0.x + master 文件跨 spec 一致性
優先級：最高

# CODEX_ROUND_5_DEEP_REVIEW

## 0. 摘要
（一段話：審了什麼、找到 N 項問題、severity 分布、master 第四輪建議優先處理項數）

## 1. 跨 spec 一致性問題
### 1.1 Contract A（資料格式 → 上下游）對齊
（逐項列）
### 1.2 Contract B（上下游 → UX）對齊
### 1.3 Contract C（UX → 資料格式 feedback loop）對齊

每項格式：
- **問題**：（一句話描述）
- **嚴重度**：critical / major / minor
- **涉及檔**：spec 路徑 + 行號
- **建議**：（給 master 第四輪整合的指引）

## 2. 跟 SPEC LOCKED 段落的細節衝突
（逐項列，同上格式）

## 3. specialist 漏項 / 越界
### 3.1 漏項清單
### 3.2 越界清單
### 3.3 D-021~D-036 / P-021~P-030 在 spec 內的消化狀態（表格）

## 4. 實作可行性疑慮
### 4.1 A.0 parser 視角
### 4.2 A.5+ skill 實作視角
### 4.3 09_g/h/i 模板實作視角
### 4.4 HTML 前端工具實作視角
### 4.5 其他 Tier 2/3 任務的可行性

## 5. Master 第四輪整合優先處理建議
### 5.1 必須拍板（critical）
### 5.2 建議拍板（major）
### 5.3 可延後（minor）
### 5.4 P-NNN promote 建議優先序
### 5.5 主 SPEC/ARCH/TASKS 整合條目清單（哪些需要在第四輪整合時補入主文件）

## 6. 報告本身的限制與保留
- 哪些審查維度因 spec 不夠成熟而無法深入
- 哪些議題需要 specialist 二修才能再審
- 跟前 4 輪 CODEX 審查比的 coverage 對照

## 7. 後續審查建議
- (d) 時機 — master 第四輪整合完後是否還需再審
- A.0 啟動前是否需 Phase 6 審查
```

---

**Commit 紀律：**

- 寫報告本身時持續存檔（不必中間 commit）
- 報告完成時 git add + commit + push origin master
- Commit message: `CODEX round 5 deep review: <N> issues found across <X> dimensions`

**進度回報：**

每完成一個審查維度（§1~§5）回 chat 短報告：
- 該維度找到多少問題
- severity 分布
- 是否有需要 user / master 中途裁決的議題

**工期估計：** 6-10 小時 CODEX 工時（含讀 + 分析 + 寫報告）

請先讀完 1-12 號文件（A/B/C 三層），告訴我你對審查 scope 的理解 + 預計執行順序，再開始寫第 5 輪深度審查報告。
```

---

# 2. 觸發前的檢查清單（給 user 用）

啟動 CODEX 深度審查前確認：

| 檢查項 | OK 不？ |
|---|---|
| DATA_FORMAT_SPEC.md v0.1 存在於 `_design/` | [ ] |
| UPSTREAM_DOWNSTREAM_SPEC.md 已升 v0.2 | [ ] |
| UX_SPEC.md 已升 v0.2 | [x] ✅ |
| 三份 spec 都已 git push 到 GitHub | [ ] |
| DECISIONS_LOG.md 是 v0.7 或更新 | [x] ✅ |
| REQUIREMENTS_LOCK.md v1.0 FINAL 存在 | [x] ✅ |
| UX_PROTOTYPE_ANALYSIS.md v0.1 存在 | [x] ✅ |

→ 7 項全勾 → 開新 CODEX 對話 → 貼 §1 prompt

---

# 3. CODEX 報告交付後的流程

```
CODEX 寫完 codex_round_5_deep_review.md + push
        ↓
user 通知 master 對話（這個對話可繼續，或新開 master 整合對話）
        ↓
master 第四輪整合對話開動：
  1. 讀 codex_round_5_deep_review.md
  2. 處理 §1~§4 的 critical / major 問題
  3. 依 §5.1~§5.5 順序整合
  4. promote P-NNN → D-NNN
  5. 升 INTEGRATION_CONTRACTS v2
  6. 主 SPEC/ARCH/TASKS 整合
  7. 修訂 PHASE_3_COMPLETION_REPORT v4.0 final
  8. 重評可進 A.0
        ↓
若全通過 → CODEX Tier 2 啟動（A.0 parser → A.4 frontmatter 補完 → A.5+ skill → 前端工具）
若有議題未解 → 第五輪 specialist refine 或開新對話處理
```

---

# 4. 版本演化軌跡

| 階段 | DECISIONS_LOG | INTEGRATION_CONTRACTS | PHASE_3_COMPLETION_REPORT |
|---|---|---|---|
| 時期 A (4 輪 CODEX 審查) | — | — | — |
| 時期 B/C v0.1-0.5 | v0.5 | v0.4 過渡 | v3.0 過渡 |
| 新 master 接手 v0.6 | v0.6 | v1 過渡 | v3.0 過渡 |
| Bucket lock | v0.7 | v1 過渡 | v4.0 草稿 |
| **三 spec 交付 + CODEX 細審** | **v0.7** | **v1 過渡** | **v4.0 草稿** |
| Master 第四輪整合 | → v1.0 | → v2 正式 | → v4.0 final |
| A.0 解除 | LOCKED | LOCKED | final |
