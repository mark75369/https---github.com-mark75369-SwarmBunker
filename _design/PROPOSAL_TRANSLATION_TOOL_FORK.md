狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：未來分支工具設計提案 — 翻譯專用 companion tool（NEW_REQ_11；user 拍板 DEFERRED 至工具 A 完整封裝後）
優先級：中

# PROPOSAL_TRANSLATION_TOOL_FORK — 翻譯專用 companion tool 分支設計提案

# 0. 文件性質

本檔是「**未來分支工具設計提案紀錄**」 — 不是 spec / 不是 D-NNN 拍板 / 不是任何當前 task 的執行依據。

紀錄這設計提案是為了：
1. 保存討論成果（master 第六輪對話內 user 提案 + master 評估的設計 insight）
2. 給未來新 master 對話 / specialist 對話 / 啟動工具 B 開發時的「**起點包**」
3. 提醒「保留工具 A 對工具 B 友好的設計選擇」（如 L3 export schema 保留所有 metadata）

**狀態：DEFERRED**

**啟動條件：** 工具 A（game-dialogue-bible）**完整封裝（寫作開發工具 release 之後）** — 即 Milestone 3 / 4 之後（Phase D 完成 + 完整 production 級 release）。提早啟動會脫離真實 source corpus + 工具 A 仍在演進。

---

# 1. 提案背景

## 1.1 user 提案脈絡

master 第六輪整合對話內，user 問「這工具用在多語言翻譯效果如何」。master 第一輪回答「工具是翻譯友善 source 工具，不是翻譯工具；用外部 i18n 工具（Crowdin / Lokalise）即可」。

user 提出更精準的洞察：「**這工具產出的資料含大量可以提高翻譯品質的部分；不直接全部包在這個工具裡，但可以透過修改這個工具做成另一個翻譯專用工具（只讀資料 + 翻譯 + QA）**」。

master 第六輪 ack 這提案 — 並承認 master 第一輪回答忽略的盲點。

## 1.2 master 第一輪回答的盲點

主流 i18n 工具（Crowdin / Lokalise / POEdit）的設計是「**純台詞 string 翻譯**」 — 翻譯員看到的是扁平 string：

```
line_235: 主角A: 你好，這把劍是我父親留下的。
```

但工具 A 產出的 source 含**豐富上下文 metadata**：
- W-rules（這世界的科技水平 / 價值觀 / 規則最小集）
- V（專有名詞表 + 慎用詞 + 黑話 + 禁用詞）
- C-* 聲線卡（角色說話風格 / 髒話來源 / 偏移特徵 / 8 議題的對話風格紀錄）
- R-* 關係（NPC 對主角的權力差 / 稱呼系統 / 情緒債 / 不能說出口的事）
- P 大綱位置（這場戲在主線哪段；資訊揭露階段）
- CH 章節節奏（這場戲在章節張力曲線位置）
- 09_a~09_i QA 報告（聲線一致性 / 節奏感 / 對話張力 / 跨場一致性）

主流 i18n 工具**不吃這些 metadata** → 翻譯員不知道「這個角色到這場戲為止應該有什麼語氣 / 情緒積累 / 稱呼變化 / 潛台詞」 → **翻譯品質遠低於 source 品質**（source 是「全 context-aware 創作」；翻譯是「context-blind 字面對應」）。

## 1.3 user 提案解的問題

「**context-aware 翻譯工具**」 — 翻譯員（人 + agent）看到的不只是字面，還包括：
- 該角色聲線卡關鍵描述（如「主角 A 對權威人物用敬語但對同輩用直白」）
- 該關係稱呼系統（如「主角 A 稱呼 B 為『兄』；B 稱主角 A 名字直呼」）
- 該場景在主線位置（如「P 第三幕揭穿前 1 場 — 角色情緒積累到頂點」）
- 上下文場景的台詞鏈
- 09_b 聲線一致性檢查報告（source 端）
- 翻譯版的 09_a (AI 味) / 09_c (禁用詞 — 各語言獨立) QA

---

# 2. 為什麼工具 B fork 是好設計

| 設計優點 | 對齊既有設計 |
|---|---|
| **完美 SoC**（separation of concerns）：工具 A source / 工具 B 翻譯 | ✓ 不破壞工具 A LOCKED D-018 #2「不存多語對白」結論 |
| **單向依賴**：工具 B 只讀工具 A export，不回寫 source | 對齊 REQUIREMENTS_LOCK §3.1「多格式輸出 + 引擎特定轉檔在外」哲學 |
| **重用既有 spec 範式** | entity_type_registry / qa_type_registry / issue_type_registry user_extensions / 5 階段對話 / phase_log / D-049 Template-detect / D-050 寫檔邊界全部直接 fork |
| **翻譯任務包是 context-aware** | source 的 W/V/C/R/P/CH metadata 全部可見 + 09_b 聲線卡 + 上下文場景 |
| **責任清楚** | 工具 A 做中文劇本創作；工具 B 做翻譯 + 翻譯 QA；不重疊 |

對比其他選項：

| 方向 | 評估 |
|---|---|
| (A) 保留現狀 + 純 i18n 工具對接 | 不充分利用 source metadata；翻譯品質低 |
| (B) 在工具 A 內加翻譯 QA 模組 | 違反 SoC；工具 A 變過大；不解決根本問題 |
| (C) 工具 A 改成多語言原生 | 違反 D-018 #2 LOCKED；需 D-NNN 大規模 partial supersede |
| **(D) fork 工具 B（user 提案；本檔紀錄）** | ✓ 完美對齊既有設計哲學 |

---

# 3. 工具 B high-level 設計構想

## 3.1 工具 B 結構

```
game-dialogue-translator/              ← 工具 B 名稱（暫定；正式啟動時 user 拍板）
├─ AGENTS.md / CLAUDE.md              ← 同 D-048 multi-agent invocation 慣例
├─ .template_root                      ← 同 D-049 Template-detect 防線
├─ _design/                            ← 工具 B spec（fork 自工具 A 部分 + 翻譯 layer）
│  ├─ ARCHITECTURE.md                 ← 工具 B 架構（fork from 工具 A ARCH + 翻譯擴充）
│  ├─ SPEC.md                         ← 翻譯 entity 類型 / KEY mapping / 翻譯狀態機
│  ├─ TRANSLATION_QA_SPEC.md          ← 翻譯 QA pipeline 規格
│  ├─ TRANSLATION_PROTOCOL_SPEC.md    ← agent 對話 5 階段翻譯流程
│  └─ registries/                     ← 翻譯類型 / 翻譯 QA registry
│     ├─ entity_type_registry.template.yaml   ← 含 T-* / G-*
│     ├─ qa_type_registry.template.yaml       ← 含翻譯 QA 09_a~09_i + 09_t1/t2/t3
│     └─ issue_type_registry.template.yaml    ← 含翻譯議題清單
├─ _input/                             ← 工具 A export 進來的 JSON+MD（read-only）
├─ _output/                            ← 翻譯後的多語言版本
├─ 01_source/                          ← 工具 A export 的 metadata（從 _input/ 解析）
│  ├─ world_overview.json
│  ├─ vocabulary.json
│  ├─ characters/*.json
│  ├─ relationships/*.json
│  ├─ plot/*.json
│  ├─ chapters/*.json
│  └─ dialogue/*.json
├─ 02_translations/                    ← 翻譯結果
│  ├─ en/
│  │  ├─ scenes/<scene_id>.md
│  │  └─ ...
│  ├─ ja/
│  ├─ ko/
│  ├─ zh-Hant/  ← 簡繁中文不同（如有需求）
│  └─ ...
├─ 03_glossary/                        ← 各語言 glossary（從 V 詞表 export 過來）
│  ├─ en/glossary.json
│  ├─ ja/glossary.json
│  └─ ...
├─ 04_translation_qa/                  ← 翻譯版 QA report
│  ├─ qa_a_ai_taste/<lang>/            ← 翻譯版 09_a 對應（各語言獨立判定）
│  ├─ qa_b_voice_consistency/<lang>/   ← 翻譯版 09_b（聲線跨語言一致性）
│  ├─ qa_c_banned_words/<lang>/        ← 翻譯版 09_c（各語言獨立禁用詞）
│  ├─ qa_d_info_control/<lang>/        ← 翻譯版 09_d
│  ├─ qa_e_final_gating/<lang>/        ← 翻譯版 09_e
│  ├─ qa_f_genre_shift/<lang>/         ← 翻譯版 09_f
│  ├─ qa_g_rhythm/<lang>/              ← 翻譯版 09_g
│  ├─ qa_h_dramatic_tension/<lang>/    ← 翻譯版 09_h
│  ├─ qa_i_cross_scene/<lang>/         ← 翻譯版 09_i
│  ├─ qa_t1_translation_consistency/   ← 跨語言版本對齊（新）
│  ├─ qa_t2_culture_adaptation/        ← 文化適配紀錄（新）
│  └─ qa_t3_ui_length_constraint/      ← UI 框長度約束（新）
├─ scripts/                            ← 工具 B 自己的 parser / QA runner
│  ├─ import_source.py                ← 從工具 A export JSON+MD 進工具 B
│  ├─ parse_translation.py             ← 解析翻譯結果 frontmatter / KEY mapping
│  ├─ check_translation_paths.py
│  ├─ check_translation_headers.py
│  └─ run_translation_qa.py
├─ .claude/skills/                     ← 工具 B 自己的 skill
│  ├─ import-source/                  ← 從工具 A export 匯入；產 01_source/
│  ├─ translate/                       ← agent 輔助翻譯 5 階段對話（核心 skill）
│  ├─ qa-translation/                  ← 翻譯版 QA
│  ├─ status/                          ← 翻譯完成度
│  ├─ check-gaps/                      ← 翻譯缺漏偵測
│  └─ （+ 中文 wrapper x 5）
└─ _user_manual/                       ← 工具 B user manual
```

## 3.2 工具 B 新 entity 類型

| Entity ID 格式 | 意義 | 創建來源 |
|---|---|---|
| `T-<source_KEY>-<lang>` | 一句翻譯（source KEY + 目標語言）| /translate skill |
| `G-<term>-<lang>` | 一個 glossary entry（術語 + 目標語言）| /translate skill 階段 4 同步 |
| `TQ-<scene_id>-<lang>-<qa_type>` | 翻譯 QA report | /qa-translation skill |

## 3.3 工具 B 新 QA 類型

**沿用工具 A 09_a~09_i（每種語言獨立跑）：**
- 翻譯版 AI 味 / 聲線 / 禁用詞 / 資訊控制 / final-gating / 類型偏移 / 節奏感 / 對話張力 / 跨場一致性

**翻譯特有 QA（新）：**
- **09_t1 翻譯一致性檢查** — 同 source KEY 跨多語言版本是否一致對應（如「主角 A 名字在 EN/JA/KO 各語言版本對應穩定」）
- **09_t2 文化適配紀錄** — 雙關 / 同音字 / 文化典故的 locale-specific 處理紀錄（如「中文『天降大任於斯人也』英文不直譯，用文化等價句」）
- **09_t3 UI 長度約束** — 翻譯後是否超出 UI 框（如「英文翻譯通常比中文長 1.3-1.5 倍；遊戲對話框 200px 寬限 X 字」）

---

# 4. 工具 B 核心 skill：/translate <scene_id> <lang>

對齊工具 A 5 階段對話範式（同 ARCHITECTURE §3.3）：

## 階段 1 — 診斷

agent 讀工具 A export 的 source 全 context：
- 該場景 dialogue lines（含 KEY metadata）
- 上下文 5 場景台詞鏈
- W/V/C/R/P/CH metadata
- 該角色聲線卡（從 03_characters/<name>_聲線卡.md）
- 該關係的稱呼系統（從 04_relationships/04_a + 04_b + 角色聲線卡【關係】段）
- 該場景在主線的位置（從 05_plot/）
- 該場景的章節節奏（從 05_b 章節結構 — Wave 8 後）
- 既有 09_a~09_i source QA reports（如已跑）

印翻譯診斷報告 + 預告階段 2 會跑翻譯議題（依目標語言）。

## 階段 2 — 探索（翻譯議題逐題）

對 user 問翻譯議題，例如：
- 「主角 A 對 B 的稱呼『兄』在 EN 翻 brother / older brother / 直呼名 first name？」
- 「這段潛台詞翻譯後保留嗎？或是字面化？」
- 「文化典故『塞翁失馬』在 JA 翻直譯 / 借日語成語 / 改述意？」
- 「該專有名詞『青虹劍』在 EN 用 Azure Rainbow Sword / Qinghong Sword (羅馬拼音) / Cyan-Crystal Blade（意譯）？」
- 「角色聲線卡標註此角色用古風語氣，EN 用 archaic style / modern equivalent？」

每題引用 source metadata 作為對話 context。

## 階段 3 — 收斂

agent 印翻譯預告稿：
- 翻譯後台詞清單（每 KEY 對應翻譯）
- 新增 glossary entries（如「兄 → Brother (capital case)」紀錄到 03_glossary/<lang>/）
- 09_t1/t2/t3 預跑風險預告

user 拍板「通過」 / 「OK」 / 「寫檔」後進階段 4。

## 階段 4 — 寫檔

依 D-050 同精神（工具 B 自己的寫檔邊界紀律）：
- 寫 02_translations/<lang>/scenes/<scene_id>.md（翻譯結果）
- 更新 03_glossary/<lang>/glossary.json（同步新術語）
- 嚴禁寫工具 A 任何檔（單向依賴）
- 嚴禁寫 01_source/（read-only mirror）
- 更新 .protocol_version phase_log（紀錄翻譯 entity 創建）

## 階段 5 — 驗證

跑 09_a~09_i 翻譯版 QA + 09_t1/t2/t3 + 印「下一步建議跑 /qa-translation 完整 QA pipeline」+ 更新 status。

---

# 5. 工具 B QA pipeline 設計

## 5.1 翻譯 QA 跑法

對每 scene + 每 lang 跑：
1. 09_a 翻譯版 AI 味（針對該語言的 AI 寫作慣性檢查）
2. 09_b 聲線一致性（同角色在不同 scene 翻譯後聲線是否漂移）
3. 09_c 禁用詞（每語言獨立禁用詞 list — 如 EN 不用 "literally" / JA 不用「ヤバい」過度等）
4. 09_d 資訊控制（翻譯後資訊揭露是否提前 / 延後）
5. 09_e final-gating（翻譯版最終裁決紀錄）
6. 09_f 類型偏移（翻譯後是否走向「西方奇幻味」「美劇對話節奏」等）
7. 09_g 節奏感（句長分布 / 段落呼吸感 — 各語言獨立判定）
8. 09_h 對話張力（攻防力度跨語言保留度）
9. 09_i 跨場一致性（同 source 跨 scene 翻譯是否一致）

## 5.2 翻譯特有 QA

10. 09_t1 翻譯一致性 — 跨多語言版本對齊（如 EN 版「兄」翻 brother；JA 版翻「兄さん」；KO 版翻「형」— 這些對應穩定，沒有 EN scene 1 翻 brother / EN scene 5 翻 older sibling）
11. 09_t2 文化適配 — 紀錄每場 locale-specific 處理（雙關保留 / 改述 / 註腳）
12. 09_t3 UI 長度約束 — 每語言對應 UI 框寬度，警告超長翻譯

---

# 6. 工時 + 時機評估

## 6.1 工時估算

| 階段 | 工時 |
|---|---|
| 設計層（fork spec + 翻譯 entity / QA / protocol 設計）| 20-30h master 對話 |
| 實作層（parser / skill / QA runner / 前端 UI）| 50-80h CODEX 對話 |
| 文檔（user manual + skill_invocation_guide）| 10-20h |
| **總計** | **80-130h master + CODEX** |

跟工具 A 從 Phase 1 到 master 第六輪整合的工時（6 個月持續開發）類似量級。

## 6.2 時機

**user 拍板：「在寫作開發工具封裝後才會進行」**

意指：工具 A 完整封裝 release 後才啟動工具 B。對應里程碑：
- **Milestone 1 達成**（2026-05-19）：第一個能跑版本（M1 user-test）✓
- **Milestone 2 預期**：全上游 skills 完成（Phase B 收尾後）
- **Milestone 3 預期**：全 dialogue 生產 skills 完成（Phase C 收尾後）
- **Milestone 4 預期**：完整 production release（Phase D 收尾後 — UI 全部完成 + L3 export 穩定 + 真實 dialogue corpus）
- **🟢 工具 B 啟動：Milestone 4 之後**（user 明示）

## 6.3 為什麼不該提早啟動

1. **工具 A 還沒實際跑過完整 dialogue 生產** — Phase C `/scene-task` + `/dialogue-write` + `/qa` 未啟動。工具 B 設計時必須看「真實 source 長什麼樣」才能設計好翻譯 entity / QA。提早 = 憑空設計 = 脫離真實需求
2. **L3 export schema 未穩定** — 工具 A 的 L3_EXPORT_PROMPT_SCHEMA v0.2 是「設計層 spec」，實際吐 JSON 還沒在 Phase A.0F 後段做。工具 B 是 JSON 消費者；source 端 schema 不穩 → 工具 B 跟著漂移
3. **真實翻譯需求未浮現** — user 還沒到「我作品要翻 EN / JP」階段；提早做 = 過度設計
4. **工具 A 收尾節奏不該被打斷** — Milestone 2 / 3 / 4 各自有 user-test 點，這些是工具 A 演進的關鍵驗證
5. **跟工具 A v0.1 同樣風險** — 工具 A 也是從 v0.1 跑了多輪 specialist + master 重構才到 LOCKED；工具 B 應該從「真實需求 + 真實 source corpus」開始，避免重複 v0.1 砍掉重練

---

# 7. 啟動工具 B 的前置條件清單

工具 A 達到下列**全部**條件後才啟動工具 B（建議第 N 輪 master 對話前自查）：

```
✓ 工具 A Milestone 4 達成（Phase D 完成 + production release）
✓ L3_EXPORT_PROMPT_SCHEMA v1.0 穩定（實際吐過真實 JSON）
✓ 至少 1 個完整作品 source corpus 存在（包含 W/V/C-* / R-* / P / CH-* / S-* / dialogue / 09_a~09_i QA reports）
✓ user 明確表達翻譯需求（「我這作品要翻 EN/JP/KO」）
✓ 工具 A 維護期穩定 6 個月以上（無 critical patch round / 無 LOCKED spec 重大改動）
```

---

# 8. 現在工具 A 可以做的「對工具 B 友好」設計選擇

不需要等到啟動工具 B；工具 A 開發過程可以**順手保留下列友好選擇**：

| 工具 A 現在的選擇 | 對工具 B 的影響 |
|---|---|
| L3_EXPORT_PROMPT_SCHEMA `keep_all_metadata: true` 預設 | 工具 B 啟動時可直接拿到 W/V/C/R/P/CH 全 metadata，不必工具 A 改 schema |
| entity_type_registry user_extensions 機制設計時保留「未來分支 fork」可行性 | 工具 B 直接 fork registry pattern，不必重寫 |
| qa_type_registry user_extensions 機制同上 | 工具 B 加 09_t1/t2/t3 屬 user_extensions 自然擴充 |
| issue_type_registry user_extensions 機制同上 | 工具 B 加翻譯議題（如「稱呼系統翻譯」「文化典故處理」）屬 user_extensions |
| KEY 機制設計時保留全 repo unique guarantee | 工具 B 用 `T-<source_KEY>-<lang>` 命名安全 |
| phase_log schema `skill / status / created_entities` 範式 | 工具 B 直接套用紀錄 T-* / G-* entity 創建 |

工具 A 開發團隊只要**不刻意破壞**上述選擇，工具 B 就有平順 fork 路徑。

---

# 9. Cross-ref

- `_design/REQUIREMENTS_LOCK.md` v1.0 §3.1 工具定位 + §3.2 i18n KEY 機制 + §4.2 可擴充 QA 機制
- `_design/DECISIONS_LOG.md` v1.5 D-018 #2「多語對白不採」LOCKED 結論
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（工具 B 主要 input 來源）
- `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D D-047 issue_type_registry（可 fork）
- `_design/DATA_FORMAT_SPEC.md` v0.4 §8 qa_type_registry（可 fork）
- `_design/POST_LOCK_PENDING.md` v0.5 NEW_REQ_11（DEFERRED entry）
- `_design/DECISIONS_LOG.md` v1.6 §6.13（提案紀錄）

---

# 10. 文件維護紀律

- 本檔屬「**提案紀錄檔**」性質 — 不是 spec / 不需要進 LOCKED 鏈
- 啟動工具 B 開發前可重讀本檔 + 評估更新點（如「工具 A v1.x 後新 metadata 是否要加進工具 B 設計考慮」）
- 啟動工具 B 後本檔 archive 進 `_design/archive/` + 工具 B 新 repo 內 `_design/PROPOSAL_HISTORY/` 保留 reference
- 期間如有相關設計 insight（如「Phase C 跑完 dialogue 後發現某些 metadata 對翻譯很關鍵」）追加到本檔 §11 附錄
