狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX (d) 短審後 master 第四輪 pre-LOCKED patch 完成的 targeted recheck 啟動包  
優先級：高  

# CODEX_RECHECK_STARTER_D2 — Master 第四輪 pre-LOCKED patch 完成後的 CODEX targeted recheck

# 0. 本檔用途

Master 第四輪整合對話完成 CODEX (d) 短審識出的 13 個必修 + 建議修項後（CC-01 ~ CC-10 + PS-01 ~ PS-05 + Pending count），把本檔 §1 內的 prompt 整段複製貼到新 CODEX 對話，啟動「**targeted recheck**」— 確認 pre-LOCKED patch 全部落地正確、可升 LOCKED。

**前置條件（必須先完成）：**

- ✓ Master 第四輪完成 INTEGRATION_CONTRACTS v2.0 + 主 SPEC v1.1 / ARCH v1.2 / TASKS v1.3 / PHASE_3 v4.0 FINAL
- ✓ CODEX (d) 短審 `CODEX_REVIEW_REPORT_D.md` 產出（NO-GO；13 finding）
- ✓ Master 第四輪 pre-LOCKED patch 完成（13 個必修 + 建議修項；對應 CC-01~CC-10 + PS-01~PS-05 + Pending count）

**本檔跟 CODEX_REVIEW_STARTER_D.md 的差別：**

| 維度 | CODEX_REVIEW_STARTER_D（前 starter）| **本檔 CODEX_RECHECK_STARTER_D2** |
|---|---|---|
| 觸發時機 | Master 第四輪整合 partial supersede 完成後 | **Pre-LOCKED patch 完成後（CODEX (d) NO-GO 修補完成）** |
| Scope | 全部主 SPEC/ARCH/TASKS 一致性 + INTEGRATION_CONTRACTS v2 + Pending | **只看 CODEX (d) 識出的 5 個 targeted recheck 範圍**（依 CODEX (d) §7 建議） |
| 預估 CODEX 時數 | 2-3 小時 | **45-90 分鐘**（只 verify 修補項；不重審全部）|
| 預期產出 | CODEX_REVIEW_REPORT_D.md（NO-GO + 13 finding）| **CODEX_RECHECK_REPORT_D2.md**（GO / 仍有殘留 finding 二選一）|

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「Master 第四輪 pre-LOCKED patch 完成後、升 LOCKED 前」的**targeted recheck**（CODEX (d) 後續審查）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔
- 你是 targeted reviewer — 只驗證 CODEX (d) 識出的 13 個 finding 修補項是否落地正確
- 你是升 LOCKED 前 final-check — 通過 → master 直接進階段 7 升 LOCKED；不通過 → 再一輪 pre-LOCKED patch
- 對應傳統：本輪是第 7 輪 CODEX 審查（前 6 輪：時期 A 4 輪 + (c) 1 輪 + (d) 1 輪）

**重要邊界（嚴格 scope）：**

- ✗ **不**重審 CODEX (c) 17 衝突 / 5 越界（已 RESOLVED via D-037~D-046）
- ✗ **不**重審 CODEX (d) §6 升 LOCKED 條件以外的議題
- ✗ **不**動 D-001 ~ D-046 拍板結論
- ✗ **不**動 REQUIREMENTS_LOCK.md（v1.0 FINAL）

**本輪 scope（嚴格限定 — CODEX (d) §7 建議的 5 個 targeted recheck 範圍）：**

1. **A-* metadata canonical 形狀統一**（CC-01 修補）
   - 檢查：Contract A.3 / B.4 / C.1 / C.5 + DF §5 + UD §13.2.1 + UX §11.1.6a + SPEC §5.1a
   - 必看：所有引用是否統一為 `10_art_assets/<subtype>/<group>.md`（DF subtype/group canonical）
   - 不可保留任何 `10_art_assets/<key>/metadata.md` 或 per-asset 寫法
   
2. **QA 8 份必跑落地**（CC-02 + PS-01/02 修補）
   - 檢查：SPEC §5.4 + §12 + ARCH §6.3 + TASKS D.4 + UD §2.5 / appendix
   - 必看：所有「5 份」/「五份」描述是否：(a) 改為 8 份 / 八份；(b) 或明確標「歷史原文，已 supersede via D-043」
   - qa_report_paths 驗證 8 條；qa_type 8 種；weight 規則明確

3. **Pending §6 校正**（CC-03 + §6 count 修補）
   - 檢查：INTEGRATION_CONTRACTS §6.2（UD 13 條 + owner / phase 完整）
   - 檢查：§6.4（P-027~P-030 對到正確 DECISIONS_LOG §6.6.5 P-ID）
   - 檢查：§6.5 拆 Phase A.0 parser / Phase A.0F frontend + 移除過期「本輪 master」目的地

4. **L3 export read-only**（CC-07 修補）
   - 檢查：L3_EXPORT_PROMPT_SCHEMA §1.2 / §1.4 + SPEC §13a + ARCH §4.2a + TASKS A.0F.8 / C.5a + UX §11.6.11
   - 必看：(a) `rerun_qa` 已移除；(b) `include_deleted` 已補；(c) phase_log 不 append `phase: export` entry；(d) UX「重跑 QA」按鈕已移除

5. **Frontend adapter + conflict modal 分清**（CC-08 + CC-09 修補）
   - 檢查 CC-08：UX §11.8.3 是否同步到 ARCH §13.2 8 endpoint（或明確標權威指向）
   - 檢查 CC-09：UX §11.7.6 mtime drift modal vs §11.7.6a entity naming conflict modal 是否分拆清楚
   - TASKS A.0F.9（entity 命名衝突 4 選項）vs A.0F.10（mtime drift 二選）是否一致

**額外 verify 項（CC-04 / CC-05 / CC-06 + PS-03 / PS-04 / PS-05 修補）：**

6. **source_keys 已加入 schema**（CC-04 修補）
   - 檢查：Contract A.1 schema 含 source_keys
   - 檢查：DF §4.2 欄位表含 source_keys
   - 檢查：DF §9.5 JSON dialogue_line record 含 source_keys
   - 檢查：TASKS A.0.2 parser 驗證含 source_keys

7. **base_dialogue 只在 phase_log**（CC-05 修補）
   - 檢查：UD §4.7 step 5 frontmatter 已移除 `base_dialogue` 行；只在 step 6 phase_log 寫
   - Contract A.6 / SPEC §5.4a 維持「base_dialogue 在 phase_log」不變

8. **trust-level 嚴格限上游**（CC-06 修補）
   - 檢查：DF §3.3 import_source 已移除「可跳 QA / 直接 final」說法
   - 對齊 Contract A.8 + UD §10.3 v0.3 + SPEC §5.4a 一致

9. **PS-03/04/05 機械落地**
   - PS-03：TASKS A.5 phase_log status 改「D-042 已 formalize」+ 補 bootstrap status 範例
   - PS-04：TASKS A.0 補啟動 gate 引用 PHASE_3 §6.2a
   - PS-05：TASKS A.0F.8 驗收只驗 clipboard，POST 移 Phase B+

---

**必讀文件（按順序）：**

A. 最高權威（不審；當對齊基準）
1. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL）
2. _design/DECISIONS_LOG.md（D-001~D-046 + P-001~P-030）
3. _design/CODEX_REVIEW_REPORT_D.md（v0.1 — 13 finding 對照基準）

B. 本輪審查對象（核心 — pre-LOCKED patch 落地）
4. _design/INTEGRATION_CONTRACTS.md（v2.0 + pre-LOCKED patch）
5. _design/SPEC.md（v1.1 + pre-LOCKED patch）
6. _design/ARCHITECTURE.md（v1.2 + pre-LOCKED patch）
7. _design/TASKS.md（v1.3 + pre-LOCKED patch）
8. _design/PHASE_3_COMPLETION_REPORT.md（v4.0 FINAL）

C. Specialist v0.3 patch + targeted patch（核心 — CC-01/05/06/09 修補）
9. _design/DATA_FORMAT_SPEC.md（v0.2 → v0.3 含 CC-04/06/07 + source_keys 修補）
10. _design/UPSTREAM_DOWNSTREAM_SPEC.md（v0.3 → v0.4 含 CC-01/05 + A-* canonical + base_dialogue 修補）
11. _design/UX_SPEC.md（v0.3 → v0.4 含 CC-01/07/08/09 + Asset Panel canonical + Export panel + conflict modal 分拆 + endpoint 對齊）
12. _design/L3_EXPORT_PROMPT_SCHEMA.md（v0.1 → v0.2 含 CC-07 rerun_qa 移除 + include_deleted 補）

D. 歷史紀錄
13. _design/HANDOFF_TO_4TH_INTEGRATION_MASTER.md
14. _design/CODEX_REVIEW_REPORT.md（CODEX (c) — 已 RESOLVED）

---

**你要交付的產物：**

新建：`_design/CODEX_RECHECK_REPORT_D2.md`

報告格式：

```markdown
狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX targeted recheck D2 — Pre-LOCKED patch 落地驗證  
優先級：高  

# CODEX_RECHECK_REPORT_D2 — Pre-LOCKED targeted recheck

## 0. 摘要

**結論：[GO / NO-GO / NEAR-GO（仍有 1-2 minor 殘留）]**

## 1. 審查範圍

### 1.1 Files Read
（列你實際讀的檔案 + 行數；按 starter §1 必讀 14 份 + 對焦修補項目段落）

### 1.2 Files NOT Modified
（明示沒動的檔案）

## 2. 9 個 targeted recheck 項目逐項驗證

對每個項目給 ✓ Pass / ✗ Fail / △ Partial：

### Recheck-01：A-* metadata canonical（CC-01 修補）
- 狀態：✓/✗/△
- 證據：line ref + 評語
- 殘留：如有

### Recheck-02：QA 8 份必跑（CC-02 + PS-01/02）
### Recheck-03：Pending §6 校正（CC-03 + count）
### Recheck-04：L3 export read-only（CC-07）
### Recheck-05：Frontend adapter + conflict modal（CC-08 + CC-09）
### Recheck-06：source_keys schema（CC-04）
### Recheck-07：base_dialogue phase_log only（CC-05）
### Recheck-08：trust-level 限上游（CC-06）
### Recheck-09：PS-03/04/05 機械落地

## 3. 新發現的 finding（若有）

不期望出現新衝突；若 pre-LOCKED patch 引入新問題列在這。

## 4. 升 LOCKED 條件評估

對 PHASE_3 §6.2a 四項：
- 1. 全 spec LOCKED → 還沒升（pending 本輪 GO 後）
- 2. DECISIONS_LOG v1.0 → 還沒升
- 3. Phase A.0.1 任務定稿 → 已定稿
- 4. CODEX (d) clean → **本輪結果決定**

## 5. Go / No-Go 決定

- **GO：** 9 項全 ✓ → master 可直接進階段 7 升 LOCKED
- **NEAR-GO：** 8+ 項 ✓，1-2 minor 殘留可在升 LOCKED 同時修 → master 自決
- **NO-GO：** 任一必修項仍 ✗ → 第二輪 pre-LOCKED patch 後再 recheck

## 6. 後續審查建議

若 GO 後 Phase A.0 / A.0F 實作期間發現新議題，建議下次審查 scope。
```

---

**你不做的事（再次重申）：**

- ✗ 不重審 CODEX (c) / (d) 已 RESOLVED 項目
- ✗ 不寫實作檔
- ✗ 不重新拍板 D-NNN
- ✗ 不提新需求

---

**估時：**

- 讀必看文件 + 修補項目段落：20-30 分（focus 在 9 項 recheck）
- 寫報告：25-45 分（含驗證每項 + 結論）
- **總估時 45-90 分鐘**

審查完成後 commit + push。master 讀完報告：GO → 階段 7；NO-GO → 再一輪 patch。
```

---

# 2. 9 個 targeted recheck 項目對照 checklist

供 CODEX 在審查時系統性走過：

## 2.1 A-* metadata canonical 形狀（CC-01）

- [ ] Contract A.3 §2.3.2 directory structure：`portraits/<character>.md` per character 等
- [ ] Contract B.4 / C.5 Mapping rules 已改為 `10_art_assets/<subtype>/<group>.md`
- [ ] DF §5.2 directory structure / §5.3 metadata schema：per-character/per-group 模型
- [ ] UD §13.2.1：已升 v0.4 改 per-group .md（原 per-asset .md supersede 標註）
- [ ] UX §11.1.6a Asset Panel：已校正路徑為 `<subtype>/<group>.md`
- [ ] UX §7.9.4 UX-71：路徑已校正
- [ ] SPEC §5.1a：`10_art_assets/<subtype>/<group>.md` 為 SoT

## 2.2 QA 8 份必跑落地（CC-02 + PS-01/02）

- [ ] SPEC §5.4 manifest 表「8 份」（或標歷史 supersede）
- [ ] SPEC §12 各處「5 份」/「五份」全已改 8 份 / 八份 或標歷史
- [ ] ARCH §6.3 寫檔/驗證/輸出段 weight 0.125 + 8 種 qa_type + 8 份 output
- [ ] TASKS D.4 驗收 8 份 + 禁止跳過 8 份
- [ ] TASKS D.5 README 6/7 步「8 份」
- [ ] Cross-skill 資料流圖：8 份 QA 報告

## 2.3 Pending §6 校正（CC-03 + count）

- [ ] §6.2 改「13 條」+ owner / phase 全列
- [ ] §6.4 P-027~P-030 對到正確 DECISIONS_LOG §6.6.5 P-ID（SINGLE_ITER / 手稿導入 / 前端 UX / L3 export）
- [ ] §6.5 拆 Phase A.0 parser / Phase A.0F frontend + 移除「本輪 master」目的地 + 補「第五輪 master」目的地

## 2.4 L3 export read-only（CC-07）

- [ ] L3_EXPORT_PROMPT_SCHEMA §1.2：`rerun_qa` 已移除 + `include_deleted: false` 已補
- [ ] L3_EXPORT_PROMPT_SCHEMA §1.4：constraints 含「不修改 phase_log，不寫入任何 entry」+ deleted dialogue_line 處理規則
- [ ] Contract A.7.6：v2.0 校正 — phase_log 不 append
- [ ] DF §9.8：v0.3 校正 — phase_log 不 append
- [ ] UX §11.6.11 Export panel UI：「重跑 QA」按鈕已改為「含已刪除 KEY」或移除

## 2.5 Frontend adapter + conflict modal 分清（CC-08 + CC-09）

CC-08 (frontend adapter)：
- [ ] UX §11.8.3：權威指向 ARCH §13.2 / 列完整 8 endpoint
- [ ] 舊 endpoint 標已 supersede

CC-09 (conflict modal)：
- [ ] UX §11.7.6 維持 mtime drift 二選一（reload / 強制覆寫 + 取消）
- [ ] UX §11.7.6a 新增 entity naming conflict 4 選項
- [ ] TASKS A.0F.10 驗收：mtime drift 不含 4 選項，明確指向 §A.0F.9 為 4 選項 task
- [ ] TASKS A.0F.9：entity 命名衝突 4 選項

## 2.6 source_keys schema（CC-04）

- [ ] Contract A.1 §2.1.1 schema：含 `source_keys` 欄位定義
- [ ] DF §4.2 欄位表：含 `source_keys`（v0.3 新增）
- [ ] DF §9.5 JSON dialogue_line record：含 `source_keys` 欄位
- [ ] TASKS A.0.2 parser 驗證：含 source_keys validation 規則

## 2.7 base_dialogue phase_log only（CC-05）

- [ ] UD §4.7 step 5：frontmatter 不寫 `base_dialogue`（已移除 + v0.4 校正註解）
- [ ] UD §4.7 step 6：phase_log 寫 `base_dialogue`（維持）
- [ ] Contract A.6 / SPEC §5.4a / DF §3.3d：base_dialogue 在 phase_log（維持）

## 2.8 trust-level 限上游（CC-06）

- [ ] DF §3.3：import_source 表已移除 `agent_assisted` 「後續可跳 QA 直接 final」說法
- [ ] DF §3.3：「下游 pipeline 行為差異」段已改為「trust-level 嚴格限上游」聲明
- [ ] 對齊 Contract A.8 / UD §10.3 / SPEC §5.4a 一致

## 2.9 PS-03/04/05 機械落地

PS-03：
- [ ] TASKS A.5 phase_log status：改「D-042 已 formalize；P-012 RESOLVED」
- [ ] Bootstrap 範例補 `status: completed`

PS-04：
- [ ] TASKS A.0 補啟動 gate 段引用 PHASE_3 §6.2a

PS-05：
- [ ] TASKS A.0F.8 驗收：clipboard 必驗；POST endpoint 移 Phase B+

---

# 3. 文件維護紀律

- 本檔是「啟動包」，CODEX (d2) 跑完後**不需要更新本檔**
- 若 CODEX (d2) 識出本檔不準確的地方，標 errata 在 CODEX_RECHECK_REPORT_D2.md
- CODEX (d2) GO 後本檔可 archive 進 `_design/archive/`，保留歷史
