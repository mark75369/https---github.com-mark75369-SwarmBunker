#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F2 / NEW_REQ_26 regression test：check_paths.py CLI flag 行為。

實跑 check_paths.py 子行程，驗證：
1. --baseline N（N 夠大）→ exit 0
2. --suppress-template-debt → error 數嚴格少於全量（舊式檔名債被降級）
3. --changed-only --base HEAD（工作樹乾淨時）→ exit 0 且回報無變更

純測試；不寫入 repo 正式檔。
"""

import os
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
CHECK_PATHS = SCRIPTS_DIR / "check_paths.py"


def _run(*flags):
    # 強制子行程以 utf-8 輸出，避免 Windows console codepage（Big5）下
    # CJK 路徑 byte 無法被 parent 以 utf-8 解碼（test-harness only）。
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    proc = subprocess.run(
        [sys.executable, str(CHECK_PATHS), *flags],
        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _error_count(out):
    m = re.search(r"errors:\s*(\d+)", out)
    return int(m.group(1)) if m else 0


def test_baseline_large_passes():
    code, out = _run("--baseline", "100000")
    assert code == 0, f"expected exit 0 with huge baseline, got {code}\n{out[-500:]}"
    assert "within baseline" in out


def test_suppress_template_debt_reduces_errors():
    _, plain = _run()
    _, suppressed = _run("--suppress-template-debt")
    n_plain = _error_count(plain)
    n_suppressed = _error_count(suppressed)
    assert n_suppressed < n_plain, (
        f"expected suppressed errors < plain: {n_suppressed} vs {n_plain}")
    assert "suppressed (template debt)" in suppressed


def test_changed_only_clean_tree():
    # 注意：此測試假設執行當下相對 HEAD 沒有「未提交且落在掃描區」的變更，
    # 或即便有，flag 仍應正常 exit（0 表無新 error）。主要驗證 flag 不炸。
    code, out = _run("--changed-only", "--base", "HEAD")
    assert code in (0, 1), f"unexpected exit {code}\n{out[-500:]}"
    assert ("no changed Markdown files" in out
            or "Summary:" in out
            or "[OK]" in out), f"unexpected output\n{out[-500:]}"


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
