狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase A 後段 A.9 task 啟動包 — Wrapper Smoke Test  
優先級：高

# CODEX_A9_STARTER — Phase A 後段 A.9：Wrapper Smoke Test

# 0. 本檔用途

Wave 5 第一條 task — 跑 4 個 Phase A skill 的中文 wrapper smoke test（A.5 / A.6 / A.7 / A.8 對應中文 wrapper）+ 寫 `_design/wrapper_smoke_test_report.md`，對齊 TASKS v1.7 §A.9（C-10 裁決：選 A wrapper + smoke test）。

**前置條件：** Wave 4 全 DONE（A.7 / A.8 / A.12 三產出落地）+ master 第六輪 Critical patch round D-049 已落地（包含 init-project SKILL.md v0.2 + .template_root marker）。

**與後續 task 的關係：** A.9 PASS → 進 A.10（人類 REVIEW gate）→ A.11（Phase A 整體驗收，含 Wave 4 review consolidation）。

⚠ **A.9 特殊性：** 本 task 是「**實機觸發測試**」屬性，不是「寫新檔」屬性。CODEX 需要在實機 Claude Code 環境（或對等的 sandbox）中以中文 slash command 觸發各 skill，觀察 agent 是否真的執行了英文主 skill 的 5 階段流程。**若無法跑實機**，CODEX 必須在報告內明示 limitation + 提供 fallback（複製主檔內容 / 等 user 親自跑）。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.9 task」— wrapper smoke test，對齊 TASKS v1.7 §A.9（C-10 裁決：選 A wrapper + smoke test）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer + verifier — 本輪跑 4 skill 的中文 wrapper smoke test + 撰寫驗證報告
- 對應傳統：Wave 5 第一條 task（依序：A.9 → A.10 → A.11）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔
- ✗ **不**動 `_tools/frontend/` 任何檔
- ✗ **不**改 `.claude/skills/*/SKILL.md` 任何檔（包括英文主檔 + 中文 wrapper）
- ✗ smoke test 失敗時**不**擅自修改主 skill 邏輯（fallback 是改 wrapper，不是改主 skill；本輪即使要改也不直接改 — 必須回 master 拍板）
- ✗ **不**跑真實 /init-project 寫檔（會污染 Template repo；smoke test 限「trigger 識別 + 確認 agent 讀到 SKILL.md」階段，不進 stage 4 寫檔）

**本 task scope（嚴格限定）：**

依 TASKS v1.7 §A.9（line 785-805）+ ARCH §3.2 wrapper 機制 + ARCH §3.3.0 multi-agent invocation 慣例。

### 任務目標

跑 4 個中文 wrapper 的 smoke test：
- `/初始化專案` → 應觸發 init-project skill
- `/建立世界觀` → 應觸發 create-world skill
- `/進度` → 應觸發 status skill
- `/缺漏檢查` → 應觸發 check-gaps skill

寫 `_design/wrapper_smoke_test_report.md`（v0.1 DRAFT；含 5 必填中文 header）紀錄結果。

### Smoke Test 流程

對每個中文 wrapper：

1. **Trigger identification（必跑）：**
   - 確認 agent 能識別中文 slash command（如 user 輸入 `/進度` 後 agent 對應到 `.claude/skills/進度/SKILL.md`）
   - 確認 agent 讀對應 wrapper 的 SKILL.md frontmatter `name` + `description`
   - 確認 agent 從 wrapper 內 reference 找到英文主檔（如 `.claude/skills/status/SKILL.md`）

2. **Main skill load（必跑）：**
   - 確認 agent 讀完英文主檔的 5 階段流程
   - 觀察 agent 是否「準備執行」（如印出 stage 1 prerequisite check / 階段 1 開場 / 等）
   - **不要進入 stage 4 寫檔**：smoke test 在 stage 1 prerequisite check 或階段 1 開場後即可停（避免污染或副作用）

3. **可選 — Stage 1 verify（部分）：**
   - 對 `/進度` 和 `/缺漏檢查`（純讀 skill）：可跑完整 5 階段（無寫檔副作用）— 但因 .template_root 存在會擋住 prerequisite check → 屬正常 detect → 紀錄
   - 對 `/初始化專案` 和 `/建立世界觀`：只跑到 prerequisite check 為止（不進 stage 4）

### Fallback 處理（若 smoke test 失敗）

依 TASKS §A.9 規定：
- 若某 host（如 Cowork / Codex App）trigger 失敗 → 紀錄 host 名 + 失敗類型（如「agent 不識別 /進度」或「agent 識別但讀不到 main skill」）
- Fallback 策略：**該 host 改用選項 3（複製主檔內容）**作為 wrapper 內容；但本 task **不執行** fallback 動作（屬未來修補；本 task 只紀錄）

### 報告結構（`_design/wrapper_smoke_test_report.md`）

```markdown
狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：Phase A 後段 A.9 wrapper smoke test 結果  
優先級：高

# wrapper_smoke_test_report — A.9 Wrapper Smoke Test 結果

## 0. 測試環境

- 測試日期：YYYY-MM-DD
- 測試 agent：[Claude Code CLI / Codex CLI / Cowork / Codex App / N/A]
- repo SHA：<commit-sha>
- limitations（如有）：[本輪只能跑 X agent 環境，其他環境留 user 親跑]

## 1. /初始化專案 smoke test

- **Trigger identification：** ✓ PASS / ✗ FAIL（理由）
- **Main skill load：** ✓ PASS / ✗ FAIL（理由）
- **Stage 1 prerequisite check 行為：** [印出 Bootstrap 先決檢查摘要 / 偵測 .template_root marker 並拒絕 / etc]
- **結論：** ✓ PASS / △ PARTIAL / ✗ FAIL
- **發現 / 觀察：** [筆記]
- **建議 fallback（若 fail）：** N/A 或 [host X 改 wrapper 為選項 3 複製主檔]

## 2. /建立世界觀 smoke test

（同上結構）

## 3. /進度 smoke test

（同上結構；可跑完整 5 階段，紀錄輸出格式對齊 ARCH §2.3 範例）

## 4. /缺漏檢查 smoke test

（同上結構；可跑完整 5 階段，紀錄 4 段輸出對齊 starter 規範）

## 5. 4 skill 總結

| Wrapper | Trigger ID | Main Load | Stage 1 | 結論 |
|---|---|---|---|---|
| /初始化專案 | ✓/✗ | ✓/✗ | ✓/✗ | PASS / PARTIAL / FAIL |
| /建立世界觀 | ✓/✗ | ✓/✗ | ✓/✗ | PASS / PARTIAL / FAIL |
| /進度 | ✓/✗ | ✓/✗ | 完整 5 階段 | PASS / PARTIAL / FAIL |
| /缺漏檢查 | ✓/✗ | ✓/✗ | 完整 5 階段 | PASS / PARTIAL / FAIL |

## 6. 整體結論

- A.9 task 結果：✓ PASS / △ PARTIAL / ✗ FAIL
- 後續行動：[進 A.10 / 修補 wrapper / 拍板 fallback]

## 7. Fallback 紀錄到 .protocol_version

若有任一 host 走 fallback 路徑，需把對應紀錄寫入該 Instance 的 `.protocol_version`（屬 Phase B 後 Instance bootstrap 後紀錄；本 task 只在報告內列指引，不真寫）：

```yaml
wrapper_fallbacks:
  - wrapper: /進度
    host: cowork
    fallback: copy_main_skill_content
    date: YYYY-MM-DD
    note: <理由>
```
```

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/TASKS.md` v1.7（§A.9 line 785-805 + A.11 Wave 4 review consolidation 段）
2. `_design/ARCHITECTURE.md` v1.5 §3.2（wrapper 機制 — 選項 2 wrapper + fallback 選項 3）+ §3.3.0（multi-agent invocation 慣例）+ §3.3.2（Template-detect 規範）
3. `_design/SPEC.md` v1.2 §10（缺漏偵測規格，給 /缺漏檢查 smoke test 參考）

B. 對齊依據
4. `.claude/skills/init-project/SKILL.md` v0.2 + `.claude/skills/初始化專案/SKILL.md`（A.5 + master 第六輪 D-049 patch）
5. `.claude/skills/create-world/SKILL.md` + `.claude/skills/建立世界觀/SKILL.md`（A.6）
6. `.claude/skills/status/SKILL.md` + `.claude/skills/進度/SKILL.md`（A.7）
7. `.claude/skills/check-gaps/SKILL.md` + `.claude/skills/缺漏檢查/SKILL.md`（A.8）
8. `_design/DECISIONS_LOG.md` v1.3 §6.11.2（D-049 Template-detect 機制）

C. 已 LOCKED 不可動文件
9. 所有 `_design/*.md` 既有 spec（除新建 wrapper_smoke_test_report.md 外不動）
10. `scripts/*.py`
11. 既有 27 模板
12. `00_protocol/*` 全部
13. `_tools/frontend/*` 全部
14. 所有 `.claude/skills/*/SKILL.md`（除非 fallback 啟動，且 fallback 必須先回 master 拍板）

---

**你要交付的產物：**

新建 1 個檔：
1. `_design/wrapper_smoke_test_report.md`

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- `_design/wrapper_smoke_test_report.md` 存在
- 5 必填中文 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
- 報告含上述 7 段全部

B. 內容
- 4 個 wrapper smoke test 結果全部列出（Trigger ID + Main Load + Stage 1）
- 整體結論明確（PASS / PARTIAL / FAIL）
- limitations 明示測試 agent 環境
- 若有 fallback 建議，符合 ARCH §3.2 選項 3 規範

C. 不破壞既有
- 不動所有 `.claude/skills/*/SKILL.md`
- 不動 `_design/` 既有 spec
- 不動 `00_protocol/` / `_tools/frontend/` / `scripts/` / 27 模板
- 不跑寫檔 stage 4 副作用（不污染 Template）
- `python scripts/check_headers.py` 0 ERROR 維持

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓ + 4 wrapper 整體結論寫進報告（PASS / PARTIAL / FAIL）
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 4 wrapper 任一 trigger ID 失敗 → 修補 round（master 拍板 fallback 機制）
- **PARTIAL：** 部分 host 環境無法跑 → 報告內明示 limitation + 留待 user 親跑

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.9 完成 → user commit/push → 回 master → master 推 A.10（人類 REVIEW gate；master 印 DRAFT 待升 REVIEW 清單給 user）→ user 親自跑 A.10 → master 寫 CODEX_A11_STARTER.md（含 Wave 4 review consolidation）→ A.11 PASS → Phase A 收尾。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.9 task 啟動包；完成後可 archive 進 `_design/archive/`
- A.9 報告 `wrapper_smoke_test_report.md` 屬持續寫作（後續 Phase B/C/D wrapper 上線時繼續加 entry）— 不 archive
- 若 A.9 NO-GO patch round → 開 CODEX_A9_PATCH_STARTER.md（同 A.0F.1 模式）
