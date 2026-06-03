---
name: 檢查
description: /qa 中文別名 — 觸發 8 份 QA 報告必跑（D-043）。實際邏輯參見 .claude/skills/qa/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/檢查` 中文別名 wrapper
優先級：高

# 中文別名 - 檢查

本 skill 是 `/qa` 的中文別名。當使用者以 `/檢查 <input>` 觸發時，等同於觸發 `/qa <input>`。

完整流程、5 階段規則、8 份 QA 報告必跑（D-043；09_a/b/c/d/f/g/h/i）+ UD §2.5.3 v0.3 序列順序、`.protocol_version` schema、D.3.5 收斂 gate dependency、rollback 與錯誤處理，全部以 `.claude/skills/qa/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/qa/SKILL.md`。
