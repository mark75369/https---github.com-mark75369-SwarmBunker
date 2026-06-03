---
name: 建立組織
description: /create-org 中文別名 — 觸發 ORG-<name> 組織建立流程。實際邏輯參見 .claude/skills/create-org/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：Claude Code `/建立組織` 中文別名 wrapper
優先級：高

# 中文別名 - 建立組織

本 skill 是 `/create-org` 的中文別名。當使用者以 `/建立組織 <name>` 觸發時，等同於觸發 `/create-org <name>`。

完整流程、五階段規則（issue-ful：動態讀 issue_type_registry 的 00_n_organization 議題清單）、`.protocol_version` schema、`.template_root` marker Template-detect、ORG card 7 段骨架、D-050 寫檔邊界（限 `11_organizations/`）、rollback 與錯誤處理，全部以 `.claude/skills/create-org/SKILL.md`（v0.2）為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/create-org/SKILL.md`。
