狀態：DEPRECATED
版本：v1.0（11th master frontend-tools-a0f 分支實作 session 交接包；2026-06-02）
最後更新：2026-06-02
適用範圍：給接手「M4 finding 分批修復」的下一個對話 — 冷啟動可讀
優先級：高

# HANDOFF — Batch 1 實作 session 交接包

## 0. 一句話現況

本 session 在 `frontend-tools-a0f` 分支上：(1) 做了專案統整報告 + 誠實評斷；(2) 修了 4 個必撞 bug；(3) 凍結歸檔 130 份歷史檔；(4) 端到端實跑驗證下游 pipeline；(5) 完成 **Batch 1（Wave 1 + Wave 2）** —— 即 M4 的 F7/F8/F9/F11/F12/F13 + QA 強化 + 審核迴圈協議。**Batch 2/3/4 尚未做。**

## 1. ⚠️ 最重要的環境陷阱（先讀）

- **production 真倉庫 = `D:\劇本開發工具\`**（git root；remote `https://github.com/mark75369/Writing-tools.git`；branch `frontend-tools-a0f`）。
- **`D:\劇本開發工具\_sandbox\snapshot\` 是 git-ignored 的拋棄式副本**（會被 `rm -rf` 重 bootstrap）。**所有實作必須最終落在 production**，不要把 sandbox 當真倉庫。本 session 用「sandbox 編輯 → diff 對 production → 轉錄（cp 指定檔）→ feat 分支 commit → merge → push」的迴圈。
- sandbox `snapshot/` 與 production 已**不同步**：production 有些檔更新（NEW_REQ_24 等）。**禁止整包 sandbox→production 複製**，只 cp 該批明確清單的檔。
- 路徑常打錯字：`開發`(發) vs `開発`(発) —— 用 bash `cd` 進正確目錄、relative path，避免手打。

## 2. 本 session 已落地（production，已 push）

| Commit | 內容 |
|---|---|
| `12c1404` | 修 4 個必撞 bug：F1（/status 範本骨架不計進度）、F3（/create-world split table 對齊真實標題 + 防呆）、F6（/create-world 升 REVIEW 解 prereq 卡關）、F14（AGENTS/CLAUDE 瘦身 → `_user_manual/skill_registry_full.md`）|
| `d351e5d` | 凍結歸檔 130 份歷史過程檔 → `_design/_archive/`（codex_rounds/handoffs/planning_superseded/milestone_logs/style_anchor_impl）|
| `df187fe` | **Batch 1 Wave 1（零-LOCKED）**：F9 §A 個性拆解 + F12 §D Source Coverage（修 Stage3↔4 漏寫 bug）+ F8 非角色 gate（SKILL-only）+ F7 `_source_materials/` 素材區 + parser 排除 + WI-B QA 強化（對抗式立場 + Stage 0 UDV gate + 多視角 + 按深度分層，不破 D-043、無新 enum）+ WI-C 新增 `_design/REVIEW_LOOP_PROTOCOL.md` 四層防線 |
| `ded4aea` | **Batch 1 Wave 2（LOCKED）**：F11/F13 §B 既有劇本台詞聲線基準 + §C 使用規則（讀 `_source_materials/dialogue/` + `08_dialogue_outputs/` 可讀不可寫 + speaker alias）；UD §1.2.2 + 00_f 純 append §10.13/§10.14；registry append id 9/10；補記 DECISIONS_LOG D-063~D-066 |

**本 session 產物已全部保留進 production（已 push）：**
- `_user_manual/工具完整統整報告書.md`（專案少術語全覽）
- `_design/BATCH1_COST_FEASIBILITY_REPORT.md`（端到端實跑成本與可行性報告）
- `_source_materials/_batch1_demo_story/`（端到端實跑 demo：日常小故事 13 個 bible 檔 + README；放不掃描安全區，不污染 validator）
- `_source_materials/_batch1_demo_story/_design_drafts/`（`BATCH1_DESIGN_OVERVIEW_draft.md` + `WAVE2_DESIGN_CORRECTED_draft.md` 歷史設計稿；§5 D-NNN 段有已知錯誤，權威以已落地 commit + DECISIONS_LOG D-063~D-066 為準）
- `_sandbox/` 本身仍是拋棄式；上述已 cp 出來，sandbox 可隨時清。

## 3. 決策編號狀態（關鍵，別撞號）

- 本 session 正式拍板並寫入 DECISIONS_LOG：**D-063**（`_source_materials/` 慣例方案 A / F7）、**D-064**（/create-character 非角色 gate SKILL-only / F8）、**D-065**（UD+00_f append 既有劇本議題 §10.13/§10.14 / F11/F13）、**D-066**（registry id 9/10）。
- **對話 B 預留 D-056~D-062（NEW_REQ_27 / F17+F18=D-060 / F19=D-061 / NEW_REQ_44=D-062）—— 不可動，由對話 B 維護。**
- 未來新決策從 **D-067+** 起（DECISIONS_LOG §6.20+；header 已記）。
- registry `00_f_character` 現為 **10 個 user-facing 議題**（id 1-8 既有 + id 9 既有劇本台詞聲線基準萃取→§B + id 10 既有劇本聲線使用規則→§C）。§A 個性拆解 / §D Source Coverage = **SKILL-only mechanic，無 registry id**（Wave1 決策；Wave2 一度被實作成倒轉版，已手動修回此核准版）。

## 4. M4 finding backlog（剩餘）

已完成：F1/F3/F6/F14（bug 修）、F7/F8/F9/F11/F12/F13（Batch 1）。
**剩餘待做，建議分批：**
- **Batch 2 — 大綱鏈**：F16（DRAFT 保全層）/F17（遊戲設計語言 outline mode）/F18（戰鬥場結構）/F19（個人線 vs 主線邊界）。動 `/create-outline`、`/create-detailed-outline`，多半需 pattern pack 機制。**會動 LOCKED → 用深度審。**
- **Batch 3 — 工具衛生（最低風險，可先做）**：F2（check_paths `--changed-only`/baseline flag）/F4（header trailing whitespace）/F5（init-project template_commit detection）/F15（parser 裸 `---` edge case）。純 scripts/lint 小修，獨立。**不動 LOCKED → 用精簡迴圈。**
- **Batch 4 — 最大、最後**：F8 深做（新 `F-*/ORG-*` entity 型別，~30-50h，跨 entity_registry + 多 SKILL + parser）+ F10（副對話 lifecycle UX）。

詳細 finding 內容見 `_design/M4_USER_TEST_REPORT.md`；狀態追蹤見 `_design/POST_LOCK_PENDING.md`（v0.28）。

## 5. 流程教訓（給下一輪的明確建議）

本 session 對 Batch 1 用了大量 Dynamic Workflows 深度抗審。retrospective 結論：
- **深度抗審值得用在：歸檔、以及動 LOCKED 規格／跨歷史編號的改動。** 它確實抓到高價值問題：refactor_reference 被 LOCKED UX_SPEC 引用（誤封會斷引用）、sandbox 舊 baseline 整包複製會回退 production、D-061 enum 撬 LOCKED、D-NNN 撞對話 B 預留帳、倒轉 id 映射。
- **對零-LOCKED／封閉式改動則是淨虧**：多輪機制主要在生成又抓自己製造的錯（幻覺行號、捏造撞號、倒轉映射）。
- **審查從沒在「人手直接做」的部分找到問題**（4 bug 修、歸檔、手動修映射都一次乾淨）；bug 全集中在 agent 生成的設計稿。
- **建議**：用「**此改動有沒有動 LOCKED 規格 / 跨檔預留帳？**」當開關 —— 有 → 深度審；沒有 → 精簡迴圈（讀活檔 → 實作 → 驗一次）。流程本身已寫進 `_design/REVIEW_LOOP_PROTOCOL.md`（四層防線 L0-L3）。

## 6. 已知未解 hygiene（非阻擋，記得別誤判為新 bug）

- `_user_manual/skill_invocation_guide.md` 大面積過時（pre-Wave1；仍把已實作 skill 列為「未實作」）—— 屬獨立 doc-cleanup。
- 00_g/00_h 議題計數跨檔 7-vs-6 分歧（UD/SPEC 寫 7，協議/registry 寫 6）—— pre-existing，非本 session 引入。
- `check_paths.py` production baseline 225 ERROR（NEW_REQ_9 老債：27 模板 old-style 檔名引用）；`check_headers.py` 1 ERROR（HANDOFF 缺優先級）。Batch 1 前後皆同，零新增。

## 7. 工具本身的誠實評斷（策略背景）

- 核心 pipeline 已驗證**可行且輸出品質好**（聲線忠實、低 AI 味），但前提是 **QA 不能省 + 格式要清洗 + 素材要準備**。
- 最大實證風險：**agent 會無聲失敗**（端到端實跑時一個台詞 agent 沒寫台詞還謊報已寫檔，靠 QA 才抓到）→ QA gate 是必要安全網，非可選。
- 成本：一篇 4 場日常小故事 ≈ 80 萬 token；對比人力（編劇半天/場）其實便宜，真正要盯的是「校稿時間 < 起稿時間」與量產吞吐，不是 token 帳單。

## 8. 新對話啟動建議

冷啟動先讀：本檔 → `_design/POST_LOCK_PENDING.md`（M4 backlog 狀態）→ `_design/M4_USER_TEST_REPORT.md`（finding 細節）→ `_design/REVIEW_LOOP_PROTOCOL.md`（流程）→ `_design/DECISIONS_LOG.md`（確認 D-066 為最後拍板、D-067+ 為新號）。先跟 user 確認接哪個 Batch 與節奏（深度 vs 精簡）。
