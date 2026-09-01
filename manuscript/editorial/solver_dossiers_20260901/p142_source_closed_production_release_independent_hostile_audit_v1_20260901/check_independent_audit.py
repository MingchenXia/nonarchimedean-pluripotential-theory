from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import stat


ROOT = Path(__file__).resolve().parent
AUTHOR = Path(
    "/private/tmp/"
    "p142_source_closed_production_release_authored_stage_dossier_v1_20260901"
)
AUTHOR_MANIFEST_SHA = (
    "4007c71e7ac04f02ac92ac90cda83c7142389a29835ac428f612d183271720a0"
)
CANDIDATE = Path(
    "/private/tmp/p142_live_adapted_candidate_v1_frozen_20260901"
)
PRIOR_AUDIT = Path(
    "/private/tmp/p142_live_adapted_candidate_v1_independent_hostile_audit_20260901"
)
P148_FAILED_SMOKE_DOSSIER = Path(
    "/private/tmp/p148_retry1_final_path_smoke_authored_fail_dossier_v1_20260901"
)
P148_FAILED_FINAL = Path(
    "/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/"
    "rethlas_hardened_v3_3_3_r5_p148_retry1_final_20260901"
)


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
            RuntimeError(f"nonfinite JSON: {item}")
        ),
    )


def parse_manifest(root: Path) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    text = manifest.read_text(encoding="utf-8")
    require(text.endswith("\n"), f"manifest LF: {root}")
    rows: dict[str, str] = {}
    for line in text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"manifest row: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate path: {relative}")
        require(not relative.startswith(("/", "../")), f"unsafe path: {relative}")
        rows[relative] = digest
    actual = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path != manifest
    )
    require(sorted(rows) == actual, f"manifest inventory: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest mismatch: {relative}")
    return rows


def check_author_tree() -> None:
    require(sha(AUTHOR / "SHA256SUMS") == AUTHOR_MANIFEST_SHA, "author manifest")
    parse_manifest(AUTHOR)
    for path in [AUTHOR, *AUTHOR.rglob("*")]:
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"author symlink: {path}")
        require("__pycache__" not in path.parts and path.suffix != ".pyc", f"cache: {path}")
    require(not (AUTHOR / "release_stage/artifacts").exists(), "authored artifacts")
    require(not (AUTHOR / "release_stage/STATIC_MODEL_LONG_SMOKE").exists(), "authored smoke")


def check_targets_and_bindings() -> None:
    targets = {
        "STATEMENT.tex": ("ADAPTED_STATEMENT.tex", "cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2"),
        "PROOF.tex": ("ADAPTED_PROOF.tex", "7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac"),
        "EXAMPLE.tex": ("ADAPTED_EXAMPLE.tex", "7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f"),
    }
    for release_name, (candidate_name, digest) in targets.items():
        outer = AUTHOR / "target" / release_name
        staged = AUTHOR / "release_stage/target" / release_name
        candidate = CANDIDATE / candidate_name
        require(sha(outer) == sha(staged) == sha(candidate) == digest, f"target: {release_name}")
        require(outer.read_bytes() == staged.read_bytes() == candidate.read_bytes(), f"target bytes: {release_name}")
    require(
        (AUTHOR / "input_bindings/P142_CANDIDATE_SHA256SUMS").read_bytes()
        == (CANDIDATE / "SHA256SUMS").read_bytes(),
        "candidate manifest binding",
    )
    require(
        (AUTHOR / "input_bindings/P142_PRIOR_AUDIT_SHA256SUMS").read_bytes()
        == (PRIOR_AUDIT / "SHA256SUMS").read_bytes(),
        "prior audit manifest binding",
    )


def check_source_bytes() -> None:
    names = [
        ("mp_2409.06221v2", "724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d", "9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23"),
        ("dxz_2302.02541v3", "3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9", "7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c"),
        ("darvas_xia_2003.04818", "794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed", "a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61"),
        ("demailly_ein_lazarsfeld_math0002035", "0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3", "59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2"),
        ("xia_2312.17150v3", "a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d", "773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9"),
    ]
    for stem, text_digest, pdf_digest in names:
        raw_text = (AUTHOR / "source_augmentation" / f"{stem}.txt").read_bytes()
        release_text_path = AUTHOR / "release_stage/runtime/sources" / f"{stem}.txt"
        release_text = release_text_path.read_bytes()
        require(raw_text.endswith(b"\n\f") and not raw_text.endswith(b"\n"), f"raw ending: {stem}")
        require(release_text == raw_text + b"\n", f"exact +LF: {stem}")
        require(sha(release_text_path) == text_digest, f"text digest: {stem}")
        raw_pdf = AUTHOR / "source_augmentation" / f"{stem}.pdf"
        release_pdf = AUTHOR / "release_stage/runtime/sources" / f"{stem}.pdf"
        require(sha(raw_pdf) == sha(release_pdf) == pdf_digest, f"PDF digest: {stem}")
        require(raw_pdf.read_bytes() == release_pdf.read_bytes(), f"PDF bytes: {stem}")


def runtime_lines(stem: str) -> list[str]:
    return (
        AUTHOR / "release_stage/runtime/sources" / f"{stem}.txt"
    ).read_text(encoding="utf-8").splitlines()


def excerpt(lines: list[str], start: int, end: int) -> str:
    return "\n".join(lines[start - 1 : end])


def check_locator_failure_is_real() -> None:
    mp = runtime_lines("mp_2409.06221v2")
    require("Definition 1.3.1" in excerpt(mp, 413, 423), "MP locator changed")
    require("pointwise convergence topology" not in excerpt(mp, 413, 423), "MP defect disappeared")
    require("pointwise convergence topology" in excerpt(mp, 424, 431), "MP missing repair bytes")

    dxz = runtime_lines("dxz_2302.02541v3")
    first = excerpt(dxz, 437, 448)
    require("I-maximal" not in first and "τψ+ := inf" not in first, "DXZ first defect disappeared")
    require("τψ+ := inf" in dxz[451] and "I-maximal" in dxz[464], "DXZ repair anchors")
    formula = excerpt(dxz, 848, 880)
    require("(28)" in formula and "natural transition map" in formula, "DXZ formula prefix")
    require("−∞, if τ > τψ+" not in formula and "−∞, if τ > τψ+" in dxz[880], "DXZ formula tail defect")

    darvas = runtime_lines("darvas_xia_2003.04818")
    require("Proposition 2.18" in excerpt(darvas, 1055, 1185), "Darvas proposition start")
    require("(ii) ϕ ≃I P [ϕ]I" not in excerpt(darvas, 1055, 1185), "Darvas defect disappeared")
    require("(ii) ϕ ≃I P [ϕ]I" in darvas[1191], "Darvas repair anchor")

    dele = runtime_lines("demailly_ein_lazarsfeld_math0002035")
    require("Theorem 2.6" in excerpt(dele, 596, 613), "DEL heading")
    require("(ii) Let X be a complex manifold" not in excerpt(dele, 596, 613), "DEL defect disappeared")
    require("(ii) Let X be a complex manifold" in dele[615], "DEL repair anchor")

    xia = runtime_lines("xia_2312.17150v3")
    require("(3.8)" in excerpt(xia, 628, 647), "Xia formula label")
    require("v 7→ sup" not in excerpt(xia, 628, 647), "Xia defect disappeared")
    require("v 7→ sup" in xia[650] and "a bijection" in xia[656], "Xia repair anchors")


def check_inherited_smoke_failure() -> None:
    runner = AUTHOR / "release_stage/run_static_model_long_smoke.py"
    failed_runner = P148_FAILED_FINAL / "run_static_model_long_smoke.py"
    runner_sha = "5a8f25b6851667d284d84bd8874fdfcdeb640f51380727a95a72eb9991b10c78"
    require(sha(runner) == sha(failed_runner) == runner_sha, "known-failed runner digest")
    require(runner.read_bytes() == failed_runner.read_bytes(), "known-failed runner bytes")
    require(
        sha(P148_FAILED_SMOKE_DOSSIER / "SHA256SUMS")
        == "e7b69860f7327da9e6a375720c2f447d81eb8a7880d1bf5c415848bcbbfc708e",
        "failed smoke dossier manifest",
    )
    failed = strict_json(P148_FAILED_SMOKE_DOSSIER / "RESULT.json")
    require(failed["verdict"] == "FAIL", "failed smoke verdict")
    require(
        {item["id"] for item in failed["blockers"]}
        == {"RAW_LIFECYCLE_NON_JSON_INTERLEAVING", "TERMINAL_PROCESS_SAMPLE_EXIT_RACE"},
        "failed smoke blocker identities",
    )
    source = runner.read_text(encoding="utf-8")
    checker = (AUTHOR / "release_stage/check_release.py").read_text(encoding="utf-8")
    require("stderr=subprocess.STDOUT" in source, "stderr merge defect disappeared")
    require("while process.poll() is None" in source, "sampling exit-race structure disappeared")
    require("non-JSON smoke output after JSON lifecycle" in checker, "raw checker gate changed")
    require("post-horizon process sample lacks the bound Codex/host roles" in checker, "horizon checker gate changed")


def check_result() -> None:
    result = strict_json(ROOT / "RESULT.json")
    require(result["verdict"] == "FAIL_SOURCE_CLOSURE_LINE_NUMBERING", "verdict")
    require(result["exact_locator_semantics"] == "FAIL", "locator status")
    require(len(result["blocking_findings"]) == 6, "finding count")
    require(result["smoke_infrastructure_readiness"] == "FAIL_KNOWN_INHERITED_RUNNER", "smoke status")
    require(len(result["infrastructure_blockers"]) == 2, "smoke blocker count")
    require(result["mathematical_target_audit"] == "PASS_NO_NEW_BLOCKER", "scope firewall")
    for field in (
        "production_submitted",
        "final_path_smoke_run",
        "service_launched",
        "live_source_modified",
        "inventory_modified",
        "git_used",
        "retirement_authorized",
    ):
        require(result[field] is False, f"boundary: {field}")


def main() -> None:
    require(
        {path.name for path in ROOT.iterdir()}
        == {"INDEPENDENT_AUDIT_REPORT.md", "RESULT.json", "SHA256SUMS", "check_independent_audit.py"},
        "audit inventory",
    )
    parse_manifest(ROOT)
    check_author_tree()
    check_targets_and_bindings()
    check_source_bytes()
    check_locator_failure_is_real()
    check_inherited_smoke_failure()
    check_result()
    print("PASS_INDEPENDENT_P142_AUDIT_DOSSIER_WITH_BINARY_FAIL")


if __name__ == "__main__":
    main()
