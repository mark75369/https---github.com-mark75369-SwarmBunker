狀態：DRAFT
版本：v0.1（F14 context-budget 瘦身：自 AGENTS.md / CLAUDE.md 移出完整 skill 清單 / 版本落地狀態 / QA 模板表 / Phase 里程碑 / 相關 spec 清單；root 檔僅保留精簡索引 + 指向本檔）
最後更新：2026-06-02
適用範圍：完整 skill 註冊表 — 按需讀取，不必每次對話載入
優先級：一般

# Skill 完整註冊表（按需讀取）

> 本檔是 `AGENTS.md` / `CLAUDE.md` 精簡 skill 索引的「完整版」。root 指令檔只保留精簡索引（指令名 + path 慣例）以節省每次對話的 context；當你需要查 **完整 path、版本、落地狀態、QA 模板、Phase 里程碑、相關 spec** 時才讀本檔。

## Agent 環境對應

| Agent 環境 | Discovery 機制 | Invocation 方式 |
|---|---|---|
| Claude Code CLI | 自動讀 root `CLAUDE.md` + 自動 discovery `.claude/skills/*/SKILL.md` | user 直接用 slash command 觸發 |
| OpenAI Codex CLI | 自動讀 root `AGENTS.md` | user 在 chat 內提 skill name，agent 依本表讀 SKILL.md |
| Codex App | 自動讀 root `AGENTS.md` | 同 Codex CLI；必要時可搭配 `_user_manual/skill_invocation_guide.md` |
| Cowork | 不自動讀 root `CLAUDE.md` / `.claude/skills/` | user 手動貼 `_user_manual/skill_invocation_guide.md` 對應 skill prompt |

## Phase A skill 清單（含中文 wrapper）

| Skill | Path | 觸發語 | 用途摘要 | 狀態 |
|---|---|---|---|---|
| init-project | `.claude/skills/init-project/SKILL.md` | `init-project` / `/init-project` | 從 Template clone 建新 Instance：bootstrap `.protocol_version` + 三 registry copy + `10_art_assets/` 結構 + `.gitignore` | 已實作 |
| 初始化專案 | `.claude/skills/初始化專案/SKILL.md` | `初始化專案` / `/初始化專案` | `/init-project` 中文 wrapper；執行時以英文主檔為權威 | 已實作 |
| create-world | `.claude/skills/create-world/SKILL.md` | `create-world` / `/create-world` | 建立世界觀：寫 `01_world/`、`02_vocabulary/`、作品專屬 `00_b` §1/§2，並更新 phase log | 已實作 |
| 建立世界觀 | `.claude/skills/建立世界觀/SKILL.md` | `建立世界觀` / `/建立世界觀` | `/create-world` 中文 wrapper；執行時以英文主檔為權威 | 已實作 |
| status | `.claude/skills/status/SKILL.md` | `status` / `/status` | 列實體完成度 + 缺漏建議；純讀取 | 已實作 |
| 進度 | `.claude/skills/進度/SKILL.md` | `進度` / `/進度` | `/status` 中文 wrapper；執行時以英文主檔為權威 | 已實作 |
| check-gaps | `.claude/skills/check-gaps/SKILL.md` | `check-gaps` / `/check-gaps` | 掃 TODO / INFERENCE / CONFLICT、缺漏實體、view 失效；純讀取 | 已實作 |
| 缺漏檢查 | `.claude/skills/缺漏檢查/SKILL.md` | `缺漏檢查` / `/缺漏檢查` | `/check-gaps` 中文 wrapper；執行時以英文主檔為權威 | 已實作 |

## Phase B+ skill 清單（含實作狀態）

| Phase | Slash Command | 中文 wrapper | 狀態 |
|---|---|---|---|
| B | `/create-character <name>` | `/建立角色 <name>` | ✅ 已實作（v0.4；Round 11 R11-CRITICAL-01 修補；含 D-050 + D-053 exception block）|
| B | `/create-relationship <a> <b>` | `/建立關係 <a> <b>` | ✅ 已實作（v0.3；含 D-050 + D-053 exception block）|
| B | `/create-outline` | `/建立大綱` | ✅ 已實作（v0.3；含 D-050 + D-053 exception block）|
| B | `/create-detailed-outline` | `/建立細綱` | ✅ 已實作（v0.3；含 D-050 子裁決 1+2 雙 block + R8-MA-01 prereq fix）|
| B | `/create-org <name>` | `/建立組織 <name>` | ✅ 已實作（v0.2；F8 Phase 3 / D-074 amendment；依 00_n 組織創建協議 v0.2 issue-ful 5 階段（動態讀 issue_type_registry 00_n_organization）+ ORG card 7 段；限寫 11_organizations/；ORG-* 無聲線卡、不進 /dialogue-write）|
| C | `/scene-task <scene_id>` | `/場景任務包 <scene_id>` | ✅ 已實作（v0.2；D-055 STYLE_ANCHOR 落地 — §3.2 抽取來源表新增 W-style 行對應 task pack §18.4 文風錨定子節；含 D-054 hybrid fallback per-scene → aggregate 06_a）|
| C | `/dialogue-write <scene_id>` | `/生成台詞 <scene_id>` | ✅ 已實作（v0.3；D-055 STYLE_ANCHOR — Stage 1 診斷新增「文風錨定狀態」；指紋來源 = 01_world/01_d；mode_tag enum：ORGANIZED / DRAFT_TRIAL / EXPERIMENTAL / CONVERGENCE / FINAL_CANDIDATE / SINGLE_ITER）|
| C | `/qa <dialogue_path>` | `/檢查 <dialogue_path>` | ✅ 已實作（v0.1；D-043 8 報告必跑：09_a/b/c/d/f/g/h/i；序列順序對齊 UD §2.5.3 v0.3；09_e 屬人類 final-gating 不入 /qa）|
| D | `/iterate-world` | `/迭代世界觀` | ✅ 已實作（v0.1；Wave 12 CODEX batch commit fa21b65；含 D1 starter v0.3 + 00_j v0.2）|
| D | `/iterate-character <name>` | `/迭代角色 <name>` | ✅ 已實作（v0.1；Wave 12 commit fa21b65；含 D2 starter v0.3 + 00_j v0.2）|
| D | `/iterate-relationship <a> <b>` | `/迭代關係 <a> <b>` | ✅ 已實作（v0.1；Wave 12 commit fa21b65；含 D3 starter v0.3 + 00_j v0.2）|
| D | `/iterate-outline` | `/迭代大綱` | ✅ 已實作（v0.1；Wave 12 commit fa21b65；含 D4 starter v0.2 + 00_j v0.2）|
| D | `/iterate-detailed-outline` | `/迭代細綱` | ✅ 已實作（v0.1；Wave 12 commit fa21b65；含 D5 starter v0.4 + 00_j v0.2 + D-054 hybrid fallback）|
| D | `/iterate-scene <S-ID> --split-to-file` | (無中文 wrapper) | ✅ 已實作（v0.1；Wave 12 commit fa21b65；D-054 NEW_REQ_15 split-to-file；含 D5 starter v0.4 + 00_j v0.2 §10.7）|
| D | `/iterate-org <name>` | `/迭代組織 <name>` | ✅ 已實作（v0.2；F8 Phase 3 / D-074 amendment；clone iterate-character、issue-ful（載 00_n_organization guidance）；00_j v0.2 type-agnostic 基底 + 00_n v0.2 context；ORG card 7 段；限寫 11_organizations/；ORG 無聲線卡）|
| D | `/view-world` | `/查看世界觀` | ✅ 已實作（v0.1；Wave 13；純讀取；chat 動態組合；不加 breadcrumb / TOC）|
| D | `/view-character <name>` | `/查看角色 <name>` | ✅ 已實作（v0.1；Wave 13；聲線卡 + 關係 + 時間線 + 弧線 + 出場場景；含 D-054 compatible scene discovery）|
| D | `/view-outline` | `/查看大綱` | ✅ 已實作（v0.1；Wave 13；主線 / 章節 / 弧線 / 資訊揭露 / 伏筆整合；純讀取）|
| D | `/view-detailed-outline` | `/查看細綱` | ✅ 已實作（v0.1；Wave 13；含 D-054 hybrid：per-scene first / aggregate 06_a fallback / missing placeholder）|
| D | `/export-world` | `/匯出世界觀` | ✅ 已實作（v0.1；Wave 14；寫 `<instance_root>/view/世界觀.md` DERIVED 7 欄；breadcrumb + 條件 TOC + return link + phase_log audit）|
| D | `/export-character <name>` | `/匯出角色 <name>` | ✅ 已實作（v0.1；Wave 14；寫 `<instance_root>/view/角色-<name>.md` DERIVED 7 欄；含 D-054 compatible scene discovery；11th master NEW_REQ_24 已拍板 hyphen 檔名，參見 export-character SKILL.md）|
| D | `/export-outline` | `/匯出大綱` | ✅ 已實作（v0.1；Wave 14；寫 `<instance_root>/view/大綱.md` DERIVED 7 欄；breadcrumb + 條件 TOC）|
| D | `/export-detailed-outline` | `/匯出細綱` | ✅ 已實作（v0.1；Wave 14；寫 `<instance_root>/view/細綱.md` DERIVED 7 欄；含 D-054 hybrid 完整三 phase）|
| D+ | `/diagnose` | `/診斷` | ✅ 已實作（v0.1；Wave 15；對齊 00_a §3.3；Mode A/B/C；6 段診斷報告；純讀取；phase_log optional audit）|
| D+ | `/integrate` | `/整理` | ✅ 已實作（v0.1；Wave 15；對齊 00_a §3.4；Stage 4a 印 diff / Stage 4b user 拍板後寫檔；D-050 / D-052 / D-054 boundary）|

## QA 模板落地狀態（9 個）

| 模板 | qa_type | 狀態 |
|---|---|---|
| `09_a_ai味qa報告模板.md` | AI_FLAVOR | ✅ 既有 |
| `09_b_角色聲線一致性檢查模板.md` | VOICE_CONSISTENCY | ✅ 既有 |
| `09_c_禁用詞檢查報告模板.md` | FORBIDDEN_WORD | ✅ 既有 |
| `09_d_資訊控制檢查報告模板.md` | INFO_CONTROL | ✅ 既有 |
| `09_e_定稿變更紀錄模板.md` | (final-gating；非 /qa) | ✅ 既有 |
| `09_f_類型偏移檢查模板.md` | GENRE_DRIFT | ✅ 既有 |
| `09_g_節奏感檢查模板.md` | RHYTHM | ✅ C4 patch round 補建（v0.1）|
| `09_h_對話張力檢查模板.md` | DRAMATIC_TENSION | ✅ C4 patch round 補建（v0.1）|
| `09_i_跨場一致性檢查模板.md` | CROSS_SCENE_CONTINUITY | ✅ C4 patch round 補建（v0.1）|

## Skill 執行慣例（Codex CLI / Codex App）

1. user 提 skill name（如「跑 init-project」或「我要建立世界觀」）。
2. agent 讀本表對應 Path；若狀態是 TBD 或檔案不存在，停止並回報尚未實作，不得用 manual 骨架自行替代。
3. agent 完整讀完對應 SKILL.md 後，再向 user 確認啟動意圖。
4. agent 依 SKILL.md 的 5 階段流程執行，不擅自跳階段、不擅自輸出邏輯。
5. 階段 4 寫檔前列出寫檔清單再確認；階段 5 驗證後印「下一步建議」。

## Phase 階段對應（master 詞彙）

- **Phase A**（Milestone 1 達成）：`init-project` / `create-world` / `status` / `check-gaps` 已實作，並含中文 wrapper。
- **Phase B**（Milestone 2 達成）：`/create-character` / `/create-relationship` / `/create-outline` / `/create-detailed-outline` 5 上游 skill 全實作（含 D-050 + D-053 exception block）。
- **Phase C**（Milestone 3 達成；2026-05-21）：`/scene-task` / `/dialogue-write` / `/qa` 3 下游 skill 全實作，含中文 wrapper；8 個 `/qa` 必跑模板齊全（09_a/b/c/d/f/g/h/i）；D-054 hybrid fallback 設計落地。
- **Phase D**（對應 TASKS §C 視圖 / 迭代 / 匯出 / 整合）：
  - Wave 12：✅ 已落地（CODEX batch commit fa21b65 — 6 SKILL.md + 5 中文 wrapper；含 D-054 NEW_REQ_15 `/iterate-scene --split-to-file`）
  - Wave 13：✅ 已實作（`/view-*` x 4 + 4 中文 wrapper）
  - Wave 14：✅ 已實作（`/export-*` x 4 + 4 中文 wrapper；L3 prompt generator 屬未來 master scope）
  - Wave 15：✅ 已實作（`/diagnose` + `/integrate` + 2 中文 wrapper；Canon Delta framework 落地於 `_design/CANON_DELTA_FRAMEWORK.md` v0.1）

## 相關 spec

- `_design/ARCHITECTURE.md` §3.3（skill 內容規範）+ §3.3.0（multi-agent invocation 慣例）+ §6.4/§6.5/§6.6/§6.7（Phase D 視圖/迭代/匯出/整合）
- `_design/DECISIONS_LOG.md` §6.12 D-050（/create-* skill 寫檔邊界）+ §6.16 D-053（/create-world exception）+ §6.17 D-054（per-scene 檔 Hybrid）
- `_design/TASKS.md` §A.12 + §C（Phase D task）
- `_design/PHASE_C_COMPLETION_REPORT.md` / `_design/PHASE_D_COMPLETION_REPORT.md`（里程碑事實檔）
- `_design/POST_LOCK_PENDING.md`（NEW_REQ 狀態追蹤）
- `_design/M4_USER_TEST_REPORT.md`（M4 量產 19 finding；F1/F3/F6/F14 等修補來源）
- `_user_manual/skill_invocation_guide.md`（對 Cowork / Codex App user 的 copy-paste 範本）
