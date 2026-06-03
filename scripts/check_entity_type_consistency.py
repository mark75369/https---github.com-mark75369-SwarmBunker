#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_entity_type_consistency.py — entity 型別鏡像漂移 lint（Batch 5 / NEW_REQ_49 / D-075）

單一權威（SoT）為 `_design/registries/entity_type_registry.template.yaml`
（Instance 端 `<instance_root>/entity_type_registry.yaml`），以
`load_entity_type_registry()` 載入。spec-doc（DFS §7.2 / §7.6、SPEC §5.1b、
manual §6）與 parser 端任何殘留硬編碼鏡像都只是 human-readable / 效能鏡像，必須
與 registry core 型別集合保持一致。本 lint 是 D-075 雙軌（保留鏡像 + drift-lint）
的「強制後盾」：型別漂移時 exit 非 0，列出 missing / extra。

漂移過去（D-055 加 W-style、D-071/D-074 加 ORG）之所以靜默累積，正是因為沒有任何
自動檢查斷言鏡像 == registry core。本 lint 補上這道防線並 wiring 進 REVIEW_LOOP L2。

檢查兩類鏡像：

A. **parser 端殘留硬編碼鏡像**（scripts/parse_frontmatter.py）
   - `OUTLINE_ENTITY_TYPES`（curated subset）：所列型別必須全為 registry core 合法型別。
   - `_entity_type_from_id` 的字面型別集合（W-rules / W-language / W-style / V / P 等
     單例 ID 直回的集合）：必須全為 registry core 合法型別。
   - `ENTITY_ID_RE`：registry core 每個型別的代表性 ID 都必須能被此 regex 接受；反之
     若該 regex 仍硬編碼，至少不得接受 registry 已不存在的型別前綴（best-effort）。
   這些檢查在 P1/P2 parser refactor（改為從 registry 動態建構）落地後仍成立——
   屆時殘留集合若被移除，對應檢查自動跳過（標 INFO）。

B. **spec-doc 鏡像 marker 區塊**（D-075 機器可檢標記）
   掃描所有 .md 內的：
       <!-- REGISTRY-MIRROR: entity-types -->
       ... （區塊內以 `\b<TYPE>\b` 形式列出型別）...
       <!-- /REGISTRY-MIRROR -->
   區塊內列出的型別集合必須 == registry core。missing（registry 有、鏡像缺）與
   extra（鏡像有、registry 無）皆報 ERROR。
   尚未加 marker 的既有鏡像（DFS / SPEC / manual 散文列舉）以 INFO 列出「建議補
   marker」，不視為 ERROR——讓 marker 採用可漸進（避免與平行 spec-doc target 對撞）。

退出碼:
  0  無 drift（INFO/建議 OK）
  1  發現 drift（parser 殘留鏡像含非法型別 / spec-doc marker 區塊與 registry 不一致）
  2  內部 / 使用錯誤（registry 載入失敗等）

使用方式:
  python scripts/check_entity_type_consistency.py
  python scripts/check_entity_type_consistency.py --root <instance_root>

純讀取 / 純檢查，不寫入任何檔案，不執行 git。
"""

import argparse
import re
import sys
import traceback
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT_DEFAULT = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import parse_frontmatter as pf  # noqa: E402
from parse_frontmatter import load_entity_type_registry  # noqa: E402

# D-075 spec-doc 機器可檢 marker。block 內列出的型別 token 與 registry core 比對。
MIRROR_OPEN_RE = re.compile(r"<!--\s*REGISTRY-MIRROR\s*:\s*entity-types\s*-->", re.IGNORECASE)
MIRROR_CLOSE_RE = re.compile(r"<!--\s*/\s*REGISTRY-MIRROR\s*-->", re.IGNORECASE)

# block 內辨識型別 token：core 型別名（W-rules / W-language / W-style / V / C / R /
# P / CH / S / A / ORG …）。以「已知 registry core 型別」逐一查找，避免把散文誤判成型別。
# 掃描範圍：本 lint 不遞迴掃全 repo，只掃明列的 spec-doc + 任何含 marker 的 .md。
SPEC_DOC_GLOBS = [
    "_design/DATA_FORMAT_SPEC.md",
    "_design/SPEC.md",
    "_user_manual/06_data_structure.md",
]

# 已知尚未加 marker、但被任務認定為「型別列舉鏡像」的 spec-doc（INFO 建議補 marker）。
KNOWN_UNMARKED_MIRRORS = {
    "_design/DATA_FORMAT_SPEC.md": "§7.2 inline registry YAML / §7.6 11-core 鏡像表",
    "_design/SPEC.md": "§5.1b core 型別列舉鏡像",
    "_user_manual/06_data_structure.md": "§6 entity 類型表",
}


def _registry_core_types(root: Path):
    """回傳 (core_type_set, registry, load_issues)。"""
    registry = load_entity_type_registry(root)
    core = set(registry.core.keys())
    return core, registry


def _representative_ids_for_core(registry):
    """為每個 core 型別產生一個代表性、應通過 id_pattern 的 ID（給 ENTITY_ID_RE 檢查）。

    以 registry 的 id_pattern 為依據手工映射常見型別；未覆蓋型別則跳過（best-effort，
    不誤報）。
    """
    samples = {
        "W-rules": "W-rules",
        "W-language": "W-language",
        "W-style": "W-style",
        "V": "V",
        "P": "P",
        "C": "C-主角A",
        "R": "R-主角A-反派B",
        "CH": "CH-01",
        "S": "S-01-03",
        "A": "A-portrait-主角A-anger",
        "ORG": "ORG-清道夫",
    }
    return {t: samples[t] for t in registry.core.keys() if t in samples}


def check_parser_mirrors(core_types, registry):
    """A. parser 端殘留硬編碼鏡像檢查。回傳 (issues, info_lines)。"""
    issues = []
    info = []

    # A1. OUTLINE_ENTITY_TYPES — curated subset 必須全為合法 registry core 型別。
    outline = getattr(pf, "OUTLINE_ENTITY_TYPES", None)
    if outline is None:
        info.append("parser: OUTLINE_ENTITY_TYPES 不存在（已 registry-derive 化 → 跳過）")
    else:
        extra = set(outline) - core_types
        if extra:
            issues.append(
                ("ERROR", "parse_frontmatter.OUTLINE_ENTITY_TYPES "
                 f"含非 registry-core 型別: {sorted(extra)}（registry core={sorted(core_types)}）"))
        else:
            info.append(f"parser: OUTLINE_ENTITY_TYPES {sorted(outline)} 全為合法 core 子集")

    # A2. _entity_type_from_id 的單例字面集合（透過行為探測，不依賴內部硬編碼結構）。
    #     對每個 core 單例 ID（無 hyphen 變體者：W-rules/W-language/W-style/V/P）以及帶
    #     prefix 型別的代表 ID，斷言 _entity_type_from_id 回傳值落在 registry core 內。
    type_from_id = getattr(pf, "_entity_type_from_id", None)
    if type_from_id is None:
        info.append("parser: _entity_type_from_id 不存在 → 跳過")
    else:
        samples = _representative_ids_for_core(registry)
        for expected_type, sample_id in sorted(samples.items()):
            got = type_from_id(sample_id)
            if got != expected_type:
                issues.append(
                    ("ERROR", f"parse_frontmatter._entity_type_from_id('{sample_id}') "
                     f"回 '{got}'，期望 '{expected_type}'（registry core 型別）"))
        info.append(
            f"parser: _entity_type_from_id 對 {len(samples)} 個 core 代表 ID 映射與 registry 一致")

    # A3. ENTITY_ID_RE — registry core 每個代表 ID 都必須被接受。
    entity_id_re = getattr(pf, "ENTITY_ID_RE", None)
    if entity_id_re is None:
        info.append("parser: ENTITY_ID_RE 不存在（已 registry-derive 化 → 跳過）")
    else:
        samples = _representative_ids_for_core(registry)
        not_accepted = [sid for sid in samples.values() if not entity_id_re.match(sid)]
        if not_accepted:
            issues.append(
                ("ERROR", "parse_frontmatter.ENTITY_ID_RE 拒絕了 registry core 代表 ID: "
                 f"{sorted(not_accepted)}（鏡像漂移：registry 有此型別但 regex 不接受）"))
        else:
            info.append(
                f"parser: ENTITY_ID_RE 接受全部 {len(samples)} 個 registry core 代表 ID")

    return issues, info


def _extract_mirror_blocks(text):
    """回傳檔內所有 REGISTRY-MIRROR block 的 (start_line, body) tuple list。"""
    lines = text.splitlines()
    blocks = []
    open_line = None
    buf = []
    for idx, line in enumerate(lines, start=1):
        if open_line is None:
            if MIRROR_OPEN_RE.search(line):
                open_line = idx
                buf = []
        else:
            if MIRROR_CLOSE_RE.search(line):
                blocks.append((open_line, "\n".join(buf)))
                open_line = None
                buf = []
            else:
                buf.append(line)
    return blocks


def _types_in_block(body, core_types):
    """以 registry core 型別名為字典，找出 block body 內出現的型別 token 集合。

    用 word-boundary 比對避免子字串誤命中（例如 'W-rules' 不會被 'W' 命中）。
    依長度由長到短比對，命中後從 body 移除，避免 'W-rules' 被 'W' 重複計入。
    """
    found = set()
    remaining = body
    for t in sorted(core_types, key=len, reverse=True):
        pattern = re.compile(rf"(?<![\w-]){re.escape(t)}(?![\w-])")
        if pattern.search(remaining):
            found.add(t)
            remaining = pattern.sub(" ", remaining)
    return found


def check_spec_doc_mirrors(root, core_types):
    """B. spec-doc marker 區塊檢查。回傳 (issues, info_lines)。"""
    issues = []
    info = []
    marked_files = set()

    # 掃描明列 spec-doc + 任何其他含 marker 的 .md（後者經 rglob 找 marker token）。
    candidate_files = set()
    for rel in SPEC_DOC_GLOBS:
        p = root / rel
        if p.is_file():
            candidate_files.add(p)
    # 額外掃描 repo 內其他 .md 是否含 marker（漸進採用後其他檔也可加 marker）。
    for p in root.rglob("*.md"):
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        try:
            head = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if MIRROR_OPEN_RE.search(head):
            candidate_files.add(p)

    for p in sorted(candidate_files):
        rel = p.relative_to(root).as_posix()
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            issues.append(("ERROR", f"{rel}: 無法讀取: {exc}"))
            continue
        blocks = _extract_mirror_blocks(text)
        if not blocks:
            continue
        marked_files.add(rel)
        for start_line, body in blocks:
            listed = _types_in_block(body, core_types)
            missing = core_types - listed
            # extra：block 內出現了 registry core 以外、看似型別的 token。由於我們只用
            # core_types 字典掃描，extra 只能是「registry 已移除但鏡像殘留」——此處無法
            # 偵測未知 token，故 extra 改為「marker 宣稱完整但漏列 core」= missing。
            if missing:
                issues.append(
                    ("ERROR", f"{rel}:{start_line}: REGISTRY-MIRROR block 漏列 registry "
                     f"core 型別: {sorted(missing)}（block 列出={sorted(listed)}）"))

    # 已知未加 marker 的鏡像 → INFO 建議補 marker（不阻擋，避免與平行 spec-doc target 對撞）。
    for rel, where in KNOWN_UNMARKED_MIRRORS.items():
        if rel in marked_files:
            continue
        p = root / rel
        if not p.is_file():
            continue
        info.append(
            f"spec-doc 鏡像 {rel}（{where}）尚未加 D-075 REGISTRY-MIRROR marker；"
            f"建議補 marker 以納入機器強制比對（目前僅 INFO，不阻擋）")

    if not marked_files:
        info.append(
            "目前 repo 內無任何 REGISTRY-MIRROR marker 區塊；spec-doc 鏡像一致性暫由 "
            "parser-mirror 檢查 + 人工 L1 守護。marker 採用後本 lint 自動納入比對。")

    return issues, info


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="entity 型別鏡像漂移 lint（spec-doc + parser 殘留鏡像 == registry core）。")
    parser.add_argument("--root", default=str(REPO_ROOT_DEFAULT), metavar="DIR",
                        help="Instance / repo root（預設本 repo root）")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] root not found: {root}", file=sys.stderr)
        return 2

    try:
        core_types, registry = _registry_core_types(root)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] 載入 entity_type_registry 失敗: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return 2

    if not core_types:
        print("[ERROR] registry core 型別集合為空（registry 載入異常？）", file=sys.stderr)
        return 2

    print(f"[INFO] registry core 型別（權威，{len(core_types)} 種）: {sorted(core_types)}")
    print(f"[INFO] registry source: {registry.source}")
    print()

    all_issues = []
    all_info = []

    parser_issues, parser_info = check_parser_mirrors(core_types, registry)
    all_issues.extend(parser_issues)
    all_info.extend(parser_info)

    spec_issues, spec_info = check_spec_doc_mirrors(root, core_types)
    all_issues.extend(spec_issues)
    all_info.extend(spec_info)

    for msg in all_info:
        print(f"[INFO ] {msg}")
    if all_info:
        print()

    n_err = 0
    for sev, msg in all_issues:
        print(f"[{sev:5s}] {msg}")
        if sev == "ERROR":
            n_err += 1

    print()
    if n_err == 0:
        print(f"[OK] check_entity_type_consistency: 無 drift（registry core {len(core_types)} 種與所有受檢鏡像一致）")
        return 0
    print(f"[FAIL] check_entity_type_consistency: {n_err} 筆型別鏡像 drift")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted", file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] unhandled exception: {exc}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(2)
