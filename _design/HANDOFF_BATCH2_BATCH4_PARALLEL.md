狀態：DEPRECATED
版本：v1.0（Batch 3 landed 後，為 Batch 2 大綱鏈 / Batch 4 entity 型別 兩個平行對話準備的冷啟動交接包；2026-06-02）
最後更新：2026-06-02
適用範圍：給接手 Batch 2 或 Batch 4 的平行對話 — 冷啟動可讀
優先級：高

# HANDOFF — Batch 2 / Batch 4 平行啟動包

## 0. 一句話現況

`frontend-tools-a0f` 上 **Batch 1 + Batch 3 已 land**。剩 **Batch 2（大綱鏈 F16/17/18/19）** 與 **Batch 4（entity 型別 F8 深做 + F10）** 兩個深度批，功能正交、可平行，但共享數個帳本/spec 檔需協調。本檔給兩個平行對話各自的 scoped brief + 防碰撞規則。

## 1. ⚠️ 環境陷阱（先讀）

- **production = `D:\劇本開發工具\`**（git root；remote `https://github.com/mark75369/Writing-tools.git`；branch `frontend-tools-a0f`）。
- `D:\劇本開發工具\_sandbox\snapshot\` 是 git-ignored 拋棄式副本，不是真倉庫。
- 路徑易打錯：`開發`(發) vs `開発`(発)；用 `git -C "D:/劇本開發工具"` 或 bash relative path。
- `scripts/__pycache__/*.pyc` 可能仍被追蹤、製造 status 噪音（已派獨立清理任務；commit 時用具體 path stage、勿 `git add -A` 連 pyc 一起）。

## 2. 冷啟動必讀

先讀本檔 → `_design/M4_USER_TEST_REPORT.md` §3（對應 finding 細節 + 每 finding 的 Stage 2 REVIEW prompt / Stage 3 APPLY target files）→ `_design/POST_LOCK_PENDING.md` 對應 NEW_REQ entry → `_design/REVIEW_LOOP_PROTOCOL.md`（四層防線）→ `_design/DECISIONS_LOG.md` 尾段（確認最新拍板號）。

## 3. 🔢 決策編號預留（杜絕撞號 — 平行對話必守）

- **最後拍板 = D-066**（DECISIONS_LOG §6.19.5）。
- **D-056~D-062 是對話 B 預留帳，不可動**（F3=D-056 / F17+F18 候選=D-060 / F19 候選=D-061 / NEW_REQ_44=D-062）。
- **D-063~D-066 已用**（Batch 1 Wave2）。
- **預留號段（本批分配，互不重疊）：**
  - **Batch 2 → D-067 ~ D-070**
  - **Batch 4 → D-071 ~ D-074**
- **M4 報告裡 F17/F18 的候選 D-060、F19 的候選 D-061 一律作廢改用乾淨號**（沿用 Batch 1 Wave2 把 D-057/D-058 作廢改 D-063/D-064 的先例；因對話 B 持有 D-056~062 預留段）。落地時在 DECISIONS_LOG + POST_LOCK 註記「原候選 D-060/D-061 vacated → 改 D-0xx」。
- ⚠️ **待 user 釐清**：對話 B 是否仍 active？若已 defunct，D-056~062 預留段可正式釋放；若 active，F17/F18/F19 該由誰落地需協調（避免兩邊都改 outline SKILL）。**B2 落地這些 finding 前必須先解這題。**

## 4. 🚧 跨批碰撞 map（平行必守）

| 共享檔 | B2 動？ | B4 動？ | 規則 |
|---|---|---|---|
| `_design/DECISIONS_LOG.md` | 開 D-067~070 | 開 D-071~074 | **序列寫**：一次一個對話寫帳本；用預留號段杜絕撞號 |
| `_design/POST_LOCK_PENDING.md` | NEW_REQ_40/41/42/43 | NEW_REQ_32/34 | 不同 entry，但**序列 merge**避免 header 版本行打架 |
| `_design/UPSTREAM_DOWNSTREAM_SPEC.md` | §1.3/§1.4 | （F8 多在 00_f/registry，少碰 UD） | B2 owns UD §1.3/1.4；若 B4 需碰 UD 先知會 |
| `scripts/parse_frontmatter.py` | — | F8 可能加 docx/型別支援 | B4 owns；與已 land 的 F15 同檔，B4 從 HEAD rebase |
| `_design/registries/entity_type_registry.yaml`(+template) | — | **F8 核心** | B4 owns |
| `.claude/skills/create-outline`, `create-detailed-outline` | **B2 核心** | （F8 長線可能碰 outline 引用 entity） | B2 owns；F8 走短線則不碰 |
| `_design/ARCHITECTURE.md` §3.3 | — | **F10 副對話 lifecycle** | B4/F10 owns |

**隔離機制**：每對話開自己的 git worktree / 分支（`feat/batch2-outline`、`feat/batch4-entity`），各自 commit，**序列 merge 回 `frontend-tools-a0f`**（B 先或 B4 先都行，但帳本檔 merge 一次一個）。

## 5. 節奏（依風險開關）

兩批都**動 LOCKED / 跨檔預留帳 → 深度抗審**（四層防線 L0→L1 外審→L2→L3 user 簽字；動 LOCKED 須走 AGENTS.md 規則 4 + DECISIONS_LOG D-NNN）。L1 建議用獨立 agent / dynamic workflow；兩個平行對話亦可互當對方 L1 reviewer（REVIEW_LOOP_PROTOCOL §5 推薦）。

## 6. Batch 2 — 大綱鏈 scoped brief

**Finding**：F16 / F17 / F18 / F19（Meta-pattern E；內部強耦合，建議四個同輪做）。
- **F16（NEW_REQ_40）**：`/create-outline`→`/create-detailed-outline` 間缺 DRAFT 原始細節保全層。user 已 ad-hoc 用 `05_plot/05_f_關卡原始細節備忘.md`。可能涉新 `00_protocol/00_m_保全層協議.md`。→ **D-067 或 D-069**。
- **F17（NEW_REQ_41）+ F18（NEW_REQ_42）**：遊戲設計語言 outline mode + 開戰前/戰鬥/戰鬥後場景結構。需 **pattern pack 機制**（依 00_b §1 作品類型載入；可能新 `_design/registries/pattern_pack_registry.yaml`）。→ **D-067**（原候選 D-060 作廢）。
- **F19（NEW_REQ_43）**：個人線 vs 主線邊界 check（群像作品 footgun）。→ **D-068**（原候選 D-061 作廢）。
- **target files / Stage 2 prompt**：見 M4 報告 §3.16–§3.19 各 finding 的「Claude Code workflow scope」段。
- **動 LOCKED**：`/create-outline`、`/create-detailed-outline` SKILL + UD §1.3/1.4 + 可能新協議 → 深度抗審。
- **前置**：先解 §3 的「對話 B 是否 active / F17-19 由誰落地」協調題。

## 7. Batch 4 — entity 型別 + 副對話 UX scoped brief

**Finding**：F8 深做 + F10（兩者邏輯不強耦合，可拆但同批管理）。
- **F8 長線（NEW_REQ_32 的方向 A）**：新 `F-*/ORG-*` entity 型別（非人格反派 / 組織型對抗源）。~30-50h，跨 `entity_type_registry`(+template) + 多個 SKILL.md + `parse_frontmatter.py`。**最大、最高風險**。註：F8 短線（方向 C，refusal gate）已於 Batch 1 D-064 落地；本批是長線實體化。→ **D-071**。
  - 先決：建議先做設計拍板（要不要新型別、weight、id pattern、target_dir、影響哪些 SKILL）再動工；可用 design workflow 跑 judge panel。
- **F10（NEW_REQ_34）**：副對話 / sub-conversation lifecycle UX 規則（主對話不該太早關副對話等 8 條）。動 `ARCHITECTURE.md` §3.3 新增 §3.3.3 + AGENTS.md/CLAUDE.md/skill_invocation_guide。→ **D-072**（或判無需 D-NNN）。
- **target files / Stage 2 prompt**：見 M4 報告 §3.8（F8）、§3.10（F10）。
- **動 LOCKED**：entity_registry template + 多 SKILL + ARCH → 深度抗審。

## 8. Batch 1 + Batch 3 已完成（背景）

- Batch 1（Wave1+2）：F7/F8gate/F9/F11/F12/F13 + QA 強化 + REVIEW_LOOP_PROTOCOL（D-063~066）。詳 `_design/HANDOFF_BATCH1_IMPL_SESSION.md`。
- Batch 3：F2/F4/F5/F15（NEW_REQ_26/28/29/39 RESOLVED；merge `ea72a67`）。零-LOCKED、無 D-NNN。
- 流程教訓（`_design/HANDOFF_BATCH1_IMPL_SESSION.md` §5）：深度抗審值得用在動 LOCKED / 跨預留帳；封閉式零-LOCKED 改動用精簡迴圈。但 Batch 3 的 L1 仍在 F5 抓到一個真 MAJOR（偵測邏輯語意 bug），故 mandated L1 不可省。
