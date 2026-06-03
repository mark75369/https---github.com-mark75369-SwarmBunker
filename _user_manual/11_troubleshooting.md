狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：錯誤訊息對照 + 故障排除  
優先級：高

# 11 故障排除

# 1. 前端 server 啟動問題

## 1.1 `Address already in use` / port 8765 被佔用

**原因：** 前一次的 server 沒關掉 / 別的程式用了 8765 port。

**解法 A：** 找出佔用 process 殺掉
```bash
# Windows
netstat -ano | findstr :8765
taskkill /F /PID <pid>

# Mac/Linux
lsof -i :8765
kill -9 <pid>
```

**解法 B：** 換 port 啟動
```bash
python _tools/frontend/serve.py --port 8766
```

## 1.2 `ModuleNotFoundError: No module named 'fastapi'` / 缺套件

**原因：** 沒安裝 dependencies。

**解法：**
```bash
pip install -r _tools/frontend/requirements.txt
```

## 1.3 `Python 3.10+ required`

**原因：** Python 版本太舊。

**解法：** 升級 Python 到 3.10 以上。`python --version` 確認版本。

## 1.4 瀏覽器開了但畫面空白

**原因 1：** server 還在啟動。等 5 秒再 refresh。

**原因 2：** 資料夾路徑含空白或特殊字元。**解法：** 把資料夾移到全 ASCII 路徑（如 `D:\game-bible\`）後重啟。

**原因 3：** 沒跑過 `/init-project`。**解法：** 先在 Claude Code 跑 `/init-project` 建專案結構，再啟前端。

---

# 2. /init-project 問題

## 2.1 `template_source not found`

**原因：** 工具的 Template repo 沒 clone。

**解法：**
```bash
git clone https://github.com/<原工具 repo>.git template
```

## 2.2 跑完 /init-project 但目錄結構不對

**原因：** Bootstrap 中途中斷。

**解法：** 刪掉現有 Instance 目錄，重跑 `/init-project`。

---

# 3. parser / agent 跑到一半中斷

## 3.1 `phase_log.lock 等候 30 秒 timeout`

**原因：** 另一個 skill 正在寫同個 Instance（多場景並行衝突）。

**解法：**
- 等對方完成
- 如果沒有別的 process 在跑（你只有一個 agent 對話），檢查是否有 stale lock：
```bash
ls .protocol_version.lock
```
有的話：
```bash
rm .protocol_version.lock
```
重試 skill。

## 3.2 `import_source != null 但 skill 不是 /create-*`

**原因：** 你在錯誤的地方加了 `--trust-level` 參數（只有 /create-* 接受）。

**解法：** 從指令移除 `--trust-level`。

## 3.3 `base_dialogue 鏈條形成 cycle`

**原因：** SINGLE_ITER lineage 出現迴圈（iter2 base_dialogue → iter1，iter1 base_dialogue 又指 iter2）。

**解法：** 編輯較舊那一檔的 phase_log，把 base_dialogue 改回 null 或正確上一輪。

## 3.4 `conflict_resolutions[*].decision: create-as-new 缺 new_entity_id`

**原因：** 手稿導入時你選了 create-as-new 但沒指定新 entity ID。

**解法：** 在 phase_log 補 new_entity_id 欄位。

---

# 4. /qa 跑很慢 / 失敗

## 4.1 跑 /qa 超過 5 分鐘

**原因 1：** 場景對白太長（> 50 句）。**解法：** 正常，等。

**原因 2：** 09_g 節奏感檢查需要全文掃 — 可能慢一點。**解法：** 正常。

**原因 3：** parser cache 失效，每次重 parse 全 repo。**解法：** 重啟前端 server。

## 4.2 8 份 QA 報告只產出 5 份

**原因：** /qa skill 還沒升級到 v1.1（D-043）— 你用的是舊 implementation。

**解法：** 確認 `_design/TASKS.md` §D.4 已升級到 v1.1（8 份必跑）。重跑 /qa。

## 4.3 qa_decision 算錯

**原因：** 9 種 status 不齊（8 QA + 09_e）。

**解法：** 跑 `/check-gaps` 看缺哪個 status 報告。補完再升 FINAL。

---

# 5. 前端編輯 / Save 問題

## 5.1 Save 跳 LOCKED race modal

**原因：** 你進 Editor 時是 DRAFT，但編輯期間外部把 source 升 LOCKED 了。

**三選項：**

| 選項 | 行為 |
|---|---|
| (A) 複製降級指令 | 走外部 chat 降級為 DEPRECATED → 回前端重來；你的編輯**必須手動重輸** |
| (B) 另存 DRAFT proposal | 把編輯寫成新檔 `v02_proposal_<date>.md`；原 LOCKED 不動 |
| (C) 取消 | 編輯留前端 state；自己決定 |

詳見 SPEC §16a + UX §11.5.8。

## 5.2 Save 跳 mtime drift conflict modal

**原因：** 編輯期間外部改了同檔（agent 在另一視窗、或 VS Code 同步開著）。

**二選項：**

| 選項 | 行為 |
|---|---|
| (A) Reload | 載入 server 當前內容，你的編輯丟失 |
| (B) 強制覆寫 | 用你的編輯覆蓋 server，外部修改丟失（**先複製外部修改片段到剪貼簿**！）|

詳見 UX §11.7.6。

## 5.3 Save 跳 entity 命名衝突 modal

**原因：** 你跑 /create-* 手稿導入，agent 偵測到 entity ID 跟既有衝突。

**四選項：**

| 選項 | 行為 |
|---|---|
| (1) merge | 把手稿併入既有 |
| (2) overwrite | 用手稿覆蓋既有 |
| (3) create-as-new | 手稿另存為新 ID（如 `_v2`）|
| (4) skip | 拒絕導入該 entity |

詳見 UX §11.7.6a。

---

# 6. Export 問題

## 6.1 Export Panel「複製 Prompt」沒反應

**原因：** clipboard API 在某些瀏覽器 / HTTPS 設定下失效。

**解法：**
- 改用 Chrome / Edge（macOS Safari 限制較多）
- 確認 server 是 `localhost`（不是 IP）— clipboard API 對 IP 限制嚴

## 6.2 Export prompt 貼到 CC 後 agent 拒跑

**原因 1：** prompt schema_version 不對齊。

**原因 2：** mode 不是 read_only。

**解法：** 看 L3_EXPORT_PROMPT_SCHEMA §1.4 read-only constraints 是否完整。

## 6.3 Export 跑完 JSON / MD 缺一份

**原因：** prompt `formats:` 沒勾兩個。

**解法：** Export Panel 確認 `☑ JSON ☑ MD` 都勾再「複製 Prompt」。

---

# 7. 資料完整性問題

## 7.1 /status 顯示「entity 缺檔」

**原因：** phase_log 紀錄已跑某 skill 但檔案不在。

**解法：** 看 phase_log 中該 entry 的 `created_entities`，手動確認哪個檔缺。

## 7.2 「KEY 全 repo unique 衝突」

**原因：** 兩個檔的 dialogue_keys 出現相同 KEY 或 alias。

**解法：** 跑 `/check-gaps --scope=keys` 列衝突清單。手動改名其中一個（aliases 自動更新）。

## 7.3 「孤立立繪」WARN

**原因：** A-portrait-X-Y 的 X 對應的 C-* entity 不存在。

**解法：**
- 確認 entity 命名（C-* 跟 portrait owner 必須一致）
- 或建立缺失的 C-* entity

## 7.4 「內文 art comment 與 frontmatter 不一致」WARN

**原因：** 內文 `<!-- 立繪：A-... -->` 跟 frontmatter `dialogue_keys.<K>.portrait` 不一致。

**解法：** 編輯時保持兩者同步（v1.1：frontmatter 是權威，內文是 view-layer 提示，可暫時不同步但建議同步）。

---

# 8. git 問題

## 8.1 commit 時 git 抱怨「LOCKED 檔變更」

**原因：** 你直接動了 LOCKED 檔的內容（pre-commit hook 可能擋）。

**解法：** 走降級流程（看 §5.1 LOCKED race modal）— 改 `狀態：LOCKED → DEPRECATED` + 09_e 紀錄。

## 8.2 git push 失敗 `rejected non-fast-forward`

**原因：** remote 有你本地沒有的 commit。

**解法：**
```bash
git pull --rebase
# 解決 conflict（如果有）
git push
```

---

# 9. 看不到答案的問題

依嚴重度找對應地方：

| 嚴重度 | 看哪 |
|---|---|
| Tool crash / 完全跑不起來 | repo issue（如有）/ 自己 debug |
| skill 行為跟預期不符 | `_design/SPEC.md` 該段確認 |
| 不確定設計層怎麼定的 | `_design/DECISIONS_LOG.md` 找對應 D-NNN |
| 找不到該怎麼操作 | [00 快速入門](00_quick_start.md) / [02-05 skill 章節](README.md) |
| 想看實際範例 | [08 工作流](08_workflows/README.md) |
| 高頻問題 | [10 FAQ](10_faq.md) |
