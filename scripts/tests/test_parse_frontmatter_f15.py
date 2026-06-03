#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F15 / NEW_REQ_39 regression test。

裸 '---'（Markdown 水平線 HR）出現在 header 之後、且後文非合法 frontmatter
時，`_find_header_adjacent_yaml` 不應把整檔剩餘內容誤判為「未閉合 YAML block」，
否則下游 `_validate_frontmatter_yaml` 會報假 ERROR。

純測試，不寫入 repo 任何正式檔（僅用 tempfile）。
"""

import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from parse_frontmatter import _find_header_adjacent_yaml, parse_file  # noqa: E402


def test_bare_hr_after_header_not_treated_as_yaml():
    """裸 '---' HR + 非 YAML 內文 + 無閉合 '---' → 應回傳 None。"""
    lines = [
        "# 標題",          # 0
        "",                # 1
        "狀態：DRAFT",      # 2  (1-based line 3)
        "",                # 3
        "---",             # 4  裸 HR
        "",                # 5
        "這是一段普通內文，不是 YAML。",  # 6
        "後面還有更多文字。",            # 7
    ]
    header_lines = {"狀態": 3}
    result = _find_header_adjacent_yaml(lines, header_lines)
    assert result is None, f"expected None for bare HR, got {result!r}"


def test_real_unclosed_frontmatter_still_detected():
    """開 '---' 後接真正 frontmatter 欄位但未閉合 → 仍應偵測為 block（不可誤殺）。"""
    lines = [
        "狀態：DRAFT",          # 0  (1-based line 1)
        "",                    # 1
        "---",                 # 2
        "entities: [W-rules]", # 3
        "depends_on: []",      # 4
    ]
    header_lines = {"狀態": 1}
    result = _find_header_adjacent_yaml(lines, header_lines)
    assert result is not None, "expected unclosed-but-real frontmatter to still be detected"


def test_parse_file_bare_hr_no_spurious_yaml_error():
    """端到端：含裸 HR 的檔不應產生 YAML 相關 ERROR。"""
    content = (
        "# 標題\n\n"
        "狀態：DRAFT\n版本：v0.1\n最後更新：2026-06-02\n適用範圍：測試\n優先級：低\n\n"
        "---\n\n"
        "正文段落，含水平線分隔但非 YAML。\n"
    )
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "sample.md"
        p.write_text(content, encoding="utf-8")
        parsed = parse_file(p, repo_root=Path(td))
        yaml_errors = [
            i for i in parsed.issues
            if i.severity == "ERROR" and "YAML" in i.message
        ]
        assert not yaml_errors, f"unexpected YAML errors: {[i.message for i in yaml_errors]}"


def test_parse_file_bare_hr_with_colon_prose_no_yaml_warn():
    """裸 HR 後接含冒號的 prose（舊行為會把它當 mapping、報缺 entities/depends_on/weight
    三條 WARN）→ 修正後應完全無 YAML-block 相關 issue。"""
    content = (
        "# 標題\n\n"
        "狀態：DRAFT\n版本：v0.1\n最後更新：2026-06-02\n適用範圍：測試\n優先級：低\n\n"
        "---\n\n"
        "Note: this is prose with a colon, not frontmatter.\n"
        "Another line: still prose.\n"
    )
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "sample.md"
        p.write_text(content, encoding="utf-8")
        parsed = parse_file(p, repo_root=Path(td))
        yaml_issues = [
            i for i in parsed.issues
            if ("YAML" in i.message or "entities" in i.message
                or "depends_on" in i.message or "weight" in i.message)
        ]
        assert not yaml_issues, f"unexpected YAML-block issues: {[i.message for i in yaml_issues]}"


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
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run())
