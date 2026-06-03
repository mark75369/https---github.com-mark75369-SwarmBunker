狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：第一次使用工具的 10 分鐘上手指南  
優先級：最高

# 00 快速入門 — 10 分鐘第一次使用

# 0. 你需要什麼

| 項目 | 說明 |
|---|---|
| **Python 3.10+** | 跑前端 server 用 |
| **Claude Code 或 Cowork** | agent 對話用 |
| **Git** | 版本控制 + push 到自己 repo |
| **瀏覽器** | 開前端工具 |
| **任何文字編輯器** | VS Code / Notepad++ / Sublime 都行 |

---

# 1. 第一次啟動（5 分鐘）

## Step 1：clone 工具

```
git clone https://github.com/<你的-username>/Writing-tools.git
cd Writing-tools
```

## Step 2：建立新專案 Instance

開 Claude Code 或 Cowork，貼以下指令：

```
/init-project
```

或中文別名：

```
/初始化專案
```

agent 會跟你對話 5 分鐘，問：
- 專案中文名稱（如「魔法學院」）
- 專案類型（視覺小說 / 對話遊戲 / 其他）
- 是否要從 Template 複製作品專屬骨架

完成後你會得到一個 Instance 目錄結構：

```
你的專案/
├── 00_protocol/
├── 01_world/
├── 02_vocabulary/
├── 03_characters/
├── 04_relationships/
├── 05_plot/
├── 06_scene_index/
├── 07_scene_tasks/
├── 08_dialogue_outputs/
├── 09_quality_assurance/
├── 10_art_assets/
└── .protocol_version
```

## Step 3：啟動前端工具

```
python _tools/frontend/serve.py
```

Terminal 會印：

```
Serving from D:/你的專案
Open browser: http://localhost:8765
Press Ctrl-C to stop
```

開瀏覽器到 `http://localhost:8765` 看到 Dashboard。

---

# 2. 寫你的第一個世界觀（3 分鐘）

## 路徑 A：從零開始對話建立（適合純新作）

在 Dashboard 點「📋 複製 /create-world 指令」按鈕 → 貼到 Claude Code，agent 會跟你對話：

```
agent：好的，先從議題 1 「世界類型快速分類」開始。
       這是高魔幻 / 低魔幻 / 都會奇幻 / 後啟示錄哪一類？

你：高魔幻，現代地球背景

agent：[繼續問議題 2 ~ 11，約 2-3 小時]
       
       所有議題收齊。寫檔到：
       - 01_world/01_a_世界觀總覽.md
       - 01_world/01_b_世界語言規格.md
       - 01_world/01_c_陣營與階級語言.md
       - 02_vocabulary/02_a-c_*.md
       - 00_protocol/00_b §1 §2 §10（作品專屬部分）
```

## 路徑 B：手稿導入（適合已有 Word / GDoc 設定）

你已經在外部寫好世界觀手稿，貼到 Claude Code 後說：

```
直接寫檔 --trust-level agent_assisted
```

agent 解析手稿的 markdown structure（`#` / `##` 段落），自動拆分到對應檔案，10 分鐘完成。

⚠ 手稿**必須有 markdown 段落結構**（純文字 agent 拒絕）。

---

# 3. 寫第一個角色（1 分鐘）

```
/create-character 主角艾莉
```

agent 跟你對話 9 個議題（角色基本 / 性格 / 動機 / 聲線測試題 / 等），30-60 分鐘產出：
- `03_characters/main/艾莉_聲線卡.md`

---

# 4. 看 Dashboard 確認進度（1 分鐘）

切回前端瀏覽器，按 F5 刷新：

```
整體完成度 23%
  W-rules    ▓▓▓▓▓▓▓▓░ 80%
  W-language ▓▓▓▓▓░░░░ 50%
  V          ▓▓▓░░░░░░ 30%
  C-艾莉      ▓▓▓▓▓▓▓░░ 75%
  ...
```

---

# 5. 接下來該做什麼

進入**日常工作循環**：

```
↓ Bible 建立（前 3 天密集）
1. /create-world          → 世界觀
2. /create-character × N  → 主要角色
3. /create-relationship   → 關係矩陣
4. /create-outline        → 主線
5. /create-detailed-outline → 章節 + 場景索引

↓ Bible 完整後，開始日常寫對白
6. /scene-task            → 任務包
7. /dialogue-write        → 3 版台詞
8. /dialogue-write --converge → v02 收斂
9. /qa                    → 8 份 QA 報告
10. F7 修補 → FINAL → LOCKED

↓ 隨時
F6 搜尋找東西
/status 看進度
/iterate-* 改既有設定

↓ 交付
Export Panel → JSON + MD → 給程式 / 翻譯 / 配音
```

---

# 6. 下一步看什麼

| 想做什麼 | 看哪章 |
|---|---|
| 想了解工具全貌 | [01 工具總覽](01_tool_overview.md) |
| 想知道每個 skill 細節 | [02 上游 skill](02_upstream_skills.md) / [03 下游 skill](03_downstream_skills.md) |
| 想看典型情境演示 | [08 工作流](08_workflows/README.md) |
| 遇到問題 | [10 FAQ](10_faq.md) / [11 故障排除](11_troubleshooting.md) |

---

# 7. 重要原則

1. **agent 寫程式 / 寫對白，你拍板**：agent 永遠給 3 版供選，你框選亮點 + 升級狀態
2. **狀態機由人類控制**：DRAFT → REVIEW → FINAL → LOCKED 升級**都需要 user 明示**，agent 不擅自升級
3. **手稿 trust-level 不影響下游 pipeline**：就算手稿導入，下游台詞還是要跑完整 8 份 QA
4. **改設定一定先看依賴反查**：改主角性格 → 工具會告訴你哪些對白檔受影響
5. **LOCKED 檔不能直接改**：必須先降級為 DEPRECATED 並在 09_e 紀錄理由
