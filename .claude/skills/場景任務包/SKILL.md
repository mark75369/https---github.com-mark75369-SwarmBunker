---
name: 場景任務包
description: /scene-task 中文別名 — 觸發場景任務包建立流程。實際邏輯參見 .claude/skills/scene-task/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/場景任務包` 中文別名 wrapper
優先級：高

# 中文別名 - 場景任務包

本 skill 是 `/scene-task` 的中文別名。當使用者以 `/場景任務包 <scene_id>` 觸發時，等同於觸發 `/scene-task <scene_id>`。

完整流程、五階段規則、`.protocol_version` schema、D-054 hybrid 讀檔 fallback（per-scene → aggregate）、D-051 後 active 單 marker Template-detect（`.template_root` marker）、rollback 與錯誤處理，全部以 `.claude/skills/scene-task/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/scene-task/SKILL.md`。
