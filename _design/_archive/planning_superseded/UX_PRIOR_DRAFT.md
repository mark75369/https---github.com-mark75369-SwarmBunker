狀態：DRAFT
版本：v0.1
最後更新：2026-05-18
適用範圍：來自前期 claude-UX 對話的 UI/UX 設計成果整理 / 給 UI/UX specialist 對話使用
優先級：中（reference）

# UX_PRIOR_DRAFT — 來自前期 claude-UX 對話的設計整理

## 0. 本檔性質與使用方式

這份文件整理了一段已結束的 claude-UX 對話（前後 4 個 Round 的 UI-only prototype 工作）中產生的設計結論，給接手的 UI/UX specialist 對話參考。

**關鍵脈絡（specialist 必讀）：**

- 前期那段 claude-UX 對話**做的是 HTML/CSS/JS web prototype**：一份 self-contained 的 `index.html`（hash routing + 中央 modal + chip filter + dark mode toggle 等），落地在 `_prototypes/ux/narrative_workspace/`。
- 本專案後來確定**沒有獨立 GUI**，所有「使用者介面」都是 agent 對話中的 Markdown 呈現，或匯出到 `view/` 的整合檔。
- 因此 prototype 中所有 button / form / modal / 互動式 chip / theme toggle / popover / hash routing 等 GUI 元件層級的設計**整體已廢棄**（詳見 §2）。
- 但 prototype 過程中產生的**內容層 / 資訊架構層**決策（哪些 block 放在一起、什麼順序、哪些不要做、怎麼描述狀態），有部分可平移到 Markdown 呈現。本檔重點是把這些可平移的部分挑出來給 specialist。

**使用方式：**

- specialist 對照 §1 各小節，分類為「可採用 / 需調整 / 衝突 / 已廢棄」。
- 本檔**不是 canon**，specialist 可以否決任何條目並提出反提案。
- 對於前期未討論的呈現情境，§1 各小節直接寫「未討論，留給 specialist 開展」，避免暗示一個其實不存在的共識。

**前期工作範圍速覽**（給 specialist 一個地理感）：

| Round | 主要產出 |
|---|---|
| Round 1 | Workspace Home、Project Dashboard、模組導航、場景索引快速覽、公版 Harness preview |
| Round 1.1 | light / dark mode toggle（CSS token 系統） |
| Round 2 | Project Dashboard 重排、**Scene Queue**、**Scene Detail（main + side cockpit）**、中央 Modal 系統（QA / HD / Canon Delta） |
| Round 2.1 | UI label 中文化（中文主 + 英文 sub） |

收束後產出了一份 `Product Requirements Candidate Register v0.1`，把 prototype 整理成「需求候選 / mock-only / 資料層 interface 候選 / 早期決策候選」四類。本檔聚焦在純 UI/UX 層，不重複 Register 的需求候選整理。

---

## 1. 已做過的設計決策

對應 UI/UX specialist 的 8 大呈現情境。

### 1.1 對應「查看完整世界觀」的設計

**未討論，留給 specialist 開展。**

前期 prototype 從未呈現過「整個世界觀的瀏覽視角」。最相近的東西是 Scene Detail 中的 Required Context，但那是**單場 scene 引用了哪些 Bible 段落**的清單，不是世界觀本身的閱讀視角。

specialist 需要從零設計 `/view-world` 的 Markdown 結構（章節順序、長文件 TOC、跨節錨點等）。

### 1.2 對應「查看單一角色」的設計

**部分討論：只在 scene context 中摘要列過角色；完整角色卡呈現未討論。**

可平移的設計結論：

- 在 Scene Detail 的 Required Context 內，**參與角色**以列表形式呈現，每項顯示三個欄位：
  - 角色名（粗體）
  - 角色定位（如 `protagonist` / `antagonist` / `mentor` / `foil`）
  - 聲線卡狀態 badge（DRAFT / REVIEW / LOCKED — 用顏色 tone 區分）
- 聲線卡狀態使用既有的三層 lifecycle status（DRAFT < REVIEW < LOCKED），這條與 root protocol 一致，可直接平移。

**未討論：**

- 單一角色完整視角（`/view-character`）的 Markdown layout
- 角色內各 section（聲線、關係、弧線、出場 scene 列表等）的排版順序
- 多角色之間的相互引用 / 跨檔導航
- 「次要角色 / NPC」與「主要角色」是否使用不同精簡度的呈現

留給 specialist 開展。

### 1.3 對應「查看大綱 / 細綱」的設計

**部分討論：單場 scene 內的 beat outline 有結論；章節或全故事大綱未討論。**

可平移的設計結論（scene 內的 beat outline）：

- 每個 beat 顯示四個欄位：
  - 標題（如「Beat 1：劍鋒相對」）
  - **Purpose**（戲劇功能）
  - **Emotional turn**（情緒轉折，如「對立 → 動搖」）
  - **Info reveal note**（揭露邊界，如「反派可揭露至 70%」）
- 每個 beat 帶一個 dialogue status badge（v01 試寫 / v02 收斂 / FINAL / 未開始）。
- Beat 順序 = scene 內閱讀順序，不暗示生產順序（呼應守則 G3，見 §4）。

**重要邊界（守則 G3）：** Beat 只是 UX grouping，**不是正式資料層必要單位**。未來可能支援短 scene、分支 dialogue、gameplay-triggered dialogue 等不一定有 beat 的情境。specialist 在 Markdown 中若要用 beat 分組，不能在格式中假設「每場必有 beat」。

**未討論：**

- 章節大綱（chapter outline）的 Markdown 呈現
- 全故事大綱 / 細綱
- 角色弧線（character arc）的呈現
- 章節之間的順序與分隔
- 主線 + 支線交織的視覺呈現

留給 specialist 開展。

### 1.4 對應「進度看板 /status」的設計

**已充分討論，是前期最多投入的區塊。可平移度最高。**

Prototype 中的 Project Dashboard 經 Round 2 重排後採用以下「閱讀順序」（**順序本身是設計重點**，因為它定義「使用者回到專案後先看到什麼」）：

1. **專案身份頭**：name / phase pill / status badge / lastUpdated / 四個 summary metric（Blockers / 待裁決 / QA Findings / Canon Δ 計數）
2. **HERO 區：下一步建議**（最優先；Markdown 中應作為 `/status` 的第一個 section）
3. **HERO 區：卡點 / 風險**（與「下一步」並列同等優先級）
4. **場景就緒度總覽**：7 個 readiness 狀態的計數（可生成台詞 / 可生成但有風險 / 暫不可生成 / 等待裁決 / 等待資料 / 已有草稿待 QA / QA 後需重寫）
5. **模組狀態總覽**：6 個生產階段（原始資料導入 / Bible 整理 / 劇情章節 / 場景索引 / 台詞生產 / QA），每個顯示一行「state + detail」
6. **三欄區**：Human Decision 待裁決 / Canon Delta 候選 / Agent 任務啟動前必讀清單
7. **模組導航**（次要入口，視覺權重明顯降低）

可平移到 Markdown `/status` 的核心設計原則：

- **下一步永遠在最前**——使用者回到專案後，第一個想知道的不是資料總覽，是「我現在該做什麼」。
- **卡點與下一步並列**——「該做什麼」與「為什麼做不下去」是同等資訊密度，不該把卡點藏到後面。
- **就緒度用計數呈現，不要用單一 progress bar**——一個 scene 可能同時 QA pending + 等待裁決 + Canon Delta 候選，單一進度條會誤導（守則 G1）。
- **狀態文字保持人類可讀**，避免直接暴露 enum 鍵（如不寫 `READY_WITH_RISK`，寫「可生成但有風險」）。
- **Workspace 層（跨專案）只放 summary chip**：前期有設計一個「跨專案待裁決 N」chip 放在 header，作為提醒使用者「有沒有什麼 cross-project 事項」的入口。可平移為 Markdown 全局狀態頂部的一行摘要。

**未討論：**

- /status 是否需要章節 / 場景級別的展開
- 多專案總覽的 Markdown 形式（前期只是 chip + alert，沒有實作展開）
- /status 在不同生產階段（Source Intake / Bible Building / Dialogue Generation）是否該有不同 layout

### 1.5 對應「REVIEW gate 清單」的設計

**部分討論：scene-level「就緒度檢查」有完整模式可平移；6 個正式 REVIEW gate 的具體清單未討論。**

Prototype 中最接近 REVIEW gate 的是 Scene Detail 的 **Scene Readiness Panel**，採三層結構：

1. **總結 badge**（單一狀態標籤，例「可生成但有風險」；UX label，不是 enum）
2. **分項 checklist**（10 項依賴）：
   - 每項：狀態 icon + 標題 +（可選）詳情副文字
   - 狀態 icon 對應顏色語意：
     - `ok` ✓（綠）
     - `partial` ◐（黃）
     - `missing` ○（紅）
     - `conflict` ⚠（紅）
     - `blocked` ⚠（紅）
     - `review` ◑（藍）
     - `na` —（灰）
   - 例：「角色關係無衝突 / conflict / 主角 ↔ NPC：聲線卡 vs 關係矩陣不一致」
3. **明確的 Next Fix**（一句白話，告訴使用者下一步具體做什麼，例「優先處理 1 項 high-risk QA finding，再裁決破格句保留性」）

可平移到 Markdown REVIEW gate checklist 的設計原則：

- **不要只給 badge 就結束**——badge 看起來權威，但實際狀態通常多重；單 badge 容易誤判（守則 G1）。**badge 必須搭配 checklist 才能完整描述**。
- **每項 checklist 帶詳情**——不要只說「✗ 缺資料」，要說「✗ 缺資料 / 夜守規則尚有 1 條 DRAFT」，這樣使用者知道去哪修。
- **Next Fix 用具體祈使句**——不要寫「需審核」，寫「審核 3 條角色設定衝突，再啟動 Scene Task」。
- **icon 可用 Markdown 等效符號替代**：✓ → `[x]` 或 `✓`、◐ → `~`、✗ → `[ ]` 或 `✗`，視 specialist 整體風格而定。

**未討論：**

- 6 個正式 REVIEW gate 各自的清單內容
- 各 gate 之間的順序與依賴
- gate 通過 / 未通過後的下一步路徑
- 跨 gate 的整合視角

留給 specialist 對應到專案實際的 6 個 gate 設計。

### 1.6 對應「QA 報告閱讀體驗」的設計

**部分討論：scene context 中的單筆 QA finding 摘要有結論；5 份正式 QA 報告 + 彙整版未討論。**

Prototype 中 QA finding 在 scene context 內顯示 5 個欄位：

- **Severity badge**（high / medium，顏色區分）
- **Title**（一行濃縮，如「主題宣言式台詞」）
- **Affected 引用**（如「b1 / l2」表示 beat 1 line 2；引用格式僅為 UX 顯示用，不是 schema）
- **Summary 段落**（解釋「為什麼這是問題」、引用具體台詞、給修改建議）
- **Suggested actions 列表**（如「view affected line / 轉為 Human Decision / request rewrite」——僅作為 mock 列舉，HTML prototype 中是 interactive button，**這部分按鈕廢棄**）

可平移到 Markdown QA 報告的設計原則：

- **Severity 是 scan 時最重要的訊號**——應該在每項 finding 的最前端（例如標題前綴 `[HIGH]` / `[MEDIUM]`）。
- **Affected 引用要夠精確讓使用者能定位到該行**——不要只寫「Beat 1 有問題」，要寫到「Beat 1 / Line 2 / 角色：主角」這個粒度。
- **Summary 要回答「為什麼」**，不只是「什麼錯了」。同時最好給出**具體的修改建議**（如「建議改為『不過是路過。』」）。
- **「suggested actions」改為純列舉文字**：在 Markdown 中是「可選的下一步」列表，不是按鈕。

**未討論：**

- 5 份 QA 報告（AI 味 / 聲線一致性 / 禁用詞 / 資訊控制 / 格式）各自的 Markdown 結構
- 彙整版 QA 報告的 layout
- QA finding 跨 scene 彙總（例如「全章 high-risk findings」）
- QA finding 與 Human Decision 之間的轉換流程在文件中如何呈現

留給 specialist 開展。

### 1.7 對應「跨檔導航」的設計

**部分討論：在 HTML hash routing 框架下做過。原 routing 機制廢棄，但 breadcrumb 與「回到 X」的概念可平移。**

Prototype 用 hash routing（如 `#/project/<id>/scene/<sid>`）做跨頁切換。這套機制**完全不適用 Markdown**，但下面這幾個概念在 Markdown 中仍可用：

- **Breadcrumb 引導列**：頁面頂部寫「工作區首頁 / [專案名] / 場景列隊 / 比劍對峙」這種定位字串，讓讀者知道「我在文件結構的哪裡」。Markdown 中可寫成第一行的引用塊或 italics 行。
- **「← 回到 X」連結**：每個 detail 頁面最上方一行的「← 回 [上層名稱]」相對連結（用 Markdown 相對路徑 `[← 回場景列隊](./scene-queue.md)`）。
- **單向 reference**：當文件 A 引用 文件 B 時，A 中給連結到 B，但 B 不必反向列出所有引用它的文件——避免雙向維護成本。

**未討論：**

- view/ 整合檔的內部錨點命名規則（heading slug、anchor 格式）
- 跨檔相對路徑的根目錄假設（是相對於 view/ 還是 project root？）
- 同一專案多份 view 檔之間的索引檔
- view 檔的 update / regenerate 時跨檔 link 失效的提示

留給 specialist 對應 `/view-*` 與 `/export-*` 的實際結構處理。

### 1.8 對應「錯誤提示」的設計

**部分討論：HTML prototype 有幾個基本錯誤狀態樣本。設計原則可平移。**

Prototype 中出現過的錯誤類型 + 範例文案：

| 類型 | 範例文案（prototype 中的） | Markdown 平移建議 |
|---|---|---|
| Not Found | `找不到 project：xxx。 [回工作區首頁]` | 寫清「找不到什麼」+「可去哪驗證 / 修正」 |
| Empty state | `本場無 blockers。`（斜體灰字） | 不只說「無 X」，可同時提示「這是正常狀態」或「下一步可考慮…」 |
| Missing required | `Scene goal 未填` | 點出哪個欄位 + 提示去哪填 |
| Conflict | `主角與 NPC：聲線卡 vs 關係矩陣不一致` | 一定要點出兩個衝突來源的具體位置 |
| Pending external | `Human Decision 待裁決後啟用` | 說明「為什麼現在不能做」+「等什麼條件解除」 |

可平移的設計原則：

- **錯誤訊息四件套**：
  1. **What** 發生什麼事
  2. **Where** 在哪個檔案 / 哪個欄位 / 哪個 scene
  3. **Why**（如果有助於使用者理解）
  4. **How to fix** 具體下一步
- **不要顯示 stack trace 或 error code**——使用者看的是 Markdown，不是 console。
- **區分「使用者輸入錯誤」與「系統狀態不滿足」**——前者是「你拼錯了 / ID 不存在」，後者是「這個 scene 的 Bible context 還沒備齊」。兩種錯誤需要不同口氣與不同修復路徑。

**未討論：**

- skill 在使用者輸入錯誤時的具體文案模板
- 多錯誤累積時的彙整呈現
- 錯誤 severity 的分級
- 錯誤是否該寫入 log 或只顯示給使用者

留給 specialist 開展。

---

## 2. 已廢棄方向

以下方向在前期 prototype 對話中**有實作或討論過**，但因為本專案最終確定「沒有獨立 GUI、所有 UI 是 agent 對話 Markdown 或匯出檔」，**全部廢棄**。specialist 不應重複這些設計。

**廢棄的 UI 元件層級：**

- 互動式 button / form / dropdown / checkbox / radio
- 中央 modal overlay（QA / Human Decision / Canon Delta 詳情都用 modal 呈現）
- backdrop click-to-close / Esc-to-close 三條關閉路徑
- Chip filter（互動式、點擊切換 filter state）
- Card hover transitions（translateY / box-shadow 變化）
- Disabled button + tooltip（用於 mock 標記「本輪不執行」）
- Sticky banner 與「PROTOTYPE」黃色頂部 banner

**廢棄的 UI 系統層級：**

- Hash routing（`#/home`、`#/project/<id>/scene/<sid>` 等）
- 路由級切換 vs 元件級 mock 的 fidelity 區分
- Light / Dark mode toggle 與整套 CSS variable theme 系統
- 早期 theme bootstrap（避免 first-paint 閃爍）
- localStorage 偏好持久化
- Empty state toggle 按鈕（review 用切換 home view）
- Glossary tooltip（互動式 `?` icon + 黑色 popover + 點擊任意處關閉）

**廢棄的工程結構：**

- `_prototypes/ux/narrative_workspace/` 四檔結構（`index.html` / `mock_data.js` / `README.md` / `prototype_notes.md`）
- self-contained HTML + inline CSS + inline JS 模式
- React-style component thinking（即使是 vanilla JS）
- 任何形式的 frontend app 規劃（package.json / Vite / Next / Electron / React app 都已多次明示禁止，**這條延續到 specialist 階段**）

**廢棄的命名候選**：

下列命名雖然在 prototype 中使用過，但因為 GUI 廢棄、且專案實際使用語境改變，**不要直接搬到 Markdown**：

- `場景列隊 / Scene Queue`（這個是 GUI 上的場景卡片清單頁，Markdown 中可能更適合叫「場景索引」或「scene index」之類）
- `單場控制台 / Scene Detail / Scene Production Cockpit`（GUI 上是個 main + side 兩欄頁面，Markdown 中可能就是「單場視圖」）
- `公版 Harness / 模板管理`（GUI 上是 workspace-level 工具入口卡片）
- `人類裁決收件匣`（GUI 上是個 inbox 模組）

specialist 應該根據實際 `/view-*` 命名重新決定，**不要為了對齊 prototype 而妥協 Markdown 命名**。

---

## 3. 未涵蓋議題

specialist 對話需要從零處理的議題（前期 claude-UX 對話完全沒碰，或只擦邊）：

1. **`/view-world` 完整世界觀的 Markdown 結構**——長文件 TOC、章節分隔、地名 / 派系 / 規則的呈現方式。
2. **`/view-character` 單一角色完整視角**——聲線卡如何在 Markdown 中呈現，多 section（聲線 / 關係 / 弧線 / 出場場景）排版順序，主要 / 次要 / NPC 角色的精簡度差異。
3. **`/view-outline` 章節大綱**與 **`/view-detailed-outline` 細綱**的差異化呈現。
4. **`/export-*` 整合檔的閱讀體驗**——把多個 view 合併成一份檔的 layout 決策、TOC 設計、章節順序、跨節錨點。
5. **6 個正式 REVIEW gate**——前期只討論 scene-level readiness（單一場景能否進入台詞生產），沒有設計 project-level 的 6 個 gate。
6. **5 份 QA 報告**（AI 味、聲線一致性、禁用詞、資訊控制、格式）各自的 Markdown 結構與**彙整版**結構。
7. **使用者輸入錯誤的 skill 內提示文案模板**——前期只有靜態錯誤 placeholder，沒有設計 skill 在使用者打錯指令 / 缺參數 / ID 不存在等情境的對話文案。
8. **長文件導航**——單份 Markdown 文件內的 TOC、anchor、heading slug 規則、回到頂部、章節展開折疊（若使用 Markdown 編輯器支援）。
9. **跨檔相對路徑的根目錄假設**——`/view-*` 之間互相 link 時，基準是 view/、project root、還是某個固定點？
10. **多 medium 輸出形式**（前期 Register §5.8 列為 future）——例如同一場 scene 可能同時匯出 dialogue draft、scene script、subtitle 包等，這在 Markdown 層的呈現策略未討論。
11. **agent 對話中的「臨時呈現」 vs `/view-*` 的「正式呈現」差異**——使用者可能在對話中要求看一個摘要，這跟 export 一份檔是不同情境，文字密度與排版可能不同。
12. **i18n / 中英混排規則**——前期確定「中文主 + 英文 sub」，但 sub 的字級、字色、是否必須加、何時可省略，沒有定案。

---

## 4. 給 UI/UX specialist 的提醒

從前期 claude-UX 對話的角度，提醒 specialist 注意以下幾點：

**1. 整個 HTML/CSS/JS prototype 已死透，但**：不要因此忽略 prototype 過程的設計討論。Prototype 雖然死了，但「閱讀順序 / 資訊優先級 / 哪些 block 放在一起」這層的決策有些可以平移。本檔 §1 標「可平移的設計結論」的部分就是這類資產。

**2. 三條核心守則（G1 / G2 / G3）在 Markdown 層仍然成立**：

- **G1 / 狀態 label 是 UX label，不是 enum。** 同一場 scene 可能同時帶 QA pending + 需要裁決 + Canon Delta pending，**不要在 Markdown 中用單一狀態欄位收斂多重狀態信號**。建議用「主狀態 + 標記清單」雙層呈現（badge + checklist）。
- **G2 / Workflow visualization 不是 state machine。** 實際生產可能回退、跳步、重跑 QA、並行處理。Markdown 中若要呈現「生產流程進度」，**順序只是 reading order，不是強制步驟**。具體警示文案：在任何 step strip / progress 視覺旁，明確標註「視覺呈現用，不代表流程順序」。
- **G3 / Beat 是 UX grouping，不是資料層必要單位。** 在 dialogue 呈現中用 beat 分組是 OK 的，但**不能在格式中假設「每場必有 beat」**——未來可能有短 scene、分支 dialogue、gameplay-triggered dialogue。

**3. Mock data shape 不是 schema 提案。** 前期 prototype 為了渲染畫面，給每場 scene 編了一份 mock 結構（含 readiness checklist 10 項、beats、mock lines、scene-scoped QA / HD / Canon Delta 等）。這些**全部都不是 schema**，specialist 不要因為這份 mock 存在就假設資料層會這樣設計。資料格式 specialist 那邊獨立在跑。

**4. Production Loop 概念可保留**：原始資料 → Bible → Scene Task → Dialogue → QA → Human Decision → Canon Delta → Bible（回流）。這是專案的核心生產循環，可在 `/status` 與 `/view-*` 中作為敘事骨架。

**5. 中文主 + 英文 sub 的命名規則**：前期 Round 2.1 把所有 UI label 改成這個風格（例「下一步建議 / Next Actions」、「卡點 · 風險 / Blockers · Risks」）。在 Markdown 中是否沿用、什麼情境下省略英文 sub，由 specialist 決定。

**6. 「下一步永遠在最前」是前期 `/status` 區塊最重要的單條結論。** 使用者回到專案後第一個想知道的是「我現在該做什麼」，不是資料總覽。Markdown `/status` 應該把「下一步」section 放在最頂，比 phase 狀態、scene 計數都優先。

**7. 「Next Fix」白話祈使句的模式可重用**。在 scene readiness、QA finding 修復建議、blocker 解除建議等地方，都用一句具體祈使的中文句子告訴使用者下一步做什麼（例「處理 1 項 high-risk QA finding，再裁決破格句保留性」），不要用模糊狀態詞。

**8. Required Context 的子分類在 Markdown 中很可能仍然成立**。前期把單場 scene 的 required context 拆成 6 類：Bible refs / characters / relationships / world vocab / info reveal limits / warnings。這個分類在 Markdown `/view-scene` 中很可能直接可用，視 specialist 對應實際資料層結構而定。

**9. Workspace 層 vs Project 層 vs Scene 層的三層思考**前期已建立。Markdown 中跨檔導航 / `/status` 範圍 / `/view-*` granularity 都需要考慮這三層之間的界線。

**10. 不要被 prototype 中的「Modal / Drawer」誘惑去設計「展開區塊」**。Markdown 不適合做「點擊展開」（雖然 GitHub flavored MD 支援 `<details>`），但 `/view-*` 與 `/export-*` 是線性閱讀的文檔，不是互動 UI。**內容該全部寫出來就全部寫出來**，需要省略時用引用 + 摘要 + 「詳見 X」連結，而不是試圖在 Markdown 中模擬 GUI 的 disclosure。

---

（本檔結束。如 specialist 對話過程中發現任何條目誤導或與實際專案需求衝突，請隨時否決並提出反提案。）
