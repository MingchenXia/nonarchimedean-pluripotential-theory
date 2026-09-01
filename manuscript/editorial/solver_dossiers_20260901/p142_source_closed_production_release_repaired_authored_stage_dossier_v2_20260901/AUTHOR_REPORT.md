# P14.2 LF-source-closed repaired production-release authored stage

## Verdict

`READY_FOR_INDEPENDENT_HOSTILE_AUDIT`

This is only an authored/static-stage verdict. It is not an independent audit
or a production-verification verdict and authorizes no final-path
installation, smoke, service launch, submission, live integration, inventory
mutation, retirement, or Git activity.

## Exact target and preserved mathematical evidence

The target is the exact P14.2 adaptation previously given the independent
verdict `PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET`. The statement,
proof, and example SHA-256 values are respectively

- `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`;
- `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac`;
- `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.

The candidate manifest hash is
`56e2084c2264dad4bb83f0d2bdd4e3348933002a6c9d9a6821ab02ae1686cdff`;
the prior independent mathematical-audit manifest hash is
`f5dd709eb704332eb0fb29ec730de0d9285ecf69190c07578ec89d625d9c31e3`.
All three target files, all 39 fixed-source files, and the copied prior
mathematical-audit bytes are unchanged from the failed v1 authored sibling.

Against the old 55-row release manifest, exactly 47 old rows are unchanged,
eight control paths change, and one helper path is added. The exact comparison
is recorded in `CHANGE_LEDGER.md` and `BYTE_PRESERVATION.json`.

## Failed-audit repairs

The P14.2 v1 independent audit, bound here with verdict
`FAIL_SOURCE_CLOSURE_LINE_NUMBERING`, showed that its LF-numbered locators
were replayed with Python `str.splitlines()`, which additionally splits at the
embedded terminal form-feed. The sibling now uses one explicit byte-level
LF-only helper for every fixed-source search, read, and evidence replay in
both host and MCP. Only `0x0a` separates source lines; form-feed remains
in-line. Exactly three helper calls occur in each implementation and no
generic split operation remains in host/MCP source-addressing code.

The convention is exercised on all 22 searchable routes. Every P14.2 block
has an exact digest and a semantic-tail assertion. The first DXZ locator is
strengthened from `437--448` to `437--458` so its advertised I-maximality
clause is present; the other LF-numbered ranges remain unchanged. The fixed
source augmentation itself remains byte-for-byte bound by manifest SHA-256
`f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739`.

The inherited P14.8 final-path runner was independently known to fail from
merged stderr/JSONL output and a process-exit sampling race. This sibling
merges the separately authored substantive repair: strict separated stdout
and stderr, a dedicated no-input PTY, root polling before and after each
bounded process scan, and terminal empty/same-PID-zombie handling after fully
bound live pre-horizon evidence. The release-specific checker and tests retain
all P14.2 source, target, pin, identity, role, cadence, TTL, and horizon gates.
The repaired runner SHA-256 is
`6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09`.

The P14.8 repair audit found the executable repair sound but returned
`FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE` because its claimed frozen tree was
writable and its mutation fixtures failed after a true directory freeze.
Here only disposable mutation copies are made writable. The authored dossier
has every directory at `0555` and every regular file at `0444`; the top
checker asserts the exact modes before and after its work.

`SOURCE_CLOSURE_REPAIR.md` gives the full repair and preservation account.

## Release identity and tests

The repaired release version is
`v3.3.3-r5-p142-source-closed-lf-v2`. It binds 22 searchable routes, 39
fixed-source files, three target files, and five P14.2 locator routes. Its
canonical pinset SHA-256 is
`0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf`;
`runtime/release_pins.py` has SHA-256
`5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6`.

The 56-row release-stage manifest has SHA-256
`0269bcf8d447dc82130673e34dfe3373947d6aa9f20fcedbf594bc475d654e28`.
A complete pre-freeze run passed all 163 tests after the final source-assertion
cleanup in 22.409 seconds. The frozen top checker then runs the same 163-test
suite twice directly from the exact read-only stage with the pinned
verification Python, `-B`, and
`PYTHONDONTWRITEBYTECODE=1`. It emits each frozen run's exact timing without
mutating this dossier and reports
`PASS_FROZEN_P142_SOURCE_CLOSED_LF_V2_AUTHORED_STAGE` only after all byte,
mode, preservation, source, target, pin, contract, and test gates pass.

## Required next gate

An independent hostile auditor must inspect this exact frozen sibling. No
310-second final-path smoke has been run, no service has been launched, and no
production submission has been made. Only after a passing independent audit
may a separate release operation install a final-path copy and exercise its
one-smoke budget.
