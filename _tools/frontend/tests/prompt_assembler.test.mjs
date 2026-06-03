/**
 * promptAssembler — Schema contract smoke test
 *
 * 跑法：
 *   node _tools/frontend/tests/prompt_assembler.test.mjs
 *
 * 嚴守 _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2 contract — 任一 test fail
 * 代表前端組的 prompt 不再符合 schema，會破壞外部 agent 解析。
 *
 * 對齊 CC-07 校正：
 *   - 無 rerun_qa 欄
 *   - 含 include_deleted（預設 false）
 *   - read_only 約束含「不修改 phase_log」
 */

import assert from "node:assert/strict";
import {
  assembleExportPrompt,
  defaultOutputPaths,
  formatIsoTimestamp,
  PROMPT_SCHEMA_VERSION,
  PROJECT_ID,
} from "../static/js/components/promptAssembler.js";

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

console.log("promptAssembler — assembleExportPrompt schema contract");

// ============ 必填區塊存在 ============

test("constants are stable (schema_version, project_id)", () => {
  assert.equal(PROMPT_SCHEMA_VERSION, "1.0");
  assert.equal(PROJECT_ID, "game-dialogue-bible");
});

test("scope=full minimum payload — 5 sections all present in order", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  // §1.1 必填區塊（依序）
  const sections = [
    "# Layer 3 Export Task —",        // 1 標題
    `schema_version: "${PROMPT_SCHEMA_VERSION}"`,  // 2 YAML 元資料開頭
    "## 執行步驟 / Steps",            // 3 執行步驟
    "## 約束規則 / Constraints",       // 4 約束
    "## 完成回報 / Completion Report", // 5 完成回報
  ];
  let lastIdx = -1;
  for (const s of sections) {
    const idx = prompt.indexOf(s);
    assert.ok(idx > -1, `section "${s}" missing`);
    assert.ok(idx > lastIdx, `section "${s}" out of order`);
    lastIdx = idx;
  }
});

// ============ YAML 元資料 schema ============

test("YAML metadata has required keys (schema_version / project_id / repo_root / timestamp / scope / formats / include_deleted / output_paths / mode / contract_refs)", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  for (const key of [
    `schema_version: "${PROMPT_SCHEMA_VERSION}"`,
    `project_id: "${PROJECT_ID}"`,
    "repo_root:",
    "timestamp:",
    "scope:",
    "formats:",
    "include_deleted:",
    "output_paths:",
    `mode: "read_only"`,
    "contract_refs:",
    "data_format_spec:",
    "upstream_downstream_spec:",
  ]) {
    assert.ok(prompt.includes(key), `YAML must include key: "${key}"`);
  }
});

test("CC-07: NO rerun_qa field in YAML", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.doesNotMatch(prompt, /rerun_qa\s*:/, "rerun_qa field must not appear (CC-07)");
});

test("CC-07: include_deleted defaults to false", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /include_deleted:\s*false/);
});

test("CC-07: include_deleted=true is honored", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, includeDeleted: true, timestamp: new Date() });
  assert.match(prompt, /include_deleted:\s*true/);
});

test("CC-07: constraints include 'do not modify phase_log'", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /不修改 phase_log|不寫入任何 phase_log entry/);
});

test("mode is locked to read_only", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /mode:\s*"read_only"/);
  assert.match(prompt, /mode\s*!=\s*"read_only".*拒跑/);
});

// ============ scope 變體 ============

test("scope=scene requires sceneId", () => {
  assert.throws(
    () => assembleExportPrompt({ scope: { type: "scene" } }),
    /sceneId required/,
  );
});

test("scope=scene with sceneId — YAML scene_id populated + scene-specific step text", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "scene", sceneId: "S-01-03" },
    timestamp: new Date(),
  });
  assert.match(prompt, /scene_id:\s*"S-01-03"/);
  assert.match(prompt, /scope\.type=scene：僅該 scene_id 與其 depends_on/);
});

test("scope=full has scene_id: null", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /scene_id:\s*null/);
});

// Phase A.0F.patch-major-2 / L3 schema drift: chapter scope was removed because
// L3_EXPORT_PROMPT_SCHEMA v0.2 §1.2 enumerates only full / outline_only / scene.
// The previous two tests (now superseded below) locked the drift instead of
// the schema — replaced with positive rejection tests.
test("scope=chapter is rejected (schema v0.2 only allows full | outline_only | scene)", () => {
  assert.throws(
    () => assembleExportPrompt({ scope: { type: "chapter", chapter: "01" } }),
    /invalid scope\.type.*schema v0\.2/,
  );
});

test("output_paths outside export/ are rejected (L3 schema v0.2 §1.4)", () => {
  assert.throws(
    () => assembleExportPrompt({
      scope: { type: "full" },
      outputPaths: { json: "tmp/out.json", md: "export/ok.md" },
    }),
    /outputPaths\.json must start with 'export\/'/,
  );
  assert.throws(
    () => assembleExportPrompt({
      scope: { type: "full" },
      outputPaths: { json: "export/ok.json", md: "../escape.md" },
    }),
    /outputPaths\.md.*must not contain '\.\.'/,
  );
  assert.throws(
    () => assembleExportPrompt({
      scope: { type: "full" },
      outputPaths: { json: "/abs/out.json", md: "export/ok.md" },
    }),
    /outputPaths\.json must be repo-relative/,
  );
});

test("scope=outline_only emits outline-specific step text", () => {
  const prompt = assembleExportPrompt({ scope: { type: "outline_only" }, timestamp: new Date() });
  assert.match(prompt, /scope\.type=outline_only：W-rules \+ W-language \+ V/);
});

test("rejects invalid scope.type", () => {
  assert.throws(
    () => assembleExportPrompt({ scope: { type: "wat" } }),
    /invalid scope\.type/,
  );
});

// ============ formats ============

test("formats both default to true", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /json:\s*true/);
  assert.match(prompt, /md:\s*true/);
});

test("formats=json only", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    formats: { json: true, md: false },
    timestamp: new Date(),
  });
  assert.match(prompt, /json:\s*true/);
  assert.match(prompt, /md:\s*false/);
  // step 5 wording only JSON (no "+ MD")
  assert.match(prompt, /5\. 寫 JSON 到 output_paths\.json/);
  assert.doesNotMatch(prompt, /5\. 寫 JSON \+ MD/);
});

test("rejects when both formats are false", () => {
  assert.throws(
    () => assembleExportPrompt({
      scope: { type: "full" },
      formats: { json: false, md: false },
    }),
    /at least one format/,
  );
});

// ============ output_paths ============

test("defaultOutputPaths produces expected pattern for scope=full", () => {
  const ts = new Date(2026, 4, 22);
  const paths = defaultOutputPaths({ type: "full" }, ts);
  assert.equal(paths.json, "export/2026-05-22_full.json");
  assert.equal(paths.md, "export/2026-05-22_full.md");
});

test("defaultOutputPaths for scene includes scene_id", () => {
  const ts = new Date(2026, 4, 22);
  const paths = defaultOutputPaths({ type: "scene", sceneId: "S-01-03" }, ts);
  assert.equal(paths.json, "export/2026-05-22_scene_S-01-03.json");
});

test("custom output_paths override defaults", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    outputPaths: { json: "export/custom.json", md: "export/custom.md" },
    timestamp: new Date(),
  });
  assert.match(prompt, /json:\s*"export\/custom\.json"/);
  assert.match(prompt, /md:\s*"export\/custom\.md"/);
});

// ============ contract refs ============

test("contract_refs includes DATA_FORMAT_SPEC + UPSTREAM_DOWNSTREAM_SPEC", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /data_format_spec:\s*"_design\/DATA_FORMAT_SPEC\.md §9"/);
  assert.match(prompt, /upstream_downstream_spec:\s*"_design\/UPSTREAM_DOWNSTREAM_SPEC\.md §12"/);
});

// ============ Completion report ============

test("completion report has all required fields", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  for (const key of [
    "schema_version",
    "project_id",
    "export_id",
    "timestamp_completed",
    "output_paths",
    "records_total",
    "records_by_type",
    "entities_scanned",
    "warnings",
    "runtime_seconds",
  ]) {
    assert.match(prompt, new RegExp(`"${key}"`), `completion report must include "${key}"`);
  }
});

// ============ Constraints ============

test("constraints list: read_only / output limit / skill ban / no state upgrade / no delete", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  assert.match(prompt, /read_only: true/);
  assert.match(prompt, /output_paths 限定.*\/export\//);
  assert.match(prompt, /不執行任何 \/create-\*.*\/dialogue-write.*\/qa.*\/scene-task/);
  assert.match(prompt, /不升級任何狀態/);
  assert.match(prompt, /不刪除任何檔案/);
});

// ============ Stats injection ============

test("stats from /api/scope-counts injected as comments", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    timestamp: new Date(),
    stats: {
      entities: { S: 26, C: 7 },
      dialogue_lines: 1234,
      art_assets: 87,
      qa_reports: 12,
    },
  });
  assert.match(prompt, /# entities: \{"S":26,"C":7\}/);
  assert.match(prompt, /# dialogue_lines: 1234/);
  assert.match(prompt, /# art_assets: 87/);
  assert.match(prompt, /# qa_reports: 12/);
});

// ============ Timestamp formatting ============

test("formatIsoTimestamp produces ISO 8601 with timezone", () => {
  const ts = formatIsoTimestamp(new Date(2026, 4, 22, 14, 32, 0));
  assert.match(ts, /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$/);
});

test("formatIsoTimestamp accepts string passthrough", () => {
  assert.equal(formatIsoTimestamp("2026-05-22T14:32:00+08:00"), "2026-05-22T14:32:00+08:00");
});

// ============ Title format ============

test("title format: '# Layer 3 Export Task — <project> — YYYY-MM-DD HH:MM'", () => {
  const ts = new Date(2026, 4, 22, 14, 32, 0);
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: ts });
  const firstLine = prompt.split("\n", 1)[0];
  assert.match(firstLine, /^# Layer 3 Export Task — game-dialogue-bible — 2026-05-22 14:32$/);
});

// ============ Bug 1 regression — markdown 空行結構保留 ============
// 防 promptAssembler.js completion 區塊空行被誤過濾（audit-P1 Bug 1）regression。
// 若有人改回 \`filter(line => line !== "")\` 不用 SKIP marker，這些 test 會炸。

test("Bug 1 regression: completion section preserves blank line between heading and intro", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  // 標題 ## 完成回報 後須有空行才到「完成後必須在 chat 回覆下列 JSON：」
  assert.match(prompt, /## 完成回報 \/ Completion Report\n\n完成後必須在 chat 回覆下列 JSON：/);
});

test("Bug 1 regression: blank line between intro and JSON fence opener", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  // 「完成後必須在 chat 回覆下列 JSON：」 後須有空行才到 ```json
  assert.match(prompt, /完成後必須在 chat 回覆下列 JSON：\n\n```json/);
});

test("Bug 1 regression: blank line between JSON fence closer and 必要欄位 footer", () => {
  const prompt = assembleExportPrompt({ scope: { type: "full" }, timestamp: new Date() });
  // ``` 後須有空行才到「必要欄位：...」
  assert.match(prompt, /```\n\n必要欄位：/);
});

test("Bug 1 regression: formats=json only — no `__SKIP__` marker leaks into output", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    formats: { json: true, md: false },
    timestamp: new Date(),
  });
  assert.doesNotMatch(prompt, /__SKIP__/, "SKIP sentinel must not leak into output");
  // 還是要保留 markdown 空行結構
  assert.match(prompt, /## 完成回報[^\n]*\n\n完成後/);
  assert.match(prompt, /```\n\n必要欄位/);
});

test("Bug 1 regression: formats=md only — no `__SKIP__` marker leaks", () => {
  const prompt = assembleExportPrompt({
    scope: { type: "full" },
    formats: { json: false, md: true },
    timestamp: new Date(),
  });
  assert.doesNotMatch(prompt, /__SKIP__/);
  assert.match(prompt, /## 完成回報[^\n]*\n\n完成後/);
});

console.log("");
console.log(`Result: ${passed} passed, ${failed} failed`);

if (failed > 0) {
  process.exitCode = 1;
}
