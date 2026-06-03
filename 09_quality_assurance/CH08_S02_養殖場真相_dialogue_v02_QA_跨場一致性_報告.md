狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：CH08_S02_養殖場真相_dialogue_v02 跨場一致性 QA 報告
優先級：中

---
entities: [S-08-02]
depends_on: [C-清道夫, C-諾拉, R-無名加工公司-諾拉]
weight: {S-08-02: 0.125}
scene_id: S-08-02
source_task: 07_scene_tasks/CH08_S02_台詞任務包.md
source_dialogue: 08_dialogue_outputs/CH08_S02_養殖場真相_dialogue_v02.md
source_dialogues: null
pipeline_state: QA_PASSED
mode_tag: null
qa_decision: PASS
qa_type: CROSS_SCENE_CONTINUITY
---

# 跨場一致性檢查報告（CROSS_SCENE_CONTINUITY / UD §3.9）

## 檢查對象

- 場景：S-08-02（CH-08）
- --scope：chapter（預設，未指定 arc/all）
- 比對排除規則：DRAFT/REVIEW/DEPRECATED/deleted + 本場本身排除

## 比對語料盤點（誠實揭露 corpus 限制）

- CH-08 章內其他已定稿場：**無**（S-08-01 尚無台詞檔）。
- 全 Instance 已 QA_PASSED 場：S-03-01 v02、S-05-01 v02——但兩者 **狀態=REVIEW**（非 FINAL/LOCKED）。依 09_i 演算法嚴格定義「比對 prior FINAL/LOCKED scenes」，此二場尚未升 FINAL，corpus 偏薄。
- **判定影響：** 嚴格 FINAL/LOCKED 比對語料為空。本報告改以「已 QA_PASSED 同主角場（S-03-01 莉娜/清道夫、S-05-01 諾拉/清道夫）做聲線漂移軟比對」+「跨場資訊/伏筆連續性」+「ORG 不變量連續性」執行，並標明此為降級比對（friction：corpus 未升 FINAL）。

## 對抗式攻擊紀錄（先攻擊再判定）

1. **攻擊切角 A — 跨場聲線漂移：**
   - 清道夫：S-03-01/S-05-01 的成本黑色幽默＋去英雄化，與本場「破傷風津貼/又得我們來收/OS 撤回依賴」一致，無漂移。
   - 諾拉：S-05-01 初遇的系統回報＋零抒情＋功利包裝，與本場「離線快取/不是天災/無追責對象」一致；且本場守住 R-ORG-諾拉 §6「不一加入就全知」——S-05-01（CH-05）諾拉不解蟲災真相，本場（CH-08 解禁）才解碼，**跨場資訊弧線連續**。攻不破。
2. **攻擊切角 B — 跨場資訊洩漏/重複揭露：** S-05-01 諾拉停在暗示層、不解真相（該場 09_d 已驗）；本場才在 CH-08 解禁——**未提前、未重複**，解禁時點對齊 05_d §0。攻不破。
3. **攻擊切角 C — 伏筆連續：** 本場回收 S-05-01 實驗室殘留（殘片對應高階技術源頭）＋前期「天災」誤導——回收對象與前場埋設一致，無斷裂。攻不破。
4. **攻擊切角 D — ORG 不變量跨場連續：** R-無名加工公司-諾拉 為 C↔ORG 單向、ORG 永不說話。本場 ORG 0 speaker 行，與 ORG card §11/00_l v0.3 §2.2 不變量一致，跨場無破例。攻不破。
5. **攻擊切角 E — 稱呼/關係階段跨場衝突：** 本場無關係階段躍遷（任務 §12.1），稱呼（瑟琳「傭兵先生」固定、莉娜叫「清道夫」表認可的階段）與前場一致，無提前/倒退。攻不破。

## Lens 雙視角結論

- **Lens A（跨場指標衝突即 FAIL）：** 軟比對範圍內聲線/資訊/伏筆/ORG 不變量/稱呼全連續，無衝突。
- **Lens B（例外辯護派）：** 諾拉 CH-05→CH-08 的「不知→解碼得知」是設計內的資訊弧線推進，非跨場矛盾。
- **是否分歧：** 否。
- **分歧時的 escalate 結果：** N/A。

## 判定

**PASS（降級比對）。** 嚴格 FINAL/LOCKED 語料為空（corpus 未升 FINAL，記 friction），已以 QA_PASSED 同主角場軟比對 + 資訊/伏筆/ORG 不變量連續性執行：跨場聲線一致、解禁時點不提前不重複、伏筆回收連續、ORG 不變量跨場守住。待 S-03/S-05/S-08 升 FINAL 後，建議重跑 09_i 完整 FINAL 比對。
