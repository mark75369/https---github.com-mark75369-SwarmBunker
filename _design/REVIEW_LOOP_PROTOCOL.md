狀態：DRAFT
版本：v0.2
歷史紀錄：v0.2（Batch 5 / NEW_REQ_49 / D-075 — L2 防線新增 `check_entity_type_consistency.py`：斷言 spec-doc / parser 殘留鏡像與 entity_type_registry core 一致，補上型別漂移強制後盾；§1 總表 L2 列 + landing record「L2 結果」欄改為三腳本；本檔 v0.1 → v0.2）
最後更新：2026-06-03
適用範圍：本 repo（工具開發 / _design / 協議檔修改）的審核迴圈治理協議
優先級：高

# REVIEW_LOOP_PROTOCOL — 審核迴圈協議（四層防線）

## §0 文件定位

本協議定義：對本 repo（工具本體、`_design/` spec、`00_protocol/` 協議、`scripts/`、`.claude/skills/`）做任何 Batch 修改時，必跑的四層審核迴圈。

- 適用對象：所有 master 輪、所有平行 Cowork、所有 design agent / Codex / Claude Code session。
- 不適用：Instance repo 內的劇本生產（那走 `/qa` + `00_a` 既有流程）。本協議與 D-043 `/qa` pipeline 明確切割，避免混淆——`/qa` 管「劇本內容品質」，本協議管「工具開發流程治理」，兩者層級不同、不互相觸發。

背景：本 repo 早已在「實踐」這套四層防線（11th master cycle 的並行 read-only `Explore` 子代理外部審、`scripts/check_paths.py` / `check_headers.py` 自動檢查、master 在 Cowork 補加 cross-check 拍板），但從未「寫成規則」。一旦換手或平行開新 Cowork，防線層級就會漏跑（典型後果：Template 被污染、stale ref 擴散到約 11 檔才被抓到）。本協議把這套防線固化為「實作者照著就能跑」的權威流程。

## §1 四層防線總表（協議核心）

| 層 | 名稱 | 抓哪一類錯 | 由誰執行 | 機制 | PASS 判準 | FAIL 動作 |
|---|---|---|---|---|---|---|
| L0 | 執行（Execute） | —（產出階段） | 主 agent（當前 session） | 依任務做出修改，產出「預計改檔清單 + 改後摘要」（AGENTS.md `## 修改流程` 既有要求） | 改檔清單與實際 git diff 一致 | 補齊清單再進 L1 |
| L1 | 外部審（External Review） | **內容錯**：邏輯矛盾、跨檔不一致、stale ref、設計判斷錯、漏處理 edge case、誤判既有設計 | **獨立 agent**（非 L0 那個 session）；典型 = read-only `Explore` 子代理或另開 Cowork | 拿 L0 的 diff + 任務描述獨立複查；產出 finding list（嚴重度分級 CRITICAL / MAJOR / MINOR / INFO） | 0 個未處理 CRITICAL / MAJOR；或全 finding 有 cross-check 結論（採納 / 駁回 / deferred） | 退回 L0 修，或進 L3 由人裁 |
| L2 | 自動檢查（Automated Check） | **機械 / 執行錯**：路徑打錯、漏檔、檔名舊式、header 缺欄、格式雜訊（NUL byte / BOM）、git 狀態異常、**entity 型別鏡像漂移**（spec-doc / parser 殘留鏡像與 entity_type_registry core 不一致） | 任何人 / CI，跑腳本即可（零判斷） | `check_paths.py` + `check_headers.py` + `check_entity_type_consistency.py` + `git status` + 改檔清點 | 三腳本 exit code 0（無 ERROR）；git status 無非預期檔；清點數 = 改檔清單數 | exit ≠ 0 → 必修到 0 才放行；不可「WARN 先放著」除非 L3 明示 |
| L3 | 人工確認（Human Sign-off） | **判斷**：finding 採不採、方案選哪個、LOCKED 是否該動、Batch 是否可收 | **人類 master**（不可由 agent 代簽） | 真的抽查（見 §2 抽查規則）+ 對 L1 finding 做採納 / 駁回 / deferred + 對 decisionNeeded 拍板 | master 明示「本 Batch 收」+ 抽查至少命中 §2 規定樣本 | 未抽查或抽查不合格 → Batch 不得標 completed |

關鍵原則（協議正文）：

- **L1 與 L0 必須是不同 agent context。** 同一 session 自審＝沒審（會帶入相同盲點）。這是 repo 既有實踐（Explore 子代理 / 另開 Cowork）的明文化。
- **L2 零判斷。** 腳本只報事實，severity 由腳本定；人不在 L2 做「這個 WARN 沒關係」的決定——那是 L3 的事。
- **L1 抓內容、L2 抓機械，兩者不可互相替代。** 自動檢查永遠抓不到「設計判斷錯」；外部審不該浪費在「路徑有沒有打錯」（那交給腳本）。

## §2 「人工關卡只有真的抽查才有效」

> **L3 簽字的價值 100% 來自抽查的真實性。** 一個只會說「看起來沒問題、通過」的人工關卡，等於沒有關卡——它只是在 L1 / L2 的結論上蓋橡皮圖章，把責任洗白卻不增加任何防護。rubber-stamp sign-off 比沒有 L3 更危險，因為它製造「已被人審過」的假安全感。

抽查最低要求（可檢核清單）：

1. **至少實際打開讀過** L1 finding 中標 CRITICAL / MAJOR 的對應 diff 段落，不是只讀 L1 的摘要。
2. **至少抽 1 個 L1 判「無問題 / PASS」的檔親自複看**——防 L1 漏報（false-negative 比 false-positive 危險）。
3. **至少復跑一次 L2 腳本親眼看 exit code**——不接受「L0 說跑過了」的轉述。
4. 抽查結果（抽了哪幾項、命中什麼）要記進 Batch landing record（見 §3），不可只寫「已抽查通過」。

對齊既有事實：過往 audit 中 master 補加的 cross-check 曾駁回 6 條 raw finding（含 1 條 grep false-positive），正是 L3 抽查抓到 L1 過報的真實案例。L3 抽查不是形式，它真的會改變結論。

## §3 套用到每個 Batch 的生命週期

把四層綁進 repo 既有的「Batch」工作單位。協議定義 Batch 五狀態機：

```
DRAFT_CHANGE → EXTERNAL_REVIEWED → AUTO_CHECKED → HUMAN_SIGNED → LANDED
   (L0)            (L1)                (L2)           (L3)         (commit)
```

規則：

- **狀態不可跳。** 一個 Batch 必須依序通過 L0 → L1 → L2 → L3 才能 commit。允許 L1 ↔ L0 回圈（審出問題退回修，重審）。
- **L2 在 L1 之後、L3 之前。** 理由：L1 改完內容後檔可能動到路徑 / header，L2 要對「L1 修正後的最終 diff」跑，否則白跑。
- **每個 Batch 一條 landing record**，欄位如下：

| 欄位 | 內容 |
|---|---|
| Batch ID / 性質 | Batch 編號與一句話性質 |
| 改檔清單 | L0 產出，L2 清點對照 |
| L1 reviewer | 哪個 agent context（子代理 runID / 另開 Cowork）+ finding 採納統計（N 採 / N 駁 / N deferred） |
| L2 結果 | 三腳本（check_paths / check_headers / check_entity_type_consistency）exit code + git status 摘要 |
| L3 抽查紀錄 | 抽了哪幾項、命中什麼（§2 第 4 點） |
| commit hash | LANDED 後由 user git log 自查 |

### §3.1 規模豁免（避免協議淪為形式）

單檔 typo / header 補欄這類「純機械、零內容判斷」的 micro-batch，可將 **L1 降級**為「L0 自述 + L2 腳本」，**但 L3 抽查與 landing record 仍必跑**。

豁免條件寫死（不可主觀，防濫用）——必須同時滿足：

1. 改動不涉及任何設計判斷（不改邏輯、不改流程、不改判準）。
2. 不觸 LOCKED 檔、不觸 `00_protocol/`、不觸 registry template。
3. 改動可被 L2 腳本完全覆蓋驗證（純路徑 / header / 格式類）。

任一條不滿足 → 不得降級，必跑完整 L1。

## §4 與既有規則的接點（cross-ref，不重寫）

- L0 的「改前列清單 / 改後摘要」直接引 AGENTS.md `## 修改流程` + `## 修改後報告格式`，不重複定義。
- L1 finding 的錯誤呈現沿 ARCHITECTURE §3.3.1 / TASKS §1.5 四件套（What / Where / Why / 下一步）。
- 動 LOCKED / `00_protocol/` 的 Batch，L3 簽字前必須走 AGENTS.md 規則 4「先提變更理由與影響範圍」+ DECISIONS_LOG 開 D-NNN——本協議不放寬該門檻，只把它列為 L3 的前置條件。
- 與 `/qa` 的切割：`/qa` 是劇本「內容品質」pipeline（D-043 八報告），本協議是工具「開發流程」治理；兩者層級不同、不互相觸發。

## §5 邊界情況處理

- **平行 Cowork 互審：** A 開的 Batch 由 B session 當 L1 reviewer，天然滿足「不同 context」。協議建議優先用此模式（比子代理更省 token、且 B 有完整 repo 視野）。
- **L1 reviewer 也是 AI 的局限：** L1 是 AI 外部審，仍可能漏報；L3 的 §2 第 2 點抽查（抽 PASS 檔複看）正是兜底 L1 AI 漏報。
- **L2 腳本 scope 限制：** 現有 `check_paths.py` 只掃 ACTIVE_DIRS + README / AGENTS（不含 `CLAUDE.md` / `.claude/skills/`）。此為已知盲區，「scripts 涵蓋 CLAUDE.md 與 skills」列為 backlog（建議推 NEW_REQ，不在本協議實作）。
- **deferred finding：** L1 審出但 L3 判「本 Batch 不處理」的，必須進 `POST_LOCK_PENDING` / NEW_REQ backlog，不可悄悄丟棄。

## §6 版本與維護

- 本檔 DRAFT 起步；待一輪 master 實跑驗證後升 REVIEW。
- 新增防線層或改判準 → 升版 + 在 DECISIONS_LOG 留 D-NNN。
