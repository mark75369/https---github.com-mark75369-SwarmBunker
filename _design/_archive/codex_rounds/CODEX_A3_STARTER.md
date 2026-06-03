狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：Phase A 後段 A.3 task 啟動包 — 00_e 世界觀創建協議寫作  
優先級：高

# CODEX_A3_STARTER — Phase A 後段 A.3：寫 00_e 世界觀創建協議

# 0. 本檔用途

Wave 2 第二條 task — 寫 `00_protocol/00_e_世界觀創建協議.md`（`/create-world` skill 對應 protocol，含 D-047 議題清單 registry 落地的第一個 protocol）。

**前置條件：** Wave 1 三條全 DONE + push（A.1 必須先完成）。

**與 A.2 / A.0F.1 平行性：** 三條動的檔完全不重疊。

**特殊重要性：** 本 task 是 D-047 issue_type_registry 三層機制（IC §4a Contract D）落地的第一個 protocol — Phase B 5 個 /create-* skill 之一的協議檔。本檔寫好後 A.6（/create-world skill 實作）會引用本協議。

---

# 1. 啟動 prompt（複製整段到新 CODEX 對話）

```
你是 game-dialogue-bible 專案的 CODEX implementer agent。

本輪是「Phase A 後段 A.3 task」— 寫 `00_protocol/00_e_世界觀創建協議.md`（`/create-world` skill 對應 protocol）。

工作資料夾：D:\劇本開發工具
GitHub remote：https://github.com/mark75369/Writing-tools.git
所有最新內容都在 master 分支上，請從這份 repo 讀取。

**你的身份與職責：**

- 你是 implementer — 本輪寫一份新 markdown 檔（`00_protocol/00_e_世界觀創建協議.md`）
- 對應傳統：Wave 2 第二條 task（與 A.2 / A.0F.1 平行可跑）
- documentation-style writer — protocol 完整提問腳本來源 100% 來自 UD §1.1，CODEX **不擅自更動**任何議題提問腳本

**重要邊界（嚴格 scope）：**

- ✗ **不**改任何 LOCKED spec / registry / parser code
- ✗ **不**動 `00_protocol/00_b_反ai味檢查表.md`（A.1 範圍）
- ✗ **不**動 `00_protocol/00_i_專案初始化協議.md`（A.2 範圍）
- ✗ **不**動 `_tools/frontend/`（A.0F.0 / A.0F.1 範圍）
- ✗ **不**寫 /create-world skill 實作（屬 A.6 task）
- ✗ **不**寫其他 /create-* protocol（00_f / 00_g / 00_h / 00_l 屬 B Phase）
- ✗ **不**擅自更動 UD §1.1 已規定的提問腳本與拆分規則（要動須先回 master）
- ✗ **不**提及任何具體作品名 / 角色名 / 設定（協議為通用骨架）

**本 task scope（嚴格限定）：**

依 TASKS v1.4 §A.3（line 586-609）+ UD v0.5 §1.1（完整 11 議題提問腳本 + 拆分 algorithm + frontmatter 規範）+ §1.0.x（共通骨架 10 區段執行細則 + 觸發語字典 + 先決缺失流程）。

### 任務目標

新建 `00_protocol/00_e_世界觀創建協議.md` — `/create-world` skill 對應 protocol（建立 W-rules / W-language / V 三實體 + 作品專屬 00_b §1 / §2 寫入）。

### 具體做法

1. **讀 UD §1.1 整段**（從 §1.1 開始到 §1.1.4 末，約 line 341-690）：
   - §1.1.1 區段 1-9 協議專屬條件
   - §1.1.2 區段 10：**11 項議題 agent 提問腳本**（line 403-674）— 每議題含「為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答 / 跳題」5 欄
   - §1.1.3 與下游的銜接點
   - §1.1.4 與 UI/UX specialist 的標記
2. **讀 UD §1.0.1 ~ §1.0.4**（共通骨架執行細則 / 觸發語字典 / 先決缺失處理 / 跳階段路徑 11 議題必要性表）
3. **讀 SPEC §17.1**（line 1510-1522 — 7 個固定 anchor）+ §17.2（寫入規則 — 00_e 寫 §1 §2 覆寫）
4. **讀 issue_type_registry**（`_design/registries/issue_type_registry.template.yaml`）：`00_e_world` 區段的 10 議題清單（user-facing；不含拆分規則）
5. **章節結構**（依 UD §1.0.1 共通 10 區段 + §1.1 專屬區段）：
   ```
   # 1. 文件目的與適用範圍
   # 2. 啟動條件（先決資料）
   # 3. 階段 1：診斷模式
   # 4. 階段 2：探索 / 補洞對話（依議題清單逐項提問；對齊 D-047 讀 issue_type_registry）
   # 5. 階段 3：收斂模式
   # 6. 階段 4：Codex 執行模式（含「自動拆分」邏輯依 §1.1.2 §10.11）
   # 7. 階段 5：實體驗證（自動呼叫 /status）
   # 8. 禁止事項
   # 9. 缺漏處理
   # 10. 專屬區段 — 11 項議題 agent 提問腳本
       ## 10.1 世界類型快速分類（REQUIRED / locked）
       ## 10.2 世界規則最小集（REQUIRED / locked）
       ## 10.3 科技水平（STRONGLY_PREFERRED）
       ## 10.4 人民生活水準（STRONGLY_PREFERRED）
       ## 10.5 各項價值觀（STRONGLY_PREFERRED）
       ## 10.6 宗教（OPTIONAL）
       ## 10.7 語言層級切片（REQUIRED / locked）
       ## 10.8 陣營與階級語言（STRONGLY_PREFERRED）
       ## 10.9 類型語氣定位（REQUIRED / locked）
       ## 10.10 越界禁區（協議邊界提醒 / STRONGLY_PREFERRED）
       ## 10.11 拆分規則（階段 4 執行指南；agent-side mechanic，不對 user 提問）
   ```
6. **每個議題 §10.1 ~ §10.10 內容**：
   - **直接複製 UD §1.1.2 對應段內容**（為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答跳題 5 欄）
   - 不擅自重寫提問腳本（CODEX 違反此項屬 BLOCKED）
   - 不擅自增加 / 刪除子題
   - 議題 ID 對齊 issue_type_registry.template.yaml 內 `00_e_world` 的 id 1-10
7. **§10.11 拆分規則**：
   - 直接複製 UD §1.1.2 §10.11 line 642-674 完整內容（拆分計畫表 + 寫檔順序 + frontmatter 規範）
   - 對齊 SPEC §17.1 / §17.2 — §1 §2 寫入 00_b 覆寫
8. **D-047 對齊段**（**新增**於 §4 階段 2 末或專門段）：
   - 明示：「agent 在階段 2 啟動時讀 `<instance_root>/issue_type_registry.yaml` 的 `00_e_world` 區段；按 `core + user_extensions − core_overrides` 動態構建議題清單；locked=true 議題不可 SKIP」
   - 引用 Contract D §4a.2（Phase B 行為）
9. **header**（依既有 27 模板風格）：
   ```
   狀態：DRAFT
   版本：v0.1
   最後更新：2026-05-19
   適用範圍：全作品 /create-world skill 對應 protocol
   優先級：高
   ```
10. **frontmatter** YAML block：
    ```yaml
    ---
    entities: []                # 協議檔不貢獻實體
    depends_on: []
    weight: {}
    ---
    ```

---

**必讀文件（按順序）：**

A. 任務權威來源（**完整讀**）
1. `_design/TASKS.md` v1.4（A.3 任務 line 586-609）
2. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.1（整段 line 341-690；含 §1.1.1 ~ §1.1.4 + §1.1.2 完整 11 議題）
3. `_design/UPSTREAM_DOWNSTREAM_SPEC.md` v0.5 §1.0.1 ~ §1.0.4（共通骨架 + 觸發語 + 先決缺失 + 跳階段表）

B. D-047 對齊
4. `_design/registries/issue_type_registry.template.yaml`（v0.1 — 00_e_world 區段 line 50-119；10 議題 id/name/required_level/locked/question_summary/protocol_ref）
5. `_design/INTEGRATION_CONTRACTS.md` v2.1 §4a Contract D（D.1 schema / D.2 Phase B 行為）
6. `_design/DECISIONS_LOG.md` v1.1 §6.9.2（D-047 拍板紀錄）

C. 對齊參考
7. `_design/SPEC.md` v1.2 §17.1（7 anchor）+ §17.2（寫入規則 — 00_e 寫 §1 §2 覆寫）
8. `_design/DATA_FORMAT_SPEC.md` v0.4 §3.2（phase_log schema — 階段 4 寫檔後 append）

D. 風格參考
9. `00_protocol/00_b_反ai味檢查表.md`（A.1 完成 — header / yaml block 風格）

E. 已 LOCKED 不可動文件
10. 所有 `_design/*.md`
11. `scripts/*.py`
12. 既有 27 模板
13. `_tools/frontend/*`
14. `00_protocol/00_b_反ai味檢查表.md`（A.1 範圍）

---

**你要交付的產物：**

唯一新建檔：`00_protocol/00_e_世界觀創建協議.md`

**驗收條件（CODEX 自我驗證）：**

A. 結構驗證
- 中文 header 5 欄 + YAML block (entities=[]/depends_on=[]/weight={})
- 含 10 個主章節對應 UD §1.0.1 共通骨架
- §10 專屬區段含 11 個議題 §10.1 ~ §10.11（順序鎖定，§10.11 為拆分規則）

B. 內容驗證
- §10.1 ~ §10.10 每議題含 5 欄（為什麼問 / agent 怎麼問 / 使用者預期答什麼 / agent 怎麼整理寫檔 / 拒答跳題）
- §10 內容對齊 UD §1.1.2 — 隨機抽 3 個議題確認文字與 UD §1.1.2 對應段一致（不擅自重寫）
- §10.11 拆分規則對齊 UD §1.1.2 §10.11 line 642-674
- §4 階段 2 提問腳本提及「讀 issue_type_registry.yaml 動態構建議題清單」（D-047 對齊）
- 整檔無作品 / 角色名 / 蟲潮孤堡相關詞
- 階段 5 明確要求自動呼叫 /status

C. Parser 驗證
- 跑 `python scripts/check_headers.py` → 0 ERROR
- 跑 `python -c "from scripts.parse_frontmatter import parse_file; r = parse_file('00_protocol/00_e_世界觀創建協議.md'); print(r.header, r.issues)"` → 全 OK

D. 不破壞既有
- `git diff --check` 通過
- 不動既有 27 模板 / _design / scripts / _tools/frontend / 00_protocol/00_b / 00_protocol/00_i

---

**Go / Done 判定指引：**

- **DONE：** 4 個驗收條件全 ✓
- **BLOCKED：** 任一驗收 ✗，回 master

請開始。
```

---

# 2. 完成條件 + 後續

CODEX A.3 完成 → user commit/push → 回 master 對話 → 我推 Phase B（B.1 寫 00_f） / 繼續 A.5 (/init-project skill) / 繼續 A.0F.1。

---

# 3. 文件維護紀律

- 本檔是 CODEX A.3 task 啟動包；完成後 archive
