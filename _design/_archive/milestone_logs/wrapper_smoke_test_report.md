狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Phase A 後段 A.9 wrapper smoke test 結果
優先級：高

# wrapper_smoke_test_report — A.9 Wrapper Smoke Test 結果

## 0. 測試環境

- 測試日期：2026-05-20
- 測試 agent：Codex App
- repo SHA：99cb281b0d4526e453257b35ee5dc8bc088fd821
- limitations：
  - 本輪只在 Codex App 對話環境測試。
  - Codex App 依 AGENTS.md discovery + 明確讀取 `.claude/skills/<name>/SKILL.md` 執行；不是 Claude Code CLI 原生 slash dispatcher。
  - Claude Code CLI / Codex CLI / Cowork 未在本輪實跑，需由 user 於各 host 親測。
  - 當前 repo 為 Template repo：root 存在 `.template_root`，`.protocol_version` 不存在，`_design/registries/*.template.yaml` 存在。所有 skill 僅測到 trigger identification / main skill load / prerequisite check，不進任何寫檔階段。

## 1. /初始化專案 smoke test

- **Trigger identification：** ✓ PASS
  - AGENTS.md skill 清單可將 `/初始化專案` 對應到 `.claude/skills/初始化專案/SKILL.md`。
  - wrapper frontmatter 已讀到 `name: 初始化專案`。
  - wrapper description 指向 `/init-project` 中文別名與 `.claude/skills/init-project/SKILL.md`。
- **Main skill load：** ✓ PASS
  - 已讀取 `.claude/skills/init-project/SKILL.md`。
  - 主檔定義完整 5 階段：Diagnosis / Exploration / Convergence / Codex Execution / Verification。
  - 主檔 v0.2 含 D-049 Template-detect 兩道防線。
- **Stage 1 prerequisite check 行為：** ✓ PASS
  - pre-Stage 1 偵測到 `.template_root` 存在，依 D-049 第一道防線應拒絕執行。
  - 同時 `_design/registries/*.template.yaml` 存在且 `.protocol_version` 不存在，D-049 第二道防線也會擋下。
  - 未進入 Stage 4，未寫 `.protocol_version`、registry copy、`10_art_assets/` 或 `.gitignore`。
- **結論：** ✓ PASS
- **發現 / 觀察：**
  - wrapper 沒有展開第二套流程，符合 ARCH §3.2 選項 2 wrapper 設計。
  - Template repo 上的拒絕行為符合 ARCH §3.3.2 與 DECISIONS_LOG D-049。
- **建議 fallback（若 fail）：** N/A

## 2. /建立世界觀 smoke test

- **Trigger identification：** ✓ PASS
  - AGENTS.md skill 清單可將 `/建立世界觀` 對應到 `.claude/skills/建立世界觀/SKILL.md`。
  - wrapper frontmatter 已讀到 `name: 建立世界觀`。
  - wrapper description 要求執行 `../create-world/SKILL.md` 完整流程。
- **Main skill load：** ✓ PASS
  - 已讀取 `.claude/skills/create-world/SKILL.md`。
  - 主檔定義完整 5 階段：Diagnostic / Exploration / Convergence / Execution / Validation。
  - 主檔明確要求 `.protocol_version` 存在，並於 Phase 4 前不得寫檔。
- **Stage 1 prerequisite check 行為：** ✓ PASS
  - 當前 repo `.protocol_version` 不存在，依 `/create-world` 啟動條件應在 Phase 1 前停止，要求先跑 `/init-project`。
  - 因 repo 同時存在 `.template_root`，本輪未進入世界觀診斷開場。
  - 未寫入 `01_world/`、`02_vocabulary/`、`00_protocol/00_b_反ai味檢查表.md` 或 `.protocol_version.phase_log`。
- **結論：** ✓ PASS
- **發現 / 觀察：**
  - wrapper 僅導向英文主檔，不新增規則，符合 A.11 對 wrapper 的驗證項。
  - 主檔載入後能到達正確的 repo-state gate。
- **建議 fallback（若 fail）：** N/A

## 3. /進度 smoke test

- **Trigger identification：** ✓ PASS
  - AGENTS.md skill 清單可將 `/進度` 對應到 `.claude/skills/進度/SKILL.md`。
  - wrapper frontmatter 已讀到 `name: 進度`。
  - wrapper description 指向 `/status` 中文別名與 `.claude/skills/status/SKILL.md`。
- **Main skill load：** ✓ PASS
  - 已讀取 `.claude/skills/status/SKILL.md`。
  - 主檔定義完整 5 階段：Diagnosis / Exploration / Derive Expected Set / Calculate Completion / Output。
  - 主檔要求使用 `scripts.parse_frontmatter.build_repo_index(".")`，並以 `_design/expected_entities.yaml` + `.protocol_version.phase_log` 推導 expected set。
- **Stage 1 prerequisite check 行為：** ✓ PASS
  - `_design/expected_entities.yaml` 存在，`scripts/parse_frontmatter.py` 存在。
  - `.protocol_version` 不存在，因此依主檔應停止於 prerequisite check，輸出 `Instance 尚未完成 Bootstrap`，下一步為先執行 `/init-project`。
  - 因 prerequisite 未通過，未計算完成度，也未掃描或修補任何 frontmatter。
- **結論：** ✓ PASS
- **發現 / 觀察：**
  - wrapper 沒有自行計算完成度，符合 wrapper 不展開第二套流程的要求。
  - Codex App 已能讀到英文主檔的 5 階段流程；完整 5 階段因 Template repo 未 bootstrap 而未執行，屬正常阻擋。
- **建議 fallback（若 fail）：** N/A

## 4. /缺漏檢查 smoke test

- **Trigger identification：** ✓ PASS
  - AGENTS.md skill 清單可將 `/缺漏檢查` 對應到 `.claude/skills/缺漏檢查/SKILL.md`。
  - wrapper frontmatter 已讀到 `name: 缺漏檢查`。
  - wrapper 權威來源指向 `../check-gaps/SKILL.md`。
- **Main skill load：** ✓ PASS
  - 已讀取 `.claude/skills/check-gaps/SKILL.md`。
  - 主檔定義完整 5 階段：Diagnosis / five scan dimensions / view refresh detection / gap-to-skill suggestions / Output。
  - 主檔輸出固定 4 段：TODO-INFERENCE-CONFLICT、entities 漏標、expected but missing、view/ 需更新。
- **Stage 1 prerequisite check 行為：** ✓ PASS
  - `_design/expected_entities.yaml` 存在，`scripts/parse_frontmatter.py` 存在，`view/` 不存在且屬可正常略過的狀態。
  - `.protocol_version` 不存在，因此依主檔應停止於 prerequisite check，要求先完成 `/init-project`。
  - 因 prerequisite 未通過，未建立 repo index，未產生 gap 報告，也未寫任何檔案。
- **結論：** ✓ PASS
- **發現 / 觀察：**
  - wrapper 明確禁止展開第二套流程，符合 ARCH §3.2 wrapper 策略。
  - Codex App 已能載入主檔並辨識完整 read-only 流程；完整 5 階段因 Template repo 未 bootstrap 而未執行，屬正常阻擋。
- **建議 fallback（若 fail）：** N/A

## 5. 4 skill 總結

| Wrapper | Trigger ID | Main Load | Stage 1 | 結論 |
|---|---|---|---|---|
| /初始化專案 | ✓ | ✓ | ✓ Template-detect 擋下 | PASS |
| /建立世界觀 | ✓ | ✓ | ✓ `.protocol_version` missing 擋下 | PASS |
| /進度 | ✓ | ✓ | ✓ `.protocol_version` missing 擋下 | PASS |
| /缺漏檢查 | ✓ | ✓ | ✓ `.protocol_version` missing 擋下 | PASS |

## 6. 整體結論

- A.9 task 結果：△ PARTIAL
- Codex App current-host 結果：✓ PASS
- PARTIAL 理由：本輪只測 Codex App，未在 Claude Code CLI / Codex CLI / Cowork 各 host 實跑中文 slash command。
- 4 個中文 wrapper 在 Codex App 的 trigger identification、main skill load、prerequisite check 都通過。
- 未發現需要啟動 ARCH §3.2 選項 3 fallback 的 host 失敗案例。
- 後續行動：若 master 接受 current-host smoke test limitation，可進 A.10；若要求完整 host matrix，需由 user 在 Claude Code CLI / Codex CLI / Cowork 補跑後追加本報告。

## 7. Fallback 紀錄到 .protocol_version

本輪無 fallback 實例，且當前為 Template repo，不寫 `.protocol_version`。

若未來某 host 走 fallback，應在對應 Instance 的 `.protocol_version` 記錄：

```yaml
wrapper_fallbacks:
  - wrapper: /進度
    host: cowork
    fallback: copy_main_skill_content
    date: 2026-05-20
    note: <理由>
```
