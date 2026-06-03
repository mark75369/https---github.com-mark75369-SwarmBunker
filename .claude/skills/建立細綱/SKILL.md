---
name: 建立細綱
description: /create-detailed-outline 中文別名 — 觸發章節 CH-* 與場景索引 S-*-* 建立流程。實際邏輯參見 .claude/skills/create-detailed-outline/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：Claude Code `/建立細綱` 中文別名 wrapper
優先級：高

# 中文別名 - 建立細綱

本 skill 是 `/create-detailed-outline` 的中文別名。當使用者以 `/建立細綱` 觸發時，等同於觸發 `/create-detailed-outline`。

完整流程、五階段規則、`.protocol_version` schema、issue_type_registry 動態載入、D-051 後 active 單 marker Template-detect（`.template_root` marker；原 D-049 #2 結構推斷防線已 partial supersede 廢除，詳 DECISIONS_LOG §6.13.2）、rollback 與錯誤處理，全部以 `.claude/skills/create-detailed-outline/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/create-detailed-outline/SKILL.md`。
