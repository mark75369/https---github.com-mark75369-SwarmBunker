/**
 * D-046 #5 / C-16 / O-03 — LOCKED 降級引導文字 anchor lock
 *
 * 跑法：
 *   node _tools/frontend/tests/sceneeditor_guide.test.mjs
 *
 * 嚴守規約：buildDowngradeGuide (SceneEditor.js) 跟 renderLockedGate (SceneDetail.js)
 * 兩處 LOCKED 降級引導文字必須**明示**：
 *   1. 不要新增 frontmatter 欄位
 *   2. 降級理由 / 降級日期 / 降級人 三欄位**不**寫到 frontmatter
 *   3. 三欄位**寫到** 09_e 紀錄
 *   4. frontmatter 只改一行 `狀態：DEPRECATED`
 *
 * 若這些 anchor 字串被改掉，會破壞 D-046 #5 / C-16 / O-03 守則，
 * 引導 user 寫不合法的 frontmatter。本 test 就是 regression 鎖。
 *
 * 對齊：
 *   - _design/DECISIONS_LOG.md D-046 #5
 *   - CODEX C-16 / O-03
 *   - _design/SPEC.md §5.2 canonical schema（不認的欄位不該加）
 *   - _design/SPEC.md §16 文件狀態機（人類控狀態）
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
    fn();
    passed += 1;
    console.log(`  ✓ ${name}`);
  } catch (err) {
    failed += 1;
    console.error(`  ✗ ${name}`);
    console.error(err instanceof Error ? err.stack : err);
  }
}

const sceneEditorSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/SceneEditor.js"), "utf-8");
const sceneDetailSrc = readFileSync(resolve(FRONTEND_ROOT, "static/js/pages/SceneDetail.js"), "utf-8");

console.log("D-046 #5 / C-16 / O-03 — LOCKED 降級引導文字 anchor lock");
console.log("");
console.log("Source 1: SceneEditor.js buildDowngradeGuide()");

test("SceneEditor: must have `buildDowngradeGuide` function", () => {
  assert.match(sceneEditorSrc, /function buildDowngradeGuide\s*\(/);
});

test("SceneEditor: anchor 「不新增 frontmatter 欄位」存在", () => {
  assert.match(sceneEditorSrc, /不新增 frontmatter 欄位/);
});

test("SceneEditor: anchor 「不要新增「降級理由」「降級日期」「降級人」等欄位」存在", () => {
  assert.match(sceneEditorSrc, /不要新增「降級理由」「降級日期」「降級人」等欄位/);
});

test("SceneEditor: anchor 「09_e」紀錄路徑存在", () => {
  assert.match(sceneEditorSrc, /09_e_定稿變更紀錄\.md/);
});

test("SceneEditor: anchor 「狀態：LOCKED.*→.*狀態：DEPRECATED」 only-change-one-line 存在", () => {
  assert.match(sceneEditorSrc, /狀態：LOCKED.*→.*狀態：DEPRECATED/);
});

test("SceneEditor: anchor「狀態：DEPRECATED.*一行.*不擅自加 schema 不認的欄位」存在", () => {
  assert.match(sceneEditorSrc, /狀態：DEPRECATED.*一行.*不擅自加 schema 不認的欄位/);
});

test("SceneEditor: D-046 #5 / C-16 / O-03 三拍板編號全引用", () => {
  assert.match(sceneEditorSrc, /D-046 #5/);
  assert.match(sceneEditorSrc, /C-16/);
  assert.match(sceneEditorSrc, /O-03/);
});

test("SceneEditor: D-031 不新增 skill 拍板被引用（防 /deprecate-scene 之類擅自加 skill）", () => {
  assert.match(sceneEditorSrc, /D-031/);
});

test("SceneEditor: SPEC §16 文件狀態升級限制原則引用", () => {
  assert.match(sceneEditorSrc, /SPEC §16/);
});

test("SceneEditor: code path 無 patch_frontmatter_field 直接調用降級理由欄位的危險邏輯", () => {
  assert.doesNotMatch(sceneEditorSrc, /patch_frontmatter_field\([^)]*降級理由/);
  assert.doesNotMatch(sceneEditorSrc, /patch_frontmatter_field\([^)]*降級日期/);
  assert.doesNotMatch(sceneEditorSrc, /patch_frontmatter_field\([^)]*降級人/);
});

console.log("");
console.log("Source 2: SceneDetail.js renderLockedGate()");

test("SceneDetail: must have `renderLockedGate` function", () => {
  assert.match(sceneDetailSrc, /function renderLockedGate\s*\(/);
});

test("SceneDetail: anchor 「不新增 frontmatter 欄位」存在", () => {
  assert.match(sceneDetailSrc, /不新增 frontmatter 欄位/);
});

test("SceneDetail: anchor 「不要新增「降級理由」「降級日期」「降級人」等欄位」存在", () => {
  assert.match(sceneDetailSrc, /不要新增「降級理由」「降級日期」「降級人」等欄位/);
});

test("SceneDetail: anchor 「09_e」 紀錄路徑存在", () => {
  assert.match(sceneDetailSrc, /09_e_定稿變更紀錄\.md/);
});

test("SceneDetail: anchor 「狀態：LOCKED.*→.*狀態：DEPRECATED」 存在", () => {
  assert.match(sceneDetailSrc, /狀態：LOCKED.*→.*狀態：DEPRECATED/);
});

test("SceneDetail: anchor 「不在 SPEC §5.2 canonical schema 內」 存在", () => {
  assert.match(sceneDetailSrc, /不在 SPEC §5\.2 canonical schema 內/);
});

test("SceneDetail: D-031 引用", () => {
  assert.match(sceneDetailSrc, /D-031/);
});

test("SceneDetail: 完整降級紀錄段含「降級理由」「降級日期」「降級人」（指引到 09_e 寫，不是 frontmatter）", () => {
  // 三欄位都必須在引導文字內出現（讓 user 知道要紀錄這些）
  assert.match(sceneDetailSrc, /降級理由/);
  assert.match(sceneDetailSrc, /降級日期/);
  assert.match(sceneDetailSrc, /降級人/);
});

console.log("");
console.log(`Result: ${passed} passed, ${failed} failed`);

if (failed > 0) {
  process.exitCode = 1;
}
