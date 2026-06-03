狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：階段 7 升 LOCKED + DECISIONS_LOG v1.0 + Phase A.0.1 任務描述定稿 checklist  
優先級：最高  

# STAGE_7_LOCKED_UPGRADE_CHECKLIST — 升 LOCKED 操作清單

# 0. 本檔用途

Master 第四輪整合對話完成階段 1-6（含 CODEX (d) 短審通過）後，**user 或下個 master 對話**依本檔執行階段 7：升 LOCKED + DECISIONS_LOG v1.0 + Phase A.0.1 確認。

**前置條件（必須先完成）：**

- ✓ 階段 1：INTEGRATION_CONTRACTS v2.0 正式版產出（1777 行）
- ✓ 階段 2：主 SPEC v1.1 partial supersede 完成
- ✓ 階段 3：主 ARCHITECTURE v1.2 partial supersede 完成
- ✓ 階段 4：主 TASKS v1.3 partial supersede 完成
- ✓ 階段 5：PHASE_3_COMPLETION_REPORT v4.0 FINAL
- ⏸ 階段 6：CODEX (d) 短審查 clean 或修補完成（CODEX_REVIEW_REPORT_D.md 產出 + master 處理完所有必修項）
- ⏸ Sandbox virtiofs cache 不穩 → 所有 commit 由 user 手動執行（不依賴 sandbox bash）

---

# 1. 階段 7 步驟（按順序）

## 1.1 Step 1：CODEX (d) 報告處理（如有必修項）

- 讀 `_design/CODEX_REVIEW_REPORT_D.md`
- 對「必修」項目逐一修補（多半是 partial supersede 落地缺漏）
- 修補完成後再跑一輪 CODEX (d) 短審 confirm clean，或 user 拍板「可進」

**若 CODEX (d) 找出 critical 衝突 → 升 user 拍板，可能要再開新對話。**

## 1.2 Step 2：所有 spec / SPEC / ARCH / TASKS / INTEGRATION_CONTRACTS 升 LOCKED

逐檔在 frontmatter 中文 header `狀態` 欄位改：

| 檔 | 從 | 到 |
|---|---|---|
| `_design/DATA_FORMAT_SPEC.md` | DRAFT | **LOCKED** |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | DRAFT | **LOCKED** |
| `_design/UX_SPEC.md` | DRAFT | **LOCKED** |
| `_design/L3_EXPORT_PROMPT_SCHEMA.md` | DRAFT | **LOCKED** |
| `_design/INTEGRATION_CONTRACTS.md` | REVIEW | **LOCKED** |
| `_design/SPEC.md` | REVIEW | **LOCKED** |
| `_design/ARCHITECTURE.md` | REVIEW | **LOCKED** |
| `_design/TASKS.md` | REVIEW | **LOCKED** |
| `_design/PHASE_3_COMPLETION_REPORT.md` | FINAL | **LOCKED**（FINAL 已是最高態；可選擇維持 FINAL）|

**注意：** REQUIREMENTS_LOCK.md 已是 FINAL，不動。

## 1.3 Step 3：DECISIONS_LOG v0.8 → v1.0 升版

開 `_design/DECISIONS_LOG.md`：

1. 在 frontmatter 改版本 `v0.8` → `v1.0`
2. 改狀態 DRAFT → **FINAL**
3. 在 §6 末尾新增 §6.8 段：

```markdown
## 6.8 Master 第四輪整合完成 + 升 LOCKED 紀錄（v1.0，YYYY-MM-DD）

**升版觸發：** master 第四輪整合對話完成階段 1-7；所有 spec / 主 SPEC/ARCH/TASKS / INTEGRATION_CONTRACTS 已標 LOCKED；可進 Phase A.0.1 實作。

**v0.8 → v1.0 變動摘要：**

- 三 specialist v0.3 patch + master 第四輪整合的 partial supersede 全部落地
- INTEGRATION_CONTRACTS v2.0 正式版完成
- 主 SPEC v1.1 / ARCH v1.2 / TASKS v1.3 partial supersede 完成
- PHASE_3_COMPLETION_REPORT v4.0 FINAL
- D-001 ~ D-046 全部對齊主文件 + 對應 partial supersede 標註
- P-021 ~ P-026 RESOLVED via D-037~D-046
- P-027 ~ P-030 進 INTEGRATION_CONTRACTS §6.4 Pending（後續細化）

**升 v1.0 後紀律：**

- 不再加新 D-NNN — 新議題另寫新 D 編號（D-047+）
- 主 SPEC / ARCH / TASKS 已 LOCKED — 動 LOCKED 段必走 supersede 機制
- 後續修訂走 v1.x partial supersede + 對應 D-NNN
- Phase A.0+ 實作期間若發現設計缺漏 → 升 master 第五輪整合對話
```

4. 在 §11.1 編號變更歷史補：

```markdown
| **v1.0（升 LOCKED — master 第四輪整合完成 + CODEX (d) clean）** | 不再加 D-NNN；新議題另寫 | — |
```

## 1.4 Step 4：Phase A.0.1 任務描述確認

讀 `_design/TASKS.md` §A.0.1 — 確認任務描述完整：

- ✓ 依賴清楚（無依賴 — 是 Phase A.0 第一個 task）
- ✓ 產出清楚（`scripts/parse_frontmatter.py` + 含 phase_log 完整解析）
- ✓ 做法 4 大段（基線 parser / phase_log 完整解析 / Expected Entity Manifest / Entity-exempt 清單）
- ✓ 驗收 6 項（含 v1.1 新測試）
- ✓ 禁止事項 3 項

若 §A.0.1 任何項不完整 → 補完後升 LOCKED。

## 1.5 Step 5：git commit + push

user **手動執行**（sandbox virtiofs cache 不穩，跳過 sandbox bash commit）：

```bash
# Windows PowerShell 或 git bash 都可
cd D:\劇本開發工具

# 提交本輪所有第四輪整合產出
git add _design/

git commit -m "Master 4th-round integration complete: \
INTEGRATION_CONTRACTS v2.0 (1777 行) + \
SPEC v1.1 / ARCH v1.2 / TASKS v1.3 partial supersede + \
PHASE_3_COMPLETION_REPORT v4.0 FINAL + \
CODEX_REVIEW_STARTER_D + \
STAGE_7_LOCKED_UPGRADE_CHECKLIST + \
DECISIONS_LOG v1.0 + LOCKED 升版 — \
Phase A.0 啟動條件全達成"

git push origin master
```

## 1.6 Step 6：宣告 Phase A.0 可啟動

- `_design/PHASE_3_COMPLETION_REPORT.md` §6.2 全 ✓
- `_design/PHASE_3_COMPLETION_REPORT.md` §6.2a 4 項全 ✓（含 CODEX (d) clean）
- 開新對話 / 接續對話啟動 Phase A.0.1（frontmatter parser 基線 + phase_log 完整解析）

---

# 2. 升 LOCKED 後的修訂紀律（明示）

| 修訂類型 | 處理 |
|---|---|
| 動 LOCKED 段內容 | 走 supersede 機制（DECISIONS_LOG §7）+ 加 v1.x partial supersede 標註 |
| 加新 D-NNN | D-047+；對齊既有編號慣例 |
| Pending 條目解決 | 在 INTEGRATION_CONTRACTS §8 後續更新區記錄 v2.x 升版 |
| user 提新需求 | 開新 Bucket 討論；可能觸發 master 第五輪整合對話 |
| CODEX 後續審查 | (e) / (f) 等下輪審查依需要觸發 |

---

# 3. 階段 7 完成後的狀態快照（期望）

```
_design/ 結構（升 LOCKED 後）：

LOCKED 文件：
- REQUIREMENTS_LOCK.md（v1.0 FINAL 維持）
- DATA_FORMAT_SPEC.md（v0.2 LOCKED）
- UPSTREAM_DOWNSTREAM_SPEC.md（v0.3 LOCKED）
- UX_SPEC.md（v0.3 LOCKED）
- L3_EXPORT_PROMPT_SCHEMA.md（v0.1 LOCKED）
- INTEGRATION_CONTRACTS.md（v2.0 LOCKED）
- SPEC.md（v1.1 LOCKED）
- ARCHITECTURE.md（v1.2 LOCKED）
- TASKS.md（v1.3 LOCKED）
- PHASE_3_COMPLETION_REPORT.md（v4.0 FINAL → LOCKED）

DECISIONS_LOG.md（v1.0 FINAL — D-001 ~ D-046）

啟動包 / 歷史紀錄：
- HANDOFF_TO_4TH_INTEGRATION_MASTER.md（已執行完）
- CODEX_REVIEW_STARTER.md（CODEX (c) 已執行）
- CODEX_REVIEW_STARTER_D.md（CODEX (d) 已執行）
- CODEX_REVIEW_REPORT.md（CODEX (c) 報告）
- CODEX_REVIEW_REPORT_D.md（CODEX (d) 報告）
- STAGE_7_LOCKED_UPGRADE_CHECKLIST.md（本檔；可選擇 archive）

archive（建議）：
- INTEGRATION_CONTRACTS_v2_SKELETON.md → archive/
- HANDOFF_TO_4TH_INTEGRATION_MASTER.md → archive/
- STAGE_7_LOCKED_UPGRADE_CHECKLIST.md → archive/

可進 Phase A.0：
- A.0.1 ~ A.0.9 parser 9 大類 tasks
- A.0F.0 ~ A.0F.11 frontend 工具 tasks
- A.4 既有 27 模板 frontmatter 補完
- A.5 init-project + Template registry 拷貝
- 其他 Phase A 既有 tasks
```

---

# 4. 文件維護紀律

- 本檔是「階段 7 操作 checklist」；user 或下個 master 對話執行完 → 可 archive
- 階段 7 完成後若發現本檔不準確處 → 補 errata（不刪除原內容）
