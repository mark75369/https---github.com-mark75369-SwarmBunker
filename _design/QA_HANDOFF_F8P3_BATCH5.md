狀態：DEPRECATED
版本：v1.0（獨立 QA 交接包 — 給「另一個對話」冷啟動驗證 F8 Phase 3 + 稽核 + Batch 5 過夜長跑，回報後 master 做收尾）
最後更新：2026-06-03
適用範圍：接手「獨立 QA / L1 外審 + L3 抽查預演」的新對話 — 冷啟動可讀、純驗證、回報 GO/NO-GO
優先級：高

# QA HANDOFF — F8 Phase 3 → 稽核 → Batch 5（過夜長跑獨立驗證）

## 0. 你的任務（一句話）

你是**獨立 QA 對話**。前一個對話（過夜自主長跑）已把 **F8 Phase 3（ORG authoring stack）+ 全 repo 稽核 + Batch 5 registry DRY 重構** 全做完並 park 在分支 `feat/f8p3-audit-batch5`（**未 merge**）。**你的工作 = 不信任自報、親手抽查驗證、回報 GO / GO-with-fixes / NO-GO + 具體 finding**，讓 master 據此決定能否收尾（簽 L3 + merge）。

**你預設只讀不改**（這是 verify pass，不是 fix pass）。若發現必須修的問題，**列 finding 回報**，不要自己動手改 LOCKED / parser（除非 master 在此對話明示授權）。

## 1. ⚠️ 環境（先讀，有陷阱）

- **production repo = `D:\劇本開發工具\`**（git root）。**路徑陷阱：`開發`(發) vs `開発`(発) 是不同字**——用 `git -C "D:/劇本開發工具"`，Edit/Read 路徑務必用「發」。
- **目前分支應為 `feat/f8p3-audit-batch5`**（先 `git -C "D:/劇本開發工具" branch --show-current` 確認）。
- 跑 Python 前設 `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1`（Windows 中文）。
- `_sandbox/` 是拋棄式區，要建 fixture 在那裡，別污染 production 模板。

## 2. 權威報告（先讀這三份，再自己驗）

| 檔 | 內容 |
|---|---|
| `_design/OVERNIGHT_WAKEUP_REPORT.md` | **主入口**：8 commit + 兩輪 QA 結論 + 決策佇列 + 技術債 backlog + L3 簽字包 |
| `_design/BATCH4_POSTLAND_AUDIT_REPORT.md` | Step 2 稽核（F8 Phase 3 land 後 8 維）|
| `_design/FINAL_AUDIT_REPORT_F8P3_BATCH5.md` | Step 4 最終稽核（F8+Batch5 全 land 後 7 維 + falsification）|

設計依據：`D074_DECISION_PACKAGE.md`（F8 Phase 3 + §13 七題）、`BATCH5_REGISTRY_DRY_REFACTOR.md`（Batch 5）、`REVIEW_LOOP_PROTOCOL.md`（四層防線 / L3 抽查規則）、`DECISIONS_LOG.md` §6.25 D-074 + §6.26 D-075。

## 3. 本批改了什麼（驗證範圍）

8 個 commit（`git -C "D:/劇本開發工具" log --oneline f2c17ac..HEAD`）：

| commit | segment | LOCKED 觸點？|
|---|---|---|
| `30106f3` | F8 3a：00_n 協議 + /create-org + /iterate-org + 2 wrapper + ORG card 6 段 + D-050 列 + ARCH §3.4 + D-074 | ✅ 00_n（新 LOCKED 協議）/ D-050 表 / ARCH |
| `24d95f1` | F8 3b：00_l v0.3 + create-relationship v0.4 C↔ORG endpoint | ✅ 00_l |
| `a79d4dc` | F8 3c：check-gaps ORG awareness | SKILL-only |
| `5011b5b` | Step 2 稽核 + 自修 M1/M2/M3/m1-m7 | ARCH v1.8 / 00_l / 00_n / scripts |
| `aff324f` | NEW_REQ_49 + D-075 帳本 | 帳本 |
| `8cef601` | Batch 5：parser/scan/status registry-derived + spec-doc 雙軌 + drift-lint | ✅ parser / DATA_FORMAT_SPEC / SPEC §5.1b |
| `ffe2f05` | 技術債清掃：2 HANDOFF header + 06_data_structure 鏡像 + NEW_REQ 47/48 | doc |
| `6e8a2d3` | Step 4 最終稽核 + 自修（ORG skill 索引 + overclaim + pyc）+ wake-up 報告 | doc / 索引 |

**核心不變量（最該驗）：**
1. **ORG-* 永無聲線卡、不進 /dialogue-write 為說話者。**
2. **parser registry-derived 後，既有 11 型別驗證行為不可變（regression 紅線）。**
3. **create-relationship 既有 C↔C 行為不可變。**
4. **未 merge 進 `frontend-tools-a0f`；未動對話 B 預留 D-056~D-062。**

## 4. 🔬 QA 抽查清單（親手跑，逐項打勾）

### 4.1 L2 機械（必跑，看 exit code 與數字）
```
cd D:/劇本開發工具    # 注意「發」
# Windows: set PYTHONIOENCODING=utf-8 & set PYTHONUTF8=1   （或 PowerShell $env:）
python scripts/check_paths.py --baseline 227      # 期望：errors 227、[OK] within baseline、exit 0
python scripts/check_headers.py                   # 期望：errors 0、exit 0
python scripts/check_entity_type_consistency.py   # 期望：[OK] 無 drift、exit 0
python -m pytest scripts/tests/ -q                # 期望：43 passed
```
**任一不符 → NO-GO finding。**

### 4.2 Regression 紅線：parser DRY 是真的 registry-derived（決定性 falsification）
在 `_sandbox/` 建拋棄式測試，**親自確認 registry 是真權威、不是 hardcoded 鏡像**：
```python
# 設 PYTHONUTF8=1；cwd = D:/劇本開發工具
import sys; sys.path.insert(0,'scripts')
import parse_frontmatter as pf
# (a) 全 repo 實 entity ID 都 validate（regression）
from parse_frontmatter import build_repo_index, load_entity_type_registry, validate_entity_id
reg=load_entity_type_registry('.'); idx=build_repo_index('.')
ids={e for pm in idx.all_files_parsed for e in (getattr(pm,'yaml_data',{}) or {}).get('entities',[])}
print('fail:', [e for e in ids if validate_entity_id(e,reg)])   # 期望：[]（空）
# (b) ENTITY_ID_RE 接受 11 型別代表、拒非法
for ok in ['W-rules','W-language','W-style','V','C-x','R-a-b','P','CH-01','S-01-01','A-portrait-x-y','ORG-x']:
    assert pf.ENTITY_ID_RE.match(ok), ok
for bad in ['ORG','ORG-','CH-1','S-1-3']:
    assert not pf.ENTITY_ID_RE.match(bad), bad
print('parser pattern OK')
```
**falsification（最強證據）**：把 ORG 從一份 sandbox registry 拷貝刪掉、repoint `load_entity_type_registry` 到該 sandbox root，確認 `ENTITY_ID_RE.match('ORG-x')` 變 `None`（型別清單真隨 registry 變動）。若刪了 ORG 還能 match → parser 仍硬編碼 = NO-GO。
（前一對話宣稱此測 PASS；**請獨立複跑**。完整步驟見 `FINAL_AUDIT_REPORT_F8P3_BATCH5.md` §3。）

### 4.3 不變量：ORG 無聲線卡 / 不說話
```
# 應 0 命中「create-org / iterate-org 寫 03_characters」或「ORG 進 dialogue speaker」
grep -rn "03_characters" .claude/skills/create-org/ .claude/skills/iterate-org/    # 應只在「不寫」清單出現
```
人工讀 `00_protocol/00_n_組織創建協議.md` §1 核心不變量 + §8 禁止事項、`create-org/SKILL.md` 邊界段，確認：不建聲線卡、不寫 03_characters/、不進 /dialogue-write、限寫 `11_organizations/`。

### 4.4 C↔ORG endpoint 正確性（00_l v0.3 + create-relationship v0.4）
讀 `00_protocol/00_l_關係創建協議.md` §2.2 + `create-relationship/SKILL.md`：
- 容許 C↔C 與 C↔ORG，**禁 ORG↔ORG**（至多一端 ORG）。
- ORG 端**跳過聲線卡關係段**（ORG 無聲線卡）；04_a/04_b 照寫。
- **C↔C 路徑零變**：`git diff 30106f3~1 -- .claude/skills/create-relationship/SKILL.md` 看是否只「新增 ORG 分支」、未改 C↔C 既有邏輯。

### 4.5 LOCKED 治理（最高優先 — REVIEW_LOOP §2）
```
git -C "D:/劇本開發工具" diff f2c17ac HEAD -- _design/ARCHITECTURE.md _design/SPEC.md _design/DATA_FORMAT_SPEC.md
```
- **ARCH**：header 已 v1.8、§3.4 內容（加 /create-org→00_n + /iterate-* 6 個含 ORG）與 header 變動摘要**一致**（Step 2 修的 M1：不能再有「§3.4 不動」卻改了內容的矛盾）。
- **SPEC §5.1b / DATA_FORMAT_SPEC §7.x**：spec-doc 雙軌只**補** W-style+ORG（7/8→11）+ 標「鏡像；權威見 registry」marker，**無列舉刪除、無 `schema_version` bump**。若有刪除或 bump → finding。
- 每個 LOCKED 觸點都該能對應到 D-074 或 D-075 背書（DECISIONS_LOG §6.25 / §6.26）。

### 4.6 帳本三方對齊（D5）
- `DECISIONS_LOG.md`：header v2.9、§6.25 D-074 + §6.26 D-075 齊全、§7 摘要行含兩者、號碼無撞號。
- **未動對話 B 預留 D-056~D-062**：`grep -n "D-05[6-9]\|D-06[0-2]" _design/DECISIONS_LOG.md` 確認本批沒新增/改寫這段。
- `POST_LOCK_PENDING.md`：header v0.37、NEW_REQ_32（Phase 3 RESOLVED via D-074）/ 47/48（RESOLVED via D-075）/ 49（PROCESSING）狀態與實況一致。

### 4.7 Skill discovery（最終稽核修的 MAJOR）
```
grep -rn "create-org" AGENTS.md CLAUDE.md _user_manual/skill_registry_full.md   # 應各命中（drift 已修）
```
確認 4 個 ORG skill 檔存在：`.claude/skills/{create-org,iterate-org,建立組織,迭代組織}/SKILL.md`。

### 4.8 git 衛生 + 未 merge
```
git -C "D:/劇本開發工具" status --short            # 期望：乾淨（空）
git -C "D:/劇本開發工具" ls-files "*.pyc"          # 期望：空
git -C "D:/劇本開發工具" branch --merged frontend-tools-a0f | grep f8p3   # 期望：無輸出（未 merge）
```

## 5. ✅ 已知 / 已接受項（**不要當新 finding 回報**）

這些是前一對話**刻意的決定或已記 backlog**，QA 時別重報為 bug：
1. **§13 七題 + D-075 五題的預設**已寫進 DRAFT 的 00_n/00_l schema —— 這是「採安全預設 + 入決策佇列等 user 拍」，不是擅自拍板。你可**評估預設是否合理**並回報意見，但別當成「未經授權的改動」。
2. **spec-doc REGISTRY-MIRROR marker 未落地**（lint 對 spec-doc 目前只 INFO，硬比對 0/3）→ 刻意 park 為 NEW_REQ_49 尾巴（parser 端強制是真的、11 型別全綠）。06_data_structure / status SKILL 的措辭已軟化、不再宣稱 lint 已守護 spec-doc。
3. **W-style/ORG 列舉殘餘**：`L3_EXPORT_PROMPT_SCHEMA`、`_user_manual/07_customization.md`、`IC:1311`、`UX_SPEC:2617`、`UPSTREAM_DOWNSTREAM_SPEC:5863` 仍是舊「7/8 種」列舉 → 已記 NEW_REQ_49 尾巴（pre-existing drift，非本批 regression）。
4. **server.py:458 OUTLINE 第三鏡像**不在 lint scope、**C-ORG 裸名 ID 碰撞**（需 C 與 ORG 同名 contrived 前提，非現行 bug）→ NEW_REQ_49 觀察項。
5. **3c views（view-world ORG compose / 獨立 view-org·export-org）+ 清道夫 R-* 遷移 + F8 方向 B** → 刻意 DEFERRED（決策佇列 / backlog）。
6. **check_paths 227 / check_headers 既有債**：227 是長期 baseline（多為舊式檔名歷史債）；check_headers 本批已從 2→0。

## 6. 你要回報什麼（回給 master 做收尾）

產出一段 QA 結論，含：
1. **總評**：GO / GO-with-fixes / NO-GO。
2. **§4 各項抽查結果**（實跑數字 + PASS/FAIL，特別是 4.1 L2 四腳本 + 4.2 falsification）。
3. **新 finding**（若有）：What / Where / Why / Evidence / 建議嚴重度——只報 §5 以外的真問題。
4. **決策佇列意見**（選答）：§13 七題 + D-075 五題的預設你覺得是否合理（尤其 Q1 6 段夠不夠 / Q2 issue-less / Q6 禁 ORG↔ORG / B3 SPEC §5.1b 是否該當純 doc-sync）。
5. **可否收尾**：若 GO，master 即可簽 L3 + 照 `OVERNIGHT_WAKEUP_REPORT.md` §7 merge；若有 blocker，列出 merge 前必修項。

## 7. 收尾條件（master 在你回報後執行）
- L3 真抽查簽字（REVIEW_LOOP §2）+ 決策佇列拍板。
- 建議**先拍 Q1/Q2/Q6 ratify 設計再 merge**（趁尚未拍板/下游未依賴時改判最省）。**更正：00_n/00_l 狀態維持 DRAFT**（全 repo 所有創建協議 00_e~00_l 狀態欄皆 DRAFT；「LOCKED-tier」= 四層防線審核紀律，非 `狀態：` 欄；不翻 LOCKED 狀態）。
- 簽字後：`feat/f8p3-audit-batch5` → `frontend-tools-a0f`（`--no-ff` merge）+ push。
- 🛑 **在 master 簽字前，本分支不得 merge 進主分支。**

## 8. Cross-ref
- `OVERNIGHT_WAKEUP_REPORT.md`（主報告 + 決策佇列 + L3 包）/ `BATCH4_POSTLAND_AUDIT_REPORT.md` / `FINAL_AUDIT_REPORT_F8P3_BATCH5.md`
- `REVIEW_LOOP_PROTOCOL.md`（四層防線 / L3 抽查規則 / L2 三腳本）
- `DECISIONS_LOG.md` §6.25 D-074 + §6.26 D-075 / `POST_LOCK_PENDING.md` NEW_REQ_32/47/48/49
