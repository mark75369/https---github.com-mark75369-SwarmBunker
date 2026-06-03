狀態：REVIEW
版本：v0.1
最後更新：2026-05-19
適用範圍：Phase A.0 / A.0F / Phase A 後段 / Phase B-C-D 開發順序評估
優先級：高

# CODEX_DEV_ORDER_EVALUATION

## §0 摘要

**判定：Caution / 可繼續，但需調整 gate。**

User 當前的 A.0 剩餘排序 `A.0.7 -> A.0.8 -> A.0.4 -> A.0.6 -> A.0.5 -> A.0.9` 是 topologically safe，理由正確：`A.0.4 art_metadata` 明確依賴 `A.0.7 entity_type_registry`。主要風險不在 A.0 重排，而在把 `A.0F.0 ~ A.0F.11` 作為 Phase B 前的完整阻塞 gate。TASKS 與 INTEGRATION_CONTRACTS 都把 A.0F 的完整驗收連到 Phase B 後真實 `C-* / R-* / P / CH-* / S-*` 資料，因此 A.0F 應拆成「A.0 後可做的 scaffold / fixture alpha」與「B.9 後 real-data acceptance」兩段。

最重要 finding：**A.0.9 完成後應先做 master 第五輪整合處理 NEW_REQ_1 / D-047，而不是等 A.0F 或 Phase A 全完成。** `issue_type_registry` 不擋 A.0 parser，但會影響 A.2 / A.3 / A.5 / A.6 以及 Phase B 的 5 個 `/create-*` skill。若太晚處理，Phase A 後段和 Phase B 會出現 hardcode 議題清單的返工。

## §1 完整 dependency graph

### §1.1 Graph Table

定義：

- `A.0` = `A.0.1 ~ A.0.9`
- `Phase A 通過` = `A.11`
- `Phase B 通過` = `B.9`
- `Phase C 通過` = `C.7`

| Task | Declared / normalized dependency | Notes |
|---|---|---|
| A.0.1 | 無 | 已完成 |
| A.0.2 | A.0.1 | 已完成 |
| A.0.3 | A.0.2 | 已完成 |
| A.0.4 | A.0.1 + A.0.7 | User 重排理由成立 |
| A.0.5 | A.0.2 + A.0.4 | 內文 A-* cross-reference 依 art_metadata |
| A.0.6 | A.0.1 + A.0.7 + A.0.8 | 可和 A.0.4 平行，但會碰同一 parser surface |
| A.0.7 | A.0.1 | 可立即繼續 |
| A.0.8 | A.0.1 | 可與 A.0.7 平行 |
| A.0.9 | A.0.1 ~ A.0.8 | A.0 parser/API 收束點 |
| A.1 | 無 | 00_b 通用骨架 |
| A.2 | A.1 | 00_i init protocol |
| A.3 | A.1 | 00_e create-world protocol |
| A.4 | A.0 | 27 模板 frontmatter 補完 |
| A.5 | A.2 + A.0.7 + A.0.8 | /init-project + registry copy |
| A.6 | A.3 | /create-world |
| A.7 | A.0 + A.4 + A.5 | /status |
| A.8 | A.7 | /check-gaps |
| A.9 | A.5 + A.6 + A.7 + A.8 | Wrapper smoke |
| A.10 | A.0 ~ A.9 | Phase A review gate |
| A.11 | A.0 ~ A.10 | Phase A full acceptance |
| A.0F.0 ~ A.0F.10 | A.0 + Phase B | TASKS only gives global dependency, no per-task dependency |
| A.0F.11 | A.0F.0 ~ A.0F.10 | Full frontend acceptance |
| B.0 | Phase A 通過 | 00_l relationship protocol |
| B.1 | Phase A 通過 | 00_f character protocol |
| B.2 | Phase A 通過 | 00_g outline protocol |
| B.3 | Phase A 通過 | 00_h detailed outline protocol |
| B.4 | 無 | 03_characters subdir structure |
| B.5 | B.1 + B.4 | /create-character |
| B.5.5 | B.5 | Character REVIEW gate |
| B.5b | B.0 + B.5 + B.5.5 | /create-relationship |
| B.6 | B.2 | /create-outline |
| B.6.5 | B.6 | Outline REVIEW gate |
| B.7 | B.3 + B.6 + B.6.5 | /create-detailed-outline |
| B.8 | B.0 + B.1 + B.2 + B.3 + B.4 + B.5 + B.5.5 + B.5b + B.6 + B.6.5 + B.7 | Phase B review gate |
| B.9 | B.0 ~ B.8 | Phase B full acceptance |
| C.1 | Phase B 通過 | 00_j iterate protocol |
| C.2 | C.1 | 5 iterate skills |
| C.3 | Phase B 通過 | 4 view skills |
| C.4 | A.0 | DERIVED/APPLIED directory-state test |
| C.5 | C.3 + C.4 | 4 export skills |
| C.5a | A.0.9 + A.0F.x | Phase ownership ambiguous; practically A.0F.8 / frontend export prompt track |
| C.6 | Phase A 通過 | /diagnose + /integrate |
| C.7 | C.1 ~ C.6 | Phase C full acceptance |
| D.0 | Phase A 通過 + Phase B 通過 + A.4 | 00_k protocol; A.4 is redundant but clarifying |
| D.1 | Phase A 通過 | 09_f template |
| D.1a | D.0 + D.1 | 09_g / 09_h / 09_i templates |
| D.2 | D.0 + Phase B 通過 | /scene-task |
| D.2.5 | D.2 | Task REVIEW gate |
| D.3 | D.0 + D.2 + D.2.5 | /dialogue-write |
| D.3.5 | D.3 | Convergence human gate |
| D.4 | D.0 + D.1 + D.1a + D.3 + D.3.5 + A.0.8 | /qa + qa_type_registry |
| D.5 | D.1 ~ D.4 | README update |
| D.6 | D.5 | Create Instance repo |
| D.6.5 | D.0 + D.4 | Canon Delta framework note; maturity track |
| D.7 | D.0 ~ D.6 | Phase D full acceptance; D.6.5 not a hard blocker if treated as post-D maturity note |

### §1.2 Cycle / Missed / Dead Dependency Findings

**Cycle check：no hard cycle** in declared TASKS dependency graph.

Potential conceptual cycle:

- `A.0.2` validation text mentions `portrait/bgm` cross-checking `art_metadata` and `source_keys` cross-checking all keys.
- `A.0.3` depends on `A.0.2`; `A.0.4` depends on `A.0.7`.
- If those cross-checks are treated as hard A.0.2 acceptance, a conceptual cycle appears.
- Safe interpretation: `A.0.2` provides parser hooks; `A.0.3` and `A.0.4` later enable cross-repo validation. Current `scripts/parse_frontmatter.py` already follows this optional hook pattern via `art_metadata_index` and `all_keys_set`.

Missed / ambiguous dependencies:

| Finding | Impact | Recommendation |
|---|---|---|
| A.0F.0 ~ A.0F.10 lack per-task dependency sections | Cannot precisely tell which frontend tasks can safely start before Phase B | Split A.0F into alpha vs real-data acceptance |
| A.0F global dependency includes Phase B, but user plan puts full A.0F before Phase B | Unsafe if interpreted as full A.0F.11 acceptance | Do not block Phase B on full A.0F |
| C.5a lives under Phase C but says it belongs to A.0F frontend task group | Ownership ambiguity | Treat as covered by A.0F.8 / Export Prompt track; C.7 should not depend on it unless TASKS is patched |
| A.0.4 voice `dialogue_keys_ref` validation benefits from A.0.3 KEY index | Not declared as hard dependency | Keep as validation-enhancing dependency or defer strict validation to A.0.9 integration |
| D.7 does not depend on D.6.5 | Fine if D.6.5 is post-D maturity note; ambiguous if user expects it in D delivery | Keep D.6.5 outside hard D.7 gate unless user reclassifies it |

Dead / over-broad dependencies:

| Candidate | Reason |
|---|---|
| A.4 depends whole A.0 | Conservative. A.4 likely does not need A.0.9 JSON API, but waiting for all parser work is safer |
| A.0F global depends Phase B | Correct for real-data acceptance; over-broad for static skeleton, build, and fixture work |
| D.0 includes A.4 while depending Phase A | Redundant because Phase A already includes A.4 |
| D.4 includes A.0.8 while depending earlier phases | Redundant but useful because /qa directly consumes qa_type_registry |

### §1.3 Critical Path

Current critical path is not a single linear chain through every task. The practical bottleneck is:

`A.0.7 / A.0.8 registry -> A.0.4 art_metadata + A.0.6 registry enum handling -> A.0.5 cross-reference -> A.0.9 structured API -> master round 5 D-047 -> A.2/A.3/A.5/A.6 -> A.7/A.8/A.9/A.10/A.11 -> Phase B create skills + human gates -> B.9 -> A.0F real-data acceptance / C/D downstream tracks`

The most critical individual tasks:

- `A.0.7` and `A.0.8`: registry foundation.
- `A.0.4`: A-* metadata and asset completeness, feeding parser, frontend, export.
- `A.0.9`: shared structured API for export / frontend.
- `A.0F.1`: 8 endpoint adapter contract.
- `A.0F.6`: LOCKED save guard.
- `D.0 / D.3 / D.4`: downstream pipeline, convergence, and 8-QA execution.

## §2 推薦執行順序

### §2.1 Single CODEX Safe Order

Recommended conservative order for one CODEX conversation:

```text
A.0.7 -> A.0.8 -> A.0.4 -> A.0.6 -> A.0.5 -> A.0.9
  -> master round 5 for NEW_REQ_1 / D-047 (+ NEW_REQ_3 if desired)
  -> A.1 -> A.2 -> A.3 -> A.4 -> A.5 -> A.6 -> A.7 -> A.8 -> A.9 -> A.10 -> A.11
  -> Phase B
  -> A.0F real-data acceptance can run after B.9, with scaffold/fixture work optionally earlier
  -> Phase C
  -> Phase D
```

If user wants minimum disruption to the current plan, the only mandatory correction is:

```text
Do not treat A.0F.11 full acceptance as a Phase B precondition.
Move master round 5 from after Phase A to immediately after A.0.9.
```

### §2.2 Parallel Batches

If multiple CODEX conversations are available, a safe high-level batch plan is:

**A.0 remaining**

| Wave | Tasks |
|---|---|
| 1 | A.0.7 + A.0.8 |
| 2 | A.0.4 + A.0.6 |
| 3 | A.0.5 |
| 4 | A.0.9 |

Note: A.0.4 / A.0.6 / A.0.5 all touch shared parser surface. Parallel design is fine, but code merge should have one integration owner.

**Phase A after A.0 + master round 5**

| Wave | Tasks |
|---|---|
| 1 | A.1 + A.4 |
| 2 | A.2 + A.3 |
| 3 | A.5 + A.6 |
| 4 | A.7 |
| 5 | A.8 |
| 6 | A.9 |
| 7 | A.10 |
| 8 | A.11 |

After D-047, A.2/A.3/A.5/A.6 may need issue registry wording and copy behavior.

**Phase B**

| Wave | Tasks |
|---|---|
| 1 | B.0 + B.1 + B.2 + B.3 + B.4 |
| 2 | B.5 + B.6 |
| 3 | B.5.5 + B.6.5 |
| 4 | B.5b + B.7 |
| 5 | B.8 |
| 6 | B.9 |

If running on the same test Instance, serialize tasks that write `.protocol_version` or the same entity files.

**A.0F**

| Track | Timing | Scope |
|---|---|---|
| A.0F alpha | After A.0.9 | Build/package, static UI, endpoint facade, fixture data, clipboard-only Export panel, basic Save guard tests |
| A.0F real-data acceptance | After B.9 | Dashboard, Scene Queue, Asset Panel, conflict flows, and Export Prompt against actual C/R/P/CH/S data |

**Phase C**

| Wave | Tasks |
|---|---|
| pre | C.4 can run after A.0; C.6 can run after Phase A |
| 1 | C.1 + C.3 |
| 2 | C.2 + C.5 |
| 3 | C.7 |

`C.5a` is better handled as A.0F / Export Prompt track unless TASKS is clarified.

**Phase D**

| Wave | Tasks |
|---|---|
| pre | D.1 can be prepared after Phase A, if governance permits |
| 1 | D.0 |
| 2 | D.1a + D.2 |
| 3 | D.2.5 |
| 4 | D.3 |
| 5 | D.3.5 |
| 6 | D.4 |
| 7 | D.5 |
| 8 | D.6 |
| 9 | D.7 |

D.2 -> D.2.5 -> D.3 -> D.3.5 -> D.4 is a hard line. The 8 QA checks inside D.4 can run in parallel, but output order and summary remain fixed.

### §2.3 Time / Wave Impact

Task-wave estimate only; not wall-clock guarantee:

| Plan | Approx length |
|---|---:|
| User current fully sequential plan | 60-62 task-units |
| Per-phase parallel, but still putting full A.0F before A.1 | 36-38 waves |
| Recommended conservative parallel plan | about 30 waves |
| Aggressive graph-only plan | about 27 waves, but governance risk is higher |

Conservative parallelization can plausibly save about 50 percent of task-wave length, but frontend merge, human REVIEW gates, and test Instance setup will dominate real time.

### §2.4 Difference vs User Current Plan

What stays safe:

- Continuing with `A.0.7 -> A.0.8 -> A.0.4 -> A.0.6 -> A.0.5 -> A.0.9` is OK.
- A.0.7 before A.0.4 is correct.

What should change:

- Move master round 5 to immediately after A.0.9.
- Do not place full `A.0F.11` before Phase B.
- Allow A.0F scaffold after A.0.9, but reserve real-data acceptance until after B.9.
- Treat `C.5a` as frontend/export prompt ownership unless TASKS is patched.

## §3 4 個 sub-eval 摘要

### §3.1 Sub-Eval-1: Dependency Graph

Conclusion: declared TASKS graph has no hard cycle. The main dependency issue is A.0F: global dependency says `A.0 + Phase B`, but user plan puts full A.0F before Phase B. Sub-Eval-1 also identified the A.0.2 optional hook issue, C.5a ownership ambiguity, and D.6.5 non-hard-gate ambiguity.

Impact: user A.0 reorder is safe; user A.0F placement needs gate correction.

### §3.2 Sub-Eval-2: Parallelization

Conclusion: A.0 remaining can compress from 6 sequential tasks to 4 waves. The whole plan can compress from about 60-62 task units to about 30 conservative waves if parallel CODEX rooms are used.

Impact: parallel work is valuable, but shared parser files and frontend Save/conflict flows need single integration ownership.

### §3.3 Sub-Eval-3: Phase Boundary + Master Round 5

Conclusion: A.0F should be split into `fixture alpha` and `real-data acceptance`; Phase B should not be blocked by full A.0F. Master round 5 should occur after A.0.9 and before A.2/A.3/A.5/A.6 / Phase B work.

Impact: this is the strongest reason to adjust user plan now.

### §3.4 Sub-Eval-4: Risk + Rollback

Conclusion: high-risk points are registry schema, A-* metadata strictness, parser YAML capability, A.0F endpoint stability, Save race guard, Export panel scope, Phase D pending items, and late D-047 integration.

Impact: add explicit rollback gates, especially before A.0.4, A.0F.1, A.0F.6, D.4, and Phase B `/create-*` implementation.

## §4 Master round 5 時機建議

Recommendation: **do master round 5 immediately after `A.0.9` completes and before Phase A後段 skill/protocol implementation proceeds beyond A.1.**

Use the real timing label, because the discussion labels are inconsistent:

- Recommended timing = "Phase A.0 9 parser sub-task 全完成後".
- Not recommended = "Phase A.0 + A.0F 全完成後".
- Not recommended = "Phase A 全完成後".
- Not recommended = reactive only.

Reasoning:

| Option | Assessment |
|---|---|
| After A.0.9 | Best. A.0 parser is complete, D-047 can reuse registry patterns, and Phase A/B implementation avoids hardcoded topic lists |
| After A.0 + A.0F | Too late if A.0F is full acceptance, because A.0F itself needs Phase B data and issue registry UI may be affected |
| After Phase A | Too late. A.2 / A.3 / A.5 / A.6 may already encode fixed issue lists |
| Reactive only | Too risky for NEW_REQ_1. Acceptable only for NEW_REQ_3 minor parser warning semantics |

NEW_REQ-specific call:

- `NEW_REQ_1 issue_type_registry`: process in master round 5 after A.0.9.
- `NEW_REQ_2 user manual`: living document; update after each completed phase or stable skill, not a master-blocking gate.
- `NEW_REQ_3 deleted KEY semantics`: can ride with the same master round 5; it is minor and should not block A.0.7-A.0.9.

## §5 Risk + Rollback 對照表

| Risk | Severity | Where it hits | Mitigation / rollback |
|---|---|---|---|
| A.0F full acceptance is scheduled before Phase B data exists | High | A.0F.2-11, Phase B gate | Split A.0F into alpha after A.0.9 and real-data acceptance after B.9 |
| D-047 issue registry is handled too late | High | A.2, A.3, A.5, A.6, Phase B `/create-*` | Move master round 5 to after A.0.9; do not hardcode issue list behavior in Phase B before D-047 |
| Registry schema mismatch, especially A-* 7 subtype vs stale 5 subtype examples | High | A.0.7, A.0.4, A.0F.7, export | Before A.0.4, verify registry templates against DF §5.1a / §7 / §8 and Contract A.3/A.5; if mismatch, stop at A.0.7 and patch through master/POST_LOCK_PENDING |
| A.0.4 makes asset cross-ref too strict too early | Medium-High | dialogue asset workflow, A.0.5, D.3 | Keep missing owner / voice refs as WARN where specs say WARN; reserve ERROR for forbidden fields, reserved subtype, invalid ID, true uniqueness breaks |
| A.0.9 structured API changes after frontend starts | High | A.0F.1, A.0F.8, C.5a | Stabilize a parser facade; if API changes, freeze A.0F.2+ and repair A.0F.1 / A.0.9 integration first |
| Save race guard fails to block latest LOCKED state | Critical | A.0F.6, A.0F.10, SPEC §16 safety | Roll back `POST /save` to read-only or save-as-only until Step 3 header reread test passes |
| Export panel accidentally executes export / skill / subprocess | High | A.0F.8, D-029 alpha, D-038 | Roll back to clipboard-only; keep local LLM POST disabled until Phase B+ lifecycle |
| Parser fallback YAML limitations surface late | Medium | A.4, A.7, C.5, D.4 | Either constrain generated YAML to block style or explicitly add PyYAML dependency when allowed by the relevant task |
| Phase D pending details are deferred too far | High | D.3.5 path B, D.4, 08_a §11.1, mutex | Before D.0/D.4, do a phase gate check; conservative rollback is to disable path B and require converge before QA |
| Shared parser/frontend files are edited by multiple CODEX rooms without integration owner | Medium | A.0.4-A.0.6, A.0F.2-A.0F.10 | Assign disjoint write scopes and one merge owner; run integration tests after each wave |

Worst case:

If A.0F reveals that LOCKED `ARCHITECTURE.md §13` endpoint design is wrong, affected tasks depend on the endpoint family:

- `/api/scene/<id>/header`, `/save`, `/save-as`: affects A.0F.4, A.0F.6, A.0F.10, Contract B.2, SPEC §16.
- `/api/scenes/<id>/versions`, `/keys/<key>/lines`: affects A.0F.3, A.0F.4, KEY details pane, A.0.2/A.0.3 consumer logic.
- `/api/assets...`: affects A.0F.2, A.0F.5, A.0F.7, A.0.4/A.0.5.
- `/api/scope-counts`: affects A.0F.8, A.0.9, C.5a.

Delay estimate:

- Small response shape fix: 0.5-1 day.
- Endpoint naming / missing endpoint fix: 1-2 days plus master patch.
- D-029 alpha or Save race guard principle change: 2-5 days plus ARCH / UX / Contracts sync.
- Parser structured API rework: 3-7 days plus A.0.9 and A.0F.1 integration retest.

## §6 對 user 的具體建議

1. 現在繼續 `A.0.7` 是 OK 的。
2. `A.0.7` 與 `A.0.8` 完成後再進 `A.0.4`，這是安全順序。
3. `A.0.4` 前先核對 registry template 是否完整包含 A-* 7 subtype 與 qa_type 8 core。
4. `A.0.9` 完成後，先開 master round 5 處理 `NEW_REQ_1 / D-047 issue_type_registry`，不要等 A.0F 或 Phase A 全完成。
5. A.0F 改採兩段制：
   - A.0.9 後可做 scaffold / fixture alpha。
   - B.9 後再做 A.0F.11 real-data acceptance。
6. Phase B 不應等待完整 A.0F；Phase B gate 應是 A.11 + master round 5 後更新過的 contract。
7. Phase D 前另做一次 short gate，確認 `08_a §11.1`、D.3.5 path B、mutex / phase_log 策略沒有殘留 pending。
8. `_user_manual/` 可持續跟進，但不應成為 parser / skill 實作阻塞。建議每個 phase 或穩定 skill 完成後更新一次。

### Final Recommendation

**Adopt the current A.0 reorder, but do not adopt the current A.0F placement as written.**

Safe next step:

```text
A.0.7 -> A.0.8 -> A.0.4 -> A.0.6 -> A.0.5 -> A.0.9
```

Then:

```text
master round 5 for D-047 -> Phase A後段 -> Phase B -> A.0F real-data acceptance / Phase C-D tracks
```

This keeps parser foundations stable, prevents Phase B hardcode rework, and avoids declaring frontend complete before the repo has the data the frontend is designed to display.

## 附錄 A：Files Read / Source Limitations

Files read directly by the main evaluation:

- `_design/TASKS.md`
- `_design/INTEGRATION_CONTRACTS.md`
- `_design/ARCHITECTURE.md`
- `_design/SPEC.md`
- `_design/DATA_FORMAT_SPEC.md`
- `_design/UPSTREAM_DOWNSTREAM_SPEC.md`
- `_design/UX_SPEC.md`
- `_design/POST_LOCK_PENDING.md`
- `_design/DECISIONS_LOG.md`
- `_design/PHASE_3_COMPLETION_REPORT.md`
- `_design/REQUIREMENTS_LOCK.md`
- `scripts/parse_frontmatter.py`
- `scripts/check_headers.py`
- `_design/expected_entities.yaml`
- `_design/entity_exempt.yaml`

Sub-evals were read-only and reported their own source limitations. No LOCKED design file was modified. No implementation code was written. No commit or push was performed.
