---
name: 生成台詞
description: /dialogue-write 中文別名 - 觸發台詞生成（試寫 v01A/B/C / 破格 / 收斂 / 單版迭代）流程。實際邏輯參見 .claude/skills/dialogue-write/SKILL.md。
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-21
適用範圍：Claude Code `/生成台詞` 中文別名 wrapper
優先級：高

# 中文別名 - 生成台詞

本 skill 是 `/dialogue-write` 的中文別名。當使用者以 `/生成台詞 <input>` 觸發時，等同於觸發 `/dialogue-write <input>`。

完整流程、6 階段規則、4 模式（試寫 / 破格 / 收斂 / SINGLE_ITER）、`.protocol_version` schema、D.2.5 task review gate dependency、rollback 與錯誤處理，全部以 `.claude/skills/dialogue-write/SKILL.md` 為權威。

本 wrapper 不展開第二套流程，不自行判斷流程行為，也不覆寫英文主檔的任何規則。執行時請讀取並遵循 `.claude/skills/dialogue-write/SKILL.md`。
