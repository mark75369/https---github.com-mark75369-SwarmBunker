import { dashboardData$, state } from "../state.js";
import { renderCopyCommandButton } from "./CopyCommandButton.js";

// Phase A.0F.patch-major-1 / D-045: A-* art assets are tracked in the
// dedicated Asset Panel (§11.1.6a) and MUST NOT appear in narrative Module
// Status. The previous row mixed art completeness into the narrative readiness
// view — CODEX Major finding. Asset progress remains accessible via
// renderAssetPanel() below.
// viewCommand: NEW_REQ_20 F1-2 — 各模組對應的 /view-* skill 指令（11th master
// frontend cycle）。7 模組 → 4 view skill（W/V→world、C/R→character、P→outline、
// CH/S→detailed-outline）。帶 <name> / <CH-ID> 者複製為指令模板由 user 填參數。
const ENTITY_MODULES = [
  { key: "W", label: "W", module: "世界觀 / World", sources: ["W", "W-rules", "W-language"], viewCommand: "/view-world" },
  { key: "V", label: "V", module: "聲線 / Voice Bible", sources: ["V"], viewCommand: "/view-world" },
  { key: "C", label: "C", module: "角色 / Characters", sources: ["C"], viewCommand: "/view-character <name>" },
  { key: "R", label: "R", module: "關係 / Relationships", sources: ["R"], viewCommand: "/view-character <name>" },
  { key: "P", label: "P", module: "劇情前提 / Premise", sources: ["P"], viewCommand: "/view-outline" },
  { key: "CH", label: "CH", module: "章節 / Chapters", sources: ["CH"], viewCommand: "/view-detailed-outline" },
  { key: "S", label: "S", module: "場景 / Scenes", sources: ["S"], viewCommand: "/view-detailed-outline" },
];

const ASSET_SUBTYPES = [
  { key: "portrait", label: "portrait（立繪）" },
  { key: "bg", label: "bg（背景）" },
  { key: "cg", label: "cg（事件圖）" },
  { key: "sfx", label: "sfx（音效）" },
  { key: "bgm", label: "bgm（背景音樂）" },
  { key: "voice", label: "voice（配音）" },
  { key: "ui", label: "ui（UI 文案）" },
];

/**
 * @typedef {Object} DashboardData
 * @property {any} scopeCounts
 * @property {any} assets
 * @property {boolean} loading
 * @property {string|null} error
 * @property {string|null} refreshedAt
 */

/**
 * @param {HTMLElement} container
 * @returns {() => void}
 */
export function renderProjectDashboard(container) {
  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    const refreshButton = target.closest("[data-dashboard-refresh]");
    if (refreshButton) {
      document.dispatchEvent(new CustomEvent("dashboard:refresh"));
      return;
    }

    const themeButton = target.closest("[data-theme-toggle]");
    if (themeButton) {
      state.themeMode.value = state.themeMode.value === "dark" ? "light" : "dark";
      return;
    }

    // 注意：`[data-copy-command]` 已由 main.js 的 installCopyCommandDelegate
    // 全域處理（UX_SPEC §11.6 通用元件）— 這裡不再重複 bind
  };

  container.addEventListener("click", handleClick);
  const unsubscribe = dashboardData$.subscribe((data) => {
    container.className = "dashboard-shell";
    container.innerHTML = renderDashboard(data);
  });

  return () => {
    container.removeEventListener("click", handleClick);
    unsubscribe();
  };
}

/**
 * @param {DashboardData} data
 * @returns {string}
 */
function renderDashboard(data) {
  const counts = data.scopeCounts?.counts || {};
  const assets = Array.isArray(data.assets?.assets) ? data.assets.assets : [];
  const projectName = escapeHtml(data.scopeCounts?.project_name || data.scopeCounts?.instance_id || "Local Workspace");
  const refreshedAt = formatDateTime(data.refreshedAt);
  const entityCounts = counts.entities || {};
  const entityTotal = totalEntities(entityCounts);
  const dialogueLines = numberValue(counts.dialogue_lines);
  const artAssets = numberValue(counts.art_assets ?? data.assets?.total);
  const qaReports = numberValue(counts.qa_reports);
  // Phase A.0F.patch-major-1 / D-045: narrative readiness denominator must NOT
  // include art_assets — A-* is tracked separately in the Asset Panel. CODEX
  // Major finding: the previous trackedTotal mixed in artAssets, so adding /
  // removing portrait files moved the narrative readiness percentage.
  const trackedTotal = Math.max(1, entityTotal + dialogueLines + qaReports);
  const readinessPercent = percent(dialogueLines, trackedTotal);

  return `
    <section class="dashboard-container">
      ${renderIdentityHeader(projectName, refreshedAt, data.loading)}
      ${data.error ? `<div class="fallback-message" role="status">${escapeHtml(data.error)}</div>` : ""}
      <p class="mobile-dashboard-hint note-text">Dashboard 建議桌面瀏覽器使用；目前顯示精簡單欄版。</p>
      <div class="hero-grid">
        ${renderNextActions()}
        ${renderBlockers(entityTotal, data.error)}
      </div>
      ${renderSceneReadiness({ readinessPercent, dialogueLines, trackedTotal, sceneCount: moduleCount(entityCounts, ["S"]) })}
      ${renderModuleStatus(entityCounts)}
      ${renderTriColumn()}
      ${renderAssetPanel({ assets, artAssets })}
      ${renderFooter(refreshedAt, data.loading)}
    </section>
  `;
}

function renderIdentityHeader(projectName, refreshedAt, loading) {
  return `
    <header class="project-header">
      <div class="project-title-block">
        <p class="breadcrumb">專案首頁 / Dashboard</p>
        <div class="project-title-row">
          <h1 class="project-name">${projectName}</h1>
          <span class="badge ${loading ? "warning" : "success"}">${loading ? "同步中" : "Local"}</span>
        </div>
        <p class="meta-text">最後更新：${escapeHtml(refreshedAt)}</p>
      </div>
      <div class="project-actions" aria-label="Project controls">
        <a class="link-button ghost" href="#/home">🏠 Home</a>
        <a class="link-button ghost" href="#/glossary">📖 Glossary</a>
        <button class="button ghost" type="button" data-theme-toggle>切換明暗</button>
        <button class="button" type="button" data-dashboard-refresh ${loading ? "disabled" : ""}>手動 refresh</button>
      </div>
    </header>
  `;
}

function renderNextActions() {
  const actions = [
    {
      command: "/init-project",
      title: "跑 /init-project 確認專案骨架",
      why: "alpha Dashboard 先提供固定入口；phase_log 推導留 real-data acceptance。",
      contextSummary: "尚未確認 .protocol_version；三 registry 是否齊全；10_art_assets/ 結構是否符合 D-041。",
    },
    {
      command: "/create-world",
      title: "試跑 /create-world 補世界觀第一輪",
      why: "Wave 3 UI 已能讀 aggregate counts，可先用 A 路徑補 narrative 來源。",
      contextSummary: "W-rules / W-language / V 三類缺漏；先補世界觀骨架再進角色建模。",
      contextRefs: ["/01_world/", "/02_vocabulary/", "/00_protocol/00_e_世界觀創建協議.md"],
    },
    {
      command: "/create-scene-task",
      title: "跑 /create-scene-task 啟動下一場任務包",
      why: "場景任務與 Scene Queue 詳細導覽留 A.0F.3。",
      contextRefs: ["/06_detailed_outline/", "/07_scene_tasks/"],
    },
  ];

  return `
    <section class="panel" aria-labelledby="next-actions-title" data-copy-source="Dashboard / HERO Next Actions">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">HERO / Next Actions</p>
          <h2 id="next-actions-title">下一步建議</h2>
        </div>
        <span class="chip">≤ 5</span>
      </div>
      <div class="card-grid">
        ${actions.map((action) => `
          <article class="card">
            <h3 class="card-title">${escapeHtml(action.title)}</h3>
            <div class="card-body">
              <p><strong>為什麼：</strong>${escapeHtml(action.why)}</p>
              <div class="card-actions">
                ${renderCopyCommandButton({
                  command: action.command,
                  contextSummary: action.contextSummary,
                  contextRefs: action.contextRefs,
                  source: "Dashboard / HERO Next Actions",
                  targetAgent: "any",
                  variant: "primary",
                  size: "md",
                })}
                <a class="link-button" href="#/scene-queue">→ Scene Queue</a>
              </div>
            </div>
          </article>
        `).join("")}
      </div>
    </section>
  `;
}

function renderBlockers(entityTotal, hasError) {
  if (hasError) {
    return `
      <section class="panel" aria-labelledby="blockers-title">
        <div class="panel-title">
          <p class="eyebrow">HERO / Blockers</p>
          <h2 id="blockers-title">卡點</h2>
        </div>
        <article class="card blocker-card">
          <span class="badge danger">! 卡點</span>
          <div class="card-body">
            <p><strong>What：</strong>Dashboard 無法取得 server aggregate counts。</p>
            <p><strong>Where：</strong>/api/scope-counts?scope=full</p>
            <p><strong>Why：</strong>server 未啟動或 API 回傳錯誤。</p>
            <p><strong>How：</strong>啟動本地 frontend server 後按手動 refresh。</p>
          </div>
        </article>
      </section>
    `;
  }

  if (entityTotal === 0) {
    return `
      <section class="panel" aria-labelledby="blockers-title">
        <div class="panel-title">
          <p class="eyebrow">HERO / Blockers</p>
          <h2 id="blockers-title">卡點</h2>
        </div>
        <article class="card blocker-card">
          <span class="badge danger">! 卡點</span>
          <div class="card-body">
            <p><strong>What：</strong>目前沒有讀到任何可追蹤 entity。</p>
            <p><strong>Where：</strong>source markdown frontmatter entities</p>
            <p><strong>Why：</strong>專案尚未建立或 header/frontmatter 未完成。</p>
            <p><strong>How：</strong>先跑 /init-project 或補齊起始實體。</p>
          </div>
        </article>
      </section>
    `;
  }

  return `
    <section class="panel" aria-labelledby="blockers-title">
      <div class="panel-title">
        <p class="eyebrow">HERO / Blockers</p>
        <h2 id="blockers-title">卡點</h2>
      </div>
      <div class="empty-state">目前無卡點 — 所有已讀實體已通過本輪 Dashboard aggregate 檢查。可考慮啟動下一場 dialogue 生產。</div>
    </section>
  `;
}

function renderSceneReadiness({ readinessPercent, dialogueLines, trackedTotal, sceneCount }) {
  const stageRows = [
    { label: "DRAFT", count: dialogueLines > 0 ? Math.max(1, Math.min(sceneCount || 1, dialogueLines)) : 0, total: Math.max(sceneCount, 1) },
    { label: "REVIEW", count: 0, total: Math.max(sceneCount, 1) },
    { label: "LOCKED", count: 0, total: Math.max(sceneCount, 1) },
    { label: "DEPRECATED", count: 0, total: Math.max(sceneCount, 1) },
    { label: "未啟動", count: Math.max(sceneCount - (dialogueLines > 0 ? 1 : 0), 0), total: Math.max(sceneCount, 1) },
  ];

  return `
    <section class="panel" aria-labelledby="readiness-title">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Scene Readiness Overview</p>
          <h2 id="readiness-title">場景就緒度</h2>
        </div>
        <span class="badge warning">${readinessPercent}%</span>
      </div>
      <div class="readiness-grid">
        <div class="progress-shell">
          <div class="progress-label-row">
            <strong>整體 ${readinessPercent}%</strong>
            <span class="meta-text">${dialogueLines} / ${trackedTotal} tracked counts</span>
          </div>
          ${progressBar(readinessPercent, "success")}
          <div class="metric-grid">
            <div class="metric-box"><span class="metric-value">${dialogueLines}</span><span class="metric-label">dialogue lines</span></div>
            <div class="metric-box"><span class="metric-value">${sceneCount}</span><span class="metric-label">S entities</span></div>
            <div class="metric-box"><span class="metric-value">${trackedTotal}</span><span class="metric-label">scope total</span></div>
          </div>
          <div class="inline-actions">
            <a class="link-button primary" href="#/scene-queue">→ 進入 Scene Queue / Enter Scene Queue</a>
          </div>
        </div>
        <div class="readiness-stages">
          ${stageRows.map((row) => `
            <div class="stage-row">
              <strong>${escapeHtml(row.label)}</strong>
              ${progressBar(percent(row.count, row.total))}
              <span class="meta-text">${row.count}</span>
            </div>
          `).join("")}
          <p class="note-text">階段順序為閱讀用，不代表必須走完一階段才能進下一階段。</p>
        </div>
      </div>
    </section>
  `;
}

function renderModuleStatus(entityCounts) {
  const maxCount = Math.max(1, ...ENTITY_MODULES.map((item) => moduleCount(entityCounts, item.sources)));

  return `
    <section class="panel" aria-labelledby="module-status-title">
      <div class="panel-title">
        <p class="eyebrow">Module Status</p>
        <h2 id="module-status-title">模組狀態總覽</h2>
      </div>
      <div class="module-table-wrap">
        <table class="module-table">
          <thead>
            <tr>
              <th>模組 / Module</th>
              <th>狀態 / Status</th>
              <th>細項 / Detail</th>
              <th>動作 / Action</th>
            </tr>
          </thead>
          <tbody>
            ${ENTITY_MODULES.map((item) => {
              const count = moduleCount(entityCounts, item.sources);
              const modulePercent = percent(count, maxCount);
              return `
                <tr>
                  <td><strong>${escapeHtml(item.label)}</strong> ${escapeHtml(item.module)}</td>
                  <td>${statusBadge(count)}</td>
                  <td class="module-count-cell">
                    <div class="mini-bar">
                      ${progressBar(modulePercent)}
                      <span>${count}</span>
                    </div>
                  </td>
                  <td>${renderCopyCommandButton({
                    command: item.viewCommand,
                    contextSummary: `檢視 ${item.module} 模組內容（${item.label}）。`,
                    source: "Dashboard / Module Status",
                    targetAgent: "claude-code",
                    variant: "ghost",
                    size: "sm",
                    label: "複製 view 指令",
                  })}</td>
                </tr>
              `;
            }).join("")}
          </tbody>
        </table>
      </div>
      <p class="note-text">模組順序依 SPEC §5.1 entity 類型；非執行順序。</p>
    </section>
  `;
}

// §11.1.6 Tri-column Snapshot — 待人類裁決 / QA Pending / Canon Δ Pending。
// NEW_REQ_20 F1-3（11th master frontend cycle）：原 Phase A.0F.2 alpha 階段 mock
// content（「Phase A 後段任務 / A.0F UI 進度 / Wave 3 狀態」進度字串）屬規格漂移
// 實 bug + 資料過時，已移除。三欄 subject 改對齊 UX_SPEC §11.1.6 status snapshot。
// 目前顯示空狀態（依 §11.1.6 + G3「不假設每場必有 X」）；動態 pending 反查待
// backend endpoint /api/dashboard/pending-status（NEW_REQ_44 — 需先定義 09_e
// 待裁決標記 / Canon Delta 儲存 schema / QA-pending 判定規則）。
function renderTriColumn() {
  const columns = [
    {
      title: "待人類裁決 / HD",
      empty: "目前無待裁決事項。下一波預期出現在 D.3.5 收斂 gate 或 QA_FAILED 後的破格保留判定。",
      target: "09_e 定稿變更紀錄",
    },
    {
      title: "QA Pending",
      empty: "目前無待跑 QA。接回外接台詞後，未跑完 09_a–09_i 的場景會列於此。",
      target: "QA 報告",
    },
    {
      title: "Canon Δ Pending",
      empty: "目前無待回流 Canon Δ。迭代產生的 canon 變更候選會列於此。",
      target: "09_d 資訊控制紀錄",
    },
  ];

  return `
    <section class="panel" aria-labelledby="tri-column-title">
      <div class="panel-title">
        <p class="eyebrow">Tri-column Snapshot</p>
        <h2 id="tri-column-title">三欄區</h2>
      </div>
      <p class="note-text">動態 pending 反查待 backend endpoint <code>/api/dashboard/pending-status</code>（NEW_REQ_44）；目前依規格顯示空狀態。</p>
      <div class="tri-column">
        ${columns.map((column) => `
          <article class="card">
            <h3 class="card-title">${escapeHtml(column.title)}</h3>
            <div class="empty-state">${escapeHtml(column.empty)}</div>
            <div class="card-actions">
              <a class="link-button" href="#/dashboard" aria-disabled="true">跳轉 ${escapeHtml(column.target)}（待 backend）</a>
            </div>
          </article>
        `).join("")}
      </div>
    </section>
  `;
}

function renderAssetPanel({ assets, artAssets }) {
  // §11.1.6a A-* Asset Panel 完整版（A.0F.11）
  // 7 subtype 分組 + 缺檔 ⚠ 警示 (UPS-UX-70) + 點 subtype 展開子表 + 跳 /10_art_assets/
  const summaries = ASSET_SUBTYPES.map((subtype) => summarizeAssets(subtype, assets));
  const complete = summaries.reduce((sum, item) => sum + item.done, 0);
  // Audit-doc C3 fix: 用 sumTotal 為單一權威分母（per-subtype 加總，跟 UI 顯示對齊），
  // 避免原 Math.max(artAssets, assets.length, sumTotal) 三 source 不一致時呈現
  // 「100% 但仍有 missing」這種違反直覺數字。Mismatch 時 console.warn 提示。
  const sumTotal = summaries.reduce((sum, item) => sum + item.total, 0);
  const total = Math.max(sumTotal, 1);
  if (sumTotal !== assets.length || (typeof artAssets === "number" && artAssets !== sumTotal)) {
    console.warn(
      "[AssetPanel] 三 source 不一致 — sumTotal:", sumTotal,
      "/ assets.length:", assets.length,
      "/ artAssets (from scope-counts):", artAssets,
      "— 用 sumTotal 為分母 (audit-doc C3)。"
    );
  }
  const assetPercent = percent(complete, total);
  const totalMissing = summaries.reduce((sum, item) => sum + item.missing, 0);

  return `
    <section class="panel" aria-labelledby="asset-panel-title" data-copy-source="Dashboard / Asset Panel">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Asset Panel — §11.1.6a (D-044 / D-045)</p>
          <h2 id="asset-panel-title">A-* 美術資產進度</h2>
        </div>
        <div class="asset-panel-summary">
          <span class="badge ${totalMissing > 0 ? "danger" : "warning"}">獨立於 narrative 完成度 ${assetPercent}% (${complete}/${total})</span>
          ${totalMissing > 0 ? `<span class="badge danger">⚠ ${totalMissing} 個缺檔</span>` : ""}
        </div>
      </div>

      <p class="note-text">
        依 D-045：A-* 完成度不納入 narrative /status 整體完成度；不影響 dialogue FINAL gate。
        7 subtype 對齊 D-044：portrait / bg / cg / sfx / bgm / voice / ui。
      </p>

      <div class="asset-grid">
        ${summaries.map((summary) => renderAssetSubtypeCard(summary)).join("")}
      </div>

      <div class="inline-actions">
        <a class="link-button primary" href="#/asset-registry" aria-disabled="true">
          → 進入 Asset Registry 完整視圖 (Phase D Wave 14 後)
        </a>
        <a class="link-button" href="#/export">
          📤 開啟 L3 Export panel
        </a>
      </div>
    </section>
  `;
}

function renderAssetSubtypeCard(summary) {
  const hasMissing = summary.missing > 0;
  const stateBadge = hasMissing
    ? `<span class="badge danger">⚠ ${summary.missing} 缺檔</span>`
    : `<span class="chip">${summary.total} KEYs</span>`;

  return `
    <article class="card asset-card">
      <div class="asset-card-header">
        <h3 class="card-title">${escapeHtml(summary.label)}</h3>
        ${stateBadge}
      </div>
      ${progressBar(summary.percent, hasMissing ? "warning" : "success")}
      <div class="asset-stats">
        <span>✓ 完成 ${summary.done}　◐ 製作中 ${summary.inProgress}</span>
        <span>○ 未啟動 ${summary.notStarted}　✗ 缺檔 ${summary.missing}</span>
        <span class="meta-text">
          覆蓋率 ${summary.total > 0 ? Math.round((summary.done / summary.total) * 100) : 0}%
          ${summary.total === 0 ? `(尚無 ${summary.label.split("（")[0]} KEY 註冊)` : ""}
        </span>
      </div>
      ${hasMissing ? `
        <p class="asset-missing-warning" role="alert">
          ⚠ 有 ${summary.missing} 個 KEY 被引用但 art_metadata 找不到對應 asset_id —
          請檢查 10_art_assets/${escapeHtml(summary.key)}/ 內 .md 檔（v0.4 master 第四輪 CC-01 對齊）。
        </p>
      ` : ""}
    </article>
  `;
}

function renderFooter(refreshedAt, loading) {
  return `
    <footer class="panel">
      <div class="panel-header">
        <p class="meta-text">最後 refresh：${escapeHtml(refreshedAt)}</p>
        <button class="button" type="button" data-dashboard-refresh ${loading ? "disabled" : ""}>手動 refresh</button>
      </div>
    </footer>
  `;
}

function statusBadge(count) {
  if (count > 0) return `<span class="badge success">~ Active</span>`;
  return `<span class="badge warning">○ 未啟動</span>`;
}

function summarizeAssets(subtype, assets) {
  const filtered = assets.filter((asset) => asset.subtype === subtype.key);
  const bucket = { done: 0, inProgress: 0, missing: 0, notStarted: 0 };

  filtered.forEach((asset) => {
    const state = classifyAssetState(asset.state_tags || []);
    bucket[state] += 1;
  });

  const total = filtered.length;
  return {
    ...subtype,
    ...bucket,
    total,
    percent: percent(bucket.done, total),
  };
}

function classifyAssetState(tags) {
  const joined = tags.join(" ").toLowerCase();
  if (/(missing|缺|lost|not_found)/.test(joined)) return "missing";
  if (/(done|complete|final|locked|完成|已完成)/.test(joined)) return "done";
  if (/(wip|progress|draft|review|製作|進行|草稿)/.test(joined)) return "inProgress";
  return "notStarted";
}

function moduleCount(entityCounts, keys) {
  return keys.reduce((sum, key) => sum + numberValue(entityCounts?.[key]), 0);
}

function totalEntities(entityCounts) {
  if (!entityCounts || typeof entityCounts !== "object") return 0;
  return Object.values(entityCounts).reduce((sum, value) => sum + numberValue(value), 0);
}

function numberValue(value) {
  return Number.isFinite(Number(value)) ? Number(value) : 0;
}

function percent(done, total) {
  if (!total) return 0;
  return Math.max(0, Math.min(100, Math.round((done / total) * 100)));
}

function progressBar(value, tone = "") {
  return `
    <div class="progress-track" aria-hidden="true">
      <div class="progress-fill ${escapeAttribute(tone)}" style="--progress-value: ${percent(value, 100)}%"></div>
    </div>
  `;
}

function formatDateTime(value) {
  if (!value) return "尚未同步";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("zh-Hant", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(date);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttribute(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}

// copyText / showToast 已由通用 CopyCommandButton 元件 +
// main.js installCopyCommandDelegate 處理（UX_SPEC §11.6）；
// ProjectDashboard 不再自行維護這兩個私函。
