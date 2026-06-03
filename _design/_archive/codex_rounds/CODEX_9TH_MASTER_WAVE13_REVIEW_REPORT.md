狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：第九輪 master Wave 13 view-* SKILL.md 完成後 CODEX 重審報告
優先級：高

# 0. 文件目的

本報告是 CODEX reviewer agent 對第九輪 master Wave 13 新建 8 個 `SKILL.md` 的只讀重審結果。

本輪檢查範圍嚴格限縮於 Wave 13 8 個新 skill 檔、D6 / D7-D9 starter 參照、D-054 fallback 對照、呈現規則 authority、baseline gate、protected-area diff 與 stale cross-ref sweep。本輪不執行真實 `/view-*` skill，不修改任何 spec / protocol / registry / existing skill；唯一新增檔案為本報告。

# 1. Wave 13 摘要 + 判定(GO / NEAR-GO / NO-GO)

**判定：GO。**

| 維度 | 判定 | 摘要 |
|---|---|---|
| 維度 1：4 個英文 view-* SKILL.md 結構 | PASS | 4 個英文主檔均具備 D6 範本要求的 11 結構段；`## 錯誤處理 / Rollback` 與 `## 錯誤呈現規則` 均存在；流程均為 5 階段。 |
| 維度 2：D9 D-054 hybrid fallback | PASS | `view-detailed-outline` 明確落地 per-scene first、aggregate fallback、missing placeholder、`read_source` enum、禁止 split-to-file，並對齊 `scene-task` 與 D054 decision package。 |
| 維度 3：呈現規則 | PASS | 4 個英文主檔均明示 chat dynamic assembly 不加 breadcrumb / 不加 TOC、source italic、project-root link、same-file anchor、單向 reference、chat source hint。 |
| 維度 4：frontmatter + 中文 5 header | PASS | 8 檔均含 frontmatter `name` / `description` 與中文 5 header；4 個中文 wrapper 為極簡 wrapper；英文主檔 `name` 對齊 directory name。 |
| 維度 5：baseline + regression + protected-area diff | PASS | `check_headers` 0 ERROR / 45 WARN；`check_paths` 247 ERROR，符合 `<= 247`；`build_repo_index('.')` 0 ERROR；diff 僅見 Wave 13 expected set，無 protected-area mismatch。 |
| 維度 6：stale cross-ref sweep | PASS | 對 8 個 Wave 13 skill 檔掃舊檔名、舊版本、5 份 QA / 09_a-d pattern，0 active match。 |

Finding 總計：0 CRITICAL / 0 MAJOR / 0 MINOR / 1 INFO。

GO 依據：本輪 6 維度全 PASS；0 CRITICAL / 0 MAJOR；`check_paths.py` 維持 hard-limit accepted baseline 247 ERROR；protected-area diff 無 mismatch；stale grep 無 active match。INFO 僅為 description 長度的非阻斷觀察，不影響 skill 可用性或 Gate 判定。

# 2. 維度 1:4 個英文 view-* SKILL.md 結構對齊 D6 範本 11 段

**判定：PASS。**

D6 範本在 `_design/CODEX_D6_STARTER.md:84-101` 定義主 `SKILL.md` 結構，包含 frontmatter、中文 5 header 與 11 個功能段。實測 4 個英文主檔均含下列必要段：

- `## 用途`
- `## 觸發語`
- `## 觸發協議`
- `## 啟動前檢查`
- `## 流程`
- `## 呈現規則`
- `## .protocol_version 寫入規範`
- `## 輸入`
- `## 輸出`
- `## 邊界`
- `## 錯誤處理 / Rollback` + `## 錯誤呈現規則`

機械核對結果：

| 檔案 | 必要段缺漏 | 5 階段流程 | 純讀取邊界 7 條 |
|---|---:|---:|---:|
| `.claude/skills/view-world/SKILL.md` | 0 | PASS, lines 72 / 90 / 123 / 194 / 205 | PASS, lines 303-311 |
| `.claude/skills/view-character/SKILL.md` | 0 | PASS, lines 78 / 96 / 137 / 192 / 203 | PASS, lines 302-310 |
| `.claude/skills/view-outline/SKILL.md` | 0 | PASS, lines 73 / 91 / 121 / 176 / 187 | PASS, lines 283-291 |
| `.claude/skills/view-detailed-outline/SKILL.md` | 0 | PASS, lines 81 / 100 / 192 / 242 / 254 | PASS, lines 355-363 |

`## 觸發協議` 對齊：4 檔均明示無對應 `00_protocol/`，以 `_design/ARCHITECTURE.md` v1.6 §4.1 為 dynamic assembly 權威，且不得修改、patch 或解讀 `00_protocol/` 作為 runtime protocol。Evidence：`view-world:36-45`、`view-character:39-49`、`view-outline:37-46`、`view-detailed-outline:41-52`。

Sidecar observation reconciliation：次要 reviewer 曾把輸出骨架內的 `## 世界規則` / `## 聲線卡` 等標題列入結構段計數，並把 optional phase_log 視為純讀取衝突。本報告未採納為 finding，理由是 D6 範本本身明列 `## .protocol_version 寫入規範` 為必要段，且明示純讀取 skill 可選寫 phase_log audit entry，不更新 entity 完成度；output skeleton heading 屬組合內容範例，不是主 skill 結構缺段。

# 3. 維度 2:D9 D-054 hybrid fallback strict verify

**判定：PASS。**

`view-detailed-outline` 已含 `### D-054 hybrid 讀檔 fallback 規範`，並指定 `_design/D054_DECISION_PACKAGE.md` v0.2 與 `.claude/skills/scene-task/SKILL.md` v0.1 作為 D-054 讀檔依據。Evidence：`.claude/skills/view-detailed-outline/SKILL.md:49-50`、`:130-132`。

Strict verify 結果：

| 要求 | 結果 | Evidence |
|---|---|---|
| Phase 1 per-scene file first | PASS | `view-detailed-outline:136-152`：先 normalize scene ID、讀 `06_a` metadata、計算 per-scene candidate、存在即讀整檔並設 `read_source = "per-scene"`。 |
| Phase 2 aggregate `06_a` fallback | PASS | `view-detailed-outline:154-164`：per-scene 不存在時讀 aggregate row，設 `read_source = "aggregate"`，marker 指向缺檔則 WARN。 |
| Missing handling | PASS | `view-detailed-outline:166-174`：兩者皆無時保留輸出結構並印 `[S-<ch>-<n> 缺漏；提示用 /create-detailed-outline 建立]`，不從 downstream 合成內容。 |
| `read_source` enum | PASS | `view-detailed-outline:176-184`：每場只記 `per-scene` / `aggregate` / `missing` 之一，禁止同時記 per-scene + aggregate。 |
| 不觸發 split-to-file | PASS | `view-detailed-outline:186-190`：明示本 skill 不觸發 split-to-file；拆檔屬未來 Phase D `/iterate-scene <S-ID> --split-to-file`。 |
| 對齊 `scene-task` | PASS | `scene-task:339-399` 採同一 D-054 fallback skeleton；差異僅在 `/scene-task` 兩者皆無時拒絕，而 view skill 保留 placeholder，符合呈現型 skill 行為。 |
| 對齊 D054 decision package | PASS | `_design/D054_DECISION_PACKAGE.md:79-90` 選 Hybrid；`:214-221` 推薦理由；`:267-269` 明示 `--split-to-file` 為未來 Phase D scope。 |

# 4. 維度 3:呈現規則對齊 ARCH §4.1 + §4.4 + UX_SPEC §7

**判定：PASS。**

Authority evidence：

- `_design/ARCHITECTURE.md:744-747`：project-root link、source italic、單向 reference、chat dynamic source 引用。
- `_design/ARCHITECTURE.md:777-781`：`/view-*` chat dynamic assembly 不加 breadcrumb；TOC 屬長 `/export-*` 整合檔。
- `_design/ARCHITECTURE.md:831-839`：跨檔 link `/` 開頭、同檔 anchor `#slug`、breadcrumb / TOC / source / 單向 reference 規則。
- `_design/UX_SPEC.md:1493-1516`：breadcrumb 與 TOC 屬 `/export-*`。
- `_design/UX_SPEC.md:1539-1557`：source italic 與 chat dynamic source 引用。

4 個英文主檔均以相同規則落地：

| 檔案 | 呈現規則 evidence |
|---|---|
| `view-world` | `.claude/skills/view-world/SKILL.md:231-239` |
| `view-character` | `.claude/skills/view-character/SKILL.md:230-238` |
| `view-outline` | `.claude/skills/view-outline/SKILL.md:214-222` |
| `view-detailed-outline` | `.claude/skills/view-detailed-outline/SKILL.md:284-292` |

檢查結果：

- chat 動態組合不加 breadcrumb：PASS。
- chat 動態組合不加 TOC：PASS。
- 每段尾加 source italic：PASS。
- 跨檔 link 以 project root 為基準 `/` 開頭：PASS。
- 同檔 anchor `#slug` 不加 `/`：PASS。
- 單向 reference：PASS。
- chat dynamic assembly 也保留 source hint：PASS。

# 5. 維度 4:frontmatter 對齊 SPEC §5.2 + 中文 5 header

**判定：PASS。**

SPEC §5.2 權威要求中文 header 5 欄。Evidence：`_design/SPEC.md:265-326`、`:381`。ARCH skill 規格要求 `name` / `description` frontmatter。Evidence：`_design/ARCHITECTURE.md:452-550`。

8 個 Wave 13 skill 檔均有 frontmatter 與中文 5 header：

| 檔案 | frontmatter | 中文 5 header | wrapper 模式 / name 對齊 |
|---|---|---|---|
| `.claude/skills/view-world/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | name = `view-world` |
| `.claude/skills/view-character/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | name = `view-character` |
| `.claude/skills/view-outline/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | name = `view-outline` |
| `.claude/skills/view-detailed-outline/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | name = `view-detailed-outline` |
| `.claude/skills/查看世界觀/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | thin wrapper, lines 12-16 |
| `.claude/skills/查看角色/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | thin wrapper, lines 12-16 |
| `.claude/skills/查看大綱/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | thin wrapper, lines 12-16 |
| `.claude/skills/查看細綱/SKILL.md` | PASS, lines 1-4 | PASS, lines 6-10 | thin wrapper, lines 12-16 |

Description length note：英文主檔 description word count 為 27 / 29 / 34 / 33 words。若以 raw character count 解讀「50-200 字」，則 `view-character` 209、`view-outline` 240、`view-detailed-outline` 224 超過 200；若不計空白，僅 `view-outline` 207 超過 200。此 repo 既有多個已接受 skill description 也超過 raw 200 chars，且 `check_headers.py` / `build_repo_index('.')` 不將此視為 error，因此本輪列為 INFO，不降級維度 4。

# 6. 維度 5:baseline + regression + protected-area diff

**判定：PASS。**

Baseline commands：

| 命令 | 實測結果 | 判定 |
|---|---|---|
| `python -X utf8 -B scripts/check_headers.py` | 167 files / 0 ERROR / 45 WARN / 167 INFO | PASS。符合 0 ERROR / WARN <= 50 / files <= 170。 |
| `python -X utf8 -B scripts/check_paths.py` | 172 files / 247 ERROR / 1 WARN / 15 INFO | PASS。符合 hard-limit accepted `<= 247 ERROR`。 |
| `python -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; ..."` | 227 parsed files / 0 ERROR / 82 WARN | PASS。符合 0 ERROR。 |

Protected-area diff command：

```text
git -c core.quotepath=false diff bb50a54..HEAD --name-status
```

實測 diff（本報告寫入前，對已 commit 的 Wave 13 set 執行）：

```text
A	.claude/skills/view-character/SKILL.md
A	.claude/skills/view-detailed-outline/SKILL.md
A	.claude/skills/view-outline/SKILL.md
A	.claude/skills/view-world/SKILL.md
A	.claude/skills/查看世界觀/SKILL.md
A	.claude/skills/查看大綱/SKILL.md
A	.claude/skills/查看細綱/SKILL.md
A	.claude/skills/查看角色/SKILL.md
A	_design/CODEX_9TH_MASTER_WAVE13_REVIEW_STARTER.md
A	_design/CODEX_D6_STARTER.md
A	_design/CODEX_D_VIEW_BATCH_STARTER.md
A	_design/HANDOFF_9TH_MASTER_CONTINUATION.md
M	_design/POST_LOCK_PENDING.md
```

判定：PASS。上述為 Wave 13 expected set：8 個 skill、D6 starter、D view batch starter、Wave 13 review starter、continuation handoff、POST_LOCK_PENDING Wave 13 狀態更新。未見 `scripts/`、`00_protocol/`、registry、LOCKED spec、既有 16 個 Phase A/B/C skill、Wave 12 starter set 或 archive 變更。

注意：task packet 同時把 `POST_LOCK_PENDING` 列入「不動段」與「Wave 13 預期變動」。本報告依 protected-area diff 指令下的「Wave 13 預期變動」處理，將目前 `POST_LOCK_PENDING.md` 修改視為 expected Wave 13 scope，不列 mismatch。

本報告本身是本輪明示允許新增的唯一 review artifact；commit 本報告後，`bb50a54..HEAD` 會額外出現 `_design/CODEX_9TH_MASTER_WAVE13_REVIEW_REPORT.md`，仍屬本輪允許輸出，不是 protected-area mismatch。

# 7. 維度 6:跨範圍 stale cross-ref grep 全掃

**判定：PASS。**

Sweep target：Wave 13 8 個新 `SKILL.md` only。

Pattern set：

- 舊檔名 stale：`04_b_關係演化時間線|05_a_主線結構\.md|05_b_章節結構\.md|05_c_角色弧線\.md|06_scene_index/06_a_場景索引\.md`
- 版本 stale：`create-character.*v0\.3|POST_LOCK_PENDING.*v0\.(9|10|11|12|13)|DECISIONS_LOG.*v1\.[1-9]|TASKS.*v1\.[1-8]|ARCH.*v1\.[1-5]`
- 5 份 / 09_a-d stale：`5 份 QA|五份 QA|09_a-d|09_a–09_d`

實測結果：0 match。判定：無 active stale cross-ref。

# 8. Finding 總計表(R-W13-<severity>-<NN>)

| ID | Severity | 狀態 | 摘要 | 影響 |
|---|---|---|---|---|
| R-W13-INFO-01 | INFO | Accepted observation | 英文主檔 description 若採 raw character count，3 檔超過 200 chars；若不計空白僅 `view-outline` 超過 200。既有 repo practice 與 validators 均未視為 gate error。 | 不影響 Wave 13 GO；可由 9th master 在未來 housekeeping 時決定是否收斂 description 長度。 |

總計：0 CRITICAL / 0 MAJOR / 0 MINOR / 1 INFO。

# 9. 決策判定 + Rationale

**決策判定：GO。**

Rationale：

1. 4 個英文 view-* SKILL.md 均符合 D6 範本的必備段落與 5 階段流程。
2. D9 `view-detailed-outline` 的 D-054 hybrid fallback 落地完整，且沒有觸發未來 `/iterate-scene --split-to-file` 的越界行為。
3. 呈現規則與 ARCH §4.1 / §4.4 / UX_SPEC §7 對齊，未把 `/export-*` 導航功能誤放進 chat dynamic assembly。
4. 8 個 skill frontmatter 與中文 5 header 齊全，wrapper 維持極簡指向英文主檔。
5. Baseline gate 無 regression：`check_headers` 0 ERROR、`check_paths` 維持 247 hard-limit、`build_repo_index` 0 ERROR。
6. Protected-area diff 無 unexpected mismatch；stale grep 無 active match。

# 10. 給 9th master 的建議(進 Wave 14 / inline patch / hard-limit accept)

建議：**進 Wave 14。**

不建議開 Wave 13 patch round。若 9th master 想完全消除 INFO observation，可在 Wave 14 前或 housekeeping 時縮短 3 個英文 description；但此項不影響當前 GO，且不需要 hard-limit accept。

Wave 14 啟動時建議沿用 Wave 13 成功模式：

- Master 先寫 D10 `/export-world` 完整 starter。
- D11-D13 採 batch starter，但要特別區分 `/view-*` chat dynamic assembly 與 `/export-*` persistent `view/` integration file。
- Wave 14 starter 應把 breadcrumb / TOC / source_files / generated_at / stale detection 與 L3 export schema 寫清楚，避免把 Wave 13 view 規則直接複製到 export。

# 11. Cross-ref

- `_design/CODEX_9TH_MASTER_WAVE13_REVIEW_STARTER.md` v0.1：本輪 review scope 與判定門檻。
- `_design/CODEX_D6_STARTER.md` v0.1：D6 /view-world 共通範本，含 11 段結構與 view 純讀取邊界。
- `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1：D7-D9 batch starter，含 D9 D-054 hybrid fallback 差異規格。
- `.claude/skills/view-world/SKILL.md` v0.1。
- `.claude/skills/view-character/SKILL.md` v0.1。
- `.claude/skills/view-outline/SKILL.md` v0.1。
- `.claude/skills/view-detailed-outline/SKILL.md` v0.1。
- `.claude/skills/查看世界觀/SKILL.md` v0.1。
- `.claude/skills/查看角色/SKILL.md` v0.1。
- `.claude/skills/查看大綱/SKILL.md` v0.1。
- `.claude/skills/查看細綱/SKILL.md` v0.1。
- `.claude/skills/scene-task/SKILL.md` v0.1：既有 D-054 fallback runtime pattern。
- `_design/D054_DECISION_PACKAGE.md` v0.2：D-054 Hybrid 拍板與推薦理由。
- `_design/ARCHITECTURE.md` v1.6 §4.1 / §4.4：dynamic assembly 與 presentation authority。
- `_design/UX_SPEC.md` v0.4 §7：cross-file navigation、breadcrumb、TOC、source reference authority。
- `_design/SPEC.md` v1.2 §5.2：中文 5 header 與 canonical frontmatter schema。
