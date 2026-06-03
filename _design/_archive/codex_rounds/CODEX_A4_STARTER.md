狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.4 task 啟動包 — 27 模板 frontmatter 補完  
優先級：高

# CODEX_A4_STARTER — Phase A 後段 A.4：補完既有 27 份模板 frontmatter

# 0. 本檔用途

Master 第五輪整合完成 + Milestone 1 啟動條件達成。本檔給「**Phase A 後段 A.4 task**」對話啟動時用。把 §1 完整 prompt 複製貼到新 CODEX 對話。

**本 task 在路線圖位置：**
- Phase A 後段 Wave 1（A.1 + A.4 可平行）— foundational template 工作
- 可與 A.1（00_b 通用骨架）+ A.0F.0（前端骨架）平行
- 完成後可繼續 A.2 / A.3 / A.5 / A.6 / B.x（多項依賴 A.4）

**前置條件：**

- ✓ 設計層 10 spec LOCKED（含 ARCH v1.3）
- ✓ Phase A.0 parser baseline + A.0.10 patch（含 BOM 修補 + entity validation 整合）
- ✓ `_design/registries/` 三 registry LOCKED

**與 A.1 / A.0F.0 平行性：**

| Task | 動到的檔 | 跟 A.4 衝突？ |
|---|---|---|
| A.1 | **新建** `00_protocol/00_b_反ai味檢查表.md` | ✗ 完全不重疊 |
| A.4（本） | **修改** 既有 27 模板 frontmatter | — |
| A.0F.0 | **新建** `_tools/frontend/` 目錄 | ✗ 完全不重疊 |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.4 task」— 補完既有 27 份模板的 frontmatter（entities + depends_on + weight 三欄）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪修改 27 份既有模板的 frontmatter（不動內文）
- 你不是 reviewer — 本輪不審 LOCKED spec
- 你是 mechanical-edit 工作者 — 本任務是依 ARCH §7.3 對照表逐檔補 YAML block，重複性高、可平行驗證
- 對應傳統：本輪是 Phase A 後段第二個 task（與 A.1 / A.0F.0 平行可跑）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry template / parser code
- ✗ **不**改既有 27 模板的**內文**（只動 frontmatter）
- ✗ **不**動 `00_protocol/00_b_反ai味檢查表.md`（如該檔存在，屬 A.1 範圍）
- ✗ **不**動 `_tools/frontend/` 任何檔（屬 A.0F.0 範圍）
- ✗ **不**升級任何模板的 status（DRAFT → REVIEW 屬人類 REVIEW gate 工作）
- ✗ **不**修改 ARCH §7.3 對照表的 entities / depends_on 初值（要改先回 ARCHITECTURE）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.4（line 611-631）+ ARCH v1.3 §7.3（line 1109-1140）+ SPEC v1.2 §5.2 Canonical Schema。

### 任務目標

把所有既有 27 份模板的 frontmatter 加上 `entities` / `depends_on` / `weight` 三欄（M6），對齊 ARCH §7.3 對照表。

### 具體做法

1. **讀 ARCH §7.3** — `_design/ARCHITECTURE.md` line 1109-1140（完整 27 模板對照表）
2. **讀 SPEC §5.2** — `_design/SPEC.md` §5.2（Canonical Schema：中文 header + YAML block 寫法 + entities/depends_on/weight 格式）
3. **掃描既有 27 份模板** — 列出實際存在的檔案，跟 ARCH §7.3 對照（如缺漏 / 多檔，列在報告 §4 不在 scope 觀察段，**不**自行新建檔）
4. **逐檔補 frontmatter**：
   - 保留既有中文 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）不動
   - 在中文 header 後加 YAML block：
     ```yaml
     ---
     entities: [<依 §7.3 表>]
     depends_on: [<依 §7.3 表初值>]
     weight: <依 §7.3 表，scalar 或 map>
     ---
     ```
   - 既有檔案的 status / version / last_updated **不動**
5. **weight 規則**（依 §7.3）：
   - 多 entities 一檔的（如 04_a 關係矩陣承載多 R-* + 多 C-*）→ weight 必須 **map** 型態，每 entity 一個值
   - 單 entity 一檔的 → weight 可 scalar
   - 實際數值由 CODEX 依「合理的加總要 ≈ 100%」原則微調（§7.3 line 1136）
6. **空模板處理**（依 §7.3 表「—」標示者，如 `00_*` 協議 / `03_b/c 模板`）：
   - 加 `entities: []` / `depends_on: []` / `weight: {}` 或省略 YAML block（依該檔既有結構）

### 27 模板的範圍

**核心 27 份**（依 ARCH §7.3 列舉）：

- `00_protocol/00_a` ~ `00_*`（協議檔，多為空 frontmatter — 詳 §7.3 第一列）
- `01_world/01_a` / `01_b` / `01_c`（世界觀 + 語言）
- `02_vocabulary/02_a` / `02_b` / `02_c`（詞彙）
- `03_characters/03_a` 角色總表 + `03_b` / `03_c` 模板
- `04_relationships/04_a` 關係矩陣 + `04_b` 時間線
- `05_plot/05_a` ~ `05_e`（主線 / 章節 / 弧線 / 資訊揭露 / 伏筆）
- `06_scene_index/06_a` 場景索引
- `07_*` / `08_*` / `09_*`（下游 pipeline — 多為 Template 範本，frontmatter 詳 §7.3 末列）

**注意：** 實際 27 數字含協議檔 + 各分類本體檔；CODEX 啟動時跑 `git ls-files | grep -E '^\d|\d_'` 確認檔名清單；若實際數 ≠ 27（譬如 30 或 25），列在報告 §4 不在 scope 觀察段，不擅自決定。

### 跨檔 weight 加總一致性

- 對每個 entity，跨檔 weight 加總應 ≈ 1.0（§7.3 line 1136 規範）
- 範例：`C-小明` 出現在 `03_characters/main/小明_聲線卡.md`（weight 1.0）+ `03_a 角色總表`（weight 0.1 索引性）+ `04_a 關係矩陣`（weight 0.2）+ `05_a 主線大綱`（weight 主要 C-* 各 0.x）... 各檔小數加總 ≈ 1.0 為 ideal target
- CODEX 不需自行算精確 1.0，但若數字明顯偏離（如某 entity 跨檔加總 > 2.0），列警示在報告

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（A.4 任務 line 611-631）
2. `_design/ARCHITECTURE.md` v1.3 §7.3（27 模板 entities / depends_on / weight 對照表 line 1109-1140）
3. `_design/SPEC.md` v1.2 §5.2（Canonical Schema 寫法）

B. 對齊參考
4. `_design/INTEGRATION_CONTRACTS.md` v2.1 Contract A.1（dialogue_keys + frontmatter 標準）
5. `_design/DATA_FORMAT_SPEC.md` v0.4 §3 / §4（frontmatter 欄位定義 + KEY 規範）

C. Parser 驗證用
6. `scripts/parse_frontmatter.py` v1.0（A.0.10 patched — 不動，跑 verification 用）
7. `scripts/check_headers.py`（A.0.1 baseline — 不動）

D. 已 LOCKED 不可動文件（明示禁區）
8. 所有 `_design/*.md`
9. `_design/registries/*.template.yaml`
10. `_design/references/*`
11. `scripts/*.py`

---

**你要交付的產物：**

修改 27 份既有模板（只動 frontmatter；不動內文）。

**驗收條件（CODEX 自我驗證）：**

A. 內容驗證
- 每個 entity 在所有引用該 entity 的檔有對應 frontmatter（含 entities / depends_on / weight）
- 隨機抽 3 個檔目視確認 `entities` 寫對（對齊 §7.3 表）
- 隨機抽 3 個檔目視確認 `depends_on` 寫對（依 §7.3 表初值）
- 隨機抽 1 個 04_a 確認 `weight` 為 **map** 型態（不是 scalar）
- 跨檔 weight 加總每個 entity ≈ 1.0（不要求精確；明顯偏離 > 2.0 列警示）

B. Frontmatter 結構驗證
- 中文 header 不動（5 欄完整）
- YAML block 在 header 後
- YAML 語法 valid（無 indent error / unquoted special char）

C. Parser 驗證（必跑）
- 跑 `python scripts/check_headers.py` → 0 ERROR（維持 baseline；WARN 可變動但不可新增 ERROR）
- 跑 `python -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); errors = [i for i in r.issues if i.severity == 'ERROR']; print('ERROR count:', len(errors))"` → 0 ERROR

D. 不破壞既有
- `git diff --check` 通過
- 僅 frontmatter 區域變動；內文（YAML block 後）**完全不動**
- 不動既有 `_design/` / `scripts/` / `_design/registries/`
- 不動 `00_protocol/00_b_反ai味檢查表.md`（若該檔由 A.1 創建中）
- 不動 `_tools/frontend/` 任何檔（若該目錄由 A.0F.0 創建中）

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A4_REPORT.md`（可選）

報告格式（如交付）：

```markdown
狀態：REVIEW
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：Phase A 後段 A.4 task 完成報告
優先級：高

# CODEX_A4_REPORT — 27 模板 frontmatter 補完

## 0. 摘要
**結論：[DONE / BLOCKED]**

實際處理檔案數：N

## 1. 修改檔案清單
- `01_world/01_a_*.md` (entities=[W-rules], depends_on=[], weight=1.0)
- `01_world/01_b_*.md` (entities=[W-language], depends_on=[W-rules], weight=1.0)
- ...（逐檔列）

## 2. 跨檔 weight 加總分析（每 entity）
- W-rules: 跨檔加總 ≈ X.X
- W-language: ...
- C-* / R-*-* / ...

## 3. 驗收結果
- 內容驗證 ✓/✗
- Frontmatter 結構 ✓/✗
- Parser 驗證 ✓/✗ (check_headers / build_repo_index)
- 不破壞既有 ✓/✗

## 4. 不在 scope 的觀察（如有）
- 實際模板數 vs 27 目標數
- 缺漏檔案 / 多餘檔案
- §7.3 對照表潛在不一致

## 5. Source Limitations
```

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件全 ✓ + check_headers + build_repo_index 都 0 ERROR
- **BLOCKED：** 任一驗收 ✗，回 master

請開始。
```

---

# 2. 平行跑時的合作紀律（A.1 / A.0F.0 同時）

若你（user）同時跑 A.1 + A.4 + A.0F.0 三個 CODEX 對話：

| 動作 | 影響 |
|---|---|
| A.1 新建 `00_protocol/00_b_反ai味檢查表.md` | 不影響 A.4 既有 27 模板 |
| A.4 修改 27 模板 frontmatter | 不影響 A.1 新建檔 / A.0F.0 frontend 目錄 |
| A.0F.0 新建 `_tools/frontend/` | 不影響 A.4 既有 27 模板 |

**commit 紀律：** 三個 task 完成後各自獨立 commit，**不要**混在同一 commit。

---

# 3. 完成條件 + 後續

CODEX A.4 完成 = 4 驗收 ✓ + 報告（可選）+ 沒動禁區。

CODEX 完成後：
- User 手動 commit + push（`git add` 改的 27 模板 + 可選報告，commit + push）
- 回 master 對話告訴我結果
- 我會：(1) short review；(2) 若 A.1 也完成 + 平行軌道 ready → 推 A.2 或 A.3

---

# 4. 文件維護紀律

- 本檔是「**CODEX A.4 task 啟動包**」；CODEX 完成後可 archive 進 `_design/archive/`
- 本檔產出後若需修補，改本檔 + 升 v0.2
