狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-18  
適用範圍：既有 Narrative Workspace Prototype Round 2.1 的拆解分析 / 給 UX specialist 第二輪的明確設計起點  
優先級：最高（UX specialist 第二輪 §11 設計輸入）  

# UX_PROTOTYPE_ANALYSIS — 既有 HTML Prototype 拆解與重用判定

# 0. 文件性質與閱讀對象

本檔由 master 對話分析既有 Narrative Workspace Prototype Round 2.1（位於 `_design/refactor_reference/`）後產出。

**輸入：**
- `_design/refactor_reference/UI_UX_SPEC.md`（631 行，13 節結構化規格）
- `_design/refactor_reference/narrative_workspace_prototype_v2.1.html`（2297 行 single-file HTML）

**目的：** 把 prototype 拆解為可重用的 UX 資產，作為 UX specialist 第二輪 §11「HTML 前端工具完整 UX 設計」的具體設計起點，避免從零畫。

**閱讀對象：**
- UX specialist 第二輪（核心對象 — 本檔是你 §11 的 starting point）
- master 對話（保留作為決策依據）
- user（確認方向 + 後續對齊）

**搭配文件：**
- `REQUIREMENTS_LOCK.md` v1.0 — 4 bucket 需求快照（最高權威）
- `DECISIONS_LOG.md` v0.6 — Bucket #1-#4 拍板紀錄 + 本檔產出的 D-035 新增
- `REVISED_WORK_ITEMS.md` v0.2 §7.5 — UX specialist 第二輪 17 條任務
- `refactor_reference/UI_UX_SPEC.md` — Prototype 自身的完整規格（細節層權威）

---

# 1. Prototype 速覽（簡化版）

完整速覽見 `refactor_reference/UI_UX_SPEC.md §1`。本節只列對我們重要的：

## 1.1 演進歷程（Round 1 → 2.1）

- Round 1：建立第一層入口 + Project Dashboard
- Round 1.1：Light/Dark mode + CSS token 重構
- Round 2：**重排成 production cockpit 模式** + Scene Queue + Scene Detail + 三種 modal
- Round 2.1：UI label 中文化（中文主 + 英文 sub）

## 1.2 7 個畫面 + 4 個橫切功能

**畫面：**
1. Workspace Home（含 empty state）
2. Project Dashboard（production cockpit 模式）
3. Scene Queue（filter + chapter grouping）
4. Scene Detail（main + side cockpit）
5. QA / HD / Canon Delta 三種 modal
6. 公版 Harness preview
7. 場景索引快速覽（legacy）

**橫切：**
- Hash routing（6 個 route）
- Light/Dark mode toggle（含 localStorage）
- Glossary tooltip popover（13 術語）
- Mock 互動分層（路由真做 / modal 真做 / 元件 alert）

## 1.3 純技術特性

- 單檔 self-contained HTML + CSS + JS
- 無建置 / 無外部依賴 / 無 framework
- 完整 dark mode token 化

---

# 2. 對齊 Bucket #3 5 必要功能

| Bucket #3 必要功能 | Prototype 對應畫面 | 對齊度 | 處理策略 |
|---|---|---|---|
| **F1 全局看板** | Project Dashboard | 🟢 **核心對齊** | 直接平移；refine HERO 區順序 + 含 A 路徑「複製指令」按鈕（D-034） |
| **F2 場景切換 + 自動 context 裝載** | Scene Queue → Scene Detail (main + side) | 🟢 **高度對齊** | 直接平移；Scene Detail 的 Required Context 6 子分區是寶 |
| **F3 多版本並排對比** | ❌ Prototype 沒做 | 🔴 **缺口** | 由 UX specialist §11.3 設計；放在新 Scene Editor 頁（依 D-035） |
| **F6 快速搜尋 + 篩選** | Scene Queue filter + chapter grouping | 🟢 **核心對齊** | 直接平移；補 facet（按 qa_type / pipeline_state） |
| **F7 直接編輯 + LOCKED 守門** | ❌ Prototype 是 read-only preview | 🔴 **設計衝突已解 — D-035 採雙頁架構** | 新增 Scene Editor 頁；read-only preview 維持在 Scene Detail |

---

# 3. §12 Critical Preserve 對齊與衝突解決紀錄

UI_UX_SPEC.md §12 列出 10 條 critical preserve。對照 Bucket 拍板：

| §12 critical | 我們的對齊 | 狀態 |
|---|---|---|
| 1. 下一步永遠在最前 | 完全對齊（F1 既有規範） | ✓ 保留 |
| 2. Next Actions / Blockers 並列 HERO | 對齊 | ✓ 保留 |
| 3. Scene Readiness 三層（badge + checklist + next fix） | 對齊 G1 | ✓ 保留 |
| **4. Scene Detail = cockpit，不是 editor** | **D-035 解決：分雙頁** | ✓ 保留（cockpit 維持 read-only） |
| 5. Required Context 6 子分區 | 跟「自動 context 裝載」相容 | ✓ 保留 |
| 6. G1 / G2 / G3 三守則 | 已採用（Bucket #2 / #3 引用） | ✓ 保留 |
| **7. Dialogue Draft Preview 是 read-only** | **D-035 解決：Editor 是另一頁** | ✓ 保留（cockpit 內的 preview 維持 read-only） |
| 8. QA / HD / Canon Delta 用中央 modal | 對齊「審視中的事件」哲學 | ✓ 保留 |
| 9. Modal 內 action 標 mock | 對齊 git workflow + agent 觸發精神 | ✓ 保留 |
| 10. 中文主 + 英文 sub | 對齊 UX §0 + Bucket 全文約束 | ✓ 保留 |

**核心衝突已解決：** D-035（見 §5）採「Cockpit + 獨立 Editor 雙頁面」架構，**完整保留 prototype 的 cockpit-first 哲學**，同時不犧牲 Bucket #3 F7「直接編輯」需求。

---

# 4. 三類分類：可平移 / 需調整 / 拒絕

## 4.1 🟢 可直接平移（UX specialist 不必重新設計）

| 項目 | 來源 | 我們用 |
|---|---|---|
| Workspace Home 多專案選擇器 | Prototype §1.2 #1 | **保留**（未來考慮多專案；現在作為 project picker entry） |
| Project Dashboard 整體 layout 7 段順序 | Prototype Round 2 重排後 | 直接用（HERO / 場景就緒度 / 模組狀態 / 三欄區） |
| Scene Queue 結構（filter + chapter grouping） | Prototype Round 2 主入口 | 直接用 + 補 facet 維度 |
| Scene Detail main + side cockpit 雙欄 | Prototype Round 2 production cockpit | 直接用，保持 read-only 性質 |
| Required Context 6 子分區（Bible refs / characters / relationships / world vocab / info reveal / warnings） | Prototype Scene Detail 設計 | 直接用，跟 Bucket #1/#2 立繪 + i18n KEY 對齊 |
| QA / HD / Canon Delta 中央 modal | Prototype 三種 modal | 直接用，對齊「事件審視」精神 |
| 公版 Harness / 模板管理 preview | Prototype §1.2 #6 | **保留**（user 確認；服務 Template/Instance 架構） |
| Glossary tooltip 13 術語 | Prototype 橫切功能 | **保留**（user 確認）|
| Light / Dark mode toggle + 雙主題 token | Prototype §1.2 / §5 | **保留**（user 確認，雙主題） |
| 三條守則 G1 / G2 / G3 | Prototype §8 | 全採用（已在 Bucket #2 / #3 引用） |
| 中文主 + 英文 sub 命名 | Prototype §9.1 | 全採用（UX §0 已定） |
| 錯誤訊息四件套（What / Where / Why / How to fix） | Prototype §9.2 | 全採用（UX §8 已定） |
| Next Fix 用具體祈使句 | Prototype §9.2 | 全採用 |

## 4.2 🟡 需調整後平移（UX specialist 在 §11 重新設計）

| 項目 | 為何要調整 | 調整方向 |
|---|---|---|
| Project Dashboard 第一個 section | 加 A 路徑「複製指令」按鈕（D-034） | HERO「下一步建議」內含「跑 /create-world」這類，旁邊加「複製指令到剪貼簿」按鈕 |
| Scene Detail 的 Dialogue Draft Preview | F3 多版本對比需要 v01A/B/C 並排 | 在 Scene Detail 維持單一 read-only preview；F3 並排對比放在新 Scene Editor 頁（D-035） |
| QA finding modal 中的 Suggested actions | Prototype 列舉作為 button mock；我們不做 button | 改成「閱讀建議純列舉文字」，跟 UX §8 對齊 |
| Hash routing | Prototype 在單檔內路由；本地 web server 可用真路由 | UX specialist 評估：保留 hash 路由 vs 用 HTML5 history API；給 trade-off |
| state 管理 | Prototype `window.MOCK` + hash | 改成從 markdown source 動態讀（user 確認後 commit 真資料） |
| Scene Detail @920px 之外的 RWD | Prototype 沒做完整 RWD | 個人桌面使用 — 保留現有 @920px 切換；超窄視窗 hint「請開啟桌面瀏覽」即可 |

## 4.3 🔴 拒絕 / 不適用我們場景

| Prototype 元素 | 拒絕理由 |
|---|---|
| Mock action alert / disabled button + tooltip 「等之後啟用」混用 | 我們前端跟 agent 完全分離（D-029 (α)）；所有真實 action 走 agent 對話；前端用「複製指令」按鈕引導 user 切外部 chat |
| Mock fidelity 三層混用（路由真做 / modal 真做 / 元件 alert） | 我們的 fidelity 規則：read-only 顯示走真資料；寫操作（save / commit）走前端 button → 本地 server API 真寫 |
| 「等之後啟用」性質的 lock / rewrite / reorder disabled button | 我們是 LOCKED 守門 — 顯示警示而不是 disabled；user 可選擇降級（走 agent） |
| 完整 a11y / i18n / RWD / 列印樣式 | 個人桌面工具，不必（user 確認） |
| 完整測試框架 | 個人專案，不必（user 確認） |
| TypeScript / 嚴格型別 | 個人專案，看 UX specialist 評估；JSDoc 可能就足夠 |

---

# 5. D-035 新拍板：Cockpit + 獨立 Editor 雙頁面架構

## 5.1 拍板內容（user 已確認）

兩個獨立頁面：

```
┌────────────────────────────────────────────────────────────┐
│ Scene Detail (cockpit) — 維持 prototype 設計               │
│ ────────────────────────────────────                       │
│ 主欄：                                                       │
│  - Scene Readiness Panel（badge + checklist + next fix）   │
│  - Required Context 6 子分區                                │
│  - **Dialogue Draft Preview（read-only）**                 │
│  - Beat / Outline Preview                                   │
│  - QA Findings 摘要 → 點開 modal                            │
│ 側欄：                                                       │
│  - Active QA / HD / Canon Delta                            │
│  - Quick Actions（含「進入編輯」按鈕 → 跳轉到 Scene Editor）│
│  - LOCKED 標示（如此場已 LOCKED 則「進入編輯」改成「降級至 DEPRECATED 才能改」）│
└────────────────────────────────────────────────────────────┘
                           ↓ 點「進入編輯」
┌────────────────────────────────────────────────────────────┐
│ Scene Editor (新增頁面 — Bucket #3 F3 + F7 在這裡)         │
│ ────────────────────────────────────                       │
│ 上方：場景標題 + 返回 Scene Detail + 「Save」按鈕            │
│ 中央三欄並排（F3）：v01A / v01B / v01C                      │
│  - 每欄是可編輯 textarea（F7）                              │
│  - 點某段台詞顯示 i18n KEY + 立繪 KEY metadata              │
│  - LOCKED 段以 disabled 灰底 + 「需降級才能改」警示          │
│ 底部：QA 狀態列 + 「跑 QA」按鈕（複製指令到剪貼簿）           │
└────────────────────────────────────────────────────────────┘
```

## 5.2 為什麼選 (X) 雙頁面

| 維度 | 雙頁面優勢 |
|---|---|
| 保留 prototype 設計遺產 | §12 #4 / #7「cockpit-first 哲學」完整保留 |
| 視覺空間 | F3 多版本並排對比需要橫向空間，獨立 Editor 頁可給滿 |
| LOCKED 守門 UX | 在「進入 Editor」入口擋比 inline 警示更清晰 |
| 操作分離 | 「審視」跟「編輯」是不同心智狀態，分頁讓 user 進入正確模式 |
| 跟 Bucket #1 D-029 (c) 手動 Save 對齊 | Editor 有清楚的「Save」按鈕，跟「自動 save」區別清楚 |

## 5.3 雙頁面間的導航

```
Workspace Home → Project Dashboard → Scene Queue → Scene Detail (cockpit, F1+F2)
                                                       ↓ 點「進入編輯」
                                                   Scene Editor (F3+F7)
                                                       ↓ Save 後
                                                   返回 Scene Detail 或 Scene Queue
```

- 從 Scene Detail 進 Editor：one click
- Editor 內無 deep navigation（避免迷路）
- Save 後 prompt user 選擇返回 cockpit 或回 Queue

## 5.4 對應的 UX specialist 子任務

REVISED_WORK_ITEMS §7.5 的 UX-12 任務原本是 F7 直接編輯 + LOCKED 守門 — 現在拆成：
- **UX-12a：Scene Editor 頁面整體 layout**（F3 三欄並排 + F7 編輯 + LOCKED 守門）
- **UX-12b：Scene Detail → Scene Editor 導航流**

---

# 6. 保留元件清單（user 確認的四項）

依 user 拍板 Q2 答案，下列 prototype 元件**保留適用到我們 single-project repo 場景**：

| 元件 | user 拍板 | 用法 |
|---|---|---|
| **Workspace Home 多專案選擇器** | ✓ 保留 | 服務「未來多專案」可能性；現在當 project picker entry；single-project 時 single entry |
| **公版 Harness / 模板管理 preview** | ✓ 保留 | 服務 SPEC §7 Template/Instance 架構；UI 上提供 Template 升級與 Instance bootstrap 入口 |
| **Glossary tooltip 13 術語** | ✓ 保留 | 個人長期記憶輔助 — 看到 W-rules / mode_tag 等 enum 可悬停看解釋 |
| **Light / Dark mode toggle + 雙主題** | ✓ 保留 | 跨日夜使用 |

→ UX specialist §11 的設計範圍包含這四項元件的 layout / 互動細節對齊。

---

# 7. §10 已知問題的處理計畫

對應 prototype §10 列出的「已知但未解決」問題，我們的處理：

## 7.1 §10.1 工程結構面

| 問題 | 處理 |
|---|---|
| 單檔過大 | ✓ 重構時拆 component（UX specialist 提實作建議；framework 由 user 之後另議） |
| 無建置流程 | △ 視需求加 Vite / 等；保留瀏覽器直開可能性 |
| 無型別保護 | △ JSDoc 就夠，不必上 TypeScript（個人專案）|
| 無測試 | ✗ 個人專案，不必 |
| State 散落 | ✓ 重構時引入輕量 state（如 signal/observable） — UX specialist 提建議 |

## 7.2 §10.2 設計面

| 問題 | 處理 |
|---|---|
| Mock 互動 fidelity 不一致 | ✓ 統一規則：read-only 走真資料；寫操作走前端 API → markdown source；agent action 用「複製指令」按鈕引導 |
| 沒有 loading 狀態 | ✓ 加 loading skeleton |
| 沒有錯誤邊界 | ✓ 加 error boundary / fallback view |
| 沒有 i18n | ✗ 中文主 + 英文 sub 已是設計約束；不抽 i18n table |
| 沒有 a11y 完整支援 | ✗ 個人工具，不必 |
| 沒有 RWD | △ 個人桌面用；保留 @920px 切換 |
| 沒有列印樣式 | ✗ 不必 |

## 7.3 §10.3 IA / UX review queue

全部交給 UX specialist §11 評估：

| review queue 項 | 暫定方向 |
|---|---|
| Project Dashboard 上半資訊過載 | UX specialist 重新評估折疊 / 重排 |
| HD blocking vs non-blocking 用 danger / warning badge 反邏輯 | UX specialist 重新對齊 |
| Scene Detail 主欄資訊密度高 / 側欄是否 sticky | UX specialist 評估，傾向 sticky 側欄 |
| Beat 內 lock / rewrite / reorder disabled button 誤判 | 我們不做 disabled — 改成「降級至 DEPRECATED 才能改」明示路徑 |
| Future module 灰階是否清楚（dark mode） | UX specialist 在 dark mode 下重測 |
| Modal centered overlay vs side sheet | UX specialist 提建議，傾向保留 centered（一致性） |

## 7.4 §10.4 資料結構警告區

**重要：** prototype 的 `mock_data` 結構**不是 schema 提案**。資料層完全交給資料格式 specialist 第二輪設計。UX specialist 不要照搬 mock_data shape。

特別三件事：
1. UI 與資料解耦（mock_data shape ≠ 真 schema）
2. 守 G1 / G2 / G3
3. QA finding 的 `affected.beatId` / `affected.lineId` 是 prototype 為顯示編的，真 schema 待資料格式 specialist 拍板（可能對應 i18n KEY 機制）

---

# 8. 採用 §11 Level 2 重構

依 prototype §11 列出的四個重構 Level：

**選 Level 2（UX 局部修正）+ 帶 Level 3 思維。**

| Level 範圍 | 我們做嗎 |
|---|---|
| Level 1 純 UI tech-stack 升級 | ✓ 必做（拆 component / build tool / state mgmt） |
| **Level 2 UX 局部修正** | ✓ **核心 scope** — 處理 §10.3 review queue + 補 F3 + F7 雙頁架構 |
| Level 3 接真資料層 | △ 部分 — 接 markdown source；mock schema 不照搬 |
| Level 4 產品化 | ✗ 不做（個人工具） |

---

# 9. UX Specialist 第二輪明確 Starting Points

UX specialist §11 設計時的具體起點，依本檔結論：

## 9.1 §11.1 F1 全局看板（Project Dashboard）

- 起點：prototype Project Dashboard 7 段順序（HERO 下一步建議 / HERO 卡點 / 場景就緒度 / 模組狀態 / 三欄區 / 模組導航）
- 改進：HERO 下一步建議旁加 A 路徑「複製指令」按鈕（D-034）
- 細節 review：依 §10.3 處理「上半資訊過載」議題

## 9.2 §11.2 F2 場景切換 + 自動 context 裝載

- 起點：prototype Scene Queue + Scene Detail (main + side) 雙層導航
- 保留：Required Context 6 子分區（Bible refs / characters / relationships / world vocab / info reveal / warnings）
- 對齊：A-\* 立繪 KEY metadata 顯示在 Required Context

## 9.3 §11.3 F3 多版本並排對比（**新設計**）

- 起點：**Prototype 沒有** — UX specialist 從零設計
- 位置：新 Scene Editor 頁（D-035 拍板）
- 中央三欄 v01A / v01B / v01C 並排
- 每欄是可編輯 textarea（連 F7）
- 點某段台詞顯示 i18n KEY + 立繪 KEY metadata
- 對齊：dialogue-write 三模式 algorithm（UPSTREAM §4）的多版本概念

## 9.4 §11.4 F6 搜尋 + 篩選

- 起點：prototype Scene Queue filter + chapter grouping
- 補：facet 維度按 qa_type / pipeline_state / 狀態 / 等
- 對齊：可擴充 qa_type enum（D-027）

## 9.5 §11.5 F7 直接編輯 + LOCKED 守門（**部分新設計**）

- 起點：prototype 有 read-only Dialogue Draft Preview，**沒有編輯介面**
- 拆兩塊：
  - **UX-12a Scene Editor 頁面 layout**（D-035 拍板）— 三欄編輯 + 手動 Save 按鈕
  - **UX-12b Scene Detail → Editor 導航流**（LOCKED 守門在「進入編輯」入口擋）
- LOCKED 守門 UX：在 cockpit 「進入編輯」按鈕變成「降級至 DEPRECATED 才能改」+ explanation

## 9.6 §11.6 跟 agent 完全分離

- 起點：prototype 的「Mock action alert + disabled button + tooltip」三層混用 — 我們不採用
- 我們的規則：
  - read-only 顯示 → 直接從 markdown source 讀
  - 寫操作（save dialogue / commit）→ 前端 button → 本地 server API → 寫 markdown
  - Agent action（跑 `/dialogue-write` / `/qa` 等）→ 「複製指令到剪貼簿」按鈕 → user 切外部 chat
- 雙視窗工作流明示

## 9.7 §11.7 多場景並行 + 編輯衝突偵測

- 起點：prototype 沒做（單一場景視角）
- 我們：可能 tab / 多瀏覽器分頁；衝突偵測在 Save 時用 checksum 比對 markdown source mtime

## 9.8 §11.8 前端 build / package / 分發

- 起點：prototype 是 single-file HTML 瀏覽器直開
- 我們：本地 web server（python `http.server` 或 FastAPI）+ 瀏覽器 localhost
- UX specialist 提實際 build script 範本

---

# 10. 給 UX Specialist 第二輪的明確 Deliverables

UX specialist 第二輪 §11 必須交付（含本檔分析輸入）：

| 子節 | Deliverable | 起點 |
|---|---|---|
| §11.1 | Project Dashboard 完整 layout + 元件清單 + 互動 spec | prototype Project Dashboard 7 段順序 + 本檔 §9.1 改進 |
| §11.2 | Scene Detail (cockpit) 完整 layout | prototype Scene Detail (main + side) + Required Context 6 子分區 |
| §11.3 | **Scene Editor 三欄並排對比 layout（新）** | 本檔 §5.1 草圖 + UX specialist 細化 |
| §11.4 | Scene Queue + 搜尋 / 篩選 UI | prototype Scene Queue + 本檔 §9.4 facet 擴充 |
| §11.5 | LOCKED 守門呈現 + Scene Detail→Editor 導航 | 本檔 §9.5 + UX specialist 細化 |
| §11.6 | 「複製指令」按鈕呈現 + 雙視窗工作流 hint | D-034 + 本檔 §9.6 |
| §11.7 | 多場景並行 + 編輯衝突偵測 UX | 從零設計 |
| §11.8 | Build / package / 啟動規格 | python http.server 範本 + 啟動文檔 |
| 額外 | Workspace Home / 公版 Harness / Glossary tooltip / Theme toggle 對齊新需求 | prototype 保留四項 |

---

# 11. 待 specialist 細化的清單

下列項目本檔不細化，留給 UX specialist：

- 三主題 token 系統的具體 CSS 變數對應（prototype §5）— specialist 評估保留 / 簡化 / 重組
- 各 modal 內互動細節（QA finding 點開後動作流 / HD 拍板流 / Canon Delta 套用流）
- 鍵盤快捷鍵（prototype 沒有 — specialist 可選擇加）
- 動畫 / transition timing
- 字體 / 字級系統具體值
- breadcrumb 在多頁面導航的具體格式（含進入 Scene Editor 的 breadcrumb）

---

# 12. 文件維護紀律

- 本檔是「prototype 拆解結論」的快照，**不是新需求文件**
- 拍板項目（D-035 + user Q2 四保留項）已記入 DECISIONS_LOG §6.6（v0.7 / 待 master 第四輪整合時 promote）
- UX specialist 第二輪以本檔 §9 / §10 為設計起點
- 後續若 specialist 提案推翻本檔某條結論 → 由 master 第四輪整合裁決
- 本檔升 REVIEW 條件：UX specialist 交付 UX_SPEC v0.2 §11 對齊本檔
- 本檔升 FINAL 條件：master 第四輪整合完成

---

# 13. 引用文件清單

- `_design/refactor_reference/UI_UX_SPEC.md`（prototype 自身規格，本檔的細節層權威）
- `_design/refactor_reference/narrative_workspace_prototype_v2.1.html`（prototype 實作）
- `REQUIREMENTS_LOCK.md` v1.0
- `DECISIONS_LOG.md` v0.6 §6.6（含本檔新增 D-035）
- `REVISED_WORK_ITEMS.md` v0.2 §7.5（UX specialist 17 條任務）
- `UX_SPEC.md` v0.1（第一輪 ≈40% 交付）
- `UX_PRIOR_DRAFT.md` v0.1（earlier UX 對話整理稿）
