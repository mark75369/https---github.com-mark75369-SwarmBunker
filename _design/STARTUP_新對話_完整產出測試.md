狀態：DRAFT
版本：v1.0（新對話啟動文件 — 完整產出測試 + 後續開發；可直接複製貼上為新對話第一則訊息）
最後更新：2026-06-03
適用範圍：開新對話接手「完整產出測試 → 正式寫作」的單一啟動入口；冷啟動自足
優先級：高

# 啟動文件 — 完整產出測試（複製本檔正文當新對話第一則訊息）

---

你是接手 **game-dialogue-bible 工具**「完整產出測試」的新對話。工具開發已全部完成並 merge+push，這個對話的任務 = **陪我（user）在乾淨 Instance 上跑完整 skill 鏈、產出真實台詞 + QA，驗證端到端可用；沒問題我就開始正式寫作。** 後續若需開發/稽核/審查，用 `/workflows` 跑、守四層防線。

## 0. 先讀這些文件（冷啟動 context）

1. **`_design/HANDOFF_PRODUCTION_TEST.md`** — 主交接包（測試計畫全文：建 Instance 步驟 / skill 鏈 / 測試重點 / 已知未做）。**先讀這份。**
2. `_user_manual/skill_registry_full.md` — 全 skill 權威清單 + 版本落地狀態。
3. `DECISIONS_LOG.md` §6.23–§6.27（D-071 ORG core / D-074 ORG authoring + amendment / D-075 registry DRY）+ `POST_LOCK_PENDING.md` v0.37 — 帳本。
4. `00_protocol/00_n_組織創建協議.md`（新 ORG 協議，v0.2 7 段 issue-ful）。
5. `_design/_DEPRECATED_REGISTER.md` — 已封存設計文件清單（**勿當活躍指引**）。
6. `_design/REVIEW_LOOP_PROTOCOL.md` — 四層防線（開發時遵守）。

## 1. ⚠️ 環境陷阱（先讀，會踩）

- 工具 repo = `D:\劇本開發工具`（remote `https://github.com/mark75369/Writing-tools.git`）。**這是 Template repo**（root 有 `.template_root`）→ **所有 /create-* skill 會拒絕在這裡跑**。測試必須在**乾淨 Instance**。
- 路徑陷阱：**`開發`(發) vs `開発`(発)** 是不同字 —— Edit/Read 路徑務必用「發」。
- 最新工具在 **`frontend-tools-a0f`** 分支（**不是 master**）。clone 後要 `git checkout frontend-tools-a0f`。
- 跑 Python/scripts 設 `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1`。
- `git -C "D:/劇本開發工具" ...`；commit/push 只在 user 要求時做；**不自行 merge LOCKED 改動進主分支**（L3 gate）。

## 2. 立即任務：建測試 Instance（clone）

```bash
git clone https://github.com/mark75369/Writing-tools.git "D:/測試專案"   # 路徑 user 定
cd "D:/測試專案"
git checkout frontend-tools-a0f      # 最新工具在這分支，不在 master
del .template_root                   # PowerShell（bash: rm .template_root）— 解 Template 鎖，skill 才肯跑
```
完成後**在這個 Instance 資料夾啟動工作**，不是在 Template repo。

## 3. 完整 skill 鏈（陪 user 依序跑；user 出創意、agent 跑 skill）

`/init-project` → `/create-world` → `/create-character` → **`/create-org`**（⭐新）→ `/create-relationship`（⭐含 **C↔ORG** endpoint）→ `/create-outline` → `/create-detailed-outline` → `/scene-task <S-ID>` → **`/dialogue-write <S-ID>`**（真實台詞）→ `/qa <dialogue_path>`。沿途 `/status` `/check-gaps` `/view-*` `/export-*`。

**測試重點：** (1) 新 ORG 鏈跑得順？`/create-org` 7 段 issue-ful + C↔ORG endpoint + `/status` 計入 ORG。(2) 不變量：ORG-* 不長聲線卡、不進 /dialogue-write 為說話者。(3) `/dialogue-write`+`/qa` 真實產出是不是「可用」水準（這是開始寫作的判準）。(4) L2 隨時可跑（pytest scripts/tests/ 應 43 pass）。(5) 記下任何卡關/rough edge。

## 4. 開發紀律（測試若帶出要修的東西）

- **用 `/workflows`（dynamic workflow）跑稽核 / 審查 / 重構 / 多步開發** —— 本專案一路如此（F8 / Batch 5 / Batch 6 都是 workflow 跑 L1 外審 + 稽核）。fan-out finder → 對抗式 verify → 合成。
- **四層防線**：L0 執行 → L1 獨立 workflow 外審 → L2（check_paths / check_headers / check_entity_type_consistency / pytest）→ **L3 user 真抽查簽字**。
- **動 LOCKED（spec / 協議 / registry / parser）必拍 D-NNN + 走四層 + L3**；agent 不代簽、不自行 merge。
- 每完成一段 **checkpoint commit**（具體 path、勿 `git add -A`）。
- 型別 drift 由 `check_entity_type_consistency.py` CI 強制（加型別只改 registry 一處）。

## 5. 已知**未**做（別期待；要時才補，用 workflow）

- F8 **方向 B**（W-language 文件語體卡）— DEFERRED；`00_n` §7 只留 hint。
- **view-org / export-org** 獨立 skill + view-world compose ORG — DEFERRED（目前看 ORG 直接讀 `11_organizations/<name>.md`）。
- **清道夫 R-* opt-in 遷移**（舊 workaround → ORG-清道夫）— user 明示才做。
- Group 4 觀察項（C-ORG 裸名 ID 碰撞等，非現行 bug）。

## 6. 起手式

1. 確認/協助 user clone 出 Instance（§2），在該 Instance 啟動。
2. 跟 user 敲定小而完整的測試題材（1 世界 + 2-3 角色 + 1 個 ORG 對抗源 + 1 主線 + 1-2 場戲）。
3. 依 §3 鏈逐 skill 陪跑，§3 重點隨時盯。
4. 跑出真實台詞 + QA → 跟 user 一起判「可不可用」。
5. 可用 → user 開始正式寫作（同 Instance 繼續長）；有 rough edge → 記下、評估是否開一輪工具修補（用 /workflows + 四層防線）。
