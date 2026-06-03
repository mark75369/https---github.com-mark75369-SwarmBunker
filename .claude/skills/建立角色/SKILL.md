---
name: 建立角色
description: /create-character 中文別名 — 觸發角色 C-<name> 建立流程。實際邏輯參見 .claude/skills/create-character/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Claude Code `/建立角色` 中文別名 wrapper
優先級：高

# 中文別名 - 建立角色

本 skill 是 `/create-character` 的中文別名。當使用者以 `/建立角色 <name>` 觸發時，等同於觸發 `/create-character <name>`。

完整流程、五階段規則、`.protocol_version` schema、issue_type_registry 動態載入、D-051 後 active 單 marker Template-detect（`.template_root` marker；原 D-049 #2 結構推斷防線已 partial supersede 廢除，詳 DECISIONS_LOG §6.13.2）、rollback 與錯誤處理，全部以 `.claude/skills/create-character/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/create-character/SKILL.md`。
