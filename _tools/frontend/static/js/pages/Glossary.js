/**
 * Glossary page — UX §11.9 (保留元件) 簡化版
 *
 * 從 static/assets/glossary.json 載入詞彙清單，分類展開可查。
 * 對齊 §11.9 — 「保留」類別不放入 prototype 拒絕清單，
 *  本輪先簡化版（無搜尋 / 無編輯）；A.0F 後期可加 search facet。
 */

const GLOSSARY_URL = "./assets/glossary.json";

/**
 * @param {HTMLElement} container
 * @returns {() => void}
 */
export function renderGlossary(container) {
  container.className = "app-shell glossary-shell";
  container.innerHTML = renderLoading();

  let cancelled = false;
  fetch(GLOSSARY_URL)
    .then((r) => r.json())
    .then((data) => {
      if (cancelled) return;
      container.innerHTML = renderGlossaryPage(data);
    })
    .catch((err) => {
      if (cancelled) return;
      container.innerHTML = renderError(err);
    });

  return () => { cancelled = true; };
}

function renderLoading() {
  return `
    <section class="dashboard-container">
      <div class="panel">
        <p class="meta-text">Glossary 載入中...</p>
      </div>
    </section>
  `;
}

function renderError(err) {
  return `
    <section class="dashboard-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁 / Dashboard</a> / Glossary
          </p>
          <div class="project-title-row">
            <h1 class="project-name">Glossary / 詞彙</h1>
          </div>
        </div>
      </header>
      <div class="fallback-message" role="status">
        無法載入 glossary.json: ${escapeHtml(err?.message || String(err))}
      </div>
    </section>
  `;
}

function renderGlossaryPage(data) {
  const cats = Array.isArray(data?.categories) ? data.categories : [];
  return `
    <section class="dashboard-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁 / Dashboard</a> / Glossary
          </p>
          <div class="project-title-row">
            <h1 class="project-name">Glossary / 詞彙</h1>
            <span class="badge success">v${escapeHtml(data?.schema_version || "?")}</span>
          </div>
          <p class="meta-text">最後更新：${escapeHtml(data?.updated || "—")}</p>
        </div>
        <div class="project-actions">
          <a class="link-button" href="#/">← Dashboard</a>
        </div>
      </header>

      ${cats.map(renderCategory).join("")}

      <p class="note-text">
        詞彙來源：_design/SPEC.md / DECISIONS_LOG.md / UX_SPEC.md / TASKS.md 等鎖定 spec。
        本頁簡化版 — A.0F 後期可加 search facet + alias 反查。
      </p>
    </section>
  `;
}

function renderCategory(cat) {
  const terms = Array.isArray(cat?.terms) ? cat.terms : [];
  return `
    <section class="panel">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Glossary Category</p>
          <h2>${escapeHtml(cat?.label || cat?.id || "?")}</h2>
        </div>
        <span class="chip">${terms.length}</span>
      </div>
      <dl class="glossary-list">
        ${terms.map((t) => `
          <div class="glossary-entry">
            <dt><code class="glossary-term">${escapeHtml(t.term)}</code></dt>
            <dd>${escapeHtml(t.definition)}</dd>
          </div>
        `).join("")}
      </dl>
    </section>
  `;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
