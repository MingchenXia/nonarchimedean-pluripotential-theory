from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import stat
import sys
from typing import Any


HERE = Path(__file__).resolve().parent
FINAL = Path(
    "/Users/mingchen/Documents/ChatGPT/Yethlas/runtime/"
    "rethlas_hardened_v3_3_3_r5_p148_retry2_final_20260901"
)
AUTHORED = Path(
    "/private/tmp/"
    "p148_smoke_infrastructure_repaired_readonly_authored_stage_dossier_v2_20260901"
)
STAGE = AUTHORED / "release_stage"
AUDIT = Path(
    "/private/tmp/"
    "p148_smoke_infrastructure_repaired_readonly_independent_hostile_audit_v2_20260901"
)

AUTHORED_SHA = "0645efed9d2ba12a99501fe07a1988e4e7a09a20e496d21c38937774d1d29d46"
STAGE_SHA = "837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912"
AUDIT_SHA = "21462160629d17c30157a1f75d8904c87a94d5b96c38c0884318b43ef26af878"
FINAL_SHA = "d2ee26df03554aa133fbf9dfd9f28166a2b6a328eb690565925dfd5dac42aab7"

SMOKE_HASHES = {
    "receipt.json": "68fc549b39912141e8418385d414616a1e3319bfdc62c54a4ece4100b03aa3b4",
    "codex.stdout.jsonl": "9859b7ca52f85b8c7c09b7e1f67eab26fa7671eeea2895a5335c096279482c4b",
    "codex.stderr.log": "8430b6c103a639a3bc6f8e732504111ea5365235a37bf32b091698bc35385b76",
    "process_samples.json": "218e77793b544ea69036159b3a67fea341785ba1c66bacec91ef81275f21af1d",
}


def require(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=lambda value: (_ for _ in ()).throw(
            ValueError(f"nonfinite JSON value: {value}")
        ),
    )


def manifest_rows(path: Path) -> dict[str, str]:
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), f"manifest lacks terminal LF: {path}")
    rows: dict[str, str] = {}
    order: list[str] = []
    for line in raw.decode("utf-8").split("\n")[:-1]:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        require(match is not None, f"malformed manifest row: {path}: {line!r}")
        digest, relative = match.groups()
        require(relative not in rows, f"duplicate manifest row: {relative}")
        require(not relative.startswith(("/", "../")), f"unsafe path: {relative}")
        rows[relative] = digest
        order.append(relative)
    require(order == sorted(order), f"unsorted manifest: {path}")
    return rows


def actual_files(root: Path) -> list[str]:
    result: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        info = path.lstat()
        require(not stat.S_ISLNK(info.st_mode), f"symlink: {root}: {relative}")
        require("__pycache__" not in path.parts, f"cache: {root}: {relative}")
        if stat.S_ISDIR(info.st_mode):
            continue
        require(stat.S_ISREG(info.st_mode), f"special file: {root}: {relative}")
        require(path.suffix != ".pyc", f"bytecode: {root}: {relative}")
        if relative != "SHA256SUMS" and not relative.startswith(
            "STATIC_MODEL_LONG_SMOKE/workspace/"
        ):
            result.append(relative)
    return sorted(result)


def validate_manifest(root: Path, expected_sha: str) -> dict[str, str]:
    manifest = root / "SHA256SUMS"
    require(sha(manifest) == expected_sha, f"manifest digest: {root}")
    rows = manifest_rows(manifest)
    require(sorted(rows) == actual_files(root), f"manifest inventory: {root}")
    for relative, digest in rows.items():
        require(sha(root / relative) == digest, f"manifest row: {root}: {relative}")
    return rows


def validate_self_manifest() -> None:
    rows = manifest_rows(HERE / "SHA256SUMS")
    require(sorted(rows) == actual_files(HERE), "dossier manifest inventory")
    for relative, digest in rows.items():
        require(sha(HERE / relative) == digest, f"dossier manifest row: {relative}")


def import_checker():
    sys.dont_write_bytecode = True
    path = FINAL / "check_release.py"
    spec = importlib.util.spec_from_file_location("p148_retry2_checker", path)
    require(spec is not None and spec.loader is not None, "checker import")
    module = importlib.util.module_from_spec(spec)
    sys.modules["p148_retry2_checker"] = module
    spec.loader.exec_module(module)
    return module


def check_inputs_and_final() -> None:
    validate_manifest(AUTHORED, AUTHORED_SHA)
    validate_manifest(AUDIT, AUDIT_SHA)
    require(sha(STAGE / "SHA256SUMS") == STAGE_SHA, "stage manifest digest")
    stage_rows = manifest_rows(STAGE / "SHA256SUMS")
    require(len(stage_rows) == 44, "stage row count")
    for relative, digest in stage_rows.items():
        require(sha(STAGE / relative) == digest, f"stage row: {relative}")

    final_rows = validate_manifest(FINAL, FINAL_SHA)
    require(len(final_rows) == 48, "final row count")
    smoke_rows = {f"STATIC_MODEL_LONG_SMOKE/{name}" for name in SMOKE_HASHES}
    require(set(final_rows) - set(stage_rows) == smoke_rows, "final-only rows")
    require(not (set(stage_rows) - set(final_rows)), "missing inherited rows")
    for relative, digest in stage_rows.items():
        require(final_rows[relative] == digest, f"inherited digest drift: {relative}")
        require((FINAL / relative).read_bytes() == (STAGE / relative).read_bytes(),
                f"inherited byte drift: {relative}")
    for name, digest in SMOKE_HASHES.items():
        require(sha(FINAL / "STATIC_MODEL_LONG_SMOKE" / name) == digest,
                f"smoke hash: {name}")
    workspace = FINAL / "STATIC_MODEL_LONG_SMOKE/workspace"
    require(workspace.is_dir() and not list(workspace.iterdir()), "workspace not empty")
    require(not (FINAL / "artifacts").exists(), "production artifacts present")

    snapshots = HERE / "snapshots"
    require((snapshots / "authored_source_SHA256SUMS").read_bytes()
            == (AUTHORED / "SHA256SUMS").read_bytes(), "authored snapshot")
    require((snapshots / "release_stage_SHA256SUMS").read_bytes()
            == (STAGE / "SHA256SUMS").read_bytes(), "stage snapshot")
    require((snapshots / "independent_audit_SHA256SUMS").read_bytes()
            == (AUDIT / "SHA256SUMS").read_bytes(), "audit snapshot")
    require((snapshots / "final_release_SHA256SUMS").read_bytes()
            == (FINAL / "SHA256SUMS").read_bytes(), "final snapshot")


def check_exact_blocker() -> None:
    smoke = FINAL / "STATIC_MODEL_LONG_SMOKE"
    receipt = strict_json(smoke / "receipt.json")
    require(receipt["status"] == "passed" and receipt["errors"] == [], "runner receipt")
    require(receipt["completed_wait_calls"] == 1, "wait-call count")
    require(receipt["wait_seconds"] == 310, "wait duration")
    require(receipt["model_manager_strategy"] == "StaticModelsManager", "model manager")
    require(receipt["catalog"]["model"] == "gpt-5.6-sol", "model")
    require(receipt["catalog"]["selected_reasoning_effort"] == "xhigh", "effort")
    require(receipt["runtime_before"] == receipt["runtime_after"], "runtime drift")
    require(receipt["workspace_before"] == receipt["workspace_after"] == {}, "workspace drift")

    records = [json.loads(line, object_pairs_hook=reject_duplicates)
               for line in (smoke / "codex.stdout.jsonl").read_text(encoding="utf-8").splitlines()]
    require(len(records) == 8, "stdout record count")
    require(records[0]["type"] == "thread.started", "thread start")
    require(records[1] == {"type": "turn.started"}, "turn start")
    require(records[2]["type"] == "item.completed"
            and records[2]["item"]["type"] == "error"
            and re.fullmatch(
                r"Exceeded skills context budget\. All skill descriptions were removed and "
                r"[1-9]\d{0,3} additional skills were not included in the model-visible skills list\.",
                records[2]["item"]["message"],
            ) is not None,
            "skills-budget error")
    require(records[3]["type"] == "item.completed"
            and records[3]["item"]["type"] == "agent_message"
            and records[3]["item"]["text"] == "", "empty pre-tool message")
    require(records[4]["type"] == "item.started"
            and records[4]["item"]["type"] == "mcp_tool_call", "tool start")
    require(records[5]["type"] == "item.completed"
            and records[5]["item"]["type"] == "mcp_tool_call"
            and records[5]["item"]["status"] == "completed", "tool completion")
    require(records[6]["type"] == "item.completed"
            and records[6]["item"] == {
                "id": records[6]["item"]["id"],
                "type": "agent_message",
                "text": "STATIC_MODEL_SMOKE_OK",
            }, "terminal marker")
    require(records[7]["type"] == "turn.completed", "turn completion")

    checker = import_checker()
    try:
        checker.check_long_smoke()
    except RuntimeError as error:
        require(str(error) == "raw smoke terminal marker mismatch",
                f"unexpected final checker error: {error}")
    else:
        raise RuntimeError("strict final checker unexpectedly passed")

    filtered = "\n".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":"))
        for index, record in enumerate(records)
        if index != 3
    ) + "\n"
    checker.validate_stdout_smoke(filtered, receipt)


def check_snapshots() -> None:
    pairs = {
        "smoke_receipt.json": "receipt.json",
        "smoke_codex_stdout.jsonl": "codex.stdout.jsonl",
        "smoke_codex_stderr.log": "codex.stderr.log",
        "smoke_process_samples.json": "process_samples.json",
    }
    for snapshot, live in pairs.items():
        require((HERE / "snapshots" / snapshot).read_bytes()
                == (FINAL / "STATIC_MODEL_LONG_SMOKE" / live).read_bytes(),
                f"snapshot drift: {snapshot}")


def main() -> None:
    validate_self_manifest()
    result = strict_json(HERE / "RESULT.json")
    require(result["verdict"] == "FAIL", "result verdict")
    require(result["smoke_run_count"] == 1, "smoke count")
    check_inputs_and_final()
    check_snapshots()
    check_exact_blocker()
    print("PASS_P148_RETRY2_FINAL_PATH_SMOKE_FAIL_DOSSIER_V2")


if __name__ == "__main__":
    main()
