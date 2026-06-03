狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：Phase A.0F 平行對話完成後 frontend 工具 + audit follow-up 4 commit CODEX strict review — 11 feature land + L3 schema contract + D-046 #5 守則對齊 + Bug 1/2 fix + spec compliance disclosure
優先級：高

# CODEX_PHASE_A0F_REVIEW_STARTER — Phase A.0F 平行對話完成 review

# 0. 本檔用途

Phase A.0F master 平行對話流程：master 切 frontend-tools-a0f feature branch → A.0F.5 CopyCommandButton → A.0F.3/4 Scene Queue/Detail+facet → A.0F.11 Asset Panel → A.0F.10 🌟 L3 Export → A.0F.9 4 保留元件 → A.0F.6+7+8 Editor+LOCKED race+mtime conflict → A.0F 整體驗收 → master 內部用 2 個 Claude general-purpose subagent 自審找 P1/P2/Doc/Test gap → audit-P1/P2/doc/test 4 commit 修補 → **本輪 CODEX 獨立 strict review 驗證 11 feature land + audit follow-up + spec compliance + 無 regression**。

**前置條件：** Phase A.0F + audit follow-up 11 commits 全在 feature branch `frontend-tools-a0f`，user 已 merge 進 master 或可直接從 branch 讀。Branch HEAD：`e37cd3e` (audit-test)。完整 commit graph：

```
e37cd3e  Phase A.0F.audit-test: regression locks (D-046 #5 anchor + Bug 1 regression)
8afab68  Phase A.0F.audit-doc:  spec compliance disclosure (C1-C4)
32e15df  Phase A.0F.audit-P2:   cleanup (dark mode + dead code + .gitignore)
50348f7  Phase A.0F.audit-P1:   Bug 1 + Bug 2 fix
─── ↑ master 內部 Claude subagent audit 後修補 4 commit ↑ ───
499bc13  ← 9th master 第二段對話 PART3 handoff (accidentally landed; merge 時帶回 master)
a13ce5a  Phase A.0F 整體驗收 + integration test + user manual v0.2
4c0c36e  Phase A.0F.6+7+8: F3 Scene Editor + LOCKED race guard + mtime conflict
1ea2b7c  Phase A.0F.9:  4 保留元件 (Workspace Home + Glossary + theme)
1357247  Phase A.0F.10: 🌟 L3 Export panel + Prompt 生成器（核心）
7b72454  Phase A.0F.11: Asset Panel 完整版 — 7 subtype + 缺檔警示
25d919f  Phase A.0F.4:  F6 搜尋 + 篩選 facet (Scene Queue)
e4721e9  Phase A.0F.3:  F2 Scene Queue + Scene Detail (cockpit, read-only)
d6ec085  ← 9th master Wave 15 (accidentally landed; merge 時帶回 master)
989de19  Phase A.0F.5:  CopyCommandButton 通用元件
140af34  ← master ancestor (Wave 15 starters)
```

**review GO →** user 拍板 Phase A.0F FINAL；branch merge 進 master；進 Phase A.0G 或 Phase B

**review NEAR-GO →** master 拍板 hard-limit accept 或 inline patch 一輪

**review NO-GO →** 大幅 restructure / 額外 patch round

⚠ **Scope 嚴格限定：本輪 verify A.0F 11 commits + audit-P1/P2/doc/test 4 commits ONLY。**
⚠ **不重審：** 9th master 第二段對話的 d6ec085 / 499bc13（屬另一軸）；既有 Phase A/B/C SKILL.md / spec / D-001~D-054 拍板。
⚠ **教訓沿用 (Phase A.0F 內化)：**
1. Sandbox virtiofs cache stale — Read tool 可能看到陳舊內容；reliable read 用 `git show HEAD:<path>` 或 `git cat-file -p` 從 git object store
2. Cowork Write/Edit tool 可能截斷 multi-byte CJK 寫入 — 長 CJK 檔用 Python script via bash write_bytes
3. sandbox 無權 unlink `.git/HEAD.lock` 與 git index tmp_obj — workaround 是 `mv` 命名
4. CC-07 校正：L3 Export 必須無 rerun_qa / include_deleted 預設 false / 約束含禁 phase_log
5. D-046 #5 / C-16 / O-03：LOCKED 降級引導**只**指示改 frontmatter 一行；降級理由/日期/人**全進** 09_e，**不**進 frontmatter

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「Phase A.0F 平行對話完成後 frontend 工具 + audit follow-up 4 commit CODEX strict review」— 對 frontend-tools-a0f branch 上 11 個 Phase A.0F commit 跑「spec compliance + D-NNN 拍板內化 + L3 schema contract + code quality + bug hunt + test coverage」全方位 strict review，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有產出在 feature branch `frontend-tools-a0f`（HEAD: e37cd3e）。請 checkout 此 branch 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / code / starter / protocol 修補
- 對應傳統：同 Round 1-4 / Wave 13 review 模式 + 加碼「審 master 自己 spawn 的 Claude subagent audit 是否漏抓 critical」
- 對應前置：Phase A.0F + audit follow-up 共 11 commits 已 push（user 在 host 端 `git checkout frontend-tools-a0f` 即可看）

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；finding 寫進 review report）
- ✗ 不跑真實 frontend server（沙箱可能不能 pip install fastapi；可選跑 Stage A AST check）
- ✗ 不重審 D-001~D-054 拍板結論
- ✗ 不重審 9th master 第二段對話 commit (d6ec085 Wave 15 / 499bc13 PART3 handoff)
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec
- ✗ 不下新 D-NNN 拍板
- ✗ 不開 Phase A.0F patch round
- ✓ 可跑技術驗證命令（node --check / node tests/*.test.mjs / python AST check / git diff / grep）
- ✓ 可建本 review report 1 個檔（_design/CODEX_PHASE_A0F_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定 — Phase A.0F 11 commits ONLY）：**

### A.0F 主進度 7 個 commit（外加 1 audit verifier）

| # | commit | 主要產出 | 對齊 spec |
|---|---|---|---|
| 1 | `989de19` | CopyCommandButton.js (433 行) + delegated handler + 10 unit test | UX_SPEC §11.6 + D-029 (α) |
| 2 | `e4721e9` | SceneQueue.js (274 行) + SceneDetail.js (477 行) + /api/scenes endpoint | UX_SPEC §11.2 + D-035 |
| 3 | `25d919f` | SceneQueue.js v2 (615 行) — F6 facet 6 維 + fuzzy search + localStorage | UX_SPEC §11.4 + D-027 |
| 4 | `7b72454` | Asset Panel 完整版 — 7 subtype 卡 + 缺檔警示 | UX_SPEC §11.1.6a + D-044 / D-045 + UPS-UX-70 |
| 5 | `1357247` | 🌟 ExportPanel.js (489 行) + promptAssembler.js (269 行) + 28 schema unit test | L3_EXPORT_PROMPT_SCHEMA v0.2 + CC-07 + ARCH §4.2a + D-038 |
| 6 | `1ea2b7c` | WorkspaceHome.js + Glossary.js + theme + glossary.json (40 詞) | UX_SPEC §11.9 |
| 7 | `4c0c36e` | SceneEditor.js (700 行) — F3 N 欄 + LOCKED race + mtime conflict | UX_SPEC §11.3 + §11.5 + §11.7 + D-040 + D-042 + D-046 #5 |
| 8 | `a13ce5a` | 整體驗收 — test_endpoints_smoke.py (Stage A AST inventory + Stage B TestClient) + user manual v0.2 | — |

### Audit follow-up 4 commit（master 內部 Claude subagent audit 後修補）

| # | commit | 修補項目 |
|---|---|---|
| 9 | `50348f7` | audit-P1: Bug 1 (promptAssembler completion filter SKIP marker) + Bug 2 (ExportPanel input 失焦 focus restore) |
| 10 | `32e15df` | audit-P2: Bug 3 (components.css #2563eb → var) + dead code 3 條 + .gitignore |
| 11 | `8afab68` | audit-doc: C1-C4 user manual 對齊 (SceneQueue facet 對照表 + SceneDetail MVP 標 + Asset Panel 分母 single source + Glossary 13 vs 40 註明) + v0.2 → v0.3 |
| 12 | `e37cd3e` | audit-test: regression locks — prompt_assembler.test.mjs +5 (Bug 1 markdown 空行) + sceneeditor_guide.test.mjs 新檔 18 test (D-046 #5 anchor lock) |

### 對齊 spec 清單

依優先級 read：
1. `_design/UX_SPEC.md` §11.1-§11.9（11 feature spec — 對應每個 commit 的主要 frontend 邏輯）
2. `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 §1.1-§1.5（promptAssembler 嚴格 contract — 5 區塊 + YAML schema + CC-07 三條）
3. `_design/ARCHITECTURE.md` §4.2a（L3 Export A1 prompt 生成器架構）+ §13.2（8 endpoint Contract C）
4. `_design/DECISIONS_LOG.md` D-027 / D-028 / D-029 (α) / D-035 / D-037 / D-038 / D-040 / D-041 / D-042 / D-044 / D-045 / D-046 #5（14 拍板內化）+ CC-07
5. `_design/SPEC.md` §5.2 canonical schema + §16 文件狀態機（D-046 #5 守則來源）

### 主要檔（read 用 `git show frontend-tools-a0f:<path>` 或先 `git checkout frontend-tools-a0f`）

**backend：**
- `_tools/frontend/server.py` (832 行；9 endpoint — 8 Contract C + 1 自加 /api/scenes)

**frontend code（13 JS）：**
- `_tools/frontend/static/js/api.js` (147)
- `_tools/frontend/static/js/state.js` (98)
- `_tools/frontend/static/js/router.js` (~220 after audit-P2 cleanup)
- `_tools/frontend/static/js/main.js` (80)
- `_tools/frontend/static/js/components/CopyCommandButton.js` (433)
- `_tools/frontend/static/js/components/ProjectDashboard.js` (~520 after audit-doc)
- `_tools/frontend/static/js/components/promptAssembler.js` (~280 after audit-P1)
- `_tools/frontend/static/js/pages/SceneQueue.js` (615)
- `_tools/frontend/static/js/pages/SceneDetail.js` (477)
- `_tools/frontend/static/js/pages/SceneEditor.js` (~700 after audit-P2)
- `_tools/frontend/static/js/pages/ExportPanel.js` (~510 after audit-P1)
- `_tools/frontend/static/js/pages/WorkspaceHome.js` (104)
- `_tools/frontend/static/js/pages/Glossary.js` (124)

**CSS + assets：**
- `_tools/frontend/static/css/components.css` (~990)
- `_tools/frontend/static/assets/glossary.json` (40 terms)

**test：**
- `_tools/frontend/tests/copy_command_button.test.mjs` (10 PASS)
- `_tools/frontend/tests/prompt_assembler.test.mjs` (33 PASS — 28 + 5 Bug 1 regression)
- `_tools/frontend/tests/sceneeditor_guide.test.mjs` (18 PASS — D-046 #5 anchor lock)
- `_tools/frontend/tests/test_endpoints_smoke.py` (Stage A 2 PASS + Stage B 11 — Stage B 需 fastapi/httpx)

**user manual：**
- `_user_manual/05_frontend_tools.md` v0.3 (430 行)

---

## Review 任務 — 7 axis（嚴格）

### Axis 1 — Spec compliance per feature

對 UX_SPEC §11.1-§11.9 11 段，每段 list：
- Mapping commit
- 真實落地 / 部分 placeholder / 全部 placeholder / 完全遺漏
- 給 file:line 證據

特別查：
- §11.2.4 Required Context 6 子分區（SceneDetail.js）— master 自評 v0.2 寫「FINAL」，audit-doc v0.3 改 MVP；CODEX 看實際 code 是否真 placeholder 還是部分實作
- §11.3.5 行級 details pane / §11.3.6 Required Context 抽屜 — SceneEditor.js 標記未落地；確認沒有殘料 stub
- §11.4.3 facet 7 維 — 實作 6 維中只 Chapter / Pipeline State 1:1 對齊；其他 5 維 [BLOCKED]；audit-doc 已加對照表 — CODEX 驗對照表的「[BLOCKED]」說法是否誠實

### Axis 2 — D-NNN 拍板內化驗證

逐條對下列拍板，引 file:line 證據 + spec 句子：
- D-027 qa_type 可擴充（SceneQueue facet 留待擴）
- D-029 (α) 完全分離（前端不 spawn / exec / 執行 agent；grep `subprocess|spawn|exec\(|popen|os.system` server.py）
- D-035 Scene Detail read-only / Scene Editor 編輯雙頁
- D-038 L3 Export A1 prompt 流程
- D-040 Save flow LOCKED race guard 5 步
- D-042 base_dialogue + iteration_note 欄位
- D-044 7 subtype canonical
- D-045 Asset 不納入 narrative
- **D-046 #5 / C-16 / O-03 — 最關鍵**：buildDowngradeGuide (SceneEditor.js) + renderLockedGate (SceneDetail.js) **真的只指示改一行 frontmatter** 且 **不擅自加** 降級理由/日期/人欄位？引導文字字串引用 + 對照 SPEC §5.2 canonical schema 確認三欄位真不在合法 schema 內 + 對照 sceneeditor_guide.test.mjs 18 anchor lock test 是否真鎖到位

### Axis 3 — L3 schema contract（promptAssembler.js）

對 L3_EXPORT_PROMPT_SCHEMA v0.2 §1.1-§1.5：
- 必填 5 區塊存在 + 順序
- YAML 元資料 10 必填 key (schema_version / project_id / repo_root / timestamp / scope / formats / include_deleted / output_paths / mode / contract_refs)
- **CC-07 三條**：(a) **無** rerun_qa 欄；(b) include_deleted 預設 false；(c) 約束含「不修改 phase_log」
- mode 鎖 "read_only"
- schema_version 鎖 "1.0"
- 33 unit test 對 schema contract 是否真實覆蓋
- **特別查 Bug 1 regression** — audit-P1 50348f7 修了 completion filter SKIP marker；CODEX 自跑 `node -e 'assembleExportPrompt(...)'` 看 prompt 完成回報區塊 markdown 空行結構是否真保留 + 5 個 regression test 是否真鎖到位

### Axis 4 — Backend 9 endpoint inventory

對 ARCH §13.2 8 Contract C + A.0F.3 自加 1 endpoint：
- server.py 真有全 9 endpoint
- 每個 endpoint 的 LOCKED / mtime / 409 / 404 / 422 path 是否完整實現
- /api/scenes endpoint docstring 是否明示「非 Contract C 鎖定，frontend adapter 自用」
- test_endpoints_smoke.py Stage A AST inventory 是否真鎖 9 endpoint

### Axis 5 — Code quality + bug hunt

- innerHTML 灌字串是否都 routed 過 escapeHtml / escapeAttr（XSS）
- 任何 eval / new Function() / dangerouslySetInnerHTML 風險
- async 函數 catch 完整？Promise reject 不會 silent swallow？
- Event listener leak（addEventListener 沒對稱 remove）
- **Bug 2 (ExportPanel input 失焦) 修補完整性** — audit-P1 50348f7 加 save/restore focus；CODEX 看實際 rerender 函數是否真正確保留 selection / cursor position
- audit-P2 dead code 三條（router.js renderEditorPlaceholder / ExportPanel state import / SceneEditor bindKeyboard）真清掉
- audit-P2 components.css `.editor-column--trial` `#2563eb` → `var(--color-primary)` 真生效

### Axis 6 — Test coverage analysis

61 JS test + Stage A 2 Python test 是否覆蓋 critical path：
- 哪些 D-NNN 拍板有 test 鎖（防 regression）
- 哪些 critical path 沒 test cover（report gap）
- sceneeditor_guide.test.mjs 18 anchor lock 真覆蓋 D-046 #5 守則的所有關鍵字串？有沒有可繞過的 anchor？

### Axis 7 — master 自評 vs reality（**meta-review**）

master 內部 spawn 2 個 Claude general-purpose subagent 自審（Agent A spec + D-NNN; Agent B code quality + bug hunt）找到 P1 Bug 1/2 + P2 Bug 3 + dead code + doc concern + test gap。master 寫 4 commit 修補。

CODEX 任務：**驗證 master 自審 audit 是否漏抓更嚴重的 critical**：
- 找有沒有 Claude subagent audit **沒抓到**的真實 bug / spec drift
- 找有沒有 audit fix 本身有遺漏或副作用
- 對照 D-046 #5 / CC-07 / D-029 (α) 等最嚴格條款，做 strict cross-check

---

## 報告格式（產 _design/CODEX_PHASE_A0F_REVIEW_REPORT.md v0.1）

```
狀態：DRAFT
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：Phase A.0F 平行對話 + audit follow-up 共 11 commit CODEX strict review
優先級：高

# CODEX_PHASE_A0F_REVIEW_REPORT v0.1

## 0. 結論 — GO / NEAR-GO / NO-GO + 一句話

## 1. Axis 1 — Spec compliance per feature
[逐 §11.x 對齊 commit + 真實 / placeholder / 缺漏 分類；file:line evidence]

## 2. Axis 2 — D-NNN 拍板內化（14 條 + CC-07）
[逐條 PASS / Concern / Critical；file:line evidence + spec 句子引用]

## 3. Axis 3 — L3 schema contract（promptAssembler）
[5 區塊 / YAML / CC-07 三條 / 33 test 覆蓋率 / Bug 1 regression 真鎖]

## 4. Axis 4 — Backend 9 endpoint inventory
[9 endpoint 真有 + 各自 status code path 完整]

## 5. Axis 5 — Code quality + bug hunt
[新 bug findings / audit-P1/P2 fix 真生效驗證 / XSS / leak]

## 6. Axis 6 — Test coverage analysis
[critical path 覆蓋度 + sceneeditor_guide.test.mjs 18 anchor 強度評估]

## 7. Axis 7 — master 自評 audit 漏抓檢查（meta-review）
[Claude subagent 漏掉的 critical findings / fix 本身的副作用]

## 8. 給 master 的 recommendation
[GO / NEAR-GO 排序 follow-up；或 NO-GO 大幅 restructure 方案]

## 9. Test sweep evidence
[本 review 跑過的 node --check / unit test / git log / grep 結果摘要]
```

**嚴格紀律：**
- 敢標 Concern / Critical — 不要假和諧
- 每 finding 必含 file:line + spec 引用 + 具體 recommendation
- 不確定的標 `[需 master 拍板]` 不要強裝懂
- 不寫任何 frontend / spec 修補（純 review）
- Claude subagent audit 可能漏抓 — 你要做更嚴格的 cross-check

開始 review。
~~~

---

# 2. 後續流程

| 階段 | 動作 |
|---|---|
| **CODEX 開新對話** | user 把上面 ~~~ block 整段貼到新 CODEX 對話 |
| **CODEX 跑 review** | 預計 30-60 分鐘 — 讀 5 spec + 13 JS + server.py + 4 test + user manual + 跑技術驗證 |
| **CODEX 產 report** | `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 |
| **user push report** | git add report + commit + push to master |
| **master 判讀 verdict** | GO → merge frontend-tools-a0f 進 master / NEAR-GO → patch round / NO-GO → restructure |

# 3. Cross-ref

- `_design/UX_SPEC.md` v0.4 §11 (11 feature spec)
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2
- `_design/ARCHITECTURE.md` §4.2a + §13.2
- `_design/DECISIONS_LOG.md` D-027/028/029/035/037/038/040/041/042/044/045/046 + CC-07
- `_design/SPEC.md` §5.2 + §16
- feature branch: `frontend-tools-a0f` (HEAD: e37cd3e)
- 既有先例 starter：`_design/CODEX_9TH_MASTER_WAVE13_REVIEW_STARTER.md` v0.1（格式範本）
