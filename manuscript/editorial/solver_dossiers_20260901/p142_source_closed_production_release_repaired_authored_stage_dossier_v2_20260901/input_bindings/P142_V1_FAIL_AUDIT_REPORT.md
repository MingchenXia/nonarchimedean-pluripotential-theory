# Independent hostile audit of the P14.2 source-closed authored stage

## Binary verdict

`FAIL_SOURCE_CLOSURE_LINE_NUMBERING`

The exact mathematical statement, proof, and example remain acceptable, and
the runtime hardening tests pass.  The present release stage is nevertheless
not ready for installation, smoke execution, or production submission.  Its
immutable P14.2 source locators use line numbers that do not have the semantics
of the release's own `search_fixed_source` and `read_fixed_source_lines`
tools.  Several ranges therefore fail to expose the theorem or definition
that the contract says they expose.  Independently, its smoke runner is
byte-for-byte the runner in the frozen P14.8 final-path release whose one smoke
failed on non-JSON warning interleaving and a terminal process-sampling race.

This is a source-evidence routing failure, not a reversal of the prior
mathematical audit.  No production run, final-path smoke, service launch, live
edit, inventory edit, retirement, or Git operation was performed.

## Frozen input identity

The authored dossier is
`/private/tmp/p142_source_closed_production_release_authored_stage_dossier_v1_20260901`.
Its top `SHA256SUMS` has SHA-256
`4007c71e7ac04f02ac92ac90cda83c7142389a29835ac428f612d183271720a0`.
The top manifest was checked against every listed byte both before and after
the audit.  The authored read-only checker was run twice with the pinned
verification Python, `-B`, and `PYTHONDONTWRITEBYTECODE=1`; both runs returned
`PASS_FROZEN_P142_SOURCE_CLOSED_AUTHORED_STAGE`.

The checker internally runs the 139-test suite on a writable byte-identical
copy.  In addition, the auditor made two separate writable byte-identical
copies and ran the full suite directly with the same Python and bytecode
settings.  They returned respectively:

- `Ran 139 tests in 21.859s` followed by `OK`;
- `Ran 139 tests in 21.001s` followed by `OK`.

The frozen authored tree remained read-only and acquired no bytecode cache,
artifact directory, smoke directory, or special file.

## Exact target and prior-audit bindings

The outer and staged copies are byte-identical to the previously audited
exact-live candidate:

- statement:
  `cc3f5fbdc8f4a491ca6121c0c254a20f05a0bfb6da5d91f11d6ae6e406a40bc2`;
- proof:
  `7f2ff066d1213107e5e4e4d6e3653016be3b0b5959205f689fa9131ae16a3dac`;
- example:
  `7010c2a461de6f2ed1fb7c1f0170c6eaa8aed38b88492ea919f8b0c1eea49f6f`.

The copied candidate manifest is byte-identical to the frozen candidate
manifest and has SHA-256
`56e2084c2264dad4bb83f0d2bdd4e3348933002a6c9d9a6821ab02ae1686cdff`.
The copied prior-audit manifest is byte-identical to the independent audit
manifest and has SHA-256
`f5dd709eb704332eb0fb29ec730de0d9285ecf69190c07578ec89d625d9c31e3`.
The copied prior result has verdict
`PASS_READY_FOR_SOURCE_CLOSED_PRODUCTION_PACKET`.  That verdict concerns the
mathematical/live adaptation; it does not certify the subsequently authored
source routes.

## Source-byte audit

For each of MP, DXZ, Darvas--Xia, DEL, and Xia, the release text is exactly the
corresponding frozen raw extraction followed by one byte `0a`.  Every raw text
ends in `0a 0c`; every release text ends in `0a 0c 0a`; all earlier bytes are
unchanged.  The five normalized text hashes are, in that order,

- `724926d161cb3744dd5037e259f098a944a072419176bdc3e02538a657e5c59d`;
- `3234b3366d4aa4e235c5d2581cb131c68b95cdb0b386622302b4707930ea57f9`;
- `794c9e34736334b6ba2ff01a257a916b619e9036cb02e2a2e160c494e6c358ed`;
- `0ae95d36227cc357a45b42336fdc1c28588be7163d25e160ba9e5a47bf8e81a3`;
- `a39c27332e746fa7f711718542658b1a0cfc526b8922f6f220e159089ac9562d`.

The companion PDFs are byte-identical to the augmentation inputs and have
the pinned hashes
`9eb2ea7686a5962ebc11c5eacd23b0cb3dcb081e27ac48292933f291fc82cb23`,
`7fede7c413e396008217a4a4c9638776dbdd7cacff90fdd463bf5ae48220246c`,
`a09dc667342b2ffb75ff55de9660c97f4d6238245f3e23ed3992cb2dfab79b61`,
`59219defe8729b2cd8db7e05cabec3736832e3bfd5aad4ac1b58390c801337a2`,
and
`773eea71af9f1fff112bf5fcab2b9046b81467df2e37165ee1da3949ff74c6d9`.

Thus terminal-LF normalization and all text/PDF pins pass.  The failure is in
the interpretation of line numbers, not in the source bytes.

## Blocking line-number defect

Both the MCP implementation and the host's independent reconstruction read a
fixed source with Python `str.splitlines()`.  That operation treats form-feed
(`0c`) as a line boundary.  The authored locator ledger was instead numbered
as though only LF separated lines.  Directly applying the runtime operation to
the exact normalized bytes gives the following contradictions.

- MP `413--423` ends just after the first two lines of Definition 1.3.1.  The
  valuation laws, extended values, and pointwise topology promised by the
  locator occur at runtime lines `424--431`.
- DXZ `437--448` contains the beginning of the relative-test-curve definition,
  but the terminal parameter occurs at runtime line `452` and I-maximality at
  runtime lines `465--466`.  The locator description explicitly claims both.
- DXZ `848--880` does contain the pseudoeffective transition setup and the
  label `(28)`, but it stops inside the displayed definition; its last branch
  is at runtime lines `881--883`.  The overlapping `873--925` route happens to
  supply those final lines, so the union closes formula (28), but the first
  advertised exact range is not self-contained.
- Darvas--Xia `1055--1185` contains the Section 2.4 assumptions and starts
  Proposition 2.18, but item (ii), the needed assertion
  `phi equivalent_I P[phi]_I`, is at runtime lines `1192--1193` and its proof
  ends at line `1204`.
- DEL `596--613` reaches Theorem 2.6 and the start of item (i), but the cited
  analytic subadditivity statement is item (ii) at runtime lines `616--617`.
  Consequently the exact route does not expose the theorem actually used.
- Xia `628--647` reaches the declaration of formula (3.8), but its right-hand
  side, perturbation independence, and sourced bijection are at runtime lines
  `648--657`.

The current tests only ask whether one broad needle appears somewhere in the
combined ranges for each source.  They therefore pass while failing to check
the individual semantic claims.  In particular, the DEL test accepts the
string `Theorem 2.6` without requiring item (ii), and the Darvas--Xia test
accepts Definition 2.12 without requiring Proposition 2.18(ii).

This defect is production-blocking because the contract commands the verifier
to use these exact ranges, the pinset authenticates the wrong map, and the
host receipt later treats those reads as primary-source evidence.  Search
queries remain available and the whole source files are pinned, but a verifier
should not have to discover that an immutable supposedly exact route has a
different line convention.

## Mathematical and interface audit outside the blocker

The target proof was reread in full.  The grid sandwich, arbitrary-infimum
upper semicontinuity argument, dense-left-parameter argument, extended-valued
Fekete argument, finite-ideal approximants, pseudoeffective transition
argument, and the projective-line example remain valid in the stated scope.
No positivity or MP-plurisubharmonicity is smuggled into the finite
approximants.

DEL Theorem 2.6(ii) is indeed printed only for psh weights.  The contract's
quasi-psh reduction is correct: locally add one bounded smooth strictly psh
function `rho` large enough that both weights become psh, apply subadditivity
to the perturbed weights, and remove `rho` and `2 rho` using invariance of
multiplier ideals under locally bounded additions.

The fixed-source search API exposes all five intended routes, the source and
target bundles are independently pinned by host and MCP, the host accepts
only the exact statement/proof pair, the MCP repeats that comparison against
the host-authored request, and the receipt schema binds source, target,
pinset, model, effort, statement, and proof digests.  No stale release marker,
bypass, cache/model-refresh route, authored artifact, final-path smoke, or
production receipt was found.

## Independently known smoke-infrastructure blocker

The staged `run_static_model_long_smoke.py` has SHA-256
`5a8f25b6851667d284d84bd8874fdfcdeb640f51380727a95a72eb9991b10c78`
and is byte-for-byte identical to the runner installed at
`rethlas_hardened_v3_3_3_r5_p148_retry1_final_20260901`.  The immutable failure
dossier for that exact runner has manifest SHA-256
`e7b69860f7327da9e6a375720c2f447d81eb8a7880d1bf5c415848bcbbfc708e`
and records a binary `FAIL` after its one 310-second final-path smoke.

The two reproduced defects are structural in the inherited code.  The runner
sets `stderr=subprocess.STDOUT`, while the checker forbids non-JSON lines after
the JSON lifecycle begins; the actual Codex process emitted pinned state-DB
warnings during the lifecycle and a shell-snapshot warning after completion.
The same runner samples while `process.poll() is None`, whereas the checker
requires a post-horizon sample carrying live bound Codex/host roles; the actual
terminal sample raced process exit and retained only the exited root displayed
as `(codex)`.  The frozen failure dossier identifies these as
`RAW_LIFECYCLE_NON_JSON_INTERLEAVING` and
`TERMINAL_PROCESS_SAMPLE_EXIT_RACE`.

No smoke was run in this static audit, as required.  Nevertheless, the exact
known-failing runner must not be installed merely to reproduce the already
frozen failure.  Final-path readiness is therefore independently `FAIL` even
after correcting the source locators.

## Required repair

Create a new sibling release; do not mutate this frozen stage.  Derive every
locator with the runtime's exact `splitlines()` operation.  Sufficient ranges
for the presently claimed interfaces include MP `421--431`; DXZ `441--466`,
`589--600`, and `863--901`; Darvas--Xia `1068--1204`; DEL `607--624`; and Xia
`636--657`.  The repair must update the locator ledger, contract, immutable
pinset, embedded host/MCP pin hashes, stage manifest, and tests.  Add a
regression test that requires the specific semantic needles in each
individual route, including DEL item (ii), Darvas--Xia Proposition 2.18(ii),
the complete branches of DXZ formula (28), and the RHS of Xia formula (3.8).

The same sibling must replace the inherited smoke runner/checker pair: keep
stdout JSONL separate from stderr; exact-allowlist only the pinned state-DB and
shell-snapshot warning formats without weakening cache/refresh/credential or
transport bans; and close the process-exit race without weakening the live
identity and cache-horizon gates.  Add regression tests for both frozen P14.8
failure modes.

Only after a distinct independent audit passes on that sibling may it proceed
to final-path smoke and production verification.
