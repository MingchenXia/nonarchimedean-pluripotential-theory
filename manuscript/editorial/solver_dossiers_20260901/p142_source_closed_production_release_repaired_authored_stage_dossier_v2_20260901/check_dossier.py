from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
STAGE = ROOT / "release_stage"
AUGMENTATION = ROOT / "source_augmentation"
TARGET = ROOT / "target"
BINDINGS = ROOT / "input_bindings"
TEST_PYTHON = Path(
    "/Users/mingchen/Projects/Yethlas/Rethlas_mixed_hessian_20260827/"
    "agents/verification/tmp/verification-venv/bin/python"
)

STAGE_MANIFEST_SHA = "0269bcf8d447dc82130673e34dfe3373947d6aa9f20fcedbf594bc475d654e28"
AUGMENTATION_MANIFEST_SHA = "f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739"
CANDIDATE_MANIFEST_SHA = "56e2084c2264dad4bb83f0d2bdd4e3348933002a6c9d9a6821ab02ae1686cdff"
PRIOR_AUDIT_MANIFEST_SHA = "f5dd709eb704332eb0fb29ec730de0d9285ecf69190c07578ec89d625d9c31e3"
PRIOR_AUDIT_REPORT_SHA = "ff611efe9a228dd547b9438349e90ddf7be417dfe32f0b5d0130d03fe88c515c"
PRIOR_AUDIT_RESULT_SHA = "a215a206d69af36f2828091799da215b317f29bedb848b03a85bb2182fa1d38d"
PINSET_SHA = "0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf"
PINS_FILE_SHA = "5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6"
V1_AUTHORED_MANIFEST_SHA = "4007c71e7ac04f02ac92ac90cda83c7142389a29835ac428f612d183271720a0"
V1_STAGE_MANIFEST_SHA = "2c3690aedd7e11adcb59add7570f539d01148e2c93dbe088f723860d8417dc2a"
P142_FAIL_AUDIT_MANIFEST_SHA = "7055f4d3765cd2e6c47d1bde0f39a6fc712b5ecef16938a3426892675d2d28f8"
P142_FAIL_AUDIT_REPORT_SHA = "61787eab970e8101e80b2cbd83c85ada41e1731860b984a0393655af38267e7a"
P142_FAIL_AUDIT_RESULT_SHA = "70ab621fe17e8f5581cf61ee2aeb1e55d81b2c3df747b1c4b26fe83bebe62f1b"
P148_REPAIR_AUTHORED_MANIFEST_SHA = "bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30"
P148_REPAIR_FAIL_AUDIT_MANIFEST_SHA = "d4843c62df5c706b76bf689484b254eb84b955872117c567b2846ac4c1baac77"
P148_REPAIR_FAIL_AUDIT_REPORT_SHA = "0c95831ab3b4094775c655310143c035f5ad9373992e2e24d01d97fb7fa4ebca"
P148_REPAIR_FAIL_AUDIT_RESULT_SHA = "e0132758e219752ae3151339e47604835507e65129074f34b84c0fe2f6c5b8ae"
TEST_COUNT = 163

TARGET_PINS = {
    "STATEMENT.tex": "cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2",
    "PROOF.tex": "7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac",
    "EXAMPLE.tex": "7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f",
}

NORMALIZED_TEXTS = {
    "mp_2409.06221v2.txt": (
        "mp_2409_06221v2",
        "724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d",
    ),
    "dxz_2302.02541v3.txt": (
        "dxz_2302_02541v3",
        "3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9",
    ),
    "darvas_xia_2003.04818.txt": (
        "darvas_xia_2003_04818",
        "794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed",
    ),
    "demailly_ein_lazarsfeld_math0002035.txt": (
        "del_math0002035",
        "0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3",
    ),
    "xia_2312.17150v3.txt": (
        "xia_2312_17150v3",
        "a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d",
    ),
}

PDFS = {
    "mp_2409.06221v2.pdf": "9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23",
    "dxz_2302.02541v3.pdf": "7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c",
    "darvas_xia_2003.04818.pdf": "a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61",
    "demailly_ein_lazarsfeld_math0002035.pdf": "59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2",
    "xia_2312.17150v3.pdf": "773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9",
}

LOCATORS = {
    "mp_2409_06221v2": ((413, 423),),
    "dxz_2302_02541v3": ((437, 458), (848, 880), (873, 925)),
    "darvas_xia_2003_04818": ((1055, 1185),),
    "del_math0002035": ((596, 613),),
    "xia_2312_17150v3": ((628, 647),),
}

LOCATOR_BLOCKS = {
    ("mp_2409_06221v2", 413, 423): "64ed7a96232e79bb48046eadbb457d5109b85180f85c82cb22102840cd352ba9",
    ("dxz_2302_02541v3", 437, 458): "ea3e5175a81fa1333e05dabd2603d08e854310abceccf655e90bc2c3a91e5d1f",
    ("dxz_2302_02541v3", 848, 880): "bdd2227acada970abb87fc7a02c0ef00d1ddebed1075ce035e5479bb9e8652c4",
    ("dxz_2302_02541v3", 873, 925): "ce8a48c466c99ad8d9190fa8d57c2c585f195ada9d06830a0a7667b7be26b77a",
    ("darvas_xia_2003_04818", 1055, 1185): "5e50e2e072684288699d9ed22e447521525ac9d502b711291ff23225e7c938c0",
    ("del_math0002035", 596, 613): "c82bb610754010ef77b61d0265103fc7bb29d66ffc7e156e8b77c8886e4e577d",
    ("xia_2312_17150v3", 628, 647): "a24ab4718fbc3ea3b411948c7f53010d4dedb8e404f7be414cd75740c3c97180",
}


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lf_only_lines(path: Path) -> list[str]:
    chunks = path.read_bytes().split(b"\x0a")
    if chunks and chunks[-1] == b"":
        chunks.pop()
    return [chunk.decode("utf-8", errors="replace") for chunk in chunks]


def check_frozen_modes() -> None:
    for path in [ROOT, *sorted(ROOT.rglob("*"))]:
        info = path.lstat()
        relative = "." if path == ROOT else path.relative_to(ROOT).as_posix()
        mode = stat.S_IMODE(info.st_mode)
        if stat.S_ISDIR(info.st_mode):
            require(mode == 0o555, f"directory is not frozen 0555: {relative}: {mode:o}")
        elif stat.S_ISREG(info.st_mode):
            require(mode == 0o444, f"regular file is not frozen 0444: {relative}: {mode:o}")
        else:
            raise RuntimeError(f"non-regular frozen-tree entry: {relative}")


def strict_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(path: Path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=strict_pairs,
        parse_constant=lambda item: (_ for _ in ()).throw(
            RuntimeError(f"nonfinite JSON value: {item}")
        ),
    )


def regular_tree_fingerprint(root: Path):
    info = root.lstat()
    require(stat.S_ISDIR(info.st_mode) and not stat.S_ISLNK(info.st_mode), f"bad root: {root}")
    rows = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        item = path.lstat()
        require(not stat.S_ISLNK(item.st_mode), f"symlink: {relative}")
        if stat.S_ISDIR(item.st_mode):
            rows.append((relative + "/", "directory", stat.S_IMODE(item.st_mode)))
            continue
        require(stat.S_ISREG(item.st_mode), f"special file: {relative}")
        require("__pycache__" not in path.parts and path.suffix != ".pyc", f"cache: {relative}")
        require(path.name != ".DS_Store", f"Finder metadata: {relative}")
        rows.append((relative, item.st_size, sha(path), stat.S_IMODE(item.st_mode)))
    return rows


def parse_manifest(
    root: Path, expected_sha: str | None = None, *, require_sorted: bool = True
):
    manifest = root / "SHA256SUMS"
    if expected_sha is not None:
        require(sha(manifest) == expected_sha, f"manifest digest: {root}")
    text = manifest.read_text(encoding="utf-8")
    require(text.endswith("\n"), f"manifest terminal LF: {root}")
    rows = {}
    order = []
    for line in text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate manifest path: {relative}")
        require(not relative.startswith(("/", "../")) and "/../" not in relative, f"unsafe path: {relative}")
        rows[relative] = digest
        order.append(relative)
    if require_sorted:
        require(order == sorted(order), f"unsorted manifest: {root}")
    actual = []
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        relative = path.relative_to(root).as_posix()
        if relative != "SHA256SUMS":
            actual.append(relative)
    require(sorted(rows) == sorted(actual), f"manifest inventory: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest byte mismatch: {root}/{relative}")
    return rows


def parse_manifest_file(path: Path) -> dict[str, str]:
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), f"bound manifest lacks terminal LF: {path.name}")
    rows: dict[str, str] = {}
    order: list[str] = []
    for line in raw.decode("utf-8").split("\n")[:-1]:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed bound manifest row: {path.name}: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate bound manifest path: {relative}")
        rows[relative] = digest
        order.append(relative)
    require(order == sorted(order), f"unsorted bound manifest: {path.name}")
    return rows


def check_preservation_ledgers() -> None:
    old_rows = parse_manifest_file(BINDINGS / "P142_V1_STAGE_SHA256SUMS")
    new_rows = parse_manifest(STAGE, STAGE_MANIFEST_SHA)
    changed = {path for path in old_rows if new_rows.get(path) != old_rows[path]}
    added = set(new_rows) - set(old_rows)
    expected_changed = {
        "STAGING_REPORT.md",
        "check_release.py",
        "run_static_model_long_smoke.py",
        "runtime/contract.md",
        "runtime/hardened_mcp.py",
        "runtime/hardened_service.py",
        "runtime/release_pins.py",
        "tests/test_runtime.py",
    }
    require(changed == expected_changed, f"changed-file ledger mismatch: {sorted(changed)}")
    require(added == {"runtime/lf_source_lines.py"}, f"added-file ledger mismatch: {sorted(added)}")
    unchanged = set(old_rows) - changed
    require(len(old_rows) == 55 and len(new_rows) == 56 and len(unchanged) == 47,
            "release preservation row counts")
    for relative in unchanged:
        require(sha(STAGE / relative) == old_rows[relative],
                f"preserved v1 byte drift: {relative}")
    protected = {
        relative
        for relative in old_rows
        if relative.startswith("runtime/sources/") or relative.startswith("target/")
    }
    require(len(protected) == 42 and protected <= unchanged,
            "source/target preservation boundary")
    ledger = strict_json(ROOT / "BYTE_PRESERVATION.json")
    require(ledger["repaired_release_stage"]["manifest_sha256"] == STAGE_MANIFEST_SHA,
            "byte-preservation manifest binding")
    require(ledger["repaired_release_stage"]["unchanged_old_rows"] == 47,
            "byte-preservation unchanged count")
    require(set(ledger["changed_paths"]) == expected_changed,
            "byte-preservation changed paths")
    require(set(ledger["added_paths"]) == added,
            "byte-preservation added paths")
    tests = strict_json(ROOT / "TEST_RUNS.json")
    require(tests["inventory"] == TEST_COUNT,
            "test-ledger inventory")
    require(tests["final_frozen_source_runs"]["required_count"] == 2,
            "test-ledger frozen run count")


def load_module(path: Path, name: str):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"cannot import: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_input_bindings() -> None:
    require(sha(BINDINGS / "P142_CANDIDATE_SHA256SUMS") == CANDIDATE_MANIFEST_SHA, "candidate binding")
    require(sha(BINDINGS / "P142_PRIOR_AUDIT_SHA256SUMS") == PRIOR_AUDIT_MANIFEST_SHA, "prior audit manifest")
    require(sha(BINDINGS / "P142_PRIOR_AUDIT_REPORT.md") == PRIOR_AUDIT_REPORT_SHA, "prior audit report")
    require(sha(BINDINGS / "P142_PRIOR_AUDIT_RESULT.json") == PRIOR_AUDIT_RESULT_SHA, "prior audit result")
    result = strict_json(BINDINGS / "P142_PRIOR_AUDIT_RESULT.json")
    require(result["verdict"] == "PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET", "prior target audit verdict")
    for field in ("production_submitted", "live_source_modified", "inventory_modified", "git_used"):
        require(result[field] is False, f"prior target audit boundary: {field}")
    bindings = {
        "P142_V1_AUTHORED_SHA256SUMS": V1_AUTHORED_MANIFEST_SHA,
        "P142_V1_STAGE_SHA256SUMS": V1_STAGE_MANIFEST_SHA,
        "P142_V1_FAIL_AUDIT_SHA256SUMS": P142_FAIL_AUDIT_MANIFEST_SHA,
        "P142_V1_FAIL_AUDIT_REPORT.md": P142_FAIL_AUDIT_REPORT_SHA,
        "P142_V1_FAIL_AUDIT_RESULT.json": P142_FAIL_AUDIT_RESULT_SHA,
        "P148_SMOKE_REPAIR_AUTHORED_SHA256SUMS": P148_REPAIR_AUTHORED_MANIFEST_SHA,
        "P148_SMOKE_REPAIR_FAIL_AUDIT_SHA256SUMS": P148_REPAIR_FAIL_AUDIT_MANIFEST_SHA,
        "P148_SMOKE_REPAIR_FAIL_AUDIT_REPORT.md": P148_REPAIR_FAIL_AUDIT_REPORT_SHA,
        "P148_SMOKE_REPAIR_FAIL_AUDIT_RESULT.json": P148_REPAIR_FAIL_AUDIT_RESULT_SHA,
    }
    for name, digest in bindings.items():
        require(sha(BINDINGS / name) == digest, f"repair provenance binding: {name}")
    p142_fail = strict_json(BINDINGS / "P142_V1_FAIL_AUDIT_RESULT.json")
    require(p142_fail["verdict"] == "FAIL_SOURCE_CLOSURE_LINE_NUMBERING",
            "P14.2 failed-audit verdict binding")
    p148_fail = strict_json(BINDINGS / "P148_SMOKE_REPAIR_FAIL_AUDIT_RESULT.json")
    require(p148_fail["verdict"] == "FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE",
            "P14.8 mode/harness failed-audit verdict binding")


def check_targets() -> None:
    for name, digest in TARGET_PINS.items():
        outer = TARGET / name
        staged = STAGE / "target" / name
        require(sha(outer) == digest, f"outer target digest: {name}")
        require(sha(staged) == digest, f"staged target digest: {name}")
        require(outer.read_bytes() == staged.read_bytes(), f"target copy mismatch: {name}")


def check_source_closure(pins) -> None:
    rows = parse_manifest(
        AUGMENTATION, AUGMENTATION_MANIFEST_SHA, require_sorted=False
    )
    require(len(rows) == 11, "augmentation row count")
    require(sha(AUGMENTATION / "SOURCE_LOCATORS.md") == "cd4b22d20ed46661032f9ef3f0c18782b84e23dad0b35d2650946effb04640c7", "raw locator ledger")
    repair = (ROOT / "SOURCE_CLOSURE_REPAIR.md").read_text(encoding="utf-8")
    contract = (STAGE / "runtime/contract.md").read_text(encoding="utf-8")
    for name, (source_id, release_digest) in NORMALIZED_TEXTS.items():
        raw = (AUGMENTATION / name).read_bytes()
        release_path = STAGE / "runtime/sources" / name
        release = release_path.read_bytes()
        require(not raw.endswith(b"\n") and raw.endswith(b"\f"), f"raw terminal shape: {name}")
        require(release == raw + b"\n", f"normalization is not exact +LF: {name}")
        require(release.endswith(b"\f\n"), f"release terminal LF: {name}")
        require(sha(release_path) == release_digest, f"normalized digest: {name}")
        relative = "sources/" + name
        require(pins.FIXED_SOURCE_RUNTIME_PATHS[source_id] == relative, f"source route: {source_id}")
        require(pins.SOURCE_BUNDLE_PINS[relative]["sha256"] == release_digest, f"source pin: {name}")
        require(release_digest in contract and release_digest in repair, f"normalized ledger: {name}")
    for name, digest in PDFS.items():
        raw_path = AUGMENTATION / name
        release_path = STAGE / "runtime/sources" / name
        require(sha(raw_path) == digest and sha(release_path) == digest, f"PDF digest: {name}")
        require(raw_path.read_bytes() == release_path.read_bytes(), f"PDF bytes: {name}")

    actual_locators = {
        source_id: tuple((start, end) for start, end, _ in locators)
        for source_id, locators in pins.P142_SOURCE_LOCATORS.items()
    }
    require(actual_locators == LOCATORS, "immutable locator map")
    for (source_id, start, end), digest in LOCATOR_BLOCKS.items():
        relative = pins.FIXED_SOURCE_RUNTIME_PATHS[source_id]
        lines = lf_only_lines(STAGE / "runtime" / relative)
        block = "\n".join(lines[start - 1 : end])
        require(hashlib.sha256(block.encode("utf-8")).hexdigest() == digest,
                f"exact LF-only locator block: {source_id}:{start}-{end}")
    dxz = lf_only_lines(STAGE / "runtime/sources/dxz_2302.02541v3.txt")
    transition = "\n".join(dxz[847:880])
    imaximal_tail = "\n".join(dxz[436:458])
    require("natural transition map" in transition and "(28)" in transition,
            "DXZ formula (28) bytes")
    require("is I-maximal if" in imaximal_tail,
            "DXZ first route omits its I-maximality tail")
    for required in (
        "848--880 (formula (28)",
        "437--458",
        "Adding the locally bounded",
        "appends exactly one LF",
        "Only byte `0x0a` separates lines",
        "mesh upper-semicontinuity proof",
    ):
        require(required in contract, f"contract closure: {required}")


def check_stage() -> None:
    rows = parse_manifest(STAGE, STAGE_MANIFEST_SHA)
    require(len(rows) == 56, "stage manifest row count")
    require(not (STAGE / "STATIC_MODEL_LONG_SMOKE").exists(), "unexpected smoke")
    require(not (STAGE / "artifacts").exists(), "unexpected production artifacts")
    pins_path = STAGE / "runtime/release_pins.py"
    require(sha(pins_path) == PINS_FILE_SHA, "release pin file hash")
    pins = load_module(pins_path, "p142_source_closed_pins")
    require(pins.RELEASE_PINSET_SHA256 == PINSET_SHA, "declared pinset")
    require(pins.canonical_pinset_sha256() == PINSET_SHA, "computed pinset")
    require(len(pins.FIXED_SOURCE_RUNTIME_PATHS) == 22, "searchable route count")
    require(len(pins.SOURCE_BUNDLE_PINS) == 39, "source bundle count")
    require(len(pins.TARGET_BUNDLE_PINS) == 3, "target bundle count")
    require(len(pins.P142_SOURCE_LOCATORS) == 5, "locator route count")
    for relative, pin in pins.SOURCE_BUNDLE_PINS.items():
        path = STAGE / "runtime" / relative
        require(path.stat().st_size == pin["bytes"] and sha(path) == pin["sha256"], f"source pin: {relative}")
    for relative, pin in pins.TARGET_BUNDLE_PINS.items():
        path = STAGE / relative
        require(path.stat().st_size == pin["bytes"] and sha(path) == pin["sha256"], f"target pin: {relative}")
    check_source_closure(pins)

    service = (STAGE / "runtime/hardened_service.py").read_text(encoding="utf-8")
    mcp = (STAGE / "runtime/hardened_mcp.py").read_text(encoding="utf-8")
    contract = (STAGE / "runtime/contract.md").read_text(encoding="utf-8")
    helper = (STAGE / "runtime/lf_source_lines.py").read_text(encoding="utf-8")
    for digest in (PINSET_SHA, PINS_FILE_SHA):
        require(digest in service and digest in mcp, f"independent embedded pin: {digest}")
    require("_assert_release_target_bundle" in service and "_assert_release_target_bundle" in mcp, "target gates")
    require("_assert_exact_p142_request" in service, "host exact-target gate")
    require("not the exact pinned P14.2 statement" in mcp, "MCP exact-target gate")
    require("v3.3.3-r5-p142-source-closed-lf-v2" in service + mcp + contract,
            "release version")
    require('split(b"\\x0a")' in helper and ".splitlines(" not in helper,
            "single byte-level LF helper")
    require(service.count("read_lf_only_source_lines(") == 3,
            "host LF helper call count")
    require(mcp.count("read_lf_only_source_lines(") == 3,
            "MCP LF helper call count")
    require(".splitlines(" not in service + mcp,
            "generic line split remains in host/MCP")
    stage_report = (STAGE / "STAGING_REPORT.md").read_text(encoding="utf-8")
    for stale in (
        "REBUILD_IN_PROGRESS_NOT_READY",
        "e45c86b46d533a7c32019c203e770818c265f4fe4fe073502937137e54b8afc3",
        "e2e633806d62d39d70b0722128a638389dd79cb7d393a6c099bf77b2e52e28c5",
        "abda9eee4ce96519951a85736824c7e1a0c0a186a1625f0e5ae2563c78f321fe",
    ):
        require(stale not in stage_report, f"stale stage marker: {stale}")
    require("848--880" in stage_report and "437--458" in stage_report
            and "appends exactly one LF" in stage_report,
            "stage repair report")

    release_check = load_module(STAGE / "check_release.py", "p142_source_closed_release_check")
    release_check.check_manifest()
    release_check.check_catalog()
    release_check.check_release_pins()
    release_check.check_code_contract()


def run_all_tests() -> None:
    require(TEST_PYTHON.exists(), "fixed test Python missing")
    for run_index in (1, 2):
        completed = subprocess.run(
            [str(TEST_PYTHON), "-B", "-m", "unittest", "discover", "-s", "tests"],
            cwd=STAGE,
            capture_output=True,
            text=True,
            timeout=240,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        output = completed.stdout + "\n" + completed.stderr
        require(completed.returncode == 0,
                f"frozen runtime test run {run_index} failed:\n{output}")
        match = re.search(rf"Ran {TEST_COUNT} tests in ([0-9.]+)s", output)
        require(match is not None,
                f"frozen runtime test run {run_index} count:\n{output}")
        require(re.search(r"\nOK\s*$", output) is not None,
                f"frozen runtime test run {run_index} verdict:\n{output}")
        print(
            f"FROZEN_RUNTIME_TEST_RUN_{run_index}: "
            f"{TEST_COUNT} tests in {match.group(1)}s: PASS"
        )


def check_result() -> None:
    result = strict_json(ROOT / "RESULT.json")
    require(
        result["status"]
        == "AUTHORED_REPAIRED_SOURCE_STAGE_READY_FOR_INDEPENDENT_HOSTILE_AUDIT",
        "authored status",
    )
    require(
        result["target"]["prior_independent_audit_verdict"]
        == "PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET",
        "prior audit binding",
    )
    require(
        result["failed_audits"]
        == {
            "p142_v1": "FAIL_SOURCE_CLOSURE_LINE_NUMBERING",
            "p148_smoke_repair": "FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE",
        },
        "failed-audit result binding",
    )
    repair = result["repairs"]
    require(repair["line_separator"] == "LF_BYTE_0X0A_ONLY", "LF repair result")
    require(repair["shared_source_line_helper"] is True, "shared-helper result")
    require(repair["host_source_addressing_call_sites"] == 3, "host helper result")
    require(repair["mcp_source_addressing_call_sites"] == 3, "MCP helper result")
    require(repair["generic_splitlines_in_host_or_mcp"] == 0, "generic split result")
    require(repair["dxz_first_locator"] == [437, 458], "DXZ first-locator result")
    require(repair["dxz_formula_28_locator"] == [848, 880], "DXZ formula result")
    require(repair["smoke_streams"] == "SEPARATE_STDOUT_STDERR", "smoke streams result")
    require(repair["smoke_stdin"] == "DEDICATED_NO_INPUT_PTY", "smoke PTY result")
    require(
        repair["process_sampler"]
        == "POLL_BEFORE_AND_AFTER_WITH_TERMINAL_OBSERVATION",
        "smoke sampler result",
    )
    require(repair["throwaway_mutation_copies_only_are_writable"] is True,
            "mutation fixture result")
    require(
        result["source_augmentation"]["text_normalization"]
        == "raw_bytes_plus_exactly_one_terminal_lf",
        "normalization result",
    )
    release = result["release_stage"]
    require(
        release["manifest_sha256"] == STAGE_MANIFEST_SHA
        and release["manifest_rows"] == 56,
        "result stage manifest",
    )
    require(release["version"] == "v3.3.3-r5-p142-source-closed-lf-v2",
            "result release version")
    require(release["canonical_pinset_sha256"] == PINSET_SHA, "result pinset")
    require(release["release_pins_sha256"] == PINS_FILE_SHA, "result pin module")
    require(
        release["runtime_tests"]
        == {
            "count": TEST_COUNT,
            "frozen_source_runs_per_checker_invocation": 2,
            "status": "PASS_PREFREEZE_AND_REQUIRED_AT_CHECK_TIME",
            "bytecode_disabled": True,
        },
        "result tests",
    )
    require(release["static_model_long_smoke"] == "NOT_RUN_AUTHORED_STAGE",
            "smoke overclaim")
    preservation = result["byte_preservation"]
    require(
        preservation
        == {
            "unchanged_old_rows": 47,
            "changed_old_rows": 8,
            "added_rows": 1,
            "all_39_fixed_source_files": True,
            "all_3_target_files": True,
            "all_prior_mathematical_audit_files": True,
        },
        "result byte-preservation ledger",
    )
    require(result["independent_hostile_audit_of_this_release"] == "NOT_YET_PERFORMED", "audit overclaim")
    require(
        result["authored_static_checker"]
        == {
            "output": "PASS_FROZEN_P142_SOURCE_CLOSED_LF_V2_AUTHORED_STAGE",
            "directories_mode": "0555",
            "regular_files_mode": "0444",
            "runs_full_suite_twice_from_exact_frozen_stage": True,
        },
        "checker result binding",
    )
    for key in ("production_submission", "final_path_smoke", "service_launch", "live_integration", "inventory_mutation", "git_activity"):
        require(result[key] == "NOT_PERFORMED", f"boundary overclaim: {key}")
    require(result["open_problem_retirement_authorized"] is False, "retirement overclaim")


def main() -> None:
    expected_top = {
        "AUTHOR_REPORT.md",
        "BYTE_PRESERVATION.json",
        "CHANGE_LEDGER.md",
        "RESULT.json",
        "SHA256SUMS",
        "SOURCE_CLOSURE_REPAIR.md",
        "TEST_RUNS.json",
        "check_dossier.py",
        "input_bindings",
        "release_stage",
        "source_augmentation",
        "target",
    }
    require({path.name for path in ROOT.iterdir()} == expected_top, "top-level inventory")
    check_frozen_modes()
    before = regular_tree_fingerprint(ROOT)
    parse_manifest(ROOT)
    check_result()
    check_input_bindings()
    check_targets()
    check_stage()
    check_preservation_ledgers()
    run_all_tests()
    require(regular_tree_fingerprint(ROOT) == before, "dossier mutated during checker")
    check_frozen_modes()
    print("PASS_FROZEN_P142_SOURCE_CLOSED_LF_V2_AUTHORED_STAGE")


if __name__ == "__main__":
    main()
