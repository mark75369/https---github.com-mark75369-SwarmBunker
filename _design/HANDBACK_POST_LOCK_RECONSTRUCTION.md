狀態：DRAFT
版本：v0.1（11th master 對話 A 開 — POST_LOCK_PENDING 結構缺口 handback 給 Claude Code / 對話 B 後續 cycle 重建）
最後更新：2026-06-01
適用範圍：交給 Claude Code（或對話 B 後續 cycle）重建 POST_LOCK_PENDING.md 兩處對話 B wrap-up 未完成的結構缺口：NEW_REQ_36-43 entry body 缺失 + §5「評估紀錄總表」section phantom；對話 A 已處理自身範圍（NEW_REQ_44/45 + NEW_REQ_35 截斷 + D-062 + errata），剩餘交此 handback
優先級：高

# HANDBACK — POST_LOCK_PENDING 結構缺口重建（交 Claude Code）

## 0. 背景

11th master 對話 A 在 frontend cycle 收尾驗證 `_design/POST_LOCK_PENDING.md` 時，發現對話 B（M4 follow-up）的 wrap-up **大面積未實際寫入 body**：v0.25 header 宣稱新增 NEW_REQ_25-43（19 entries）+ §5.20 + §5.21，但檔案 body 只有 NEW_REQ_25-35，且 NEW_REQ_35 結尾被截斷在 mid-word（`連動 NEW_REQ_34 F`）。

對話 A 已處理**屬自己 scope** 的部分（見 §4）。本檔 handback **對話 B ownership** 的兩個結構缺口給 Claude Code 重建。對話 A 不替對話 B 捏造其 finding 內容。

---

## 1. 缺口 A — NEW_REQ_36-43 entry body 缺失（8 entries）

### 1.1 現況

POST_LOCK_PENDING body 最後一個 entry 是 NEW_REQ_35（F11）。NEW_REQ_36-43 **完全沒有 entry body**，只在少數 cross-ref（如 NEW_REQ_37 entry 提到「NEW_REQ_38」）+ header 版本註記出現。

### 1.2 source material 齊全 — 直接從 M4 報告重建

對話 B 的 finding 原始內容**完整存在** `_design/M4_USER_TEST_REPORT.md` §3.12-§3.19。映射規則 `NEW_REQ_N = F(N-24)`（已驗證：NEW_REQ_27=F3 / NEW_REQ_35=F11）：

| 待建 entry | F# | M4 source | 主題 | D-NNN candidate（M4 標註）|
|---|---|---|---|---|
| NEW_REQ_36 | F12 | §3.12 | 聲線卡缺「Source Coverage / Downstream Hooks」固定尾段（output 層）| — |
| NEW_REQ_37 | F13 | §3.13 | `/create-character` 主動讀既有台詞 + 聲線卡加「既有劇本台詞聲線基準」段 | 連動 STYLE_ANCHOR W-style |
| NEW_REQ_38 | F14 | §3.14 | AGENTS.md / CLAUDE.md 開場 context budget 過大 | — |
| NEW_REQ_39 | F15 | §3.15 | `parse_frontmatter.py` 裸 `---` 誤判 YAML block（line 2892 bug）| — |
| NEW_REQ_40 | F16 | §3.16 | `/create-outline`→`/create-detailed-outline` 中間缺 DRAFT 原始細節保全層 | — |
| NEW_REQ_41 | F17 | §3.17 | `/create-outline` 缺「遊戲設計語言」/「關卡功能 table」結構化輸出 | D-060（pattern pack；合 F18）|
| NEW_REQ_42 | F18 | §3.18 | `/create-detailed-outline` 缺「開戰前→戰鬥→戰鬥後」場景結構 | D-060（pattern pack；合 F17）|
| NEW_REQ_43 | F19 | §3.19 | `/create-outline`/`/create-detailed-outline` 缺「個人劇情 vs 主線邊界」check | — |

### 1.3 重建指引

每個 entry 沿用 **既有 NEW_REQ_25-35 的 entry 格式**（POST_LOCK body 內現成範本）：標題行（`## NEW_REQ_N — <主題>（狀態；11th master 對話 B M4 follow-up F<n>；層）`）+ 欄位：**狀態 / 時點 / 提出者 / 需求背景 / 分類+嚴重度 / 提議方案 / 對既有 spec 的影響 / 處理時機 / Owner / Cross-ref**。內容從 M4 §3.12-§3.19 對應小節 + §4 Meta-pattern 分組（Wave-A1~A6）抽取。插入位置：POST_LOCK body NEW_REQ_45 之後（或依號序整理）。

---

## 2. 缺口 B — §5「評估紀錄總表」section 為 phantom

### 2.1 現況（比缺口 A 更根本）

POST_LOCK_PENDING **整個檔案 body 沒有任何 `# 5` / `## 5.x` section**。但多輪 header 版本註記宣稱新增了一連串 §5.x：

- v0.19 註記：「§5 評估總表 10 個 subsection」
- v0.22 註記：「restore §5.3-§5.12 + §5.13/§5.14/§5.15」
- v0.23 註記：「§5.16 first-run + §5.17」
- v0.24 註記：「§5.18 second-run + §5.19」
- v0.25 註記：「§5.20 對話 B 評估總表 + §5.21」

實際 body 只有 `# 0` / `# 1 新需求清單` / `# 2 後續更新區（保留）` 三個 top-level section。**§5.3-§5.21 全部不存在於 body**（僅 header 提及 + 散見 cross-ref 如「§5.8 確認」）。

### 2.2 這是跨多輪 master 的文件債

§5 phantom 不是對話 B 單獨造成 — 從 v0.19（10th master）就開始 header 宣稱 §5 而 body 無。對話 B 的 §5.20/§5.21 只是延續此 pattern。

### 2.3 Claude Code 需 user 拍板的兩條路

| 路 | 做法 | 適用 |
|---|---|---|
| **路 1 — 重建** | 依 header 註記 + 各輪 source（M4 報告 §4 / first-run + second-run audit memo / 各 NEW_REQ deferred 評估）實際補寫 `# 5 評估紀錄總表` section + §5.3-§5.21 subsection | 若 §5 的評估總表內容有現實查閱價值 |
| **路 2 — 正式宣告不重建** | 在 header 加一條 errata：「§5.x 為歷史虛擬編號；評估紀錄實際分散於各 NEW_REQ entry + AUDIT_2026Q2_REPORT + M4 報告；本檔不另建 §5 section」，並清掉散落的 §5.x cross-ref（改指實際位置）| 若 §5 內容已被各 entry + AUDIT + M4 覆蓋，重建屬冗餘 |

對話 A 評估傾向**路 2**（§5 內容大多已分散在各 NEW_REQ entry 與 AUDIT/M4，重建恐製造維護負擔），但屬對話 B / user 拍板範圍，不替決。

---

## 3. 對話 A 已處理（不要重做）

| 項 | 狀態 |
|---|---|
| NEW_REQ_44 entry body（backend endpoint + 3 schema）| ✅ 對話 A 已補入 body |
| NEW_REQ_45 entry body（scope-C reframe defer）| ✅ 對話 A 已補入 body |
| NEW_REQ_35 截斷殘句補完 + errata | ✅ 對話 A 已補（依 NEW_REQ_34=F10）|
| v0.26 header 不實「§5.22」陳述修正 | ✅ 對話 A 已改 |
| D-NNN 號 D-056 撞車 → 順延 D-062 | ✅ 對話 A 已起草 `_design/D062_DECISION_PACKAGE.md` |
| 6 檔 CRLF churn 排除 | ✅ 對話 A 已還原（未入 commit）|
| AUDIT_2026Q2_REPORT §9.5 errata | ✅ 對話 A 已補 3 條 |

---

## 4. Cross-ref

- `_design/POST_LOCK_PENDING.md`（待重建檔；NEW_REQ_36-43 + §5 section）
- `_design/M4_USER_TEST_REPORT.md` v1.0 §3.12-§3.19（F12-F19 source）+ §4（Meta-pattern / Wave 分組；§5.20 重建來源）
- `_design/AUDIT_2026Q2_REPORT.md` §9.5（對話 A errata 3 條）
- `_design/D062_DECISION_PACKAGE.md` v0.1（D-062 拍板包；NEW_REQ_44 前置）
- 既有 NEW_REQ_25-35 entry（POST_LOCK body；重建格式範本）
