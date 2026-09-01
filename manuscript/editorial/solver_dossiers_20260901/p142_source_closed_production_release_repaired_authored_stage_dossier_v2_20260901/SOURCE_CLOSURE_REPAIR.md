# P14.2 LF-source and smoke-infrastructure sibling repair

Date: 1 September 2026.

## Immutable inputs and scope

This dossier is a fresh authored sibling. It does not mutate either failed
input. The P14.2 v1 authored manifest has SHA-256
`4007c71e7ac04f02ac92ac90cda83c7142389a29835ac428f612d183271720a0`;
its independent audit returned
`FAIL_SOURCE_CLOSURE_LINE_NUMBERING`. The P14.8 smoke-repair authored
manifest has SHA-256
`bea75f18d2b5f765d07439c19189fa203b7a7f772a7dff9cd09c1d1d65721a30`;
its independent audit returned
`FAIL_NOT_READY_FOR_FINAL_PATH_SMOKE` because the source tree was writable
and its mutation fixtures did not work once the tree was frozen.

The target statement, proof, and example, all 39 fixed-source files, and the
prior mathematical-audit bindings are byte-preserved. This repair changes no
mathematical target and makes no new mathematical claim.

## The line-separator defect and its repair

The five P14.2 text extractions are intentionally normalized by appending one
LF byte to their immutable raw bytes. Each therefore ends in `0a 0c 0a`.
The v1 locator ledger was numbered with LF as the only separator, while both
runtime implementations used Python `str.splitlines()`, which also treats the
embedded form-feed byte `0x0c` as a separator. The failed audit consequently
found advertised semantic tails outside six runtime reads.

The sibling defines one release-local helper,
`runtime/lf_source_lines.py::read_lf_only_source_lines`. It reads bytes,
splits only on byte `0x0a`, removes only the empty chunk created by a terminal
LF, and then decodes each remaining chunk as UTF-8 with replacement. A
form-feed, carriage return, vertical tab, or any other character remains
inside its LF-delimited line.

Every fixed-source addressing operation in both independent implementations
uses that helper:

- host fixed-source search;
- host fixed-source line read;
- host evidence-query replay;
- MCP fixed-source search;
- MCP fixed-source line read;
- MCP evidence-query validation.

There are exactly three helper call sites in each implementation and no use of
`str.splitlines()` remains in either host or MCP source-addressing code. The
same LF-only convention governs search results, line reads, locator replay,
and exact content assertions for all 22 searchable routes, not only the five
new routes.

Under that single convention the inherited P14.2 locators are semantically
complete except for the first DXZ range. That range is strengthened from
`437--448` to `437--458`, so the same exact read now includes the advertised
I-maximality clause at its tail. Formula (28) remains `848--880`; its last
branch is present under LF-only numbering. The complete immutable map is:

| route | LF-only ranges |
|---|---|
| `mp_2409_06221v2` | `413--423` |
| `dxz_2302_02541v3` | `437--458`, `848--880`, `873--925` |
| `darvas_xia_2003_04818` | `1055--1185` |
| `del_math0002035` | `596--613` |
| `xia_2312_17150v3` | `628--647` |

The suite authenticates each of the seven blocks by exact SHA-256 and by its
advertised semantic tail. It separately performs search and read
reconstruction against a hard-coded content anchor for every one of the 22
routes. A synthetic separator fixture proves that only LF splits while
form-feed, carriage return, and vertical tab remain in-line.

## Preserved source normalization

The frozen source augmentation at
`/private/tmp/p142_source_augmentation_20260901` remains unmodified. Its
manifest SHA-256 is
`f64f4d05cafb3dff687b05dfc2f6d4917032d89d4f008fcebb7000e8b99f8739`.
For each text, the release bytes still equal the corresponding augmentation
bytes followed by exactly one `0a`; all PDFs remain exact copies.

| source | raw bytes / SHA-256 | release bytes / SHA-256 |
|---|---|
| MP | 209,776 / `0445ccf2c4474b6576a8053d0c7c038ffbd72c2ab27bb3d5704b90dd0e5beb62` | 209,777 / `724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d` |
| DXZ | 141,745 / `7d5a061d240096139e6302c2b4da2e9c125a8839730fc90909c1488baa446244` | 141,746 / `3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9` |
| Darvas--Xia | 182,599 / `584f24a0760cbf074fbf4c3fe9c08cfa8c33df2021fde4278c9926952267805a` | 182,600 / `794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed` |
| DEL | 61,146 / `04f029bd7a50e5d47ae75ced56f65bde2e59a8d421bd3204713fd6137d11f065` | 61,147 / `0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3` |
| Xia | 73,721 / `c75572e06a2df8cb9dbd76726678a52db5e79587ec568df41f4886e3e4ee8005` | 73,722 / `a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d` |

The DEL quasi-psh interface remains the explicit local reduction already
audited as correct: add bounded smooth strictly psh perturbations on a
relatively compact coordinate ball, apply the printed psh theorem, and use
invariance of multiplier ideals under locally bounded additions.

## Smoke runner and checker repair

The sibling incorporates the substantively audited P14.8 runner repair. The
new runner SHA-256 is
`6898ef6e8789620dafb5ade3b694f82157a3ef11325ae50670c84aaa2ffc8c09`.
It keeps stdout JSONL separate from stderr, supplies a dedicated no-input PTY
instead of piped stdin, and polls the root process before and after each
bounded process scan. The release checker validates strict stdout JSONL,
anchored pinned stderr warning classes, live identity and role binding,
cadence, cache horizon, and a terminal observation. Its narrowly specified
terminal handling admits one empty or same-PID zombie observation after the
fully bound live pre-horizon evidence and transcript-bound completion; it
does not relax any target, source, model, identity, role, cadence, TTL, or
horizon gate.

The P14.8 regression inventory is merged into the P14.2 suite, including
separated-stream replay, optional-stdin banner rejection, no-input PTY
construction, poll-before/after enforcement, terminal empty/zombie handling,
wrong-PID rejection, and the pre/post-completion cache-horizon cases. The
independently audited identity, role, and cadence validators remain in the
release checker unchanged except for the narrowly additive terminal-state
logic.

## Read-only staging repair

Mutation tests copy the stage into a disposable temporary directory and make
only that copy writable: directories `0755`, regular files `0644`, with mode
changes performed without following symlinks. The authored sibling itself is
frozen with every directory exactly `0555` and every regular file exactly
`0444`.

The top checker asserts those modes before and after checking, fingerprints
the entire regular tree, and runs the complete 163-test suite twice directly
from the exact frozen `release_stage` using `-B` and
`PYTHONDONTWRITEBYTECODE=1`. It rejects any byte, mode, cache, special-file,
artifact, or smoke-tree mutation.

## Byte ledger and boundary

Against the 55-row v1 release manifest, 47 old rows remain byte-identical,
eight declared control paths change, and the one LF helper path is added.
`CHANGE_LEDGER.md` and `BYTE_PRESERVATION.json` record and independently bind
that comparison.

This remains an authored source stage only. It has not been installed at a
final path, smoked, launched, submitted, integrated, used to mutate an
inventory, retired, or committed. Its required next gate is a new independent
hostile audit of these exact frozen bytes.
