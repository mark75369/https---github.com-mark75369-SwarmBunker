/**
 * API client for the local frontend adapter.
 *
 * Endpoint set (對齊 ARCH §13.2 8 endpoint + Phase A.0F.3 補 /api/scenes list +
 * Phase A.0F.patch-P0 補 /api/scene/<id>/version-content):
 *   1. GET  /api/scene/<id>/header
 *   2. POST /api/scene/<id>/save
 *   3. POST /api/scene/<id>/save-as
 *   4. GET  /api/scenes/<id>/versions
 *   5. GET  /api/scenes/<id>/keys/<key>/lines
 *   6. GET  /api/assets?scope=...
 *   7. GET  /api/assets/<id>/usage
 *   8. GET  /api/scope-counts?scope=...
 *   +  GET  /api/scenes?chapter=...  (Phase A.0F.3 frontend adapter 自用 list endpoint)
 *   +  GET  /api/scene/<id>/version-content?path=... (Phase A.0F.patch-P0 — exact-path content load)
 */

/**
 * @param {string} path
 * @param {RequestInit} [options]
 * @returns {Promise<any>}
 */
export async function requestJson(path, options = {}) {
  const response = await fetch(path, {
    headers: {
      "Accept": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    // 嘗試解析 JSON error body（含 server-provided error code + suggestion）
    let body = null;
    try {
      body = await response.json();
    } catch {
      // body 不是 JSON — 不致命
    }
    const err = new Error(`Request failed: ${response.status} ${response.statusText}`);
    err.status = response.status;
    err.body = body;
    err.path = path;
    throw err;
  }

  return response.json();
}

/**
 * @param {string} [scope]
 * @returns {Promise<any>}
 */
export function fetchScopeCounts(scope = "full") {
  const params = new URLSearchParams({ scope });
  return requestJson(`/api/scope-counts?${params.toString()}`);
}

/**
 * @param {string} [scope]
 * @returns {Promise<any>}
 */
export function fetchAssets(scope = "all") {
  const params = new URLSearchParams({ scope });
  return requestJson(`/api/assets?${params.toString()}`);
}

/**
 * @returns {Promise<{scopeCounts: any, assets: any}>}
 */
export async function fetchDashboardData() {
  const [scopeCounts, assets] = await Promise.all([
    fetchScopeCounts("full"),
    fetchAssets("all"),
  ]);
  return { scopeCounts, assets };
}

/**
 * Phase A.0F.3 新增 — 取所有場景 summary（Scene Queue UI 用）。
 *
 * @param {string} [chapter]  可選 chapter 篩選（如 "01" / "Ch02"）
 * @returns {Promise<{scenes: any[], total: number, chapters: string[]}>}
 */
export function fetchScenes(chapter) {
  const params = new URLSearchParams();
  if (chapter) params.set("chapter", chapter);
  const qs = params.toString();
  return requestJson(`/api/scenes${qs ? "?" + qs : ""}`);
}

/**
 * Endpoint #1：取單一場景 header + mtime + parse issues
 * @param {string} sceneId
 */
export function fetchSceneHeader(sceneId) {
  return requestJson(`/api/scene/${encodeURIComponent(sceneId)}/header`);
}

/**
 * Endpoint #4：取單一場景的所有 versioned dialogue 檔
 * @param {string} sceneId
 */
export function fetchSceneVersions(sceneId) {
  return requestJson(`/api/scenes/${encodeURIComponent(sceneId)}/versions`);
}

/**
 * Phase A.0F.patch-P0：取 exact (scene_id, path) 版本檔 raw markdown content.
 *
 * Why: SceneEditor previously used `fetch("/" + v.path)` to read scene
 * markdown, but the server only mounts `_tools/frontend/static` at `/` so the
 * request returned a 404 body that was silently used as the textarea
 * baseline. This endpoint enforces fail-closed semantics: path must live
 * under 08_dialogue_outputs/ and match scene_id (server.resolve_target_path).
 *
 * @param {string} sceneId
 * @param {string} relPath  repo-relative POSIX path (must live under 08_dialogue_outputs/)
 * @returns {Promise<{scene_id:string, path:string, content:string, mtime:number, header:any}>}
 */
export function fetchSceneVersionContent(sceneId, relPath) {
  const params = new URLSearchParams({ path: relPath });
  return requestJson(`/api/scene/${encodeURIComponent(sceneId)}/version-content?${params.toString()}`);
}

/**
 * Endpoint #5：取單一 dialogue KEY 跨版本對照
 * @param {string} sceneId
 * @param {string} key
 */
export function fetchSceneKeyLines(sceneId, key) {
  return requestJson(`/api/scenes/${encodeURIComponent(sceneId)}/keys/${encodeURIComponent(key)}/lines`);
}

/**
 * Endpoint #7：反查 asset 使用場景 list
 * @param {string} assetId
 */
export function fetchAssetUsage(assetId) {
  return requestJson(`/api/assets/${encodeURIComponent(assetId)}/usage`);
}

/**
 * Endpoint #2: write a single scene file (mtime checksum + LOCKED race guard).
 *
 * Phase A.0F.patch-P0: payload MUST include `target_path` (the v.path the
 * editor was working with). The server no longer falls back to
 * resolve_scene_file's latest-mtime candidate, so multi-version scenes
 * (v01/v02) can no longer overwrite the wrong file.
 *
 * @param {string} sceneId
 * @param {{content: string, mtime_baseline: number, target_path: string}} payload
 */
export function saveScene(sceneId, payload) {
  return requestJson(`/api/scene/${encodeURIComponent(sceneId)}/save`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}

/**
 * Endpoint #3: save-as DRAFT proposal (LOCKED race modal option B).
 *
 * Phase A.0F.patch-P0: payload MUST include `target_path` (the editor source
 * v.path). Proposal naming + base_dialogue lineage are derived from that
 * exact path.
 *
 * @param {string} sceneId
 * @param {{content: string, target_path: string, base_dialogue?: string, iteration_note?: string, proposal_suffix?: string}} payload
 */
export function saveSceneAs(sceneId, payload) {
  return requestJson(`/api/scene/${encodeURIComponent(sceneId)}/save-as`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}
