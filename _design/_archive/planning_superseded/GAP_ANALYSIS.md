狀態：DRAFT  
版本：v0.2  
最後更新：2026-05-18  
適用範圍：需求 refresh 對既有設計的 Gap Analysis / 新 master 對話接手第三步產出  
優先級：最高  

# GAP_ANALYSIS — 需求 refresh vs 既有設計缺口分析

# 0. 文件目的與本檔狀態

本檔由「新 master 對話」（v0.4 之後重啟的 master）在收到 user 需求 refresh 後產出，回答三件事：

1. 需求 refresh 提到但既有產物**未涵蓋**的點（缺口）
2. 既有產物涵蓋但需求 refresh **已不需要**的點（沉沒成本）
3. 既有產物與需求 refresh **衝突**的點（需 user 拍板）

**閱讀順序：** §1 快速映射 → §2/§3 已對齊區 → §4 缺口 → §5 衝突 → §6 結論。

**搭配文件：** `REVISED_WORK_ITEMS.md`（依本檔結論拆任務）、`DECISIONS_LOG.md`（依本檔結論新增 D-NNN / P-NNN）。

**本檔狀態：** DRAFT；user 對 §5 衝突點與 §4.1–§4.3 缺口拍板後升 REVIEW。

---

# 1. 需求 refresh 快速映射

| 需求 refresh 條目 | 對應既有設計 | 已涵蓋程度 |
|---|---|---|
| A-1 與 AGENT 整理世界觀（優先度低） | `/create-world`（00_e）+ UPSTREAM §1.1（11 議題完整提問腳本） | ✓ 100% 設計、≈90% UPSTREAM 內容；實作未啟動 |
| A-2 與 AGENT 整理人設（優先度低） | `/create-character`（00_f）+ `/create-relationship`（00_l）+ UPSTREAM §1.2 / §1.5 | ✓ 100% 設計；實作未啟動 |
| A-3 與 AGENT 整理大綱細綱（優先度低） | `/create-outline`（00_g）+ `/create-detailed-outline`（00_h）+ UPSTREAM §1.3 / §1.4 | ✓ 100% 設計；實作未啟動 |
| B-1 世界觀拆解成台詞生成判斷 + 評測標準 | `/create-world` 階段 4 自動拆分 → 01_a/01_b/01_c/02_*；09_a–f QA 模板對照 00_b §1–§7 | △ 拆分邏輯定義完；評測標準經 00_b 連動 09_a–f，但**「手寫世界觀導入後拆解」這條路徑沒有獨立 skill** |
| B-2 人設拆解成台詞生成判斷 + 評測標準 | `/create-character` 階段 4 拆分 + 09_b 聲線一致性檢查 | △ 同上：「手寫人設導入」路徑缺 |
| C-1 依資訊產出符合 / 低 AI 味台詞 | `/dialogue-write` 三模式（試寫 / 破格 / 收斂）+ UPSTREAM §4 algorithm；`/qa` 5 份報告 | ✓ 設計與 algorithm 完整 |
| **C-2 將台詞依指定需求與格式輸出成對應文件** | 既有 00_c 台詞輸出格式（agent 對話內模式）+ 08_a/08_b 台詞檔模板 | ✗ **嚴重缺口** — 既有設計只涵蓋 chat 內呈現模式，**未涵蓋「角色名+台詞+立繪+KEY」「物品名+說明+圖」等客製化輸出表現格式 + 多 entity 類型 export template 機制**（user 在追問中明示） |
| **D 視覺化管理進度與各種資料** | `/status` 看板（ARCHITECTURE §2.3 範例）+ `/view-*` 動態組合 + `/export-*` 靜態檔 + UX_SPEC §0/§1/§7/§8 | △ 設計方向已立但 **UX §2–§6 全未交付**；且 **user 提到 HTML 原型** 跟 UX_SPEC §1.4「HTML 整層廢棄」存在新衝突，待新 P-NNN 釐清 |

**整體訊號：** 需求 refresh 與既有設計骨幹（Markdown + Git + frontmatter + agent 對話）**完全相容**；偏離出現在「**輸出端 scope**」與「**視覺化具體路徑**」兩塊，而非核心架構。

---

# 2. 已涵蓋且方向完全對齊（整批繼承不動）

下列既有設計與需求 refresh 100% 對齊，**不需任何調整**：

## 2.1 架構與資料層（LOCKED）

- SPEC §1「以 Markdown 為儲存層、以 agent 對話為操作介面」定位 — 直接對應需求 refresh §1 整體
- SPEC §5.1 邏輯實體類型（W / V / C-* / R-*-* / P / CH-* / S-*-*） — 涵蓋需求 A/B/C 上的所有實體
- SPEC §5.2 canonical schema（中文 header 5 欄 + YAML 上游 3 欄 + 下游 8 欄） — 適用範圍不變
- SPEC §5.3 完成度公式 — 直接支援需求 D 的進度視覺化
- SPEC §5.4 expected entity manifest + `.protocol_version.phase_log` — 直接支援需求 D 的「視覺化管理」
- SPEC §16 文件狀態機（7 種狀態） — 全 scope 適用
- SPEC §17 作品專屬 00_b 7 個 section anchors — 直接支援需求 B 的「評測標準從世界觀拆出」

## 2.2 上游創建協議內容（A 優先級降低後仍保留）

- UPSTREAM §1.1（00_e 11 議題） / §1.2（00_f 9 議題） / §1.3（00_g 7 議題） / §1.4（00_h 7 議題） / §1.5（00_l 6 議題）— **內容全保留**，只是實作優先級延後
- UPSTREAM §1.0.1–§1.0.3 共通骨架執行細則 — 不動

## 2.3 下游 pipeline 設計

- UPSTREAM §2 下游 00_k 全內容 — 直接支援需求 C-1
- UPSTREAM §3 6 份 QA 模板（09_a/b/c/d/e/f） — 直接支援需求 B 的「評測標準」
- UPSTREAM §4 `/dialogue-write` 三模式 algorithm — 直接支援需求 C-1
- UPSTREAM §6 多場景並行處理 — 直接支援需求 D 的「方便管理」

## 2.4 已確認的 UX 規則（UX_SPEC §0/§1/§7/§8）

- 三守則 G1 / G2 / G3
- 全文呈現約束（純 Markdown、中文主＋英文 sub）
- 錯誤呈現四件套（What / Where / Why / 下一步）
- 跨檔導航五規則（連結基準 / breadcrumb / TOC / source 引用 / 單向 reference）

## 2.5 既有 D-018 的最終裁決（**6 項中 5 項維持**）

D-018 promote 為最終的 6 項「不採」，**5 項仍維持**：
- retcon vs supersede 區分 — 維持不採
- continuity_check 獨立實體 — 維持不採
- scene 粒度（exchange-level） — 維持不採（維持策略 A 一場一檔）
- protected_tier 多層保護 — 維持不採
- 特殊資料格式 — **此項需 reopen**（見 §5.1）

**但第 2 項「多語言對白」需 supersede**（見 §5.2）：user 在 Q2 答案明示「每段台詞還要有 KEY 來處理多語言」 — 不是要存多語對白本文，而是要 i18n KEY 欄位讓外部系統引用。這跟 D-018 #2「schema 不擴充 `language` / `translation_of`」需要區分對待。

---

# 3. 已涵蓋但優先級/排序需要調整（沉沒成本但仍要做）

## 3.1 Phase A 任務（上游 5 份協議實作）優先級降低

**現況：** TASKS §2 Phase A 含 A.1–A.11，涵蓋 00_b 通用骨架、00_i bootstrap、00_e 世界觀協議、frontmatter 補完、`/init-project` / `/create-world` / `/status` / `/check-gaps` skill 等。Phase B 是其餘上游協議（00_f / 00_g / 00_h / 00_l）+ skill。

**需求 refresh：** A 優先度低 — 「可以先設計，但實作優先度低於其他項目，因為可以使用網頁版的 GPT 或 CLAUDE 處理，但因為沒辦法直接讀取專案資料所以會有上下文導入、繼承等問題而降低效率和品質」（user 原話）。

**Gap：** 既有 TASKS Phase A → B → C → D 是「依賴序」（Phase B 寫 00_f 需要 Phase A 的 00_b 通用骨架就位才能進角色與類型氣質合規檢查；Phase C 的 `/view-*` 需要 Phase B 的角色檔存在才能動態組合；Phase D 的 `/dialogue-write` 需要任務包，任務包需要先有場景索引，場景索引需要先有細綱…）。**單純把 A/B 延後做不通**。

**處理建議（不擅自改 TASKS）：**
- 既有 Phase A/B/C/D 序順本身不動（依賴邏輯不能違反）
- **新增「Phase 0.5：手稿導入快速路徑」**（見 §4.4），讓 user 能繞過 `/create-*` 5 階段對話，直接把已有的世界觀/人設/大綱手稿丟進工具拆解
- 這條捷徑跑完後，B/C/D 的下游 skill 依然能用（因為產出檔結構一致）
- A 路徑（完整 `/create-*` 對話）仍保留設計，但實作排序可放在 D 之後

## 3.2 UX §2–§6 升優先級

**現況：** PHASE_3_COMPLETION_REPORT v3.0 把 UX §2–§6 列為「等剩餘 specialist 補完」的阻塞點，但實作順序上 UX 排第三（資料格式 → 上下游 → UX）。

**需求 refresh：** D 是四大關鍵情境之一；視覺化管理直接關乎 user 對「目前設計到哪了 / 我下一步該做什麼」的掌控感。

**處理建議：** UX 第二輪不再排第三 — **與資料格式 / 上下游第二輪並行啟動**（或甚至先動，因為 UX §2–§6 不依賴資料格式 / 上下游第二輪結論）。詳見 REVISED_WORK_ITEMS §2.3。

## 3.3 既有的 `/create-*` 5 階段對話設計（A 優先級降低後）

**現況：** UPSTREAM §1.1–§1.5 完整交付 40 議題提問腳本（≈90% 內容）。

**Gap：** 內容**沒浪費** — A 優先級雖降低，但仍要做（user 明示「可以先設計」）。沉沒成本不沉沒。

**處理建議：** 內容凍結（不動 UPSTREAM §1.1–§1.5），實作優先級調整為「Phase D 之後」或「跟 D 視覺化並行做、user 看哪個先到就先用」。

---

# 4. 需求新增點 — 既有設計未涵蓋（缺口）

## 4.1 多種「表現格式」客製化輸出機制（**重大缺口**）

**user 原話：** 「主要是輸出成不同的表現格式，像是如果是角色台詞，那就需要有，腳色名、台詞、立繪的格式，且每段台詞還要有 KEY 來處理多語言。而如果是物品說明，那就是物品名、物品說明、物品圖片等，會依照不同需求而有很多變化的輸出格式，所以這塊會需要有辦法大量且彈性客製化和管理」

**既有設計現況：**
- 00_c 台詞輸出格式：只規範 chat 內模式呈現（試寫 / 收斂 / 破格的 markdown 風格）
- 08_a / 08_b：台詞檔模板，但格式固定（DIALOGUE 風格的 markdown 段落 + frontmatter）
- 沒有「export template」「output adapter」「presentation format」機制
- D-018 #6「特殊資料格式」明示「Phase D 後另議」 — 但 user 在 refresh 直接點出 = **本輪要 reopen**

**缺口具體內容：**

1. **Export template 機制** — 同一份 source 台詞檔可依不同 template 匯出成不同表現格式（如 `template:character_dialogue_with_portrait` / `template:item_description_with_icon` / `template:scene_script_for_unity` 等）
2. **輸出表現格式對應的欄位映射** — template 定義「source frontmatter 欄位 + 內容段落」如何映射到「output 欄位」
3. **多 entity 類型支援** — 不只 dialogue，還含「物品」「立繪」等新 entity 類型（見 §4.3）
4. **大量管理** — 多 template 應該有索引、版本、test fixture 等管理機制

**對既有 schema 的衝擊：**
- SPEC §5.2 canonical schema 核心不動（中文 header + YAML）
- 但需要新增「output 端」的擴充：可能是新 frontmatter 欄位 `export_templates: [...]`、可能是獨立的 `/protocol/00_m 輸出模板協議.md` + `_templates/` 目錄
- 需資料格式 specialist 第二輪正式設計

**處理建議：** 新增 P-016「客製化輸出表現格式機制」（見 DECISIONS_LOG 更新）— 屬「需 reopen D-003 / D-018 #6」級議題；資料格式 + 上下游 specialist 第二輪共同設計。

## 4.2 i18n KEY 機制（**重大缺口，supersede D-018 #2**）

**user 原話：** 「每段台詞還要有 KEY 來處理多語言」

**既有設計現況：**
- D-018 #2「多語言對白：最終不採用，schema 不擴充 `language` / `translation_of`」 — promote 為最終
- UPSTREAM §4.6「不採多語」對齊 — `/dialogue-write` 拒絕含 `language: en` 等任務包

**澄清 user 意圖：** **不是要存多語對白本文**（如同一場戲存中文版 + 英文版各一份），而是**每段台詞需要 unique KEY**（例：`dlg.ch01.s03.l001`）讓外部系統用該 KEY 連結各語言對照表。多語言對照本身不在本工具，外部 i18n 系統（PO / JSON i18n / Unity Localization）負責，但本工具必須**提供穩定的 KEY**。

**這跟 D-018 #2 是兩件事：**
- D-018 #2 否決：在本工具 schema 中**存多語對白**（會撐爆 schema、增加維護成本、與 user 真實需求不符）
- 本需求肯定：在本工具中**為每段台詞提供 unique KEY**（schema 微擴充，外部系統消費）

**對 schema 的衝擊：**
- 既有 08_b 台詞檔的 dialogue 段落需要 KEY 欄位（可能在段落 metadata 或行首標籤）
- 新增 frontmatter 欄位 `dialogue_key_prefix` 或在每段加 `<!-- key: dlg.ch01.s03.l001 -->` 註解
- KEY 命名規則需要全 repo unique guarantee
- canon delta 與 retcon 時 KEY 處理規則（保留原 KEY 或新 KEY）

**處理建議：** 新增 P-017「台詞 i18n KEY 機制」並標明 **partial supersede D-018 #2**；資料格式 specialist 第二輪設計具體 schema 微擴充方案。

## 4.3 非 dialogue 類資料（物品說明、立繪/圖片 metadata）（**重大缺口**）

**user 原話：** 「物品說明，那就是物品名、物品說明、物品圖片等」

**既有設計現況：**
- SPEC §5.1 7 種實體類型：W-rules / W-language / V / C-* / R-*-* / P / CH-* / S-*-* — 全部圍繞「敘事 / 台詞 Bible」
- 沒有「物品 / 道具」「立繪 / 圖片資產」「UI 文案」等遊戲性實體
- D-018 #6「特殊資料格式 Phase D 後另議」隱性涵蓋 — 但 user refresh 直接點出

**user 訊號解讀：** 整個專案 scope **超出「台詞 Bible」，往「遊戲文字資料庫」走** — 包含：
- 角色台詞（既有）
- 物品說明（新）
- 立繪 / 圖片 metadata（新，不存實檔但引用素材）
- 隱含：UI 文案、教學文案、技能說明、其他遊戲文字資料

**對 schema 的衝擊：**
- SPEC §5.1 邏輯實體類型需要擴充（D-018 #6 設計時保留「entity 類型保留新增空間」 — 本輪正式啟動此擴充）
- 候選新類型：
  - `I-<item_id>` — 物品 / 道具
  - `A-<asset_id>` — 美術資產引用（立繪、圖片、SE、配音檔等的 metadata，不存實檔）
  - `UI-<element_id>` — UI 文案（按鈕、教學、提示等）
- 每個新類型需要對應的目錄結構、創建協議、模板、frontmatter 欄位
- 與既有 C-* 的關聯（C-主角A 的立繪 → A-portrait-主角A-default / A-portrait-主角A-angry 等）

**對 skill 與 protocol 的衝擊：**
- 可能需要新 skill（`/create-item` / `/create-asset` / `/view-item` 等）
- 可能需要新協議（00_m 物品創建協議 / 00_n 資產 metadata 協議）
- 或者抽出共通的「自訂類型擴充」機制，讓 user 在 Instance bootstrap 時定義自己的類型

**處理建議：** 新增 P-018「非 dialogue 類資料的 entity 類型擴充」；此為**最大 scope 擴充**，跟 user 進一步釐清「本輪要做哪些類型」與「哪些先標 reserved 等之後再做」。

## 4.4 手稿導入路徑（次要缺口）

**user 訊號：** A 優先度低的理由「可以使用網頁版的 GPT 或 CLAUDE 處理，但因為沒辦法直接讀取專案資料所以會有上下文導入、繼承等問題」 — 暗示 user 會在外部產出世界觀/人設/大綱手稿，再導入本工具。

**既有設計現況：**
- `/create-*` 5 階段對話：診斷 → 探索 → 收斂 → 寫檔 → 驗證 — 假設「使用者從空白開始」
- 沒有 `/import-*` skill 或「貼長篇手稿 → 自動拆解 + 補 frontmatter」的快速路徑
- Phase A.4 frontmatter 補完只處理「既有 27 份 template 檔」，不處理使用者新貼入的手稿

**Gap：** 既有 `/create-*` 階段 4「自動拆分」邏輯 + 既有的 frontmatter 補完邏輯 — 兩者組合**已能支援手稿導入**，只是沒抽出成獨立 skill。

**處理建議：** 新增 P-019「手稿導入快速路徑」 — 由上下游 specialist 第二輪評估是抽出 `/import-world` / `/import-character` / `/import-outline` 三個新 skill，或在 `/create-*` 加 `--from-draft <path>` 參數重用階段 4。

## 4.5 視覺化管理具體呈現（已知缺口，但需求 refresh 加重）

**現況：** UX_SPEC §2 / §3 / §4 / §5 / §6 全部「Batch 補完」未交付 — 已知阻塞。

**需求 refresh 加重：** D 是四大關鍵情境之一；user 對視覺化管理「我能看到目前設計到哪、下一步該做什麼」的需求很實際。

**處理建議：** 已在 §3.2 涵蓋（UX §2–§6 升優先級、可與其他 specialist 並行）。

---

# 5. 需求衝突點（需 user 拍板）

## 5.1 客製化輸出格式 vs D-018 #6 / D-003

**衝突：** D-018 / D-003 將「特殊資料格式」議題 promote / 拍板為「Phase D 後另議」、「schema 不額外擴充，僅留 unknown 欄位 WARN 不 ERROR 的彈性」。但需求 refresh §1 C-2 與 user 追問答案明示**本輪即需設計客製化輸出機制**。

**裁決選項：**
- (a) **partial supersede D-018 #6 / D-003** — 客製化輸出機制本輪設計、實作排序留待後續評估
- (b) 維持 D-018 #6 / D-003，本輪僅做「最小可行版」（如只支援「角色台詞 + 立繪 + KEY」一種 template，物品說明等留 Phase E）
- (c) 本輪完全不做，等 Phase D 後再說（但 user 已說 C-2 是核心需求 — 此選項可能不符 user 意圖）

**master 暫定方向：** (a) — partial supersede，理由：user 明示為核心需求；既有設計的「不採」是基於「當時無實際需求」前提，前提已變。

**user 需拍板。**

## 5.2 i18n KEY vs D-018 #2

**衝突：** D-018 #2「多語言對白：最終不採用，schema 不擴充」。但 user 明示「每段台詞還要有 KEY 來處理多語言」 — 需要 schema 微擴充。

**澄清：** 兩者其實是不同議題（見 §4.2）。

**裁決選項：**
- (a) **partial supersede D-018 #2** — 區分「不存多語本文」（維持原裁決）與「提供 i18n KEY」（新增支援）；schema 新增 KEY 欄位
- (b) 維持 D-018 #2 不動，i18n KEY 由外部系統（如手動建立 mapping table）處理 — 但 user 在 refresh 明示為核心需求

**master 暫定方向：** (a) — partial supersede 的「分項區分」處理；資料格式 specialist 第二輪設計具體 schema 微擴充。

**user 需拍板。**

## 5.3 新 entity 類型擴充 vs SPEC §5.1 LOCKED

**衝突：** SPEC §5.1 邏輯實體類型 7 種被列為「4 輪 CODEX 審查通過、LOCKED 不擅動」（DECISIONS_LOG §5.6）。但需求 refresh 揭露 user 需要「物品 / 立繪 / 其他遊戲文字資料」 — 需要新 entity 類型。

**裁決選項：**
- (a) **正式增列 entity 類型**（如 I-* item / A-* asset / UI-* element） — 動 SPEC §5.1 LOCKED 段
- (b) 用 D-018 #6 預留的「unknown user-defined 欄位 WARN 不 ERROR」彈性，讓 user 在 Instance bootstrap 時自訂類型 — 不動 SPEC，但 master / parser 需新增「自訂類型註冊機制」
- (c) 本輪僅納入最迫切的（如 I-* item），其他 reserve

**master 暫定方向：** (c) — 漸進式擴充，本輪僅新增 user 已具體點名的類型（物品、立繪）；其他類型等下次 refresh 再評估。SPEC §5.1 LOCKED 需 partial supersede（標明擴充由 master 在新 D-NNN 中明示）。

**user 需拍板，且需釐清本輪要納入哪些類型**（見 REVISED_WORK_ITEMS §3 user 直接拍板項）。

## 5.4 HTML 路徑 vs UX_SPEC §1.4

**衝突：** UX_SPEC §1.4「prototype §2 列舉的所有 GUI 元件、UI 系統、工程結構整體已廢棄」。user 在 Q3 答「之前用 HTML 做過原型」+ Q1 追問答「可以先詳細討論可行性在決定使用哪個方案會比較好」。

**裁決選項：**（已在追問 Q1 列出）
- (a) 恢復 HTML 呈現，superseded UX_SPEC §1.4
- (b) 維持純 Markdown
- (c) 兩條都預留，現在先不拍板

**user 已拍板：(c)** — 列為新 P-NNN，UX specialist 第二輪先補完 Markdown 路徑（不逾 A.0 暫停線），HTML 路徑等視覺化實際跳起來再判斷。

**處理：** 標 P-020 跟蹤。

## 5.5 A 優先級降低 vs Phase A → B → C → D 嚴格依賴

**衝突：** 既有 TASKS Phase 序按依賴排定，A 不可單獨延後而不影響 B/C/D。

**澄清：** A 降低的是「**user 跟 AGENT 對話整理**」（即 `/create-*` 5 階段對話的實際使用），不是「上游協議檔的存在」。如果有「手稿導入路徑」（§4.4），user 可以繞過 `/create-*` 對話、直接讓工具消費已寫好的世界觀/人設/大綱，B/C/D 依然成立。

**裁決選項：**
- (a) 不動 TASKS Phase 序；新增「Phase 0.5 手稿導入」作為 A 的繞行路徑
- (b) 動 TASKS Phase 序，把 A 降到最後（但會破壞依賴）
- (c) 把 A 跟 D 並行做（既有設計已允許 Phase 間「微跳」 — Q17=B）

**master 暫定方向：** (a) — 新增手稿導入路徑（P-019），Phase A 本身的 `/create-*` 對話路徑保留設計、實作可延後。

**user 需拍板。**

---

# 6. 結論：方向是否偏離

## 6.1 整體判定

**沒有方向偏離。** 需求 refresh 與既有設計核心架構（Markdown + Git + frontmatter + agent 對話 + 邏輯實體 + skill 系統）**完全相容**。偏離出現在「scope 邊界」 — user 真實需求比既有設計假設的「台詞 Bible」更廣：

| 維度 | 既有設計假設 | 需求 refresh 揭露的真實 scope |
|---|---|---|
| 工具用途 | 長篇遊戲劇本 + 台詞生產 | **遊戲文字資料庫 + 多格式輸出** |
| 資料類別 | 敘事相關（W/V/C/R/P/CH/S） | 敘事 + 物品 + 立繪 + 其他遊戲文字資料 |
| 輸出端 | chat 內呈現 + 08_b 固定 dialogue 模板 | **彈性 export template + i18n KEY + 多表現格式** |
| 上游入口 | 使用者跟 AGENT 對話從零建立 | **手稿導入 + 對話建立（兩條都要）** |
| 視覺化呈現 | 純 Markdown（HTML 廢棄） | **暫不拍板 — HTML 路徑保留可行性討論** |

## 6.2 既有設計的價值

- 核心架構（schema / 實體系統 / pipeline / QA / skill 模式）**全部不動且可直接消費**
- UPSTREAM §1–§6 substantive 內容（≈90% 已交付）**全部不浪費**
- UX_SPEC §0/§1/§7/§8 已建立的規則全部可用
- DECISIONS_LOG D-001~D-018 + P-001~P-015 全部脈絡清晰

## 6.3 需要新增的 scope（量化）

- **新增 entity 類型：** 2–3 個（I-* item / A-* asset / UI-* element 等，最終數量待 user 拍板）
- **新增 skill：** 估 3–6 個（手稿導入 3 個 + 客製化輸出 2–3 個）
- **新增協議：** 估 2–3 份（如 00_m 物品創建 / 00_n 輸出模板 / 00_o 資產引用）
- **新增 frontmatter 欄位：** 估 1–3 個（KEY 相關 + export template 對應）
- **新增 P / D 條目：** 5 條（P-016 / P-017 / P-018 / P-019 / P-020）

## 6.4 對 A.0 暫停的影響

- A.0 暫停**繼續維持**，不受需求 refresh 影響
- 但 A.0 解除條件更新：原本是「等 UX §2–§6 補完 + 上下游 §9 補完 + DATA_FORMAT 釐清」三項；新增「等 §4.1–§4.3 三項缺口的 specialist 第二輪設計完成」
- 詳見 REVISED_WORK_ITEMS

## 6.5 對 user 的核心訊息（最簡版）

1. **既有設計沒走偏** — 核心架構完全可用
2. **但 scope 變廣了** — 從「台詞 Bible」擴張到「遊戲文字資料庫 + 多格式輸出」
3. **本輪要新增 5 條 P/D 議題**（多輸出格式 / i18n KEY / 新 entity 類型 / 手稿導入 / HTML 路徑可行性）
4. **三個 specialist 第二輪工作量上升**（特別是資料格式跟上下游） — 但 UPSTREAM §1–§6 既有交付仍可繼承
5. **A.0 啟動仍要等**，但解除條件多了新需求對應的 specialist 設計

詳見 `REVISED_WORK_ITEMS.md`。

---

# 7. Bucket #1–#4 lock 後的狀態更新（v0.2）

本節由 v0.2 追加。Bucket #1-#4 user 拍板完成後，對 v0.1 §4 / §5 條目的狀態更新 + 額外揭露的缺口紀錄。詳細需求快照見 `REQUIREMENTS_LOCK.md` v1.0；詳細決策見 `DECISIONS_LOG.md` v0.6 §6.6。

## 7.1 §5 五項衝突的解決狀態

| 編號 | 衝突 | v0.1 狀態 | v0.2 解決 |
|---|---|---|---|
| H1 | 客製化輸出格式 vs D-018 #6 / D-003 | 暫定 (a) partial supersede | **RESOLVED via D-024** — scope 大幅縮減為 JSON+MD 雙吐 |
| H2 | i18n KEY vs D-018 #2 | 暫定 (a) partial supersede | **RESOLVED via D-022** — KEY 機制本輪設計 |
| H3 | 新 entity 類型 vs SPEC §5.1 LOCKED | 暫定 (c) 漸進式擴充 | **RESOLVED via D-023 + D-025** — A-\* 本輪實作 + 其他類別接口 |
| H4 | HTML 路徑 vs UX_SPEC §1.4 | user 已答 (c) 暫不拍板 | **RESOLVED via D-029 + D-030** — HTML web UI 拍板 + UX §1.4 partial supersede |
| H5 | A 優先級降低 vs Phase 依賴 | 暫定 (a) 新增手稿導入 | **RESOLVED via D-031** — 改用既有跳階段機制，不新增 import skill |

## 7.2 §4 五項缺口的處理狀態

| 編號 | 缺口 | v0.2 處理 |
|---|---|---|
| §4.1 | 多種「表現格式」客製化輸出機制 | **scope 大幅縮減**（v0.1 設想多套版 framework 砍掉）— 改為 JSON + MD 雙吐固定中介格式（D-024）；引擎特定轉檔工具外處理 |
| §4.2 | i18n KEY 機制 | **本輪設計，partial supersede D-018 #2**（D-022）；具體 schema 留資料格式 specialist（P-022） |
| §4.3 | 非 dialogue 類資料 | **本輪實作 A-\* + 其他類別接口**（D-023 / D-025）；I-\* / UI-\* / SKILL-\* reserved |
| §4.4 | 手稿導入路徑 | **不新增 skill，沿用既有跳階段機制**（D-031）+ markdown structure 要求（D-032）+ entity 命名衝突 4 選項（D-033） |
| §4.5 | 視覺化管理具體呈現 | **HTML web UI + 5 必要功能**（D-029）；UX_SPEC §1.4 partial supersede（D-030） |

## 7.3 Bucket 討論中額外揭露的新缺口（v0.1 未涵蓋）

下列訊號在 Bucket #1-#4 討論時揭露，v0.1 沒預期到，補入紀錄：

### G6：三層架構正式分離（Bucket #1 揭露）

v0.1 沒明確認知「**Layer 1 撰寫 / Layer 2 前端管理 / Layer 3 export** 三層分離」這個概念。需求 refresh + Bucket #1 討論才把這個結構顯化。處理：D-021 確立三層架構；SPEC §2 補入；ARCHITECTURE 增 §5「三層架構」副節（master 整合任務）。

### G7：可擴充機制設計哲學（Bucket #1 + #2 揭露）

v0.1 提了「新增 entity 類型」但沒提「**未來能擴充**」的設計哲學。Bucket #1 user「其他類別留接口」+ Bucket #2 user「後面可能還會迭代追加評測標準」兩個訊號合起來指向**可擴充 schema 機制**：

- entity 類型 registry（D-025）
- qa_type 變可擴充 enum（D-027）
- 未來機制（如 mode_tag 是否變可擴充）保留討論空間

處理：資料格式 specialist 第二輪設計 registry schema；A.0 parser 驗證邏輯需改。

### G8：QA 維度擴充（Bucket #2 揭露）

v0.1 沒提「09_g/h/i 新增」。Bucket #2 user 拍板加 3 份：

- 09_g 節奏感（句長變化 / 段落呼吸感）
- 09_h 對話張力（攻防力度）
- 09_i 跨場一致性（partial supersede D-018 #3 continuity_check）

處理：D-026 / D-027；UPSTREAM §3 補三節（上下游 specialist 第二輪）。

### G9：/dialogue-write SINGLE_ITER 模式（Bucket #2 揭露）

v0.1 沒提「user 習慣的單版本迭代寫法」。Bucket #2 user 拍板加 SINGLE_ITER：

- 既有試寫 / 破格 / 收斂 3 模式維持
- 加第 4 模式 SINGLE_ITER — agent 寫一版 → user 迴圈改

處理：D-028（partial supersede P-010 「不新增 /iterate-dialogue」改為加參數）；mode_tag enum 增 SINGLE_ITER；UPSTREAM §4 補 algorithm。

### G10：前端工具跟既有設計的整合方式（Bucket #3 揭露）

v0.1 沒設想前端工具會：
- 用本地 web server（不是純 HTML / 不是桌面 app）
- 跟 agent 完全分離（不內嵌 chat）
- 手動 Save（不是 auto-save）

這三條決定影響：
- 前端工具的實作 scope（含 server 端 API）
- 跟既有 Markdown source 的 sync 方式
- git workflow 跟前端的銜接

處理：D-029 鎖定三條；UX specialist 第二輪設計 + 上下游 specialist 評估 server API。

### G11：A 路徑前端入口的「複製指令」設計（Bucket #4 揭露）

v0.1 沒設想「前端工具提供哪個 entry point 引導 user 跑 A 對話」。Bucket #4 拍板「複製指令按鈕」 — 點按鈕複製 `/create-world` 指令 + context 到剪貼簿，user 切外部 chat 貼上跑。

處理：D-034；UX specialist 設計 context 內容（P-029 部分）。

## 7.4 v0.2 對「方向是否偏離」的最終判定

**v0.1 §6 結論：「沒有方向偏離，scope 變廣了」** — 本輪確認此判定**仍然成立**。

但 v0.2 補充：

- **核心架構（Markdown + Git + frontmatter + agent 對話 + 邏輯實體 + skill 系統）100% 可用** — 不變
- **scope 擴張的真實量化（v0.1 後修正）：**
  - 新增 entity 類型：**1 個本輪實作**（A-\*）+ 多個接口預留（v0.1 估 2-3 個本輪）
  - 新增 skill：**0 個**（v0.1 估 3-6 個；Bucket 拍板「不新增 skill」）
  - 新增協議：**0-1 個**（00_p 可擴充 QA 協議；v0.1 估 2-3 個）
  - 新增 QA 模板：**3 份**（09_g/h/i；v0.1 沒提）
  - 新增 frontmatter 欄位：**3-5 個**（KEY 相關 + A-\* metadata + import_source 等；v0.1 估 1-3 個）
  - 新增 P / D 條目：**14 D + 10 P**（v0.1 估 5 條 P；本輪實際 14 D 19 P）
  - **前端工具：v0.1 沒設想，現為新增大塊任務**

- **scope 收斂的部分（v0.1 預想但 Bucket 砍掉）：**
  - 多套版 framework → 縮減為 JSON+MD 雙吐
  - `/import-*` 3 新 skill → 改用既有跳階段機制
  - 多 entity 類型一次全做 → 漸進式（本輪只做 A-\*）

→ **整體 scope 比 v0.1 預估的稍小**（沒新 skill、entity 漸進），**但揭露了前端工具的大塊新需求**（v0.1 完全沒設想）。

## 7.5 對 A.0 暫停的更新

v0.1 §6.4 列「A.0 解除條件更新：4 項」。v0.2 確認**繼續暫停**，解除條件對齊 REQUIREMENTS_LOCK §9.2 / REVISED_WORK_ITEMS v0.2 的階段 1A/1B/1C 並行完成。

詳細見 `PHASE_3_COMPLETION_REPORT.md` v4.0。

---

# 8. 文件維護紀律

- 本檔是「需求 refresh vs 既有設計」的對照分析，不是新需求文件
- 新需求由 `REQUIREMENTS_REFRESH`（user 提供）+ Bucket #1-#4 拍板紀錄共同授權
- 任何 §5 衝突的裁決必須由 user 明示，記入 DECISIONS_LOG D-NNN
- 任何 §4 新缺口的具體設計由對應 specialist 第二輪交付，記入 REVISED_WORK_ITEMS
- §7 v0.2 追加：Bucket lock 後狀態更新；後續 specialist 交付後若有新缺口，繼續寫 §8.x 或升 v0.3
- 本檔升 REVIEW 條件：specialist 第二輪交付後對齊本檔結論無重大偏差
- 本檔升 FINAL 條件：master 第四輪整合完成、主 SPEC/ARCHITECTURE/TASKS 已更新
