import { dashboardData$, state } from "../state.js";

/**
 * Workspace Home — UX §11.9 保留元件
 *
 * #/home — 多入口首頁，方便快速跳到各功能：
 *   - Project Dashboard (#/)
 *   - Scene Queue (#/scene-queue)
 *   - Export Panel (#/export)
 *   - Glossary (#/glossary)
 *   - Theme toggle
 *
 * @param {HTMLElement} container
 * @returns {() => void}
 */
export function renderWorkspaceHome(container) {
  container.className = "app-shell workspace-home";

  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    if (target.closest("[data-theme-toggle]")) {
      state.themeMode.value = state.themeMode.value === "dark" ? "light" : "dark";
    }
  };
  container.addEventListener("click", handleClick);

  const unsubscribe = dashboardData$.subscribe((data) => {
    const counts = data.scopeCounts?.counts || {};
    const scenes = Number(counts.entities?.S || 0);
    const dialogueLines = Number(counts.dialogue_lines || 0);
    const artAssets = Number(counts.art_assets || 0);
    const refreshedAt = data.refreshedAt ? new Date(data.refreshedAt).toLocaleString("zh-Hant") : "尚未同步";

    container.innerHTML = `
      <section class="dashboard-container">
        <header class="project-header">
          <div class="project-title-block">
            <p class="breadcrumb">Workspace Home</p>
            <div class="project-title-row">
              <h1 class="project-name">劇本開發工具 / Game Dialogue Bible</h1>
              <span class="badge success">Local</span>
            </div>
            <p class="meta-text">最後同步：${escapeHtml(refreshedAt)}</p>
          </div>
          <div class="project-actions">
            <button class="button ghost" type="button" data-theme-toggle>切換明暗 / Toggle theme</button>
          </div>
        </header>

        <section class="panel">
          <div class="panel-title">
            <p class="eyebrow">Quick Stats</p>
            <h2>整體概況</h2>
          </div>
          <div class="metric-grid">
            <div class="metric-box"><span class="metric-value">${scenes}</span><span class="metric-label">場景 / S-*</span></div>
            <div class="metric-box"><span class="metric-value">${dialogueLines}</span><span class="metric-label">dialogue lines</span></div>
            <div class="metric-box"><span class="metric-value">${artAssets}</span><span class="metric-label">A-* assets</span></div>
          </div>
        </section>

        <section class="panel">
          <div class="panel-title">
            <p class="eyebrow">主要入口 / Main Entries</p>
            <h2>選擇下一步</h2>
          </div>
          <div class="workspace-entry-grid">
            <a class="workspace-entry-card" href="#/">
              <h3>📊 Project Dashboard</h3>
              <p>整體看板：HERO 下一步 / 卡點 / 場景就緒度 / 模組狀態 / Asset Panel</p>
            </a>
            <a class="workspace-entry-card" href="#/scene-queue">
              <h3>📋 Scene Queue</h3>
              <p>場景列表 + 7 維 facet 搜尋 + chapter group + 進場景 cockpit</p>
            </a>
            <a class="workspace-entry-card" href="#/export">
              <h3>📤 Layer 3 Export Panel</h3>
              <p>產 L3 export prompt：clipboard 或 POST 到本地 LLM endpoint（D-038 A1）</p>
            </a>
            <a class="workspace-entry-card" href="#/glossary">
              <h3>📖 Glossary</h3>
              <p>專案常用詞彙：狀態 / 實體 / mode tag / QA 模板 / 設計守則</p>
            </a>
          </div>
        </section>
      </section>
    `;
  });

  return () => {
    container.removeEventListener("click", handleClick);
    unsubscribe();
  };
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
