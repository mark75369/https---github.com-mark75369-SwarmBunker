狀態：DRAFT（骨架）  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：上游 skill 完整語法 + 議題清單 + 範例對話  
優先級：高（Phase B/C 完成後補完整內容）

# 02 上游 Skill

> ⏳ **本章骨架待 Phase B/C 完成後補完整內容**（範例對話、隱藏功能、進階參數）  
> 目前提供 skill 清單 + 議題清單 + 觸發方式

# 1. Skill 清單（20 個）

## 1.1 Create（5 個）

| Skill | 中文別名 | 議題數 | 對應協議檔 |
|---|---|---|---|
| `/create-world` | `/建立世界觀` | 11 | `00_protocol/00_e_*.md` |
| `/create-character <name>` | `/建立角色 <name>` | 9 | `00_protocol/00_f_*.md` |
| `/create-relationship <a> <b>` | `/建立關係 <a> <b>` | 6 | `00_protocol/00_l_*.md` |
| `/create-outline` | `/建立大綱` | 7 | `00_protocol/00_g_*.md` |
| `/create-detailed-outline` | `/建立細綱` | 7 | `00_protocol/00_h_*.md` |

## 1.2 Iterate（5 個）

| Skill | 中文別名 | 行為 |
|---|---|---|
| `/iterate-world` | `/迭代世界觀` | 改現有世界觀 + 反查依賴 |
| `/iterate-character <name>` | `/迭代角色 <name>` | 改現有角色 + 反查依賴 |
| `/iterate-relationship <a> <b>` | `/迭代關係 <a> <b>` | 改關係 + 反查依賴 |
| `/iterate-outline` | `/迭代大綱` | 改主線 + 反查依賴 |
| `/iterate-detailed-outline` | `/迭代細綱` | 改章節 / 場景索引 + 反查依賴 |

## 1.3 View（4 個 — chat 動態組合）

| Skill | 中文別名 | 行為 |
|---|---|---|
| `/view-world` | `/查看世界觀` | chat 印完整世界觀（不寫檔）|
| `/view-character <name>` | `/查看角色 <name>` | chat 印完整角色（不寫檔）|
| `/view-outline` | `/查看大綱` | chat 印完整主線（不寫檔）|
| `/view-detailed-outline` | `/查看細綱` | chat 印完整章節 + 場景（不寫檔）|

## 1.4 Export（4 個 — 寫 view/ 靜態檔）

| Skill | 中文別名 | 行為 | 輸出 |
|---|---|---|---|
| `/export-world` | `/匯出世界觀` | 整合到單檔 | `view/世界觀.md` |
| `/export-character <name>` | `/匯出角色 <name>` | 整合到單檔 | `view/角色_<name>.md` |
| `/export-outline` | `/匯出大綱` | 整合到單檔 | `view/大綱.md` |
| `/export-detailed-outline` | `/匯出細綱` | 整合到單檔 | `view/細綱.md` |

---

# 2. 議題清單預覽

## 2.1 /create-world（11 議題）

| # | 議題 | 必要度 |
|---|---|---|
| 1 | 世界類型快速分類 | REQUIRED |
| 2 | 世界規則最小集 | REQUIRED |
| 3 | 科技水平 | STRONGLY_PREFERRED |
| 4 | 人民生活水準 | STRONGLY_PREFERRED |
| 5 | 各項價值觀 | STRONGLY_PREFERRED |
| 6 | 宗教 | OPTIONAL |
| 7 | 語言層級切片 | REQUIRED |
| 8 | 陣營與階級語言 | STRONGLY_PREFERRED |
| 9 | 類型語氣定位 | REQUIRED |
| 10 | 越界禁區（00_b §2）| STRONGLY_PREFERRED |
| 11 | 拆分規則 | N/A（技術項）|

## 2.2 /create-character（9 議題）

⏳ Phase B 完成後補

## 2.3 /create-relationship（6 議題）

⏳ Phase B 完成後補

## 2.4 /create-outline（7 議題）

⏳ Phase B 完成後補

## 2.5 /create-detailed-outline（7 議題）

⏳ Phase B 完成後補

---

# 3. 觸發方式

3 種方式都行：

1. **直接打 skill 指令**
   ```
   /create-world
   /create-character 主角A
   ```

2. **中文別名**
   ```
   /建立世界觀
   /建立角色 主角A
   ```

3. **從前端複製按鈕**：Dashboard 的「📋 複製 /create-world 指令」按鈕 → 自動複製含 context 摘要的指令 → 貼到外部 chat

---

# 4. 手稿導入觸發語

對應 SPEC §6.2 + UD §10。

```
直接寫檔 [--trust-level=<level>]
```

- 預設：無（路徑 A 從零對話）
- `agent_assisted`：手稿導入 — 你在外部 agent 編輯過
- `external_llm`：手稿導入 — 你從外部 LLM 直接得到

**手稿必須有 markdown structure（`#` / `##` 段落）。**

⚠ trust-level 只影響上游創建，**不影響下游 pipeline**（下游永遠走完整 8 份 QA）。

---

# 5. 待補內容（隨 Phase B/C 補）

- [ ] 每個 skill 完整議題清單（含問題範例）
- [ ] 5 階段對話完整範例
- [ ] 手稿導入完整範例（路徑 B）
- [ ] 衝突 4 選項處理範例
- [ ] 進階參數（如 `--scope=*` / `--skip-issue=N`）
- [ ] 隱藏功能（如「現在 11 議題進度？」「議題 6 改 OPTIONAL」）
- [ ] 各 skill 常見錯誤
