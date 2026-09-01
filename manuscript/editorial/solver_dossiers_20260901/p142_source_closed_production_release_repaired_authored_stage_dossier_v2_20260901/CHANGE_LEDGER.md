# P14.2 repaired authored source stage: changed-file ledger

Date: 1 September 2026.

The immutable comparison base is the 55-row release-stage manifest whose
SHA-256 is
`2c3690aedd7e11adcb59add7570f539d01148e2c93dbe088f723860d8417dc2a`.
The repaired sibling has 56 rows. Exactly 47 old paths are byte-identical,
eight old paths change, and one path is added.

## Changed paths

- `STAGING_REPORT.md`: records the two failed audits, both repairs, the
  LF-only line convention, and the authored-stage boundary.
- `check_release.py`: incorporates separated smoke-stream validation,
  before/after process polling, terminal-observation validation, and static
  gates for the LF helper and strengthened locator.
- `run_static_model_long_smoke.py`: byte-identical to the substantively
  audited P14.8 stream/sampler repair, SHA-256
  `6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09`.
- `runtime/contract.md`: specifies the LF-only source-addressing convention,
  the strengthened DXZ range, separated stdout/stderr, the no-input PTY, and
  the terminal process-observation contract.
- `runtime/hardened_service.py`: all host fixed-source search, line-read, and
  evidence-query replay paths call the shared LF-only helper; the release
  pins and version are updated.
- `runtime/hardened_mcp.py`: all MCP fixed-source search, line-read, and
  evidence-query paths call the same local LF-only helper; the release pins
  and version are updated.
- `runtime/release_pins.py`: only the release name, canonical pinset digest,
  and first DXZ locator endpoint change. The endpoint is strengthened from
  line 448 to line 458 to include the advertised I-maximality clause.
- `tests/test_runtime.py`: incorporates the P14.8 stream/sampler regressions,
  makes only disposable mutation fixtures writable, checks the single LF
  helper, exercises search/read reconstruction on all 22 source routes, and
  authenticates all seven P14.2 locator blocks by exact digest and semantic
  tail.

## Added path

- `runtime/lf_source_lines.py`: the single byte-level source line decoder.
  Only byte `0x0a` separates lines; form-feed remains in-line.

## Preserved paths

All 39 fixed-source files, all three target files, the canonical-reference
helper, both schemas, the model catalog, and the smoke MCP are byte-identical
to the v1 authored stage. The exact list and hashes are machine-recorded in
`BYTE_PRESERVATION.json` and independently rechecked by `check_dossier.py`.

This ledger describes an authored static sibling only. It records no final
installation, smoke, service launch, production submission, receipt,
manuscript integration, inventory mutation, retirement, or Git operation.
