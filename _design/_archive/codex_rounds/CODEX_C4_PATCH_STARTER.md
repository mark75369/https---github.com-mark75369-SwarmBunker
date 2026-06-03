狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-21  
適用範圍：Phase C Wave 10 補丁 patch round — 補建 09_g/h/i 三 QA 模板（TASKS §D.1a / D-043 遺留 debt；C.3 /qa skill 設 prerequisite check 缺即拒絕，本 patch 解除 Milestone 3 阻塞）  
優先級：高

# CODEX_C4_PATCH_STARTER — Phase C Wave 10 補 09_g/h/i 三 QA 模板

# 0. 本檔用途

Phase C Wave 10 補丁 patch round — 補建 `09_quality_assurance/09_g_節奏感檢查模板.md` + `09_h_對話張力檢查模板.md` + `09_i_跨場一致性檢查模板.md` 三個 QA 模板。

**背景：** D-043（DECISIONS_LOG §6.7~§6.9 partial supersede D-018 #3）2026-05 升級 QA 從 5 → 8 報告必跑。TASKS v1.9 §D.1a 列為 task 但 master 沒實際補建 → 9_g/h/i 三模板從未存在 repo 內。C.3 /qa skill 設「8 模板存在」為 runtime prerequisite — 缺任一拒絕執行。

**Milestone 3 阻塞解除：** 補完 3 模板後 user 在 Instance 才能實際跑 /qa 完整 8 報告 pipeline；Milestone 3「user 可量產台詞」才真正達成。

**前置條件：** Phase C Wave 10 C.1 + C.2 + C.3 PASS（3 個下游 skill 全落地 + commit/push）。

**C4 patch PASS → 進 Wave 11 整體驗收（CODEX_C_FINAL_STARTER）→ PHASE_C_COMPLETION_REPORT v1.0 → 🟡 Milestone 3 達成**

⚠ **慣例（依 POST_LOCK_PENDING NEW_REQ_10）：**
- 本 starter outer agent-prompt fence 用 `~~~`

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase C Wave 10 patch round」— 補建 09_g/h/i 三 QA 模板（TASKS §D.1a / D-043 遺留 debt；解除 C.3 /qa skill prerequisite 阻塞）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪建 3 個新 QA 模板檔（純通用 Template；非作品專屬）
- 對應 task：TASKS v1.9 §D.1a「v1.1 新增 task — 對應 D-026 + D-043（8 份必跑）」
- C4 patch PASS → 進 Wave 11 整體驗收 → Milestone 3 達成

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 00_k v0.1；R8-INFO-06 stale 仍不本輪處理）
- ✗ **不**改 _tools/frontend/ / scripts/ 任何檔
- ✗ **不**動既有 SKILL.md（含 Phase C C.1/C.2/C.3 + 中文 wrapper）
- ✗ **不**改 5 個既有 QA 模板（09_a / 09_b / 09_c / 09_d / 09_f）— 已 LOCKED
- ✗ **不**改 09_e 模板（final-gating 紀錄 — M9 鎖定）
- ✗ **不**跑真實 /qa 寫 QA 報告（屬 user 親跑 M3 testing）
- ✗ **不**動 D-054 落地檔（DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.12 / D054_DECISION_PACKAGE v0.2）
- ✗ **不**新建除這 3 模板外的任何檔

**本 task scope（嚴格限定）：**

依 TASKS v1.9 §D.1a + UD v0.5 §3.7 / §3.8 / §3.9 + 既有 09_a/b/c/d/f 模板格式範式。

### 任務目標

新建 3 個檔：

| # | 路徑 | qa_type | algorithm 來源 |
|---|---|---|---|
| 1 | `09_quality_assurance/09_g_節奏感檢查模板.md` | RHYTHM | UD §3.7 |
| 2 | `09_quality_assurance/09_h_對話張力檢查模板.md` | DRAMATIC_TENSION | UD §3.8 |
| 3 | `09_quality_assurance/09_i_跨場一致性檢查模板.md` | CROSS_SCENE_CONTINUITY | UD §3.9 |

### 3 模板共用結構（依 TASKS §D.1a + 對齊既有 09_a/b/c/d/f）

每模板含：

- frontmatter（依 5 必填中文 header + YAML block）：
  ```yaml
  狀態：DRAFT
  版本：v0.1
  最後更新：2026-05-21
  適用範圍：[該模板用途，依 qa_type 對應]
  優先級：中
  
  ---
  qa_type: [RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY]
  entities: []
  depends_on: []
  weight: {}
  ---
  ```
- markdown 主體含 5 層檢查框架（對齊 UD §3.5.1 通用結構）：
  - `## 用途`
  - `## qa_type` 段（明示 enum 值對應 qa_type_registry）
  - `## 5 層檢查框架`（對應 UD §3.<x>.1 段）
  - `## 檢查 algorithm`（對應 UD §3.<x>.2 段；本模板核心）
  - `## frontmatter M7/M10 對齊`（對齊 UD §3.<x>.3 段）
  - `## 通用化原則`（依 UD §3.<x>.4 段；不含任何作品專屬內容）
  - `## 輸出格式`（QA 報告產出規範；含 8 欄 frontmatter + body 結構）

### 09_g 節奏感檢查模板（依 UD §3.7）

- **qa_type：** RHYTHM
- **檢查重點：** 句長分布 / 句長變異度 / 長短句交替 / 段落呼吸感
- **適用範圍：** 「對單場台詞檔做節奏感分析的通用 QA 模板（含 5 層檢查框架）」
- **algorithm 摘要（從 UD §3.7 抄入）：**
  - 句長分布統計（短句 < 10 字 / 中句 10-25 字 / 長句 > 25 字 比例）
  - 句長變異度（相鄰句長變化百分比）
  - 長短句交替模式（連續短/連續長句段落偵測）
  - 段落呼吸感（段落間留白 / 對話分行密度）
- **完整 algorithm：** 抄 UD §3.7 完整內容（保留 6+ 子節節奏分析項）

### 09_h 對話張力檢查模板（依 UD §3.8）

- **qa_type：** DRAMATIC_TENSION
- **檢查重點：** 推進 / 讓步 / 揭穿 / 反擊頻率 + 攻防力度量化
- **適用範圍：** 「對單場台詞檔做對話張力分析的通用 QA 模板（含 5 層檢查框架）」
- **algorithm 摘要（從 UD §3.8 抄入）：**
  - 推進句 vs 讓步句比例（角色推動劇情 vs 角色退讓）
  - 揭穿時機（資訊揭露密度跟章節節奏對齊）
  - 反擊頻率（被動句 vs 主動句轉換）
  - 攻防力度量化（每句的「衝突指數」評分）
- **完整 algorithm：** 抄 UD §3.8 完整內容

### 09_i 跨場一致性檢查模板（依 UD §3.9）

- **qa_type：** CROSS_SCENE_CONTINUITY
- **檢查重點：** 跨場聲線漂移 / 跨場資訊洩漏 / 跨場節奏 arc
- **適用範圍：** 「對多場台詞檔做跨場一致性分析的通用 QA 模板（含 5 層檢查框架）」
- **algorithm 摘要（從 UD §3.9 抄入）：**
  - 跨場聲線漂移（同一 C-* 在不同場的聲線特徵差異）
  - 跨場資訊洩漏（早場揭露違反 05_d 約束的後場資訊）
  - 跨場節奏 arc（連續多場節奏走勢；high/mid/low 模式）
  - 跨場伏筆對齊（05_e 伏筆從場景到場景的傳遞）
- **完整 algorithm：** 抄 UD §3.9 完整內容
- **跨場範圍：** 跨章 / 跨集 / 主角 arc 全長（依 REQUIREMENTS_LOCK §4.1 拍板「跨場」定義）

### 通用化原則（3 模板共用 — 對齊 UD §3.5.4）

- **不含任何作品專屬內容**（無「林思羽」/「陳則安」/「情緒感知體質」等具體角色 / 世界觀 / 主線細節）
- **純通用 Template**：可被任何 Instance 繼承後填入該作品專屬內容
- **frontmatter `entities: []` / `depends_on: []` / `weight: {}`**（Template 內為空；Instance 跑 /qa 時動態填入 entity list / dependency / weight）
- **參考既有 09_a / 09_b / 09_c / 09_d / 09_f 模板**（已 LOCKED 通用 Template；本輪 3 模板採同樣風格 / 同樣結構）

### 啟動前檢查

```
Before writing the 3 templates, verify:

- current folder is the Template repo（`.template_root` marker exists at repo root）
- 5 個既有 QA 模板存在：`09_quality_assurance/09_a_AI味檢查模板.md` / `09_b_角色聲線一致性模板.md` / `09_c_禁用詞檢查模板.md` / `09_d_資訊控制檢查模板.md` / `09_f_類型偏移檢查模板.md`
- 09_e 模板存在但**不在本輪 scope**：`09_quality_assurance/09_e_定稿變更紀錄模板.md`
- UD §3.7 / §3.8 / §3.9 可讀（algorithm 來源）
- `_design/registries/qa_type_registry.template.yaml` v0.1 已含 RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY enum 值（D-043 拍板時應已建；只 verify 不動）
```

### 文字長度建議

每模板 ~150-250 行 markdown（含 5 層檢查框架 + 完整 algorithm 抄寫 UD §3.<x>）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §3.7（09_g algorithm）+ §3.8（09_h algorithm）+ §3.9（09_i algorithm）（**本 task 主要 reference — algorithm 抄寫源**）
2. `_design/TASKS.md` v1.9 §D.1a（v1.1 新增 task；對應 D-026 + D-043）
3. `_design/SPEC.md` v1.2 §12.7（v1.1 對齊 8 份序列順序）
4. `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1（QA 模板擴充 — 3 模板用途說明）

B. 對齊依據（格式範本 — LOCKED 不動）
5. `09_quality_assurance/09_a_AI味檢查模板.md`（**主要格式範本**）
6. `09_quality_assurance/09_b_角色聲線一致性模板.md`（格式範本）
7. `09_quality_assurance/09_c_禁用詞檢查模板.md`（格式範本）
8. `09_quality_assurance/09_d_資訊控制檢查模板.md`（格式範本）
9. `09_quality_assurance/09_f_類型偏移檢查模板.md`（格式範本 — UD §3.5 對應）
10. `_design/registries/qa_type_registry.template.yaml` v0.1（9 種 qa_type enum verify）

C. R8-INFO-06 context（背景 — 本輪不處理但需理解）
11. `00_protocol/00_k_台詞生產流程協議.md` v0.1 階段 3（5 報告 stale；本輪不 patch）
12. `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043（8 報告必跑拍板）

D. 已 LOCKED 不可動文件
13. 所有 `_design/*.md` 既有 spec
14. `scripts/*.py`
15. 既有 27 模板（含 09_a/b/c/d/f/e）
16. 所有 `00_protocol/` 檔
17. `_tools/frontend/*` 全部
18. 既有 SKILL.md（init-project / create-* x5 / status / check-gaps / 6 中文 wrapper / scene-task / dialogue-write / qa / 場景任務包 / 生成台詞 / 檢查）

---

**你要交付的產物：**

新建 3 個檔：
1. `09_quality_assurance/09_g_節奏感檢查模板.md` v0.1
2. `09_quality_assurance/09_h_對話張力檢查模板.md` v0.1
3. `09_quality_assurance/09_i_跨場一致性檢查模板.md` v0.1

不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 3 個模板存在於 `09_quality_assurance/` 目錄
- 各自含 5 必填中文 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）+ YAML block (`qa_type` / `entities` / `depends_on` / `weight`)
- 採同 09_a/b/c/d/f 風格的 markdown 主體

B. 內容
- 09_g：qa_type=RHYTHM；algorithm 對齊 UD §3.7
- 09_h：qa_type=DRAMATIC_TENSION；algorithm 對齊 UD §3.8
- 09_i：qa_type=CROSS_SCENE_CONTINUITY；algorithm 對齊 UD §3.9
- 3 模板均含 5 層檢查框架（用途 / qa_type / 框架 / algorithm / 通用化原則 / 輸出格式）
- 完全不含作品專屬內容（無具體角色名 / 世界觀 / 主線細節）

C. 不破壞既有
- 不動既有 27 模板（含 09_a/b/c/d/e/f）
- 不動 _design/ / 00_protocol/ / scripts/ / _tools/frontend/ / .claude/skills/
- `python scripts/check_headers.py` 0 ERROR 維持
- `python scripts/check_paths.py` baseline -3（補完 3 模板後，C.3 /qa skill prerequisite check 應該不再回報 09_g/h/i 缺檔 baseline ERROR；驗證 baseline 應降）

---

**Go / Done 判定指引：**

- **DONE：** A/B/C 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** algorithm 跟 UD §3.7/§3.8/§3.9 不對齊 OR 含作品專屬內容 OR 格式不對齊 09_a/b/c/d/f → 修補 round

請開始。
~~~

---

# 2. 完成條件 + 後續

CODEX C4 patch 完成 → user commit/push → 回 master：

1. **9th master cleanup queue 更新**（POST_LOCK_PENDING NEW_REQ_19）：「09_g/h/i 三模板補建」從 deferred 標 ✅ RESOLVED via C4 patch round（屬第八輪 master Phase C 收尾範圍）
2. master 寫 Wave 11 整體驗收 starter（`CODEX_C_FINAL_STARTER.md`）
3. CODEX 跑 Wave 11 → 撰寫 `_design/PHASE_C_COMPLETION_REPORT.md` v1.0
4. 🟡 Milestone 3 達成宣告
5. master 寫 `HANDOFF_TO_9TH_MASTER.md` 接 Phase D

---

# 3. 文件維護紀律

- 本檔是 Phase C Wave 10 補丁 starter；完成後可 archive
- ⚠ 補完 3 模板後 user M3 testing 才能實際跑 /qa 完整 8 報告 pipeline；Milestone 3 真正達成

---

# 4. Cross-ref

- `_design/TASKS.md` v1.9 §D.1a（v1.1 新增 task；對應 D-026 + D-043）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §3.7 / §3.8 / §3.9（algorithm 抄寫源）
- `_design/DECISIONS_LOG.md` v2.0 §6.7~§6.9 D-043（8 報告必跑拍板）
- `_design/SPEC.md` v1.2 §12.7
- `_design/REQUIREMENTS_LOCK.md` v1.0 §4.1
- `_design/POST_LOCK_PENDING.md` v0.12 NEW_REQ_19（9th master cleanup queue — 09_g/h/i 補建本輪由 8th master 提前處理）
- `_design/registries/qa_type_registry.template.yaml` v0.1
- `.claude/skills/qa/SKILL.md` v0.1（C.3 ；prerequisite check 缺 3 模板即拒絕）
- 既有 5 個 QA 模板（09_a/b/c/d/f）— 格式範本
