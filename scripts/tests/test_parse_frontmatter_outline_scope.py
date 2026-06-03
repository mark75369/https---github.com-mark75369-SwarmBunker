#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch 5 / NEW_REQ_49 — P3-OUTLINE_ENTITY_TYPES regression test.

P3 target: OUTLINE_ENTITY_TYPES + _record_matches_outline_scope() in
scripts/parse_frontmatter.py. The hardcoded set {W-rules, W-language, V, C, R,
P, CH} was a deliberate *curated narrative-outline subset* (NOT a full registry
mirror): it intentionally EXCLUDES W-style / S / A / ORG. The Batch 5 refactor
keeps that curated membership (via _OUTLINE_ENTITY_TYPE_ALLOWLIST) but intersects
it with the registry's valid types so a registry rename/removal is caught instead
of silently lingering.

REGRESSION RED LINE (must stay byte-identical):
  1. OUTLINE_ENTITY_TYPES == the original literal 7-element set.
  2. W-style / S / A / ORG remain EXCLUDED from outline scope (no /view-outline
     scope expansion = no regression).
  3. _record_matches_outline_scope() matches iff a record's `entities` contains
     at least one outline-scope type, exactly as before.

Pure test; writes no repo file.
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import parse_frontmatter as pf  # noqa: E402
from parse_frontmatter import (  # noqa: E402
    EntityRecord,
    _entity_type_from_id,
    _record_matches_outline_scope,
    load_entity_type_registry,
)

# The exact pre-refactor hardcoded set. This literal is the regression oracle and
# must NOT be sourced from the module under test.
_ORIGINAL_OUTLINE_SET = {"W-rules", "W-language", "V", "C", "R", "P", "CH"}
_DELIBERATELY_EXCLUDED = {"W-style", "S", "A", "ORG"}


def _record_with_entities(entities):
    return EntityRecord(source_file="t.md", frontmatter={"entities": list(entities)})


def test_outline_entity_types_byte_identical():
    assert set(pf.OUTLINE_ENTITY_TYPES) == _ORIGINAL_OUTLINE_SET, (
        f"OUTLINE_ENTITY_TYPES drifted from the curated subset: "
        f"got {sorted(pf.OUTLINE_ENTITY_TYPES)}"
    )


def test_outline_scope_deliberate_exclusions():
    for excluded in _DELIBERATELY_EXCLUDED:
        assert excluded not in pf.OUTLINE_ENTITY_TYPES, (
            f"{excluded} must stay OUT of outline scope (no /view-outline "
            f"scope expansion = regression red line)"
        )


def test_outline_subset_of_registry_types():
    reg = load_entity_type_registry(REPO_ROOT)
    valid = reg.all_valid_types()
    for t in pf.OUTLINE_ENTITY_TYPES:
        assert t in valid, f"outline type {t} not in registry — drift guard breach"


def test_record_matches_outline_scope_positive():
    # Each in-scope type, alone, must put a record in outline scope.
    for in_scope_id in ["W-rules", "W-language", "V", "C-foo", "R-a-b", "P", "CH-01"]:
        rec = _record_with_entities([in_scope_id])
        assert _record_matches_outline_scope(rec), f"{in_scope_id} should be outline scope"


def test_record_matches_outline_scope_negative():
    # Excluded types, alone, must NOT put a record in outline scope.
    for out_id in ["W-style", "S-01-02", "A-portrait-x-y", "ORG-corp"]:
        rec = _record_with_entities([out_id])
        assert not _record_matches_outline_scope(rec), (
            f"{out_id} must NOT be outline scope (deliberate exclusion)"
        )


def test_record_matches_outline_scope_mixed_and_empty():
    # Mixed: any in-scope member wins.
    rec = _record_with_entities(["ORG-corp", "S-01-02", "C-hero"])
    assert _record_matches_outline_scope(rec), "mixed record with C-* is outline scope"
    # No entities -> not outline scope.
    assert not _record_matches_outline_scope(_record_with_entities([]))
    # Only excluded -> not outline scope.
    assert not _record_matches_outline_scope(_record_with_entities(["A-bg-x-y", "ORG-z"]))


def test_entity_type_from_id_unchanged_for_11_types():
    # Byte-for-byte mapping the curated subset relies on.
    expected = {
        "W-rules": "W-rules",
        "W-language": "W-language",
        "W-style": "W-style",
        "V": "V",
        "P": "P",
        "C-hero": "C",
        "R-a-b": "R",
        "CH-01": "CH",
        "S-01-02": "S",
        "A-portrait-hero-01": "A",
        "ORG-corp": "ORG",
    }
    for entity_id, want in expected.items():
        got = _entity_type_from_id(entity_id)
        assert got == want, f"_entity_type_from_id({entity_id!r}) = {got!r}, want {want!r}"


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
