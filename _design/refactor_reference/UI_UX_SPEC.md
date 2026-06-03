狀態：DRAFT
版本：v1.0（從 prototype Round 2.1 整理）
最後更新：2026-05-18
適用範圍：給「新重構專案」對話的 UI/UX 完整規格參考
優先級：高（為新對話的主要設計輸入）

# Narrative Workspace — UI/UX 規格

> 配對的 single-file HTML 參考：`narrative_workspace_prototype_v2.1.html`（同資料夾）
> 直接用瀏覽器開那份 HTML 可實際操作所有畫面與互動。

---

## 0. 文件目的與閱讀方式

這份文件是 **Narrative Workspace UI prototype Round 2.1** 的完整 UI/UX 規格整理。給新重構專案的對話直接使用。

**這份文件回答：**

- prototype 已經做了什麼（畫面 / 互動 / 設計決策）
- 為什麼這樣設計（rationale）
- 重構時應保留什麼（critical design intent）
- 重構時應改善什麼（已知問題與候選方向）
- mock 邊界在哪（哪些是真做、哪些是假裝）

**這份文件不回答：**

- 重構後該用什麼框架（React / Vue / Svelte / vanilla 等都由新專案自決）
- 真實後端 / API / 資料層怎麼接（prototype 是 UI-only / mock-only）
- 業務邏輯細節（請參考 prototype 自身的 prototype_notes.md 與 Product Requirements Candidate Register v0.1）

**如何配合 single-file HTML 使用：**

- 邊讀本檔邊在瀏覽器開 `narrative_workspace_prototype_v2.1.html`
- 每節提到的畫面 / 元件都可在 HTML 中實際看到
- 路由可直接在網址 hash 切換（如 `#/project/wuxia-ensemble/scene/ch02-s04`）

---

## 1. Prototype 速覽

### 1.1 演進史

| Round | 主要產出 | 為什麼 |
|---|---|---|
| Round 1 | Workspace Home、Project Dashboard、模組導航、場景索引快速覽、公版 Harness preview、empty state | 建立第一層入口架構與專案內導航心智 |
| Round 1.1 | light / dark mode toggle、CSS token 系統重構 | UX 偏好 |
| Round 2 | Project Dashboard 重排、Scene Queue（新主入口）、Scene Detail（main + side cockpit）、QA / HD / Canon Delta 中央 Modal | 從「模組首頁」轉成「production cockpit」 |
| Round 2.1 | UI label 中文化（中文主 + 英文 sub） | 統一語言風格 |

### 1.2 範圍

**有實作的畫面（7 個）：**

1. Workspace Home（含 empty state）
2. Project Dashboard（重排後的 production cockpit 模式）
3. Scene Queue（場景列隊，filter + chapter grouping）
4. Scene Detail（單場控制台，main + side 兩欄）
5. QA Finding / Human Decision / Canon Delta 三種 modal
6. 公版 Harness / 模板管理 preview
7. 場景索引快速覽（Round 1 legacy 表格，保留供對比）

**有完整實作的橫切功能：**

- Hash routing（支援 6 個 route）
- Light / Dark mode toggle（含 localStorage 持久化 + first-paint flash 防護）
- Glossary tooltip popover（13 個術語）
- Mock 互動分層（路由級真做 / modal 真做 / 元件級 alert）

### 1.3 關鍵特性

- **單檔 self-contained**：原本拆 4 檔，single-file 版整合成一個 HTML
- **無建置流程**：純原生 HTML + CSS + JS，瀏覽器直開
- **無外部依賴**：沒有 React / Vue / 任何 framework / npm package
- **零真實後端**：所有資料來自 `window.MOCK`，所有「動作」全 mock
- **完整響應主題切換**：每個 component 都正確套用 dark mode token

---

## 2. 整體架構

### 2.1 檔案結構（原版 4 檔）

```
_prototypes/ux/narrative_workspace/
├── index.html           ← UI 主檔（inline CSS / JS）
├── mock_data.js         ← window.MOCK 全頁共用 mock data
├── README.md            ← 使用說明
└── prototype_notes.md   ← 設計筆記 / UX 驗證 / review queue
```

Single-file 版把 mock_data.js inline 進 index.html，方便新對話 reference。

### 2.2 JS 結構（模組化分區）

主 script 用 IIFE wrap，內部以 section comment 分 13 大區塊：

```
0.  Helpers（$, $$, escapeHtml, gloss, mockAction）
1.  Hash router（parse / go / onChange）
2.  Glossary popover
3.  Modal infrastructure
4.  Theme toggle
5.  Empty state toggle
6.  Header / breadcrumb 渲染
7.  View: Workspace Home
8.  View: Project Dashboard
9.  View: Scene Queue
10. View: Scene Detail
11. View: Scene Dialogue (legacy)
12. View: 公版 Harness preview
13. Action handlers + Modal openers
14. Render dispatcher
```

### 2.3 CSS 結構

- `:root` 與 `[data-theme="dark"]` 兩組 CSS variable（約 36 個 token）
- Component 區塊用 `/* ===== xxx ===== */` 分區註解
- 全部 component 透過 var() 引用 token，無硬編色（除少數刻意保留：白底 button text、glossary popover 永遠深色等）

---

## 3. 路由與資訊架構

### 3.1 路由表

| Hash | 畫面 |
|---|---|
| `#/home`（預設） | Workspace Home |
| `#/home?empty=1` | Workspace Home empty state |
| `#/project/<id>` | Project Dashboard |
| `#/project/<id>/scene-queue` | Scene Queue |
| `#/project/<id>/scene-queue?filter=<KEY>` | filtered Scene Queue |
| `#/project/<id>/scene/<sid>` | Scene Detail |
| `#/project/<id>/scene-dialogue` | 場景索引快速覽（legacy） |
| `#/templates` | 公版 Harness / 模板管理 preview |

合法 readiness filter KEY：`READY` / `READY_WITH_RISK` / `BLOCKED` / `AWAITING_DECISION` / `AWAITING_DATA` / `DRAFT_PENDING_QA` / `QA_NEEDS_REWRITE`

### 3.2 三層導航結構

```
Workspace（跨專案）
  ├── Workspace Home（project 摘要 + 工具層入口）
  └── Templates preview（公版 Harness，所有 project 共用）

Project（單一專案）
  └── Project Dashboard
        ├── Scene Queue（場景列隊）
        │     └── Scene Detail（單場控制台）
        │           └── QA / HD / Canon Delta Modal（中央 overlay）
        └── Scene Dialogue（legacy 快速覽）
```

### 3.3 Project Dashboard 區塊閱讀順序（Round 2 重排，**設計重點**）

```
1. Project Identity（PD-Header + 4 個 summary metric）
2. HERO：下一步建議 / Next Actions ← 最優先
3. HERO：卡點 · 風險 / Blockers · Risks（與 ↑ 並列）
4. 場景就緒度總覽 / Scene Readiness Summary（7 個 chip + 計數）
5. 模組狀態總覽 / Module Status Overview（6 個 phase block）
6. Triplet（Human Decision 待裁決 / Canon Delta 候選 / Agent 必讀）
7. 模組導航 / Module Navigation（視覺權重降低，dashed border）
```

**核心 IA 原則：** 使用者回到專案後第一個問題是「我現在該做什麼」，所以 Next Actions 必須在最前；Blockers 並列因為「該做什麼」與「為什麼做不下去」是同等資訊密度。

### 3.4 Scene Detail 兩欄佈局（Round 2 設計重點）

**Main 欄（2fr）由上到下：**

1. Scene Header（pos + 標題 + readiness badge + project badge）
2. Scene Goal / Dramatic Purpose
3. Scene Readiness Panel（badge + checklist 10 項 + next fix）
4. 必要脈絡 / Required Context（warnings + 6 子分區）
5. Beat 與大綱預覽 / Beat / Outline Preview
6. 台詞草稿預覽 / Dialogue Draft Preview（**read-only**）

**Side 欄（1fr）由上到下：**

1. 下一步（紫色 highlight 卡片）
2. ⚠ 卡點 / Blockers
3. QA 結果 / QA Findings（含 severity badge + affected reference + summary）
4. Human Decision 待裁決（含 blocking / non-blocking badge）
5. Canon Delta 候選
6. Agent 動作 / Mock Agent Actions

**Responsive：** 寬度 ≤920px 時兩欄變單欄（main 在上、side 在下）。

---

## 4. UI 元件目錄

### 4.1 基礎元件

| 元件 | 用途 | tone 變體 |
|---|---|---|
| `.btn` | 按鈕 | default / primary / ghost / small / disabled |
| `.badge` | 狀態小標 | info / success / warning / danger / muted / future |
| `.card` | 卡片容器 | clickable（hover translateY） |
| `.info-icon` | 術語 tooltip 觸發點（`?` 圓形） | hover 變色 |
| `.glossary-pop` | tooltip 浮層（深底） | 在兩主題下都保持深色 |
| `.summary-chip` | header 圓角 chip | info tone |
| `.theme-toggle-btn` | 主題切換 pill | 自帶 hover 反白 |
| `.placeholder-note` | 灰底 dashed 提示框 | 用於空狀態 / mock 註記 |

### 4.2 結構元件

| 元件 | 出處 | 說明 |
|---|---|---|
| `.proto-banner` | 全頁 sticky 頂部 | 黃色 PROTOTYPE 標籤 + 控制區（theme / empty toggle） |
| `.app-header` | 全頁 header | brand + breadcrumb + header-actions |
| `.breadcrumb` | navigation | 含 `.sep` 分隔點與 `.current` 當前位置 |
| `.pd-header` | Dashboard 頂部 | 4 個 count-cell metric grid |
| `.sd-header` | Scene Detail 頂部 | pos pill + 標題 + badge row |
| `.sd-layout` | Scene Detail body | CSS Grid 2:1，<920px 變單欄 |
| `.sd-block` | Scene Detail 內每個區塊 | 包含 `.sd-block-title` |

### 4.3 列表 / 表格元件

| 元件 | 出處 | 視覺特徵 |
|---|---|---|
| `.hero-list` | Dashboard HERO 區 | 帶箭頭 ▸ 與右側 → |
| `.mini-list` | Dashboard Triplet | item 為 surface-alt 卡片 |
| `.summary-list` | Scene Detail side | item 帶 hover border 變色 |
| `.checklist` | Scene Readiness Panel | 左側 status icon 顏色映射 |
| `.scene-table` | Legacy 場景索引 | hover row 變色 |
| `.lines-list` | Dialogue Draft Preview | grid 90px / 1fr / auto 三欄 |
| `.module-grid` | Module Navigation | auto-fill cards，Future 卡片虛線 |

### 4.4 互動元件

| 元件 | 行為 |
|---|---|
| `.readiness-chip` | hover translateY，zero count 半透明，data-nav 跳 filtered queue |
| `.sq-filter-chip` | 點擊套用 filter，active 狀態反白 |
| `.scene-card` | clickable 卡片，hover 上抬 + 陰影加深 |
| `.modal-backdrop` | 點擊背景關閉 modal |
| `.modal-card` | 中央 overlay |
| `.next-action-card` | Scene Detail side 紫色 highlight，點擊跳 modal 或 agent action |

### 4.5 狀態指示元件

| 元件 | 用途 | 視覺特徵 |
|---|---|---|
| `.count-cell` | 4 格 metric（Blockers / 待裁決 / QA / Canon Δ） | num 大字 + lbl 標籤，tone 變色 |
| `.rp-badge` | Readiness 主 badge | 5 種 tone（success/warning/danger/info/muted） |
| `.future-tag` | Future 模組角標 | 絕對定位右上 |
| `.sc-strip .step` | Scene card 上的 mini production strip | 6 段彩色長條 |
| `.qa-tag` / `.info-tag` | dialogue line 上的標記 | high/medium 不同色 |

---

## 5. 設計 Token 系統

### 5.1 完整 token 列表（36 個）

```
基礎 surface 系
--bg / --surface / --surface-alt / --surface-hover

邊線系
--border / --border-strong

文字系
--text / --muted / --subtle

主色（Primary，藍）
--primary / --primary-hover / --primary-soft / --primary-soft-border

警告（Warning，琥珀 / 金）
--warning / --warning-bg / --warning-border / --warning-text / --warning-text-strong

危險（Danger，紅）
--danger / --danger-bg / --danger-border

成功（Success，綠）
--success / --success-bg / --success-border

資訊（Info，藍系）
--info / --info-bg / --info-border / --info-border-hover

未來 / 灰階
--future / --future-bg / --future-border

Prototype banner 專用
--proto-bg / --proto-border / --proto-active-bg / --proto-active-text / --proto-controls-btn-bg

特殊
--modal-backdrop / --shadow-sm / --shadow-md / --shadow-lg / --radius
```

### 5.2 Light vs Dark 對照（重點變化）

| 角色 | Light | Dark |
|---|---|---|
| 頁面背景 | `#f5f6fa` | `#0f1115` |
| Card 表面 | `#ffffff` | `#1a1d23` |
| 主色 Primary | `#4a6cf7` | `#6c8aff` |
| Warning 主色 | `#b8860b`（深琥珀） | `#fbbf24`（金黃） |
| Danger 主色 | `#c94a4a` | `#f87171` |
| Prototype banner 底 | `#fff5d4` | `#3d2f10` |

**設計原則：** dark mode 的「主色」普遍提亮（從深色提到中亮），背景則加深，確保對比 ≥4.5:1（粗略未實測）。

### 5.3 主題切換實作

1. `<html>` 設 `data-theme="dark"` 屬性切換
2. CSS `[data-theme="dark"] { ... }` 覆寫 `:root` 變數
3. `<head>` 內有 early bootstrap script，first paint 前讀 localStorage 套上 attribute
4. 主 script 的 toggle handler 寫入 localStorage + 同步按鈕 label
5. body 加 `transition: background-color/color .2s ease` 讓切換平滑

**Anti-pattern 避開：** 沒有用 `prefers-color-scheme` 自動偵測系統主題（這是有意保留 — 預設 light，等使用者明示切換）。

---

## 6. 互動模式（Mock vs Real）

### 6.1 路由級切換（**真做**）

- Workspace Home ↔ Project Dashboard ↔ Scene Queue ↔ Scene Detail
- Scene Detail ↔ Modal（其實 Modal 不是路由，是 DOM 注入）
- Scene Queue filter chip → 切 URL hash
- Breadcrumb 任何上層連結
- Project Dashboard 上的 Scene Readiness chip → filtered Scene Queue
- Project Dashboard Next Action 中 target=scene-detail → 直跳 Scene Detail

### 6.2 Modal 開關（**真做**）

- 開啟：點 QA / HD / Canon Delta item 或 Next Action target=modal-*
- 關閉路徑（4 條，**都該保留**）：
  1. 右上 `×` 按鈕
  2. 點背景灰區
  3. 按 `Esc`
  4. Foot 區 `關閉` 按鈕

### 6.3 元件級 mock（**alert**）

- 新增專案 / 排序 / project menu（封存/隱藏/刪除）
- 跨專案待裁決 chip
- Project Dashboard 中其他 next action（非 scene-detail）/ blocker（無 sceneId）/ Triplet item / reading-item
- Future module 卡片
- Templates preview 中所有 placeholder
- Scene Detail 中 ref-link / scene-blocker / agent action
- Modal 內所有 action 按鈕（accept / reject / defer / view-line / create-hd / request-rewrite / accept-write / revise）

### 6.4 Disabled 互動（**無 click handler，僅 tooltip**）

- Beat 內 line 旁的 lock 🔒 / rewrite ↻ / reorder ⇅ 按鈕（per A4 設計 ruling — preview only）
- 標記 `enabled=false` 的 agent action（顯示 ⊘ + warning 文字）

### 6.5 持久化狀態（**真做，localStorage**）

- 主題偏好 `narrative-ws-theme`：`'light'` | `'dark'`
- 容錯：以 `file://` 開啟若擋 `localStorage`，try/catch 容忍，切換仍可用但不持久化

### 6.6 鍵盤行為

- `Esc` 關閉 modal
- `Tab` 焦點順序遵循 DOM 順序（無客製 tabindex 管理）
- 元素 `tabindex="0"` 用於 info-icon（讓 keyboard 使用者也能聚焦觸發 tooltip）

---

## 7. Mock Data 結構

> ⚠ 所有結構皆為 UI prototype 呈現用，**不是 schema 提案**。重構時可全面重設計資料結構。

### 7.1 全域 window.MOCK 結構

```text
window.MOCK = {
  __mock__: true,
  __notice__: 'PROTOTYPE MOCK DATA — not a schema...',
  glossary: { '<term>': '<plain-language definition>', ... },     # 13 條
  readinessLabels: { READY: {label, tone}, ... },                  # 7 種
  workspace: { name, crossProjectPendingDecisions, ..., templateLayerEntry },
  moduleDefs: [ {id, label, desc, future}, ... ],                  # 8 module
  projects: [ {Project}, ... ],                                    # 3 個 mock project
}
```

### 7.2 Project 物件主要欄位

```
id, name, type, status, lastUpdated, nextStep, phase
blockers, pendingDecisions, qaFindings, canonDeltaCandidates  (4 個 summary count)
sourceImport / bibleStatus / plotStatus / sceneStatus / dialogueStatus / qaStatus
  (6 個 phase block，各帶 state + detail)
humanDecisionItems, canonDeltaItems, nextActions, blockerItems, agentPreTaskReadingList
scenes[]
```

### 7.3 Scene 物件主要欄位（**Round 2 巢狀**）

```
id, chapter, position, label, title, dramaticPurpose
readiness:
  badge: '<READY|READY_WITH_RISK|...>'
  checklist: [{id, label, status, detail}, ...] (10 項)
  nextFix: '<plain-language 祈使句>'
taskStatus, dialogueStatus, qa
humanDecisionsCount, canonDeltaCount
requiredContext:
  bibleRefs[], characters[], relationships[], worldVocab[]
  infoReveal[], warnings[]
beats: [{id, title, purpose, emotionalTurn, infoRevealNote, dialogueStatus, lines: [...]}]
qaFindings: [{id, severity, title, affected, summary, suggestedActions}]
humanDecisions: [{id, priority, blocking, title, area, preview}]
canonDeltas: [{id, source, title, state, pendingReview, impact, preview}]
nextAction: {label, target, sceneId?, hdId?, qaId?, agentActionId?}
blockers: [{id, text, area}]
agentActions: [{id, label, enabled, warning?}]
```

### 7.4 三個 mock project（用於測不同階段）

- `urban-fantasy` — Bible Building（3 scenes：READY / BLOCKED / AWAITING_DECISION）
- `wuxia-ensemble` — Dialogue Generation（4 scenes：DRAFT_PENDING_QA / READY_WITH_RISK / READY / BLOCKED）
  - 最豐富的 demo scene：`ch02-s04`（READY_WITH_RISK + 2 QA + 1 HD + 1 Canon Delta + 4 agent actions）
- `campus-mystery` — Source Intake（0 scenes — 測 empty case）

---

## 8. 三條核心設計守則（G1 / G2 / G3）

這三條是「即使重構也應該守住」的設計戒律，原始來自資料結構分析端：

### G1：狀態 label 是 UX label，不是 enum

同一 scene 可能同時帶多個狀態信號（例：QA pending + Needs Decision + Delta pending）。
prototype 為了 UX 顯示簡化成單一 badge + checklist，但這個簡化方式**不能被當成正式狀態模型**。

→ 重構時：badge 旁一定要搭配 detail / checklist，不要單靠 badge 表達完整狀態。

### G2：Production mini-strip 是 workflow visualization，不是狀態機

實際 scene production 可能回退、跳步、重跑 QA、並行處理。
Scene card 上的 6 段 mini-strip 順序只是 UI reading order，**不是步驟強制流向**。

→ 重構時：若要做生產進度視覺化，明確標註「視覺呈現用，不代表必然順序」（prototype 已加 tooltip）。

### G3：Beat 是 UX grouping，不是正式資料層必要單位

未來可能支援短 scene、branching dialogue、gameplay-triggered dialogue，**不能強迫每句 line 都屬於 beat**。

→ 重構時：Dialogue Draft Preview 的 beat 分組是 OK 的，但元件不能依賴「每場必有 beat」這個假設。

---

## 9. 命名與文案規則

### 9.1 中文主 + 英文 sub（Round 2.1 確立）

prototype 採用「中文主標 + 灰字 / 小字英文 sub-label」格式：

```html
<h3>下一步建議 <span class="en-sub">/ Next Actions</span></h3>
```

範例：

- `下一步建議 / Next Actions`
- `卡點 · 風險 / Blockers · Risks`
- `場景就緒度 / Scene Readiness Panel`
- `必要脈絡 / Required Context · Bible Reference (mock)`
- `台詞草稿預覽 / Dialogue Draft Preview · read-only`
- `Beat 與大綱預覽 / Beat / Outline Preview`
- `QA 結果 / QA Findings`
- `Agent 動作 / Mock Agent Actions`

### 9.2 文案語氣

- **Next Fix / Next Action 用具體祈使句**：不寫「需審核」，寫「審核 3 條角色設定衝突，再啟動 Scene Task」。
- **Mock 標記要明顯**：所有 mock action 與 modal foot 都有「所有按鈕為 mock — 不寫真資料」灰字提示。
- **錯誤提示四件套**：What / Where / Why / How to fix（prototype 中的 not-found / missing / conflict 案例皆遵循）。

---

## 10. 已知問題與重構候選

> 以下是 prototype 已知但**沒解決**的問題，重構時可選擇處理。

### 10.1 工程結構面

| 問題 | 描述 | 建議方向 |
|---|---|---|
| 單檔過大 | index.html 1630 行（single-file 版 2298 行） | 重構成 modular code（依框架選擇拆 component） |
| 無建置流程 | 純原生 HTML/CSS/JS | 視需求加 Vite / esbuild / 等（保留瀏覽器直開的可能性） |
| 無型別保護 | mock_data 巢狀 5 層，欄位錯字不會被偵測 | TypeScript / JSDoc |
| 無測試 | 沒有任何 unit / integration test | 至少對 router / readiness 計算 / modal 開關加 test |
| State 散落 | 全頁 state 都在 `window.MOCK` 與 hash | 引入 state management（小規模可用 signal/observable） |

### 10.2 設計面（重構機會）

| 議題 | 現況 | 改善方向 |
|---|---|---|
| Mock 互動 fidelity 不一致 | 路由真做 vs alert vs disabled tooltip 三層混用 | 統一互動規範（或明確標示每類） |
| 沒有 loading 狀態 | 所有 view 同步渲染，無 skeleton | 加 loading skeleton（若改成 async data） |
| 沒有錯誤邊界 | render 出錯整頁壞 | error boundary / fallback view |
| 沒有 i18n | 中文寫死在 view 渲染與 mock data 中 | 抽 i18n string table，至少中英切換 |
| 沒有 a11y 完整支援 | 基本 aria-label / role 有，但缺 focus trap、live region 等 | 補 modal focus trap、announce 等 |
| 沒有 RWD | 只在 Scene Detail @920px 做 grid 切換，其他畫面在窄視窗會擠 | 全面 review responsive |
| 沒有列印樣式 | 列印效果未定義 | 視需求加 `@media print` |

### 10.3 IA / UX 面（已留 review queue）

| 議題 | 為什麼 |
|---|---|
| Project Dashboard 上半 + Scene Readiness chips + Module Status + Triplet 是否資訊過載 | 使用者實際 review 後可能要折疊或重排 |
| HD blocking vs non-blocking 用 danger / warning badge 是否反邏輯 | non-blocking 用 danger 似乎錯位 |
| Scene Detail 主欄資訊密度高，是否該 sticky 側欄 | 長 scroll 時側欄會看不到 |
| Beat 內 lock / rewrite / reorder 按鈕用 disabled + tooltip，是否會被誤判為「等之後啟用」 | 其實是「不打算做」 |
| Future module 灰階是否還夠清楚 | 在 dark mode 下可能更不明顯 |
| Modal 採 centered overlay vs side sheet | sheet 在現代 productivity tool 更常見 |

### 10.4 資料結構面（**警告區**）

> ⚠ 以下不是 schema 提案，是「重構若要動資料層，請先讀」。

prototype 的 mock_data 為呈現方便採用了高度巢狀結構（scene 內包 beats、beats 內包 lines、scene 還有平行的 qaFindings / humanDecisions / canonDeltas array）。**這個結構不是 schema 設計建議**。資料層重構時應該：

1. 與 UI 解耦（mock_data shape 不該決定真資料結構）
2. 考慮 G3：scene 不一定有 beat，beat 不一定有 line
3. 考慮 G1：scene 可能同時帶多重狀態，現在的 `readiness.badge` 是單值
4. QA finding 的 `affected.beatId` / `affected.lineId` 是 prototype 為顯示方便編的，正式 stable reference 待設計

---

## 11. 重構路徑建議

依重構深度遞增：

### Level 1：純 UI tech-stack 升級（保留所有 UX）

- 維持所有畫面、IA、互動模式不變
- 把原生 JS 轉成框架（React/Vue/Svelte）
- 加 build tool、TS
- 拆 component
- 加 test
- 補 i18n / a11y / RWD

**保留：** §3 IA、§4 元件目錄、§5 token 系統、§6 互動模式
**改進：** §10.1 工程結構面

### Level 2：UX 局部修正（基於本 prototype 的 review queue）

在 Level 1 上：
- 處理 §10.3 列出的 IA / UX review queue 項目
- 微調 fidelity（讓 mock 邊界更清晰，或開始接真功能）
- 補 §10.2 列出的設計面缺項（loading、錯誤邊界、i18n）

**改進：** §10.3 列出的全部

### Level 3：接真資料層

- 替換 `window.MOCK` 為真實 API / 後端
- 重新設計資料 schema（**不要照搬 prototype mock 結構**）
- 守住 G1 / G2 / G3 三條核心戒律
- 加 loading / error state

**改進：** §10.4 + 整套資料流

### Level 4：產品化

- 真實使用者測試
- 完整 a11y / i18n / 多人協作
- 真實 agent action（取代 mock alert）
- 真實 Bible 引用 / Canon Delta 寫回機制
- 完整 Dialogue Editor（取代 read-only preview）
- Future module（Info Reveal / Export）落地

---

## 12. 重構時應**保留**的設計決策（critical）

不論重構走多深，以下幾條都是設計核心，建議保留：

1. **「下一步永遠在最前」**（Project Dashboard 第一個 section）
2. **Next Actions 與 Blockers 並列為 HERO**（同等優先級）
3. **Scene Readiness 三層結構**：badge + checklist + next fix（單 badge 會誤導，per G1）
4. **Scene Detail = production cockpit，不是 editor**：在進入 dialogue editor 前先確認 context、readiness、blockers、QA/HD/CD 影響
5. **Required Context 6 子分區**：Bible refs / characters / relationships / world vocab / info reveal / warnings（這個資訊架構很完整）
6. **三條守則 G1 / G2 / G3**：狀態多重 / 流程非線性 / Beat 非必要
7. **Dialogue Draft Preview 一定要是 read-only**（在 cockpit 階段不該變編輯器）
8. **中央 Modal 而非展開**：QA / HD / Canon Delta 用 modal 標示「審視中的事件」，比 inline 展開更清楚
9. **Modal 內 action 不執行真功能**：所有 lifecycle action 都應有明確的「mock / 待人類拍板」標記
10. **中文主 + 英文 sub 的命名規則**（B4 ruling）

---

## 13. 給新對話的快速上手指南

1. 開 single-file HTML：`narrative_workspace_prototype_v2.1.html`
2. 推薦 review 順序：
   - `#/home` → 點 `[範例] 群像武俠` 卡片
   - Project Dashboard 看 HERO + Scene Readiness chips
   - 點 chip `可生成但有風險` 進 filtered Scene Queue
   - 點 CH02_S04 → 進入 Scene Detail（最豐富的 demo）
   - 點側欄 QA / HD / Canon Delta 三項 → 看三種 modal
   - 切 dark mode 確認所有畫面在深色下仍可讀
   - 回 `#/home` → 用 banner 切 empty state
3. 讀本檔 §11 決定重構 Level
4. 讀本檔 §12 確保保留 critical 決策
5. 讀本檔 §10 評估要處理哪些已知問題

---

## 附錄 A：原始演進紀錄參考

如需細部設計討論紀錄（每 round 的 review queue、UX 驗證目標、可能反推資料層觀察），請參考：

```
game-dialogue-bible/_prototypes/ux/narrative_workspace/prototype_notes.md
```

含 Round 1 / 1.1 / 2 / 2.1 完整 review queue（三標籤 [使用者] / [主控室] / [兩者]）與設計筆記。

## 附錄 B：產品需求候選整理

由 GPT-文件工廠根據 prototype review 整理出的「Product Requirements Candidate Register v0.1」涵蓋：

- 8 項 Product Requirement Candidates
- 7 項 Mock-only / Not Productized Yet
- 8 項 Data-layer Interface Candidates（含 Output Medium / Artifact Type 三分類）
- 8 項 Early Decision Candidates

該文件不在本 repo，但若新對話需要產品需求層級的整理（不只 UI/UX），可向使用者要求。
