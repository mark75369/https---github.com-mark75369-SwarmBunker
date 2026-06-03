狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：Phase A.0F CODEX strict review NO-GO 後 patch round — 修 P0 (Editor content + exact-path save) + P1 (XSS) + Major (D-045 / L3 schema drift) + Concern (LOCKED route bypass / guide copy mode) + regression test 補洞
優先級：極高（CODEX 已判 NO-GO 不可 merge）

# CODEX_PHASE_A0F_PATCH_ROUND_STARTER — Phase A.0F NO-GO 後 patch round

# 0. 本檔用途

Phase A.0F master 平行對話：A.0F.5/3/4/11/10/9/6+7+8 → 整體驗收 → audit-P1/P2/doc/test → audit-codex-starter → **CODEX strict review (見 `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1) 判 NO-GO** → 本輪 fresh Claude 對話接手 patch round。

**前置條件：**
- Branch `frontend-tools-a0f`（HEAD `2f7a1c1` audit-codex-starter）
- CODEX report `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 已 land master（user 端 push）— **patch master 必須先讀**
- Phase A.0F 12 commit + audit 4 commit + audit-codex-starter 1 commit = 17 commit 全在 branch

**patch GO →** branch 升 FINAL；merge 進 master；進 Phase A.0G 或 Phase B
**patch NEAR-GO →** 再開 CODEX strict review 2nd round
**patch NO-GO →** restructure（不太可能 — Phase A.0F 架構大致對，只是 P0/P1 fix）

⚠ **Scope 嚴格限定：本輪 patch ONLY，不擴新 feature。**
- 修 CODEX report §8 列的 8 條 + report 內補充提到的 P2/P3 minor
- 不重審 D-001~D-054 / Phase A/B/C / 9th master 軸
- 不擅啟新 D-NNN 拍板（如有 schema drift 需正式修 schema，回升 user 拍板）

⚠ **教訓沿用（Phase A.0F 累積 + CODEX review 新增）：**
1. Sandbox virtiofs cache stale — 用 `git show <branch>:<path>` 從 git object store 讀檔
2. Cowork Write/Edit tool 可能截斷 multi-byte CJK — 長 CJK 檔用 Python write_bytes
3. sandbox 無權 unlink `.git/HEAD.lock` / git index tmp_obj — workaround `mv .git/HEAD.lock .git/HEAD.lock.old.N`
4. CC-07 三條 / D-046 #5 守則最嚴
5. **CODEX 新教訓 1**：沒 runtime 驗證的 endpoint integration **必裂** — sandbox 無法跑 fastapi 就**必須**寫 fixture-based test 對 Stage B 的 path identity / 404 fail-closed / LOCKED race 真實流
6. **CODEX 新教訓 2**：UI text 對齊 ≠ math 對齊 — 任何「獨立計算」/「不納入」必須**對 computation 直接驗**，不只看 UI string
7. **CODEX 新教訓 3**：unit test 測「自己 vs 自己」≠ 測「自己 vs spec」— schema enum / scope 變體**必對照 spec 字面 list** 驗
8. **CODEX 新教訓 4**：XSS audit 不能只 grep escapeHtml，必須追 user input → DOM 完整 data flow（含 localStorage / 跨 rerender）
9. **CODEX 新教訓 5**：backend resolve by sceneId 跟 frontend edit by version 是兩個 identity，**path 必須明示傳遞**，不能讓 backend 用 mtime 倒推

---

# 1. 啟動 prompt（複製整段到新 Claude 對話）

~~~
你是 game-dialogue-bible 專案的 Phase A.0F patch master — 接續 Phase A.0F NO-GO 後 patch round。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
分支：frontend-tools-a0f（HEAD: 2f7a1c1，CODEX review 後狀態）

**第一步必讀（按順序）：**
1. `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 — CODEX strict review NO-GO 報告（5 P0/P1/Major + 8 patch 順序）
2. `_design/CODEX_PHASE_A0F_REVIEW_STARTER.md` v0.1 — 原 starter 含 12 commit 列表 + spec 對齊
3. `_user_manual/05_frontend_tools.md` v0.3 — 既有 11 feature 落地狀態 + audit-doc 對齊
4. `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 — L3 schema contract 鎖（修 #5 schema drift 必對照）
5. `_design/UX_SPEC.md` §11.3 / §11.5 / §11.7 — Editor + LOCKED + conflict 規範

**Scope 嚴格限定（patch round ONLY）：**
- `_tools/frontend/` + `_user_manual/05_frontend_tools.md` + 本 patch 必要時 `_design/` 補新 starter / report
- 不擴新 feature；不重審 D-001~D-054；不動 9th master 軸 commit
- patch 順序依 CODEX report §8（P0 必修 → P1 → Major → Concern）

**Patch 順序（CODEX report §8）：**

P0（架構性 broken — 必修）：
1. **Editor content loading**
   - Backend: 新加 endpoint `GET /api/scene/<id>/version-content?path=<rel>` 回 raw markdown content；驗 path 在 08_dialogue_outputs/ 內 + 對應 scene_id
   - 或：extend `GET /api/scenes/<id>/versions` 也帶 content（建議用前者保持 versions endpoint 輕量）
   - Frontend `SceneEditor.js:80-85`: 改用該 endpoint，check `response.ok`，404 → fail closed (顯示 error，不 silently 灌 404 body)
   - Test: 加 fixture-based regression test — 真實 dialogue 檔 + 404 fail closed
2. **Exact-path save / save-as**
   - Frontend payload 加 `target_path: v.path` 或 stable `version_token`
   - Backend `server.py:506` save_scene + `server.py:561` save_scene_as 改用 payload path（不用 resolve_scene_file 倒推）
   - 驗 path 在 08_dialogue_outputs/ + 對應 scene_id（避免 path traversal）
   - 套 LOCKED / mtime / write 全用該 exact path
   - Test: 雙版本 fixture，編 v01 save 不能寫到 v02

P1（XSS — 釋出 blocker）：
3. **SceneQueue search summary XSS**
   - `SceneQueue.js:316` escape filterSummary
   - `filterSummaryText():344-353` 對 `filters.search` escape 或結構化 token 渲染
   - Validate localStorage state shape on load
   - Test: 加 XSS regression — 輸入 `<img src=x onerror=alert(1)>` 不該 inject

Major（spec 違反）：
4. **D-045 narrative separation**
   - `ProjectDashboard.js:81-84` trackedTotal **不**含 artAssets
   - `server.py:446-447` entity_counts **不** merge A-* asset_id（或加 scope filter）
   - `ProjectDashboard.js:4-12` ENTITY_MODULES 移除 A row（或標記 A 不入 readiness）
   - Test: 加 D-045 regression — A-* 改變不應影響 narrative readiness %
5. **L3 schema drift**
   - 兩選：(a) 移除 `scope.type=chapter` 跟 unconstrained custom output_paths（保持 v0.2 contract）；(b) 升 schema v1.1 + 更新 L3_EXPORT_PROMPT_SCHEMA.md（**需 user 拍板**，不能擅升 schema）
   - 建議 (a)：移除 chapter scope + 限定 output_paths 必須 `^export/` 前綴
   - Test: 加 schema enforcement — chapter scope 應 throw / 非 export/ 路徑應 throw

Concern：
6. **LOCKED route bypass**
   - `router.js:208-212` `#/scene/<id>/edit` direct hash 必先 preflight `/api/scene/<id>/header`
   - 若 LOCKED → redirect 回 `#/scene/<id>` 並顯示 LOCKED gate
7. **§11.6.7 guide/raw copy mode**
   - `SceneDetail.js:421-429` renderLockedGate 不用 renderCopyCommandButton wrapper
   - 改用 pure clipboard write — 不加 marker 不組 payload
   - 或：CopyCommandButton 加 `rawMode: true` 變體 不 wrap marker
8. **Router cleanup leak（P2）**
   - `router.js:217-228` cleanup 補 remove `scenes:refresh` + `scene-detail:refresh` document listener
9. **SceneEditor dirty back dialog minor（P3）**
   - `SceneEditor.js:223-234` escape version 字串（雖低風險）

**驗收條件（每 patch 後）：**
- node --check 全 PASS
- 61 JS test 全 PASS（加新 regression test 後變 70+）
- test_endpoints_smoke.py Stage A PASS
- 若有 backend endpoint 改動 — 加 fixture-based test 對 Stage B（可能需 user host 端跑）

**Commit 慣例：**
- `Phase A.0F.patch-P0-<n>:` Editor 修 P0 兩條（可分兩 commit 或合一）
- `Phase A.0F.patch-P1:` XSS 修
- `Phase A.0F.patch-major-<n>:` D-045 / L3 schema 各一 commit
- `Phase A.0F.patch-concern-<n>:` LOCKED bypass / guide copy mode 各一 commit
- `Phase A.0F.patch-test:` 新 regression test 合一 commit
- 總計約 6-8 個 patch commit

**完成後產出：**
- 新 starter `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1 給 CODEX 跑 2nd round strict review
- 或直接 user push 給 CODEX 用「短版啟動指令」（master 給的範本）

**禁止：**
- 不擴新 feature（不加 details pane / Required Context 抽屜 / 新 facet 維度等）
- 不擅升 L3_EXPORT_PROMPT_SCHEMA.md v0.2 為 v1.1（need user 拍板 D-NNN）
- 不擅啟 new D-NNN 拍板
- 不動 9th master 軸 commit (d6ec085 / 499bc13)
- 不重審 audit-P1/P2/doc/test 4 commit（CODEX 已 verified those）

開始 patch round。
~~~

---

# 2. 後續流程

| 階段 | 動作 |
|---|---|
| **user 開新 Claude 對話** | 把上面 ~~~ block 整段貼到新 Claude 對話 |
| **新 master 跑 patch round** | 預計 6-8 commit；先 P0 互鎖 → P1 → Major → Concern |
| **完成後產 round 2 starter** | `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` 給 CODEX 2nd round verify |
| **CODEX 2nd round** | user 用短版啟動指令貼到新 CODEX 對話跑 strict review |
| **GO 後** | merge frontend-tools-a0f 進 master，Phase A.0F FINAL |

# 3. Cross-ref

- `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1（**第一步必讀** — 完整 NO-GO 報告）
- `_design/CODEX_PHASE_A0F_REVIEW_STARTER.md` v0.1（原 starter 含 12 commit 列表 + spec 對齊）
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（schema 鎖；patch #5 必對照）
- `_design/UX_SPEC.md` v0.4 §11.3 / §11.5 / §11.6 / §11.7
- `_design/DECISIONS_LOG.md` D-027 / D-029 / D-035 / D-038 / D-040 / D-042 / D-044 / **D-045**（Major 違反） / D-046 #5 + CC-07
- `_design/SPEC.md` §5.2 + §16
- `_user_manual/05_frontend_tools.md` v0.3
- branch: `frontend-tools-a0f` (HEAD: 2f7a1c1)
- 既有先例 patch starter：`_design/CODEX_8TH_MASTER_PATCH2_REVIEW_STARTER.md` / `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_STARTER.md` v0.1（格式範本）
