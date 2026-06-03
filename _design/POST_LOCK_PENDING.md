狀態：DRAFT
版本：v0.37（11th master frontend 過夜自主長跑 — F8 Phase 3 落地（D-074）— NEW_REQ_32 bracket 更新：Phase 3 已 RESOLVED via D-074（00_n 協議 + /create-org + /iterate-org + ORG card 6 段 + 00_l v0.3 C↔ORG endpoint + D-050 列 + expected_entities + ARCH §3.4 v1.8 + check-gaps v0.2 + 掃描清單補 11_organizations）；3c views + 清道夫遷移 DEFERRED；§13 七題入決策佇列、park 在 L3；DECISIONS §6.25；本檔 v0.36 → v0.37。Batch 5 NEW_REQ_49 見檔尾）
歷史紀錄：v0.35（Batch 4 — F8 ORG-* core Phase 1 落地 partial supersede — NEW_REQ_32（F8 長線 direction A）→ ✅ RESOLVED via D-071（registry root+template append ORG 型別 + parser ENTITY_ID_RE/_entity_type_from_id 加 ORG/W-style + ORG regression test 4/4；ORG-* 成 valid LOCKED core；spec 本批不改 — core 權威為 registry，§7.6/§5.1b 列舉 drift 入 NEW_REQ_48 追蹤）；Phase 2/3 後續批；parser W-style drive-by 部分解 NEW_REQ_47 + 新開 NEW_REQ_48（spec-doc 列舉 drift）；feat/batch4-entity；LOCKED-tier 走四層防線 + QA wf_9ef532f0 + DECISIONS_LOG §6.23 D-071；本檔 v0.34 → v0.35）
歷史紀錄：v0.34（Batch 4 hygiene — (1) NEW_REQ_38（F14）DEFERRED → ✅ RESOLVED 狀態核對同步（F14 已於前批落地：CLAUDE 瘦身 + AGENTS 205→~127 + skill_registry_full.md；minimal-list 採選項 c）+ (2) 新增 NEW_REQ_47（parser entity-type 硬編碼鏡像應 registry-derived；tech-debt DEFERRED）；另 git rm --cached 2 個 tracked .pyc（已在 .gitignore）；本檔 v0.33 → v0.34）
歷史紀錄：v0.33（Batch 4 — registry 損壞修復落地 partial supersede — 新增 NEW_REQ_46（root entity_type_registry.yaml 無法 parse）→ ✅ RESOLVED via D-073（刪 line 94-98 重複孤兒尾段、最小 truncate；root core 與 template core deep-equal；純機械 0 設計改動）；含評審更正「root 並未缺 W-style」；feat/batch4-entity；LOCKED-tier 走四層防線 + DECISIONS_LOG §6.22 D-073；F8/NEW_REQ_32 ORG-* core（D-071）設計已拍板待 Phase 1；本檔 v0.32 → v0.33）
歷史紀錄：v0.32（Batch 4 — F10 副對話 lifecycle UX 落地；NEW_REQ_34 DEFERRED → RESOLVED via D-072；ARCH v1.6 → v1.7 §3.3.3 + AGENTS/CLAUDE v0.6/skill_invocation_guide v0.2 短指標；DECISIONS §6.21；接 Batch 2 v0.31 之後；本檔 v0.31 → v0.32）；v0.31（Batch 2 NEW_REQ_41/42 RESOLVED via D-067 pattern pack；本檔 v0.30 → v0.31）；v0.30（Batch 2 NEW_REQ_40/43 RESOLVED via D-069/D-068；本檔 v0.29 → v0.30）；v0.29（Batch 3 工具衛生落地 partial supersede — F2/F4/F5/F15 → NEW_REQ_26/28/29/39 全 RESOLVED；F2 check_paths CLI flag（--changed-only/--base/--baseline/--suppress-template-debt）/ F4 header 尾空白 strip（53 檔純空白，git diff -w 證明零語意變更，rule-4 user 核准）/ F5 template_commit 偵測守衛（L1 抓 MAJOR：Instance HEAD ≠ Template commit，已加守衛）/ F15 parser 裸 --- 防呆；feat/batch3-hygiene；零-LOCKED 語意、無 D-NNN；L0→L1 workflow wf_32930e84→L2→L3 簽字全跑；本檔 v0.28 → v0.29）
歷史紀錄：v0.28（11th master frontend Wave2 落地紀錄 partial supersede — (1) NEW_REQ_31(F7)/32(F8)/33(F9)/36(F12) → ✅ RESOLVED(Wave1)；NEW_REQ_35(F11)/37(F13) → ✅ RESOLVED(Wave2) + 補 WI-B/WI-C 落地紀錄 + Cross-ref + (2) 乾淨編號更正：NEW_REQ_31 依賴 D-057 → D-063 / NEW_REQ_32 依賴 D-058 → D-064（對話 B 預留 D-056~D-062，本批改用乾淨段 D-063~D-066；D-057/D-058 在本批作廢）+ (3) 誠實揭露升格：NEW_REQ_33/35/36/37 原『不需 D-NNN』更正為『升格 D-065/D-066』（落地觸及 LOCKED UD §1.2.2 + 00_f + registry）；對應 DECISIONS_LOG v2.2 §6.19 D-063~D-066；不動對話 B 的 D-056~D-062 預留帳；本檔 v0.27 → v0.28）
歷史紀錄：v0.27（11th master frontend dialogue 後續 reconciliation partial supersede — 修 v0.26「前端」merge commit `92356f8` 引入的結構 regression：(1) **去重 NEW_REQ_44**（移除對話 A 置於 NEW_REQ_35 後的離序重複版 @原 1650；保留 D-062-aware 內容、置於 NEW_REQ_43 後成數字序）+ (2) **去重 NEW_REQ_45**（移除對話 A 離序版 @原 1679，該版尾段 corruption 混入 NEW_REQ_35/F11 殘留 `parse_frontmatter docx`/Wave-A3/§3.11；保留乾淨完整版、置於 44 後）+ (3) **更正 v0.26 header §5 誤判**：v0.26 (4) 稱「§5『評估紀錄總表』為歷史 phantom / body 從未寫入 / 不另建 §5.22」**為誤述** — 實際 §5 section 自 v0.24（commit 016137d）起即完整存在於 body（§5.1–§5.22），§5.22 亦已寫入（line ~2334）；本 v0.27 更正此誤判，§5 body 不動 + (4) **HANDBACK_POST_LOCK_RECONSTRUCTION.md v0.1 已 stale**：其缺口 A（NEW_REQ_36-43 缺失）+ 缺口 B（§5 phantom）皆不成立（36-43 由對話 B commit `08605a7`/v0.25 寫入完整 body；§5 自 v0.24 存在）；故未執行該 handback 任務 A/B（盲做會三份化 36-43），改做實際需要的去重；不動 36-43 / §5 body；本檔 v0.26 → v0.27）
歷史紀錄：v0.26（11th master frontend dialogue cycle wrap-up partial supersede — (1) NEW_REQ_20 BLOCKED → RESOLVED（前端 F1-2 module row CopyCommandButton + F1-3a 三欄區對齊 §11.1.6 落地；F1-3b backend 拆 NEW_REQ_44）+ (2) NEW_REQ_24 DEFERRED → RESOLVED via Option 1（hyphen → underscore 統一 ~26 canonical/runtime refs；不動 LOCKED spec）+ (3) 新增 NEW_REQ_44（backend pending-status endpoint + 3 schema；OPEN）+ NEW_REQ_45（frontend scope-C reframe；DEFERRED 待 user 外接寫作反饋）+ (4) frontend cycle 收尾紀錄落於 _design/AUDIT_2026Q2_REPORT.md §9（本檔 §5「評估紀錄總表」結構為歷史 phantom — §5.3-§5.21 僅存在於 header 版本註記、body 從未實際寫入；故不另建 §5.22）；本檔 v0.25 → v0.26 ※ **對話 A 2026-06-01 patch：補入 NEW_REQ_44 / NEW_REQ_45 entry body（原 v0.26 header 宣稱已開但 body 未寫）+ 修本 (4) 不實 §5.22 陳述 + 補完 NEW_REQ_35 截斷殘句；詳檔尾 NEW_REQ_35 errata**）
歷史紀錄：v0.25（11th master 對話 B M4 user-test follow-up sub-scope wrap-up partial supersede — (1) 新增 NEW_REQ_25-43（19 entries 對應 F1-F19；2026-05-25~2026-06-01 量產期間 16 user-report verify 後拆 19 distinct finding；分 5 大 meta-pattern：A Phase A→B chain coherence / B /create-character 5-step pipeline / C CLI lint parser / D Agent context UX / E Outline 層品質）+ (2) 新增 §5.20 11th master 對話 B M4 follow-up 評估紀錄總表（19 NEW_REQ 評估 + Wave-A1~A6 分組 + α/β/γ/δ 4 scope option 工時）+ (3) 新增 §5.21 升 v0.25 紀律 + (4) D-NNN candidate D-056~D-061 預留；對應 _design/M4_USER_TEST_REPORT.md v1.0 + 5 採納 transcribe-ready for Claude Code workflow Stage 2/3；本檔 v0.24 → v0.25）
歷史紀錄：v0.24（11th master 對話 A second-run audit transcribe + frontend handoff partial supersede — §5.18 second-run + §5.19 紀律 + NEW_REQ_24 + NEW_REQ_22 first+second cycle 完成）；v0.23（11th master 對話 A first-run audit transcribe partial supersede — §5.16 first-run transcribe + §5.17 升 v0.23 紀律 + 落地 5 patch batch）
歷史紀錄：v0.22（11th master 對話 A reframe 戰略落地 partial supersede — restore §5.3-§5.12 + 新增 NEW_REQ_22 + NEW_REQ_20 BLOCKED + §5.13/§5.14/§5.15）
歷史紀錄：v0.21（10th master 第十輪 D-055 拍板 partial supersede — pre-generation 文風錨定機制後續維護新增 NEW_REQ_21 PROCESSING（9 子項：5 項 RFC §10.5 + §11.2 + 3 項 RFC §11.1 風險追蹤 + 1 項 T10 inventory carry-over）；對應 STYLE_ANCHOR_PROPOSAL v0.1 + STYLE_ANCHOR_IMPL_STARTER v0.1 + DECISIONS_LOG §6.18 D-055）；v0.20（10th master 第十輪整合對話 M4 user-test follow-up 新增 NEW_REQ_20 — Phase A.0F F1 Dashboard 三欄區 spec drift + data 過時 + 模組狀態入口待後續 UI 三條 finding；推 11+ 輪 master patch）；v0.19（10th master 階段 6 NEW_REQ deferred backlog 重新評估 partial supersede — §5 評估總表 10 個 subsection 涵蓋 NEW_REQ_9/11/14/15/16/17/18 + 19 確認）
歷史紀錄：v0.18（9th master Round 4 NEAR-GO hard-limit accept — R4-MAJOR-01 屬 diff anchor 設定問題；CODEX 已用 `HEAD~1..HEAD` 確認真實 scope 乾淨；屬 starter wording 設計缺陷不是 spec regression；加教訓內化第 5 條「Master 寫 review starter 時 diff anchor 必須精確」；9th master Round 1-4 review cycle 完整收尾）；v0.17 為 Round 3 trivial inline patch；v0.16 為 Round 2 inline patch round；v0.15 為 Round 1 inline patch round；v0.14 為 9th master cleanup queue 處理
最後更新：2026-06-02
適用範圍：LOCKED 後新出現的需求 / 設計缺漏 / 後續修補項紀錄
優先級：中


# POST_LOCK_PENDING — 升 LOCKED 後新需求清單

# 0. 本檔用途

設計階段（10 spec）於 2026-05-19 升 LOCKED 後，user / CODEX / Phase A.0+ 實作過程**新發現的需求 / 缺漏 / 修補項**集中紀錄於此。

**本檔不是 LOCKED**，可持續追加。各項處理時機標示清楚（D-047+ / Phase X / 持續寫作）。

**累積一定量後，觸發 master 第五輪整合對話**（升 INTEGRATION_CONTRACTS v2.1+ + 主 SPEC v1.2+ partial supersede）。

---

# 1. 新需求清單

## NEW_REQ_1 議題清單 registry（候選 D-047）

**狀態：** ✅ **RESOLVED via D-047**（master 第五輪 2026-05-19 拍板 + `_design/registries/issue_type_registry.template.yaml` v0.1 LOCKED + IC v2.1 §4a Contract D 落地；詳 DECISIONS_LOG §6.9.2）

備註：實際 yaml key 命名依 UD LOCKED 權威修正為 `00_e_world / 00_f_character / 00_g_outline / 00_h_detailed_outline / 00_l_relationship`（v0.1 提議方案的 yaml key `00_g_relationship / 00_h_outline / 00_l_detailed_outline` 對應錯位由 D-047 同時 supersede）；議題定義改為 user-facing only（10+8+6+6+6 = 36 議題；拆分規則為 agent 階段 4 mechanic 不入 registry）。

**需求背景（2026-05-19，user 提出）：**
- 既有 5 個 /create-* skill 的議題清單（11/9/6/7/7）在 LOCKED 設計中 hardcode 在 UD §1.1-§1.5
- user 希望：每個專案可依類型增減 / 微調議題（例：恐怖類加「驚悚密度曲線」、純愛類刪「越界禁區」）
- 現有 entity_type_registry / qa_type_registry 已建立可擴充 pattern，**議題清單缺對應 registry**

**提議方案：**

新增 `issue_type_registry.yaml`（位置 `_design/registries/` Template + Instance root）：

```yaml
# issue_type_registry.template.yaml
version: 1
schema_version: data_format_spec_v0.2

core:
  00_e_world:
    - id: 1
      name: 世界類型快速分類
      required_level: REQUIRED
      locked: true
    - id: 2
      name: 世界規則最小集
      required_level: REQUIRED
      locked: true
    # ... 11 個議題
  00_f_character:
    # ... 9 個議題
  00_g_relationship:
    # ... 6 個議題
  00_h_outline:
    # ... 7 個議題
  00_l_detailed_outline:
    # ... 7 個議題

user_extensions:
  00_e_extra:
    []   # user 可加自訂議題
  00_f_extra:
    []
  # ...

core_overrides:
  00_e_skip:
    []   # user 可標 SKIP 既有議題（如純愛遊戲跳過議題 6 宗教）
  00_f_skip:
    []
  # ...
```

**parser 行為：**
- /create-* skill 啟動時讀 `<instance_root>/issue_type_registry.yaml`
- 議題清單 = core 議題 + user_extensions - core_overrides
- 議題順序：先 core（依編號）後 user_extensions
- 對 LOCKED `core[*].locked: true` 議題禁止跳過（user_extensions 才可彈性增減）

**對既有 spec 的影響：**
- UD §1.0.4 / §1.1-§1.5 議題清單描述改為「參考 issue_type_registry — 此處為 core 議題範本」
- 5 個 /create-* skill 實作要讀 registry（屬 Phase B 任務）
- 前端工具加 issue registry 編輯 UI（屬 Phase A.0F 後續任務）

**預估工時：**
- master 第五輪拍板 + 升 D-047 + 升相關 spec：2-3 小時對話工時
- Phase B /create-* skill 實作讀 registry：1-2 天
- 前端 issue registry 編輯 UI：1-2 天

**對 Phase A.0.1 開工影響：** **無**（parser 基線不需知道議題 registry）

**進入機制：** Phase A.0 9 個 parser sub-task 全完成後 → 開新 master 第五輪整合對話 → 拍板 D-047 → 補 issue_type_registry.yaml Template

---

## NEW_REQ_2 完整使用說明書

**狀態：** 持續寫作中 — 已建第一版骨架（11 章）於 `_user_manual/`

**需求背景（2026-05-19，user 提出）：**
- 工具完成後可能有大量隱藏功能 user 不知道
- 需要一份統一的使用說明書避免忘記如何用
- 涵蓋所有 26 skill + 前端工具 + 隱藏功能 + 客製化 / 故障排除

**位置：** `_user_manual/`（不在 `_design/` 內 — manual 是 user-facing，跟設計層獨立）

**章節結構（11 章 + 5 workflow 子檔）：**

| # | 檔 | 完成度 |
|---|---|---|
| 00 | quick_start.md | ✅ v0.1 完整（10 分鐘上手）|
| 01 | tool_overview.md | ✅ v0.1 完整（工具定位 + 三層架構 + 26 skill 表）|
| 02 | upstream_skills.md | 🔄 骨架（Phase B/C 完成後補）|
| 03 | downstream_skills.md | 🔄 骨架（Phase D 完成後補）|
| 04 | management_skills.md | 🔄 骨架（Phase A.0 完成後補）|
| 05 | frontend_tools.md | 🔄 骨架（Phase A.0F 完成後補）|
| 06 | data_structure.md | ✅ v0.1 完整（lock 過的 schema）|
| 07 | customization.md | ✅ v0.1 完整（registry 機制；D-047 後補議題客製化）|
| 08 | workflows/（5 子檔）| 🔄 骨架（各 phase 完成後補真實案例）|
| 09 | advanced.md | 🔄 骨架（隨開發補）|
| 10 | faq.md | ✅ v0.1 完整 |
| 11 | troubleshooting.md | ✅ v0.1 完整 |

**更新時機：**
- 每完成一個 phase / skill 就同步更新 manual 對應章節
- 不等到最後才寫（避免遺忘）
- 每次 manual 更新走輕量 commit（不需要 master 對話介入）

**Manual 是否 LOCKED：** 不 LOCKED — 是 living document，持續更新

---

# 2. 後續更新區（保留）

未來新需求 / 設計缺漏在此追加：

## NEW_REQ_3 deleted KEY 內文存在性處理細化（minor）

**狀態：** ✅ **RESOLVED**（master 第五輪 2026-05-19 — 拍板補 WARN「該 KEY status=deleted，建議從內文移除」；落地 DF v0.4 §11.1.2；實作時機由 Phase A.X 後續 patch 補；詳 DECISIONS_LOG §6.9.3）

**時點：** 2026-05-19  
**提出者：** CODEX A.0.2 spec interpretation question

**需求背景：**
- DF §4.5 描述 `status: deleted` 語意為「內文整段移除」
- 但 DF §11.1.2 parser 行為只要求 `deleted_at` 必填；沒明示「內文必須移除」為 parser validation rule
- A.0.2 實作採寬鬆解讀：允許 deleted KEY 內文仍存在（漸進刪除友善），順序檢查照常含
- master 第四輪拍板接受此寬鬆解讀

**未決細節（可在 master 第五輪細化）：**
- 是否補 WARN「該 KEY status=deleted，建議從內文移除」？
- 還是維持寬鬆（不警告）？
- 前端 Editor 顯示 deleted KEY 的策略（已在 UX §11.2.9 / §11.3.4 規範為灰色+刪除線）— parser 是否該幫前端標記？

**處理時機：** Phase A.0 全 sub-task 完成後 → master 第五輪整合可一起處理（minor 細化，不擋 LOCKED 升版）

---

## NEW_REQ_4 DF §7.2 Template 範例殘留（minor — LOCKED 後發現）

**狀態：** ✅ **RESOLVED**（master 第五輪 2026-05-19 — DF v0.3→v0.4 partial supersede；§7.2 + §8.2 + §8.3 + §9.1 同類擴充 cleanup 全部對齊權威 template；詳 DECISIONS_LOG §6.9.4）

**時點：** 2026-05-19  
**提出者：** CODEX A.0.7 spec interpretation question

**需求背景：**
- DF §7.2 Template schema 範例 (line 1492 + 1548) 仍是 v0.1 寫法：
  - `schema_version: data_format_spec_v0.1`（應為 v0.3）
  - A subtype `id_pattern: ^A-(portrait|bg|cg|icon|effect)-.+-.+$` + allowed_values 列 5 種（應為 7 種 portrait/bg/cg/sfx/bgm/voice/ui）
- DF §5.1a v0.2 patch 已採 7 subtype + reserved_subtypes（D-044 拍板）
- DF §7.2 範例段沒同步更新 — partial supersede 殘留

**A.0.7 採對齊處理（CODEX 判定正確）：**
- 實作 `_design/registries/entity_type_registry.template.yaml` 採 `data_format_spec_v0.3` + 7 subtype + `icon/effect/video/shader` 放 reserved_subtypes
- 對齊 D-044 + DF §5.1a v0.2 patch + Contract A.3

**處理時機：** master 第五輪整合（在 A.0.9 後）跟 D-047 一併處理；DF §7.2 範例段補 supersede 註記 + 對齊 v0.3 寫法

---

## NEW_REQ_5 target_dir 多目錄 schema 不嚴謹（minor）

**狀態：** ✅ **RESOLVED**（master 第五輪 2026-05-19 — 採推薦選 b 維持 csv 字串 + schema 明示 comma-separated；落地 DF v0.4 §7.3；entity_type_registry.template.yaml 不動；詳 DECISIONS_LOG §6.9.5）

**時點：** 2026-05-19  
**提出者：** CODEX A.0.7 spec interpretation question

**需求背景：**
- DF §7.2 Template `S.target_dir` 是逗號分隔字串：`06_scene_index/, 07_scene_tasks/, 08_dialogue_outputs/`
- Schema 定義為 single string but 實際是 csv — schema 不嚴謹
- A.0.7 parser 已 ad-hoc 支援逗號切分

**提議方案（master 第五輪細化）：**
- 選 a：改 schema 為 `target_dirs: list[str]`（更嚴謹，需 patch Template + parser）
- 選 b：維持 csv 字串但 schema 明示「comma-separated list」（最小變動）
- 選 c：拆兩欄位 `primary_target_dir + secondary_target_dirs`（過度設計）

推薦選 b（最小變動 + 解釋現狀）。

**處理時機：** master 第五輪整合（在 A.0.9 後）跟 D-047 一併處理

---

## NEW_REQ_6 UD §3.10.4 `.qa_extension/` 寫法 vs DF §8 `qa_type_registry.yaml user_extensions` 衝突（minor）

**狀態：** ✅ **RESOLVED**（master 第五輪 2026-05-19 — UD v0.4→v0.5 partial supersede；§3.10.2 / §3.10.3 / §3.10.4 / §3.10.5 全 6 處 .qa_extension operative refs 改成 user_extensions: 段寫法；DF §8.3 + §8.10 補 algorithm / report_template 欄位承接（CODEX (e) recheck patch round）；詳 DECISIONS_LOG §6.9.6）

**時點：** 2026-05-19  
**提出者：** CODEX A.0.8 spec interpretation question

**需求背景：**
- UD §3.10.4 v0.4 仍寫舊機制：
  - `.qa_extension/<qa_type_name>.yaml` 在 Instance root（line 3613/3643/3663/3690）
  - 「9 種 enum 含 `<USER_DEFINED>`」（line 3714）
  - A.0 parser 掃 `.qa_extension/*.yaml`（line 3715）
- DF §8 v0.2 + Contract A.5 v2.0 採新機制：
  - 單一 `qa_type_registry.yaml` 含 `core` + `user_extensions:` 段
  - 8 core enum + user 自加，不含 USER_DEFINED 通配
- 兩個 LOCKED spec 寫法**衝突** — pre-LOCKED patch round 1-4b 沒 grep 到 UD §3.10 細節（屬 v0.3 patch 未清盡的歷史殘留）

**A.0.8 採對齊處理（CODEX 判定正確）：**
- 實作 `_design/registries/qa_type_registry.template.yaml` 採 DF §8 + Contract A.5 pattern
- **不**做 `.qa_extension/*.yaml` 掃描
- 對齊 D-043 + DF §8 + Contract A.5

**處理時機：** master 第五輪整合（在 A.0.9 後）跟 D-047 + NEW_REQ_4/5 一併處理：
- UD §3.10.4 改寫成「user_extensions: 段內加 entry」pattern
- 移除 `.qa_extension/` 寫法 + USER_DEFINED 通配
- 補 supersede 註記

---

## NEW_REQ_7 Skill multi-agent invocation UX（major — M1 user-test 發現）

**狀態：** ✅ **RESOLVED via D-048**（master 第六輪 2026-05-20 拍板候選 b+c — root AGENTS.md + CLAUDE.md + `_user_manual/skill_invocation_guide.md`；落地 ARCH v1.4 §3.3 multi-agent invocation 慣例段 + TASKS v1.5 A.12 task；詳 DECISIONS_LOG §6.10.2）

**時點：** 2026-05-19  
**提出者：** user（M1 user-test Phase 2）

**需求背景：**
- 26 skill 中只有 Claude Code CLI user 能用 `/init-project` slash command 直接觸發
- 其他 agent 環境（Cowork / OpenAI Codex CLI / Codex App）user 必須每次手動貼長 prompt 引導 agent 讀 SKILL.md — 不直覺、易出錯
- M1 user-test 跑 Cowork 跑通 /init-project 5 階段但需手動引導；Codex CLI 同樣需引導但 prerequisite check 正確（拒絕 rerun）

**拍板方案（候選 b + c）：**
- **root `AGENTS.md`**（OpenAI Codex CLI / Codex App 慣例）：列 26 skill 清單 + multi-agent invocation 規格
- **root `CLAUDE.md`**（Anthropic Claude Code CLI 慣例）：列 26 skill 清單 + 對應 invocation 規格（與 AGENTS.md 90% 共享內容）
- **`_user_manual/skill_invocation_guide.md`**（NEW_REQ_2 manual scope）：給 Cowork / Codex App user 的 copy-paste fallback 範本（agent 不自動讀但 user 可 reference）

**未採方案：**
- 候選 a（每 skill 加 INVOKE.md）：26 個維護點 + 涉跨 spec D-048 + 工時 ~13h
- 候選 d（a + b + c 全包）：工時 ~20h + 3 處同步

**對既有 spec 的影響：**
- ARCH v1.3 §3.3 skill 內容規範 → v1.4 新增 §3.3.X「Multi-agent invocation 慣例」段
- TASKS v1.4 → v1.5 加 A.12 task（屬 Wave 4 平行）
- 不涉 IC / SPEC §0-§17 / UD / DF 修訂

**處理時機：** master 第六輪 — D-048 拍板 + Wave 4 A.12 task 跑 CODEX 對話

---

## NEW_REQ_8 Template repo 污染（Critical — M1 user-test 後續發現）

**狀態：** ✅ **RESOLVED via D-049 + D-051 partial supersede**（master 第六輪 Critical patch round 2026-05-20 拍板候選 d = a+b 兩道防線組合 D-049；後第七輪 master inline patch round 2026-05-20 拍板 D-051 partial supersede 移除防線 #2 — 因 fresh Instance clone 必然 false-positive；目前 active 為 D-051 後單防線 #1 `.template_root` marker — 落地檔：00_protocol/00_i v0.3 / .claude/skills/init-project/SKILL.md v0.3 / .template_root marker / ARCH v1.6 §3.3.2 / TASKS v1.6 A.5b / DECISIONS_LOG v1.9 §6.11 + §6.13；詳 DECISIONS_LOG §6.11.2 D-049 + §6.13.2 D-051）

**時點：** 2026-05-20  
**提出者：** user（M1 user-test 後續驗證發現 + 第六輪 master 對話內回報）

**需求背景（Critical）：**
- user 跑 /init-project 透過 Cowork 在 Template repo（D:\劇本開發工具）上跑通 5 階段
- agent 沒擋住 — 直接寫了 Instance-specific 資料（.protocol_version / 3 registry copies / 10_art_assets/ / 可能還改了 00_b/00_c/00_d）到 Template repo
- 根因：00_i §2 既有 4 條啟動條件無法區分 Template repo vs Instance repo（兩者都有 00_protocol/ / 01_world/ ~ 09_quality_assurance/ 等目錄）
- 影響：Template 被污染 → 影響所有後續開發 + git 紀錄混亂；user 必須手動清理（git checkout + git clean）
- 嚴重度 **Critical**（M1 路徑 broken — 影響後續任何 /init-project 試跑安全）

**user 提議候選：**
- 候選 a：00_i §2 啟動條件加 negative check「不得存在 `_design/registries/*.template.yaml`」
- 候選 b：Template repo root 加 `.template_root` marker；agent 啟動見此檔即拒絕
- 候選 c：/init-project 啟動前 confirmation prompt — 「你已 clone Template 到新目錄了嗎？」
- 候選 d（推薦）：a + b 組合

**拍板方案：候選 d（a + b 兩道防線組合）**

落地三維度檢測規則（依 ARCH v1.5 §3.3.2）：
- **第一道防線（候選 b 落地）：** `.template_root` marker file 檢測 — explicit signal，user 必須手動刪以表「轉換為 Instance」意圖
- **第二道防線（候選 a 落地）：** registries template 殘留 + 未 bootstrap 推斷 — automatic inference，catch user 忘刪 marker 的 false negative
- 既有 bootstrap completed 檢測（D-042 既有）保留

**對既有 spec 的影響：**
- 00_protocol/00_i v0.1 → v0.2 partial supersede（§2 啟動條件加 #5 #6）
- .claude/skills/init-project/SKILL.md v0.1 → v0.2 master inline patch（啟動前檢查加 2 條 bullet + 兩段拒絕文案）
- 中文 wrapper `.claude/skills/初始化專案/SKILL.md`：**不**動（極簡 wrapper 自動跟英文主檔）
- ARCH v1.4 → v1.5（§3.3 加新子節 §3.3.2）
- TASKS v1.5 → v1.6（加 A.5b Critical patch task 紀錄）
- `.template_root` marker file：新建於 D:\劇本開發工具/ root
- 不涉 SPEC / IC / DF / UD / UX_SPEC / REQUIREMENTS_LOCK 修訂

**對 Wave 4 三 starter 的影響：**
- A.7 / A.8 starter：**不**受影響（純讀 skill 不涉 bootstrap）
- A.12 starter：**不**受影響但 Wave 4 review checkpoint 必驗 A.12 產出 AGENTS.md / CLAUDE.md / skill_invocation_guide.md 引用 init-project description 對齊 v0.2

**user 後續手動動作（Template 污染清理 cookbook）：**
- 詳 DECISIONS_LOG §6.11.3
- git checkout / clean 對應檔
- commit + push 本輪 Critical patch round 一包
- 後續再做 user-test 時：先 `git clone` 到新目錄 → `cd` 進去 → `rm .template_root` → 跑 /init-project

**處理時機：** master 第六輪 Critical patch round — 已完成 inline patch（不發 CODEX 對話；屬 master 緊急 patch + 短審查 紀律）

---

## NEW_REQ_9 check_paths Windows vs sandbox baseline 差異（DEFERRED — minor 環境議題）

**狀態：** 🟡 **DEFERRED**（master 第六輪 2026-05-20 紀錄 — 留 Phase A.X 未來 cleanup 範圍；不阻 Phase A 收尾 / Phase B 啟動）

**時點：** 2026-05-20  
**提出者：** master 第六輪 A.11 整體驗收 — CODEX 跑出 254 ERROR / master sandbox 跑出 243 ERROR

**需求背景：**
- `scripts/check_paths.py` 在 Windows 端跑：254 ERROR（226 old-style + 28 missing active）
- 同 working tree 在 sandbox（Linux）跑：243 ERROR（226 old-style + 17 missing active）
- 226 old-style 兩端完全一致；diff 全在 missing active reference（+11）
- 11 個 ERROR 全部 source 為既有 Template 範例模板檔（`01_world/` / `02_vocabulary/` / `03_characters/` / `05_plot/` 等），不是本輪新建/改檔
- 原因：Windows filesystem case-insensitive 對 path resolution 行為跟 sandbox case-sensitive 不同所致

**對 A.11 的影響（已解決）：**
- A.11 starter 設 `≤245` 門檻是基於 sandbox baseline 243 — Windows 跑超過門檻 → CODEX 標 NO-GO
- master 第六輪裁決：接受 Windows baseline 254；採 inline patch（DECISIONS_LOG §6.11.7）改 PHASE_A_COMPLETION_REPORT v1.0 NO-GO → v1.1 PASS
- 不開 cleanup round（11 個 ERROR 屬環境差異，非設計缺陷）

**提議解法（DEFERRED 不本輪做）：**
- 候選 a：修 check_paths.py 加 case-insensitive resolution mode（讓 Windows 跑出跟 sandbox 一樣的結果）— 屬 scripts/ 行為對齊範圍，工時 1-2h
- 候選 b：226 老式檔名 reference 全部 rename 對齊新命名（Phase A.X 大 cleanup round 範圍）— 工時 5-10h
- 候選 c：在 A.11 starter / 未來 baseline gate 文檔內明示「baseline 數字依 user 環境決定，不寫 hard 數字」— 文檔層級規範，工時 0.5h
- 推薦 a + c：a 修 script，c 修文檔規範；b 留 Phase B 後 cleanup

**處理時機：** Phase A.X 未來 cleanup round（不阻 Phase A 收尾 / Phase B 啟動）；屬「環境兼容性議題」非「設計缺陷」

**Owner：** 未來 Phase A.X cleanup CODEX 對話

---

## NEW_REQ_10 CODEX starter fence 巢套慣例（DEFERRED — minor 文檔規範改進）

**狀態：** 🟡 **DEFERRED**（master 第七輪 2026-05-20 紀錄 — 留未來 starter 寫作慣例改進範圍；不阻 Wave 7 / Wave 8 推進）

**時點：** 2026-05-20  
**提出者：** master 第七輪 Wave 7 B.6.5 起手包寫作 — master 第六輪 reviewer feedback 提示

**需求背景：**
- master 第七輪寫 `_design/CODEX_B65_REVIEW_GATE_STARTER.md` v0.1 時，outer agent-prompt fence 用 ```（同 B.5 / B.6 / A.11 既有 starter 慣例）
- starter 內部 nest ```bash / ```python code block — `scripts/check_paths.py` 的 `FENCE_RE` 用相同 marker（backtick）做 toggle，外層 ``` 被內層 ``` 二次匹配 toggle 為 False → 內部 path reference 未被 skip → check_paths 報 5 個假 ERROR
- 加上 outside fence 的 2 個 Instance-only 表格 path reference（`<instance_root>/05_plot/05_a_主線大綱.md` 在 Template repo 內必然 missing） — 共 +7 ERROR
- 第七輪 master inline patch：outer fence 改 `~~~`（內層 ``` 不會 toggle 不同 marker fence）+ outside fence 的 Instance-only concrete path 前加 `<instance_root>/` 前綴（PATH_RE 的 `(?<![\w/])` lookbehind 因 `/` 阻擋 match）→ check_paths 回到 sandbox baseline 243 ERROR +0 增量

**問題本質：**

`scripts/check_paths.py` 的 fence/path detection 對「outer ``` + nested ```」場景不穩定：

```
FENCE_RE = re.compile(r"^(\s*)(```|~~~)")
PATH_RE = re.compile(
    r"(?<![\w/])"
    r"(?:0[0-9]_\w+|archive|_design)"
    r"/[\w./\-一-鿿]+"
    r"\.(?:md|py|json|yml|yaml|toml|csv)"
    r"\b"
)
```

`iter_non_fenced_lines` 依 `fence_char == marker` 做 toggle，但巢套相同 marker 會錯亂。

**提議慣例（未來 starter 寫作規範）：**

1. **所有 CODEX starter outer agent-prompt fence 用 `~~~`**（內部 nest ``` 不會 toggle 它）
2. **所有 Instance-only concrete path 引用** 在 design docs (`_design/`) 內前加 `<instance_root>/` 前綴或用 `<placeholder>` 變數寫法（PATH_RE 因 `<` 非 word/path 字元自動 break）
3. **既有 starter 不必回頭修**（Wave 6/7 既有 SKILL.md / protocol 沒中此 bug — 因為它們沒用 nested fence；屬 Phase B/C 後 cleanup）

**對 Wave 8 starter 影響：**

第七輪 master 寫 Wave 8（B.7 / B.8 / B.9）三 starter 時應採新慣例：
- outer agent-prompt fence 用 ~~~
- Instance-only concrete path 前加 `<instance_root>/` 前綴

**未採方案：**

- **修 scripts/check_paths.py 認 nested fence**：屬 scripts/ 行為改進範圍，工時 1-2h；但 (~~~ outer + 前綴) 慣例本身更清楚不歧義，script 改寫屬 over-engineering
- **接受 +7 ERROR 升 baseline**：稀釋 baseline 校正紀律（baseline 接受是「不可修」議題如 NEW_REQ_9 環境差異；本檔屬「可修」starter 寫法 bug）— 已 RESOLVED inline patch

**對既有 spec 的影響：**

- `_design/POST_LOCK_PENDING.md` v0.4 → v0.5（本檔；加 NEW_REQ_10 紀錄）
- `_design/CODEX_B65_REVIEW_GATE_STARTER.md` v0.1（master 第七輪 inline patch — outer fence ~~~  + 3 處 outside fence path 加 `<instance_root>/` 前綴；屬 starter 寫法修補不升 version）
- `_design/phase_b_outline_review_log.md` v0.1（master 第七輪 inline patch — 2 處 path 加前綴；不升 version）
- 不涉 SPEC / IC / DF / UD / ARCH / TASKS / REQUIREMENTS_LOCK / UX_SPEC 修訂

**處理時機：**

- master 第七輪 — inline patch 已完成（B.6.5 兩檔修補）
- 第七輪 master 寫 Wave 8 三 starter 時採新慣例
- Phase A.X 未來 cleanup CODEX 對話可考慮修 `scripts/check_paths.py` 認 nested fence（如有必要）

**Owner：** master 第七輪 inline patch + 第六輪 master reviewer feedback  
**Cross-ref：** POST_LOCK_PENDING NEW_REQ_9 baseline 校正紀律（區隔「不可修」vs「可修」）/ `scripts/check_paths.py` FENCE_RE + PATH_RE / DECISIONS_LOG §6.11.7 baseline 校正先例

---

## NEW_REQ_11 翻譯工具分支提案（DEFERRED — Future tool fork；user 拍板「工具 A 完整封裝後啟動」）

**狀態：** 🟡 **DEFERRED**（master 第六輪 2026-05-20 紀錄；user 拍板啟動條件：工具 A 完整封裝 release 之後 / Milestone 4 之後；不是 D-NNN 拍板，是「未來分支設計提案」性質）

**時點：** 2026-05-20  
**提出者：** user（master 第六輪閒聊延伸內提出 — 「這工具產出的資料含大量可以提高翻譯品質的部分，透過修改這個工具做成另一個翻譯專用工具」）

**需求背景：**
- 工具 A 產出的 source 含豐富上下文 metadata（W-rules / V / 聲線卡 / 關係 / 大綱位置 / 章節節奏 / QA reports）— 對翻譯品質提升極有價值
- 主流 i18n 工具（Crowdin / Lokalise / POEdit）設計給「純台詞 string 翻譯」— 翻譯員看不到這些 metadata → 翻譯品質遠低於 source 品質
- user 提案：fork 工具 A 做「翻譯專用 companion tool」（只讀 source + 翻譯 + 翻譯 QA），單向依賴工具 A export

**提議方案（已紀錄完整設計於 `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md`）：**

工具 B（暫名 `game-dialogue-translator`）：
- 結構同工具 A 範式（AGENTS.md + CLAUDE.md + .template_root + _design/ + .claude/skills/ + scripts/ + ...）
- 新 entity：`T-<source_KEY>-<lang>` 翻譯 / `G-<term>-<lang>` glossary
- 新 QA：09_a~09_i 翻譯版（每語言獨立）+ 09_t1 翻譯一致性 / 09_t2 文化適配 / 09_t3 UI 長度約束
- 核心 skill：/translate <scene_id> <lang>（5 階段對話，含 source full context 餵入）

**設計優點：**
- 完美 SoC（工具 A source / 工具 B 翻譯）
- 不破壞工具 A LOCKED D-018 #2 「不存多語對白」
- 單向依賴（工具 B 只讀工具 A export）
- 重用既有 spec 範式（entity / qa / issue registry user_extensions 機制 + 5 階段對話 + phase_log）

**工時估算：** 80-130h master + CODEX（跟工具 A 從 Phase 1 到 master 第六輪整合的工時類似量級）。

**啟動條件（user 拍板）：**

```
✓ 工具 A Milestone 4 達成（Phase D 完成 + production release）
✓ L3_EXPORT_PROMPT_SCHEMA v1.0 穩定（實際吐過真實 JSON）
✓ 至少 1 個完整作品 source corpus 存在
✓ user 明確表達翻譯需求（「我這作品要翻 EN/JP/KO」）
✓ 工具 A 維護期穩定 6 個月以上
```

**現在工具 A 可以做的「對工具 B 友好」設計選擇（順手保留）：**
- L3_EXPORT_PROMPT_SCHEMA 預設保留所有 metadata
- entity / qa / issue registry user_extensions 機制設計時保留「未來分支 fork」可行性
- KEY 機制全 repo unique guarantee 維持
- phase_log schema 範式維持（工具 B 直接 fork）

**處理時機：** 工具 A 完整封裝 release 後 — 不在當前 master 對話 / Phase B / Phase C / Phase D scope 內

**Owner：** 未來新 master 對話（啟動工具 B 開發時）

**Cross-ref：** `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` v0.1（完整設計提案）/ DECISIONS_LOG §6.14（翻譯工具提案紀錄）/ REQUIREMENTS_LOCK §3.2 i18n KEY + §4.2 可擴充 QA 機制 / D-018 #2 LOCKED

---

## NEW_REQ_12 — /create-world 寫 00_b §1/§2 vs D-050 子裁決 1 衝突（✅ RESOLVED via D-053）

**狀態：** ✅ **RESOLVED via D-053**（第七輪 master 2026-05-21 收尾重審 patch round — CR-01 從 DEFERRED 升 CRITICAL；user 拍板採 Option A — D-053 partial supersede D-050 子裁決 1 加 /create-world exception 寫 00_b §1/§2 Instance-specific section；詳 DECISIONS_LOG v1.9 §6.16.2）

**原狀態紀錄（v0.7 / 2026-05-20）：** 🟡 DEFERRED（M2 testing 期間觀察到；當時以為不阻 Phase C 啟動 — CODEX 重審後升 CRITICAL）

**時點：** 2026-05-20（M2 testing 期間 /create-world 跑完後觀察到）  
**提出者：** 第七輪 master（M2 testing /create-world 階段 4 寫檔後）

**需求背景：**

M2 testing 跑 /create-world 時 agent 寫了 `00_protocol/00_b §1 §2` — 但 D-050 子裁決 1（DECISIONS_LOG §6.12.2）明示「所有 /create-* skill 嚴禁寫 00_protocol/，唯一例外是 /init-project」。

**衝突源：**
- `/create-world` SKILL.md（Phase A.6 落地版本）內 §10.9「類型語氣」拆分規則寫到 `00_protocol/00_b_反 AI 味檢查表.md §1 §2`（這是早於 D-050 的設計）
- DECISIONS_LOG v1.5 §6.12.2 寫「create-world 已對齊 D-050 W 行」— 此聲稱**不準確**（6 輪 master 寫 D-050 時沒實際 verify create-world SKILL.md 內容是否真的不寫 00_protocol/）
- 實際 Phase A.6 落地版本仍允許寫 00_b §1 §2

**為什麼仍是「不大不小」的問題（不阻 M2）：**
- Instance 端 00_b 屬「作品-specific」（§1 作品類型 / §2 髒話尺度等）— 寫入屬合理範圍
- D-050 子裁決 1 over-broad block 的本質是「不該擋 Instance-specific section 寫入」— 跟 D-049 #6 over-broad 同類缺陷
- M2 testing 已用 manual mode 跑完 /create-world，沒有實際傷害

**提議方案：**

選 1（推薦）：D-053 partial supersede D-050 子裁決 1
- 加 exception「/create-world 可寫 00_b §1 §2 屬 Instance-specific section 範圍」
- 同時保留「不寫 00_a / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l」核心紀律
- 其他 /create-* skill 仍嚴禁寫 00_protocol/

選 2：移除 /create-world SKILL.md 寫 00_b 動作（強制對齊 D-050）
- 需要 /create-world SKILL.md 升 v0.2
- 失去 §10.9 類型語氣寫回 00_b 的功能；改成「印建議 + user 手動編 00_b」
- 增加 user friction

選 3：暫不處理（標永久 deferred）— 因為實際無傷害

推薦：**選 1（D-053）** — 第七輪 master 收尾全面重審期間 CODEX 升此 finding 為 CRITICAL；user 拍板採選 1 並在 §6.16 patch round 落地 D-053。**已 RESOLVED（不再 deferred 給 8th master）。**

**對 Phase C 啟動的影響：** 已解除（D-053 落地後）— Phase C `/scene-task` / `/dialogue-write` / `/qa` 不寫 00_protocol/，紀律仍 hold

**處理時機（歷史紀錄）：** 原預期「8th master Phase C 啟動前處理」— 實際提前在第七輪 master §6.16 重審 patch round 內處理（CR-01 升 CRITICAL → user 拍板採選 1 → D-053 落地）

**Owner（歷史紀錄）：** 原 8th master；實際第七輪 master inline patch（§6.16 round）

**Cross-ref：** DECISIONS_LOG §6.12.2 D-050 子裁決 1（被 partial supersede） / DECISIONS_LOG §6.16.2 D-053（落地拍板）/ Phase A.6 落地 /create-world SKILL.md §10.9 / M2 testing /create-world 階段 4 寫檔紀錄 / 同類 D-049 #6 over-broad 設計缺陷（D-051 已 partial supersede）/ CODEX_7TH_MASTER_FINAL_REVIEW_REPORT CR-01 finding

---

## NEW_REQ_13 — per-scene 檔 convention（✅ RESOLVED via D-054 Hybrid）

**狀態：** ✅ **RESOLVED via D-054**（第八輪 master 2026-05-21 拍板選 1 Hybrid — aggregate 06_a 預設 + `/iterate-scene --split-to-file` 拆出選項（屬 Phase D 範圍延後實作；NEW_REQ_15 追蹤）+ `/scene-task` 兩階段 fallback；0 LOCKED spec supersede；既有 00_h SKILL.md line 198 escape hatch wording 自然承接；詳 DECISIONS_LOG §6.17.2 D-054 + D054_DECISION_PACKAGE v0.2 §3 推薦理由）

**原狀態紀錄（v0.7~v0.9 / 2026-05-20）：** 🟡 DEFERRED（M2 testing /create-detailed-outline 階段 3 CONFLICT-1 中發現；不阻 M2；推 8th master Phase C 啟動前處理）

**時點：** 2026-05-20（M2 testing /create-detailed-outline 階段 3 user CONFLICT-1）  
**提出者：** 第七輪 master（M2 testing /create-detailed-outline 階段 3）

**需求背景：**

M2 testing 跑 /create-detailed-outline 時，第七輪 master 在 Stage 3 啟動 prompt 中寫「每場一檔 06_scene_index/CH<n>_S<m>_<scene_name>.md」— 但 agent 抓出 CONFLICT-1：

- 既有 /create-detailed-outline SKILL.md（B.7 v0.1 落地版本）+ D-050 子裁決 2 CH 行寫「`05_b` + `06_a` (聚合式單檔)」
- repo 目前 `06_scene_index/` 也只有聚合式 `06_a_場景索引模板.md`
- per-scene 檔屬未來 convention，現行 spec 未支援

**M2 testing 採 agent 提議方案：** 本輪採聚合式 `06_a`，per-scene 拆檔屬未來 NEW_REQ migration。

**為什麼 per-scene 檔在 Phase C 可能更好：**

- **/scene-task `<S-ID>` 效率**：Phase C `/scene-task` 跑一個場景時讀單一場景檔 vs 讀整個聚合 06_a — per-scene 檔 context 用量低
- **per-scene git diff**：editor 改一場時 diff 只動該場檔；聚合式整檔 diff 太大
- **per-scene merge conflict**：多人或多 agent 同時動不同場無 race
- **per-scene LOCKED 粒度**：可單獨 LOCK 某場（聚合式只能整檔 LOCK）

**為什麼當前聚合式仍合理：**

- /create-detailed-outline 一次建 30+ 場 — 寫聚合 1 檔 vs 寫 30 檔，前者效率高
- /status 讀單一聚合檔取得所有 S-* status 比讀 30 檔快
- frontmatter weight S=0.2 全部對齊 — 聚合式自然支援

**提議方案：**

選 1（推薦）：Hybrid convention — 場景建立時用聚合 06_a，user 標記某場「需獨立檔」時 split 出來
- /create-detailed-outline 階段 4 預設聚合
- /iterate-scene `<S-ID>` 加 `--split-to-file` 選項，把該場從 06_a split 為 `06_scene_index/CH<n>_S<m>_<scene_name>.md`
- /scene-task 讀檔時優先讀 per-scene 檔（如存在），否則 fallback 聚合

選 2：完全 per-scene convention — /create-detailed-outline 階段 4 直接每場一檔
- 修改 /create-detailed-outline SKILL.md
- 修改 D-050 子裁決 2 CH 行寫 `06_scene_index/<scene-files>` directory pattern
- /status / build_repo_index 對 per-scene 檔的支援已就位（parser 不分聚合 vs split）

選 3：完全聚合 convention — 維持現狀，per-scene 永不支援

推薦：**選 1（Hybrid）**，但屬 8th master Phase C 規劃 scope（/scene-task / /dialogue-write 設計時拍板）

**對 Phase C 啟動的影響：** 直接影響 /scene-task SKILL.md 設計 — 應該在 /scene-task 落地前先拍板 convention

**處理時機：** 8th master 規劃 Phase C `/scene-task` 設計時 — open D-054 拍板選 1 / 2 / 3

**Owner：** 8th master（Phase C `/scene-task` 規劃時）

**Cross-ref：** DECISIONS_LOG §6.12.2 D-050 子裁決 2 CH 行 / /create-detailed-outline SKILL.md v0.1 / M2 testing /create-detailed-outline 階段 3 CONFLICT-1 紀錄 / 8th master Phase C 規劃預期項

---

## NEW_REQ_14 — PHASE_X_COMPLETION_REPORT §6 補入 AI-assisted 機制（DEFERRED — UX 改進；同 D-052 模式）

**狀態：** 🟡 **DEFERRED**（第七輪 master 2026-05-20 紀錄 — M2 testing PHASE_B_COMPLETION_REPORT §6 補入時 user 觀察到 friction；推 8th master Phase C 啟動前 / Phase C 收尾前處理）

**時點：** 2026-05-20  
**提出者：** user（M2 testing PHASE_B_COMPLETION_REPORT §6 補入步驟期間）

**需求背景：**

每個 Phase 收尾的 `PHASE_X_COMPLETION_REPORT.md`（X = A / B / C / D）含 §6「user 親跑端到端」placeholder — CODEX 寫 §1-§5 + §7-§9（framework verification + 聲明 + cross-ref），但 §6「事實紀錄」屬 user 親身經歷必須手動補：

- 哪天跑的 / 用什麼 agent 環境跑的
- 中間 issues / resolutions
- testing 規模（建幾個角色 / 章節）
- user-specific 拍板（例：選 Option A 走 D-051）

PHASE_A_COMPLETION_REPORT v1.1 §6 由 master 第六輪內補；PHASE_B_COMPLETION_REPORT v1.0 §6 由 master 第七輪內補；屬整個專案生命週期 ~4 次（A / B / C / D 各一次）但每次手動 markdown 編輯 ~5-10 分鐘。

**提議方案（同 D-052 模式）：**

**「AI-assisted §6 補入流程」：**

```
1. user 明示：「我跑了 phase X end-to-end，跑通：[skill 清單] / [N 個 gate] / [M 個 issues]」
2. AI 從以下資料 reconstruct testing 事實：
   - .protocol_version.phase_log（哪些 skill completed / 時間戳）
   - phase_x_*_review_log.md（哪些 gate 過 / 拍板理由）
   - git log（本輪 commit 順序 + message）
   - DECISIONS_LOG（期間新加的 D-NNN / 議題處理）
   - POST_LOCK_PENDING（期間新加的 NEW_REQ）
3. AI 給 user 看「擬補入 §6 內容」draft（含 testing 摘要 + 議題處理 + Phase 啟動條件對應 4 子段）
4. user 拍板「OK」/「改 [...]」
5. AI 執行 §6 patch（用「精確邊界 patch」— 不全檔覆蓋）+ 跑 check_headers / check_paths verify
6. AI 給 user 看 git diff，user commit + push
```

**Accountability 保留：**
- §6.1 拍板背景紀錄 user 明示拍板原文 + email + 時間戳
- AI reconstruct 限定基於既有檔案事實，不憑空捏造
- git diff 完整透明可審計

**對比現狀（PHASE_B_COMPLETION_REPORT §6 手動補）：**
- 手動編輯時間：~5-10 分鐘
- AI-assisted：~2-3 分鐘（user 明示 + verify diff）+ user 不必手寫 markdown table

**未採方案：**
- 完全 AI auto-generate §6（無 user 拍板）：違反 D-052 accountability 紀律
- 移除 §6 placeholder（純跳過）：失去 PHASE_X_COMPLETION_REPORT 的 user-side 驗證證據

**對既有 spec 的影響：**
- 若採此 NEW_REQ，需修改 PHASE_X_COMPLETION_REPORT 寫作 starter（A.11 / B.9 / 未來 C.X / D.X）— 加 §6 補入 AI-assisted flow 說明
- 不涉 SPEC / IC / DF / UD / ARCH / TASKS / REQUIREMENTS_LOCK 修訂

**處理時機：** 8th master 寫 CODEX_C_FINAL_STARTER（Phase C 收尾 CODEX starter）時順手實作 AI-assisted §6 補入流程 — 屆時 user 親跑 Phase C 端到端 後直接走 AI-assisted

**Owner：** 8th master（Phase C 收尾 starter 設計時）

**Cross-ref：** D-052 同模式紀律（AI-assisted + user 明示拍板）/ PHASE_A_COMPLETION_REPORT v1.1 §6 / PHASE_B_COMPLETION_REPORT v1.0 §6 / 第七輪 master 手動補入 M2 testing 觀察紀錄

---

## NEW_REQ_15 — per-scene 拆檔 convention 迭代評估（DEFERRED — 依方案 1 真實使用後 trigger）

**狀態：** 🟡 **DEFERRED**（第八輪 master 2026-05-21 紀錄；user 拍板原文「先走方案一，未來實際使用後如果有迭代需求在後續版本再進行優化，幫我把這點紀錄在未來更新文件中」；對應 D-054 紀錄 §6.17.2 結尾「未來迭代條件紀錄」段）

**時點：** 2026-05-21（D-054 拍板同時新增）  
**提出者：** user（D-054 拍板時明示要求紀錄未來迭代條件）

**需求背景：**

D-054 拍板選 1 Hybrid（DECISIONS_LOG v2.0 §6.17.2）— aggregate 06_a 預設 + `/iterate-scene --split-to-file` 拆出選項。方案 1 的設計哲學是「**保留未來選擇權**」 — 若實際使用後發現方案 1 hybrid 不夠用 / per-scene 變主流需求，未來可開 D-056+ supersede（議題號原預留為 D-055；依 DECISIONS_LOG §6.18.2 順延至 D-056 或當時最近未用編號）。

本 NEW_REQ_15 是該「未來迭代評估」的追蹤位置 — 不是已知需求，而是「**監控觸發條件**」。

**未來迭代 trigger 條件建議（給未來 master 對話參考；非 hard rule）：**

| trigger | 條件 | 對應評估動作 |
|---|---|---|
| **trigger A — 使用規模** | user 在實際作品撰寫 N 個場景（建議 N ≥ 30）後回報「想全 per-scene」/「聚合 06_a 太大難維護」| 評估 D-056+ 全 per-scene supersede（議題號原預留為 D-055；§6.18.2 順延）|
| **trigger B — split-to-file 使用頻率** | Phase D `/iterate-scene --split-to-file` 實作後，user 連續多次（建議 ≥ 5 場）拆檔 | 評估「per-scene 是否變預設」（hybrid 反向）|
| **trigger C — 並行寫作需求** | 多 agent 並行寫作模式（NEW_REQ_11 翻譯工具或其他平行使用）需求增多 | 評估 per-scene 對 race condition 的緩解 |
| **trigger D — git diff / merge conflict 摩擦** | 真實 git diff / merge conflict 在聚合 06_a 模式下持續發生 user friction | 評估拆檔降低 conflict |

**若 trigger 達成 → 下一輪 master 開 D-056+ 拍板包（議題號原預留為 D-055；依 §6.18.2 順延），候選選項：**

1. **D-056+ 選項 A：** 升級「per-scene 變預設 + 聚合保留 fallback」（hybrid 反向；D-054 的 mirror image）
2. **D-056+ 選項 B：** 強制全 per-scene（同 D-054 原方案 2；當時被拒絕但若使用 evidence 支持可重議）
3. **D-056+ 選項 C：** 維持 D-054 hybrid 但加 `/iterate-aggregate-to-split-all` 批量拆全 Instance（介於選 A 與選 B）

**對既有 spec 的影響（DEFERRED 期間）：** **無**（NEW_REQ_15 純追蹤；DEFERRED 期間不動任何 spec）

**處理時機：** 
- **短期（Phase C/D 期間）：** master 對話結尾 handoff 時順手 audit「user 在 Phase C/D 期間是否觸發 trigger A-D 任一」；若無，繼續 DEFERRED
- **中期（Milestone 4 後 / production release 後）：** user 跑真實作品撰寫一段時間後評估
- **長期（工具 B 翻譯工具啟動時 / 多 agent 並行需求出現時）：** trigger C 重點評估

**Owner：** 未來 master 對話（依 trigger 達成情況評估 D-056+ 拍板需求；議題號原預留為 D-055；§6.18.2 順延）

**Cross-ref：** 
- DECISIONS_LOG v2.0 §6.17.2 D-054（拍板紀錄 + 未來迭代條件記錄段）
- DECISIONS_LOG v2.0 §6.17.4 升 v2.0 後紀律「未來迭代追蹤紀律」首例
- NEW_REQ_13（RESOLVED via D-054 — 本 NEW_REQ_15 是其 follow-up 追蹤）
- D054_DECISION_PACKAGE v0.2 §3 推薦理由「保留未來選擇權」段
- NEW_REQ_11 翻譯工具分支（trigger C 相關 — 若工具 B 啟動可能拉高 per-scene 需求）
- POST_LOCK_PENDING NEW_REQ_5/9/10/11/14（其他 DEFERRED 項；本檔追蹤模式參考）

---

## NEW_REQ_16 — 自動化 QA Layer 1：Cross-ref Consistency Lint Script（DEFERRED — Phase D 期間考慮實作）

**狀態：** 🟡 **DEFERRED**（第七輪 master 2026-05-21 紀錄 — user 拍板「待未來實作 + 屆時要重新完整設計」）

**時點：** 2026-05-21（第七輪 master 對話收尾期間 user 提出「未來自動化 QA 工具 nightly 跑」需求）

**提出者：** user（觀察到第七輪累積 7 輪 CODEX 重審 + 9+ MINOR finding 仍存在 → 反推未來能否自動化）

**需求背景：**

第七輪 master 期間經 7 輪 CODEX 全面重審後仍累積 3 MAJOR + 6 MINOR 殘留（已 hard-limit accept 推 8th master cleanup）— 根因為：

1. **「Fix one, find two」遞迴模式**：每次 patch 引入新的 stale cross-ref
2. **CODEX review 無底洞**：每輪抓更深層細節（spec → starter → wrapper → description）
3. **架構天生 cross-ref 密集**：~40+ 互相 reference 的檔 + ~5-10 個檔 per D-NNN 同步
4. **缺自動化 cross-ref checker**：所有同步靠 CODEX review + 人類 patch

詳第七輪 master 對話內「為什麼 9 輪 重審還有 MINOR」討論。

**提議方案（高層架構 — 屆時實作須重新完整設計）：**

新增 `scripts/cross_ref_lint.py`（純規則 lint script — 無 AI；100% 安全）：

- 跨檔 version refs 對齊驗證（mention 的 starter v0.2 vs starter header v0.3 mismatch 偵測）
- D-NNN supersede 鏈完整性（LOCKED 變動 vs DECISIONS_LOG D-NNN 背書是否齊全）
- TASKS partial supersede ledger 涵蓋範圍 vs DECISIONS_LOG §6.X.2 落地紀錄一致性
- POST_LOCK_PENDING NEW_REQ status vs 落地 commit 對齊
- 輸出 JSON / markdown 格式 finding report（含 severity / file:line / 建議 patch）

**預估規模：** 200-400 行 Python；6-8 小時實作 + 2-4 小時 testing

**ROI 估算：** 自動抓 ~80% 7th master 期間 MINOR finding → 後續 master 對話省 30-60 分鐘 / 輪 cleanup 時間

**重要紀律（user 明示）：** **屆時實作時要重新完整設計** — 本 NEW_REQ 只是高層 vision；不要直接按本提議方案規格 code，需要先：

1. 分析當下實際 cross-ref 模式（屆時可能跟 v0.11 不同）
2. 設計 schema（findings JSON 結構）
3. 寫 test fixtures
4. 規劃白名單檔範圍（哪些檔可被 lint / 哪些不能）
5. 整合進 build / CI（pre-commit hook / GitHub Actions）

**處理時機：** **Phase D 期間** — 文檔債開始累積 + Phase D 14 個 skill 上線會大量產生 cross-ref → 此時實作 ROI 最高

**Owner：** 9th 或 10th master（Phase D 設計時提案）

**Cross-ref：** 第七輪 master 對話內「為什麼 9 輪 重審還有 MINOR」+「自動化 QA 工具 4 層架構」討論 / `check_headers.py` + `check_paths.py`（既有 lint）/ NEW_REQ_17 (Layer 2 auto-patch) / NEW_REQ_18 (Layer 3 nightly review)

---

## NEW_REQ_17 — 自動化 QA Layer 2：Auto-patcher for Safe Simple Patches（DEFERRED — 封版後實作）

**狀態：** 🟡 **DEFERRED**（第七輪 master 2026-05-21 紀錄 — 依賴 NEW_REQ_16 先實作；user 拍板「屆時重新完整設計」）

**時點：** 2026-05-21

**提出者：** user（同 NEW_REQ_16 討論）

**需求背景：**

NEW_REQ_16 Layer 1 lint 能**偵測** finding 但**不自動修**；需要 Layer 2 auto-patcher 處理「safe simple finding」（stale version refs / 機械字串替換）。

**提議方案（高層架構 — 屆時實作須重新完整設計）：**

新增 `scripts/auto_patch_safe.py`：

- 讀 Layer 1 finding report
- 篩「白名單檔 + 簡單機械替換」類型 finding（例：v0.2 → v0.3）
- backup → patch → verify with Layer 1 lint → auto-commit OR auto-revert
- commit 前 file size diff ±1% 限制（避免 §6.16 truncation incident 復現）
- 排除歷史紀錄段（DECISIONS_LOG / PHASE_X_COMPLETION_REPORT 內 history 不該被改）

**Safety net 設計（屆時必含）：**

- git branch 隔離（不直接動 master branch）
- 每 patch 後跑 lint verify
- 失敗 100% auto-revert
- 結果寄信 / GitHub PR 通知 user（不自動 merge）

**預估規模：** 300-500 行 Python；8-12 小時實作 + 4-8 小時 safety net testing

**ROI 估算：** 夜間自動清掉 ~80% Layer 1 finding → user 早上只看 git log + 0-3 個需人類判斷的 finding

**重要紀律（user 明示）：** **屆時實作時要重新完整設計** — 特別注意 §6.16 truncation incident 教訓：機械批量 patch 容易 corrupt 巨檔；safety net 是大頭。

**處理時機：** **Milestone 4 封版後 1-3 個月** — framework 穩定 + Phase C/D 量產台詞累積 cross-ref drift 後

**Owner：** 封版後維護期 master（屆時可能是 11+ 輪）

**Cross-ref：** NEW_REQ_16（依賴前置）/ §6.16 truncation incident 紀錄（DECISIONS_LOG §6.16.3）/ 第七輪 master 對話內 4 層架構討論

---

## NEW_REQ_18 — 自動化 QA Layer 3：Nightly AI-driven Semantic Review（DEFERRED — 翻譯工具 fork 前考慮）

**狀態：** 🟡 **DEFERRED**（第七輪 master 2026-05-21 紀錄 — 依賴 NEW_REQ_16/17 先實作 + 封版後評估；user 拍板「屆時重新完整設計」）

**時點：** 2026-05-21

**提出者：** user

**需求背景：**

NEW_REQ_16/17 Layer 1/2 只解「規則層」finding；**「語意層」finding**（例：「這段話用 D-049 兩道防線概括但實際 D-051 後是單防線」/ CR-01 級設計層自相矛盾）需要 AI semantic understanding。

第七輪期間 Layer 1 規則抓不到的 finding 約佔 20%（多在 LOCKED spec 內部 stale wording 層）— 這類需要 AI Reviewer。

**提議方案（高層架構 — 屆時實作須重新完整設計）：**

定時（每週 1 次 / 每月 1 次）自動 dispatch CODEX-like AI API 跑 6 維度重審：

- 用 CODEX_7TH_MASTER_FINAL_REVIEW_STARTER 為模板（已有現成的；7 輪 review 已驗證的 prompt）
- 自動產出 review report
- 結果寄信 / GitHub Issue 通知 user（不自動 patch — 由 user 起床看 + 開 master 對話處理）

**為什麼不自動 patch（Layer 4 不做）：**

§6.16 truncation incident 教訓 — AI auto-apply 巨型 patch 風險過高。語意層 finding 通常需要人類判斷選 Option A/B/C（D-051 / D-053 都是這種）。

**預估規模：** 12-20 小時實作（含 API 整合 + alert system + cost budget cap）

**ROI 估算：** Catch Layer 1/2 抓不到的設計層 drift → 早期發現 critical bug（避免半年後才被 review 抓到）

**Cost 估算：** 每輪 review ~$1-3 API cost；每週 1 次 = ~$50-150 / 年

**重要紀律（user 明示）：** **屆時實作時要重新完整設計** — 特別評估：
1. 封版後是否還會持續累積語意 drift（如果 framework 穩定 → Layer 3 ROI 低）
2. cost vs catch rate 比例（API 錢 vs 早期發現 critical bug 價值）
3. notification 頻率（每週 vs 每月 vs 觸發式）

**處理時機：** **Milestone 4 封版後 6+ 個月** — 觀察封版後是否還有大量語意 drift；如果是則實作；如果框架穩定則跳過

**未來分支（NEW_REQ_11 翻譯工具）：** 若工具 B 啟動 → tool A + B 共用 NEW_REQ_16/17/18 → ROI 翻倍

**Owner：** 封版後維護期 master（屆時可能是 13+ 輪）

**Cross-ref：** NEW_REQ_16/17（前置依賴）/ NEW_REQ_11 翻譯工具分支（潛在 reuse 對象）/ CODEX_7TH_MASTER_FINAL_REVIEW_STARTER（現成 prompt 模板）/ 第七輪 master 對話內 4 層架構討論

---

## NEW_REQ_19 — 9th master cleanup queue（PROCESSED via 9th master cleanup queue — 8th master Round 10 hard-limit accepted 殘留追蹤）

**狀態：** 🟢 **PROCESSED via 9th master cleanup queue**（10th master POST_LOCK_PENDING v0.19 §5.8 確認；11th master 對話 A second-run cycle audit B1 finding 後同步 header；原 v0.13 紀錄為 DEFERRED，9th master cleanup queue 已完整處理 R8-INFO-06 + R10-MI-01/02/03 + R10-MA-01 ack；對應 user 拍板 Path A —「同 NEW_REQ_16 哲學，cascade pattern 屬未來自動化處理範圍；繼續手動 patch 等於否認 user 設計判斷」）

> **v0.13 補註（2026-05-21，C.3 後 C4 patch round）：** TASKS §D.1a 09_g/h/i 三 QA 模板（D-026 + D-043 拍板時遺留 debt）原屬 Phase D 範圍，但 C.3 /qa skill 落地後設「8 模板存在」為 runtime prerequisite — 缺則拒絕。為避免阻塞 Milestone 3「user 可量產台詞」，由第八輪 master 在 Phase C 收尾期間提前發起 **C4 patch round**（CODEX_C4_PATCH_STARTER v0.1）補建 3 模板。**此補建非 NEW_REQ_19 原 scope**（NEW_REQ_19 追蹤 Round 10 殘留 4 finding + R8-INFO-06），但屬第八輪 master 範圍提前消化的 Phase D §D.1a debt — 9th master 接手時 TASKS §D.1a 可直接標 ✅ DONE。

**時點：** 2026-05-21（第八輪 master Round 10 結果出來後 user 拍板）

**提出者：** 第八輪 master（Round 10 NEAR-GO 後 hard-limit accepted）

**需求背景：**

第八輪 master 跑完 Cleanup round + Round 8 GO + patch round 2 + Round 9 NEAR-GO + D-054 拍板落地 + patch round 3 + Round 10 NEAR-GO。Round 10 結果含 1 MAJOR + 3 MINOR：

| Finding | 性質 | 處理 |
|---|---|---|
| R10-MA-01 | starter-vs-user-平行-add mismatch（user 收尾期間平行加 NEW_REQ_16/17/18 到 POST_LOCK_PENDING v0.11；Round 10 starter 寫「不動 POST_LOCK_PENDING v0.10」屬 starter wording 過時，非真 spec 違反）| **明示授權**：user 平行加 NEW_REQ_16/17/18 屬正當作業；Round 10 starter scope 過時不算違規。本 NEW_REQ_19 紀錄此 ack 即可。|
| R10-MI-01 | patch round 3 sequencing cascade — R9-MI-01/02/05 task 寫 cross-ref 時 CH 還是 v0.2；R9-INFO-02 task 後升 CH v0.3，但前面 task 寫的 cross-ref 沒回頭改 | 入 9th master cleanup queue；屬 NEW_REQ_16 lint script 自動偵測對象 |
| R10-MI-02 | 同 R10-MI-01 — phase_b_review_log §4 寫時 character_review_log v0.2 / outline_review_log v0.3；後續 task 升 v0.3 / v0.4 沒回頭改 | 同上 |
| R10-MI-03 | 同 R10-MI-01 — PHASE_B v1.2 header note 寫時 B9 v0.3；R9-MI-05 task 升 B9 v0.4 沒回頭改 | 同上 |

**Plus 既有 backlog：**

| 既有 finding | 性質 | 來源 |
|---|---|---|
| R8-INFO-06 | 00_protocol/00_k v0.1 階段 3 仍寫「5 份 QA」（pre-D-043 stale；D-043 升級為 8 份必跑）| Round 8 報告 §10；patch round 2 / 3 故意不處理；C3 starter 直接 ref UD §2.5.3 v0.3 為權威避開 |
| R10-MA-01 ack | user 平行加 NEW_REQ_16/17/18（v0.11）— 屬正當作業 | Round 10 報告 §4.2；本 NEW_REQ_19 明示 authorize |

**Cascade 根因（user 已預料）：**

1. **「Fix one, find two」遞迴模式**：每次 patch round 同輪 sequential task 寫的 cross-ref 不知道後面 task 會升版（已連續 3 輪 patch round 2/3/4 出現同類問題）
2. **缺自動化 cross-ref checker**：所有同步靠 CODEX review + 人類 patch — NEW_REQ_16 lint script 規劃中
3. **架構天生 cross-ref 密集**：~40+ 互相 reference 的檔；每改一個版本需要 cascade 到 5-10+ 處

**處理方式（依 user 拍板 Path A）：**

1. **不再開 patch round 4** — 繼續手動會再 cascade（同 NEW_REQ_16 哲學）
2. **入 9th master cleanup queue** — 9th master 對話接手 Phase D 時，順手處理或留更晚輪
3. **NEW_REQ_16 lint script 實作後**（DEFERRED 至 Phase D）— 屆時自動偵測本 NEW_REQ_19 所列全部 stale + 未來新 cascade
4. **R8-INFO-06 (00_k v0.1) 處理時機：** 配合 Phase C Wave 9 C.3 starter 設計 — C.3 直接 ref UD §2.5.3 v0.3 為權威；00_k v0.2 升版實作可推 9th master 或封版前

**對 Phase C 啟動的影響：** 無 — 4 finding 全屬版本 cross-ref 文檔層級，不影響 /scene-task / /dialogue-write / /qa skill runtime；Phase C Wave 9 三 starter 已寫好可 commit + 進 Wave 10 CODEX 跑 skill 實作。

**未來迭代 trigger 條件（給 9th master / 之後 master 參考）：**

- **trigger A — NEW_REQ_16 lint script 實作完成**（Phase D 期間）→ 跑 lint → 自動 patch / 列出 finding → 9th master cleanup
- **trigger B — 9th master 對話開始 Phase D / 視圖 / 迭代 / 匯出 / 整合 設計**時 → 順手 cleanup R10 殘留（如有 wall-time）
- **trigger C — 封版前最終 cleanup round**（Milestone 4 前）→ 整個 9th master cleanup queue 一次處理

**對既有 spec 的影響（DEFERRED 期間）：** **無**（NEW_REQ_19 純追蹤；DEFERRED 期間不動任何 spec / SKILL.md / starter / protocol）

**處理時機：**
- **短期（Phase C 期間）：** 不處理；Phase C 焦點在 Wave 9 + Wave 10 + Wave 11
- **中期（Phase D 期間）：** 9th master 順手 cleanup（如有 wall-time）OR NEW_REQ_16 lint script 實作後自動處理
- **長期（封版前）：** 整個 9th master cleanup queue 必清

**Owner：** 9th master 對話（接手 Phase D 時順手處理或留更晚輪）

**Cross-ref：**
- NEW_REQ_16/17/18（自動化 QA 工具 3 層架構 — 解決 cascade pattern 的根因）
- R8-INFO-06（00_k v0.1 5→8 報告 stale）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_REPORT.md` v0.1（Round 10 NEAR-GO 紀錄；§7 finding 列表）
- `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_STARTER.md` v0.1（本輪 starter；scope wording 過時造成 R10-MA-01）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1（R8-INFO-06 來源）
- Phase C Wave 9 三 starter（C1/C2/C3）— 不受本 NEW_REQ_19 影響
- 第八輪 master 對話內 user 拍板「Path A: hard-limit accept」紀錄

---

### NEW_REQ_19 9th master 處理紀錄（2026-05-22）

**狀態更新：** 🟡 DEFERRED → 🟢 **PROCESSED**（9th master cleanup queue 處理；待 cleanup verify baseline 確認後可標 ✅ RESOLVED）

**處理時點：** 2026-05-22（9th master 對話接手 Phase D 啟動前；用 grep 全掃 sweep 模式一次性處理避免 cascade）

**處理結果：**

| Finding | 處理 | 落地檔 |
|---|---|---|
| R8-INFO-06（00_k v0.1 → v0.2）| ✅ 已升 v0.2 | `00_protocol/00_k_台詞生產流程協議.md`：5 → 8 報告對齊 D-043；序列順序對齊 UD §2.5.3 v0.3 (09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i)；§6.2 FINAL gate 補 9-status 齊全條件；header v0.1 → v0.2 含 partial supersede via D-043 |
| R10-MI-01（CH skill v0.2 cross-ref 殘留）| ✅ sweep 完成 | `phase_b_review_log.md` v0.5 → v0.6 / `PHASE_B_COMPLETION_REPORT.md` v1.2 → v1.3 / `CODEX_B9_STARTER.md` v0.4 → v0.5 — CH 全部對齊 v0.3 |
| R10-MI-02（character/outline review log 版本 stale）| ✅ sweep 完成 | `phase_b_review_log.md` v0.6 line 140-141：character_review_log v0.2 → v0.3 + outline_review_log v0.3 → v0.4 |
| R10-MI-03（PHASE_B 引用 B9 v0.3 stale）| ✅ sweep 完成 | `PHASE_B_COMPLETION_REPORT.md` v1.3：B9 v0.3 → v0.4 + POST_LOCK_PENDING v0.9 → v0.13 + 工作樹備註對齊 v1.3 當前事實 |
| R10-MA-01 ack | ✅ 9th master 明示 authorize | 確認 user 平行加 NEW_REQ_16/17/18/19（POST_LOCK_PENDING v0.11 → v0.13）屬正當作業；第八輪 master Round 10 starter scope 過時 wording 不算 spec 違反；無新 patch 需要。本紀錄為 ack consolidation |
| AGENTS.md / CLAUDE.md Phase C skill table | ✅ 已更新 | 兩檔「Phase B+ skill（未實作，標 TBD）」表重做：Phase B 4 個 /create-* + Phase C 3 個下游 skill + 3 中文 wrapper + 09_g/h/i 三模板全標 ✅ 已實作；Phase D /iterate-* / /view-* / /export-* / /diagnose / /integrate 明示 TBD（Phase D Wave 12-15 範圍）；CLAUDE.md header v0.1 → v0.2 → v0.3（Round 1 inline patch）；相關 spec 版本對齊（ARCH v1.6 / DECISIONS_LOG v2.0 / TASKS v1.9 / POST_LOCK_PENDING v0.14 + PHASE_C_COMPLETION_REPORT v1.0）|
| 08_a §11.1 5 → 8 修正 (P-009) | ✅ 已升 v0.3 | `08_dialogue_outputs/08_a_台詞版本管理規範.md` v0.2 → v0.3：§11.1 表格從 5 必跑（09_a/b/c/d/e）改 8 必跑（09_a/b/c/d/f/g/h/i）+ 09_e final-gating 必要前置；補序列印出順序 + qa_decision PASS 條件 + FINAL gate 9-status 齊全；user 起手選項「Cleanup queue 全做（含 08_a）」明示同意動 LOCKED 性質模板。R1-MI-04 後再升 v0.4（§3/§6.4/§12.1/§13.4/§17 全 sweep 對齊 9-status gate）|

**Round 2 NO-GO inline patch round 處理紀錄（2026-05-22）：**

| Finding | 結果 | 落地 |
|---|---|---|
| R2-MAJOR-01（D5 /iterate-scene D-053 block 缺 external_action_required）| ✅ 修 | D5 v0.2 → v0.3 line 241 補 external_action_required phase_log 指示對齊 /iterate-detailed-outline + D1-D4 |
| R2-MAJOR-02（D5 line 76 frontmatter「下游 8 欄」與 SPEC §5.2 衝突）| ✅ 修 | D5 v0.3 line 76 + line 245 「下游 8 欄」→「上游/靜態檔三欄」對齊 SPEC §5.2 + 06_a 模板實際 frontmatter |
| R2-MAJOR-03（check_paths 247 vs 預期 239）| 🟢 hard-limit accept | sandbox baseline 239 屬 false negative；Windows 247 為事實 baseline；屬 NEW_REQ_9 既有 baseline debt（27 模板 old-style filename reference 大寫格式 01A/01B/02A/05D 等）；屬 LOCKED 模板需 D-NNN 拍板，推 10th master |
| R2-MINOR-01（D1-D3 active 段舊檔名）| ✅ sweep | D1/D2/D3 v0.2 → v0.3 indirect 反查表 4 處 path 對齊實際 repo |
| R2-MINOR-02（D1/D2 create-character v0.3 → v0.4）| ✅ sweep | D1/D2 v0.3 共 3 處 active reference 對齊 v0.4 |
| R2-INFO-01（14 files diff vs 13 files）| ✅ ack | Round 2 review starter +1；protected-area diff PASS |
| R2-INFO-02（Round 1 patch trailing whitespace）| 🟢 留 future cleanup | 屬 patch hygiene；不阻 Wave 13 |

**Round 3 NEAR-GO inline patch（2026-05-22 — Round 3 後 trivial wording 修補）：**

| Finding | 結果 | 落地 |
|---|---|---|
| R3-MAJOR-01（D5 line 76 + line 245 含 8-欄 mention 精確詞串；strict grep 即使在否定句仍命中）| ✅ 修 | D5 v0.3 → v0.4：line 76 + line 245 把該 mention 改為具體 7+1 欄列舉（pipeline_state / mode_tag / qa_decision / qa_type / source_task / source_dialogue / source_dialogues / scene_id）；header note v0.4 也避用該精確詞串 |

**Round 4 NEAR-GO（2026-05-22）— R4-MAJOR-01 hard-limit accept：**

| Finding | 結果 | 落地 |
|---|---|---|
| R4-MAJOR-01（`HEAD~2..HEAD` diff window 觸及 Round 3 review report；屬 starter 寫的 diff anchor 不精確 — 假設 commit composition 3 commits，實際 4 commits）| 🟢 hard-limit accept | CODEX 已用 `HEAD~1..HEAD` 確認真實 R3 inline patch + R4 starter scope 乾淨（3 檔：D5 + POST_LOCK_PENDING + Round 4 starter）；Round 3 review report 屬 9th master 工作流自然 immutable history；user 完全沒動其內容；hard-limit accept 屬 starter wording 設計缺陷不是 spec regression |
| R4-INFO-01 | ✅ ack | `HEAD~1..HEAD` 真實 scope 乾淨 — 輔助證據支持 R4-MAJOR-01 hard-limit accept |

**Round 3 + Round 4 NEAR-GO 視為 GO 條件（依 user 拍板路徑）：**
- R3-MAJOR-01 已 RESOLVED (D5 v0.4 strict grep 0 matches)
- R4-MAJOR-01 hard-limit accept (diff anchor 設定問題；非真實 regression)
- check_paths 247 ERROR 維持（R2-MAJOR-03 hard-limit accept）
- 0 真實 protected-area diff regression (HEAD~1..HEAD scope 乾淨)
- 0 新 spec regression
- 9th master 視為 GO → 進 Wave 13 (採新模式：master 寫 D6 完整 + CODEX batch 寫 D7-D9)

**Round 2 教訓內化（HANDOFF_TO_10TH_MASTER 紀錄）：**

1. **Master 跑 baseline 必須以 Windows 端為權威**：sandbox virtiofs cache 在某些 check_paths case 會產 false negative；sandbox 跑出的 ERROR 數低於實際；只能作 noise 對照
2. **Cascade sweep 必須擴及 broader pattern grep**：CODEX review 列出的具體 hits 是「sample 抽樣」；master inline patch sweep 必須對全 repo 跑 broader pattern grep 確保 cleanup
3. **Master 寫 starter 時涉及 SPEC frontmatter 段須直接 grep SPEC §5.2 verify**：不可憑記憶寫具體欄位數字
4. **Master 寫 supersede note 時要避免重複 finding 內精確詞串**：strict grep 不分否定句 / 歷史 narrative；wording 應描述「修補性質」而非重述被改的字串本身（Round 3 R3-MAJOR-01 教訓）
5. **Master 寫 review starter 時 diff anchor 必須精確**：不要假設 user commit composition；`HEAD~N..HEAD` 的 N 設定必須考慮可能含 review report commit；推薦改用「明示 commit hash」（如 `<round-N-baseline-commit>..HEAD`）或「`HEAD~1..HEAD` 限定最後一個 commit」；避免 diff window 多框住 immutable history 造成 false MAJOR finding（Round 4 R4-MAJOR-01 教訓）

**未處理項（推 10th master）：**

- NEW_REQ_16 lint script 實作仍 DEFERRED（短期可於 Phase D 期間考慮；長期屬 11+ 輪 master 範圍）
- NEW_REQ_9 既有 check_paths baseline debt — 27 模板 old-style filename reference（大寫 01A/01B/02A/05D 等格式）；屬 LOCKED 模板需 D-NNN 拍板；推 10th master 評估
- R2-INFO-02 Round 1 patch trailing whitespace 殘留（屬 patch hygiene；不阻運作）

**「Fix one, find two」cascade pattern 預防紀律（9th master 內化）：**

- ✅ patch round 開始前用 grep 全掃所有 stale cross-ref；列出所有 active stale；一次性 sweep（vs 第八輪 patch round 2/3 局部修補導致 cascade）
- ✅ 每個 patch task 開始前先決定本輪所有檔案的目標版本；統一 cascade
- ✅ patch round 結束前再跑 grep 全掃 verify
- 未來：等 NEW_REQ_16 lint script 實作後自動化

**Owner ack：** 9th master 對話（依 user Path A hard-limit accept + cleanup queue 全做選項拍板執行）

---

## NEW_REQ_20 — Phase A.0F F1 Dashboard 三欄區 spec drift + data 過時 + 入口待後續 UI（RESOLVED — 11th master frontend cycle F1-2 + F1-3a 落地；F1-3b backend 拆 NEW_REQ_44）

**狀態（11th master frontend cycle 2026-06-01 更新）：** 🟢 **RESOLVED（前端部分）**
- **F1-1**（W=2 數字）：✓ 合理，不動（原結論成立）。
- **F1-2**（7 module row「入口待後續 UI」placeholder）：✅ 落地 — `ProjectDashboard.js` renderModuleStatus 動作欄改 CopyCommandButton 複製對應 `/view-*` 指令（W/V→view-world、C/R→view-character `<name>`、P→view-outline、CH/S→view-detailed-outline）。
- **F1-3a**（三欄區 mock content spec drift + 過時）：✅ 落地 — renderTriColumn 改寫對齊 UX_SPEC §11.1.6（標題「待人類裁決 / QA Pending / Canon Δ Pending」+ §11.1.6 空狀態文案 + 移除過時 mock + 誠實標 backend pending）。
- **F1-3b**（backend `/api/dashboard/pending-status` endpoint）：拆 **NEW_REQ_44**（F-A3 audit 揭示需先定義 3 data schema，超出 frontend scope）。
- 對應 frontend cycle Stage 1 audit F-A2 + F-A3；AUDIT_2026Q2_REPORT.md §9。

**原狀態紀錄：** 🔵 **BLOCKED on NEW_REQ_22 outcome**（11th master 對話 A 2026-06-01 reframe — 工具角色轉換成「QA + 初始資料 + 專案管理」+ 外接寫作後，frontend dashboard scope 可能整個 rebuild；本 NEW_REQ_20 patch 屬「為短期 polish 做的 work，audit 結果出來後可能整個 rebuild」風險高；推延到 sandbox Dynamic Workflows audit 結論出來後再評估「對齊 §11.1.6 spec」vs「整個 dashboard scope 重設」；對應 NEW_REQ_22 工具角色轉換戰略落地路徑）

**原狀態紀錄：** 🟡 **DEFERRED**（10th master 第十輪整合對話 2026-05-23 M4 user-test follow-up 發現；推 11+ 輪 master patch；屬封版後 user-test 自然 output）

**時點：** 2026-05-23（10th master Milestone 4 真正封版宣告完成後第一次 M4 user-test 跑前端 F1 Project Dashboard 期間發現）

**提出者：** user（10th master 對話內 M4 user-test 第一次跑 frontend `http://localhost:8765/#/` 報告觀察）

**需求背景：**

10th master Milestone 4 真正封版宣告完成（PHASE_D_COMPLETION_REPORT v1.1 §10）後，user 第一次開瀏覽器跑 F1 Project Dashboard 觀察到 3 個 finding：

| # | Finding | 性質 |
|---|---|---|
| F1-1 | 模組狀態總覽 `W=2 V=1 P=1` 數字顯示 | ✓ **合理**（per SPEC §5.1 W module = W-rules + W-language 兩 sub-entity；ProjectDashboard.js line 10 ENTITY_MODULES 定義；不需要 patch）|
| F1-2 | 模組狀態總覽 7 個 entity row 每行「動作」欄位顯示「入口待後續 UI」aria-disabled link | **設計性延後 placeholder**（ProjectDashboard.js line 325 hard-coded）；UX_SPEC §11.1 未 spec 具體點擊行為；Phase A.0F audit cycle Round 4 GO 接受此 placeholder；11+ 輪 patch 可接到 `/view-*` skill CopyCommandButton 或對應模組目錄 listing |
| F1-3 | 三欄區「Phase A 後段任務 / Phase A.0F UI 進度 / Wave 3 狀態」column + bullet 點 + 「跳轉 09_e 待後續」action | **規格漂移實 bug + 資料過時雙重問題**：(a) Subject mismatch — UX_SPEC §11.1.6 (line 766-783) 要求 status snapshot（待人類裁決 + 09_e ref / QA Pending / Canon Δ Pending），實作是 Phase 開發進度 mock string；(b) bullet 點 data 已過時 — 提到 "B.9 後 real-data acceptance / A.0F.3 進行中 / F3-F7 進行中 / Wave 3 狀態" 等內容，但這些都在 Phase A.0F audit Round 4 GO close-out 前後已完成 |

**根因分析：**

F1-3 屬 Phase A.0F.2 alpha 階段（dashboard 最早期 land）的 placeholder content；當時前端只 land UI 結構但 backend status data API 還沒接通，前端用 hard-coded mock string 占位。Phase A.0F audit cycle 4 輪（Round 1-4）的審查重點在 A.0F.6+ 之後的 feature（F3 Scene Editor / LOCKED race guard / L3 Export Panel / Asset Panel 等），沒回頭重審 A.0F.2 alpha 階段 placeholder 內容是否對齊 spec / data 是否更新。屬「audit cycle 漏掉的 finding」+「M4 user-test 自然抓出的 finding」雙重性質。

**提議方案（11+ 輪 master patch；不本輪做）：**

選 1（推薦）：對齊 UX_SPEC §11.1.6 status snapshot
- 改寫 `_tools/frontend/static/js/components/ProjectDashboard.js` line 339-353 `renderTriColumn()` 三欄為「待人類裁決 / QA Pending / Canon Δ Pending」
- 接 backend status data API（如 `_tools/frontend/server.py` 新增 `/api/dashboard/pending-status` endpoint 反查 `09_e_*` 待裁決紀錄 + `09_a-i` 未跑場景 + Canon Delta 候選清單）
- 「跳轉 09_e」link 改成 column 1「待人類裁決」對應 action（連到 09_e 編輯入口或 placeholder if 09_e edit UI 未實作）
- F1-2「入口待後續 UI」可順手 patch wording 為更友善 placeholder（如「→ 跑 /view-<module>」CopyCommandButton 複製指令）或接到對應 chat dynamic view 入口

選 2：保留現狀 + 在 dashboard 加 disclaimer
- 在 dashboard 頁面頂端加「⚠ 三欄區目前為 Phase A.0F alpha 階段 placeholder；待 11+ 輪 master patch」warning banner
- 短期 patch wording 不接 backend；只標示狀態給 user 看
- 屬「快速修補不阻封版」性質

選 3：完全移除三欄區 + 改為空狀態
- 移除 `renderTriColumn()` call；dashboard 7 段順序少一段
- 等 11+ 輪 master 有 backend status API 時再加回
- 屬「最少誤導 user」策略

推薦選 1（完整 patch；對齊 spec + 接 backend）— 屬 11+ 輪 master 中工時 task；估 frontend 1-2h + backend 2-3h + test 1-2h

**對既有 spec 的影響（本輪 DEFERRED 期間）：**
- 不動 LOCKED spec（UX_SPEC v0.4 既有 §11.1.6 wording 已是正確規格；本 NEW_REQ 是實作對齊 spec 的 patch）
- 不動既有 51 SKILL.md / 27 模板 / 9 QA 模板 / 3 registry
- frontend code 屬 `_tools/frontend/` scope；不屬 LOCKED spec 範圍；patch 不需開 D-NNN 拍板

**對 Milestone 4 真正封版宣告的影響：** **無**
- M4 真正封版條件 1「Phase A.0F 11 個 feature 全 PASS + 整體驗收 + integration test + user manual v0.2」已 ✓ 達成（commit `a13ce5a` + audit Round 4 GO commit `2ed48f3`）
- F1 Dashboard 11 feature 之一屬「FINAL」狀態（user manual v0.3 line 35）；但 dashboard 內部 sub-region（三欄區）的 alpha 階段 placeholder 屬 Phase A.0F.2 早期 land 殘留；audit cycle 沒 flag 為 Major/Minor finding
- M4 真正封版宣告不需 partial supersede；本 NEW_REQ 屬封版後 user-test 自然 follow-up（NEW_REQ_14 機制的早期 sister case；屬同模式 user-test trigger 新 NEW_REQ）

**處理時機：**
- **短期（本輪 DEFERRED）：** 不動 frontend code；屬 11+ 輪 master scope
- **中期（11+ 輪 master 對話）：** 11th master 接手時可順手 patch（屬 Phase A.0F follow-up）；建議在 NEW_REQ_16 lint script spec 規劃完成後 / 或 user M4 user-test 跑量產期間順手處理
- **長期：** 若 11th master 未 patch，推 12+ 輪持續 monitor

**Owner：** 11+ 輪 master 對話（依 user 拍板實際 patch 啟動）

**Cross-ref：**
- `_design/UX_SPEC.md` v0.4 §11.1.6 三欄區 spec（line 764-783 status snapshot 規格）+ §11.1.5 模組狀態總覽 spec
- `_tools/frontend/static/js/components/ProjectDashboard.js` line 292-335（renderModuleStatus）+ line 337-377（renderTriColumn）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.1 §10.2 條件 1（Phase A.0F 11 feature 全 PASS；F1-3 屬 audit cycle 漏掉 finding；不阻封版）+ §10.2 條件 8（M4 user-test 屬封版後活動）
- `_design/HANDOFF_TO_11TH_MASTER.md` v1.0 §3 路徑 B（11+ 輪 master 推薦工作）+ §7.1 立即可做的事（M4 user-test）
- NEW_REQ_14 PHASE_X §6 AI-assisted 補入機制（本 finding 屬 M4 user-test follow-up 第一個正當 case；觸發 NEW_REQ_14 機制；後續可考慮跟 §6 補入機制 batch 處理）

---

## NEW_REQ_21 — pre-generation 文風錨定機制後續維護（PROCESSING — 核心實作已透過 D-055 落地；以下為後續維護與擴張議題）

**狀態：** 🟢 **PROCESSING**（核心實作透過 D-055 落地完成；後續維護議題待 NEW_REQ trigger 時逐項處理）

**時點：** 2026-05-28（10th master 第十輪 D-055 拍板同日）

**提出者：** 第十輪 master + user（拍板方案 A 重量級時明示「未涵蓋議題列入未來 NEW_REQ 候選」）

**需求背景：**

D-055 拍板 pre-generation 文風錨定機制（`01_world/01_d_文風樣本與指紋.md` 新建 / `00_b §1.1 §1.2` 擴充 / `07_a §18.3 §18.4` 擴充 / `/scene-task` + `/dialogue-write` skill 升版 / W-style entity registry 註冊 / Instance handoff package 製作）8 處變更 batch 落地，覆蓋本提案 §10 acceptance criteria 全部核心項。但 RFC §10.5（不在 acceptance scope）+ §11.1（已知風險）+ §11.2（open questions）+ Q4 / Q5 仍有未涵蓋議題屬「成熟期擴張」+「後續維護校準」+「風險追蹤」性質，集中入本 NEW_REQ 追蹤（共 9 子項：5 項源自 §10.5 / §11.2 + 3 項源自 §11.1 風險 + 1 項 T10 inventory carry-over）。

**子項：**

1. **指紋校準頻率（維護紀律）**
   - 每累積 5 個新增 Level（或 user 自訂閾值）重跑 `_tools/fingerprint_analyzer.py`（如未來實作）校準 01_d 指紋
   - 偏差 > 15% 須拍板是否更新基線
   - 處理時機：corpus 擴張到 Level 10+ 後逐項評估
   - 對應 RFC §11.1.1 風險（指紋過時風險）

2. **QA 自動量化驗證（未來 NEW_REQ 候選；屬成熟期功能）**
   - 句長 / 標點 / 特徵詞偏差自動 FAIL — 屬未來增強
   - 當前 09_b（角色聲線一致性檢查）仍走定性檢查
   - 處理時機：D-055 落地後實際使用一段時間，user 抓出 09_b 定性檢查漏網案例後評估
   - 對應 RFC §10.5「不在 acceptance scope」第 1 項 + RFC §11.2 Q2

3. **`/anchor-style` 新 skill（未來 NEW_REQ 候選）**
   - 自動更新 01_d 指紋
   - 屬 D-053 scope 擴張議題
   - 處理時機：若指紋校準頻繁度高、人工編輯成本過大時觸發
   - 對應 RFC §10.5「不在 acceptance scope」第 2 項

4. **第三方全知敘述者規範（未來 NEW_REQ 候選）**
   - 序章 / 終章 / cut-scene 若需全知敘述，另立 `01_e_全知敘事規範.md` 或併入 01_d 加第四層
   - 本作目前無此層需求；屬未來擴張
   - 處理時機：作品實際需要全知敘述場景時觸發
   - 對應 RFC §10.5「不在 acceptance scope」第 3 項 + RFC §11.2 Q3

5. **諾拉 17 個技術詞同步 02_a（小修；後續一致性檢查）**
   - 諾拉指紋的 17 個技術詞（材料 / 實驗 / 控制 / 能源 / 核心 / 系統 / 研究 / 效率 / 修復 / 晶片 / 設備 / 物資 / 只要 / 還有 / 一邊 / 可以 / ...）需檢查交叉一致性與 `02_vocabulary/02_a_專有名詞表.md`
   - 若不在 02_a 出現，評估是否補入正式名詞表
   - 處理時機：T10 Instance handoff 落地後可順手檢查；屬實作 follow-up 性質
   - 對應 RFC §11.2 Q4

6. **破格模式 escape hatch（00_b §1.2 補丁；屬 T1 後續補丁不在 T10 scope）**
   - 若 01_d 規範把 trial 版本綁太死，會壓抑「破格模式」（00_a §3.7）
   - 建議：00_b §1.2 加註「破格模式可暫時越界，由人類裁決」
   - 為何要追蹤：T1 已寫 00_b §1.1 §1.2 schema 但沒加破格 escape；屬於回頭補丁性質；不追蹤會在實際跑 `/dialogue-write --experimental` 時碰壁
   - 處理時機：T1 後續補丁；可開新 D-NNN patch 或併入 11+ 輪 master cleanup batch；不在本輪 T10 scope
   - 對應 RFC §11.1.2 風險（指紋過嚴風險）

7. **階段聲線變化追蹤（01_d 新增章節 # 6；可於 T10 順手處理）**
   - 4 角色現有指紋是 Level 7-9 階段；後期關係改變 / 弧線推進後可能合理漂移
   - 建議：01_d 加「# 6. 階段聲線變化追蹤」§（對齊 03_b §17.1）
   - 為何要追蹤：T10 Instance 01_d 落地時若沒處理，後期作品推進到 Level 15+ 角色關係質變時，指紋會 false-positive flag 所有合理漂移
   - 處理時機：T10 Instance handoff package 落地時可順手處理；若 T10 已落地，本子項標 ✅ 已於 T10 處理（落地於 01_d # 6）；否則 NEW_REQ_21 PROCESSING 狀態續延
   - 對應 RFC §11.1.3 風險（角色聲線漂移問題）

8. **諾拉旁白特例明示（01_d # 3.4 子節加註；可於 T10 順手處理）**
   - 諾拉有 7 行短旁白（多為 3-5 字行為），是否屬「主角旁白」例外？
   - 建議：01_d # 3.4 諾拉子節加註「諾拉旁白限自身物理動作短句，禁延伸環境描述；不違反『旁白優先歸主角』跨層硬約束 — 諾拉短旁白是『角色行為自述』性質，主角旁白是『場景視角描述』性質」
   - 為何要追蹤：T10 Instance 01_d 落地時若沒明示，下游 `/scene-task` 抽諾拉指紋時會混淆兩條規則
   - 處理時機：T10 Instance handoff package 落地時可順手處理；若 T10 已落地，本子項標 ✅ 已於 T10 處理（落地於 01_d # 3.4）；否則 NEW_REQ_21 PROCESSING 狀態續延
   - 對應 RFC §11.1.4 風險（諾拉旁白特例的爭議）

9. **既有 instance task packs 升級工具（N/A — 本 batch 落地時 Instance 端 inventory 0 個既有 task packs）**
   - T5 改 07_a 模板後，既有 instance per-scene task packs（如 `CH01_S01_*.md`）不會自動 inherit §18.3 §18.4
   - **T10-d inventory 結果：** `D:\劇本開發\game-script-A\07_scene_tasks\` 含 1 個模板檔 + **0 個 per-scene task packs**
   - **結論：N/A** — 無既有 instance task packs 需要升級
   - 未來 user 新建 task packs 時將自動 inherit T5 落地的 §18.3 §18.4 結構（從 07_a 模板 fork）；無 carry-over 升級需求
   - 處理時機：**已 RESOLVED via N/A**（不需 future trigger；若未來 user 大量產出 task packs 後再回頭需要 schema migration，再開新 NEW_REQ）
   - 對應 K-05（既有 task packs 不會自動升 §18.3 §18.4 概念追蹤；T10-d 證實 Instance 端 0 個既有 → K-05 同步降級為 N/A）

**T10-d Instance inventory 註記：**

子項 9 與 K-05（carry-over）的「既有 task packs 升級議題」在 T10-d inventory 階段確認為 N/A（Instance 端 0 個既有 per-scene task packs）。本議題在本 batch 落地週期內無實際 trigger；但未來 Instance 端 task pack 量產後仍需重評（若量產時 07_a 模板已升 v0.2+ 含 §18.5 之類新子節，仍可能有 carry-over 議題）— 屬「條件性 future NEW_REQ」性質，不入本 NEW_REQ_21 子項。

**未涵蓋（屬更深遠擴張，目前不入 NEW_REQ）：**

- 跨作品文風樣本庫（Template 端議題；與本 instance 無關；屬 Template 工具 fork scope）— 對應 RFC §10.5 第 4 項
- AI 自動取樣選樣本（樣本選擇需 human-in-the-loop）— 對應 RFC §10.5 第 5 項
- 負例樣本從通用 LLM 預設輸出抽取（design-time 反模式 vs 真實 corpus 負例的差距）— 對應 RFC §11.2 Q5

**對既有 spec 的影響：**
- **0 LOCKED spec supersede**（本 NEW_REQ 僅追蹤後續維護議題；D-055 已落地核心；既有 D-001~D-055 拍板結論全不動）
- 子項 6 落地時可能觸發新 D-NNN（00_b §1.2 加 escape 註）；屬未來 patch 範圍，本 NEW_REQ 只追蹤
- 子項 7 / 8 落地路徑在 Instance 端 01_d；不影響 Template / LOCKED spec
- 子項 1 / 2 / 3 / 4 屬「未來 NEW_REQ trigger 後評估」性質；evaluator 為當時 master

**對 D-055 落地完整性的影響：**
- D-055 acceptance criteria（RFC §10）核心 8 處變更**不依賴**本 NEW_REQ；D-055 可獨立宣告完成
- 本 NEW_REQ 屬「D-055 落地後的後續維護紀律」+「D-055 未涵蓋風險追蹤」性質
- 即使本 NEW_REQ 永久 PROCESSING，不阻 D-055 RESOLVED 宣告

**處理時機：**
- **本輪短期（T10 可順手處理）：** 子項 5（諾拉 17 技術詞檢查）、子項 7（階段聲線變化章節）、子項 8（諾拉旁白特例明示）
- **本輪後續補丁（11+ 輪 master 或新 patch round）：** 子項 6（00_b §1.2 加 escape 註）
- **中期（依 corpus 擴張節奏）：** 子項 1（指紋校準頻率，Level 10+ trigger）
- **長期（依使用痛點 trigger）：** 子項 2 / 3 / 4（QA 自動量化 / /anchor-style / 全知敘述者）

**Owner：** 第十輪 master 開立 + 後續使用過程 user / 未來 master 依 trigger 逐項處理

**Cross-ref：**
- `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1 §10.5（不在 acceptance scope）+ §11.1（已知風險）+ §11.2（Open questions）
- `_design/STYLE_ANCHOR_IMPL_STARTER.md` v0.1 §4（Q1-Q5 拍板紀錄）
- `_design/DECISIONS_LOG.md` §6.18 D-055（本拍板）
- `01_world/01_d_文風樣本與指紋.md` v0.1（Template schema-only）+ instance handoff package（具體指紋）
- `02_vocabulary/02_a_專有名詞表.md`（子項 5 對齊檢查目標）
- D-053（D-053 scope 不擴大；`/anchor-style` 新 skill 屬 D-053 擴張議題）
- `03_characters/03_b_主要角色聲線卡模板.md` §17.1（子項 7 階段聲線表對齊目標）
- `00_protocol/00_a_台詞生產協議.md` §3.7（子項 6 破格模式語境）

---

## NEW_REQ_22 — 工具角色轉換 + Claude Code Dynamic Workflows audit 路徑（PROCESSING — 11th master 對話 A 戰略落地）

**狀態：** 🟢 **PROCESSING**（11th master 對話 A 2026-06-01 reframe 11th master scope；戰略落地交接文件全 land；audit pipeline 跑動推延到 user bootstrap sandbox + 親跑 Claude Code Dynamic Workflows 完成後）

**時點：** 2026-06-01（11th master 對話 A 內 user reframe；放棄原 NEW_REQ_20 frontend patch 6-task 計畫；改成「寫交接文件 + 後續 REVIEW Claude Code 產出」模式）

**提出者：** user（11th master 對話 A 內主動 reframe；引用另一條對話討論結論作為戰略方向 source）

**需求背景：**

10th master Milestone 4 真正封版宣告完成後，user 在 M4 user-test 階段觀察到核心限制：

- LLM 直接生 dialogue 品質受 base model 影響；工具 A 既有 QA 8 模板 + 三層守則 + Voice Bible 等護欄無法突破品質 ceiling
- 11+ 輪 master 對話累積 tech debt 規模（NEW_REQ_9 baseline 老債 / NEW_REQ_16 lint script 未實作 / 51 SKILL.md 部分可能 dead code / POST_LOCK_PENDING 多項 DEFERRED 狀態未巡檢 / K-NN 表跨 batch 累積未統一 inventory / D-055 編號衝突 manifest / commit 235debb 對 POST_LOCK_PENDING §5.3-§5.12 意外截斷 ~110 行設計史 等）需要大規模 cleanup
- 既有 frontend dashboard 三欄區（NEW_REQ_20）等 Phase A.0F.2 alpha 階段 placeholder 殘留屬「現工具角色未來會被重塑前提下，patch 也短壽」

結論：工具 A 後續定位 = QA 工具 + 初始資料建置工具 + 專案管理工具；寫作走外部 API / 工具；產出 dialogue 接回工具 A 跑 QA 8 模板 + 09_e 人類拍板紀錄 + 升 FINAL 流程。

**戰略方向（11th master 對話 A reframe 結論）：**

| 維度 | 原計畫（10th master HANDOFF_11TH_PARALLEL_SETUP）| 新計畫（NEW_REQ_22 reframe）|
|---|---|---|
| 工具 A 角色 | 自動寫作 pipeline | QA + 初始資料建置 + 專案管理 + 外接寫作 |
| 11th master 對話 A scope | 跑 NEW_REQ_20 frontend patch 6 步驟 | 寫戰略落地交接文件 + 後續 REVIEW Claude Code 產出 |
| 11th master 對話 B scope | M4 user-test follow-up + NEW_REQ_14 §6 補入 | 退場（M4 user-test 屬「為將被替換的 in-tool 寫作 pipeline 做 test」ROI 大降；推延到大重構完成 + 工具新角色定型後再跑）|
| 11th master 對話 C scope | Codex CLI 量產台詞 skill chain | 退場（外接寫作後此量產 path 即將被替換）|
| Tech debt cleanup | 等 NEW_REQ_16 lint script 落地後自動處理 | 用 Claude Code 2026-05-28 ship 的 Dynamic Workflows（1000 subagent 並行 audit / screening）跑 sandbox 大重構 |
| Sandbox 性質 | n/a | D:\劇本開發工具\_sandbox\snapshot\（在 production 子目錄；.gitignore 排除；audit 結論走人工 transcribe 回 production）|

**提議方案：**

11th master 對話 A 戰略落地 6-task 包（已 land；本 NEW_REQ_22 即該 6-task 結論）：

1. `_design/SANDBOX_REFACTOR_PLAN.md` v0.1 — 含 sandbox bootstrap 指引 + 11 audit 任務 spec（Cat A 冗餘 / Cat B 做一半 / Cat C 漂移 / Cat D Template-Instance 同步）+ first-run 建議 A1 + B4 + C1 + 結論回流流程
2. 本 POST_LOCK_PENDING v0.21 → v0.22 partial supersede — restore §5.3-§5.12 + 加 NEW_REQ_22 entry + 加 §5.13/§5.14/§5.15
3. `_design/HANDOFF_TO_11TH_MASTER.md` v1.0 → v1.1 — §9 amendment 紀錄 scope reframe
4. `_design/HANDOFF_11TH_PARALLEL_SETUP.md` v0.1 → v0.2 — header note 紀錄並行模式廢止
5. 建根 `.gitignore` 加 `/_sandbox/` 排除
6. 建 `_sandbox/README.md` — sandbox 根目錄指引

**對既有 spec 的影響：**

- 不動 10 LOCKED spec / D-001~D-055 拍板結論 / 51 SKILL.md / 27 模板 / 9 QA 模板 / 3 registry / 00_protocol 任何檔
- POST_LOCK_PENDING 升 v0.22 partial supersede 屬「設計史層」非「設計層」變動
- 不擅自啟新 D-056+ 拍板（audit 結論若觸發拍板需求 → user 拍板後落地）
- frontend code 不動（NEW_REQ_20 patch BLOCKED on 本 NEW_REQ_22 outcome）

**對 Milestone 4 真正封版宣告的影響：** **無**

- M4 真正封版條件 1-8 已 ✓ 達成（PHASE_D_COMPLETION_REPORT v1.1 §10.2）
- 本 NEW_REQ_22 屬封版後維護期戰略性轉向；不需 partial supersede 封版宣告
- M4 user-test 推延符合「封版後 user-test 屬封版後活動」紀律（NEW_REQ_14 機制保留待未來新 phase 結束時用）

**處理時機：**

- **本輪（11th master 對話 A 戰略落地）：** 6-task 包全 land + GIT SUMMARY 給 user
- **下階段（user 親跑 Claude Code Dynamic Workflows）：** sandbox bootstrap + first-run A1 + B4 + C1 audit + 帶 report 回對話 A
- **後續（master REVIEW + 結論 transcribe）：** 依 audit ROI 評估擴大 second-run / third-run；可能跑數週至數月
- **長期：** audit pipeline 跑完 11 任務 → 工具 A 進入「QA + 初始資料 + 專案管理工具」穩定維護期

**Owner：** 11th master 對話 A（戰略落地交接 + 後續 audit report REVIEW + 結論 transcribe）/ user（sandbox bootstrap + 親跑 Claude Code）

**Cross-ref：**
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（本 NEW_REQ_22 戰略落地核心檔；含 11 audit 任務 spec + sandbox bootstrap + first-run 建議 + 結論回流流程）
- `_design/HANDOFF_TO_11TH_MASTER.md` v1.1（§9 amendment 紀錄 scope reframe；本 NEW_REQ_22 對應）
- `_design/HANDOFF_11TH_PARALLEL_SETUP.md` v0.2（header note 紀錄並行模式廢止；對話 A reframe / 對話 B C 退場）
- 根 `.gitignore`（11th master 對話 A 新建；加 `/_sandbox/` 排除）
- `_sandbox/README.md`（11th master 對話 A 新建；sandbox 根目錄指引）
- NEW_REQ_20（改標 BLOCKED on NEW_REQ_22 outcome；frontend dashboard patch 推延到 audit 結論出來後）
- NEW_REQ_21 STYLE_ANCHOR PROCESSING（v0.21 落地；本 v0.22 不變動其 entry；sandbox audit C1「D-055 編號衝突 audit」會涵蓋 STYLE_ANCHOR D-055 vs 原 D-054 §6.17.2 預留 D-055 號議題）
- NEW_REQ_14 PHASE_X §6 AI-assisted 補入機制（推延；M4 user-test 退場期間機制保留）
- NEW_REQ_16 lint script（audit B 類 finding 可能對 lint script spec 提供需求輸入；屬未來 master scope）
- CLAUDE.md 教訓 6（長 multi-byte 檔 truncation 風險；commit 235debb 對本檔 §5.3-§5.12 manifest；詳 §5.15 audit trail）
- 外部 reference：Claude Code Dynamic Workflows 公告（2026-05-28；研究預覽期；1000 subagent 上限）

---

## NEW_REQ_24 — 角色 view 檔名 hyphen `角色-<name>` vs underscore `角色_<name>` design 拍板（RESOLVED via Option 1 — 11th master frontend cycle 統一 underscore）

**狀態（11th master frontend cycle 2026-06-01 更新）：** 🟢 **RESOLVED via Option 1（hyphen → underscore）**
- **拍板**：user 拍 Option 1（統一 underscore，對齊 5 LOCKED spec 權威）。F-B1 audit 確認 commit `b94f741`（Wave 14, data-format-specialist-v2）的 hyphen 選擇 **無任何 documented rationale**（commit message 無解釋；無 D-NNN 紀錄）→ per handoff §2.2「audit 未揭示新 reasoning → Option 1」。
- **不需 D-NNN**：Option 1 不修改 LOCKED spec（5 LOCKED spec 已是 underscore），故在 frontend cycle scope 內，無需 D-056（且 D-056~D-061 已由對話 B 預留）。
- **落地**（canonical/runtime refs → underscore）：`export-character/SKILL.md` 16 refs + L231 directive 反轉（改為「canonical = underscore；reverses Wave 14 hyphen commit b94f741」）；`CLAUDE.md` L89 + `AGENTS.md` L153；`CODEX_D_EXPORT_BATCH_STARTER.md` 5；`CODEX_D_FINAL_STARTER.md` 1；`HANDOFF_11TH_PARALLEL_SETUP.md` 1；`PHASE_D_COMPLETION_REPORT.md` 2。
- **刻意保留 hyphen**（discussion/history refs）：本 NEW_REQ_24 entry 下方 option 比較表（歷史紀錄）+ `FRONTEND_DIALOGUE_KICKOFF.md` L80（audit task 描述）+ `export-character/SKILL.md` L231 反轉 directive 內「Do not write `角色-<name>.md`」一處。
- 對應 frontend cycle Stage 1 audit F-B1；AUDIT_2026Q2_REPORT.md §9。

**原狀態紀錄：** 🟡 **DEFERRED**（11th master 對話 A second-run audit 期間發現；audit memo 低估 scope；推 frontend dialogue 接手）

**時點：** 2026-06-01（11th master 對話 A second-run audit cycle Stage 4 採納拍板期間發現 scope expansion）

**提出者：** 11th master 對話 A（second-run Stage 2 REVIEW memo §2 #4 → Stage 4 採納 verify 時補 scan 全 repo 發現實際 scope ~27 refs，遠超 memo 估的 2 doc fix）

**需求背景：**

11th master second-run audit Stage 2 REVIEW memo §2 #4 標：

- Audit 原述：「IC/ARCH/UX 三方分歧 vs CLAUDE/AGENTS 連字號離群」
- Cross-check 修正：ARCH 純底線；真相是 CLAUDE.md L89 + AGENTS.md L153 連字號離群（vs IC/ARCH/UX/SPEC/UPSTREAM 5 LOCKED spec 都用底線）
- 推薦：A 統一底線（改 2 檔）

但 Stage 4 採納時 master 補做全 repo scan 發現實際 scope：

| 用底線 `角色_<name>`（13 refs）| 用連字號 `角色-<name>`（27 refs）|
|---|---|
| `_design/IC` L886 / `SPEC` L1270 / `UPSTREAM` L6100 / `UX` L590/L651/L652/L789/L1581/L2645/L2646/L2648 / `.claude/skills/view-character/SKILL.md` L198 / `_user_manual/01_tool_overview.md` L118 / `_user_manual/02_upstream_skills.md` L48 | `.claude/skills/export-character/SKILL.md` 16 處（**含 L231 explicit Wave 14 directive：「Do not write `view/角色_<name>.md`; the Wave 14 filename is hyphenated as `角色-<name>.md`.」**）/ `CLAUDE.md` L89 / `AGENTS.md` L153 / `_design/CODEX_D_EXPORT_BATCH_STARTER.md` 5 處 / `_design/CODEX_D_FINAL_STARTER.md` L206 / `_design/HANDOFF_11TH_PARALLEL_SETUP.md` L460 / `_design/PHASE_D_COMPLETION_REPORT.md` L137/L281 |

**關鍵發現：** Wave 14 implementer 在 `export-character/SKILL.md` L231 **明寫 explicit directive 反對 underscore**：「Do not write `view/角色_<name>.md`; the Wave 14 filename is hyphenated as `角色-<name>.md`.」— 這屬 runtime 明確設計選擇，非單純 drift。

**這不是 mechanical fix 而是 design 議題：**

- 反轉 Wave 14 implementer 的 explicit 設計選擇需要理解原因（filesystem/URL 慣例？實作偏好？）
- 5 LOCKED spec underscore 屬 4th master era 早期；Wave 14 是 9th master 之後 — 時序上 Wave 14 是 newer canon
- 沒有 D-NNN 拍板紀錄 Wave 14 implementer 為什麼選 hyphen
- Silent 反轉風險：可能 break Wave 14 implementer's intended URL/filesystem behavior

**提議方案（拍板選項）：**

選 1 — A 統一底線（hyphen → underscore；27 refs change）：
- 改 `export-character/SKILL.md` 16 處 + 刪 L231 explicit directive
- 改 CLAUDE.md / AGENTS.md / 4 design/starter/handoff 共 ~10 處
- pros：對齊 5 LOCKED spec 權威；wave 14 drift 清掉
- cons：反轉 Wave 14 implementer's explicit 設計選擇；可能 break intended filesystem/URL behavior；27 refs 大批次

選 2 — B 統一連字號（underscore → hyphen；14 refs change）：
- 改 5 LOCKED spec（IC + SPEC + UPSTREAM + UX_SPEC + 等）共 ~11 refs
- 改 view-character/SKILL.md + 2 user_manual 共 3 refs
- pros：保留 Wave 14 implementer's 設計選擇；runtime → LOCKED spec 對齊
- cons：modifies 5 LOCKED spec（rule 4 needs explicit justification）；逆向 LOCKED authority

選 3（推薦）— defer 到 frontend audit cycle：
- frontend dialogue 跑 AUDIT_PROTOCOL 對 `_tools/frontend/` 時順手 audit 此 finding
- 含 Wave 14 implementer reasoning 的 deeper audit 出來後再決定（如：訪 git blame / commit messages / dev discussion）
- 11th master 對話 A 本 cycle 不處理；NEW_REQ_24 tracking
- pros：collect 更多 context 再決定；不擅自反轉 Wave 14 / 不擅自改 LOCKED spec
- cons：drift 暫時持續

**對既有 spec 的影響（DEFERRED 期間）：無**
- 不動任何檔
- NEW_REQ_24 純 tracking

**處理時機：**

- frontend dialogue 接手 frontend handoff doc 後跑 AUDIT_PROTOCOL Stage 1 audit task 包含本 finding（建議列為 audit scope candidate）
- frontend audit 結論出來後 → frontend dialogue user 拍板 + transcribe

**Owner：** frontend dialogue（11th master 對話 A 推延後接手；user 帶 frontend handoff doc 開新 Cowork dialogue）

**Cross-ref：**

- `_sandbox/audit-reports/AUDIT_2026Q2_CROSSCHECK_MEMO_20260601_1345.md` §2 #4（Stage 2 REVIEW 原識別 + cross-check 修正）
- `_design/AUDIT_2026Q2_REPORT.md` §8.3 deferred row + §8.6 second-run cross-check 修正紀錄
- `.claude/skills/export-character/SKILL.md` L231 explicit Wave 14 directive
- 5 LOCKED spec underscore refs（IC L886 / SPEC L1270 / UPSTREAM L6100 / UX_SPEC 8 處 / view-character SKILL L198）
- 27 hyphen refs（export-character SKILL 16 / CLAUDE/AGENTS / 4 design 檔）

---

## NEW_REQ_25 — `/status` 把 Template skeleton 當實體進度（11th master 對話 B M4 follow-up F1）

**狀態：** 🟡 DEFERRED — 推 Claude Code workflow Wave-A2（依賴 D-059 拍板 template 狀態語意統一）

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain）

**需求背景：** Template skeleton (01_a / 05_a 等) frontmatter 含 `entities: [W-rules]` / `entities: [P]` + 狀態 REVIEW/DRAFT；/status SKILL.md Stage 4 Rule 8 把它們計入「未追蹤實體」；fresh Instance bootstrap 後 W-rules 已顯示 75%（REVIEW score）。

**分類：** 🐛 spec drift bug（template design vs /status calculation logic 沒對齊）；**嚴重度：** 🟠 MAJOR

**提議方案：** 3 修法選項拍板（D-059 候選 — 連動 NEW_REQ_30 同根因）：
- (a) Template 移除 entities 或改 狀態 為新 enum TEMPLATE_SKELETON
- (b) /status SKILL.md Stage 4 Rule 8 加 filename pattern 排除
- (c) 加 phase_log evidence 為計算前置條件

**對既有 spec 的影響：** /status SKILL.md + 7 個 W/V template + 多個 03_/05_ template；D-059 拍板需動 LOCKED template；屬 D-NNN 拍板範圍。

**處理時機：** Wave-A2（D-NNN dependent）

**User workaround：** 無 user-side workaround；user 透過 F6 workaround 部分覆蓋（手動升 狀態）。

**Owner：** Claude Code workflow Stage 2 REVIEW + user 拍板 D-059 → Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.1（完整 verify evidence + Claude Code workflow scope）
- NEW_REQ_30（F6 same root cause；template skeleton 狀態語意 ad-hoc）
- `.claude/skills/status/SKILL.md` Stage 4 Rule 8
- `01_world/01_a_世界觀總覽.md` + `05_plot/05_a_主線大綱模板.md` + 其他 template skeleton

---

## NEW_REQ_26 — `check_paths.py` 247 baseline error 干擾驗證；無 `--changed-only` flag（11th master 對話 B M4 follow-up F2）

**狀態：** ✅ **RESOLVED（Batch 3 工具衛生，2026-06-02，feat/batch3-hygiene）** — `check_paths.py` 加 `--changed-only` / `--base <ref>` / `--baseline <N>` / `--suppress-template-debt` 四 flag + 回歸測試 `scripts/tests/test_check_paths_f2.py`（3 案例）；無 flag 行為與基線完全一致（225 ERROR / exit 1）。零-LOCKED、無 D-NNN。〔INFO backlog：`--changed-only` 的 CJK 路徑比對測試覆蓋可增強（L1 reviewer INFO；非阻擋）〕

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain；每輪驗證撞 247 baseline 干擾判斷本輪新增）

**需求背景：** scripts/check_paths.py monolithic CLI；exit code 1 on any ERROR；無 `--changed-only` / `--baseline <file>` / `--suppress-template-debt` flag；247 baseline 屬 NEW_REQ_9 既有 debt。

**分類：** ⚠ design gap（CLI UX 改進）+ NEW_REQ_9 sister case；**嚴重度：** 🟡 MINOR

**提議方案：** 加 CLI flag：`--changed-only` (git diff base) / `--baseline <file>` (指定 baseline error 數) / `--suppress-template-debt` (排除 NEW_REQ_9 27 模板 old-style refs)；補對應 unit test fixture。

**對既有 spec 的影響：** 不涉 LOCKED spec；scripts/ 行為改進；可併 NEW_REQ_16 lint script 同輪實作省 overlap。

**處理時機：** Wave-A6（封版後維護期；可獨立或併 NEW_REQ_16 lint script）

**User workaround：** user 端跑 diff-only grep（git diff 後 grep 新加 old-style filename）。

**Owner：** Claude Code workflow Stage 3 APPLY / 11+ 輪 master NEW_REQ_16 lint script 同輪

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.2
- NEW_REQ_9（既有 baseline debt 27 模板 old-style filename refs）
- NEW_REQ_16（lint script spec 規劃；推薦合併）
- `scripts/check_paths.py`

---

## NEW_REQ_27 — `/create-world` SKILL.md split rule vs 01_a 實際 section 對不上（CRITICAL；11th master 對話 B M4 follow-up F3）

**狀態：** 🔴 DEFERRED — 推 Claude Code workflow Wave-A2（依賴 D-056 拍板修哪邊）

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain；採保守 workaround 新增 §0）

**需求背景：** `.claude/skills/create-world/SKILL.md` §Split Rules 寫 10.1 世界類型→01_a §1 世界類型 (overwrite) / 10.2→§2 / 10.3→§3 等；實際 `01_world/01_a_世界觀總覽.md` Grep 出 24 個 section heading「§1 文件目的 / §2 與其他文件的關係 / §3 世界觀一句話定義...§24 最終檢查表」— 完全對不上。每個 user 跑 /create-world 必撞。

**分類：** 🐛 spec drift bug（SKILL.md vs LOCKED template 對不上）；**嚴重度：** 🔴 CRITICAL — 直接影響 Phase B 上游 pipeline

**提議方案：** **D-056 拍板必開** — 3 修法選項：
- (a) 改 SKILL.md split rule 對齊 01_a 24 sections（最不動 LOCKED）
- (b) 改 01_a template sections 對齊 SKILL.md（需動 LOCKED template）
- (c) 加 `<!-- PROJECT_WORLD_BASELINE_START -->` anchor markers（user 提案）
- 推薦 (a) + 補 anchor

**對既有 spec 的影響：** (a) /create-world SKILL.md line 263-282；(b) `01_world/01_a_世界觀總覽.md` LOCKED template；(c) 兩邊都動 + 模板加 anchor。

**處理時機：** Wave-A2（D-056 拍板後）；**user 拍板路徑後屬 critical patch**

**User workaround：** 量產期間採 conservative 新增 `# 0. 本作...基線` section（不動模板正文）— 結構性 workaround 非 ad-hoc。

**Owner：** user 拍板 D-056 → Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.3
- NEW_REQ_30（F6 same chain — /create-world 接口）
- `.claude/skills/create-world/SKILL.md`
- `01_world/01_a_世界觀總覽.md`

---

## NEW_REQ_28 — Markdown header 兩空白 hard-break vs `git diff --check` 衝突（11th master 對話 B M4 follow-up F4）

**狀態：** ✅ **RESOLVED（Batch 3 工具衛生，2026-06-02，feat/batch3-hygiene）** — 53 檔 header 欄位行尾端空白確定性 strip（460 行）；`git diff -w` 對 52 純-F4 檔輸出為空 = 純空白、header 值 byte-identical、零語意變更；觸及 INTEGRATION_CONTRACTS / L3_EXPORT_PROMPT_SCHEMA / SPEC / UD 等 LOCKED 檔，經 rule-4 user 核准。零-LOCKED 語意、無 D-NNN。

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產期間累積 57 WARN）

**需求背景：** 模板 header 5 欄多行尾用兩空白做 Markdown hard-break；skill 改「最後更新」就會被 `git diff --check` 報 trailing whitespace。8th/9th master CODEX review 多次 flag 為 R12-MI-01 / R2-INFO-02 INFO/MINOR known issue；POST_LOCK_PENDING line 916/951 已紀錄為 patch hygiene cleanup。

**分類：** ⚠ design gap（模板規範 vs git linter workflow tension；缺統一規範）；**嚴重度：** 🟡 MINOR

**提議方案：**
- (a) 批量 strip 既有檔 header trailing space + 改規範用單行（推薦）
- (b) 寫 lint script 自動 strip header 區
- (c) `.gitattributes` 設特定區段允許 trailing

**對既有 spec 的影響：** 所有 27 LOCKED template + AGENTS.md + CLAUDE.md header 區；不動 LOCKED spec 本體。

**處理時機：** Wave-A1（quick-win；低風險；批量 patch）

**User workaround：** 無；累積 57 WARN（user CYCLE end /status 報告數字）。

**Owner：** Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.4
- POST_LOCK_PENDING §1 既有 R2-INFO-02 / R12-MI-01 紀錄

---

## NEW_REQ_29 — `.protocol_version.template_commit` 直接 fallback TODO（11th master 對話 B M4 follow-up F5）

**狀態：** ✅ **RESOLVED（Batch 3 工具衛生，2026-06-02，feat/batch3-hygiene）** — `/init-project` SKILL.md + `00_i §9.2` 補 template_commit 偵測守衛：先確認 git 可用 + Instance 有 `.git` + 自 clone 後零本地 commit + HEAD 確為 Template commit，才寫 SHA，否則 TODO+WARN；同步 §3.1/§8#9/§7 階段 5 WARN 槽。L1 reviewer 抓出原版 MAJOR（`git rev-parse HEAD` 取 Instance HEAD ≠ Template commit）已修正。零-LOCKED 語意、無 D-NNN。

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產期間 /init-project 跑出 TODO 注意到）

**需求背景：** `.claude/skills/init-project/SKILL.md` line 266「If Template commit is unknown, write `template_commit: TODO`」+ `00_protocol/00_i_專案初始化協議.md` line 313 同；SKILL.md 沒明示 detection step「先試 git rev-parse HEAD」→ agent 直接 fallback TODO。Instance 在 user clone 後自有 .git；可抓 commit hash。

**分類：** 🐛 spec gap / runtime gap（SKILL.md 缺 detection 流程明示）；**嚴重度：** 🟡 MINOR — debug traceability 缺失

**提議方案：** SKILL.md 加 detection step：(a) 試 `git rev-parse HEAD` (b) 若 success 寫該 hash (c) 若 git 不可用或 .git 缺，fallback TODO + 明示 WARN。

**對既有 spec 的影響：** `.claude/skills/init-project/SKILL.md` line 266 + `00_protocol/00_i_專案初始化協議.md` line 313；不涉 LOCKED spec。

**處理時機：** Wave-A1（quick-win；2-3h；低風險）

**User workaround：** 無。

**Owner：** Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.5
- `.claude/skills/init-project/SKILL.md`
- `00_protocol/00_i_專案初始化協議.md`

---

## NEW_REQ_30 — `/create-world` Phase 4 沒升狀態；卡 `/create-character` REVIEW 門檻（11th master 對話 B M4 follow-up F6）

**狀態：** 🟡 DEFERRED — 推 Claude Code workflow Wave-A2（依賴 D-059 拍板；可合 NEW_REQ_25 一起做）

**時點：** 2026-05-25（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain；/create-character 被阻擋）

**需求背景：** /create-character SKILL.md line 70「W-rules, V, and W-language each exist and are at least REVIEW」；/create-world Phase 4 §Frontmatter Rules（line 286-300）只寫 entities/depends_on/weight；完全沒提 狀態 bump；Template skeleton 起始狀態 ad-hoc 混雜（01_a REVIEW / 01_b DRAFT / 01_c REVIEW / 02_a REVIEW / 02_b DRAFT / 02_c REVIEW）。

**分類：** 🐛 spec drift bug（Phase 4 缺 狀態 bump step；Template 起始狀態 ad-hoc；下游 prereq 跟上游 output 不對齊）；**嚴重度：** 🟠 MAJOR — 每個 user 跑 /create-character 必撞

**提議方案：** **D-059 拍板候選**（合 NEW_REQ_25 同根因）— 3 選項：
- (a) /create-world Phase 4 加 狀態 bump step（DRAFT → REVIEW after successful write）
- (b) /create-character 允許 `prereq_waived` flag + 寫 phase_log
- (c) 兩者都做 + Template skeleton 起始狀態語意統一

**對既有 spec 的影響：** /create-world SKILL.md Phase 4 + /create-character SKILL.md prereq check + 7 個 W/V template files 起始狀態語意；屬 D-NNN 拍板範圍。

**處理時機：** Wave-A2（D-059 拍板後；合 NEW_REQ_25 同輪做）

**User workaround：** 量產期間已手動：01_b DRAFT → REVIEW / 02_b DRAFT → REVIEW。

**Owner：** user 拍板 D-059 → Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.6
- NEW_REQ_25（F1 same root cause；template skeleton 狀態語意）
- `.claude/skills/create-world/SKILL.md` + `.claude/skills/create-character/SKILL.md`
- D-053 partial supersede 紀錄（/create-world exception）

---

## NEW_REQ_31 — source/reference 原始素材檔放置規範缺失（11th master 對話 B M4 follow-up F7）

**狀態：** ✅ **RESOLVED via D-063（Wave1 落地，2026-06-02）** — 採方案 A（`_source_materials/` source 慣例）；`/create-character` SKILL.md 引用本慣例落地（Wave1）。〔Wave2 編號更正：本條原寫「依賴 D-057 拍板」，因對話 B 已預留 D-056~D-062，11th master frontend Wave 改用乾淨編號 D-063；D-057 在本批作廢，見 DECISIONS_LOG §6.19.2 D-063〕

**時點：** 2026-05-26（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain；/create-character 撞 source 檔被 parser 阻斷）

**需求背景：** user 把人物完整人設與既有劇本素材放入 `03_characters/`（如 `女_1_瑟琳_人設v_0_1.md` / `05_蟲潮孤島劇本.md.docx`）；.md source 缺 5 欄 header 時被 parser/header/status 流程當正式追蹤文件掃描；spec 從未定義 source material 該放哪；/create-character SKILL.md 寫檔範圍只列 main/minor/npc；check_paths.py IGNORE_DIR_NAMES 沒 source/reference 排除。

**分類：** ⚠ design gap（cross-layer：parser exclude + SKILL.md 寫檔邊界 + entity_type_registry subdirectory + user_manual + AGENTS.md）；**嚴重度：** 🟠 MAJOR — 每個 user 量產撞

**提議方案：** **D-057 拍板候選** — 3 方案：
- A 建立 `03_characters/source/` 並排除 parser（推薦；最 contained）
- B source 仍需 header 但 parser 不視為 entity（用 source_type / canonical metadata）
- C 全域 `_source_materials/characters/` 

**對既有 spec 的影響：** cross-layer：parser scripts/ + 5 個 /create-* SKILL.md + entity_type_registry.yaml + user_manual + AGENTS.md。

**處理時機：** Wave-A2（D-057 拍板後）

**User workaround：** 量產期間補 5 欄 header 給 `女_1_瑟琳_人設v_0_1.md` 等；屬 instance-level 不算 Template patch。

**Owner：** user 拍板 D-063（原誤編 D-057）→ Claude Code workflow Stage 3 APPLY（Wave1 已落地）

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.7（含 user 完整 patch 提案）
- DECISIONS_LOG §6.19.2 D-063（`_source_materials/` source 慣例方案 A；RESOLVED via D-063）
- NEW_REQ_25（F1 sister — parser 掃描範圍 vs entity 語意）
- NEW_REQ_32（F8 cross-cutting — entity registry 邊界）

---

## NEW_REQ_32 — 非人格反派 / 組織型對抗源 entity 缺型別（11th master 對話 B M4 follow-up F8）

**狀態：** ✅ **RESOLVED via D-064（短線 gate / Wave1）+ D-071（長線 ORG-* core / Batch 4 Phase 1，2026-06-02）** — 方向 C 非角色 gate（D-064，Wave1 落地）**＋** 方向 A 新 ORG-* core 型別 Phase 1 floor（D-071：registry root+template append ORG + parser ENTITY_ID_RE/_entity_type_from_id + ORG regression test；ORG-* 成 valid LOCKED core、可手工 author / 被 depends_on / /status 顯示）。兩者組合（gate 攔截 + ORG 正向落點）。〔**Phase 2 已落地**（D-071 後續、SKILL-only；create-character gate 第 3 選項 → live ORG-* + /status ORG opt-in 列舉；DECISIONS §6.24）。**Phase 3 已 RESOLVED via D-074**（2026-06-03 過夜自主長跑，feat/f8p3-audit-batch5）：新 LOCKED 協議 00_n_組織創建協議（mirror 00_l、issue-less）+ /create-org + /iterate-org（無聲線卡、限寫 11_organizations/）+ ORG card 6 段 + 00_l v0.3 C↔ORG endpoint（至多一端 ORG）+ D-050 子裁決 2 append /create-org 列 + expected_entities create_org opt-in + ARCH §3.4 v1.8 + check-gaps v0.2 + 掃描清單補 11_organizations（M3）；§13 七題採推薦預設全入決策佇列、park 在 L3；DECISIONS §6.25。**3c views 部分（view-world ORG compose / 獨立 view-org·export-org）+ 清道夫 R-* opt-in 遷移仍 DEFERRED**（決策佇列）。**方向 B**（W-language 文件語體擴充）仍 DEFERRED。原『依賴 D-058』編號更正見 §6.19.3 D-064。詳設計見 D074_DECISION_PACKAGE / DECISIONS §6.25。**〔amendment 2026-06-03（DECISIONS §6.27）：user L3 拍板 §13 Q1=7 段（加組織結構/層級）+ Q2=issue-ful（00_n 改讀 issue_type_registry 00_n_organization key，7 議題）+ Q6 ratify 禁 ORG↔ORG；上文「issue-less / ORG card 6 段」實況已升 issue-ful / 7 段；多一 LOCKED 觸點 issue_type_registry.template v0.2。〕**〕

**時點：** 2026-05-27（11th master 對話 B M4 user-test follow-up）

**提出者：** user（Codex CLI 對話 C 量產 chain；/create-character 反派B 撞「已破產清算公司只有殘留文件」）

**需求背景：** entity_type_registry core 只 9 種（W-rules / W-language / V / C / R / P / CH / S / A）+ reserved（I / UI / SKILL）；無 F / ORG / Faction / Organization；/create-character SKILL.md 沒 non-character refusal logic；01_a §9「勢力與組織」placeholder 屬 W-rules 子段不是獨立 entity。

**分類：** ⚠ design gap（cross-layer：entity registry 缺 F/ORG type + skill chain 缺 refusal + W-language 缺文件語體擴充）；**嚴重度：** 🟠 MAJOR — 任何含公司/制度/殘留組織的作品都撞

**提議方案：** **D-058 拍板必開** — 3 方向：
- A 新 F-*/ORG-* entity（最 deep；30-50h；涉 entity_type_registry + 11 SKILL.md + parser；推 13+ 輪）
- B 擴 W-language 文件語體卡（中度；5-8h；屬 W-language extension）
- C /create-character Stage 1 加 non-character refusal（最 shallow；1-2h；short-term workaround）
- 推薦 C 短期 + B 中期

**對既有 spec 的影響：** 方向 C：/create-character SKILL.md + 00_f 協議；方向 B：W-language sub-card 擴；方向 A：cross 11 SKILL.md。

**處理時機：** Wave-A4 短中期（方向 C+B）；Wave-A5 long-term（方向 A 13+ 輪）

**User workaround：** user 已停手不寫 C-反派B；後續把「清道夫」公司建為 R-target 而非 C-target（R-清道夫-瑟琳 等 3 R）— ad-hoc workaround。

**Owner：** user 拍板 D-064（原誤編 D-058）→ Claude Code workflow Stage 3 APPLY（方向 C 短期；Wave1 已落地）

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.8（含 user 完整 3 方向提案）
- DECISIONS_LOG §6.19.3 D-064（`/create-character` 非角色 gate SKILL-only；RESOLVED via D-064 方向 C）
- NEW_REQ_31（F7 sister — entity registry 邊界類）
- `_design/registries/entity_type_registry.yaml`

---

## NEW_REQ_33 — 角色卡缺集中式「個性拆解」固定段（11th master 對話 B M4 follow-up F9）

**狀態：** ✅ **RESOLVED（Wave1 落地，2026-06-02）** — voice card 個性拆解段 + 00_f / UD §1.2.2 對應落地。〔Wave2 升格揭露：本條原判「不需 D-NNN」（視為 SKILL-only / 文字微調）；因落地實際觸及 LOCKED UD §1.2.2 + 00_f 議題清單，依「動 LOCKED 必拍 D-NNN」紀律升格，對應 **D-065/D-066**（UD/00_f append + registry append）；見 DECISIONS_LOG §6.19.4/§6.19.5〕

**時點：** 2026-05-28（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間瑟琳/莉娜角色卡實際使用感受；副對話補 patch 後對比明顯）

**需求背景：** /create-character SKILL.md Stage 4 §Split Rules（line 163-172）8 個 voice card sections 全是「聲線技術規格」（角色定位 / 聲線輪廓 / 去名測試 / 合規檢查 / 髒話來源 / 偏移檢查 / 聲線污染 / 與類型氣質合規）；UD §1.2.2 議題 1-8 全部技術 voice 性質；完全沒「個性拆解」固定欄位。

**分類：** ⚠ design gap（spec / SKILL.md / UD 議題 layer 都缺）；**嚴重度：** 🟠 MAJOR

**提議方案：** voice card 新增固定 § 個性拆解（10 子段：表層個性 / 內在個性 / 自尊來源 / 核心恐懼 / 情緒遮掩 / 可愛魅力來源 / 努力與缺陷表現 / 壓力下變形 / 角色差異 / 不可偏移人格模板）；補 00_f 議題 9 + UD §1.2.2 對應 script。

**對既有 spec 的影響：** /create-character SKILL.md Stage 4 §Split Rules + 00_f 協議 + UD §1.2.2；不涉 LOCKED spec。

**處理時機：** Wave-A1（quick-medium-win；4.5-7h；屬 Meta-pattern B chain 一環）

**User workaround：** 量產期間 user 在副對話手動補入「個性拆解」段。

**Owner：** Claude Code workflow Stage 3 APPLY（Wave1 已落地；升格 D-065/D-066 背書）

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.9（含 Wave2 升格加註）
- DECISIONS_LOG §6.19.4 D-065 + §6.19.5 D-066（升格背書；UD/00_f append + registry append）
- NEW_REQ_35 + NEW_REQ_36 + NEW_REQ_37（F11 + F12 + F13 same Meta-pattern B chain）
- `.claude/skills/create-character/SKILL.md` Stage 4 §Split Rules

---

## NEW_REQ_34 — 副對話 / sub-conversation lifecycle UX 規則缺失（11th master 對話 B M4 follow-up F10）

**狀態：** ✅ **RESOLVED via D-072（Batch 4 落地，2026-06-02）** — ARCH §3.3 純新增子節 §3.3.3「Sub-conversation / Parallel-chat 慣例」固化副對話 lifecycle 8 條規則（權威全文）+ 同步 root AGENTS.md / CLAUDE.md v0.6 / `_user_manual/skill_invocation_guide.md` v0.2 短指標。〔原規劃「合 NEW_REQ_38 同 ARCH §3.3 patch」已不適用：F14/NEW_REQ_38 已於前批獨立落地（CLAUDE.md 瘦身 v0.5）；本批 F10 獨立做 §3.3.3 純新增，並對齊 F14 瘦身紀律——root 檔僅放短指標，權威全文留 ARCH。〕

**時點：** 2026-05-28（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間用副對話讀大量素材時撞主 agent 太早關閉副對話）

**需求背景：** ARCH §3.3.0 multi-agent invocation 慣例（D-048）只規範 4 個 agent 環境的 discovery 機制 + invocation 方式；完全沒 sub-conversation lifecycle / 主對話/副對話分工 / 副對話 only-read / 副對話 close 時機規則；grep 整個 repo 沒「副對話」/「次要對話」/「sub-conversation」概念。

**分類：** ⚠ design gap（ARCH §3.3.0 multi-agent invocation 慣例維護擴充；cross-cutting agent UX）；**嚴重度：** 🟡 MINOR-MAJOR — 不阻 runtime 但影響量產 UX

**提議方案：** ARCH §3.3.3「Sub-conversation / Parallel-chat 慣例」新段：8 條規則（只讀不寫 / 明列讀過檔 / 明列未讀限制 / 只給 evidence summary / 主對話負責 skill stage / 不關閉除 user 明示 / reuse 同副對話 / 主對話 wording 範例）+ 同步 AGENTS / CLAUDE / skill_invocation_guide。

**對既有 spec 的影響：** ARCH §3.3 新增 §3.3.3（不動 §3.3.0/3.3.1/3.3.2）+ AGENTS.md + CLAUDE.md + `_user_manual/skill_invocation_guide.md`。

**處理時機：** Wave-A3（合 NEW_REQ_38 同 ARCH §3.3 patch；省 overlap）

**User workaround：** user 端 ad-hoc 提醒 agent 不要關副對話；chat-level instruction 不是 Template patch。

**Owner：** Claude Code workflow Stage 3 APPLY（Batch 4；feat/batch4-entity）

**Batch 4 落地紀錄（2026-06-02）：** F10 由 Batch 4 落地 — ARCH v1.6 → v1.7 純新增 §3.3.3（8 條規則權威全文，0 LOCKED supersede，比照 D-048/D-049 擴充模式）+ AGENTS.md 短指標段 + CLAUDE.md v0.5 → v0.6 短指標段 + skill_invocation_guide v0.1 → v0.2（新增 §7 copy-paste 範本，原 §7/§8 順延 §8/§9）。RESOLVED via D-072（DECISIONS_LOG §6.21）。走四層防線（L0→L1 外審→L2→L3 user 簽字）。

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.10
- DECISIONS_LOG §6.21 D-072（RESOLVED 背書）
- `_design/ARCHITECTURE.md` §3.3.3（權威全文）+ §3.3.0（D-048 invocation 慣例；本段為其 lifecycle 擴充）
- NEW_REQ_38（F14 same Meta-pattern D — Agent context / UX layer；本段對齊其 root 瘦身紀律）
- NEW_REQ_35 + NEW_REQ_37（F11/F13 connected — 副對話是其既有劇本 ingestion 機制）

---

## NEW_REQ_35 — `/create-character` 缺「已寫劇本萃取」input scope（11th master 對話 B M4 follow-up F11；input 層）

**狀態：** ✅ **RESOLVED via D-065（Wave2 落地，2026-06-02）** — UD §1.2.2 + 00_f §10.13/§10.14 既有劇本議題 append + registry core.00_f_character append（連動 D-066）；input scope 擴充落地。〔Wave2 升格揭露：F11 在 M4_USER_TEST_REPORT 原判『不需 D-NNN』；因落地需動 LOCKED UD §1.2.2 + 00_f + registry，升格為必拍，對應 **D-065/D-066**；見 DECISIONS_LOG §6.19.4/§6.19.5〕

**時點：** 2026-05-29（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間補讀莉娜既有劇本後發現聲線規律遠比只讀人設準確）

**需求背景：** /create-character SKILL.md inputs（line 291-299）只列「Long-form character material」+「Answers to dynamic issue questions」；完全沒提「previously-written dialogue / docx / 既有劇本」處理；UD §1.2.2 議題 1-8 沒對應議題。莉娜案例：只讀人設 = 「暴躁技師」；補讀劇本 = 罵人綁定具體技術問題 / 老娘本小姐天才火炮藝術密度需控管 / 可懂火控但不宜搶諾拉定位。

**分類：** ⚠ design gap（skill input scope 擴充；屬 input 層）；**嚴重度：** 🟠 MAJOR — 直接影響角色卡品質；翻拍/續作必撞

**提議方案：** SKILL.md Stage 1/2 擴 input scope：既有劇本 / docx / .txt / .csv / .json 接受；speaker alias matching；docx 讀取規範（fallback warning if 環境不支援）；補 00_f 議題 + UD §1.2.2 對應 script。

**對既有 spec 的影響：** /create-character SKILL.md + 00_f 協議 + UD §1.2.2 + 副對話 reuse 機制（連動 NEW_REQ_34 F10）。

> ⚠ **Errata（11th master 對話 A 2026-06-01 補）：** 本句以上原為對話 B 寫入時截斷的殘句（檔案結尾 mid-word `連動 NEW_REQ_34 F`），對話 A 依 NEW_REQ_34 = F10 副對話補完。另：v0.25 header 宣稱新增 NEW_REQ_36-43（8 entries）+ §5.20 + §5.21，但這些 **entry body / section 從未實際寫入本檔 body**（僅存在於 header 版本註記與少數 cross-ref）；屬對話 B wrap-up 未完成的結構缺口，待對話 B 後續 cycle 補。對話 A 本次只補入下方 NEW_REQ_44 / NEW_REQ_45（frontend cycle 自身 entry）+ 修 v0.26 header §5.22 不實陳述。

**Wave2 落地紀錄（WI-B；2026-06-02）：** F11 input scope 由 **WI-B**（既有劇本 input scope work item）落地 — UD §1.2.2 append 既有劇本角色設定承接議題 + 00_f §10.13 子節 + registry core.00_f_character id 9（連動 D-066）。RESOLVED via D-065/D-066。

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.11（含 Wave2 升格加註）
- DECISIONS_LOG §6.19.4 D-065（UD/00_f append；含升格揭露）+ §6.19.5 D-066（registry append）
- NEW_REQ_37（F13 output 層；**同輪 Wave2 實作**）
- NEW_REQ_33 + NEW_REQ_36（F9 + F12 same Meta-pattern B chain）

---

## NEW_REQ_36 — 聲線卡缺「Source Coverage / Downstream Hooks」固定尾段（11th master 對話 B M4 follow-up F12；output 層）

**狀態：** ✅ **RESOLVED（Wave1 落地，2026-06-02）** — voice card § Source Coverage / Downstream Hooks 固定尾段 + 00_f / UD §1.2.2 對應落地。〔Wave2 升格揭露：F12 原判「不需 D-NNN」（視為 SKILL-only）；因落地觸及 LOCKED UD §1.2.2 + 00_f 議題清單，升格對應 **D-065/D-066**；見 DECISIONS_LOG §6.19.4/§6.19.5〕

**時點：** 2026-05-29（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間瑟琳/莉娜案例實測 — source 檔大量下游素材 Stage 3 chat 顯示後 Stage 4 寫檔消失）

**需求背景：** /create-character SKILL.md Stage 3 line 136 有「Downstream notes」概念但只在 chat preview 出現，line 324 明示「without granting writes to those files」；Stage 4 §Split Rules（line 163-172）8 個 voice section 完全沒「Source Coverage / Downstream Hooks」固定欄位 → Stage 3 chat 顯示的 downstream notes → Stage 4 寫檔消失 → 下游 skill 拿不到 hooks。

**分類：** ⚠ design gap（skill output structure；屬 output 層）；**嚴重度：** 🟠 MAJOR — user 拍 priority HIGH

**提議方案：** voice card 新增固定 § Source Coverage（或 § 原始設定覆蓋與下游素材摘要）含 5 子段：
1. 已吸收進聲線主體的 source 資訊
2. 交給 /create-relationship 的 hooks
3. 交給 /create-outline / /create-detailed-outline 的 hooks
4. 交給 /scene-task 的 hooks
5. 不應直接當台詞使用的 source 資訊
+ 補 00_f 議題 + UD §1.2.2 對應 script。

**對既有 spec 的影響：** /create-character SKILL.md Stage 4 §Split Rules + 00_f 協議 + UD §1.2.2。

**處理時機：** Wave-A1（quick-medium-win；5-9h；屬 Meta-pattern B chain；user 拍 priority HIGH）

**User workaround：** 量產期間 user 副對話手動補入 source coverage 段。

**Owner：** Claude Code workflow Stage 3 APPLY（Wave1 已落地；升格 D-065/D-066 背書）

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.12（含 user 完整 patch 提案 + Wave2 升格加註）
- DECISIONS_LOG §6.19.4 D-065 + §6.19.5 D-066（升格背書）
- NEW_REQ_33 + NEW_REQ_35 + NEW_REQ_37（F9 + F11 + F13 same Meta-pattern B chain）

---

## NEW_REQ_37 — `/create-character` 需主動讀既有台詞 + 聲線卡固定加「既有劇本台詞聲線基準」段（11th master 對話 B M4 follow-up F13；CRITICAL；output 層強化）

**狀態：** ✅ **RESOLVED via D-065/D-066（Wave2 落地，2026-06-02）** — UD §1.2.2 + 00_f §10.14 既有劇本既定關係/台詞聲線基準議題 append + registry core.00_f_character id 10（D-066）；output 層強化落地，與 NEW_REQ_35 F11 同輪 Wave2 完成。〔Wave2 升格揭露：F13 原判『不需 D-NNN』；因落地需動 LOCKED UD §1.2.2 + 00_f + registry，升格為必拍，對應 **D-065/D-066**；見 DECISIONS_LOG §6.19.4/§6.19.5〕

**時點：** 2026-05-30（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間實測「比設定 source 更高價值的下游資料」；user 拍 priority HIGH）

**需求背景：** /create-character SKILL.md line 18 明示「does not create ... dialogue」；line 322 D-050 邊界 08_dialogue_outputs/ 在「不寫」清單**但沒禁讀**；完全沒 speaker alias 機制（MainGirlA = 瑟琳 / MainGirlB = 莉娜 / MainGirlC = 諾拉）/ 既有劇本讀取規則 / docx 支援 / Stage 4 §Split Rules 沒「既有劇本台詞聲線基準」+「既有劇本聲線使用規則」section / 8-12 句篩選標準（初登場 / 危機反應 / 任務前 / 戰後 / 日常互動 / 被肯定吐槽 / 關係推進 / 中後期成長）。

**分類：** ⚠ design gap（cross-layer：input 機制 + output structure + alias matching + docx 支援 + 篩選標準）；**嚴重度：** 🔴 CRITICAL — user 親口判 priority HIGH；直接影響 /dialogue-write 文筆一致性

**提議方案：** SKILL.md 擴：
1. Stage 1 確認既有台詞 + speaker alias
2. Stage 2 讀 08_dialogue_outputs/ + docx + .txt + .csv + .json 不寫
3. 台詞篩選標準 8-12 句覆蓋 8 場景類型
4. Stage 4 加 § 既有劇本台詞聲線基準 + § 既有劇本聲線使用規則
5. cross-ref STYLE_ANCHOR W-style 機制（voice card 繼承 W-style 文風指紋 + 加 character-specific 聲線特徵）

**對既有 spec 的影響：** /create-character SKILL.md Stage 1/2/3/4 + 00_f 協議 + UD §1.2.2 + 可能 parse_frontmatter.py 加 docx 支援；D-050 邊界 clarification（讀 vs 寫）。

**處理時機：** Wave-A3（必須同輪實作 NEW_REQ_35 F11 input 層；input + output 一氣呵成）

**User workaround：** 量產期間用副對話讀既有劇本 + 手動補入聲線基準 + 使用規則段。

**Owner：** Claude Code workflow Stage 3 APPLY（同輪 NEW_REQ_35；Wave2 已落地；D-065/D-066 背書）

**Wave2 落地紀錄（WI-C；2026-06-02）：** F13 output 層強化由 **WI-C**（既有劇本台詞聲線基準 output work item）落地 — UD §1.2.2 append 既有劇本既定關係/事件承接議題 + 00_f §10.14 子節 + registry core.00_f_character id 10（D-066）。與 WI-B（NEW_REQ_35 F11 input 層）同輪 Wave2 一氣呵成。RESOLVED via D-065/D-066。

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.13（含 Wave2 升格加註）
- DECISIONS_LOG §6.19.4 D-065（UD/00_f append；含升格揭露）+ §6.19.5 D-066（registry append）
- NEW_REQ_35（F11 input 層；**同輪 Wave2 實作**）
- NEW_REQ_33 + NEW_REQ_36（F9 + F12 same Meta-pattern B chain）
- NEW_REQ_21（STYLE_ANCHOR W-style；voice card 繼承 W-style 文風指紋）
- D-055（STYLE_ANCHOR pre-generation 文風錨定機制）
- D-050（08_dialogue_outputs/ 邊界 clarification 讀 vs 寫）

---

## NEW_REQ_38 — AGENTS.md / CLAUDE.md 開場 context budget 過大（11th master 對話 B M4 follow-up F14）

**狀態：** ✅ **RESOLVED（F14 已於前批落地；Batch 4 狀態核對同步，2026-06-02）** — 瘦身已完成：CLAUDE.md → v0.5（完整 skill 清單 / Phase 狀態移出）+ AGENTS.md（205 → ~127 行）+ 新建 `_user_manual/skill_registry_full.md`；minimal-list 子題（台詞品質規則 + 禁止傾向）採選項 (c) 仍保留 root（兩段現存於 AGENTS.md）。〔本批僅核對標 RESOLVED；F14 實作非 Batch 4 所做，原 DEFERRED 為 stale 狀態漂移。〕

**時點：** 2026-05-30（11th master 對話 B M4 user-test follow-up）

**提出者：** user（/create-outline 對話內 context 飆 72% 撞天花板）

**需求背景：** AGENTS.md 205 行 / CLAUDE.md 137 行 / skill_invocation_guide.md 137 行；AGENTS.md 行 1-104 是核心 hard rules；行 105-205（~100 行）幾乎全是 skill 清單 + invocation 範本 + Phase A/B/C/D skill 表 + QA 模板狀態 + Codex CLI 範本 + Phase 階段對應 — 屬「按需讀取」內容。

**分類：** ⚠ design gap（root agent instructions context budget；屬 ARCH §3.3.0 multi-agent invocation 慣例維護擴充）；**嚴重度：** 🟠 MAJOR — 影響所有 Codex CLI/App skill 對話穩定性

**提議方案：** 瘦身 AGENTS.md (205 → ~150 行) + CLAUDE.md (137 → ~120 行)；移出 skill 清單 / Phase 狀態到 `_user_manual/skill_registry_full.md` 新建檔；同步更新 skill 表反映 STYLE_ANCHOR 後 scene-task v0.2 / dialogue-write v0.3；對話 A reframe 後 frontend dialogue handoff 機制反映。

**user 第 4 節 minimal list 需 user 拍板**：是否含「台詞品質規則」(AGENTS.md line 34-45) +「禁止傾向」(line 46-59)？三選一：(a) 移到 /dialogue-write + /qa SKILL.md / (b) 移到 _user_manual/ / (c) 仍保留在 root。

**對既有 spec 的影響：** AGENTS.md + CLAUDE.md + 新建 `_user_manual/skill_registry_full.md` + `_user_manual/skill_invocation_guide.md` 對齊；不涉 LOCKED spec。

**處理時機：** Wave-A1（**第一個處理**；5-7.5h；屬 Meta-pattern D；瘦身後其他 patch 對話 context budget 充裕）

**User workaround：** 無；累積 context 飆升。

**Owner：** Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.14（含 user 完整 patch 提案）
- NEW_REQ_34（F10 same Meta-pattern D — Agent context / UX layer）
- ARCH §3.3.0（D-048 落地段）
- NEW_REQ_22（11th master 對話 A reframe；本 patch 反映 reframe 後機制）

---

## NEW_REQ_39 — `parse_frontmatter.py` 把裸 `---` 誤判 YAML block 起點（11th master 對話 B M4 follow-up F15）

**狀態：** ✅ **RESOLVED（Batch 3 工具衛生，2026-06-02，feat/batch3-hygiene）** — `parse_frontmatter.py` `_find_header_adjacent_yaml` 未閉合 `---` 分支加 `_looks_like_frontmatter_yaml` 守衛：裸 Markdown HR（後接非 YAML 內文）回 None、不再把整檔剩餘誤判為未閉合 YAML block 報假 ERROR；真未閉合 frontmatter 仍偵測（不誤殺）。+ 回歸測試 `scripts/tests/test_parse_frontmatter_f15.py`（4 案例，含 WARN-case）。零-LOCKED、無 D-NNN。

**時點：** 2026-05-31（11th master 對話 B M4 user-test follow-up；Codex 自報）

**提出者：** Codex（量產期間 inline 報告自己撞到）

**需求背景：** `_user_manual/agents_md_context_budget_update_request.md` 第 7 行單獨 `---` 被 `build_repo_index('.')` 誤判 YAML block 起點但後文非合法 YAML；Codex 已 inline 移除該裸 `---`（user 端 instance workaround）；parser 端仍 fragile。

**Verify**：parse_frontmatter.py line 2873-2892 `_find_header_adjacent_yaml()` line 2880-2890 正常路徑「開 `---` + 閉 `---`」對找到 + `_looks_like_frontmatter_yaml` 過濾非 YAML → 安全返回 None；**line 2892 bug**：若只有開 `---` 沒閉 `---`（Markdown HR 邊界）→ parser 把整檔剩下內容當 unclosed YAML block → 下游 `_validate_frontmatter_yaml` 嘗試 YAML parse 失敗報 ERROR。

**分類：** 🐛 runtime bug（parser edge case；防呆強化）；**嚴重度：** 🟡 MINOR — 多數情況 work；user 量產 raw material / proposal doc 內常用 HR 會撞

**提議方案：** 補 line 2892 unclosed YAML edge case：套用 `_looks_like_frontmatter_yaml` 檢查 + return None if not；加 test fixture for unclosed `---`。

**對既有 spec 的影響：** `scripts/parse_frontmatter.py` line 2892 + `scripts/tests/`；不涉 LOCKED spec。

**處理時機：** Wave-A1（micro-fix；1.5-2h；最低風險）

**User workaround：** Codex 已 inline 移除該裸 `---`；屬 instance-level 不是 Template parser fix。

**Owner：** Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.15
- NEW_REQ_26（F2 same Meta-pattern C — CLI / lint / parser 工具層）
- `scripts/parse_frontmatter.py`

---

## NEW_REQ_40 — `/create-outline` → `/create-detailed-outline` 中間缺 DRAFT 原始細節保全層（11th master 對話 B M4 follow-up F16）

**狀態：** ✅ RESOLVED via D-069（Batch 2 大綱鏈 L0；保全層 convention，不建 00_m；05_f 必帶 5 欄 header；兩 skill 唯讀）

**時點：** 2026-05-31（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間 /create-outline 撞主線骨架簡潔 vs 細節保全 tension；user 已建 `05_plot/05_f_關卡原始細節備忘.md` workaround）

**需求背景：** /create-outline + /create-detailed-outline + UD 完全沒「原始細節 / 保全 / DRAFT preservation layer」concept；user 已 ad-hoc 用 `05_plot/05_f_關卡原始細節備忘.md` workaround（DRAFT / entities: [] / depends_on: [P] / 不更新 .protocol_version / 不建 CH-*/S-*）。

**分類：** ⚠ design gap（新 workflow concept；屬 /create-outline → /create-detailed-outline 間 layer 擴充）；**嚴重度：** 🟠 MAJOR — 通用對所有長篇作品

**提議方案：** 從 user `05_f` workaround 抽象成 spec：
- (a) 檔名 pattern `<目錄>/<\d+_x>_原始細節備忘.md`
- (b) frontmatter 規則（狀態 DRAFT / entities: [] / depends_on 指上游 / 不登錄 .protocol_version / 不建 CH-*/S-*）
- (c) /create-outline + /create-detailed-outline SKILL.md 提及「該 layer 為資料源」
- (d) 可能新建 `00_protocol/00_m_保全層協議.md`（待 user 拍板是否新 protocol）

**對既有 spec 的影響：** /create-outline + /create-detailed-outline SKILL.md + UD §1.3 + 可能新建 protocol；不涉 LOCKED spec 本體。

**處理時機：** Wave-A1（quick-medium-win；5-9h；屬 Meta-pattern E 通用層；user 已 workaround motivating evidence）

**User workaround：** 量產期間建 `05_plot/05_f_關卡原始細節備忘.md`。

**Owner：** Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.16
- NEW_REQ_41 + NEW_REQ_42 + NEW_REQ_43（F17 + F18 + F19 same Meta-pattern E）

---

## NEW_REQ_41 — `/create-outline` 寫作 UX 缺「遊戲設計語言」/「關卡功能 table」結構化輸出（11th master 對話 B M4 follow-up F17）

**狀態：** ✅ RESOLVED via D-067（Batch 2 大綱鏈 L0；pattern pack 唯讀 registry + outline_table 可選 mode；原候選 D-060 vacated 改 D-067）

**時點：** 2026-05-31（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產期間 /create-outline 撞「過度文學化分析」希望切遊戲設計語言）

**需求背景：** SKILL.md 完全沒「遊戲設計 / 關卡功能 / 玩家 X 取得 Y / 開戰前後鉤子」table 格式；沒「優先用遊戲設計語言整理」UX wording。user 推薦 table 格式：關卡 / 開戰前功能 / 戰鬥功能 / 戰鬥後功能 / 玩家新增資訊 / 後續鉤子 / 禁止提前。

**分類：** ⚠ design gap（UX wording + 結構化輸出格式缺；屬 genre-specific 可選 mode）；**嚴重度：** 🟡 MINOR-MAJOR — 遊戲類作品需要；非遊戲類不需

**提議方案：** **D-060 拍板候選**（pattern pack 機制；合 NEW_REQ_42 F18 一起）：
- (a) 依 00_b §1 作品類型載入
- (b) `tower_defense` pack 含遊戲設計 table 格式
- (c) `visual_novel` pack 預留
- (d) pack registry 規範（新建 `_design/registries/pattern_pack_registry.yaml`）

**對既有 spec 的影響：** /create-outline SKILL.md Stage 1/2 + 新建 pattern_pack_registry.yaml + skill_invocation_guide.md；不涉 LOCKED spec。

**處理時機：** Wave-A3（D-060 拍板後；合 NEW_REQ_42 同 pattern pack 同輪做）

**User workaround：** 量產期間 user 端主動引導 agent 用遊戲設計語言；ad-hoc。

**Owner：** user 拍板 D-060 → Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.17
- NEW_REQ_42（F18 same pattern pack；**必同 D-060 拍板 + 同輪實作**）
- NEW_REQ_40 + NEW_REQ_43（F16 + F19 same Meta-pattern E）

---

## NEW_REQ_42 — `/create-detailed-outline` 缺「開戰前→戰鬥→戰鬥後」場景結構支援（11th master 對話 B M4 follow-up F18）

**狀態：** ✅ RESOLVED via D-067（Batch 2 大綱鏈 L0；pattern pack scene_types enum + 戰鬥前後場 + 06_a 行內 note；戰鬥場 auto_dialogue:false 下游 /scene-task 對接列後續批；原候選 D-060 vacated 改 D-067）

**時點：** 2026-05-31（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產《蟲潮孤堡》塔防遊戲；每關只有兩個劇情場開戰前 + 戰鬥後；戰鬥是玩法段非劇情台詞）

**需求背景：** SKILL.md 沒「劇情場 vs 戰鬥場」場景類型 enum；沒「開戰前 / 戰鬥後」格式支援；場景結構假設通用單一場景；可能誤建戰鬥本身為 S-*（含完整 dialogue）。

**分類：** ⚠ design gap（genre-specific 結構支援缺）；**嚴重度：** 🟡 MINOR-MAJOR — 戰鬥型作品需要；視覺小說不需

**提議方案：** 合 NEW_REQ_41 同 **D-060** pattern pack 機制：
- (a) 場景類型 enum 加 `劇情場` / `戰鬥前場` / `戰鬥場` / `戰鬥後場` / `UI/語音場`
- (b) `tower_defense` pattern pack 含「每關 = 戰鬥前場 + 戰鬥場(skip dialogue) + 戰鬥後場」
- (c) `arpg` pack 預留
- (d) 戰鬥場不自動進 /dialogue-write

**對既有 spec 的影響：** /create-detailed-outline SKILL.md + UD §1.4 + 連動 pattern_pack_registry.yaml；不涉 LOCKED spec。

**處理時機：** Wave-A3（D-060 拍板後；合 NEW_REQ_41 同輪做）

**User workaround：** 量產期間 user 端手動標記場景類型。

**Owner：** user 拍板 D-060 → Claude Code workflow Stage 3 APPLY（合 NEW_REQ_41）

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.18
- NEW_REQ_41（F17 same pattern pack；**必同 D-060 拍板 + 同輪實作**）
- NEW_REQ_40 + NEW_REQ_43（F16 + F19 same Meta-pattern E）

---

## NEW_REQ_43 — `/create-outline` / `/create-detailed-outline` 缺「個人劇情 vs 主線邊界」check（11th master 對話 B M4 follow-up F19）

**狀態：** ✅ RESOLVED via D-068（Batch 2 大綱鏈 L0；UD agent 主導 check；原候選 D-061 vacated 改 D-068）

**時點：** 2026-05-31（11th master 對話 B M4 user-test follow-up）

**提出者：** user（量產《蟲潮孤堡》塔防遊戲；含主線 + 多女角群像 + 12 段個人線結構）

**需求背景：** SKILL.md 沒「個人線消耗保護」/「個人線高潮邊界」/「12 段個人線結構」check。user 案例：主線 Lv10-Lv26 可使用女角功能但不應消耗女角後續個人劇情高潮；女角 12 段角色劇情（1-3 出場/介紹/第一次成人 + 後續 9 段獨立）；主線支線可塑造世界觀人物設定但不能自動把女角個人線寫完。

**分類：** ⚠ design gap（內容邊界規則缺；通用 footgun）；**嚴重度：** 🟠 MAJOR — 任何群像作品撞

**提議方案：** **D-061 拍板候選**：
- (a) UD §1.3.X 加新議題「主線可使用角色功能但不消耗個人線高潮」
- (b) /create-outline Stage 3 預告稿加 check：每章節列出「使用了哪些角色 / 是否消耗個人線」
- (c) /create-detailed-outline 同 check
- (d) 12 段個人線結構紀錄 convention（含成人段降權邊界）

**對既有 spec 的影響：** /create-outline + /create-detailed-outline SKILL.md + UD §1.3；不涉 LOCKED spec。

**處理時機：** Wave-A3（D-061 拍板後）

**User workaround：** 量產期間 user 端 ad-hoc 邊界檢查；無正式 patch。

**Owner：** user 拍板 D-061 → Claude Code workflow Stage 3 APPLY

**Cross-ref：**
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.19
- NEW_REQ_40 + NEW_REQ_41 + NEW_REQ_42（F16 + F17 + F18 same Meta-pattern E）

---

## NEW_REQ_44 — dashboard `/api/dashboard/pending-status` backend endpoint + 3 schema（OPEN — BLOCKED on D-062 拍板；11th master frontend cycle 從 NEW_REQ_20 F1-3b 拆出）

**狀態：** 🔴 **OPEN — BLOCKED on D-062 拍板**（3 data schema 為 backend 前置；拍板前 backend 不實作）

**時點：** 2026-06-01（11th master frontend dialogue cycle；F-A3 audit 揭示）

**來源：** NEW_REQ_20 F1-3b 拆出 — frontend cycle 已落地 F1-3a（renderTriColumn 對齊 UX_SPEC §11.1.6 + 移除過時 mock + 誠實標 backend pending），但「接真實 pending 資料」需 backend endpoint，超出 frontend scope。

**需求背景：** `_tools/frontend/server.py`（984 行）10 個現有 endpoint 中不存在 `/api/dashboard/pending-status`。UX_SPEC §11.1.6 三欄區（左：待人類裁決 HD / 中：QA pending / 右：Canon Δ pending）的資料來源都缺機器可讀 schema：(1) 09_e 無「待裁決 vs 已裁決」標記；(2) Canon Δ 候選無儲存位置 / schema / lifecycle；(3) 無「QA 完成」定義 +「缺哪些 QA type」反查邏輯（`qa_report_count()` 只計檔案數）。

**分類：** ⚠ design gate（新資料契約；觸 09_quality_assurance 模板 + 協議層，可能含 LOCKED spec）；**嚴重度：** 🟠 MAJOR（NEW_REQ_20 三欄完整化的唯一阻塞）

**提議方案：** **D-062 拍板必開**（詳 `_design/D062_DECISION_PACKAGE.md`）— 3 schema 各 3 選項：Schema 1（09_e `decision_status` enum 欄，推薦 1A）/ Schema 2（新建 `09_j_canon_delta候選表.md`，推薦 2A，需 D-062 一併授權新建）/ Schema 3（8 必跑=完成 + 反查缺漏集合，推薦 3A，對齊 D-043）。

**對既有 spec 的影響：** 09_e 模板加欄 + 新建 09_j（皆需 D-062 授權）+ QA 完成定義文件化（可能觸 DATA_FORMAT_SPEC / INTEGRATION_CONTRACTS）+ server.py 加 route + state.js/api.js/ProjectDashboard.js 加 `pendingStatus` state 欄（後兩者屬 frontend scope，schema 定後直接做）。

**處理時機：** D-062 拍板後 → schema 落地 → backend 實作 → frontend 接線 → NEW_REQ_20 完全 RESOLVED。

**Owner：** user 拍板 D-062 →（schema 落地：對話 A 或下一 cycle）→ frontend dialogue 後續 cycle Stage 3 APPLY。

**Cross-ref：**
- `_design/D062_DECISION_PACKAGE.md` v0.1（本 entry 的前置拍板包；3 schema 完整選項 + 推薦 + 影響範圍）
- NEW_REQ_20（F1-3b 拆出來源；現標「前端部分 RESOLVED」）
- `_design/AUDIT_2026Q2_REPORT.md` §9.3（finding 拆分）+ §9.5（backend 越界防護）
- `_sandbox/audit-reports/audit-F-A3-backend-state.md`（3 schema 缺口 file:line 證據）
- `_design/UX_SPEC.md` §11.1.6（三欄區規格目標）

---

## NEW_REQ_45 — frontend scope-C reframe 評估（DEFERRED — 待 user 外接寫作實操反饋）

**狀態：** 🟡 **DEFERRED**（tracking；待 user evidence）

**時點：** 2026-06-01（11th master frontend cycle Stage 1 audit F-C1）

**提出者：** 11th master frontend dialogue（frontend cycle F-C1 reframe audit）

**需求背景：**

工具角色 reframe（NEW_REQ_22）後，frontend Phase A.0F feature（UX_SPEC §11 實為 5 核心 + 4 輔助 = 9 段，非 handoff 口語「11 feature」）的存廢評估。F-C1 audit（read-only）列出多條「spec 設計 vs 新角色 use case 落差」（F1 Dashboard QA 視角 / F2 Scene Detail「外接寫作接回後 QA 入口」/ F3 Scene Editor 多版本並排可能失去主要 use case / F7 LOCKED 守門 multi-tool coordination 等）。

但 F-C1 自承這些 finding 屬「假設外接寫作大幅改變 use case」的**推測性判斷**，需 user 實際跑通外接寫作 workflow 反饋才能準確評估 scope C 大小。

**提議方案（對齊 FRONTEND_HANDOFF §4）：**
- **本 cycle 不 apply**（路徑 M = audit C 不 refactor）。
- user 用幾週 + 跑通外接寫作 1-2 場戲完整閉環（外部工具產台詞 → 接回跑 QA → 09_e 人類拍板）。
- evidence 累積後 → 後續 frontend cycle / master 對話評估 scope C 大小（可能小 patch / 可能 UX_SPEC v0.4 → v0.5 新角色適配版）。
- ⚠ **不採** F-C1 報告末段「開 NEW_REQ_25-43 / β 路線」碎片化建議（過度建構；本 entry 單一 tracking 即可）。

**處理時機：** 待 user 外接寫作實操反饋（estimated 數週後）。

**Cross-ref：** NEW_REQ_22（reframe parent）+ `_design/FRONTEND_HANDOFF.md` §2.3 + §4 + `_design/AUDIT_2026Q2_REPORT.md` §9 + `_sandbox/audit-reports/audit-F-C1-reframe.md`

---

## NEW_REQ_46 — root `entity_type_registry.yaml` 損壞無法 parse（Batch 4 F8 設計時發現）

**狀態：** ✅ **RESOLVED via D-073（Batch 4 落地，2026-06-02）** — 刪 line 94-98 重複孤兒尾段、保留單一 `user_extensions: []`（最小 truncate，不 overwrite template）；root core 與 template core deep-equal。

**時點：** 2026-06-02（11th master frontend Batch 4 接手 F8 設計、讀 registry 時發現）

**提出者：** Claude Code（Batch 4 L0；F8 ORG-* 設計 precursor 檢查）

**需求背景：** root `entity_type_registry.yaml`（instance registry，LOCKED-tier parse 權威）在 line 94 拋 `yaml.parser.ParserError`：line 93 `user_extensions: []` 之後殘留重複孤兒尾段（line 94-98：`description:` / `- prefix: SKILL` / `description:` / 第二個 `user_extensions: []`），整檔無法 `yaml.safe_load`。`_design/registries/entity_type_registry.template.yaml`（同 LOCKED-tier，乾淨）為對照基準。屬 live latent bug — 任何載入此 registry 的 skill（/status、/create-*、/check-gaps）潛在受影響；損壞使 instance-side `user_extensions` 在 parse 失敗時靜默丟失、退回 template-only core。

**分類：** ⚠ 機械損壞（registry parse 失敗）；**嚴重度：** 🟠 MAJOR — registry 是 entity 型別 parse 權威，無法 parse 影響全 tooling

**提議方案：** 刪 line 94-98 孤兒尾段、保留單一結尾 `user_extensions: []`（最小 truncate，**不** overwrite-from-template 以保留 root 既有內容）。

> **評審更正：** F8 judge panel 冠軍/保守提案原稿曾誤診「root 缺 W-style / 只 9 型別」；實測為**誤**——root 與 template **皆**含 10 個 core 型別（含 W-style）。損壞純是尾段重複。rationale = 「純刪重複尾段」。

**對既有 spec 的影響：** 1 檔 `entity_type_registry.yaml`（root instance）；0 新型別、0 設計改動（ORG-* 屬 D-071 Phase 1，另案）；template 不動。

**處理時機：** Batch 4 — F10 落地後即修（F8 ORG-* core / D-071 Phase 1 的 Phase 0 precursor）。

**Owner：** Claude Code workflow Stage 3 APPLY（Batch 4；feat/batch4-entity）+ user 拍板獨立 D-073。

**Batch 4 落地紀錄（2026-06-02）：** L0 已 truncate + 實測 `yaml.safe_load` 通過、10 core types + 3 reserved + `user_extensions: []` 與 template `core` deep-equal。LOCKED-tier 走四層防線（無 §3.1 豁免）。RESOLVED via D-073。

**Cross-ref：**
- DECISIONS_LOG §6.22 D-073（RESOLVED 背書）
- `D071_DECISION_PACKAGE.md` §4（registry 修復併入說明）
- NEW_REQ_32（F8 ORG-* core；本修復為其 Phase 0 precursor）
- `entity_type_registry.yaml` + `_design/registries/entity_type_registry.template.yaml`

---

## NEW_REQ_47 — `parse_frontmatter.py` entity-type 硬編碼鏡像應改 registry-derived（Batch 4 F8 panel 發現）

**狀態：** ✅ **RESOLVED via D-075 / Batch 5（2026-06-03，過夜自主長跑 feat/f8p3-audit-batch5，consolidate 入 NEW_REQ_49，park 等 L3）** — W-style 兩處 drift 先於 D-071 drive-by 補；**registry-derived 重構本批根治**：`ENTITY_ID_RE` / `_entity_type_from_id` / `OUTLINE_ENTITY_TYPES` 改從 `load_entity_type_registry()` 動態建構、移除硬編碼鏡像，配套 regression（pytest 43 pass，既有型別驗證行為不變）。詳 DECISIONS_LOG §6.26 D-075 / NEW_REQ_49。〔原狀態：🟡 DEFERRED（部分解）〕

**時點：** 2026-06-02（11th master frontend Batch 4；F8 judge panel + L1 審查發現）

**提出者：** Claude Code（F8 設計 panel；first-principles / dual 提案 graft）

**需求背景：** `scripts/parse_frontmatter.py` 內有兩處 entity-type 的硬編碼平行鏡像，與 `entity_type_registry.yaml` 的權威清單會 drift：
- `ENTITY_ID_RE`（line ~108）：手列各型別 alt。〔**D-071 已 drive-by 修復**：補入 `W-style`（原 D-055 漏同步）+ `ORG`。〕
- `_entity_type_from_id`（line ~1635）：另一處 id→type 的硬編碼對應。〔**D-071 已 drive-by 修復**：補入 `W-style`（原誤回 "W"）；ORG 走既有 fallback 正確回 "ORG"。〕
兩者**仍為硬編碼**（drive-by 僅補當前缺口）；理想應從 registry 動態衍生（single source of truth），避免每加一型別就要改多處、且免再 drift —— **此為本 NEW_REQ 剩餘範圍**。另：spec-doc 端同型列舉 drift（DF §7.6/§7.1/§7.2 + SPEC §5.1b + manual §6）見 NEW_REQ_48。

**分類：** ⚠ tech-debt（parser 維護性；registry 為權威但有硬編碼鏡像）；**嚴重度：** 🟡 MINOR-MAJOR — 不阻 runtime，但每次加型別都是 drift 風險源

**提議方案：** 把 `ENTITY_ID_RE` / `_entity_type_from_id` 改為從 `load_entity_type_registry()` 動態建構；移除硬編碼型別清單。需配套測試確保現有行為不變。

**對既有 spec 的影響：** `scripts/parse_frontmatter.py`（純工具；非 LOCKED spec）；不動 registry / 不動 entity 語意。

**處理時機：** F8 Phase 1（D-071）已 drive-by 補 W-style + ORG 當前缺口；**registry-derived 重構**留後續批。

**Owner：** 未指派（future batch）。

**Cross-ref：**
- `D071_DECISION_PACKAGE.md` §3b + §7 風險 6（tech-debt follow-up note）
- DECISIONS_LOG §6.22（D-073 registry 修復；同檔 parser 相關）
- `scripts/parse_frontmatter.py` line ~108（ENTITY_ID_RE）+ line ~1635（_entity_type_from_id）

---

## NEW_REQ_48 — LOCKED spec / manual 的 core entity 型別列舉 drift（W-style + ORG 缺）（Batch 4 F8 Phase 1 QA 發現）

**狀態：** ✅ **RESOLVED via D-075 / Batch 5（2026-06-03，過夜自主長跑，consolidate 入 NEW_REQ_49，park 等 L3）** — 採 D-075「保留鏡像 + drift-lint」雙軌（§提議方案選項 2 的精神 + 選項 1 的列舉保留）：DATA_FORMAT_SPEC v0.5 §7.1/§7.2/§7.6 + SPEC v1.3 §5.1b + manual（工具完整統整報告書 §6 + 06_data_structure §1）補 W-style + ORG 至 11 + 標「（鏡像；權威見 entity_type_registry）」；新 `check_entity_type_consistency.py` 守護。SPEC §5.1b 為 LOCKED → 等 L3 簽字。詳 DECISIONS_LOG §6.26 D-075 / NEW_REQ_49。〔原狀態：🟡 DEFERRED〕

**時點：** 2026-06-02（11th master frontend Batch 4；F8 Phase 1 D-071 adversarial QA 發現）

**提出者：** Claude Code（D-071 QA workflow `wf_9ef532f0`）

**需求背景：** entity_type_registry 為 core 型別**運作權威**，但數處 LOCKED spec / user manual 仍以**靜態文字列舉** core 型別清單，未隨 core 新增同步，已 drift：
- `_design/DATA_FORMAT_SPEC.md` §7.6（規範性 per-type 表，列 9）+ §7.1 line ~1512 + §7.2 sample core block（mirror，stale）— 缺 **W-style + ORG**。
- `_design/SPEC.md` §5.1b line ~255（「既有 7 種…+ A-*」= 8）— 缺 **W-style + ORG**。
- `_user_manual/工具完整統整報告書.md` §6（user-facing core 型別表）— 缺 **ORG**（W-style 曾補）。
- registry 現有 **11** core（W-rules/W-language/W-style/V/C/R/P/CH/S/A/ORG）。

**根因 + 先例：** drift 非 D-071 新生 —— **D-055 加 W-style core 時即已造成**，且當時拍板「0 LOCKED spec supersede / SPEC/DF 全不動」。D-071（ORG）沿用同先例、**compound** 此 drift。註：§7.8 曾為 A-* 記「9th core 類型」（A-* 有同步、W-style/ORG 無），故專案慣例本身不一致。

**分類：** ⚠ doc-sync（LOCKED canonical schema 文字 vs 運作 registry 不一致）；**嚴重度：** 🟡 MINOR — 非功能（parser/registry 為權威且正確）、precedent-blessed；但屬 LOCKED 優先級:最高 spec 之事實矛盾，不應靜默累積

**提議方案：** 二選一（user 拍板）——
1. **doc-sync（推薦）**：補 W-style + ORG 為 §7.6 表新列 + §7.8 partial-supersede 註 + SPEC §5.1b line 255 + manual §6，比照 A-* 之「9th core 類型」紀錄；doc-only，無 schema_version bump。
2. **registry-derived 化**：把 spec 端列舉改為「以 registry 為準」指標、移除靜態清單（與 NEW_REQ_47 parser 端同精神 = single source of truth）。

**對既有 spec 的影響：** DATA_FORMAT_SPEC §7.6/§7.1/§7.2 + SPEC §5.1b（皆 LOCKED）+ manual §6；走四層防線。**不**綁進 D-071（避免 F8 擴入 SPEC.md/DF LOCKED 區；沿 D-055 precedent 解耦）。

**處理時機：** F8 Phase 2/3 或獨立 doc-sync 批。

**Owner：** 未指派（future batch）。

**Cross-ref：**
- DECISIONS_LOG §6.23.2 D-071（spec 無需改 rationale 修正後指向本條）
- D-055（W-style core；drift 起源 + 「0 LOCKED supersede」先例）
- NEW_REQ_47（parser 端同型硬編碼鏡像 drift；姊妹條）
- `_design/DATA_FORMAT_SPEC.md` §7.6/§7.1/§7.2 + `_design/SPEC.md` §5.1b + `_user_manual/工具完整統整報告書.md` §6

---

## NEW_REQ_49 — entity 型別清單單一真相源化 / registry DRY 重構（Batch 5；consolidate NEW_REQ_47 + 48 + 稽核 drift）

**狀態：** 🟢 PROCESSING（Batch 5；過夜自主長跑 feat/f8p3-audit-batch5 開 entry + 拍 D-075 + 跑 workflow；2026-06-03）— consolidate NEW_REQ_47（parser 硬編碼鏡像）+ NEW_REQ_48（spec-doc 列舉 drift）+ BATCH4_POSTLAND_AUDIT_REPORT 之 D1/D2 drift + i1/i3/i4 + M3（scanner 漏掃 10_art_assets/11_organizations）為單一 entry。

**時點：** 2026-06-03（F8 Phase 3 land + Step 2 全 repo 稽核跑完後，§1 前置滿足）

**提出者：** 過夜自主長跑（依 BATCH5_REGISTRY_DRY_REFACTOR.md + BATCH4_POSTLAND_AUDIT_REPORT.md drift findings）

**需求背景（根因）：** entity 型別清單目前**硬編碼在多處、會 drift**（Batch 4 + F8 Phase 3 已實證）：
- **parser**（NEW_REQ_47）：`scripts/parse_frontmatter.py` `ENTITY_ID_RE`(~line 109) + `_entity_type_from_id`(~line 1635) + `OUTLINE_ENTITY_TYPES`(~line 104) 為 registry 硬編碼鏡像。
- **spec-doc**（NEW_REQ_48 / 稽核 i1）：`DATA_FORMAT_SPEC §7.6/§7.1/§7.2` + `SPEC §5.1b` + `_user_manual/工具完整統整報告書.md §6` 靜態列舉「7 種 / 8 種」core，缺 W-style + ORG（registry 實 11）。
- **scan-scope**（稽核 M3）：`check_paths.py ACTIVE_DIRS/ACTIVE_PREFIXES/PATH_RE` + `check_headers.py TEMPLATE_PATTERNS` 寫死目錄清單；F8 Phase 3 已 drive-by 補 `11_organizations`（最小 hardcode），但 `10_art_assets` 仍漏、且未根治（應 registry target_dir 衍生）。
- **/status**（稽核線）：`.claude/skills/status/SKILL.md` 型別列舉 + weight 寫死。
- 每加一型別需改 N 處、漏改靜默 drift。

**分類：** ⚠ tech-debt（DRY / drift 風險源）；**嚴重度：** 🟠 MAJOR（治理層；非 runtime 阻擋，但每次加型別都是 drift 源）

**重構目標（高槓桿子集 4 塊 + lint capstone；BATCH5 §2）：**
1. **parser registry-derived**：`ENTITY_ID_RE` / `_entity_type_from_id` 從 `load_entity_type_registry()` 動態建構；移除硬編碼鏡像 + 配套 regression（既有所有型別驗證行為不可變）。
2. **spec-doc 去 drift（D-075 採「保留鏡像 + drift-lint」雙軌）**：補 W-style + ORG，列舉處標「（鏡像；權威見 entity_type_registry）」；不移除列舉（契約規格需 inline 可讀性）。
3. **scan-scope registry-derived**：`ACTIVE_DIRS` / `TEMPLATE_PATTERNS` 從 registry 各型別 `target_dir` 衍生（含 `10_art_assets` + `11_organizations`，根治 M3）。
4. **/status registry-derived**：型別清單 + weight 改讀 registry。
5. **drift-lint（capstone）**：新增 `scripts/check_entity_type_consistency.py` 斷言「所有仍存在的列舉鏡像 == registry」；把「漏改」從可能變結構上不可能。

**刻意不做（殘餘）：** 每個 SKILL 內文全 registry-generic（回報遞減）→ NEW_REQ_49 尾巴 / 續記。

**對既有 spec 的影響：** `scripts/parse_frontmatter.py` + `check_paths.py` + `check_headers.py`（工具）+ `DATA_FORMAT_SPEC` / `SPEC §5.1b`（LOCKED，doc-sync 加鏡像 marker）+ `/status` SKILL + 新 lint script。Tier-4 → 四層防線 + D-075 + L3。

**處理時機：** Batch 5（本批；過夜自主長跑跑 workflow L0+L1+L2，park 在 feat/f8p3-audit-batch5 等 L3）。

**Owner：** 過夜自主長跑 + user L3 簽字。

**Cross-ref：**
- DECISIONS_LOG §6.26 D-075（拍板背書）
- `BATCH5_REGISTRY_DRY_REFACTOR.md`（§2 worklist + §4 workflow）/ `BATCH4_POSTLAND_AUDIT_REPORT.md`（drift findings 來源）
- NEW_REQ_47（parser 鏡像）+ NEW_REQ_48（spec-doc drift）（皆 consolidate 入本條）
- `scripts/parse_frontmatter.py` ~line 104/109/1635 / `check_paths.py` / `check_headers.py` / `entity_type_registry.yaml`

---

## NEW_REQ_N（待補）

（時點：YYYY-MM-DD；提出者：user / CODEX / Phase X 實作發現）

（需求描述）

（提議方案）

（處理時機）

---

# 3. 累積觸發 master 第五輪整合條件

當以下任一成立，觸發 master 第五輪整合對話：

1. **累積 ≥ 3 個 NEW_REQ 涉及主 SPEC / ARCH / TASKS / INTEGRATION_CONTRACTS 修訂**
2. **單一 NEW_REQ 是 critical 程度**（影響 Phase A.0+ 實作邊界）
3. **user 主動要求做下一輪整合**
4. **Phase A.0 / A.0F / B / C / D 任一階段完成後做收尾整合**

第五輪整合對話的工作：
- 把 POST_LOCK_PENDING 中累積的 NEW_REQ 處理掉
- 升 INTEGRATION_CONTRACTS v2.1+ 
- 升主 SPEC / ARCH / TASKS partial supersede（v1.2+ / v1.3+ / v1.4+）
- DECISIONS_LOG 升 v1.1+ + 加新 D-047+ 拍板
- 可選跑 CODEX (e) 短審查

---

# 4. 文件維護紀律

- 本檔可持續追加 — 不需要 LOCKED
- 每個 NEW_REQ 5 欄位必填（狀態 / 需求背景 / 提議方案 / 影響 / 處理時機）
- 進入 master 第五輪後解決的 NEW_REQ 標 RESOLVED 並紀錄對應 D-NNN
- 本檔不影響 LOCKED 設計層的權威性

---

# 5. 10th master 第十輪整合對話階段 6 評估紀錄總表（v0.19 partial supersede）

**評估日期：** 2026-05-23（10th master 第十輪整合對話 Milestone 4 真正封版宣告後）
**評估 owner：** 10th master 對話 + user 拍板「跑階段 6 只作評估不寫 NEW_REQ_16 spec」
**評估對象：** NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_14 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18
**不評估：** NEW_REQ_1~8 / 10 / 12 / 13 / 19（已 RESOLVED 或 PROCESSED）

**Wave 12 落地後新事實基準：**
- ✅ Phase D Wave 12 6 SKILL.md + 5 中文 wrapper 落地（commit fa21b65；10th master 階段 3）
- ✅ Wave 12 含 `/iterate-scene --split-to-file` D-054 NEW_REQ_15 落地
- ✅ Phase A.0F audit cycle Round 4 GO close-out（commit 2ed48f3）
- ✅ Milestone 4 真正封版宣告（PHASE_D_COMPLETION_REPORT v1.1 §10）
- baseline 維持 check_paths 247 ERROR / check_headers 0 ERROR / build_repo_index 0 ERROR

## 5.1 NEW_REQ_9 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — check_paths Windows vs sandbox baseline 差異 + 27 模板 old-style filename reference 未改名 |
| 10th master 評估 | **維持 hard-limit accept**（不本輪動）— sandbox cache 差異屬環境議題，scripts/check_paths.py 行為對齊改寫屬未來 Phase A.X 範圍；27 模板 old-style filename rename 屬 LOCKED 模板需開 D-055+ 拍板，風險高 ROI 低 |
| 推薦處理時機 | **等 NEW_REQ_16 lint script 落地後**（11+ 輪 master scope）一次性自動偵測 + 修補 |
| trigger 條件 | 無；屬技術債類 backlog |
| Owner | 11+ 輪 master 對話（NEW_REQ_16 lint script 實作後）|
| 本輪 action | 無（維持 v0.18 狀態）|

## 5.2 NEW_REQ_11 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — 翻譯工具分支（工具 B `game-dialogue-translator` fork） |
| 10th master 評估 | **本輪明確不動**；屬 11+ 輪 master scope；Milestone 4 真正封版已達成（前置條件 1/5 ✓）但其他 4 個前置條件未達成（L3_EXPORT_PROMPT_SCHEMA v1.0 穩定 / 至少 1 完整作品 corpus / user 明確需求 / 工具 A 維護期穩定 6 個月）|
| 推薦處理時機 | **M4 + 6 個月 + user 明確翻譯需求達成後** |
| trigger 條件 | 4 個前置條件全達成 + user 主動拍板啟動工具 B 開發 |
| Owner | 12+ 輪 master 對話（屆時新建 `game-dialogue-translator` repo + 完整提案見 `_design/PROPOSAL_TRANSLATION_TOOL_FORK.md` v0.1）|
| 本輪 action | 無（維持 v0.18 狀態 + reference PHASE_D_COMPLETION_REPORT v1.1 §10.4 後續路徑）|

## 5.3 NEW_REQ_14 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — PHASE_X_COMPLETION_REPORT §6 補入 AI-assisted 機制 |
| 10th master 評估 | **機制已就緒；等 user 跑 M4 chain 後啟動**；本輪 PHASE_D_COMPLETION_REPORT v1.1 §6 placeholder 保留屬封版後 user-test 範圍；NEW_REQ_14 機制屬封版後第一個 user 親跑 task 的 follow-up |
| 推薦處理時機 | **user 完成 M4 chain user-test 後** — agent reconstruct §6 草稿 → user 拍板「採」/「改」/「棄」→ patch PHASE_D §6 placeholder |
| trigger 條件 | user 親跑 M4 chain + user 明示「我跑完了；請補入 §6」 |
| Owner | 11th master 對話 或 user 用既有 master 對話內 inline patch |
| 本輪 action | 無（機制描述已寫於 v0.18 NEW_REQ_14 entry）|

## 5.4 NEW_REQ_15 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — D-054 hybrid 迭代評估 monitor trigger A/B/C/D |
| 10th master 評估 | **monitor 中；本輪不開 D-055**；Wave 12 落地後 `/iterate-scene --split-to-file` runtime 已可用，trigger B 開始可被觸發；尚未有實際 split 紀錄 |
| 推薦處理時機 | trigger A/B/C/D 任一達成後 |
| trigger 條件 | (A) user 寫 ≥ 30 場後回報「聚合 06_a 太大」/ (B) `/iterate-scene --split-to-file` 連續 ≥ 5 次拆檔 / (C) 工具 B 翻譯 / 多 agent 並行需求出現 / (D) 聚合 06_a 持續 git merge friction |
| Owner | 11+ 輪 master 對話（依 trigger 達成情況評估 D-055 拍板需求）|
| 本輪 action | 無；保留 monitor 狀態 |

## 5.5 NEW_REQ_16 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — 自動化 QA Layer 1 Cross-ref Consistency Lint Script |
| 10th master 評估 | **建議起手；spec 規劃推 11+ 輪實作**（依 user 拍板「跑階段 6 只作評估不寫 NEW_REQ_16 spec」）；ROI 高（9th master Round 1-4 cascade 4 輪 + Wave 12 commit 內 typo 修補都可被此 lint 自動抓出）；屬封版後維護期最先實作項 |
| 推薦處理時機 | **11+ 輪 master 對話起手**（建議第 11 輪先跑 spec 規劃 + design review；第 11/12 輪實作 200-400 行 Python）|
| trigger 條件 | 11+ 輪 master 對話 user 拍板啟動 |
| Owner | 11+ 輪 master 對話 |
| 本輪 action | 無（不寫 spec 規劃）；但本評估紀錄屬「11+ 輪 master 接手起點」reference |
| 預估規模 | 200-400 行 Python；6-8h 實作 + 2-4h testing |
| ROI 估算 | 自動抓 ~80% master 期間 MINOR finding → 後續每輪 master 省 30-60 分鐘 cleanup 時間 |

## 5.6 NEW_REQ_17 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — 自動化 QA Layer 2 Auto-patcher for Safe Simple Patches |
| 10th master 評估 | **本輪不動**；依賴 NEW_REQ_16 先實作；屬 11+ 輪 master scope |
| 推薦處理時機 | **NEW_REQ_16 落地 + Milestone 4 封版後 1-3 個月使用觀察期完成後** — framework 穩定 + Phase C/D 量產台詞累積 cross-ref drift 後 |
| trigger 條件 | NEW_REQ_16 落地 + user 主動拍板需要 auto-patch |
| Owner | 12+ 輪 master 對話或封版後維護期 master |
| 本輪 action | 無 |

## 5.7 NEW_REQ_18 10th master 評估紀錄

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟡 DEFERRED — 自動化 QA Layer 3 Nightly AI-driven Semantic Review |
| 10th master 評估 | **本輪不動**；依賴 NEW_REQ_16/17 先實作 + 評估封版後是否還有語意 drift；屬 11+ 輪 master scope；翻譯工具 fork（NEW_REQ_11）若啟動則 ROI 翻倍 |
| 推薦處理時機 | **Milestone 4 封版後 6+ 個月**；觀察封版後是否還有大量語意 drift → 是則實作；框架穩定則跳過 |
| trigger 條件 | NEW_REQ_16/17 落地 + 持續 6 個月語意 drift 觀察 |
| Owner | 13+ 輪 master 對話或封版後維護期 |
| 本輪 action | 無 |

## 5.8 NEW_REQ_19 10th master 紀錄確認（不重評）

| 項目 | 內容 |
|---|---|
| v0.18 狀態 | 🟢 PROCESSED via 9th master cleanup queue（Path A hard-limit accept）|
| 10th master 評估 | **維持 PROCESSED 狀態；不重評**；9th master 第一段已完整處理 R8-INFO-06 + R10-MI-01/02/03 + R10-MA-01 ack + AGENTS.md / CLAUDE.md Phase C skill table + 08_a §11.1 P-009 修正 |
| 本輪 action | 確認 NEW_REQ_19 已 RESOLVED；本輪不變動 |

## 5.9 階段 6 評估總結

| 分類 | NEW_REQ | 10th master 結論 |
|---|---|---|
| **本輪不動 + 11+ 輪起手** | NEW_REQ_16 | 建議起手；spec 規劃 + 200-400 行 Python 實作推 11+ 輪 |
| **本輪不動 + 依賴鏈延後** | NEW_REQ_9 | 等 NEW_REQ_16 落地後自動處理 |
| | NEW_REQ_17 | 依賴 NEW_REQ_16 + 封版後 1-3 個月 |
| | NEW_REQ_18 | 依賴 NEW_REQ_16/17 + 封版後 6+ 個月 |
| **本輪不動 + monitor** | NEW_REQ_15 | trigger A/B/C/D 達成則開 D-055 |
| **本輪不動 + 屬封版後 user-test follow-up** | NEW_REQ_14 | user 跑完 M4 chain 後啟動 AI-assisted §6 補入 |
| **本輪不動 + 大 future fork** | NEW_REQ_11 | M4 + 6 個月 + 4 個前置條件達成 + user 拍板 → 啟動工具 B `game-dialogue-translator` |
| **本輪不動 + 已 PROCESSED** | NEW_REQ_19 | 9th master cleanup queue 完成；維持 PROCESSED |

**10th master 階段 6 評估完成；7 個 deferred NEW_REQ 全有明確結論 + 推薦處理時機 + trigger 條件；屬 11th master HANDOFF 起點 reference。**

## 5.10 升 v0.19 後紀律

- 後續 NEW_REQ 新增繼續追加進 §1 / §2 區（既有結構）
- 11+ 輪 master 對話如要 partial supersede 本評估紀錄 → 開新 §5.X.X subsection；不修改既有 §5.1 ~ §5.9（屬 10th master 評估歷史紀錄）
- 7 個 deferred NEW_REQ 任一觸發 trigger 達成 → 對應 NEW_REQ entry 加 RESOLVED 紀錄 + 升相應 D-NNN 拍板
- NEW_REQ_16 lint script 實作對象擴展（含 NEW_REQ_9 27 模板 + 任何未來 cascade pattern）由 11+ 輪 master spec 規劃決定

## 5.11 NEW_REQ_20 10th master 紀錄確認（M4 user-test follow-up post-§5.9 新加）

| 項目 | 內容 |
|---|---|
| 性質 | 10th master Milestone 4 真正封版宣告完成後第一次 M4 user-test 跑前端 F1 Dashboard 發現的 finding；屬 §5.9 階段 6 評估總表完成後新加 |
| v0.20 狀態 | 🟡 DEFERRED — 推 11+ 輪 master patch |
| 10th master 評估 | **不本輪 patch**；屬封版後 user-test follow-up 自然 output；對齊 PHASE_D v1.1 §10.2 條件 8（M4 user-test 屬封版後活動）+ NEW_REQ_14 AI-assisted §6 補入機制的早期 sister case（同模式 user-test trigger 新 NEW_REQ）|
| 推薦處理時機 | 11+ 輪 master 對話起手時順手 patch（建議跟 NEW_REQ_16 lint script spec 規劃同輪處理；或 user 跑量產期間順手）|
| 本輪 action | 開 NEW_REQ_20 entry 紀錄於 §1（含完整 5 欄位 + 提議方案 3 選 + 對 Milestone 4 真正封版宣告無影響說明）+ §5.11 評估紀錄；不動 frontend code |
| Owner | 11+ 輪 master 對話 |

## 5.12 升 v0.20 後紀律（partial supersede §5.10）

- §5.10 原紀律維持有效（後續 NEW_REQ 新增繼續追加進 §1；11+ 輪如要 partial supersede §5 紀錄開新 §5.X.X subsection）
- 新增紀律：**M4 user-test follow-up 發現的 finding 屬 NEW_REQ_14 機制 + POST_LOCK_PENDING 雙重紀錄範圍**
   - finding 屬 frontend / skill runtime 發現 → 開新 NEW_REQ entry 紀錄於 §1（如本 NEW_REQ_20）
   - finding 屬 PHASE_X §6 user 親跑紀錄補入 → 走 NEW_REQ_14 AI-assisted §6 補入機制
   - 兩者可同輪 batch 處理
- NEW_REQ_20 屬「audit cycle 漏掉 finding」+「M4 user-test 自然抓出 finding」雙重性質範例；未來 NEW_REQ_21+ 若同性質可沿用本 entry 為 reference template

## 5.13 NEW_REQ_22 11th master 對話 A 紀錄（工具角色轉換 + Dynamic Workflows audit 路徑；POST_LOCK_PENDING v0.22 partial supersede）

| 項目 | 內容 |
|---|---|
| 性質 | 11th master 對話 A reframe 11th master scope；工具 A 從「自動寫作 pipeline」轉成「QA + 初始資料建置 + 專案管理」+ 外接寫作；用 Claude Code 2026-05-28 ship 的 Dynamic Workflows 並行 audit / screening 跑 11+ 輪累積 tech debt 大重構；屬封版後維護期戰略性轉向 |
| v0.21 狀態 | 不存在（NEW_REQ_22 為 v0.22 新建）|
| 11th master 對話 A 評估 | **本輪不寫 Dynamic Workflows audit 結果；只寫戰略落地交接文件** — 6 task 包：(1) 寫 SANDBOX_REFACTOR_PLAN.md v0.1（含 11 audit 任務 spec + sandbox bootstrap 指引 + first-run A1/B4/C1 建議）+ (2) 本 POST_LOCK_PENDING v0.21 → v0.22 partial supersede + (3) HANDOFF_TO_11TH_MASTER v1.0 → v1.1 §9 amendment + (4) HANDOFF_11TH_PARALLEL_SETUP v0.1 → v0.2 header note + (5) 建 root .gitignore 加 /_sandbox/ 排除 + (6) 寫 _sandbox/README.md |
| 推薦處理時機 | **user bootstrap sandbox 後親跑 Claude Code Dynamic Workflows**（first-run 建議 A1 + B4 + C1 三項 read-only audit；估 token 50K-130K / 耗時 10-30 分）→ 帶 audit report 回 11th master 對話 A → master REVIEW + cross-check + 人工 transcribe 結論回 production |
| trigger 條件 | user 依本 NEW_REQ_22 + SANDBOX_REFACTOR_PLAN bootstrap sandbox + 親跑 Claude Code Dynamic Workflows |
| Owner | 11th master 對話 A（戰略落地交接 + 後續 audit report REVIEW + 結論 transcribe）/ user（sandbox bootstrap + 親跑 Claude Code）|
| 本輪 action | 完成 6 task 包；audit pipeline 跑動推延到 user bootstrap 完成後 |

## 5.14 升 v0.22 後紀律（partial supersede §5.12）

- §5.12 原紀律維持有效（finding 屬 frontend / skill runtime 發現開新 NEW_REQ entry / finding 屬 PHASE_X §6 補入走 NEW_REQ_14）
- 新增紀律：**audit 結論回流走人工 transcribe 流程 — sandbox/audit-reports/ 內檔 read → master REVIEW → user 拍板 → 寫 NEW_REQ_23+ 進 §1 或新 audit summary 檔進 _design/**
   - finding 屬「新議題」→ 寫 NEW_REQ_23+ 進本檔 §1（用 NEW_REQ_22 為 template）
   - finding 屬「拍板需求」→ 升 D-056+ 拍板（user 拍板後落地）
   - finding 屬「audit summary 紀錄」→ 寫 `_design/AUDIT_2026Q2_REPORT.md` 或類似
   - finding 屬「明顯小 typo / wording fix」→ 直接 edit 對應 production 檔 + GIT SUMMARY
- ✗ 不從 sandbox/snapshot/ 內 cp 檔回 production（避免帶入未審 finding）
- ✗ subagent 不能 auto-commit / push 到 production
- 重要 lesson：commit 235debb 對本檔造成 §5.3-§5.12 ~110 行設計史意外截斷（CLAUDE.md 教訓 6 manifest）+ commit msg「更新」缺 rationale；屬 sandbox audit B1（NEW_REQ status 巡檢）+ B4（K-NN 表 inventory）first manifest case；未來 audit 應特別追根因 + 走 NEW_REQ_16 lint script 預防
- 教訓內化第 11 條（11th master 對話 A 新增）：**Edit tool 對 ~100 行以上中文新增內容仍有截斷風險；長中文 patch 一律改用 Python script via bash 一次性 write file 取代** — 教訓 6 (cat heredoc) 擴展為 (Python script 安全度更高，可邏輯化錯誤處理)

## 5.15 §5.3-§5.12 restoration audit trail（v0.22 補入）

| 欄位 | 內容 |
|---|---|
| 損壞發生時點 | commit 235debb (`Phase A.0F patch master "更新"` 2026-06-01 10:40 +0800) |
| 損壞 commit 內 POST_LOCK_PENDING.md diff | +117 / -113 行（淨 +4 行）；新增 NEW_REQ_21 STYLE_ANCHOR entry ~115 行；意外移除 §5.3-§5.12 ~110 行 |
| 損壞性質 | 極高機率為意外 truncation 而非 intentional removal — commit msg「更新」缺 rationale；STYLE_ANCHOR 升 D-055 本身是合理 batch 但對 §5 評估史無覆寫需求 |
| 對應 CLAUDE.md 教訓 | 教訓 6（長 multi-byte 檔請用 Python script via bash 或 cat heredoc 不用 Write/Edit tool 避免截斷風險）|
| 11th master 對話 A 處理 | 用戶拍板「選 1 restoration + 推進」 → restoration source: commit 3f60aa6 (`10th master M4 user-test follow-up: 新增 NEW_REQ_20`)；該 commit 為損壞前最後乾淨版本 |
| Restoration 操作 | first attempt 用 cat heredoc + Edit tool 混合策略 → Edit tool 自身又觸發截斷（教訓 6 第二次 manifest）→ second attempt 改純 Python script via bash 一次性 write file 取代成功 |
| Restoration verify | restored 後 §5.2 full + §5.3 NEW_REQ_14 + §5.4 NEW_REQ_15 + §5.5 NEW_REQ_16 + §5.6 NEW_REQ_17 + §5.7 NEW_REQ_18 + §5.8 NEW_REQ_19 + §5.9 階段 6 評估總結 + §5.10 升 v0.19 後紀律 + §5.11 NEW_REQ_20 + §5.12 升 v0.20 後紀律 全部還原 + 加 §5.13 NEW_REQ_22 評估 + §5.14 升 v0.22 紀律 + 本 §5.15 audit trail |
| 預防建議 | 屬 sandbox audit candidate finding；NEW_REQ_16 lint script 規劃時加「檔案截斷偵測」rule（行數驟降 + 結構斷裂偵測）|

## 5.16 NEW_REQ_22 first-run audit transcribe 紀錄（POST_LOCK_PENDING v0.23 partial supersede）

11th master 對話 A first-run sandbox Dynamic Workflows audit 結論已 transcribe 回 production。完整紀錄詳 `_design/AUDIT_2026Q2_REPORT.md` v0.1；本節屬摘要 + cross-ref。

| 項目 | 內容 |
|---|---|
| First-run runID | `wf_14f66b33-f4b`（2026-06-01 11:43:02 起跑；4m29s wall-time）|
| 架構 | Claude Code Dynamic Workflows；3 並行 read-only 分支（A1 / B4 / C1）+ 6 subagent |
| Token | 402K（< 500K 上限）|
| Report 落地 | `_sandbox/audit-reports/` 三 .md（A1 12.5KB + B4 9.5KB + C1 16.8KB；sandbox 內檔屬 .gitignore 排除暫存）|
| Audit 品質 | **0 fabrication** verified by master cross-check；所有 critical finding file:line+quote 對齊 production |
| 採納落地 batch | **Batch A** 5 個 edit（4 runtime SKILL D-055→D-056+ 順延 + SANDBOX_REFACTOR_PLAN K-11→K-09 fix）+ **Batch B** 7 檔 30 replacements（spec / starter / handoff stale D-055 ref 順延）+ **m2** 4 檔 41 path ref drift replacements（NN[A-Z]_ → NN_dir/NN_x_）+ **m3** 2 檔加交叉註記（句長 enum 刻意分層說明）|
| 對齊既有拍板 | DECISIONS_LOG §6.18.2:2209-2211 D-055 編號裁示（per-scene 順延 D-056+）；本輪 transcribe 全執行該裁示 |
| 不擅自啟新 D-NNN | ✗ 不擅自開 D-056；per-scene supersede 議題仍待 NEW_REQ_15 trigger 達成 + user 拍板 |
| 歷史檔保留 | ✓ HANDOFF_TO_9TH/10TH + D054_DECISION_PACKAGE APPLIED + CODEX_8TH_MASTER_FINAL_REVIEW x2 全保留（史料價值）|
| Deferred finding | (1) A1 scope 擴 00_f 角色創建協議 53 hits / (2) path ref drift 13 個非 m2-scope 檔 ~160 remaining refs / (3) 51 SKILL.md dead code（user 加碼 second-run B3）→ 全進 second-run |
| Stage 5 second-run | 待 user 帶 prompt 回 Claude Code（A2 + B1 + C3 + B3 + A1 scope 擴）|

**NEW_REQ_22 status：** 維持 PROCESSING；first-run cycle 完整收尾；待 user 啟動 second-run。

## 5.17 升 v0.23 後紀律（partial supersede §5.14）

- §5.14 原紀律維持有效（audit 結論回流走人工 transcribe；finding 性質分流到 NEW_REQ entry / D-NNN 拍板 / audit summary / typo fix）
- 新增紀律：**audit transcribe 完成同步寫 long-term audit log（`_design/AUDIT_2026Q2_REPORT.md`）+ 升 POST_LOCK_PENDING 對應 §5.X subsection；兩檔互為 cross-ref，audit-reports/ sandbox 暫存可 rm 不影響 production 端紀錄**
- 新增紀律：**audit 採納 finding 落地若涉「D-NNN 編號順延」屬執行既有拍板裁示性質 → 不需新 D-NNN；直接 transcribe + 紀錄 §5.X 即可**
- 新增紀律：**audit 發現 scope 擴展（如 m2 從 4 檔擴 17 檔）→ 嚴守原 scope 跑完 + 把擴展發現紀錄為 deferred finding → 轉 next run；不擅自 self-justify scope creep**
- 對應 §5.16 Batch A+B+m2+m3 全執行此紀律
- 教訓內化第 11 條繼續適用（長中文 patch 用 Python script via bash；本輪 §5.16 + §5.17 + AUDIT_2026Q2_REPORT 全採 Python script 寫）

## 5.18 NEW_REQ_22 second-run audit cycle 收尾紀錄（POST_LOCK_PENDING v0.24 partial supersede）

11th master 對話 A 已完整跑通 first-run + second-run audit cycle。second-run 結論 transcribe 已 land。完整紀錄詳 `_design/AUDIT_2026Q2_REPORT.md` §8；本節屬摘要 + cross-ref。

| 項目 | 內容 |
|---|---|
| Second-run runID | `wf_0c26aede-c8a`（user 跑於 Claude Code Dynamic Workflows）|
| 架構 | Stage 1 — 5 並行 read-only audit（A2 / B1 / C3 / B3 / A1.5）+ Stage 2 — Claude Code single-agent REVIEW（**首次驗證 CLAUDE_CODE_AUDIT_PROTOCOL.md design sound**）|
| Report 落地 | `_sandbox/audit-reports/`：5 audit report + 1 cross-check memo |
| Audit 品質 | Stage 2 REVIEW cross-check 嚴謹度 high；A2 三條中度 finding 全 cross-check 駁回；snapshot stale 主動標 + production re-verify |
| 採納 batch | **5 採**：§1 #1 iterate-* TBD → ✅（CLAUDE.md/AGENTS.md 14 處 + Wave 12 desc）+ §1 #2 dialogue-write v0.3（2 row）+ §1 #3 scene-task v0.2（2 row）+ §1 #6 NEW_REQ_19 RESOLVED（POST_LOCK_PENDING 2 處）+ §2 #5 細綱 export 單檔（UX_SPEC 3 處）共 23 處 patch |
| **1 Deferred** | §2 #4 角色檔名 hyphen vs underscore — scope expansion 嚴重（audit memo 估 2 檔 fix 實際 27 refs；含 reverse Wave 14 explicit directive `export-character SKILL.md L231`）→ 開 NEW_REQ_24 推 frontend audit cycle |
| 6 駁回 | #7 false positive / #8 ALREADY FIXED in prod / A2-a/b/c 三條（D-045/D-042 既有設計）/ #9 計數分母不同非矛盾 |
| 1 self-handled | C1 D-055 stale ref 本 cycle Batch A/B 已自己處理；audit 仍報是因 snapshot stale |
| 對齊 protocol | CLAUDE_CODE_AUDIT_PROTOCOL.md v0.1 §1.2 user checkpoint + §4 Stage 2 REVIEW + §5 Stage 3 APPLY（本 cycle 走 manual transcribe 路徑而非 Stage 3 APPLY，因 LOCKED spec 涉變動審慎）|
| 開啟 NEW_REQ_24 | 推 frontend dialogue 接手 |

**NEW_REQ_22 status：** 維持 PROCESSING；**first-run + second-run cycle 完整收尾**；CLAUDE_CODE_AUDIT_PROTOCOL.md 3-stage design 驗證 sound；frontend dialogue 接手 frontend AUDIT_PROTOCOL（含 NEW_REQ_20 dashboard 3 finding + NEW_REQ_24 角色檔名）。

## 5.19 升 v0.24 後紀律（partial supersede §5.17）

- §5.17 原紀律維持有效（audit 採納 finding 落地若涉「D-NNN 編號順延」屬執行既有拍板裁示性質 → 不需新 D-NNN；scope 嚴守原 audit scope 不擅自 self-justify scope creep）
- 新增紀律：**audit memo scope 估算可能低估；採納拍板執行前 master 必補做全 repo scan verify 真實 scope；如真實 scope > 估算 50% → 重拍板**
   - 本 cycle 範例：§2 #4 audit memo 估 2 檔 fix，master verify 後實際 27 refs → 觸發 scope expansion 重拍板 → 推 NEW_REQ_24 deferred
- 新增紀律：**audit transcribe 涉 LOCKED spec 變動屬必審項；單純 wording 對齊（如 UX_SPEC L592/L658/L791 內部不一致）可直接 patch；逆轉設計選擇（如 reverse Wave 14 implementer directive）需新 D-NNN 拍板或 deferred 處理**
   - 本 cycle 範例：§2 #5 UX_SPEC 3 處內部不一致 → 直接 patch（單純對齊）；§2 #4 reverse Wave 14 directive → deferred
- 新增紀律：**CLAUDE_CODE_AUDIT_PROTOCOL.md Stage 2 REVIEW 由 Claude Code 跑驗證 design sound 後**，11+ 輪後續 audit cycle 可優先用該 protocol（Cowork master 降為 optional consultant 模式生效）
- 對應 §5.18 second-run cycle 全執行此紀律

## 5.20 11th master 對話 B M4 user-test follow-up 評估紀錄總表（POST_LOCK_PENDING v0.25 partial supersede）

**評估日期：** 2026-06-01（11th master 對話 B M4 user-test follow-up sub-scope wrap-up）
**評估 owner：** 11th master 對話 B（M4 user-test follow-up sub-scope）+ user 拍板 Option (c) Hybrid（M4 wrap up + 接 frontend dialogue 拆另一部分）
**評估對象：** NEW_REQ_25-43（19 entries 對應 F1-F19；2026-05-25~2026-06-01 量產期間 chat-bridge 蒐集 + verify）
**完整 reasoning source：** `_design/M4_USER_TEST_REPORT.md` v1.0（700+ 行 cycle factual report；含 19 finding 完整 verify evidence + 5 meta-pattern + Wave 分組 + Claude Code workflow 餵入點）

**M4 user-test cycle 背景：**
- Instance repo：`D:\劇本開發\game-script-A`（《蟲潮孤堡》塔防遊戲；user 量產新 Instance；非原 prompt 設想的 `劇本開發工具-test`）
- 量產進度：/init-project → /create-world → /create-character × 4 → /create-relationship × 3 → /create-outline → /create-detailed-outline（pending REVIEW gate）
- 平行 batch（不影響本 sub-scope）：STYLE_ANCHOR D-055 implementation batch（2026-05-28 完成；W-style entity 新增）+ 11th master 對話 A reframe（v0.21 → v0.24）

### 5.20.1 19 finding 分類統計

| 分類 enum | 數量 | Finding ID |
|---|---|---|
| 🐛 spec drift bug | 4 | F1 / F3 / F6 / F15 |
| 🐛 spec gap / runtime gap | 1 | F5 |
| ⚠ design gap | 14 | F2 / F4 / F7 / F8 / F9 / F10 / F11 / F12 / F13 / F14 / F16 / F17 / F18 / F19 |
| **嚴重度 CRITICAL** | 2 | F3 / F13 |
| **嚴重度 MAJOR** | 11 | F1 / F6 / F7 / F8 / F9 / F11 / F12 / F14 / F16 / F19 |
| **嚴重度 MINOR / MINOR-MAJOR** | 6 | F2 / F4 / F5 / F10 / F15 / F17 / F18 |

### 5.20.2 5 大 Meta-pattern

| Meta-pattern | Findings | 數量 | 共同根因 |
|---|---|---|---|
| **A — Phase A→B chain coherence** | F1 / F3 / F5 / F6 / F7 / F8 | 6 | /init-project → /create-world → /create-character 上游接口設計不完整；spec 跟實際 LOCKED template / user 真實使用案例對不齊 |
| **B — /create-character 品質提升 5-step pipeline** | F9 / F10 / F11 / F12 / F13 | 5 | ingestion 機制 → input → output 3 fixed sections 缺；user 量產實測 motivating evidence |
| **C — CLI / lint / parser 工具層** | F2 / F4 / F15 | 3 | scripts/ 工具友善度 + 防呆強化 |
| **D — Agent context / UX layer** | F10 / F14 | 2（F10 重複計入 B）| ARCH §3.3.0 multi-agent invocation 慣例 D-048 落地後續擴充未跟進 |
| **E — Outline 層品質提升 chain** | F16 / F17 / F18 / F19 | 4 | /create-outline + /create-detailed-outline 量產撞到的 UX gap；分通用 vs genre-specific |

### 5.20.3 Wave 分組（按 ROI / 風險 / 依賴）

| Wave | Finding | 工時範圍 | 風險 | 觸發條件 |
|---|---|---|---|---|
| **Wave-A1** quick-wins | NEW_REQ_38 (F14) + NEW_REQ_39 (F15) + NEW_REQ_29 (F5) + NEW_REQ_30 (F6)[依 D-059] + NEW_REQ_33 (F9) + NEW_REQ_36 (F12) + NEW_REQ_28 (F4) + NEW_REQ_40 (F16) + NEW_REQ_43 (F19)[依 D-061] | 25-44h | 🟢 LOW | 立即可啟動；部分依 D-NNN |
| **Wave-A2** D-NNN dependent | NEW_REQ_27 (F3)[D-056] + NEW_REQ_31 (F7)[D-057] + NEW_REQ_25 (F1)+NEW_REQ_30 (F6) 整合[D-059] | 18-27h | 🟡 MED | 需 user 拍板 D-NNN |
| **Wave-A3** Cross-layer / 中工時 | NEW_REQ_35 (F11)+NEW_REQ_37 (F13) 合併 + NEW_REQ_34 (F10) + NEW_REQ_41 (F17)+NEW_REQ_42 (F18) pattern pack[D-060] + NEW_REQ_43 (F19)[D-061] | 23-39h | 🟡 MED | F11+F13 必同輪；F17+F18 需 D-060 |
| **Wave-A4** F8 短中期 | NEW_REQ_32 (F8) 方向 C + 方向 B[D-058] | 5-10h | 🟡 MED | 需 D-058 |
| **Wave-A5** F8 long-term（可選；推 13+ 輪）| NEW_REQ_32 (F8) 方向 A 新 F-*/ORG-* entity | +30-50h | 🔴 HIGH | 跨 entity_type_registry + 11 SKILL.md |
| **Wave-A6** F2 併 NEW_REQ_16 lint | NEW_REQ_26 (F2) + NEW_REQ_16 spec 規劃 | 6-10h | 🟢 LOW | 屬封版後維護期 |

### 5.20.4 4 種 scope option（user 後續拍板）

| Option | 內容 | 工時 |
|---|---|---|
| **α** | 本 POST_LOCK_PENDING v0.25 + M4_USER_TEST_REPORT.md v1.0 落地；後續完全推 12+ 輪 master | **3.5-5h**（本對話 wrap-up；已完成）|
| **β（推薦）** | α + Wave-A1（9 個 quick-medium-win） | +25-44h |
| **γ** | α + 完整短中期（Wave-A1+A2+A3+A4）| +71-120h |
| **δ** | γ + Wave-A5（F8 long-term） | +30-50h |

### 5.20.5 D-NNN candidate 6 個（user 後續拍板）

| D-NNN | 對應 Finding | 用途 |
|---|---|---|
| D-056 | F3 / NEW_REQ_27 | /create-world split rule 修哪邊（SKILL.md / template / anchor）|
| D-057 | F7 / NEW_REQ_31 | source/reference dir convention |
| D-058 | F8 / NEW_REQ_32 | 非人格反派 entity 方向 A/B/C |
| D-059 | F1+F6 / NEW_REQ_25+30 | template skeleton 起始狀態語意 + Phase 4 狀態 bump |
| D-060 | F17+F18 / NEW_REQ_41+42 | pattern pack 機制（依 00_b §1 作品類型載入 mode）|
| D-061 | F19 / NEW_REQ_43 | 個人線邊界規則 |

### 5.20.6 Claude Code workflow 餵入策略

依 CLAUDE_CODE_AUDIT_PROTOCOL.md：
- **跳過 Stage 1 AUDIT** — 本對話已完成 verify；findings 屬「user-test direct observation + master verification」性質
- **Stage 2 REVIEW** — 把 19 NEW_REQ 拆 9 個 batch（B1-B9；按 Meta-pattern + D-NNN 依賴分組；詳 `M4_USER_TEST_REPORT.md` §6.2）
- **Stage 3 APPLY** — 依 user 拍板 Wave 順序（建議 β 路線；Wave-A1 quick-wins 第一個處理；F14 瘦身應**最先**）

### 5.20.7 跨 batch 互動紀錄

| 互動 | 涉及 |
|---|---|
| STYLE_ANCHOR W-style ↔ NEW_REQ_37 (F13) | W-style 作品級文風指紋；F13 角色級聲線基準；理想架構 F13 voice card 繼承 W-style 文風指紋 + 加 character-specific 聲線特徵；F13 patch 時 cross-ref STYLE_ANCHOR 機制 |
| 11th master 對話 A reframe ↔ NEW_REQ_38 (F14) | F14 瘦身 patch 應同步更新 AGENTS.md 反映 reframe 後 frontend handoff 機制 + STYLE_ANCHOR 後 scene-task v0.2 / dialogue-write v0.3 |
| Frontend dialogue scope vs M4 follow-up | F1-F19 全 0 個 frontend finding；自然切乾淨；frontend dialogue scope（NEW_REQ_20 dashboard + NEW_REQ_24 角色檔名）不在本批 |
| PHASE_D §6 補入機制 (NEW_REQ_14) | `M4_USER_TEST_REPORT.md` v1.0 含 user 親跑 M4 chain 事實摘要；可作為 NEW_REQ_14 AI-assisted §6 補入機制 reconstruct 草稿來源；user 後續可拍板「採」/「改後採」/「棄」決定是否 patch `PHASE_D_COMPLETION_REPORT.md` §6 placeholder |

## 5.21 升 v0.25 後紀律（partial supersede §5.19）

- §5.19 原紀律維持有效（audit memo scope 估算 / audit transcribe LOCKED spec 變動需新 D-NNN / CLAUDE_CODE_AUDIT_PROTOCOL Stage 2 REVIEW 由 Claude Code 跑驗證 design sound）
- 新增紀律：**user-test follow-up sub-scope 累積 finding 寫進 NEW_REQ 時，必同時寫對應 cycle factual report**（如本 cycle 的 `_design/M4_USER_TEST_REPORT.md` v1.0）作為 reasoning source；NEW_REQ entry 屬 condensed reference；完整 verify evidence + Claude Code workflow scope 保留在 cycle report
- 新增紀律：**chat-bridge 蒐集模式（user 在 skill 對話撞 finding → 切到 user-test follow-up 對話貼 → master verify + 分類 + 紀錄）的後續 cycle 應沿用本 cycle 範例**：(1) Scratch table incremental update（chat context 不落地）(2) wrap-up trigger 時批量落地 POST_LOCK_PENDING + cycle report（避免每 finding 都動磁碟）(3) 跨 batch 互動明示 cross-ref（STYLE_ANCHOR / 對話 A reframe / PHASE_D §6 等）
- 新增紀律：**finding 跟既有 NEW_REQ 重疊時必明示判斷**：本 cycle F11 + F13 是 input + output 層必同輪實作；F1 + F6 同根因可合 D-NNN 拍板；F17 + F18 同 pattern pack 機制 — 紀錄這些連動關係於 NEW_REQ entry cross-ref 段
- 新增紀律：**Claude Code workflow Stage 2/3 餵入點明示**：每 finding NEW_REQ entry 含「Owner」段（Claude Code workflow Stage X / 11+/12+ 輪 master / Cowork master 諮詢）+ cycle report §6 含 Stage 2 batch 分組建議；省 Stage 1 AUDIT 步驟（findings 已 verify）

---

## 5.22 11th master frontend dialogue cycle 收尾紀錄（POST_LOCK_PENDING v0.26 partial supersede）

| 欄位 | 內容 |
|---|---|
| cycle | 11th master frontend dialogue（接 FRONTEND_HANDOFF；路徑 M）|
| 時點 | 2026-06-01 |
| workflow | 3-stage（Stage 1 用 Claude Code Dynamic Workflows 5 並行 read-only Explore 子代理；runID `wf_e5ec596f-bce`；610K token / 3m wall）|
| Stage 1 AUDIT | 5 report：F-A1 deadcode / F-A2 dashboard / F-A3 backend-state / F-B1 filename / F-C1 reframe（落 `_sandbox/audit-reports/`）|
| Stage 2 REVIEW | master cross-check 全 finding 對 production verify（0 fabrication；嚴重度校正 F-A1 CRITICAL→MINOR 等）；memo 落 `_sandbox/review-reports/REVIEW_frontend_cycle_20260601.md` |
| Stage 3 APPLY | user 逐 finding 拍板：NR24 Option 1 / F1-3 前端修+backend 拆 / F1-2 mapping / dead file 刪 / scope C defer |
| 採納統計 | 落地：A1-1/A1-2 dead file git rm + F1-2 + F1-3a（ProjectDashboard.js）+ NEW_REQ_24 Option 1（~26 refs 6 檔）；拆：NEW_REQ_44（backend）+ NEW_REQ_45（scope C defer）|
| 測試 | frontend node 4 test files + python smoke 22 全 PASS（含 patch_round_regression）|

**關鍵教訓（內化）：**

1. **kickoff 指令 stale 偵測**：FRONTEND_HANDOFF / KICKOFF 寫「POST_LOCK_PENDING v0.24 / 開 NEW_REQ_25」，但接手時實檔已是 v0.25 且 NEW_REQ_25-43 被對話 B 佔用（commit 08605a7）。frontend cycle Stage 4 前先 grep 最高 NEW_REQ 編號 → 改用 NEW_REQ_44/45，未 clobber 對話 B work。**後續 cycle 接手前必 verify 交接文件版本 vs 實檔版本。**
2. **audit memo scope 校正再現**：NEW_REQ_24 memo 估 2 檔，frontend cycle Stage 1 F-B1 verify 為 ~26 canonical refs（+ snapshot 鏡像更多）；嚴守 Option 1 不動 LOCKED spec → 無需 D-056。
3. **「完整 backend」拆分紀律**：NEW_REQ_20 F1-3 原提「接 backend」，F-A3 audit 揭示 backend 需先定 3 data schema（超 frontend scope）→ 前端先修顯示 bug（spec-correct 標題 + 空狀態），backend 拆 NEW_REQ_44。避免 frontend cycle 越界改 09_quality_assurance 模板 / 協議。
4. **F-C1 過度建構偵測**：audit 報告末段建議「開 NEW_REQ_25-43 / β 路線」碎片化 19 entry —— 違反工具角色「不過早重做」；改為單一 tracking NEW_REQ_45 + 待 user 實操 evidence。

