/**
 * Scene Detail page — F2 下半 cockpit, read-only（UX_SPEC §11.2.2）
 *
 * Layout：main + side 雙欄
 *   Main:
 *     §11.2.3 Scene Readiness Panel  (badge + checklist + Next Fix)
 *     §11.2.4 Required Context (6 子分區，本輪 placeholder)
 *     §11.2.7 Beat / Outline Preview (read-only，本輪 placeholder)
 *     §11.2.9 Dialogue Draft Preview (tab 切版本，read-only)
 *     §11.2.10 QA Findings 摘要 + click 展 modal (本輪 placeholder)
 *   Side (sticky):
 *     §11.2.5 Active QA findings 摘要
 *     §11.2.6 Active HD / Canon Δ
 *     §11.2.8 Quick Actions（含「進入編輯」按鈕 + 多個複製指令）
 *
 * 對齊：
 *   - D-035 read-only cockpit；編輯走「進入編輯」跳 §11.3
 *   - §11.5 LOCKED 守門：DRAFT/REVIEW 直接跳 Editor；LOCKED 改顯示降級引導；
 *     DEPRECATED 跳 Editor 加 banner
 *   - §11.6 通用 CopyCommandButton（renderCopyCommandButton import）
 *   - §11.0.4 G1 / G2 / G3 守則
 *
 * Phase A.0F.6 (Editor) + A.0F.7 (LOCKED race guard) 後本頁的「進入編輯」按鈕
 * 才完整 wire；本輪先骨架 + 跳轉 #/scene/<id>/edit placeholder。
 *
 * Phase A.0F 階段 Required Context 6 子分區 / Beat preview / QA findings full modal
 * 部分屬 [BLOCKED:UPSTREAM_DOWNSTREAM]（需要 backend 提供反查 API），
 * 本輪先以 [NEEDS_SCHEMA_SUPPORT] placeholder 文案標示。
 */

import { sceneDetailData$ } from "../state.js";
import {
  renderCopyCommandButton,
  copyToClipboard,
  showCopyToast,
  showCopyFallbackModal,
} from "../components/CopyCommandButton.js";

/**
 * @param {HTMLElement} container
 * @param {{sceneId: string, loadSceneDetail: (id: string, opts?: {force?:boolean}) => Promise<any>}} ctx
 * @returns {() => void}
 */
export function renderSceneDetail(container, { sceneId, loadSceneDetail }) {
  const handleClick = (event) => {
    const target = /** @type {HTMLElement} */ (event.target);
    const refresh = target.closest("[data-scene-detail-refresh]");
    if (refresh) {
      document.dispatchEvent(new CustomEvent("scene-detail:refresh", { detail: { sceneId } }));
    }
  };
  container.addEventListener("click", handleClick);

  const unsubscribe = sceneDetailData$.subscribe((data) => {
    if (data.sceneId !== sceneId && !data.loading) {
      // Detail signal 已被別頁切走，避免渲染錯誤資料
      return;
    }
    container.className = "app-shell scene-detail-shell";
    container.innerHTML = renderDetailPage(data, sceneId);
  });

  return () => {
    container.removeEventListener("click", handleClick);
    unsubscribe();
  };
}

function renderDetailPage(data, sceneId) {
  const loading = data.loading;
  const error = data.error;
  const header = data.header;
  const versions = data.versions;
  const summary = data.summary;
  const pipelineState = header?.header?.["狀態"] || summary?.pipeline_state || "未啟動";

  return `
    <section class="dashboard-container scene-detail-container">
      <header class="project-header">
        <div class="project-title-block">
          <p class="breadcrumb">
            <a class="link-button ghost" href="#/">專案首頁</a> /
            <a class="link-button ghost" href="#/scene-queue">Scene Queue</a> /
            ${escapeHtml(sceneId)}
          </p>
          <div class="project-title-row">
            <h1 class="project-name">${escapeHtml(sceneId)}</h1>
            <span class="badge ${pipelineStateTone(pipelineState)}">${escapeHtml(pipelineState)}</span>
          </div>
          <p class="meta-text">最後 refresh：${escapeHtml(formatDateTime(data.refreshedAt))}</p>
        </div>
        <div class="project-actions" aria-label="Scene Detail controls">
          <a class="link-button" href="#/scene-queue">← Scene Queue</a>
          <button class="button" type="button" data-scene-detail-refresh ${loading ? "disabled" : ""}>手動 refresh</button>
        </div>
      </header>

      ${error ? `<div class="fallback-message" role="status">${escapeHtml(error)}</div>` : ""}

      <div class="scene-detail-grid">
        <div class="scene-detail-main">
          ${renderReadinessPanel(summary, pipelineState)}
          ${renderRequiredContextPlaceholder(sceneId)}
          ${renderBeatPlaceholder(sceneId)}
          ${renderDialoguePreview(versions, summary, sceneId)}
          ${renderQaFindingsPlaceholder(summary, sceneId)}
        </div>
        <aside class="scene-detail-side">
          ${renderActiveQaSide(summary, sceneId)}
          ${renderActiveHdSide()}
          ${renderQuickActions(sceneId, pipelineState, header)}
        </aside>
      </div>
    </section>
  `;
}

function renderReadinessPanel(summary, pipelineState) {
  if (!summary) {
    return `
      <section class="panel">
        <div class="panel-title">
          <p class="eyebrow">Scene Readiness Panel — §11.2.3</p>
          <h2>場景就緒度</h2>
        </div>
        <div class="empty-state">場景列表載入中或本場不存在於 /api/scenes。</div>
      </section>
    `;
  }
  const dialogueDone = (summary.dialogue_count || 0) > 0;
  const taskDone = Boolean(summary.task_path);
  const qaDone = (summary.qa_report_count || 0) > 0;
  const checklist = [
    { label: "任務包已建立 / Task package present", ok: taskDone },
    { label: "Dialogue version 存在 / Dialogue versions exist", ok: dialogueDone },
    { label: "至少跑過一輪 QA / At least one QA report", ok: qaDone },
    { label: "Pipeline state 升至 REVIEW / Promoted to REVIEW", ok: pipelineState === "REVIEW" || pipelineState === "FINAL" },
    { label: "Pipeline state 升至 FINAL / Promoted to FINAL", ok: pipelineState === "FINAL" },
  ];
  const doneCount = checklist.filter((i) => i.ok).length;

  return `
    <section class="panel">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Scene Readiness Panel — §11.2.3</p>
          <h2>場景就緒度</h2>
        </div>
        <span class="badge ${doneCount >= 4 ? "success" : "warning"}">${doneCount}/${checklist.length}</span>
      </div>
      <ul class="readiness-checklist">
        ${checklist.map((item) => `
          <li>
            <span class="check-icon" aria-hidden="true">${item.ok ? "✓" : "✗"}</span>
            <span>${escapeHtml(item.label)}</span>
          </li>
        `).join("")}
      </ul>
      <p class="note-text">
        * 此 checklist 為前端簡易推導；正式 readiness 規則（含 Required Context 6 子分區 / 角色聲線 / 立繪 KEY 等 10 項）
        屬 [BLOCKED:UPSTREAM_DOWNSTREAM]，由上下游 specialist 第二輪設計後本頁同步擴充。
      </p>
    </section>
  `;
}

function renderRequiredContextPlaceholder(sceneId) {
  return `
    <section class="panel">
      <div class="panel-title">
        <p class="eyebrow">Required Context — §11.2.4</p>
        <h2>必要 Context (6 子分區)</h2>
      </div>
      <ol class="required-context-list">
        <li><strong>Bible 引用</strong>：W-rules / V-vocab — [NEEDS_SCHEMA_SUPPORT] 反查 API</li>
        <li><strong>出場角色</strong>：C-* 聲線卡 + A-* 立繪 KEY — 待 backend 反查 API</li>
        <li><strong>角色關係</strong>：R-*-* 動態 + 過去史 — 待反查</li>
        <li><strong>世界詞彙 / 禁用詞</strong>：本場可用 / 禁用 / 慎用 — 待 markdown 標記方式對齊</li>
        <li><strong>資訊揭露控制</strong>：本場應揭露 / 必須保密 — 待 P (Premise) 反查</li>
        <li><strong>跨場警示</strong>：聲線漂移 / 資訊洩漏 — 待跨場一致性 query</li>
      </ol>
      <p class="note-text">
        * 6 子分區的詳細內容反查屬 [BLOCKED:UPSTREAM_DOWNSTREAM]，需要 backend
        提供 entity manifest + cross-ref query API（UX §11.0.7）。本輪先骨架，
        Phase A.0F 後續或 Phase D Wave 13 /view-* 整合時補。
      </p>
    </section>
  `;
}

function renderBeatPlaceholder(sceneId) {
  return `
    <section class="panel">
      <div class="panel-title">
        <p class="eyebrow">Beat / Outline Preview — §11.2.7</p>
        <h2>Beat 結構</h2>
      </div>
      <p class="note-text">
        Beat 結構（建議分 N 拍）— 對齊細綱 06_detailed_outline/* read-only 渲染。
        Phase A.0F 後續會補 markdown 渲染 + scene anchor 反查；本輪僅骨架。
        G3 守則：Beat 是「建議」，不是「本場必有 N beat」。
      </p>
    </section>
  `;
}

function renderDialoguePreview(versions, summary, sceneId) {
  const versionList = versions?.versions || summary?.dialogue_versions || [];
  if (versionList.length === 0) {
    return `
      <section class="panel">
        <div class="panel-title">
          <p class="eyebrow">Dialogue Draft Preview — §11.2.9</p>
          <h2>台詞稿預覽 (read-only)</h2>
        </div>
        <div class="empty-state">本場尚無 dialogue 版本檔。可考慮跑 /dialogue-write ${escapeHtml(sceneId)} 起首版。</div>
        <div class="card-actions">
          ${renderCopyCommandButton({
            command: `/dialogue-write ${sceneId}`,
            source: `Scene Detail ${sceneId}`,
            targetAgent: "any",
            variant: "primary",
            size: "md",
          })}
        </div>
      </section>
    `;
  }
  return `
    <section class="panel">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">Dialogue Draft Preview — §11.2.9 (read-only)</p>
          <h2>台詞稿預覽</h2>
        </div>
        <span class="chip">${versionList.length} 版本</span>
      </div>
      <ul class="dialogue-version-list">
        ${versionList.map((v) => `
          <li>
            <strong>${escapeHtml(v.version || "?")}</strong>
            <span class="meta-text">${escapeHtml(v.path || "")}</span>
            <span class="badge ${pipelineStateTone(v.status)}">${escapeHtml(v.status || "—")}</span>
          </li>
        `).join("")}
      </ul>
      <p class="note-text">
        * 行級 read-only preview（dlg.&lt;ch&gt;.&lt;s&gt;.&lt;line&gt; tag）屬 §11.2.9 完整版；
        本輪先列版本檔，行級渲染待 Phase A.0F.6 Editor 上線後一併實作。
        編輯走 §11.3 Scene Editor，不在本頁。
      </p>
    </section>
  `;
}

function renderQaFindingsPlaceholder(summary, sceneId) {
  const count = summary?.qa_report_count || 0;
  return `
    <section class="panel">
      <div class="panel-header">
        <div class="panel-title">
          <p class="eyebrow">QA Findings 摘要 — §11.2.10</p>
          <h2>QA findings</h2>
        </div>
        <span class="badge ${count > 0 ? "success" : "warning"}">${count} 份報告</span>
      </div>
      ${count === 0 ? `
        <div class="empty-state">本場目前無 QA 報告。可考慮跑 /qa ${escapeHtml(sceneId)} 啟首輪檢查。</div>
        <div class="card-actions">
          ${renderCopyCommandButton({
            command: `/qa ${sceneId}`,
            source: `Scene Detail ${sceneId}`,
            targetAgent: "any",
            variant: "primary",
            size: "md",
          })}
        </div>
      ` : `
        <p class="note-text">
          QA findings 完整 modal（含 5 欄位 severity / title / affected / summary / suggested actions）
          屬 §11.2.10 完整版，需要 backend 反查 09_quality_assurance/ 內具體 finding 結構。
          本輪先顯示報告數，完整 modal 待後續實作。
        </p>
      `}
    </section>
  `;
}

function renderActiveQaSide(summary, sceneId) {
  return `
    <section class="panel scene-side-panel">
      <div class="panel-title">
        <p class="eyebrow">Active QA — §11.2.5</p>
        <h3>QA findings 側欄</h3>
      </div>
      <p class="note-text">
        側欄摘要待 backend 提供 09_quality_assurance/ finding parser。
        當前場景報告數：${escapeHtml(String(summary?.qa_report_count || 0))} 份。
      </p>
      ${renderCopyCommandButton({
        command: `/qa ${sceneId}`,
        source: `Scene Detail ${sceneId} / Side`,
        targetAgent: "any",
        variant: "secondary",
        size: "sm",
      })}
    </section>
  `;
}

function renderActiveHdSide() {
  return `
    <section class="panel scene-side-panel">
      <div class="panel-title">
        <p class="eyebrow">Active HD / Canon Δ — §11.2.6</p>
        <h3>待裁決 / Canon Delta</h3>
      </div>
      <p class="note-text">
        HD pending + Canon Δ pending 列表待 backend 提供。
        modal 內走「複製拍板紀錄到 09_e」按鈕（依 D-029 α，不直接執行）。
      </p>
    </section>
  `;
}

function renderQuickActions(sceneId, pipelineState, header) {
  const isLocked = pipelineState === "LOCKED";
  const isDeprecated = pipelineState === "DEPRECATED";
  const isUnstarted = pipelineState === "未啟動";
  const filePath = header?.path || "";

  return `
    <section class="panel scene-side-panel scene-quick-actions">
      <div class="panel-title">
        <p class="eyebrow">Quick Actions — §11.2.8</p>
        <h3>進入編輯 / 複製指令</h3>
      </div>
      ${isLocked ? renderLockedGate(sceneId, filePath) : ""}
      ${isDeprecated ? renderDeprecatedBanner() : ""}
      ${isUnstarted ? `
        <p class="note-text">本場尚未啟動 dialogue。先跑 /dialogue-write 試寫首版。</p>
        ${renderCopyCommandButton({
          command: `/dialogue-write ${sceneId}`,
          source: `Scene Detail ${sceneId} / Quick Actions`,
          targetAgent: "any",
          variant: "primary",
          size: "md",
        })}
      ` : ""}
      ${!isLocked && !isUnstarted ? `
        <a class="link-button primary" href="#/scene/${encodeURIComponent(sceneId)}/edit">
          → 進入編輯 / Enter Editor
        </a>
      ` : ""}
      <div class="quick-action-grid">
        ${renderCopyCommandButton({
          command: `/qa ${sceneId}`,
          source: `Scene Detail ${sceneId} / Quick Actions`,
          targetAgent: "any",
          variant: "secondary",
          size: "sm",
        })}
        ${renderCopyCommandButton({
          command: `/dialogue-write ${sceneId} --single-iter`,
          source: `Scene Detail ${sceneId} / Quick Actions`,
          targetAgent: "any",
          variant: "secondary",
          size: "sm",
        })}
        <a class="link-button" href="#/export">📤 開啟 L3 Export panel (scene scope)</a>
      </div>
    </section>
  `;
}

function renderLockedGate(sceneId, filePath) {
  // §11.5.2 + §11.5.3 v0.3 LOCKED 降級引導文字
  const guideText = [
    `─── 場景 ${sceneId} 從 LOCKED 降級為 DEPRECATED ───`,
    ``,
    `此場景目前 pipeline_state 為 LOCKED，依 SPEC §16 文件狀態機規則不可直接編輯。`,
    `請手動執行下列兩步（不新增 frontmatter 欄位）：`,
    ``,
    `1. 編輯 frontmatter（外部編輯器，如 VS Code）：`,
    `   檔案：${filePath || "(請從 Scene Detail header 抓 path)"}`,
    `   只改一行：狀態：LOCKED  →  狀態：DEPRECATED`,
    `   不要新增「降級理由」「降級日期」「降級人」等欄位 —`,
    `   這些欄位不在 SPEC §5.2 canonical schema 內，請放到下一步的 09_e。`,
    ``,
    `2. 在 09_e final-gating 紀錄檔補一條完整降級紀錄：`,
    `   檔案：09_quality_assurance/09_e_定稿變更紀錄.md`,
    `   附加段落：`,
    `     ## ${sceneId} LOCKED → DEPRECATED 降級 / [今天日期]`,
    `     - 場景：${sceneId}`,
    `     - 原狀態：LOCKED`,
    `     - 新狀態：DEPRECATED`,
    `     - 降級日期：[YYYY-MM-DD]`,
    `     - 降級人：[user 名稱]`,
    `     - 降級理由：[具體理由]`,
    `     - 影響：v02 不再為定稿；如要新版定稿請跑`,
    `            /dialogue-write ${sceneId} --single-iter --note "依新 W-rules 重做"`,
    ``,
    `3. 回到 Scene Detail 重整頁面。重整後「進入編輯」按鈕應啟用。`,
    ``,
    `─── 注意 ───`,
    `- 降級操作不走 skill（D-031）`,
    `- frontmatter 只改 \`狀態：DEPRECATED\` 一行 — 不擅自加 schema 不認的欄位`,
    `- 完整降級紀錄（理由、日期、操作人、影響）全部進 09_e，由人類追溯`,
    `- 依 SPEC §16 文件狀態升級限制原則，狀態機由人類控制`,
  ].join("\n");

  return `
    <div class="locked-gate" role="alert">
      <strong>⚠ 此場景已 LOCKED — §11.5</strong>
      <p>
        <strong>What：</strong>此場景 pipeline_state 為 LOCKED<br>
        <strong>Where：</strong>${escapeHtml(filePath || "(待 header API 提供 path)")}<br>
        <strong>Why：</strong>依 SPEC §16 文件狀態機規則，LOCKED 場景的台詞不可直接編輯，必須先降級為 DEPRECATED 並紀錄理由<br>
        <strong>How to fix（降級流程，3 步）：</strong>
      </p>
      <ol class="locked-steps">
        <li>點下方「複製降級引導文字」按鈕</li>
        <li>切到外部編輯器手動改 frontmatter 狀態欄位</li>
        <li>在 09_e 紀錄降級理由後重整本頁</li>
      </ol>
      ${/* Phase A.0F.patch-concern-2 / §11.6.7: LOCKED downgrade guide is
            * pure guide/raw text, NOT a command payload. Previously this used
            * renderCopyCommandButton which wraps the text with
            * COPY_MARKER_OPEN/CLOSE + "指令：/Context/來源" header. CODEX
            * Concern §1 §11.6 / §8 #7. We now emit a raw-mode button that
            * fires a dedicated click handler in main.js (data-locked-guide).
            */ ""}
      <button
        type="button"
        class="copy-command-button copy-command-button--primary copy-command-button--md"
        data-locked-guide-button="true"
        data-locked-guide-text="${escapeAttr(guideText)}"
      >📋 複製降級引導文字 / Copy downgrade guide</button>
      <p class="note-text">
        替代動作：本頁本身就是 read-only 預覽；也可跳轉 09_e 定稿變更紀錄查歷史。
        Phase A.0F.7 LOCKED race guard 完整版會在 Editor Save flow 內再做一層 Step 3 pre-flight 檢查。
      </p>
    </div>
  `;
}

function renderDeprecatedBanner() {
  return `
    <div class="deprecated-banner" role="status">
      <strong>~ 此場景已 DEPRECATED — §11.5.4</strong>
      <p>編輯不影響定稿。如要新版定稿，可跑 /dialogue-write &lt;id&gt; 產新版本。</p>
    </div>
  `;
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

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttrSafe(value) {
  return String(value).replace(/[^\w-]/g, "_");
}

// Phase A.0F.patch-concern-2: escape values for use inside double-quoted HTML
// attributes (e.g. data-locked-guide-text="..."). Mirrors the helper used in
// SceneEditor.js / SceneQueue.js for consistency.
function escapeAttr(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}
