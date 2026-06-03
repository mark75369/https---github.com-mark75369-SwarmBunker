狀態：APPLIED
版本：v0.2（user 拍板選 1 Hybrid — 2026-05-21；拍板原文「先走方案一，未來實際使用後如果有迭代需求在後續版本再進行優化」；落地 DECISIONS_LOG §6.17 D-054 + POST_LOCK_PENDING NEW_REQ_13 RESOLVED + NEW_REQ_15 未來迭代追蹤）
最後更新：2026-05-21
適用範圍：D-054 NEW_REQ_13 per-scene 檔 convention 拍板包 — RESOLVED；保留作 D-054 拍板過程歷史紀錄 + 未來 D-055 重新評估時的 baseline 參考
優先級：高

# D054_DECISION_PACKAGE — per-scene 檔 convention 拍板包（✅ RESOLVED via Option 1）

# 0. 拍板結果摘要（v0.2 — 2026-05-21）

**✅ user 拍板：選 1 Hybrid**

- **拍板時間：** 2026-05-21
- **拍板原文：** 「先走方案一，未來實際使用後如果有迭代需求在後續版本再進行優化，幫我把這點紀錄在未來更新文件中」
- **未來迭代條件追蹤位置：** POST_LOCK_PENDING NEW_REQ_15「per-scene 拆檔 convention 迭代評估」DEFERRED（含 trigger A/B/C/D 建議 + 未來 D-055 候選選項預留）
- **落地檔：** 
  - DECISIONS_LOG v1.9 → **v2.0** §6.17 D-054 拍板紀錄 + §6.17.4 「未來迭代追蹤紀律」首例
  - POST_LOCK_PENDING v0.9 → **v0.10**（NEW_REQ_13 RESOLVED + NEW_REQ_15 DEFERRED 新增）
  - D054_DECISION_PACKAGE v0.1 → **v0.2**（本檔；標 APPLIED）
- **0 LOCKED spec supersede**（純新增拍板；不動 D-050/00_h/TASKS/UD/SPEC 任何既有 LOCKED 規範）
- **Phase C Wave 9 影響：** CODEX_C1_STARTER (/scene-task) 須含「per-scene → aggregate」兩階段 fallback 讀檔邏輯；C2/C3 不受影響

---

# 0.1 文件目的（v0.1 原文保留）

POST_LOCK_PENDING NEW_REQ_13（per-scene 檔 convention DEFERRED；2026-05-20 提出）在 Phase C `/scene-task` starter 寫作前需 user 拍板。本檔列 3 方案 + 推薦 + 對 Phase C 影響，給 user 拍板後落地：

- DECISIONS_LOG §6.17 D-054（新拍板紀錄）
- POST_LOCK_PENDING NEW_REQ_13 標 ✅ RESOLVED via D-054
- 可能涉及：00_h v0.3 / TASKS v1.10 / D-050 子裁決 2 CH 行 / SPEC §5.1 / UD §2.3 partial supersede（依拍板方案影響範圍變動）

**對 Phase C Wave 9 starter 的影響：** 8th master 必須拍板 D-054 才能寫 `/scene-task` starter（讀檔來源 = aggregate 06_a vs per-scene `06_scene_index/CH<n>_S<m>_*.md`）。

**前置 context：** Round 8 §8 D-054 audit（CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md §8）— 當前 spec baseline 已 audit 完。

---

# 1. 議題本質

NEW_REQ_13（POST_LOCK_PENDING.md:512-565）原文摘要：

- M2 testing 跑 `/create-detailed-outline` 階段 3 user 抓出 CONFLICT-1：starter 寫「每場一檔 `06_scene_index/CH<n>_S<m>_<name>.md`」，但 SKILL.md + D-050 子裁決 2 CH 行寫「`05_b + 06_a`（聚合單檔）」
- M2 testing 採聚合式 06_a；per-scene 拆檔屬未來 NEW_REQ migration
- Phase C `/scene-task` 起手前要先拍板：聚合 vs per-scene vs hybrid

## 1.1 當前 spec baseline（Round 8 audit 結論）

依 Round 8 §8 D-054 audit 表（10 row 跨檔審查）：

| 檔 | 當前 convention | 屬性 |
|---|---|---|
| `_design/SPEC.md` §5.1 | `S-<ch>-<n>` 是 1 個 entity 對映 `06_scene_index/` `07_scene_tasks/` `08_dialogue_outputs/` | hybrid |
| `_design/SPEC.md` §12.5 | `/scene-task` 為**單一 scene** 建 task pack | per-scene |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.3.2 | `/scene-task` 讀 `06_a` 抽取單一 scene row | per-scene from aggregate source |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.3.4 | `/scene-task` 寫 `07_scene_tasks/CH<n>_S<m>_*.md` per-scene | per-scene |
| `_design/TASKS.md` §D.2/D.3/D.4 | /scene-task / /dialogue-write / /qa 都 per-scene | per-scene |
| `00_protocol/00_h_細綱創建協議.md` | /create-detailed-outline 寫聚合 05_b + 06_a；S-* 維持 20% 完成度 | **聚合 06_a** |
| `00_protocol/00_k_台詞生產流程協議.md` | downstream 需 S-* 在 06_a 中，再寫 per-scene 07/08/09 | hybrid |
| `.claude/skills/create-detailed-outline/SKILL.md` | runtime 寫 05_b + 06_a；line 198 已含 escape hatch「Follow the existing local `06_scene_index` convention」 | **聚合 06_a with hybrid escape hatch** |
| `_design/registries/issue_type_registry.template.yaml` | 00_h 議題 placement 未明確；高風險場景 issue 引用 `06_a risk_type` | **聚合 06_a / 模糊未定** |

**結論：** 當前 spec 已是 **lifecycle hybrid**（上游聚合 + 下游 per-scene）；D-054 真正未決議題是「**`06_scene_index/` 內部本身**是否拆 per-scene 還是維持單一 `06_a`」。

## 1.2 為什麼此議題重要（影響 Phase C 起手）

`/scene-task` SKILL.md 的讀檔邏輯依賴此拍板：

- 若 06_scene_index 維持聚合 06_a → `/scene-task` 讀單檔 grep S-ID 對應 row
- 若 06_scene_index 拆 per-scene → `/scene-task` 讀對應 per-scene 檔
- 若 hybrid → `/scene-task` 須兩種都支援（fallback 邏輯）

不拍板就寫 starter → 後續可能要重寫 SKILL.md + protocol；屬 Phase C 起手 blocker。

---

# 2. 3 方案分析

## 2.1 方案 1：Hybrid（aggregate 06_a 預設 + `/iterate-scene --split-to-file` 拆出選項；**推薦**）

### 設計

- **/create-detailed-outline 階段 4**：預設寫聚合 06_a（**現狀不變**；D-050 子裁決 2 CH 行不動）
- **新增 `/iterate-scene <S-ID> --split-to-file` 選項**（屬 Phase D `/iterate-*` series 範圍；本拍板只 commit 設計意圖，實作延後 Phase D）
  - 把指定場景從聚合 06_a split 為獨立 `06_scene_index/CH<n>_S<m>_<scene_name>.md` 檔
  - 同時在原 06_a 行加 `<!-- split-to-file: CH<n>_S<m>_<scene_name>.md -->` marker（防止下游讀檔混淆）
- **/scene-task 讀檔 fallback 邏輯**：
  1. 先 check `06_scene_index/CH<n>_S<m>_<scene_name>.md` 是否存在
  2. 存在 → 讀 per-scene 檔
  3. 不存在 → fallback 讀 aggregate 06_a 對應 row
- **既有 00_h SKILL.md line 198 escape hatch wording 對齊**：「If a local Instance has adopted per-scene scene-index files, do not switch file organization during this skill」維持不動，自然承接 D-054 拍板

### 落地工作

| 動作 | 工時 | 影響 |
|---|---|---|
| DECISIONS_LOG §6.17 D-054 拍板 + 紀錄 3 方案推理 | 30 分 | 新拍板 |
| POST_LOCK_PENDING NEW_REQ_13 標 RESOLVED via D-054 | 5 分 | 對齊 |
| `/scene-task` starter (CODEX_C1_STARTER) 含 fallback 邏輯設計 | 含在 Wave 9 starter 內 | 設計新增 |
| `/iterate-scene --split-to-file` 設計意圖紀錄（不實作） | 入 POST_LOCK_PENDING NEW_REQ_15（新）或 9th master handoff queue | 延後 Phase D |
| 00_h / TASKS / D-050 子裁決 2 CH 行 | **不動**（D-054 不 supersede 任何既有 LOCKED） | 0 |
| SPEC §5.1 / UD §2.3 | **不動** | 0 |

### Pros

1. **改動範圍最小**：不破壞任何既有 LOCKED spec / SKILL.md / protocol；零 supersede
2. **跟既有 escape hatch 對齊**：00_h SKILL.md line 198 已預留此設計
3. **user 創作彈性最大**：小場景批量用聚合（30+ 場一次建）；重要長場景可拆出獨立檔做 LOCKED 粒度控制
4. **per-scene 拆出後 LOCKED 粒度可單場**：對長期創作 / 多 milestone 鎖場有用
5. **git diff 粒度可選**：批量編輯用聚合；單場改動拆出後 diff 乾淨
6. **跟下游 07/08/09 per-scene 不衝突**：上游可選聚合或拆；下游維持 per-scene

### Cons

1. **/scene-task 邏輯稍複雜**：須兩階段 fallback check（per-scene → aggregate）
2. **`/iterate-scene --split-to-file` 屬未來實作**：本拍板 commit 設計但不實作，留 Phase D
3. **長期可能出現 mixed Instance**：部分場景 per-scene 拆，部分聚合在 06_a；user 需自己管 split 紀錄（marker 可協助）

### 跟 Round 8 §8 audit 結論吻合度

✓ 直接落地 audit 結論「當前 docs 已是 hybrid in lifecycle；06_scene_index 內部 convention 是未決議題」

---

## 2.2 方案 2：完全 per-scene

### 設計

- **/create-detailed-outline 階段 4 重做**：直接每場一檔（一次建 N 個 `06_scene_index/CH<n>_S<m>_*.md`）
- **06_a 改為 index 索引**：只列場景 ID + 檔路徑 + 高層摘要（不含完整內容）
- **/scene-task 直接讀 per-scene 檔**：不需要 fallback
- **D-050 子裁決 2 CH 行需 supersede**：寫檔範圍從「`05_b + 06_a` only」改「`05_b + 06_a (index) + 06_scene_index/CH<n>_S<m>_*.md per-scene`」

### 落地工作

| 動作 | 工時 | 影響 |
|---|---|---|
| DECISIONS_LOG §6.17 D-054 拍板 + supersede D-050 子裁決 2 CH 行 | 60 分 | 新拍板 + supersede |
| POST_LOCK_PENDING NEW_REQ_13 標 RESOLVED via D-054 | 5 分 | 對齊 |
| `/create-detailed-outline` SKILL.md rewrite Stage 4 + D-050 寫檔表更新 | 60-90 分 | v0.2 → v0.3 |
| 00_protocol/00_h_細綱創建協議.md rewrite Stage 4 段 | 30-60 分 | v0.2 → v0.3 |
| `_design/TASKS.md` §B.7 partial supersede（更新 line 1362 + Stage 4 描述）| 30 分 | v1.9 → v1.10 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` §2.3 partial supersede | 30 分 | v0.5 → v0.6 |
| `_design/SPEC.md` §5.1 entity ↔ file mapping 補 per-scene 變體 | 30 分 | v1.2 → v1.3 |
| `/scene-task` starter 設計（純 per-scene 讀檔） | 含在 Wave 9 | 設計簡化 |
| frontmatter weight S-*-* = 0.2 在 per-scene 多檔 case 重算 | 30 分 | scripts 可能需動 |
| 27 模板 `06_a_場景索引模板.md` 改為 index pattern | 30 分 | 模板變動 |

### Pros

1. **Git diff 粒度最細**：一場改動只動一檔
2. **多人/多 agent 並行寫不同場景無 race condition**
3. **LOCKED 粒度單場**（同方案 1）
4. **跟下游 07/08/09 per-scene 完全對稱**：所有 scene 相關檔都 per-scene
5. **`/scene-task` 邏輯簡化**：直接讀對應 per-scene 檔，無 fallback

### Cons

1. **改動範圍最大**：5+ spec 改動（SKILL.md / 00_h / TASKS / UD / SPEC）+ supersede D-050 + 模板變動
2. **效率差**：/create-detailed-outline 一次建 30+ 場 = 寫 30+ 檔（vs 1 個聚合檔）
3. **/status 讀 30 檔 vs 1 檔** — 慢
4. **/check-gaps 讀檔範圍擴大** — 效能影響
5. **frontmatter weight 管理複雜**：S-*-* 在多檔 case 如何計算 0.2 weight 需重新設計
6. **per-scene 檔命名衝突風險**：scene_name 含特殊字元（中文、空格）可能造成 filename 問題
7. **Round 8 §8 audit 顯示「當前 spec 已 hybrid」**：強行改全 per-scene 跟既有 escape hatch 設計衝突
8. **跟既有 00_h v0.2 + create-detailed-outline v0.2 design intent 衝突**：屬 architecture rewrite

### 跟 Round 8 §8 audit 結論吻合度

✗ 與 audit 結論「當前 docs 已是 hybrid in lifecycle」衝突；需大幅 supersede

---

## 2.3 方案 3：完全聚合（維持現狀，NEW_REQ_13 標 NOT_NEEDED）

### 設計

- 維持 `/create-detailed-outline` 寫聚合 06_a only（現狀；D-050 子裁決 2 不動）
- `/scene-task` 讀 06_a 對應 row（現狀；UD §2.3.2 已寫）
- NEW_REQ_13 標 NOT_NEEDED / DEFERRED 永久；不開 D-054 拍板
- 00_h SKILL.md line 198 escape hatch 移除（避免誤導）

### 落地工作

| 動作 | 工時 | 影響 |
|---|---|---|
| POST_LOCK_PENDING NEW_REQ_13 標 NOT_NEEDED + 理由說明 | 10 分 | 對齊 |
| 00_h SKILL.md line 198 escape hatch 移除（v0.2 → v0.3） | 15 分 | 縮小 spec |
| 不開 D-054（不需新拍板） | 0 | 0 |
| `/scene-task` starter 設計（純聚合讀檔） | 含在 Wave 9 | 設計簡化 |

### Pros

1. **零新拍板**（NEW_REQ_13 DEFERRED → NOT_NEEDED 即可）
2. **設計穩定**：spec 不動
3. **/scene-task 邏輯最簡單**：純聚合讀 06_a

### Cons

1. **長期創作受限**：大型作品（100+ 場）06_a 整檔超大、git diff 雜
2. **per-scene LOCKED 粒度無法支援**：要 LOCK 單場只能整個 06_a LOCKED（過大）
3. **跟下游 per-scene 不對稱**：聚合上游 vs per-scene 下游 — 設計上不優雅但仍可運作
4. **未來若有 per-scene 需求需重開拍板**：等於 D-054 推遲到下一輪 master
5. **跟 00_h escape hatch wording 衝突**：line 198 要移除才一致；變動雖小但屬「縮小已有彈性」

### 跟 Round 8 §8 audit 結論吻合度

△ Audit 顯示 hybrid 是當前 baseline；方案 3 等於放棄既有 escape hatch 彈性

---

# 3. 推薦：方案 1 Hybrid

## 3.1 推薦理由

1. **跟 Round 8 §8 audit 結論最一致** — 「當前 docs 已是 hybrid in lifecycle；06_scene_index 內部 convention 是未決」
2. **跟既有 00_h escape hatch wording 自然對齊** — line 198 已預留此設計，方案 1 等於 codify 既有意圖
3. **改動範圍最小** — 零 LOCKED spec supersede（vs 方案 2 的 5+ spec supersede）
4. **user 創作彈性最大** — 同時保留聚合效率 + per-scene LOCKED 粒度
5. **`/iterate-scene --split-to-file` 屬未來實作** — 本拍板 commit 設計意圖；實作可延 Phase D，不影響 Phase C 起手
6. **/scene-task fallback 邏輯複雜度可控** — 兩階段 check 屬標準 fallback pattern，不增加太多 SKILL.md 複雜度

## 3.2 跟方案 2 的 trade-off 點

方案 2 的「per-scene 拆檔 = 設計優雅 / git diff 乾淨」優點在方案 1 也有（透過 `--split-to-file`）；方案 1 額外保留聚合彈性。方案 2 唯一獨有優點是「`/scene-task` 邏輯較簡單（無 fallback）」— 但這個複雜度增量很小（10-15 lines SKILL.md）vs 方案 2 5+ spec supersede 的工時。

## 3.3 跟方案 3 的 trade-off 點

方案 3 唯一獨有優點是「零新拍板」— 但這是放棄既有 escape hatch 設計彈性換來的。Phase C testing 跑下去若 user 真的想拆 per-scene，仍需重開拍板（NEW_REQ_13 重新打開）。

---

# 4. 對 Phase C Wave 9 的影響（依拍板方案）

## 4.1 拍板方案 1 後 Phase C starter 設計

`CODEX_C1_STARTER.md`（/scene-task starter）讀檔邏輯段：

```
讀 scene_id S-<ch>-<n> 對應 spec 時，依以下順序：
1. 先 check `06_scene_index/CH<n>_S<m>_<scene_name>.md` 是否存在
   - 存在 → 讀整檔（per-scene mode）
   - 不存在 → 進步驟 2
2. fallback 讀 `06_scene_index/06_a_場景索引.md` 對應 S-<ch>-<n> row
3. 若兩者皆無 → 拒絕（⏸ 條件未滿足）；提示 user 先跑 /create-detailed-outline
```

C2 `/dialogue-write` + C3 `/qa` 不受 D-054 影響（讀 task pack 不讀 06_scene_index 直接）。

## 4.2 拍板方案 2 後 Phase C starter 設計

`/scene-task` 直接讀 per-scene 檔；但 starter 寫作前需先處理：
- /create-detailed-outline rewrite + 00_h v0.3 + TASKS partial supersede + UD partial supersede + SPEC partial supersede
- **約 2-3 小時 wall-time 在拍板與 Wave 9 之間**

## 4.3 拍板方案 3 後 Phase C starter 設計

`/scene-task` 純聚合讀 06_a；starter 寫作前需先處理：
- 00_h line 198 escape hatch 移除（v0.2 → v0.3）

---

# 5. 落地步驟（拍板後執行）

## 5.1 拍板方案 1 落地

1. 8th master 寫 DECISIONS_LOG §6.17 D-054 拍板紀錄（5 欄：日期/議題/決策/影響/Owner）
2. POST_LOCK_PENDING NEW_REQ_13 標 ✅ RESOLVED via D-054
3. POST_LOCK_PENDING 新增 NEW_REQ_15「/iterate-scene --split-to-file 選項實作（Phase D scope）」DEFERRED
4. 8th master 寫 CODEX_C1_STARTER.md 含 fallback 邏輯
5. user commit/push
6. 進 Phase C Wave 9 後續工作

## 5.2 拍板方案 2 落地

1. 8th master 寫 DECISIONS_LOG §6.17 D-054 拍板 + supersede D-050 子裁決 2 CH 行紀錄
2. 8th master 多檔 partial supersede patch round（00_h v0.3 / TASKS v1.10 / UD v0.6 / SPEC v1.3 / create-detailed-outline v0.3）
3. user commit/push
4. CODEX 跑 Round 10 重審驗證 spec consistency
5. 8th master 寫 CODEX_C1_STARTER.md 純 per-scene 讀檔
6. 進 Phase C Wave 9 後續工作

## 5.3 拍板方案 3 落地

1. POST_LOCK_PENDING NEW_REQ_13 標 NOT_NEEDED + 理由
2. 8th master 改 00_h SKILL.md line 198 移除 escape hatch（v0.2 → v0.3）
3. user commit/push
4. 8th master 寫 CODEX_C1_STARTER.md 純聚合讀檔
5. 進 Phase C Wave 9 後續工作

---

# 6. user 拍板需回應

請 user 從以下選一個並回應：

- **「拍板選 1 Hybrid」**（推薦）+ 拍板理由（一句話）→ 我落地 §5.1
- **「拍板選 2 完全 per-scene」** + 拍板理由 → 我落地 §5.2
- **「拍板選 3 完全聚合」** + 拍板理由 → 我落地 §5.3
- **「我要先看 evidence」** → 我列具體 spec 段落 / SKILL.md 行給你看
- **「我要修改方案 X 的某些細節」** → 你指出哪些細節需要修改

---

# 7. Cross-ref

- `_design/POST_LOCK_PENDING.md` v0.9 NEW_REQ_13（per-scene 檔 convention 議題提出 + 3 方案候選）
- `_design/CODEX_8TH_MASTER_CLEANUP_REVIEW_REPORT.md` v0.1 §8（Round 8 D-054 pending state audit；10 row 跨檔審查）
- `_design/HANDOFF_TO_8TH_MASTER.md` v1.0 §4.2（8th master Phase C 規劃時 open D-054）
- `_design/DECISIONS_LOG.md` v1.9 §6.12.2 D-050 子裁決 2（CH 行寫檔範圍）
- `_design/SPEC.md` v1.2 §5.1（entity 定義 ↔ file mapping）
- `_design/SPEC.md` v1.2 §12.5（任務包必填欄位）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.3（/scene-task 讀檔 + 寫檔規範）
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §2.4/§2.5（/dialogue-write + /qa；不直接受 D-054 影響）
- `_design/TASKS.md` v1.9 §D.2 / §D.3 / §D.4（下游 3 skill task spec）
- `00_protocol/00_h_細綱創建協議.md` v0.2 §10.7 / §10.8（細綱拆分規格 + 聚合 06_a 設計）
- `00_protocol/00_k_台詞生產流程協議.md` v0.1（下游 pipeline）
- `.claude/skills/create-detailed-outline/SKILL.md` v0.2 line 198（既有 escape hatch wording）
- `_design/registries/issue_type_registry.template.yaml`（00_h_detailed_outline 議題）
