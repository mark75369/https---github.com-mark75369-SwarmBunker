狀態：LOCKED
版本：v1.8（11th master frontend 過夜自主長跑 — F8 Phase 3 / D-074：§3.4 各 skill 對應協議表純新增 `/create-org → 00_n` 列 + `/iterate-*` 5 個 → 6 個（含 ORG）；屬純新增列（既有列不動），比照 D-072 擴充模式；v1.7 → v1.8）
歷史紀錄：v1.7（11th master frontend Batch 4 — F10 / NEW_REQ_34 via D-072：§3.3 新增子節 §3.3.3「Sub-conversation / Parallel-chat 慣例」8 條規則；屬純新增段，不動 §3.3.0/§3.3.1/§3.3.2 既有 LOCKED 內容；同步 AGENTS.md / CLAUDE.md / skill_invocation_guide.md 短指標；v1.6 → v1.7）；v1.6（8th master Cleanup round partial supersede via D-051 — §3.3.2 active wording R7-MA-02 reconciliation：行 633 / 639-642 從「三道檢測 / 三維度檢測 / structural inference」改為「D-051 後 active 兩維度（#1 marker + #3 bootstrap completed）」+ Cross-ref pin 升 00_i v0.3 / init-project v0.3；§3.3.2 supersede 框架 v1.5 既有，本輪只清 active wording 殘留）
最後更新：2026-06-03
適用範圍：Game Dialogue Bible 實作架構規格 / CODEX 實作依據
優先級：最高

# ARCHITECTURE — 實作架構

> **v1.7 → v1.8 變動摘要（2026-06-03，第十一輪 master frontend 過夜自主長跑 — F8 Phase 3 / D-074 ORG authoring stack）：**
>
> 本輪 ARCH v1.8 對 v1.7 做 **純新增（非 supersede）** — §3.4「各 skill 對應協議」表：
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §3.4 各 skill 對應的協議 | D-074（DECISIONS_LOG §6.25） | 純新增 `/create-org → 00_protocol/00_n_組織創建協議.md` 列；`/iterate-*` 由「5 個（W/C/R/P/CH）」改「6 個（W/C/R/P/CH/ORG；ORG 加 00_n context）」。既有列一字不動。 |
>
> **v1.8 不動段：** §1 / §2 / §3.1 / §3.3.* / §4 ~ §13 全部 v1.7 既有完整不動。
>
> **v1.6 → v1.7 變動摘要（2026-06-02，第十一輪 master frontend Batch 4 — F10 / NEW_REQ_34 副對話 lifecycle）：**
>
> 本輪 ARCH v1.7 對 v1.6 做 **純新增（非 supersede）** — 在 §3.3 下新增子節 §3.3.3，比照 D-048 新增 §3.3.0 / D-049 新增 §3.3.2 的擴充模式；既有 LOCKED 內容一字不動。
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §3.3 Skill 內容規範 | D-072（DECISIONS_LOG §6.21） | 新增 §3.3.3「Sub-conversation / Parallel-chat 慣例」段 — 補副對話 lifecycle 8 條規則（只讀不寫 / 明列讀過檔 / 明列未讀限制 / 只回 evidence summary / 主對話負責 skill stage / 不關閉除 user 明示 / reuse 同副對話 / 主對話 wording 範例）；既有 §3.3.0 / §3.3.1 / §3.3.2 / §3.4 全部不動（**註：§3.4 於 v1.8 後由 D-074 純新增列，見上方 v1.8 摘要**） |
>
> **v1.7 不動段（保留 v1.6 LOCKED 原狀）：** §1 / §2 / §3.1 / §3.3.0 / §3.3.1 / §3.3.2 / §3.4 / §4 ~ §13 全部 v1.6 既有完整不動（**§3.4 於 v1.8 後由 D-074 新增列**）。
>
> **對應 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 不變；D-001 ~ D-066 拍板不變；本輪只加 D-072 新議題（NEW_REQ_34 副對話 UX）。同步 root AGENTS.md / CLAUDE.md / `_user_manual/skill_invocation_guide.md` 加短指標（權威規則仍以本段為準，root 檔僅引用——對齊 F14 root context budget 瘦身紀律）。
>
> 第十一輪 master frontend Batch 4 owner：§3.3.3 Sub-conversation / Parallel-chat 慣例段。

---

> **v1.5 → v1.6 partial supersede 變動摘要（2026-05-21，第八輪 master Cleanup round — R7-MA-02 active wording reconciliation）：**
>
> 本輪 ARCH v1.6 對 v1.5 LOCKED 內容做 **minor partial supersede** — §3.3.2 內 D-051 strikethrough block（v1.5 既有）後仍殘留 active wording 與廢除 #2 矛盾，本輪 cleanup：
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §3.3.2 Instance repo 啟動順序（行 633）| D-051（DECISIONS_LOG v1.6 §6.13） | 「三道檢測 PASS」→「兩道檢測 PASS（D-051 後 active #1 marker + #3 bootstrap completed；#2 廢除）」 |
> | §3.3.2 未來 bootstrap skill 擴充規則（行 639-640）| D-051 | 「三維度檢測 / 取代 marker + structural inference」→「兩維度檢測（#1 marker + #3 bootstrap completed）/ 取代 marker 檢測；不引入 D-051 已廢除的 #2 structural inference」 |
> | §3.3.2 Cross-ref（行 642）| D-051 | 00_i v0.2 → v0.3 / init-project SKILL.md v0.2 → v0.3 / 加 D-051 + DECISIONS_LOG §6.13 cross-ref |
>
> **v1.6 不動段（保留 v1.5 LOCKED 原狀）：**
> - §3.3.2 D-051 strikethrough block（行 603-609）— v1.5 既有完整保留
> - §3.3.2 規範本體（檢測規則第 1 條 / 第 3 條 / Template repo 責任 / 為什麼採單一 marker 段）— v1.5 既有完整保留
> - 其他所有段（§1 / §2 / §3.1 / §3.3.1 / §3.3.3+ / §4 ~ §13）— v1.5 既有完整不動
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 不變；D-001 ~ D-053 拍板不變；本輪只 cleanup §3.3.2 R7-MA-02 active wording 殘留（CODEX Round 7 重審識別）。
>
> 第八輪 master Cleanup round owner：R7-MA-02 §3.3.2 active wording reconciliation。

---

> **v1.4 → v1.5 partial supersede 變動摘要（2026-05-20，master 第六輪 Critical patch round）：**
>
> 本輪 ARCH v1.5 對 v1.4 LOCKED 內容做 **partial supersede** — 保留原段內容 + 加 v1.5 標註說明擴充範圍。
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §3.3 Skill 內容規範 | D-049 | 新增 §3.3.2「Template-detect 規範」段 — 補 root `.template_root` marker + `_design/registries/*.template.yaml` + `.protocol_version` 三維度檢測規範；既有 §3.3 / §3.3.0 / §3.3.1 / §3.4 全部不動 |
>
> **v1.5 不動段（保留 v1.4 LOCKED 原狀）：**
> - §1 ~ §13 全部（除 §3.3 加新子節 §3.3.2 外）
> - §3.3.0 multi-agent invocation 慣例段（v1.4 新增）保留
> - 其他所有 v1.3 / v1.4 既有 partial supersede 段保留
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-048 拍板不變；本輪只加 D-049 新議題（M1-CRITICAL-01 Template-detect）。
>
> Master 第六輪 Critical patch round owner：§3.3.2 Template-detect 規範段。

---

> **v1.3 → v1.4 partial supersede 變動摘要（2026-05-20，master 第六輪整合）：**
>
> 本輪 ARCH v1.4 對 v1.3 LOCKED 內容做 **partial supersede** — 保留原段內容 + 加 v1.4 標註說明擴充範圍。
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §3.3 Skill 內容規範 | D-048 | 新增 §3.3.0「Multi-agent invocation 慣例」段 — 補 root AGENTS.md + CLAUDE.md + _user_manual/skill_invocation_guide.md 慣例對齊 4 個 agent 環境（Claude Code CLI / Codex CLI / Codex App / Cowork）；既有 §3.3 / §3.3.1 / §3.4 全部不動 |
>
> **v1.4 不動段（保留 v1.3 LOCKED 原狀）：**
> - §1 ~ §13 全部（除 §3.3 加新子節 §3.3.0 外）
> - §12.A.0.10 patch round 紀錄保留
> - 其他所有 v1.3 既有 partial supersede 段保留
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-047 拍板不變；本輪只加 D-048 新議題（NEW_REQ_7 multi-agent UX）。
>
> Master 第六輪整合 owner：§3.3.0 multi-agent invocation 慣例段。

---

> **v1.2 → v1.3 partial supersede 變動摘要（2026-05-19，master 第五輪整合）：**
>
> 本輪 ARCH v1.3 對 v1.2 LOCKED 內容做 **partial supersede（非 supersede）** — 保留原段內容 + 加 v1.3 標註說明擴充範圍。
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §12 Phase A.0 parser 規格 | D-047 + Stage 0 | 補新增 §12.1.10 issue_type_registry 載入 + 驗證規格（A.0 後續 patch round 落地）；既有 §12.1.1 ~ §12.1.9 全部不動 |
> | §12.x A.0.10 patch round 紀錄 | Stage 0 NO-GO 修補 | 在 §12 末加新 §12.A.0.10「Gate 1 NO-GO patch round 紀錄」 — build_repo_index 整合 cross-ref + entity ID 驗證 + UTF-8 BOM；既有 A.0.1 ~ A.0.9 規格全部不動 |
> | §13 Phase A.0F frontend | D-047 + 兩段制保留 | §13.x A.0F real-data acceptance scope 加 issue registry 編輯 panel mention；既有 A.0F alpha scope 不變 |
>
> **v1.3 不動段（保留 v1.2 LOCKED 原狀）：**
> - §1 ~ §11 全部
> - §6.3 / §6.5 / §6.7（D-043 8 QA 落地）保留
> - §12.1.1 ~ §12.1.9（A.0 parser 9 sub-task 規格）保留
> - §13 既有 A.0F endpoint family / 8 endpoints（D-029）保留
> - 其他所有 v1.2 既有 partial supersede 段保留
>
> **對應 v1.0 LOCKED 不變段：** REQUIREMENTS_LOCK v1.0 north star 不變；D-001 ~ D-046 拍板不變；本輪只加 D-047 新議題 + Stage 0 patch round 紀錄。
>
> Master 第五輪整合 owner：A.0.x issue registry parser 規格 + A.0.10 patch round 紀錄。

---

> **v1.1 → v1.2 partial supersede 變動摘要（2026-05-19，master 第四輪整合）：**
>
> | ARCH 段 | 對應 D-NNN | 動作摘要 |
> |---|---|---|
> | §1.2 Instance repo 結構 | D-023 + D-041 | 補 `10_art_assets/` 目錄結構（7 subtype） |
> | §3.x → 新增 §3.5 | D-038 + 對齊 v0.3 D-NNN | 補「Layer 3 Export A1 prompt 生成器」章節（前端內嵌，無 server CLI） |
> | §6 → 新增 §6.7 | D-043 | 補 `/qa` 改寫對應 8 份報告（既有 6.3 段補 v1.2 註） |
> | §A.0 → 新增 §A.0.x parser 9 大類 | DF §11.1 + D-037 / D-042 / D-044 / D-045 | 補 A.0 parser 必處理項 9 大類規格 |
> | 新增 §10 Frontend Adapter | UX §11.8.3 + Contract C + B.2/B.4 | 新增 frontend adapter 8 個 API endpoint 規格 |
>
> **north-star 對齊原則：** REQUIREMENTS_LOCK v1.0 > D-037~D-046 > D-001~D-036 > specialist v0.3 一致性。  
> 完整跨段對齊參考 `_design/INTEGRATION_CONTRACTS.md` v2.0（master 第四輪整合產出）+ `_design/SPEC.md` v1.1。

# 0. 文件定位

本文件回答「**How**」的問題：

- 檔案實際長什麼樣
- 資料夾結構長什麼樣
- frontmatter 怎麼寫
- skill 用什麼機制實作
- 視圖層怎麼動態組合
- 依賴反查怎麼實作

設計層面的「Why」與決策請見 `SPEC.md`，實作任務拆解請見 `TASKS.md`。

---

# 1. 兩個 Repo 的完整結構

## 1.1 Template repo（`game-dialogue-bible-template`）

```
game-dialogue-bible-template/
├─ AGENTS.md                          已就位
├─ README.md                          已就位（v0.2-clean）
│
├─ 00_protocol/                       通用協議
│  ├─ 00_a_台詞生產協議.md             已就位（模式系統完整）
│  ├─ 00_b_反ai味檢查表.md             ★Phase A 待建（通用骨架版）
│  ├─ 00_c_台詞輸出格式.md             已就位
│  ├─ 00_d_工作流總覽.md               已就位
│  ├─ 00_e_世界觀創建協議.md           ★Phase A 待建
│  ├─ 00_f_角色創建協議.md             ★Phase B 待建
│  ├─ 00_g_大綱創建協議.md             ★Phase B 待建
│  ├─ 00_h_細綱創建協議.md             ★Phase B 待建
│  ├─ 00_i_專案初始化協議.md           ★Phase A 待建
│  ├─ 00_j_迭代協議.md                 ★Phase C 待建
│  ├─ 00_k_台詞生產流程協議.md         ★Phase D 待建
│  └─ 00_l_關係創建協議.md             ★Phase B 待建（C-7 新增）
│
├─ 01_world/                          世界觀模板
│  ├─ 01_a_世界觀總覽.md
│  ├─ 01_b_世界語言規格.md
│  └─ 01_c_陣營與階級語言.md
│
├─ 02_vocabulary/                     詞彙系統模板
│  ├─ 02_a_專有名詞表.md
│  ├─ 02_b_俗稱與黑話表.md
│  └─ 02_c_禁用詞與慎用詞表.md
│
├─ 03_characters/                     角色模板
│  ├─ 03_a_角色總表.md
│  ├─ 03_b_主要角色聲線卡模板.md
│  ├─ 03_c_次要角色與npc模板.md
│  ├─ main/                          （主要角色實例 — Instance 才會有檔案）
│  ├─ minor/                         （次要角色實例）
│  └─ npc/                           （NPC 類型實例）
│
├─ 04_relationships/                  關係模板
│  ├─ 04_a_角色關係矩陣.md
│  └─ 04_b_關係變化時間線.md
│
├─ 05_plot/                           劇情結構模板
│  ├─ 05_a_主線大綱模板.md
│  ├─ 05_b_章節結構模板.md
│  ├─ 05_c_角色弧線表.md
│  ├─ 05_d_資訊揭露表.md
│  └─ 05_e_伏筆與回收表.md
│
├─ 06_scene_index/
│  └─ 06_a_場景索引模板.md
│
├─ 07_scene_tasks/
│  └─ 07_a_單場台詞任務包模板.md
│
├─ 08_dialogue_outputs/
│  ├─ 08_a_台詞版本管理規範.md
│  └─ 08_b_生成台詞檔案模板.md
│
├─ 09_quality_assurance/
│  ├─ 09_a_ai味qa報告模板.md
│  ├─ 09_b_角色聲線一致性檢查模板.md
│  ├─ 09_c_禁用詞檢查報告模板.md
│  ├─ 09_d_資訊控制檢查報告模板.md
│  ├─ 09_e_定稿變更紀錄模板.md
│  └─ 09_f_類型偏移檢查模板.md         ★Phase D 待建
│
├─ archive/                           歷史紀錄區
│  └─ 00_protocol_模式系統公版補丁_v_0_2.md  （APPLIED）
│
├─ scripts/                           檢查腳本（clean 版本）
│  ├─ check_paths.py
│  └─ check_headers.py
│
├─ .claude/                           ★Phase A 待建（Claude Code skills 目錄）
│  └─ skills/
│     ├─ init-project/                Phase A
│     ├─ 初始化專案/                   Phase A（中文別名）
│     ├─ create-world/                 Phase A
│     ├─ 建立世界觀/                   Phase A
│     ├─ status/                       Phase A
│     ├─ 進度/                         Phase A
│     ├─ check-gaps/                   Phase A
│     ├─ 缺漏檢查/                     Phase A
│     ├─ create-character/             Phase B
│     ├─ create-relationship/          Phase B（C-7 新增）
│     ├─ create-outline/               Phase B
│     ├─ create-detailed-outline/      Phase B
│     ├─ view-world/                   Phase C
│     ├─ view-character/               Phase C
│     ├─ view-outline/                 Phase C
│     ├─ view-detailed-outline/        Phase C
│     ├─ export-*/                     Phase C（4 個）
│     ├─ iterate-*/                    Phase C（4 個）
│     ├─ diagnose/                     Phase C
│     ├─ integrate/                    Phase C
│     ├─ scene-task/                   Phase D
│     ├─ dialogue-write/               Phase D
│     ├─ qa/                           Phase D
│     └─ <中文別名依此類推>
│
├─ _design/                           設計文件區（本目錄）
│  ├─ SPEC.md
│  ├─ ARCHITECTURE.md                  本檔
│  ├─ TASKS.md
│  ├─ EXTRACTION_NOTES.md
│  └─ references/
│     └─ 00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md
│
├─ view/                              ★Instance 才會有內容（空目錄保留）
│  └─ .gitkeep
│
└─ .protocol_version.template          ★Phase A 待建（Instance bootstrap 後會填）
```

## 1.2 Instance repo（如《蟲潮孤堡》）

```
<作品名>-dialogue-bible/
├─ AGENTS.md                          從 Template clone
├─ README.md                          從 Template clone（Bootstrap 階段填入作品名等）
├─ .protocol_version                  Instance 特有（紀錄 Template commit + 微調）
│
├─ 00_protocol/                       同 Template 結構
│  ├─ 00_a_台詞生產協議.md             從 Template clone
│  ├─ 00_b_反ai味檢查表.md             Bootstrap 階段可微調（從通用骨架擴充為作品專屬版）
│  ├─ 00_c_台詞輸出格式.md             Bootstrap 階段可微調
│  ├─ 00_d_工作流總覽.md               Bootstrap 階段可微調
│  └─ 00_e–00_j                      從 Template clone（不可微調）
│
├─ 01_world/                          上游創建協議跑完後填入內容
│  ├─ 01_a_世界觀總覽.md
│  ├─ 01_b_世界語言規格.md
│  └─ 01_c_陣營與階級語言.md
│
├─ 02_vocabulary/                     上游創建協議跑完後填入內容
├─ 03_characters/                     上游創建協議跑完後填入內容
│  └─ main/、minor/、npc/             具體角色檔案
├─ 04_relationships/                  上游創建協議跑完後填入內容
├─ 05_plot/                           上游創建協議跑完後填入內容
├─ 06_scene_index/                    上游創建協議跑完後填入內容
├─ 07_scene_tasks/                    日常使用累積（每場一個任務包）
├─ 08_dialogue_outputs/               日常使用累積（每場多版本台詞 + 定稿）
├─ 09_quality_assurance/              日常使用累積（QA 報告）
│                                     v1.2：含 09_a / 09_b / 09_c / 09_d / 09_e / 09_f / **09_g / 09_h / 09_i**
│                                     （D-043 — 09_g 節奏感 / 09_h 對話張力 / 09_i 跨場一致性 v1.2 新增）
├─ 10_art_assets/                     **v1.2 新增 via D-023 + D-041 — A-* 美術資產 metadata（per-file SoT）**
│  ├─ 10_a_portrait_index.md          A-portrait-* 索引
│  ├─ 10_b_background_index.md        A-bg-* 索引
│  ├─ 10_c_cg_index.md                A-cg-* 索引
│  ├─ 10_d_sfx_index.md               A-sfx-* 索引（v1.2 新）
│  ├─ 10_e_bgm_index.md               A-bgm-* 索引（v1.2 新）
│  ├─ 10_f_voice_index.md             A-voice-* 索引（v1.2 新）
│  ├─ 10_g_ui_index.md                A-ui-* 索引（v1.2 新；取代 v0.1 icon）
│  ├─ portraits/                      A-portrait-* per character metadata
│  ├─ backgrounds/                    A-bg-* per scene / global
│  ├─ cg/                             A-cg-* per scene / global
│  ├─ sfx/                            A-sfx-* per group（v1.2 新）
│  ├─ bgm/                            A-bgm-* per mood / chapter（v1.2 新）
│  ├─ voice/                          A-voice-* per character（v1.2 新；含該角色所有 voice line）
│  └─ ui/                             A-ui-* per UI 區塊（v1.2 新）
│
├─ 11_items/                          **v1.2 預留接口（本輪不實作；DF §7 reserved_prefixes）**
├─ 12_ui_text/                        **v1.2 預留接口（本輪不實作）**
├─ 13_skills/                         **v1.2 預留接口（本輪不實作）**
│
├─ export/                            **v1.2 新增 via D-038 — Layer 3 Export 輸出目錄；加 .gitignore**
├─ archive/                           歷史紀錄
├─ scripts/                           從 Template clone
├─ .claude/skills/                    從 Template clone
│
├─ entity_type_registry.yaml          **v1.2 新增 via D-025 — Instance bootstrap 時從 Template 複製**
├─ qa_type_registry.yaml              **v1.2 新增 via D-043 + DF §8 — 同上**
│
└─ view/                              `/export-*` 跑過後才有內容
   ├─ 世界觀.md
   ├─ 角色_<name>.md
   ├─ 大綱.md
   └─ 細綱.md
```

---

# 2. Frontmatter 規範

## 2.1 既有檔案的 markdown-style header

既有 27 份模板都使用 markdown 風格 header：

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-07
適用範圍：通用模板
優先級：高
```

`scripts/check_headers.py` 可正確解析這種格式（支援半形 / 全形冒號）。

## 2.2 唯一 Canonical Schema（CODEX 審查回饋鎖定）

依 SPEC 第 5.2 節，**只有一種格式**：既有中文 header 行 + 後續 YAML block 標記實體、依賴、權重。三份設計文件以此為準，不再提供 A/B 兩種方案。

```markdown
狀態：DRAFT
版本：v0.1
最後更新：2026-05-17
適用範圍：主角A 聲線卡
優先級：高

---
entities:
  - C-主角A
  - R-主角A-反派B
depends_on:
  - W-rules
  - W-language
weight:
  C-主角A: 1.0
  R-主角A-反派B: 0.3
---
```

**Parser/Helper 實作要點**（給 Phase A.0）：

1. **混合 header 解析**：先解析中文 header 5 行（接受半形 / 全形冒號），再解析後續 YAML block
2. **YAML block 偵測**：以「`---` 行起頭、`---` 行結尾」為界，介於兩者間為 YAML 內容
3. **欄位 normalization**（O1 鎖定）：
   - `entities` 無 YAML → 回傳空 list `[]`
   - `depends_on` 無 YAML 或欄位缺漏 → 回傳空 list `[]`
   - `weight` scalar → 自動展開為 per-entity map：`{e: scalar for e in entities}`
   - `weight` map → 維持 map（但驗證 keys ⊆ entities）
   - `weight` 完全缺漏 → 預設 scalar 1.0 → 展開為 map
   - 下游欄位（scene_id 等）缺漏 → 回傳 `None`
4. **無 YAML block 容忍**：協議檔（00_*）通常沒有 `entities`/`depends_on`/`weight`，parser 必須能接受純 header 檔
5. **缺欄處理**：必填欄位（中文 header 5 欄）缺漏 → ERROR；YAML block 欄位缺漏 → WARN
6. **DERIVED 與 APPLIED 狀態**：parser 必須接受這兩個目錄專用狀態（DERIVED 限 `view/`，APPLIED 限 `archive/`）
7. **下游欄位識別**：parser 偵測到 scene_id 等下游欄位時，標記檔案為「pipeline 產物」（影響 `/status` 分類）

**Parser 回傳結構（O1）：**

```python
{
    "header": {
        "狀態": "DRAFT",        # str
        "版本": "v0.1",
        "最後更新": "2026-05-17",
        "適用範圍": "...",
        "優先級": "高",
    },
    "yaml": {
        "entities": ["C-主角A"],         # list[str]，無 YAML → []
        "depends_on": ["W-rules"],       # list[str]，無 YAML → []
        "weight": {"C-主角A": 1.0},      # dict[str, float]，scalar 已展開
        # 下游欄位（僅 pipeline 產物有）
        "scene_id": None,                # str | None
        "source_task": None,             # str | None
        "source_dialogue": None,         # str | None（單一台詞檔，/qa 用）
        "source_dialogues": None,        # list[str] | None（複數，--converge 收斂用）
        "pipeline_state": None,          # str | None
        "mode_tag": None,                # str | None
        "qa_decision": None,             # str | None
        "qa_type": None,                 # str | None（僅 QA 報告）
    },
    "is_pipeline_artifact": False,       # bool（依下游欄位是否存在判定）
}
```

**`depends_on` 欄位用法**（C-9 裁決：選 C frontmatter 標記）：

- 標的：本檔案內容若依賴其他實體（即「該實體變動時，本檔案也應被視為受影響」）
- 例：`01_c 陣營與階級語言.md` 內容依據 W-rules 衍生 → `depends_on: [W-rules]`
- 初值：可為空 `[]`，使用者後續逐步補完
- 反查方向：`/iterate-*` 修改 X 實體 → 找 frontmatter 中 `depends_on` 含 X 的所有檔案，列入影響範圍

`scripts/check_headers.py` 需在 Phase A 同步更新以支援 YAML block 解析（見 TASKS A.0）。

## 2.3 完成度計算（給 `/status` skill 實作參考）

偽碼：

```python
def calculate_entity_completion(entity_id, all_files):
    contributing = []
    for f in all_files:
        if entity_id in f.entities:
            weight = f.weight.get(entity_id, 1.0) if isinstance(f.weight, dict) else f.weight
            score = STATUS_SCORE[f.status]  # DRAFT=25, REVIEW=75, FINAL/LOCKED=100, else=0
            contributing.append((score, weight))
    if not contributing:
        return 0
    total_weighted_score = sum(s * w for s, w in contributing)
    total_weight = sum(w for _, w in contributing)
    return total_weighted_score / total_weight
```

`/status` 輸出範例：

```
=== 邏輯實體完成度 ===

W-rules               100%  (FINAL)
W-language             75%  (1 REVIEW)
V                      50%  (3 DRAFT)
C-主角A                75%  (1 REVIEW + 1 DRAFT in 04_a)
C-反派B                25%  (1 DRAFT)
R-主角A-反派B           50%  (聲線卡與關係矩陣中該對段落均 DRAFT)
P                       0%  (尚未建立)
CH-01                  25%
CH-02                   0%
...

=== 缺漏實體 ===
- P：主線尚未建立，建議跑 /create-outline
- CH-03 ~ CH-12：章節尚未建立，建議完成主線後跑 /create-detailed-outline
```

---

# 3. Skill 實作機制

## 3.1 Skill 目錄結構

每個 skill 是 `.claude/skills/<name>/` 一個資料夾，內含一份 `SKILL.md`：

```
.claude/skills/init-project/
└─ SKILL.md
```

`SKILL.md` 結構：

```markdown
---
name: init-project
description: 建立新 Instance repo 的 Bootstrap 流程。從 Template clone 後執行，引導使用者完成專案初始化、Template 微調、`.protocol_version` 紀錄。
---

# /init-project Skill

## 用途
[skill 在什麼情境用]

## 流程
[詳細流程，呼叫哪個協議、執行哪些動作]

## 輸入
[skill 接收的資料]

## 輸出
[skill 產生的檔案 / 訊息]

## 邊界
[skill 不做什麼]
```

## 3.2 雙語別名實作

每個 skill 同時有英文與中文資料夾，**內容指向同一份 SKILL.md**：

```
.claude/skills/
├─ init-project/
│  └─ SKILL.md                  ← 主實作
└─ 初始化專案/
   └─ SKILL.md                  ← 內容指向上面那份
```

**實作策略選項**（CODEX 在 Phase A 擇一）：

**選項 1：符號連結（symlink）**
```
.claude/skills/初始化專案/SKILL.md → ../init-project/SKILL.md
```
優點：永遠同步、零維護。
缺點：Windows 對 symlink 支援不一致（需開發者模式或管理員權限）。

**選項 2：Wrapper 檔（最小重定向）**
```markdown
---
name: 初始化專案
description: 別名 — 觸發 init-project skill。詳見 init-project/SKILL.md。
---

# 中文別名

本 skill 是 `init-project` 的中文別名，實作見 `../init-project/SKILL.md`。

[包含主 skill 完整內容的 include 或重定向指示]
```

**選項 3：複製主檔內容**
完整複製一份。
優點：相容性最強。
缺點：兩份要同步維護。

**鎖定（C-10 裁決：選 A wrapper + smoke test）：選項 2（Wrapper 檔）**

理由與配套：
- 比起 symlink，wrapper 跨 host（Windows / macOS / Linux / Claude Code / CODEX APP）相容性最好
- 比起複製，wrapper 一份實作邏輯，未來改動只改主 skill 不會漏
- **Phase A 必須新增 smoke test 任務**：實際以中文 slash command 觸發，確認 agent 真的執行了主 skill 的流程，而不是只看 description 就結束
- 若 smoke test 在某 host 失敗 → 該 host 改用選項 3（複製）作為 fallback；smoke test 紀錄 fallback 結果到 `.protocol_version`

Wrapper SKILL.md 內容範本：

```markdown
---
name: 初始化專案
description: 中文別名 — 觸發 init-project skill。請執行 ../init-project/SKILL.md 的完整流程。
---

# 中文別名 — 初始化專案

本 skill 是 `/init-project` 的中文別名。
完整流程定義於 `../init-project/SKILL.md`，請以該檔內容為準執行。

當使用者以 `/初始化專案` 觸發本 skill 時，等同於觸發 `/init-project`，
不要在此 wrapper 內展開另一套流程。
```

## 3.3 Skill 內容規範

所有 skill 的 SKILL.md 必須說明：

| 區塊 | 內容 |
|---|---|
| `frontmatter name` | skill 名稱（kebab-case 英文或中文） |
| `frontmatter description` | 50–200 字描述，agent 依此判斷是否觸發 |
| `## 用途` | 使用情境、適用對象 |
| `## 觸發協議` | 此 skill 對應的協議文件路徑 |
| `## 流程` | 5 個階段（依共通骨架）的具體執行步驟 |
| `## 輸入` | 使用者要提供什麼 |
| `## 輸出` | skill 會建立／修改哪些檔案 |
| `## 邊界` | 不做什麼、不可越界什麼 |
| `## 錯誤呈現規則` | 沿用 TASKS §1.5 的錯誤訊息四件套（What / Where / Why / 下一步）；區分使用者錯誤（`✗`）與系統狀態未滿足（`⏸`）；不暴露 enum 鍵 / stack trace 給使用者 |

### 3.3.0 Multi-agent invocation 慣例（v1.4 新增 via D-048）

**M1 user-test 發現：** 26 skill 中只有 Claude Code CLI user 能用 `/init-project` 等 slash command 直接觸發；Cowork / OpenAI Codex CLI / Codex App 的 user 必須手動貼 prompt 引導 agent 讀 SKILL.md。為對齊 multi-agent ecosystem，本工具補 **root agent-discovery 檔慣例** + **manual fallback**。

**4 個 agent 環境的 invocation 機制：**

| Agent 環境 | discovery 機制 | invocation 方式 |
|---|---|---|
| **Claude Code CLI**（Anthropic） | 自動讀 root `CLAUDE.md` + 自動 discovery `.claude/skills/*/SKILL.md` | `/init-project` 等 slash command 直接觸發 |
| **OpenAI Codex CLI** | 自動讀 root `AGENTS.md`（Codex 慣例） | user 在 chat 內提 skill name，agent 從 AGENTS.md 找到 SKILL.md 路徑後讀檔執行 |
| **Codex App**（OpenAI） | 自動讀 root `AGENTS.md` | 同 Codex CLI |
| **Cowork**（Anthropic Claude Desktop App / 本工具）| **不**自動讀 root CLAUDE.md / .claude/skills/ | user 手動貼 `_user_manual/skill_invocation_guide.md` 對應 skill 段的 copy-paste prompt |

**3 個檔的對應職責：**

1. **`AGENTS.md`（root）：** OpenAI Codex ecosystem 慣例自動 discovery 檔
   - 內容：工具總述 / 26 skill 清單（含 path / 觸發條件 / 用途摘要） / 工作流程說明 / Codex-specific invocation 範本
   - 維護：每加新 skill 同步 +1 entry
   
2. **`CLAUDE.md`（root）：** Anthropic Claude Code CLI 慣例自動 discovery 檔
   - 內容：與 AGENTS.md 90% 共享（工具總述 + skill 清單 + 工作流程）
   - 差異：Claude Code-specific invocation 範本（強調 slash command 直接觸發）
   - 維護：每加新 skill 同步 +1 entry（兩處）
   
3. **`_user_manual/skill_invocation_guide.md`（NEW_REQ_2 manual scope）：** Cowork / Codex App user 的 copy-paste fallback
   - 內容：每 skill 1 段對應的「給 agent 的 prompt 範本」（user 手動貼到 chat）
   - 對齊：AGENTS.md / CLAUDE.md 的 skill 清單；但格式是 copy-paste-ready prompt
   - 維護：屬 NEW_REQ_2 user_manual 持續寫作範疇

**規則（D-048 落地）：**

- AGENTS.md + CLAUDE.md 必須對齊 — 兩份檔 skill 清單同步（CI / pre-commit hook 可選但本輪不強制）
- 不採候選 a：**禁止**每 skill 加 `.claude/skills/<name>/INVOKE.md`（避免 26 維護點）
- 新 skill 上線流程加一步：「同步更新 AGENTS.md + CLAUDE.md + skill_invocation_guide.md」
- Phase A.12 task 落地 v1 內容（含本輪所有 5 skill：init-project / create-world / status / check-gaps + 4 中文 wrapper）

**Cross-ref：** DECISIONS_LOG §6.10.2 D-048 / POST_LOCK_PENDING NEW_REQ_7 RESOLVED / TASKS v1.5 A.12 / M1 user-test Phase 2 finding。

### 3.3.2 Template-detect 規範（v1.5 新增 via D-049；v1.5 partial supersede via D-051 — 第二道防線移除）

> **D-051 partial supersede note（DECISIONS_LOG v1.9 §6.13.2 / 2026-05-20）：**
>
> 本段原 D-049 設計兩道防線（#1 marker + #2 registry inference）— 第二道防線在 fresh Instance clone 場景必然 false-positive（Template + fresh Instance file-state 完全相同）→ 反而擋下合理 bootstrap。**D-051 partial supersede：移除第二道防線；保留條件 #1 marker 為唯一 explicit Template-detect 信號。**
>
> 落地：00_i v0.3 + .claude/skills/init-project/SKILL.md v0.3。本段保留歷史紀錄 + 設計演進說明；agent runtime 紀律以 00_i v0.3 / init-project SKILL.md v0.3 為權威。未來 ARCH v1.6 cleanup round 可考慮把本段 prune 為單防線描述（不阻 7th master handoff）。

**M1-CRITICAL-01 發現：** user 跑 /init-project 透過 Cowork 在 Template repo（D:\劇本開發工具）上跑通完整 5 階段；Template 被污染。根因為 00_i §2 既有啟動條件無法區分 Template vs Instance。本段定義所有未來 bootstrap 類 skill（含 /init-project + Phase B+ 預定的其他 /init-* 系列若有）必須遵循的 Template-detect 規範（v1.5 兩道防線 → D-051 後單防線）。

**Template repo vs Instance repo 結構差異：**

| 維度 | Template repo | Instance repo（已 bootstrap）| Instance repo（剛 clone，未 bootstrap）|
|---|---|---|---|
| 目錄結構（00_protocol/ / 01_world/ ...）| ✓ 存在 | ✓ 存在 | ✓ 存在 |
| `_design/registries/*.template.yaml` | ✓ 存在 | ⚠ 可能存在（user 是否清理視個別 Instance）| ✓ 存在（剛 clone） |
| `.protocol_version` | ✗ 不存在 | ✓ 存在 + bootstrap completed | ✗ 不存在 |
| `.template_root` marker | ✓ 存在 | ✗ 不存在（bootstrap 前 user 已刪） | ⚠ 應該已刪（user bootstrap 前的責任） |

**檢測規則（v1.5 原 D-049 三維度 → v1.5 partial supersede via D-051：條件 #2 廢除；當前 active 兩維度 #1 + #3）：**

任何 bootstrap 類 skill 在 Stage 1 開始前，agent 必須依下列順序檢測：

1. **`.template_root` marker 檢測（第一道防線 — explicit signal；**v1.5 active**）：**
   - 若 root 存在 `.template_root` → 拒絕執行 + 印「⏸ 條件未滿足 / 此目錄是 Template repo」拒絕文案（含 What/Where/Why/下一步）
   - 提示 user：若已決定為新 Instance，請手動刪 `.template_root` 後重跑

2. ~~**registries template 殘留 + 未 bootstrap 推斷（第二道防線 — automatic inference）：**~~
   - **【D-051 partial supersede — 本條規則已廢除 / 移出 active spec】**
   - 原 D-049 設計：若 `_design/registries/*.template.yaml` 存在 **AND** `.protocol_version` 不存在 → 拒絕執行
   - **廢除理由：** fresh Instance clone（user 已刪 `.template_root`）file-state 跟 Template 完全相同 → 此規則必然 false-positive → 反而擋下合理 bootstrap
   - **D-051 拍板：移除本條件；防線 #1（marker）為唯一 explicit Template-detect 信號**
   - 詳 DECISIONS_LOG v1.9 §6.13.2 D-051 / 00_i v0.3 §2 / init-project SKILL.md v0.3
   - **本段保留作歷史紀錄；agent runtime 不再 enforce 此規則**

3. **既有 bootstrap completed 檢測（D-042 既有；**v1.5 active**）：**
   - 若 `.protocol_version` 存在 + phase_log 含 `phase: bootstrap, status: completed` → 拒絕 rerun
   - 此規則 catch user 已 bootstrap 的 Instance 試圖重跑

**為什麼採單一 explicit marker 而非互補多防線（D-051 後設計收斂）：**

- 條件 #1（marker）是 explicit signal — 強迫 user 對「這目錄是 Instance」做出明示動作（刪 marker），降低誤跑風險
- ~~原 D-049 設計：條件 #2 是 automatic inference 互補~~ — **D-051 後廢除**（因 fresh Instance clone 無法跟 Template 區分；條件 #2 必然 false-positive 反而擋合理 bootstrap）
- 「user accidentally 刪 Template marker」屬罕見 user error；git checkout / git diff 可立即發現 + 救回 → 不需要 inline 防線兜底（屬已知 edge case，由 git history 復原）
- 條件 #3（bootstrap completed）仍 active 防 rerun

**Template repo 自身的責任：**

- Template repo root 必須有 `.template_root` marker file（含說明何時可刪）
- Template repo 不得有 `.protocol_version`（若 Template 有就違反 §3.3.2 基本前提）

**Instance repo 啟動順序（user-facing）：**

```
1. git clone <template-url> <new-instance-dir>     # user 動作
2. cd <new-instance-dir>                            # user 動作
3. rm .template_root                                # user 動作（D-049 顯式 signal）
4. 跑 /init-project（任一 agent 環境）              # agent 跑 §3.3.2 active 兩道檢測（#1 marker + #3 bootstrap completed；D-051 後 #2 廢除）PASS 後進 Stage 1
5. 完成 bootstrap → `.protocol_version` 寫好         # agent 動作
```

**未來 bootstrap 類 skill 擴充規則：**

- 若 Phase B+ 新增其他 /init-* 系列 skill（如 /init-character-pack / 未來擴充類型），必須同等遵循 §3.3.2 active 兩維度檢測（D-051 後 #1 marker + #3 bootstrap completed）
- 不允許新 skill 用「user 一句話確認」這種 weak check 取代 `.template_root` marker 檢測
- **不引入 D-051 已廢除的 #2 structural inference**（registries-template 存在 + .protocol_version 不存在 → BLOCK）— 該規則對 fresh Instance clone 必然 false-positive，已由 D-051 partial supersede 移出 active spec

**Cross-ref：** DECISIONS_LOG §6.11.2 D-049（兩道防線原拍板）/ DECISIONS_LOG §6.13.2 D-051（partial supersede 移除 #2）/ POST_LOCK_PENDING NEW_REQ_8 RESOLVED（D-049 落地；後 D-051 partial supersede）/ 00_protocol/00_i v0.3 §2 條件 #5（#6 已 D-051 移除）/ .claude/skills/init-project/SKILL.md v0.3 啟動前檢查 / `.template_root` marker file / M1 user-test post-finding / M2 testing fresh Instance clone false-positive observation。

### 3.3.1 錯誤呈現一致性要求（時期 C 整合）

所有 skill 在拒絕執行或回報錯誤時，必須遵循 UX_SPEC §8 的通用結構（已整合至 TASKS §1.5）。要點：

- 標題用 `## ✗ 無法執行 / Cannot Proceed`（使用者錯誤）或 `## ⏸ 條件未滿足 / Prerequisites Not Met`（系統狀態未滿足）
- 四欄必含：What / Where / Why / 下一步
- 「下一步」用祈使句，避免「應該」「可能」「建議考慮」
- 不顯示 stack trace、不顯示 error code、不顯示內部 enum 鍵（`pipeline_state: TASK_REVIEW` → 改「任務包已升 REVIEW」）
- 多錯誤累積時用「彙整 + 逐項展開」（標題加「— N 項問題」+ 整體下一步）
- 空狀態文案用 italic 包覆，且要說明「為什麼是正常」或「下一步可考慮」

詳細格式範本見 DECISIONS_LOG.md R13–R17 與 UX_SPEC §8。

### 3.3.3 Sub-conversation / Parallel-chat 慣例（v1.7 新增 via D-072）

**M4 user-test 發現（F10 / NEW_REQ_34）：** 量產期間 user 放入大量既有人設與 docx 後，主對話需保留 skill 階段推進、不適合塞長素材，遂另開**副對話**讀取既有劇本／docx 萃取聲線。副對話讀取效果良好，但出現 UX 問題：**主 agent 太早關閉副對話**（user 還想追讀就被收掉）。本段把「主對話 / 副對話」分工固化為慣例，補 §3.3.0 multi-agent invocation 慣例未涵蓋的 **sub-conversation lifecycle** 缺口。

**定義：**

- **主對話（main conversation）：** 持有 skill stage 狀態、負責推進 SKILL.md 各階段、執行寫檔的對話。
- **副對話（sub-conversation / parallel-chat）：** 為消化大量 raw material（既有劇本 / docx / .txt / .csv / .json / 長人設）而另開的對話；只做讀取與萃取，把 evidence 回報主對話，不持有 skill 狀態、不寫檔。
- 此分工典型用於 `/create-character` 既有劇本萃取（F11/F13 ingestion 機制；見 NEW_REQ_35/37）、`/create-world` 大量世界觀筆記消化等 input-heavy 場景。

**副對話 lifecycle 8 條規則（D-072 落地；本段為權威）：**

| # | 規則 | 說明 |
|---|---|---|
| 1 | **只讀不寫** | 副對話只讀 source material（含 `_source_materials/` / 既有 08_dialogue_outputs/ / user 貼入素材）；**一切寫檔（entity 檔 / phase_log / view/）只能由主對話經 SKILL.md 階段執行**。副對話不得寫任何 Instance 檔。 |
| 2 | **明列讀過的檔** | 副對話回報時必須逐一列出**實際讀過**的檔案路徑 / 素材名（含 docx / txt / csv / json）；不得只說「已讀完素材」。 |
| 3 | **明列未讀範圍與限制** | 副對話必須明示**沒讀到 / 讀不全**的部分（環境不支援 docx → fallback warning；檔案過長只抽樣；某格式無法解析）；讓主對話知道 evidence 覆蓋邊界，不得隱性截斷當作全讀。 |
| 4 | **只回 evidence summary** | 副對話回主對話的是**萃取後的 evidence 摘要 / 聲線規律 / 引用片段**，不是把 raw material 整段貼回主對話（保護主對話 context budget；對齊 F14 / NEW_REQ_38 瘦身紀律）。需要原文佐證時給定位（檔名 + 段落 / 行）。 |
| 5 | **主對話負責 skill stage 推進** | skill 的 5 階段狀態機由主對話持有並推進；副對話**不得**自行宣告階段完成、不得代主對話寫檔或拍板。副對話只供料，stage gate 仍在主對話。 |
| 6 | **不關閉副對話除非 user 明示** | 主 agent **不得**在 ingestion 任務未明確結束前主動關閉 / 拋棄副對話；只有 user 明示「副對話可收了」才結束。預設保持副對話 open 以便追讀補問。**（本條為 F10 核心痛點。）** |
| 7 | **reuse 同一副對話** | 同一 ingestion 任務內需要多輪追讀時，**reuse 既有副對話**（保留其已讀 context），不要每次另開新副對話重讀，避免重複 token 與 context 漂移。 |
| 8 | **主對話 wording 範例** | 主對話委派 / 維持副對話時，用明確 wording 標示分工與生命週期（範例見下），降低「太早關閉」「副對話越權寫檔」風險。 |

**主對話 wording 範例（規則 8 落地；供 main agent copy-adapt）：**

```text
[委派副對話讀取]
我在主對話保留 /create-character 階段推進。請在副對話只讀以下既有素材並萃取聲線 evidence（不要寫任何檔）：
- 讀：_source_materials/莉娜_既有劇本.docx、08_dialogue_outputs/ 內莉娜相關台詞
- 回報：(a) 實際讀過的檔清單 (b) 讀不到/讀不全的部分 (c) 聲線規律 evidence 摘要（給檔名+段落定位，不要整段貼回）
副對話請保持開啟，我可能會追問；未經我明示請勿結束。

[追讀]
沿用同一副對話（不要另開），補讀莉娜在危機場景的台詞，回報增量 evidence。

[結束]
ingestion 完成，副對話可以收了。
```

**3 個 root 檔的同步責任（對齊 §3.3.0 維護模式 + F14 瘦身紀律）：**

- 本段（ARCH §3.3.3）為**權威**；`AGENTS.md` / `CLAUDE.md` / `_user_manual/skill_invocation_guide.md` 僅加**短指標**（8 條規則精簡列 + 指回本段），不複製全文，避免 root context budget 再膨脹。
- 新增 ingestion 類 skill 流程時，沿用本段副對話分工，不另立第二套 lifecycle。

**Cross-ref：** DECISIONS_LOG §6.21 D-072 / POST_LOCK_PENDING NEW_REQ_34（RESOLVED via D-072）/ NEW_REQ_35 + NEW_REQ_37（F11/F13 — 副對話是其 ingestion 機制）/ NEW_REQ_38（F14 同 Meta-pattern D — Agent context / UX layer；本段第 4 條對齊其瘦身紀律）/ §3.3.0（multi-agent invocation 慣例；本段為其 sub-conversation lifecycle 擴充）/ M4_USER_TEST_REPORT §3.10。

## 3.4 各 skill 對應的協議

| Skill | 對應協議 |
|---|---|
| `/init-project` | `00_protocol/00_i_專案初始化協議.md` |
| `/create-world` | `00_protocol/00_e_世界觀創建協議.md` |
| `/create-character` | `00_protocol/00_f_角色創建協議.md` |
| `/create-relationship` | `00_protocol/00_l_關係創建協議.md`（C-7 新增） |
| `/create-outline` | `00_protocol/00_g_大綱創建協議.md` |
| `/create-detailed-outline` | `00_protocol/00_h_細綱創建協議.md` |
| `/create-org` | `00_protocol/00_n_組織創建協議.md`（F8 Phase 3；D-074 新增） |
| `/iterate-*` (6 個：W、C、R、P、CH、ORG) | `00_protocol/00_j_迭代協議.md`（ORG 加 00_n context；D-074） |
| `/view-*` (4 個) | 無協議，純技術功能 |
| `/export-*` (4 個) | 無協議，純技術功能 |
| `/diagnose` | `00_protocol/00_a` 中的「診斷模式」 |
| `/integrate` | `00_protocol/00_a` 中的「整理模式」 |
| `/scene-task` | `00_protocol/00_k` 階段 1 + `07_scene_tasks/07_a` |
| `/dialogue-write` | `00_protocol/00_k` 階段 2 + `00_a` + `08_dialogue_outputs/08_*` |
| `/qa` | `00_protocol/00_k` 階段 3 + `00_b` + `09_quality_assurance/09_*` |
| `/status` | 無協議，純技術功能 |
| `/check-gaps` | 無協議，純技術功能 |

---

# 4. 視圖層實作

## 4.1 `/view-*` 動態組合

`/view-world` 的執行邏輯（伪碼）：

```
1. 讀取 01_world/01_a, 01_world/01_b, 01_world/01_c
2. 讀取 02_vocabulary/02_a, 02_b, 02_c
3. 把所有內容組合成單一 Markdown 結構：
   - "# 世界觀"
   - "## 規則" → 01_a 內容
   - "## 世界語言" → 01_b 內容
   - "## 陣營與階級語言" → 01_c 內容
   - "## 詞彙系統"
     - "### 專有名詞" → 02_a
     - "### 俗稱與黑話" → 02_b
     - "### 禁用詞與慎用詞" → 02_c
4. 在 chat 中以 Markdown 印出
5. 不寫入任何檔案
```

`/view-character <name>` 的執行邏輯：

```
1. 讀取 03_characters/main/<name>_*.md 或 minor/<name>_*.md（依存在的位置）
2. 從 04_relationships/04_a 中抽出該角色相關段落
3. 從 04_relationships/04_b 中抽出該角色出現的時間線
4. 從 05_plot/05_c 中抽出該角色弧線
5. 組合成單一 Markdown 結構：
   - "# 角色：<name>"
   - "## 聲線卡" → 角色卡內容
   - "## 關係" → 關係矩陣相關段落
   - "## 時間線" → 關係變化時間線相關段落
   - "## 弧線" → 角色弧線
6. 印出
```

**抽取段落的依據：** 透過 entities `C-<name>` 或 `R-<name>-*`、`R-*-<name>` 在 frontmatter 中的對應，或透過文件內 `## <角色名>` 等 anchor。CODEX 在 Phase C 決定具體實作。

**呈現規則（時期 C 整合 UX_SPEC §7）：**

- 跨檔連結基準：project root（`/` 開頭），例如 `[主角A](/03_characters/main/主角A_聲線卡.md)`；同檔內 anchor 跳轉用 `#anchor-slug` 不加 `/`
- Source 引用格式：每段內容結束時加 italic 一行 `*來源：[/path/to/source.md](/path/to/source.md)*`；多源逗號分隔
- 單向 reference：A 引用 B 時 A 內寫連結，B 不必反向列；例外：`/view-character` 末尾的「出場場景」由 frontmatter `entities` 反查動態生成（不維護反向欄位）
- chat 動態組合也加 source 引用（即使連結點不到，純文字仍提供定位線索）

## 4.2 `/export-*` 靜態整合檔

`/export-world` 與 `/view-world` 邏輯相同，但結果寫入 `view/世界觀.md` 而非印在 chat。

寫入時的 frontmatter：

```markdown
狀態：DERIVED
版本：對應 source 的最高版本
最後更新：[執行時的日期]
適用範圍：世界觀整合視圖
優先級：中
生成方式：/export-world  
組合來源：
  - 01_world/01_a_世界觀總覽.md
  - 01_world/01_b_世界語言規格.md
  - 01_world/01_c_陣營與階級語言.md
  - 02_vocabulary/02_a_專有名詞表.md
  - 02_vocabulary/02_b_俗稱與黑話表.md
  - 02_vocabulary/02_c_禁用詞與慎用詞表.md
```

`DERIVED` 是新狀態（非標準狀態機之一），標示「衍生檔，不可直接修改」。修改要修 source 後重新 `/export-*`。

**`check_headers.py` 需要把 `DERIVED` 加入 `VALID_STATUS`**（Phase C 同步更新）。

**呈現規則（時期 C 整合 UX_SPEC §7）：**

- Breadcrumb：每份 `/export-*` 整合檔在 frontmatter 之後、第一個 `#` 標題之前加一行 breadcrumb（例：`> 專案首頁 / 世界觀 / 完整視圖`）；不加箭頭符號、不加日期、不加狀態 badge。`/view-*` chat 動態組合**不加** breadcrumb
- 整合檔末尾加返回連結：`[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)`（`/view/README.md` 在 `/export-*` 累積 ≥1 份後**由使用者手動建立**，不自動生成 — DECISIONS_LOG P-004 暫定）
- TOC 觸發條件：整合檔預估 > 200 行時，在 frontmatter 與 breadcrumb 之後、第一個 `#` 標題之前插入「## 目錄 / Contents」TOC
- Anchor slug：依 GitHub Flavored Markdown 自動規則，不手動寫 `{#anchor}`；slug 與標題一致性由 `/export-*` skill **內部驗證**（DECISIONS_LOG P-005 暫定 — 不擴大 `check_headers.py` global linter scope）
- 跨檔連結基準與 source 引用：同 §4.1 規則

## 4.2a Layer 3 Export — A1 prompt 生成器（v1.2 新增 via D-024 + D-038 + D-039）

> **v1.2 新增章節 via D-024（套版機制縮減為 JSON+MD 雙吐）+ D-038（A1 prompt 流程）+ D-039（DF `manifest + records[]` 為權威）+ CODEX C-03 / C-04 解決**  
> **適用範圍：** 描述 Layer 3 Export 的實作架構（前端 panel 內嵌 prompt 生成器，無 server CLI）；不擴 §4.2 既有 4 個 `/export-*`

### 4.2a.1 設計原則

依 D-029 α + D-038 細化：

- 前端 web server **不**啟動 subprocess / 不 spawn child process / 不執行任何 export 邏輯
- Layer 3 Export 「執行」全在外部 agent（CC / CODEX APP / 本地 LLM endpoint）process 中發生
- 前端 server.py 的職責只到「**組裝 prompt → 複製 / POST**」為止

### 4.2a.2 Prompt 生成器組成（前端內嵌）

| 元件 | 位置 | 職責 |
|---|---|---|
| `ExportPromptPanel`（UI） | UX §11.6.11 | 範圍 / 格式 / 路徑 / 推送方式選擇 UI |
| `promptAssembler.js`（前端 JS） | `_tools/frontend/static/promptAssembler.js`（建議路徑） | 依使用者選項組裝 prompt 5 區塊（標題 + YAML 元資料 + 步驟 + 約束 + 完成回報），對齊 `_design/L3_EXPORT_PROMPT_SCHEMA.md` §1 |
| `clipboardWriter`（前端 JS） | 同上 | `navigator.clipboard.writeText(prompt)` |
| `endpointPoster`（前端 JS）| 同上 | `fetch(POST, url, { body: { prompt, format: 'json' } })`；30 秒超時 |
| **server.py 不負責 export** | `_tools/frontend/server.py` | 僅提供 `GET /api/scope-counts?scope=...` 等「組 prompt 需要的元資料」endpoint（讓 prompt 中 stats 區塊填具體數字）|

### 4.2a.3 Push mode 三選項（沿 L3_EXPORT_PROMPT_SCHEMA §4 lifecycle）

| Push mode | 實作機制 | Phase |
|---|---|---|
| `clipboard`（預設） | `navigator.clipboard.writeText()` | Phase A.0 必做 |
| `local_llm_endpoint` | `fetch(POST, user-set-URL)` + Bearer Auth + model param | Phase B 後必做（D-038 附帶第 2 項）|
| `claude_api` / `openai_api` | 同上但對應 API endpoint + retry | Phase C+ 選做（disabled in panel）|

### 4.2a.4 與 §4.2 既有 4 個 `/export-*` 的區分

| 維度 | §4.2 既有 4 個 `/export-*` skill | §4.2a Layer 3 Export A1 prompt |
|---|---|---|
| 實作位置 | `.claude/skills/<name>/skill.md` + Python script | 前端 panel 內嵌 prompt 生成器（無 skill） |
| 輸出位置 | `view/<topic>.md` | `export/<instance>_<timestamp>.{json,md}` |
| 觸發 | Claude skill | 前端按鈕產 prompt → user 貼 → agent 跑 |
| 是否新增 skill | 否（既有 4 個維持） | **否**（不新增；prompt schema 取代 skill 定義）|

兩條 export 路徑共存，互不取代（對齊 SPEC §13a + Contract A.7）。

## 4.3 跨檔導航統一規則（時期 C 整合 UX_SPEC §7 全節）

下列規則為所有 view 系列（`/view-*` 與 `/export-*`）與 status 看板共用，集中放於此節避免分散：

| 規則 | 內容 | 來源 |
|---|---|---|
| 連結基準 | project root，所有跨檔 link 以 `/` 開頭（例：`/01_world/01_a_世界觀總覽.md`） | UX §7.1 |
| 同檔 anchor | 用 `#anchor-slug`，不加 `/` | UX §7.1 |
| Breadcrumb | 僅 `/export-*` 整合檔加；`/view-*` chat 不加；格式 `> 專案首頁 / 世界觀 / 完整視圖`；不加箭頭、日期、badge | UX §7.2 |
| 整合檔末尾返回連結 | `[← 回 /view-* 系列總覽](/view/README.md) ｜ [回專案首頁](/README.md)` | UX §7.2 |
| `/view/README.md` 生成方式 | 使用者手動建立（非自動）— DECISIONS_LOG P-004 暫定 | DECISIONS_LOG P-004 |
| TOC 觸發 | 整合檔 > 200 行時插入「## 目錄 / Contents」TOC；位置：frontmatter + breadcrumb 之後、第一個 `#` 之前 | UX §7.3 |
| Slug 規則 | 依 GFM 自動，不手寫 `{#anchor}`；中文主＋英文 sub `世界規則 / World Rules` → slug `世界規則-world-rules`；slug 一致性由 `/export-*` skill 內驗證 — DECISIONS_LOG P-005 | UX §7.3, P-005 |
| Source 引用格式 | 每段結尾 italic 一行 `*來源：[/path](/path)*`；多源逗號分隔；chat 與檔案皆加 | UX §7.4 |
| 單向 reference | A 引用 B 時 A 內寫；B 不反向列；例外：`/view-character` 末段「出場場景」由 `entities` 反查動態生成 | UX §7.5 |
| view 失效偵測 | source 變動但 view 未重 export 時，由 `/check-gaps` 偵測並印警告（文案沿用 UX §7.7）— DECISIONS_LOG P-003 暫定 | UX §7.7, P-003 |

## 4.4 創建階段的自動拆分

`/create-world` 階段 4 執行邏輯：

```
1. 取階段 3 收斂後的整合內容（使用者已拍板）
2. 依協議專屬區段的「拆分規則」判斷每段落歸屬：
   - 世界規則／科技／生活水準／價值觀／宗教 → 01_a
   - 語言層級 → 01_b
   - 陣營與階級語言 → 01_c
   - 詞彙 → 02_a/b/c
   - 類型語氣 → 作品專屬 00_b 骨架
3. 對每個目標檔案：
   a. 讀取既有檔案
   b. 把整合內容中對應段落寫入既有檔案的對應區段
   c. 更新 frontmatter（status 升 DRAFT、updated 日期、entities 標記）
4. 報告：列出修改的檔案、每個檔案新增了什麼
```

---

# 5. 影響範圍評估實作（C-9 裁決：選 C depends_on frontmatter）

通用迭代協議的核心：使用者改某實體 → AI 反查所有受影響檔案。

**反查邏輯（依 SPEC 5.2 鎖定的 frontmatter schema）：**

- **直接受影響**：`entities` 包含 modified_entity 的檔案（這些檔案「貢獻給」該實體）
- **依賴受影響**：`depends_on` 包含 modified_entity 的檔案（這些檔案「依賴於」該實體）
- **間接受影響**（可選）：直接受影響檔案的 entities 所對應的次級實體被影響

實作（給 `00_j` 階段 2 與所有 `/iterate-*` 用）：

```python
def find_affected_files(modified_entity, all_files):
    direct = []      # entities 含 modified_entity
    depends = []     # depends_on 含 modified_entity
    indirect = []    # 直接受影響檔案的次級實體被影響

    # 直接受影響：「貢獻」關係
    for f in all_files:
        if modified_entity in f.entities:
            direct.append(f)

    # 依賴受影響：「依賴」關係（C-9 新增）
    for f in all_files:
        if modified_entity in f.depends_on:
            depends.append(f)

    # 間接受影響：直接受影響檔案的其他 entities 對應的檔案
    secondary_entities = set()
    for f in direct:
        for e in f.entities:
            if e != modified_entity:
                secondary_entities.add(e)

    for f in all_files:
        if f in direct or f in depends:
            continue
        if any(e in f.entities for e in secondary_entities):
            indirect.append(f)

    return {
        "direct": direct,
        "depends": depends,
        "indirect": indirect,
    }
```

**注意：**
- `depends_on` 是檔案自己宣告的「我依賴 X」，比起反查 entities 的次級關係更明確
- 兩條反查路徑互補：`entities` 反查抓「定義該實體的檔案」，`depends_on` 反查抓「使用該實體的檔案」
- 初版 `depends_on` 可能不完整（許多檔案還沒標），這時要靠 indirect 兜底；使用者使用過程中逐步補完 `depends_on`

呼叫範例：

```text
使用者：/iterate-world 我要在世界觀加入「宗教階級」一項

AI：好。先做影響範圍評估：

直接受影響（entities 含 W-rules）：
- 01_world/01_a_世界觀總覽.md（將新增宗教階級段落）

依賴受影響（depends_on 含 W-rules）：
- 01_world/01_b_世界語言規格.md（內容依賴世界規則）
- 01_world/01_c_陣營與階級語言.md（內容依賴世界規則）
- 02_vocabulary/02_a_專有名詞表.md（內容依賴世界規則）
- 03_characters/main/主角A_聲線卡.md（角色用詞依賴世界規則）

間接受影響（次級實體的對應檔案，由 entities 反查補漏）：
- 04_relationships/04_a_角色關係矩陣.md（含主角的關係段落）

請選擇本輪要處理的範圍：
1. 只改 01_a
2. 改 01_a + 依賴受影響全部
3. 改 01_a + 依賴受影響 + 間接受影響
4. 全部都改

請順帶確認：以上「依賴受影響」清單看起來是否完整？
若有遺漏，請補上對應檔案的 frontmatter depends_on，下次反查就會抓到。
```

---

# 6. 下游 skill 實作（`/scene-task`、`/dialogue-write`、`/qa`）

下游三個 skill 是台詞生產 pipeline 的核心，共同被 `00_k 台詞生產流程協議` 規範。每個 skill 內部沿用「共通骨架 5 階段」（診斷 → 探索 → 收斂 → 執行 → 驗證），但內容對應到下游語境。

## 6.1 `/scene-task` 實作

**輸入：** 場景 ID（CH<n> S<m>），例如 `CH01 S03`

**5 階段：**

1. **診斷階段** — 讀 06_a 場景索引找到該場戲，確認場景存在且至少 DRAFT；檢查所有先決實體（W、V、C、R、P、CH）是否至少 REVIEW；列出缺漏。

2. **探索階段** — 從各實體抽取本場必要資訊：
   - W：本場需要的世界規則／語言層級／陣營階級語言
   - V：本場禁用詞與允許用的俗稱黑話
   - C：本場出場角色的聲線卡引用
   - R：本場相關角色對之間的關係狀態
   - 05_d 資訊揭露表：本場必須透露／禁止透露
   - 05_e 伏筆：本場潛伏的伏筆或回收

3. **收斂階段** — 把抽取的資料整合成單場任務包草稿；列出缺漏（標 TODO）；問使用者要補哪些資訊。

4. **執行階段** — 寫入 `07_scene_tasks/CH<n>_S<m>_台詞任務包.md`，依 07_a 模板；frontmatter 完整含下游欄位（M7/M10 對齊 SPEC 5.2）：
   ```yaml
   狀態：DRAFT
   ---
   entities: [S-<n>-<m>]
   depends_on: [W-rules, V, <相關 C-*>, <相關 R-*-*>, P, CH-<n>]
   weight: {S-<n>-<m>: 1.0}
   scene_id: S-<n>-<m>
   source_task: null         # 任務包本身就是源頭，此欄為 null
   source_dialogue: null
   pipeline_state: TASK_DRAFT
   mode_tag: null
   qa_decision: null
   ```

5. **驗證階段** — 自動 `/status`，確認 S-<n>-<m> 出現在實體清單中；append phase_log 一筆（含 scene_id、task_path）；建議下一步「人類審任務包」。

**輸出檔案：** 一份任務包 `.md`

**禁止：**
- 不得擅自補完本場必須透露／禁止透露的資訊
- 不得擅自修改其他場景的任務包
- 不得擅自把任務包狀態升 REVIEW（必須人類審）

## 6.2 `/dialogue-write` 實作

**輸入：** 任務包路徑（例 `07_scene_tasks/CH01_S03_台詞任務包.md`）

**5 階段：**

1. **診斷階段** — 確認任務包至少 REVIEW；列出任務包中標 TODO 的欄位（缺漏項）；若 TODO 太多則拒絕生成。

2. **探索階段（可選）** — 若使用者明說「跑探索」，先產短篇探索片段（語氣方向實驗），不寫入正式版本。

3. **試寫階段（主流程）** — 依任務包資訊與 00_a 試寫模式規範，產 3 版本（v01A/B/C）：
   - v01A：克制、短句、強潛台詞
   - v01B：攻防更強、衝突更尖
   - v01C：情緒更重、但避免直說

4. **破格階段（可選）** — 若使用者明說「跑破格」，產 v01D 破格版（沿用 00_a 破格模式規範）；標明 `Mode Tag: EXPERIMENTAL`。

5. **收斂階段（可選）** — 若使用者明說「直接收斂」，跳過試寫直接整合（適用於人類已有明確方向時）。

**執行階段** — 寫入 `08_dialogue_outputs/CH<n>_S<m>_<簡稱>_dialogue_v01A.md` 等檔案；依 08_b 模板；frontmatter 完整含下游欄位（M7/M10 對齊 SPEC 5.2）：
```yaml
狀態：DRAFT
---
entities: [S-<n>-<m>]
depends_on: [<本場相關 C-*>, <相關 R-*-*>]
weight: {S-<n>-<m>: 1.0}
scene_id: S-<n>-<m>
source_task: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
source_dialogue: null         # 試寫版自己就是源頭；--converge 產 v02 時填上 v01 路徑
pipeline_state: DIALOGUE_TRIAL # 或收斂時 DIALOGUE_CONVERGED
mode_tag: DRAFT_TRIAL          # 或 EXPERIMENTAL / CONVERGENCE
qa_decision: null
```

**驗證階段** — 自動 `/status`；append phase_log 一筆（含 scene_id、dialogue_paths 清單、mode_tag）；建議下一步「人類挑亮點 + 收斂」或「跑 /qa」。

**輸出檔案：** 3–5 份多版本台詞 `.md`

**禁止：**
- 不得擅自把試寫版直接標 FINAL
- 不得把破格版混入正式 v0X 中（必須清楚標記 EXPERIMENTAL）
- 不得擅自修改任務包

## 6.3 `/qa` 實作

**輸入：** 台詞檔路徑（例 `08_dialogue_outputs/CH01_S03_xxx_dialogue_v01A.md`）

**5 階段：**

1. **診斷階段** — 確認台詞檔至少 DRAFT；對照任務包讀取本場規格。

2. **執行階段（不需要探索／收斂）** — 依**八份** QA 模板分別跑檢查（v1.2 partial supersede via D-043 — 從 5 份擴為 8 份）：
   - 09_a AI 味檢查（AI_FLAVOR）
   - 09_b 角色聲線一致性檢查（VOICE_CONSISTENCY）
   - 09_c 禁用詞檢查（FORBIDDEN_WORD）
   - 09_d 資訊控制檢查（INFO_CONTROL）
   - 09_f 類型偏移檢查（GENRE_DRIFT）
   - **09_g 節奏感檢查（RHYTHM）** — v1.2 新（D-026 + D-043）
   - **09_h 對話張力檢查（DRAMATIC_TENSION）** — v1.2 新（D-026 + D-043）
   - **09_i 跨場一致性檢查（CROSS_SCENE_CONTINUITY）** — v1.2 新（D-026 + D-043）

   **並行檢查、序列印出順序（UD §2.5.3）：** 09_f → 09_d → 09_h → 09_b → 09_g → 09_a → 09_c → 09_i

3. **彙整階段** — 統合**八份**報告中的最高優先問題；標示 QA_PASS 或 QA_FAIL（v1.2：8 份全 PASS 才 PASS，任一 FAIL 即 FAIL）。

4. **寫檔階段** — 在 `09_quality_assurance/` 下寫入 **8 份**報告（v1.2 / D-043；原 5 份 supersede），命名 `<台詞檔基本名>_<QA 類型>_報告.md`。每份報告的 frontmatter 完整含下游欄位（M7/M10 對齊 SPEC 5.2）：
   ```yaml
   狀態：DRAFT
   ---
   entities: [S-<n>-<m>]
   depends_on: [<台詞檔對應的 C-*、R-*-*>]
   weight: {S-<n>-<m>: 0.125}   # 8 份報告各 0.125，加總 1.0（v1.2 / D-043；原 5 份 × 0.2 supersede）
   scene_id: S-<n>-<m>
   source_task: 07_scene_tasks/CH<n>_S<m>_台詞任務包.md
   source_dialogue: 08_dialogue_outputs/CH<n>_S<m>_..._dialogue_vXX.md
   pipeline_state: QA_PASSED    # 或 QA_FAILED
   mode_tag: null
   qa_decision: PASS            # 或 FAIL（v1.2：8 份全 PASS 才 PASS）
   qa_type: AI_FLAVOR           # 8 種之一（v1.2 / D-043；原 5 種 + RHYTHM / DRAMATIC_TENSION / CROSS_SCENE_CONTINUITY）
   ```
   同步更新台詞檔的 frontmatter（只動 pipeline_state + qa_decision，不動內容）。

5. **驗證階段** — 自動 `/status`；append phase_log 一筆（含 scene_id、target_dialogue、**qa_report_paths 8 個**（v1.2 / D-043；原 5 個 supersede）、qa_decision）；列出 QA 結論與下一步建議。

**輸出檔案：** **8 份** QA 報告 `.md`（v1.2 / D-043）

**禁止：**
- 不得直接修改台詞檔
- 不得擅自決定 QA_PASS 進而升級台詞檔狀態（QA_PASS 只是 mode tag，FINAL 必須人類確認）
- 不得擅自刪除人類已標記「保留」的句子

## 6.4 三個 skill 的資料流

```text
場景索引 06_a       任務包 07_a 模板        台詞 08_b 模板       QA 09_a-i 模板（v1.2 / D-043；原 09_a-f supersede — 含 09_g/h/i 共 8 份）
     ↓                   ↓                    ↓                    ↓
  /scene-task   →     任務包 .md      →   /dialogue-write  →   多版本台詞 .md   →   /qa   →   **8 份** QA 報告（v1.2 / D-043）
                          ↑                                              ↑
                      W/V/C/R/                                   00_a 規則
                      05_d 揭露
                      05_e 伏筆
```

## 6.5 與上游 skill 的差異

| 維度 | 上游 (`/create-*`) | 下游 (`/scene-task`、`/dialogue-write`、`/qa`) |
|---|---|---|
| 觸發場景 | 一次性建設定 | 日常多次重複 |
| 對話深度 | 場景化長對話 | 較短，依任務包直接執行 |
| 多版本 | 通常單一輸出 | 預設 3 版本（試寫） |
| QA 銜接 | 不需要 QA | 必須跑 **8 份** QA（v1.2 / D-043；原 5 份 supersede — 09_a/b/c/d/f/g/h/i）|
| 狀態流轉 | DRAFT → REVIEW → LOCKED | DRAFT → ALT/EXPERIMENTAL → REVIEW → QA_PASS → FINAL → LOCKED |

## 6.6 共用元件

三個下游 skill 共用以下基礎元件（建議 CODEX 把共用邏輯抽出成 helper）：

- **實體掃描**：找出本場相關實體與檔案
- **資訊抽取**：從多份檔案中抽取本場必要段落
- **狀態驗證**：檢查實體狀態是否滿足啟動條件
- **任務包讀取與解析**：解析 07_a 格式
- **`/status` 呼叫**：階段 5 自動驗證

## 6.7 五份上游協議與下游 skill 共通階段執行規則（時期 C 整合 UPSTREAM_DOWNSTREAM_SPEC §1.0）

UPSTREAM_DOWNSTREAM_SPEC 第一輪交付的「共通骨架執行細則」（§1.0.1–§1.0.3）為所有上游 `/create-*` 與下游 `/scene-task` `/dialogue-write` `/qa` 共用的「5 階段執行通則」基礎。本節整合上述內容，作為 CODEX 實作 skill SKILL.md「## 流程」段落的權威骨架。

**範圍：** 適用於遵循「共通骨架 10 區段」的所有 skill — 即 `/create-world` `/create-character` `/create-relationship` `/create-outline` `/create-detailed-outline` `/scene-task` `/dialogue-write` `/qa` 以及未來的 `/iterate-*`。

### 6.7.1 區段 1–9 共通執行細則摘要

來源：UPSTREAM_DOWNSTREAM_SPEC §1.0.1。完整內容見該檔，本節僅摘要 CODEX 實作要點。

| 區段 | 共通執行要點 |
|---|---|
| §1 文件目的與適用範圍 | 固定句型：「本協議規範 `/<skill>` 在「<實體類型>」實體創建過程中的執行流程」 |
| §2 啟動條件 | 驗證：(a) 先決實體狀態（各協議專屬），(b) Instance 已 bootstrap（`.protocol_version` 存在），(c) 沒有針對相同實體的進行中協議。任一失敗即拒絕啟動並引導使用者補齊 |
| §3 階段 1 診斷模式 | 開場固定：(a) 印先決資料清單摘要，(b) 邀請使用者貼長段假設，(c) 用 00_a §3.3 診斷模式產出診斷報告六固定段（**不寫檔**），(d) 結尾印「階段 2 提問清單預告」等使用者確認 |
| §4 階段 2 探索 / 補洞 | 場景化對話式（SPEC Q10=B）：每次最多丟 3 題，按優先序；每題附「為什麼問」「答完影響哪檔」；使用者可說「跳這題」「先跳到 X」；每完成一題印「議題進度條」；偵測衝突即先丟出討論 |
| §5 階段 3 收斂模式 | 整合成「收斂預告稿」5 必含欄位：(1) 每議題最終結論一句話、(2) 拆分計畫（含完整路徑）、(3) 衝突點清單、(4) TODO 清單、(5) 影響範圍預告。等使用者明確「通過」/「OK」/「寫檔」才進階段 4 |
| §6 階段 4 Codex 執行 | 固定順序：(1) 計算目標路徑、(2) 對每檔讀現有 / 新建 / 找 anchor 寫入、(3) frontmatter 補完 SPEC §5.2 規範、(4) 00_b 寫入依 SPEC §17 規則、(5) `.protocol_version.phase_log` append。寫檔順序：主分拆檔 → 衍生分拆檔 → 00_b。任一步出錯 rollback 並印錯訊息、不更新 phase_log |
| §7 階段 5 實體驗證 | 自動 `/status`：(1) 列本次新建 / 更新實體 ID + 完成度、(2) 列寫入檔案清單、(3) expected entity manifest 對照、(4) 後續建議下一步 skill。**不可自動跑下一個 skill** |
| §8 禁止事項 | 6 條共通禁止：不擅自升狀態 / 不擅自跳階段 / 不擅自補關鍵設定（標 TODO 停） / 不動 LOCKED / 不呼叫其他 `/create-*` / 不擅自新增實體類型 或 enum 值 |
| §9 缺漏處理 | TODO / INFERENCE / CONFLICT 三類標記法（見 SPEC §9 與 UPSTREAM §1.0.1 §9）。CONFLICT > 0 時不得自動進階段 4 |

### 6.7.2 使用者觸發語字典（共通）

來源：UPSTREAM_DOWNSTREAM_SPEC §1.0.2。所有上游與下游 skill 必須穩定識別下列觸發語：

| 觸發語 | 行為 |
|---|---|
| `跳到階段 X` / `跳階段` | agent 印當前已確認資料快照、請使用者確認 → 跳到階段 X |
| `跳這題` / `跳這個議題` | 當前議題標 TODO 並進下一題 |
| `先跳到議題 X` | 當前議題標 TODO 並跳到議題 X |
| `通過` / `OK` / `寫檔` | 從階段 3 進階段 4（僅在階段 3 有效） |
| `中止` / `取消` | 不寫檔離開協議；`.protocol_version.phase_log` 補 `status: aborted` |
| `重來` / `從頭來` | 棄置目前累積的所有議題答案，從階段 1 重啟（保留診斷報告） |
| `這部分先不要動` | 該議題對應的分拆檔在階段 4 跳過寫入 |
| `直接寫檔` | 從階段 1 / 2 直接跳階段 4（僅允許在迭代且無 CONFLICT 時用） |

UX 呈現規則：各 skill 在每階段開頭印「本階段可用觸發語」提示行；具體格式由 UX specialist 第二輪在 UX_SPEC §2/§4/§5 確認（v1 待補）。

### 6.7.3 先決資料缺失處理流程（共通）

來源：UPSTREAM_DOWNSTREAM_SPEC §1.0.3。當區段 2 啟動條件不通過：

1. 印缺漏清單（哪些實體缺、缺到什麼程度）
2. 對每個缺漏實體建議對應 skill
3. 提供三選項：
   - **跑那個 skill**（agent 不自動跑，使用者主動觸發）
   - **先跳過先決條件**（僅在使用者明確聲明可接受 TODO 等補時用；`.protocol_version.phase_log` 標 `prereq_waived: true` 與原因）
   - **取消**（不啟動本協議）

**禁止：** agent 在 `prereq_waived: true` 情況下不得把實體狀態升 REVIEW 或以上。

### 6.7.4 UPSTREAM §1–§6 substantive 內容已交付（v0.3 修正）

**v0.2 初版誤判 UPSTREAM 「Batch 補完」未交；v0.3 修正：** UPSTREAM_DOWNSTREAM_SPEC.md 已 ≈90% 完成（3503 行，§0–§8 完整），含：

- §1.1–§1.5：五份上游協議（00_e / 00_f / 00_g / 00_h / 00_l）完整 agent 提問腳本、寫檔規則、拆分 algorithm（11 + 9 + 7 + 7 + 6 = 40 個議題）
- §2：下游 00_k 完整內容（10 區段全展開）
- §3：6 份 QA 模板內容（含 09_e M9 對齊修正）
- §4：`/dialogue-write` 三模式 algorithm（試寫 / 破格 / 收斂）
- §5：Canon delta 框架（成熟期功能；Phase D 不實作 skill）
- §6：多場景並行處理（race condition 規範與 file-level mutex 機制）
- §7：53 個 [UX] 標記（UX-1 ~ UX-53）
- §8：8 議題資料格式依賴

CODEX 在 Phase A.3 / B.0 / B.1 / B.2 / B.3 / D.0 / D.1 / D.3 / D.4 等任務啟動時，**以 UPSTREAM 對應節為權威來源**寫對應協議檔 / skill 實作。

### 6.7.5 多場景並行處理（P-015 暫定，原 D-017）

完整機制依 `UPSTREAM_DOWNSTREAM_SPEC.md` §6.1–§6.9。本節摘要 CODEX 實作要點：

**並行容忍度（依 UPSTREAM §6.1 表）：**

| 操作 | 容忍度 |
|---|---|
| 對「不同場景」的 `/scene-task` / `/dialogue-write` / `/qa` | 完全並行可 |
| 對「同一場景」的 `/scene-task` / `/dialogue-write` / `/qa` | **禁止** |
| 同一場景 `/scene-task` + `/dialogue-write` 同時 | **禁止** — pipeline_state 競爭 |
| `/iterate-*` 與下游 skill 同時 | **禁止** — 上游實體變動，下游檢查失效 |

**phase_log 寫入鎖：**

- 主機制：`flock`（Linux）/ OS 對應機制（Windows）；鎖檔 `.protocol_version.lock`；排他鎖；30 秒 timeout
- Fallback：sentinel file 模式（適用 OS 不支援 flock）
- 取得鎖才能 append phase_log entry；釋放後即刻

**場景狀態升級鎖：**

- 對每個場景 ID，agent 升 `pipeline_state` 前先比對「預期狀態 vs 實際狀態」；不一致即 abort
- 寫檔用「讀整檔 → 修改 frontmatter → 寫整檔」atomic + `<file>.tmp` + OS-level rename pattern
- 加上 `<file>.lock` 排他鎖；30 秒 timeout

**跨場景並行的依賴檢查：**

- `/iterate-*` 啟動時掃 phase_log 中 `status: in_progress` 的下游 skill；若有引用將迭代的實體 → 拒絕並列出
- 使用者選：等下游 / 中止下游 / 強制（強制時下游可能升狀態失敗）

**並行衝突 abort 紀錄：** 依 SPEC §5.4 phase_log 範例的 abort entry 格式（含 `status: aborted` + `abort_reason` + `detail`）。**`status` 欄位本身屬 P-012 暫定（原 D-014），第二輪資料格式 specialist 在 DATA_FORMAT_SPEC §6 正式確認後 promote 為 D-NNN。**

---

# 7. Git Workflow

## 6.1 Commit 節奏

**建議規則：**
- 每完成一個 phase 子任務 commit 一次
- 一個 commit 對應一組相關檔案，避免「一次 commit 整個 phase」
- Commit message 用既有風格（簡潔英文，例如 `add phase A bootstrap protocol`）

## 6.2 Branch 策略（多 Instance 升級用）

**Template repo：**
- `main` 為穩定版
- 大改動先開 feature branch

**Instance repo：**
- 從 Template 用 `Use this template` 一次性 clone
- Instance 之後完全獨立，不再追蹤 Template
- 若使用者想升級 Template 修改到 Instance：在 Instance 加 `git remote add upstream <template-url>`，手動 cherry-pick

## 6.3 `.gitignore` 建議

```
# Python
__pycache__/
*.pyc
.venv/
venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# 暫存
*.tmp
*.bak
```

---

# 8. 既有檔案的特別注意事項

## 7.1 `00_a 台詞生產協議.md` 已完整

既有 00_a 已包含完整模式系統（10 種模式、所有規則），CODEX 在 Phase A–D 不需要重寫。新建 `00_e–00_j` 時引用 `00_a` 即可。

## 7.2 `00_b` 通用骨架 vs 蟲潮孤堡專案版

**Phase A 任務：**
- CODEX 從 `_design/references/00_b_反ai味檢查表_蟲潮孤堡專案版_參考用.md` 反推出**通用骨架版本**，寫入 `00_protocol/00_b_反ai味檢查表.md`
- 通用骨架應**保留結構**：檢查表分類、QA 報告格式、模式差異表
- 通用骨架應**移除作品專屬**：不得提及蟲潮孤堡、黑翼、蟲災、瑟琳、莉娜、諾拉等任何具體作品內容
- 蟲潮孤堡專案版本身留在 `references/`，Phase D 結尾搬到 Instance repo

## 7.3 既有 27 份模板的 frontmatter 補完（M6 加 depends_on 初值）

Phase A 需要把所有既有檔案的 frontmatter 加上 `entities`、`depends_on` 與 `weight`：

| 檔案 | entities | depends_on（初值） | weight |
|---|---|---|---|
| `00_*` 協議 | — | — | — |
| `01_a 世界觀總覽` | `[W-rules]` | `[]` | 1.0 |
| `01_b 世界語言規格` | `[W-language]` | `[W-rules]` | 1.0 |
| `01_c 陣營與階級語言` | `[W-language]` | `[W-rules]` | 0.7 |
| `02_a 專有名詞表` | `[V]` | `[W-rules]` | 1.0 |
| `02_b 俗稱與黑話表` | `[V]` | `[W-rules, W-language]` | 0.5 |
| `02_c 禁用詞與慎用詞表` | `[V]` | `[W-rules, W-language]` | 0.5 |
| `03_a 角色總表` | （所有 C-*） | `[W-rules]` | 各 0.1（索引性） |
| `03_b/c 模板` | — | — | — |
| `03_characters/main/<name>_聲線卡.md`（Instance 才有） | `[C-<name>]` | `[W-rules, W-language, V]` | 1.0 |
| `04_a 關係矩陣` | （所有 R-*-* 與所有 C-*） | `[W-rules]` + 相關 C-* | R 各 0.5，C 各 0.2 |
| `04_b 時間線` | 同上 | 同上 + `[P]` | R 各 0.3，C 各 0.1 |
| `05_a 主線大綱` | `[P]` | `[W-rules]` + 主要 C-* | 1.0 |
| `05_b 章節結構` | （所有 CH-*） | `[P]` | 各 0.5 |
| `05_c 角色弧線表` | （所有 C-* 加 CH-*） | `[P]` + 相關 C-* | 各 0.3 |
| `05_d 資訊揭露表` | （所有 CH-*） | `[P]` | 各 0.2 |
| `05_e 伏筆與回收` | （所有 CH-*） | `[P]` | 各 0.2 |
| `06_a 場景索引` | （所有 S-*-* 與 CH-*） | `[P]` + 相關 CH-* | S 各 0.5，CH 各 0.1 |
| `07_*/08_*/09_*` | （單場相關時標 S-<ch>-<n>） | 該場相關 C-* / R-*-* / CH-<n> | 1.0 |

**規則：**
- 實際 weight 數值由 CODEX 在 Phase A 依「合理的加總要 ≈ 100%」原則微調
- `depends_on` 初值可能不完整，使用者後續迭代時補完
- `04_a 關係矩陣` 由於是 1 份檔案承載多個 R-* + 多個 C-*，weight 必須用 map 表達
- 下游 pipeline 檔（07/08/09）的 frontmatter 還需要 scene_id / source_task / pipeline_state / mode_tag 等下游欄位（見 SPEC 5.2.3）

## 8.4 `archive/00_protocol_模式系統公版補丁_v_0_2.md`

狀態為 `APPLIED`，**不需要做任何處理**。保留作為歷史紀錄，幫助未來理解模式系統演化。

---

# 9. 給 CODEX 的實作備忘

## 9.1 開發環境

- CODEX 工作目錄：Instance repo 或 Template repo（依任務）
- Skill 開發環境：Claude Code（測試 `.claude/skills/` 機制）
- 測試 frontmatter 解析：執行 `python scripts/check_headers.py`
- 測試路徑引用：執行 `python scripts/check_paths.py`

## 9.2 寫新檔案的標準流程

1. 從相同類別的既有檔案抄出 header 風格
2. 寫內容
3. 跑 `check_headers.py` 驗證 header 完整
4. 跑 `check_paths.py` 驗證內部引用都有效
4. 跑 `check_paths.py` 驗證內部引用都有效
5. 加入 frontmatter 的 `entities`、`depends_on` 與 `weight`（依 SPEC 5.2 canonical schema）
6. Commit

## 9.3 修改既有檔案的標準流程

1. 確認該檔案目前的狀態（DRAFT / REVIEW / LOCKED）
2. LOCKED 文件需先取得確認
3. 修改後更新 `最後更新` 日期
4. 跑兩個 check 腳本
5. 若修改影響其他實體，列出來（依 `depends_on` 反查）
6. Commit

## 9.4 禁止事項（再次強調）

- 不得擅自把 DRAFT 升 REVIEW 或更高狀態（必須由 REVIEW gate 任務人工執行）
- 不得修改 LOCKED 文件的核心內容
- 不得擅自補完重大世界觀／角色／劇情設定
- 不得把作品專屬內容寫入 Template repo
- 不得在 Template repo 內 hard-code 任何具體作品

---

# 10. 命名與路徑慣例

## 10.1 檔名


- 用「`數字_小寫字母_中文名稱.md`」格式
- 子資料夾下的角色檔：`<角色名>_聲線卡.md`、`<角色名>_次要角色卡.md`、`<NPC類型>_模板.md`
- 任務包：`CHxx_Sxx_台詞任務包.md`
- 台詞檔：`CHxx_Sxx_<場景簡稱>_dialogue_vXXY.md`

## 10.2 章節編號

- 章節用兩位數：`CH01` ~ `CH27`
- 場景用三層：`CH01_S01`、`CH01_S02`、...

## 10.3 實體 ID（含 O7 分支支援）

- 角色：`C-<角色名>`（用實際角色名）
- 關係：`R-<名 A>-<名 B>`，A、B 按字典序
- 章節：`CH-<n>`
- 場景：`S-<ch>-<n>`
- 分支場景：`S-<ch>-<n><suffix>`，例如 `S-01-03a`、`S-01-03b`、`S-01-03sub`
- 對應檔名：`CH01_S03a_xxx.md`、`CH01_S03sub_xxx.md`

---

# 11. CODEX 審查請特別檢查

1. **檔案結構是否漏項**：Template 結構列表是否完整？
2. **frontmatter Canonical Schema** 是否與 SPEC 5.2 一致？parser 偽碼是否完整？特別檢查下游 7 個欄位（scene_id / source_task / source_dialogue / pipeline_state / mode_tag / qa_decision / qa_type）的解析
3. **雙語 skill 實作策略**：wrapper + smoke test 是否能跨 host work？
4. **動態組合 vs 靜態整合檔**：`/view-*` 動態組合的計算成本是否會在大型 repo 變慢？
5. **影響範圍評估**：depends_on 反查 + entities 反查互補後是否足夠？
6. **既有檔案 frontmatter 補完**：建議的 weight 分配與 depends_on 初值是否合理？
7. **下游 metadata 完整性**：07/08/09 目錄下檔案的 frontmatter 是否能機器可讀地反查任務包與台詞檔（透過 source_task / source_dialogue 雙向追蹤）

審查者請列出修正建議。

---

# 12. A.0 Parser 規格（v1.2 新增 via DF §11.1 + D-037 / D-042 / D-044 / D-045 + Contract A）

> **v1.2 新增章節 — 對應 Phase A.0 parser tasks 的具體規格清單。** 依 DF §11.1 + 三 specialist v0.3 patch + D-037~D-046 拍板統合為 9 大類處理項，每類對應 TASKS A.0.x 一個或多個 task。

## 12.1 Parser 9 大類處理項總表

| 大類 | 對應 DF / Contract | 對應 TASKS task |
|---|---|---|
| 12.1.1 phase_log 新欄位解析 | DF §11.1.1 + Contract A.2 | A.0.x phase_log 解析 + 8 enum 驗證 + cycle 偵測 |
| 12.1.2 dialogue_keys Map 解析 | DF §11.1.2 + Contract A.1 | A.0.x dialogue_keys Map 解析 + 內文 KEY comment 一致性驗證 |
| 12.1.3 全 repo KEY + alias unique 集合 | DF §11.1.3 + Contract A.1 + A.4 | A.0.x KEY 全 repo unique 集合 + 反向索引 |
| 12.1.4 art_metadata + A-* prefix 識別 | DF §11.1.4 + Contract A.3 + C.5 | A.0.x A-* metadata 掃描 + subtype 7 種驗證 + 禁止欄位偵測 |
| 12.1.5 內文 A-* cross-reference 解析 | DF §11.1.5 + Contract A.1 + A.3 | A.0.x 內文 A-* view-layer 提示 vs frontmatter 權威來源驗證 |
| 12.1.6 mode_tag / qa_type 擴充 enum 處理 | DF §11.1.6 + Contract A.5 + A.6 | A.0.x mode_tag 6 種 + qa_type 8 種 + registry 解析 |
| 12.1.7 entity_type_registry 讀取 | DF §11.1.7 + Contract A.5 | A.0.x entity_type_registry Template/Instance 讀取 + valid set 構建 |
| 12.1.8 qa_type_registry 讀取 | DF §11.1.8 + Contract A.5 | A.0.x qa_type_registry 讀取 + template_path 驗證 |
| 12.1.9 JSON export 結構化資料 API | DF §11.1.9 + Contract A.7 | A.0.x parser 提供 `get_all_entities()` / `get_all_dialogue_lines()` / `get_all_art_metadata()` / `get_manifest_snapshot()` API |

## 12.2 Parser 行為摘要（每大類關鍵驗證 / WARN / ERROR）

| 大類 | 關鍵 ERROR | 關鍵 WARN |
|---|---|---|
| 12.1.1 phase_log | `status: aborted` 缺 `abort_reason` / `detail`；`import_source != null` 但非 `/create-*` skill；`base_dialogue` 鏈條 cycle；`conflict_resolutions[*].decision` 不在 enum；`decision: create-as-new` 缺 `new_entity_id` | `iteration_count` 出現於非 SINGLE_ITER mode_tag |
| 12.1.2 dialogue_keys | KEY ↔ map key 不一致；`line_index` 順序 ↔ 內文 KEY 順序不一致；`status: deleted` 缺 `deleted_at`；`status: deprecated` 缺 `deprecated_reason`；`portrait`/`bgm`（非 null）不對應 valid A-* asset | 內文 `<!-- 立繪：A-... -->` 提示與 frontmatter 不一致 |
| 12.1.3 全 repo KEY unique | KEY 衝突（含 aliases） | — |
| 12.1.4 art_metadata | `subtype` 不在 allowed 7 種；`subtype` 在 reserved_subtypes 內；強制禁止欄位（`file_path` / `url` 等）出現 | `subtype: portrait` 的 owner 不存在於 C-*；`subtype: voice` 的 dialogue_keys_ref 不存在 |
| 12.1.5 內文 A-* | — | 內文引用 A-* 但 `depends_on` 未列；引用歷史 alias 而非當前 asset_id |
| 12.1.6 mode_tag / qa_type | enum 不在 valid set 內 | 未知 qa_type（registry 通過但 09_x 模板不存在） |
| 12.1.7 entity_type_registry | `user_extensions[*].type` 跟 core 重複；core 段被刪除但對應 entity 仍存在（防 silent drop） | user_extensions 用 `reserved_prefixes` 前綴；`target_dir` 不存在 |
| 12.1.8 qa_type_registry | `user_extensions[*].template_path` 對應檔案不存在 | 09_x 模板 `qa_type` 值與 registry entry 不對應 |
| 12.1.9 JSON export API | — | parser 啟動失敗時降級為「空 records[]」並 WARN |

## 12.3 Parser API 設計（建議 — 屬 Phase A.0 實作範圍）

```python
# 偽碼示意；具體實作由 Phase A.0 task 決定
class FrontmatterParser:
    def parse_dialogue_keys_map(self, file_path) -> Dict[str, DialogueKeyEntry]: ...
    def get_all_dialogue_keys() -> Set[str]: ...                 # 全 repo unique 集合
    def get_alias_to_current_key_map() -> Dict[str, str]: ...    # 反向索引
    def parse_art_metadata(self, file_path) -> List[ArtMetadataEntry]: ...
    def get_asset_completeness_by_subtype() -> Dict[Subtype, CompletenessStats]: ...  # D-045
    def get_entity_type_registry() -> EntityTypeRegistry: ...
    def get_qa_type_registry() -> QaTypeRegistry: ...
    def parse_phase_log(self) -> List[PhaseLogEntry]: ...
    def validate_phase_log(self, entries) -> List[ValidationError]: ...  # cycle / abort_reason / etc.
    
    # JSON Export API（Contract A.7）
    def get_all_entities(self) -> List[EntityRecord]: ...
    def get_all_dialogue_lines(self) -> List[DialogueLineRecord]: ...
    def get_all_art_metadata(self) -> List[ArtMetadataRecord]: ...
    def get_manifest_snapshot(self) -> ManifestSnapshot: ...
```

## 12.4 Parser 啟動順序

1. 讀 `<instance_root>/entity_type_registry.yaml`（不存在 → fallback Template + WARN）
2. 讀 `<instance_root>/qa_type_registry.yaml`（不存在 → fallback Template + WARN）
3. 掃描 `<instance_root>` 全 markdown 檔
4. 對每個 .md：
   - 解析中文 header 5 欄
   - 解析 YAML frontmatter（含 entities / depends_on / weight / 下游 8 欄 / dialogue_keys / art_metadata）
   - 對下游台詞檔解析內文 KEY comment + A-* cross-ref
   - 對 A-* metadata 檔驗證強制禁止欄位
5. 建全 repo KEY + alias unique 集合
6. 對 `.protocol_version` 解析 phase_log + 驗證
7. 構建內部資料結構（entity index / dialogue_keys index / art_metadata index / phase_log index）

## 12.5 Parser cache / mtime / content-hash

- v1.2 採 disk fstat mtime 為 server-side 權威；前端 baseline 記憶體 cache
- content-hash 升級備案為 PENDING（NS-23；DF Phase 4 補）
- 詳見 Contract C + UX §11.7.5

## 12.6 issue_type_registry 載入 + 驗證（v1.3 新增 via D-047 + Contract D）

**對應 §12.1.10 — Phase A.0 後續 patch round 落地（非 A.0.10 範圍）：**

| 項 | 規格 |
|---|---|
| Registry 載入 | parser 啟動時讀 `<instance_root>/issue_type_registry.yaml`（不存在 → Template fallback + WARN）|
| Schema 驗證 | 5 skill key 合法性 / id 範圍（core: 1-99；user_extensions: ≥100）/ required_level enum / locked 布林 / question_summary 字串 / protocol_ref 字串 |
| user_extensions 衝突 | id 與 core 重複 → ERROR；id < 100 → ERROR；locked=true → WARN（自動視為 false）|
| core_overrides 衝突 | skip_id 對應 locked=true 議題 → WARN（條目忽略）；skip_id 不存在於 core → WARN（條目忽略）|
| API 設計（建議）| `load_issue_type_registry(repo_root) -> IssueTypeRegistry`；`get_skill_issues(skill_key) -> list[IssueEntry]`（套用 core + user_extensions − core_overrides）|

**落地時機：** A.0.10 patch round（Stage 0）**不**處理本項；屬 Phase A.X 後續 patch round 或 Phase B 實作前的 parser 補強（按需求觸發）。

## 12.A.0.10 Gate 1 NO-GO patch round 紀錄（v1.3 新增）

**觸發：** Gate 1 CODEX review 識出 3 critical parser integration gap（NO-GO 判定）：
- C1: `build_repo_index()` 未整合 A.0.5 cross-ref validator + A.0.2 art existence cross-check
- C2: `entity_type_registry` 一般 ID 驗證未在 index 層套用
- C3: Windows UTF-8 BOM header 漏讀風險

**修補方式：** master 第五輪委派新 CODEX 對話跑 A.0.10 patch round（starter scope 嚴限 3 critical），落地：

| Critical | 修補位置 | 新函式 / 變更 |
|---|---|---|
| C1 | `scripts/parse_frontmatter.py:1126-1162` / `:1225-1273` | `_validate_dialogue_files_with_art_index()` — 在 art_metadata_index 建好後重跑 dialogue_keys art-aware 驗證 + 呼叫 `validate_body_vs_frontmatter_consistency()`；issue 去重 `_dedupe_validation_issues((line_num, message))` |
| C2 | `scripts/parse_frontmatter.py:1164-1209` | `_validate_frontmatter_entity_id_fields()` — 對 frontmatter entities / depends_on 跑 `validate_entity_id`，issues 聚合到 RepoIndex |
| C3 | `scripts/parse_frontmatter.py:459`（含 phase_log / registry / fallback source read 入口）| `parse_file()` 改 `encoding="utf-8-sig"` + `parse_markdown_text()` strip leading BOM |

**驗證：** 6 synthetic case 全 PASS（missing A-* / body A-* not in depends_on / historical alias / unknown entity prefix / invalid pattern / UTF-8 BOM）；check_headers.py 0 ERROR（75 files / 13 WARN）；build_repo_index('.') 0 ERROR（parsed_files=99 / 43 WARN）；100 fake dialogue perf 0.44s（< 5s）。

**影響：** A.0 parser 從「可跑但不完整 gate」升為「可信 gate」，後續 A.4 / A.7 / A.0F.8 / C.5a / D.4 可信賴 build_repo_index 為唯一 issue source。M1 / M3 / M4 / m1-m3 finding 留 Phase A.X 後續 patch round（不在 Stage 0 scope）。

**Cross-ref：** CODEX_GATE_1_REVIEW_REPORT.md / CODEX_A010_PATCH_STARTER.md / CODEX_A010_PATCH_REPORT.md / DECISIONS_LOG §6.9.7

---

# 13. Frontend Adapter API（v1.2 新增 via UX §11.8.3 + Contract C + B.2/B.4）

> **v1.2 新增章節** — 對應 frontend server.py 的 API endpoint 規格清單。前端 server 職責：local viewer / editor + Save race guard + Asset Panel query + Export prompt 元資料供應。**不**執行 export / 不啟動 subprocess（D-029 α + D-038）。

## 13.1 Frontend server 啟動

```bash
# Instance root 下
python _tools/frontend/serve.py
# > Serving from D:/劇本開發工具
# > Open browser: http://localhost:8765
# > Press Ctrl-C to stop
```

對應 UX §11.8（Build / package / 啟動規格）。

## 13.2 Frontend Adapter 8 個 API Endpoint（v1.2）

| Endpoint | 用途 | 對應 Contract / UX |
|---|---|---|
| `GET /api/scene/<id>/header` | Save race guard pre-flight 讀 frontmatter `狀態` + mtime checksum | B.2 / UX §11.5.8 |
| `POST /api/scene/<id>/save` | Save flow Step 5（含 mtime checksum）| B.2 / UX §11.5.8 |
| `POST /api/scene/<id>/save-as` | LOCKED race modal B 選項「另存為 DRAFT proposal」 | B.2 / UX §11.5.8.2 |
| `GET /api/scenes/<id>/versions` | 多版本 entity manifest query（場景 → 版本 list）| NS-15 / UX §11.3.3 |
| `GET /api/scenes/<id>/keys/<key>/lines` | 場景行查 query（依 i18n KEY 找跨版本 line content）| NS-30 / UX §11.3.5 |
| `GET /api/assets?scope=...` | A-* asset manifest query（場景反查所有可用立繪 KEY）| NS-2 / Contract B.4 / UX §11.1.6a |
| `GET /api/assets/<id>/usage` | A-* 反查「該 KEY 被多少場景引用」（`dialogue_keys.<KEY>.portrait/bgm/sfx` 反查）| UPS-UX-80 / Contract B.4 |
| `GET /api/scope-counts?scope=...` | Export prompt 用「組 prompt 所需的元資料」（給 prompt stats 區塊填具體數字）| 4.2a.2 |

## 13.3 Frontend Adapter 不提供的 endpoint（明示）

- **不**提供 `POST /api/export/run`（D-029 α + D-038 — export 不在前端執行）
- **不**提供 `POST /api/skill/run`（同上 — agent 不在前端執行）
- **不**提供 `GET /api/qa/run`（同上 — QA 由外部 agent 執行）

## 13.4 全文 search index

v1.2 採 client-side full-scan fallback（個人工具規模可接受）；large repo 才升級 search index（NS-31 Pending；屬後續優化）。

## 13.5 Edit-lock 機制

v1.2 採 advisory lock（不強制；server 端可實作 client_session_id 註冊）— NS-25 / UX §11.7.7。

## 13.6 mtime / content-hash

- mtime 為 server-side 權威；前端 baseline 記憶體 cache
- content-hash 升級備案為 Pending（NS-23）

## 13.7 對應 Phase A.0 內部任務分派

詳見 TASKS Phase A.0 補的 frontend adapter task 群。
