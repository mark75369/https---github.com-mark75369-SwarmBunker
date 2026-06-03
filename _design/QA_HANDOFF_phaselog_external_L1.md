狀態：REVIEW
版本：v1.0（外部 QA / L1 finding 交接 — .protocol_version phase_log 外審結果，回交給「剛實作此部分的對話」(L0) 做交互確認 採納/駁回/deferred）
最後更新：2026-06-03
適用範圍：接手 L0（產出 .protocol_version phase_log 紀錄的那個對話）— 對下列 L1 finding 逐條交互確認，不可橡皮圖章
優先級：高

# QA HANDOFF — `.protocol_version` phase_log 外部 QA（L1 → L0 交互確認）

## 0. 你的任務（一句話）

你是 **L0**（剛把這些 phase_log 紀錄寫出來的對話）。我是 **L1 外部審**（與你不同 context，用 workflow 32 個獨立 agent 親手重推、不採信任何自報數字）。
**請對 §4 每一條 finding 做交互確認**：在「L0 結論」欄填 **採納 / 駁回 / deferred**，並對 MAJOR 以上至少**親手重現一次**再下判斷（對齊 `REVIEW_LOOP_PROTOCOL.md` §2 抽查規則：L1 摘要不可只蓋章）。

> 本檔是 **L1 finding list**，不是修復指示。**我沒有改動 `.protocol_version`**（它正被並發寫入，盲改會撞 race）。修不修、怎麼修，由你交互確認後決定。

---

## 1. ⚠️ 先讀：這是一個「活檔 + 並發寫入」的前提陷阱

`.protocol_version` 是 **runtime tracking 活檔，本次外審期間仍在被並發 append**。實測同一檔兩個時間點：

| 指標 | 早期快照（外審 brief） | 外審當下實際 |
|---|---|---|
| phase_log 總數 | 57 | **67** |
| qa entry 數 | 3 | **13**（全 13 場） |

**含意（兩條都要你確認）：**
1. 我交給 workflow 的 ground-truth brief（57/3）**是過期快照**，已被 reviewer 當場抓錯（見 GT-META）。**請以 67/13 為準。**
2. 早先一度被疑為缺陷的 **「104 份 QA 檔 vs 只登 3 筆 qa」屬假警報** —— 那只是讀到 run 進行到一半。**現在 disk 13 場 QA ↔ phase_log 13 筆 qa 完全對齊，無 orphan**（F2 已確認）。此項**不需處理**，但請你交互確認後正式關閉，避免它再被當缺陷流傳。

---

## 2. 環境 / 範圍

- 目標檔：`_sandbox/測試專案/.protocol_version`（top-level key `phase_log` 為 list）。
- 跑 Python 前設 `PYTHONIOENCODING=utf-8 PYTHONUTF8=1`（Windows 中文）。
- 外審手法：workflow `external-qa-phaselog`，5 維獨立審（yaml-structure / forward-consistency / backward-consistency / l2-tooling / anchoring-semantics）→ 每條 finding 派對抗 verifier 重推。**27 findings、0 被駁回**。
- **`.protocol_version` 不在 `check_paths.py` / `check_headers.py` 掃描範圍內**（無 5 欄 header 的 runtime 檔）→ 此檔目前**無任何 L2 自動守門**，只能靠這種外審（見 L2-03）。

---

## 3. 通過項（請依 L3 規則抽 ≥1 條 PASS 檔親手複看，防 L1 漏報）

| ID | 結論 | 證據 |
|---|---|---|
| STRUCT-01/02 | 結構乾淨：yaml.safe_load 成功、67 筆全 column 0、**零誤縮排**；原「qa 嵌在 dialogue-write 下」縮排缺陷**確實已不存在** | `MIS2:0 MIS4:0 MISN:0`；col0 count 67 == safe_load 67 |
| FWD-01 | 前向一致：phase_log 引用的每條路徑（dialogue_paths/qa_report_paths/…）在 disk 都存在 | 0 missing |
| F2 | 後向一致：13 場 ×8=104 份 QA 報告 ↔ phase_log 13 筆 qa，場景集完全相同 | disk−log、log−disk 皆空 |
| F3/F4 | 對白 52 檔 ↔ 28 dialogue-write entry、任務包 13 ↔ 13 scene-task entry，無 orphan | — |

---

## 4. Findings（需你交互確認）— What / Where / Why / 下一步

### F-A ｜ ANCH-02 ｜**MAJOR**｜F-004 read-modify-write 競態造成重複 entry
- **What**：phase_log 有 **2 筆完全重複** entry，整組 S-04-02 dialogue-write（trial + converge）被 append 兩次。
- **Where**：`phase_log` index **41 == 43**（`/dialogue-write`，scene S-04-02）、**42 == 44**（`/dialogue-write --converge`，scene S-04-02）。總 67 筆，**唯一僅 65 筆**。
- **Why**：典型 read-modify-write 並發未上鎖 → 同一批 append 落兩次。**這是真缺陷，不是縮排假象。**（我已親手重現：`total 67 | unique 65 | dup index 41==43, 42==44`）
- **下一步**：dedup 該 2 筆。**但須等並發寫入靜止後**用 read-modify-write 安全處理，否則與正在寫的 agent 撞車。→ **L0 結論：採納（已親手重現 total 67 / unique 65 / dup 41==43、42==44，與 L1 完全吻合）。dedup 修復 deferred —— 2 筆為無害冗餘 log、不擋寫作；且程式化重寫 .protocol_version YAML 會清掉既有 issue_completions 註解（破壞可讀性），須以保留格式方式（ruamel 或手術式刪塊）於並發靜止時做。root cause = F-004 並發 race，已折入工具迭代 handoff（WP-3）。**

### F-B ｜ ANCH-03 ｜**MAJOR（語義）**｜`qa_decision==PASS` ≠ 定樁/FINAL
- **What**：phase_log 把場景標到「QA 通過（PASS）」，但**沒有任何一場是正式定樁（FINAL）**。
- **Where**：13 筆 qa entry 的 `qa_decision: PASS` / `depth_layer`，無 FINAL 對應狀態。
- **Why**：下游 skill / 人若拿 phase_log 當「哪場已定樁」依據會**過度解讀**——PASS 只是 QA 階段結論，不等於凍結。
- **下一步**：確認語義定義；若需「定樁」概念，應有獨立 FINAL 標記，勿讓 PASS 被誤讀。→ **L0 結論：採納（屬設計正確，非缺陷）。/qa skill 設計上 qa_decision=PASS 就是 pre-final QA 結論，FINAL/定樁須人類填 09_e final-gating（qa skill 明文不 auto 升 FINAL、不建 09_e）。PASS≠FINAL 是 by-design 的關卡分離。無需改資料；列為「下游/人勿把 PASS 讀成定樁」的語義提醒即可。**

### F-C ｜ SCHEMA-01 ｜**MINOR**｜qa entry 鍵不一致
- **What**：qa entry schema key 不統一。
- **Where**：多數用 `depth_layer`，但 **S-04-02 用 `depth_tier`**；**S-06-02** 多帶 `frictions / lens_divergence / udv_result`（他處皆無）。
- **Why**：不影響 parse，但破壞 entry schema 一致性，未來程式化彙整會踩坑。
- **下一步**：統一 `depth_tier`→`depth_layer`；裁定 S-06-02 額外鍵保留或移除。→ **L0 結論：採納（已重現：9 條 depth_layer / S-04-02 用 depth_tier / S-06-02 多帶 frictions·lens_divergence·udv_result / 3 條無 depth 鍵）。cosmetic、不影響 parse 與寫作 → 修復 deferred（與 F-A 同批手術式處理）。建議裁定：depth_tier→depth_layer；S-06-02 額外鍵屬 dialogue/qa agent 自帶診斷、可保留但應列為 optional schema。root cause = 並發 agent 各寫略異 schema，折入工具 handoff（schema 一致性 / F-D lint 可一併檢）。**

### F-D ｜ L2-03 ｜**INFO（流程缺口）**｜本檔無 L2 自動守門
- **What**：`.protocol_version` 不在兩支 L2 掃描器範圍。
- **Why**：此 runtime 活檔的縮排 / 重複 / schema 漂移**沒有任何自動化能抓**，只能靠外審。
- **下一步**：考慮補一支輕量 lint（parse + dedup + schema 檢查）進 L2，否則 F-A 類缺陷會反覆發生。→ **L0 結論：採納 → 轉工具迭代 handoff。確認 .protocol_version 確不在 check_paths/check_headers 範圍。建議新增 `scripts/check_phaselog.py`（yaml.safe_load + entry dedup + qa schema 檢查）並掛 L2/pytest。此項 + F-A/F-C root cause 與既有 F-004（WP-3 並發）合併為一個工具 WP，交新對話。**

### GT-META ｜ COUNT-01/02 · GT-REFUTE · L2-06 ｜**MAJOR（交接準確性）**｜外審 brief 數字過期
- **What**：外審 brief 宣稱 57 entries / 3 qa，實際 67 / 13。
- **Why**：源於活檔並發（§1）。reviewer 因被要求「不准採信 brief、自己重推」而當場抓出——**這是外部 QA 生效的證據，也提醒：交接快照不可當權威，必當場重算。**
- **下一步**：本 finding 主要供你知情；確認以 67/13 為準即可。→ **L0 結論：採納（資訊性）。確認以 67/13 為準（已親手 yaml.safe_load 重算）。同意「交接快照不可當權威、須當場重算」原則——這也是本專案副對話/workflow 慣例。**

---

## 5. 交互確認 checklist（L0 親手做，勿只讀本檔摘要）

- [ ] 親手 `yaml.safe_load` 重算 `len(phase_log)` 與 qa 數 → 應得 **67 / 13**
- [ ] 親手重現 **F-A 重複**：dedup by entry → 應得 unique **65**、dup index **41==43 / 42==44**
- [ ] 抽 ≥1 條 §3 PASS 項親自複看（防 L1 漏報；建議抽 F2 後向一致）
- [ ] 對 F-A / F-B / GT-META（MAJOR）逐條填採納/駁回/deferred
- [ ] **修 F-A 前確認並發寫入已靜止**；deferred 項記入 backlog，不可悄悄丟棄（協議 §「deferred finding」）

## 6. 落地紀錄（L0 回填）

| 欄位 | 內容 |
|---|---|
| L1 reviewer | workflow `external-qa-phaselog`（runId wf_b339118d-ca9，32 agents，27 findings / 0 駁回）|
| L0 交互確認 | **5 採納 / 0 駁回 / 0 推翻**（F-A/F-B/F-C/F-D/GT-META 全採納；其中 F-B 採納為「設計正確、非缺陷」）。L0 = Claude Opus 4.8 主對話（2026-06-03），親手重現 F-A（67/65/dup 41==43·42==44）、F-C（depth_tier·額外鍵）、GT-META（67/13）。外部 QA 手法與結論背書。 |
| 修復 commit | F-A dedup / F-C schema normalize = **deferred**（無害症狀、不擋寫作；須保留格式手術式處理於並發靜止時）。root cause（F-004 並發 race / F-D 無 lint / schema 一致性）= **轉工具迭代 handoff**（見 `D:/findings-iter/_design/TOOL_ITERATION_HANDOFF.md`）|
| 殘留 deferred | F-A dedup、F-C normalize（Instance 本地 cosmetic，安全時可手術式清）；F-D check_phaselog.py lint（工具 WP，新對話做）|
