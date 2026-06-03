狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：Phase D Wave 16 task — Phase D 整體驗收 + 撰寫 _design/PHASE_D_COMPLETION_REPORT.md v1.0；Milestone 4 接近條件聲明（非達成）  
優先級：高

# CODEX_D_FINAL_STARTER — Phase D Wave 16：Phase D 整體驗收

# 0. 本檔用途

Phase D Wave 16 task — Phase D 整體驗收 + 撰寫 `_design/PHASE_D_COMPLETION_REPORT.md` v1.0。對齊 TASKS v1.9 §C.7（Phase D 整體驗收 — 註：master 詞彙的「Phase D」 = TASKS 詞彙的「Phase C」；視圖 + 迭代 + 匯出 + 整合 phase）+ PHASE_C_COMPLETION_REPORT v1.0 pattern + PHASE_B_COMPLETION_REPORT v1.4 對照。

**前置條件：** 9th master 第二段對話 Wave 14（4 個 /export-* + 4 wrapper）+ Wave 15（/diagnose + /integrate + 2 wrapper）已落地；Wave 13（4 個 /view-* + 4 wrapper）9th master 第一段已落地；Wave 12 starter 已落地（5 個 /iterate-* + /iterate-scene --split-to-file；**6 個 SKILL.md 尚未實作 — 屬 deferred state**）+ Canon Delta framework 已寫入（屬 framework reference 不實作 skill）。

**Wave 16 性質：** Milestone 4 接近條件最後守門關卡 — 動用完整 CODEX 4 維度重審 + 撰寫 PHASE_D_COMPLETION_REPORT。9th master 第二段對話 Wave 14/15 採 master 端內部 verify；Wave 16 不同 — 動用完整 CODEX review starter（屬最終 milestone；對齊 9th master 第一段 5 條教訓內化）。

**重要紀律提醒：**

1. **master 詞彙 vs TASKS 詞彙錯位** — master「Phase D」（視圖+迭代+匯出+整合 = 9th master scope）= TASKS「Phase C」（C.1~C.7）。本 starter 用 master 詞彙；TASKS reference 用 §C.x。
2. **Milestone 4 紀律（嚴守 wording）** — Phase D 完成 **≠** Milestone 4 達成；差在 Phase A.0F 前端工具補完（屬 10th master scope）。本 Wave PHASE_D_COMPLETION_REPORT 宣告「**Milestone 4 接近條件達成**」（非達成）。
3. **Wave 12 SKILL.md 尚未實作** — 9th master 第一段對話只寫 starter；6 個 SKILL.md（5 /iterate-* + /iterate-scene --split-to-file）尚未由 CODEX D.1-D.5 task 實作。Phase D 整體驗收必須明示這個 partial 狀態 + 推 10th master 或更晚輪 scope。

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`
- Instance-only path 前綴 `<instance_root>/`
- **新紀律（9th master 第二段對話內化）：** 寫長 multi-byte 檔請用 Python script via bash；不用 Write/Edit tool（避截斷風險；Cowork tool 對長中文檔有截斷風險）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer + verifier agent。

本輪是「Phase D Wave 16 task」— Phase D 整體驗收 + 撰寫 _design/PHASE_D_COMPLETION_REPORT.md v1.0，對齊 TASKS v1.9 §C.7（Phase D 整體驗收）+ PHASE_C_COMPLETION_REPORT v1.0 pattern + PHASE_B_COMPLETION_REPORT v1.4 對照。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**Token 不是限制** — 如有需要你可以 spawn 多個次要 CODEX 對話做使用增加品質和效率。例如：可以開子對話分別 verify Wave 12 / 13 / 14 / 15 各自 落地狀態 / 跑 baseline / grep frontmatter 對齊 SPEC §5.2 / 對照 D-054 hybrid fallback 各 skill 實作一致性，再回主對話彙整撰寫 report。優先選擇能提升品質的工作切分。

**你的身份與職責：**

- 你是 implementer + verifier — 本輪跑 Phase D 4 個 Wave 落地驗證 + Canon Delta framework 驗證 + L3 schema 對齊備忘驗證 + 撰寫 Phase D 完成報告
- 對應傳統：Wave 16 最終 task；Wave 16 PASS → Phase D 收尾 + Milestone 4 **接近條件達成（非達成）** + 開放 Phase A.0F 平行對話結束後的 10th master 接手封版
- 注意 master vs TASKS 詞彙錯位：master「Phase D」（視圖+迭代+匯出+整合 = 9th master scope）= TASKS「Phase C」（C.1~C.7）。本 starter 用 master 詞彙；TASKS reference 用 §C.x。

**重要邊界（嚴格 scope）：**

- ✗ 不改任何 LOCKED spec / registry / parser code
- ✗ 不改既有 27 模板 / 00_protocol/ 任何檔（含 9th master 第一段對話 Round 1-4 已升 v0.2 的 protocol）
- ✗ 不改 .claude/skills/*/SKILL.md 任何檔（含 Wave 13 view-* + Wave 14 export-* + Wave 15 diagnose/integrate + 中文 wrapper）
- ✗ 不改既有 Phase A / Phase B / Phase C SKILL.md
- ✗ 不改 D-001~D-054 拍板（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.18 / D054_DECISION_PACKAGE v0.2 / CANON_DELTA_FRAMEWORK v0.1）
- ✗ 不修補 check_paths baseline（屬 NEW_REQ_9 / NEW_REQ_19 範圍；推 10th master）
- ✗ 不跑真實 /iterate-* / /view-* / /export-* / /diagnose / /integrate 寫檔（會污染 Template 或產生 view/ export/ 檔；端到端測試屬 user 親跑 M4）
- ✗ 不升任何檔狀態
- ✗ 不寫 Phase A.0F 任何檔（屬 Phase A.0F 平行對話 scope + 10th master scope）
- ✗ 不擅自實作 Wave 12 缺漏的 6 個 SKILL.md（屬 10th master 或更晚輪 scope；本 Wave 只 verify Wave 12 starter 落地不檢查 SKILL.md 存在）
- ✗ 不擅自寫 HANDOFF_TO_10TH_MASTER.md（屬本 starter PASS 後另一個 task）

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §C.7 + Phase A.11 / Phase B B.9 / Phase C Wave 11 pattern。

### 任務目標

新建 1 個檔：
1. `_design/PHASE_D_COMPLETION_REPORT.md` v1.0（Phase D 完成報告；含 5 必填中文 header + 9 段結構對齊 PHASE_C_COMPLETION_REPORT pattern）

### Wave 16 驗收 4 個維度

**維度 1：技術驗證（CODEX 跑全部）**

1. **check_headers.py：** \`python -X utf8 -B scripts/check_headers.py\` 須報 0 ERROR；WARN 數記錄當前 baseline（含 PHASE_D_COMPLETION_REPORT v1.0 可能 +1 WARN 屬既有 markdown header 慣例）
2. **check_paths.py：** \`python -X utf8 -B scripts/check_paths.py\` 報 ERROR；本輪不要求降低 baseline，但要求**不增加** — Windows 端權威為 ≤ 247 ERROR（R2-MAJOR-03 hard-limit accept）；新建 PHASE_D_COMPLETION_REPORT 內 path reference 全採新慣例（outer fence ~~~ + Instance-only path 加 <instance_root>/ 前綴）
3. **build_repo_index：**
   \`\`\`python
   from scripts.parse_frontmatter import build_repo_index
   result = build_repo_index('.')
   errors = [i for i in result.issues if getattr(i, 'severity', None) == 'ERROR']
   warnings = [i for i in result.issues if getattr(i, 'severity', None) == 'WARN']
   \`\`\`
   - 要求：errors == 0
   - perf：< 5s
4. **expected_entities.yaml 對齊：** 確認 _design/expected_entities.yaml 存在 + Wave 16 後仍可被 build_repo_index 載入 0 ERROR

**維度 2：Phase D 4 個 Wave 落地 review consolidation**

5. **Wave 12 starter 落地驗證（SKILL.md 未實作；只 verify starter）：**
   - _design/CODEX_D1_STARTER.md v0.3 存在 + 5 必填 header（/iterate-world；共通範本）
   - _design/CODEX_D2_STARTER.md v0.3 存在（/iterate-character；引用 D1）
   - _design/CODEX_D3_STARTER.md v0.3 存在（/iterate-relationship；引用 D1）
   - _design/CODEX_D4_STARTER.md v0.2 存在（/iterate-outline；引用 D1）
   - _design/CODEX_D5_STARTER.md v0.4 存在（/iterate-detailed-outline + /iterate-scene --split-to-file；D-054 NEW_REQ_15 落地）
   - 00_protocol/00_j_迭代協議.md v0.2 存在（共通基底；9th master 第一段升版）
   - 5 個 D starter 全含 D-050 + D-053 邊界三 block + frontmatter 紀律 + phase_log entry 規範
   - **明示 partial 狀態：** Wave 12 SKILL.md 尚未實作（5 個 /iterate-* + /iterate-scene = 6 SKILL.md + 中文 wrapper）；屬 CODEX D.1-D.5 task 範圍；推 10th master 或更晚輪實作；本 Wave 16 不擅自實作

6. **Wave 13 4 個 /view-* SKILL.md 驗證（已落地）：**
   - .claude/skills/view-world/SKILL.md v0.1 + 查看世界觀 wrapper v0.1
   - .claude/skills/view-character/SKILL.md v0.1 + 查看角色 wrapper v0.1
   - .claude/skills/view-outline/SKILL.md v0.1 + 查看大綱 wrapper v0.1
   - .claude/skills/view-detailed-outline/SKILL.md v0.1（含 D-054 hybrid fallback）+ 查看細綱 wrapper v0.1
   - 4 個英文主檔 11 段結構齊全 + 5 階段流程對齊 ARCH §4.1 動態組合 + 純讀取邊界 7 條
   - phase_log entry 含 read_sources + output_target: chat（read-only audit pattern）

7. **Wave 14 4 個 /export-* SKILL.md 驗證（已落地）：**
   - .claude/skills/export-world/SKILL.md v0.1 + 匯出世界觀 wrapper v0.1
   - .claude/skills/export-character/SKILL.md v0.1 + 匯出角色 wrapper v0.1
   - .claude/skills/export-outline/SKILL.md v0.1 + 匯出大綱 wrapper v0.1
   - .claude/skills/export-detailed-outline/SKILL.md v0.1（**含 D-054 hybrid fallback 完整三 Phase**）+ 匯出細綱 wrapper v0.1
   - 4 個英文主檔 11 段結構齊全 + 5 階段流程對齊 ARCH §4.2 靜態整合檔
   - DERIVED frontmatter 7 欄齊全（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級 / 生成方式 / 組合來源）
   - Breadcrumb / 條件 TOC > 200 行 / 末尾返回連結紀律對齊 ARCH §4.3
   - 邊界三 block（D-050 子裁決 1 + D-053 紀錄 + D-050 子裁決 2 寫檔目錄表）
   - phase_log entry 含 output_path + output_lines + breadcrumb_added + toc_added + slug_validation_result
   - **§4.2a Layer 3 Export A1 prompt 生成器明示不實作**（屬 Phase A.0F.x / 10th master scope）

8. **Wave 15 /diagnose + /integrate SKILL.md 驗證（已落地）：**
   - .claude/skills/diagnose/SKILL.md v0.1 + 診斷 wrapper v0.1
   - .claude/skills/integrate/SKILL.md v0.1 + 整理 wrapper v0.1
   - /diagnose 對齊 00_a §3.3 診斷模式 — 6 段診斷報告格式對齊 §3.3.4 + 三種使用模式 (Mode A scan_all / Mode B file_path / Mode C inline_text) + 純讀取邊界 8 條（D6 7 條 + §3.3.3 5 條延伸）+ phase_log optional audit 預設不寫
   - /integrate 對齊 00_a §3.4 整理模式 — Stage 4 拆 4a 印 diff / 4b 寫檔嚴格分離 + 邊界四 block（D-050 三 + D-052 AI-assisted 紀律精神）+ D-054 hybrid 維持 aggregate 06_a 預設

**維度 3：Phase D 整體鏈驗收（14 SKILL.md + 14 wrapper + 5 starter + 1 framework）**

9. **整體 skill 落地狀態：**

   | Wave | 英文主檔 | 中文 wrapper | 狀態 |
   |---|---|---|---|
   | 12 (5 + split-to-file) | iterate-world / iterate-character / iterate-relationship / iterate-outline / iterate-detailed-outline | 迭代世界觀 / 迭代角色 / 迭代關係 / 迭代大綱 / 迭代細綱 | ⏳ Starter only；SKILL.md 待實作 |
   | 13 (4) | view-world / view-character / view-outline / view-detailed-outline | 查看世界觀 / 查看角色 / 查看大綱 / 查看細綱 | ✅ 落地 |
   | 14 (4) | export-world / export-character / export-outline / export-detailed-outline | 匯出世界觀 / 匯出角色 / 匯出大綱 / 匯出細綱 | ✅ 落地 |
   | 15 (2) | diagnose / integrate | 診斷 / 整理 | ✅ 落地 |

10. **整體 pipeline 依賴鏈：**
    - 上游（Phase B）→ /create-* / /iterate-* 維護
    - 視圖層 → /view-* chat / /export-* DERIVED view/ 整合檔
    - 通用模式 → /diagnose（純讀取）/ /integrate（寫檔需 user 拍板）
    - 下游（Phase C）→ /scene-task → /dialogue-write → /qa（已落地）
    - Canon Delta framework → 未來 11+ 輪 master 實作（屬「成熟期功能」）

**維度 4：Canon Delta framework + L3 schema 對齊備忘 + Phase D 啟動條件 + Milestone 4 接近條件**

11. **Canon Delta framework 落地（不實作 skill）：**
    - _design/CANON_DELTA_FRAMEWORK.md v0.1 存在 + 對齊 UD v0.5 §5 完整 framework（5.1 識別 / 5.2 抽取演算法 / 5.3 提案流程 / 5.4 回寫執行 / 5.5 與既有實體互動 / 5.6 禁止事項 / 5.7 phase_log / 5.8 UI/UX 標記）
    - 屬「成熟期功能」framework reference；給 11+ 輪 master / 工具 B 翻譯工具 fork reference 用
    - 明示啟動條件 4 trigger（A Milestone 4+6 個月 / B 工具 B 啟動 / C user 主動回報 / D 跟 NEW_REQ_16/17/18 自動化 QA 工具同步）
    - 跟既有 Phase D /qa / /iterate-* / 09_e LOCKED 模板的關聯紀錄

12. **L3 Export schema 對齊備忘（不實作）：**
    - CODEX_D10_STARTER.md §Z 段含 L3 schema 對齊備忘
    - Wave 14 /export-* 寫出的 view/<entity>.md 結構 vs L3_EXPORT_PROMPT_SCHEMA v0.2 §1.1 5 區塊對齊狀況紀錄
    - 兩條 export 路徑共存不取代（§4.2 4 個 /export-* skill + §4.2a Layer 3 Export A1 prompt 生成器）— 屬 ARCH §4.2a.4 區分表
    - §4.2a L3 prompt 生成器本體屬 Phase A.0F.x / 10th master scope；本 Wave 不實作

13. **Phase D 啟動條件達成宣告：**
    - ✓ Wave 13/14/15 SKILL.md 全落地（10 個英文主檔 + 10 個中文 wrapper）
    - ✓ Wave 12 starter 落地（5 個 D starter + 00_j 迭代協議）
    - ⏳ Wave 12 SKILL.md 待 CODEX D.1-D.5 task 實作（屬 deferred；推 10th master 或更晚輪）
    - ✓ Canon Delta framework v0.1 落地（不實作 skill）
    - ✓ L3 schema 對齊備忘落地（不實作生成器）
    - ✓ 9th master 第二段對話 Round 1-4 review cycle 教訓 5 條內化（POST_LOCK_PENDING v0.18）

14. **Milestone 4 接近條件達成宣告（非達成）：**

    | 條件 | 狀態 | 說明 |
    |---|---|---|
    | Phase D 4 個 Wave 設計框架完成 | ✓ 達成 | starter + 落地 SKILL.md + framework reference |
    | Phase D Wave 13/14/15 SKILL.md 落地 | ✓ 達成 | 10 SKILL.md + 10 wrapper |
    | Phase D Wave 12 SKILL.md 落地 | ⏳ 待 10th master / 更晚輪 | 5 個 /iterate-* + /iterate-scene = 6 SKILL.md + 6 wrapper |
    | Canon Delta framework 紀錄 | ✓ 達成 | framework reference；不實作 |
    | L3 schema 對齊備忘 | ✓ 達成 | 對齊備忘紀錄；不實作生成器 |
    | **Phase A.0F 前端工具補完** | ⏳ 待 Phase A.0F 平行對話 + 10th master | A.0F.3 ~ A.0F.11 + 整體驗收（11 個 feature spec；UX_SPEC §11）|
    | Milestone 4 真正封版宣告 | ⏳ 待 10th master | Phase D 完成 + Phase A.0F 補完 = 真正 Milestone 4 達成 |

    **明示 wording：** 本報告宣告「**Milestone 4 接近條件達成**」（非達成）— Phase D 設計框架完成 + Wave 13-15 落地；剩餘 Wave 12 SKILL.md + Phase A.0F 前端工具補完 = 真正 Milestone 4 封版條件，屬 10th master 範圍。

### PHASE_D_COMPLETION_REPORT 9 段結構（對齊 PHASE_C_COMPLETION_REPORT v1.0 pattern）

請依以下 9 段結構撰寫 _design/PHASE_D_COMPLETION_REPORT.md v1.0：

- **§0 文件目的**（含本檔位置 + 對齊 PHASE_C / PHASE_B / PHASE_A 同 pattern + 本檔特殊性：Wave 12 SKILL.md partial + Milestone 4 接近條件非達成）
- **§1 驗收摘要**（4 維度表 + Milestone 4 接近條件達成宣告 + repo SHA + 驗收日期 + repo 性質 + 寫檔範圍）
- **§2 維度 1：技術驗證**（baseline 表 + 紀律 5 條對齊 PHASE_C §2 pattern）
- **§3 維度 2：Wave 12-15 review consolidation**（4 個 sub-section：§3.1 Wave 12 starter / §3.2 Wave 13 view-* / §3.3 Wave 14 export-* / §3.4 Wave 15 diagnose+integrate；每 sub-section 列具體驗收項表）
- **§4 維度 3：Phase D 整體鏈驗收**（§4.1 14 SKILL.md 落地狀態表 + §4.2 14 wrapper 落地狀態表 + §4.3 Wave 12 SKILL.md partial 狀態說明 + §4.4 pipeline 依賴鏈）
- **§5 維度 4：Canon Delta framework + L3 schema 對齊備忘 + Phase D 啟動條件**
- **§6 端到端測試（user 親跑步驟 — placeholder）**：M4 user-test 建議步驟 + NEW_REQ_14 AI-assisted §6 補入機制紀錄
- **§7 Phase D 完成聲明**：4 維度 PASS + Milestone 4 接近條件達成 + Wave 12 SKILL.md / Phase A.0F 推 10th master scope
- **§8 後續：10th master 啟動條件聲明** + 接手 scope 表（Phase A.0F.3 ~ A.0F.11 + Wave 12 SKILL.md 實作 + Milestone 4 封版宣告）
- **§9 Cross-ref**

### §6 user 親跑 placeholder + NEW_REQ_14 AI-assisted §6 補入機制（沿用 PHASE_C pattern）

M4 user-test 建議步驟（待 user 親跑）：

| 步驟 | Skill / Gate | 預期結果 |
|---:|---|---|
| 1 | 確認 Phase C M3 testing Instance 內 W/V/C/R/P/CH/S ≥ REVIEW + 至少 1 場 dialogue 進入 DIALOGUE_FINAL | M4 prerequisites 滿足 |
| 2 | /view-world | chat 印整合視圖（W-rules + V + W-language + 00_b §1/§2）|
| 3 | /export-world | 寫 <instance_root>/view/世界觀.md DERIVED 整合檔 |
| 4 | /view-character <name> | chat 印角色整合視圖（含 D-054 hybrid scene-index discovery）|
| 5 | /export-character <name> | 寫 <instance_root>/view/角色_<name>.md DERIVED |
| 6 | /diagnose | chat 印 6 段診斷報告（對齊 00_a §3.3.4）|
| 7 | /integrate <target> --target=character 或其他 target | Stage 4a 印 diff + 等 user 拍板 → Stage 4b 寫檔 |
| 8 | （Wave 12 SKILL.md 實作後）/iterate-world | 對齊 00_j 迭代協議跑變更點識別 + 影響範圍評估 |
| 9 | /status + /check-gaps | 確認 Phase D 對 Instance 完成度的影響可見 |

**user 親跑結果待補：** [user 跑完 M4 chain 後在本檔 §6 補入結果摘要]

NEW_REQ_14 AI-assisted §6 補入機制：

1. user 在 master 對話內明示拍板：「我已跑完 M4 chain；請補入 §6」。
2. agent 讀 Instance 的 .protocol_version.phase_log、git log、review_log、實際 runtime 檔案清單。
3. agent reconstruct §6 事實摘要：步驟、結果、發現議題、是否需 D-NNN / NEW_REQ。
4. agent 先列草稿與 evidence，等待 user 拍板 OK。
5. user OK 後，agent 才把 §6 placeholder 更新為實際 M4 testing 結果。

此流程沿用 D-052 的 AI-assisted / manual fallback 精神：user 做權威拍板，agent 只做 mechanical reconstruction 與報告落地。

### §8 10th master 啟動條件聲明 + 接手 scope 表

10th master 可由下一輪 user 接手啟動。10th master scope：

- **A. Phase A.0F.3 ~ A.0F.11 前端工具補完**（依 TASKS §A.0F + UX_SPEC §11 11 個 feature spec）
- **B. Wave 12 SKILL.md 實作**（5 個 /iterate-* + /iterate-scene --split-to-file = 6 SKILL.md + 6 中文 wrapper；對齊 9th master 第一段對話 D1-D5 starter）
- **C. Milestone 4 真正封版宣告**（PHASE_D_COMPLETION_REPORT v1.X partial supersede 把「接近條件達成」升「達成」）
- **D. NEW_REQ_9 / NEW_REQ_11 / NEW_REQ_15 / NEW_REQ_16 / NEW_REQ_17 / NEW_REQ_18 重新評估**（屬 deferred backlog；依 POST_LOCK_PENDING v0.18）

10th master 啟動條件達成判定：

| 條件 | 目前狀態 | 說明 |
|---|---|---|
| Phase D Template 端 completion | ✓ 達成 | 本報告 4 維度 PASS（含 Wave 12 SKILL.md partial）|
| Wave 13/14/15 SKILL.md 落地 | ✓ 達成 | 10 SKILL.md + 10 wrapper |
| Canon Delta framework 紀錄 | ✓ 達成 | _design/CANON_DELTA_FRAMEWORK.md v0.1 |
| L3 schema 對齊備忘 | ✓ 達成 | CODEX_D10_STARTER §Z |
| Wave 12 SKILL.md 實作 | ⏳ 待 10th master | 6 SKILL.md + 6 wrapper |
| Phase A.0F 前端工具補完 | ⏳ 待 Phase A.0F 平行對話 + 10th master | 11 個 feature + 整體驗收 |
| M4 Instance end-to-end | 待 user 親跑 | §6 placeholder；不阻 Template 端 Milestone 4 接近條件聲明 |

10th master cleanup queue / 後續優先序：

| 優先序 | 項目 | 狀態 |
|---:|---|---|
| 1 | Wave 12 SKILL.md 實作（D.1-D.5 task）+ /iterate-scene --split-to-file | DEFERRED；屬 10th master 起手必做 |
| 2 | Phase A.0F.3 ~ A.0F.11 + 整體驗收 | DEFERRED；Phase A.0F 平行對話進行中；10th master 接手收尾 |
| 3 | NEW_REQ_9 check_paths baseline 247 ERROR 中 27 老式 filename reference | DEFERRED；屬 LOCKED 模板需 D-NNN 拍板 |
| 4 | NEW_REQ_16/17/18 自動化 QA 工具 3 層架構（lint script / auto-patcher / nightly review）| DEFERRED；屬封版後維護期 |
| 5 | NEW_REQ_15 D-054 hybrid 迭代評估（trigger A/B/C/D monitor）| DEFERRED；屬實際使用後評估 |
| 6 | NEW_REQ_11 工具 B 翻譯工具分支 | DEFERRED；屬封版後分支設計 |

### 寫檔紀律

1. **嚴禁修改既有檔**（除新建 _design/PHASE_D_COMPLETION_REPORT.md）
2. **新檔含 5 必填中文 header**（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
3. **新檔內 path reference 採新慣例**（outer fence ~~~ / Instance-only path 加 <instance_root>/ 前綴）
4. **明示 partial 狀態 + Milestone 4 接近條件（非達成）wording**
5. **不擅自實作 Wave 12 缺漏 6 個 SKILL.md**
6. **不擅自寫 HANDOFF_TO_10TH_MASTER.md**

### 不允許

- ✗ 擅自實作 Wave 12 缺漏的 6 SKILL.md
- ✗ 擅自寫 HANDOFF_TO_10TH_MASTER.md
- ✗ 升任何檔狀態（含 PHASE_D_COMPLETION_REPORT 必為 DRAFT v1.0）
- ✗ 擅自啟動 D-NNN 拍板（如有發現議題 → 在 PHASE_D_COMPLETION_REPORT §8 列為「待 10th master 評估」）
- ✗ 擅自跑真實 /iterate-* / /view-* / /export-* / /diagnose / /integrate 寫檔（會污染 Template）
- ✗ 改 .protocol_version 任何欄位

### 完成回報

PHASE_D_COMPLETION_REPORT.md 寫好後請回報：

- 報告路徑：_design/PHASE_D_COMPLETION_REPORT.md
- 行數 / bytes
- 4 維度結果（pass / fail 個別宣告）
- Wave 12 SKILL.md partial 狀態確認
- Milestone 4 接近條件達成宣告（非達成）
- baseline 跑後結果（check_headers + check_paths + build_repo_index）
- 是否有需要 master 拍板的議題
- 建議下一步（master 端 inline patch 或進 Wave 16 Step 3 跑 CODEX review starter）
~~~

---

# 2. 完成條件 + 後續

Wave 16 task 完成 = 以下全部 ✓：

\`\`\`
✓ _design/PHASE_D_COMPLETION_REPORT.md v1.0 落地（9 段結構齊全）
✓ 4 維度驗收結果寫入報告（partial PASS — Wave 12 SKILL.md partial state 明示）
✓ §6 user 親跑 placeholder 含 NEW_REQ_14 AI-assisted 機制紀錄
✓ Milestone 4 接近條件達成宣告（非達成；含「真正 Milestone 4 達成需 Wave 12 SKILL.md + Phase A.0F」明示）
✓ §8 10th master 啟動條件聲明 + scope 表
✓ §9 Cross-ref 齊全
✓ baseline check_headers 0 ERROR / check_paths ≤ 247 ERROR（Windows 端權威；R2-MAJOR-03 hard-limit accept 維持）
✓ 完成回報含議題列表（如有）
\`\`\`

PASS 後續：

- master 端內部 review + 跑 Wave 16 Step 3 CODEX review starter（屬最終 milestone；動用完整 CODEX 4-6 維度重審）
- review PASS 後 → Wave 16 Step 4 寫 HANDOFF_TO_10TH_MASTER.md（屬另一個 task；本 starter 不擅自寫）

---

# 3. 文件維護紀律

- 本 starter 是「啟動指南」；CODEX 跑完後**不需要更新本檔**
- PHASE_D_COMPLETION_REPORT v1.0 必為 DRAFT 狀態（master 端 review + Wave 16 Step 3 CODEX review PASS 後可考慮升 REVIEW，但屬下一輪 master / 10th master scope）
- 若 CODEX 跑出來發現 Wave 14/15 SKILL.md 內有 finding → 回報 master 端 inline patch；不擅自改 SKILL.md
- 若發現需要新 D-NNN 拍板 → 列在 PHASE_D_COMPLETION_REPORT §8 「待 10th master 評估」；不擅自開拍板

---

# 4. Cross-ref

- _design/TASKS.md v1.9 §C.7（Phase D 整體驗收 task spec）
- _design/PHASE_C_COMPLETION_REPORT.md v1.0（pattern 對齊範本）
- _design/PHASE_B_COMPLETION_REPORT.md v1.4（同 pattern 對照）
- _design/PHASE_A_COMPLETION_REPORT.md v1.1（同 pattern 對照）
- _design/CODEX_C_FINAL_STARTER.md v0.1（同 starter pattern 對照）
- _design/HANDOFF_9TH_MASTER_CONTINUATION.md v1.0（9th master 第二段對話 scope）
- _design/HANDOFF_TO_9TH_MASTER.md v1.0（原 9th master 整體 scope）
- _design/POST_LOCK_PENDING.md v0.18（NEW_REQ deferred 清單 + 9th master 第一段 5 條教訓內化）
- _design/D054_DECISION_PACKAGE.md v0.2（D-054 hybrid 拍板包）
- _design/CANON_DELTA_FRAMEWORK.md v0.1（本 Wave 落地的 framework reference）
- _design/CODEX_D1_STARTER.md v0.3 ~ CODEX_D5_STARTER.md v0.4（Wave 12 starter set；SKILL.md 待實作）
- _design/CODEX_D6_STARTER.md v0.1 + CODEX_D_VIEW_BATCH_STARTER.md v0.1（Wave 13 starter）
- _design/CODEX_D10_STARTER.md v0.1（含 §Z L3 schema 對齊備忘）+ CODEX_D_EXPORT_BATCH_STARTER.md v0.1（Wave 14 starter）
- _design/CODEX_D14_STARTER.md v0.1 + CODEX_D_DIAGNOSE_INTEGRATE_BATCH_STARTER.md v0.1（Wave 15 starter）
- .claude/skills/view-*/SKILL.md v0.1 + 4 中文 wrapper（Wave 13 落地）
- .claude/skills/export-*/SKILL.md v0.1 + 4 中文 wrapper（Wave 14 落地）
- .claude/skills/diagnose/SKILL.md v0.1 + 診斷 wrapper v0.1（Wave 15 落地）
- .claude/skills/integrate/SKILL.md v0.1 + 整理 wrapper v0.1（Wave 15 落地）
