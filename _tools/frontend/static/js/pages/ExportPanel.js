/**
 * Export Panel — L3 Bundle Export A1 prompt UI（UX_SPEC §11.6.11 + ARCH §4.2a）
 *
 * 對齊 _design/L3_EXPORT_PROMPT_SCHEMA.md v0.2 + D-038 A1 流程：
 *   - 範圍 / 格式 / 路徑 / 推送方式選擇
 *   - 預覽 prompt modal
 *   - 推送方式 3 種：clipboard（必做）/ local_llm_endpoint（必做）/ Claude/OpenAI API (Phase C+ disabled)
 *   - schema_version "1.0" 鎖（promptAssembler.js 內 const）
 *   - CC-07 校正內化（無 rerun_qa / 含 include_deleted / read_only 禁 phase_log）
 *
 * 對齊 D-029 (α)：前端不執行 export 邏輯；只組 prompt → clipboard / POST 給外部 agent。
 */

// Note: audit-P2 cleanup — unused `state` import removed
import {
  assembleExportPrompt,
  defaultOutputPaths,
  formatIsoTimestamp,
  PROMPT_SCHEMA_VERSION,
} from "../components/promptAssembler.js";
import {
  copyToClipboard,
  showCopyToast,
  showCopyFallbackModal,
} from "../components/CopyCommandButton.js";
import { fetchScopeCounts } from "../api.js";

const STORAGE_KEY = "export-panel-state-v1";
const PUSH_TIMEOUT_MS = 30000;  // 30s timeout per ARCH §4.2a.2

/** @typedef {{
 *   scopeType: "full"|"outline_only"|"scene",
 *   sceneId: string,
 *   formatJson: boolean,
 *   formatMd: boolean,
 *   includeDeleted: boolean,
 *   pushMode: "clipboard"|"local_llm_endpoint",
 *   endpointUrl: string,
 *   endpointAuth: string,
 *   endpointModel: string,
 *   customPathJson: string,
 *   customPathMd: string,
 *   useCustomPaths: boolean
 * }} ExportFormState */

function defaultState() {
  return {
    scopeType: "full",
    sceneId: "",
    formatJson: true,
    formatMd: true,
    includeDeleted: false,
    pushMode: "clipboard",
    endpointUrl: "",
    endpointAuth: "",
    endpointModel: "",
    customPathJson: "",
    customPathMd: "",
    useCustomPaths: false,
  };
}

function loadState() {
  if (typeof window === "undefined") return defaultState();
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) return defaultState();
    return { ...defaultState(), ...JSON.parse(raw) };
  } catch {
    return defaultState();
  }
}

function saveState(s) {
  if (typeof window === "undefined") return;
  try {
    // Don't persist sensitive auth token by default — keep URL + model only
    const persistable = { ...s, endpointAuth: "" };
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(persistable));
  } catch {
    // ignore
  }
}

/**
 * @param {HTMLElement} container
 * @returns {() => void}
 */
export function renderExportPanel(container) {
  /** @type {ExportFormState} */
  let formState = loadState();
  let scopeCountsState = { loading: false, data: null, error: null };

  function rerender() {
    // Bug 2 fix (audit-P1): 保存 active input field + cursor，rerender 後還原；
    // 否則 user 每按一鍵就失焦無法連續輸入。Pattern 對齊 SceneQueue.js focus restore。
    const active = document.activeElement;
    let savedFocus = null;
    if (active && active.matches && active.matches("[data-export-field]")) {
      savedFocus = {
        field: active.getAttribute("data-export-field"),
        selectionStart: typeof active.selectionStart === "number" ? active.selectionStart : null,
        selectionEnd: typeof active.selectionEnd === "number" ? active.selectionEnd : null,
      };
    }
    container.className = "app-shell";
    container.innerHTML = renderPage(formState, scopeCountsState);
    if (savedFocus) {
      const sel = `[data-export-field="${savedFocus.field}"]`;
      const next = container.querySelector(sel);
      if (next instanceof HTMLInputElement) {
        next.focus();
        if (savedFocus.selectionStart !== null) {
          try { next.setSelectionRange(savedFocus.selectionStart, savedFocus.selectionEnd); } catch {}
        }
      }
    }
  }

  // 抓 stats（給 prompt YAML 註解 + UI 顯示）
  function refreshScopeCounts() {
    // Phase A.0F.patch-round2-P2 / option (a) wiring: outline_only now has
    // first-class /api/scope-counts support; previously this branch fell
    // through to "full", which then injected full-scope stats into the
    // outline_only prompt YAML comments (CODEX 2nd-round drift).
    let scopeArg = "full";
    if (formState.scopeType === "scene" && formState.sceneId) {
      scopeArg = `scene/${formState.sceneId}`;
    } else if (formState.scopeType === "outline_only") {
      scopeArg = "outline_only";
    }
    scopeCountsState = { loading: true, data: null, error: null };
    rerender();
    fetchScopeCounts(scopeArg)
      .then((data) => { scopeCountsState = { loading: false, data, error: null }; rerender(); })
      .catch((err) => { scopeCountsState = { loading: false, data: null, error: err?.message || "load failed" }; rerender(); });
  }

  function currentPrompt() {
    const scope = buildScope(formState);
    // Phase A.0F.patch-round2-P2 / option (b) defensive fallback: do NOT inject
    // stats into the prompt YAML when scope-counts failed or has not returned
    // yet. Injecting partial / wrong-scope counts misleads the downstream
    // agent (CODEX 2nd-round drift finding). When the API returns successfully
    // for the chosen scope, the comments still ship as before.
    const statsScope = scopeCountsState.data?.scope;
    const expectedScopeArg = (
      formState.scopeType === "scene" && formState.sceneId
        ? `scene/${formState.sceneId}`
        : formState.scopeType === "outline_only"
          ? "outline_only"
          : "full"
    );
    const stats = (
      scopeCountsState.error || !scopeCountsState.data || statsScope !== expectedScopeArg
        ? undefined
        : scopeCountsState.data.counts
    );
    let outputPaths = undefined;
    if (formState.useCustomPaths && (formState.customPathJson || formState.customPathMd)) {
      const def = defaultOutputPaths(scope);
      outputPaths = {
        json: formState.customPathJson || def.json,
        md: formState.customPathMd || def.md,
      };
    }
    return assembleExportPrompt({
      scope,
      formats: { json: formState.formatJson, md: formState.formatMd },
      includeDeleted: formState.includeDeleted,
      outputPaths,
      stats,
    });
  }

  async function doCopy() {
    try {
      const prompt = currentPrompt();
      const result = await copyToClipboard(prompt);
      if (result.ok) {
        showCopyToast({
          variant: "success",
          title: "✓ 已複製 L3 Export prompt 到剪貼簿",
          body: "請貼到 Claude Code / Codex / 本地 LLM endpoint 跑（read_only mode）。",
          duration: 6000,
        });
      } else {
        showCopyFallbackModal(prompt);
      }
    } catch (err) {
      showCopyToast({
        variant: "error",
        title: "⚠ 組 prompt 失敗",
        body: err instanceof Error ? err.message : String(err),
      });
    }
  }

  async function doPush() {
    try {
      const prompt = currentPrompt();
      if (!formState.endpointUrl) {
        showCopyToast({ variant: "error", title: "⚠ 未設定 endpoint URL" });
        return;
      }
      const headers = { "Content-Type": "application/json" };
      if (formState.endpointAuth) headers["Authorization"] = `Bearer ${formState.endpointAuth}`;
      const body = JSON.stringify({
        prompt,
        format: "json",
        model: formState.endpointModel || undefined,
        schema_version: PROMPT_SCHEMA_VERSION,
      });

      const controller = new AbortController();
      const timeoutId = window.setTimeout(() => controller.abort(), PUSH_TIMEOUT_MS);
      showCopyToast({ variant: "success", title: "推送中...", body: `POST ${formState.endpointUrl}`, duration: PUSH_TIMEOUT_MS });

      const resp = await fetch(formState.endpointUrl, {
        method: "POST",
        headers,
        body,
        signal: controller.signal,
      });
      window.clearTimeout(timeoutId);
      if (resp.ok) {
        showCopyToast({
          variant: "success",
          title: "✓ 已推送",
          body: `${resp.status} ${resp.statusText}`,
          duration: 6000,
        });
      } else {
        showCopyToast({
          variant: "error",
          title: `⚠ 推送失敗 ${resp.status}`,
          body: resp.statusText,
        });
      }
    } catch (err) {
      const msg = err?.name === "AbortError"
        ? `推送超時 (${PUSH_TIMEOUT_MS / 1000}s)`
        : (err instanceof Error ? err.message : String(err));
      showCopyToast({ variant: "error", title: "⚠ 推送失敗", body: msg });
    }
  }

  function openPreviewModal() {
    try {
      const prompt = currentPrompt();
      openPromptPreview(prompt);
    } catch (err) {
      showCopyToast({
        variant: "error",
        title: "⚠ 組 prompt 失敗",
        body: err instanceof Error ? err.message : String(err),
      });
    }
  }

  const handleInput = (event) => {
    const target = /** @type {HTMLInputElement} */ (event.target);
    const field = target.getAttribute("data-export-field");
    if (!field) return;
    if (target.type === "checkbox") {
      formState[field] = target.checked;
    } else {
      formState[field] = target.value;
    }
    saveState(formState);
    rerender();
  };

  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    if (target.closest("[data-export-refresh-stats]")) { refreshScopeCounts(); return; }
    if (target.closest("[data-export-preview]")) { openPreviewModal(); return; }
    if (target.closest("[data-export-copy]")) { doCopy(); return; }
    if (target.closest("[data-export-push]")) { doPush(); return; }
    if (target.closest("[data-export-reset]")) {
      formState = defaultState();
      saveState(formState);
      rerender();
      return;
    }
    const scopeRadio = target.closest("[data-export-scope-radio]");
    if (scopeRadio) {
      formState.scopeType = scopeRadio.getAttribute("data-export-scope-radio");
      saveState(formState);
      rerender();
      return;
    }
    const pushRadio = target.closest("[data-export-push-radio]");
    if (pushRadio) {
      formState.pushMode = pushRadio.getAttribute("data-export-push-radio");
      saveState(formState);
      rerender();
      return;
    }
  };

  container.addEventListener("input", handleInput);
  container.addEventListener("click", handleClick);
  rerender();
  refreshScopeCounts();

  return () => {
    container.removeEventListener("input", handleInput);
    container.removeEventListener("click", handleClick);
  };
}

function buildScope(formState) {
  // Phase A.0F.patch-major-2 / L3 schema drift: schema v0.2 only allows
  // full | outline_only | scene. `chapter` scope was a UI-only feature that
  // never matched a schema enum — CODEX Major finding §3. UI radio drops the
  // chapter option below.
  const scope = { type: formState.scopeType };
  if (formState.scopeType === "scene") scope.sceneId = formState.sceneId || "(unset)";
  return scope;
}

function renderPage(formState, scopeCountsState) {
  const scope = buildScope(formState);
  const defPaths = defaultOutputPaths(scope);
  const counts = scopeCountsState.data?.counts;
  const refreshedHint = scopeCountsState.loading
    ? "stats 同步中..."
    : scopeCountsState.error
      ? `stats 載入失敗：${scopeCountsState.error}`
      : counts
        ? `stats: ${JSON.stringify(counts)}`
        : "尚未取 stats";

  return `
    <section class="dashboard-container export-panel-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁 / Dashboard</a> /
            Export Panel
          </p>
          <div class="project-title-row">
            <h1 class="project-name">Layer 3 Bundle Export</h1>
            <span class="badge success">schema v${PROMPT_SCHEMA_VERSION}</span>
          </div>
          <p class="meta-text">D-038 A1 流程 + L3_EXPORT_PROMPT_SCHEMA v0.2 + CC-07 校正</p>
        </div>
        <div class="project-actions">
          <a class="link-button" href="#/">← Dashboard</a>
          <button class="button ghost" type="button" data-export-reset>重置表單</button>
        </div>
      </header>

      <section class="panel export-form-panel">
        <div class="panel-title">
          <p class="eyebrow">Export Configuration</p>
          <h2>範圍 / 格式 / 路徑 / 推送</h2>
        </div>

        <!-- 範圍 -->
        <fieldset class="facet-group">
          <legend>範圍 / Scope</legend>
          <div class="export-radio-row">
            ${renderScopeRadio(formState, "full", "全部 / Full")}
            ${renderScopeRadio(formState, "outline_only", "僅大綱 / Outline only")}
            ${renderScopeRadio(formState, "scene", "僅本場景 / Single scene")}
            <!-- Phase A.0F.patch-major-2: chapter scope 已移除 — L3_EXPORT_PROMPT_SCHEMA
                 v0.2 §1.2 未列；如需 chapter scope 必須先升 schema_version 並走 D-NNN 拍板 -->
          </div>
          ${formState.scopeType === "scene" ? `
            <label class="export-input-row">
              <span class="meta-text">Scene ID：</span>
              <input type="text" class="export-input" data-export-field="sceneId"
                value="${escapeAttr(formState.sceneId)}" placeholder="S-01-03" />
            </label>
          ` : ""}
        </fieldset>

        <!-- 格式 -->
        <fieldset class="facet-group">
          <legend>格式 / Formats</legend>
          <div class="export-check-row">
            <label><input type="checkbox" data-export-field="formatJson" ${formState.formatJson ? "checked" : ""}/> JSON</label>
            <label><input type="checkbox" data-export-field="formatMd" ${formState.formatMd ? "checked" : ""}/> MD</label>
            <label title="含 status=deleted 的 dialogue_line (CC-07)">
              <input type="checkbox" data-export-field="includeDeleted" ${formState.includeDeleted ? "checked" : ""}/>
              含已刪除 KEY (include_deleted)
            </label>
          </div>
        </fieldset>

        <!-- 路徑 -->
        <fieldset class="facet-group">
          <legend>路徑 / Output Paths</legend>
          <label class="export-check-row">
            <input type="checkbox" data-export-field="useCustomPaths" ${formState.useCustomPaths ? "checked" : ""}/>
            自訂路徑（預設依 scope 自動）
          </label>
          ${formState.useCustomPaths ? `
            <label class="export-input-row">
              <span class="meta-text">JSON：</span>
              <input type="text" class="export-input" data-export-field="customPathJson"
                value="${escapeAttr(formState.customPathJson)}" placeholder="${escapeAttr(defPaths.json)}" />
            </label>
            <label class="export-input-row">
              <span class="meta-text">MD：</span>
              <input type="text" class="export-input" data-export-field="customPathMd"
                value="${escapeAttr(formState.customPathMd)}" placeholder="${escapeAttr(defPaths.md)}" />
            </label>
          ` : `
            <p class="meta-text">預設：${escapeHtml(defPaths.json)} + ${escapeHtml(defPaths.md)}</p>
          `}
        </fieldset>

        <!-- 推送方式 -->
        <fieldset class="facet-group">
          <legend>推送方式 / Push Mode</legend>
          <div class="export-radio-row">
            ${renderPushRadio(formState, "clipboard", "Clipboard（預設）")}
            ${renderPushRadio(formState, "local_llm_endpoint", "POST 到本地 LLM endpoint")}
          </div>
          ${formState.pushMode === "local_llm_endpoint" ? `
            <label class="export-input-row">
              <span class="meta-text">URL：</span>
              <input type="text" class="export-input" data-export-field="endpointUrl"
                value="${escapeAttr(formState.endpointUrl)}" placeholder="http://localhost:11434/api/generate" />
            </label>
            <label class="export-input-row">
              <span class="meta-text">Bearer Auth：</span>
              <input type="password" class="export-input" data-export-field="endpointAuth"
                value="${escapeAttr(formState.endpointAuth)}" placeholder="(token; 不存 localStorage)" />
            </label>
            <label class="export-input-row">
              <span class="meta-text">Model：</span>
              <input type="text" class="export-input" data-export-field="endpointModel"
                value="${escapeAttr(formState.endpointModel)}" placeholder="llama3.1-70b" />
            </label>
            <p class="note-text">超時 ${PUSH_TIMEOUT_MS / 1000}s（ARCH §4.2a.2）。Auth token 不持久化到 localStorage。</p>
          ` : ""}
          <p class="note-text">
            POST 到 Claude API / OpenAI API：disabled in panel（Phase C+ 才開；
            對齊 L3_EXPORT_PROMPT_SCHEMA §4 lifecycle）
          </p>
        </fieldset>

        <!-- Stats preview -->
        <div class="export-stats-row">
          <span class="meta-text">📊 ${escapeHtml(refreshedHint)}</span>
          <button class="button ghost" type="button" data-export-refresh-stats ${scopeCountsState.loading ? "disabled" : ""}>
            ${scopeCountsState.loading ? "..." : "🔄 重抓 stats"}
          </button>
        </div>

        <!-- Action buttons -->
        <div class="export-action-row">
          <button class="button" type="button" data-export-preview>👁 預覽 Prompt</button>
          ${formState.pushMode === "clipboard" ? `
            <button class="button primary" type="button" data-export-copy>📋 複製 Prompt 到剪貼簿</button>
          ` : `
            <button class="button primary" type="button" data-export-push>📤 推送到 endpoint</button>
            <button class="button" type="button" data-export-copy>📋 同時複製到剪貼簿</button>
          `}
        </div>

        <p class="note-text">
          ⚠ D-029 (α) 完全分離：前端只組 prompt，不執行 export 邏輯。
          外部 agent 收到 prompt 後依 read_only mode 嚴格只讀；
          不修改 phase_log（CC-07）；不擅升狀態。
        </p>
      </section>
    </section>
  `;
}

function renderScopeRadio(formState, value, label) {
  const checked = formState.scopeType === value;
  return `
    <button type="button"
      class="facet-chip ${checked ? "facet-chip--active" : ""}"
      data-export-scope-radio="${escapeAttr(value)}"
    >${escapeHtml(label)}</button>
  `;
}

function renderPushRadio(formState, value, label) {
  const checked = formState.pushMode === value;
  return `
    <button type="button"
      class="facet-chip ${checked ? "facet-chip--active" : ""}"
      data-export-push-radio="${escapeAttr(value)}"
    >${escapeHtml(label)}</button>
  `;
}

function openPromptPreview(prompt) {
  document.querySelectorAll(".export-preview-modal").forEach((el) => el.remove());
  const modal = document.createElement("div");
  modal.className = "copy-fallback-modal export-preview-modal";
  modal.innerHTML = `
    <div class="copy-fallback-modal__backdrop" data-close></div>
    <div class="copy-fallback-modal__panel" style="max-width: 800px;">
      <header class="copy-fallback-modal__header">
        <strong>👁 L3 Export Prompt 預覽（read-only）</strong>
        <button type="button" class="copy-fallback-modal__close" aria-label="關閉" data-close>×</button>
      </header>
      <div class="copy-fallback-modal__body">
        <p>下方為依目前選項組裝出的完整 prompt，可審視後再貼出 / 推送：</p>
        <textarea class="copy-fallback-modal__textarea" readonly style="min-height: 400px;"></textarea>
      </div>
      <footer class="copy-fallback-modal__footer">
        <button type="button" class="button" data-close>關閉</button>
      </footer>
    </div>
  `;
  const ta = modal.querySelector(".copy-fallback-modal__textarea");
  if (ta instanceof HTMLTextAreaElement) ta.value = prompt;
  modal.addEventListener("click", (event) => {
    const t = event.target;
    if (t instanceof HTMLElement && t.hasAttribute("data-close")) modal.remove();
  });
  document.body.append(modal);
  if (ta instanceof HTMLTextAreaElement) {
    setTimeout(() => { ta.focus(); ta.select(); }, 0);
  }
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
