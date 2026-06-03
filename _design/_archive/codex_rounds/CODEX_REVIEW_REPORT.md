狀態：DRAFT
版本：v0.1
最後更新：2026-05-19
適用範圍：CODEX 第 (c) 階段深度審查報告 — 三 specialist v0.x + master 基線跨 spec 一致性
優先級：最高

# CODEX_REVIEW_REPORT

## 0. 摘要

本輪審查讀取啟動包、三份 specialist spec、REQUIREMENTS_LOCK、SPEC / ARCHITECTURE / TASKS / DECISIONS_LOG 基線，重點檢查 DF / UD / UX 之間的真實介面、LOCKED 基線 partial supersede 是否越界、REQUIREMENTS_LOCK §7 的 13 項衝擊是否完整 cover、以及 `[UX]` / `[NEEDS_SCHEMA_SUPPORT]` / `TBD-*` 標記是否合理。

結論：三份 spec 已 cover 大部分需求方向，但尚不能直接交給 master 第四輪整合為 v1。主要問題集中在 Contract A/B/C 的資料形狀未對齊，尤其 `dialogue_keys`、A-* source of truth、L3 export JSON / 觸發模型、UX marker 覆蓋、phase_log 擴充欄位與 LOCKED 編輯守門。建議 master 第四輪先處理 8 個 P0/P1 裁決，再做 SPEC / ARCHITECTURE / TASKS 整合。

## 1. 審查範圍

### 1.1 Files Read

- `_design/CODEX_REVIEW_STARTER.md`
- `_design/REQUIREMENTS_LOCK.md`
- `_design/MASTER_PLAN.md`
- `_design/INTEGRATION_CONTRACTS.md`
- `_design/DATA_FORMAT_SPEC.md`
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
- `_design/UX_SPEC.md`
- `_design/SPEC.md`
- `_design/ARCHITECTURE.md`
- `_design/TASKS.md`
- `_design/DECISIONS_LOG.md`

### 1.2 Files Not Modified

- 三份 specialist spec 未改。
- SPEC / ARCHITECTURE / TASKS / DECISIONS_LOG 未改。
- `00_protocol/`、`archive/`、任何 LOCKED 文件未改。

### 1.3 Report Output

- 本報告新建：`_design/CODEX_REVIEW_REPORT.md`

## 2. 衝突清單

### C-01 `dialogue_keys` canonical schema 形狀互斥

- 嚴重度：critical
- 涉及檔：`DATA_FORMAT_SPEC.md:482-503`, `UPSTREAM_DOWNSTREAM_SPEC.md:2347-2356`, `UPSTREAM_DOWNSTREAM_SPEC.md:5625`, `UPSTREAM_DOWNSTREAM_SPEC.md:6503`
- 問題：DF 將 `dialogue_keys` 定為 list of objects，每筆含 `key / line_index / speaker / aliases / created_at`；UD 消費端則用 `dialogue_keys.<KEY>.*` mapping，並把 `source_keys`、portrait / bgm / sfx 等句級資料掛在同一 mapping 下。
- 影響：parser、`/dialogue-write`、前端 details pane、JSON export、i18n alias lookup 會解析不同資料形狀。
- 建議：master 先拍板一個 canonical 形狀。若重視 grep / stable object key，採 mapping；若重視順序與 array validation，採 list，但 UD / UX 全部改成 list query。

### C-02 A-* 逐句引用 source of truth 未對齊

- 嚴重度：critical
- 涉及檔：`DATA_FORMAT_SPEC.md:828-846`, `DATA_FORMAT_SPEC.md:1716-1722`, `UPSTREAM_DOWNSTREAM_SPEC.md:6538-6554`, `UPSTREAM_DOWNSTREAM_SPEC.md:6556-6617`
- 問題：DF 允許 A-* 逐句引用由內文中文 prefix / HTML comment / frontmatter 任一來源處理，甚至可從 `depends_on` 推斷；UD 則把 `dialogue_keys.<KEY>.portrait/bgm/sfx` 視為 single source of truth，內文 art comment 只是 view layer。
- 影響：同一句台詞的立繪、BGM、SFX 可能在 parser、editor、export 中出現不同結果。
- 建議：master 明確定義「句級 A-* 引用權威來源」。建議以 frontmatter `dialogue_keys` 結構為權威，內文 comment 只做可讀提示，且 parser 驗證一致。

### C-03 L3 export 觸發模型互斥

- 嚴重度：critical
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:4986-4997`, `UPSTREAM_DOWNSTREAM_SPEC.md:5934-5949`, `UX_SPEC.md:1989-1998`, `UX_SPEC.md:3408-3424`, `REQUIREMENTS_LOCK.md:237-248`
- 問題：UD 設計前端按鈕由本地 server 直接 call CLI；UX 依 D-029 α 完全分離，拒絕前端直接跑 server-side CLI，主張複製指令到外部 chat / agent。
- 影響：前端 server API、使用者工作流、export implementation owner 完全不同，無法同時實作。
- 建議：master 必須先裁決「前端工具是否允許執行非 agent 的本地 CLI」。若完全分離包括所有寫檔/CLI，採 UX；若完全分離只禁止 agent action、允許 local tool action，採 UD 並修 D-029 解釋。

### C-04 L3 JSON contract 形狀不一致

- 嚴重度：critical
- 涉及檔：`DATA_FORMAT_SPEC.md:1572-1598`, `DATA_FORMAT_SPEC.md:1633-1647`, `UPSTREAM_DOWNSTREAM_SPEC.md:6010-6103`
- 問題：DF 正式 schema 是 `manifest + records[]`，record_type 分 `entity / dialogue_line / art_metadata`；UD 接點需求是 top-level `export_metadata / entities / assets / dialogues / qa_reports / phase_log` 六區。
- 影響：exporter、前端 API、外部轉檔工具會對不上同一 JSON schema；DF 將 P-024 標 resolved 過早。
- 建議：master 裁決採 normalized records 還是 consumer-friendly top-level map。若採 DF records，UD 的六區只能是 derived adapter view；若採 UD 六區，DF §9 必須重寫。

### C-05 A-* registry / metadata source of truth 衝突

- 嚴重度：critical
- 涉及檔：`DATA_FORMAT_SPEC.md:702-740`, `DATA_FORMAT_SPEC.md:1071-1185`, `UPSTREAM_DOWNSTREAM_SPEC.md:6273-6280`, `UPSTREAM_DOWNSTREAM_SPEC.md:6714-6718`
- 問題：DF 採 `10_art_assets/` index + individual metadata files，並另有 entity type registry；UD 仍以 `_assets/00_assets_registry.md` 或 `_assets/registry.yaml` 作為 A-* registry 驗證來源。
- 影響：A.0 parser、A-* lifecycle、前端 dropdown、export 會不知道從哪裡讀資產 metadata。
- 建議：master 選定唯一權威。可採 `10_art_assets/` 作 source of truth，若需要 `_assets/registry.yaml`，只能作 generated cache 或廢除。

### C-06 UX marker 覆蓋缺口：UD 有 UX-1..UX-80，UX 只覆蓋 UX-1..UX-53

- 嚴重度：major
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:317-319`, `UPSTREAM_DOWNSTREAM_SPEC.md:4062-4064`, `UPSTREAM_DOWNSTREAM_SPEC.md:5499-5503`, `UPSTREAM_DOWNSTREAM_SPEC.md:5791-5793`, `UPSTREAM_DOWNSTREAM_SPEC.md:6228-6231`, `UPSTREAM_DOWNSTREAM_SPEC.md:6704-6708`, `UX_SPEC.md:1577-1710`
- 問題：UD §7 舊彙整只收 53 個 `[UX]`；UD §10-§13 又新增 UX-54~UX-80。UX_SPEC §7.8 仍宣稱對齊 53 個，未建立 UX-54~UX-80 覆蓋矩陣。
- 影響：手稿導入、SINGLE_ITER、KEY UI、cross-ref、export、A-* lifecycle 的 UX 接點無法被 master 系統核對。
- 建議：master 要求 UX 二修補「UX-54~UX-80 對應表」，並合併 UX-54/55 與 UX-64/65 重複項。

### C-07 phase_log schema 擴充未收斂

- 嚴重度：major
- 涉及檔：`DATA_FORMAT_SPEC.md:288-308`, `DATA_FORMAT_SPEC.md:327-345`, `UPSTREAM_DOWNSTREAM_SPEC.md:2447-2459`, `UPSTREAM_DOWNSTREAM_SPEC.md:5689-5699`
- 問題：DF formalize `status + import_source`；UD 正文又依賴 `entities_touched`、`iteration_count`、`iteration_note`、`base_dialogue`、`conflict_resolutions`，但 §9.1.4 正式提案只收 `status + import_source`。
- 影響：多場景 mutex、手稿導入衝突紀錄、SINGLE_ITER lineage、A.0 parser validation 都缺 canonical schema。
- 建議：master 將 P-012 拆成已決 `status/import_source` 與待決 `entities_touched/iteration/conflict fields`，指定 DF 或 UD 補一份 phase_log sub-schema。

### C-08 手稿導入 trust-level 是否影響下游狀態，UD 內部不一致

- 嚴重度：major
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:5222-5227`, `UPSTREAM_DOWNSTREAM_SPEC.md:5481-5484`, `DATA_FORMAT_SPEC.md:337-345`, `REQUIREMENTS_LOCK.md:204-211`
- 問題：UD §10.3 說 `agent_assisted` 可跳 QA 直接進 `DIALOGUE_FINAL`，但 §10.7.2 又說手稿導入只屬上游創建協議，下游 `/scene-task` / `/dialogue-write` / `/qa` 不適用；DF 也規定 `import_source != null` 只允許 `/create-*`。
- 影響：`agent_assisted` 的「跳 QA」到底是上游資料可信、下游台詞可 final，還是需求描述殘留，會影響 parser 與 gate。
- 建議：master 定義 trust-level 的作用層。建議先限制為上游 `/create-*` 導入 context，不得直接將台詞 pipeline 推到 `DIALOGUE_FINAL`。

### C-09 SINGLE_ITER 使用 `source_dialogues` 與 SPEC 鎖定語義衝突

- 嚴重度：major
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:3955-3960`, `SPEC.md:235-238`, `UX_SPEC.md:2000-2010`
- 問題：SPEC 鎖定 `source_dialogues` 僅 `--converge` 產出的 v02 使用；UD 將 SINGLE_ITER base path 寫入 `source_dialogues`。
- 影響：前端 Z1 混合並排、收斂 lineage、單版本迭代 lineage 會混用同一欄位語義。
- 建議：master 裁決 SINGLE_ITER 是否新設 `base_dialogue` / `iteration_parent`；不要重用 `source_dialogues` 除非 SPEC §5.2.3 明確擴義。

### C-10 KEY 刪除 / 棄用 lifecycle 不一致

- 嚴重度：major
- 涉及檔：`DATA_FORMAT_SPEC.md:515`, `DATA_FORMAT_SPEC.md:584-595`, `UPSTREAM_DOWNSTREAM_SPEC.md:2383-2388`
- 問題：DF 用 `deleted_at` 且 `key` 前綴 `[DELETED]`、內文移除；UD 用 `deprecated: true`、保留 `<!-- KEY: ... DEPRECATED -->` comment 並刪內容。
- 影響：KEY unique history、QA cross-scene 排除、export 是否輸出空句、前端顯示 DEPRECATED KEY 都會不同。
- 建議：master 統一 lifecycle 欄位。建議不要改變 `key` 值本身，改用 `status/deleted_at/deprecated_reason` metadata，避免破壞 alias lookup。

### C-11 QA 數量與 09_g/h/i 必要性未一致

- 嚴重度：major
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:1939-1974`, `UPSTREAM_DOWNSTREAM_SPEC.md:2439-2440`, `UPSTREAM_DOWNSTREAM_SPEC.md:3443-3448`, `UX_SPEC.md:1077-1088`, `REQUIREMENTS_LOCK.md:171-179`
- 問題：REQUIREMENTS_LOCK 與 UX 明確是 8 份 QA + 09_e final-gating；UD 主 pipeline §2.5 仍寫執行 5 份報告，且 09_g/h/i 在部分段落被寫成可選旗標。
- 影響：Phase D `/qa` 實作、QA report completeness、FINAL gate 會不一致。
- 建議：master 裁決 09_g/h/i 是否預設必跑。若本輪新增即進 pipeline，UD §2.5 / §9 / §7 舊「5 份」全部需修。

### C-12 UX 引入不存在或已否決的 skill 名稱

- 嚴重度：major
- 涉及檔：`UX_SPEC.md:582`, `UX_SPEC.md:2611`, `UX_SPEC.md:3565`, `UX_SPEC.md:3568`, `UPSTREAM_DOWNSTREAM_SPEC.md:4879-4889`, `SPEC.md:1084-1111`
- 問題：UX 使用 `/export-dialogue`，但 SPEC skill 清單只有 4 個 `/export-*`；UX 也多處使用 `/iterate-dialogue`，但 P-010 / D-028 已決定不新增該 skill，改 `/dialogue-write --single-iter`。
- 影響：違反 26 skill 清單不動，使用者複製指令會失效。
- 建議：UX 全文將 `/iterate-dialogue` 改為 `/dialogue-write --single-iter`；`/export-dialogue` 必須由 master 決定是新 skill、CLI wrapper，或改成既有 export / CLI。

### C-13 A-* subtype / owner 範圍不足

- 嚴重度：major
- 涉及檔：`DATA_FORMAT_SPEC.md:688`, `DATA_FORMAT_SPEC.md:799`, `UPSTREAM_DOWNSTREAM_SPEC.md:5552`, `UPSTREAM_DOWNSTREAM_SPEC.md:5566`
- 問題：DF 的 A-* subtype 主要是 portrait/bg/cg/icon/effect，metadata 偏 `character`；UD 需要 portrait/bg/cg/sfx/bgm/voice/ui，owner 可為 `C-*` / `S-*` / `CH-*` / global。
- 影響：BGM / SFX / voice / UI 等 asset 在 UD / export 中已出現，但 DF schema 不保證容納。
- 建議：master 決定本輪 A-* scope 是否只含立繪與背景，或正式擴大到 UD 列出的音效 / BGM / UI。若擴大，DF §5 需補 subtype registry。

### C-14 A-* 完成度是否計入 `/status` 互相矛盾

- 嚴重度：major
- 涉及檔：`DATA_FORMAT_SPEC.md:858-867`, `DATA_FORMAT_SPEC.md:896-906`, `UPSTREAM_DOWNSTREAM_SPEC.md:2442`, `UPSTREAM_DOWNSTREAM_SPEC.md:6602-6606`
- 問題：DF 定義 A-* 完成度並放入 `/status` parser 影響；UD 說 A-* 預設不計入 entity 完成度。
- 影響：F1 dashboard、`/status` 完成度、A-* metadata 缺失是否阻塞主線會不同。
- 建議：master 裁決 A-* 是否納入全局完成度。建議先不納入 narrative readiness，只在 asset panel 顯示獨立 completeness。

### C-15 LOCKED 編輯守門可被 Save/force overwrite 繞過

- 嚴重度：critical
- 涉及檔：`UX_SPEC.md:3198-3208`, `UX_SPEC.md:3359-3363`, `UX_SPEC.md:3710-3712`, `UX_SPEC.md:3752-3764`, `SPEC.md:1176-1181`
- 問題：UX 將 LOCKED 守門設在進 Editor 前，Editor 內無 LOCKED 守門；若外部 agent / VS Code 在使用者編輯期間把檔案升 LOCKED，Save 衝突流程仍可能 force overwrite。
- 影響：前端可能覆寫最新 LOCKED 文件，違反 SPEC §16 與 repo AGENTS 規則。
- 建議：Save 前必須重新讀 source header；若最新 `狀態=LOCKED`，禁止 overwrite，只允許複製降級指令或另存 DRAFT proposal。

### C-16 LOCKED → DEPRECATED 降級引導擅自新增 frontmatter 欄位

- 嚴重度：major
- 涉及檔：`UX_SPEC.md:3253-3262`, `UX_SPEC.md:2041-2050`, `SPEC.md:223-242`, `DATA_FORMAT_SPEC.md:1879-1890`
- 問題：UX §11.5.3 指引使用者加入 `降級理由 / 降級日期 / 降級人` frontmatter 欄位；SPEC canonical schema 沒有這三欄，DF 也強調既有 frontmatter 零破壞。雖 UX §10.10 有列 master 裁決，但 §11 已寫成具體操作。
- 影響：前端引導會產生未經 DF / master 接受的新欄位。
- 建議：將這三欄改為 09_e / body log / phase_log proposal，或先標 `[NEEDS_SCHEMA_SUPPORT]`，不可作為操作步驟。

### C-17 `[NEEDS_SCHEMA_SUPPORT]` 混入 query/API/adapter 問題

- 嚴重度：major
- 涉及檔：`UX_SPEC.md:1840`, `UX_SPEC.md:1873`, `UX_SPEC.md:1883-1894`, `UX_SPEC.md:1907-1909`, `UX_SPEC.md:1915-1916`, `DATA_FORMAT_SPEC.md:1023-1040`
- 問題：UX §9 將 A-* manifest query API、版本 manifest query、跨場 query、edit-lock、search index、server API 等列為 schema support；這些多數應屬 parser service / frontend adapter / upstream algorithm，不是 DF schema 本身。
- 影響：DF owner 會被要求承擔不屬於 schema 的 runtime/API 設計；master 難以判斷哪些真要改 SPEC §5。
- 建議：UX §9 重分三欄：`schema`、`query/API/adapter`、`upstream algorithm`。只有 `schema` 交 DF。

## 3. 越界嫌疑清單

### O-01 DF 宣稱「無需 master 裁決」語氣過滿

- 嚴重度：major
- 涉及檔：`DATA_FORMAT_SPEC.md:2034-2036`, `DATA_FORMAT_SPEC.md:2049`, `DATA_FORMAT_SPEC.md:2062`
- 嫌疑：DF 本身多處 partial supersede SPEC §5.1 / §5.2.4，且與 UD / UX 有 Contract A/C 衝突，卻宣稱所有 DF-1~DF-11 無 master 裁決、P-021~P-024 全 resolved、P-025~P-030 schema 容納由本檔保證。
- 判斷：方向有 D-022~D-028 支撐，不算擅自推翻 LOCKED；但「resolved」與「無需 master」應降級為「資料格式初稿答案，待 Contract A/C 裁決」。

### O-02 UX 新增不存在 skill 名稱

- 嚴重度：major
- 涉及檔：`UX_SPEC.md:3565`, `UX_SPEC.md:3568`, `SPEC.md:1084-1111`, `UPSTREAM_DOWNSTREAM_SPEC.md:4879-4889`
- 嫌疑：`/export-dialogue` 與 `/iterate-dialogue` 都不在目前鎖定 skill 清單中，且 `/iterate-dialogue` 已由 D-028 明確改為不新增。
- 判斷：屬越界嫌疑。需改為既有 skill / CLI / copy text，或升 master 裁決新增 skill。

### O-03 UX 降級引導新增 frontmatter 欄位

- 嚴重度：major
- 涉及檔：`UX_SPEC.md:3253-3262`, `SPEC.md:223-242`
- 嫌疑：降級理由等欄位未經 DF / SPEC 接受即寫成操作步驟。
- 判斷：屬越界嫌疑。若需要這些欄位，應先成為 schema proposal。

### O-04 UD 將 `entities_touched` 當 P-012 同套 schema 擴充，但未列入正式提案

- 嚴重度：major
- 涉及檔：`UPSTREAM_DOWNSTREAM_SPEC.md:2499`, `UPSTREAM_DOWNSTREAM_SPEC.md:5689-5699`, `UPSTREAM_DOWNSTREAM_SPEC.md:4905-4918`
- 嫌疑：正文依賴新 phase_log 欄位，但需 master 裁決清單沒有完整收。
- 判斷：不是惡性越界，但 master 不能視為已決。

### O-05 UX 將 mode_tag 說成可擴充

- 嚴重度：minor
- 涉及檔：`UX_SPEC.md:3111-3114`, `DATA_FORMAT_SPEC.md:925-930`, `DATA_FORMAT_SPEC.md:950-956`
- 嫌疑：DF 僅把 mode_tag 5→6 加 SINGLE_ITER；可擴充 registry 是 qa_type，不是 mode_tag。
- 判斷：UX 用語需修正；若 mode_tag 也要可擴充，需 master 新裁決。

## 4. REQUIREMENTS_LOCK §7 十三項覆蓋檢查

| # | REQUIREMENTS_LOCK §7 項目 | 覆蓋狀態 | 審查結果 |
|---|---|---|---|
| 1 | SPEC §5.1 新增 A-* | partial | DF / UD 均 cover，但 registry、subtype、完成度未對齊 |
| 2 | qa_type 增 3 種變可擴充 | partial | DF / UX cover；UD 主 QA pipeline 仍殘留 5 份與可選語義 |
| 3 | mode_tag 增 SINGLE_ITER | partial | DF / UD cover；UD `source_dialogues` 用法與 SPEC 衝突，UX 誤稱 mode_tag 可擴充 |
| 4 | D-003 特殊資料格式提前設計 JSON+MD | partial | DF / UD / UX 均 cover，但觸發模型與 JSON shape critical conflict |
| 5 | D-018 #2 多語不採但加 KEY | partial | 已 cover KEY，但 `dialogue_keys` shape / deletion lifecycle 衝突 |
| 6 | D-018 #3 continuity 不採獨立實體但加 QA | partial | 已 cover 09_g/h/i，但必要性 / pipeline inclusion 未一致 |
| 7 | D-018 #6 特殊資料格式 Phase D 後另議改 export | partial | 同 #4 |
| 8 | P-010 不新增 `/iterate-dialogue`，改 single-iter | not clean | DF / UD 正確；UX 仍使用 `/iterate-dialogue` |
| 9 | UX_SPEC §1.4 HTML 廢棄 partial supersede | covered | UX §1.4 / §11 cover；需釐清 D-029 α 對 CLI 的範圍 |
| 10 | UX_SPEC §2-§6 scope 擴大 | partial | UX 補完 §2-§6；但 UD UX-54~80 未納入覆蓋矩陣 |
| 11 | P-016 套版機制 scope 縮小 | partial | 有 JSON+MD 固定雙吐方向；但 export skill vs CLI vs copy command 未決 |
| 12 | P-019 手稿導入路徑細化 | partial | 有 UD §10；但上游/下游 trust-level 作用不一致 |
| 13 | P-020 HTML 路徑 promoted | covered | UX §11 cover F1/F2/F3/F6/F7；但 LOCKED Save guard 需修 |

## 5. 標記合理性檢查

### 5.1 `[UX]`

- UD 全文出現 UX-1..UX-80 共 80 個編號。
- UX_SPEC 只覆蓋 UX-1..UX-53。
- 缺口：UX-54..UX-80 全部未進 UX §7 覆蓋矩陣。
- 重複：UX-54/55 與 UX-64/65 描述高度重疊。
- 建議：master 不應直接接受 UX §7「已對齊 53 個」作為 Contract B 完成證明；需補 UX-54~80 對照表。

### 5.2 `[NEEDS_SCHEMA_SUPPORT]`

- UX §9 彙整 NS-1..NS-33 共 33 項。
- 合理 schema 類：A-* ID / metadata、i18n KEY、qa_type registry、JSON mapping、`source_dialogues` 使用語義。
- 不宜歸 DF schema 類：query API、server API response shape、search index、edit-lock、mtime/content-hash、issue progress query。
- 建議：拆成 schema / query API / algorithm 三類後再分派 owner。

### 5.3 `TBD-*`

- UD 有 `[TBD-UX-CONFIRM]` 與 `[TBD-master-CONFIRM]`，主要集中於 export trigger、手稿導入衝突 UI、CLI 名稱 / git policy。
- 這些 TBD 大多合理，但需在 UD §9 與 UX §10 去重，避免同一問題被列成多個 master item。

## 6. 各 spec 需 master 裁決議題去重

### 6.1 DF

DF 宣稱無需 master 裁決，但實際需 master 裁決 / 整合前修正：

- `dialogue_keys` list vs map。
- A-* registry / metadata source of truth。
- JSON top-level schema。
- A-* subtype / owner scope。
- P-025~P-030 schema 支援宣稱降級。

### 6.2 UD

UD §9 議題多數合理，但需補收：

- `entities_touched` 是否進 P-012。
- SINGLE_ITER `source_dialogues` 用法。
- 09_g/h/i 是否預設必跑。
- UX-54~80 新增 marker 是否追加 Contract B。
- `dialogue_keys` / A-* / JSON shape 與 DF 衝突。

### 6.3 UX

UX §10 議題合理，但需去重 / 修正：

- L3 export 觸發與 UD §9.2.3 合併。
- LOCKED → DEPRECATED flow 與 UD P-013 / 09_e / schema 合併。
- `/iterate-dialogue` 不應列為設計選項，直接改 `/dialogue-write --single-iter`。
- UX-54~80 補表。
- NS-1~33 owner 拆分。

## 7. Master 第四輪整合建議優先序

### P0 — 先裁決，否則不能整合

1. `dialogue_keys` canonical shape：list vs map，並同步 KEY deletion / alias lifecycle。
2. A-* source of truth：`10_art_assets/` metadata files vs `_assets/registry`，以及句級 A-* 權威來源。
3. L3 export 權威：前端是否能 call CLI；export 是 skill、CLI、還是兩層 wrapper。
4. L3 JSON schema：DF `manifest + records[]` vs UD 六區 top-level。
5. LOCKED Save guard：前端 Save 前重讀最新 header，禁止覆寫最新 LOCKED。

### P1 — 第四輪整合時同步拍板

1. P-012 phase_log 擴充是否納入 `entities_touched`、iteration fields、conflict fields。
2. SINGLE_ITER lineage 欄位：是否新設 `base_dialogue` / `iteration_parent`，或擴義 `source_dialogues`。
3. 09_g/h/i 是否預設必跑，是否影響 FINAL gate。
4. A-* subtype / owner scope 是否包含 bgm/sfx/voice/ui。
5. A-* 是否納入 `/status` 完成度。
6. UX-54~80 是否追加進 UX_SPEC，重複編號如何合併。

### P2 — 可延後但需記錄

1. `/view/README.md` 自動 / 手動生成。
2. export output 是否進 git、`export/` 是否 ignore。
3. Canon delta threshold。
4. Glossary 13 術語具體文字。
5. multi-medium future scope。

## 8. 主 SPEC / ARCHITECTURE / TASKS 整合條目

完成 P0/P1 裁決後，master 第四輪應更新：

- SPEC §5.1：A-* entity 與 user-defined entity registry 的精確範圍。
- SPEC §5.2.3 / §5.2.4：`dialogue_keys`、`mode_tag=SINGLE_ITER`、`qa_type` 8 種 + registry。
- SPEC §5.4：phase_log sub-schema，包括 `status`、`import_source` 與是否採 `entities_touched` / iteration fields。
- SPEC §12：QA pipeline 5→8 的正式流程、09_e 非 QA 的 final-gating 位置。
- SPEC §13 / §14：L3 export 與既有 4 個 `/export-*` 的分工；是否新增 CLI 或 skill。
- SPEC §16：LOCKED → DEPRECATED 降級流程與前端守門限制。
- ARCHITECTURE：A.0 parser API / frontend adapter / export CLI/server handler 權責。
- TASKS：A.0 parser、A.5 init-project、C.5 export、D.4 QA、前端工具任務群的 sequencing。
- INTEGRATION_CONTRACTS v2：Contract A/B/C 真實介面改為本輪裁決後的形狀。

## 9. 後續審查建議

- master 第四輪整合前：先處理本報告 P0，不建議直接升 INTEGRATION_CONTRACTS v2。
- master 第四輪整合後：建議再做一次短審，範圍只看 Contract A/B/C 是否已收斂與 SPEC / ARCH / TASKS 是否一致。
- A.0 啟動前：需要 parser-readiness review，特別是 `dialogue_keys`、A-* registry、phase_log、JSON export 四項。

