狀態：DRAFT  
版本：v0.1  
最後更新：2026-05-19  
適用範圍：高頻問題集  
優先級：高

# 10 常見問題 FAQ

# 1. 工具定位

## Q1：我能用這工具寫開放世界 RPG 嗎？

**A：可以，但不建議。** 工具設計給「線性主線 + 對話為主」的遊戲（VN、IF、對話 RPG）。開放世界 / 多分支劇情樹在 v1.0 沒原生支援，要自己擴充。

## Q2：我能用這工具自己出版小說 / 漫畫腳本嗎？

**A：可以但偏離設計初衷。** 工具的 8 份 QA 報告（特別是「跨場一致性」「對話張力」）對小說有用，但缺乏小說專屬機制（章節篇幅 / 描寫 / 敘事視角等）。建議當「對白工具」用 + 自己處理描寫。

## Q3：能多人協作嗎？

**A：v1.0 是個人工具。** 設計沒考慮多人協作（mutex / lock / merge 都是個人級）。多人協作要等未來擴充。

---

# 2. 上游建設定

## Q4：跑 /create-world 要多久？

**A：路徑 A（從零對話）2-3 小時 / 路徑 B（手稿導入）10 分鐘。** 但路徑 B 要你的手稿有清楚 markdown structure（`#` / `##` 段落）。

## Q5：跑 /create-character 失敗，agent 說「議題 5 缺漏」怎麼辦？

**A：跑「直接寫檔」要 REQUIRED 議題全部齊備。** 缺 REQUIRED 議題 agent 會拒絕。補答後重貼，或退回正常對話路徑（不加「直接寫檔」）讓 agent 引導你補。

## Q6：手稿導入後設定不滿意，能改嗎？

**A：能。** 跑 `/iterate-world` 或 `/iterate-character`。工具會自動反查依賴，告訴你改了會影響哪些檔。

## Q7：能不能省略某個議題？

**A：v1.0 不能（議題清單 hardcode）。** 計畫中的 D-047（議題 registry）會支援 `core_overrides` 跳過 core 議題 + `user_extensions` 加新議題。預計 Phase A.0 完成後實作。

---

# 3. 下游寫對白

## Q8：/dialogue-write 為什麼一定要產 3 版？只要 1 版可以嗎？

**A：3 版是設計核心。** 給 user 框選亮點再收斂 v02 比直接給 1 版品質高很多。如果你真的只想要 1 版，跑 `/dialogue-write --single-iter`（單版本迭代，跟 agent 迴圈改一版到滿意）。

## Q9：/qa 跑完 8 份報告但都 PASS，但我覺得對白不好怎麼辦？

**A：QA 是機械檢查，不是品味判斷。** 8 份 QA 主要找：類型偏移 / 資訊洩漏 / 聲線不一致 / 節奏 / 張力等結構性問題。對白「好不好」是品味，由你拍板。覺得不好 → 跑 `/dialogue-write --single-iter` 迭代。

## Q10：能不能跳過 QA 直接升 FINAL？

**A：不能。** SPEC §16 文件狀態機要求 FINAL **必須先 QA_PASSED**。你可以**跑 QA 但保留違規亮點**（在 09_e 紀錄人類裁決理由），但不能完全跳過 QA。

## Q11：trust-level agent_assisted 不是可以跳 QA 嗎？

**A：不行。** trust-level **只影響上游 `/create-*` 階段紀錄**，**不影響下游 pipeline**。手稿導入後台詞還是要走 DRAFT → 8 份 QA → REVIEW → FINAL。

---

# 4. 美術資產

## Q12：A-* metadata 要怎麼建？

**A：跟一般 entity 同樣，在 `10_art_assets/<subtype>/<group>.md` 寫 frontmatter `art_metadata` list。** 每個 group .md 含該 group 所有 asset 的 entry（per-character 或 per-group canonical 模型）。

範例：`10_art_assets/portraits/主角A.md` 內 list 含主角A 所有 portrait variants。

## Q13：A-* 的「狀態」（製作中 / 完成 / 缺檔）怎麼標？

**A：在 art_metadata entry 的 `status` 欄位標（active / deprecated / deleted）。** 「製作中」/「未啟動」屬於 v1.0 沒支援的 state — 用 free text 寫在 `state_tags` 或 `notes`，前端 Asset Panel 會解析。

## Q14：缺檔 A-* 引用會怎樣？

**A：parser 偵測會印 WARN「孤立立繪」。** 不阻擋升 FINAL（D-045：A-* 完成度不入 narrative /status）— 由 user 決定要不要等繪師補。

---

# 5. 版本控制 / git

## Q15：要不要 git commit？多久 commit 一次？

**A：每完成一個邏輯單位就 commit。** 例如：跑完 /create-world 一次 commit、寫完一場戲一次 commit、升 LOCKED 一次 commit。工具設計**手動 Save + 手動 commit**（不自動）— 保 git history 乾淨。

## Q16：能不能合作 fork repo？

**A：v1.0 個人工具，沒支援多人 merge。** 你可以自己 fork，但 merge 衝突要手動處理。

---

# 6. 前端工具

## Q17：前端 server 跑不起來怎麼辦？

**A：看 [11 故障排除](11_troubleshooting.md) §1。** 常見問題：port 8765 被佔用 / Python 版本太舊 / 路徑含空白。

## Q18：能用手機開前端嗎？

**A：v1.0 設計 ≥ 1280px 桌面。** < 768px 顯示精簡版（只有 HERO + 場景就緒度）。不建議手機編輯。

## Q19：能多開幾個瀏覽器分頁嗎？

**A：可以。** 多分頁開不同場景 OK。**同時編同場景**會觸發 advisory edit-lock（提示但不強制）+ mtime drift conflict modal（Save 時偵測 + 二選一 reload / 強制覆寫）。

---

# 7. 交付下游

## Q20：JSON Export 跑很慢？

**A：100 場景以下不該慢（< 10 秒）。** 如果慢 → 看 [11 故障排除](11_troubleshooting.md) §4。可能是 parser cache 失效。

## Q21：JSON 給 Unity 工程師後他要做什麼？

**A：寫 5-10 分鐘 Python / C# script，把 JSON 轉成 Unity 對話資料（如 ScriptableObject）。** JSON 格式是固定 `manifest + records[]`，每個 record 含 `key / speaker / content / portrait / bgm / scene_id`。

## Q22：能直接吐成 Yarn Spinner / Ink 等 dialogue 格式嗎？

**A：v1.0 不直接吐。** JSON 是中介層，由外部 script 轉。但你可以寫一份「JSON → Yarn」轉換 script 一次寫永久用。

---

# 8. 改設定

## Q23：改主角性格會影響哪些對白？

**A：跑 `/iterate-character C-主角A` 後 agent 會自動掃描所有 `depends_on: C-主角A` 的檔，列出受影響清單。** LOCKED 檔需先降級（走 09_e 降級紀錄流程）。

## Q24：能不能改 LOCKED 檔？

**A：不能直接改。** 流程：
1. 改 frontmatter `狀態：LOCKED → DEPRECATED`
2. 在 09_e final-gating 紀錄補一條降級紀錄（含理由 / 日期 / 操作人 / 影響）
3. 重做新版本 → 重跑 QA → 升 FINAL → 升 LOCKED

---

# 9. 客製化

## Q25：能不能加自己想到的議題到 /create-character？

**A：v1.0 不行（議題 hardcode）。** 計畫中的 D-047 會加 `issue_type_registry`。預計 Phase A.0 完成後實作。詳見 [07 客製化](07_customization.md) §4。

## Q26：能加自己想到的 entity 類型嗎（如 LOC-* 地點）？

**A：可以。** 編 Instance root 的 `entity_type_registry.yaml` 在 `user_extensions:` 段加。詳見 [07 客製化](07_customization.md) §1。

## Q27：能加自己想到的 QA 模組嗎？

**A：可以。** 寫新 09_x_* 模板 + 編 `qa_type_registry.yaml` 在 `user_extensions:` 段加 + 跑 `/qa --include-user-qa`。詳見 [07 客製化](07_customization.md) §2。

---

# 10. 隱藏 / 進階功能

## Q28：怎麼讓 agent 在對話中印當前議題進度？

**A：說「現在 11 議題進度？」** agent 會印進度條。

## Q29：能不能臨時下調議題重要度？

**A：在 /create-* 對話中說「議題 6 改 OPTIONAL」** 可臨時下調（不寫 registry）。

## Q30：怎麼看一個 dialogue KEY 被哪些場景引用？

**A：前端 Asset Panel 子表「覆蓋」欄會顯示。** 或跑 `/check-gaps --scope=keys` 列全部 KEY 引用反查表。

---

# 11. 出問題

## Q31：agent 跑到一半說「並行衝突」？

**A：另一個 skill 正在寫同個 Instance。** 等 30 秒重試。如果一直失敗 → 看 [11 故障排除](11_troubleshooting.md) §3。

## Q32：parser 報「未知 entity 類型」？

**A：你引用了 entity_type_registry 沒列的 prefix。** 兩種可能：
1. 拼錯（例如 `C-主角A` 寫成 `C主角A`）
2. 用了沒註冊的自訂類型（在 user_extensions 註冊）

## Q33：前端 Save 失敗，跳 LOCKED race modal？

**A：你進 Editor 時是 DRAFT，但編輯期間外部把 source 升 LOCKED 了。** 三選項：
1. 複製降級指令 → 走外部 chat 降級 → 回前端重來
2. 另存 DRAFT proposal → 不覆蓋 LOCKED
3. 取消 → 編輯內容留前端，自己決定

---

# 12. 看不到答案的問題

直接看：

- [11 故障排除](11_troubleshooting.md) — 錯誤訊息對照
- `_design/SPEC.md` — 設計層權威（規格細節）
- `_design/TASKS.md` — 實作層細節
- `_design/POST_LOCK_PENDING.md` — 已知未支援需求

或在你的 repo issue 開 issue（如果有 GitHub repo）。
