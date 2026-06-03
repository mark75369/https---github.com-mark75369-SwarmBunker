#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Frontmatter parser baseline (A.0.1).

YAML parsing strategy:
- Prefer PyYAML if available (`import yaml`).
- Fall back to local limited YAML subset parser (no PyYAML dependency in A.0.1).
- A.5 /init-project may add PyYAML to requirements.txt for full YAML compliance.

Subset parser supports:
- list of scalars
- dict of scalar/list/dict (max nest depth 3)
- map of scalars (for `weight` field)
- nested dialogue_keys Map + art_metadata List (treated as raw dict/list, deep validation deferred to A.0.2/A.0.4)

Does NOT support:
- YAML anchors / aliases
- Flow style ({a: 1, b: 2})
- Multi-line strings (| / >)
- Custom tags

If user encounters complex YAML, install PyYAML manually:
  pip install pyyaml
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Any

try:  # pragma: no cover - local checkout intentionally has no PyYAML.
    import yaml as _pyyaml  # type: ignore
except Exception:  # pragma: no cover
    _pyyaml = None


REQUIRED_HEADER_FIELDS = ["狀態", "版本", "最後更新", "適用範圍", "優先級"]

VALID_DOCUMENT_STATUSES = {
    "DRAFT",
    "REVIEW",
    "FINAL",
    "LOCKED",
    "DEPRECATED",
    "APPLIED",
    "DERIVED",
}
VALID_PRIORITIES = {"最高", "高", "中", "低", "一般"}

VALID_PIPELINE_STATES = {
    "SCENE_INDEXED",
    "TASK_DRAFT",
    "TASK_REVIEW",
    "DIALOGUE_TRIAL",
    "DIALOGUE_CONVERGED",
    "QA_PASSED",
    "QA_FAILED",
    "DIALOGUE_FINAL",
    "DIALOGUE_LOCKED",
}
VALID_MODE_TAGS = {
    "ORGANIZED",
    "DRAFT_TRIAL",
    "EXPERIMENTAL",
    "CONVERGENCE",
    "FINAL_CANDIDATE",
    "SINGLE_ITER",
}
VALID_QA_DECISIONS = {"PASS", "FAIL", "ARBITRATE_REQUIRED"}

DOWNSTREAM_FIELDS = [
    "scene_id",
    "source_task",
    "source_dialogue",
    "source_dialogues",
    "pipeline_state",
    "mode_tag",
    "qa_decision",
    "qa_type",
]
UPSTREAM_FIELDS = ["entities", "depends_on", "weight"]
YAML_RECOGNIZED_FIELDS = set(UPSTREAM_FIELDS + DOWNSTREAM_FIELDS + ["dialogue_keys", "art_metadata"])

VALID_PHASE_STATUSES = {"completed", "in_progress", "aborted"}
VALID_IMPORT_SOURCES = {"agent_assisted", "external_llm"}
VALID_CONFLICT_DECISIONS = {"merge", "overwrite", "create-as-new", "skip"}
VALID_DIALOGUE_KEY_STATUSES = {"active", "deprecated", "deleted"}
VALID_ART_STATUSES = {"active", "deprecated", "deleted"}
ART_SUBTYPE_ORDER = ("portrait", "bg", "cg", "sfx", "bgm", "voice", "ui")
ART_RESERVED_SUBTYPES = ("icon", "effect", "video", "shader")
ART_FORBIDDEN_FIELDS = {"file_path", "url", "source_image", "binary_data"}
ART_REQUIRED_ERROR_FIELDS = ("asset_id", "display_name", "subtype", "state_tags", "aliases", "created_at")
EXPORT_SCHEMA_VERSION = "1.0"
EXPORT_TOOL_VERSION = "v0.1"
DATA_FORMAT_SPEC_VERSION = "data_format_spec_v0.3"
EXPORT_EXCLUDED_RECORD_DIRS = {".git", "_design", "_archive", "archive", "_user_manual"}
# User-supplied source materials live under <instance_root>/_source_materials/.
# They are NOT entities, carry no entity ID, and must be excluded from the
# repo-wide markdown scan that feeds build_repo_index (see _iter_repo_markdown_files).
SOURCE_MATERIAL_DIR_NAMES = {"_source_materials"}

# Narrative-outline scope: the curated subset of entity types that the export /
# scope-count layer treats as "outline" content. This is a *semantic* subset and
# is intentionally NARROWER than the full registry type set — W-style / S / A /
# ORG are deliberately excluded (NEW_REQ_49: the registry has no outline-scope
# field, so the curated membership lives here, but every member is validated
# against the registry at access time so a dropped/renamed core type can never
# silently survive here). Authoritative type set: entity_type_registry. Access
# the validated set via the module attribute OUTLINE_ENTITY_TYPES (registry-
# intersected) rather than this raw allowlist.
_OUTLINE_ENTITY_TYPE_ALLOWLIST = ("W-rules", "W-language", "V", "C", "R", "P", "CH")

VERSION_RE = re.compile(r"^v?\d+\.\d+(?:\.\d+)?(?:-[\w]+)?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# NOTE: ENTITY_ID_RE and OUTLINE_ENTITY_TYPES are NOT defined here as module
# globals. They are derived at first access from load_entity_type_registry()
# core[].id_pattern + user_extensions, via the module-level __getattr__ below
# (PEP 562). This removes the second, drift-prone hardcoded mirror of the
# per-type id_pattern set that previously lived here (NEW_REQ_49 / P1-ENTITY_ID_RE).
DEFAULT_DIALOGUE_KEY_RE = re.compile(r"^dlg\.ch\d{2}\.s\d{2}[a-z]*\.l\d{3}(?:_[a-z0-9_]+)?$")
USER_DEFINED_DIALOGUE_KEY_RE = re.compile(r"^[a-z0-9._-]+$")
KEY_COMMENT_RE = re.compile(r"<!--\s*KEY\s*[:：]\s*(.*?)\s*-->", re.IGNORECASE)
ART_COMMENT_RE = re.compile(r"<!--\s*(立繪|背景|BGM|SFX|A-portrait|A-bg|A-bgm|A-sfx)\s*[:：]\s*(.*?)\s*-->", re.IGNORECASE)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->")

ART_COMMENT_FIELD_BY_TYPE = {
    "立繪": "portrait",
    "背景": "bg",
    "BGM": "bgm",
    "SFX": "sfx",
    "a-portrait": "portrait",
    "a-bg": "bg",
    "a-bgm": "bgm",
    "a-sfx": "sfx",
}
ART_COMMENT_TYPE_BY_FIELD = {
    "portrait": "立繪",
    "bg": "背景",
    "bgm": "BGM",
    "sfx": "SFX",
}

ENTITY_TYPE_REGISTRY_TEMPLATE_PATH = Path("_design/registries/entity_type_registry.template.yaml")
QA_TYPE_REGISTRY_TEMPLATE_PATH = Path("_design/registries/qa_type_registry.template.yaml")
HEAD_LINES = 30


@dataclass
class ValidationIssue:
    severity: str
    line_num: int
    message: str


@dataclass
class ParsedMarkdown:
    path: str | None
    header: dict[str, str | None]
    yaml_data: Any = None
    yaml_start_line: int | None = None
    yaml_end_line: int | None = None
    issues: list[ValidationIssue] = field(default_factory=list)
    is_pipeline_artifact: bool = False
    source_text: str = ""


@dataclass
class PhaseLogResult:
    entries: list[dict[str, Any]]
    issues: list[ValidationIssue] = field(default_factory=list)


@dataclass
class DialogueKeyEntry:
    map_key: str
    line_index: int | None
    speaker: str | None
    aliases: list[str]
    portrait: str | None
    bgm: str | None
    sfx: list[str]
    status: str
    created_at: Any = None
    renamed_at: Any = None
    deleted_at: Any = None
    deprecated_reason: str | None = None
    source_keys: list[str] | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    line_num: int = 0


@dataclass
class DialogueKeysResult:
    entries: dict[str, DialogueKeyEntry]
    body_key_order: list[str] = field(default_factory=list)
    body_key_lines: dict[str, list[int]] = field(default_factory=dict)
    body_art_comments: dict[str, dict[str, list[str]]] = field(default_factory=dict)
    issues: list[ValidationIssue] = field(default_factory=list)


@dataclass
class BodyArtReference:
    associated_key: str
    art_type: str
    asset_id: str
    line_in_file: int


@dataclass
class BodyArtRefResult:
    refs: list[BodyArtReference]
    issues: list[ValidationIssue] = field(default_factory=list)


@dataclass
class AllDialogueKeysIndex:
    all_keys_set: set[str] = field(default_factory=set)
    alias_to_current_key: dict[str, tuple[str, str]] = field(default_factory=dict)
    key_to_file_path: dict[str, str] = field(default_factory=dict)
    file_results: dict[str, DialogueKeysResult] = field(default_factory=dict)
    issues: list[ValidationIssue] = field(default_factory=list)

    def get_all_dialogue_keys(self) -> set[str]:
        return set(self.all_keys_set)

    def get_alias_to_current_key_map(self) -> dict[str, str]:
        return {
            alias: current_key
            for alias, (current_key, _file_path) in self.alias_to_current_key.items()
        }

    def get_alias_to_current_key_file_map(self) -> dict[str, tuple[str, str]]:
        return dict(self.alias_to_current_key)


@dataclass
class ArtMetadataEntry:
    asset_id: str
    display_name: str
    subtype: str
    owner: str | None
    state_tags: list[str]
    aliases: list[str]
    created_at: str
    renamed_at: str | None
    deleted_at: str | None
    status: str | None
    deprecated_reason: str | None
    dialogue_keys_ref: str | None
    source_file: str


@dataclass
class ArtMetadataResult:
    entries: list[ArtMetadataEntry]
    issues: list[ValidationIssue] = field(default_factory=list)


@dataclass
class ArtMetadataIndex:
    by_asset_id: dict[str, ArtMetadataEntry] = field(default_factory=dict)
    by_subtype: dict[str, list[ArtMetadataEntry]] = field(default_factory=dict)
    by_owner: dict[str, list[ArtMetadataEntry]] = field(default_factory=dict)
    all_asset_ids: set[str] = field(default_factory=set)
    alias_to_current: dict[str, str] = field(default_factory=dict)
    issues: list[ValidationIssue] = field(default_factory=list)
    files_scanned: list[str] = field(default_factory=list)


@dataclass
class CompletenessStats:
    subtype: str
    total: int
    completed: int
    in_progress: int
    not_started: int
    missing: int
    coverage_pct: float


@dataclass
class EntityTypeEntry:
    type: str
    description: str
    id_pattern: str
    id_pattern_compiled: re.Pattern
    target_dir: str
    cross_ref_allowed: bool
    locked: bool
    subtype_allowed: list[str] | None = None
    subtype_reserved: list[str] | None = None


@dataclass
class EntityTypeRegistry:
    version: int
    schema_version: str
    core: dict[str, EntityTypeEntry]
    reserved_prefixes: list[str]
    user_extensions: dict[str, EntityTypeEntry]
    source: str
    issues: list[ValidationIssue] = field(default_factory=list)

    def get_entry(self, type_or_prefix: str) -> EntityTypeEntry | None:
        return self.core.get(type_or_prefix) or self.user_extensions.get(type_or_prefix)

    def all_valid_types(self) -> set[str]:
        return set(self.core) | set(self.user_extensions)


@dataclass
class QaTypeEntry:
    qa_type: str
    description: str
    template_path: str
    locked: bool


@dataclass
class QaTypeRegistry:
    version: int
    schema_version: str
    core: dict[str, QaTypeEntry]
    user_extensions: dict[str, QaTypeEntry]
    source: str
    issues: list[ValidationIssue] = field(default_factory=list)

    def get_entry(self, qa_type: str) -> QaTypeEntry | None:
        return self.core.get(qa_type) or self.user_extensions.get(qa_type)

    def all_valid_qa_types(self) -> set[str]:
        return set(self.core) | set(self.user_extensions)


@dataclass
class RepoIndex:
    entity_registry: EntityTypeRegistry
    qa_registry: QaTypeRegistry
    all_files_parsed: list[ParsedMarkdown]
    all_dialogue_keys: AllDialogueKeysIndex
    art_metadata_index: ArtMetadataIndex
    body_art_refs: dict[str, BodyArtRefResult]
    phase_log_result: PhaseLogResult
    issues: list[ValidationIssue]
    repo_root: str = ""

    def get_completeness(self) -> dict[str, CompletenessStats]:
        return get_asset_completeness_by_subtype(self.art_metadata_index, self.body_art_refs)


@dataclass
class EntityRecord:
    record_type: str = field(default="entity", init=False)
    source_file: str = ""
    header: dict[str, str | None] = field(default_factory=dict)
    frontmatter: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    downstream_fields: dict[str, Any] = field(default_factory=dict)
    art_metadata: list[dict[str, Any]] | None = None


@dataclass
class DialogueLineRecord:
    record_type: str = field(default="dialogue_line", init=False)
    source_file: str = ""
    key: str = ""
    line_index: int = 0
    speaker: str | None = None
    aliases: list[str] = field(default_factory=list)
    portrait: str | None = None
    bgm: str | None = None
    sfx: list[str] = field(default_factory=list)
    status: str = "active"
    created_at: str = ""
    renamed_at: str | None = None
    deleted_at: str | None = None
    deprecated_reason: str | None = None
    source_keys: list[str] | None = None
    content: str | None = None
    in_scene_context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ArtMetadataRecord:
    record_type: str = field(default="art_metadata", init=False)
    source_file: str = ""
    asset_id: str = ""
    display_name: str = ""
    subtype: str = ""
    owner: str | None = None
    state_tags: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    dialogue_keys_ref: str | None = None
    created_at: str = ""
    renamed_at: str | None = None
    deleted_at: str | None = None
    status: str | None = None
    deprecated_reason: str | None = None


@dataclass
class ManifestSnapshot:
    export_version: str
    exported_at: str
    tool_version: str
    instance_id: str
    spec_version: str
    stats: dict[str, Any]
    entity_type_registry: dict[str, Any]
    qa_type_registry: dict[str, Any]


class LimitedYamlError(ValueError):
    pass


def parse_markdown_text(
    content: str,
    rel_path: str | None = None,
    qa_type_registry: QaTypeRegistry | None = None,
) -> ParsedMarkdown:
    content = content.lstrip("\ufeff")
    lines = content.splitlines()
    header, header_lines, issues = _parse_header(lines)
    _validate_header(header, header_lines, issues)

    yaml_data = None
    yaml_start_line = None
    yaml_end_line = None
    is_pipeline_artifact = False

    block = _find_header_adjacent_yaml(lines, header_lines)
    if block:
        yaml_text, yaml_start_line, yaml_end_line = block
        try:
            yaml_data = load_yaml_text(yaml_text)
        except LimitedYamlError as exc:
            issues.append(ValidationIssue("ERROR", yaml_start_line, f"YAML parse error: {exc}"))
            yaml_data = None

        if yaml_data is not None:
            _validate_frontmatter_yaml(yaml_data, yaml_start_line, issues, qa_type_registry)
            if isinstance(yaml_data, dict):
                is_pipeline_artifact = any(yaml_data.get(field) is not None for field in DOWNSTREAM_FIELDS)

    return ParsedMarkdown(
        path=rel_path,
        header=header,
        yaml_data=yaml_data,
        yaml_start_line=yaml_start_line,
        yaml_end_line=yaml_end_line,
        issues=issues,
        is_pipeline_artifact=is_pipeline_artifact,
        source_text=content,
    )


def parse_file(
    path: str | Path,
    repo_root: str | Path | None = None,
    qa_type_registry: QaTypeRegistry | None = None,
) -> ParsedMarkdown:
    file_path = Path(path)
    rel_path = file_path.as_posix()
    if repo_root is not None:
        try:
            rel_path = file_path.relative_to(Path(repo_root)).as_posix()
        except ValueError:
            rel_path = file_path.as_posix()

    try:
        content = file_path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError as exc:
        return ParsedMarkdown(
            path=rel_path,
            header={field_name: None for field_name in REQUIRED_HEADER_FIELDS},
            issues=[ValidationIssue("ERROR", 0, f"cannot read file: {exc}")],
        )

    resolved_qa_registry = qa_type_registry
    if resolved_qa_registry is None:
        registry_root = Path(repo_root) if repo_root is not None else Path(".")
        resolved_qa_registry = load_qa_type_registry(registry_root)

    return parse_markdown_text(content, rel_path=rel_path, qa_type_registry=resolved_qa_registry)


def parse_phase_log_text(content: str, rel_path: str = ".protocol_version") -> PhaseLogResult:
    try:
        data = load_yaml_text(content)
    except LimitedYamlError as exc:
        return PhaseLogResult(entries=[], issues=[ValidationIssue("ERROR", 1, f"YAML parse error: {exc}")])

    if isinstance(data, dict):
        raw_entries = data.get("phase_log", [])
    else:
        raw_entries = data

    if raw_entries is None:
        raw_entries = []
    if not isinstance(raw_entries, list):
        return PhaseLogResult(
            entries=[],
            issues=[ValidationIssue("ERROR", 1, f"{rel_path}: phase_log must be a list")],
        )

    entries: list[dict[str, Any]] = []
    issues: list[ValidationIssue] = []
    for idx, entry in enumerate(raw_entries, start=1):
        if not isinstance(entry, dict):
            issues.append(ValidationIssue("ERROR", 0, f"{rel_path}: phase_log[{idx}] must be a dict"))
            continue
        entries.append(entry)

    issues.extend(validate_phase_log(entries, rel_path=rel_path))
    return PhaseLogResult(entries=entries, issues=issues)


def load_entity_type_registry(
    instance_root: str | Path,
    fallback_to_template: bool = True,
) -> EntityTypeRegistry:
    """Load the Phase A.0 entity type registry for an Instance root.

    Template core entries remain authoritative even when an Instance registry is
    present. Instance registries add user_extensions only.
    """
    root = Path(instance_root)
    issues: list[ValidationIssue] = []

    template_path = root / ENTITY_TYPE_REGISTRY_TEMPLATE_PATH
    template_data, template_issues = _read_registry_yaml(template_path)
    issues.extend(template_issues)

    template_map = template_data if isinstance(template_data, dict) else {}
    if template_data is not None and not isinstance(template_data, dict):
        issues.append(ValidationIssue("ERROR", 0, f"{template_path.as_posix()}: registry YAML must be a map"))

    template_version = _registry_int(template_map.get("version"), 0)
    template_schema_version = str(template_map.get("schema_version") or "")
    core = _parse_entity_type_entries(
        template_map.get("core", []),
        "core",
        root,
        issues,
        validate_target_dirs=False,
    )
    reserved_prefixes = _parse_reserved_prefixes(template_map.get("reserved_prefixes", []), issues)

    instance_path = root / "entity_type_registry.yaml"
    source = "instance"
    registry_map: dict[str, Any] = {}

    if instance_path.exists():
        instance_data, instance_issues = _read_registry_yaml(instance_path)
        issues.extend(instance_issues)
        if isinstance(instance_data, dict):
            registry_map = instance_data
            _validate_instance_core_entries(registry_map.get("core"), core, root, issues)
            if not reserved_prefixes:
                reserved_prefixes = _parse_reserved_prefixes(registry_map.get("reserved_prefixes", []), issues)
        elif instance_data is not None:
            issues.append(ValidationIssue("ERROR", 0, f"{instance_path.as_posix()}: registry YAML must be a map"))
    elif fallback_to_template:
        source = "template_fallback"
        registry_map = template_map
        issues.append(ValidationIssue("WARN", 0, "Instance registry 不存在，fallback Template"))
    else:
        source = "instance"
        issues.append(ValidationIssue("ERROR", 0, "Instance registry 不存在"))

    version = _registry_int(registry_map.get("version"), template_version)
    schema_version = str(registry_map.get("schema_version") or template_schema_version)
    user_extensions = _parse_entity_type_entries(
        registry_map.get("user_extensions", []),
        "user_extensions",
        root,
        issues,
        validate_target_dirs=True,
    )
    _validate_user_extension_entries(user_extensions, core, reserved_prefixes, issues)

    return EntityTypeRegistry(
        version=version,
        schema_version=schema_version,
        core=core,
        reserved_prefixes=reserved_prefixes,
        user_extensions=user_extensions,
        source=source,
        issues=issues,
    )


def get_entity_type_registry(instance_root: str | Path = ".") -> EntityTypeRegistry:
    return load_entity_type_registry(instance_root)


# ---------------------------------------------------------------------------
# Registry-derived module constants (NEW_REQ_49 / P1-ENTITY_ID_RE).
#
# ENTITY_ID_RE, OUTLINE_ENTITY_TYPES are no longer hardcoded. They are derived
# once (module-cached) from the entity_type_registry so they can never drift
# from the per-type id_pattern / type set. validate_entity_id() remains the
# authoritative per-type validator (it uses each entry's id_pattern_compiled);
# ENTITY_ID_RE is only a fast, registry-derived pre-filter for phase_log
# entities_touched WARN checks.
# ---------------------------------------------------------------------------

# Repo root for module-level (no instance_root passed) registry resolution:
# scripts/parse_frontmatter.py -> repo root is the parent of scripts/.
_MODULE_REPO_ROOT = Path(__file__).resolve().parent.parent

_DERIVED_REGISTRY_CACHE: EntityTypeRegistry | None = None
_DERIVED_ENTITY_ID_RE: re.Pattern | None = None
_DERIVED_OUTLINE_TYPES: frozenset[str] | None = None


def _module_entity_type_registry() -> EntityTypeRegistry:
    """Module-cached registry for deriving ENTITY_ID_RE / OUTLINE_ENTITY_TYPES.

    Loaded once from the repo-root template (fallback_to_template=True so a bare
    checkout with no Instance registry still resolves). Cached because these
    derivations feed hot, module-level constants; callers that need a per-
    Instance registry must still call load_entity_type_registry(instance_root).
    """
    global _DERIVED_REGISTRY_CACHE
    if _DERIVED_REGISTRY_CACHE is None:
        _DERIVED_REGISTRY_CACHE = load_entity_type_registry(
            _MODULE_REPO_ROOT, fallback_to_template=True
        )
    return _DERIVED_REGISTRY_CACHE


def _registry_entries_in_order(registry: EntityTypeRegistry) -> list[EntityTypeEntry]:
    return list(registry.core.values()) + list(registry.user_extensions.values())


def _strip_anchors(pattern: str) -> str:
    """Strip a single leading ^ and trailing $ so patterns can be alternated."""
    body = pattern
    if body.startswith("^"):
        body = body[1:]
    if body.endswith("$") and not body.endswith(r"\$"):
        body = body[:-1]
    return body


def _build_entity_id_re(registry: EntityTypeRegistry) -> re.Pattern:
    """Build a single anchored alternation from every registry id_pattern.

    Each branch is the registry entry's own id_pattern (anchors stripped, wrapped
    in a non-capturing group), so ENTITY_ID_RE accepts exactly the union of IDs
    the registry considers well-formed and cannot drift from per-type patterns.
    """
    branches = [
        f"(?:{_strip_anchors(entry.id_pattern)})"
        for entry in _registry_entries_in_order(registry)
        if entry.id_pattern
    ]
    if not branches:
        # Defensive: an empty registry should match nothing rather than everything.
        return re.compile(r"(?!)")
    return re.compile(r"^(?:" + "|".join(branches) + r")$")


def _build_outline_entity_types(registry: EntityTypeRegistry) -> frozenset[str]:
    """Intersect the curated outline allowlist with valid registry types.

    Keeps the deliberate narrative-outline subset (excludes W-style / S / A /
    ORG) while guaranteeing every member still exists in the registry, so a
    dropped/renamed core type can never silently linger in outline scope.
    """
    valid = registry.all_valid_types()
    return frozenset(t for t in _OUTLINE_ENTITY_TYPE_ALLOWLIST if t in valid)


def _entity_id_re() -> re.Pattern:
    global _DERIVED_ENTITY_ID_RE
    if _DERIVED_ENTITY_ID_RE is None:
        _DERIVED_ENTITY_ID_RE = _build_entity_id_re(_module_entity_type_registry())
    return _DERIVED_ENTITY_ID_RE


def _outline_entity_types() -> frozenset[str]:
    global _DERIVED_OUTLINE_TYPES
    if _DERIVED_OUTLINE_TYPES is None:
        _DERIVED_OUTLINE_TYPES = _build_outline_entity_types(_module_entity_type_registry())
    return _DERIVED_OUTLINE_TYPES


def _reset_registry_derived_cache() -> None:
    """Clear the module-cached registry derivations (test hook only)."""
    global _DERIVED_REGISTRY_CACHE, _DERIVED_ENTITY_ID_RE, _DERIVED_OUTLINE_TYPES
    _DERIVED_REGISTRY_CACHE = None
    _DERIVED_ENTITY_ID_RE = None
    _DERIVED_OUTLINE_TYPES = None


def __getattr__(name: str) -> Any:
    """PEP 562 module-level attribute hook for registry-derived constants.

    Keeps `from parse_frontmatter import ENTITY_ID_RE` / `OUTLINE_ENTITY_TYPES`
    working while the values are computed lazily from the registry on first use.
    """
    if name == "ENTITY_ID_RE":
        return _entity_id_re()
    if name == "OUTLINE_ENTITY_TYPES":
        return _outline_entity_types()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def load_qa_type_registry(
    instance_root: str | Path = ".",
    fallback_to_template: bool = True,
) -> QaTypeRegistry:
    """Load the Phase A.0 qa_type registry for an Instance root.

    Template core entries remain authoritative even when an Instance registry is
    present. Instance registries add user_extensions only. The 09_e final-gating
    record is intentionally not part of this registry.
    """
    root = Path(instance_root)
    issues: list[ValidationIssue] = []

    template_path = root / QA_TYPE_REGISTRY_TEMPLATE_PATH
    template_data, template_issues = _read_registry_yaml(template_path)
    issues.extend(template_issues)

    template_map = template_data if isinstance(template_data, dict) else {}
    if template_data is not None and not isinstance(template_data, dict):
        issues.append(ValidationIssue("ERROR", 0, f"{template_path.as_posix()}: registry YAML must be a map"))

    template_version = _registry_int(template_map.get("version"), 0)
    template_schema_version = str(template_map.get("schema_version") or "")
    core = _parse_qa_type_entries(template_map.get("core", []), "core", issues)

    instance_path = root / "qa_type_registry.yaml"
    source = "instance"
    registry_map: dict[str, Any] = {}

    if instance_path.exists():
        instance_data, instance_issues = _read_registry_yaml(instance_path)
        issues.extend(instance_issues)
        if isinstance(instance_data, dict):
            registry_map = instance_data
            _validate_instance_qa_core_entries(registry_map.get("core"), core, issues)
        elif instance_data is not None:
            issues.append(ValidationIssue("ERROR", 0, f"{instance_path.as_posix()}: registry YAML must be a map"))
    elif fallback_to_template:
        source = "template_fallback"
        registry_map = template_map
        issues.append(ValidationIssue("WARN", 0, "Instance registry 不存在，fallback Template"))
    else:
        source = "instance"
        issues.append(ValidationIssue("ERROR", 0, "Instance registry 不存在"))

    version = _registry_int(registry_map.get("version"), template_version)
    schema_version = str(registry_map.get("schema_version") or template_schema_version)
    user_extensions = _parse_qa_type_entries(registry_map.get("user_extensions", []), "user_extensions", issues)
    registry = QaTypeRegistry(
        version=version,
        schema_version=schema_version,
        core=core,
        user_extensions=user_extensions,
        source=source,
        issues=issues,
    )
    _validate_qa_user_extension_entries(user_extensions, core, root, issues, registry)

    return registry


def get_qa_type_registry(instance_root: str | Path = ".") -> QaTypeRegistry:
    return load_qa_type_registry(instance_root)


def validate_mode_tag(value: Any) -> ValidationIssue | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        return ValidationIssue("ERROR", 0, "mode_tag must be a non-empty string")
    if value not in VALID_MODE_TAGS:
        allowed = "/".join(sorted(VALID_MODE_TAGS))
        return ValidationIssue("ERROR", 0, f"mode_tag 值 '{value}' 不在允許集合 ({allowed}) 內")
    return None


def validate_frontmatter_qa_type(
    value: Any,
    registry: QaTypeRegistry | None = None,
) -> ValidationIssue | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        return ValidationIssue("ERROR", 0, "qa_type must be a non-empty string")

    resolved_registry = registry if registry is not None else load_qa_type_registry(".")
    if value not in resolved_registry.all_valid_qa_types():
        return ValidationIssue("ERROR", 0, f"未知 qa_type {value}")
    return None


def validate_qa_type(qa_type_value: str, registry: QaTypeRegistry) -> ValidationIssue | None:
    return validate_frontmatter_qa_type(qa_type_value, registry=registry)


def detect_qa_type_silent_drops(repo_root: str | Path, registry: QaTypeRegistry) -> list[ValidationIssue]:
    root = Path(repo_root)
    issues: list[ValidationIssue] = []

    for path in sorted(root.glob("**/*.md")):
        if not path.is_file() or ".git" in path.parts:
            continue
        parsed = parse_file(path, repo_root=root, qa_type_registry=registry)
        if not isinstance(parsed.yaml_data, dict):
            continue

        qa_type_value = parsed.yaml_data.get("qa_type")
        if not isinstance(qa_type_value, str) or not qa_type_value:
            continue
        if validate_qa_type(qa_type_value, registry) is None:
            continue

        rel_path = _index_rel_path(path, root)
        issues.append(
            ValidationIssue(
                "ERROR",
                parsed.yaml_start_line or 0,
                f"{rel_path}: 現存 QA qa_type {qa_type_value} 但 qa_type 已從 registry 移除",
            )
        )

    return issues


def validate_entity_id(entity_id: str, registry: EntityTypeRegistry) -> ValidationIssue | None:
    if not isinstance(entity_id, str) or not entity_id:
        return ValidationIssue("ERROR", 0, "entity ID must be a non-empty string")

    type_name, entry = _resolve_entity_type_entry(entity_id, registry)
    if entry is None:
        return ValidationIssue("ERROR", 0, f"未知 entity 類型 {type_name}")

    if entry.type == "A":
        subtype_issue = _validate_art_entity_subtype(entity_id, entry)
        if subtype_issue is not None:
            return subtype_issue

    if not entry.id_pattern_compiled.match(entity_id):
        return ValidationIssue("ERROR", 0, f"entity ID 格式不符: {entity_id}")

    return None


def detect_silent_drops(repo_root: str | Path, registry: EntityTypeRegistry) -> list[ValidationIssue]:
    root = Path(repo_root)
    issues: list[ValidationIssue] = []

    for path in sorted(root.glob("**/*.md")):
        if not path.is_file() or ".git" in path.parts:
            continue
        parsed = parse_file(path, repo_root=root)
        if not isinstance(parsed.yaml_data, dict):
            continue

        rel_path = _index_rel_path(path, root)
        line_num = parsed.yaml_start_line or 0
        for field_name in ("entities", "depends_on"):
            raw_values = parsed.yaml_data.get(field_name)
            if not isinstance(raw_values, list):
                continue
            for entity_id in raw_values:
                if not isinstance(entity_id, str):
                    continue
                type_name, entry = _resolve_entity_type_entry(entity_id, registry)
                if entry is not None:
                    continue
                issues.append(
                    ValidationIssue(
                        "ERROR",
                        line_num,
                        f"{rel_path}: 現存 {type_name}-* entity 但類型 {type_name} 已從 registry 移除",
                    )
                )

    return issues


def parse_dialogue_keys_map(
    parsed_markdown: ParsedMarkdown,
    *,
    art_metadata_index: set[str] | None = None,
    all_keys_set: set[str] | AllDialogueKeysIndex | None = None,
) -> DialogueKeysResult:
    """Parse and validate a single file's dialogue_keys map.

    `art_metadata_index` and `all_keys_set` are intentionally optional hooks for
    A.0.4 and A.0.3 cross-file validators. With both omitted, this function only
    performs the A.0.2 single-file checks.
    """
    resolved_all_keys_set = _coerce_all_keys_set(all_keys_set)
    issues: list[ValidationIssue] = []
    body_key_order, body_key_lines, body_art_comments, body_issues = _parse_body_dialogue_comments(parsed_markdown)
    issues.extend(body_issues)

    result = DialogueKeysResult(
        entries={},
        body_key_order=body_key_order,
        body_key_lines=body_key_lines,
        body_art_comments=body_art_comments,
        issues=issues,
    )

    yaml_data = parsed_markdown.yaml_data
    if not isinstance(yaml_data, dict):
        if body_key_order:
            issues.append(ValidationIssue("ERROR", 0, "dialogue_keys missing: body KEY comments require frontmatter map"))
        return result

    raw_dialogue_keys = yaml_data.get("dialogue_keys")
    if raw_dialogue_keys is None:
        if body_key_order:
            issues.append(ValidationIssue("ERROR", parsed_markdown.yaml_start_line or 0, "dialogue_keys missing: body KEY comments require frontmatter map"))
        return result
    if not isinstance(raw_dialogue_keys, dict):
        issues.append(ValidationIssue("ERROR", parsed_markdown.yaml_start_line or 0, "dialogue_keys must be a map"))
        return result

    entry_line_nums = _dialogue_key_entry_line_nums(parsed_markdown)
    mode_tag = yaml_data.get("mode_tag")
    for map_key, raw_entry in raw_dialogue_keys.items():
        key = str(map_key)
        line_num = entry_line_nums.get(key, parsed_markdown.yaml_start_line or 0)
        entry = _parse_dialogue_key_entry(
            key,
            raw_entry,
            line_num,
            mode_tag=mode_tag,
            art_metadata_index=art_metadata_index,
            all_keys_set=resolved_all_keys_set,
            issues=issues,
        )
        result.entries[key] = entry

    _validate_body_key_consistency(result.entries, body_key_order, body_key_lines, issues)
    _validate_art_comment_consistency(result.entries, body_art_comments, body_key_lines, issues)
    return result


def parse_body_art_references(parsed_markdown: ParsedMarkdown) -> BodyArtRefResult:
    """Parse view-layer A-* art HTML comments associated with body KEY comments."""
    refs: list[BodyArtReference] = []
    issues: list[ValidationIssue] = []
    lines = _source_lines(parsed_markdown)
    start_idx = parsed_markdown.yaml_end_line or 0
    pending_key: str | None = None

    for idx in range(start_idx, len(lines)):
        line_no = idx + 1
        line = lines[idx]

        for key_match in KEY_COMMENT_RE.finditer(line):
            pending_key = key_match.group(1).strip()

        for art_match in ART_COMMENT_RE.finditer(line):
            art_type = _canonical_art_comment_type(art_match.group(1))
            asset_id = art_match.group(2).strip()

            if pending_key is None:
                issues.append(
                    ValidationIssue(
                        "WARN",
                        line_no,
                        f"內文 art comment 必須在 KEY comment 後: {art_type}:{asset_id}",
                    )
                )
                continue
            if not asset_id.startswith("A-"):
                issues.append(
                    ValidationIssue(
                        "WARN",
                        line_no,
                        f"內文 art comment asset_id 必須使用 A-*：{asset_id}",
                    )
                )
                continue

            refs.append(
                BodyArtReference(
                    associated_key=pending_key,
                    art_type=art_type,
                    asset_id=asset_id,
                    line_in_file=line_no,
                )
            )

        if HTML_COMMENT_RE.sub("", line).strip():
            pending_key = None

    return BodyArtRefResult(refs=refs, issues=issues)


def validate_body_vs_frontmatter_consistency(
    parsed_markdown: ParsedMarkdown,
    dialogue_keys_result: DialogueKeysResult,
    art_index: ArtMetadataIndex | None = None,
) -> list[ValidationIssue]:
    """Validate view-layer body art hints against frontmatter dialogue_keys authority."""
    body_refs_result = parse_body_art_references(parsed_markdown)
    issues = list(body_refs_result.issues)
    depends_on_assets = _frontmatter_depends_on_asset_ids(parsed_markdown)

    seen_consistency: set[tuple[str, str, str, str]] = set()
    for ref in body_refs_result.refs:
        entry = dialogue_keys_result.entries.get(ref.associated_key)
        if entry is None:
            continue
        _validate_body_ref_against_dialogue_entry(ref, entry, issues, seen_consistency)

    seen_dependency: set[tuple[str, str, str]] = set()
    for ref in body_refs_result.refs:
        _validate_declared_asset_dependency(
            ref.asset_id,
            depends_on_assets,
            ref.line_in_file,
            f"內文 KEY '{ref.associated_key}'",
            issues,
            seen_dependency,
        )
        _validate_historical_asset_alias(
            ref.asset_id,
            ref.line_in_file,
            f"內文 KEY '{ref.associated_key}'",
            art_index,
            issues,
        )

    for entry in dialogue_keys_result.entries.values():
        for asset_id in _dialogue_entry_asset_ids(entry):
            _validate_declared_asset_dependency(
                asset_id,
                depends_on_assets,
                entry.line_num,
                f"frontmatter dialogue_keys.{entry.map_key}",
                issues,
                seen_dependency,
            )
            _validate_historical_asset_alias(
                asset_id,
                entry.line_num,
                f"frontmatter dialogue_keys.{entry.map_key}",
                art_index,
                issues,
            )

    return issues


def build_all_dialogue_keys_index(repo_root: str | Path) -> AllDialogueKeysIndex:
    """Build the repo-wide dialogue KEY/alias set and reverse indexes."""
    root = Path(repo_root)
    dialogue_root = root / "08_dialogue_outputs"
    index = AllDialogueKeysIndex()
    parsed_files: list[tuple[str, ParsedMarkdown]] = []
    conflict_issues: list[ValidationIssue] = []

    for path in sorted(dialogue_root.glob("**/*.md")):
        if not path.is_file():
            continue
        rel_path = _index_rel_path(path, root)
        parsed = parse_file(path, repo_root=root)
        first_pass = parse_dialogue_keys_map(parsed)
        parsed_files.append((rel_path, parsed))
        _add_dialogue_result_to_index(index, rel_path, first_pass, conflict_issues)

    index.issues.extend(conflict_issues)

    for rel_path, parsed in parsed_files:
        result = parse_dialogue_keys_map(parsed, all_keys_set=index)
        index.file_results[rel_path] = result
        index.issues.extend(_issues_with_path(rel_path, parsed.issues))
        index.issues.extend(_issues_with_path(rel_path, result.issues))

    return index


def parse_art_metadata(
    parsed_markdown: ParsedMarkdown,
    *,
    entity_registry: EntityTypeRegistry | None = None,
    known_entity_ids: set[str] | None = None,
    all_keys_set: set[str] | AllDialogueKeysIndex | None = None,
) -> ArtMetadataResult:
    """Parse and validate one file's art_metadata list.

    `entity_registry`, `known_entity_ids`, and `all_keys_set` are optional
    cross-file hooks. With them omitted, this stays a single-file parser.
    """
    issues: list[ValidationIssue] = []
    result = ArtMetadataResult(entries=[], issues=issues)
    yaml_data = parsed_markdown.yaml_data
    if not isinstance(yaml_data, dict):
        return result

    raw_art_metadata = yaml_data.get("art_metadata")
    if raw_art_metadata is None:
        return result
    if not isinstance(raw_art_metadata, list):
        issues.append(ValidationIssue("ERROR", parsed_markdown.yaml_start_line or 0, "art_metadata must be a list"))
        return result

    allowed_subtypes, reserved_subtypes, _art_entry = _art_subtype_sets(entity_registry)
    resolved_all_keys_set = _coerce_all_keys_set(all_keys_set)
    entry_line_nums = _art_metadata_entry_line_nums(parsed_markdown)
    source_file = parsed_markdown.path or ""

    for idx, raw_entry in enumerate(raw_art_metadata):
        line_num = entry_line_nums[idx] if idx < len(entry_line_nums) else parsed_markdown.yaml_start_line or 0
        entry = _parse_art_metadata_entry(
            raw_entry,
            idx,
            source_file,
            line_num,
            allowed_subtypes=allowed_subtypes,
            reserved_subtypes=reserved_subtypes,
            entity_registry=entity_registry,
            known_entity_ids=known_entity_ids,
            all_keys_set=resolved_all_keys_set,
            issues=issues,
        )
        if entry is not None:
            result.entries.append(entry)

    return result


def build_art_metadata_index(
    repo_root: str | Path,
    entity_registry: EntityTypeRegistry,
    qa_registry: QaTypeRegistry | None = None,
    all_keys_set: set[str] | AllDialogueKeysIndex | None = None,
) -> ArtMetadataIndex:
    """Build the repo-wide A-* art metadata index from 10_art_assets/**/*.md."""
    del qa_registry  # Reserved A.0.8 hook; A.0.4 has no qa_type behavior.

    root = Path(repo_root)
    art_root = root / "10_art_assets"
    index = ArtMetadataIndex(
        by_subtype={subtype: [] for subtype in _art_allowed_subtypes(entity_registry)},
    )

    if not art_root.is_dir():
        return index

    art_entry = entity_registry.get_entry("A")
    if art_entry is None:
        index.issues.append(ValidationIssue("ERROR", 0, "entity_type_registry missing A entry"))
        return index

    known_entity_ids = _collect_repo_entity_ids(root)
    resolved_all_keys_set = _coerce_all_keys_set(all_keys_set)
    conflict_issues: list[ValidationIssue] = []

    for path in sorted(art_root.glob("**/*.md")):
        if not path.is_file():
            continue
        rel_path = _index_rel_path(path, root)
        index.files_scanned.append(rel_path)
        parsed = parse_file(path, repo_root=root)
        result = parse_art_metadata(
            parsed,
            entity_registry=entity_registry,
            known_entity_ids=known_entity_ids,
            all_keys_set=resolved_all_keys_set,
        )
        index.issues.extend(_issues_with_path(rel_path, parsed.issues))
        index.issues.extend(_issues_with_path(rel_path, result.issues))

        for entry in result.entries:
            _add_art_entry_to_index(index, entry, conflict_issues)

    index.issues.extend(conflict_issues)
    return index


def compute_asset_missing_count(art_index: ArtMetadataIndex, body_refs_aggregated: Any) -> dict[str, int]:
    """Count referenced A-* IDs that are absent from current art metadata by subtype."""
    subtype_keys = list(ART_SUBTYPE_ORDER)
    missing_by_subtype: dict[str, set[str]] = {subtype: set() for subtype in subtype_keys}

    for asset_id in _iter_aggregated_asset_ids(body_refs_aggregated):
        if not isinstance(asset_id, str) or not asset_id.startswith("A-"):
            continue
        if asset_id in art_index.by_asset_id:
            continue
        subtype = _asset_subtype_from_id(asset_id)
        if subtype not in missing_by_subtype:
            missing_by_subtype[subtype] = set()
        missing_by_subtype[subtype].add(asset_id)

    return {subtype: len(asset_ids) for subtype, asset_ids in missing_by_subtype.items()}


def get_asset_completeness_by_subtype(
    index: ArtMetadataIndex,
    body_refs_index: Any = None,
) -> dict[str, CompletenessStats]:
    """Return D-045 asset-panel completeness by subtype, independent of narrative /status."""
    subtype_keys = list(ART_SUBTYPE_ORDER)
    for subtype in sorted(index.by_subtype):
        if subtype not in subtype_keys:
            subtype_keys.append(subtype)
    missing_counts = compute_asset_missing_count(index, body_refs_index) if body_refs_index is not None else {}
    for subtype in sorted(missing_counts):
        if subtype not in subtype_keys:
            subtype_keys.append(subtype)

    stats: dict[str, CompletenessStats] = {}
    for subtype in subtype_keys:
        entries = index.by_subtype.get(subtype, [])
        completed = 0
        in_progress = 0
        not_started = 0
        score = 0.0

        for entry in entries:
            completeness = _asset_entry_completion_pct(entry)
            if completeness >= 100:
                completed += 1
            elif completeness >= 50:
                in_progress += 1
            else:
                not_started += 1
            score += completeness

        missing = missing_counts.get(subtype, 0)
        total = len(entries)
        denominator = total + missing
        coverage_pct = round(score / denominator, 2) if denominator else 0.0
        stats[subtype] = CompletenessStats(
            subtype=subtype,
            total=total,
            completed=completed,
            in_progress=in_progress,
            not_started=not_started,
            missing=missing,
            coverage_pct=coverage_pct,
        )

    return stats


def _validate_dialogue_files_with_art_index(
    parsed_files: list[ParsedMarkdown],
    all_dialogue_keys: AllDialogueKeysIndex,
    art_metadata_index: ArtMetadataIndex,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    known_asset_ids = art_metadata_index.all_asset_ids

    for parsed in parsed_files:
        rel_path = parsed.path or ""
        if not rel_path or _is_export_record_excluded(rel_path):
            continue
        if not _has_dialogue_keys_map(parsed):
            continue

        result = parse_dialogue_keys_map(
            parsed,
            art_metadata_index=known_asset_ids,
            all_keys_set=all_dialogue_keys,
        )
        all_dialogue_keys.file_results[rel_path] = result
        issues.extend(_issues_with_path(rel_path, result.issues))

        consistency_issues = validate_body_vs_frontmatter_consistency(
            parsed,
            result,
            art_metadata_index,
        )
        issues.extend(_issues_with_path(rel_path, consistency_issues))

    return issues


def _has_dialogue_keys_map(parsed_markdown: ParsedMarkdown) -> bool:
    yaml_data = parsed_markdown.yaml_data
    return isinstance(yaml_data, dict) and "dialogue_keys" in yaml_data


def _validate_frontmatter_entity_id_fields(
    parsed_markdown: ParsedMarkdown,
    registry: EntityTypeRegistry,
) -> list[ValidationIssue]:
    yaml_data = parsed_markdown.yaml_data
    if not isinstance(yaml_data, dict):
        return []

    issues: list[ValidationIssue] = []
    for field_name in ("entities", "depends_on"):
        raw_values = yaml_data.get(field_name)
        if not isinstance(raw_values, list):
            continue

        line_num = _frontmatter_field_line_num(parsed_markdown, field_name)
        for entity_id in raw_values:
            if not isinstance(entity_id, str):
                continue
            issue = validate_entity_id(entity_id, registry)
            if issue is not None:
                issues.append(
                    ValidationIssue(
                        issue.severity,
                        line_num,
                        f"{field_name}: {issue.message}",
                    )
                )

    return issues


def _frontmatter_field_line_num(parsed_markdown: ParsedMarkdown, field_name: str) -> int:
    if parsed_markdown.yaml_start_line is None:
        return 0

    lines = _source_lines(parsed_markdown)
    start_idx = parsed_markdown.yaml_start_line
    end_idx = parsed_markdown.yaml_end_line - 1 if parsed_markdown.yaml_end_line is not None else len(lines)
    pattern = re.compile(rf"^\s*{re.escape(field_name)}\s*:")

    for idx in range(start_idx, min(end_idx, len(lines))):
        if pattern.match(_strip_inline_comment(lines[idx])):
            return idx + 1

    return parsed_markdown.yaml_start_line or 0


def _dedupe_validation_issues(issues: list[ValidationIssue]) -> list[ValidationIssue]:
    deduped: list[ValidationIssue] = []
    seen: set[tuple[int, str]] = set()

    for issue in issues:
        key = (issue.line_num, issue.message)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(issue)

    return deduped


def build_repo_index(repo_root: str | Path) -> RepoIndex:
    """Scan one Instance root and assemble the Phase A.0 parser indexes."""
    root = Path(repo_root)
    entity_registry = load_entity_type_registry(root)
    qa_registry = load_qa_type_registry(root)

    all_files_parsed: list[ParsedMarkdown] = []
    for path in _iter_repo_markdown_files(root):
        all_files_parsed.append(parse_file(path, repo_root=root, qa_type_registry=qa_registry))

    all_dialogue_keys = build_all_dialogue_keys_index(root)
    art_metadata_index = build_art_metadata_index(
        root,
        entity_registry,
        qa_registry,
        all_dialogue_keys,
    )
    dialogue_integration_issues = _validate_dialogue_files_with_art_index(
        all_files_parsed,
        all_dialogue_keys,
        art_metadata_index,
    )

    body_art_refs: dict[str, BodyArtRefResult] = {}
    body_ref_issues: list[ValidationIssue] = []
    for parsed in all_files_parsed:
        rel_path = parsed.path or ""
        if not rel_path or _is_export_record_excluded(rel_path):
            continue
        ref_result = parse_body_art_references(parsed)
        body_art_refs[rel_path] = ref_result
        body_ref_issues.extend(_issues_with_path(rel_path, ref_result.issues))

    phase_log_result = _parse_repo_phase_log(root)

    issues: list[ValidationIssue] = []
    issues.extend(entity_registry.issues)
    issues.extend(qa_registry.issues)
    for parsed in all_files_parsed:
        rel_path = parsed.path or ""
        issues.extend(_issues_with_path(rel_path, parsed.issues) if rel_path else parsed.issues)
        entity_ref_issues = _validate_frontmatter_entity_id_fields(parsed, entity_registry)
        issues.extend(_issues_with_path(rel_path, entity_ref_issues) if rel_path else entity_ref_issues)
    issues.extend(all_dialogue_keys.issues)
    issues.extend(art_metadata_index.issues)
    issues.extend(dialogue_integration_issues)
    issues.extend(body_ref_issues)
    issues.extend(phase_log_result.issues)
    issues = _dedupe_validation_issues(issues)

    return RepoIndex(
        entity_registry=entity_registry,
        qa_registry=qa_registry,
        all_files_parsed=all_files_parsed,
        all_dialogue_keys=all_dialogue_keys,
        art_metadata_index=art_metadata_index,
        body_art_refs=body_art_refs,
        phase_log_result=phase_log_result,
        issues=issues,
        repo_root=root.resolve().as_posix(),
    )


def get_all_entities(repo_index: RepoIndex) -> list[EntityRecord]:
    """Return DF §9.4 entity records from parsed markdown data files."""
    records: list[EntityRecord] = []
    for parsed in repo_index.all_files_parsed:
        rel_path = parsed.path or ""
        if not _is_export_entity_source(parsed):
            continue
        yaml_data = parsed.yaml_data if isinstance(parsed.yaml_data, dict) else {}
        art_metadata = yaml_data.get("art_metadata")
        records.append(
            EntityRecord(
                source_file=rel_path,
                header={field_name: parsed.header.get(field_name) for field_name in REQUIRED_HEADER_FIELDS},
                frontmatter={field_name: yaml_data.get(field_name) for field_name in UPSTREAM_FIELDS},
                body=_markdown_body_text(parsed),
                downstream_fields={field_name: yaml_data.get(field_name) for field_name in DOWNSTREAM_FIELDS},
                art_metadata=_raw_art_metadata_export(art_metadata),
            )
        )

    return sorted(records, key=lambda record: record.source_file)


def get_all_dialogue_lines(repo_index: RepoIndex, include_deleted: bool = False) -> list[DialogueLineRecord]:
    """Return DF §9.5 dialogue_line records, sorted by (scene_id, line_index)."""
    parsed_by_path = {
        parsed.path: parsed
        for parsed in repo_index.all_files_parsed
        if parsed.path is not None
    }
    records: list[DialogueLineRecord] = []

    for rel_path, dialogue_result in repo_index.all_dialogue_keys.file_results.items():
        if _is_export_record_excluded(rel_path):
            continue
        parsed = parsed_by_path.get(rel_path)
        yaml_data = parsed.yaml_data if parsed is not None and isinstance(parsed.yaml_data, dict) else {}
        scene_id = yaml_data.get("scene_id")

        for key, entry in dialogue_result.entries.items():
            if entry.status == "deleted" and not include_deleted:
                continue
            records.append(
                DialogueLineRecord(
                    source_file=rel_path,
                    key=key,
                    line_index=entry.line_index or 0,
                    speaker=entry.speaker,
                    aliases=list(entry.aliases),
                    portrait=entry.portrait,
                    bgm=entry.bgm,
                    sfx=list(entry.sfx),
                    status=entry.status,
                    created_at=_export_optional_string(entry.created_at) or "",
                    renamed_at=_export_optional_string(entry.renamed_at),
                    deleted_at=_export_optional_string(entry.deleted_at),
                    deprecated_reason=entry.deprecated_reason if isinstance(entry.deprecated_reason, str) else None,
                    source_keys=list(entry.source_keys) if entry.source_keys is not None else None,
                    content=_extract_dialogue_content(parsed, key) if parsed is not None else None,
                    in_scene_context={"scene_id": scene_id},
                )
            )

    return sorted(records, key=lambda record: (str(record.in_scene_context.get("scene_id") or ""), record.line_index, record.key))


def get_all_art_metadata(repo_index: RepoIndex) -> list[ArtMetadataRecord]:
    """Return DF §9.6 art_metadata records, sorted by (subtype, asset_id)."""
    records = [
        ArtMetadataRecord(
            source_file=entry.source_file,
            asset_id=entry.asset_id,
            display_name=entry.display_name,
            subtype=entry.subtype,
            owner=entry.owner,
            state_tags=list(entry.state_tags),
            aliases=list(entry.aliases),
            dialogue_keys_ref=entry.dialogue_keys_ref,
            created_at=entry.created_at,
            renamed_at=entry.renamed_at,
            deleted_at=entry.deleted_at,
            status=entry.status,
            deprecated_reason=entry.deprecated_reason,
        )
        for entry in repo_index.art_metadata_index.by_asset_id.values()
        if not _is_export_record_excluded(entry.source_file)
    ]
    return sorted(records, key=lambda record: (record.subtype, record.asset_id))


def get_manifest_snapshot(
    repo_index: RepoIndex,
    *,
    exported_at: str = "",
    tool_version: str = EXPORT_TOOL_VERSION,
) -> ManifestSnapshot:
    """Return the DF §9.2 manifest snapshot for an export caller."""
    stats = _export_stats(repo_index)
    repo_root = Path(repo_index.repo_root) if repo_index.repo_root else Path(".")
    return ManifestSnapshot(
        export_version=EXPORT_SCHEMA_VERSION,
        exported_at=exported_at,
        tool_version=tool_version,
        instance_id=repo_root.name,
        spec_version=DATA_FORMAT_SPEC_VERSION,
        stats=stats,
        entity_type_registry=_entity_registry_snapshot(repo_index.entity_registry),
        qa_type_registry=_qa_type_registry_snapshot(repo_index.qa_registry),
    )


def get_scope_counts(
    repo_index: RepoIndex,
    scope: str = "full",
    scene_id: str | None = None,
) -> dict[str, Any]:
    """Return export prompt metadata counts for full / outline_only / scene scopes."""
    if scope == "full":
        entities = get_all_entities(repo_index)
        dialogue_lines = get_all_dialogue_lines(repo_index)
        art_metadata = get_all_art_metadata(repo_index)
        return _scope_count_payload(scope, entities, dialogue_lines, art_metadata)

    if scope == "outline_only":
        entities = [
            record
            for record in get_all_entities(repo_index)
            if _record_matches_outline_scope(record)
        ]
        return _scope_count_payload(scope, entities, [], [])

    if scope == "scene":
        if not scene_id:
            raise ValueError("scene_id is required when scope='scene'")
        return _scene_scope_counts(repo_index, scene_id)

    raise ValueError("scope must be one of: full, outline_only, scene")


def _iter_repo_markdown_files(repo_root: Path):
    for path in sorted(repo_root.glob("**/*.md")):
        if not path.is_file() or ".git" in path.parts:
            continue
        # _source_materials/ holds raw user source materials, not entities;
        # exclude the whole subtree from the repo-wide entity scan.
        if any(part in SOURCE_MATERIAL_DIR_NAMES for part in path.parts):
            continue
        yield path


def _parse_repo_phase_log(repo_root: Path) -> PhaseLogResult:
    phase_log_path = repo_root / ".protocol_version"
    if not phase_log_path.exists():
        return PhaseLogResult(entries=[])
    try:
        content = phase_log_path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError as exc:
        return PhaseLogResult(entries=[], issues=[ValidationIssue("ERROR", 0, f".protocol_version: cannot read file: {exc}")])
    return parse_phase_log_text(content)


def _is_export_record_excluded(rel_path: str) -> bool:
    normalized = rel_path.replace("\\", "/")
    parts = [part for part in normalized.split("/") if part]
    if not parts:
        return True
    if len(parts) == 1:
        return True
    if parts[0] in EXPORT_EXCLUDED_RECORD_DIRS:
        return True
    return parts[-1].startswith("00_") and parts[-1].endswith(".md")


def _is_export_entity_source(parsed: ParsedMarkdown) -> bool:
    rel_path = parsed.path or ""
    if not rel_path or _is_export_record_excluded(rel_path):
        return False
    return all(parsed.header.get(field_name) is not None for field_name in REQUIRED_HEADER_FIELDS)


def _raw_art_metadata_export(raw_art_metadata: Any) -> list[dict[str, Any]] | None:
    if not isinstance(raw_art_metadata, list):
        return None
    exported: list[dict[str, Any]] = []
    for raw_entry in raw_art_metadata:
        if not isinstance(raw_entry, dict):
            continue
        exported.append(
            {
                key: value
                for key, value in raw_entry.items()
                if key not in ART_FORBIDDEN_FIELDS and not str(key).startswith("base64_")
            }
        )
    return exported


def _markdown_body_text(parsed: ParsedMarkdown) -> str:
    lines = _source_lines(parsed)
    start_idx = parsed.yaml_end_line if parsed.yaml_end_line is not None else _header_body_start_idx(lines)
    return "\n".join(lines[start_idx:]).lstrip("\n")


def _header_body_start_idx(lines: list[str]) -> int:
    header_end_idx = 0
    patterns = {
        field_name: re.compile(rf"^\s*{re.escape(field_name)}\s*[:：]\s*(.+?)\s*$")
        for field_name in REQUIRED_HEADER_FIELDS
    }
    for idx, line in enumerate(lines[:HEAD_LINES], start=1):
        if any(pattern.match(line) for pattern in patterns.values()):
            header_end_idx = idx
    return header_end_idx


def _extract_dialogue_content(parsed: ParsedMarkdown, key: str) -> str | None:
    lines = _source_lines(parsed)
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
            return _strip_dialogue_content_markup(stripped)
        return None
    return None


def _strip_dialogue_content_markup(text: str) -> str:
    result = text.strip()
    result = re.sub(r"^\s*(?:[-*]\s*)?(?:\*\*|__)[^*_：:]{1,80}[：:](?:\*\*|__)\s*", "", result)
    result = re.sub(r"(\*\*|__)(.*?)\1", r"\2", result)
    result = re.sub(r"(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)", r"\1", result)
    result = re.sub(r"(?<!_)_(?!_)(.*?)(?<!_)_(?!_)", r"\1", result)
    return result.strip()


def _export_optional_string(value: Any) -> str | None:
    if value is None:
        return None
    isoformat = getattr(value, "isoformat", None)
    if callable(isoformat):
        return str(isoformat())
    return str(value)


def _entity_registry_snapshot(registry: EntityTypeRegistry) -> dict[str, Any]:
    return {
        "version": registry.version,
        "schema_version": registry.schema_version,
        "source": registry.source,
        "reserved_prefixes": list(registry.reserved_prefixes),
        "core": {
            type_name: _entity_type_entry_snapshot(entry)
            for type_name, entry in sorted(registry.core.items())
        },
        "user_extensions": {
            type_name: _entity_type_entry_snapshot(entry)
            for type_name, entry in sorted(registry.user_extensions.items())
        },
    }


def _entity_type_entry_snapshot(entry: EntityTypeEntry) -> dict[str, Any]:
    return {
        "type": entry.type,
        "description": entry.description,
        "id_pattern": entry.id_pattern,
        "target_dir": entry.target_dir,
        "cross_ref_allowed": entry.cross_ref_allowed,
        "locked": entry.locked,
        "subtype_allowed": list(entry.subtype_allowed) if entry.subtype_allowed is not None else None,
        "subtype_reserved": list(entry.subtype_reserved) if entry.subtype_reserved is not None else None,
    }


def _qa_type_registry_snapshot(registry: QaTypeRegistry) -> dict[str, Any]:
    return {
        "version": registry.version,
        "schema_version": registry.schema_version,
        "source": registry.source,
        "core": {
            qa_type: _qa_type_entry_snapshot(entry)
            for qa_type, entry in sorted(registry.core.items())
        },
        "user_extensions": {
            qa_type: _qa_type_entry_snapshot(entry)
            for qa_type, entry in sorted(registry.user_extensions.items())
        },
    }


def _qa_type_entry_snapshot(entry: QaTypeEntry) -> dict[str, Any]:
    return {
        "qa_type": entry.qa_type,
        "description": entry.description,
        "template_path": entry.template_path,
        "locked": entry.locked,
    }


def _export_stats(repo_index: RepoIndex) -> dict[str, Any]:
    entities = get_all_entities(repo_index)
    dialogue_lines = get_all_dialogue_lines(repo_index)
    art_metadata = get_all_art_metadata(repo_index)
    return {
        "total_entities": len(entities),
        "total_dialogue_lines": len(dialogue_lines),
        "total_art_assets": len(art_metadata),
        "by_entity_type": _entity_type_counts_from_records(entities),
    }


def _entity_type_counts_from_records(records: list[EntityRecord]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        for entity_id in _entity_ids_from_record(record):
            entity_type = _entity_type_from_id(entity_id)
            counts[entity_type] = counts.get(entity_type, 0) + 1
    return dict(sorted(counts.items()))


def _entity_ids_from_record(record: EntityRecord) -> list[str]:
    entities = record.frontmatter.get("entities")
    if not isinstance(entities, list):
        return []
    return [entity_id for entity_id in entities if isinstance(entity_id, str)]


def _depends_on_ids_from_record(record: EntityRecord) -> list[str]:
    depends_on = record.frontmatter.get("depends_on")
    if not isinstance(depends_on, list):
        return []
    return [entity_id for entity_id in depends_on if isinstance(entity_id, str)]


def _entity_type_from_id(entity_id: str) -> str:
    """Map an entity ID to its type name via the registry (no hardcoded mirror).

    Resolves against the module-cached registry; falls back to the leading
    prefix for IDs whose type is absent from the registry (same behavior the
    previous hardcoded fallback gave for unknown prefixes).
    """
    type_name, _entry = _resolve_entity_type_entry(entity_id, _module_entity_type_registry())
    return type_name


def _record_matches_outline_scope(record: EntityRecord) -> bool:
    outline_types = _outline_entity_types()
    return any(_entity_type_from_id(entity_id) in outline_types for entity_id in _entity_ids_from_record(record))


def _scope_count_payload(
    scope: str,
    entities: list[EntityRecord],
    dialogue_lines: list[DialogueLineRecord],
    art_metadata: list[ArtMetadataRecord],
) -> dict[str, Any]:
    return {
        "scope": scope,
        "total_entities": len(entities),
        "total_dialogue_lines": len(dialogue_lines),
        "total_art_assets": len(art_metadata),
        "total_records": len(entities) + len(dialogue_lines) + len(art_metadata),
        "by_entity_type": _entity_type_counts_from_records(entities),
    }


def _scene_scope_counts(repo_index: RepoIndex, scene_id: str) -> dict[str, Any]:
    all_entities = get_all_entities(repo_index)
    scene_dialogue_lines = [
        record
        for record in get_all_dialogue_lines(repo_index)
        if record.in_scene_context.get("scene_id") == scene_id
    ]

    dependency_ids: set[str] = {scene_id}
    for record in all_entities:
        record_entities = set(_entity_ids_from_record(record))
        if scene_id in record_entities or record.downstream_fields.get("scene_id") == scene_id:
            dependency_ids.update(record_entities)
            dependency_ids.update(_depends_on_ids_from_record(record))

    for dialogue_record in scene_dialogue_lines:
        if dialogue_record.portrait:
            dependency_ids.add(dialogue_record.portrait)
        if dialogue_record.bgm:
            dependency_ids.add(dialogue_record.bgm)
        dependency_ids.update(dialogue_record.sfx)

    scene_entities = [
        record
        for record in all_entities
        if record.downstream_fields.get("scene_id") == scene_id
        or bool(set(_entity_ids_from_record(record)) & dependency_ids)
    ]
    scene_art_metadata = [
        record
        for record in get_all_art_metadata(repo_index)
        if record.asset_id in dependency_ids or bool(set(record.aliases) & dependency_ids)
    ]

    payload = _scope_count_payload("scene", scene_entities, scene_dialogue_lines, scene_art_metadata)
    payload["scene_id"] = scene_id
    payload["depends_on_count"] = len(dependency_ids - {scene_id})
    return payload


def _coerce_all_keys_set(all_keys_source: set[str] | AllDialogueKeysIndex | None) -> set[str] | None:
    if isinstance(all_keys_source, AllDialogueKeysIndex):
        return all_keys_source.all_keys_set
    return all_keys_source


def _canonical_art_comment_type(label: str) -> str:
    upper_label = label.upper()
    if upper_label in {"BGM", "SFX"}:
        return upper_label
    if label.lower().startswith("a-"):
        return label.lower()
    return label


def _frontmatter_depends_on_asset_ids(parsed_markdown: ParsedMarkdown) -> set[str]:
    yaml_data = parsed_markdown.yaml_data
    if not isinstance(yaml_data, dict):
        return set()
    depends_on = yaml_data.get("depends_on")
    if not isinstance(depends_on, list):
        return set()
    return {item for item in depends_on if isinstance(item, str) and item.startswith("A-")}


def _dialogue_entry_asset_ids(entry: DialogueKeyEntry) -> list[str]:
    asset_ids: list[str] = []
    if entry.portrait:
        asset_ids.append(entry.portrait)
    if entry.bgm:
        asset_ids.append(entry.bgm)
    asset_ids.extend(entry.sfx)
    return asset_ids


def _validate_body_ref_against_dialogue_entry(
    ref: BodyArtReference,
    entry: DialogueKeyEntry,
    issues: list[ValidationIssue],
    seen: set[tuple[str, str, str, str]],
) -> None:
    field_name = _art_comment_field_name(ref.art_type)
    if field_name is None or field_name == "bg":
        return

    issue_kind: str | None = None
    authority_value: Any = None
    if field_name in {"portrait", "bgm"}:
        authority_value = getattr(entry, field_name)
        if not authority_value:
            issue_kind = "missing"
        elif authority_value != ref.asset_id:
            issue_kind = "mismatch"
    elif field_name == "sfx":
        authority_value = entry.sfx
        if not entry.sfx:
            issue_kind = "missing"
        elif ref.asset_id not in entry.sfx:
            issue_kind = "mismatch"

    if issue_kind is None:
        return

    seen_key = (issue_kind, ref.associated_key, field_name, ref.asset_id)
    if seen_key in seen:
        return
    seen.add(seen_key)

    if issue_kind == "missing":
        issues.append(
            ValidationIssue(
                "WARN",
                ref.line_in_file,
                f"內文 art 提示無 frontmatter 對應: KEY '{ref.associated_key}' {ref.art_type} {ref.asset_id}",
            )
        )
        return

    issues.append(
        ValidationIssue(
            "WARN",
            ref.line_in_file,
            f"內文提示與 frontmatter 權威來源不符: KEY '{ref.associated_key}' {ref.art_type} {ref.asset_id} != {authority_value}",
        )
    )


def _validate_declared_asset_dependency(
    asset_id: str,
    depends_on_assets: set[str],
    line_num: int,
    source_label: str,
    issues: list[ValidationIssue],
    seen: set[tuple[str, str, str]],
) -> None:
    if not asset_id.startswith("A-") or asset_id in depends_on_assets:
        return
    seen_key = (source_label, asset_id, "depends_on")
    if seen_key in seen:
        return
    seen.add(seen_key)
    issues.append(
        ValidationIssue(
            "WARN",
            line_num,
            f"{source_label}: 內文/frontmatter 引用未宣告依賴 {asset_id}",
        )
    )


def _validate_historical_asset_alias(
    asset_id: str,
    line_num: int,
    source_label: str,
    art_index: ArtMetadataIndex | None,
    issues: list[ValidationIssue],
) -> None:
    if art_index is None:
        return
    current_id = art_index.alias_to_current.get(asset_id)
    if current_id is None or current_id == asset_id:
        return
    issues.append(
        ValidationIssue(
            "WARN",
            line_num,
            f"{source_label}: 引用歷史 alias，建議改用當前 ID {asset_id} -> {current_id}",
        )
    )


def _asset_subtype_from_id(asset_id: str) -> str:
    parts = asset_id.split("-", 2)
    if len(parts) >= 2 and parts[1]:
        return parts[1]
    return "unknown"


def _iter_aggregated_asset_ids(value: Any):
    if value is None:
        return
    if isinstance(value, str):
        if value.startswith("A-"):
            yield value
        return
    if isinstance(value, BodyArtRefResult):
        for ref in value.refs:
            yield ref.asset_id
        return
    if isinstance(value, BodyArtReference):
        yield value.asset_id
        return
    if isinstance(value, DialogueKeysResult):
        for entry in value.entries.values():
            yield from _dialogue_entry_asset_ids(entry)
        return
    if isinstance(value, DialogueKeyEntry):
        yield from _dialogue_entry_asset_ids(value)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str) and key.startswith("A-"):
                yield key
            yield from _iter_aggregated_asset_ids(item)
        return
    if isinstance(value, (list, tuple, set, frozenset)):
        for item in value:
            yield from _iter_aggregated_asset_ids(item)


def _add_dialogue_result_to_index(
    index: AllDialogueKeysIndex,
    rel_path: str,
    result: DialogueKeysResult,
    issues: list[ValidationIssue],
) -> None:
    for map_key, entry in result.entries.items():
        current_ref = (map_key, rel_path)
        duplicate_current_key = False

        existing_file = index.key_to_file_path.get(map_key)
        if existing_file is not None and existing_file != rel_path:
            duplicate_current_key = True
            issues.append(
                ValidationIssue(
                    "ERROR",
                    entry.line_num,
                    f"{rel_path}: cross-file dialogue KEY conflict: '{map_key}' appears in both {existing_file} and {rel_path}",
                )
            )
        elif existing_file is None:
            index.key_to_file_path[map_key] = rel_path

        existing_alias_ref = index.alias_to_current_key.get(map_key)
        if not duplicate_current_key and existing_alias_ref is not None and existing_alias_ref != current_ref:
            existing_key, existing_path = existing_alias_ref
            issues.append(
                ValidationIssue(
                    "ERROR",
                    entry.line_num,
                    f"{rel_path}: dialogue_keys.{map_key}: map key collides with alias in {existing_path} -> {existing_key}",
                )
            )

        index.all_keys_set.add(map_key)

        for alias in entry.aliases:
            index.all_keys_set.add(alias)

            key_file = index.key_to_file_path.get(alias)
            alias_is_own_current_key = key_file == rel_path and alias == map_key
            alias_is_duplicate_current_key = duplicate_current_key and alias == map_key
            collides_with_current_key = key_file is not None and not alias_is_own_current_key and not alias_is_duplicate_current_key
            if collides_with_current_key:
                issues.append(
                    ValidationIssue(
                        "ERROR",
                        entry.line_num,
                        f"{rel_path}: dialogue_keys.{map_key}: alias '{alias}' collides with current map key in {key_file}",
                    )
                )
                continue

            existing_alias_ref = index.alias_to_current_key.get(alias)
            if existing_alias_ref is not None and existing_alias_ref != current_ref:
                existing_key, existing_path = existing_alias_ref
                issues.append(
                    ValidationIssue(
                        "ERROR",
                        entry.line_num,
                        f"{rel_path}: dialogue_keys.{map_key}: alias '{alias}' also points to '{existing_key}' in {existing_path}",
                    )
                )
                continue

            if existing_alias_ref is None:
                index.alias_to_current_key[alias] = current_ref


def _parse_art_metadata_entry(
    raw_entry: Any,
    idx: int,
    source_file: str,
    line_num: int,
    *,
    allowed_subtypes: set[str],
    reserved_subtypes: set[str],
    entity_registry: EntityTypeRegistry | None,
    known_entity_ids: set[str] | None,
    all_keys_set: set[str] | None,
    issues: list[ValidationIssue],
) -> ArtMetadataEntry | None:
    prefix = f"art_metadata[{idx}]"
    if not isinstance(raw_entry, dict):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: entry must be a map"))
        return None

    _validate_art_forbidden_fields(raw_entry, prefix, line_num, issues)
    _validate_art_required_fields(raw_entry, prefix, line_num, issues)

    asset_id = _coerce_art_required_string(raw_entry.get("asset_id"), f"{prefix}.asset_id", line_num, issues)
    display_name = _coerce_art_required_string(raw_entry.get("display_name"), f"{prefix}.display_name", line_num, issues)
    subtype = _coerce_art_required_string(raw_entry.get("subtype"), f"{prefix}.subtype", line_num, issues)
    owner = _coerce_art_optional_string(raw_entry.get("owner"), f"{prefix}.owner", line_num, issues)
    state_tags = _parse_art_string_list(raw_entry.get("state_tags"), f"{prefix}.state_tags", line_num, issues, require_non_empty=False)
    aliases = _parse_art_string_list(raw_entry.get("aliases"), f"{prefix}.aliases", line_num, issues, require_non_empty=True)
    created_at = _coerce_art_required_string(raw_entry.get("created_at"), f"{prefix}.created_at", line_num, issues)
    renamed_at = _coerce_art_optional_string(raw_entry.get("renamed_at"), f"{prefix}.renamed_at", line_num, issues)
    deleted_at = _coerce_art_optional_string(raw_entry.get("deleted_at"), f"{prefix}.deleted_at", line_num, issues)
    status = _coerce_art_optional_string(raw_entry.get("status"), f"{prefix}.status", line_num, issues)
    deprecated_reason = _coerce_art_optional_string(raw_entry.get("deprecated_reason"), f"{prefix}.deprecated_reason", line_num, issues)
    dialogue_keys_ref = _coerce_art_optional_string(raw_entry.get("dialogue_keys_ref"), f"{prefix}.dialogue_keys_ref", line_num, issues)

    _validate_art_subtype_value(subtype, allowed_subtypes, reserved_subtypes, prefix, line_num, issues)
    _validate_art_asset_id(asset_id, subtype, entity_registry, prefix, line_num, issues)
    _validate_art_aliases(aliases, prefix, line_num, entity_registry, issues)
    _validate_art_status(status, prefix, line_num, issues)
    _validate_art_owner_and_voice_ref(
        subtype,
        owner,
        dialogue_keys_ref,
        prefix,
        line_num,
        known_entity_ids,
        all_keys_set,
        issues,
    )

    return ArtMetadataEntry(
        asset_id=asset_id,
        display_name=display_name,
        subtype=subtype,
        owner=owner,
        state_tags=state_tags,
        aliases=aliases,
        created_at=created_at,
        renamed_at=renamed_at,
        deleted_at=deleted_at,
        status=status,
        deprecated_reason=deprecated_reason,
        dialogue_keys_ref=dialogue_keys_ref,
        source_file=source_file,
    )


def _validate_art_forbidden_fields(
    raw_entry: dict[str, Any],
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    for field_name in raw_entry:
        if field_name in ART_FORBIDDEN_FIELDS or field_name.startswith("base64_"):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: forbidden art metadata field '{field_name}'"))


def _validate_art_required_fields(
    raw_entry: dict[str, Any],
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    for field_name in ART_REQUIRED_ERROR_FIELDS:
        if field_name not in raw_entry:
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: missing required field '{field_name}'"))
    if "owner" not in raw_entry:
        issues.append(ValidationIssue("WARN", line_num, f"{prefix}: missing owner"))


def _coerce_art_required_string(
    value: Any,
    label: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        if value:
            return value
        issues.append(ValidationIssue("ERROR", line_num, f"{label} must be a non-empty string"))
        return ""
    if isinstance(value, (int, float, bool, list, dict)):
        issues.append(ValidationIssue("ERROR", line_num, f"{label} must be a string"))
    return str(value)


def _coerce_art_optional_string(
    value: Any,
    label: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool, list, dict)):
        issues.append(ValidationIssue("ERROR", line_num, f"{label} must be a string or null"))
    return str(value)


def _parse_art_string_list(
    value: Any,
    label: str,
    line_num: int,
    issues: list[ValidationIssue],
    *,
    require_non_empty: bool,
) -> list[str]:
    if not isinstance(value, list):
        issues.append(ValidationIssue("ERROR", line_num, f"{label} must be a list"))
        return []
    if require_non_empty and not value:
        issues.append(ValidationIssue("ERROR", line_num, f"{label} must contain at least one value"))
        return []

    values: list[str] = []
    seen: set[str] = set()
    for item_idx, item in enumerate(value):
        if not isinstance(item, str) or not item:
            issues.append(ValidationIssue("ERROR", line_num, f"{label}[{item_idx}] must be a non-empty string"))
            continue
        if item in seen:
            issues.append(ValidationIssue("ERROR", line_num, f"{label}[{item_idx}] duplicates '{item}' in the same entry"))
            continue
        seen.add(item)
        values.append(item)
    return values


def _validate_art_subtype_value(
    subtype: str,
    allowed_subtypes: set[str],
    reserved_subtypes: set[str],
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    if not subtype:
        return
    if subtype in reserved_subtypes and subtype not in allowed_subtypes:
        issues.append(
            ValidationIssue(
                "ERROR",
                line_num,
                f"{prefix}: subtype '{subtype}' 在 reserved_subtypes；該 subtype 已預留但本輪不採",
            )
        )
        return
    if subtype not in allowed_subtypes:
        allowed = "/".join(sorted(allowed_subtypes))
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: 未知 A-* subtype '{subtype}' (allowed: {allowed})"))


def _validate_art_asset_id(
    asset_id: str,
    subtype: str,
    entity_registry: EntityTypeRegistry | None,
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    if not asset_id:
        return
    if not asset_id.startswith("A-"):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: asset_id must use A-* prefix"))
        return

    id_parts = asset_id.split("-", 3)
    id_subtype = id_parts[1] if len(id_parts) > 1 else ""
    if subtype and id_subtype and subtype != id_subtype:
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: asset_id subtype '{id_subtype}' differs from subtype '{subtype}'"))

    if entity_registry is None:
        if not re.match(r"^A-[^-]+-.+-.+$", asset_id):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: asset_id 格式不符: {asset_id}"))
        return

    issue = validate_entity_id(asset_id, entity_registry)
    if issue is not None:
        issues.append(ValidationIssue(issue.severity, line_num, f"{prefix}: {issue.message}"))


def _validate_art_aliases(
    aliases: list[str],
    prefix: str,
    line_num: int,
    entity_registry: EntityTypeRegistry | None,
    issues: list[ValidationIssue],
) -> None:
    for alias_idx, alias in enumerate(aliases):
        if not alias.startswith("A-"):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases[{alias_idx}] must use A-* prefix"))
            continue
        if entity_registry is None:
            if not re.match(r"^A-[^-]+-.+-.+$", alias):
                issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases[{alias_idx}] 格式不符: {alias}"))
            continue
        issue = validate_entity_id(alias, entity_registry)
        if issue is not None:
            issues.append(ValidationIssue(issue.severity, line_num, f"{prefix}: aliases[{alias_idx}] {issue.message}"))


def _validate_art_status(
    status: str | None,
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    if status is None:
        return
    if status not in VALID_ART_STATUSES:
        allowed = "/".join(sorted(VALID_ART_STATUSES))
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: status '{status}' is invalid (allowed: {allowed})"))


def _validate_art_owner_and_voice_ref(
    subtype: str,
    owner: str | None,
    dialogue_keys_ref: str | None,
    prefix: str,
    line_num: int,
    known_entity_ids: set[str] | None,
    all_keys_set: set[str] | None,
    issues: list[ValidationIssue],
) -> None:
    if subtype == "portrait":
        if not _owner_is_known_entity(owner, "C-", known_entity_ids):
            issues.append(ValidationIssue("WARN", line_num, f"{prefix}: 孤立立繪 owner '{owner}' 不對應 C-* entity"))
        return

    if subtype in {"bg", "cg"}:
        if owner == "global":
            return
        if not _owner_is_known_entity(owner, ("S-", "CH-"), known_entity_ids):
            issues.append(ValidationIssue("WARN", line_num, f"{prefix}: {subtype} owner '{owner}' 不對應 S-* / CH-* / global"))
        return

    if subtype == "voice":
        if not _owner_is_known_entity(owner, "C-", known_entity_ids):
            issues.append(ValidationIssue("WARN", line_num, f"{prefix}: voice owner '{owner}' 不對應 C-* entity"))
        if not dialogue_keys_ref:
            issues.append(ValidationIssue("WARN", line_num, f"{prefix}: voice subtype requires dialogue_keys_ref"))
        elif all_keys_set is not None and dialogue_keys_ref not in all_keys_set:
            issues.append(ValidationIssue("WARN", line_num, f"{prefix}: dialogue_keys_ref '{dialogue_keys_ref}' not found in all_keys_set"))


def _owner_is_known_entity(
    owner: str | None,
    prefixes: str | tuple[str, ...],
    known_entity_ids: set[str] | None,
) -> bool:
    if owner is None or owner == "":
        return False
    prefix_tuple = (prefixes,) if isinstance(prefixes, str) else prefixes
    if not owner.startswith(prefix_tuple):
        return False
    if known_entity_ids is not None and owner not in known_entity_ids:
        return False
    return True


def _add_art_entry_to_index(
    index: ArtMetadataIndex,
    entry: ArtMetadataEntry,
    issues: list[ValidationIssue],
) -> None:
    if not entry.asset_id:
        return

    existing = index.by_asset_id.get(entry.asset_id)
    if existing is not None:
        issues.append(
            ValidationIssue(
                "ERROR",
                0,
                f"{entry.source_file}: cross-file art asset_id conflict: '{entry.asset_id}' appears in both {existing.source_file} and {entry.source_file}",
            )
        )
    else:
        index.by_asset_id[entry.asset_id] = entry

    existing_alias_current = index.alias_to_current.get(entry.asset_id)
    if existing_alias_current is not None and existing_alias_current != entry.asset_id:
        existing_entry = index.by_asset_id.get(existing_alias_current)
        existing_path = existing_entry.source_file if existing_entry is not None else "<unknown>"
        issues.append(
            ValidationIssue(
                "ERROR",
                0,
                f"{entry.source_file}: asset_id '{entry.asset_id}' collides with alias in {existing_path} -> {existing_alias_current}",
            )
        )

    index.by_subtype.setdefault(entry.subtype, []).append(entry)
    if entry.owner:
        index.by_owner.setdefault(entry.owner, []).append(entry)

    alias_candidates = [entry.asset_id]
    alias_candidates.extend(alias for alias in entry.aliases if alias not in alias_candidates)
    for alias in alias_candidates:
        index.all_asset_ids.add(alias)
        existing_current_entry = index.by_asset_id.get(alias)
        if existing_current_entry is not None and alias != entry.asset_id:
            issues.append(
                ValidationIssue(
                    "ERROR",
                    0,
                    f"{entry.source_file}: alias '{alias}' collides with current asset_id in {existing_current_entry.source_file}",
                )
            )
            continue

        existing_current = index.alias_to_current.get(alias)
        if existing_current is not None and existing_current != entry.asset_id:
            existing_entry = index.by_asset_id.get(existing_current)
            existing_path = existing_entry.source_file if existing_entry is not None else "<unknown>"
            issues.append(
                ValidationIssue(
                    "ERROR",
                    0,
                    f"{entry.source_file}: alias '{alias}' also points to '{existing_current}' in {existing_path}",
                )
            )
            continue

        if existing_current is None:
            index.alias_to_current[alias] = entry.asset_id


def _collect_repo_entity_ids(repo_root: Path) -> set[str]:
    entity_ids: set[str] = set()
    for path in sorted(repo_root.glob("**/*.md")):
        if not path.is_file() or ".git" in path.parts:
            continue
        parsed = parse_file(path, repo_root=repo_root)
        if not isinstance(parsed.yaml_data, dict):
            continue
        raw_entities = parsed.yaml_data.get("entities")
        if not isinstance(raw_entities, list):
            continue
        for entity_id in raw_entities:
            if isinstance(entity_id, str):
                entity_ids.add(entity_id)
    return entity_ids


def _art_allowed_subtypes(entity_registry: EntityTypeRegistry | None) -> list[str]:
    allowed, _reserved, _entry = _art_subtype_sets(entity_registry)
    ordered = [subtype for subtype in ART_SUBTYPE_ORDER if subtype in allowed]
    ordered.extend(sorted(subtype for subtype in allowed if subtype not in ordered))
    return ordered or list(ART_SUBTYPE_ORDER)


def _art_subtype_sets(
    entity_registry: EntityTypeRegistry | None,
) -> tuple[set[str], set[str], EntityTypeEntry | None]:
    if entity_registry is None:
        return set(ART_SUBTYPE_ORDER), set(ART_RESERVED_SUBTYPES), None

    art_entry = entity_registry.get_entry("A")
    if art_entry is None:
        return set(), set(), None

    allowed = set(art_entry.subtype_allowed or ART_SUBTYPE_ORDER)
    reserved = set(art_entry.subtype_reserved or ART_RESERVED_SUBTYPES)
    return allowed, reserved, art_entry


def _asset_entry_completion_pct(entry: ArtMetadataEntry) -> float:
    tags = {tag.lower() for tag in entry.state_tags}
    if tags & {"done", "complete", "completed"}:
        return 100.0
    if tags & {"wip", "in_progress", "in-progress"}:
        return 50.0
    return 25.0


def _art_metadata_entry_line_nums(parsed_markdown: ParsedMarkdown) -> list[int]:
    lines = _source_lines(parsed_markdown)
    if parsed_markdown.yaml_start_line is None:
        return []

    start_idx = parsed_markdown.yaml_start_line
    end_idx = parsed_markdown.yaml_end_line - 1 if parsed_markdown.yaml_end_line is not None else len(lines)
    in_art_metadata = False
    base_indent = 0
    entry_lines: list[int] = []

    for idx in range(start_idx, min(end_idx, len(lines))):
        raw_line = _strip_inline_comment(lines[idx]).rstrip()
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        if not in_art_metadata:
            if re.match(r"^art_metadata\s*:", stripped):
                in_art_metadata = True
                base_indent = indent
            continue

        if indent <= base_indent:
            break
        if stripped.startswith("- "):
            entry_lines.append(idx + 1)

    return entry_lines


def _issues_with_path(rel_path: str, issues: list[ValidationIssue]) -> list[ValidationIssue]:
    return [
        ValidationIssue(issue.severity, issue.line_num, f"{rel_path}: {issue.message}")
        for issue in issues
    ]


def _index_rel_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def validate_phase_log(entries: list[dict[str, Any]], rel_path: str = ".protocol_version") -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    base_by_dialogue: dict[str, str | None] = {}

    for idx, entry in enumerate(entries, start=1):
        prefix = f"{rel_path}: phase_log[{idx}]"
        status = entry.get("status", "in_progress")
        if status not in VALID_PHASE_STATUSES:
            issues.append(ValidationIssue("ERROR", 0, f"{prefix}: status '{status}' is invalid"))

        if status == "aborted":
            if not entry.get("abort_reason"):
                issues.append(ValidationIssue("ERROR", 0, f"{prefix}: status aborted requires abort_reason"))
            if not entry.get("detail"):
                issues.append(ValidationIssue("ERROR", 0, f"{prefix}: status aborted requires detail"))
            if entry.get("abort_reason") == "parallel_conflict" and not entry.get("entities_touched"):
                issues.append(ValidationIssue("ERROR", 0, f"{prefix}: parallel_conflict requires entities_touched"))

        import_source = entry.get("import_source")
        if import_source is not None:
            if import_source not in VALID_IMPORT_SOURCES:
                issues.append(ValidationIssue("ERROR", 0, f"{prefix}: import_source '{import_source}' is invalid"))
            skill = entry.get("skill")
            if not isinstance(skill, str) or not skill.startswith("/create-"):
                issues.append(ValidationIssue("ERROR", 0, f"{prefix}: import_source requires /create-* skill"))

        _validate_phase_log_entities_touched(entry, prefix, issues)
        _validate_phase_log_iteration(entry, prefix, issues)
        _validate_phase_log_conflicts(entry, prefix, import_source, issues)

        if entry.get("mode_tag") == "SINGLE_ITER":
            dialogue_paths = entry.get("dialogue_paths")
            if isinstance(dialogue_paths, list):
                for dialogue_path in dialogue_paths:
                    if isinstance(dialogue_path, str):
                        base_by_dialogue[dialogue_path] = entry.get("base_dialogue")

    _validate_base_dialogue_cycles(base_by_dialogue, rel_path, issues)
    return issues


def load_yaml_text(text: str) -> Any:
    if _pyyaml is not None:  # pragma: no cover
        try:
            loaded = _pyyaml.safe_load(text)
        except Exception as exc:
            raise LimitedYamlError(str(exc)) from exc
        return {} if loaded is None else loaded

    return _parse_limited_yaml(text)


def _read_registry_yaml(path: Path) -> tuple[Any, list[ValidationIssue]]:
    try:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
    except FileNotFoundError:
        return None, [ValidationIssue("ERROR", 0, f"{path.as_posix()}: registry file not found")]
    except OSError as exc:
        return None, [ValidationIssue("ERROR", 0, f"{path.as_posix()}: cannot read registry: {exc}")]

    try:
        return load_yaml_text(text), []
    except LimitedYamlError as exc:
        return None, [ValidationIssue("ERROR", 1, f"{path.as_posix()}: YAML parse error: {exc}")]


def _registry_int(value: Any, default: int) -> int:
    return value if isinstance(value, int) else default


def _parse_entity_type_entries(
    raw_entries: Any,
    section_name: str,
    root: Path,
    issues: list[ValidationIssue],
    *,
    validate_target_dirs: bool,
) -> dict[str, EntityTypeEntry]:
    if raw_entries is None:
        return {}
    if not isinstance(raw_entries, list):
        issues.append(ValidationIssue("ERROR", 0, f"{section_name} must be a list"))
        return {}

    entries: dict[str, EntityTypeEntry] = {}
    for idx, raw_entry in enumerate(raw_entries, start=1):
        label = f"{section_name}[{idx}]"
        if not isinstance(raw_entry, dict):
            issues.append(ValidationIssue("ERROR", 0, f"{label} must be a map"))
            continue

        type_value = raw_entry.get("type")
        if not isinstance(type_value, str) or not type_value:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.type is required"))
            continue
        if type_value in entries:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.type '{type_value}' duplicates another {section_name} entry"))
            continue

        pattern_value = raw_entry.get("id_pattern")
        if not isinstance(pattern_value, str) or not pattern_value:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.id_pattern is required"))
            pattern_value = r"(?!)"
        try:
            compiled_pattern = re.compile(pattern_value)
        except re.error as exc:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.id_pattern is invalid regex: {exc}"))
            compiled_pattern = re.compile(r"(?!)")

        target_dir = _registry_target_dir(raw_entry.get("target_dir"), label, issues)
        if validate_target_dirs:
            _validate_registry_target_dir(target_dir, root, label, issues)

        subtype_allowed, subtype_reserved = _parse_entity_subtype(raw_entry, label, issues)
        description = raw_entry.get("description")
        entries[type_value] = EntityTypeEntry(
            type=type_value,
            description=description if isinstance(description, str) else "",
            id_pattern=pattern_value,
            id_pattern_compiled=compiled_pattern,
            target_dir=target_dir,
            cross_ref_allowed=raw_entry.get("cross_ref_allowed") is True,
            locked=raw_entry.get("locked") is True,
            subtype_allowed=subtype_allowed,
            subtype_reserved=subtype_reserved,
        )

    return entries


def _parse_qa_type_entries(
    raw_entries: Any,
    section_name: str,
    issues: list[ValidationIssue],
) -> dict[str, QaTypeEntry]:
    if raw_entries is None:
        return {}
    if not isinstance(raw_entries, list):
        issues.append(ValidationIssue("ERROR", 0, f"{section_name} must be a list"))
        return {}

    entries: dict[str, QaTypeEntry] = {}
    for idx, raw_entry in enumerate(raw_entries, start=1):
        label = f"{section_name}[{idx}]"
        if not isinstance(raw_entry, dict):
            issues.append(ValidationIssue("ERROR", 0, f"{label} must be a map"))
            continue

        qa_type_value = raw_entry.get("qa_type")
        if not isinstance(qa_type_value, str) or not qa_type_value:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.qa_type is required"))
            continue
        if qa_type_value in entries:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.qa_type '{qa_type_value}' duplicates another {section_name} entry"))
            continue

        template_path = raw_entry.get("template_path")
        if not isinstance(template_path, str) or not template_path:
            issues.append(ValidationIssue("ERROR", 0, f"{label}.template_path is required"))
            template_path = ""

        description = raw_entry.get("description")
        entries[qa_type_value] = QaTypeEntry(
            qa_type=qa_type_value,
            description=description if isinstance(description, str) else "",
            template_path=template_path,
            locked=raw_entry.get("locked") is True,
        )

    return entries


def _registry_target_dir(raw_target_dir: Any, label: str, issues: list[ValidationIssue]) -> str:
    if isinstance(raw_target_dir, str) and raw_target_dir:
        return raw_target_dir
    if isinstance(raw_target_dir, list) and all(isinstance(item, str) for item in raw_target_dir):
        return ", ".join(raw_target_dir)

    issues.append(ValidationIssue("WARN", 0, f"{label}.target_dir should be a relative path string"))
    return ""


def _parse_entity_subtype(
    raw_entry: dict[str, Any],
    label: str,
    issues: list[ValidationIssue],
) -> tuple[list[str] | None, list[str] | None]:
    raw_subtype = raw_entry.get("subtype")
    subtype_allowed: list[str] | None = None
    subtype_reserved: list[str] | None = None

    if isinstance(raw_subtype, dict):
        subtype_allowed = _optional_str_list(raw_subtype.get("allowed_values"), f"{label}.subtype.allowed_values", issues)
        subtype_reserved = _optional_str_list(raw_subtype.get("reserved_subtypes"), f"{label}.subtype.reserved_subtypes", issues)
    elif isinstance(raw_subtype, list):
        subtype_allowed = _optional_str_list(raw_subtype, f"{label}.subtype", issues)
    elif raw_subtype is not None:
        issues.append(ValidationIssue("ERROR", 0, f"{label}.subtype must be a list or map"))

    if subtype_reserved is None:
        subtype_reserved = _optional_str_list(raw_entry.get("reserved_subtypes"), f"{label}.reserved_subtypes", issues)

    return subtype_allowed, subtype_reserved


def _optional_str_list(raw_values: Any, label: str, issues: list[ValidationIssue]) -> list[str] | None:
    if raw_values is None:
        return None
    if not isinstance(raw_values, list):
        issues.append(ValidationIssue("ERROR", 0, f"{label} must be a list"))
        return None

    values: list[str] = []
    for idx, value in enumerate(raw_values):
        if not isinstance(value, str) or not value:
            issues.append(ValidationIssue("ERROR", 0, f"{label}[{idx}] must be a non-empty string"))
            continue
        values.append(value)
    return values


def _parse_reserved_prefixes(raw_prefixes: Any, issues: list[ValidationIssue]) -> list[str]:
    if raw_prefixes is None:
        return []
    if not isinstance(raw_prefixes, list):
        issues.append(ValidationIssue("ERROR", 0, "reserved_prefixes must be a list"))
        return []

    prefixes: list[str] = []
    for idx, raw_prefix in enumerate(raw_prefixes, start=1):
        if isinstance(raw_prefix, str):
            prefix = raw_prefix
        elif isinstance(raw_prefix, dict) and isinstance(raw_prefix.get("prefix"), str):
            prefix = raw_prefix["prefix"]
        else:
            issues.append(ValidationIssue("ERROR", 0, f"reserved_prefixes[{idx}] must be a string or map with prefix"))
            continue
        if prefix not in prefixes:
            prefixes.append(prefix)
    return prefixes


def _validate_user_extension_entries(
    user_extensions: dict[str, EntityTypeEntry],
    core: dict[str, EntityTypeEntry],
    reserved_prefixes: list[str],
    issues: list[ValidationIssue],
) -> None:
    for type_name in user_extensions:
        if type_name in core:
            issues.append(ValidationIssue("ERROR", 0, f"user_extensions type {type_name} 不可跟 core 重複"))

        reserved_prefix = _reserved_prefix_for_type(type_name, reserved_prefixes)
        if reserved_prefix is not None:
            issues.append(ValidationIssue("WARN", 0, f"user_extensions type {type_name} 使用 reserved_prefix {reserved_prefix}"))


def _validate_instance_core_entries(
    raw_core: Any,
    template_core: dict[str, EntityTypeEntry],
    root: Path,
    issues: list[ValidationIssue],
) -> None:
    if raw_core in (None, []):
        return

    instance_core = _parse_entity_type_entries(
        raw_core,
        "instance.core",
        root,
        issues,
        validate_target_dirs=False,
    )
    for type_name, instance_entry in instance_core.items():
        template_entry = template_core.get(type_name)
        if template_entry is None:
            issues.append(ValidationIssue("ERROR", 0, f"instance core type {type_name} 不在 Template core"))
            continue
        if _entity_entry_signature(instance_entry) != _entity_entry_signature(template_entry):
            issues.append(ValidationIssue("ERROR", 0, f"instance core type {type_name} 與 Template core 不一致"))


def _validate_qa_user_extension_entries(
    user_extensions: dict[str, QaTypeEntry],
    core: dict[str, QaTypeEntry],
    root: Path,
    issues: list[ValidationIssue],
    registry: QaTypeRegistry,
) -> None:
    for qa_type, entry in user_extensions.items():
        if qa_type in core:
            issues.append(ValidationIssue("ERROR", 0, f"user_extensions qa_type {qa_type} 不可跟 core 重複"))

        template_path = _resolve_qa_template_path(entry, root, issues)
        if template_path is None:
            continue

        parsed = parse_file(template_path, repo_root=root, qa_type_registry=registry)
        template_qa_type = None
        if isinstance(parsed.yaml_data, dict):
            template_qa_type = parsed.yaml_data.get("qa_type")

        if template_qa_type != qa_type:
            issues.append(
                ValidationIssue(
                    "WARN",
                    parsed.yaml_start_line or 0,
                    f"{entry.template_path}: template frontmatter qa_type '{template_qa_type}' 與 registry entry '{qa_type}' 不對應",
                )
            )


def _resolve_qa_template_path(
    entry: QaTypeEntry,
    root: Path,
    issues: list[ValidationIssue],
) -> Path | None:
    normalized = entry.template_path.replace("\\", "/").strip()
    path = Path(normalized)
    has_parent_traversal = any(part == ".." for part in normalized.split("/"))
    if path.is_absolute() or has_parent_traversal:
        issues.append(ValidationIssue("ERROR", 0, f"user_extensions qa_type {entry.qa_type} template_path '{entry.template_path}' 必須是相對路徑"))
        return None

    if not normalized.startswith("09_quality_assurance/"):
        issues.append(ValidationIssue("ERROR", 0, f"user_extensions qa_type {entry.qa_type} template_path 必須位於 09_quality_assurance/"))
        return None

    template_path = root / path
    if not template_path.is_file():
        issues.append(ValidationIssue("ERROR", 0, f"user_extensions qa_type {entry.qa_type} template_path '{entry.template_path}' 不存在"))
        return None

    return template_path


def _validate_instance_qa_core_entries(
    raw_core: Any,
    template_core: dict[str, QaTypeEntry],
    issues: list[ValidationIssue],
) -> None:
    if raw_core in (None, []):
        return

    instance_core = _parse_qa_type_entries(raw_core, "instance.core", issues)
    for qa_type, instance_entry in instance_core.items():
        template_entry = template_core.get(qa_type)
        if template_entry is None:
            issues.append(ValidationIssue("ERROR", 0, f"instance core qa_type {qa_type} 不在 Template core"))
            continue
        if _qa_entry_signature(instance_entry) != _qa_entry_signature(template_entry):
            issues.append(ValidationIssue("ERROR", 0, f"instance core qa_type {qa_type} 與 Template core 不一致"))


def _entity_entry_signature(entry: EntityTypeEntry) -> tuple[Any, ...]:
    return (
        entry.description,
        entry.id_pattern,
        entry.target_dir,
        entry.cross_ref_allowed,
        entry.locked,
        tuple(entry.subtype_allowed or []),
        tuple(entry.subtype_reserved or []),
    )


def _qa_entry_signature(entry: QaTypeEntry) -> tuple[Any, ...]:
    return (
        entry.description,
        entry.template_path,
        entry.locked,
    )


def _reserved_prefix_for_type(type_name: str, reserved_prefixes: list[str]) -> str | None:
    for reserved_prefix in sorted(reserved_prefixes, key=len, reverse=True):
        if type_name == reserved_prefix or type_name.startswith(f"{reserved_prefix}-"):
            return reserved_prefix
    return None


def _validate_registry_target_dir(
    target_dir: str,
    root: Path,
    label: str,
    issues: list[ValidationIssue],
) -> None:
    for item in _split_registry_target_dirs(target_dir):
        normalized = item.replace("\\", "/").strip()
        if not normalized:
            issues.append(ValidationIssue("WARN", 0, f"{label}.target_dir is empty"))
            continue
        path = Path(normalized)
        has_parent_traversal = any(part == ".." for part in normalized.split("/"))
        if path.is_absolute() or has_parent_traversal:
            issues.append(ValidationIssue("WARN", 0, f"{label}.target_dir '{item}' 必須是相對路徑"))
            continue
        if not (root / path).is_dir():
            issues.append(ValidationIssue("WARN", 0, f"{label}.target_dir '{item}' 不存在"))


def _split_registry_target_dirs(target_dir: str) -> list[str]:
    return [item.strip() for item in target_dir.split(",")] if target_dir else [""]


def _resolve_entity_type_entry(
    entity_id: str,
    registry: EntityTypeRegistry,
) -> tuple[str, EntityTypeEntry | None]:
    entries = list(registry.core.values()) + list(registry.user_extensions.values())
    candidates = [
        entry
        for entry in entries
        if entity_id == entry.type or entity_id.startswith(f"{entry.type}-")
    ]
    if candidates:
        entry = max(candidates, key=lambda item: len(item.type))
        return entry.type, entry
    return _unknown_entity_prefix(entity_id), None


def _unknown_entity_prefix(entity_id: str) -> str:
    if "-" not in entity_id:
        return entity_id
    return entity_id.split("-", 1)[0]


def _validate_art_entity_subtype(entity_id: str, entry: EntityTypeEntry) -> ValidationIssue | None:
    parts = entity_id.split("-", 3)
    subtype = parts[1] if len(parts) > 1 else ""
    allowed = set(entry.subtype_allowed or [])
    reserved = set(entry.subtype_reserved or [])

    if subtype in reserved and subtype not in allowed:
        return ValidationIssue("ERROR", 0, f"subtype {subtype} 在 reserved_subtypes，不在 allowed_values")
    if allowed and subtype not in allowed:
        return ValidationIssue("ERROR", 0, f"未知 A-* subtype {subtype}")
    return None


def _parse_header(lines: list[str]) -> tuple[dict[str, str | None], dict[str, int], list[ValidationIssue]]:
    header = {field_name: None for field_name in REQUIRED_HEADER_FIELDS}
    header_lines: dict[str, int] = {}
    issues: list[ValidationIssue] = []
    patterns = {
        field_name: re.compile(rf"^\s*{re.escape(field_name)}\s*[:：]\s*(.+?)\s*$")
        for field_name in REQUIRED_HEADER_FIELDS
    }

    for line_no, line in enumerate(lines[:HEAD_LINES], start=1):
        for field_name, pattern in patterns.items():
            if field_name in header_lines:
                continue
            match = pattern.match(line)
            if match:
                header[field_name] = match.group(1).strip()
                header_lines[field_name] = line_no

    return header, header_lines, issues


def _validate_header(
    header: dict[str, str | None],
    header_lines: dict[str, int],
    issues: list[ValidationIssue],
) -> None:
    for field_name in REQUIRED_HEADER_FIELDS:
        value = header.get(field_name)
        if value is None:
            issues.append(ValidationIssue("ERROR", 0, f"缺少欄位 '{field_name}'"))
            continue

        line_num = header_lines.get(field_name, 0)
        if field_name == "狀態" and value not in VALID_DOCUMENT_STATUSES:
            allowed = "/".join(sorted(VALID_DOCUMENT_STATUSES))
            issues.append(ValidationIssue("WARN", line_num, f"狀態 值 '{value}' 不在允許集合 ({allowed}) 內"))
        elif field_name == "版本" and not VERSION_RE.match(value):
            issues.append(ValidationIssue("WARN", line_num, f"版本 格式異常 '{value}' (期望 vN.N 或 N.N，可附 -suffix)"))
        elif field_name == "最後更新" and not DATE_RE.match(value):
            issues.append(ValidationIssue("WARN", line_num, f"最後更新 格式異常 '{value}' (期望 YYYY-MM-DD)"))
        elif field_name == "優先級" and value not in VALID_PRIORITIES:
            allowed = "/".join(sorted(VALID_PRIORITIES))
            issues.append(ValidationIssue("WARN", line_num, f"優先級 值 '{value}' 不在允許集合 ({allowed}) 內"))


def _find_header_adjacent_yaml(lines: list[str], header_lines: dict[str, int]) -> tuple[str, int, int] | None:
    if not header_lines:
        return None

    idx = max(header_lines.values())
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx >= len(lines) or lines[idx].strip() != "---":
        return None

    end_idx = idx + 1
    while end_idx < len(lines):
        if lines[end_idx].strip() == "---":
            block_lines = lines[idx + 1 : end_idx]
            if not _looks_like_frontmatter_yaml(block_lines):
                return None
            return "\n".join(block_lines), idx + 1, end_idx + 1
        end_idx += 1

    # 未找到閉合 '---'：開頭 '---' 多半是 Markdown 水平分隔線（HR），
    # 而非 frontmatter YAML block 起點。僅當剩餘內容確實像 frontmatter
    # 才視為未閉合 block；否則回傳 None，避免把整檔剩餘內容誤判為 YAML
    # 並在下游 _validate_frontmatter_yaml 報假 ERROR（F15 / NEW_REQ_39）。
    tail_lines = lines[idx + 1 :]
    if not _looks_like_frontmatter_yaml(tail_lines):
        return None
    return "\n".join(tail_lines), idx + 1, len(lines)


def _looks_like_frontmatter_yaml(lines: list[str]) -> bool:
    key_re = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:")
    for line in lines:
        stripped = _strip_inline_comment(line).strip()
        if not stripped:
            continue
        match = key_re.match(stripped)
        if match and match.group(1) in YAML_RECOGNIZED_FIELDS:
            return True
    return False


def _validate_frontmatter_yaml(
    data: Any,
    start_line: int,
    issues: list[ValidationIssue],
    qa_type_registry: QaTypeRegistry | None,
) -> None:
    if not isinstance(data, dict):
        issues.append(ValidationIssue("ERROR", start_line, "YAML block must be a mapping"))
        return

    for field_name in UPSTREAM_FIELDS:
        if field_name not in data:
            issues.append(ValidationIssue("WARN", start_line, f"YAML block 缺少欄位 '{field_name}'"))

    if "entities" in data and data["entities"] is not None and not isinstance(data["entities"], list):
        issues.append(ValidationIssue("WARN", start_line, "entities should be a list"))
    if "depends_on" in data and data["depends_on"] is not None and not isinstance(data["depends_on"], list):
        issues.append(ValidationIssue("WARN", start_line, "depends_on should be a list"))
    if "weight" in data and data["weight"] is not None and not isinstance(data["weight"], (int, float, dict)):
        issues.append(ValidationIssue("WARN", start_line, "weight should be scalar or map"))
    if "dialogue_keys" in data and data["dialogue_keys"] is not None and not isinstance(data["dialogue_keys"], dict):
        issues.append(ValidationIssue("WARN", start_line, "dialogue_keys should be a map"))
    if "art_metadata" in data and data["art_metadata"] is not None and not isinstance(data["art_metadata"], list):
        issues.append(ValidationIssue("WARN", start_line, "art_metadata should be a list"))

    _validate_enum_value(data, "pipeline_state", VALID_PIPELINE_STATES, "WARN", start_line, issues)
    mode_tag_issue = validate_mode_tag(data.get("mode_tag"))
    if mode_tag_issue is not None:
        issues.append(_issue_at_line(mode_tag_issue, start_line))
    _validate_enum_value(data, "qa_decision", VALID_QA_DECISIONS, "ERROR", start_line, issues)
    qa_type_issue = validate_frontmatter_qa_type(data.get("qa_type"), registry=qa_type_registry)
    if qa_type_issue is not None:
        issues.append(_issue_at_line(qa_type_issue, start_line))


def _issue_at_line(issue: ValidationIssue, line_num: int) -> ValidationIssue:
    return ValidationIssue(issue.severity, line_num, issue.message)


def _validate_enum_value(
    data: dict[str, Any],
    field_name: str,
    allowed_values: set[str],
    severity: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    value = data.get(field_name)
    if value is None:
        return
    if value not in allowed_values:
        allowed = "/".join(sorted(allowed_values))
        issues.append(ValidationIssue(severity, line_num, f"{field_name} 值 '{value}' 不在允許集合 ({allowed}) 內"))


def _validate_phase_log_entities_touched(
    entry: dict[str, Any],
    prefix: str,
    issues: list[ValidationIssue],
) -> None:
    entities_touched = entry.get("entities_touched", [])
    if entities_touched is None:
        return
    if not isinstance(entities_touched, list):
        issues.append(ValidationIssue("ERROR", 0, f"{prefix}: entities_touched must be a list"))
        return

    for entity_id in entities_touched:
        if not isinstance(entity_id, str):
            issues.append(ValidationIssue("WARN", 0, f"{prefix}: entities_touched contains non-string ID"))
        elif not _entity_id_re().match(entity_id):
            issues.append(ValidationIssue("WARN", 0, f"{prefix}: entities_touched ID '{entity_id}' does not match known core patterns"))


def _validate_phase_log_iteration(
    entry: dict[str, Any],
    prefix: str,
    issues: list[ValidationIssue],
) -> None:
    mode_tag = entry.get("mode_tag")
    if mode_tag is not None and mode_tag not in VALID_MODE_TAGS:
        issues.append(ValidationIssue("ERROR", 0, f"{prefix}: mode_tag '{mode_tag}' is invalid"))

    iteration_count = entry.get("iteration_count")
    if mode_tag != "SINGLE_ITER" and iteration_count is not None:
        issues.append(ValidationIssue("WARN", 0, f"{prefix}: iteration_count only has meaning for SINGLE_ITER"))
    if mode_tag != "SINGLE_ITER" and entry.get("base_dialogue") is not None:
        issues.append(ValidationIssue("WARN", 0, f"{prefix}: base_dialogue only has meaning for SINGLE_ITER"))

    if mode_tag == "SINGLE_ITER":
        if not isinstance(iteration_count, int):
            issues.append(ValidationIssue("ERROR", 0, f"{prefix}: SINGLE_ITER requires integer iteration_count"))
            return
        if iteration_count < 1:
            issues.append(ValidationIssue("ERROR", 0, f"{prefix}: iteration_count must start from 1"))
        if iteration_count >= 2 and not entry.get("base_dialogue"):
            issues.append(ValidationIssue("ERROR", 0, f"{prefix}: iteration_count >= 2 requires base_dialogue"))


def _validate_phase_log_conflicts(
    entry: dict[str, Any],
    prefix: str,
    import_source: Any,
    issues: list[ValidationIssue],
) -> None:
    conflicts = entry.get("conflict_resolutions")
    if conflicts is None:
        return
    if import_source is None:
        issues.append(ValidationIssue("WARN", 0, f"{prefix}: conflict_resolutions only has meaning when import_source is set"))
    if not isinstance(conflicts, list):
        issues.append(ValidationIssue("ERROR", 0, f"{prefix}: conflict_resolutions must be a list"))
        return

    for conflict_idx, conflict in enumerate(conflicts, start=1):
        conflict_prefix = f"{prefix}.conflict_resolutions[{conflict_idx}]"
        if not isinstance(conflict, dict):
            issues.append(ValidationIssue("ERROR", 0, f"{conflict_prefix}: entry must be a dict"))
            continue
        if not conflict.get("entity_id"):
            issues.append(ValidationIssue("ERROR", 0, f"{conflict_prefix}: entity_id is required"))
        if not conflict.get("resolved_at"):
            issues.append(ValidationIssue("ERROR", 0, f"{conflict_prefix}: resolved_at is required"))
        decision = conflict.get("decision")
        if decision not in VALID_CONFLICT_DECISIONS:
            issues.append(ValidationIssue("ERROR", 0, f"{conflict_prefix}: decision '{decision}' is invalid"))
        if decision == "create-as-new" and not conflict.get("new_entity_id"):
            issues.append(ValidationIssue("ERROR", 0, f"{conflict_prefix}: create-as-new requires new_entity_id"))


def _validate_base_dialogue_cycles(
    base_by_dialogue: dict[str, str | None],
    rel_path: str,
    issues: list[ValidationIssue],
) -> None:
    for dialogue_path in sorted(base_by_dialogue):
        seen: set[str] = set()
        current: str | None = dialogue_path
        while current is not None and current in base_by_dialogue:
            if current in seen:
                issues.append(ValidationIssue("ERROR", 0, f"{rel_path}: base_dialogue cycle detected at {current}"))
                break
            seen.add(current)
            current = base_by_dialogue.get(current)


def _parse_dialogue_key_entry(
    map_key: str,
    raw_entry: Any,
    line_num: int,
    *,
    mode_tag: Any,
    art_metadata_index: set[str] | None,
    all_keys_set: set[str] | None,
    issues: list[ValidationIssue],
) -> DialogueKeyEntry:
    if not isinstance(raw_entry, dict):
        issues.append(ValidationIssue("ERROR", line_num, f"dialogue_keys.{map_key}: entry must be a map"))
        raw: dict[str, Any] = {}
    else:
        raw = raw_entry

    prefix = f"dialogue_keys.{map_key}"
    _validate_dialogue_key_name(map_key, line_num, issues, f"{prefix}: map key")
    _validate_dialogue_entry_required_fields(raw, prefix, line_num, issues)

    line_index = raw.get("line_index")
    if not isinstance(line_index, int):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: line_index must be an integer"))
        parsed_line_index: int | None = None
    elif line_index < 1:
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: line_index must be 1-based"))
        parsed_line_index = line_index
    else:
        parsed_line_index = line_index

    speaker = raw.get("speaker")
    if speaker is not None and not isinstance(speaker, str):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: speaker must be a string or null"))
        speaker = None

    aliases = _parse_dialogue_aliases(raw.get("aliases"), prefix, line_num, issues)
    portrait = _parse_optional_asset_field(raw.get("portrait"), "portrait", "A-portrait-", prefix, line_num, art_metadata_index, issues)
    bgm = _parse_optional_asset_field(raw.get("bgm"), "bgm", "A-bgm-", prefix, line_num, art_metadata_index, issues)
    sfx = _parse_sfx_field(raw.get("sfx"), prefix, line_num, art_metadata_index, issues)

    status_value = raw.get("status", "active")
    status = status_value if isinstance(status_value, str) else ""
    if status not in VALID_DIALOGUE_KEY_STATUSES:
        allowed = "/".join(sorted(VALID_DIALOGUE_KEY_STATUSES))
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: status '{status_value}' is invalid (allowed: {allowed})"))

    deleted_at = raw.get("deleted_at")
    deprecated_reason = raw.get("deprecated_reason")
    if status == "deleted" and not _has_dialogue_value(deleted_at):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: status deleted requires deleted_at"))
    if status == "deprecated" and not _has_dialogue_value(deprecated_reason):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: status deprecated requires deprecated_reason"))

    source_keys = _parse_source_keys(raw.get("source_keys"), prefix, line_num, mode_tag, all_keys_set, issues)

    return DialogueKeyEntry(
        map_key=map_key,
        line_index=parsed_line_index,
        speaker=speaker,
        aliases=aliases,
        portrait=portrait,
        bgm=bgm,
        sfx=sfx,
        status=status or str(status_value),
        created_at=raw.get("created_at"),
        renamed_at=raw.get("renamed_at"),
        deleted_at=deleted_at,
        deprecated_reason=deprecated_reason if isinstance(deprecated_reason, str) else deprecated_reason,
        source_keys=source_keys,
        raw=raw,
        line_num=line_num,
    )


def _validate_dialogue_entry_required_fields(
    raw: dict[str, Any],
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> None:
    for field_name in ("line_index", "speaker", "aliases", "portrait", "bgm", "sfx", "created_at"):
        if field_name not in raw:
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: missing required field '{field_name}'"))


def _parse_dialogue_aliases(
    raw_aliases: Any,
    prefix: str,
    line_num: int,
    issues: list[ValidationIssue],
) -> list[str]:
    if not isinstance(raw_aliases, list):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases must be a non-empty list"))
        return []
    if not raw_aliases:
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases must contain at least one key"))
        return []

    aliases: list[str] = []
    for idx, alias in enumerate(raw_aliases):
        if not isinstance(alias, str):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases[{idx}] must be a string"))
            continue
        aliases.append(alias)

    if aliases and not DEFAULT_DIALOGUE_KEY_RE.match(aliases[0]):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: aliases[0] must use default key syntax"))
    return aliases


def _parse_optional_asset_field(
    value: Any,
    field_name: str,
    required_prefix: str,
    prefix: str,
    line_num: int,
    art_metadata_index: set[str] | None,
    issues: list[ValidationIssue],
) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: {field_name} must be a string or null"))
        return None
    if not value.startswith(required_prefix):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: {field_name} must use {required_prefix}* asset_id"))
    elif art_metadata_index is not None and value not in art_metadata_index:
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: {field_name} asset_id '{value}' not found in art metadata index"))
    return value


def _parse_sfx_field(
    value: Any,
    prefix: str,
    line_num: int,
    art_metadata_index: set[str] | None,
    issues: list[ValidationIssue],
) -> list[str]:
    if value is None:
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: sfx must be a list"))
        return []
    if not isinstance(value, list):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: sfx must be a list"))
        return []

    sfx_values: list[str] = []
    for idx, asset_id in enumerate(value):
        if not isinstance(asset_id, str):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: sfx[{idx}] must be a string"))
            continue
        if not asset_id.startswith("A-sfx-"):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: sfx[{idx}] must use A-sfx-* asset_id"))
        elif art_metadata_index is not None and asset_id not in art_metadata_index:
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: sfx asset_id '{asset_id}' not found in art metadata index"))
        sfx_values.append(asset_id)
    return sfx_values


def _parse_source_keys(
    value: Any,
    prefix: str,
    line_num: int,
    mode_tag: Any,
    all_keys_set: set[str] | None,
    issues: list[ValidationIssue],
) -> list[str] | None:
    if value is None:
        return None
    if not isinstance(value, list):
        issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: source_keys must be a list or null"))
        return None

    source_keys: list[str] = []
    for idx, source_key in enumerate(value):
        if not isinstance(source_key, str):
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: source_keys[{idx}] must be a string"))
            continue
        if all_keys_set is not None and source_key not in all_keys_set:
            issues.append(ValidationIssue("ERROR", line_num, f"{prefix}: source_keys[{idx}] '{source_key}' not found in all_keys_set"))
        source_keys.append(source_key)

    if mode_tag != "CONVERGENCE":
        issues.append(ValidationIssue("WARN", line_num, f"{prefix}: source_keys only has meaning for v02 CONVERGENCE dialogue"))
    return source_keys


def _validate_dialogue_key_name(
    key: str,
    line_num: int,
    issues: list[ValidationIssue],
    label: str,
) -> None:
    if DEFAULT_DIALOGUE_KEY_RE.match(key):
        return
    if USER_DEFINED_DIALOGUE_KEY_RE.match(key):
        issues.append(ValidationIssue("WARN", line_num, f"{label} '{key}' uses user-defined key syntax"))
        return
    issues.append(ValidationIssue("ERROR", line_num, f"{label} '{key}' contains characters outside allowed key syntax"))


def _parse_body_dialogue_comments(
    parsed_markdown: ParsedMarkdown,
) -> tuple[list[str], dict[str, list[int]], dict[str, dict[str, list[str]]], list[ValidationIssue]]:
    lines = _source_lines(parsed_markdown)
    start_idx = parsed_markdown.yaml_end_line or 0
    key_order: list[str] = []
    key_lines: dict[str, list[int]] = {}
    art_comments: dict[str, dict[str, list[str]]] = {}
    issues: list[ValidationIssue] = []
    pending_key: str | None = None
    pending_line = 0

    for idx in range(start_idx, len(lines)):
        line_no = idx + 1
        line = lines[idx]
        key_matches = list(KEY_COMMENT_RE.finditer(line))
        for match in key_matches:
            if pending_key is not None:
                issues.append(ValidationIssue("ERROR", pending_line, f"body KEY '{pending_key}' has no following dialogue/action line before next KEY"))
            pending_key = match.group(1).strip()
            pending_line = line_no
            key_order.append(pending_key)
            key_lines.setdefault(pending_key, []).append(line_no)
            art_comments.setdefault(pending_key, {"portrait": [], "bg": [], "bgm": [], "sfx": []})

        if pending_key is not None:
            for art_match in ART_COMMENT_RE.finditer(line):
                field_name = _art_comment_field_name(art_match.group(1))
                if field_name is None:
                    continue
                asset_id = art_match.group(2).strip()
                art_comments.setdefault(pending_key, {"portrait": [], "bg": [], "bgm": [], "sfx": []})[field_name].append(asset_id)

        if HTML_COMMENT_RE.sub("", line).strip():
            pending_key = None
            pending_line = 0

    if pending_key is not None:
        issues.append(ValidationIssue("ERROR", pending_line, f"body KEY '{pending_key}' has no following dialogue/action line"))

    return key_order, key_lines, art_comments, issues


def _validate_body_key_consistency(
    entries: dict[str, DialogueKeyEntry],
    body_key_order: list[str],
    body_key_lines: dict[str, list[int]],
    issues: list[ValidationIssue],
) -> None:
    for key, line_nums in body_key_lines.items():
        if key not in entries:
            issues.append(ValidationIssue("ERROR", line_nums[0], f"body KEY '{key}' is not present in frontmatter dialogue_keys"))
        if len(line_nums) > 1:
            issues.append(ValidationIssue("ERROR", line_nums[1], f"body KEY '{key}' appears more than once"))

    body_key_set = set(body_key_order)
    for key, entry in entries.items():
        if entry.status != "deleted" and key not in body_key_set:
            issues.append(ValidationIssue("ERROR", entry.line_num, f"dialogue_keys.{key}: non-deleted key is missing body KEY comment"))

    unique_known_body_order: list[str] = []
    seen: set[str] = set()
    for key in body_key_order:
        if key in entries and key not in seen:
            unique_known_body_order.append(key)
            seen.add(key)

    represented_entries = [entries[key] for key in unique_known_body_order]
    if any(entry.line_index is None for entry in represented_entries):
        return

    line_index_to_key: dict[int, str] = {}
    for entry in represented_entries:
        assert entry.line_index is not None
        existing_key = line_index_to_key.get(entry.line_index)
        if existing_key is not None:
            issues.append(ValidationIssue("ERROR", entry.line_num, f"dialogue_keys.{entry.map_key}: line_index duplicates {existing_key}"))
        line_index_to_key[entry.line_index] = entry.map_key

    expected_order = [entry.map_key for entry in sorted(represented_entries, key=lambda item: item.line_index or 0)]
    if expected_order != unique_known_body_order:
        line_num = body_key_lines.get(unique_known_body_order[0], [0])[0] if unique_known_body_order else 0
        issues.append(
            ValidationIssue(
                "ERROR",
                line_num,
                f"body KEY order does not match dialogue_keys line_index order (expected {expected_order}, got {unique_known_body_order})",
            )
        )


def _validate_art_comment_consistency(
    entries: dict[str, DialogueKeyEntry],
    body_art_comments: dict[str, dict[str, list[str]]],
    body_key_lines: dict[str, list[int]],
    issues: list[ValidationIssue],
) -> None:
    for key, art_map in body_art_comments.items():
        entry = entries.get(key)
        if entry is None:
            continue
        line_num = body_key_lines.get(key, [entry.line_num])[0]
        for field_name in ("portrait", "bgm"):
            comments = art_map.get(field_name, [])
            if not comments:
                continue
            expected = getattr(entry, field_name)
            for asset_id in comments:
                art_type = ART_COMMENT_TYPE_BY_FIELD[field_name]
                if not expected:
                    issues.append(
                        ValidationIssue(
                            "WARN",
                            line_num,
                            f"內文 art 提示無 frontmatter 對應: KEY '{key}' {art_type} {asset_id}",
                        )
                    )
                elif asset_id != expected:
                    issues.append(
                        ValidationIssue(
                            "WARN",
                            line_num,
                            f"內文提示與 frontmatter 權威來源不符: KEY '{key}' {art_type} {asset_id} != {expected}",
                        )
                    )

        sfx_comments = art_map.get("sfx", [])
        for asset_id in sfx_comments:
            if not entry.sfx:
                issues.append(
                    ValidationIssue(
                        "WARN",
                        line_num,
                        f"內文 art 提示無 frontmatter 對應: KEY '{key}' SFX {asset_id}",
                    )
                )
            elif asset_id not in entry.sfx:
                issues.append(
                    ValidationIssue(
                        "WARN",
                        line_num,
                        f"內文提示與 frontmatter 權威來源不符: KEY '{key}' SFX {asset_id} != {entry.sfx}",
                    )
                )


def _dialogue_key_entry_line_nums(parsed_markdown: ParsedMarkdown) -> dict[str, int]:
    lines = _source_lines(parsed_markdown)
    if parsed_markdown.yaml_start_line is None:
        return {}

    start_idx = parsed_markdown.yaml_start_line
    end_idx = parsed_markdown.yaml_end_line - 1 if parsed_markdown.yaml_end_line is not None else len(lines)
    in_dialogue_keys = False
    base_indent = 0
    child_indent: int | None = None
    line_nums: dict[str, int] = {}

    for idx in range(start_idx, min(end_idx, len(lines))):
        raw_line = _strip_inline_comment(lines[idx]).rstrip()
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()
        if not in_dialogue_keys:
            if re.match(r"^dialogue_keys\s*:", stripped):
                in_dialogue_keys = True
                base_indent = indent
            continue

        if indent <= base_indent:
            break
        if child_indent is None:
            child_indent = indent
        if indent != child_indent or stripped.startswith("- "):
            continue
        key, _value = _split_yaml_key_value(stripped, idx + 1)
        line_nums[key.strip("'\"")] = idx + 1

    return line_nums


def _art_comment_field_name(label: str) -> str | None:
    return ART_COMMENT_FIELD_BY_TYPE.get(_canonical_art_comment_type(label))


def _has_dialogue_value(value: Any) -> bool:
    return value is not None and value != ""


def _source_lines(parsed_markdown: ParsedMarkdown) -> list[str]:
    text = parsed_markdown.source_text
    if not text and parsed_markdown.path:
        try:
            text = Path(parsed_markdown.path).read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            text = ""
    return text.splitlines()


def _parse_limited_yaml(text: str) -> Any:
    items = _prepare_yaml_lines(text)
    if not items:
        return {}
    value, idx = _parse_yaml_block(items, 0, items[0][0])
    if idx != len(items):
        line_no = items[idx][2]
        raise LimitedYamlError(f"unexpected trailing YAML at line {line_no}")
    return value


def _prepare_yaml_lines(text: str) -> list[tuple[int, str, int]]:
    items: list[tuple[int, str, int]] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        if "\t" in raw_line[: len(raw_line) - len(raw_line.lstrip())]:
            raise LimitedYamlError(f"tabs are not supported at line {line_no}")
        line = _strip_inline_comment(raw_line).rstrip()
        if not line.strip() or line.strip() == "...":
            continue
        indent = len(line) - len(line.lstrip(" "))
        items.append((indent, line.strip(), line_no))
    return items


def _parse_yaml_block(
    items: list[tuple[int, str, int]],
    idx: int,
    indent: int,
) -> tuple[Any, int]:
    if idx >= len(items):
        return None, idx
    item_indent, text, _line_no = items[idx]
    if item_indent < indent:
        return None, idx
    if item_indent != indent:
        raise LimitedYamlError(f"unexpected indent at line {items[idx][2]}")
    if text.startswith("- "):
        return _parse_yaml_list(items, idx, indent)
    return _parse_yaml_map(items, idx, indent)


def _parse_yaml_map(
    items: list[tuple[int, str, int]],
    idx: int,
    indent: int,
) -> tuple[dict[str, Any], int]:
    result: dict[str, Any] = {}
    while idx < len(items):
        item_indent, text, line_no = items[idx]
        if item_indent < indent:
            break
        if item_indent > indent:
            raise LimitedYamlError(f"unexpected indent at line {line_no}")
        if text.startswith("- "):
            break

        key, value_text = _split_yaml_key_value(text, line_no)
        idx += 1
        if value_text == "":
            if idx < len(items) and items[idx][0] > indent:
                value, idx = _parse_yaml_block(items, idx, items[idx][0])
            else:
                value = None
        else:
            value = _parse_yaml_scalar(value_text, line_no)
        result[key] = value

    return result, idx


def _parse_yaml_list(
    items: list[tuple[int, str, int]],
    idx: int,
    indent: int,
) -> tuple[list[Any], int]:
    result: list[Any] = []
    while idx < len(items):
        item_indent, text, line_no = items[idx]
        if item_indent < indent:
            break
        if item_indent != indent or not text.startswith("- "):
            break

        rest = text[2:].strip()
        idx += 1
        if rest == "":
            if idx < len(items) and items[idx][0] > indent:
                value, idx = _parse_yaml_block(items, idx, items[idx][0])
            else:
                value = None
            result.append(value)
            continue

        if _looks_like_inline_mapping_pair(rest):
            key, value_text = _split_yaml_key_value(rest, line_no)
            item: dict[str, Any] = {}
            if value_text == "":
                if idx < len(items) and items[idx][0] > indent:
                    value, idx = _parse_yaml_block(items, idx, items[idx][0])
                else:
                    value = None
            else:
                value = _parse_yaml_scalar(value_text, line_no)
            item[key] = value

            if idx < len(items) and items[idx][0] > indent:
                continuation, idx = _parse_yaml_block(items, idx, items[idx][0])
                if not isinstance(continuation, dict):
                    raise LimitedYamlError(f"list item continuation must be a map near line {line_no}")
                item.update(continuation)
            result.append(item)
        else:
            result.append(_parse_yaml_scalar(rest, line_no))

    return result, idx


def _split_yaml_key_value(text: str, line_no: int) -> tuple[str, str]:
    if ":" not in text:
        raise LimitedYamlError(f"expected key: value at line {line_no}")
    key, value = text.split(":", 1)
    key = key.strip()
    if not key:
        raise LimitedYamlError(f"empty key at line {line_no}")
    return key, value.strip()


def _looks_like_inline_mapping_pair(text: str) -> bool:
    return re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*:", text) is not None


def _parse_yaml_scalar(text: str, line_no: int) -> Any:
    value = text.strip()
    if value in {"null", "Null", "NULL", "~"}:
        return None
    if value in {"true", "True", "TRUE"}:
        return True
    if value in {"false", "False", "FALSE"}:
        return False
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_parse_yaml_scalar(part, line_no) for part in _split_inline_list(inner)]
    if value.startswith("{") and value.endswith("}"):
        raise LimitedYamlError(f"flow style maps are not supported at line {line_no}")
    if value.startswith("|") or value.startswith(">"):
        raise LimitedYamlError(f"multi-line strings are not supported at line {line_no}")
    if value.startswith("!") or value.startswith("&") or value.startswith("*"):
        raise LimitedYamlError(f"custom tags, anchors, and aliases are not supported at line {line_no}")
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if re.match(r"^-?\d+$", value):
        try:
            return int(value)
        except ValueError:
            return value
    if re.match(r"^-?\d+\.\d+$", value):
        try:
            return float(value)
        except ValueError:
            return value
    return value


def _split_inline_list(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None
    depth = 0
    for char in text:
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue
        if char in {"'", '"'}:
            quote = char
            current.append(char)
            continue
        if char in "[(":
            depth += 1
        elif char in "])":
            depth -= 1
        if char == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if current:
        parts.append("".join(current).strip())
    return parts


def _strip_inline_comment(line: str) -> str:
    quote: str | None = None
    for idx, char in enumerate(line):
        if quote:
            if char == quote:
                quote = None
            continue
        if char in {"'", '"'}:
            quote = char
            continue
        if char == "#" and (idx == 0 or line[idx - 1].isspace()):
            return line[:idx].rstrip()
    return line
