狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.1 task 啟動包 — 00_b 通用骨架寫作  
優先級：高

# CODEX_A1_STARTER — Phase A 後段 A.1：寫 00_b 反 AI 味檢查表通用骨架

# 0. 本檔用途

Master 第五輪整合完成 + Milestone 1 啟動條件全達成（DECISIONS_LOG v1.1 §6.9.10）。

本檔給「**Phase A 後段 A.1 task**」對話啟動時用。把 §1 完整 prompt 複製貼到新 CODEX 對話。

**本 task 在路線圖位置：**
- Phase A 後段 Wave 1（A.1 + A.4 可平行）— 最 foundational + 無依賴 + 規模最小
- 完成後可繼續 A.4（27 模板 frontmatter 補完）/ A.2（init protocol）/ A.3（create-world protocol）

**前置條件（必須先完成）：**

- ✓ 設計層 10 spec LOCKED（DECISIONS_LOG v1.1 / IC v2.1 / SPEC v1.2 / ARCH v1.3 / TASKS v1.4 / DF v0.4 / UD v0.5 / UX v0.4 / L3 v0.2 / REQUIREMENTS_LOCK v1.0）
- ✓ Phase A.0 parser baseline + A.0.10 patch（scripts/parse_frontmatter.py）
- ✓ `_design/registries/` 三 registry LOCKED（entity v0.3 / qa v0.3 / issue v0.1）
- ✓ master 第五輪整合對話 push 完成

**本檔跟既有 CODEX starter 的差別：**

| 維度 | A010_PATCH_STARTER / REVIEW_STARTER_E | **本檔 A1_STARTER** |
|---|---|---|
| Phase | 設計層整合 / 收束 review | **Phase A 後段實作** |
| CODEX 身份 | implementer / reviewer | **implementer**（寫新 markdown 檔）|
| Scope | parser patch / spec verify | **單檔 documentation 寫作** |
| 預估時數 | 1-2 小時 / 30-45 分 | **1-2 小時** |
| 預期產出 | parser code + report | **`00_protocol/00_b_反ai味檢查表.md` 通用骨架（單檔）** |

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.1 task」— 寫作品專屬通用骨架 `00_protocol/00_b_反ai味檢查表.md`。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪寫一份新 markdown 檔（`00_protocol/00_b_反ai味檢查表.md`）
- 你不是 reviewer — 本輪不審 LOCKED spec、不改 spec
- 你是 documentation-style writer — 任務是 documentation 重構（從特定作品版反推通用骨架），不是 code implementer
- 對應傳統：本輪是 Phase A 後段第一個 task；Phase A.0 parser 已 baseline + A.0.10 patched + Milestone 1 啟動條件達成

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec（10 份設計檔 + 3 份 registry template + parser code）
- ✗ **不**改既有 27 份既有模板（屬 A.4 task）
- ✗ **不**寫其他 protocol 檔（00_i 屬 A.2 / 00_e 屬 A.3）
- ✗ **不**寫 skill 檔（屬 A.5+）
- ✗ **不**新增 spec 段落 / D-NNN / NEW_REQ
- ✗ **不**動 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`（reference 不動）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.1（line 535-563）+ SPEC v1.2 §17.1（line 1510-1522）+ ARCH v1.3 §7.3（依賴對照表，如需）：

### 任務目標

從 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`（蟲潮孤堡專案專屬版）反推通用骨架，產出 `00_protocol/00_b_反ai味檢查表.md`。

### 具體做法

1. **讀 reference 全文** — `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`（整檔）
2. **讀 SPEC §17.1** — `_design/SPEC.md` line 1510-1522（鎖定 7 個 section anchor 順序與名稱）
3. **保留**：結構（檢查表分類、QA 報告格式、模式差異表、高風險詞分類、句型檢查、髒話檢查、死亡處理、聲線污染、報告格式）
4. **移除**：所有作品專屬內容
   - 「蟲潮孤堡」/「黑翼」/「蟲災」/ 任何作品名
   - 「瑟琳」/「莉娜」/「諾拉」/ 任何角色名
   - 蟲潮孤堡專屬世界觀設定（語言層級、陣營名等）
5. **替換**：作品專屬範例改為通用範例
   - 角色名 → `<角色 A>` / `<角色 B>` / `<反派>` / `<NPC>` 等占位符
   - 作品名 → `<作品名>`
   - 陣營名 → `<陣營 A>` / `<陣營 B>`
   - 具體髒話範例 → `<該角色慣用髒話 1>` 等
6. **加 frontmatter**（在中文 header 後加 YAML block，依 SPEC §5.2 Canonical Schema）：
   ```yaml
   ---
   entities: []                    # 協議檔不貢獻實體
   depends_on: []                  # 通用骨架無依賴
   weight: {}                      # 不適用
   ---
   ```
7. **保留 header**（中文 header 在前；YAML block 在 header 後）：
   ```
   狀態：DRAFT
   版本：v0.1
   最後更新：2026-05-19
   適用範圍：全作品通用骨架
   優先級：高
   ```
8. **必含 SPEC §17.1 的 7 個固定 section anchors**（順序/名稱完全鎖定，CODEX 不得擅自重命名 / 重排序）：

   ```markdown
   ## 1. 作品類型語氣定位          ← 待 00_e 寫入（Template 端先放佔位說明）
   ## 2. 髒話尺度與死亡處理偏好    ← 待 00_e 寫入
   ## 3. 規模定位                  ← 待 00_g 寫入
   ## 4. 類型偏移風險清單          ← 待 00_g 寫入
   ## 5. 角色偏移檢查清單          ← 待 00_f 寫入（每角色一個 ### 子節）
   ## 6. 高風險場景的處理方式      ← 待 00_h 寫入（每場景類型一個 ### 子節）
   ## 7. 經驗累積的偏移案例        ← 日常使用 / 人類手動寫入
   ```

   每個 anchor 下放「**Template 端佔位說明**」（短句解釋此 section 由哪個協議寫入 / 寫入方式），不放實際內容（Instance bootstrap 階段 + 上游協議跑完才填）。

9. **保留 reference 中既有的 AI 味檢查邏輯結構**（檢查表本體 + QA 報告格式 + 模式差異表 + 高風險詞分類等），這些是骨架的核心；只把作品專屬例子換成占位符。

### 輸出檔案規範

- 路徑：`00_protocol/00_b_反ai味檢查表.md`（注意是 repo root 下的目錄，**不是** `_design/` 內）
- 編碼：UTF-8（無 BOM）
- 換行：對齊 repo 既有 markdown 風格

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.4（A.1 任務全段 line 535-563）
2. `_design/SPEC.md` v1.2 §17（line 1505-1548）— 含 §17.1 鎖定 7 anchor + §17.2 寫入規則 + §17.3 衝突標記 + §17.4 跨 repo 規則
3. `_design/SPEC.md` v1.2 §5.2（Canonical Schema — 中文 header + YAML block 寫法）

B. 內容反推依據（必讀整檔）
4. `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md`（整檔；reference 不動）

C. 對齊參考（不審；當依據；只看引用段落）
5. `_design/ARCHITECTURE.md` v1.3 §7.3（依賴對照表，用於確認協議檔 entities/depends_on 預期值）
6. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.0.1（共通骨架執行細則 — 確認協議檔結構規範）

D. 已 LOCKED 不可動文件（明示禁區）
7. 所有 `_design/*.md`
8. `_design/registries/*.template.yaml`
9. `scripts/parse_frontmatter.py` / `scripts/check_headers.py`
10. 既有 27 份模板（路徑見 ARCH §7.3 對照表）

---

**你要交付的產物：**

唯一新建檔：`00_protocol/00_b_反ai味檢查表.md`

**驗收條件（CODEX 自我驗證）：**

A. 內容驗證
- 整檔搜尋無「蟲潮孤堡」/「黑翼」/「蟲災」/「瑟琳」/「莉娜」/「諾拉」等具體作品/角色名
- 適用範圍寫「全作品通用骨架」（不是「全作品」/ 不是「蟲潮孤堡」）
- 結構與 reference 對照：檢查表分類、QA 報告格式、模式差異表、高風險詞分類、句型檢查、髒話檢查、死亡處理、聲線污染、報告格式 — 全部保留
- 含 SPEC §17.1 7 個固定 section anchors（順序/名稱完全一致）
- 每個 §1-§7 anchor 下有「待協議寫入」佔位說明（短句 + 引用 SPEC §17.2 寫入規則）

B. Frontmatter 驗證
- 中文 header 在前（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
- YAML block 在 header 後（entities: [] / depends_on: [] / weight: {}）
- 跑 `python scripts/check_headers.py` → 該新檔通過 0 ERROR（其他 75 檔不受影響；維持 0 ERROR baseline）

C. Parser 驗證
- 跑 `python -c "from scripts.parse_frontmatter import parse_file; r = parse_file('00_protocol/00_b_反ai味檢查表.md'); print(r.header); print('issues:', r.issues)"` → header 5 欄完整 / issues 為空

D. 不破壞既有
- `git diff --check` 通過（無 whitespace issue）
- `git status --short -uall` 預期：1 new file `00_protocol/00_b_反ai味檢查表.md`（+ 本 starter / 完成報告若你新建）
- 不動既有 27 模板 / 不動 _design 全部 / 不動 scripts/ 全部

---

**你交付物之外（建議產出，可選）：**

新建：`_design/CODEX_A1_REPORT.md`（可選）

報告格式（如交付）：

```markdown
狀態：REVIEW
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：Phase A 後段 A.1 task 完成報告
優先級：高

# CODEX_A1_REPORT — 00_b 通用骨架寫作完成

## 0. 摘要
**結論：[DONE / BLOCKED]**

## 1. 修改檔案
- `00_protocol/00_b_反ai味檢查表.md`（新建）
- （可選）本報告

## 2. 反推過程紀錄
（從 reference 抽離作品內容的策略；占位符選擇邏輯）

## 3. 驗收結果
- 內容驗證 ✓/✗（含證據）
- Frontmatter 驗證 ✓/✗
- Parser 驗證 ✓/✗
- 不破壞既有 ✓/✗

## 4. 不在 scope 的觀察（如有）
（如 reference 內 spec 不一致或新發現問題，列出但不修；交回 master 後續處理）

## 5. Source Limitations
```

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件（A/B/C/D）全 ✓
- **BLOCKED：** 任一驗收 ✗，回 master 第六輪或調整 starter

請開始。
```

---

# 2. 額外給 CODEX 的提示（如 CODEX 提問時可參考）

## 2.1 為什麼這個 task 看起來很單純但邊界要嚴

A.1 是 Phase A 後段第一個 task；產出 `00_b` 通用骨架後 — A.2 / A.3 / A.5 / A.6 / B.x 全會引用它。**若 anchor 順序錯或名稱錯，後續所有 protocol / skill 都要返工**。所以 SPEC §17.1 是硬鎖。

## 2.2 為什麼要保留 reference 結構而不重新設計

蟲潮孤堡版 reference 已是 AI 味檢查的成熟設計；本 task 是「**通用化**」不是「**重新設計**」。保留邏輯結構 + 抽離作品內容 = Template 的目的。重新設計屬於 spec 改動，不在本輪 scope。

## 2.3 commit 紀律

CODEX 改完後**不要**自己 commit / push（virtiofs cache 偶會 stale）— 由 user 手動執行。CODEX 只負責生新檔 + （可選）報告。

---

# 3. 完成條件 + 後續

CODEX A.1 完成 = 以下全部 ✓：

```
✓ 00_protocol/00_b_反ai味檢查表.md 新建完成
✓ A/B/C/D 4 驗收全 ✓
✓ （可選）_design/CODEX_A1_REPORT.md 產出
✓ 沒動任何 LOCKED 設計檔 / 既有模板 / scripts
```

CODEX 完成後：
- User 手動 commit + push（`git add 00_protocol/00_b_反ai味檢查表.md` + 可選 report，commit + push）
- 回 master 對話告訴我結果
- 我會：(1) 短 review 新檔；(2) 推薦下一個 task（A.4 或 A.2）

---

# 4. 文件維護紀律

- 本檔是「**CODEX A.1 task 啟動包**」；CODEX 完成後可 archive 進 `_design/archive/`
- 本檔產出後若需修補，改本檔 + 升 v0.2，**不**重發 prompt
