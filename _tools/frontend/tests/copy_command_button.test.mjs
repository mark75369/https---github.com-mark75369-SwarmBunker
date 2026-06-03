/**
 * CopyCommandButton — pure function smoke test
 *
 * 跑法（在 D:/劇本開發工具 根目錄或本 tests/ 目錄）：
 *   node _tools/frontend/tests/copy_command_button.test.mjs
 *
 * 對應 UX_SPEC §11.6.3 剪貼簿格式規範驗證。
 * 不需要任何測試 framework；用 Node 內建 `assert`。
 */

import assert from "node:assert/strict";

import {
  assembleCopyPayload,
  COPY_MARKER_OPEN,
  COPY_MARKER_CLOSE,
} from "../static/js/components/CopyCommandButton.js";

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

console.log("CopyCommandButton — assembleCopyPayload");

test("minimum payload — only command", () => {
  const text = assembleCopyPayload({
    command: "/qa S-01-03",
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  assert.ok(text.startsWith(COPY_MARKER_OPEN), "starts with marker");
  assert.ok(text.endsWith(COPY_MARKER_CLOSE), "ends with marker");
  assert.match(text, /指令：/);
  assert.match(text, /\/qa S-01-03/);
  assert.match(text, /來源：/);
  // 不該出現「已有 Context 摘要」「相關檔案引用」「備註」段
  assert.doesNotMatch(text, /已有 Context 摘要/);
  assert.doesNotMatch(text, /相關檔案引用/);
  assert.doesNotMatch(text, /備註/);
});

test("full payload — all 5 sections in correct order", () => {
  const text = assembleCopyPayload({
    command: "/dialogue-write S-01-03",
    contextSummary: "W-rules 14/27\nC-主角A 聲線卡狀態：REVIEW",
    contextRefs: ["/01_world/01_a_世界觀總覽.md", "/03_characters/main/主角A_聲線卡.md"],
    contextNotes: "本場 v01A trial 後預期跑 single-iter convergence。",
    source: "Scene Detail S-01-03",
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  // 依序 5 段
  const sectionOrder = ["指令：", "已有 Context 摘要：", "相關檔案引用：", "備註：", "來源："];
  let lastIdx = -1;
  for (const section of sectionOrder) {
    const idx = text.indexOf(section);
    assert.ok(idx > -1, `section "${section}" must exist`);
    assert.ok(idx > lastIdx, `section "${section}" must follow previous section`);
    lastIdx = idx;
  }
  // contextSummary 多行自動加 `- ` prefix
  assert.match(text, /- W-rules 14\/27/);
  assert.match(text, /- C-主角A 聲線卡狀態：REVIEW/);
  // contextRefs 加 `- ` prefix
  assert.match(text, /- \/01_world\/01_a_世界觀總覽\.md/);
  assert.match(text, /- \/03_characters\/main\/主角A_聲線卡\.md/);
  // source 段含時間戳
  assert.match(text, /前端工具 \/ Scene Detail S-01-03 \/ 2026-05-22 14:32/);
});

test("rejects missing command", () => {
  assert.throws(
    () => assembleCopyPayload({}),
    /command is required/,
  );
  assert.throws(
    () => assembleCopyPayload({ command: "" }),
    /command is required/,
  );
  assert.throws(
    () => assembleCopyPayload({ command: "   " }),
    /command is required/,
  );
});

test("trims whitespace on command", () => {
  const text = assembleCopyPayload({
    command: "  /qa S-01-03  ",
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  // 不應留下前後空白
  assert.match(text, /\n  \/qa S-01-03\n/);
});

test("empty arrays / strings are ignored (not rendered as empty sections)", () => {
  const text = assembleCopyPayload({
    command: "/qa S-01-03",
    contextSummary: "",
    contextRefs: [],
    contextNotes: "",
    source: "",
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  assert.doesNotMatch(text, /已有 Context 摘要/);
  assert.doesNotMatch(text, /相關檔案引用/);
  assert.doesNotMatch(text, /備註/);
  // source 空時 fallback「未指定來源」
  assert.match(text, /前端工具 \/ 未指定來源 \//);
});

test("contextRefs filters out non-string / empty entries", () => {
  const text = assembleCopyPayload({
    command: "/qa S-01-03",
    contextRefs: ["/path/a.md", "", null, undefined, "  ", "/path/b.md"],
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  assert.match(text, /- \/path\/a\.md/);
  assert.match(text, /- \/path\/b\.md/);
  // 不該出現「- 」獨立行（空項被濾掉）
  const lines = text.split("\n");
  const refLines = lines.filter((line) => line.startsWith("- ") || line.startsWith("- /"));
  assert.equal(refLines.length, 2, "exactly 2 valid refs");
});

test("contextSummary preserves existing bullet prefix", () => {
  const text = assembleCopyPayload({
    command: "/qa S-01-03",
    contextSummary: "- 已有 bullet\n• 替代 bullet",
    timestamp: new Date(2026, 4, 22, 14, 32, 0),
  });
  // 既有 bullet 不該被再加一次 `- `
  assert.match(text, /\n- 已有 bullet\n/);
  // 既有 • bullet 不該被加 `- `
  assert.match(text, /\n• 替代 bullet\n/);
  // 不應出現雙 prefix
  assert.doesNotMatch(text, /- - 已有/);
  assert.doesNotMatch(text, /- • 替代/);
});

test("markers are stable strings (snapshot)", () => {
  assert.equal(COPY_MARKER_OPEN, "─── [前端工具產生] ───");
  assert.equal(COPY_MARKER_CLOSE, "─── /[前端工具產生] ───");
});

test("timestamp accepts string passthrough", () => {
  const text = assembleCopyPayload({
    command: "/qa S-01-03",
    timestamp: "2026-05-22 (custom format)",
  });
  assert.match(text, /\/ 2026-05-22 \(custom format\)$/m);
});

test("timestamp defaults to current time when omitted", () => {
  const text = assembleCopyPayload({ command: "/qa S-01-03" });
  // 應 match YYYY-MM-DD HH:MM 格式（不檢具體值）
  assert.match(text, /\/ \d{4}-\d{2}-\d{2} \d{2}:\d{2}$/m);
});

console.log("");
console.log(`Result: ${passed} passed, ${failed} failed`);

if (failed > 0) {
  process.exitCode = 1;
}
