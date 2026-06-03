狀態：DRAFT
版本：v0.1
最後更新：2026-05-22
適用範圍：Phase A.0F 平行對話 + audit follow-up 共 11 commit CODEX strict review
優先級：高

# CODEX_PHASE_A0F_REVIEW_REPORT v0.1

## 0. 結論 — NO-GO

**NO-GO。** A.0F 不能 merge / FINAL，原因不是小型 UI polish，而是 F3/F7 Scene Editor 的核心工作流不成立：目前 Editor 讀不到真實 markdown content，且 Save / Save-as 沒有鎖定使用者正在編的 exact version/path，會導致空內容、404 body、錯檔 mtime conflict，甚至錯版本覆寫風險。

本 review 以 `frontend-tools-a0f` branch object store 為準讀檔（`git show frontend-tools-a0f:<path>` / `git grep frontend-tools-a0f -- ...`），不信任 working tree。現場 branch 為 `frontend-tools-a0f`，HEAD `2f7a1c1`；feature/audit review 目標到 `e37cd3e`，`2f7a1c1` 是本 review starter commit，不作為功能實作的一部分評分。

主要 blocking findings：

- **P0 — Editor content load broken**：`SceneEditor.js:80-85` 用 `fetch("/" + v.path)` 讀 repo markdown，但 `server.py:817-818` 只把 `/` mount 到 `_tools/frontend/static`，不是 repo root；`fetch()` 對 404 不 reject，會把 404 body 當 textarea baseline。
- **P0 — Save target identity lost**：`SceneEditor.js:260-267` / `api.js:123-132` 只送 `sceneId + content + mtime_baseline`；`server.py:112-117` 每次重新 resolve 最新候選檔，`server.py:506-548` 寫該 resolved path，未使用正在編的 `v.path`。
- **P1 — SceneQueue XSS sink**：`SceneQueue.js:316` raw 插入 `filterSummary`；`SceneQueue.js:344-353` 由未 escape 的 search text 組字串。
- **Major — D-045 drift**：Dashboard readiness / module status 把 A-* 混入 narrative counts，違反 D-045「A-* 不納入 narrative /status」。
- **Major — L3 schema drift**：`promptAssembler.js` / ExportPanel 新增 `scope.type=chapter` 與任意 custom output_paths，但 `L3_EXPORT_PROMPT_SCHEMA.md` v0.2 未允許 chapter，且要求 output_paths 限定 `repo_root/export/`。

## 1. Axis 1 — Spec compliance per feature

### §11.1 Project Dashboard / F1

Mapping commit: `a13ce5a` + earlier F1 work; A.0F.11 asset panel from `7b72454`.

Status: **Partial / Major concern**.

Implemented:
- Dashboard reads live aggregate data through `fetchDashboardData()` and renders F1 sections (`ProjectDashboard.js:72-99`).
- A-* Asset Panel renders 7 subtype cards and independent narrative warning text (`ProjectDashboard.js:371-407`).

Concern:
- D-045 requires A-* asset progress separate from narrative readiness. `UX_SPEC.md:2516` says A-* completion must not enter narrative `/status`, and must be fully separated from §11.1.4 / §11.1.5.
- Actual code includes `artAssets` in `trackedTotal` and readiness denominator (`ProjectDashboard.js:81-84`), includes A in module status source list (`ProjectDashboard.js:4-12`), and backend merges art assets into `entity_ids` / entity_counts (`server.py:446-447`).

Recommendation: remove A-* from narrative readiness/module status counts; keep it only in `renderAssetPanel()`.

### §11.2 Scene Queue + Scene Detail cockpit / F2

Mapping commit: `e4721e9`.

Status: **Scene Queue list implemented; Scene Detail is honest MVP placeholder**.

Implemented:
- `/api/scenes` adapter endpoint exists and is documented as non-Contract-C self-use (`server.py:720-727`).
- Scene Detail read-only cockpit layout exists, with readiness panel, version list, QA count, quick actions, and LOCKED gate (`SceneDetail.js:55-360`).

Partial / placeholder:
- Required Context 6 sub-sections are only placeholder text (`SceneDetail.js:162-180`), matching manual disclosure (`_user_manual/05_frontend_tools.md:37`, `422-424`).
- QA Findings full modal and Beat Preview are placeholders (`SceneDetail.js:182-280`).

Concern:
- Dashboard / Queue still uses `/create-scene-task` in some suggestions (`ProjectDashboard.js:141-142`, `SceneQueue.js:559`), while AGENTS.md lists implemented Phase C skill as `/scene-task <scene_id>` (`AGENTS.md:139`). This is a command naming drift in user-facing copy.

### §11.3 Scene Editor / F3

Mapping commit: `4c0c36e`.

Status: **Critical broken implementation**.

Implemented surface:
- N-column editor UI, dirty state, diff preview, keyboard handler, modal scaffold, save / save-as controls exist (`SceneEditor.js:63-688`).
- Details pane and Required Context drawer are explicitly not landed (`SceneEditor.js:30`, `525-528`), which is disclosed in manual (`_user_manual/05_frontend_tools.md:425-426`).

Critical:
- `SceneEditor.js:80-85` comments that it needs raw fetch `GET /<rel_path>` and then does `fetch("/" + v.path).then((r) => r.text()).catch(() => "")`.
- `server.py:817-818` mounts only `_tools/frontend/static` at `/`; repo markdown paths under `/08_dialogue_outputs/...` are not served.
- The request can return 404 HTML/text and still be used as content because `response.ok` is never checked.

Critical:
- N-column dirty versions are saved one by one, but payload lacks target path (`SceneEditor.js:260-267`).
- API wrapper only accepts `{content, mtime_baseline}` (`api.js:123-132`).
- Backend resolve picks the latest candidate by mtime, not the user-selected version (`server.py:100-117`, `512-548`).

Recommendation: add a controlled content API or return exact content from `/api/scenes/{id}/versions`; save/save-as payload must include exact repo-relative path or verified version token.

### §11.4 Scene Queue Search + Facets / F6

Mapping commit: `25d919f`.

Status: **Partial, not full §11.4 compliance**.

Implemented:
- Search, Chapter, Pipeline State, Task Status, Has Dialogue, Has QA, Has LOCKED Version facets are rendered (`SceneQueue.js:273-323`).
- localStorage persisted state exists (`SceneQueue.js:58-76`).

Concern:
- UX spec §11.4.3 defines 7 dimensions: Chapter / Pipeline State / Mode Tag / Stage / QA Type / Readiness / Characters (`UX_SPEC.md:3410-3424`).
- Actual implementation uses non-spec replacements and omits dynamic QA Type despite D-027 (`SceneQueue.js:7-15`, `301-313`).
- Manual discloses these as not implemented (`_user_manual/05_frontend_tools.md:171-181`, `428-430`), so this is not hidden, but it cannot be counted as FINAL §11.4 compliance.

### §11.5 F7 Direct Edit + LOCKED Gate

Mapping commit: `4c0c36e`.

Status: **Server-side guard present, UI gate incomplete, save target bug makes guard unreliable per version**.

Pass:
- Server save checks latest header for LOCKED before mtime conflict (`server.py:517-529`, then `531-545`), matching D-040 ordering.

Concern:
- Direct hash route bypass exists: router accepts `#/scene/<id>/edit` directly (`router.js:30`, `208-212`), while UX says Editor should be entered only from Scene Detail and direct URL should redirect/deny (`UX_SPEC.md:3010-3020`, `3645-3648`).
- SceneEditor does not block LOCKED on entry; it only displays status / DEPRECATED banner (`SceneEditor.js:481-517`).
- Because save target identity is lost, LOCKED race guard may check the wrong version path.

### §11.6 CopyCommandButton + Export Prompt

Mapping commits: `989de19`, `1357247`.

Status: **CopyCommandButton tests pass; guide/raw special case drift**.

Pass:
- CopyCommandButton has 10 passing tests.
- L3 Export panel/prompt assembler exists and CC-07 basics pass.

Concern:
- UX §11.6.7 says LOCKED downgrade guide is pure guide/raw text, not command payload wrapper (`UX_SPEC.md:4040-4047`).
- Scene Detail uses `renderCopyCommandButton()` for guide text (`SceneDetail.js:421-429`), but CopyCommandButton always wraps payload with markers via `assembleCopyPayload()` (`CopyCommandButton.js:59-87`, `341-349`).

### §11.7 Multi-scene / mtime conflict

Mapping commit: `4c0c36e`.

Status: **UI present, core target identity bug blocks confidence**.

Implemented:
- mtime conflict modal exists and can reload or retry force overwrite (`SceneEditor.js:382-431`).
- backend returns `MTIME_DRIFT` body with server content (`server.py:531-545`).

Critical:
- Conflict detection is on whichever file `resolve_scene_file(scene_id)` chooses, not necessarily the edited column.
- Test coverage explicitly does not cover LOCKED race / mtime full flow (`test_endpoints_smoke.py:21-23`).

### §11.8 Build / package / endpoint surface

Mapping commit: `a13ce5a`.

Status: **Static frontend and 9 endpoint inventory present; runtime content route missing for Editor**.

Pass:
- `server.py` defines 8 Contract C endpoints + `/api/scenes` (`server.py:488`, `506`, `561`, `622`, `642`, `672`, `695`, `707`, `720`).
- `/api/scenes` docstring states it is not Contract C locked and is frontend adapter self-use (`server.py:722-727`).

Critical integration gap:
- No endpoint serves exact markdown content by version/path, while Editor relies on that behavior (`SceneEditor.js:80-85`).

### §11.9 Four reserved components

Mapping commit: `1ea2b7c`.

Status: **Landed with disclosure**.

Implemented:
- Workspace Home, Glossary, and theme routes are wired.
- Manual discloses glossary has 40 terms while §11.9.3 minimum was 13 (`_user_manual/05_frontend_tools.md:404`).

## 2. Axis 2 — D-NNN 拍板內化（D-027~D-046 + CC-07）

- **D-027 qa_type 可擴充 — Concern.** Spec requires QA Type dynamic facet from current schema/registry (`UX_SPEC.md:3418-3424`, `3479-3485`); actual F6 only has `Has QA` boolean and manual marks qa_type dynamic facet deferred (`SceneQueue.js:301-313`; `_user_manual/05_frontend_tools.md:430`).
- **D-028 SINGLE_ITER — Partial PASS.** UI command copy uses `/dialogue-write <scene_id> --single-iter` (`SceneDetail.js:359`, downgrade guides at `396`, `608`), but mode_tag facet is not implemented.
- **D-029 alpha separation — PASS.** Grep found no real `subprocess`, `exec(`, `popen`, `os.system`, `eval`, `new Function`, or `dangerouslySetInnerHTML` implementation in server/frontend. Export push is HTTP POST to user endpoint, not local CLI action.
- **D-035 Scene Detail read-only / Editor edit split — Concern.** Scene Detail is read-only and Editor is separate, but direct hash route bypass violates the specified entry model (`router.js:208-212`; `UX_SPEC.md:3645-3648`).
- **D-037 dialogue_keys Map — Partial.** Endpoint for key lines exists (`server.py:642-667`), but §11.3.5 details pane that should surface key metadata is not landed (`SceneEditor.js:30`, `525-528`).
- **D-038 L3 Export A1 — Concern.** A1 prompt assembler exists, but schema drift on `chapter` and unchecked `output_paths` undermines strict contract.
- **D-039 records[] authority — Partial PASS.** Prompt references DATA_FORMAT_SPEC §9 manifest + records[] (`promptAssembler.js:193-204`), but no runtime export is executed in A.0F, as expected.
- **D-040 LOCKED race guard — Critical due target identity.** Guard logic exists (`server.py:517-529`), but because backend resolves by `scene_id` instead of exact edited path, the guard can check the wrong version.
- **D-041 A-* SoT = `10_art_assets/` — PASS.** Asset APIs use `build_repo_index()` / art metadata index (`server.py:672-702`), and dashboard warnings point to `10_art_assets/<subtype>/` (`ProjectDashboard.js:448-450`).
- **D-042 base_dialogue / iteration_note — Partial.** `save-as` writes `base_dialogue` and `iteration_note` (`server.py:586-606`), but save-as target basename is still derived from the latest resolved path, not exact edited version (`server.py:571-577`).
- **D-044 7 subtype canonical — PASS.** Dashboard uses portrait / bg / cg / sfx / bgm / voice / ui (`ProjectDashboard.js:15-22`, `396-407`).
- **D-045 A-* not narrative — Critical/Major.** Violated by readiness denominator and entity counts (`ProjectDashboard.js:81-84`; `server.py:446-447`) despite UI text saying independent (`ProjectDashboard.js:406`).
- **D-046 #5 / C-16 / O-03 — Core text PASS, wrapper Concern.** SceneEditor and SceneDetail both instruct only changing `狀態：LOCKED -> 狀態：DEPRECATED` and moving reason/date/person to 09_e (`SceneEditor.js:592-616`; `SceneDetail.js:379-404`), matching SPEC §16a (`SPEC.md:1483-1491`). Concern remains that CopyCommandButton wraps SceneDetail guide text as command payload.
- **CC-07 — Basic PASS, adjacent schema Concern.** No `rerun_qa:` YAML field, `include_deleted` defaults false, and prompt says not to modify phase_log (`promptAssembler.js:164-167`, `213-221`). `chapter` and custom paths are separate schema drift concerns.

## 3. Axis 3 — L3 schema contract（promptAssembler）

Pass:
- Five required sections are assembled in order (`promptAssembler.js:129-260`).
- YAML contains required keys: `schema_version`, `project_id`, `repo_root`, `timestamp`, `scope`, `formats`, `include_deleted`, `output_paths`, `mode`, `contract_refs` (`promptAssembler.js:135-178`).
- `schema_version` is locked to `"1.0"` and `mode` to `"read_only"` (`promptAssembler.js:135`, `173`).
- CC-07 basics pass: no `rerun_qa:` field, include_deleted false by default, and constraints include not modifying phase_log (`promptAssembler.js:164-167`, `213-221`).
- Bug 1 regression is fixed by SKIP sentinel and 5 regression tests (`promptAssembler.js:226-260`; `prompt_assembler.test.mjs:304-346`).

Concerns:
- **Schema enum drift:** `L3_EXPORT_PROMPT_SCHEMA.md:80-82` lists only full / outline_only / scene. `promptAssembler.js:30`, `99`, `105-106`, `148-149`, `198` adds `chapter`, ExportPanel exposes it (`ExportPanel.js:32`, `343-359`), and tests lock it as valid (`prompt_assembler.test.mjs:142-155`) without schema version bump.
- **Path constraint not enforced:** schema requires output_paths under `repo_root/export/` (`L3_EXPORT_PROMPT_SCHEMA.md:96-99`), but assembler accepts arbitrary `opts.outputPaths` (`promptAssembler.js:120-122`) and UI allows custom paths (`ExportPanel.js:377-393`). Tests only cover happy-path `export/custom.*` (`prompt_assembler.test.mjs:216-223`).

Verdict: L3 is usable for happy-path prompt generation, but not strict schema compliant.

## 4. Axis 4 — Backend 9 endpoint inventory

Endpoint inventory PASS:

| Endpoint | Evidence | Review |
|---|---|---|
| `GET /api/scene/{scene_id}/header` | `server.py:488` | Exists; returns path/header/mtime/issues. |
| `POST /api/scene/{scene_id}/save` | `server.py:506` | Exists; has 404 / 409 LOCKED / 409 MTIME paths, but target identity bug. |
| `POST /api/scene/{scene_id}/save-as` | `server.py:561` | Exists; writes proposal and lineage fields, but target basename uses resolved latest path. |
| `GET /api/scenes/{scene_id}/versions` | `server.py:622` | Exists; returns versions without content. |
| `GET /api/scenes/{scene_id}/keys/{key}/lines` | `server.py:642` | Exists; returns key line data across versions. |
| `GET /api/assets` | `server.py:672` | Exists; supports all / subtype / scene scopes. |
| `GET /api/assets/{asset_id}/usage` | `server.py:695` | Exists; 404 unknown asset path. |
| `GET /api/scope-counts` | `server.py:707` | Exists; 400 invalid scope path. |
| `GET /api/scenes` | `server.py:720` | Exists; docstring explicitly says non-Contract-C frontend adapter self-use (`server.py:722-727`). |

Critical integration issue:
- Endpoint inventory does not include an exact markdown content endpoint, yet `SceneEditor.js:80-85` depends on static serving of repo markdown. Since `server.py:818` mounts only static frontend files, this breaks F3.

Test evidence:
- `test_endpoints_smoke.py` Stage A locks 9 endpoint inventory (`test_endpoints_smoke.py:36-46`, `72-81`) and passed.
- Stage B runtime tests were skipped because `httpx` is not installed.
- No test covers exact path save, content load, LOCKED overwrite denied with fixture, mtime drift with fixture, save-as proposal collision, or per-version write correctness.

## 5. Axis 5 — Code quality + bug hunt

### P0 — SceneEditor content load broken

Evidence:
- `SceneEditor.js:80-85` fetches `"/" + v.path` and never checks `response.ok`.
- `server.py:817-818` serves `_tools/frontend/static`, not repo root.
- `server.py:622-637` versions endpoint returns version/path/mtime/header only, not content.

Impact:
- Any scene with versions can open Editor with textarea containing 404 content or empty string.
- Because baselineContent becomes that bad content, a later save can write corrupt content.

Recommendation:
- Return `content` from `/api/scenes/{id}/versions` or add `GET /api/scene/{id}/version-content?path=...`.
- Fail closed when content fetch fails.
- Add regression test with a real version fixture.

### P0 — Save / Save-as target identity lost

Evidence:
- Frontend save payload only includes `content` and `mtime_baseline` (`SceneEditor.js:260-267`; `api.js:123-132`).
- Backend resolves by latest mtime candidate (`server.py:100-117`, `512-518`) and writes that path (`server.py:548`).
- Save-as also resolves by scene_id for target basename (`server.py:571-577`).

Impact:
- Editing v01 can attempt to save v02.
- mtime conflict can be false because baseline belongs to edited column but server compares latest candidate.
- LOCKED guard can check wrong version.

Recommendation:
- Payload must include exact repo-relative path or stable version token.
- Backend must validate path under `08_dialogue_outputs/`, verify it matches scene_id, then apply LOCKED / mtime / write to that exact path.
- Add double-version fixture tests.

### P1 — SceneQueue filter summary XSS

Evidence:
- `SceneQueue.js:316` inserts `${filterSummary}` raw into innerHTML.
- `filterSummaryText()` uses raw `filters.search` (`SceneQueue.js:344-353`).
- Search input is persisted and rerendered (`SceneQueue.js:124-130`, `58-65`).

Repro:
- Type `<img src=x onerror=alert(1)>` into Scene Queue search; active filter summary can parse it as HTML.

Recommendation:
- Escape the summary before insertion, or render structured tokens with per-token escaping.
- Validate localStorage state shape on load.

### P2 — Router cleanup listener leak

Evidence:
- `initRouter()` adds `hashchange`, `scenes:refresh`, `scene-detail:refresh` listeners (`router.js:217-222`).
- Cleanup only removes `hashchange` (`router.js:225-228`).

Impact:
- Re-initializing router in tests/HMR/remount can duplicate document handlers.

### P3 — Minor unescaped dirty version list

Evidence:
- Dirty back dialog uses `dirtyVersions().map((v) => v.version).join(" / ")` inside innerHTML (`SceneEditor.js:223-234`).
- Current `VERSION_RE` restricts versions (`server.py:33`), so exploitability is low, but it violates the XSS discipline.

Validated passes:
- No `eval`, `new Function`, or `dangerouslySetInnerHTML` found.
- Bug 2 focus restore exists and restores selection for ExportPanel inputs (`ExportPanel.js:96-119`).
- audit-P2 cleanup is mostly true: `.editor-column--trial` uses CSS var; `#2563eb` remains only in explanatory comment (`components.css:1238-1241`).

## 6. Axis 6 — Test coverage analysis

Executed tests:

- `node _tools/frontend/tests/copy_command_button.test.mjs` -> 10 passed.
- `node _tools/frontend/tests/prompt_assembler.test.mjs` -> 33 passed.
- `node _tools/frontend/tests/sceneeditor_guide.test.mjs` -> 18 passed.
- JS total: 61 passed.
- `Get-ChildItem ... *.js | ForEach-Object { node --check $_.FullName }` -> PASS, no syntax errors.
- `PYTHONIOENCODING=utf-8; PYTHONDONTWRITEBYTECODE=1; python _tools/frontend/tests/test_endpoints_smoke.py` -> Stage A 2 passed, Stage B skipped due missing `httpx`.

Coverage that is meaningful:

- CopyCommandButton payload format and stable markers.
- Prompt schema happy-path, CC-07 basics, Bug 1 blank-line regression.
- D-046 #5 anchor strings in SceneEditor and SceneDetail.
- Endpoint inventory AST shape.

Critical coverage gaps:

- No test for Editor loading real markdown content.
- No test for `fetch()` 404 fail-closed behavior.
- No test for exact per-version save target.
- No test for LOCKED race guard against exact edited file.
- No test for save-as proposal target path / base_dialogue correctness against edited version.
- No XSS test for SceneQueue summary.
- No router cleanup test.
- No D-045 test ensuring A-* is excluded from narrative readiness/module status.
- No L3 test rejecting `chapter` until schema allows it, or rejecting output paths outside `export/`.

sceneeditor_guide.test.mjs assessment:
- It is useful but string-anchor based. It locks the D-046 #5 words (`sceneeditor_guide.test.mjs:52-133`) but does not verify the actual copy payload mode, route gate, save target, or server behavior.

## 7. Axis 7 — master 自評 audit 漏抓檢查（meta-review）

Master/Claude audit reportedly found:
- Bug 1 promptAssembler completion blank-line filtering.
- Bug 2 ExportPanel focus restore.
- Bug 3 dark mode hardcoded color.
- Dead code and doc/test gaps.

Those fixes are mostly present and pass their narrow tests. However, the audit missed more severe issues:

- **Missed P0:** Editor cannot reliably load true markdown content.
- **Missed P0:** Editor save/save-as lacks exact version/path identity.
- **Missed P1:** SceneQueue search summary XSS.
- **Missed Major:** D-045 narrative readiness includes A-* counts.
- **Missed Major:** L3 schema drift (`chapter`, unchecked custom paths).
- **Missed Concern:** direct route into Editor bypasses Scene Detail gate.
- **Missed Concern:** guide/raw copy special case is wrapped as command payload.

Meta-review conclusion: the audit follow-up improved known narrow issues but did not cover end-to-end Editor correctness, backend target identity, or adversarial UI data handling. These are release-blocking for Phase A.0F.

## 8. 給 master 的 recommendation

Verdict: **NO-GO** until at least P0/P1 are patched and tested.

Required patch order:

1. **Fix Editor content loading**: backend returns exact content for each version; frontend checks `response.ok` and fails closed.
2. **Fix exact-path save/save-as**: payload includes exact path or stable version token; server validates path and scene_id before LOCKED/mtime/write.
3. **Add regression tests**: double-version fixture, exact v01/v02 save, LOCKED exact target, mtime exact target, content load failure.
4. **Fix SceneQueue XSS** and add test.
5. **Fix D-045 narrative separation** and add test that A-* does not enter readiness/module status.
6. **Resolve L3 schema drift**: either remove chapter scope/custom outside-export paths, or update schema with explicit version bump and validation.
7. **Fix LOCKED route bypass**: direct `#/scene/<id>/edit` must preflight header and block/redirect if LOCKED.
8. **Fix guide/raw copy mode** if §11.6.7 remains authoritative.

After those patches, rerun JS tests, Stage A endpoint inventory, and at least one Stage B/runtime fixture path. Only then reconsider GO vs NEAR-GO.

## 9. Test sweep evidence

Commands run in this review:

```powershell
git status --short -uall
git rev-parse --abbrev-ref HEAD
git rev-parse HEAD
git log --oneline --decorate --max-count=20 frontend-tools-a0f
git show frontend-tools-a0f:_design/CODEX_PHASE_A0F_REVIEW_STARTER.md
git grep ... frontend-tools-a0f -- _design/... _tools/frontend/...
node _tools/frontend/tests/copy_command_button.test.mjs
node _tools/frontend/tests/prompt_assembler.test.mjs
node _tools/frontend/tests/sceneeditor_guide.test.mjs
Get-ChildItem -LiteralPath _tools\frontend\static\js -Recurse -Filter *.js | ForEach-Object { node --check $_.FullName }
$env:PYTHONIOENCODING='utf-8'; $env:PYTHONDONTWRITEBYTECODE='1'; python _tools/frontend/tests/test_endpoints_smoke.py
node --input-type=module -e "import { assembleExportPrompt } from './_tools/frontend/static/js/components/promptAssembler.js'; ..."
```

Observed:

- Branch already on `frontend-tools-a0f`, HEAD `2f7a1c1aeb35fa308c2425e27d58b6866afd34be`.
- `git checkout frontend-tools-a0f` failed due existing `.git/HEAD.lock`; current branch/HEAD already matched requested branch, so review proceeded read-only.
- Working tree had pre-existing starter path dirty state: `D _design/CODEX_PHASE_A0F_REVIEW_STARTER.md` and `?? _design/CODEX_PHASE_A0F_REVIEW_STARTER.md`; review reads used branch object store.
- JS tests: 61 passed, 0 failed.
- JS syntax check: PASS.
- Python smoke: Stage A 2 passed; Stage B skipped because `httpx` package is not installed.

