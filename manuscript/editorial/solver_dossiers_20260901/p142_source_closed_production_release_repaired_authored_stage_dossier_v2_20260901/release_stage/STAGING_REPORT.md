# Rethlas v3.3.3-r5-p142-source-closed-lf-v2 repaired authored source stage

Date: 1 September 2026.

## Boundary

This is an isolated authored/static source stage under `/private/tmp`. It has
not been installed at a final release path, launched as a production service,
submitted for production verification, integrated into the live manuscript or
open-problem inventory, or committed to Git. No smoke or production artifact
tree is present. Its sole current status is ready for an independent hostile
audit of these exact frozen bytes.

The mathematical target, all 39 fixed-source files, all three target files,
the model catalog, schemas, canonical-reference helper, and smoke MCP are
byte-identical to the frozen P14.2 v1 authored stage. Transcript binding,
immutable model-catalog selection, source-result recomputation, host memory
replay, receipt reconstruction, and process-group cleanup are retained.

The inherited smoke runner was independently known to fail after its one
final-path smoke because it merged stderr into JSONL stdout and stopped
sampling across the terminal process-exit race. This sibling incorporates the
separately authored P14.8 repair: strict stdout JSONL and stderr artifacts are
separate, a dedicated no-input PTY suppresses the piped-stdin prelude, the
runner polls before and after each process scan, and the checker handles one
terminal empty or same-PID zombie observation without weakening the live
identity, role, cadence, or cache-horizon gates. The P14.8 independent audit
found those executable repairs substantively sound but rejected its writable
source modes and mutation harness. This sibling also repairs that later
finding: mutation tests make only their disposable copies writable, while the
authored dossier itself is frozen read-only and checked by exact mode.

The inherited `p148_ch51_dependency_v3` route remains bound to accepted
Chapter 51 production run `20260901T143740Z_9b8ffa07bc57_69cb27d9`; the host status was accepted, the verifier verdict was correct, and its independent
receipt audit passed. This inherited source is not an acceptance record for
the P14.2 target.

## Audited target identity

The target comes from
`/private/tmp/p142_live_adapted_candidate_v1_frozen_20260901`. That frozen
candidate's `SHA256SUMS` has SHA-256
`56e2084c2264dad4bb83f0d2bdd4e3348933002a6c9d9a6821ab02ae1686cdff`.
Its independent hostile-audit dossier has `SHA256SUMS` SHA-256
`f5dd709eb704332eb0fb29ec730de0d9285ecf69190c07578ec89d625d9c31e3`
and binary verdict `PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET`.

The exact adapted files are materialized without byte changes as
`target/STATEMENT.tex`, `target/PROOF.tex`, and `target/EXAMPLE.tex`:

| target | bytes | SHA-256 |
|---|---:|---|
| statement | 3,518 | `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2` |
| proof | 7,938 | `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac` |
| example | 1,460 | `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f` |

The example is also byte-identical to the canonical example. The canonical
pre-adaptation statement and proof hashes remain
`488868dc2b2d1d62b23864970f8bf36acc0a6c7c85d27eaf66e6a9ed7120c949`
and `bf991c724e138626fbd8fcd4fc6f613d7979f3bf75a3614c569a1ff3c7d21e21`.

## Source closure

The fixed augmentation is
`/private/tmp/p142_source_augmentation_20260901`. Its `SHA256SUMS` has
SHA-256
`f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739`;
its locator ledger has SHA-256
`cd4b22d20ed46661032f9ef3f0c18782b84e23dad0b35d2650946effb04640c7`.
All five PDFs are byte-identical to the augmentation. Each extracted text in
the augmentation ended in a form-feed byte without terminal LF. The authored
release copy appends exactly one LF and changes no preceding byte. Four
additional text/PDF pairs were added for MP, Darvas--Xia,
Demailly--Ein--Lazarsfeld, and Xia. The authored release locator for DXZ was
strengthened beyond the initial augmentation ledger by adding lines 848--880,
which contain the cited transition formula (28) and its scope. This v2 sibling
further closes the first DXZ route through lines 457--458, where I-maximality
is stated. The frozen DXZ source bytes themselves were not changed.

The immutable P14.2 routes and locators are:

| route | fixed locator |
|---|---|
| `mp_2409_06221v2` | lines 413--423: Definition 1.3.1, tropical spectrum, extended values, pointwise topology |
| `dxz_2302_02541v3` | lines 437--458, 848--880, and 873--925: relative test curves through I-maximality, formula (28) transition, and Definition 3.3 inverse system |
| `darvas_xia_2003_04818` | lines 1055--1185: compact Kähler pseudoeffective framework, Definition 2.12, Proposition 2.18(ii) |
| `del_math0002035` | lines 596--613: Theorem 2.6(ii), analytic subadditivity |
| `xia_2312_17150v3` | lines 628--647: formula (3.8), raw multiplier-ideal transform and projective comparison |

These locators close imported definitions and source interfaces only. They do
not purport to source the candidate's mesh upper-semicontinuity proof or a
Mesquita--Piccione positivity theorem. This firewall is explicit in the
runtime contract and tested statically.

DEL Theorem 2.6(ii) is printed for psh weights. The contract transparently
closes the target's quasi-psh use by the standard local argument: on a
relatively compact chart add a bounded smooth strictly psh function large
enough to make both weights psh, apply the theorem, and remove the bounded
perturbations using invariance of multiplier ideals under locally bounded
additions.

All 22 source routes now use one shared release-local byte decoder in both the
MCP and the host reconstruction. Only byte `0x0a` separates lines. Form-feed
byte `0x0c` and every other separator recognized by Python's generic
`splitlines()` remain inside their containing line. The seven P14.2 locator
blocks are asserted by exact block SHA-256 as well as by every semantic tail
identified in the failed audit. A separate all-route test executes search and
read reconstruction against a hard-coded content anchor in each of the 22
searchable sources.

The normalized release text hashes are MP
`724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d`,
DXZ `3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9`,
Darvas--Xia
`794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed`,
DEL `0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3`,
and Xia `a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d`.

## Immutable release pins and service/MCP contract

The release contains 22 searchable routes, 39 fixed source files, 3 pinned
target files, and 5 pinned P14.2 locator routes. The canonical pinset SHA-256
is
`0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf`.
`runtime/release_pins.py` has SHA-256
`5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6`.

The host service and MCP independently embed and verify both values. Both
independently verify the complete source inventory and all three target
files. The host admits only a request whose statement and proof are
byte-for-byte equal to the pinned materializations; the MCP repeats that gate
against the host-authored request. Completion receipts additionally bind the
three target digests. The example is pinned contextual material and is not
silently added to either verification input.

Changed control hashes are:

| file | SHA-256 |
|---|---|
| `runtime/hardened_service.py` | `4bd4dfec62f7b0b66c7a05a930420187add85e544e6d87cc2cf122bc22a83b8a` |
| `runtime/hardened_mcp.py` | `c7a6931309c41e7b694797082633a7ad11b26704b1c375bf6b07de7e44328f98` |
| `runtime/lf_source_lines.py` | `85237a0918dfe538ab79843aac6f4514c2c0a75efbff03cbdfbb70e27d37b250` |
| `runtime/contract.md` | `87860bcbfd4336d697925a2d3867e8384e57043da12d4a9a30edfee53f68dd42` |
| `runtime/release_pins.py` | `5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6` |
| `run_static_model_long_smoke.py` | `6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09` |
| `tests/test_runtime.py` | `7b37ccc0bb4666ee313b9a087caff4c8e85d15c930c08c24490af6ad2b28452b` |
| `check_release.py` | `1778f318199267efe84ba685684baef440314f7f6c71d55ea7b68275f0de774f` |

## Static gates

The source-augmentation manifest verifies. The target files agree with the
independently audited adaptation. The release-pin module imports and
recomputes its declared canonical digest. Static tests cover the exact target
gate, independent MCP rejection of a non-pinned request, each target-byte
mutation, each source-byte mutation, route and locator contents, receipt
target hashes, and the inherited hardened runtime gates.

The complete 163-test runtime suite is run twice from the fully frozen source
tree with bytecode disabled. Exact final timings are emitted by the frozen top
checker and reported to the next auditor; no post-freeze mutation records
them.

No symlink, special file, Python bytecode, cache directory, artifact tree, or
smoke tree is permitted. `check_release.py` deliberately still requires a
fresh final-path 310-second smoke for a final release verdict; that gate has
not been run here.

The required next step is an independent hostile audit of this exact authored
source stage. Only after a passing audit may a separate operation install it
at a new final path, run the fresh smoke, and decide whether to submit the
pinned P14.2 pair. This stage itself authorizes none of those operations.
