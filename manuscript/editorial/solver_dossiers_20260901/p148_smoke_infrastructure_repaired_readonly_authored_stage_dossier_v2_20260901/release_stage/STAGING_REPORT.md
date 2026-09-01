# Rethlas P14.8 read-only smoke-infrastructure repaired authored source stage

Date: 1 September 2026.

## Boundary

This is a new isolated pre-smoke sibling under /private/tmp.  It preserves the
exact stream, pseudo-terminal, and process-sampler repairs of the failed
read-only v1 sibling and changes only the source-freeze boundary, its mutation
fixtures, and this report.  It has not been installed at a final release path,
smoke-run, launched as a verification service, used for a P14.8 submission, or
integrated into the live book.  It is ready only for an independent hostile
audit of its authored/static bytes and modes.

Every source-stage directory is mode `0555` and every regular file is mode
`0444`.  No file requires an execution bit: each Python entry point is invoked
through the pinned interpreter.  The hostile mutation tests copy the release
to a disposable temporary tree and make only that copy owner-writable
(`0755` directories and `0644` regular files), never following symlinks.  The
frozen source is never passed to `chmod`.  Three tests bind the exact source
modes, successful disposable mutations, source-mode invariance, and symlink
non-following.

The P14.8 target is deliberately not installed as a fixed source.  Its exact
unchanged statement/proof hashes are

- 9cd8fe1533c99d9d2de9e351610da4b7843d156a523d97344032cf75e3953715;
- adb2cac53f227dad668b30e054e278af0f0ac2644a597879fdb99e569dabbfd9.

## Accepted Chapter 51 dependency

The no-pluripolar-charge block is bound to production run
20260901T143740Z_9b8ffa07bc57_69cb27d9.  The run used gpt-5.6-sol at xhigh;
the host status was accepted, the verifier verdict was correct, and both the
critical-error and gap lists were empty.  The independent receipt audit has
verdict PASS.  Its machine-summary SHA-256 is
9bb022221ae30d321e00a4569bf9e2a0c19ee4252b3e26b2be7ca44c994a2930.

This exact binding applies to the isolated no-charge proof.  The present
source stage does not claim a production verdict for the P14.8 target.

## Repaired dependency packet

The fixed source id p148_ch51_dependency_v3 routes to
runtime/sources/p148_ch51_dependency_v3.txt.  The file is the exact ordered
concatenation of ten spans from a 4,516-line corrected Chapter 51 source.  It
has 784 LF-terminated lines, 34,444 bytes, and SHA-256
c2404ea689ed09cf80fb8059145bc74bab123fd39c7e1d3b70f2f37b4c484fce.

The tenth-span map and full corrected source are frozen in
/private/tmp/p148_ch51_dependency_v3_packet_20260901.  That packet manifest
has SHA-256
87ca97e402d845d4628f72d67c28e19b05674a23f3aa478be04221cecd5df0ff.

Three source-interface repairs are present:

1. the status is bound to the accepted Chapter 51 run above;
2. source lines 3288--3301 supply only the definition of
   \(P_\theta[\varphi]_{\mathcal I}\);
3. the Cantor choice is \(\ell_0=1\) and
   \(\ell_m=\mathrm e^{-4^m}\) for \(m\geq1\), with the first ratio checked
   separately.

The definition-only span has 14 lines, 420 bytes, and SHA-256
6f88ee1baa59594bb4c637cdac959842d97441dd0b303053009fce59714ee2c1.
The packet excludes the I-projection theorem beginning at source line 3303,
its proof, the zero-mass/all-mass conclusion, and every P14.8 marker.

The corrected full source differs from the accepted postimage only at lines
3775, 3776, 3784, 3785, and 3786.  Its SHA-256 is
b31c01ebe39eff954e322a5924ef5814b64337d389605ed247ddd38f71279965.
There is no line shift.

## Fixed sources and release pins

All thirty inherited r5 source files are byte-identical.  The only source
replacement is the v3 internal dependency above.  The runtime has eighteen
searchable routes and thirty-one pinned source files.  The canonical pinset
is
3f7e644253d2e77395fa17c55b8a1f8ddf4e56b07eeeeab430a6c0898ac53020,
and runtime/release_pins.py has SHA-256
eb0c0397af80a46d40837807c2e2c84272aad9d5f49fa0ba2a47000b49978645.

The already pinned Boucksom notes close the Lelong/Siu/Demailly inputs used by
the target proof.  The pinned Kellay--Mashreghi source states the generalized
Cantor logarithmic-capacity criterion as formula (3.4).  No additional
source file is needed for mathematical closure.  This does not authenticate
the exact historical page number in the Carleson citation.

All mathematical packet bytes, all thirty-one fixed-source bytes, both runtime
executables, both schemas, the static catalog, the source-pin module, the
canonical-reference module, and the smoke MCP are byte-identical to the
independently audited predecessor.  The only substantive sibling changes are
the smoke contract, runner, final-release checker, and regression tests.  Their
hashes are:

| file | SHA-256 |
|---|---|
| runtime/contract.md | fd02279e2379d505a033a38500041b1f9541f9a6daa3c55350cc135448e07abf |
| run_static_model_long_smoke.py | 6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09 |
| check_release.py | 2fcacad42bd34caca8763e80d7c326545d189d49cc70e1f4fe0b73a6a41cf356 |
| tests/test_runtime.py | 9a227222fb8528ac5d753b078c0c5f8a19937ba0543de1e48f07576c92844962 |

The runner writes strict JSONL stdout to `codex.stdout.jsonl` and writes stderr
to `codex.stderr.log`; the streams are never merged.  Stderr accepts only the
two exact timestamped state-database and shell-snapshot cleanup formats.  A
dedicated no-input pseudo-terminal prevents Codex's optional piped-stdin banner
instead of allowlisting it.  Every other stderr line, including cache/refresh,
credential, authentication, transport, TLS, websocket, and endpoint
diagnostics, fails closed.

The sampler polls before and after each `ps` scan.  All live samples retain the
old exact identity, role, cadence, elapsed-time, and horizon checks.  Exactly
one final `exited_before_scan` or `exited_during_scan` observation records a
poll/scan race; a sole same-PID `(codex)` zombie is terminal evidence rather
than a live identity mutation.  The terminal horizon bridge is accepted only
after the transcript-bound 310-second MCP completion, with a fully bound live
sample immediately before the 300-second horizon.

No earlier smoke receipt or artifact directory is present or reusable.  The
smoke MCP itself remains byte-identical to the predecessor.

## Static gates

The dependency packet checker passes.  The release pin module imports and
recomputes the canonical digest.  The service and MCP independently embed the
pinset and release-pin-file hashes.  The complete runtime test suite passed
with bytecode disabled after the byte and mode freeze:

- 161 tests twice on the frozen v2 tree; the exact elapsed times are frozen in
  the enclosing authored dossier.

The 26 tests added relative to the independently audited pre-repair release
include the inherited 23 deterministic split-stream, allowlist, PTY, process
race, and horizon fixtures, together with the three read-only-boundary tests.
The stream tests include exact allowlist rejection tests for
cache/refresh/credential/transport text, exact
rejection of `Reading additional input from stdin...`, a real PTY `isatty`
check, both sides of the poll/`ps` race, a full same-PID terminal-zombie sample
replay, and positive/negative cache-horizon bridge tests.  A throwaway in-memory
replay of the failed smoke's seven JSON records, 104 state warnings, one shell
warning, 22 live samples, and one terminal sample passes the repaired v2
validators after only stream separation, PTY-banner removal, path rebinding,
and addition of the new observation-state fields.

No symlink, special file, Python bytecode, cache directory, artifact tree, or
smoke tree is present.  The full check_release.py gate intentionally remains
unavailable until a fresh final-path 310-second smoke has been created.  A
future installer must copy this frozen source into a new installation tree,
make only that installation copy and its smoke-output location writable, and
leave this source-stage tree at its exact read-only modes.

The required next order is: independent hostile audit of these exact bytes;
installation at a new, previously nonexistent final path; exactly one fresh
final-path smoke and regenerated manifest; independent final release/receipt
audit; then, and only then, production submission of the unchanged P14.8
target.  No final installation, smoke, production call, live integration,
retirement, or git staging is authorized by this authored stage.
