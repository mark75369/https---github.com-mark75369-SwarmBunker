import { state, scenesData$, sceneDetailData$ } from "./state.js";
import { renderProjectDashboard } from "./components/ProjectDashboard.js";
import { renderWorkspaceHome } from "./pages/WorkspaceHome.js";
import { renderSceneQueue } from "./pages/SceneQueue.js";
import { renderSceneDetail } from "./pages/SceneDetail.js";
import { renderExportPanel } from "./pages/ExportPanel.js";
import { renderGlossary } from "./pages/Glossary.js";
import { renderSceneEditor } from "./pages/SceneEditor.js";
import { fetchScenes, fetchSceneHeader, fetchSceneVersions } from "./api.js";

/**
 * @param {string} [hash]
 * @returns {string}
 */
export function normalizeRoute(hash = window.location.hash) {
  const raw = hash.replace(/^#/, "").trim();
  if (!raw || raw === "/") return "/";
  return raw.startsWith("/") ? raw : `/${raw}`;
}

/**
 * @param {string} route
 * @returns {boolean}
 */
export function isDashboardRoute(route) {
  return route === "/" || route === "/dashboard";
}

const SCENE_DETAIL_RE = /^\/scene\/([A-Za-z0-9_-]+)\/?$/;
const SCENE_EDITOR_RE = /^\/scene\/([A-Za-z0-9_-]+)\/edit\/?$/;

function renderNotFound(container) {
  container.className = "app-shell";
  container.innerHTML = `
    <section class="dashboard-container">
      <div class="panel">
        <div class="panel-title">
          <p class="eyebrow">Route</p>
          <h1 class="project-name">找不到頁面 / Not found</h1>
        </div>
        <p class="meta-text">沒有對應的 hash route。</p>
        <a class="link-button primary" href="#/">返回 Project Dashboard</a>
        <a class="link-button" href="#/scene-queue">前往 Scene Queue</a>
      </div>
    </section>
  `;
  return () => {};
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

let scenesLoadPromise = null;

function loadScenes({ force = false } = {}) {
  const current = scenesData$.value;
  if (scenesLoadPromise && !force) return scenesLoadPromise;
  if (!force && current.data && !current.error) return Promise.resolve(current);

  scenesData$.value = { ...current, loading: true, error: null };

  scenesLoadPromise = fetchScenes()
    .then((data) => {
      const next = {
        data,
        loading: false,
        error: null,
        refreshedAt: new Date().toISOString(),
      };
      scenesData$.value = next;
      return next;
    })
    .catch((err) => {
      const next = {
        ...scenesData$.value,
        loading: false,
        error: err?.message || "無法連到 server，請確認 server 已啟動",
        refreshedAt: new Date().toISOString(),
      };
      scenesData$.value = next;
      return next;
    })
    .finally(() => {
      scenesLoadPromise = null;
    });
  return scenesLoadPromise;
}

const sceneDetailLoadPromises = new Map();

function loadSceneDetail(sceneId, { force = false } = {}) {
  const current = sceneDetailData$.value;
  if (sceneDetailLoadPromises.has(sceneId) && !force) {
    return sceneDetailLoadPromises.get(sceneId);
  }
  if (!force && current.sceneId === sceneId && current.header && !current.error) {
    return Promise.resolve(current);
  }

  sceneDetailData$.value = {
    sceneId,
    header: null,
    versions: null,
    summary: null,
    loading: true,
    error: null,
    refreshedAt: null,
  };

  const promise = Promise.all([
    fetchSceneHeader(sceneId).catch((err) => ({ __error: err })),
    fetchSceneVersions(sceneId).catch((err) => ({ __error: err })),
    loadScenes(),
  ])
    .then(([header, versions, scenesState]) => {
      const headerError = header?.__error;
      const versionsError = versions?.__error;
      const summary = scenesState?.data?.scenes?.find((s) => s.scene_id === sceneId) || null;
      const errors = [];
      if (headerError) errors.push(`header: ${headerError.message || headerError}`);
      if (versionsError) errors.push(`versions: ${versionsError.message || versionsError}`);
      const next = {
        sceneId,
        header: headerError ? null : header,
        versions: versionsError ? null : versions,
        summary,
        loading: false,
        error: errors.length ? errors.join("；") : null,
        refreshedAt: new Date().toISOString(),
      };
      sceneDetailData$.value = next;
      return next;
    })
    .catch((err) => {
      const next = {
        ...sceneDetailData$.value,
        loading: false,
        error: err?.message || "Scene Detail 載入失敗",
        refreshedAt: new Date().toISOString(),
      };
      sceneDetailData$.value = next;
      return next;
    })
    .finally(() => {
      sceneDetailLoadPromises.delete(sceneId);
    });

  sceneDetailLoadPromises.set(sceneId, promise);
  return promise;
}

/**
 * Phase A.0F.patch-concern-1: preflight gate for `#/scene/<id>/edit`.
 *
 * Workflow:
 *   1. Show a transient "checking LOCKED status" panel.
 *   2. Hit GET /api/scene/<id>/header.
 *   3a. If 狀態 === "LOCKED" → redirect to `#/scene/<id>` so the user sees
 *       §11.5.2 LOCKED gate + downgrade guide rather than entering the editor.
 *   3b. Otherwise → mount the actual SceneEditor.
 *   3c. On header error → mount the editor anyway (fail-open for read; editor
 *       itself will surface load failures with fail-closed save behavior added
 *       in patch-P0).
 *
 * @param {HTMLElement} app
 * @param {string} sceneId
 * @returns {() => void}
 */
function renderEditorPreflight(app, sceneId) {
  app.className = "app-shell";
  app.innerHTML = `
    <section class="dashboard-container">
      <div class="panel">
        <p class="meta-text">Scene Editor ${escapeHtml(sceneId)} — 檢查 LOCKED 狀態中...</p>
      </div>
    </section>
  `;

  let cleanup = () => {};
  let cancelled = false;

  fetchSceneHeader(sceneId)
    .then((header) => {
      if (cancelled) return;
      const status = header?.header?.["狀態"];
      if (status === "LOCKED") {
        // Replace location hash so the user lands on Scene Detail. The next
        // hashchange will mount SceneDetail (which renders the LOCKED gate).
        window.location.hash = `#/scene/${encodeURIComponent(sceneId)}`;
        return;
      }
      cleanup = renderSceneEditor(app, { sceneId });
    })
    .catch(() => {
      if (cancelled) return;
      // Fail-open for header read failure; SceneEditor's load flow itself is
      // fail-closed for content and will show a banner if anything is wrong.
      cleanup = renderSceneEditor(app, { sceneId });
    });

  return () => {
    cancelled = true;
    cleanup();
  };
}

/**
 * @param {{app: HTMLElement, onDashboardRoute?: () => void}} options
 * @returns {() => void}
 */
export function initRouter({ app, onDashboardRoute } = {}) {
  let cleanup = () => {};

  const updateRoute = () => {
    const route = normalizeRoute();
    state.route.value = route;

    cleanup();
    cleanup = () => {};

    // 1. Dashboard
    if (isDashboardRoute(route)) {
      cleanup = renderProjectDashboard(app);
      onDashboardRoute?.();
      return;
    }
    // 2. Workspace Home
    if (route === "/home") {
      cleanup = renderWorkspaceHome(app);
      return;
    }
    // 3. Scene Queue
    if (route === "/scene-queue") {
      cleanup = renderSceneQueue(app, { loadScenes });
      loadScenes();
      return;
    }
    // 4. Scene Detail
    const detailMatch = SCENE_DETAIL_RE.exec(route);
    if (detailMatch) {
      const sceneId = decodeURIComponent(detailMatch[1]);
      cleanup = renderSceneDetail(app, { sceneId, loadSceneDetail });
      loadSceneDetail(sceneId);
      return;
    }
    // 5. Export Panel (Phase A.0F.10)
    if (route === "/export") {
      cleanup = renderExportPanel(app);
      return;
    }
    // 5b. Glossary (Phase A.0F.9)
    if (route === "/glossary") {
      cleanup = renderGlossary(app);
      return;
    }
    // 6. Scene Editor (Phase A.0F.6 + A.0F.7 + A.0F.8 — F3 + LOCKED race guard + mtime conflict)
    // Phase A.0F.patch-concern-1: direct hash route `#/scene/<id>/edit` must
    // preflight the scene header. If the scene is LOCKED, redirect to Scene
    // Detail (which carries the §11.5.2 LOCKED gate / downgrade guide).
    // CODEX Concern §1 §11.5: previously the route mounted SceneEditor
    // immediately, allowing direct URL access into the editor while LOCKED.
    const editorMatch = SCENE_EDITOR_RE.exec(route);
    if (editorMatch) {
      const sceneId = decodeURIComponent(editorMatch[1]);
      cleanup = renderEditorPreflight(app, sceneId);
      return;
    }
    cleanup = renderNotFound(app);
  };

  // Phase A.0F.patch-P2: cleanup must remove the document listeners too,
  // otherwise re-initialising the router (tests / HMR / remount) duplicates
  // them. CODEX P2 finding.
  const onScenesRefresh = () => loadScenes({ force: true });
  const onSceneDetailRefresh = (event) => {
    const sid = event?.detail?.sceneId || sceneDetailData$.value.sceneId;
    if (sid) loadSceneDetail(sid, { force: true });
  };

  window.addEventListener("hashchange", updateRoute);
  document.addEventListener("scenes:refresh", onScenesRefresh);
  document.addEventListener("scene-detail:refresh", onSceneDetailRefresh);
  updateRoute();

  return () => {
    window.removeEventListener("hashchange", updateRoute);
    document.removeEventListener("scenes:refresh", onScenesRefresh);
    document.removeEventListener("scene-detail:refresh", onSceneDetailRefresh);
    cleanup();
  };
}
