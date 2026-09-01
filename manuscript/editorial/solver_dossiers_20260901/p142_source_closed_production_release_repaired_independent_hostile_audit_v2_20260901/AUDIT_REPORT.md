# Independent hostile audit of the repaired P14.2 source-closed authored dossier

Date: 1 September 2026.

## Binary result

**PASS.** I found no blocker in the exact frozen dossier at
`/private/tmp/p142_source_closed_production_release_repaired_authored_stage_dossier_v2_20260901`.
The audited top `SHA256SUMS` has SHA-256
`3c72e3bac7cb2b301d895c4b5437971fb5edf26f861985e761cd2a89e5b7492d`.
This verdict is limited to the exact bytes and modes bound by that hash.

I did not install the release, run the static-model smoke, launch the service,
submit a production verification, touch the live manuscript or inventory, or
use Git.

## Frozen tree and manifests

I inspected the tree with `lstat`, never trusting candidate prose. The tree has
102 entries including its root: nine real directories and 93 regular files.
Every directory is exactly `0555`; every regular file is exactly `0444`.
There are no symlinks, special files, `__pycache__` directories, `.pyc` files,
Finder metadata, production `artifacts`, or `STATIC_MODEL_LONG_SMOKE` tree.

The canonical byte-and-mode snapshot digest is
`69c1a02599a22e51ffb972f4fd36341874c4aa005ffb465ceb91d6d32780e12f`.
An independently created `cp -a` disposable copy produced the identical
snapshot digest and identical 102-entry inventory. The same source digest was
obtained after every test and hostile-mutation run.

I parsed manifests independently, enforced terminal LF, strict row syntax,
duplicate and unsafe-path rejection, exact inventory equality, and every row
digest:

- top manifest: 92 rows, SHA-256
  `3c72e3bac7cb2b301d895c4b5437971fb5edf26f861985e761cd2a89e5b7492d`;
- release manifest: 56 rows, SHA-256
  `0269bcf8d447dc82130673e34dfe3373947d6aa9f20fcedbf594bc475d654e28`;
- frozen source-augmentation input ledger: 11 rows, SHA-256
  `f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739`.

The top and release manifests are sorted. The source-augmentation ledger keeps
its pre-existing legacy row order; it is an immutable bound input, not the
release manifest, and all 11 rows and its exact inventory verify.

## Target and source preservation

The outer and staged target copies are byte-identical and match the immutable
pins:

- `STATEMENT.tex`:
  `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`;
- `PROOF.tex`:
  `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac`;
- `EXAMPLE.tex`:
  `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.

Against the bound 55-row v1 release manifest, exactly 47 old paths are
unchanged, the eight declared control paths change, and
`runtime/lf_source_lines.py` is the sole addition. All 39 fixed-source files
and all three target files are among the 47 unchanged paths.

For each of the five augmented texts, I compared raw bytes directly. The
release text is exactly the raw input followed by one `0a` byte; each release
ends in `0a 0c 0a`. The five PDF pairs are byte-identical. Exact sizes and
hashes are recorded in `STATIC_AUDIT_EVIDENCE.json`.

## LF-only addressing, locators, and pins

The shared helper reads bytes, splits only on `0x0a`, removes only the empty
chunk caused by a terminal LF, and decodes after splitting. Neither host nor
MCP source-addressing code contains `.splitlines(`. Each has exactly three
calls to the shared helper, covering fixed-source search, line reads, and
evidence-query replay. An independent synthetic byte fixture confirmed that
form-feed, carriage return, and vertical tab remain inside an LF-delimited
line.

I recomputed all seven advertised LF-addressed locator block hashes and checked
the semantic tails, including DXZ `437--458` through “is I-maximal if” and DXZ
`848--880` through all branches of formula (28). The exact block hashes are:

- MP `413--423`: `64ed7a96232e79bb48046eadbb457d5109b85180f85c82cb22102840cd352ba9`;
- DXZ `437--458`: `ea3e5175a81fa1333e05dabd2603d08e854310abceccf655e90bc2c3a91e5d1f`;
- DXZ `848--880`: `bdd2227acada970abb87fc7a02c0ef00d1ddebed1075ce035e5479bb9e8652c4`;
- DXZ `873--925`: `ce8a48c466c99ad8d9190fa8d57c2c585f195ada9d06830a0a7667b7be26b77a`;
- Darvas--Xia `1055--1185`: `5e50e2e072684288699d9ed22e447521525ac9d502b711291ff23225e7c938c0`;
- DEL `596--613`: `c82bb610754010ef77b61d0265103fc7bb29d66ffc7e156e8b77c8886e4e577d`;
- Xia `628--647`: `a24ab4718fbc3ea3b411948c7f53010d4dedb8e404f7be414cd75740c3c97180`.

The release-pins module hash is
`5a858706ab908f5da6d6e0fc883b095202562c87bd2fb48ab8f8608e2ca714f6`.
I independently recomputed its canonical pinset hash as
`0412636c6dee5af057f0093075d85de96809719eb55c185b9409c5b71996decf`.
All 22 routes, 39 source bundle pins, and three target bundle pins resolve to
real regular files of the exact pinned sizes and hashes.

## Stdout, stderr, PTY, and process-sampling gates

No smoke was run. I audited the runner and checker statically and exercised
their regression harnesses. The runner opens separate exclusive stdout JSONL
and stderr log handles, passes a dedicated no-input PTY slave as stdin, and
polls the root process both before and after every bounded process scan. The
checker separately validates strict stdout JSONL, anchored stderr warning
classes and counts, pinned command/model/MCP identity, PID/PPID ancestry and
roles, sample cadence, the cache-horizon bracket, and exactly one final
terminal observation. It rejects a wrong terminal zombie PID and a terminal
observation before MCP completion.

The suite contains nine `SmokeProcessObservationTests` and 14
`SplitSmokeLogGateTests`. These include PTY terminal validation, the
exit-before-scan and exit-during-scan races, bound/unbound zombie cases,
poll-around-scan, terminal horizon bridges, optional-stdin banner rejection,
stdout/stderr interleaving rejection, transport/credential stderr rejection,
warning-window and warning-count gates, and path escape rejection.

## Independent tests and checker coverage

From the exact frozen disposable copy, with `-B` and
`PYTHONDONTWRITEBYTECODE=1`, I ran the full suite independently:

`Ran 163 tests in 26.137s` — `OK`.

I then ran the authored top checker from the same exact frozen copy. It ran the
complete suite twice from that copy and reported:

- `FROZEN_RUNTIME_TEST_RUN_1: 163 tests in 22.057s: PASS`;
- `FROZEN_RUNTIME_TEST_RUN_2: 163 tests in 22.426s: PASS`;
- `PASS_FROZEN_P142_SOURCE_CLOSED_LF_V2_AUTHORED_STAGE`.

I also invoked the release checker’s non-smoke manifest, catalog, release-pin,
and code-contract gates independently; all four passed. The 163-test inventory
and class counts are recorded in `TEST_EVIDENCE.json`.

## Hostile mutations

Fourteen hostile mutations were made only in independent disposable copies.
All fourteen were rejected. They cover writable-mode drift, a symlink, a FIFO,
a bytecode cache, forbidden artifact and smoke trees, fixed-source byte drift,
coherent target-plus-manifest repinning, duplicate JSON keys after top-manifest
repinning, regression to `splitlines`, merged stderr, removal of the no-input
PTY, removal of the poll-after-scan gate, and downgrade of DXZ `437--458` to
`437--448`. For stage-level static mutations I recomputed the mutable release
manifest so the intended deeper gate, rather than a stale row hash, was tested.
Exact observed gates are recorded in `HOSTILE_MUTATIONS.json`; the executable
harness is `hostile_mutations.py`.

## Boundary and conclusion

The exact frozen dossier passes this independent hostile audit with no
blockers. This is not evidence of a final-path installation or a live smoke;
those operations were expressly outside scope and were not performed.
