狀態：DRAFT（骨架）  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：管理 / 監控 5 個 skill  
優先級：高（Phase A.0 完成後補完整內容）

# 04 管理 Skill

> ⏳ **本章骨架待 Phase A.0 完成後補完整內容**  
> 目前提供 skill 清單 + 用途

# 1. Skill 清單（5 個）

| Skill | 中文別名 | 用途 |
|---|---|---|
| `/init-project` | `/初始化專案` | 建新專案結構（每個 Instance 只跑一次）|
| `/status` | `/進度` | 看整體完成度 + 下一步建議 |
| `/check-gaps` | `/缺漏檢查` | 找出所有 TODO + 缺檔 + 過期 view |
| `/diagnose` | `/診斷` | 純診斷模式入口（不寫檔）|
| `/integrate` | `/整理` | 純整理模式入口（資料轉模板欄位）|

---

# 2. /init-project

## 2.1 啟動

```
/init-project
```

跟 agent 對話 5 分鐘確認：
- 專案中文名稱
- 專案類型（VN / IF / RPG / 其他）
- 是否從 Template 複製作品專屬骨架

## 2.2 產出

- 完整目錄結構（00_protocol/ ~ 10_art_assets/）
- `.protocol_version`（紀錄 Template commit + 初始 phase_log）
- `entity_type_registry.yaml`（Template 複製）
- `qa_type_registry.yaml`（Template 複製）
- `export/` 目錄 + `.gitignore`
- `10_art_assets/` 7 subtype 子目錄結構

## 2.3 待補內容

- [ ] Bootstrap 範例對話
- [ ] Template 微調流程
- [ ] 初始化失敗 troubleshooting

---

# 3. /status

## 3.1 啟動

```
/status
```

## 3.2 輸出

7 段順序印出：

1. **下一步 / Next Actions** — agent 推薦的下個動作
2. **卡點 / Blockers** — 阻擋進度的問題
3. **場景就緒度** — 每個 S-* 的 pipeline_state 進度條
4. **模組狀態總覽** — W / V / C / R / P / CH 等 entity 完成度
5. **三欄區** — pending / blocked / recent activity
6. **A-* Asset Panel** — 7 subtype 美術資產進度（v1.1 獨立 panel）
7. **相關 view 連結清單**

## 3.3 待補內容

- [ ] 完整 /status 輸出範例
- [ ] 三欄區的具體判定邏輯
- [ ] Asset Panel 子表展開

---

# 4. /check-gaps

## 4.1 啟動

```
/check-gaps
/check-gaps --scope=keys    # 只看 KEY 衝突
/check-gaps --scope=assets  # 只看 A-* 缺檔
```

## 4.2 找的東西

- TODO 標記（手稿導入時 STRONGLY_PREFERRED 未答的議題）
- A-* 缺檔（被引用但 `10_art_assets/` 沒有）
- 過期 view（source mtime > view 匯出時間）
- KEY 衝突（全 repo 不 unique）
- frontmatter 缺必填欄位
- 依賴實體未存在（depends_on 引用不存在 entity）

## 4.3 待補內容

- [ ] 各種 gap 類型詳細列表
- [ ] gap 修補流程
- [ ] 自動修補 vs 手動修補

---

# 5. /diagnose

## 5.1 用途

純診斷模式 — 不寫檔，純粹分析。

## 5.2 範例

```
/diagnose 為什麼主角A 聲線一致性 QA 過不了？
```

agent 讀相關檔（聲線卡 + 對白檔 + 09_b 報告）後分析給 chat 印。

## 5.3 待補內容

- [ ] 各類診斷情境範例

---

# 6. /integrate

## 6.1 用途

純整理模式 — 把資料轉成模板欄位（如把對話內容整理到聲線卡的「進階性格」段）。

## 6.2 待補內容

- [ ] 整理範例

---

# 7. 待補（隨 Phase A.0 / A.5 完成補）

- [ ] /init-project 詳細 Bootstrap 流程
- [ ] /status 完整輸出範例
- [ ] /check-gaps 所有 gap 類型
- [ ] /diagnose 多種用法
- [ ] /integrate 用法
- [ ] 5 個 skill 隱藏參數
