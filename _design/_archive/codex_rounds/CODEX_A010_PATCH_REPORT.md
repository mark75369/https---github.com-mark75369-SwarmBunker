狀態：REVIEW
版本：v0.1
最後更新：2026-05-19
適用範圍：CODEX A.0.10 parser patch round 完成報告
優先級：高

# CODEX_A010_PATCH_REPORT — Phase A.0 parser patch 落地驗證

## 0. 摘要

**結論：PASS**

3 critical：C1 ✓ / C2 ✓ / C3 ✓

## 1. 修補檔案與行範圍

- scripts/parse_frontmatter.py：line 110-121（A-* body comment label 補強）/ line 404-459（BOM 入口處理）/ line 1126-1273（build_repo_index 整合 + issue 去重）/ line 1439、2442、3447（同 parser 內其他讀檔入口改 utf-8-sig）

## 2. 3 critical 修補逐項

### C1 build_repo_index 整合 cross-ref + art existence

- 修補位置：line 110-121、1126-1162、1225-1273
- 修補摘要：build_repo_index 在 art_metadata_index 建好後，對含 dialogue_keys 的 parsed markdown 重跑 art-aware parse_dialogue_keys_map，套用 art_metadata_index.all_asset_ids；同時呼叫 validate_body_vs_frontmatter_consistency，將 body A-* depends_on WARN 與 historical alias WARN 聚合進 RepoIndex.issues。新增 issue 去重，避免 second pass 重複報同一 path+line+message。
- synthetic case 結果：C1-a ✓ / C1-b ✓ / C1-c ✓
- 殘留：無 critical 殘留。

### C2 entity_type_registry 一般 ID 驗證

- 修補位置：line 1164-1209、1263-1267
- 修補摘要：build_repo_index 對每個 parsed markdown 的 frontmatter entities / depends_on list 逐項呼叫 validate_entity_id，將未知 prefix / id_pattern 不符聚合進 RepoIndex.issues。驗證只套用 entities / depends_on，不重複驗證 dialogue_keys 的 portrait / bgm / sfx。
- synthetic case 結果：C2-a ✓ / C2-b ✓
- 殘留：detect_silent_drops 既有 public helper 未改寫；本輪以 index 層 validate_entity_id 覆蓋一般 frontmatter silent pass critical。

### C3 UTF-8 BOM header

- 修補位置：line 404-459、1439、2442、3447
- 採方案：a（parse_file 改 utf-8-sig）+ parse_markdown_text 入口 strip leading BOM；同 parser 內 phase_log / registry / fallback source read 也改 utf-8-sig。
- synthetic case 結果：C3-a ✓
- 殘留：無。

## 3. Regression 結果

- check_headers.py：75 files / 0 ERROR / 13 WARN / exit 0
- build_repo_index('.')：parsed_files=99 / 0 ERROR / 43 WARN。WARN 維持 Gate 1 baseline 類型，未因本輪 patch 新增 false-positive ERROR；parsed_files 與 check_headers 掃描數高於 Gate 1 baseline，原因是目前工作樹已有既有未追蹤 _design/CODEX_A010_PATCH_STARTER.md，且本輪新增本報告。
- 100 fake dialogue perf：0.4397s / parsed_files=102 / 0 ERROR / 1 WARN（Instance registry fallback）/ < 5s
- git diff --check：exit 0；僅 PowerShell/Git 回報 scripts/parse_frontmatter.py 下次 Git touch 會 LF→CRLF 的工作樹提示。

## 4. 不在 scope 的觀察（不修補）

- M1 normalized return contract：未處理。
- M3 get_all_dialogue_lines 排序：未處理。
- M4 scene scope voice：未處理。
- m1-m3 docstring / dead hook / registry template comment header：未處理；讀取時觀察到 entity_type_registry.template.yaml 仍屬既有 template comment header 狀態，按本輪邊界不修改。

## 5. 升 LOCKED 後續路線

- PASS → master 第五輪可直接進 D-047 拍板。

## 6. Source Limitations

- 實際讀取：_design/CODEX_GATE_1_REVIEW_REPORT.md、_design/TASKS.md 指定 A.0 段落、_design/DATA_FORMAT_SPEC.md §11.1.2 / §11.1.5 / §11.1.7、_design/INTEGRATION_CONTRACTS.md Contract A.1 / A.3 / A.5 引用段、_design/ARCHITECTURE.md §12.1.1 ~ §12.1.9、scripts/parse_frontmatter.py、scripts/check_headers.py、_design/registries/entity_type_registry.template.yaml、_design/registries/qa_type_registry.template.yaml、_design/expected_entities.yaml。
- 未審、不改：_design 下 LOCKED spec 文件本體設計層、既有 9 個 sub-task 核心邏輯、_design/registries/*.template.yaml、_design/expected_entities.yaml、_design/entity_exempt.yaml。
- 判斷限制：本輪 synthetic 使用臨時 Instance root，複製 registry template 後驗證 parser 行為；未新增正式 test file。
