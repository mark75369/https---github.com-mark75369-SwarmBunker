狀態：REVIEW
版本：v0.1
最後更新：2026-05-19
適用範圍：CODEX D2 targeted recheck Part 2（Recheck-02 ~ Recheck-09）
優先級：高

# CODEX_RECHECK_REPORT_D2_PART2 - Pre-LOCKED targeted recheck Part 2

## §0 摘要 + 整體 Go/No-Go

本報告只驗證 Recheck-02 ~ Recheck-09；Recheck-01 承接既有結論，視為已 PASS，本輪不重審。

整體結果：

| 項目 | 判定 |
|---|---|
| Recheck-01 | ✓ PASS（承接 Recheck-01；本輪未重審） |
| Recheck-02 | ✗ FAIL |
| Recheck-03 | ✓ PASS |
| Recheck-04 | ✓ PASS |
| Recheck-05 | ✓ PASS |
| Recheck-06 | ✓ PASS |
| Recheck-07 | ✓ PASS |
| Recheck-08 | ✓ PASS（target scope 內；§3 記一個非本輪對象殘留） |
| Recheck-09 | ✓ PASS |

**整體 Go/No-Go：NO-GO。**

原因：Recheck-02 是必修 targeted recheck，雖然 SPEC / ARCH / TASKS D.4 / Contract 主體多已改成 8 份 QA，但 UPSTREAM_DOWNSTREAM_SPEC 的狀態機、舊閱讀順序、跨 skill 表與 Appendix C 實作清單仍留有未標 supersede 的「5 份 QA」指令，足以誤導 Phase D `/qa` 實作。建議再一輪 patch 後重跑 Recheck-02；其餘項目可保留 PASS 結論。

## §1 審查範圍 + Files Read

### 1.1 Scope

- 本輪 scope：`_design/CODEX_RECHECK_STARTER_D2.md` §2.2 ~ §2.9 定義的 Recheck-02 ~ Recheck-09。
- 明確排除：不重審 Recheck-01；不重審 CODEX (c) / (d) 已 RESOLVED 項目；不寫實作檔；不提新需求。
- Repo 狀態：開始時 `git status --short -uall` 無輸出，工作樹乾淨。

### 1.2 Files Read

1. `_design/REQUIREMENTS_LOCK.md`
2. `_design/DECISIONS_LOG.md`
3. `_design/CODEX_REVIEW_REPORT_D.md`
4. `_design/CODEX_RECHECK_STARTER_D2.md`
5. `_design/INTEGRATION_CONTRACTS.md`
6. `_design/SPEC.md`
7. `_design/ARCHITECTURE.md`
8. `_design/TASKS.md`
9. `_design/DATA_FORMAT_SPEC.md`
10. `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
11. `_design/UX_SPEC.md`
12. `_design/L3_EXPORT_PROMPT_SCHEMA.md`

### 1.3 Files Modified

- 新增本報告：`_design/CODEX_RECHECK_REPORT_D2_PART2.md`
- 未修改任何審查對象或 LOCKED / protocol / archive 文件。

## §2 Recheck-02 ~ Recheck-09 逐項驗證

### Recheck-02：QA 8 份必跑落地（CC-02 + PS-01/02）

**判定：✗ FAIL**

已通過的部分：

- REQUIREMENTS_LOCK 的新基準為「8 份 QA 模板 + 1 份 final-gating」：`REQUIREMENTS_LOCK.md:163-179`。
- SPEC `qa_type` 已列 8 種，且標明 5 -> 8：`SPEC.md:341-345`。
- SPEC §5.4 manifest / phase_log 已用 8 份 QA：`SPEC.md:416`、`SPEC.md:475-485`。
- SPEC §12.7 已明確要求 `/qa` 必跑 8 份、8 份全 PASS 才 PASS、FINAL gate 需 8 QA + 09_e：`SPEC.md:1123-1149`。
- ARCH §6.3 已列 8 份、`weight: 0.125`、`qa_type` 8 種之一、`qa_report_paths 8 個`：`ARCHITECTURE.md:855-888`。
- ARCH §6.4 / §6.5 資料流已改成 8 份 QA：`ARCHITECTURE.md:898-914`。
- TASKS D.4 已要求 8 份全部必跑、8 份報告、8 種 `qa_type`、驗收恰好 8 份、禁止跳過 8 份：`TASKS.md:1579-1608`、`TASKS.md:1616-1629`。
- Contract B.5 已要求 UI 完整呈現 8 份、8 行總覽、8 份全 PASS：`INTEGRATION_CONTRACTS.md:1298-1339`。
- UD §2.5.3 主段已改成 8 份必跑：`UPSTREAM_DOWNSTREAM_SPEC.md:1957-1999`。
- UD Appendix A.6 已改為 8 份 QA 報告與 8 種 `qa_type`：`UPSTREAM_DOWNSTREAM_SPEC.md:7075-7099`。

失敗證據：

- SPEC §12.10 仍把下游展開來源寫成「5+1 QA 模板內容」與「6 份 QA 模板內容」，未標 D-043 supersede：`SPEC.md:1185-1193`。
- UD §2.8 禁止事項仍寫「不得跳過 5 份 QA 報告其中任一份」，未標 supersede：`UPSTREAM_DOWNSTREAM_SPEC.md:2112-2123`。
- UD §2.10.1 狀態機仍寫 `DIALOGUE_CONVERGED -> QA_PASSED / QA_FAILED` 條件為「5 份報告完整」：`UPSTREAM_DOWNSTREAM_SPEC.md:2206-2210`。
- UD §2.10.5 仍保留「五份 QA 報告閱讀順序」、並行跑 5 份、後面 4 份重看等舊執行邏輯：`UPSTREAM_DOWNSTREAM_SPEC.md:2288-2301`。
- UD §2.10.6 跨 skill 表仍寫 `/qa` 主要產出「5 份 QA 報告 .md」：`UPSTREAM_DOWNSTREAM_SPEC.md:2303-2309`。
- UD Appendix C.D.4 實作 checklist 仍要求「並行跑 5 份檢查」與只列 09_a/b/c/d/f，會直接污染 `/qa` 實作：`UPSTREAM_DOWNSTREAM_SPEC.md:7391-7405`。

結論：核心權威段有大幅修正，但「所有 5 份 / 五份 描述已改 8 份或標 supersede」未達成，且殘留位於狀態機與實作 checklist，故不是 minor 殘字。

### Recheck-03：Pending §6 校正（CC-03 + count）

**判定：✓ PASS**

證據：

- INTEGRATION_CONTRACTS §6.2 標「13 條」，且 13 列都有 Owner / Phase：`INTEGRATION_CONTRACTS.md:1661-1677`。
- DECISIONS_LOG §6.6.5 的真實 P-027~P-030 為 SINGLE_ITER / 手稿導入 / 前端工具 UX / L3 export：`DECISIONS_LOG.md:980-989`。
- INTEGRATION_CONTRACTS §6.4 依 DECISIONS_LOG §6.6.5 對齊 P-027~P-030，並列 resolved mapping：`INTEGRATION_CONTRACTS.md:1703-1723`。
- INTEGRATION_CONTRACTS §6.5 已拆 Phase A.0 parser 與 Phase A.0F frontend adapter，並把過期目的地改為第五輪 master：`INTEGRATION_CONTRACTS.md:1729-1741`。

備註：DECISIONS_LOG 舊摘要仍有 P-027~P-030 Pending 的歷史描述，但本 recheck 要求的是 INTEGRATION_CONTRACTS §6.4 對齊 DECISIONS_LOG §6.6.5；該目標已達成。

### Recheck-04：L3 export 純 read-only（CC-07）

**判定：✓ PASS**

證據：

- L3 prompt schema §1.2 明確移除 `rerun_qa`，並補 `include_deleted: false`：`L3_EXPORT_PROMPT_SCHEMA.md:57-61`。
- L3 prompt schema §1.4 明確禁止修改 source、禁止執行 `/qa`、禁止修改 phase_log / 寫入 phase_log entry，且定義 deleted dialogue_line 預設排除：`L3_EXPORT_PROMPT_SCHEMA.md:92-104`。
- SPEC §13a.5 明確 export 跑完後不寫 phase_log：`SPEC.md:1324-1325`。
- Contract A.7.6 與 DF §9.8 同步 phase_log 不 append：`INTEGRATION_CONTRACTS.md:841-842`、`DATA_FORMAT_SPEC.md:2218`。
- UX §11.6.11 已對齊 prompt panel，push mode 是 clipboard / POST prompt；不是 frontend 執行 export：`UX_SPEC.md:4178-4198`。
- ARCH §4.2a 說前端 server.py 只組 prompt、複製 / POST；不負責 export：`ARCHITECTURE.md:605-622`。
- TASKS A.0F.8 驗收含 `include_deleted` flag 並只把 clipboard 納入 Phase A.0 必做：`TASKS.md:873-881`。

### Recheck-05：Frontend adapter + conflict modal（CC-08 + CC-09）

**判定：✓ PASS**

證據：

- ARCH §13.2 定義 8 個 frontend adapter endpoint：`ARCHITECTURE.md:1294-1305`。
- UX §11.8.3 明確以 ARCH §13.2 為權威，列同一組 8 endpoint，並標舊 endpoint 不再列權威：`UX_SPEC.md:4541-4569`。
- UX §11.7.6 是 mtime drift modal，二選一為 reload / 強制覆寫，加取消；且只處理 non-LOCKED mtime drift：`UX_SPEC.md:4317-4356`。
- UX §11.7.6a 新增 entity naming conflict 4 選項，且明確跟 mtime drift 分拆：`UX_SPEC.md:4362-4412`。
- TASKS A.0F.9 專責 entity 命名衝突 4 選項：`TASKS.md:883-889`。
- TASKS A.0F.10 專責 mtime drift，明示 entity 命名衝突不在本 task：`TASKS.md:891-900`。

### Recheck-06：source_keys schema（CC-04）

**判定：✓ PASS**

證據：

- Contract A.1 schema 含 `source_keys`：`INTEGRATION_CONTRACTS.md:139-142`。
- DF §4.2 欄位表含 `source_keys`，說明為句級收斂 lineage：`DATA_FORMAT_SPEC.md:724-727`。
- DF §9.5 JSON `dialogue_line` record 含 `"source_keys"`：`DATA_FORMAT_SPEC.md:2118-2121`。
- TASKS A.0.2 parser validation 含 `source_keys` list/null 與 valid KEY 檢查：`TASKS.md:331-334`。

### Recheck-07：base_dialogue phase_log only（CC-05）

**判定：✓ PASS**

證據：

- UD §4.7 step 5 frontmatter 明確不寫 `base_dialogue`，並註明 lineage 走 phase_log：`UPSTREAM_DOWNSTREAM_SPEC.md:4089-4102`。
- UD §4.7 step 6 phase_log 維持 `base_dialogue`：`UPSTREAM_DOWNSTREAM_SPEC.md:4105-4116`。
- Contract A.6 將 `SINGLE_ITER` lineage 欄位定位在 phase_log `base_dialogue`，不重用 `source_dialogues`：`INTEGRATION_CONTRACTS.md:703-715`。
- SPEC §5.4a 定義 `base_dialogue` 是 phase_log 欄位，獨立於 SPEC §5.2.3 frontmatter `source_dialogues`：`SPEC.md:544-556`。
- DF §3.3d 定義 `base_dialogue`，並說明不重用 `source_dialogues`：`DATA_FORMAT_SPEC.md:423-442`。

### Recheck-08：trust-level 限上游（CC-06）

**判定：✓ PASS（target scope 內）**

證據：

- DF §3.3 import_source 表已改成「只記錄上游來源 / 不提供品質 gate 豁免」，規則中禁止下游升 `DIALOGUE_FINAL` 或跳過 8 份 QA：`DATA_FORMAT_SPEC.md:354-376`。
- DF §3.3 的「v0.2 -> v0.3 寫法變動」明確標舊寫法為 v0.2，並標 v0.3 新寫法為兩條路徑皆走標準 pipeline：`DATA_FORMAT_SPEC.md:378-381`。
- UD §10.3 明確 `--trust-level` 只在上游 `/create-*` 跳階段有效，不影響下游 pipeline，禁止跳過 QA 直接進 `DIALOGUE_FINAL`：`UPSTREAM_DOWNSTREAM_SPEC.md:5408-5435`。
- UD §10.7.2 明確下游 skill 收到 `--trust-level` 應拒絕，且下游 phase entry 的 `import_source` 永遠 null：`UPSTREAM_DOWNSTREAM_SPEC.md:5689-5698`。
- Contract A.8 明確 trust-level 只限上游 `/create-*`，對下游 pipeline 影響為無：`INTEGRATION_CONTRACTS.md:890-922`。
- SPEC §5.4a 明確 `import_source` 只在上游 `/create-*` 跳階段路徑有效，下游永遠走標準 DRAFT -> QA -> REVIEW -> FINAL：`SPEC.md:559-565`。

備註：REQUIREMENTS_LOCK §6.2 與 DECISIONS_LOG 舊摘要仍有 `agent_assisted` 跳 QA 的舊文字；因本輪要求 A 類文件「不審，當對齊基準」，此處列入 §3 新發現 / source limitation，不改 Recheck-08 target scope 判定。

### Recheck-09：PS-03/04/05 機械落地

**判定：✓ PASS**

證據：

- TASKS A.5 已將 phase_log `status` 欄位標為 D-042 已 formalize、P-012 RESOLVED：`TASKS.md:616-620`。
- TASKS A.5 bootstrap 範例補 `status: completed`，驗收也要求第一筆 bootstrap 紀錄含該 status：`TASKS.md:621-639`。
- TASKS A.0 啟動 gate 引用 PHASE_3_COMPLETION_REPORT §6.2a，並列出全 4 項條件：`TASKS.md:235-241`。
- TASKS A.0F.8 驗收只把 clipboard 納入 Phase A.0 必做，`local_llm_endpoint` POST 明確移到 Phase B+ 驗收：`TASKS.md:873-881`。

## §3 新發現 finding

### NF-D2-01 [Minor / source-limitation] trust-level 舊口徑仍留在最高權威快照與舊決策摘要

**狀態：** 不改 Recheck-08 target scope PASS，但建議 master 在升 LOCKED 前處理或標 supersede。

證據：

- REQUIREMENTS_LOCK §6.2 仍寫 `--trust-level agent_assisted` 為「跳 QA」，`external_llm` 為「走完整 QA」：`REQUIREMENTS_LOCK.md:262-270`。
- DECISIONS_LOG 舊 P-019 RESOLVED 摘要仍寫「agent_assisted 跳 QA / external_llm 走完整 QA」：`DECISIONS_LOG.md:642-645`。
- 後續正式 target 文件已改為限上游，見 Recheck-08 證據；因此此 finding 是 authority snapshot / historical summary 的殘留，不是新需求。

## §4 升 LOCKED 條件評估

對照 `_design/CODEX_RECHECK_STARTER_D2.md` §5：

1. **全 spec LOCKED：不建議現在升。** Recheck-02 未通過，UD 仍有可污染 Phase D 實作的 5 份 QA 殘留。
2. **DECISIONS_LOG v1.0：暫緩。** Recheck-03 target scope pass，但 §3 的 trust-level 舊摘要建議在 v1.0 前整理或標 supersede。
3. **Phase A.0.1 任務描述定稿：可視為已定稿。** TASKS A.0 gate、parser 9 大類、source_keys、base_dialogue、phase_log status 等本輪相關點均對齊。
4. **CODEX (d) clean：未 clean。** Recheck-02 必修項 fail。

結論：尚未達到 Stage 7 升 LOCKED 條件。

## §5 最終 Go/No-Go

**NO-GO。**

理由：

- Recheck-01 已 PASS。
- 本輪 Recheck-03 ~ Recheck-09 target scope 均 PASS。
- Recheck-02 未達成「QA 8 份必跑 + 所有 5 份 / 五份 改 8 份或標 supersede」要求，且殘留位於 UD 狀態機與實作 checklist，不宜升 LOCKED。

建議下一步：只針對 Recheck-02 的殘留做一輪小 patch，重點清單為 `SPEC.md:1187-1192`、`UPSTREAM_DOWNSTREAM_SPEC.md:2122`、`2209`、`2288-2309`、`7394`；同時可順手處理 §3 的 trust-level 舊摘要殘留。完成後只需重跑 Recheck-02，必要時 spot-check Recheck-08。
