from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
import re
import stat
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import requests
from fastmcp import FastMCP
from jsonschema import Draft202012Validator

try:
    import canonical_reference as _canonical_reference
except ModuleNotFoundError:  # package-style launch from the parent directory
    from . import canonical_reference as _canonical_reference

try:
    import release_pins as _release_pins
except ModuleNotFoundError:  # package-style launch from the parent directory
    from . import release_pins as _release_pins

try:
    import lf_source_lines as _lf_source_lines
except ModuleNotFoundError:  # package-style launch from the parent directory
    from . import lf_source_lines as _lf_source_lines

if Path(_canonical_reference.__file__).resolve() != Path(__file__).resolve().with_name(
    "canonical_reference.py"
):
    raise RuntimeError("canonical-reference helper was not loaded from the runtime bundle")
canonicalize_external_reference_record = (
    _canonical_reference.canonicalize_external_reference_record
)

LF_SOURCE_LINES_PATH = Path(__file__).resolve().with_name("lf_source_lines.py")
if Path(_lf_source_lines.__file__).resolve() != LF_SOURCE_LINES_PATH:
    raise RuntimeError("LF-only source helper was not loaded from the runtime bundle")
read_lf_only_source_lines = _lf_source_lines.read_lf_only_source_lines

RELEASE_PINS_PATH = Path(__file__).resolve().with_name("release_pins.py")
if Path(_release_pins.__file__).resolve() != RELEASE_PINS_PATH:
    raise RuntimeError("release pins were not loaded from the runtime bundle")
EXPECTED_RELEASE_PINSET_SHA256 = (
    "0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf"
)
EXPECTED_RELEASE_PINS_FILE_SHA256 = (
    "5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6"
)
if _release_pins.canonical_pinset_sha256() != EXPECTED_RELEASE_PINSET_SHA256:
    raise RuntimeError("release pinset differs from the MCP's immutable pin")
if _release_pins.RELEASE_PINSET_SHA256 != EXPECTED_RELEASE_PINSET_SHA256:
    raise RuntimeError("release pinset declared digest differs from the MCP pin")
if hashlib.sha256(RELEASE_PINS_PATH.read_bytes()).hexdigest() != EXPECTED_RELEASE_PINS_FILE_SHA256:
    raise RuntimeError("release_pins.py differs from the MCP's immutable file pin")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--statement-sha256", required=True)
    parser.add_argument("--proof-sha256", required=True)
    parser.add_argument("--nonce", required=True)
    return parser.parse_args()


ARGS = _parse_args()
RUNTIME_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = RUNTIME_ROOT.parent
ARTIFACT_ROOT = PROJECT_ROOT / "artifacts"
RESULTS_ROOT = ARTIFACT_ROOT / "results"
MEMORY_ROOT = ARTIFACT_ROOT / "memory"
RECEIPTS_ROOT = ARTIFACT_ROOT / "receipts"
SCHEMA_PATH = RUNTIME_ROOT / "verification_output.schema.json"
MEMORY_RECORD_SCHEMA_PATH = RUNTIME_ROOT / "memory_record.schema.json"
CANONICAL_REFERENCE_PATH = RUNTIME_ROOT / "canonical_reference.py"
MODEL_CATALOG_RELATIVE_PATH = "model_catalog.gpt-5.6-sol.json"
MODEL_CATALOG_PATH = RUNTIME_ROOT / MODEL_CATALOG_RELATIVE_PATH
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "xhigh"
EXPECTED_MODEL_CATALOG_BYTES = 41355
EXPECTED_MODEL_CATALOG_SHA256 = (
    "75ecc0f5301dcc5474598335a12e82e9195eeb04f55197f2589109b34f3988fa"
)
MODEL_MANAGER_STRATEGY = "StaticModelsManager"

RUN_ID = ARGS.run_id
STATEMENT_SHA256 = ARGS.statement_sha256
PROOF_SHA256 = ARGS.proof_sha256
NONCE = ARGS.nonce

SAFE_RUN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,159}$")
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
if not SAFE_RUN_RE.fullmatch(RUN_ID):
    raise SystemExit("unsafe run id")
if not HEX64_RE.fullmatch(STATEMENT_SHA256):
    raise SystemExit("invalid statement digest")
if not HEX64_RE.fullmatch(PROOF_SHA256):
    raise SystemExit("invalid proof digest")
if not HEX64_RE.fullmatch(NONCE):
    raise SystemExit("invalid nonce")

RUN_MEMORY_DIR = MEMORY_ROOT / RUN_ID
RUN_RESULTS_DIR = RESULTS_ROOT / RUN_ID
REQUEST_PATH = RUN_RESULTS_DIR / "request.json"
OUTPUT_PATH = RUN_RESULTS_DIR / "verification.json"
RECEIPT_PATH = RECEIPTS_ROOT / f"{RUN_ID}.json"
STATE_PATH = RUN_MEMORY_DIR / "state.json"

CHANNEL_FILES: Dict[str, str] = {
    "statement_checks": "statement_checks.jsonl",
    "reference_checks": "reference_checks.jsonl",
    "verification_reports": "verification_reports.jsonl",
    "failed_checks": "failed_checks.jsonl",
    "events": "events.jsonl",
}

SOURCE_MAP: Dict[str, Path] = {
    source_id: RUNTIME_ROOT / relative
    for source_id, relative in _release_pins.FIXED_SOURCE_RUNTIME_PATHS.items()
}
SOURCE_BUNDLE_PINS = {
    relative: dict(pin)
    for relative, pin in _release_pins.SOURCE_BUNDLE_PINS.items()
}
TARGET_BUNDLE_PINS = {
    relative: dict(pin)
    for relative, pin in _release_pins.TARGET_BUNDLE_PINS.items()
}
P142_SOURCE_LOCATORS = {
    source_id: tuple(locators)
    for source_id, locators in _release_pins.P142_SOURCE_LOCATORS.items()
}

THEOREM_SEARCH_URL = "https://leansearch.net/thm/search"
THEOREM_SEARCH_TASK = (
    "Given a math statement, retrieve useful references, such as theorems, "
    "lemmas, and definitions, that are useful for solving the given problem."
)

LOCK = threading.RLock()
PHASE = "new"
EVENTS: List[Dict[str, Any]] = []
COUNTS: Dict[str, int] = {name: 0 for name in CHANNEL_FILES}
TOOL_COUNTS: Dict[str, int] = {}
QUERIED_CHANNELS: set[str] = set()
FULLY_QUERIED_CHANNELS: set[str] = set()
VALIDATED_PAYLOAD_SHA256: Optional[str] = None
META_STATEMENT_SHA256: Optional[str] = None
META_STATEMENT_NORMALIZED_SHA256: Optional[str] = None
RUNTIME_CONTRACT_VERSION = "rethlas-hardened-runtime-contract-v3.3.3-r5-p142-source-closed-lf-v2"

try:
    request_info = REQUEST_PATH.lstat()
except OSError:
    request_info = None
if request_info is None or not stat.S_ISREG(request_info.st_mode):
    raise SystemExit("host-authored request.json is missing")


def _reject_duplicate_object_pairs(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def _reject_nonfinite_json_constant(value: str) -> Any:
    raise ValueError(f"non-finite JSON constant is forbidden: {value}")


def _strict_json_loads(text: str) -> Any:
    return json.loads(
        text,
        object_pairs_hook=_reject_duplicate_object_pairs,
        parse_constant=_reject_nonfinite_json_constant,
    )


HOST_REQUEST = _strict_json_loads(REQUEST_PATH.read_text(encoding="utf-8"))
if not isinstance(HOST_REQUEST, dict):
    raise SystemExit("host-authored request.json is not an object")
if set(HOST_REQUEST) != {
    "statement",
    "proof",
    "statement_sha256",
    "proof_sha256",
}:
    raise SystemExit("host-authored request.json keys differ from the exact schema")
HOST_STATEMENT = HOST_REQUEST.get("statement")
HOST_PROOF = HOST_REQUEST.get("proof")
if not isinstance(HOST_STATEMENT, str) or not isinstance(HOST_PROOF, str):
    raise SystemExit("host-authored request strings are missing")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_text(text: str) -> str:
    return _sha256_bytes(text.encode("utf-8"))


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _assert_static_model_catalog() -> Dict[str, Any]:
    """Independently bind the MCP receipt to the host-selected static catalog."""

    try:
        info = MODEL_CATALOG_PATH.lstat()
    except OSError as error:
        raise RuntimeError("static model catalog is missing") from error
    if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
        raise RuntimeError("static model catalog must be a regular non-symlink file")
    if info.st_size != EXPECTED_MODEL_CATALOG_BYTES:
        raise RuntimeError("static model catalog byte length differs from immutable pin")
    digest = _sha256_file(MODEL_CATALOG_PATH)
    if digest != EXPECTED_MODEL_CATALOG_SHA256:
        raise RuntimeError("static model catalog bytes differ from immutable pin")
    try:
        catalog = _strict_json_loads(MODEL_CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        raise RuntimeError("static model catalog is not strict UTF-8 JSON") from error
    if not isinstance(catalog, dict) or set(catalog) != {"models"}:
        raise RuntimeError("static model catalog top-level keyset is not exact")
    models = catalog.get("models")
    if not isinstance(models, list) or len(models) != 1 or not isinstance(models[0], dict):
        raise RuntimeError("static model catalog must contain exactly one model")
    selected = models[0]
    if selected.get("slug") != MODEL:
        raise RuntimeError("static model catalog selected-model mismatch")
    levels = selected.get("supported_reasoning_levels")
    if not isinstance(levels, list) or not levels:
        raise RuntimeError("static model catalog reasoning-level list is missing")
    efforts: List[str] = []
    for level in levels:
        if not isinstance(level, dict) or not isinstance(level.get("effort"), str):
            raise RuntimeError("static model catalog has an invalid reasoning-level entry")
        efforts.append(level["effort"])
    if len(set(efforts)) != len(efforts):
        raise RuntimeError("static model catalog has duplicate reasoning levels")
    if REASONING_EFFORT not in efforts:
        raise RuntimeError("static model catalog does not support the selected reasoning effort")
    return {
        "runtime_path": MODEL_CATALOG_RELATIVE_PATH,
        "bytes": info.st_size,
        "sha256": digest,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "supported_reasoning_efforts": efforts,
        "manager": MODEL_MANAGER_STRATEGY,
    }


def _assert_release_source_bundle() -> Dict[str, Dict[str, Any]]:
    sources_root = RUNTIME_ROOT / "sources"
    try:
        root_info = sources_root.lstat()
    except OSError as error:
        raise RuntimeError("fixed-source directory is missing") from error
    if not stat.S_ISDIR(root_info.st_mode) or stat.S_ISLNK(root_info.st_mode):
        raise RuntimeError("fixed-source directory must be a non-symlink directory")

    actual_paths: Dict[str, Path] = {}
    for path in sorted(sources_root.rglob("*")):
        relative = path.relative_to(RUNTIME_ROOT).as_posix()
        info = path.lstat()
        if stat.S_ISLNK(info.st_mode):
            raise RuntimeError(f"fixed-source symlink forbidden: {relative}")
        if not stat.S_ISREG(info.st_mode):
            raise RuntimeError(f"fixed-source non-file forbidden: {relative}")
        actual_paths[relative] = path

    expected_paths = set(SOURCE_BUNDLE_PINS)
    if set(actual_paths) != expected_paths:
        missing = sorted(expected_paths - set(actual_paths))
        extra = sorted(set(actual_paths) - expected_paths)
        raise RuntimeError(
            f"fixed-source inventory mismatch; missing={missing}; extra={extra}"
        )

    actual: Dict[str, Dict[str, Any]] = {}
    for relative, path in actual_paths.items():
        info = path.lstat()
        actual[relative] = {
            "bytes": info.st_size,
            "sha256": _sha256_file(path),
        }
    if actual != SOURCE_BUNDLE_PINS:
        raise RuntimeError("fixed-source bytes differ from immutable release pins")
    if {path.relative_to(RUNTIME_ROOT).as_posix() for path in SOURCE_MAP.values()} != {
        relative
        for relative in SOURCE_BUNDLE_PINS
        if relative.endswith((".txt", ".html"))
    }:
        raise RuntimeError("fixed-source routing does not cover the exact pinned texts")
    return actual


def _assert_release_target_bundle() -> Dict[str, Dict[str, Any]]:
    actual: Dict[str, Dict[str, Any]] = {}
    for relative, pin in TARGET_BUNDLE_PINS.items():
        path = PROJECT_ROOT / relative
        try:
            info = path.lstat()
        except OSError as error:
            raise RuntimeError(f"pinned P14.2 target is missing: {relative}") from error
        if not stat.S_ISREG(info.st_mode) or stat.S_ISLNK(info.st_mode):
            raise RuntimeError(f"pinned P14.2 target must be a regular non-symlink file: {relative}")
        actual[relative] = {"bytes": info.st_size, "sha256": _sha256_file(path)}
    if actual != TARGET_BUNDLE_PINS:
        raise RuntimeError("P14.2 target bytes differ from immutable release pins")
    return actual


STATIC_MODEL_CATALOG_BASELINE = _assert_static_model_catalog()
RELEASE_SOURCE_BASELINE = _assert_release_source_bundle()
RELEASE_TARGET_BASELINE = _assert_release_target_bundle()

if HOST_STATEMENT != (PROJECT_ROOT / "target/STATEMENT.tex").read_text(encoding="utf-8"):
    raise SystemExit("host request is not the exact pinned P14.2 statement")
if HOST_PROOF != (PROJECT_ROOT / "target/PROOF.tex").read_text(encoding="utf-8"):
    raise SystemExit("host request is not the exact pinned P14.2 proof")


def _is_strict_int(value: Any) -> bool:
    """Python booleans are not admissible JSON integer fields."""

    return type(value) is int


if _sha256_text(HOST_STATEMENT) != STATEMENT_SHA256:
    raise SystemExit("host request statement digest mismatch")
if _sha256_text(HOST_PROOF) != PROOF_SHA256:
    raise SystemExit("host request proof digest mismatch")
if HOST_REQUEST.get("statement_sha256") != STATEMENT_SHA256:
    raise SystemExit("host request recorded statement digest mismatch")
if HOST_REQUEST.get("proof_sha256") != PROOF_SHA256:
    raise SystemExit("host request recorded proof digest mismatch")


def _canonical_json_bytes(payload: Dict[str, Any]) -> bytes:
    return json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _atomic_json(path: Path, payload: Dict[str, Any], *, exclusive: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if exclusive:
        with path.open("x", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=True)
            handle.write("\n")
        return
    temporary = path.with_name(path.name + f".tmp-{os.getpid()}")
    with temporary.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=True)
        handle.write("\n")
    os.replace(temporary, path)


def _append_jsonl(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def _iter_jsonl(path: Path) -> Iterable[Dict[str, Any]]:
    if not path.exists():
        return
    with path.open("rb") as handle:
        for line_number, raw_bytes in enumerate(handle, start=1):
            if not raw_bytes.endswith(b"\n"):
                raise ValueError(f"JSONL line {line_number} lacks terminal LF")
            encoded_line = raw_bytes[:-1]
            if encoded_line.endswith(b"\r"):
                encoded_line = encoded_line[:-1]
            line = encoded_line.decode("utf-8", errors="strict")
            if not line.strip():
                raise ValueError(
                    f"JSONL line {line_number} is blank or whitespace-only"
                )
            value = _strict_json_loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"JSONL line {line_number} is not an object")
            yield value


def _require_run_id(run_id: str) -> None:
    if run_id != RUN_ID:
        raise ValueError("run_id does not match the host-bound run")


def _require_initialized() -> None:
    if PHASE != "initialized":
        raise RuntimeError(f"tool requires initialized phase; current phase is {PHASE}")


def _record_event(tool: str, detail: Optional[Dict[str, Any]] = None) -> None:
    TOOL_COUNTS[tool] = TOOL_COUNTS.get(tool, 0) + 1
    event: Dict[str, Any] = {
        "sequence": len(EVENTS) + 1,
        "timestamp_utc": _utc_now(),
        "tool": tool,
    }
    if detail:
        event["detail"] = detail
    EVENTS.append(event)
    if RUN_MEMORY_DIR.exists():
        COUNTS["events"] += 1
        _append_jsonl(
            RUN_MEMORY_DIR / CHANNEL_FILES["events"],
            {"timestamp_utc": event["timestamp_utc"], "record": event},
        )


def _persist_state() -> None:
    if not RUN_MEMORY_DIR.exists():
        return
    _atomic_json(
        STATE_PATH,
        {
            "format": "rethlas-hardened-mcp-state-v1",
            "runtime_contract_version": RUNTIME_CONTRACT_VERSION,
            "run_id": RUN_ID,
            "phase": PHASE,
            "statement_sha256": STATEMENT_SHA256,
            "proof_sha256": PROOF_SHA256,
            "meta_statement_sha256": META_STATEMENT_SHA256,
            "meta_statement_normalized_sha256": META_STATEMENT_NORMALIZED_SHA256,
            "events": EVENTS,
            "channel_counts": COUNTS,
            "tool_counts": TOOL_COUNTS,
            "queried_channels": sorted(QUERIED_CHANNELS),
            "fully_queried_channels": sorted(FULLY_QUERIED_CHANNELS),
            "validated_payload_sha256": VALIDATED_PAYLOAD_SHA256,
            "mcp_pid": os.getpid(),
            "updated_at_utc": _utc_now(),
        },
    )


def _channel_path(channel: str) -> Path:
    if channel not in CHANNEL_FILES:
        raise ValueError(f"unknown channel: {channel}")
    return RUN_MEMORY_DIR / CHANNEL_FILES[channel]


def _validate_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    errors: List[str] = []
    schema = _strict_json_loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for error in validator.iter_errors(payload):
        location = ".".join(str(part) for part in error.path)
        errors.append(f"schema error at {location or '<root>'}: {error.message}")

    report = payload.get("verification_report")
    verdict = payload.get("verdict")
    hints = payload.get("repair_hints")
    critical: List[Any] = []
    gaps: List[Any] = []
    if isinstance(report, dict):
        if isinstance(report.get("critical_errors"), list):
            critical = report["critical_errors"]
        if isinstance(report.get("gaps"), list):
            gaps = report["gaps"]
    findings = bool(critical or gaps)
    if verdict == "correct":
        if findings:
            errors.append("correct verdict is incompatible with findings")
        if hints != "":
            errors.append("correct verdict requires empty repair_hints")
    elif verdict == "wrong":
        if not findings:
            errors.append("wrong verdict requires a finding")
        if not isinstance(hints, str) or not hints.strip():
            errors.append("wrong verdict requires nonempty repair_hints")
    else:
        errors.append("verdict must be correct or wrong")
    return {"valid": not errors, "errors": errors}


def _memory_record_errors(channel: str, record: Dict[str, Any]) -> List[str]:
    schema = _strict_json_loads(MEMORY_RECORD_SCHEMA_PATH.read_text(encoding="utf-8"))
    errors: List[str] = []
    for error in Draft202012Validator(schema).iter_errors(record):
        location = ".".join(str(part) for part in error.path)
        errors.append(f"{location or '<root>'}: {error.message}")
    expected_type = {
        "statement_checks": "statement_check",
        "reference_checks": "reference_check",
    }.get(channel)
    if expected_type is None:
        errors.append(f"memory records are forbidden in channel {channel}")
    elif record.get("record_type") != expected_type:
        errors.append(f"record_type must equal {expected_type}")

    if channel == "reference_checks" and record.get("record_type") == "reference_check":
        mode = record.get("reference_mode")
        if mode == "external":
            if record.get("search_status") not in {"ok", "transport_unavailable"}:
                errors.append("external reference search_status must be ok or transport_unavailable")
            search_query = record.get("search_query")
            matching_searches = [
                event
                for event in EVENTS
                if event.get("tool") == "search_arxiv_theorems"
                and isinstance(event.get("detail"), dict)
                and isinstance(search_query, str)
                and event["detail"].get("query_sha256") == _sha256_text(search_query)
            ]
            if not matching_searches:
                errors.append("external reference record lacks its exact theorem-search event")
                bound_theorem_searches: List[Dict[str, Any]] = []
            else:
                bound_theorem_searches = [
                    event
                    for event in matching_searches
                    if event["detail"].get("status") == record.get("search_status")
                    and event["detail"].get("result_sha256")
                    == record.get("search_result_sha256")
                    and event["detail"].get("count") == record.get("search_result_count")
                ]
            if matching_searches and not bound_theorem_searches:
                errors.append("external theorem-search result binding differs from its event")
        else:
            bound_theorem_searches = []
        theorem_sequences = {
            event.get("sequence")
            for event in bound_theorem_searches
            if _is_strict_int(event.get("sequence"))
        }
        for evidence in record.get("source_evidence", []):
            if not isinstance(evidence, dict):
                continue
            source_id = evidence.get("source_id")
            if source_id not in SOURCE_MAP:
                errors.append(f"unknown source evidence id {source_id!r}")
                continue
            source_path = SOURCE_MAP[source_id]
            if evidence.get("sha256") != _sha256_file(source_path):
                errors.append(f"source evidence digest mismatch for {source_id}")
            fixed_query = evidence.get("search_query")
            matching_fixed_searches = [
                event
                for event in EVENTS
                if event.get("tool") == "search_fixed_source"
                and isinstance(event.get("detail"), dict)
                and event["detail"].get("source_id") == source_id
                and isinstance(fixed_query, str)
                and event["detail"].get("query_sha256") == _sha256_text(fixed_query)
            ]
            if not matching_fixed_searches:
                errors.append(f"source evidence for {source_id} lacks its fixed-source search")
                bound_fixed_searches: List[Dict[str, Any]] = []
            else:
                bound_fixed_searches = [
                    event
                    for event in matching_fixed_searches
                    if event["detail"].get("result_sha256")
                    == evidence.get("search_result_sha256")
                    and event["detail"].get("hits") == evidence.get("search_result_count")
                    and _is_strict_int(event.get("sequence"))
                    and any(
                        theorem_sequence < event["sequence"]
                        for theorem_sequence in theorem_sequences
                    )
                ]
            if matching_fixed_searches and not bound_fixed_searches:
                errors.append(
                    f"fixed-source search binding/order differs for {source_id}"
                )
            fixed_sequences = {
                event["sequence"] for event in bound_fixed_searches
            }
            valid_ranges: List[Tuple[int, int]] = []
            for line_range in evidence.get("line_ranges", []):
                if not isinstance(line_range, dict):
                    continue
                start_line = line_range.get("start_line")
                end_line = line_range.get("end_line")
                if (
                    not _is_strict_int(start_line)
                    or not _is_strict_int(end_line)
                    or end_line < start_line
                ):
                    errors.append(f"invalid source line range for {source_id}")
                    continue
                valid_ranges.append((start_line, end_line))
                matching_read = any(
                    event.get("tool") == "read_fixed_source_lines"
                    and isinstance(event.get("detail"), dict)
                    and event["detail"].get("source_id") == source_id
                    and event["detail"].get("start_line") == start_line
                    and event["detail"].get("end_line") == end_line
                    and _is_strict_int(event.get("sequence"))
                    and any(
                        fixed_sequence < event["sequence"]
                        for fixed_sequence in fixed_sequences
                    )
                    for event in EVENTS
                )
                if not matching_read:
                    errors.append(
                        f"source evidence range {source_id}:{start_line}-{end_line} "
                        "has no correctly ordered fixed-source read"
                    )
            if isinstance(fixed_query, str) and fixed_query:
                source_lines = read_lf_only_source_lines(source_path)
                query_lines = {
                    index
                    for index, line in enumerate(source_lines, start=1)
                    if fixed_query.casefold() in line.casefold()
                }
                if not any(
                    start <= match_line <= end
                    for start, end in valid_ranges
                    for match_line in query_lines
                ):
                    errors.append(
                        f"fixed-source query for {source_id} has no hit inside the cited ranges"
                    )
    return errors


def _canonical_finding(value: Any) -> str:
    if not isinstance(value, dict):
        raise ValueError("finding must be an object")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _persisted_findings() -> Tuple[Counter[str], Counter[str]]:
    critical: Counter[str] = Counter()
    gaps: Counter[str] = Counter()
    for channel in ("statement_checks", "reference_checks"):
        for entry in _iter_jsonl(_channel_path(channel)):
            record = entry.get("record", entry)
            if not isinstance(record, dict):
                raise ValueError("persisted memory record is not an object")
            for value in record.get("critical_errors", []):
                critical[_canonical_finding(value)] += 1
            for value in record.get("gaps", []):
                gaps[_canonical_finding(value)] += 1
    return critical, gaps


def _assert_no_dropped_findings(payload: Dict[str, Any]) -> None:
    persisted_critical, persisted_gaps = _persisted_findings()
    report = payload["verification_report"]
    final_critical = Counter(
        _canonical_finding(value) for value in report["critical_errors"]
    )
    final_gaps = Counter(_canonical_finding(value) for value in report["gaps"])
    if persisted_critical != final_critical or persisted_gaps != final_gaps:
        raise ValueError(
            "final report finding multiset differs from persisted records: "
            + json.dumps(
                {
                    "persisted_critical_errors": persisted_critical,
                    "final_critical_errors": final_critical,
                    "persisted_gaps": persisted_gaps,
                    "final_gaps": final_gaps,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )


APP = FastMCP("verification_agent")


@APP.tool(name="memory_init")
def memory_init(run_id: str, meta: Dict[str, Any]) -> Dict[str, Any]:
    global PHASE, META_STATEMENT_SHA256, META_STATEMENT_NORMALIZED_SHA256
    with LOCK:
        _require_run_id(run_id)
        if PHASE != "new":
            raise RuntimeError("memory_init must be the first and only initialization")
        if not isinstance(meta, dict):
            raise ValueError("meta must be an object")
        if set(meta) != {"statement"}:
            raise ValueError("meta keys must be exactly statement")
        statement = meta.get("statement")
        if not isinstance(statement, str):
            raise ValueError("meta.statement must be the exact statement string")
        META_STATEMENT_SHA256 = _sha256_text(statement)
        META_STATEMENT_NORMALIZED_SHA256 = _sha256_text(statement.rstrip("\n"))
        host_normalized_sha256 = _sha256_text(HOST_STATEMENT.rstrip("\n"))
        if META_STATEMENT_NORMALIZED_SHA256 != host_normalized_sha256:
            raise ValueError(
                "meta.statement differs from the host-bound statement beyond terminal newlines"
            )

        RUN_MEMORY_DIR.mkdir(parents=False, exist_ok=False)
        for filename in CHANNEL_FILES.values():
            (RUN_MEMORY_DIR / filename).touch(exist_ok=False)
        _atomic_json(
            RUN_MEMORY_DIR / "meta.json",
            {
                "run_id": RUN_ID,
                "statement": statement,
                "statement_sha256": META_STATEMENT_SHA256,
                "statement_normalized_sha256": META_STATEMENT_NORMALIZED_SHA256,
                "host_statement_sha256": STATEMENT_SHA256,
                "host_statement_normalized_sha256": host_normalized_sha256,
                "proof_sha256": PROOF_SHA256,
                "created_at_utc": _utc_now(),
            },
            exclusive=True,
        )
        PHASE = "initialized"
        _record_event(
            "memory_init",
            {
                "meta_statement_sha256": META_STATEMENT_SHA256,
                "meta_statement_normalized_sha256": META_STATEMENT_NORMALIZED_SHA256,
                "host_statement_sha256": STATEMENT_SHA256,
            },
        )
        _persist_state()
        return {
            "status": "ok",
            "run_id": RUN_ID,
            "phase": PHASE,
            "statement_sha256": META_STATEMENT_SHA256,
            "statement_normalized_sha256": META_STATEMENT_NORMALIZED_SHA256,
            "host_statement_sha256": STATEMENT_SHA256,
        }


@APP.tool(name="memory_append")
def memory_append(run_id: str, channel: str, record: Dict[str, Any]) -> Dict[str, Any]:
    with LOCK:
        _require_run_id(run_id)
        _require_initialized()
        if channel not in {"statement_checks", "reference_checks"}:
            raise ValueError("channel must be statement_checks or reference_checks")
        if not isinstance(record, dict):
            raise ValueError("record must be an object")
        if (
            channel == "reference_checks"
            and record.get("reference_mode") == "external"
        ):
            raise ValueError(
                "external reference records must use memory_append_reference"
            )
        record_errors = _memory_record_errors(channel, record)
        if record_errors:
            raise ValueError(
                "invalid memory record: "
                + json.dumps(record_errors, ensure_ascii=False)
            )
        if channel == "reference_checks":
            existing_reference_records = [
                entry.get("record")
                for entry in _iter_jsonl(_channel_path("reference_checks"))
                if isinstance(entry.get("record"), dict)
            ]
            mode = record.get("reference_mode")
            if mode == "no_external_references" and existing_reference_records:
                raise ValueError("the no-reference record must be the sole reference record")
            if mode == "external" and any(
                existing.get("reference_mode") == "no_external_references"
                for existing in existing_reference_records
            ):
                raise ValueError("an external reference cannot follow a no-reference record")
        entry = {
            "timestamp_utc": _utc_now(),
            "channel": channel,
            "record": record,
        }
        _append_jsonl(_channel_path(channel), entry)
        COUNTS[channel] += 1
        FULLY_QUERIED_CHANNELS.discard(channel)
        _record_event("memory_append", {"channel": channel, "index": COUNTS[channel]})
        _persist_state()
        return {"status": "ok", "run_id": RUN_ID, "channel": channel, "index": COUNTS[channel]}


@APP.tool(name="memory_append_reference")
def memory_append_reference(run_id: str, record: Dict[str, Any]) -> Dict[str, Any]:
    """Canonically bind and persist one external-reference audit record."""

    with LOCK:
        _require_run_id(run_id)
        _require_initialized()
        if not isinstance(record, dict):
            raise ValueError("record must be an object")
        canonical_record, binding = canonicalize_external_reference_record(
            record, EVENTS, SOURCE_MAP
        )
        record_errors = _memory_record_errors("reference_checks", canonical_record)
        if record_errors:
            raise ValueError(
                "invalid canonical external-reference record: "
                + json.dumps(record_errors, ensure_ascii=False)
            )
        existing_reference_records = [
            entry.get("record")
            for entry in _iter_jsonl(_channel_path("reference_checks"))
            if isinstance(entry.get("record"), dict)
        ]
        if any(
            existing.get("reference_mode") == "no_external_references"
            for existing in existing_reference_records
        ):
            raise ValueError("an external reference cannot follow a no-reference record")
        entry = {
            "timestamp_utc": _utc_now(),
            "channel": "reference_checks",
            "record": canonical_record,
        }
        _append_jsonl(_channel_path("reference_checks"), entry)
        COUNTS["reference_checks"] += 1
        FULLY_QUERIED_CHANNELS.discard("reference_checks")
        _record_event(
            "memory_append_reference",
            {
                "channel": "reference_checks",
                "index": COUNTS["reference_checks"],
                **binding,
            },
        )
        _persist_state()
        return {
            "status": "ok",
            "run_id": RUN_ID,
            "channel": "reference_checks",
            "index": COUNTS["reference_checks"],
            "canonical_record_sha256": binding["canonical_record_sha256"],
        }


@APP.tool(name="memory_query")
def memory_query(
    run_id: str,
    channel: str,
    contains: Optional[str] = None,
    limit: int = 1000,
    reverse: bool = False,
) -> Dict[str, Any]:
    with LOCK:
        _require_run_id(run_id)
        _require_initialized()
        if channel not in {"statement_checks", "reference_checks"}:
            raise ValueError("channel must be statement_checks or reference_checks")
        if contains is not None and not isinstance(contains, str):
            raise ValueError("contains must be null or a string")
        if not _is_strict_int(limit) or limit <= 0 or limit > 10000:
            raise ValueError("limit out of range")
        if type(reverse) is not bool:
            raise ValueError("reverse must be a strict boolean")
        all_items = list(_iter_jsonl(_channel_path(channel)))
        items = list(all_items)
        if contains:
            needle = contains.casefold()
            items = [
                item
                for item in items
                if needle in json.dumps(item, ensure_ascii=False).casefold()
            ]
        if reverse:
            items.reverse()
        items = items[:limit]
        QUERIED_CHANNELS.add(channel)
        if contains is None and not reverse and limit >= len(all_items):
            FULLY_QUERIED_CHANNELS.add(channel)
        _record_event("memory_query", {"channel": channel, "returned": len(items)})
        _persist_state()
        return {"run_id": RUN_ID, "channel": channel, "count": len(items), "items": items}


@APP.tool(name="search_arxiv_theorems")
def search_arxiv_theorems(query: str, num_results: int = 10) -> Dict[str, Any]:
    with LOCK:
        _require_initialized()
        if not query.strip():
            raise ValueError("query must be nonempty")
        if not _is_strict_int(num_results) or not 1 <= num_results <= 50:
            raise ValueError("num_results must be a strict integer from 1 to 50")
        try:
            response = requests.post(
                THEOREM_SEARCH_URL,
                json={"query": query, "task": THEOREM_SEARCH_TASK, "num_results": num_results},
                timeout=30,
            )
            response.raise_for_status()
            raw = _strict_json_loads(response.text)
            normalized = []
            if isinstance(raw, list):
                for item in raw:
                    if isinstance(item, dict):
                        normalized.append(
                            {
                                "title": str(item.get("title", "")),
                                "theorem": str(item.get("theorem", "")),
                                "arxiv_id": str(item.get("arxiv_id", "")),
                                "theorem_id": str(item.get("theorem_id", "")),
                            }
                        )
            result = {
                "status": "ok",
                "query": query,
                "count": len(normalized),
                "results": normalized,
            }
        except Exception as exc:
            result = {
                "status": "transport_unavailable",
                "query": query,
                "count": 0,
                "results": [],
                "error_type": type(exc).__name__,
            }
        result_sha256 = _sha256_bytes(_canonical_json_bytes(result))
        result["result_sha256"] = result_sha256
        _record_event(
            "search_arxiv_theorems",
            {
                "query_sha256": _sha256_text(query),
                "status": result["status"],
                "count": result["count"],
                "result_sha256": result_sha256,
            },
        )
        _persist_state()
        return result


@APP.tool(name="search_fixed_source")
def search_fixed_source(
    source_id: str,
    query: str,
    context_lines: int = 8,
    max_hits: int = 12,
) -> Dict[str, Any]:
    with LOCK:
        _require_initialized()
        _assert_release_source_bundle()
        if source_id not in SOURCE_MAP:
            raise ValueError(f"unknown fixed source: {source_id}")
        if not query.strip():
            raise ValueError("query must be nonempty")
        if (
            not _is_strict_int(context_lines)
            or not _is_strict_int(max_hits)
            or not 0 <= context_lines <= 40
            or not 1 <= max_hits <= 50
        ):
            raise ValueError("source search bounds out of range")
        path = SOURCE_MAP[source_id]
        lines = read_lf_only_source_lines(path)
        needle = query.casefold()
        hits = []
        for index, line in enumerate(lines):
            if needle not in line.casefold():
                continue
            start = max(0, index - context_lines)
            end = min(len(lines), index + context_lines + 1)
            hits.append(
                {
                    "match_line": index + 1,
                    "start_line": start + 1,
                    "end_line": end,
                    "text": "\n".join(
                        f"{line_no + 1}: {lines[line_no]}" for line_no in range(start, end)
                    ),
                }
            )
            if len(hits) >= max_hits:
                break
        result = {
            "source_id": source_id,
            "source_sha256": _sha256_file(path),
            "query": query,
            "count": len(hits),
            "hits": hits,
        }
        result_sha256 = _sha256_bytes(_canonical_json_bytes(result))
        result["result_sha256"] = result_sha256
        _record_event(
            "search_fixed_source",
            {
                "source_id": source_id,
                "query_sha256": _sha256_text(query),
                "hits": len(hits),
                "result_sha256": result_sha256,
            },
        )
        _persist_state()
        return result


@APP.tool(name="read_fixed_source_lines")
def read_fixed_source_lines(source_id: str, start_line: int, end_line: int) -> Dict[str, Any]:
    with LOCK:
        _require_initialized()
        _assert_release_source_bundle()
        if source_id not in SOURCE_MAP:
            raise ValueError(f"unknown fixed source: {source_id}")
        if (
            not _is_strict_int(start_line)
            or not _is_strict_int(end_line)
            or start_line < 1
            or end_line < start_line
            or end_line - start_line > 400
        ):
            raise ValueError("invalid source line range")
        path = SOURCE_MAP[source_id]
        lines = read_lf_only_source_lines(path)
        if start_line > len(lines):
            raise ValueError("start_line exceeds source length")
        end_line = min(end_line, len(lines))
        text = "\n".join(
            f"{line_no + 1}: {lines[line_no]}"
            for line_no in range(start_line - 1, end_line)
        )
        _record_event(
            "read_fixed_source_lines",
            {"source_id": source_id, "start_line": start_line, "end_line": end_line},
        )
        _persist_state()
        return {
            "source_id": source_id,
            "source_sha256": _sha256_file(path),
            "start_line": start_line,
            "end_line": end_line,
            "text": text,
        }


@APP.tool(name="validate_verification_output")
def validate_verification_output(run_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    global VALIDATED_PAYLOAD_SHA256
    with LOCK:
        _require_run_id(run_id)
        _require_initialized()
        if not isinstance(payload, dict):
            raise ValueError("payload must be an object")
        validation = _validate_payload(payload)
        if validation["valid"]:
            _assert_no_dropped_findings(payload)
            VALIDATED_PAYLOAD_SHA256 = _sha256_bytes(_canonical_json_bytes(payload))
        _record_event(
            "validate_verification_output",
            {"valid": validation["valid"], "payload_sha256": VALIDATED_PAYLOAD_SHA256},
        )
        _persist_state()
        return validation


@APP.tool(name="write_verification_output")
def write_verification_output(run_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    global PHASE
    with LOCK:
        _require_run_id(run_id)
        _require_initialized()
        model_catalog = _assert_static_model_catalog()
        if model_catalog != STATIC_MODEL_CATALOG_BASELINE:
            raise RuntimeError("static model catalog differs from MCP startup baseline")
        _assert_release_source_bundle()
        if COUNTS["statement_checks"] < 1:
            raise RuntimeError("at least one sequential statement check is required")
        if COUNTS["reference_checks"] < 1:
            raise RuntimeError("at least one reference or explicit no-reference check is required")
        if not {"statement_checks", "reference_checks"}.issubset(
            FULLY_QUERIED_CHANNELS
        ):
            raise RuntimeError("both finding channels must be fully queried before finalization")
        payload_sha256 = _sha256_bytes(_canonical_json_bytes(payload))
        if VALIDATED_PAYLOAD_SHA256 != payload_sha256:
            raise RuntimeError("the exact final payload was not successfully validated")
        validation = _validate_payload(payload)
        if not validation["valid"]:
            raise ValueError("invalid final payload")
        _assert_no_dropped_findings(payload)
        if OUTPUT_PATH.exists() or RECEIPT_PATH.exists():
            raise FileExistsError("one-shot output or receipt already exists")

        _atomic_json(OUTPUT_PATH, payload, exclusive=True)
        report_entry = {
            "timestamp_utc": _utc_now(),
            "channel": "verification_reports",
            "record": {
                "event_type": "final_report_written",
                "output_path": str(OUTPUT_PATH),
                "verdict": payload.get("verdict"),
                "payload_sha256": payload_sha256,
            },
        }
        _append_jsonl(_channel_path("verification_reports"), report_entry)
        COUNTS["verification_reports"] += 1
        PHASE = "finalized"
        _record_event("write_verification_output", {"payload_sha256": payload_sha256})
        _persist_state()

        receipt = {
            "format": "rethlas-hardened-completion-receipt-v1",
            "runtime_contract_version": RUNTIME_CONTRACT_VERSION,
            "release_pinset_sha256": EXPECTED_RELEASE_PINSET_SHA256,
            "release_pins_file_sha256": EXPECTED_RELEASE_PINS_FILE_SHA256,
            "model_catalog_runtime_path": MODEL_CATALOG_RELATIVE_PATH,
            "model_catalog_sha256": model_catalog["sha256"],
            "model_catalog_model": model_catalog["model"],
            "model_catalog_reasoning_effort": model_catalog["reasoning_effort"],
            "run_id": RUN_ID,
            "nonce": NONCE,
            "statement_sha256": STATEMENT_SHA256,
            "proof_sha256": PROOF_SHA256,
            "meta_statement_sha256": META_STATEMENT_SHA256,
            "meta_statement_normalized_sha256": META_STATEMENT_NORMALIZED_SHA256,
            "payload_sha256": payload_sha256,
            "output_file_sha256": _sha256_file(OUTPUT_PATH),
            "output_path": str(OUTPUT_PATH),
            "phase": PHASE,
            "events": EVENTS,
            "channel_counts": COUNTS,
            "tool_counts": TOOL_COUNTS,
            "queried_channels": sorted(QUERIED_CHANNELS),
            "fully_queried_channels": sorted(FULLY_QUERIED_CHANNELS),
            "mcp_pid": os.getpid(),
            "mcp_runtime_sha256": _sha256_file(Path(__file__).resolve()),
            "canonical_reference_sha256": _sha256_file(CANONICAL_REFERENCE_PATH),
            "schema_sha256": _sha256_file(SCHEMA_PATH),
            "memory_record_schema_sha256": _sha256_file(MEMORY_RECORD_SCHEMA_PATH),
            "memory_files_sha256": {
                path.name: _sha256_file(path)
                for path in sorted(RUN_MEMORY_DIR.iterdir())
                if path.is_file()
            },
            "source_sha256": {
                source_id: _sha256_file(path) for source_id, path in SOURCE_MAP.items()
            },
            "source_bundle_sha256": {
                relative: str(pin["sha256"])
                for relative, pin in SOURCE_BUNDLE_PINS.items()
            },
            "target_bundle_sha256": {
                relative: str(pin["sha256"])
                for relative, pin in TARGET_BUNDLE_PINS.items()
            },
            "completed_at_utc": _utc_now(),
        }
        _atomic_json(RECEIPT_PATH, receipt, exclusive=True)
        return {
            "status": "ok",
            "run_id": RUN_ID,
            "output_path": str(OUTPUT_PATH),
            "receipt_path": str(RECEIPT_PATH),
            "payload_sha256": payload_sha256,
        }


def main() -> None:
    APP.run()


if __name__ == "__main__":
    main()
