#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_paths.py - 路徑引用與舊式檔名檢查（clean 版本）

掃描 Markdown 文件，檢查：

1. 舊式檔名引用（例如 00A_*.md, 09A_*.md） -- ERROR。
2. 引用但不存在的內部路徑 -- 依前綴分類為 ERROR / WARNING / INFO。

純讀取 / 純檢查，不寫入任何檔案。預設不執行 git；僅 --changed-only
會以 read-only 方式呼叫 git diff / ls-files 取得變更檔清單。

退出碼:
  0  無 ERROR（warnings/infos OK）；或 error 數 ≤ --baseline
  1  發現 ERROR（且超出 --baseline，若有指定）
  2  內部 / 使用錯誤

使用方式:
  python scripts/check_paths.py                       # 全量掃描
  python scripts/check_paths.py --changed-only        # 只掃相對 HEAD 變更檔
  python scripts/check_paths.py --changed-only --base origin/main
  python scripts/check_paths.py --suppress-template-debt   # 隱藏舊式檔名債（NEW_REQ_9）
  python scripts/check_paths.py --baseline 225        # error ≤ 225 視為通過

  F2 / NEW_REQ_26：上述 flag 讓量產期可快速判斷「本輪是否新增錯誤」，
  不必再手動跑 diff-only grep。

注意：本腳本是從原版清理而來，已移除舊架構的概念（_docs trio / tasks /
_projects / _logs / _source_materials 等）。新架構（含 _design / Instance
bootstrap / skills / view 層）的進階檢查留給 CODEX 在 Phase A-D 補上。
"""

import argparse
import re
import subprocess
import sys
import traceback
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Repo root 從本腳本位置推算：scripts/<this>.py -> repo root
REPO_ROOT = Path(__file__).resolve().parent.parent

# Batch 5 / NEW_REQ_49 — scan scope registry-derived 化。
# 讓 parse_frontmatter（同目錄）可被 import；run as `python scripts/check_paths.py`
# 時 scripts/ 已在 sys.path[0]，此處再加一次以容許其他呼叫時機。
_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

# 非 registry-entity 目錄：協議 / 設計 / QA 三者不是任何型別的 target_dir，
# 但仍屬 check_paths 掃描與「活躍引用應存在」範圍。registry 衍生的 entity
# target_dir（含 10_art_assets / 11_organizations）會 union 進來。
_FIXED_SCAN_DIRS = ["00_protocol", "09_quality_assurance", "_design"]

# Registry 載入失敗時的 fallback（與 F8 Phase 3 前的硬編碼鏡像等價 + 10/11 dir）。
# 真實來源永遠是 entity_type_registry；fallback 僅在 import / parse 失敗時生效。
_FALLBACK_ENTITY_DIRS = [
    "01_world",
    "02_vocabulary",
    "03_characters",
    "04_relationships",
    "05_plot",
    "06_scene_index",
    "07_scene_tasks",
    "08_dialogue_outputs",
    "10_art_assets",
    "11_organizations",
]


def _registry_entity_dirs():
    """從 entity_type_registry core 衍生所有 entity target_dir（去 trailing slash）。

    S 型別 target_dir 是逗號分隔多目錄，需 split。載入 / import 失敗時 fallback
    至 _FALLBACK_ENTITY_DIRS，確保本腳本永不因 registry 問題而崩潰。
    """
    try:
        from parse_frontmatter import load_entity_type_registry
        reg = load_entity_type_registry(REPO_ROOT)
        dirs = []
        for entry in reg.core.values():
            for part in entry.target_dir.split(","):
                d = part.strip().rstrip("/")
                if d and d not in dirs:
                    dirs.append(d)
        if dirs:
            return dirs
    except Exception:
        pass
    return list(_FALLBACK_ENTITY_DIRS)


def _build_scan_scope():
    """單一真實來源：合併 registry entity target_dir + 固定協議/設計/QA 目錄。

    回傳 (active_dirs, active_prefixes, dir_alternation)：
      active_dirs       : 排序後的掃描目錄名清單
      active_prefixes   : 對應的 '<dir>/' tuple（path 分類用）
      dir_alternation   : PATH_RE 用的目錄 alternation（已 re.escape）
    """
    scope = set(_registry_entity_dirs()) | set(_FIXED_SCAN_DIRS)
    active_dirs = sorted(scope)
    active_prefixes = tuple(f"{d}/" for d in active_dirs)
    # alternation：依長度降序避免前綴互吞（純數字/底線/中英目錄名）
    dir_alternation = "|".join(
        re.escape(d) for d in sorted(scope, key=lambda s: (-len(s), s))
    )
    return active_dirs, active_prefixes, dir_alternation


_ACTIVE_DIRS, _ACTIVE_PREFIXES, _DIR_ALT = _build_scan_scope()

# 要掃描 .md 的活躍目錄（registry-derived；含 10_art_assets / 11_organizations）
# 註：_source_materials/（user 原始素材區）天然不在 ACTIVE_DIRS 內，check_paths
# 只走此清單列出的目錄，故不會掃到該素材區；無需在 IGNORE_DIR_NAMES 加 no-op 條目。
ACTIVE_DIRS = _ACTIVE_DIRS

# 要掃描的根層級文件
ACTIVE_ROOT_FILES = ["README.md", "AGENTS.md"]

# 從不掃描的目錄
IGNORE_DIR_NAMES = {
    ".git",
    "archive",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "scripts",
}

# 引用但不存在會被歸為 INFO（已知未來會建立的路徑）
# 10_art_assets/：A 型別 art-asset 目錄，量產晚期才填；現存引用多為 spec 範例
# （主角A 等 placeholder），缺檔不應視為 active ERROR，否則 registry-derived 掃描
# 會讓 baseline error 暴增（Batch 5 NEW_REQ_49 設計裁決：安全可逆預設 → INFO）。
FUTURE_PREFIXES = (
    "_design/",
    "10_art_assets/",
)

# 引用但不存在會被歸為 WARNING（歷史區域，引用可能合法）
HISTORICAL_PREFIXES = (
    "archive/",
)

# 活躍路徑前綴 -- 引用應該在活躍區存在（registry-derived；含 11_organizations）。
# 10_art_assets/ 雖在掃描範圍內，但其缺檔引用走 FUTURE_PREFIXES → INFO（見上），
# classify_path_reference 先判 FUTURE 再判 ACTIVE，故 10_ 不會落入此 ERROR 桶。
ACTIVE_PREFIXES = _ACTIVE_PREFIXES

# 舊式檔名 pattern。匹配如：
#   00A_台詞生產協議.md
#   09A_AI味QA報告模板.md
# 必須有 .md 才算實際檔案引用（非僅討論 pattern 本身）。
OLD_STYLE_RE = re.compile(r"\b0[0-9][A-Ea-e]_\S*?\.md\b")

# 內部路徑引用。必須從已知目錄前綴起頭。
# 目錄 alternation 由 registry-derived scan scope（_DIR_ALT，含 10_art_assets /
# 11_organizations + 00_protocol/_design/09_quality_assurance）+ archive 動態組成，
# 取代 F8 Phase 3 前 '0[0-9]_\w+|11_\w+|archive|_design' 硬編碼鏡像（Batch 5 NEW_REQ_49）。
PATH_RE = re.compile(
    r"(?<![\w/])"  # 前面不可有 word/slash
    r"(?:" + _DIR_ALT + r"|archive)"
    r"/[\w./\-一-鿿]+"
    r"\.(?:md|py|json|yml|yaml|toml|csv)"
    r"\b"
)

# Code fence 標記
FENCE_RE = re.compile(r"^(\s*)(```|~~~)")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_md_files():
    """回傳活躍掃描範圍內所有 .md 檔案（已排序）。"""
    files = []

    for dirname in ACTIVE_DIRS:
        d = REPO_ROOT / dirname
        if not d.exists() or not d.is_dir():
            continue
        for p in d.rglob("*.md"):
            rel = p.relative_to(REPO_ROOT)
            if any(part in IGNORE_DIR_NAMES for part in rel.parts[:-1]):
                continue
            files.append(p)

    for name in ACTIVE_ROOT_FILES:
        p = REPO_ROOT / name
        if p.is_file():
            files.append(p)

    return sorted(set(files))


def iter_non_fenced_lines(lines):
    """產生不在 code fence 內的 (line_num, content)。

    追蹤 ``` 與 ~~~ fence。fence 行本身會被略過。
    """
    in_fence = False
    fence_char = None
    for i, line in enumerate(lines, start=1):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(2)[0]  # ` 或 ~
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif fence_char == marker:
                in_fence = False
                fence_char = None
            continue
        if in_fence:
            continue
        yield i, line


def classify_path_reference(ref):
    """為缺失的路徑引用回傳 (severity, message_prefix)。"""
    if ref.startswith(FUTURE_PREFIXES):
        return "INFO", f"future reference '{ref}' (not yet created)"
    if ref.startswith(HISTORICAL_PREFIXES):
        return "WARN", f"historical reference '{ref}' (does not exist)"
    if ref.startswith(ACTIVE_PREFIXES):
        return "ERROR", f"missing active reference '{ref}'"
    return "WARN", f"unknown path prefix '{ref}'"


def check_old_style(non_fenced_lines):
    issues = []
    seen = set()
    for line_num, content in non_fenced_lines:
        for m in OLD_STYLE_RE.finditer(content):
            ref = m.group()
            key = (line_num, ref)
            if key in seen:
                continue
            seen.add(key)
            issues.append(("ERROR", line_num, f"old-style filename reference '{ref}'"))
    return issues


def check_path_existence(non_fenced_lines):
    issues = []
    seen = set()
    for line_num, content in non_fenced_lines:
        for m in PATH_RE.finditer(content):
            ref = m.group()
            key = (line_num, ref)
            if key in seen:
                continue
            seen.add(key)

            target = REPO_ROOT / ref
            if target.exists():
                continue
            sev, msg = classify_path_reference(ref)
            issues.append((sev, line_num, msg))
    return issues


def scan_file(path):
    """掃描單一檔案。回傳 (severity, line_num, message) 清單。"""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
    except OSError as e:
        return [("ERROR", 0, f"cannot read file: {e}")]

    issues = []

    # NUL byte detection
    nul_count = content.count("\x00")
    if nul_count:
        issues.append(("WARN", 0, f"file contains {nul_count} NUL byte(s)"))

    lines = content.splitlines()
    nfl = list(iter_non_fenced_lines(lines))

    issues.extend(check_old_style(nfl))
    issues.extend(check_path_existence(nfl))

    return issues


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def fmt_severity(sev):
    return f"[{sev:5s}]"


def print_issue(file_path, sev, line_num, msg):
    rel = file_path.relative_to(REPO_ROOT).as_posix()
    loc = f"{rel}:{line_num}" if line_num else rel
    print(f"{fmt_severity(sev)} {loc}: {msg}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="檢查 Markdown 路徑引用與舊式檔名（純讀取）。")
    p.add_argument("--changed-only", action="store_true",
                   help="只掃描相對 --base 有變更（含 untracked）的 .md；read-only git")
    p.add_argument("--base", default="HEAD", metavar="REF",
                   help="--changed-only 的比較基準（預設 HEAD）")
    p.add_argument("--baseline", type=int, default=None, metavar="N",
                   help="可接受的 baseline error 數；error ≤ N 時 exit 0（NEW_REQ_9 既有債）")
    p.add_argument("--suppress-template-debt", action="store_true",
                   help="把舊式檔名引用降級為 INFO、不計入 error（NEW_REQ_9：27 份模板檔的 old-style 引用，共約 190 筆）")
    return p.parse_args(argv)


def get_changed_files(base):
    """回傳相對 base 有變更（含 untracked）的檔案絕對路徑集合；git 失敗回 None。

    以 read-only 方式呼叫 git；core.quotepath=false 確保 CJK 檔名不被引號轉義。
    """
    git_base = ["git", "-C", str(REPO_ROOT), "-c", "core.quotepath=false"]
    try:
        diff = subprocess.run(
            git_base + ["diff", "--name-only", base],
            capture_output=True, text=True, encoding="utf-8")
        if diff.returncode != 0:
            print(f"[ERROR] --changed-only: git diff failed: {diff.stderr.strip()}",
                  file=sys.stderr)
            return None
        untracked = subprocess.run(
            git_base + ["ls-files", "--others", "--exclude-standard"],
            capture_output=True, text=True, encoding="utf-8")
        if untracked.returncode != 0:
            print(f"[ERROR] --changed-only: git ls-files failed: {untracked.stderr.strip()}",
                  file=sys.stderr)
            return None
        names = diff.stdout.splitlines() + untracked.stdout.splitlines()
        return {(REPO_ROOT / n).resolve() for n in names if n.strip()}
    except FileNotFoundError:
        print("[ERROR] --changed-only: git executable not available", file=sys.stderr)
        return None


def main(argv=None):
    args = parse_args(argv)

    if not REPO_ROOT.is_dir():
        print(f"[ERROR] repo root not found: {REPO_ROOT}", file=sys.stderr)
        return 2

    try:
        files = find_md_files()
    except Exception as e:
        print(f"[ERROR] failed to enumerate files: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return 2

    if not files:
        print("[ERROR] no Markdown files found in active scan scope", file=sys.stderr)
        return 2

    if args.changed_only:
        changed = get_changed_files(args.base)
        if changed is None:
            return 2
        files = [p for p in files if p.resolve() in changed]
        if not files:
            print(f"[OK] check_paths: no changed Markdown files vs '{args.base}'")
            return 0

    n_err = n_warn = n_info = 0
    n_suppressed = 0

    for path in files:
        try:
            issues = scan_file(path)
        except Exception as e:
            print(f"[ERROR] scan failure on {path.relative_to(REPO_ROOT).as_posix()}: {e}",
                  file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            n_err += 1
            continue

        for sev, line_num, msg in issues:
            if (args.suppress_template_debt and sev == "ERROR"
                    and msg.startswith("old-style filename reference")):
                # NEW_REQ_9 既有 baseline debt：降級為 INFO，不計入 error
                sev = "INFO"
                n_suppressed += 1
            print_issue(path, sev, line_num, msg)
            if sev == "ERROR":
                n_err += 1
            elif sev == "WARN":
                n_warn += 1
            elif sev == "INFO":
                n_info += 1

    total = n_err + n_warn + n_info
    print()
    if total == 0:
        print(f"[OK] check_paths: scanned {len(files)} files, no issues found")
    else:
        print("Summary:")
        print(f"  files scanned: {len(files)}")
        print(f"  errors:        {n_err}")
        print(f"  warnings:      {n_warn}")
        print(f"  infos:         {n_info}")
        if args.suppress_template_debt:
            print(f"  suppressed (template debt): {n_suppressed}")

    if args.baseline is not None:
        if n_err <= args.baseline:
            print(f"[OK] errors ({n_err}) within baseline ({args.baseline})")
            return 0
        print(f"[FAIL] errors ({n_err}) exceed baseline ({args.baseline})")
        return 1

    return 1 if n_err > 0 else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"[ERROR] unhandled exception: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(2)
