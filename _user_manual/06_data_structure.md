狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：entity 類型、檔名規則、frontmatter schema 完整參考  
優先級：高

# 06 資料結構參考

# 1. 11 種 entity 類型

對應 SPEC §5.1 / §5.1a + entity_type_registry。

> **（鏡像；權威見 `entity_type_registry`）** — 本表為 registry core 的人類可讀鏡像（Batch 5 / D-075 雙軌：保留列舉 + 標權威指標）。若本表與 `entity_type_registry.yaml` core 不一致，以 registry 為準。parser 端鏡像（ENTITY_ID_RE 等）由 `scripts/check_entity_type_consistency.py` **強制比對**；本鏡像已於 **Batch 6 加 REGISTRY-MIRROR marker**，納入 lint 機器強制比對（drift 時 CI 報 ERROR）。

<!-- REGISTRY-MIRROR: entity-types -->
core 11 種：W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG
<!-- /REGISTRY-MIRROR -->


| Prefix | 類型 | 命名範例 | 對應目錄 |
|---|---|---|---|
| `W-rules` | 世界規則 | `W-rules`（單例）| `01_world/01_a_世界觀總覽.md` |
| `W-language` | 世界語言 | `W-language`（單例）| `01_world/01_b_世界語言規格.md` + `01_c_陣營與階級語言.md` |
| `W-style` | 文風樣本與指紋（D-055）| `W-style`（單例）| `01_world/01_d_文風樣本與指紋.md` |
| `V` | 詞彙系統 | `V`（單例）| `02_vocabulary/` |
| `C-<name>` | 角色 | `C-主角A` / `C-反派B` | `03_characters/main\|minor\|npc/<name>_*.md` |
| `R-<a>-<b>` | 關係 | `R-主角A-反派B`（字典序）| `04_relationships/*` |
| `P` | 主線 | `P`（單例）| `05_plot/05_a_主線大綱.md` |
| `CH-<n>` | 章節 | `CH-01` / `CH-12`（兩位數）| `05_plot/05_b-e_*` |
| `S-<ch>-<n>` | 場景 | `S-01-03` / `S-01-03a`（分支）/ `S-01-03sub`（支線）| `06_scene_index/`、`07_scene_tasks/`、`08_dialogue_outputs/` |
| `A-<subtype>-<owner>-<state>` | 美術資產（v1.1 新增）| `A-portrait-主角A-anger` / `A-bgm-tension-01` | `10_art_assets/<subtype>/<group>.md` |
| `ORG-<name>` | 組織 / 非人格對抗源（F8 / D-071+D-074）| `ORG-清道夫`（無聲線卡）| `11_organizations/<name>.md` |

## 1.1 命名規則

| 規則 | 細節 |
|---|---|
| 中文角色名直接用 | `C-主角A`、`C-反派B`、`C-夥伴C` |
| 關係按字典序 | `R-主角A-反派B`（不是 `R-反派B-主角A`）|
| 章節兩位數 | `CH-01`、`CH-12` |
| 場景三層 | `S-01-03`（第 1 章第 3 場）|
| 場景分支 | `S-01-03a` / `S-01-03b`（同場景變體）|
| 場景支線 | `S-01-03sub`（衍生支線）|
| A-* 4 段 | `A-<subtype>-<owner>-<state>` |

## 1.2 A-* subtype 7 種 + owner 對應

| Subtype | owner 對應 | 範例 |
|---|---|---|
| `portrait` | 必對應 C-* | `A-portrait-主角A-anger` |
| `bg` | 必對應 S-* / CH-* / global | `A-bg-cafe-day` |
| `cg` | 對應 S-* / CH-* / global | `A-cg-finale01-default` |
| `sfx` | 通常 global，可選 S-* | `A-sfx-glass-break` |
| `bgm` | 通常 global / CH-* | `A-bgm-tension-01` |
| `voice` | 必對應 C-* + dialogue KEY | `A-voice-主角A-line001` |
| `ui` | 通常 global | `A-ui-button-confirm` |

---

# 2. Frontmatter Schema

對應 SPEC §5.2.3。

## 2.1 完整欄位定義

每份 .md 開頭都含 **中文 header（5 欄）+ YAML block**：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-19
適用範圍：主角A 聲線卡
優先級：高

---
entities:
  - C-主角A
depends_on:
  - W-rules
  - W-language
weight:
  C-主角A: 1.0
---
```

## 2.2 中文 header 5 欄（必填，所有檔案）

| 欄位 | 值 | 說明 |
|---|---|---|
| `狀態` | DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED | 文件成熟度 |
| `版本` | `vN.N` 或 `v01A` / `v02` 等 | 版本標記 |
| `最後更新` | YYYY-MM-DD | 日期 |
| `適用範圍` | 自由文字 | 描述 |
| `優先級` | 最高 / 高 / 中 / 低 / 一般 | 重要度 |

## 2.3 YAML block 上游 3 欄（多數檔案有）

| 欄位 | 必填 | 說明 |
|---|---|---|
| `entities` | 視檔案 | 本檔貢獻給哪些 entity（list）|
| `depends_on` | 視檔案 | 本檔依賴哪些 entity（迭代反查用）|
| `weight` | 視檔案 | 對 entity 完成度的貢獻權重（scalar 或 map）|

## 2.4 YAML block 下游欄位（僅下游 pipeline 檔有）

| 欄位 | 值 | 說明 |
|---|---|---|
| `scene_id` | `S-01-03` | 場景 ID |
| `source_task` | 任務包路徑 | 從哪個任務包來 |
| `source_dialogue` | 單一台詞檔路徑 | QA 報告必填 |
| `source_dialogues` | list[path] | 僅 v02 收斂版用 |
| `pipeline_state` | 9 種 enum | 場景狀態機（見 §3）|
| `mode_tag` | 6 種 enum（含 SINGLE_ITER）| 對白 mode |
| `qa_decision` | PASS / FAIL / ARBITRATE_REQUIRED / null | QA 結論 |
| `qa_type` | 8 種 enum | QA 報告類型 |

## 2.5 dialogue_keys Map（下游台詞檔專屬，v1.1 新增）

每段台詞一個 KEY，含完整 metadata：

```yaml
dialogue_keys:
  dlg.ch01.s03.l001:
    line_index: 1
    speaker: C-主角A
    aliases: [dlg.ch01.s03.l001]
    portrait: A-portrait-主角A-anger
    bgm: A-bgm-tension-01
    sfx: [A-sfx-glass-break]
    status: active                # active | deprecated | deleted
    created_at: 2026-05-22
    renamed_at: null
    deleted_at: null
    deprecated_reason: null
    source_keys: null             # v02 收斂版才填（句級 lineage）
```

## 2.6 art_metadata List（A-* metadata 檔專屬，v1.1 新增）

每個 group .md 含該 group 所有 asset 的 entry：

```yaml
# 10_art_assets/portraits/主角A.md
---
entities:
  - A-portrait-主角A-default
  - A-portrait-主角A-anger
  - A-portrait-主角A-smile
depends_on: [C-主角A]
art_metadata:
  - asset_id: A-portrait-主角A-default
    subtype: portrait
    owner: C-主角A
    state_tags: [default, neutral]
    aliases: []
    status: active
    deprecated_reason: null
    deleted_at: null
    display_name: 主角A 預設立繪
    created_at: 2026-05-22
  - asset_id: A-portrait-主角A-anger
    # ...
---
```

---

# 3. 狀態三維度

對應 SPEC §5.2.4。

## 3.1 A. `狀態` — 文件成熟度（共用所有檔案）

```
DRAFT → REVIEW → FINAL → LOCKED → DEPRECATED
                                  ↓
              APPLIED（補丁類）/ DERIVED（view/ 衍生檔）
```

## 3.2 B. `pipeline_state` — 場景進度（僅下游檔）

```
SCENE_INDEXED        場景索引中存在
   ↓ /scene-task
TASK_DRAFT           任務包 DRAFT
   ↓ 人類審 D.2.5 gate
TASK_REVIEW          任務包 REVIEW
   ↓ /dialogue-write
DIALOGUE_TRIAL       多版本 v01A/B/C
   ↓ 人類挑亮點 D.3.5 gate
DIALOGUE_CONVERGED   收斂版 v02
   ↓ /qa
QA_PASSED / QA_FAILED
   ↓ 人類確認 + 填 09_e
DIALOGUE_FINAL
   ↓ 人類 LOCKED
DIALOGUE_LOCKED
```

## 3.3 C. `mode_tag` — 對白 mode（僅 /dialogue-write 產物）

| 值 | 用途 |
|---|---|
| `ORGANIZED` | 整理產出 |
| `DRAFT_TRIAL` | 試寫 v01A/B/C |
| `EXPERIMENTAL` | 破格 v01D |
| `CONVERGENCE` | 收斂 v02 |
| `FINAL_CANDIDATE` | 待 final |
| `SINGLE_ITER` | 單版本迭代（v1.1 新）|

## 3.4 D. `qa_type` — QA 報告類型（僅 QA 報告檔）

| 值 | 對應模板 |
|---|---|
| `AI_FLAVOR` | 09_a AI 味檢查 |
| `VOICE_CONSISTENCY` | 09_b 角色聲線一致性 |
| `FORBIDDEN_WORD` | 09_c 禁用詞檢查 |
| `INFO_CONTROL` | 09_d 資訊控制 |
| `GENRE_DRIFT` | 09_f 類型偏移 |
| `RHYTHM` | 09_g 節奏感（v1.1 新）|
| `DRAMATIC_TENSION` | 09_h 對話張力（v1.1 新）|
| `CROSS_SCENE_CONTINUITY` | 09_i 跨場一致性（v1.1 新）|

---

# 4. 完成度公式

```
單檔案完成度：
  不存在 / 空檔   → 0%
  DRAFT          → 25%
  REVIEW         → 75%
  FINAL / LOCKED → 100%
  DEPRECATED     → 不計入

單實體完成度：
  Σ(檔案完成度 × weight) / Σ(weight)
  其中只計算 entities 包含該實體的檔案
```

範例：C-主角A 完成度 =
- 03_characters/main/主角A_聲線卡.md（status REVIEW × weight 1.0）= 75
- 04_relationships/04_a.md（status DRAFT × weight 0.3）= 7.5
- 05_plot/05_c.md（status DRAFT × weight 0.5）= 12.5
- = (75 + 7.5 + 12.5) / 1.8 ≈ **52.8%**

---

# 5. phase_log Schema

存在 `.protocol_version` 檔的 `phase_log:` 段落。每個 skill 跑完 append 一筆。

```yaml
phase_log:
  - phase: <phase_name>           # bootstrap / create-world / ... / qa
    date: YYYY-MM-DD
    skill: /<skill_name>
    status: completed             # completed | in_progress | aborted
    import_source: null           # agent_assisted | external_llm | null（v1.1 新）
    created_entities: [...]
    entities_touched: [...]       # v1.1 新（多場景並行 mutex）
    iteration_count: null         # v1.1 新（僅 SINGLE_ITER）
    iteration_note: null          # v1.1 新（僅 SINGLE_ITER）
    base_dialogue: null           # v1.1 新（僅 SINGLE_ITER iteration_count >= 2）
    conflict_resolutions: []      # v1.1 新（手稿導入衝突 4 選項紀錄）
    # ... 其他 phase-specific 欄位
```

---

# 6. 9 種 status 完整對照

| 狀態 | 完成度 | 規則 | 作用範圍 |
|---|---|---|---|
| DRAFT | 25% | 草稿，可大幅修改 | 全域 |
| REVIEW | 75% | 可使用，但需審核 | 全域 |
| FINAL | 100% | 人類確認定稿（需 QA 通過）| 全域 |
| LOCKED | 100% | 已鎖定，不得擅自改動 | 全域 |
| DEPRECATED | 不計入 | 已棄用 | 全域 |
| APPLIED | 不計入 | 補丁類已套用 | `archive/` 專用 |
| DERIVED | 不計入 | 衍生整合檔 | `view/` 專用 |

---

# 7. 完整參考

如果想看 schema 完整定義：

- **SPEC** `_design/SPEC.md` §5 — 邏輯實體 + frontmatter
- **DF** `_design/DATA_FORMAT_SPEC.md` — 完整 schema（DF specialist 交付版本）
- **INTEGRATION_CONTRACTS** `_design/INTEGRATION_CONTRACTS.md` — Contract A.1~A.8（各種 schema 跨 spec 對齊）
