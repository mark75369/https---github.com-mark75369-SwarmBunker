狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：Phase A.0F NO-GO patch round 2 完成後 CODEX 3rd strict review (verify Round 2 兩個 finding 全修 + 90 JS test + Stage B 9 fixture test + acceptance opt-in flag)
優先級：極高（GO 後 branch 可 merge 進 master / Phase A.0G 或 Phase B）

# CODEX_PHASE_A0F_REVIEW_STARTER_ROUND3 — Phase A.0F patch round 2 CODEX 3rd review

# 0. 本檔用途

Phase A.0F master 平行對話 12 commit + audit 4 commit + audit-codex starter 2 commit
→ 1st CODEX strict review 判 **NO-GO**（`_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1）
→ patch round 1 跑 7 commit（HEAD a996ad5）
→ Round 2 starter `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1 land
→ 2nd CODEX strict review 判 **NEAR-GO**（兩個 finding）
→ patch round 2 跑 2 commit（HEAD fc2948b）
→ 本輪：CODEX 3rd strict review verify Round 2 兩個 finding 全修

**前置條件：**
- Branch `frontend-tools-a0f`（HEAD `fc2948b`，Round 2 patch 完成狀態）
- 1st CODEX report `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 已 land master
- Round 2 starter `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1 已 land master
- 2nd CODEX report（NEAR-GO 反饋；user 已貼回 master）

**review GO →** branch 升 FINAL；merge 進 master；進 Phase A.0G 或 Phase B
**review NEAR-GO →** 再開 patch round 3（小修）
**review NO-GO →** 不太可能（剩兩條都是 acceptance / drift level）

⚠ **Scope 嚴格限定：本輪 verify ONLY，不擴新 feature。**
- 對齊 2nd CODEX report 兩個 finding（#1 acceptance blocker / #2 L3 stats drift）
- 確認 Round 2 patch 兩個 commit 都 verifiable
- 不擅啟新 D-NNN 拍板
- 不重審 1st / Round-2 已 verified 部分

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 Phase A.0F 第三輪 CODEX strict reviewer。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
分支：frontend-tools-a0f（HEAD: fc2948b，Round 2 patch 完成後）

**第一步必讀（按順序）：**
1. `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 — 1st strict review NO-GO 報告（基準）
2. `_design/CODEX_PHASE_A0F_PATCH_ROUND_STARTER.md` v0.1 — Round 1 patch 啟動指引
3. `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1 — Round 2 verify starter（已 PASS NEAR-GO）
4. 2nd CODEX NEAR-GO 報告（master 端紀錄；兩個 finding：#1 acceptance blocker / #2 L3 stats drift）
5. `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2 — L3 schema contract 鎖
6. `_design/UX_SPEC.md` §11.3 / §11.5 / §11.6 / §11.7

**Round 2 patch 2 commit (HEAD fc2948b 起回溯)：**

| commit | subject | 範圍 |
|---|---|---|
| `fc2948b` | patch-round2-P1 | Stage B acceptance blocker (requirements.txt + skip fail nonzero) |
| `51ba03e` | (bundled) | L3 stats drift outline_only (a+b 雙修；含 9th master handoff 雜檔) |
| `393229f` | patch-round2-starter | Round 2 starter (1st-round 收尾) |

⚠ 注意：`51ba03e` commit 是 user 在 host 端把 Round 2 P2 patch 跟 9th master handoff 雜檔（無關 Phase A.0F）一起 push 的綜合 commit。本輪 review 只看其中 Round 2 P2 部分（4 個 frontend file 改動），不審其他雜檔。

**Verify 順序（2nd CODEX report finding 對齊）：**

Round 2 finding #1 — Stage B acceptance blocker (commit `fc2948b`)：
1. **requirements.txt 補 httpx**
   - 對齊：fastapi.testclient.TestClient 內部依賴 httpx
   - Verify: `git show frontend-tools-a0f:_tools/frontend/requirements.txt | grep -i httpx`
   - 預期：含 `httpx>=0.27` + 註解說明為何（與 fastapi TestClient 綁定）
   - 對等 Stage B：host 跑 `pip install -r requirements.txt` 之後不應再 skip
   - 預期：Stage B 全 9 fixture test PASS（含 outline_only）

2. **Stage B skip → exit code 2（acceptance blocker）**
   - test_endpoints_smoke.py main() 預設 ImportError/ModuleNotFoundError → return 2
   - 新 opt-in flag `--allow-stage-b-skip` 容許 skip → return 0（沙箱模式）
   - Verify: `git show frontend-tools-a0f:_tools/frontend/tests/test_endpoints_smoke.py | grep -n "return 2\|allow-stage-b-skip"`
   - 沙箱測試：
     - 預設跑：`python tests/test_endpoints_smoke.py` → exit 2（因為 fastapi 沒裝）
     - 加 flag：`python tests/test_endpoints_smoke.py --allow-stage-b-skip` → exit 0
   - Host 跑：`pip install -r requirements.txt && python tests/test_endpoints_smoke.py` → exit 0 全 PASS
   - regression test anchor：`requirements.txt: includes httpx` +
     `test_endpoints_smoke.py: Stage B skip returns nonzero by default`

Round 2 finding #2 — L3 stats drift outline_only (commit `51ba03e` 部分內容)：
3. **Backend (option a)：server.py outline_only 正式 scope**
   - `is_outline_entity` / `parsed_outline_relevant` 依 L3 schema §1.3
     (W-rules + W-language + V + C-* + R-*-* + P + CH-*；排除 S / A)
   - `parsed_matches_scope` 加 outline_only 分支
   - `scope_counts_payload` outline_only 排除 A-* art_entries + 跳過 type=='S'
   - `valid_scope_counts_scope` 接受 outline_only
   - 400 error message 列舉 outline_only
   - Verify: `git show frontend-tools-a0f:_tools/frontend/server.py | grep -n "outline_only\|parsed_outline_relevant"`
   - Verify: 跑 `/api/scope-counts?scope=outline_only` → 200, body.scope='outline_only',
     counts.entities.S==0, counts.entities.A==0, counts.art_assets==0

4. **Frontend (option b)：ExportPanel.js 配合 + defensive fallback**
   - refreshScopeCounts: scopeType=outline_only → scopeArg='outline_only'
   - currentPrompt: defensive — error / no data / scope mismatch → stats=undefined
   - expectedScopeArg 含 full / scene/<id> / outline_only 三 branch
   - Verify: `git show frontend-tools-a0f:_tools/frontend/static/js/pages/ExportPanel.js | grep -n "outline_only\|expectedScopeArg"`
   - regression test anchor：`ExportPanel.js: refreshScopeCounts maps outline_only` +
     `currentPrompt suppresses stats when scope-counts errored or scope mismatches`

5. **新 regression test (Stage B + JS)**
   - test_endpoints_smoke.py: `test_scope_counts_outline_only` (Stage B)
   - patch_round_regression.test.mjs: +4 anchor test
     - refreshScopeCounts maps outline_only
     - currentPrompt defensive fallback
     - server.py parsed_outline_relevant + outline_only branch
     - server.py valid_scope_counts_scope accept outline_only
   - + Round 2 P1 補的 2 anchor：
     - requirements.txt: includes httpx
     - Stage B skip returns nonzero by default

**驗收條件：**
- `node --check` 全 PASS（13 JS file）
- 90 JS test 全 PASS：
  - copy_command_button       10/10
  - patch_round_regression   29/29 (Round 2 +6)
  - prompt_assembler          33/33
  - sceneeditor_guide         18/18
- Stage A endpoint inventory 10/10 PASS
- Stage B：host 端 `pip install -r requirements.txt` 之後跑
  `python tests/test_endpoints_smoke.py` 應全 PASS（不需要再手動 pip install httpx）
- Stage B 9 個 fixture test：
  - 既有 8 個（version-content / target_path / D-045 / 其他）
  - +1 新增 `test_scope_counts_outline_only`
- 沙箱模式可選：`python tests/test_endpoints_smoke.py --allow-stage-b-skip`

**禁止：**
- 不擴新 feature
- 不擅升 L3_EXPORT_PROMPT_SCHEMA.md v0.2 → v1.1
- 不擅啟 new D-NNN 拍板
- 不動 9th master 軸 commit (d6ec085 / 499bc13 / 51ba03e 內 9th master 雜檔部分)
- 不重審 1st-round 已 PASS 的部分（如 CC-07 / Bug 1 / Bug 2）
- 不重審 Round 2 已 PASS 的部分（如 patch-P0 / patch-P1 / patch-major-1 /
  patch-major-2 chapter rejection / patch-concern-1 / patch-concern-2 /
  patch-P2 / patch-P3）

開始 3rd strict review。
~~~

---

# 2. 後續流程

| 階段 | 動作 |
|---|---|
| **user 開新 CODEX 對話** | 把上面 ~~~ block 整段貼到新 CODEX 對話 |
| **CODEX 3rd strict review** | 預計回 GO / NEAR-GO / NO-GO 報告 |
| **CODEX 報告 land** | 寫到 `_design/CODEX_PHASE_A0F_REVIEW_REPORT_ROUND3.md` v0.1 |
| **GO 後** | merge frontend-tools-a0f 進 master，Phase A.0F FINAL |
| **NEAR-GO** | 補一輪 patch round 3 跑修；新 round 4 starter |
| **NO-GO** | 不太可能 — 剩兩條都是 acceptance / drift level |

# 3. Cross-ref

- `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1（1st strict review NO-GO 報告）
- `_design/CODEX_PHASE_A0F_PATCH_ROUND_STARTER.md` v0.1（Round 1 patch 啟動指引）
- `_design/CODEX_PHASE_A0F_REVIEW_STARTER.md` v0.1（原 review starter 含 12 commit 列表）
- `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1（Round 2 verify starter）
- `_design/L3_EXPORT_PROMPT_SCHEMA.md` v0.2（schema 鎖；output_paths + scope enum）
- `_design/UX_SPEC.md` v0.4 §11.3 / §11.5 / §11.6 / §11.7
- `_design/DECISIONS_LOG.md` D-027 / D-029 / D-035 / D-038 / D-040 / D-042 / D-044 / **D-045** / D-046 #5 + CC-07
- `_design/SPEC.md` §5.2 + §16
- `_user_manual/05_frontend_tools.md` v0.3
- branch: `frontend-tools-a0f` (HEAD: fc2948b)

# 4. 教訓 — Round 2 新增

**Round 2 累積 (delta vs Round 1)：**
13. **acceptance script 的 skip 路徑必須非 0** — 安靜回 0 等於 CI 看不見問題；
    skip 預設 fail，opt-in flag 才回 0（沙箱模式）。
14. **frontend scope-arg 跟 backend scope enum 必須對齊** — 任何一方加新 enum，
    另一方一定要 round-trip 對齊（防 outline_only 走 "full" stats 那種 silent drift）。
15. **defensive fallback 跟「正確修法」要一起做** — 即使 backend 修完，frontend 也該對
    「未來 backend 漂移」加防線（user pick a+b 雙修，不只 a 或 b 單修）。
16. **requirements.txt 的依賴清單要對齊實際 import** — 別讓 transitive dependency
    （如 httpx via fastapi.testclient）silently 缺一個就 skip。
