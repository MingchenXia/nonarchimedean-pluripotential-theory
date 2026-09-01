# Independent hostile audit of the P14.8 read-only smoke-infrastructure sibling v2

Date: 2026-09-01

Verdict: **PASS_READY_FOR_NEW_FINAL_PATH_SMOKE**.

This is an independent static and hostile audit of the exact frozen candidate
at
`/private/tmp/p148_smoke_infrastructure_repaired_readonly_authored_stage_dossier_v2_20260901`.
The candidate was never modified.  This audit did not install a final path,
run a smoke, submit a production verification, edit the book or inventory, or
perform a git operation.

## Exact object and preservation

The candidate top manifest has SHA-256
`0645efed9d2ba12a99501fe07a1988e4e7a09a20e496d21c38937774d1d29d46`.
Its release manifest has 44 rows and SHA-256
`837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912`.
The packet manifest is
`87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff`.
Every manifest row was independently rehashed and every inventory was rebuilt
from the filesystem.

The statement and proof remain respectively
`9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715`
and
`adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9`.
All 31 fixed-source rows are byte-identical to the already audited v1 release.
Of the 44 release rows, 42 are byte-identical to v1.  The only changed
substantive rows are `STAGING_REPORT.md` and `tests/test_runtime.py`; the
release manifest is regenerated metadata.  The runner, release checker,
runtime contract, hardened service, hardened MCP, schemas, static catalog,
canonical-reference module, smoke MCP, release pins, and all stream, PTY,
polling and sampler logic are exact v1 bytes.

The frozen candidate contains seven directories and seventy regular files.
Every directory is exactly `0555`, every regular file is exactly `0444`, and
there is no symlink, special file, bytecode/cache path, live smoke-output tree,
or production-artifact tree.  The historical failed-smoke snapshots are
evidence inputs, not a smoke execution in this candidate.

## Independent execution

The candidate top checker passed and, within that invocation, ran the exact
161-test suite twice in 15.193 and 15.279 seconds.  I then invoked the exact
suite directly twice from the frozen release tree with the pinned verification
interpreter and bytecode disabled; both 161-test runs passed in 15.283 and
15.601 seconds.  Thus four complete frozen-tree suite executions passed in
this audit.  Pre/post byte-and-mode fingerprints prove that these invocations
did not alter the candidate.

## Hostile matrix

An independent mutation harness made only disposable copies and established:

1. a single `0444` to `0644` mode drift is rejected immediately by the top
   checker;
2. an unmanifested contract-byte mutation is rejected by the release manifest;
3. replacing the split stderr sink by `subprocess.STDOUT` is rejected by the
   executable code-contract gate;
4. replacing `os.openpty()` by `os.pipe()` is rejected by the PTY contract;
5. deleting the disposable-copy thaw call makes the mutation regression hit
   the expected filesystem write barrier, so the helper is necessary;
6. the pristine helper refuses both its source root and every source
   descendant, while a sibling disposable copy is thawed successfully;
7. its two `lstat` passes skip a disposable symlink, leaving an external
   `0444` target byte- and mode-identical;
8. strict stdout accepts only JSONL, rejects a warning interleaved into stdout,
   and stderr accepts only the exact bounded warning forms;
9. the dedicated PTY and split-stream anchors are present in the frozen runner;
10. the pre-poll live, exit-between-polls, and pre-scan-exit cases have the
    required distinct outcomes;
11. a terminal observation after the 300-second horizon and MCP completion is
    accepted, while an early terminal bridge is rejected; and
12. a bound terminal zombie is accepted but a PID-substituted zombie is
    rejected.

All hostile cases passed, all temporary trees were removed after being made
writable, and the frozen source fingerprint was unchanged.

## Boundary

This PASS clears only the static source-stage gate.  It authorizes the owner to
install these exact bytes at one new, previously nonexistent final path and to
run one fresh long smoke there.  It is not a smoke receipt, production Rethlas
receipt, mathematical novelty certificate, live-book integration, or P14.8
retirement decision.
