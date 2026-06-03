---
name: 進度
description: "/status 中文別名 — 列出實體完成度與缺漏建議。實際邏輯參見 .claude/skills/status/SKILL.md。"
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：/進度 中文 wrapper
優先級：高

# 中文別名 — 進度

本 skill 是 `/status` 的中文別名。當使用者以 `/進度` 觸發時，等同於觸發 `/status`。

完整流程、五階段規則、完成度公式、expected set 推導、缺漏實體建議、下游檔案檢查、時期 C 呈現規則、錯誤處理與禁止事項，全部以 `.claude/skills/status/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行計算完成度，也不覆寫英文主檔的任何規則。

執行時請讀取並遵循 `.claude/skills/status/SKILL.md`。
