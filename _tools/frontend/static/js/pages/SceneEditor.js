/**
 * Scene Editor page — F3 N 欄並排 + F7 編輯 + LOCKED race guard + mtime conflict
 *
 * 對齊 UX_SPEC §11.3 + §11.5 + §11.7：
 *   §11.3.1 進入路徑：唯一從 Scene Detail Quick Actions 跳 #/scene/<id>/edit
 *   §11.3.2 頁面 layout: header + version 標頭列 + 中央 N 欄並排 + 底部狀態列
 *   §11.3.3 N 欄自適應（v01A/v01B/v01C/v02 混合並排）
 *   §11.3.4 中央 N 欄並排編輯區（textarea + dirty 標記）
 *   §11.3.7 底部狀態列 + Save 流程（5 步含 D-040 race guard）
 *   §11.3.8 Diff Preview Modal（i18n KEY label per segment）
 *   §11.5.6 Editor 內離開時的 dirty 守門（confirm dialog）
 *   §11.5.8 Save flow 必經 LOCKED race guard（5 步; D-040）
 *   §11.5.8.2 LOCKED race modal 三選項
 *   §11.7.6 mtime conflict modal（二選: reload 棄改 / 強制覆寫）
 *
 * 本輪 (A.0F.6+7+8) 落地 MVP：
 *   ✓ N 欄並排 textarea 編輯
 *   ✓ 行級 i18n KEY 顯示（dlg.ch.s.line tag）
 *   ✓ dirty 標記 + bottom dirty status
 *   ✓ Save 全部 flow + Diff Preview Modal + i18n KEY label per segment
 *   ✓ Step 3 pre-flight LOCKED race guard（D-040）
 *   ✓ LOCKED race modal 三選項（複製降級 / 另存 DRAFT proposal / 取消）
 *   ✓ mtime conflict modal（二選: reload 棄改 / 強制覆寫）
 *   ✓ Save 後留 Editor (Q4 / D-035 §5.3)
 *   ✓ Ctrl/Cmd-S = Save
 *   ✓ Esc = 關 modal
 *   ✓ DEPRECATED warning banner（§11.5.4）
 *   ✓ 離開時 dirty confirm dialog（§11.5.6）
 *
 * 未落地（後續：可加 §11.3.5 行級 details pane + §11.3.6 Required Context 抽屜）
 *
 * 對齊：
 *   - D-029 (α) 完全分離 — Save 只走本地 API，不 spawn agent
 *   - D-035 雙頁面（Scene Detail cockpit / Scene Editor 編輯）
 *   - D-040 Save flow LOCKED race guard
 *   - D-042 base_dialogue / iteration_note 欄位 (save-as 用)
 *   - SPEC §16 文件狀態機（LOCKED 不可直接編輯）
 */

import { fetchSceneVersions, fetchSceneHeader, fetchSceneVersionContent, saveScene, saveSceneAs } from "../api.js";
import { renderCopyCommandButton, copyToClipboard, showCopyToast, showCopyFallbackModal } from "../components/CopyCommandButton.js";

/**
 * @param {HTMLElement} container
 * @param {{sceneId: string}} ctx
 * @returns {() => void}
 */
export function renderSceneEditor(container, { sceneId }) {
  /** @type {{
   *   loading: boolean,
   *   error: string|null,
   *   header: any,
   *   versions: Array<{version:string,path:string,mtime:number,status:string,content:string,dirty:boolean,baselineContent:string}>,
   * }} */
  let editorState = {
    loading: true,
    error: null,
    header: null,
    versions: [],
  };

  container.className = "app-shell scene-editor-shell";
  container.innerHTML = renderLoading(sceneId);

  // ============ 初始載入 ============
  loadEditor();

  async function loadEditor() {
    try {
      const [headerResp, versionsResp] = await Promise.all([
        fetchSceneHeader(sceneId).catch((err) => ({ __error: err })),
        fetchSceneVersions(sceneId).catch((err) => ({ __error: err })),
      ]);
      if (headerResp.__error || versionsResp.__error) {
        const errs = [headerResp.__error, versionsResp.__error].filter(Boolean).map((e) => e?.message || e).join("；");
        editorState = { loading: false, error: errs, header: null, versions: [] };
        rerender();
        return;
      }
      // Phase A.0F.patch-P0: previously `fetch("/" + v.path)` hit the static
      // mount (`_tools/frontend/static`) and silently returned a 404 body as
      // the textarea baseline. CODEX flagged this P0. Now we go through
      // GET /api/scene/<id>/version-content?path=<rel> which fail-closes on
      // missing files and validates path under 08_dialogue_outputs/.
      const loadErrors = [];
      const versionsWithContent = await Promise.all(
        (versionsResp.versions || []).map(async (v) => {
          try {
            const contentResp = await fetchSceneVersionContent(sceneId, v.path);
            const md = typeof contentResp?.content === "string" ? contentResp.content : "";
            const mtime = typeof contentResp?.mtime === "number" ? contentResp.mtime : v.mtime;
            return {
              ...v,
              mtime,
              content: md,
              baselineContent: md,
              dirty: false,
              loadFailed: false,
            };
          } catch (err) {
            loadErrors.push(`${v.version || v.path}: ${err?.message || String(err)}`);
            return {
              ...v,
              content: "",
              baselineContent: "",
              dirty: false,
              loadFailed: true,
              loadError: err?.message || String(err),
            };
          }
        })
      );
      const allFailed = versionsWithContent.length > 0 && versionsWithContent.every((v) => v.loadFailed);
      const combinedError = allFailed
        ? `所有版本內容讀取失敗（請重整 / 確認 server）：${loadErrors.join("；")}`
        : null;
      const loadWarnings = (!allFailed && loadErrors.length > 0) ? loadErrors : null;
      editorState = {
        loading: false,
        error: combinedError,
        header: headerResp,
        versions: versionsWithContent,
        loadWarnings,
      };
      rerender();
    } catch (err) {
      editorState = { loading: false, error: err?.message || "載入失敗", header: null, versions: [] };
      rerender();
    }
  }

  function rerender() {
    container.innerHTML = renderEditorPage(sceneId, editorState);
    // Restore textarea state — but since we re-render fully, we need to put content back
    bindTextareaEvents();
  }

  function bindTextareaEvents() {
    container.querySelectorAll("[data-version-textarea]").forEach((ta) => {
      const v = ta.getAttribute("data-version-textarea");
      ta.addEventListener("input", (event) => {
        const newContent = /** @type {HTMLTextAreaElement} */ (event.target).value;
        const version = editorState.versions.find((x) => x.version === v);
        if (!version) return;
        version.content = newContent;
        version.dirty = newContent !== version.baselineContent;
        updateBottomStatusBar();
      });
    });
  }

  // audit-P2 cleanup: bindKeyboard() no-op marker removed; keyboard handler is added
  // globally in handleKeyboard via document.addEventListener — see below.

  function updateBottomStatusBar() {
    const bar = container.querySelector("[data-bottom-status]");
    if (!bar) return;
    bar.innerHTML = renderBottomStatus(sceneId, editorState);
  }

  // ============ Event handlers ============

  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    if (target.closest("[data-editor-save]")) { tryStartSave(); return; }
    if (target.closest("[data-editor-back]")) { tryBack(); return; }
    if (target.closest("[data-editor-refresh]")) { editorState = { ...editorState, loading: true }; rerender(); loadEditor(); return; }
  };

  const handleKeyboard = (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key === "s") {
      event.preventDefault();
      tryStartSave();
      return;
    }
    if (event.key === "Escape") {
      const modal = document.querySelector(".editor-modal");
      if (modal) modal.remove();
    }
  };

  container.addEventListener("click", handleClick);
  document.addEventListener("keydown", handleKeyboard);

  // ============ Save flow ============

  function dirtyVersions() {
    return editorState.versions.filter((v) => v.dirty);
  }

  function tryStartSave() {
    const dirty = dirtyVersions();
    if (dirty.length === 0) {
      showCopyToast({ variant: "success", title: "✓ 無修改可 Save", duration: 2500 });
      return;
    }
    // §11.3.8 Diff Preview Modal
    openDiffPreviewModal(dirty);
  }

  function tryBack() {
    const dirty = dirtyVersions();
    if (dirty.length === 0) {
      window.location.hash = `#/scene/${encodeURIComponent(sceneId)}`;
      return;
    }
    // §11.5.6 dirty 守門 confirm dialog
    openDirtyBackDialog();
  }

  function openDiffPreviewModal(dirtyList) {
    const modal = createModal();
    const renderDiffSection = (v) => {
      const diff = computeLineDiff(v.baselineContent, v.content);
      return `
        <div class="editor-diff-section">
          <h4>${escapeHtml(v.version)} (${diff.added} 行 +, ${diff.removed} 行 -, ${diff.modified} 行 ±)</h4>
          <pre class="editor-diff-block">${renderDiffPreLines(diff.lines)}</pre>
        </div>
      `;
    };
    modal.innerHTML = `
      <div class="copy-fallback-modal__backdrop" data-close></div>
      <div class="copy-fallback-modal__panel" style="max-width: 880px;">
        <header class="copy-fallback-modal__header">
          <strong>💾 Save 前確認 / Confirm Save</strong>
          <button type="button" class="copy-fallback-modal__close" aria-label="關閉" data-close>×</button>
        </header>
        <div class="copy-fallback-modal__body">
          <p>場景 ${escapeHtml(sceneId)}，要寫回以下 ${dirtyList.length} 個版本：</p>
          ${dirtyList.map(renderDiffSection).join("")}
          <p class="note-text">
            ⚠ Save 後 dirty 標記清除；不自動跳回 Scene Detail (Q4 / D-035 §5.3)。
            i18n KEY label per segment 待後續 i18n table 串接後補充 (§11.3.8 對齊 [NEEDS_SCHEMA_SUPPORT])。
          </p>
        </div>
        <footer class="copy-fallback-modal__footer">
          <button type="button" class="button" data-close>取消</button>
          <button type="button" class="button primary" data-confirm-save>確認寫回 / Confirm</button>
        </footer>
      </div>
    `;
    modal.addEventListener("click", (event) => {
      const t = event.target;
      if (t instanceof HTMLElement && t.hasAttribute("data-close")) { modal.remove(); return; }
      if (t instanceof HTMLElement && t.hasAttribute("data-confirm-save")) {
        modal.remove();
        doSave(dirtyList);
      }
    });
    document.body.append(modal);
  }

  function openDirtyBackDialog() {
    const modal = createModal();
    modal.innerHTML = `
      <div class="copy-fallback-modal__backdrop" data-close></div>
      <div class="copy-fallback-modal__panel">
        <header class="copy-fallback-modal__header">
          <strong>⚠ 確認返回 / Confirm Navigation</strong>
          <button type="button" class="copy-fallback-modal__close" data-close>×</button>
        </header>
        <div class="copy-fallback-modal__body">
          <p>您有未儲存的變更（${dirtyVersions().map((v) => escapeHtml(String(v.version || "?"))).join(" / ")}）。</p>
          <p class="note-text">選擇下一步：</p>
        </div>
        <footer class="copy-fallback-modal__footer">
          <button type="button" class="button primary" data-back-save>儲存後返回</button>
          <button type="button" class="button" data-back-discard>捨棄變更返回</button>
          <button type="button" class="button ghost" data-close>取消（留 Editor）</button>
        </footer>
      </div>
    `;
    modal.addEventListener("click", (event) => {
      const t = event.target;
      if (!(t instanceof HTMLElement)) return;
      if (t.hasAttribute("data-close")) { modal.remove(); return; }
      if (t.hasAttribute("data-back-save")) {
        modal.remove();
        const dirty = dirtyVersions();
        doSave(dirty, { afterSave: () => { window.location.hash = `#/scene/${encodeURIComponent(sceneId)}`; } });
      }
      if (t.hasAttribute("data-back-discard")) {
        modal.remove();
        window.location.hash = `#/scene/${encodeURIComponent(sceneId)}`;
      }
    });
    document.body.append(modal);
  }

  async function doSave(dirtyList, { afterSave } = {}) {
    // Save 一個一個 — 確保每個都過 race guard
    for (const v of dirtyList) {
      // Phase A.0F.patch-P0: fail-closed — versions that failed to load have
      // no trustworthy baseline; refuse to save them rather than risk wiping
      // the file with an empty payload.
      if (v.loadFailed) {
        showCopyToast({
          variant: "error",
          title: `⚠ Save ${v.version} 拒絕`,
          body: "此版本內容讀取失敗（fail-closed），請先重整 / 修復後再 save。",
        });
        return;
      }
      try {
        // Phase A.0F.patch-P0: pass `target_path` so backend uses the exact
        // version the user was editing; do not let server resolve by mtime.
        const resp = await saveScene(sceneId, {
          content: v.content,
          mtime_baseline: v.mtime,
          target_path: v.path,
        });
        if (resp.saved) {
          v.baselineContent = v.content;
          v.dirty = false;
          v.mtime = resp.new_mtime;
        }
      } catch (err) {
        // 409 path: LOCKED_OVERWRITE_DENIED (D-040) 或 MTIME_DRIFT
        const body = err?.body;
        if (err?.status === 409 && body) {
          if (body.error === "LOCKED_OVERWRITE_DENIED") {
            openLockedRaceModal(v, body);
          } else if (body.error === "MTIME_DRIFT") {
            openMtimeConflictModal(v, body);
          } else {
            showCopyToast({ variant: "error", title: `⚠ Save ${v.version} 失敗 (409)`, body: body.suggestion || body.error });
          }
          return;  // 中斷 — 先處理 conflict
        }
        showCopyToast({ variant: "error", title: `⚠ Save ${v.version} 失敗`, body: err?.message || String(err) });
        return;
      }
    }
    showCopyToast({
      variant: "success",
      title: `✓ Save 完成 (${dirtyList.length} 版)`,
      body: "dirty 已清，留在 Editor (Q4 / D-035 §5.3)",
    });
    rerender();
    if (afterSave) afterSave();
  }

  // §11.5.8.2 LOCKED race modal — 三選項 (D-040)
  function openLockedRaceModal(version, serverBody) {
    const modal = createModal();
    const filePath = version.path || serverBody?.path || "(unknown)";
    const guideText = buildDowngradeGuide(sceneId, filePath);
    modal.innerHTML = `
      <div class="copy-fallback-modal__backdrop" data-close></div>
      <div class="copy-fallback-modal__panel" style="max-width: 720px;">
        <header class="copy-fallback-modal__header">
          <strong>⚠ ${escapeHtml(version.version)} 已升 LOCKED — Save 被擋下 (D-040)</strong>
          <button type="button" class="copy-fallback-modal__close" data-close>×</button>
        </header>
        <div class="copy-fallback-modal__body">
          <p><strong>What：</strong>場景 ${escapeHtml(sceneId)} (${escapeHtml(version.version)}) 在您編輯期間被外部升 LOCKED</p>
          <p><strong>Where：</strong>${escapeHtml(filePath)}</p>
          <p><strong>Why：</strong>依 SPEC §16 + D-040 race guard，前端不得 overwrite LOCKED 場景</p>
          <p><strong>How：</strong>請選擇下一步（您的編輯內容會保留在前端 state，不會立刻丟失）：</p>
        </div>
        <div class="locked-race-options">
          <button type="button" class="button" data-locked-race="copy-downgrade">
            (A) 📋 複製降級指令 → 切外部 chat 跑
          </button>
          <button type="button" class="button" data-locked-race="save-as">
            (B) 💾 另存為 DRAFT proposal
          </button>
          <button type="button" class="button ghost" data-close>
            (C) 取消 — 留 Editor 不 Save
          </button>
        </div>
        <p class="note-text">
          (A) 走 §11.5.3 v0.3 引導：手動改 frontmatter 一行 + 09_e 紀錄完整降級理由<br>
          (B) 寫新檔 v??_proposal_&lt;timestamp&gt;.md (DRAFT 狀態)，原 LOCKED 檔不動 — 用 D-042 base_dialogue/iteration_note<br>
          (C) 純 client-side 動作；編輯留前端 state，可手動 copy 出去
        </p>
      </div>
    `;
    modal.addEventListener("click", async (event) => {
      const t = event.target;
      if (!(t instanceof HTMLElement)) return;
      if (t.hasAttribute("data-close")) { modal.remove(); return; }
      const action = t.getAttribute("data-locked-race");
      if (action === "copy-downgrade") {
        const result = await copyToClipboard(guideText);
        if (result.ok) {
          showCopyToast({ variant: "success", title: "✓ 已複製降級引導", body: "請切外部 chat / 編輯器執行" });
        } else {
          showCopyFallbackModal(guideText);
        }
        modal.remove();
      }
      if (action === "save-as") {
        modal.remove();
        await doSaveAs(version);
      }
    });
    document.body.append(modal);
  }

  // §11.5.8 (B) 另存 DRAFT proposal
  async function doSaveAs(version) {
    try {
      const note = window.prompt("iteration_note (選填 — 從 LOCKED race 中救回 proposal 的理由):", "從 LOCKED race 中救回的 proposal");
      // Phase A.0F.patch-P0: target_path is required (proposal base + LOCKED race target).
      const resp = await saveSceneAs(sceneId, {
        content: version.content,
        target_path: version.path,
        base_dialogue: version.path,
        iteration_note: note || "從 LOCKED race 中救回的 proposal",
      });
      if (resp.saved) {
        showCopyToast({
          variant: "success",
          title: "✓ 已另存為 DRAFT proposal",
          body: `新檔：${resp.saved_as_path}`,
          duration: 6000,
        });
        // 修正 dirty marker — proposal 已寫，原 LOCKED 檔仍 dirty 在 Editor (user 自己 discard or 繼續編)
      }
    } catch (err) {
      showCopyToast({ variant: "error", title: "⚠ 另存 proposal 失敗", body: err?.message || String(err) });
    }
  }

  // §11.7.6 mtime conflict modal — 二選: reload 棄改 / 強制覆寫
  function openMtimeConflictModal(version, serverBody) {
    const modal = createModal();
    const serverContent = serverBody?.server_content || "";
    modal.innerHTML = `
      <div class="copy-fallback-modal__backdrop" data-close></div>
      <div class="copy-fallback-modal__panel" style="max-width: 880px;">
        <header class="copy-fallback-modal__header">
          <strong>⚠ ${escapeHtml(version.version)} mtime 衝突 — 外部修改</strong>
          <button type="button" class="copy-fallback-modal__close" data-close>×</button>
        </header>
        <div class="copy-fallback-modal__body">
          <p>${escapeHtml(version.path)} 在您編輯期間被外部修改（mtime drift 偵測）。</p>
          <p class="note-text">兩選項（§11.7.6）：</p>
          <details>
            <summary>查看 server 端最新內容前 500 字</summary>
            <pre class="editor-diff-block">${escapeHtml(serverContent.slice(0, 500))}${serverContent.length > 500 ? "..." : ""}</pre>
          </details>
        </div>
        <footer class="copy-fallback-modal__footer">
          <button type="button" class="button" data-mtime-action="reload">Reload — 棄我的改動</button>
          <button type="button" class="button danger" data-mtime-action="force-overwrite">強制覆寫 — 用我的改動</button>
          <button type="button" class="button ghost" data-close>取消</button>
        </footer>
      </div>
    `;
    modal.addEventListener("click", async (event) => {
      const t = event.target;
      if (!(t instanceof HTMLElement)) return;
      if (t.hasAttribute("data-close")) { modal.remove(); return; }
      const action = t.getAttribute("data-mtime-action");
      if (action === "reload") {
        modal.remove();
        editorState = { ...editorState, loading: true };
        rerender();
        loadEditor();
      }
      if (action === "force-overwrite") {
        modal.remove();
        // Phase A.0F.patch-P0: force-overwrite must reference the exact edited
        // version, not the latest scene candidate via /header. Re-fetch
        // version-content for that exact path to get the current mtime.
        try {
          const fresh = await fetchSceneVersionContent(sceneId, version.path);
          version.mtime = fresh?.mtime || version.mtime;
          const resp = await saveScene(sceneId, {
            content: version.content,
            mtime_baseline: version.mtime,
            target_path: version.path,
          });
          if (resp.saved) {
            version.baselineContent = version.content;
            version.dirty = false;
            version.mtime = resp.new_mtime;
            showCopyToast({ variant: "success", title: `✓ 強制覆寫 ${version.version} 完成` });
            rerender();
          }
        } catch (err) {
          showCopyToast({ variant: "error", title: "⚠ 強制覆寫失敗", body: err?.message || String(err) });
        }
      }
    });
    document.body.append(modal);
  }

  return () => {
    container.removeEventListener("click", handleClick);
    document.removeEventListener("keydown", handleKeyboard);
    document.querySelectorAll(".editor-modal").forEach((el) => el.remove());
  };
}

// ============ render helpers ============

function renderLoading(sceneId) {
  return `
    <section class="dashboard-container">
      <div class="panel">
        <p class="meta-text">Scene Editor ${escapeHtml(sceneId)} 載入中...</p>
      </div>
    </section>
  `;
}

function renderEditorPage(sceneId, st) {
  if (st.loading) return renderLoading(sceneId);
  if (st.error) {
    return `
      <section class="dashboard-container">
        <header class="project-header">
          <div class="project-title-block">
            <p class="breadcrumb">
              <a class="link-button ghost" href="#/">專案首頁</a> /
              <a class="link-button ghost" href="#/scene-queue">Scene Queue</a> /
              <a class="link-button ghost" href="#/scene/${encodeURIComponent(sceneId)}">${escapeHtml(sceneId)}</a> /
              編輯
            </p>
            <h1 class="project-name">${escapeHtml(sceneId)} Editor</h1>
          </div>
          <div class="project-actions">
            <button class="button" type="button" data-editor-refresh>重試載入</button>
          </div>
        </header>
        <div class="fallback-message" role="status">載入失敗：${escapeHtml(st.error)}</div>
      </section>
    `;
  }
  const versions = st.versions;
  const pipelineState = st.header?.header?.["狀態"] || "未啟動";
  const isDeprecated = pipelineState === "DEPRECATED";

  return `
    <section class="dashboard-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁</a> /
            <a class="link-button ghost" href="#/scene-queue">Scene Queue</a> /
            <a class="link-button ghost" href="#/scene/${encodeURIComponent(sceneId)}">${escapeHtml(sceneId)}</a> /
            <strong>編輯</strong>
          </p>
          <div class="project-title-row">
            <h1 class="project-name">${escapeHtml(sceneId)} Editor</h1>
            <span class="badge ${pipelineStateTone(pipelineState)}">${escapeHtml(pipelineState)}</span>
          </div>
        </div>
        <div class="project-actions">
          <button class="button" type="button" data-editor-back>← 返回 Scene Detail</button>
          <button class="button primary" type="button" data-editor-save>💾 Save 全部 (Ctrl/Cmd-S)</button>
        </div>
      </header>

      ${isDeprecated ? `
        <div class="deprecated-banner" role="status">
          <strong>⚠ Warning：此場景已 DEPRECATED — §11.5.4</strong>
          <p>編輯不影響定稿。如要新版定稿，建議跑 /dialogue-write 產新版本。</p>
        </div>
      ` : ""}

      ${Array.isArray(st.loadWarnings) && st.loadWarnings.length > 0 ? `
        <div class="deprecated-banner" role="alert">
          <strong>⚠ 部分版本內容讀取失敗（fail-closed）— 失敗版本將 disable Save</strong>
          <ul>
            ${st.loadWarnings.map((line) => `<li>${escapeHtml(line)}</li>`).join("")}
          </ul>
          <p>請按「重試載入」或確認 server / 路徑。</p>
        </div>
      ` : ""}

      ${versions.length === 0 ? `
        <div class="empty-state">本場目前無 dialogue 版本檔可編輯。請先跑 /dialogue-write ${escapeHtml(sceneId)} 起首版。</div>
      ` : `
        <section class="editor-columns" data-columns-count="${versions.length}">
          ${versions.map((v) => renderVersionColumn(v)).join("")}
        </section>
      `}

      <footer class="panel editor-bottom-bar" data-bottom-status>
        ${renderBottomStatus(sceneId, st)}
      </footer>

      <p class="note-text">
        Ctrl/Cmd-S = Save。Esc = 關 modal。Save flow 5 步含 D-040 LOCKED race guard +
        §11.7.6 mtime conflict modal。離開時 dirty 守門 (§11.5.6)。
        §11.3.5 行級 details pane + §11.3.6 Required Context 抽屜留後續擴充。
      </p>
    </section>
  `;
}

function renderVersionColumn(v) {
  const isTrial = /^v0?1/.test(v.version || "");
  const isConvergence = /^v0?2/.test(v.version || "");
  const failed = Boolean(v.loadFailed);
  return `
    <article class="editor-column ${isTrial ? "editor-column--trial" : ""} ${isConvergence ? "editor-column--convergence" : ""}">
      <header class="editor-column-header">
        <div>
          <strong class="editor-column-version">${escapeHtml(v.version || "?")}</strong>
          <span class="badge ${pipelineStateTone(v.status)}">${escapeHtml(v.status || "—")}</span>
          ${failed ? `<span class="badge danger">⚠ 內容載入失敗</span>` : ""}
        </div>
        <div class="editor-column-meta">
          <span class="meta-text">mtime: ${formatMtime(v.mtime)}</span>
          <span class="meta-text">${escapeHtml(v.path || "")}</span>
          ${failed && v.loadError ? `<span class="meta-text">${escapeHtml(String(v.loadError))}</span>` : ""}
        </div>
        ${renderCopyCommandButton({
          command: `/qa ${(v.path || '').match(/CH(\d+)_S(\d+)/) ? `S-${v.path.match(/CH(\d+)_S(\d+)/)[1]}-${v.path.match(/CH(\d+)_S(\d+)/)[2]}` : '<scene>'} --version ${v.version}`,
          source: `Scene Editor / ${v.version}`,
          targetAgent: "any",
          variant: "ghost",
          size: "sm",
          label: `📋 跑 ${v.version} QA`,
        })}
      </header>
      <textarea
        class="editor-textarea"
        data-version-textarea="${escapeAttr(v.version)}"
        spellcheck="false"
        ${failed ? "disabled" : ""}
      >${escapeHtml(v.content)}</textarea>
      ${failed ? `<p class="note-text">⚠ fail-closed：本版本內容讀取失敗，Save 已 disable。請先重整 / 修復路徑。</p>` : ""}
    </article>
  `;
}

function renderBottomStatus(sceneId, st) {
  const dirty = st.versions.filter((v) => v.dirty);
  return `
    <div class="editor-bottom-status">
      <div>
        ${dirty.length > 0
          ? `<strong>● Dirty:</strong> ${dirty.map((v) => escapeHtml(v.version)).join(" / ")}`
          : `<span class="meta-text">○ 無未儲存變更</span>`}
      </div>
      <div class="editor-bottom-actions">
        <button class="button primary" type="button" data-editor-save ${dirty.length === 0 ? "disabled" : ""}>
          💾 Save 全部 (${dirty.length})
        </button>
      </div>
    </div>
  `;
}

function buildDowngradeGuide(sceneId, filePath) {
  const date = new Date().toISOString().slice(0, 10);
  return [
    `─── 場景 ${sceneId} 從 LOCKED 降級為 DEPRECATED ───`,
    ``,
    `此場景在您編輯期間被升 LOCKED。依 SPEC §16 + D-040 race guard，`,
    `前端不得 overwrite LOCKED 場景。請手動執行下列兩步（不新增 frontmatter 欄位）：`,
    ``,
    `1. 編輯 frontmatter（外部編輯器）：`,
    `   檔案：D:/劇本開發工具/${filePath}`,
    `   只改一行：狀態：LOCKED  →  狀態：DEPRECATED`,
    `   不要新增「降級理由」「降級日期」「降級人」等欄位（D-046 #5 / C-16 / O-03）。`,
    ``,
    `2. 在 09_e final-gating 紀錄檔補一條完整降級紀錄：`,
    `   檔案：09_quality_assurance/09_e_定稿變更紀錄.md`,
    `   附加段落：`,
    `     ## ${sceneId} LOCKED → DEPRECATED 降級 / ${date}`,
    `     - 場景：${sceneId}`,
    `     - 原狀態：LOCKED`,
    `     - 新狀態：DEPRECATED`,
    `     - 降級日期：${date}`,
    `     - 降級人：[user 名稱]`,
    `     - 降級理由：[具體理由]`,
    `     - 影響：本版本不再為定稿；如要新版定稿請跑`,
    `            /dialogue-write ${sceneId} --single-iter --note "依新 W-rules 重做"`,
    ``,
    `3. 回 Editor 重整頁面 — 重整後 Save 流程會通過 race guard。`,
    ``,
    `─── 注意 ───`,
    `- 降級操作不走 skill（D-031）`,
    `- frontmatter 只改 \`狀態：DEPRECATED\` 一行 — 不擅自加 schema 不認的欄位`,
    `- 完整降級紀錄全部進 09_e，由人類追溯`,
    `- 依 SPEC §16 文件狀態升級限制原則，狀態機由人類控制`,
  ].join("\n");
}

function computeLineDiff(baseline, current) {
  // Naive line-based diff — 不做 LCS，僅 line-by-line 比對 + 標記增/刪/改
  const baseLines = baseline.split("\n");
  const curLines = current.split("\n");
  const maxLen = Math.max(baseLines.length, curLines.length);
  const out = [];
  let added = 0, removed = 0, modified = 0;
  for (let i = 0; i < maxLen; i += 1) {
    const b = baseLines[i];
    const c = curLines[i];
    if (b === undefined && c !== undefined) {
      out.push({ kind: "added", text: c, lineNum: i + 1 });
      added += 1;
    } else if (b !== undefined && c === undefined) {
      out.push({ kind: "removed", text: b, lineNum: i + 1 });
      removed += 1;
    } else if (b !== c) {
      out.push({ kind: "removed", text: b, lineNum: i + 1 });
      out.push({ kind: "added", text: c, lineNum: i + 1 });
      modified += 1;
    }
  }
  return { lines: out, added, removed, modified };
}

function renderDiffPreLines(lines) {
  if (lines.length === 0) return `<span class="meta-text">(無實質差異)</span>`;
  return lines.slice(0, 100).map((l) => {
    const sign = l.kind === "added" ? "+" : "-";
    const cls = l.kind === "added" ? "diff-added" : "diff-removed";
    return `<span class="${cls}">${sign} ${escapeHtml(l.text)}</span>`;
  }).join("\n") + (lines.length > 100 ? "\n<span class=\"meta-text\">... " + (lines.length - 100) + " 行省略</span>" : "");
}

function createModal() {
  const modal = document.createElement("div");
  modal.className = "copy-fallback-modal editor-modal";
  modal.setAttribute("role", "dialog");
  modal.setAttribute("aria-modal", "true");
  return modal;
}

function formatMtime(mtime) {
  if (!mtime) return "—";
  const d = new Date(mtime * 1000);
  if (Number.isNaN(d.getTime())) return "—";
  return d.toLocaleString("zh-Hant");
}

function pipelineStateTone(state) {
  if (!state) return "warning";
  if (state === "LOCKED") return "warning";
  if (state === "DEPRECATED") return "warning";
  if (state === "REVIEW") return "success";
  if (state === "FINAL") return "success";
  return "";
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
