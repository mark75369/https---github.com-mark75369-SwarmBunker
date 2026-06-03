狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Gate 1 CODEX review NO-GO 後 — A.0.10 parser patch round 啟動包  
優先級：最高

# CODEX_A010_PATCH_STARTER — Phase A.0 收束 Gate 1 NO-GO 後的 parser patch round

# 0. 本檔用途

第四輪 master 對話完成設計層 LOCKED + Phase A.0 9 個 parser sub-task 實作後，由 master 第五輪整合 master 啟動 Gate 1 CODEX review。結論為 **NO-GO**（`_design/CODEX_GATE_1_REVIEW_REPORT.md` v0.1，2026-05-19）：

- C1 `build_repo_index()` 沒整合 A.0.5 cross-reference validator + A.0.2 art existence cross-check
- C2 A.0.7 `entity_type_registry` 未對一般 `entities` / `depends_on` 跑 ID 驗證
- C3 Windows UTF-8 BOM header 漏讀風險

這 3 critical 不修，D-047 issue_type_registry 拍板會建立在不可信 gate 上，後續 A.4 / A.7 / A.0F.8 / C.5a / D.4 都可能誤把目前漏掉的 validation 當已保證。

本檔給「CODEX A.0.10 parser patch round」對話啟動時用。把 §1 完整 prompt 複製貼到新 CODEX 對話。

**前置條件（必須先完成）：**

- ✓ Master 第四輪完成升 LOCKED（9 spec v1.0 / v1.1 / v1.2 / v1.3 / v0.2~v0.4）
- ✓ Phase A.0 9 個 parser sub-task 全 commit（A.0.1 ~ A.0.9）
- ✓ Gate 1 CODEX review 完成 + 報告產出（`CODEX_GATE_1_REVIEW_REPORT.md`，NO-GO）
- ✓ Master 第五輪整合 master 接手 + 讀完 7 份必讀

**本檔跟既有 starter 的差別：**

| 維度 | CODEX_REVIEW_STARTER_D / RECHECK_STARTER_D2 | **本檔 CODEX_A010_PATCH_STARTER** |
|---|---|---|
| 觸發時機 | 設計層審查 / pre-LOCKED 修補 verify | **Phase A.0 9 task 完成 + Gate 1 NO-GO 後** |
| CODEX 身份 | reviewer（不改檔） | **implementer + self-verify（改 parser、跑 synthetic test）** |
| Scope | spec 文件 | **scripts/parse_frontmatter.py + 對應 synthetic test 驗證** |
| 預估 CODEX 時數 | 45-90 分 / 2-3 小時 | **1-2 小時**（只修 3 critical + self-test） |
| 預期產出 | recheck report | **patch + `CODEX_A010_PATCH_REPORT.md`（PASS / 仍有殘留）+ master 接 mini-recheck** |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A.0 收束 Gate 1 NO-GO 後的 A.0.10 parser patch round」— 把 3 個 critical parser integration gap 修補，讓 build_repo_index() 成為可信 gate。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + self-verifier — 本輪改 scripts/parse_frontmatter.py（+ 必要時 scripts/check_headers.py 邊角）
- 你 NOT 是 reviewer — 本輪不審 LOCKED spec 文件、不改設計層
- 你是 patch-round only — 只修 §3 列出的 3 critical；其他 Gate 1 finding（M1-M4 major / m1-m3 minor）不在本輪 scope
- 對應傳統：本輪是 A.0.10 task（Phase A.0 收束後的整合修補）

**重要邊界（嚴格 scope）：**

- ✗ **不**改 _design/ 下任何 LOCKED spec 文件（DF / UD / UX / L3 / IC / SPEC / ARCH / TASKS / DECISIONS_LOG / REQUIREMENTS_LOCK）
- ✗ **不**改既有 9 個 sub-task 的核心邏輯 — 只在 build_repo_index 整合層 + parse_file 入口處 patch
- ✗ **不**處理 M1（normalized return contract）/ M3（get_all_dialogue_lines 排序）/ M4（scene scope voice）/ m1-m3（docstring / dead hook / template comment）
- ✗ **不**新增 PyYAML 等外部依賴（沿用既有 fallback YAML loader）
- ✗ **不**動 _design/registries/*.template.yaml（已對齊 D-043 / D-044）
- ✗ **不**動 _design/expected_entities.yaml / entity_exempt.yaml

**本輪 scope（嚴格限定 — 3 critical）：**

### Critical-1（C1）：`build_repo_index()` 整合 A.0.5 cross-ref validator + A.0.2 art existence cross-check

**Spec 依據：**
- DF §11.1.2 + §11.1.5（line 2399-2441）：
  - dialogue `portrait/bgm/sfx` 必須對應 valid A-* asset
  - 內文 A-* 引用未列 `depends_on` 要 WARN
  - 引用 historical alias 要 WARN
- Contract A.1 / A.3（IC line 198-214 + 507-518）
- TASKS A.0.2 / A.0.4 / A.0.5 驗收（TASKS line 300, 337, 376）

**現況證據（Gate 1 report §3.C1）：**
- `validate_body_vs_frontmatter_consistency()` 存在（`scripts/parse_frontmatter.py:871-924`）但 `build_repo_index()` 沒呼叫
- `parse_dialogue_keys_map()` 可收 `art_metadata_index`（`:757-815`），但 `build_all_dialogue_keys_index()` 沒做第二/三 pass 套 art metadata（`:927-952`）
- `build_repo_index()` 是先 `build_all_dialogue_keys_index()`，後 `build_art_metadata_index()`（`:1131-1137`），順序錯
- Synthetic：dialogue `portrait: A-portrait-hero-missing` 在 temp repo 跑 `build_repo_index()` 回傳 0 ERROR（應 ERROR）

**修補方向（建議；CODEX 可調整實作細節）：**
1. `build_repo_index()` 改順序：
   - load registries → parse all files → build art_metadata_index FIRST → 用 `art_metadata_index.all_asset_ids` 跑 dialogue_keys 第二 pass → 對每個 dialogue file 跑 `validate_body_vs_frontmatter_consistency()`
2. 也可不調換 `build_all_dialogue_keys_index` 的內部結構，改在 `build_repo_index` 整合層補一個「art_metadata_index 已知後重跑 dialogue_keys 驗證」迴圈
3. `validate_body_vs_frontmatter_consistency()` 對每個有 dialogue_keys 的 parsed_markdown 跑，issues 聚合到 `RepoIndex.issues`
4. 要 idempotent — 不能因為跑兩次 dialogue_keys parse 就重複報同樣的 issue（去重 key 用 path+line+message）

### Critical-2（C2）：A.0.7 `entity_type_registry` 一般 ID 驗證在 index 層套用

**Spec 依據：**
- TASKS A.0.7（line 416-424）：對 `entities` / `depends_on` 每個 ID 比對 valid set + regex；未知類型 ERROR；防 silent drop
- DF §11.1.7（line 2454-2462）

**現況證據（Gate 1 report §3.C2）：**
- `validate_entity_id()` 存在（`scripts/parse_frontmatter.py:704`）但 `build_repo_index()` 沒呼叫
- `detect_silent_drops()` 存在（`:723`）但沒整合
- `_validate_frontmatter_yaml()` 只做 list/type/enum 檢查（`:2792-2824`）
- Synthetic：`entities: [Z-unknown]` + `depends_on: [BadPrefix-1]` 跑 `build_repo_index()` 回傳 0 ERROR

**修補方向（建議）：**
1. `build_repo_index()` 對每個 parsed_markdown 的 `yaml_data` 的 `entities` / `depends_on` list（如為 list of string）跑 `validate_entity_id(eid, entity_registry)`
2. issues 聚合到 `RepoIndex.issues`（帶上 path + 該欄位 line 號；line 號可從 yaml_data line metadata 拿或退而求其次用 `yaml_start_line`）
3. 注意：**只**對 `entities` / `depends_on` 跑（不要對 dialogue_keys 內的 portrait/bgm/sfx 重複跑 — 那走 dialogue_keys path）
4. A-* 是否需要在這裡 reject 由 art_metadata_index 處理（C1 已涵蓋），這裡 validate_entity_id 對 A-* 走 subtype 驗證即可

### Critical-3（C3）：Windows UTF-8 BOM header 漏讀

**Spec 依據：**
- 隱性需求：Windows PowerShell / editor 工作流（user 平台）
- `check_headers.py` 為 Phase A.0 gate（TASKS A.0.1 驗收）

**現況證據（Gate 1 report §3.M2 / §6 第 3 點）：**
- `parse_file()` 用 `encoding="utf-8"`（`scripts/parse_frontmatter.py:453-455`）
- `_parse_header()` regex 沒處理 leading BOM（`:2713-2729`）
- Synthetic：`"﻿狀態: DRAFT"` 會導致 `狀態=None`，誤報「缺少欄位 '狀態'」

**修補方向（建議擇一）：**
- 選 a：`parse_file()` 改 `encoding="utf-8-sig"`（簡單；自動 strip BOM）
- 選 b：`parse_markdown_text()` / `_parse_header()` 入口處 strip leading `﻿`（精準，但要在三個讀檔入口都改：`parse_file` + `_parse_repo_phase_log` + `_read_registry_yaml`）

推薦 a — 變動最小。但若選 a，要確認 `parse_markdown_text` 接收 string 時（不經 parse_file）也要能處理 BOM（補一行 `text = text.lstrip("﻿")` 即可）。

---

**必讀文件（按順序）：**

A. 對齊基準（不審；當 spec 依據；只看引用段落）
1. _design/CODEX_GATE_1_REVIEW_REPORT.md（NO-GO 報告 — 你的修補依據）
2. _design/TASKS.md（A.0.1 / A.0.2 / A.0.4 / A.0.5 / A.0.7 / A.0.9 驗收段；line 300/337/376/391/416）
3. _design/DATA_FORMAT_SPEC.md（§11.1.2 / §11.1.5 / §11.1.7；line 2399-2462）
4. _design/INTEGRATION_CONTRACTS.md（Contract A.1 / A.3 / A.5；line 198-214 / 507-518 / 592-620）
5. _design/ARCHITECTURE.md（§12.1.1 ~ §12.1.9）

B. 本輪修補對象（核心 — 你動的檔）
6. scripts/parse_frontmatter.py（21 dataclass + 29 public function；只動 build_repo_index 區段 + parse_file 入口）
7. scripts/check_headers.py（不要動核心 — 但要驗證 BOM 修補後仍 0 ERROR）

C. 必跑驗證對象
8. _design/registries/entity_type_registry.template.yaml（不動，但 validate_entity_id 行為要對齊）
9. _design/registries/qa_type_registry.template.yaml（不動）
10. _design/expected_entities.yaml（不動）

---

**你要交付的產物：**

A. patch（直接改檔）
- scripts/parse_frontmatter.py — 3 critical 修補
- （必要時）scripts/check_headers.py 邊角調整（如 BOM patch 牽動）

B. self-verify synthetic test（可放在 scripts/__synthetic_a010__.py 暫存檔或 inline 跑 + 回報結果；commit 前可刪暫存）

必跑 6 個 synthetic case：
1. **C1-a missing A-* asset**：tempfile dialogue `portrait: A-portrait-hero-missing` + 空 art_metadata → `build_repo_index()` 應有 ERROR
2. **C1-b body A-* not in depends_on**：tempfile dialogue 內文 `<!-- A-bg: A-bg-castle-night -->` 但 frontmatter `depends_on` 沒列 → 應有 WARN
3. **C1-c historical alias**：tempfile dialogue 內文引用 A-* alias 但 art_metadata 標已 supersede → 應有 WARN
4. **C2-a unknown entity prefix**：tempfile `entities: [Z-unknown]` → `build_repo_index()` 應有 ERROR
5. **C2-b invalid pattern**：tempfile `depends_on: [BadPrefix-1]` → 應有 ERROR
6. **C3-a UTF-8 BOM header**：tempfile content = `"﻿狀態：DRAFT\n版本：v0.1\n..."` → `parse_file()` 應正確讀到 `狀態=DRAFT`，不報「缺少欄位 '狀態'」

C. regression（必跑，不能破壞）
1. `python scripts/check_headers.py` — 72 files, 0 ERROR, exit 0（WARN 數可變，但 0 ERROR 不可變）
2. `build_repo_index('.')` smoke — parsed_files=96，0 ERROR 維持（WARN 數可能增加 — A.0.5 cross-ref validator / entity validation 新啟用後 repo 內若有真實 ref/depends_on 缺漏會新增 WARN，這正常；但**不可**因 patch 引入新的 false-positive ERROR）
3. Performance sanity：跑 100 fake dialogue 檔 `build_repo_index` 應 < 5s（Gate 1 baseline ~0.08s 不可衰退到 10x 以上）

D. patch report：新建 `_design/CODEX_A010_PATCH_REPORT.md`

報告格式：

```markdown
狀態：REVIEW  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX A.0.10 parser patch round 完成報告  
優先級：高  

# CODEX_A010_PATCH_REPORT — Phase A.0 parser patch 落地驗證

## 0. 摘要

**結論：[PASS / PARTIAL / FAIL]**

3 critical：C1 [✓/✗] / C2 [✓/✗] / C3 [✓/✗]

## 1. 修補檔案與行範圍

- scripts/parse_frontmatter.py：line X-Y（build_repo_index 整合）/ line A-B（parse_file BOM）/ ...
- （其他）

## 2. 3 critical 修補逐項

### C1 build_repo_index 整合 cross-ref + art existence
- 修補位置：line X-Y
- 修補摘要：（變動描述）
- synthetic case 結果：C1-a [✓] / C1-b [✓] / C1-c [✓]
- 殘留：（如有）

### C2 entity_type_registry 一般 ID 驗證
- 修補位置：line X-Y
- synthetic case 結果：C2-a [✓] / C2-b [✓]
- 殘留：

### C3 UTF-8 BOM header
- 修補位置：line X-Y
- 採方案：a（utf-8-sig）/ b（strip BOM in parse_markdown_text）
- synthetic case 結果：C3-a [✓]
- 殘留：

## 3. Regression 結果

- check_headers.py：[72 files / 0 ERROR / N WARN / exit 0]
- build_repo_index('.')：[parsed_files=96 / 0 ERROR / N WARN]（WARN 從 43 變到 ? — 解釋變動原因）
- 100 fake dialogue perf：[Ns]

## 4. 不在 scope 的觀察（不修補）

（如 patch 過程發現其他 finding 屬 M1-M4 / m1-m3，列出但不修；交回 master 第五輪後續處理）

## 5. 升 LOCKED 後續路線

- PASS → master 第五輪可直接進 D-047 拍板
- PARTIAL → master 第五輪依殘留決定是否再一輪 patch 或可帶入 D-047 一併處理
- FAIL → 第二輪 patch round

## 6. Source Limitations

（你實際讀的檔；不修的 spec 區段；任何依靠假設的判斷）
```

---

**Go / No-Go 判定指引：**

- **PASS：** 6 個 synthetic case 全 ✓ + regression 0 ERROR 維持 + perf < 5s
- **PARTIAL：** 5+ synthetic case ✓，1 個有合理解釋（如 alias 機制細節需要再對 spec），其他全 ✓ — master 自決可否接著 D-047
- **FAIL：** ≥ 2 synthetic case ✗ 或 regression 退步引入新 ERROR — 第二輪 patch

請開始。
```

---

# 2. 額外給 CODEX 的提示（可選；如 CODEX 在 prompt 內提問本檔可參考）

## 2.1 既有 parser 結構速覽

```
scripts/parse_frontmatter.py (≈ 2900 line)
├── ValidationIssue / ParsedMarkdown / DialogueKeysResult / ArtMetadataResult / ... (21 dataclass)
├── parse_file() :440 ← BOM 修補入口
├── parse_markdown_text() :400 ← 也可能要 strip BOM（如獨立呼叫）
├── _parse_header() :2713 ← BOM 影響的 regex
├── validate_entity_id() :704 ← C2 要在 build_repo_index 套用
├── detect_silent_drops() :723
├── parse_dialogue_keys_map() :757 ← C1 art_metadata_index 第二 pass
├── validate_body_vs_frontmatter_consistency() :871 ← C1 build_repo_index 要呼叫
├── build_all_dialogue_keys_index() :927 ← C1 可能要重排
├── build_art_metadata_index() :1005
├── build_repo_index() :1121 ← C1 主修補點
└── ...
```

## 2.2 ArtMetadataIndex.all_asset_ids 是現成的

`ArtMetadataIndex.all_asset_ids: set[str]`（`:247`）已經包含 asset_id + alias，可直接餵 `parse_dialogue_keys_map(parsed, art_metadata_index=art_metadata_index.all_asset_ids)`。

## 2.3 不要為了「優雅」改太多

CODEX 容易把 build_repo_index 重構整段。本輪只要功能正確 + 6 synthetic case 全過 + 0 ERROR regression 維持。風格上的優化（如把整段拆 helper function）可以做但不是 acceptance criteria。

## 2.4 commit 紀律

CODEX 改完後**不要**自己 commit / push（virtiofs cache 問題）— 由 user 手動執行。CODEX 只負責生報告 + 改檔。

---

# 3. 完成條件 + master 第五輪後續

CODEX A.0.10 patch round 完成 = 以下全部 ✓：

```
✓ scripts/parse_frontmatter.py 3 critical patch 完成
✓ 6 個 synthetic case 全 PASS
✓ check_headers.py 0 ERROR 維持
✓ build_repo_index('.') 0 ERROR 維持
✓ 100 fake dialogue perf < 5s
✓ _design/CODEX_A010_PATCH_REPORT.md 產出
✓ 沒動任何 LOCKED spec 文件
```

CODEX 完成後：
- User 手動 commit + push scripts/parse_frontmatter.py + report
- Master 第五輪整合 master 接手 read CODEX_A010_PATCH_REPORT.md
- 若 PASS → 直接進階段 3 拍板 D-047
- 若 PARTIAL / FAIL → master 第五輪判斷是否需要第二輪 patch（或殘留帶入 D-047 一併處理）

---

# 4. 文件維護紀律

- 本檔是「**CODEX patch round 啟動包**」；CODEX 完成後可 archive 進 `_design/archive/`
- 本檔產出後若需修補（如 user 加 additional scope），改本檔 + 升 v0.2，**不**重發 prompt（CODEX 對話內就地補丁）
