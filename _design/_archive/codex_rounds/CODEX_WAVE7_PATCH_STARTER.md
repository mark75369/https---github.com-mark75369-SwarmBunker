狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase B Wave 7 patch round — 3 個主 SKILL.md 對齊 D-050 邊界裁決  
優先級：高

# CODEX_WAVE7_PATCH_STARTER — Wave 7 patch round（對齊 D-050 邊界裁決）

# 0. 本檔用途

對 Wave 7 review NO-GO 後 3 個主 SKILL.md（`create-character` / `create-relationship` / `create-outline`）跑 patch round，對齊 master 第六輪 D-050 拍板（DECISIONS_LOG v1.5 §6.12.2）的兩條子裁決：

- **D-050 子裁決 1：** /create-* skill 嚴禁寫 00_protocol/（唯一例外 /init-project）
- **D-050 子裁決 2：** /create-* skill 寫檔目錄嚴格依本子裁決 2 表限定

Patch 完成後跑 Round 2 review；GO 後 Wave 7 PASS → 進 Wave 8。

**對應 review report：** `_design/CODEX_WAVE67_REVIEW_REPORT.md` v0.1 §6 W7-MAJOR-01 / -02 / -03。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Wave 7 patch round」— 對 3 個主 SKILL.md 跑修補對齊 D-050 邊界裁決（DECISIONS_LOG v1.5 §6.12.2）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 修補 3 個主 SKILL.md 對齊 D-050 兩條子裁決
- 對齊傳統：同 Wave 2 A.0F.1 NO-GO patch round 模式（CODEX 修補 + 後續 Round 2 review）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / `00_protocol/` 任何檔（含 Wave 6 patch 後的 00_f / 00_l / 00_g v0.2）
- ✗ **不**動 `_tools/frontend/` / `scripts/`
- ✗ **不**改 3 個中文 wrapper（已 PASS）
- ✗ **不**改既有 8 SKILL.md（init-project / create-world / status / check-gaps + 4 wrapper）
- ✗ **不**新增 INVOKE.md（D-048 嚴禁）

**本 task scope（嚴格限定）：**

依 DECISIONS_LOG v1.5 §6.12.2 D-050 兩條子裁決 + CODEX_WAVE67_REVIEW_REPORT v0.1 §6 三個 Major finding。

### 任務目標：3 個主 SKILL.md patch round

| 檔 | 對應 finding | 主要 patch 範圍 |
|---|---|---|
| `.claude/skills/create-character/SKILL.md` | W7-MAJOR-02 | 收斂 Stage 4 write set + 加 D-050 邊界明示 + 升 v0.2 |
| `.claude/skills/create-relationship/SKILL.md` | W7-MAJOR-03 | 補角色聲線卡關係段 merge + 移除 05_plot 寫入 + 升 v0.2 |
| `.claude/skills/create-outline/SKILL.md` | W7-MAJOR-01 | 移除 05_b chapter shell / CH-* / 00_b 寫入 + 升 v0.2 |

### Patch 每個主 SKILL.md 共用動作

#### Patch 共用 1：升 header v0.1 → v0.2

```diff
- 狀態：DRAFT
- 版本：v0.1
- 最後更新：2026-05-20
+ 狀態：DRAFT
+ 版本：v0.2（Wave 7 patch round — D-050 邊界對齊）
+ 最後更新：2026-05-20
```

#### Patch 共用 2：邊界段加 D-050 嚴禁項

每 SKILL.md 的「邊界」/「## 邊界」/「The skill must not」段加下列明示句（對應 D-050 兩條子裁決）：

```
**D-050 子裁決 1（DECISIONS_LOG v1.5 §6.12.2）：**
- 嚴禁修改任何 `00_protocol/` 內檔（含 00_a / 00_b / 00_c / 00_d / 00_e / 00_f / 00_g / 00_h / 00_i / 00_k / 00_l）
- 唯一例外是 /init-project（依 00_i §6 LOCKED 設計）；本 skill 不在例外範圍

**D-050 子裁決 2（DECISIONS_LOG v1.5 §6.12.2）：**
- 本 skill 寫檔目錄嚴格限定為下列範圍；任何超出範圍的寫入屬越界
- 越界寫入觸發 ⏸ 條件未滿足拒絕 + WARN（不靜默越界）
- 詳寫檔目錄表見本 SKILL.md 「## 輸出」段
```

### Patch /create-character/SKILL.md（W7-MAJOR-02 修補）

依 D-050 子裁決 2 C 行：寫檔目錄限定 **`03_characters/main/<name>_聲線卡.md`** + **`minor/<name>_聲線卡.md`** + **`npc/<NPC類型>模板.md`**。

修補動作：
1. **移除以下寫入授權**（屬越界）：
   - `04_relationships/04_a` 等 04 目錄寫入 → 不寫；改為 stage 5 印「下一步建議跑 /create-relationship 補關係段」
   - `05_plot/05_c` 等 05 目錄寫入 → 不寫；屬 P skill scope
   - `09_quality_assurance/09_a` 等 09 目錄寫入 → 不寫；屬下游 /qa skill scope
   - `00_protocol/00_b` §5 寫入 → 嚴禁；屬 /init-project 例外範圍
2. **保留以下寫入**（合法）：
   - `03_characters/main/<name>_聲線卡.md`（主角色）
   - `03_characters/minor/<name>_聲線卡.md`（次角色）
   - `03_characters/npc/<NPC類型>模板.md`（NPC 類型；複用模板）
3. **「## 輸出」段加 D-050 寫檔目錄表**：列出 C skill 的合法寫檔目錄 + 明示「不寫」目錄
4. **「## 邊界」段加 D-050 共用 patch 句**
5. Stage 4 寫檔順序 review：只寫 03_characters/ 範圍

### Patch /create-relationship/SKILL.md（W7-MAJOR-03 修補）

依 D-050 子裁決 2 R 行：寫檔目錄限定 **`04_relationships/04_a` (matrix row append)** + **`04_b` (timeline if 議題 6 觸發)** + **`03_characters/<a>_聲線卡.md` 的「關係段」merge** + **`<b>_聲線卡.md` 的「關係段」merge**。

修補動作：
1. **補必要輸出**（W7-MAJOR-03 缺漏項）：
   - 在 Stage 4 寫檔清單加：「修改 `03_characters/<a>_聲線卡.md` 的【關係】段 — 加 `<b>` 對應關係描述」（merge 操作；不寫整個聲線卡）
   - 同上對 `<b>_聲線卡.md`
   - 強調「關係段」merge 是「**section-level merge**」— 只動聲線卡內【關係】子段，不動其他段
2. **移除以下寫入授權**（屬越界）：
   - `05_plot/05_c` 等 05 目錄寫入 → 不寫；屬 P skill scope
   - `00_protocol/` 任何寫入 → 嚴禁
3. **保留以下寫入**（合法）：
   - `04_relationships/04_a_角色關係矩陣.md`（matrix row append）
   - `04_relationships/04_b_關係變化時間線.md`（timeline；只在議題 6 觸發時）
   - `03_characters/<a>_聲線卡.md` 與 `<b>_聲線卡.md` 的【關係】子段 merge
4. **「## 輸出」段加 D-050 寫檔目錄表**
5. **「## 邊界」段加 D-050 共用 patch 句** + 明示「不寫 03_characters/<x>_聲線卡.md 的其他段」

### Patch /create-outline/SKILL.md（W7-MAJOR-01 修補；最嚴重）

依 D-050 子裁決 2 P 行：寫檔目錄限定 **`05_plot/05_a` (主體)** + **`05_c` (角色弧線；議題 4 觸發)** + **`05_d` (資訊揭露；議題 4 觸發)** + **`05_e` (伏筆與回收；議題 5 觸發)**。

修補動作：
1. **移除以下寫入授權**（屬越界）：
   - `05_plot/05_b_章節結構模板.md` **chapter shells 寫入** → 嚴禁；**屬 CH skill 的 B.7 scope**（/create-detailed-outline）
   - `00_protocol/00_b` §3/§4 寫入 → 嚴禁；屬 /init-project 例外範圍
   - **CH-* entities 示範與寫入** → 嚴禁；P skill 不寫 CH 檔，CH entities 屬 CH skill scope
2. **保留以下寫入**（合法）：
   - `05_plot/05_a_主線大綱模板.md`（主體；P entity 主要寫檔位置）
   - `05_plot/05_c_角色弧線表.md`（議題 4「與世界規則、角色合規性檢查」觸發時）
   - `05_plot/05_d_資訊揭露表.md`（議題 4 觸發時，含資訊揭露時間軸）
   - `05_plot/05_e_伏筆與回收表.md`（議題 5「規模定位」觸發伏筆規模時）
3. **創建 entity 限定為 P**（單一，無 suffix；不創 CH-*）
4. Stage 5 印「下一步建議跑 /create-detailed-outline 補 05_b chapter shell 與 CH-* entities」+ B.6.5 主線 REVIEW gate
5. **「## 輸出」段加 D-050 寫檔目錄表** + 明示「不寫 05_b chapter shell」+「不寫 00_protocol/」+「不創 CH-* entities」
6. **「## 邊界」段加 D-050 共用 patch 句** + 強調「P skill 不跨 CH scope」

### 中文 wrapper 不動

3 個中文 wrapper（建立角色 / 建立關係 / 建立大綱）review 已 PASS — **不動**。本 patch round 不涉及 wrapper。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/DECISIONS_LOG.md` v1.5 §6.12.2 D-050 兩條子裁決（**首要權威**）
2. `_design/CODEX_WAVE67_REVIEW_REPORT.md` v0.1 §6 W7-MAJOR-01 / -02 / -03（finding 細節）
3. `_design/CODEX_WAVE7_SKILLS_STARTER.md` v0.1（原 Wave 7 starter 規範；patch 後再 review）

B. 對齊基準
4. `_design/ARCHITECTURE.md` v1.5 §3.3 / §3.3.0 / §3.3.2（skill 內容規範 + multi-agent + Template-detect）
5. `_design/SPEC.md` v1.2 §5.1 entity / §5.4 phase_log
6. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2 / §1.3 / §1.5（C/P/R 上游腳本）
7. `00_protocol/00_f_角色創建協議.md` v0.2 / `00_l_關係創建協議.md` v0.2 / `00_g_大綱創建協議.md` v0.2（Wave 6 已對齊）

C. 既有 reference（不改）
8. `.claude/skills/init-project/SKILL.md` v0.2（D-049 範式；屬 /init-project 例外，不在 D-050 子裁決 1 範圍內）
9. `.claude/skills/create-world/SKILL.md`（已對齊 D-050 W 行）
10. `_design/registries/issue_type_registry.template.yaml` v0.1

D. 嚴禁區（不可動）
11. 所有 `_design/*.md`（含 DECISIONS_LOG v1.5；本輪不動）
12. `scripts/*.py`
13. 27 模板
14. `00_protocol/` 全部
15. `_tools/frontend/*`
16. 既有 8 SKILL.md + 3 中文 wrapper

---

**你要交付的產物：**

修改 3 個既有 SKILL.md：
1. `.claude/skills/create-character/SKILL.md` v0.1 → v0.2
2. `.claude/skills/create-relationship/SKILL.md` v0.1 → v0.2
3. `.claude/skills/create-outline/SKILL.md` v0.1 → v0.2

不新建任何檔；不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 3 個 SKILL.md header v0.2 + 最後更新 2026-05-20
- 每個 SKILL.md「## 輸出」段含 D-050 寫檔目錄表
- 每個 SKILL.md「## 邊界」段含 D-050 子裁決 1 + 子裁決 2 明示句

B. create-character 內容驗收
- 移除 04_relationships / 05_plot / 09_quality_assurance / 00_protocol 寫入授權
- 保留 03_characters/main / minor / npc 寫入授權
- Stage 4 寫檔順序限 03_characters/

C. create-relationship 內容驗收
- 加角色聲線卡【關係】子段 merge 必要輸出（對 <a> 與 <b>；section-level merge 不是整檔寫）
- 移除 05_plot / 00_protocol 寫入授權
- 保留 04_relationships/04_a + 04_b 寫入

D. create-outline 內容驗收
- 移除 05_plot/05_b chapter shell 寫入授權
- 移除 00_protocol/00_b §3/§4 寫入授權
- 移除 CH-* entities 示範與寫入
- 保留 05_plot/05_a + 05_c / 05_d / 05_e（依議題觸發）
- created_entities 限定為 P（單一；不創 CH-*）

E. 不破壞既有
- 3 個中文 wrapper（建立角色 / 建立關係 / 建立大綱）未動
- 既有 8 SKILL.md / 27 模板 / 00_protocol/ / _design/ / scripts/ / _tools/frontend/ 未動
- `python -X utf8 scripts/check_headers.py` 0 ERROR 維持
- `python -c "from scripts.parse_frontmatter import parse_file; [parse_file(p) for p in ['.claude/skills/create-character/SKILL.md', '.claude/skills/create-relationship/SKILL.md', '.claude/skills/create-outline/SKILL.md']]"` 0 ERROR

---

**Go / Done 判定指引：**

- **DONE：** A/B/C/D/E 驗收全 ✓ → 進 Round 2 review（重跑 CODEX_WAVE67_REVIEW_STARTER 同 prompt）
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 三個 patch 任一不對齊 D-050 → 修補

請開始。
```

---

# 2. 完成條件 + 後續

CODEX patch round 完成 → user commit/push → 跑 Round 2 review（同 CODEX_WAVE67_REVIEW_STARTER prompt）→ Round 2 GO 後 Wave 7 PASS → 進 Wave 8。

Round 2 review 預期結果：
- 3 個主 SKILL.md 維度 2 從 △/✗ 升 ✓
- 維度 1 / 3 / 4 維持 ✓
- 整體判定 GO

---

# 3. 文件維護紀律

- 本檔是 Wave 7 patch round CODEX task 啟動包；完成後可 archive 進 `_design/archive/`
- patch 完成 + Round 2 review GO 後可考慮升 ARCH v1.6 §3.3.3 + TASKS v1.9（把 D-050 邊界紀律寫進 spec 體；屬第七輪 master 動作）
- 若 Round 2 仍有 finding → 修補 round 同模式
