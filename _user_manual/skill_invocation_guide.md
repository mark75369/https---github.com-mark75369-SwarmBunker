狀態：DRAFT
版本：v0.2（11th master frontend Batch 4 — F10 / NEW_REQ_34 via D-072：新增 §7「副對話 / Sub-conversation 慣例（ingestion）」copy-paste 範本，指回 ARCH §3.3.3；原 §7/§8 順延為 §8/§9；§9 multi-agent cross-ref 補 §3.3.3；v0.1 → v0.2）
最後更新：2026-06-02
適用範圍：Cowork / Codex App user 的 skill copy-paste prompt 範本
優先級：中

# Skill Invocation Guide — Cowork / Codex App user 用 copy-paste 範本

## 0. 本檔用途

對 Claude Code CLI user：slash command 直接觸發（看 `CLAUDE.md`）。
對 Codex CLI user：agent 自動讀 `AGENTS.md` 後 user 對話啟動。
對 Codex App user：agent 會讀 `AGENTS.md`；若當前環境未自動載入，可貼本檔 prompt 引導。
對 Cowork user：agent 不自動讀 `.claude/skills/`；user 需要手動貼 prompt 引導 agent 讀對應 SKILL.md。

本檔提供每個 Phase A skill 的標準 copy-paste prompt。user 一次貼，agent 即能識別 skill 並執行 SKILL.md 5 階段流程。

素材放置：user 原始輸入素材（人設、既有劇本台詞、世界觀筆記等）統一放 `_source_materials/` 素材區供 skill 讀取參考；該區 `.md` 素材不需 5 欄 header（唯一例外為其 `README.md`），且不被掃描器計為實體。

## 1. 使用方法

1. 找到下方對應 skill 的「給 agent 的 prompt」段。
2. 整段 copy。
3. 貼到 Cowork / Codex App chat 內。
4. agent 讀 SKILL.md 後跟 user 確認啟動意圖。
5. 跟 agent 對話跑完 5 階段流程。

若 prompt 指向的 SKILL.md 不存在，agent 必須停止並回報尚未實作，不得用本檔摘要替代正式 skill。

## 2. /init-project — 初始化專案

### 用途摘要

建立新 Instance repo 的 bootstrap：`.protocol_version`、三份 registry copy、`10_art_assets/` 七個 subtype 目錄、`.gitignore`，以及限 `00_b` / `00_c` / `00_d` 的 Template 微調。

### 給 agent 的 prompt（整段 copy）

```text
請讀取本 repo 內 .claude/skills/init-project/SKILL.md 的完整內容，依該檔規範執行 /init-project skill 流程。

本 skill 用於建立新 Instance repo 的 bootstrap：
- 階段 1: 對 user 詢問新專案基本資料（作品名、repo name、Template source、Template commit、bootstrap date、類型、長度、語氣、輸出偏好、參考作品）
- 階段 2: 列限定 00_b / 00_c / 00_d 的微調候選
- 階段 3: user 拍板每個微調，印 Bootstrap 收斂預告稿
- 階段 4: 嚴格依 SKILL.md 寫檔順序執行（.protocol_version / 三 registry copy / 10_art_assets/ / .gitignore / 00_b-00_d 微調 / verify）
- 階段 5: 驗證並建議下一步 /create-world

請完整對齊 SKILL.md 規範，不擅自跳階段、不擅自微調 00_a / 00_e 到 00_l / 01-09 模板。若偵測到 Template repo 或已完成 bootstrap，依 SKILL.md 的 Prerequisites Not Met 格式停止。
```

## 3. /create-world — 建立世界觀

### 用途摘要

建立作品世界觀基礎：`W-rules`、`W-language`、`V`，寫入 `01_world/`、`02_vocabulary/`、作品專屬 `00_b` §1/§2，並更新 `.protocol_version.phase_log`。

### 給 agent 的 prompt（整段 copy）

```text
請讀取本 repo 內 .claude/skills/create-world/SKILL.md 的完整內容，依該檔規範執行 /create-world skill 流程。

本 skill 用於建立世界觀：
- Phase 1: 診斷 user 貼上的世界觀材料，只在 chat 內產出診斷報告，不寫檔
- Phase 2: 讀 issue_type_registry.yaml，依 00_e_world 動態議題清單提問；每次最多三題
- Phase 3: 印 world convergence preview，列 target files、00_b §1/§2 preview、TODO / INFERENCE / CONFLICT、entities 與 split plan
- Phase 4: user 明確通過後，依固定順序寫 01_world/、02_vocabulary/、00_b §1/§2
- Phase 5: 驗證 W-rules / W-language / V，更新 phase_log，並自動呼叫 /status；不得自動呼叫 /create-character

請完整對齊 SKILL.md 規範，不擅自跳階段、不把推論寫成正式設定、不建立角色/關係/大綱/場景/台詞。若 target file 為 LOCKED 或必要 registry 無法讀取，依 SKILL.md 的錯誤格式停止。
```

## 4. /status — 進度查詢

### 用途摘要

列實體完成度、下一步建議、卡點、場景就緒度、模組狀態、三欄區、A-* Asset Panel、相關 view 連結。此 skill 屬純讀取。

### 給 agent 的 prompt（整段 copy）

```text
請讀取本 repo 內 .claude/skills/status/SKILL.md 的完整內容，依該檔規範執行 /status skill 流程。

本 skill 用於純讀取進度查詢：
- Stage 1: 檢查 Instance 是否已完成 bootstrap；若 .protocol_version 或 phase_log 不符合條件，依 Prerequisites Not Met 格式停止
- Stage 2: 讀 _design/expected_entities.yaml、.protocol_version phase_log，以及 scripts/parse_frontmatter.py 的 build_repo_index(".")
- Stage 3: 從 completed phase_log 推導 expected entity set，不把 entities_touched 當作 created entities
- Stage 4: 依 ARCH §2.3 / SPEC §5.3 公式計算每個 entity 完成度，並另外列 downstream artifact gaps
- Stage 5: 輸出邏輯實體完成度、缺漏實體、未追蹤實體、非 blocking asset section 與下游檔案檢查

請完整對齊 SKILL.md 規範。此 skill 純讀取，不得寫檔、修 header、更新 .protocol_version、修改 LOCKED 檔或自動觸發其他 skill。
```

## 5. /check-gaps — 缺漏檢查

### 用途摘要

掃描 TODO、A-* 缺檔、過期 view、KEY 衝突、frontmatter 缺必填欄位、依賴實體不存在等缺漏。此 skill 屬純讀取。

### 給 agent 的 prompt（整段 copy）

```text
請讀取本 repo 內 .claude/skills/check-gaps/SKILL.md 的完整內容，依該檔規範執行 /check-gaps skill 流程。

本 skill 用於純讀取缺漏檢查：
- Stage 1: 使用 scripts/parse_frontmatter.py 的 build_repo_index(".") 建立 repo index；若 parser ERROR，先停止並列前 5 項 ERROR
- Stage 2: 掃 TODO / INFERENCE / CONFLICT marker、空 entities 但有內容的檔案、expected but missing entities 與 artifact gaps
- Stage 3: 檢查 view/ 整合檔是否因 source mtime 較新而失效；若沒有 view/，輸出正常空狀態
- Stage 4: 依缺漏類型對應下一個 user-triggered skill，但不得自動觸發
- Stage 5: 依 SKILL.md 固定順序輸出四段報告：marker、entities 漏標、缺漏實體、view/ 整合檔需更新

請完整對齊 SKILL.md 規範。此 skill 純讀取，不得寫檔、更新 .protocol_version、修改 LOCKED 檔、修補缺漏或自動觸發其他 skill。
```

## 6. 已 implemented skill 對照中文 wrapper

| 英文 skill | 中文 wrapper | 觸發內容對照 |
|---|---|---|
| `/init-project` | `/初始化專案` | 同流程，中文 description；執行時以 `.claude/skills/init-project/SKILL.md` 為權威 |
| `/create-world` | `/建立世界觀` | 同流程，中文 description；執行時以 `.claude/skills/create-world/SKILL.md` 為權威 |
| `/status` | `/進度` | 同流程，中文 description；執行時以 `.claude/skills/status/SKILL.md` 為權威 |
| `/check-gaps` | `/缺漏檢查` | 同流程，中文 description；執行時以 `.claude/skills/check-gaps/SKILL.md` 為權威 |

中文 wrapper 在 Cowork 內 user 也可貼上述「給 agent 的 prompt」段；agent 應對齊主 skill，不建立第二套流程。

## 7. 副對話 / Sub-conversation 慣例（ingestion）

當你要餵大量既有素材（既有劇本 / docx / 長人設 / .txt / .csv / .json）給某個 skill 時，建議**另開一個副對話**只做讀取萃取，主對話保留 skill 階段推進。權威規則 8 條見 `_design/ARCHITECTURE.md` §3.3.3；要點：副對話只讀不寫、明列讀過/未讀的檔、只回 evidence 摘要（不整段貼回）、skill stage 留在主對話、**主對話別太早關副對話**、同任務 reuse 同一副對話。

### 給副對話的 prompt（整段 copy）

```text
請在這個副對話只做「讀取與萃取」，不要寫任何檔。
- 讀：<列出要讀的素材路徑 / 檔名，含 docx / txt / csv / json>
- 回報三段：(a) 你實際讀過的檔清單 (b) 讀不到 / 讀不全的部分（環境不支援 docx、檔過長只抽樣、解析失敗都要講）(c) 萃取出的聲線 / 設定 evidence 摘要——給「檔名 + 段落 / 行」定位，不要把原文整段貼回。
請保持這個副對話開啟，我可能會追問補讀；未經我明示請勿結束。
```

### 主對話端維持 / 結束副對話的 wording

```text
[追讀] 沿用同一副對話（不要另開），補讀 <X> 場景的素材，回報增量 evidence。
[結束] ingestion 完成，這個副對話可以收了。
```

## 8. Phase B+ skill 未實作

預定 skill 將在 Phase B / C / D 落地，包含 `/create-character`、`/create-relationship`、`/create-outline`、`/create-detailed-outline`、`/iterate-*`、`/view-*`、`/export-*`、`/scene-task`、`/dialogue-write`、`/qa`、`/diagnose`、`/integrate` 與中文 wrapper。屆時需同步更新：

- `AGENTS.md`
- `CLAUDE.md`
- `_user_manual/skill_invocation_guide.md`

## 9. 相關文件

- 對 Claude Code CLI user：直接用 slash command（看 `CLAUDE.md`）
- 對 Codex CLI / Codex App user：看 `AGENTS.md`
- 各 skill SKILL.md 權威：`.claude/skills/<name>/SKILL.md`
- 詳細 multi-agent 慣例：`_design/ARCHITECTURE.md` §3.3.0（invocation）+ §3.3.3（副對話 lifecycle）
- A.12 task 權威：`_design/TASKS.md` v1.5 §A.12
