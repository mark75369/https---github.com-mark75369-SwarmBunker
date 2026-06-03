狀態：DRAFT
版本：v0.1
最後更新：2026-06-02
適用範圍：_source_materials/ 原始素材區用途與排除規則說明
優先級：中

# _source_materials/ — 原始素材區說明

## 1. 本區是什麼

`_source_materials/` 是 **user 原始輸入素材**的存放區，例如翻拍/續作的既有劇本台詞、人設草稿、世界觀設定筆記、劇情大綱草案等。

這些檔案是「餵給 skill 的輸入」，**不是 repo 產出的實體（entity）**。它們不帶 entity ID、不參與進度計算、不需要文件頭。

## 2. 子目錄分類（依用途，不依模組編號）

| 子目錄 | 用途 |
|---|---|
| `characters/` | 人設 source（角色設定、人設草稿等） |
| `world/` | 世界觀 source（世界觀設定、背景筆記等） |
| `outline/` | 劇情 / 關卡 / 大綱 source |
| `dialogue/` | 既有劇本台詞 source（翻拍 / 續作既有對白） |

非 `.md` 素材（`.docx` / `.txt` / `.csv` / `.json` 等）可直接放入對應子目錄，掃描器本就只掃 `*.md`，不受影響。

## 3. 排除規則（為何本區不被掃描）

- **本區的 `.md` 素材檔不需要中文 5 欄文件頭。** 本 `README.md` 仍保留 5 欄 header 作為慣例，但目前**不在任何掃描器涵蓋範圍**（`check_headers.py` 的 `TEMPLATE_PATTERNS` 不含本區、且非遞迴），不會被自動驗證。
- `scripts/parse_frontmatter.py` 的全 repo 掃描（`build_repo_index` 經由 `_iter_repo_markdown_files`）已將 `_source_materials/` 整個子樹排除（`SOURCE_MATERIAL_DIR_NAMES` 常數），因此本區素材**不計實體進度、不報 frontmatter 缺漏**。
- `scripts/check_paths.py` 只掃 `ACTIVE_DIRS` 列出的目錄，`_source_materials/` 天然不在其中。
- `scripts/check_headers.py` 的 `TEMPLATE_PATTERNS` 為單層（非遞迴）白名單且不含本區，故本區素材天然不被報 header 缺漏。
- `/status`、`/check-gaps` 底層走 `build_repo_index`，行為自動正確：本區不計實體進度、不報 header 缺漏。

## 4. 注意事項

- 不要在本區素材檔誤填 `entities:` frontmatter 欄位；本區檔案不是實體。
- 本區是 user 原始輸入，不是 skill 產物存放區；skill 產出（聲線卡、大綱等）仍寫入對應模組目錄（`03_characters/` 等）。
