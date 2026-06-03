#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_headers.py - Frontmatter 完整性檢查（Phase A.0.1）

檢查 00-09 模板與 _design/*.md 的中文 header 五欄位完整性，
並透過 scripts/parse_frontmatter.py 解析 header-adjacent YAML block。

嚴重度:
  - 缺任一中文 header 五欄位:                       ERROR
  - 欄位格式異常:                                    WARNING
  - YAML block 欄位缺漏或 enum 異常:                 WARNING / ERROR（依 parser 規則）
  - 每檔 狀態/版本/最後更新 摘要:                    INFO

純讀取 / 純檢查，不寫入任何檔案，不執行 git。
"""

import sys
import traceback
from pathlib import Path

from parse_frontmatter import (
    load_entity_type_registry,
    parse_file,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


# 非 registry 掃描目錄（協議 / QA / 設計筆記）——這些不是任何實體型別的 target_dir，
# 但仍需 header 稽核，故顯式列出。皆走單層 glob（與既有行為一致）。
NON_REGISTRY_SCAN_DIRS = [
    "00_protocol",
    "09_quality_assurance",
    "_design",
]

# 需要遞迴（**/*.md）的 registry target_dir。其餘 registry 目錄沿用單層 glob，
# 以逐字保留既有 header 稽核範圍（regression 紅線）。
# 10_art_assets/ 的 .md（subtype index.md / 資產卡）位於 <subtype>/ 子層
# （portrait/bg/cg/sfx/bgm/voice/ui），單層 glob 會漏掉，故對此目錄用遞迴。
RECURSIVE_SCAN_DIRS = {
    "10_art_assets",
}


def _registry_scan_dirs():
    """從 entity_type_registry 衍生掃描目錄集合（取代 F8 Phase 3 最小 hardcode）。

    對 core + user_extensions 的每個 target_dir 欄位（可為逗號分隔多目錄，例如 S
    型別的 06_scene_index/, 07_scene_tasks/, 08_dialogue_outputs/）拆解、取頂層
    目錄名。回傳 dir-name 集合（不含尾斜線）。registry 載入失敗時 fallback 至
    template，再不行則回空集合，由 NON_REGISTRY_SCAN_DIRS + 既有目錄兜底。
    """
    dirs: set[str] = set()
    try:
        registry = load_entity_type_registry(REPO_ROOT, fallback_to_template=True)
    except Exception:
        return dirs
    entries = list(registry.core.values()) + list(registry.user_extensions.values())
    for entry in entries:
        for raw in (entry.target_dir or "").split(","):
            item = raw.strip().strip("/")
            if not item:
                continue
            # 只取頂層目錄名（防止 registry 寫成多層路徑時 pattern 失準）。
            top = item.split("/", 1)[0]
            if top:
                dirs.add(top)
    return dirs


def _build_template_patterns():
    """組裝 glob allowlist：registry-derived target_dir + 非 registry 目錄。

    - registry 目錄：除 RECURSIVE_SCAN_DIRS（10_art_assets，.md 在 subtype 子層）
      用 '<dir>/**/*.md' 外，其餘用單層 '<dir>/*.md'（保留既有非遞迴行為）。
    - 非 registry 目錄（00_protocol / 09_quality_assurance / _design）：單層。
    所有目錄皆不含 _source_materials/，故 user 原始素材區天然不被掃到。
    """
    seen: set[str] = set()
    patterns: list[str] = []

    def _add(dirname: str, recursive: bool):
        if dirname in seen:
            return
        seen.add(dirname)
        glob = "/**/*.md" if recursive else "/*.md"
        patterns.append(f"{dirname}{glob}")

    for dirname in sorted(_registry_scan_dirs()):
        _add(dirname, recursive=dirname in RECURSIVE_SCAN_DIRS)
    for dirname in NON_REGISTRY_SCAN_DIRS:
        _add(dirname, recursive=dirname in RECURSIVE_SCAN_DIRS)

    return patterns


TEMPLATE_PATTERNS = _build_template_patterns()


def find_files():
    """回傳 allowlist 比對到的所有檔案（已排序）。"""
    files = []
    for pattern in TEMPLATE_PATTERNS:
        for p in REPO_ROOT.glob(pattern):
            if p.is_file():
                files.append(p)
    return sorted(set(files))


def scan_file(path):
    """掃描單一檔案。回傳 (issues, info_message)。"""
    parsed = parse_file(path, repo_root=REPO_ROOT)

    summary_parts = []
    for key in ("狀態", "版本", "最後更新"):
        value = parsed.header.get(key)
        summary_parts.append(f"{key}={value if value else '<missing>'}")
    info_msg = " | ".join(summary_parts)

    issues = [(issue.severity, issue.line_num, issue.message) for issue in parsed.issues]
    return issues, info_msg


def fmt_severity(sev):
    return f"[{sev:5s}]"


def print_issue(rel_path, sev, line_num, msg):
    loc = f"{rel_path}:{line_num}" if line_num else rel_path
    print(f"{fmt_severity(sev)} {loc}: {msg}")


def main():
    if not REPO_ROOT.is_dir():
        print(f"[ERROR] repo root not found: {REPO_ROOT}", file=sys.stderr)
        return 2

    try:
        files = find_files()
    except Exception as exc:
        print(f"[ERROR] failed to enumerate files: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return 2

    if not files:
        print("[ERROR] no files found via allowlist", file=sys.stderr)
        return 2

    info_lines = []
    issue_blocks = []

    for path in files:
        try:
            issues, info = scan_file(path)
        except Exception as exc:
            issue_blocks.append((path, [("ERROR", 0, f"scan failure: {exc}")]))
            traceback.print_exc(file=sys.stderr)
            continue

        rel = path.relative_to(REPO_ROOT).as_posix()
        if info:
            info_lines.append((rel, info))
        if issues:
            issue_blocks.append((path, issues))

    if info_lines:
        max_path_len = min(60, max(len(rel) for rel, _ in info_lines))
        for rel, info in info_lines:
            print(f"{fmt_severity('INFO')} {rel:<{max_path_len}}: {info}")
        print()

    n_err = n_warn = 0
    n_info = len(info_lines)

    for path, issues in issue_blocks:
        rel = path.relative_to(REPO_ROOT).as_posix()
        for sev, line_num, msg in issues:
            print_issue(rel, sev, line_num, msg)
            if sev == "ERROR":
                n_err += 1
            elif sev == "WARN":
                n_warn += 1

    print()
    if n_err == 0 and n_warn == 0:
        print(f"[OK] check_headers: scanned {len(files)} files, all headers OK (infos: {n_info})")
    else:
        print("Summary:")
        print(f"  files scanned: {len(files)}")
        print(f"  errors:        {n_err}")
        print(f"  warnings:      {n_warn}")
        print(f"  infos:         {n_info}")

    return 1 if n_err > 0 else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        sys.exit(2)
    except Exception as exc:
        print(f"[ERROR] unhandled exception: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(2)
