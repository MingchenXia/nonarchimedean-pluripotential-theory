# P06.2 real-PL zero-current converse: live integration receipt

**Integration date:** 25 August 2026 (Asia/Shanghai)
**Status:** **REPAIRED EXACT-LIVE BYTES VERIFIED; CONTINUOUS FIREWALL RETAINED**
**Controlling production run:** `20260825T061351Z_655e7f503e5d`
**Proof item:** `pi_eea98ea0a54108cae4e076be`
**Model / scrutiny:** `gpt-5.6-sol` / `xhigh`
**Verdict:** `final/correct`, zero critical errors, zero gaps

## Superseding exact-live control

The current Chapter 18 proposition and proof are controlled by statement SHA
`655e7f503e5db0cee8e0c94fdc765b6923aeebb7b89c7b5b98ad7827fa6e2421`
and proof SHA
`7ad130bab1d9dd61ecbac818005c4b80fe405c3d9710a6bb588fea6fa30a856a`.
The request decoded byte-identically to both live slices.  The full current
receipt is
`p06_real_pl_zero_current_live_scope_arithmetic_v4_production_receipt_20260825.md`.

Everything below this paragraph records the earlier integration snapshot and
is historical where it conflicts with the superseding exact-live receipt.
In particular, run `20260825T032958Z_3a27f19be958` no longer controls the
adapted live proof.

## Historical frozen bytes

The first mathematical promotion was controlled by the following frozen exact
packet and its then-current production receipt:

| File | SHA-256 |
|---|---|
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_statement_exact_20260825.tex` | `3a27f19be9582f1082a17cbce819042f68cf5f37c8f2702fbcded89e7a616ab7` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_proof_exact_20260825.tex` | `c37af7bb8acbc388056f90ca97009f80b30cbea36ebaf10927400ef29364cbda` |
| `../rethlas_packets_20260825/p06_real_pl_zero_current_skeletal_round2_request_20260825.json` | `ab90e06b9159ca8b835b176a8c18268b9f38cd0d1df271c205a61b0d3645e851` |
| `p06_real_pl_zero_current_skeletal_round2_production_receipt.md` | `78467df82284a8769f950d7a0466693f19c4e28baf4acefa82ba65f2986efaa6` |

The live proof preserves the accepted mathematical argument.  Its editorial
changes are limited to the book's notation (`\dprimeddprime`), bibliography
keys and `\Cref`/`\eqref` references, a numbered unnamed proposition label,
and surrounding expository transitions.  This is an integration of a frozen
packet, not a post-integration byte-identity Rethlas gate.

## Live installation

| File | Lines | Bytes | SHA-256 | Integrated role |
|---|---:|---:|---|---|
| `../../parts/part2/ch18_delta_forms.tex` | 3969 | 190979 | `1d1af6b841e9bf8ca88b40b9bdeb49c355360614660f7058576a393df011c72e` | unnamed proposition `prop:ch18-real-pl-zero-current-harmonic`, full skeletal proof, continuous warning, weakly-smooth comparison, hypothesis/comparison ledgers, provenance |
| `../../parts/part2/ch19_cld_examples.tex` | 3974 | 191061 | `99ae0d5fa010c68ff6c5f4094cde7886c69a46c8f59c95a6fa6191b834b6952d` | direct Wanner consequence `cor:ch19-continuous-zero-current-harmonic` in the published smooth-proper-curve scope |
| `../../parts/part6/ch72_major_open_problems.tex` | 2190 | 107839 | `a28f1e9973a40e2abb60947459f0cee56257e64de80ff251b72ef3e6cd4d8c7e` | retires only the real-PL subproblem and retains the arbitrary continuous higher-dimensional question |

The Wanner corollary is a direct source consequence and is not represented as
part of the Rethlas-verified real-PL packet.  It assumes an algebraically
closed complete nontrivially valued field and an open subset of the
analytification of a smooth proper algebraic curve.

## Editorial records

| File | SHA-256 |
|---|---|
| `../../../RESEARCH_QUESTION_LEDGER.md` | `45cee0df47bc64beee259e0343e53af5ae34849ac1af9d50489add4d8891b54d` |
| `../major_open_problem_program.md` | `4bffb4488d78789992f5b6dfd4012c772b212dd8451bb640b0e06dde192c172` |
| `../open_problem_atomic_inventory_20260824.md` | `35f5ab5808a04b38eceee87e33af415d31a39770fa4ff821b597c512ad93db7f` |
| `../rethlas_verified_results.md` | `49192cb3e865da1c2c6a2ca04880a9524ed6f3441d9d0baabd468aa7b8d69f00` |
| `../theorem_provenance.md` | `243fffcd40357a1a48ddda740dfb39032b67c9d25ae2903fb46129672766f538` |
| `../solver_dossiers_20260825/p06_zero_current_pluriharmonic_20260825.md` | `b95def545fd64115ecd9d86fd2ba8f70f1211b2b844f9d72da36a83ffb0d571d` |
| `../../appendices/appL_provenance.tex` | `06b2a1520c426e08f7e8ac9b67ba2a573ed446e19aceee1e9b71762aa091b85f` |

## Rejection history preserved

Round one remains a negative proof object:

- run `20260825T031243Z_1603e0a83037`;
- item `pi_ef4b8ab22822f1ccc0242d30`;
- verdict `final/wrong`;
- rejection receipt SHA-256
  `3f3ef424d0dd22e33d57e4cb5355b588f86286b6378ca32b73346e022c35dd04`.

Its target-side boundary-separation argument is absent from the live proof.
All round-one response, verification, log, manifest, and guard artifacts are
retained unchanged.

## Static and focused-build checks

- `git diff --check`: passed.
- Citation keys `CLD25`, `GJR26`, `GR25Classical`, and `Wanner19`: each
  present in the live bibliography.
- Six new theorem/equation labels: each occurs exactly once.
- Focused `latexmk -pdf -interaction=nonstopmode -halt-on-error` build of
  Chapters 18, 19, and 72: exit code `0`.
- Focused PDF SHA-256:
  `0b211effdec474f1889b41b332ab30a72a5d846bcc446328b1fbb91587df0e73`.
- Focused log SHA-256:
  `adca8329d4e60b78c9da68966f58b6f7bb4efa2d1a255c925abcfa6680a0cbed`.
- A second focused Appendix L build also exited `0`; its PDF and log SHA-256
  values are, respectively,
  `e927cf3bb889881d0686a0e636d6b173da14efb78a0574851f45af2070b6279c`
  and
  `b71f1bfc18ad422ff346720790e3ef03a12d42997b65a017b4ff547445415cf8`.
- The slice intentionally omits the other chapters and therefore reports
  unresolved external cross-references.  All six labels introduced by this
  integration were emitted in the auxiliary file, the bibliography resolved,
  and the log contains no TeX error, emergency stop, fatal error, duplicate
  label, or duplicate destination.

## Scope firewall

The promoted theorem applies only to real-PL functions on the stated good,
separated, boundaryless, strict, pure-dimensional spaces.  It does not claim
that an arbitrary continuous function with zero CLD current is harmonic or
classically pluriharmonic in higher dimension.  No novelty or priority claim
is made.
