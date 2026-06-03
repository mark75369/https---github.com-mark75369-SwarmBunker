---
name: 初始化專案
description: /init-project 中文別名 — 觸發新專案初始化流程。實際邏輯參見 .claude/skills/init-project/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Claude Code `/初始化專案` 中文別名 wrapper
優先級：高

# 中文別名 - 初始化專案

本 skill 是 `/init-project` 的中文別名。當使用者以 `/初始化專案` 觸發時，等同於觸發 `/init-project`。

完整流程、五階段規則、`.protocol_version` schema、三 registry copy、`10_art_assets/` 建立、`.gitignore` 規則、rollback、錯誤處理與禁止事項，全部以 `.claude/skills/init-project/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷 Bootstrap 行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/init-project/SKILL.md`。
