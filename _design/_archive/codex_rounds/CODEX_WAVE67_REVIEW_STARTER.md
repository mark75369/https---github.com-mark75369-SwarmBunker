狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-20  
適用範圍：Phase B Wave 6 + Wave 7 整合 CODEX review checkpoint  
優先級：高

# CODEX_WAVE67_REVIEW_STARTER — Wave 6 + Wave 7 整合 review checkpoint

# 0. 本檔用途

對 master 第六輪延伸落地的 **Wave 6（4 protocol D-047 patch）** + **Wave 7（6 個 /create-* skill SKILL.md）** 跑正式 CODEX review，在 B.9 Phase B 整體驗收前 catch 任何偏離 starter 規範 / spec 對齊 / 邊界違反問題。

**對齊 Wave 2 review 模式** — Round 1 結果可能是 GO / NEAR-GO / NO-GO；NO-GO 開修補 round → Round 2 重審；NEAR-GO 修補殘留後接受。

**reviewer 限定 scope：** 只審 Wave 6 + Wave 7 落地檔；不重審 Phase A / Wave 1-5 / D-001~D-049 拍板已 RESOLVED 議題。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「Wave 6 + Wave 7 整合 review checkpoint」 — 對 Wave 6 4 protocol patch 與 Wave 7 6 個 SKILL.md 跑 NO-GO/PARTIAL/GO 判定。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 本輪只判定 Wave 6 / Wave 7 是否對齊各自 starter 規範 + spec；不擅自修補
- 對齊傳統：Wave 2 review Round 1 模式（NO-GO / NEAR-GO / GO 判定）

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何檔（reviewer 限定 — 只看不改）
- ✗ **不**重審 Phase A / Wave 1-5 / D-001~D-049 已 RESOLVED 議題
- ✗ **不**對 master sandbox vs Windows baseline 差異提爭議（屬 §6.11.7 已拍板）
- ✗ **不**修補 check_paths 既有 226 老式檔名 reference（屬 Template 設計遺留，POST_LOCK_PENDING NEW_REQ_9 DEFERRED）

**本 task scope（嚴格限定）：**

### 審查維度

**維度 1：Wave 6 4 protocol D-047 patch（4 檔）**

對齊 `_design/CODEX_WAVE6_PROTOCOLS_PATCH_STARTER.md` line 19 之 starter 規範：

| Protocol | 對應 yaml key | 議題數 (core) | 必驗 |
|---|---|---|---|
| 00_l_關係創建協議 | 00_l_relationship | 6 | header v0.2 + §2 + §4.0 + §4.1 + 議題數 6 |
| 00_f_角色創建協議 | 00_f_character | 8 | header v0.2 + §2 + §4.0 + §4.1 + 議題數 8 + 殘留「9 議題」0 命中 |
| 00_g_大綱創建協議 | 00_g_outline | 6 | header v0.2 + §2 + §4.0 + §4.1 + 議題數 6 + 殘留「7 議題」0 命中 |
| 00_h_細綱創建協議 | 00_h_detailed_outline | 6 | header v0.2 + §2 + §4.0 + §4.1 + 議題數 6 + 殘留「7 議題」0 命中 |

每 protocol 必驗 5 項：
1. **header：** 狀態：DRAFT / 版本：v0.2（D-047 對齊註記）/ 最後更新：2026-05-20 / 5 必填欄齊
2. **§2 啟動條件加 issue registry 條目：** 含 `<instance_root>/issue_type_registry.yaml` 可讀 + Template fallback + schema 異常拒絕
3. **§4.0 議題清單動態構建段：** 對應 skill key（00_l_relationship / 00_f_character / 00_g_outline / 00_h_detailed_outline）+ 6 條 core/user_extensions/core_overrides 規則 + Registry 異常處理
4. **§4.1 議題順序預設表：** 5-column（順序 / 議題 / required_level / locked / 為什麼這時問）+ 議題數對齊 issue_type_registry.template.yaml v0.1
5. **既有「N 個議題」舊寫法 supersede：** grep「9 個議題」/「9 項議題」/「7 個議題」/「7 項議題」應為 0 命中（在對應 protocol）

**維度 2：Wave 7 3 主 SKILL.md（依 ARCH §3.3）**

對齊 `_design/CODEX_WAVE7_SKILLS_STARTER.md` line 19 之 starter 規範：

| Skill | 對應 protocol | 議題 yaml key | 觸發語 | entity 命名 |
|---|---|---|---|---|
| create-character | 00_f v0.2 | 00_f_character | /create-character <name> | C-<name> |
| create-relationship | 00_l v0.2 | 00_l_relationship | /create-relationship <a> <b> | R-<a>-<b> |
| create-outline | 00_g v0.2 | 00_g_outline | /create-outline | P |

每主 SKILL.md 必驗 7 項：
1. **frontmatter：** name + description（50-200 字描述）
2. **中文 5 必填 header**
3. **5 階段流程對應對應 protocol v0.2 §3-§7**（不擅自加減階段）
4. **啟動前檢查含 D-049 Template-detect 兩道防線**（`.template_root` marker + registries inference）+ Bootstrap completed check（D-042 phase_log.bootstrap completed）+ 上游 entity REVIEW check（C 需 W/V 至少 REVIEW；R 需 C；P 需 W/V）
5. **議題清單動態載入段含 D-047 機制**：對應 yaml skill key + Template fallback + 完整提問腳本 ref UD §1.x.2
6. **phase_log schema：** created_entities **單數逐筆**（不是空陣列 / 不是 list of list）+ status: completed（D-042）+ skill: /create-<x>
7. **邊界明示禁止：** 跨 Phase 寫檔 / 自動 trigger 下游 / 修改 00_protocol/ / 在已有同名 entity 上重寫（衝突 → 拒絕）

**維度 3：Wave 7 3 中文 wrapper（極簡）**

每 wrapper 必驗 3 項：
1. **frontmatter：** name（中文）+ description（指向英文主檔）
2. **中文 5 必填 header**
3. **不展開第二套流程**：主體只說「本 wrapper 觸發英文 skill 同樣流程；以英文主檔為權威；不覆寫規則」（約 10-20 行 markdown body）

**維度 4：嚴禁項**

| 嚴禁 | 來源 |
|---|---|
| `.claude/skills/<name>/INVOKE.md` 0 命中 | D-048 否決候選 a |
| 0 個既有 SKILL.md 被改（init-project / create-world / status / check-gaps + 4 中文 wrapper） | 邊界 |
| 0 個 protocol 被改（含本輪 Wave 6 patch 後的 00_f/00_l/00_g/00_h v0.2 — 不再改）| 邊界 |
| 0 個既有 spec 被改 | 邊界 |
| `python scripts/check_headers.py` 0 ERROR 維持 | baseline |

### Review 報告結構

新建 `_design/CODEX_WAVE67_REVIEW_REPORT.md`（v0.1 DRAFT；5 必填中文 header）：

```markdown
# CODEX_WAVE67_REVIEW_REPORT

## 0. 摘要

- 結論：GO / NEAR-GO / NO-GO
- 維度 1（Wave 6 4 protocol）：✓ / △ / ✗ 各檔 result
- 維度 2（Wave 7 3 主 SKILL.md）：✓ / △ / ✗ 各檔 result
- 維度 3（Wave 7 3 中文 wrapper）：✓ / △ / ✗ 各檔 result
- 維度 4（嚴禁項）：✓ / ✗
- 重要 finding 數：N（其中 Critical X / Major Y / Minor Z）

## 1. 審查範圍

- Files Read（含具體 line range）
- Files NOT Modified（reviewer 邊界）

## 2. 維度 1 Wave 6 4 protocol 逐項驗證

### Review-W6-00_l
- 狀態：✓ / △ / ✗
- 必驗 5 項逐項 + 證據引用（line 號）+ 殘留 0 命中 grep 結果
- 殘留 / finding：[列舉]

### Review-W6-00_f / 00_g / 00_h（同上結構）

## 3. 維度 2 Wave 7 3 主 SKILL.md 逐項驗證

### Review-W7-create-character
- 狀態：✓ / △ / ✗
- 必驗 7 項逐項 + 證據引用
- 殘留 / finding：[列舉]

### Review-W7-create-relationship / create-outline（同上結構）

## 4. 維度 3 Wave 7 3 中文 wrapper 逐項驗證

| wrapper | frontmatter | 5 欄 header | 極簡 + 指向主檔 | 結論 |
|---|---|---|---|---|
| 建立角色 | ✓/✗ | ✓/✗ | ✓/✗ | PASS/△/FAIL |
| 建立關係 | ✓/✗ | ✓/✗ | ✓/✗ | PASS/△/FAIL |
| 建立大綱 | ✓/✗ | ✓/✗ | ✓/✗ | PASS/△/FAIL |

## 5. 維度 4 嚴禁項

| 嚴禁 | 結果 |
|---|---|
| .claude/skills/**/INVOKE.md 0 命中 | ✓/✗ |
| 既有 8 SKILL.md 未動 | ✓/✗ |
| 4 protocol 未再改 | ✓/✗ |
| 既有 _design/ spec 未動（除本輪 Wave 6 patch 紀錄外）| ✓/✗ |
| check_headers 0 ERROR | ✓/✗ |

## 6. 新發現的 finding

對每 finding 列：
- ID（如 W6-F-01 / W7-F-02）
- 嚴重度（Critical / Major / Minor）
- 影響（什麼壞 / 哪些檔 / 哪些 spec ref）
- 修補建議

## 7. Go / NEAR-GO / No-Go 決定

- **GO：** 維度 1-4 全 ✓ + finding 全 Minor 或 0
- **NEAR-GO：** 維度 1-4 大多 ✓ + 1-2 △ + finding ≤ 2 Major
- **NO-GO：** 維度 1-4 任一 ✗ 或 ≥ 3 Major finding 或 1+ Critical finding

## 8. Source Limitations

- 環境差異（如 Windows vs sandbox path resolution）紀錄
- 未跑的 verify 命令說明（如不跑實機 /create-character 寫檔測試）
```

---

**必讀文件（按順序）：**

A. 任務權威來源
1. `_design/CODEX_WAVE6_PROTOCOLS_PATCH_STARTER.md`（Wave 6 starter 規範）
2. `_design/CODEX_WAVE7_SKILLS_STARTER.md`（Wave 7 starter 規範）

B. 對齊基準
3. `_design/DECISIONS_LOG.md` v1.4 §6.9.2 D-047 + §6.11.2 D-049 + §6.11.7 baseline 校正
4. `_design/ARCHITECTURE.md` v1.5 §3.3 / §3.3.0 / §3.3.2
5. `_design/SPEC.md` v1.2 §5.1 / §5.4
6. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2 phase_log schema
7. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.2 / §1.3 / §1.5
8. `_design/registries/issue_type_registry.template.yaml` v0.1（議題清單 source）

C. 審查對象
9. `00_protocol/00_l_關係創建協議.md` v0.2
10. `00_protocol/00_f_角色創建協議.md` v0.2
11. `00_protocol/00_g_大綱創建協議.md` v0.2
12. `00_protocol/00_h_細綱創建協議.md` v0.2
13. `.claude/skills/create-character/SKILL.md` + 建立角色/SKILL.md
14. `.claude/skills/create-relationship/SKILL.md` + 建立關係/SKILL.md
15. `.claude/skills/create-outline/SKILL.md` + 建立大綱/SKILL.md

D. Reference templates
16. `00_protocol/00_e_世界觀創建協議.md` v0.2（Wave 6 patch 模板基準）
17. `.claude/skills/init-project/SKILL.md` v0.2（Wave 7 D-049 範式基準）
18. `.claude/skills/create-world/SKILL.md`（Wave 7 D-047 動態載入範式基準）

E. 嚴禁區（reviewer 不可動）
19. 所有檔（reviewer 限定 — 只看不改）
20. 唯一允許新建：`_design/CODEX_WAVE67_REVIEW_REPORT.md`

---

**你要交付的產物：**

1 個檔：
1. `_design/CODEX_WAVE67_REVIEW_REPORT.md`（v0.1 DRAFT）

**驗收條件：**

A. 檔結構
- review 報告存在 + 5 必填中文 header + §0-§8 段全部
- GO / NEAR-GO / NO-GO 決定明確

B. 內容
- 維度 1-4 全部逐項驗證 + 證據引用
- finding 全部列舉 + ID + 嚴重度 + 修補建議
- Source limitations 列舉

C. 不破壞
- 沒動任何審查對象檔（reviewer 限定）
- `python scripts/check_headers.py` 0 ERROR 維持

---

**Go / Done 判定指引：**

- **Review 報告 DONE** = A/B/C 全 ✓
- 不要擅自修補任何發現的 finding（屬下一輪 patch round task）
- 對 Wave 6 / Wave 7 給最終 GO / NEAR-GO / NO-GO 判定

請開始。
```

---

# 2. 完成條件 + 後續

CODEX review 完成 → user commit/push → 回 master（本輪或第七輪 master）→
- **GO：** 直接進 Wave 8（B.7 / B.8 / B.9）；review consolidation 涵蓋
- **NEAR-GO：** 修補殘留（master inline patch / 短 CODEX patch round）→ 進 Wave 8
- **NO-GO：** 開 CODEX_WAVE67_PATCH_STARTER.md → 修補 → Round 2 review → GO 後進 Wave 8

---

# 3. 文件維護紀律

- 本檔是 CODEX Wave 6+7 review checkpoint 啟動包；完成後可 archive 進 `_design/archive/`
- review 報告 `CODEX_WAVE67_REVIEW_REPORT.md` 屬「review 事實檔」（同 Wave 2 review report）— Round 2 重審時可追加 entry
- 不對 master sandbox vs Windows baseline 差異提爭議（屬 §6.11.7 已拍板）
