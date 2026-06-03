狀態：DRAFT
版本：v0.1
最後更新：2026-05-19
適用範圍：CODEX 第 (d) 階段短審查 — master 第四輪 partial supersede 完成後、升 LOCKED 前 cross-spec final-check
優先級：最高

# CODEX_REVIEW_REPORT_D — 第 (d) 階段短審查報告

## 0. 摘要

**結論：本輪不建議直接升 LOCKED。** INTEGRATION_CONTRACTS v2.0 主體方向已收斂，但仍有多個會誤導 Phase A.0 / A.0F / D.4 實作的 P0/P1 級落地殘留，必須先修補後再進第七階段升 LOCKED。

整體判斷：不是需求或 D-NNN 拍板需要重開，而是 partial supersede 尚未完全清掉舊文與跨文件欄位形狀。最高優先修補點是 A-* metadata 檔案形狀、D-043「8 份 QA 必跑」殘留 5 份舊文、P-027~P-030 Pending 錯配，以及 frontend adapter / L3 export / conflict modal 的 contract 對齊。

## 1. 審查範圍

### Files Read

使用者訊息稱「14 份文件」，但清單實際列出 13 個路徑。本輪只讀取清單中的 13 份，不自行補讀未列文件：

1. `_design/REQUIREMENTS_LOCK.md`
2. `_design/DECISIONS_LOG.md`
3. `_design/INTEGRATION_CONTRACTS.md`
4. `_design/SPEC.md`
5. `_design/ARCHITECTURE.md`
6. `_design/TASKS.md`
7. `_design/PHASE_3_COMPLETION_REPORT.md`
8. `_design/DATA_FORMAT_SPEC.md`
9. `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
10. `_design/UX_SPEC.md`
11. `_design/L3_EXPORT_PROMPT_SCHEMA.md`
12. `_design/CODEX_REVIEW_REPORT.md`
13. `_design/HANDOFF_TO_4TH_INTEGRATION_MASTER.md`

### Files NOT Modified

- 未修改任何既有 spec / SPEC / ARCHITECTURE / TASKS / INTEGRATION_CONTRACTS / LOCKED 或 FINAL 文件。
- 未修改 `00_protocol/`、`09_quality_assurance/`、`scripts/`、`.claude/skills/` 或其他實作檔。
- 本輪唯一新增輸出：`_design/CODEX_REVIEW_REPORT_D.md`。

## 2. 衝突清單

### CC-01 [P0] A-* metadata 檔案形狀在 Contract A/B/C、DF、UD、UX 之間仍不一致

**Line refs：**
- `_design/INTEGRATION_CONTRACTS.md:422`：Contract A.3 採 `10_art_assets/` subtype 目錄 + group metadata 檔。
- `_design/INTEGRATION_CONTRACTS.md:478`：A.3 說每份 `10_art_assets/<subtype>/<group>.md` 內有 `art_metadata` list。
- `_design/DATA_FORMAT_SPEC.md:1031`：DF §5.2 採 `portraits/主角A.md`、`sfx/ambient.md` 等 subtype/group 檔。
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md:6419`：UD §13.2.1 採每個 asset 一份 `10_art_assets/A-portrait-主角A-default.md`。
- `_design/INTEGRATION_CONTRACTS.md:1261`、`_design/INTEGRATION_CONTRACTS.md:1624`：Contract B.4 / C.5 又使用 `10_art_assets/<key>/metadata.md`。
- `_design/UX_SPEC.md:2605`、`_design/UX_SPEC.md:2609`：UX Asset Panel 同樣使用 `10_art_assets/<key>/metadata.md` / `10_art_assets/<key>/`。

**問題：** D-041 已確定 SoT 是 `10_art_assets/`，但「一個 A-* entity 對應一檔」、「subtype/group 檔內 list」、「key folder + metadata.md」三種檔案粒度同時存在。這會讓 A.0 parser、Asset Panel、UD lifecycle、缺檔偵測互相實作成不同模型。

**建議：** 由 master 選一個 canonical 檔案形狀。若採 DF/Contract A 的 subtype/group list，修 UD §13.2.1、UX §11.1.6a、Contract B.4/C.5；若採 UD per-asset `.md`，修 DF §5、SPEC §5.1a、ARCH §1.2、TASKS A.0.4 / A.5、Contract A.3/B.4/C.5。不要保留 `<key>/metadata.md` 第三種模型。

### CC-02 [P0] D-043「8 份 QA 必跑」未完整落地，仍殘留 5 份 QA 舊文

**Line refs：**
- `_design/SPEC.md:416`、`_design/SPEC.md:571`、`_design/SPEC.md:578`：§5.4 manifest / phase_log 說 QA 對應 5 份報告。
- `_design/SPEC.md:987`、`_design/SPEC.md:1015`、`_design/SPEC.md:1043`、`_design/SPEC.md:1178`、`_design/SPEC.md:1204`、`_design/SPEC.md:1570`：§12 仍多處寫 5 份。
- `_design/ARCHITECTURE.md:869`、`_design/ARCHITECTURE.md:875`、`_design/ARCHITECTURE.md:882`、`_design/ARCHITECTURE.md:886`、`_design/ARCHITECTURE.md:888`：ARCH §6.3 寫五份、`weight: 0.2`、qa_type 五種之一、`qa_report_paths 5 個`。
- `_design/TASKS.md:1571`、`_design/TASKS.md:1586`、`_design/TASKS.md:1594`、`_design/TASKS.md:1607`：TASKS D.4 寫五份、驗收恰好 5 份、禁止跳過 5 份。
- `_design/INTEGRATION_CONTRACTS.md:1297`、`_design/UPSTREAM_DOWNSTREAM_SPEC.md:1957`、`_design/SPEC.md:1128`：權威新口徑均為 8 份。

**問題：** 主 SPEC §12.7 已修成 8 份，但 §5.4、§12 其他段、ARCH §6.3、TASKS D.4 仍足以讓 Phase D 實作照 5 份寫。

**建議：** 全部改為 8 份 QA：09_a / 09_b / 09_c / 09_d / 09_f / 09_g / 09_h / 09_i。`qa_report_paths` 驗證 8 條；`qa_type` 改 8 種之一；若權重仍需總和 1.0，明定 8 份權重規則。

### CC-03 [P0] P-027~P-030 Pending 在 INTEGRATION_CONTRACTS §6.4 被錯配

**Line refs：**
- `_design/DECISIONS_LOG.md:980`：P-027 = `/dialogue-write SINGLE_ITER` algorithm。
- `_design/DECISIONS_LOG.md:983`：P-028 = 手稿導入細節。
- `_design/DECISIONS_LOG.md:986`：P-029 = 前端工具 UX 細節。
- `_design/DECISIONS_LOG.md:989`：P-030 = L3 export 觸發方式。
- `_design/INTEGRATION_CONTRACTS.md:1703`-`_design/INTEGRATION_CONTRACTS.md:1706`：§6.4 卻把 P-027~P-030 寫成 UX 細節 / canon delta / glossary / multi-medium future。

**問題：** 這不是單純描述不完整，而是 Pending ID 對到錯議題。若照 §6.4 分派，SINGLE_ITER algorithm、手稿導入、前端 UX、L3 export 會被錯送到不相干目的地。

**建議：** 以 DECISIONS_LOG §6.6.5 為基準重寫 §6.4。P-027 派 UD §4.7 / TASKS D.3；P-028 派 UD §10 + UX conflict flow；P-029 派 UX §11 + A.0F；P-030 標 RESOLVED via D-038 或只留 Phase B+ POST endpoint 後續。

### CC-04 [P1] `dialogue_keys` schema 被 UD 使用 `source_keys`，但 Contract A.1 / DF §4.2 / JSON mapping 沒有此欄位

**Line refs：**
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md:2382`、`_design/UPSTREAM_DOWNSTREAM_SPEC.md:2397`、`_design/UPSTREAM_DOWNSTREAM_SPEC.md:2416`、`_design/UPSTREAM_DOWNSTREAM_SPEC.md:4275`：UD 使用 `dialogue_keys.<KEY>.source_keys` 做收斂句級 lineage。
- `_design/INTEGRATION_CONTRACTS.md:128`-`_design/INTEGRATION_CONTRACTS.md:142`：Contract A.1 schema 無 `source_keys`。
- `_design/DATA_FORMAT_SPEC.md:705`-`_design/DATA_FORMAT_SPEC.md:717`：DF §4.2 欄位表無 `source_keys`。
- `_design/DATA_FORMAT_SPEC.md:2117`-`_design/DATA_FORMAT_SPEC.md:2118`：DF §9.5 JSON dialogue_line mapping 也無此欄位。

**問題：** 如果句級收斂 lineage 是必要 contract，parser / JSON export 目前不會保存；如果不是必要 contract，UD 會要求實作者寫出不存在欄位。

**建議：** 決定是否保留 `source_keys`。保留就加入 Contract A.1、DF §4.2、DF §9.5、A.0 parser；不保留就從 UD §2.11 / §4.8 移除，改只用檔案級 `source_dialogues`。

### CC-05 [P1] `base_dialogue` 位置衝突：Contract/SPEC 說 phase_log，UD 寫入 dialogue frontmatter

**Line refs：**
- `_design/INTEGRATION_CONTRACTS.md:706`-`_design/INTEGRATION_CONTRACTS.md:709`：A.6 明確說 SINGLE_ITER lineage 用 phase_log `base_dialogue`。
- `_design/SPEC.md:321`、`_design/SPEC.md:556`：SPEC 說 `source_dialogues` 不擴義，SINGLE_ITER 走 phase_log `base_dialogue`。
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md:4090`-`_design/UPSTREAM_DOWNSTREAM_SPEC.md:4099`：UD §4.7 step 5 把 `base_dialogue` 寫在 dialogue 檔 frontmatter。

**問題：** 這會讓 A.0 parser 實作對 `base_dialogue` 的讀取位置不一致，並可能擅自擴 SPEC §5.2.3 下游欄位表。

**建議：** UD §4.7 step 5 移除 frontmatter `base_dialogue`，只在 step 6 phase_log 寫 `base_dialogue / iteration_count / iteration_note`。若真的要 dialogue frontmatter 也存 lineage，必須同步升 Contract A.6 + DF + SPEC。

### CC-06 [P1] trust-level 邊界仍被 DF §3.3 寫成可跳 QA / 直接 final

**Line refs：**
- `_design/DATA_FORMAT_SPEC.md:361`：`agent_assisted` 寫「後續可跳 QA 直接 final」。
- `_design/DATA_FORMAT_SPEC.md:370`-`_design/DATA_FORMAT_SPEC.md:372`：DF 說 `agent_assisted` 可直接跳到 `DIALOGUE_FINAL`。
- `_design/INTEGRATION_CONTRACTS.md:895`-`_design/INTEGRATION_CONTRACTS.md:921`：Contract A.8 明確說 trust-level 只限上游 `/create-*`，不影響下游 pipeline，也不得跳 8 份 QA。
- `_design/SPEC.md:565`：SPEC §5.4a 同樣說 trust-level 不影響下游 pipeline_state。

**問題：** A.8 / SPEC / UD 已修正，但 DF schema owner 的文字仍保留舊語義，會讓 parser 或 import_source 驗證走錯方向。

**建議：** DF §3.3 改為「只記錄上游來源，不提供品質 gate 豁免」。刪除 `DIALOGUE_FINAL` / 跳 QA 說法。

### CC-07 [P1] L3 export read-only contract 與 `rerun_qa` / `phase_log` append / `include_deleted` flag 不一致

**Line refs：**
- `_design/L3_EXPORT_PROMPT_SCHEMA.md:57`：metadata schema 含 `rerun_qa`。
- `_design/L3_EXPORT_PROMPT_SCHEMA.md:92`-`_design/L3_EXPORT_PROMPT_SCHEMA.md:95`：read-only constraints 禁止改 source、禁止執行 `/qa`、禁止修改 phase_log。
- `_design/UX_SPEC.md:4098`-`_design/UX_SPEC.md:4099`：Export panel 顯示「重跑 QA」勾選。
- `_design/INTEGRATION_CONTRACTS.md:840`、`_design/DATA_FORMAT_SPEC.md:2199`：另一邊又說 export 跑完後 phase_log 補 `phase: export`。
- `_design/INTEGRATION_CONTRACTS.md:818`、`_design/UPSTREAM_DOWNSTREAM_SPEC.md:6231`：提到 prompt 可加 `include_deleted: true`，但 L3 prompt metadata schema 未定此欄。

**問題：** Export A1 本來是 read-only prompt 生成與外部 agent export；`rerun_qa` 和 phase_log append 會讓它變成 pipeline action。`include_deleted` 也缺欄位來源。

**建議：** 將「重跑 QA」移除或改為「include existing QA reports」。決定 export 是否可 append `phase_log`：若 read-only 到 phase_log 也不寫，刪 Contract/DF 的 append；若允許 export log，L3 §1.4 明確列唯一允許寫入。補上 `include_deleted: bool` 或刪除其他 spec 對此 flag 的引用。

### CC-08 [P1] Frontend adapter endpoint contract 未同步到 UX §11.8.3

**Line refs：**
- `_design/ARCHITECTURE.md:1294`-`_design/ARCHITECTURE.md:1305`：ARCH §13.2 定義 8 endpoint。
- `_design/TASKS.md:800`-`_design/TASKS.md:815`：TASKS A.0F.1 也列同 8 endpoint。
- `_design/INTEGRATION_CONTRACTS.md:1039`-`_design/INTEGRATION_CONTRACTS.md:1113`：Contract B.2 依賴 `header / save / save-as`。
- `_design/UX_SPEC.md:4484`-`_design/UX_SPEC.md:4493`：UX §11.8.3 仍是舊 endpoint 清單，缺 `GET /api/scene/<id>/header`、`POST /api/scene/<id>/save-as`、asset endpoints、scope-counts，且 `scene` / `scenes` path 命名不一致。

**問題：** A.0F 實作者若看 UX §11.8.3，會漏實作 Save race guard preflight、DRAFT proposal save-as、Asset Panel query、Export prompt scope counts。

**建議：** UX §11.8.3 直接鏡射 ARCH §13.2，或明確標「以 ARCH §13.2 為權威」並移除舊 endpoint 清單。

### CC-09 [P1] Contract B.8 的 entity 命名衝突 4 選項與 UX/TASKS 的 mtime conflict modal 混線

**Line refs：**
- `_design/INTEGRATION_CONTRACTS.md:1416`-`_design/INTEGRATION_CONTRACTS.md:1456`：B.8 要求 entity 命名衝突 4 選項 merge / overwrite / create-as-new / skip。
- `_design/UX_SPEC.md:4317`-`_design/UX_SPEC.md:4321`：UX §11.7.6 實際只處理 mtime drift，且是 reload / force overwrite 二選。
- `_design/TASKS.md:867`-`_design/TASKS.md:873`：A.0F.9 要 entity 命名衝突 4 選項。
- `_design/TASKS.md:875`-`_design/TASKS.md:879`：A.0F.10 又說 mtime conflict 提供 reload / keep / merge 三選項，與 UX 二選不一致。

**問題：** 目前「手稿導入 entity naming conflict」與「前端 save mtime drift conflict」被同名 Conflict Modal 混在一起。

**建議：** 將 UX mtime conflict 固定為 reload / force overwrite / cancel 或依 UX 原二選；另新增 `11.7.6a` 或獨立章節承接 Contract B.8 的 entity naming conflict 4-option modal。

### CC-10 [P2] KEY lifecycle 細欄位與 deprecated 行為仍有差異

**Line refs：**
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md:2471`-`_design/UPSTREAM_DOWNSTREAM_SPEC.md:2498`：UD 使用 `deprecated_at`、`sfx: null`，且 deprecated 句內文移除。
- `_design/DATA_FORMAT_SPEC.md:712`：DF §4.2 要 `sfx` 是 list / 空 list。
- `_design/DATA_FORMAT_SPEC.md:843`：DF §4.5 的 deprecated 語義與 UD 移除內文策略不同。
- `_design/INTEGRATION_CONTRACTS.md:1538`-`_design/INTEGRATION_CONTRACTS.md:1540`：Contract C.2 只映射 `deprecated_reason` / `deleted_at`，沒有 `deprecated_at`。

**問題：** 這不一定阻塞主 contract，但會影響 KEY UI、parser lifecycle 驗證與 export JSON。

**建議：** 決定是否需要 `deprecated_at`。若保留，補進 Contract A.1/C.2、DF §4.2/§9.5；若不保留，UD 刪除。`sfx` 統一為空 list `[]` 或 nullable。

## 3. Partial supersede 落地缺漏清單

### PS-01 [必修] SPEC §5.4 / §12 的 D-043 殘留

SPEC §12.7 已正確寫 8 份，但 §5.4 manifest 與 §12 多處仍寫 5 份。代表 D-043 只在局部落地，未完成整章掃描。建議以 `09_a/b/c/d/f/g/h/i` 全量替換相關框架、state machine、cross-skill table、M9 審查摘要中的 5 份說法；若保留舊文，必須明確標「歷史原文，已 supersede」。

### PS-02 [必修] ARCH §6.3 與 TASKS D.4 未同步 D-043

ARCH §6.3 前半段已列 8 份，但寫檔/驗證/輸出段仍是 5 份；TASKS D.4 同樣前半段已列 8 份，驗收與禁止段回到 5 份。這是最可能直接污染實作的缺漏。

### PS-03 [建議修] TASKS A.5 phase_log status 還停在 P-012 暫定

SPEC §5.4 已說 `status` 經 D-042 formalize，但 TASKS A.5 範例缺 `status: completed`，且 `_design/TASKS.md:613` 仍寫「P-012 暫定 / 待資料格式 specialist 第二輪正式確認」。建議改成「D-042 已 formalize，P-012 僅歷史標註」並補 bootstrap 範例欄位。

### PS-04 [建議修] TASKS A.0 啟動 gate 未承接 PHASE_3 §6.2a

PHASE_3 §6.2a 說 Phase A.0 還需第 6 階段短審 clean + 第 7 階段升 LOCKED，TASKS A.0 卻寫「依賴：無」。建議補一句：「實作依賴：無；啟動 gate：PHASE_3_COMPLETION_REPORT §6.2a 全部完成後才可執行。」

### PS-05 [建議修] A.0F / Phase B+ push mode 分期不清

L3 schema / SPEC / ARCH / UX 都說 Phase A.0 clipboard 必做，local LLM endpoint Phase B 後必做；但 TASKS A.0F.8 驗收要求 `local_llm_endpoint POST 成功`。建議 A.0F.8 只驗 clipboard，POST endpoint 移到 Phase B 後或 C.5a。

## 4. Pending 殘留分派檢查

### UD §9 Pending

不 clean。`_design/INTEGRATION_CONTRACTS.md:1657` 標「12 條」，但 `_design/INTEGRATION_CONTRACTS.md:1661`-`_design/INTEGRATION_CONTRACTS.md:1673` 實列 13 條；其中 `9.3.3`、`9.3.4` 處理欄為 `—`，沒有 owner / phase；`9.2.5` 仍派給「master 第四輪整合」，但本檔已是第四輪後 v2.0。

### UX §9 Pending

部分 clean。§6.3 有依 schema / query-API-adapter / upstream algorithm 三類總結 13 條 PENDING，方向正確；但以 grouped IDs 呈現，不足以讓每個 NS item 都有單一 owner + 時點。建議 §6.3 補「13 條逐項表」或明確說 grouped row 的每個 ID 共用同一 owner / phase。

### P-027~P-030

不 clean。§6.4 目前四條 Pending 與 DECISIONS_LOG §6.6.5 的 P-ID 不相符，見 CC-03。此項是升 LOCKED 前必修。

### §6.5 7 個目的地

目的地類型大致齊全，但有兩個問題：
- `_design/INTEGRATION_CONTRACTS.md:1713` 把 frontend server.py 8 endpoint + Asset Panel API 放進「Phase A.0 內部 task」，但 TASKS 已把 frontend 定義為獨立 Phase A.0F，且依賴 A.0 + Phase B。
- `_design/INTEGRATION_CONTRACTS.md:1712` 仍有「本輪 master 第四輪整合對話」目的地，對 v2.0 發布後狀態已過期。

建議拆成「Phase A.0 parser」與「Phase A.0F frontend adapter」，並把已過期的第四輪目的地改成「第五輪修補 / 升 LOCKED 前修補」或直接標 RESOLVED。

## 5. 給 master 第四輪整合的修補建議

### 必修

- 修 CC-01：A-* metadata 檔案形狀只保留一種 canonical，連動 DF / UD / UX / Contract A/B/C / SPEC / ARCH / TASKS。
- 修 CC-02：清掉 D-043 8 份 QA 的所有 5 份舊文，尤其 SPEC §5.4 / §12、ARCH §6.3、TASKS D.4。
- 修 CC-03：重寫 P-027~P-030 Pending 分派。
- 修 CC-04 / CC-05：決定 `source_keys` 是否入 schema；確保 `base_dialogue` 只在 phase_log 或同步升 schema。
- 修 CC-06：DF §3.3 刪除 trust-level 跳 QA / 直接 final 語義。
- 修 CC-08 / CC-09：frontend adapter endpoints 與兩種 conflict modal 分清。

### 建議修

- 修 CC-07：L3 export read-only、phase_log append、`rerun_qa`、`include_deleted` flag 一次對齊。
- 補 TASKS A.5 的 phase_log `status` formalized 口徑。
- 補 TASKS A.0 啟動 gate，避免升 LOCKED 前被誤讀為可直接開工。
- 修 A.0 / A.0F 分派混線。

### 可延後

- CC-10 KEY lifecycle 細節可作 v2.1 修補，但若 A.0 parser 馬上要寫 lifecycle 驗證，建議一併修。
- SPEC §5.1「7 邏輯類別 / 8 ID pattern / A-* 後 core concrete patterns」措辭可作低風險清理。

## 6. 升 LOCKED 條件評估

對 PHASE_3 §6.2a 四項：

| # | 條件 | 本輪評估 |
|---|---|---|
| 1 | 三 spec v0.3 + 主 SPEC v1.1 + ARCH v1.2 + TASKS v1.3 + INTEGRATION_CONTRACTS v2.0 全標 LOCKED | **未達成**。目前仍 REVIEW / DRAFT，且本報告列 P0/P1 修補項。 |
| 2 | DECISIONS_LOG 升 v1.0 | **未達成**。目前讀到 v0.8。 |
| 3 | Phase A.0.1 frontmatter parser 任務描述定稿 | **部分達成但不宜啟動**。A.0.1 本身很完整，但 A-* 檔案形狀、`source_keys`、trust-level、QA 8 份殘留會影響 parser 邊界。 |
| 4 | CODEX (d) 短審查 clean | **未達成**。本輪 finding 不 clean，需至少修必修項後重跑短回歸審查。 |

**Go / No-Go：NO-GO。** 不建議升 LOCKED；建議先做一輪「第五輪小修補 / pre-LOCKED patch」，再讓 CODEX 做 targeted recheck。

## 7. 後續審查建議

修補後不需要重審整個 v0.3 patch。建議做一輪小型 targeted recheck，範圍只限：

1. A-* metadata canonical 形狀：Contract A.3 / B.4 / C.1 / C.5 + DF §5 + UD §13.2.1 + UX §11.1.6a。
2. QA 8 份：SPEC §5.4 + §12、ARCH §6.3、TASKS D.4、UD §2.5 / appendix。
3. Pending §6：UD 12/13 count、UX 13 grouped owner、P-027~P-030 mapping、A.0 vs A.0F destination。
4. L3 export read-only：L3 schema、SPEC §13a、ARCH §4.2a、TASKS A.0F.8 / C.5a、UX §11.6.11。
5. Frontend adapter + conflict modal：ARCH §13、TASKS A.0F、UX §11.7.6 / §11.8.3、Contract B.2 / B.8。

通過上述 targeted recheck 後，才建議進 PHASE_3 §6.2a 的第 7 階段升 LOCKED。
