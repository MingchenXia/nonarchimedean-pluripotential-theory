# Independent hostile audit of the Chapter 51 source-closed packet and static stage

Date: 1 September 2026.

## Verdict

**FAIL_REPAIR_REQUIRED.**  Neither frozen artifact may be used for final-path
installation, final-path smoke, or production submission.  This verdict does
not reject the Chapter 51 mathematical target.  Exact target preservation,
the DDNL import boundary, the internal proof boundary, source line contents,
and the hardened host/MCP byte bindings passed.  Three finite infrastructure
and provenance blockers remain.

## Audited objects and boundaries

The audited authored objects are:

1. `/private/tmp/ch51_npp_ledger_comprehensive_production_packet_v1_20260901`;
2. `/private/tmp/rethlas_hardened_v3_3_3_r5_ch51_npp_ledger_v2_source_closed_stage_20260901`.

I treated all author reports as untrusted.  I did not install either object,
run a final-path smoke, submit a production request, edit a live manuscript or
inventory, or perform a git operation.  The only executions were read-only
checkers, source extraction to stdout, and the static unit suite with `-B` and
`PYTHONDONTWRITEBYTECODE=1`.

## Blocker 1: two extraction commands are false

ID: `SOURCE_EXTRACTION_MODE_MISDECLARED`.

Both copies of `SOURCE_ROUTES.json` say that the BEGZ and Bedford--Taylor text
files were extracted with plain `pdftotext`.  Re-extraction from the exact
pinned PDFs proves otherwise:

| source | declared command | plain bytes / SHA-256 | `-layout` bytes / SHA-256 | recorded pre-normalization SHA-256 |
|---|---|---|---|---|
| BEGZ arXiv:0812.3674v2 | `pdftotext` | 123,642 / `51410bdbf39ac3e3c36b5b3f953325a5e81cbdb424c9046d0b1d6414e1eac697` | 163,107 / `890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7` | `890173e309165984432e7326d13b7e096662cc805fbc19045a297f12211254c7` |
| Bedford--Taylor 1982 | `pdftotext` | 67,569 / `b90db94a1d308e526b1b08bf20536e1ff4f79b29a012658c84379f44a591a83a` | 83,498 / `716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b` | `716a2e1012a35ab6811873bc9f84d981627b7d6f4d9e6e4c8d48b0b525460d8b` |

The DDNL route correctly declares `pdftotext -layout` and reproduces raw hash
`c46d0c5d9ef56e4788337baef00e53bd099f130cf13913cd94b1ba19e9c5004f`.
For all three sources, the bundled text is exactly the actual `-layout` output
followed by one LF byte.  Thus the PDF pins, bundled text pins, normalization,
routed LF line numbers, and routed line contents are sound; the two extraction
mode declarations are the defect.  The authored checkers do not reproduce the
declared command and therefore miss it.

## Blocker 2: declared LF routes and runtime tool lines diverge

ID: `LF_ROUTE_AND_RUNTIME_LINE_NUMBERING_DIVERGE`.

`SOURCE_ROUTES.json` declares “one-based inclusive ranges in the pinned
UTF-8/LF text files.”  The contract repeats those ranges.  But both host and
MCP implement fixed-source search and read with Python `str.splitlines()`.
That method treats each PDF form-feed byte as another line boundary, whereas
the declared LF convention does not.  Replaying both conventions gives:

| anchor | LF line | host/MCP `splitlines()` line |
|---|---:|---:|
| DDNL first “less singular than” definition line | 62 | 63 |
| DDNL Theorem 1.1 | 81 | 82 |
| BEGZ Definition 1.1 | 211 | 215 |
| Bedford--Taylor Theorem 6.9 | 1107 | 1131 |

This is not cosmetic.  The contract tells the verifier to read
Bedford--Taylor lines 1104--1118, but the tool returns those numbers under the
`splitlines()` convention, so that read ends thirteen tool lines before
Theorem 6.9.  The unit suite itself stores pairs called `lf_line_number` and
`runtime_line_number`, thereby documenting the shift, but never requires the
runtime to implement the route contract or checks that every contracted range
contains its cited anchor.

## Blocker 3: the stage reuses a runner with a frozen failed smoke

ID: `KNOWN_FAILED_FINAL_PATH_SMOKE_RUNNER_REUSED`.

The stage's `run_static_model_long_smoke.py` has SHA-256
`5a8f25b6851667d284d84bd8874fdfcdeb640f51380727a95a72eb9991b10c78`.
It is byte-identical to the runner in the P14.8 retry1 final release whose one
and only final-path smoke has a frozen binary `FAIL` dossier.  The copied
failure record is included as `P148_FAILED_SMOKE_RESULT.json`.

The code still writes stdout and stderr to one purported JSONL file through
`stderr=subprocess.STDOUT`.  The failed run showed exact state-database and
shell-snapshot warnings interleaved after lifecycle JSON.  The code also
samples only under `while process.poll() is None`; the failed run's first
post-horizon sample occurred after root exit and saw the same PID as `(codex)`,
so the bound live roles disappeared.  These are the documented
`RAW_LIFECYCLE_NON_JSON_INTERLEAVING` and
`TERMINAL_PROCESS_SAMPLE_EXIT_RACE` blockers, not a speculative concern.

The stage is static-only, so no smoke should have been run during authoring.
But an independent static audit cannot authorize installing a byte-identical
runner already known to fail the next mandatory gate.

## Gates that passed

- Both top SHA-256 ledgers reproduce exactly: packet
  `145f6305a0ea847c176e1cd55d8da46977d8c2545c873d792a6c1ba5f7a18d71`,
  stage
  `9a227d3c7bf256d97dc9a361b63bf06d4633b463916d60b08326a27ba92950b1`.
  Their inventories equal their regular-file trees, excluding only each
  ledger itself.  Both JSON manifests reproduce file sizes and hashes.
- The packet checker passed twice, and the stage checker passed twice, under
  the pinned verification venv with bytecode disabled.
- The complete 135-test runtime suite passed twice with zero failures and zero
  errors, in 17.138 and 16.293 seconds.  The runs created no `__pycache__`,
  `.pyc`, `.pytest_cache`, smoke directory, artifact directory, request,
  receipt, or production output in either audited object.
- The statement and proof remain byte-identical through the v2 candidate,
  packet, packet exact-source copies, stage targets, and stage fixed-source
  copies.  Their hashes are respectively
  `9ff17ccf6ecafdaedf746e8472671bbd9436cf5661667e27815e1a1d39698575`
  and
  `187ef5530c9baf375cab4d15108a4447f3ddb3cc4c0b2780a7bf8d7cd2f33d70`.
- Proof lines 317--327 are the sole imported substantive theorem.  Under the
  declared LF convention, DDNL lines 62--65 give the less-singular orientation
  and lines 81--86 state Theorem
  1.1.  Adjoining `n-p` smooth Kähler entries gives the stated `p<n`
  specialization.  Statement lines 1--150 and Proof lines 51--316 and
  328--420 remain explicitly internal.  The theorem statement at Proof lines
  1--49 is read as part of the exact proof field under the contract and is not
  silently treated as an external result.
- Under the declared LF convention, the BEGZ and Bedford--Taylor ranges contain the cited local definition,
  Kiselman example, basic properties, compact-Kähler finiteness, closedness,
  modification formula, capacity definition, and capacity-zero
  characterization.  No routed line interval is out of bounds.
- The canonical release pinset independently recomputes to
  `c731c6d278c9fe905d1d4d109b46b9a01181c2bb146f6eef3a010d0b0d3063d0`.
  All twenty searchable text/HTML/TeX routes cover exactly the searchable
  members of the thirty-four-file pinned source bundle.  Host and MCP bind
  the pinset and pin-module file separately, reject mutation, missing, extra,
  symlinked, and cross-wired sources, and reconstruct fixed-source searches
  and reads from the frozen bytes.
- Diffing the host and MCP against the immediately preceding r5 runtime shows
  only the expected pin hashes, release-version strings, and addition of TeX
  as a searchable suffix.  No source-query bypass or mathematical scope
  inflation was introduced.  The target does not absorb any open-problem
  retirement.

## Required sibling repair

1. Leave both audited objects unchanged.  In new sibling artifacts, change
   the BEGZ and Bedford--Taylor extraction fields to `pdftotext -layout`, then
   regenerate every affected route, report, manifest, and SHA ledger.  Extend
   the checker to execute each declared extraction mode against the pinned PDF
   and compare the raw hash before applying the one-LF normalization.
2. Make line numbering single-valued.  The least disruptive repair is an
   explicit LF-only decoder/splitter used by host reconstruction and both MCP
   fixed-source tools; update every other fixed-source replay path to use the
   same helper.  Alternatively, repin every route and contract range to the
   form-feed-aware tool convention.  In either case, add regression tests that
   each exact contracted range contains its cited anchor, especially
   Bedford--Taylor Theorem 6.9.
3. Build the sibling stage from the independently audited repaired smoke
   infrastructure, separating JSON stdout from classified stderr and removing
   the post-exit role-sampling race without weakening the 300-second live
   horizon.  Preserve the exact Chapter 51 target and all source pins.
4. Obtain a fresh independent static audit of that sibling.  Only after it
   passes may a new final path be installed and smoked exactly once.  A passed
   smoke and independent final-release audit are still required before any
   production submission.
