狀態：DRAFT（骨架）  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：隱藏功能 / 加速技巧 / 進階用法  
優先級：低（持續累積）

# 09 進階技巧

> ⏳ **本章持續累積**。隨開發過程發現的隱藏功能 / user 用熟之後想要的進階技巧都在這裡。

# 1. agent 對話隱藏觸發語

| 觸發語 | 效果 |
|---|---|
| 「現在 11 議題進度？」 | agent 印當前 /create-* 議題進度條 |
| 「議題 6 改 OPTIONAL」 | 臨時下調議題重要度（不寫 registry）|
| 「直接寫檔」 | 跳階段觸發手稿導入 / 提早寫檔 |
| 「直接寫檔 --trust-level=agent_assisted」 | 同上 + 標 trust-level |
| 「跳階段 4」 | 跳過階段 2-3 探索 / 收斂，直接寫檔 |

⏳ 待 Phase B/C/D 完成後補更多

---

# 2. /qa 進階參數

```
/qa <dialogue_path> --include-user-qa     # 含 user_extensions QA
/qa <dialogue_path> --scope=chapter        # 跨章一致性
/qa <dialogue_path> --scope=arc            # 跨弧線一致性
/qa <dialogue_path> --scope=all            # 全 Instance 一致性
```

⏳ Phase D 完成後補

---

# 3. /dialogue-write 進階參數

```
/dialogue-write S-01-03 --single-iter --note "..." --iter 3
/dialogue-write S-01-03 --converge --picks "v01A.l001,v01B.l003,v01C.l005"
/dialogue-write S-01-03 --experimental --tone=詩化
```

⏳ Phase D 完成後補

---

# 4. /status 進階用法

```
/status                        # 全 Instance 概覽
/status C-主角A                # 單實體完成度
/status --scope=chapter --ch=01 # 單章完成度
/status --json                 # 機器可讀 JSON 輸出
```

⏳ Phase A.0 完成後補

---

# 5. 多場景並行工作流

⏳ Phase A.0F 完成後補

---

# 6. 大量手稿批次導入

⏳ Phase B 完成後補

---

# 7. canon delta（成熟期功能）

⏳ Phase D+ 成熟期實作後補

---

# 8. 多 Instance 管理（多專案共用世界觀）

⏳ 未來擴充

---

# 9. 自架 LLM endpoint 對接

對應 L3_EXPORT_PROMPT_SCHEMA §4 推送方式 lifecycle。

⏳ Phase B 之後實作 + 補

---

# 10. 自訂 frontmatter 欄位（不擴充 SPEC）

⏳ D-047 後補（議題 registry 上線後）

---

# 11. 待補項持續累積區

- [ ] phase_log 修補（手動補漏的紀錄）
- [ ] 多分頁同編的 best practice
- [ ] mtime drift 預防
- [ ] git workflow 與工具整合（pre-commit hook 等）
- [ ] CI/CD 整合（自動 export / 自動 build）
- [ ] 跟其他寫作工具（Scrivener / Obsidian）的橋接
