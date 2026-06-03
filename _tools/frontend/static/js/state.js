/**
 * Lightweight observable state for the local frontend.
 */

/**
 * @template T
 * @param {T} initialValue
 * @returns {{
 *   value: T,
 *   subscribe: (subscriber: (value: T) => void) => () => void
 * }}
 */
export function createSignal(initialValue) {
  let value = initialValue;
  const subscribers = new Set();

  return {
    get value() {
      return value;
    },
    set value(nextValue) {
      if (Object.is(nextValue, value)) return;
      value = nextValue;
      subscribers.forEach((subscriber) => subscriber(value));
    },
    subscribe(subscriber) {
      subscribers.add(subscriber);
      subscriber(value);
      return () => subscribers.delete(subscriber);
    },
  };
}

const storedTheme = typeof window !== "undefined" ? window.localStorage.getItem("dashboard-theme") : null;

/**
 * @typedef {Object} DashboardData
 * @property {Object|null} scopeCounts
 * @property {Object|null} assets
 * @property {boolean} loading
 * @property {string|null} error
 * @property {string|null} refreshedAt
 */

/** @type {ReturnType<typeof createSignal<DashboardData>>} */
export const dashboardData$ = createSignal({
  scopeCounts: null,
  assets: null,
  loading: false,
  error: null,
  refreshedAt: null,
});

/**
 * @typedef {Object} ScenesData
 * @property {Object|null} data  // { scenes, total, chapters }
 * @property {boolean} loading
 * @property {string|null} error
 * @property {string|null} refreshedAt
 */

/** @type {ReturnType<typeof createSignal<ScenesData>>} */
export const scenesData$ = createSignal({
  data: null,
  loading: false,
  error: null,
  refreshedAt: null,
});

/**
 * @typedef {Object} SceneDetailData
 * @property {string|null} sceneId
 * @property {Object|null} header        // /api/scene/<id>/header
 * @property {Object|null} versions      // /api/scenes/<id>/versions
 * @property {Object|null} summary       // 該場 scene summary（從 scenesData 取）
 * @property {boolean} loading
 * @property {string|null} error
 * @property {string|null} refreshedAt
 */

/** @type {ReturnType<typeof createSignal<SceneDetailData>>} */
export const sceneDetailData$ = createSignal({
  sceneId: null,
  header: null,
  versions: null,
  summary: null,
  loading: false,
  error: null,
  refreshedAt: null,
});

export const state = {
  route: createSignal("/"),
  themeMode: createSignal(storedTheme === "dark" ? "dark" : "light"),
  dashboardData: dashboardData$,
  scenesData: scenesData$,
  sceneDetailData: sceneDetailData$,
};
