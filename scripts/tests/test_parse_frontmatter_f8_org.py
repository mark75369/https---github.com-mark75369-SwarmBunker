#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F8 / NEW_REQ_32 + D-071 regression test — ORG-* core entity type。

Phase 1 落地新 core 型別 ORG-*（組織 / 非人格反派 / 組織型對抗源）。
本測試守住：
  1. ENTITY_ID_RE 接受 ORG-<name>，且順手修復的 W-style 亦被接受（NEW_REQ_47 drift）。
  2. _entity_type_from_id 對 ORG-* 回 "ORG"（走 fallback）、對 W-style 回 "W-style"。
  3. registry（root + template）含 ORG core 條目，屬性正確（^ORG-.+$ / 11_organizations/ / locked）。
  4. validate_entity_id 對 ORG-清道夫 通過、對 ORG-（空名）報格式錯。

純測試，不寫入 repo 任何正式檔。
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from parse_frontmatter import (  # noqa: E402
    ENTITY_ID_RE,
    _entity_type_from_id,
    _resolve_entity_type_entry,
    load_entity_type_registry,
    validate_entity_id,
)


def test_entity_id_re_accepts_org_and_wstyle():
    assert ENTITY_ID_RE.match("ORG-清道夫"), "ORG-<name> 應被 ENTITY_ID_RE 接受"
    assert ENTITY_ID_RE.match("ORG-scavenger_corp"), "ORG-<ascii> 應被接受"
    assert ENTITY_ID_RE.match("W-style"), "W-style 應被接受（修復 NEW_REQ_47 drift）"
    assert not ENTITY_ID_RE.match("ORG-"), "ORG-（空名）不應通過"
    assert not ENTITY_ID_RE.match("ORG"), "裸 ORG（無 hyphen）不應通過"


def test_entity_type_from_id_org_and_wstyle():
    assert _entity_type_from_id("ORG-清道夫") == "ORG", "ORG-* 應對應型別 ORG"
    assert _entity_type_from_id("W-style") == "W-style", "W-style 應回完整型別名（非 'W'）"


def test_registry_has_org_core_type():
    reg = load_entity_type_registry(REPO_ROOT)
    type_name, entry = _resolve_entity_type_entry("ORG-清道夫", reg)
    assert entry is not None, f"ORG 型別應存在於 registry core（resolved type={type_name}）"
    assert entry.type == "ORG"
    assert entry.target_dir == "11_organizations/"
    assert entry.locked is True
    assert entry.id_pattern_compiled.match("ORG-清道夫")


def test_validate_entity_id_org():
    reg = load_entity_type_registry(REPO_ROOT)
    assert validate_entity_id("ORG-清道夫", reg) is None, "ORG-清道夫 應為合法 entity ID"
    bad = validate_entity_id("ORG-", reg)
    assert bad is not None and bad.severity == "ERROR", "ORG-（空名）應報格式 ERROR"


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
