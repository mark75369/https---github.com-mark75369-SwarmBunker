#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 5 / NEW_REQ_49 / D-075 regression — entity 型別鏡像漂移 lint。

守住 check_entity_type_consistency.py 的行為：
  1. 對乾淨 repo（registry 11 core + parser 殘留鏡像皆合法）exit 0、無 ERROR。
  2. REGISTRY-MIRROR marker block 漏列 core 型別 → 偵測為 drift（ERROR）。
  3. marker block 完整列 11 core → 無 drift。
  4. parser 殘留鏡像（OUTLINE_ENTITY_TYPES / ENTITY_ID_RE / _entity_type_from_id）
     的合法性檢查行為（含「殘留集合不存在 → 跳過」的 P1/P2-refactor-ready 分支）。
  5. block token 比對用 word-boundary，'W-style' 不被 'W-rules' / 'V' 誤命中。

純測試，不寫入 repo 任何正式檔（僅在 tmp 目錄構造合成 fixture）。
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import check_entity_type_consistency as lint  # noqa: E402
from parse_frontmatter import load_entity_type_registry  # noqa: E402


EXPECTED_CORE = {
    "W-rules", "W-language", "W-style", "V", "C", "R", "P", "CH", "S", "A", "ORG",
}


def test_registry_core_is_11_types():
    reg = load_entity_type_registry(REPO_ROOT)
    core = set(reg.core.keys())
    assert core == EXPECTED_CORE, f"registry core 應為 11 種，實得 {sorted(core)}"


def test_clean_repo_exit_zero():
    rc = lint.main(["--root", str(REPO_ROOT)])
    assert rc == 0, f"乾淨 repo 應 exit 0，實得 {rc}"


def test_parser_mirrors_no_drift():
    reg = load_entity_type_registry(REPO_ROOT)
    core = set(reg.core.keys())
    issues, _info = lint.check_parser_mirrors(core, reg)
    errs = [m for sev, m in issues if sev == "ERROR"]
    assert not errs, f"parser 殘留鏡像不應 drift，實得: {errs}"


def test_outline_subset_must_be_valid_core():
    # OUTLINE_ENTITY_TYPES 是 curated subset，必須全為 registry core 合法型別。
    import parse_frontmatter as pf
    reg = load_entity_type_registry(REPO_ROOT)
    core = set(reg.core.keys())
    outline = getattr(pf, "OUTLINE_ENTITY_TYPES", set())
    assert set(outline) <= core, (
        f"OUTLINE_ENTITY_TYPES {sorted(outline)} 含非 core 型別: {sorted(set(outline) - core)}")


def test_entity_id_re_accepts_all_core_samples():
    reg = load_entity_type_registry(REPO_ROOT)
    samples = lint._representative_ids_for_core(reg)
    assert set(samples.keys()) == EXPECTED_CORE, "代表性 ID 樣本應覆蓋全 11 core 型別"
    import parse_frontmatter as pf
    for t, sid in samples.items():
        assert pf.ENTITY_ID_RE.match(sid), f"ENTITY_ID_RE 應接受 core 型別 {t} 的代表 ID {sid}"


def test_marker_block_missing_type_is_drift():
    core = set(EXPECTED_CORE)
    body = "鏡像列表：W-rules, W-language, V, C, R, P, CH, S, A, ORG"  # 故意漏 W-style
    listed = lint._types_in_block(body, core)
    assert "W-style" not in listed, "W-style 不在 block → 應被偵測為漏列"
    missing = core - listed
    assert missing == {"W-style"}, f"應只漏 W-style，實得 {sorted(missing)}"


def test_marker_block_complete_no_drift():
    core = set(EXPECTED_CORE)
    body = "W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG"
    listed = lint._types_in_block(body, core)
    assert listed == core, f"完整 block 應列出全 11 core，實得 {sorted(listed)}"


def test_word_boundary_no_false_substring_match():
    core = set(EXPECTED_CORE)
    # 只含 W-rules 與 V，不該誤命中 W-style / W-language（'W-' 前綴子串）。
    body = "只提到 W-rules 與 V 兩種"
    listed = lint._types_in_block(body, core)
    assert listed == {"W-rules", "V"}, f"word-boundary 比對誤命中: {sorted(listed)}"


def test_synthetic_marked_doc_detects_drift(tmp_path):
    # 構造合成 repo：複製 registry template，放一份含漏列 marker 的 .md，跑 check_spec_doc_mirrors。
    reg_dir = tmp_path / "_design" / "registries"
    reg_dir.mkdir(parents=True)
    src = REPO_ROOT / "_design" / "registries" / "entity_type_registry.template.yaml"
    (reg_dir / "entity_type_registry.template.yaml").write_text(
        src.read_text(encoding="utf-8"), encoding="utf-8")

    doc = tmp_path / "mirror_doc.md"
    doc.write_text(
        "前言\n"
        "<!-- REGISTRY-MIRROR: entity-types -->\n"
        "core: W-rules / W-language / V / C / R / P / CH / S / A / ORG\n"  # 漏 W-style
        "<!-- /REGISTRY-MIRROR -->\n"
        "後文\n",
        encoding="utf-8")

    reg = load_entity_type_registry(tmp_path)
    core = set(reg.core.keys())
    issues, _info = lint.check_spec_doc_mirrors(tmp_path, core)
    errs = [m for sev, m in issues if sev == "ERROR"]
    assert any("W-style" in m for m in errs), f"應偵測 marker block 漏列 W-style，實得: {errs}"


def test_synthetic_marked_doc_complete_no_drift(tmp_path):
    reg_dir = tmp_path / "_design" / "registries"
    reg_dir.mkdir(parents=True)
    src = REPO_ROOT / "_design" / "registries" / "entity_type_registry.template.yaml"
    (reg_dir / "entity_type_registry.template.yaml").write_text(
        src.read_text(encoding="utf-8"), encoding="utf-8")

    doc = tmp_path / "mirror_doc.md"
    doc.write_text(
        "<!-- REGISTRY-MIRROR: entity-types -->\n"
        "W-rules / W-language / W-style / V / C / R / P / CH / S / A / ORG\n"
        "<!-- /REGISTRY-MIRROR -->\n",
        encoding="utf-8")

    reg = load_entity_type_registry(tmp_path)
    core = set(reg.core.keys())
    issues, _info = lint.check_spec_doc_mirrors(tmp_path, core)
    errs = [m for sev, m in issues if sev == "ERROR"]
    assert not errs, f"完整 marker block 不應 drift，實得: {errs}"


def _run():
    import tempfile
    tests = [(k, v) for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    failed = 0
    for name, fn in tests:
        try:
            if "tmp_path" in fn.__code__.co_varnames[:fn.__code__.co_argcount]:
                with tempfile.TemporaryDirectory() as td:
                    fn(Path(td))
            else:
                fn()
            print(f"[PASS] {name}")
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {name}: {e}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"[ERROR] {name}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run())
