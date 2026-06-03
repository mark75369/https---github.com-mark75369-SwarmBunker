狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase B Wave 6 task 啟動包 — B.0/B.1/B.2/B.3 4 個 protocol D-047 對齊 patch round  
優先級：高

# CODEX_WAVE6_PROTOCOLS_PATCH_STARTER — Phase B Wave 6：4 個 /create-* protocol D-047 對齊

# 0. 本檔用途

Phase B Wave 6 第一波 task（B.0~B.3）— **4 個既有 protocol patch round 對齊 D-047 issue_type_registry 機制**（同 master 第五輪 A.3 patch 00_e 模式）。

**重要 scope 修正：**
- 原 TASKS v1.7 §B.0~B.3 寫法為「**寫新** 00_l / 00_f / 00_g / 00_h protocol」
- master 第六輪本輪驗證：**4 個 protocol 已存在**（May 18 第五輪整合期間完成）— 結構性已完整含 5 階段流程 + 5 必填 header
- 但 **0 個引用 D-047 / issue_type_registry / user_extensions / core_overrides 機制**（D-047 拍板於 master 第五輪後續，4 個 protocol 寫作早於 D-047 拍板）
- Wave 6 task scope 變為 **「對齊 D-047 patch round」**（同 A.3 對 00_e 模式）

**B.4** 03_characters/ 子目錄結構 master 已 verify 存在（main / minor / npc 三子目錄；May 16 既有）— 不需 CODEX 動作 → B.4 自動完成。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase B Wave 6 task」— 對 4 個既有 protocol 跑 D-047 對齊 patch round（同 A.3 對 00_e patch 模式）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪 patch 4 個既有 protocol 對齊 D-047 issue_type_registry 機制
- 對應傳統：Wave 6 第一波 task（含 B.0 + B.1 + B.2 + B.3）；B.4 已由 master verify 完成

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**改既有 27 模板 / 其他 protocol（00_a / 00_b / 00_c / 00_d / 00_e / 00_i / 00_k）
- ✗ **不**動 `_tools/frontend/` / `scripts/` 任何檔
- ✗ **不**動任何 `.claude/skills/` 既有 8 個 SKILL.md
- ✗ **不**動 `_design/` 既有 LOCKED spec（除了 TASKS 升 v1.8 紀錄 B.0~B.4 patch 完成）
- ✗ **不**新寫 5 階段流程（已存在；只加 D-047 機制段）

**本 task scope（嚴格限定）：**

依 DECISIONS_LOG v1.4 §6.9.2 D-047 + issue_type_registry.template.yaml v0.1 + 00_e 第五輪 A.3 patch 後狀態（reference template）。

### 任務目標

對 4 個既有 protocol 各加 3 個 D-047 對齊段 + 升 v0.1 → v0.2：

1. `00_protocol/00_l_關係創建協議.md` v0.1 → v0.2（對應 yaml key `00_l_relationship`，6 議題）
2. `00_protocol/00_f_角色創建協議.md` v0.1 → v0.2（對應 yaml key `00_f_character`，8 議題）
3. `00_protocol/00_g_大綱創建協議.md` v0.1 → v0.2（對應 yaml key `00_g_outline`，6 議題）
4. `00_protocol/00_h_細綱創建協議.md` v0.1 → v0.2（對應 yaml key `00_h_detailed_outline`，6 議題）

### 對齊參考：00_e 第五輪 A.3 patch 後的 D-047 段（reference template）

讀 `00_protocol/00_e_世界觀創建協議.md` v0.2 的下列段作為 patch 模板：

- §2 啟動條件加第 5 條「`<instance_root>/issue_type_registry.yaml` 可讀（D-047 + Contract D §4a 對齊）」+ Template fallback 規則
- §4.0「議題清單動態構建（D-047 / Contract D §4a.2）」段 — 含 6 條規則 + Registry 異常處理
- §4.1「議題順序預設表」— 5-column table（順序 / 議題 / required_level / locked / 為什麼這時問）

### 每個 protocol 的 patch 規格

對每個 protocol（00_l / 00_f / 00_g / 00_h），執行下列 patch：

#### Patch 1：header v0.1 → v0.2

```diff
- 版本：v0.1
+ 版本：v0.2（D-047 對齊 — 加 issue_type_registry 動態構建機制段）
- 最後更新：2026-05-18
+ 最後更新：2026-05-20
```

#### Patch 2：§2 啟動條件加 D-047 條目

在既有 §2 啟動條件 list 末加新條目（沿用 00_e §2 第 5 條格式）：

```markdown
N. **`<instance_root>/issue_type_registry.yaml` 可讀**（D-047 + Contract D §4a 對齊）：
   - registry 不存在 → 從 `_design/registries/issue_type_registry.template.yaml` Template fallback + WARN
   - registry schema 異常（YAML parse error / 缺對應 skill key 等）→ 拒絕進階段 2
```

對應 4 個 protocol 各自的 skill key 為：
- `00_l` → `00_l_relationship`
- `00_f` → `00_f_character`
- `00_g` → `00_g_outline`
- `00_h` → `00_h_detailed_outline`

#### Patch 3：在 §4（階段 2 章節）開頭加 §4.0 動態構建段

新加章節（複製 00_e §4.0 結構，把 `00_e_world` 改成對應 skill key）：

```markdown
## 4.0 議題清單動態構建（D-047 / Contract D §4a.2）

階段 2 啟動時，agent **必須**讀 `<instance_root>/issue_type_registry.yaml` 的 `<對應_skill_key>` skill key 區段，按 **`core + user_extensions − core_overrides`** 動態構建議題清單：

1. **core 議題**先依 `id` 升序排列（id 1-99 為 core 保留範圍）。
2. **`user_extensions[*]`** 接在 core 議題後（id ≥ 100 為 user 自訂議題保留範圍）。
3. 套用 **`core_overrides[*].skip_id`** 過濾：
   - 對應 core entry `locked=true` → agent **忽略**該 override 並 **WARN**「locked 議題 id={n} 不可 SKIP，core_overrides 條目被忽略」；該議題仍出現在清單
   - 對應 core entry `locked=false` → 從議題清單中移除
   - `skip_id` 不存在於 core → WARN「core_overrides skip_id={n} 找不到對應 core 議題；條目被忽略」
4. 對每個議題：
   - `required_level=REQUIRED` → 跳階段 4 前**必答**；缺漏拒絕進階段 4
   - `required_level=STRONGLY_PREFERRED` → 跳階段 4 允許但 phase_log 紀錄缺漏 + 對應分拆檔段落標 TODO
   - `required_level=OPTIONAL` → 跳階段 4 允許不紀錄
5. `core[*].question_summary` 只作為 opener；agent 完整提問腳本詳本檔對應 §N（沿用 UD §1.x.2 完整內容）。
6. **拆分規則不入 registry** — 屬 agent 階段 4 寫檔 mechanic，由本檔末節固定執行，不對 user 提問。

**Registry 異常處理：**
- 若 registry 載入失敗（YAML parse error / 缺對應 skill key 等）→ agent **拒絕進階段 2**，請 user 修補 registry
- 若 `user_extensions[*].id < 100` 或 與 core id 重複 → parser ERROR；agent 拒絕進階段 2
```

⚠ **每個 protocol 的「對應 §N」與「UD §1.x.2」要填對：**
- 00_l → `本檔對應 §10`（如有；否則指 §8 後段）+ UD §1.5.2
- 00_f → `本檔對應 §N`（依既有 protocol 內議題列表所在段） + UD §1.2.2
- 00_g → `本檔對應 §N` + UD §1.3.2
- 00_h → `本檔對應 §N` + UD §1.4.2

#### Patch 4：在 §4.0 後加 §4.1 議題順序預設表

依 `issue_type_registry.template.yaml` v0.1 的 core 議題清單，生成 5-column 表：

| 順序 | 議題 | required_level | locked | 為什麼這時問 |

「為什麼這時問」欄 CODEX 依議題語意推導（簡短一句話；對齊 UD §1.x.2 既有腳本若有）。

每個 protocol 對應的議題清單：

**00_l_relationship（6 議題）：**
```yaml
- id: 1  關係類型分類             REQUIRED         locked=true
- id: 2  權力差                  STRONGLY_PREFERRED locked=false
- id: 3  稱呼系統                REQUIRED         locked=true
- id: 4  情緒債                  STRONGLY_PREFERRED locked=false
- id: 5  不能說出口的事          STRONGLY_PREFERRED locked=false
- id: 6  關係時間線錨點          STRONGLY_PREFERRED locked=false
```

**00_f_character（8 議題）：**
```yaml
- id: 1  角色類型分類            REQUIRED         locked=true
- id: 2  聲線測試題（5 個極端場景） REQUIRED         locked=true
- id: 3  去名測試前置            STRONGLY_PREFERRED locked=false
- id: 4  與 W-rules / V / W-language 合規性檢查 STRONGLY_PREFERRED locked=false
- id: 5  髒話來源欄位            STRONGLY_PREFERRED locked=false
- id: 6  偏移檢查欄位            STRONGLY_PREFERRED locked=false
- id: 7  聲線污染檢查            OPTIONAL         locked=false
- id: 8  與類型氣質合規檢查      STRONGLY_PREFERRED locked=false
```

**00_g_outline（6 議題）：**
```yaml
- id: 1  必先三件事              REQUIRED         locked=true
- id: 2  想要 vs 需要測試（戲劇經典原則） REQUIRED locked=true
- id: 3  結構選擇                REQUIRED         locked=true
- id: 4  與世界規則、角色合規性檢查 STRONGLY_PREFERRED locked=false
- id: 5  規模定位                STRONGLY_PREFERRED locked=false
- id: 6  類型偏移風險清單        STRONGLY_PREFERRED locked=false
```

**00_h_detailed_outline（6 議題）：**
```yaml
- id: 1  章節節奏分布            REQUIRED         locked=true
- id: 2  角色弧線 × 章節矩陣對齊  REQUIRED         locked=true
- id: 3  資訊揭露時間軸          REQUIRED         locked=true
- id: 4  伏筆與回收佈點          STRONGLY_PREFERRED locked=false
- id: 5  高風險場景識別          REQUIRED         locked=true
- id: 6  高風險場景的「作品專屬正確處理方式」 STRONGLY_PREFERRED locked=false
```

每個議題對應「為什麼這時問」CODEX 自行從 issue_type_registry.template.yaml 的 `description` 欄位或 UD §1.x.2 對話腳本中抓取摘要（簡短一句）。

#### Patch 5：既有「議題數」描述對齊 registry

某些 protocol 既有寫法可能 hardcode 議題數（如 00_f 寫「9 個議題」但 registry 是 8 個；00_g / 00_h 寫「7 個議題」但 registry 都是 6 個）— 對齊改為 **registry core 數 + 註腳「最終議題清單依 registry user_extensions / core_overrides 動態構建」**。

| Protocol | 既有寫法（可能）| Patch 後 |
|---|---|---|
| 00_l | 6 議題（既有對齊）| 6 user-facing 議題 + 註腳 D-047 動態構建 |
| 00_f | 9 議題（既有）| **8 user-facing 議題** + 註腳 D-047 動態構建 + supersede 9 議題舊寫法 |
| 00_g | 7 議題（既有）| **6 user-facing 議題** + 註腳 D-047 動態構建 + supersede 7 議題舊寫法 |
| 00_h | 7 議題（既有）| **6 user-facing 議題** + 註腳 D-047 動態構建 + supersede 7 議題舊寫法 |

CODEX grep 4 個 protocol 找「N 個議題」「N 項議題」文字並對齊 patch（同 Wave 2 Round 2 review A3-R2-01 殘留文字修補模式）。

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/DECISIONS_LOG.md` v1.4 §6.9.2（D-047 拍板）+ §6.11.7（baseline 校正裁決）
2. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D（issue_type_registry）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2 / §1.3 / §1.4 / §1.5（4 個 /create-* skill 上游權威）
4. `_design/registries/issue_type_registry.template.yaml` v0.1（議題清單 source）

B. Reference template（patch 模板）
5. `00_protocol/00_e_世界觀創建協議.md` v0.2（A.3 第五輪 patch 後狀態 — 4 個 protocol 對齊 reference）

C. 既有 protocol（待 patch）
6. `00_protocol/00_l_關係創建協議.md` v0.1
7. `00_protocol/00_f_角色創建協議.md` v0.1
8. `00_protocol/00_g_大綱創建協議.md` v0.1
9. `00_protocol/00_h_細綱創建協議.md` v0.1

D. 已 LOCKED 不可動文件
10. 所有 `_design/*.md` 既有 spec（除升 TASKS v1.8 紀錄 patch 完成外不動）
11. `scripts/*.py`
12. 既有 27 模板
13. `00_protocol/00_a / 00_b / 00_c / 00_d / 00_e / 00_i / 00_k`（其他 protocol 不動）
14. `_tools/frontend/*` 全部
15. 所有 `.claude/skills/*/SKILL.md`

---

**你要交付的產物：**

修改 4 個既有 protocol 檔：
1. `00_protocol/00_l_關係創建協議.md` v0.1 → v0.2
2. `00_protocol/00_f_角色創建協議.md` v0.1 → v0.2
3. `00_protocol/00_g_大綱創建協議.md` v0.1 → v0.2
4. `00_protocol/00_h_細綱創建協議.md` v0.1 → v0.2

不新建任何檔；不動其他檔。

**驗收條件（CODEX 自我驗證）：**

A. 檔結構
- 4 個 protocol header v0.2 + 最後更新 2026-05-20
- 每個 protocol 含 §2 啟動條件加 D-047 條目 + §4.0 動態構建段 + §4.1 議題順序預設表
- 議題數對齊：00_l = 6 / 00_f = 8 / 00_g = 6 / 00_h = 6（user-facing 議題；refs to D-047 動態構建）
- 既有「N 個議題」hardcode 文字全 supersede 對齊

B. 內容
- §4.0 結構對齊 00_e §4.0 模板（6 條規則 + Registry 異常處理）
- skill key 對應對齊（00_l → 00_l_relationship / 00_f → 00_f_character / 等）
- §4.1 5-column 表完整（順序 / 議題 / required_level / locked / 為什麼這時問）
- 議題 required_level / locked 對齊 issue_type_registry.template.yaml v0.1

C. 不破壞既有
- 4 個 protocol 既有 5 階段流程內容不動（除議題數文字 supersede）
- 沒動其他 protocol / spec / SKILL.md
- `python scripts/check_headers.py` 0 ERROR 維持
- `python -c "from scripts.parse_frontmatter import parse_file; [parse_file(p) for p in ['00_protocol/00_l_關係創建協議.md', '00_protocol/00_f_角色創建協議.md', '00_protocol/00_g_大綱創建協議.md', '00_protocol/00_h_細綱創建協議.md']]"` 0 ERROR

D. 其他
- 4 個 protocol 跟 00_e v0.2 的對齊範式一致（風格、用語、結構順序）
- 不擅自重寫 5 階段流程細節
- 不擅自加新議題（屬 D-NNN+ 拍板範圍）

---

**Go / Done 判定指引：**

- **DONE：** A/B/C/D 驗收全 ✓
- **BLOCKED：** 任一驗收 ✗ 回 master
- **NO-GO：** 4 protocol 任一 patch 不對齊 D-047 → 修補 round

請開始。
```

---

# 2. 完成條件 + 後續

CODEX Wave 6 patch round 完成 → user commit/push → 回 master → master 升 TASKS v1.8（紀錄 B.0~B.4 完成 + Wave 6 patch round 紀錄）→ 推 Wave 7（B.5 + B.5.5 + B.5b + B.6 + B.6.5）。

---

# 3. 文件維護紀律

- 本檔是 CODEX Wave 6 patch round task 啟動包；完成後可 archive 進 `_design/archive/`
- 若 patch round NO-GO → 開 CODEX_WAVE6_PATCH_PATCH_STARTER.md（同 A.0F.1 模式）
