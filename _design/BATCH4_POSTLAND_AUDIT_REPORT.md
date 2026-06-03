狀態：DEPRECATED
版本：v1.0（F8 Phase 3 land 後全 repo 8 維對抗式稽核 + ORG smoke test；workflow wf_7516c2eb-692，43 agents / 2.23M token / 596 tool uses）
最後更新：2026-06-03
適用範圍：feat/f8p3-audit-batch5（Step 2 稽核結論；餵 Step 3 Batch 5 + Step 5 wake-up）
優先級：高

# BATCH4 POST-LAND 稽核報告 — F8 Phase 3 ORG authoring stack

## 1. 一句話總評

**GO-with-fixes** — F8 Phase 3 核心功能（registry / parser / create-org / iterate-org / create-relationship C↔ORG / expected_entities / check-gaps）逐項驗證為真實落地、ORG smoke test 全綠、零「commit 宣稱但檔案落空」無聲失敗；本批引入 3 個 MAJOR 收尾缺口 + 多項 MINOR，**已於本輪（commit 後述）全數自修**；INFO/drift 類歸 Batch 5（NEW_REQ_48/49）。

## 2. Confirmed Findings（去重後）

### MAJOR（本輪須修，已修）
- **M1 ARCH §3.4 改了卻說沒改**：commit 30106f3 實質改 LOCKED v1.7 ARCH §3.4（/iterate-* 5→6 + append /create-org 列），但 header 仍寫「§3.4 全部不動」、版本未升。→ 本輪修：bump v1.8 + 補變動摘要 + 修「不動」措辭。
- **M2 view-world ORG compose 承諾未兌現**：D-074 §6.25 3c 列「view-world compose ORG」，00_n §7 + iterate-org §5 已無條件指引跑 /view-world，但 view-world 0 ORG awareness。→ 本輪修（採 b）：兩處指標改「ORG compose 待後續批；目前直接讀 11_organizations/<name>.md」+ §6.25 3c「views」標 deferred + 入決策佇列。
- **M3 scanner 漏掃 11_organizations/**：check_paths/check_headers 掃描清單無 11_organizations（也無 10_art_assets）；PATH_RE 前綴 0[0-9]_ 無法匹配 1X_。→ 本輪修 ORG 部分（補 11_organizations 至清單 + PATH_RE）；10_art_assets + registry-driven 動態衍生 → NEW_REQ_49 / Batch 5。

### MINOR（本批 regression，已修）
- **m1** /status 三處「待 Phase 3」stale-ref（/create-org 已 live）→ 改 live + bump v0.3。
- **m2** /status「ORG 不在 expected_entities」斷言已成假（Phase 3 已加 create_org block）→ 改述 + 補 Stage-3 列。
- **m3** create-relationship line 42/53 引 00_l v0.2（應 v0.3）→ 改 v0.3。
- **m4** iterate-org 引 00_j v0.2 但 00_j 無 ORG，與 ARCH §3.4 衝突 → 軟化 ARCH §3.4 措辭 + iterate-org 註明 00_j 為基底。
- **m5** create-relationship Stage 1 prompt 未鏡像 00_l v0.3 C↔ORG 變體 → 補條件變體 prompt（C↔C 路徑不變）。
- **m6** 00_l / create-relationship 引「§13 Q6」溯源錯指 → 改引「DECISIONS_LOG §6.25.2 item 6」。
- **m7** POST_LOCK NEW_REQ_32 未隨 D-074 更新 → 改「Phase 3 RESOLVED via D-074」+ bump v0.37。

### INFO（歸 Batch 5 / 無需動作）
- **i1** DATA_FORMAT_SPEC / SPEC §5.1b / IC / UX_SPEC / manual 多處「7 種/8 種」列舉缺 W-style+ORG（registry 實 11）—— pre-existing drift（D-055/D-071），非本批 regression → **NEW_REQ_48 / Batch 5**。
- **i3** ARCH「7 種敘事 entity」/ L3_EXPORT「所有 entity」語意缺 ORG（邊界案例）→ Batch 5。
- **i4** _entity_type_from_id 無顯式 ORG branch（靠 split fallback，test pin）/ core target_dir 不在 load 時驗存在 / R-<a>-<b> 裸名跨 C/ORG namespace 潛在碰撞（非現行 bug）→ **NEW_REQ_49 / Batch 5**。
- **i5** DECISIONS_LOG §7 摘要行局部逆序（cosmetic，pre-existing）→ 日後 cleanup。
- **i6** §13 七題已 park 等 user 拍，但 Q1/Q2/Q6 預設已寫進 DRAFT 00_n/00_l schema → L3 抽查重點（翻 LOCKED 前先拍）。

## 3. Smoke Test：PASS（端到端真實執行）
- ORG-測試 fixture 在 _sandbox 實跑 parse_frontmatter：validate_entity_id 通過、_entity_type_from_id=="ORG"、registry resolve → 11_organizations/、build_repo_index 收錄。
- 非 org control（C-對照）零 delta；無 org sandbox 行為零變動。生產 template 未動、scratch 清乾淨。
- 結論：parser/registry 層對 ORG 核心契約健全、無 regression；M3 為 L2 *腳本* 層問題，與 parser 正交。

## 4. F8 Phase 3 L1 結論（D8）
**L1 = GO-with-fixes → 本輪自修後轉 PASS。** 核心交付物逐項真實落地、無無聲失敗；3 MAJOR 收尾缺口為本批新引入（非 pre-existing drift），已於本輪補齊。§13 處置（park + 全入決策佇列 + panel 1/3 誠實揭露）通過審核標準。

## 5. 給 user 的 L3 抽查指引
1. **LOCKED 治理**：ARCH header v1.8 是否與 §3.4 內容一致（M1 修補兌現）。
2. **§13 park 預設改判成本**：Q1（6 段 card）/Q2（issue-less）/Q6（禁 ORG↔ORG）預設已寫進 00_n/00_l **DRAFT** schema；**先拍這三題再把 00_n/00_l v0.3 翻 LOCKED**（趁 DRAFT 改判最省）。
3. **view-world ORG**：確認 M2 採 (b) 改指標 + §6.25 3c 標 deferred（view-org 入佇列）。
4. **L2 防線**：建一張壞 header ORG 卡測 check_headers 是否報錯（驗 M3 修補）。
5. **drift sweep 邊界**：確認 i1 只進 NEW_REQ_48/49、本輪未就地改任何 LOCKED spec。
6. **L3 簽字有效性**：1/2 涉 LOCKED 與協議翻鎖，務必親眼看檔後再簽（REVIEW_LOOP §2）。

## 6. Cross-ref
- workflow run `wf_7516c2eb-692`（full result：tasks/w8e854qx0.output）
- `BATCH4_POSTLAND_AUDIT.md`（§5 workflow 來源）/ `D074_DECISION_PACKAGE.md` §13
- Batch 5 worklist：本報告 §2 INFO i1/i3/i4 + M3 registry-driven + 10_art_assets → `BATCH5_REGISTRY_DRY_REFACTOR.md` / NEW_REQ_48 / NEW_REQ_49
