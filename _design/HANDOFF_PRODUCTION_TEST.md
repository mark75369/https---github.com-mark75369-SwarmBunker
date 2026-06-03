狀態：DRAFT
版本：v1.0（交接包 — 給「完整產出測試」新對話：clone 乾淨 Instance → 跑全 skill 鏈 → 驗證可正式寫作）
最後更新：2026-06-03
適用範圍：接手「完整產出測試」的新對話 — 冷啟動可讀；陪 user 跑完整上游→下游 skill 鏈、驗證端到端可用
優先級：高

# HANDOFF — 完整產出測試（end-to-end production test）

## 0. 一句話

工具開發已**全部完成並 merge + push**（F8 Phase 3 ORG + Batch 5 registry DRY + Batch 6 技術債清掃，全在 `frontend-tools-a0f`）。**這個新對話的任務 = 陪 user 在一個乾淨 Instance 上跑完整 skill 鏈、產出真實台詞 + QA，驗證端到端可用。測試沒問題，user 就要開始正式寫作。**

## 1. ⚠️ 環境（先讀，有陷阱）

- **目前工具 repo = `D:\劇本開發工具`**（git root；remote `https://github.com/mark75369/Writing-tools.git`）。**這是 Template repo**（root 有 `.template_root` marker）—— **所有 /create-* skill 會拒絕在這裡跑**（D-049 防污染 gate）。所以測試**必須在乾淨 Instance**。
- **路徑陷阱**：`開發`(發) vs `開発`(発) 是不同字。
- 最新工具在 **`frontend-tools-a0f`** 分支（**不是 master**；master 還沒收到這些）。clone 後要 `git checkout frontend-tools-a0f`。
- 跑 Python / scripts 設 `PYTHONIOENCODING=utf-8` + `PYTHONUTF8=1`（Windows 中文）。

## 2. 建測試 Instance（user 已選：clone 成新 Instance）

```bash
# 1. clone 到新資料夾（路徑 user 定，例）
git clone https://github.com/mark75369/Writing-tools.git "D:/測試專案"
cd "D:/測試專案"
# 2. 切到最新工具分支（重要 — 最新工具不在 master）
git checkout frontend-tools-a0f
# 3. 解除 Template marker，讓它變 Instance（skill 才肯跑）
del .template_root          # PowerShell；bash 用 rm .template_root
```
完成後這個資料夾就是乾淨 Instance，可跑 skill。**新對話應在這個 Instance 資料夾啟動**（不是在 Template repo）。

## 3. 完整產出測試的 skill 鏈（陪 user 依序跑；user 出創意，agent 跑 skill）

> 觸發 skill 時用 slash command；中文 wrapper 亦可。權威清單見 `_user_manual/skill_registry_full.md`。

| 階段 | skill | 測什麼 |
|---|---|---|
| Bootstrap | `/init-project` | Instance 初始化（.protocol_version / registry 拷貝 / 目錄）|
| A 世界觀 | `/create-world` | W-rules / W-language / V（issue-ful 5 階段）|
| B 角色 | `/create-character` | 一兩個 C-*（聲線卡）|
| B 組織 | **`/create-org`** | ⭐ **新功能**：ORG-*（7 段 issue-ful；無聲線卡）。建一個非人格對抗源（如清道夫公司/某制度）|
| B 關係 | `/create-relationship` | ⭐ C↔C **和 C↔ORG endpoint**（新；至多一端 ORG、禁 ORG↔ORG）|
| B 大綱 | `/create-outline` | P 主線 |
| B 細綱 | `/create-detailed-outline` | CH-* / S-* |
| C 任務包 | `/scene-task <S-ID>` | 單場任務包 |
| C 台詞 | `/dialogue-write <S-ID>` | ⭐ **真實台詞產出**（v01A/B/C）= 完整產出測試核心 |
| C QA | `/qa <dialogue_path>` | 8 份 QA 報告 |
| 輔助 | `/status` `/check-gaps` `/view-*` `/export-*` | 沿途檢查；**特別確認 /status 正確計入 ORG**、check-gaps 掃 11_organizations/ |

## 4. 測試重點（要特別盯的，因為是這批新東西 + 第一次真實端到端）

1. **新 ORG 鏈**：`/create-org` 7 段 issue-ful 流程跑得順嗎？建出的 `11_organizations/<name>.md` 合理嗎？`/create-relationship` 的 C↔ORG endpoint（ORG 端不寫聲線卡）對嗎？`/status` 把 ORG 計入嗎？
2. **不變量**：ORG-* 全程**不該**長出聲線卡、不該被 `/dialogue-write` 當說話者。
3. **真實產出品質**：`/dialogue-write` 出的台詞 + `/qa` 8 報告，是不是 user 真能用的水準（這才是「測試沒問題就開始寫作」的判準）。
4. **L2 隨時可跑**（在 Instance 內）：`python scripts/check_paths.py` / `check_headers.py` / `check_entity_type_consistency.py` / `python -m pytest scripts/tests/ -q`（應 43 pass）。
5. **rough edges**：第一次真實使用，留意任何 skill 指引不清、卡關、產出不如預期 —— 記下來，可能是下一輪要補的。

## 5. 已知**未**做（別期待；要時才補）

- **F8 方向 B**：W-language 文件語體卡（ORG 殘留文件「讀起來」的語體）—— `00_n` §7 只留 hint，DEFERRED。
- **view-org / export-org 獨立 skill** + view-world compose ORG —— DEFERRED；目前看 ORG 直接讀 `11_organizations/<name>.md`。
- **清道夫 R-* opt-in 遷移**：若 user 之前用 `R-清道夫-*` workaround，要遷成 `ORG-清道夫` 是 opt-in，user 明示才做。
- Group 4 觀察項（C-ORG 裸名 ID 碰撞等，非現行 bug）。

## 6. 工具現況 / 權威指標

- **整鏈帳本**：`DECISIONS_LOG.md` v2.10（D-074 F8 Phase 3 + §6.27 amendment / D-075 Batch 5）/ `POST_LOCK_PENDING.md` v0.37。
- **skill 權威清單**：`_user_manual/skill_registry_full.md`。
- **型別權威**：`entity_type_registry.yaml`（11 種 core，含 ORG）；drift 由 `check_entity_type_consistency.py` CI 強制。
- **已封存（DEPRECATED）設計文件索引**：`_design/_DEPRECATED_REGISTER.md` —— 這些勿當活躍指引。
- **協議**：`00_protocol/00_n_組織創建協議.md`（ORG，v0.2 7 段 issue-ful）+ 既有 00_e/00_f/00_g/00_h/00_l。

## 7. 給新對話的起手式

1. 確認 user 已 clone 出 Instance（§2）；新對話在該 Instance 啟動。
2. 跟 user 確認測試故事題材（小而完整即可：一個世界 + 2-3 角色 + 1 個 ORG 對抗源 + 一條主線 + 一兩場戲）。
3. 依 §3 鏈逐 skill 陪跑；§4 重點隨時盯。
4. 跑到 `/dialogue-write` + `/qa` 出真實產出 → 跟 user 一起判「可不可用」。
5. 可用 → user 開始正式寫作（同一個 Instance 繼續長）。有 rough edge → 記下，評估是否要再開一輪工具修補。

## 8. Cross-ref
- `_design/OVERNIGHT_WAKEUP_REPORT.md`（DEPRECATED；整鏈歷史）/ `_DEPRECATED_REGISTER.md`
- `DECISIONS_LOG.md` §6.23-§6.27 / `_user_manual/skill_registry_full.md` / `00_protocol/00_n`
