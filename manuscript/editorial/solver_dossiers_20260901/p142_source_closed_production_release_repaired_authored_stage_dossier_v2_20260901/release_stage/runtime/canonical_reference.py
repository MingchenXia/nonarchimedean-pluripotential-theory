from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Dict, List, Mapping, Sequence, Tuple


SIMPLIFIED_EXTERNAL_KEYS = {
    "location",
    "status",
    "search_query",
    "search_evidence",
    "source_evidence",
    "contextual_definition_comparison",
    "applicability",
    "critical_errors",
    "gaps",
    "detail",
}
SIMPLIFIED_SOURCE_KEYS = {
    "source_id",
    "search_query",
    "line_ranges",
    "comparison",
}
LINE_RANGE_KEYS = {"start_line", "end_line"}
CANONICAL_ONLY_KEYS = {
    "record_type",
    "reference_mode",
    "search_status",
    "search_result_sha256",
    "search_result_count",
    "sha256",
}


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _canonical_json_sha256(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _is_strict_int(value: Any) -> bool:
    return type(value) is int


def _require_exact_keys(
    value: Mapping[str, Any], expected: set[str], location: str
) -> None:
    actual = set(value)
    if actual != expected:
        added = sorted(actual - expected)
        missing = sorted(expected - actual)
        raise ValueError(
            f"{location} keys mismatch; unexpected={added}, missing={missing}"
        )


def _require_nonempty_string(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location} must be a nonempty string")
    return value


def _latest_exact_event(
    events: Sequence[Mapping[str, Any]],
    tool: str,
    predicate: Callable[[Mapping[str, Any]], bool],
    description: str,
) -> Mapping[str, Any]:
    matches = [
        event
        for event in events
        if event.get("tool") == tool
        and _is_strict_int(event.get("sequence"))
        and isinstance(event.get("detail"), dict)
        and predicate(event["detail"])
    ]
    if not matches:
        raise ValueError(f"no exact preceding {description} event")
    return max(matches, key=lambda event: int(event["sequence"]))


def canonicalize_external_reference_record(
    simplified: Mapping[str, Any],
    events: Sequence[Mapping[str, Any]],
    source_paths: Mapping[str, Path],
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Build a source-bound reference record from successful MCP events.

    The caller supplies only mathematical judgments and exact search/read
    selectors.  Result digests, result counts, transport status, and fixed
    source digests are copied or computed here and cannot be supplied by the
    model.  The returned binding is suitable for inclusion in the append
    event and independent host replay.
    """

    if not isinstance(simplified, Mapping):
        raise ValueError("record must be an object")
    _require_exact_keys(simplified, SIMPLIFIED_EXTERNAL_KEYS, "record")
    if any(key in simplified for key in CANONICAL_ONLY_KEYS):
        raise ValueError("record contains a canonical-only field")

    search_query = _require_nonempty_string(
        simplified.get("search_query"), "record.search_query"
    )
    theorem_event = _latest_exact_event(
        events,
        "search_arxiv_theorems",
        lambda detail: detail.get("query_sha256") == _sha256_text(search_query),
        "theorem search",
    )
    theorem_detail = theorem_event["detail"]
    theorem_sequence = int(theorem_event["sequence"])
    search_status = theorem_detail.get("status")
    search_result_sha256 = theorem_detail.get("result_sha256")
    search_result_count = theorem_detail.get("count")
    if search_status not in {"ok", "transport_unavailable"}:
        raise ValueError("bound theorem search has an invalid status")
    if (
        not isinstance(search_result_sha256, str)
        or len(search_result_sha256) != 64
        or any(character not in "0123456789abcdef" for character in search_result_sha256)
    ):
        raise ValueError("bound theorem search has an invalid result digest")
    if not _is_strict_int(search_result_count) or search_result_count < 0:
        raise ValueError("bound theorem search has an invalid result count")

    simplified_sources = simplified.get("source_evidence")
    if not isinstance(simplified_sources, list):
        raise ValueError("record.source_evidence must be an array")
    canonical_sources: List[Dict[str, Any]] = []
    source_bindings: List[Dict[str, Any]] = []
    for source_index, source in enumerate(simplified_sources):
        location = f"record.source_evidence[{source_index}]"
        if not isinstance(source, Mapping):
            raise ValueError(f"{location} must be an object")
        _require_exact_keys(source, SIMPLIFIED_SOURCE_KEYS, location)
        if any(key in source for key in CANONICAL_ONLY_KEYS):
            raise ValueError(f"{location} contains a canonical-only field")
        source_id = _require_nonempty_string(source.get("source_id"), f"{location}.source_id")
        if source_id not in source_paths:
            raise ValueError(f"{location}.source_id is not allowlisted")
        fixed_query = _require_nonempty_string(
            source.get("search_query"), f"{location}.search_query"
        )
        fixed_event = _latest_exact_event(
            events,
            "search_fixed_source",
            lambda detail, source_id=source_id, fixed_query=fixed_query: (
                detail.get("source_id") == source_id
                and detail.get("query_sha256") == _sha256_text(fixed_query)
            ),
            f"fixed-source search for {source_id}",
        )
        fixed_sequence = int(fixed_event["sequence"])
        if theorem_sequence >= fixed_sequence:
            raise ValueError(
                f"{location} violates theorem-search < fixed-source-search order"
            )
        fixed_detail = fixed_event["detail"]
        fixed_result_sha256 = fixed_detail.get("result_sha256")
        fixed_result_count = fixed_detail.get("hits")
        if (
            not isinstance(fixed_result_sha256, str)
            or len(fixed_result_sha256) != 64
            or any(character not in "0123456789abcdef" for character in fixed_result_sha256)
        ):
            raise ValueError(f"{location} bound search has an invalid result digest")
        if not _is_strict_int(fixed_result_count) or fixed_result_count < 0:
            raise ValueError(f"{location} bound search has an invalid hit count")

        line_ranges = source.get("line_ranges")
        if not isinstance(line_ranges, list) or not line_ranges:
            raise ValueError(f"{location}.line_ranges must be a nonempty array")
        canonical_ranges: List[Dict[str, int]] = []
        read_sequences: List[int] = []
        for range_index, line_range in enumerate(line_ranges):
            range_location = f"{location}.line_ranges[{range_index}]"
            if not isinstance(line_range, Mapping):
                raise ValueError(f"{range_location} must be an object")
            _require_exact_keys(line_range, LINE_RANGE_KEYS, range_location)
            start_line = line_range.get("start_line")
            end_line = line_range.get("end_line")
            if (
                not _is_strict_int(start_line)
                or not _is_strict_int(end_line)
                or start_line < 1
                or end_line < start_line
            ):
                raise ValueError(f"{range_location} is invalid")
            read_event = _latest_exact_event(
                events,
                "read_fixed_source_lines",
                lambda detail, source_id=source_id, start_line=start_line, end_line=end_line: (
                    detail.get("source_id") == source_id
                    and detail.get("start_line") == start_line
                    and detail.get("end_line") == end_line
                ),
                f"fixed-source read for {source_id}:{start_line}-{end_line}",
            )
            read_sequence = int(read_event["sequence"])
            if fixed_sequence >= read_sequence:
                raise ValueError(
                    f"{range_location} violates fixed-source-search < read order"
                )
            canonical_ranges.append(
                {"start_line": int(start_line), "end_line": int(end_line)}
            )
            read_sequences.append(read_sequence)

        source_path = source_paths[source_id]
        if not source_path.is_file() or source_path.is_symlink():
            raise ValueError(f"allowlisted source {source_id} is not a regular file")
        source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
        canonical_sources.append(
            {
                "source_id": source_id,
                "sha256": source_sha256,
                "search_query": fixed_query,
                "search_result_sha256": fixed_result_sha256,
                "search_result_count": fixed_result_count,
                "line_ranges": canonical_ranges,
                "comparison": copy.deepcopy(source.get("comparison")),
            }
        )
        source_bindings.append(
            {
                "source_index": source_index,
                "source_id": source_id,
                "fixed_search_sequence": fixed_sequence,
                "read_sequences": read_sequences,
            }
        )

    canonical: Dict[str, Any] = {
        "record_type": "reference_check",
        "reference_mode": "external",
        "location": copy.deepcopy(simplified.get("location")),
        "status": copy.deepcopy(simplified.get("status")),
        "search_query": search_query,
        "search_result_sha256": search_result_sha256,
        "search_result_count": search_result_count,
        "search_status": search_status,
        "search_evidence": copy.deepcopy(simplified.get("search_evidence")),
        "source_evidence": canonical_sources,
        "contextual_definition_comparison": copy.deepcopy(
            simplified.get("contextual_definition_comparison")
        ),
        "applicability": copy.deepcopy(simplified.get("applicability")),
        "critical_errors": copy.deepcopy(simplified.get("critical_errors")),
        "gaps": copy.deepcopy(simplified.get("gaps")),
        "detail": copy.deepcopy(simplified.get("detail")),
    }
    binding = {
        "theorem_search_sequence": theorem_sequence,
        "source_bindings": source_bindings,
        "canonical_record_sha256": _canonical_json_sha256(canonical),
    }
    return canonical, binding
