狀態：DRAFT
版本：v0.1（11th master 對話 A 落地 — 工具角色轉換 + Claude Code Dynamic Workflows audit / screening 戰略方向 + sandbox bootstrap 指引 + 11 audit 任務 spec + first-run 建議 + 結論回流流程）
最後更新：2026-06-01
適用範圍：給 user 在 D:\劇本開發工具\_sandbox\snapshot\ 內跑 Claude Code Dynamic Workflows audit；本檔屬 sandbox bootstrap 指引 + audit 任務基底 + 結論回流流程性質；對 production 無 LOCKED spec 影響
優先級：高

# SANDBOX_REFACTOR_PLAN — Claude Code Dynamic Workflows audit 戰略落地包

# 0. 文件目的

10th master Milestone 4 真正封版宣告完成後（PHASE_D_COMPLETION_REPORT v1.1 §10），11th master 對話 A（Cowork）內 user reframe 11th master scope：

- **工具角色轉換**：從「自動寫作 pipeline」轉成「QA + 初始資料建置 + 專案管理」+ 外接寫作（外部 API / 工具產 dialogue → 接回工具 A 跑 QA）
- **11+ 輪累積 tech debt 篩檢**：用 Claude Code 2026-05-28 ship 的 Dynamic Workflows（1000 subagent 並行 audit / screening）跑大重構
- **Sandbox boundary**：實驗 fork 跑 audit，不直接迭代成 production；audit 結論走人工 cherry-pick / transcribe 回 production

11th master 對話 A 從原「跑 NEW_REQ_20 frontend patch」轉成「寫交接文件 + 後續 REVIEW Claude Code 產出」模式。本檔屬該轉向的核心交接物件。

# 1. 戰略背景與 Dynamic Workflows fit 度

## 1.1 工具角色轉換的合理性

工具 A 設計初衷是「對話式建構長篇遊戲劇本 Bible + 用 skill chain 半自動產台詞」。10 輪 master 對話 + Milestone 4 真正封版宣告後 user 在 M4 user-test 階段觀察到核心限制：

- LLM 直接生 dialogue 品質仍受 base model 影響；工具 A 的 skill chain 雖有 QA 8 模板 + 三層守則 + Voice Bible 等護欄，但「品質的 ceiling 仍由外部寫作工具決定」
- 11+ 輪 master 對話累積的 tech debt（NEW_REQ_9 baseline 老債 / NEW_REQ_16 lint script 未實作 / 51 SKILL.md 部分可能 dead code / POST_LOCK_PENDING 多項 DEFERRED 狀態未巡檢 / K-NN 表跨 batch 累積未統一 inventory 等）需要大規模 cleanup
- 既有 frontend dashboard 三欄區（NEW_REQ_20）等 Phase A.0F.2 alpha 階段 placeholder 殘留屬「現工具角色未來會被重塑前提下，patch 也短壽」

結論：工具 A 後續定位 = QA 工具 + 初始資料建置工具 + 專案管理工具；寫作走外部 API / 工具（如 Claude API 直接呼叫 / Codex CLI 跑 / 其他 LLM 工具）→ 產出 dialogue 接回工具 A 跑 QA 8 模板 + 09_e 人類拍板紀錄 + 升 FINAL 流程。

## 1.2 Dynamic Workflows fit 度

Claude Code 2026-05-28 ship 的 Dynamic Workflows 支援：

- 1000 subagent 並行 audit（research preview；上限 1000）
- 主 agent 整合 subagent 報告
- 並行不互相 block；比序列 batch 快 100x
- 跨檔 consistency check / 跨檔 grep / 大量 dimension 全掃

這正對應 11+ 輪累積 tech debt 篩檢需求：

| Dynamic Workflows 強項 | 11+ 輪累積需求 fit |
|---|---|
| 並行 audit 多檔 / 多 dimension | 篩檢冗餘 / 找小毛病（11 個 audit 任務分 Cat A/B/C/D 四類）|
| 跨檔 consistency check | 找做一半的東西 + Template / Instance 同步議題 |
| 大量 dimension 全掃 | 51 SKILL.md dead code audit + K-NN 表 inventory |
| 主 agent 整合 subagent 報告 | 一次性 surface 所有議題給 user 拍板 |

不適合的方向：用 Dynamic Workflows 自動產台詞（並行不解決品質 ceiling 問題；屬「對症錯藥」）。

## 1.3 Sandbox 紀律

研究預覽期 + 1000 subagent 並行 + 寫操作潛在 race condition 風險 → 必須 sandbox 跑：

- ✗ 不直接動 production（D:\劇本開發工具\）
- ✗ Subagent 不 auto-commit
- ✗ 不從 sandbox 直接 cp 檔回 production（避免污染）
- ✓ Sandbox 在 production 子目錄（_sandbox/）便於 master REVIEW + 共用 .git 但 .gitignore 排除
- ✓ Subagent 首試強制 read-only mode（純 audit report 輸出；不寫檔）
- ✓ Audit 結論走人工 cherry-pick / transcribe 回 production（master 讀完 audit-reports/ → 寫對應 NEW_REQ_22+ 進 POST_LOCK_PENDING 或寫獨立 audit report 進 _design/）
- ✓ Audit 結束 rm -rf _sandbox/ 重 bootstrap baseline（避免長期殘留污染）

---

# 2. Sandbox bootstrap 指引

## 2.1 目錄結構

```
D:\劇本開發工具\                       ← production；不動
  ├── _design/                          ← production；不動
  ├── _tools/                           ← production；不動
  ├── _user_manual/                     ← production；不動
  ├── .claude/                          ← production；不動
  ├── 00_protocol/                      ← production；不動
  ├── 01_world/ ... 10_art_assets/      ← production；不動
  ├── AGENTS.md / CLAUDE.md / README.md ← production；不動
  ├── .gitignore                        ← 11th master 對話 A 新建；加 /_sandbox/ 排除
  └── _sandbox/                         ← 11th master 對話 A 新建；.gitignore 排除
      ├── README.md                     ← sandbox 用途 + 紀律 + cleanup 指引
      ├── snapshot/                     ← production 完整快照（Claude Code 在這裡跑 audit）
      │   └── (production 內容鏡像；不含 .git / _sandbox / node_modules)
      └── audit-reports/                ← Claude Code 產出的 audit report 暫存（user 閱讀 + master REVIEW）
```

## 2.2 PowerShell bootstrap 指令

```powershell
cd D:\劇本開發工具

# 1. 建 sandbox 子目錄結構
mkdir _sandbox
mkdir _sandbox\snapshot
mkdir _sandbox\audit-reports

# 2. cp production 內容進 snapshot（推薦用 robocopy，原生支援多目錄排除）
robocopy . _sandbox\snapshot /E /XD .git _sandbox node_modules .venv __pycache__ /XF *.pyc

# robocopy 退出碼 0-7 屬正常（8+ 才是 error）
# 預期看到 "Files copied: N / Dirs copied: M"

# 3. verify bootstrap 完成
cd _sandbox\snapshot
ls _design\ | Measure-Object   # 應該跟 production _design/ 同檔數
ls .claude\skills\ | Measure-Object  # 應該看到 51 SKILL.md
ls 00_protocol\ | Measure-Object  # 應該看到 13 protocol
test-path .git    # 應該 False（snapshot 內無 .git）

# 4. 回 production 跑 git status verify .gitignore 排除生效
cd D:\劇本開發工具
git status   # 應該看不到 _sandbox/ 任何條目（被 .gitignore 排除）
```

## 2.3 alternative：xcopy（如 robocopy 不可用）

```powershell
# 先建 exclude-list.txt
@"
\.git\
\_sandbox\
\node_modules\
\__pycache__\
\.venv\
"@ | Out-File -Encoding ascii _sandbox\exclude-list.txt

xcopy /E /I /Y /EXCLUDE:_sandbox\exclude-list.txt . _sandbox\snapshot\
```

## 2.4 .gitignore 排除確認

production root .gitignore 應含（11th master 對話 A task 5 落地）：

```
# Sandbox for Claude Code Dynamic Workflows audit (2026-Q2)
# 詳 _design/SANDBOX_REFACTOR_PLAN.md
# audit 結束 rm -rf _sandbox/ 重 bootstrap baseline
/_sandbox/
```

bootstrap 後 production root 跑 `git status` 應該 _sandbox/ 完全不出現。

---

# 3. 11 audit 任務 spec

各 audit 任務含：name / category / mode（read-only / write）/ scope / expected_output / token estimate / first-run flag。

**全 11 項首試強制 read-only mode**（純 audit report 輸出；不動 sandbox snapshot 內檔）。寫操作（cleanup / fix）走 master 人工 transcribe 回 production 路徑。

## 3.1 Cat A — 冗餘 / 重複內容 audit

### A1 — 4 角色聲音資訊跨檔 dedupe【first-run 推薦】

| 欄位 | 內容 |
|---|---|
| name | 4 角色聲音資訊跨檔 dedupe + 矛盾偵測 |
| category | A 冗餘 / 重複內容 |
| mode | read-only |
| scope | sandbox snapshot 內 03_characters/main/*_聲線卡.md + 01_world/01_d_*.md（如有）+ 02_vocabulary/02_c_*.md（如有）+ 03_characters/03_a_*.md（如有）+ 任何 character voice 相關 ref |
| 任務 | 對每個有「聲線」資訊的角色：(1) 列出所有出現位置 / (2) dedupe 出 unique 欄位 / (3) 標 source of truth / (4) 找出跨檔矛盾（同欄位但不同 wording / value）/ (5) 提出對齊建議 |
| expected_output | sandbox/audit-reports/A1_voice_dedup_<timestamp>.md：含 (per 角色 5 子節) + 全 repo 矛盾 summary table |
| token estimate | ~20K-50K（4-8 角色 × 5-8 處 source × 跨檔 grep）|
| ROI 目的 | 直接看 Dynamic Workflows 對「跨檔 dedupe + 矛盾偵測」強度 |

### A2 — 跨 spec 重複概念 source-of-truth 標示

| 欄位 | 內容 |
|---|---|
| name | _design/ 內 10 LOCKED spec 跨檔重複概念 source-of-truth 標示 |
| category | A 冗餘 / 重複內容 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/*.md（10 LOCKED spec：REQUIREMENTS_LOCK / DECISIONS_LOG / SPEC / ARCHITECTURE / TASKS / DATA_FORMAT_SPEC / INTEGRATION_CONTRACTS / UPSTREAM_DOWNSTREAM_SPEC / UX_SPEC / L3_EXPORT_PROMPT_SCHEMA）|
| 任務 | 對重複出現概念（如「D-050 寫檔邊界」/「D-054 hybrid fallback」/「entity weight」/「phase_log schema」等）：(1) 列出所有出現位置 / (2) 標 source of truth（哪份 spec 是權威）/ (3) 找出 wording 差異 / (4) 提出 cross-ref 對齊建議 |
| expected_output | sandbox/audit-reports/A2_spec_dedup_<timestamp>.md：含 (per 重複概念 4 子節) + cross-ref 缺漏 table |
| token estimate | ~50K-150K（10 spec × ~30 重複概念 × 跨檔 grep）|

### A3 — 大綱 / 細綱 / 場景索引重疊區域對齊 issue

| 欄位 | 內容 |
|---|---|
| name | 05_plot/05_a 主線大綱 + 05_plot/05_b 細綱 + 06_scene_index/06_a 場景索引三者重疊區域對齊 audit |
| category | A 冗餘 / 重複內容 |
| mode | read-only |
| scope | sandbox snapshot 內 05_plot/* + 06_scene_index/* |
| 任務 | (1) 三者 entity overlap（CH / S）/ (2) 同 entity ID 跨檔 metadata 對齊（如 weight / status / depends_on）/ (3) D-054 hybrid（aggregate 06_a vs per-scene 檔）混用情況 / (4) 找出 stale ref（主線改了細綱沒同步等）|
| expected_output | sandbox/audit-reports/A3_outline_alignment_<timestamp>.md：含 entity overlap matrix + cross-ref 缺漏 table |
| token estimate | ~30K-80K |

## 3.2 Cat B — 做一半 / 過度建構

### B1 — POST_LOCK_PENDING NEW_REQ_1~21 status 巡檢

| 欄位 | 內容 |
|---|---|
| name | POST_LOCK_PENDING NEW_REQ_1~21 status 巡檢 + DEFERRED too long candidate |
| category | B 做一半 / 過度建構 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/POST_LOCK_PENDING.md 全檔 |
| 任務 | (1) 對 21 個 NEW_REQ 標準化 status（RESOLVED / DEFERRED / PROCESSED / BLOCKED）/ (2) DEFERRED 超過 60 天且無 trigger 條件達成 candidate close / (3) PROCESSING 無進度 candidate 重啟 owner / (4) 跟 DECISIONS_LOG D-NNN 拍板對齊 cross-ref / (5) 建議 close / 維持 / 升級處理 |
| expected_output | sandbox/audit-reports/B1_new_req_status_<timestamp>.md：含 21 NEW_REQ status table + 建議 actions |
| token estimate | ~30K-60K（POST_LOCK_PENDING.md ~40K token）|

### B2 — _design/ CODEX_*_STARTER.md 落地狀態 inventory

| 欄位 | 內容 |
|---|---|
| name | _design/ CODEX_*_STARTER.md 全清單 + 落地狀態 inventory |
| category | B 做一半 / 過度建構 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/CODEX_*.md（含 CODEX_D1_STARTER / CODEX_D5_STARTER / CODEX_D_W12_STARTER / CODEX_D_FINAL_STARTER 等）|
| 任務 | (1) 列全清單 / (2) 對每個 starter：CODEX 是否實際跑過 / 跑出產物有沒有落地 / 跟 SKILL.md / spec 對齊度 / (3) 分類：✓ 落地 + 跑通 / ✓ 落地但未跑 / ✗ 寫了沒跑 / ✗ obsolete / (4) 建議 close / archive / 重跑 |
| expected_output | sandbox/audit-reports/B2_codex_starter_inventory_<timestamp>.md：含全清單 table + 分類 |
| token estimate | ~40K-80K（~20 starter × 短 grep verify）|

### B3 — .claude/skills/ 51 SKILL.md dead code audit

| 欄位 | 內容 |
|---|---|
| name | .claude/skills/ 51 SKILL.md 反查 dead code + invocation path audit |
| category | B 做一半 / 過度建構 |
| mode | read-only |
| scope | sandbox snapshot 內 .claude/skills/*/SKILL.md + AGENTS.md + CLAUDE.md skill 表 |
| 任務 | (1) 列 51 SKILL.md 全清單 + (2) AGENTS.md / CLAUDE.md / user_manual 是否引用 / (3) 中文 wrapper 對英文主檔對應正確 / (4) 議題清單 / 階段 / 流程是否實際對齊 spec / (5) dead code candidate 標示 |
| expected_output | sandbox/audit-reports/B3_skill_audit_<timestamp>.md：含 51 SKILL.md table + dead code candidate + 建議 close / fix |
| token estimate | ~80K-200K（51 SKILL.md × cross-ref）|

### B4 — K-NN 表跨 batch inventory 統一【first-run 推薦】

| 欄位 | 內容 |
|---|---|
| name | K-NN 表（STYLE_ANCHOR batch K-01~K-09；first-run B4 verify 僅單 batch 無其他 batch）統一 inventory + 分類 + RESOLVED / OPEN 標示 |
| category | B 做一半 / 過度建構 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/* + 任何含 K-NN ref 的檔（grep "K-\d+"）|
| 任務 | (1) 全 repo grep 出所有 K-NN ref / (2) per K-NN：分類（STYLE_ANCHOR batch / 其他 batch）+ source 起源 + status（RESOLVED / OPEN / OBSOLETE）/ (3) 跨 batch 重複編號 audit / (4) 統一 inventory table |
| expected_output | sandbox/audit-reports/B4_knn_inventory_<timestamp>.md：含全 K-NN table + 分類 + status |
| token estimate | ~20K-50K |
| ROI 目的 | 直接看 Dynamic Workflows 對「跨對話累積 issue 收斂」能力 |

## 3.3 Cat C — stale ref / 漂移

### C1 — D-055 編號衝突 audit【first-run 推薦】

| 欄位 | 內容 |
|---|---|
| name | D-055 編號衝突全 audit + rename 方案提案 |
| category | C stale ref / 漂移 |
| mode | read-only |
| scope | sandbox snapshot 全 repo grep "D-055" |
| 任務 | (1) 找出所有 D-055 ref / (2) 分類：(a)「指 STYLE_ANCHOR」/ (b)「指 per-scene supersede candidate」/ (c) 其他 / (3) 提出 rename 方案（如 D-055 維持原意 + D-055a / D-055b 分流，或 D-055 → D-056 升一個編號）/ (4) 影響範圍評估 |
| expected_output | sandbox/audit-reports/C1_d055_conflict_<timestamp>.md：含全 D-055 ref table + 分類 + rename 方案 |
| token estimate | ~15K-30K |
| ROI 目的 | 直接看 Dynamic Workflows 對「全 repo grep + 分類 + 提案」能力 |

### C2 — HANDOFF_TO_* stale 內容歸檔 candidate

| 欄位 | 內容 |
|---|---|
| name | 多輪 master（7th-11th）累積 HANDOFF_TO_*.md 各檔 stale 內容歸檔 candidate audit |
| category | C stale ref / 漂移 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/HANDOFF_TO_*.md + _design/HANDOFF_11TH_*.md + _design/archive/HANDOFF_*.md（如有）|
| 任務 | (1) 列全 HANDOFF 清單 + (2) per HANDOFF：哪些 §段內容 stale（已被後 master 對話 supersede）/ 哪些仍 active / (3) archive candidate（建議哪些檔該 mv 進 _design/archive/）/ (4) cross-ref 衝突點 |
| expected_output | sandbox/audit-reports/C2_handoff_stale_<timestamp>.md：含全 HANDOFF table + archive 建議 |
| token estimate | ~30K-80K |

### C3 — CLAUDE.md / AGENTS.md vs .claude/skills/ 漂移 audit

| 欄位 | 內容 |
|---|---|
| name | CLAUDE.md / AGENTS.md 內 skill 清單表 vs 實際 .claude/skills/ 內容 cross-check 漂移點 |
| category | C stale ref / 漂移 |
| mode | read-only |
| scope | sandbox snapshot 內 CLAUDE.md + AGENTS.md + .claude/skills/*/SKILL.md |
| 任務 | (1) CLAUDE.md / AGENTS.md skill 表內每 row：對應 SKILL.md 實際存在？/ 版本對齊？/ 狀態 ✅ / ⏳ TBD 正確？/ (2) 反向：實際 SKILL.md 是否在表內？/ (3) 漂移點清單 |
| expected_output | sandbox/audit-reports/C3_skill_table_drift_<timestamp>.md：含漂移點 table + fix 建議 |
| token estimate | ~30K-50K |

## 3.4 Cat D — Template / Instance 同步

### D1 — Instance _design/ 同步議題 audit（K-07）

| 欄位 | 內容 |
|---|---|
| name | Instance repo（D:\劇本開發工具-test\）_design/ 同步議題全 audit |
| category | D Template / Instance 同步 |
| mode | read-only |
| scope | sandbox snapshot 內 _design/* + Instance repo（D:\劇本開發工具-test\_design/*）|
| 任務 | (1) Template vs Instance _design/ 檔逐檔 diff / (2) Instance 端應該不含 _design/（屬 Template-only）但實際可能有殘留 / (3) 哪些 Instance 端檔該被清掉 / 哪些是合法 Instance-specific patch / (4) 嚴重程度分類 |
| expected_output | sandbox/audit-reports/D1_instance_design_sync_<timestamp>.md：含 diff table + 清理建議 |
| token estimate | ~40K-100K（如 Instance repo 已 init；如未 init 此 audit skip）|
| 注意 | 需 user pre-condition：D:\劇本開發工具-test\ 已存在且有內容；如未 init 則 audit skip + 紀錄為「pre-condition not met」|

### D2 — .claude/skills/ Instance 端 stale 程度跨檔同步

| 欄位 | 內容 |
|---|---|
| name | .claude/skills/ Template vs Instance 端 stale 程度跨檔同步狀態總表 |
| category | D Template / Instance 同步 |
| mode | read-only |
| scope | sandbox snapshot 內 .claude/skills/* + Instance repo 對應目錄（如存在）|
| 任務 | (1) 51 SKILL.md per skill：Template 版本 vs Instance 版本（如有）/ (2) Instance scene-task 是否仍 v0.1（user raise）等 stale point / (3) 跨檔同步狀態總表 + fix 建議 |
| expected_output | sandbox/audit-reports/D2_skill_instance_sync_<timestamp>.md：含 sync table |
| token estimate | ~50K-100K |
| 注意 | 同 D1 pre-condition |

---

# 4. First-run 建議

## 4.1 推薦三項：A1 + B4 + C1（並行 read-only audit）

| audit | category | 涵蓋 audit 類型 | 估 token |
|---|---|---|---|
| A1 | A 冗餘 / 重複內容 | 跨檔 dedupe + 矛盾偵測 | 20K-50K |
| B4 | B 做一半 / 過度建構 | 跨對話累積 issue 收斂 inventory | 20K-50K |
| C1 | C stale ref / 漂移 | 全 repo grep + 分類 + 提案 | 15K-30K |

**三項合計估 token：50K-130K**；耗時 10-30 分鐘 wall-time（依 subagent 並行度）。

**理由**：
- 三項都是純 audit / read-only → 安全
- 三項都有明確 expected output → 容易評估好壞（user + master 都能 verify）
- 三項涵蓋 dedupe / inventory / cross-ref 三種主流 audit 類型 → 一次試完看 ROI 廣度
- 三項合計 token < 200K → 不燒爆 Max plan 額度
- 三項都不需要 D1 / D2 的 Instance pre-condition

## 4.2 second-run（first-run ROI 評估後）

如 first-run 結果 user + master REVIEW 認為 ROI 合理（audit 品質 high；fabricated finding 少；可採用 finding 數量 > 5），擴大 second-run 範圍：

- 加 A2（10 LOCKED spec 重複概念）
- 加 B1（NEW_REQ_1~21 status 巡檢）
- 加 C3（CLAUDE.md / AGENTS.md drift）

second-run 估 token：100K-300K。

## 4.3 third-run（建立穩定 audit pipeline 後）

剩餘 audit（A3 / B2 / B3 / C2 / D1 / D2）依優先級分批跑。建議優先 B3（dead code）+ C2（HANDOFF archive）+ B2（CODEX_*_STARTER inventory）— 因為 cleanup ROI 高。

D1 / D2 視 Instance repo 是否 init 而定（pre-condition gating）。

## 4.4 audit 品質評估指標

每次 audit 結束 user + master 需共同評估：

| 維度 | 指標 |
|---|---|
| 完整性 | 預期 scope 是否全覆蓋（無 grep miss）|
| 準確性 | finding 是否事實正確（無 fabrication）|
| 可採用率 | finding / 建議實際被採納的比例（target ≥ 60%）|
| 可重現性 | 同 audit 重跑結果是否一致（target ≥ 80%）|

如可採用率 < 30% → audit prompt 需重設計或 Dynamic Workflows 本身對該類任務不適合。

---

# 5. Audit 結論回流流程

## 5.1 流程概覽

```
[Step 1] user 在 sandbox/snapshot/ 跑 Claude Code Dynamic Workflows audit
    ↓
[Step 2] Claude Code 產出 audit-reports/<task>_<timestamp>.md
    ↓
[Step 3] user 切回 Cowork 對話 A 帶 audit report（截圖 / 貼文字 / 上傳檔）
    ↓
[Step 4] master REVIEW audit report：cross-check + 標 fabricated finding + 提採納建議
    ↓
[Step 5] user 拍板「採」/「改」/「棄」each finding
    ↓
[Step 6] master 把採納 finding 人工 transcribe 回 production：
    - finding 屬「新議題」→ 寫 NEW_REQ_22+ 進 _design/POST_LOCK_PENDING.md
    - finding 屬「拍板需求」→ 升 D-056+ 拍板（user 拍板後落地）
    - finding 屬「audit summary 紀錄」→ 寫 _design/AUDIT_2026Q2_REPORT.md
    - finding 屬「明顯小 typo / wording fix」→ 直接 edit 對應 production 檔 + GIT SUMMARY
    ↓
[Step 7] user 手動 commit + push production 變動
    ↓
[Step 8] sandbox 內 audit-reports 視需要保留（或 audit pipeline 結束 rm -rf _sandbox/ 一起清）
```

## 5.2 不該做的事

- ✗ 從 sandbox/snapshot/ 內 cp 檔回 production（避免帶入未審 finding）
- ✗ subagent auto-commit（研究預覽期不可信任）
- ✗ master 跳過 cross-check 直接信 audit report（base model 仍會 fabricate finding）
- ✗ user 拍板前直接 patch production（無 audit trail）

## 5.3 master REVIEW 紀律（給 11th master 對話 A）

對話 A 收到 user 帶回的 audit report 後：

1. **完整讀 report**：不跳過 finding；含 ✓ / ⚠ / ✗ 三類分類
2. **cross-check 對 production**：對每個 finding 在 production repo 內 grep / Read verify 是否 fabricated
3. **嚴重度標示**：CRITICAL（影響 LOCKED spec 或 D-NNN 拍板）/ MAJOR（影響 11+ SKILL.md / 模板）/ MINOR（typo / wording）/ INFO（已知 / 已 DEFERRED）
4. **印 finding 採納建議清單**給 user 拍板（不擅自 patch）
5. **user 拍板後執行 Step 6 transcribe**

---

# 6. Boundary 紀律

## 6.1 sandbox 不動 production

- ✓ sandbox/snapshot/ 內檔屬「production 快照副本」；read-only 性質
- ✗ 不從 sandbox/snapshot/ 直接 cp 檔回 production
- ✗ Subagent 不能寫 production 路徑（D:\劇本開發工具\ 但不在 _sandbox/ 內）
- ✗ Subagent 不能跑 git commit / push 到 production origin

## 6.2 subagent 首試 read-only mode

研究預覽期：

- 全 11 audit 任務首試強制 read-only mode（純 audit report 輸出）
- 寫操作（cleanup / fix）走 master 人工 transcribe 回 production 路徑（§5）
- 1000 subagent 同時寫檔 = race condition 災難；研究預覽期不可信任 atomicity

## 6.3 cleanup 紀律

- audit pipeline 結束 → rm -rf _sandbox/ 重 bootstrap baseline
- 避免長期殘留污染（snapshot 過時 + audit-reports 累積）
- 如要保留 audit-reports/ 歷史紀錄 → mv 進 production _design/audit-archives-2026Q2/ + .gitignore unblock 該子目錄（或不入 git tree 由 user 自己備份）

## 6.4 token budget 監控

- Max plan 每月 token 額度（具體額度由 Anthropic 公佈為準）
- 單次 workflow 估 50K-300K token；建議單次上限 500K 避免燒爆
- audit pipeline 整體（3 run 全跑完）估 500K-1M token
- 看 Anthropic dashboard 每日用量 + 月度 cap

## 6.5 audit report 品質受 base model 影響

- Dynamic Workflows 主 agent + 1000 subagent 都是 LLM；fabrication 風險仍在
- audit 結果不是 ground truth；要 master + user 雙人 cross-check
- 對「明顯結構性問題」（如 D-055 編號衝突）信度較高
- 對「設計層判斷」（如某 SKILL.md 是否 dead code）信度較低；需 human-in-the-loop

---

# 7. 並行對話 setup 退場確認

11th master 對話 A reframe 後，原 HANDOFF_11TH_PARALLEL_SETUP v0.1 規劃的三對話並行模式退場：

| 對話 | 原 scope | 退場狀態 |
|---|---|---|
| A Cowork frontend patch | 跑 NEW_REQ_20 6 步驟 | ✗ 退場；改成「寫交接文件 + 後續 REVIEW Claude Code 產出」 |
| B Cowork M4 user-test follow-up | 跑 NEW_REQ_14 §6 AI-assisted 補入 + 紀錄 finding | ✗ 退場（如尚未開）；M4 user-test 屬「為將被替換的 in-tool 寫作 pipeline 做 test」ROI 大降；推延到大重構完成 + 工具新角色定型後再跑 |
| C Codex CLI 量產台詞 | 跑 1-2 場戲 skill chain 量產 | ✗ 退場（如尚未開）；同 B 理由；外接寫作後此量產 path 即將被替換 |

並行協調機制（PARALLEL_SETUP §5）整段廢止。三對話資料夾衝突風險不再存在（因為三對話都不跑）。

新模式：**單對話 A（Cowork）+ user 親跑 Claude Code sandbox audit + master REVIEW 路徑**。

---

# 8. 跟既有 NEW_REQ 關係

| NEW_REQ | 跟本檔關係 |
|---|---|
| NEW_REQ_9 baseline 老債 | sandbox audit B1（NEW_REQ status 巡檢）會涵蓋；B3（51 SKILL.md dead code）可能附帶清掉部分老債 |
| NEW_REQ_11 翻譯工具 fork | 不影響；屬 12+ 輪 master scope；audit 結論不會推進此 NEW_REQ |
| NEW_REQ_14 PHASE_X §6 補入機制 | 退場（M4 user-test 推延）；機制本身保留待未來新 phase 結束時用 |
| NEW_REQ_15 D-054 hybrid trigger | audit A3（大綱/細綱對齊）可能附帶觀察到 trigger 達成證據 |
| NEW_REQ_16 lint script | 暫推延；sandbox audit 結論可能對 lint script spec 提供需求輸入 |
| NEW_REQ_17 / 18 自動化 QA Layer 2/3 | 暫推延；依賴 NEW_REQ_16 |
| NEW_REQ_19 PROCESSED | 不變 |
| NEW_REQ_20 frontend patch | 改標 BLOCKED on NEW_REQ_22 outcome（POST_LOCK_PENDING v0.22）|
| NEW_REQ_21 STYLE_ANCHOR pre-generation 文風錨定機制 | PROCESSING；10th master D-055 拍板已落地（STYLE_ANCHOR_PROPOSAL v0.1 + STYLE_ANCHOR_IMPL_STARTER v0.1 + STYLE_ANCHOR_BATCH_COMPLETION_REPORT v0.X）；sandbox audit C1（D-055 編號衝突）會 cover STYLE_ANCHOR D-055 vs 原 D-054 §6.17.2 預留 D-055 號議題；本檔不動其 entry |
| NEW_REQ_22 工具角色轉換 + audit 路徑 | 本檔即 NEW_REQ_22 落地實體（11th master 對話 A 戰略落地核心 NEW_REQ）|

---

# 9. Cross-ref

- `_design/POST_LOCK_PENDING.md` v0.22（11th master 對話 A 落地；§1 NEW_REQ_22 entry + §5.13 評估 + §5.14 升 v0.22 紀律 + §5.15 §5.3-§5.12 restoration audit trail；NEW_REQ_20 改標 BLOCKED on NEW_REQ_22）
- `_design/HANDOFF_TO_11TH_MASTER.md` v1.1（11th master 對話 A 落地；§9 amendment 紀錄 scope reframe + 新路徑 F Stage 1-6）
- `_design/HANDOFF_11TH_PARALLEL_SETUP.md` v0.2（11th master 對話 A 落地；§0.5 並行模式廢止紀錄）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.1 §10（Milestone 4 真正封版宣告；本檔不動其結論）
- `_design/DECISIONS_LOG.md` v2.1 D-001~D-055 LOCKED（含 10th master D-055 STYLE_ANCHOR pre-generation 文風錨定機制 §6.18；本檔不動其結論；sandbox audit C1 會 cover D-055 編號衝突 audit；audit 結論若觸發新拍板需求 → 升 D-056+ 走人工 transcribe 流程）
- `_design/STYLE_ANCHOR_PROPOSAL.md` v0.1（10th master D-055 拍板 source of truth；sandbox audit C1 + B4 可能 reference 此檔）
- `_design/STYLE_ANCHOR_IMPL_STARTER.md` v0.1（D-055 implementer batch task starter；sandbox audit B2 「CODEX_*_STARTER inventory」可能 cover）
- `_design/STYLE_ANCHOR_BATCH_COMPLETION_REPORT.md`（D-055 batch 落地報告；sandbox audit B2 cover）
- `_design/REQUIREMENTS_LOCK.md` v1.0 FINAL（north star 不動）
- `_sandbox/README.md`（sandbox 根目錄指引；user bootstrap 時自然出現；本檔 §2 詳述路徑）
- `.gitignore`（production root；11th master 對話 A 新建；加 /_sandbox/ 排除）
- 外部 reference：Claude Code Dynamic Workflows 公告（2026-05-28；https://claude.com/blog/introducing-dynamic-workflows-in-claude-code）

---

# 10. 文件維護紀律

- 本檔屬 11th master 對話 A 戰略落地文件；audit pipeline 跑通後依需求 supersede v0.1 → v0.2+
- 11 audit 任務 spec 可依 first-run / second-run / third-run 經驗 inline patch（加 anti-pattern lesson / 改 prompt wording）
- audit 結論回流流程（§5）依實際操作經驗精煉
- audit 全 11 任務跑完 + 結論全 transcribe 完 → 本檔可標 RESOLVED 或 archive

---

**11th master 對話 A 戰略落地完成 → 後續工作流：user bootstrap sandbox → user 親跑 Claude Code Dynamic Workflows → user 帶 audit report 回對話 A → master REVIEW + 人工 transcribe → user commit production → 重複 audit pipeline 直到 11 任務完。**
