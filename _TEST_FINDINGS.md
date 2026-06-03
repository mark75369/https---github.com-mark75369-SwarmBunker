狀態：DRAFT
版本：v0.1
最後更新：2026-06-03
適用範圍：完整產出測試 — 工具迭代 findings 收集（非實體；測試用）
優先級：高

# 完整產出測試 — 工具 findings（撈迭代點）

> 自主 Workflow 測試過程中發現的工具摩擦/不一致/bug。供測試後評估迭代。
> 環境：Instance=`D:\劇本開發工具\_sandbox\測試專案`（Template clone，frontend-tools-a0f）。

## Findings

### F-001 [minor/設計不一致] create-character / create-org 無 Status Bump，下游關係卡關
- **現象**：`create-world` SKILL 有「Status Bump（解除下游 prereq 卡關）」段，寫檔後自動把 W-rules/W-language/V DRAFT→REVIEW。但 `create-character`、`create-org` SKILL **無**對應段；卡寫成 DRAFT。
- **影響**：`/create-relationship` 前置要求兩端 ≥REVIEW + B.5.5 review gate。角色/ORG 停在 DRAFT → 關係 skill 會被擋。
- **判定**：可能 by-design（B.5.5 是人類 review gate，REVIEW 須人簽）。但與 create-world 的自動升級**不對稱**，值得文件化或補一致行為。
- **自主模式處置**：用獨立 review agent 驗證卡忠實後代行升 REVIEW（記錄 reviewer 身分）。

### F-002 [MAJOR/協議矛盾] create-world §Status Bump 直接抵觸 00_e §8.1
- SKILL §Status Bump 要 agent 寫檔後升 DRAFT→REVIEW；但 00_e 協議 §8.1 第1條明文「agent 不得擅自升 REVIEW/FINAL/LOCKED」。兩份對同一動作給相反指令。SKILL 是 runtime 權威且帶 exception，agent 自行以 SKILL 為準。
- **建議**：00_e §8.1 加註「/create-world Status Bump 為例外」或 SKILL 顯式引 supersede 裁決號。（F-001 是此問題的下游不對稱面。）

### F-003 [MAJOR/下游契約斷鏈] create-character D-050 寫權 vs 00_f/UD §10.9 直接矛盾 → QA 基線斷鏈
- 00_f §6/§10.9 + UD §10.9 要求把：偏移基線→`00_b §5`、專屬髒話→`02_b`、高風險句型→`09_a`、row→`04_a/05_c`。但 SKILL D-050 子裁決2 嚴禁本 skill 寫 03_characters/ 以外。SKILL 說 D-050 supersede，結果這些 append **全做不到**，只能降級成聲線卡 §D hook。
- **影響（重要）**：下游 `09_b 聲線一致性`/`09_a AI味`/`09_f 類型偏移` 應讀的 `00_b §5`/`09_a` 基線**空著** → /qa 屆時可能抓不到基線。4 角色卡都累積同類 TODO，跨 skill 漏接風險。
- **建議**：協議層裁決「這些 append 改由誰/哪階段寫」（補銜接 skill 或放寬特定 append）。**測試影響**：到 /qa 階段我會評估是否由 orchestrator 從 §D hook 回填 00_b §5/09_a 讓 QA 有意義。

### F-004 [MAJOR/並發] .protocol_version phase_log 並發寫入 race
- 並行 create-character/create-org agents 同時 append 同一 phase_log，Edit 連續「file modified since read」失敗，改用 python read-modify-write retry 才落地。SKILL「.protocol_version 寫入規範」假設單一 writer，無鎖/順序策略。
- **範圍**：自主多 agent 並行才會踩；單人正常用不會。**建議**：append-only 鎖 / 每實體獨立 log 片段 / 或記明「並行跑須序列化 phase_log 寫入」。

### F-005 [minor/待拍板] 作品名 蟲潮孤堡(Instance) vs 蟲潮孤島(源素材)
- 堡 vs 島不一致。agent 已在 01_a §4 並列標 INFERENCE 未自行拍板。**待 user 拍板統一**（非阻擋）。

### F-006~F-016 [minor] 其他 frictions（彙整）
- F-006 create-world Split Rules：10.5 衍生禁忌 map 到 §22(劇透控管)語義不吻合，§17 更貼切（agent 兩處都寫兼顧）。
- F-007 create-world 把已填真內容與大量未填模板小節(地區A/勢力A/陣營A…)留在同一 REVIEW 檔 → 易誤導下游以為是真設定。建議收尾清佔位列或標「範圍外，待下游」。
- F-008 create-character SKILL 寫「eight technical sections」但實列 9 段（角色定位…與類型氣質合規）。數字與列舉不一致。
- F-009 create-character §A 落點 wording 不一致（line423「after 角色定位」vs line421「8 技術段之後」）。
- F-010 create-character 三套議題編號（協議 §10.x / registry id / 缺漏表議題N）易混；§10.13→id9、§10.14→id10 因 gap-jump 跳號。建議放對照表。
- F-011 create-character 首個角色去名測試無對照對象；協議未規範 single-character 情況（agent skip+TODO）。
- F-012 create-character 不回填 `03_a 角色總表`（D-050 不授權）→ 4 卡未登索引，索引與卡脫節。
- F-013 create-org：受影響 C-* 未建實體時 depends_on 兩難（懸空 vs「補相關C-*」）。agent 保守只放已建實體+§5描述+TODO。建議協議補規則。
- F-014 [env] parse_frontmatter.py 在 Python 3.14 動態 import 時 @dataclass 拋例外（CLI 單檔 rc=0 正常）；check_paths 227 baseline noise 使 L2 難判讀。建議升相容性或記錄 227 為已知 noise。
- F-015 create-character §B 未規範第一人稱旁白/內心獨白行()是否納入代表台詞。
- F-016 [源素材] 劇本 key `BeforeBattle_021` 重複出現(line93/445)不同台詞 → 下游以 key 索引需注意源檔 key 碰撞。

> **Bible phase 評語**：4 角色聲線卡 + ORG 全 success、獨立 review 逐句 grep 驗證 §B verbatim、無謊報/無聲失敗。聲線忠實度高（review 抓到各角記憶點）。最該迭代的是 3 個 MAJOR（F-002/F-003/F-004），其中 **F-003 會實質影響 /qa**。

---
## Structure phase findings（關係/大綱/細綱）

### F-022 [★BLOCKER級系統性／頭號迭代點] D-050 寫權收窄 vs 全 create-* 協議 §10.x 拆分表系統性矛盾
- **現象**：D-050 子裁決把每個 create-* 的寫權收窄到「自己的主目錄」，但各協議（00_e/00_f/00_g/00_h/00_l）與 UD §10.x 的拆分表**沒同步更新**，仍列出跨檔寫入目標。每個 skill 跑都撞同一矛盾，靠 SKILL 內一句「D-050 supersedes」救，協議表格本身未標。
- **全鏈命中清單（這次實測逐一驗到）**：
  - create-character：`00_b §5`偏移基線 / `02_b`髒話 / `09_a`高風險句型 / `04_a`/`05_c` row（F-003）
  - create-relationship：`02_c §關係禁語` / `05_c`弧線註記（F-017）
  - create-outline：`00_b §3`規模定位 / `00_b §4`類型偏移風險 / `05_b`章節空殼
  - create-detailed-outline：`05_c`弧線 / `05_d`資訊揭露 / `05_e`伏筆 / `00_b §6`高風險基線（只寫 05_b+06_a）
- **後果（直接影響後續 /qa 與 view/export）**：這些跨檔基線**全空**、只活在各 entity 卡的 hook/TODO。下游 09_b(聲線一致)/09_a(AI味)/09_d(資訊控制)/09_f(類型偏移) 應讀的基線位置都沒內容；`05_d 資訊揭露`空 → 蟲災真相揭露控制（S-08-02 核心）只有 05_b 摘要。
- **建議（頭號迭代）**：① 各協議 §10.x 表逐列加「D-050 收窄後此目標改由誰/何時寫」；② 或補一個「跨檔基線回填」銜接 skill/階段；③ 或放寬特定必要 append。**測試處置**：進 /qa 前我會評估由 orchestrator 從各卡 hook 回填關鍵基線（至少 05_d 資訊揭露 + 00_b §5 偏移），讓 QA 測得到真品質。

### F-023 [minor] 04_b 關係變化時間線全空（順序性）
- 文件化鏈順序 relationship 在 detailed-outline 前 → 關係建立時 05_b 章節未存在 → 議題6時間線錨點跳過 → **04_b 整檔無內容**（連 placeholder 都沒）。skill 依協議正確延後（TODO(6) 待 /iterate-relationship 補），但下游掃 04_b 看不到 4 段關係的時間線。
- **建議**：① 文件化鏈順序考慮把 relationship 移到 detailed-outline 後；② 或 relationship 跳 04_b 時在 04_b 留一行 skipped-TODO 指標；③ 或明示 /iterate-relationship 是 detailed-outline 後的必跑補洞步。

### F-024 [minor] 細綱只寫 05_b+06_a，章節級弧線/揭露/伏筆/高風險降為 05_b 摘要（F-022 子集，下游 05_c/05_d/05_e 空）。
### F-025 [minor] ID 漂移：ORG card §6 hook 寫 `R-諾拉-ORG`，正式 ID 為 `R-無名加工公司-諾拉`。建議 hook 用正式 ID。
### F-026 [minor] 04_a/04_b 通用模板示範段(18-19 個)與 00_l 議題輸出結構對齊度低 → agent 改 append 獨立 R-* 段；下游 view/export 聚合需處理「示範段 vs 真 R-* 段」並存。
### F-027 [minor] 細綱 high 章節佔比 44%(4/9) 略超 00_h §10.1 的 40% 疲勞閾值；協議無「戰鬥型作品閾值豁免」指引（agent 自判可接受）。
### F-028 [minor] check_headers「版本格式異常」WARN：升級寫入用長註解版本字串觸發（與全 repo verbose 慣例同類，0 errors 不影響 gate）。warnings 由 52→56。

> **Structure phase 評語**：4 關係（含 C↔ORG 不變量完美）+ 大綱 P + 13 場 + 9 章全 success、全 REVIEW、獨立驗證無謊報。**最該迭代仍是 F-022（系統性 D-050 vs 協議矛盾，跨檔基線全斷）**——這是整個工具最大的結構性問題，且會在 /qa 顯形。

---
## Production Wave 1 findings（S-03-01 / S-05-01 / S-08-02）

> **總評：台詞可用、商業級。3 場全 8/8 QA PASS、UDV 全過、無謊報無聲失敗。ORG 不變量(S-08-02 ORG 不說話、只透過文件現身)完美。聲線忠實度高、AI 味 0、資訊控制模範。工具端到端可產出可用台詞。**

### F-022 影響確認（非阻擋）
- 05_d 逐場揭露 row 空 → 09_d 資訊控制改用 關係§5「不能說出口」+ 任務包§8 知情矩陣 + 06_a + W-rules§22.1 二手推導；結論可靠但缺權威一手 row。
- 00_b §5偏移/§6高風險 空 → 09_b 偏移改用聲線卡偏移段+§A.10。
- 02_c §7/§8.2/§9 角色/場景禁用詞空 → 09_c 用任務包§14.3+02_c §3/§5 全作品詞表掃描。
- **正向**：00_b §1/§2 由 create-world 落地 → 09_a/09_f/09_c 基線完整。F-022 傷害是**部分**非全毀。

### F-029 [minor] UDV 第4條 vs 自主跑 DRAFT 任務包
- /qa Stage 0 UDV 第4條要求 source_task ≥REVIEW，否則 upstream_gate_skipped abort；但自主跑任務包為 DRAFT/TASK_DRAFT。agent 依「自主視為授權」+ phase_log 明記 waiver → 判 WARN 不 abort。SKILL 未寫「自主跑下 UDV 第4條 / D.2.5 waiver 如何互動」→ 下個 agent 可能誤 abort 或誤靜默放行。建議 SKILL 補明。

### F-030 [minor] 台詞檔 QA 狀態欄位多處不同步
- v02 檔同時有：frontmatter `QA 狀態：未檢查`(line10) + `## QA 狀態`表(未檢查) + frontmatter `pipeline_state: QA_PASSED`/`qa_decision: PASS`。/qa 只更新後兩個 frontmatter 欄，前面「未檢查」殘留 → 同檔自相矛盾、易誤讀。建議 /qa 一併更新 QA 狀態表/行，或模板移除冗餘表示。

### F-031 [minor/早期狀態] 09_i 跨場一致性比較集為空
- 專案早期無 FINAL/LOCKED 場 → 09_i 只能做前瞻 continuity、無法實證跨場比對（已在報告明寫，非無聲失敗）。建議 SKILL 對「比較集為空」補明確指引；CH-03/08 定稿後應對 S-05-01 重跑 09_i(scope=arc)。

### F-032 [minor] 8 報模板無「對抗式攻擊切角 / 雙 lens」欄位
- 對抗式立場是 /qa SKILL runtime 要求，但 09_a..09_i 模板本身無對應欄位，agent 須自行加段。模板可用度中上、無阻擋。建議模板補對抗式骨架欄。

---
## Production Wave 2 + 最終驗收 findings

### F-033 [★ERROR級/真bug] dialogue-write 產出 header 漏「優先級」必填欄 → 52 檔 check_headers ERROR
- **根因**：08_b 台詞模板 header 正確（含「優先級：高」），但 dialogue-write skill 產出的 v01A/B/C/v02 header 自訂結構（狀態/版本/最後更新/**來源任務包**/適用範圍/生成模式/修改者/QA 狀態），**漏掉必填「優先級」**。13 場×4 檔=52 檔全 ERROR。
- **嚴重度**：ERROR 級、會擋 check_headers CI gate（L2）。是這次唯一 ERROR 級工具 bug。
- **建議**：dialogue-write SKILL 的輸出 header 規範補回「優先級」欄（對齊 08_b 模板 5 欄）。
- **測試處置**：已批次補「優先級：中」到 52 檔，check_headers 回 0 errors。Instance 可乾淨寫作。

### F-034 [pre-existing] phase_log 既有 S-03-01/S-05-01 qa entry 縮排異常
- Wave1 並發 qa append 時兩筆 entry 縮排嵌錯層級（非 top-level）；Wave2 已用正確 top-level append。屬 F-004 並發 race 的殘留產物，YAML 仍可 parse。建議手動校正縮排或視為 F-004 子證據。

> **Production 全 13 場總評**：13 v02 + 39 試寫 + 104 QA 報告全到齊；**13/13 場 8/8 QA PASS、全可用、0 blockers、UDV 全過、無謊報無聲失敗**。四人場聲線分得開、ORG 不變量(S-08-02)守住。**工具端到端可產出商業級可用台詞。** L2 最終：check_headers 0 err、entity-type 無 drift、pytest 43 pass。

---
## 🏁 完整產出測試 — 最終裁決

**結論：GO（工具端到端可用，可開始正式寫作）。**

### 端到端鏈驗證（10 skill 全跑通，自主 Workflow）
init-project → create-world → create-character×4 → create-org → create-relationship×4(含C↔ORG) → create-outline → create-detailed-outline → scene-task×13 → dialogue-write×13(v01A/B/C→v02) → qa×13(8報) — **全部 success**。

### 產物盤點
W世界3 + V1 + C角色4 + **ORG 1** + R關係4(3 C↔C + 1 C↔ORG) + P1 + CH9 + S13；台詞 13 v02 + 39 試寫；QA 104 報。全 REVIEW。

### 三大核心判準
1. **真實台詞品質 = 可用/商業級**：聲線忠實(§B 文風錨)、潛台詞足、AI 味 0、資訊控制模範。13/13 場 8/8 QA PASS。
2. **ORG 新功能 = 完全可用**：create-org 7 段順、C↔ORG endpoint 正確、**不變量全守**(ORG 無聲線卡/不當說話者/S-08-02 以文件現身/status 計入)。
3. **無聲失敗防護 = 有效**：Stage 0 UDV 全 13 場跑、無謊報、無空殼（上一輪爆雷處這次乾淨）。

### L2 最終：check_headers 0 err（F-033 修後）/ entity-type 無 drift / pytest 43 pass。Template 零污染。

### 工具迭代清單（撈到 34 條，依優先序）
- **F-022 [系統性頭號]**：D-050 寫權 vs 全 create-* 協議 §10.x 拆分表矛盾 → 跨檔基線(00_b §5/§6、02_b、02_c、05_c/d/e、04_b)全沒寫、只剩 hook。QA 靠二手推導仍可做但非權威。**最該修。**
- **F-033 [ERROR級真bug，已暫修]**：dialogue-write 產出 header 漏「優先級」→ 52 檔 check_headers ERROR。
- **F-004 [並發]**：.protocol_version phase_log 多 agent 並發 race（僅自主多 agent 觸發）。
- **F-002**：create-world Status Bump vs 00_e §8.1 矛盾。
- 其餘 F-001/F-005~F-032/F-034：議題編號三套混、§A/技術段數字不一致、03_a 總表不回填、作品名 孤堡vs孤島待拍板、09_i 早期比較集空、UDV第4條 vs 自主DRAFT、台詞QA狀態欄不同步… 詳見上。

### 成本（commercial 規劃用）
13 場全深(v01A/B/C→收斂→8報QA) + 完整 Bible/Structure ≈ **~10M token、4 個 workflow 約 2.4 小時**。長篇數百場需據此估算。




