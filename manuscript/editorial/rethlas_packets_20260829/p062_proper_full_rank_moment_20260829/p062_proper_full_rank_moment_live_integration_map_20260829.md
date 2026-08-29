# P06.2 proper full-rank moment factor: live-integration record

Date: 29 August 2026

The exact theorem and proof and the audited surrounding blocks were promoted
to the live manuscript on 29 August 2026.  The anchor instructions below
preserve the pre-promotion copy map as an audit trail.  The unrestricted
P06.2 atom remains open.

## 1. Exact-byte and activation gate

The only theorem bytes authorized by the production verdict are the existing
frozen files:

- `p062_proper_full_rank_moment_statement_20260829.tex`, SHA-256
  `75e9cb498ce4cb7b036f8a15f7da87b187c189e2bb1566aa7bda9027b947327c`;
- `p062_proper_full_rank_moment_proof_20260829.tex`, SHA-256
  `0ed2c67ee5120b044bef273f75f11f45d8a04577cd385da1069d9e6f1d01a440`.

Production Rethlas run `20260829T031126Z_75e9cb498ce4`, checked item
`pi_f96fe9f8904943602779f274`, returned final `correct`, with zero critical
errors and zero gaps, for those exact bytes.  The live integration should
therefore use two `\input` commands.  It must not paste, restyle, rename, or
otherwise rewrite the statement or proof.  In particular:

- keep the proposition without an optional or conventional name;
- keep every `\label`, `\eqref`, and `\cref` byte-for-byte;
- keep `\mathrm d'\mathrm d''` in the frozen files, as required by their
  production convention;
- use the live-book macros `\rd`, `\rmi`, `\rme`, and
  `\dprimeddprime` only in new surrounding prose;
- do not fold the automatic-calibration corollary into the principal
  proposition; and
- retain both scope firewalls: the theorem requires one proper full-rank
  moment factor, and the unrestricted arbitrary-continuous problem is open.

The live targets had the following SHA-256 values at this read-only audit:

- `parts/part2/ch18_delta_forms.tex`:
  `e9fae7228751ed8e7273487bda62232117a260c29046bb542cedea08cc6dbd20`;
- `parts/part6/ch72_major_open_problems.tex`:
  `bb599ef3711cb09f110ce45a0f97ba7bcbc790ac0652f2135a1f49d75a5a0a4c`;
- `editorial/open_problem_atomic_inventory_20260824.md`:
  `11d011e591139f1f8d7a8b462134e64d2f6c1afd64641240ab646142e68955af`;
- `appendices/appL_provenance.tex`:
  `245254d56133387a713502dfc35397fa7bda5cab6ee17f89f0d1f74c6196f699`.

These hashes are audit anchors, not an instruction to overwrite later
independent edits.

## 2. Primary technical home: Chapter 18

The natural primary home is `parts/part2/ch18_delta_forms.tex`, in
`\section{Harmonic tropicalizations}` and
`\subsection{Harmonic PL functions}`.  Insert the staged file
`p062_proper_full_rank_moment_ch18_insertion_20260829.tex` immediately after
the source paragraph ending “the proof neither pulls back a CLD current nor
uses a target-side cutoff to avoid the image of the boundary” (present line
3560), and immediately before

```tex
\begin{warning}{The continuous zero-current problem}
```

This position is load-bearing: it follows
`\cref{prop:ch18-real-pl-zero-current-harmonic}` and its source audit, and it
lets the warning summarize both bounded results before the next subsection
develops the tropical-image calibration.  Replace the existing warning by
the copy-ready warning in the ancillary-update file.  The staged insertion
contains only bridge prose and `\input` commands, so the verified statement
and proof remain exact.

The following Chapter 18 consistency updates are natural but ancillary and
must be applied as individual blocks, not by inputting the whole staging
file:

1. replace the continuous zero-current warning at present lines 3562–3575;
2. add the factor-scope row after the “real-PL zero-current converse” row in
   the hypothesis ledger (present lines 4589–4593);
3. add the factor-scope row after the zero-current row in the comparison
   ledger (present lines 4622–4625);
4. add the source-note paragraph after the real-PL source paragraph (present
   lines 4643–4647); and
5. optionally narrow the prose at present lines 3876–3880 from “arbitrary
   continuous function” to “arbitrary continuous function outside the
   proper full-rank factor scope.”

Copy-ready versions are in
`p062_proper_full_rank_moment_ch18_ancillary_updates_20260829.tex`.

Chapter 69, `parts/part6/ch69_verified_extensions.tex`, is a defensible
secondary home because it collects verified book-level deductions and
already uses calibrated proper pushforward.  If house policy requires that
home, the least disruptive alternative anchor is immediately before
`\section{Three definitions of PL plurisubharmonicity}` (present line 1424).
Do not place a second copy there if Chapter 18 is used.  The Chapter 18 home
is preferred because it keeps the zero-current theorem, its warning, its
moment-factor exception, and the harmonic-tropicalization discussion in one
logical sequence.

## 3. Chapter 72 frontier narrowing

In `parts/part6/ch72_major_open_problems.tex`, the exact insertion point is
inside `\subsection{Pluriharmonic regularity}`, after the historical
real-PL receipt paragraph ending

```tex
None of these three historical proofs is used.
```

(present line 1426).  Replace the following paragraph beginning “The
continuous problem in ... remains open” and ending at the Wanner curve
cross-reference (present lines 1428–1434) with the first block of
`p062_proper_full_rank_moment_ch72_narrowing_20260829.tex`.

Replace the local status summary beginning “Thus the real-PL subproblem ...”
(present lines 1464–1467) with the second block of that file.  In the chapter
closing status list, a short factor-scope bullet may also be inserted before
the existing smooth-proper-curve regularization bullet (present lines
2425–2428 in the audited snapshot).  That copy-ready item is Block 3 of the
same staging file.

The Chapter 72 wording must say all of the following:

- the factor theorem covers `h=\varphi\circ F`, not arbitrary continuous
  `h`;
- `F` is a proper full-rank pleasant moment with full nonempty connected open image;
- the principal proposition assumes the constant multiplicity calibration;
- boundarylessness makes that calibration automatic only through the
  separately proved corollary;
- the proof uses `F_*[h]=m[\varphi]`, not a pullback of an arbitrary current
  to curves; and
- P06.2 remains open without this factorization/properness/full-image
  package.

Because this integration adds a 29 August production gate, change only the
verification-record date at present line 8 from 28 to 29 August 2026.  Keep
the literature cutoff at 24 August 2026.

## 4. Atomic-inventory narrowing

The heading
`prob:frontier-pluriharmonic --- 2 atoms` remains unchanged.  P06.2 remains
one active tier-T2 atom; no atom count, tier count, or queue position changes.
Replace only the P06.2 bullet at present lines 129–132 and add the exact scope
paragraph staged in
`p062_proper_full_rank_moment_inventory_narrowing_20260829.md`.

The status is “open after the weakly smooth, real-PL, proper full-rank
moment-factor, and smooth-proper-curve cases,” not “resolved,” “conditional,”
or “retired.”  The retained target is the arbitrary continuous function that
need not admit any moment factorization.

Change only the inventory date at present line 3 from 28 to 29 August 2026.
Keep the literature cutoff at 24 August 2026 and keep the T2 queue at present
lines 515–517 unchanged.

## 5. Provenance appendix

For a full live integration, `appendices/appL_provenance.tex` should record
the production gate without changing the open-problem count:

- add the 29 August receipt paragraph after the real-PL receipt paragraph
  ending at present line 162;
- add a provenance record after the real-PL record ending at present line
  1148; and
- narrow the first item in “Questions not promoted to theorems” at present
  lines 1434–1442, while keeping the arbitrary continuous problem open.

Copy-ready blocks are staged in
`p062_proper_full_rank_moment_appL_narrowing_20260829.tex`.  If that appendix
is updated, change “verifications through 28 August” at present line 1426 to
“verifications through 29 August”; the count of 54 active atoms remains
unchanged.

## 6. Bibliography and source-key ledger

No bibliography entry is needed.  The frozen theorem and proof use only keys
already in `bibliography/NonArchimedean.bib`:

| Key | Existing entry | Use in the frozen proof |
|---|---:|---|
| `GR25Classical` | present line 109 | terminal classical pluriharmonicity |
| `CLD25` | present line 272 | moments, calibration, integration, currents, Euclidean Hessian, Poincaré–Lelong |
| `GJR26` | present line 414 | terminal harmonicity and real-PL closure |

The surrounding Chapter 72 curve comparison also uses the existing key
`Wanner19` (present line 379).  Chapter 72's final reading note already cites
`CLD25`, `GJR26`, `GR25Classical`, and `Wanner19` at present lines 2439–2440.

## 7. Label and cross-reference ledger

The following new labels are confined to the frozen packet and had no live
collision at this audit:

- theorem environments:
  `prop:p062-proper-full-rank-moment`,
  `cor:p062-proper-full-rank-moment-automatic-calibration`;
- scope and boundary remarks:
  `rem:p062-proper-full-rank-moment-scope`,
  `rem:p062-proper-full-rank-moment-boundary-audit`;
- enumerated hypotheses:
  `itm:p062-moment:image`, `itm:p062-moment:proper`,
  `itm:p062-moment:calibration`;
- statement equations:
  `eq:p062-moment-explicit-pushforward-calibration`,
  `eq:p062-moment-full-image`, `eq:p062-moment-constant-calibration`,
  `eq:p062-moment-zero-current`, `eq:p062-moment-affine-target`,
  `eq:p062-moment-affine-source`;
- proof equations:
  `eq:p062-moment-signed-pullback`,
  `eq:p062-moment-sign-calibration`, `eq:p062-moment-test-support`,
  `eq:p062-moment-pushforward-current-pairing`,
  `eq:p062-moment-pushforward-current`,
  `eq:p062-moment-target-zero-pushforward`,
  `eq:p062-moment-target-zero-current`,
  `eq:p062-moment-unit-zero-current`, `eq:p062-moment-cell-weight`, and
  `eq:p062-moment-facet-balance`.

Existing cross-references that should remain in the surrounding live prose
are:

- `prob:frontier-pluriharmonic`;
- `prop:ch18-real-pl-zero-current-harmonic`;
- `cor:ch19-continuous-zero-current-harmonic`;
- `def:ch16-harmonic-function` and `sec:ch16-harmonic-ambiguity`;
- `sec:ch18-harmonic-trop-def` and `ex:ch18-harmonic-ordinary`.

The P21.3 continuous-CLD-psh classification is not a converse for arbitrary
continuous zero-current functions and must not be cited as one.  The only
bridge in this packet is the exact Euclidean pushforward identity followed by
the CLD Euclidean Hessian/convexity recognition step.
