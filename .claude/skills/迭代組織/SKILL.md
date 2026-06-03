---
name: 迭代組織
description: /iterate-org skill 的中文 wrapper；執行時以英文主檔為權威。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：Claude Code `/迭代組織` 中文別名 wrapper
優先級：高

# 中文別名 - 迭代組織

本 skill 是 `/iterate-org` 的中文別名。當使用者以 `/迭代組織 <name>` 觸發時，等同於觸發 `/iterate-org <name>`。

完整流程、五階段規則、issue-ful 設計（載 issue_type_registry 的 00_n_organization guidance）、ORG card 7 段、影響範圍雙路反查、`.protocol_version` schema、D-050 寫檔邊界（限 `11_organizations/`）、ORG 無聲線卡不變量、rollback 與錯誤處理，全部以 `.claude/skills/iterate-org/SKILL.md`（v0.2）為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/iterate-org/SKILL.md`。
