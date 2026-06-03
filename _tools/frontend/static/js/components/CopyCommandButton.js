/**
 * CopyCommandButton — 通用「複製指令」按鈕元件
 *
 * 對應 UX_SPEC §11.6（master 鎖定的單一通用元件）。
 *
 * 設計守則：
 *   - D-029 (α) 完全分離：前端**不**執行 agent；按鈕只把組好的 prompt 寫到剪貼簿
 *   - §11.6.3 剪貼簿格式：開頭/結尾 `─── [前端工具產生] ───` 分隔線 + 指令 + Context 摘要 + 相關檔案引用 + 來源
 *   - §11.6.4 視覺三 variant：primary / secondary / ghost；emoji 📋 強制
 *   - §11.6.5 toast 反饋：✓ 已複製到剪貼簿，自動 5s 消失；失敗 → fallback modal 顯示文字框
 *
 * 用法（兩種模式）：
 *
 *   1) 純 DOM string 模式（適用 innerHTML 大區塊渲染）：
 *      container.innerHTML = renderCopyCommandButton({
 *        command: "/dialogue-write S-01-03",
 *        contextSummary: "...",
 *        contextRefs: ["/03_characters/main/主角A_聲線卡.md"],
 *        source: "Scene Detail S-01-03",
 *        variant: "primary",
 *      });
 *
 *      然後在 app 啟動時呼叫一次 `installCopyCommandDelegate(document)` 註冊 delegated click handler。
 *
 *   2) 直接呼叫模式（適用程式化）：
 *      const text = assembleCopyPayload({ command: "/qa S-01-03" });
 *      const result = await copyToClipboard(text);
 *      if (result.ok) showCopyToast({ variant: "success", title: "✓ 已複製到剪貼簿" });
 *      else showCopyFallbackModal(text);
 */

export const COPY_MARKER_OPEN = "─── [前端工具產生] ───";
export const COPY_MARKER_CLOSE = "─── /[前端工具產生] ───";

/**
 * 組裝剪貼簿 payload — pure function，方便 unit test。
 *
 * @param {Object} opts
 * @param {string} opts.command  主指令（必填，如 "/dialogue-write S-01-03"）
 * @param {string} [opts.contextSummary]  Context 摘要（可選）
 * @param {string[]} [opts.contextRefs]  跨檔 ref list（可選）
 * @param {string} [opts.contextNotes]  自由文字註解（可選）
 * @param {string} [opts.source]  來源描述（如 "Scene Detail S-01-03"）
 * @param {Date|string} [opts.timestamp]  時間戳；預設 new Date()
 * @returns {string}  完整剪貼簿文字
 */
export function assembleCopyPayload({
  command,
  contextSummary,
  contextRefs,
  contextNotes,
  source,
  timestamp,
} = {}) {
  if (typeof command !== "string" || !command.trim()) {
    throw new Error("assembleCopyPayload: command is required and must be a non-empty string");
  }

  const lines = [COPY_MARKER_OPEN, "指令：", `  ${command.trim()}`];

  if (typeof contextSummary === "string" && contextSummary.trim()) {
    lines.push("", "已有 Context 摘要：");
    contextSummary.trim().split(/\r?\n/).forEach((raw) => {
      const trimmed = raw.trim();
      if (!trimmed) return;
      lines.push(trimmed.startsWith("-") || trimmed.startsWith("•") ? trimmed : `- ${trimmed}`);
    });
  }

  if (Array.isArray(contextRefs) && contextRefs.length > 0) {
    lines.push("", "相關檔案引用：");
    contextRefs.forEach((ref) => {
      if (typeof ref === "string" && ref.trim()) {
        lines.push(`- ${ref.trim()}`);
      }
    });
  }

  if (typeof contextNotes === "string" && contextNotes.trim()) {
    lines.push("", "備註：", contextNotes.trim());
  }

  lines.push("", "來源：");
  const ts = formatTimestamp(timestamp);
  lines.push(`  前端工具 / ${(source && source.trim()) || "未指定來源"} / ${ts}`);
  lines.push(COPY_MARKER_CLOSE);
  return lines.join("\n");
}

/**
 * 寫入剪貼簿。優先用 navigator.clipboard.writeText；失敗時 fallback 到 execCommand。
 *
 * @param {string} text
 * @returns {Promise<{ok: true} | {ok: false, error: Error}>}
 */
export async function copyToClipboard(text) {
  if (typeof text !== "string") {
    return { ok: false, error: new Error("copyToClipboard: text must be a string") };
  }

  if (typeof navigator !== "undefined" && navigator.clipboard?.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      return { ok: true };
    } catch (err) {
      // fall through to legacy fallback
      const legacyResult = legacyCopy(text);
      if (legacyResult.ok) return legacyResult;
      return { ok: false, error: err instanceof Error ? err : new Error(String(err)) };
    }
  }
  return legacyCopy(text);
}

function legacyCopy(text) {
  if (typeof document === "undefined") {
    return { ok: false, error: new Error("document is not available") };
  }
  try {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.setAttribute("readonly", "");
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";
    textArea.style.top = "-1000px";
    document.body.append(textArea);
    textArea.select();
    const success = document.execCommand("copy");
    textArea.remove();
    if (success) return { ok: true };
    return { ok: false, error: new Error("document.execCommand('copy') returned false") };
  } catch (err) {
    return { ok: false, error: err instanceof Error ? err : new Error(String(err)) };
  }
}

/**
 * 顯示 toast。
 *
 * @param {Object} [opts]
 * @param {"success"|"error"} [opts.variant]
 * @param {string} [opts.title]
 * @param {string} [opts.body]
 * @param {number} [opts.duration]  ms；0 表不自動消失
 */
export function showCopyToast({
  variant = "success",
  title = "",
  body = "",
  duration = 5000,
} = {}) {
  if (typeof document === "undefined") return null;
  document.querySelectorAll(".copy-toast").forEach((el) => el.remove());

  const toast = document.createElement("div");
  toast.className = `copy-toast copy-toast--${variant}`;
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");

  const icon = variant === "success" ? "✓" : "⚠";
  const safeTitle = escapeHtml(title);
  const safeBody = body ? `<p class="copy-toast__text">${escapeHtml(body)}</p>` : "";

  toast.innerHTML = `
    <div class="copy-toast__icon" aria-hidden="true">${icon}</div>
    <div class="copy-toast__body">
      ${safeTitle ? `<strong class="copy-toast__title">${safeTitle}</strong>` : ""}
      ${safeBody}
    </div>
    <button type="button" class="copy-toast__close" aria-label="關閉">×</button>
  `;

  toast.querySelector(".copy-toast__close")?.addEventListener("click", () => toast.remove());
  document.body.append(toast);

  if (duration > 0) {
    window.setTimeout(() => toast.classList.add("copy-toast--leaving"), Math.max(0, duration - 300));
    window.setTimeout(() => toast.remove(), duration);
  }

  return toast;
}

/**
 * 剪貼簿失敗時的 fallback modal — 顯示文字框讓 user 手動全選複製。
 *
 * @param {string} text
 */
export function showCopyFallbackModal(text) {
  if (typeof document === "undefined") return null;
  document.querySelectorAll(".copy-fallback-modal").forEach((el) => el.remove());

  const modal = document.createElement("div");
  modal.className = "copy-fallback-modal";
  modal.setAttribute("role", "dialog");
  modal.setAttribute("aria-modal", "true");
  modal.setAttribute("aria-labelledby", "copy-fallback-title");
  modal.innerHTML = `
    <div class="copy-fallback-modal__backdrop" data-close></div>
    <div class="copy-fallback-modal__panel" role="document">
      <header class="copy-fallback-modal__header">
        <strong id="copy-fallback-title">⚠ 複製失敗 / Copy failed</strong>
        <button type="button" class="copy-fallback-modal__close" aria-label="關閉" data-close>×</button>
      </header>
      <div class="copy-fallback-modal__body">
        <p>瀏覽器不允許自動複製。請手動全選下方文字 (Ctrl/Cmd+A) 後複製 (Ctrl/Cmd+C)：</p>
        <textarea class="copy-fallback-modal__textarea" readonly aria-label="待複製內容"></textarea>
      </div>
      <footer class="copy-fallback-modal__footer">
        <button type="button" class="button" data-close>關閉</button>
      </footer>
    </div>
  `;

  const textarea = modal.querySelector(".copy-fallback-modal__textarea");
  if (textarea instanceof HTMLTextAreaElement) {
    textarea.value = text;
  }

  modal.addEventListener("click", (event) => {
    const target = event.target;
    if (target instanceof HTMLElement && target.hasAttribute("data-close")) {
      modal.remove();
    }
  });

  document.body.append(modal);

  if (textarea instanceof HTMLTextAreaElement) {
    // 自動聚焦 + 全選方便 Ctrl/Cmd+C
    window.setTimeout(() => {
      textarea.focus();
      textarea.select();
    }, 0);
  }

  return modal;
}

const VARIANT_CLASS = {
  primary: "copy-command-button copy-command-button--primary",
  secondary: "copy-command-button copy-command-button--secondary",
  ghost: "copy-command-button copy-command-button--ghost",
};

const SIZE_CLASS = {
  sm: "copy-command-button--sm",
  md: "copy-command-button--md",
  lg: "copy-command-button--lg",
};

/**
 * 渲染按鈕為 HTML string（適合 innerHTML 大區塊組合）。
 * 配合 `installCopyCommandDelegate()` 註冊的 delegated handler 一起用。
 *
 * @param {Object} opts
 * @param {string} opts.command
 * @param {string} [opts.contextSummary]
 * @param {string[]} [opts.contextRefs]
 * @param {string} [opts.contextNotes]
 * @param {string} [opts.source]
 * @param {"any"|"claude-code"|"cowork"|"codex"} [opts.targetAgent]
 * @param {"primary"|"secondary"|"ghost"} [opts.variant]
 * @param {"sm"|"md"|"lg"} [opts.size]
 * @param {string} [opts.label]
 * @param {string} [opts.title]  hover tooltip
 * @returns {string}  HTML
 */
export function renderCopyCommandButton({
  command,
  contextSummary,
  contextRefs,
  contextNotes,
  source,
  targetAgent,
  variant = "secondary",
  size = "md",
  label,
  title,
} = {}) {
  if (typeof command !== "string" || !command.trim()) {
    throw new Error("renderCopyCommandButton: command is required");
  }

  const variantClass = VARIANT_CLASS[variant] || VARIANT_CLASS.secondary;
  const sizeClass = SIZE_CLASS[size] || SIZE_CLASS.md;
  const buttonLabel = label ?? `📋 複製 ${command.trim()} 指令`;

  const payload = {};
  if (contextSummary) payload.contextSummary = contextSummary;
  if (Array.isArray(contextRefs) && contextRefs.length > 0) payload.contextRefs = contextRefs;
  if (contextNotes) payload.contextNotes = contextNotes;
  if (source) payload.source = source;
  if (targetAgent) payload.targetAgent = targetAgent;

  const payloadAttr = Object.keys(payload).length > 0
    ? ` data-copy-payload="${escapeAttrJson(payload)}"`
    : "";

  const titleAttr = title ? ` title="${escapeAttr(title)}"` : "";

  return `<button type="button" class="${variantClass} ${sizeClass}" data-copy-command="${escapeAttr(command.trim())}"${payloadAttr}${titleAttr}>${escapeHtml(buttonLabel)}</button>`;
}

/**
 * 在指定 root 上掛 delegated click handler，捕捉所有 `[data-copy-command]` 按鈕。
 * App 啟動時呼叫一次即可（main.js）。
 *
 * @param {Element|Document} [root]
 * @returns {() => void}  detach function
 */
export function installCopyCommandDelegate(root = document) {
  if (!root || typeof root.addEventListener !== "function") {
    return () => {};
  }

  const handler = async (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const button = target.closest("[data-copy-command]");
    if (!button) return;

    event.preventDefault();

    const command = button.getAttribute("data-copy-command") || "";
    if (!command) return;

    let payload = {};
    const rawPayload = button.getAttribute("data-copy-payload");
    if (rawPayload) {
      try {
        payload = JSON.parse(rawPayload);
        if (typeof payload !== "object" || payload === null) payload = {};
      } catch (err) {
        console.warn("CopyCommandButton: data-copy-payload JSON parse failed", err);
        payload = {};
      }
    }

    let text;
    try {
      text = assembleCopyPayload({
        command,
        contextSummary: payload.contextSummary,
        contextRefs: payload.contextRefs,
        contextNotes: payload.contextNotes,
        source: payload.source || inferSourceFromContext(button),
      });
    } catch (err) {
      console.error("CopyCommandButton: assemble failed", err);
      showCopyToast({
        variant: "error",
        title: "⚠ 組裝失敗",
        body: err instanceof Error ? err.message : String(err),
      });
      return;
    }

    const result = await copyToClipboard(text);
    if (result.ok) {
      const where = formatTargetAgent(payload.targetAgent);
      showCopyToast({
        variant: "success",
        title: "✓ 已複製到剪貼簿",
        body: `請切到 ${where} 貼上 (Ctrl/Cmd+V) 後執行。`,
        duration: 5000,
      });
    } else {
      console.warn("CopyCommandButton: clipboard write failed", result.error);
      showCopyFallbackModal(text);
    }
  };

  root.addEventListener("click", handler);
  return () => root.removeEventListener("click", handler);
}

function formatTargetAgent(targetAgent) {
  switch (targetAgent) {
    case "claude-code":
      return "Claude Code";
    case "cowork":
      return "Cowork";
    case "codex":
      return "Codex";
    case "any":
    default:
      return "Claude Code / Cowork / Codex";
  }
}

function inferSourceFromContext(button) {
  let el = button;
  while (el && el !== document.body) {
    const src = el.getAttribute?.("data-copy-source");
    if (src) return src;
    el = el.parentElement;
  }
  const route = document.querySelector("#app")?.dataset?.route || "/";
  return `Route ${route}`;
}

function formatTimestamp(ts) {
  if (typeof ts === "string" && ts.trim()) return ts.trim();
  const date = ts instanceof Date ? ts : new Date();
  if (Number.isNaN(date.getTime())) return new Date().toISOString();
  const pad = (n) => String(n).padStart(2, "0");
  return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}`;
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

function escapeAttrJson(obj) {
  // 雙引號屬性 — 把 < > & " ' 全轉義
  return JSON.stringify(obj)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
