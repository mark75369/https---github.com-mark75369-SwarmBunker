---
name: 缺漏檢查
description: "/check-gaps 中文別名 — 列出 TODO 標記 / 缺漏實體 / view/ 失效。實際邏輯參見 .claude/skills/check-gaps/SKILL.md。"
---

狀態：DRAFT
版本：v0.1
最後更新：2026-05-20
適用範圍：/缺漏檢查 中文 wrapper；對應 /check-gaps
優先級：高

# 中文別名 — 缺漏檢查

## 用途

本 skill 是 `/check-gaps` 的中文別名。

當使用者以 `/缺漏檢查` 觸發本 skill 時，等同於觸發 `/check-gaps`，用來掃描 TODO / INFERENCE / CONFLICT 標記、entities 漏標、缺漏實體，以及 view/ 整合檔失效。

## 觸發語

- `/缺漏檢查`
- Equivalent main skill: `/check-gaps`

## 權威來源

完整流程定義於 `../check-gaps/SKILL.md`，請以該檔內容為準執行。

不要在此 wrapper 內展開另一套流程；不要改寫、簡化或覆蓋英文主 skill 的五階段規則。

## 邊界

本 wrapper 不寫任何檔案，不更新 `.protocol_version`，不自動觸發其他 skill。

若本 wrapper 與 `../check-gaps/SKILL.md` 有任何衝突，以英文主 skill 為權威。
