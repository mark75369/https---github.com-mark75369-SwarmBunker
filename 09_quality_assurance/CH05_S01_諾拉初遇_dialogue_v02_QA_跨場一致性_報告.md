狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：CH05_S01_諾拉初遇_dialogue_v02 跨場一致性 QA 報告
優先級：中

---
entities: [S-05-01]
depends_on: [C-清道夫, C-諾拉, R-清道夫-諾拉]
weight: {S-05-01: 0.125}
scene_id: S-05-01
source_task: 07_scene_tasks/CH05_S01_台詞任務包.md
source_dialogue: 08_dialogue_outputs/CH05_S01_諾拉初遇_dialogue_v02.md
source_dialogues: null
pipeline_state: QA_PASSED
mode_tag: null
qa_decision: PASS
qa_type: CROSS_SCENE_CONTINUITY
---

# 跨場一致性檢查報告（09_i / CROSS_SCENE_CONTINUITY）

## 檢查對象

- 檔案：CH05_S01_諾拉初遇_dialogue_v02.md；場景：S-05-01；版本：v02；日期：2026-06-03
- scope：chapter（預設，CH-05）。

## 比對範圍盤點（排除規則）

依 09_i 演算法：排除 DRAFT / REVIEW / DEPRECATED / 已刪 + 當前場本身；只與 prior FINAL / LOCKED 場 + per-scene QA 資料比對。

08_dialogue_outputs/ 現有產出：
- CH03_S01_莉娜首戰_dialogue_v02（DIALOGUE_CONVERGED / REVIEW）→ **排除**（非 FINAL/LOCKED，且不同章 CH-03）。
- CH05_S01_諾拉初遇_dialogue_v01A/B/C（trial）→ **排除**（trial 來源版，非獨立場）。
- CH05_S01_..._v02（本場）→ **排除自身**。
- CH08_S02_養殖場真相_v01A/B/C（trial，無 v02）→ **排除**（trial / DRAFT / 不同章）。

**結論：CH-05 章內無其他已定稿（FINAL/LOCKED）場可比；全 Instance 尚無任一 FINAL/LOCKED 台詞場。** 故跨場「實證比對」對象集為空。

## 改以「跨場一致性前瞻檢查」（對未來場的 continuity 約束）

對象集為空時，09_i 不能空判 PASS，須改檢「本場是否埋下會與後續場衝突的一致性地雷」：

| 一致性維度 | 本場狀態 | 與下游場（CH-06 諾拉入隊 / CH-08 真相）相容性 |
|---|---|---|
| 諾拉聲線漂移 | 系統腔 + 萬物換算 + 收尾要睡，初遇冷度 | 相容：弧線起點，後續可演化不衝突 |
| 資訊洩漏 / 重複揭露 | 蟲災真相零洩漏，伏筆只埋不收（行 107） | 相容：CH-08 回收點未被本場提前燒掉 |
| 稱呼一致性 | 諾拉「你」、清道夫「妳/瘋婆子」，未用「外部威脅處理單元」 | 相容：後期稱呼留給關係推進後，未提前 |
| 關係階段 | 暫時休戰（非信任），高價值人力支援起點 | 相容：未跳階到 CH-06+ 的「更好睡的地方 / 安全感來源」 |
| 伏筆 continuity | 「實驗室殘留 / 資訊黑洞」首次放置（§10.1） | 相容：標明回收 CH-08 S-08-02，與 05_e §0 一致 |

## 對抗式攻擊紀錄

1. **攻擊：本場諾拉是否說了任何「她現在不該知道、但本場說出會卡死 CH-08 回收」的話？** 檢視行 107——她明確「數據不足，不下結論」，把真相解碼權留給 CH-08。**攻不破**：未提前燒回收點。
2. **攻擊：本場稱呼 / 關係階段是否超前，導致 CH-06 入隊場會出現「倒退」不一致？** 檢視——本場停在初遇休戰 + 功能稱呼，CH-06 從這裡往「更好睡的地方」推進是自然遞進，無倒退風險。**攻不破**。
3. **攻擊：對象集為空是否應該直接 PASS（敷衍）？** 不可。已改跑前瞻 continuity 檢查（上表 5 維度），確認本場未埋下游衝突地雷，才判 PASS。**這是實質檢查不是空判**。

## Lens 對

- **lens A（跨場指標衝突派）結論：** 無可比 FINAL/LOCKED 場；前瞻檢查 5 維度均與下游場相容，無 continuity 地雷。PASS。
- **lens B（例外辯護派）結論：** 對象集為空非缺陷（本場是 CH-05 首個定稿場、Instance 早期），前瞻約束已涵蓋；無「跨場差異是否真衝突」爭議。PASS。
- **是否分歧：** 否。
- **分歧時 escalate 結果：** N/A。

## Friction 記錄

- 跨場實證比對對象集為空（Instance 尚無 FINAL/LOCKED 場），09_i 此時只能做前瞻 continuity 約束、無法做真正的跨場聲線 / 資訊漂移比對。**這是 Instance 進度早期的固有限制，非本場缺陷。** 建議：CH-03 / CH-08 場定稿後，回頭對 S-05-01 重跑 09_i（scope=arc）做真正跨場比對。

## 結論

PASS。無可比定稿場，已改前瞻 continuity 檢查 5 維度（聲線 / 資訊 / 稱呼 / 關係階段 / 伏筆）均與下游 CH-06/CH-08 相容，未埋衝突地雷。Friction：跨場實證比對待更多 FINAL 場後重跑。
