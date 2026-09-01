from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import stat
import sys


SOURCE = Path(
    "/private/tmp/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901"
)
COPY = Path("/private/tmp/p142_hostile_audit_copy.oKqmYk/frozen")
STAGE = SOURCE / "release_stage"
AUGMENTATION = SOURCE / "source_augmentation"

EXPECTED_TARGETS = {
    "STATEMENT.tex": "cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2",
    "PROOF.tex": "7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac",
    "EXAMPLE.tex": "7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f",
}
EXPECTED_MANIFESTS = {
    "top": "3c72e3bac7cb2b301d895c4b5437971fb5edf26f861985e761cd2a89e5b7492d",
    "release": "0269bcf8d447dc82130673e34dfe3373947d6aa9f20fcedbf594bc475d654e28",
    "augmentation": "f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739",
}
EXPECTED_LOCATORS = {
    "mp_2409_06221v2": ((413, 423),),
    "dxz_2302_02541v3": ((437, 458), (848, 880), (873, 925)),
    "darvas_xia_2003_04818": ((1055, 1185),),
    "del_math0002035": ((596, 613),),
    "xia_2312_17150v3": ((628, 647),),
}
EXPECTED_BLOCKS = {
    ("mp_2409_06221v2", 413, 423): (
        "64ed7a96232e79bb48046eadbb457d5109b85180f85c82cb22102840cd352ba9",
        ("Definition 1.3.1", "v(I · J) = v(I) + v(J)", "v(0X ) = +∞", "pointwise convergence topology"),
    ),
    ("dxz_2302_02541v3", 437, 458): (
        "ea3e5175a81fa1333e05dabd2603d08e854310abceccf655e90bc2c3a91e5d1f",
        ("relative test curve", "τψ+ := inf", "finite energy test curve", "is I-maximal if"),
    ),
    ("dxz_2302_02541v3", 848, 880): (
        "bdd2227acada970abb87fc7a02c0ef00d1ddebed1075ce035e5479bb9e8652c4",
        ("pseudoeffective transcendental class", "natural transition map", "if τ < τψ+", "if τ = τψ+", "if τ > τψ+", "(28)"),
    ),
    ("dxz_2302_02541v3", 873, 925): (
        "ce8a48c466c99ad8d9190fa8d57c2c585f195ada9d06830a0a7667b7be26b77a",
        ("Definition 3.3", "projective limit", "does not depend on the choice", "(29)", "Theorem 3.4", "Proposition 2.18(ii)"),
    ),
    ("darvas_xia_2003_04818", 1055, 1185): (
        "5e50e2e072684288699d9ed22e447521525ac9d502b711291ff23225e7c938c0",
        ("Deﬁnition 2.12", "I-singularity types", "Proposition 2.18", "(ii) ϕ ≃I P [ϕ]I", "strong", "openness theorem"),
    ),
    ("del_math0002035", 596, 613): (
        "c82bb610754010ef77b61d0265103fc7bb29d66ffc7e156e8b77c8886e4e577d",
        ("Theorem 2.6", "(ii) Let X be a complex manifold", "J (φ + ψ) ⊆ J (φ) · J (ψ)", "diagonal trick"),
    ),
    ("xia_2312_17150v3", 628, 647): (
        "a24ab4718fbc3ea3b411948c7f53010d4dedb8e404f7be414cd75740c3c97180",
        ("v (I(kϕ))", "(3.8)", "v 7→ sup", "independent of the choice of ω", "Theorem 3.12", "a bijection."),
    ),
}
NORMALIZED = {
    "mp_2409.06221v2.txt": "724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d",
    "dxz_2302.02541v3.txt": "3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9",
    "darvas_xia_2003.04818.txt": "794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed",
    "demailly_ein_lazarsfeld_math0002035.txt": "0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3",
    "xia_2312.17150v3.txt": "a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d",
}
PDFS = {
    "mp_2409.06221v2.pdf": "9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23",
    "dxz_2302.02541v3.pdf": "7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c",
    "darvas_xia_2003.04818.pdf": "a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61",
    "demailly_ein_lazarsfeld_math0002035.pdf": "59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2",
    "xia_2312.17150v3.pdf": "773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9",
}


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def snapshot(root: Path) -> tuple[list[dict[str, object]], str]:
    paths = [root, *sorted(root.rglob("*"))]
    rows: list[dict[str, object]] = []
    for path in paths:
        info = path.lstat()
        relative = "." if path == root else path.relative_to(root).as_posix()
        if stat.S_ISDIR(info.st_mode):
            kind = "directory"
            require(stat.S_IMODE(info.st_mode) == 0o555, f"directory mode: {relative}")
            rows.append({"path": relative, "kind": kind, "mode": "0555"})
        elif stat.S_ISREG(info.st_mode):
            kind = "regular"
            require(stat.S_IMODE(info.st_mode) == 0o444, f"file mode: {relative}")
            rows.append(
                {
                    "path": relative,
                    "kind": kind,
                    "mode": "0444",
                    "bytes": info.st_size,
                    "sha256": digest(path),
                }
            )
        else:
            raise RuntimeError(f"symlink or special entry: {relative}")
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()
    return rows, digest_bytes(payload)


def parse_manifest(
    root: Path, expected_digest: str, *, require_sorted: bool = True
) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    require(digest(manifest) == expected_digest, f"manifest digest: {root}")
    raw = manifest.read_bytes()
    require(raw.endswith(b"\n") and b"\r" not in raw, f"manifest line endings: {root}")
    result: dict[str, str] = {}
    order: list[str] = []
    for raw_line in raw.split(b"\n")[:-1]:
        line = raw_line.decode("utf-8")
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {line!r}")
        sha256, relative = match.groups()
        require(relative not in result, f"duplicate manifest row: {relative}")
        require(not relative.startswith(("/", "../")) and "/../" not in relative, f"unsafe manifest row: {relative}")
        result[relative] = sha256
        order.append(relative)
    if require_sorted:
        require(order == sorted(order), f"unsorted manifest: {root}")
    actual = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.relative_to(root).as_posix() != "SHA256SUMS"
    )
    require(sorted(result) == actual, f"manifest inventory mismatch: {root}")
    for relative, sha256 in result.items():
        require(digest(root / relative) == sha256, f"manifest byte mismatch: {root}/{relative}")
    return result


def load_pins():
    sys.dont_write_bytecode = True
    path = STAGE / "runtime/release_pins.py"
    spec = importlib.util.spec_from_file_location("independent_frozen_pins", path)
    require(spec is not None and spec.loader is not None, "pin module loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lf_lines(path: Path) -> list[str]:
    chunks = path.read_bytes().split(b"\x0a")
    if chunks and chunks[-1] == b"":
        chunks.pop()
    return [chunk.decode("utf-8", errors="replace") for chunk in chunks]


def main() -> None:
    source_rows, source_snapshot = snapshot(SOURCE)
    copy_rows, copy_snapshot = snapshot(COPY)
    require(source_rows == copy_rows, "disposable copy differs from source")

    top = parse_manifest(SOURCE, EXPECTED_MANIFESTS["top"])
    release = parse_manifest(STAGE, EXPECTED_MANIFESTS["release"])
    augmentation = parse_manifest(
        AUGMENTATION, EXPECTED_MANIFESTS["augmentation"], require_sorted=False
    )
    require((len(top), len(release), len(augmentation)) == (92, 56, 11), "manifest row counts")

    forbidden: list[str] = []
    for path in SOURCE.rglob("*"):
        relative = path.relative_to(SOURCE).as_posix()
        parts = path.parts
        if "__pycache__" in parts or path.suffix == ".pyc" or path.name == ".DS_Store":
            forbidden.append(relative)
        if relative.startswith("release_stage/artifacts/") or relative == "release_stage/artifacts":
            forbidden.append(relative)
        if relative.startswith("release_stage/STATIC_MODEL_LONG_SMOKE/") or relative == "release_stage/STATIC_MODEL_LONG_SMOKE":
            forbidden.append(relative)
    require(not forbidden, f"cache/artifact/smoke paths: {forbidden}")

    target_evidence: dict[str, str] = {}
    for name, expected in EXPECTED_TARGETS.items():
        outer = SOURCE / "target" / name
        staged = STAGE / "target" / name
        require(digest(outer) == digest(staged) == expected, f"target preservation: {name}")
        target_evidence[name] = expected

    normalization: dict[str, dict[str, object]] = {}
    for name, expected_release_sha in NORMALIZED.items():
        raw = (AUGMENTATION / name).read_bytes()
        staged = (STAGE / "runtime/sources" / name).read_bytes()
        require(not raw.endswith(b"\n") and raw.endswith(b"\f"), f"raw terminal form: {name}")
        require(staged == raw + b"\n", f"not exact raw plus LF: {name}")
        require(digest_bytes(staged) == expected_release_sha, f"normalized hash: {name}")
        normalization[name] = {
            "raw_bytes": len(raw),
            "raw_sha256": digest_bytes(raw),
            "release_bytes": len(staged),
            "release_sha256": expected_release_sha,
            "terminal_hex": staged[-3:].hex(),
        }
    for name, expected in PDFS.items():
        raw = AUGMENTATION / name
        staged = STAGE / "runtime/sources" / name
        require(raw.read_bytes() == staged.read_bytes(), f"PDF preservation: {name}")
        require(digest(raw) == expected, f"PDF hash: {name}")

    pins = load_pins()
    require(digest(STAGE / "runtime/release_pins.py") == "5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6", "pins file hash")
    require(pins.RELEASE_PINSET_SHA256 == "0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf", "declared canonical pin")
    require(pins.canonical_pinset_sha256() == pins.RELEASE_PINSET_SHA256, "computed canonical pin")
    require((len(pins.FIXED_SOURCE_RUNTIME_PATHS), len(pins.SOURCE_BUNDLE_PINS), len(pins.TARGET_BUNDLE_PINS)) == (22, 39, 3), "pin counts")
    for relative, pin in pins.SOURCE_BUNDLE_PINS.items():
        path = STAGE / "runtime" / relative
        require(path.lstat().st_size == pin["bytes"] and digest(path) == pin["sha256"], f"source pin: {relative}")
    for relative, pin in pins.TARGET_BUNDLE_PINS.items():
        path = STAGE / relative
        require(path.lstat().st_size == pin["bytes"] and digest(path) == pin["sha256"], f"target pin: {relative}")

    actual_locators = {
        source_id: tuple((start, end) for start, end, _ in locators)
        for source_id, locators in pins.P142_SOURCE_LOCATORS.items()
    }
    require(actual_locators == EXPECTED_LOCATORS, "locator map")
    block_evidence: dict[str, dict[str, object]] = {}
    for (source_id, start, end), (expected_sha, fragments) in EXPECTED_BLOCKS.items():
        relative = pins.FIXED_SOURCE_RUNTIME_PATHS[source_id]
        block = "\n".join(lf_lines(STAGE / "runtime" / relative)[start - 1 : end])
        actual_sha = digest_bytes(block.encode("utf-8"))
        require(actual_sha == expected_sha, f"locator block hash: {source_id}:{start}-{end}")
        missing = [fragment for fragment in fragments if fragment not in block]
        require(not missing, f"locator semantic omissions: {source_id}:{start}-{end}:{missing}")
        block_evidence[f"{source_id}:{start}-{end}"] = {
            "sha256": actual_sha,
            "semantic_fragments": list(fragments),
        }

    helper = (STAGE / "runtime/lf_source_lines.py").read_text(encoding="utf-8")
    service = (STAGE / "runtime/hardened_service.py").read_text(encoding="utf-8")
    mcp = (STAGE / "runtime/hardened_mcp.py").read_text(encoding="utf-8")
    runner = (STAGE / "run_static_model_long_smoke.py").read_text(encoding="utf-8")
    release_checker = (STAGE / "check_release.py").read_text(encoding="utf-8")
    require('split(b"\\x0a")' in helper and ".splitlines(" not in helper, "LF helper implementation")
    require(".splitlines(" not in service and ".splitlines(" not in mcp, "generic source line split")
    require(service.count("read_lf_only_source_lines(") == 3, "host helper call count")
    require(mcp.count("read_lf_only_source_lines(") == 3, "MCP helper call count")
    synthetic = b"alpha\fbeta\rcarriage\x0bvertical\nsecond\n"
    chunks = synthetic.split(b"\x0a")
    if chunks[-1] == b"":
        chunks.pop()
    require(chunks == [b"alpha\fbeta\rcarriage\x0bvertical", b"second"], "synthetic LF addressing")

    for marker in (
        "os.openpty()",
        "stdin=stdin_slave_fd",
        "stdout=stdout_handle",
        "stderr=stderr_handle",
        "if process.poll() is not None:",
        '"exited_before_scan"',
        '"exited_during_scan"',
    ):
        require(marker in runner, f"smoke runner marker: {marker}")
    require("stderr=subprocess.STDOUT" not in runner, "merged smoke streams")
    require(runner.count("if process.poll() is not None:") >= 2, "poll gates")
    for checker_marker in (
        "validate_stdout_smoke",
        "validate_stderr_smoke",
        "validate_process_samples",
        "validate_cache_horizon_bracketing",
        'receipt.get("stdin_strategy") == "dedicated-pty-no-input"',
        "terminal process observation",
    ):
        require(checker_marker in release_checker, f"release checker coverage: {checker_marker}")

    old_manifest = SOURCE / "input_bindings/P142_V1_STAGE_SHA256SUMS"
    old_rows: dict[str, str] = {}
    for line in old_manifest.read_bytes().decode("utf-8").split("\n")[:-1]:
        sha256, relative = line.split("  ", 1)
        old_rows[relative] = sha256
    changed = sorted(path for path, sha256 in old_rows.items() if release.get(path) != sha256)
    added = sorted(set(release) - set(old_rows))
    unchanged = sorted(path for path, sha256 in old_rows.items() if release.get(path) == sha256)
    require((len(old_rows), len(changed), len(added), len(unchanged)) == (55, 8, 1, 47), "preservation ledger counts")
    require(added == ["runtime/lf_source_lines.py"], "preservation added path")
    protected = [path for path in unchanged if path.startswith("runtime/sources/") or path.startswith("target/")]
    require(len(protected) == 42, "39 sources plus three targets preserved")

    evidence = {
        "status": "PASS",
        "source": str(SOURCE),
        "disposable_copy": str(COPY),
        "entry_count_including_root": len(source_rows),
        "directory_count": sum(row["kind"] == "directory" for row in source_rows),
        "regular_file_count": sum(row["kind"] == "regular" for row in source_rows),
        "source_tree_snapshot_sha256": source_snapshot,
        "copy_tree_snapshot_sha256": copy_snapshot,
        "manifest_sha256": EXPECTED_MANIFESTS,
        "manifest_rows": {"top": len(top), "release": len(release), "augmentation": len(augmentation)},
        "target_sha256": target_evidence,
        "source_normalization": normalization,
        "canonical_pinset_sha256": pins.canonical_pinset_sha256(),
        "release_pins_sha256": digest(STAGE / "runtime/release_pins.py"),
        "source_route_count": len(pins.FIXED_SOURCE_RUNTIME_PATHS),
        "source_bundle_file_count": len(pins.SOURCE_BUNDLE_PINS),
        "target_bundle_file_count": len(pins.TARGET_BUNDLE_PINS),
        "locator_blocks": block_evidence,
        "preservation": {
            "old_rows": len(old_rows),
            "unchanged": len(unchanged),
            "changed": changed,
            "added": added,
            "protected_39_sources_plus_3_targets": len(protected),
        },
        "forbidden_paths": forbidden,
        "lf_only": {
            "host_calls": service.count("read_lf_only_source_lines("),
            "mcp_calls": mcp.count("read_lf_only_source_lines("),
            "generic_splitlines_host_mcp": service.count(".splitlines(") + mcp.count(".splitlines("),
            "synthetic_non_lf_separators_preserved": True,
        },
        "smoke_static_gates": {
            "separate_stdout_stderr": True,
            "dedicated_no_input_pty": True,
            "poll_before_and_after": True,
            "terminal_observation": True,
            "checker_stdout_stderr_process_horizon_coverage": True,
        },
    }
    print(json.dumps(evidence, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
