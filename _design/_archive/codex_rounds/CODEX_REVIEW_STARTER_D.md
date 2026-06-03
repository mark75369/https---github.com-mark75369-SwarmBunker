狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：CODEX 第四輪短審查 (d) 啟動包 — 只看 v2 contracts + 主 SPEC/ARCH/TASKS 一致性  
優先級：高  

# CODEX_REVIEW_STARTER_D — Master 第四輪整合產出後的 CODEX (d) 短審查

# 0. 本檔用途

當 master 第四輪整合對話完成階段 1-5（INTEGRATION_CONTRACTS v2.0 + 主 SPEC v1.1 + ARCH v1.2 + TASKS v1.3 + PHASE_3_COMPLETION_REPORT v4.0 FINAL）後，把本檔 §1 內的 prompt 整段複製貼到新 CODEX 對話，啟動「**v2 contracts + 主 SPEC/ARCH/TASKS 一致性短審查**」（時序對應 master 規劃的「(d) 時機」）。

**本檔跟 CODEX_REVIEW_STARTER.md（c）的差別：**

| 維度 | (c) starter | **(d) starter（本檔）** |
|---|---|---|
| 觸發時機 | specialist v0.2 第二輪交付後 + 第四輪整合前 | **第四輪整合 partial supersede 完成後 + 升 LOCKED 前** |
| Scope | 全 14 份文件深度審查（含三 spec v0.2 內部一致性 + 跨 spec 衝突 17 條 + 越界 5 條）| **只看 v2 contracts + 主 SPEC/ARCH/TASKS 一致性**（**不重審**三 spec v0.3 內部） |
| 預估 CODEX 時數 | 4-6 小時（找 17 衝突 + 越界）| **2-3 小時**（驗證 partial supersede 落地一致性 + Pending 殘留） |
| 預期產出 | CODEX_REVIEW_REPORT.md（17 衝突 + 5 越界）| **CODEX_REVIEW_REPORT_D.md**（新衝突 / 落地缺漏 / Pending 對齊） |

**搭配傳統：** 跟之前 SPEC/ARCH/TASKS 經歷的 4 輪 CODEX 審查模式對齊。本輪是「master 第四輪整合 + v0.3 patch + (c) 收斂後」的第 6 輪 CODEX 審查。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX deep-review agent。

本輪是「master 第四輪整合對話完成 partial supersede 後、升 LOCKED 前」的**短審查（(d) 時機）**。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 main / master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer，不是 implementer — 本輪不寫實作檔
- 你是 cross-spec auditor — 檢視 master 第四輪整合的 partial supersede 落地是否一致
- 你是 升 LOCKED 前的 final-check — clean 後 master 第七階段可升 LOCKED
- 對應傳統：本輪是第 6 輪 CODEX 審查（前 5 輪：時期 A 4 輪 + (c) 1 輪）

**重要邊界（v0.3 patch 已 lock — 不要重審）：**

- ✗ **不**重審 DATA_FORMAT_SPEC v0.2 / UPSTREAM_DOWNSTREAM_SPEC v0.3 / UX_SPEC v0.3 內部一致性（CODEX (c) 已審 + master 第四輪 D-037~D-046 收斂）
- ✗ **不**重新提出 17 衝突 / 5 越界（CODEX_REVIEW_REPORT.md 已記）
- ✗ **不**動 D-001 ~ D-046 拍板結論
- ✗ **不**動 REQUIREMENTS_LOCK.md（v1.0 FINAL）

**本輪 scope（嚴格限定 4 大類）：**

1. **v2 contracts 內部一致性** — `_design/INTEGRATION_CONTRACTS.md` v2.0 中 Contract A.1~A.8 / B.1~B.8 / C.1~C.5 的 schema 是否互相對齊
2. **主 SPEC v1.1 partial supersede 落地驗證** — 7 段（§5.1 / §5.2.3 / §5.2.4 / §5.4 / §12 / §13a / §14a / §16a）的 v1.1 標註是否：
   - 對齊 D-NNN
   - 沒有打破 LOCKED 段落順序
   - 北極星理由清楚
3. **主 ARCH v1.2 + TASKS v1.3 partial supersede 落地驗證** — 新章節 / 新 task 是否：
   - 對齊 INTEGRATION_CONTRACTS v2.0
   - 對齊 SPEC v1.1
   - 沒有引入新衝突
4. **Pending 殘留分派** — INTEGRATION_CONTRACTS §6 Pending 13 條（UX §9 PENDING）+ 12 條（UD §9）+ 4 條（P-027~P-030）是否清楚分派到正確目的地

---

**必讀文件（按順序，最新權威優先）：**

A. 最高權威 — 需求 + 決策層
1. _design/REQUIREMENTS_LOCK.md（v1.0 FINAL — 4 bucket 拍板的需求快照；不審；當對齊基準）
2. _design/DECISIONS_LOG.md（含 D-001~D-046 + P-001~P-030；§6.7 P0/P1 拍板紀錄；不審；當對齊基準）

B. 本輪審查對象（核心）— Master 第四輪整合產出
3. _design/INTEGRATION_CONTRACTS.md（**v2.0 — 本輪審查核心；1777 行**）
4. _design/SPEC.md（**v1.1 — 7 段 partial supersede**）
5. _design/ARCHITECTURE.md（**v1.2 — 新 §4.2a / §12 / §13**）
6. _design/TASKS.md（**v1.3 — A.0 → 9 大類 / A.0F 新增 / D.1a 新增 / C.5a 新增**）
7. _design/PHASE_3_COMPLETION_REPORT.md（**v4.0 FINAL**）

C. 三 specialist v0.3 patch（**對齊基準，不重審**）
8. _design/DATA_FORMAT_SPEC.md（v0.2；DF 命名 v0.2 但實質與 UD/UX v0.3 同輪次）
9. _design/UPSTREAM_DOWNSTREAM_SPEC.md（v0.3）
10. _design/UX_SPEC.md（v0.3）
11. _design/L3_EXPORT_PROMPT_SCHEMA.md（v0.1，master 上輪新建；contract 級）

D. 歷史紀錄（給 context；不重審）
12. _design/CODEX_REVIEW_REPORT.md（CODEX (c) 17 衝突 + 5 越界紀錄；多數 RESOLVED via D-037~D-046）
13. _design/HANDOFF_TO_4TH_INTEGRATION_MASTER.md（master 第四輪接手指南）

---

**你要交付的產物：**

新建：`_design/CODEX_REVIEW_REPORT_D.md`

報告格式：

```markdown
狀態：DRAFT  
版本：v0.1  
最後更新：YYYY-MM-DD  
適用範圍：CODEX 第四輪短審查 (d) 報告 — v2 contracts + 主 SPEC/ARCH/TASKS 一致性  
優先級：高  

# CODEX_REVIEW_REPORT_D — Master 第四輪整合 partial supersede 落地審查

## 0. 摘要（結論一句話 + 整體判斷）

## 1. 審查範圍

### 1.1 Files Read
（列你實際讀的檔案 + 行數）

### 1.2 Files NOT Modified
（明示沒動的檔案 — 你是 reviewer 不是 implementer）

## 2. 衝突清單（如有）

對每個衝突依 CODEX (c) 格式列：
- 編號：CC-NN（"Cross-spec Critical" 或 "Cross-spec Conflict" 第 d 輪）
- 嚴重度：critical / major / minor
- 涉及檔
- 問題（具體 line ref）
- 影響
- 建議（master 應該怎麼處理）

## 3. Partial supersede 落地缺漏清單（如有）

對每個缺漏列：
- SPEC / ARCH / TASKS 哪一段
- 該段 partial supersede 對應 D-NNN
- 缺漏內容（如「mode_tag SINGLE_ITER 加進 §5.2.4 但 §5.4 phase_log 範例沒同步補 base_dialogue 欄位」）
- 建議補法

## 4. Pending 殘留分派檢查

對 INTEGRATION_CONTRACTS §6 各 Pending 條目：
- 條目是否真的分派清楚（owner + phase）
- 是否有條目被遺漏（具體 line ref）

## 5. 給 master 第四輪整合的修補建議

依優先級排：
- **必修**（critical / 升 LOCKED 前必處理）
- **建議修**（major / 影響 Phase A.0 但不擋 LOCKED）
- **可延後**（minor / 後續細化即可）

## 6. 升 LOCKED 條件評估

對 Phase A.0 啟動條件（PHASE_3 §6.2a 4 項）：
- 哪些已 ready
- 哪些需修補後才 ready

## 7. 後續審查建議

如本輪審查後仍有未解項，建議下次審查 scope。
```

---

**你不做的事（再次重申）：**

- ✗ 不寫實作檔（00_protocol / 09_quality_assurance / scripts / .claude/skills 等）
- ✗ 不改既有 spec / SPEC / ARCH / TASKS / INTEGRATION_CONTRACTS 任何內容
- ✗ 不重審 specialist v0.3 spec 內部
- ✗ 不重新拍板 D-001~D-046 結論
- ✗ 不提新需求

---

**估時：**

- 讀 14 份文件：30-45 分（focus 在 partial supersede + Contracts v2 + Pending）
- 寫報告：1-1.5 小時
- **總估時 2-2.5 小時**

審查完成後直接 commit 報告檔 + push。master 第四輪整合對話讀完報告後做最後修補 + 升 LOCKED（階段 7）。
```

---

# 2. 預期審查結論的可能類型

依過往 CODEX 審查經驗，本輪可能的結論：

| 結論類型 | 觸發 |
|---|---|
| **A: clean — 0 critical** | partial supersede 落地完整一致 → master 可直接進階段 7 升 LOCKED |
| **B: 1-3 個 major 缺漏** | 多半是「某 D-NNN 在 SPEC 標了但 ARCH / TASKS 沒同步」— master 一次性補修，30 分內處理完，仍升 LOCKED |
| **C: 1+ 個 critical 衝突** | 罕見（D-037~D-046 收斂已對齊大部分）— 升 user 拍板，可能要再開新對話 |

**過往機率分布（依 CODEX (c) 經驗）：**
- A：30%
- B：60%
- C：10%

---

# 3. 對 v2 contracts 的具體審查 checklist（給 CODEX 參考）

CODEX 在審查時可以對照本 checklist 系統性走過：

## 3.1 Contract A 8 條 — schema 內部對齊

- [ ] A.1 dialogue_keys Map shape — DF §4.2 + UD §2.11.4 + UX §11.3.5 三邊欄位完全一致？
- [ ] A.2 phase_log 8 欄位 — DF §3 + UD §6/§10.6 + SPEC §5.4 + SPEC §5.4a 一致？
- [ ] A.3 A-* metadata SoT = `10_art_assets/` — DF §5 + UD §13.2.1（v0.3）+ UX §11.1.6a + SPEC §5.1a 一致？
- [ ] A.4 KEY status enum — DF §4.5 + UD §2.11.5 + UX §7.9.2 + Contract C.2 一致？
- [ ] A.5 qa_type 8 + registry — DF §6.2/§8 + UD §2.5/§3.1-§3.9 + SPEC §5.2.4 + SPEC §12.7 一致？
- [ ] A.6 mode_tag SINGLE_ITER + base_dialogue — DF §6.1/§3.3d + UD §4.7/§4.5 + SPEC §5.2.4 + SPEC §5.4a 一致？
- [ ] A.7 JSON `manifest + records[]` — DF §9 + UD §12.6/§12.7 + SPEC §13a + L3_EXPORT_PROMPT_SCHEMA 一致？
- [ ] A.8 trust-level 限上游 — DF §3.3 + UD §10.3（v0.3） + UX §7.9.1 一致？

## 3.2 Contract B 8 條 — pipeline ↔ UI 對齊

- [ ] B.1 UX-1~80 全覆蓋 — UD §7 + §10/§11/§12/§13 + UX §7.8/§7.9 對照表完整？
- [ ] B.2 Save race guard — UX §11.5.7-9 + SPEC §16a + ARCH §13.2 endpoint 一致？
- [ ] B.3 Export Prompt panel — UX §11.6.11 + L3_EXPORT_PROMPT_SCHEMA + ARCH §4.2a + TASKS C.5a 一致？
- [ ] B.4 Asset Panel — UX §11.1.6a + SPEC §5.1a + ARCH §13.2 endpoint 6/7 一致？
- [ ] B.5 8 QA execution order — UD §2.5.3 + UX §6 + TASKS D.4（v1.1）+ ARCH §6.3（v1.2）一致？
- [ ] B.6 KEY status enum dropdown — UX §11.3.5 + Contract A.4 一致？
- [ ] B.7 trust-level 無前端 UI 選 — UX §7.9.1 UX-67 + Contract A.8 一致？
- [ ] B.8 Conflict modal 4 選項 — UX §7.9.1 UX-66 + §11.7.6 + Contract A.8 conflict_resolutions 一致？

## 3.3 Contract C 5 條 — DF ↔ UX adapter

- [ ] C.1 A-* subtype 7 → UI — DF §5.1a + UX §11.1.6a/§11.3.5/§11.4 一致？
- [ ] C.2 KEY status enum → UI — DF §4.5 + UX §11.3.4-5 一致？
- [ ] C.3 JSON records[] → 前端不消費 — ARCH §4.2a + UD §12.7 + UX §11.8.3 一致？
- [ ] C.4 phase_log new fields → /status — DF §3 + UX §11.1.6/§11.3.5 一致？
- [ ] C.5 A-* completeness 不入 narrative status — DF §5.6 + UX §11.1.6a.2 + Contract B.4 一致？

## 3.4 主 SPEC v1.1 partial supersede 7 段

- [ ] §5.1 / §5.1a / §5.1b — A-* + 可擴充 registry 完整？
- [ ] §5.2.3 — dialogue_keys / art_metadata 兩列加在表末（不打破順序）？
- [ ] §5.2.4 — mode_tag 6 + qa_type 8 標可擴充？
- [ ] §5.4 + §5.4a — phase_log status 升正式 + 5 新欄位範例 + SINGLE_ITER lineage？
- [ ] §12.7 — 5 → 8 份必跑 + 09_e 維持不屬 QA？
- [ ] §13a — Layer 3 Export A1 prompt 新章節 + 不擾既有 4 個 /export-*？
- [ ] §14a — 不存在 skill 不新增 + 既有 4 個不擴 JSON 輸出？
- [ ] §16a — LOCKED → DEPRECATED 走 09_e 不加 frontmatter 三欄位？

## 3.5 主 ARCH v1.2 + TASKS v1.3 partial supersede

- [ ] ARCH §1.2 補 `10_art_assets/` 結構 + `export/` + registry yamls？
- [ ] ARCH §4.2a Layer 3 Export A1 prompt 生成器章節完整？
- [ ] ARCH §6.3 QA 5 → 8 改寫對應 TASKS D.4？
- [ ] ARCH §12 A.0 Parser 9 大類規格對應 TASKS A.0.1-A.0.9？
- [ ] ARCH §13 Frontend Adapter 8 個 endpoint 對應 TASKS A.0F.1？
- [ ] TASKS A.0 → 9 大類 + A.0F 11 個 + A.5 補 registry / `10_art_assets/` / `.gitignore` + D.1a 新 + D.4 8 報告改寫 + C.5a 新？

## 3.6 Pending 殘留分派檢查

- [ ] INTEGRATION_CONTRACTS §6.2 UD Pending 12 條都有 owner + 處理時點？
- [ ] §6.3 UX §9 PENDING 13 條都分派？
- [ ] §6.4 P-027~P-030 都標 phase？
- [ ] §6.5 Pending 分派總覽 7 個目的地涵蓋所有 Pending？

---

# 4. 文件維護紀律

- 本檔是「啟動包」，CODEX (d) 跑完後**不需要更新本檔**
- 若 CODEX (d) 識出本檔不準確的地方，標 errata 在 CODEX_REVIEW_REPORT_D.md
- CODEX (d) 完成後本檔可 archive 進 `_design/archive/`，保留歷史
