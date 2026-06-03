狀態：DEPRECATED
版本：v1.0（Batch 4（F8 ORG）續跑設計文件 — Phase 3 重做 + Phase 4-7（含 DRY 版 Phase 7）+ 自我 QA；自主長跑模式；user 離線期間執行；2026-06-03）
最後更新：2026-06-03
適用範圍：給被截斷的 Batch 4 對話（或接手的新對話）續跑 — 冷啟動可讀、可長時間自主執行、自我 QA、停在 L3 gate
優先級：高

# BATCH4_RESUME — F8 續跑（Phase 3-7 + 自我 QA / 自主長跑）

## 0. 一句話現況（先讀）

你（Batch 4）被 user 在 Phase 3 期間截斷，已跑約一小時。**但 git 已提交的進度只到 Phase 2**（HEAD 線：`0bd67fb` F8 Phase 2 = create-character gate→ORG + /status ORG 列舉）。**那一小時的 Phase 3 工作未 commit → 已遺失。** user 已離線去睡，本檔授權你**自主長時間續跑 + 自我 QA**，但**停在 L3 人工簽字 gate**（見 §2 規則 5）。

## 1. ⚠️ 開工前自我盤點（CRITICAL，先做再動工）

不要相信「我之前做到 Phase 3」的記憶——**以 git 實況為準**：
1. `git -C "D:/劇本開發工具" log --oneline -10`：確認已 commit 到哪個 Phase（目前 = Phase 2 `0bd67fb`，加 docs `739bc76`）。
2. `git status --short`：確認主樹乾淨。
3. **逐一驗證每個「宣稱完成」的 Phase 其產物是否真在 repo**（§7 無聲失敗教訓）：Phase 1 ORG registry entry 在不在？Phase 2 /create-character gate + /status ORG 列舉在不在？**Phase 3（view/export ORG）的檔在不在 → 不在就從 Phase 3 重做。**
4. 結論：**從第一個「未真正 landed」的 Phase 接續**（預期 = Phase 3）。

## 2. 🤖 自主長跑模式守則（user 離線期間，務必遵守）

1. **每個 Phase 一結束就 checkpoint commit**（血淚教訓：剛才一小時 Phase 3 沒 commit、截斷即遺失）。用具體 path `git add <檔>`，**勿 `git add -A`**（會掃進 `scripts/__pycache__/*.pyc`）。commit message 標 Phase + NEW_REQ + D-NNN。
2. **在隔離分支跑**：從現在 HEAD 開 `git checkout -b feat/batch4-phase4-7`，後續全在此分支 commit。**不要在 user 睡覺時把 Tier-4 / Phase-7 的 LOCKED 改動 merge / push 到 `frontend-tools-a0f`**——那要等 L3（見規則 5）。
3. **重活用 dynamic workflows**：Phase 7 的規格轉換 fan-out、以及 §4 自我 QA，都該用 Workflow 工具跑（這是「動 LOCKED / 跨大量檔」該用重型 workflow 的場景）。
4. **別停下來等 user**（他在睡）。遇到「真正需要 user 拍板」的決策（破壞向後相容、CRITICAL 設計分叉、要不要動 user 沒授權的檔）→ **寫進 §5 WAKE-UP 決策佇列，用最安全、可逆的預設繼續**，不要卡死、也不要亂猜硬幹。
5. **🛑 停在 L3 gate（不可違反）**：所有 Phase + 自我 QA 跑完後，**不可自行把 Tier-4 / LOCKED 改動 merge 到 `frontend-tools-a0f`**——REVIEW_LOOP_PROTOCOL L3 + AGENTS.md 規則 4 要求人工簽字 + rule-4 LOCKED 核准，agent 不可代簽。把成果 park 在 `feat/batch4-phase4-7` 分支 + 產出 §5 wake-up 報告，等 user 醒來審閱簽字。**你可以 push 該 feature 分支**（方便 user 審），但**不 merge 進主分支**。
6. **保守原則**：動 LOCKED 規格時，能用「保留鏡像 + 標註『權威見 registry』」就不要激進刪除；不確定的改動寧可標 TODO + 入 §5 佇列，不要賭。

## 3. 剩餘 Phase 展開（從 Phase 3 接續）

每個 Phase 的收尾固定動作：**做 → checkpoint commit → L1 workflow 獨立審 → L2 跑腳本（check_paths/check_headers/build_repo_index/tests）→ 修 → 再 commit**。

- **Phase 3 — `/view-org` + `/export-org`**（重做）：仿 view/export-character；view 不寫檔、export 寫 `view/組織_*.md` DERIVED。+ 中文 wrapper。
- **Phase 4 — `/iterate-org`**：仿 iterate-character（00_j 五階段 + impact backtrace：動組織卡要回溯哪些角色隸屬、哪些場景/大綱提到）。+ wrapper。
- **Phase 5 — 跨引用接線**：`/status` 缺漏建議含 ORG；角色↔組織關係表達方式（沿用 R-* 還是新欄位——若涉設計分叉入 §5 佇列）；大綱/細綱/場景/台詞如何引用 ORG（`01_a §9 勢力與組織` 是否升為指向 ORG entity）。
- **Phase 6 — QA + /status 計數收尾**：qa_type_registry 是否需 ORG 專屬 QA（或沿用既有）；確認 /status、build_repo_index 對 ORG 計數正確。

### Phase 7 — LOCKED 規格對齊 = **DRY 指標版**（user 已拍板折入，非手加列舉）

⚠️ **不要**手動把 ORG 逐一塞進 ~10 份規格的型別列舉（會導致同批規格未來被改第二次）。改做：
1. 那 ~10 份枚舉 entity 型別的 LOCKED 規格（UPSTREAM_DOWNSTREAM_SPEC / SPEC / DATA_FORMAT_SPEC / INTEGRATION_CONTRACTS / ARCHITECTURE / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA / UX_SPEC 等）：能改指標的，改成「entity 型別清單以 `entity_type_registry` 為唯一權威」並移除硬列舉；因契約/可讀性必須保留列舉的，**標註「（鏡像；權威見 entity_type_registry）」並確保與 registry 一致**。
2. `/status` 型別清單 + weight 改讀 registry（回工 Phase 2 手接的部分，別寫死）。
3. `check_paths.py` ACTIVE_DIRS / `check_headers.py` TEMPLATE_PATTERNS 改從 registry `target_dir` 推導，不再寫死目錄清單。
4. 吸收 **NEW_REQ_47**（`parse_frontmatter.py` entity-type 硬編碼鏡像 → registry-derived）。
5. **刻意不做**：把每個 SKILL 內文邏輯全改 registry-generic（回報遞減，留未來可選 = NEW_REQ_49 殘餘）。
6. 把 **NEW_REQ_47 + NEW_REQ_48** 標為「併入 B4 Phase 7 解決」；開 **D-074**（你 B4 預留段下一個乾淨號；已用 D-071/072/073）記「Phase 7 = DRY 指標版」拍板 + 理由 + 影響範圍。
7. Phase 7 是 Tier-4（動更深、ORG drift 風險最高）→ 走完整四層防線；L1 用 workflow fan-out 審跨規格一致性。

## 4. 自我 QA（Phase 7 後，跑 BATCH4_POSTLAND_AUDIT）

全 Phase 在 `feat/batch4-phase4-7` 完成後，**自我 QA = 直接跑 `_design/BATCH4_POSTLAND_AUDIT.md` §5 的 workflow 腳本**（傳給 Workflow 工具）。該稽核 §0 前置「全 Phase 完成 + 樹乾淨」此時在本分支成立。它會：7 維 fan-out（含 ORG 功能 smoke test）→ 對抗式 verify → 合成報告。

收到稽核 report 後：
- **親自復跑 smoke test 的任何 FAIL 步驟**（§7 無聲失敗：別只信合成）。
- CRITICAL / MAJOR 且**修法安全可逆** → 自主修 + checkpoint commit + 記錄。
- 涉設計判斷 / 破壞相容 / 不確定 → **入 §5 WAKE-UP 決策佇列**，不自行硬幹。
- drift 類 finding → cross-ref 進 NEW_REQ_49。

## 5. 🌅 WAKE-UP 報告 + 決策佇列（park 等 L3）

全部跑完後，產出一份給 user 的 wake-up 報告（印在對話 + 建議落成 `_design/BATCH4_WAKEUP_REPORT.md`），含：
1. **landed 清單**：`feat/batch4-phase4-7` 上每個 Phase 的 commit hash + 一句話。
2. **自我 QA 結論**：稽核 report 摘要（confirmed findings 依嚴重度 + smoke test 結論）。
3. **自主修了什麼**：列自動修正項。
4. **WAKE-UP 決策佇列**：所有「需要 user 拍板」的項目（每項：問題 / 你採的安全預設 / 待 user 確認的選項）。
5. **L3 + rule-4 簽字請求**：明列哪些是 LOCKED 改動需 rule-4 核准、L3 抽查指引（REVIEW_LOOP §2：開 CRITICAL/MAJOR diff、抽 1 個 PASS 檔複看、親跑 L2）。
6. **merge 指示**：user 簽字後的 merge `feat/batch4-phase4-7` → `frontend-tools-a0f` + push 步驟。
7. **明確聲明：尚未 merge 進主分支，等 L3。**

## 6. Cross-ref

- `_design/BATCH4_POSTLAND_AUDIT.md`（§4 自我 QA 用的稽核 workflow）
- `_design/REVIEW_LOOP_PROTOCOL.md`（四層防線；L3 不可代簽）
- `_design/HANDOFF_BATCH2_BATCH4_PARALLEL.md`（B4 scoped brief + D-NNN 預留 D-071~074 + 碰撞 map）
- NEW_REQ_32（F8 源）/ 46/47/48（drift 證據）/ 49（registry DRY 重構，殘餘 skill-generic 部分）
- F8 Phase 完整展開：見本對話交付脈絡（registry → create → view/export → iterate → 跨引用 → QA → 規格 DRY 對齊）
