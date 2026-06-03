"""
Phase A.0F 整體驗收 — Integration smoke test

跑法（從 D:/劇本開發工具 根目錄）：
    cd _tools/frontend
    pip install -r requirements.txt
    python tests/test_endpoints_smoke.py

或 pytest：
    python -m pytest tests/test_endpoints_smoke.py -v

兩階段：
  階段 A (stdlib only — 沙箱可跑)：用 AST 解析 server.py，verify 9 endpoint 都定義了
  階段 B (需要 fastapi)：用 TestClient in-process 呼叫每個 endpoint，verify 回應 schema

對齊：
- ARCH §13.2 Contract C 8 endpoint 必跑
- A.0F.3 自加 /api/scenes list endpoint
- L3 Export prompt schema 對齊 (透過 promptAssembler unit test 已 cover)

不測：
- LOCKED race / mtime conflict 完整流（需 dummy data fixture）
- 前端 UI 互動（屬 browser smoke test 範疇，留後續 Playwright）
"""
import ast
import sys
from pathlib import Path

FRONTEND_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = FRONTEND_DIR.parent.parent
SERVER_PY = FRONTEND_DIR / "server.py"


# ============ 階段 A — stdlib AST inventory check ============

EXPECTED_ENDPOINTS = [
    ("GET",  "/api/scene/{scene_id}/header"),
    ("POST", "/api/scene/{scene_id}/save"),
    ("POST", "/api/scene/{scene_id}/save-as"),
    ("GET",  "/api/scenes/{scene_id}/versions"),
    ("GET",  "/api/scenes/{scene_id}/keys/{key}/lines"),
    ("GET",  "/api/assets"),
    ("GET",  "/api/assets/{asset_id}/usage"),
    ("GET",  "/api/scope-counts"),
    ("GET",  "/api/scenes"),  # A.0F.3 自加 list endpoint
    ("GET",  "/api/scene/{scene_id}/version-content"),  # Phase A.0F.patch-P0
]


def find_endpoints_in_server_py():
    """Parse server.py AST, return list of (method, path) tuples from @app.METHOD decorators."""
    tree = ast.parse(SERVER_PY.read_text(encoding="utf-8"))
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.AsyncFunctionDef) and not isinstance(node, ast.FunctionDef):
            continue
        for dec in node.decorator_list:
            if not isinstance(dec, ast.Call):
                continue
            if not isinstance(dec.func, ast.Attribute):
                continue
            method = dec.func.attr.upper()
            if method not in ("GET", "POST", "PUT", "DELETE", "PATCH"):
                continue
            if not dec.args:
                continue
            path_node = dec.args[0]
            if isinstance(path_node, ast.Constant) and isinstance(path_node.value, str):
                found.append((method, path_node.value))
    return found


def test_ast_endpoints_inventory():
    """階段 A — verify 所有 9 個必要 endpoint 都定義了。"""
    found = set(find_endpoints_in_server_py())
    missing = [ep for ep in EXPECTED_ENDPOINTS if ep not in found]
    extra = [ep for ep in found if ep not in EXPECTED_ENDPOINTS]
    if missing:
        raise AssertionError(f"server.py missing endpoints: {missing}")
    print(f"  ✓ server.py defines all {len(EXPECTED_ENDPOINTS)} expected endpoints (AST inventory)")
    if extra:
        print(f"    note: extra endpoints found (not necessarily a problem): {extra}")


def test_ast_server_py_parseable():
    """階段 A — verify server.py syntactically OK + 無 truncation。"""
    try:
        ast.parse(SERVER_PY.read_text(encoding="utf-8"))
    except SyntaxError as e:
        raise AssertionError(f"server.py syntax error (possibly truncated): {e}")
    # truncation check
    text = SERVER_PY.read_text(encoding="utf-8")
    if "uvicorn.run" not in text:
        raise AssertionError("server.py missing uvicorn.run block — possibly truncated")
    if not text.rstrip().endswith(")"):
        raise AssertionError(f"server.py doesn't end with `)` — possibly truncated. Last 50 chars: {text[-50:]!r}")
    print("  ✓ server.py parseable + has uvicorn.run + properly terminated")


# ============ 階段 B — FastAPI TestClient (optional) ============

def get_client():
    sys.path.insert(0, str(FRONTEND_DIR))
    sys.path.insert(0, str(PROJECT_ROOT))
    from server import app  # type: ignore
    from fastapi.testclient import TestClient  # type: ignore
    return TestClient(app)


def test_scope_counts_full():
    client = get_client()
    r = client.get("/api/scope-counts?scope=full")
    assert r.status_code == 200, r.text
    body = r.json()
    assert "counts" in body
    for key in ("entities", "dialogue_lines", "art_assets", "qa_reports"):
        assert key in body["counts"], f"missing {key} in counts"
    print("  ✓ /api/scope-counts?scope=full — entities/dialogue/assets/qa counts present")


def test_scope_counts_invalid_rejected():
    client = get_client()
    r = client.get("/api/scope-counts?scope=invalid_wat")
    assert r.status_code == 400
    print("  ✓ /api/scope-counts rejects invalid scope")


def test_assets_all():
    client = get_client()
    r = client.get("/api/assets?scope=all")
    assert r.status_code == 200, r.text
    body = r.json()
    assert "assets" in body and "total" in body
    print(f"  ✓ /api/assets?scope=all — {body['total']} assets")


def test_assets_subtype_filter():
    client = get_client()
    r = client.get("/api/assets?scope=subtype/portrait")
    assert r.status_code == 200, r.text
    print("  ✓ /api/assets?scope=subtype/portrait")


def test_scenes_list():
    """Phase A.0F.3 自加 endpoint。"""
    client = get_client()
    r = client.get("/api/scenes")
    assert r.status_code == 200, r.text
    body = r.json()
    for key in ("scenes", "total", "chapters"):
        assert key in body
    for s in body["scenes"]:
        for key in ("scene_id", "pipeline_state", "dialogue_versions", "qa_report_count"):
            assert key in s, f"scene missing {key}: {s}"
    print(f"  ✓ /api/scenes — {body['total']} scenes, {len(body['chapters'])} chapters")


def test_scenes_chapter_filter():
    client = get_client()
    r = client.get("/api/scenes?chapter=01")
    assert r.status_code == 200, r.text
    body = r.json()
    for s in body["scenes"]:
        assert s.get("chapter") == "01" or s["scene_id"].startswith("S-01-"), s
    print(f"  ✓ /api/scenes?chapter=01 — {body['total']} scenes")


def test_scene_header_404():
    client = get_client()
    r = client.get("/api/scene/S-99-99/header")
    assert r.status_code == 404
    print("  ✓ /api/scene/S-99-99/header → 404")


def test_scene_versions_404():
    client = get_client()
    r = client.get("/api/scenes/S-99-99/versions")
    assert r.status_code == 404
    print("  ✓ /api/scenes/S-99-99/versions → 404")


def test_scene_key_lines_404():
    client = get_client()
    r = client.get("/api/scenes/S-99-99/keys/dlg.ch99.s99.l001/lines")
    assert r.status_code == 404
    print("  ✓ /api/scenes/S-99-99/keys/.../lines → 404")


def test_asset_usage_404():
    client = get_client()
    r = client.get("/api/assets/A-portrait-nonexistent-default/usage")
    assert r.status_code == 404
    print("  ✓ /api/assets/<unknown>/usage → 404")


def test_save_scene_missing_body():
    client = get_client()
    r = client.post("/api/scene/S-01-01/save", json={})
    assert r.status_code in (400, 404, 422), f"got {r.status_code}: {r.text}"
    print(f"  ✓ /api/scene/S-01-01/save with empty body → {r.status_code}")


# ============ Phase A.0F.patch-P0 Stage B regression ============

def test_version_content_missing_path():
    """Phase A.0F.patch-P0: version-content endpoint requires `path` query."""
    client = get_client()
    r = client.get("/api/scene/S-01-01/version-content")
    assert r.status_code == 400, f"expected 400 (missing path), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/S-01-01/version-content (no path) → 400")


def test_version_content_path_outside_dialogue_root():
    """Phase A.0F.patch-P0: reject paths outside 08_dialogue_outputs/."""
    client = get_client()
    # Try a path that exists in repo but is outside DIALOGUE_ROOT.
    r = client.get("/api/scene/S-01-01/version-content?path=_design/SPEC.md")
    assert r.status_code == 404, f"expected 404 (out of dialogue root), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/.../version-content with out-of-root path → 404")


def test_version_content_path_traversal_rejected():
    """Phase A.0F.patch-P0: reject .. traversal even if prefixed with 08_dialogue_outputs/."""
    client = get_client()
    r = client.get("/api/scene/S-01-01/version-content?path=08_dialogue_outputs/../_design/SPEC.md")
    assert r.status_code == 404, f"expected 404 (traversal), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/.../version-content with .. traversal → 404")


def test_version_content_unknown_scene_path():
    """Phase A.0F.patch-P0: reject path that does not exist."""
    client = get_client()
    r = client.get("/api/scene/S-99-99/version-content?path=08_dialogue_outputs/CH99_S99_dialogue_v01.md")
    assert r.status_code == 404, f"expected 404 (missing), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/.../version-content with nonexistent path → 404")


def test_save_scene_missing_target_path():
    """Phase A.0F.patch-P0: save requires target_path; absence → 400, not silent latest-mtime resolve."""
    client = get_client()
    r = client.post("/api/scene/S-01-01/save", json={"content": "hi", "mtime_baseline": 0})
    assert r.status_code == 400, f"expected 400 (no target_path), got {r.status_code}: {r.text}"
    assert "target_path" in r.text
    print("  ✓ /api/scene/S-01-01/save without target_path → 400")


def test_save_scene_target_path_outside_dialogue():
    """Phase A.0F.patch-P0: save rejects target_path outside dialogue root."""
    client = get_client()
    r = client.post("/api/scene/S-01-01/save", json={
        "content": "hi",
        "mtime_baseline": 0,
        "target_path": "_design/SPEC.md",
    })
    assert r.status_code == 404, f"expected 404 (outside dialogue root), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/.../save with out-of-root target_path → 404")


def test_save_scene_as_missing_target_path():
    """Phase A.0F.patch-P0: save-as requires target_path too."""
    client = get_client()
    r = client.post("/api/scene/S-01-01/save-as", json={"content": "hi"})
    assert r.status_code == 400, f"expected 400 (no target_path), got {r.status_code}: {r.text}"
    print("  ✓ /api/scene/S-01-01/save-as without target_path → 400")


# ============ Phase A.0F.patch-major-1 / D-045 Stage B regression ============

def test_scope_counts_outline_only():
    """Phase A.0F.patch-round2-P2 / option (a): /api/scope-counts supports
    scope=outline_only per L3 schema §1.3.

    Checks:
      - 200 (no longer 400)
      - counts.entities.S == 0 (scene bodies excluded)
      - counts.entities.A == 0 (D-045 + outline_only both exclude A-*)
      - counts.art_assets == 0 (A-* excluded from outline scope)
      - body['scope'] == 'outline_only' so the front-end can verify the
        scope-counts response actually answers the requested scope.
    """
    client = get_client()
    r = client.get("/api/scope-counts?scope=outline_only")
    assert r.status_code == 200, f"expected 200 outline_only, got {r.status_code}: {r.text}"
    body = r.json()
    assert body.get("scope") == "outline_only", f"scope field mismatch: {body.get('scope')}"
    entities = body["counts"].get("entities", {})
    assert entities.get("S", 0) == 0, (
        f"outline_only must exclude scene bodies; entities.S = {entities.get('S')}"
    )
    assert entities.get("A", 0) == 0, (
        f"outline_only must exclude art assets; entities.A = {entities.get('A')}"
    )
    assert body["counts"].get("art_assets", -1) == 0, (
        f"outline_only must report art_assets == 0; got {body['counts'].get('art_assets')}"
    )
    print("  â /api/scope-counts?scope=outline_only â 200; S/A excluded; art_assets == 0")


def test_scope_counts_excludes_a_from_entities():
    """Phase A.0F.patch-major-1 / D-045: entity_counts must NOT contain A-* art assets.

    CODEX Major finding: previously art assets were merged into entity_counts,
    inflating the narrative readiness denominator. After the patch the asset
    panel still tracks A-* (via counts.art_assets), but counts.entities['A']
    should stay 0 even when 10_art_assets/ has registered assets.
    """
    client = get_client()
    r = client.get("/api/scope-counts?scope=full")
    assert r.status_code == 200, r.text
    body = r.json()
    entities = body["counts"].get("entities", {})
    assert entities.get("A", 0) == 0, (
        f"counts.entities['A'] must be 0 per D-045; got {entities.get('A')}"
    )
    # art_assets still reported via counts.art_assets
    assert isinstance(body["counts"].get("art_assets", 0), int)
    print("  ✓ /api/scope-counts: counts.entities['A'] == 0 (D-045 narrative separation)")


# ============ runner ============

STAGE_A_TESTS = [
    test_ast_endpoints_inventory,
    test_ast_server_py_parseable,
]

STAGE_B_TESTS = [
    test_scope_counts_full,
    test_scope_counts_invalid_rejected,
    test_assets_all,
    test_assets_subtype_filter,
    test_scenes_list,
    test_scenes_chapter_filter,
    test_scene_header_404,
    test_scene_versions_404,
    test_scene_key_lines_404,
    test_asset_usage_404,
    test_save_scene_missing_body,
    # Phase A.0F.patch-P0 regression tests
    test_version_content_missing_path,
    test_version_content_path_outside_dialogue_root,
    test_version_content_path_traversal_rejected,
    test_version_content_unknown_scene_path,
    test_save_scene_missing_target_path,
    test_save_scene_target_path_outside_dialogue,
    test_save_scene_as_missing_target_path,
    # Phase A.0F.patch-major-1 D-045 regression
    test_scope_counts_excludes_a_from_entities,
    # Phase A.0F.patch-round2-P2 / option (a) regression
    test_scope_counts_outline_only,
]


def _force_utf8_console() -> None:
    """Phase A.0F.patch-round3 (CODEX 3rd review NEAR-GO finding):
    Reconfigure stdout/stderr to UTF-8 with error replacement so that the
    test output (which uses ✓ / ✗ / ⏭ markers plus Chinese explanatory text)
    does not raise UnicodeEncodeError under Windows CP950 / Big5 default
    consoles. Acceptance must work without requiring the runner to set
    PYTHONIOENCODING=utf-8 externally; otherwise the script crashes before
    any test runs and the harness reports a misleading failure.

    Falls back silently on old Python (< 3.7) or non-standard stdout
    streams that lack reconfigure(); in those cases the behavior matches
    pre-patch (caller may still set PYTHONIOENCODING=utf-8 as escape hatch).
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError, AttributeError):
            # Stream cannot be reconfigured (e.g. wrapped pipe, BytesIO);
            # silently ignore — caller can still PYTHONIOENCODING=utf-8.
            continue


def main():
    _force_utf8_console()
    print("Phase A.0F integration smoke test")
    print()

    # Phase A.0F.patch-round2-P1 (CODEX 2nd review finding #1):
    # `--allow-stage-b-skip` opt-in is required to treat a Stage B skip
    # (caused by missing fastapi / httpx) as a clean exit. Without the flag,
    # a skip exits with code 2, so CI / host acceptance scripts can no longer
    # mistake a silent skip for a passing run. Stage A still runs
    # unconditionally so sandbox / sandbox-like environments can call this
    # script with the opt-in flag and still get the AST inventory check.
    allow_stage_b_skip = "--allow-stage-b-skip" in sys.argv

    print("Stage A — stdlib AST inventory check (沙箱可跑):")
    passed_a, failed_a = 0, 0
    for t in STAGE_A_TESTS:
        try:
            t()
            passed_a += 1
        except Exception as e:
            failed_a += 1
            print(f"  ✗ {t.__name__}: {type(e).__name__}: {e}")
    print(f"  Stage A: {passed_a} passed, {failed_a} failed")
    print()

    print("Stage B — FastAPI TestClient (需要 fastapi + httpx 已裝):")
    try:
        get_client()
    except (ImportError, ModuleNotFoundError) as e:
        print(f"  ⏭  Stage B SKIPPED — {e}")
        print(f"     在 host 端跑：cd _tools/frontend && pip install -r requirements.txt && python tests/test_endpoints_smoke.py")
        if allow_stage_b_skip:
            print("     --allow-stage-b-skip: 容許 skip（沙箱模式）")
            return 0 if failed_a == 0 else 1
        print("     Stage B skip → exit code 2（acceptance 必須 install fastapi+httpx 後跑完 Stage B；")
        print("     若你確定要容許 skip，加 --allow-stage-b-skip flag）")
        return 2
    except Exception as e:
        print(f"  ⏭  Stage B SKIPPED — client init failed: {e}")
        if allow_stage_b_skip:
            return 0 if failed_a == 0 else 1
        return 2

    passed_b, failed_b = 0, 0
    for t in STAGE_B_TESTS:
        try:
            t()
            passed_b += 1
        except Exception as e:
            failed_b += 1
            print(f"  ✗ {t.__name__}: {type(e).__name__}: {e}")
    print(f"  Stage B: {passed_b} passed, {failed_b} failed")
    print()

    total_failed = failed_a + failed_b
    total_passed = passed_a + passed_b
    print(f"Total: {total_passed} passed, {total_failed} failed")
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
