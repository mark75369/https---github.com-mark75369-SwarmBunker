/**
 * Scene Queue page — F2 + F6（UX_SPEC §11.2.1 + §11.4）
 *
 * Phase A.0F.3 落地 F2 列表 + chapter group + scene cards。
 * Phase A.0F.4 擴充 F6 — 7 維 facet + fuzzy search + localStorage persisted state。
 *
 * Facet 7 維（依 UX §11.4.3 對齊）：
 *   1. Chapter — 章別（動態 enum，從 scenes 反查 + 「未分章」）
 *   2. Pipeline State — DRAFT / REVIEW / LOCKED / DEPRECATED / 未啟動（SPEC §16 固定 5 桶）
 *   3. Task Status — DRAFT / REVIEW / null（任務包狀態）
 *   4. Has Dialogue — yes / no（是否已起 v01）
 *   5. Has QA — yes / no（是否跑過 QA）
 *   6. Has LOCKED Version — yes / no（是否有任一 LOCKED dialogue 版）
 *   7. (Mode Tag / Characters facet 屬 [BLOCKED:UPSTREAM_DOWNSTREAM] —
 *      mode_tag 需要 dialogue 內部讀取；Characters 需要 entities 反查 — 待 backend 擴充)
 *
 * Search：scene_id / chapter / pipeline_state / task_path 全文 fuzzy
 *         (i18n KEY 跨檔搜尋待 backend 提供 search API — [NEEDS_SCHEMA_SUPPORT])
 *
 * 對齊：
 *   - §11.4.4 facet 互動：單一 facet 內多選 OR；facet 間 AND
 *   - §11.4.4 Persisted state — localStorage('scene-queue-facets-v1')
 *   - §11.4.5 G1 守則 — count + 詳細欄位三層
 *   - §11.4.6 empty state 文案
 *   - §11.4.7 篩選結果批次 export 按鈕（CopyCommandButton 批次指令）
 *   - D-027 qa_type 可擴充 — facet 動態讀（本輪先列固定 6 維，qa_type 留 A.0F.10 之後）
 */

import { scenesData$ } from "../state.js";
import { renderCopyCommandButton } from "../components/CopyCommandButton.js";

const STORAGE_KEY = "scene-queue-facets-v1";

/** @typedef {{
 *   search: string,
 *   chapters: string[],
 *   pipelineStates: string[],
 *   taskStatuses: string[],
 *   hasDialogue: "any"|"yes"|"no",
 *   hasQa: "any"|"yes"|"no",
 *   hasLocked: "any"|"yes"|"no"
 * }} QueueFilters */

/** @returns {QueueFilters} */
function defaultFilters() {
  return {
    search: "",
    chapters: [],
    pipelineStates: [],
    taskStatuses: [],
    hasDialogue: "any",
    hasQa: "any",
    hasLocked: "any",
  };
}

/** @returns {QueueFilters} */
function loadFilters() {
  if (typeof window === "undefined") return defaultFilters();
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultFilters();
    const parsed = JSON.parse(raw);
    // Phase A.0F.patch-P1 — validate localStorage shape strictly. Attacker
    // could pre-seed localStorage with arrays-of-objects, function-like keys,
    // or HTML-laced strings; without validation those flow into facet renders
    // and the active filter summary (CODEX P1 finding).
    return sanitizeFilters(parsed);
  } catch {
    return defaultFilters();
  }
}

/**
 * Strict shape coercion for loaded filter state. Unknown / malformed fields
 * fall back to defaults. Only string / "any|yes|no" enum values pass through.
 * @param {any} raw
 * @returns {QueueFilters}
 */
function sanitizeFilters(raw) {
  const base = defaultFilters();
  if (!raw || typeof raw !== "object" || Array.isArray(raw)) return base;
  const triEnum = (v) => (v === "yes" || v === "no" ? v : "any");
  const stringArray = (v) => (Array.isArray(v) ? v.filter((x) => typeof x === "string") : []);
  return {
    search: typeof raw.search === "string" ? raw.search : "",
    chapters: stringArray(raw.chapters),
    pipelineStates: stringArray(raw.pipelineStates),
    taskStatuses: stringArray(raw.taskStatuses),
    hasDialogue: triEnum(raw.hasDialogue),
    hasQa: triEnum(raw.hasQa),
    hasLocked: triEnum(raw.hasLocked),
  };
}

/** @param {QueueFilters} filters */
function saveFilters(filters) {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(filters));
  } catch {
    // localStorage may be disabled — degrade gracefully
  }
}

/**
 * @param {HTMLElement} container
 * @param {{loadScenes: ({force?: boolean}?) => Promise<any>}} ctx
 * @returns {() => void}
 */
export function renderSceneQueue(container, { loadScenes }) {
  /** @type {QueueFilters} */
  let filters = loadFilters();

  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    const refresh = target.closest("[data-scenes-refresh]");
    if (refresh) {
      document.dispatchEvent(new CustomEvent("scenes:refresh"));
      return;
    }
    const facetBtn = target.closest("[data-facet-toggle]");
    if (facetBtn) {
      const facet = facetBtn.getAttribute("data-facet-toggle");
      const value = facetBtn.getAttribute("data-facet-value") || "";
      toggleFacetValue(filters, facet, value);
      saveFilters(filters);
      rerender();
      return;
    }
    const facetRadio = target.closest("[data-facet-radio]");
    if (facetRadio) {
      const facet = facetRadio.getAttribute("data-facet-radio");
      const value = facetRadio.getAttribute("data-facet-value") || "any";
      if (facet === "hasDialogue") filters.hasDialogue = value;
      if (facet === "hasQa") filters.hasQa = value;
      if (facet === "hasLocked") filters.hasLocked = value;
      saveFilters(filters);
      rerender();
      return;
    }
    if (target.closest("[data-facets-reset]")) {
      filters = defaultFilters();
      saveFilters(filters);
      rerender();
      return;
    }
  };

  const handleInput = (event) => {
    const target = /** @type {HTMLInputElement} */ (event.target);
    if (target.matches("[data-search-input]")) {
      filters.search = target.value;
      saveFilters(filters);
      rerender();
    }
  };

  container.addEventListener("click", handleClick);
  container.addEventListener("input", handleInput);

  function rerender() {
    const data = scenesData$.value;
    container.className = "app-shell";
    container.innerHTML = renderQueuePage(data, filters);
    // 保留搜尋框 focus
    const searchInput = container.querySelector("[data-search-input]");
    if (searchInput instanceof HTMLInputElement && document.activeElement?.matches("[data-search-input]")) {
      const len = searchInput.value.length;
      searchInput.focus();
      searchInput.setSelectionRange(len, len);
    }
  }

  const unsubscribe = scenesData$.subscribe(() => rerender());

  return () => {
    container.removeEventListener("click", handleClick);
    container.removeEventListener("input", handleInput);
    unsubscribe();
  };
}

function toggleFacetValue(filters, facet, value) {
  const list = filters[facet];
  if (!Array.isArray(list)) return;
  const idx = list.indexOf(value);
  if (idx >= 0) {
    list.splice(idx, 1);
  } else {
    list.push(value);
  }
}

function applyFilters(scenes, filters) {
  const norm = (s) => String(s || "").toLowerCase();
  const needle = norm(filters.search).trim();
  return scenes.filter((scene) => {
    // Chapter
    if (filters.chapters.length > 0) {
      const ch = scene.chapter || "__unassigned__";
      if (!filters.chapters.includes(ch)) return false;
    }
    // Pipeline State
    if (filters.pipelineStates.length > 0) {
      if (!filters.pipelineStates.includes(scene.pipeline_state)) return false;
    }
    // Task Status
    if (filters.taskStatuses.length > 0) {
      const ts = scene.task_status || "__none__";
      if (!filters.taskStatuses.includes(ts)) return false;
    }
    // Has Dialogue
    if (filters.hasDialogue !== "any") {
      const has = (scene.dialogue_count || 0) > 0;
      if (filters.hasDialogue === "yes" && !has) return false;
      if (filters.hasDialogue === "no" && has) return false;
    }
    // Has QA
    if (filters.hasQa !== "any") {
      const has = (scene.qa_report_count || 0) > 0;
      if (filters.hasQa === "yes" && !has) return false;
      if (filters.hasQa === "no" && has) return false;
    }
    // Has LOCKED version
    if (filters.hasLocked !== "any") {
      const versions = Array.isArray(scene.dialogue_versions) ? scene.dialogue_versions : [];
      const hasLocked = versions.some((v) => v.status === "LOCKED");
      if (filters.hasLocked === "yes" && !hasLocked) return false;
      if (filters.hasLocked === "no" && hasLocked) return false;
    }
    // Search — scene_id / chapter / pipeline_state / task_path / task_status
    if (needle) {
      const haystack = [
        scene.scene_id, scene.chapter, scene.pipeline_state,
        scene.task_path, scene.task_status,
      ].map(norm).join(" ");
      if (!haystack.includes(needle)) return false;
    }
    return true;
  });
}

function activeFilterCount(filters) {
  let n = 0;
  if (filters.search && filters.search.trim()) n += 1;
  n += filters.chapters.length;
  n += filters.pipelineStates.length;
  n += filters.taskStatuses.length;
  if (filters.hasDialogue !== "any") n += 1;
  if (filters.hasQa !== "any") n += 1;
  if (filters.hasLocked !== "any") n += 1;
  return n;
}

function renderQueuePage(data, filters) {
  const loading = data.loading;
  const error = data.error;
  const payload = data.data;
  const allScenes = Array.isArray(payload?.scenes) ? payload.scenes : [];
  const chapters = Array.isArray(payload?.chapters) ? payload.chapters : [];
  const filtered = applyFilters(allScenes, filters);
  const refreshedAt = formatDateTime(data.refreshedAt);
  const activeCount = activeFilterCount(filters);

  return `
    <section class="dashboard-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁 / Dashboard</a> /
            Scene Queue
          </p>
          <div class="project-title-row">
            <h1 class="project-name">Scene Queue / 場景列表</h1>
            <span class="badge ${loading ? "warning" : "success"}">${filtered.length} / ${allScenes.length} 場</span>
          </div>
          <p class="meta-text">最後更新：${escapeHtml(refreshedAt)}</p>
        </div>
        <div class="project-actions" aria-label="Scene Queue controls">
          <a class="link-button" href="#/">← Dashboard</a>
          <button class="button" type="button" data-scenes-refresh ${loading ? "disabled" : ""}>手動 refresh</button>
        </div>
      </header>

      ${error ? `<div class="fallback-message" role="status">${escapeHtml(error)}</div>` : ""}

      ${renderFacetPanel(filters, allScenes, chapters, filtered.length, activeCount)}

      ${renderChapterGroups(filtered, chapters, allScenes.length === 0 && !loading)}
    </section>
  `;
}

function renderFacetPanel(filters, allScenes, chapters, filteredCount, activeCount) {
  const stateCounts = countByPipelineState(allScenes);
  const taskStatusCounts = countByTaskStatus(allScenes);
  const chapterCounts = countByChapter(allScenes);
  const filterSummary = filterSummaryText(filters);

  return `
    <section class="panel scene-queue-facet">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">F6 Search + Filter — §11.4</p>
          <h2>搜尋 + 篩選</h2>
        </div>
        ${activeCount > 0 ? `
          <button class="button ghost" type="button" data-facets-reset>清除所有篩選 (${activeCount})</button>
        ` : ""}
      </div>

      <div class="facet-search-row">
        <label class="facet-search-label">
          <span class="meta-text">🔍 全文搜尋</span>
          <input
            type="search"
            data-search-input
            placeholder="輸入 scene ID / chapter / pipeline state / task path..."
            value="${escapeAttr(filters.search || "")}"
            class="facet-search-input"
          />
        </label>
        ${filteredCount === 0 ? `<span class="meta-text">無結果</span>` : ""}
      </div>

      <div class="facet-grid">
        ${renderMultiFacet("Chapter / 章別", "chapters", filters.chapters,
          buildChapterFacetItems(chapterCounts, chapters))}

        ${renderMultiFacet("Pipeline State / 狀態", "pipelineStates", filters.pipelineStates,
          buildEnumFacetItems(stateCounts, ["DRAFT", "REVIEW", "LOCKED", "DEPRECATED", "未啟動", "FINAL"]))}

        ${renderMultiFacet("Task Status / 任務包狀態", "taskStatuses", filters.taskStatuses,
          buildEnumFacetItems(taskStatusCounts, ["DRAFT", "REVIEW", "LOCKED", "__none__"]))}

        ${renderTriFacet("Has Dialogue / 是否有 dialogue", "hasDialogue", filters.hasDialogue)}
        ${renderTriFacet("Has QA / 是否有 QA", "hasQa", filters.hasQa)}
        ${renderTriFacet("Has LOCKED Version / 是否有 LOCKED 版", "hasLocked", filters.hasLocked)}
      </div>

      ${activeCount > 0 ? `<p class="meta-text">已套用 ${activeCount} 個 facet — ${filterSummary}</p>` : ""}

      ${filteredCount > 0 && activeCount > 0 ? `
        <div class="facet-export-row">
          <span class="meta-text">當前 ${filteredCount} 場 ID：</span>
          ${renderCopyCommandButton({
            command: "/qa " + getFilteredIds(allScenes, filters).slice(0, 20).join(","),
            label: `📋 複製批次 /qa 指令 (${Math.min(20, filteredCount)} 場)`,
            source: "Scene Queue / Filtered Batch Export",
            contextNotes: filteredCount > 20 ? `Showing first 20 of ${filteredCount} filtered scenes` : undefined,
            targetAgent: "any",
            variant: "secondary",
            size: "sm",
          })}
        </div>
      ` : ""}

      <p class="note-text">
        Persisted state via localStorage('${STORAGE_KEY}')。Mode Tag / Characters 維 facet 待 backend 擴充 — [BLOCKED:UPSTREAM_DOWNSTREAM]。
      </p>
    </section>
  `;
}

function getFilteredIds(allScenes, filters) {
  return applyFilters(allScenes, filters).map((s) => s.scene_id);
}

/**
 * Build the active-filter summary as escaped HTML.
 *
 * Phase A.0F.patch-P1: previously this returned a raw string assembled from
 * `filters.search`/`filters.chapters`/... which then got dropped into
 * innerHTML at the call site. Anything the user types into the search field
 * (including <img src=x onerror=...>) flowed through unescaped — the search
 * value is persisted in localStorage and rerendered on every keystroke, so
 * the sink was always live. CODEX P1 finding.
 *
 * Each token now goes through escapeHtml() before joining. Numeric-style
 * enums (chapter list / pipeline state list / task status list) also pass
 * through escapeHtml even though they come from server data, because facet
 * keys can be added by future schema and we want a single safe path.
 */
function filterSummaryText(filters) {
  const parts = [];
  if (filters.search) parts.push(`搜尋 "${escapeHtml(filters.search)}"`);
  if (filters.chapters.length) parts.push(`Ch ${filters.chapters.map(escapeHtml).join("/")}`);
  if (filters.pipelineStates.length) parts.push(`狀態 ${filters.pipelineStates.map(escapeHtml).join("/")}`);
  if (filters.taskStatuses.length) parts.push(`任務包 ${filters.taskStatuses.map(escapeHtml).join("/")}`);
  if (filters.hasDialogue !== "any") parts.push(`Dialogue=${escapeHtml(filters.hasDialogue)}`);
  if (filters.hasQa !== "any") parts.push(`QA=${escapeHtml(filters.hasQa)}`);
  if (filters.hasLocked !== "any") parts.push(`LOCKED=${escapeHtml(filters.hasLocked)}`);
  return parts.join("；");
}

function renderMultiFacet(label, facetKey, selected, items) {
  return `
    <fieldset class="facet-group">
      <legend>${escapeHtml(label)}</legend>
      <div class="facet-chip-row">
        ${items.map((item) => `
          <button
            type="button"
            class="facet-chip ${selected.includes(item.value) ? "facet-chip--active" : ""} ${item.count === 0 ? "facet-chip--empty" : ""}"
            data-facet-toggle="${escapeAttr(facetKey)}"
            data-facet-value="${escapeAttr(item.value)}"
            ${item.count === 0 ? "disabled" : ""}
          >${escapeHtml(item.label)} <span class="facet-chip-count">${item.count}</span></button>
        `).join("")}
      </div>
    </fieldset>
  `;
}

function renderTriFacet(label, facetKey, current) {
  const opts = [
    { value: "any", label: "全部" },
    { value: "yes", label: "Yes" },
    { value: "no", label: "No" },
  ];
  return `
    <fieldset class="facet-group">
      <legend>${escapeHtml(label)}</legend>
      <div class="facet-chip-row">
        ${opts.map((opt) => `
          <button
            type="button"
            class="facet-chip ${current === opt.value ? "facet-chip--active" : ""}"
            data-facet-radio="${escapeAttr(facetKey)}"
            data-facet-value="${escapeAttr(opt.value)}"
          >${escapeHtml(opt.label)}</button>
        `).join("")}
      </div>
    </fieldset>
  `;
}

function buildChapterFacetItems(counts, chapters) {
  const items = chapters.map((ch) => ({
    value: ch,
    label: `Ch ${ch}`,
    count: counts[ch] || 0,
  }));
  if ((counts.__unassigned__ || 0) > 0) {
    items.push({ value: "__unassigned__", label: "未分章", count: counts.__unassigned__ });
  }
  return items;
}

function buildEnumFacetItems(counts, enumValues) {
  const items = [];
  for (const v of enumValues) {
    const label = v === "__none__" ? "(未建立)" : v;
    items.push({ value: v, label, count: counts[v] || 0 });
  }
  // 補上其他不在 enum 的（如未來新狀態）
  for (const v of Object.keys(counts)) {
    if (!enumValues.includes(v)) {
      items.push({ value: v, label: v, count: counts[v] });
    }
  }
  return items;
}

function countByPipelineState(scenes) {
  const out = {};
  for (const s of scenes) {
    const k = s.pipeline_state || "未啟動";
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

function countByTaskStatus(scenes) {
  const out = {};
  for (const s of scenes) {
    const k = s.task_status || "__none__";
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

function countByChapter(scenes) {
  const out = {};
  for (const s of scenes) {
    const k = s.chapter || "__unassigned__";
    out[k] = (out[k] || 0) + 1;
  }
  return out;
}

function renderChapterGroups(scenes, allChapters, sourceEmpty) {
  if (sourceEmpty) {
    return `
      <div class="empty-state">
        *目前無場景 — 可能尚未建立任何 S-* entity 或 dialogue 檔。可考慮跑 /create-outline + /create-detailed-outline 建立場景骨架。*
      </div>
    `;
  }
  if (scenes.length === 0) {
    return `
      <div class="empty-state">
        *目前篩選條件下無場景符合。*<br><br>
        可考慮：清除部分 facet（如取消 Ch 限制）；用 fuzzy 搜尋替代精確 ID 搜尋；確認場景索引 06_a_場景索引.md 是否包含目標場景。
      </div>
    `;
  }

  const groups = new Map();
  for (const ch of allChapters) groups.set(ch, []);
  groups.set("__unassigned__", []);
  for (const scene of scenes) {
    const ch = scene.chapter || "__unassigned__";
    if (!groups.has(ch)) groups.set(ch, []);
    groups.get(ch).push(scene);
  }

  return Array.from(groups.entries())
    .filter(([_, list]) => list.length > 0)
    .map(([chapter, list]) => renderChapterGroup(chapter, list))
    .join("");
}

function renderChapterGroup(chapter, scenes) {
  const label = chapter === "__unassigned__"
    ? "未分章 / Unassigned"
    : `第 ${chapter} 章 / Chapter ${chapter}`;
  return `
    <section class="panel scene-queue-group" aria-label="${escapeAttr(label)}">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Chapter Group</p>
          <h2>${escapeHtml(label)}</h2>
        </div>
        <span class="chip">${scenes.length} 場</span>
      </div>
      <div class="scene-card-grid">
        ${scenes.map(renderSceneCard).join("")}
      </div>
    </section>
  `;
}

function renderSceneCard(scene) {
  const sid = scene.scene_id;
  const versions = Array.isArray(scene.dialogue_versions) ? scene.dialogue_versions : [];
  const versionList = versions.map((v) => v.version).filter(Boolean).join(" / ") || "—";
  const lastMtime = formatRelativeTime(scene.latest_mtime);
  const pipelineState = scene.pipeline_state || "未啟動";
  const stateTone = pipelineStateTone(pipelineState);
  const nextFix = inferNextFix(scene);

  return `
    <article class="scene-card">
      <header class="scene-card-header">
        <div>
          <span class="scene-card-id">${escapeHtml(sid)}</span>
          ${scene.chapter ? `<span class="meta-text">Ch ${escapeHtml(scene.chapter)}</span>` : ""}
        </div>
        <span class="badge ${stateTone}">${escapeHtml(pipelineState)}</span>
      </header>
      <dl class="scene-card-meta">
        <div>
          <dt>任務包 / Task</dt>
          <dd>${scene.task_path ? `<span class="meta-text">${escapeHtml(scene.task_status || "—")}</span>` : `<span class="meta-text">未建立</span>`}</dd>
        </div>
        <div>
          <dt>Dialogue 版本</dt>
          <dd>${escapeHtml(String(scene.dialogue_count || 0))} 版 (${escapeHtml(versionList)})</dd>
        </div>
        <div>
          <dt>QA 報告</dt>
          <dd>${escapeHtml(String(scene.qa_report_count || 0))} 份</dd>
        </div>
        <div>
          <dt>實體</dt>
          <dd>${escapeHtml(String(scene.entities_count || 0))} 個</dd>
        </div>
        <div>
          <dt>最後修改</dt>
          <dd>${escapeHtml(lastMtime)}</dd>
        </div>
      </dl>
      <p class="scene-card-next-fix">
        <strong>下一步 / Next Fix：</strong>${escapeHtml(nextFix)}
      </p>
      <div class="card-actions">
        <a class="link-button primary" href="#/scene/${encodeURIComponent(sid)}">
          → 進入場景 cockpit / Enter Scene Detail
        </a>
      </div>
    </article>
  `;
}

function inferNextFix(scene) {
  const state = scene.pipeline_state || "";
  if (state === "未啟動") {
    if (!scene.task_path) return "建立任務包：跑 /create-scene-task " + scene.scene_id;
    return "啟動試寫：跑 /dialogue-write " + scene.scene_id;
  }
  if (state === "DRAFT") {
    if ((scene.qa_report_count || 0) === 0) return "跑首輪 QA：/qa " + scene.scene_id;
    return "審 DRAFT 後升 REVIEW";
  }
  if (state === "REVIEW") return "通過 REVIEW gate 後升 FINAL";
  if (state === "LOCKED") return "場景已 LOCKED — 編輯需走降級流程（§11.5 Z2 candidate α）";
  if (state === "DEPRECATED") return "場景已 DEPRECATED — 不影響定稿；可考慮新版";
  return "—";
}

function pipelineStateTone(state) {
  if (!state) return "warning";
  if (state === "LOCKED") return "warning";
  if (state === "DEPRECATED") return "warning";
  if (state === "REVIEW") return "success";
  if (state === "FINAL") return "success";
  if (state === "未啟動") return "warning";
  return "";
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

function formatRelativeTime(mtime) {
  if (!mtime) return "未修改";
  const date = new Date(mtime * 1000);
  if (Number.isNaN(date.getTime())) return "未修改";
  const now = Date.now();
  const diffMs = now - date.getTime();
  const day = 24 * 60 * 60 * 1000;
  if (diffMs < day) return "今天";
  if (diffMs < 7 * day) return `${Math.floor(diffMs / day)} 天前`;
  return new Intl.DateTimeFormat("zh-Hant", { dateStyle: "short" }).format(date);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttr(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}
