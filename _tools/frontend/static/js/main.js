import { fetchDashboardData, requestJson } from "./api.js";
import { initRouter } from "./router.js";
import { dashboardData$, state } from "./state.js";
import {
  installCopyCommandDelegate,
  assembleCopyPayload,
  copyToClipboard,
  showCopyToast,
  showCopyFallbackModal,
} from "./components/CopyCommandButton.js";

let dashboardLoadPromise = null;

/**
 * @param {{force?: boolean}} [options]
 * @returns {Promise<any>}
 */
function loadDashboardData({ force = false } = {}) {
  const current = dashboardData$.value;

  if (dashboardLoadPromise && !force) return dashboardLoadPromise;
  if (!force && current.scopeCounts && current.assets && !current.error) {
    return Promise.resolve(current);
  }

  dashboardData$.value = {
    ...current,
    loading: true,
    error: null,
  };

  dashboardLoadPromise = fetchDashboardData()
    .then(({ scopeCounts, assets }) => {
      const nextData = {
        scopeCounts,
        assets,
        loading: false,
        error: null,
        refreshedAt: new Date().toISOString(),
      };
      dashboardData$.value = nextData;
      return nextData;
    })
    .catch(() => {
      const nextData = {
        ...dashboardData$.value,
        loading: false,
        error: "無法連到 server，請確認 server 已啟動",
        refreshedAt: new Date().toISOString(),
      };
      dashboardData$.value = nextData;
      return nextData;
    })
    .finally(() => {
      dashboardLoadPromise = null;
    });

  return dashboardLoadPromise;
}

document.addEventListener("DOMContentLoaded", () => {
  const app = document.querySelector("#app");
  if (!app) return;

  state.route.subscribe((route) => {
    app.dataset.route = route;
  });

  state.themeMode.subscribe((mode) => {
    document.documentElement.dataset.theme = mode;
    window.localStorage.setItem("dashboard-theme", mode);
  });

  document.addEventListener("dashboard:refresh", () => {
    loadDashboardData({ force: true });
  });

  initRouter({
    app,
    onDashboardRoute: () => loadDashboardData(),
  });

  // 安裝通用 CopyCommandButton delegated click handler（UX_SPEC §11.6）
  // — 整個 app 只掛一次；任何 `[data-copy-command]` 按鈕都會被捕捉並執行
  //   assembleCopyPayload + copyToClipboard + showCopyToast 流程
  installCopyCommandDelegate(document);

  // Phase A.0F.patch-concern-2 / UX §11.6.7: LOCKED downgrade guide is pure
  // raw text — NOT a command payload. The LOCKED gate button carries the full
  // guide text in data-locked-guide-text and we write it straight to the
  // clipboard, without the COPY_MARKER_OPEN/CLOSE wrapper that the standard
  // command button applies. CODEX Concern §1 §11.6 / §8 #7.
  document.addEventListener("click", async (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;
    const button = target.closest("[data-locked-guide-button]");
    if (!button) return;
    event.preventDefault();
    const guideText = button.getAttribute("data-locked-guide-text") || "";
    if (!guideText.trim()) return;
    const result = await copyToClipboard(guideText);
    if (result.ok) {
      showCopyToast({
        variant: "success",
        title: "✓ 已複製降級引導文字",
        body: "請切到外部編輯器手動依步驟降級。",
        duration: 6000,
      });
    } else {
      showCopyFallbackModal(guideText);
    }
  });

  window.frontendScaffold = {
    loadDashboardData,
    requestJson,
    // 暴露 CopyCommandButton API 給其他模組或 console debug 用
    copyCommand: {
      assembleCopyPayload,
      copyToClipboard,
      showCopyToast,
      showCopyFallbackModal,
    },
  };
});
