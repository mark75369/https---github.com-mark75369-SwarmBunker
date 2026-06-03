狀態：DEPRECATED
版本：v0.1（11th master frontend Batch 4 — F8 / NEW_REQ_32 長線 direction A 設計拍板 package；judge panel wf_8e11eda5-789 綜合 + user 4 分歧點拍板：① 單一 ORG-* core ② prefix ORG-* ③ Phase 0+1 floor ④ registry 修復獨立 D-073；本 package 記錄拍板'd 設計方向，Phase 0+1 實作待落地）
最後更新：2026-06-02
適用範圍：F8 / NEW_REQ_32 ORG-* 實體型別實作依據（D-071 拍板紀錄 + 實作 spec）
優先級：高

# D071_DECISION_PACKAGE — F8 / NEW_REQ_32：非人格 / 組織型對抗源實體（ORG-*）

> **本檔定位：** F8 長線 direction A（新實體型別）的設計拍板紀錄 + 實作 spec。方向經 judge panel（4 提案 × 3 評審交叉評分 → 綜合）+ user 4 分歧點拍板確定。**本檔不落地任何 LOCKED 改動**；正式 registry / parser / spec 變更走四層防線 + DECISIONS_LOG D-071 時為準。
>
> **與 D-064 的關係：** 組合而非取代。D-064（Batch 1 落地）= NEW_REQ_32 短線 = `/create-character` 非角色拒絕閘；本案 = 長線正向落點（給「不會說話但需獨立追蹤」的對抗源一個 node 身份）。

## 1. 拍板結論（user 2026-06-02 決）

| # | 分歧點 | 拍板 | 評審立場 |
|---|---|---|---|
| 1 | 型別數量與性質 | **單一 `ORG-*` core** | 3 評審一致列第一（8/8/7.5） |
| 2 | prefix 標籤 | **`ORG-*`**（非 F-*） | 2 user-facing 評審偏好；貼 01_a §9「勢力與組織」 |
| 3 | 首批落地範圍 | **Phase 0+1 floor**（/create-org 延 Phase 3） | 最低風險、最快見效 |
| 4 | registry 損壞修復歸屬 | **獨立 D-073 precursor**（非併 D-071） | live parse bug，與 F8 設計解耦、先落地 |

**被否決方案：** 雙型別 F-*+ORG-*（雙 one-way door + F/ORG taxonomy 心智負擔，user-mental-model 評審視為 regression）；no-new-type user_extension（instance-local 碎片化、無 /create-org 則實質難 author）。

## 2. 完整 schema 規格（D-071 Phase 1）

新增 core 條目（插入位置：`A` subtype block 之後、`reserved_prefixes:` 之前；**template 與 instance root 兩檔 core block 必須逐字相同**，否則 `_validate_instance_core_entries` 報 mismatch）：

```yaml
  - type: ORG
    description: 組織 / 非人格反派 / 組織型對抗源（公司 / 制度 / 機構 / 體系 / 殘留或已解散組織；不會說話、無聲線卡、不進 /dialogue-write 為說話者；是可被 P / S / R / C 以穩定 ID depends_on / cross-ref 的一級節點）
    id_pattern: ^ORG-.+$
    target_dir: 11_organizations/
    cross_ref_allowed: true
    locked: true
```

| 欄位 | 值 |
|---|---|
| type id | `ORG`（單一，不拆 F/ORG） |
| id_pattern | `^ORG-.+$`（與 `^C-.+$` 同風格） |
| target_dir | `11_organizations/`（新編號目錄，遵 NN_name/；避開 create-character 的 D-050 邊界、避免污染 03_characters/） |
| weight | scalar `1.0`（單檔單實體 → `{ORG-<name>: 1.0}`） |
| cross_ref_allowed | `true` |
| locked | `true`（core = LOCKED-tier；one-way door，user 已有意識簽核不可逆性） |
| core vs extension | **core** |

**完成度數學（ARCH §2.3）：** per-entity 正規化，分母只含貢獻該 entity 的檔；新增 ORG-* **數學上不可能** distort 既有 W/V/C/R/P/CH/S/A 百分比，僅 /status 多一列。

## 3. 影響檔清單 + 各檔改動

### 3a. Registry（LOCKED-tier，走四層防線）— Phase 1
- `entity_type_registry.yaml`（root instance）：append ORG 條目（前置：D-073 已修損壞）。
- `_design/registries/entity_type_registry.template.yaml`：append ORG 條目（與 root core block 逐字相同）。

### 3b. parse_frontmatter.py — Phase 1（~3-4 行 + fixtures；非「零改動」）
驗證路徑（`validate_entity_id` / `_resolve_entity_type_entry` / `all_valid_types`）**零邏輯改動** — ORG-* 一進 registry 即生效（僅 `entry.type=="A"` 有 subtype 特例，ORG-* 一般化通過）。需動：
1. `ENTITY_ID_RE`（line 108-110）：加 `ORG-.+` alternative（否則 `_validate_phase_log_entities_touched` 對 `ORG-清道夫` 噴假 WARN）。〔附帶觀察：此 regex 已與 registry drift、缺 W-style — 記為 §6 tech-debt follow-up，不在 D-071 scope〕
2. `OUTLINE_ENTITY_TYPES`（line 104）：**判斷後不改**（ORG 是 world-tier 節點非 outline 實體）。
3. dir 掃描：確認 `11_organizations/` 被 `_iter_repo_markdown_files` 涵蓋、不在 EXPORT_EXCLUDED / SOURCE_MATERIAL 排除集（新編號目錄自動涵蓋，補 1 個 confirming test）。
4. fixtures：`ORG-清道夫` 驗證通過、`ORG-` 格式不符、ORG-* 在 entities/depends_on 可 resolve。

### 3c. Specs — Phase 1
- **DATA_FORMAT_SPEC §5.2**：core 型別 append 屬 additive，**無需 bump schema_version**（change note 記錄即可）。
- **ARCH §2.3**：註記 ORG-* scalar 1.0 + per-entity 正規化；**§3.4** skill→protocol map 加 create-org → 00_n（Phase 3）。
- **SPEC / UD**：核心無語意 supersede。

### 3d. SKILL.md
| Skill | 改動 | Phase |
|---|---|---|
| **status** | enumeration 加 ORG 分組（純讀） | 2（必） |
| **create-character** | Stage 1.0 gate alternative #3 文字更新 → 指向 live `/create-org`；**拒絕行為與 D-050 邊界完全不動**（仍只寫 03_characters/） | 2（必） |
| **create-org（新）** | Phase B 5 階段 skill；只寫 `11_organizations/`，不寫 00_protocol/、不寫 03_characters/、不建聲線卡 | 3（延） |
| **iterate-org（新）** | 00_j v0.2 五階段；ORG-* 編輯 + 清道夫遷移 | 3（延） |
| **check-gaps / view-world(or view-org) / export-org** | ORG-* awareness | 3（延） |
| **create-relationship** | 可選：允許 R-* 一端為 ORG-*（C-瑟琳 ↔ ORG-清道夫；清道夫 workaround 乾淨遷移落點） | 3（延） |

### 3e. expected_entities / 00_protocol
- **expected_entities**：ORG-* opt-in，不列必有實體（與 P/CH 缺漏只在被 depends_on 時報的 parity 一致）。
- **新 `00_protocol/00_n_組織創建協議.md`**：create-org 的 5 階段權威，對齊 00_f/00_l 體例。Phase 3。

## 4. registry 損壞修復（D-073 — 獨立 precursor）

**user 拍板：標獨立 D-073、F10 落地後即落地、與 F8/D-071 解耦。**（NEW_REQ_46）

- **損壞實況：** root `entity_type_registry.yaml` line 94 拋 `yaml.parser.ParserError`；line 93 `user_extensions: []` 後重複孤兒尾巴（line 94-98：`description:` / `- prefix: SKILL` / `description:` / 第二個 `user_extensions: []`）。
- **修法：** 刪 line 94-98 孤兒尾巴，保留單一結尾 `user_extensions: []`。
- **評審一致更正（重要）：root 並未缺 W-style。** 實測 root 與 template 皆含 10 core 型別（含 W-style）；損壞純是尾巴重複。**rationale 必須是「純刪重複尾巴」，不可寫成「restore missing W-style / 9 型別」**（後者是冠軍/保守提案原稿誤診，會誤導 L1）。修法 = 最小 truncate（**不** overwrite-from-template，以保留 root 既有內容）。
- **L0 已完成（Batch 4 worktree）：** 已 truncate + 實測 `yaml.safe_load` 通過、10 core types + 3 reserved + `user_extensions: []` 與 template `core` deep-equal。L1/L2/L3 待 F10 commit 後跑（帳本序列寫）。
- **L2 加固：** smoke check `python -c "import yaml; yaml.safe_load(...)"` 斷言 0 ERROR。
- **latent-bug：** 損壞使 instance-side `user_extensions` 在 parse 失敗時靜默丟失、退回 template-only core；即使 ORG-* 永不啟用都該修，故獨立先行。

## 5. 既有 R-清道夫-* workaround 遷移（Phase 3，opt-in）

user 已建 `R-清道夫-瑟琳` / `R-清道夫-諾拉` / `R-清道夫-莉娜`（把組織塞進關係端，語意失真但合法 `^R-.+-.+$`）。

**處置：不自動改寫、不刪除（守 LOCKED 規則 #3 + 不靜默改寫 user 內容，同 D-054 posture）。opt-in 引導遷移：**
1. `/create-org` 建 `ORG-清道夫`（11_organizations/），harvest 三個 R-* 的對抗來源內容。
2. （Phase 3 若 create-relationship 接受 ORG endpoint）每個 R-清道夫-X 改 home 為 `C-X ↔ ORG-清道夫`。
3. user 明確確認後，舊 R-清道夫-* 標 **DEPRECATED（不刪）**，phase_log 記 migration entry。
4. 預設 /status 出 advisory：「ORG-清道夫 型別可用；/iterate-relationship 可重指 R-清道夫-* — 可選」。

## 6. 工時 + 分步落地

總約 **8–14h**（遠低於 M4 §3.8 direction-A 30–50h 原估 — parser 已 registry-driven、D-064 已吸收 create-character 拒絕工作、不複用 create-character 寫檔而以薄 /create-org 承載）。

| Phase | 內容 | 工時 | 先後 |
|---|---|---|---|
| **Phase 0**（= D-073） | 修 root registry 損壞；四層防線 + yaml.safe_load smoke + 最小 parse 單測。獨立 commit。 | 1–2h | 先（F10 後） |
| **Phase 1**（= D-071 core） | ORG 條目 append（template + 修好 root，core block 逐字相同）；parser 三表面 + fixtures；DATA_FORMAT_SPEC/ARCH 註記；D-071 寫 DECISIONS_LOG。LOCKED-tier 四層防線。 | 4–7h | 先 |
| **Phase 2** | create-character gate 一行 + status ORG 分組。 | 1–2h | 中 |
| **Phase 3（可延後）** | /create-org + /iterate-org + 00_n + 中文 wrapper；create-relationship ORG endpoint + R-清道夫-* 遷移；check-gaps/view-org/export-org。 | 4–8h | 延 |

**最小可用底線 = Phase 0+1**（ORG-* 成 valid 型別、可手工 author / 走 /integrate）。

## 7. 風險 / Blast radius

整體小且 additive。強制核心（Phase 0+1）僅動：2 registry YAML（LOCKED-tier → 四層防線）、parse_frontmatter.py（~3-4 行 + fixtures）、DATA_FORMAT_SPEC/ARCH 註記、新目錄 `11_organizations/`。既有 /create-*//iterate-*//view-*//export-* 行為零改（自動接受 ORG-* depends_on）；既有權重/完成度零位移；D-064 閘門零削弱。

**具名風險：**
1. **D-050 違規（本案已避開）：** 不讓 create-character 寫 01_world/；改薄 /create-org + 新 11_organizations/。
2. **one-way door：** core:locked 不可逆、所有 instance 繼承（user 已簽核）。
3. **Template/instance core block drift：** 兩 ORG block 須逐字相同；mitigation：複製同 block + CI/L2 斷言。
4. **precursor 排序：** Phase 0（D-073）必先於 Phase 1。
5. **scope creep：** Phase 3 明確可延後；floor 不含。
6. **tech-debt follow-up（不在 D-071 scope）：** `ENTITY_ID_RE`(line 108) / `_entity_type_from_id`(line 1635) 是 registry 硬編碼鏡像（前者已 drift 缺 W-style），長期應 registry-derived。建議另開 NEW_REQ 追蹤。

## 8. Provenance

- judge panel run：`wf_8e11eda5-789`（4 提案 × 3 評審 + 綜合；8 agents）。
- 冠軍：`minimal-single-ORG`（registry-consistency 8 / user-mental-model 8 / cost-risk 7.5；3 評審一致第一）。
- 評審抓到並修正的 2 錯：① W-style 未缺失（誤診）② create-character 寫 01_world 違 D-050（改 /create-org）。
- 採納 grafts：first-principles（11_organizations/ 新目錄、精確 parser checklist、referenceability narrative）；dual（R-* ORG endpoint + harvest/DEPRECATED 遷移）；no-new-type（one-way-door 拍板準則、latent-bug articulation、yaml smoke gate）。
- user 拍板：2026-06-02 AskUserQuestion（4 分歧點全採推薦）。

**Cross-ref：** POST_LOCK_PENDING NEW_REQ_32（F8 長線；待 D-071 Phase 1 落地時 RESOLVED）+ NEW_REQ_46（registry 損壞；D-073）/ M4_USER_TEST_REPORT §3.8 / DECISIONS_LOG D-064（短線閘）+ D-071（待寫）+ D-073（待寫）/ entity_type_registry.yaml(+template) / scripts/parse_frontmatter.py / .claude/skills/create-character/SKILL.md。
