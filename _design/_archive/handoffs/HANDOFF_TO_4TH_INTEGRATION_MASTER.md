狀態：DRAFT  
版本：v1.0  
最後更新：2026-05-19  
適用範圍：給「第四輪整合 master」新對話的接手包  
優先級：最高

# HANDOFF_TO_4TH_INTEGRATION_MASTER — 第四輪整合 master 對話接手包

# 0. 文件目的

這是給「新 master 對話」啟動時用的接手包。前一個 master 對話跨過了：
- Phase 3 設計第二輪三 specialist 完成
- CODEX (c) 深度審查
- P0 五項 + P1 六項拍板（D-037 ~ D-046）
- 三 specialist v0.3 patch 派工 + 接收 + 驗證

**到本接手包為止「設計階段」剩下：**
- 升 INTEGRATION_CONTRACTS v0 → v2
- 升主 SPEC / ARCHITECTURE / TASKS
- 升 PHASE_3_COMPLETION_REPORT v4.0 FINAL
- 觸發 CODEX (d) 短審查（可選）
- 升 LOCKED + 啟動 Phase A.0

預估剩餘工時：1 個 master 對話 + 1 次 CODEX 短審查 ≈ 1-2 天（看 user push 頻率）。

---

# 1. 對話啟動指令（直接複製貼到新對話）

```
我是 game-dialogue-bible 專案的使用者。前一個 master 對話完成 P0/P1 拍板（D-037~D-046）+ 三 specialist v0.3 patch 派工 + 接收驗證，把接手包寫好交給你。

工作資料夾：D:\劇本開發工具

你是「第四輪整合 master」對話。

**第一步必讀（按順序）：**
1. _design/HANDOFF_TO_4TH_INTEGRATION_MASTER.md（本檔，你的 scope）
2. _design/INTEGRATION_CONTRACTS_v2_SKELETON.md（你要填的骨架）
3. _design/DECISIONS_LOG.md §6.7（D-037~D-046 拍板紀錄）
4. _design/CODEX_REVIEW_REPORT.md（CODEX (c) 識出的衝突 + 越界）
5. _design/REQUIREMENTS_LOCK.md（user 需求 lock）

**第二步讀三 spec v0.3：**
6. _design/DATA_FORMAT_SPEC.md（DF v0.2 / 2674 行 — 注意：DF 命名 v0.2 但實質與 UD/UX v0.3 同輪次）
7. _design/UPSTREAM_DOWNSTREAM_SPEC.md（UD v0.3 / 7401 行）
8. _design/UX_SPEC.md（UX v0.3 / 5051 行）
9. _design/L3_EXPORT_PROMPT_SCHEMA.md（master 上一輪新建，contract 級）

**第三步讀主基線：**
10. _design/SPEC.md（基線 — 你要動的對象）
11. _design/ARCHITECTURE.md（同上）
12. _design/TASKS.md（同上）
13. _design/INTEGRATION_CONTRACTS.md（v0 — 你要升 v2）
14. _design/PHASE_3_COMPLETION_REPORT.md（v4.0 草稿 — 你要升 FINAL）

**你的 scope：**
- 把 INTEGRATION_CONTRACTS_v2_SKELETON.md 所有 [FILL-IN] 填完，產出 INTEGRATION_CONTRACTS v2 正式版
- 升主 SPEC / ARCHITECTURE / TASKS（依 §5.2/§5.3/§5.4 工作清單）
- 升 PHASE_3_COMPLETION_REPORT 為 FINAL
- 觸發 CODEX (d) 短審查（用 CODEX_REVIEW_STARTER.md，但 scope 改為「只看 v2 contracts + 主 SPEC 一致性」）
- 升 LOCKED + 啟動 Phase A.0

**禁止越界：**
- 不重做三 specialist v0.3 spec 內容（pattern lock，只搬進主 SPEC）
- 不改 D-001 ~ D-046 拍板結論（要動需 user 拍板）
- 不寫 00_protocol / 09_qa 實檔（CODEX tier 2 邊界，屬 Phase A.0 之後）
- 不擅自啟動 Phase A.0 寫 parser（升 LOCKED 後才開）

請先回報你讀完 14 份文件後對 scope + 順序的理解，再開始填 contracts。
```

---

# 2. 當前狀態快照

## 2.1 設計文件狀態

| 檔 | 版本 | 狀態 | 行數 | 備註 |
|---|---|---|---|---|
| SPEC.md | v0.x | LOCKED 設計層（4 輪 CODEX 審） | — | 你要動的對象（partial supersede）|
| ARCHITECTURE.md | v0.x | LOCKED 設計層 | — | 同上 |
| TASKS.md | v0.x | LOCKED 設計層 | — | 同上 |
| DECISIONS_LOG.md | v0.8 | DRAFT | 1201 | 含 D-001 ~ D-046 |
| INTEGRATION_CONTRACTS.md | v1（過渡） | DRAFT | — | 你要升 v2 |
| INTEGRATION_CONTRACTS_v2_SKELETON.md | v2.0-skeleton | DRAFT | ~250 | 上輪 master 寫的骨架 |
| PHASE_3_COMPLETION_REPORT.md | v4.0 草稿 | DRAFT | — | 你要升 FINAL |
| REQUIREMENTS_LOCK.md | v1.0 | FINAL | — | 不動，當 north star |
| DATA_FORMAT_SPEC.md | **v0.2** | DRAFT (第 1 輪 patch 完) | 2674 | DF 第 1 輪 patch |
| UPSTREAM_DOWNSTREAM_SPEC.md | **v0.3** | DRAFT (第 1 輪 patch 完) | 7401 | UD 第 1 輪 patch |
| UX_SPEC.md | **v0.3** | DRAFT (第 1 輪 patch 完) | 5051 | UX 第 1 輪 patch |
| L3_EXPORT_PROMPT_SCHEMA.md | v0.1 | DRAFT | 189 | master 新建 |
| CODEX_REVIEW_REPORT.md | v0.1 | DRAFT | 334 | CODEX (c) 審查結果 |

**注意版本號不對齊：** DF 命名 v0.2，UD/UX 命名 v0.3。三 spec **內容輪次同等**（CODEX 審查後 master 拍板的第一輪 patch 都已交付）。不要看數字以為 DF 落後。

## 2.2 git commit 歷史（近 8 次）

```
962a5f3 UD v0.3 patch: D-037 KEY status enum + D-038/039 §12 A1+records / D-041 10_art_assets / D-042 base_dialogue / D-043 8 QA / D-046 cross-ref / C-08 trust-level / O-04/05 議題清單 / §0 v0.3
35b907e UX v0.3 patch: D-046 8 項 + L3_EXPORT_PROMPT_SCHEMA 對齊
23481d8 DF v0.2 patch: D-037 dialogue_keys Map + KEY lifecycle / D-042 phase_log 5 new fields / D-044 A-* subtype 7 / D-045 A-* not in narrative status / O-01 tone adjustment — Master 4th-round P0/P1 integration
3acda89 Master 4th-round: D-037~D-046 + L3_EXPORT_PROMPT_SCHEMA v0.1 + CODEX review report archived
e0549a9 DF-9+10+11+§13: migration table + parser 9-cat checklist + master TBD (empty) + cross-ref summary — DATA_FORMAT_SPEC v0.1 complete
4e102a4 UD-4th: §12 export skill + §13 A-* downstream + §2.12 cross-ref overview + §9 new issues v0.2-F~H
e66a134 UD-3rd: i18n KEY writing + §11 cross-ref + §10 manuscript import
6bce0a2 DF-5+6+7: extensible entity/qa_type registries (Template/Instance/parser) + JSON export schema (single-file records[] + manifest)
```

## 2.3 三 spec v0.3 驗證結果

| 檢查 | 結果 |
|---|---|
| check_headers.py | 0 errors / 4 warnings（全 pre-existing 在 INTEGRATION_CONTRACTS / PHASE_3_REPORT / UX_PRIOR_DRAFT / UX_PROTOTYPE_ANALYSIS）|
| check_paths.py | 245 errors（baseline 全 in 01_a/b/c 既有模板 + UD §2 v0.1 substantive line 3749）|

三 spec **自身**完全 clean，零新增 error。

---

# 3. 整合工作清單（按執行順序）

## 3.1 階段 1：填 INTEGRATION_CONTRACTS_v2_SKELETON 為正式 v2

**輸入：**
- `_design/INTEGRATION_CONTRACTS_v2_SKELETON.md`（骨架 + `[FILL-IN]` 佔位）
- 三 spec v0.3

**動作：**
- 逐條把 Contract A.1~A.8 / B.1~B.8 / C.1~C.5 填具體形狀
- 從三 spec 對應段拷貝 schema 範例
- 處理跨 spec 衝突（若還有）— 標 `[MASTER-TBD]` 升 user 裁決

**輸出：** `_design/INTEGRATION_CONTRACTS.md` 升 v2.0

**預估行數：** 1500-2000 行

**預估時間：** 1-2 小時對話工時

## 3.2 階段 2：升主 SPEC

**SPEC 段落更新清單（依 D-NNN）：**

| SPEC 段 | 對齊 D-NNN | 動作 |
|---|---|---|
| §5.1 | D-024 (A-* added) + D-044 (7 subtype) | partial supersede — A-* entity 加 7 subtype enum |
| §5.2.3 | D-027 (SINGLE_ITER) | mode_tag 5→6 + SINGLE_ITER 行為定義 |
| §5.2.4 | D-043 + DF Phase 3 §8 | qa_type 5→8 + extensible registry |
| §5.4 | D-042 | phase_log sub-schema 補 5 新欄位 |
| §12 | D-043 | QA pipeline 5→8 + 09_e final-gating |
| §13 / §14 | D-038 | L3 export A1 流程；既有 4 個 /export-* 不擴充 |
| §16 | D-040 + D-046 #5 | LOCKED → DEPRECATED 降級流程；無 frontmatter 三欄位 |

**禁止：** 不動 §4 18 項設計決策匯總（已 LOCKED）。

**預估時間：** 1-2 小時

## 3.3 階段 3：升主 ARCHITECTURE

**ARCHITECTURE 段落更新清單：**

| 段 | 動作 |
|---|---|
| A.0 parser 章節 | 補 9 大類處理項（DF §11） |
| Frontend adapter 章節 | 新增 8 個 API endpoint（UX NS Query-API 類） |
| Export 章節 | 改寫為 A1 prompt 生成器（前端內嵌，無 server） |

**預估時間：** 30 分鐘 - 1 小時

## 3.4 階段 4：升主 TASKS

**TASKS 段落更新清單：**

| 段 | 動作 |
|---|---|
| Phase A.0 | 補 9 項 parser tasks（對應 DF §11） |
| Phase A.5 | 新建 init-project task 用 entity_type_registry / qa_type_registry Template |
| Phase C.5 | export prompt 生成（前端 only） |
| Phase D.4 | QA pipeline 5→8 改寫 |
| 前端工具任務群 | 補 F1/F2/F3/F6/F7 + Export panel + Asset panel |

**預估時間：** 1 小時

## 3.5 階段 5：升 PHASE_3_COMPLETION_REPORT v4.0 為 FINAL

**內容：**
- Phase 3 設計收斂統計（三 spec 行數 / 總 D-NNN 數 / Pending 議題彙整）
- Phase A.0 準備度評估
- 進 LOCKED 條件 check

**預估時間：** 30 分鐘

## 3.6 階段 6：CODEX (d) 短審查（可選但建議）

**觸發方式：** 用既有 `_design/CODEX_REVIEW_STARTER.md`，但 scope 縮限為：
- 只看 INTEGRATION_CONTRACTS v2 + 主 SPEC/ARCH/TASKS 升級段
- 不重審三 spec v0.3
- 不寫實檔

**預估 CODEX 時數：** 1-2 小時

**回來後動作：** 若 CODEX 找出新衝突，回階段 1 修小 patch；若 clean，進階段 7。

## 3.7 階段 7：升 LOCKED + 開 Phase A.0

**最後動作：**
1. 三 spec v0.3 + INTEGRATION_CONTRACTS v2 + 主 SPEC/ARCH/TASKS 全標 LOCKED
2. DECISIONS_LOG 升 v1.0（不再加新 D-NNN，新議題另寫）
3. 開 Phase A.0 第一個 parser task

---

# 4. 跨 spec Pending 議題清單

依 INTEGRATION_CONTRACTS_v2_SKELETON §6 抓出。**整合 master 對話需在升主 SPEC / TASKS 時參考。**

## 4.1 UD §9 Pending (12 條)

| 編號 | 議題 | 優先級 | 對齊建議 |
|---|---|---|---|
| 9.1.1 | P-009 08_a §11.1 patch | 高 | CODEX tier 2 寫 |
| 9.1.3 | P-011 canon delta | 低 / 成熟期 | Phase D+ |
| 9.1.5 | P-013 LOCKED retcon | 中 | 對齊 D-040 後再議 |
| 9.1.7 | P-015 file mutex | 中 | A.0 parser 後 |
| 9.2.1 | v0.2-A 00_q 實檔 | — | CODEX tier 2 邊界 |
| 9.2.2 | v0.2-B 00_p 實檔 | — | CODEX tier 2 邊界 |
| 9.2.4 | v0.2-D 衝突 merge UI | — | [TBD-UX-CONFIRM] |
| 9.2.5 | v0.2-E §2.10.3 19 vs 20 欄 | 低 | master 整合對齊 |
| 9.3.1 | 高風險場景 enum | 中 | 對齊 09_h |
| 9.3.2 | D.3.5 路徑 B 後處理 | 高 | 對齊 D-043 |
| 9.3.3 | 05_b 章節空殼 weight | 低 | — |
| 9.3.4 | 00_b anchors 擴充 | 低 | — |
| 9.3.5 | 下游 pipeline 解讀權威 | 中 | 對齊 D-039 |

## 4.2 UX §9 Pending（依分類）

- Schema 類 11 PARTIAL（D-038 / D-039 已 RESOLVED 大部分）
- Query-API-Adapter 類 9 條（屬 parser service / frontend adapter — 主 ARCH 補）
- Algorithm 類 2 條（屬 upstream algorithm — 主 ARCH 或 D.4 補）
- NS-NEW-1 09_e schema（待 UD §3.6.3 / §3.6.6 細化）

## 4.3 既有 P-027 ~ P-030 Pending

DECISIONS_LOG §6.6.5 仍 Pending：
- P-027 UX 細節（合併進 UX v0.3 §10）
- P-028 canon delta 設計（成熟期）
- P-029 glossary 13 術語具體文字
- P-030 multi-medium future scope

---

# 5. 已 RESOLVED 議題彙整（D-037 ~ D-046）

| D-NNN | 議題 | 對齊 spec |
|---|---|---|
| D-037 | dialogue_keys = Map (DICT) + KEY lifecycle status enum | DF §4.2 / §4.5 + UD §2.11.5 |
| D-038 | L3 export A1 prompt + CC/CODEX + 4 附帶 | UD §12 + UX §11.6.11 + L3_EXPORT_PROMPT_SCHEMA |
| D-039 | JSON `manifest + records[]` 為權威，UD 六區降 derived | UD §12 + DF §9 (不動) |
| D-040 | LOCKED Save race guard | UX §11.5.7~9 |
| D-041 | A-* SoT = `10_art_assets/`（confirm） | DF §5 + UD §13 |
| D-042 | phase_log 5 新欄位 + `base_dialogue` 新欄位 | DF §3.3a~e + UD §4.7 |
| D-043 | 8 份 QA 全預設必跑 + 09_e final-gating | UD §2.5 + UX §11 |
| D-044 | A-* subtype 7 種 | DF §5.1a |
| D-045 | A-* 不納入 narrative `/status` | DF §5.6 + UX §11.1.6a |
| D-046 | UX-54~80 補表 + 7 項 patch | UX §7.9 + §11.5 + §11.6.11 + §11.4.3 |

---

# 6. 風險警示給整合 master

## 6.1 升主 SPEC 時的 partial supersede 處理

主 SPEC 是 4 輪 CODEX 審查 LOCKED 文件。即使 D-NNN 已拍板，partial supersede 段也要：
1. 明確標 `[v1.x partial supersede via D-NNN]`
2. 保留原段內容 → 註明 supersede 範圍
3. 不刪除原段

**例：** SPEC §5.1 既有 7 種 entity 類型 → v1.x 加第 8 種 A-*（D-024 + D-044）→ 用 `[v1.x partial supersede via D-024 + D-044]` 標註。

## 6.2 主 SPEC 升級觸發的潛在新衝突

若整合 master 對話發現「兩個 D-NNN 在主 SPEC 段落落地時互相牴觸」，例如：
- D-037 dialogue_keys Map shape vs SPEC §5.2.3 既有 frontmatter 順序鎖定
- D-042 phase_log 新欄位 vs SPEC §5.4 既有 phase_log schema 描述

**處理方式：** 標 `[MASTER-TBD]`，回頭升 user 拍板，**不要擅自決定**。

## 6.3 三 spec v0.3 內部一致性

CODEX (c) 審查時找出的 17 條衝突，三 specialist v0.3 patch 後**多數已 RESOLVED**，但仍可能殘留：
- 11 條 RESOLVED via D-037~D-046（佔大部分）
- 少數可能在 patch 時對齊不完全（如 UD §10.6 phase_log 紀錄是否被三 specialist 一致理解）
- 整合 master 對話建議跑一輪 quick cross-ref：搜尋 `[BLOCKED:UPSTREAM_DOWNSTREAM]` / `[TBD-UX-CONFIRM]` 標記，看殘留是否 conflict 還是已對齊

## 6.4 sandbox virtiofs cache 已知問題

工作目錄 Windows 端是權威。Sandbox 端 `wc -l` / `md5sum` 偶爾顯示舊版（cache 故障），但 git HEAD 和 Windows 端真實檔內容是 OK 的。若整合 master 對話也撞到，記得用 `git show HEAD:<path>` 取真實內容，不要相信 sandbox 端 wc。

---

# 7. 整合完成 = 進 Phase A.0 的條件

```
進 Phase A.0 前必須全部成立：

✓ INTEGRATION_CONTRACTS v2 完整版（所有 [FILL-IN] 填完）
✓ 主 SPEC / ARCHITECTURE / TASKS 對齊 D-037~D-046
✓ PHASE_3_COMPLETION_REPORT v4.0 升 FINAL
✓ （可選）CODEX (d) 短審查通過
✓ 三 spec v0.3 + 主 SPEC v1.x 同 LOCKED
✓ DECISIONS_LOG v1.0
✓ Phase A.0 第一個 task（A.0.1 frontmatter parser）任務描述定稿
```

---

# 8. 給整合 master 對話的提醒

1. 你不是 specialist，**不寫詳細 schema 提案**。你的工作是「把已拍板結論搬進主 SPEC / ARCH / TASKS」+「填 contracts」。
2. 主 SPEC partial supersede 段都要保留原段 + 加 supersede 標記，**不刪除**。
3. 整合過程若發現「兩個 D-NNN 在實作層牴觸」，立刻停手回升 user 拍板，不擅自決定。
4. CODEX tier 2 邊界**不在你 scope** — 不要寫 00_p / 00_q 等實檔。
5. Phase A.0 啟動本身**不是你的工作** — 你的最後動作是「升 LOCKED + 確認 Phase A.0.1 任務描述定稿」。實際寫 parser 程式是 Phase A.0 內部 task。
6. context 預算管理：若你做到一半發現 context 不夠，寫一份 v2 接手包（HANDOFF v2）給下一個 master 對話。

---

# 9. 文件維護紀律

- 本檔是「**接手指南**」，整合 master 對話讀完後**不需要更新本檔**
- 若整合 master 對話發現本檔有不準確的地方，標 errata 在新 D-NNN 中
- 整合完成後可把本檔 archive 進 `_design/archive/`，保留歷史
