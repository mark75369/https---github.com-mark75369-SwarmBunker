狀態：DRAFT
版本：v1.0（Wave2 設計修正 — 對抗審 gate 後重驗活檔行號 + 套用 B1/B2/M1-M7 已核實 fix-list；本檔取代 `_WAVE2_設計總覽.md` 中被 gate 標錯的部分）
最後更新：2026-06-02
適用範圍：Wave2 /create-character 設計修正實作 spec（F9/F11/F12/F13 = NEW_REQ_33/35/36/37 落地）；DECISIONS_LOG / POST_LOCK / M4 / UD / 00_f / SPEC / registry 同步
優先級：高

# Wave2 FINAL 實作 spec（修正後）

> **本檔取代 `_WAVE2_設計總覽.md` 中被 gate 標錯的部分。** 凡與本檔衝突，以本檔為準。
> 本檔所有行號為 Wave2 設計修正 agent **親自對活檔重驗後** 的正確行號（重驗日 2026-06-02）。
> 適用對象：F9 / F11 / F12 / F13（= NEW_REQ_33 / 35 / 36 / 37）= M4 Batch B2 create-character chain。

---

## 0. 重驗摘要（被 gate 標錯處 → 已更正）

| gate 標錯項 | 原（錯）陳述 | 重驗後正確值 | fix |
|---|---|---|---|
| SPEC「9議題」行號 | 「SPEC.md line 7323『9議題』」 | SPEC.md **僅 1613 行，無 7323**；SPEC 的「9議題」在 **SPEC.md:942**；line 7323 是 **UD** 的 | B1 |
| 9議題 cross-ref 處數 | 單一處 | **兩處**：SPEC.md:942 + UD:7323，各自獨立同步 | B1 |
| 00_f §10 baseline | §10 只到 §10.8 / §10.9 | §10 **延伸到 §10.11**（§10.9=line 290、§10.10=line 304、§10.11=line 312）| M1 |
| 新 script 編號位置 | 「§10.8 後 §10.9 前 或 §10.10-§10.11 之間」（矛盾雙選項）| **純 append 於 §10.11 之後，編號 §10.13/§10.14（gap-jump 跳 §10.12）** | M1 |
| 同步面數 | 11 點 | **12 點**（補第 4 同步面：SKILL.md:395-427 輸出骨架）| M2 |
| D-NNN 性質 | F9/F11/F12/F13「不需 D-NNN」 | **升格 D-056/D-057 必拍**（Wave2 落地需動 LOCKED UD + registry）| B2 |
| F17+F18 / F19 候選號 | D-060 / D-061 | **D-066 / D-067**（D-060~D-065 已被 QA work item + WI-C 佔，二次撞號）| B2 |
| D-047 描述計數 | core 36（10+8+6+6+6）| 00_f 8→10 後改 **38（10+10+6+6+6）** | M3 |
| ≥100 契約來源行號 | issue_type_registry line 84-85 | **line 328**（SKILL line 337 引用不變）| M4 |
| 措辭 | 「0 supersede / 純 append」 | 新 script + registry id 9/10 = 純 append；但 count/ordinal/標題 = **就地計數修正**，須列入 D-056 授權範圍 | M5 |

---

## 1. §B / §C 骨架 + F11 input / speaker-alias 機制（沿用既有設計，不變）

> 本節 input/output 機制沿用 M4 §3.11/§3.13 + NEW_REQ_35/37 既有提議，**不變更語意**；僅在此彙整供 Wave2 落地引用。

### 1.1 §B 既有劇本台詞聲線基準（F13 / NEW_REQ_37 output 層）

寫入 SKILL.md「聲線卡固定段骨架」段（活檔 line 395-427）作 §B append，並對齊 §A/§D 既有 anchor-title pattern：

```md
## §B 既有劇本台詞聲線基準
> 本段保存「從既有劇本台詞萃取」的角色聲線基準，供 /dialogue-write 對齊文筆。
> D-050：本段只**讀** `08_dialogue_outputs/` + 既有劇本 source（docx/.txt/.csv/.json），**永不寫** 08。
> cross-ref STYLE_ANCHOR W-style（D-055）：voice card §B 繼承 W-style 作品級文風指紋 + 加 character-specific 聲線特徵。

1. **speaker alias 對照**：<MainGirlA=瑟琳 / MainGirlB=莉娜 / MainGirlC=諾拉 等別名 → C-<name> 對照表>
2. **8-12 句代表台詞**（覆蓋 8 場景類型）：初登場 / 危機反應 / 任務前準備 / 戰後反應 / 日常互動 / 被肯定被吐槽 / 關係推進 / 中後期成長語氣
3. **萃取出的聲線規律**：<由代表台詞歸納，例：罵人綁定具體技術問題、不宜搶其他角色定位>
4. **與人設 source 的差異**：<只讀人設 vs 補讀劇本的聲線落差紀錄>
```

### 1.2 §C 既有劇本聲線使用規則（F13 / NEW_REQ_37 output 層強化）

```md
## §C 既有劇本聲線使用規則
1. **可直接複用的聲線特徵**：<哪些已驗證可直接帶進新台詞>
2. **需調整後使用**：<舊台詞中過時 / 偏移 / 與當前 canon 衝突者>
3. **不可直接當台詞使用的 source**：<僅供理解，不入正式台詞；與 §D 第 5 子段呼應不重複>
```

### 1.3 F11 input / speaker-alias 機制（NEW_REQ_35；input 層，沿用不變）

- Stage 1：agent 確認 user 是否有既有劇本台詞 + 提供 speaker alias 對照。
- Stage 2：讀 `08_dialogue_outputs/` + docx / .txt / .csv / .json（**只讀不寫**）；docx 無法解析時印既有 WARN（沿用 SKILL.md line 151 規範），不靜默跳過。
- 篩選標準：8-12 句覆蓋上述 8 場景類型。
- **D-050 邊界 clarification（讀 vs 寫）**：08_dialogue_outputs/ 維持「不寫」清單（SKILL.md line 391 / D-050 子裁決 2），但 Wave2 明示「**沒禁讀**」——讀取不擴大寫檔範圍，寫檔仍嚴格限 `03_characters/`。此 clarification 列入 D-057 授權範圍（見 §4）。
- **F11 + F13 必同輪實作**（input + output 一氣呵成；單做 F11 沒落地處、單做 F13 沒讀進來無法寫基準）。

---

## 2. 【12 點同步 checklist】（每點標重驗後正確行號）

> 計數口徑統一寫死：**`9 = 8 真議題 + 1 拆分（§10.9 確認）`；`11 = 8 + 新 2（§10.13 個性拆解 / §10.14 source coverage）+ 1 拆分`**。
> 拆分規則確認（UD 序號 9 / §10.9）屬 agent-side mechanic 不是真 user-facing 技術議題；故「真議題」由 8 → 10。

| # | 同步面 | 活檔 + 重驗行號 | 動作 | 性質（M5）|
|---|---|---|---|---|
| 1 | SKILL.md Stage 2 core issue 表 | `create-character/SKILL.md` line 164-173（id 1-8 表）| append id 9（個性拆解）+ id 10（source coverage）兩 row | 純 append |
| 2 | SKILL.md §Split Rules 表 | line 218-229（§10.9 對照表）| append 兩 row：id 9→§A 個性拆解、id 10→§D source coverage 寫入 voice card | 純 append（§A/§D 既有 line 228-229 已存在，補對 id 9/10 的 registry 映射）|
| 3 | SKILL.md registry 拒絕條件 | line 337（user extension id < 100 reject）| **行號不變**；只確認 id 9/10 屬 core（1-99 範圍）不觸發 ≥100 規則 | 不改（確認）|
| 4 | **SKILL.md 輸出骨架（M2 第 4 同步面）** | line 395-427『聲線卡固定段骨架（§A/§D）』；line 397 明寫「Stage 3 preview / Stage 4 write / output structure 須一致」| 在此 append §B（line 1.1）+ §C（line 1.2）md 骨架；維持 §A→§B→§C→§D 順序與 Stage 3/4 一致 | 純 append |
| 5 | 00_f §10 新 script | `00_f_角色創建協議.md` §10 baseline 到 §10.11（line 312）| append **§10.13 個性拆解 / §10.14 source coverage**（gap-jump 跳 §10.12）於 §10.11 之後 | 純 append |
| 6 | 00_f §4.1 議題順序預設表 | line 105-114（8 row 表）| append 議題 9（個性拆解）+ 議題 10（source coverage）兩 row | 純 append |
| 7 | 00_f §4.1 計數句 | line 103『00_f core 共 **8 個** user-facing 議題（registry 對應 id 1-8）』| 就地改『**10 個** user-facing 議題（registry 對應 id 1-10）』 | 就地計數修正（D-056）|
| 8 | 00_f §1 處理清單 | line 15-25（本協議處理 8 項 + 拆分）| append「個性拆解」「source coverage / 下游 hooks」兩條 | 純 append |
| 9 | UD §1.2.2 新 script | `UPSTREAM_DOWNSTREAM_SPEC.md` create-character 區段最後 script = §10.9（拆分表 line 969-979；frontmatter 規範 line 991-995）| append **§10.13 / §10.14**（同 00_f 對齊，gap-jump 跳 §10.12）於 §10.9 之後（line 995 之後、§1.2.3 line 997 之前）| 純 append |
| 10 | UD §1.2.1 議題清單表 | line 735-744（9 row：id 1-8 + 9 拆分規則確認）| append 議題 10（個性拆解）+ 議題 11（source coverage）兩 row；並就地改 line 744 序號區既有「9」計數語 | append + 就地計數修正（D-056）|
| 11 | UD §1.2.2 標題「9項議題」 | line 773『### 1.2.2 區段 10：專屬區段 — **9 項議題** agent 提問腳本』；body line 769『**9 個議題**中…』；UX line 1005『N 個角色 × **9 個議題**』 | 就地改三處「9」→「11」 | 就地計數修正（D-056）|
| 12 | 兩處「9議題」cross-ref（B1 拆兩目標）| (a) `SPEC.md:942`『\| 00_f 角色（**9議題**） \| UD §1.2 \|』；(b) `UD:7323`『\| §10.2 00_f 專屬區段 \| §1.2 \| **9議題** agent 提問腳本 \|』| 各自就地改「9議題」→「11議題」 | 就地計數修正（D-056；不改議題語意）|

**registry 同步（不入 12 點同步面，但屬必動 LOCKED template）：**
- `issue_type_registry.template.yaml` `core.00_f_character` append id=9 + id=10 兩 entry（6 欄：id/name/required_level/locked/question_summary/protocol_ref）。屬純 append；**user 自訂 ID 從 100 起跳契約在 line 328**（非 line 84-85）；SKILL line 337 引用不變。

---

## 3. UD / 00_f 各自的 append 點（M1 定案）

### 3.1 00_f append 點
- baseline：§10 延伸到 **§10.11**（§10.9 拆分規則 = line 290 / §10.10 角色等級對應 = line 304 / §10.11 Frontmatter 規範 = line 312）。
- append 點：**§10.11 之後**（line 312 段尾、§11 line 325 之前）。
- 新編號：**§10.13 個性拆解 / §10.14 source coverage / 下游 hooks**（gap-jump 跳 §10.12，避免與未來可能補的 §10.12 撞號）。
- **刪除**原 `_WAVE2_設計總覽.md` 的「§10.8 後 §10.9 前 或 §10.10-§10.11 之間」矛盾雙選項。

### 3.2 UD append 點
- create-character 區段最後 script = **§10.9 拆分規則**（拆分計畫表 line 969-979；frontmatter 規範 line 991-995）。
- append 點：**§10.9 之後**（line 995 frontmatter 規範段尾、§1.2.3 「與下游的銜接點」line 997 之前）。
- 新編號：**§10.13 / §10.14**（與 00_f 對齊；同採 gap-jump 跳 §10.12）。

### 3.3 §10.13 / §10.14 內容綱要（00_f + UD 對齊；6 欄 script）
- **§10.13 個性拆解**（F9 / NEW_REQ_33；10 子段：表層個性 / 內在個性 / 自尊來源 / 核心恐懼 / 情緒遮掩 / 可愛魅力來源 / 努力與缺陷表現 / 壓力下變形 / 角色差異 / 不可偏移人格模板）。寫入 voice card §A；agent 由議題 1-8 答案綜合，Stage 3 user 確認。required_level = STRONGLY_PREFERRED / locked = false。
- **§10.14 source coverage / 下游 hooks**（F12 / NEW_REQ_36；5 子段：已吸收 source / 交 /create-relationship hooks / 交 /create-outline+/create-detailed-outline hooks / 交 /scene-task hooks / 不應直接當台詞 source）。寫入 voice card §D；只登錄 hooks 不授權寫下游檔。required_level = STRONGLY_PREFERRED / locked = false。
- §B/§C（F11+F13 既有劇本聲線基準 + 使用規則）屬輸出骨架 append（同步面 #4），**不另開 registry 議題**——其性質同 §A/§D「agent-side Stage 4 mechanic」，由議題答案 + 既有劇本 source 綜合，Stage 3 預覽、Stage 4 寫入；F11 input 機制掛在 Stage 1/2（§1.3）。

---

## 4. D-056 / D-057 條目草稿（含 M5 授權範圍 + B2 升格揭露）

> **下一個可用正式 D 編號 = D-056**（DECISIONS_LOG 最後正式拍板 = D-055 §6.18；§6.19 明寫「新議題進 §6.19+（D-056+）」）。

### D-056（草稿）：Wave2 /create-character 個性拆解 + source coverage 落地（F9 + F12 / NEW_REQ_33 + 36）

**日期：** 待 user 拍板  
**性質揭露（B2）：** M4 §3.9 / §3.12 原判 F9 / F12「不需 D-NNN」。Wave2 落地需動 **LOCKED UD §1.2.2 + LOCKED issue_type_registry.template.yaml + LOCKED 00_f**，故**升格為 D-056 必拍**。本條目即此升格紀錄。  
**決策：** voice card 新增固定 §A 個性拆解（10 子段）+ §D source coverage（5 子段）；補 00_f §10.13/§10.14 + UD §1.2.2 §10.13/§10.14 + registry core.00_f_character id 9/10。  
**授權範圍（M5）：**
- **純 append（不 supersede）：** 00_f §10.13/§10.14 新 script；UD §10.13/§10.14 新 script；registry id 9/10 entry；SKILL.md §A/§B/§C/§D 骨架 + Split Rules 兩 row。
- **就地計數修正（既有 LOCKED 內容，授權改 count/ordinal/標題，不改議題語意）：**
  - UD line 773『9 項議題』→『11 項議題』；UD line 769『9 個議題』→『11』；UD line 1005『9 個議題』→『11』
  - UD line 735-744 議題表序號（補 10/11 row）
  - 00_f line 103『共 8 個』→『10』
  - SPEC.md:942『9議題』→『11議題』
  - UD:7323『9議題』→『11議題』
- **D-047 描述計數同步（M3）：** DECISIONS_LOG line 1264『core：列 36 user-facing 議題（10+8+6+6+6）』+ line 1256『5 skill × 36 user-facing 議題』，00_f 8→10 後改 **38（10+10+6+6+6）**。

### D-057（草稿）：Wave2 /create-character 既有劇本萃取 input + 聲線基準 output + D-050 讀邊界 clarification（F11 + F13 / NEW_REQ_35 + 37）

**日期：** 待 user 拍板  
**性質揭露（B2）：** M4 §3.11 / §3.13 原判 F11 / F13「不需（屬 SKILL.md 擴範圍）」。Wave2 落地需動 **LOCKED UD §1.2.2 + 可能 LOCKED 00_f + D-050 邊界 clarification（讀 vs 寫）**，故**升格為 D-057 必拍**。本條目即此升格紀錄。  
**決策：** SKILL.md Stage 1/2 擴 input scope（既有劇本 / docx / .txt / .csv / .json 只讀不寫 + speaker alias matching + 8-12 句篩選 8 場景類型）；voice card 加 §B 既有劇本台詞聲線基準 + §C 既有劇本聲線使用規則；cross-ref STYLE_ANCHOR W-style（D-055）。  
**授權範圍：**
- **D-050 邊界 clarification：** `08_dialogue_outputs/` 維持「不寫」（D-050 子裁決 2 不變），明示「**可讀不可寫**」；讀取不擴大寫檔範圍，寫檔仍嚴格限 `03_characters/`。
- **F11 + F13 必同輪實作**（input + output 一氣呵成）。
- 純 append：SKILL.md §B/§C 骨架；若需，UD §10.13/§10.14 補 input/聲線基準 script 子段（與 D-056 共用新編號區，不另開 §10.15）。

---

## 5. 完整 D-NNN reconciliation（含 D-066/D-067 指派 + M7 清理清單）

### 5.1 撞號根因
M4 §8.2 + POST_LOCK §5.20.5 舊 candidate 表把 **D-056~D-061** 預指給 F3/F7/F8/F1+F6/F17+F18/F19。但：
1. Wave2 把 create-character 群（F9/F11/F12/F13）升格佔 **D-056/D-057**（B2 升格）；
2. fix-list 指明 **D-060~D-065 已被 QA work item + WI-C 佔**；
3. 故 F17+F18 / F19 二次撞號，重指派 **D-066 / D-067**。

### 5.2 最終 D 編號分配表（本檔為權威）

| 最終 D 編號 | Finding / NEW_REQ | 用途 | 舊 candidate（已重指派）|
|---|---|---|---|
| **D-056** | F9 + F12 / NEW_REQ_33 + 36 | 個性拆解 §A + source coverage §D（Wave2）| — (新；舊 D-056=F3 被頂下) |
| **D-057** | F11 + F13 / NEW_REQ_35 + 37 | 既有劇本萃取 input + 聲線基準 output + D-050 讀邊界 | — (新；舊 D-057=F7 被頂下) |
| (待定) | F3 / NEW_REQ_27 | /create-world split rule 修哪邊 | 舊 D-056（已重指派，見本表）|
| (待定) | F7 / NEW_REQ_31 | source/reference dir convention | 舊 D-057（已重指派，見本表）|
| (待定) | F8 / NEW_REQ_32 | 非人格反派 entity 方向 | 舊 D-058 |
| (待定) | F1+F6 / NEW_REQ_25+30 | template skeleton 起始狀態 + Phase4 bump | 舊 D-059 |
| D-060~D-065 | QA work item + WI-C | （已被佔，非本批；不得重用）| — |
| **D-066** | F17 + F18 / NEW_REQ_41 + 42 | pattern pack 機制（依 00_b §1 作品類型載入 mode）| 舊 D-060（二次撞號，已重指派）|
| **D-067** | F19 / NEW_REQ_43 | 個人線邊界規則 | 舊 D-061（二次撞號，已重指派）|

> 注：F3/F7/F8/F1+F6 的最終正式號待各自批次拍板時於 §6.19 順延取下一個未用號；本檔只確定 Wave2 必拍的 D-056/D-057 與被二次撞號的 D-066/D-067。F3/F7 不再保證拿 D-056/D-057（已被 Wave2 佔）。

### 5.3 M7 清理清單（一律 inline 註『舊 candidate（已重指派，見 §6.19 reconciliation）』；只改狀態不刪歷史）

| 檔案 | 位置（重驗行號）| 舊字樣 | 清理動作 |
|---|---|---|---|
| POST_LOCK | §5.20.3 line 2285-2287 | Wave-A3『…pattern pack[D-060]…[D-061]』| inline 註舊 candidate 重指派 → D-066/D-067 |
| POST_LOCK | §5.20.5 line 2305-2310 | D-056=F3 / D-057=F7 / D-060=F17+18 / D-061=F19 | inline 註：D-056/D-057 已被 Wave2 create-character 群佔；F17+18→D-066、F19→D-067 |
| POST_LOCK | NEW_REQ_41 body line 1819/1829/1837/1841/1845 | 『依賴 D-060…』『D-060 拍板候選』 | inline 改 D-066（註舊 D-060）|
| POST_LOCK | NEW_REQ_42 body line 1852/1862/1870/1874/1878 | 『D-060 pattern pack』 | inline 改 D-066（註舊 D-060）|
| POST_LOCK | NEW_REQ_43 body line 1885/1895/1903/1907 | 『依賴 D-061』『D-061 拍板候選』 | inline 改 D-067（註舊 D-061）|
| POST_LOCK | NEW_REQ_33 line 1574 | 『不需 D-NNN』 | 改『升格 D-056 必拍（Wave2 動 LOCKED UD/registry）』|
| POST_LOCK | NEW_REQ_35 line 1633 | 狀態列（無明標但 M4 §3.11 判不需）| 同步註『升格 D-057 必拍』|
| POST_LOCK | NEW_REQ_36 line 1653 | (Wave-A1；M4 §3.12 判不需) | 同步註『升格 D-056 必拍』|
| POST_LOCK | NEW_REQ_37 line 1687 | (Wave-A3；M4 §3.13 判不需) | 同步註『升格 D-057 必拍』|
| M4 | §3.9 line 214 | 『D-NNN candidate \| 不需』| 改『升格 D-056 必拍（Wave2 動 LOCKED UD/registry）』|
| M4 | §3.11 line 242 | 『不需（屬 SKILL.md 擴範圍）』| 改『升格 D-057 必拍』|
| M4 | §3.12 line 256 | 『不需』| 改『升格 D-056 必拍』|
| M4 | §3.13 line 270 | 『不需（屬 SKILL.md 擴 + D-050 邊界明示讀邊界）』| 改『升格 D-057 必拍』|
| M4 | §8.2 line 571-576 | D-056=F3 / D-057=F7 / D-060=F17+18 / D-061=F19 | inline 註舊 candidate 重指派（同 POST_LOCK §5.20.5）|
| M4 | §6.2 Batch 規劃表 line 496（B8）| 『F17+F18 pattern pack（D-060）』| inline 改 D-066（註舊 D-060）|
| M4 | §6.2 line 491（B3）+ §5.x Wave-A3 line 448 | 『…D-060…D-061…』| inline 改 D-066/D-067（註舊號）|

### 5.4 §6.19.6 deferred 表行序（M6）
DECISIONS_LOG §6.19 新增的 deferred / 重指派表，行序改 **D-060 / D-061 / D-062 升序**呈現（升序列出 QA work item + WI-C 既佔號 + 被頂下的舊 candidate），避免亂序造成 reviewer 再次誤判撞號。

---

## 6. DECISIONS_LOG / POST_LOCK 補記草稿

### 6.1 DECISIONS_LOG 補記
- 新建 **§6.19**（承 line 2241『新議題進 §6.19+（D-056+）』），含 §6.19.x：
  - §6.19.x D-056 條目（見本檔 §4）
  - §6.19.x D-057 條目（見本檔 §4）
  - §6.19.6 deferred / 重指派表（M6 升序：D-060/D-061/D-062…；含 D-066/D-067 指派 + 舊 candidate 重指派揭露）
- **§6.9.2 D-047 就地修正（M3）：** line 1264『36 user-facing 議題（10+8+6+6+6）』→『**38（10+10+6+6+6）**』；line 1256『5 skill × 36』→『5 skill × **38**』。標註「D-056 授權範圍內就地計數修正；不改 D-047 機制語意」。
- header 版本 v2.1 → v2.2，note 寫「Wave2 D-056/D-057 拍板 + D-047 計數 36→38 + D-066/D-067 重指派」。

### 6.2 POST_LOCK 補記
- NEW_REQ_33/35/36/37：狀態列『不需 D-NNN』→『升格 D-056/D-057 必拍（見 §6.19 reconciliation）』（見 §5.3 清理表）。
- §5.20.5 candidate 表：inline 註重指派（D-056/D-057 → Wave2 create-character 群；F3/F7 順延；F17+18→D-066、F19→D-067）。
- §5.20.3 Wave-A3 + NEW_REQ_41/42/43 body：D-060→D-066、D-061→D-067 inline 改 + 註舊號。
- **Errata 對齊（重驗發現的額外不一致；建議一併修）：** POST_LOCK line 1647 Errata 宣稱「NEW_REQ_36-43 entry body 從未實際寫入本檔 body」，但重驗發現 NEW_REQ_36（line 1651+）/ 37（1685+）/ 41（1817+）/ 42（1850+）/ 43（1883+）body **實際存在**。該 Errata 自身已 stale；補記時應更正為「body 已存在，僅 §5.20/§5.21 section 結構曾缺，現補」。
- header 版本升版，note 寫「Wave2 D-NNN 升格 + 重指派 + Errata 自我更正」。

---

## 7. 落地順序建議（不阻 user 拍板）
1. user 拍板 D-056 + D-057（B2 升格）+ D-066/D-067 重指派。
2. registry append id 9/10（純 append）。
3. 00_f §10.13/§10.14 append + §4.1 表 + line 103 計數 + §1 清單（同步面 5/6/7/8）。
4. UD §10.13/§10.14 append + §1.2.1 表 + §1.2.2 標題/body 計數（同步面 9/10/11）。
5. SPEC.md:942 + UD:7323 兩處「9議題」→「11議題」（同步面 12 / B1 兩目標）。
6. SKILL.md core issue 表 + Split Rules + §B/§C 骨架（同步面 1/2/4）。
7. DECISIONS_LOG §6.19 + §6.9.2 計數修正 + POST_LOCK / M4 清理（§5.3 + §6）。
8. F11+F13 必同輪；F9/F12 可隨同批落地（Batch B2 一輪到位）。
