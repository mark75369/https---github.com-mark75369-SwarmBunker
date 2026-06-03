狀態：DEPRECATED
版本：v1.0（Batch 4（F8 ORG + F10）落地後「全 repo 一致性 + 回歸稽核」啟動文件；含可直接跑的 dynamic workflow 腳本；2026-06-03）
最後更新：2026-06-03
適用範圍：給 Batch 4 全 Phase 完成後、跑工具層大規模稽核的新對話 — 冷啟動可讀 + 直接觸發 workflow
優先級：高

# BATCH4_POSTLAND_AUDIT — Batch 4 落地後全 repo 稽核啟動文件

## 0. 用途與觸發時機

本檔給「Batch 4 收尾後跑一輪大規模工具層稽核」的新對話用。讀完即可直接用 §5 的 workflow 腳本觸發。

**務必在以下條件全部成立後才跑：**
- Batch 4 **全部 Phase 完成**（F8 不只 Phase 1 ORG 型別，還含 /create-org skill、view/export、iterate、跨引用、QA、~10 份 LOCKED 規格對齊；F10 已落地）。
- 所有平行分支（Batch 2 / Batch 4）**都已整合進 `frontend-tools-a0f`**。
- **主工作樹乾淨**（`git status` 無未提交檔）——半成品或 mid-flight 狀態下稽核沒意義。

## 1. ⚠️ 這不是 `/qa`

本 repo 有兩套互不觸發的 QA（見 REVIEW_LOOP_PROTOCOL §0）：
- `/qa`（D-043 八報告）= **劇本內容品質**（台詞），對象是 Instance repo 的台詞產出。**本次不跑這個。**
- 本稽核 = **工具開發流程治理**（REVIEW_LOOP 四層防線的放大版：全 repo 一致性 + 回歸 + 功能 smoke test）。

跑錯層會白做。本檔只做後者。

## 2. 為什麼 Batch 4 後要跑這輪

- F8 = 新增第一類 entity 型別（ORG），是所有批裡 **blast radius 最大**的改動（registry + parser + /status + ~10 LOCKED 規格 + 多 skill）。
- drift 已實際發生：Batch 4 自己開了 NEW_REQ_46（registry 損壞）/ 47（parser 硬編碼鏡像）/ 48（LOCKED spec 型別列舉 drift）。抓到 3 個，通常還有沒抓到的。
- 多對話平行 merge（B2 + B4）→ 各自單獨過、合在一起卻可能漂移的整合風險。
- 這類「語意走樣 / 跨規格漂移 / 舊資料」風險 **L2 腳本抓不到，只有系統性稽核能抓**。

## 3. 稽核維度（7 維 + 功能 smoke test）

| 維度 | 查什麼 | PASS 判準 |
|---|---|---|
| **D1 跨規格列舉一致性** | 每個列「合法 entity 型別」的地方（~10 LOCKED 規格 + /status + skills + check_paths/check_headers）是否全一致含 **W-style + ORG**（NEW_REQ_48 系統化版） | 無任何一處漏列/多列/型別清單彼此矛盾 |
| **D2 registry 完整性** | entity_type_registry(+template) parse 正常、id_pattern 無衝突（ORG 不誤撞 R/C 等）、KEY 全 repo 唯一、ORG 有 weight | registry 合法 + 無 pattern 重疊 |
| **D3 L2 機械** | check_paths / check_headers / build_repo_index / 全測試（scripts/tests/）通過；baseline delta 有解釋 | 腳本 exit 0 或 delta 可解釋；測試全綠 |
| **D4 跨引用完整** | skill 互引、view/export 對 ORG、/status 計數、無斷引（check-gaps 視角） | 無斷引、ORG 在該被引用處都被引用 |
| **D5 決策帳本完整** | D-067~074 一致、無撞號、**未碰對話 B 預留段 D-056~D-062**、DECISIONS_LOG ↔ POST_LOCK ↔ skill 三方對齊 | 號碼連續無衝突、三方紀錄一致 |
| **D6 向後相容 / opt-in** | 沒有 org 的專案行為是否零變動（/status 不因 ORG 多扣分、掃描不新報錯）；既有資料（如《蟲潮孤堡》清道夫 R-workaround）未被破壞 | 無 org 專案零感；舊資料不破 |
| **D7 F8 Phase 完整性** | F8 是否每個 Phase 都真做了（create-ORG / view / export / iterate / 跨引用 / QA / spec 對齊），有無 Phase 漏做或半做 | 無宣稱完成卻未落地的 Phase |
| **SMOKE ORG 端到端功能** | 在**拋棄式 scratch 區**建最小 ORG fixture，跑 parser + /status 計數邏輯，確認 ORG 被辨識+計入、且不破壞 non-org 專案 | 功能實跑通過（**看行為不看 agent 自報**，§7 無聲失敗教訓） |

## 4. 嚴重度與處置

- CRITICAL / MAJOR：阻擋；本輪修或開 NEW_REQ + 排 fix。
- MINOR：記錄；可併入後續。
- INFO：記 backlog。
- 每個 finding 必須經**對抗式 verify**（獨立 reviewer 試駁，無法確證為真就降為 NOT_A_BUG）才算數——對齊 REVIEW_LOOP §2「L1 過報會被 L3 抽查駁回」的精神。
- **所有 drift 類 finding 直接餵 NEW_REQ_49（registry DRY 重構 / Batch 5）** 當實證理由。

## 5. Workflow 腳本（直接丟給 Workflow 工具跑）

新對話確認 §0 條件成立後，把以下腳本傳給 `Workflow` 工具的 `script` 參數即可。維度 fan-out（find）→ 對抗式 verify → 合成報告。

```js
export const meta = {
  name: 'batch4-postland-audit',
  description: 'Batch 4 (F8 ORG + F10) 落地後全 repo 一致性 + 回歸稽核：7 維 fan-out → 對抗式 verify → 合成 + ORG 功能 smoke test',
  phases: [
    { title: 'Find', detail: '7 維度平行 finder + ORG 功能 smoke test' },
    { title: 'Verify', detail: '每個 finding 獨立對抗式複查（試駁）' },
    { title: 'Synthesize', detail: '去重 + 嚴重度分級 + 處置建議 + 餵 NEW_REQ_49' },
  ],
}

const REPO = 'D:/劇本開發工具'

const FINDING_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    dimension: { type: 'string' },
    verdict: { type: 'string', enum: ['CLEAN', 'ISSUES_FOUND'] },
    summary: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          severity: { type: 'string', enum: ['CRITICAL', 'MAJOR', 'MINOR', 'INFO'] },
          what: { type: 'string' }, where: { type: 'string' },
          why: { type: 'string' }, evidence: { type: 'string' }, suggestion: { type: 'string' },
        },
        required: ['severity', 'what', 'where', 'why', 'evidence', 'suggestion'],
      },
    },
  },
  required: ['dimension', 'verdict', 'summary', 'findings'],
}

const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    real: { type: 'boolean' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    reasoning: { type: 'string' },
    corrected_severity: { type: 'string', enum: ['CRITICAL', 'MAJOR', 'MINOR', 'INFO', 'NOT_A_BUG'] },
  },
  required: ['real', 'confidence', 'reasoning', 'corrected_severity'],
}

const SMOKE_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    passed: { type: 'boolean' },
    steps: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          step: { type: 'string' },
          result: { type: 'string', enum: ['PASS', 'FAIL', 'SKIP'] },
          detail: { type: 'string' },
        },
        required: ['step', 'result', 'detail'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['passed', 'steps', 'summary'],
}

const common = `production repo = ${REPO}，branch frontend-tools-a0f。用 \`git -C "${REPO}" ...\`、Read、Grep 自行查證；需要時用 Bash 跑 scripts。對抗式心態：主動找真實問題，每個 finding 附 What/Where/Why/Evidence/建議，只報能指出具體證據的問題、不湊數。`

const DIMENSIONS = [
  { key: 'D1-spec-enum', prompt: `${common}\n\n【D1 跨規格 entity 型別列舉一致性】檢查每個列「合法 entity 型別」的地方是否全一致含 W-style + ORG：~10 份 _design/ LOCKED 規格（UPSTREAM_DOWNSTREAM_SPEC / SPEC / DATA_FORMAT_SPEC / INTEGRATION_CONTRACTS / ARCHITECTURE / REQUIREMENTS_LOCK / L3_EXPORT_PROMPT_SCHEMA / UX_SPEC）、.claude/skills/status/SKILL.md、scripts/check_paths.py + check_headers.py、_user_manual/。找漏列 / 多列 / 彼此矛盾。回傳 schema。` },
  { key: 'D2-registry', prompt: `${common}\n\n【D2 registry 完整性】Read _design/registries/entity_type_registry.template.yaml 與 root entity_type_registry.yaml：(1) 兩者 parse 正常、無損壞（NEW_REQ_46 曾損壞）；(2) ORG 的 id_pattern 不與既有 pattern（C/R/CH/S/A 等）重疊或互相 shadow；(3) ORG 有 target_dir + weight；(4) KEY 全 repo 唯一性邏輯不被新型別破壞。回傳 schema。` },
  { key: 'D3-l2-mechanical', prompt: `${common}\n\n【D3 L2 機械】用 Bash 跑：python scripts/check_paths.py（記 error 數）、python scripts/check_headers.py、python -c 跑 build_repo_index('.')、跑 scripts/tests/ 下全部測試。對照基線（check_paths ~225、check_headers 既有 2 ERROR/34 WARN 為既有債）；任何 delta 必須能解釋為 Batch 4 預期變動，否則報 finding。Windows 子行程設 PYTHONIOENCODING=utf-8。回傳 schema。` },
  { key: 'D4-xref', prompt: `${common}\n\n【D4 跨引用完整】檢查 ORG 相關跨引用：/create-org / view / export / iterate skill 是否互引一致、view/export 是否處理 ORG、/status 是否計數 ORG、AGENTS.md/CLAUDE.md/skill_registry_full.md skill 清單是否含新 skill、有無斷引（仿 check-gaps 視角）。回傳 schema。` },
  { key: 'D5-ledger', prompt: `${common}\n\n【D5 決策帳本完整】Read _design/DECISIONS_LOG.md 尾段 + _design/POST_LOCK_PENDING.md：(1) Batch 2/4 用的 D-067~D-074 號碼連續、無撞號、無重複定義；(2) **完全未動對話 B 預留段 D-056~D-062**；(3) DECISIONS_LOG ↔ POST_LOCK 對應 NEW_REQ 狀態 ↔ 實際 skill/registry 落地 三方對齊（如 NEW_REQ_32/34/46/47/48 狀態與實況一致）。回傳 schema。` },
  { key: 'D6-backcompat', prompt: `${common}\n\n【D6 向後相容 / opt-in】檢查「沒有 org 的專案是否零感」：/status 完成度公式是否因加 ORG 而讓無 org 專案被多扣分（應 opt-in 不扣）；新目錄/型別是否讓 check_paths/check_headers 對無 org 專案新報錯；既有把組織當 R-workaround 的資料（如《蟲潮孤堡》清道夫）是否有非破壞遷移路徑、不會被當錯誤。回傳 schema。` },
  { key: 'D7-f8-phases', prompt: `${common}\n\n【D7 F8 Phase 完整性】對照 _design/BATCH4_POSTLAND_AUDIT.md §3 與 F8 設計（Phase 1 ORG 型別 / Phase 2 create-ORG skill+協議+issue / Phase 3 view+export / Phase 4 iterate / Phase 5 跨引用 / Phase 6 QA / Phase 7 ~10 LOCKED 規格對齊）。逐 Phase 查「是否真落地」vs「宣稱完成卻沒做/半做」。特別查 §7 無聲失敗：有沒有 commit message 說做了、實際檔案卻沒有對應內容。回傳 schema。` },
]

phase('Find')

// 7 維度：find → 對抗式 verify（pipeline，無 barrier）
const dimResults = await pipeline(
  DIMENSIONS,
  (d) => agent(d.prompt, { label: `find:${d.key}`, phase: 'Find', schema: FINDING_SCHEMA }),
  (review, d) => parallel(
    (review.findings || []).map((f) => () =>
      agent(
        `${common}\n\n【對抗式 verify】獨立複查下列 finding，試著駁倒它。預設若無法以具體證據確證為真，就回 real:false / corrected_severity:NOT_A_BUG。\n維度：${d.key}\n嚴重度：${f.severity}\nWhat：${f.what}\nWhere：${f.where}\nWhy：${f.why}\nEvidence：${f.evidence}`,
        { label: `verify:${d.key}`, phase: 'Verify', schema: VERDICT_SCHEMA }
      ).then((v) => ({ ...f, dimension: d.key, verdict: v }))
    )
  )
)

// ORG 端到端功能 smoke test（不靠靜態審查；在拋棄式 scratch 區實跑）
const smoke = await agent(
  `${common}\n\n【SMOKE：ORG 端到端功能】不要污染 production 模板。在拋棄式 scratch 區（如系統 temp 或 _sandbox 下臨時目錄）建最小 fixture：一個含合法 ORG-* frontmatter 的檔 + 一個 non-org 對照。用 scripts/parse_frontmatter.py / build_repo_index 與 /status 計數邏輯，實跑確認：(1) ORG-* 被 parser 辨識、id 驗證通過；(2) /status 邏輯把 ORG 計入（有 org 時）；(3) 無 org 的 fixture 行為零變動。回報每步 PASS/FAIL/detail。看實際行為，不採信「應該會動」的推測。回傳 schema。`,
  { label: 'smoke:ORG-lifecycle', phase: 'Find', schema: SMOKE_SCHEMA }
)

// 合成：去重 + 嚴重度分級 + 處置建議 + 餵 NEW_REQ_49
phase('Synthesize')
const all = dimResults.flat().filter(Boolean)
const confirmed = all.filter((x) => x.verdict && x.verdict.real && x.verdict.corrected_severity !== 'NOT_A_BUG')
const report = await agent(
  `${common}\n\n【合成稽核報告】以下是 7 維度經對抗式 verify 後確認為真的 findings（JSON）與 ORG 功能 smoke test 結果。請產出一份 markdown 稽核報告：(1) 一句話總評（GO / GO-with-fixes / NO-GO）；(2) 依嚴重度分組列 confirmed findings（去重）；(3) smoke test 結論；(4) 處置建議——哪些本輪修、哪些開 NEW_REQ、哪些 drift 類直接餵 NEW_REQ_49（registry DRY 重構 / Batch 5）；(5) 給 user 的 L3 抽查指引（依 REVIEW_LOOP §2）。\n\nconfirmed findings：${JSON.stringify(confirmed)}\n\nsmoke：${JSON.stringify(smoke)}`,
  { label: 'synthesize:audit-report', phase: 'Synthesize' }
)

return { report, confirmed, smoke, raw_finding_count: all.length, confirmed_count: confirmed.length }
```

## 6. 稽核後動作

- 主對話收到 workflow 回傳的 `report` 後，**親自復核 confirmed findings**（§7 無聲失敗：別只信 agent 合成）——尤其 smoke test 的 FAIL 步驟要親手重跑一次。
- CRITICAL/MAJOR → 本輪修（深度抗審）或開 NEW_REQ 排程。
- drift 類 finding → 全部 cross-ref 進 **NEW_REQ_49（registry DRY 重構 / Batch 5）**，當實證理由。
- 稽核結論本身走 **L3：user 真抽查簽字**（REVIEW_LOOP §2）後才算這輪收。

## 7. Cross-ref

- `_design/REVIEW_LOOP_PROTOCOL.md`（四層防線；§0 兩種 QA 切割）
- `_design/HANDOFF_BATCH2_BATCH4_PARALLEL.md`（B2/B4 交接 + D-NNN 預留 + 碰撞 map）
- NEW_REQ_46/47/48（Batch 4 期間 drift 證據）/ NEW_REQ_49（registry DRY 重構，本稽核 findings 的去處）
- `_design/M4_USER_TEST_REPORT.md` §3.8（F8 finding 源）
