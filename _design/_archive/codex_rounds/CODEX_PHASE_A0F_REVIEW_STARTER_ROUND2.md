狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：Phase A.0F NO-GO patch round 完成後 CODEX 2nd strict review (verify P0/P1/Major/Concern 8 條全修 + 84 JS test + Stage B 8 fixture test)
優先級：極高（GO 後 branch 可 merge 進 master / Phase A.0G 或 Phase B）

# CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2 — Phase A.0F patch round CODEX 2nd review

# 0. 本檔用途

Phase A.0F master 平行對話 12 commit + audit 4 commit + audit-codex starter 2 commit
→ **CODEX strict review (1st) 判 NO-GO**（`_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1）
→ patch master 跑 patch round 共 7 commit
→ 本輪：CODEX 2nd strict review verify 全修

**前置條件：**
- Branch `frontend-tools-a0f`（HEAD `a996ad5`，patch round 完成狀態）
- 1st CODEX report `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 已 land master（必讀）
- patch starter `_design/CODEX_PHASE_A0F_PATCH_ROUND_STARTER.md` v0.1（patch master 啟動指引）

**review GO →** branch 升 FINAL；merge 進 master；進 Phase A.0G 或 Phase B
**review NEAR-GO →** 再開 patch round（小修）
**review NO-GO →** 再開 patch round（中修）/ 或 restructure（如果發現新 P0）

⚠ **Scope 嚴格限定：本輪 verify ONLY，不擴新 feature。**
- 對齊 1st report §8 列的 8 條（P0 #1 / P0 #2 / P1 / Major #1 / Major #2 / Concern #1 / Concern #2 / P2 / P3）
- 確認 patch round 7 commit 都 verifiable
- 不擅啟新 D-NNN 拍板
- 不重審 D-001~D-054 / Phase A/B/C / 9th master 軸

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 Phase A.0F 第二輪 CODEX strict reviewer。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
分支：frontend-tools-a0f（HEAD: a996ad5，patch round 7 commit 完成後）

**第一步必讀（按順序）：**
1. `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 — 1st strict review NO-GO 報告（基準）
2. `_design/CODEX_PHASE_A0F_PATCH_ROUND_STARTER.md` v0.1 — patch round 啟動指引（8 條 + 教訓）
3. `_design/CODEX_PHASE_A0F_REVIEW_STARTER.md` v0.1 — 原 review starter 含 12 commit 列表
4. `_user_manual/05_frontend_tools.md` v0.3 — 既有 11 feature 落地狀態 + audit-doc 對齊
5. `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 — L3 schema contract 鎖
6. `_design/UX_SPEC.md` §11.3 / §11.5 / §11.6 / §11.7

**Patch round 7 commit (HEAD a996ad5 起回溯)：**

| commit | subject | 範圍 |
|---|---|---|
| `a996ad5` | patch-test | regression test 補洞 + api.js restore + Stage B tests |
| `2cfb651` | patch-concern-2 | §11.6.7 LOCKED downgrade guide as pure raw text |
| `9d2814a` | patch-concern-1+P2 | LOCKED route bypass preflight + router cleanup leak |
| `772fcc8` | patch-major-2 | L3 schema drift — 移除 chapter scope + enforce export/ prefix |
| `c0640be` | patch-major-1 | D-045 narrative readiness 排除 A-* (Dashboard) |
| `52c03c9` | patch-P1 | SceneQueue search summary XSS sink fix |
| `bef5516` | patch-P0 | Editor content loading + exact-path save (server.py + api.js + SceneEditor.js) |

**Verify 順序（1st report §8 patch 順序對齊）：**

P0 (架構性 broken — verify 已修)：
1. **Editor content loading**
   - server.py: `resolve_target_path(scene_id, raw_path)` 4 條驗 ✓
   - server.py: `GET /api/scene/{scene_id}/version-content?path=<rel>` endpoint ✓
   - SceneEditor.js: 改用 `fetchSceneVersionContent`（不再 fetch("/" + v.path)）✓
   - fail-closed：catch err → loadFailed=true → save disable + warning banner ✓
   - Verify: `git show frontend-tools-a0f:_tools/frontend/server.py | grep -n version-content`
   - Verify: `git show frontend-tools-a0f:_tools/frontend/static/js/pages/SceneEditor.js | grep -n fetchSceneVersionContent`

2. **Exact-path save / save-as**
   - server.py: save_scene + save_scene_as 必收 `target_path`（缺 → 400；驗失敗 → 404）✓
   - server.py: 不再 fallback 到 `resolve_scene_file`（雙版本錯版風險消除）✓
   - api.js: saveScene + saveSceneAs JSDoc 加 `target_path: string` 必填欄 ✓
   - SceneEditor.js: doSave / doSaveAs / force-overwrite 全傳 target_path ✓
   - mtime force-overwrite 改用 fetchSceneVersionContent 取最新 mtime ✓
   - Verify: `git show frontend-tools-a0f:_tools/frontend/server.py | sed -n '/async def save_scene/,/^@app/p'`
   - Verify: `git show frontend-tools-a0f:_tools/frontend/static/js/pages/SceneEditor.js | grep -n target_path`

P1 (XSS — verify 已修)：
3. **SceneQueue search summary XSS**
   - SceneQueue.js: filterSummaryText 對 search / chapters / pipelineStates / taskStatuses /
     hasDialogue / hasQa / hasLocked 全 escape ✓
   - 新增 sanitizeFilters 嚴格校驗 localStorage shape ✓
   - loadFilters 改 route through sanitizeFilters（不再 raw spread）✓
   - Verify: `git show frontend-tools-a0f:_tools/frontend/static/js/pages/SceneQueue.js | grep -n filterSummaryText`
   - Verify: regression test `patch_round_regression.test.mjs` 含 3 個 P1 anchor

Major (spec 違反 — verify 已修)：
4. **D-045 narrative separation**
   - ProjectDashboard.js: ENTITY_MODULES 移除 A row ✓
   - ProjectDashboard.js: trackedTotal 不再含 artAssets ✓
   - server.py: entity_counts 跳過 entity_type=="A" ✓
   - Asset Panel 仍透過 renderAssetPanel() 完整顯示 ✓
   - Verify: regression test `test_scope_counts_excludes_a_from_entities`
     (counts.entities['A'] == 0 even with assets registered)

5. **L3 schema drift**
   - 選 option (a)：移除 chapter scope + 限定 output_paths `^export/` 前綴 ✓
   - promptAssembler.js: ScopeType / ScopeOpts 移除 chapter ✓
   - promptAssembler.js: 新增 `assertExportPath(value, field)` 拒絕：
     絕對路徑 / .. segment / 不以 export/ 開頭 ✓
   - ExportPanel.js: UI radio 移除 chapter scope option ✓
   - Verify: prompt_assembler.test.mjs 33 test 全 PASS（含 chapter rejection + path rejection 2 個新 test）

Concern (verify 已修)：
6. **LOCKED route bypass**
   - router.js: SceneEditor route dispatch 到 `renderEditorPreflight` ✓
   - renderEditorPreflight fetch /api/scene/<id>/header → LOCKED → redirect ✓
   - Header API 錯誤 → fail-open mount Editor（內部 fail-closed） ✓
   - Verify: regression test `router.js: SceneEditor route dispatches to renderEditorPreflight`

7. **§11.6.7 guide/raw copy mode**
   - SceneDetail.js: renderLockedGate 不再用 renderCopyCommandButton wrapper ✓
   - 改用 [data-locked-guide-button] + [data-locked-guide-text] pure DOM button ✓
   - main.js: delegated click handler 走 copyToClipboard(rawGuideText) ✓
   - 不再包 COPY_MARKER_OPEN/CLOSE / 不再加 "指令：/已有 Context/來源" header ✓
   - Verify: regression test `SceneDetail.js: LOCKED gate emits data-locked-guide-button`
   - Verify: regression test `main.js: installs delegated handler for data-locked-guide-button`

8. **Router cleanup leak (P2)**
   - router.js: cleanup 補 removeEventListener for scenes:refresh + scene-detail:refresh ✓
   - 提前命名 handler 函式以便 remove ✓
   - Verify: regression test `router.js: cleanup removes scenes:refresh + scene-detail:refresh document listeners`

9. **SceneEditor dirty back dialog minor (P3)**
   - SceneEditor.js: openDirtyBackDialog 用 escapeHtml(String(v.version || "?")) ✓
   - Verify: regression test `SceneEditor.js: dirty back dialog escapes v.version through escapeHtml`

**驗收條件：**
- `node --check` 全 PASS（12 JS file）
- 84 JS test 全 PASS：
  - copy_command_button       10/10
  - patch_round_regression   23/23 (NEW)
  - prompt_assembler          33/33
  - sceneeditor_guide         18/18
- Stage A endpoint inventory 10/10 PASS（含新 `/api/scene/{scene_id}/version-content`）
- Stage B 8 個新 fixture test：
  - test_version_content_missing_path (400)
  - test_version_content_path_outside_dialogue_root (404)
  - test_version_content_path_traversal_rejected (404)
  - test_version_content_unknown_scene_path (404)
  - test_save_scene_missing_target_path (400)
  - test_save_scene_target_path_outside_dialogue (404)
  - test_save_scene_as_missing_target_path (400)
  - test_scope_counts_excludes_a_from_entities (D-045)
  在 host 端跑 `cd _tools/frontend && pip install -r requirements.txt && python tests/test_endpoints_smoke.py` 即可

**禁止：**
- 不擴新 feature
- 不擅升 L3_EXPORT_PROMPT_SCHEMA.md v0.2 → v1.1（option (a) 維持鎖）
- 不擅啟 new D-NNN 拍板
- 不動 9th master 軸 commit (d6ec085 / 499bc13)
- 不重審 audit-P1/P2/doc/test 4 commit（1st CODEX 已 verified）
- 不再 review 1st-round 已 PASS 的部分（如 CC-07 / Bug 1 / Bug 2）

開始 2nd strict review。
~~~

---

# 2. 後續流程

| 階段 | 動作 |
|---|---|
| **user 開新 CODEX 對話** | 把上面 ~~~ block 整段貼到新 CODEX 對話 |
| **CODEX 2nd strict review** | 預計回 GO / NEAR-GO / NO-GO 報告 |
| **CODEX 報告 land** | 寫到 `_design/CODEX_PHASE_A0F_REVIEW_REPORT_ROUND2.md` v0.1 |
| **GO 後** | merge frontend-tools-a0f 進 master，Phase A.0F FINAL |
| **NEAR-GO** | 補一輪 patch master 跑修；新 round 3 starter |
| **NO-GO** | 開新 patch round；不擅升新 D-NNN |

# 3. Cross-ref

- `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1（1st strict review NO-GO 報告 — 8 條基準）
- `_design/CODEX_PHASE_A0F_PATCH_ROUND_STARTER.md` v0.1（patch round 啟動指引）
- `_design/CODEX_PHASE_A0F_REVIEW_STARTER.md` v0.1（原 review starter 含 12 commit 列表）
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（schema 鎖；output_paths + scope enum）
- `_design/UX_SPEC.md` v0.4 §11.3 / §11.5 / §11.6 / §11.7
- `_design/DECISIONS_LOG.md` D-027 / D-029 / D-035 / D-038 / D-040 / D-042 / D-044 / **D-045** / D-046 #5 + CC-07
- `_design/SPEC.md` §5.2 + §16
- `_user_manual/05_frontend_tools.md` v0.3
- branch: `frontend-tools-a0f` (HEAD: a996ad5)
- 既有 patch starter 範本：`_design/CODEX_8TH_MASTER_PATCH2_REVIEW_STARTER.md` / `_design/CODEX_8TH_MASTER_PATCH3_REVIEW_STARTER.md` v0.1

# 4. 教訓沿用 + 新增

**patch master 累積 (delta vs 1st-round starter)：**
1. Sandbox virtiofs cache stale — 用 `git show <branch>:<path>` 從 git object store 讀檔 ✓ 應用
2. Cowork Write/Edit tool 可能截斷 multi-byte CJK — 長 CJK 檔用 Python write_bytes ✓ 應用（server.py + SceneEditor.js + SceneQueue.js + ProjectDashboard.js + promptAssembler.js + ExportPanel.js + router.js + SceneDetail.js + main.js 全部用此法）
3. sandbox 無權 unlink `.git/HEAD.lock` / git index tmp_obj — workaround `mv .git/HEAD.lock .git/HEAD.lock.old.N` ✓ 應用
4. CC-07 三條 / D-046 #5 守則最嚴 ✓ sceneeditor_guide.test.mjs 18 test 全 PASS
5. CODEX 教訓 1: 沒 runtime 驗證的 endpoint integration 必裂 — 已補 Stage B 8 個 fixture test
6. CODEX 教訓 2: UI text 對齊 ≠ math 對齊 — D-045 test 對 counts.entities['A'] 直接驗 == 0
7. CODEX 教訓 3: unit test 測「自己 vs 自己」≠ 測「自己 vs spec」— L3 chapter rejection + path
   enforcement 用 positive rejection test
8. CODEX 教訓 4: XSS audit 不能只 grep escapeHtml — 追完整 user input → DOM data flow，
   sanitizeFilters 補 localStorage shape 校驗
9. CODEX 教訓 5: backend resolve by sceneId 跟 frontend edit by version 是兩個 identity —
   target_path 必傳，server.resolve_target_path 4 條驗

**patch round 新教訓：**
10. **小心 Edit tool 對長 CJK 檔的截斷** — server.py / SceneEditor.js 都曾被截斷；
    patch master 後續一律用 Python write_bytes（從 git object 重建 + apply patch）。
11. **regression test 寫 split 切片時要避開重複 token** — openDirtyBackDialog / force-overwrite
    都同名出現多次；用 `parts.slice(2).join(...)` 拿 declaration 之後的 body。
12. **api.js 之類短文件也可能截斷** — 確認每個檔的 byte count + 跑 node --check + 跑
    test 是強制 step。
