狀態：DRAFT（骨架）  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：下游寫對白 3 個 skill 完整語法  
優先級：高（Phase D 完成後補完整內容）

# 03 下游 Skill

> ⏳ **本章骨架待 Phase D 完成後補完整內容**（範例、進階參數、隱藏功能）  
> 目前提供 skill 清單 + pipeline 流程 + 8 份 QA 順序

# 1. Skill 清單（3 個）

| Skill | 中文別名 | 模式 | 對應協議檔 |
|---|---|---|---|
| `/scene-task <scene_id>` | `/場景任務包 <scene_id>` | — | `00_protocol/00_k_*.md` 階段 1 |
| `/dialogue-write <scene_id>` | `/生成台詞 <scene_id>` | 試寫 / 破格 / 收斂 / SINGLE_ITER | `00_protocol/00_k_*.md` 階段 2 |
| `/qa <dialogue_path>` | `/檢查 <dialogue_path>` | — | `00_protocol/00_k_*.md` 階段 3 |

---

# 2. 下游 Pipeline 場景狀態機

```
SCENE_INDEXED        場景索引中存在（/create-detailed-outline 產出）
   ↓ /scene-task
TASK_DRAFT           任務包 DRAFT
   ↓ 人類審 D.2.5 gate
TASK_REVIEW          任務包 REVIEW
   ↓ /dialogue-write
DIALOGUE_TRIAL       多版本 v01A/B/C
   ↓ 人類挑亮點 D.3.5 gate
DIALOGUE_CONVERGED   收斂版 v02
   ↓ /qa
QA_PASSED / QA_FAILED
   ↓ 人類確認 + 填 09_e
DIALOGUE_FINAL
   ↓ 人類 LOCKED
DIALOGUE_LOCKED
```

---

# 3. /dialogue-write 4 種模式

| 模式 | 指令 | 行為 |
|---|---|---|
| 試寫（預設） | `/dialogue-write S-01-03` | 產 v01A 克制 / v01B 衝突 / v01C 情緒 三版 |
| 破格 | `/dialogue-write S-01-03 --experimental` | 產 v01D 詩化 / 黑色幽默等大膽版 |
| 收斂 | `/dialogue-write S-01-03 --converge --picks "v01A.l001,v01B.l003"` | 整合亮點產 v02 |
| 單版本迭代（v1.1 新）| `/dialogue-write S-01-03 --single-iter --note "..."` | 跟 user 迴圈改一版到滿意 |

---

# 4. /qa 跑 8 份報告（v1.1）

對應 SPEC §12.7 + UD §2.5.3。

## 4.1 並行檢查、序列印出順序

```
1. 09_f 類型偏移檢查（GENRE_DRIFT）— 最優先
2. 09_d 資訊控制檢查（INFO_CONTROL）
3. 09_h 對話張力檢查（DRAMATIC_TENSION）— v1.1 新
4. 09_b 角色聲線一致性（VOICE_CONSISTENCY）
5. 09_g 節奏感檢查（RHYTHM）— v1.1 新
6. 09_a AI 味檢查（AI_FLAVOR）
7. 09_c 禁用詞檢查（FORBIDDEN_WORD）
8. 09_i 跨場一致性檢查（CROSS_SCENE_CONTINUITY）— v1.1 新（最後）
```

## 4.2 qa_decision 計算

- **PASS：** 8 份全 PASS
- **FAIL：** 任一份 FAIL
- **ARBITRATE_REQUIRED：** 人類保留違規亮點（在 09_e 標）

## 4.3 FINAL gate logic

需 9 種 status 齊全（8 QA + 09_e final-gating 紀錄）。

---

# 5. 09_e 定稿變更紀錄（不是 QA）

09_e 是「人類在 final-gating 時填」的紀錄。**`/qa` skill 不產生 09_e**。

兩種用途：

1. **QA 通過後升 FINAL** 前的人類裁決紀錄（保留違規亮點理由）
2. **LOCKED → DEPRECATED 降級時**的降級紀錄（理由 / 日期 / 操作人 / 影響）

詳見 SPEC §16a + §12.7。

---

# 6. Layer 3 Export — A1 prompt 流程

不是 skill — 走前端 Export Panel：

```
1. 前端開 Export Panel
2. 選範圍 / 格式 / 推送方式
3. 點「複製 Prompt」
4. 切到 Claude Code 貼上
5. agent 跑 export → 產 export/<instance>_<date>.{json,md}
6. JSON 給下游工種（程式 / 翻譯 / 配音）
```

詳見 [05 前端工具](05_frontend_tools.md) Export Panel 章節 + `_design/L3_EXPORT_PROMPT_SCHEMA.md`。

---

# 7. 待補內容（隨 Phase D 補）

- [ ] /scene-task 完整範例（任務包必填 20 欄）
- [ ] /dialogue-write 4 種模式完整範例
- [ ] /qa 8 份 QA 各自命中範例
- [ ] 09_e 填寫範例
- [ ] Z1 三欄並排挑亮點 UI 互動
- [ ] LOCKED 降級完整流程範例
- [ ] 多場景並行的衝突處理範例
