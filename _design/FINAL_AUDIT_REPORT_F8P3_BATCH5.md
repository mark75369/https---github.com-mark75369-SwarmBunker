狀態：DEPRECATED
版本：v1.0（Step 4 最終全稽核：F8 Phase 3 + Batch 5 全 land 後重跑 8 維 + ORG smoke + falsification；workflow wf_f81550df-650，35 agents / 1.87M token / 623 tool uses）
最後更新：2026-06-03
適用範圍：feat/f8p3-audit-batch5（Step 4 QA 閉環結論；餵 Step 5 wake-up + L3）
優先級：高

# 最終全稽核報告（QA 閉環）— F8 Phase 3 + Batch 5 registry DRY

## 1. 一句話總評

**GO-with-fixes** — 7 維全綠（D1-D7 機械/規格/registry/xref/ledger/backcompat/phases 無 BLOCKER），ORG smoke **4/4 + falsification PASS**（sandbox 刪 ORG → registry-derived ENTITY_ID_RE branch 11→10、拒 ORG-測試，**證明 parser DRY 為真 load-bearing、非 hardcoded 鏡像**）。本批引入 1 MAJOR（ORG skill 索引 drift）+ 1 INFO overclaim，**已本輪自修**；其餘為 pre-existing backlog → NEW_REQ_49 尾巴。

## 2. Confirmed findings（去重，修正後嚴重度）

### MAJOR（本批 F8 Phase 3 引入，已本輪自修）
- **ORG skill 未回填 3 份 agent-discovery 索引表**：`/create-org`·`/iterate-org`（+ 中文 wrapper）四檔磁碟存在，但 AGENTS.md / CLAUDE.md / `_user_manual/skill_registry_full.md` 三索引表漏列 → 依索引 discovery 的 agent 找不到 ORG skill（Claude Code 自動 discovery 不受影響，故非 runtime break，但對「索引一致性為前提」的 repo 實質有害）。**已修**：AGENTS.md B/D 列 + CLAUDE.md v0.7 B/D 列 + skill_registry_full.md B/D 兩列補 ORG。

### INFO（本批引入，已本輪自修）
- **spec-doc 漂移強制後盾尚未 load-bearing 的 prose overclaim**：`check_entity_type_consistency.py` 的 ERROR 級硬比對只認 `<!-- REGISTRY-MIRROR -->` marker；全 repo 0 個生產 spec-doc 含此 marker，故 spec-doc 鏡像目前 lint 僅 INFO（**parser 端強制為真且 11 型別全綠**；spec-doc 暫由 parser-mirror + 人工 L1 守護）。此屬 commit 8cef601 + script docstring 明文 park 的 NEW_REQ_49 尾巴（行為與文件一致、刻意漸進）。**但** 06_data_structure / status SKILL 的 prose 用現在式「守護一致性 / asserts these mirrors stay equal」屬 overclaim → **已軟化措辭**（標明 parser 端強制 vs spec-doc 待 marker）。

### MINOR / INFO（pre-existing backlog → NEW_REQ_49 尾巴 / 衛生）
- **[pre-existing] W-style/ORG 列舉殘餘未收斂**：`L3_EXPORT_PROMPT_SCHEMA §79/81/96`（export scope.type=full 掃描指令，literal reading 會漏 W-style/ORG 檔；同段 L80「所有 entity」為權威語意緩衝）、`_user_manual/07_customization.md` L46/L72 core 數量自相矛盾（8 vs 9，皆 < 11）、`IC:1311` + `UX_SPEC:2617`「7 entity types」分工表、`UPSTREAM_DOWNSTREAM_SPEC:5863`「7 種敘事 entity」命名快照。i1/i3 已點名，Batch 5 §2 scope 縮減未含 → **NEW_REQ_49 尾巴 W-style/ORG 殘餘 sweep（留痕）**。
- **[pre-existing] frontend pyc tracked**：`_tools/frontend/__pycache__/server.cpython-310.pyc` 違反 .gitignore（完成 3fa3c63 partial untrack）→ **已 git rm --cached**。（評審反駁：.pyc 不會 shadow 同名 .py；byte 差為 branch 分歧假象，非本批改動。）
- **[pre-existing] server.py:458 OUTLINE_ENTITY_TYPES 第三鏡像** 不在 D-075 lint scope（lint 只 introspect parse_frontmatter + rglob *.md）→ NEW_REQ_49 尾巴。
- **[pre-existing, 非現行 bug] C-ORG 裸名 ID 碰撞**：R-`<a>`-`<b>` 去前綴，C↔C 與 C↔ORG 同裸名會撞同 ID（dup guard abort，非覆蓋）；需 C 與 ORG 同名之 contrived 前提（i4）。
- **[本批, cosmetic] DECISIONS_LOG §7 摘要 §6.26/§6.25 局部逆序**（與既有 §6.13/§6.14 同型；body header 排序正確、摘要齊全）。

## 3. Smoke 結論：PASS（4/4 + falsification）
- ORG-測試 fixture（5 欄 header + entities/depends_on/weight）實跑 parse_frontmatter：parse 0 ERROR、validate_entity_id 合法、`_entity_type_from_id=='ORG'`、跨引 C-主角 depends_on 通過。
- registry resolve ORG → `11_organizations/`、`^ORG-.+$`（root+template 鏡像一致）。
- registry-derived ENTITY_ID_RE 接受全 11 型別代表 ID（branch==11）、拒 6 非法（裸 ORG / CH-1 / A-unknownsub…），OUTLINE 收斂 {W-rules,W-language,V,C,R,P,CH}。
- **Falsification（決定性）**：sandbox registry 刪 ORG → `ENTITY_ID_RE.match('ORG-測試')` 翻 None、branch 11→10 ⇒ regex 真 registry-derived。
- 非 org control 零回歸；scratch 已刪、git tree 乾淨。

## 4. 各維結論（一句話）
- **D1 spec-enum**：issues（pre-existing W-style/ORG 列舉殘餘擴散 L3_EXPORT/07_customization/IC/UX_SPEC/UPS；無 critical）→ NEW_REQ_49 尾巴。
- **D2 registry**：clean（DRY 落地、parser 端強制為真；spec-doc 機器強制刻意 park + module-cache 理論邊界皆 INFO）。
- **D3 L2-mechanical**：clean（三腳本全綠；tracked pyc 已清；server.py 第三鏡像 INFO）。
- **D4 xref**：issues→**已修**（ORG skill 索引 drift MAJOR 已回填）。
- **D5 ledger**：clean（v2.9 / §6.25 D-074 + §6.26 D-075 齊全；未動 D-056~D-062；摘要排序 cosmetic）。
- **D6 backcompat**：clean（ORG 純新增、非 ORG 路徑零回歸；C↔C 零變）。
- **D7 phases**：clean（Phase 推進完整、無無聲失敗）。
- **smoke**：clean（4/4 + falsification）。

## 5. 殘餘 backlog（見 wake-up §5 完整清單）
- **本批已修**：ORG skill 三索引回填 / overclaim 措辭軟化 / frontend pyc untrack。
- **NEW_REQ_49 尾巴**：spec-doc REGISTRY-MIRROR marker 全強制 / W-style+ORG 列舉殘餘 sweep（L3_EXPORT/07_customization/IC/UX_SPEC/UPS）/ server.py 第三鏡像 registry-derive。
- **刻意延後**：F8 方向 B / skill-generic / view-org·export-org / 清道夫遷移。
- **非現行 bug**：C-ORG 裸名 ID 碰撞（i4）。

## 6. L3 抽查指引（補 wake-up §6）
1. 親跑 lint：`python scripts/check_entity_type_consistency.py` → exit 0、三 spec-doc INFO、輸出「無 REGISTRY-MIRROR marker 區塊」。決策：marker 是否本輪即補（0/3→3/3）或維持 prose+人工 L1（已軟化 overclaim）。
2. ORG skill 索引：grep `create-org` 於 AGENTS.md / skill_registry_full.md（**現應命中**，drift 已修）。
3. parser 端強制為真：複跑 smoke falsification（刪 ORG → ENTITY_ID_RE 拒 ORG-測試）。
4. W-style/ORG 殘餘留痕：grep `7 entity types`（命中 IC:1311 + UX_SPEC:2617），確認列入 NEW_REQ_49 尾巴。
5. git 衛生：`git ls-files "*.pyc"` → 應為空。

## 7. Cross-ref
- workflow run `wf_f81550df-650`（full result：tasks/wc26wco3f.output）
- Step 2 稽核 `BATCH4_POSTLAND_AUDIT_REPORT.md` / Batch 5 verify `wf_96cca42d-1ca`
- DECISIONS_LOG §6.25 D-074 + §6.26 D-075 / POST_LOCK NEW_REQ_49 / `OVERNIGHT_WAKEUP_REPORT.md`
