狀態：LOCKED
版本：v2.1（master 第五輪整合 — D-047 issue_type_registry contract + Stage 0 A.0.10 對齊 + NEW_REQ_3/4/5/6 RESOLVED）
最後更新：2026-05-19
適用範圍：三 specialist v0.4 patch 完成後的 Contract A/B/C 正式介面 / Master 第四輪整合對話 owns / pre-LOCKED CC-01~CC-09 + PS-01~PS-05 + Recheck-02 殘留清盤 / master 第五輪 Contract D 加入
優先級：最高

# INTEGRATION_CONTRACTS — Specialist 跨界介面契約 v2.1

# v2.1 變動摘要（master 第五輪 — 2026-05-19）

**新增：**
- **Contract D**（§4a 全新章節）— D-047 issue_type_registry 契約：UD ↔ DF ↔ Phase B /create-* skill / 三介面對齊；包含 D.1 schema / D.2 Phase B 讀 registry 行為 / D.3 user_extensions / core_overrides 衝突處理 / D.4 A.0F frontend 編輯 UI 對齊（real-data acceptance scope）
- §0.3 D-NNN 拍板清單加 D-047 row

**v2.0 → v2.1 partial supersede：**
- Contract A.5（qa_type 8 種 + extensible registry）內容**不動** — 但 v2.1 註腳補：本契約對齊 DF §8 v0.2 + UD §3.10 v0.5 NEW_REQ_6 修補（UD §3.10 已從「`.qa_extension/*.yaml` 獨立檔」改為「`qa_type_registry.yaml user_extensions:` 段」寫法，與 Contract A.5 完全一致 — 之前的 spec 衝突已 RESOLVED via NEW_REQ_6）
- §1 三 Contracts Overview 加 Contract D box

**v2.1 不動：**
- Contract A.1 ~ A.4 / A.6 ~ A.8（D-037 ~ D-046 落地內容不動）
- Contract B.1 ~ B.8（不動）
- Contract C.1 ~ C.5（不動）
- §5 / §6 / §7 / §8 / §9 結構不動，僅 §8.2 補 v2.1 升版紀錄

**v2.1 小 typo cleanup（同 DF §8.2/§9.1 / UD §12 NEW_REQ_4 同類擴充模式）：**
- §2.5.3 qa_type_registry yaml 範例 schema_version v0.1→v0.3 + template_path 改完整相對路徑（對齊 qa_type_registry.template.yaml 權威）
- §2.7.1 JSON export manifest 範例 spec_version v0.1→v0.4（對齊 DF v0.4 當前版本）

# 0. 文件性質與 v2.0 狀態

## 0.1 v2.0 跟 v1（過渡版）的關係

| 版本 | 性質 | 時點 |
|---|---|---|
| v0 | 預估版 — master 對話在 specialist 啟動前寫的「預期介面」 | Phase 3 啟動前 |
| v1（過渡版） | specialist 第一輪部分交付後寫的 partial refine | Phase 3 第一輪交付後 |
| **v2.0（本檔）** | **specialist 第二輪 + v0.3 patch + CODEX (c) 17 衝突 + master 第四輪 D-037~D-046 拍板後的正式介面** | Phase 3 收斂完成；進 Phase A.0 前的最後 contract 形狀 |

**v1 → v2.0 變動摘要：**

1. v1 §2 Contract A 只列 9 列 schema 議題（多數標「不擴充」）；**v2.0 §2 Contract A 重寫為 8 條真實介面**（A.1 ~ A.8），涵蓋 v0.3 patch 後三 specialist 對齊形狀
2. v1 §3 Contract B 只列 53 個 UX-N 對應；**v2.0 §3 Contract B 重寫為 8 條跨流程介面**（B.1 ~ B.8），含完整 UX-1~UX-80（合併後 78 元件）覆蓋
3. v1 無 Contract C 實質內容（標 Batch 5 補完）；**v2.0 §4 新增 Contract C 5 條**（C.1 ~ C.5）DF ↔ UX 跨層映射
4. v1 §8/§9 Pending 議題已多數 RESOLVED via D-037~D-046；**v2.0 §6 重新整理 Pending 殘留 + 對 Phase A.0 / 後續階段的分派**
5. v2.0 整合 CODEX (c) 審查的 17 條衝突 + 5 條越界結論：11 條 critical/major RESOLVED via D-037~D-046；殘留條目進 §6 Pending

**v2.0 不變動的 v1 內容：**

- §5 Master 強制介入議題清單（不動）
- §6 衝突偵測與升級機制（不動，移至 §7）
- §7 三 specialist 回傳節奏建議（v2.0 為歷史紀錄；本輪三 specialist 第二輪 + v0.3 patch 已完成）

## 0.2 v2.0 閱讀對象

| 對象 | 用途 |
|---|---|
| Phase A.0 parser 開發者 | Contract A 全部 8 條 = parser 必處理的資料形狀清單 |
| Phase A.0 frontend adapter 開發者 | Contract B/C 全部 = frontend server.py API endpoint 規格 |
| 未來 specialist 重啟設計（如 user 後續加新需求） | v2.0 §0 ~ §5 = 既有契約完整快照；新需求 refresh 後從本檔啟動新 contract refine |
| CODEX (d) 短審查者 | v2.0 全文 = 跨 spec 一致性檢查的權威依據 |
| 整合 master 後續對話 | §6 Pending + §8 後續更新區 = 接手依據 |

## 0.3 v2.0 對應的 D-NNN 拍板清單

本檔 v2.0 內容對應以下 D-NNN（依執行順序）：

| D-NNN | 簡述 | 主要落地在 v2.0 哪條 |
|---|---|---|
| D-037 | dialogue_keys Map shape + KEY lifecycle status enum | A.1 + A.4 + B.6 + C.2 |
| D-038 | L3 export A1 prompt + CC/CODEX + 4 附帶 | A.7（間接）+ B.3 + C.3 |
| D-039 | JSON `manifest + records[]` 為權威 | A.7 + C.3 |
| D-040 | LOCKED Save guard | B.2 |
| D-041 | A-* SoT = `10_art_assets/` | A.3 |
| D-042 | phase_log 5 新欄位 + base_dialogue | A.2 + A.6 + C.4 |
| D-043 | 8 份 QA 全預設必跑 + 09_e final-gating | A.5 + B.5 |
| D-044 | A-* subtype 7 種 | A.3 + C.1 |
| D-045 | A-* 不納入 narrative /status | B.4 + C.5 |
| D-046 | UX-54~80 補表 + 7 項 patch | B.1 + B.3 + B.6 + B.8 + §5.2 既有 4 個 /export-* 不擴充 |
| **D-047**（v2.1 新增）| **issue_type_registry 三層機制（5 skill × 36 user-facing 議題客製化）** | **§4a 全新 Contract D（D.1 ~ D.4）** |

**重要：** v2.0 不引入新 D-NNN；本檔是「拍板結論的介面具體化」，不是「再設計」。若 v2.0 落地時發現 D-NNN 互相牴觸（例如兩條 D-NNN 在同一接點要求不同行為），master 第四輪整合對話依 north-star 對齊原則自選方案 + 寫理由標註（north-star 優先序：REQUIREMENTS_LOCK v1.0 > D-037~D-046 > D-001~D-036 > specialist v0.3 一致性）。

**v2.1 新增 D-047：** master 第五輪整合對話拍板新 D，落地為新 Contract D（§4a）— 與既有 D-037 ~ D-046 不衝突。

---

# 1. 三 Contracts Overview

```
┌─────────────────────────────────────────────────────────────┐
│ Contract A：DF ↔ UD（資料形狀 ↔ 上下游消費）                  │
│ 「資料是這個形狀；下游 pipeline 必須依此消費 / 寫入」          │
├─────────────────────────────────────────────────────────────┤
│ A.1  dialogue_keys Map shape（D-037）                        │
│ A.2  phase_log 完整 schema（基礎 + 5 新欄位）（D-042）         │
│ A.3  A-* SoT = `10_art_assets/` + 7 subtype（D-041 + D-044） │
│ A.4  i18n KEY lifecycle status enum（D-037）                 │
│ A.5  qa_type 8 種 + extensible registry（D-043）             │
│ A.6  mode_tag SINGLE_ITER + base_dialogue lineage（D-042）   │
│ A.7  JSON `manifest + records[]` 為 export 權威（D-039）     │
│ A.8  trust-level 限上游 /create-* 路徑（C-08 + D-038）       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Contract B：UD ↔ UX（上下游邏輯 ↔ 前端呈現）                  │
│ 「pipeline 行為是這樣；UI 必須對應呈現這些事件 / 狀態」       │
├─────────────────────────────────────────────────────────────┤
│ B.1  UX-1~UX-80 全覆蓋（合併後 78 元件）（D-046 #1+#2）       │
│ B.2  Save race guard for LOCKED — 5 步流程（D-040）          │
│ B.3  Export Prompt panel UI（D-038 + L3_EXPORT_PROMPT_SCHEMA）│
│ B.4  Asset Panel for A-* — 7 subtype 獨立顯示（D-045）       │
│ B.5  8 QA execution order UI 對齊（D-043）                   │
│ B.6  KEY status enum dropdown / badge（D-037）               │
│ B.7  trust-level 限上游 — 無前端 UI 選（C-08 + D-038）       │
│ B.8  Conflict modal — entity 命名衝突 4 選項（D-033）         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Contract C：DF ↔ UX（資料形狀 ↔ 前端呈現）                    │
│ 「frontend adapter 從資料形狀 derive UI 用的 view」          │
├─────────────────────────────────────────────────────────────┤
│ C.1  A-* subtype 7 種 → UI dropdown / chip（D-044）           │
│ C.2  KEY status enum → UI dropdown / badge（D-037）          │
│ C.3  JSON records[] → 前端不消費，用 derived view（D-038/039）│
│ C.4  phase_log new fields → /status & details pane（D-042）  │
│ C.5  A-* completeness → asset panel only（D-045）            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Contract D（v2.1 新增）：DF ↔ UD ↔ Phase B（議題清單客製化）  │
│ 「issue_type_registry 三層機制 — 5 skill × 36 議題」          │
├─────────────────────────────────────────────────────────────┤
│ D.1  issue_type_registry.yaml schema 與 Template/Instance     │
│      分層（D-047）                                            │
│ D.2  Phase B /create-* skill 讀 registry 動態構建議題清單     │
│      （core + user_extensions − core_overrides）（D-047）     │
│ D.3  user_extensions / core_overrides 衝突處理 + locked       │
│      議題防 SKIP 規則（D-047）                                 │
│ D.4  A.0F frontend issue registry 編輯 UI 對齊                │
│      （real-data acceptance scope）（D-047）                  │
└─────────────────────────────────────────────────────────────┘
```

**三條 contract 的方向（v2.0 對齊 v1 §1 三方向但內容重寫）：**

- Contract A：資料層 → pipeline 層的單向消費契約（DF specifies, UD consumes）
- Contract B：pipeline 層 → UI 層的單向呈現契約（UD specifies, UX consumes）
- Contract C：資料層 ↔ UI 層的雙向 adapter 契約（兩邊都要對齊；前端 adapter 服從 DF schema，UX 反饋的 schema 需求在 §9 已三類分派）

---

# 2. Contract A 詳細（DF ↔ UD）

## 2.1 A.1 — dialogue_keys Map shape

**對應 D-NNN：** D-037（partial supersede DF v0.1 list of objects）+ CODEX C-01 / C-10 解決  
**Schema 來源權威：** `_design/DATA_FORMAT_SPEC.md` §4.2（v0.2 Map shape）  
**UD 消費端：** UD §2.11.4-5（dialogue_keys 寫入規範 + KEY lifecycle）  
**對應 SPEC 落地：** SPEC §5.2.3 欄位定義表新增 `dialogue_keys` 列（partial supersede via D-037）

### 2.1.1 Schema 完整形狀

`dialogue_keys` 是下游台詞檔（`08_dialogue_outputs/**/*.md`）frontmatter 內的 YAML Map block，每個 KEY 一個 entry：

```yaml
dialogue_keys:
  <KEY>:                            # Map key = 當前生效的 KEY；無獨立 key: 欄位
    line_index: int                 # 1-based；對應內文 KEY comment 出現順序
    speaker: <entity_id | null>     # C-* / R-* entity；動作描述 / 旁白為 null
    aliases: [<KEY history>]        # 改名歷史；首位永遠是預設名
    portrait: <A-portrait-* | null> # 句級立繪（v0.2 權威來源）
    bgm: <A-bgm-* | null>           # 句級 BGM
    sfx: [<A-sfx-* list>]           # 句級 SFX（list；空 [] 表示無）
    status: <status_enum>           # active | deprecated | deleted（D-037 + A.4）
    created_at: YYYY-MM-DD
    renamed_at: YYYY-MM-DD | null
    deleted_at: YYYY-MM-DD | null   # status=deleted 必填
    deprecated_reason: str | null   # status=deprecated 必填
    source_keys: [<KEY list> | null]# v2.0 校正 CC-04 — 句級收斂 lineage（僅 v02 收斂版用；v01 試寫 / SINGLE_ITER 為 null）
```

### 2.1.2 完整範例

```yaml
dialogue_keys:
  dlg.ch01.s03.l001:
    line_index: 1
    speaker: C-主角A
    aliases:
      - dlg.ch01.s03.l001
    portrait: A-portrait-主角A-anger
    bgm: A-bgm-tension-01
    sfx:
      - A-sfx-glass-break
    status: active
    created_at: 2026-05-22
    renamed_at: null
    deleted_at: null
    deprecated_reason: null

  boss_intro_line_2:                 # user-defined KEY（改名後）
    line_index: 2
    speaker: C-反派B
    aliases:
      - dlg.ch01.s03.l002             # 預設名移到 aliases
    portrait: A-portrait-反派B-default
    bgm: A-bgm-tension-01
    sfx: []
    status: active
    created_at: 2026-05-22
    renamed_at: 2026-05-23
    deleted_at: null
    deprecated_reason: null

  dlg.ch01.s03.l003:                  # 動作描述（speaker = null）
    line_index: 3
    speaker: null
    aliases:
      - dlg.ch01.s03.l003
    portrait: null                    # 動作描述通常不換立繪
    bgm: A-bgm-tension-01
    sfx: []
    status: active
    created_at: 2026-05-22
```

### 2.1.3 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF（schema owner）** | 定義 Map shape + 各欄位語義；§4.2 + §4.5 + §4.6（全 repo unique 機制）+ §11.1.2/11.1.3 parser 行為規範 |
| **UD（pipeline consumer）** | §2.11 KEY 寫入規範（分階段時機 + 命名規則 + 同場多版本共享規則 + alias 更新流程）；§4.8 KEY 生成 algorithm；§11.3 句子級 cross-ref 規則 |
| **UX（UI consumer）** | §11.3.5 details pane 分欄顯示（不暴露 raw YAML）；§7.9.2 UX-60~63 對照表；§11.6.11.7 / §11.3.4 內文 `<!-- KEY: -->` 顯示策略 |

### 2.1.4 Parser 必處理項（A.0）

對應 DF §11.1.2 + §11.1.3：

1. 解析 frontmatter `dialogue_keys` Map（YAML 本身保證 map key unique）
2. 解析內文 HTML comment `<!-- KEY: <key> -->`
3. 驗證 KEY ↔ map key 一致；不一致 → ERROR
4. 驗證 `line_index` 順序 ↔ 內文 KEY comment 順序一致；不一致 → ERROR
5. 驗證 KEY 命名符合 §4.1 預設語法或 user-defined 規則
6. 驗證 `aliases[0]` 為預設名格式
7. v0.2 新增驗證（D-037）：
   - `status` 在 enum `active / deprecated / deleted` 內
   - `status: deleted` 必有 `deleted_at`；`status: deprecated` 必有 `deprecated_reason`
   - `portrait` / `bgm`（若非 null）必須對應 valid A-* asset_id（cross-check `art_metadata`，見 A.3）
   - `sfx` list 各元素必須對應 valid A-sfx-* asset_id
   - 內文 `<!-- 立繪：A-... -->` / `<!-- BGM：A-... -->` 提示與 frontmatter 不一致 → **WARN**（非 ERROR；允許編輯期間暫時不同步）
8. 全 repo unique 集合：`⋃ (map_key) ∪ ⋃ (entry.aliases[*])` for all dialogue files；`status: deleted` 仍計入

### 2.1.5 v0.1 → v0.2 遷移路徑（DF 已對齊；本節僅備忘）

- v0.1 list of objects 寫法 → v0.2 Map shape（D-037）
- v0.1 `[DELETED]` prefix 寫法 → v0.2 `status: deleted` metadata（D-037 + C-10）
- DF §4.2 / §4.5 已直接 patch 為 v0.2 Map shape；既有 27 模板**無**現存 dialogue_keys block（dialogue 檔本身是 Phase D 才開始產），故無遷移工作

### 2.1.6 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §4.2 / §4.5 / §4.6 Map shape + lifecycle | ✓ v0.2 已落地 |
| UD §2.11.4 dialogue_keys block 規範 | ✓ v0.3 已用 mapping 寫法（C-01 解決） |
| UD §2.11.5 KEY lifecycle status enum | ✓ v0.3 已對齊三值 enum（D-037 + C-10 解決） |
| UD §11.3 句子級 cross-ref | ✓ v0.3 已對齊 `dialogue_keys.<X>.speaker` mapping |
| UX §11.3.5 details pane | ✓ v0.3 不暴露 raw YAML（D-037 對齊） |
| UX §7.9.2 UX-60~63 | ✓ v0.3 補完 |

### 2.1.7 Pending（無）

A.1 跨 spec 完全收斂。

---

## 2.2 A.2 — phase_log 完整 schema（基礎 + 5 新欄位）

**對應 D-NNN：** D-042（5 新欄位）+ CODEX C-07（schema 未收斂）+ C-09（SINGLE_ITER lineage 衝突）+ O-04 解決  
**Schema 來源權威：** `_design/DATA_FORMAT_SPEC.md` §3.1 ~ §3.4（v0.2 完整 entry schema）  
**UD 消費端：** UD §6（多場景並行）+ §10.6（手稿導入 phase_log 紀錄）+ §4.7（SINGLE_ITER algorithm 用 base_dialogue）  
**對應 SPEC 落地：** SPEC §5.4 phase_log schema 補完（partial supersede via D-042；既有 status 欄位升從「P-012 暫定」為正式）

### 2.2.1 Schema 完整形狀

`phase_log` 是每個 Instance 根目錄 `.protocol_version` 文件內的 list of entries；每個 skill 呼叫產一筆 entry：

```yaml
phase_log:
  - phase: <phase_name>                # bootstrap / create-world / ... / qa / export
    date: YYYY-MM-DD
    skill: /<skill_name>
    status: <status_enum>              # completed | in_progress | aborted
    import_source: <import_enum>       # agent_assisted | external_llm | null
    
    # === 既有欄位 ===
    created_entities: [<id>, ...]
    customizations: [...]              # bootstrap only
    scene_id: <S-id>                   # 下游 phase
    task_path: <path>                  # scene-task
    dialogue_paths: [<path>, ...]      # dialogue-write
    target_dialogue: <path>            # qa
    qa_report_paths: [<path>, ...]     # qa
    qa_decision: <enum>                # qa
    mode_tag: <enum>                   # dialogue-write
    abort_reason: <enum>               # status=aborted
    detail: <free text>                # status=aborted
    
    # === v0.2 新增 5 欄位（D-042）===
    entities_touched: [<id>, ...]      # 多場景並行 mutex
    iteration_count: int               # SINGLE_ITER 第幾次（v0.2 新；非 SINGLE_ITER 為 null）
    iteration_note: str                # 本次迭代意圖（v0.2 新；非 SINGLE_ITER 為 null）
    base_dialogue: <file_path>         # SINGLE_ITER lineage（v0.2 新；獨立欄位不重用 source_dialogues）
    conflict_resolutions: [<dict>, ...]# 手稿導入命名衝突 4 選項紀錄（v0.2 新；無衝突省略）
```

### 2.2.2 8 個關鍵欄位定義

| 欄位 | enum / 型別 | 寫入時機 / 規則 |
|---|---|---|
| `status` | `completed` / `in_progress` / `aborted` | 階段 1 寫 `in_progress`；階段 5 改為 `completed`；abort 改為 `aborted` + 必填 `abort_reason` + `detail`；省略視為 `in_progress`（保守解讀） |
| `import_source` | `agent_assisted` / `external_llm` / null | 該次 skill 的執行 context；null = 既有路徑；非 null 但 skill 不是 `/create-*` → ERROR |
| `entities_touched` | List[entity_id] | 多場景並行 mutex；⊇ `created_entities`；省略視為空 list；abort 因並行衝突時必填 |
| `iteration_count` | int（從 1 起算） / null | 僅 `mode_tag: SINGLE_ITER` 有意義；其他 mode_tag 為 null |
| `iteration_note` | free text / null | 同上；user 在 SINGLE_ITER 跟 agent 迴圈中討論修改方向摘要 |
| `base_dialogue` | file_path / null | 僅 SINGLE_ITER 且 `iteration_count >= 2` 必填；指向 `iteration_count - 1` 的檔；**不重用 SPEC 鎖定的 source_dialogues**；不允許 cycle（parser ERROR） |
| `conflict_resolutions` | List[dict] | 僅 `import_source != null` 有意義；每筆 dict schema：`{entity_id, decision (merge/overwrite/create-as-new/skip), new_entity_id (僅 create-as-new), resolved_at, detail}` |
| `source_dialogues` | List[path] / null（SPEC §5.2.3 鎖定）| **僅 --converge 產出的 v02 用**；列出本次收斂引用的 trial 路徑；非收斂版填 null 或省略；**SINGLE_ITER 不重用此欄位**（走 base_dialogue） |

### 2.2.3 完整範例（含 SINGLE_ITER lineage + 手稿導入衝突）

```yaml
phase_log:
  # 既有路徑（import_source 省略）
  - phase: bootstrap
    date: 2026-05-17
    skill: /init-project
    status: completed
    created_entities: []
    customizations: [...]

  - phase: create-world
    date: 2026-05-18
    skill: /create-world
    status: completed
    entities_touched: [W-rules, W-language, V]   # v0.2 多場景 mutex
    created_entities: [W-rules, W-language, V]

  # 手稿導入路徑（agent_assisted）+ 命名衝突 4 選項
  - phase: create-character
    date: 2026-05-19
    skill: /create-character
    status: completed
    import_source: agent_assisted               # v0.2
    skipped_stages: [1_diagnosis, 2_exploration]
    imported_manuscript_lines: 124
    entities_touched: [C-主角A, C-夥伴C, R-主角A-反派B]
    created_entities: [C-主角A, C-夥伴C_v2]      # 注意：因衝突解決 created 改為 _v2
    conflict_resolutions:                       # v0.2
      - entity_id: C-夥伴C
        decision: create-as-new
        new_entity_id: C-夥伴C_v2
        resolved_at: 2026-05-19
        detail: 手稿版跟既有 C-夥伴C 是不同角色
      - entity_id: R-主角A-反派B
        decision: skip
        resolved_at: 2026-05-19
        detail: 既有 R-* 比手稿版更新

  # SINGLE_ITER 第 1 次（無 base_dialogue）
  - phase: dialogue-write
    date: 2026-05-22
    skill: /dialogue-write
    status: completed
    scene_id: S-01-03
    dialogue_paths: [08_dialogue_outputs/CH01_S03_v01_iter1.md]
    mode_tag: SINGLE_ITER                       # v0.2 D-027
    iteration_count: 1                          # v0.2 D-042
    iteration_note: "第一次 SINGLE_ITER 起跑"     # v0.2 D-042
    base_dialogue: null                         # v0.2 D-042 — 第 1 次無 base

  # SINGLE_ITER 第 2 次（base_dialogue 指 iter1）
  - phase: dialogue-write
    date: 2026-05-23
    skill: /dialogue-write
    status: completed
    scene_id: S-01-03
    dialogue_paths: [08_dialogue_outputs/CH01_S03_v01_iter2.md]
    mode_tag: SINGLE_ITER
    iteration_count: 2                          # v0.2
    iteration_note: "user 要求主角A 第 2 句更冷峻；反派B 第 4 句更挑釁"  # v0.2
    base_dialogue: 08_dialogue_outputs/CH01_S03_v01_iter1.md          # v0.2

  # 並行衝突 abort（既有，補 entities_touched）
  - phase: dialogue-write
    date: 2026-05-24
    skill: /dialogue-write
    status: aborted
    scene_id: S-01-04
    abort_reason: parallel_conflict
    detail: phase_log.lock 等候 30 秒 timeout；另一個 /scene-task 正在執行
    entities_touched: [S-01-04, C-主角A]        # v0.2 給並行衝突排查用必填
```

### 2.2.4 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §3 完整 schema 定義 + §11.1.1 parser 行為（含 cycle 偵測 / abort_reason 必填驗證 / SINGLE_ITER 限制） |
| **UD** | §6 多場景並行用 `entities_touched`；§10.6 手稿導入用 `conflict_resolutions` + `import_source`；§4.7 SINGLE_ITER algorithm 用 `base_dialogue`；trust-level 限上游（A.8 詳） |
| **UX** | §11.1.6 三欄區 + §11.3.5 details pane 顯示 phase_log 摘要；§11.5.3 LOCKED 降級不擅自加 frontmatter 欄位（改寫進 09_e；D-046 #5）|

### 2.2.5 Parser 必處理項（A.0）

對應 DF §11.1.1：

1. 解析 8 個 enum 欄位 + 5 個 v0.2 新欄位
2. `status: aborted` 必有 `abort_reason` + `detail`，否則 ERROR
3. `import_source != null` 但 skill 不是 `/create-*` 系列 → ERROR
4. `iteration_count >= 2` 必有 `base_dialogue`；指向另一檔的 path
5. `base_dialogue` 鏈條不形成 cycle（parser ERROR）
6. `conflict_resolutions[*].decision` 在 enum 內；`decision: create-as-new` 必填 `new_entity_id`
7. `entities_touched` 各 ID 須符合 §7 entity_type_registry valid set
8. SINGLE_ITER lineage 不寫入 `source_dialogues`（避免與 --converge v02 衝突；C-09 解決）

### 2.2.6 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §3 完整 schema | ✓ v0.2 已落地 |
| UD §6.2 phase_log 寫入鎖 / §10.6 手稿 phase_log | ✓ v0.3 已對齊 5 新欄位 |
| UD §4.5 跨模式狀態總表 | ✓ v0.3 含 SINGLE_ITER + base_dialogue |
| UX §11.5 LOCKED 降級不擅加 frontmatter | ✓ v0.3 已修正（D-046 #5 / C-16 / O-03） |

### 2.2.7 Pending（無）

A.2 跨 spec 完全收斂。

---

## 2.3 A.3 — A-* SoT = `10_art_assets/` + 7 subtype

**對應 D-NNN：** D-041（SoT 為 `10_art_assets/`；廢「`_assets/registry.yaml`」）+ D-044（subtype 7 種）+ CODEX C-05（A-* registry SoT 衝突）+ C-13（subtype 範圍）解決  
**Schema 來源權威：** DF §5.1a（subtype registry）+ §5.2（目錄結構）+ §5.3（metadata frontmatter schema）  
**UD 消費端：** UD §13.2.1（v0.3 對齊：`10_art_assets/` per-file metadata，無統一 registry 檔案）  
**對應 SPEC 落地：** SPEC §5.1 entity 類型表新增 `A-*` 列（partial supersede via D-024 + D-044）

### 2.3.1 SoT 形式：per-file metadata，無統一 registry 檔

**v0.2 → v0.3 重大變動（D-041 + C-05）：**

- v0.2 寫法：`_assets/00_assets_registry.md` 或 `_assets/registry.yaml` 作為 A-* 驗證來源
- **v0.3 寫法：A-* 唯一權威 = `10_art_assets/` 目錄下 metadata files**；**不存在統一 registry 檔案**

理由（D-041）：
- 對齊既有 entity 模式（C-* / R-* 各自一份檔）
- A.0 parser 可平行掃描；無單檔寫入鎖瓶頸
- git diff 友善 — 改一個 asset 只 touch 一個檔
- 廢除「registry generated cache」這層抽象

### 2.3.2 目錄結構（v0.2 — 7 種 subtype）

```
10_art_assets/
├── 10_a_portrait_index.md          # A-portrait-* 索引
├── 10_b_background_index.md        # A-bg-* 索引
├── 10_c_cg_index.md                # A-cg-* 索引
├── 10_d_sfx_index.md               # A-sfx-* 索引（v0.2 新）
├── 10_e_bgm_index.md               # A-bgm-* 索引（v0.2 新）
├── 10_f_voice_index.md             # A-voice-* 索引（v0.2 新）
├── 10_g_ui_index.md                # A-ui-* 索引（v0.2 新；取代 v0.1 icon）
├── portraits/                      # A-portrait-* 個別 metadata（per character）
│   ├── 主角A.md
│   └── 反派B.md
├── backgrounds/                    # A-bg-* 個別 metadata（per scene / global）
├── cg/                             # A-cg-* 個別 metadata
├── sfx/                            # A-sfx-* per group（v0.2 新）
├── bgm/                            # A-bgm-* per mood / chapter（v0.2 新）
├── voice/                          # A-voice-* per character（v0.2 新；含該角色所有 voice line）
└── ui/                             # A-ui-* per UI 區塊（v0.2 新）
```

### 2.3.3 A-* ID 命名規則

```
A-<subtype>-<owner>-<state>
```

| 欄位 | 規則 |
|---|---|
| `<subtype>` | 7 種 enum：`portrait / bg / cg / sfx / bgm / voice / ui`（§2.3.4 subtype registry） |
| `<owner>` | 中文角色名 OR ASCII 識別字；對應 C-* / S-* / CH-* / global（依 subtype 不同；§2.3.5） |
| `<state>` | ASCII 小寫詞；如 `default / anger / day / 01 / line001` |

### 2.3.4 subtype registry（D-044）

7 種 `allowed_values`：`portrait / bg / cg / sfx / bgm / voice / ui`

4 種 `reserved_subtypes`（未來擴充，本輪不採）：`icon`（合併進 ui）/ `effect`（合併進 cg）/ `video`（reserved）/ `shader`（reserved）

**未來擴充 subtype 流程：** 從 `reserved_subtypes` 移除 + 加到 `allowed_values` + bump entity_type_registry version + master 裁決（D-NNN 紀錄）；A-\* 是 core + locked，user 不可在 Instance user_extensions 段改 subtype。

### 2.3.5 `<owner>` 對應規則

| subtype | `<owner>` 對應 | 範例 | parser 驗證 |
|---|---|---|---|
| `portrait` | **必對應 C-* entity** | `A-portrait-主角A-anger` ↔ `C-主角A` | 不對應 → WARN「孤立立繪」 |
| `bg` | **必對應 S-* / CH-* / global** | `A-bg-cafe-day` / `A-bg-global-rain` | 不對應 → WARN |
| `cg` | 對應 S-* / CH-* / global | `A-cg-finale01-default` | 不對應 → WARN |
| `sfx` | 通常 global，可選 S-* | `A-sfx-glass-break` | 無強制對應 |
| `bgm` | 通常 global / CH-* | `A-bgm-tension-01` | 無強制對應 |
| `voice` | **必對應 C-* + dialogue KEY**（句級 voice line） | `A-voice-主角A-line001` | 不對應 C-* → WARN；對應的 dialogue KEY 不存在 → WARN |
| `ui` | 通常 global | `A-ui-button-confirm` | 無強制對應 |

### 2.3.6 metadata frontmatter schema（DF §5.3）

每份 `10_art_assets/<subtype>/<group>.md` 的 frontmatter 含 `art_metadata` block；每個 A-* asset 一個 entry：

```yaml
art_metadata:
  - asset_id: A-portrait-主角A-anger
    display_name: 主角A 憤怒立繪
    subtype: portrait                     # v0.2 新欄位
    owner: C-主角A                        # v0.2 改名自 v0.1 character
    state_tags: [anger, hostile, combat]
    aliases: [A-portrait-主角A-anger]
    created_at: 2026-05-22
    renamed_at: null
    deleted_at: null
    status: active                         # 對齊 D-037 status enum：active|deprecated|deleted
    deprecated_reason: null
    dialogue_keys_ref: null                # 僅 subtype=voice 必填，指向 dialogue KEY
```

**強制禁止欄位（DF §5.7）：** 不允許 `file_path` / `url` / `source_image` / `binary_data` / `base64_*` 等指向實檔的欄位 → parser ERROR。實檔對應由外部系統（Unity / 引擎 / 等）自己處理。

### 2.3.7 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §5 完整 A-* schema；§5.1a subtype registry；§5.3 metadata frontmatter；§5.7 禁止欄位；§11.1.4 parser 行為 |
| **UD** | §13.2 A-* lifecycle 流程（建立 / 改名 / DEPRECATE / 刪除）；§13.3-§13.5 任務包 / dialogue 引用 A-* 的規則；§11.2.2 + §11.3.3 cross-ref 規則 |
| **UX** | §11.1.6a Asset Panel（7 subtype 分組）；§11.3.5 details pane「立繪 KEY」dropdown；§11.4 facet 第 8 維 A-* asset；§7.9.6 UX-76~80 |

### 2.3.8 Parser 必處理項（A.0）

對應 DF §11.1.4 + §11.1.5：

1. 識別 entity 類型 prefix `A-*` 加入 valid set
2. 掃描 `10_art_assets/**/*.md` 目錄；不存在統一 registry 檔（D-041）
3. 解析 frontmatter `art_metadata` block 各 entry
4. v0.2 subtype 驗證（D-044）：值在 `allowed_values` 7 種內；在 `reserved_subtypes` 內 ERROR
5. v0.2 owner 驗證（§2.3.5）：依 subtype 不同的 owner 對應規則
6. 強制禁止欄位偵測：`file_path` / `url` / `source_image` / `binary_data` / `base64_*` → ERROR
7. asset_id 全 repo unique（含 aliases；§4.6 機制延伸至 A-*）
8. v0.2 完成度行為（D-045）：parser 提供獨立 API `get_asset_completeness_by_subtype()`；**不納入** narrative `/status` expected entity manifest 比對

### 2.3.9 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §5 subtype registry + per-file metadata | ✓ v0.2 已落地 |
| UD §13.2.1 `10_art_assets/` per-file（廢 `_assets/registry.yaml`）| ✓ v0.3 已對齊（D-041 解決） |
| UX §11.1.6a 7 subtype 分組顯示 | ✓ v0.3 已對齊（D-044 解決） |
| UX §11.3.5 立繪 KEY dropdown | ✓ v0.3 已對齊 |

### 2.3.10 Pending（無）

A.3 跨 spec 完全收斂。

---

## 2.4 A.4 — i18n KEY lifecycle status enum

**對應 D-NNN：** D-037（status enum 取代 v0.1 `[DELETED]` prefix）+ CODEX C-10 解決  
**Schema 來源權威：** DF §4.5（KEY 生命週期 v0.2）+ §4.4（alias mapping）  
**UD 消費端：** UD §2.11.5（KEY lifecycle status enum 對齊）  
**對應 SPEC 落地：** 屬 A.1 dialogue_keys Map 內欄位；不獨立進 SPEC

### 2.4.1 status enum 三值定義

| status | 語義 | 對應行為 |
|---|---|---|
| `active` | KEY 當前生效；該句仍在 dialogue 內文中活躍 | 預設值；正常引用；export JSON / MD 含 |
| `deprecated` | KEY 仍存在於 frontmatter alias map（lookup 仍命中），但已不對應 dialogue 內文活躍句 | 保 alias mapping 不 break；外部 i18n lookup 舊 KEY 仍命中；export JSON `records[]` 仍含；export MD 視圖**不顯示**該句 |
| `deleted` | KEY 已永久棄用；frontmatter entry 仍保留作歷史；內文整段移除 | parser 排除主動引用；export JSON **預設不含**（除非 prompt 加 `include_deleted: true`） |

### 2.4.2 觸發場景

| 觸發場景 | agent 行為 |
|---|---|
| user 在 SINGLE_ITER 把句改寫但 KEY 保留 | `status: active` 維持；只改內文 + alias |
| user 在 SINGLE_ITER 刪句但 KEY 想保 alias | `status: deprecated` + `deprecated_at` + `deprecated_reason`；內文移除該句 |
| user 在 retcon / 修稿真刪 KEY | `status: deleted` + `deleted_at`；frontmatter entry **保留**（歷史 record）；內文移除 |

**核心原則：** 三條 status 路徑都**不改 `key` 值本身** — 對齊 D-037「不破壞 alias lookup」原則。

### 2.4.3 v0.1 → v0.2 寫法變動（兼容處理）

| v0.1 寫法 | v0.2 對應 |
|---|---|
| `deprecated: true` | `status: deprecated` |
| `deprecated: false`（隱含預設） | `status: active`（明示） |
| 內文 `<!-- KEY: dlg.xxx DEPRECATED -->` | **廢棄** — 不再用 comment 標 DEPRECATED；改用 frontmatter `status` 為單一權威 |
| `deprecated_reason: <text>` | 維持，並補 `deprecated_at` 時間戳 |
| `[DELETED]` prefix on key | **廢棄** — KEY 本身 immutable，lifecycle 由 metadata 表達 |

**A.0 parser 過渡期相容：** 允許 `deprecated: true` 作為 alias 處理（視為 `status: deprecated`），但寫檔時統一 emit 新 enum 寫法。

### 2.4.4 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §4.5 lifecycle status enum 三值 | ✓ v0.2 已落地 |
| UD §2.11.5 lifecycle 對齊 D-037 | ✓ v0.3 已對齊 |
| UX §7.9.2 UX-63 DEPRECATED KEY 視覺化 | ✓ v0.3 已對齊（灰色 + 刪除線） |
| Contract C.2（前端 UI dropdown / badge） | ✓ 本檔 §4.2 對應 |

### 2.4.5 Pending（無）

---

## 2.5 A.5 — qa_type 8 種 + extensible registry

**對應 D-NNN：** D-043（8 份 QA 全預設必跑 + 09_e final-gating）+ CODEX C-11（QA 數量與必要性未一致）解決；對齊 P-023（entity registry / qa_type registry）RESOLVED via DF Phase 3 §7+§8 + D-043  
**Schema 來源權威：** DF §6.2（qa_type enum 擴充）+ §8（qa_type registry Template/Instance）  
**UD 消費端：** UD §2.5（8 份 QA 必跑）+ §3.1~§3.9（8 份 QA 模板）+ §3.10（00_p 接點 schema 評估）  
**對應 SPEC 落地：** SPEC §5.2.4 qa_type enum 5→8 + 標可擴充（partial supersede via D-027 + D-043）；SPEC §12.7 QA 報告構成補 09_g/h/i + 標明 09_e 不屬於 QA（既有 M9 鎖定維持，但本輪明示）

### 2.5.1 qa_type 8 種 enum

| qa_type | 對應 09_* | v0.1 / v0.2 |
|---|---|---|
| `AI_FLAVOR` | 09_a AI 味檢查 | v0.1 既有 |
| `VOICE_CONSISTENCY` | 09_b 角色聲線一致性 | v0.1 既有 |
| `FORBIDDEN_WORD` | 09_c 禁用詞檢查 | v0.1 既有 |
| `INFO_CONTROL` | 09_d 資訊控制檢查 | v0.1 既有 |
| `GENRE_DRIFT` | 09_f 類型偏移檢查 | v0.1 既有 |
| `RHYTHM` | 09_g 節奏感檢查 | **v0.2 新（D-026 + D-043）** |
| `DRAMATIC_TENSION` | 09_h 對話張力檢查 | **v0.2 新（D-026 + D-043）** |
| `CROSS_SCENE_CONTINUITY` | 09_i 跨場一致性檢查 | **v0.2 新（D-026 + D-043）** |

**09_e final-gating 紀錄不在 QA pipeline，不入 registry**（屬 SPEC §12.7 M9 鎖定 + UD §3.5 範圍）。

### 2.5.2 QA pipeline 行為（D-043 — 全預設必跑）

- **並行檢查（同時跑 — 8 份）**
- **序列印出順序（D-043 + 上下游邏輯協同重排）：**
  1. 09_f 類型偏移檢查（最優先 — 類型跑掉影響其他判定）
  2. 09_d 資訊控制檢查（資訊洩漏先於 character 層）
  3. 09_h 對話張力檢查（張力強度標準依類型；09_f 之後跑）
  4. 09_b 角色聲線一致性（角色 OOC 判定）
  5. 09_g 節奏感檢查（節奏依賴聲線；09_b 之後）
  6. 09_a AI 味檢查（表層字面層）
  7. 09_c 禁用詞檢查（機械詞表比對）
  8. 09_i 跨場一致性檢查（最後 — 需前面所有 per-scene 結果交叉比對）
- **`qa_decision` 計算：** 8 份全 PASS → PASS；任一 FAIL → FAIL；人類保留違規亮點 → ARBITRATE_REQUIRED（不由 agent 自動產生，user 後續在 09_e 標）
- **FINAL gate logic：** 需 9 種 status 齊全（8 QA + 09_e final-gating）

### 2.5.3 qa_type registry 擴充機制（DF §8）

三層架構（Template / Instance / parser）：

```yaml
# qa_type_registry.template.yaml
version: 1
schema_version: data_format_spec_v0.3        # [v2.1 patch — 對齊 qa_type_registry.template.yaml 權威]

core:
  - qa_type: AI_FLAVOR
    template_path: 09_quality_assurance/09_a_ai味qa報告模板.md
    locked: true
  # ... 8 core qa_type

user_extensions:
  []   # user 加新 qa_type 在此

# 09_e final-gating 紀錄不在 QA pipeline，不入 registry
```

**user 新增 qa_type 流程：**
1. 在 Instance `qa_type_registry.yaml` 的 `user_extensions:` 段加新 entry
2. 在 `09_quality_assurance/` 加對應 09_x 模板檔
3. 對應 09_x 模板 frontmatter `qa_type` 值與 registry entry 對應
4. 由「QA 模組擴充協議」00_p（DF §8.7 接點 schema；本輪不寫實檔）規範新模板的結構要求

### 2.5.4 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §6.2 8 種 enum；§8 Template/Instance registry schema；§8.7 00_p 接點 schema；§11.1.6/11.1.8 parser 行為 |
| **UD** | §2.5 8 份 QA 並行 + 序列；§3.1~§3.9 8 份模板完整 algorithm；§3.10 00_p 評估 |
| **UX** | §6 QA Combined Report 顯示 8 份；§7.9（無 UX-N 直接對齊，但 UX §6 已含 8 份報告閱讀體驗）|

### 2.5.5 Parser 必處理項（A.0）

對應 DF §11.1.6 + §11.1.8：

1. `qa_type` valid set 擴為 8 種（基線 5 → 8）
2. `qa_type` set 變開放可擴充（registry 解析）
3. 啟動時讀 `<instance_root>/qa_type_registry.yaml`；不存在 → fallback Template + WARN
4. 載入 `core` + `user_extensions` 為 valid qa_type set
5. 對 QA 報告檔 frontmatter `qa_type` 驗證在 set 內
6. 對 `user_extensions[*].template_path` 驗證對應檔案存在於 `09_quality_assurance/`（不存在 ERROR）
7. 對應 09_x 模板 frontmatter `qa_type` 值與 registry entry 對應（不對應 WARN）
8. FINAL gate logic 補 9 種 status check（8 QA + 09_e）

### 2.5.6 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §6.2 / §8 8 種 + registry | ✓ v0.2 已落地 |
| UD §2.5 8 份必跑 + 序列順序 | ✓ v0.3 已對齊（D-043 解決） |
| UX §6 8 份 QA Combined Report | ✓ v0.3 已含 |
| 09_e 不屬 QA pipeline | ✓ SPEC §12.7 + DF §6.2 + UD §3.6 一致 |

### 2.5.7 Pending（無；但 00_p 實檔本輪不寫）

00_p 「QA 模組擴充協議」實檔屬 CODEX tier 2 邊界；本輪 DF §8.7 已給接點 schema，未來 CODEX tier 2 拿到 master 第四輪整合產物後再寫。

---

## 2.6 A.6 — mode_tag SINGLE_ITER + base_dialogue lineage

**對應 D-NNN：** D-027（mode_tag 增 SINGLE_ITER）+ D-028（partial supersede P-010 — 不新增 `/iterate-dialogue` skill）+ D-042（SINGLE_ITER lineage 用新 `base_dialogue` 欄位）+ CODEX C-09（SINGLE_ITER 用 `source_dialogues` 與 SPEC 鎖定衝突）解決  
**Schema 來源權威：** DF §6.1（mode_tag 擴充 SINGLE_ITER）+ §3.3d（base_dialogue 欄位）  
**UD 消費端：** UD §4.7（SINGLE_ITER mode algorithm）+ §4.5（跨模式狀態總表 v0.3 擴 SINGLE_ITER + base_dialogue）  
**對應 SPEC 落地：** SPEC §5.2.4 mode_tag enum 5→6（partial supersede via D-027）；SPEC §5.2.3 鎖定的 `source_dialogues` **不擴義** — SINGLE_ITER lineage 走 phase_log `base_dialogue` 獨立欄位

### 2.6.1 mode_tag 6 種 enum

| mode_tag | 用途 | v0.1 / v0.2 |
|---|---|---|
| `ORGANIZED` | 整理產出 | v0.1 既有 |
| `DRAFT_TRIAL` | 試寫 v01A/B/C | v0.1 既有 |
| `EXPERIMENTAL` | 破格 v01D | v0.1 既有 |
| `CONVERGENCE` | 收斂 v02 | v0.1 既有 |
| `FINAL_CANDIDATE` | 待 final | v0.1 既有 |
| `SINGLE_ITER` | **單版本迭代**（D-027 新增） | **v0.2 新** |

### 2.6.2 SINGLE_ITER vs CONVERGENCE 對 lineage 欄位的使用

**核心區分（C-09 解決）：**

| mode_tag | lineage 欄位 | 位置 | 鎖定語義 |
|---|---|---|---|
| `CONVERGENCE`（v02） | `source_dialogues: list[path]` | SPEC §5.2.3 frontmatter 下游欄位 | **僅 --converge 用**；列本次收斂引用的 trial 路徑 |
| `SINGLE_ITER` | `base_dialogue: str (file_path)` | `phase_log` entry 欄位（DF §3.3d） | 指上一輪迭代的檔案路徑 |

**為何不重用 `source_dialogues`：**
- SPEC §5.2.3 明確鎖定 `source_dialogues` 僅 `--converge` 產出的 v02 用
- 重用會造成「收斂 lineage vs SINGLE_ITER lineage 同欄位混語義」 — CODEX C-09 critical
- 採新獨立欄位 `base_dialogue` 解決 — SPEC §5.2.3 維持鎖定不變

### 2.6.3 SINGLE_ITER 寫入規則（DF §3.3b~d）

- `iteration_count: int`（從 1 起算）
- 第 1 次（`iteration_count: 1`）→ `base_dialogue: null`
- 第 N 次（N >= 2）→ `base_dialogue` 必填指向第 N-1 的檔
- 不允許 cycle：`base_dialogue` 鏈條不能形成迴圈（parser ERROR）
- `iteration_note: str` 紀錄本次迭代意圖（user 跟 agent 迴圈討論的修改方向摘要）

### 2.6.4 SINGLE_ITER skill 觸發（D-028）

- **不新增 `/iterate-dialogue` skill**（partial supersede P-010）
- 採 `/dialogue-write --single-iter` 旗標啟動
- 對應 UD §4.7 algorithm

### 2.6.5 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §6.1 mode_tag enum；§3.3d base_dialogue 欄位 schema；§11.1.6 parser 行為（cycle 偵測）|
| **UD** | §4.7 SINGLE_ITER algorithm；§4.5 跨模式狀態總表；§4.8 KEY 生成共用步驟（SINGLE_ITER 繼承 KEY） |
| **UX** | §7.9.3 UX-57~59（base_dialogue / 迭代版本預覽 / iter 鏈視覺化 / ≥3 次迭代建議跑 QA）；§11.3.3 Editor lineage timeline；§11.3.5 details pane「版本對照」 |

### 2.6.6 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §6.1 + §3.3d | ✓ v0.2 已落地 |
| UD §4.7 SINGLE_ITER algorithm | ✓ v0.3 已用 base_dialogue（非 source_dialogues） |
| UX §7.9.3 UX-57~59 | ✓ v0.3 已對齊 base_dialogue 欄位 |
| SPEC §5.2.3 source_dialogues 鎖定不擴義 | ✓ DF §3.3d / UD §4.7 / UX §7.9.3 均不擾動 |

### 2.6.7 Pending（無）

---

## 2.7 A.7 — JSON `manifest + records[]` 為 export 權威

**對應 D-NNN：** D-024（套版機制大幅縮減 — JSON+MD 雙吐）+ D-038（A1 prompt 流程）+ D-039（JSON schema 權威）+ CODEX C-03（L3 export 觸發模型互斥）+ C-04（JSON contract 形狀不一致）解決；對齊 P-024（JSON 中介格式）RESOLVED via D-039  
**Schema 來源權威：** DF §9（JSON 中介格式完整 schema）  
**UD 消費端：** UD §12（Layer 3 Export 流程；v0.3 大改）+ §12.6（D-039 對齊）+ §12.7（UD 六區降為 derived adapter view）  
**對應 SPEC 落地：** SPEC §13 / §14（既有 4 個 `/export-*` 不擴充；新增 §13a Layer 3 Export 章節描述 A1 prompt 流程 + 引用 L3_EXPORT_PROMPT_SCHEMA）

### 2.7.1 JSON 整體結構（DF §9.1）

```json
{
  "manifest": {
    "export_version": "1.0",
    "exported_at": "2026-05-22T14:30:00Z",
    "tool_version": "<agent 版本>",
    "instance_id": "<work-name>",
    "spec_version": "data_format_spec_v0.4",
    "stats": {
      "total_entities": 47,
      "total_dialogue_lines": 1532,
      "total_art_assets": 23,
      "by_entity_type": { "C": 8, "R": 6, "S": 15, "CH": 12, "A": 23, "...": "..." }
    },
    "entity_type_registry": { "... snapshot": "..." },
    "qa_type_registry": { "... snapshot": "..." }
  },
  "records": [
    { "record_type": "entity", "...": "..." },
    { "record_type": "dialogue_line", "...": "..." },
    { "record_type": "art_metadata", "...": "..." }
  ]
}
```

### 2.7.2 record_type 三類（DF §9.3-§9.6）

| record_type | 對應 SPEC | 對應 §11 cross-ref |
|---|---|---|
| `entity` | SPEC §5.2 上游 / 靜態檔（W / V / C / R / P / CH / S 上游） | UD §11.2.1 |
| `dialogue_line` | DF §4.2 `dialogue_keys` block 中一筆 entry | UD §11.3 |
| `art_metadata` | DF §5.3 `art_metadata` block 中一筆 entry（A-*） | UD §11.2.2 |

各 record schema 完整定義見 DF §9.4 / §9.5 / §9.6。

### 2.7.3 UD 六區降為 derived adapter view（D-039 + C-04 解決）

**v0.2 → v0.3 重大變動：**
- v0.2 UD §12.6.1 提案 6 區 top-level（`export_metadata` / `entities` / `assets` / `dialogues` / `qa_reports` / `phase_log`）為 export 權威
- **v0.3 拍板（D-039）：** JSON contract = DF `manifest + records[]` 權威；UD 六區降為 **derived adapter view**（runtime 從 records[] 算出來；非 export 權威）

**6 區 adapter view derivation 規則（UD §12.7.2 給 consumer 端參考實作）：**

| 6 區 | derivation |
|---|---|
| `export_metadata` | = `manifest`（直接映射） |
| `entities` | filter `records[]` where `record_type == "entity"` → mapping `<entity_id>: <record>` |
| `assets` | filter `records[]` where `record_type == "art_metadata"` → mapping `<asset_id>: <record>` |
| `dialogues` | filter `records[]` where `record_type == "dialogue_line"` → mapping `<key>: <record>` |
| `qa_reports` | filter `records[]` where `record_type == "entity"` 且 `source_file` 在 `09_quality_assurance/` 下；依 scene_id 分組 |
| `phase_log` | 從 manifest 或專用 record_type（屬 DF §9 擴充）抽出 |

### 2.7.4 JSON 不含項目（D-039 + UD §12.6.4）

- 多語對白本文（D-018 #2 維持不採；KEY 對應的翻譯由外部 i18n 處理）
- 實檔路徑或 URL（A-* 只存 metadata KEY；§2.3.6 + DF §5.7 強制禁止欄位）
- `_archive/` / `_design/` 目錄內容
- 純協議檔（`00_*.md`）— 工具規範不屬「資料」
- `status: deleted` 的 dialogue line（除非 prompt 加 `include_deleted: true`）

### 2.7.5 一對一映射規則（DF §9.7）

| SPEC §5.2 frontmatter | JSON output |
|---|---|
| 中文 header 5 欄 | `entity` record 的 `header` 子物件 |
| YAML 上游 3 欄（entities / depends_on / weight） | `entity` record 的 `frontmatter` 子物件 |
| YAML 下游 8 欄（scene_id / source_task / source_dialogue / source_dialogues / pipeline_state / mode_tag / qa_decision / qa_type） | `entity` record 的 `downstream_fields` 子物件 |
| 內文 `<!-- KEY: ... -->` | `dialogue_line` record 的 `key`（與 frontmatter dialogue_keys map key 校驗一致） |
| **frontmatter `dialogue_keys[<KEY>].portrait/bgm/sfx`**（v0.2 權威來源） | `dialogue_line` record 的 `portrait` / `bgm` / `sfx` 三欄 |
| `dialogue_keys` Map 中每筆 (key, entry) | 各自一筆 `dialogue_line` record |
| `art_metadata` block 每筆 entry | 各自一筆 `art_metadata` record |

**對齊規則：** JSON 是「frontmatter 的 1:1 結構化序列化」— 不做 transform / 不做 derive；transform 是外部 script 責任。

### 2.7.6 輸出檔位置 + git 管理（D-038 附帶第 3 項；v2.0 校正 CC-07）

- 建議檔名：`export/<instance_id>_<YYYYMMDD>_<HHMMSS>.json` + `export/<instance_id>_<YYYYMMDD>_<HHMMSS>.md`
- 位置：Instance root `export/` 目錄
- 加入 `.gitignore`（export 是衍生產物）
- 同次 export 同時產 JSON + MD 兩檔（D-024 雙吐）
- **export 跑完後 phase_log 不寫入任何 entry**（v2.0 master 第四輪 CC-07 校正 — 對齊 L3_EXPORT_PROMPT_SCHEMA §1.4 read-only constraints；原「補一筆 phase: export entry」supersede）
- **理由：** Layer 3 Export 為純 read-only contract；不視為 pipeline event；export 紀錄由外部 agent 在 chat 中回報（L3_EXPORT_PROMPT_SCHEMA §1.5 完成回報格式），不污染 phase_log

### 2.7.7 既有 4 個 `/export-*` 不擴充（D-038 + C-12 / O-02 解決）

| Skill | 行為 | 跟 Layer 3 Export 區分 |
|---|---|---|
| `/export-world` | 把 W/V 整合為 `view/世界觀.md`（DERIVED） | 給人讀 / 離線分享；不擴 JSON 輸出 |
| `/export-character` | 把指定角色 + 關係 + 弧線整合為 `view/角色_<name>.md` | 同上 |
| `/export-outline` | 把 P 主線整合為 `view/大綱.md` | 同上 |
| `/export-detailed-outline` | 把 05_b-05_e 整合為 `view/細綱.md` | 同上 |

**Layer 3 Export（JSON + MD 雙吐）不新增 skill** — 走 A1 prompt 流程（D-038；見 §3.3 B.3）。

### 2.7.8 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §9 完整 JSON schema；§9.7 frontmatter 一對一映射；§11.1.9 parser 提供「結構化資料」API 給 export agent 用 |
| **UD** | §12 Layer 3 Export 流程；§12.6 JSON contract；§12.7 UD 六區降為 derived view；§12.9 輸出位置 + git 管理 |
| **UX** | §11.6.11 Export Prompt panel UI（B.3 詳）；§11.6.11.7 入口位置（4 處）|

### 2.7.9 Parser 必處理項（A.0）

對應 DF §11.1.9：

1. parser 不直接負責 export
2. 提供「結構化資料」API 給 export agent（屬上下游 UD-3）使用
3. API 形狀（建議，屬 ARCHITECTURE 範圍）：
   - `get_all_entities()` → list of entity records
   - `get_all_dialogue_lines()` → list of dialogue_line records（按 KEY 排序）
   - `get_all_art_metadata()` → list of art_metadata records
   - `get_manifest_snapshot()` → manifest 物件（含 registry snapshots）
4. 對應 §9 JSON output schema 一對一映射

### 2.7.10 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §9 `manifest + records[]` 權威 | ✓ v0.2 已落地 |
| UD §12.6 JSON contract = DF | ✓ v0.3 已對齊（D-039 解決） |
| UD §12.7 六區 derived | ✓ v0.3 已對齊（取代 v0.2 §12.6.1 提案） |
| UX §11.6.11 不消費 JSON / 用 derived view | ✓ v0.3 已對齊（前端不直接處理 records[]） |
| 既有 4 /export-* 不擴 JSON | ✓ D-038 + UD §12.10 + UX §11.1.7 已對齊 |

### 2.7.11 Pending（無）

---

## 2.8 A.8 — trust-level 限上游 /create-* 路徑

**對應 D-NNN：** D-031（手稿導入路徑分支 — agent_assisted / external_llm）+ D-038（細化 D-029 α「完全分離」邊界）+ CODEX C-08（trust-level 是否影響下游狀態未一致）解決  
**Schema 來源權威：** DF §3.3（`import_source` 欄位 enum）+ §3.3e（`conflict_resolutions`）  
**UD 消費端：** UD §10.3（v0.3 修正：trust-level 嚴格限上游）+ §10.5（entity 命名衝突 4 選項處理）  
**對應 SPEC 落地：** SPEC §5.4 phase_log schema 補 `import_source` 欄位（屬 A.2 範圍；本條獨立說明 trust-level 邊界）

### 2.8.1 trust-level 嚴格邊界（v0.3 修正 C-08）

**重要原則：** `--trust-level` 參數**只在上游 `/create-*` skill 跳階段路徑下有效**，**不影響下游 `/scene-task` / `/dialogue-write` / `/qa` pipeline_state**。

下游台詞 pipeline 永遠走標準 DRAFT → QA → REVIEW → FINAL，**不允許**手稿導入跳過 QA 直接進 `DIALOGUE_FINAL`。

| 參數值 | 適用情境 | 對上游 `/create-*` 寫檔的行為 | 對下游 pipeline 影響 |
|---|---|---|---|
| `--trust-level=agent_assisted` | user 已在外部用 agent 工具編輯過手稿；品質可信 | 寫檔後實體 `狀態: DRAFT`（與 standard 路徑一致）；STRONGLY_PREFERRED 缺漏標 TODO；phase_log 紀錄 `import_source: agent_assisted` | **無** — 下游永遠跑完整 QA |
| `--trust-level=external_llm` | user 從外部 LLM 直接得到，未經審 | 寫檔後實體 `狀態: DRAFT`（與 agent_assisted 同等級）；phase_log 紀錄 `import_source: external_llm` + `recommended_followup: "建議跑 /iterate-* 補洞"` | **無**（同左） |

### 2.8.2 兩條 trust-level 路徑的實質差別（UD §10.3 v0.3 重新對齊）

| 差別維度 | agent_assisted | external_llm |
|---|---|---|
| 上游實體寫檔後狀態 | DRAFT（同 standard） | DRAFT（同 standard） |
| 上游實體升 REVIEW 條件 | user 手動審查通過 | user 手動審查通過 |
| phase_log `import_source` 值 | `agent_assisted` | `external_llm` |
| phase_log `recommended_followup` | null | `"建議跑 /iterate-* 補洞"` |
| 對下游 dialogue pipeline 影響 | **無**（下游永遠跑完整 QA） | **無**（同左） |
| 對下游 pipeline_state 影響 | **無**（不可跳 QA） | **無**（同左） |

### 2.8.3 三條 agent 禁止行為（UD §10.3）

- agent 不得依 `import_source: agent_assisted` 把下游 dialogue 升 `DIALOGUE_FINAL`
- agent 不得依 `import_source: agent_assisted` 跳過 §2.5 的 8 份 QA 必跑流程
- agent 不得把 trust-level 解讀為「品質 gate 豁免」— trust-level 只記錄資料來源，不改變 pipeline 規則

### 2.8.4 D-029 α「完全分離」的細化（D-038 + C-03 解決）

- v0.2 解讀：「前端不執行 agent，但可執行 local CLI」
- **v0.3 拍板（D-038）：** 收緊為「**前端不執行任何 agent action / local CLI**」（即使是 non-LLM 的 local tool action 也不允許）

對應行為：
- 前端 web server **只做 viewer / editor**；不啟動 subprocess / 不 spawn child process / 不 import 任何 export-related backend module
- Export 動作的「執行」全在外部 agent（CC / CODEX / 本地 LLM）的 process 中發生
- 前端的「推送方式」三選項都是「**把 prompt 送出去**」，不是「**前端跑 export**」
- 對應 B.3 Export Panel + B.7 trust-level UI（無前端 UI 選 trust-level — 走外部 chat）

### 2.8.5 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §3.3 `import_source` enum；§3.3e `conflict_resolutions` schema；§11.1.1 parser 驗證 |
| **UD** | §10.3 trust-level 限上游邊界（v0.3 對齊 C-08）；§10.5 entity 命名衝突 4 選項；§10.7 與其他章節對齊聲明（trust-level 不影響下游 pipeline 規則） |
| **UX** | §7.9.1 UX-67（trust-level 選擇走外部 chat，不在前端 UI 選）；§11.6 複製指令按鈕；對應 B.7 |

### 2.8.6 Parser 必處理項（A.0）

對應 DF §11.1.1：

1. `import_source` enum 驗證在 `agent_assisted / external_llm / null` 內
2. `import_source != null` 但 skill 不是 `/create-*` 系列 → ERROR
3. `conflict_resolutions[*]` 僅 `import_source != null` 時有意義；驗證 schema 完整性

### 2.8.7 跨 spec 對齊狀態

| 接點 | 狀態 |
|---|---|
| DF §3.3 / §3.3e | ✓ v0.2 已落地 |
| UD §10.3 trust-level 嚴格限上游 | ✓ v0.3 已對齊（C-08 解決） |
| UD §10.7 對下游不影響聲明 | ✓ v0.3 已對齊 |
| UX §7.9.1 UX-67 不在前端 UI 選 | ✓ v0.3 已對齊 |
| Contract B.7（前端無 trust-level 選擇 UI） | ✓ 本檔 §3.7 對應 |

### 2.8.8 Pending（無）

---

# 3. Contract B 詳細（UD ↔ UX）

## 3.1 B.1 — UX-1~UX-80 全覆蓋（合併後 78 元件）

**對應 D-NNN：** D-046 #1+#2（UX-54~80 補表 + 合併重複項）+ CODEX C-06（UX marker 覆蓋缺口）解決  
**來源權威：** UD §7（UX-1~UX-53）+ UD §10/§11/§12/§13（UX-54~UX-80）+ UX §7.8（UX-1~53 對齊表）+ UX §7.9（UX-54~80 對照表 v0.3 新增）

### 3.1.1 對齊矩陣（合併後 78 元件）

依 D-046 #2 + UD §10.5.3 / §1.0.4 對齊聲明合併 UX-54+55、UX-64+65 為兩筆，淨增 25 筆（總 78 元件）。

| UD §N.x | UX 範圍 | UX §N.y 對齊 | 元件數 |
|---|---|---|---|
| §7.1 上游協議共通互動 | UX-1 ~ UX-6 | UX §7.8 | 6 |
| §7.2 00_e 世界觀協議 | UX-7 ~ UX-9 | UX §7.8 | 3 |
| §7.3 00_f 角色協議 | UX-10 ~ UX-13 | UX §7.8 | 4 |
| §7.4 00_g 大綱協議 | UX-14 ~ UX-17 | UX §7.8 | 4 |
| §7.5 00_h 細綱協議 | UX-18 ~ UX-22 | UX §7.8 | 5 |
| §7.6 00_l 關係協議 | UX-23 ~ UX-26 | UX §7.8 | 4 |
| §7.7 下游 00_k pipeline | UX-27 ~ UX-34 | UX §7.8 | 8 |
| §7.8 QA 報告 | UX-35 ~ UX-38 | UX §7.8 | 4 |
| §7.9 dialogue-write | UX-39 ~ UX-41 | UX §7.8 | 3 |
| §7.10 Canon delta | UX-42 ~ UX-45 | UX §7.8 | 4 |
| §7.11 多場景並行 | UX-46 ~ UX-49 | UX §7.8 | 4 |
| §7.12 跨節共通 | UX-50 ~ UX-53 | UX §7.8 | 4 |
| §10 手稿導入路徑 | UX-54+55（合併）/ UX-56 / UX-64+65（合併）/ UX-66~68 | UX §7.9.1 | 6 |
| §11 dialogue_keys + KEY UI | UX-60 ~ UX-63 | UX §7.9.2 | 4 |
| §11 SINGLE_ITER 迭代 | UX-57 ~ UX-59 | UX §7.9.3 | 3 |
| §11 entity ID + cross-ref UI | UX-69 ~ UX-71 | UX §7.9.4 | 3 |
| §12 Export 路徑 | UX-72 ~ UX-75 | UX §7.9.5 → §11.6.11 | 4 |
| §13 A-* lifecycle | UX-76 ~ UX-80 | UX §7.9.6 | 5 |
| **總計** | UX-1~UX-80 合併後 | **78 元件** | — |

### 3.1.2 [BLOCKED:UPSTREAM_DOWNSTREAM] 8 個（v0.3 已標記）

依 UX §7.9.7 統計 — 8 個元件具體 algorithm 或 UD §12 改寫等由上下游決：

| 元件範例 | 狀態 | 處理 |
|---|---|---|
| UPS-UX-37 09_e 表單 schema | PENDING | 屬 NS-NEW-1（UD §3.6.3 / §3.6.6 補；本輪不寫實檔） |
| UPS-UX-44 依賴樹狀圖 | UX §10.3 拍板「v0.2 不做」 | 不在本輪 scope |
| UPS-UX-72~75 Export 路徑 | RESOLVED via D-038（A1 prompt）| 已對齊 §11.6.11 |
| 其他 5 個 | 散在 §7.8 / §7.9 | 各自 BLOCKED 標記內已說明 |

### 3.1.3 對 UX-* 編號擴充的紀律

- 本輪 v0.3 covered UX-1 ~ UX-80（合併後 78 元件）
- 未來新增 UX 需求 → 沿用 UX-N+1 連號（不重編；新議題另寫）
- 重複合併不重新給編號（UX-54+55 維持兩編號名稱，只合併實作為一元件）

### 3.1.4 三邊責任分工

| 邊 | 責任 |
|---|---|
| **UD** | §7（53）+ §10/§11/§12/§13（27 新增）標 [UX] 標記 + 描述需求 |
| **UX** | §7.8 對齊 UX-1~53 + §7.9 對齊 UX-54~80（v0.3 新增） — 各對應 L1（純 Markdown 模板）+ L2（HTML 前端工具）兩層 |
| **Master** | 確認 78 元件對照表收斂；新編號擴充時走 master 拍板 |

### 3.1.5 Pending（無）

UX-1~UX-80 對照表完整覆蓋。

---

## 3.2 B.2 — Save race guard for LOCKED — 5 步流程

**對應 D-NNN：** D-040（LOCKED Save guard — Save 前重讀最新 header）+ CODEX C-15（LOCKED 編輯守門可被 Save / force overwrite 繞過）解決  
**來源權威：** UX §11.5.7 ~ §11.5.8（Save flow 修訂版 + LOCKED race modal）

### 3.2.1 為何需要 race guard

CODEX C-15 critical：原 v0.2 設計把 LOCKED 守門只放在「進入 Editor 前」入口，但 user 進入 Editor 時場景是 DRAFT、編輯期間外部 agent / VS Code / 另一分頁把 source 升 LOCKED 的情境真實存在，**留下 race window 讓 Save 覆寫最新 LOCKED**，違反 SPEC §16 文件狀態機規則。

D-040 拍板：**Save flow 必須在實際寫檔前重讀最新 source header**，若最新 `狀態=LOCKED` 則禁止 overwrite。

### 3.2.2 Save flow 修訂版（5 步）

```
User 點「💾 Save 全部」
   │
   ▼
Step 1：前端組 dirty diff（沿 §11.3.8 diff preview modal）
   │
   ▼
Step 2：User 在 diff preview modal 點「確認寫回」
   │
   ▼
Step 3：前端送 pre-flight 請求到本地 server：
   GET /api/scene/<id>/header  (回傳 frontmatter 最新狀態 + mtime checksum)
   │
   ├─── Step 3a：若最新 `狀態 != LOCKED`（DRAFT / REVIEW / DEPRECATED）：
   │       前端進 Step 4 正常 Save flow
   │
   └─── Step 3b：若最新 `狀態 == LOCKED`：
           前端**禁止 overwrite** → 跳 §3.2.3 LOCKED race modal
           → User 三選項處理 → flow 終止 / 另存 proposal / 取消
   │
   ▼
Step 4：前端送 Save 請求（含 mtime checksum，沿 §11.7.5 衝突偵測）
   │
   ▼
Step 5：Server 寫檔成功 → 200 / 衝突 → 409 → §11.7.6 conflict modal
```

**關鍵：** Step 3 是 D-040 race guard，**在 Step 4 mtime checksum 之前**先做 LOCKED 檢查。理由：
- mtime checksum 偵測「外部修改」但不分辨修改類型
- 若外部修改是「升 LOCKED」，前端不該即使 mtime 對齊也覆寫
- LOCKED race 比 mtime drift 嚴重 — 一個是內容衝突可由 user 選 reload，一個是狀態機破壞

### 3.2.3 LOCKED race modal — 三選項對話框

當 Step 3b 觸發（最新 `狀態=LOCKED`），前端跳 modal，三選項：

| 選項 | 行為 |
|---|---|
| **(A) 複製降級指令** | 走 UX §11.5.3 Z2 candidate α 流程 — user 切外部 chat 跑 frontmatter 改動 + 09_e 紀錄，回前端重來；本次編輯內容必須手動重輸（不會自動接續） |
| **(B) 另存為 DRAFT proposal** | 把本次編輯寫成新檔 `v02_proposal_<日期>.md`（DRAFT 狀態）；原 LOCKED v02.md 不動；user 之後可決定 promote / merge |
| **(C) 取消 — 留 Editor 不 Save** | 編輯內容留前端 state；user 自己決定下一步（可手動 copy paste 出去 / 等場景重新降級） |

**「另存 DRAFT proposal」(B 選項) 行為細節（UX §11.5.8.2）：**

```
前端送請求：
  POST /api/scene/<id>/save-as
  body: {
    target_path: "08_dialogue_outputs/CH01_S03/v02_proposal_2026-05-19.md",
    content: <editor 內容>,
    initial_status: "DRAFT",
    ...
  }
```

理由：新檔是 DRAFT 狀態的全新檔，**不違反 SPEC §16 升級限制**。

### 3.2.4 與 LOCKED 進入 Editor 守門（§11.5.1）的關係

- 進入 Editor 前守門：LOCKED 場景 Quick Actions 顯示「⚠ 此場景已 LOCKED」+ 複製降級指令按鈕；user 不能直接進 Editor
- Save race guard：user 進 Editor 時是 DRAFT/REVIEW，編輯期間外部把 source 升 LOCKED → Step 3 race guard 擋下

兩道守門互補，無重疊。

### 3.2.5 三邊責任分工

| 邊 | 責任 |
|---|---|
| **UD** | §6.3 場景狀態升級鎖（既有）；不主動定 Save flow（屬前端） |
| **UX** | §11.5.7-11.5.9 完整 5 步 flow + LOCKED race modal + B 選項「另存 proposal」schema |
| **Frontend adapter（屬 ARCH）** | `GET /api/scene/<id>/header` endpoint；`POST /api/scene/<id>/save` + mtime checksum；`POST /api/scene/<id>/save-as` for B 選項 |

### 3.2.6 Pending（無）

D-040 拍板完整對齊 UX §11.5.7-9；ARCHITECTURE frontend adapter endpoint 規格在本檔 Contract C + 階段 3 落地。

---

## 3.3 B.3 — Export Prompt panel UI

**對應 D-NNN：** D-038（L3 export A1 prompt 流程 + CC/CODEX + 4 附帶）+ CODEX C-03（L3 export 觸發模型互斥）+ C-12（不存在 skill 名稱）+ O-02（越界）解決  
**來源權威：** UX §11.6.11（Export Prompt panel UI；v0.3 新增）+ `_design/L3_EXPORT_PROMPT_SCHEMA.md`（contract 級，master 新建）

### 3.3.1 為什麼 Export 是特例（跟一般「複製指令」按鈕分開）

| 維度 | 一般 `CopyCommandButton`（§11.6.1~§11.6.10） | `ExportPromptPanel`（§11.6.11） |
|---|---|---|
| 複製內容 | 單一 skill command + context 摘要 | 完整 prompt contract（5 區塊 — 標題 + YAML 元資料 + 步驟 + 約束 + 完成回報） |
| 觸發方式 | 按鈕 one-click 直接複製 | 開 panel → 選 scope / formats / push mode → 預覽 → 複製 / 推送 |
| Push mode | clipboard only | **clipboard + POST endpoint**（推送方式可擴）|
| 目標 agent | claude-code / cowork 任意 chat | claude-code / CODEX APP / 本地 LLM endpoint / Claude API / OpenAI API（任何能讀 prompt 的） |
| 對應 skill | 多個 `/create-*`、`/dialogue-write`、`/qa` 等 | **無 skill** — L3 export 走 prompt contract 不走 skill（D-038 + D-031）|

### 3.3.2 Export panel 必要元件（沿 L3_EXPORT_PROMPT_SCHEMA §2.1）

```
┌─────────────────────────────────────────────────┐
│ Layer 3 Bundle Export                            │
├─────────────────────────────────────────────────┤
│ 範圍 / Scope：                                   │
│          ⦿ 全部 / Full repo                       │
│          ○ 僅大綱 / Outline only                  │
│          ○ 僅本場景 / Scene  [CH01_S03 ▼]        │
│                                                  │
│ 格式 / Formats：                                  │
│          ☑ JSON  ☑ MD  ☐ 含已刪除 KEY            │
│                                                  │
│ 輸出路徑 / Output：                               │
│          export/2026-05-19_full.{json,md}        │
│          [改路徑...]                             │
│                                                  │
│ 推送方式 / Push Mode：                            │
│          ⦿ 複製到 clipboard（預設）              │
│          ○ POST 到本地 LLM endpoint              │
│              URL: [____________________]         │
│              Auth: [Bearer __________]           │
│              Model: [llama3.1-70b____]           │
│              [測試連線]                          │
│          ○ POST 到 Claude API (TODO — Phase C+)  │
│          ○ POST 到 OpenAI API (TODO — Phase C+)  │
│                                                  │
│ [預覽 Prompt]   [複製 / 推送]                    │
└─────────────────────────────────────────────────┘
```

### 3.3.3 預覽 Prompt modal

點「預覽 Prompt」按鈕 → 中央 modal 顯示完整組裝後的 prompt（依使用者選項實時組）：含標題行 + YAML 元資料 + 執行步驟 5 條 + 約束規則 + 完成回報格式（依 L3_EXPORT_PROMPT_SCHEMA §1.1 5 區塊）。

### 3.3.4 「複製 / 推送」按鈕行為（依 push mode 動態變）

| Push mode | 按鈕 label | 行為 |
|---|---|---|
| `clipboard`（預設） | `[📋 複製 Prompt]` | 把組裝完成的 prompt 全文寫到 clipboard；toast「已複製，請貼到 Claude Code / CODEX APP」 |
| `local_llm_endpoint` | `[🚀 推送到 ${user-set-URL}]` | fetch POST 到 URL，body 為 `{ prompt, format: "json" }`；等回應 → 顯示「✓ 推送成功（含回應摘要）」或 30 秒超時「⚠ 已推送（無回應）」 |
| `claude_api`（TODO） | `[🚀 推送到 Claude API]` (disabled, tooltip「Phase C+ 啟用」) | — |
| `openai_api`（TODO） | `[🚀 推送到 OpenAI API]` (disabled, tooltip「Phase C+ 啟用」) | — |

### 3.3.5 推送方式 lifecycle（沿 L3_EXPORT_PROMPT_SCHEMA §4）

| 階段 | 推送方式 | 狀態 |
|---|---|---|
| Phase A.0 | clipboard | **必做**（v0.3 範圍） |
| Phase B 後 | POST 到本地 LLM endpoint（Ollama / vLLM / 自架） | **必做**（D-038 附帶第 2 項） |
| Phase C+ | POST 到 Claude API / OpenAI API（含 auth + retry） | 選做 |
| 未來 | webhook / 觸發 GitHub Action | 待議 |

### 3.3.6 Export panel 入口位置（4 處 — D-046 #4 + UX §11.6.11.7）

| 位置 | 按鈕 label | 預設 scope |
|---|---|---|
| §11.1.5 模組狀態 H Export 行 | `[📤 開啟 Export panel]` | type: "full" |
| §11.1.7 Module Navigation View Files 區 | `[📤 開啟 Export panel]` | type: "full" |
| §11.2.2 Scene Detail Quick Actions | `[📤 Export 本場景]` | type: "scene", scene_id: 當前 |
| §11.4.7 篩選結果區 | `[📤 Export 篩選結果（N 場）]` | type: "scene" 多選或 batch |

舊「複製 /export-* 指令」按鈕**全部移除**（依 D-046 #4 + C-12）。

### 3.3.7 D-029 α「完全分離」對齊（§11.6.11.6）

依 D-038 對 D-029 α 的細化：「完全分離 = 前端不執行任何 agent action / local CLI；local non-LLM tool action 也不採（仍需 terminal）」。

- Export panel **本身**只組 prompt + 複製 / POST — **不執行 export**
- 實際 export 由 user 切到 CC / CODEX / 本地 LLM 跑
- POST 推送模式是「prompt 直送 LLM endpoint」 — 仍是 LLM agent 在做事，**不是本地 CLI**

### 3.3.8 三邊責任分工

| 邊 | 責任 |
|---|---|
| **Master（L3_EXPORT_PROMPT_SCHEMA owner）** | Prompt schema 5 區塊定義；schema_version 管理；推送方式 lifecycle |
| **UD** | §12 Layer 3 Export 流程（A1 prompt 模式）；§12.4 接點需求；§12.10 既有 4 /export-* 不擴 JSON |
| **UX** | §11.6.11 Export panel UI（7 子節）；§11.6.11.7 入口 4 處；§7.9.5 UX-72~75 對齊 |
| **Frontend adapter（屬 ARCH）** | 不執行 export（D-029 α）；只負責 prompt 組裝 + POST endpoint（push mode `local_llm_endpoint` 時） |

### 3.3.9 Pending（無）

D-038 + L3_EXPORT_PROMPT_SCHEMA + UX §11.6.11 完整對齊。

---

## 3.4 B.4 — A-* Asset Panel — 7 subtype 獨立顯示

**對應 D-NNN：** D-045（A-* 不納入 narrative `/status`）+ D-044（7 subtype）+ CODEX C-14（A-* 完成度是否計入 /status 互相矛盾）解決  
**來源權威：** UX §11.1.6a（Asset Panel；v0.3 新增）

### 3.4.1 設計原則

依 D-045 拍板：**A-* 完成度不納入 narrative `/status` 整體完成度**（理由：大綱寫到一半時繪師才開工很正常，不該卡台詞 FINAL）。前端 Dashboard 仍要有獨立 panel 顯示 A-* 進度，但跟 narrative 完全分離。

### 3.4.2 7 subtype 分組顯示（依 D-044）

```
┌─────────────────────────────────────────────────────────────────┐
│ A-* 美術資產進度 / Asset Panel                                  │
│ ─── 獨立於 narrative 完成度（D-045）─── 整體 35%（87/247）       │
│                                                                  │
│ ┌─ portrait（立繪）─ ✓ 12 ◐ 4 ○ 8 ✗ 3 ─ 27 KEYs (52%)   ┐    │
│ ┌─ bg（背景）─────── ✓ 8  ◐ 2 ○ 15      25 KEYs (40%)   ┘    │
│ ┌─ cg（事件圖）───── ✓ 3       ○ 12      15 KEYs (20%)   ┐    │
│ ┌─ sfx（音效）────── ✓ 24 ◐ 5 ○ 36      65 KEYs (37%)   ┘    │
│ ┌─ bgm（背景音樂）── ✓ 6       ○ 8       14 KEYs (43%)   ┐    │
│ ┌─ voice（配音）──── ✗ 全部                0/85 KEYs (0%)  │    │
│ ┌─ ui（UI 文案）──── ✓ 6                  6 KEYs (100%)   ┘    │
│                                                                  │
│ [→ 進入 Asset Registry 完整視圖]                                 │
│ [📤 開啟 Export panel — 含 A-*（依 scope）]                     │
└─────────────────────────────────────────────────────────────────┘
```

**位置：** Project Dashboard 中，**在 §11.1.6 三欄區與 §11.1.7 模組導航之間**。理由：三欄區是 narrative 卡點 / pending；本 panel 是平行的 asset 維度資訊，跟 narrative 並列但概念分離。

### 3.4.3 子表 — A-* KEY 詳細展開（§11.1.6a.1）

點某 subtype 展開後顯示每個 KEY 一行：

| 欄位 | 內容 |
|---|---|
| KEY | A-* asset_id |
| Owner | 對應 C-* / S-* / CH-* / global（依 §2.3.5 規則） |
| State | `✓ 完成` / `◐ 製作中` / `○ 未啟動` / `✗ 缺檔` 四桶（v2.0 校正 CC-01：從 `10_art_assets/<subtype>/<group>.md` 的 `art_metadata[*].status` 反查；採 DF subtype/group canonical 模型）|
| 覆蓋 | 動態反查「該 KEY 被多少場景引用」（從 `dialogue_keys.<KEY>.portrait/bgm/sfx` 反查；D-037 對齊）|

**⚠ 缺檔警示（UPS-UX-70 對應；v2.0 校正 CC-01）：** 若某 KEY 被引用但 `10_art_assets/<subtype>/<group>.md` 內 `art_metadata` 不含對應 asset_id，badge 變紅 ⚠ + 顯示「✗ 缺檔」+ 引用場景數。

**v2.0 校正 CC-01 — A-* canonical 檔案形狀為 DF subtype/group 模型：** v2.0 草版 §3.4.3 + §4.5.2 + UX §11.1.6a 寫 `10_art_assets/<key>/metadata.md` 三種混在 spec 中。CODEX (d) 識出 master 採 DF subtype/group 為 canonical。詳見 Contract A.3（§2.3.2 目錄結構：`portraits/<character>.md` per character，`sfx/<group>.md` per group 等）。

### 3.4.4 與 §11.1.4/5 narrative 完成度的分工

| 維度 | §11.1.4/5 narrative | §11.1.6a A-* asset |
|---|---|---|
| 對象 | W/V/C/R/P/CH/S（7 entity types） | A-* 美術資產（7 subtype） |
| 完成度 | 「整體 58%」**包含**所有 narrative entity | 「整體 35%」**僅** A-* — 跟 narrative 完全獨立 |
| 影響 FINAL gate | ✓ — REVIEW gate（A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5）全部要求 | **✗**（D-045）— A-* 缺漏不阻塞 dialogue FINAL |
| Source of truth | source markdown frontmatter / 內文 | `10_art_assets/` registry（D-041） |

> **（D-075 doc-sync 指標）：** 上表「W/V/C/R/P/CH/S（7 entity types）」為 v1.0 基底敘事 entity 集；`W-style`（D-055）/ `ORG`（D-071/D-074）為後加 opt-in 型別，present 時亦計入 narrative 完成度。entity 型別權威見 `entity_type_registry`（現 11 種 core）；本表計數為歷史框架，不重寫。

### 3.4.5 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §5.6 A-* 完成度計算（獨立公式）；§11.1.4 parser 提供獨立 API `get_asset_completeness_by_subtype()` |
| **UD** | §13.10 與 narrative `/status` 分工聲明 |
| **UX** | §11.1.6a 完整 Asset Panel UI；§11.1.6a.1 子表；§11.1.6a.2 跟 narrative 分工說明；§11.1.6a.3 對齊 D-NNN |
| **Frontend adapter** | endpoint `GET /api/assets?scope=...` + `GET /api/assets/<id>/usage`（NS-2 + UPS-UX-80 反查 query） |

### 3.4.6 Pending

| Pending | 來源 | 處理 |
|---|---|---|
| `GET /api/assets/<id>/usage`「該 KEY 被多少場景引用」反查 query | NS-2（UX §9.2）/ UPS-UX-80 | △ PARTIAL — schema 已定，query API endpoint 由階段 3 ARCHITECTURE 補 |

---

## 3.5 B.5 — 8 QA execution order UI 對齊

**對應 D-NNN：** D-043（8 份 QA 全預設必跑 + 09_e final-gating）+ CODEX C-11 解決  
**來源權威：** UD §2.5.3（v0.3 序列順序）+ UX §6（QA 8 份報告閱讀體驗 + 彙整版）

### 3.5.1 8 QA 序列印出順序（D-043 + 上下游邏輯協同重排）

UI 必須**完整呈現 8 份報告**，按下列順序顯示（並行檢查但序列印出）：

1. 09_f 類型偏移檢查（GENRE_DRIFT）— 最優先
2. 09_d 資訊控制檢查（INFO_CONTROL）
3. 09_h 對話張力檢查（DRAMATIC_TENSION）— v0.2 新
4. 09_b 角色聲線一致性（VOICE_CONSISTENCY）
5. 09_g 節奏感檢查（RHYTHM）— v0.2 新
6. 09_a AI 味檢查（AI_FLAVOR）
7. 09_c 禁用詞檢查（FORBIDDEN_WORD）
8. 09_i 跨場一致性檢查（CROSS_SCENE_CONTINUITY）— v0.2 新；最後

**理由邏輯（UD §2.5.3）：**
- 09_f 最優先 — 類型偏移影響其他判定基準
- 09_h 在 09_f 之後 — 不同類型的張力強度標準不同
- 09_g 在 09_b 之後 — 角色聲線決定句子長短偏好
- 09_i 最後 — 需要所有 per-scene QA 結果交叉比對

### 3.5.2 QA Combined Report layout（UX §6.3）

UI 必須提供「彙整版」呈現所有 8 份 + 09_e final-gating 段：

```
# QA Combined Report — S-01-03
## 下一步 / Next Fix
## 總體 Badge（綠 / 黃 / 紅）
## Required Context（6 子分區）
## 各模板狀態總覽（8 行；qa_type / 狀態 / 命中數）
## 詳細 Findings（按 severity 排序）
```

### 3.5.3 qa_decision 計算規則

- **PASS：** 8 份全 PASS
- **FAIL：** 任一份 FAIL
- **ARBITRATE_REQUIRED：** 人類保留違規亮點（不由 agent 自動產生，user 在 09_e 標）

### 3.5.4 FINAL gate logic

FINAL gate 需 9 種 status 齊全（8 QA + 09_e final-gating 紀錄）。前端顯示 FINAL gate 進度時要 9 格 checklist。

### 3.5.5 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §6.2 8 種 qa_type enum；§8 registry |
| **UD** | §2.5.3 並行 + 序列順序；§3.1~§3.9 8 份模板完整 algorithm |
| **UX** | §6 各 QA 模板閱讀體驗 + §6.3 彙整版；§6.5 跟 §11.2.10 QA finding modal 關係 |

### 3.5.6 Pending（無）

---

## 3.6 B.6 — KEY status enum dropdown / badge

**對應 D-NNN：** D-037（KEY lifecycle status enum）  
**來源權威：** UX §7.9.2 UX-60~63（dialogue_keys + KEY UI）+ §11.3.5 details pane

### 3.6.1 UI 元件規範

| 元件 | 行為 |
|---|---|
| **KEY metadata 顯示**（§11.3.5）| 不顯示 raw YAML；改顯示「KEY: dlg.ch01.s03.l001 / 說話者: 主角A / 立繪: A-portrait-主角A-default / status: active」分欄 |
| **內文 `<!-- KEY: -->` 顯示策略**（§11.2.9 / §11.3.4）| 預設**隱藏** comment（純讀人類友善版）；hover 該行可顯示 KEY；切換「顯示 KEY」按鈕 toggle 全文 KEY 顯示 |
| **rename KEY 按鈕**（§11.3.5）| 不在 textarea 直接編 KEY；改在 details pane 提供「rename KEY」按鈕 → 開 modal 輸入新 KEY + 自動把舊 KEY 加入 aliases |
| **DEPRECATED KEY 視覺化**（§11.2.9 / §11.3.4） | 灰色 + 刪除線；details pane 顯示 `status: deprecated / deprecated_reason / deleted_at` |

### 3.6.2 status 三值的 UI 對應

| status | UI 視覺 | 互動 |
|---|---|---|
| `active` | 正常字色；無 badge | 可編輯 / 可 rename |
| `deprecated` | 灰色 + 刪除線；橘色 ⚠ badge「DEPRECATED」 | 可 hover 顯示 `deprecated_reason`；不主動推升 active |
| `deleted` | 預設隱藏；切「顯示已刪除」toggle 才顯示；紅色 ✗ badge「DELETED」 | hover 顯示 `deleted_at`；不可編輯 |

### 3.6.3 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §4.2 / §4.5 schema（A.1 + A.4） |
| **UD** | §2.11.4 雙軌規範；§2.11.8 [UX] 標記 UX-60~63 |
| **UX** | §7.9.2 對照表；§11.3.4-5 編輯介面 + details pane |

### 3.6.4 Pending（無）

---

## 3.7 B.7 — trust-level 限上游 — 無前端 UI 選

**對應 D-NNN：** C-08（trust-level 是否影響下游 — 嚴格限上游）+ D-038（D-029 α 細化）  
**來源權威：** UX §7.9.1 UPS-UX-67（trust-level 選擇走外部 chat，不在前端 UI 選）

### 3.7.1 UI 規範

| 規則 | 內容 |
|---|---|
| 前端**不**提供 trust-level 選擇 UI | 對應 D-029 α + D-038 細化（前端不執行 agent / local CLI） |
| trust-level 選擇走外部 chat | user 在 CC / CODEX 內跑 `/create-* --trust-level=agent_assisted` 或 `--trust-level=external_llm` |
| 前端「複製指令」按鈕（§11.6）內含 trust-level 提示 | 提示 user：「請指定 trust-level： --trust-level agent_assisted / external_llm」 |
| trust-level 結果回到前端的顯示 | `/status` 內可加「最近導入」段顯示 `import_source: agent_assisted | external_llm`；§11.1.6 三欄區「最近導入」卡 |

### 3.7.2 trust-level 不在前端的理由（再確認）

- D-029 α「完全分離」 + D-038 細化：前端不執行任何 agent action / local CLI
- trust-level 是「agent 跑 `/create-*` 時 user 給的 context flag」 — 屬 agent skill 範圍
- 前端只是 viewer / editor — 不啟動 agent，因此不選 trust-level

### 3.7.3 三邊責任分工

| 邊 | 責任 |
|---|---|
| **UD** | §10.3 trust-level 限上游邊界；§10.5 entity 命名衝突 4 選項 |
| **UX** | §7.9.1 UX-67 對齊；§11.6 通用「複製指令」按鈕含 trust-level 提示文字 |

### 3.7.4 Pending（無）

---

## 3.8 B.8 — Conflict modal — entity 命名衝突 4 選項

**對應 D-NNN：** D-033（entity 命名衝突 4 選項 — merge / overwrite / create-as-new / skip）+ D-046 #5 + CODEX 議題 v0.2-D 衝突 merge UI [TBD-UX-CONFIRM]  
**來源權威：** UX §7.9.1 UPS-UX-66（衝突偵測表呈現）+ §11.7.6 Conflict Modal 延伸支援

### 3.8.1 4 選項定義（D-033）

| decision | 行為 |
|---|---|
| `merge` | 把手稿版內容併入既有 entity；entity_id 不變；agent 智能 merge |
| `overwrite` | 用手稿版完全覆蓋既有 entity；entity_id 不變 |
| `create-as-new` | 手稿版作為新 entity，agent 自動產 new_entity_id（如 `C-夥伴C_v2`）；既有 entity 不動 |
| `skip` | 拒絕導入該 entity；既有 entity 不動；對應的 created_entities **不出現**該 ID |

### 3.8.2 Conflict modal layout（§11.7.6 延伸）

```
┌──── entity 命名衝突 — 4 選項處理 ─────────────────┐
│                                                     │
│ ⚠ 偵測到衝突：手稿中 entity `C-主角A` 跟既有 entity │
│   `C-主角A`（最後更新 2026-05-15）同名。            │
│                                                     │
│ 既有版本摘要（按 hover 查看）：                      │
│   - 聲線：克制、短句、強潛台詞                       │
│   - 性格：內向、責任感重                             │
│                                                     │
│ 手稿版本摘要：                                       │
│   - 聲線：（手稿描述）                               │
│   - 性格：（手稿描述）                               │
│                                                     │
│ 選擇處理方式：                                       │
│ [📋 複製 merge 指令]                                 │
│ [📋 複製 overwrite 指令]                             │
│ [📋 複製 create-as-new 指令]                         │
│ [📋 複製 skip 指令]                                  │
│                                                     │
│ [關閉 modal]                                        │
└─────────────────────────────────────────────────────┘
```

**注意：** 前端**不**直接執行 merge / overwrite 等動作（D-029 α）。modal 內按鈕複製對應 trust-level + decision 的指令到剪貼簿，user 切外部 chat 跑 agent 處理。

### 3.8.3 conflict_resolutions 紀錄（phase_log 寫入）

Agent 處理完每個衝突後，phase_log 寫入 entry：

```yaml
conflict_resolutions:
  - entity_id: C-主角A
    decision: merge
    resolved_at: 2026-05-19
    detail: 手稿版聲線描述併入既有聲線卡的「進階性格」段
  - entity_id: C-夥伴C
    decision: create-as-new
    new_entity_id: C-夥伴C_v2
    resolved_at: 2026-05-19
    detail: 手稿版跟既有 C-夥伴C 是不同角色
```

### 3.8.4 三邊責任分工

| 邊 | 責任 |
|---|---|
| **DF** | §3.3e `conflict_resolutions` schema |
| **UD** | §10.5 4 選項處理 algorithm；§10.6 phase_log 紀錄擴充 |
| **UX** | §7.9.1 UX-66 對齊；§11.7.6 Conflict Modal 延伸 |

### 3.8.5 Pending

| Pending | 來源 | 處理 |
|---|---|---|
| 衝突偵測表呈現的具體欄位（既有 vs 手稿 diff 顯示細節）| UPS-UX-66 / UD §9.2.4 [TBD-UX-CONFIRM] | △ PARTIAL — 屬 UX specialist 後續細化（D-046 UX patch 範疇）；本輪 UX §11.7.6 框架已收，diff 顯示細節 v0.3 不完全展開 |

---

# 4. Contract C 詳細（DF ↔ UX）

Contract C 是 DF 資料形狀 ↔ UX 前端呈現的 adapter 契約。前端 server.py（frontend adapter）讀 DF 資料後 derive UI 用的 view；UX 反饋的 schema 需求在 UX §9 已三類分派（22 schema / 9 query-API-adapter / 2 upstream algorithm）。

本檔 §4 列出 5 條跨 DF/UX 的直接介面條目（不重複 §2 Contract A 的 schema 細節，只描述「資料如何 mapping 到 UI 元件」）。

## 4.1 C.1 — A-* subtype 7 種 → UI dropdown / chip

**對應 D-NNN：** D-044（7 subtype 正式擴大）  
**來源權威：** DF §5.1a（subtype registry）+ UX §11.1.6a / §11.3.5 / §11.4 facet 第 8 維

### 4.1.1 Mapping 規則

| DF 資料形狀 | UX UI 元件 | 位置 |
|---|---|---|
| `art_metadata[*].subtype` enum 7 種 | Asset Panel 7 區塊分組 | §11.1.6a |
| `art_metadata[*].subtype` | Editor details pane「立繪 KEY」dropdown 來源（subtype=portrait） | §11.3.5 |
| `art_metadata[*].subtype` | 搜尋 facet 第 8 維 A-* asset（subtype / owner / state 三層 sub-facet） | §11.4 |
| `art_metadata[*].subtype` | Conflict modal 顯示衝突 entity 的 subtype label | §11.7.6 |

### 4.1.2 UI 顯示規則

| subtype | 顯示中文 label | icon（建議）|
|---|---|---|
| portrait | 立繪 | 👤 |
| bg | 背景 | 🏞️ |
| cg | 事件圖 | 🎨 |
| sfx | 音效 | 🔊 |
| bgm | 背景音樂 | 🎵 |
| voice | 配音 | 🎤 |
| ui | UI 文案 | 🔘 |

reserved_subtypes（icon / effect / video / shader）不出現在 UI dropdown（D-044 + DF §5.1a parser ERROR）。

### 4.1.3 Pending（無）

---

## 4.2 C.2 — KEY status enum → UI dropdown / badge

**對應 D-NNN：** D-037（KEY lifecycle status enum）  
**來源權威：** DF §4.5 + UX §7.9.2 UX-63 + §11.3.5 details pane

### 4.2.1 Mapping 規則

| DF 資料形狀 | UX UI 元件 |
|---|---|
| `dialogue_keys.<KEY>.status` enum 三值 | Editor textarea + Preview 視覺呈現（§3.6.2 B.6）|
| `dialogue_keys.<KEY>.deprecated_reason` | details pane hover tooltip |
| `dialogue_keys.<KEY>.deleted_at` | details pane 顯示 |

### 4.2.2 UI 顯示規則（同 §3.6.2 B.6）

| status | UI 視覺 |
|---|---|
| `active` | 正常字色；無 badge |
| `deprecated` | 灰色 + 刪除線；橘色 ⚠ badge「DEPRECATED」 |
| `deleted` | 預設隱藏；切「顯示已刪除」toggle 才顯示；紅色 ✗ badge「DELETED」 |

### 4.2.3 Pending（無）

---

## 4.3 C.3 — JSON records[] → 前端不消費，用 derived view

**對應 D-NNN：** D-038（A1 prompt）+ D-039（records[] 為權威）+ D-029 α（完全分離）  
**來源權威：** DF §9 + UD §12.7（六區 derived view 規範）+ UX §11.8.3（server endpoint）

### 4.3.1 設計原則

依 D-029 α + D-038 細化：前端**不**直接消費 JSON export records[]。前端 server.py 從 source markdown 直接讀 → derive 各 UI 需要的 view，不經過 JSON export 中介層。

理由：
- JSON export 是「外部轉檔吃」的 contract（A.7）
- 前端 server.py 是「local viewer / editor」 — 直接讀 source markdown 更新即時
- 避免「user 改檔 → 跑 export → 前端讀 JSON」中介 step

### 4.3.2 Frontend adapter view derivation

前端 server.py 從 source markdown derive 出的 UI 用 view，包括：

| Frontend view | 來源 |
|---|---|
| Scene Queue 列表 | scan `08_dialogue_outputs/**/*.md` frontmatter |
| Scene Detail cockpit | 該 scene 的所有版本檔 frontmatter + dialogue_keys |
| Asset Panel 7 subtype 統計 | scan `10_art_assets/**/*.md` art_metadata |
| Project Dashboard 完成度 | DF §5.3 完成度公式 + Expected Entity Manifest |

**這些 view 跟 JSON `manifest + records[]` 是平行存在**：JSON 是 export 給外部吃；前端 view 是即時計算給 UI 用。兩者都從 source markdown derive，但 derivation 邏輯與 schema 不同。

### 4.3.3 Pending（無 — 但 frontend adapter endpoint 規格屬 ARCHITECTURE 範圍）

---

## 4.4 C.4 — phase_log new fields → /status & details pane

**對應 D-NNN：** D-042（phase_log 5 新欄位）  
**來源權威：** DF §3 + UX §11.1.6 三欄區 + §11.3.5 details pane

### 4.4.1 Mapping 規則

| phase_log 欄位 | UI 元件位置 | 顯示形式 |
|---|---|---|
| `import_source` | §11.1.6 三欄區「最近導入」卡 + /status 「最近導入」段 | label「agent_assisted」/「external_llm」+ 日期 |
| `entities_touched` | /status 多場景並行視覺化 + Editor lineage timeline | 該次 skill 呼叫期間讀寫的 entity ID list |
| `iteration_count` | Editor lineage timeline 顯示「iter N」 | UX §7.9.3 UX-58 對齊 |
| `iteration_note` | Editor details pane「版本對照」段 | UX §7.9.3 UX-57 對齊 |
| `base_dialogue` | Editor lineage chain 顯示「base_dialogue → v01A_iter1 → v01A_iter2」 | UX §7.9.3 UX-58 對齊 |
| `conflict_resolutions[*]` | Conflict modal 處理完後在 details pane 顯示衝突歷史 | UX §7.9.1 UX-66 對齊 |

### 4.4.2 Pending（無）

---

## 4.5 C.5 — A-* completeness → asset panel only, 不入 narrative status

**對應 D-NNN：** D-045（A-* 不納入 narrative `/status`）+ CODEX C-14 解決  
**來源權威：** DF §5.6 + UX §11.1.6a.2 跟 §11.1.4-5 分工

### 4.5.1 分工規則

| 維度 | narrative entity（§11.1.4-5） | A-* asset（§11.1.6a） |
|---|---|---|
| 完成度公式 | DF §5.3（既有，含 weight）| DF §5.6（v0.2 新獨立公式）|
| Parser API | `get_entity_completeness()`（既有）| `get_asset_completeness_by_subtype()`（v0.2 新；D-045）|
| 影響 FINAL gate | ✓ | **✗** |
| /status 顯示 | 「整體 58%」含 7 narrative entity 類型 | 不在 `/status` 整體完成度內；獨立 Asset Panel |

### 4.5.2 Mapping 規則

| DF 資料形狀 | UX UI 元件 |
|---|---|
| `get_asset_completeness_by_subtype()` 結果 | §11.1.6a Asset Panel 7 subtype 分組 + 各自百分比 |
| `art_metadata[*].state_tags`（v2.0 校正 CC-01：從 `10_art_assets/<subtype>/<group>.md` 反查；採 DF subtype/group canonical 模型）| Asset Panel 子表 State 欄位（✓ 完成 / ◐ 製作中 / ○ 未啟動 / ✗ 缺檔） |
| `dialogue_keys.<KEY>.portrait/bgm/sfx` 反查 | Asset Panel 子表「覆蓋」欄（該 KEY 被多少場景引用） |

### 4.5.3 Pending（無 — A-* 反查 query API 屬 NS-2，見 §3.4.6）

---

# 4a. Contract D 詳細（v2.1 新增 — D-047 issue_type_registry）

**Contract D 性質：** 三向契約（DF ↔ UD ↔ Phase B /create-* skill）— 跟 Contract A/B/C 屬於資料→消費單向 / pipeline→UI 單向 / 資料↔UI 雙向不同；Contract D 是「**registry schema（DF/共用）→ skill consume（UD/Phase B）→ frontend editor（UX/A.0F）**」三向對齊。

**對應 D-NNN：** D-047（master 第五輪拍板）

**來源權威：**
- `_design/registries/issue_type_registry.template.yaml` v0.1 — 權威 schema 範本（master 第五輪建）
- DECISIONS_LOG §6.9.2（D-047 拍板紀錄）
- UD §1.1-§1.5 — 5 個 /create-* skill 議題清單來源（partial supersede 留 Phase B 實作時處理）

## 4a.1 D.1 — issue_type_registry.yaml schema + Template/Instance 分層

### 4a.1.1 三層機制（對齊 entity_type_registry / qa_type_registry pattern）

```yaml
# issue_type_registry.template.yaml schema
version: 1
schema_version: data_format_spec_v0.3    # 借用 DF v0.3 既有 registry 通用 meta-schema

core:                                     # LOCKED 議題範本 — REQUIRED 議題 locked=true 禁 SKIP
  00_e_world:                             # /create-world — 10 user-facing 議題
    - id: 1                               # 1-base，10.N 對應 id N
      name: 世界類型快速分類
      required_level: REQUIRED            # REQUIRED / STRONGLY_PREFERRED / OPTIONAL
      locked: true                        # REQUIRED → true；其他 → false
      question_summary: "..."             # agent 提問腳本摘要
      protocol_ref: "UD §1.1.2 §10.1"     # UD 完整提問腳本對應位置
    # ... 10 entries
  00_f_character: [...]                   # /create-character — 8 議題
  00_g_outline: [...]                     # /create-outline — 6 議題
  00_h_detailed_outline: [...]            # /create-detailed-outline — 6 議題
  00_l_relationship: [...]                # /create-relationship — 6 議題
                                          # 拆分規則 NOT in registry（agent 階段 4 mechanic）

user_extensions:                          # user 加自訂議題（per skill）
  00_e_world:
    - id: 100                             # user 議題 id 從 100 起跳避免與 core 衝突
      name: 驚悚密度曲線
      required_level: STRONGLY_PREFERRED
      locked: false                       # user 加的議題永遠 locked=false
      question_summary: "..."
      protocol_ref: "user-defined"
  # ... per skill

core_overrides:                           # user 標 SKIP 既有 core 議題（只能標 locked=false 議題）
  00_e_world:
    - skip_id: 5                          # core[*].id 編號
      reason: "純愛主題，價值觀僅在後期擴充時考量"
  # ... per skill
```

### 4a.1.2 Template / Instance 分層（同 entity / qa registry pattern）

| 層 | 檔案 | 狀態 | bootstrap 行為 |
|---|---|---|---|
| Template | `_design/registries/issue_type_registry.template.yaml` | DRAFT v0.1（本輪建）| 不動 — Phase B/A.0F 編輯指向 Instance 端 |
| Instance | `<instance_root>/issue_type_registry.yaml` | 由 `/init-project` 從 Template 複製 | user 可編輯 user_extensions / core_overrides |

### 4a.1.3 議題定義邊界

| 維度 | 屬 registry | 不屬 registry |
|---|---|---|
| user-facing 議題（agent 向 user 問的問題） | ✓ core | — |
| user 自加 user-facing 議題 | ✓ user_extensions | — |
| user 標 SKIP 既有議題 | ✓ core_overrides | — |
| 拆分規則（agent 階段 4 寫檔 mechanic）| — | hardcode 在 /create-* protocol |
| frontmatter 規範（拆分規則內附）| — | DF / UD spec |
| 議題回答如何寫入分拆檔 | — | UD §1.x.2 §10.N agent 整理寫檔段 |

## 4a.2 D.2 — Phase B /create-* skill 讀 registry 動態構建議題清單

### 4a.2.1 啟動行為

Phase B 每個 /create-* skill 啟動時：

1. 讀 `<instance_root>/issue_type_registry.yaml`（若不存在從 Template fallback + WARN）
2. 對 skill 對應的 key（e.g., `/create-world` → `00_e_world`）取 core + user_extensions
3. 套用 core_overrides 過濾：
   - 對 `core_overrides[<skill>][*].skip_id` 中的 id：若對應 core entry `locked=true` → 忽略並 WARN「locked 議題 id=N 不可 SKIP，core_overrides 條目被忽略」
   - 若對應 core entry `locked=false` → 從議題清單中移除
4. 議題順序：先 core（依 id 升序）後 user_extensions（依 id 升序）
5. 對每個議題：
   - REQUIRED → 用 UD §1.0.4 跳階段路徑 REQUIRED 行為（拒絕跳階段 4 直到補齊）
   - STRONGLY_PREFERRED → 跳階段 4 允許但 phase_log 紀錄缺漏
   - OPTIONAL → 跳階段 4 允許不紀錄

### 4a.2.2 5 階段對話路徑（既有 /create-* skill 流程）

階段 2「探索 / 補洞對話」對議題逐項提問。Phase B 實作時讀 registry 的 `question_summary` 作為 opener，完整 agent 對話腳本仍從 `protocol_ref` 指向的 UD §1.x.2 §10.N 段拿。

### 4a.2.3 跳階段路徑（手稿導入）

跳階段路徑 agent 解析手稿 markdown structure，對每個 registry 議題抓取對應段；同 §4a.2.1 行為。

## 4a.3 D.3 — user_extensions / core_overrides 衝突處理 + locked 防 SKIP

### 4a.3.1 衝突類型 + parser 行為

| 衝突 | 行為 | Severity |
|---|---|---|
| user_extensions[*].id 與 core[*].id 重複 | parser ERROR：`user_extensions 議題 id={n} 與 core id={n} 衝突；user 議題 id 須 >= 100` | ERROR |
| user_extensions[*].id < 100 | parser ERROR：`user 議題 id 須 >= 100（避免與未來 core 議題擴充衝突）` | ERROR |
| user_extensions[*].locked = true | parser WARN：`user 加的議題 locked 應為 false；自動視為 false` | WARN |
| core_overrides[*].skip_id 對應 core entry locked=true | parser WARN：`locked 議題 id={n} 不可 SKIP；core_overrides 條目被忽略`；該議題仍出現在 skill 議題清單 | WARN |
| core_overrides[*].skip_id 不存在於 core | parser WARN：`core_overrides skip_id={n} 找不到對應 core 議題；條目被忽略` | WARN |
| skill key 不在 5 個合法 key（`00_e_world` / `00_f_character` / `00_g_outline` / `00_h_detailed_outline` / `00_l_relationship`）| parser ERROR | ERROR |

### 4a.3.2 locked: true 議題對應 D-047 拍板

Registry core 中 `locked: true` 議題對應 UD §1.0.4 跳階段路徑 REQUIRED 列；這些議題是 protocol 基底，user 不可透過 core_overrides 跳過。共 **15** 個（00_e: 4 / 00_f: 2 / 00_g: 3 / 00_h: 4 / 00_l: 2）。

## 4a.4 D.4 — A.0F frontend issue registry 編輯 UI 對齊

### 4a.4.1 Phase 範圍

- **A.0F alpha（A.0.10 後）：** 不做 issue registry UI（屬 real-data acceptance scope）
- **A.0F real-data acceptance（B.9 後）：** 加 issue registry 編輯 UI

### 4a.4.2 UI 元件需求（給 UX specialist Phase A.0F.x 設計參考）

| UI 元件 | 行為 | 對齊 |
|---|---|---|
| Skill 切換 tabs | 5 個 skill（00_e_world / 00_f_character / 00_g_outline / 00_h_detailed_outline / 00_l_relationship）| 對應 5 個 /create-* skill |
| 議題列表 | 顯示 core 議題（lock icon for locked=true / overridden 議題標灰）+ user_extensions 議題（user 標識）| 顯示 id / name / required_level chip |
| 議題詳細 panel | 顯示 question_summary / protocol_ref（連 UD 內文）| 不可編 core 議題；可編 user_extensions 議題 + 標 SKIP core 議題（限 locked=false）|
| 加 user 議題 | 表單：name / required_level / question_summary | id 自動分配 ≥ 100 + 撞 ID 偵測 |
| 標 SKIP core 議題 | 對 locked=false 議題加 SKIP toggle + reason 欄 | locked=true 議題禁 SKIP（disabled toggle）|
| Save | 寫回 `<instance_root>/issue_type_registry.yaml` | 走 LOCKED Save guard B.2 + parser refresh trigger |

### 4a.4.3 Pending（A.0F real-data acceptance 落地時細化）

- UX-XX（待 UX specialist 編號）：issue registry 編輯 panel 完整元件樹（推到 A.0F real-data acceptance Phase）

## 4a.5 Pending（Contract D — v2.1 sealed）

- **DF spec 端：** D-047 schema 細節（registry 通用 meta-schema 借自 DF v0.3；issue_type_registry 專屬欄位 id / required_level / locked / question_summary / protocol_ref 由 Contract D §4a.1 本契約定義；不擴 DF）
- **UD spec 端：** §1.1-§1.5 議題清單描述改為「core 議題範本參考」屬 Phase B 實作開始前處理（spec partial supersede 留下一輪 master / Phase B specialist 同步處理；不擋本 v2.1）
- **A.0 parser 端：** Phase A.X parser patch round 補實作（Stage 0 A.0.10 已不在此 scope；後續 round 加 `load_issue_type_registry()` + validate user_extensions / core_overrides 邏輯）

---

# 5. Master 強制介入議題清單（v1 保留 + v2.0 補增）

以下議題**任何 specialist 都不能單方面決定**，必須升級 master：

| 議題 | 為什麼要 master 介入 |
|---|---|
| canonical schema 5 欄位 header 改動 | 影響全 repo 既有 27 份檔案 |
| 上游 5 份協議 + 00_i / 00_j / 00_k 的「框架結構」改動 | 已通過 4 輪審查 |
| skill 清單增刪 | 影響 TASKS、ARCHITECTURE、文件導航 |
| REVIEW gate 數量或位置改動 | 影響 Phase 之間的可進入條件 |
| `_design/` 內 SPEC/ARCHITECTURE/TASKS 三份文件的章節結構 | 4 輪審查通過的成果 |
| **D-NNN 拍板結論的修訂 / 推翻**（v2.0 新增） | 屬 D-NNN 修訂走 supersede 機制（DECISIONS_LOG §7） |
| **三 specialist v0.3 patch 後的 schema 修訂**（v2.0 新增） | 屬 specialist 第三輪派工或 master 第五輪整合的決定範圍 |
| **L3_EXPORT_PROMPT_SCHEMA `schema_version` bump**（v2.0 新增）| 屬 master 文件權威 |
| **entity_type_registry / qa_type_registry core 段修訂**（v2.0 新增） | 屬 LOCKED core 操作 |

---

# 6. Pending 議題彙整（v2.0 — 對齊 D-037~D-046 後殘留）

依 UD §9.4 + UX §9.4 + DF §12.4 + DECISIONS_LOG §6.7.3 整理：本輪 v0.3 patch 完成後跨 spec 殘留 Pending 條目。

## 6.1 DF Pending（從 DF §12 整理）

DF v0.2 宣稱 0 master 裁決議題；§12.4 列 18 項機械落地工作（屬 master 第四輪整合 + Phase A.0 範圍，非 Pending）。**DF 跨 spec 殘留：0 條。**

## 6.2 UD §9 Pending（v2.0 校正 — 13 條；CC-d Pending count 校正）

| 編號 | 議題 | 優先級 | Owner | Phase |
| --- | --- | --- | --- | --- |
| 9.1.1 | P-009 08_a §11.1 patch | 高 | CODEX tier 2 + TASKS D.4/D.5 | Phase D 實作前要拍板 |
| 9.1.3 | P-011 canon delta threshold | 低 / 成熟期 | upstream specialist | Phase D+ 成熟期 |
| 9.1.5 | P-013 LOCKED retcon | 中 | upstream specialist | 對齊 D-040 後再議（Phase A.0F 後）|
| 9.1.7 | P-015 file mutex（多場景並行） | 中 | A.0 parser + ARCH | Phase A.0 parser 後（Windows flock fallback）|
| 9.2.1 | v0.2-A 00_q 實檔 | 中 | CODEX tier 2 | Phase A.0 之後（CODEX tier 2 邊界；本輪不寫）|
| 9.2.2 | v0.2-B 00_p 實檔 | 中 | CODEX tier 2 | 同上 |
| 9.2.4 | v0.2-D 衝突 merge UI 細節 | 中 | UX specialist 後續 patch | Phase A.0F 後（B.8 已標 PARTIAL；UX §11.7.6a 已新增框架）|
| 9.2.5 | v0.2-E §2.10.3 19 vs 20 欄偏離 | 低 | upstream specialist 後續 patch | 第五輪整合對齊 |
| 9.3.1 | 高風險場景 enum | 中 | upstream specialist + 09_h algorithm | Phase D 實作前 |
| 9.3.2 | D.3.5 路徑 B 後處理 | 高 | upstream specialist + TASKS D.3.5 | Phase D 實作前要拍板（對齊 D-043）|
| 9.3.3 | 05_b 章節空殼 weight | 低 | DF specialist Phase 4 + SPEC §5.3 補充 | Phase D+ 細化 |
| 9.3.4 | 00_b anchors 擴充 | 低 | upstream specialist + SPEC §17.1 補充 | Phase D+ 細化 |
| 9.3.5 | 下游 pipeline 解讀權威 | 中 | upstream specialist + master 第五輪 | 對齊 D-039；第五輪整合 |

## 6.3 UX §9 Pending（依三類拆分後 — UX §9.4）

| 類別 | 數量 | RESOLVED | PARTIAL | PENDING |
|---|---|---|---|---|
| §9.1 Schema 類 | 22 | 11 | 4 | 7 |
| §9.2 Query/API/Adapter 類 | 9 | 0 | 5 | 4 |
| §9.3 Upstream Algorithm 類 | 2 | 0 | 0 | 2 |
| **總計** | **33** | **11** | **9** | **13** |

**重要 PENDING 條目（v2.0 主整合接點）：**

| # | 議題 | Owner | 處理 |
|---|---|---|---|
| NS-18 | 「本場可用/禁用/慎用詞彙」markdown 標記 | DF（建議 Phase 4） | DF 後續 patch；建議欄位 `scene_vocab_allowed / forbidden / cautious` |
| NS-19 | 「本場應揭露/必須保密」資訊標記 | DF（建議 Phase 4） | 同上；建議欄位 `info_reveal_required / info_reveal_blocked` |
| NS-23 | content-hash 升級備案 | DF / server runtime | v0.3 採 mtime；後續可考慮 content_hash 欄位 |
| NS-24 | freshness 欄位是否動態維護 | DF | 建議 view 整合檔 frontmatter `freshness: ok\|stale` |
| NS-26~28 | Template / Instance / multi-project schema | DF / integrated master plan | DF Phase 4 |
| NS-NEW-1 | 09_e 定稿變更紀錄段落格式 | UD §3.6.3 / §3.6.6 | 待上下游細化；前端引導對齊 |
| NS-2 / NS-15 / NS-29 / NS-30 / NS-31 | query / API endpoint 規格 | Frontend adapter（ARCH） | 階段 3 ARCHITECTURE 落地 |
| NS-32 / NS-33 | 9/11 議題進度 query algorithm | UD §1.1.4 / §1.2.4 | UD 後續 patch |

## 6.4 既有 P-027 ~ P-030 處理對照（v2.0 校正 CODEX (d) CC-03）

DECISIONS_LOG §6.6.5 真實 P-027~P-030 議題：

| P-ID（真實對應） | 議題 | v0.3 patch 後狀態 | 處理 |
|---|---|---|---|
| **P-027** `/dialogue-write SINGLE_ITER` algorithm（上下游 specialist）| SINGLE_ITER 具體 algorithm；跟既有三模式切換；mode_tag phase_log 紀錄 | **RESOLVED via UD §4.7（v0.2/v0.3）+ D-027 + D-028 + D-042** | 完整 algorithm 在 UD §4.7；TASKS D.3 落地對應 SINGLE_ITER 模式 |
| **P-028** 手稿導入細節（上下游 specialist）| markdown structure 解析；trust-level phase_log 紀錄；entity 命名衝突 4 選項具體行為 | **RESOLVED via UD §10 + D-031~D-033 + D-042 + Contract A.8 + B.8** | UD §10.4 解析 algorithm / §10.5 4 選項 / §10.6 phase_log；UX §11.7.6a entity naming conflict modal（v0.3 patch 後加） |
| **P-029** 前端工具 UX 細節（UX specialist）| F1 看板下一步建議；F3 視覺結構；F6 facet；F7 編輯 UI；LOCKED 守門呈現；多場景並行；編輯衝突；複製指令 context；build/package；L3 export 前端入口 | **MOSTLY RESOLVED via UX §11（v0.2/v0.3）+ D-029/D-030/D-040/D-046 + Contract B.2/B.3/B.4/B.6/B.8** | UX §11 完整覆蓋 F1~F7 + LOCKED 守門 + Save race guard + Conflict modal + build/package + Export panel；殘留細節（如 UX §11.4 facet 8 維、UPS-UX-66 conflict diff 顯示細節）→ §6.3 Pending |
| **P-030** L3 export 觸發方式（上下游 + UX specialist）| CLI / 前端按鈕 / agent 指令；前端按鈕跑 CLI script | **RESOLVED via D-038（A1 prompt 流程）+ UD §12 + UX §11.6.11 + L3_EXPORT_PROMPT_SCHEMA v0.1 + Contract A.7/B.3/C.3** | 採 A1 prompt 流程，不用 CLI；clipboard / POST 三層觸發路徑 |

**v2.0 校正紀錄（依 CODEX (d) CC-03）：** v2.0 草版 §6.4 誤把 P-027~P-030 描述對到 v0.5 時期 P-027~P-030 候選描述（UX 細節 / canon delta / glossary / multi-medium）。本次校正以 DECISIONS_LOG §6.6.5 為真實基準。

**RESOLVED 對照表（v2.0 校正）：**

| Pending | RESOLVED 透過 | 落地位置 |
|---|---|---|
| P-027 SINGLE_ITER | UD §4.7 + D-027/D-028/D-042 | UD §4.7 algorithm；TASKS D.3 mode_tag SINGLE_ITER 支援 |
| P-028 手稿導入 | UD §10 + D-031~D-033 + D-042 | UD §10.x；Contract A.8 + B.8 |
| P-029 前端工具 UX | UX §11 + D-029/030/040/046 | UX §11 全節；Contract B.2/B.3/B.4/B.6/B.8 |
| P-030 L3 export 觸發 | D-038 + L3_EXPORT_PROMPT_SCHEMA | UD §12 + UX §11.6.11 + Contract A.7/B.3 |

P-027~P-030 全部 RESOLVED；無需後續分派為 Pending。**v2.0 此節從「Pending」改為「處理對照」性質。**

## 6.5 Pending 分派總覽（v2.0 校正 CC-d §6.5）

| 目的地 | 數量 | 範圍 |
|---|---|---|
| **Phase A.0 parser 內部 task**（A.0.1~A.0.9）| 約 5 條 | parser 9 大類處理項；對齊 ARCH §12 + TASKS A.0.x |
| **Phase A.0F frontend adapter 內部 task**（A.0F.1~A.0F.10）| 約 3 條 | frontend server.py 8 endpoint + Asset Panel API + Save race guard；對齊 ARCH §13 + TASKS A.0F.x；**依賴 Phase A.0 完成 + Phase B**|
| **CODEX tier 2（Phase A.0 之後）** | 約 4 條 | 00_p 實檔 / 00_q 實檔 / 08_a §11.1 patch / D.3.5 路徑 B 後處理 |
| **UX specialist 後續細化（Phase D 或之後）** | 約 6 條 | UX-66 conflict UI diff 顯示細節 / NS-18~19 task 欄位 / NS-NEW-1 09_e schema |
| **DF specialist 後續細化（Phase 4）** | 約 5 條 | NS-23 content_hash / NS-24 freshness / NS-26~28 Template/Instance/multi-project |
| **UD specialist 後續細化** | 約 5 條 | UD §9 高優先 9.1.1 / 9.3.2 + UD §1.1.4 / §1.2.4 algorithm |
| **成熟期（Phase D 之後）** | 約 4 條 | P-011 canon delta threshold / canon delta retcon |
| **第五輪 master 整合（pre-LOCKED 後續修補）** | 約 2 條 | UD §9.2.5 / §9.3.5 屬本輪未展開細節，第五輪整合對齊 |

**v2.0 校正紀錄（依 CODEX (d) §6.5 finding）：**

- v2.0 草版「本輪 master 第四輪整合對話」目的地對 v2.0 發布後狀態已過期 → 改為「第五輪 master 整合（pre-LOCKED 後續修補）」+ 移動已 RESOLVED 條目
- 「Phase A.0 內部 task」拆為 **Phase A.0 parser** 與 **Phase A.0F frontend adapter** 兩個目的地 — 對齊 TASKS 已把 frontend 定義為獨立 Phase A.0F，且依賴 Phase A.0 parser + Phase B

---

# 7. 文件維護紀律

- v2.0 是「**正式版 contract 介面**」 — 後續 specialist 第三輪 / master 第五輪整合對話對任何 contract 修訂需走升 v2.1+ 流程
- 修訂 contract 不刪除舊版內容；標 supersede 規則同 DECISIONS_LOG §7
- 跨 spec 對齊狀態欄位（每條 contract §N.M.6 / N.M.7「跨 spec 對齊狀態」表）若任一 ✓ 變 ✗ → 立即升 master 並 freeze 相關 spec
- v2.0 升 v2.1+ 條件：以下任一觸發
  1. 三 specialist 任一份 spec v0.4+ patch 涉及跨 spec 介面
  2. 新 D-NNN 拍板（D-047+）涉及 Contract A/B/C 任一條
  3. CODEX (d) 短審或後續審查找出 v2.0 與三 spec v0.3 / 主 SPEC v1.x 的新衝突
  4. user 提新需求 refresh 涉及 contract 改動
- 本檔 v2.0 對應的 git commit：「Master 4th-round v2.0: Contract A.1~A.8 / B.1~B.8 / C.1~C.5 + Pending 整理 + 維護紀律」

---

# 8. 後續更新區（保留給 v2.1+）

第五輪整合 master 對話 / 新 specialist patch 後 / 進一步需求 refresh 時於此區追加更新紀錄。

## 8.1 v2.0 → v2.1 升版條件範本

```
v2.0 → v2.1（YYYY-MM-DD）— <觸發原因簡述>

變動條目：
- §N.M: <修訂內容>
- §X.Y: <修訂內容>

對齊 D-NNN：
- D-NNN（簡述）

對 v2.0 的 supersede 範圍：
- 本次未 supersede / supersede §N.M（理由：...）

Owner：第五輪 master / 第三輪 <specialist> / 其他
```

## 8.2 v2.0 → v2.1 升版紀錄（master 第五輪 — 2026-05-19）

**觸發原因：** master 第五輪整合對話拍板 D-047（issue_type_registry 三層機制），需在 IC v2.x 加 Contract D 對齊三方介面（DF / UD / Phase B）。同時 NEW_REQ_6 RESOLVED 確認 Contract A.5 與 UD §3.10 已對齊（v0.4 衝突修補完成）。

**變動條目：**
- §0（header）：v2.0 → v2.1 + 加 v2.1 變動摘要 block
- §0.3 D-NNN 拍板清單：加 D-047 row + 補「v2.1 新增 D-047」說明
- §1 三 Contracts Overview：加 Contract D box（D.1 ~ D.4）
- §4a（**全新章節**）：Contract D 詳細
  - §4a.1 D.1 issue_type_registry.yaml schema + Template/Instance 分層
  - §4a.2 D.2 Phase B /create-* skill 讀 registry 動態構建議題清單
  - §4a.3 D.3 user_extensions / core_overrides 衝突處理 + locked 防 SKIP
  - §4a.4 D.4 A.0F frontend issue registry 編輯 UI 對齊
  - §4a.5 Pending（v2.1 sealed）
- §8.2（本節）：v2.1 升版紀錄

**對齊 D-NNN：**
- D-047（master 第五輪 — issue_type_registry 三層機制；5 skill × 36 user-facing 議題；UD LOCKED 權威命名）

**對 v2.0 的 supersede 範圍：**
- Contract A.1 ~ A.8 / B.1 ~ B.8 / C.1 ~ C.5 **不 supersede**
- Contract A.5（qa_type 8 種 + extensible registry）內容不動 — v2.1 註腳補：本契約與 UD §3.10 v0.5（NEW_REQ_6 修補）對齊 — 之前的 spec 衝突已 RESOLVED
- §5 Master 強制介入議題清單 **不 supersede**
- §6 Pending **不 supersede**
- §7 文件維護紀律 **不 supersede**

**Owner：** master 第五輪整合對話

**Cross-ref：**
- DECISIONS_LOG v1.1 §6.9.2（D-047 拍板紀錄）
- `_design/registries/issue_type_registry.template.yaml` v0.1（registry 權威範本）
- DF v0.4（partial supersede — NEW_REQ_3/4/5 落地）
- UD v0.5（partial supersede — NEW_REQ_6 落地）
- SPEC v1.2（partial supersede — §5.1 issue registry 機制 mention）
- ARCH v1.3（partial supersede — A.0.x issue registry parser 規格 + A.0.10 patch round）
- TASKS v1.4（partial supersede — A.0.10 task + B Phase /create-* 對齊 + A.0F 兩段制保留）

---

# 9. 附錄 — v1（過渡版）內容已 supersede 對照（v2.0 紀錄）

v1 內容大部分已被 v2.0 supersede；以下對照保留作歷史紀錄：

| v1 章節 | v2.0 對應 | 變化 |
|---|---|---|
| v1 §0 v1 過渡版盤點 | v2.0 §0 v2.0 性質 | 完全重寫 — v1 specialist 完成度 0/40/90 → v2.0 三 specialist v0.3 patch 完成 |
| v1 §1 介面總覽 | v2.0 §1 三 Contracts Overview | 重寫 — 加 ASCII diagram |
| v1 §2 Contract A 9 列 | v2.0 §2 Contract A 8 條 A.1~A.8 | 完全重寫 — schema 議題列表 → 真實介面條目 |
| v1 §3 Contract B（53 UX）| v2.0 §3 Contract B 8 條 B.1~B.8 | 完全重寫 — UX-N 對齊表 → 跨流程介面條目 |
| v1 §4 Contract C（無實質）| v2.0 §4 Contract C 5 條 C.1~C.5 | 完全新寫 |
| v1 §5 Master 強制介入議題 | v2.0 §5 Master 強制介入議題 | 保留 + v2.0 補增 4 條 |
| v1 §6 衝突偵測升級機制 | v2.0 §5 + §7（拆 + 移） | 拆併 |
| v1 §7 三 specialist 回傳節奏 | （已完成，刪） | v0.3 patch + 第四輪整合已完成此節奏 |
| v1 §8 議題狀態 v0→v1 對照 | v2.0 §6 Pending | 內容已多數 RESOLVED via D-037~D-046；殘留進 §6 |
| v1 §9 v1 新增 11 議題 | v2.0 §6 / DECISIONS_LOG §6.7 | 多數已 RESOLVED 或進 §6 Pending |
| v1 §10 第二輪 specialist 啟動清單 | （已完成，刪） | 三 specialist 第二輪 + v0.3 patch 已完成 |
