狀態：LOCKED  
版本：v4.0 FINAL（master 第四輪整合 + specialist v0.4 patch + CODEX (c) + (d) + (d2) 全部 PASS）  
最後更新：2026-05-19  
適用範圍：Master 整合 Phase 3 完成度報告 / Phase A.0 解除條件評估  
優先級：最高  

# PHASE_3_COMPLETION_REPORT — Master 整合對話完成度報告

# 0. 本檔定位

**本檔由 v4.0 草稿升 v4.0 FINAL（2026-05-19，master 第四輪整合對話）。**

**v4.0 草稿 → v4.0 FINAL 升版條件全部達成：**

- ✓ 三 specialist 第二輪 + v0.3 patch 全部交付
- ✓ CODEX (c) 深度審查 17 衝突 + 5 越界全部收斂
- ✓ master 第四輪 D-037 ~ D-046 全部拍板
- ✓ 主 SPEC v1.1 / ARCHITECTURE v1.2 / TASKS v1.3 partial supersede 完成
- ✓ INTEGRATION_CONTRACTS v2.0 正式版產出（A.1~A.8 / B.1~B.8 / C.1~C.5 全部具體化）
- ✓ L3_EXPORT_PROMPT_SCHEMA v0.1 新建（master 對齊 D-038 A1 prompt 流程）
- ✓ Phase A.0 解除條件評估完成（§6.2 五項條件全 ✓）

本檔涵蓋：
- v3.0 過渡版 + 本輪 Bucket #1-#4 拍板的整合摘要
- 三 specialist 第二輪啟動就緒度
- A.0 暫停狀態的更新（仍暫停，但解除條件已更新）
- 對應 master 第四輪整合對話的接手指引

**搭配文件：** `REQUIREMENTS_LOCK.md` v1.0 / `GAP_ANALYSIS.md` v0.2 / `REVISED_WORK_ITEMS.md` v0.2 / `DECISIONS_LOG.md` v0.6

---

# 1. 裁決一句話

**A.0 仍暫停，但阻塞性質改變了。**

v3.0 時的阻塞 = 「UX §2-§6 未交付 + 上下游 §9 未對齊 + DATA_FORMAT 釐清未完」 — 純 specialist 工作未完。

**v4.0 草稿時的阻塞 = user 需求面已完整 lock，剩三 specialist 第二輪需執行設計細化 + master 第四輪整合。** 阻塞清楚、路徑明確、可立即啟動。

---

# 2. 版本修正紀錄

| 版本 | 日期 | 修正內容 |
|---|---|---|
| v1.0 | 2026-05-18 上午 | 誤判 UPSTREAM ≈ 15%，結論「需大幅重做第二輪」 |
| v2.0 | 2026-05-18 下午 | 修正 UPSTREAM 實際 ≈ 90%；重新評估阻塞點為 UX §2-§6 |
| v3.0 | 2026-05-18 | 初代 master 補充裁決：D-018 promote D-001a 6 議題為最終；P-009 ~ P-015 降為 Pending；暫停所有 A.0+ 啟動 |
| **v4.0 (草稿)** | 2026-05-18 | **新 master 對話接手：需求 refresh + Bucket #1-#4 完整拍板；D-019 ~ D-034 新增；P-016 ~ P-020 RESOLVED；P-021 ~ P-030 新增 [SPECIALIST_TBD]** |

---

# 3. 對照 MASTER_PLAN §6「完成標準」逐項判定（v4.0 FINAL）

| # | 完成標準 | v3.0 狀態 | v4.0 草稿狀態 | **v4.0 FINAL 狀態（2026-05-19）** |
|---|---|---|---|---|
| 1 | 三份 specialist spec 已通過 master 整合 | △ UPSTREAM ≈90% / UX ≈40% / DATA_FORMAT 0% | △ 需求 lock 完成第二輪可啟動 | **✓ 三 specialist v0.3 patch 全部交付**（DF v0.2 / UD v0.3 / UX v0.3；CODEX (c) 17 衝突全部 RESOLVED via D-037~D-046）|
| 2 | INTEGRATION_CONTRACTS 升 v1（過渡版） | △ 已升 v1 過渡版 | △ v2 待第二輪後 | **✓ INTEGRATION_CONTRACTS v2.0 正式版產出**（A.1~A.8 / B.1~B.8 / C.1~C.5 全部具體化；1777 行） |
| 3 | 主 SPEC/ARCHITECTURE/TASKS 整合 specialist 產出 | △ 已整合 D-018 / P-009 ~ P-015 / UPSTREAM substantive | △ Bucket lock 的 D-021~D-034 尚未整合到主文件 | **✓ 主 SPEC v1.1 / ARCH v1.2 / TASKS v1.3 partial supersede 完成**（保留原段 + 加 v1.1/v1.2/v1.3 標註；對齊 D-024~D-046） |
| 4 | `_design/` 結構乾淨 | △ UPSTREAM 缺 §9 / UX 多塊 Batch 補完 / DATA_FORMAT 不存在 | △ + REQUIREMENTS_LOCK.md（v1.0 FINAL）+ GAP/REVISED v0.2 | **✓ 結構乾淨**：三 spec v0.3 + 主 SPEC v1.1 + ARCH v1.2 + TASKS v1.3 + INTEGRATION_CONTRACTS v2.0 + L3_EXPORT_PROMPT_SCHEMA v0.1 + DECISIONS_LOG v0.8（待升 v1.0）|
| 5 | 可進 Phase A.0 實作 | ✗ | ✗ 暫停維持，解除條件更新 | **✓ Phase A.0 解除條件全達成（§6.2）— 可進 A.0** |

**合計：5 項全 ✓ — Phase 3 完整收斂；可進 Phase A.0。**

---

# 4. 新 master 對話完成的工作（v4.0 新增）

## 4.1 階段 1：盤點 + 報告現狀

讀完 15 份既有文件 + 既有 4 份 master 文件，向 user 完整報告現狀。

## 4.2 階段 2：需求 refresh 接受 + 初步分析（Gap Analysis）

- 接受 user 提供的 `REQUIREMENTS_REFRESH` v0.1
- 產出 `GAP_ANALYSIS.md` v0.1（缺口分析 + 衝突盤點）
- 產出 `REVISED_WORK_ITEMS.md` v0.1（任務拆解）
- 更新 `DECISIONS_LOG.md` v0.5（標 P-006/007/008 為 RESOLVED + D-019/020 + P-016 ~ P-020 暫定）

## 4.3 階段 3：Bucket #1-#4 深入討論 + 拍板

依「潛在設計衝擊由大到小」順序與 user 逐 bucket 討論：

| Bucket | 主議題 | 結果 | 新 D | 新 P |
|---|---|---|---|---|
| #1 客製化輸出 + 多 entity | 揭露三層架構；JSON+MD 雙吐；A-\* 立繪只存 KEY；i18n KEY 機制 | 5 個 D 拍板 | D-021 ~ D-025 | P-021 ~ P-024 |
| #2 高品質台詞 + 評測 | 新增 09_g/h/i；可擴充 QA 機制；/dialogue-write SINGLE_ITER；手稿 trust-level | 3 個 D 拍板 | D-026 ~ D-028 | P-025 ~ P-028 |
| #3 視覺化管理 + HTML | HTML web UI；本地 server；手動 Save；完全分離；5 必要功能 | 2 個 D 拍板 | D-029 ~ D-030 | P-029 部分 |
| #4 A 路徑 + 手稿導入 | 重用既有跳階段機制不新增 skill；markdown 結構要求；entity 命名衝突 4 選項；複製指令按鈕 | 4 個 D 拍板 | D-031 ~ D-034 | P-029 部分 + P-030 |

**累計：** 14 個新 D 拍板 + 10 個新 [SPECIALIST_TBD] P 議題 + 5 個原 P (016-020) RESOLVED

## 4.4 階段 4：產出設計修補清單與需求 lock 文件

5 份文件產出（含本檔）：

| # | 文件 | 變更 |
|---|---|---|
| 1 | `_design/REQUIREMENTS_LOCK.md` v1.0 (新) | 4 bucket 拍板完整需求快照 |
| 2 | `_design/DECISIONS_LOG.md` v0.6 | §6.6 新增 D-021 ~ D-034 + P-021 ~ P-030；P-016 ~ P-020 RESOLVED |
| 3 | `_design/GAP_ANALYSIS.md` v0.2 | §7 新增 Bucket lock 後狀態更新 |
| 4 | `_design/REVISED_WORK_ITEMS.md` v0.2 | §7 新增 v0.2 修訂節（supersede §2 / §3）|
| 5 | `_design/PHASE_3_COMPLETION_REPORT.md` v4.0 (草稿，本檔) | Bucket lock 後完成度報告 |

## 4.5 本輪 master 沒做（依「整合者不是設計者」原則）

- 沒擅動主 SPEC / ARCHITECTURE / TASKS（屬第四輪整合）
- 沒寫具體 schema 細節（屬資料格式 specialist 第二輪）
- 沒設計 QA algorithm（屬上下游 specialist 第二輪）
- 沒設計前端工具 UX（屬 UX specialist 第二輪）
- 沒擅自 promote P-021 ~ P-030 為 D-NNN（等 specialist 第二輪提案）

---

# 5. Specialist 第二輪啟動就緒度（v4.0 新增）

依 `REVISED_WORK_ITEMS.md` v0.2 §7 與 `REQUIREMENTS_LOCK.md` §9.2：

## 5.1 三 specialist 啟動條件全部滿足

| Specialist | 啟動條件 | 滿足狀態 |
|---|---|---|
| 資料格式 | H1/H2/H3 + §3.2 + §3.3 拍板 | ✓ Bucket #1 拍板（D-021 ~ D-025）|
| 上下游 | H1/H2/H3/H5 + §3.2 + §3.3 拍板 | ✓ Bucket #1 + #2 + #4 拍板（D-021 ~ D-033）|
| UX | H4 拍板 | ✓ Bucket #3 拍板（D-029 + D-030）|

**結論：三 specialist 第二輪可立即並行啟動。**

## 5.2 三 specialist 第二輪核心任務（精簡）

詳見 `REVISED_WORK_ITEMS.md` v0.2 §7.3 / §7.4 / §7.5。核心如下：

**資料格式（DF-1 ~ DF-11）：**
- i18n KEY schema + A-\* entity schema
- 可擴充 entity 類型 + qa_type registry 機制
- JSON 中介格式 schema
- mode_tag / qa_type enum 擴展
- phase_log + status + import_source 欄位

**上下游（UD-1 ~ UD-12）：**
- 補 §9 對齊 P-009 ~ P-015
- 文件化「跳階段機制做手稿導入」（不新增 skill）
- 設計 L3 export skill（JSON + MD 雙吐）
- 設計 A-\* 美術資產協議
- 新增 09_g/h/i QA 模板 algorithm
- /dialogue-write SINGLE_ITER 模式
- 評估 00_p 可擴充 QA 協議

**UX（UX-1 ~ UX-17）：**
- §1.4 partial supersede 重寫
- 補完 §2-§6（純 Markdown for L1/L3）
- 對齊 UPSTREAM §7 53 個 [UX] 標記
- **新增 §11 大塊：HTML 前端工具完整 UX 設計**（F1/F2/F3/F6/F7 + 「複製指令」按鈕 + LOCKED 守門 + 編輯衝突偵測 + build/package）

## 5.3 預估工期

| 階段 | 工期 |
|---|---|
| 資料格式第二輪 | 8-12 小時 |
| 上下游第二輪 | 12-18 小時 |
| UX 第二輪 | 15-25 小時 |
| Master 第四輪整合 | 4-6 小時 |
| **總計（並行壓縮後）** | **25-40 小時** |

---

# 6. A.0 暫停狀態的更新（v4.0 修訂）

## 6.1 A.0 狀態（v4.0 FINAL — 解除）

**v4.0 FINAL 狀態：** Phase A.0 **可進入實作**。

**v3.0 / v4.0 草稿時的阻塞已全部解除：**
- ✓ 需求面已 lock（REQUIREMENTS_LOCK v1.0 FINAL）
- ✓ 設計面已整合到主 SPEC v1.1 / ARCHITECTURE v1.2 / TASKS v1.3
- ✓ A.0 parser 設計依賴全 ready：DF v0.2 §11.1 9 大類處理項 + ARCH §12 落地 + TASKS A.0.1~A.0.9 拆解
- ✓ A.4 既有 27 份模板 frontmatter 補完依賴 ready：DF §10.3 已證 frontmatter 零破壞；A-\* 是新增 entity 類型（不動既有檔）

## 6.2 A.0 解除條件（v4.0 FINAL — 全達成）

| # | 條件 | v4.0 草稿 | **v4.0 FINAL** |
|---|---|---|---|
| 1 | 需求面 lock | ✓ Bucket #1-#4 完成 | ✓ 維持 |
| 2 | 三 specialist 第二輪交付 | ✗ 待啟動 | **✓ 三 specialist v0.3 patch 全部交付（DF v0.2 / UD v0.3 / UX v0.3）+ CODEX (c) 收斂** |
| 3 | Master 第四輪整合 — 主 SPEC/ARCHITECTURE/TASKS 已更新 | ✗ 待第四輪 | **✓ SPEC v1.1 / ARCH v1.2 / TASKS v1.3 partial supersede 完成** |
| 4 | INTEGRATION_CONTRACTS 升 v2 | ✗ 待第四輪 | **✓ v2.0 正式版產出（1777 行；A.1~A.8 / B.1~B.8 / C.1~C.5 全具體化）** |
| 5 | P-021 ~ P-030 全部 promote 為 D-NNN 或 supersede | ✗ 待第二輪 + 第四輪 | **✓ P-021~P-026 RESOLVED via D-037~D-046；P-027~P-030 進 INTEGRATION_CONTRACTS §6.4 Pending（成熟期 / 後續細化）** |

**全部達成 → A.0 已解除（v4.0 FINAL）。**

## 6.2a Phase A.0 啟動條件（v4.0 FINAL 新增）

進 Phase A.0 還需要：

| # | 條件 | 狀態 |
|---|---|---|
| 1 | 三 spec v0.3 + 主 SPEC v1.1 + ARCH v1.2 + TASKS v1.3 + INTEGRATION_CONTRACTS v2.0 全標 LOCKED | ⏸ 待階段 7（升 LOCKED + DECISIONS_LOG v1.0） |
| 2 | DECISIONS_LOG 升 v1.0 | ⏸ 待階段 7 |
| 3 | Phase A.0.1 frontmatter parser 任務描述定稿 | ✓ TASKS §A.0.1 v1.1 已寫完整任務描述 |
| 4 | （可選）CODEX (d) 短審查 clean | ⏸ 待階段 6 |

**階段 6（CODEX d 短審）+ 階段 7（升 LOCKED）完成後 → 開 Phase A.0.1。**

## 6.3 Phase 0.5「手稿導入快速路徑」獨立啟動可能性

依 D-031（沿用既有跳階段機制，不新增 skill）+ D-032（手稿格式 markdown structure）+ D-033（entity 命名衝突 4 選項）：

- **Phase 0.5 = 既有跳階段機制 + 文件化 use case + trust-level 參數**
- 不依賴新 skill 開發
- 依賴 i18n KEY schema 與 entity 命名衝突 algorithm（待上下游 specialist UD-2 設計）

**結論：** Phase 0.5 不能比 Phase A.0 更早啟動，因為兩者依賴 specialist 第二輪同一批設計。

---

# 7. 對 master 第四輪整合對話的接手指引（v4.0 新增）

當三 specialist 第二輪全部交付後，重啟一個 master 整合對話：

## 7.1 必讀文件清單（按順序）

1. `_design/REQUIREMENTS_LOCK.md` v1.0 — 需求面真相
2. `_design/DECISIONS_LOG.md` v0.6 — 所有決策歷史
3. `_design/GAP_ANALYSIS.md` v0.2 — 缺口分析
4. `_design/REVISED_WORK_ITEMS.md` v0.2 — 任務拆解
5. 本檔（`PHASE_3_COMPLETION_REPORT.md` v4.0 草稿） — 完成度狀態
6. 三 specialist 第二輪交付：
   - `_design/DATA_FORMAT_SPEC.md` v0.1
   - `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.2
   - `_design/UX_SPEC.md` v0.2
7. `_design/INTEGRATION_CONTRACTS.md` v1（過渡版） — 跨 specialist 介面

## 7.2 第四輪 master 工作清單

1. **盤點三 specialist 第二輪交付**
   - 對照 REVISED_WORK_ITEMS §7.3 / §7.4 / §7.5 任務表，逐項驗收
   - 標記未完成 / 偏離 / 衝突
   - 跨 specialist 衝突由 master 仲裁

2. **promote P-021 ~ P-030 為 D-NNN（或 supersede）**
   - specialist 提案符合 master 暫定 → promote
   - specialist 提案不同 → master 重裁
   - 新編號從 **D-035** 起

3. **升 INTEGRATION_CONTRACTS v1 → v2**
   - 紀錄三條 contract 的真實介面（資料格式 ↔ 上下游 ↔ UX）
   - 不再是「過渡版」

4. **整合到主 SPEC / ARCHITECTURE / TASKS**
   - SPEC §2 補入三層架構
   - SPEC §5.1 增 A-\* + 可擴充 entity 類型機制
   - SPEC §5.2.4 qa_type enum 可擴充化 + mode_tag 增 SINGLE_ITER + qa_type 增 RHYTHM/DRAMATIC_TENSION/CROSS_SCENE_CONTINUITY
   - SPEC §5.2 frontmatter 微擴充（i18n KEY 欄位等）
   - SPEC §5.4 phase_log 增 status + import_source 欄位
   - ARCHITECTURE 增 §5「三層架構」 + 補入 §6.7 UD-2 跳階段手稿導入 use case
   - TASKS 重新編列：Phase 0.5 手稿導入 + 新 09_g/h/i 任務 + 前端工具實作任務群 + A.0 解除 + A.4 補完
   - UX_SPEC §1.4 重寫範圍縮小至 L1/L3

5. **修訂 PHASE_3_COMPLETION_REPORT v4.0 草稿 → v4.0 final**
   - 升 final 條件：上述 1-4 全部完成
   - 升 final 後本檔升 REVIEW；通過 master 終審後升 FINAL

6. **重評可進 A.0**
   - 對照本檔 §6.2 五項條件
   - 全部通過 → 宣告 A.0 可解除

## 7.3 第四輪 master 不做（傳承「整合者不是設計者」原則）

- 不寫 specialist 沒寫的新 spec 內容
- 不擅動 SPEC 已通過 4 輪 CODEX 審查的核心
- 不擅自新增 skill / entity / enum 值
- 不繞過 user 拍板需求（如 user 沒同意動 D-018 剩下 4 項，不擅自動）

---

# 8. 給使用者的下一步指引（v4.0 修訂）

## 8.1 立即（如要繼續推進）

**啟動三 specialist 第二輪：**

- 對每個 specialist 開新對話，使用對應 `_design/SPECIALIST_STARTER_*.md` 啟動包
- 啟動時明示告訴 specialist：
  - 本輪是 **第二輪 refine**
  - 必讀：`REQUIREMENTS_LOCK.md` v1.0 + `DECISIONS_LOG.md` v0.6 §6.6 + `REVISED_WORK_ITEMS.md` v0.2 §7 對應 specialist 任務段
  - 必交付：對應 spec v0.x + §最後段「需 master 裁決問題清單」

- **資料格式 specialist：** 工期 8-12 小時；交付 DATA_FORMAT_SPEC.md v0.1（DF-1 ~ DF-11）
- **UX specialist：** 工期 15-25 小時；交付 UX_SPEC.md v0.2（UX-1 ~ UX-17，含新增 §11 前端工具大塊）
- **上下游 specialist：** 工期 12-18 小時；交付 UPSTREAM_DOWNSTREAM_SPEC.md v0.2（UD-1 ~ UD-12）

三個並行可行。如硬要序順：資料格式先（因 UD-3/4 部分依賴 JSON schema）。

## 8.2 三 specialist 第二輪交付後

重啟一個 master 整合對話（第四輪），執行本檔 §7.2 工作清單。預估工期 4-6 小時。

## 8.3 第四輪整合完成後

- PHASE_3_COMPLETION_REPORT 升 v4.0 final
- A.0 解除（如全條件通過）
- 進 Phase A.0 / Phase 0.5 實作

## 8.4 本輪不做（沿用 v3.0 §8.4）

**主 SPEC / ARCHITECTURE / TASKS 內容變更暫停。** 等第四輪整合再做。

---

# 9. 信心度與保留條款

- 本報告對「A.0 暫停維持」的判定信心度：**高**
- 本報告對「三 specialist 第二輪可立即並行啟動」的判定信心度：**高**
- 本報告對「Bucket #1-#4 拍板已涵蓋核心需求」的判定信心度：**高**（user 已逐 bucket 確認）
- 本報告對「specialist 第二輪 25-40 小時工期估計」的信心度：**中**（依過往時期經驗推估，特別是 UX 第二輪新增 §11 大塊有變動空間）
- 本報告對「第四輪整合 4-6 小時」的信心度：**中—高**（流程清晰，但取決於 specialist 第二輪品質）

**保留條款：**
- 若 specialist 第二輪交付揭露 user 需求新缺口 → 開新 Bucket 討論，本檔升 v4.1
- 若 specialist 第二輪在 P-021 ~ P-030 上提出與 master 暫定不同的方案 → master 第四輪重裁，可能 supersede 部分 D-021 ~ D-034

---

# 10. 後續更新區（保留）

第四輪整合 master 對話後或進一步需求 refresh 時於此區追加更新紀錄。預期升至 v4.0 final（第四輪整合後）或 v5.0 草稿（新需求 refresh 後）。

## 10.1 v4.0 草稿 → v4.0 FINAL 升版紀錄（2026-05-19，master 第四輪整合對話）

**升版觸發：** specialist 第二輪 + v0.3 patch + CODEX (c) 17 衝突收斂 + master 第四輪整合對話完成。

**v4.0 FINAL 整合產出：**

| # | 產出 | 行數 / 狀態 |
|---|---|---|
| 1 | `_design/INTEGRATION_CONTRACTS.md` v2.0 | 1777 行（Contract A.1~A.8 / B.1~B.8 / C.1~C.5 全具體化 + Pending 整理 + 維護紀律） |
| 2 | `_design/SPEC.md` v1.1 | partial supersede via D-024~D-046（§5.1 / §5.1a / §5.1b / §5.2.3 / §5.2.4 / §5.4 / §5.4a / §12.7 / §13a / §14a / §16a）|
| 3 | `_design/ARCHITECTURE.md` v1.2 | partial supersede（§1.2 / §4.2a / §6.3 / §12 A.0 Parser 9 大類 / §13 Frontend Adapter 8 endpoint） |
| 4 | `_design/TASKS.md` v1.3 | partial supersede（A.0 → 9 大類 / A.0F → 11 個前端工具 task / A.5 / C.5 / C.5a / D.1a / D.4）|
| 5 | `_design/PHASE_3_COMPLETION_REPORT.md` v4.0 FINAL（本檔） | §3 完成判定全 ✓ / §6.2 A.0 解除條件全達成 |

**整合過程的 north-star 對齊原則：**

依 user 第四輪整合對話拍板：partial supersede 衝突點由 master 自選對齊方案 + 寫理由標註。對齊優先序：
- REQUIREMENTS_LOCK v1.0（north star）
- D-037~D-046（master 第四輪 P0/P1 拍板）
- D-001~D-036（既有拍板）
- specialist v0.3 一致性

整合過程**無**發現新 D-NNN 牴觸需求，所有 partial supersede 順利落地。

**未完成 / 後續工作：**

| # | 項目 | 接續 phase |
|---|---|---|
| 1 | CODEX (d) 短審查（擴大到 ARCH + TASKS 一致性）| 階段 6 — 本對話內或下對話 |
| 2 | 升 LOCKED（三 spec v0.3 + 主 SPEC v1.1 + INTEGRATION_CONTRACTS v2.0 + ARCH v1.2 + TASKS v1.3）| 階段 7 |
| 3 | DECISIONS_LOG 升 v1.0（不再加新 D-NNN，新議題另寫）| 階段 7 |
| 4 | Phase A.0.1 frontmatter parser 任務描述定稿 | 階段 7（TASKS §A.0.1 v1.1 已寫完整任務描述，可直接啟動）|
| 5 | git commit 第四輪整合產出 | user 手動（sandbox virtiofs cache 不穩，本對話跳過 sandbox commit）|

**進 Phase A.0 條件總覽：**

- ✓ §6.2 五項 A.0 解除條件全達成（v4.0 FINAL）
- ⏸ §6.2a 啟動條件 4 項（待階段 6 + 7）

**信心度（v4.0 FINAL）：**
- 對「Phase 3 完整收斂」判定信心度：**高**
- 對「partial supersede 無新衝突」信心度：**中—高**（CODEX (d) 短審後升「高」）
- 對「Phase A.0 啟動條件 ready」信心度：**高**（TASKS A.0.1 任務描述已完整定稿）

---

# 11. 附錄

## 11.1 編號變更歷史

| 時間軸 | D 編號 | P 編號 |
|---|---|---|
| v0.2（時期 C 第一次）| D-007 ~ D-010 | P-004 ~ P-007 |
| v0.3（UPSTREAM 重盤點後）| + D-011 ~ D-017 | + P-008 |
| v0.4（初代 master 補充裁決後）| + D-018（supersedes D-001a/D-007/D-016）；D-011 ~ D-017 → P-009 ~ P-015 | — |
| v0.5（新 master 接手）| + D-019 ~ D-020 | + P-016 ~ P-020；P-006/007/008 RESOLVED |
| **v0.6（Bucket #1-#4 拍板）** | **+ D-021 ~ D-034** | **+ P-021 ~ P-030；P-016 ~ P-020 RESOLVED** |
| v0.7 ~ v0.8（specialist 第二輪 + CODEX (c) + master 第四輪 P0/P1 拍板） | + D-035 ~ D-046 | P-021 ~ P-026 RESOLVED；P-027~P-030 進 Pending（後續細化）|
| **v1.0（升 LOCKED — 階段 7 觸發）** | 不再加 D-NNN；新議題另寫 | — |

## 11.2 Bucket 拍板的 partial supersede 清單對照

| 既有設計 | 衝擊類型 | D-NNN | 詳見 REQUIREMENTS_LOCK §7 第 N 項 |
|---|---|---|---|
| SPEC §5.1 邏輯實體 7 種 | partial supersede — 增 A-\* | D-023 / D-025 | 1 |
| SPEC §5.2.4 qa_type LOCKED | partial supersede — 變可擴充 | D-027 | 2 |
| SPEC §5.2.4 mode_tag LOCKED | partial supersede — 增 SINGLE_ITER | D-028 | 3 |
| D-003 / D-018 #6 特殊資料格式 | partial supersede — 本輪設計縮減版 | D-024 | 4, 7 |
| D-018 #2 多語不採 | partial supersede — 加 KEY 機制 | D-022 | 5 |
| D-018 #3 continuity_check 不採 | partial supersede — 加跨場 QA | D-026 | 6 |
| P-010 不新增 /iterate-dialogue | partial supersede — 改加 --single-iter | D-028 | 8 |
| UX_SPEC §1.4 HTML 廢棄 | partial supersede — L2 採 HTML | D-029 / D-030 | 9 |

---

# 12. 文件維護紀律

- 本檔由 master 對話維護；v4.0 草稿 → v4.0 final 升版條件 = §7.2 全部完成
- 任何後續變更必須對應 §11.1 編號變更歷史補一行
- 本檔不是 SPEC — 不影響主 SPEC/ARCHITECTURE/TASKS 的權威性
- 本檔 v4.0 草稿與 v3.0 過渡版的關係：v3.0 過渡版的「結論」已被 v4.0 草稿全面 supersede；v3.0 內容保留於 git 歷史
