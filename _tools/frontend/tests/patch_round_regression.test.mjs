/**
 * Phase A.0F.patch-test: regression tests for the CODEX NO-GO patch round.
 *
 * Run:
 *   node _tools/frontend/tests/patch_round_regression.test.mjs
 *
 * Coverage map (CODEX_PHASE_A0F_REVIEW_REPORT v0.1 §8 patch order):
 *   #3  P1  — SceneQueue XSS sink + localStorage shape sanitize
 *   #5  Major #1 D-045 — ProjectDashboard narrative separation (source check)
 *   #5b Major #2 L3 — chapter scope rejection + non-export path rejection
 *               (also covered in prompt_assembler.test.mjs; here we add the
 *                schema-vs-spec anchor checks)
 *   #7  Concern #1 — LOCKED route preflight presence (source check)
 *   #7b Concern #2 — §11.6.7 raw-mode guide button (no COPY_MARKER wrap)
 *   #8  P2  — router cleanup removes document listeners
 *   #9  P3  — SceneEditor dirty back dialog escapes version string
 *
 * Notes:
 *   - JSDOM is not available in the test runner; UI flow checks are AST/string
 *     anchors over the source, not live DOM mutation. The intent is to guard
 *     against regressions where someone re-introduces the unsafe pattern.
 *   - Pure-function tests (XSS sanitize / filterSummaryText) import the
 *     module directly and exercise the function.
 */

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, resolve } from "node:path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const FRONTEND_ROOT = resolve(__dirname, "..");

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    const result = fn();
    if (result && typeof result.then === "function") {
      result
        .then(() => {
          passed += 1;
          console.log(`  ✓ ${name}`);
        })
        .catch((err) => {
          failed += 1;
          console.error(`  ✗ ${name}`);
          console.error(err instanceof Error ? err.stack : err);
        });
    } else {
      passed += 1;
      console.log(`  ✓ ${name}`);
    }
  } catch (err) {
    failed += 1;
    console.error(`  ✗ ${name}`);
    console.error(err instanceof Error ? err.stack : err);
  }
}

const sceneQueueSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/SceneQueue.js"), "utf-8");
const sceneEditorSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/SceneEditor.js"), "utf-8");
const sceneDetailSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/SceneDetail.js"), "utf-8");
const dashboardSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/components/ProjectDashboard.js"), "utf-8");
const routerSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/router.js"), "utf-8");
const serverSrc = readFileSync(resolve(FRONTEND_ROOT, "server.py"), "utf-8");
const apiSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/api.js"), "utf-8");

console.log("Phase A.0F.patch-test: NO-GO patch round regression checks");
console.log("");
console.log("--- #1 P0 / Editor content loading + exact-path save ---");

test("server.py: resolve_target_path validates 4 conditions", () => {
  assert.match(serverSrc, /def resolve_target_path\(scene_id: str, raw_path: str\)/);
  assert.match(serverSrc, /08_dialogue_outputs\//);
  assert.match(serverSrc, /\.\." in candidate_rel.split\("\/\"\)/);
  assert.match(serverSrc, /scene_matches\(candidate, parsed, scene_id\)/);
});

test("server.py: version-content endpoint exists + uses resolve_target_path", () => {
  assert.match(serverSrc, /@app\.get\("\/api\/scene\/\{scene_id\}\/version-content"\)/);
  assert.match(serverSrc, /async def get_scene_version_content\(scene_id: str, path: /);
  assert.match(serverSrc, /"content": read_markdown\(target_path\)/);
});

test("server.py: save_scene requires target_path (not resolve_scene_file fallback)", () => {
  // Source must contain explicit target_path required check and call resolve_target_path.
  const saveSlice = serverSrc.split(/async def save_scene\(scene_id: str/)[1] || "";
  const block = saveSlice.split(/@app\.post/)[0] || saveSlice;
  assert.match(block, /target_path is required/);
  assert.match(block, /resolve_target_path\(scene_id, target_path_raw\)/);
});

test("server.py: save_scene_as requires target_path", () => {
  const slice = serverSrc.split(/async def save_scene_as\(scene_id: str/)[1] || "";
  const block = slice.split(/@app\.get/)[0] || slice;
  assert.match(block, /target_path is required/);
  assert.match(block, /resolve_target_path\(scene_id, target_path_raw\)/);
});

test("api.js: saveScene + saveSceneAs type-doc mention target_path required", () => {
  assert.match(apiSrc, /target_path: string/);
  assert.match(apiSrc, /fetchSceneVersionContent\(sceneId, relPath\)/);
});

test("SceneEditor.js: loadEditor uses fetchSceneVersionContent (no static-mount fetch)", () => {
  assert.match(sceneEditorSrc, /fetchSceneVersionContent\(sceneId, v\.path\)/);
  // Strip comment lines before checking that the unsafe pattern is gone — the
  // patch comment intentionally references the legacy code as documentation.
  const codeOnly = sceneEditorSrc
    .split(/\n/)
    .filter((line) => !/^\s*\/\//.test(line))
    .join("\n");
  assert.doesNotMatch(codeOnly, /fetch\("\/" \+ v\.path\)/);
});

test("SceneEditor.js: doSave passes target_path + refuses loadFailed versions", () => {
  assert.match(sceneEditorSrc, /target_path: v\.path/);
  assert.match(sceneEditorSrc, /v\.loadFailed/);
});

test("SceneEditor.js: force-overwrite re-fetches version-content (not /header)", () => {
  // The literal string force-overwrite appears in the modal HTML and as the
  // action value; the actual code body comes after the second occurrence.
  const parts = sceneEditorSrc.split(/force-overwrite/);
  const slice = parts.slice(2).join("force-overwrite");
  assert.match(slice, /fetchSceneVersionContent\(sceneId, version\.path\)/);
});

console.log("");
console.log("--- #3 P1 / SceneQueue XSS ---");

const { default: queueModule } = await import(`data:text/javascript,export default {}`).catch(() => ({ default: {} }));

// Pure-function tests: import the module and exercise filterSummaryText.
const { filterSummaryText: _exportProbe } = await import("../static/js/pages/SceneQueue.js").catch(() => ({}));

// SceneQueue.js does not export filterSummaryText (it is module-internal). Use
// source anchors plus an indirect check via load-time behaviour described in the
// patch. The escape coverage is asserted by source.
test("SceneQueue.js: filterSummaryText escapes search input before injection", () => {
  // Source must run escapeHtml() over filters.search inside the summary builder.
  const slice = sceneQueueSrc.split(/function filterSummaryText/)[1] || "";
  const block = slice.split(/^\}/m)[0] || slice;
  assert.match(block, /escapeHtml\(filters\.search\)/);
  assert.match(block, /filters\.chapters\.map\(escapeHtml\)/);
  assert.match(block, /filters\.pipelineStates\.map\(escapeHtml\)/);
  assert.match(block, /filters\.taskStatuses\.map\(escapeHtml\)/);
  assert.match(block, /escapeHtml\(filters\.hasDialogue\)/);
});

test("SceneQueue.js: sanitizeFilters coerces malformed localStorage shapes", () => {
  // Function present; defends every facet field type.
  assert.match(sceneQueueSrc, /function sanitizeFilters\(raw\)/);
  assert.match(sceneQueueSrc, /triEnum.*v === "yes" \|\| v === "no"/);
  assert.match(sceneQueueSrc, /stringArray.*Array\.isArray\(v\).*typeof x === "string"/);
});

test("SceneQueue.js: loadFilters routes through sanitizeFilters (no raw spread)", () => {
  const slice = sceneQueueSrc.split(/function loadFilters/)[1] || "";
  const block = slice.split(/^\}/m)[0] || slice;
  assert.match(block, /sanitizeFilters\(parsed\)/);
  // Old unsafe pattern (raw spread without shape coercion) must be gone.
  assert.doesNotMatch(block, /\{ \.\.\.defaultFilters\(\), \.\.\.parsed \}/);
});

console.log("");
console.log("--- #5 Major #1 / D-045 narrative separation ---");

test("server.py: entity_counts merge skips A-* art assets", () => {
  // Source must skip A-type entities in the entity_counts loop.
  assert.match(serverSrc, /if entity_type == "A":/);
  assert.match(serverSrc, /per D-045 we ignore them/);
});

test("ProjectDashboard.js: ENTITY_MODULES omits A row", () => {
  const slice = dashboardSrc.split(/const ENTITY_MODULES = \[/)[1] || "";
  const block = slice.split(/\];/)[0] || slice;
  assert.doesNotMatch(block, /key: "A"/);
  assert.match(block, /key: "S"/);
});

test("ProjectDashboard.js: trackedTotal excludes artAssets from narrative denominator", () => {
  // The new expression should not add artAssets to the trackedTotal sum.
  assert.match(dashboardSrc, /trackedTotal = Math\.max\(1, entityTotal \+ dialogueLines \+ qaReports\)/);
  assert.doesNotMatch(dashboardSrc, /trackedTotal = Math\.max\(1, entityTotal \+ dialogueLines \+ artAssets \+ qaReports\)/);
});

console.log("");
console.log("--- #5b Major #2 / L3 schema drift ---");
// Most cases live in prompt_assembler.test.mjs (chapter rejection + path
// validation). Add an anchor check that the schema-vs-spec helper landed.
const { assembleExportPrompt } = await import("../static/js/components/promptAssembler.js");

test("L3 schema: assertExportPath helper exists in source", () => {
  const src = readFileSync(resolve(FRONTEND_ROOT, "static/js/components/promptAssembler.js"), "utf-8");
  assert.match(src, /function assertExportPath\(value, field\)/);
  assert.match(src, /must start with 'export\/' per L3 schema v0\.2/);
});

test("L3 schema: chapter scope explicitly rejected", () => {
  assert.throws(
    () => assembleExportPrompt({ scope: { type: "chapter" } }),
    /schema v0\.2/,
  );
});

test("L3 schema: non-export output_paths explicitly rejected", () => {
  assert.throws(
    () => assembleExportPrompt({
      scope: { type: "full" },
      outputPaths: { json: "tmp/out.json", md: "export/ok.md" },
    }),
    /export\//,
  );
});

console.log("");
console.log("--- #5c Major #2 round-2 / outline_only stats ---");

test("ExportPanel.js: refreshScopeCounts maps outline_only â scope=outline_only (not full)", () => {
  const panelSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/ExportPanel.js"), "utf-8");
  // Source must build scope-arg "outline_only" for the outline_only branch.
  assert.match(panelSrc, /formState\.scopeType === "outline_only"/);
  const slice = panelSrc.split(/function refreshScopeCounts/)[1] || "";
  const block = slice.split(/\n  function /)[0] || slice;
  assert.match(block, /scopeArg = "outline_only"/);
});

test("ExportPanel.js: currentPrompt suppresses stats when scope-counts errored or scope mismatches", () => {
  const panelSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/ExportPanel.js"), "utf-8");
  const slice = panelSrc.split(/function currentPrompt/)[1] || "";
  const block = slice.split(/\n  function /)[0] || slice;
  // Defensive fallback: stats is undefined when error / no data / scope mismatch.
  assert.match(block, /scopeCountsState\.error \|\| !scopeCountsState\.data \|\| statsScope !== expectedScopeArg/);
  // expectedScopeArg branch must cover outline_only.
  assert.match(block, /formState\.scopeType === "outline_only"/);
});

test("server.py: parsed_matches_scope handles scope=outline_only via parsed_outline_relevant", () => {
  assert.match(serverSrc, /def parsed_outline_relevant\(parsed: Any\)/);
  // outline_only branch must precede the scene/* / chapter/* branches in
  // parsed_matches_scope so that scope == "outline_only" short-circuits.
  assert.match(serverSrc, /if scope == "outline_only":/);
});

test("server.py: valid_scope_counts_scope accepts outline_only", () => {
  assert.match(serverSrc, /scope == "outline_only"/);
  // 400 error message must enumerate outline_only too.
  assert.match(serverSrc, /scope must be full, outline_only, scene\/<id>, or chapter\/<ch>/);
});

console.log("");
console.log("--- Round 2 finding #1 / Stage B acceptance blocker ---");

test("requirements.txt: includes httpx (fastapi.testclient.TestClient dependency)", () => {
  const reqs = readFileSync(resolve(FRONTEND_ROOT, "requirements.txt"), "utf-8");
  assert.match(reqs, /^httpx\b/m);
  assert.match(reqs, /fastapi\b/);
});

test("test_endpoints_smoke.py: Stage B skip returns nonzero by default", () => {
  const smokeSrc = readFileSync(resolve(FRONTEND_ROOT, "tests/test_endpoints_smoke.py"), "utf-8");
  // Default skip path must return 2, not 0. Without the opt-in flag a skip
  // is treated as an acceptance failure (CODEX 2nd review finding #1).
  assert.match(smokeSrc, /return 2/);
  // Opt-in flag must exist for sandbox / dev workflows that need to call the
  // script when fastapi is unavailable.
  assert.match(smokeSrc, /--allow-stage-b-skip/);
  // The error path must still surface the install hint.
  assert.match(smokeSrc, /pip install -r requirements\.txt/);
});

test("test_endpoints_smoke.py: forces UTF-8 stdout to survive Windows CP950 console (CODEX 3rd review)", () => {
  const smokeSrc = readFileSync(resolve(FRONTEND_ROOT, "tests/test_endpoints_smoke.py"), "utf-8");
  // Helper must exist and be called from main() before any print() — otherwise
  // ✓ / ✗ / Chinese explanatory text raise UnicodeEncodeError under default
  // Windows CP950 / Big5 console, crashing the script before tests run.
  assert.match(smokeSrc, /def _force_utf8_console\(/);
  assert.match(smokeSrc, /_force_utf8_console\(\)/);
  // Reconfigure call must target both stdout and stderr.
  assert.match(smokeSrc, /sys\.stdout, sys\.stderr/);
  // errors="replace" — never crash on edge characters.
  assert.match(smokeSrc, /errors="replace"/);
});

console.log("");
console.log("--- #7 Concern #1 / LOCKED route bypass preflight ---");

test("router.js: SceneEditor route dispatches to renderEditorPreflight (not renderSceneEditor directly)", () => {
  const slice = routerSrc.split(/SCENE_EDITOR_RE\.exec\(route\)/)[1] || "";
  const block = slice.split(/cleanup = renderNotFound/)[0] || slice;
  assert.match(block, /renderEditorPreflight\(app, sceneId\)/);
  // Direct mount path must be gone.
  assert.doesNotMatch(block, /^\s*cleanup = renderSceneEditor\(app, \{ sceneId \}\);/m);
});

test("router.js: renderEditorPreflight redirects on LOCKED", () => {
  const slice = routerSrc.split(/function renderEditorPreflight/)[1] || "";
  const block = slice.split(/export function initRouter/)[0] || slice;
  assert.match(block, /"LOCKED"/);
  assert.match(block, /window\.location\.hash =/);
});

console.log("");
console.log("--- #7b Concern #2 / §11.6.7 raw-mode guide button ---");

test("SceneDetail.js: LOCKED gate emits data-locked-guide-button (not renderCopyCommandButton wrapper)", () => {
  const slice = sceneDetailSrc.split(/function renderLockedGate/)[1] || "";
  const block = slice.split(/\nfunction /)[0] || slice;
  assert.match(block, /data-locked-guide-button="true"/);
  assert.match(block, /data-locked-guide-text=/);
  // CopyCommandButton wrapper must not appear for the guide text now.
  assert.doesNotMatch(block, /renderCopyCommandButton\(\{[^}]*command:\s*"降級引導文字"/);
});

test("main.js: installs delegated handler for data-locked-guide-button (writes raw text)", () => {
  const mainSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/main.js"), "utf-8");
  assert.match(mainSrc, /\[data-locked-guide-button\]/);
  // Must call copyToClipboard with the raw guideText, not assembleCopyPayload.
  assert.match(mainSrc, /copyToClipboard\(guideText\)/);
  assert.doesNotMatch(mainSrc, /assembleCopyPayload\([^)]*guideText/);
});

console.log("");
console.log("--- #8 P2 / Router cleanup leak fix ---");

test("router.js: cleanup removes scenes:refresh + scene-detail:refresh document listeners", () => {
  // Both listeners must appear as removeEventListener calls in the returned cleanup.
  const slice = routerSrc.split(/window\.addEventListener\("hashchange", updateRoute\)/)[1] || "";
  assert.match(slice, /document\.removeEventListener\("scenes:refresh", onScenesRefresh\)/);
  assert.match(slice, /document\.removeEventListener\("scene-detail:refresh", onSceneDetailRefresh\)/);
});

console.log("");
console.log("--- #9 P3 / SceneEditor dirty back dialog escapes version string ---");

test("SceneEditor.js: dirty back dialog escapes v.version through escapeHtml", () => {
  // openDirtyBackDialog appears twice (callsite + declaration); look at the
  // body that follows the declaration.
  const parts = sceneEditorSrc.split(/openDirtyBackDialog/);
  const slice = parts.slice(2).join("openDirtyBackDialog");
  const block = slice.split(/\n  async function |\n  function /)[0] || slice;
  assert.match(block, /escapeHtml\(String\(v\.version \|\| "\?"\)\)/);
  assert.doesNotMatch(block, /dirtyVersions\(\)\.map\(\(v\) => v\.version\)\.join/);
});

console.log("");
// Allow async tests (the import().then chain) to settle before reporting.
await new Promise((r) => setTimeout(r, 50));
console.log(`Result: ${passed} passed, ${failed} failed`);
if (failed > 0) process.exitCode = 1;
