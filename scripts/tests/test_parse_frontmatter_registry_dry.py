#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NEW_REQ_49 / P1-ENTITY_ID_RE regression test — registry-derived parser constants.

Batch 5 registry DRY 重構：parse_frontmatter 的 ENTITY_ID_RE / _entity_type_from_id /
OUTLINE_ENTITY_TYPES 改為從 load_entity_type_registry() 動態建構，移除第二份硬編碼鏡像。

本測試守住既有 11 型別（W-rules / W-language / W-style / V / C / R / P / CH / S / A /
ORG）的驗證行為逐字不變，並證明：
  1. ENTITY_ID_RE 由 registry id_pattern 衍生（drift-proof）：接受 11 型別合法 ID、
     拒絕殘形；且現在與 registry 權威 pattern 對齊（CH-\\d{2} / S registry pattern /
     A subtype enum），不再用舊鬆散鏡像。
  2. _entity_type_from_id 對 11 型別逐字回正確型別名（W-style 回 'W-style' 非 'W'；
     ORG-* 回 'ORG'；未知前綴回前綴本身）。
  3. OUTLINE_ENTITY_TYPES 仍為策展窄子集（不含 W-style / S / A / ORG），且每個成員
     都存在於 registry（registry-intersected，不會留下被移除的型別）。
  4. ENTITY_ID_RE 與 validate_entity_id（registry 權威 validator）對 11 型別一致。

純測試，不寫入 repo 任何正式檔。
"""

import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import parse_frontmatter as pf  # noqa: E402
from parse_frontmatter import (  # noqa: E402
    ENTITY_ID_RE,
    OUTLINE_ENTITY_TYPES,
    _entity_type_from_id,
    load_entity_type_registry,
    validate_entity_id,
)

# Canonical legal IDs for each of the 11 core types (one representative each, plus
# a couple of S / CH / A variants the registry pattern allows).
LEGAL_IDS = [
    "W-rules",
    "W-language",
    "W-style",
    "V",
    "C-林",
    "C-alice",
    "R-林-王",
    "P",
    "CH-01",
    "CH-12",
    "S-01-02",
    "S-01-02a",
    "S-01-02sub",
    "A-portrait-林-happy",
    "A-bg-街道-night",
    "ORG-清道夫",
    "ORG-scavenger_corp",
]

# Malformed / residual IDs every layer must reject.
ILLEGAL_IDS = [
    "ORG-",
    "ORG",
    "W",
    "C",
    "R-林",
    "Z-foo",
    "CH-1",       # drift case: single-digit CH (registry requires \d{2})
    "CH-123",
    "S-1-2",      # drift case: single-digit S segments
    "S-01-02A",   # drift case: uppercase suffix (registry allows [a-z]+ / sub)
    "A-icon-x-y",  # reserved subtype, not in allowed enum
]

EXPECTED_TYPE = {
    "W-rules": "W-rules",
    "W-language": "W-language",
    "W-style": "W-style",
    "V": "V",
    "C-林": "C",
    "R-林-王": "R",
    "P": "P",
    "CH-01": "CH",
    "S-01-02": "S",
    "A-portrait-林-happy": "A",
    "ORG-清道夫": "ORG",
}

OUTLINE_EXPECTED = {"W-rules", "W-language", "V", "C", "R", "P", "CH"}


def test_entity_id_re_accepts_all_legal_ids():
    for entity_id in LEGAL_IDS:
        assert ENTITY_ID_RE.match(entity_id), f"{entity_id} 應被 ENTITY_ID_RE 接受"


def test_entity_id_re_rejects_illegal_ids():
    for entity_id in ILLEGAL_IDS:
        assert not ENTITY_ID_RE.match(entity_id), f"{entity_id} 不應被 ENTITY_ID_RE 接受"


def test_entity_id_re_is_registry_derived_not_hardcoded():
    """ENTITY_ID_RE 每個 branch 必須對應 registry 的某個 id_pattern（無第二份硬編碼）。"""
    reg = load_entity_type_registry(REPO_ROOT)
    patterns = {e.id_pattern for e in reg.core.values()} | {
        e.id_pattern for e in reg.user_extensions.values()
    }
    # registry CH / S / A 權威 pattern 應已被吸收（drift 已修）。
    assert r"^CH-\d{2}$" in patterns
    assert any(p.startswith("^S-") and r"\d{2}" in p for p in patterns)
    # 舊硬編碼的鬆散 CH-\d{1,2} 不應再出現在 ENTITY_ID_RE。
    assert r"\d{1,2}" not in ENTITY_ID_RE.pattern, "ENTITY_ID_RE 仍含舊鬆散 CH/S 鏡像"


def test_entity_type_from_id_verbatim():
    for entity_id, expected in EXPECTED_TYPE.items():
        assert _entity_type_from_id(entity_id) == expected, (
            f"{entity_id} 型別應為 {expected}"
        )
    # 未知前綴 fallback 行為不變。
    assert _entity_type_from_id("Z-unknown") == "Z"


def test_outline_entity_types_curated_subset_and_registry_valid():
    assert set(OUTLINE_ENTITY_TYPES) == OUTLINE_EXPECTED, (
        "OUTLINE_ENTITY_TYPES 應維持策展窄子集（不含 W-style/S/A/ORG）"
    )
    reg = load_entity_type_registry(REPO_ROOT)
    valid = reg.all_valid_types()
    for t in OUTLINE_ENTITY_TYPES:
        assert t in valid, f"outline 型別 {t} 必須存在於 registry"


def test_entity_id_re_consistent_with_validate_entity_id():
    """對 11 型別合法 ID，pre-filter 與 registry 權威 validator 一致 (都 pass)。"""
    reg = load_entity_type_registry(REPO_ROOT)
    for entity_id in LEGAL_IDS:
        assert ENTITY_ID_RE.match(entity_id)
        assert validate_entity_id(entity_id, reg) is None, (
            f"{entity_id} 應通過 validate_entity_id"
        )
    # 對 registry 拒絕的 drift 殘形，pre-filter 也應拒絕（不放行）。
    for entity_id in ("CH-1", "S-1-2", "A-icon-x-y"):
        assert validate_entity_id(entity_id, reg) is not None
        assert not ENTITY_ID_RE.match(entity_id)


def test_derived_constants_are_cached_and_resettable():
    """二次存取回同一物件（module-cached），reset hook 後重建。"""
    first = pf.ENTITY_ID_RE
    second = pf.ENTITY_ID_RE
    assert first is second, "ENTITY_ID_RE 應為 module-cached 同一物件"
    pf._reset_registry_derived_cache()
    third = pf.ENTITY_ID_RE
    assert isinstance(third, re.Pattern)
    # reset 後仍接受合法 ID。
    assert third.match("ORG-清道夫")


def _run():
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
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"[ERROR] {t.__name__}: {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run())
