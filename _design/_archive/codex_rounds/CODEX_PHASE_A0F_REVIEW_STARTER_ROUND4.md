狀態：DRAFT
版本：v0.1
最後更新：2026-05-23
適用範圍：Phase A.0F CODEX 3rd NEAR-GO 後 patch round 3 完成 → 4th strict review verify Windows CP950 console UTF-8 修法
優先級：極高（GO 後 branch 可 merge 進 master / Phase A.0G 或 Phase B）

# CODEX_PHASE_A0F_REVIEW_STARTER_ROUND4 — Phase A.0F patch round 3 CODEX 4th review

# 0. 本檔用途

1st CODEX **NO-GO**（5 P0/P1/Major + 8 patch 順序）
→ Round 1 patch 7 commit
→ 2nd CODEX **NEAR-GO**（兩個 finding：acceptance blocker / L3 stats drift）
→ Round 2 patch 2 commit
→ 3rd CODEX **NEAR-GO**（一個 finding：Windows CP950 console UnicodeEncodeError）
→ Round 3 patch 1 commit
→ 本輪：CODEX 4th strict review verify CP950 console fix

**前置條件：**
- Branch `frontend-tools-a0f`（HEAD: <round-3 commit hash; user push 後告知>）
- 3rd CODEX NEAR-GO 報告 master 端紀錄

**review GO →** branch 升 FINAL；merge 進 master；Phase A.0F 收尾
**review NEAR-GO →** 第 4 輪 patch（不太可能 — 剩這條是 acceptance harness 級別）

⚠ **Scope 嚴格限定：本輪 verify ONLY，1 個 finding。**

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

~~~
你是 game-dialogue-bible 專案的 Phase A.0F 第四輪 CODEX strict reviewer。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
分支：frontend-tools-a0f（HEAD: <round-3 commit hash>，Round 3 patch 完成後）

**第一步必讀（按順序）：**
1. `_design/CODEX_PHASE_A0F_REVIEW_REPORT.md` v0.1 — 1st NO-GO 報告（基準）
2. `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND2.md` v0.1 — Round 2 verify starter
3. `_design/CODEX_PHASE_A0F_REVIEW_STARTER_ROUND3.md` v0.1 — Round 3 verify starter（3rd NEAR-GO 已 PASS body finding）
4. 3rd CODEX NEAR-GO 報告（master 端紀錄；一個 finding：Windows CP950 console UnicodeEncodeError）

**Round 3 patch 1 commit：**

| commit | subject | 範圍 |
|---|---|---|
| `<hash>` | patch-round3 | test_endpoints_smoke.py 強制 stdout/stderr UTF-8 |

**Verify 順序（3rd CODEX finding 對齊）：**

Round 3 finding — Windows CP950 console UnicodeEncodeError：

1. **`_force_utf8_console()` helper 存在 + 在 main() 第一行被呼叫**
   - test_endpoints_smoke.py: 新增 `_force_utf8_console()` 函式
   - main() 第一行呼叫 `_force_utf8_console()`
   - Verify: `git show frontend-tools-a0f:_tools/frontend/tests/test_endpoints_smoke.py | grep -n "_force_utf8_console"`
   - 預期：定義 + main() 呼叫共 2 個 anchor

2. **reconfigure 目標 stdout + stderr，errors="replace" fallback 安全**
   - 對 sys.stdout + sys.stderr 兩個 stream 都跑 reconfigure
   - 用 errors="replace" 避免邊角字符 crash
   - 用 getattr(stream, "reconfigure", None) 防 Python < 3.7 / 非標準 stdout
   - Verify: `git show frontend-tools-a0f:_tools/frontend/tests/test_endpoints_smoke.py | grep -A 8 "_force_utf8_console"`

3. **沙箱跑（不設 PYTHONIOENCODING）應全 PASS 不 crash**
   - 沙箱：`python tests/test_endpoints_smoke.py --allow-stage-b-skip` → exit 0
   - Host CP950 console：`python tests/test_endpoints_smoke.py`（不 PYTHONIOENCODING）→
     不應 UnicodeEncodeError；Stage A 全跑；Stage B（裝完 fastapi+httpx）也全跑
   - 模擬 CP950：`PYTHONIOENCODING=cp950:strict python tests/test_endpoints_smoke.py
     --allow-stage-b-skip` → 仍 exit 0（reconfigure 把 stdout 改 UTF-8）

4. **regression anchor test：`test_endpoints_smoke.py: forces UTF-8 stdout to survive
   Windows CP950 console (CODEX 3rd review)`**
   - 在 _tools/frontend/tests/patch_round_regression.test.mjs
   - 鎖 4 條：_force_utf8_console 定義 / 被 call / stdout+stderr target / errors="replace"

**驗收條件：**
- node --check 全 PASS (13 JS file)
- 91 JS test 全 PASS：
  - copy_command_button       10/10
  - patch_round_regression   30/30 (Round 3 +1)
  - prompt_assembler          33/33
  - sceneeditor_guide         18/18
- Stage A endpoint inventory 10/10 PASS
- Stage B (host 裝完 fastapi+httpx 後跑) 全 PASS（22 total expected per 3rd CODEX evidence）
- Windows CP950 console 不需要外部 PYTHONIOENCODING=utf-8 也能跑完整套
  acceptance script（不 crash on ✓/✗/中文）

**禁止：**
- 不擴新 feature
- 不擅升 L3_EXPORT_PROMPT_SCHEMA.md v0.2 → v1.1
- 不擅啟 new D-NNN 拍板
- 不動 9th master 軸 commit
- 不重審 1st/Round-2/Round-3 已 PASS 的部分（body findings 已全 RESOLVED）

開始 4th strict review。
~~~

# 2. 後續流程

| 階段 | 動作 |
|---|---|
| **user 開新 CODEX 對話** | 把 §1 ~~~ block 整段貼到新 CODEX 對話 |
| **CODEX 4th strict review** | 預計回 GO（剩這條是 acceptance polish）|
| **GO 後** | merge frontend-tools-a0f 進 master，Phase A.0F FINAL |

# 3. Cross-ref

- 前三 round starter / report
- branch: frontend-tools-a0f (HEAD: <round-3 hash>)

# 4. 教訓 — Round 3 新增

17. **acceptance script 自己要處理 console encoding 邊界** — 別假設 UTF-8 環境；
    用 `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` 在 main()
    第一行就把 stream 鎖死，這樣 cross-platform 都能跑（Windows CP950 / Big5 /
    Linux UTF-8 一致）。
18. **errors="replace" 比 strict 安全** — strict 遇到無法 encode 的字符會 crash；
    replace 用 ? 取代不會 crash，acceptance script 永遠走到底。
