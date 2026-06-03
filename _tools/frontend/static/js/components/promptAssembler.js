/**
 * promptAssembler — Layer 3 Export Prompt 組裝 (UX_SPEC §11.6.11 + ARCH §4.2a)
 *
 * 嚴格對齊 _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2 contract：
 *   - 必填 5 區塊（依序）：標題 / YAML 元資料 / 步驟 / 約束 / 完成回報
 *   - schema_version 鎖 "1.0"（破壞性改動須升 schema 版號 + 走 master 拍板 D-NNN）
 *   - mode 鎖 "read_only"
 *   - CC-07 校正內化：
 *     * 無 rerun_qa 欄（與 read_only 衝突）
 *     * 新增 include_deleted（預設 false；含 status=deleted dialogue_line 才設 true）
 *     * read_only 約束含「不修改 phase_log」（純 export 不視為 pipeline event）
 *
 * 設計守則：
 *   - pure function — 可 unit test，無 side effect
 *   - prompt 是 contract，任何 LLM endpoint 收到都能跑
 *   - D-029 (α) 完全分離：前端只組 prompt，不執行
 *
 * 公開 API:
 *   assembleExportPrompt(opts) → prompt string
 *   defaultOutputPaths(scope, ts) → { json, md }
 *   PROMPT_SCHEMA_VERSION (constant "1.0")
 */

export const PROMPT_SCHEMA_VERSION = "1.0";
export const PROJECT_ID = "game-dialogue-bible";

const DATA_FORMAT_SPEC_REF = "_design/DATA_FORMAT_SPEC.md §9";
const UPSTREAM_DOWNSTREAM_SPEC_REF = "_design/UPSTREAM_DOWNSTREAM_SPEC.md §12";

/** @typedef {"full"|"outline_only"|"scene"} ScopeType */

/** @typedef {{
 *   type: ScopeType,
 *   sceneId?: string,
 *   entityFilter?: { types?: string[], exclude?: string[] }
 * }} ScopeOpts */

/** @typedef {{
 *   scope: ScopeOpts,
 *   formats?: { json?: boolean, md?: boolean },
 *   includeDeleted?: boolean,
 *   outputPaths?: { json?: string, md?: string },
 *   repoRoot?: string,
 *   timestamp?: Date|string,
 *   stats?: { entities?: any, dialogue_lines?: number, art_assets?: number, qa_reports?: number }
 * }} AssembleOpts */

/**
 * Generate ISO 8601 timestamp with timezone (e.g. "2026-05-22T14:32:00+08:00").
 * @param {Date|string} [ts]
 * @returns {string}
 */
export function formatIsoTimestamp(ts) {
  if (typeof ts === "string" && ts.trim()) return ts.trim();
  const date = ts instanceof Date ? ts : new Date();
  if (Number.isNaN(date.getTime())) return new Date().toISOString();
  const pad = (n) => String(n).padStart(2, "0");
  const tzOffsetMin = -date.getTimezoneOffset();
  const sign = tzOffsetMin >= 0 ? "+" : "-";
  const tzH = pad(Math.floor(Math.abs(tzOffsetMin) / 60));
  const tzM = pad(Math.abs(tzOffsetMin) % 60);
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}T${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}${sign}${tzH}:${tzM}`;
}

/**
 * 預設 output paths — 命名規約：export/<YYYY-MM-DD>_<scope-key>.{json,md}
 * @param {ScopeOpts} scope
 * @param {Date|string} [ts]
 * @returns {{json: string, md: string}}
 */
export function defaultOutputPaths(scope, ts) {
  const date = ts instanceof Date ? ts : (typeof ts === "string" && ts.trim() ? new Date(ts) : new Date());
  const pad = (n) => String(n).padStart(2, "0");
  const dateStr = `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
  let key = "full";
  if (scope.type === "outline_only") key = "outline";
  else if (scope.type === "scene" && scope.sceneId) key = `scene_${scope.sceneId}`;
  return {
    json: `export/${dateStr}_${key}.json`,
    md: `export/${dateStr}_${key}.md`,
  };
}

/**
 * 組 prompt — 嚴格按 §1.1 5 區塊。
 * @param {AssembleOpts} opts
 * @returns {string}
 */
export function assembleExportPrompt(opts = {}) {
  if (!opts || typeof opts !== "object") {
    throw new Error("assembleExportPrompt: opts is required");
  }
  const scope = opts.scope;
  if (!scope || typeof scope !== "object" || !scope.type) {
    throw new Error("assembleExportPrompt: scope.type is required");
  }
  if (!["full", "outline_only", "scene"].includes(scope.type)) {
    // Phase A.0F.patch-major-2 / L3 schema drift: schema v0.2 §1.2 enumerates
    // only full / outline_only / scene. `chapter` is rejected until a future
    // schema bump (CODEX Major finding §3).
    throw new Error(`assembleExportPrompt: invalid scope.type "${scope.type}" — schema v0.2 only allows full | outline_only | scene`);
  }
  if (scope.type === "scene" && !scope.sceneId) {
    throw new Error("assembleExportPrompt: scope.sceneId required when scope.type=scene");
  }

  const formats = {
    json: opts.formats?.json !== false,  // default true
    md: opts.formats?.md !== false,       // default true
  };
  if (!formats.json && !formats.md) {
    throw new Error("assembleExportPrompt: at least one format (json or md) must be enabled");
  }

  const includeDeleted = opts.includeDeleted === true;
  const repoRoot = opts.repoRoot || "D:\\劇本開發工具";
  const timestamp = formatIsoTimestamp(opts.timestamp);
  const outputPaths = {
    json: opts.outputPaths?.json || defaultOutputPaths(scope, opts.timestamp).json,
    md: opts.outputPaths?.md || defaultOutputPaths(scope, opts.timestamp).md,
  };
  // Phase A.0F.patch-major-2 / L3 schema drift: schema v0.2 §1.4 requires
  // output_paths to live under repo_root/export/. Reject any custom path that
  // leaves the export/ root. CODEX Major finding §3 §8 #5.
  assertExportPath(outputPaths.json, "outputPaths.json");
  assertExportPath(outputPaths.md, "outputPaths.md");
  const stats = opts.stats || null;

  const dateLabel = timestamp.slice(0, 16).replace("T", " ");
  const projectId = PROJECT_ID;

  // ============ 區塊 1：標題 ============
  const title = `# Layer 3 Export Task — ${projectId} — ${dateLabel}`;

  // ============ 區塊 2：YAML 元資料 ============
  const yamlLines = [
    "---",
    `schema_version: "${PROMPT_SCHEMA_VERSION}"`,
    `project_id: "${projectId}"`,
    `repo_root: ${jsonScalar(repoRoot)}`,
    `timestamp: "${timestamp}"`,
    ``,
    `scope:`,
    `  type: "${scope.type}"`,
  ];
  if (scope.type === "scene") {
    yamlLines.push(`  scene_id: "${scope.sceneId}"`);
  } else {
    yamlLines.push(`  scene_id: null`);
  }
  if (scope.entityFilter) {
    yamlLines.push(`  entity_filter:`);
    if (Array.isArray(scope.entityFilter.types) && scope.entityFilter.types.length) {
      yamlLines.push(`    types: [${scope.entityFilter.types.map(jsonScalar).join(", ")}]`);
    }
    if (Array.isArray(scope.entityFilter.exclude) && scope.entityFilter.exclude.length) {
      yamlLines.push(`    exclude: [${scope.entityFilter.exclude.map(jsonScalar).join(", ")}]`);
    }
  }
  yamlLines.push(``);
  yamlLines.push(`formats:`);
  yamlLines.push(`  json: ${formats.json ? "true" : "false"}`);
  yamlLines.push(`  md: ${formats.md ? "true" : "false"}`);
  yamlLines.push(`  # v0.2 master 第四輪 CC-07 校正：rerun_qa 欄位移除`);
  yamlLines.push(`  # 理由：read_only mode 禁止執行 /qa；rerun_qa 屬 pipeline action 跟 read_only 衝突`);
  yamlLines.push(``);
  yamlLines.push(`include_deleted: ${includeDeleted ? "true" : "false"}  # v0.2 CC-07 — 含 status: deleted 的 dialogue_line？預設 false`);
  yamlLines.push(``);
  yamlLines.push(`output_paths:`);
  yamlLines.push(`  json: ${jsonScalar(outputPaths.json)}`);
  yamlLines.push(`  md: ${jsonScalar(outputPaths.md)}`);
  yamlLines.push(``);
  yamlLines.push(`mode: "read_only"  # 鎖死 — agent 看到 mode != "read_only" 一律拒跑`);
  yamlLines.push(``);
  yamlLines.push(`contract_refs:`);
  yamlLines.push(`  data_format_spec: "${DATA_FORMAT_SPEC_REF}"`);
  yamlLines.push(`  upstream_downstream_spec: "${UPSTREAM_DOWNSTREAM_SPEC_REF}"`);
  if (stats) {
    yamlLines.push(``);
    yamlLines.push(`# 前端產 prompt 時抓到的 scope counts（agent 完成後應對齊）：`);
    if (stats.entities) yamlLines.push(`# entities: ${JSON.stringify(stats.entities)}`);
    if (typeof stats.dialogue_lines === "number") yamlLines.push(`# dialogue_lines: ${stats.dialogue_lines}`);
    if (typeof stats.art_assets === "number") yamlLines.push(`# art_assets: ${stats.art_assets}`);
    if (typeof stats.qa_reports === "number") yamlLines.push(`# qa_reports: ${stats.qa_reports}`);
  }
  yamlLines.push("---");
  const yamlBlock = yamlLines.join("\n");

  // ============ 區塊 3：執行步驟（標準 5 步驟，§1.3） ============
  const steps = [
    "## 執行步驟 / Steps",
    "",
    "1. 讀 contract_refs 中指向的 DATA_FORMAT_SPEC §9（manifest + records[] schema）。",
    "2. 依 scope 掃描 repo_root 下所有相關 entity 檔（W/V/C/R/P/CH/S/A-*）。",
    `   - scope.type=full：所有 entity`,
    `   - scope.type=outline_only：W-rules + W-language + V + C-* + R-*-* + P + CH-*`,
    `   - scope.type=scene：僅該 scene_id 與其 depends_on`,
    "3. 依 §9.2 寫 manifest header（entity_type_registry / qa_type_registry snapshot + scope + counts）。",
    "4. 依 §9.3-§9.6 將每筆轉為 records[]：",
    "   - frontmatter → record fields",
    "   - 內文（保留段落結構）→ record.body",
    "   - dialogue 檔的 dialogue_keys block 完整保留",
    `5. 寫 ${formats.json ? "JSON" : ""}${formats.json && formats.md ? " + " : ""}${formats.md ? "MD" : ""} 到 ${formats.json ? `output_paths.json (${outputPaths.json})` : ""}${formats.json && formats.md ? " + " : ""}${formats.md ? `output_paths.md (${outputPaths.md})` : ""}。`,
    "6. 完成回報（見 §完成回報 段）。",
  ];
  const stepsBlock = steps.join("\n");

  // ============ 區塊 4：約束規則（§1.4） ============
  const constraints = [
    "## 約束規則 / Constraints (read_only mode — strict, do not violate)",
    "",
    "- `read_only: true` → 不得改動任何 source entity 檔（W/V/C/R/P/CH/S/A-* 全 read-only）",
    `- output_paths 限定 ${repoRoot}/export/ 下，不可寫到其他目錄`,
    "- 不執行任何 /create-* /dialogue-write /qa /scene-task 等 skill",
    "- **不修改 phase_log，不寫入任何 phase_log entry**（v0.2 CC-07 校正 — export 不 append `phase: export` 紀錄；Layer 3 Export 純 read-only，不視為 pipeline event）",
    "- 不升級任何狀態（狀態機由人類控制）",
    "- 不刪除任何檔案（即使是過期 export 也不動）",
    "- 若遇到無法讀的檔（loop / permission），記入 export warnings，不阻塞整體",
    `- mode != "read_only" 的 prompt 一律拒跑（檢查到 mode 不是 read_only 就 return error）`,
    `- 已有 status: deleted 的 dialogue_line：${includeDeleted ? "**含**於 JSON records[]（include_deleted=true）" : "**不**含（預設 include_deleted=false）"}`,
  ];
  const constraintsBlock = constraints.join("\n");

  // ============ 區塊 5：完成回報格式（§1.5） ============
  // Bug 1 fix (audit-P1): 用 __SKIP__ marker 區分「條件式 skip」vs「刻意空行」
  // 原 `filter(line => line !== "")` 會把 markdown 區塊間刻意保留的空行也濾掉，
  // 破壞 §1.5 完成回報區塊的可讀結構。
  const SKIP = "__SKIP__";
  const completion = [
    "## 完成回報 / Completion Report",
    "",
    "完成後必須在 chat 回覆下列 JSON：",
    "",
    "```json",
    "{",
    `  "schema_version": "${PROMPT_SCHEMA_VERSION}",`,
    `  "project_id": "${projectId}",`,
    `  "export_id": "<agent 生成的 UUID>",`,
    `  "timestamp_completed": "<ISO 8601>",`,
    `  "output_paths": {`,
    formats.json ? `    "json": { "path": "${outputPaths.json}", "size_bytes": <N>, "absolute_path": "<repo_root + path>" }${formats.md ? "," : ""}` : SKIP,
    formats.md ? `    "md":   { "path": "${outputPaths.md}",   "size_bytes": <N>, "absolute_path": "<repo_root + path>" }` : SKIP,
    `  },`,
    `  "records_total": <N>,`,
    `  "records_by_type": { "entity": <N>, "dialogue_line": <N>, "art_metadata": <N> },`,
    `  "entities_scanned": <N>,`,
    `  "warnings": [`,
    `    { "path": "<rel>", "reason": "<text>" }`,
    `  ],`,
    `  "runtime_seconds": <N>`,
    "}",
    "```",
    "",
    `必要欄位：output_paths / records_total / records_by_type / entities_scanned / warnings / runtime_seconds / export_id`,
  ];
  const completionBlock = completion.filter((line) => line !== SKIP).join("\n");

  // 組合
  return [title, "", yamlBlock, "", stepsBlock, "", constraintsBlock, "", completionBlock].join("\n");
}

function jsonScalar(value) {
  if (typeof value !== "string") return JSON.stringify(value);
  // YAML scalar — 用 JSON-style 雙引號（YAML 1.2 兼容）
  return JSON.stringify(value);
}

/**
 * Phase A.0F.patch-major-2: enforce `output_paths` 必須以 `export/` 為前綴。
 *
 * L3_EXPORT_PROMPT_SCHEMA v0.2 §1.4：「output_paths 限定 repo_root/export/
 * 下，不可寫到其他目錄」。schema 是 LOCKED contract，未升 schema_version
 * 不允許 export 寫出 export/ 之外。
 *
 * 拒絕：絕對路徑、含 `..` segment、不以 `export/` 開頭。
 *
 * @param {string} value
 * @param {string} field
 */
function assertExportPath(value, field) {
  if (typeof value !== "string" || !value.trim()) {
    throw new Error(`assembleExportPrompt: ${field} must be a non-empty string`);
  }
  const norm = value.replace(/\\/g, "/").trim();
  if (norm.startsWith("/")) {
    throw new Error(`assembleExportPrompt: ${field} must be repo-relative (got absolute: ${value})`);
  }
  if (norm.split("/").includes("..")) {
    throw new Error(`assembleExportPrompt: ${field} must not contain '..' segments (got: ${value})`);
  }
  if (!norm.startsWith("export/")) {
    throw new Error(`assembleExportPrompt: ${field} must start with 'export/' per L3 schema v0.2 §1.4 (got: ${value})`);
  }
}
