# P14.8 smoke-infrastructure read-only repair: authored source-stage sibling v2

Date: 2026-09-01

Authored verdict: `READY_FOR_INDEPENDENT_STATIC_AUDIT`.  This is not an
independent verdict and does not authorize installation or a smoke run.

## Reason for the sibling

The preceding authored source stage has top-manifest SHA-256
`bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30`.
Its independent hostile audit, whose manifest is
`d4843c62df5c706b76bf689484b254eb84b955872117c567b2846ac4c1baac77`,
returned `FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE`: its original mode claim was
false, and six hostile mutation tests failed after its directories were made
read-only because `shutil.copytree` preserved those modes in the disposable
copies.  Neither failed frozen object was mutated.

This new sibling repairs only that read-only boundary and the associated test
harness.  Every source-stage directory is `0555`; every regular file is
`0444`.  None of the Python files has a shebang or needs an execution bit,
because each entry point is called through the pinned Python interpreter.
The top checker rejects every other mode, symlink, special file, bytecode
cache, smoke tree, or production-artifact tree.

## Repair

The sole mutation-copy helper now takes a mode snapshot of the frozen source,
copies it to a fresh `TemporaryDirectory`, rejects any attempt to thaw the
source or a descendant of it, and changes only the disposable copy to `0755`
directories and `0644` regular files.  Its two passes use `lstat` and skip
symlinks; no symlink target is passed to `chmod`.  Every hostile source or
catalog mutation fixture goes through this helper.

Three regression tests prove that:

1. all source directories and regular files have the exact frozen modes;
2. the disposable copy admits byte writes, directory and file creation,
   rename, unlink, and removal while source bytes and modes remain unchanged;
3. a disposable symlink is skipped and its external frozen target remains
   `0444`.

A future final-path installer must copy this frozen tree to a new installation
path and make only that installation copy, including its smoke-output
directory, writable.  It must not relax the source-stage modes.

## Exact byte preservation

The v2 release manifest has 44 rows and SHA-256
`837d5bb55d134bf4040c1083ffb1cf068b6b6c83bbc16bd7e86f2a1d8f247912`.
Relative to the failed v1 authored stage, 42 rows are byte-identical.  The
only substantive changes are:

| path | v1 SHA-256 | v2 SHA-256 |
|---|---|---|
| `STAGING_REPORT.md` | `7437c5c814574ea94ca8c2f9ec28066f965efbd8f8635db6277f015330e86f36` | `6eb900d5ff6612cc255b7204e1f364e19cbe05d44e80ca947aff030572487e29` |
| `tests/test_runtime.py` | `558a7068e2ebe958d7f267033642f6ea9f83e29cfad3fbfb1cbf6ab218fe4ce2` | `9a227222fb8528ac5d753b078c0c5f8a19937ba0543de1e48f07576c92844962` |

`SHA256SUMS` is the only additionally changed generated release metadata.
The stream splitter, exact stderr allowlists, dedicated no-input PTY,
poll/scan race handling, terminal-zombie rules, identity/role/cadence/TTL
gates, release checker, runtime contract, service, MCP, schemas, catalog,
canonical-reference module, smoke MCP, release pins, and all 31 fixed sources
are exact v1 bytes.

The mathematical packet is also exact.  Its manifest is
`87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff`;
the statement and proof remain respectively
`9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715`
and
`adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9`.

## Static evidence and boundary

The final inventory is 161 tests: the inherited 158 plus the three read-only
regressions.  The frozen top checker runs the complete suite twice with the
pinned verification Python and bytecode disabled, checks all exact byte and
mode ledgers, replays the failed smoke evidence under the unchanged repaired
validators, and proves that neither the release tree nor the enclosing dossier
changed.  The checker is itself run twice after the final byte and mode freeze;
its elapsed times are reported externally so that no post-freeze write is
needed.

No final path was installed.  No smoke, production request, live-book edit,
P14.8 retirement, or git operation was performed.  The next gate is a new
independent hostile audit of these exact bytes and modes.
