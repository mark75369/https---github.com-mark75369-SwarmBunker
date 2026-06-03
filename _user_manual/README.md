狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：工具使用說明書入口 + 全章節索引  
優先級：高

# Game Dialogue Bible 使用說明書

# 0. 這是什麼

這是 **Game Dialogue Bible（遊戲對話聖經）工具**的完整使用說明書。

本工具是「**個人遊戲劇本工作室**」 — 一個人 + AI agent，能完整產出視覺小說 / 對話遊戲類劇本（世界觀 + 角色 + 主線 + 對白 + 美術資產引用），並交付給程式 / 翻譯 / 配音等下游工種。

---

# 1. 章節索引

依使用場景查找：

## 第一次使用 / 想了解工具是什麼

| 章節 | 內容 |
|---|---|
| [00 快速入門](00_quick_start.md) | 10 分鐘上手 — 第一次啟動工具到產出第一句對白 |
| [01 工具總覽](01_tool_overview.md) | 工具定位、三層架構、26 個 skill 全表 |

## 日常使用 / 想知道某個 skill 怎麼用

| 章節 | 內容 |
|---|---|
| [02 上游 skill](02_upstream_skills.md) | `/create-*` `/iterate-*` `/view-*` `/export-*`（建設定 / 改設定 / 看設定 / 匯出設定）|
| [03 下游 skill](03_downstream_skills.md) | `/scene-task` `/dialogue-write` `/qa`（寫對白 pipeline）|
| [04 管理 skill](04_management_skills.md) | `/init-project` `/status` `/check-gaps` `/diagnose` `/integrate` |
| [05 前端工具](05_frontend_tools.md) | F1 看板 / F2 場景切換 / F3 三欄並排 / F6 搜尋 / F7 編輯 / Asset Panel / Export Panel |

## 想知道資料怎麼存 / 怎麼自訂

| 章節 | 內容 |
|---|---|
| [06 資料結構](06_data_structure.md) | entity 類型、命名規則、frontmatter schema |
| [07 客製化](07_customization.md) | 自訂 entity 類型 / QA 模組 / 議題清單（未來）/ 00_b 擴充 |

## 想看典型工作流情境

| 章節 | 內容 |
|---|---|
| [08 工作流](08_workflows/README.md) | 5 個典型情境：從零建專案 / 手稿導入 / 寫單場戲 / 改設定 / 交付下游 |

## 進階 / 常見問題 / 故障排除

| 章節 | 內容 |
|---|---|
| [09 進階技巧](09_advanced.md) | 隱藏功能 / 加速技巧 / 多專案管理 |
| [10 常見問題 FAQ](10_faq.md) | 高頻問題集 |
| [11 故障排除](11_troubleshooting.md) | 錯誤訊息對照 + 修復方法 |

---

# 2. 完成度說明

本說明書是 living document — 隨工具開發 phase 進度補充：

| 章節 | 完成度 |
|---|---|
| 00 / 01 / 06 / 07 / 10 / 11 | ✅ v0.1 完整（設計層 lock 已含內容）|
| 04 管理 skill | 🔄 Phase A.0 完成後補 |
| 05 前端工具 | 🔄 Phase A.0F 完成後補 |
| 02 上游 skill | 🔄 Phase B/C 完成後補 |
| 03 下游 skill | 🔄 Phase D 完成後補 |
| 08 工作流 | 🔄 各 phase 完成後補真實案例 |
| 09 進階技巧 | 🔄 持續累積 |

---

# 3. 配套文件

| 角色 | 看什麼 |
|---|---|
| **user（你）** | 本說明書（`_user_manual/`）|
| **CODEX（實作 agent）** | `_design/SPEC.md` + `_design/TASKS.md` + `_design/ARCHITECTURE.md` |
| **下游工種**（程式 / 翻譯 / 配音）| Export 出來的 JSON + MD |

---

# 4. 文件維護紀律

- 本說明書持續更新（非 LOCKED）
- 每個 phase / skill 完成後**同步更新對應章節**（不留到最後寫）
- 新發現的隱藏功能 / 高階技巧進 09 章
- user 反饋的常見問題進 10 章
- 實作期間發現的 error pattern 進 11 章
