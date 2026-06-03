狀態：DEPRECATED
版本：v1.0（過夜自主長跑 wake-up 報告；F8 Phase 3 → 稽核 → Batch 5 → 最終稽核全跑完並自修，park 在 feat/f8p3-audit-batch5 等 L3；最終全稽核 wf_f81550df-650 GO-with-fixes 已回填 + 自修）
最後更新：2026-06-03
適用範圍：user 醒來審閱 + 簽 L3 的單一入口；對齊 OVERNIGHT_RUN_F8P3_AUDIT_BATCH5.md §5
優先級：高

# 🌅 WAKE-UP REPORT — F8 Phase 3 → 稽核 → Batch 5 → 最終稽核（過夜自主長跑）

> **一句話：** 整條鏈做完，兩輪自我 QA 閉環 + 獨立 QA 對話複驗皆 GO（§2.4）；user 已 L3 拍板決策佇列 + 授權收尾 → **已 merge 進 `frontend-tools-a0f` + push**（見下方 L3 收尾紀錄）。

## L3 收尾紀錄（2026-06-03，user 拍板 + 授權）

- **決策佇列 L3 拍板**：Q1 = **ORG card 7 段**（加組織結構/層級）/ Q2 = **issue-ful**（00_n 改讀 issue_type_registry 00_n_organization key）/ Q6 = **禁 ORG↔ORG**；Q3/Q4/Q5/Q7 維持預設。落地 = **D-074 amendment**（DECISIONS_LOG v2.10 §6.27；commit `b7acd12`）。
- **D-074 amendment L1 外審**（`wf_5a3f9b19-a27`）：GO-with-fixes → 8 周邊同步 finding 全修（commit `5f0b70f`）→ L1 PASS。
- **狀態欄更正**（QA 複驗發現）：00_n / 00_l 維持 `狀態：DRAFT`（全 sibling 創建協議皆 DRAFT；「LOCKED-tier」= 四層防線審核紀律，非狀態欄）；**不翻 LOCKED 狀態**。
- **L2 收尾**：check_paths 227 baseline / check_headers **0** / check_entity_type_consistency 0 / pytest 43 — 全綠。
- **收尾動作**：user 授權「我 merge + push」→ `feat/f8p3-audit-batch5` --no-ff merge → `frontend-tools-a0f` + push origin。**整鏈已落主分支。**

## 0. 啟動前提確認（§1）
- ✅ 唯一驅動者：本對話獨佔驅動，未偵測平行 F8 commit。
- ✅ 隔離分支 `feat/f8p3-audit-batch5`（從 `f2c17ac` 起，HEAD 線見 §1）。
- 🛑 **未 merge 任何 LOCKED 改動進 `frontend-tools-a0f`**（L3 gate）。

## 1. 分支 + 每 segment commit hash + 一句話

分支 `feat/f8p3-audit-batch5`（base `f2c17ac`）：

| # | commit | segment | 一句話 |
|---|---|---|---|
| Step 0 | （併入 §6.25）| reconcile F8 編號 | 採 D-074 authoring-stack 編號為 canonical；**`BATCH4_RESUME_PHASE4-7_AUTONOMOUS` 的 Phase 4-7 編號作廢**（iterate/view/export 併入 Phase 3；「Phase 7 spec 對齊」歸 Batch 5）|
| Step 1 / 3a | `30106f3` | F8 Phase 3 core | 00_n 協議（mirror 00_l、issue-less）+ /create-org + /iterate-org + 2 wrapper + ORG card 6 段 + D-050 列 + expected_entities + ARCH §3.4 + DECISIONS §6.25 D-074 |
| Step 1 / 3b | `24d95f1` | C↔ORG endpoint | 00_l v0.3 §2.2 + create-relationship v0.4：一端可為 ORG-*（至多一端，禁 ORG↔ORG），ORG 端無聲線卡；C↔C 行為不變 |
| Step 1 / 3c | `a79d4dc` | check-gaps ORG awareness | check-gaps v0.2 加 ORG-*→/create-org；view-org + 清道夫遷移入決策佇列 |
| Step 2 | `5011b5b` | 全 repo 8 維稽核 + 自修 | GO-with-fixes；自修 M1/M2/M3-ORG/m1-m7（見 §3）；報告 `BATCH4_POSTLAND_AUDIT_REPORT.md` |
| Step 3 setup | `aff324f` | NEW_REQ_49 + D-075 | 建 entry + 拍板 registry DRY 重構 |
| Step 3 | `8cef601` | Batch 5 registry DRY | parser/scan/status registry-derived + spec-doc 雙軌 + check_entity_type_consistency.py capstone；43 tests pass |
| Step 4 | `ffe2f05` | 技術債清掃 | 修 2 HANDOFF header（check_headers 2→0）+ 06_data_structure 鏡像同步 + NEW_REQ 47/48 對齊 |
| Step 4 | `（最終稽核 commit）` | 最終全稽核 + 自修 | GO-with-fixes、7 維全綠、smoke 4/4 + falsification PASS；自修 ORG skill 三索引 drift（MAJOR）+ overclaim 措辭 + frontend pyc untrack；報告 `FINAL_AUDIT_REPORT_F8P3_BATCH5.md` |

## 2. 自我 QA 結論（兩輪稽核閉環）

### 2.1 Step 2 稽核（F8 Phase 3 land 後）— `wf_7516c2eb-692`
- **GO-with-fixes**；43 agents / 8 維 + ORG smoke **PASS** / 零無聲失敗。
- 3 MAJOR（M1 ARCH header 矛盾 / M2 view-world 懸空指標 / M3 scanner 漏掃 ORG）+ 7 MINOR 全為本批新引入，**已本輪自修**（§3）。drift 類（i1/i3/i4）歸 Batch 5。
- 詳 `_design/BATCH4_POSTLAND_AUDIT_REPORT.md`。

### 2.2 Batch 5 verify（registry DRY 重構）— `wf_96cca42d-1ca`
- **GO-with-fixes**；12 target DONE。
- `drift_eliminated = true`（check_entity_type_consistency exit 0，registry core 11 種 = 所有鏡像一致）。
- `regression_clean = true`（pytest **43 pass**；11 型別代表 ID validate_entity_id/_entity_type_from_id/ENTITY_ID_RE 行為一致；ENTITY_ID_RE 收緊僅對齊 validate_entity_id、0 真實 ID 影響）。
- `l2_clean = true`（親 stash 對拍 committed baseline：check_paths 227 / check_headers 逐字相同；delta=0）。

### 2.3 Step 4 最終全稽核（7 維全跑 + falsification）— `wf_f81550df-650`
- **GO-with-fixes（7 維全綠）**；35 agents。詳 `_design/FINAL_AUDIT_REPORT_F8P3_BATCH5.md`。
- **7 維結論**：D1 spec-enum=issues（pre-existing 殘餘→NEW_REQ_49 尾巴）/ D2 registry=clean / D3 L2=clean（三腳本全綠）/ D4 xref=**issues→已修**（ORG skill 索引 drift）/ D5 ledger=clean（未動 D-056~D-062）/ D6 backcompat=clean（C↔C 零變、非 org 零感）/ D7 phases=clean（無無聲失敗）。
- **ORG smoke = 4/4 + falsification PASS**：sandbox 刪 ORG → registry-derived ENTITY_ID_RE branch 11→10、拒 ORG-測試 ⇒ **證明 parser DRY 為真 load-bearing、非 hardcoded 鏡像**（最強回歸證據）。
- 本批引入 1 MAJOR（ORG skill 索引 drift）+ 1 INFO（overclaim 措辭）**已本輪自修**（§3）；其餘 pre-existing → NEW_REQ_49 尾巴（§5）。

### 2.4 獨立 QA 對話複驗（另一對話，只讀不改、不信自報）— `QA_HANDOFF_F8P3_BATCH5.md`
- **結論：GO（可收尾）。** §4 八項抽查全 PASS，§5 以外**無新 blocker**。
- 兩個最強客觀證據獨立複跑通過：**L2 四腳本**（check_paths 227/[OK]、check_headers 0 ERROR、lint [OK] 無 drift、pytest 43 passed）+ **falsification**（先讀 parser 機制確認 ENTITY_ID_RE 經 PEP 562 `__getattr__`→`_build_entity_id_re` 從每 entry id_pattern 動態組，再刪 ORG→重建→`ORG-x` 變 None、`C-x` 仍 match ⇒ 真 registry-derived 非硬編碼）。
- 加碼對抗檢查：base `f2c17ac` 229 → HEAD 227，**本批淨減 2 path error、零新增**。
- 不變量 5 處一致（ORG 永無聲線卡 / 不說話）、C↔C 純加性零變、LOCKED 治理只補不刪無 schema bump、帳本三方對齊、**D-056~062 未動**、未 merge。
- QA 對話對決策佇列意見：Q6 禁 ORG↔ORG 合理、B3 SPEC §5.1b「保留鏡像+marker」為最小破壞正確選擇、Q1/Q2 屬產品判斷留 master L3 拍。

## 3. 自動修了什麼（本輪）

**Step 2 稽核 confirmed findings 自修（安全可逆、本批 regression）：**
- **M1** ARCH §3.4 改了卻說「不動」→ bump v1.8 + 補變動摘要 + 修措辭（traceability）。
- **M2** view-world ORG compose 懸空指標 → 00_n §7 / iterate-org §5 改「直接讀 11_organizations/<name>.md」+ §6.25 3c views 標 DEFERRED（入決策佇列 Q5）。
- **M3** scanner 漏掃 ORG → Step 2 先補 11_organizations hardcode；**Batch 5 根治**為 registry-derived（含 10_art_assets）。
- **m1/m2** /status v0.4：修「待 Phase 3」stale + 「不在 expected_entities」假斷言。
- **m3** create-relationship 00_l ref v0.2→v0.3；**m4** iterate-org 00_j type-agnostic 基底說明；**m5** create-relationship Stage 1 C↔ORG prompt 變體；**m6** 「§13 Q6」→ DECISIONS_LOG §6.25.2 item 6；**m7** POST_LOCK NEW_REQ_32 → Phase 3 RESOLVED via D-074；**i2** 補 D-074 ref。

**Step 4 技術債清掃自修：**
- 2 HANDOFF header 補「優先級」→ check_headers 2→0 ERROR（新 L2「三腳本 exit 0」gate 成真）。
- 06_data_structure.md §1 8→11 種鏡像同步 + marker。
- NEW_REQ_47/48 → RESOLVED via D-075（consolidate NEW_REQ_49）。

**Step 4 最終稽核 confirmed findings 自修：**
- **MAJOR** ORG skill 未回填 3 索引表 → AGENTS.md + CLAUDE.md v0.7 + skill_registry_full.md B/D 列補 /create-org·/iterate-org（discovery drift 修復）。
- **INFO overclaim** → 06_data_structure / status SKILL prose 軟化：標明「parser 端鏡像由 lint 強制；spec-doc 鏡像目前 INFO，marker 待補（NEW_REQ_49 尾巴）」，不再宣稱 lint 已守護 spec-doc。
- **pre-existing 衛生** → `_tools/frontend/__pycache__/server.cpython-310.pyc` git rm --cached（完成 3fa3c63 partial untrack；tracked pyc 歸零）。

## 4. 🟦 決策佇列（最重要 — 待你拍板）

> 全部採安全可逆預設先做、入此佇列；**Q1/Q2/Q6 的預設已寫進 00_n/00_l schema**。
> **⚠️ 更正（QA 複驗發現）：** 原稿多處寫「拍板後把 00_n/00_l 由 DRAFT 翻 LOCKED」**不正確** —— 全 repo 所有創建協議（00_e/00_f/00_g/00_h/00_l）狀態欄**皆為 DRAFT**；「LOCKED-tier」指**四層防線審核紀律**（governance），不是 `狀態：` 欄。00_n/00_l 狀態應**維持 DRAFT**（比照所有 sibling 協議），**不翻 LOCKED 狀態欄**（翻了會與全部 sibling 不一致、且可能誤導對 LOCKED 特殊處理的 scanner/skill）。
> 建議**先拍 Q1/Q2/Q6 ratify 設計再 merge**（趁 user 尚未拍板、下游尚未依賴時改判最省）；狀態欄不動。

### 4.1 D-074 §13 七題（F8 Phase 3）
| # | 問題 | 採的預設 | 可選項 |
|---|---|---|---|
| Q1 | ORG card 段數 | **6 段**（組織本質/對抗性質/殘留型態/影響範圍/下游 hooks/文件語體 hint）| 加「組織結構/層級」段？|
| Q2 | 00_n issue-less | **issue-less**（不加 registry skill key，比照 /iterate-scene）| 加 `core.00_n_organization` issue list（多一 LOCKED registry 觸點）|
| Q3 | 單一 D-074 | **單一 umbrella 收全部** | 拆多號 |
| Q4 | create-relationship endpoint | **本批做（3b 已落地）** | 延後獨立批 |
| Q5 | view-org 獨立 | **不獨立、DEFERRED**（先直接讀 11_organizations/；獨立 view-org/export-org + view-world ORG compose 待後續批）| 本批補 view-world ORG 段 / 建獨立 view-org |
| Q6 | ORG↔ORG 關係 | **不允許**（至多一端 ORG）| 允許 ORG↔ORG |
| Q7 | 方向 B（W-language 文件語體卡）| **仍延後**（Phase 3 只留 §6 hint hook）| 本批做方向 B |

### 4.2 D-075 / Batch 5 spec-doc 策略
| # | 問題 | 採的預設 | 可選項 |
|---|---|---|---|
| B1 | spec-doc 策略 | **保留鏡像 + drift-lint 雙軌**（列舉補 11 + 標「權威見 registry」marker）| 純指標（移除列舉）|
| B2 | drift-lint 納入本批 | **納入**（check_entity_type_consistency.py capstone）| 延後 |
| B3 | SPEC §5.1b LOCKED doc-sync | 採安全 doc-sync（補 W-style+ORG，無 schema_version bump、無列舉刪除）；**待你 L3 確認為 doc-sync 非契約變更** | 視為 LOCKED 契約變更需正式拍板 |
| B4 | spec-doc `<!-- REGISTRY-MIRROR -->` marker 全強制 | **暫不**（lint 目前 INFO；marker 全強制 = NEW_REQ_49 尾巴）| 本批補 marker 啟用機器 ERROR 比對 |
| B5 | skill-generic 殘餘（每 SKILL 內文全 registry-generic）| **續記 NEW_REQ_49 尾巴**（回報遞減）| 本批做 |

## 5. 🗂 技術債 / backlog 清單（Step 4 清掃結果）

**(a) 程式/協議/文件殘留標記：** ✅ 零新增 active TODO/INFERENCE/CONFLICT。grep 確認 F8 Phase 3 + Batch 5 新增檔僅含 marker **格式範本**（`<!-- INFERENCE: <依據>; 待人類確認 -->` 等 placeholder，屬 skill 指示 agent 用法），非 active debt。
**(b) 決策佇列：** §4 全部（D-074 §13 七題 + D-075 B1-B5）。
**(c) workflow INFO/MINOR backlog（NEW_REQ_49 尾巴 / 留痕）：**
- spec-doc `<!-- REGISTRY-MIRROR -->` marker 未落地（lint 目前 INFO，硬比對 0/3）→ NEW_REQ_49 尾巴（marker 補上後 lint 自動納入機器強制 ERROR 比對）。
- **W-style/ORG 列舉殘餘未收斂**（Batch 5 §2 scope 縮減未含；最終稽核 D1 點名）：`L3_EXPORT_PROMPT_SCHEMA §79/81/96`（export full-scope 掃描指令）、`_user_manual/07_customization.md` L46/L72（core 8 vs 9 自相矛盾）、`IC:1311` + `UX_SPEC:2617`「7 entity types」、`UPSTREAM_DOWNSTREAM_SPEC:5863`「7 種敘事 entity」→ NEW_REQ_49 尾巴 W-style/ORG sweep。
- `server.py:458` OUTLINE_ENTITY_TYPES 第三鏡像不在 lint scope（rglob *.md 掃不到 .py）→ NEW_REQ_49 尾巴。
- DATA_FORMAT_SPEC appendix 殘留 count / DFS §7.2 yaml inline 註解 → 下輪 full count sweep。
- DECISIONS_LOG §7 摘要 §6.26/§6.25 局部逆序（cosmetic，與既有 §6.13/§6.14 同型）→ 日後 cleanup。
- C-ORG 裸名 ID 碰撞（i4，需 C 與 ORG 同名 contrived 前提，非現行 bug）→ NEW_REQ_49 觀察項。
**(d) 待清理 / superseded doc：**
- `BATCH4_RESUME_PHASE4-7_AUTONOMOUS.md` 的 Phase 4-7 編號**已作廢**（Step 0 reconcile；其 iterate/view/export 併入 Phase 3）→ 建議標 DEPRECATED 或註明編號作廢。
- 本檔 `OVERNIGHT_RUN_F8P3_AUDIT_BATCH5.md`（過夜計畫）+ 本 wake-up 報告：L3 收後可標 APPLIED/DEPRECATED。
- `D074_DECISION_PACKAGE.md`（草案，§13 已拍）：L3 收後可標 APPLIED。
**(e) 刻意延後殘餘：**
- F8 **方向 B**（W-language 文件語體卡，~5-8h）— DEFERRED；ORG card §6 只留 hint。
- Batch 5 **skill-generic 殘餘**（每 SKILL 內文全 registry-generic）— NEW_REQ_49 尾巴。
- **view-org / export-org 獨立 skill + view-world ORG compose**（§4 Q5）— DEFERRED。
- **清道夫 R-* opt-in 遷移**（user 明示才做：/create-org ORG-清道夫 → 舊 R-* 標 DEPRECATED）— DEFERRED。
- **10_art_assets header 稽核**：Batch 5 已納 scan-scope，但 10_art_assets 缺檔引用走 FUTURE→INFO（A-* 量產晚期才填）。

## 6. 🛑 L3 + rule-4 簽字請求

**LOCKED 觸點清單（全有 D-074 / D-075 背書）：**
1. 新 `00_protocol/00_n_組織創建協議.md`（D-074；狀態 DRAFT，比照所有 sibling 協議維持 DRAFT；LOCKED-tier 指審核紀律）。
2. `00_protocol/00_l_關係創建協議.md` v0.3 ORG-endpoint（D-074）。
3. `_design/DECISIONS_LOG.md` D-050 子裁決 2 表 append /create-org 列（D-074）。
4. `_design/ARCHITECTURE.md` v1.8 §3.4（D-074；純新增列）。
5. `scripts/parse_frontmatter.py` registry-derived（D-075；regression 紅線守住）。
6. `_design/DATA_FORMAT_SPEC.md` v0.5 + `_design/SPEC.md` v1.3 §5.1b spec-doc 雙軌（D-075；**SPEC §5.1b 需你確認 doc-sync 性質，見 §4.2 B3**）。

**抽查指引（REVIEW_LOOP §2；真抽查才有效）：**
1. **LOCKED 治理**：`git -C "D:/劇本開發工具" diff f2c17ac HEAD -- _design/ARCHITECTURE.md _design/SPEC.md _design/DATA_FORMAT_SPEC.md` — 確認列舉只補不刪、無 schema_version bump、header 版本與內容一致。
2. **§13 merge 前 ratify 三題**：Q1（6 段）/Q2（issue-less）/Q6（禁 ORG↔ORG）—— 趁尚未拍板/下游未依賴時改判最省；**狀態欄維持 DRAFT，不翻 LOCKED**（更正見 §4 開頭）。
3. **親跑 L2 三腳本**（cwd repo，`PYTHONIOENCODING=utf-8 PYTHONUTF8=1`）：
   - `python scripts/check_paths.py --baseline 227` → exit 0
   - `python scripts/check_headers.py` → 0 ERROR
   - `python scripts/check_entity_type_consistency.py` → exit 0、`[OK] 無 drift`
   - `python -m pytest scripts/tests/ -q` → 43 passed
4. **抽 1 PASS 檔複看**：`git diff scripts/parse_frontmatter.py`（_build_entity_id_re / registry-derived；ENTITY_ID_RE 不再硬編碼）。
5. **view-world ORG 抽查**：確認 M2 已改指標（不會指引跑 /view-world 看空 ORG）。

## 7. Merge 指示（簽字後）
```
# 簽字 + Q1/Q2/Q6 ratify 後（狀態欄維持 DRAFT，不翻 LOCKED）：
git -C "D:/劇本開發工具" checkout frontend-tools-a0f
git -C "D:/劇本開發工具" merge --no-ff feat/f8p3-audit-batch5
git -C "D:/劇本開發工具" push origin frontend-tools-a0f
```
（feature 分支可先 push 供審：`git push -u origin feat/f8p3-audit-batch5`。）

## 8. ⚠️ 明確聲明
**尚未 merge 進主分支 `frontend-tools-a0f`。** 全鏈 park 在 `feat/f8p3-audit-batch5`，等你 L3 真抽查簽字 + §4 決策佇列拍板。agent 不代簽、不自行 merge LOCKED 改動。

## 9. Cross-ref
- `OVERNIGHT_RUN_F8P3_AUDIT_BATCH5.md`（過夜計畫）/ `BATCH4_POSTLAND_AUDIT_REPORT.md`（Step 2 稽核）
- `D074_DECISION_PACKAGE.md`（F8 Phase 3 設計 + §13）/ `BATCH5_REGISTRY_DRY_REFACTOR.md`（Batch 5）
- DECISIONS_LOG §6.25 D-074 + §6.26 D-075 / POST_LOCK NEW_REQ_32/47/48/49
- workflow runs：`wf_7516c2eb-692`（Step 2）/ `wf_96cca42d-1ca`（Batch 5）/ `wf_f81550df-650`（最終稽核）
