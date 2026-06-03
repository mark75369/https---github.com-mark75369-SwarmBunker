狀態：DEPRECATED
版本：v0.1（F8 Phase 3 — ORG-* authoring stack 設計草案；待 master 拍板 D-074。NOTE: 原 design judge panel wf_ac0e3a40 跑 1hr 後僅 1/3 proposal 完成（minimal-mirror）+ API error + user 中斷，judge/synthesis 未跑；本草案 = 主對話依「救回的 minimal-mirror proposal + 本 session 已讀 00_f/00_l/D-050/create-* 料」手寫，非 panel 綜合）
最後更新：2026-06-03
適用範圍：F8 / NEW_REQ_32 Phase 3（ORG-* authoring stack）實作依據 + D-074 拍板紀錄
優先級：高

# D074_DECISION_PACKAGE — F8 Phase 3：ORG-* authoring stack（待拍板）

> **定位：** F8 長線 direction A 的 **Phase 3**（authoring / ingestion 層）。Phase 1（D-071，ORG-* core 型別）+ Phase 2（D-071 後續，gate + /status）已落地 merge。本檔是 Phase 3 的設計草案，**待 master 拍板 D-074 後**才依四層防線分步實作。**本檔不落地任何 LOCKED 改動。**
>
> **provenance（誠實揭露）：** design judge panel `wf_ac0e3a40` 跑 ~1hr 後只有 1/3 proposal（minimal-mirror-00f）完整完成；另 1 撞 API "fetch failed"、1 被 user 中斷；judge + synthesis 未跑。故本草案非 3-proposal panel 綜合，而是主對話用救回的 minimal-mirror proposal + 本 session 已讀的 00_f/00_l/D-050/create-character/create-relationship 料手寫。**因缺對抗評審，open questions（§13）請 master 逐項拍。**

## 1. 推薦設計（一句話）
**以「最小、鏡像既有慣例」為基線**：`00_n_組織創建協議`（mirror `00_l`、**issue-less**）+ `/create-org`（clone create-character 形狀、只寫 `11_organizations/`、無聲線卡）+ ORG-* card 6 段 schema + create-relationship 容許 C↔ORG endpoint + 清道夫 opt-in 遷移；**一個 D-074 收**所有 LOCKED 觸點；分 3a/3b/3c 子步落地。

## 2. ORG-* entity card schema（11_organizations/<name>.md 固定段）
1. **組織本質**（essence）：是什麼組織 / 制度 / 體系；一句話定位。
2. **對抗性質與來源**（antagonism）：為何是對抗源；對抗形式（制度壓迫 / 殘留債務 / 體系慣性…）。
3. **殘留型態**（residual）：以什麼形式存在 / 被引用——文件 / 條文 / 設施 / 流程；是否已破產/解散。
4. **影響範圍**（influence）：影響哪些角色 / 地點 / 主線段。
5. **下游 hooks**（hooks）：交給 /create-outline·/scene-task·/create-relationship 的鉤子（**不含台詞**）。
6. **文件語體 hint**（hint→方向 B）：殘留文件「讀起來」的語體線索（官腔/條文體…）——**僅 hint，方向 B 才正式做 W-language 文件語體卡**。
- frontmatter：`entities: [ORG-<name>]` / `depends_on: [W-rules, …]` / `weight: {}`（預設 1.0）/ 5 欄 header 狀態 DRAFT。

## 3. 00_n_組織創建協議.md（LOCKED-tier 新協議）
- **mirror `00_l_關係創建協議`** 的 5 階段骨架（診斷 → 探索 → 收斂 → 執行寫檔 → 驗證）。
- **issue-less**（不新增 `core.00_n_organization` 至 issue_type_registry）——比照 `/iterate-scene` 不載 issue registry；ORG 的探索用協議內固定提問（如 §2 的 6 段對應問題），避免又動 registry core（省一個 LOCKED 觸點）。〔open Q13-2：是否仍要 issue list〕
- 寫檔邊界：只 `11_organizations/`；嚴禁 00_protocol/ / 03_characters/ / 不建聲線卡。

## 4. /create-org SKILL.md + 中文 wrapper /建立組織
- clone `create-character` SKILL 形狀（5 階段 + 啟動前檢查 + 錯誤呈現四欄）。
- **啟動前檢查**：建議 W-rules 至少 REVIEW（ORG 需世界觀脈絡）；目標須為「非人格組織/制度對抗源」（呼應 create-character gate 選項 3）。
- inputs：W-rules/V context + `_source_materials/`（殘留文件素材）。
- **寫檔邊界：只 `11_organizations/<name>.md`**（D-050 新增 row，見 §5）。
- **must-not**：不建聲線卡、不寫 03_characters/、不進 /dialogue-write 為說話者、不寫 00_protocol/。
- 中文 wrapper `/建立組織` 薄 alias（同既有 wrapper 模式）。

## 5. D-050 子裁決 2 擴充（LOCKED — 需 D-074）
DECISIONS_LOG §6.12 D-050 子裁決 2「/create-* skill 寫檔目錄嚴格限定表」append 一列：
```
| /create-org | 11_organizations/ |
```
- partial supersede D-050（純 append 一列，既有列不動）；走四層防線 + D-074 背書。

## 6. /iterate-org SKILL.md + /迭代組織
- clone `iterate-character`（00_j v0.2 5 階段）；scope 只 `11_organizations/` + phase_log；不寫 00_b。

## 7. create-relationship ORG-endpoint 規則（動 00_l + SKILL；LOCKED 觸點）
- 容許 `R-<C>-<ORG>` / `R-<ORG>-<C>`（一端 C-* 一端 ORG-*；例 C-瑟琳 ↔ ORG-清道夫）。
- **啟動前檢查調整**：原要求「兩個 C-* 至少 REVIEW」→ 改「兩端實體至少 REVIEW，其中**至多一端為 ORG-***」（ORG 端無聲線卡）。
- **no-voice-card 處理**：寫 04_a/04_b 關係矩陣/時間線照舊；但 **ORG 端不寫聲線卡關係段**（ORG 無聲線卡）——只 C 端聲線卡寫關係段。
- 〔open Q13-4：是否本批就動 create-relationship，或 3b 延後〕

## 8. 清道夫 R-* 遷移政策（opt-in，不自動）
- user 已建 `R-清道夫-*`（workaround）。遷移：`/create-org` 建 `ORG-清道夫`（harvest 三個 R 的對抗來源內容）→ 舊 `R-清道夫-*` 標 **DEPRECATED**（不刪、不自動改寫，守 LOCKED #3 + D-054 posture）→ phase_log 記 migration。**全程 opt-in、user 明示才做。**

## 9. 其他更新
- **view**：`/view-world` 在「勢力與組織」段 compose ORG-*；或新 `/view-org`。〔open Q13-5〕
- **export**：`/export-org` → DERIVED `view/組織-<name>.md`。
- **check-gaps**：掃 `11_organizations/`；空/placeholder ORG、懸空 `depends_on:[ORG-*]` 可報。
- **expected_entities.yaml**：加 `create_org` phase（opt-in, repeatable）。
- **ARCH §3.4** skill→協議 map：加 `/create-org → 00_n`。
- 中文 wrappers：/建立組織 /迭代組織（/匯出組織 if export-org）。

## 10. D-074 拍板範圍 + LOCKED 清單
**一個 D-074 umbrella 收**（推薦）。LOCKED 觸點：
1. 新 `00_protocol/00_n_組織創建協議.md`（新 LOCKED 協議）。
2. D-050 子裁決 2 表 append /create-org 列（§5）。
3. create-relationship 00_l ORG-endpoint 規則（§7）——若 3b 同批。
4. （若採 issue list）issue_type_registry append `core.00_n_organization`——**本草案建議不採**（issue-less），則無此觸點。
- SKILL-only（非 LOCKED）：/create-org /iterate-org /export-org SKILL + wrappers + view/check-gaps + expected_entities + ARCH §3.4 註。

## 11. Phase 3 子分步落地（四層防線，各步可獨立 L3）
- **3a core**（必先）：00_n 協議 + /create-org + /iterate-org + ORG card schema + D-050 +row + expected_entities + ARCH §3.4。→ ORG-* 可正式經 skill 建立/迭代。
- **3b endpoint**：create-relationship ORG-endpoint（動 00_l）。
- **3c migration + views**：清道夫遷移 + view-org/export-org/check-gaps awareness。
- 3a 為 floor；3b/3c 可延後或併。

## 12. 工時 + 風險
- 工時：~6-9h（3a ~4h / 3b ~2h / 3c ~2-3h）。
- 風險：3 個 LOCKED 觸點（00_n / D-050 / 00_l）；ORG-* no-voice invariant 不可破；ORG↔ORG 關係是否允許（建議否）；create-relationship 改動需 regression（既有 C↔C 不可壞）。

## 13. 給 master 拍板的開放問題（因 panel 未完整，請逐項拍）

> ✅ **全 7 題已 L3 拍板（2026-06-03，DECISIONS_LOG §6.25 D-074 + §6.27 amendment）：** Q1=**7 段**（加組織結構/層級）/ Q2=**issue-ful**（00_n 讀 issue_type_registry）/ Q3=單一 D-074 / Q4=endpoint 本批 / Q5=view-org DEFERRED / Q6=**禁 ORG↔ORG** / Q7=方向 B DEFERRED。本草案 §13 以下為原始開放題凍結快照（point-in-time）；落地實況以 DECISIONS §6.25/§6.27 為準。

1. **ORG card 段數**：6 段（§2）夠嗎？要加「組織結構/層級」段？
2. **00_n issue-less**（推薦）vs 加 `core.00_n_organization` issue list（多一個 LOCKED registry 觸點）？
3. **一個 D-074** 收全部（推薦）vs 拆多號？
4. **create-relationship ORG-endpoint** 本批做（3b）vs 延後獨立批？
5. **view-org 獨立** vs 併入 view-world？
6. ORG↔ORG 關係允許嗎？（建議否，至多一端 ORG）
7. 方向 B（W-language 文件語體卡）確認**仍延後**、Phase 3 只留 §2.6 hint hook？

## Cross-ref
- F8 設計總包 `D071_DECISION_PACKAGE.md`（Phase 1 + §6 Phase 3 scope）
- DECISIONS_LOG §6.23 D-071（ORG core）+ §6.24（Phase 2）+ §6.12 D-050（子裁決 2 表）+ §6.16 D-053
- POST_LOCK NEW_REQ_32（F8）/ NEW_REQ_47（parser registry-derived）/ NEW_REQ_48（spec-doc drift）
- 00_protocol/00_f / 00_l / 00_j；.claude/skills/create-character / create-relationship / iterate-character
- 號段：D-074（Batch 4 最後預留；本草案建議單一 D-074）
