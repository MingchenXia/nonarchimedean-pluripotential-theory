# P14.2 V5 hostile-audit result — 9 September 2026

## Terminal outcome

- HTTP status: 200
- Verification status: final
- Verdict: wrong
- Checked proof items: 4
- Critical errors: 5
- Gaps: 6

This audit does not change the manuscript's P14.2 status or authorize a
smoke, production, or retirement claim. It supplies concrete repairs required
before a further source-stage audit.

## Frozen receipt

| File | SHA-256 |
| --- | --- |
| VERIFICATION_RUN_V5_20260909/request.json | 1061d992242d8f3c21c9dddca8a840f812ceb0908eb0377d58da53f980210cad |
| VERIFICATION_RUN_V5_20260909/response.json | 2a63d7b5eb060971450c400a93577055630c6aa8c6e2d3c724b81168f784370b |
| VERIFICATION_RUN_V5_20260909/headers.json | 0c04586b26fd531f5d16290bbbb9efe805056c8726c6c4d6144649b6cb0dd2cc |

The exact request and response are retained in VERIFICATION_RUN_V5_20260909/.

## Findings that must be repaired

1. The smoke runner itself must validate the full allowed item shape and
   lifecycle, bind MCP starts to completions, and validate root identity,
   role set, sampling cadence, and cache-horizon evidence before it records
   a passed smoke. Replaying those checks only in check_release.py is
   insufficient.
2. Replay must exact-allowlist every wrapper, including an optional pre-tool
   error record. Parsed diagnostic-bearing strings, including usage content,
   must be checked as well as raw JSON bytes so escaped forbidden text cannot
   bypass the filter.
3. Structured argument/result comparisons must preserve JSON types and
   canonical forms; ordinary Python dictionary equality incorrectly accepts
   values such as 310.0 in place of the required integer 310.
4. A renewed packet must exhibit check_release.py and the relevant regression
   tests, not merely pin their hashes. It must prove manifest authentication,
   complete inventory comparison, and file/directory read-only enforcement
   against mutable-manifest and inventory mutations.
5. The tests must include forbidden stdout/stderr content paired with a false
   zero diagnostic count, behavioral MCP form-feed/CR/vertical-tab fixtures,
   and an independent recorded-statement-digest mutation that demonstrably
   fails before the FastMCP import sentinel.

## Local evidence retained

The exact frozen candidate manifest passed SHA-256 replay. With the candidate's
pinned verification Python, its 172-test suite also passed. Those local checks
are provenance and regression evidence only; they do not cure the independent
reviewer's five critical errors or support a downstream claim.
