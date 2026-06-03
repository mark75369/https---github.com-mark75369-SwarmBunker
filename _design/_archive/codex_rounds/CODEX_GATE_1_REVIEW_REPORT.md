狀態：REVIEW
版本：v0.1
最後更新：2026-05-19
適用範圍：Phase A.0 parser sub-task 收束 review / master 第五輪整合前 gate
優先級：最高

# CODEX_GATE_1_REVIEW_REPORT

## §0 摘要 + Go / NEAR-GO / NO-GO

**判定：NO-GO。**

Phase A.0 parser 的主要 API、registry 載入、`check_headers.py` baseline、JSON record accessor smoke test 都能跑；既有 repo `build_repo_index('.')` 也維持 0 ERROR。但收束 review 發現 repo-level integration 尚未把幾個 spec-required validator 串成同一條可信 gate：

- A.0.5 內文 A-* cross-reference / `depends_on` / historical alias validation 有 function，但 `build_repo_index()` 沒有呼叫。
- A.0.2 的 `art_metadata_index` existence cross-check 有 hook，但 repo-level build 先建 dialogue key index、後建 art index，沒有回填驗證；缺失 A-* asset 可通過。
- A.0.7 entity_type_registry 對一般 `entities` / `depends_on` 的 ID 驗證未整合；未知 entity prefix 可通過。
- Windows UTF-8 BOM 會讓第一行 `狀態` 漏讀，在 PowerShell 工作流下是實際風險。

結論：master 第五輪不建議直接進 D-047。建議先做 parser patch round，修完後再進 D-047 / issue_type_registry。

## §1 審查範圍 + Files Read

### Scope

- 本輪只審 Phase A.0 parser 實作、cross-task integration、spec 落地一致性、API 穩定性。
- 本輪未重審 LOCKED spec 內容本身。
- 本輪未修改 LOCKED 文件、未 commit、未 push。
- 本輪唯一 repo 產物為本報告。

### Files Read

- `_design/REQUIREMENTS_LOCK.md`
- `_design/SPEC.md`
- `_design/DATA_FORMAT_SPEC.md`
- `_design/INTEGRATION_CONTRACTS.md`
- `_design/ARCHITECTURE.md`
- `_design/L3_EXPORT_PROMPT_SCHEMA.md`
- `_design/TASKS.md`
- `_design/POST_LOCK_PENDING.md`
- `_design/CODEX_DEV_ORDER_EVALUATION.md`
- `scripts/parse_frontmatter.py`
- `scripts/check_headers.py`
- `_design/registries/entity_type_registry.template.yaml`
- `_design/registries/qa_type_registry.template.yaml`
- `_design/expected_entities.yaml`
- `_design/entity_exempt.yaml`

### Commands / Evidence Runs

- `git status --short -uall`：開始時乾淨；測試副作用 `scripts/__pycache__` 已清理。
- `python scripts/check_headers.py`：72 files, 0 ERROR, 12 WARN, exit 0。
- `build_repo_index('.')`：96 parsed files, 43 WARN, 0 ERROR；registry fallback 正常。
- Registry YAML load：4 份 YAML 均 valid；entity core=9，qa core=8。
- Synthetic hook tests：missing A-* / invalid entity / BOM / enum / phase_log cycle / export fixture。
- Sub-Review-1 API stability、Sub-Review-2 performance、Sub-Review-3 A.0.5/A.0.9 integration 已納入 findings。

## §2 7 項必驗逐項驗證

| # | 項目 | 判定 | 證據 |
|---|---|---|---|
| 1 | `scripts/parse_frontmatter.py` 完整 code review | △ PARTIAL | 21 dataclass + 29 public function 大致覆蓋 A.0.1-A.0.9；核心 smoke 可跑。但 public docstring 不完整，多個 public entry 無 docstring（如 `parse_markdown_text()` / `parse_file()` at `scripts/parse_frontmatter.py:400`, `:440`）；repo-level validator hook 未完全串接；BOM edge case fail。 |
| 2 | A.0.1 ~ A.0.9 regression | △ PARTIAL | A.0.1 enum / phase_log direct tests PASS；A.0.6 8 core qa_type PASS；A.0.9 record accessor fixture PASS。Regression fail 在 A.0.2/A.0.4/A.0.5/A.0.7 integration：direct hook 可抓，但 `build_repo_index()` 不抓 missing art / invalid entity。TASKS 驗收要求見 `_design/TASKS.md:300`、`:337`、`:376`、`:391`、`:416`。 |
| 3 | 跨 sub-task hook 整合驗證 | ✗ FAIL | `parse_dialogue_keys_map()` 有 `art_metadata_index` / `all_keys_set` hooks（`scripts/parse_frontmatter.py:757`），但 `build_all_dialogue_keys_index()` 只先單檔、後 all_keys pass（`:939`, `:947`），沒有 art metadata pass；`build_art_metadata_index()` 直接 `del qa_registry`（`:1005`, `:1012`）；`validate_body_vs_frontmatter_consistency()` 存在（`:871`）但 repo build 未呼叫。 |
| 4 | spec 落地一致性檢查 | ✗ FAIL | DF / ARCH / TASKS 要求 A-* existence、內文 A-* depends_on/alias、entity_type_registry 一般 ID 驗證；程式只有局部 hook，未整合到 main index。見 `_design/DATA_FORMAT_SPEC.md:2399`、`:2440`、`:2454` 對照 `scripts/parse_frontmatter.py:1121`、`:2792`。 |
| 5 | `scripts/check_headers.py` 整合驗證 | ✓ PASS | `check_headers.py` delegates `parse_file`（`scripts/check_headers.py:22`, `:54`）；CLI 行為仍掃 allowlist 並輸出 INFO/WARN summary。實跑 72 files, 0 ERROR, 12 WARN, exit 0。 |
| 6 | `_design/registries/` Template YAML 對齊 spec | △ PARTIAL | YAML valid；entity core 9 含 A 7 subtype（`_design/registries/entity_type_registry.template.yaml:58`）；qa core 8（`_design/registries/qa_type_registry.template.yaml:16`）。但 entity registry template 只有英文 comment header（`:1`-`:4`），缺中文 5 欄 comment header；qa registry 有完整中文 comment header（`:1`-`:5`）。 |
| 7 | `build_repo_index('.')` smoke test | ✓ PASS | parsed_files=96, issues=43 WARN / 0 ERROR；entity registry source=`template_fallback`, core=9；qa registry source=`template_fallback`, core=8；entities=26, dialogue_lines=0, art_metadata=0。WARN 皆屬現有 header / fallback baseline。 |

## §3 跨 sub-task 整合 finding

### Critical

**C1. `build_repo_index()` 未整合 A.0.5 cross-reference validator，且 A.0.2 art existence hook 沒有 repo-level 使用。**

- Spec 要求：`portrait` / `bgm` / `sfx` 必須對應 valid A-* asset（`_design/DATA_FORMAT_SPEC.md:2399`-`:2404`）；內文 A-* 引用未列 `depends_on` 要 WARN，引用 historical alias 要 WARN（`_design/DATA_FORMAT_SPEC.md:2433`-`:2441`）。
- Code 現況：`validate_body_vs_frontmatter_consistency()` 有完整邏輯（`scripts/parse_frontmatter.py:871`-`:924`），但 `build_repo_index()` 只呼叫 `parse_body_art_references()`（`:1141`-`:1147`），未呼叫該 consistency validator。
- Code 現況：`parse_dialogue_keys_map()` 可收 `art_metadata_index`（`:757`-`:815`），但 `build_all_dialogue_keys_index()` 沒有拿 `art_metadata_index` 做第二/第三 pass（`:927`-`:952`）；`build_repo_index()` 是先 `build_all_dialogue_keys_index()`，後 `build_art_metadata_index()`（`:1131`-`:1137`）。
- Synthetic evidence：dialogue `portrait: A-portrait-hero-missing` 在 temp repo 的 `build_repo_index()` 回傳 0 ERROR；直接呼叫 `parse_dialogue_keys_map(..., art_metadata_index=set())` 才會報 missing asset ERROR。

**C2. A.0.7 entity_type_registry 未套用到一般 frontmatter `entities` / `depends_on` 驗證。**

- Spec 要求：對 `entities` / `depends_on` 每個 ID 比對 valid set、regex，未知類型 ERROR，並防 silent drop（`_design/TASKS.md:416`-`:424`; `_design/DATA_FORMAT_SPEC.md:2454`-`:2462`）。
- Code 現況：`validate_entity_id()` 與 `detect_silent_drops()` 存在（`scripts/parse_frontmatter.py:704`, `:723`），但 `build_repo_index()` 未呼叫；`_validate_frontmatter_yaml()` 只做 list/type 檢查與 enum 檢查（`:2792`-`:2824`）。
- Synthetic evidence：temp file `entities: [Z-unknown]` + `depends_on: [BadPrefix-1]` 經 `build_repo_index()` 回傳 0 ERROR。

### Major

**M1. ARCH/TASKS 的 normalized return contract 尚未落地。**

- Spec 要求：無 YAML 時 `entities`/`depends_on` 回傳空 list，`weight` scalar 展開成 per-entity map，缺漏 downstream 欄位回傳 `None`（`_design/ARCHITECTURE.md:267`-`:273`; `_design/TASKS.md:260`）。
- Code 現況：`parse_markdown_text()` 回傳 raw `yaml_data`，無 YAML 時為 `None`（`scripts/parse_frontmatter.py:428`-`:437`）；scalar `weight` 保持 raw scalar。
- Synthetic evidence：純 header 檔 `yaml_data=None`；`weight: 0.5` 回傳 `{'weight': 0.5}`，未展開。

**M2. Windows UTF-8 BOM 會漏讀第一行 header。**

- Code 現況：`parse_file()` 用 `encoding="utf-8"`（`scripts/parse_frontmatter.py:453`-`:455`），`_parse_header()` regex 沒處理 leading BOM（`:2713`-`:2729`）。
- Synthetic evidence：`"\ufeff狀態: DRAFT"` 會導致 `狀態=None` 並報 `缺少欄位 '狀態'`。
- 影響：Windows PowerShell / editor 若寫出 UTF-8 BOM，`check_headers.py` 會誤報。

**M3. `get_all_dialogue_lines()` ordering 與 spec/API wording 不一致。**

- Spec/API wording：`get_all_dialogue_lines()` 應回傳 dialogue_line records「按 KEY 排序」（`_design/TASKS.md:454`; `_design/INTEGRATION_CONTRACTS.md:870`-`:872`; `_design/DATA_FORMAT_SPEC.md:2477`-`:2479`）。
- Code 現況：排序為 `(scene_id, line_index, key)`（`scripts/parse_frontmatter.py:1238`）。
- 影響：內容 schema PASS，但 deterministic ordering contract 需 patch 或在 spec 明確改口。

**M4. `scene` scope counts 未納入 `A-voice-*`。**

- Sub-Review-3 fixture：full scope 正常，scene scope 只從 dialogue record 的 `portrait/bgm/sfx` 建 dependencies，未用 `art_metadata.dialogue_keys_ref` 反查 voice asset。
- Code 現況：`_scene_scope_counts()` 只加入 `portrait/bgm/sfx`（`scripts/parse_frontmatter.py:1565`-`:1570`），再用 asset_id / aliases 篩 art metadata（`:1578`-`:1581`）。
- 影響：A.0F.8 / C.5a scene export prompt counts 可能少算 voice assets。

### Minor

**m1. Public API surface 尚未收斂。**

- AST 顯示 29 public functions + 21 dataclasses；多數 dataclass / public helper 無 docstring。
- 建議：補 `__all__` 或 facade 文件，至少穩定 `build_repo_index()` + export read APIs。

**m2. `build_art_metadata_index(..., qa_registry=...)` 是 dead hook。**

- `qa_registry` 參數存在但立即 `del qa_registry`（`scripts/parse_frontmatter.py:1005`-`:1012`）。
- 若只是 reserved hook，建議改文件說明；若是本輪要求「實際使用」，需 patch。

**m3. entity registry template comment header 不完整。**

- `_design/registries/entity_type_registry.template.yaml:1`-`:4` 缺中文 5 欄 comment header；`qa_type_registry.template.yaml:1`-`:5` 已有。

## §4 spec 落地不一致 finding

1. **DF §11.1.2 / §11.1.5 vs parser build path**  
   DF 要求 dialogue `portrait/bgm/sfx` cross-check art metadata、內文 A-* `depends_on` missing WARN、historical alias WARN（`_design/DATA_FORMAT_SPEC.md:2399`-`:2441`）。Parser 有局部 function，但 `build_repo_index()` 未整合（`scripts/parse_frontmatter.py:1121`-`:1160`）。

2. **Contract A.1 / A.3 vs repo-level hook wiring**  
   Contract A.1 要求 `portrait/bgm/sfx` valid A-* cross-check（`_design/INTEGRATION_CONTRACTS.md:198`-`:214`）；A.3 要求 art metadata / A-* unique / completeness API（`_design/INTEGRATION_CONTRACTS.md:507`-`:518`）。現況 A-* metadata index 可建，但 dialogue side 不回查 art index。

3. **DF §11.1.7 / TASKS A.0.7 vs general entity validation**  
   Registry loader 對 template/user_extensions 有效，但一般 source markdown 的 `entities` / `depends_on` 未依 registry 驗證。這違反 `_design/TASKS.md:416`-`:424` 與 `_design/DATA_FORMAT_SPEC.md:2454`-`:2462`。

4. **ARCH §2.2 normalized return vs raw parser result**  
   ARCH 要 normalization（`_design/ARCHITECTURE.md:267`-`:273`），但 `ParsedMarkdown.yaml_data` 是 raw parse result。若下游 `/status` 假設 normalized，會有缺欄與 weight 語義分歧。

5. **A.0.9 ordering wording vs implementation**  
   `get_all_dialogue_lines()` content fields 對齊 DF §9.5，但排序不是按 KEY；需 patch code 或修正 spec/API wording。

6. **L3 scene-scope voice asset coverage**  
   DF §9.6 / L3 export fixture顯示 voice record 可輸出，但 scene scope counts 不納入 voice dependency，會影響 prompt stats / scene export completeness。

## §5 後續 master 第五輪修補建議

### 必修（NO-GO / Critical）

1. **補 repo-level validation pass。**  
   建議啟動順序：load registries → parse all files → build key index first pass → build art metadata index → rerun dialogue key validation with `art_metadata_index.all_asset_ids` → run `validate_body_vs_frontmatter_consistency()` per file → aggregate issues into `RepoIndex.issues`。

2. **把 entity_type_registry 套到一般 `entities` / `depends_on`。**  
   對每個 parsed YAML list entry 呼叫 `validate_entity_id()`；將 `detect_silent_drops()` / registry-removal guard 納入 build 或提供明確 gate function，避免未知 prefix silent pass。

3. **處理 BOM。**  
   `parse_file()` / `_parse_repo_phase_log()` / `_read_registry_yaml()` 讀檔建議改 `utf-8-sig` 或在 `_parse_header()` 前 strip leading `\ufeff`；這是 Windows workflow 必修。

### 建議修（Major / 影響 Milestone 1）

1. 明確區分 raw parser result 與 normalized parser result：若保留 raw，新增 `normalize_frontmatter()` facade；若改 `ParsedMarkdown`，同步測試 `/status` 使用情境。
2. 決定 `get_all_dialogue_lines()` 排序 contract：按 KEY 或按 scene/line；決定後讓 spec 和 code 同步。
3. 修 `get_scope_counts(scope="scene")`，納入 `A-voice-*` via `dialogue_keys_ref`。
4. 為 A.0.9 facade 加 `__all__` 或 API stability note，避免 A.0F / C / D 直接依賴 helper internals。

### 可延後（Minor）

1. 補 public function / dataclass docstrings，至少補 critical API。
2. 清理或文件化 `qa_registry` reserved hook。
3. 補 entity registry template 中文 5 欄 comment header。
4. 記錄 performance watch：`get_all_dialogue_lines()` 每 KEY 掃 body 有單檔大量 KEY O(n²) 風險；`_validate_base_dialogue_cycles()` 長 chain 也有 O(n²) 風險。100 fake dialogue 檔 smoke 目前約 0.08s，非立即 blocker。

## §6 對 master 第五輪整合的 prep clarity

**目前不建議直接做 D-047。**

建議 master 第五輪順序改為：

1. **Parser patch round**：修 §5 必修項，至少讓 `build_repo_index()` 成為可信 gate。
2. **Gate re-run**：`check_headers.py`、`build_repo_index('.')`、synthetic cross-ref / invalid entity / BOM / export fixture / 100 fake dialogue perf。
3. **再做 D-047**：issue_type_registry / NEW_REQ_1。

若不先 patch，D-047 會建立在 parser 「可跑但不完整 gate」的狀態上，後續 A.4 / A.7 / A.0F.8 / C.5a / D.4 都可能把目前漏掉的 validation 當成已保證。

## §7 後續審查建議

下一輪 scope 建議固定為「parser patch verification」，不要重開設計審查：

- 只讀：`scripts/parse_frontmatter.py`、`scripts/check_headers.py`、兩份 registry template、必要 spec line refs。
- 必跑：
  - `python scripts/check_headers.py`
  - `build_repo_index('.')`
  - missing A-* asset 應 ERROR
  - invalid `entities` / `depends_on` 應 ERROR
  - body A-* not in `depends_on` 應 WARN
  - historical A-* alias reference 應 WARN
  - UTF-8 BOM header 應 PASS
  - `get_all_dialogue_lines(include_deleted=False/True)` fixture
  - `get_scope_counts(scope="scene")` 含 voice asset
  - 100 fake dialogue performance sanity

API stability 建議以 `build_repo_index()` + `get_all_entities()` + `get_all_dialogue_lines()` + `get_all_art_metadata()` + `get_manifest_snapshot()` + `get_scope_counts()` 作為 Phase A.0 對外 facade；其他 public helper 先視為 internal。
