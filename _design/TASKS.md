狀態：LOCKED
版本：v1.9（第七輪 master partial supersede 兩處：(1) D-052 — §A.10/§B.5.5/§B.6.5/§B.8「禁止 CODEX 自行升 status」段加 AI-assisted 後 user 明示拍板 exception（CR-02 backfill v1.9 header 補入 §A.10）；(2) D-050 / D-053 — §B.7「階段 4 拆分」line 1362 限定 05_b + 06_a only（05_c/d/e 屬 P /create-outline scope 不寫）；其他段不動）
最後更新：2026-05-20
適用範圍：Game Dialogue Bible 重啟版實作任務拆解 / CODEX 執行清單
優先級：最高

# TASKS — 實作任務拆解

> **v1.8 → v1.9 partial supersede 變動摘要（2026-05-20 ~ 2026-05-21，第七輪 master inline patch rounds — D-052 + D-050/D-053 兩處 partial supersede；R7-MA-01 補 ledger by 8th master Cleanup round 2026-05-21）：**
>
> 本輪 TASKS v1.9 對 v1.8 LOCKED 內容做 **partial supersede 兩處** — 保留原段內容 + 加 v1.9 標註說明擴充範圍。
>
> | TASKS 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §A.10（Phase A 整體 REVIEW gate）| D-052（DECISIONS_LOG v1.8 §6.15.2 + v1.9 §6.15.2 CR-02 backfill）| 「禁止 CODEX 自行升 status」段加 user 明示拍板後 AI-execute exception；同性質人類 REVIEW gate；CR-02 backfill 補 §A.10 涵蓋（原 v1.8 inline patch 漏列）|
> | §B.5.5（角色 REVIEW gate）| D-052 | 「禁止 CODEX 自行升 status」段加 AI-assisted exception；review_log §1 entry AI 可代寫（精確邊界 patch）|
> | §B.6.5（主線 REVIEW gate）| D-052 | 同上；對 4 個 P-tagged 檔 frontmatter + review_log §1 entry |
> | §B.8（Phase B 整體 REVIEW gate）| D-052 | 同上；對 5 類實體 + review_log §1 entry 5 個 §1.2.X 子段 |
> | §B.7「階段 4 拆分」（line 1362）| D-050 + D-053（DECISIONS_LOG v1.5 §6.12.2 + v1.9 §6.16.2）| /create-detailed-outline 寫檔範圍嚴格限定 `05_b + 06_a` only（05_c/d/e 屬 P /create-outline scope 不寫）；對應 D-050 子裁決 2 CH 行 + D-053 partial supersede D-050 子裁決 1（/create-world 寫 00_b §1/§2 exception；不影響 §B.7）|
>
> **v1.9 不動段（保留 v1.8 LOCKED 原狀）：**
> - §A.0 ~ §A.9 / §A.11 / §A.12 全部
> - §A.0F.0 ~ §A.0F.11 全部
> - §B.0 ~ §B.4 / §B.5 / §B.5b / §B.6 / §B.7（除 line 1362 階段 4 拆分外）/ §B.9 不動 active scope
> - §C / §D Phase 全部
> - Wave 4 / Wave 5 / Wave 6 / Wave 7 / Wave 8 順序定義不變
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 不變；D-001 ~ D-053 拍板不變；本輪 partial supersede 屬「禁止」精細化（D-052）+ 寫檔邊界 cleanup（D-050/D-053 既有），不改 task 結構。
>
> 第七輪 master inline patch round owner：D-052 / D-050 §B.7 partial supersede 落地；8th master Cleanup round 2026-05-21 owner：本 v1.8→v1.9 ledger backfill（R7-MA-01 — 補在 TASKS top summary 區，使 LOCKED partial supersede record 完整）。

---

> **v1.7 → v1.8 partial supersede 變動摘要（2026-05-20，master 第六輪延伸 Wave 6 完成後紀錄）：**
>
> 本輪 TASKS v1.8 對 v1.7 LOCKED 內容做 **minor partial supersede** — B.0~B.4 task scope 從「寫新 protocol」修正為「Wave 6 D-047 對齊 patch round」+ 紀錄完成狀態。
>
> | TASKS 段 | 對應決策 | 動作摘要 |
> |---|---|---|
> | B.0 ~ B.3 task scope | master 第六輪延伸 Wave 6 patch round | 修正 task 性質：4 個 protocol 已存在 (May 18 第五輪整合期間)，本輪 patch 為 D-047 對齊 (header v0.2 + §2 啟動條件 + §4.0 動態構建 + §4.1 議題預設表)；非「寫新檔」 |
> | B.4 task | master 已 verify | 標 ✓ DONE（03_characters/main/minor/npc 子目錄已存在 May 16 既有）|
>
> **v1.8 不動段（保留 v1.7 LOCKED 原狀）：**
> - A.0 ~ A.12 全部
> - A.0F.0 ~ A.0F.9 全部
> - B.5 ~ B.9 全部（Wave 7 / Wave 8 scope 不變）
> - C / D Phase 全部
> - Wave 4 / Wave 5 順序定義不變
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 不變；D-001 ~ D-049 拍板不變。
>
> Master 第六輪延伸 owner：B.0~B.4 Wave 6 patch round 完成紀錄。

---

> **v1.6 → v1.7 partial supersede 變動摘要（2026-05-20，master 第六輪 Wave 4 完成後紀錄）：**
>
> 本輪 TASKS v1.7 對 v1.6 LOCKED 內容做 **minor partial supersede** — A.11 task scope 加 Wave 4 review consolidation 備註，反映 user 拍板「Wave 4 review 延後 A.11 一起跑」。
>
> | TASKS 段 | 對應決策 | 動作摘要 |
> |---|---|---|
> | A.11 Phase A 整體驗收 | user 拍板（master 第六輪本對話內） | 在 A.11 既有「做法」段後加「Wave 4 review consolidation」子節 — A.11 CODEX 啟動時必須驗 Wave 4 三產出（A.7 status / A.8 check-gaps / A.12 multi-agent invocation 檔三份）對齊各自 starter 規範 |
>
> **v1.7 不動段（保留 v1.6 LOCKED 原狀）：**
> - A.0 ~ A.10 全部
> - A.5b 全部
> - A.12 全部
> - A.0F.0 ~ A.0F.9 全部
> - B / C / D Phase 全部
> - Wave 4 / Wave 5 順序定義不變
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 不變；D-001 ~ D-049 拍板不變。
>
> Master 第六輪 owner：A.11 Wave 4 review consolidation 備註。

---

> **v1.5 → v1.6 partial supersede 變動摘要（2026-05-20，master 第六輪 Critical patch round）：**
>
> 本輪 TASKS v1.6 對 v1.5 LOCKED 內容做 **partial supersede** — 保留原段內容 + 加 v1.6 標註說明擴充範圍。
>
> | TASKS 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | A.5 後加 A.5b task | D-049 + NEW_REQ_8 | 新增 A.5b「Critical patch round — Template-detect 機制」task；屬 master 直接 patch 完成（不發 CODEX 對話）；紀錄 patch 結果與影響 |
>
> **v1.6 不動段（保留 v1.5 LOCKED 原狀）：**
> - A.0 ~ A.5 / A.6 ~ A.11 / A.12 全部
> - A.0F.0 ~ A.0F.9 全部
> - B / C / D Phase 全部
> - Wave 4 = A.7 + A.8 + A.12（不動）
> - Wave 5 = A.9 + A.10 + A.11（不動）
> - A.5b 是「歷史紀錄類 task」（master 已完成 inline patch；不是 future task）
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-048 拍板不變；本輪只加 D-049 對應 A.5b task。
>
> Master 第六輪 Critical patch round owner：A.5b task spec + Template-detect patch 落地紀錄。

---

> **v1.4 → v1.5 partial supersede 變動摘要（2026-05-20，master 第六輪整合）：**
>
> 本輪 TASKS v1.5 對 v1.4 LOCKED 內容做 **partial supersede** — 保留原段內容 + 加 v1.5 標註說明擴充範圍。
>
> | TASKS 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | Phase A 後段加 A.12 task | D-048 + NEW_REQ_7 | 新增 A.12「NEW_REQ_7 落地 — root AGENTS.md + CLAUDE.md + skill_invocation_guide.md」task；屬 Wave 4 平行（與 A.7 / A.8 同步可跑）|
>
> **v1.5 不動段（保留 v1.4 LOCKED 原狀）：**
> - A.0 ~ A.11 全部
> - A.0F.0 ~ A.0F.9 全部
> - B / C / D Phase 全部
> - Wave 4 = A.7 + A.8 + A.12（A.12 為 v1.5 新增；A.7 / A.8 不動）
> - Wave 5 = A.9 + A.10 + A.11（依序，A.10/A.11 含人類 REVIEW gate）
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-047 拍板不變；本輪只加 D-048 對應 A.12 task。
>
> Master 第六輪整合 owner：A.12 task spec + Wave 4 啟動聲明。

---

> **v1.3 → v1.4 partial supersede 變動摘要（2026-05-19，master 第五輪整合）：**
>
> 本輪 TASKS v1.4 對 v1.3 LOCKED 內容做 **partial supersede（非 supersede）** — 保留原段內容 + 加 v1.4 標註說明擴充範圍。
>
> | TASKS 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | A.0 末加 A.0.10 task | Stage 0 NO-GO patch round | 新增 A.0.10「parser patch round — 3 critical fix」task（已由 CODEX 完成 PASS；TASKS 紀錄）|
> | A.X 預留（未排定） | Phase A.X | A.0.10 後 M1/M3/M4/m1-m3 finding 處理屬 Phase A.X（不在 A.0 收束 scope；按需求觸發）|
> | A.5 init-project 對齊 | D-047 | A.5 補「拷貝 `issue_type_registry.template.yaml` 到 Instance root」task；既有 entity / qa registry 拷貝行為不動 |
> | B.5 / B.5b / B.6 / B.7 + B.0 ~ B.3 protocol | D-047 | 5 個 /create-* skill 實作 task 補「讀 `<instance_root>/issue_type_registry.yaml` 動態構建議題清單」要求；既有 task 結構不動 |
> | A.0F 兩段制 | CODEX_DEV_ORDER_EVALUATION §3 | 重申 A.0F 拆 alpha（A.0.10 後）+ real-data acceptance（B.9 後）；既有 A.0F.0 ~ A.0F.11 任務 mapping 不動，僅補階段標記 |
> | A.0F real-data acceptance | D-047 | A.0F.x（待 UX specialist 編號）加「issue_type_registry 編輯 panel」task — 屬 A.0F real-data acceptance scope（非 alpha）|
>
> **v1.4 不動段（保留 v1.3 LOCKED 原狀）：**
> - 既有 A.0.1 ~ A.0.9 task 結構與驗收條件不動
> - 既有 A.0F.0 ~ A.0F.11 task 結構與驗收條件不動（兩段制標記為新加，scope 不變）
> - 既有 A.1 ~ A.11 task 結構不動
> - 既有 B.0 ~ B.9 task 結構不動（僅補議題 registry 讀取要求）
> - 既有 C / D phase 全部不動
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-046 拍板不變；本輪只加 D-047 新議題 + Stage 0 patch round task 紀錄。
>
> Master 第五輪整合 owner：A.0.10 task + B Phase /create-* 議題 registry 對齊 + A.0F 兩段制保留。

---

> **v1.2 → v1.3 partial supersede 變動摘要（2026-05-19，master 第四輪整合）：**
>
> | TASKS 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | A.0 frontmatter parser | DF §11 + D-037/042/044/045 | 從「單一 task」擴為 **9 大類 tasks**（A.0.1 ~ A.0.9）對應 ARCH §12 |
> | **A.0F 新增前端工具任務群** | D-029/030 + Contract B + ARCH §13 | 新增 11 個 A.0F tasks（A.0F.0 ~ A.0F.11）— Phase A.0F |
> | A.5 init-project | D-025 + D-043 + D-038 | 補 entity_type_registry / qa_type_registry Template 拷貝 + `10_art_assets/` 目錄 + `.gitignore` `export/` |
> | **D.1a 新增** | D-026 + D-043 | 新增 09_g / 09_h / 09_i 三份 QA 模板 task |
> | D.4 /qa skill | D-043 | 5 報告 → 8 報告必跑 + 序列順序對齊 |
> | **C.5a 新增** | D-024 + D-038 + D-039 | 新增 Layer 3 Export prompt 生成器（前端 only，無新 skill）|
> | C.5 既有 4 /export-* | D-038 + D-046 #4 | 維持不動 + 不擴 JSON 輸出標註 |
>
> **north-star 對齊原則：** REQUIREMENTS_LOCK v1.0 > D-037~D-046 > D-001~D-036 > specialist v0.3 一致性。  
> 完整跨段對齊參考 `_design/INTEGRATION_CONTRACTS.md` v2.0 + `_design/SPEC.md` v1.1 + `_design/ARCHITECTURE.md` v1.2。

# 0. 文件定位

本文件是 4 階段實作任務的具體拆解，每個任務含：

- 任務編號
- 任務描述
- 依賴（必須先完成的任務）
- 產出檔案
- 驗收條件
- 禁止事項

CODEX 執行時應**按序執行**，但允許微跳（`Q17=B`）— 例如 Phase A 結尾若還有時間，可預作 Phase B 的協議文件。

Phase 之間原則上嚴格按序驗收。

---

# 1. 跨 Phase 通用規則

## 1.1 每完成一個任務的 commit 慣例

```
git add <相關檔案>
git commit -m "<phase>.<task>: <簡述>"

例：
git commit -m "A.1: add 00_e 世界觀創建協議"
git commit -m "A.5: implement /create-world skill with 中文 alias"
```

## 1.2 每完成一個任務必跑

```
python scripts/check_paths.py
python scripts/check_headers.py
```

若任一回報 ERROR，先修正再 commit。

## 1.3 通用禁止事項（每個任務都遵守）

- 不得擅自把 DRAFT 升 REVIEW 或更高狀態
- 不得修改 LOCKED 文件的核心內容
- 不得擅自補完重大世界觀／角色／劇情設定
- 不得把作品專屬內容寫入 Template repo
- 不得 force push、不得 commit 暫存檔
- 修改後必須回報 diff 摘要與影響範圍

## 1.4 全域文件頭規則（O4 鎖定）

**所有由 CODEX 在執行任務時新增的 `.md` 檔案**（包括：協議檔、模板檔、log 檔、報告檔、驗收紀錄等）**必須含 SPEC 5.2 的標準中文 header 5 欄位**：

```
狀態：DRAFT（或對應狀態）
版本：v0.1
最後更新：YYYY-MM-DD
適用範圍：<簡短描述>
優先級：<最高/高/中/低/一般>
```

依檔案類型補 YAML block（entities / depends_on / weight / 下游欄位）。

涵蓋但不限於：
- `_design/expected_entities.yaml` / `entity_exempt.yaml`（YAML 本身有 header 註解標準頭）
- `_design/wrapper_smoke_test_report.md`（A.9）
- `_design/phase_a_review_log.md`（A.10）
- `_design/phase_b_character_review_log.md`（B.5.5）
- `_design/phase_b_outline_review_log.md`（B.6.5）
- `_design/phase_b_review_log.md`（B.8）
- `_design/phase_d_task_review_log.md`（D.2.5）
- `_design/phase_d_dialogue_review_log.md`（D.3.5）
- 各 Phase 整體驗收報告（A.11 / B.9 / C.7 / D.7）
- 整體交付完成報告（D.7）

驗收時若任一新檔缺 header → ERROR。

## 1.5 錯誤呈現與使用者訊息規則（時期 C 整合 UX_SPEC §8）

所有 skill 在拒絕執行或回報錯誤時，必須遵循下列通用結構（詳細範本見 UX_SPEC §8 與 DECISIONS_LOG R13–R17）：

### 1.5.1 錯誤訊息四件套

任何拒絕或錯誤回報必含四欄：

```markdown
## ✗ 無法執行 / Cannot Proceed

- **What**：（簡短說明什麼失敗）
- **Where**：（精確指到檔案路徑 / 欄位 / 行）
- **Why**：（依本任務或 SPEC 規則說明）
- **下一步**：（祈使句，可立刻照做的動作）
```

「下一步」用祈使句，避免「應該」「可能」「建議考慮」等模糊詞。

### 1.5.2 使用者錯誤 vs 系統狀態未滿足（兩種口氣）

- **使用者錯誤**（指令拼錯、ID 不存在、參數缺失）→ 標題用 `## ✗ 無法執行 / Cannot Proceed`，口氣客觀、可操作、不指責
- **系統狀態未滿足**（先決條件不夠成熟、需等其他階段完成）→ 標題用 `## ⏸ 條件未滿足 / Prerequisites Not Met`，口氣是「等什麼條件解除、解除後做什麼」，**不要寫成像使用者犯錯**

### 1.5.3 空狀態文案

不只說「無 X」，要說「為什麼是正常」或「下一步可考慮」。用 `*斜體*` 包覆，跟正式內容區隔。

範例：
```markdown
## 卡點 / Blockers

*目前無卡點 — 所有實體已通過先決條件檢查。可考慮跑 `/scene-task` 啟動下一場 dialogue 生產。*
```

### 1.5.4 多錯誤累積彙整

命中多個錯誤時用「彙整 + 逐項展開」，**不平鋪四件套四次**：

- 標題前置「— N 項問題」讓使用者知道規模
- 每問題保留 Where + 下一步兩欄（What/Why 在標題與彙整段已說）
- 末尾加「整體下一步」收束

### 1.5.5 不暴露 enum 鍵 / debug 給使用者

- 不顯示 stack trace、error code
- 不顯示內部 enum 鍵（如 `pipeline_state: TASK_REVIEW`），改為人類可讀詞（「任務包已升 REVIEW」）
- debug 紀錄寫入 `_design/<phase>_review_log.md` 或 `.protocol_version.phase_log`，**不**印在 chat
- 例外：`--verbose` / `--debug` 旗標可附技術細節（由各 skill SKILL.md 自行定義）

### 1.5.6 4 個符號系統（DECISIONS_LOG D-006）

- ✓ 成功 / 完成
- ⏸ 條件未滿足（gate 擋住，可解決）
- ⚠ 注意但可繼續
- ✗ 使用者錯誤（必須修正）

所有 skill 訊息一致使用此符號系統。

## 1.6 全文呈現約束（時期 C 整合 UX_SPEC §0）

所有 skill 產出的 chat 訊息與檔案內容必須遵循：

- **純 Markdown**：無 GUI 元件、無 `<details>` 展開、無內嵌 HTML（除 GFM 廣泛支援的非互動標籤）
- **中文主＋英文 sub 命名**：標題與一級區塊用「中文 / English」格式（例：「邏輯實體完成度 / Entity Completion」）；表格欄位、代碼塊內、頻繁重複的次級標籤可省 sub
- **跨檔 link**：以 project root 為基準（`/` 開頭，例如 `/01_world/01_a_世界觀總覽.md`），不用相對路徑
- **文件越長越靠前頭放**：「下一步」「重點摘要」「TOC」

### 1.6.1 三條核心守則 G1 / G2 / G3（UX_SPEC §0 / UX_PRIOR_DRAFT 平移）

- **G1：badge 不單獨呈現** — 任何狀態 badge 必須搭配 checklist 或計數，避免單一狀態欄位收斂多重狀態信號
- **G2：流程視覺化僅為閱讀順序，不是 state machine** — 任何 `/status` 或 view 中的階段順序，旁邊明寫「閱讀順序用，不代表強制執行步驟」
- **G3：UX grouping 不是資料層必要單位** — beat、章節分組等可用於排版，但格式不能假設「每場必有 beat」「每份角色必有弧線段」

## 1.7 設計階段完成度檢查（v1.2 / v0.4 修正：A.0 暫停啟動）

**初代 master 補充裁決（D-018 後續指示）：暫停所有 Phase A.0+ 啟動建議。**

CODEX **不得**在以下條件全部滿足前啟動任何 Phase A.0 任務（含 A.0 parser/helper、A.4 frontmatter 補完等「不依賴第二輪」的任務也暫停）：

1. ✗ UX_SPEC §2 / §3 / §4 / §5 / §6 / §9 / §10「Batch X 補完」段交付
2. ✗ UPSTREAM_DOWNSTREAM_SPEC §9「需 master 裁決問題清單」集中段交付
3. ✗ DATA_FORMAT_SPEC.md 交付或正式紀錄不交付（P-006 釐清）
4. ✗ 第二輪 master 整合對話跑完，產出 PHASE_3_COMPLETION_REPORT v3.0+ 的 final 版本（標明可進 A.0）

**理由：**
- A.0 parser 設計與 phase_log.status 欄位（P-012 暫定）相關，若資料格式 specialist 推翻擴充，parser 需 rework
- A.4 既有模板 frontmatter 補完依 ARCHITECTURE §7.3 對照表，若有 schema 變動同樣 rework
- 後續任務（A.1 起）阻塞於 UX 第二輪，A.0 即使先做也無法立刻啟動 A.1
- 統一在「設計階段全部完成」後一次性開工，避免 rework 與決策不一致

**v0.3 修正內容（保留作參考）：UPSTREAM_DOWNSTREAM_SPEC.md 已 ≈90% 完成（3503 行）**，多數任務的 UPSTREAM 依賴已 ready；但因 v0.4 全暫停，本表「✓ ready」狀態僅為「**內容已 ready，但實作仍暫停**」。

**主要剩餘阻塞點集中於 UX_SPEC.md 的 §2–§6** 待第二輪 UX specialist 補完。

| 任務 | 依賴 | 狀態 |
|---|---|---|
| A.1（寫 00_b 通用骨架） | UX_SPEC §6（QA 報告閱讀體驗，確認 00_b §6/§7 呈現規則） | ✗ UX §6 待第二輪 |
| A.3（寫 00_e 世界觀協議） | UPSTREAM §1.1 + 共通 §1.0 | ✓ 已 ready |
| B.0（寫 00_l 關係創建協議） | UPSTREAM §1.5 + 共通 §1.0 | ✓ 已 ready |
| B.1（寫 00_f 角色協議） | UPSTREAM §1.2 + 共通 §1.0 | ✓ 已 ready |
| B.2（寫 00_g 大綱協議） | UPSTREAM §1.3 + 共通 §1.0 | ✓ 已 ready |
| B.3（寫 00_h 細綱協議） | UPSTREAM §1.4 + 共通 §1.0 | ✓ 已 ready |
| D.0（寫 00_k 流程協議） | UPSTREAM §2 + §6（多場景並行） | ✓ 已 ready |
| D.1（寫 09_f 類型偏移檢查模板） | UPSTREAM §3.5 | ✓ 已 ready |
| D.3 `/dialogue-write` skill | UPSTREAM §4 三模式 algorithm | ✓ 已 ready |
| D.4 `/qa` 5+1 報告 | UPSTREAM §3 + UX §6 呈現 | △ 邏輯 ready；UX 呈現待 §6 |
| D.4 / D.5 既有 08_a §11.1 修正（**P-009** 暫定，原 D-011） | SPEC §12.10.1 / UPSTREAM §3.6.2 | △ 內容 ready；待第二輪 specialist §9 正式提案 |
| C.3 `/view-*` skills | UX §2（4 個 Markdown 模板） | ✗ UX §2 待第二輪 |
| C.5 `/export-*` skills | UX §3（檔案 layout）；本檔 §1.6 已給通用約束 | △ 通用約束 ready；具體 layout 待 §3 |
| A.7 `/status` skill | UX §4 看板格式 | △ 邏輯 ready；UX 呈現待 §4 |
| A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5 gates | UX §5 清單格式 | △ 邏輯 ready；UX 呈現待 §5 |
| `.protocol_version.phase_log` 加 `status` 欄位（**P-012** 暫定，原 D-014） | SPEC §5.4 範例已加 | △ TASKS A.5 暫定加；待資料格式 specialist 正式確認 |
| 多場景並行 mutex 機制（**P-015** 暫定，原 D-017） | ARCHITECTURE §6.7.5；UPSTREAM §6.2 / §6.3 | △ 內容 ready；待第二輪 §9 正式提案 |
| Canon delta 框架紀錄（**P-011** 暫定，原 D-013） | SPEC §12.10 / UPSTREAM §5 | △ Phase D 後成熟期；本輪不實作 skill；待 §9 正式提案 |

~~A.0（parser/helper）與既有 27 份模板的 frontmatter 補完（A.4）**不依賴第二輪 specialist** — 可獨立啟動，但建議仍等資料格式 specialist 第二輪 formalize 後再開（避免 phase_log.status 欄位需要 rework）。~~

**v0.4 暫停（取代 v0.3 建議）：** A.0 與 A.4 也暫停啟動，等三個 specialist 全部完成 + 第二輪 master 整合完成後再啟動。

詳見 DECISIONS_LOG.md §5.5「第二輪 specialist 補完清單」與本檔 §1.7 暫停條件。

---

# 2. Phase A — 地基 + Bootstrap + 世界觀

**目標：** 使用者能從零開新專案、建好世界觀、查看進度。

**Phase A 完整驗收：**
1. 跑 `/init-project` 能完整完成 bootstrap，產出 `.protocol_version` 與初始目錄
2. 跑 `/create-world` 能依場景化對話跑完 5 階段，自動拆分到 `01_a` `01_b` `01_c` / `02_*` / 作品專屬 `00_b`（view/ export 留待 Phase C）
3. 跑 `/status` 能看到 W-rules / W-language / V 三個實體完成度
4. 跑 `/check-gaps` 能列出待補項
5. `check_paths.py` 與 `check_headers.py` 都 0 error

## A.0 實作 frontmatter parser / helper（前置任務 — v1.1 partial supersede via D-037~D-046 + ARCH §12）

**v1.1 變動摘要：** A.0 由「單一 parser task」擴為「**9 大類 parser tasks**」對應 ARCH §12.1 + DF §11.1。原 v1.0 A.0 任務描述為 v1.1 「A.0.1 frontmatter parser 基線」（仍為 Phase A.0 第一個 task）；其他 8 大類在 A.0.2 ~ A.0.9 對應 ARCH §12.1.2~12.1.9。

**實作依賴：** 無

**啟動 gate（v1.1 新增 — 對齊 PHASE_3_COMPLETION_REPORT §6.2a）：** 本 task 屬 Phase A.0 範圍；啟動前 PHASE_3_COMPLETION_REPORT §6.2a 全 4 項條件必須達成（三 spec v0.3 + 主 SPEC v1.1 + ARCH v1.2 + TASKS v1.3 + INTEGRATION_CONTRACTS v2.0 全標 LOCKED + DECISIONS_LOG v1.0 + Phase A.0.1 任務描述定稿 + CODEX (d) 短審 clean）。Master 第四輪 / 第五輪整合對話完成升 LOCKED 後才可開工。

**整體產出（v1.1 — 對應 ARCH §12 + Contract A.1~A.7）：**
- `scripts/parse_frontmatter.py`（新檔）— 共用 parser 模組
- 更新 `scripts/check_headers.py` 引用上述 parser
- `_design/expected_entities.yaml`（新檔）— Expected Entity Manifest 源檔
- `_design/registries/entity_type_registry.template.yaml`（v1.1 新）
- `_design/registries/qa_type_registry.template.yaml`（v1.1 新）

### A.0.1 frontmatter parser 基線 + phase_log 完整解析（對應 ARCH §12.1.1 + Contract A.2）

**依賴：** 無

**產出：**
- `scripts/parse_frontmatter.py` 含 phase_log 完整解析
- 8 enum 欄位驗證 + 5 v1.1 新欄位驗證

**做法：**

1. **基線 parser 實作**（依 SPEC §5.2 canonical schema + ARCH §2.2 normalized return）：
   - 解析中文 header 5 必填欄位（接受半形 / 全形冒號）
   - 偵測並解析後續 YAML block（`---` ... `---`）
   - YAML block 內容含**上游 3 欄**：`entities` / `depends_on` / `weight`
   - YAML block 內容含**下游 8 欄**（pipeline 產物用）：`scene_id` / `source_task` / `source_dialogue` / `source_dialogues` / `pipeline_state` / `mode_tag` / `qa_decision` / `qa_type`
   - **v1.1 新增：** YAML block 容納 `dialogue_keys` Map（下游台詞檔）+ `art_metadata` List（A-* metadata 檔）— 詳見 A.0.2 / A.0.4
   - `weight` 支援 scalar 與 map 兩種型態
   - 容忍純 header 檔（協議檔通常無 YAML block）
   - 缺欄位處理：必填欄位缺 → ERROR；YAML block 欄位缺 → WARN
   - 支援 7 種狀態：DRAFT / REVIEW / FINAL / LOCKED / DEPRECATED / APPLIED / DERIVED
   - **下游 enum 驗證（v1.1 對齊 SPEC §5.2.4）：**
     - `pipeline_state` ∈ {SCENE_INDEXED, TASK_DRAFT, TASK_REVIEW, DIALOGUE_TRIAL, DIALOGUE_CONVERGED, QA_PASSED, QA_FAILED, DIALOGUE_FINAL, DIALOGUE_LOCKED, null}
     - `mode_tag` ∈ {ORGANIZED, DRAFT_TRIAL, EXPERIMENTAL, CONVERGENCE, FINAL_CANDIDATE, **SINGLE_ITER**, null}（v1.1 / D-027）
     - `qa_decision` ∈ {PASS, FAIL, ARBITRATE_REQUIRED, null}
     - `qa_type` ∈ {AI_FLAVOR, VOICE_CONSISTENCY, FORBIDDEN_WORD, INFO_CONTROL, GENRE_DRIFT, **RHYTHM, DRAMATIC_TENSION, CROSS_SCENE_CONTINUITY**, null}（v1.1 / D-043；加 registry 解析後變可擴充）
   - **下游欄位偵測**：parser 看到任一下游欄位非 null → 標記檔案為 `is_pipeline_artifact: True`

2. **phase_log 完整解析（v1.1 新 — 對應 Contract A.2 + DF §3 / §11.1.1）：**
   - 解析 `.protocol_version.phase_log[*]` 每筆 entry
   - **8 個 enum / 必填欄位驗證：**
     - `status` ∈ {`completed`, `in_progress`, `aborted`}；省略視為 `in_progress`（保守解讀）
     - `status: aborted` 必有 `abort_reason` + `detail` → 缺 ERROR
     - `import_source` ∈ {`agent_assisted`, `external_llm`, null}
     - `import_source != null` 但 skill 不是 `/create-*` 系列 → ERROR
   - **5 個 v1.1 新欄位（D-042）：**
     - `entities_touched: List[entity_id]`（多場景並行 mutex；省略視為空 list；abort 因並行衝突時必填）
     - `iteration_count: int`（僅 SINGLE_ITER 有意義）
     - `iteration_note: str`（僅 SINGLE_ITER 有意義）
     - `base_dialogue: file_path`（僅 SINGLE_ITER 且 iteration_count >= 2 必填；指向另一檔 path；**不允許 cycle** → cycle 偵測 ERROR）
     - `conflict_resolutions: List[dict]`（僅 import_source != null 有意義；驗證 decision enum + create-as-new 必填 new_entity_id）

3. **Expected Entity Manifest 初值**（依 SPEC §5.4）：
   - 寫入 `_design/expected_entities.yaml`
   - 列出每個 phase 完成後應該存在的實體類別

4. **Entity-exempt 清單**：
   - 協議檔（00_a–00_l）不必標 entities
   - 模板檔（03_b、03_c）不必標 entities（實際 Instance 角色檔才標）
   - 此清單寫入 parser 配置或 `_design/entity_exempt.yaml`

**驗收：**
- `python scripts/check_headers.py` 0 ERROR（沿用既有檔案）
- 對 27 份既有模板 + 任一含 YAML block 的測試檔解析無錯
- **下游欄位驗證測試**：建立一個假測試檔含 `pipeline_state: DIALOGUE_TRIAL`、`mode_tag: DRAFT_TRIAL`、`source_task: ...`，parser 能完整正確解析並標 `is_pipeline_artifact: True`
- **Enum 驗證測試**：對 `pipeline_state: INVALID_STATE` 之類錯誤值應報 WARN
- **v1.1 SINGLE_ITER 驗證測試**：mode_tag=SINGLE_ITER 範例檔，iteration_count: 2，base_dialogue 指向 iter1，parser 正確解析；base_dialogue cycle 範例正確 ERROR
- **v1.1 phase_log 驗證測試**：手稿導入路徑（`import_source: agent_assisted` + `conflict_resolutions` 多筆）正確解析；agent_assisted 但 skill 不是 /create-* 正確 ERROR
- `expected_entities.yaml` 內容對齊 SPEC §5.4 manifest 表

**禁止：**
- 不得改動既有 27 份模板的 header 內容（A.4 才做）
- 不得自行決定 Expected Entity Manifest 內容（嚴格對齊 SPEC）

### A.0.2 dialogue_keys Map 解析 + 內文 KEY comment 一致性（對應 ARCH §12.1.2 + Contract A.1）

**依賴：** A.0.1

**產出：**
- `scripts/parse_frontmatter.py` 補 `parse_dialogue_keys_map(file_path) -> Dict[str, DialogueKeyEntry]`
- 解析下游台詞檔內文 HTML comment `<!-- KEY: ... -->` 與 frontmatter 一致性驗證

**做法：**
1. 解析下游 `08_dialogue_outputs/**/*.md` frontmatter `dialogue_keys` Map（v0.2 D-037 shape）
2. 解析內文 HTML comment `<!-- KEY: <key> -->`
3. **驗證（DF §11.1.2 + D-037 + C-10 解決）：**
   - KEY ↔ map key 一致性 → 不一致 ERROR
   - `line_index` 順序 ↔ 內文 KEY comment 順序一致 → 不一致 ERROR
   - 一檔內 map key unique（YAML 本身保證）
   - KEY 命名符合 §4.1 預設語法 / user-defined
   - `aliases[0]` 為預設名格式
   - `status` ∈ {`active`, `deprecated`, `deleted`}
   - `status: deleted` 必有 `deleted_at`；`status: deprecated` 必有 `deprecated_reason`
   - `portrait` / `bgm`（非 null）必須對應 valid A-* asset_id（cross-check `art_metadata`；依賴 A.0.4）
   - `sfx` list 各元素必須對應 valid A-sfx-*
   - **`source_keys`（v1.1 新增 via master 第四輪 CC-04 校正）** — 句級收斂 lineage；list 或 null；list 內每個 KEY 必須對應 valid 既有 KEY（cross-check 全 repo KEY + alias unique 集合，§A.0.3）；非 v02 收斂版台詞檔的 entry 若有 source_keys 非 null → WARN「source_keys 僅 v02 收斂版有意義」
   - 內文 `<!-- 立繪：A-... -->` / `<!-- BGM：A-... -->` 提示與 frontmatter 不一致 → **WARN**（非 ERROR）

**驗收：** dialogue_keys Map 測試檔（含 active / deprecated / deleted 三狀態）解析無錯；故意製造 KEY ↔ map key 不一致 → ERROR。

### A.0.3 全 repo KEY + alias unique 集合 + 反向索引（對應 ARCH §12.1.3 + Contract A.1 + A.4）

**依賴：** A.0.2

**產出：** parser 提供 `get_all_dialogue_keys() -> Set[str]` + `get_alias_to_current_key_map() -> Dict[str, str]`

**做法：**
1. 啟動時掃描所有 `08_dialogue_outputs/**/*.md`
2. 建全 repo KEY 集合：`⋃ (map_key) ∪ ⋃ (entry.aliases[*])`
3. `status: deleted` entry 的 map key 與 aliases **仍計入** unique 集合（KEY 不重用原則）
4. 任何新增 / 改名前先查集合；衝突 ERROR
5. 建反向索引 `alias → 當前 KEY + 檔案路徑`

**驗收：** KEY 全 repo unique 集合測試；alias 跨檔 lookup 正確。

### A.0.4 art_metadata + A-* prefix 識別（對應 ARCH §12.1.4 + Contract A.3 + C.5）

**依賴：** A.0.1 + A.0.7（entity_type_registry）

**產出：**
- parser 提供 `parse_art_metadata(file_path) -> List[ArtMetadataEntry]`
- `get_asset_completeness_by_subtype() -> Dict[Subtype, CompletenessStats]`（D-045 獨立 API）

**做法：**
1. 識別 entity 類型 prefix `A-*` 加入 valid set
2. 掃描 `10_art_assets/**/*.md` 目錄；**不存在統一 registry 檔**（D-041）
3. 解析 frontmatter `art_metadata` block 各 entry
4. **v0.2 subtype 驗證（D-044）：**
   - 值在 `allowed_values` 7 種內：portrait / bg / cg / sfx / bgm / voice / ui
   - 在 `reserved_subtypes` 內（icon / effect / video / shader）→ ERROR
5. **v0.2 owner 驗證：**
   - `subtype: portrait` 的 owner 必對應既有 C-* entity → 不對應 WARN
   - `subtype: voice` 的 owner 必對應 C-* + `dialogue_keys_ref` 必填且對應既有 KEY → WARN
6. **強制禁止欄位偵測（DF §5.7）：** `file_path` / `url` / `source_image` / `binary_data` / `base64_*` → ERROR
7. asset_id 全 repo unique（含 aliases；同 A.0.3 機制延伸）
8. **v0.2 完成度（D-045）：** parser 提供獨立 API `get_asset_completeness_by_subtype()` 給前端 Asset Panel；**不**納入 narrative `/status` expected entity manifest 比對

**驗收：** 7 種 subtype 範例檔解析無錯；reserved_subtype 範例 → ERROR；禁止欄位範例 → ERROR；Asset 完成度與 narrative 完成度分離。

### A.0.5 內文 A-* cross-reference 解析（對應 ARCH §12.1.5 + Contract A.1 + A.3）

**依賴：** A.0.2 + A.0.4

**做法：**
1. 解析下游台詞檔 / 任務包內文 `<!-- 立繪：A-... -->` / `<!-- 背景：A-... -->` / `<!-- BGM：A-... -->` / `<!-- SFX：A-... -->` 等 HTML comment
2. **v0.2 規則（per DF §4.3 + D-037）：**
   - 內文 art comment **僅 view-layer 提示**，非權威來源
   - 句級 A-* 權威來源 = frontmatter `dialogue_keys[<KEY>].portrait/bgm/sfx`
   - 不一致 → WARN（非 ERROR — 允許編輯期間暫時不同步）
3. 對照 frontmatter `depends_on` — 內文引用 A-* 但 `depends_on` 未列 → WARN
4. 引用歷史 alias（非當前 asset_id）→ WARN「建議改用當前 ID」

**驗收：** 內文 art comment vs frontmatter 不一致範例 → WARN（非 ERROR）。

### A.0.6 mode_tag / qa_type 擴充 enum + registry 解析（對應 ARCH §12.1.6 + Contract A.5 + A.6）

**依賴：** A.0.1 + A.0.7 + A.0.8

**做法：**
- `mode_tag` valid set 加 SINGLE_ITER（基線 5 → 6 種；v1.1 / D-027）
- `qa_type` valid set 加 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY（基線 5 → 8 種；v1.1 / D-043）
- `qa_type` set 變開放可擴充（依賴 A.0.8 registry 解析）

**驗收：** SINGLE_ITER + 8 種 qa_type 全部 enum 識別正確。

### A.0.7 entity_type_registry 讀取（對應 ARCH §12.1.7 + Contract A.5）

**依賴：** A.0.1

**產出：**
- `_design/registries/entity_type_registry.template.yaml`（新檔；對齊 DF §7.2）
- parser 提供 `get_entity_type_registry() -> EntityTypeRegistry`

**做法：**
1. 啟動時讀 `<instance_root>/entity_type_registry.yaml`
2. 不存在 → fallback `_design/registries/entity_type_registry.template.yaml` + WARN
3. 載入 `core` + `user_extensions` 為 valid entity type set
4. 對 frontmatter `entities` / `depends_on` 內每個 ID：
   - 取 prefix 比對 valid set → 不在 set 內 ERROR
   - 依 entry 的 `id_pattern` regex 驗證 ID 格式 → 不符 ERROR
5. **對 user_extensions 驗證：**
   - `type` 不可跟 core 重複（ERROR）
   - `type` prefix 不可在 `reserved_prefixes` 內（WARN）
   - `id_pattern` 為 valid regex（ERROR 否則）
   - `target_dir` 為 valid 相對路徑（WARN 若 dir 不存在）
6. 偵測「現存 X-* entity 但類型 X 已從 registry 移除」→ ERROR（防 silent drop）

**驗收：** Template/Instance registry 機制 + core/user_extensions 對齊測試。

### A.0.8 qa_type_registry 讀取（對應 ARCH §12.1.8 + Contract A.5）

**依賴：** A.0.1

**產出：**
- `_design/registries/qa_type_registry.template.yaml`（新檔；對齊 DF §8.2）
- parser 提供 `get_qa_type_registry() -> QaTypeRegistry`

**做法：**
1. 啟動時讀 `<instance_root>/qa_type_registry.yaml`
2. 不存在 → fallback Template + WARN
3. 載入 `core` + `user_extensions` 為 valid qa_type set
4. 對 QA 報告檔 frontmatter `qa_type` 驗證在 set 內
5. 對 `user_extensions[*].template_path` 驗證對應檔案存在於 `09_quality_assurance/`（不存在 → ERROR）
6. 對應 09_x 模板 frontmatter `qa_type` 值與 registry entry 對應（不對應 → WARN）

**驗收：** 8 core qa_type + user 加新 qa_type + 09_x 模板對應測試。

### A.0.9 JSON export 結構化資料 API（對應 ARCH §12.1.9 + Contract A.7）

**依賴：** A.0.1 ~ A.0.8

**做法：**
- parser **不直接負責 export**，但提供「結構化資料」API 給 export agent（Layer 3 Export A1 prompt agent）使用
- API 形狀（建議；具體簽名屬 Phase A.0 實作決定）：
  - `get_all_entities() -> List[EntityRecord]`
  - `get_all_dialogue_lines() -> List[DialogueLineRecord]`（按 KEY 排序）
  - `get_all_art_metadata() -> List[ArtMetadataRecord]`
  - `get_manifest_snapshot() -> ManifestSnapshot`（含 registry snapshots）
- 對應 DF §9 JSON output schema 一對一映射（DF §9.7）

**驗收：** API 回傳的 records[] 各條 schema 對齊 DF §9.4-§9.6；manifest snapshot 含 entity_type_registry + qa_type_registry 完整快照。

### A.0 完整驗收（v1.1 — 9 大類 task 全部完成後）

- A.0.1 ~ A.0.9 各自驗收項全 pass
- `python scripts/check_headers.py` 0 ERROR
- A.4 任務可依賴此 parser
- 後續 frontend server / Layer 3 Export agent 可直接 import parser API

**禁止（v1.1 維持原文 + 補新）：**
- 不得改動既有 27 份模板的 header 內容（A.4 才做）
- 不得自行決定 Expected Entity Manifest 內容（嚴格對齊 SPEC）

### A.0.10 Parser patch round — 3 critical fix（v1.4 新增；對應 ARCH §12.A.0.10 + Stage 0）

**狀態：** ✅ **DONE**（CODEX 2026-05-19 PASS）

**依賴：** A.0.1 ~ A.0.9 全完成 + Gate 1 CODEX review NO-GO 觸發

**觸發背景：** Gate 1 CODEX review 識出 3 critical parser integration gap（NO-GO 判定）— build_repo_index 未整合 cross-ref validator + entity ID 一般驗證未跑 + Windows UTF-8 BOM 漏讀。

**做法：**
- master 第五輪委派新 CODEX 對話跑 patch round（starter scope 嚴限 3 critical + 不准動 LOCKED spec）
- 3 critical：
  - C1: 新建 `_validate_dialogue_files_with_art_index()` + 整合 `validate_body_vs_frontmatter_consistency()` + issue 去重
  - C2: 新建 `_validate_frontmatter_entity_id_fields()` 對 frontmatter entities / depends_on 跑 `validate_entity_id`
  - C3: `parse_file()` 改 `encoding="utf-8-sig"` + 其他讀檔入口同步

**驗收：**
- 6 synthetic case 全 PASS（missing A-* / body A-* not in depends_on / historical alias / unknown entity prefix / invalid pattern / UTF-8 BOM）
- `python scripts/check_headers.py` 維持 0 ERROR（75 files / 13 WARN）
- `build_repo_index('.')` 維持 0 ERROR（parsed_files=99 / 43 WARN）
- 100 fake dialogue perf < 5s（實測 0.44s）
- 不動 LOCKED spec
- 產出 CODEX_A010_PATCH_REPORT.md

**不在 scope（屬 Phase A.X 後續 patch round）：**
- M1 normalized return contract
- M3 get_all_dialogue_lines 排序對齊 spec
- M4 scene scope voice asset coverage
- m1-m3 docstring / dead hook / template comment header polish
- 議題 registry 載入（D-047 — 屬 Phase A.X 後續或 Phase B 實作前）
- deleted KEY 內文存在性 WARN（NEW_REQ_3 — 屬 Phase A.X 後續）

**Cross-ref：** `_design/CODEX_A010_PATCH_STARTER.md` / `_design/CODEX_A010_PATCH_REPORT.md` / DECISIONS_LOG §6.9.7
- **不得**讓 parser 寫檔（parser 是 read-only；寫檔是 skill 責任）
- **不得**在 A.0.1 ~ A.0.9 內擅啟 frontend server（屬獨立 Phase A.0 frontend adapter task 群，見 §A.0F）

---

## A.1 寫 `00_protocol/00_b_反 AI 味檢查表.md`（通用骨架）

**依賴：** 無
**產出：** `00_protocol/00_b_反ai味檢查表.md`
**做法：**
- 從 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md` 反推通用骨架
- **保留**：結構（檢查表分類、QA 報告格式、模式差異表、高風險詞分類、句型檢查、髒話檢查、死亡處理、聲線污染、報告格式）
- **移除**：所有作品專屬內容（蟲潮孤堡、黑翼、蟲災、瑟琳、莉娜、諾拉等）
- **替換**：作品專屬範例改為通用範例（用 `<作品名>`、`<角色 A>`、`<反派 B>` 等占位符）
- **加上 frontmatter**：status: DRAFT, version: v0.1, last_updated: 2026-05-17, entities: 無（協議檔不貢獻實體）

**驗收：**
- 文件中不出現任何具體作品名稱、具體角色名稱
- 結構與蟲潮孤堡版對照，骨架完整
- 適用範圍寫「全作品通用骨架」
- **必須含 SPEC 17.1 的 7 個固定 section anchors（O2）：**
  - `## 1. 作品類型語氣定位`
  - `## 2. 髒話尺度與死亡處理偏好`
  - `## 3. 規模定位`
  - `## 4. 類型偏移風險清單`
  - `## 5. 角色偏移檢查清單`
  - `## 6. 高風險場景的處理方式`
  - `## 7. 經驗累積的偏移案例`
- 順序、名稱完全一致（CODEX 不得擅自重新命名 section）

**禁止：**
- 不得保留任何蟲潮孤堡專屬內容
- 不得創造新的「作品專屬內容」（這是 Instance 在 Bootstrap 階段才做的事）
- 不得改動 7 個 section anchor 名稱與順序

## A.2 寫 `00_protocol/00_i_專案初始化協議.md`

**依賴：** A.1（00_b 通用骨架完成才能在 i 中提及）
**產出：** `00_protocol/00_i_專案初始化協議.md`
**內容：**
- 沿用 SPEC.md 第 8 節定義的「10 區段共通骨架 + Bootstrap 專屬區段」
- 階段 1：診斷模式 — 接收新專案基本資料
- 階段 2：探索 — 列出可微調的 Template 文件（限 00_b / 00_c / 00_d）
- 階段 3：收斂 — 使用者拍板每個微調
- 階段 4：執行 — 寫 `.protocol_version`、套用微調
- 階段 5：驗證 — 報告 Bootstrap 完成狀態
- 專屬區段：`.protocol_version` YAML 格式範本、微調清單範本、Bootstrap 完成後的標準目錄狀態

**驗收：**
- 結構符合 SPEC 第 8 節
- 明確標示「Bootstrap 允許微調的文件限定 00_b / 00_c / 00_d」
- `.protocol_version` 範本完整

**禁止：**
- 不得允許微調 `00_a`、`00_e`–`00_j`、`01–09` 模板

## A.3 寫 `00_protocol/00_e_世界觀創建協議.md`

**依賴：** A.1

**產出：** `00_protocol/00_e_世界觀創建協議.md`

**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §1.1（含 11 議題完整 agent 提問腳本、寫檔規則、拆分 algorithm）+ §1.0.1 共通骨架執行細則 + §1.0.2 觸發語字典 + §1.0.3 先決資料缺失流程

**做法：**
- 依 UPSTREAM §1.1 完整內容寫協議檔；CODEX 不擅自更動 UPSTREAM 已規定的提問腳本與拆分規則
- 沿用 SPEC §9「共通骨架 10 區段」+ §10.1 11 項議題清單作為章節骨架
- 階段 4 自動拆分依 UPSTREAM §1.1.2 區段 10.11 表
- 階段 5 自動呼叫 `/status`

**驗收：**
- 11 項專屬區段完整，每項含 UPSTREAM §1.1.2 的「為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答 / 跳題」5 欄
- 拆分規則明確（依 UPSTREAM §1.1.2 §10.11 表）
- frontmatter 規範依 UPSTREAM §1.1.2 §10.11 末段
- 階段 5 明確要求自動呼叫 `/status`
- 區段 1–9 的執行細則依 UPSTREAM §1.0.1

**禁止：**
- 不得在協議中提及任何具體作品
- 不得擅自更動 UPSTREAM §1.1 提案的提問腳本或拆分規則（要動須先回 master）

## A.4 補完既有 27 份模板的 frontmatter（entities + depends_on + weight）

**依賴：** A.0（parser/helper 必須先存在才能驗證）

**產出：** 修改所有既有檔案的 header（在中文 header 後加 YAML block）

**做法：**
- 採用 SPEC 第 5.2 節的 Canonical Schema（中文 header + YAML block）
- 依 ARCHITECTURE 第 7.3 節的對照表加上 `entities`、`depends_on` 與 `weight`（M6 三欄一起補）
- 既有檔案的 status / version / last_updated 等不動

**驗收：**
- 跑 `python scripts/check_headers.py`，所有檔案 0 error（依 A.0 parser 規範）
- 隨機抽 3 個檔案目視確認 `entities` 寫對
- 隨機抽 3 個檔案目視確認 `depends_on` 寫對（依 7.3 表初值）
- 隨機抽 1 個 04_a 確認 `weight` 為 map 型態

**禁止：**
- 不得改動既有檔案的內容（只動 frontmatter）
- 不得擅自升級狀態
- 不得修改 7.3 表中已列的 entities / depends_on 初值（要改先回 ARCHITECTURE 改表）

## A.5 實作 `/init-project` skill（含中文別名）+ `.protocol_version` schema 設計（v1.1 partial supersede via D-025 + D-043）

**v1.1 變動摘要：** A.5 在 v1.0 基礎上補「Template registry 拷貝步驟」 — Instance bootstrap 時必須從 Template 複製 `entity_type_registry.template.yaml` → `entity_type_registry.yaml` 與 `qa_type_registry.template.yaml` → `qa_type_registry.yaml`。

**依賴：** A.2 + A.0.7 + A.0.8（registry parser ready）

**產出：**
- `.claude/skills/init-project/SKILL.md`
- `.claude/skills/初始化專案/SKILL.md`（採 wrapper 策略）
- `.protocol_version` schema 鎖定（依 SPEC §5.4 phase_log + Bootstrap 微調）
- **v1.1 新增 Bootstrap 步驟：** 從 Template 複製 `entity_type_registry.yaml` + `qa_type_registry.yaml` 到 Instance root
- **v1.1 新增 Bootstrap 步驟：** Instance root 加 `.gitignore` 列 `export/`（D-038 附帶第 3 項）
- **v1.1 新增 Bootstrap 步驟：** 建立 `10_art_assets/` 目錄結構（7 subtype 索引檔 + 7 subtype 子目錄）

**做法：**
- SKILL.md 內容遵循 ARCHITECTURE 第 3.3 節 skill 內容規範
- description 寫明：「建立新 Instance repo 的 Bootstrap 流程。從 Template clone 後執行，引導使用者完成專案初始化、Template 微調、`.protocol_version` 紀錄。」
- 中文 wrapper 的 description：「`/init-project` 中文別名 — 觸發新專案初始化流程。」
- `.protocol_version` 初始 schema（M4）：

```yaml
template_source: github.com/<user>/game-dialogue-bible-template
template_commit: <commit-sha>
bootstrap_date: YYYY-MM-DD
project_name: <作品名>

customizations:
  - file: 00_protocol/00_b_反ai味檢查表.md
    type: 專案化
    note: ...

phase_log:
  - phase: bootstrap
    date: YYYY-MM-DD
    skill: /init-project
    created_entities: []
    scene_ids: []
    customizations: [<上面的 customizations 條目>]
```

`/init-project` 跑完階段 5 時 append 此 bootstrap 條目到 `phase_log`，後續每個 skill 在自己的階段 5 也 append 一筆。

**`status` 欄位（v1.1 — D-042 已 formalize；P-012 RESOLVED 為歷史標註）：** 每筆 phase_log entry 必須含 `status: <completed | aborted | in_progress>`（正式欄位；DATA_FORMAT_SPEC v0.2 §3.2 已 formalize；DECISIONS_LOG §6.7.3 P-012 RESOLVED via D-042）：
- `completed`：skill 正常完成階段 5（預設）
- `in_progress`：skill 進入階段 1 後寫入；正常完成階段 5 時改為 `completed`
- `aborted`：skill 因並行衝突 / rollback 等中止；含 `abort_reason` 與 `detail` 欄位

Bootstrap 條目示例（v1.1 — 補 status 欄位）：

```yaml
phase_log:
  - phase: bootstrap
    date: 2026-05-17
    skill: /init-project
    status: completed                        # v1.1 D-042 已 formalize
    created_entities: []
    customizations: [<上面的 customizations 條目>]
```

完整範例見 SPEC §5.4 + §5.4a phase_log schema（含 5 個 v1.1 新欄位）。

**驗收：**
- 在 Claude Code 中輸入 `/init-project` 與 `/初始化專案` 都能觸發
- skill 依 00_i 協議跑 5 階段流程
- 跑完後產生有效的 `.protocol_version` YAML 檔，含 `phase_log` 段落且第一筆是 bootstrap 紀錄 + `status: completed`
- 跑完後輸出「建議下一步跑 `/create-world`」
- 此檔案本身有標準文件頭（O4）

**禁止：**
- 不得允許微調 00_a、00_e–00_j、01–09 模板（必須阻擋）
- 不得手動編輯 `.protocol_version` 的 `phase_log`（只能由 skill 末段寫入）

## A.5b Critical patch round — Template-detect 機制（v1.6 新增 via D-049 + NEW_REQ_8；master 第六輪已完成）

**性質：** 歷史紀錄類 task — master 第六輪 Critical patch round 已 inline 完成；本段紀錄 patch scope / 落地檔 / 驗收結果。

**依賴：** A.5 ✓ DONE（init-project skill 已 implemented）；M1 user-test 跑完發現 M1-CRITICAL-01

**觸發背景：** M1 user-test 後續發現 user 跑 /init-project 透過 Cowork 在 Template repo（D:\劇本開發工具）上跑通 5 階段，Template 被污染。根因為 00_i §2 既有 4 條啟動條件無法區分 Template vs Instance。屬 Critical 級緊急 patch（HANDOFF §3 階段 1 Critical 分流）。

**拍板：** D-049 採候選 d（候選 a + b 兩道防線組合）— 詳 DECISIONS_LOG §6.11.2。

**patch 落地清單（master inline 已完成）：**

| 檔 | 動作 |
|---|---|
| `00_protocol/00_i_專案初始化協議.md` | v0.1 → v0.2；§2 啟動條件加 #5（`.template_root` marker check）+ #6（registries template 殘留 + 未 bootstrap 推斷 check）+ 註腳說明兩道防線互補 |
| `.claude/skills/init-project/SKILL.md` | v0.1 → v0.2；「啟動前檢查」段加 2 條 bullet（對齊 00_i §2 #5 #6）+ 兩段完整拒絕文案模板 |
| `.template_root`（root，新建）| 新建 marker file（含說明 + cross-ref + 何時可刪指引）|
| `_design/ARCHITECTURE.md` | v1.4 → v1.5；§3.3 加新子節 §3.3.2「Template-detect 規範」段（三維度檢測規則 + 兩道防線理由 + 未來 bootstrap 類 skill 擴充規則）|
| `_design/DECISIONS_LOG.md` | v1.2 → v1.3；新 §6.11 + D-049 拍板紀錄 + Template 污染清理 cookbook |
| `_design/POST_LOCK_PENDING.md` | v0.2 → v0.3；NEW_REQ_8 RESOLVED via D-049 |
| `_design/TASKS.md`（本檔）| v1.5 → v1.6；本段 A.5b 紀錄 |

**未動：**
- `.claude/skills/初始化專案/SKILL.md`（極簡 wrapper 引用英文主檔自動跟）
- 三 Wave 4 starter（CODEX_A7 / CODEX_A8 / CODEX_A12）不動：A.7 / A.8 純讀 skill 不涉 bootstrap；A.12 文件檔，引用 init-project description 自動跟 v0.2（但 Wave 4 review 必須驗 A.12 產出對齊 v0.2 — 詳 §6.11.6）
- SPEC / IC / DF / UD / UX_SPEC / REQUIREMENTS_LOCK 全部不動

**驗收（master inline patch 驗證）：**
- 00_i header v0.2 標註存在
- init-project SKILL.md v0.2 標註存在 + 啟動前檢查含 D-049 第一/第二道防線 bullet + 兩段拒絕文案
- `.template_root` 存在於 D:\劇本開發工具/ root
- ARCH §3.3.2 段存在 + 三道檢測規則完整
- DECISIONS_LOG §6.11 + D-049 紀錄完整 + Template 污染清理 cookbook 存在
- 不動段：SPEC / IC / DF / UD / UX_SPEC 等版本未變

**user 後續手動動作：**
- 清理 Template repo（D:\劇本開發工具）內 M1-CRITICAL-01 user-test 跑出來的污染（git checkout + clean）— 詳 DECISIONS_LOG §6.11.3 cookbook
- commit + push 本輪 Critical patch round 一包

**禁止：**
- A.5b 屬已完成歷史 task — 不再開新 CODEX 對話
- 不得 retract D-049 拍板（除非用 supersedes D-049 編號重拍）

---

## A.6 實作 `/create-world` skill（含中文別名）

**依賴：** A.3
**產出：**
- `.claude/skills/create-world/SKILL.md`
- `.claude/skills/建立世界觀/SKILL.md`

**做法：**
- 沿用 00_e 協議跑 5 階段
- 階段 4 執行自動拆分
- 階段 5 自動呼叫 `/status`

**驗收：**
- 在 Instance repo 中跑 `/create-world`，貼一段假世界觀
- 5 階段都能跑完
- 拆分結果寫入 01_a / 01_b / 01_c / 02_a/b/c / 作品專屬 00_b
- 階段 5 列出 W-rules、W-language、V 完成度

**禁止：**
- 不得跳過診斷階段直接寫檔（除非使用者明說）
- 不得擅自補完使用者未提供的設定

## A.7 實作 `/status` skill（含中文別名）

**依賴：** A.0、A.4、A.5（依賴 parser、frontmatter 已補、`.protocol_version` schema 已鎖）

**產出：**
- `.claude/skills/status/SKILL.md`
- `.claude/skills/進度/SKILL.md`

**做法（M4 鎖定）：**

1. 讀 `_design/expected_entities.yaml`（manifest 規則，A.0 已建）
2. 讀 Instance 根目錄 `.protocol_version` 的 `phase_log` 段落
3. 比對兩者推導**具體 expected set**：
   - 依 phase_log 已跑過的 phase + 每個 entry 的 `created_entities`（單數逐筆）與 `scene_id`（單數逐筆，scene-task / dialogue-write / qa 各 phase 都用單數 scene_id），aggregate 成「實際應存在的實體 set」。bootstrap entry 的 `scene_ids: []` 是特例（複數空陣列，未來不再使用，僅保留向下相容）
4. 掃描全 repo 所有 .md 的 frontmatter（用 A.0 parser）
5. 依 SPEC 第 5.3 節完成度公式聚合到實體
6. 對每個 expected entity：
   - 有貢獻檔 → 跑完成度公式
   - 無貢獻檔 → 計為 0%，標「缺漏，建議跑 `<對應 skill>`」
7. 不在 expected set 的實體（使用者手動建）→ 也計算，但標「未追蹤」
8. 輸出 ARCHITECTURE 第 2.3 節範例格式

**驗收：**
- 在剛 init 完的空 Instance 跑 `/status`，列出 0 個實體（phase_log 只有 bootstrap）
- 跑完 `/create-world` 後再跑 `/status`，看到 W-rules / W-language / V 三個實體；其他類別還沒跑過所以不出現
- 跑完 `/create-character C-主角A` 後再跑 `/status`，看到 C-主角A 出現
- 若刪除某 expected entity 的檔案，`/status` 標「缺漏」
- 若手動建立未在 phase_log 的實體檔案，`/status` 標「未追蹤」
- **呈現規則（時期 C）：**
  - 遵循 §1.5「不暴露 enum 鍵」：`pipeline_state` 等內部值不直接顯示給使用者，改為人類可讀詞
  - 遵循 §1.6.1「G1：badge 不單獨呈現」：實體狀態不只一個 badge，必須附完成度數字或檔案清單
  - 遵循 §1.6.1「G2：流程視覺化僅為閱讀順序」：若 status 列出「下游 pipeline 階段」，須加注「閱讀順序用，不代表強制執行步驟」
- 具體格式範本待 UX_SPEC §4 第二輪交付後補上（A.7 第二輪 refine task）

**禁止：**
- 不得修改任何檔案（純讀取）
- 不得擅自更新 `.protocol_version`（只有對應 skill 在自己階段 5 寫入）

## A.8 實作 `/check-gaps` skill（含中文別名）

**依賴：** A.7（兩者實作邏輯類似）
**產出：**
- `.claude/skills/check-gaps/SKILL.md`
- `.claude/skills/缺漏檢查/SKILL.md`

**做法：**
- 掃描 frontmatter 中標有 `TODO`、`INFERENCE`、`CONFLICT` 的段落
- 掃描 entities 為空但檔案有內容的情形
- 掃描期望存在但實際不存在的檔案（依模板對照表）
- **偵測 view/ 失效**（時期 C 整合 DECISIONS_LOG P-003 暫定）：對 `view/<entity>.md` 比對其 `組合來源` 列出的 source 檔的 mtime；若任一 source 的 mtime 晚於 view 檔的 mtime → 標「view/ 整合檔需更新」並印 UX §7.7 的警告文案
- 輸出待補項清單

**驗收：**
- 跑 `/check-gaps` 列出所有 TODO 標記與缺漏實體
- 報告格式清晰
- **view/ 失效偵測測試：** 跑 `/export-world` 後修改某 source 檔的 mtime（如 `touch 01_world/01_a_世界觀總覽.md`），再跑 `/check-gaps`，應印出 UX §7.7 文案「## ⚠ view/ 整合檔需更新 / View Files Need Refresh」段落
- **呈現規則：** 遵循 §1.5「錯誤呈現四件套」與 §1.6 全文呈現約束

## A.9 Wrapper Smoke Test（C-10 裁決：選 A）

**依賴：** A.5、A.6、A.7、A.8（4 個 Phase A skill 全部實作完才能完整測試中文 wrapper）

**做法：**
- 在實機 Claude Code 環境中，以中文 slash command 觸發各個已實作的 skill：
  - `/初始化專案` → 應觸發 init-project 流程
  - `/建立世界觀` → 應觸發 create-world 流程
  - `/進度` → 應觸發 status 流程
  - `/缺漏檢查` → 應觸發 check-gaps 流程
- 比對：每個中文觸發是否真的執行了英文主 skill 的流程（而非只回覆 description 內容）
- 若 fail，紀錄哪個 host / skill 出問題、改用 fallback（複製主檔內容）並重測

**驗收：**
- 4 個中文 skill 都觸發成功
- `_design/wrapper_smoke_test_report.md` 寫出測試結果
- 任何 fallback 紀錄到該 Instance 的 `.protocol_version`

**禁止：**
- 不得跳過此測試
- 不得在 smoke test 失敗時擅自修改主 skill 邏輯（fallback 是改 wrapper，不是改主 skill）

## A.10 Phase A REVIEW Gate（人類審查與升級）

**依賴：** A.0–A.9 全完成

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. **DRAFT 待升 REVIEW 的檔案**（依 Phase B 啟動條件 W/V/C/R/P/CH 需至少 REVIEW）：
   - 列出所有 `entities: [W-rules]` 的檔案及其當前 status
   - 列出所有 `entities: [W-language]` 的檔案
   - 列出所有 `entities: [V]` 的檔案
   - 對每份 DRAFT 檔案，提示「人類審完後請手動把 frontmatter 狀態改為 REVIEW，或保留 DRAFT 等下輪」
2. **未升級警告**：若使用者跳過此 gate 直接想進 Phase B，CODEX 應拒絕並重新印出待審清單
3. **升級紀錄**：人類完成升級後，CODEX 把升級摘要寫入 `_design/phase_a_review_log.md`（哪些檔案、誰升的、何時）

**驗收：**
- 人類完成所有 Phase B 啟動所需檔案的升級
- `phase_a_review_log.md` 存在且內容對齊實際升級行為

**禁止（v1.9 D-052 partial supersede — 「不得自行」精細化）：**
- CODEX 不得**未經 user 明示拍板**自行升級任何檔案狀態（保留 human-in-the-loop accountability 核心紀律）
- **但 user 明示拍板「同意升 + 拍板理由」後**，CODEX 可代為執行 mechanical edits（W/V 模板檔 frontmatter status / 最後更新日期 + phase_a_review_log §1 entry 寫入）— 屬「user-directed execution」非「self-initiated upgrade」；詳 DECISIONS_LOG v1.9 §6.15.2 D-052 + §6.16.2 D-053
- 不得跳過此 gate（直接進 Phase B）

## A.11 Phase A 整體驗收

**依賴：** A.0–A.10 全完成
**做法：**
- 跑 `python scripts/check_paths.py`，0 error
- 跑 `python scripts/check_headers.py`，0 error
- 端到端測試：
  1. clone Template repo 到一個測試目錄
  2. **刪 `.template_root` marker**（D-049 落地步驟）
  3. 跑 `/init-project`，輸入假專案資料，完成 bootstrap
  4. 確認產生 `.protocol_version`
  5. 跑 `/create-world`，貼一段測試世界觀，完成 5 階段
  6. 確認 01_a / 01_b / 01_c / 02_* / 作品 00_b 都有內容
  7. 跑 `/status`，確認實體完成度更新
  8. 跑 `/check-gaps`，確認 TODO 清單合理
- 撰寫 Phase A 驗收報告，包含上述測試的截圖或文字紀錄

### Wave 4 review consolidation（v1.7 新增備註；user 拍板延後處理）

A.11 整體驗收的 CODEX 對話**必須額外驗** Wave 4 三產出對齊各自 starter 規範（master 第六輪 Wave 4 review 延後到本任務一併處理；對齊 user 拍板）：

| Wave 4 產出 | 驗證項 |
|---|---|
| A.7 `/status` skill | 對齊 `_design/CODEX_A7_STARTER.md` line 19 之 prompt 規範：5 階段流程 / `build_repo_index` `parse_file` API 用法 / expected set 推導 / 完成度公式對齊 ARCH §2.3 / 缺漏 entity 對應 skill 表 / 時期 C 三條呈現規則 / 4 類錯誤處理 |
| A.8 `/check-gaps` skill | 對齊 `_design/CODEX_A8_STARTER.md` line 19 之 prompt 規範：5 階段流程 / TODO·INFERENCE·CONFLICT 掃描 / 空 entities 偵測 / expected-but-missing / view/ mtime 失效偵測對齊 P-003 + UX §7.7 文案 / 4 段輸出 |
| A.12 multi-agent invocation 檔三份 | 對齊 `_design/CODEX_A12_STARTER.md` line 19 之 prompt 規範：AGENTS.md 既有規範段未改 + skill 清單擴充對齊 ARCH §3.3.0 / CLAUDE.md 新建含 4 主 skill + 4 中文 wrapper / skill_invocation_guide.md 4 段 copy-paste prompt / 嚴禁 `.claude/skills/<name>/INVOKE.md`（D-048 否決候選 a） |

中文 wrapper（`/進度` / `/缺漏檢查` / `/初始化專案` / `/建立世界觀`）作為極簡 wrapper，驗證項只有：frontmatter 對齊 + 指向英文主檔為權威 + 不展開第二套流程。

**A.11 對 Wave 4 三產出的判定：**
- 三產出**全部對齊**對應 starter 規範 → A.11 Wave 4 review consolidation PASS（與整體驗收同時 PASS）
- 任一產出**偏離** starter 規範 → A.11 整體驗收 NO-GO；發 patch round 修補偏離項 → 重驗

**Phase A 通過 → 開放 Phase B。**

## A.12 NEW_REQ_7 落地 — root AGENTS.md + CLAUDE.md + skill_invocation_guide.md（v1.5 新增 via D-048）

**依賴：** A.5（init-project skill 已完成）+ A.6（create-world skill 已完成）。A.7 / A.8 完成度可平行 — A.12 內容含本輪 5 skill（init-project / create-world / status / check-gaps + 4 中文 wrapper），但首輪 commit 可只列已完成 skill 並標 TBD「待 A.7 / A.8 完成後同步補入」；若 Wave 4 三條 CODEX 等 A.7 / A.8 完成後再合併也可。

**產出：**
- `AGENTS.md`（repo root）：OpenAI Codex CLI / Codex App 慣例自動 discovery 檔
- `CLAUDE.md`（repo root）：Anthropic Claude Code CLI 慣例自動 discovery 檔
- `_user_manual/skill_invocation_guide.md`（manual scope）：Cowork / Codex App user 的 copy-paste fallback 範本

**內容規格（依 ARCH v1.4 §3.3.0）：**

每份檔的最低內容要求：

| 區塊 | AGENTS.md | CLAUDE.md | skill_invocation_guide.md |
|---|---|---|---|
| 工具總述 | ✓（≈ 共享）| ✓（≈ 共享）| ✓（簡述）|
| 26 skill 清單 + path | ✓ | ✓ | ✓（含 copy-paste prompt）|
| 工作流程說明 | ✓（≈ 共享）| ✓（≈ 共享）| 不必 |
| invocation 範本 | ✓（Codex-specific）| ✓（Claude Code-specific：強調 slash command）| ✓（4 環境通用 copy-paste）|
| skill 互依 / Phase 階段對齊 | ✓ | ✓ | 不必（屬 manual 其他章）|

**做法：**

1. **AGENTS.md / CLAUDE.md 內容對齊：** 兩份檔 skill 清單 + 工作流程段 90% 共享；差異只在前置 ecosystem 慣例段與 invocation 範本子段
2. **skill 清單來源：** 掃 `.claude/skills/*/SKILL.md` 取 frontmatter `name + description`；本輪首先列：
   - `init-project` + 中文 wrapper `初始化專案`
   - `create-world` + 中文 wrapper `建立世界觀`
   - `status` + 中文 wrapper `進度`（Wave 4 完成後補入；或標 TBD）
   - `check-gaps` + 中文 wrapper `缺漏檢查`（Wave 4 完成後補入；或標 TBD）
   - 其他 22 個 skill（Phase B+ 未實作）標 TBD
3. **skill_invocation_guide.md 結構：** `_user_manual/` 第 4 章 management_skills.md 擴充段，或獨立 04b skill_invocation_guide.md（依 NEW_REQ_2 manual 既有結構決定）
4. **Cowork 對齊：** skill_invocation_guide.md 每 skill 段含「給 Cowork agent 的標準 prompt 模板」— user copy-paste 後 agent 能正確識別並執行 SKILL.md 流程

**驗收：**

- AGENTS.md / CLAUDE.md skill 清單一致（grep 對齊）
- skill_invocation_guide.md 每 skill 1 段 copy-paste prompt
- 跑 Cowork 跑 `/init-project`：user 從 skill_invocation_guide.md copy paste prompt 後，agent 能對齊 SKILL.md 5 階段執行
- 跑 OpenAI Codex CLI（如可用）：agent 啟動自動讀 AGENTS.md + 能列舉 skill 清單
- 跑 Claude Code CLI：agent 啟動自動讀 CLAUDE.md + 能列舉 skill 清單

**禁止：**

- **不**新增 `.claude/skills/<name>/INVOKE.md`（D-048 否決候選 a）
- **不**改動現有 26 SKILL.md 內容（A.12 只新增 root + manual 檔，不動 skill 內容）
- **不**寫 CI / pre-commit hook 強制兩份 root 檔對齊（本輪 manual 維護；hook 屬未來 NEW_REQ_8+）

---

# 2a. Phase A.0F — 前端工具任務群（v1.1 新增 via D-029/030 + Contract B + ARCH §13）

> **v1.1 新增 task 群** — 對應 REQUIREMENTS_LOCK §5「前端工具層拍板」（F1/F2/F3/F6/F7 5 必要功能 + Export panel + Asset panel）、Contract B 全部 8 條、ARCH §13 frontend adapter 8 個 API endpoint。

**整體目標：** Local web server 啟動後，user 開瀏覽器 `localhost` 看 F1 全局看板 / F2 場景切換 / F3 多版本並排 / F6 搜尋篩選 / F7 直接編輯（LOCKED 守門 + Save race guard）；Export panel 產 prompt；Asset Panel 顯示 A-* 進度。

**整體依賴：** Phase A.0（A.0.1 ~ A.0.9 parser ready）+ Phase B（C-* / R-* / P / CH-* / S-* 實體有資料才能顯示）

**整體禁止（D-029 α + D-038 + D-031）：**
- **不**啟動 subprocess / spawn child process
- **不**執行 agent / local CLI
- **不**新增 skill（包括 `/export-dialogue` 不存在的 skill）
- **不**擅自加 frontmatter 欄位（LOCKED 降級走 09_e，D-046 #5）

## A.0F.0 前端 build / package / 啟動規格（依 UX §11.8）

**產出：**
- `_tools/frontend/serve.py`（Python `http.server` 或 FastAPI；建議 FastAPI for API routing）
- `_tools/frontend/static/`（HTML / CSS / JS）
- `requirements.txt`（如用 FastAPI 列依賴）

**驗收：** `python _tools/frontend/serve.py` 啟動，瀏覽器 `http://localhost:8765` 開到 Workspace Home。

## A.0F.1 frontend adapter 8 個 API endpoint（依 ARCH §13.2 + Contract C）

**產出：** server.py 提供以下 8 endpoint：

| # | Endpoint | 對應 Contract |
|---|---|---|
| 1 | `GET /api/scene/<id>/header` | B.2 |
| 2 | `POST /api/scene/<id>/save` | B.2 |
| 3 | `POST /api/scene/<id>/save-as` | B.2 LOCKED race modal B 選項 |
| 4 | `GET /api/scenes/<id>/versions` | NS-15 / UX §11.3.3 |
| 5 | `GET /api/scenes/<id>/keys/<key>/lines` | NS-30 / UX §11.3.5 |
| 6 | `GET /api/assets?scope=...` | B.4 / NS-2 |
| 7 | `GET /api/assets/<id>/usage` | B.4 / UPS-UX-80 |
| 8 | `GET /api/scope-counts?scope=...` | §C.5a Export prompt |

**驗收：** 8 endpoint 全 work；integration test 通過。

## A.0F.2 F1 Project Dashboard / 全局看板（依 UX §11.1）

**產出：** Dashboard 頁面含 HERO / 場景就緒度 / 模組狀態 / 三欄區 / Asset Panel / 模組導航 / 互動 / RWD。

**驗收：** 整體完成度顯示正確；場景就緒度進度條；場景索引可點跳轉。

## A.0F.3 F2 Scene Queue + Scene Detail (cockpit, read-only)（依 UX §11.2）

**產出：** Scene Queue 列表 + Scene Detail cockpit（read-only；編輯入口跳 §11.5）

**驗收：** 場景列表 + 切換 + cockpit Required Context 完整顯示。

## A.0F.4 F3 Scene Editor 三欄並排 — 新頁面（依 UX §11.3 + D-035）

**產出：** Scene Editor 三欄並排 layout + textarea + Save 全部 + details pane + lineage timeline + 版本對照

**驗收：** v01A / v01B / v01C 三欄並排可編輯；details pane 顯示 KEY metadata 不暴露 raw YAML。

## A.0F.5 F6 Scene Queue 搜尋 + 篩選 facet（依 UX §11.4）

**產出：** Scene Queue 上方搜尋框 + 8 維 facet（含 A-* asset 第 8 維 subtype/owner/state 三層）

**驗收：** 搜尋 fuzzy + facet filter 正確；A-* facet 含 7 subtype（D-044）。

## A.0F.6 F7 直接編輯 + LOCKED 守門 + Scene Detail → Editor 導航（依 UX §11.5 + Contract B.2）

**產出：**
- 進入 Editor 前 LOCKED 守門（§11.5.1-3）
- LOCKED Save race guard 5 步流程（§11.5.7-8；Contract B.2）
- LOCKED race modal 三選項（A / B / C）

**禁止（D-046 #5）：** LOCKED 降級引導**不擅自加 frontmatter 三欄位**；降級紀錄全部進 09_e final-gating 紀錄。

**驗收：** LOCKED 場景 Quick Actions 顯示複製降級指令按鈕；Save race guard Step 3 重讀 header 攔截 LOCKED 升級；B 選項另存 DRAFT proposal 成功。

## A.0F.7 Asset Panel — A-* 7 subtype 獨立顯示（依 UX §11.1.6a + Contract B.4 + C.5）

**產出：** Project Dashboard 內 A-* Asset Panel 7 subtype 分組 + 子表 KEY 詳細 + 缺檔警示

**驗收：** A-* 完成度與 narrative 完成度完全分離；7 subtype 各自百分比正確；A-portrait-* 缺檔 → 紅 ⚠ badge。

## A.0F.8 Export Prompt panel（依 UX §11.6.11 + Contract B.3 + §C.5a）

**產出：** Export panel 4 入口 + 完整 UI（範圍 / 格式 / 路徑 / 推送方式）+ 預覽 Prompt modal + 複製/推送行為

**驗收（v1.2 對齊 PS-05 + L3 lifecycle）：**
- 4 入口（§11.1.5 / §11.1.7 / §11.2.2 / §11.4.7）可開啟 Export panel
- prompt 對齊 L3_EXPORT_PROMPT_SCHEMA §1.1 5 區塊（含 v0.2 新增 `include_deleted` flag；CC-07 對齊）
- **clipboard push mode 正確**（Phase A.0 必做；本驗收涵蓋）
- **`local_llm_endpoint` POST：** Phase A.0 panel UI 內列為選項但**不**作驗收項；正式驗收在 Phase B+（屬 L3_EXPORT_PROMPT_SCHEMA §4 lifecycle Phase B 後必做範疇；Phase A.0 階段 UI disabled tooltip「Phase B+ 啟用」即可）

## A.0F.9 Conflict modal — entity 命名衝突 4 選項（依 UX §11.7.6a + Contract B.8；v1.3 校正 — 原 §11.7.6 typo）

**產出：** Conflict modal 顯示既有 vs 手稿 diff + 4 選項按鈕（merge / overwrite / create-as-new / skip）

**禁止：** Modal 內按鈕**只複製對應指令**，**不**直接執行 merge 等動作（D-029 α）。

**驗收：** Modal 開啟 + 4 選項按鈕複製不同指令文字。

## A.0F.10 多場景並行 + 編輯衝突偵測（依 UX §11.7）

**v1.2 變動（CC-09 解決）：** 本 task 只負責「**mtime drift conflict**」對應 UX §11.7.6 + Contract B.2（**二選項：reload / 強制覆寫**）。entity 命名衝突 4 選項處理對應 §A.0F.9 + UX §11.7.6a + Contract B.8。兩種 conflict modal **分拆實作**。

**產出：** mtime checksum 偵測 + 409 conflict modal（mtime drift only）+ multi-tab edit-lock（advisory）

**驗收（v1.2 對齊 UX §11.7.6 + CC-09）：**
- 多分頁同編偵測
- mtime drift conflict 跳 modal 提供 **reload / 強制覆寫 / 取消** 三選項（對齊 UX §11.7.6 拍板）
- entity 命名衝突 4 選項處理屬 §A.0F.9 範圍，**不**在本 task

## A.0F.11 Phase A.0F 整體驗收

**驗收：**
- A.0F.0 ~ A.0F.10 各自驗收項全 pass
- 跑通典型 user session（REQUIREMENTS_LOCK §2 7 步流程）：terminal 啟動 → 瀏覽器看 F1 → F2 切場景 → F3 並排 → F7 編輯 → Save → 外部 agent 改檔 → 前端 refresh 看到結果 → Export panel 複製 prompt → git commit

---

# 3. Phase B — 其餘上游創建協議

**目標：** 使用者能建完所有上游設定（角色／主線／細綱）。

**Phase B 完整驗收：**
1. 四個 `/create-*` skill 都能跑完整 5 階段（character / relationship / outline / detailed-outline）
2. 自動拆分到對應 entity 檔
3. `/status` 能看到 C-* / R-* / P / CH-* / S-* 實體完成度
4. `check_paths.py` 與 `check_headers.py` 都 0 error

> **v1.8 Wave 6 完成紀錄（master 第六輪延伸；2026-05-20）：**
> 
> B.0 ~ B.4 全部 ✓ DONE：
> - B.0 / B.1 / B.2 / B.3：4 個 protocol（00_l / 00_f / 00_g / 00_h）已存在於 May 18 第五輪期間；本輪 Wave 6 跑 D-047 對齊 patch round（v0.1 → v0.2；§2 啟動條件加 issue_type_registry 條目 + §4.0 動態構建段 + §4.1 議題預設表 + 議題數對齊 6/8/6/6）— PASS via CODEX_WAVE6_PROTOCOLS_PATCH_STARTER
> - B.4 03_characters/ 子目錄：master verify 既有 main/minor/npc 三子目錄（May 16）— ✓ DONE
> 
> 下列 B.0 ~ B.4 原 spec 保留供歷史紀錄參考；現實 scope 以 v1.8 上述完成紀錄為準。

## B.0 寫 `00_protocol/00_l_關係創建協議.md`（C-7 新增）

**依賴：** Phase A 通過
**產出：** `00_protocol/00_l_關係創建協議.md`
**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §1.5（含 6 議題完整 agent 提問腳本、寫檔規則、拆分 algorithm）+ §1.0.1–§1.0.3

**做法：**
- 依 UPSTREAM §1.5 完整內容寫協議檔
- 沿用共通骨架 10 區段；專屬區段對應 SPEC §10.5 列出的 7 項議題
- 啟動條件：涉及的兩個 C-* 都至少 REVIEW

**驗收：**
- 專屬區段含 UPSTREAM §1.5.2 的具體提問腳本（每項 5 欄）
- 啟動條件明確（兩角色 REVIEW 才能跑）
- 拆分規則明確（寫到 04_a 對應段落 + 04_b 時間線）
- **00_l 協議檔本身 frontmatter**：協議檔不貢獻實體，YAML block 可省略（M5 釐清）
- **產物檔案 frontmatter 規則**：04_a 中該對關係段落、04_b 中時間線錨點，frontmatter 標 `entities: [R-<a>-<b>]`、`depends_on: [C-<a>, C-<b>, W-rules]`

## B.1 寫 `00_protocol/00_f_角色創建協議.md`

**依賴：** Phase A 通過
**產出：** `00_protocol/00_f_角色創建協議.md`
**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §1.2（含 9 議題完整 agent 提問腳本、N 角色 × 9 議題深度/廣度優先模式）+ §1.0.1–§1.0.3

**做法：**
- 依 UPSTREAM §1.2 完整內容寫協議檔
- 啟動條件：W-rules、V、W-language 至少 REVIEW
- 區段 4 探索順序依 UPSTREAM §1.2.1 表（深度優先預設，使用者可選廣度優先）

**驗收：**
- 9 項專屬區段含 UPSTREAM §1.2.2 具體提問腳本
- 啟動條件明確
- 拆分規則明確（主角／副主／NPC 子目錄）

## B.2 寫 `00_protocol/00_g_大綱創建協議.md`

**依賴：** Phase A 通過
**產出：** `00_protocol/00_g_大綱創建協議.md`
**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §1.3（含 7 議題完整 agent 提問腳本、寫回 00_b §3/§4）+ §1.0.1–§1.0.3

**驗收：**
- 7 項專屬區段含 UPSTREAM §1.3.2 具體提問腳本
- 規模定位、類型偏移風險清單會寫回作品專屬 00_b §3/§4

## B.3 寫 `00_protocol/00_h_細綱創建協議.md`

**依賴：** Phase A 通過
**產出：** `00_protocol/00_h_細綱創建協議.md`
**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §1.4（含 7 議題完整 agent 提問腳本、寫回 00_b §6）+ §1.0.1–§1.0.3

**驗收：**
- 7 項專屬區段含 UPSTREAM §1.4.2 具體提問腳本
- 高風險場景處理規則會寫回作品專屬 00_b §6

## B.4 確認 `03_characters/` 子目錄結構存在

**依賴：** 無
**產出：** 確認 `03_characters/main/`、`minor/`、`npc/` 三個子目錄存在（在 Template repo 為空目錄，可放 `.gitkeep`）

**驗收：**
- 三個子目錄存在於 Template repo
- 各有 `.gitkeep` 或 README 描述用途

## B.5 實作 `/create-character` skill（含中文別名）

**依賴：** B.1、B.4（拆分需要 main/minor/npc 子目錄存在）
**產出：**
- `.claude/skills/create-character/SKILL.md`
- `.claude/skills/建立角色/SKILL.md`

**做法：**
- 沿用 00_f 協議
- 啟動條件檢查：W-rules / V / W-language 是否至少 REVIEW，否則拒絕並提示
- 階段 4 自動拆分到 main/ 或 minor/ 或 npc/
- 階段 5 自動 `/status`

**驗收：**
- 在 W-rules 還是 DRAFT 時跑 `/create-character`，被拒絕
- 在 W-rules REVIEW 後跑 `/create-character`，能跑完 5 階段
- 拆分到正確子目錄
- 偏移風險寫入作品專屬 00_b

## B.5.5 角色 REVIEW Gate（M3：在 B.5b 之前）

**依賴：** B.5（至少有 2 個 C-* DRAFT）

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. 所有 `entities: [C-*]` 的檔案，當前 status
2. 提示「`/create-relationship` 需要兩個 C-* REVIEW；請手動把要建立關係的兩角色 frontmatter 狀態升 REVIEW」
3. 升級紀錄寫入 `_design/phase_b_character_review_log.md`（標準文件頭）

**驗收：**
- 至少 2 個 C-* 已升 REVIEW（為 B.5b 啟動條件鋪路）
- 升級紀錄存在

**禁止（v1.9 D-052 partial supersede — 「不得自行」精細化）：**
- CODEX 不得**未經 user 明示拍板**自行升級任何 C-* 狀態（保留 human-in-the-loop accountability 核心紀律）
- **但 user 明示拍板「同意升 + 拍板理由」後**，CODEX 可代為執行 mechanical edits（frontmatter status / 最後更新日期 + review_log §1 entry 寫入）— 屬「user-directed execution」非「self-initiated upgrade」；詳 DECISIONS_LOG v1.9 §6.15.2 D-052 + §6.16.2 D-053
- 不得直接跳到 B.5b（要先過此 gate）— 此條 D-052 不動

## B.5b 實作 `/create-relationship` skill（含中文別名，C-7 新增）

**依賴：** B.0、B.5、B.5.5（角色 REVIEW gate 必須先過）

**產出：**
- `.claude/skills/create-relationship/SKILL.md`
- `.claude/skills/建立關係/SKILL.md`（中文別名 wrapper）

**做法：**
- 沿用 00_l 關係創建協議
- 啟動條件檢查：兩個 C-* 都至少 REVIEW，否則拒絕並提示
- 階段 4 自動拆分到 04_a 對應段落 + 04_b 時間線
- 階段 5 自動 `/status`
- frontmatter 標 `entities: [R-<a>-<b>]`、`depends_on: [C-<a>, C-<b>, W-rules]`

**驗收：**
- 跑 `/create-relationship 主角A 反派B` 能跑完 5 階段
- 04_a 中對應段落已建立
- 04_b 時間線錨點已建立
- R-主角A-反派B 出現在 `/status` 實體清單
- 兩角色其一還是 DRAFT 時，skill 拒絕並提示

**禁止：**
- 不得擅自決定關係本質（真實關係 vs 表面關係 需使用者拍板）
- 不得跳過任一角色的 REVIEW 檢查

## B.6 實作 `/create-outline` skill（含中文別名）

**依賴：** B.2
**產出：**
- `.claude/skills/create-outline/SKILL.md`
- `.claude/skills/建立大綱/SKILL.md`

**做法：**
- 沿用 00_g 協議
- 啟動條件檢查（主角 C-* 至少 DRAFT）
- 階段 4 寫 05_a、規模定位寫回作品 00_b
- 階段 5 自動 `/status`

**驗收：**
- 缺主角時拒絕
- 跑完後 P 實體完成度上升
- 規模定位寫入作品 00_b

## B.6.5 主線 REVIEW Gate（M3：在 B.7 之前）

**依賴：** B.6（P 已 DRAFT）

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. `entities: [P]` 的檔案（`05_a_主線大綱.md`）當前 status
2. 提示「`/create-detailed-outline` 需要 P 至少 REVIEW；請人類審完後手動把 frontmatter 狀態升 REVIEW」
3. 升級紀錄寫入 `_design/phase_b_outline_review_log.md`（標準文件頭）

**驗收：**
- P 已升 REVIEW（為 B.7 啟動條件鋪路）
- 升級紀錄存在

**禁止（v1.9 D-052 partial supersede — 「不得自行」精細化）：**
- CODEX 不得**未經 user 明示拍板**自行升級 P 的狀態（保留 human-in-the-loop accountability 核心紀律）
- **但 user 明示拍板「同意升 + 拍板理由」後**，CODEX 可代為執行 mechanical edits（frontmatter status / 最後更新日期 + review_log §1 entry 寫入）— 屬「user-directed execution」非「self-initiated upgrade」；詳 DECISIONS_LOG v1.9 §6.15.2 D-052 + §6.16.2 D-053
- 不得直接跳到 B.7 — 此條 D-052 不動

## B.7 實作 `/create-detailed-outline` skill（含中文別名）

**依賴：** B.3、B.6、B.6.5（主線 REVIEW gate 必須先過）
**產出：**
- `.claude/skills/create-detailed-outline/SKILL.md`
- `.claude/skills/建立細綱/SKILL.md`

**做法：**
- 沿用 00_h 協議
- 啟動條件檢查（P 至少 REVIEW）
- 階段 4 拆分（**v1.9 D-050 對齊 partial supersede**：依 D-050 子裁決 2 CH 行限定 `05_b + 06_a only`；`05_c/d/e` 屬 P /create-outline scope 不寫；詳 DECISIONS_LOG v1.9 §6.12.2 D-050 + §6.16.2 D-053）
- 階段 5 自動 `/status`

**驗收：**
- P 還是 DRAFT 時拒絕
- 跑完後 CH-* 與 S-*-* 實體陸續出現

## B.8 Phase B REVIEW Gate（人類審查與升級）

**依賴：** B.0、B.1、B.2、B.3、B.4、B.5、B.5.5、B.5b、B.6、B.6.5、B.7 全完成（明列所有 sub-task）

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. **DRAFT 待升 REVIEW 的檔案**（涵蓋 Phase D 啟動條件所需的所有實體類型）：
   - 列出所有 `entities: [C-*]` 的檔案
   - 列出所有 `entities: [R-*-*]` 的檔案
   - 列出所有 `entities: [P]` 的檔案
   - 列出所有 `entities: [CH-*]` 的檔案
   - 列出所有 `entities: [S-*-*]` 的檔案（場景索引產物，D.7 整體驗收要求至少 REVIEW；補 #5）
2. **升 REVIEW 後可進 Phase C / Phase D 的指引**
3. **升級紀錄**：寫入 `_design/phase_b_review_log.md`

**驗收：**
- 人類完成所有需要升級的檔案
- `phase_b_review_log.md` 存在且對齊實際升級行為

**禁止（v1.9 D-052 partial supersede — 「不得自行」精細化）：**
- CODEX 不得**未經 user 明示拍板**自行升級任何檔案狀態（保留 human-in-the-loop accountability 核心紀律）
- **但 user 明示拍板「同意升 + 拍板理由」後**，CODEX 可代為執行 mechanical edits（5 類實體 frontmatter status / 最後更新日期 + phase_b_review_log §1 entry 寫入；5 個 §1.2.X 子段都涵蓋）— 屬「user-directed execution」非「self-initiated upgrade」；詳 DECISIONS_LOG v1.9 §6.15.2 D-052 + §6.16.2 D-053

## B.9 Phase B 整體驗收

**依賴：** B.0、B.1–B.8 全完成
**做法：**
- 端到端測試：
  1. 接續 Phase A 的測試 Instance
  2. 跑 `/create-character` 建立主角與反派
  3. 跑 `/create-relationship 主角A 反派B` 建立關係
  4. 跑 `/create-outline` 建立主線
  5. 跑 `/create-detailed-outline` 建立章節結構
  6. 跑 `/status`，確認 C-* / R-* / P / CH-* 都有完成度
- 撰寫 Phase B 驗收報告

**Phase B 通過 → 開放 Phase C。**

---

# 4. Phase C — 視圖 + 迭代

**目標：** 使用者能隨時看完整版設定、能在任何已建設定上做迭代。

**Phase C 完整驗收：**
1. `/view-*` 能即時組合分拆檔印在 chat
2. `/export-*` 能寫出 `view/<entity>.md` 整合檔
3. `/iterate-*` 能跑通用迭代協議，**強制跑影響範圍評估**
4. `/diagnose` 與 `/integrate` 可獨立呼叫對應模式

## C.1 寫 `00_protocol/00_j_迭代協議.md`

**依賴：** Phase B 通過（要對所有上游實體生效）
**產出：** `00_protocol/00_j_迭代協議.md`
**內容：**
- 沿用共通骨架（內容調整為迭代邏輯）
- 階段 1：變更點識別
- 階段 2：**強制**影響範圍評估（SPEC 第 11 節 + ARCHITECTURE 第 5 節）
- 階段 3：收斂
- 階段 4：執行（**不**重新生成 view；view/export 由 C.3/C.5 提供，使用者需要時手動跑 `/export-*`）
- 階段 5：實體驗證
- 專屬區段 10：各上游協議的迭代呼叫指南

**驗收：**
- 階段 2 強制執行影響範圍評估
- 各上游協議的迭代指南完整（W-rules、C、P、CH 各自的特別注意事項）

## C.2 實作 5 個 `/iterate-*` skill（含中文別名，M5 修正）

**依賴：** C.1

**產出：**
- `iterate-world` / `迭代世界觀`
- `iterate-character` / `迭代角色`
- `iterate-relationship` / `迭代關係`（M5 新增）
- `iterate-outline` / `迭代大綱`
- `iterate-detailed-outline` / `迭代細綱`

**做法：**
- 全部 5 個 skill 共用 00_j 協議的底層邏輯
- 每個 skill 在 SKILL.md 中說明對應的實體類型（W、C、R、P、CH）
- 影響範圍評估的反查邏輯依 ARCHITECTURE 第 5 節實作（雙路：entities + depends_on）

**驗收：**
- 跑 `/iterate-world` 修改 W-rules，能列出 V、W-language、相關 C-* 受影響（雙路反查正確）
- 跑 `/iterate-relationship` 修改某對關係，列出 04_a 對應段落 + 04_b 時間線
- 使用者拍板「只改 W-rules」時，skill 不會擅自連動修改其他檔案
- 跑完後 `.protocol_version.phase_log` 新增一筆 iterate 紀錄（含 modified_entity 與受影響檔清單）

**注意：** view/export 在 C.3/C.5 才實作。iterate 完成後**不**強制重新生成 view（移到 C.7 整體驗收測試）。若使用者要手動重生，需自行呼叫對應 `/export-*`。

## C.3 實作 4 個 `/view-*` skill（含中文別名）

**依賴：** Phase B 通過（要有實體才有東西可組合）
**產出：**
- `view-world` / `查看世界觀`
- `view-character` / `查看角色`
- `view-outline` / `查看大綱`
- `view-detailed-outline` / `查看細綱`

**做法：**
- 依 ARCHITECTURE 第 4.1 節邏輯實作
- 動態 read source 檔，組合後印在 chat
- 不寫實體檔

**驗收：**
- 跑 `/view-world` 看到完整世界觀（含 01_a/b/c 與 02_*）
- 跑 `/view-character 主角A` 看到該角色聲線卡 + 關係矩陣中該角色段落 + 弧線

## C.4 測試 `DERIVED` 狀態只允許在 `view/` 目錄（O3 鎖定）

**依賴：** A.0（parser 已支援 7 種狀態）

**做法：**
- A.0 parser 已內建 7 種狀態，C.4 不再「加入」狀態
- 本任務聚焦：在 `check_headers.py` 加入「目錄專用狀態」規則
- DERIVED 出現在 `view/` 目錄之外 → ERROR
- APPLIED 出現在 `archive/` 目錄之外 → ERROR
- 新增測試案例驗證此規則

**驗收：**
- 跑 `check_headers.py` 對 `view/foo.md`（狀態=DERIVED）不報錯
- 跑 `check_headers.py` 對 `01_world/foo.md`（狀態=DERIVED）報 ERROR
- 跑 `check_headers.py` 對 `archive/補丁.md`（狀態=APPLIED）不報錯
- 跑 `check_headers.py` 對 `00_protocol/foo.md`（狀態=APPLIED）報 ERROR

**為什麼先 C.4 後 C.5：** export 會產生 view/ 下的 DERIVED 檔，C.4 的目錄專用規則先確認，C.5 export 才能寫對位置。

## C.5 實作 4 個 `/export-*` skill（含中文別名）— v1.1 對齊 D-038 + D-046 #4

**v1.1 變動摘要：** C.5 既有 4 個 `/export-*` skill **維持不動**（寫 view/<topic>.md 給人讀）；**不擴 JSON 輸出**（D-038 + D-046 #4 + CODEX C-12 / O-02 解決）。Layer 3 Export JSON+MD 雙吐走獨立 A1 prompt 流程（見 §C.5a — 前端 only，無新 skill）。

**依賴：** C.3（與 view 共用組合邏輯）、C.4（parser 已支援 DERIVED）
**產出：**
- `export-world` / `匯出世界觀`
- `export-character` / `匯出角色`
- `export-outline` / `匯出大綱`
- `export-detailed-outline` / `匯出細綱`

**做法：**
- 與對應 `/view-*` 邏輯相同，但結果寫入 `view/<entity>.md`
- 新檔案 status 為 `DERIVED`
- header 含「組合來源」段落
- **呈現規則（時期 C 整合 UX_SPEC §7 / ARCHITECTURE §4.2 / §4.3）：**
  - frontmatter 之後、第一個 `#` 之前加 breadcrumb（例：`> 專案首頁 / 世界觀 / 完整視圖`）
  - 整合檔預估 > 200 行時插入「## 目錄 / Contents」TOC（位置：frontmatter + breadcrumb 之後、第一個 `#` 之前）
  - TOC slug 規則：依 GFM 自動，不手寫 `{#anchor}`
  - **skill 內驗證 slug 一致性**（DECISIONS_LOG P-005 暫定）：生成 TOC 後比對實際標題的 slug 與 TOC 連結是否一致，不一致即拒絕寫檔並印錯訊息
  - 整合檔末尾加 `[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)` 返回連結（`/view/README.md` 為使用者手動建立，本 skill 不自動產 — P-004）
  - 每段內容結尾 italic 一行 `*來源：[/path](/path)*`，多源逗號分隔
  - 跨檔 link 一律以 project root 為基準（`/` 開頭）

**驗收：**
- `view/` 目錄下產生對應整合檔
- 整合檔可正常被 `check_headers.py` 解析（DERIVED 已被 C.4 認可）
- **breadcrumb 在 frontmatter 之後、`#` 標題之前出現**
- **若預估 > 200 行，TOC 段落存在於正確位置**
- **TOC slug 與實際標題一致**（skill 內驗證通過才寫檔）
- **每段尾有 source italic 引用**
- **跨檔 link 均以 `/` 開頭**

## C.5a Layer 3 Export prompt 生成器（v1.1 新增 via D-024 + D-038 + D-039 — 前端 only）

**v1.1 變動摘要：** 對應 SPEC §13a + ARCH §4.2a + Contract A.7 + B.3 — Layer 3 Export 走 A1 prompt 流程，**前端內嵌 prompt 生成器**，**無新 skill**。本 task 屬「前端工具任務群」（非 Claude skill task），實作在 §A.0F 系列 task。

**依賴：** A.0.9（parser get_*_records API ready）+ §A.0F.x（frontend adapter ready）

**產出：**
- 前端 `ExportPromptPanel` 元件（依 UX §11.6.11）
- 前端 `promptAssembler.js` 對齊 `_design/L3_EXPORT_PROMPT_SCHEMA.md` §1 5 區塊
- 前端 `clipboardWriter` + `endpointPoster`
- server.py `GET /api/scope-counts?scope=...` endpoint

**禁止：**
- **不**新增 `/export-dialogue` / 其他不存在 skill（D-031 + D-046 #4）
- **不**啟動 subprocess / spawn child process（D-029 α）
- **不**前端執行 export（D-038 — export 在外部 agent process 中發生）

**驗收：**
- 點 Export panel「複製 Prompt」按鈕 → prompt 全文寫到 clipboard
- prompt 對齊 L3_EXPORT_PROMPT_SCHEMA §1.1 5 區塊（標題 + YAML 元資料 + 步驟 + 約束 + 完成回報）
- push mode `local_llm_endpoint` 可正確 POST 到 user 設定的 URL
- Export panel 4 個入口（§11.1.5 / §11.1.7 / §11.2.2 / §11.4.7）可開啟

## C.6 實作 `/diagnose` 與 `/integrate` skill

**依賴：** Phase A 完成（兩者是通用模式入口）
**產出：**
- `.claude/skills/diagnose/SKILL.md` + `.claude/skills/診斷/SKILL.md`
- `.claude/skills/integrate/SKILL.md` + `.claude/skills/整理/SKILL.md`

**做法：**
- `/diagnose` 對應 00_a 中的「診斷模式」
- `/integrate` 對應 00_a 中的「整理模式」
- 兩者不綁定特定協議，可獨立呼叫

**驗收：**
- 跑 `/diagnose` 並貼任意素材，能輸出診斷報告格式
- 跑 `/integrate` 並提供素材，能輸出可寫檔的結構化結論

## C.7 Phase C 整體驗收

**依賴：** C.1–C.6 全完成
**做法：**
- 端到端測試：
  1. 接續 Phase B 的測試 Instance
  2. 跑 `/view-world`，確認看到完整組合
  3. 跑 `/export-world`，確認 `view/世界觀.md` 產生
  4. 跑 `/iterate-world`，修改世界觀
  5. 確認影響範圍評估列出受影響實體
  6. 拍板後使用者自行決定是否重新生成 view（手動跑 `/export-*`，非自動）
  7. 跑 `/diagnose` 對某段內容做診斷
- 撰寫 Phase C 驗收報告

**Phase C 通過 → 開放 Phase D。**

---

# 5. Phase D — 台詞生產 + QA + 對外

**目標：** 完整系統可用、可分享。

**Phase D 完整驗收：**
1. 跑 `/scene-task` 能產出可送 `/dialogue-write` 的單場任務包
2. 跑 `/dialogue-write` 能依任務包產 3+ 版本台詞
3. 跑 `/qa` 能依 09 全套模板出報告
4. README.md 完整、可作為新使用者進入點
5. 蟲潮孤堡 Instance repo 建立完成

## D.0 寫 `00_protocol/00_k_台詞生產流程協議.md`

**依賴：** Phase A 通過（依 00_a、00_b、00_c）；Phase B 通過（依 00_e–00_h 完成上游）；A.4 完成（既有檔案 frontmatter 補完，能跑 /status）

**產出：** `00_protocol/00_k_台詞生產流程協議.md`

**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §2.1–§2.10（00_k 10 區段完整展開）+ §6（多場景並行處理）

**做法：**
- 依 UPSTREAM §2 完整內容寫協議檔
- 沿用 SPEC §12 框架；具體內容（場景狀態機觸發條件、與 00_a 模式對應、任務包必填、多版本方向、QA 閱讀順序、跨 skill 呼叫、多場景並行）依 UPSTREAM §2.10 各小節
- P-015 暫定（原 D-017）多場景並行 mutex 機制依 UPSTREAM §6（ARCHITECTURE §6.7.5 摘要）

**驗收：**
- 10 區段完整對應 UPSTREAM §2.1–§2.10
- 場景狀態機定義清楚（依 UPSTREAM §2.10.1）
- 與 00_a 模式對應表完整（依 UPSTREAM §2.10.2）
- 任務包必填欄位完整（依 UPSTREAM §2.10.3）
- **8 份** QA 閱讀順序明示（v1.1 / D-043；依 UPSTREAM §2.5.3 v0.3 序列順序；原 5 份 supersede）
- 跨 skill 呼叫關係清楚（依 UPSTREAM §2.10.6）
- 多場景並行段落（依 UPSTREAM §2.10.7 + §6）
- 跑 `check_paths.py` 與 `check_headers.py` 都 0 error

**禁止：**
- 不得重複 00_a 的「規則層」內容（00_k 是流程層）
- 不得擅自新增 00_a 沒有的模式
- 不得擅自把 DRAFT 升 REVIEW

## D.1 寫 `09_quality_assurance/09_f_類型偏移檢查模板.md`

**依賴：** Phase A 通過（依 00_b 通用骨架）
**產出：** `09_quality_assurance/09_f_類型偏移檢查模板.md`
**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §3.5（含 5 層檢查框架、檢查 algorithm、frontmatter M7/M10 對齊、與蟲潮孤堡專案版的通用化規則）

**做法：**
- 依 UPSTREAM §3.5.1 模板結構（5 層檢查框架）寫通用版
- 依 §3.5.2 檢查 algorithm 設計檢查項分類
- 依 §3.5.3 frontmatter 對齊 M7/M10
- 依 §3.5.4 通用化原則：移除任何蟲潮孤堡專屬內容

**驗收：**
- 結構完整（5 層檢查框架）
- 不含任何作品專屬內容
- frontmatter `qa_type: GENRE_DRIFT`

## D.1a 寫 09_g / 09_h / 09_i 三份 QA 模板（v1.1 新增 via D-026 + D-043）

**v1.1 新增 task — 對應 D-026（partial supersede D-018 #3）+ D-043（8 份必跑）**

**依賴：** D.0、D.1（同模式）

**產出：**
- `09_quality_assurance/09_g_節奏感檢查模板.md` — qa_type: RHYTHM
- `09_quality_assurance/09_h_對話張力檢查模板.md` — qa_type: DRAMATIC_TENSION
- `09_quality_assurance/09_i_跨場一致性檢查模板.md` — qa_type: CROSS_SCENE_CONTINUITY

**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §3.7（09_g algorithm）+ §3.8（09_h algorithm）+ §3.9（09_i algorithm）

**做法：**
- 模板格式同 D.1（5 層檢查框架）
- frontmatter `qa_type` 對應三種新 enum 值
- 各模板的具體 algorithm 從 UD §3.7-§3.9 抄入
- 加 `00_p QA 擴充協議接點 schema` 對齊聲明（屬 UD §3.10 接點 schema；本輪不寫 00_p 實檔）

**禁止：**
- **不**擅寫 algorithm 細節（必須對齊 UD §3.7-§3.9）
- **不**新建作品專屬內容（通用模板）
- **不**寫 `00_p` 實檔（CODEX tier 2 邊界）

**驗收：**
- 3 份模板結構完整
- frontmatter `qa_type` 對應 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY
- 對齊 UD §3.7-§3.9 algorithm

## D.2 實作 `/scene-task` skill（含中文別名）

**依賴：** D.0（依賴 00_k 協議）；Phase B 通過（需要 C-*、R-*、CH-*、S-* 等實體）

**產出：**
- `.claude/skills/scene-task/SKILL.md`
- `.claude/skills/場景任務包/SKILL.md`（中文別名 wrapper）

**做法：**
依 00_k 階段 1「任務包建立」執行 5 內部階段（見 ARCHITECTURE 第 6.1 節）：
1. **診斷階段**：讀 06_a 場景索引、檢查 W／V／C／R／P／CH 先決實體狀態（至少 REVIEW）；列出缺漏
2. **探索階段**：從 W-rules / V / C-* / R-*-* / 05_d 揭露表 / 05_e 伏筆 抽取本場必要資訊
3. **收斂階段**：整合成任務包草稿、列出缺漏（標 TODO）、問使用者要補哪些
4. **執行階段**：寫入 `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`，依 07_a 模板；frontmatter 完整含下游欄位（M7/M10 對齊 ARCHITECTURE 6.1）：`entities: [S-<n>-<m>]`、`狀態: DRAFT`、`scene_id: S-<n>-<m>`、`source_task: null`、`source_dialogue: null`、`pipeline_state: TASK_DRAFT`、`mode_tag: null`、`qa_decision: null`、`depends_on: [W-rules, V, <相關 C-*>, <相關 R-*-*>, P, CH-<n>]`
5. **驗證階段**：自動 `/status`，確認 S-<n>-<m> 出現；append `.protocol_version.phase_log` 一筆（含 scene_id、task_path）

任務包必填欄位完整對照 SPEC 第 12.5 節。

**驗收：**
- 跑 `/scene-task CH01 S03` 能產出 `07_scene_tasks/CH01_S03_台詞任務包.md`
- 任務包包含 SPEC 第 12.5 節所有必填欄位
- 缺漏項標 TODO，不擅自補完
- 跑 `/status` 能看到 S-01-03 出現

**禁止：**
- 不得擅自補完本場必須透露／禁止透露的資訊
- 不得擅自修改其他場景的任務包
- 不得擅自把任務包狀態升 REVIEW（必須人類審）

## D.2.5 任務包 REVIEW Gate（M3：在 D.3 之前）

**依賴：** D.2（至少有 1 個任務包 DRAFT）

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. 所有任務包檔（`07_scene_tasks/CH<n>_S<m>_台詞任務包.md`）當前 status 與 `pipeline_state`
2. 提示「`/dialogue-write` 需要任務包 REVIEW 才可跑；請人類審完後手動把 frontmatter `狀態` 改 REVIEW、`pipeline_state` 改 TASK_REVIEW」
3. 升級紀錄寫入 `_design/phase_d_task_review_log.md`（標準文件頭）

**驗收：**
- 至少 1 個任務包升 REVIEW + pipeline_state TASK_REVIEW
- 升級紀錄存在

**禁止：**
- CODEX 不得自行升級任務包狀態
- 不得直接跳到 D.3

## D.3 實作 `/dialogue-write` skill（含中文別名）

**依賴：** D.0、D.2、D.2.5（任務包必須先過 REVIEW gate）

**產出：**
- `.claude/skills/dialogue-write/SKILL.md`
- `.claude/skills/生成台詞/SKILL.md`（中文別名 wrapper）

**內容權威來源：** `UPSTREAM_DOWNSTREAM_SPEC.md` §4.1–§4.6（三模式 algorithm：§4.2 試寫、§4.3 收斂、§4.4 破格、§4.5 跨模式狀態總表、§4.6 與資料格式假設對齊）

**做法：**
依 00_k 階段 2「多版本試寫」執行 5 內部階段（見 ARCHITECTURE 第 6.2 節）；具體 algorithm 依 UPSTREAM §4：
1. **診斷階段**：確認任務包 `狀態=REVIEW` **且** `pipeline_state=TASK_REVIEW`（M3 D.2.5 gate 完成才會兩者同時成立）；列出 TODO 欄位；TODO 缺核心欄位即拒絕（量化見下）
2. **探索階段（可選）**：使用者明說「跑探索」時，先產短篇探索片段
3. **試寫階段（主流程）**：依 00_a 試寫模式與 08_b 模板，產 v01A / v01B / v01C 三版本
4. **破格階段（可選）**：使用者明說「跑破格」時，產 v01D 破格版，標 `mode_tag: EXPERIMENTAL`
5. **收斂階段（可選）**：使用者明說「直接收斂」時，跳過試寫直接整合

**執行階段** — 寫入 `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A.md` 等；frontmatter **完整含下游 8 欄**（M7/M10 全對齊）：
```yaml
entities: [S-<n>-<m>]
depends_on: [<相關 C-*, R-*-*>]
weight: {S-<n>-<m>: 1.0}
scene_id: S-<n>-<m>
source_task: <任務包相對路徑>
source_dialogue: null         # 試寫版自己就是源頭
source_dialogues: null        # 非收斂版填 null（僅 --converge 產出 v02 時填 trial list）
pipeline_state: DIALOGUE_TRIAL  # 收斂版改 DIALOGUE_CONVERGED
mode_tag: DRAFT_TRIAL           # 或 EXPERIMENTAL / CONVERGENCE
qa_decision: null
qa_type: null
```
中文 header 5 欄：`狀態: DRAFT`（收斂版改 REVIEW）+ 其他 4 欄。

**驗證階段** — 自動 `/status`；append `.protocol_version.phase_log` 一筆（含 `phase: dialogue-write`、`scene_id`、`dialogue_paths: [v01A 路徑, v01B 路徑, v01C 路徑]`、`mode_tag`）；建議下一步「人類挑亮點 + 收斂（D.3.5）」或（例外）「直接跑 /qa」

**輸入鎖定（O6 + M8 `--converge` contract）：** `/dialogue-write` 接受以下輸入形態，其他拒絕：

**A. 試寫模式（預設）：**
1. 完整任務包檔案路徑：`/dialogue-write 07_scene_tasks/CH01_S03_台詞任務包.md`
2. scene_id：`/dialogue-write S-01-03`（從 06_a 場景索引推導任務包路徑）
3. 無參數：使用上一輪 `/scene-task` 產出的任務包

→ 產 v01A/B/C，`pipeline_state: DIALOGUE_TRIAL`、`mode_tag: DRAFT_TRIAL`

**B. 破格模式：**
`/dialogue-write <輸入> --experimental` → 產 v01D，`mode_tag: EXPERIMENTAL`

**C. 收斂模式（M8 + #7 釐清）：**
`/dialogue-write <任務包輸入> --converge <v01A 路徑> <v01B 路徑> [...]` → 產 v02 收斂版

**輸入規則：**
- 必須含 1 個任務包輸入（A 的三種形態之一）+ **2 個以上既有 trial 版本路徑**
- 收斂模式**不再重新試寫**（跳過試寫階段），但**必須引用既有 trial 檔**作為素材
- 若使用者只提供任務包而無 trial 路徑 → 拒絕並提示「請先跑試寫模式產 trial 版本，或提供既有 trial 路徑」

**產出：**
- `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v02.md`
- frontmatter：`狀態: REVIEW`、`pipeline_state: DIALOGUE_CONVERGED`、`mode_tag: CONVERGENCE`、`source_dialogue: null`（單一不適用）、`source_dialogues: [v01A 路徑, v01B 路徑, ...]`（**複數欄位**列出引用的 trial）
- 收斂版自動由 D.3.5 gate 觸發；也可使用者手動指定

**TODO 拒絕條件量化（O5）：** 任務包以下「核心欄位」缺任一即拒絕：
- 出場角色
- 必須透露資訊
- 禁止透露資訊
- 出場角色聲線卡引用
- 角色表層目標
- 角色真實目標

（非核心欄位的 TODO 不阻擋執行，但會在報告中列出）

**驗收：**
- 跑 `/dialogue-write` 依任務包產 3 版本（DRAFT_TRIAL）
- 破格選項可獨立觸發產 EXPERIMENTAL 版
- 核心欄位缺漏時拒絕並列出缺什麼
- 每版 frontmatter 完整（含下游欄位）
- 不擅自標記 FINAL

**禁止：**
- 不得擅自把試寫版直接標 FINAL
- 不得把破格版混入正式 v01A/B/C（必須標 EXPERIMENTAL）
- 不得擅自修改任務包
- 不得跳過核心欄位拒絕邏輯

## D.3.5 收斂版人類選版 Gate（M8 鎖定下游閉環）

**依賴：** D.3（至少有 3 版本 DRAFT_TRIAL）

**做法：**

CODEX 印出以下清單供使用者人工檢視：

1. 所有 `pipeline_state: DIALOGUE_TRIAL` 的台詞檔
2. 提示使用者：「請挑亮點 + 決定本場走哪條路徑」：
   - **路徑 A（建議）**：人類挑亮點 → 跑 `/dialogue-write --converge` 產收斂版 v02 → 升 `pipeline_state: DIALOGUE_CONVERGED`、`狀態: REVIEW`、`mode_tag: CONVERGENCE` → 才進 D.4
   - **路徑 B（例外）**：使用者明確命令「直接對 v01A 跑 QA」→ 跳過收斂，直接進 D.4；但 QA_PASSED 後**不能直接升 FINAL**（必須先回 CONVERGENCE）
3. 升級紀錄寫入 `_design/phase_d_dialogue_review_log.md`（標準文件頭）

**驗收：**
- 至少 1 個台詞檔升 CONVERGENCE 或經使用者明示走路徑 B
- 升級紀錄存在

**禁止：**
- CODEX 不得自行決定走哪條路徑
- 不得跳過此 gate

## D.4 實作 `/qa` skill（含中文別名，v1.1 partial supersede via D-043：5 報告 → 8 報告必跑 + 09_e 維持拆出）

**v1.1 變動摘要：** D.4 由 v1.0「5 份 QA + 09_e 拆出」改為「**8 份 QA 必跑 + 09_e 維持 final-gating 紀錄**」（D-043 + CODEX C-11 解決）。新增 09_g 節奏感 / 09_h 對話張力 / 09_i 跨場一致性三份模板任務見 §D.1a（v1.1 新增 task）。

**依賴：** D.0、D.1、**D.1a（v1.1 新 — 09_g/h/i 模板）**、D.3、D.3.5（必須先過收斂 gate 或使用者明示路徑 B）+ A.0.8（qa_type_registry）

**產出：**
- `.claude/skills/qa/SKILL.md`
- `.claude/skills/檢查/SKILL.md`（中文別名 wrapper）

**內容權威來源（v1.1）：** `UPSTREAM_DOWNSTREAM_SPEC.md` §3.1–§3.9（**8 份** QA 模板各自的檢查 algorithm，含 §3.1 09_a / §3.2 09_b / §3.3 09_c / §3.4 09_d / §3.5 09_f / §3.7 09_g / §3.8 09_h / §3.9 09_i；§3.6 09_e 不在 /qa 範圍）+ §2.5（00_k 階段 3 的 5 個子階段；v0.3 對齊 D-043 序列順序）

**附加任務（P-009 暫定，原 D-011；v1.1 對齊 UD §9.1.1）：** 本 skill 實作期間同時修正既有 `08_a 台詞版本管理規範 §11.1` 對「必要 QA」的描述：「**09_a/b/c/d/f/g/h/i（由 /qa 產出 — v1.1 從 5 份擴為 8 份）；09_e 為 final-gating 紀錄**」。可在 D.4 或 D.5 完成此修正。

**做法（v1.1 對齊 D-043 + UD §2.5.3）：**
依 00_k 階段 3「QA」執行 5 內部階段（見 ARCHITECTURE §6.3）：
1. **診斷階段**：確認台詞檔 `狀態≥DRAFT` **且** `pipeline_state ∈ {DIALOGUE_CONVERGED, DIALOGUE_TRIAL}`（D.3.5 gate 完成才會有 CONVERGED；trial 是路徑 B 例外）；對照任務包讀本場規格
2. **執行階段（v1.1 — D-043 + 並行檢查 + 序列印出順序）**：依**八份** QA 模板分別跑檢查，全部必跑：
   - **並行檢查（同時跑 8 份）：** 09_a / 09_b / 09_c / 09_d / 09_f / **09_g / 09_h / 09_i**
   - **序列印出順序（UD §2.5.3 v0.3 + master 確認方向）：**
     1. 09_f 類型偏移檢查（qa_type=GENRE_DRIFT）— 最優先
     2. 09_d 資訊控制檢查（qa_type=INFO_CONTROL）
     3. **09_h 對話張力檢查（qa_type=DRAMATIC_TENSION）— v1.1 新**
     4. 09_b 聲線一致性檢查（qa_type=VOICE_CONSISTENCY）
     5. **09_g 節奏感檢查（qa_type=RHYTHM）— v1.1 新**
     6. 09_a AI 味檢查（qa_type=AI_FLAVOR）
     7. 09_c 禁用詞檢查（qa_type=FORBIDDEN_WORD）
     8. **09_i 跨場一致性檢查（qa_type=CROSS_SCENE_CONTINUITY）— v1.1 新；最後**
   - **09_e 不在此 skill 範圍**（09_e 是定稿變更紀錄，由人類在 final-gating 時填；v1.1 新增「LOCKED → DEPRECATED 降級紀錄」用途，見 SPEC §16a）
3. **彙整階段（v1.1 / D-043）**：依 SPEC §12.7（v1.1 對齊 8 份序列順序）統合最高優先問題；標 `qa_decision: PASS`（**8 份全 PASS**）或 `FAIL`（任一 FAIL）
4. **寫檔階段（v1.1 / D-043）**：在 `09_quality_assurance/` 下寫 **8 份**報告（原「5 份」supersede）；每份報告 frontmatter **完整含下游 8 欄**：
```yaml
entities: [S-<n>-<m>]
depends_on: [<相關 C-*、R-*-*>]
weight: {S-<n>-<m>: 0.125}      # v1.1 / D-043 — 8 份各 0.125 加總 1.0（原 5 份各 0.2 supersede）
scene_id: S-<n>-<m>
source_task: <任務包路徑>
source_dialogue: <目標台詞檔路徑>
source_dialogues: null
pipeline_state: QA_PASSED       # 或 QA_FAILED
mode_tag: null                  # M7 對齊：QA 報告自身無 mode_tag
qa_decision: PASS               # 或 FAIL（v1.1：8 份全 PASS 才 PASS）
qa_type: AI_FLAVOR              # 8 種之一（v1.1 / D-043 — AI_FLAVOR / VOICE_CONSISTENCY / FORBIDDEN_WORD / INFO_CONTROL / GENRE_DRIFT / RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY）
```
中文 header 5 欄齊全。

5. **驗證階段（v1.1 / D-043）**：自動 `/status`；更新台詞檔的 `pipeline_state` 與 `qa_decision`（只動 frontmatter，不動內容）；append `.protocol_version.phase_log` 一筆（含 `phase: qa`、`scene_id`、`target_dialogue: <台詞檔路徑>`、**`qa_report_paths: [8 份路徑]`**（原 5 份 supersede）、`qa_decision`）；列出 QA 結論與下一步建議

**輸入鎖定（O6）：** `/qa` 接受以下三種輸入，其他拒絕：
1. 完整台詞檔路徑：`/qa 08_dialogue_outputs/CH01_S03_<簡稱>_dialogue_v02.md`
2. scene_id + 版本：`/qa S-01-03 v02`（推導路徑）
3. 無參數：使用上一輪 `/dialogue-write` 收斂後產出的版本

**驗收（v1.1 / D-043）：**
- 跑 `/qa 08_dialogue_outputs/CH01_S03_*_v02.md` 產出**恰好 8 份** QA 報告（不多不少；原 5 份 supersede）
- 8 份報告的 frontmatter 各標不同 `qa_type`（8 種之一）
- **不**產生 09_e
- 彙整報告依 SPEC §12.7（v1.1）8 份序列順序排序
- 不直接修改原台詞檔
- 台詞檔的 `pipeline_state` 與 `qa_decision` 更新到位
- 跑 `/status` 能反映 QA 結果（含 9 種 status：8 QA + 09_e 是否齊全）

**禁止（v1.1 / D-043）：**
- 不得直接修改台詞檔內容（只能更新 frontmatter 的 pipeline_state / qa_decision）
- 不得擅自決定 PASS 進而升級台詞檔 `狀態`（升級需人類）
- 不得擅自刪除人類已標記「保留」的句子
- 不得產生 09_e
- 不得跳過 **8 份**其中任一報告（原「5 份」supersede）

## D.5 完整更新 README.md

**依賴：** D.1–D.4 全完成
**做法：**
- 補上完整的使用流程說明
- 補上 skill 清單與雙語別名表
- 補上「新使用者第一次怎麼用」的 quickstart
- 移除「v0.2-clean」之類的過渡狀態描述
- 升級版本到 v1.0

**驗收：**
- README.md 可作為新使用者的進入點
- 涵蓋所有 skill 與工作流

## D.6 建立《蟲潮孤堡》Instance repo 並搬移專案版 00_b

**依賴：** D.5
**做法：**
- 在 GitHub 建立新 repo `蟲潮孤堡-dialogue-bible`
- 從 Template repo 用 "Use this template" 複製
- 跑 `/init-project`，輸入蟲潮孤堡的專案基本資料
- 把 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md` 內容搬到 Instance 的 `00_protocol/00_b_反ai味檢查表.md`
- 在 `.protocol_version` 紀錄此次搬移

**驗收：**
- Instance repo 存在於 GitHub
- 包含完整 Template 內容 + 蟲潮孤堡專屬 00_b
- `.protocol_version` 完整紀錄

## D.6.5 Canon Delta 框架紀錄（Phase D 後成熟期 — P-011 + P-013 暫定，原 D-013 / D-015）

**依賴：** D.0、D.4（既有下游 pipeline 跑通）

**性質：** 本任務**不實作 skill**，僅紀錄 canon delta 框架的權威來源與重要性 threshold；實作留待 Phase E 或之後成熟期。

**做法：**
- 在 `_design/CANON_DELTA_FRAMEWORK.md`（新檔，可選）或本 TASKS.md 末附錄記錄：
  - 框架完整內容權威來源：`UPSTREAM_DOWNSTREAM_SPEC.md` §5.1–§5.8
  - master 暫定接受的「重要性 threshold」5 條規則（DECISIONS_LOG P-011，原 D-013）：
    - 涉及實體 ≤ C-* / R-*-* / V → 抽取
    - 涉及具體角色屬性（外觀、年齡、家庭、職業）→ 抽取
    - 涉及世界規則（魔法、科技、宗教）→ 抽取
    - 涉及一次性場景細節（穿著、心情、天氣）→ **不抽取**
    - 涉及單純情緒表達（「我難過」「我生氣」）→ **不抽取**
  - LOCKED 檔 retcon 走 UPSTREAM §3.6.6 路徑（DECISIONS_LOG P-013，原 D-015）：09_e 補 retcon 紀錄 + 原版降 DEPRECATED + 新版本走完整 pipeline

**驗收：**
- 框架紀錄文件存在
- DECISIONS_LOG P-011 與 P-013（原 D-013 / D-015）在文件中明示
- 不實作 skill；UPSTREAM §5 為唯一權威來源

**禁止：**
- 本輪不實作 canon delta 抽取演算法
- 不修改 `/qa` skill 觸發 canon delta 抽取（成熟期再加）

## D.7 Phase D 整體驗收

**依賴：** D.0–D.6 全完成
**做法：**
- 端到端測試（在《蟲潮孤堡》Instance 上）：
  1. 確認 W-rules / V / C-* / P / CH-* / S-* 都至少 REVIEW
  2. 跑 `/scene-task CH01 S03` 建立任務包
  3. 過 D.2.5 任務包 REVIEW gate（人類升 REVIEW）
  4. 跑 `/dialogue-write` 產 3 版台詞
  5. 過 D.3.5 收斂 gate（人類挑亮點 + 跑 `--converge` 或選路徑 B）
  6. 跑 `/qa` 對收斂版跑全套 **8 份** QA（v1.1 / D-043；原 5 份 supersede）
  7. 確認 **8 份** QA 報告生成（且不含 09_e）
  8. 跑 `/status` 確認所有實體完成度
  9. 驗證 `.protocol_version.phase_log` 含完整下游紀錄（task_path / dialogue_paths / qa_report_paths / target_dialogue）
- 撰寫 Phase D 驗收報告
- 撰寫整體交付完成報告

**Phase D 通過 → 系統完整可用。**

---

# 6. Skill 清單總表（執行順序檢視）

| Phase | Skill | 對應協議 |
|---|---|---|
| A | `/init-project` 初始化專案 | 00_i |
| A | `/create-world` 建立世界觀 | 00_e |
| A | `/status` 進度 | 無（純技術） |
| A | `/check-gaps` 缺漏檢查 | 無（純技術） |
| B | `/create-character` 建立角色 | 00_f |
| B | `/create-relationship` 建立關係 | 00_l |
| B | `/create-outline` 建立大綱 | 00_g |
| B | `/create-detailed-outline` 建立細綱 | 00_h |
| C | `/iterate-world` 迭代世界觀 | 00_j |
| C | `/iterate-character` 迭代角色 | 00_j |
| C | `/iterate-relationship` 迭代關係 | 00_j |
| C | `/iterate-outline` 迭代大綱 | 00_j |
| C | `/iterate-detailed-outline` 迭代細綱 | 00_j |
| C | `/view-*`（4 個）| 無（純技術） |
| C | `/export-*`（4 個）| 無（純技術） |
| C | `/diagnose` / `/integrate` | 00_a 模式入口 |
| D | `/scene-task` | 00_k 階段 1 |
| D | `/dialogue-write`（支援 `--experimental` 與 `--converge`）| 00_k 階段 2 |
| D | `/qa` | 00_k 階段 3 |

**總計：** 26 個英文 skill + 26 中文別名 = 52 個 SKILL.md（採 wrapper 策略可省半數內容維護）。

---

# 7. 整體交付完成標誌

當以下全部成立，本次重啟設計實作完成：

1. ✅ Template repo (`game-dialogue-bible-template`) 完整、可運作
2. ✅ Instance repo (`蟲潮孤堡-dialogue-bible`) 完整、含蟲潮孤堡專屬 00_b
3. ✅ 所有 4 phase 驗收通過（含 REVIEW gates A.10、B.5.5、B.6.5、B.8、D.2.5、D.3.5、wrapper smoke test）
4. ✅ `check_paths.py` 與 `check_headers.py` 對 Template 與 Instance 都 0 error
5. ✅ 26 個 skill 都可在 Claude Code 中觸發（中英文雙觸發）
6. ✅ 端到端流程：`/init-project` → `/create-world` → … → `/qa` 全程可走通
7. ✅ `.protocol_version.phase_log` 完整紀錄下游追蹤欄位（task_path / dialogue_paths / qa_report_paths）
8. ✅ README.md 與 `_design/` 文件齊全

---

# 8. 給 CODEX 審查者的建議

**請特別檢查（第三輪修正後）：**

1. **M7/M10 三份對齊**：SPEC 5.2 / ARCHITECTURE 6.1–6.3 / TASKS D.2–D.4 是否一致提到 pipeline_state / source_task / source_dialogue / qa_decision / qa_type
2. **A.0 parser 下游 7 欄**：是否完整列出在 TASKS A.0 + ARCHITECTURE 2.2，含 enum 驗證
3. **phase_log 下游追蹤**：task_path / dialogue_paths / qa_report_paths / target_dialogue 是否在 SPEC 5.4 schema 中
4. **REVIEW gates 完整性**：A.10 / B.5.5 / B.6.5 / B.8 / D.2.5 / D.3.5 是否覆蓋所有需要人類升級的階段
5. **C.2 不再要求重生 view**：依賴順序合理
6. **D.3 `--converge` contract**：A/B/C 三種輸入形態是否清楚
7. **O4 全域文件頭規則**：TASKS 1.4 是否覆蓋所有新 .md 報告
8. **A.9 依賴 A.5–A.8**：smoke test 順序正確

**審查通過後，從 A.0 開始實作。任何阻塞問題請列出，使用者裁決。**
