狀態：DEPRECATED
版本：v1.1（過夜自主總執行計畫：F8 Phase 3 → 稽核 → Batch 5 → Step 4 最終全稽核 + 技術債清掃；user 離線、停在 L3 gate；v1.0 → v1.1 補 Step 4 QA 閉環；2026-06-03）
最後更新：2026-06-03
適用範圍：給「過夜獨佔驅動 F8 Phase 3 + 稽核 + Batch 5」的單一新對話 — 冷啟動可讀、自主長跑、停在 L3、產 wake-up 報告
優先級：高

# OVERNIGHT — F8 Phase 3 → 稽核 → Batch 5（自主長跑總計畫）

## 0. 一句話

你是**唯一**獨佔驅動這條鏈的對話：**reconcile F8 編號 → 跑完 F8 Phase 3（ORG authoring stack）→ 跑 BATCH4_POSTLAND_AUDIT → 跑 Batch 5 registry DRY 重構 → Step 4 最終全稽核 + 技術債清掃**。user 已離線睡覺。你**自主做完所有 work + 把整輪 QA 跑完閉環，但停在 L3 人工簽字 gate，不 merge 任何 LOCKED 改動進主分支**。user 醒來只剩「審閱 + 簽字」，不必清醒等 QA。

## 1. ⚠️ 啟動前提（先驗，缺一就停下回報）

1. **你是唯一驅動者**：啟動前確認**其他平行 F8 對話已停**（曾有兩條 master 對話同 branch 驅動 F8 → 必撞）。若偵測到他人正在 commit，停下回報。
2. **環境**：production = `D:\劇本開發工具\`（branch `frontend-tools-a0f`；remote Writing-tools）。`_sandbox\snapshot\` 拋棄式。`git -C "D:/劇本開發工具"`。`__pycache__` 已 gitignore。Windows 設 `PYTHONUTF8=1`。
3. **開隔離分支** `feat/f8p3-audit-batch5`（從現在 HEAD `6880fab` 或更新者）。整條鏈在此分支 commit。
4. **git 現況**：HEAD 線含 F8 Phase 1/2 已 land + 4 份設計/交接 doc（BATCH4_POSTLAND_AUDIT / BATCH4_RESUME / D074_DECISION_PACKAGE / HANDOFF_F8_PHASE3 / BATCH5_REGISTRY_DRY）。F8 committed 只到 **Phase 2**。

## 2. 🛑 L3 真相（不可違反）

整鏈是 Tier-4（LOCKED 規格 + parser 核心 + 新協議 00_n + skills）。**REVIEW_LOOP_PROTOCOL L3 + AGENTS.md 規則 4 要求人工簽字 + rule-4 核准；agent 不可代簽、不可自行 merge LOCKED 改動進 `frontend-tools-a0f`。** 你做完所有 work + 自我 QA 後 **park 在 `feat/f8p3-audit-batch5`**（可 push 此 feature 分支供審）+ 產 wake-up 報告。**「跑到 Batch 5 結束」= 做完並 park，不是 merged。**

## 3. 自主長跑守則

1. **每完成一個 segment / Phase 就 checkpoint commit**（具體 path，**勿 `git add -A`**；訊息標 segment + NEW_REQ + D-NNN）。教訓：未 commit 的長跑一截斷就全遺失。
2. **重活用 dynamic workflow**：F8 Phase 3 各 step 的 L1 外審、稽核（BATCH4_POSTLAND_AUDIT §5）、Batch 5 重構（BATCH5_REGISTRY_DRY §4）都有現成腳本。
3. **每個 Phase 走四層防線的 L0→L1（獨立 workflow 外審）→L2（check_paths/check_headers/build_repo_index/tests）**；L3 留給 user。
4. **不停下等 user**：需 user 拍板的 → 採**安全可逆預設** + 寫進決策佇列，繼續。只有「不可逆 / 會破壞向後相容 / 無法預設」才硬停回報。
5. **regression 是紅線**：任何既有行為（既有型別驗證、既有 C↔C 關係、無 org 專案）被破壞 = 該 segment NO-GO、回退。
6. **保守**：動 LOCKED 能「保留鏡像 + 標權威見 registry」就不激進刪除；不確定標 TODO + 入佇列。

## 4. 執行鏈（依序，各段 checkpoint commit）

### Step 0 — reconcile F8 編號（預設已定，直接採用）
**採 D-074 authoring-stack 編號為 canonical**：F8 = Phase 1（ORG core ✅）/ Phase 2（gate+/status ✅）/ **Phase 3（create-org + iterate + relationship endpoint + migration + view/export，一個 D-074 收）** / 方向 B（W-language 文件語體卡，DEFERRED）。
→ **`BATCH4_RESUME_PHASE4-7_AUTONOMOUS.md` 的 Phase 4-7 編號作廢**：其 iterate/view/export 併入本 Phase 3；其「Phase 7 spec 對齊」歸 **Batch 5**（不在 F8）。把此 reconcile 記一句進 wake-up 報告。

### Step 1 — F8 Phase 3（依 `D074_DECISION_PACKAGE.md`）
1. 讀 `D074_DECISION_PACKAGE.md` 全文 + `D071_DECISION_PACKAGE.md` §6。
2. **採草案 §1 推薦設計為預設**：`00_n_組織創建協議`(mirror 00_l、issue-less) + `/create-org`(clone create-character、只寫 `11_organizations/`、無聲線卡) + ORG card 6 段 + create-relationship 容許 C↔ORG endpoint + 清道夫 opt-in 遷移；一個 D-074 收；分 **3a core / 3b endpoint / 3c migration**。
3. **§13 的 7 個 open questions**：**逐項採草案推薦答案當預設 + 全部寫進決策佇列**（型別段數 / 00_n issue-less / 單一 D-074 / endpoint 本批 / view-org 獨立 / ORG↔ORG / 方向 B 延後）。只有某題會造成不可逆破壞才硬停。
4. 依 3a→3b→3c 分步：各步 L0 → checkpoint commit → L1 獨立 workflow 外審 → L2 → 修。**不變量**：ORG-* 永無聲線卡、不進 /dialogue-write 為說話者；create-relationship 改動需 regression（C↔C 不可壞）。LOCKED 觸點（00_n / D-050 子裁決 2 +row / 00_l）以 **D-074** 背書。

### Step 2 — 全 repo 稽核（`BATCH4_POSTLAND_AUDIT.md`）
F8 Phase 3 在本分支 land 後，§0 前提（全 Phase 完成 + 樹乾淨）此時於本分支成立。把 `BATCH4_POSTLAND_AUDIT.md §5` 的 workflow 腳本傳給 Workflow 工具跑。收到 report：親自重跑 smoke test 的 FAIL 步驟；CRITICAL/MAJOR 安全可逆者自修 + commit；drift findings 全部**留給 Step 3**（它們是 Batch 5 的 worklist）。checkpoint commit 稽核報告。

### Step 3 — Batch 5 registry DRY 重構（`BATCH5_REGISTRY_DRY_REFACTOR.md`）
1. 驗 §1 前置（F8 land + 稽核跑完）✅。
2. **建 NEW_REQ_49**（POST_LOCK；consolidate NEW_REQ_47 + 48 + 稽核 D1/D2 drift）。
3. **拍 D-075**（spec-doc 策略採預設「保留鏡像 + drift-lint」雙軌；parser registry-derived）。
4. 跑 `BATCH5_REGISTRY_DRY_REFACTOR.md §4` workflow（inventory → refactor fan-out → verify 重跑稽核 D1/D2/D3 + parser regression）。
5. **regression 紅線**：parser registry-derived 後既有所有型別驗證行為不可變。checkpoint commit。

### Step 4 — 最終全稽核 + 技術債清掃（鏈尾 QA 閉環）
**目的**：讓整條過夜跑**結束在一輪完整自我 QA + 零技術債移交**，user 醒來不必清醒等 QA。

1. **最終全稽核**：F8 Phase 3 + Batch 5 全 land 後，**再跑一次完整 `BATCH4_POSTLAND_AUDIT.md §5` workflow（7 維全跑，非只 D1/D2/D3）**——確認重構動完 parser/spec/scripts 後，跨引用(D4)/帳本(D5)/向後相容(D6)/Phase 完整(D7)/ORG smoke 全部仍乾淨。再冒 CRITICAL/MAJOR：安全可逆者自修 + commit + 重跑該維；涉設計者入決策佇列。
2. **技術債清掃**：收齊整條過夜跑累積的所有債，整進 wake-up 報告「技術債 / backlog」段，不留隱性債：
   - (a) 程式 / 協議 / 文件裡留下的 TODO / INFERENCE / CONFLICT 標記（可跑 `/check-gaps` 視角）；
   - (b) 全部決策佇列項；
   - (c) 各 workflow 的 INFO / MINOR backlog；
   - (d) 已被取代的 doc（`BATCH4_RESUME_PHASE4-7_AUTONOMOUS` 的 Phase 編號已作廢、本 OVERNIGHT 計畫本身、其他 superseded 設計稿）——標 DEPRECATED 或記入清理清單；
   - (e) 刻意延後的殘餘（F8 方向 B W-language 文件語體卡 / Batch 5 skill-generic 殘餘 / NEW_REQ_49 尾巴）。
3. **帳本對齊**：把該關的 NEW_REQ 狀態（32/34/46/47/48/49）對齊實況、該記的記進 POST_LOCK + DECISIONS_LOG（D-074 / D-075）；**不動對話 B 預留段 D-056~062**。
4. checkpoint commit 最終稽核報告 + 帳本對齊。

## 5. 🌅 WAKE-UP 報告（park 等 L3）

全鏈跑完後產出 wake-up 報告（印對話 + 落 `_design/OVERNIGHT_WAKEUP_REPORT.md`），含：
1. **分支 + 每 segment commit hash + 一句話**（Step 0 reconcile / F8 3a/3b/3c / Step 2 稽核 / Batch 5 / Step 4 最終稽核）。
2. **自我 QA 結論（兩輪稽核閉環）**：Step 2 稽核摘要 + Batch 5 verify（drift_eliminated / regression_clean / l2_clean）+ **Step 4 最終全稽核 7 維結論（GO / GO-with-fixes / NO-GO）**。
3. **自動修了什麼**（含 Step 4 再冒並自修的項）。
4. **決策佇列**（最重要）：D-074 §13 七題各採的預設 + 待你確認；spec-doc 策略；任何其他預設。每項：問題 / 你採的預設 / 可選項。
5. **技術債 / backlog 清單**（Step 4 清掃結果）：剩餘 TODO / INFO / 延後殘餘（方向 B / skill-generic / NEW_REQ_49 尾巴）/ 待清理的 superseded doc / 待對齊帳本——全列出，不留隱性債。
6. **L3 + rule-4 簽字請求**：列所有 LOCKED 觸點 + 抽查指引（REVIEW_LOOP §2：開 CRITICAL/MAJOR diff、抽 1 PASS 檔複看、親跑 L2 + check_entity_type_consistency.py）。
7. **merge 指示**：簽字後 `feat/f8p3-audit-batch5` → `frontend-tools-a0f` + push。
8. **明確聲明：尚未 merge 進主分支，等 L3。**

## 6. Cross-ref
- `D074_DECISION_PACKAGE.md`（F8 Phase 3 設計 + §13 七題）/ `D071_DECISION_PACKAGE.md`（F8 總）
- `BATCH4_POSTLAND_AUDIT.md`（Step 2 稽核 workflow）/ `BATCH5_REGISTRY_DRY_REFACTOR.md`（Step 3 重構 workflow）
- `HANDOFF_F8_PHASE3_AND_REGISTRY_DRY.md`（背景 + 精確 location）/ `BATCH4_RESUME_PHASE4-7_AUTONOMOUS.md`（Phase 編號已 Step 0 作廢）
- `REVIEW_LOOP_PROTOCOL.md`（四層防線 / L3 不可代簽）/ `DECISIONS_LOG.md`（D-074 待落 / D-075 Batch 5）/ `POST_LOCK_PENDING.md`（NEW_REQ_47/48/49）
- 號段：D-074 = F8 Phase 3；**D-075+ = Batch 5**；D-056~062 對話 B 預留勿動；NEW_REQ 最高 48 → 49 = Batch 5。
