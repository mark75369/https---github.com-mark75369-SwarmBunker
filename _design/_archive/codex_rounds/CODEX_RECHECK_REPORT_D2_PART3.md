狀態：REVIEW
版本：v0.1
最後更新：2026-05-19
適用範圍：CODEX D2 targeted recheck Part 3（Recheck-02 完整重審 + Recheck-08 NF-D2-01 spot-check）
優先級：高

# CODEX_RECHECK_REPORT_D2_PART3

## 0. 本輪 scope

本輪只處理：

1. Recheck-02 完整重審：QA 5→8 殘留、09_g/h/i 是否全預設必跑、8 份 qa_report_paths / qa_type / weight、FINAL gate 是否 8 QA + 09_e。
2. Recheck-08 spot-check：NF-D2-01 是否已在 REQUIREMENTS_LOCK §6.2 與 DECISIONS_LOG P-019 加 supersede / 細化註記。

不重審 Recheck-01、Recheck-03、Recheck-04、Recheck-05、Recheck-06、Recheck-07、Recheck-09；其 PASS 狀態沿用 Part2 報告。

## 1. 整體判定

**整體 Go/No-Go：NO-GO。**

| 項目 | 判定 |
|---|---|
| Recheck-02 | ✗ FAIL |
| Recheck-08 / NF-D2-01 spot-check | ✓ PASS |

原因：Part2 列出的 Recheck-02 舊失敗點大多已修正，但本輪在必讀範圍 `UPSTREAM_DOWNSTREAM_SPEC.md` §3 全章中發現新的阻斷殘留：09_e 模板對齊清單仍把「必要 QA」寫成 5 項（09_a/b/c/d/f），且沒有標 D-043 supersede。這仍會污染 Phase D `/qa` / 09_e 實作判斷，因此 master 不建議進階段 7 升 LOCKED。

## 2. Files Read

- `_design/REQUIREMENTS_LOCK.md`：§4.1、§6.2（§6.2 僅 spot-check footnote，不審 v1.0 原表）
- `_design/DECISIONS_LOG.md`：P-019、D-043
- `_design/CODEX_RECHECK_REPORT_D2_PART2.md`：Recheck-02、Recheck-08、NF-D2-01、Part2 NO-GO 結論
- `_design/SPEC.md`：§5.4、§12.7、§12.10
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`：§0、§1 intro、§2.5、§2.8、§2.10.1、§2.10.5、§2.10.6、§3 全章目標段、§7 UX-30/35、§8.3、§11.1、Appendix A.6、Appendix B、Appendix C.D.4
- `_design/INTEGRATION_CONTRACTS.md`：Contract A.5、B.5
- `_design/ARCHITECTURE.md`：§6.3、§6.5
- `_design/TASKS.md`：D.4、D.5

## 3. Recheck-02：QA 8 份必跑落地

**判定：✗ FAIL。**

### 3.1 已修正 / 已對齊部分

- REQUIREMENTS_LOCK 的新基準仍是 **8 份 QA + 1 份 final-gating**：`REQUIREMENTS_LOCK.md:163-179`。
- SPEC §5.4 manifest / phase_log 已要求 QA 跑完對應 **8 份 QA 報告**，且 `qa_report_paths` 範例列 8 條：`SPEC.md:416`、`SPEC.md:475-485`。
- SPEC §12.7 明確 `/qa` 必跑 8 份、`qa_decision` 8 份全 PASS 才 PASS、FINAL gate 需 8 QA + 09_e：`SPEC.md:1128-1149`。
- SPEC §12.10 已修正 Part2 的「5+1 / 6 份」殘留，改為 8+1 / 9 份並標 D-043 supersede：`SPEC.md:1187-1192`。
- UD §2.5.3 已改為 8 份必跑，09_g/h/i 不再可選，`qa_report_paths` 列 8 條：`UPSTREAM_DOWNSTREAM_SPEC.md:1957-2030`。
- UD §2.8、§2.10.1、§2.10.5、§2.10.6 已修正 Part2 失敗點，均改成 8 份或標 D-043 supersede：`UPSTREAM_DOWNSTREAM_SPEC.md:2122`、`2209`、`2288-2312`。
- UD §3 開頭與 QA frontmatter 範例已用 8 份 / 0.125 / 8 種 `qa_type`：`UPSTREAM_DOWNSTREAM_SPEC.md:2637-2639`、`2708-2716`。
- UD §3.9.1 / §3.9.6 已明確 09_i 預設必跑、`--scope` 只切換範圍，不是 on/off：`UPSTREAM_DOWNSTREAM_SPEC.md:3435-3437`、`3575-3581`。
- UD Appendix A.6 已是 8 份 QA、`weight: 0.125`、8 種 `qa_type`：`UPSTREAM_DOWNSTREAM_SPEC.md:7077-7101`。
- UD Appendix C.D.4 已要求並行跑 8 份，列出 09_g/h/i，要求 8 份各 0.125、8 種 `qa_type`、8 條 `qa_report_paths`：`UPSTREAM_DOWNSTREAM_SPEC.md:7393-7409`。
- Contract A.5 / B.5 已對齊 8 種 `qa_type`、8 QA 序列、FINAL gate 9 status：`INTEGRATION_CONTRACTS.md:592-620`、`1301-1341`。
- ARCH §6.3 / §6.5 已對齊 8 份、0.125、8 種 `qa_type`、8 條 `qa_report_paths`：`ARCHITECTURE.md:855-888`、`914`。
- TASKS D.4 已要求 8 份全必跑、frontmatter 0.125、8 種 `qa_type`、8 條 `qa_report_paths`、驗收恰好 8 份：`TASKS.md:1562-1629`。

### 3.2 阻斷殘留

**R2-P3-01 [Blocking] UD §3.6.4 仍把 09_e「必要 QA」對齊清單寫成 5 項。**

證據：

- `UPSTREAM_DOWNSTREAM_SPEC.md:3072-3074`：
  - 「§8.1 QA 結果總表的『必要 QA』清單改為 5 項（09_a/b/c/d/f）」
  - 「§8.3.4 ... 改名為『與 09_a/b/c/d/f QA 階段的承接』」

為何阻斷：

- 該段位於本輪必讀的 UD §3 全章，且語氣是「需做以下對齊」，不是歷史註腳。
- 它未標 `v0.4 / D-043 supersede`，也未補 09_g/h/i。
- 上方 §3.6.2 已正確寫 8 份，但 §3.6.4 會直接指導 09_e 模板 §8.1 / §8.3.4 的修補，足以讓 D.4 / D.5 實作回寫成 5 項。

最小修補方向：

- 將 `UPSTREAM_DOWNSTREAM_SPEC.md:3073` 改為 8 項：09_a/b/c/d/f/g/h/i。
- 將 `UPSTREAM_DOWNSTREAM_SPEC.md:3074` 的承接名稱改為 09_a/b/c/d/f/g/h/i，或明確標原 5 項寫法已由 D-043 supersede。

### 3.3 Recheck-02 checklist

| 檢查點 | 判定 | 證據 |
|---|---|---|
| Part2 舊失敗點是否修正 | ✓ | SPEC §12.10、UD §2.8 / §2.10.1 / §2.10.5 / §2.10.6 / Appendix C.D.4 均已修正 |
| `qa_report_paths` 8 條 | ✓ | `SPEC.md:475-485`、`UPSTREAM_DOWNSTREAM_SPEC.md:2021-2030`、`TASKS.md:1608` |
| `qa_type` 8 種 | ✓ | `SPEC.md:1149`、`UPSTREAM_DOWNSTREAM_SPEC.md:7101`、`INTEGRATION_CONTRACTS.md:592-603` |
| `weight` 0.125 | ✓ | `UPSTREAM_DOWNSTREAM_SPEC.md:2708`、`7089`、`TASKS.md:1596`、`ARCHITECTURE.md:875` |
| 09_g/h/i 全預設必跑 | ✓ | `UPSTREAM_DOWNSTREAM_SPEC.md:1959-1972`、`3437`、`3577-3581` |
| FINAL gate 8 QA + 09_e | ✓ | `SPEC.md:1147`、`UPSTREAM_DOWNSTREAM_SPEC.md:2056-2077`、`INTEGRATION_CONTRACTS.md:1339-1341` |
| 所有 5 份 / 五份 QA 描述已改 8 份或標 D-043 supersede | ✗ | `UPSTREAM_DOWNSTREAM_SPEC.md:3073-3074` 仍是未標 supersede 的 5 項必要 QA 指令 |

## 4. Recheck-08 / NF-D2-01 spot-check

**判定：✓ PASS。**

### 4.1 REQUIREMENTS_LOCK §6.2

`REQUIREMENTS_LOCK.md:269` 的 v1.0 原表仍保留 `agent_assisted` 跳 QA / `external_llm` 走完整 QA，符合「不改原 v1.0 lock 表」要求。

表後已新增註腳：`REQUIREMENTS_LOCK.md:272` 明確說明 v1.0 lock 原文保留不動，後續 D-031 + D-038 + CODEX C-08 細化後，`--trust-level` 嚴格限上游 `/create-*`，不影響下游 pipeline；下游永遠走標準 DRAFT → QA → REVIEW → FINAL，兩條 trust-level 路徑下游皆走完整 8 份 QA。

### 4.2 DECISIONS_LOG P-019

`DECISIONS_LOG.md:645` 的 v0.6 舊摘要仍保留 `agent_assisted` 跳 QA / `external_llm` 走完整 QA。

`DECISIONS_LOG.md:646` 已加 v0.8 細化，明確標 v0.6 摘要為舊寫法，真實邊界由 CODEX C-08 + master 第四輪拍板細化：trust-level 嚴格限上游 `/create-*`，不影響下游 pipeline；兩條 trust-level 路徑下游皆走完整 8 份 QA。

### 4.3 NF-D2-01 狀態

NF-D2-01 的加註要求已完成。若只看 Recheck-08 spot-check，minor 不再殘留。

## 5. 結論

**NO-GO。**

Recheck-08 / NF-D2-01 已補註通過，但 Recheck-02 仍有阻斷殘留。升 LOCKED 前至少需修正 `UPSTREAM_DOWNSTREAM_SPEC.md:3073-3074`，再重跑 Recheck-02；若只修這一處，本輪其他 Recheck-02 已對齊項可沿用本報告證據作為下一輪比對基準。

## 6. Source Limitations

- 本輪未重審 Recheck-01、Recheck-03、Recheck-04、Recheck-05、Recheck-06、Recheck-07、Recheck-09。
- REQUIREMENTS_LOCK §6.2 只 spot-check 註腳是否存在；未審 v1.0 原表內容。
- 本輪是 deep-review 報告，不修正文檔內容。
