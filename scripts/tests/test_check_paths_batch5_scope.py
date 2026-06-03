#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 5 / NEW_REQ_49 regression test：check_paths.py scan scope registry-derived 化。

驗證 ACTIVE_DIRS / ACTIVE_PREFIXES / PATH_RE 由 entity_type_registry core 衍生，
取代 F8 Phase 3 前的三處硬編碼鏡像，且：

1. scan scope == registry core target_dir（含 10_art_assets / 11_organizations）
   ∪ 固定協議/設計/QA 目錄（00_protocol / 09_quality_assurance / _design）。
2. ACTIVE_PREFIXES 與 ACTIVE_DIRS 嚴格對齊（每個 dir 有對應 '<dir>/' prefix）。
3. PATH_RE 能匹配 registry-derived 目錄路徑（10_ / 11_ 泛化驗證 — 取代舊
   '0[0-9]_|11_' special-case）。
4. 10_art_assets/ 缺檔引用分類為 INFO（FUTURE），非 ERROR — 防 baseline error 暴增。
5. 既有型別目錄分類行為不變（01_world 缺檔 → ERROR；archive → WARN；_design → INFO）。
6. registry 載入失敗時 fallback 仍含 10/11 dir，腳本不崩潰。

純測試；不寫入 repo 正式檔。
"""

import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import check_paths as cp  # noqa: E402
from parse_frontmatter import load_entity_type_registry  # noqa: E402


def _registry_derived_scope():
    reg = load_entity_type_registry(REPO_ROOT)
    dirs = set()
    for entry in reg.core.values():
        for part in entry.target_dir.split(","):
            d = part.strip().rstrip("/")
            if d:
                dirs.add(d)
    return dirs | set(cp._FIXED_SCAN_DIRS)


def test_active_dirs_match_registry_derived_scope():
    expected = _registry_derived_scope()
    assert set(cp.ACTIVE_DIRS) == expected, (
        f"ACTIVE_DIRS 應 == registry-derived scope\n"
        f"  got:     {sorted(cp.ACTIVE_DIRS)}\n"
        f"  expected:{sorted(expected)}")


def test_10_and_11_present():
    for d in ("10_art_assets", "11_organizations"):
        assert d in cp.ACTIVE_DIRS, f"{d} 應在 ACTIVE_DIRS"
        assert f"{d}/" in cp.ACTIVE_PREFIXES, f"{d}/ 應在 ACTIVE_PREFIXES"


def test_active_prefixes_align_with_dirs():
    assert cp.ACTIVE_PREFIXES == tuple(f"{d}/" for d in cp.ACTIVE_DIRS)


def test_fixed_protocol_design_qa_retained():
    for d in ("00_protocol", "09_quality_assurance", "_design"):
        assert d in cp.ACTIVE_DIRS, f"非 entity 目錄 {d} 應保留於 scan scope"


def test_path_re_matches_registry_dirs():
    # 10_ / 11_ 泛化：取代舊 '0[0-9]_|11_' special-case
    samples = [
        "10_art_assets/portraits/主角A.md",
        "11_organizations/ORG-foo.md",
        "01_world/W-rules.md",
        "00_protocol/00_a.md",
        "_design/SPEC.md",
        "archive/補丁.md",
    ]
    for s in samples:
        assert cp.PATH_RE.search(s), f"PATH_RE 應匹配 {s}"


def test_10_art_assets_missing_is_info_not_error():
    sev, _msg = cp.classify_path_reference("10_art_assets/portraits/主角A.md")
    assert sev == "INFO", f"10_art_assets 缺檔應分類 INFO（防 baseline 暴增），got {sev}"


def test_existing_classification_unchanged():
    assert cp.classify_path_reference("01_world/nope.md")[0] == "ERROR"
    assert cp.classify_path_reference("11_organizations/ORG-nope.md")[0] == "ERROR"
    assert cp.classify_path_reference("archive/x.md")[0] == "WARN"
    assert cp.classify_path_reference("_design/nope.md")[0] == "INFO"


def test_registry_failure_fallback():
    import parse_frontmatter as pf
    orig = pf.load_entity_type_registry
    try:
        def boom(*a, **k):
            raise RuntimeError("simulated registry failure")
        pf.load_entity_type_registry = boom
        dirs = cp._registry_entity_dirs()
    finally:
        pf.load_entity_type_registry = orig
    assert "10_art_assets" in dirs and "11_organizations" in dirs, (
        "fallback dirs 應含 10/11，registry 失敗時腳本不得遺漏掃描範圍")


def _main():
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"[PASS] {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"[FAIL] {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_main())
