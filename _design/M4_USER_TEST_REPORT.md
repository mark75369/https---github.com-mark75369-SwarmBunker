狀態：DRAFT
版本：v1.0（11th master 對話 B M4 user-test follow-up sub-scope 完整 cycle 報告；2026-05-25 ~ 2026-06-01 量產期間 16 user-report → 19 verified finding；對應 POST_LOCK_PENDING v0.25 NEW_REQ_25-43 + PHASE_D §6 補入機制 NEW_REQ_14 sister case；Claude Code workflow Stage 2/3 input candidate）
最後更新：2026-06-01
適用範圍：M4 user-test cycle factual report + Claude Code workflow Stage 2/3 input
優先級：高

# M4_USER_TEST_REPORT — 11th master 對話 B M4 user-test follow-up 完整紀錄

# 0. 文件目的

11th master 對話 B（M4 user-test follow-up sub-scope）於 2026-05-25 ~ 2026-06-01 期間透過 chat-bridge 機制 monitor user 在 Codex CLI 對話 C 跑 Instance repo 量產 chain（`D:\劇本開發\game-script-A`《蟲潮孤堡》塔防遊戲）。

累積 16 user-report，verify 後拆解為 19 distinct finding（F1-F19；含 STYLE_ANCHOR completion report 與 frontend handoff prompt 為 context 不計 finding）。

本檔三用途：

1. **M4 user-test cycle factual record** — 對應 `PHASE_D_COMPLETION_REPORT.md` v1.1 §6 user 親跑 placeholder；屬 NEW_REQ_14 AI-assisted §6 補入機制 candidate（user 後續可拍板「採」/「改後採」/「棄」決定是否 patch PHASE_D §6）
2. **POST_LOCK_PENDING v0.25 NEW_REQ_25-43 entry 詳細 reasoning source** — POST_LOCK entries 的 condensed snapshot；本檔保留完整 verify evidence + user workaround + cross-batch interaction
3. **Claude Code workflow（CLAUDE_CODE_AUDIT_PROTOCOL 3-stage）input candidate** — findings 已由本對話 verify 過；可直接餵 Stage 2 REVIEW（每 finding 對應建議 review prompt）或 Stage 3 APPLY（每 finding 對應 target file scope）跳過 Stage 1 AUDIT

本檔不修改 LOCKED spec / 任何 SKILL.md / template / parser / registry / 00_protocol。所有提議方案屬未來 patch round 範圍。

---

# 1. M4 user-test 背景

## 1.1 cycle 範圍

| 項目 | 內容 |
|---|---|
| 對話 owner | 11th master 對話 B — M4 user-test follow-up sub-scope（原 HANDOFF_11TH_PARALLEL_SETUP §3 三對話 setup 一員；setup 後續廢止但本 sub-scope 持續）|
| 執行期間 | 2026-05-25 ~ 2026-06-01（約 8 天 chat-time；不含 user 量產 wall-time）|
| 量產場域 | `D:\劇本開發\game-script-A`（user 新建 Instance repo；非原 prompt 提到的 `D:\劇本開發工具-test\`）|
| 量產作品 | 《蟲潮孤堡》塔防遊戲（pattern: tower defense + 群像角色 + 主線 + 個人線 12 段）|
| 量產 skill chain 進度 | /init-project → /create-world → /create-character × 4 → /create-relationship × 3 → /create-outline → /create-detailed-outline (pending REVIEW gate)|
| 平行 batch（不在本對話 scope）| (1) STYLE_ANCHOR D-055 implementation batch（W-style entity 新增；2026-05-28 完成）; (2) 11th master 對話 A reframe（工具角色轉換 + Claude Code Dynamic Workflows audit；POST_LOCK_PENDING v0.21 → v0.24）|

## 1.2 finding 蒐集機制（chat-bridge）

依 `_design/HANDOFF_11TH_PARALLEL_SETUP.md` §5 雙對話分工模式：

```
[Codex CLI 對話 C] user 跑 skill 撞 finding
   ↓ (user 切視窗到 Cowork 對話 B)
[本對話 B chat-bridge] user 貼 finding 描述（自然語言）
   ↓
[本對話 B verify] read 對應 spec / SKILL.md / parser source / template
   ↓
[本對話 B 分類] 6 enum：✓ 合理 / deferred placeholder / 🐛 spec drift bug / 🐛 runtime bug / ⚠ design gap / 📝 §6 補入 candidate / 🎯 Canon Delta candidate
   ↓
[本對話 B scratch] 累積到 chat context（v1 → v11 incremental update；未落地磁碟）
   ↓ (本對話 wrap-up trigger)
[本檔 落地]
```

## 1.3 wrap-up trigger

2026-06-01 user 透過 frontend dialogue handoff prompt 觸發 scope discrepancy check；user 拍板選項 (c) Hybrid：M4 wrap up + 接 frontend dialogue（後者拆另一部分）+ 整合 deliverable 給 Claude Code workflow 實作。

本檔屬本對話 wrap-up 第一個 deliverable（第二個 deliverable = POST_LOCK_PENDING v0.25 patch）。

---

# 2. 量產進度快照（2026-06-01）

依 user 從 Codex CLI 切回報的 `/status` 輸出（含 STYLE_ANCHOR completion report 報備內 Codex 跑出的數字）：

| Phase | 實體 | 完成度 | 已套用 workaround |
|---|---|---:|---|
| /init-project | bootstrap | 完成 | （無；F5 active 但不阻量產）|
| /create-world | W-rules / W-language / V | 75% / 75% / 75% | **F6 workaround**：01_b + 02_b 手動 DRAFT → REVIEW（卡 /create-character 前置門檻）|
| /create-character × 4 | C-瑟琳 / 莉娜 / 諾拉 / 清道夫 | 66.7% × 4 | **F7 workaround**：source material `女_1_瑟琳_人設v_0_1.md` 等補 5 欄 header；**F11 workaround**：副對話讀 docx 既有劇本萃取 |
| /create-relationship × 3 | R-清道夫-瑟琳/諾拉/莉娜 | 25% × 3 | **F8 workaround**：清道夫公司建為 R-target 而非 C-target |
| /create-outline | P | 25% | **F16 workaround**：手動建 `05_plot/05_f_關卡原始細節備忘.md` 保全原始細節 |
| /create-detailed-outline | （pending REVIEW gate）| - | **F18 ad-hoc**：開戰前→戰鬥→戰鬥後格式 user 端手動標記 |
| 後續 chain | /scene-task / /dialogue-write / /qa | 未啟動 | 待 detailed-outline 通過 REVIEW gate |

**Baseline 維持**：
- `check_paths.py`: 247 ERROR（hard-limit accept；NEW_REQ_9 既有 debt）
- `check_headers.py`: 0 ERROR / 57 WARN（57 含 F4 trailing whitespace；user 報告含此數字）
- `build_repo_index('.')`: 0 ERROR

**已透過 STYLE_ANCHOR + Codex inline patch 解的旁路**：
- W-style entity（STYLE_ANCHOR D-055）新增；不在本 M4 cycle finding 範圍
- F15 parser 裸 `---` Codex 對 `_user_manual/agents_md_context_budget_update_request.md` inline 移除裸 `---`（user 端 instance workaround；parser 端仍有 line 2892 bug）

---

# 3. 19 Findings 詳細紀錄

每個 finding entry 結構：User 報告精簡 / Verify 結果 / 分類 / 嚴重度 / NEW_REQ slot / D-NNN candidate / User workaround / 跨 finding 關聯 / Claude Code workflow scope。

## 3.1 F1 — `/status` 把 Template skeleton 當實體進度

| 項目 | 內容 |
|---|---|
| User 報告 | 剛初始化後、甚至 `/create-world` 後，`/status` 會看到模板檔 frontmatter 裡既有的 P / W / V entity，導致出現「未追蹤實體」或進度偏高 |
| Verify 結果 | `01_world/01_a_世界觀總覽.md` frontmatter 含 `entities: [W-rules]` + 狀態 REVIEW；`05_plot/05_a_主線大綱模板.md` 含 `entities: [P]` + 狀態 DRAFT；`.claude/skills/status/SKILL.md` Stage 4 Rule 8 規範「frontmatter 內 entity 不在 expected set 即計算 + 標未追蹤」 → fresh Instance bootstrap 後 W-rules 已顯示 75%（REVIEW score map）|
| 分類 | 🐛 spec drift bug（template design vs /status calculation logic 沒對齊）|
| 嚴重度 | 🟠 MAJOR |
| NEW_REQ slot | NEW_REQ_25 |
| D-NNN candidate | 可能合 NEW_REQ_30 一起拍 D-059（template 狀態語意統一）|
| User workaround | 無 user-side workaround；user 透過 F6 workaround 部分覆蓋（手動升 狀態） |
| 跨 finding 關聯 | F6 同根因（template skeleton 狀態語意 ad-hoc）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「對齊 /status SKILL.md Rule 8 跟 template skeleton frontmatter；判斷修哪邊：(a) template 移除 entities (b) /status 加 filename pattern 排除 (c) 加 phase_log evidence 為計算前置條件」；Stage 3 APPLY target files 範圍：`.claude/skills/status/SKILL.md` + `01_world/01_a_*.md` + `05_plot/05_a_*.md` + `03_characters/*.md` + 其他 template skeleton |

## 3.2 F2 — `check_paths.py` 247 baseline error 干擾驗證

| 項目 | 內容 |
|---|---|
| User 報告 | `check_paths.py` 在 fresh Instance 仍有 247 個 baseline error；Phase 5 驗證很難判斷「本輪是否新增錯誤」；user 必須額外跑 diff-only grep |
| Verify 結果 | `scripts/check_paths.py` 是 monolithic CLI；exit code 1 on any ERROR；無 `--changed-only` / `--baseline` / `--suppress-template-debt` flag；247 ERROR 屬 NEW_REQ_9 既有 baseline debt（27 模板 old-style filename reference）|
| 分類 | ⚠ design gap（CLI UX 改進）+ NEW_REQ_9 sister case |
| 嚴重度 | 🟡 MINOR |
| NEW_REQ slot | NEW_REQ_26 |
| D-NNN candidate | 不需 |
| User workaround | user 端跑 diff-only grep（git diff 後 grep 新加 old-style filename）|
| 跨 finding 關聯 | NEW_REQ_9 sister；可合 NEW_REQ_16 lint script 同輪實作 |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 check_paths.py CLI flag：`--changed-only` (git diff base) / `--baseline <file>` (指定 baseline error 數) / `--suppress-template-debt` (排除 NEW_REQ_9 27 模板 old-style refs)；補對應 unit test fixture」；Stage 3 APPLY target files：`scripts/check_paths.py` + `scripts/tests/` |

## 3.3 F3 — `/create-world` SKILL.md split rule vs 01_a 實際 section 對不上（CRITICAL）

| 項目 | 內容 |
|---|---|
| User 報告 | SKILL.md 寫的是覆寫世界觀 §1/§2/§3，但實際模板是大型通用文件沒有足夠乾淨的 project-specific anchor；user 採保守作法新增 `# 0. 本作...基線`避免亂改模板正文 |
| Verify 結果 | `.claude/skills/create-world/SKILL.md` line 268-282 §Split Rules 寫 10.1 世界類型 → 01_a §1 世界類型 (overwrite) / 10.2 世界規則 → 01_a §2 世界規則 / 10.3 科技水平 → 01_a §3 科技水平...；實際 `01_world/01_a_世界觀總覽.md` Grep 出 24 個 section heading 為「§1 文件目的 / §2 與其他文件的關係 / §3 世界觀一句話定義 / §4 作品基本定位 / §5 世界基調 / §6 世界運作規則 / §7 歷史與時間線...§24 最終檢查表」— 完全對不上 |
| 分類 | 🐛 spec drift bug（SKILL.md vs LOCKED template 對不上；user 必須採 workaround） |
| 嚴重度 | 🔴 CRITICAL — 直接影響 Phase B 上游 pipeline；每個 user 必撞 |
| NEW_REQ slot | NEW_REQ_27 |
| D-NNN candidate | **D-056 拍板必開**（修 SKILL.md / 修 LOCKED template / 加 anchor marker 三選一）|
| User workaround | user 採 conservative 新增 `# 0. 本作...基線` section（不動模板正文）|
| 跨 finding 關聯 | F6 同 chain（/create-world 接口問題）；user workaround 結構性 — 不是 ad-hoc |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「3 修法選項分析：(a) 改 SKILL.md split rule 對齊 01_a 24 sections (b) 改 01_a template sections 對齊 SKILL.md (c) 加 `<!-- PROJECT_WORLD_BASELINE_START -->` anchor markers；含 risk / 工時 / D-NNN 拍板邊界；推薦 (a) + 補 anchor」；Stage 3 APPLY 視 user 拍板：(a) `.claude/skills/create-world/SKILL.md` line 263-282 / (b) `01_world/01_a_世界觀總覽.md` (LOCKED-tier；需 D-056) / (c) 兩邊都動 |

## 3.4 F4 — Markdown header 兩空白 hard-break vs `git diff --check` 衝突

| 項目 | 內容 |
|---|---|
| User 報告 | 模板 header 多行尾用兩個空白做 Markdown hard-break；skill 更新「最後更新」就會被 `git diff --check` 報 trailing whitespace |
| Verify 結果 | 既有 `01_a_世界觀總覽.md` header line 3-7 verify 每行尾真有 2 空白；8th/9th master CODEX review 多次 flag 為 R12-MI-01 / R2-INFO-02 INFO/MINOR known issue；POST_LOCK_PENDING line 916/951 已紀錄為 patch hygiene cleanup；CYCLE end /status 仍報 57 warnings |
| 分類 | ⚠ design gap（模板規範 vs git linter workflow tension；缺統一規範）|
| 嚴重度 | 🟡 MINOR — 不阻 runtime；干擾每次 skill 寫檔 commit 累積煩躁度 |
| NEW_REQ slot | NEW_REQ_28 |
| D-NNN candidate | 不需 |
| User workaround | 無；累積到 57 WARN |
| 跨 finding 關聯 | （獨立）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計：(a) 批量 strip 既有檔 header trailing space + 改規範用單行 (b) 寫 lint script 自動 strip header 區 (c) `.gitattributes` 設特定區段允許 trailing；推薦 (a) + 加紀律」；Stage 3 APPLY target files：所有 27 LOCKED template + AGENTS.md + CLAUDE.md header 區 |

## 3.5 F5 — `.protocol_version.template_commit` 直接 fallback TODO

| 項目 | 內容 |
|---|---|
| User 報告 | `/init-project` 已能寫 template source，但沒自動記錄實際 template commit；後續追 bug 時缺來源版本 |
| Verify 結果 | `.claude/skills/init-project/SKILL.md` line 266「If Template commit is unknown, write `template_commit: TODO`」+ `00_protocol/00_i_專案初始化協議.md` line 313 同；SKILL.md 沒明示 detection step「先試 git rev-parse HEAD」 → agent 直接 fallback TODO |
| 分類 | 🐛 spec gap / runtime gap（SKILL.md 缺 detection 流程明示）|
| 嚴重度 | 🟡 MINOR — debug traceability 缺失 |
| NEW_REQ slot | NEW_REQ_29 |
| D-NNN candidate | 不需 |
| User workaround | 無 |
| 跨 finding 關聯 | （獨立）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「補 SKILL.md detection step：(a) 試 `git rev-parse HEAD`（Instance 在 user clone 後自有 .git）(b) 若 success 寫該 hash (c) 若 git 不可用或 .git 缺，fallback TODO + 明示 WARN」；Stage 3 APPLY target files：`.claude/skills/init-project/SKILL.md` line 266 + `00_protocol/00_i_專案初始化協議.md` line 313 |

## 3.6 F6 — `/create-world` Phase 4 沒升狀態；卡 `/create-character` REVIEW 門檻

| 項目 | 內容 |
|---|---|
| User 報告 | /create-world Phase 4 成功寫入後，部分必要分檔仍保留 Template 原本 DRAFT 狀態（01_b DRAFT / 02_b DRAFT），導致 `/create-character` 啟動條件要求 W-rules / V / W-language 至少 REVIEW 時被阻擋；user 手動升 REVIEW 才能進 Stage 1 |
| Verify 結果 | `.claude/skills/create-character/SKILL.md` line 70「W-rules, V, and W-language each exist and are at least REVIEW」；`.claude/skills/create-world/SKILL.md` Phase 4 §Frontmatter Rules（line 286-300）只寫 entities/depends_on/weight；完全沒提 狀態 bump；Template skeleton 起始狀態 ad-hoc 混雜（01_a REVIEW / 01_b DRAFT / 01_c REVIEW / 02_a REVIEW / 02_b DRAFT / 02_c REVIEW）|
| 分類 | 🐛 spec drift bug（Phase 4 缺 狀態 bump step；Template 起始狀態 ad-hoc；下游 prereq 跟上游 output 不對齊）|
| 嚴重度 | 🟠 MAJOR — 每個 user 跑 /create-character 必撞 |
| NEW_REQ slot | NEW_REQ_30 |
| D-NNN candidate | 可合 F1（NEW_REQ_25）一起拍 **D-059**（template 狀態語意統一 + Phase 4 狀態 bump 機制）|
| User workaround | 量產期間已手動：01_b DRAFT → REVIEW / 02_b DRAFT → REVIEW |
| 跨 finding 關聯 | F1 同根因（template skeleton 狀態語意）；連動 patch |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「3 修法選項：(a) /create-world Phase 4 加 狀態 bump step (b) /create-character 允許 `prereq_waived` flag + 寫 phase_log (c) 兩者都做；含 Template skeleton 起始狀態語意統一」；Stage 3 APPLY target files：`.claude/skills/create-world/SKILL.md` Phase 4 + `.claude/skills/create-character/SKILL.md` prereq check + 7 個 W/V template files (01_a~01_c, 02_a~02_c) |

## 3.7 F7 — source/reference 原始素材檔放置規範缺失

| 項目 | 內容 |
|---|---|
| User 報告 | user 把人物完整人設與既有劇本素材放入 `03_characters/`（如 `女_1_瑟琳_人設v_0_1.md` / `05_蟲潮孤島劇本.md.docx`）；.md source 缺 5 欄 header 時被 parser/header/status 流程當正式追蹤文件掃描；/status 或 /create-character Phase 5 可能被非正式 source 檔阻斷；spec 未定義 source material 該放哪 |
| Verify 結果 | /create-character SKILL.md line 22-24 寫檔範圍只列 `main/ minor/ npc/`；完全沒提 source / 原始素材 / reference subdirectory；check_paths.py IGNORE_DIR_NAMES 沒 source/reference 排除；entity_type_registry 03_characters/ target_dir 沒細分 main/minor/npc/source/reference；整個 spec layer 從未定義「user 提供的人物原始設定該放哪」|
| 分類 | ⚠ design gap（cross-layer：parser exclude + SKILL.md 寫檔邊界 + entity_type_registry subdirectory + user_manual + AGENTS.md）|
| 嚴重度 | 🟠 MAJOR — 每個 user 量產撞；user 已寫完整 patch 提案 |
| NEW_REQ slot | NEW_REQ_31 |
| D-NNN candidate | **D-057 拍板候選**（source dir convention：`03_characters/source/` vs 全域 `_source_materials/`；含 header 必填性、parser 排除規則）|
| User workaround | 量產期間補 5 欄 header 給 `女_1_瑟琳_人設v_0_1.md` 等；避免 parser 阻斷；屬 instance-level 不算 Template patch |
| 跨 finding 關聯 | F1 sister case（parser 掃描範圍 vs entity 語意）；F8 cross-cutting（entity registry 邊界）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「3 方案 (A 新建 source 目錄並排除 parser / B source 仍需 header 但 parser 不視為 entity / C 全域 `_source_materials/`)；含跨層影響評估」；Stage 3 APPLY target files：parser scripts/ + 5 個 `/create-*` SKILL.md + `_design/registries/entity_type_registry.yaml` + `_user_manual/skill_invocation_guide.md` + AGENTS.md |

## 3.8 F8 — 非人格反派 / 組織型對抗源 entity 缺型別

| 項目 | 內容 |
|---|---|
| User 報告 | user 原本要跑 `/create-character 反派B`，但反派是已破產清算的公司只有殘留文件不會說話；目前 /create-character 強假設 target 是會說話的 C-* 角色 |
| Verify 結果 | entity_type_registry core 只 9 種（W-rules / W-language / V / C / R / P / CH / S / A）+ reserved（I / UI / SKILL）；無 F / ORG / Faction / Organization；/create-character SKILL.md 沒 non-character refusal logic；01_a §9「勢力與組織」有 placeholder 但屬 W-rules 子段不是獨立 entity |
| 分類 | ⚠ design gap（cross-layer：entity registry 缺 F/ORG type + skill chain 缺 refusal + W-language 缺文件語體擴充）|
| 嚴重度 | 🟠 MAJOR — 任何含公司/制度/殘留組織的作品都撞 |
| NEW_REQ slot | NEW_REQ_32 |
| D-NNN candidate | **D-058 拍板必開**（方向 A 新 F-*/ORG-* entity / 方向 B 擴 W-language 文件語體卡 / 方向 C /create-character refusal 短期）|
| User workaround | user 已停手不寫 C-反派B；後續把「清道夫」公司建為 R-target 而非 C-target（R-清道夫-瑟琳 等 3 個 R）— 屬 ad-hoc workaround |
| 跨 finding 關聯 | F7 sister（entity registry 邊界類）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「3 方向設計 + 工時：A 新 F-*/ORG-* entity (30-50h；涉 entity_type_registry + 11 SKILL.md + parser；推 13+ 輪) / B 擴 W-language 文件語體 (5-8h；屬 W-language extension) / C /create-character Stage 1 加 non-character refusal (1-2h；short-term)；推薦 C 短期 + B 中期」；Stage 3 APPLY target files (方向 C)：`.claude/skills/create-character/SKILL.md` Stage 1 + `00_protocol/00_f_角色創建協議.md` |

## 3.9 F9 — 角色卡缺集中式「個性拆解」固定段

| 項目 | 內容 |
|---|---|
| User 報告 | 角色卡個性資訊分散在「角色本質一句話 / 角色核心心理 / 遮掩方式 / 情緒狀態 / 聲線污染檢查」；user 實際使用覺得不夠明顯；莉娜討論時補出更好用拆解（表層個性/內在個性/自尊來源/情緒遮掩/句子節奏/個性亮點）|
| Verify 結果 | /create-character SKILL.md Stage 4 §Split Rules（line 163-172）8 個 voice card sections 全是「聲線技術規格」（角色定位 / 聲線輪廓 / 去名測試 / 合規檢查 / 髒話來源 / 偏移檢查 / 聲線污染 / 與類型氣質合規）；UD §1.2.2 議題 1-8 全部技術 voice 性質；完全沒「個性拆解」固定欄位 |
| 分類 | ⚠ design gap（spec / SKILL.md / UD 議題 layer 都缺）|
| 嚴重度 | 🟠 MAJOR — user 主動發現需求；其他 user 同樣會撞「角色卡用起來不抓人物」感受 |
| NEW_REQ slot | NEW_REQ_33 |
| D-NNN candidate | 不需 〔**Wave2 升格**：對應 **D-065/D-066**（落地觸及 LOCKED UD §1.2.2 + 00_f 議題清單 + registry，升格為必拍）；見 DECISIONS_LOG §6.19.4/§6.19.5 + POST_LOCK_PENDING NEW_REQ_33（RESOLVED Wave1）〕 |
| User workaround | 量產期間 user 在副對話手動補入「個性拆解」段 |
| 跨 finding 關聯 | F11 + F12 + F13 同 chain（/create-character 品質提升 5-step pipeline）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 voice card 新增固定 § 個性拆解 (表層個性/內在個性/自尊來源/核心恐懼/情緒遮掩/可愛魅力來源/努力與缺陷表現/壓力下變形/角色差異/不可偏移人格模板)；補 00_f 議題 9 + UD §1.2.2 對應 script」；Stage 3 APPLY target files：`.claude/skills/create-character/SKILL.md` Stage 4 §Split Rules + `00_protocol/00_f_角色創建協議.md` + `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §1.2.2 |

## 3.10 F10 — 副對話 / sub-conversation lifecycle UX 規則缺失

| 項目 | 內容 |
|---|---|
| User 報告 | user 放入大量既有人設與 docx 後，主對話需保留 skill 階段推進，不適合塞長素材；副對話讀取效果良好但出現 UX 問題：主 agent 太早關閉副對話 |
| Verify 結果 | ARCH §3.3.0 multi-agent invocation 慣例（D-048）只規範 4 個 agent 環境的 discovery 機制 + invocation 方式；完全沒 sub-conversation lifecycle / 主對話/副對話分工 / 副對話 only-read / 副對話 close 時機規則；grep 整個 repo 沒「副對話」/「次要對話」/「sub-conversation」概念 |
| 分類 | ⚠ design gap（ARCH §3.3.0 multi-agent invocation 慣例維護擴充；屬 cross-cutting agent UX）|
| 嚴重度 | 🟡 MINOR-MAJOR — 不阻 runtime；對量產 UX 影響大 |
| NEW_REQ slot | NEW_REQ_34 |
| D-NNN candidate | 不需 〔**Batch 4 升格**：原判「不需 D-NNN」；因落地在 **LOCKED ARCH** 新增 §3.3.3 子節（動 LOCKED 必拍紀律），升格為必拍，對應 **D-072**；見 DECISIONS_LOG §6.20 + POST_LOCK_PENDING NEW_REQ_34（RESOLVED via D-072，Batch 4）。沿 D-065/D-066 誠實揭露升格先例。〕 |
| User workaround | user 端 ad-hoc 提醒 agent 不要關副對話；屬 chat-level instruction 不是 Template patch |
| 跨 finding 關聯 | F14 同 Meta-pattern D（Agent context / UX layer）；F11 同 chain（副對話是 F11 ingestion 機制）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 ARCH §3.3.3「Sub-conversation / Parallel-chat 慣例」新段：8 條規則（只讀不寫 / 明列讀過檔 / 明列未讀限制 / 只給 evidence summary / 主對話負責 skill stage / 不關閉除 user 明示 / reuse 同副對話 / 主對話 wording 範例）」；Stage 3 APPLY target files：`_design/ARCHITECTURE.md` §3.3 新增 §3.3.3 + `AGENTS.md` + `CLAUDE.md` + `_user_manual/skill_invocation_guide.md` |

## 3.11 F11 — `/create-character` 缺「已寫劇本萃取」input scope（input 層）

| 項目 | 內容 |
|---|---|
| User 報告 | 莉娜角色卡只讀人物設定會得到「暴躁技師」；補讀已寫劇本後才發現更準確的聲線規律（罵人綁定具體技術問題 / 老娘本小姐天才火炮藝術密度需控管 / 可懂火控但不宜搶諾拉定位）|
| Verify 結果 | /create-character SKILL.md inputs（line 291-299）只列「Long-form character material」+「Answers to dynamic issue questions」；完全沒提「previously-written dialogue / docx / 既有劇本」處理；UD §1.2.2 議題 1-8 沒對應議題 |
| 分類 | ⚠ design gap（skill input scope 擴充；屬 input 層）|
| 嚴重度 | 🟠 MAJOR — 直接影響角色卡品質；翻拍/續作必撞 |
| NEW_REQ slot | NEW_REQ_35 |
| D-NNN candidate | 不需（屬 SKILL.md 擴範圍）〔**Wave2 升格**：對應 **D-065/D-066**（落地實際需動 LOCKED UD §1.2.2 append + 00_f §10.13/§10.14 + registry core.00_f_character append，逾 SKILL-only，升格為必拍）；見 DECISIONS_LOG §6.19.4/§6.19.5 + POST_LOCK_PENDING NEW_REQ_35（RESOLVED Wave2）〕 |
| User workaround | 量產期間用副對話讀 docx 既有劇本萃取（F10 機制）|
| 跨 finding 關聯 | F10 提供 ingestion 機制 / F13 是 output 層延伸 / F9 + F12 是其他 output 段；**F11 + F13 必須同輪實作**（input + output 一氣呵成；單做 F11 沒地方落地、單做 F13 沒讀進來無法寫基準）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 SKILL.md Stage 1/2 擴 input scope：既有劇本 / docx / .txt / .csv / .json 接受；speaker alias matching；docx 讀取規範（fallback warning if 環境不支援）；補 00_f 議題 9 對應 script」；Stage 3 APPLY target files：`.claude/skills/create-character/SKILL.md` Stage 1/2/3 + `00_protocol/00_f_角色創建協議.md` + UD §1.2.2 + 副對話 reuse 機制（連動 F10）|

## 3.12 F12 — 聲線卡缺「Source Coverage / Downstream Hooks」固定尾段（output 層）

| 項目 | 內容 |
|---|---|
| User 報告 | 聲線卡可用於聲線 QA 與台詞生成，但 source 檔中大量對 /create-relationship / /create-outline / /scene-task 有價值的資訊未被穩定承接；user 已實測瑟琳 / 莉娜案例驗證 |
| Verify 結果 | /create-character SKILL.md Stage 3 line 136 有「Downstream notes」概念但只在 chat preview 出現，line 324「without granting writes to those files」；Stage 4 §Split Rules（line 163-172）8 個 voice section 完全沒「Source Coverage / Downstream Hooks」固定欄位 → Stage 3 chat 顯示的 downstream notes → Stage 4 寫檔消失 → 下游 skill 拿不到 hooks |
| 分類 | ⚠ design gap（skill output structure；屬 output 層）|
| 嚴重度 | 🟠 MAJOR — user 實測撞到；影響下游 chain pipeline 素材保存；user 拍 priority HIGH |
| NEW_REQ slot | NEW_REQ_36 |
| D-NNN candidate | 不需 〔**Wave2 升格**：對應 **D-065/D-066**（落地觸及 LOCKED UD §1.2.2 + 00_f 議題清單 + registry，升格為必拍）；見 DECISIONS_LOG §6.19.4/§6.19.5 + POST_LOCK_PENDING NEW_REQ_36（RESOLVED Wave1）〕 |
| User workaround | 量產期間 user 副對話手動補入 source coverage 段 |
| 跨 finding 關聯 | F9 + F11 + F13 同 chain（/create-character 5-step pipeline）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 voice card 新增固定 § Source Coverage 含 5 子段：(1) 已吸收進聲線主體的 source 資訊 (2) 交給 /create-relationship 的 hooks (3) 交給 /create-outline / /create-detailed-outline 的 hooks (4) 交給 /scene-task 的 hooks (5) 不應直接當台詞使用的 source 資訊；補 00_f 議題 + UD §1.2.2」；Stage 3 APPLY target files：`.claude/skills/create-character/SKILL.md` Stage 4 §Split Rules + `00_protocol/00_f_角色創建協議.md` + UD §1.2.2 |

## 3.13 F13 — `/create-character` 需主動讀既有台詞 + 聲線卡固定加「既有劇本台詞聲線基準」段（output 層強化）

| 項目 | 內容 |
|---|---|
| User 報告 | 既有劇本台詞是最接近最終玩家體驗的聲線資料；user 拍 priority HIGH；應 speaker alias matching（MainGirlA = 瑟琳 / MainGirlB = 莉娜 / MainGirlC = 諾拉）+ docx 支援 + 8-12 句篩選標準（初登場 / 危機反應 / 任務前準備 / 戰後反應 / 日常互動 / 被肯定被吐槽 / 關係推進 / 中後期成長語氣）|
| Verify 結果 | /create-character SKILL.md line 18 明示「does not create ... dialogue」；line 322 D-050 邊界 08_dialogue_outputs/ 在「不寫」清單但**沒禁讀**；完全沒 speaker alias / 既有劇本讀取 / docx 支援 / Stage 4 §Split Rules 沒「既有劇本台詞聲線基準」 + 「既有劇本聲線使用規則」section |
| 分類 | ⚠ design gap（cross-layer：input 機制 + output structure + alias matching + docx 支援 + 篩選標準）|
| 嚴重度 | 🔴 CRITICAL — user 親口判 priority HIGH；直接影響 /dialogue-write 文筆一致性 |
| NEW_REQ slot | NEW_REQ_37 |
| D-NNN candidate | 不需（屬 SKILL.md 擴 + D-050 邊界明示讀邊界）〔**Wave2 升格**：對應 **D-065/D-066**（落地實際需動 LOCKED UD §1.2.2 append + 00_f §10.13/§10.14 + registry core.00_f_character append，逾 SKILL-only，升格為必拍）；見 DECISIONS_LOG §6.19.4/§6.19.5 + POST_LOCK_PENDING NEW_REQ_37（RESOLVED Wave2）〕 |
| User workaround | 量產期間用副對話讀既有劇本 + 手動補入聲線基準 + 使用規則段 |
| 跨 finding 關聯 | **F11 + F13 必須同輪實作**（input + output 一氣呵成）；連動 STYLE_ANCHOR W-style 機制（W-style = 作品級文風指紋；F13 = 角色級聲線基準；理想架構 F13 voice card 繼承 W-style 文風指紋 + 加 character-specific 聲線特徵）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 SKILL.md 擴：(1) Stage 1 確認既有台詞 + speaker alias (2) Stage 2 讀 08_dialogue_outputs/ + docx + .txt + .csv + .json 不寫 (3) 台詞篩選標準 8-12 句覆蓋 8 場景類型 (4) Stage 4 加 § 既有劇本台詞聲線基準 + § 既有劇本聲線使用規則 (5) cross-ref STYLE_ANCHOR W-style 機制；Stage 3 APPLY target files：`.claude/skills/create-character/SKILL.md` Stage 1/2/3/4 + `00_protocol/00_f_角色創建協議.md` + UD §1.2.2 + 可能 `scripts/parse_frontmatter.py` 加 docx 支援」|

## 3.14 F14 — AGENTS.md / CLAUDE.md 開場 context budget 過大

| 項目 | 內容 |
|---|---|
| User 報告 | AGENTS.md 開場過長 + 完整 skill 清單 / Phase 狀態 / 相關 spec 清單 / 歷史落地狀態；每個新對話一開始就消耗大量 context；user 跑 /create-outline 期間 context 飆 72% |
| Verify 結果 | AGENTS.md 205 行 / CLAUDE.md 137 行 / skill_invocation_guide.md 137 行；AGENTS.md 行 1-104 是核心 hard rules；行 105-205（~100 行）幾乎全是 skill 清單 + invocation 範本 + Phase A/B/C/D skill 表 + QA 模板狀態 + Codex CLI 範本 + Phase 階段對應 — 屬 user 提的「按需讀取」內容 |
| 分類 | ⚠ design gap（root agent instructions context budget；屬 ARCH §3.3.0 multi-agent invocation 慣例維護擴充）|
| 嚴重度 | 🟠 MAJOR — 影響所有 Codex CLI/App skill 對話穩定性；長流程 skill 最受影響 |
| NEW_REQ slot | NEW_REQ_38 |
| D-NNN candidate | 不需 |
| User workaround | 無；累積 context 飆升 |
| 跨 finding 關聯 | F10 同 Meta-pattern D；patch 順序應**F14 最先**（瘦身後其他 patch 對話 context budget 充裕）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「瘦身 AGENTS.md (205 → ~150 行) + CLAUDE.md (137 → ~120 行)；移出 skill 清單 / Phase 狀態到 `_user_manual/skill_registry_full.md` 新建檔；確認 user 第 4 節 minimal list 是否含「台詞品質規則」+「禁止傾向」(line 34-59) — 拍板移到 /dialogue-write + /qa SKILL.md / _user_manual / 仍 root；同步更新 skill 表反映 STYLE_ANCHOR 後 scene-task v0.2 / dialogue-write v0.3」；Stage 3 APPLY target files：`AGENTS.md` + `CLAUDE.md` + 新建 `_user_manual/skill_registry_full.md` + `_user_manual/skill_invocation_guide.md` 對齊 |

## 3.15 F15 — `parse_frontmatter.py` 把裸 `---` 誤判 YAML block 起點

| 項目 | 內容 |
|---|---|
| User 報告 | Codex 自報：`_user_manual/agents_md_context_budget_update_request.md` 第 7 行有單獨 `---`，被 `build_repo_index('.')` 誤判 YAML block 起點但後文非合法 YAML；Codex 已 inline 移除該裸 `---`（user 端 instance workaround）|
| Verify 結果 | `scripts/parse_frontmatter.py` line 2873-2892 `_find_header_adjacent_yaml()`；line 2880-2890 正常路徑「開 `---` + 閉 `---`」對找到 + `_looks_like_frontmatter_yaml` 過濾非 YAML → 安全返回 None；**line 2892 bug**：若只有開 `---` 沒閉 `---`（Markdown HR 邊界）→ parser 把整檔剩下內容當 unclosed YAML block → 下游 `_validate_frontmatter_yaml` 嘗試 YAML parse 失敗報 ERROR |
| 分類 | 🐛 runtime bug（parser edge case；防呆強化）|
| 嚴重度 | 🟡 MINOR — 多數情況 work；user 量產 raw material / proposal doc 內常用 HR 會撞 |
| NEW_REQ slot | NEW_REQ_39 |
| D-NNN candidate | 不需 |
| User workaround | Codex 已 inline 移除該裸 `---`；屬 instance-level 不是 Template parser fix |
| 跨 finding 關聯 | F2 + F4 同 Meta-pattern C（CLI / lint / parser 工具層）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「補 line 2892 unclosed YAML edge case：套用 `_looks_like_frontmatter_yaml` 檢查 + return None if not；加 test fixture for unclosed `---`」；Stage 3 APPLY target files：`scripts/parse_frontmatter.py` line 2892 + `scripts/tests/test_parse_frontmatter.py`（可能新建 fixture）|

## 3.16 F16 — `/create-outline` → `/create-detailed-outline` 中間缺 DRAFT 原始細節保全層

| 項目 | 內容 |
|---|---|
| User 報告 | user 一次提供大量有效關卡大綱資訊，正式 `05_a` 為維持主線骨架簡潔壓縮細節；後續對話只讀 `05_a` 可能丟失原始關卡動機 / 支線鉤子 / 黑色幽默 / 玩法條件 / 戰鬥前後資訊 |
| Verify 結果 | /create-outline + /create-detailed-outline + UD 完全沒「原始細節 / 保全 / DRAFT preservation layer」concept；user 已 ad-hoc 用 `05_plot/05_f_關卡原始細節備忘.md` workaround（DRAFT / entities: [] / depends_on: [P] / 不更新 .protocol_version / 不建 CH-*/S-*）|
| 分類 | ⚠ design gap（新 workflow concept；屬 /create-outline → /create-detailed-outline 間 layer 擴充）|
| 嚴重度 | 🟠 MAJOR — user 已實作 workaround；通用對所有長篇作品都有價值 |
| NEW_REQ slot | NEW_REQ_40 |
| D-NNN candidate | 可能涉新 `00_protocol/00_m_保全層協議.md`（待 user 拍板）|
| User workaround | 量產期間建 `05_plot/05_f_關卡原始細節備忘.md` |
| 跨 finding 關聯 | F17 + F18 + F19 同 Meta-pattern E（Outline 層品質提升 chain）|
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 DRAFT 保全層 convention（從 user `05_f` workaround 抽象）：(a) 檔名 pattern `<目錄>/<\d+_x>_原始細節備忘.md` (b) frontmatter 規則 (狀態 DRAFT / entities: [] / depends_on 指上游 / 不登錄 .protocol_version / 不建 CH-*/S-*) (c) /create-outline + /create-detailed-outline SKILL.md 提及「該 layer 為資料源」(d) 可能新建 `00_protocol/00_m_保全層協議.md`」；Stage 3 APPLY target files：`.claude/skills/create-outline/SKILL.md` + `.claude/skills/create-detailed-outline/SKILL.md` + UD §1.3 + 可能新建 protocol |

## 3.17 F17 — `/create-outline` 寫作 UX 缺「遊戲設計語言」/「關卡功能 table」結構化輸出

| 項目 | 內容 |
|---|---|
| User 報告 | user 希望大綱討論不要一開始就過度深入文學化分析；應優先用遊戲設計 / 關卡功能語言整理（這關玩家要知道什麼 / 取得什麼 / 後續鉤子 / 禁止提前揭露）+ table 格式（關卡 / 開戰前功能 / 戰鬥功能 / 戰鬥後功能 / 玩家新增資訊 / 後續鉤子 / 禁止提前）|
| Verify 結果 | SKILL.md 完全沒「遊戲設計 / 關卡功能 / 玩家 X 取得 Y / 開戰前後鉤子」table 格式；沒「優先用遊戲設計語言整理」UX wording |
| 分類 | ⚠ design gap（UX wording + 結構化輸出格式缺；屬 genre-specific 可選 mode）|
| 嚴重度 | 🟡 MINOR-MAJOR — 影響 UX 流暢度；遊戲類作品需要；非遊戲類不需 |
| NEW_REQ slot | NEW_REQ_41 |
| D-NNN candidate | **D-060 拍板候選**（pattern pack 機制：依 00_b §1 作品類型自動載入可選 mode）|
| User workaround | 量產期間 user 端主動引導 agent 用遊戲設計語言；ad-hoc |
| 跨 finding 關聯 | F18 同 pattern pack（合併實作可省 overlap）；F16 + F19 同 Meta-pattern E |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計 pattern pack 機制：(a) 依 00_b §1 作品類型載入；(b) `tower_defense` pack 含遊戲設計 table 格式（關卡 / 開戰前功能 / 戰鬥功能 / 戰鬥後功能 / 玩家新增資訊 / 後續鉤子 / 禁止提前）；(c) `visual_novel` pack 預留；含 pack registry 規範」；Stage 3 APPLY target files：`.claude/skills/create-outline/SKILL.md` Stage 1/2 + 可能新建 `_design/registries/pattern_pack_registry.yaml` + `_user_manual/skill_invocation_guide.md` |

## 3.18 F18 — `/create-detailed-outline` 缺「開戰前→戰鬥→戰鬥後」場景結構支援

| 項目 | 內容 |
|---|---|
| User 報告 | 本作每關只有兩個劇情場（開戰前 / 戰鬥後）；戰鬥是玩法段非劇情台詞場景；戰鬥中短句 / UI / 戰鬥語音作獨立需求；/create-detailed-outline 不該把戰鬥本身誤建成完整台詞場景 |
| Verify 結果 | SKILL.md 沒「劇情場 vs 戰鬥場」場景類型 enum；沒「開戰前 / 戰鬥後」格式支援；場景結構假設通用單一場景；可能誤建戰鬥本身為 S-*（含完整 dialogue）|
| 分類 | ⚠ design gap（genre-specific 結構支援缺）|
| 嚴重度 | 🟡 MINOR-MAJOR — 戰鬥型作品需要；視覺小說不需 |
| NEW_REQ slot | NEW_REQ_42 |
| D-NNN candidate | 合 F17 一起拍 **D-060**（pattern pack 機制）|
| User workaround | 量產期間 user 端手動標記場景類型 |
| 跨 finding 關聯 | F17 同 pattern pack；F16 + F19 同 Meta-pattern E |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「擴 SKILL.md：(a) 場景類型 enum 加 `劇情場` / `戰鬥前場` / `戰鬥場` / `戰鬥後場` / `UI/語音場`；(b) `tower_defense` pattern pack 含「每關 = 戰鬥前場 + 戰鬥場(skip dialogue) + 戰鬥後場」；(c) `arpg` pack 預留；(d) 戰鬥場不自動進 /dialogue-write」；Stage 3 APPLY target files：`.claude/skills/create-detailed-outline/SKILL.md` + UD §1.4 + 連動 pattern_pack_registry.yaml |

## 3.19 F19 — `/create-outline` / `/create-detailed-outline` 缺「個人劇情 vs 主線邊界」check

| 項目 | 內容 |
|---|---|
| User 報告 | 主線 Lv10-Lv26 可使用女角功能但不應消耗女角後續個人劇情高潮；女角 12 段角色劇情（1-3 出場/介紹/第一次成人；後續 9 段獨立）；主線支線可塑造世界觀人物設定但不能自動把女角個人線寫完 |
| Verify 結果 | SKILL.md 沒「個人線消耗保護」/「個人線高潮邊界」/「12 段個人線結構」check |
| 分類 | ⚠ design gap（內容邊界規則缺；通用 footgun）|
| 嚴重度 | 🟠 MAJOR — 任何群像作品撞；user 親身發現需求 |
| NEW_REQ slot | NEW_REQ_43 |
| D-NNN candidate | **D-061 拍板候選**（個人線邊界規則）|
| User workaround | 量產期間 user 端 ad-hoc 邊界檢查；無正式 patch |
| 跨 finding 關聯 | F16 + F17 + F18 同 Meta-pattern E |
| Claude Code workflow scope | Stage 2 REVIEW prompt：「設計個人線邊界規則：(a) UD §1.3.X 加新議題「主線可使用角色功能但不消耗個人線高潮」；(b) /create-outline Stage 3 預告稿加 check：每章節列出「使用了哪些角色 / 是否消耗個人線」；(c) /create-detailed-outline 同 check；(d) 12 段個人線結構紀錄 convention」；Stage 3 APPLY target files：`.claude/skills/create-outline/SKILL.md` Stage 3 + `.claude/skills/create-detailed-outline/SKILL.md` + UD §1.3 |

---

# 4. 5 大 Meta-pattern 分析

## 4.1 Meta-pattern A — Phase A→B chain coherence（6/19）

**涉及 finding**：F1, F3, F5, F6, F7, F8

**共同根因**：/init-project → /create-world → /create-character 上游接口設計不完整；spec 寫的 split rule / target dir / 狀態 / target type 跟實際 LOCKED template / user 真實使用案例對不齊。

**Pattern 特徵**：
- 全部集中在 Phase A→B 上游 chain
- 5/6 user 已採 workaround（F3 加 § 0 / F6 手動升 REVIEW / F7 補 header / F8 改 R-target）
- 修哪邊（SKILL.md / template / parser / registry）涉跨 layer 拍板（D-056 / D-057 / D-058 / D-059）

**處理建議**：屬「結構性 chain coherence patch round」main task；不是逐個 finding 散修；應一次性對齊 SKILL.md + LOCKED template + entity_type_registry 邊界。

## 4.2 Meta-pattern B — `/create-character` 品質提升 5-step pipeline（5/19）

**涉及 finding**：F9, F10, F11, F12, F13

**Pipeline**：
- **Ingestion 機制** — F10 副對話 UX lifecycle（提供大量 raw material 讀取機制；主對話保留 skill 推進）
- **Input 端** — F11 已寫劇本萃取 input scope（Stage 1/2 接受 existing dialogue / docx）
- **Input 端強化** — F13 既有台詞 + speaker alias + docx 支援 + 篩選標準（required-when-exists）
- **Output 端 1** — F9 個性拆解段（Stage 4 voice card 加固定 § 個性拆解）
- **Output 端 2** — F12 Source Coverage / Downstream Hooks（Stage 4 voice card 加固定 § Source Coverage 5 子段）
- **Output 端 3** — F13 既有劇本聲線基準段（Stage 4 voice card 加固定 § 既有劇本台詞聲線基準 + § 既有劇本聲線使用規則）

**處理建議**：屬「/create-character 品質提升 chain main task」；F11 + F13 input/output 必須同輪實作；F9 + F12 可獨立但建議合併同輪做（同 SKILL.md / 00_f / UD patch）；F10 屬 ARCH §3.3.3 擴充可獨立做但跟 F11/F13 連動。

**連動 STYLE_ANCHOR W-style**：W-style = 作品級文風指紋；F13 = 角色級聲線基準；理想架構 F13 voice card 繼承 W-style 文風指紋 + 加 character-specific 聲線特徵。

## 4.3 Meta-pattern C — CLI / lint / parser 工具層改進（3/19）

**涉及 finding**：F2, F4, F15

**共同根因**：scripts/ 層工具友善度 + 防呆強化；不涉 LOCKED spec。

**處理建議**：
- F15 是 quick-fix（1.5-2h；line 2892 補一行檢查）
- F2 屬 quick-win（5-8h；加 CLI flag + tests）
- F4 屬 cleanup batch（4-7h；批量 strip + 規範 update）
- 三者可同輪做或併入 NEW_REQ_16 lint script spec 規劃；屬「Wave-A1 quick-win」候選

## 4.4 Meta-pattern D — Agent context / UX layer（2/19）

**涉及 finding**：F10（副對話 lifecycle）+ F14（root context bloat）

**共同根因**：ARCH §3.3.0 multi-agent invocation 慣例（D-048）落地後續擴充未跟進。

**處理建議**：F14 應**第一個處理**（瘦身 root → 後續 patch 對話 context budget 充裕）；F10 可隨後做；兩者合併同輪實作可省 overlap（同 ARCH §3.3 patch）。

## 4.5 Meta-pattern E — Outline 層品質提升 chain（4/19）

**涉及 finding**：F16, F17, F18, F19

**共同根因**：/create-outline + /create-detailed-outline 兩個 skill 在實際量產撞到的 UX gap；分通用 vs genre-specific。

**通用層**：
- F16 原始細節保全層（所有長篇作品都有價值；user 已 workaround）
- F19 個人線 vs 主線邊界（所有群像作品撞）

**Genre-specific 層**：
- F17 遊戲設計語言 UX（遊戲類作品需要）
- F18 開戰前→戰鬥→戰鬥後格式（戰鬥型作品需要）
- 兩者應設計為「依 00_b §1 作品類型自動載入 pattern pack」可選 mode（D-060 拍板）

**處理建議**：F16 + F19 屬通用優先；F17 + F18 屬 pattern pack 機制需 D-060 拍板（屬中工時）。

## 4.6 Meta-pattern 之間互動

| 互動 | 描述 |
|---|---|
| Meta-A vs Meta-B | F6（/create-world 狀態 bump）影響 /create-character 啟動條件；Meta-A 是 Meta-B 的前置條件 |
| Meta-B vs STYLE_ANCHOR | F13 既有劇本聲線基準 ↔ W-style 文風指紋；分層互補 |
| Meta-D vs 後續所有 patch | F14 瘦身應**最先**；其他 patch 對話受惠 |
| Meta-E genre-specific | F17 / F18 pattern pack 機制可能影響未來 NEW_REQ_11 工具 B 翻譯工具 fork 設計（翻譯工具可能 reuse pattern pack）|

---

# 5. 推薦處理 Wave + 工時 estimate

## 5.1 Wave 分組（按 ROI / 風險 / 依賴）

| Wave | Finding | 工時範圍 | 風險 | 觸發條件 |
|---|---|---|---|---|
| **Wave-A1** quick-wins 低風險先做 | F14 + F15 + F5 + F6 + F9 + F12 + F4 + F16 + F19 (9 個) | 25-44h | 🟢 LOW | 立即可啟動；不需 D-NNN |
| **Wave-A2** D-NNN dependent | F3（D-056）+ F7（D-057）+ F1+F6 整合（D-059）| 18-27h | 🟡 MED | 需 user 拍板 D-NNN 修哪邊 |
| **Wave-A3** Cross-layer / 中工時 | F11+F13 合併（D-050 邊界明示）+ F10 + F17+F18 pattern pack（D-060）+ F19 邊界 check（D-061）| 23-39h | 🟡 MED | F11+F13 必須同輪；F17+F18 需 pattern pack 機制拍板 |
| **Wave-A4** F8 短中期 | F8 方向 C（refusal）+ 方向 B（W-language 文件語體擴）| 5-10h | 🟡 MED | 需 D-058 拍板 |
| **Wave-A5（可選）** F8 long-term | F8 方向 A（新 F-*/ORG-* entity）| +30-50h | 🔴 HIGH | 跨 entity_type_registry + 11 SKILL.md；推 13+ 輪 |
| **Wave-A6（可選）** F2 併 NEW_REQ_16 lint script | F2 + NEW_REQ_16 spec 規劃 | 6-10h | 🟢 LOW | 屬封版後維護期 |

## 5.2 4 種 scope option

| Option | 內容 | 工時 |
|---|---|---|
| **α — 純紀錄推 12+ 輪** | 本檔 + POST_LOCK_PENDING v0.25 patch；後續完全推 12+ 輪 master | **3.5-5h**（本對話 wrap-up）|
| **β — Wave-A1 quick-win**（推薦）| α + Wave-A1（9 個 quick-medium-win） | +25-44h |
| **γ — 完整短中期（不含 F8 long-term）** | α + Wave-A1 + A2 + A3 + A4 | +71-120h（共 ~75-125h）|
| **δ — 全範圍含 F8 long-term** | γ + Wave-A5 | +30-50h（共 ~105-175h）|

**推薦：β** — F14 + F15 + F5 + F9 + F12 + F4 + F16 + F19 全屬高 ROI 低風險快 win；F6 屬 user 已 workaround 但 spec patch 後其他 user 受惠。

## 5.3 Wall-time 預估

| 節奏 | 短中期（含 γ）| 含 F8 long-term |
|---|---|---|
| 密集模式 | 3-4 月 | 6-8 月 |
| 均衡模式 | 8-12 月 | 15-22 月 |
| 慢節奏 | 12-18 月 | 14+ 輪推遲 |

---

# 6. Claude Code Workflow 餵入點

每 finding 在 §3 紀錄結尾的「Claude Code workflow scope」段已含對應 Stage 2 REVIEW prompt + Stage 3 APPLY target files。本節提供整體餵入策略。

## 6.1 整體建議

依 CLAUDE_CODE_AUDIT_PROTOCOL.md：
- **跳過 Stage 1 AUDIT** — 本對話已完成 verify；findings 屬「user-test direct observation + master verification」性質
- **Stage 2 REVIEW** — 把本檔 §3 19 entries 拆成 N 個 review task（建議按 Meta-pattern 分組：A/B/C/D/E 5 個 batch）
- **Stage 3 APPLY** — 依 user 拍板 Wave 順序（建議 β 路線）

## 6.2 Stage 2 REVIEW 分組建議

| Batch | Finding | Review prompt 重點 |
|---|---|---|
| Batch B1 | F14 + F15 + F4（quick-fix 工具層 + Meta-D 第一步）| 純 mechanical fix；無設計層議題；建議直接合 Stage 3 |
| Batch B2 | F5 + F9 + F12 + F11 + F13（Meta-pattern B + 部分 A）| /create-character / 00_f / UD 同檔多 patch；建議 same SKILL.md 一輪到位 |
| Batch B3 | F16 + F19（Meta-pattern E 通用層）| /create-outline + /create-detailed-outline + UD 同檔；建議 same review batch |
| Batch B4 | F6 + F1（Meta-pattern A 部分 + template 狀態語意）| 需 D-059 拍板（template skeleton 起始狀態 + Phase 4 狀態 bump）|
| Batch B5 | F10（副對話 lifecycle）| 純 ARCH 擴；獨立 review |
| Batch B6 | F2 + NEW_REQ_16 | Quick-win + lint script 整合；獨立或合 NEW_REQ_16 |
| Batch B7 | F3 + F7 + F8 短中期（D-056 / D-057 / D-058）| 需多 D-NNN 拍板；user 諮詢 Cowork master 模式適用 |
| Batch B8 | F17 + F18 pattern pack（D-060）| 需 D-060 拍板 pattern pack 機制 |
| Batch B9（可選）| F8 long-term（方向 A 新 entity）| 涉跨 11 SKILL.md；屬 13+ 輪 scope |

## 6.3 Stage 3 APPLY 邊界提醒

依 CLAUDE_CODE_AUDIT_PROTOCOL.md §3-§5 紀律：
- ✓ APPLY 寫入 production（`D:\劇本開發工具\`）但**不**寫 `_sandbox/`
- ✓ Double gating（user 拍板才 apply；apply 後 user 跑 commit + push）
- ✓ apply-reports/APPLY_<ts>.md 含 audit trail
- ✗ 不動 LOCKED spec（D-001~D-055）除非新 D-056+ 拍板
- ✗ 不動 _tools/frontend/（屬 frontend dialogue scope；F1-F19 都不涉）
- ✗ 不動 D-050 邊界（F13 讀 08_dialogue_outputs/ 屬讀不是寫；不違反 D-050）

---

# 7. 跨 batch 互動紀錄

## 7.1 STYLE_ANCHOR D-055 batch（2026-05-28）

- **新 W-style entity** + `01_world/01_d_文風樣本與指紋.md` + scene-task v0.2 / dialogue-write v0.3
- **0 個本檔 finding 跟 STYLE_ANCHOR 重複**（STYLE_ANCHOR scope 在 /scene-task + /dialogue-write 前處理；本檔 scope 在 /create-* skill chain）
- **F13 應 cross-ref W-style 機制**（W-style = 作品級文風指紋；F13 = 角色級聲線基準；F13 patch 時 voice card 結構應繼承 W-style）

## 7.2 11th master 對話 A reframe（POST_LOCK v0.21 → v0.24）

- **NEW_REQ_22**（工具角色轉換 + Claude Code Dynamic Workflows audit 路徑）落地
- **本檔屬 reframe 後 Claude Code workflow Stage 2/3 input**（直接受惠於 reframe）
- **F14 patch 落地後跟對話 A reframe 後 frontend handoff 機制協調**：F14 patch 應更新 AGENTS.md 反映 scene-task v0.2 / dialogue-write v0.3（STYLE_ANCHOR 後）+ 反映 reframe 後 frontend 改 frontend dialogue 接手
- **NEW_REQ_20 dashboard + NEW_REQ_24 角色檔名**：屬 frontend dialogue scope；不在本檔範圍

## 7.3 跟 frontend dialogue 邊界

- frontend dialogue 拿到 user pasted FRONTEND_HANDOFF.md prompt（已在另一個 Cowork chat 啟動）
- F1-F19 全 0 個 frontend finding；自然切乾淨
- 若未來 frontend dialogue 跑 audit cycle 撞到任何 finding，由 frontend dialogue 開 NEW_REQ_44+；不在本檔 numbering 範圍

## 7.4 跟 PHASE_D §6 補入機制（NEW_REQ_14）

- 本檔 §1-§3 含 user 親跑 M4 chain 事實摘要 + 議題處理 + Phase 啟動條件對應（pre-/create-detailed-outline 階段）
- 可作為 NEW_REQ_14 AI-assisted §6 補入機制的 reconstruct 草稿來源
- User 後續可拍板「採」/「改後採」/「棄」決定是否 patch `PHASE_D_COMPLETION_REPORT.md` §6 placeholder
- 本檔不主動 patch PHASE_D §6（屬 user 拍板後續 step）

---

# 8. Cross-ref

## 8.1 對應 POST_LOCK_PENDING v0.25 entries

| Finding | NEW_REQ entry |
|---|---|
| F1 | NEW_REQ_25 |
| F2 | NEW_REQ_26 |
| F3 | NEW_REQ_27 |
| F4 | NEW_REQ_28 |
| F5 | NEW_REQ_29 |
| F6 | NEW_REQ_30 |
| F7 | NEW_REQ_31 |
| F8 | NEW_REQ_32 |
| F9 | NEW_REQ_33 |
| F10 | NEW_REQ_34 |
| F11 | NEW_REQ_35 |
| F12 | NEW_REQ_36 |
| F13 | NEW_REQ_37 |
| F14 | NEW_REQ_38 |
| F15 | NEW_REQ_39 |
| F16 | NEW_REQ_40 |
| F17 | NEW_REQ_41 |
| F18 | NEW_REQ_42 |
| F19 | NEW_REQ_43 |

## 8.2 對應 D-NNN candidate

| D-NNN | Finding | 用途 |
|---|---|---|
| D-056 | F3 | /create-world split rule 修哪邊（SKILL.md / template / anchor）|
| D-057 | F7 | source/reference dir convention |
| D-058 | F8 | 非人格反派 entity 方向 A/B/C |
| D-059 | F1 + F6 | template skeleton 起始狀態語意 + Phase 4 狀態 bump |
| D-060 | F17 + F18 | pattern pack 機制（依 00_b §1 作品類型載入 mode）|
| D-061 | F19 | 個人線邊界規則 |

## 8.3 相關文件

- `_design/POST_LOCK_PENDING.md` v0.25（含 NEW_REQ_25-43 entries + §5.20 + §5.21 評估紀錄）
- `_design/PHASE_D_COMPLETION_REPORT.md` v1.1 §6（user 親跑 placeholder；本檔屬 §6 補入 candidate via NEW_REQ_14 機制）
- `_design/HANDOFF_TO_11TH_MASTER.md` v1.1 §9 amendment（11th master scope reframe；本檔 sub-scope 屬 reframe 前 setup 持續 wrap-up）
- `_design/HANDOFF_11TH_PARALLEL_SETUP.md` §3（本對話 B M4 follow-up sub-scope 規範）
- `_design/STYLE_ANCHOR_BATCH_COMPLETION_REPORT.md` v1.0（STYLE_ANCHOR D-055 batch；2026-05-28 完成）
- `_design/AUDIT_2026Q2_REPORT.md` v0.1（11th master 對話 A first+second cycle 紀錄；本檔屬 Cycle N+1 input candidate）
- `_sandbox/CLAUDE_CODE_AUDIT_PROTOCOL.md` v0.1（3-stage workflow；本檔 §6 對齊 Stage 2/3 餵入）
- `_design/SANDBOX_REFACTOR_PLAN.md` v0.1（sandbox audit 戰略落地核心檔）
- `_design/DECISIONS_LOG.md` v2.1（D-001~D-055；新 D-056+ 拍板候選見 §8.2）
- `_design/REQUIREMENTS_LOCK.md` v1.0 FINAL（不動）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5（多 finding 涉 UD §1.2.2 / §1.3 / §1.4 擴充）
- `_design/ARCHITECTURE.md` v1.6 §3.3.0（multi-agent invocation；F10 + F14 落地依據）
- `_design/CANON_DELTA_FRAMEWORK.md` v0.1（成熟期功能；本檔不涉但 F11/F12/F13 outputs 可能影響未來 canon delta extraction）
- `.claude/skills/init-project/SKILL.md` v0.3+（F5 patch 對象）
- `.claude/skills/create-world/SKILL.md` v0.1（F3 + F6 patch 對象；含 D-053 exception）
- `.claude/skills/create-character/SKILL.md` v0.4（F8 + F9 + F11 + F12 + F13 patch 對象）
- `.claude/skills/create-outline/SKILL.md` v0.3（F16 + F17 + F19 patch 對象）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.3（F16 + F18 + F19 patch 對象）
- `.claude/skills/status/SKILL.md` v0.1（F1 patch 對象）
- `00_protocol/00_f_角色創建協議.md`（F9 + F11 + F12 + F13 patch 對象）
- `00_protocol/00_i_專案初始化協議.md`（F5 patch 對象）
- 未來新建：`00_protocol/00_m_保全層協議.md`（F16 candidate；待 D-NNN 拍板）
- 未來新建：`_user_manual/skill_registry_full.md`（F14 candidate）
- 未來新建：`_design/registries/pattern_pack_registry.yaml`（F17 + F18 D-060 拍板後）
- `scripts/parse_frontmatter.py`（F15 patch 對象 line 2892）
- `scripts/check_paths.py`（F2 patch 對象）
- `AGENTS.md`（F14 主要 patch 對象）
- `CLAUDE.md`（F14 同步 patch 對象）

---

# 9. 維護紀律

本檔屬 11th master 對話 B M4 user-test follow-up sub-scope 完整 cycle 落地紀錄。屬「factual snapshot」性質：
- ✗ 不再追加新 finding（後續 user-test cycle 應寫獨立 M4_USER_TEST_REPORT_v2.md 等）
- ✓ 可標 partial supersede 若有 finding 後續 RESOLVED via patch
- ✓ 跟 POST_LOCK_PENDING NEW_REQ_25-43 entries 同步維護（任一 RESOLVED 時兩邊都標）
- ✓ Claude Code workflow 後續 cycle 跑完後可在本檔加 §10「Patch Round Audit Trail」紀錄哪些 finding 已 RESOLVED via 哪個 cycle
