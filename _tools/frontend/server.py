"""
劇本開發工具 前端 server
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_ROOT = Path(__file__).resolve().parent
STATIC_DIR = FRONTEND_ROOT / "static"

sys.path.insert(0, str(PROJECT_ROOT))
# Batch 6 / NEW_REQ_49：entity 型別判定改用 parser 的 registry-derived 權威函式，
# 取代本檔原本硬編碼的 entity_type_from_id 第三鏡像（曾漏 W-style，與 parser drift）。
from scripts.parse_frontmatter import (  # noqa: E402
    build_repo_index,
    parse_file,
    _entity_type_from_id as entity_type_from_id,
)

app = FastAPI(title="劇本開發工具前端")

HEADER_FIELDS = ("狀態", "版本", "最後更新", "適用範圍", "優先級")
DIALOGUE_ROOT = PROJECT_ROOT / "08_dialogue_outputs"
KEY_COMMENT_RE = re.compile(r"<!--\s*KEY\s*:\s*(.*?)\s*-->")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->")
SCENE_ID_RE = re.compile(r"^S-(?P<chapter>\d{2})-(?P<scene>\d{2})(?P<suffix>[A-Za-z]+|sub)?$")
PATH_SCENE_RE = re.compile(r"CH(?P<chapter>\d{2})_S(?P<scene>\d{2})(?P<suffix>[A-Za-z]+|sub)?", re.IGNORECASE)
VERSION_RE = re.compile(r"_dialogue_(?P<version>v[0-9][A-Za-z0-9._-]*)$", re.IGNORECASE)


def json_error(status_code: int, message: str) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": message})


def rel_path(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def issue_payload(issue: Any) -> dict[str, Any]:
    return {
        "severity": getattr(issue, "severity", None),
        "line_num": getattr(issue, "line_num", None),
        "message": getattr(issue, "message", str(issue)),
    }


def header_payload(parsed: Any) -> dict[str, str | None]:
    return {field: parsed.header.get(field) for field in HEADER_FIELDS}


def scene_file_token(scene_id: str) -> str | None:
    match = SCENE_ID_RE.match(scene_id)
    if not match:
        return None
    suffix = match.group("suffix") or ""
    return f"CH{match.group('chapter')}_S{match.group('scene')}{suffix}"


def scene_id_from_path(path: Path) -> str | None:
    match = PATH_SCENE_RE.search(path.as_posix())
    if not match:
        return None
    suffix = match.group("suffix") or ""
    return f"S-{match.group('chapter')}-{match.group('scene')}{suffix}"


def parsed_scene_id(parsed: Any, path: Path) -> str | None:
    yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
    scene_id = yaml_data.get("scene_id")
    if isinstance(scene_id, str) and scene_id:
        return scene_id
    return scene_id_from_path(path)


def scene_matches(path: Path, parsed: Any, scene_id: str) -> bool:
    if parsed_scene_id(parsed, path) == scene_id:
        return True
    token = scene_file_token(scene_id)
    return token is not None and token.lower() in path.stem.lower()


def version_from_path(path: Path) -> str | None:
    match = VERSION_RE.search(path.stem)
    if not match:
        return None
    return match.group("version")


def iter_dialogue_files() -> list[Path]:
    if not DIALOGUE_ROOT.exists():
        return []
    return sorted(path for path in DIALOGUE_ROOT.glob("**/*.md") if path.is_file())


def scene_file_candidates(scene_id: str, *, versioned_only: bool = False) -> list[tuple[Path, Any]]:
    candidates: list[tuple[Path, Any]] = []
    for path in iter_dialogue_files():
        if versioned_only and version_from_path(path) is None:
            continue
        parsed = parse_file(path, repo_root=PROJECT_ROOT)
        if scene_matches(path, parsed, scene_id):
            candidates.append((path, parsed))
    candidates.sort(key=lambda item: item[0].stat().st_mtime, reverse=True)
    return candidates


def resolve_scene_file(scene_id: str) -> tuple[Path, Any] | None:
    candidates = scene_file_candidates(scene_id)
    if not candidates:
        return None
    versioned_candidates = [candidate for candidate in candidates if version_from_path(candidate[0]) is not None]
    return (versioned_candidates or candidates)[0]


def resolve_target_path(scene_id: str, raw_path: str) -> tuple[Path, Any] | None:
    """Validate a client-supplied repo-relative path and return (path, parsed).

    Phase A.0F.patch-P0: front-end Save / Save-as / version-content must supply
    the exact `v.path` that was being edited (repo-relative POSIX). Backend may
    NOT fall back to resolve_scene_file (which picks the latest mtime candidate)
    because a multi-version scene (v01/v02) would then write the wrong version.

    Path validation (reject any path that fails any check):
      1. must be repo-relative, no absolute, no `..` segments
      2. must live under DIALOGUE_ROOT (`08_dialogue_outputs/`)
      3. file must exist
      4. after parsing frontmatter, scene_matches(path, parsed, scene_id) must
         be True (prevents another scene's file from being saved under this id).

    Returns (path, parsed) or None when any check fails (caller should reply
    with 400 / 404 accordingly).
    """
    if not isinstance(raw_path, str) or not raw_path.strip():
        return None
    candidate_rel = raw_path.strip().replace("\\", "/")
    if candidate_rel.startswith("/") or ".." in candidate_rel.split("/"):
        return None
    if not candidate_rel.startswith("08_dialogue_outputs/"):
        return None
    candidate = (PROJECT_ROOT / candidate_rel).resolve()
    try:
        candidate.relative_to(DIALOGUE_ROOT.resolve())
    except (ValueError, RuntimeError):
        return None
    if not candidate.is_file():
        return None
    parsed = parse_file(candidate, repo_root=PROJECT_ROOT)
    if not scene_matches(candidate, parsed, scene_id):
        return None
    return candidate, parsed


async def read_json_object(request: Request) -> dict[str, Any]:
    try:
        payload = await request.json()
    except Exception as exc:  # FastAPI wraps malformed JSON differently by backend.
        raise ValueError(f"invalid JSON body: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("JSON body must be an object")
    return payload


def required_string(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def required_float(payload: dict[str, Any], field: str) -> float:
    value = payload.get(field)
    if not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    return float(value)


def sanitize_suffix(value: Any) -> str:
    if isinstance(value, str) and value.strip():
        suffix = value.strip()
    else:
        suffix = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    suffix = re.sub(r'[<>:"/\\|?*\s]+', "_", suffix)
    suffix = suffix.strip("._")
    return suffix or datetime.now().strftime("%Y-%m-%d_%H%M%S")


def optional_string(payload: dict[str, Any], field: str) -> str | None:
    value = payload.get(field)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    return value


def is_locked(parsed: Any) -> bool:
    return parsed.header.get("狀態") == "LOCKED"


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def _line_body_and_ending(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    if line.endswith("\r"):
        return line[:-1], "\r"
    return line, ""


def _content_newline(content: str) -> str:
    return "\r\n" if "\r\n" in content else "\n"


def _header_line_indices(lines: list[str]) -> dict[str, int]:
    patterns = {
        field: re.compile(rf"^\s*{re.escape(field)}\s*[:：]\s*(.+?)\s*$")
        for field in HEADER_FIELDS
    }
    indices: dict[str, int] = {}
    for idx, line in enumerate(lines[:30]):
        body, _ending = _line_body_and_ending(line)
        for field, pattern in patterns.items():
            if field not in indices and pattern.match(body):
                indices[field] = idx
    return indices


def _replace_header_value(line: str, field: str, value: str) -> str:
    body, ending = _line_body_and_ending(line)
    pattern = re.compile(rf"^(\s*{re.escape(field)}\s*[:：]\s*)(.*?)(\s*)$")
    match = pattern.match(body)
    if not match:
        return line
    return f"{match.group(1)}{value}{match.group(3)}{ending}"


def patch_proposal_status(content: str) -> tuple[str, bool, str | None]:
    lines = content.splitlines(keepends=True)
    indices = _header_line_indices(lines)
    missing = [field for field in HEADER_FIELDS if field not in indices]
    if missing:
        fields = ", ".join(missing)
        return content, False, f"frontmatter header missing required fields: {fields}; status patch skipped"

    status_idx = indices["狀態"]
    body, _ending = _line_body_and_ending(lines[status_idx])
    match = re.match(r"^\s*狀態\s*[:：]\s*(.+?)\s*$", body)
    if match and match.group(1).strip() == "DRAFT":
        return content, False, None

    lines[status_idx] = _replace_header_value(lines[status_idx], "狀態", "DRAFT")
    return "".join(lines), True, None


def _yaml_block_bounds(lines: list[str], header_indices: dict[str, int]) -> tuple[int, int] | None:
    missing = [field for field in HEADER_FIELDS if field not in header_indices]
    if missing:
        return None

    idx = max(header_indices.values()) + 1
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx >= len(lines) or lines[idx].strip() != "---":
        return None

    end_idx = idx + 1
    while end_idx < len(lines):
        if lines[end_idx].strip() == "---":
            return idx, end_idx
        end_idx += 1
    return idx, len(lines)


def _yaml_scalar(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_./-]+", value):
        return value
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def patch_frontmatter_field(content: str, field: str, value: str) -> tuple[str, bool, bool]:
    lines = content.splitlines(keepends=True)
    header_indices = _header_line_indices(lines)
    bounds = _yaml_block_bounds(lines, header_indices)
    if bounds is None:
        return content, False, False

    _start_idx, end_idx = bounds
    scalar = _yaml_scalar(value)
    field_re = re.compile(rf"^{re.escape(field)}\s*:")
    for idx in range(bounds[0] + 1, end_idx):
        body, ending = _line_body_and_ending(lines[idx])
        if field_re.match(body):
            lines[idx] = f"{field}: {scalar}{ending or _content_newline(content)}"
            return "".join(lines), True, True

    newline = _content_newline(content)
    lines.insert(end_idx, f"{field}: {scalar}{newline}")
    return "".join(lines), True, True


def extract_dialogue_content(parsed: Any, key: str) -> str | None:
    lines = parsed.source_text.splitlines()
    start_idx = parsed.yaml_end_line or 0
    for idx in range(start_idx, len(lines)):
        key_matches = list(KEY_COMMENT_RE.finditer(lines[idx]))
        if not any(match.group(1).strip() == key for match in key_matches):
            continue

        for content_idx in range(idx + 1, len(lines)):
            candidate = lines[content_idx]
            if KEY_COMMENT_RE.search(candidate):
                return None
            stripped = HTML_COMMENT_RE.sub("", candidate).strip()
            if not stripped:
                continue
            return strip_dialogue_content_markup(stripped)
        return None
    return None


def strip_dialogue_content_markup(text: str) -> str:
    result = text.strip()
    result = re.sub(r"^\s*(?:[-*]\s*)?(?:\*\*|__)[^*_：:]{1,80}[：:](?:\*\*|__)\s*", "", result)
    result = re.sub(r"^\s*(?:[-*]\s*)?[^：:\n]{1,80}[：:]\s*", "", result)
    result = re.sub(r"(\*\*|__)(.*?)\1", r"\2", result)
    result = re.sub(r"(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)", r"\1", result)
    result = re.sub(r"(?<!_)_(?!_)(.*?)(?<!_)_(?!_)", r"\1", result)
    return result.strip()


def asset_payload(entry: Any) -> dict[str, Any]:
    return {
        "asset_id": entry.asset_id,
        "subtype": entry.subtype,
        "display_name": entry.display_name,
        "owner": entry.owner,
        "state_tags": list(entry.state_tags),
        "aliases": list(entry.aliases),
    }


def asset_usage_records(repo_index: Any, asset_id: str) -> list[dict[str, Any]]:
    parsed_by_path = {
        parsed.path: parsed
        for parsed in repo_index.all_files_parsed
        if parsed.path is not None
    }
    usage: list[dict[str, Any]] = []
    for file_path, dialogue_result in repo_index.all_dialogue_keys.file_results.items():
        parsed = parsed_by_path.get(file_path)
        if parsed is None:
            continue
        path = PROJECT_ROOT / file_path
        scene_id = parsed_scene_id(parsed, path)
        version = version_from_path(path)
        for key, entry in dialogue_result.entries.items():
            for field in asset_reference_fields(entry, asset_id):
                usage.append(
                    {
                        "scene_id": scene_id,
                        "key": key,
                        "field": field,
                        "version": version,
                    }
                )
    usage.sort(key=lambda item: (str(item["scene_id"] or ""), str(item["version"] or ""), item["key"], item["field"]))
    return usage


def asset_reference_fields(entry: Any, asset_id: str) -> list[str]:
    fields: list[str] = []
    if entry.portrait == asset_id:
        fields.append("portrait")
    if entry.bgm == asset_id:
        fields.append("bgm")
    if asset_id in entry.sfx:
        fields.append("sfx")
    return fields


def scene_asset_ids(repo_index: Any, scene_id: str) -> set[str]:
    return {
        usage["asset_id"]
        for asset_id in repo_index.art_metadata_index.by_asset_id
        for usage in (
            {"asset_id": asset_id, **record}
            for record in asset_usage_records(repo_index, asset_id)
            if record["scene_id"] == scene_id
        )
    }


# entity_type_from_id 改 import 自 scripts.parse_frontmatter（registry-derived，見檔頭 import）。
# 原本地硬編碼版本（漏 W-style，與 parser drift）於 Batch 6 / NEW_REQ_49 移除。


def parsed_entities(parsed: Any) -> list[str]:
    yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
    entities = yaml_data.get("entities")
    if not isinstance(entities, list):
        return []
    return [entity for entity in entities if isinstance(entity, str)]


def parsed_matches_scope(parsed: Any, scope: str) -> bool:
    if scope == "full":
        return True
    # Phase A.0F.patch-round2-P2 / option (a): outline_only follows L3 schema
    # §1.3 — W-rules + W-language + V + C-* + R-*-* + P + CH-*. Scene-body
    # files (S-*) and art-metadata files (A-*) are excluded.
    if scope == "outline_only":
        return parsed_outline_relevant(parsed)
    yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
    rel = parsed.path or ""
    path = PROJECT_ROOT / rel
    scene_id = yaml_data.get("scene_id") if isinstance(yaml_data.get("scene_id"), str) else scene_id_from_path(path)
    if scope.startswith("scene/"):
        return scene_id == scope.split("/", 1)[1]
    if scope.startswith("chapter/"):
        chapter = normalize_chapter(scope.split("/", 1)[1])
        return scene_id is not None and scene_id.startswith(f"S-{chapter}-")
    return False


def normalize_chapter(raw: str) -> str:
    value = raw.strip()
    if value.upper().startswith("CH"):
        value = value[2:]
    return value.zfill(2)


# Phase A.0F.patch-round2-P2 / option (a): L3 schema §1.3 outline_only.
# outline_only includes the narrative-bible entity types but excludes scene
# bodies (S-*) and art assets (A-*). The same list also drives qa_report_count
# and art_assets filtering for the outline_only scope.
OUTLINE_ENTITY_TYPES: frozenset[str] = frozenset({"W-rules", "W-language", "V", "P"})
OUTLINE_ENTITY_PREFIXES: tuple[str, ...] = ("C-", "R-", "CH-")


def is_outline_entity(entity_id: str) -> bool:
    """Return True if `entity_id` belongs to the L3 outline_only scope."""
    if entity_id in OUTLINE_ENTITY_TYPES:
        return True
    return any(entity_id.startswith(prefix) for prefix in OUTLINE_ENTITY_PREFIXES)


def parsed_outline_relevant(parsed: Any) -> bool:
    """Return True if `parsed`'s declared entities overlap the outline scope."""
    entities = parsed_entities(parsed)
    return any(is_outline_entity(ent) for ent in entities)


def scope_counts_payload(repo_index: Any, scope: str) -> dict[str, Any]:
    selected_paths = {
        parsed.path
        for parsed in repo_index.all_files_parsed
        if parsed.path is not None and parsed_matches_scope(parsed, scope)
    }
    entity_ids: set[str] = set()
    for parsed in repo_index.all_files_parsed:
        if parsed.path in selected_paths:
            entity_ids.update(parsed_entities(parsed))

    art_entries = list(repo_index.art_metadata_index.by_asset_id.values())
    if scope == "outline_only":
        # Phase A.0F.patch-round2-P2 / option (a): outline_only excludes A-* art
        # assets per L3 schema §1.3. counts.art_assets reports 0 for this scope.
        art_entries = []
    elif scope.startswith("scene/"):
        wanted_assets = scene_asset_ids(repo_index, scope.split("/", 1)[1])
        art_entries = [entry for entry in art_entries if entry.asset_id in wanted_assets]
    elif scope.startswith("chapter/"):
        chapter = normalize_chapter(scope.split("/", 1)[1])
        scene_ids = {
            parsed_scene_id(parsed, PROJECT_ROOT / (parsed.path or ""))
            for parsed in repo_index.all_files_parsed
            if parsed.path in selected_paths
        }
        wanted_assets = {
            usage["asset_id"]
            for scene_id in scene_ids
            if scene_id is not None and scene_id.startswith(f"S-{chapter}-")
            for usage in (
                {"asset_id": asset_id, **record}
                for asset_id in repo_index.art_metadata_index.by_asset_id
                for record in asset_usage_records(repo_index, asset_id)
                if record["scene_id"] == scene_id
            )
        }
        art_entries = [entry for entry in art_entries if entry.asset_id in wanted_assets]

    # Phase A.0F.patch-major-1 / D-045: A-* are art assets, not narrative
    # entities. They must NOT be merged into entity_counts (which feeds the
    # narrative readiness percentage and Module Status). Keep A-* visible only
    # in counts.art_assets and the asset panel. CODEX Major finding.
    entity_counts: dict[str, int] = {"C": 0, "R": 0, "S": 0, "CH": 0, "A": 0}
    for entity_id in sorted(entity_ids):
        entity_type = entity_type_from_id(entity_id)
        if entity_type == "A":
            # frontmatter may still list A-* entities; per D-045 we ignore them
            # for narrative readiness, but the asset panel reads art_metadata
            # directly so the count remains accurate.
            continue
        # Phase A.0F.patch-round2-P2 / option (a): outline_only excludes scene
        # bodies (S-*) per L3 schema §1.3. The narrative bible files that the
        # outline scope cares about still declare C-* / R-* / CH-* / W-rules
        # entities through their frontmatter and pass through above.
        if scope == "outline_only" and entity_type == "S":
            continue
        entity_counts[entity_type] = entity_counts.get(entity_type, 0) + 1

    dialogue_lines = 0
    for file_path, result in repo_index.all_dialogue_keys.file_results.items():
        if scope != "full" and file_path not in selected_paths:
            continue
        dialogue_lines += sum(1 for entry in result.entries.values() if entry.status != "deleted")

    return {
        "scope": scope,
        "counts": {
            "entities": entity_counts,
            "dialogue_lines": dialogue_lines,
            "art_assets": len(art_entries),
            "qa_reports": qa_report_count(repo_index, scope),
        },
    }


def qa_report_count(repo_index: Any, scope: str) -> int:
    total = 0
    for parsed in repo_index.all_files_parsed:
        rel = parsed.path or ""
        if not rel.startswith("09_quality_assurance/") or "模板" in rel:
            continue
        yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
        if "qa_type" not in yaml_data:
            continue
        if scope != "full" and not parsed_matches_scope(parsed, scope):
            continue
        total += 1
    return total


def valid_scope_counts_scope(scope: str) -> bool:
    # Phase A.0F.patch-round2-P2 / option (a): outline_only is L3 schema §1.2.
    return (
        scope == "full"
        or scope == "outline_only"
        or scope.startswith("scene/")
        or scope.startswith("chapter/")
    )


@app.get("/api/scene/{scene_id}/header")
async def get_scene_header(scene_id: str) -> Any:
    try:
        resolved = resolve_scene_file(scene_id)
        if resolved is None:
            return json_error(404, f"scene not found: {scene_id}")
        path, parsed = resolved
        return {
            "scene_id": scene_id,
            "path": rel_path(path),
            "header": header_payload(parsed),
            "mtime": path.stat().st_mtime,
            "issues": [issue_payload(issue) for issue in parsed.issues],
        }
    except Exception as exc:
        return json_error(500, str(exc))


@app.post("/api/scene/{scene_id}/save")
async def save_scene(scene_id: str, request: Request) -> Any:
    try:
        payload = await read_json_object(request)
        content = required_string(payload, "content")
        mtime_baseline = required_float(payload, "mtime_baseline")
        # Phase A.0F.patch-P0: target_path is required. Front-end editing v01
        # must explicitly request save against v01. Backend no longer resolves
        # the latest mtime candidate (CODEX P0 finding: wrong-version write on
        # multi-version scenes).
        target_path_raw = optional_string(payload, "target_path")
        if target_path_raw is None or not target_path_raw.strip():
            return json_error(
                400,
                "target_path is required â the editor must send the "
                "exact repo-relative POSIX v.path that was being edited.",
            )
        resolved = resolve_target_path(scene_id, target_path_raw)
        if resolved is None:
            return json_error(
                404,
                f"target_path validation failed â path must live under "
                f"08_dialogue_outputs/ and match scene_id {scene_id}",
            )

        path, _parsed = resolved
        latest_parsed = parse_file(path, repo_root=PROJECT_ROOT)
        current_mtime = path.stat().st_mtime
        if is_locked(latest_parsed):
            return JSONResponse(
                status_code=409,
                content={
                    "error": "LOCKED_OVERWRITE_DENIED",
                    "scene_id": scene_id,
                    "current_status": "LOCKED",
                    "current_mtime": current_mtime,
                    "suggestion": f"用 /api/scene/{scene_id}/save-as 另存 DRAFT proposal",
                },
            )

        if abs(current_mtime - mtime_baseline) > 0.000001:
            return JSONResponse(
                status_code=409,
                content={
                    "error": "MTIME_DRIFT",
                    "scene_id": scene_id,
                    "saved": False,
                    "current_mtime": current_mtime,
                    "mtime_baseline": mtime_baseline,
                    "mtime_drift": True,
                    "server_content": read_markdown(path),
                    "server_header": header_payload(latest_parsed),
                    "client_content_length": len(content),
                    "suggestion": "前端 Conflict modal 應顯示 server_content vs client_content 兩版差異",
                },
            )

        path.write_text(content, encoding="utf-8")
        return {
            "scene_id": scene_id,
            "saved": True,
            "new_mtime": path.stat().st_mtime,
            "mtime_drift": False,
        }
    except ValueError as exc:
        return json_error(400, str(exc))
    except Exception as exc:
        return json_error(500, str(exc))


@app.post("/api/scene/{scene_id}/save-as")
async def save_scene_as(scene_id: str, request: Request) -> Any:
    try:
        payload = await read_json_object(request)
        content = required_string(payload, "content")
        base_scene_id = optional_string(payload, "base_scene_id")
        if base_scene_id is None:
            base_scene_id = optional_string(payload, "base_dialogue")
        base_scene_id = base_scene_id.strip() if base_scene_id and base_scene_id.strip() else scene_id
        iteration_note = optional_string(payload, "iteration_note")
        # Phase A.0F.patch-P0: target_path is required so the proposal is based
        # on the exact version the user was editing (CODEX P0 finding).
        target_path_raw = optional_string(payload, "target_path")
        if target_path_raw is None or not target_path_raw.strip():
            return json_error(
                400,
                "target_path is required â save-as must reference the "
                "editor source v.path (repo-relative POSIX).",
            )
        resolved = resolve_target_path(scene_id, target_path_raw)
        if resolved is None:
            return json_error(
                404,
                f"target_path validation failed â path must live under "
                f"08_dialogue_outputs/ and match scene_id {scene_id}",
            )

        original_path, _parsed = resolved
        suffix = sanitize_suffix(payload.get("proposal_suffix"))
        target_path = original_path.with_name(f"{original_path.stem}_proposal_{suffix}{original_path.suffix}")
        if target_path.exists():
            return json_error(409, f"proposal file already exists: {rel_path(target_path)}")

        warnings: list[str] = []
        content, _status_patched, status_warning = patch_proposal_status(content)
        if status_warning:
            warnings.append(status_warning)

        content, _base_patched, yaml_found = patch_frontmatter_field(content, "base_dialogue", base_scene_id)
        if not yaml_found:
            warnings.append("frontmatter YAML block not found; base_dialogue not recorded")

        iteration_note_recorded = False
        if iteration_note is not None and iteration_note.strip():
            content, iteration_note_recorded, yaml_found = patch_frontmatter_field(
                content,
                "iteration_note",
                iteration_note.strip(),
            )
            if not yaml_found:
                warnings.append("frontmatter YAML block not found; iteration_note not recorded")

        response_payload: dict[str, Any] = {
            "original_scene_id": scene_id,
            "saved_as_path": rel_path(target_path),
            "saved": True,
            "proposal_status": "DRAFT",
            "base_dialogue": base_scene_id,
            "iteration_note_recorded": iteration_note_recorded,
        }
        if warnings:
            response_payload["warnings"] = warnings

        target_path.write_text(content, encoding="utf-8")
        return JSONResponse(
            status_code=200,
            content=response_payload,
        )
    except ValueError as exc:
        return json_error(400, str(exc))
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/scene/{scene_id}/version-content")
async def get_scene_version_content(scene_id: str, path: Optional[str] = None) -> Any:
    """Return raw markdown content for the exact (scene_id, path) pair.

    Phase A.0F.patch-P0: front-end Editor uses this endpoint to load the version
    body. Previously SceneEditor.js did `fetch("/" + v.path)`, but server.py
    only mounts `_tools/frontend/static` at `/`, so the fetch returned a 404
    body that was silently used as the textarea baseline. CODEX flagged this as
    P0. The new endpoint enforces fail-closed semantics: path must live under
    08_dialogue_outputs/ and match the scene_id.

    Returns: { scene_id, path, content, mtime, header }
    """
    try:
        if path is None or not path.strip():
            return json_error(400, "path query parameter is required")
        resolved = resolve_target_path(scene_id, path)
        if resolved is None:
            return json_error(
                404,
                f"version-content validation failed â path must live under "
                f"08_dialogue_outputs/ and match scene_id {scene_id}",
            )
        target_path, parsed = resolved
        return {
            "scene_id": scene_id,
            "path": rel_path(target_path),
            "content": read_markdown(target_path),
            "mtime": target_path.stat().st_mtime,
            "header": header_payload(parsed),
        }
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/scenes/{scene_id}/versions")
async def get_scene_versions(scene_id: str) -> Any:
    try:
        candidates = scene_file_candidates(scene_id, versioned_only=True)
        if not candidates:
            return json_error(404, f"scene not found: {scene_id}")
        versions = [
            {
                "version": version_from_path(path),
                "path": rel_path(path),
                "mtime": path.stat().st_mtime,
                "header": header_payload(parsed),
            }
            for path, parsed in sorted(candidates, key=lambda item: str(version_from_path(item[0]) or ""))
        ]
        return {"scene_id": scene_id, "versions": versions}
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/scenes/{scene_id}/keys/{key}/lines")
async def get_scene_key_lines(scene_id: str, key: str) -> Any:
    try:
        candidates = scene_file_candidates(scene_id, versioned_only=True)
        if not candidates:
            return json_error(404, f"scene not found: {scene_id}")

        lines: list[dict[str, Any]] = []
        for path, parsed in sorted(candidates, key=lambda item: str(version_from_path(item[0]) or "")):
            yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
            dialogue_keys = yaml_data.get("dialogue_keys")
            if not isinstance(dialogue_keys, dict):
                continue
            raw_entry = dialogue_keys.get(key)
            if not isinstance(raw_entry, dict):
                continue
            lines.append(
                {
                    "version": version_from_path(path),
                    "line_index": raw_entry.get("line_index"),
                    "content": extract_dialogue_content(parsed, key),
                    "speaker": raw_entry.get("speaker"),
                    "status": raw_entry.get("status", "active"),
                }
            )
        return {"scene_id": scene_id, "key": key, "lines": lines}
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/assets")
async def get_assets(scope: Optional[str] = None) -> Any:
    try:
        requested_scope = scope or "all"
        repo_index = build_repo_index(PROJECT_ROOT)
        assets = list(repo_index.art_metadata_index.by_asset_id.values())
        if requested_scope == "all":
            filtered = assets
        elif requested_scope.startswith("subtype/"):
            subtype = requested_scope.split("/", 1)[1]
            filtered = [entry for entry in assets if entry.subtype == subtype]
        elif requested_scope.startswith("scene/"):
            asset_ids = scene_asset_ids(repo_index, requested_scope.split("/", 1)[1])
            filtered = [entry for entry in assets if entry.asset_id in asset_ids]
        else:
            return json_error(400, "scope must be all, scene/<id>, or subtype/<name>")

        payload = [asset_payload(entry) for entry in sorted(filtered, key=lambda item: (item.subtype, item.asset_id))]
        return {"scope": requested_scope, "assets": payload, "total": len(payload)}
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/assets/{asset_id}/usage")
async def get_asset_usage(asset_id: str) -> Any:
    try:
        repo_index = build_repo_index(PROJECT_ROOT)
        if asset_id not in repo_index.art_metadata_index.by_asset_id:
            return json_error(404, f"asset not found: {asset_id}")
        usage = asset_usage_records(repo_index, asset_id)
        return {"asset_id": asset_id, "usage": usage, "total": len(usage)}
    except Exception as exc:
        return json_error(500, str(exc))


@app.get("/api/scope-counts")
async def get_scope_counts(scope: Optional[str] = None) -> Any:
    try:
        requested_scope = scope or "full"
        if not valid_scope_counts_scope(requested_scope):
            return json_error(400, "scope must be full, outline_only, scene/<id>, or chapter/<ch>")
        repo_index = build_repo_index(PROJECT_ROOT)
        return scope_counts_payload(repo_index, requested_scope)
    except Exception as exc:
        return json_error(500, str(exc))



@app.get("/api/scenes")
async def list_scenes(chapter: Optional[str] = None) -> Any:
    """List all S-* scenes for Scene Queue UI (UX_SPEC §11.2.1).

    Optional ?chapter=01 filter. Returns scenes + total + chapters list.

    對齊 UX §11.2.1 Scene card 欄位需求；非 Contract C 鎖定 8 endpoint，
    屬 frontend adapter 自用 list endpoint（避免 N+1 呼叫 /header + /versions）。
    """
    try:
        repo_index = build_repo_index(PROJECT_ROOT)
        seen_scene_ids = set()
        for parsed in repo_index.all_files_parsed:
            for ent in parsed_entities(parsed):
                if ent.startswith("S-") and SCENE_ID_RE.match(ent):
                    seen_scene_ids.add(ent)
        for path in iter_dialogue_files():
            parsed = parse_file(path, repo_root=PROJECT_ROOT)
            sid = parsed_scene_id(parsed, path)
            if sid and SCENE_ID_RE.match(sid):
                seen_scene_ids.add(sid)
        if chapter:
            ch = normalize_chapter(chapter)
            seen_scene_ids = {s for s in seen_scene_ids if s.startswith("S-" + ch + "-")}
        scenes = [scene_summary(scene_id, repo_index) for scene_id in sorted(seen_scene_ids)]
        chapters = sorted({s["chapter"] for s in scenes if s.get("chapter")})
        return {"scenes": scenes, "total": len(scenes), "chapters": chapters}
    except Exception as exc:
        return json_error(500, str(exc))


def scene_summary(scene_id, repo_index):
    """Summary metadata for one scene (UX §11.2.1 Scene card)."""
    match = SCENE_ID_RE.match(scene_id)
    chapter = match.group("chapter") if match else None
    task_path = None
    task_status = None
    for parsed in repo_index.all_files_parsed:
        rel = parsed.path or ""
        if not rel.startswith("07_scene_tasks/"):
            continue
        path = PROJECT_ROOT / rel
        if scene_matches(path, parsed, scene_id):
            task_path = rel
            task_status = parsed.header.get("狀態")
            break
    candidates = scene_file_candidates(scene_id, versioned_only=True)
    versions = []
    latest_mtime = None
    latest_status = None
    for path, parsed in candidates:
        ver = version_from_path(path)
        st = path.stat()
        mt = st.st_mtime
        v_status = parsed.header.get("狀態")
        versions.append({
            "version": ver,
            "path": rel_path(path),
            "mtime": mt,
            "status": v_status,
        })
        if latest_mtime is None or mt > latest_mtime:
            latest_mtime = mt
            latest_status = v_status
    qa_count = 0
    for parsed in repo_index.all_files_parsed:
        rel = parsed.path or ""
        if not rel.startswith("09_quality_assurance/") or "模板" in rel:
            continue
        if scene_id in parsed_entities(parsed):
            qa_count += 1
    entities_set = set()
    if task_path:
        for parsed in repo_index.all_files_parsed:
            if parsed.path == task_path:
                entities_set.update(parsed_entities(parsed))
                break
    for v in versions:
        for parsed in repo_index.all_files_parsed:
            if parsed.path == v["path"]:
                entities_set.update(parsed_entities(parsed))
                break
    pipeline_state = latest_status or task_status or "未啟動"
    return {
        "scene_id": scene_id,
        "chapter": chapter,
        "task_path": task_path,
        "task_status": task_status,
        "dialogue_versions": versions,
        "dialogue_count": len(versions),
        "latest_mtime": latest_mtime,
        "pipeline_state": pipeline_state,
        "qa_report_count": qa_count,
        "entities_count": len(entities_set),
    }


# Static assets
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    print(f"> Serving from {PROJECT_ROOT}")
    print(f"> Open browser: http://{args.host}:{args.port}")
    print("> Press Ctrl-C to stop")
    uvicorn.run(app, host=args.host, port=args.port)
