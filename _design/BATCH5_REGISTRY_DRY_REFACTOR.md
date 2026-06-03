狀態：DEPRECATED
版本：v1.0（Batch 5 — registry DRY 重構（NEW_REQ_49）workflow 交付文件；整合平行 F8 對話 handoff §5 + 全 repo 稽核 + 本線討論；2026-06-03）
最後更新：2026-06-03
適用範圍：接手「registry DRY 重構 / Batch 5」的新對話 — 冷啟動可讀、workflow 模式執行、自主長跑、停在 L3 gate
優先級：高

# BATCH5 — Registry DRY 重構（NEW_REQ_49）workflow 交付文件

## 0. 一句話

把「entity 型別清單」從**散落多處的硬編碼鏡像**收斂成**單一真相源 = `entity_type_registry`**，並加一支 drift-lint 讓未來「加一型別只改一處、漏改自動被抓」。本檔含可直接跑的 workflow 腳本 + 自主長跑守則。整合自：平行 F8 對話 `HANDOFF_F8_PHASE3_AND_REGISTRY_DRY.md §5`（精確 location）+ `BATCH4_POSTLAND_AUDIT.md`（drift findings 來源）+ 本線重構討論（Tier 成本階梯 / 高槓桿子集）。

## 1. ⚠️ 前置依賴與定序（CRITICAL — 不滿足不要啟動）

本重構**必須**在以下兩件都完成後才跑（解平行 handoff §8 Q2 定序題）：
1. **F8 全部 land**（ORG authoring stack 完成、ORG 已穩定進 registry）——不管採哪套 F8 phase 編號，重點是 registry 的 core 型別已定稿含 ORG。
2. **`BATCH4_POSTLAND_AUDIT` 已跑完**——它的 **D1（跨規格列舉一致性）+ D2（registry）+ D3（L2 機械）findings 就是本重構的完整 worklist + 實證理由**。沒有它，worklist 不完整。

> 若啟動時 F8 仍在進行 / 稽核未跑：**停下回報**，不要在移動標靶上重構。

平行協調備註：另有一條 master 對話用不同 phase 編號驅動 F8（見 `HANDOFF_F8_PHASE3_AND_REGISTRY_DRY.md §6`）。**那是 F8 自己要 reconcile 的事，與本 Batch 5 無關**——本重構只依賴「F8 結果已 land」，不依賴它的 phase 怎麼編。

## 2. Confirmed scope（整合兩線）

**根因**：型別清單硬編碼在多處、會 drift（Batch 4 已實證）。**高槓桿子集（做這 4 塊 + lint）：**

| # | 目標 | 精確 location（平行 handoff §5 提供） | 改法 | 對應 |
|---|---|---|---|---|
| 1 | **parser registry-derived** | `scripts/parse_frontmatter.py`：`ENTITY_ID_RE`（~line 108）+ `_entity_type_from_id`（~line 1635）= registry 硬編碼鏡像 | 改為從 `load_entity_type_registry()` 動態建構 id 驗證與型別判定；移除硬編碼鏡像 | NEW_REQ_47 |
| 2 | **spec-doc 去 drift** | `DATA_FORMAT_SPEC §7.6`(規範表)/§7.1/§7.2 sample、`SPEC §5.1b`、`_user_manual/工具完整統整報告書.md §6` 靜態列舉 core 型別（缺 W-style + ORG） | 改「以 registry 為準」指標寫法；必須保留列舉的標「（鏡像；權威見 entity_type_registry）」 | NEW_REQ_48 |
| 3 | **掃描範圍** | `check_paths.py` `ACTIVE_DIRS` / `check_headers.py` `TEMPLATE_PATTERNS`（寫死目錄清單） | 從 registry 各型別的 `target_dir` 推導 | （本線提出） |
| 4 | **/status** | `.claude/skills/status/SKILL.md` 型別清單 + weight | 改讀 registry，不寫死 | （本線提出） |
| 5 | **drift-lint（capstone）** | 新增 `scripts/check_entity_type_consistency.py` | 斷言「所有仍存在的列舉鏡像 == registry」；未來 drift CI 自動抓 → 把「漏改」從可能變成結構上不可能 | 整合兩線 |

**刻意不做（殘餘留未來可選）**：把每個 SKILL 內文邏輯全改 registry-generic（回報遞減）。NEW_REQ_49 完成後此殘餘可關單或續記。

## 3. 開工步驟

1. **驗 §1 前置**（F8 land + 稽核跑完）。不滿足 → 停、回報。
2. **建 NEW_REQ_49**（POST_LOCK；目前最高 = 48）：consolidate NEW_REQ_47（parser）+ NEW_REQ_48（spec-doc）+ 稽核 D1/D2 drift findings 為單一 entry。
3. **拍 D-075**（下一個乾淨號；D-074 = F8 Phase 3）：spec-doc 策略（純指標 vs 保留鏡像+lint 雙軌）+ parser registry-derived 拍板 + 影響範圍。動多份 LOCKED → AGENTS.md 規則 4 + 四層防線。
4. **跑 §4 workflow**（L0 + L1）→ L2 → **L3 master 簽字**後才 merge。

## 4. Workflow 腳本（直接丟給 Workflow 工具）

inventory（確認完整 worklist）→ refactor fan-out（每目標一 agent，檔互斥可平行）→ verify（重跑稽核 D1/D2/D3 + parser regression，確認 drift 消除且既有型別驗證不壞）→ 合成 L3 package。

```js
export const meta = {
  name: 'batch5-registry-dry-refactor',
  description: 'Registry DRY 重構：型別清單單一真相源化（parser/spec-doc/scan/status + drift-lint）。inventory → refactor fan-out → verify → L3 package',
  phases: [
    { title: 'Inventory', detail: '盤點所有型別硬編碼鏡像（合稽核 D1/D2 findings）→ 權威 worklist' },
    { title: 'Refactor', detail: '每目標一 agent 平行改 registry-derived/指標（檔互斥）+ 各自 regression' },
    { title: 'Verify', detail: '重跑稽核 D1/D2/D3 + parser regression：drift 消除 & 零回歸' },
    { title: 'Synthesize', detail: '合成 L3 簽字包' },
  ],
}

const REPO = 'D:/劇本開發工具'
const common = `production repo = ${REPO}，branch frontend-tools-a0f。用 \`git -C "${REPO}" ...\`、Read、Grep、Bash 自行查證。`

const TARGET_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    targets: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          id: { type: 'string' }, file: { type: 'string' }, location: { type: 'string' },
          current: { type: 'string' }, plan: { type: 'string' },
          kind: { type: 'string', enum: ['parser', 'spec-doc', 'scan-scope', 'status', 'lint-new', 'other'] },
        },
        required: ['id', 'file', 'location', 'current', 'plan', 'kind'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['targets', 'summary'],
}

const CHANGE_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    target_id: { type: 'string' }, status: { type: 'string', enum: ['DONE', 'BLOCKED', 'SKIPPED'] },
    files_changed: { type: 'array', items: { type: 'string' } },
    diff_summary: { type: 'string' }, self_l2: { type: 'string' },
    needs_user_decision: { type: 'string' },
  },
  required: ['target_id', 'status', 'files_changed', 'diff_summary', 'self_l2', 'needs_user_decision'],
}

const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    drift_eliminated: { type: 'boolean' }, regression_clean: { type: 'boolean' },
    l2_clean: { type: 'boolean' }, findings: { type: 'array', items: { type: 'string' } },
    detail: { type: 'string' },
  },
  required: ['drift_eliminated', 'regression_clean', 'l2_clean', 'findings', 'detail'],
}

// ── Inventory ──
phase('Inventory')
const inv = await agent(
  `${common}\n\n【Inventory】產出 entity 型別硬編碼鏡像的權威 worklist。來源：(1) 讀 _design/BATCH4_POSTLAND_AUDIT 的 D1/D2 findings（若已有報告檔則讀之）；(2) Read scripts/parse_frontmatter.py 的 ENTITY_ID_RE(~108) + _entity_type_from_id(~1635)；(3) Grep 全 repo 找其他列舉 core 型別處（DATA_FORMAT_SPEC §7.6/7.1/7.2、SPEC §5.1b、_user_manual/工具完整統整報告書.md §6、check_paths.py ACTIVE_DIRS、check_headers.py TEMPLATE_PATTERNS、status SKILL）。每個 target 標 file/location/current/plan/kind。回傳 schema。`,
  { label: 'inventory', phase: 'Inventory', schema: TARGET_SCHEMA }
)

// ── Refactor fan-out（每 target 一 agent；檔互斥不需 worktree 隔離）──
phase('Refactor')
const changes = await parallel(
  (inv.targets || []).map((t) => () =>
    agent(
      `${common}\n\n【Refactor target ${t.id}（${t.kind}）】只改這個 target、只動其檔（${t.file}），不要碰其他 target 的檔（避免平行衝突）。\nlocation：${t.location}\ncurrent：${t.current}\nplan：${t.plan}\n\n要求：parser/scan/status 類 → 改 registry-derived 並加/更新 regression（既有所有型別驗證行為不可變）；spec-doc 類 → 改指標或標「鏡像；權威見 entity_type_registry」；lint-new → 寫 scripts/check_entity_type_consistency.py 斷言鏡像==registry。做完自跑相關 L2（python script / 測試）寫進 self_l2。遇需 user 拍板的設計分叉填 needs_user_decision、用安全可逆預設先做、不硬幹。回傳 schema。`,
      { label: `refactor:${t.id}`, phase: 'Refactor', schema: CHANGE_SCHEMA }
    )
  )
)

// ── Verify（重跑稽核維度 + regression）──
phase('Verify')
const verify = await agent(
  `${common}\n\n【Verify】確認重構成效與零回歸：(1) 重跑 BATCH4_POSTLAND_AUDIT 的 D1（跨規格列舉一致性）+ D2（registry）+ D3（L2 機械）邏輯，確認型別 drift 已消除；(2) 跑 scripts/tests/ 全部 + 新的 check_entity_type_consistency.py，確認 exit 0；(3) 用既有各型別樣本確認 parser 驗證行為與重構前一致（regression）。Windows 設 PYTHONUTF8=1。回傳 schema。`,
  { label: 'verify', phase: 'Verify', schema: VERIFY_SCHEMA }
)

// ── Synthesize ──
phase('Synthesize')
const report = await agent(
  `${common}\n\n【合成 L3 package】依下列產出 markdown：(1) 一句話 GO/GO-with-fixes/NO-GO；(2) 改了哪些 target（changes）；(3) verify 結論（drift_eliminated / regression_clean / l2_clean）；(4) needs_user_decision 佇列；(5) L3 抽查指引（REVIEW_LOOP §2：開 LOCKED diff、抽 1 PASS 檔複看、親跑 L2 + check_entity_type_consistency.py）；(6) merge 指示（user 簽字後）。\n\nchanges：${JSON.stringify(changes.filter(Boolean))}\n\nverify：${JSON.stringify(verify)}`,
  { label: 'synthesize', phase: 'Synthesize' }
)

return { report, inventory: inv, changes: changes.filter(Boolean), verify }
```

## 5. 自主長跑守則 + Tier-4 / 四層防線（與 BATCH4_RESUME 同紀律）

- **這是 Tier-4**（動 parser 核心驗證路徑 + 多份 LOCKED spec）→ 走完整四層防線；workflow 跑 L0+L1，L2 跑腳本，**L3 master 真抽查簽字後才 merge**。
- **隔離分支** `feat/batch5-registry-dry` 從 F8+稽核都 land 後的 HEAD 開；**每完成一組 target 就 checkpoint commit**（具體 path，勿 `git add -A`）。
- **不可自行把 LOCKED 改動 merge 進 `frontend-tools-a0f`**（L3 gate；agent 不代簽）。可 push feature 分支供審。
- **regression 是紅線**：parser registry-derived 後，既有 W/V/C/R/P/CH/S/A/W-style/ORG 全部驗證行為**不可變**——任何 regression = NO-GO。
- 需 user 拍板的設計分叉（spec-doc 純指標 vs 保留鏡像）→ 用安全預設（保留鏡像 + lint）先做、列佇列等簽字。

## 6. 給 master 的開放問題

1. **spec-doc 策略**：純指標（移除列舉）vs 保留鏡像 + drift-lint 雙軌？（建議**後者**：契約類規格需要 inline 列舉可讀性，靠 lint 保證一致最穩。）
2. **drift-lint 是否納入本批**（建議納入——它把 drift 從「靠審查抓」變「結構上不可能」，是本重構的 capstone）。
3. **殘餘 skill-generic**（每個 SKILL 內文 registry-generic）本批做還是續記 NEW_REQ_49 尾巴？（建議續記，回報遞減）。
4. 啟動時若 F8/稽核未完 → 依 §1 停下，等定序。

## 7. Cross-ref
- `_design/HANDOFF_F8_PHASE3_AND_REGISTRY_DRY.md`（§5 精確 location 來源；§6 平行 F8 對撞——屬 F8 範圍非本批）
- `_design/BATCH4_POSTLAND_AUDIT.md`（drift findings 來源 = 本批 worklist；verify 重跑其 D1/D2/D3）
- `_design/REVIEW_LOOP_PROTOCOL.md`（四層防線 / L3 不可代簽）
- NEW_REQ_47（parser 鏡像）/ NEW_REQ_48（spec-doc drift）/ NEW_REQ_49（本批，consolidate；待建 entry）
- 本線討論：Tier 成本階梯（Tier-3 entity 型別貴 → 重構後降 Tier-1）/ 「registry 驅動降風險」段
