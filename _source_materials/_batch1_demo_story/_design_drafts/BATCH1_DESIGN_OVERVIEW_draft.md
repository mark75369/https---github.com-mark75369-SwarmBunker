狀態：DRAFT
版本：v0.1（Batch 1 設計輪產出；待 user 審 + 對抗式 review）
最後更新：2026-06-02
適用範圍：Batch 1 設計總覽（WI-A/F7/F8短/WI-B/WI-C）
優先級：中

# Batch 1 設計總覽

## ＝＝ 彙整 ＝＝

＝＝＝ Batch 1 設計總覽（供 user 審）＝＝＝
版本：彙整 v0.1 / 2026-06-02 / DECISIONS_LOG 現至 D-055，本批草擬 D-056 起

## 0. 本批是什麼

五個設計 agent 輸出可歸為三組：
- 組 1（同檔高耦合）：WI-A（F9/F11/F12/F13 聲線品質鏈）＋ F7（source 放置規範）＋ F8-短（非角色目標拒絕）。三者都改 `.claude/skills/create-character/SKILL.md` 與 `00_protocol/00_f_角色創建協議.md`，且 F7 是 WI-A 讀 source 的耦合前提 → 必須序列化、同輪規劃。
- 組 2（獨立下游）：WI-B（/qa 對抗式＋分層＋上游真做驗證＋多 lens）。改 `.claude/skills/qa/SKILL.md`＋觸碰 `00_a`/`00_k`。與組 1 無同檔衝突。
- 組 3（流程治理）：WI-C（審核迴圈協議）。新建 `_design/REVIEW_LOOP_PROTOCOL.md`＋AGENTS/CLAUDE 薄 pointer。
- 第五份 = Batch 1 測試計畫，無 fileChanges、無 decisionNeeded，是組 1 實作後的驗收協議（前提：組 1＋WI-B 已落地，否則 BLOCKED）。

本批全部「只設計、不實作」。已驗證現況：create-character/SKILL.md=v0.4 DRAFT（line 159 Split Rules、line 322 D-050 不寫表含 08+00_protocol、line 82 Stage 1、line 296 inputs）；UD=LOCKED v0.5 優先級最高；00_f=DRAFT 但位於 00_protocol/ 受 D-050 子裁決 1 保護。

## 1. 跨項衝突與同檔協調（核心）

### 1.1 create-character/SKILL.md（WI-A + F7 + F8 三方共寫，最高衝突）
三方對同一檔不同區段下手，無內容矛盾但有插入序列依賴：
- WI-A：Stage 1 加既有素材確認、Stage 2 加「既有劇本素材讀取」子節、Stage 3 第7項改寫、Stage 4 §Split Rules 加 4 行（§A/§B/§C/§D）、輸出段加「合法讀取來源表」與 D-050 寫檔表並列。
- F7：Stage 1/2 的 source 預設查找路徑必須指向 D-057 拍板的 `_source_materials/` 結構（與 WI-A 的「讀 source」是同一段邏輯，須共用同一查找根）。
- F8-短：Stage 1 起始 prompt 後插入「Stage 1.0 非角色目標前置判定」gate。
協調點：三方修改必須由「同一個實作 Batch、序列化」完成，不可三個 agent 平行 fan-out 改同檔（會互相覆蓋）。建議單一 owner 一次改完 SKILL.md，順序＝F8 Stage 1.0 gate（最前）→ WI-A Stage 1 素材確認 → WI-A Stage 2 讀取（內含 F7 查找路徑）→ WI-A Stage 3/4/輸出表。

### 1.2 00_f_角色創建協議.md（WI-A + F8 共寫，且為受保護的 00_protocol/）
- WI-A：§4.1 議題順序表加議題 9/10/11、§9 缺漏表加 9/10/11、§10 新增 §10.12/13/14 script、§10.9 拆分表加 §A-§D、§2 啟動條件補「既有素材選填」。
- F8-短：§Stage 1 對應段補「非角色目標前置判定」規則。
協調點：兩者都動 00_f，且 00_f 受 D-050 子裁決 1「嚴禁 /create-* 寫 00_protocol/」保護 → 任何對 00_f 的 patch 都需 master 拍板授權（非 skill runtime 寫，是 design-time 人工 patch）。已驗證 00_f §2/§4.1/§10.9 區段存在，插入點不相撞，但仍須序列化。WI-A 的 00_f 改動規模遠大於 F8（F8 可選擇不動 00_f，僅改 SKILL.md — 見 D-058）。

### 1.3 UD（LOCKED 最高優先）只有 WI-A 觸碰
WI-A 要在 UD §1.2.2 加 3 個 script 並重編號「§10.9 拆分規則」。WI-B 明確聲明「不改 UD 演算法定義，只在 SKILL.md 加 lens 拆分」→ 兩者不撞 UD。但 WI-A 的 UD 重編號會牽動所有引用「§10.9 拆分規則」舊編號的 cross-ref（registry protocol_ref、SKILL.md 議題映射）。

### 1.4 registry template（LOCKED-tier 兩份）
- WI-A 改 `issue_type_registry.template.yaml`（加 core id 9/10/11）。
- F7 改 `entity_type_registry.template.yaml`（僅加註解，不加型別）。
兩份是不同檔，無直接衝突；但同屬 registry template「LOCKED-tier / D-047 contract」，建議同一拍板可見範圍處理。

### 1.5 AGENTS.md / CLAUDE.md（F7 + WI-C 共寫 root 兩檔）
- F7：在目錄結構/慣例說明補 `_source_materials/` 用途。
- WI-C：加「審核迴圈（四層防線）」pointer 段於 `## 修改流程` 後。
協調點：兩者都動 root AGENTS.md 同一帶（修改流程/慣例附近）＋都受 D-048 AGENTS/CLAUDE 同步規則約束 → 兩處內容須對齊、且只動 production root 那份（不動 `_sandbox/snapshot/`）。序列化插入避免行衝突。

### 1.6 00_protocol-tier 集中拍板
WI-A（00_f）、F8（00_f）、WI-B（00_a/00_k）都觸 00_protocol-tier；WI-A 還觸 UD（LOCKED 最高）。全部需正式拍板 + 影響範圍評估，本批僅設計。

## 2. 草擬 D-056 起決策清單

見 draftDecisions 結構欄。對應關係：
- D-056 = WI-A D-A1（改 LOCKED UD 加 3 script）
- D-057 = WI-A D-A2（改 issue_type_registry.template 加 id 9/10/11）
- D-058 = F7 source 放置 convention
- D-059 = F8-短 非角色拒絕是否入 00_f
- D-060 = WI-B QA 對抗式立場入 00_a（原 D-B1）
- D-061 = WI-B 分層 QA 是否突破 D-043 8份硬規（原 D-B2）
- D-062 = WI-B 上游真做驗證跨-skill 紀律入 00_k（原 D-B3）
- D-063 = WI-C 審核迴圈落地位置
- D-064 = WI-C 四層防線強制力等級＋規模豁免
- D-065 = WI-C / L2 腳本 scope 擴及 CLAUDE.md+skills（可併入 D-064 或留 backlog NEW_REQ）

注意：F7 原稿把 source convention 編為「D-057」、F8 編為「D-058」；本彙整重新統一編號為 D-058（source）/ D-059（F8），請以本清單為準避免與 WI-A 的 D-056/D-057 撞號。

## 3. LOCKED / 協議級檔變更彙總

見 lockedChangeList 結構欄。摘要：
- LOCKED 最高：UD（WI-A，需 D-056）
- LOCKED-tier registry：issue_type_registry.template（WI-A，需 D-057）、entity_type_registry.template（F7 僅註解）
- 00_protocol/（受 D-050 子裁決 1）：00_f（WI-A + F8）、00_a（WI-B 需 D-060）、00_k（WI-B 需 D-061+D-062）
- root 治理檔：AGENTS.md / CLAUDE.md（F7 + WI-C，受 D-048 同步規則）

## 4. 實作順序（同檔序列化）

見 implementationOrder 結構欄。

## 5. 仍需 user 拍板

見 openQuestionsForUser 結構欄。最關鍵三題：(a) D-056 是否准動 LOCKED UD；(b) D-061 是否准分層 QA 突破 D-043 8份硬規（牽 enum 連鎖）；(c) D-058 source convention 選 A/B/C（決定 WI-A 查找路徑，必須先拍）。

## ＝＝ 各工作項設計 ＝＝


### WI-A：/create-character 聲線品質升級鏈（F9 個性拆解 + F11 既有劇本萃取 input + F12 Source Coverage/Hooks + F13 既有劇本台詞聲線基準）— 同一輪、同一組檔（create-character SKILL.md + 00_f 協議 + UD §1.2.2 LOCKED + registry template）一致落地設計。本輪只設計、不實作。

## 0. 設計總綱與一致性原則

四個 finding 必須同檔、同輪、互不衝突地落地。對應 NEW_REQ_35(F11 input) / NEW_REQ_37(F13 output 強化, CRITICAL) / NEW_REQ_33(F9 個性拆解) / NEW_REQ_36(F12 Source Coverage)。F11+F13 為 input/output 一氣呵成（單做任一無效）；F9/F12 為 output 段可獨立但同輪做最省。

**統一架構決定（貫穿四項）：**
1. **輸入層擴充（F11+F13）** 落在 SKILL.md Stage 1（確認來源 + speaker alias）與 Stage 2（讀取執行 + 篩選）。
2. **輸出層三新段（F9/F12/F13）** 落在聲線卡固定段，並在 SKILL.md Stage 4 §Split Rules、00_f §10.9 拆分表、UD §10.9 拆分表三處同步登錄，否則 Stage 3 chat 顯示但 Stage 4 寫檔消失（F12 verify 已證實此 bug）。
3. **議題層** 新增三個 user-facing 議題到 registry core（id 9/10/11）+ 00_f §10 + UD §1.2.2 §10 對應 script，因為 Stage 2 是 D-047 動態構建，固定段必須有對應議題才會被問到、才會有素材寫入。
4. **D-050 讀寫邊界明示（F13 關鍵）**：08_dialogue_outputs/ 在現行 SKILL.md「不寫」清單，但 D-050 子裁決 2 只規範「寫」不規範「讀」。F13 要求明示「可讀不可寫」，需新增一條「合法讀取來源表」與既有「D-050 寫檔目錄表」並列，避免 agent 誤以為 08 全禁。

**聲線卡新段插入位置（相對現行 8 技術段，採固定編號附加段）：**
現行卡技術段為「角色定位 / 聲線輪廓 / 聲線範例 / 去名測試紀錄 / 合規檢查紀錄 / 髒話來源 / 偏移檢查 / 聲線污染檢查 / 與類型氣質合規」。新段建議統一掛在技術段之後，順序為：
- §A 個性拆解（F9）— 緊接「角色定位」之後最佳（人物理解先於技術規格），實作上採「append 在卡尾、但用固定錨點標題」即可，不強制重排既有段。
- §B 既有劇本台詞聲線基準（F13）
- §C 既有劇本聲線使用規則（F13）
- §D Source Coverage / 下游 Hooks（F12）— 永遠放卡尾（它是「本卡如何被下游消費」的總結）。

---

## 1. F11 輸入層設計（Stage 1/2 主動讀既有劇本/docx/txt/csv/json + speaker alias）

### 1.1 SKILL.md Stage 1 擴充（在現行開場 prompt 後加一段「既有素材確認」）
Stage 1 開場 prompt 之後，agent 必須加問（固定 wording 骨架）：
> 除了人設想法，這個角色是否有**既有劇本台詞**可供參考？（翻拍 / 續作 / 已寫過的場景）
> 若有，請提供：(a) 檔案或貼上內容（支援 .md / .docx / .txt / .csv / .json）；(b) 該角色在劇本裡的 **speaker 標籤 / 別名**（例：MainGirlA = 瑟琳）。
> 既有台詞是最接近最終玩家體驗的聲線資料，會大幅提升聲線卡準確度。沒有也可以，我會只用人設建卡並標註「無既有劇本基準」。

診斷報告（Stage 1 結尾）新增一列：**「既有劇本素材狀態」**＝ 無 / 已提供（檔名 + 格式）/ 待提供。

### 1.2 SKILL.md Stage 2 讀取執行規範（新增子節「## 既有劇本素材讀取」）
- **讀取範圍**：`08_dialogue_outputs/`、user 提供的外部 .docx/.txt/.csv/.json，以及副對話（連動 F10/NEW_REQ_34 機制）轉述的 evidence summary。
- **speaker alias 比對**：建立 alias map（如 `MainGirlA → C-瑟琳`），只抽取比對命中的台詞；命中不確定的標 `<!-- INFERENCE: alias MainGirlA→瑟琳 為推定，待人類確認 -->`。
- **docx fallback**：若執行環境無 docx 解析能力（scripts/ 目前無 docx 支援，已查證），agent 印 `WARN：docx 無法自動解析，請改貼純文字或用副對話轉述`，不得靜默跳過。
- **不寫保證**：本段反覆明示「讀 08_dialogue_outputs/ 屬讀取，不觸發任何寫入；本 skill 永不寫 08」。

### 1.3 議題層（registry core 新增 id 9）
新增 user-facing 議題 9「既有劇本台詞萃取」（required_level: STRONGLY_PREFERRED, locked: false）：當 Stage 1 確認有既有素材時觸發，問 speaker alias + 篩選優先場景；無素材時 agent 自動跳過並 phase_log 記 `9: skipped(無既有劇本)`。

---

## 2. F13 輸出層設計（既有劇本台詞聲線基準 + 既有劇本聲線使用規則；含 8-12 句篩選標準）

### 2.1 篩選標準（8-12 句，覆蓋 8 場景類型 — 固定清單）
agent 從既有台詞按以下 8 類各挑 1-2 句代表（總 8-12 句），無對應類別標「（既有劇本無此類）」：
1. 初登場 / 第一印象句
2. 危機反應（險境 / 突發）
3. 任務前準備 / 決策句
4. 戰後 / 事件後反應
5. 日常互動 / 閒談
6. 被肯定 / 被吐槽時的回應
7. 關係推進 / 情感升溫節點
8. 中後期成長語氣（與初期對比）

### 2.2 聲線卡新段 §B「既有劇本台詞聲線基準」（確切標題 + 欄位骨架）
```md
## §B 既有劇本台詞聲線基準
> 來源：<既有劇本檔名/路徑> via speaker alias <alias→C-name>。本段為「最接近最終玩家體驗」的聲線錨點，優先級高於人設推導；與人設衝突時於此標 CONFLICT 待人類拍板。
> D-050 邊界：本段內容為「讀 08_dialogue_outputs/ 或既有劇本」萃取，本 skill 不寫 08。

| 場景類型 | 代表台詞（原文引用） | 聲線特徵歸納 |
|---|---|---|
| 初登場 | "<原句>" | <句長/語氣/潛台詞> |
| 危機反應 | "<原句>" | ... |
| 任務前準備 | ... | ... |
| 戰後反應 | ... | ... |
| 日常互動 | ... | ... |
| 被肯定/被吐槽 | ... | ... |
| 關係推進 | ... | ... |
| 成長語氣 | ... | ... |

**指紋總結（3-5 條）：** <從上表歸納的可複用聲線規律>
**與人設 source 的差異：** <既有劇本揭示但人設沒寫到的規律；或衝突點標 CONFLICT>
```

### 2.3 聲線卡新段 §C「既有劇本聲線使用規則」（確切標題 + 欄位骨架）
```md
## §C 既有劇本聲線使用規則
> 給 /dialogue-write 的「如何使用上面基準」指引。

- **直接複用**：哪些原句/句式可被下游直接借用或仿寫。
- **僅供語感、不可照抄**：哪些屬具體劇情綁定，只能取語氣不取內容。
- **已過時 / 不再採用**：既有劇本中已被人設或本卡 supersede 的舊聲線（標明原因）。
- **alias 對照表**：<原劇本 speaker 標籤> = <C-name>（供下游回溯）。
- **覆蓋優先序**：既有劇本基準 > 本卡技術段推導 > 人設 source 推測（衝突時的採用順序）。
```

### 2.4 cross-ref STYLE_ANCHOR / W-style（D-055 / NEW_REQ_21）
§B 開頭加一行：「本段為**角色級**聲線基準，應與作品級 W-style 文風指紋（01_world/01_d，D-055 STYLE_ANCHOR）分層互補：W-style 管作品文風，本段管角色聲線。」（只 cross-ref，不在本輪實作 W-style 繼承機制。）

### 2.5 議題層（registry core 新增 id 10）
議題 10「既有劇本聲線基準與使用規則」（STRONGLY_PREFERRED, locked: false）：依議題 9 萃取結果產 §B/§C。無既有素材時 §B/§C 寫 placeholder「無既有劇本基準（僅人設建卡）」，狀態保持 DRAFT。

---

## 3. F9 輸出層設計（個性拆解固定段 — 10 子段）

### 3.1 聲線卡新段 §A「個性拆解」（確切標題 + 10 子段骨架）
對照 sandbox 目標卡（瑟琳 §2/§3/§7/§8 已隱含此結構），固定 10 子段：
```md
## §A 個性拆解
1. **表層個性**（聽得到的那一面）：<玩家第一耳聽到什麼>
2. **內在個性**（驅動台詞的那一面）：<真正決定他說什麼的底層>
3. **自尊來源**：<他的價值感建立在什麼上>
4. **核心恐懼**：<他最怕失去/變成什麼>
5. **情緒遮掩**：<他如何藏情緒；用什麼掩飾>
6. **魅力來源**（可愛/吸引點）：<讓人喜歡這角色的具體聲線點>
7. **努力與缺陷表現**：<他怎麼努力、缺陷怎麼在台詞露出>
8. **壓力變形**：<壓力下聲線怎麼變；對齊既有「壓力下語言變形」段，若已有則此處給總綱、細節指向該段>
9. **角色差異**：<與哪些角色易混；差別在哪>（與「去名測試」「聲線污染」呼應，不重複而是人物層總結）
10. **不可偏移人格模板**：<3-5 條「無論劇情怎麼推都不能變的人格核心」>（與「偏移檢查」呼應；偏移檢查是聲線層，本子段是人格層）
```

### 3.2 與既有段的去重原則（避免衝突）
§A「個性拆解」是**人物理解層**；既有「偏移檢查 / 聲線污染 / 與類型氣質合規」是**技術執行層**。設計上 §A 子段 8/9/10 在 wording 上明示「總綱在此、細節見對應技術段」，避免內容打架。00_f §9 缺漏表須補議題 11 缺漏處理（見 §5）。

### 3.3 議題層（registry core 新增 id 11）
議題 11「個性拆解」（STRONGLY_PREFERRED, locked: false）：agent 主導從人設 + 既有劇本（若有）+ 聲線測試（議題 2）綜合產出 10 子段初判，user 逐項確認/修正。

---

## 4. F12 輸出層設計（Source Coverage / 下游 Hooks 固定尾段 — 5 子段）

### 4.1 聲線卡新段 §D「Source Coverage / 下游 Hooks」（確切標題 + 5 子段骨架）
永遠置於卡尾。對應 NEW_REQ_36 五子段：
```md
## §D Source Coverage / 下游 Hooks
> 本段保存「source 檔中有價值但不屬本卡主體」的資訊，供下游 skill 承接。D-050：本段只是登錄 hooks，不授權本 skill 寫任何下游檔。

1. **已吸收進聲線主體的 source 資訊**：<已轉化進本卡各段的素材清單>
2. **交給 /create-relationship 的 hooks**：<關係相關線索（不在本 skill 寫 04）>
3. **交給 /create-outline / /create-detailed-outline 的 hooks**：<劇情/弧線線索（不在本 skill 寫 05/06）>
4. **交給 /scene-task 的 hooks**：<場景/任務包線索（不在本 skill 寫 07）>
5. **不應直接當台詞使用的 source 資訊**：<背景設定/作者筆記等，僅供理解不可入台詞>
```

### 4.2 與 Stage 3 Downstream notes 的接線（修 F12 verify 的 bug 根因）
現行 SKILL.md Stage 3 第 7 項「Downstream notes ... without granting writes」只在 chat 出現、Stage 4 無對應寫檔段 → notes 消失。設計修正：Stage 3 預告稿第 7 項改為「Downstream notes（將寫入聲線卡 §D Source Coverage，不寫下游檔）」，並在 Stage 4 §Split Rules 加 §D 寫入行。如此 chat 預告與寫檔一致。

### 4.3 議題層
F12 不需獨立 user-facing 議題（它是 agent 對既有議題 1-11 答案的「下游分流總結」），由 Stage 4 機制固定產出，類似 §10.9 拆分規則的 agent-side mechanic。在 00_f §10.9 與 UD §10.9 拆分表加 §D 對應行即可。

---

## 5. 三檔同步登錄清單（一致性核心 — 缺一即 F12-style 消失 bug）

### 5.1 SKILL.md Stage 4 §Split Rules 新增 4 行
在現行 8 行拆分表後加：
| source | target | write mode |
|---|---|---|
| 議題 11 個性拆解 | voice card `§A 個性拆解` | overwrite |
| 議題 10 既有劇本基準 | voice card `§B 既有劇本台詞聲線基準` + `§C 既有劇本聲線使用規則` | overwrite |
| 議題 1-11 下游分流（agent mechanic）| voice card `§D Source Coverage / 下游 Hooks` | overwrite |

### 5.2 00_f §10 新增三個議題 script（§10.12 / §10.13 / §10.14，沿 UD 格式）+ §10.9 拆分表加 §A/§B/§C/§D 行 + §9 缺漏表加議題 9/10/11 缺漏處理 + §4.1 議題順序表加 3 列。

### 5.3 UD §1.2.2 新增 §10.9（既有劇本萃取）/ §10.10（既有劇本基準與規則）/ §10.11（個性拆解）三個完整 agent 提問 script，並把現行「§10.9 拆分規則」重編號為 §10.12（或在拆分表加 §A-§D 行）。**注意 UD 為 LOCKED，需拍板（見 decisionNeeded D-A1）。**

### 5.4 registry template `00_f_character` core 新增 id 9/10/11 三 entry（皆 STRONGLY_PREFERRED, locked: false）。**registry template 改動需拍板（見 decisionNeeded D-A2）。**

---

## 6. 相依（不在本 agent 設計範圍，但標明）
- **/iterate-character SKILL.md** 必須認得新段 §A/§B/§C/§D：其「影響範圍評估規範」與 Stage 4 寫檔需把新段納入「目標聲線卡 scope」；現行只說「聲線卡」整體，技術上已涵蓋，但 §B/§C 含既有劇本萃取，iterate 時也應能讀 08/外部素材（與本輪 F11/F13 input 機制對齊）。列為相依工作項，由後續 agent 設計。
- /export-character / /view-character 的組裝邏輯會自動帶出新段（純讀，無需改），但若要在 view 加 TOC 錨點屬可選微調。

## 7. 邊界與不做
- 不在本 skill 寫 08_dialogue_outputs/（只讀）。
- 不擴大 D-050 寫檔目錄（仍限 03_characters/）。
- 不在本輪實作 docx parser（scripts/ 無 docx；用 agent runtime / 副對話 fallback + WARN）。
- 不實作 W-style 繼承機制（只 cross-ref）。

### F7 + F8-短：source 素材放置規範 + /create-character 非角色目標拒絕（設計，本輪不實作）

## 0. 設計前提與現況確認（已讀證據）

### 0.1 掃描機制現況（三條獨立掃描路徑，互不一致 — 這是 F7 的根因）
- **`scripts/parse_frontmatter.py`** 的全 repo 掃描函式（`_iter_repo_markdown_files` L1428、`_collect_repo_entity_ids` L2296、`detect_silent_drops` L732、`detect_qa_type_silent_drops` L684、`build_repo_index` 經由 L1428）一律 `repo_root.glob("**/*.md")`，**只排除 `.git`**（`".git" in path.parts`）。沒有任何 source/ 或底線目錄排除。export 路徑另有 `EXPORT_EXCLUDED_RECORD_DIRS = {".git","_design","_archive","archive","_user_manual"}`（L99）只用於 export-record，不影響 entity 掃描。
- **`scripts/check_paths.py`**：掃 `ACTIVE_DIRS`（00–09 + _design）用 `d.rglob("*.md")`（**遞迴**），有 `IGNORE_DIR_NAMES = {.git, archive, node_modules, __pycache__, .venv, venv, scripts}`（L57-65），靠 `rel.parts[:-1]` 比對排除（L125）。**沒有 source/reference**。它只檢查「內文路徑引用是否存在」，不檢查 header；對 source 檔本身不會報 header 缺漏，但 source 檔內文若引用不存在路徑會被 ERROR。
- **`scripts/check_headers.py`**：`TEMPLATE_PATTERNS` 全部是 `REPO_ROOT.glob("00_protocol/*.md")` 形式（**非遞迴，單層**，L27-39、L46）。**關鍵事實**：`03_characters/source/瑟琳.md` 這種「子目錄內」的檔案**不會被 check_headers 掃到**（因為是 `03_characters/*.md` 單層）。但 user 報告的 `03_characters/女_1_瑟琳_人設v_0_1.md`（直接放在 `03_characters/` 第一層）**會**被 check_headers 報 5 欄 header 缺漏，也會被 parser `**/*.md` 掃到。
- **結論（修正 F7 報告的部分敘述）**：F7 報告說「source 檔被 parser/header/status 阻斷」只在 source 檔放在**模組目錄第一層**時成立；一旦放進**子目錄**，check_headers 因非遞迴已天然漏掉，但 parser 的 `**/*.md` 仍會掃到（且若 source 檔含裸 `---` HR 會撞 F15 NEW_REQ_39 的 unclosed-YAML bug）。因此 F7 的乾淨解必須同時處理 parser 的 `**/*.md` 與 check_paths 的 rglob，否則 source 檔仍被部分工具掃描。

### 0.2 entity 計數現況
- `/status`、`/check-gaps` 都靠 `build_repo_index` + frontmatter `entities` 欄位 + phase_log。**source 檔若沒有 `entities:` 欄位就不會被計成實體**（`_collect_repo_entity_ids` L2302 要求 `entities` 是 list）。所以「source 被當實體計入進度」這件事，只有在 source 檔誤填 `entities:` 時才發生；真正的痛點是 **header 缺漏 ERROR**（check_headers）與 **YAML 誤判 ERROR**（parser，F15）。
- `entity_type_registry.template.yaml` 的 C 型別 `target_dir: 03_characters/`（L37），沒有 main/minor/npc/source 細分；registry 不是「掃描白名單」，純粹是 id_pattern + target_dir 對照，因此 registry 本身不需要為 source 排除負責，但**需要新增一行註記說明 source 不是 entity**以免未來誤解。

### 0.3 /create-character Stage 1 現況
- `00_f` 五階段，Stage 1（SKILL.md L82-101）做 chat-only 診斷，無任何「target 是否為會說話的角色」判斷。寫檔邊界 D-050 限定 `03_characters/`（L22-24 只列 main/minor/npc）。無 non-character refusal logic。

---

## 1. F7 設計：source 素材放置規範

### 1.1 方案比較（三方案，對齊 NEW_REQ_31 A/B/C）

| 方案 | 放置位置 | header 要求 | parser/check 排除做法 | 跨層成本 | 與 WI-A(F11/F13 讀 source) 的耦合 |
|---|---|---|---|---|---|
| **A（推薦）** | 全域單一 `_source_materials/`，下分 `characters/ world/ outline/ dialogue/`（依用途，不依模組編號）| **不需** 5 欄 header | 底線前綴 + 加入所有掃描器的 ignore set | 中（5 掃描點 + registry 註記 + SKILL.md + AGENTS/manual）| skill 讀 source 只需指向一個固定根，最簡單 |
| B | 各模組目錄下 `source/` 子夾（如 `03_characters/source/`）| 不需 | 各掃描器加 `source` 到 ignore；但 check_paths IGNORE 比對 `rel.parts[:-1]` 可直接加，parser 要改 `**/*.md` 過濾 | 中高（路徑分散，五個 /create-* 各自指向不同 source/）| skill 要按模組找 source，較分散 |
| C | source 仍需 header 但靠 metadata（如 `doc_role: source`）讓 parser 不視為 entity | 需 5 欄 | 改 parser 語意層而非路徑層 | 高（動 parser 語意 + header 規範）| 不影響讀取，但 user 要為每個素材寫 header，量產體驗差 |

### 1.2 推薦：方案 A（全域 `_source_materials/`，底線前綴排除）

**理由**：
1. 與既有慣例一致——repo 已用底線前綴目錄表示「非實體工作區」（`_design/`、`_user_manual/`、`_archive/`），export 排除清單 `EXPORT_EXCLUDED_RECORD_DIRS` 已包含這些底線目錄。新增 `_source_materials/` 語意自洽。
2. **單一根**讓 WI-A（F11/F13 skill 讀 source）只需一個固定查找點，避免方案 B「skill 要按模組猜 source 位置」的耦合複雜度。這是任務明示的耦合前提。
3. source 是「user 原始輸入素材」，本質不屬於任一模組產物，放全域比塞進 `03_characters/` 更符合語意（人設 source 同時餵 /create-character 與 /create-relationship）。
4. 排除實作最簡單：底線前綴可用一條規則覆蓋所有掃描器。

**目錄結構（建議，不強制子分類）**：
```
_source_materials/
  README.md            （唯一需 5 欄 header 的檔；說明本目錄用途與排除規則）
  characters/          （人設 source：女_1_瑟琳_人設v_0_1.md 等）
  world/               （世界觀 source）
  outline/             （劇情/關卡 source）
  dialogue/            （既有劇本台詞 source；.docx/.txt/.csv/.json 亦可）
  _原始劇本.docx       （非 .md 素材直接放，掃描器本就只掃 *.md）
```

### 1.3 header 必填性裁定
- `_source_materials/` 下的 **.md 素材檔不需要 5 欄 header**（這是方案 A 的核心便利）。
- **唯一例外**：`_source_materials/README.md` 需 5 欄 header（狀態：DRAFT / 版本 / 最後更新 / 適用範圍 / 優先級），作為目錄說明與排除規則的權威來源，並讓 check_headers 仍能驗證它。
- 非 .md 素材（.docx/.txt/.csv/.json）本來就不被任何掃描器掃（全部只 glob `*.md`），無需處理。

### 1.4 各掃描器排除規則（實作者照著改）

實作者需新增一個**共用排除判定**（建議在 `parse_frontmatter.py` 定義常數，其他兩個 check 腳本 import 或各自複製）：

```python
# parse_frontmatter.py 新增（與 EXPORT_EXCLUDED_RECORD_DIRS 並列）
SOURCE_MATERIAL_DIR_NAMES = {"_source_materials"}
# 通用判定：任一路徑段命中即排除（除了該目錄自己的 README.md 走 check_headers 白名單）
```

**逐點改動**：
1. **`parse_frontmatter.py`** — 在 `_iter_repo_markdown_files`（L1428）、`_collect_repo_entity_ids`（L2296）、`detect_silent_drops`（L732）、`detect_qa_type_silent_drops`（L684）四處 `glob("**/*.md")` 迴圈的 skip 條件，從 `".git" in path.parts` 擴成 `".git" in path.parts or any(p in SOURCE_MATERIAL_DIR_NAMES for p in path.parts)`。建議抽成一個 helper `def _is_ignored_scan_path(path)` 統一這四處（也順手收斂未來維護）。
   - 注意：`README.md` 在 `_source_materials/` 內也會被一併排除掃描——這是可接受的，因為 README 本身沒有 entity，排除不影響 entity 計數；check_headers 才負責驗它（見下）。
2. **`check_paths.py`** — `IGNORE_DIR_NAMES`（L57-65）新增 `"_source_materials"`。既有 `rel.parts[:-1]` 比對（L125）即自動生效（含整個子樹）。
3. **`check_headers.py`** — 因為 `TEMPLATE_PATTERNS` 是單層白名單且不含 `_source_materials/`，**source 素材天然不會被掃**，無需改。但**需新增一行**讓 README 被驗證：在 `TEMPLATE_PATTERNS`（L27-39）加 `"_source_materials/README.md"`（精確檔，非 glob 整夾），確保唯一需 header 的檔被檢查。
4. **`/status`、`/check-gaps`** SKILL.md — 因兩者底層走 `build_repo_index`（已在第 1 點排除），行為自動正確。仍建議在兩 SKILL.md 的「掃描範圍」說明段補一句「`_source_materials/` 為 user 原始素材區，不計入實體進度、不報 header 缺漏」，避免未來 agent 誤解。

### 1.5 entity_type_registry 註記
在 `entity_type_registry.template.yaml` 頂部註解區（L1-5 附近）新增一行說明：
```yaml
# Source materials live in <instance_root>/_source_materials/ and are NOT entities.
# They carry no entity ID and are excluded from all frontmatter scans.
```
不新增任何 core/reserved 型別（嚴守「F7 不新增 entity 型別」）。

### 1.6 與 WI-A（F11/F13 skill 讀 source）對齊
- F11/F13 要讓 /create-character「讀既有劇本/人設 source 但不寫」。方案 A 提供**固定可預期的查找根** `_source_materials/`：WI-A 設計時，skill 的 Stage 1/2 input 探測順序建議為「先問 user 是否有素材 → 預設掃 `_source_materials/characters/` 與 `_source_materials/dialogue/` → 也接受 user 直接貼路徑」。
- **本設計需與 WI-A 共同拍板的耦合點**：WI-A 讀取的「預設查找路徑」必須等於本設計拍的 `_source_materials/` 結構。若 D-057 改採方案 B（各模組 source/），WI-A 的查找邏輯要改成「按 entity 類型對應到 `03_characters/source/` 等」——成本較高。**故推薦 A 也利於 WI-A**。此耦合點列入 decisionNeeded D-057。

---

## 2. F8-短 設計：/create-character Stage 1 非角色目標拒絕（短期版，不新增 entity 型別）

### 2.1 目標與邊界
- 短期版**只在 /create-character Stage 1 加一個診斷分支**：偵測 target 是否為「不會說話的組織/制度/殘留實體」，若是則**拒絕建立 C-* 並給替代建議**。
- **不新增** F-*/ORG-* entity（那是方向 A，13+ 輪 scope）。
- **不動** entity_type_registry、parser、其他 SKILL.md。最小 footprint：僅 `create-character/SKILL.md` Stage 1 + `00_f_角色創建協議.md` 對應段。

### 2.2 判斷邏輯（放在 Stage 1 診斷「之前」，作為前置 gate）

在 SKILL.md `### Stage 1 - Diagnosis`（L82）**起始 prompt 之後、產出診斷報告之前**插入一個判定子步驟「Stage 1.0 — 目標可說話性檢查」：

```md
### Stage 1.0 — 目標可說話性檢查（non-character refusal gate）

在進入聲線診斷前，對每個 target 名稱判斷其是否為「可承載角色聲線的會說話主體」。
若 user 提供的描述顯示某 target 屬下列任一型別，視為「非角色目標」：

- 已破產/清算/解散，只剩文件或遺留物、不會主動說話的組織或公司
- 制度、法規、體系、機制等抽象規則性存在
- 純背景設定的勢力/陣營（無具體可發聲的代表人物）
- 地點、物件、事件本身（非擬人化）

判定信號（任一即提問確認，不武斷拒絕）：
- user 描述含「公司/組織/勢力/制度/體系/機構」且**未指定一個會說話的代表人物**
- user 描述含「已破產/已清算/已解散/只剩文件/不會說話/沒有人格」
- target 名稱本身是組織名而非人名，且 user 未說明擬人化發聲口徑
```

**處理流程（三步）**：
1. **不武斷**：偵測到信號時，先問一句確認，而非直接拒絕：
   ```md
   `<target>` 看起來是組織/制度而非會說話的角色。請確認：
   (a) 它有一個會說話的代表人物（請給人名，我改建那個人為 C-*）
   (b) 它本身不會說話，只是對抗來源/背景設定
   ```
2. **若 user 選 (b) 或確認非角色** → **拒絕建立 C-***，輸出標準拒絕 + 三個替代建議：
   ```md
   ⏸ 條件未滿足：`<target>` 不是會說話的角色，/create-character 不建立 C-<target>。

   建議改用：
   1. 若它與某會說話角色有對抗/從屬關係 → 用 `/create-relationship <會說話角色> <該角色相關方>`，
      把該組織的影響寫進關係，或在 01_a §9「勢力與組織」記為 W-rules 子段。
   2. 若它有可發聲的代言人 → 改 `/create-character <代言人名>`，把組織背景寫進該角色 source。
   3. 若未來需要獨立的「組織/勢力」實體型別 → 此為 F8 方向 A（新 F-*/ORG-* entity），
      屬未來 patch round；本輪標記待未來 entity 型別，不在此建立。
   ```
3. **若 user 選 (a)（指定代表人物）** → 把 target 改成該人名，正常進 Stage 1 診斷。

### 2.3 與既有「啟動前檢查」的關係
- 此 gate 屬 Stage 1 內的**內容語意判斷**，與「啟動前檢查」（L52-77，那是 repo 結構/前置實體/重名檢查）不同層，**不混入**。放 Stage 1.0 是因為要先看 user 對該 target 的描述才能判斷，而描述是 Stage 1 起始 prompt 才取得的。
- 拒絕用既有 `⏸ 條件未滿足` 標準 wording（與 L66 一致），維持 skill 既有體例。

### 2.4 00_f 協議對應段
`00_protocol/00_f_角色創建協議.md` 屬 LOCKED-tier 00_protocol。需在其 Stage 1 對應段補一條「非角色目標前置判定」規則。**此為動 00_protocol/，必須 D-058 拍板授權**（方向 C）。若不願動 00_protocol，退而求其次：僅改 SKILL.md，並在 SKILL.md 註明「本 gate 為 D-058 方向 C 短期措施，00_f 協議待方向 A 一併納入」——此分歧列入 decisionNeeded。

### 2.5 W-language 文件語體（方向 B）標記
方向 B（擴 W-language 承接「不會說話組織的文件語體」）**不在 F8-短範圍**，但拒絕訊息的替代建議 1 已預埋接口（記入 01_a §9 / W-rules 子段），未來方向 B 可平滑接上。本輪僅在 decisionNeeded 提醒。

---

## 3. 不做什麼（守 LOCKED 紀律）
- 不新增任何 entity 型別（registry core/reserved 不動，只加註解）。
- 不改 parser 語意層（不採方案 C 的 doc_role metadata）。
- 不擅改 00_protocol/00_f：動它需 D-058 授權；否則只動 SKILL.md。
- 不寫任何 production 檔（本輪純設計）。

### WI-B：/qa 強化為「獨立 + 對抗式 + 分層門檻 + 上游真做驗證」

## 0. 設計總綱與權威定位

本設計把 `/qa` 從「同一 agent 自問自答、確認式、八報告一刀切」升級為四個正交強化：(1) **審≠寫的對抗式立場**；(2) **分層門檻**（FINAL 厚 QA / 早期試寫薄 QA）；(3) **上游步驟真做驗證**（接住 S-01-03 式跳步+謊報寫檔）；(4) **多 lens 分歧**（取代同問三次）。

權威鏈現況（已讀）：
- `00_protocol/00_a_台詞生產協議.md` §3.9 = QA 模式「只檢查不大改 / 生命力保護 / 禁止事項」的根權威。狀態欄 DRAFT，但位於 `00_protocol/`，受 CLAUDE.md 規則 1-4 + D-050 子裁決 1「嚴禁修改任何 00_protocol/ 內檔」保護 → **00_protocol-tier，動它要拍板**。
- `00_protocol/00_k_台詞生產流程協議.md` v0.2 §5 = QA 階段流程權威（8 報告序列、qa_decision、phase_log shape）。同屬 `00_protocol/`，**動它要拍板**。
- `.claude/skills/qa/SKILL.md` v0.1 = runtime 實作層。**非 LOCKED、非 00_protocol、可直接改**。
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.5 / §3.x = 8 演算法權威（本輪未開讀全文，但 SKILL.md 已內嵌 guardrail，本設計只在 SKILL.md 層加 lens 拆分，不改 UD 演算法定義）。

設計原則：**儘量把強化落在 SKILL.md（可直接改層），只有「對抗式立場入協議」「上游真做驗證入流程協議」「分層門檻改 8 報告必跑硬規」三項可能觸動 00_protocol-tier，集中到 decisionNeeded 拍板。** 以下分四塊給出具體修改點 + 新增檢查條目，標清哪些是 SKILL-only、哪些等拍板。

---

## 1. 強化 (1)：審的 agent ≠ 寫的 agent + 對抗式立場

### 1.1 問題
現行 SKILL.md 整份語氣是「跑檢查 → 算 PASS/FAIL」，沒有任何「QA agent 必須與生成 agent 對立、預設找碴而非確認」的立場宣告。同一條對話裡寫完台詞順手 `/qa`，模型傾向確認自己剛寫的東西。

### 1.2 SKILL.md 具體修改點（可直接改層）

**新增 §「QA 立場宣告（Adversarial Stance）」**，插在現 `## 用途` 之後、`## 觸發語` 之前：

> ## QA 立場宣告（Adversarial Stance）
> 1. `/qa` 是**對抗式審查**，不是確認。QA agent 的預設立場是「這個版本有問題，我要找出來」，而非「證明它可以過」。
> 2. **審≠寫隔離原則**：執行 `/qa` 時，agent 必須以「我沒有寫過這份台詞、我是外部審查者」的視角運作。禁止引用「我剛才寫這句時的意圖」作為通過理由；只能引用台詞檔落地的字面內容 + 上游 LOCKED/FINAL 事實。
> 3. **冷啟動重讀**：Stage 1 必須從磁碟重新讀取目標台詞檔與所有上游來源，不得依賴同對話 context 中生成階段的記憶。若偵測到本次 `/qa` 與產出該台詞的 `/dialogue-write` 在同一 runtime context，必須在 Stage 1 元資訊印出 `審查隔離警示：本次 QA 與生成同源，已強制冷啟動重讀`。
> 4. **舉證責任反轉**：每份報告的 PASS 不是預設，必須由 agent 主動列出「我嘗試攻擊本項的 N 個切角 + 為何攻不破」才允許判 PASS。攻擊切角數低於該報告 lens 數（見多視角段）視為審查不完整 → 該報告 FAIL。

**新增 §「對抗式自檢清單」** 併入 Stage 3 彙整前，要求 agent 對自己的判定再質疑一次：

> 在印彙整摘要前，agent 必須自問並在 chat 印出回答：
> - 我有沒有因為「這是剛生成的版本」而放寬標準？
> - 我每一個 PASS 是否都列出了實際攻擊切角，而非「看起來沒問題」？
> - 我有沒有把 09_f / 09_d 的重大命中當成小問題輕放？

### 1.3 觸動 00_protocol？
「對抗式立場」是**新增語意**，00_a §3.9 現只說「只檢查不大改」，沒說「對抗」。若只落在 SKILL.md，協議與實作會語意分歧。**建議在 00_a §3.9 補一個原則句，屬 00_protocol-tier → 見 decisionNeeded D-B1。** 若拍板不動協議，則 SKILL.md 自帶宣告、不引用協議新句即可（fallback 可行）。

---

## 2. 強化 (2)：分層門檻（FINAL 厚 QA / 早期試寫薄 QA）

### 2.1 問題
現行 D-043 規定「8 份全跑、8 份全 PASS 才 PASS」，對 `DIALOGUE_TRIAL`（早期試寫，本來就要拋棄大半）和 `DIALOGUE_CONVERGED`（準 FINAL）一視同仁。早期試寫被迫跑厚 QA → 浪費 + 鼓勵 user 跳過 QA；而真正該嚴的 FINAL 前反而沒有比 converged 更厚的一關。

### 2.2 設計：三層 QA tier

| Tier | 觸發 pipeline_state / 旗標 | 報告集合 | 門檻 |
|---|---|---|---|
| **薄 QA（TRIAL_LIGHT）** | `DIALOGUE_TRIAL` 且 user 明示 `--tier=light` 或預設 trial 路徑 | 必跑 4 份：09_f 類型偏移 / 09_d 資訊控制 / 09_b 聲線 / 09_c 禁用詞（「踩線會污染後續判斷」的硬傷集合）| 4 份全 PASS → `QA_LIGHT_PASSED`（**新狀態，需拍板**或復用 `QA_PASSED`+標記）；不得直接升 FINAL |
| **標準 QA（STANDARD）** | `DIALOGUE_CONVERGED`（現行預設）| 8 份全跑（現行 D-043 集合不變）| 8 份全 PASS → `QA_PASSED` |
| **厚 QA（FINAL_GATE）** | `DIALOGUE_CONVERGED` 且 user 明示 `--tier=final` | 8 份 + 強制 09_i `--scope=arc` 起跳 + 強制「對抗式自檢清單」逐項書面 + 強制 lens 全展開（不得 collapse）| 8 份全 PASS 且無 ARBITRATE 懸置 → `QA_PASSED`（FINAL-ready 註記）|

預設仍是 STANDARD（向後相容，不破壞現有量產 chain）。薄/厚為 opt-in 旗標。

### 2.3 SKILL.md 具體修改點

- `## 觸發語` 的輸入鎖定表：在 `--scope` 之外新增可選 `--tier`，enum `light` / `standard` / `final`，預設依 pipeline_state 推導（TRIAL→light 提示、CONVERGED→standard）。
- 新增 §「QA tier 判定」插在 Stage 1 之前：依 pipeline_state + `--tier` 旗標決定報告集合與門檻，並在 Stage 1 元資訊印出本次 tier + 跑哪幾份 + 為何。
- `## qa_decision 計算規則` 改寫為**依 tier 的計算**：薄 QA 只算 4 份、標準/厚算 8 份。明確寫：薄 QA PASS **不可** mapping 到可升 FINAL 的狀態。
- Stage 5 next-step：薄 QA PASS 後印「這是早期試寫薄檢，升 FINAL 前必須回 DIALOGUE_CONVERGED 重跑標準或厚 QA」。

### 2.4 觸動 00_protocol？
分層門檻**直接牴觸** 00_k §5.4「8 份全 PASS 才 PASS」+ §8 禁止事項第 9 條「不得跳過 8 份任一份」+ §10.1 狀態機。薄 QA 只跑 4 份 = 形式上「跳過 4 份」。**這是協議級變更 → 見 decisionNeeded D-B2。** 若拍板不採分層，退路：保留 8 份全跑，但 SKILL.md 內把「薄/厚」改成「報告深度」而非「報告張數」（8 份都跑，trial 時每份簡化、final 時每份加嚴），這樣不破 D-043 張數硬規但仍有分層感（次佳方案，已寫入 D-B2 選項）。

---

## 3. 強化 (3)：上游步驟真做驗證（接住 S-01-03 跳步+謊報寫檔）

### 3.1 問題（核心教訓）
S-01-03 式無聲失敗：上游 skill（如 `/dialogue-write`）只在 chat 回了節拍/摘要，卻宣稱「已寫檔」，實際磁碟沒有檔案或檔案是空殼/狀態不符。下游 `/qa` 若只信任 phase_log 或 frontmatter 宣稱值，就會對一個根本沒真正落地的產物發 PASS。現行 SKILL.md「啟動前檢查」雖驗了「檔存在 + 狀態 >= DRAFT + pipeline_state 合法 + source_task 存在」，但**沒有交叉驗證「宣稱 vs 實體」是否一致**，也沒驗「上游該產的副產物真的都在」。

### 3.2 設計：新增 Stage 0「上游交付真實性驗證（Upstream Delivery Verification, UDV）」

插在現 Stage 1 之前，作為硬性 gate；任一項失敗 → `⏸ 條件未滿足` 拒絕，寫 phase_log `aborted`，不進 Stage 1。

新增檢查條目（具體可執行）：

1. **檔案實體存在且非空殼**：目標台詞檔不只 `存在`，還必須含實際台詞 body（非僅 frontmatter + 標題）。偵測「只有節拍/大綱/TODO 佔位、無實際對白行」→ 判為**疑似謊報寫檔**，拒絕並印「上游宣稱已寫檔但檔內無實際台詞 body」。
2. **宣稱 vs 實體交叉比對**：
   - phase_log 最近一筆 `/dialogue-write` 的 `dialogue_paths` / `status: completed` 宣稱的檔，**逐一驗證磁碟真的存在**。phase_log 說 completed 但檔不在 → 判**跳步+謊報**，拒絕並列出哪些宣稱檔缺失。
   - frontmatter `pipeline_state` 宣稱 `DIALOGUE_CONVERGED`，但 phase_log 找不到對應 `/dialogue-write --converge` completed 紀錄 → 判**狀態謊報**，拒絕。
3. **上游必要前置產物齊備**：`source_task` 指的任務包不只存在，還必須含 00_k §10.3 核心欄位（3/9/10/12/14/15）非空 + 任務包狀態 >= REVIEW。任務包是空殼或 DRAFT → 判**上游 gate 跳步**（`/dialogue-write` 不該在任務包未過 review gate 時產出），拒絕。
4. **依賴實體真達標**：`entities` / `depends_on` 列的每個 C-*/R-*-* 不只「檔存在」，狀態必須真的 >= REVIEW（現行第 9 項有驗狀態，本條強化為：若宣稱依賴與檔內實際狀態不符也判謊報）。
5. **無聲失敗指紋掃描**：掃目標台詞檔是否出現上游「假裝完成」的指紋——例如整檔只有 `（此處待補）` / `TODO` / 「以下為節拍」「beat 1/2/3」而無對白；或 body 行數異常少於任務包戲劇目的所需。命中 → 標記 `SUSPECTED_NO_OP_DELIVERY` 並拒絕進 QA。

### 3.3 SKILL.md 具體修改點
- 新增完整 §「Stage 0 — 上游交付真實性驗證（UDV）」含上述 5 條 checklist + 各自的拒絕文案（沿用 `⏸ 條件未滿足` 格式 What/Where/Why/下一步）。
- `## 啟動前檢查 / Input and dialogue checks` 第 2、4、8、9 項升級為「交叉驗證宣稱 vs 實體」措辭（不只存在性）。
- `## 流程` 開頭「Run exactly five stages」改為「Run Stage 0 gate then five stages」。
- phase_log abort entry 新增 `abort_reason` enum 值：`upstream_delivery_unverified`（謊報寫檔）/ `upstream_gate_skipped`（跳步）。

### 3.4 觸動 00_protocol？
UDV 的**檢查行為**屬 SKILL.md runtime，可直接加。但「下游 QA 必須驗證上游真做了步驟」這條**跨 skill 紀律**，最自然的家是 00_k（流程協議，本就規範 skill 串接 + 狀態機）。若要讓 `/scene-task`、`/dialogue-write` 也對齊「不得謊報寫檔 / 寫檔後自驗」，需在 00_k 補一節 → 00_protocol-tier。**見 decisionNeeded D-B3。** 退路：先只在 `/qa` SKILL.md 落地 UDV gate（防守端先補上），協議補強留待拍板。

---

## 4. 強化 (4)：多視角（lens）分歧，取代同問三次

### 4.1 問題
現行八報告各自獨立但「同質」——都是「讀台詞 → 比基準 → 報 PASS/FAIL」，本質上是對同一份台詞問了八次「你 OK 嗎」，且每份內部又是單一視角。模型容易八次都用同一套寬鬆判準。真正的對抗應是**不同立場的審查者互相不同意**，分歧本身就是訊號。

### 4.2 設計：每份報告內嵌 ≥2 個對立 lens，分歧即 escalate

為每份 QA 報告定義「對立 lens 對」，agent 必須分別以兩個立場各跑一次，**若兩 lens 結論不一致，不得取寬鬆者，必須 escalate 為該報告 NEEDS_REVIEW（在 /qa 中折疊為 FAIL）+ 列出分歧點交人類**。

| 報告 | lens A（嚴格/規則派） | lens B（生命力/創作派） | 分歧處理 |
|---|---|---|---|
| 09_f 類型偏移 | 嚴格類型守門：任何偏離基準即偏移 | 風格冒險辯護：這是刻意破格亮點 | 分歧 → 列為人類裁決（呼應 00_a §3.9.3 生命力保護）|
| 09_d 資訊控制 | 洩漏零容忍：任何疑似提前揭露即 FAIL | 敘事需要派：這是必要鋪陳非洩漏 | 分歧 → FAIL + 標「資訊邊界爭議」|
| 09_b 聲線 | OOC 嚴判：偏離聲線卡即 FAIL | 角色成長派：弧線階段允許聲線演化 | 分歧 → 標「聲線演化 vs OOC 爭議」交人類 |
| 09_h 對話張力 | 張力不足即弱場 | 留白派：克制是本場刻意設計 | 分歧 → NEEDS_REVIEW |
| 09_a AI 味 | 句型/抽象詞密度超標即 AI 味 | 風格核心派：這是作品語感非 AI 味（00_a §3.9.4 禁止把風格核心誤判 AI 味）| 分歧 → 強制保留 + 標人類確認 |
| 09_g 節奏 / 09_c 禁用詞 / 09_i 跨場 | 機械/數據派 | 例外辯護派（禁用詞的解禁時點 / 跨場是否真衝突）| 分歧 → 列證據交人類 |

### 4.3 SKILL.md 具體修改點
- 改寫 `## 8 報告詳細 algorithm` 表：每列「Algorithm summary」後追加 `Lens 對：A=<嚴格立場> / B=<生命力立場>；雙 lens 必跑；分歧 → escalate`。
- Stage 2 改寫：每份報告輸出必須含「lens A 結論 / lens B 結論 / 是否分歧 / 分歧時的 escalate 結果」四欄，而非單一 PASS/FAIL。
- `## qa_decision 計算規則` 補一條：**任一報告 lens 分歧未由人類裁決 → 該報告計為 FAIL（或 ARBITRATE_REQUIRED 懸置，依 tier）**，不得 agent 自行取寬鬆 lens 收斂。
- 報告模板輸出對接 00_a §3.9.3 既有的「可保留不規則亮點 / 不建議機械修正項」兩表——lens B 的辯護結果直接填這兩表（與既有協議無縫接）。

### 4.4 觸動 00_protocol？
多 lens 是 SKILL.md 內的**執行方法細化**，且 lens B 的「生命力辯護」與 09_e 人類裁決流程完全對齊 00_a §3.9.3 既有設計，**不新增協議概念**。判定：**可直接落 SKILL.md，不需拍板**（唯一前提是不改 8 演算法的 UD 定義，只在其上加 lens 拆分）。

---

## 5. 修改點彙總（按檔）

| 檔 | 層級 | 動作 | 需拍板？ |
|---|---|---|---|
| `.claude/skills/qa/SKILL.md` | runtime（可改）| 加 §對抗式立場 / Stage 0 UDV / §QA tier 判定 / lens 拆分 / qa_decision 改寫 / abort enum | 否（lens、UDV gate 行為、對抗自檢可直接做）；但 tier 報告張數、新狀態值受 D-B2 約束 |
| `00_protocol/00_a_台詞生產協議.md` §3.9 | 00_protocol-tier | 補「對抗式立場 + 審≠寫隔離」原則句 | **是 → D-B1** |
| `00_protocol/00_k_台詞生產流程協議.md` §5/§8/§10.1 | 00_protocol-tier | 分層門檻（薄/厚）+ 新 pipeline_state + 上游真做驗證跨-skill 紀律 | **是 → D-B2 + D-B3** |

---

## 6. 邊界情況

- **薄 QA 後想升 FINAL**：必須硬擋，回 CONVERGED 重跑（已寫入 §2.3）。
- **UDV 誤判合法的純破格節拍稿**：破格稿 `mode_tag: EXPERIMENTAL` 本就不該進標準 QA；UDV 第 5 條的無聲失敗指紋掃描須排除「user 明示這是節拍/大綱稿」的情形——加白名單：若 frontmatter `mode_tag` 為大綱類或 user 明示，改為 WARN 不拒絕。
- **lens 全分歧導致全 FAIL**：這是預期行為（分歧=訊號），但 Stage 3 須清楚告訴 user「FAIL 來自 lens 分歧而非硬傷」，避免 user 誤以為台詞爛。
- **同源冷啟動偵測無法 100% 可靠**：偵測不到同源時仍以對抗立場運作（立場宣告是預設，不依賴偵測）。
- **向後相容**：未帶 `--tier` 的既有調用一律走 STANDARD 8 份，行為與現行一致，不破壞量產中的 chain。

### WI-C：標準防線「執行→外部審→自動檢查→人工確認」寫成規則（審核迴圈協議 REVIEW_LOOP_PROTOCOL）

## 1. 設計目標與背景

repo 早已在「實踐」這套四層防線，但從未「寫成規則」：
- 外部審：11th master cycle 用 5 並行 read-only `Explore` 子代理跑 audit（AUDIT_2026Q2_REPORT §9.1）。
- 自動檢查：`scripts/check_paths.py` / `check_headers.py`（純讀取、退出碼 0/1/2）。
- 人工確認：master 在 Cowork 補加 cross-check + 拍板（§8.6「兩道 cross-check 後：5 採 + 1 deferred + 6 駁回」）。

問題是：這只存在於各輪 master 的肌肉記憶與散落的 audit report，沒有一份「實作者照著就能跑」的權威協議。一旦換手或平行開新 Cowork，防線層級就會漏跑（典型後果：M1-CRITICAL-01 Template 被污染、D-055 stale ref 擴散到 ~11 檔才被抓到）。

WI-C 要把這套防線固化為協議，明確四層各自「抓哪一類錯」「誰執行」「PASS/FAIL 判準」「漏跑後果」，並把它綁進每個 Batch 的生命週期。

## 2. 落地位置決策（推薦：新建 `_design/REVIEW_LOOP_PROTOCOL.md`）

三個候選位置：

| 方案 | 內容 | 評估 |
|---|---|---|
| A. 寫進 AGENTS.md / CLAUDE.md 新段 | 直接擴 root 兩檔 `## 修改流程` 後 | 兩檔需同步維護（D-048 既有負擔），且協議內容長（四層 × 判準 × Batch 綁定），塞進 root 會稀釋 root「精簡索引」定位 |
| B. 寫進 `00_protocol/`（如 00_m_審核迴圈協議.md） | 當成通用協議檔 | ✗ 不可行：`00_protocol/` 是「劇本生產」通用骨架、會 clone 進每個 Instance；本協議是「工具開發流程」治理規則，不該污染 Instance |
| **C. 新建 `_design/REVIEW_LOOP_PROTOCOL.md`（推薦）** | 完整協議本體放 `_design/`，AGENTS.md + CLAUDE.md 各加一段「指向本檔」的短 pointer | ✓ 對齊 repo 既有慣例（長 spec 放 `_design/`，root 只放精簡索引 + 指標，如 AGENTS.md 已用「按需讀取 `skill_registry_full.md`」模式）；DRAFT 狀態自建不動任何 LOCKED |

**推薦 C。** 理由：(1) 本協議治理的是「對本 repo 的 _design / 工具 / 協議檔修改」這層 meta 流程，天然屬 `_design/`；(2) `_design/` 的 .md 不會 clone 進 Instance，不污染劇本生產線；(3) root 兩檔只需加薄 pointer，維護點最小。

### 2.1 新檔 header（5 必填欄位，對齊 CLAUDE.md 文件頭格式）

```
狀態：DRAFT
版本：v0.1
最後更新：2026-06-02
適用範圍：本 repo（工具開發 / _design / 協議檔修改）的審核迴圈治理協議
優先級：高
```

無 YAML entities block（本檔非實體追蹤檔，比照 00_* 協議檔慣例可省略）。

## 3. `_design/REVIEW_LOOP_PROTOCOL.md` 完整段落結構

實作者照下列章節逐節寫即可。

### §0 文件定位
- 一句話：定義對本 repo（工具本體、_design spec、00_protocol 協議、scripts、skills）做任何 Batch 修改時，必跑的四層審核迴圈。
- 適用對象：所有 master 輪、所有平行 Cowork、所有 design agent / Codex / Claude Code session。
- 不適用：Instance repo 內的劇本生產（那走 /qa + 00_a 既有流程）。明確切割，避免與 D-043 /qa pipeline 混淆。

### §1 四層防線總表（協議核心）

| 層 | 名稱 | 抓哪一類錯 | 由誰執行 | 機制 | PASS 判準 | FAIL 動作 |
|---|---|---|---|---|---|---|
| L0 | 執行（Execute） | — | 主 agent（當前 session） | 依任務做出修改，產出「預計改檔清單 + 改後摘要」（AGENTS.md `## 修改流程` 既有要求） | 改檔清單與實際 git diff 一致 | 補齊清單再進 L1 |
| L1 | 外部審（External Review）| **內容錯**：邏輯矛盾、跨檔不一致、stale ref、設計判斷錯、漏處理 edge case、誤判既有設計 | **獨立 agent**（非 L0 那個 session）；典型 = read-only `Explore` 子代理 or 另開 Cowork | 拿 L0 的 diff + 任務描述，獨立複查；產出 finding list（嚴重度分級 CRITICAL/MAJOR/MINOR/INFO）| 0 個未處理 CRITICAL/MAJOR；或全 finding 有 cross-check 結論（採納/駁回/deferred）| 退回 L0 修，或進 L3 由人裁 |
| L2 | 自動檢查（Automated Check）| **機械/執行錯**：路徑打錯、漏檔、檔名舊式、header 缺欄、格式雜訊（NUL byte / BOM）、git 狀態異常 | 任何人/CI，跑腳本即可（零判斷） | `check_paths.py` + `check_headers.py` + `git status` + 改檔清點 | 兩腳本 exit code 0（無 ERROR）；git status 無非預期檔；清點數=改檔清單數 | exit≠0 → 必修到 0 才放行；不可「WARN 先放著」除非 L3 明示 |
| L3 | 人工確認（Human Sign-off）| **判斷**：finding 採不採、方案選哪個、LOCKED 是否該動、Batch 是否可收 | **人類 master**（不可由 agent 代簽） | 真的抽查（見 §3-§2 抽查規則）+ 對 L1 finding 做採納/駁回/deferred + 對 decisionNeeded 拍板 | master 明示「本 Batch 收」+ 抽查至少命中 §4 規定樣本 | 未抽查或抽查不合格 → Batch 不得標 completed |

關鍵原則寫進協議正文（粗體）：
- **L1 與 L0 必須是不同 agent context。** 同一 session 自審＝沒審（會帶入相同盲點）。這是 repo 既有實踐（Explore 子代理 / 另開 Cowork）的明文化。
- **L2 零判斷。** 腳本只報事實，severity 由腳本定，人不在 L2 做「這個 WARN 沒關係」的決定 — 那是 L3 的事。
- **L1 抓內容、L2 抓機械，兩者不可互相替代。** 自動檢查永遠抓不到「設計判斷錯」；外部審不該浪費在「路徑有沒有打錯」（那交給腳本）。

### §2 「人工關卡只有真的抽查才有效」提醒（協議必含、獨立成節）

正文明寫（這是 user 點名要的）：

> **L3 簽字的價值 100% 來自抽查的真實性。** 一個只會說「看起來沒問題、通過」的人工關卡，等於沒有關卡 — 它只是在 L1/L2 的結論上蓋橡皮圖章，把責任洗白卻不增加任何防護。rubber-stamp sign-off 比沒有 L3 更危險，因為它製造「已被人審過」的假安全感。

抽查最低要求（寫成可檢核清單）：
1. **至少實際打開讀過** L1 finding 中標 CRITICAL/MAJOR 的對應 diff 段落，不是只讀 L1 的摘要。
2. **至少抽 1 個 L1 判「無問題 / PASS」的檔親自複看** — 防 L1 漏報（false-negative 比 false-positive 危險）。
3. **至少復跑一次 L2 腳本親眼看 exit code** — 不接受「L0 說跑過了」的轉述。
4. 抽查結果（抽了哪幾項、命中什麼）要記進 Batch landing record（見 §3），不可只寫「已抽查通過」。

對齊既有事實：AUDIT §8.6 master 補加 cross-check 駁回了 6 條 raw finding（含 1 條 grep false-positive），正是 L3 抽查抓到 L1 過報的真實案例 — 協議用此當範例註腳。

### §3 套用到每個 Batch 的生命週期

把四層綁進 repo 既有的 "Batch" 工作單位（AUDIT report §2「落地 batch 紀錄」格式已是事實標準）。協議定義 Batch 五狀態機：

```
DRAFT_CHANGE → EXTERNAL_REVIEWED → AUTO_CHECKED → HUMAN_SIGNED → LANDED
   (L0)            (L1)                (L2)           (L3)         (commit)
```

規則：
- **狀態不可跳。** 一個 Batch 必須依序通過 L0→L1→L2→L3 才能 commit。允許 L1↔L0 回圈（審出問題退回修，重審）。
- **L2 在 L1 之後、L3 之前。** 理由：L1 改完內容後檔可能動到路徑/header，L2 要對「L1 修正後的最終 diff」跑，否則白跑。
- **每個 Batch 一條 landing record**，格式沿用 AUDIT report §2 既有欄位 + 補三欄：

| 欄位 | 內容 |
|---|---|
| Batch ID / 性質 | 既有 |
| 改檔清單 | L0 產出，L2 清點對照 |
| L1 reviewer | 哪個 agent context（子代理 runID / 另開 Cowork）+ finding 採納統計（N 採 / N 駁 / N deferred）|
| L2 結果 | 兩腳本 exit code + git status 摘要 |
| L3 抽查紀錄 | 抽了哪幾項、命中什麼（§2 第 4 點）|
| commit hash | LANDED 後由 user git log 自查（沿 AUDIT §2 既有慣例）|

- **規模豁免（避免協議淪為形式）：** 單檔 typo / header 補欄這類「純機械、零內容判斷」的 micro-batch，可 L1 降級為「L0 自述 + L2 腳本」，但 L3 抽查與 landing record 仍必跑。豁免條件寫死（不可主觀），防濫用。

### §4 與既有規則的接點（明寫 cross-ref，不重寫）
- L0 的「改前列清單 / 改後摘要」直接引 AGENTS.md `## 修改流程` + `## 修改後報告格式`，不重複定義。
- L1 finding 的錯誤呈現沿 ARCH §3.3.1 / TASKS §1.5 四件套（What/Where/Why/下一步）。
- 動 LOCKED / 00_protocol 的 Batch，L3 簽字前必須走 AGENTS.md 規則 4「先提變更理由與影響範圍」+ DECISIONS_LOG 開 D-NNN — 本協議不放寬該門檻，只把它列為 L3 的前置條件。
- 與 /qa 的切割：/qa 是劇本「內容品質」pipeline（D-043 八報告），本協議是工具「開發流程」治理；兩者層級不同、不互相觸發。

### §5 版本與維護
- 本檔 DRAFT 起步；待一輪 master 實跑驗證後升 REVIEW。
- 新增防線層或改判準 → 升版 + 在 DECISIONS_LOG 留 D-NNN。

## 4. AGENTS.md / CLAUDE.md 的薄 pointer（兩處同步）

在 AGENTS.md `## 修改流程` 之後、`---` 之前插入一小節；CLAUDE.md 對應位置插入內容對齊的中文段。內容（約 5 行）：

```
## 審核迴圈（四層防線）

對本 repo 的工具 / _design / 協議檔做任何 Batch 修改，必跑四層防線：
L0 執行 → L1 外部審（獨立 agent 查內容錯）→ L2 自動檢查（check_paths/check_headers/git status 查機械錯）→ L3 人工確認（master 真抽查後簽字）。
四層不可跳、L1 必須由與 L0 不同的 agent 執行、L3 簽字只有真抽查才有效。
完整判準、Batch 狀態機、landing record 格式見 `_design/REVIEW_LOOP_PROTOCOL.md`。
```

維護負擔：兩處 pointer 內容須對齊（沿 D-048 AGENTS/CLAUDE 同步規則）。pointer 是穩定指標、不含判準細節，故未來改協議多半不需動 root 兩檔。

## 5. 邊界情況處理（協議須涵蓋）
- **平行 Cowork 互審：** A 開的 Batch 由 B session 當 L1 reviewer，天然滿足「不同 context」。協議建議優先用此模式（比子代理更省 token、且 B 有完整 repo 視野）。
- **L1 reviewer 也是 AI 的局限：** 明寫「L1 是 AI 外部審，仍可能漏報；L3 的 §2 第 2 點抽查（抽 PASS 檔複看）正是兜底 L1 AI 漏報」。
- **L2 腳本 scope 限制：** 現有 check_paths 只掃 ACTIVE_DIRS + README/AGENTS（不含 CLAUDE.md / .claude/skills/）。協議須註明此盲區，並把「scripts 涵蓋 CLAUDE.md 與 skills」列為已知 backlog（建議推 NEW_REQ，不在本 WI 實作）。
- **deferred finding：** L1 審出但 L3 判「本 Batch 不處理」的，必須進 POST_LOCK_PENDING / NEW_REQ backlog，不可悄悄丟棄（沿 AUDIT §8.6「1 deferred 進 NEW_REQ」既有實踐）。

### 本批測試輪計畫（Batch 1 = Meta-pattern B `/create-character` 品質提升 pipeline：F7 source 讀取規範 + F9 個性拆解 + F11 既有劇本萃取 + F12 Source Coverage + F13 既有台詞聲線基準 + speaker alias；外加 QA 強化抓「跳步只回摘要」+ check_paths/check_headers 污染回歸）。本輪只定「過關標準」，供實作完成後執行測試用。

中文設計說明如下。本計畫只定義「實作完成後怎麼測 Batch 1」的可執行測試協議與 PASS/FAIL 判準；本輪不實作、不寫任何 production 檔。

---

# 0. 前置事實（讀現況後確認）

讀過的檔：
- `_sandbox/TEST/`：兩張聲線卡（`03_characters/main/瑟琳_聲線卡.md`、`清道夫_聲線卡.md`）、4 場台詞（`08_dialogue_outputs/S-01-01..04_台詞.md`）、2 份 QA（`09_a_AI味QA.md`、`09_b_聲線一致性QA.md`）、3 份 source 素材（`女_1_瑟琳_人設v_0_1.md`、`男主角_清道夫_人設v_0_1.md` 等）。
- `_design/M4_USER_TEST_REPORT.md`（F1-F19；Batch 1 = Meta-pattern B = F9/F10/F11/F12/F13，加 F7 source dir convention 為其前置）。
- `.claude/skills/create-character/SKILL.md` v0.4（**現況**：input 只列「Long-form character material」；Split Rules 只 8 個技術 voice section；**沒有** F7 source 讀取、F11 既有劇本萃取、F13 speaker alias / 既有台詞讀取、F9 個性拆解段、F12 Source Coverage 段）。
- `scripts/check_paths.py`、`scripts/check_headers.py`、`scripts/parse_frontmatter.py`。

**關鍵基線事實（測試判準會用到）：**

1. **TEST baseline 聲線卡已是「目標增強後輸出」**：`瑟琳_聲線卡.md` 已含 §2 表層性格 / §3 內在性格 / §8 壓力下語言變形（個性拆解 = F9）、開頭 `> 來源：_sandbox/TEST/女_1_瑟琳_人設v_0_1.md`（source coverage 雛形 = F12/F7）、[INFERENCE] 標記、稱呼硬規則。`清道夫_聲線卡.md` 含 §8「§5.5 既有台詞語氣範例的處理說明」＋尾段「源人設檔路徑」＋「人設檔未提供成句台詞→需另查既有劇本」註記（= F13 既有台詞讀取意識的雛形）。→ 這代表 baseline 是「人工已照新規則手動補出來的樣子」，測試要驗的是**重跑 skill 後 agent 能不能自己產出同等結構**，而非跟一個低品質 baseline 比。
2. **check 腳本 root = production repo root**（由 script 位置推算，非 cwd）。`check_headers.py` 只掃固定 `TEMPLATE_PATTERNS` allowlist（production 頂層 00_~09_、_design），**不掃 `_sandbox/`**。`check_paths.py` 會 walk 全 repo，`IGNORE_DIR_NAMES` = {.git, archive, node_modules, __pycache__, .venv, venv, scripts}，**不含 `_sandbox`** → check_paths **會**下探 `_sandbox/`，這正是 F7 source 污染向量。
3. **Windows console cp950 會在遇到 emoji（✅ 等）時 crash**（實測 check_headers 印 INFO 時 UnicodeEncodeError）。測試執行必須先 `set PYTHONIOENCODING=utf-8`（或 `$env:PYTHONIOENCODING='utf-8'`）再跑，否則 crash 屬環境問題非 FAIL。
4. **量產 baseline 數字**（M4 report §2）：check_paths.py = 247 ERROR（NEW_REQ_9 既有 debt，hard-limit accept）；check_headers.py = 0 ERROR / 57 WARN。本計畫所有「無新增 ERROR」判準都以此為基準線 diff。

---

# 1. 測試環境準備（共通前置；不算測試項）

> 目的：確保測試可重現、baseline 數字鎖死、不污染 production。

PRE-1. **隔離 fixture**：把 `_sandbox/TEST/` 完整複製到一次性測試工作區 `_sandbox/TEST_RUN_<ts>/`（或 git stash 保護），所有重跑寫檔都打到複本。理由：避免覆寫 baseline，留 baseline 供 diff。
PRE-2. **鎖 baseline 數字**：實作前先各跑一次（`PYTHONIOENCODING=utf-8`）：
   - `python scripts/check_paths.py > baseline_paths_BEFORE.txt 2>&1; echo exit=$?`
   - `python scripts/check_headers.py > baseline_headers_BEFORE.txt 2>&1; echo exit=$?`
   記下 ERROR/WARN 總數（預期 paths=247 ERROR、headers=0 ERROR/57 WARN，若實際不同以實測為新 baseline）。
PRE-3. **凍結 source 素材原樣**：保留 `女_1_瑟琳_人設v_0_1.md`、`男主角_清道夫_人設v_0_1.md`、`完整劇本V3.md`（含既有台詞，供 F11/F13 萃取）於測試工作區，記其路徑（F7 路徑檢查用）。
PRE-4. **確認 skill 已實作**：grep `.claude/skills/create-character/SKILL.md`，確認已含 F7/F9/F11/F12/F13 對應新段（input scope 提既有劇本/docx；Split Rules 新增「個性拆解」「Source Coverage / Downstream Hooks」「既有劇本台詞聲線基準」「既有劇本聲線使用規則」；Stage 1/2 提 speaker alias）。若未實作 → 整個 Batch 1 測試 BLOCKED，不可用舊 SKILL.md 假測。

---

# 2. 測試項 T1 — 重跑 /create-character 瑟琳 + 清道夫（驗證新規則自吸收既有劇本）

## T1 執行步驟
1. 在測試工作區對 `C-瑟琳`、`C-清道夫` 各跑一次 `/create-character`（可一次帶兩名走 breadth-first）。
2. **input 只提供 source 素材路徑**，不手動貼增強內容：明確告訴 agent「素材在 `女_1_瑟琳_人設v_0_1.md`、`男主角_清道夫_人設v_0_1.md`，既有劇本在 `完整劇本V3.md`，自己去讀」。**不替它補 F9/F12/F13 內容**——測的就是它會不會自己讀、自己長出新段。
3. 走完 5 階段，Stage 3 收斂預覽通過後寫檔到測試工作區。
4. 保存：新生成的兩張聲線卡 + 該 run 的完整 chat transcript（用於 F7 路徑、speaker alias、跳步檢查）。

## T1 PASS/FAIL 判準（逐條；任一「必過項」FAIL 即 T1 FAIL）

**T1-A（必過）4 個新段全到位**：新生成聲線卡必須含以下 4 類新段（對應 Batch 1 四個 finding；段名可微調但語意需到位）：
   - F9 個性拆解：表層性格 + 內在性格 + 自尊/恐懼來源 + 情緒遮掩 + 壓力下變形（對照 baseline 瑟琳卡 §2/§3/§8）。
   - F12 Source Coverage / Downstream Hooks：明列「已吸收進聲線的 source 資訊」+「交給 /create-relationship / /create-outline / /scene-task 的 hooks」+「不應直接當台詞用的 source 資訊」。
   - F13 既有劇本台詞聲線基準：從 `完整劇本V3.md` 抽出該角色既有台詞，歸納聲線特徵（對照 baseline 清道夫卡 §8 的歸納形態）。
   - F13 既有劇本聲線使用規則：明寫哪些可直接複用、哪些不可。
   PASS = 兩張卡都齊 4 類；FAIL = 任一張缺任一類，或只有空標題無實質內容。

**T1-B（必過）真的讀了 source（F7 路徑證據）**：transcript 中必須出現 agent **實際讀取 source 檔的證據**——(a) 引用 source 檔的具體原句/段落編號（如「人設 §5.3 三句反差」「§2.2 固定稱呼傭兵先生」），且 (b) 聲線卡內出現只可能來自 source 而非 prompt 的細節（瑟琳「傭兵先生」硬稱呼、清道夫「黑翼防衛」「成本/交差邏輯」「§5.5 未提供成句台詞」）。
   - PASS = 兩角色都有具體 source 引用 + source-only 細節落卡。
   - FAIL = agent 憑空編角色設定、或只覆述 prompt 名字而無 source 內容、或聲稱讀了但拿不出任何 source 專屬細節（= 幻覺/跳讀）。

**T1-C（必過）F13 既有台詞被真讀**：清道夫卡必須正確反映 source 的關鍵事實——「人設檔 §5.5/§15 明示不提供成句台詞範例，需另查既有劇本」，且若 `完整劇本V3.md` 有清道夫台詞，需抽出實際句子歸納（不是只寫「應另查」就交差）。
   - PASS = 既有台詞基準段有來自 `完整劇本V3.md` 的實際台詞依據，或在劇本確無該角色台詞時明確記錄「既有劇本無 X 角色台詞」並標 source 已查。
   - FAIL = 段落空殼、或宣稱已讀但無任何台詞引用、或把人設檔當台詞範例誤用。

**T1-D（必過）speaker alias matching（若 source 用代號）**：若 `完整劇本V3.md` 用 MainGirlA/B/C 或英文代號，transcript 需顯示 agent 做了 alias 對應（MainGirlA=瑟琳 等）。若 source 直接用中文名則本項 N/A（記為 N/A 不算 FAIL）。

**T1-E（必過）寫檔邊界守 D-050**：只寫 `03_characters/`（含新段）+ phase_log；**未**寫 `00_protocol/`、`08_dialogue_outputs/`、`04_*`、source 檔本身。
   - FAIL = 任何 D-050 越界寫入，或回頭改寫了 source 素材檔。

**T1-F（必過）INFERENCE/TODO 紀律**：source 未明寫而由 agent 推導的內容須標 `[INFERENCE]` 或 `<!-- INFERENCE -->`（對照 baseline 瑟琳卡 line 9 + line 92）。
   - FAIL = 把推導當 canon 直接寫死、無任何 INFERENCE 標記但卡內明顯有超出 source 的設定。

**T1-G（品質參考，非阻斷）vs baseline 對比**：新卡結構完整度 ≥ baseline 卡（baseline 已是人工增強版）。記為「達到/接近/低於 baseline」三檔，低於 baseline 不直接判 FAIL 但需在報告標註 regression 風險。

---

# 3. 測試項 T2 — 重生一場台詞 + 跑強化後 /qa，與 baseline 逐項 diff

## T2 執行步驟
1. 選 **S-01-02**（baseline AI 味最重的一場：瑟琳「金句產生器」、清道夫散文腔、簡繁亂碼 `嘴�里`），用重跑後的新聲線卡重生該場台詞（走 /scene-task → /dialogue-write）。
2. 對重生台詞跑強化後 `/qa`（8 報告必跑；至少逐項比對 09_a AI味 + 09_b 聲線一致性）。
3. 與 baseline `09_a_AI味QA.md` §2、`09_b_聲線一致性QA.md` S-01-02 段逐項 diff。

## T2 PASS/FAIL 判準

**T2-A（必過）交付物乾淨**：重生台詞 .md 只含中文 header + 場景描述 + 台詞行，**無** agent meta-narration（無「I'll write」「say the word」「節拍對照」「聲線守則落實」英文工作宣言）、無 ```md 包裹、無亂碼/簡繁混用。
   - PASS = 0 個 meta-narration 片段、0 亂碼。
   - FAIL = 出現任一 baseline §0 點名的污染類型（這是 baseline 四場全中的問題，重生後不該再犯）。

**T2-B（必過）AI 味改善（逐項 diff）**：對照 baseline 09_a §2 點名的 S-01-02 具體問題句，逐句檢查新台詞是否已改善：
   - 瑟琳「路也會留下以前的事」「能走到這裡就已經很厲害了」主題宣言 → 新版應改為具體動作/孩子氣反應，不再由角色親口總結主題。
   - 清道夫「東西爛得慢」「痕還在」散文腔金句 → 削刻意對仗。
   - PASS = baseline 點名問題句 ≥ 多數已消除或弱化，且新版整體判定由 CONDITIONAL → PASS（或 AI 味問題句數明顯下降）。
   - FAIL = 同類問題句原樣重現、或新增等量新 AI 味問題（淨無改善）。

**T2-C（必過）聲線一致性不退步**：對照 baseline 09_b，去名測試仍 PASS、稱呼零漂移（瑟琳 100% 「傭兵先生」、清道夫不糾正）、結巴密度對得上關係階段、無踩兩卡紅線（無「我會保護妳」救世腔、無人格羞辱、瑟琳不沾莉娜嗆辣/諾拉冷漠）。
   - PASS = 聲線一致性 ≥ baseline（仍 PASS、無新混同）。
   - FAIL = 出現稱呼漂移、紅線、或去名測試不成立。

**T2-D（品質參考）F13 連動效果**：新聲線卡含「既有劇本台詞聲線基準」後，重生台詞是否更貼既有劇本語感（散文腔金句衝動下降）。記敘述性觀察，非硬阻斷。

> 註：T2 的「進步」判準錨定在 **baseline QA 報告已點名的具體問題清單**（09_a §5 七條 + 09_b 建議），逐條標「已修/部分/未修/惡化」，避免主觀。

---

# 4. 測試項 T3 — 故意埋「agent 跳步只回摘要」失敗，驗證強化後 QA 會抓

## 背景
baseline S-01-03 正是真實發生過的此類失敗：「整場沒有台詞，只有『台詞檔已產出：<path>』+ 節拍對照摘要，實際台詞缺席」（09_a §3、09_b S-01-03 段）。本項驗證強化後 /qa 是否**穩定**抓到這種「跳步只回摘要」交付物。

## T3 執行步驟（注入 3 個變體 fixture）
構造 3 個故意失敗的台詞 fixture（不走正常生成，直接造缺陷檔）：
- **T3-fix-1（純摘要）**：仿 baseline S-01-03——檔內只有「台詞檔已產出：<path>」+ 節拍對照摘要 + 聲線守則自述，**零句實際台詞**。
- **T3-fix-2（meta-narration 夾雜）**：仿 S-01-01/02/04——有台詞但夾「I'll write the dialogue file...」「say the word and I'll write it」英文工作宣言 + ```md 包裹。
- **T3-fix-3（半摘要）**：前半有 2-3 句台詞，後半用「（其餘節拍照聲線守則處理，略）」代替應有台詞。
對 3 個 fixture 各跑強化後 `/qa`。

## T3 PASS/FAIL 判準

**T3-A（必過，核心）/qa 必須對 3 個 fixture 全部判 FAIL/CONDITIONAL 並點名缺陷**：
   - T3-fix-1：必須報「交付物缺台詞正文/無法逐句 QA」（對照 baseline 09_a 確實抓到了——強化後不得反而漏掉）。
   - T3-fix-2：必須報「交付物混入 agent meta-narration，須刪除」。
   - T3-fix-3：必須報「台詞不完整/以摘要代替正文」。
   - PASS = 3/3 都被點名為阻斷級或最高優先問題。
   - **FAIL = 任一 fixture 被 /qa 判 PASS、或漏報缺陷、或只報次要問題而沒抓到「正文缺席/摘要代替」這個主問題**（這是本項唯一真正要證明的能力）。

**T3-B（必過）不誤殺**：對一份**乾淨完整**的對照 fixture（T2 重生的合格台詞或 baseline 中合格場），強化後 /qa 不得誤報「跳步/摘要」缺陷。
   - PASS = 乾淨檔不被誤判為摘要交付。
   - FAIL = 出現 false positive（把正常台詞當成摘要/跳步）。

**T3-C（參考）抓取定位品質**：/qa 是否明確指出是哪一場/哪一段缺正文（定位精度），記敘述觀察。

> 設計理由：baseline QA 已能抓 S-01-03（純摘要），所以 T3 的真正風險是「強化後 /qa 改了流程後反而漏抓」或「只抓表面 AI 味卻放過交付物缺席」。T3-A 鎖死「主問題必須是正文缺席而非次要 AI 味」。

---

# 5. 測試項 T4 — check_paths / check_headers 污染回歸（source 檔不再污染、無新增 ERROR）

## 背景
F7 的核心痛點：source 素材 `.md`（如 `女_1_瑟琳_人設v_0_1.md`）放進 instance 後，缺 5 欄 header 或含 old-style 路徑時被 parser/header/paths 流程當正式追蹤文件掃描而報錯。`check_paths.py` 會下探 `_sandbox/`（IGNORE_DIR_NAMES 不含 _sandbox），是污染向量。F7 patch 後預期有 source dir convention（如 `03_characters/source/` 或全域 `_source_materials/`）+ parser 排除規則。

## T4 執行步驟
1. 在測試工作區，把 source 素材依 **F7 patch 後規範**放置（測 patch 是否真讓 source 不污染）。
2. `PYTHONIOENCODING=utf-8` 下重跑：
   - `python scripts/check_paths.py > paths_AFTER.txt 2>&1; echo exit=$?`
   - `python scripts/check_headers.py > headers_AFTER.txt 2>&1; echo exit=$?`
3. 與 PRE-2 的 BEFORE 檔逐行 diff。

## T4 PASS/FAIL 判準

**T4-A（必過）無新增 ERROR**：`check_paths.py` ERROR 數 ≤ baseline（247；NEW_REQ_9 既有 debt 不算新增），`check_headers.py` ERROR 數 = 0。
   - PASS = paths ERROR 不超過 baseline、headers ERROR = 0。
   - FAIL = 出現任何**新的** ERROR（diff BEFORE→AFTER 出現新行），尤其是指向 source 素材檔或新生成聲線卡的 ERROR。

**T4-B（必過）source 檔不再被當追蹤文件污染**：AFTER 輸出中，source 素材檔（`女_1_瑟琳_人設v_0_1.md` 等）**不應**出現 ERROR/WARN（F7 patch 後應被 parser 排除，或被放到排除目錄）。
   - PASS = 0 個 source 素材檔相關 issue。
   - FAIL = source 檔仍被掃描報錯（代表 F7 patch 未真正解決污染）。

**T4-C（必過）新生成聲線卡 header 合規**：T1 重生的兩張卡若落在 production allowlist 掃描範圍（`03_characters/main/*.md`），check_headers 須對其 0 ERROR（5 欄 header 完整）。
   - FAIL = 新卡缺 header 欄位、或 header 位置錯（如被 push 到標題之後導致 parser 抓不到——注意 baseline 瑟琳 source 檔 header 在標題後，新卡須避免此 pattern）。

**T4-D（環境前置，非 FAIL 項）**：若未設 PYTHONIOENCODING 導致 cp950 emoji crash，須先修環境再跑；此 crash 不計入 ERROR 判準（屬已知 Windows console 限制，對應 F4/工具層議題，非本 batch scope）。

---

# 6. 整體 Batch 1 過關判定（roll-up）

| 測試項 | 必過判準 | Batch 1 PASS 條件 |
|---|---|---|
| T1 自吸收 source | T1-A~T1-F 全過 | 全部必過項 PASS |
| T2 重生+QA diff | T2-A~T2-C 全過 | 全部必過項 PASS |
| T3 跳步摘要抓取 | T3-A + T3-B 全過 | 全部必過項 PASS |
| T4 污染回歸 | T4-A~T4-C 全過 | 全部必過項 PASS |

- **Batch 1 PASS** = T1/T2/T3/T4 所有「必過」判準全 PASS；「品質參考」項僅記錄不阻斷。
- **Batch 1 CONDITIONAL** = 必過項全過但 ≥1 個品質參考項標 regression 風險（需人工複核後放行）。
- **Batch 1 FAIL** = 任一「必過」判準 FAIL；報告須逐項列哪個 finding（F7/F9/F11/F12/F13）對應的能力未達標，回退給實作。

---

# 7. 測試產出物（測試執行後須留存）
- `baseline_*_BEFORE.txt` / `*_AFTER.txt` + diff（T4 證據）。
- T1 重跑兩張新聲線卡 + 完整 chat transcript（T1-B/T1-D/T3 證據）。
- T2 重生台詞 + 新 8 份 QA 報告 + 對 baseline 09_a/09_b 的逐條「已修/部分/未修/惡化」對照表。
- T3 三個失敗 fixture + 各自 /qa 輸出 + 判定表。
- 一份 Batch 1 測試結論（PASS/CONDITIONAL/FAIL + 逐 finding 對應）。

---

# 8. 風險與注意（測試執行者須知）
- baseline 聲線卡已是「目標增強版」（人工手補），故 T1 是「能否自動重現」而非「跟爛 baseline 比進步」；勿誤把 baseline 當低標。
- T2「進步」必須錨定 baseline QA **已點名的具體問題句**逐條判定，避免主觀「感覺有變好」。
- T3 真正風險是強化後 /qa「改流程後漏抓正文缺席」或「只抓 AI 味放過交付物缺席」，故 T3-A 鎖「主問題必須是正文缺席」。
- 所有 check 腳本須 `PYTHONIOENCODING=utf-8`，否則 emoji crash 屬環境噪音非 FAIL。
- 全程在 `_sandbox/TEST_RUN_<ts>/` 複本操作，勿覆寫 baseline、勿寫 production `00_protocol/`、勿改 source 素材檔。