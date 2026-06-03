狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：CH07_S01_火力掩護_dialogue_v02 跨場一致性 QA 報告
優先級：中

---
entities: [S-07-01]
depends_on: [C-清道夫, C-莉娜, R-清道夫-莉娜, P, CH-07]
weight: {S-07-01: 0.125}
scene_id: S-07-01
source_task: 07_scene_tasks/CH07_S01_台詞任務包.md
source_dialogue: 08_dialogue_outputs/CH07_S01_火力掩護_dialogue_v02.md
source_dialogues: null
pipeline_state: QA_PASSED
mode_tag: null
qa_decision: PASS
qa_type: CROSS_SCENE_CONTINUITY
---

# 台詞 QA 詳細報告 — 跨場一致性（CROSS_SCENE_CONTINUITY）

## 檢查對象

- 檔案：08_dialogue_outputs/CH07_S01_火力掩護_dialogue_v02.md
- 場景：S-07-01
- 版本：v02
- 檢查日期：2026-06-03
- scope：chapter（預設）

## 對抗式立場宣告

審≠寫隔離。對抗預設：「這版與同對前場（莉娜清道夫線）聲線/資訊/節奏弧出現衝突或斷裂」。

## 比較集說明（F-031 前瞻 vs 實證）

- 嚴格 09_i corpus（FINAL/LOCKED 同章場）：**空**。CH-07 內另一場 S-07-02 v02 為 REVIEW/DIALOGUE_CONVERGED（非 FINAL/LOCKED），依 SKILL 09_i 排除 DRAFT/REVIEW，故同章無合格實證比較對象。
- 軟比對（QA_PASSED 同對前場）：S-03-01 v02（莉娜首戰，已 QA_PASSED，同 R-清道夫-莉娜 對）可作 voice/relationship continuity 軟錨；S-04-01（社畜修砲，同對）為 DIALOGUE_CONVERGED 尚未 QA，僅作弧線方向參考。
- 本報告 = 前瞻式 continuity（F-031）+ S-03-01 QA_PASSED 軟比對。

## 攻擊切角（lens A 跨場指標衝突即 FAIL）

1. **攻擊：與 S-03-01 比，莉娜對清道夫的稱呼是否前後衝突？** 攻不破：S-03-01 結尾莉娜首次叫代號「清道夫」=戰技互認信號；本場（更後）莉娜結尾再叫「喂，清道夫」+ 綁任務關心，稱呼演進方向一致（互認→託付後背），無衝突，為合理累進。
2. **攻擊：關係階段是否跳階/倒退？** 攻不破：R-清道夫-莉娜 §D-2 弧線（互嗆→同類社畜→火力搭檔→託付後背→撤離）；S-03-01=戰技互認雛形，本場=託付後背頂點，階段嚴格前進無跳階（任務包 §12.1 確認「S-03-01 起點→此處頂點」）。
3. **攻擊：資訊揭露是否與前場重複揭露或矛盾？** 攻不破：蟲群異常「不對勁」延續前章吐槽加深（非首次揭露、非重複關鍵揭露），蟲災成因持續 HIDDEN，與全線資訊弧一致（W-rules §22.1 / 05_d §0）。
4. **攻擊：聲線指紋是否跨場漂移無因？** 攻不破：兩場清道夫皆成本/記帳語言 + 危機切短；莉娜皆老娘自稱 + 罵綁火控 + 個頭/個屁後綴 + 叫代號表認可。漂移有因（關係階段推進），符合 00_b §17.2 合理變化。

## lens B（例外辯護派 / 跨場差異是否真衝突）

- 本場託付烈度（「我把後面，交給妳」半破戒）高於 S-03-01——lens B：這不是聲線衝突，而是關係頂點的設計性深化（破戒情境 R §5-1），跨場差異屬刻意弧線推進，非斷裂。確認非真衝突。

## 雙 lens 結論

- lens A：跨場稱呼/關係階段/資訊弧/聲線指紋皆連續無衝突（對 S-03-01 軟比對）。
- lens B：託付深化為刻意弧線推進，非衝突。
- 是否分歧：否。
- escalate 結果：N/A。

## 結論

PASS（前瞻式 + S-03-01 QA_PASSED 軟比對）。跨場 continuity 連續，無洩漏/重複揭露/聲線無因漂移。當 CH-07 同章場升 FINAL/LOCKED 後，建議回跑實證 09_i 複核。

## 跨場問題

| 類型 | 前場 | 本場 | 衝突 | 處理 |
|---|---|---|---|---|
| （無） | S-03-01（軟比對） | S-07-01 | 無 | — |

## F-031 / friction 註記

同章 FINAL/LOCKED corpus 為空（S-07-02 僅 REVIEW），09_i 降級為前瞻式 + 同對 QA_PASSED（S-03-01）軟比對。待同章場定稿後回補實證比對，記 friction。
