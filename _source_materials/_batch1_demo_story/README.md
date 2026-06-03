狀態：DRAFT
版本：v1.0（Batch 1 端到端實跑 demo 產物保留；2026-06-02）
最後更新：2026-06-02
適用範圍：示範用生成樣本 — 非 Template、非任何正式 Instance 內容
優先級：一般

# Batch 1 端到端實跑 demo 故事（保留樣本）

本資料夾是 11th master frontend session（2026-06-02）做端到端實跑時，由多 agent pipeline 從《蟲潮孤堡》素材生成的一篇**日常小故事《一台修不好的事》**的完整 bible 產物，作為「下游 pipeline 真的跑得通、輸出品質可看」的實證樣本保留。

**這不是 Template、也不是任何正式 Instance 的內容。** 它刻意放在 `_source_materials/`（F7 不掃描安全區），不參與實體進度、不被 parser/check 掃描、不會污染任何正式倉庫狀態。

## 內容（4 場日常小故事，約 86 句台詞）

- `01_world/` 日常向世界觀摘要、`03_characters/main/` 瑟琳+清道夫聲線卡、`04_relationships/` 關係+既有聲線基準（上游消化）
- `05_plot/` 主線大綱+細綱、`06_scene_index/` 場景索引
- `08_dialogue_outputs/` S-01-01~04 四場台詞
- `09_quality_assurance/` AI 味 + 聲線一致性 QA 報告

## 對應紀錄

- 成本與可行性結論見 `_design/BATCH1_COST_FEASIBILITY_REPORT.md`。
- 此次實跑也暴露「agent 會無聲失敗」（S-01-03 一度只回節拍摘要並謊報已寫檔，靠 QA 抓到後重生）—— 是「QA gate 為必要安全網」的實證。
