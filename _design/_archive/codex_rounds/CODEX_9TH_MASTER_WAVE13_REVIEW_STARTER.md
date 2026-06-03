狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-22  
適用範圍：第九輪 master Wave 13 CODEX implementer 兩輪（D.6 + batch D7-D9）完成後 Wave 13 重審 — 4 個 view-* skill 結構對齊 + D9 D-054 hybrid fallback + 呈現規則 + baseline + protected-area diff  
優先級：高

# CODEX_9TH_MASTER_WAVE13_REVIEW_STARTER — Wave 13 重審

# 0. 本檔用途

9th master 第一段對話流程：cleanup queue → Wave 12 → Round 1-4 review cycle (4 輪 inline patch) → Wave 13 starter set → CODEX D.6 implementer task → CODEX batch D7-D9 implementer task → **本輪 Wave 13 重審驗證 Wave 13 8 個新 SKILL.md 對齊 starter set + ARCH §4.1/§4.4 + UX §7 + D-054 落地 + 無新 regression**。

**前置條件：** 9th master Wave 13 starter set + CODEX D.6 + CODEX batch 全 push 完成。當前 master commit：
- `d0997b8`：Wave 13 starter set + POST_LOCK_PENDING v0.18
- `0b8851f`：D.6 SKILL.md (view-world + 查看世界觀)
- `cff5c06`：D7-D9 SKILL.md (view-character + view-outline + view-detailed-outline + 3 中文 wrapper)

**重審 GO →** 9th master 第二段對話進 Wave 14（採新模式：master 寫 D10 完整 + CODEX batch D11-D13）

**重審 NEAR-GO →** master 拍板 hard-limit accept 或 inline patch

**重審 NO-GO →** 大幅 restructure

⚠ **Scope 嚴格限定：本輪 verify Wave 13 8 個新 SKILL.md ONLY。**

⚠ **教訓 5 條內化（沿用 9th master 第一段）：**
1. Windows baseline 權威
2. Cascade sweep broader pattern
3. SPEC frontmatter 段直接 grep verify
4. Supersede note 避免重複 finding 內精確詞串
5. **Review starter diff anchor 精確** — 本輪用**明示 commit hash** `bb50a54..HEAD`（Round 4 review report 為 anchor；含 Wave 13 完整 3 commits）

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 CODEX reviewer agent。

本輪是「第九輪 master Wave 13 CODEX implementer 兩輪完成後 Wave 13 重審」— 對 Wave 13 新建 8 個 SKILL.md 跑「結構對齊 D6 範本 + D9 D-054 hybrid fallback + 呈現規則 + baseline + protected-area diff + cross-ref sweep」多重檢查，產出 GO / NEAR-GO / NO-GO 判定。

工作資料夾：D:\劇本開發工具 (Template repo)
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 reviewer — 純讀取 / 純檢查；本輪不寫任何 spec / SKILL.md / starter / protocol 修補
- 對應傳統：同 Round 1-4 重審模式但 scope 限縮到 Wave 13 SKILL.md；master 端已內部 verify 4 個英文 view-* SKILL.md 結構對齊 11 段 + D9 D-054 hybrid fallback 完整，但未跑 CODEX 獨立判定；本輪補回 CODEX strict verify
- 對應前置：Wave 13 D.6 + batch implementer task 已完成 + user 已 commit/push（3 個 commit：d0997b8 + 0b8851f + cff5c06）

**重要邊界（嚴格 scope）：**

- ✗ 不改任何檔（純檢查；發現 finding 寫進 review report）
- ✗ 不跑真實 /view-* skill（Template 內無 Instance entity）
- ✗ 不重審 D-001~D-054 拍板結論
- ✗ 不重審 Round 1-4 review cycle 已 accepted finding（R10-MA-01 / R1-MA-02 設計拍板 a / R2-MAJOR-03 hard-limit accept / R4-MAJOR-01 hard-limit accept 等）
- ✗ 不重審 cleanup queue (Task 1-6) / Wave 12 starter set (Task 7) 落地（屬 Round 1-4 cycle 範圍）
- ✗ 不重審 Phase A/B/C 既有 SKILL.md / protocol / spec
- ✗ 不下新 D-NNN 拍板
- ✗ 不開 9th master patch round
- ✓ 可跑技術驗證命令
- ✓ 可建本 review report 1 個檔（_design/CODEX_9TH_MASTER_WAVE13_REVIEW_REPORT.md v0.1）

**本 task scope（嚴格限定 — Wave 13 8 個新 SKILL.md ONLY）：**

依 Wave 13 starter set (`_design/CODEX_D6_STARTER.md` v0.1 + `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1) + CODEX D.6 + batch 兩輪 implementer task 落地：

### Wave 13 新建 8 個 SKILL.md（本輪 verify 對象）

| # | 路徑 | task | commit |
|---|---|---|---|
| 1 | `.claude/skills/view-world/SKILL.md` v0.1 | D.6 英文主檔 | 0b8851f |
| 2 | `.claude/skills/查看世界觀/SKILL.md` v0.1 | D.6 中文 wrapper | 0b8851f |
| 3 | `.claude/skills/view-character/SKILL.md` v0.1 | D.7 英文主檔 | cff5c06 |
| 4 | `.claude/skills/查看角色/SKILL.md` v0.1 | D.7 中文 wrapper | cff5c06 |
| 5 | `.claude/skills/view-outline/SKILL.md` v0.1 | D.8 英文主檔 | cff5c06 |
| 6 | `.claude/skills/查看大綱/SKILL.md` v0.1 | D.8 中文 wrapper | cff5c06 |
| 7 | `.claude/skills/view-detailed-outline/SKILL.md` v0.1 | D.9 英文主檔（含 D-054 hybrid fallback）| cff5c06 |
| 8 | `.claude/skills/查看細綱/SKILL.md` v0.1 | D.9 中文 wrapper | cff5c06 |

### Wave 13 不動段（聲明）

以下檔本輪 **不動**（聲明 + 應由本輪 verify protected-area diff）：

- LOCKED spec / registries / scripts / 27 模板 / 00_protocol/全部 (含 00_j v0.2 / 00_k v0.2)
- 既有 16 個 SKILL.md + Wave 12 starter 對應的 12 個 SKILL.md (尚未實作 - 屬 CODEX D.1-D.5 task；非 9th master 第一段 scope)
- Round 1-4 已落地檔（08_a v0.4 / phase_b_review_log v0.6 / PHASE_B v1.4 / CODEX_B9_STARTER v0.5 / AGENTS.md / CLAUDE.md v0.3 / Wave 12 starter v0.3-0.4）
- 第八輪 review reports + Round 1-4 review reports（屬 immutable history）
- D054_DECISION_PACKAGE / PHASE_A/B/C_COMPLETION_REPORT / HANDOFF_TO_9TH_MASTER
- DECISIONS_LOG v2.0 / POST_LOCK_PENDING v0.18

⚠ **Protected-area diff 檢查（沿用第 5 條教訓 — 用明示 commit hash）：** `git diff bb50a54..HEAD --name-status` 應只見 Wave 13 + 本 review starter；任何觸及上述不動範圍 → 列為 R-W13-MA-XX

**Wave 13 後預期 baseline（Windows 端權威；對齊 9th master 第一段第二輪 verify）：**

- check_headers: 0 ERROR / ≤ 50 WARN / ≤ 170 files
- check_paths: **≤ 247 ERROR**（hard-limit accept R2-MAJOR-03）
- build_repo_index: 0 ERROR (Windows 端權威)

---

# 2. 重審範圍與維度（6 維度）

**維度 1 — 4 個英文 view-* SKILL.md 結構對齊 D6 範本 11 段**

對 view-world / view-character / view-outline / view-detailed-outline 4 個英文主檔跑 grep + 結構 verify：

預期含 11 段（依 D6 範本）：
1. `## 用途`
2. `## 觸發語`
3. `## 觸發協議`（指向 ARCH §4.1 為權威；無 00_protocol/ 對應）
4. `## 啟動前檢查`
5. `## 流程`（5 階段：診斷 / 反查 source / 組合 / 呈現 / 驗證）
6. `## 呈現規則`（chat 動態組合不加 breadcrumb / 不加 TOC / source italic / 跨檔 link `/` 開頭 / 單向 reference）
7. `## .protocol_version 寫入規範`（可選 phase_log audit entry）
8. `## 輸入`
9. `## 輸出`（chat Markdown 印；不寫檔）
10. `## 邊界`（**純讀取邊界 7 條**：不寫檔 / 不寫 view/ 整合檔 / 不擴 source / 不升 entity / 不擅自呼叫其他 view-* / 不擅自重新組織 source / 不寫 LOCKED）
11. `## 錯誤處理 / Rollback` + `## 錯誤呈現規則`

判定：PASS / PARTIAL / FAIL；列任何漏段 / 不齊全。

**維度 2 — D9 D-054 hybrid fallback strict verify**

對 `view-detailed-outline/SKILL.md` 跑：

- 含「D-054 hybrid 讀檔 fallback 規範」段
- Phase 1 (per-scene file first) 完整：check per-scene 路徑 → 存在 → 讀檔 → `read_source = "per-scene"`
- Phase 2 (aggregate 06_a fallback)：per-scene 不存在 → 讀 06_a row → `read_source = "aggregate"`
- Missing handling：兩者皆無 → 印 placeholder + `read_source = "missing"`；split-to-file marker 但 per-scene 檔失蹤 → 印 WARN
- `read_source` enum：`per-scene` / `aggregate` / `missing`；不允許同時 per-scene + aggregate
- **不觸發 split-to-file**（屬未來 /iterate-scene <S-ID> --split-to-file scope）
- 對齊 `.claude/skills/scene-task/SKILL.md` v0.1 既有 D-054 fallback 邏輯
- 對齊 `_design/D054_DECISION_PACKAGE.md` v0.2 §3 推薦理由

判定：PASS / PARTIAL / FAIL

**維度 3 — 呈現規則對齊 ARCH §4.1 + §4.4 + UX_SPEC §7**

對 4 個英文 view-* SKILL.md 跑：

- chat 動態組合**不加 breadcrumb**（vs /export-* 必加；ARCH §4.4 line 833 為權威）
- chat 動態組合**不加 TOC**（vs /export-* 預估 > 200 行加；ARCH §4.4 line 779）
- 每段尾加 source italic `*來源：[/path](/path)*`（ARCH §4.4 + UX §7.2）
- 跨檔 link 一律以 project root 為基準（`/` 開頭）；同檔 anchor `#slug` 不加 `/`（ARCH §4.4）
- 單向 reference：本 skill 引用 source 時加連結；source 不必反向列（ARCH §4.4）
- chat 動態組合也加 source 引用（即使連結點不到，純文字仍提供定位線索；ARCH §4.4）

判定：PASS / PARTIAL / FAIL

**維度 4 — frontmatter 對齊 SPEC §5.2 + 中文 5 header**

對 4 個英文主檔 + 4 個中文 wrapper 跑：

- 8 個 SKILL.md 都含 frontmatter (name + description) + 中文 5 header（狀態 / 版本 / 最後更新 / 適用範圍 / 優先級）
- 4 個中文 wrapper 採極簡模式（指向英文主檔為權威；不重複大段 substantive）
- 4 個英文主檔 description 50-200 字
- 4 個英文主檔 frontmatter name 對齊 directory name

判定：PASS / PARTIAL / FAIL

**維度 5 — baseline + regression + protected-area diff**

技術驗證：

- 跑 check_headers.py / check_paths.py / build_repo_index
- check_paths 目標：**≤ 247 ERROR**（hard-limit accept）
- `git diff bb50a54..HEAD --name-status` — 對比 Wave 13 變動範圍
- Wave 13 預期變動：
  - 新建 `_design/CODEX_D6_STARTER.md` v0.1（master 寫）
  - 新建 `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1（master 寫）
  - 新建 `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（master 寫；可能在 HEAD~1 commit）
  - 修改 `_design/POST_LOCK_PENDING.md` v0.18（master 寫）
  - 新建 8 個 SKILL.md (4 英文主檔 + 4 中文 wrapper) — CODEX D.6 + batch task 寫
- 任何觸及「Wave 13 不動段」範圍 → R-W13-MA-XX

判定：PASS / PARTIAL / FAIL

**維度 6 — 跨範圍 stale cross-ref grep 全掃**

對 Wave 13 8 個新 SKILL.md 跑 stale pattern grep：

- 舊檔名 stale：`04_b_關係演化時間線|05_a_主線結構\.md|05_b_章節結構\.md|05_c_角色弧線\.md|06_scene_index/06_a_場景索引\.md|01A_世界觀總覽|01B_世界語言|02A_專有名詞|05D_資訊揭露`
- 版本 stale：`create-character.*v0\.3|POST_LOCK_PENDING.*v0\.(9|10|11|12|13)|DECISIONS_LOG.*v1\.[1-9]|TASKS.*v1\.[1-8]|ARCH.*v1\.[1-5]`
- 5 份 / 09_a-d stale（屬 Phase C cleanup 範圍）：`5 份 QA|五份 QA|09_a-d|09_a–09_d`（若在 view skill 內出現可能 inappropriate）
- 0 active match 預期；任何 active match（除 supersede note / 歷史 narrative）→ R-W13-MI-XX

判定：PASS / PARTIAL / FAIL

---

# 3. Finding 嚴重度 + 判定門檻

- **CRITICAL**：D-054 落地破壞 / SKILL.md frontmatter 不可用 / Wave 13 SKILL.md 含未授權寫檔 / 新 spec 衝突
- **MAJOR**：結構漏段（11 段不齊）/ D9 D-054 hybrid fallback 不完整 / 呈現規則 wording 偏離 ARCH §4.1 / 新 baseline regression / protected-area diff mismatch
- **MINOR**：sweep 漏掉的 active stale / cross-ref 邊緣偏差 / wording polish
- **INFO**：observation / 改善建議

Finding ID 命名：`R-W13-<severity>-<NN>`

判定門檻：

- **GO（PASS）**：0 CRITICAL + 0 MAJOR + 6 維度全 PASS + check_paths ≤ 247 ERROR + 0 protected-area diff → 9th master 第二段對話進 Wave 14
- **NEAR-GO**：0 CRITICAL + ≤ 1 MAJOR + ≤ 3 MINOR → master 拍板 hard-limit accept 或 inline patch
- **NO-GO**：≥ 1 CRITICAL 或 ≥ 2 MAJOR

# 4. 輸出格式

寫 1 個檔：`_design/CODEX_9TH_MASTER_WAVE13_REVIEW_REPORT.md` v0.1

必含段：

```
# 0. 文件目的
# 1. Wave 13 摘要 + 判定（GO / NEAR-GO / NO-GO）
# 2. 維度 1：4 個英文 view-* SKILL.md 結構對齊 D6 範本 11 段
# 3. 維度 2：D9 D-054 hybrid fallback strict verify
# 4. 維度 3：呈現規則對齊 ARCH §4.1 + §4.4 + UX_SPEC §7
# 5. 維度 4：frontmatter 對齊 SPEC §5.2 + 中文 5 header
# 6. 維度 5：baseline + regression + protected-area diff
# 7. 維度 6：跨範圍 stale cross-ref grep 全掃
# 8. Finding 總計表（R-W13-<severity>-<NN>）
# 9. 決策判定 + Rationale
# 10. 給 9th master 的建議（進 Wave 14 / inline patch / hard-limit accept）
# 11. Cross-ref
```

# 5. 起跑命令

```bash
cd /sessions/<your_session>/mnt/劇本開發工具
python3 -X utf8 -B scripts/check_headers.py 2>&1 | tail -3
python3 -X utf8 -B scripts/check_paths.py 2>&1 | tail -3
python3 -X utf8 -B -c "from scripts.parse_frontmatter import build_repo_index; r = build_repo_index('.'); print('ERR:', len([i for i in r.issues if i.severity == 'ERROR']))"
git log --oneline -8
git diff bb50a54..HEAD --name-status
```

維度 1-2 verify：
```bash
# 維度 1：結構 grep
for f in .claude/skills/view-world/SKILL.md .claude/skills/view-character/SKILL.md .claude/skills/view-outline/SKILL.md .claude/skills/view-detailed-outline/SKILL.md; do
  echo "=== $f ==="
  grep -n "^## " "$f" | head -20
done

# 維度 2：D9 D-054 hybrid fallback
grep -n "D-054\|per-scene\|06_a\|hybrid\|fallback\|split-to-file\|read_source" .claude/skills/view-detailed-outline/SKILL.md
```

維度 6 stale grep：
```bash
grep -rn "04_b_關係演化時間線\|05_a_主線結構\.md\|05_b_章節結構\.md\|05_c_角色弧線\.md\|06_scene_index/06_a_場景索引\.md" .claude/skills/view-*/
grep -rn "create-character.*v0\.3\|POST_LOCK_PENDING.*v0\.\(9\|10\|11\|12\|13\)" .claude/skills/view-*/
grep -rn "5 份 QA\|五份 QA\|09_a-d" .claude/skills/view-*/
```

⚠ 排除歷史 narrative / supersede note 段

# 6. Cross-ref

- `_design/CODEX_D6_STARTER.md` v0.1（D.6 共通範本；Wave 13 結構 reference）
- `_design/CODEX_D_VIEW_BATCH_STARTER.md` v0.1（D7-D9 batch starter；Wave 13 結構 reference）
- `_design/ARCHITECTURE.md` v1.6 §4.1 + §4.4（view 動態組合 + 呈現規則）
- `_design/SPEC.md` v1.2 §5.2（frontmatter canonical schema）
- `_design/UX_SPEC.md` v0.4 §7（呈現規則 — 跨檔 link / source 引用 / 單向 reference）
- `_design/D054_DECISION_PACKAGE.md` v0.2（D-054 hybrid 推 NEW_REQ_15）
- `_design/DECISIONS_LOG.md` v2.0 §6.17 D-054
- `.claude/skills/scene-task/SKILL.md` v0.1（D-054 hybrid fallback 既有範本；D9 應對齊）
- `_design/POST_LOCK_PENDING.md` v0.18（Round 1-4 cycle 完整紀錄 + 5 條教訓內化）
- `_design/HANDOFF_9TH_MASTER_CONTINUATION.md` v1.0（9th master 第二段對話接手包）
