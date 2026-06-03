狀態：DEPRECATED
版本：v1.0（F8 Phase 3 + registry DRY 重構 冷啟動交接包；接手前一對話 context 將滿；2026-06-03）
最後更新：2026-06-03
適用範圍：接手「F8 Phase 3 實作」與「registry DRY 重構（NEW_REQ_49 / Batch 5）」的新對話 — 冷啟動可讀
優先級：高

# HANDOFF — F8 Phase 3 + registry DRY 重構

## 0. 一句話現況
`frontend-tools-a0f` 上 **Batch 4（F10 + D-073 + F8 Phase 1 + Phase 2）已全部 land + push**。剩兩條：**(A) F8 Phase 3**（ORG-* authoring stack；D-074 設計草案已寫好待拍板）+ **(B) registry DRY 重構**（NEW_REQ_49 / Batch 5；entity 型別清單單一真相源化）。另有平行的 **BATCH4_POSTLAND_AUDIT** 稽核對話在跑。

## 1. ⚠️ 環境（先讀）
- **production = `D:\劇本開發工具\`**（git root；remote `https://github.com/mark75369/Writing-tools.git`；branch `frontend-tools-a0f`）。`_sandbox\snapshot\` 是拋棄式副本不要當真倉庫。
- 路徑陷阱：`開發`(發) vs `開発`(発)；用 `git -C "D:/劇本開發工具"`。`scripts/__pycache__/*.pyc` 已 untrack + gitignore（Batch 4 hygiene）。
- **四層防線必跑**（動工具/_design/協議/LOCKED）：L0→L1 外審（獨立 agent）→L2（check_paths/check_headers/git）→L3 master 真抽查簽字。動 LOCKED/00_protocol → 必走 AGENTS.md 規則 4 + DECISIONS_LOG D-NNN。詳 `_design/REVIEW_LOOP_PROTOCOL.md`。
- L2 baseline：check_headers **2 ERROR**（2 份 HANDOFF 檔缺「優先級」欄，pre-existing）+ ~34 WARN（verbose 版本行慣例）；check_paths ~225 baseline。用 `python scripts/check_paths.py --changed-only --base <ref>` 比對只看自己引入的。Windows 設 `PYTHONUTF8=1`。

## 2. git 現況（2026-06-03）
```
739bc76 docs: BATCH4_POSTLAND_AUDIT（另一對話/master 開的稽核啟動檔；已 push）
0bd67fb feat(skills): F8 Phase 2（gate + /status ORG；D-071 後續；已 push）
2803345 merge: Batch 4 (F8/F10) into frontend-tools-a0f（已 push）
...（1d1d36a F8 Phase1 / 3fa3c63 hygiene / 275d9b3 D-073 / f766ba6 F10 / 36b8713 Batch2 merge）
```
- 本交接所附 `D074_DECISION_PACKAGE.md` + 本檔，隨此 commit 一起進 repo。
- 工作樹乾淨。merged 分支 `feat/batch4-entity` 已刪、worktree 已 remove。`feat/batch2-outline`(worktree D:/batch2-wt) / `feat/batch3-hygiene` 為他人 merged 殘留，未清。

## 3. 決策號 / NEW_REQ 號段（杜絕撞號）
- **已用**：D-067/068/069（Batch 2 大綱鏈）/ D-071（F8 ORG core）/ D-072（F10）/ D-073（registry 修復）。**D-074 = F8 Phase 3 預留**（見 D074 package）。
- **D-056~D-062 = 對話 B 預留段**（user 已拍板對話 B defunct，但本批一律未動其帳；釋放屬另一動作）。**D-070 = Batch 2 spare 未用**。
- 下一個乾淨決策號 = **D-075+**（Phase 3 之後）。
- NEW_REQ：最高已用 **48**。**NEW_REQ_49 = registry DRY 重構（Batch 5）**，被 BATCH4_POSTLAND_AUDIT §4/§6 引為「drift findings 去處」但**尚未在 POST_LOCK 建 entry**（避免與稽核對話撞，留給稽核 / Batch 5 owner 正式建）。

## 4. 條 A — F8 Phase 3（ORG-* authoring stack）
**現況**：設計草案 **`_design/D074_DECISION_PACKAGE.md` 已寫好**（待 master 拍板）。⚠ 該草案因 design panel `wf_ac0e3a40` 跑 1hr 只 1/3 proposal 完成 + API error + user 中斷，**非 panel 綜合、缺對抗評審**，是主對話手寫；**§13 open questions 請 master 逐項拍**。

**推薦設計（草案 §1）**：最小鏡像——`00_n_組織創建協議`(mirror 00_l、issue-less) + `/create-org`(clone create-character、只寫 `11_organizations/`、無聲線卡) + ORG card 6 段 + create-relationship 容許 C↔ORG endpoint + 清道夫 opt-in 遷移；**一個 D-074 收**；分 **3a core / 3b endpoint / 3c migration**。

**接手步驟**：
1. 讀 `D074_DECISION_PACKAGE.md` 全文 + `D071_DECISION_PACKAGE.md`（Phase 1 + §6 Phase 3 scope）。
2. 跟 master 拍 §13 的 7 個 open questions（型別段數 / 00_n issue-less / 單一 D-074 / endpoint 本批或延 / view-org 獨立 / ORG↔ORG / 方向 B 延後）。**建議重跑一個輕量 design panel 補對抗評審**（前次太重才空轉——縮 proposal 工作量、設逾時），或 master 直接拍。
3. 拍板後依 **3a→3b→3c** 分步、各步走四層防線 + QA（比照 D-071：L0→L1 獨立外審→L2→adversarial QA workflow→L3 簽）。LOCKED 觸點（00_n 新協議 / D-050 子裁決 2 +row / create-relationship 00_l）必 D-074 背書。
4. **不變量**：ORG-* 永無聲線卡、不進 /dialogue-write 為說話者。create-relationship 改動需 regression（既有 C↔C 不可壞）。
- **方向 B**（W-language 文件語體卡，~5-8h）= F8 最後一塊，**仍 DEFERRED**；Phase 3 只在 ORG card §6 留 hint hook，不實作。F8 = 方向 A(Phase1-3)+B 全完才閉案。

## 5. 條 B — registry DRY 重構（NEW_REQ_49 / Batch 5）＝「另一個部分的重構需求」
**問題根因**：entity 型別清單目前**硬編碼在多處、會 drift**（Batch 4 已實證抓到）：
- **parser**（NEW_REQ_47）：`scripts/parse_frontmatter.py` `ENTITY_ID_RE`(line ~108) + `_entity_type_from_id`(line ~1635) 是 registry 的硬編碼鏡像；W-style 曾 drift（D-071 已 drive-by 補 W-style+ORG，但**仍硬編碼**、未根治）。
- **spec-doc**（NEW_REQ_48）：`DATA_FORMAT_SPEC §7.6`(規範表)/§7.1/§7.2 sample + `SPEC §5.1b` + `_user_manual/工具完整統整報告書.md §6` 靜態列舉 core 型別，缺 W-style + ORG（沿 D-055「0 LOCKED spec supersede」先例未同步）。
- **+ BATCH4_POSTLAND_AUDIT** 跑出的 D1（跨規格列舉一致性）drift findings 全部餵這裡。

**重構目標**：讓 entity 型別清單**單一真相源 = `entity_type_registry`**；parser 改為從 `load_entity_type_registry()` 動態建構（移除 ENTITY_ID_RE/_entity_type_from_id 硬編碼）；spec-doc 端改為「以 registry 為準」指標或同步機制。**消除「每加一型別要改 N 處」的 drift 源頭。**

**接手步驟**：
1. **先等 BATCH4_POSTLAND_AUDIT 跑完**（見 §6）——它的 D1/D2 findings 是本重構的完整清單 + 實證理由。
2. 在 POST_LOCK 正式開 **NEW_REQ_49**（若稽核對話未開），consolidate NEW_REQ_47 + NEW_REQ_48 + 稽核 drift findings。
3. 設計：parser registry-derived（含 regression test 確保現有行為不變）；spec-doc sync 策略（doc-only partial-supersede 補列 vs registry-pointer）。屬 **Batch 5**、可能多檔 LOCKED → 設計拍板（D-075+）+ 四層防線。
4. 風險：動 parser 核心驗證路徑 + 多份 LOCKED spec；務必 regression（既有所有型別驗證不可壞）。

## 6. 平行線 — ⚠️ 有另一條 master 對話也在驅動 F8（須先協調！）
**2026-06-03 偵測到平行對話在同一 branch 上 commit 了兩份 F8 文件（author 同為 `Phase A.0F patch master`）：**
- `739bc76` `_design/BATCH4_POSTLAND_AUDIT.md` — 全 repo 稽核啟動檔（見下）。
- `22e6f9a` `_design/BATCH4_RESUME_PHASE4-7_AUTONOMOUS.md` — F8 **Phase 3-7 + 自我 QA / 自主長跑** resume 計畫。

🚨 **Phase numbering 分歧（必先解）：** 本交接 + `D074_DECISION_PACKAGE.md` 用**本對話的編號**（Phase 1=ORG core ✅ / Phase 2=gate+/status ✅ / **Phase 3=create-org+iterate+relationship+migration+view/export**）。平行對話用**另一套**（Phase 3=view+export / 4=iterate / 5=跨引用 / 6=QA / 7=~10 LOCKED 規格對齊；見 BATCH4_POSTLAND_AUDIT §3 D7 + BATCH4_RESUME_PHASE4-7_AUTONOMOUS）。**兩套 F8 設計/計畫並存、會對撞或重工。接手第一件事 = 跟 master 確認「以哪一套 phasing 為準」、把 D074 草案與平行對話的 Phase4-7 計畫合併或擇一，再動工。**

### 6.1 BATCH4_POSTLAND_AUDIT（稽核線）
- `_design/BATCH4_POSTLAND_AUDIT.md`（commit 739bc76）是 master/另一對話開的**全 repo 工具層稽核啟動檔**，含可直接跑的 7 維 workflow 腳本（§5）。
- ⚠ 其 §0 觸發前提寫「**Batch 4 全部 Phase 完成**」才跑——但**F8 Phase 3 其實還沒做**（只到 Phase 2）。接手者須跟 master 釐清：稽核要等 Phase 3 做完才跑，還是先跑稽核現狀（F8 只到 Phase 2 + ORG core）。**兩條（Phase 3 實作 vs 稽核）+ 本重構有順序相依**，需 master 定序，避免重工/對撞。
- 稽核的 drift findings → NEW_REQ_49（= 條 B）。所以 **稽核 → NEW_REQ_49 → Batch 5 重構** 是一條線；F8 Phase 3 是另一條。

## 7. 關鍵檔 / 指標
- 設計：`D074_DECISION_PACKAGE.md`（Phase 3）/ `D071_DECISION_PACKAGE.md`（F8 總）/ `BATCH4_POSTLAND_AUDIT.md`（稽核 + NEW_REQ_49 線）。
- 帳本：`DECISIONS_LOG.md`（§6.23 D-071 / §6.24 Phase 2 / §6.12 D-050 / §6.16 D-053）/ `POST_LOCK_PENDING.md`（NEW_REQ_32/34/46/47/48）。
- 慣例：`REVIEW_LOOP_PROTOCOL.md`（四層防線）/ `M4_USER_TEST_REPORT.md §3.8`（F8 源）。
- 實作對象：`entity_type_registry.yaml`(+template) / `scripts/parse_frontmatter.py` / `.claude/skills/create-character`·`create-relationship`·`iterate-character`·`status` / `00_protocol/00_f`·`00_l`·`00_j`。
- 已過防線的 Batch 4 commits：見 §2。

## 8. 給 master 的開放問題（接手對話先解）
1. **F8 Phase 3 怎麼起手**：重跑輕量 design panel 補對抗評審，還是你直接拍 D074 §13？
2. **定序**：先做 F8 Phase 3 實作 → 再跑 BATCH4_POSTLAND_AUDIT → 再 Batch 5 重構？還是先跑稽核（現狀）→ 重構 → 再 Phase 3？（稽核 §0 假設 Phase 3 已完成，與現實不符，須定序。）
3. **NEW_REQ_49 由誰建**：稽核對話 vs Batch 5 owner vs 本線？
4. registry DRY 重構（條 B）範圍確認 = NEW_REQ_47 + NEW_REQ_48 + 稽核 drift？（本交接此假設；若「另一個部分的重構需求」另有所指請更正。）
